// Classical Mechanics & Special Relativity Interactive Simulation Engine
// 15 Interactive 60-FPS Canvas Simulations for Lagrangian, Hamiltonian & Relativistic Dynamics

window.CM_SIMS = {

  // 1. Particle System Momentum & Center of Mass
  "particle-system-momentum-sim": {
    title: "Particle System Dynamics & Center of Mass Conservation",
    desc: "Observe how internal collision forces cannot accelerate the center of mass (v_CM = const) while individual particle momenta change dynamically.",
    isAnimated: true,
    controls: [
      { id: "m1", label: "Mass 1 (kg)", min: 1, max: 10, step: 0.5, value: 3 },
      { id: "m2", label: "Mass 2 (kg)", min: 1, max: 10, step: 0.5, value: 5 },
      { id: "e", label: "Restitution Coeff (e)", min: 0.1, max: 1.0, step: 0.05, value: 0.95 }
    ],
    p1: { x: 80, y: 150, vx: 3.5, vy: 1.2 },
    p2: { x: 380, y: 180, vx: -2.5, vy: -0.8 },
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const m1 = vals.m1 || 3, m2 = vals.m2 || 5, e = vals.e || 0.95;

      // Update positions
      this.p1.x += this.p1.vx; this.p1.y += this.p1.vy;
      this.p2.x += this.p2.vx; this.p2.y += this.p2.vy;

      // Boundary bounce
      const r1 = 12 + m1 * 1.5, r2 = 12 + m2 * 1.5;
      if (this.p1.x < r1 || this.p1.x > w - r1) this.p1.vx *= -1;
      if (this.p1.y < r1 || this.p1.y > h - r1) this.p1.vy *= -1;
      if (this.p2.x < r2 || this.p2.x > w - r2) this.p2.vx *= -1;
      if (this.p2.y < r2 || this.p2.y > h - r2) this.p2.vy *= -1;

      // Collision between particles
      const dx = this.p2.x - this.p1.x, dy = this.p2.y - this.p1.y;
      const dist = Math.hypot(dx, dy);
      if (dist < r1 + r2) {
        const nx = dx / dist, ny = dy / dist;
        const kx = this.p1.vx - this.p2.vx, ky = this.p1.vy - this.p2.vy;
        const p = 2 * (nx * kx + ny * ky) / (m1 + m2) * (1 + e) / 2;
        this.p1.vx -= p * m2 * nx; this.p1.vy -= p * m2 * ny;
        this.p2.vx += p * m1 * nx; this.p2.vy += p * m1 * ny;
      }

      // Center of mass
      const cx = (m1 * this.p1.x + m2 * this.p2.x) / (m1 + m2);
      const cy = (m1 * this.p1.y + m2 * this.p2.y) / (m1 + m2);

      // Draw connecting line
      ctx.strokeStyle = "rgba(148, 163, 184, 0.25)";
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(this.p1.x, this.p1.y);
      ctx.lineTo(this.p2.x, this.p2.y);
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw CM
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath();
      ctx.arc(cx, cy, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#fbbf24";
      ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Center of Mass (R)", cx + 10, cy - 8);

      // Draw Particle 1
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath();
      ctx.arc(this.p1.x, this.p1.y, r1, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.fillText(`m1 = ${m1}kg`, this.p1.x - 18, this.p1.y - r1 - 6);

      // Draw Particle 2
      ctx.fillStyle = "#ec4899";
      ctx.beginPath();
      ctx.arc(this.p2.x, this.p2.y, r2, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.fillText(`m2 = ${m2}kg`, this.p2.x - 18, this.p2.y - r2 - 6);

      // Header Readout
      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px monospace";
      const P_total_mag = Math.hypot(m1 * this.p1.vx + m2 * this.p2.vx, m1 * this.p1.vy + m2 * this.p2.vy);
      ctx.fillText(`Total Momentum |P|: ${P_total_mag.toFixed(2)} kg·m/s (Conserved)`, 20, 30);
      ctx.fillText(`P_total = m1 v1 + m2 v2 = M V_CM`, 20, 50);
    }
  },

  // 2. Bead on Rotating Wire Hoop (Pitchfork Bifurcation)
  "rotating-wire-hoop-sim": {
    title: "Bead on a Uniformly Rotating Wire Hoop: Pitchfork Bifurcation",
    desc: "Observe the supercritical pitchfork bifurcation at critical rotation speed ω_c = √(g/R). For ω < ω_c, θ=0 is stable; for ω > ω_c, θ=0 becomes unstable and symmetric equilibrium angles cos θ* = g/(R ω²) emerge.",
    isAnimated: true,
    controls: [
      { id: "omega", label: "Hoop Spin Rate ω (rad/s)", min: 1, max: 15, step: 0.2, value: 5 },
      { id: "radius", label: "Hoop Radius R (m)", min: 0.5, max: 2.0, step: 0.1, value: 1.0 }
    ],
    theta: 0.05,
    theta_dot: 0,
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const omega = vals.omega || 5;
      const R = vals.radius || 1.0;
      const g = 9.81;
      const omega_c = Math.sqrt(g / R);

      // Equation of motion: θ̈ = (ω² cos θ - g/R) sin θ - damping * θ̇
      const dt = 0.02;
      for (let s = 0; s < 5; s++) {
        const theta_ddot = (omega * omega * Math.cos(this.theta) - g / R) * Math.sin(this.theta) - 0.8 * this.theta_dot;
        this.theta_dot += theta_ddot * (dt / 5);
        this.theta += this.theta_dot * (dt / 5);
      }

      const cx = w * 0.45, cy = h * 0.5;
      const hoopRad = Math.min(w, h) * 0.35;

      // Draw rotating circular hoop (perspective ellipse)
      const squash = 0.3 + 0.7 * Math.abs(Math.cos(time * 0.003 * omega));
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.ellipse(cx, cy, hoopRad * squash, hoopRad, 0, 0, Math.PI * 2);
      ctx.stroke();

      // Draw vertical spin axis
      ctx.strokeStyle = "rgba(148, 163, 184, 0.5)";
      ctx.lineWidth = 1.5;
      ctx.setLineDash([5, 5]);
      ctx.beginPath();
      ctx.moveTo(cx, cy - hoopRad - 25);
      ctx.lineTo(cx, cy + hoopRad + 25);
      ctx.stroke();
      ctx.setLineDash([]);

      // Bead position
      const beadX = cx + hoopRad * squash * Math.sin(this.theta);
      const beadY = cy + hoopRad * Math.cos(this.theta);

      // Draw bead
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath();
      ctx.arc(beadX, beadY, 11, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 2;
      ctx.stroke();

      // Theoretical equilibrium calculation
      let eqAngleDeg = 0;
      let state = "Subcritical: Single Stable Minimum at θ = 0°";
      if (omega > omega_c) {
        const cos_th = (g / R) / (omega * omega);
        eqAngleDeg = Math.acos(cos_th) * 180 / Math.PI;
        state = `Supercritical: Bifurcated Equilibrium θ* = ±${eqAngleDeg.toFixed(1)}°`;
      }

      // Information Panel
      ctx.fillStyle = "#e2e8f0";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Bifurcation State:", w * 0.62, 40);
      ctx.font = "12px Inter, sans-serif";
      ctx.fillStyle = omega > omega_c ? "#10b981" : "#38bdf8";
      ctx.fillText(state, w * 0.62, 60);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px monospace";
      ctx.fillText(`Rotation Speed: ω = ${omega.toFixed(1)} rad/s`, w * 0.62, 90);
      ctx.fillText(`Critical Speed: ω_c = ${omega_c.toFixed(2)} rad/s`, w * 0.62, 110);
      ctx.fillText(`Instantaneous θ: ${(this.theta * 180 / Math.PI).toFixed(1)}°`, w * 0.62, 130);
      ctx.fillText(`Stability: ${omega > omega_c ? "θ=0 UNSTABLE" : "θ=0 STABLE"}`, w * 0.62, 150);
    }
  },

  // 3. The Brachistochrone Race
  "brachistochrone-sim": {
    title: "The Brachistochrone Problem: Cycloid vs Straight vs Circle",
    desc: "Interactive demonstration of the calculus of variations. Watch three beads race from (0,0) to (x2, y2) under gravity: Cycloid (fastest path), Straight Line, and Circular Arc.",
    isAnimated: true,
    controls: [
      { id: "gravity", label: "Gravity g (m/s²)", min: 5, max: 20, step: 0.5, value: 9.81 },
      { id: "reset", label: "Rerun Race (Toggle 0/1)", min: 0, max: 1, step: 1, value: 0 }
    ],
    t: 0,
    lastReset: 0,
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      if (vals.reset !== this.lastReset) {
        this.t = 0;
        this.lastReset = vals.reset;
      }
      this.t += 0.016;

      const g = vals.gravity || 9.81;
      const x0 = 50, y0 = 60;
      const x1 = w - 80, y1 = h - 60;

      // Draw Paths
      // 1. Straight Line Path
      ctx.strokeStyle = "#94a3b8";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(x0, y0);
      ctx.lineTo(x1, y1);
      ctx.stroke();

      // 2. Cycloid Path
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3;
      ctx.beginPath();
      const numPoints = 80;
      const cycloidPts = [];
      const theta_max = 2.412; // approximate parameter for endpoint
      const a = (x1 - x0) / (theta_max - Math.sin(theta_max));
      for (let i = 0; i <= numPoints; i++) {
        const th = (i / numPoints) * theta_max;
        const px = x0 + a * (th - Math.sin(th));
        const py = y0 + a * (1 - Math.cos(th));
        cycloidPts.push({ x: px, y: py });
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Approximate transit times
      const T_cycloid = Math.PI * Math.sqrt(a / g) * 0.76;
      const T_straight = Math.sqrt(2 * Math.hypot(x1 - x0, y1 - y0) / (g * Math.sin(Math.atan2(y1 - y0, x1 - x0)))) * 0.45;

      // Cycloid Bead
      const fracC = Math.min(1.0, this.t / T_cycloid);
      const idxC = Math.floor(fracC * (cycloidPts.length - 1));
      const ptC = cycloidPts[idxC];
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath();
      ctx.arc(ptC.x, ptC.y, 8, 0, Math.PI * 2);
      ctx.fill();

      // Straight Line Bead
      const fracS = Math.min(1.0, this.t / T_straight);
      const ptS = { x: x0 + fracS * (x1 - x0), y: y0 + fracS * (y1 - y0) };
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath();
      ctx.arc(ptS.x, ptS.y, 8, 0, Math.PI * 2);
      ctx.fill();

      // Labels & Legend
      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`● Cycloid (Euler-Lagrange Extremum) - T: ${T_cycloid.toFixed(2)}s`, 60, 30);
      ctx.fillStyle = "#f59e0b";
      ctx.fillText(`● Straight Line Path - T: ${T_straight.toFixed(2)}s`, 60, 50);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px monospace";
      ctx.fillText(`Race Elapsed Time: ${this.t.toFixed(2)}s`, w - 240, 30);
    }
  },

  // 4. Double Pendulum & Deterministic Chaos
  "double-pendulum-sim": {
    title: "Double Pendulum: Nonlinear Dynamics & Chaotic Phase Space",
    desc: "Numerical Runge-Kutta simulation of the coupled nonlinear double pendulum. Observe extreme sensitivity to initial conditions and the transition from regular normal modes to deterministic chaos.",
    isAnimated: true,
    controls: [
      { id: "length", label: "Rod Length l (m)", min: 0.5, max: 1.5, step: 0.1, value: 1.0 },
      { id: "energy", label: "Initial Energy (Angle θ1 deg)", min: 10, max: 170, step: 5, value: 90 }
    ],
    th1: 1.5, th2: 1.5,
    w1: 0, w2: 0,
    trail: [],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const l = (vals.length || 1.0) * 85;
      const g = 9.81 * 80;
      const m1 = 1.0, m2 = 1.0;

      // Runge-Kutta 4th Order Physics Step
      const dt = 0.03;
      for (let step = 0; step < 4; step++) {
        const delta = this.th1 - this.th2;
        const den1 = l * (2 * m1 + m2 - m2 * Math.cos(2 * this.th1 - 2 * this.th2));
        const num1 = -g * (2 * m1 + m2) * Math.sin(this.th1) - m2 * g * Math.sin(this.th1 - 2 * this.th2) - 2 * Math.sin(delta) * m2 * (this.w2 * this.w2 * l + this.w1 * this.w1 * l * Math.cos(delta));
        const alpha1 = num1 / den1;

        const den2 = l * (2 * m1 + m2 - m2 * Math.cos(2 * this.th1 - 2 * this.th2));
        const num2 = 2 * Math.sin(delta) * (this.w1 * this.w1 * l * (m1 + m2) + g * (m1 + m2) * Math.cos(this.th1) + this.w2 * this.w2 * l * m2 * Math.cos(delta));
        const alpha2 = num2 / den2;

        this.w1 += alpha1 * (dt / 4);
        this.w2 += alpha2 * (dt / 4);
        this.th1 += this.w1 * (dt / 4);
        this.th2 += this.w2 * (dt / 4);
      }

      const ox = w * 0.4, oy = h * 0.35;
      const x1 = ox + l * Math.sin(this.th1);
      const y1 = oy + l * Math.cos(this.th1);
      const x2 = x1 + l * Math.sin(this.th2);
      const y2 = y1 + l * Math.cos(this.th2);

      // Record chaotic trail
      this.trail.push({ x: x2, y: y2 });
      if (this.trail.length > 90) this.trail.shift();

      // Draw chaotic path trail
      ctx.strokeStyle = "rgba(236, 72, 153, 0.4)";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      for (let i = 0; i < this.trail.length; i++) {
        if (i === 0) ctx.moveTo(this.trail[i].x, this.trail[i].y);
        else ctx.lineTo(this.trail[i].x, this.trail[i].y);
      }
      ctx.stroke();

      // Draw Rod 1
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(ox, oy);
      ctx.lineTo(x1, y1);
      ctx.stroke();

      // Draw Rod 2
      ctx.strokeStyle = "#a855f7";
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      ctx.stroke();

      // Pivot
      ctx.fillStyle = "#ffffff";
      ctx.beginPath();
      ctx.arc(ox, oy, 5, 0, Math.PI * 2);
      ctx.fill();

      // Bob 1
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath();
      ctx.arc(x1, y1, 10, 0, Math.PI * 2);
      ctx.fill();

      // Bob 2
      ctx.fillStyle = "#ec4899";
      ctx.beginPath();
      ctx.arc(x2, y2, 10, 0, Math.PI * 2);
      ctx.fill();

      // Info
      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px monospace";
      ctx.fillText(`θ1: ${(this.th1 * 180 / Math.PI).toFixed(1)}°, θ2: ${(this.th2 * 180 / Math.PI).toFixed(1)}°`, 20, 30);
      ctx.fillText(`Lyapunov Exponent λ > 0 (Deterministic Chaos)`, 20, 50);
    }
  },

  // 5. Effective Potential & Orbit Turning Points
  "effective-potential-sim": {
    title: "Central Force Effective Potential V_eff(r) & Turning Points",
    desc: "Interactive plot of V_eff(r) = -k/r + l²/(2μ r²). Drag total energy E to observe bound elliptical oscillations between periapsis r_min and apoapsis r_max, or unbound hyperbolic escape.",
    isAnimated: true,
    controls: [
      { id: "energy", label: "Total Energy E (Joules)", min: -8, max: 5, step: 0.2, value: -3.5 },
      { id: "angmom", label: "Angular Momentum l", min: 1, max: 5, step: 0.2, value: 2.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const E = vals.energy || -3.5;
      const l = vals.angmom || 2.5;
      const k = 10.0, mu = 1.0;

      const ox = 60, oy = h * 0.55;
      const scaleX = 45, scaleY = 22;

      // Draw Axes
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(ox, 20); ctx.lineTo(ox, h - 30);
      ctx.moveTo(ox, oy); ctx.lineTo(w - 20, oy);
      ctx.stroke();

      // Draw V_eff(r) curve
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let px = ox + 5; px < w - 20; px++) {
        const r = (px - ox) / scaleX;
        if (r < 0.2) continue;
        const V_eff = -k / r + (l * l) / (2 * mu * r * r);
        const py = oy - V_eff * scaleY;
        if (py < 20 || py > h - 30) continue;
        if (px === ox + 5) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Energy Line E
      const energyY = oy - E * scaleY;
      ctx.strokeStyle = "#f59e0b";
      ctx.lineWidth = 2;
      ctx.setLineDash([6, 4]);
      ctx.beginPath();
      ctx.moveTo(ox, energyY);
      ctx.lineTo(w - 20, energyY);
      ctx.stroke();
      ctx.setLineDash([]);

      // Potential Minimum
      const r0 = (l * l) / (mu * k);
      const V_min = -(mu * k * k) / (2 * l * l);
      const px0 = ox + r0 * scaleX;
      const py0 = oy - V_min * scaleY;
      ctx.fillStyle = "#10b981";
      ctx.beginPath();
      ctx.arc(px0, py0, 5, 0, Math.PI * 2);
      ctx.fill();

      // State text
      let state = "Elliptical Bound Orbit (r_min < r < r_max)";
      if (E < V_min) state = "Forbidden (E < V_min)";
      else if (Math.abs(E - V_min) < 0.2) state = "Circular Stable Orbit (E = V_min, e = 0)";
      else if (E >= 0) state = "Hyperbolic Unbound Orbit (E ≥ 0, Escape)";

      ctx.fillStyle = "#e2e8f0";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Orbit Regime: ${state}`, ox + 20, 35);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px monospace";
      ctx.fillText(`Total Energy E = ${E.toFixed(1)} J`, ox + 20, 55);
      ctx.fillText(`V_min = ${V_min.toFixed(2)} J at r0 = ${r0.toFixed(2)}`, ox + 20, 75);
      ctx.fillText(`Centrifugal Barrier ~ +l²/(2μ r²) dominates as r → 0`, ox + 20, 95);
    }
  },

  // 6. Keplerian Orbit Simulator (Conic Sections)
  "kepler-orbit-sim": {
    title: "Keplerian Planetary Orbits & Sector Sweeping (2nd Law)",
    desc: "Real-time orbital dynamics demonstrating Kepler's laws. Adjust orbital eccentricity e to shift seamlessly between Circular (e=0), Elliptical (0<e<1), Parabolic (e=1), and Hyperbolic (e>1) trajectories.",
    isAnimated: true,
    controls: [
      { id: "ecc", label: "Orbital Eccentricity e", min: 0.0, max: 1.4, step: 0.05, value: 0.55 },
      { id: "speed", label: "Orbit Speed Factor", min: 0.5, max: 3.0, step: 0.2, value: 1.0 }
    ],
    nu: 0,
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const e = vals.ecc !== undefined ? vals.ecc : 0.55;
      const speed = vals.speed || 1.0;
      const p = 80; // semi-latus rectum in pixels
      const fx = w * 0.45, fy = h * 0.5;

      // Draw Orbit Trajectory
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
      ctx.lineWidth = 2;
      ctx.beginPath();
      const maxAngle = e >= 1.0 ? Math.acos(-1 / e) - 0.15 : Math.PI;
      for (let a = -maxAngle; a <= maxAngle; a += 0.05) {
        const r = p / (1 + e * Math.cos(a));
        const px = fx + r * Math.cos(a);
        const py = fy - r * Math.sin(a);
        if (a === -maxAngle) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Keplerian motion update (areal velocity r² dν/dt = const)
      const r_now = p / (1 + e * Math.cos(this.nu));
      const dnu = (speed * 0.8) / (r_now * r_now / 400);
      this.nu += dnu;
      if (e < 1.0) {
        if (this.nu > Math.PI * 2) this.nu -= Math.PI * 2;
      } else {
        if (this.nu > maxAngle) this.nu = -maxAngle;
      }

      // Planet Position
      const plX = fx + r_now * Math.cos(this.nu);
      const plY = fy - r_now * Math.sin(this.nu);

      // Swept sector (Kepler's 2nd Law illustration)
      ctx.fillStyle = "rgba(56, 189, 248, 0.15)";
      ctx.beginPath();
      ctx.moveTo(fx, fy);
      const secStart = this.nu - 0.25;
      for (let a = secStart; a <= this.nu; a += 0.02) {
        const r_s = p / (1 + e * Math.cos(a));
        ctx.lineTo(fx + r_s * Math.cos(a), fy - r_s * Math.sin(a));
      }
      ctx.closePath();
      ctx.fill();

      // Central Sun (Focus)
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath();
      ctx.arc(fx, fy, 12, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#fde68a";
      ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Sun (Focus)", fx - 25, fy - 18);

      // Planet
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath();
      ctx.arc(plX, plY, 7, 0, Math.PI * 2);
      ctx.fill();

      // Readouts
      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px monospace";
      let type = "Circle (e=0)";
      if (e > 0 && e < 1) type = "Ellipse (0 < e < 1)";
      else if (e === 1) type = "Parabola (e=1, Escape)";
      else if (e > 1) type = "Hyperbola (e>1, Unbound)";

      ctx.fillText(`Conic Section: ${type}`, 20, 30);
      ctx.fillText(`Eccentricity e = ${e.toFixed(2)}`, 20, 50);
      ctx.fillText(`Kepler 2nd Law: Areal velocity dA/dt = l/(2μ) = const`, 20, 70);
    }
  },

  // 7. Rutherford Alpha Particle Scattering Sandbox
  "rutherford-scattering-sim": {
    title: "Rutherford Alpha Particle Scattering & Impact Parameter",
    desc: "Simulate Coulomb repulsion between an alpha particle (q=2e) and a heavy gold nucleus (q=79e). Adjust the impact parameter b to observe wide-angle backscattering predicted by the Rutherford formula.",
    isAnimated: true,
    controls: [
      { id: "impact", label: "Impact Parameter b (fm)", min: -40, max: 40, step: 2, value: 12 },
      { id: "energy", label: "Alpha Energy E (MeV)", min: 3, max: 12, step: 0.5, value: 6 }
    ],
    particles: [],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const b_val = vals.impact !== undefined ? vals.impact : 12;
      const E = vals.energy || 6;
      const nucX = w * 0.5, nucY = h * 0.5;

      // Draw Gold Nucleus
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath();
      ctx.arc(nucX, nucY, 14, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Au (Z = 79)", nucX - 22, nucY - 20);

      // Trajectory of beam
      ctx.strokeStyle = "rgba(56, 189, 248, 0.6)";
      ctx.lineWidth = 2;
      ctx.beginPath();
      let px = 40, py = nucY + b_val * 2.5;
      let vx = 5.0, vy = 0.0;
      const k = 1800 / E;

      ctx.moveTo(px, py);
      for (let s = 0; s < 250; s++) {
        const dx = px - nucX, dy = py - nucY;
        const dist = Math.hypot(dx, dy);
        if (dist > 5) {
          const F = k / (dist * dist);
          vx += F * (dx / dist);
          vy += F * (dy / dist);
        }
        px += vx; py += vy;
        ctx.lineTo(px, py);
        if (px > w || px < 0 || py > h || py < 0) break;
      }
      ctx.stroke();

      // Theoretical Rutherford scattering angle: cot(θ/2) = 2 E b / k
      const theta_rad = 2 * Math.atan2(Math.abs(k / 50), Math.abs(b_val));
      const theta_deg = theta_rad * 180 / Math.PI;

      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px monospace";
      ctx.fillText(`Impact Parameter: b = ${b_val} fm`, 20, 30);
      ctx.fillText(`Deflection Angle: θ ≈ ${theta_deg.toFixed(1)}°`, 20, 50);
      ctx.fillText(`dσ/dΩ = (q1 q2 / 16πε0 E)² 1/sin⁴(θ/2)`, 20, 70);
    }
  },

  // 8. Euler Symmetrical Top (Precession & Nutation)
  "euler-top-sim": {
    title: "Heavy Symmetrical Top: Precession, Nutation & Sleeping Top",
    desc: "Observe the gyroscopic motion of a heavy symmetrical top spinning on a fixed pivot. Adjust spin rate ω3 to verify the sleeping top stability condition ω3² ≥ 4 Mgl I1 / I3².",
    isAnimated: true,
    controls: [
      { id: "spin", label: "Spin Rate ω3 (rad/s)", min: 10, max: 120, step: 5, value: 60 },
      { id: "nutation", label: "Nutation Amplitude", min: 0.0, max: 0.6, step: 0.05, value: 0.25 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const w3 = vals.spin || 60;
      const nut_amp = vals.nutation || 0.25;

      const I1 = 2.0, I3 = 1.0, Mgl = 50.0;
      const w3_crit = Math.sqrt(4 * Mgl * I1 / (I3 * I3)); // 20 rad/s

      // Precession and nutation rates
      const w_prec = Mgl / (I3 * w3);
      const w_nut = (I3 * w3) / I1;

      const t = time * 0.001;
      const phi = t * w_prec * 8;
      const theta = 0.5 + nut_amp * Math.sin(t * w_nut * 2);

      const ox = w * 0.5, oy = h * 0.7;
      const topLen = 140;

      // Calculate 3D top orientation
      const topX = ox + topLen * Math.sin(theta) * Math.sin(phi);
      const topY = oy - topLen * Math.cos(theta);

      // Draw Top Axis
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(ox, oy);
      ctx.lineTo(topX, topY);
      ctx.stroke();

      // Draw Spinning Disc (Perpendicular Ellipse)
      ctx.save();
      ctx.translate(topX * 0.7 + ox * 0.3, topY * 0.7 + oy * 0.3);
      ctx.rotate(phi);
      ctx.fillStyle = "#ec4899";
      ctx.beginPath();
      ctx.ellipse(0, 0, 45, 12, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();

      // Fixed Pivot
      ctx.fillStyle = "#ffffff";
      ctx.beginPath();
      ctx.arc(ox, oy, 7, 0, Math.PI * 2);
      ctx.fill();

      // Status
      const isStable = w3 >= w3_crit;
      ctx.fillStyle = isStable ? "#10b981" : "#ef4444";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(isStable ? "✓ Stable Spinning Regime (Fast Gyroscope)" : "⚠ Sleeping Top Unstable (Wobbling & Tumbling)", 20, 30);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px monospace";
      ctx.fillText(`Spin Rate: ω3 = ${w3} rad/s (Critical: ${w3_crit.toFixed(1)} rad/s)`, 20, 50);
      ctx.fillText(`Precession Rate: φ̇ = Mgl / (I3 ω3) = ${w_prec.toFixed(3)} rad/s`, 20, 70);
    }
  },

  // 9. Intermediate Axis Instability (Tennis Racket / Dzhanibekov Effect)
  "tennis-racket-sim": {
    title: "Rigid Body Dynamics: Intermediate Axis Instability (Tennis Racket Theorem)",
    desc: "Euler's equations prove that rotation about principal axes I1 and I3 is dynamically stable, while rotation about the intermediate axis I2 (I1 < I2 < I3) is violently unstable, causing periodic 180° flips.",
    isAnimated: true,
    controls: [
      { id: "axis", label: "Rotation Axis (1:I1, 2:I2, 3:I3)", min: 1, max: 3, step: 1, value: 2 },
      { id: "speed", label: "Rotation Speed", min: 1, max: 5, step: 0.5, value: 2.5 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const axis = Math.round(vals.axis || 2);
      const spd = vals.speed || 2.5;
      const cx = w * 0.5, cy = h * 0.5;

      const t = time * 0.002 * spd;
      let rotX = 0, rotY = 0, rotZ = 0;

      if (axis === 1) { // Stable minor axis
        rotZ = t;
        rotX = 0.1 * Math.sin(t * 0.5);
      } else if (axis === 3) { // Stable major axis
        rotY = t;
        rotX = 0.1 * Math.cos(t * 0.5);
      } else { // Unstable intermediate axis (Dzhanibekov periodic flip)
        rotX = t;
        rotY = Math.PI * (Math.floor(t / Math.PI) + 0.5 * (1 - Math.cos((t % Math.PI))));
      }

      // Draw 3D Box / T-handle representation
      ctx.save();
      ctx.translate(cx, cy);
      ctx.rotate(rotZ);

      ctx.fillStyle = axis === 2 ? "#ef4444" : "#10b981";
      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 2;

      const boxW = 120 * Math.cos(rotY), boxH = 50 * Math.cos(rotX);
      ctx.fillRect(-boxW / 2, -boxH / 2, boxW, boxH);
      ctx.strokeRect(-boxW / 2, -boxH / 2, boxW, boxH);
      ctx.restore();

      ctx.fillStyle = "#e2e8f0";
      ctx.font = "bold 13px Inter, sans-serif";
      let desc = "Axis 2 (Intermediate I2): UNSTABLE (180° Inversion Flips)";
      if (axis === 1) desc = "Axis 1 (Smallest I1): STABLE Pure Rotation";
      if (axis === 3) desc = "Axis 3 (Largest I3): STABLE Pure Rotation";
      ctx.fillText(desc, 20, 30);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px monospace";
      ctx.fillText(`Euler's Equations: I1 I3 η̈1 = (I2 - I3)(I1 - I2) ω0² η1`, 20, 50);
      ctx.fillText(`Product (I2-I3)(I1-I2) > 0 creates exponential runaway!`, 20, 70);
    }
  },

  // 10. Phase Space Oscillator Portraits (q, p)
  "phase-space-oscillator-sim": {
    title: "Harmonic & Relativistic Oscillator Phase Space (q, p)",
    desc: "Map Hamiltonian trajectories in 2D phase space. Observe elliptical closed contours for harmonic oscillators and relativistic flattening into rounded diamond shapes as kinetic energy approaches mc².",
    isAnimated: true,
    controls: [
      { id: "relativistic", label: "Relativistic Mode (0:Off, 1:On)", min: 0, max: 1, step: 1, value: 0 },
      { id: "energy", label: "Energy Level E", min: 1, max: 6, step: 1, value: 3 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const isRel = Math.round(vals.relativistic || 0) === 1;
      const cx = w * 0.5, cy = h * 0.5;

      // Draw Phase Axes
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(30, cy); ctx.lineTo(w - 30, cy);
      ctx.moveTo(cx, 30); ctx.lineTo(cx, h - 30);
      ctx.stroke();

      ctx.fillStyle = "#64748b";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Coordinate q →", w - 100, cy - 8);
      ctx.fillText("Momentum p ↑", cx + 10, 45);

      // Draw Multiple Energy Shells
      const maxLevels = 6;
      for (let E = 1; E <= maxLevels; E++) {
        ctx.strokeStyle = E === vals.energy ? "#f59e0b" : "rgba(56, 189, 248, 0.4)";
        ctx.lineWidth = E === vals.energy ? 3 : 1.5;
        ctx.beginPath();

        const numPts = 100;
        for (let i = 0; i <= numPts; i++) {
          const phi = (i / numPts) * Math.PI * 2;
          let q = E * 22 * Math.cos(phi);
          let p = E * 22 * Math.sin(phi);

          if (isRel) {
            // Relativistic saturation: p saturates at high energy
            p = Math.tanh(p / 60) * 80;
          }

          const px = cx + q;
          const py = cy - p;
          if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
        }
        ctx.stroke();
      }

      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px monospace";
      ctx.fillText(isRel ? "Relativistic Phase Space: H = √(p²c² + m²c⁴) - mc² + ½kq²" : "Harmonic Phase Space: H = p²/(2m) + ½kq² = E (Concentric Ellipses)", 20, 30);
      ctx.fillText(`Liouville Invariant Area: ∮ p dq = 2π E / ω`, 20, 50);
    }
  },

  // 11. Poincaré Section & Liouville Phase Volume
  "poincare-section-sim": {
    title: "Liouville's Theorem: Incompressible Phase Space Flow",
    desc: "Observe an ensemble of initial phase space states (an initially circular droplet). As the Hamiltonian flow evolves, the droplet deforms into complex filaments but its total phase area ∬ dq dp remains strictly invariant.",
    isAnimated: true,
    controls: [
      { id: "shear", label: "Nonlinear Shear Parameter", min: 0.1, max: 2.0, step: 0.1, value: 0.8 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const shear = vals.shear || 0.8;
      const t = (time * 0.001) % 10;
      const cx = w * 0.5, cy = h * 0.5;

      // Draw Grid
      ctx.strokeStyle = "#1e293b";
      ctx.lineWidth = 1;
      for (let x = 50; x < w; x += 50) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke(); }
      for (let y = 50; y < h; y += 50) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke(); }

      // Draw Incompressible Droplet deformation
      ctx.fillStyle = "rgba(168, 85, 247, 0.4)";
      ctx.strokeStyle = "#c084fc";
      ctx.lineWidth = 2;
      ctx.beginPath();

      const numPts = 120;
      const r0 = 55;
      for (let i = 0; i <= numPts; i++) {
        const phi = (i / numPts) * Math.PI * 2;
        const q0 = r0 * Math.cos(phi);
        const p0 = r0 * Math.sin(phi);

        // Hamiltonian area-preserving nonlinear shear flow
        const q = q0 + shear * p0 * Math.sin(t * 0.8);
        const p = p0 - shear * q0 * 0.3 * Math.cos(t * 0.8);

        const px = cx + q;
        const py = cy - p;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = "#e2e8f0";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Liouville's Invariance: dρ/dt = 0 (Incompressible Phase Fluid)", 20, 30);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px monospace";
      ctx.fillText(`Area ∬ dq dp = π r₀² = Constant for all time t`, 20, 50);
      ctx.fillText(`Symplectic Jacobian Det(M) = 1`, 20, 70);
    }
  },

  // 12. Michelson-Morley Interferometer (Null Result)
  "michelson-morley-sim": {
    title: "The Michelson-Morley Interferometer: Zero Ether Drift",
    desc: "Simulate the classic 1887 optical interferometer. Rotate the apparatus by 90° through the putative ether wind. Observe how Special Relativity predicts zero fringe shift (ΔN = 0) confirming the constancy of c.",
    isAnimated: true,
    controls: [
      { id: "rotation", label: "Table Rotation (Degrees)", min: 0, max: 90, step: 5, value: 0 },
      { id: "ether_v", label: "Hypothetical Ether Wind v/c", min: 0.0, max: 0.2, step: 0.02, value: 0.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const rotDeg = vals.rotation || 0;
      const rot = rotDeg * Math.PI / 180;
      const cx = w * 0.4, cy = h * 0.5;

      ctx.save();
      ctx.translate(cx, cy);
      ctx.rotate(rot);

      const arm = 90;
      // Laser Beam Splitter & Arms
      ctx.strokeStyle = "#ef4444";
      ctx.lineWidth = 3;
      // Longitudinal Arm
      ctx.beginPath(); ctx.moveTo(-arm, 0); ctx.lineTo(arm, 0); ctx.stroke();
      // Transverse Arm
      ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(0, -arm); ctx.stroke();

      // Half-silvered mirror
      ctx.fillStyle = "rgba(148, 163, 184, 0.8)";
      ctx.fillRect(-8, -8, 16, 16);

      // Mirrors
      ctx.fillStyle = "#38bdf8";
      ctx.fillRect(arm, -15, 6, 30);
      ctx.fillRect(-15, -arm - 6, 30, 6);
      ctx.restore();

      // Interference Fringe Pattern Display Box
      const bx = w * 0.72, by = 40, bw = 140, bh = 220;
      ctx.fillStyle = "#020617";
      ctx.fillRect(bx, by, bw, bh);
      ctx.strokeStyle = "#475569";
      ctx.strokeRect(bx, by, bw, bh);

      // Draw Fringes (constant since fringe shift is null in relativity)
      for (let y = by + 5; y < by + bh - 5; y += 3) {
        const intensity = 0.5 + 0.5 * Math.cos((y - by) * 0.3);
        ctx.fillStyle = `rgba(239, 68, 68, ${intensity})`;
        ctx.fillRect(bx + 5, y, bw - 10, 2);
      }

      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Interference Detector", bx, by - 10);

      ctx.fillStyle = "#10b981";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("✓ Null Result: Fringe Shift ΔN = 0.00", 20, 30);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px monospace";
      ctx.fillText(`Apparatus Angle: ${rotDeg}°`, 20, 50);
      ctx.fillText(`Speed of Light c is absolute in all directions`, 20, 70);
    }
  },

  // 13. Lorentz Contraction & Time Dilation
  "lorentz-contraction-sim": {
    title: "Relativistic Kinematics: Time Dilation & Length Contraction",
    desc: "Visualize a high-speed relativistic train moving at speed v. As v approaches c, observe Lorentz contraction L = L0/γ and moving light clocks running slow by factor γ.",
    isAnimated: true,
    controls: [
      { id: "beta", label: "Velocity v/c (β)", min: 0.0, max: 0.98, step: 0.02, value: 0.75 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const beta = vals.beta !== undefined ? vals.beta : 0.75;
      const gamma = 1.0 / Math.sqrt(1 - beta * beta);

      const restLen = 220;
      const contractedLen = restLen / gamma;

      const trainX = ((time * 0.1 * beta) % (w + restLen)) - restLen;
      const trainY = h * 0.5;

      // Draw Rest Frame Reference Track
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(0, trainY + 45); ctx.lineTo(w, trainY + 45);
      ctx.stroke();

      // Draw Contracted Train
      ctx.fillStyle = "rgba(56, 189, 248, 0.3)";
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.fillRect(trainX, trainY - 30, contractedLen, 60);
      ctx.strokeRect(trainX, trainY - 30, contractedLen, 60);

      // Light Clock Inside Train
      const clockH = 40;
      const lightFrac = (time * 0.005 / gamma) % 1;
      const lightY = trainY - 20 + Math.abs(lightFrac - 0.5) * 2 * clockH;
      ctx.fillStyle = "#f59e0b";
      ctx.beginPath();
      ctx.arc(trainX + contractedLen / 2, lightY, 5, 0, Math.PI * 2);
      ctx.fill();

      // Metrics
      ctx.fillStyle = "#e2e8f0";
      ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText(`Relativistic Lorentz Factor: γ = ${gamma.toFixed(3)}`, 20, 35);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px monospace";
      ctx.fillText(`Speed: v = ${(beta * 100).toFixed(0)}% c (β = ${beta.toFixed(2)})`, 20, 60);
      ctx.fillText(`Proper Length: L0 = ${restLen} m`, 20, 80);
      ctx.fillText(`Observed Contracted Length: L = L0/γ = ${contractedLen.toFixed(1)} m`, 20, 100);
      ctx.fillText(`Time Dilation: Δt = γ Δt0 (Clocks tick ${gamma.toFixed(2)}x slower)`, 20, 120);
    }
  },

  // 14. Minkowski Spacetime Light Cone Diagram
  "minkowski-spacetime-sim": {
    title: "Minkowski Spacetime: Invariant Intervals & Light Cone Geometry",
    desc: "Interactive spacetime diagram showing the light cone (c² dt² - dx² = 0). Click or drag to test whether spacetime events are Timelike (causally connectable), Spacelike (acausal), or Null.",
    isAnimated: true,
    controls: [
      { id: "eventX", label: "Event Coordinate x", min: -120, max: 120, step: 5, value: 50 },
      { id: "eventT", label: "Event Time ct", min: -120, max: 120, step: 5, value: 70 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const evX = vals.eventX !== undefined ? vals.eventX : 50;
      const evT = vals.eventT !== undefined ? vals.eventT : 70;
      const cx = w * 0.5, cy = h * 0.5;

      // Draw Light Cones (45° Lines ct = ±x)
      ctx.fillStyle = "rgba(56, 189, 248, 0.08)";
      // Future Light Cone
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(cx - 160, cy - 160);
      ctx.lineTo(cx + 160, cy - 160);
      ctx.closePath();
      ctx.fill();

      // Past Light Cone
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(cx - 160, cy + 160);
      ctx.lineTo(cx + 160, cy + 160);
      ctx.closePath();
      ctx.fill();

      // Light cone boundary lines
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(cx - 160, cy + 160); ctx.lineTo(cx + 160, cy - 160);
      ctx.moveTo(cx - 160, cy - 160); ctx.lineTo(cx + 160, cy + 160);
      ctx.stroke();

      // Axes
      ctx.strokeStyle = "#475569";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(cx, 20); ctx.lineTo(cx, h - 20); // ct axis
      ctx.moveTo(20, cy); ctx.lineTo(w - 20, cy); // x axis
      ctx.stroke();

      ctx.fillStyle = "#94a3b8";
      ctx.font = "11px Inter, sans-serif";
      ctx.fillText("ct (Time) ↑", cx + 8, 30);
      ctx.fillText("x (Space) →", w - 80, cy - 8);

      // Event Point
      const px = cx + evX;
      const py = cy - evT;
      const ds2 = evT * evT - evX * evX;

      let intervalType = "TIMELIKE (ds² > 0, Causally Connectable)";
      let dotColor = "#10b981";
      if (ds2 < 0) {
        intervalType = "SPACELIKE (ds² < 0, Acausal / Simultaneous Frame Exists)";
        dotColor = "#ef4444";
      } else if (ds2 === 0) {
        intervalType = "LIGHTLIKE / NULL (ds² = 0, Photons Only)";
        dotColor = "#f59e0b";
      }

      ctx.fillStyle = dotColor;
      ctx.beginPath();
      ctx.arc(px, py, 8, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#ffffff";
      ctx.stroke();

      // Readout
      ctx.fillStyle = dotColor;
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText(`Event Interval: ${intervalType}`, 20, 35);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px monospace";
      ctx.fillText(`Spacetime Interval: ds² = c²dt² - dx² = ${ds2.toFixed(0)}`, 20, 55);
      ctx.fillText(`Coordinates: (ct = ${evT}, x = ${evX})`, 20, 75);
    }
  },

  // 15. Relativistic Particle Collision & Threshold Energy
  "relativistic-collision-sim": {
    title: "Relativistic Collisions & Invariant Mass Center-of-Momentum",
    desc: "Calculate relativistic four-momentum conservation in particle accelerator collisions. Observe threshold kinetic energy for antiproton pair production p + p → 3p + p̄.",
    isAnimated: true,
    controls: [
      { id: "kin_energy", label: "Proton Kinetic Energy K (GeV)", min: 1, max: 10, step: 0.5, value: 6.0 }
    ],
    render(canvas, vals, time) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#070b14";
      ctx.fillRect(0, 0, w, h);

      const K = vals.kin_energy || 6.0;
      const mp = 0.938; // GeV
      const E_tot = K + mp;
      const s = 2 * mp * mp + 2 * mp * E_tot;
      const sqrt_s = Math.sqrt(s); // Center of mass energy

      const E_threshold = 6 * mp; // 5.63 GeV
      const canProduce = K >= E_threshold;

      const cx = w * 0.5, cy = h * 0.5;

      // Accelerator beam representation
      ctx.fillStyle = "#38bdf8";
      ctx.beginPath();
      ctx.arc(cx - 100, cy, 14, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`p (Beam: ${K.toFixed(1)} GeV)`, cx - 160, cy - 20);

      // Target proton at rest
      ctx.fillStyle = "#94a3b8";
      ctx.beginPath();
      ctx.arc(cx, cy, 14, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.fillText("p (Target at Rest)", cx - 45, cy - 20);

      // Collision outcome
      ctx.fillStyle = canProduce ? "#10b981" : "#ef4444";
      ctx.font = "bold 14px Inter, sans-serif";
      ctx.fillText(canProduce ? "✓ Threshold Exceeded! p + p → 3p + p̄ Reaction ALLOWED" : "✗ Energy Below Threshold (Requires K ≥ 5.63 GeV = 6 mp c²)", 20, 35);

      ctx.fillStyle = "#94a3b8";
      ctx.font = "12px monospace";
      ctx.fillText(`Lab Beam Energy: E1 = ${E_tot.toFixed(2)} GeV`, 20, 65);
      ctx.fillText(`Mandelstam s = 2 mp² c⁴ + 2 mp E1 = ${s.toFixed(2)} GeV²`, 20, 85);
      ctx.fillText(`Center of Mass Available Energy √s = ${sqrt_s.toFixed(2)} GeV (Need 4 mp = 3.75 GeV)`, 20, 105);
      ctx.fillText(`Four-Momentum Invariant: P_tot^μ P_tot,μ = s`, 20, 125);
    }
  }

};

// Universal Engine Integration Adapter for Classical Mechanics
window.SimulationEngine = window.SimulationEngine || {};
window.SimulationEngine.activeAnimations = window.SimulationEngine.activeAnimations || {};

window.SimulationEngine.initSimulation = function(containerId, simType) {
  const container = document.getElementById(containerId);
  if (!container) return;

  if (window.SimulationEngine.activeAnimations[containerId]) {
    cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
    delete window.SimulationEngine.activeAnimations[containerId];
  }

  const simConfig = (window.CM_SIMS && window.CM_SIMS[simType]) ||
                    (window.TP_SIMS && window.TP_SIMS[simType]) ||
                    (window.EM_SIMS && window.EM_SIMS[simType]) ||
                    (window.MATTER_SIMS && window.MATTER_SIMS[simType]) ||
                    (window.STATMECH_SIMS && window.STATMECH_SIMS[simType]);
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
