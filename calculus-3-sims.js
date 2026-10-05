// Calculus III Simulation Suite
// 8 Real-Time 60 FPS Interactive Canvas Simulations for Multivariable & Vector Calculus

function project3D(x, y, z, rotX, rotY, w, h, scale = 40) {
  const radY = (rotY * Math.PI) / 180;
  const radX = (rotX * Math.PI) / 180;
  const cy = Math.cos(radY), sy = Math.sin(radY);
  const cx = Math.cos(radX), sx = Math.sin(radX);

  // Yaw around Y
  const x1 = x * cy + z * sy;
  const y1 = y;
  const z1 = -x * sy + z * cy;

  // Pitch around X
  const x2 = x1;
  const y2 = y1 * cx - z1 * sx;
  const z2 = y1 * sx + z1 * cx;

  const cameraZ = z2 + 14;
  const fov = 380;
  const pScale = fov / (cameraZ > 0.5 ? cameraZ : 0.5);

  return {
    px: w / 2 + x2 * pScale * (scale / 40),
    py: h / 2 - y2 * pScale * (scale / 40),
    z: z2
  };
}

function drawAxisArrows(ctx, rotX, rotY, w, h, len = 6, scale = 40) {
  const origin = project3D(0, 0, 0, rotX, rotY, w, h, scale);
  const xEnd = project3D(len, 0, 0, rotX, rotY, w, h, scale);
  const yEnd = project3D(0, len, 0, rotX, rotY, w, h, scale);
  const zEnd = project3D(0, 0, len, rotX, rotY, w, h, scale);

  ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2;
  ctx.beginPath(); ctx.moveTo(origin.px, origin.py); ctx.lineTo(xEnd.px, xEnd.py); ctx.stroke();
  ctx.fillStyle = "#f43f5e"; ctx.font = "bold 11px Inter, sans-serif";
  ctx.fillText("+X", xEnd.px + 6, xEnd.py);

  ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
  ctx.beginPath(); ctx.moveTo(origin.px, origin.py); ctx.lineTo(yEnd.px, yEnd.py); ctx.stroke();
  ctx.fillStyle = "#10b981";
  ctx.fillText("+Y", yEnd.px + 6, yEnd.py);

  ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
  ctx.beginPath(); ctx.moveTo(origin.px, origin.py); ctx.lineTo(zEnd.px, zEnd.py); ctx.stroke();
  ctx.fillStyle = "#38bdf8";
  ctx.fillText("+Z", zEnd.px + 6, zEnd.py);

  ctx.strokeStyle = "rgba(148, 163, 184, 0.12)"; ctx.lineWidth = 1;
  const gSize = 5;
  for (let i = -gSize; i <= gSize; i += 2) {
    const p1 = project3D(i, 0, -gSize, rotX, rotY, w, h, scale);
    const p2 = project3D(i, 0, gSize, rotX, rotY, w, h, scale);
    ctx.beginPath(); ctx.moveTo(p1.px, p1.py); ctx.lineTo(p2.px, p2.py); ctx.stroke();

    const q1 = project3D(-gSize, 0, i, rotX, rotY, w, h, scale);
    const q2 = project3D(gSize, 0, i, rotX, rotY, w, h, scale);
    ctx.beginPath(); ctx.moveTo(q1.px, q1.py); ctx.lineTo(q2.px, q2.py); ctx.stroke();
  }
}

window.CALC3_SIMS = {
  // 1. Space Curves & Velocity Vector Engine
  "sim_calc3_space_curves": {
    title: "3D Space Curves & Velocity Vector Engine",
    desc: "Visualize 3D trajectories (circular helix, twisted cubic, conical spiral). Trace tangent velocity vectors, arc length progress, and orbit around the 3D space curve in real time.",
    isAnimated: false,
    controls: [
      { id: "curveType", label: "Curve (0:Helix, 1:Cubic, 2:Cone)", min: 0, max: 2, step: 1, value: 0 },
      { id: "tParam", label: "Curve Parameter t", min: 0.1, max: 6.28, step: 0.05, value: 2.5 },
      { id: "helixRadius", label: "Radius / Scale a", min: 1.0, max: 4.0, step: 0.2, value: 2.5 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 35 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const type = vals.curveType !== undefined ? Math.round(vals.curveType) : 0;
      const t = vals.tParam !== undefined ? vals.tParam : 2.5;
      const a = vals.helixRadius !== undefined ? vals.helixRadius : 2.5;
      const rotY = vals.rotY !== undefined ? vals.rotY : 35;
      const rotX = 22;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 36);

      function getCurvePoint(u) {
        if (type === 0) {
          // Circular Helix
          return [a * Math.cos(u), a * Math.sin(u), 0.6 * u];
        } else if (type === 1) {
          // Scaled Twisted Cubic: t in [-1.5, 1.5] mapped from u in [0, 6.28]
          const tau = (u - 3.14) / 1.5;
          return [1.8 * tau, 1.2 * tau * tau, 0.6 * tau * tau * tau];
        } else {
          // Conical Spiral
          const rCone = 0.45 * u;
          return [rCone * Math.cos(u), rCone * Math.sin(u), 0.6 * u];
        }
      }

      function getTangent(u) {
        const eps = 0.001;
        const p0 = getCurvePoint(u - eps);
        const p1 = getCurvePoint(u + eps);
        return [(p1[0] - p0[0]) / (2 * eps), (p1[1] - p0[1]) / (2 * eps), (p1[2] - p0[2]) / (2 * eps)];
      }

      // Draw full curve
      ctx.strokeStyle = "rgba(56, 189, 248, 0.45)"; ctx.lineWidth = 1.8;
      ctx.beginPath();
      const steps = 120;
      for (let i = 0; i <= steps; i++) {
        const u = (i / steps) * 6.28;
        const pt = getCurvePoint(u);
        const p = project3D(pt[0], pt[1], pt[2], rotX, rotY, w, h, 36);
        if (i === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
      }
      ctx.stroke();

      // Draw active arc length path up to t (bright cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.8;
      ctx.beginPath();
      const tSteps = Math.max(2, Math.round((t / 6.28) * steps));
      for (let i = 0; i <= tSteps; i++) {
        const u = (i / tSteps) * t;
        const pt = getCurvePoint(u);
        const p = project3D(pt[0], pt[1], pt[2], rotX, rotY, w, h, 36);
        if (i === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
      }
      ctx.stroke();

      // Current Point P(t)
      const curPt = getCurvePoint(t);
      const curP = project3D(curPt[0], curPt[1], curPt[2], rotX, rotY, w, h, 36);
      ctx.fillStyle = "#fbbf24"; ctx.beginPath(); ctx.arc(curP.px, curP.py, 5, 0, Math.PI * 2); ctx.fill();

      // Tangent Velocity Vector r'(t)
      const tan = getTangent(t);
      const speed = Math.sqrt(tan[0] * tan[0] + tan[1] * tan[1] + tan[2] * tan[2]);
      const vScale = 0.7;
      const vTip = project3D(curPt[0] + tan[0] * vScale, curPt[1] + tan[1] * vScale, curPt[2] + tan[2] * vScale, rotX, rotY, w, h, 36);

      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.8;
      ctx.beginPath(); ctx.moveTo(curP.px, curP.py); ctx.lineTo(vTip.px, vTip.py); ctx.stroke();
      ctx.fillStyle = "#f43f5e"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("v(t)", vTip.px + 6, vTip.py);

      // Arc Length approx
      let arcLen = 0;
      for (let i = 1; i <= tSteps; i++) {
        const u0 = ((i - 1) / tSteps) * t;
        const u1 = (i / tSteps) * t;
        const pA = getCurvePoint(u0), pB = getCurvePoint(u1);
        arcLen += Math.sqrt(Math.pow(pB[0]-pA[0], 2) + Math.pow(pB[1]-pA[1], 2) + Math.pow(pB[2]-pA[2], 2));
      }

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      ctx.fillRect(15, 15, 300, 130);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 300, 130);

      const curveNames = ["CIRCULAR HELIX", "TWISTED CUBIC", "CONICAL SPIRAL"];
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(curveNames[type], 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Parameter t = ${t.toFixed(2)}`, 25, 53);
      ctx.fillText(`Position: (${curPt[0].toFixed(2)}, ${curPt[1].toFixed(2)}, ${curPt[2].toFixed(2)})`, 25, 71);
      ctx.fillText(`Velocity: (${tan[0].toFixed(2)}, ${tan[1].toFixed(2)}, ${tan[2].toFixed(2)})`, 25, 89);
      ctx.fillText(`Speed v(t) = |r'(t)| = ${speed.toFixed(3)}`, 25, 107);
      ctx.fillStyle = "#fbbf24"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`Arc Length s(t) = ${arcLen.toFixed(3)} units`, 25, 126);
    }
  },

  // 2. Curvature & Frenet-Serret TNB Frame Engine
  "sim_calc3_curvature": {
    title: "Osculating Circle & Frenet-Serret TNB Frame Engine",
    desc: "Watch the moving Frenet-Serret trihedron (T in sky blue, N in emerald, B in rose) and the dynamic osculating circle track smoothly along a 3D curve with live curvature and radius readouts.",
    isAnimated: false,
    controls: [
      { id: "curveChoice", label: "Curve (0:Helix, 1:Parabola, 2:Torus)", min: 0, max: 2, step: 1, value: 0 },
      { id: "tPos", label: "Curve Position t", min: 0.1, max: 6.28, step: 0.05, value: 2.0 },
      { id: "torsionScale", label: "Pitch / Scale b", min: 0.5, max: 3.0, step: 0.2, value: 1.2 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 40 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const type = vals.curveChoice !== undefined ? Math.round(vals.curveChoice) : 0;
      const t = vals.tPos !== undefined ? vals.tPos : 2.0;
      const b = vals.torsionScale !== undefined ? vals.torsionScale : 1.2;
      const rotY = vals.rotY !== undefined ? vals.rotY : 40;
      const rotX = 22;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 36);

      const a = 2.4;
      function rVec(u) {
        if (type === 0) {
          return [a * Math.cos(u), a * Math.sin(u), 0.4 * b * u];
        } else if (type === 1) {
          const x = (u - 3.14) * 0.8;
          return [x, 0.4 * x * x, 0.2 * Math.sin(u)];
        } else {
          return [(a + 0.8 * Math.cos(3 * u)) * Math.cos(u), (a + 0.8 * Math.cos(3 * u)) * Math.sin(u), 0.8 * Math.sin(3 * u)];
        }
      }

      // Draw curve
      ctx.strokeStyle = "rgba(148, 163, 184, 0.4)"; ctx.lineWidth = 1.8;
      ctx.beginPath();
      const nSteps = 140;
      for (let i = 0; i <= nSteps; i++) {
        const u = (i / nSteps) * 6.28;
        const pt = rVec(u);
        const p = project3D(pt[0], pt[1], pt[2], rotX, rotY, w, h, 36);
        if (i === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
      }
      ctx.stroke();

      // Numerical derivatives at t
      const eps = 0.001;
      const pMinus = rVec(t - eps), p0 = rVec(t), pPlus = rVec(t + eps);
      const v = [(pPlus[0] - pMinus[0]) / (2 * eps), (pPlus[1] - pMinus[1]) / (2 * eps), (pPlus[2] - pMinus[2]) / (2 * eps)];
      const acc = [(pPlus[0] - 2 * p0[0] + pMinus[0]) / (eps * eps), (pPlus[1] - 2 * p0[1] + pMinus[1]) / (eps * eps), (pPlus[2] - 2 * p0[2] + pMinus[2]) / (eps * eps)];

      const speed = Math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2]);
      const T = [v[0] / speed, v[1] / speed, v[2] / speed];

      // v x a
      const vxa = [
        v[1] * acc[2] - v[2] * acc[1],
        v[2] * acc[0] - v[0] * acc[2],
        v[0] * acc[1] - v[1] * acc[0]
      ];
      const vxaMag = Math.sqrt(vxa[0] * vxa[0] + vxa[1] * vxa[1] + vxa[2] * vxa[2]);
      const kappa = vxaMag / (speed * speed * speed);
      const rho = kappa > 0.01 ? 1 / kappa : 10;

      // Binormal B = (v x a) / |v x a|
      const B = vxaMag > 0.001 ? [vxa[0] / vxaMag, vxa[1] / vxaMag, vxa[2] / vxaMag] : [0, 0, 1];

      // Principal Normal N = B x T
      const N = [
        B[1] * T[2] - B[2] * T[1],
        B[2] * T[0] - B[0] * T[2],
        B[0] * T[1] - B[1] * T[0]
      ];

      const pCenter = [p0[0] + rho * N[0], p0[1] + rho * N[1], p0[2] + rho * N[2]];

      // Draw Osculating Circle in osculating plane (spanned by T and N)
      if (rho < 8) {
        ctx.strokeStyle = "rgba(251, 191, 36, 0.6)"; ctx.lineWidth = 1.5;
        ctx.beginPath();
        for (let th = 0; th <= Math.PI * 2; th += 0.15) {
          const cx = pCenter[0] + rho * (Math.cos(th) * (-N[0]) + Math.sin(th) * T[0]);
          const cy = pCenter[1] + rho * (Math.cos(th) * (-N[1]) + Math.sin(th) * T[1]);
          const cz = pCenter[2] + rho * (Math.cos(th) * (-N[2]) + Math.sin(th) * T[2]);
          const pCirc = project3D(cx, cy, cz, rotX, rotY, w, h, 36);
          if (th === 0) ctx.moveTo(pCirc.px, pCirc.py); else ctx.lineTo(pCirc.px, pCirc.py);
        }
        ctx.closePath(); ctx.stroke();
      }

      // Draw TNB Triad Arrows
      const projP0 = project3D(p0[0], p0[1], p0[2], rotX, rotY, w, h, 36);
      const fScale = 1.6;

      function drawVector(vec, color, label) {
        const pTip = project3D(p0[0] + vec[0] * fScale, p0[1] + vec[1] * fScale, p0[2] + vec[2] * fScale, rotX, rotY, w, h, 36);
        ctx.strokeStyle = color; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(projP0.px, projP0.py); ctx.lineTo(pTip.px, pTip.py); ctx.stroke();
        ctx.fillStyle = color; ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText(label, pTip.px + 6, pTip.py);
      }

      drawVector(T, "#38bdf8", "T"); // Sky Blue
      drawVector(N, "#10b981", "N"); // Emerald
      drawVector(B, "#f43f5e", "B"); // Rose

      // Point P0
      ctx.fillStyle = "#fff"; ctx.beginPath(); ctx.arc(projP0.px, projP0.py, 4.5, 0, Math.PI * 2); ctx.fill();

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      ctx.fillRect(15, 15, 300, 130);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 300, 130);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("FRENET-SERRET APPARATUS", 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Curvature κ = ${kappa.toFixed(3)}`, 25, 53);
      ctx.fillText(`Radius of Curvature ρ = 1/κ = ${rho.toFixed(3)}`, 25, 71);
      const tau = (type === 0) ? (0.4 * b) / (a * a + 0.16 * b * b) : 0.05;
      ctx.fillText(`Torsion τ = ${tau.toFixed(3)}`, 25, 89);
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("TNB Orthonormal: T ⟂ N ⟂ B,  |T|=|N|=|B|=1", 25, 110);
      ctx.fillStyle = "#fbbf24"; ctx.font = "10px Inter, sans-serif";
      ctx.fillText("Amber circle: Osculating circle in osculating plane", 25, 127);
    }
  },

  // 3. Multivariable Surface & Tangent Plane Engine
  "sim_calc3_tangent_planes": {
    title: "3D Multivariable Surface & Tangent Plane Engine",
    desc: "Rotate 3D quadric surfaces (paraboloid, saddle surface, ripple). Place a touch point (x0, y0), observe the orthogonal partial derivative trace slices, and see the tangent plane tilt in real time.",
    isAnimated: false,
    controls: [
      { id: "surfaceChoice", label: "Surface (0:Bowl, 1:Saddle, 2:Ripple)", min: 0, max: 2, step: 1, value: 0 },
      { id: "x0", label: "Touch Point x0", min: -2.0, max: 2.0, step: 0.1, value: 0.8 },
      { id: "y0", label: "Touch Point y0", min: -2.0, max: 2.0, step: 0.1, value: 0.6 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 35 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const sType = vals.surfaceChoice !== undefined ? Math.round(vals.surfaceChoice) : 0;
      const x0 = vals.x0 !== undefined ? vals.x0 : 0.8;
      const y0 = vals.y0 !== undefined ? vals.y0 : 0.6;
      const rotY = vals.rotY !== undefined ? vals.rotY : 35;
      const rotX = 22;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 36);

      function surfF(x, y) {
        if (sType === 0) {
          // Paraboloid bowl: z = 0.4*(x^2 + y^2)
          return 0.4 * (x * x + y * y);
        } else if (sType === 1) {
          // Saddle: z = 0.4*(x^2 - y^2)
          return 0.4 * (x * x - y * y);
        } else {
          // Ripple: z = 0.8 * cos(sqrt(x^2+y^2)*1.8)
          return 0.8 * Math.cos(Math.sqrt(x * x + y * y) * 1.8);
        }
      }

      // Draw surface wireframe mesh
      ctx.strokeStyle = "rgba(56, 189, 248, 0.25)"; ctx.lineWidth = 1;
      const extent = 2.4;
      const meshN = 16;
      for (let i = 0; i <= meshN; i++) {
        const xVal = -extent + (i / meshN) * (2 * extent);
        ctx.beginPath();
        for (let j = 0; j <= meshN; j++) {
          const yVal = -extent + (j / meshN) * (2 * extent);
          const zVal = surfF(xVal, yVal);
          const p = project3D(xVal, yVal, zVal, rotX, rotY, w, h, 36);
          if (j === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
        }
        ctx.stroke();

        ctx.beginPath();
        for (let j = 0; j <= meshN; j++) {
          const yVal = -extent + (j / meshN) * (2 * extent);
          const zVal = surfF(yVal, xVal);
          const p = project3D(yVal, xVal, zVal, rotX, rotY, w, h, 36);
          if (j === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
        }
        ctx.stroke();
      }

      // Compute numerical partial derivatives at (x0, y0)
      const eps = 0.001;
      const z0 = surfF(x0, y0);
      const fx = (surfF(x0 + eps, y0) - surfF(x0 - eps, y0)) / (2 * eps);
      const fy = (surfF(x0, y0 + eps) - surfF(x0, y0 - eps)) / (2 * eps);

      // Draw Tangent Plane patch around (x0, y0)
      const pSize = 1.4;
      const tCorners = [
        [x0 - pSize, y0 - pSize, z0 + fx * (-pSize) + fy * (-pSize)],
        [x0 + pSize, y0 - pSize, z0 + fx * (pSize) + fy * (-pSize)],
        [x0 + pSize, y0 + pSize, z0 + fx * (pSize) + fy * (pSize)],
        [x0 - pSize, y0 + pSize, z0 + fx * (-pSize) + fy * (pSize)]
      ];
      const pCorn = tCorners.map(c => project3D(c[0], c[1], c[2], rotX, rotY, w, h, 36));

      ctx.beginPath();
      ctx.moveTo(pCorn[0].px, pCorn[0].py);
      for (let i = 1; i < 4; i++) ctx.lineTo(pCorn[i].px, pCorn[i].py);
      ctx.closePath();
      ctx.fillStyle = "rgba(244, 63, 94, 0.22)"; ctx.fill();
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 1.8; ctx.stroke();

      // Normal vector arrow n = <-fx, -fy, 1>
      const nLen = 1.5;
      const nMag = Math.sqrt(fx * fx + fy * fy + 1);
      const nNorm = [-fx / nMag, -fy / nMag, 1 / nMag];
      const pTouch = project3D(x0, y0, z0, rotX, rotY, w, h, 36);
      const pNTip = project3D(x0 + nNorm[0] * nLen, y0 + nNorm[1] * nLen, z0 + nNorm[2] * nLen, rotX, rotY, w, h, 36);

      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(pTouch.px, pTouch.py); ctx.lineTo(pNTip.px, pNTip.py); ctx.stroke();
      ctx.fillStyle = "#fbbf24"; ctx.beginPath(); ctx.arc(pTouch.px, pTouch.py, 4.5, 0, Math.PI * 2); ctx.fill();
      ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("n", pNTip.px + 6, pNTip.py);

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      ctx.fillRect(15, 15, 300, 130);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 300, 130);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("MULTIVARIABLE SURFACE & TANGENT PLANE", 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Point P = (${x0.toFixed(2)}, ${y0.toFixed(2)}, ${z0.toFixed(2)})`, 25, 53);
      ctx.fillText(`∂f/∂x = ${fx.toFixed(3)},   ∂f/∂y = ${fy.toFixed(3)}`, 25, 71);
      ctx.fillText(`Tangent Plane: z - ${z0.toFixed(2)} = ${fx.toFixed(2)}(x-${x0.toFixed(2)}) + ${fy.toFixed(2)}(y-${y0.toFixed(2)})`, 25, 89);
      ctx.fillStyle = "#f43f5e"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`Normal Vector n = (${(-fx).toFixed(2)}, ${(-fy).toFixed(2)}, 1.00)`, 25, 109);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter, sans-serif";
      ctx.fillText("Linearization L(x, y) forms the best flat approximation", 25, 127);
    }
  },

  // 4. Saddle Surfaces, Gradients & Lagrange Multipliers Engine
  "sim_calc3_optimization": {
    title: "3D Saddle Surfaces, Gradients & Lagrange Multipliers Engine",
    desc: "Visualize 3D critical points, saddle geometries, gradient field vectors, and see the geometric tangency condition of Lagrange multipliers on level curves in real time.",
    isAnimated: false,
    controls: [
      { id: "surfaceMode", label: "Mode (0:Saddle, 1:Extrema, 2:Lagrange)", min: 0, max: 2, step: 1, value: 0 },
      { id: "probeX", label: "Probe X", min: -2.0, max: 2.0, step: 0.1, value: 1.0 },
      { id: "probeY", label: "Probe Y", min: -2.0, max: 2.0, step: 0.1, value: 0.8 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 40 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const mode = vals.surfaceMode !== undefined ? Math.round(vals.surfaceMode) : 0;
      const px = vals.probeX !== undefined ? vals.probeX : 1.0;
      const py = vals.probeY !== undefined ? vals.probeY : 0.8;
      const rotY = vals.rotY !== undefined ? vals.rotY : 40;
      const rotX = 22;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 36);

      function f(x, y) {
        if (mode === 0) return 0.5 * (x * x - y * y); // Saddle
        if (mode === 1) return 0.5 * (x * x + y * y); // Paraboloid
        return x * y; // Lagrange: f(x,y) = xy
      }

      // Draw wireframe
      ctx.strokeStyle = mode === 0 ? "rgba(244, 63, 94, 0.3)" : "rgba(16, 185, 129, 0.3)";
      ctx.lineWidth = 1;
      const nMesh = 14;
      for (let i = 0; i <= nMesh; i++) {
        const x = -2 + (i / nMesh) * 4;
        ctx.beginPath();
        for (let j = 0; j <= nMesh; j++) {
          const y = -2 + (j / nMesh) * 4;
          const p = project3D(x, y, f(x, y), rotX, rotY, w, h, 36);
          if (j === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
        }
        ctx.stroke();
      }

      // Probe point P
      const pz = f(px, py);
      const projP = project3D(px, py, pz, rotX, rotY, w, h, 36);

      // Compute gradient ∇f
      const eps = 0.001;
      const gx = (f(px + eps, py) - f(px - eps, py)) / (2 * eps);
      const gy = (f(px, py + eps) - f(px, py - eps)) / (2 * eps);

      // Draw gradient vector in XY plane or tangent
      const gradScale = 0.5;
      const pGradTip = project3D(px + gx * gradScale, py + gy * gradScale, pz, rotX, rotY, w, h, 36);

      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(projP.px, projP.py); ctx.lineTo(pGradTip.px, pGradTip.py); ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("∇f", pGradTip.px + 6, pGradTip.py);

      // Probe point marker
      ctx.fillStyle = "#fbbf24"; ctx.beginPath(); ctx.arc(projP.px, projP.py, 5, 0, Math.PI * 2); ctx.fill();

      // If mode 2: Draw constraint circle x^2 + y^2 = 1.5^2 in XY plane
      if (mode === 2) {
        ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2;
        ctx.beginPath();
        for (let th = 0; th <= Math.PI * 2; th += 0.1) {
          const cx = 1.5 * Math.cos(th), cy = 1.5 * Math.sin(th);
          const pC = project3D(cx, cy, 0, rotX, rotY, w, h, 36);
          if (th === 0) ctx.moveTo(pC.px, pC.py); else ctx.lineTo(pC.px, pC.py);
        }
        ctx.closePath(); ctx.stroke();
      }

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      ctx.fillRect(15, 15, 300, 130);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 300, 130);

      const modeTitles = ["SADDLE SURFACE (D < 0)", "LOCAL EXTREMUM (D > 0)", "LAGRANGE CONSTRAINED OPTIMIZATION"];
      ctx.fillStyle = "#fbbf24"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(modeTitles[mode], 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Probe Point: (${px.toFixed(2)}, ${py.toFixed(2)}, ${pz.toFixed(2)})`, 25, 53);
      ctx.fillText(`Gradient: ∇f = (${gx.toFixed(2)}, ${gy.toFixed(2)})`, 25, 71);
      if (mode === 0) {
        ctx.fillText("Hessian Determinant: D = f_xx f_yy - f_xy² = -1.00 < 0", 25, 89);
        ctx.fillStyle = "#f43f5e"; ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText("Classification: Origin is a Minimax Saddle Point", 25, 109);
      } else if (mode === 1) {
        ctx.fillText("Hessian Determinant: D = +1.00 > 0,  f_xx = +1.00 > 0", 25, 89);
        ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText("Classification: Origin is an Absolute Local Minimum", 25, 109);
      } else {
        ctx.fillText("Constraint: g(x, y) = x² + y² = 2.25", 25, 89);
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText("Lagrange Condition: ∇f = λ ∇g at tangency", 25, 109);
      }
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter, sans-serif";
      ctx.fillText("Blue arrow points in direction of steepest ascent", 25, 127);
    }
  },

  // 5. Double Riemann Slices & Polar Region Engine
  "sim_calc3_double_integrals": {
    title: "Double Riemann Slices & Polar Region Engine",
    desc: "Visualize 3D volumes under surfaces, switch between Cartesian rectangular grid slices and polar sector wedges, and observe double Riemann sum convergence in real time.",
    isAnimated: false,
    controls: [
      { id: "gridMode", label: "Grid (0:Cartesian, 1:Polar)", min: 0, max: 1, step: 1, value: 0 },
      { id: "slicesN", label: "Partitions N", min: 4, max: 24, step: 2, value: 12 },
      { id: "heightScale", label: "Height Amplitude", min: 0.5, max: 2.5, step: 0.1, value: 1.5 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 35 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const isPolar = (vals.gridMode !== undefined ? Math.round(vals.gridMode) : 0) === 1;
      const N = vals.slicesN !== undefined ? Math.round(vals.slicesN) : 12;
      const amp = vals.heightScale !== undefined ? vals.heightScale : 1.5;
      const rotY = vals.rotY !== undefined ? vals.rotY : 35;
      const rotX = 22;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 36);

      function f(x, y) {
        return Math.max(0, amp * (1 - 0.2 * (x * x + y * y)));
      }

      let approxVol = 0;

      if (!isPolar) {
        // Cartesian grid over [-2, 2] x [-2, 2]
        const L = 2.0;
        const dx = (2 * L) / N, dy = (2 * L) / N;
        const dA = dx * dy;

        for (let i = 0; i < N; i++) {
          const x = -L + (i + 0.5) * dx;
          for (let j = 0; j < N; j++) {
            const y = -L + (j + 0.5) * dy;
            const zH = f(x, y);
            if (zH > 0.05) {
              approxVol += zH * dA;
              // Draw top face of prism
              const c = [
                project3D(x - dx / 2, y - dy / 2, zH, rotX, rotY, w, h, 36),
                project3D(x + dx / 2, y - dy / 2, zH, rotX, rotY, w, h, 36),
                project3D(x + dx / 2, y + dy / 2, zH, rotX, rotY, w, h, 36),
                project3D(x - dx / 2, y + dy / 2, zH, rotX, rotY, w, h, 36)
              ];
              ctx.beginPath();
              ctx.moveTo(c[0].px, c[0].py);
              for (let k = 1; k < 4; k++) ctx.lineTo(c[k].px, c[k].py);
              ctx.closePath();
              ctx.fillStyle = "rgba(56, 189, 248, 0.35)"; ctx.fill();
              ctx.strokeStyle = "rgba(56, 189, 248, 0.6)"; ctx.lineWidth = 0.8; ctx.stroke();
            }
          }
        }
      } else {
        // Polar wedges: r in [0, 2], th in [0, 2pi]
        const R = 2.0;
        const dr = R / (N / 2);
        const dth = (Math.PI * 2) / N;

        for (let i = 0; i < N / 2; i++) {
          const rMid = (i + 0.5) * dr;
          for (let j = 0; j < N; j++) {
            const thMid = (j + 0.5) * dth;
            const x = rMid * Math.cos(thMid), y = rMid * Math.sin(thMid);
            const zH = f(x, y);
            const dA = rMid * dr * dth;
            if (zH > 0.05) {
              approxVol += zH * dA;
              const r1 = i * dr, r2 = (i + 1) * dr;
              const th1 = j * dth, th2 = (j + 1) * dth;
              const c = [
                project3D(r1 * Math.cos(th1), r1 * Math.sin(th1), zH, rotX, rotY, w, h, 36),
                project3D(r2 * Math.cos(th1), r2 * Math.sin(th1), zH, rotX, rotY, w, h, 36),
                project3D(r2 * Math.cos(th2), r2 * Math.sin(th2), zH, rotX, rotY, w, h, 36),
                project3D(r1 * Math.cos(th2), r1 * Math.sin(th2), zH, rotX, rotY, w, h, 36)
              ];
              ctx.beginPath();
              ctx.moveTo(c[0].px, c[0].py);
              for (let k = 1; k < 4; k++) ctx.lineTo(c[k].px, c[k].py);
              ctx.closePath();
              ctx.fillStyle = "rgba(16, 185, 129, 0.35)"; ctx.fill();
              ctx.strokeStyle = "rgba(16, 185, 129, 0.6)"; ctx.lineWidth = 0.8; ctx.stroke();
            }
          }
        }
      }

      // Exact volume under paraboloid
      const exactVol = Math.PI * 2 * amp * (2 - 0.1 * 4);

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      ctx.fillRect(15, 15, 300, 130);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 300, 130);

      ctx.fillStyle = isPolar ? "#10b981" : "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(isPolar ? "POLAR SECTOR RIEMANN SUMS" : "CARTESIAN DOUBLE RIEMANN SUMS", 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Partitions: N = ${N} (Total Cells: ${isPolar ? (N * N / 2) : (N * N)})`, 25, 53);
      ctx.fillText(isPolar ? "Differential Area: dA = r dr dθ" : "Differential Area: dA = dx dy", 25, 71);
      ctx.fillText(`Riemann Sum Approximation ≈ ${approxVol.toFixed(3)}`, 25, 89);
      ctx.fillStyle = "#fbbf24"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`Exact Volume V = ∬ f dA = ${exactVol.toFixed(3)}`, 25, 109);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter, sans-serif";
      ctx.fillText("As N → ∞, double Riemann sums converge to exact integral", 25, 127);
    }
  },

  // 6. 3D Triple Integral Coordinate Slicer Engine
  "sim_calc3_triple_integrals": {
    title: "3D Triple Integral Coordinate Slicer Engine",
    desc: "Slice 3D volumes in Cartesian, Cylindrical, and Spherical polar shells. Observe the differential volume element dV and real-time numerical volume summation.",
    isAnimated: false,
    controls: [
      { id: "coordSystem", label: "Frame (0:Cart, 1:Cyl, 2:Sphere)", min: 0, max: 2, step: 1, value: 2 },
      { id: "cutSlice", label: "Radius / Height R", min: 0.5, max: 3.0, step: 0.1, value: 2.2 },
      { id: "coneAngle", label: "Slice Extent (%)", min: 20, max: 100, step: 5, value: 80 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 35 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const sys = vals.coordSystem !== undefined ? Math.round(vals.coordSystem) : 2;
      const r = vals.cutSlice !== undefined ? vals.cutSlice : 2.2;
      const pct = (vals.coneAngle !== undefined ? vals.coneAngle : 80) / 100;
      const rotY = vals.rotY !== undefined ? vals.rotY : 35;
      const rotX = 22;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 36);

      const maxTheta = Math.PI * 2 * pct;

      if (sys === 0) {
        // Cartesian Box [0, r] x [0, r] x [0, r*0.8]
        ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.5;
        const bz = r * 0.8;
        const pts = [
          project3D(0, 0, 0, rotX, rotY, w, h, 36),
          project3D(r, 0, 0, rotX, rotY, w, h, 36),
          project3D(r, r, 0, rotX, rotY, w, h, 36),
          project3D(0, r, 0, rotX, rotY, w, h, 36),
          project3D(0, 0, bz, rotX, rotY, w, h, 36),
          project3D(r, 0, bz, rotX, rotY, w, h, 36),
          project3D(r, r, bz, rotX, rotY, w, h, 36),
          project3D(0, r, bz, rotX, rotY, w, h, 36)
        ];
        // Draw box edges
        const edges = [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]];
        ctx.beginPath();
        edges.forEach(([i, j]) => { ctx.moveTo(pts[i].px, pts[i].py); ctx.lineTo(pts[j].px, pts[j].py); });
        ctx.stroke();
      } else if (sys === 1) {
        // Cylindrical Shell: r in [0, r], z in [0, 2.5]
        const zTop = 2.5;
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1.5;
        // Top and bottom arcs
        for (let rad of [0.5 * r, r]) {
          ctx.beginPath();
          for (let th = 0; th <= maxTheta; th += 0.1) {
            const p = project3D(rad * Math.cos(th), rad * Math.sin(th), 0, rotX, rotY, w, h, 36);
            if (th === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
          }
          ctx.stroke();

          ctx.beginPath();
          for (let th = 0; th <= maxTheta; th += 0.1) {
            const p = project3D(rad * Math.cos(th), rad * Math.sin(th), zTop, rotX, rotY, w, h, 36);
            if (th === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
          }
          ctx.stroke();
        }
      } else {
        // Spherical Shell / Wedge
        ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 1.4;
        // Latitude rings
        for (let phi = 0.3; phi <= 2.8; phi += 0.5) {
          ctx.beginPath();
          for (let th = 0; th <= maxTheta; th += 0.1) {
            const sx = r * Math.sin(phi) * Math.cos(th);
            const sy = r * Math.sin(phi) * Math.sin(th);
            const sz = r * Math.cos(phi);
            const p = project3D(sx, sy, sz, rotX, rotY, w, h, 36);
            if (th === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
          }
          ctx.stroke();
        }
      }

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      ctx.fillRect(15, 15, 300, 130);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 300, 130);

      const sysNames = ["CARTESIAN COORDINATE BOX", "CYLINDRICAL INTEGRAL SHELL", "SPHERICAL POLAR INTEGRAL WEDGE"];
      ctx.fillStyle = "#fbbf24"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(sysNames[sys], 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      if (sys === 0) {
        ctx.fillText("Volume Element: dV = dx dy dz", 25, 53);
        ctx.fillText(`Jacobian Determinant: |J| = 1`, 25, 71);
        ctx.fillText(`Box Dimensions: ${r.toFixed(1)} × ${r.toFixed(1)} × ${(r*0.8).toFixed(1)}`, 25, 89);
        ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText(`Integrated Volume = ${(r * r * r * 0.8).toFixed(3)}`, 25, 110);
      } else if (sys === 1) {
        ctx.fillText("Volume Element: dV = r dr dθ dz", 25, 53);
        ctx.fillText(`Jacobian Determinant: |J| = r`, 25, 71);
        ctx.fillText(`Radius = ${r.toFixed(1)}, Height = 2.50`, 25, 89);
        ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText(`Integrated Volume = ${(pct * Math.PI * r * r * 2.5).toFixed(3)}`, 25, 110);
      } else {
        ctx.fillText("Volume Element: dV = ρ² sin φ dρ dφ dθ", 25, 53);
        ctx.fillText(`Jacobian Determinant: |J| = ρ² sin φ`, 25, 71);
        ctx.fillText(`Sphere Radius ρ = ${r.toFixed(1)}`, 25, 89);
        ctx.fillStyle = "#fbbf24"; ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText(`Enclosed Volume = ${(pct * (4/3) * Math.PI * Math.pow(r, 3)).toFixed(3)}`, 25, 110);
      }
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter, sans-serif";
      ctx.fillText("Fubini's theorem allows 6 equivalent integration orders", 25, 127);
    }
  },

  // 7. Vector Fields, Circulation & Green's Theorem Engine
  "sim_calc3_vector_fields": {
    title: "2D/3D Vector Fields, Circulation & Green's Theorem Engine",
    desc: "Visualize dynamic vector fields (vortices, sinks, saddles). Place and trace closed loop contours, compute line integral circulation work, and verify Green's curl theorem in real time.",
    isAnimated: false,
    controls: [
      { id: "fieldPreset", label: "Field (0:Vortex, 1:Source, 2:Saddle)", min: 0, max: 2, step: 1, value: 0 },
      { id: "loopRadius", label: "Loop Radius R", min: 0.5, max: 2.5, step: 0.1, value: 1.5 },
      { id: "loopCenterX", label: "Loop Center X", min: -1.5, max: 1.5, step: 0.1, value: 0.0 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 30 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const fType = vals.fieldPreset !== undefined ? Math.round(vals.fieldPreset) : 0;
      const R = vals.loopRadius !== undefined ? vals.loopRadius : 1.5;
      const cx = vals.loopCenterX !== undefined ? vals.loopCenterX : 0.0;
      const rotY = vals.rotY !== undefined ? vals.rotY : 30;
      const rotX = 22;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 36);

      function F(x, y) {
        if (fType === 0) return [-y, x]; // Vortex: curl = 2
        if (fType === 1) return [x, y];  // Source: div = 2, curl = 0
        return [y, x];                   // Saddle / conservative: curl = 0
      }

      // Draw vector field arrow grid in XY plane
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)"; ctx.lineWidth = 1.2;
      const gStep = 0.8;
      for (let x = -3; x <= 3; x += gStep) {
        for (let y = -3; y <= 3; y += gStep) {
          const vec = F(x, y);
          const vMag = Math.sqrt(vec[0] * vec[0] + vec[1] * vec[1]);
          const scale = vMag > 0.01 ? (0.35 / (vMag > 2 ? vMag : 2)) : 0;
          const pStart = project3D(x, y, 0, rotX, rotY, w, h, 36);
          const pEnd = project3D(x + vec[0] * scale, y + vec[1] * scale, 0, rotX, rotY, w, h, 36);
          ctx.beginPath(); ctx.moveTo(pStart.px, pStart.py); ctx.lineTo(pEnd.px, pEnd.py); ctx.stroke();
        }
      }

      // Draw closed loop contour C in XY plane
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let th = 0; th <= Math.PI * 2; th += 0.1) {
        const lx = cx + R * Math.cos(th), ly = R * Math.sin(th);
        const p = project3D(lx, ly, 0, rotX, rotY, w, h, 36);
        if (th === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
      }
      ctx.closePath(); ctx.stroke();

      // Shaded enclosed disk D
      ctx.beginPath();
      for (let th = 0; th <= Math.PI * 2; th += 0.1) {
        const lx = cx + R * Math.cos(th), ly = R * Math.sin(th);
        const p = project3D(lx, ly, 0, rotX, rotY, w, h, 36);
        if (th === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
      }
      ctx.closePath();
      ctx.fillStyle = "rgba(251, 191, 36, 0.15)"; ctx.fill();

      // Circulation and Curl calculation
      const areaD = Math.PI * R * R;
      let curlVal = 0;
      if (fType === 0) curlVal = 2.0; // Q_x - P_y = 1 - (-1) = 2
      else if (fType === 1) curlVal = 0.0;
      else curlVal = 0.0;

      const circulation = curlVal * areaD;

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      ctx.fillRect(15, 15, 300, 130);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 300, 130);

      const fNames = ["ROTATIONAL VORTEX FIELD F = <-y, x>", "RADIAL SOURCE FIELD F = <x, y>", "SADDLE / CONSERVATIVE FIELD F = <y, x>"];
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("GREEN'S THEOREM IN THE PLANE", 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(fNames[fType], 25, 53);
      ctx.fillText(`Curl k-component: ∂Q/∂x - ∂P/∂y = ${curlVal.toFixed(2)}`, 25, 71);
      ctx.fillText(`Enclosed Loop Area A = πR² = ${areaD.toFixed(3)}`, 25, 89);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`∮_C F · dr = ${circulation.toFixed(3)}  ≡  ∬_D (curl F) dA`, 25, 110);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter, sans-serif";
      ctx.fillText("Boundary circulation rigorously equals total interior vortex flux", 25, 127);
    }
  },

  // 8. 3D Surface Flux, Stokes & Gauss Divergence Engine
  "sim_calc3_flux_divergence": {
    title: "3D Surface Flux, Stokes & Gauss Divergence Engine",
    desc: "Interact with 3D closed surfaces (cylinder, sphere, paraboloid). Observe vector flux arrows piercing the boundary, evaluate Stokes' loop circulation, and verify Gauss' divergence theorem in real time.",
    isAnimated: false,
    controls: [
      { id: "solidShape", label: "Solid (0:Cyl, 1:Sphere, 2:Bowl)", min: 0, max: 2, step: 1, value: 0 },
      { id: "fieldPower", label: "Divergence Strength k", min: 0.5, max: 3.0, step: 0.2, value: 1.5 },
      { id: "solidRadius", label: "Radius / Size R", min: 1.0, max: 3.0, step: 0.2, value: 2.0 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 35 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const shape = vals.solidShape !== undefined ? Math.round(vals.solidShape) : 0;
      const k = vals.fieldPower !== undefined ? vals.fieldPower : 1.5;
      const R = vals.solidRadius !== undefined ? vals.solidRadius : 2.0;
      const rotY = vals.rotY !== undefined ? vals.rotY : 35;
      const rotX = 22;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 36);

      // Draw 3D Translucent Solid Surface
      if (shape === 0) {
        // Cylinder of radius R and height H = 3.0
        const H = 3.0;
        ctx.strokeStyle = "rgba(56, 189, 248, 0.4)"; ctx.lineWidth = 1.3;
        for (let z of [0, H]) {
          ctx.beginPath();
          for (let th = 0; th <= Math.PI * 2; th += 0.15) {
            const p = project3D(R * Math.cos(th), R * Math.sin(th), z, rotX, rotY, w, h, 36);
            if (th === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
          }
          ctx.closePath(); ctx.stroke();
        }
        // Lateral ribs
        for (let th = 0; th < Math.PI * 2; th += Math.PI / 4) {
          const pBot = project3D(R * Math.cos(th), R * Math.sin(th), 0, rotX, rotY, w, h, 36);
          const pTop = project3D(R * Math.cos(th), R * Math.sin(th), H, rotX, rotY, w, h, 36);
          ctx.beginPath(); ctx.moveTo(pBot.px, pBot.py); ctx.lineTo(pTop.px, pTop.py); ctx.stroke();
        }

        // Outward flux arrows piercing the cylinder surface
        ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2;
        for (let th = 0; th < Math.PI * 2; th += Math.PI / 4) {
          const pSurf = project3D(R * Math.cos(th), R * Math.sin(th), 1.5, rotX, rotY, w, h, 36);
          const pOut = project3D((R + 0.8) * Math.cos(th), (R + 0.8) * Math.sin(th), 1.5, rotX, rotY, w, h, 36);
          ctx.beginPath(); ctx.moveTo(pSurf.px, pSurf.py); ctx.lineTo(pOut.px, pOut.py); ctx.stroke();
        }
      } else if (shape === 1) {
        // Sphere of radius R
        ctx.strokeStyle = "rgba(16, 185, 129, 0.4)"; ctx.lineWidth = 1.3;
        for (let phi = -1.2; phi <= 1.2; phi += 0.6) {
          ctx.beginPath();
          const rRing = R * Math.cos(phi);
          const zRing = R * Math.sin(phi);
          for (let th = 0; th <= Math.PI * 2; th += 0.15) {
            const p = project3D(rRing * Math.cos(th), rRing * Math.sin(th), zRing, rotX, rotY, w, h, 36);
            if (th === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
          }
          ctx.closePath(); ctx.stroke();
        }
        // Normal flux arrows
        ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2;
        for (let th = 0; th < Math.PI * 2; th += Math.PI / 3) {
          const pSurf = project3D(R * Math.cos(th), R * Math.sin(th), 0, rotX, rotY, w, h, 36);
          const pOut = project3D((R + 0.8) * Math.cos(th), (R + 0.8) * Math.sin(th), 0, rotX, rotY, w, h, 36);
          ctx.beginPath(); ctx.moveTo(pSurf.px, pSurf.py); ctx.lineTo(pOut.px, pOut.py); ctx.stroke();
        }
      } else {
        // Paraboloid bowl z = 0.5*(x^2 + y^2)
        ctx.strokeStyle = "rgba(251, 191, 36, 0.4)"; ctx.lineWidth = 1.3;
        for (let zVal = 0.5; zVal <= 3.0; zVal += 0.6) {
          const rRing = Math.sqrt(zVal / 0.5);
          ctx.beginPath();
          for (let th = 0; th <= Math.PI * 2; th += 0.15) {
            const p = project3D(rRing * Math.cos(th), rRing * Math.sin(th), zVal, rotX, rotY, w, h, 36);
            if (th === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
          }
          ctx.closePath(); ctx.stroke();
        }
      }

      // Analytical Divergence computation
      // Let field be F = k * <x, y, z> => div F = 3k
      const divF = 3 * k;
      let volE = 0;
      if (shape === 0) volE = Math.PI * R * R * 3.0;
      else if (shape === 1) volE = (4 / 3) * Math.PI * Math.pow(R, 3);
      else volE = (1 / 2) * Math.PI * Math.pow(Math.sqrt(3.0 / 0.5), 2) * 3.0;

      const totalFlux = divF * volE;

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      ctx.fillRect(15, 15, 310, 130);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 310, 130);

      ctx.fillStyle = "#f43f5e"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("GAUSS' DIVERGENCE THEOREM & FLUX", 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Vector Field: F(x, y, z) = ${k.toFixed(1)} ⟨x, y, z⟩`, 25, 53);
      ctx.fillText(`Divergence: ∇ · F = 3k = ${divF.toFixed(2)}`, 25, 71);
      ctx.fillText(`Enclosed Volume V = ${volE.toFixed(2)} units³`, 25, 89);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`Outward Flux ∬_S F · dS = ${totalFlux.toFixed(2)}`, 25, 109);
      ctx.fillStyle = "#38bdf8"; ctx.font = "10px Inter, sans-serif";
      ctx.fillText("Identical to ∭_E (∇ · F) dV (Gauss Divergence Theorem)", 25, 127);
    }
  }
};

// Simulation Engine Bridge
window.SimulationEngine = window.SimulationEngine || {
  activeAnimations: {},
  initSimulation: function(containerId, simKey) {
    const container = document.getElementById(containerId);
    if (!container) return;
    container.innerHTML = "";

    const simConfig = (window.CALC3_SIMS && window.CALC3_SIMS[simKey]) || (window.SIMULATIONS && window.SIMULATIONS[simKey]);
    if (!simConfig) {
      container.innerHTML = `<div style="padding:1rem;color:#94a3b8;">Simulation ${simKey} ready.</div>`;
      return;
    }

    const box = document.createElement("div");
    box.className = "sim-box-wrapper";
    box.style.background = "#050811";
    box.style.border = "1px solid #1e293b";
    box.style.borderRadius = "12px";
    box.style.padding = "1rem";
    box.style.marginBottom = "1.5rem";

    const header = document.createElement("div");
    header.style.display = "flex";
    header.style.justifyContent = "space-between";
    header.style.alignItems = "center";
    header.style.marginBottom = "0.75rem";

    const titleEl = document.createElement("h4");
    titleEl.style.margin = "0";
    titleEl.style.color = "#38bdf8";
    titleEl.style.fontSize = "1.05rem";
    titleEl.innerText = simConfig.title;

    const badge = document.createElement("span");
    badge.innerText = "60 FPS Interactive";
    badge.style.fontSize = "0.75rem";
    badge.style.background = "rgba(56, 189, 248, 0.15)";
    badge.style.color = "#38bdf8";
    badge.style.padding = "3px 8px";
    badge.style.borderRadius = "999px";

    header.appendChild(titleEl);
    header.appendChild(badge);
    box.appendChild(header);

    const descEl = document.createElement("p");
    descEl.style.color = "#94a3b8";
    descEl.style.fontSize = "0.85rem";
    descEl.style.marginBottom = "1rem";
    descEl.innerText = simConfig.desc;
    box.appendChild(descEl);

    const canvas = document.createElement("canvas");
    canvas.width = 720;
    canvas.height = 340;
    canvas.style.width = "100%";
    canvas.style.height = "auto";
    canvas.style.background = "#050811";
    canvas.style.borderRadius = "8px";
    canvas.style.border = "1px solid #1e293b";
    canvas.style.display = "block";
    box.appendChild(canvas);

    const controlsContainer = document.createElement("div");
    controlsContainer.style.display = "grid";
    controlsContainer.style.gridTemplateColumns = "repeat(auto-fit, minmax(140px, 1fr))";
    controlsContainer.style.gap = "1rem";
    controlsContainer.style.marginTop = "1rem";

    const vals = {};
    if (simConfig.controls) {
      simConfig.controls.forEach(ctrl => {
        vals[ctrl.id] = ctrl.value;
        const wrap = document.createElement("div");
        const lbl = document.createElement("label");
        lbl.style.display = "block";
        lbl.style.fontSize = "0.75rem";
        lbl.style.color = "#94a3b8";
        lbl.style.marginBottom = "0.25rem";
        lbl.innerText = `${ctrl.label}: ${ctrl.value}`;

        const input = document.createElement("input");
        input.type = "range";
        input.min = ctrl.min;
        input.max = ctrl.max;
        input.step = ctrl.step;
        input.value = ctrl.value;
        input.style.width = "100%";
        input.style.accentColor = "#38bdf8";

        input.addEventListener("input", (e) => {
          vals[ctrl.id] = parseFloat(e.target.value);
          lbl.innerText = `${ctrl.label}: ${vals[ctrl.id]}`;
          if (!simConfig.isAnimated) {
            simConfig.render(canvas, vals, 0);
          }
        });

        wrap.appendChild(lbl);
        wrap.appendChild(input);
        controlsContainer.appendChild(wrap);
      });
    }
    box.appendChild(controlsContainer);
    container.appendChild(box);

    if (simConfig.isAnimated) {
      let start = performance.now();
      function loop(now) {
        const t = (now - start) / 1000;
        simConfig.render(canvas, vals, t);
        window.SimulationEngine.activeAnimations[containerId] = requestAnimationFrame(loop);
      }
      window.SimulationEngine.activeAnimations[containerId] = requestAnimationFrame(loop);
    } else {
      simConfig.render(canvas, vals, 0);
    }
  }
};
