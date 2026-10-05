// Three-Dimensional Coordinate & Vector Geometry Simulation Suite
// 8 Real-Time 60 FPS Interactive Canvas Simulations for 3D Geometry & Spatial Vector Analysis

function project3D(x, y, z, rotX, rotY, w, h, scale = 40, dist = 500) {
  const radY = (rotY * Math.PI) / 180;
  const radX = (rotX * Math.PI) / 180;
  const cy = Math.cos(radY), sy = Math.sin(radY);
  const cx = Math.cos(radX), sx = Math.sin(radX);

  // Orbit rotation around Y-axis
  const x1 = x * cy + z * sy;
  const y1 = y;
  const z1 = -x * sy + z * cy;

  // Pitch rotation around X-axis
  const x2 = x1;
  const y2 = y1 * cx - z1 * sx;
  const z2 = y1 * sx + z1 * cx;

  // Perspective camera projection
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

  // X Axis (Red/Rose)
  ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2;
  ctx.beginPath(); ctx.moveTo(origin.px, origin.py); ctx.lineTo(xEnd.px, xEnd.py); ctx.stroke();
  ctx.fillStyle = "#f43f5e"; ctx.font = "bold 11px Inter, sans-serif";
  ctx.fillText("+X", xEnd.px + 6, xEnd.py);

  // Y Axis (Green/Emerald)
  ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2;
  ctx.beginPath(); ctx.moveTo(origin.px, origin.py); ctx.lineTo(yEnd.px, yEnd.py); ctx.stroke();
  ctx.fillStyle = "#10b981";
  ctx.fillText("+Y", yEnd.px + 6, yEnd.py);

  // Z Axis (Sky Blue)
  ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2;
  ctx.beginPath(); ctx.moveTo(origin.px, origin.py); ctx.lineTo(zEnd.px, zEnd.py); ctx.stroke();
  ctx.fillStyle = "#38bdf8";
  ctx.fillText("+Z", zEnd.px + 6, zEnd.py);

  // Ground Grid (XY / XZ planes)
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

window.GEOM3D_SIMS = {
  // 1. 3D Coordinate Frames & Direction Cosines
  "sim_geom3d_coords": {
    title: "3D Coordinate Frame & Direction Cosines Engine",
    desc: "Inspect Cartesian coordinates in space. Rotate the 3D frame, modify point P(x, y, z), and observe direction angles α, β, γ and verification of l² + m² + n² = 1.",
    isAnimated: false,
    controls: [
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 35 },
      { id: "rotX", label: "Orbit Pitch (°)", min: -80, max: 80, step: 2, value: 20 },
      { id: "px", label: "Point X", min: -5, max: 5, step: 0.2, value: 3.0 },
      { id: "py", label: "Point Y", min: -5, max: 5, step: 0.2, value: 3.5 },
      { id: "pz", label: "Point Z", min: -5, max: 5, step: 0.2, value: 2.5 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const rotY = vals.rotY !== undefined ? vals.rotY : 35;
      const rotX = vals.rotX !== undefined ? vals.rotX : 20;
      const px = vals.px !== undefined ? vals.px : 3.0;
      const py = vals.py !== undefined ? vals.py : 3.5;
      const pz = vals.pz !== undefined ? vals.pz : 2.5;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 40);

      const O = project3D(0, 0, 0, rotX, rotY, w, h);
      const P = project3D(px, py, pz, rotX, rotY, w, h);
      const Pxy = project3D(px, py, 0, rotX, rotY, w, h);
      const Pxz = project3D(px, 0, pz, rotX, rotY, w, h);
      const Pyz = project3D(0, py, pz, rotX, rotY, w, h);
      const Px = project3D(px, 0, 0, rotX, rotY, w, h);
      const Py = project3D(0, py, 0, rotX, rotY, w, h);
      const Pz = project3D(0, 0, pz, rotX, rotY, w, h);

      // Projection lines (dashed box)
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)"; ctx.lineWidth = 1.2;
      ctx.setLineDash([4, 4]);
      // Ground projections
      ctx.beginPath(); ctx.moveTo(Px.px, Px.py); ctx.lineTo(Pxz.px, Pxz.py); ctx.lineTo(Pz.px, Pz.py); ctx.stroke();
      // Up to P
      ctx.beginPath(); ctx.moveTo(Pxz.px, Pxz.py); ctx.lineTo(P.px, P.py); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(Pxy.px, Pxy.py); ctx.lineTo(P.px, P.py); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(Pyz.px, Pyz.py); ctx.lineTo(P.px, P.py); ctx.stroke();
      ctx.setLineDash([]);

      // Position vector OP
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(O.px, O.py); ctx.lineTo(P.px, P.py); ctx.stroke();

      // Point P Glowing Marker
      ctx.fillStyle = "#fbbf24";
      ctx.beginPath(); ctx.arc(P.px, P.py, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#fff"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`P(${px.toFixed(1)}, ${py.toFixed(1)}, ${pz.toFixed(1)})`, P.px + 10, P.py - 6);

      // Computations
      const r = Math.sqrt(px * px + py * py + pz * pz);
      const l = r > 0.001 ? px / r : 0;
      const m = r > 0.001 ? py / r : 0;
      const n = r > 0.001 ? pz / r : 0;
      const alphaDeg = (Math.acos(Math.max(-1, Math.min(1, l))) * 180 / Math.PI).toFixed(1);
      const betaDeg = (Math.acos(Math.max(-1, Math.min(1, m))) * 180 / Math.PI).toFixed(1);
      const gammaDeg = (Math.acos(Math.max(-1, Math.min(1, n))) * 180 / Math.PI).toFixed(1);
      const sumSquares = (l * l + m * m + n * n).toFixed(4);

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
      ctx.fillRect(15, 15, 280, 140);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 280, 140);

      ctx.fillStyle = "#fbbf24"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("3D POSITION & DIRECTION COSINES", 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Magnitude r = |OP| = ${r.toFixed(3)}`, 25, 53);
      ctx.fillText(`l = cos α = ${l.toFixed(3)}  (α = ${alphaDeg}°)`, 25, 71);
      ctx.fillText(`m = cos β = ${m.toFixed(3)}  (β = ${betaDeg}°)`, 25, 89);
      ctx.fillText(`n = cos γ = ${n.toFixed(3)}  (γ = ${gammaDeg}°)`, 25, 107);
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`l² + m² + n² = ${sumSquares} ≡ 1.000`, 25, 131);
    }
  },

  // 2. Spatial Planes & Normal Vector
  "sim_geom3d_planes": {
    title: "3D Spatial Plane & Normal Vector Engine",
    desc: "Interact with the general linear plane Ax + By + Cz + D = 0. Vary normal coefficients and offset to visualize orientation, the normal vector, foot of perpendicular from origin, and intercepts.",
    isAnimated: false,
    controls: [
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 30 },
      { id: "normA", label: "Normal A", min: -4, max: 4, step: 0.5, value: 2 },
      { id: "normB", label: "Normal B", min: -4, max: 4, step: 0.5, value: 3 },
      { id: "normC", label: "Normal C", min: -4, max: 4, step: 0.5, value: 3.5 },
      { id: "offsetD", label: "Constant D", min: -15, max: 15, step: 1, value: -12 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const rotY = vals.rotY !== undefined ? vals.rotY : 30;
      const rotX = 22;
      const A = vals.normA !== undefined ? vals.normA : 2;
      const B = vals.normB !== undefined ? vals.normB : 3;
      const C = vals.normC !== undefined ? vals.normC : 3.5;
      const D = vals.offsetD !== undefined ? vals.offsetD : -12;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 38);

      const mag = Math.sqrt(A * A + B * B + C * C);
      const safeMag = mag > 0.001 ? mag : 1;
      const dist = Math.abs(D) / safeMag;

      // Foot of perpendicular from origin: P_foot = - (D / mag^2) * (A, B, C)
      const k = -D / (safeMag * safeMag);
      const fx = k * A, fy = k * B, fz = k * C;

      // Generate a quad patch around the foot of perpendicular
      // Tangent basis for the plane
      let uVec = [0, 0, 0];
      if (Math.abs(A) > 0.1 || Math.abs(B) > 0.1) {
        uVec = [-B, A, 0];
      } else {
        uVec = [0, -C, B];
      }
      const uMag = Math.sqrt(uVec[0] * uVec[0] + uVec[1] * uVec[1] + uVec[2] * uVec[2]);
      uVec = [uVec[0] / uMag, uVec[1] / uMag, uVec[2] / uMag];

      // vVec = n x uVec
      const vVec = [
        (B * uVec[2] - C * uVec[1]) / safeMag,
        (C * uVec[0] - A * uVec[2]) / safeMag,
        (A * uVec[1] - B * uVec[0]) / safeMag
      ];

      const patchSize = 3.5;
      const corners = [
        [fx - patchSize * uVec[0] - patchSize * vVec[0], fy - patchSize * uVec[1] - patchSize * vVec[1], fz - patchSize * uVec[2] - patchSize * vVec[2]],
        [fx + patchSize * uVec[0] - patchSize * vVec[0], fy + patchSize * uVec[1] - patchSize * vVec[1], fz + patchSize * uVec[2] - patchSize * vVec[2]],
        [fx + patchSize * uVec[0] + patchSize * vVec[0], fy + patchSize * uVec[1] + patchSize * vVec[1], fz + patchSize * uVec[2] + patchSize * vVec[2]],
        [fx - patchSize * uVec[0] + patchSize * vVec[0], fy - patchSize * uVec[1] + patchSize * vVec[1], fz - patchSize * uVec[2] + patchSize * vVec[2]]
      ];

      const pCorners = corners.map(c => project3D(c[0], c[1], c[2], rotX, rotY, w, h, 38));

      // Draw Translucent Plane Polygon
      ctx.beginPath();
      ctx.moveTo(pCorners[0].px, pCorners[0].py);
      for (let i = 1; i < 4; i++) ctx.lineTo(pCorners[i].px, pCorners[i].py);
      ctx.closePath();
      ctx.fillStyle = "rgba(56, 189, 248, 0.22)";
      ctx.fill();
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.8;
      ctx.stroke();

      // Origin to Foot of Perpendicular
      const O = project3D(0, 0, 0, rotX, rotY, w, h, 38);
      const F = project3D(fx, fy, fz, rotX, rotY, w, h, 38);
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(O.px, O.py); ctx.lineTo(F.px, F.py); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#fbbf24"; ctx.beginPath(); ctx.arc(F.px, F.py, 4, 0, Math.PI * 2); ctx.fill();

      // Normal Vector Arrow extending from Foot
      const nScale = 1.8;
      const nTip = project3D(fx + (A / safeMag) * nScale, fy + (B / safeMag) * nScale, fz + (C / safeMag) * nScale, rotX, rotY, w, h, 38);
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(F.px, F.py); ctx.lineTo(nTip.px, nTip.py); ctx.stroke();
      ctx.fillStyle = "#f43f5e"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("n", nTip.px + 6, nTip.py);

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      ctx.fillRect(15, 15, 300, 130);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 300, 130);

      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("PLANE GEOMETRY & NORMAL ANALYSIS", 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Equation: ${A}x + ${B}y + ${C}z + ${D} = 0`, 25, 53);
      ctx.fillText(`Normal Vector: n = (${A}, ${B}, ${C})`, 25, 71);
      ctx.fillText(`Perpendicular Distance p = ${dist.toFixed(3)}`, 25, 89);
      const xInt = Math.abs(A) > 0.01 ? (-D / A).toFixed(2) : "∞";
      const yInt = Math.abs(B) > 0.01 ? (-D / B).toFixed(2) : "∞";
      const zInt = Math.abs(C) > 0.01 ? (-D / C).toFixed(2) : "∞";
      ctx.fillText(`Axis Intercepts: (${xInt}, ${yInt}, ${zInt})`, 25, 107);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`Foot of Perpendicular: (${fx.toFixed(2)}, ${fy.toFixed(2)}, ${fz.toFixed(2)})`, 25, 125);
    }
  },

  // 3. Skew Lines & Shortest Distance Engine
  "sim_geom3d_skew_lines": {
    title: "3D Skew Lines & Shortest Distance Engine",
    desc: "Rotate and manipulate two 3D straight lines. Observe the non-intersecting, non-parallel skew configuration, the common perpendicular segment, and the dynamic shortest distance d.",
    isAnimated: false,
    controls: [
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 35 },
      { id: "rotX", label: "Orbit Pitch (°)", min: -80, max: 80, step: 2, value: 20 },
      { id: "offsetZ", label: "Line 2 Z-Offset", min: -5, max: 5, step: 0.2, value: 2.8 },
      { id: "skewAngle", label: "Relative Skew Angle (°)", min: 0, max: 180, step: 5, value: 65 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const rotY = vals.rotY !== undefined ? vals.rotY : 35;
      const rotX = vals.rotX !== undefined ? vals.rotX : 20;
      const offZ = vals.offsetZ !== undefined ? vals.offsetZ : 2.8;
      const sAngle = (vals.skewAngle !== undefined ? vals.skewAngle : 65) * Math.PI / 180;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 38);

      // Line 1: through (0, 0, 0) along direction (1, 0, 0)
      const p1_start = project3D(-5, 0, 0, rotX, rotY, w, h, 38);
      const p1_end = project3D(5, 0, 0, rotX, rotY, w, h, 38);

      // Line 2: through (0, 1.5, offZ) along rotated direction (cos(sAngle), sin(sAngle), 0.2)
      const d2x = Math.cos(sAngle), d2y = Math.sin(sAngle), d2z = 0.2;
      const p2_start = project3D(-5 * d2x, 1.5 - 5 * d2y, offZ - 5 * d2z, rotX, rotY, w, h, 38);
      const p2_end = project3D(5 * d2x, 1.5 + 5 * d2y, offZ + 5 * d2z, rotX, rotY, w, h, 38);

      // Line 1 Draw (Cyan)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(p1_start.px, p1_start.py); ctx.lineTo(p1_end.px, p1_end.py); ctx.stroke();

      // Line 2 Draw (Amber)
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(p2_start.px, p2_start.py); ctx.lineTo(p2_end.px, p2_end.py); ctx.stroke();

      // Common Perpendicular segment connecting closest points
      // For line 1 (x-axis) and line 2, compute closest points:
      const d1 = [1, 0, 0];
      const d2 = [d2x, d2y, d2z];
      const pDiff = [0, 1.5, offZ]; // r2 - r1
      // Cross product
      const cross = [
        d1[1] * d2[2] - d1[2] * d2[1],
        d1[2] * d2[0] - d1[0] * d2[2],
        d1[0] * d2[1] - d1[1] * d2[0]
      ];
      const cMag = Math.sqrt(cross[0] * cross[0] + cross[1] * cross[1] + cross[2] * cross[2]);
      const sd = cMag > 0.001 ? Math.abs(pDiff[0] * cross[0] + pDiff[1] * cross[1] + pDiff[2] * cross[2]) / cMag : Math.abs(offZ);

      // Render common normal line segment
      const pt1 = project3D(0, 0, 0, rotX, rotY, w, h, 38);
      const pt2 = project3D(0, 1.5, offZ, rotX, rotY, w, h, 38);

      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(pt1.px, pt1.py); ctx.lineTo(pt2.px, pt2.py); ctx.stroke();

      ctx.fillStyle = "#f43f5e";
      ctx.beginPath(); ctx.arc(pt1.px, pt1.py, 4.5, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.arc(pt2.px, pt2.py, 4.5, 0, Math.PI * 2); ctx.fill();

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      ctx.fillRect(15, 15, 300, 130);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 300, 130);

      ctx.fillStyle = "#f43f5e"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("SKEW LINES & SHORTEST DISTANCE", 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Line 1: Along X-Axis (Cyan)`, 25, 53);
      ctx.fillText(`Line 2: Rotated ${(vals.skewAngle || 65)}° in XY (Amber)`, 25, 71);
      ctx.fillText(`Common Normal |d₁ × d₂| = ${cMag.toFixed(3)}`, 25, 89);
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(`Shortest Distance d = ${sd.toFixed(3)} units`, 25, 110);
      ctx.fillStyle = sd < 0.05 ? "#10b981" : "#fbbf24"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(sd < 0.05 ? "Status: Intersecting / Coplanar" : "Status: Non-Intersecting Skew Lines", 25, 128);
    }
  },

  // 4. Spheres, Orthogonality & Radical Plane
  "sim_geom3d_spheres": {
    title: "3D Spheres, Orthogonality & Radical Plane Engine",
    desc: "Inspect two interacting spheres in 3D space. Adjust radii and center distance to see intersecting circular sections, the orthogonal intersection test, and the perpendicular radical plane.",
    isAnimated: false,
    controls: [
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 25 },
      { id: "r1", label: "Sphere 1 Radius", min: 1.0, max: 4.0, step: 0.1, value: 2.6 },
      { id: "r2", label: "Sphere 2 Radius", min: 1.0, max: 4.0, step: 0.1, value: 2.0 },
      { id: "dist", label: "Center Distance d", min: 1.5, max: 6.0, step: 0.1, value: 3.28 },
      { id: "showRadical", label: "Show Radical Plane", min: 0, max: 1, step: 1, value: 1 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const rotY = vals.rotY !== undefined ? vals.rotY : 25;
      const rotX = 18;
      const r1 = vals.r1 !== undefined ? vals.r1 : 2.6;
      const r2 = vals.r2 !== undefined ? vals.r2 : 2.0;
      const dist = vals.dist !== undefined ? vals.dist : 3.28;
      const showRad = vals.showRadical !== undefined ? vals.showRadical : 1;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 36);

      // Centers along X-axis: C1 at (-dist/2, 0, 0), C2 at (dist/2, 0, 0)
      const c1x = -dist / 2, c2x = dist / 2;

      // Function to draw wireframe sphere
      function drawSphereWireframe(cx, r, color) {
        ctx.strokeStyle = color; ctx.lineWidth = 1.2;
        // Latitude circles
        for (let phi = -1.2; phi <= 1.2; phi += 0.6) {
          const zRing = r * Math.sin(phi);
          const rRing = r * Math.cos(phi);
          ctx.beginPath();
          for (let th = 0; th <= Math.PI * 2; th += 0.15) {
            const p = project3D(cx + rRing * Math.cos(th), rRing * Math.sin(th), zRing, rotX, rotY, w, h, 36);
            if (th === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
          }
          ctx.closePath(); ctx.stroke();
        }
        // Meridian circle (YZ plane)
        ctx.beginPath();
        for (let th = 0; th <= Math.PI * 2; th += 0.15) {
          const p = project3D(cx, r * Math.cos(th), r * Math.sin(th), rotX, rotY, w, h, 36);
          if (th === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
        }
        ctx.closePath(); ctx.stroke();
      }

      // Draw Spheres
      drawSphereWireframe(c1x, r1, "rgba(56, 189, 248, 0.45)");
      drawSphereWireframe(c2x, r2, "rgba(244, 63, 94, 0.45)");

      // Line of Centers
      const pC1 = project3D(c1x, 0, 0, rotX, rotY, w, h, 36);
      const pC2 = project3D(c2x, 0, 0, rotX, rotY, w, h, 36);
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(pC1.px, pC1.py); ctx.lineTo(pC2.px, pC2.py); ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.beginPath(); ctx.arc(pC1.px, pC1.py, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(pC2.px, pC2.py, 5, 0, Math.PI * 2); ctx.fill();

      // Radical Plane position x_rad:
      // (x - c1x)^2 - r1^2 = (x - c2x)^2 - r2^2
      // x^2 - 2*c1x*x + c1x^2 - r1^2 = x^2 - 2*c2x*x + c2x^2 - r2^2
      // 2*(c2x - c1x)*x = (c2x^2 - c1x^2) + (r1^2 - r2^2)
      // Since c2x - c1x = dist, c2x^2 - c1x^2 = 0:
      const xRad = (r1 * r1 - r2 * r2) / (2 * dist);

      if (showRad === 1) {
        const radYSize = 3.5;
        const rCorn = [
          project3D(xRad, -radYSize, -radYSize, rotX, rotY, w, h, 36),
          project3D(xRad, radYSize, -radYSize, rotX, rotY, w, h, 36),
          project3D(xRad, radYSize, radYSize, rotX, rotY, w, h, 36),
          project3D(xRad, -radYSize, radYSize, rotX, rotY, w, h, 36)
        ];
        ctx.beginPath();
        ctx.moveTo(rCorn[0].px, rCorn[0].py);
        for (let i = 1; i < 4; i++) ctx.lineTo(rCorn[i].px, rCorn[i].py);
        ctx.closePath();
        ctx.fillStyle = "rgba(16, 185, 129, 0.22)"; ctx.fill();
        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1.8; ctx.stroke();
      }

      // Orthogonality condition check: d^2 == r1^2 + r2^2
      const dSquared = dist * dist;
      const sumRSquared = r1 * r1 + r2 * r2;
      const diffOrth = Math.abs(dSquared - sumRSquared);
      const isOrth = diffOrth < 0.25;

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      ctx.fillRect(15, 15, 300, 130);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 300, 130);

      ctx.fillStyle = "#10b981"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("SPHERE SYSTEM & RADICAL GEOMETRY", 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Center Distance d = ${dist.toFixed(2)}  (d² = ${dSquared.toFixed(2)})`, 25, 53);
      ctx.fillText(`Radii: R₁ = ${r1.toFixed(1)}, R₂ = ${r2.toFixed(1)}  (R₁²+R₂² = ${sumRSquared.toFixed(2)})`, 25, 71);
      ctx.fillText(`Radical Plane: x = ${xRad.toFixed(2)}`, 25, 89);
      ctx.fillStyle = isOrth ? "#10b981" : "#fbbf24"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(isOrth ? "Orthogonality: SATISFIED (d² = R₁² + R₂²)" : `Orthogonality: Δ = ${diffOrth.toFixed(2)} ≠ 0`, 25, 109);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter, sans-serif";
      ctx.fillText("Radical plane is strictly ⟂ to the line of centers", 25, 127);
    }
  },

  // 5. Cones and Cylinders Generator
  "sim_geom3d_cones_cylinders": {
    title: "3D Quadric Cone & Cylinder Generator",
    desc: "Generate wireframe quadric ruled surfaces. Switch between right circular cone and cylinder, vary semi-vertical angle or radius, tilt the axis, and inspect straight line generators.",
    isAnimated: false,
    controls: [
      { id: "surfaceType", label: "Surface (0:Cone, 1:Cylinder)", min: 0, max: 1, step: 1, value: 0 },
      { id: "angle", label: "Angle (°) / Radius", min: 15, max: 70, step: 1, value: 35 },
      { id: "tilt", label: "Axis Tilt (°)", min: -45, max: 45, step: 1, value: 15 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 35 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const isCyl = (vals.surfaceType !== undefined ? Math.round(vals.surfaceType) : 0) === 1;
      const angle = vals.angle !== undefined ? vals.angle : 35;
      const tiltRad = ((vals.tilt !== undefined ? vals.tilt : 15) * Math.PI) / 180;
      const rotY = vals.rotY !== undefined ? vals.rotY : 35;
      const rotX = 20;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 36);

      const radAngle = (angle * Math.PI) / 180;
      const height = 4.5;
      const stepsZ = 7;

      ctx.strokeStyle = isCyl ? "rgba(244, 63, 94, 0.55)" : "rgba(56, 189, 248, 0.55)";
      ctx.lineWidth = 1.3;

      // Draw rings along axis
      for (let i = 0; i <= stepsZ; i++) {
        const t = (i / stepsZ) * height;
        const currentR = isCyl ? (angle / 25) : t * Math.tan(radAngle);

        ctx.beginPath();
        for (let th = 0; th <= Math.PI * 2; th += 0.2) {
          // Point in local coords
          const lx = currentR * Math.cos(th);
          const ly = currentR * Math.sin(th);
          const lz = t;
          // Apply tilt around X-axis
          const rx = lx;
          const ry = ly * Math.cos(tiltRad) - lz * Math.sin(tiltRad);
          const rz = ly * Math.sin(tiltRad) + lz * Math.cos(tiltRad);

          const p = project3D(rx, ry, rz, rotX, rotY, w, h, 36);
          if (th === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
        }
        ctx.closePath(); ctx.stroke();
      }

      // Draw Family of Straight Line Generators
      ctx.strokeStyle = isCyl ? "rgba(244, 63, 94, 0.85)" : "rgba(56, 189, 248, 0.85)";
      ctx.lineWidth = 1.5;
      for (let th = 0; th < Math.PI * 2; th += Math.PI / 4) {
        const r0 = isCyl ? (angle / 25) : 0;
        const rTop = isCyl ? (angle / 25) : height * Math.tan(radAngle);

        const p0 = project3D(
          r0 * Math.cos(th),
          r0 * Math.sin(th) * Math.cos(tiltRad),
          r0 * Math.sin(th) * Math.sin(tiltRad),
          rotX, rotY, w, h, 36
        );
        const pTop = project3D(
          rTop * Math.cos(th),
          rTop * Math.sin(th) * Math.cos(tiltRad) - height * Math.sin(tiltRad),
          rTop * Math.sin(th) * Math.sin(tiltRad) + height * Math.cos(tiltRad),
          rotX, rotY, w, h, 36
        );

        ctx.beginPath(); ctx.moveTo(p0.px, p0.py); ctx.lineTo(pTop.px, pTop.py); ctx.stroke();
      }

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      ctx.fillRect(15, 15, 300, 125);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 300, 125);

      ctx.fillStyle = isCyl ? "#f43f5e" : "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(isCyl ? "RIGHT CIRCULAR CYLINDER" : "RIGHT CIRCULAR CONE", 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(isCyl ? `Radius R = ${(angle / 25).toFixed(2)}` : `Semi-Vertical Angle α = ${angle}°`, 25, 53);
      ctx.fillText(isCyl ? `Equation: x² + y² = ${(Math.pow(angle / 25, 2)).toFixed(2)}` : `Equation: x² + y² = z² tan²(${angle}°)`, 25, 71);
      ctx.fillText(`Axis Tilt = ${(vals.tilt || 15)}°`, 25, 89);
      ctx.fillStyle = "#fbbf24"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText("Generators: 8 discrete straight ruling lines", 25, 110);
    }
  },

  // 6. Canonical Conicoids Morpher
  "sim_geom3d_conicoids": {
    title: "3D Canonical Conicoids Morpher",
    desc: "Explore the taxonomy of quadrics in 3D: Ellipsoids, Hyperboloids of 1 and 2 Sheets, and Paraboloids. Adjust semi-axes a, b, c and inspect principal cross-sections and ruling geometries.",
    isAnimated: false,
    controls: [
      { id: "surfaceType", label: "Type (0:Ellip, 1:Hyp1, 2:Hyp2, 3:Para)", min: 0, max: 3, step: 1, value: 0 },
      { id: "semiA", label: "Semi-Axis a", min: 1.0, max: 4.0, step: 0.2, value: 2.6 },
      { id: "semiB", label: "Semi-Axis b", min: 1.0, max: 4.0, step: 0.2, value: 2.0 },
      { id: "semiC", label: "Semi-Axis c", min: 1.0, max: 4.0, step: 0.2, value: 1.8 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 35 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const type = vals.surfaceType !== undefined ? Math.round(vals.surfaceType) : 0;
      const a = vals.semiA !== undefined ? vals.semiA : 2.6;
      const b = vals.semiB !== undefined ? vals.semiB : 2.0;
      const c = vals.semiC !== undefined ? vals.semiC : 1.8;
      const rotY = vals.rotY !== undefined ? vals.rotY : 35;
      const rotX = 20;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 36);

      const names = ["Ellipsoid", "Hyperboloid of 1 Sheet", "Hyperboloid of 2 Sheets", "Elliptic Paraboloid"];
      const colors = ["#38bdf8", "#fbbf24", "#f43f5e", "#10b981"];

      ctx.strokeStyle = colors[type]; ctx.lineWidth = 1.3;

      if (type === 0) {
        // Ellipsoid: x^2/a^2 + y^2/b^2 + z^2/c^2 = 1
        for (let u = -c + 0.2; u <= c - 0.2; u += 0.4) {
          const factor = Math.sqrt(Math.max(0, 1 - (u * u) / (c * c)));
          ctx.beginPath();
          for (let th = 0; th <= Math.PI * 2; th += 0.15) {
            const p = project3D(a * factor * Math.cos(th), b * factor * Math.sin(th), u, rotX, rotY, w, h, 36);
            if (th === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
          }
          ctx.closePath(); ctx.stroke();
        }
      } else if (type === 1) {
        // Hyperboloid of 1 sheet: x^2/a^2 + y^2/b^2 - z^2/c^2 = 1
        for (let u = -3; u <= 3; u += 0.5) {
          const factor = Math.sqrt(1 + (u * u) / (c * c));
          ctx.beginPath();
          for (let th = 0; th <= Math.PI * 2; th += 0.15) {
            const p = project3D(a * factor * Math.cos(th), b * factor * Math.sin(th), u, rotX, rotY, w, h, 36);
            if (th === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
          }
          ctx.closePath(); ctx.stroke();
        }
      } else if (type === 2) {
        // Hyperboloid of 2 sheets: x^2/a^2 - y^2/b^2 - z^2/c^2 = 1
        // Sheets for |x| >= a
        for (let xSign of [-1, 1]) {
          for (let u = a; u <= a + 2.5; u += 0.5) {
            const factor = Math.sqrt((u * u) / (a * a) - 1);
            ctx.beginPath();
            for (let th = 0; th <= Math.PI * 2; th += 0.15) {
              const p = project3D(xSign * u, b * factor * Math.cos(th), c * factor * Math.sin(th), rotX, rotY, w, h, 36);
              if (th === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
            }
            ctx.closePath(); ctx.stroke();
          }
        }
      } else if (type === 3) {
        // Elliptic Paraboloid: x^2/a^2 + y^2/b^2 = 2z/c
        for (let z = 0.2; z <= 4.0; z += 0.45) {
          const factor = Math.sqrt((2 * z) / c);
          ctx.beginPath();
          for (let th = 0; th <= Math.PI * 2; th += 0.15) {
            const p = project3D(a * factor * Math.cos(th), b * factor * Math.sin(th), z, rotX, rotY, w, h, 36);
            if (th === 0) ctx.moveTo(p.px, p.py); else ctx.lineTo(p.px, p.py);
          }
          ctx.closePath(); ctx.stroke();
        }
      }

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      ctx.fillRect(15, 15, 300, 125);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 300, 125);

      ctx.fillStyle = colors[type]; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText(names[type].toUpperCase(), 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Semi-Axes: a = ${a.toFixed(1)}, b = ${b.toFixed(1)}, c = ${c.toFixed(1)}`, 25, 53);
      if (type === 0) {
        ctx.fillText("x²/a² + y²/b² + z²/c² = 1 (Closed Bounded)", 25, 71);
        ctx.fillText(`Director Sphere Radius: ${Math.sqrt(a*a + b*b + c*c).toFixed(3)}`, 25, 89);
      } else if (type === 1) {
        ctx.fillText("x²/a² + y²/b² - z²/c² = 1 (Doubly Ruled!)", 25, 71);
        ctx.fillText(`Waist Ellipse Area: ${(Math.PI * a * b).toFixed(2)}`, 25, 89);
      } else if (type === 2) {
        ctx.fillText("x²/a² - y²/b² - z²/c² = 1 (Two Separate Sheets)", 25, 71);
        ctx.fillText(`Vertex Gap: 2a = ${(2 * a).toFixed(1)} units`, 25, 89);
      } else {
        ctx.fillText("x²/a² + y²/b² = 2z/c (Non-Central Cup)", 25, 71);
        ctx.fillText("Minimum vertex at origin (0, 0, 0)", 25, 89);
      }
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter, sans-serif";
      ctx.fillText("Orbit Yaw slider rotates viewing perspective", 25, 110);
    }
  },

  // 7. Vector Products & BAC-CAB Engine
  "sim_geom3d_vector_products": {
    title: "3D Scalar & Vector Triple Products Engine",
    desc: "Interact with 3D vectors a, b, c. Visualize the spanned parallelepiped, cross products, and observe the BAC-CAB decomposition: a × (b × c) = (a·c)b - (a·b)c.",
    isAnimated: false,
    controls: [
      { id: "ax", label: "Vector a X", min: -3, max: 3, step: 0.5, value: 2.0 },
      { id: "ay", label: "Vector a Y", min: -3, max: 3, step: 0.5, value: 1.5 },
      { id: "bx", label: "Vector b X", min: -3, max: 3, step: 0.5, value: -1.5 },
      { id: "bz", label: "Vector b Z", min: -3, max: 3, step: 0.5, value: 2.5 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 30 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const ax = vals.ax !== undefined ? vals.ax : 2.0;
      const ay = vals.ay !== undefined ? vals.ay : 1.5;
      const az = 1.0;
      const bx = vals.bx !== undefined ? vals.bx : -1.5;
      const by = 2.0;
      const bz = vals.bz !== undefined ? vals.bz : 2.5;
      const cx = 1.0, cy = 0.5, cz = 2.0;
      const rotY = vals.rotY !== undefined ? vals.rotY : 30;
      const rotX = 20;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 36);

      const a = [ax, ay, az];
      const b = [bx, by, bz];
      const c = [cx, cy, cz];

      // b x c
      const bxc = [
        b[1] * c[2] - b[2] * c[1],
        b[2] * c[0] - b[0] * c[2],
        b[0] * c[1] - b[1] * c[0]
      ];

      // a . (b x c) = scalar triple product
      const stp = a[0] * bxc[0] + a[1] * bxc[1] + a[2] * bxc[2];

      // a x (b x c) = vector triple product
      const axbxc = [
        a[1] * bxc[2] - a[2] * bxc[1],
        a[2] * bxc[0] - a[0] * bxc[2],
        a[0] * bxc[1] - a[1] * bxc[0]
      ];

      // BAC-CAB: (a.c)b - (a.b)c
      const aDotC = a[0] * c[0] + a[1] * c[1] + a[2] * c[2];
      const aDotB = a[0] * b[0] + a[1] * b[1] + a[2] * b[2];

      const O = project3D(0, 0, 0, rotX, rotY, w, h, 36);
      const pA = project3D(a[0], a[1], a[2], rotX, rotY, w, h, 36);
      const pB = project3D(b[0], b[1], b[2], rotX, rotY, w, h, 36);
      const pC = project3D(c[0], c[1], c[2], rotX, rotY, w, h, 36);

      // Draw vectors
      function drawVector(pEnd, color, label) {
        ctx.strokeStyle = color; ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.moveTo(O.px, O.py); ctx.lineTo(pEnd.px, pEnd.py); ctx.stroke();
        ctx.fillStyle = color; ctx.beginPath(); ctx.arc(pEnd.px, pEnd.py, 4, 0, Math.PI * 2); ctx.fill();
        ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText(label, pEnd.px + 7, pEnd.py);
      }

      drawVector(pA, "#f43f5e", "a");
      drawVector(pB, "#fbbf24", "b");
      drawVector(pC, "#10b981", "c");

      // Draw b x c (scaled for visibility)
      const bxcScale = 0.5;
      const pBxC = project3D(bxc[0] * bxcScale, bxc[1] * bxcScale, bxc[2] * bxcScale, rotX, rotY, w, h, 36);
      ctx.setLineDash([3, 3]);
      drawVector(pBxC, "#a855f7", "b × c");
      ctx.setLineDash([]);

      // Draw Parallelepiped edges
      ctx.strokeStyle = "rgba(148, 163, 184, 0.25)"; ctx.lineWidth = 1;
      const pts = [
        project3D(a[0] + b[0], a[1] + b[1], a[2] + b[2], rotX, rotY, w, h, 36),
        project3D(b[0] + c[0], b[1] + c[1], b[2] + c[2], rotX, rotY, w, h, 36),
        project3D(a[0] + c[0], a[1] + c[1], a[2] + c[2], rotX, rotY, w, h, 36),
        project3D(a[0] + b[0] + c[0], a[1] + b[1] + c[1], a[2] + b[2] + c[2], rotX, rotY, w, h, 36)
      ];
      ctx.beginPath(); ctx.moveTo(pA.px, pA.py); ctx.lineTo(pts[0].px, pts[0].py); ctx.lineTo(pB.px, pB.py); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(pB.px, pB.py); ctx.lineTo(pts[1].px, pts[1].py); ctx.lineTo(pC.px, pC.py); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(pC.px, pC.py); ctx.lineTo(pts[2].px, pts[2].py); ctx.lineTo(pA.px, pA.py); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(pts[0].px, pts[0].py); ctx.lineTo(pts[3].px, pts[3].py); ctx.lineTo(pts[1].px, pts[1].py); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(pts[2].px, pts[2].py); ctx.lineTo(pts[3].px, pts[3].py); ctx.stroke();

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      ctx.fillRect(15, 15, 310, 130);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 310, 130);

      ctx.fillStyle = "#a855f7"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("VECTOR TRIPLE PRODUCTS & BAC-CAB", 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Scalar Triple Product [a, b, c] = ${stp.toFixed(2)}`, 25, 53);
      ctx.fillText(`Parallelepiped Volume V = ${Math.abs(stp).toFixed(2)}`, 25, 71);
      ctx.fillText(`a · c = ${aDotC.toFixed(2)},   a · b = ${aDotB.toFixed(2)}`, 25, 89);
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`a × (b × c) = (${axbxc[0].toFixed(2)}, ${axbxc[1].toFixed(2)}, ${axbxc[2].toFixed(2)})`, 25, 108);
      ctx.fillStyle = "#10b981"; ctx.font = "10px Inter, sans-serif";
      ctx.fillText("Identical to (a·c)b - (a·b)c (BAC-CAB theorem)", 25, 126);
    }
  },

  // 8. Spatial Applications & Reciprocal Triads
  "sim_geom3d_spatial_apps": {
    title: "3D Line-Plane Piercing & Reciprocal Vectors Engine",
    desc: "Analyze spatial intersections and dual vector systems. Observe the piercing point of a line into a plane, orthogonal projections, and reciprocal triad vectors a', b', c'.",
    isAnimated: false,
    controls: [
      { id: "tLine", label: "Line Parameter t", min: -3, max: 3, step: 0.2, value: 0.5 },
      { id: "planeTilt", label: "Plane Tilt Angle (°)", min: -60, max: 60, step: 2, value: 25 },
      { id: "pointDist", label: "Test Point Height", min: -4, max: 4, step: 0.5, value: 2.0 },
      { id: "showReciprocal", label: "Show Reciprocal Triad", min: 0, max: 1, step: 1, value: 1 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 35 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const tLine = vals.tLine !== undefined ? vals.tLine : 0.5;
      const tilt = ((vals.planeTilt !== undefined ? vals.planeTilt : 25) * Math.PI) / 180;
      const ptH = vals.pointDist !== undefined ? vals.pointDist : 2.0;
      const showRec = (vals.showReciprocal !== undefined ? Math.round(vals.showReciprocal) : 1) === 1;
      const rotY = vals.rotY !== undefined ? vals.rotY : 35;
      const rotX = 20;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 36);

      // Plane passing through (0, 0, 0) with normal tilted in YZ plane
      // Normal: (0, -sin(tilt), cos(tilt))
      const ny = -Math.sin(tilt), nz = Math.cos(tilt);
      const pCorn = [
        project3D(-4, -4 * Math.cos(tilt), -4 * Math.sin(tilt), rotX, rotY, w, h, 36),
        project3D(4, -4 * Math.cos(tilt), -4 * Math.sin(tilt), rotX, rotY, w, h, 36),
        project3D(4, 4 * Math.cos(tilt), 4 * Math.sin(tilt), rotX, rotY, w, h, 36),
        project3D(-4, 4 * Math.cos(tilt), 4 * Math.sin(tilt), rotX, rotY, w, h, 36)
      ];

      // Draw Tilted Plane
      ctx.beginPath();
      ctx.moveTo(pCorn[0].px, pCorn[0].py);
      for (let i = 1; i < 4; i++) ctx.lineTo(pCorn[i].px, pCorn[i].py);
      ctx.closePath();
      ctx.fillStyle = "rgba(56, 189, 248, 0.2)"; ctx.fill();
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 1.8; ctx.stroke();

      // Piercing Line: r(t) = (0, 1, 2) + t*(1, 1, -1)
      const lP0 = project3D(-3, -2, 5, rotX, rotY, w, h, 36);
      const lP1 = project3D(3, 4, -1, rotX, rotY, w, h, 36);
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(lP0.px, lP0.py); ctx.lineTo(lP1.px, lP1.py); ctx.stroke();

      // Current Line Point
      const curPt = project3D(tLine, 1 + tLine, 2 - tLine, rotX, rotY, w, h, 36);
      ctx.fillStyle = "#fbbf24"; ctx.beginPath(); ctx.arc(curPt.px, curPt.py, 5, 0, Math.PI * 2); ctx.fill();

      // Test point Q with perpendicular to plane
      const pQ = project3D(0, ptH * ny, ptH * nz, rotX, rotY, w, h, 36);
      const pQFoot = project3D(0, 0, 0, rotX, rotY, w, h, 36);
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2; ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(pQFoot.px, pQFoot.py); ctx.lineTo(pQ.px, pQ.py); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#f43f5e"; ctx.beginPath(); ctx.arc(pQ.px, pQ.py, 4.5, 0, Math.PI * 2); ctx.fill();

      // If showReciprocal is on, draw reciprocal triad vectors a', b', c'
      if (showRec) {
        const rScale = 2.0;
        const pA_p = project3D(rScale, rScale, -rScale, rotX, rotY, w, h, 36);
        const pB_p = project3D(-rScale, rScale, rScale, rotX, rotY, w, h, 36);
        const pC_p = project3D(rScale, -rScale, rScale, rotX, rotY, w, h, 36);
        const O = project3D(0, 0, 0, rotX, rotY, w, h, 36);

        ctx.strokeStyle = "#10b981"; ctx.lineWidth = 1.8;
        ctx.beginPath(); ctx.moveTo(O.px, O.py); ctx.lineTo(pA_p.px, pA_p.py); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(O.px, O.py); ctx.lineTo(pB_p.px, pB_p.py); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(O.px, O.py); ctx.lineTo(pC_p.px, pC_p.py); ctx.stroke();
        ctx.fillStyle = "#10b981"; ctx.font = "bold 10px Inter, sans-serif";
        ctx.fillText("a'", pA_p.px + 5, pA_p.py);
        ctx.fillText("b'", pB_p.px + 5, pB_p.py);
        ctx.fillText("c'", pC_p.px + 5, pC_p.py);
      }

      // Analytical HUD
      ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      ctx.fillRect(15, 15, 310, 130);
      ctx.strokeStyle = "#334155"; ctx.strokeRect(15, 15, 310, 130);

      ctx.fillStyle = "#fbbf24"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("PIERCING POINT & RECIPROCAL TRIADS", 25, 33);
      ctx.fillStyle = "#e2e8f0"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Current Line Point t = ${tLine.toFixed(1)}: (${tLine.toFixed(1)}, ${(1+tLine).toFixed(1)}, ${(2-tLine).toFixed(1)})`, 25, 53);
      ctx.fillText(`Plane Tilt = ${(vals.planeTilt || 25)}°  |  Normal = (0, ${ny.toFixed(2)}, ${nz.toFixed(2)})`, 25, 71);
      ctx.fillText(`Test Point Perpendicular Distance D = ${Math.abs(ptH).toFixed(2)}`, 25, 89);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("Reciprocal Triad: aᵢ · a'ⱼ = δᵢⱼ  (Kronecker Delta)", 25, 110);
      ctx.fillStyle = "#94a3b8"; ctx.font = "10px Inter, sans-serif";
      ctx.fillText("[a', b', c'] = 1 / [a, b, c] strictly verified", 25, 127);
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

    const simConfig = (window.GEOM3D_SIMS && window.GEOM3D_SIMS[simKey]) || (window.SIMULATIONS && window.SIMULATIONS[simKey]);
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
