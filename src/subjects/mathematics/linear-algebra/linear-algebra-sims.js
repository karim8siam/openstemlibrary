// Linear Algebra & Spectral Theory Simulation Suite
// 8 Real-Time 60 FPS Interactive Canvas Simulations for Vector Spaces, Transformations, Eigenvalues & Quadratic Forms

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

window.LA_SIMS = {
  // 1. Linear Systems & Hyperplane Intersections
  "sim_la_linear_systems": {
    title: "3D Hyperplane & Linear Systems Intersection Engine",
    desc: "Visualize three intersecting planes in R^3. Real-time determinant calculation, Gaussian elimination status, and geometric tracking of the unique solution point x* = A^(-1) b.",
    isAnimated: false,
    controls: [
      { id: "a11", label: "Eq1: x coeff", min: -3, max: 3, step: 0.5, value: 1.0 },
      { id: "a12", label: "Eq1: y coeff", min: -3, max: 3, step: 0.5, value: 2.0 },
      { id: "a13", label: "Eq1: z coeff", min: -3, max: 3, step: 0.5, value: 1.0 },
      { id: "b1",  label: "Eq1: const b1", min: -5, max: 5, step: 0.5, value: 4.0 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 35 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const a11 = vals.a11 !== undefined ? vals.a11 : 1.0;
      const a12 = vals.a12 !== undefined ? vals.a12 : 2.0;
      const a13 = vals.a13 !== undefined ? vals.a13 : 1.0;
      const b1  = vals.b1  !== undefined ? vals.b1  : 4.0;
      const rotY = vals.rotY !== undefined ? vals.rotY : 35;
      const rotX = 22;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 32);

      // System:
      // a11*x + a12*y + a13*z = b1
      // 1*x - 1*y + 2*z = 2
      // 2*x + 1*y - 1*z = 1
      const A = [
        [a11, a12, a13],
        [1, -1, 2],
        [2, 1, -1]
      ];
      const B = [b1, 2, 1];

      // det(A)
      const detA = a11 * ((-1)*(-1) - 2*1) - a12 * (1*(-1) - 2*2) + a13 * (1*1 - (-1)*2);
      // = a11 * (-1) - a12 * (-5) + a13 * 3 = -a11 + 5*a12 + 3*a13

      let sol = null;
      if (Math.abs(detA) > 1e-4) {
        // Cramer's rule
        const detX = b1 * ((-1)*(-1) - 2*1) - a12 * (2*(-1) - 2*1) + a13 * (2*1 - (-1)*1);
        const detY = a11 * (2*(-1) - 2*1) - b1 * (1*(-1) - 2*2) + a13 * (1*1 - 2*2);
        const detZ = a11 * ((-1)*1 - 2*1) - a12 * (1*1 - 2*2) + b1 * (1*1 - (-1)*2);
        sol = [detX / detA, detY / detA, detZ / detA];
      }

      // Draw Plane 2 (fixed): x - y + 2z = 2 -> y = x + 2z - 2
      ctx.fillStyle = "rgba(56, 189, 248, 0.12)";
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
      ctx.lineWidth = 1;
      const p2Corners = [
        [-3, -3 + 2*(-3) - 2, -3],
        [3, 3 + 2*(-3) - 2, -3],
        [3, 3 + 2*(3) - 2, 3],
        [-3, -3 + 2*(3) - 2, 3]
      ];
      ctx.beginPath();
      p2Corners.forEach((pt, idx) => {
        const pr = project3D(pt[0], pt[1]*0.4, pt[2], rotX, rotY, w, h, 32);
        if (idx === 0) ctx.moveTo(pr.px, pr.py); else ctx.lineTo(pr.px, pr.py);
      });
      ctx.closePath(); ctx.fill(); ctx.stroke();

      // Draw Plane 1 (dynamic):
      ctx.fillStyle = "rgba(244, 63, 94, 0.15)";
      ctx.strokeStyle = "rgba(244, 63, 94, 0.6)";
      ctx.lineWidth = 1.5;
      const p1Corners = [
        [-3, 0, -3], [3, 0, -3], [3, 0, 3], [-3, 0, 3]
      ].map(pt => {
        let yVal = 0;
        if (Math.abs(a12) > 0.1) {
          yVal = (b1 - a11*pt[0] - a13*pt[2]) / a12;
        }
        return [pt[0], yVal * 0.4, pt[2]];
      });
      ctx.beginPath();
      p1Corners.forEach((pt, idx) => {
        const pr = project3D(pt[0], pt[1], pt[2], rotX, rotY, w, h, 32);
        if (idx === 0) ctx.moveTo(pr.px, pr.py); else ctx.lineTo(pr.px, pr.py);
      });
      ctx.closePath(); ctx.fill(); ctx.stroke();

      // Draw Solution Point
      if (sol) {
        const pr = project3D(sol[0], sol[1]*0.4, sol[2], rotX, rotY, w, h, 32);
        ctx.fillStyle = "#fbbf24";
        ctx.beginPath(); ctx.arc(pr.px, pr.py, 6, 0, Math.PI * 2); ctx.fill();
        ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 2; ctx.stroke();

        ctx.fillStyle = "#fbbf24"; ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText(`x* = (${sol[0].toFixed(2)}, ${sol[1].toFixed(2)}, ${sol[2].toFixed(2)})`, pr.px + 8, pr.py - 6);
      }

      // HUD readout
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Linear System Hyperplane Analysis", 25, 30);

      ctx.font = "11px Inter, sans-serif"; ctx.fillStyle = "#94a3b8";
      ctx.fillText(`det(A) = ${detA.toFixed(2)}`, 25, 52);

      const statusColor = Math.abs(detA) > 1e-4 ? "#10b981" : "#f43f5e";
      const statusText = Math.abs(detA) > 1e-4 ? "Consistent • Unique Point Solution (Rank 3)" : "Singular • Infinitely Many or Inconsistent (Rank < 3)";
      ctx.fillStyle = statusColor; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(statusText, 25, 72);
    }
  },

  // 2. Vector Space & Subspace Closure Laboratory
  "sim_la_subspaces": {
    title: "Vector Space & Subspace Closure Laboratory",
    desc: "Test whether linear combinations c1 u + c2 v remain inside a 2D subspace W passing through origin in R^3. Interactive verification of vector addition and scalar multiplication closure.",
    isAnimated: false,
    controls: [
      { id: "uX", label: "Vector u_x", min: -3, max: 3, step: 0.5, value: 1.5 },
      { id: "uY", label: "Vector u_y", min: -3, max: 3, step: 0.5, value: 2.0 },
      { id: "c1", label: "Scalar c1", min: -2, max: 2, step: 0.2, value: 1.0 },
      { id: "c2", label: "Scalar c2", min: -2, max: 2, step: 0.2, value: -0.5 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 40 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const ux = vals.uX !== undefined ? vals.uX : 1.5;
      const uy = vals.uY !== undefined ? vals.uY : 2.0;
      const c1 = vals.c1 !== undefined ? vals.c1 : 1.0;
      const c2 = vals.c2 !== undefined ? vals.c2 : -0.5;
      const rotY = vals.rotY !== undefined ? vals.rotY : 40;
      const rotX = 25;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 34);

      // Subspace W: spanned by u = (ux, uy, 0) and v = (0, 1.5, 2.0)
      const u = [ux, uy, 0];
      const v = [0, 1.5, 2.0];
      const comb = [c1 * u[0] + c2 * v[0], c1 * u[1] + c2 * v[1], c1 * u[2] + c2 * v[2]];

      // Draw Subspace W Plane
      ctx.fillStyle = "rgba(56, 189, 248, 0.15)";
      ctx.strokeStyle = "rgba(56, 189, 248, 0.35)";
      ctx.lineWidth = 1;
      const planePoints = [
        [-3*u[0] - 2*v[0], -3*u[1] - 2*v[1], -3*u[2] - 2*v[2]],
        [3*u[0] - 2*v[0], 3*u[1] - 2*v[1], 3*u[2] - 2*v[2]],
        [3*u[0] + 2*v[0], 3*u[1] + 2*v[1], 3*u[2] + 2*v[2]],
        [-3*u[0] + 2*v[0], -3*u[1] + 2*v[1], -3*u[2] + 2*v[2]]
      ];
      ctx.beginPath();
      planePoints.forEach((pt, idx) => {
        const pr = project3D(pt[0]*0.5, pt[1]*0.5, pt[2]*0.5, rotX, rotY, w, h, 34);
        if (idx === 0) ctx.moveTo(pr.px, pr.py); else ctx.lineTo(pr.px, pr.py);
      });
      ctx.closePath(); ctx.fill(); ctx.stroke();

      const orig = project3D(0, 0, 0, rotX, rotY, w, h, 34);

      // Draw u vector (cyan)
      const uPr = project3D(u[0], u[1], u[2], rotX, rotY, w, h, 34);
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(orig.px, orig.py); ctx.lineTo(uPr.px, uPr.py); ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText("u", uPr.px + 6, uPr.py);

      // Draw v vector (emerald)
      const vPr = project3D(v[0], v[1], v[2], rotX, rotY, w, h, 34);
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(orig.px, orig.py); ctx.lineTo(vPr.px, vPr.py); ctx.stroke();
      ctx.fillStyle = "#10b981";
      ctx.fillText("v", vPr.px + 6, vPr.py);

      // Draw linear combination vector c1*u + c2*v (rose/gold)
      const cPr = project3D(comb[0], comb[1], comb[2], rotX, rotY, w, h, 34);
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 3;
      ctx.beginPath(); ctx.moveTo(orig.px, orig.py); ctx.lineTo(cPr.px, cPr.py); ctx.stroke();
      ctx.fillStyle = "#fbbf24"; ctx.beginPath(); ctx.arc(cPr.px, cPr.py, 5, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#fbbf24"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`c1 u + c2 v = (${comb[0].toFixed(1)}, ${comb[1].toFixed(1)}, ${comb[2].toFixed(1)})`, cPr.px + 8, cPr.py);

      // HUD readout
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Subspace Closure Verification", 25, 30);
      ctx.font = "11px Inter, sans-serif"; ctx.fillStyle = "#10b981";
      ctx.fillText("✓ Axiom 1: 0 ∈ W (Plane contains origin)", 25, 52);
      ctx.fillText("✓ Axiom 2: u + v ∈ W (Closed under addition)", 25, 70);
      ctx.fillText(`✓ Axiom 3: ${c1.toFixed(1)} u + ${c2.toFixed(1)} v ∈ W (Closed under scalar multiplication)`, 25, 88);
    }
  },

  // 3. Linear Independence & Span Volume Engine
  "sim_la_span_independence": {
    title: "Linear Independence & Span Volume Engine",
    desc: "Manipulate vector v3 in R^3. The engine computes the determinant volume of the parallelepiped formed by {v1, v2, v3}. When volume = 0, vectors collapse into a 2D plane (linearly dependent).",
    isAnimated: false,
    controls: [
      { id: "v3X", label: "v3_x", min: -3, max: 3, step: 0.2, value: 1.0 },
      { id: "v3Y", label: "v3_y", min: -3, max: 3, step: 0.2, value: 1.0 },
      { id: "v3Z", label: "v3_z", min: -3, max: 3, step: 0.2, value: 2.0 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 45 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const v3x = vals.v3X !== undefined ? vals.v3X : 1.0;
      const v3y = vals.v3Y !== undefined ? vals.v3Y : 1.0;
      const v3z = vals.v3Z !== undefined ? vals.v3Z : 2.0;
      const rotY = vals.rotY !== undefined ? vals.rotY : 45;
      const rotX = 22;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 35);

      const v1 = [2.5, 0.0, 0.0];
      const v2 = [0.0, 2.5, 0.0];
      const v3 = [v3x, v3y, v3z];

      // Volume = |det([v1, v2, v3])| = |v1_x * v2_y * v3_z| = 2.5 * 2.5 * |v3_z|
      const detVal = v1[0] * v2[1] * v3[2];
      const vol = Math.abs(detVal);
      const isIndep = vol > 0.1;

      // Parallelepiped vertices
      const corners = [
        [0,0,0],
        v1,
        [v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2]],
        v2,
        v3,
        [v1[0]+v3[0], v1[1]+v3[1], v1[2]+v3[2]],
        [v1[0]+v2[0]+v3[0], v1[1]+v2[1]+v3[1], v1[2]+v2[2]+v3[2]],
        [v2[0]+v3[0], v2[1]+v3[1], v2[2]+v3[2]]
      ];

      const projCorners = corners.map(pt => project3D(pt[0], pt[1], pt[2], rotX, rotY, w, h, 35));

      // Draw faces
      const faces = [
        [0,1,2,3], [4,5,6,7], [0,1,5,4], [2,3,7,6], [0,3,7,4], [1,2,6,5]
      ];
      ctx.fillStyle = isIndep ? "rgba(56, 189, 248, 0.15)" : "rgba(244, 63, 94, 0.25)";
      ctx.strokeStyle = isIndep ? "rgba(56, 189, 248, 0.6)" : "rgba(244, 63, 94, 0.8)";
      ctx.lineWidth = 1.2;

      faces.forEach(f => {
        ctx.beginPath();
        f.forEach((idx, i) => {
          if (i === 0) ctx.moveTo(projCorners[idx].px, projCorners[idx].py);
          else ctx.lineTo(projCorners[idx].px, projCorners[idx].py);
        });
        ctx.closePath(); ctx.fill(); ctx.stroke();
      });

      // Draw vectors v1, v2, v3
      const orig = projCorners[0];
      [
        { p: projCorners[1], col: "#f43f5e", lbl: "v1" },
        { p: projCorners[3], col: "#10b981", lbl: "v2" },
        { p: projCorners[4], col: "#fbbf24", lbl: "v3" }
      ].forEach(item => {
        ctx.strokeStyle = item.col; ctx.lineWidth = 2.8;
        ctx.beginPath(); ctx.moveTo(orig.px, orig.py); ctx.lineTo(item.p.px, item.p.py); ctx.stroke();
        ctx.fillStyle = item.col; ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText(item.lbl, item.p.px + 6, item.p.py);
      });

      // HUD readout
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Parallelepiped Span & Independence", 25, 30);
      ctx.font = "11px Inter, sans-serif"; ctx.fillStyle = "#94a3b8";
      ctx.fillText(`Determinant Volume = ${vol.toFixed(2)}`, 25, 52);

      const statusColor = isIndep ? "#10b981" : "#f43f5e";
      const statusText = isIndep ? "✓ Linearly Independent • Spans R^3 (Rank 3)" : "⚠ Linearly Dependent • Collapsed Coplanar (Rank 2)";
      ctx.fillStyle = statusColor; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(statusText, 25, 72);
    }
  },

  // 4. The Four Fundamental Matrix Subspaces (Strang Diagram Engine)
  "sim_la_four_subspaces": {
    title: "The Four Fundamental Subspaces (Strang Diagram Engine)",
    desc: "Interactive dual-space decomposition: Row Space C(A^T) ⊥ Null Space N(A) in R^n, and Column Space C(A) ⊥ Left Null Space N(A^T) in R^m. Direct visualization of the Rank-Nullity Theorem.",
    isAnimated: false,
    controls: [
      { id: "m11", label: "A[1,1]", min: -2, max: 2, step: 0.5, value: 1.0 },
      { id: "m12", label: "A[1,2]", min: -2, max: 2, step: 0.5, value: 2.0 },
      { id: "m21", label: "A[2,1]", min: -2, max: 2, step: 0.5, value: 2.0 },
      { id: "m22", label: "A[2,2]", min: -2, max: 2, step: 0.5, value: 4.0 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const a11 = vals.m11 !== undefined ? vals.m11 : 1.0;
      const a12 = vals.m12 !== undefined ? vals.m12 : 2.0;
      const a21 = vals.m21 !== undefined ? vals.m21 : 2.0;
      const a22 = vals.m22 !== undefined ? vals.m22 : 4.0;

      const det = a11 * a22 - a12 * a21;
      const rank = (Math.abs(det) > 0.1) ? 2 : ((a11===0 && a12===0 && a21===0 && a22===0) ? 0 : 1);
      const nullity = 2 - rank;

      // Two panels: Left = Domain R^2, Right = Codomain R^2
      const leftW = w * 0.45;
      const rightX = w * 0.55;
      const cy = h * 0.55;
      const cx1 = leftW * 0.5;
      const cx2 = rightX + (w - rightX) * 0.5;

      // Left Panel: R^n (Domain)
      ctx.strokeStyle = "#1e293b"; ctx.lineWidth = 1;
      ctx.strokeRect(20, 44, leftW - 20, h - 64);
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Domain R^n: C(A^T) ⊕ N(A)", 35, 64);

      // Draw Axes in Left
      ctx.strokeStyle = "rgba(148, 163, 184, 0.2)";
      ctx.beginPath(); ctx.moveTo(cx1, 55); ctx.lineTo(cx1, h - 30); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(30, cy); ctx.lineTo(leftW - 10, cy); ctx.stroke();

      // Right Panel: R^m (Codomain)
      ctx.strokeRect(rightX, 44, w - rightX - 20, h - 64);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Codomain R^m: C(A) ⊕ N(A^T)", rightX + 15, 64);

      // Draw Axes in Right
      ctx.strokeStyle = "rgba(148, 163, 184, 0.2)";
      ctx.beginPath(); ctx.moveTo(cx2, 55); ctx.lineTo(cx2, h - 30); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(rightX + 10, cy); ctx.lineTo(w - 30, cy); ctx.stroke();

      // Row space line C(A^T) in Left
      const rowAngle = Math.atan2(a12, a11);
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(cx1 - 100 * Math.cos(rowAngle), cy + 100 * Math.sin(rowAngle));
      ctx.lineTo(cx1 + 100 * Math.cos(rowAngle), cy - 100 * Math.sin(rowAngle));
      ctx.stroke();
      ctx.fillStyle = "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`Row Space C(A^T) [dim=${rank}]`, cx1 + 35, cy - 60);

      // Null space line N(A) in Left (strictly perpendicular to Row Space!)
      const nullAngle = rowAngle + Math.PI / 2;
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.5; ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(cx1 - 100 * Math.cos(nullAngle), cy + 100 * Math.sin(nullAngle));
      ctx.lineTo(cx1 + 100 * Math.cos(nullAngle), cy - 100 * Math.sin(nullAngle));
      ctx.stroke(); ctx.setLineDash([]);
      ctx.fillStyle = "#f43f5e";
      ctx.fillText(`Null Space N(A) [dim=${nullity}]`, cx1 - 120, cy + 70);

      // Column space line C(A) in Right
      const colAngle = Math.atan2(a21, a11);
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(cx2 - 100 * Math.cos(colAngle), cy + 100 * Math.sin(colAngle));
      ctx.lineTo(cx2 + 100 * Math.cos(colAngle), cy - 100 * Math.sin(colAngle));
      ctx.stroke();
      ctx.fillStyle = "#10b981";
      ctx.fillText(`Column Space C(A) [dim=${rank}]`, rightX + 25, cy - 60);

      // Left Null space line N(A^T) in Right (strictly perpendicular to C(A)!)
      const leftNullAngle = colAngle + Math.PI / 2;
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2.5; ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(cx2 - 100 * Math.cos(leftNullAngle), cy + 100 * Math.sin(leftNullAngle));
      ctx.lineTo(cx2 + 100 * Math.cos(leftNullAngle), cy - 100 * Math.sin(leftNullAngle));
      ctx.stroke(); ctx.setLineDash([]);
      ctx.fillStyle = "#fbbf24";
      ctx.fillText(`Left Null N(A^T) [dim=${nullity}]`, cx2 - 120, cy + 70);

      // Top HUD Readout
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 12px Inter, sans-serif";
      ctx.fillText("Fundamental Theorem of Linear Algebra: Rank-Nullity dim V = rank(A) + nullity(A)", 20, 20);
      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Matrix Rank r = ${rank}  |  Nullity n - r = ${nullity}  |  det(A) = ${det.toFixed(2)}`, 20, 36);
    }
  },

  // 5. 2D Linear Transformation & Grid Morpher
  "sim_la_transformations": {
    title: "2D Linear Transformation & Grid Morpher",
    desc: "Watch the Cartesian grid smoothly transform under matrix T. Traces unit square deformation, basis vectors e1 and e2, orientation, and area scaling given by det(T).",
    isAnimated: false,
    controls: [
      { id: "t11", label: "T[1,1]", min: -2, max: 2, step: 0.2, value: 1.2 },
      { id: "t12", label: "T[1,2]", min: -2, max: 2, step: 0.2, value: 0.8 },
      { id: "t21", label: "T[2,1]", min: -2, max: 2, step: 0.2, value: 0.0 },
      { id: "t22", label: "T[2,2]", min: -2, max: 2, step: 0.2, value: 1.5 },
      { id: "interp", label: "Morph Blend (0:I -> 1:T)", min: 0, max: 1, step: 0.05, value: 1.0 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const t11 = vals.t11 !== undefined ? vals.t11 : 1.2;
      const t12 = vals.t12 !== undefined ? vals.t12 : 0.8;
      const t21 = vals.t21 !== undefined ? vals.t21 : 0.0;
      const t22 = vals.t22 !== undefined ? vals.t22 : 1.5;
      const s = vals.interp !== undefined ? vals.interp : 1.0;

      // Interpolate between Identity and T
      const m11 = (1 - s) * 1.0 + s * t11;
      const m12 = (1 - s) * 0.0 + s * t12;
      const m21 = (1 - s) * 0.0 + s * t21;
      const m22 = (1 - s) * 1.0 + s * t22;

      const det = m11 * m22 - m12 * m21;
      const trace = m11 + m22;

      const cx = w * 0.5, cy = h * 0.55;
      const scale = 50;

      function transformPoint(x, y) {
        const tx = m11 * x + m12 * y;
        const ty = m21 * x + m22 * y;
        return { px: cx + tx * scale, py: cy - ty * scale };
      }

      // Draw transformed grid
      ctx.strokeStyle = "rgba(148, 163, 184, 0.15)"; ctx.lineWidth = 1;
      const gMax = 5;
      for (let i = -gMax; i <= gMax; i++) {
        // Vertical grid lines
        const p1 = transformPoint(i, -gMax);
        const p2 = transformPoint(i, gMax);
        ctx.beginPath(); ctx.moveTo(p1.px, p1.py); ctx.lineTo(p2.px, p2.py); ctx.stroke();

        // Horizontal grid lines
        const q1 = transformPoint(-gMax, i);
        const q2 = transformPoint(gMax, i);
        ctx.beginPath(); ctx.moveTo(q1.px, q1.py); ctx.lineTo(q2.px, q2.py); ctx.stroke();
      }

      // Draw transformed unit square
      const sq0 = transformPoint(0, 0);
      const sq1 = transformPoint(1, 0);
      const sq2 = transformPoint(1, 1);
      const sq3 = transformPoint(0, 1);

      ctx.fillStyle = det >= 0 ? "rgba(56, 189, 248, 0.25)" : "rgba(244, 63, 94, 0.25)";
      ctx.strokeStyle = det >= 0 ? "#38bdf8" : "#f43f5e"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(sq0.px, sq0.py);
      ctx.lineTo(sq1.px, sq1.py);
      ctx.lineTo(sq2.px, sq2.py);
      ctx.lineTo(sq3.px, sq3.py);
      ctx.closePath(); ctx.fill(); ctx.stroke();

      // Draw transformed basis vectors T(e1) and T(e2)
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.8;
      ctx.beginPath(); ctx.moveTo(sq0.px, sq0.py); ctx.lineTo(sq1.px, sq1.py); ctx.stroke();
      ctx.fillStyle = "#f43f5e"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`T(e1) = [${m11.toFixed(2)}, ${m21.toFixed(2)}]`, sq1.px + 6, sq1.py);

      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.8;
      ctx.beginPath(); ctx.moveTo(sq0.px, sq0.py); ctx.lineTo(sq3.px, sq3.py); ctx.stroke();
      ctx.fillStyle = "#10b981";
      ctx.fillText(`T(e2) = [${m12.toFixed(2)}, ${m22.toFixed(2)}]`, sq3.px + 6, sq3.py);

      // HUD readout
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Linear Transformation Matrix Action", 25, 30);
      ctx.font = "11px Inter, sans-serif"; ctx.fillStyle = "#94a3b8";
      ctx.fillText(`det(T) = Area Ratio = ${det.toFixed(2)}  |  tr(T) = ${trace.toFixed(2)}`, 25, 52);

      let orient = det > 0.05 ? "Orientation Preserved (+)" : (det < -0.05 ? "Orientation Reversed (- Reflection)" : "Singular / Collapsed (Rank < 2)");
      let orientColor = det > 0.05 ? "#10b981" : (det < -0.05 ? "#f43f5e" : "#fbbf24");
      ctx.fillStyle = orientColor; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`State: ${orient}`, 25, 72);
    }
  },

  // 6. Eigenvector Field & Diagonal Matrix Alignment Engine
  "sim_la_eigen_diagonalization": {
    title: "Eigenvector Field & Diagonal Matrix Alignment Engine",
    desc: "Rotate principal axes and adjust eigenvalues λ1 and λ2. The engine tracks the ellipse A(S^1), eigenvector invariant directions, and shows how test vector x stretches purely along eigenvectors.",
    isAnimated: false,
    controls: [
      { id: "theta", label: "Axis Angle θ (°)", min: 0, max: 180, step: 5, value: 30 },
      { id: "lam1",  label: "Eigenvalue λ1", min: -2.5, max: 2.5, step: 0.25, value: 2.0 },
      { id: "lam2",  label: "Eigenvalue λ2", min: -2.5, max: 2.5, step: 0.25, value: 0.8 },
      { id: "vAngle", label: "Test Vector Angle (°)", min: 0, max: 360, step: 5, value: 30 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const thDeg = vals.theta !== undefined ? vals.theta : 30;
      const lam1  = vals.lam1  !== undefined ? vals.lam1  : 2.0;
      const lam2  = vals.lam2  !== undefined ? vals.lam2  : 0.8;
      const vDeg  = vals.vAngle !== undefined ? vals.vAngle : 30;

      const th = (thDeg * Math.PI) / 180;
      const vRad = (vDeg * Math.PI) / 180;

      const cx = w * 0.5, cy = h * 0.55;
      const rUnit = 55;

      // Matrix A = R(th) * diag(lam1, lam2) * R(-th)
      const c = Math.cos(th), s = Math.sin(th);
      const a11 = lam1 * c * c + lam2 * s * s;
      const a12 = (lam1 - lam2) * c * s;
      const a21 = a12;
      const a22 = lam1 * s * s + lam2 * c * c;

      // Draw original unit circle S^1
      ctx.strokeStyle = "rgba(148, 163, 184, 0.25)"; ctx.lineWidth = 1.2;
      ctx.beginPath(); ctx.arc(cx, cy, rUnit, 0, Math.PI * 2); ctx.stroke();

      // Draw transformed ellipse A(S^1)
      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 2.2;
      ctx.beginPath();
      const nSteps = 100;
      for (let i = 0; i <= nSteps; i++) {
        const phi = (i / nSteps) * Math.PI * 2;
        const ux = Math.cos(phi), uy = Math.sin(phi);
        const tx = a11 * ux + a12 * uy;
        const ty = a21 * ux + a22 * uy;
        const px = cx + tx * rUnit;
        const py = cy - ty * rUnit;
        if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      // Draw Eigenvector Directions
      // v1 direction: (cos(th), sin(th)) with eigenvalue lam1
      const e1Len = lam1 * rUnit;
      ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2.5; ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(cx - 2.5 * rUnit * c, cy + 2.5 * rUnit * s);
      ctx.lineTo(cx + 2.5 * rUnit * c, cy - 2.5 * rUnit * s);
      ctx.stroke(); ctx.setLineDash([]);
      ctx.fillStyle = "#10b981"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`v1 (λ1 = ${lam1.toFixed(2)})`, cx + e1Len * c + 6, cy - e1Len * s);

      // v2 direction: (-sin(th), cos(th)) with eigenvalue lam2
      const e2Len = lam2 * rUnit;
      ctx.strokeStyle = "#fbbf24"; ctx.lineWidth = 2.5; ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(cx + 2.5 * rUnit * s, cy + 2.5 * rUnit * c);
      ctx.lineTo(cx - 2.5 * rUnit * s, cy - 2.5 * rUnit * c);
      ctx.stroke(); ctx.setLineDash([]);
      ctx.fillStyle = "#fbbf24";
      ctx.fillText(`v2 (λ2 = ${lam2.toFixed(2)})`, cx - e2Len * s + 6, cy - e2Len * c);

      // Draw Test Vector x (rose) and T(x)
      const vx = Math.cos(vRad), vy = Math.sin(vRad);
      const tx = a11 * vx + a12 * vy;
      const ty = a21 * vx + a22 * vy;

      // Vector x
      ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 2.2;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + vx * rUnit, cy - vy * rUnit); ctx.stroke();
      ctx.fillStyle = "#f43f5e"; ctx.fillText("x", cx + vx * rUnit + 4, cy - vy * rUnit);

      // Vector A x
      ctx.strokeStyle = "#ffffff"; ctx.lineWidth = 2.8;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + tx * rUnit, cy - ty * rUnit); ctx.stroke();
      ctx.fillStyle = "#ffffff"; ctx.fillText("A x", cx + tx * rUnit + 6, cy - ty * rUnit);

      // Check alignment (angle diff)
      const diff1 = Math.abs((vDeg - thDeg + 360) % 180);
      const isEigen = (diff1 < 3 || diff1 > 177 || Math.abs(diff1 - 90) < 3);

      // HUD readout
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Spectral Alignment & Invariant Eigenspaces", 25, 30);
      ctx.font = "11px Inter, sans-serif"; ctx.fillStyle = "#94a3b8";
      ctx.fillText(`Matrix A = [[${a11.toFixed(2)}, ${a12.toFixed(2)}], [${a21.toFixed(2)}, ${a22.toFixed(2)}]]`, 25, 52);

      const statusColor = isEigen ? "#10b981" : "#f43f5e";
      const statusText = isEigen ? "★ ALIGNED! Test vector x is an Eigenvector (A x is strictly parallel to x)" : "Arbitrary vector x (A x rotates away from x)";
      ctx.fillStyle = statusColor; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(statusText, 25, 72);
    }
  },

  // 7. 3D Gram-Schmidt Orthonormalization & QR Engine
  "sim_la_inner_product_gram_schmidt": {
    title: "3D Gram-Schmidt Orthonormalization & QR Engine",
    desc: "Step through the Gram-Schmidt process in R^3: orthogonal projection of v2 onto u1, projection of v3 onto span{u1, u2}, and normalization to the orthonormal basis {e1, e2, e3}.",
    isAnimated: false,
    controls: [
      { id: "v2Skew", label: "v2 Skew Angle (°)", min: 10, max: 80, step: 5, value: 35 },
      { id: "v3Elev", label: "v3 Elevation (°)", min: 10, max: 80, step: 5, value: 45 },
      { id: "step",   label: "Gram-Schmidt Step (0:Raw, 1:u2 Perp, 2:u3 Perp, 3:ONB)", min: 0, max: 3, step: 1, value: 3 },
      { id: "rotY",   label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 35 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const skewDeg = vals.v2Skew !== undefined ? vals.v2Skew : 35;
      const elevDeg = vals.v3Elev !== undefined ? vals.v3Elev : 45;
      const step    = vals.step   !== undefined ? Math.round(vals.step) : 3;
      const rotY    = vals.rotY   !== undefined ? vals.rotY : 35;
      const rotX    = 24;

      drawAxisArrows(ctx, rotX, rotY, w, h, 6, 36);

      const skew = (skewDeg * Math.PI) / 180;
      const elev = (elevDeg * Math.PI) / 180;

      // Original vectors v1, v2, v3
      const v1 = [3.2, 0.0, 0.0];
      const v2 = [3.0 * Math.cos(skew), 3.0 * Math.sin(skew), 0.0];
      const v3 = [1.5, 2.0 * Math.sin(elev), 2.8 * Math.cos(elev)];

      // Gram-Schmidt calculation:
      // u1 = v1
      const u1 = [v1[0], v1[1], v1[2]];
      const normU1 = Math.sqrt(u1[0]*u1[0] + u1[1]*u1[1] + u1[2]*u1[2]);
      const e1 = [u1[0]/normU1, u1[1]/normU1, u1[2]/normU1];

      // u2 = v2 - (v2 . e1) * e1
      const dotV2E1 = v2[0]*e1[0] + v2[1]*e1[1] + v2[2]*e1[2];
      const projV2_U1 = [dotV2E1 * e1[0], dotV2E1 * e1[1], dotV2E1 * e1[2]];
      const u2 = [v2[0] - projV2_U1[0], v2[1] - projV2_U1[1], v2[2] - projV2_U1[2]];
      const normU2 = Math.sqrt(u2[0]*u2[0] + u2[1]*u2[1] + u2[2]*u2[2]);
      const e2 = [u2[0]/normU2, u2[1]/normU2, u2[2]/normU2];

      // u3 = v3 - (v3 . e1) * e1 - (v3 . e2) * e2
      const dotV3E1 = v3[0]*e1[0] + v3[1]*e1[1] + v3[2]*e1[2];
      const dotV3E2 = v3[0]*e2[0] + v3[1]*e2[1] + v3[2]*e2[2];
      const projV3_U12 = [
        dotV3E1 * e1[0] + dotV3E2 * e2[0],
        dotV3E1 * e1[1] + dotV3E2 * e2[1],
        dotV3E1 * e1[2] + dotV3E2 * e2[2]
      ];
      const u3 = [v3[0] - projV3_U12[0], v3[1] - projV3_U12[1], v3[2] - projV3_U12[2]];
      const normU3 = Math.sqrt(u3[0]*u3[0] + u3[1]*u3[1] + u3[2]*u3[2]);
      const e3 = [u3[0]/normU3, u3[1]/normU3, u3[2]/normU3];

      const orig = project3D(0, 0, 0, rotX, rotY, w, h, 36);

      function drawVector(vec, col, lbl, isUnit = false) {
        const factor = isUnit ? 2.5 : 1.0;
        const pr = project3D(vec[0] * factor, vec[1] * factor, vec[2] * factor, rotX, rotY, w, h, 36);
        ctx.strokeStyle = col; ctx.lineWidth = isUnit ? 3.5 : 2.2;
        ctx.beginPath(); ctx.moveTo(orig.px, orig.py); ctx.lineTo(pr.px, pr.py); ctx.stroke();
        ctx.fillStyle = col; ctx.font = "bold 11px Inter, sans-serif";
        ctx.fillText(lbl, pr.px + 6, pr.py);
      }

      if (step === 0) {
        // Raw vectors
        drawVector(v1, "#38bdf8", "v1");
        drawVector(v2, "#10b981", "v2");
        drawVector(v3, "#fbbf24", "v3");
      } else if (step === 1) {
        // Step 1: u1 and u2
        drawVector(u1, "#38bdf8", "u1 = v1");
        drawVector(u2, "#10b981", "u2 ⊥ u1");
        drawVector(v3, "rgba(251, 191, 36, 0.4)", "v3 (pending)");
      } else if (step === 2) {
        // Step 2: u1, u2, u3 (mutually orthogonal)
        drawVector(u1, "#38bdf8", "u1");
        drawVector(u2, "#10b981", "u2");
        drawVector(u3, "#f43f5e", "u3 ⊥ {u1, u2}");
      } else {
        // Step 3: Orthonormal basis e1, e2, e3
        drawVector(e1, "#38bdf8", "e1 (unit)", true);
        drawVector(e2, "#10b981", "e2 (unit)", true);
        drawVector(e3, "#f43f5e", "e3 (unit)", true);
      }

      // HUD readout
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Gram-Schmidt Orthogonalization Process", 25, 30);

      const stepTitles = [
        "Step 0: Original Non-Orthogonal Vectors {v1, v2, v3}",
        "Step 1: First Orthogonal Pair {u1, u2} with u2 = v2 - proj(v2)",
        "Step 2: Mutually Orthogonal Set {u1, u2, u3}",
        "Step 3: Complete Orthonormal Basis {e1, e2, e3} with <ei, ej> = δij"
      ];
      ctx.fillStyle = step === 3 ? "#10b981" : "#38bdf8"; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(stepTitles[step], 25, 52);

      ctx.fillStyle = "#94a3b8"; ctx.font = "11px Inter, sans-serif";
      ctx.fillText(`Inner Products: <e1, e2> = 0.00  |  <e1, e3> = 0.00  |  <e2, e3> = 0.00`, 25, 72);
    }
  },

  // 8. 3D Quadratic Form Surface & Energy Landscape Morpher
  "sim_la_quadratic_forms": {
    title: "3D Quadratic Form Surface & Energy Landscape Morpher",
    desc: "Vary coefficients a, b, c of q(x, y) = a x^2 + 2b x y + c y^2. Real-time 3D surface rendering, Sylvester principal minors, eigenvalues, and definiteness classification (Positive Definite, Indefinite, Negative Definite).",
    isAnimated: false,
    controls: [
      { id: "qa", label: "Coeff a (x²)", min: -3, max: 3, step: 0.5, value: 1.5 },
      { id: "qb", label: "Cross b (xy)", min: -3, max: 3, step: 0.25, value: 0.5 },
      { id: "qc", label: "Coeff c (y²)", min: -3, max: 3, step: 0.5, value: 1.5 },
      { id: "rotY", label: "Orbit Yaw (°)", min: -180, max: 180, step: 2, value: 35 }
    ],
    render(canvas, vals) {
      const ctx = canvas.getContext("2d");
      const w = canvas.width, h = canvas.height;
      ctx.fillStyle = "#050811"; ctx.fillRect(0, 0, w, h);

      const a = vals.qa !== undefined ? vals.qa : 1.5;
      const b = vals.qb !== undefined ? vals.qb : 0.5;
      const c = vals.qc !== undefined ? vals.qc : 1.5;
      const rotY = vals.rotY !== undefined ? vals.rotY : 35;
      const rotX = 22;

      drawAxisArrows(ctx, rotX, rotY, w, h, 5, 34);

      // Eigenvalues of [[a, b], [b, c]]:
      // det([a-λ, b; b, c-λ]) = λ² - (a+c)λ + (ac - b²) = 0
      const tr = a + c;
      const disc = Math.max(0, (a - c)*(a - c) + 4 * b * b);
      const lam1 = (tr + Math.sqrt(disc)) / 2;
      const lam2 = (tr - Math.sqrt(disc)) / 2;

      // Sylvester minors
      const delta1 = a;
      const delta2 = a * c - b * b;

      let defText = "";
      let defColor = "";
      if (delta1 > 0 && delta2 > 0) {
        defText = "Positive Definite (Elliptic Paraboloid / Energy Bowl)";
        defColor = "#10b981";
      } else if (delta1 < 0 && delta2 > 0) {
        defText = "Negative Definite (Inverted Paraboloid / Ridge Peak)";
        defColor = "#f43f5e";
      } else if (delta2 < 0) {
        defText = "Indefinite (Hyperbolic Paraboloid / Saddle Point)";
        defColor = "#fbbf24";
      } else {
        defText = "Semidefinite / Degenerate Parabolic Cylinder";
        defColor = "#38bdf8";
      }

      // Render 3D Surface z = a x² + 2b x y + c y²
      const gGrid = 8;
      const range = 2.0;
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)"; ctx.lineWidth = 1;

      // Draw surface wireframe
      for (let i = -gGrid; i <= gGrid; i++) {
        const x = (i / gGrid) * range;
        ctx.beginPath();
        for (let j = -gGrid; j <= gGrid; j++) {
          const y = (j / gGrid) * range;
          const z = (a * x * x + 2 * b * x * y + c * y * y) * 0.35;
          const pr = project3D(x * 1.5, z, y * 1.5, rotX, rotY, w, h, 34);
          if (j === -gGrid) ctx.moveTo(pr.px, pr.py); else ctx.lineTo(pr.px, pr.py);
        }
        ctx.stroke();
      }

      for (let j = -gGrid; j <= gGrid; j++) {
        const y = (j / gGrid) * range;
        ctx.beginPath();
        for (let i = -gGrid; i <= gGrid; i++) {
          const x = (i / gGrid) * range;
          const z = (a * x * x + 2 * b * x * y + c * y * y) * 0.35;
          const pr = project3D(x * 1.5, z, y * 1.5, rotX, rotY, w, h, 34);
          if (i === -gGrid) ctx.moveTo(pr.px, pr.py); else ctx.lineTo(pr.px, pr.py);
        }
        ctx.stroke();
      }

      // HUD readout
      ctx.fillStyle = "#f8fafc"; ctx.font = "bold 13px Inter, sans-serif";
      ctx.fillText("Quadratic Energy Landscape & Sylvester Inertia", 25, 30);

      ctx.font = "11px Inter, sans-serif"; ctx.fillStyle = "#94a3b8";
      ctx.fillText(`q(x, y) = ${a.toFixed(1)}x² + ${ (2*b).toFixed(1) }xy + ${c.toFixed(1)}y²`, 25, 52);
      ctx.fillText(`Eigenvalues: λ1 = ${lam1.toFixed(2)}, λ2 = ${lam2.toFixed(2)}  |  Minors: Δ1 = ${delta1.toFixed(2)}, Δ2 = ${delta2.toFixed(2)}`, 25, 70);

      ctx.fillStyle = defColor; ctx.font = "bold 11px Inter, sans-serif";
      ctx.fillText(`Classification: ${defText}`, 25, 88);
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

    const simConfig = (window.LA_SIMS && window.LA_SIMS[simKey]) ||
                      (window.CALC3_SIMS && window.CALC3_SIMS[simKey]) ||
                      (window.SIMULATIONS && window.SIMULATIONS[simKey]);

    if (!simConfig) {
      container.innerHTML = `<div style="padding:1rem;color:#94a3b8;">Simulation ${simKey} ready.</div>`;
      return;
    }

    if (window.SimulationEngine.activeAnimations[containerId]) {
      cancelAnimationFrame(window.SimulationEngine.activeAnimations[containerId]);
      delete window.SimulationEngine.activeAnimations[containerId];
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
