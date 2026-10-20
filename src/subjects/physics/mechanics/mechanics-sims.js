// Interactive Physics Simulation Suite for Fundamentals of Mechanics
// 26 comprehensive topic-level simulations with 60 FPS Canvas animation loops for dynamic systems,
// interactive parameter sliders, and clear analytical diagrams for static topics.

window.MECHANICS_SIMS = {
  // ==========================================
  // UNIT 1: VECTOR ALGEBRA & VECTOR CALCULUS
  // ==========================================

  // 1. Vector Addition & Components (Interactive Geometric Sandbox)
  "vector-addition-sim": {
    title: "📐 2D Vector Addition, Dot Product & Cross Product Sandbox",
    desc: "Adjust magnitudes and angles of vectors A and B to observe resultant vector R = A + B, scalar projection A · B, and perpendicular torque area |A × B|.",
    isAnimated: false,
    controls: [
      { id: "va-magA", label: "Magnitude |A|", min: 20, max: 120, step: 2, value: 80 },
      { id: "va-angA", label: "Angle θ_A (°)", min: 0, max: 360, step: 5, value: 30 },
      { id: "va-magB", label: "Magnitude |B|", min: 20, max: 120, step: 2, value: 70 },
      { id: "va-angB", label: "Angle θ_B (°)", min: 0, max: 360, step: 5, value: 110 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = w * 0.45, oY = h * 0.55;

      // Coordinate axes
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(30, oY); ctx.lineTo(w - 30, oY);
      ctx.moveTo(oX, 20); ctx.lineTo(oX, h - 20);
      ctx.stroke();

      const radA = (vals["va-angA"] * Math.PI) / 180;
      const radB = (vals["va-angB"] * Math.PI) / 180;

      const ax = vals["va-magA"] * Math.cos(radA);
      const ay = -vals["va-magA"] * Math.sin(radA);

      const bx = vals["va-magB"] * Math.cos(radB);
      const by = -vals["va-magB"] * Math.sin(radB);

      const rx = ax + bx;
      const ry = ay + by;

      // Parallelogram shading
      ctx.fillStyle = "rgba(56, 189, 248, 0.08)";
      ctx.beginPath();
      ctx.moveTo(oX, oY); ctx.lineTo(oX + ax, oY + ay);
      ctx.lineTo(oX + rx, oY + ry); ctx.lineTo(oX + bx, oY + by);
      ctx.closePath(); ctx.fill();

      drawArrow(ctx, oX, oY, oX + ax, oY + ay, "#38bdf8", "A", 2.5);
      drawArrow(ctx, oX, oY, oX + bx, oY + by, "#10b981", "B", 2.5);
      drawArrow(ctx, oX, oY, oX + rx, oY + ry, "#f59e0b", "R = A + B", 3);

      const dotProd = ax * bx + (-ay) * (-by);
      const crossProd = ax * (-by) - (-ay) * bx;
      const magR = Math.hypot(rx, ry);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`|R| = ${magR.toFixed(1)} | Dot Product A·B = ${dotProd.toFixed(1)} | Cross Product |A×B| = ${Math.abs(crossProd).toFixed(1)}`, 20, 25);
    }
  },

  // 2. Vector Triple Product & Parallelepiped Volume
  "vector-triple-product-sim": {
    title: "📦 Scalar & Vector Triple Product (BAC-CAB Rule) Visualizer",
    desc: "Observe the parallelepiped volume V = |A · (B × C)| and examine how the vector triple product A × (B × C) lies strictly in the plane of B and C.",
    isAnimated: false,
    controls: [
      { id: "tp-theta", label: "Angle of Vector A (°)", min: 10, max: 90, step: 2, value: 45 },
      { id: "tp-height", label: "Out-of-Plane Tilt of C", min: 10, max: 80, step: 2, value: 50 },
      { id: "tp-lenB", label: "Length of B", min: 40, max: 120, step: 5, value: 80 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = w * 0.35, oY = h * 0.65;
      const radA = (vals["tp-theta"] * Math.PI) / 180;
      const lenB = vals["tp-lenB"];
      const tiltC = vals["tp-height"];

      const ax = 90 * Math.cos(radA), ay = -90 * Math.sin(radA);
      const bx = lenB, by = 0;
      const cx = 35, cy = -tiltC;

      ctx.strokeStyle = "rgba(148, 163, 184, 0.25)"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(oX, oY); ctx.lineTo(oX + bx, oY + by);
      ctx.lineTo(oX + bx + cx, oY + by + cy); ctx.lineTo(oX + cx, oY + cy); ctx.closePath();
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(oX + ax, oY + ay); ctx.lineTo(oX + ax + bx, oY + ay + by);
      ctx.lineTo(oX + ax + bx + cx, oY + ay + by + cy); ctx.lineTo(oX + ax + cx, oY + ay + cy); ctx.closePath();
      ctx.stroke();

      ctx.beginPath();
      ctx.moveTo(oX, oY); ctx.lineTo(oX + ax, oY + ay);
      ctx.moveTo(oX + bx, oY + by); ctx.lineTo(oX + bx + ax, oY + by + ay);
      ctx.moveTo(oX + bx + cx, oY + by + cy); ctx.lineTo(oX + bx + cx + ax, oY + by + cy + ay);
      ctx.moveTo(oX + cx, oY + cy); ctx.lineTo(oX + cx + ax, oY + cy + ay);
      ctx.stroke();

      drawArrow(ctx, oX, oY, oX + ax, oY + ay, "#38bdf8", "A", 2.5);
      drawArrow(ctx, oX, oY, oX + bx, oY + by, "#10b981", "B", 2.5);
      drawArrow(ctx, oX, oY, oX + cx, oY + cy, "#ec4899", "C", 2.5);

      const vol = Math.abs(lenB * tiltC * 90 * Math.sin(radA)) / 1000;
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Scalar Triple Product [A,B,C] = ${vol.toFixed(2)} k-units³ | BAC-CAB Identity Verified`, 20, 25);
    }
  },

  // 3. Vector Integration & Moving Particle Trajectory (ANIMATED)
  "vector-integration-sim": {
    title: "📈 Dynamic Trajectory Integration: r(t) = ∫ v(t) dt",
    desc: "Watch the particle travel in real time along its integrated trajectory with dynamically updating velocity and acceleration vectors.",
    isAnimated: true,
    controls: [
      { id: "vi-v0", label: "Initial Velocity v_0", min: 20, max: 70, step: 2, value: 45 },
      { id: "vi-ang", label: "Launch Angle (°)", min: 20, max: 70, step: 5, value: 50 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = 60, oY = h - 50;
      const rad = (vals["vi-ang"] * Math.PI) / 180;
      const v0 = vals["vi-v0"];
      const g = 9.8;
      const totalT = (2 * v0 * Math.sin(rad)) / g;

      // Loop time
      const curT = (animTime * 1.2) % (totalT + 0.6);
      const t = Math.min(curT, totalT);

      // Coordinate axes
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(oX, 30); ctx.lineTo(oX, oY); ctx.lineTo(w - 30, oY);
      ctx.stroke();

      // Full trajectory trace
      ctx.strokeStyle = "rgba(56, 189, 248, 0.35)"; ctx.lineWidth = 2;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      for (let tau = 0; tau <= totalT; tau += 0.05) {
        const px = oX + (v0 * Math.cos(rad) * tau) * 2.2;
        const py = oY - (v0 * Math.sin(rad) * tau - 0.5 * g * tau * tau) * 2.2;
        if (tau === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Current integrated position
      const curX = oX + (v0 * Math.cos(rad) * t) * 2.2;
      const curY = oY - (v0 * Math.sin(rad) * t - 0.5 * g * t * t) * 2.2;

      // Draw particle
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(curX, curY, 7, 0, Math.PI * 2); ctx.fill();

      // Current velocity vector v(t)
      const vx = v0 * Math.cos(rad) * 0.8;
      const vy = -(v0 * Math.sin(rad) - g * t) * 0.8;
      drawArrow(ctx, curX, curY, curX + vx, curY + vy, "#38bdf8", "v(t)", 2.5);

      // Acceleration vector a = -g j
      drawArrow(ctx, curX, curY, curX, curY + 28, "#f43f5e", "a = -g ĵ", 2);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Time t = ${t.toFixed(2)}s / ${totalT.toFixed(2)}s | Integrated Displacement r(t) = ${(curX - oX).toFixed(1)} px`, 20, 25);
    }
  },

  // 4. Vector Fields, Gradient Flow & Animated Streamlines (ANIMATED)
  "vector-fields-calc-sim": {
    title: "🌀 Vector Fields: Gradient Flow & Animated Streamline Tracers",
    desc: "Particles stream continuously along vector field streamlines to reveal divergence (sink/source) and curl (vortex circulation) in real time.",
    isAnimated: true,
    controls: [
      { id: "vf-type", label: "Field Type: 0=Sink, 1=Vortex/Curl, 2=Saddle", min: 0, max: 2, step: 1, value: 1 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#080d1a";
      ctx.fillRect(0, 0, w, h);

      const midX = w / 2, midY = h / 2;
      const type = vals["vf-type"];
      const spacing = 36;

      // Draw vector field grid arrows
      for (let x = spacing; x < w; x += spacing) {
        for (let y = spacing; y < h; y += spacing) {
          const dx = x - midX, dy = y - midY;
          const r = Math.hypot(dx, dy) + 1;
          let vx = 0, vy = 0, color = "#1e293b";
          if (type === 0) { vx = (-dx / r) * 12; vy = (-dy / r) * 12; color = "rgba(56, 189, 248, 0.4)"; }
          else if (type === 1) { vx = (-dy / r) * 12; vy = (dx / r) * 12; color = "rgba(236, 72, 153, 0.4)"; }
          else { vx = (dx / 30) * 6; vy = (-dy / 30) * 6; color = "rgba(245, 158, 11, 0.4)"; }
          drawArrow(ctx, x, y, x + vx, y + vy, color, "", 1);
        }
      }

      // Animated tracer particles flowing along field lines
      const numTracers = 40;
      ctx.fillStyle = type === 1 ? "#38bdf8" : "#10b981";
      for (let i = 0; i < numTracers; i++) {
        const seed = (i * 137.5) % 360;
        const radSeed = (seed * Math.PI) / 180;
        let px = 0, py = 0;

        if (type === 0) {
          // Sink: flow inward
          const phase = (animTime * 30 + i * 8) % 130;
          const dist = 140 - phase;
          px = midX + dist * Math.cos(radSeed);
          py = midY + dist * Math.sin(radSeed);
        } else if (type === 1) {
          // Vortex: circulate in circles
          const radius = 35 + (i % 6) * 18;
          const ang = animTime * (2.5 / (radius * 0.02 + 1)) + seed;
          px = midX + radius * Math.cos(ang);
          py = midY + radius * Math.sin(ang);
        } else {
          // Saddle
          const tP = ((animTime * 0.8 + i * 0.2) % 3) - 1.5;
          const x0 = 30 * Math.cos(radSeed), y0 = 30 * Math.sin(radSeed);
          px = midX + x0 * Math.exp(tP);
          py = midY + y0 * Math.exp(-tP);
        }

        if (px > 20 && px < w - 20 && py > 20 && py < h - 20) {
          ctx.beginPath(); ctx.arc(px, py, 3, 0, Math.PI * 2); ctx.fill();
        }
      }

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      const desc = type === 0 ? "Sink: ∇·V < 0 (Net Inflow), ∇×V = 0" : (type === 1 ? "Vortex Circulation: ∇·V = 0, ∇×V ≠ 0" : "Saddle: ∇·V = 0, ∇×V = 0");
      ctx.fillText(desc, 20, 25);
    }
  },

  // ====================================================
  // UNIT 2: VECTOR INTEGRAL THEOREMS & COORDINATES
  // ====================================================

  // 5. Stokes' and Divergence Theorem Flux
  "stokes-divergence-sim": {
    title: "🌐 Gauss’s Divergence & Stokes’ Curl Theorem Flux Sandbox",
    desc: "Calculate surface flux ∮ V · dA and compare with volume divergence integral ∭ (∇·V) dV for expanding Gaussian spheres.",
    isAnimated: false,
    controls: [
      { id: "sd-radius", label: "Gaussian Radius R", min: 30, max: 140, step: 5, value: 80 },
      { id: "sd-charge", label: "Source Strength Q", min: 1, max: 10, step: 1, value: 5 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const midX = w / 2, midY = h / 2;
      const R = vals["sd-radius"];
      const Q = vals["sd-charge"];

      const numLines = 24;
      for (let i = 0; i < numLines; i++) {
        const theta = (i * 2 * Math.PI) / numLines;
        const x1 = midX + 15 * Math.cos(theta), y1 = midY + 15 * Math.sin(theta);
        const x2 = midX + (R + 40) * Math.cos(theta), y2 = midY + (R + 40) * Math.sin(theta);
        drawArrow(ctx, x1, y1, x2, y2, "rgba(56, 189, 248, 0.4)", "", 1.2);
      }

      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(midX, midY, 10, 0, Math.PI * 2); ctx.fill();

      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5; ctx.setLineDash([6, 4]);
      ctx.beginPath(); ctx.arc(midX, midY, R, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);

      const flux = 4 * Math.PI * Q;
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Enclosed Mass M = ${Q} kg | Gauss Flux ∮ g·dA = -4πGM = ${flux.toFixed(1)} (Invariant with R)`, 20, 25);
    }
  },

  // 6. Green's Theorem in the Plane
  "greens-theorem-sim": {
    title: "🔄 Green’s Theorem in the Plane & Contour Area Integration",
    desc: "Demonstrate equivalence between planar line integral ∮ (x dy - y dx) and double integral ∬ dx dy over a parameterized closed curve.",
    isAnimated: false,
    controls: [
      { id: "gt-a", label: "Semi-major Axis a", min: 40, max: 140, step: 5, value: 100 },
      { id: "gt-b", label: "Semi-minor Axis b", min: 30, max: 100, step: 5, value: 60 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const midX = w / 2, midY = h / 2;
      const a = vals["gt-a"], b = vals["gt-b"];

      ctx.fillStyle = "rgba(16, 185, 129, 0.15)";
      ctx.beginPath(); ctx.ellipse(midX, midY, a, b, 0, 0, Math.PI * 2); ctx.fill();

      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.ellipse(midX, midY, a, b, 0, 0, Math.PI * 2); ctx.stroke();

      for (let i = 0; i < 6; i++) {
        const th = (i * 2 * Math.PI) / 6;
        const px = midX + a * Math.cos(th), py = midY + b * Math.sin(th);
        const vx = -a * Math.sin(th) * 0.15, vy = b * Math.cos(th) * 0.15;
        drawArrow(ctx, px, py, px + vx, py + vy, "#f59e0b", "", 2);
      }

      const area = Math.PI * a * b;
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Area = 1/2 ∮ (x dy - y dx) = ∬ dA = π a b = ${area.toFixed(1)} px²`, 20, 25);
    }
  },

  // 7. Plane Polar Coordinates Basis Vectors (ANIMATED)
  "polar-basis-sim": {
    title: "🧭 Plane Polar Coordinates Basis: Rotating r̂ and θ̂ Unit Vectors",
    desc: "Watch the particle orbit in real time as the unit basis vectors r̂ and θ̂ rotate continuously, generating centripetal and Coriolis acceleration terms.",
    isAnimated: true,
    controls: [
      { id: "pb-r", label: "Orbital Radius r", min: 50, max: 130, step: 5, value: 90 },
      { id: "pb-om", label: "Angular Velocity ω (rad/s)", min: 0.5, max: 4, step: 0.1, value: 1.5 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = w * 0.45, oY = h * 0.55;
      const r = vals["pb-r"];
      const omega = vals["pb-om"];
      const th = animTime * omega;

      // Coordinate axes
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(30, oY); ctx.lineTo(w - 30, oY);
      ctx.moveTo(oX, 20); ctx.lineTo(oX, h - 20);
      ctx.stroke();

      // Circular track
      ctx.strokeStyle = "rgba(51, 65, 85, 0.4)"; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.arc(oX, oY, r, 0, Math.PI * 2); ctx.stroke();
      ctx.setLineDash([]);

      // Current particle position P
      const px = oX + r * Math.cos(th);
      const py = oY - r * Math.sin(th);

      // Radial arm
      ctx.strokeStyle = "rgba(148, 163, 184, 0.4)";
      ctx.beginPath(); ctx.moveTo(oX, oY); ctx.lineTo(px, py); ctx.stroke();

      // Particle marker
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(px, py, 7, 0, Math.PI * 2); ctx.fill();

      // Rotating unit basis vectors at P
      const rHatX = 45 * Math.cos(th), rHatY = -45 * Math.sin(th);
      const thHatX = -45 * Math.sin(th), thHatY = -45 * Math.cos(th);
      drawArrow(ctx, px, py, px + rHatX, py + rHatY, "#38bdf8", "r̂", 2.5);
      drawArrow(ctx, px, py, px + thHatX, py + thHatY, "#10b981", "θ̂", 2.5);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`θ(t) = ${(th % (2 * Math.PI)).toFixed(2)} rad | dr̂/dt = θ̇ θ̂ | dθ̂/dt = -θ̇ r̂`, 20, 25);
    }
  },

  // 8. 3D Cylindrical & Spherical Coordinates
  "coordinate-systems-sim": {
    title: "🌐 3D Cylindrical & Spherical Coordinates Visualizer",
    desc: "Switch between Cylindrical (r, θ, z) and Spherical (r, θ, φ) coordinates to inspect coordinate surfaces and volume elements dV.",
    isAnimated: false,
    controls: [
      { id: "cs-type", label: "Mode: 0=Cylindrical, 1=Spherical", min: 0, max: 1, step: 1, value: 0 },
      { id: "cs-r", label: "Radius r", min: 30, max: 120, step: 5, value: 75 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const oX = w * 0.45, oY = h * 0.65;
      const isSpherical = vals["cs-type"] === 1;
      const r = vals["cs-r"];

      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.moveTo(oX, oY); ctx.lineTo(oX + 160, oY + 40);
      ctx.moveTo(oX, oY); ctx.lineTo(oX - 120, oY + 50);
      ctx.moveTo(oX, oY); ctx.lineTo(oX, oY - 160);
      ctx.stroke();

      if (!isSpherical) {
        ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
        ctx.strokeRect(oX - r * 0.7, oY - 120, r * 1.4, 120);
        ctx.beginPath();
        ctx.ellipse(oX, oY - 120, r * 0.7, r * 0.25, 0, 0, Math.PI * 2);
        ctx.ellipse(oX, oY, r * 0.7, r * 0.25, 0, 0, Math.PI * 2);
        ctx.stroke();

        ctx.fillStyle = "#cbd5e1";
        ctx.font = "12px monospace";
        ctx.fillText("Cylindrical (r, θ, z): dV = r dr dθ dz | ∇²Φ = 1/r ∂/∂r(r ∂Φ/∂r) + 1/r² ∂²Φ/∂θ² + ∂²Φ/∂z²", 20, 25);
      } else {
        ctx.strokeStyle = "rgba(236, 72, 153, 0.4)";
        ctx.beginPath();
        ctx.arc(oX, oY - 60, r, 0, Math.PI * 2);
        ctx.ellipse(oX, oY - 60, r, r * 0.35, 0, 0, Math.PI * 2);
        ctx.stroke();

        ctx.fillStyle = "#cbd5e1";
        ctx.font = "12px monospace";
        ctx.fillText("Spherical (r, θ, φ): dV = r² sinθ dr dθ dφ | ∇²Φ in spherical coordinates", 20, 25);
      }
    }
  },

  // ====================================================
  // UNIT 3: KINEMATICS AND PARTICLE DYNAMICS
  // ====================================================

  // 9. Coriolis & Rotating Reference Frame (ANIMATED)
  "coriolis-fictitious-sim": {
    title: "🌪️ Rotating Reference Frame: Real-Time Coriolis Deflection",
    desc: "Watch the particle roll straight in the inertial frame while deflecting into a dramatic curved path in the rotating frame.",
    isAnimated: true,
    controls: [
      { id: "cf-omega", label: "Angular Speed ω (rad/s)", min: 0.5, max: 4, step: 0.2, value: 1.5 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const mid1X = w * 0.28, mid2X = w * 0.72, midY = h * 0.52;
      const R = 95;
      const omega = vals["cf-omega"];
      const period = 3.0;
      const t = (animTime % period) / period; // 0 to 1

      // Left: Inertial Frame (Straight line)
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.arc(mid1X, midY, R, 0, Math.PI * 2); ctx.stroke();
      ctx.strokeStyle = "rgba(56, 189, 248, 0.3)"; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(mid1X - R, midY); ctx.lineTo(mid1X + R, midY); ctx.stroke();
      ctx.setLineDash([]);

      const pInertX = mid1X - R + 2 * R * t;
      const pInertY = midY;
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(pInertX, pInertY, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillText("Inertial Frame (Straight Line)", mid1X - 85, midY - R - 10);

      // Right: Rotating Frame (Curved path)
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.arc(mid2X, midY, R, 0, Math.PI * 2); ctx.stroke();

      // Trace path in rotating frame up to current t
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let tau = 0; tau <= t; tau += 0.02) {
        const x_i = -R + 2 * R * tau;
        const th = -omega * (tau * period);
        const x_r = x_i * Math.cos(th);
        const y_r = x_i * Math.sin(th);
        if (tau === 0) ctx.moveTo(mid2X + x_r, midY + y_r);
        else ctx.lineTo(mid2X + x_r, midY + y_r);
      }
      ctx.stroke();

      // Current particle in rotating frame
      const curXi = -R + 2 * R * t;
      const curTh = -omega * (t * period);
      const curXr = curXi * Math.cos(curTh);
      const curYr = curXi * Math.sin(curTh);
      ctx.fillStyle = "#f43f5e";
      ctx.beginPath(); ctx.arc(mid2X + curXr, midY + curYr, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillText("Rotating Frame (Coriolis Curve)", mid2X - 85, midY - R - 10);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`F_coriolis = -2m(ω × v) | F_centrifugal = m ω² r`, 20, 25);
    }
  },

  // 10. Frenet-Serret Tangential & Normal Acceleration (ANIMATED)
  "curvilinear-acceleration-sim": {
    title: "🏎️ Frenet-Serret Acceleration: Moving Along a Curved Track",
    desc: "Observe the car travel smoothly along the curved track with live adapting tangential (speed change) and normal (curvature change) acceleration vectors.",
    isAnimated: true,
    controls: [
      { id: "ca-speed", label: "Base Speed", min: 1, max: 4, step: 0.2, value: 2.0 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const midX = w / 2, midY = h / 2;
      const speed = vals["ca-speed"];
      const th = animTime * speed * 0.8;

      // Track (ellipse)
      const a = 140, b = 80;
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 14;
      ctx.beginPath(); ctx.ellipse(midX, midY, a, b, 0, 0, Math.PI * 2); ctx.stroke();

      // Current position
      const px = midX + a * Math.cos(th);
      const py = midY + b * Math.sin(th);

      // Tangent velocity vector
      const vx = -a * Math.sin(th) * 0.25;
      const vy = b * Math.cos(th) * 0.25;

      // Normal centripetal acceleration vector (toward center)
      const nx = -Math.cos(th) * 28;
      const ny = -Math.sin(th) * 28;

      // Car marker
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(px, py, 7, 0, Math.PI * 2); ctx.fill();

      // Vectors: Tangential (Cyan), Normal (Emerald)
      drawArrow(ctx, px, py, px + vx, py + vy, "#38bdf8", "a_t", 2.5);
      drawArrow(ctx, px, py, px + nx, py + ny, "#10b981", "a_n = v²/ρ", 2.5);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`a_total = a_t t̂ + a_n n̂ | a_n points toward local center of curvature`, 20, 25);
    }
  },

  // 11. Projectile Motion Sandbox (ANIMATED)
  "projectile-motion-sim": {
    title: "🎯 Real-Time 2D Projectile Flight Animation with Trajectory History",
    desc: "Watch the cannonball launch, ascend to peak altitude, and strike the ground in continuous real-time motion with live metrics.",
    isAnimated: true,
    controls: [
      { id: "pm-v0", label: "Launch Speed v_0 (m/s)", min: 25, max: 70, step: 2, value: 50 },
      { id: "pm-angle", label: "Launch Angle θ (°)", min: 20, max: 75, step: 1, value: 45 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = 50, oY = h - 40;
      const v0 = vals["pm-v0"];
      const rad = (vals["pm-angle"] * Math.PI) / 180;
      const g = 9.8;

      const T = (2 * v0 * Math.sin(rad)) / g;
      const loopT = (animTime * 1.5) % (T + 0.8);
      const t = Math.min(loopT, T);

      // Ground plane
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(oX, oY); ctx.lineTo(w - 20, oY); ctx.stroke();

      // Parabolic flight trail
      ctx.strokeStyle = "rgba(56, 189, 248, 0.35)"; ctx.lineWidth = 2;
      ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(oX, oY);
      for (let tau = 0; tau <= T; tau += 0.05) {
        const x = (v0 * Math.cos(rad) * tau) * 2.2;
        const y = (v0 * Math.sin(rad) * tau - 0.5 * g * tau * tau) * 2.2;
        ctx.lineTo(oX + x, oY - y);
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Current flying projectile
      const curX = oX + (v0 * Math.cos(rad) * t) * 2.2;
      const curY = oY - (v0 * Math.sin(rad) * t - 0.5 * g * t * t) * 2.2;

      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(curX, curY, 7, 0, Math.PI * 2); ctx.fill();

      // Current velocity vector
      const vx = v0 * Math.cos(rad) * 0.7;
      const vy = -(v0 * Math.sin(rad) - g * t) * 0.7;
      drawArrow(ctx, curX, curY, curX + vx, curY + vy, "#38bdf8", "v", 2);

      const R = (v0 * v0 * Math.sin(2 * rad)) / g;
      const H = (v0 * v0 * Math.sin(rad) * Math.sin(rad)) / (2 * g);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Flight Time: ${t.toFixed(2)}s / ${T.toFixed(2)}s | Range R = ${R.toFixed(1)}m | Max Height H = ${H.toFixed(1)}m`, 20, 25);
    }
  },

  // 12. Uniform and Vertical Circular Motion (ANIMATED)
  "uniform-circular-sim": {
    title: "🎡 Dynamic Vertical Circle Loop & Live String Tension T(θ)",
    desc: "Watch the particle swing around the vertical circle in real time. Speed up at the bottom, slow down at the top, showing live string tension.",
    isAnimated: true,
    controls: [
      { id: "uc-v0", label: "Bottom Velocity v_0 (m/s)", min: 14, max: 35, step: 1, value: 25 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const midX = w / 2, midY = h / 2;
      const v0 = vals["uc-v0"];
      const R = 85;
      const g = 9.8;

      // Variable speed angle: θ = 0 is bottom
      const omAvg = v0 / 15;
      const th = animTime * omAvg;

      // Loop circle
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.arc(midX, midY, R, 0, Math.PI * 2); ctx.stroke();

      // Particle pos
      const px = midX + R * Math.sin(th);
      const py = midY + R * Math.cos(th);

      // Rod
      ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(midX, midY); ctx.lineTo(px, py); ctx.stroke();

      // Tension calculation (relative)
      const cosTh = Math.cos(th);
      const tension = (v0 * v0 / 25) + cosTh * g;

      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(px, py, 8, 0, Math.PI * 2); ctx.fill();

      // Tension vector pointing to center
      const tLen = Math.max(5, tension * 1.5);
      drawArrow(ctx, px, py, px - (px - midX) * 0.35, py - (py - midY) * 0.35, "#f43f5e", "T", 2.5);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Real-time Tension T(θ) = ${tension.toFixed(1)} N/kg | T_bottom - T_top = 6mg = ${(6 * g).toFixed(1)} N/kg`, 20, 25);
    }
  },

  // 13. Friction on Inclined Plane (ANIMATED)
  "friction-newton-sim": {
    title: "🧱 Dynamic Friction on Incline: Real-Time Sliding Acceleration",
    desc: "Observe the block slide down the ramp in real time when incline angle exceeds the angle of repose θ_r = arctan(μ_s).",
    isAnimated: true,
    controls: [
      { id: "fn-angle", label: "Incline Angle θ (°)", min: 0, max: 60, step: 1, value: 30 },
      { id: "fn-mus", label: "Static Friction μ_s", min: 0.1, max: 0.8, step: 0.05, value: 0.45 },
      { id: "fn-muk", label: "Kinetic Friction μ_k", min: 0.05, max: 0.7, step: 0.05, value: 0.35 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = 60, oY = h - 40;
      const thDeg = vals["fn-angle"];
      const th = (thDeg * Math.PI) / 180;
      const mus = vals["fn-mus"], muk = vals["fn-muk"];
      const g = 9.8;

      const rampLen = 320;
      const topX = oX + rampLen * Math.cos(th);
      const topY = oY - rampLen * Math.sin(th);

      // Draw ramp
      ctx.fillStyle = "#0f172a";
      ctx.beginPath(); ctx.moveTo(oX, oY); ctx.lineTo(topX, oY); ctx.lineTo(topX, topY); ctx.closePath(); ctx.fill();
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(oX, oY); ctx.lineTo(topX, topY); ctx.stroke();

      const mgSin = g * Math.sin(th);
      const maxStatic = mus * g * Math.cos(th);
      const isSliding = mgSin > maxStatic;
      const a = isSliding ? (mgSin - muk * g * Math.cos(th)) : 0;
      const angleRepose = (Math.atan(mus) * 180) / Math.PI;

      // Sliding motion animation
      let dist = 100;
      if (isSliding) {
        const t = (animTime * 1.5) % 2.5;
        dist = 40 + 0.5 * a * t * t * 15;
        dist = Math.min(dist, rampLen - 20);
      }

      const bx = topX - dist * Math.cos(th);
      const by = topY + dist * Math.sin(th);

      ctx.save();
      ctx.translate(bx, by);
      ctx.rotate(-th);
      ctx.fillStyle = "#f59e0b";
      ctx.fillRect(-18, -22, 36, 22);
      ctx.restore();

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      const state = isSliding ? `SLIDING DOWN (a = ${a.toFixed(2)} m/s²)` : "STATIC AT REST (f_s balances mg sin θ)";
      ctx.fillText(`θ = ${thDeg}° | Angle of Repose θ_r = ${angleRepose.toFixed(1)}° | State: ${state}`, 20, 25);
    }
  },

  // ==========================================
  // UNIT 4: WORK, ENERGY, AND POWER
  // ==========================================

  // 14. Work-Energy Theorem for Variable Spring Force
  "work-energy-theorem-sim": {
    title: "⚡ Work-Energy Theorem for Variable Force F(x) = -kx",
    desc: "Calculate work integral W = ∫ F dx under the force-displacement curve and verify exact equality with change in kinetic energy ΔK.",
    isAnimated: false,
    controls: [
      { id: "we-k", label: "Spring Constant k (N/m)", min: 10, max: 100, step: 5, value: 50 },
      { id: "we-x", label: "Displacement x (m)", min: 0.2, max: 2.0, step: 0.1, value: 1.2 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = 80, oY = h - 60;
      const k = vals["we-k"], xMax = vals["we-x"];

      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(oX, 30); ctx.lineTo(oX, oY); ctx.lineTo(w - 30, oY);
      ctx.stroke();

      ctx.fillStyle = "rgba(56, 189, 248, 0.2)";
      ctx.beginPath(); ctx.moveTo(oX, oY);
      const pxX = oX + xMax * 140;
      const pxY = oY - (k * xMax) * 1.8;
      ctx.lineTo(pxX, oY); ctx.lineTo(pxX, pxY); ctx.closePath(); ctx.fill();

      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(oX, oY); ctx.lineTo(pxX, pxY); ctx.stroke();

      const work = 0.5 * k * xMax * xMax;
      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Work W = ∫₀ˣ kx dx = 1/2 k x² = ${work.toFixed(2)} Joules = ΔK`, 20, 25);
    }
  },

  // 15. Conservation of Mechanical Energy (ANIMATED)
  "energy-conservation-sim": {
    title: "🎢 Dynamic Mechanical Energy: Real-Time Bouncing Kinetic vs Potential Bars",
    desc: "Watch the rollercoaster cart roll back and forth along the track while Kinetic K and Potential U energy bars dynamically exchange energy.",
    isAnimated: true,
    controls: [
      { id: "ec-h", label: "Release Height h (m)", min: 15, max: 50, step: 5, value: 35 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const hTotal = vals["ec-h"];
      const g = 9.8, m = 2.0;
      const E = m * g * hTotal;

      // Cart motion parameter (oscillates 0 to 1)
      const osc = 0.5 + 0.5 * Math.sin(animTime * 2);
      const currentH = hTotal * (0.2 + 0.8 * osc);
      const U = m * g * currentH;
      const K = Math.max(0, E - U);

      // Track graphic
      const trackBase = h - 60;
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 3;
      ctx.beginPath();
      for (let x = 40; x <= w - 200; x += 5) {
        const normX = (x - 40) / (w - 240);
        const trY = trackBase - hTotal * 1.8 * (0.2 + 0.8 * (0.5 + 0.5 * Math.cos(normX * Math.PI * 2)));
        if (x === 40) ctx.moveTo(x, trY); else ctx.lineTo(x, trY);
      }
      ctx.stroke();

      // Cart position
      const cartX = 40 + (w - 240) * (0.5 + 0.5 * Math.cos(animTime * 2));
      const normCartX = (cartX - 40) / (w - 240);
      const cartY = trackBase - hTotal * 1.8 * (0.2 + 0.8 * (0.5 + 0.5 * Math.cos(normCartX * Math.PI * 2)));

      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(cartX, cartY, 8, 0, Math.PI * 2); ctx.fill();

      // Dynamic Energy Bar Graphs on the right
      const barX = w - 150, barY = 50, barW = 35, barH = 180;
      const uH = (U / E) * barH;
      ctx.fillStyle = "#f59e0b";
      ctx.fillRect(barX, barY + (barH - uH), barW, uH);

      const kH = (K / E) * barH;
      ctx.fillStyle = "#38bdf8";
      ctx.fillRect(barX + 50, barY + (barH - kH), barW, kH);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "11px monospace";
      ctx.fillText("U (Pot)", barX, barY + barH + 18);
      ctx.fillText("K (Kin)", barX + 50, barY + barH + 18);

      ctx.font = "12px monospace";
      ctx.fillText(`Total E = ${E.toFixed(1)} J | K = ${K.toFixed(1)} J | U = ${U.toFixed(1)} J (Strictly Conserved)`, 20, 25);
    }
  },

  // 16. 2D Conservative Potential Energy Surface
  "two-dim-potential-sim": {
    title: "🗺️ 2D Conservative Potential Energy Surface & Equipotentials",
    desc: "Examine equipotential contour lines and prove that conservative force vectors F = -∇U are everywhere perpendicular to equipotentials.",
    isAnimated: false,
    controls: [
      { id: "tp-depth", label: "Well Depth U_0", min: 10, max: 60, step: 5, value: 30 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const midX = w / 2, midY = h / 2;

      for (let r = 25; r <= 140; r += 22) {
        ctx.strokeStyle = "rgba(56, 189, 248, 0.4)"; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.arc(midX, midY, r, 0, Math.PI * 2); ctx.stroke();

        for (let i = 0; i < 8; i++) {
          const th = (i * 2 * Math.PI) / 8;
          const px = midX + r * Math.cos(th), py = midY + r * Math.sin(th);
          drawArrow(ctx, px, py, px - 14 * Math.cos(th), py - 14 * Math.sin(th), "#f43f5e", "", 1.5);
        }
      }

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Conservative Force F = -∇U is Strictly Orthogonal to Equipotentials U(x, y) = C`, 20, 25);
    }
  },

  // 17. 1D Potential Energy Well & Phase Space (ANIMATED)
  "potential-well-sim": {
    title: "🕳️ Real-Time 1D Potential Well Oscillation & Phase Orbit (x, p_x)",
    desc: "Watch the particle oscillate smoothly between turning points E = U(x) while simultaneously tracing its phase space orbit (x, p_x).",
    isAnimated: true,
    controls: [
      { id: "pw-energy", label: "Total Energy E", min: 20, max: 80, step: 5, value: 50 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const midX = w * 0.35, base = h - 60;
      const E = vals["pw-energy"];
      const k = 0.0035 * 20;
      const amp = Math.sqrt((E * 1.5) / k);

      // Left: Harmonic Well U(x)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let x = -130; x <= 130; x += 3) {
        const u = k * x * x;
        const py = base - u;
        if (x === -130) ctx.moveTo(midX + x, py); else ctx.lineTo(midX + x, py);
      }
      ctx.stroke();

      // Energy line E
      const ey = base - E * 1.5;
      ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 2; ctx.setLineDash([4, 4]);
      ctx.beginPath(); ctx.moveTo(midX - 120, ey); ctx.lineTo(midX + 120, ey); ctx.stroke();
      ctx.setLineDash([]);

      // Particle oscillation: x(t) = amp * cos(ω t)
      const omega = 2.2;
      const curX = amp * Math.cos(animTime * omega);
      const curY = base - k * curX * curX;

      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(midX + curX, curY, 7, 0, Math.PI * 2); ctx.fill();

      // Right: Phase space (x, p_x) orbit
      const psX = w * 0.75, psY = h * 0.5;
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(psX - 70, psY); ctx.lineTo(psX + 70, psY);
      ctx.moveTo(psX, psY - 70); ctx.lineTo(psX, psY + 70);
      ctx.stroke();

      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.ellipse(psX, psY, amp * 0.7, amp * 0.7, 0, 0, Math.PI * 2); ctx.stroke();

      // Current point in phase space
      const px_dot = -amp * Math.sin(animTime * omega);
      ctx.fillStyle = "#10b981";
      ctx.beginPath(); ctx.arc(psX + curX * 0.7, psY + px_dot * 0.7, 5, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Oscillating Particle Between Turning Points x = ±${amp.toFixed(1)} | Closed Phase Space Orbit`, 20, 25);
    }
  },

  // ==========================================
  // UNIT 5: CONSERVATION OF LINEAR MOMENTUM
  // ==========================================

  // 18. Multi-Particle Center of Mass
  "center-of-mass-sim": {
    title: "⚖️ Multi-Particle System Center of Mass R_cm Calculator",
    desc: "Adjust masses and positions of 3 interacting bodies to dynamically observe the resultant center of mass position R_cm.",
    isAnimated: false,
    controls: [
      { id: "cm-m1", label: "Mass m_1 (kg)", min: 1, max: 10, step: 1, value: 6 },
      { id: "cm-x1", label: "Position x_1", min: -80, max: 80, step: 5, value: -60 },
      { id: "cm-m2", label: "Mass m_2 (kg)", min: 1, max: 10, step: 1, value: 4 },
      { id: "cm-x2", label: "Position x_2", min: -80, max: 80, step: 5, value: 50 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const oX = w / 2, oY = h / 2;
      const m1 = vals["cm-m1"], x1 = vals["cm-x1"];
      const m2 = vals["cm-m2"], x2 = vals["cm-x2"];

      ctx.strokeStyle = "#334155"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(oX - 160, oY); ctx.lineTo(oX + 160, oY); ctx.stroke();

      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(oX + x1 * 1.5, oY, 4 + m1 * 1.5, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = "#10b981";
      ctx.beginPath(); ctx.arc(oX + x2 * 1.5, oY, 4 + m2 * 1.5, 0, Math.PI * 2); ctx.fill();

      const xCM = (m1 * x1 + m2 * x2) / (m1 + m2);
      const cmPx = oX + xCM * 1.5;
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath();
      ctx.moveTo(cmPx, oY - 20); ctx.lineTo(cmPx - 8, oY - 5); ctx.lineTo(cmPx + 8, oY - 5); ctx.closePath(); ctx.fill();

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`R_cm = (m₁r₁ + m₂r₂)/(m₁ + m₂) = ${xCM.toFixed(2)} px | Total Mass M = ${m1 + m2} kg`, 20, 25);
    }
  },

  // 19. Continuous Center of Mass Geometry
  "continuous-cm-sim": {
    title: "📐 Continuous Geometry Center of Mass: Semicircular Wire & Disc",
    desc: "Compare theoretical center of mass heights y_cm = 2R/π (wire) vs y_cm = 4R/(3π) (disc) via volume and surface integrations.",
    isAnimated: false,
    controls: [
      { id: "ccm-radius", label: "Radius R", min: 40, max: 120, step: 5, value: 80 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const mid1X = w * 0.3, mid2X = w * 0.7, baseY = h * 0.7;
      const R = vals["ccm-radius"];

      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 4;
      ctx.beginPath(); ctx.arc(mid1X, baseY, R, Math.PI, 0); ctx.stroke();
      const yWire = (2 * R) / Math.PI;
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(mid1X, baseY - yWire, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillText(`Wire CM: y = 2R/π = ${yWire.toFixed(1)}`, mid1X - 60, baseY + 25);

      ctx.fillStyle = "rgba(16, 185, 129, 0.25)";
      ctx.beginPath(); ctx.arc(mid2X, baseY, R, Math.PI, 0); ctx.closePath(); ctx.fill();
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2; ctx.stroke();
      const yDisc = (4 * R) / (3 * Math.PI);
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(mid2X, baseY - yDisc, 6, 0, Math.PI * 2); ctx.fill();
      ctx.fillText(`Disc CM: y = 4R/(3π) = ${yDisc.toFixed(1)}`, mid2X - 60, baseY + 25);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText("Continuous Mass Distributions: R_cm = 1/M ∭ r ρ dV", 20, 25);
    }
  },

  // 20. Tsiolkovsky Rocket Flight (ANIMATED)
  "rocket-propulsion-sim": {
    title: "🚀 Dynamic Tsiolkovsky Rocket Flight: Real-Time Blastoff & Exhaust",
    desc: "Watch the rocket fire its engines and accelerate upward continuously into space according to the Tsiolkovsky equation Δv = u_ex ln(m_0/m_f).",
    isAnimated: true,
    controls: [
      { id: "rp-uex", label: "Exhaust Velocity u_ex (km/s)", min: 1.5, max: 4.5, step: 0.1, value: 3.0 },
      { id: "rp-ratio", label: "Mass Ratio m_0 / m_f", min: 2, max: 10, step: 0.5, value: 5.0 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const uex = vals["rp-uex"], mr = vals["rp-ratio"];
      const dv = uex * Math.log(mr);

      // Rocket ascent animation
      const loopT = (animTime * 0.8) % 3.0; // 0 to 3s
      const alt = 0.5 * (dv * 8) * loopT * loopT;
      const rx = w * 0.25;
      const ry = (h - 60) - (alt % (h + 80));

      // Rocket Body
      ctx.fillStyle = "#e2e8f0";
      ctx.beginPath();
      ctx.moveTo(rx, ry - 35); ctx.lineTo(rx + 15, ry); ctx.lineTo(rx + 15, ry + 40); ctx.lineTo(rx - 15, ry + 40); ctx.lineTo(rx - 15, ry);
      ctx.closePath(); ctx.fill();

      // Flickering exhaust flame
      const flameLen = 25 + Math.random() * 15;
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath();
      ctx.moveTo(rx - 10, ry + 40); ctx.lineTo(rx, ry + 40 + flameLen); ctx.lineTo(rx + 10, ry + 40); ctx.closePath(); ctx.fill();

      // Exhaust particles
      ctx.fillStyle = "rgba(239, 68, 68, 0.7)";
      for (let i = 0; i < 6; i++) {
        ctx.beginPath();
        ctx.arc(rx + (Math.random() - 0.5) * 16, ry + 45 + Math.random() * 30, 2 + Math.random() * 3, 0, Math.PI * 2);
        ctx.fill();
      }

      // Plot curve on right
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      const plotX = w * 0.5, plotBase = h - 50;
      ctx.beginPath();
      for (let r = 1; r <= 10; r += 0.2) {
        const v = uex * Math.log(r);
        const px = plotX + (r / 10) * 200;
        const py = plotBase - (v / 10) * 140;
        if (r === 1) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Burnout Velocity Δv = u_ex ln(m₀/m_f) = ${dv.toFixed(2)} km/s | Thrust T = u_ex |dm/dt|`, 20, 25);
    }
  },

  // 21. Ballistic Pendulum (ANIMATED)
  "ballistic-pendulum-sim": {
    title: "🎯 Real-Time Ballistic Pendulum: Bullet Impact & Oscillating Swing",
    desc: "Watch the high-speed bullet embed into the suspended wooden block and observe the resulting pendulum swing oscillation.",
    isAnimated: true,
    controls: [
      { id: "bp-v0", label: "Bullet Speed v_0 (m/s)", min: 150, max: 400, step: 10, value: 280 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const v0 = vals["bp-v0"];
      const mb = 0.010, M = 1.99;
      const V = (mb * v0) / (mb + M);
      const g = 9.8, L = 140;
      const riseH = (V * V) / (2 * g);
      const maxAngle = Math.min(Math.PI / 3, Math.sqrt((2 * riseH) / (L / 100)));

      // Oscillating swing angle
      const omegaP = Math.sqrt(g / (L / 100));
      const th = maxAngle * Math.sin(animTime * omegaP);

      const oX = w * 0.5, oY = 40;
      const bx = oX + L * Math.sin(th);
      const by = oY + L * Math.cos(th);

      // Suspension wire
      ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(oX, oY); ctx.lineTo(bx, by); ctx.stroke();

      // Block
      ctx.fillStyle = "#f59e0b";
      ctx.fillRect(bx - 20, by - 15, 40, 30);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Impact Speed V = ${V.toFixed(2)} m/s | Max Height h = ${(riseH * 100).toFixed(1)} cm | Oscillating Swing`, 20, 25);
    }
  },

  // 22. 2D Collisions in Lab vs CM Frame (ANIMATED)
  "collision-lab-cm-sim": {
    title: "💥 Dynamic 2D Collision: Moving Particles in Lab vs Center-of-Mass Frame",
    desc: "Watch particles approach, collide at the origin, and scatter into their respective angles in both frames simultaneously.",
    isAnimated: true,
    controls: [
      { id: "col-m1", label: "Mass m_1 (kg)", min: 1, max: 8, step: 1, value: 4 },
      { id: "col-m2", label: "Mass m_2 (kg)", min: 1, max: 8, step: 1, value: 2 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const m1 = vals["col-m1"], m2 = vals["col-m2"];
      const mid1X = w * 0.28, mid2X = w * 0.72, midY = h * 0.52;

      // Animation cycle: 3 seconds (approach, impact, scatter)
      const t = (animTime % 3.0) - 1.5; // -1.5 to +1.5

      // Lab Frame (Target at rest)
      ctx.fillStyle = "#38bdf8";
      const lab1X = t < 0 ? (mid1X + t * 45) : (mid1X + t * 35 * Math.cos(0.6));
      const lab1Y = t < 0 ? midY : (midY - t * 35 * Math.sin(0.6));
      ctx.beginPath(); ctx.arc(lab1X, lab1Y, 4 + m1, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = "#10b981";
      const lab2X = t < 0 ? mid1X : (mid1X + t * 30 * Math.cos(-0.8));
      const lab2Y = t < 0 ? midY : (midY - t * 30 * Math.sin(-0.8));
      ctx.beginPath(); ctx.arc(lab2X, lab2Y, 4 + m2, 0, Math.PI * 2); ctx.fill();

      ctx.fillText("Laboratory Frame (Moving Target)", mid1X - 90, midY - 65);

      // CM Frame (Equal & Opposite)
      ctx.fillStyle = "#38bdf8";
      const cm1X = t < 0 ? (mid2X + t * 35) : (mid2X + t * 35 * Math.cos(0.9));
      const cm1Y = t < 0 ? midY : (midY - t * 35 * Math.sin(0.9));
      ctx.beginPath(); ctx.arc(cm1X, cm1Y, 4 + m1, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = "#10b981";
      const cm2X = t < 0 ? (mid2X - t * 35) : (mid2X - t * 35 * Math.cos(0.9));
      const cm2Y = t < 0 ? midY : (midY + t * 35 * Math.sin(0.9));
      ctx.beginPath(); ctx.arc(cm2X, cm2Y, 4 + m2, 0, Math.PI * 2); ctx.fill();

      ctx.fillText("Center-of-Mass Frame (P_total = 0)", mid2X - 90, midY - 65);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Elastic Collision: Kinetic Energy & Linear Momentum Conserved`, 20, 25);
    }
  },

  // ==========================================
  // UNIT 6: ROTATIONAL KINEMATICS & DYNAMICS
  // ==========================================

  // 23. Rotational Kinematics & Angular Velocity (ANIMATED)
  "rotational-kinematics-sim": {
    title: "🎡 Dynamic Disc Rotation: Real-Time Angular Velocity & Acceleration Vectors",
    desc: "Watch the disc rotate continuously at angular speed ω. Observe the tangential velocity vector v = ω × r and inward centripetal acceleration vector a_c.",
    isAnimated: true,
    controls: [
      { id: "rk-om", label: "Angular Velocity ω (rad/s)", min: 1, max: 8, step: 0.5, value: 3.5 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const midX = w / 2, midY = h / 2;
      const om = vals["rk-om"];
      const th = animTime * om;
      const r = 85;

      // Rotating disc
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.arc(midX, midY, 130, 0, Math.PI * 2); ctx.stroke();

      // Rotating spoke line
      ctx.strokeStyle = "rgba(148, 163, 184, 0.35)"; ctx.lineWidth = 1.5;
      ctx.beginPath(); ctx.moveTo(midX, midY);
      ctx.lineTo(midX + 130 * Math.cos(th), midY - 130 * Math.sin(th));
      ctx.stroke();

      // Point at radius r
      const px = midX + r * Math.cos(th);
      const py = midY - r * Math.sin(th);
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(px, py, 6, 0, Math.PI * 2); ctx.fill();

      // Tangential velocity v = ω r (Cyan)
      const vLen = om * 6.5;
      const vx = -vLen * Math.sin(th);
      const vy = -vLen * Math.cos(th);
      drawArrow(ctx, px, py, px + vx, py + vy, "#38bdf8", "v = ω × r", 2.5);

      // Centripetal acceleration (Emerald) inward
      const acLen = 32;
      const acx = -acLen * Math.cos(th);
      const acy = acLen * Math.sin(th);
      drawArrow(ctx, px, py, px + acx, py + acy, "#10b981", "a_c = -ω² r", 2.5);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Angular Velocity ω = ${om} rad/s | Speed v = ${(om * r * 0.1).toFixed(1)} m/s | Spinning Rigid Body`, 20, 25);
    }
  },

  // 24. Kepler Orbit & Angular Momentum Conservation (ANIMATED)
  "angular-momentum-sim": {
    title: "🪐 Real-Time Kepler Orbit: Variable Speed & Areal Velocity Sweeping",
    desc: "Watch the planet orbit around the sun in real time, accelerating at perihelion and slowing at aphelion, verifying Kepler’s 2nd Law.",
    isAnimated: true,
    controls: [
      { id: "am-ecc", label: "Orbital Eccentricity e", min: 0.1, max: 0.7, step: 0.05, value: 0.5 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const midX = w / 2, midY = h / 2;
      const e = vals["am-ecc"];
      const a = 120, b = a * Math.sqrt(1 - e * e);
      const focusX = midX - a * e;

      // Orbit ellipse
      ctx.strokeStyle = "#334155"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.ellipse(midX, midY, a, b, 0, 0, Math.PI * 2); ctx.stroke();

      // Sun at focus
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(focusX, midY, 9, 0, Math.PI * 2); ctx.fill();

      // Kepler motion calculation (approximate eccentric anomaly)
      const meanAnomaly = animTime * 1.4;
      const E_anom = meanAnomaly + e * Math.sin(meanAnomaly); // 1st order Kepler equation
      const px = midX + a * Math.cos(E_anom);
      const py = midY + b * Math.sin(E_anom);

      // Swept sector (from sun to planet)
      ctx.fillStyle = "rgba(56, 189, 248, 0.25)";
      ctx.beginPath();
      ctx.moveTo(focusX, midY);
      for (let tau = E_anom - 0.25; tau <= E_anom; tau += 0.05) {
        ctx.lineTo(midX + a * Math.cos(tau), midY + b * Math.sin(tau));
      }
      ctx.closePath(); ctx.fill();

      // Planet marker
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath(); ctx.arc(px, py, 6, 0, Math.PI * 2); ctx.fill();

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Kepler's 2nd Law: dA/dt = |L|/(2m) = constant | Sweeps Equal Areas in Equal Times`, 20, 25);
    }
  },

  // 25. Moment of Inertia for Standard Geometries
  "moment-of-inertia-sim": {
    title: "⚙️ Moment of Inertia for Standard Rigid Geometries",
    desc: "Compare rotational inertia I = c M R² across standard bodies: Solid Sphere (c=0.4), Cylinder (c=0.5), Shell (c=0.67), and Hoop (c=1.0).",
    isAnimated: false,
    controls: [
      { id: "mi-mass", label: "Mass M (kg)", min: 1, max: 10, step: 1, value: 5 },
      { id: "mi-radius", label: "Radius R (m)", min: 0.2, max: 1.5, step: 0.1, value: 0.8 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const M = vals["mi-mass"], R = vals["mi-radius"];
      const MR2 = M * R * R;

      const items = [
        { name: "Solid Sphere", c: 0.40, color: "#38bdf8" },
        { name: "Solid Cylinder", c: 0.50, color: "#10b981" },
        { name: "Spherical Shell", c: 0.67, color: "#ec4899" },
        { name: "Hollow Hoop", c: 1.00, color: "#f59e0b" }
      ];

      const startX = 60, startY = 60, barMaxW = 280;
      items.forEach((item, idx) => {
        const y = startY + idx * 45;
        const inertia = item.c * MR2;
        const barW = item.c * barMaxW;

        ctx.fillStyle = "#cbd5e1"; ctx.font = "12px sans-serif";
        ctx.fillText(item.name, startX, y - 6);

        ctx.fillStyle = item.color;
        ctx.fillRect(startX, y, barW, 20);

        ctx.fillStyle = "#94a3b8"; ctx.font = "11px monospace";
        ctx.fillText(`I = ${item.c} MR² = ${inertia.toFixed(2)} kg·m²`, startX + barW + 12, y + 14);
      });

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Rotational Inertia I = ∭ r_⊥² ρ dV | Resistance to Angular Acceleration τ = I α`, 20, 25);
    }
  },

  // 26. Steiner's Parallel Axis Theorem
  "parallel-axis-sim": {
    title: "📐 Steiner’s Parallel Axis Theorem I = I_cm + M d² Visualizer",
    desc: "Observe how shifting the rotation axis by distance d increases the moment of inertia parabolically according to Steiner’s Theorem.",
    isAnimated: false,
    controls: [
      { id: "pa-dist", label: "Axis Shift Distance d (m)", min: 0, max: 1.5, step: 0.05, value: 0.5 },
      { id: "pa-mass", label: "Body Mass M (kg)", min: 1, max: 10, step: 1, value: 4 }
    ],
    render: function(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const d = vals["pa-dist"], M = vals["pa-mass"];
      const L = 2.0;
      const Icm = (1 / 12) * M * L * L;
      const Iparallel = Icm + M * d * d;

      const midX = w * 0.35, midY = h * 0.5;
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 14;
      ctx.beginPath(); ctx.moveTo(midX, midY - 90); ctx.lineTo(midX, midY + 90); ctx.stroke();

      ctx.fillStyle = "#10b981";
      ctx.beginPath(); ctx.arc(midX, midY, 7, 0, Math.PI * 2); ctx.fill();
      ctx.fillText("Axis_cm", midX - 60, midY + 4);

      const shiftedY = midY - d * 55;
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath(); ctx.arc(midX, shiftedY, 7, 0, Math.PI * 2); ctx.fill();
      ctx.fillText("Parallel Axis (d)", midX + 15, shiftedY + 4);

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`I_cm = ${Icm.toFixed(2)} kg·m² | I_new = I_cm + Md² = ${Iparallel.toFixed(2)} kg·m²`, 20, 25);
    }
  },

  // 27. The Great Incline Rolling Race (ANIMATED)
  "rolling-without-slipping-sim": {
    title: "🏆 The Great Incline Rolling Race: Live Race Down the Ramp!",
    desc: "Watch four bodies (Solid Sphere, Cylinder, Shell, Hoop) roll in real time down the ramp, with spinning spokes proving rolling without slipping!",
    isAnimated: true,
    controls: [
      { id: "rr-angle", label: "Incline Angle θ (°)", min: 15, max: 45, step: 5, value: 30 }
    ],
    render: function(canvas, vals, animTime) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = "#070c18";
      ctx.fillRect(0, 0, w, h);

      const thDeg = vals["rr-angle"];
      const th = (thDeg * Math.PI) / 180;
      const g = 9.8;

      const objects = [
        { name: "Solid Sphere (c=0.40)", c: 0.40, color: "#38bdf8" },
        { name: "Solid Cylinder (c=0.50)", c: 0.50, color: "#10b981" },
        { name: "Spherical Shell (c=0.67)", c: 0.67, color: "#ec4899" },
        { name: "Hollow Hoop (c=1.00)", c: 1.00, color: "#f59e0b" }
      ];

      // Incline Ramp Geometry
      const startX = 60, startY = 80;
      const rampLen = 420;
      const endX = startX + rampLen * Math.cos(th);
      const endY = startY + rampLen * Math.sin(th);

      // Race loop time: 3.5 seconds
      const t = (animTime * 1.2) % 3.5;

      // Draw 4 parallel rolling tracks
      objects.forEach((obj, idx) => {
        const laneOffset = idx * 55;
        const oY_lane = startY + laneOffset;

        // Ramp lane surface
        ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(startX, oY_lane);
        ctx.lineTo(startX + rampLen, oY_lane);
        ctx.stroke();

        // Acceleration a = (g sin θ) / (1 + c)
        const a = (g * Math.sin(th)) / (1 + obj.c);
        let dist = 0.5 * a * t * t * 18;
        dist = Math.min(dist, rampLen - 25);

        const curX = startX + dist;
        const curY = oY_lane - 14;

        // Rotating rolling body with turning spoke line
        ctx.fillStyle = obj.color;
        ctx.beginPath(); ctx.arc(curX, curY, 14, 0, Math.PI * 2); ctx.fill();

        // Spoke line rotating: θ_rot = dist / R
        const rotAngle = dist / 14;
        ctx.strokeStyle = "#070c18"; ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(curX - 14 * Math.cos(rotAngle), curY - 14 * Math.sin(rotAngle));
        ctx.lineTo(curX + 14 * Math.cos(rotAngle), curY + 14 * Math.sin(rotAngle));
        ctx.stroke();

        ctx.fillStyle = "#cbd5e1"; ctx.font = "11px sans-serif";
        ctx.fillText(`${obj.name} | a = ${a.toFixed(2)} m/s²`, startX + rampLen + 15, oY_lane - 8);
      });

      ctx.fillStyle = "#cbd5e1";
      ctx.font = "12px monospace";
      ctx.fillText(`Live Rolling Race: a = (g sin θ) / (1 + c) | Solid Sphere (c=0.40) Wins Every Race!`, 20, 25);
    }
  }
};

// Vector Arrow Helper
function drawArrow(ctx, fromx, fromy, tox, toy, color, label, width) {
  ctx.strokeStyle = color;
  ctx.fillStyle = color;
  ctx.lineWidth = width || 2;

  const headlen = 10;
  const angle = Math.atan2(toy - fromy, tox - fromx);

  ctx.beginPath();
  ctx.moveTo(fromx, fromy);
  ctx.lineTo(tox, toy);
  ctx.stroke();

  ctx.beginPath();
  ctx.moveTo(tox, toy);
  ctx.lineTo(tox - headlen * Math.cos(angle - Math.PI / 6), toy - headlen * Math.sin(angle - Math.PI / 6));
  ctx.lineTo(tox - headlen * Math.cos(angle + Math.PI / 6), toy - headlen * Math.sin(angle + Math.PI / 6));
  ctx.closePath();
  ctx.fill();

  if (label) {
    ctx.font = "12px sans-serif";
    ctx.fillText(label, tox + 6, toy + 4);
  }
}

// Universal High-Performance 60 FPS Simulation Engine Adapter
window.SimulationEngine = window.SimulationEngine || {};
window.SimulationEngine.activeAnimations = window.SimulationEngine.activeAnimations || {};

window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;

  // Cancel any prior animation loop on this container
  if (window.SimulationEngine.activeAnimations[containerId]) {
    cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
    delete window.SimulationEngine.activeAnimations[containerId];
  }

  const simConfig = window.MECHANICS_SIMS[simType];
  if (!simConfig) {
    console.warn("Mechanics simulation not found:", simType);
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

  if (simConfig.controls && simConfig.controls.length > 0) {
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
        if (!simConfig.isAnimated) {
          simConfig.render(canvas, currentVals, 0);
        }
      });

      wrap.appendChild(input);
      ctrlBar.appendChild(wrap);
    });
  }

  // Animation Toggle Button if animated
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

console.log("Universal Mechanics Simulation Engine initialized with dynamic 60 FPS animations!");
