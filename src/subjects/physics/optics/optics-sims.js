// Interactive Physics Simulation Engine for Optics: Wave Optics, Modern Optics, Lasers & Fourier Optics
// Implements 23 interactive Canvas simulations embedded topic-by-topic inline.

window.OPTICS_SIMS = {
  // 1. Young's Double Slit
  "young-double-slit": {
    title: "🔬 Young’s Double-Slit Dynamic Interference & Intensity Profile",
    desc: "Adjust slit separation $d$, optical wavelength $\\lambda$, and distance $D$ to observe live wave superposition, fringe spacing $\\beta = \\lambda D / d$, and irradiance intensity curves.",
    controls: [
      { id: "yd-d", label: "Slit Separation d (μm)", min: 10, max: 100, step: 2, value: 35 },
      { id: "yd-wl", label: "Wavelength λ (nm)", min: 380, max: 750, step: 5, value: 532 },
      { id: "yd-D", label: "Screen Distance D (cm)", min: 50, max: 200, step: 5, value: 100 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const d = vals["yd-d"] * 1e-6;
      const wl = vals["yd-wl"] * 1e-9;
      const D = vals["yd-D"] * 1e-2;
      const beta = (wl * D) / d; // fringe width in m

      // Wavelength to RGB color
      const rgb = wlToRGB(vals["yd-wl"]);

      // Draw Screen Fringe Pattern (top half)
      const topH = h * 0.55;
      const imgData = ctx.createImageData(w, Math.floor(topH));
      const midX = w / 2;
      const scaleX = 0.005 / w; // 5mm span

      for (let x = 0; x < w; x++) {
        const yPos = (x - midX) * scaleX;
        const delta = (2 * Math.PI * d * yPos) / (wl * D);
        const intensity = Math.pow(Math.cos(delta / 2), 2);

        for (let y = 0; y < topH; y++) {
          const idx = (y * w + x) * 4;
          imgData.data[idx] = Math.floor(rgb.r * intensity);
          imgData.data[idx + 1] = Math.floor(rgb.g * intensity);
          imgData.data[idx + 2] = Math.floor(rgb.b * intensity);
          imgData.data[idx + 3] = 255;
        }
      }
      ctx.putImageData(imgData, 0, 0);

      // Draw Intensity Curve (bottom half)
      ctx.fillStyle = "#090d16";
      ctx.fillRect(0, topH, w, h - topH);

      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(0, h - 20);
      ctx.lineTo(w, h - 20);
      ctx.stroke();

      ctx.strokeStyle = `rgb(${rgb.r}, ${rgb.g}, ${rgb.b})`;
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      const plotH = h - topH - 30;
      for (let x = 0; x < w; x++) {
        const yPos = (x - midX) * scaleX;
        const delta = (2 * Math.PI * d * yPos) / (wl * D);
        const intensity = Math.pow(Math.cos(delta / 2), 2);
        const py = h - 20 - intensity * plotH;
        if (x === 0) ctx.moveTo(x, py);
        else ctx.lineTo(x, py);
      }
      ctx.stroke();

      // Readout
      ctx.fillStyle = "#38bdf8";
      ctx.font = "12px monospace";
      ctx.fillText(`Fringe Width β = ${(beta * 1000).toFixed(3)} mm | λ = ${vals["yd-wl"]} nm | d = ${vals["yd-d"]} μm`, 12, h - 8);
    }
  },

  // 2. Young's Fringe Geometry
  "young-fringe-geometry": {
    title: "📐 Hyperbolic Wavefront Geometry & Ray Interference Tracing",
    desc: "Traces wavelets emerging from two coherent point sources, illustrating the hyperbolic loci of constant phase difference and wavefront superposition.",
    controls: [
      { id: "yfg-sep", label: "Source Separation d", min: 20, max: 80, step: 2, value: 40 },
      { id: "yfg-freq", label: "Wavenumber (Rings)", min: 5, max: 20, step: 1, value: 10 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const d = vals["yfg-sep"];
      const s1 = { x: w * 0.25, y: h / 2 - d / 2 };
      const s2 = { x: w * 0.25, y: h / 2 + d / 2 };

      // Background field
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      // Draw wavefront circles
      const numRings = vals["yfg-freq"] * 3;
      const ringSpacing = 16;
      ctx.lineWidth = 1;

      for (let r = ringSpacing; r < numRings * ringSpacing; r += ringSpacing) {
        ctx.strokeStyle = "rgba(56, 189, 248, 0.25)";
        ctx.beginPath();
        ctx.arc(s1.x, s1.y, r, -Math.PI / 2, Math.PI / 2);
        ctx.stroke();

        ctx.strokeStyle = "rgba(16, 185, 129, 0.25)";
        ctx.beginPath();
        ctx.arc(s2.x, s2.y, r, -Math.PI / 2, Math.PI / 2);
        ctx.stroke();
      }

      // Draw sources
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(s1.x, s1.y, 4, 0, Math.PI * 2); ctx.fill();
      ctx.fillText("S₁", s1.x - 20, s1.y + 4);

      ctx.fillStyle = "#10b981";
      ctx.beginPath(); ctx.arc(s2.x, s2.y, 4, 0, Math.PI * 2); ctx.fill();
      ctx.fillText("S₂", s2.x - 20, s2.y + 4);

      // Draw observation screen
      const screenX = w * 0.88;
      ctx.strokeStyle = "#94a3b8";
      ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(screenX, 20); ctx.lineTo(screenX, h - 20); ctx.stroke();
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px sans-serif";
      ctx.fillText("Screen", screenX - 18, 15);

      // Draw hyperbolic interference bands
      ctx.strokeStyle = "rgba(245, 158, 11, 0.6)";
      ctx.lineWidth = 1.5;
      for (let m = -3; m <= 3; m++) {
        ctx.beginPath();
        for (let py = 20; py < h - 20; py += 4) {
          const r1 = Math.hypot(screenX - s1.x, py - s1.y);
          const r2 = Math.hypot(screenX - s2.x, py - s2.y);
          if (Math.abs((r2 - r1) - m * ringSpacing) < 8) {
            ctx.lineTo(screenX, py);
          }
        }
        ctx.stroke();
      }
    }
  },

  // 3. Fresnel Biprism
  "fresnel-biprism": {
    title: "💎 Fresnel Biprism Virtual Source Ray Tracer & Wavelength Analyzer",
    desc: "Simulates wavefront division by a small-angle glass biprism $\\alpha$, showing formation of two virtual coherent sources $S_1, S_2$ and resulting interference fringes.",
    controls: [
      { id: "bp-alpha", label: "Refracting Angle α (arcmin)", min: 10, max: 60, step: 5, value: 30 },
      { id: "bp-u", label: "Slit-Biprism Distance u (cm)", min: 10, max: 50, step: 2, value: 25 },
      { id: "bp-n", label: "Glass Index n", min: 1.45, max: 1.70, step: 0.01, value: 1.52 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const alphaRad = (vals["bp-alpha"] / 60) * (Math.PI / 180);
      const n = vals["bp-n"];
      const dev = (n - 1) * alphaRad; // deviation angle
      const u = vals["bp-u"] * 1e-2;
      const d = 2 * u * dev; // virtual source distance in m

      ctx.fillStyle = "#0a0e1a";
      ctx.fillRect(0, 0, w, h);

      // Slit S
      const slitX = 40, slitY = h / 2;
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(slitX, slitY, 4, 0, Math.PI * 2); ctx.fill();
      ctx.fillText("Slit S", slitX - 10, slitY - 10);

      // Biprism outline
      const bpX = 180;
      ctx.fillStyle = "rgba(56, 189, 248, 0.15)";
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(bpX, 40);
      ctx.lineTo(bpX + 25, h / 2);
      ctx.lineTo(bpX, h - 40);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();
      ctx.fillText("Biprism", bpX - 10, 30);

      // Virtual sources S1, S2
      const virtSpread = (d * 1000) * 12; // graphical scale
      const s1Y = slitY - virtSpread, s2Y = slitY + virtSpread;

      ctx.fillStyle = "#ec4899";
      ctx.beginPath(); ctx.arc(slitX, s1Y, 3, 0, Math.PI * 2); ctx.fill();
      ctx.fillText("S₁ (Virtual)", slitX - 15, s1Y - 6);

      ctx.beginPath(); ctx.arc(slitX, s2Y, 3, 0, Math.PI * 2); ctx.fill();
      ctx.fillText("S₂ (Virtual)", slitX - 15, s2Y + 14);

      // Trace light rays
      ctx.strokeStyle = "rgba(245, 158, 11, 0.4)";
      ctx.lineWidth = 1;
      // Ray 1: Upper prism
      ctx.beginPath(); ctx.moveTo(slitX, slitY); ctx.lineTo(bpX + 12, h * 0.35); ctx.lineTo(w - 30, h * 0.42); ctx.stroke();
      // Ray 2: Lower prism
      ctx.beginPath(); ctx.moveTo(slitX, slitY); ctx.lineTo(bpX + 12, h * 0.65); ctx.lineTo(w - 30, h * 0.58); ctx.stroke();

      // Screen & Fringes on right
      const scX = w - 40;
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(scX, 30, 25, h - 60);

      // Draw simulated fringes inside screen
      for (let y = 35; y < h - 35; y += 4) {
        const fringeInt = 0.5 + 0.5 * Math.cos((y - h / 2) * (virtSpread * 0.15));
        ctx.fillStyle = `rgba(56, 189, 248, ${fringeInt})`;
        ctx.fillRect(scX + 2, y, 21, 3);
      }

      // Stats
      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px monospace";
      ctx.fillText(`Virtual Separation d = ${(d * 1000).toFixed(3)} mm | Deviation δ = ${(dev * 180 / Math.PI * 60).toFixed(2)}' | n = ${n.toFixed(2)}`, 20, h - 12);
    }
  },

  // 4. Lloyd's Mirror
  "lloyd-mirror": {
    title: "🪞 Lloyd’s Mirror: Grazing Incidence & π Phase Jump Verification",
    desc: "Shows direct and reflected rays producing interference fringes, demonstrating why the fringe at the mirror surface boundary ($y = 0$) is completely dark.",
    controls: [
      { id: "lm-h", label: "Source Height h (mm)", min: 1, max: 10, step: 0.5, value: 3 },
      { id: "lm-wl", label: "Wavelength λ (nm)", min: 400, max: 700, step: 10, value: 550 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = "#070c17";
      ctx.fillRect(0, 0, w, h);

      const mirrorY = h * 0.65;
      const hScale = vals["lm-h"] * 8;
      const s1X = 60, s1Y = mirrorY - hScale;
      const s2Y = mirrorY + hScale; // Virtual image

      // Draw Optical Mirror
      ctx.fillStyle = "#334155";
      ctx.fillRect(100, mirrorY, w * 0.65, 8);
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(100, mirrorY); ctx.lineTo(100 + w * 0.65, mirrorY); ctx.stroke();
      ctx.fillStyle = "#38bdf8";
      ctx.font = "11px sans-serif";
      ctx.fillText("Front Surface Mirror (Grazing Interface)", 150, mirrorY + 22);

      // Real Source S1
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(s1X, s1Y, 4, 0, Math.PI * 2); ctx.fill();
      ctx.fillText("S₁ (Real)", s1X - 20, s1Y - 10);

      // Virtual Source S2
      ctx.fillStyle = "rgba(245, 158, 11, 0.4)";
      ctx.beginPath(); ctx.arc(s1X, s2Y, 4, 0, Math.PI * 2); ctx.fill();
      ctx.fillText("S₂ (Virtual Image)", s1X - 20, s2Y + 18);

      // Screen on Right
      const scX = w - 50;
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(scX, 30, 30, mirrorY - 20);

      // Draw Ray paths
      ctx.strokeStyle = "rgba(16, 185, 129, 0.6)"; // Direct ray
      ctx.beginPath(); ctx.moveTo(s1X, s1Y); ctx.lineTo(scX, mirrorY * 0.5); ctx.stroke();

      ctx.strokeStyle = "rgba(239, 68, 68, 0.6)"; // Reflected ray
      const bounceX = 260;
      ctx.beginPath(); ctx.moveTo(s1X, s1Y); ctx.lineTo(bounceX, mirrorY); ctx.lineTo(scX, mirrorY * 0.5); ctx.stroke();

      // Draw Dark boundary fringe at y = 0
      ctx.fillStyle = "#ef4444";
      ctx.fillRect(scX, mirrorY - 3, 30, 6);
      ctx.fillStyle = "#fff";
      ctx.font = "10px sans-serif";
      ctx.fillText("Dark (Δ = λ/2)", scX - 75, mirrorY + 4);

      // Fringes on screen
      for (let y = 35; y < mirrorY - 5; y += 4) {
        const pathDiff = ((mirrorY - y) * hScale) * 0.05;
        const intVal = 0.5 + 0.5 * Math.cos(pathDiff + Math.PI); // π phase shift!
        ctx.fillStyle = `rgba(56, 189, 248, ${intVal})`;
        ctx.fillRect(scX + 2, y, 26, 3);
      }

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Boundary Phase Jump: δ = π radians (Destructive interference at contact)`, 20, h - 14);
    }
  },

  // 5. Stokes' Relations
  "stokes-reversibility": {
    title: "🔄 Stokes’ Reversibility Principle & Boundary Amplitude Relations",
    desc: "Visualizes beam splitting and its time-reversed counterpart at a planar dielectric boundary, proving $r' = -r$ and $t t' = 1 - r^2$.",
    controls: [
      { id: "st-r", label: "Amplitude Reflectance r", min: 0.1, max: 0.8, step: 0.05, value: 0.4 },
      { id: "st-rev", label: "Time Reversal Mode", min: 0, max: 1, step: 1, value: 0 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = "#080d1a";
      ctx.fillRect(0, 0, w, h);

      const midY = h / 2;
      const r = vals["st-r"];
      const t = Math.sqrt(1 - r * r);
      const isReversed = vals["st-rev"] === 1;

      // Medium 1 and Medium 2
      ctx.fillStyle = "rgba(56, 189, 248, 0.08)";
      ctx.fillRect(0, 0, w, midY);
      ctx.fillStyle = "rgba(16, 185, 129, 0.08)";
      ctx.fillRect(0, midY, w, midY);

      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(0, midY); ctx.lineTo(w, midY); ctx.stroke();

      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px sans-serif";
      ctx.fillText("Medium 1 (Rarer: n₁ = 1.0)", 16, midY - 14);
      ctx.fillText("Medium 2 (Denser: n₂ = 1.5)", 16, midY + 24);

      const midX = w / 2;

      if (!isReversed) {
        // Forward Ray
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(midX - 120, midY - 100); ctx.lineTo(midX, midY); ctx.stroke();
        ctx.fillStyle = "#f59e0b"; ctx.fillText("Incident Ray (E₀ = 1)", midX - 150, midY - 110);

        // Reflected Ray
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5 * r;
        ctx.beginPath(); ctx.moveTo(midX, midY); ctx.lineTo(midX + 120, midY - 100); ctx.stroke();
        ctx.fillStyle = "#38bdf8"; ctx.fillText(`Reflected: r = ${r.toFixed(2)}`, midX + 60, midY - 110);

        // Transmitted Ray
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5 * t;
        ctx.beginPath(); ctx.moveTo(midX, midY); ctx.lineTo(midX + 70, midY + 100); ctx.stroke();
        ctx.fillStyle = "#10b981"; ctx.fillText(`Transmitted: t = ${t.toFixed(2)}`, midX + 80, midY + 90);
      } else {
        // Reversed Rays
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(midX + 120, midY - 100); ctx.lineTo(midX, midY); ctx.stroke();
        ctx.fillText("Reversed r", midX + 90, midY - 80);

        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(midX + 70, midY + 100); ctx.lineTo(midX, midY); ctx.stroke();
        ctx.fillText("Reversed t", midX + 50, midY + 80);

        // Reconstituted Incident Ray
        ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(midX, midY); ctx.lineTo(midX - 120, midY - 100); ctx.stroke();
        ctx.fillText("Net Reconstituted: r² + tt' = 1.00", midX - 180, midY - 80);

        // Cancelled Ray in Medium 2
        ctx.strokeStyle = "#ef4444"; ctx.setLineDash([4, 4]);
        ctx.beginPath(); ctx.moveTo(midX, midY); ctx.lineTo(midX - 70, midY + 100); ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillText("Cancelled: t(r + r') = 0 => r' = -r", midX - 160, midY + 80);
      }
    }
  },

  // 6. Thin Film Anti-Reflection Coating
  "thin-film-coating": {
    title: "🌈 Thin-Film Interference & Anti-Reflection Coating Tuner",
    desc: "Calculate constructive/destructive reflected intensity as a function of coating thickness $d$, film index $n_c$, and wavelength $\\lambda$.",
    controls: [
      { id: "tf-d", label: "Film Thickness d (nm)", min: 50, max: 400, step: 5, value: 100 },
      { id: "tf-nc", label: "Coating Index nc", min: 1.2, max: 2.2, step: 0.02, value: 1.38 },
      { id: "tf-wl", label: "Wavelength λ (nm)", min: 380, max: 750, step: 5, value: 550 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const d = vals["tf-d"];
      const nc = vals["tf-nc"];
      const wl = vals["tf-wl"];
      const ng = 1.52; // crown glass

      // Reflectances at boundaries
      const r1 = (1.0 - nc) / (1.0 + nc);
      const r2 = (nc - ng) / (nc + ng);
      const phase = (2 * Math.PI / wl) * (2 * nc * d);

      // Net reflection intensity
      const rNet = (r1 * r1 + r2 * r2 + 2 * r1 * r2 * Math.cos(phase)) /
                    (1 + r1 * r1 * r2 * r2 + 2 * r1 * r2 * Math.cos(phase));
      const reflPct = rNet * 100;

      ctx.fillStyle = "#090d18";
      ctx.fillRect(0, 0, w, h);

      // Visual layers
      const layerW = w * 0.45;
      // Air
      ctx.fillStyle = "#1e293b";
      ctx.fillRect(20, 20, layerW, 50);
      ctx.fillStyle = "#94a3b8"; ctx.fillText("Air (n₀ = 1.0)", 30, 48);

      // Coating
      ctx.fillStyle = "rgba(56, 189, 248, 0.3)";
      ctx.fillRect(20, 70, layerW, 70);
      ctx.fillStyle = "#38bdf8"; ctx.fillText(`Dielectric Coating (nc = ${nc.toFixed(2)}, d = ${d} nm)`, 30, 110);

      // Substrate Glass
      ctx.fillStyle = "rgba(16, 185, 129, 0.25)";
      ctx.fillRect(20, 140, layerW, 80);
      ctx.fillStyle = "#10b981"; ctx.fillText("Glass Substrate (ng = 1.52)", 30, 180);

      // Reflectance Gauge Bar on right
      const rx = w * 0.58;
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "14px sans-serif";
      ctx.fillText("Reflected Power %:", rx, 45);

      ctx.fillStyle = "#1e293b";
      ctx.fillRect(rx, 60, w * 0.35, 30);

      ctx.fillStyle = reflPct < 1 ? "#10b981" : reflPct < 5 ? "#38bdf8" : "#f59e0b";
      ctx.fillRect(rx, 60, (w * 0.35) * (reflPct / 20), 30);

      ctx.fillStyle = "#fff";
      ctx.font = "16px monospace";
      ctx.fillText(`${reflPct.toFixed(2)}%`, rx + 10, 82);

      // Optimal AR thickness condition
      const optD = wl / (4 * nc);
      const optNc = Math.sqrt(ng);
      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px sans-serif";
      ctx.fillText(`Target AR Thickness for ${wl} nm: d_opt = ${optD.toFixed(1)} nm`, rx, 130);
      ctx.fillText(`Target Index: nc_opt = √ng = ${optNc.toFixed(2)}`, rx, 155);
    }
  },

  // 7. Newton's Rings
  "newtons-rings": {
    title: "🎯 Newton’s Rings Circular Interference Pattern & Radius Analyzer",
    desc: "Simulates Newton's rings formed by a plano-convex lens of curvature $R$ on an optical flat. Test liquid immersion ($\mu$) and wavelength adjustments.",
    controls: [
      { id: "nr-R", label: "Curvature Radius R (m)", min: 0.5, max: 3.0, step: 0.1, value: 1.5 },
      { id: "nr-wl", label: "Wavelength λ (nm)", min: 400, max: 700, step: 10, value: 589 },
      { id: "nr-mu", label: "Film Index μ (Liquid)", min: 1.0, max: 1.6, step: 0.05, value: 1.0 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const R = vals["nr-R"];
      const wl = vals["nr-wl"] * 1e-9;
      const mu = vals["nr-mu"];
      const rgb = wlToRGB(vals["nr-wl"]);

      const midX = w / 2, midY = h / 2;
      const maxR = Math.min(midX, midY) - 10;
      const imgData = ctx.createImageData(w, h);
      const scaleMeter = 0.003 / maxR; // 3mm radius window

      for (let y = 0; y < h; y++) {
        for (let x = 0; x < w; x++) {
          const dx = (x - midX) * scaleMeter;
          const dy = (y - midY) * scaleMeter;
          const rGeom = Math.sqrt(dx * dx + dy * dy);

          const airThickness = (rGeom * rGeom) / (2 * R);
          const delta = (2 * Math.PI / wl) * (2 * mu * airThickness) + Math.PI; // +π for reflection jump
          const intensity = Math.pow(Math.cos(delta / 2), 2);

          const idx = (y * w + x) * 4;
          imgData.data[idx] = Math.floor(rgb.r * intensity);
          imgData.data[idx + 1] = Math.floor(rgb.g * intensity);
          imgData.data[idx + 2] = Math.floor(rgb.b * intensity);
          imgData.data[idx + 3] = 255;
        }
      }
      ctx.putImageData(imgData, 0, 0);

      // Center dark spot label
      ctx.fillStyle = "#fff";
      ctx.font = "11px monospace";
      ctx.fillText("Central Dark Spot (r = 0, Δ = λ/2)", 15, 20);
      ctx.fillText(`R = ${R.toFixed(1)} m | μ = ${mu.toFixed(2)} | λ = ${vals["nr-wl"]} nm`, 15, h - 12);
    }
  },

  // 8. Michelson Interferometer
  "michelson-interferometer": {
    title: "🧭 Michelson Interferometer: Fringe Shift & Mirror Translation Metrology",
    desc: "Translate movable mirror $M_2$ to count shifting circular Haidinger fringes and verify sub-nanometer wavelength measuring capability.",
    controls: [
      { id: "mi-d", label: "Mirror Displacement Δd (μm)", min: 0, max: 20, step: 0.1, value: 5.0 },
      { id: "mi-wl", label: "Wavelength λ (nm)", min: 400, max: 700, step: 10, value: 632 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const d = vals["mi-d"] * 1e-6;
      const wl = vals["mi-wl"] * 1e-9;
      const fringesShifted = (2 * d) / wl;
      const rgb = wlToRGB(vals["mi-wl"]);

      const midX = w / 2, midY = h / 2;
      const imgData = ctx.createImageData(w, h);
      const maxR = Math.min(midX, midY);

      for (let y = 0; y < h; y++) {
        for (let x = 0; x < w; x++) {
          const rNorm = Math.hypot(x - midX, y - midY) / maxR;
          const theta = rNorm * 0.08; // small angle
          const delta = (4 * Math.PI * d * Math.cos(theta)) / wl;
          const intensity = 0.5 + 0.5 * Math.cos(delta);

          const idx = (y * w + x) * 4;
          imgData.data[idx] = Math.floor(rgb.r * intensity);
          imgData.data[idx + 1] = Math.floor(rgb.g * intensity);
          imgData.data[idx + 2] = Math.floor(rgb.b * intensity);
          imgData.data[idx + 3] = 255;
        }
      }
      ctx.putImageData(imgData, 0, 0);

      ctx.fillStyle = "rgba(10, 14, 26, 0.8)";
      ctx.fillRect(10, 10, 320, 50);
      ctx.fillStyle = "#38bdf8";
      ctx.font = "13px monospace";
      ctx.fillText(`Mirror Shift Δd: ${vals["mi-d"].toFixed(2)} μm`, 20, 32);
      ctx.fillText(`Fringes Shifted N = 2Δd/λ: ${fringesShifted.toFixed(2)}`, 20, 50);
    }
  },

  // 9. Fabry-Perot Etalon
  "fabry-perot-etalon": {
    title: "⚡ Fabry-Pérot Multiple-Beam Interferometer & Airy Sharpness Finesse",
    desc: "Vary surface reflectance $R$ from $0.20$ to $0.98$ to observe transformation from broad sinusoidal fringes into ultra-sharp transmission peaks governed by Airy’s formula.",
    controls: [
      { id: "fp-r", label: "Mirror Reflectance R", min: 0.1, max: 0.98, step: 0.02, value: 0.85 },
      { id: "fp-d", label: "Cavity Spacing d (mm)", min: 1, max: 10, step: 0.5, value: 5.0 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const R = vals["fp-r"];
      const F = (4 * R) / Math.pow(1 - R, 2);
      const finesse = (Math.PI * Math.sqrt(R)) / (1 - R);

      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      // Plot Airy Transmission Function IT(δ)
      const plotH = h - 70;
      ctx.strokeStyle = "#334155";
      ctx.beginPath();
      ctx.moveTo(40, plotH + 20); ctx.lineTo(w - 20, plotH + 20); ctx.stroke();

      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      const numOrders = 4;
      const xSpan = w - 60;
      for (let px = 0; px < xSpan; px++) {
        const delta = (px / xSpan) * (numOrders * 2 * Math.PI);
        const transmission = 1.0 / (1.0 + F * Math.pow(Math.sin(delta / 2), 2));
        const py = plotH + 20 - transmission * plotH;
        if (px === 0) ctx.moveTo(40 + px, py);
        else ctx.lineTo(40 + px, py);
      }
      ctx.stroke();

      // Readouts
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Reflectance R = ${R.toFixed(2)} | Finesse F = ${F.toFixed(1)} | Effective Finesse ℱ = ${finesse.toFixed(1)}`, 20, h - 20);
      ctx.fillStyle = "#10b981";
      ctx.fillText("Airy Peaks T = 1.0 (Constructive 2d cos θ = mλ)", 20, 25);
    }
  },

  // 10. Fresnel Half-Period Zones
  "fresnel-half-period-zones": {
    title: "🌐 Fresnel Half-Period Zones 3D Annular Construction",
    desc: "Visualizes concentric annular half-period zones $r_n = \\sqrt{n b \\lambda}$ with equal areas $A_n \\approx \\pi b \\lambda$ and alternating phase contributions.",
    controls: [
      { id: "hz-zones", label: "Number of Zones", min: 3, max: 15, step: 1, value: 8 },
      { id: "hz-b", label: "Distance b (cm)", min: 20, max: 100, step: 5, value: 50 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = "#080c16";
      ctx.fillRect(0, 0, w, h);

      const midX = w / 2, midY = h / 2;
      const nZones = vals["hz-zones"];
      const maxRadius = Math.min(midX, midY) - 20;

      for (let n = nZones; n >= 1; n--) {
        const r = maxRadius * Math.sqrt(n / nZones);
        ctx.fillStyle = n % 2 === 1 ? "rgba(56, 189, 248, 0.4)" : "rgba(15, 23, 42, 0.9)";
        ctx.strokeStyle = "#38bdf8";
        ctx.lineWidth = 1.5;

        ctx.beginPath();
        ctx.arc(midX, midY, r, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();

        if (n <= 5) {
          ctx.fillStyle = "#cbd5e1";
          ctx.font = "10px sans-serif";
          ctx.fillText(`Zone ${n}`, midX + r * 0.7, midY - r * 0.7);
        }
      }

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Equal Zone Area Property: A_n = π b λ = const | Exposed: ${nZones} zones`, 15, h - 14);
    }
  },

  // 11. Zone Plate Focus
  "zone-plate-focus": {
    title: "🔍 Fresnel Zone Plate Multi-Focal Diffractive Concentrator",
    desc: "Examines intensity amplification $I \\propto 4N^2 I_0$ at the primary focus $f_1 = r_1^2 / \\lambda$ and odd harmonic foci $f_3 = f_1/3, f_5 = f_1/5$.",
    controls: [
      { id: "zp-n", label: "Open Zones N", min: 5, max: 40, step: 1, value: 15 },
      { id: "zp-f", label: "Primary Focal Length f₁ (cm)", min: 10, max: 50, step: 2, value: 25 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = "#080d19";
      ctx.fillRect(0, 0, w, h);

      const N = vals["zp-n"];
      const f1 = vals["zp-f"];
      const gain = 4 * N * N;

      // Draw Zone Plate cross section on left
      const zpx = 80;
      ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(zpx, 30); ctx.lineTo(zpx, h - 30); ctx.stroke();

      for (let i = 1; i <= N; i++) {
        const yTop = h / 2 - i * 4;
        const yBot = h / 2 + i * 4;
        ctx.fillStyle = i % 2 === 0 ? "#0f172a" : "#38bdf8";
        ctx.fillRect(zpx - 4, yTop - 2, 8, 4);
        ctx.fillRect(zpx - 4, yBot - 2, 8, 4);
      }

      // Draw Converging Rays to Foci
      const f1X = zpx + (w - zpx - 60);
      const f3X = zpx + (w - zpx - 60) / 3;

      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(zpx, 40); ctx.lineTo(f1X, h / 2);
      ctx.moveTo(zpx, h - 40); ctx.lineTo(f1X, h / 2);
      ctx.stroke();

      // Primary Focal Spot
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(f1X, h / 2, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillText(`Primary Focus f₁ (${f1} cm)`, f1X - 60, h / 2 - 14);

      // Third Harmonic Focal Spot
      ctx.fillStyle = "#ec4899";
      ctx.beginPath(); ctx.arc(f3X, h / 2, 4, 0, Math.PI * 2); ctx.fill();
      ctx.fillText(`f₃ = f₁/3`, f3X - 20, h / 2 + 20);

      ctx.fillStyle = "#10b981";
      ctx.font = "13px monospace";
      ctx.fillText(`Focal Spot Intensity Amplification: I = 4N² I₀ = ${gain} × Unobstructed`, 20, h - 14);
    }
  },

  // 12. Cornu Spiral & Straight Edge
  "cornu-spiral-edge": {
    title: "🌀 Cornu Spiral & Straight-Edge Fresnel Diffraction Profile",
    desc: "Plots the Cornu clothoid curve and traces the resultant vector to show $I = 0.25 I_0$ at the geometrical edge and rapid fringe oscillations into illuminated space.",
    controls: [
      { id: "cs-v", label: "Wavefront Parameter v", min: -4.0, max: 4.0, step: 0.1, value: 1.2 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      // Draw Cornu Spiral on Left
      const midX = w * 0.35, midY = h * 0.5;
      const scale = 140;

      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (let t = -4.0; t <= 4.0; t += 0.05) {
        const pt = fresnelIntegrals(t);
        const px = midX + pt.C * scale;
        const py = midY - pt.S * scale;
        if (t === -4.0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Current Vector on Cornu Spiral
      const v = vals["cs-v"];
      const ptV = fresnelIntegrals(v);
      const zNeg = fresnelIntegrals(-4.0); // asymptotic corner (-0.5, -0.5)

      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(midX - 0.5 * scale, midY + 0.5 * scale);
      ctx.lineTo(midX + ptV.C * scale, midY - ptV.S * scale);
      ctx.stroke();

      // Draw Straight-Edge Intensity Curve on Right
      const plotX = w * 0.70;
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px sans-serif";
      ctx.fillText("Straight Edge Diffraction Profile:", plotX - 20, 30);

      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let py = 45; py < h - 45; py += 3) {
        const tv = (py - midY) / 30;
        const pt = fresnelIntegrals(tv);
        const chordSq = Math.pow(pt.C + 0.5, 2) + Math.pow(pt.S + 0.5, 2);
        const intPx = plotX + chordSq * 45;
        if (py === 45) ctx.moveTo(intPx, py);
        else ctx.lineTo(intPx, py);
      }
      ctx.stroke();

      ctx.fillStyle = "#ef4444";
      ctx.fillText("Edge (v = 0, I = 0.25 I₀)", plotX - 20, midY);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "12px monospace";
      ctx.fillText(`v = ${v.toFixed(1)} | Chord² (Intensity) = ${(Math.pow(ptV.C + 0.5, 2) + Math.pow(ptV.S + 0.5, 2)).toFixed(3)} I₀`, 15, h - 12);
    }
  },

  // 13. Poisson-Arago Spot
  "poisson-spot": {
    title: "🌕 Poisson-Arago Spot in Circular Obstacle Shadow",
    desc: "Demonstrates wave diffraction forming a bright constructive Poisson-Arago spot at the geometric center of an opaque circular disc's shadow.",
    controls: [
      { id: "ps-rad", label: "Disc Radius a (mm)", min: 1, max: 6, step: 0.5, value: 3 },
      { id: "ps-wl", label: "Wavelength λ (nm)", min: 400, max: 700, step: 20, value: 632 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const midX = w / 2, midY = h / 2;
      const discR = vals["ps-rad"] * 18;
      const rgb = wlToRGB(vals["ps-wl"]);

      const imgData = ctx.createImageData(w, h);

      for (let y = 0; y < h; y++) {
        for (let x = 0; x < w; x++) {
          const r = Math.hypot(x - midX, y - midY);
          let intensity = 0;

          if (r < discR) {
            // Inside shadow: central Arago spot!
            const j0 = Math.cos(r * 0.4);
            intensity = Math.exp(-r * 0.08) * Math.pow(j0, 2);
          } else {
            // Outside shadow: diffraction ripples
            intensity = 0.8 + 0.2 * Math.cos((r - discR) * 0.5);
          }

          const idx = (y * w + x) * 4;
          imgData.data[idx] = Math.floor(rgb.r * intensity);
          imgData.data[idx + 1] = Math.floor(rgb.g * intensity);
          imgData.data[idx + 2] = Math.floor(rgb.b * intensity);
          imgData.data[idx + 3] = 255;
        }
      }
      ctx.putImageData(imgData, 0, 0);

      // Label Poisson-Arago spot
      ctx.fillStyle = "#fff";
      ctx.font = "12px sans-serif";
      ctx.fillText("Poisson-Arago Central Bright Spot", midX - 95, midY - discR - 10);
      ctx.fillText(`Disc Shadow Radius = ${vals["ps-rad"]} mm`, 15, h - 14);
    }
  },

  // 14. Single Slit Fraunhofer
  "single-slit-fraunhofer": {
    title: "📊 Fraunhofer Single Slit Sinc Pattern & Diffraction Minima",
    desc: "Explore the sinc-squared intensity distribution $I = I_0 (\\sin \\beta / \\beta)^2$, showing how narrowing slit width $a$ broadens the central maximum.",
    controls: [
      { id: "ss-a", label: "Slit Width a (μm)", min: 10, max: 100, step: 2, value: 30 },
      { id: "ss-wl", label: "Wavelength λ (nm)", min: 380, max: 750, step: 5, value: 532 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const a = vals["ss-a"] * 1e-6;
      const wl = vals["ss-wl"] * 1e-9;
      const rgb = wlToRGB(vals["ss-wl"]);

      ctx.fillStyle = "#090d18";
      ctx.fillRect(0, 0, w, h);

      // Plot sinc^2 curve
      const plotH = h - 60;
      const midX = w / 2;

      ctx.strokeStyle = `rgb(${rgb.r}, ${rgb.g}, ${rgb.b})`;
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      for (let px = 0; px < w; px++) {
        const theta = ((px - midX) / (w * 0.5)) * 0.05; // 0.05 rad span
        const beta = (Math.PI * a * Math.sin(theta)) / wl;
        const sinc = beta === 0 ? 1.0 : Math.sin(beta) / beta;
        const intVal = sinc * sinc;
        const py = h - 30 - intVal * plotH;

        if (px === 0) ctx.moveTo(px, py);
        else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Readout
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      const divAngle = (wl / a) * (180 / Math.PI);
      ctx.fillText(`First Minimum: a sin θ = λ => θ₁ = ${divAngle.toFixed(3)}° | Central Max: 85% total energy`, 15, 25);
    }
  },

  // 15. Double Slit Fraunhofer
  "double-slit-fraunhofer": {
    title: "✨ Double-Slit Diffraction Envelope & Missing Spectral Orders",
    desc: "Demonstrates high-frequency two-beam interference fringes modulated by single-slit diffraction envelope, showing missing orders when $d/a = m/p$.",
    controls: [
      { id: "ds-a", label: "Slit Width a (μm)", min: 10, max: 40, step: 2, value: 15 },
      { id: "ds-d", label: "Separation d (μm)", min: 30, max: 120, step: 5, value: 60 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const a = vals["ds-a"] * 1e-6;
      const d = vals["ds-d"] * 1e-6;
      const wl = 532e-9;
      const ratio = d / a;

      ctx.fillStyle = "#080c16";
      ctx.fillRect(0, 0, w, h);

      const plotH = h - 60;
      const midX = w / 2;

      // Draw single-slit envelope (dashed)
      ctx.strokeStyle = "rgba(148, 163, 184, 0.4)";
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      for (let px = 0; px < w; px++) {
        const theta = ((px - midX) / (w * 0.5)) * 0.04;
        const beta = (Math.PI * a * Math.sin(theta)) / wl;
        const sinc = beta === 0 ? 1.0 : Math.sin(beta) / beta;
        const py = h - 30 - (sinc * sinc) * plotH;
        if (px === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw combined double slit pattern
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2;
      ctx.beginPath();
      for (let px = 0; px < w; px++) {
        const theta = ((px - midX) / (w * 0.5)) * 0.04;
        const beta = (Math.PI * a * Math.sin(theta)) / wl;
        const alpha = (Math.PI * d * Math.sin(theta)) / wl;
        const sinc = beta === 0 ? 1.0 : Math.sin(beta) / beta;
        const intVal = Math.pow(sinc, 2) * Math.pow(Math.cos(alpha), 2);
        const py = h - 30 - intVal * plotH;
        if (px === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.fillStyle = "#f59e0b";
      ctx.font = "12px monospace";
      ctx.fillText(`Slit Ratio d/a = ${ratio.toFixed(2)} => Missing Order m = ${Math.round(ratio)}`, 15, 25);
    }
  },

  // 16. Grating Spectrometer
  "grating-spectrometer": {
    title: "🌈 Diffraction Grating Spectrometer & Multi-Line Dispersion",
    desc: "Simulate dispersion $(a+b)\\sin\\theta = m\\lambda$ of atomic spectral lines (Hydrogen Balmer series / Sodium doublet) as a function of groove density.",
    controls: [
      { id: "gs-n", label: "Ruling (lines/mm)", min: 100, max: 1200, step: 50, value: 600 },
      { id: "gs-m", label: "Spectral Order m", min: 1, max: 3, step: 1, value: 1 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const linesPerM = vals["gs-n"] * 1e3;
      const d = 1.0 / linesPerM;
      const m = vals["gs-m"];

      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      // Hydrogen Balmer Lines
      const lines = [
        { name: "H-α (Red)", wl: 656.3 },
        { name: "H-β (Cyan)", wl: 486.1 },
        { name: "H-γ (Blue)", wl: 434.0 },
        { name: "H-δ (Violet)", wl: 410.2 }
      ];

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px sans-serif";
      ctx.fillText(`Diffraction Grating Spectrometer (Order m = ${m}, ${vals["gs-n"]} lines/mm):`, 20, 25);

      const baseY = 80;
      lines.forEach((l, idx) => {
        const sinTheta = (m * l.wl * 1e-9) / d;
        if (sinTheta <= 1.0) {
          const thetaDeg = Math.asin(sinTheta) * (180 / Math.PI);
          const px = 60 + (sinTheta / 0.8) * (w - 120);

          const rgb = wlToRGB(l.wl);
          ctx.strokeStyle = `rgb(${rgb.r}, ${rgb.g}, ${rgb.b})`;
          ctx.lineWidth = 4;
          ctx.beginPath(); ctx.moveTo(px, baseY); ctx.lineTo(px, h - 50); ctx.stroke();

          ctx.fillStyle = `rgb(${rgb.r}, ${rgb.g}, ${rgb.b})`;
          ctx.font = "11px monospace";
          ctx.fillText(`${l.name}: θ = ${thetaDeg.toFixed(2)}°`, px - 40, baseY + idx * 24 + 20);
        }
      });
    }
  },

  // 17. Rayleigh Resolution Criterion
  "rayleigh-criterion": {
    title: "🎯 Rayleigh Criterion for Resolution & Two-Source Overlap",
    desc: "Slide angular separation $\\Delta \\theta$ to test Rayleigh’s 81% saddle dip criterion between two monochromatic Airy diffraction peaks.",
    controls: [
      { id: "rc-sep", label: "Angular Separation (Airy units)", min: 0.5, max: 2.0, step: 0.05, value: 1.0 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const sep = vals["rc-sep"]; // 1.0 = exactly at Rayleigh limit
      ctx.fillStyle = "#090d18";
      ctx.fillRect(0, 0, w, h);

      const midX = w / 2;
      const plotH = h - 70;
      const spread = 80;

      // Peak 1 and Peak 2 centers
      const c1 = midX - (sep * spread) / 2;
      const c2 = midX + (sep * spread) / 2;

      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();

      for (let px = 0; px < w; px++) {
        const u1 = (px - c1) / spread * Math.PI;
        const u2 = (px - c2) / spread * Math.PI;
        const s1 = u1 === 0 ? 1 : Math.sin(u1) / u1;
        const s2 = u2 === 0 ? 1 : Math.sin(u2) / u2;
        const intVal = (s1 * s1 + s2 * s2) * 0.5;
        const py = h - 30 - intVal * plotH;

        if (px === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      const status = sep < 0.95 ? "Unresolved (Merged Peak)" : sep <= 1.05 ? "Rayleigh Limit (81% Saddle Dip)" : "Well Resolved (Distinct Peaks)";
      ctx.fillStyle = sep < 0.95 ? "#ef4444" : sep <= 1.05 ? "#f59e0b" : "#10b981";
      ctx.font = "13px monospace";
      ctx.fillText(`Separation: ${sep.toFixed(2)} Rayleigh Units => ${status}`, 20, 25);
    }
  },

  // 18. Polarization Malus
  "polarization-malus": {
    title: "🕶️ States of Polarization & Malus’s Law Three-Polarizer Experiment",
    desc: "Rotate the middle polarizer angle $\\theta$ to show unblocking of light between crossed polarizers via projection $I = I_0 \\cos^2\\theta_1 \\cos^2\\theta_2$.",
    controls: [
      { id: "pm-th", label: "Middle Polarizer Angle θ (°)", min: 0, max: 90, step: 2, value: 45 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const thRad = (vals["pm-th"] * Math.PI) / 180;
      // P1 at 0°, P2 at θ, P3 at 90° (crossed with P1)
      const transPct = Math.pow(Math.cos(thRad), 2) * Math.pow(Math.cos(Math.PI / 2 - thRad), 2) * 100;

      ctx.fillStyle = "#080c16";
      ctx.fillRect(0, 0, w, h);

      // Draw 3 Polarizer plates
      const pY = h / 2 - 40;
      // P1 (Vertical 0°)
      drawPolarizer(ctx, 80, pY, 0, "P₁ (0°)");
      // P2 (Rotated θ)
      drawPolarizer(ctx, w / 2 - 25, pY, vals["pm-th"], `P₂ (${vals["pm-th"]}°)`);
      // P3 (Horizontal 90°)
      drawPolarizer(ctx, w - 130, pY, 90, "P₃ (90°)");

      // Output light beam on far right
      ctx.fillStyle = `rgba(56, 189, 248, ${transPct / 25})`;
      ctx.fillRect(w - 60, h / 2 - 20, 40, 40);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "13px monospace";
      ctx.fillText(`Final Transmitted Intensity: ${transPct.toFixed(2)}% of incident light`, 20, h - 15);
      ctx.fillText("Notice: Insertion of middle polarizer transmits light between crossed polarizers!", 20, 30);
    }
  },

  // 19. Birefringence & Nicol Prism
  "birefringence-nicol": {
    title: "💎 Birefringent Calcite Crystal Double Refraction & Nicol Prism",
    desc: "Simulate splitting into Ordinary ($o$-ray, $n_o = 1.658$) and Extraordinary ($e$-ray, $n_e = 1.486$) rays with total internal reflection at the Canada balsam cut.",
    controls: [
      { id: "bn-rot", label: "Crystal Rotation (°)", min: 0, max: 360, step: 5, value: 45 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = "#080d19";
      ctx.fillRect(0, 0, w, h);

      // Nicol Prism Rhombus
      ctx.fillStyle = "rgba(56, 189, 248, 0.12)";
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(100, 40); ctx.lineTo(w - 100, 40);
      ctx.lineTo(w - 160, h - 40); ctx.lineTo(40, h - 40);
      ctx.closePath();
      ctx.fill(); ctx.stroke();

      // Canada Balsam Cut Line
      ctx.strokeStyle = "#ec4899"; ctx.lineWidth = 1.5; ctx.setLineDash([5, 5]);
      ctx.beginPath(); ctx.moveTo(w - 100, 40); ctx.lineTo(40, h - 40); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ec4899"; ctx.font = "11px sans-serif";
      ctx.fillText("Canada Balsam Layer (n = 1.55)", 110, h / 2);

      // Rays
      const midY = h / 2;
      // Incident Unpolarized Ray
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(10, midY); ctx.lineTo(70, midY); ctx.stroke();
      ctx.fillText("Unpolarized Ray", 5, midY - 10);

      // e-ray passes straight through
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(70, midY); ctx.lineTo(w - 130, midY - 15); ctx.lineTo(w - 10, midY - 15); ctx.stroke();
      ctx.fillStyle = "#10b981"; ctx.fillText("Extraordinary Ray (e-ray): Transmitted (100% Polarized)", w - 340, midY - 25);

      // o-ray reflects down by TIR
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(70, midY); ctx.lineTo(130, midY + 15); ctx.lineTo(160, h - 40); ctx.stroke();
      ctx.fillStyle = "#ef4444"; ctx.fillText("Ordinary Ray (o-ray): Total Internal Reflection (TIR)", 120, h - 20);
    }
  },

  // 20. Retardation Plates
  "retardation-plates": {
    title: "🔄 Quarter-Wave (QWP) & Half-Wave (HWP) Polarization State Transformer",
    desc: "Transforms linear, circular, and elliptical polarization states through optical retardation delay $\\delta = (2\\pi/\\lambda)|n_e - n_o|d$.",
    controls: [
      { id: "rp-type", label: "Waveplate: 0=QWP (λ/4), 1=HWP (λ/2)", min: 0, max: 1, step: 1, value: 0 },
      { id: "rp-ang", label: "Incident Polarization Angle (°)", min: 0, max: 90, step: 5, value: 45 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      ctx.fillStyle = "#080c16";
      ctx.fillRect(0, 0, w, h);

      const isHWP = vals["rp-type"] === 1;
      const theta = (vals["rp-ang"] * Math.PI) / 180;
      const midX = w / 2, midY = h / 2;
      const R = 80;

      // Draw Lissajous Polarization Ellipse
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3;
      ctx.beginPath();

      const delta = isHWP ? Math.PI : Math.PI / 2;
      for (let t = 0; t <= Math.PI * 2; t += 0.05) {
        const ex = R * Math.cos(theta) * Math.cos(t);
        const ey = R * Math.sin(theta) * Math.cos(t + delta);
        if (t === 0) ctx.moveTo(midX + ex, midY - ey);
        else ctx.lineTo(midX + ex, midY - ey);
      }
      ctx.stroke();

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "13px monospace";
      if (!isHWP) {
        const isCirc = vals["rp-ang"] === 45;
        ctx.fillText(`Quarter-Wave Plate (QWP): ${isCirc ? "Pure Circularly Polarized Light!" : "Elliptically Polarized Light"}`, 20, 25);
      } else {
        ctx.fillText(`Half-Wave Plate (HWP): Rotates Linear Polarization to 2θ = ${vals["rp-ang"] * 2}°`, 20, 25);
      }
    }
  },

  // 21. Laurent Polarimeter
  "polarimeter-half-shade": {
    title: "🧪 Laurent’s Half-Shade Polarimeter & Sugar Concentration Assay",
    desc: "Match the brightness of the two semicircular halves to detect optical activity $[\alpha] = \theta / (l \cdot c)$ of chiral sugar solutions.",
    controls: [
      { id: "lh-c", label: "Sugar Concentration c (g/cm³)", min: 0.0, max: 0.3, step: 0.02, value: 0.1 },
      { id: "lh-ana", label: "Analyzer Rotation (°)", min: -30, max: 30, step: 1, value: 0 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const c = vals["lh-c"];
      const specRot = 66.0; // cane sugar [α]
      const l = 2.0; // 20cm = 2dm
      const rot = specRot * l * c; // optical rotation in deg
      const ana = vals["lh-ana"];

      // Relative intensities in left and right fields
      const radL = ((ana - rot) * Math.PI) / 180;
      const radR = ((ana - rot - 6) * Math.PI) / 180; // 6° half-shade angle
      const intL = Math.pow(Math.cos(radL), 2);
      const intR = Math.pow(Math.cos(radR), 2);

      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const midX = w / 2, midY = h / 2;
      const radius = 90;

      // Left Semicircle
      ctx.fillStyle = `rgba(245, 158, 11, ${intL})`;
      ctx.beginPath();
      ctx.arc(midX, midY, radius, Math.PI / 2, Math.PI * 1.5);
      ctx.fill();

      // Right Semicircle
      ctx.fillStyle = `rgba(245, 158, 11, ${intR})`;
      ctx.beginPath();
      ctx.arc(midX, midY, radius, -Math.PI / 2, Math.PI / 2);
      ctx.fill();

      // Dividing Line
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(midX, midY - radius); ctx.lineTo(midX, midY + radius); ctx.stroke();

      const matched = Math.abs(intL - intR) < 0.03;
      ctx.fillStyle = matched ? "#10b981" : "#cbd5e1";
      ctx.font = "13px monospace";
      ctx.fillText(`Optical Rotation θ = +${rot.toFixed(1)}° | Balance: ${matched ? "PERFECT MATCH!" : "Adjust Analyzer Angle"}`, 20, 25);
    }
  },

  // 22. Laser Gain Threshold
  "laser-gain-threshold": {
    title: "⚡ 3-Level vs 4-Level Population Inversion & Laser Gain Threshold",
    desc: "Compare pump rate requirements to overcome threshold gain condition $\\gamma_{\\text{th}} = \\alpha_s + \\frac{1}{2L}\\ln(1/R_1 R_2)$.",
    controls: [
      { id: "lg-pump", label: "Pump Power (W)", min: 1, max: 50, step: 1, value: 20 },
      { id: "lg-r2", label: "Output Coupler R₂", min: 0.8, max: 0.99, step: 0.01, value: 0.95 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const pump = vals["lg-pump"];
      const r2 = vals["lg-r2"];
      const r1 = 1.0;
      const L = 0.3; // 30cm
      const loss = 0.02;
      const gammaTh = loss + (1 / (2 * L)) * Math.log(1 / (r1 * r2));

      ctx.fillStyle = "#080c16";
      ctx.fillRect(0, 0, w, h);

      // Plot Gain vs Pump Power for 3-level vs 4-level
      const plotH = h - 60;
      ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
      // Threshold line
      const thY = h - 30 - (gammaTh / 0.8) * plotH;
      ctx.beginPath(); ctx.moveTo(60, thY); ctx.lineTo(w - 30, thY); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#ef4444"; ctx.font = "11px sans-serif";
      ctx.fillText(`Threshold γ_th = ${gammaTh.toFixed(3)} m⁻¹`, 70, thY - 8);

      // 4-level laser curve (low threshold)
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let p = 1; p <= 50; p++) {
        const gain4 = 0.025 * p;
        const px = 60 + (p / 50) * (w - 100);
        const py = h - 30 - (gain4 / 0.8) * plotH;
        if (p === 1) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.fillStyle = "#10b981"; ctx.fillText("4-Level Laser (Nd:YAG, He-Ne)", w - 210, 80);

      // 3-level laser curve (high threshold)
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let p = 1; p <= 50; p++) {
        const gain3 = Math.max(0, 0.020 * (p - 18));
        const px = 60 + (p / 50) * (w - 100);
        const py = h - 30 - (gain3 / 0.8) * plotH;
        if (p === 1) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.fillStyle = "#f59e0b"; ctx.fillText("3-Level Laser (Ruby)", w - 210, 110);
    }
  },

  // 23. Laser Longitudinal & Transverse TEM Modes
  "laser-tem-modes": {
    title: "🎯 Transverse Hermite-Gaussian Laser Modes (TEM_mn)",
    desc: "Render spatial 2D irradiance distributions for fundamental Gaussian mode $\\text{TEM}_{00}$, doughnut mode $\\text{TEM}_{01}$, and higher-order cavity modes $\\text{TEM}_{11}, \\text{TEM}_{20}$.",
    controls: [
      { id: "tem-m", label: "Transverse Order m", min: 0, max: 2, step: 1, value: 0 },
      { id: "tem-n", label: "Transverse Order n", min: 0, max: 2, step: 1, value: 0 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      const m = vals["tem-m"];
      const n = vals["tem-n"];
      const midX = w / 2, midY = h / 2;
      const w0 = 40; // beam waist

      const imgData = ctx.createImageData(w, h);

      for (let y = 0; y < h; y++) {
        for (let x = 0; x < w; x++) {
          const rx = (x - midX) / w0;
          const ry = (y - midY) / w0;

          // Hermite polynomials
          const hm = hermite(m, rx * Math.SQRT2);
          const hn = hermite(n, ry * Math.SQRT2);
          const intensity = Math.pow(hm * hn, 2) * Math.exp(-2 * (rx * rx + ry * ry));

          const normInt = Math.min(1.0, intensity);
          const idx = (y * w + x) * 4;
          imgData.data[idx] = Math.floor(239 * normInt); // Laser Red 632.8nm
          imgData.data[idx + 1] = Math.floor(68 * normInt);
          imgData.data[idx + 2] = Math.floor(68 * normInt);
          imgData.data[idx + 3] = 255;
        }
      }
      ctx.putImageData(imgData, 0, 0);

      ctx.fillStyle = "#fff";
      ctx.font = "14px monospace";
      ctx.fillText(`Transverse Mode: TEM_${m}${n} (${m === 0 && n === 0 ? "Fundamental Gaussian" : "Higher Hermite-Gaussian Order"})`, 20, 25);
    }
  }
};

// --- Helper Functions ---
function wlToRGB(wl) {
  let r = 0, g = 0, b = 0;
  if (wl >= 380 && wl < 440) { r = -(wl - 440) / (440 - 380); b = 1.0; }
  else if (wl >= 440 && wl < 490) { g = (wl - 440) / (490 - 440); b = 1.0; }
  else if (wl >= 490 && wl < 510) { g = 1.0; b = -(wl - 510) / (510 - 490); }
  else if (wl >= 510 && wl < 580) { r = (wl - 510) / (580 - 510); g = 1.0; }
  else if (wl >= 580 && wl < 645) { r = 1.0; g = -(wl - 645) / (645 - 580); }
  else if (wl >= 645 && wl <= 780) { r = 1.0; }
  return { r: Math.round(r * 255), g: Math.round(g * 255), b: Math.round(b * 255) };
}

function fresnelIntegrals(v) {
  // Numerical approximation of Fresnel integrals C(v) and S(v)
  let c = 0, s = 0;
  const n = 100;
  const dt = v / n;
  for (let i = 0; i < n; i++) {
    const t = (i + 0.5) * dt;
    c += Math.cos(Math.PI * t * t / 2) * dt;
    s += Math.sin(Math.PI * t * t / 2) * dt;
  }
  return { C: c, S: s };
}

function drawPolarizer(ctx, x, y, angleDeg, label) {
  ctx.fillStyle = "rgba(56, 189, 248, 0.2)";
  ctx.strokeStyle = "#38bdf8";
  ctx.lineWidth = 2;
  ctx.strokeRect(x, y, 50, 80);
  ctx.fillRect(x, y, 50, 80);

  // Transmission Axis line
  const angRad = (angleDeg * Math.PI) / 180;
  const cx = x + 25, cy = y + 40;
  ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(cx - 20 * Math.sin(angRad), cy - 20 * Math.cos(angRad));
  ctx.lineTo(cx + 20 * Math.sin(angRad), cy + 20 * Math.cos(angRad));
  ctx.stroke();

  ctx.fillStyle = "#cbd5e1"; ctx.font = "11px sans-serif";
  ctx.fillText(label, x - 5, y + 100);
}

function hermite(n, x) {
  if (n === 0) return 1;
  if (n === 1) return 2 * x;
  if (n === 2) return 4 * x * x - 2;
  return 1;
}

console.log("Optics interactive simulation engine compiled successfully!");

// Universal Engine Integration Adapter
window.SimulationEngine = window.SimulationEngine || {};
window.SimulationEngine.activeInstances = window.SimulationEngine.activeInstances || {};

window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const simConfig = window.OPTICS_SIMS[simType];
  if (!simConfig) {
    console.warn("Optics simulation not found:", simType);
    return;
  }

  container.innerHTML = "";

  const box = document.createElement("div");
  box.className = "sim-inline-card";
  box.style.background = "#0c1322";
  box.style.border = "1px solid #1e293b";
  box.style.borderRadius = "12px";
  box.style.padding = "1.5rem";
  box.style.margin = "1.75rem 0";

  const header = document.createElement("div");
  header.style.marginBottom = "1rem";
  header.innerHTML = `
    <h4 style="color:#38bdf8; font-size:1.15rem; margin-bottom:0.35rem; display:flex; align-items:center; gap:0.5rem;">
      ${simConfig.title}
    </h4>
    <p style="color:#94a3b8; font-size:0.9rem; line-height:1.5;">${simConfig.desc}</p>
  `;
  box.appendChild(header);

  // Canvas
  const canvas = document.createElement("canvas");
  canvas.width = 720;
  canvas.height = 340;
  canvas.style.width = "100%";
  canvas.style.height = "auto";
  canvas.style.borderRadius = "8px";
  canvas.style.display = "block";
  canvas.style.background = "#070b14";
  canvas.style.border = "1px solid #1e293b";
  box.appendChild(canvas);

  // Control Controls Bar
  const ctrlBar = document.createElement("div");
  ctrlBar.style.display = "flex";
  ctrlBar.style.flexWrap = "wrap";
  ctrlBar.style.gap = "1.25rem";
  ctrlBar.style.marginTop = "1rem";
  ctrlBar.style.padding = "0.75rem 1rem";
  ctrlBar.style.background = "#080e1c";
  ctrlBar.style.borderRadius = "8px";
  ctrlBar.style.border = "1px solid #1e293d";

  const currentVals = {};

  simConfig.controls.forEach(ctrl => {
    currentVals[ctrl.id] = ctrl.value;

    const wrap = document.createElement("div");
    wrap.style.display = "flex";
    wrap.style.flexDirection = "column";
    wrap.style.gap = "0.25rem";
    wrap.style.minWidth = "160px";

    const labelRow = document.createElement("div");
    labelRow.style.display = "flex";
    labelRow.style.justifyContent = "space-between";
    labelRow.style.fontSize = "0.82rem";
    labelRow.style.color = "#cbd5e1";

    const titleSpan = document.createElement("span");
    titleSpan.innerText = ctrl.label;
    const valSpan = document.createElement("span");
    valSpan.style.fontFamily = "monospace";
    valSpan.style.color = "#38bdf8";
    valSpan.innerText = ctrl.value;

    labelRow.appendChild(titleSpan);
    labelRow.appendChild(valSpan);
    wrap.appendChild(labelRow);

    const input = document.createElement("input");
    input.type = "range";
    input.min = ctrl.min;
    input.max = ctrl.max;
    input.step = ctrl.step;
    input.value = ctrl.value;
    input.style.accentColor = "#38bdf8";
    input.style.cursor = "pointer";

    input.addEventListener("input", (e) => {
      const v = parseFloat(e.target.value);
      currentVals[ctrl.id] = v;
      valSpan.innerText = v;
      simConfig.render(canvas, currentVals);
    });

    wrap.appendChild(input);
    ctrlBar.appendChild(wrap);
  });

  box.appendChild(ctrlBar);
  container.appendChild(box);

  // Initial draw
  simConfig.render(canvas, currentVals);
};
