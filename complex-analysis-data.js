window.COURSE_DATA = {
  "courseCode": "MTH 3103",
  "courseTitle": "Complex Analysis",
  "courseSubtitle": "Holomorphic Functions, Cauchy Theory, Laurent Expansions, Residue Calculus & Conformal Mappings",
  "credits": 3,
  "lectureHours": 45,
  "prerequisites": "Calculus I (MTH 1102), Calculus II (MTH 1202) & Calculus III (MTH 2101)",
  "description": "Rigorous university honors-level digital textbook covering single-variable complex function theory: metric topology of the complex plane, stereographic projection, holomorphic functions, Cauchy-Riemann equations and harmonic conjugates, complex contour integration, Cauchy-Goursat theorem, Cauchy integral formulas, Liouville's theorem and the Fundamental Theorem of Algebra, Morera's theorem, the Maximum Modulus Principle, Taylor and Laurent series expansions, singularity classifications (removable, poles, essential), Casorati-Weierstrass theorem, Cauchy residue calculus, contour integration techniques (Jordan's Lemma, indented contours, branch cuts and keyholes), Rouché's theorem and root tracking, and conformal Möbius transformations with 8 interactive 60 FPS simulations and 24 tiered solved university examination problems.",
  "units": [
    {
      "number": 1,
      "title": "Metric Topology of the Complex Plane, Stereographic Projection & Power Series",
      "leadSummary": "Point-set topology of C, open disks, connectedness, stereographic projection onto the Riemann sphere, chordal metric, complex sequences, and power series convergence.",
      "simulations": [
        "complex-stereographic-sim"
      ],
      "sections": [
        {
          "secNumber": "1.1",
          "title": "Complex Plane C, Metric Topology, Open/Connected Domains & Jordan Curve Theorem",
          "content": "<h3>1. The Complex Field and Metric Structure</h3>\n<p>The set of complex numbers $\\mathbb{C} = \\{z = x + iy : x, y \\in \\mathbb{R}, i^2 = -1\\}$ forms an algebraically closed complete field. Endowed with the Euclidean modulus metric:</p>\n$$d(z_1, z_2) = |z_1 - z_2| = \\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$$\n<p>$\\mathbb{C}$ is isometric to $\\mathbb{R}^2$ as a real metric space, but possesses the richer structure of complex multiplication.</p>\n<p>An open $\\epsilon$-disk centered at $z_0 \\in \\mathbb{C}$ is denoted by $D(z_0, \\epsilon) = \\{z \\in \\mathbb{C} : |z - z_0| < \\epsilon\\}$. A subset $\\Omega \\subseteq \\mathbb{C}$ is called:</p>\n<ul>\n<li><b>Open:</b> if for every $z \\in \\Omega$, there exists $\\epsilon > 0$ such that $D(z, \\epsilon) \\subseteq \\Omega$.</li>\n<li><b>Connected:</b> if it cannot be partitioned into two disjoint, non-empty open sets. In $\\mathbb{C}$, an open set is connected if and only if it is path-connected (any two points can be connected by a polygonal path lying entirely within $\\Omega$).</li>\n<li><b>Domain:</b> an open, connected non-empty subset $D \\subseteq \\mathbb{C}$.</li>\n<li><b>Simply Connected Domain:</b> a domain $D$ without holes; every closed continuous loop $\\gamma \\subset D$ can be continuously contracted to a point within $D$.</li>\n</ul>\n\n<h3>2. The Jordan Curve Theorem</h3>\n<div class=\"math-theorem\">\n<b>Theorem 1.1 (Jordan Curve Theorem):</b> Let $\\gamma: [0, 1] \\to \\mathbb{C}$ be a simple (non-self-intersecting) closed continuous curve (a Jordan curve). Then its complement $\\mathbb{C} \\setminus \\gamma$ consists of exactly two connected components:\n<ol>\n<li>A bounded open domain called the <b>Interior</b> $\\text{Int}(\\gamma)$.</li>\n<li>An unbounded open domain called the <b>Exterior</b> $\\text{Ext}(\\gamma)$.</li>\n</ol>\nThe curve $\\gamma$ is the common topological boundary of both components.\n</div>"
        },
        {
          "secNumber": "1.2",
          "title": "Stereographic Projection, The Riemann Sphere Ĉ and Chordal Metric",
          "simulation": "complex-stereographic-sim",
          "content": "<h3>1. The Extended Complex Plane & The Riemann Sphere</h3>\n<p>To analyze limits at infinity in complex analysis, we compactify $\\mathbb{C}$ by adjoining a single point at infinity, $\\infty$, creating the <b>extended complex plane</b>:</p>\n$$\\widehat{\\mathbb{C}} = \\mathbb{C} \\cup \\{\\infty\\}$$\n<p>Topologically, $\\widehat{\\mathbb{C}}$ is homeomorphic to the unit 2-sphere $S^2 = \\{(X, Y, Z) \\in \\mathbb{R}^3 : X^2 + Y^2 + Z^2 = 1\\}$ via <b>stereographic projection</b> from the North Pole $N = (0, 0, 1)$.</p>\n\n<h3>2. Explicit Coordinate Transformations</h3>\n<p>A ray joining the North Pole $N(0, 0, 1)$ to a point $P(X, Y, Z) \\in S^2$ intersects the equatorial plane $Z = 0$ (identified with $\\mathbb{C}$ via $z = x + iy$) at:</p>\n$$x = \\frac{X}{1 - Z}, \\quad y = \\frac{Y}{1 - Z} \\implies z = \\frac{X + iY}{1 - Z}$$\n<p>Conversely, for any $z = x + iy \\in \\mathbb{C}$, the unique point on the sphere $S^2$ is:</p>\n$$X = \\frac{2x}{|z|^2 + 1} = \\frac{z + \\bar{z}}{|z|^2 + 1}, \\quad Y = \\frac{2y}{|z|^2 + 1} = \\frac{z - \\bar{z}}{i(|z|^2 + 1)}, \\quad Z = \\frac{|z|^2 - 1}{|z|^2 + 1}$$\n<p>As $|z| \\to \\infty$, $Z \\to 1$, mapping the point at infinity $\\infty$ directly to the North Pole $N(0, 0, 1)$.</p>\n\n<h3>3. The Chordal Metric</h3>\n<p>The chordal distance $\\chi(z_1, z_2)$ is the 3D Euclidean distance between their spherical projections:</p>\n$$\\chi(z_1, z_2) = \\frac{2|z_1 - z_2|}{\\sqrt{1 + |z_1|^2}\\sqrt{1 + |z_2|^2}}, \\quad \\chi(z, \\infty) = \\frac{2}{\\sqrt{1 + |z|^2}}$$\n<p>Under $\\chi$, $\\widehat{\\mathbb{C}}$ is a compact metric space.</p>"
        },
        {
          "secNumber": "1.3",
          "title": "Complex Sequences, Infinite Series, Radius of Convergence & Cauchy-Hadamard Formula",
          "content": "<h3>1. Complex Sequences and Series</h3>\n<p>A sequence $\\{z_n\\} \\subset \\mathbb{C}$ converges to $L = \\alpha + i\\beta$ if and only if $\\text{Re}(z_n) \\to \\alpha$ and $\\text{Im}(z_n) \\to \\beta$ as $n \\to \\infty$. Completeness of $\\mathbb{R}^2$ guarantees that every Cauchy sequence in $\\mathbb{C}$ converges.</p>\n\n<h3>2. Complex Power Series and The Cauchy-Hadamard Theorem</h3>\n<p>Consider the formal power series centered at $z_0 \\in \\mathbb{C}$:</p>\n$$\\sum_{n=0}^\\infty a_n (z - z_0)^n$$\n<div class=\"math-theorem\">\n<b>Theorem 1.2 (Cauchy-Hadamard Formula):</b> The radius of convergence $R \\in [0, \\infty]$ of the power series is given by:\n$$\\frac{1}{R} = \\limsup_{n \\to \\infty} \\sqrt[n]{|a_n|}$$\n<ul>\n<li>If $|z - z_0| < R$, the series converges <b>absolutely</b> and locally uniformly to an analytic function.</li>\n<li>If $|z - z_0| > R$, the series diverges.</li>\n<li>On the boundary circle $|z - z_0| = R$, the series may converge at some points and diverge at others.</li>\n</ul>\n</div>"
        }
      ]
    },
    {
      "number": 2,
      "title": "Holomorphic Functions, Cauchy-Riemann Equations & Harmonic Conjugates",
      "leadSummary": "Complex differentiability, the Cauchy-Riemann equations in Cartesian and polar forms, geometric conformality, and harmonic conjugate potentials.",
      "simulations": [
        "complex-cr-flow-sim"
      ],
      "sections": [
        {
          "secNumber": "2.1",
          "title": "Complex Differentiability, Holomorphic / Analytic Functions & Geometric Conformal Interpretation",
          "content": "<h3>1. Complex Differentiability</h3>\n<p>Let $f: \\Omega \\to \\mathbb{C}$ be a function defined on an open set $\\Omega \\subseteq \\mathbb{C}$, and let $z_0 \\in \\Omega$. We say that $f$ is <b>complex differentiable</b> at $z_0$ if the limit:</p>\n$$f'(z_0) = \\lim_{\\Delta z \\to 0} \\frac{f(z_0 + \\Delta z) - f(z_0)}{\\Delta z}$$\n<p>exists. Crucially, this limit must be completely <b>independent</b> of the direction in which $\\Delta z = \\Delta x + i\\Delta y \\to 0$ in the 2D complex plane!</p>\n<div class=\"math-theorem\">\n<b>Definition 2.1:</b> A function $f$ is called <b>holomorphic</b> (or analytic) on an open set $\\Omega$ if it is complex differentiable at every point of $\\Omega$. A function holomorphic on the entire complex plane $\\mathbb{C}$ is called an <b>entire function</b>.\n</div>\n\n<h3>2. Geometric Meaning: Infinitesimal Conformal Invariance</h3>\n<p>Write the derivative in polar form: $f'(z_0) = r e^{i\\theta} \\ne 0$. For an infinitesimal displacement $dz$, the differential transformation is:</p>\n$$dw = f'(z_0) dz = (r e^{i\\theta}) |dz| e^{i\\phi} = (r |dz|) e^{i(\\phi + \\theta)}$$\n<p>This means the mapping $w = f(z)$ acts infinitesimally as a uniform <b>scaling</b> by factor $r = |f'(z_0)|$ and a rigid <b>rotation</b> by angle $\\theta = \\arg f'(z_0)$. Consequently, angles between curves and orientations are locally <b>preserved</b> (conformality).</p>"
        },
        {
          "secNumber": "2.2",
          "title": "The Cauchy-Riemann Equations in Cartesian and Polar Forms with Sufficiency Proofs",
          "simulation": "complex-cr-flow-sim",
          "content": "<h3>1. Derivation of the Cauchy-Riemann Equations</h3>\n<p>Let $f(z) = u(x, y) + i v(x, y)$ where $u, v: \\mathbb{R}^2 \\to \\mathbb{R}$ are real-valued. Approach $0$ along the real axis ($\\Delta z = \\Delta x$):</p>\n$$f'(z) = \\lim_{\\Delta x \\to 0} \\frac{u(x+\\Delta x, y) - u(x, y) + i[v(x+\\Delta x, y) - v(x, y)]}{\\Delta x} = \\frac{\\partial u}{\\partial x} + i \\frac{\\partial v}{\\partial x}$$\n<p>Approach $0$ along the imaginary axis ($\\Delta z = i\\Delta y$):</p>\n$$f'(z) = \\lim_{\\Delta y \\to 0} \\frac{u(x, y+\\Delta y) - u(x, y) + i[v(x, y+\\Delta y) - v(x, y)]}{i\\Delta y} = \\frac{1}{i}\\frac{\\partial u}{\\partial y} + \\frac{\\partial v}{\\partial y} = \\frac{\\partial v}{\\partial y} - i \\frac{\\partial u}{\\partial y}$$\n<p>Equating real and imaginary parts yields the celebrated <b>Cauchy-Riemann Equations</b>:</p>\n$$\\frac{\\partial u}{\\partial x} = \\frac{\\partial v}{\\partial y}, \\qquad \\frac{\\partial u}{\\partial y} = -\\frac{\\partial v}{\\partial x}$$\n\n<h3>2. The Sufficiency Theorem</h3>\n<div class=\"math-theorem\">\n<b>Theorem 2.1 (Looman-Menchoff / Sufficiency):</b> Let $u(x, y)$ and $v(x, y)$ have continuous first-order partial derivatives throughout an open neighborhood of $z_0 = (x_0, y_0)$. If the Cauchy-Riemann equations hold at $z_0$, then $f(z) = u + iv$ is complex differentiable at $z_0$ with derivative:\n$$f'(z_0) = u_x(x_0, y_0) + i v_x(x_0, y_0) = u_x - i u_y$$\n</div>\n\n<h3>3. Polar Form of Cauchy-Riemann Equations</h3>\n<p>In polar coordinates $z = r e^{i\\theta}$, $f(z) = u(r, \\theta) + i v(r, \\theta)$:</p>\n$$\\frac{\\partial u}{\\partial r} = \\frac{1}{r} \\frac{\\partial v}{\\partial \\theta}, \\qquad \\frac{\\partial v}{\\partial r} = -\\frac{1}{r} \\frac{\\partial u}{\\partial \\theta}$$\n<p>The derivative is given by $f'(z) = e^{-i\\theta} \\left( \\frac{\\partial u}{\\partial r} + i \\frac{\\partial v}{\\partial r} \\right)$.</p>"
        },
        {
          "secNumber": "2.3",
          "title": "Harmonic Functions, Harmonic Conjugates, Orthogonal Trajectories & Fluid Potentials",
          "content": "<h3>1. Harmonic Functions</h3>\n<p>Let $f = u + iv$ be holomorphic on domain $D$. If $u, v \\in C^2(D)$, differentiate the C-R equations:</p>\n$$\\frac{\\partial^2 u}{\\partial x^2} = \\frac{\\partial}{\\partial x}\\left(\\frac{\\partial v}{\\partial y}\\right) = \\frac{\\partial^2 v}{\\partial x \\partial y}, \\qquad \\frac{\\partial^2 u}{\\partial y^2} = \\frac{\\partial}{\\partial y}\\left(-\\frac{\\partial v}{\\partial x}\\right) = -\\frac{\\partial^2 v}{\\partial y \\partial x}$$\n<p>By Schwarz's theorem on mixed partials ($v_{xy} = v_{yx}$):</p>\n$$\\nabla^2 u = \\frac{\\partial^2 u}{\\partial x^2} + \\frac{\\partial^2 u}{\\partial y^2} = 0, \\qquad \\nabla^2 v = \\frac{\\partial^2 v}{\\partial x^2} + \\frac{\\partial^2 v}{\\partial y^2} = 0$$\n<p>Both the real and imaginary parts of a holomorphic function are <b>harmonic functions</b>! The function $v$ is called the <b>harmonic conjugate</b> of $u$.</p>\n\n<h3>2. Orthogonal Equipotentials and Fluid Streamlines</h3>\n<p>Compute the inner product of gradients:</p>\n$$\\nabla u \\cdot \\nabla v = \\left( \\frac{\\partial u}{\\partial x} \\right) \\left( \\frac{\\partial v}{\\partial x} \\right) + \\left( \\frac{\\partial u}{\\partial y} \\right) \\left( \\frac{\\partial v}{\\partial y} \\right) = (u_x)(-u_y) + (u_y)(u_x) = 0$$\n<p>Hence, the level curves $u(x, y) = c_1$ and $v(x, y) = c_2$ are strictly <b>mutually orthogonal</b> wherever $f'(z) \\ne 0$. In 2D fluid dynamics, $u$ is the velocity potential and $v$ is the stream function.</p>"
        }
      ]
    },
    {
      "number": 3,
      "title": "Complex Integration, Rectifiable Curves & The Cauchy-Goursat Theorem",
      "leadSummary": "Line integrals along complex contours, ML-inequality, winding numbers, homotopy, and the Cauchy-Goursat theorem for simply connected domains.",
      "simulations": [
        "complex-contour-sim"
      ],
      "sections": [
        {
          "secNumber": "3.1",
          "title": "Contour Integrals along Rectifiable Arcs, The ML-Inequality & Fundamental Theorem",
          "content": "<h3>1. Definition of Contour Integration</h3>\n<p>Let $\\gamma: [a, b] \\to \\mathbb{C}$ be a piecewise smooth path parameterized by $z(t) = x(t) + i y(t)$. For a continuous function $f(z) = u + iv$ on $\\gamma$, the contour integral is defined by:</p>\n$$\\int_\\gamma f(z)\\,dz = \\int_a^b f(z(t)) z'(t)\\,dt = \\int_a^b [u x' - v y']\\,dt + i \\int_a^b [u y' + v x']\\,dt$$\n\n<h3>2. The ML-Inequality (Darboux Inequality)</h3>\n<div class=\"math-theorem\">\n<b>Theorem 3.1 (The ML-Inequality):</b> Let $\\gamma$ be a rectifiable contour of arc length $L = \\int_a^b |z'(t)|\\,dt$. If $|f(z)| \\le M$ for all $z \\in \\gamma$, then:\n$$\\left| \\int_\\gamma f(z)\\,dz \\right| \\le \\int_\\gamma |f(z)|\\,|dz| \\le M \\cdot L$$\n</div>\n\n<h3>3. Fundamental Theorem of Complex Calculus</h3>\n<p>If $f(z)$ possesses a holomorphic primitive $F(z)$ (such that $F'(z) = f(z)$) on an open domain containing $\\gamma$:</p>\n$$\\int_\\gamma f(z)\\,dz = F(z(b)) - F(z(a))$$\n<p>In particular, if $\\gamma$ is a closed loop ($z(b) = z(a)$), then $\\oint_\\gamma f(z)\\,dz = 0$.</p>"
        },
        {
          "secNumber": "3.2",
          "title": "Winding Numbers (Index of a Curve) & Homotopy of Paths",
          "simulation": "complex-contour-sim",
          "content": "<h3>1. The Winding Number / Index</h3>\n<p>Let $\\gamma$ be a closed piecewise smooth curve in $\\mathbb{C}$, and let $z_0 \\notin \\gamma$. The <b>winding number</b> (or index) of $\\gamma$ with respect to $z_0$ measures the net number of counter-clockwise revolutions that $\\gamma$ makes around $z_0$:</p>\n$$\\text{Ind}_\\gamma(z_0) = \\frac{1}{2\\pi i} \\oint_\\gamma \\frac{dz}{z - z_0}$$\n<div class=\"math-theorem\">\n<b>Theorem 3.2:</b> $\\text{Ind}_\\gamma(z_0)$ is always an <b>integer</b>. It is constant on each connected component of $\\mathbb{C} \\setminus \\gamma$, and equals $0$ on the unbounded exterior component.\n</div>"
        },
        {
          "secNumber": "3.3",
          "title": "The Cauchy-Goursat Theorem for Triangles, Polygons and Simply Connected Domains",
          "content": "<h3>1. Goursat's Lemma for Triangles</h3>\n<p>Goursat proved Cauchy's theorem without assuming continuity of partial derivatives $u_x, u_y, v_x, v_y$, requiring only complex differentiability!</p>\n<div class=\"math-theorem\">\n<b>Goursat's Lemma:</b> Let $\\Omega \\subseteq \\mathbb{C}$ be an open set and $T \\subset \\Omega$ a solid triangle whose boundary $\\partial T$ lies in $\\Omega$. If $f$ is holomorphic on $\\Omega$, then:\n$$\\oint_{\\partial T} f(z)\\,dz = 0$$\n</div>\n<p>The proof subdivides $T$ into four congruent subtriangles, selecting the one that maximizes the integral, creating a nested sequence $T_0 \\supset T_1 \\supset T_2 \\dots$ converging to a point $z^*$, where Taylor differentiability $f(z) = f(z^*) + f'(z^*)(z - z^*) + \\epsilon(z)(z - z^*)$ forces the integral to zero.</p>\n\n<h3>2. The Cauchy-Goursat Theorem</h3>\n<div class=\"math-theorem\">\n<b>Theorem 3.3 (Cauchy-Goursat Theorem):</b> If $f(z)$ is holomorphic on a simply connected domain $D$, and $\\gamma$ is any closed rectifiable Jordan contour in $D$, then:\n$$\\oint_\\gamma f(z)\\,dz = 0$$\n</div>"
        }
      ]
    },
    {
      "number": 4,
      "title": "Cauchy's Integral Formula, Liouville's Theorem & The Maximum Modulus Principle",
      "leadSummary": "Cauchy's integral formulas for functions and higher derivatives, Cauchy's estimates, Liouville's theorem, Fundamental Theorem of Algebra, and the Maximum Modulus Principle.",
      "simulations": [
        "complex-max-modulus-sim"
      ],
      "sections": [
        {
          "secNumber": "4.1",
          "title": "Cauchy's Integral Formula & Integral Formula for Higher Derivatives",
          "content": "<h3>1. Cauchy's Integral Formula</h3>\n<div class=\"math-theorem\">\n<b>Theorem 4.1 (Cauchy's Integral Formula):</b> Let $f(z)$ be holomorphic on a simply connected domain $D$, and let $\\gamma$ be a simple closed counter-clockwise contour in $D$. For any point $z_0 \\in \\text{Int}(\\gamma)$:\n$$f(z_0) = \\frac{1}{2\\pi i} \\oint_\\gamma \\frac{f(z)}{z - z_0}\\,dz$$\n</div>\n<p>This remarkable theorem states that the values of a holomorphic function inside a domain are completely and uniquely determined by its values on the boundary $\\gamma$!</p>\n\n<h3>2. Formulas for Higher Derivatives & Infinite Smoothness</h3>\n<p>Differentiating under the integral sign with respect to the parameter $z_0$:</p>\n$$f^{(n)}(z_0) = \\frac{n!}{2\\pi i} \\oint_\\gamma \\frac{f(z)}{(z - z_0)^{n+1}}\\,dz, \\quad n = 1, 2, 3, \\dots$$\n<div class=\"math-theorem\">\n<b>Corollary 4.1 (Infinite Differentiability):</b> If $f(z)$ is holomorphic in a domain $D$, then $f$ is <b>infinitely differentiable</b> in $D$, and all of its derivatives $f'(z), f''(z), \\dots, f^{(n)}(z)$ are also holomorphic in $D$!\n</div>"
        },
        {
          "secNumber": "4.2",
          "title": "Cauchy's Estimates, Liouville's Theorem & The Fundamental Theorem of Algebra",
          "content": "<h3>1. Cauchy's Inequalities</h3>\n<div class=\"math-theorem\">\n<b>Theorem 4.2 (Cauchy's Estimate):</b> Let $f(z)$ be holomorphic on a disk $\\overline{D}(z_0, R)$. If $|f(z)| \\le M$ on the boundary circle $|z - z_0| = R$, then:\n$$|f^{(n)}(z_0)| \\le \\frac{n! M}{R^n}, \\quad n = 0, 1, 2, \\dots$$\n</div>\n\n<h3>2. Liouville's Theorem</h3>\n<div class=\"math-theorem\">\n<b>Theorem 4.3 (Liouville's Theorem):</b> Every <b>bounded entire</b> function is constant.\n</div>\n<p><b>Proof:</b> Let $f(z)$ be entire with $|f(z)| \\le M$ for all $z \\in \\mathbb{C}$. For any $z_0 \\in \\mathbb{C}$ and any radius $R > 0$, Cauchy's estimate for $n = 1$ gives $|f'(z_0)| \\le \\frac{M}{R}$. Letting $R \\to \\infty$ yields $|f'(z_0)| = 0$. Since $z_0$ was arbitrary, $f'(z) \\equiv 0$, so $f(z)$ is constant. $\\blacksquare$</p>\n\n<h3>3. The Fundamental Theorem of Algebra</h3>\n<div class=\"math-theorem\">\n<b>Theorem 4.4 (Fundamental Theorem of Algebra):</b> Every non-constant polynomial $P(z) = a_n z^n + \\dots + a_0$ ($a_n \\ne 0, n \\ge 1$) with complex coefficients has at least one root in $\\mathbb{C}$.\n</div>\n<p><b>Proof:</b> Suppose $P(z) \\ne 0$ for all $z \\in \\mathbb{C}$. Then $g(z) = \\frac{1}{P(z)}$ is an entire function. Since $|P(z)| \\to \\infty$ as $|z| \\to \\infty$, $g(z) \\to 0$, so $g(z)$ is bounded on $\\mathbb{C}$. By Liouville's theorem, $g(z)$ must be constant, contradicting that $P(z)$ has degree $n \\ge 1$. Thus $P(z)$ must have a root in $\\mathbb{C}$. $\\blacksquare$</p>"
        },
        {
          "secNumber": "4.3",
          "title": "Morera's Theorem, The Maximum Modulus Principle & Schwarz's Lemma",
          "simulation": "complex-max-modulus-sim",
          "content": "<h3>1. Morera's Theorem (Converse of Cauchy's Theorem)</h3>\n<div class=\"math-theorem\">\n<b>Theorem 4.5 (Morera's Theorem):</b> Let $f: D \\to \\mathbb{C}$ be continuous on a domain $D$. If $\\oint_\\gamma f(z)\\,dz = 0$ for every closed triangular loop $\\gamma \\subset D$, then $f(z)$ is holomorphic in $D$.\n</div>\n\n<h3>2. The Maximum Modulus Principle</h3>\n<div class=\"math-theorem\">\n<b>Theorem 4.6 (Maximum Modulus Principle):</b> Let $f(z)$ be holomorphic on a bounded domain $D$ and continuous on its closure $\\overline{D}$. If $|f(z)|$ attains its maximum at an interior point $z_0 \\in D$, then $f(z)$ is constant throughout $D$.\nConsequently, the maximum of $|f(z)|$ is strictly achieved on the boundary $\\partial D$:\n$$\\max_{z \\in \\overline{D}} |f(z)| = \\max_{z \\in \\partial D} |f(z)|$$\n</div>\n\n<h3>3. Schwarz's Lemma</h3>\n<div class=\"math-theorem\">\n<b>Theorem 4.7 (Schwarz's Lemma):</b> Let $f: \\mathbb{D} \\to \\mathbb{D}$ be holomorphic on the unit disk $\\mathbb{D} = \\{|z| < 1\\}$ such that $f(0) = 0$. Then:\n$$|f(z)| \\le |z| \\quad \\text{for all } z \\in \\mathbb{D}, \\quad \\text{and} \\quad |f'(0)| \\le 1$$\nIf $|f(z)| = |z|$ for any non-zero $z \\in \\mathbb{D}$, or if $|f'(0)| = 1$, then $f(z) = e^{i\\theta} z$ for some constant $\\theta \\in \\mathbb{R}$.\n</div>"
        }
      ]
    },
    {
      "number": 5,
      "title": "Complex Series Expansions: Taylor, Laurent & Singularity Classification",
      "leadSummary": "Taylor series representation, Laurent series on annular domains, classification of isolated singularities (removable, poles, essential), Casorati-Weierstrass theorem, and Picard's Great Theorem.",
      "simulations": [
        "complex-laurent-annulus-sim"
      ],
      "sections": [
        {
          "secNumber": "5.1",
          "title": "Taylor Series Expansion of Holomorphic Functions & Analytic Radii of Convergence",
          "content": "<h3>1. Taylor's Expansion Theorem</h3>\n<div class=\"math-theorem\">\n<b>Theorem 5.1 (Taylor's Theorem):</b> Let $f(z)$ be holomorphic on an open disk $D(z_0, R)$. Then $f(z)$ has a unique power series representation:\n$$f(z) = \\sum_{n=0}^\\infty a_n (z - z_0)^n$$\nconverging absolutely for all $|z - z_0| < R$, where the coefficients $a_n$ are given by:\n$$a_n = \\frac{f^{(n)}(z_0)}{n!} = \\frac{1}{2\\pi i} \\oint_\\gamma \\frac{f(\\zeta)}{(\\zeta - z_0)^{n+1}}\\,d\\zeta$$\nThe radius of convergence $R$ equals the exact distance from $z_0$ to the nearest singularity of $f(z)$.\n</div>"
        },
        {
          "secNumber": "5.2",
          "title": "Laurent Series Expansion on Annular Domains r < |z - z0| < R",
          "simulation": "complex-laurent-annulus-sim",
          "content": "<h3>1. Laurent's Theorem</h3>\n<p>When a function $f(z)$ is holomorphic in an annular region $A = \\{z \\in \\mathbb{C} : r < |z - z_0| < R\\}$ ($0 \\le r < R \\le \\infty$), it can be represented by a series containing both positive and negative powers of $(z - z_0)$:</p>\n<div class=\"math-theorem\">\n<b>Theorem 5.2 (Laurent's Theorem):</b> For any $z \\in A$:\n$$f(z) = \\sum_{n=-\\infty}^\\infty c_n (z - z_0)^n = \\underbrace{\\sum_{n=1}^\\infty \\frac{b_n}{(z - z_0)^n}}_{\\text{Principal Part}} + \\underbrace{\\sum_{n=0}^\\infty a_n (z - z_0)^n}_{\\text{Analytic Part}}$$\nwhere the coefficients are given by:\n$$c_n = \\frac{1}{2\\pi i} \\oint_\\gamma \\frac{f(\\zeta)}{(\\zeta - z_0)^{n+1}}\\,d\\zeta, \\quad n \\in \\mathbb{Z}$$\nalong any simple closed counter-clockwise contour $\\gamma$ in the annulus.\n</div>"
        },
        {
          "secNumber": "5.3",
          "title": "Classification of Isolated Singularities: Removable, Poles & Essential Singularities",
          "content": "<h3>1. Types of Isolated Singularities</h3>\n<p>Let $z_0$ be an isolated singularity of $f(z)$ (meaning $f$ is holomorphic on punctured disk $0 < |z - z_0| < R$). The nature of the singularity is determined by the <b>principal part</b> $\\sum_{n=1}^\\infty \\frac{b_n}{(z - z_0)^n}$ of its Laurent series:</p>\n<div class=\"math-theorem\">\n<b>Classification:</b>\n<ol>\n<li><b>Removable Singularity:</b> The principal part vanishes entirely ($b_n = 0$ for all $n \\ge 1$). $\\lim_{z \\to z_0} f(z)$ exists and is finite. (Riemann's Removable Singularity Theorem: bounded near $z_0 \\implies$ removable).</li>\n<li><b>Pole of Order $m \\ge 1$:</b> The principal part terminates with finite non-zero terms:\n$$\\frac{b_m}{(z - z_0)^m} + \\dots + \\frac{b_1}{z - z_0}, \\quad b_m \\ne 0$$\nIn this case, $\\lim_{z \\to z_0} |f(z)| = \\infty$. If $m = 1$, it is a <b>simple pole</b>.</li>\n<li><b>Essential Singularity:</b> The principal part contains <b>infinitely many</b> non-zero terms. The limit $\\lim_{z \\to z_0} f(z)$ does not exist (not even as $\\infty$). Example: $e^{1/z} = \\sum_{n=0}^\\infty \\frac{1}{n! z^n}$ at $z = 0$.</li>\n</ol>\n</div>"
        },
        {
          "secNumber": "5.4",
          "title": "Behavior Near Essential Singularities: Casorati-Weierstrass & Picard Theorems",
          "content": "<h3>1. The Casorati-Weierstrass Theorem</h3>\n<div class=\"math-theorem\">\n<b>Theorem 5.3 (Casorati-Weierstrass Theorem):</b> Let $z_0$ be an isolated essential singularity of $f(z)$. Then for any complex number $w \\in \\mathbb{C}$, any $\\epsilon > 0$, and any $\\delta > 0$, there exists a point $z \\in D(z_0, \\delta) \\setminus \\{z_0\\}$ such that:\n$$|f(z) - w| < \\epsilon$$\nIn other words, the image of any punctured neighborhood of an essential singularity is <b>dense</b> in the entire complex plane $\\mathbb{C}$!\n</div>\n\n<h3>2. Picard's Great Theorem</h3>\n<div class=\"math-theorem\">\n<b>Theorem 5.4 (Picard's Great Theorem):</b> In any punctured neighborhood of an isolated essential singularity, $f(z)$ assumes <b>every complex value</b> infinitely many times, with at most <i>one possible exception</i>!\n(For example, $e^{1/z}$ assumes every complex value except $0$).\n</div>"
        }
      ]
    },
    {
      "number": 6,
      "title": "The Residue Theorem, Argument Principle & Rouché's Theorem",
      "leadSummary": "Residue calculus at simple and higher-order poles, Cauchy's residue theorem, logarithmic derivatives, Argument Principle, and Rouché's root-counting theorem.",
      "simulations": [
        "complex-rouche-roots-sim"
      ],
      "sections": [
        {
          "secNumber": "6.1",
          "title": "Definition of Residue & Calculation Techniques for Simple and Multiple Poles",
          "content": "<h3>1. Definition of Residue</h3>\n<p>The <b>residue</b> of $f(z)$ at an isolated singularity $z_0$ is the coefficient $c_{-1}$ of $\\frac{1}{z - z_0}$ in its Laurent series expansion:</p>\n$$\\text{Res}(f, z_0) = c_{-1} = \\frac{1}{2\\pi i} \\oint_\\gamma f(z)\\,dz$$\n\n<h3>2. Operational Formulas for Computing Residues</h3>\n<div class=\"math-theorem\">\n<b>Formulas for Residues:</b>\n<ul>\n<li><b>Simple Pole ($m = 1$):</b>\n$$\\text{Res}(f, z_0) = \\lim_{z \\to z_0} (z - z_0) f(z)$$\nIf $f(z) = \\frac{p(z)}{q(z)}$ where $p(z_0) \\ne 0$, $q(z_0) = 0$, and $q'(z_0) \\ne 0$:\n$$\\text{Res}(f, z_0) = \\frac{p(z_0)}{q'(z_0)}$$</li>\n<li><b>Pole of Order $m \\ge 1$:</b>\n$$\\text{Res}(f, z_0) = \\frac{1}{(m - 1)!} \\lim_{z \\to z_0} \\frac{d^{m-1}}{dz^{m-1}} \\left[ (z - z_0)^m f(z) \\right]$$</li>\n</ul>\n</div>"
        },
        {
          "secNumber": "6.2",
          "title": "Cauchy's Residue Theorem & Homology Formulation",
          "content": "<h3>1. Cauchy's Residue Theorem</h3>\n<div class=\"math-theorem\">\n<b>Theorem 6.1 (Cauchy's Residue Theorem):</b> Let $D$ be a simply connected domain and $\\gamma$ a simple closed counter-clockwise contour in $D$. Let $f(z)$ be holomorphic on and inside $\\gamma$, except at a finite number of isolated singularities $z_1, z_2, \\dots, z_k$ lying strictly in the interior of $\\gamma$. Then:\n$$\\oint_\\gamma f(z)\\,dz = 2\\pi i \\sum_{j=1}^k \\text{Res}(f, z_j)$$\n</div>"
        },
        {
          "secNumber": "6.3",
          "title": "The Argument Principle, Logarithmic Derivatives & Zeros/Poles Counting",
          "content": "<h3>1. The Logarithmic Derivative</h3>\n<p>If $f(z)$ has a zero of order $m$ at $z_0$, $f(z) = (z - z_0)^m g(z)$ with $g(z_0) \\ne 0$. Then $\\frac{f'(z)}{f(z)} = \\frac{m}{z - z_0} + \\frac{g'(z)}{g(z)}$, giving a simple pole with residue $m$.</p>\n<p>If $f(z)$ has a pole of order $p$ at $z_0$, $f(z) = (z - z_0)^{-p} h(z)$, giving residue $-p$.</p>\n\n<h3>2. The Argument Principle</h3>\n<div class=\"math-theorem\">\n<b>Theorem 6.2 (The Argument Principle):</b> Let $f(z)$ be meromorphic in a domain containing a simple closed contour $\\gamma$ and its interior, with no zeros or poles on $\\gamma$. Let $Z$ be the number of zeros and $P$ the number of poles of $f(z)$ inside $\\gamma$ (counted with multiplicity). Then:\n$$\\frac{1}{2\\pi i} \\oint_\\gamma \\frac{f'(z)}{f(z)}\\,dz = Z - P = \\frac{1}{2\\pi} \\Delta_\\gamma \\arg f(z)$$\nwhere $\\Delta_\\gamma \\arg f(z)$ is the total change in the argument of $f(z)$ as $z$ traverses $\\gamma$ once counter-clockwise.\n</div>"
        },
        {
          "secNumber": "6.4",
          "title": "Rouché's Theorem & Location of Polynomial Roots in Disk Regions",
          "simulation": "complex-rouche-roots-sim",
          "content": "<h3>1. Rouché's Theorem</h3>\n<div class=\"math-theorem\">\n<b>Theorem 6.3 (Rouché's Theorem):</b> Let $f(z)$ and $g(z)$ be holomorphic on and inside a simple closed contour $\\gamma$. If the strict inequality:\n$$|g(z)| < |f(z)| \\quad \\text{for all } z \\in \\gamma$$\nholds on the boundary $\\gamma$, then $f(z)$ and $f(z) + g(z)$ have the exact same number of zeros (counted with multiplicity) inside $\\gamma$.\n</div>\n<p><b>Proof Intuition:</b> Think of a person walking a dog on a leash around a flagpole. If the person's distance from the pole $|f(z)|$ is strictly greater than the length of the leash $|g(z)|$, the dog must wind around the flagpole the exact same number of times as the person!</p>"
        }
      ]
    },
    {
      "number": 7,
      "title": "Advanced Contour Integration Techniques: Real Integrals, Jordan's Lemma & Branch Cuts",
      "leadSummary": "Evaluation of real trigonometric and improper rational integrals, Jordan's lemma, indented contours, and multivalued functions with branch cuts and keyhole contours.",
      "simulations": [
        "complex-contour-indent-sim"
      ],
      "sections": [
        {
          "secNumber": "7.1",
          "title": "Rational Trigonometric Integrals ∫_0^(2π) R(cos θ, sin θ) dθ via Unit Circle Substitution",
          "content": "<h3>1. Unit Circle Substitution</h3>\n<p>Integrals of the form $I = \\int_0^{2\\pi} R(\\cos\\theta, \\sin\\theta)\\,d\\theta$ where $R$ is a rational function without singularities on $[0, 2\\pi]$ are evaluated by parameterizing the unit circle $C = \\{|z| = 1\\}$ via $z = e^{i\\theta}$:</p>\n$$dz = i e^{i\\theta} d\\theta = i z\\,d\\theta \\implies d\\theta = \\frac{dz}{iz}$$\n$$\\cos\\theta = \\frac{z + z^{-1}}{2} = \\frac{z^2 + 1}{2z}, \\qquad \\sin\\theta = \\frac{z - z^{-1}}{2i} = \\frac{z^2 - 1}{2iz}$$\n<p>The integral transforms directly into a rational contour integral over the unit circle:</p>\n$$I = \\oint_{|z|=1} R\\left( \\frac{z^2 + 1}{2z}, \\frac{z^2 - 1}{2iz} \\right) \\frac{dz}{iz} = 2\\pi i \\sum_{|z_k| < 1} \\text{Res}(F, z_k)$$"
        },
        {
          "secNumber": "7.2",
          "title": "Improper Real Integrals ∫_(-∞)^∞ P(x)/Q(x) dx & Semi-Circular Contours",
          "content": "<h3>1. Rational Integrals over the Real Line</h3>\n<p>To evaluate $\\int_{-\\infty}^\\infty \\frac{P(x)}{Q(x)}\\,dx$ where $P, Q$ are polynomials, $Q(x) \\ne 0$ for $x \\in \\mathbb{R}$, and $\\deg Q \\ge \\deg P + 2$:</p>\n<p>Integrate $f(z) = \\frac{P(z)}{Q(z)}$ over the closed contour $\\Gamma_R = [-R, R] \\cup C_R$, where $C_R$ is the upper semicircle $z = R e^{i\\theta}, \\theta \\in [0, \\pi]$. By Cauchy's Residue Theorem:</p>\n$$\\int_{-R}^R f(x)\\,dx + \\int_{C_R} f(z)\\,dz = 2\\pi i \\sum_{\\text{Im}(z_k) > 0} \\text{Res}(f, z_k)$$\n<p>By the $ML$-inequality, as $R \\to \\infty$:</p>\n$$\\left| \\int_{C_R} f(z)\\,dz \\right| \\le \\frac{M}{R^{\\deg Q - \\deg P}} \\cdot (\\pi R) \\to 0$$\n$$\\int_{-\\infty}^\\infty \\frac{P(x)}{Q(x)}\\,dx = 2\\pi i \\sum_{\\text{Im}(z_k) > 0} \\text{Res}\\left( \\frac{P}{Q}, z_k \\right)$$"
        },
        {
          "secNumber": "7.3",
          "title": "Fourier-Type Integrals, Indented Contours & Jordan's Lemma",
          "simulation": "complex-contour-indent-sim",
          "content": "<h3>1. Jordan's Lemma</h3>\n<div class=\"math-theorem\">\n<b>Theorem 7.1 (Jordan's Lemma):</b> Let $C_R$ be the upper semicircle $z = R e^{i\\theta}, 0 \\le \\theta \\le \\pi$. If $g(z)$ is continuous on $C_R$ and $M(R) = \\max_{z \\in C_R} |g(z)| \\to 0$ as $R \\to \\infty$, then for any $m > 0$:\n$$\\lim_{R \\to \\infty} \\int_{C_R} g(z) e^{imz}\\,dz = 0$$\n</div>\n<p>This allows evaluation of Fourier transforms $\\int_{-\\infty}^\\infty f(x) e^{imx}\\,dx$ under the milder degree condition $\\deg Q \\ge \\deg P + 1$!</p>\n\n<h3>2. Indented Semicircular Contours</h3>\n<p>When the integrand has simple poles on the real axis (such as $\\frac{e^{iz}}{z}$ at $z = 0$), we indent the contour around the singularity using a small semicircle $\\gamma_\\epsilon$ of radius $\\epsilon$:</p>\n<div class=\"math-theorem\">\n<b>Fractional Residue Theorem:</b> If $\\gamma_\\epsilon$ is a clockwise circular arc of angle $\\alpha$ around a simple pole $z_0$:\n$$\\lim_{\\epsilon \\to 0} \\int_{\\gamma_\\epsilon} f(z)\\,dz = -\\alpha i\\, \\text{Res}(f, z_0)$$\nFor a clockwise semicircle on the real axis ($\\alpha = \\pi$), the contribution is $-\\pi i \\text{Res}(f, z_0)$.\n</div>"
        },
        {
          "secNumber": "7.4",
          "title": "Multivalued Functions, Branch Points, Branch Cuts, Keyhole & Dogbone Contours",
          "content": "<h3>1. Multivalued Functions and Branch Points</h3>\n<p>Functions like $\\log z = \\ln|z| + i(\\arg z + 2\\pi k)$ and $z^\\alpha = e^{\\alpha \\log z}$ are multivalued. A point $z_0$ is a <b>branch point</b> if traversing a small closed loop around $z_0$ changes the branch value of the function.</p>\n<p>A <b>branch cut</b> is a curve introduced in $\\mathbb{C}$ to prevent paths from encircling the branch point, rendering the function single-valued and holomorphic on the cut domain.</p>\n\n<h3>2. The Keyhole Contour</h3>\n<p>To evaluate integrals of the form $\\int_0^\\infty x^{\\alpha - 1} f(x)\\,dx$ ($0 < \\alpha < 1$), we cut the plane along the positive real axis $[0, \\infty)$ and integrate over a keyhole contour consisting of:\n<ol>\n<li>The upper edge of the cut: $z = x + i0^+ \\implies z^\\alpha = x^\\alpha$.</li>\n<li>Large outer circle $C_R$ ($R \\to \\infty$).</li>\n<li>The lower edge of the cut: $z = x - i0^+ \\implies z^\\alpha = x^\\alpha e^{2\\pi i \\alpha}$.</li>\n<li>Small inner circle $C_\\epsilon$ around $0$ ($\\epsilon \\to 0$).</li>\n</ol>\nThe difference between the upper and lower edges yields $(1 - e^{2\\pi i \\alpha}) \\int_0^\\infty x^{\\alpha - 1} f(x)\\,dx = 2\\pi i \\sum \\text{Res}$.</p>"
        }
      ]
    },
    {
      "number": 8,
      "title": "Conformal Mappings, Möbius Transformations & Analytic Continuation",
      "leadSummary": "Angle and scale preservation of conformal maps, Möbius bilinear transformations, cross-ratio invariance, circle-to-circle property, Joukowsky airfoil maps, and analytic continuation.",
      "simulations": [
        "complex-mobius-grid-sim"
      ],
      "sections": [
        {
          "secNumber": "8.1",
          "title": "Conformal Mapping Theory, Angle Preservation & Scale Invariance",
          "content": "<h3>1. Definition of Conformal Mapping</h3>\n<p>A mapping $w = f(z)$ is called <b>conformal</b> at $z_0$ if it preserves both the magnitude and sense (orientation) of angles between any two smooth intersecting curves at $z_0$.</p>\n<div class=\"math-theorem\">\n<b>Theorem 8.1 (Conformality Criterion):</b> Let $f(z)$ be holomorphic in a domain $D$. Then $f(z)$ is conformal at every point $z_0 \\in D$ where $f'(z_0) \\ne 0$.\n</div>\n<p>Points where $f'(z_0) = 0$ are called <b>critical points</b>. At a critical point where $f^{(k)}(z_0) = 0$ for $k = 1, \\dots, m-1$ and $f^{(m)}(z_0) \\ne 0$, angles between curves are multiplied by factor $m$.</p>"
        },
        {
          "secNumber": "8.2",
          "title": "Bilinear (Möbius) Transformations w = (az + b)/(cz + d) & Cross-Ratio Invariance",
          "simulation": "complex-mobius-grid-sim",
          "content": "<h3>1. Möbius (Bilinear) Transformations</h3>\n<p>A <b>Möbius transformation</b> is a rational function of the form:</p>\n$$w = T(z) = \\frac{az + b}{cz + d}, \\quad a, b, c, d \\in \\mathbb{C}, \\quad ad - bc \\ne 0$$\n<p>Under functional composition, Möbius transformations form the projective linear group $\\text{PGL}(2, \\mathbb{C})$ acting as conformal automorphisms of the extended complex plane $\\widehat{\\mathbb{C}}$.</p>\n\n<h3>2. The Circle-to-Circle Property</h3>\n<div class=\"math-theorem\">\n<b>Theorem 8.2 (Preservation of Generalized Circles):</b> Every Möbius transformation maps generalized circles (which include straight lines as circles of infinite radius) to generalized circles.\n</div>\n\n<h3>3. Cross-Ratio Invariance</h3>\n<div class=\"math-theorem\">\n<b>Theorem 8.3 (Cross-Ratio Invariance):</b> For any four distinct points $z_1, z_2, z_3, z_4 \\in \\widehat{\\mathbb{C}}$, the cross-ratio:\n$$(z_1, z_2; z_3, z_4) = \\frac{(z_1 - z_3)(z_2 - z_4)}{(z_1 - z_4)(z_2 - z_3)}$$\nis <b>strictly invariant</b> under any Möbius transformation $T$:\n$$(T(z_1), T(z_2); T(z_3), T(z_4)) = (z_1, z_2; z_3, z_4)$$\nConsequently, the unique Möbius transformation mapping three given points $z_1, z_2, z_3$ to $w_1, w_2, w_3$ is determined by equating $(w, w_1; w_2, w_3) = (z, z_1; z_2, z_3)$.\n</div>"
        },
        {
          "secNumber": "8.3",
          "title": "Canonical Mappings: Upper Half-Plane to Unit Disk & Joukowsky Transformation",
          "content": "<h3>1. The Cayley Transform: Upper Half-Plane to Unit Disk</h3>\n<p>The upper half-plane $\\mathbb{H} = \\{\\text{Im}(z) > 0\\}$ is conformally mapped onto the open unit disk $\\mathbb{D} = \\{|w| < 1\\}$ by the Cayley transform:</p>\n$$w = e^{i\\theta} \\frac{z - z_0}{z - \\bar{z}_0}, \\quad z_0 \\in \\mathbb{H}, \\quad \\theta \\in \\mathbb{R}$$\n<p>The real axis $\\mathbb{R} = \\partial \\mathbb{H}$ maps onto the unit circle $\\partial \\mathbb{D} = \\{|w| = 1\\}$.</p>\n\n<h3>2. The Joukowsky Airfoil Transformation</h3>\n<p>The Joukowsky transformation maps fluid flow past a circular cylinder onto flow past an aerodynamic airfoil with a sharp trailing edge:</p>\n$$w = z + \\frac{c^2}{z}, \\quad c > 0$$\n<p>Critical points occur where $\\frac{dw}{dz} = 1 - \\frac{c^2}{z^2} = 0 \\implies z = \\pm c$. The circle $|z| = c$ collapses onto the real segment $[-2c, 2c]$. A circle passing through $z = -c$ and containing $z = c$ maps onto a streamlined airfoil shape (Joukowsky profile).</p>"
        },
        {
          "secNumber": "8.4",
          "title": "Analytic Continuation, Schwarz Reflection Principle & Riemann Surfaces",
          "content": "<h3>1. Analytic Continuation and Permanence of Functional Relations</h3>\n<p>If two holomorphic functions $f_1, f_2$ on domains $D_1, D_2$ agree on a non-empty open overlap $D_1 \\cap D_2$, then $f_2$ is the unique <b>analytic continuation</b> of $f_1$ into $D_2$.</p>\n\n<h3>2. The Schwarz Reflection Principle</h3>\n<div class=\"math-theorem\">\n<b>Theorem 8.4 (Schwarz Reflection Principle):</b> Let $D$ be a domain symmetric with respect to the real axis ($z \\in D \\iff \\bar{z} \\in D$), and let $D^+ = \\{z \\in D : \\text{Im}(z) > 0\\}$. If $f(z)$ is holomorphic in $D^+$, continuous on $D^+ \\cup (D \\cap \\mathbb{R})$, and real-valued on $D \\cap \\mathbb{R}$, then $f$ can be analytically continued to the entire domain $D$ by defining:\n$$f(z) = \\overline{f(\\bar{z})} \\quad \\text{for } z \\in D^-$$\n</div>\n\n<h3>3. Riemann Surfaces</h3>\n<p>To eliminate branch cuts and render multivalued functions globally single-valued and holomorphic, Bernhard Riemann introduced <b>Riemann surfaces</b>: multi-sheeted branched covering spaces over $\\mathbb{C}$. For example, $w = \\sqrt{z}$ is a single-valued holomorphic function on a two-sheeted helical Riemann surface connected along the branch cut.</p>"
        }
      ]
    }
  ],
  "problems": [
    {
      "id": "prob-01",
      "tier": 1,
      "difficultyLabel": "Tier 1 • University Standard",
      "title": "Harmonic Conjugate & Construction of Holomorphic Function",
      "statement": "Verify that $u(x, y) = x^3 - 3xy^2 + 2x$ is harmonic, and find its harmonic conjugate $v(x, y)$ such that $f(z) = u + iv$ with $f(0) = 0$.",
      "solution": "<b>Step 1: Check Laplace's Equation $\\nabla^2 u = 0$</b><br>\n$$\\frac{\\partial u}{\\partial x} = 3x^2 - 3y^2 + 2, \\quad \\frac{\\partial^2 u}{\\partial x^2} = 6x$$\n$$\\frac{\\partial u}{\\partial y} = -6xy, \\quad \\frac{\\partial^2 u}{\\partial y^2} = -6x$$\n$$\\nabla^2 u = \\frac{\\partial^2 u}{\\partial x^2} + \\frac{\\partial^2 u}{\\partial y^2} = 6x - 6x = 0$$\nHence $u(x, y)$ is harmonic on $\\mathbb{R}^2$.<br><br>\n<b>Step 2: Apply Cauchy-Riemann Equations</b><br>\nFrom $\\frac{\\partial v}{\\partial y} = \\frac{\\partial u}{\\partial x}$:\n$$\\frac{\\partial v}{\\partial y} = 3x^2 - 3y^2 + 2$$\nIntegrating with respect to $y$:\n$$v(x, y) = \\int (3x^2 - 3y^2 + 2)\\,dy = 3x^2 y - y^3 + 2y + g(x)$$\n<br><b>Step 3: Differentiate with respect to $x$ and equate to $-u_y$</b><br>\n$$\\frac{\\partial v}{\\partial x} = 6xy + g'(x) = -\\frac{\\partial u}{\\partial y} = -(-6xy) = 6xy \\implies g'(x) = 0 \\implies g(x) = C$$\nThus $v(x, y) = 3x^2 y - y^3 + 2y + C$.<br><br>\n<b>Step 4: Initial condition and $f(z)$ formulation</b><br>\n$$f(0) = u(0, 0) + i v(0, 0) = 0 + i C = 0 \\implies C = 0$$\n$$f(z) = (x^3 - 3xy^2 + 2x) + i(3x^2 y - y^3 + 2y) = (x + iy)^3 + 2(x + iy) = z^3 + 2z$$",
      "answer": "$v(x, y) = 3x^2 y - y^3 + 2y$ and $f(z) = z^3 + 2z$."
    },
    {
      "id": "prob-02",
      "tier": 1,
      "difficultyLabel": "Tier 1 • University Standard",
      "title": "Radius of Convergence of Complex Power Series",
      "statement": "Find the exact radius of convergence of the complex power series:<br>$$\\sum_{n=1}^\\infty \\frac{(3 + 4i)^n}{n^2} z^n$$",
      "solution": "<b>Step 1: Identify coefficients</b><br>\nThe general term is $a_n z^n$ where $a_n = \\frac{(3 + 4i)^n}{n^2}$.<br><br>\n<b>Step 2: Modulus of coefficients</b><br>\nNotice that $|3 + 4i| = \\sqrt{3^2 + 4^2} = \\sqrt{25} = 5$.\n$$|a_n| = \\frac{|3 + 4i|^n}{n^2} = \\frac{5^n}{n^2}$$\n<br><b>Step 3: Apply the Ratio Test / Cauchy-Hadamard</b><br>\nUsing the ratio test:\n$$\\lim_{n \\to \\infty} \\left| \\frac{a_{n+1}}{a_n} \\right| = \\lim_{n \\to \\infty} \\frac{5^{n+1}}{(n+1)^2} \\cdot \\frac{n^2}{5^n} = \\lim_{n \\to \\infty} 5 \\left( \\frac{n}{n+1} \\right)^2 = 5$$\n<br><b>Step 4: Radius of convergence</b><br>\n$$R = \\frac{1}{\\lim_{n \\to \\infty} |a_{n+1}/a_n|} = \\frac{1}{5}$$\n(On the boundary circle $|z| = 1/5$, $|a_n z^n| = \\frac{1}{n^2}$, so the series converges absolutely by the Weierstrass M-test).",
      "answer": "$R = \\frac{1}{5}$"
    },
    {
      "id": "prob-03",
      "tier": 1,
      "difficultyLabel": "Tier 1 • University Standard",
      "title": "Cauchy's Integral Formula on Unit Circle",
      "statement": "Evaluate the contour integral over the counter-clockwise circle $C: |z| = 1$:<br>$$\\oint_C \\frac{e^z}{z(z - 2)}\\,dz$$",
      "solution": "<b>Step 1: Singularities of the integrand</b><br>\nThe integrand $f(z) = \\frac{e^z}{z(z - 2)}$ has two simple poles: at $z_1 = 0$ and $z_2 = 2$.<br><br>\n<b>Step 2: Location relative to contour $C: |z| = 1$</b><br>\n- $z_1 = 0$: lies <b>inside</b> $C$ since $|0| = 0 < 1$.\n- $z_2 = 2$: lies <b>outside</b> $C$ since $|2| = 2 > 1$.<br><br>\n<b>Step 3: Apply Cauchy's Integral Formula</b><br>\nRewrite the integrand as $\\frac{g(z)}{z - 0}$ where $g(z) = \\frac{e^z}{z - 2}$.\nSince $g(z)$ is holomorphic on and inside $C$:\n$$\\oint_C \\frac{e^z}{z(z - 2)}\\,dz = \\oint_C \\frac{g(z)}{z - 0}\\,dz = 2\\pi i\\, g(0)$$\n<br><b>Step 4: Evaluate $g(0)$</b><br>\n$$g(0) = \\frac{e^0}{0 - 2} = -\\frac{1}{2}$$\n$$\\oint_C \\frac{e^z}{z(z - 2)}\\,dz = 2\\pi i \\left(-\\frac{1}{2}\\right) = -\\pi i$$",
      "answer": "$-\\pi i$"
    },
    {
      "id": "prob-04",
      "tier": 1,
      "difficultyLabel": "Tier 1 • University Standard",
      "title": "Taylor Series & Exact Radius of Convergence",
      "statement": "Find the Taylor series expansion of $f(z) = \\frac{1}{z^2 - 4}$ about $z_0 = 0$ and determine its exact radius of convergence.",
      "solution": "<b>Step 1: Algebraic factorization</b><br>\nRewrite $f(z)$ to utilize the geometric series formula:\n$$f(z) = \\frac{1}{-4(1 - z^2/4)} = -\\frac{1}{4} \\frac{1}{1 - (z/2)^2}$$\n<br><b>Step 2: Geometric Series Expansion</b><br>\nFor $|z/2|^2 < 1 \\iff |z| < 2$:\n$$\\frac{1}{1 - (z/2)^2} = \\sum_{n=0}^\\infty \\left( \\frac{z^2}{4} \\right)^n = \\sum_{n=0}^\\infty \\frac{z^{2n}}{4^n}$$\n<br><b>Step 3: Assemble Taylor Series</b><br>\n$$f(z) = -\\frac{1}{4} \\sum_{n=0}^\\infty \\frac{z^{2n}}{4^n} = -\\sum_{n=0}^\\infty \\frac{z^{2n}}{4^{n+1}} = -\\frac{1}{4} - \\frac{z^2}{16} - \\frac{z^4}{64} - \\dots$$\n<br><b>Step 4: Radius of Convergence</b><br>\nSingularities of $f(z)$ are the roots of $z^2 - 4 = 0 \\implies z = \\pm 2$.\nDistance from center $z_0 = 0$ to nearest singularity is $| \\pm 2 - 0| = 2$.\nHence $R = 2$.",
      "answer": "$f(z) = -\\sum_{n=0}^\\infty \\frac{z^{2n}}{4^{n+1}}$ with radius of convergence $R = 2$."
    },
    {
      "id": "prob-05",
      "tier": 1,
      "difficultyLabel": "Tier 1 • University Standard",
      "title": "Laurent Series in Annular Domain 1 < |z| < 2",
      "statement": "Find the Laurent series expansion of $f(z) = \\frac{1}{(z - 1)(z - 2)}$ in the annular region $1 < |z| < 2$.",
      "solution": "<b>Step 1: Partial Fraction Decomposition</b><br>\n$$\\frac{1}{(z - 1)(z - 2)} = \\frac{A}{z - 1} + \\frac{B}{z - 2}$$\n$1 = A(z - 2) + B(z - 1)$.\nAt $z = 1$: $1 = -A \\implies A = -1$.\nAt $z = 2$: $1 = B \\implies B = 1$.\n$$f(z) = -\\frac{1}{z - 1} + \\frac{1}{z - 2}$$\n<br><b>Step 2: Expand $-\\frac{1}{z - 1}$ for $|z| > 1$ (Principal Part)</b><br>\nSince $|z| > 1 \\implies \\left|\\frac{1}{z}\\right| < 1$:\n$$-\\frac{1}{z - 1} = -\\frac{1}{z(1 - 1/z)} = -\\frac{1}{z} \\sum_{n=0}^\\infty \\frac{1}{z^n} = -\\sum_{n=0}^\\infty \\frac{1}{z^{n+1}} = -\\sum_{m=1}^\\infty \\frac{1}{z^m}$$\n<br><b>Step 3: Expand $\\frac{1}{z - 2}$ for $|z| < 2$ (Analytic Part)</b><br>\nSince $|z| < 2 \\implies \\left|\\frac{z}{2}\\right| < 1$:\n$$\\frac{1}{z - 2} = -\\frac{1}{2(1 - z/2)} = -\\frac{1}{2} \\sum_{n=0}^\\infty \\left(\\frac{z}{2}\\right)^n = -\\sum_{n=0}^\\infty \\frac{z^n}{2^{n+1}}$$\n<br><b>Step 4: Combine both series</b><br>\n$$f(z) = -\\sum_{m=1}^\\infty \\frac{1}{z^m} - \\sum_{n=0}^\\infty \\frac{z^n}{2^{n+1}} = \\dots - \\frac{1}{z^2} - \\frac{1}{z} - \\frac{1}{2} - \\frac{z}{4} - \\frac{z^2}{8} - \\dots$$",
      "answer": "$f(z) = -\\sum_{m=1}^\\infty \\frac{1}{z^m} - \\sum_{n=0}^\\infty \\frac{z^n}{2^{n+1}}$"
    },
    {
      "id": "prob-06",
      "tier": 1,
      "difficultyLabel": "Tier 1 • University Standard",
      "title": "Residue Computation at Simple and Multiple Poles",
      "statement": "Calculate the residues at all poles for:<br>$$f(z) = \\frac{z^2 + 1}{(z - 1)^2 (z + 2)}$$",
      "solution": "<b>Step 1: Identify poles and orders</b><br>\n- Pole at $z = -2$: simple pole (order 1).\n- Pole at $z = 1$: double pole (order 2).<br><br>\n<b>Step 2: Residue at simple pole $z = -2$</b><br>\n$$\\text{Res}(f, -2) = \\lim_{z \\to -2} (z + 2) f(z) = \\lim_{z \\to -2} \\frac{z^2 + 1}{(z - 1)^2} = \\frac{(-2)^2 + 1}{(-2 - 1)^2} = \\frac{5}{(-3)^2} = \\frac{5}{9}$$\n<br><b>Step 3: Residue at double pole $z = 1$</b><br>\nUsing formula for pole of order 2 ($m = 2$):\n$$\\text{Res}(f, 1) = \\frac{1}{(2 - 1)!} \\lim_{z \\to 1} \\frac{d}{dz} \\left[ (z - 1)^2 f(z) \\right] = \\lim_{z \\to 1} \\frac{d}{dz} \\left( \\frac{z^2 + 1}{z + 2} \\right)$$\nQuotient rule:\n$$\\frac{d}{dz} \\left( \\frac{z^2 + 1}{z + 2} \\right) = \\frac{2z(z + 2) - (z^2 + 1)(1)}{(z + 2)^2} = \\frac{2z^2 + 4z - z^2 - 1}{(z + 2)^2} = \\frac{z^2 + 4z - 1}{(z + 2)^2}$$\nEvaluate at $z = 1$:\n$$\\text{Res}(f, 1) = \\frac{1^2 + 4(1) - 1}{(1 + 2)^2} = \\frac{4}{9}$$\n(Notice: $\\text{Res}(f, -2) + \\text{Res}(f, 1) = \\frac{5}{9} + \\frac{4}{9} = 1 = -\\text{Res}(f, \\infty)$).",
      "answer": "$\\text{Res}(f, -2) = \\frac{5}{9}$ and $\\text{Res}(f, 1) = \\frac{4}{9}$."
    },
    {
      "id": "prob-07",
      "tier": 1,
      "difficultyLabel": "Tier 1 • University Standard",
      "title": "Real Trigonometric Definite Integral via Residue Calculus",
      "statement": "Evaluate using contour integration:<br>$$\\int_0^{2\\pi} \\frac{d\\theta}{5 + 4\\cos\\theta}$$",
      "solution": "<b>Step 1: Unit circle transformation</b><br>\nLet $z = e^{i\\theta} \\implies d\\theta = \\frac{dz}{iz}$, and $\\cos\\theta = \\frac{z + z^{-1}}{2} = \\frac{z^2 + 1}{2z}$.\n$$\\int_0^{2\\pi} \\frac{d\\theta}{5 + 4\\cos\\theta} = \\oint_{|z|=1} \\frac{1}{5 + 4\\left(\\frac{z^2 + 1}{2z}\\right)} \\frac{dz}{iz} = \\oint_{|z|=1} \\frac{dz}{i z \\left(5 + \\frac{2z^2 + 2}{z}\\right)}$$\n$$= \\oint_{|z|=1} \\frac{dz}{i(2z^2 + 5z + 2)}$$\n<br><b>Step 2: Factor denominator</b><br>\n$2z^2 + 5z + 2 = (2z + 1)(z + 2) = 2(z + 1/2)(z + 2)$.\nPoles: $z_1 = -1/2$ and $z_2 = -2$.<br><br>\n<b>Step 3: Poles inside unit circle $|z| = 1$</b><br>\n- $z_1 = -1/2$: $| -1/2 | = 1/2 < 1$ (<b>inside</b>).\n- $z_2 = -2$: $| -2 | = 2 > 1$ (<b>outside</b>).<br><br>\n<b>Step 4: Residue at $z_1 = -1/2$</b><br>\n$$\\text{Res}\\left( \\frac{1}{i(2z^2 + 5z + 2)}, -\\frac{1}{2} \\right) = \\lim_{z \\to -1/2} \\frac{z + 1/2}{2i(z + 1/2)(z + 2)} = \\frac{1}{2i(-1/2 + 2)} = \\frac{1}{2i(3/2)} = \\frac{1}{3i}$$\n<br><b>Step 5: Apply Residue Theorem</b><br>\n$$\\int_0^{2\\pi} \\frac{d\\theta}{5 + 4\\cos\\theta} = 2\\pi i \\left( \\frac{1}{3i} \\right) = \\frac{2\\pi}{3}$$",
      "answer": "$\\frac{2\\pi}{3}$"
    },
    {
      "id": "prob-08",
      "tier": 1,
      "difficultyLabel": "Tier 1 • University Standard",
      "title": "Möbius Transformation via Cross-Ratio",
      "statement": "Find the unique Möbius transformation $w = T(z)$ mapping $z_1 = 0, z_2 = 1, z_3 = \\infty$ to $w_1 = -1, w_2 = -i, w_3 = 1$.",
      "solution": "<b>Step 1: Cross-ratio formula</b><br>\nThe cross-ratio $(w, w_1; w_2, w_3) = (z, z_1; z_2, z_3)$ is invariant:\n$$\\frac{(w - w_2)(w_1 - w_3)}{(w - w_3)(w_1 - w_2)} = \\frac{(z - z_2)(z_1 - z_3)}{(z - z_3)(z_1 - z_2)}$$\n<br><b>Step 2: Handle points with $\\infty$</b><br>\nSince $z_3 = \\infty$, the RHS simplifies to:\n$$\\frac{z - z_2}{z_1 - z_2} = \\frac{z - 1}{0 - 1} = -(z - 1) = 1 - z$$\n<br><b>Step 3: Substitute $w$-points into LHS</b><br>\n$w_1 = -1, w_2 = -i, w_3 = 1$:\n$$\\frac{(w - (-i))(-1 - 1)}{(w - 1)(-1 - (-i))} = \\frac{(w + i)(-2)}{(w - 1)(-1 + i)} = \\frac{2(w + i)}{(1 - i)(w - 1)}$$\nMultiply numerator and denominator by $1 + i$: $\\frac{2}{1 - i} = \\frac{2(1 + i)}{2} = 1 + i$.\n$$(1 + i) \\frac{w + i}{w - 1} = 1 - z$$\n<br><b>Step 4: Solve for $w$</b><br>\n$$(1 + i)(w + i) = (1 - z)(w - 1) \\implies (1 + i)w + i - 1 = w(1 - z) - (1 - z)$$\n$$w[(1 + i) - (1 - z)] = -(1 - z) - (i - 1) = z - 1 - i + 1 = z - i$$\n$$w(z + i) = z - i \\implies w = \\frac{z - i}{z + i}$$\nVerify:\n$z = 0 \\implies w = -i/i = -1$.\n$z = 1 \\implies w = \\frac{1 - i}{1 + i} = -i$.\n$z \\to \\infty \\implies w \\to 1$. Perfect!",
      "answer": "$w = \\frac{z - i}{z + i}$"
    },
    {
      "id": "prob-09",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Advanced Analytical",
      "title": "Constancy of Holomorphic Functions with Constant Modulus",
      "statement": "Prove that if $f(z) = u(x, y) + i v(x, y)$ is holomorphic on a connected domain $D$ and $|f(z)| = c$ is constant on $D$, then $f(z)$ must be constant.",
      "solution": "<b>Case 1: $c = 0$</b><br>\nIf $|f(z)| = 0$, then $f(z) = 0$ for all $z \\in D$, which is identically constant.<br><br>\n<b>Case 2: $c > 0$</b><br>\nSince $|f(z)|^2 = u^2 + v^2 = c^2$, differentiate partially with respect to $x$ and $y$:\n$$2u \\frac{\\partial u}{\\partial x} + 2v \\frac{\\partial v}{\\partial x} = 0 \\implies u u_x + v v_x = 0 \\quad \\text{--- (1)}$$\n$$2u \\frac{\\partial u}{\\partial y} + 2v \\frac{\\partial v}{\\partial y} = 0 \\implies u u_y + v v_y = 0 \\quad \\text{--- (2)}$$\n<br><b>Step 2: Apply Cauchy-Riemann equations</b><br>\nRecall $u_y = -v_x$ and $v_y = u_x$. Substituting into (2):\n$$-u v_x + v u_x = 0 \\implies v u_x - u v_x = 0 \\quad \\text{--- (3)}$$\n<br><b>Step 3: Linear System for $(u_x, v_x)$</b><br>\nFrom (1) and (3), we have the matrix equation:\n$$\\begin{pmatrix} u & v \\\\ v & -u \\end{pmatrix} \\begin{pmatrix} u_x \\\\ v_x \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 0 \\end{pmatrix}$$\nThe determinant of this coefficient matrix is:\n$$\\det \\begin{pmatrix} u & v \\\\ v & -u \\end{pmatrix} = -u^2 - v^2 = -(u^2 + v^2) = -c^2 \\ne 0$$\nSince the determinant is strictly non-zero, the linear system has only the trivial solution:\n$$u_x = 0, \\quad v_x = 0$$\nBy the Cauchy-Riemann equations, $v_y = u_x = 0$ and $u_y = -v_x = 0$.<br>\nTherefore, the gradient of both $u$ and $v$ vanishes throughout $D$. Since $D$ is connected, $u$ and $v$ are constant, which proves $f(z)$ is constant. $\\blacksquare$",
      "answer": "Proved: $f'(z) = 0$ everywhere on connected domain $D \\implies f(z)$ is constant."
    },
    {
      "id": "prob-10",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Advanced Analytical",
      "title": "Cauchy's Integral Formula for Second Derivative",
      "statement": "Evaluate the contour integral over counter-clockwise circle $C: |z| = 3$:<br>$$\\oint_C \\frac{\\cos z}{(z - \\pi/2)^3}\\,dz$$",
      "solution": "<b>Step 1: Singularity and contour check</b><br>\nThe integrand has a pole of order 3 at $z_0 = \\pi/2 \\approx 1.5708$.\nThe contour is $|z| = 3$. Since $|\\pi/2| < 3$, $z_0$ lies <b>inside</b> $C$.<br><br>\n<b>Step 2: Apply Cauchy's formula for derivatives</b><br>\n$$f^{(n)}(z_0) = \\frac{n!}{2\\pi i} \\oint_C \\frac{f(z)}{(z - z_0)^{n+1}}\\,dz \\implies \\oint_C \\frac{f(z)}{(z - z_0)^{n+1}}\\,dz = \\frac{2\\pi i}{n!} f^{(n)}(z_0)$$\nFor denominator $(z - \\pi/2)^3$, we have $n + 1 = 3 \\implies n = 2$.\nHere $f(z) = \\cos z$.<br><br>\n<b>Step 3: Compute second derivative</b><br>\n$$f'(z) = -\\sin z, \\quad f''(z) = -\\cos z$$\nEvaluate at $z_0 = \\pi/2$:\n$$f''(\\pi/2) = -\\cos(\\pi/2) = 0$$\n<br><b>Step 4: Evaluate integral</b><br>\n$$\\oint_C \\frac{\\cos z}{(z - \\pi/2)^3}\\,dz = \\frac{2\\pi i}{2!} f''(\\pi/2) = \\pi i (0) = 0$$",
      "answer": "$0$"
    },
    {
      "id": "prob-11",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Advanced Analytical",
      "title": "Proof of Liouville's Theorem via Cauchy's Estimate",
      "statement": "Prove Liouville's theorem: Every bounded entire function is constant, using Cauchy's integral estimates.",
      "solution": "<b>Step 1: Hypothesis</b><br>\nLet $f: \\mathbb{C} \\to \\mathbb{C}$ be an entire function (holomorphic on all of $\\mathbb{C}$), and suppose there exists $M > 0$ such that $|f(z)| \\le M$ for all $z \\in \\mathbb{C}$.<br><br>\n<b>Step 2: Apply Cauchy's Estimate for $f'(z_0)$</b><br>\nLet $z_0 \\in \\mathbb{C}$ be an arbitrary point. For any $R > 0$, consider the circle $C_R = \\{z \\in \\mathbb{C} : |z - z_0| = R\\}$.\nBy Cauchy's derivative formula:\n$$f'(z_0) = \\frac{1}{2\\pi i} \\oint_{C_R} \\frac{f(z)}{(z - z_0)^2}\\,dz$$\nApplying the $ML$-inequality:\n$$\\left| f'(z_0) \\right| \\le \\frac{1}{2\\pi} \\max_{z \\in C_R} \\frac{|f(z)|}{|z - z_0|^2} \\cdot \\text{Length}(C_R) \\le \\frac{1}{2\\pi} \\frac{M}{R^2} (2\\pi R) = \\frac{M}{R}$$\n<br><b>Step 3: Take the limit $R \\to \\infty$</b><br>\nSince $f$ is entire, the circle $C_R$ is valid for arbitrarily large $R$.\nTaking the limit as $R \\to \\infty$:\n$$0 \\le |f'(z_0)| \\le \\lim_{R \\to \\infty} \\frac{M}{R} = 0 \\implies |f'(z_0)| = 0 \\implies f'(z_0) = 0$$\nSince $z_0$ was chosen arbitrarily in $\\mathbb{C}$, $f'(z) = 0$ for all $z \\in \\mathbb{C}$.\nBecause $\\mathbb{C}$ is connected, $f(z)$ must be constant everywhere. $\\blacksquare$",
      "answer": "Proved: $|f'(z_0)| \\le \\frac{M}{R} \\to 0$ as $R \\to \\infty \\implies f'(z) \\equiv 0$."
    },
    {
      "id": "prob-12",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Advanced Analytical",
      "title": "Singularity Classification: Isolated vs Non-Isolated Singularities",
      "statement": "Classify all singularities of $f(z) = \\frac{1}{\\sin(1/z)}$ and determine whether $z = 0$ is an isolated singularity.",
      "solution": "<b>Step 1: Zeros of the denominator</b><br>\nSingularities occur where $\\sin(1/z) = 0$:\n$$\\frac{1}{z} = n\\pi, \\quad n \\in \\mathbb{Z} \\setminus \\{0\\} \\implies z_n = \\frac{1}{n\\pi}$$\n<br><b>Step 2: Nature of singularities $z_n$</b><br>\nFor each $n \\ne 0$, $\\sin(1/z_n) = 0$ and the derivative of denominator at $z_n$ is:\n$$\\left. \\frac{d}{dz} \\sin(1/z) \\right|_{z_n} = \\cos(1/z_n) \\left(-\\frac{1}{z_n^2}\\right) = \\cos(n\\pi) (-n^2 \\pi^2) = (-1)^{n+1} n^2 \\pi^2 \\ne 0$$\nHence, each $z_n = \\frac{1}{n\\pi}$ is a <b>simple pole</b>.<br><br>\n<b>Step 3: Analysis of $z = 0$</b><br>\nNotice that as $n \\to \\infty$, the poles accumulate:\n$$\\lim_{n \\to \\infty} z_n = \\lim_{n \\to \\infty} \\frac{1}{n\\pi} = 0$$\nEvery punctured neighborhood $D(0, \\epsilon) \\setminus \\{0\\}$ contains infinitely many poles $z_n$ (for all $n > \\frac{1}{\\pi\\epsilon}$).\nTherefore, $z = 0$ is <b>NOT an isolated singularity</b>! It is an <b>accumulation point of poles</b> (non-isolated essential singularity).",
      "answer": "$z_n = \\frac{1}{n\\pi}$ ($n \\in \\mathbb{Z} \\setminus \\{0\\}$) are simple poles; $z = 0$ is a non-isolated singularity (accumulation point of poles)."
    },
    {
      "id": "prob-13",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Advanced Analytical",
      "title": "Rouché's Theorem: Roots of Polynomial in Concentric Annuli",
      "statement": "Use Rouché's theorem to prove that all five roots of $z^5 + 3z + 1 = 0$ lie in $|z| < 2$, and exactly one root lies in $|z| < 1$.",
      "solution": "<b>Part 1: Disk $|z| < 2$</b><br>\nLet $f(z) = z^5$ and $g(z) = 3z + 1$.\nOn the circle $C_2: |z| = 2$:\n$$|f(z)| = |z|^5 = 2^5 = 32$$\n$$|g(z)| = |3z + 1| \\le 3|z| + 1 = 3(2) + 1 = 7$$\nSince $|g(z)| = 7 < 32 = |f(z)|$ on $|z| = 2$, by Rouché's Theorem, $f(z) + g(z) = z^5 + 3z + 1$ has the same number of roots inside $|z| < 2$ as $f(z) = z^5$.\nSince $z^5$ has 5 roots (at $z = 0$), all 5 roots of $z^5 + 3z + 1 = 0$ lie inside $|z| < 2$.<br><br>\n<b>Part 2: Disk $|z| < 1$</b><br>\nNow choose $f_1(z) = 3z$ and $g_1(z) = z^5 + 1$.\nOn the circle $C_1: |z| = 1$:\n$$|f_1(z)| = 3|z| = 3(1) = 3$$\n$$|g_1(z)| = |z^5 + 1| \\le |z|^5 + 1 = 1 + 1 = 2$$\nSince $|g_1(z)| = 2 < 3 = |f_1(z)|$ on $|z| = 1$, by Rouché's Theorem, $f_1(z) + g_1(z) = z^5 + 3z + 1$ has the same number of roots inside $|z| < 1$ as $f_1(z) = 3z$.\nSince $3z = 0$ has exactly 1 root (at $z = 0$), $z^5 + 3z + 1 = 0$ has <b>exactly 1 root</b> inside $|z| < 1$.<br><br>\n(The remaining 4 roots lie in the annular region $1 \\le |z| < 2$).",
      "answer": "Proved: All 5 roots lie in $|z| < 2$; exactly 1 root in $|z| < 1$; 4 roots in $1 \\le |z| < 2$."
    },
    {
      "id": "prob-14",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Advanced Analytical",
      "title": "Improper Rational Integral via Semicircular Contour",
      "statement": "Evaluate using contour integration:<br>$$\\int_{-\\infty}^\\infty \\frac{x^2}{(x^2 + 1)(x^2 + 4)}\\,dx$$",
      "solution": "<b>Step 1: Complex extension and contour</b><br>\nLet $f(z) = \\frac{z^2}{(z^2 + 1)(z^2 + 4)}$.\nIntegrate over $\\Gamma_R = [-R, R] \\cup C_R$ where $C_R$ is the upper semicircle in the upper half-plane $\\text{Im}(z) > 0$.<br><br>\n<b>Step 2: Poles in the upper half-plane</b><br>\nDenominator roots: $z = \\pm i$ and $z = \\pm 2i$.\nPoles with $\\text{Im}(z) > 0$: $z_1 = i$ and $z_2 = 2i$.<br><br>\n<b>Step 3: Residue at $z_1 = i$</b><br>\n$$\\text{Res}(f, i) = \\lim_{z \\to i} (z - i) \\frac{z^2}{(z - i)(z + i)(z^2 + 4)} = \\frac{i^2}{(2i)(i^2 + 4)} = \\frac{-1}{(2i)(3)} = \\frac{-1}{6i} = \\frac{i}{6}$$\n<br><b>Step 4: Residue at $z_2 = 2i$</b><br>\n$$\\text{Res}(f, 2i) = \\lim_{z \\to 2i} (z - 2i) \\frac{z^2}{(z^2 + 1)(z - 2i)(z + 2i)} = \\frac{(2i)^2}{((2i)^2 + 1)(4i)} = \\frac{-4}{(-3)(4i)} = \\frac{1}{3i} = -\\frac{i}{3}$$\n<br><b>Step 5: Apply Residue Theorem</b><br>\n$$\\int_{-\\infty}^\\infty \\frac{x^2}{(x^2 + 1)(x^2 + 4)}\\,dx = 2\\pi i [\\text{Res}(f, i) + \\text{Res}(f, 2i)] = 2\\pi i \\left( \\frac{i}{6} - \\frac{i}{3} \\right) = 2\\pi i \\left(-\\frac{i}{6}\\right) = \\frac{2\\pi}{6} = \\frac{\\pi}{3}$$",
      "answer": "$\\frac{\\pi}{3}$"
    },
    {
      "id": "prob-15",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Advanced Analytical",
      "title": "Dirichlet Integral ∫_0^∞ (sin x)/x dx via Indented Contour",
      "statement": "Evaluate the Dirichlet integral $\\int_0^\\infty \\frac{\\sin x}{x}\\,dx = \\frac{\\pi}{2}$ using an indented contour around the pole at $z = 0$.",
      "solution": "<b>Step 1: Complex integrand and contour</b><br>\nConsider $f(z) = \\frac{e^{iz}}{z}$.\nContour $\\Gamma$:\n1. $[-R, -\\epsilon]$ along real axis.\n2. Clockwise semicircle $\\gamma_\\epsilon: z = \\epsilon e^{i\\theta}, \\theta: \\pi \\to 0$.\n3. $[\\epsilon, R]$ along real axis.\n4. Counter-clockwise semicircle $C_R: z = R e^{i\\theta}, \\theta: 0 \\to \\pi$.<br>\nSince $f(z)$ has no poles inside $\\Gamma$, Cauchy's Theorem gives $\\oint_\\Gamma f(z)\\,dz = 0$.<br><br>\n<b>Step 2: Real axis contribution</b><br>\n$$\\int_{-R}^{-\\epsilon} \\frac{e^{ix}}{x}\\,dx + \\int_\\epsilon^R \\frac{e^{ix}}{x}\\,dx = \\int_\\epsilon^R \\frac{e^{ix} - e^{-ix}}{x}\\,dx = 2i \\int_\\epsilon^R \\frac{\\sin x}{x}\\,dx$$\n<br><b>Step 3: Small indentation $\\gamma_\\epsilon$ ($\\epsilon \\to 0$)</b><br>\nNear $z = 0$, $\\frac{e^{iz}}{z} = \\frac{1 + iz + \\dots}{z} = \\frac{1}{z} + i + \\dots$.\n$$\\lim_{\\epsilon \\to 0} \\int_{\\gamma_\\epsilon} \\frac{e^{iz}}{z}\\,dz = -\\pi i\\, \\text{Res}\\left(\\frac{e^{iz}}{z}, 0\\right) = -\\pi i(1) = -\\pi i$$\n<br><b>Step 4: Large semicircle $C_R$ ($R \\to \\infty$)</b><br>\nBy Jordan's lemma, $\\lim_{R \\to \\infty} \\int_{C_R} \\frac{e^{iz}}{z}\\,dz = 0$.<br><br>\n<b>Step 5: Total sum</b><br>\n$$2i \\int_0^\\infty \\frac{\\sin x}{x}\\,dx - \\pi i + 0 = 0 \\implies 2i \\int_0^\\infty \\frac{\\sin x}{x}\\,dx = \\pi i \\implies \\int_0^\\infty \\frac{\\sin x}{x}\\,dx = \\frac{\\pi}{2}$$",
      "answer": "$\\int_0^\\infty \\frac{\\sin x}{x}\\,dx = \\frac{\\pi}{2}$"
    },
    {
      "id": "prob-16",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Advanced Analytical",
      "title": "Conformal Exponential Mapping of Infinite Horizontal Strip",
      "statement": "Determine the conformal image of the horizontal strip $S = \\{z = x + iy : -\\infty < x < \\infty, 0 < y < \\pi\\}$ under $w = e^z$.",
      "solution": "<b>Step 1: Coordinate transformation</b><br>\nLet $z = x + iy \\implies w = u + iv = e^{x + iy} = e^x (\\cos y + i\\sin y)$.\nIn polar form $w = \\rho e^{i\\phi}$:\n$$\\rho = |w| = e^x, \\qquad \\phi = \\arg w = y$$\n<br><b>Step 2: Range of modulus and argument</b><br>\n- As $x \\in (-\\infty, \\infty)$, the modulus $\\rho = e^x$ ranges over $(0, \\infty)$.\n- As $y \\in (0, \\pi)$, the argument $\\phi = y$ ranges over $(0, \\pi)$.<br><br>\n<b>Step 3: Boundary mapping</b><br>\n- Lower boundary $y = 0$: $w = e^x (\\cos 0 + i\\sin 0) = e^x > 0$. Maps to the positive real axis $(0, \\infty)$.\n- Upper boundary $y = \\pi$: $w = e^x (\\cos\\pi + i\\sin\\pi) = -e^x < 0$. Maps to the negative real axis $(-\\infty, 0)$.\n- As $x \\to -\\infty$, $w \\to 0$ (the origin).<br><br>\n<b>Conclusion:</b> The infinite horizontal strip $0 < y < \\pi$ is mapped conformally and bijectively onto the <b>Upper Half-Plane</b> $\\mathbb{H} = \\{w \\in \\mathbb{C} : \\text{Im}(w) > 0\\}$.",
      "answer": "Upper Half-Plane $\\mathbb{H} = \\{w \\in \\mathbb{C} : \\text{Im}(w) > 0\\}$."
    },
    {
      "id": "prob-17",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Rigorous Proof of Morera's Theorem",
      "statement": "Prove Morera's Theorem: If $f: D \\to \\mathbb{C}$ is continuous and $\\oint_\\gamma f(z)\\,dz = 0$ for every closed triangular contour $\\gamma \\subset D$, then $f$ is holomorphic in $D$.",
      "solution": "<b>Step 1: Construct a local primitive $F(z)$</b><br>\nLet $z_0 \\in D$. Choose an open disk $B(z_0, r) \\subseteq D$. For any $z \\in B(z_0, r)$, define:\n$$F(z) = \\int_{[z_0, z]} f(\\zeta)\\,d\\zeta$$\nwhere $[z_0, z]$ is the straight line segment from $z_0$ to $z$.<br><br>\n<b>Step 2: Differentiate $F(z)$</b><br>\nFor any $h \\in \\mathbb{C}$ with $z + h \\in B(z_0, r)$, consider the triangle with vertices $z_0, z, z + h$.\nBy hypothesis, the integral over the boundary of this triangle vanishes:\n$$\\int_{[z_0, z]} f(\\zeta)\\,d\\zeta + \\int_{[z, z+h]} f(\\zeta)\\,d\\zeta + \\int_{[z+h, z_0]} f(\\zeta)\\,d\\zeta = 0$$\nTherefore:\n$$F(z + h) - F(z) = \\int_{[z, z+h]} f(\\zeta)\\,d\\zeta$$\n<br><b>Step 3: Difference quotient limit</b><br>\n$$\\frac{F(z + h) - F(z)}{h} - f(z) = \\frac{1}{h} \\int_{[z, z+h]} [f(\\zeta) - f(z)]\\,d\\zeta$$\nSince $f$ is continuous at $z$, for any $\\epsilon > 0$, there exists $\\delta > 0$ such that $|f(\\zeta) - f(z)| < \\epsilon$ whenever $|\\zeta - z| \\le |h| < \\delta$.\nUsing the $ML$-inequality:\n$$\\left| \\frac{F(z + h) - F(z)}{h} - f(z) \\right| \\le \\frac{1}{|h|} \\cdot \\epsilon \\cdot |h| = \\epsilon$$\nTaking $h \\to 0$ proves $F'(z) = f(z)$ for all $z \\in B(z_0, r)$.<br><br>\n<b>Step 4: Infinite differentiability of holomorphic functions</b><br>\nSince $F(z)$ is complex differentiable in $B(z_0, r)$, $F$ is holomorphic.\nBy Corollary 4.1, every holomorphic function is infinitely differentiable!\nTherefore, its derivative $F'(z) = f(z)$ is also holomorphic in $B(z_0, r)$, and since $z_0$ was arbitrary, $f(z)$ is holomorphic throughout $D$. $\\blacksquare$",
      "answer": "Proved: $F(z)$ is a primitive of $f(z) \\implies F$ is holomorphic $\\implies f = F'$ is holomorphic."
    },
    {
      "id": "prob-18",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Proof of Maximum Modulus Principle via Mean Value Property",
      "statement": "Prove the Maximum Modulus Principle using the Mean Value Property for holomorphic functions.",
      "solution": "<b>Step 1: The Mean Value Property</b><br>\nLet $f(z)$ be holomorphic in a domain $D$. For any $z_0 \\in D$ and circle $C_r: z = z_0 + r e^{i\\theta}$ lying with its disk in $D$, Cauchy's Integral Formula gives:\n$$f(z_0) = \\frac{1}{2\\pi i} \\oint_{C_r} \\frac{f(z)}{z - z_0}\\,dz = \\frac{1}{2\\pi i} \\int_0^{2\\pi} \\frac{f(z_0 + r e^{i\\theta})}{r e^{i\\theta}} (i r e^{i\\theta})\\,d\\theta = \\frac{1}{2\\pi} \\int_0^{2\\pi} f(z_0 + r e^{i\\theta})\\,d\\theta$$\n<br><b>Step 2: Triangle Inequality</b><br>\nTaking the modulus:\n$$|f(z_0)| \\le \\frac{1}{2\\pi} \\int_0^{2\\pi} |f(z_0 + r e^{i\\theta})|\\,d\\theta$$\n<br><b>Step 3: Assume local maximum at interior point</b><br>\nSuppose $|f(z)|$ attains a local maximum at $z_0$, so $|f(z)| \\le |f(z_0)|$ for all $z \\in D(z_0, \\delta)$.\nThen for any $0 < r < \\delta$:\n$$|f(z_0)| \\le \\frac{1}{2\\pi} \\int_0^{2\\pi} |f(z_0 + r e^{i\\theta})|\\,d\\theta \\le \\frac{1}{2\\pi} \\int_0^{2\\pi} |f(z_0)|\\,d\\theta = |f(z_0)|$$\nThe two outer expressions are equal, forcing the inequality to be an equality:\n$$\\frac{1}{2\\pi} \\int_0^{2\\pi} [|f(z_0)| - |f(z_0 + r e^{i\\theta})|]\\,d\\theta = 0$$\nSince the integrand is continuous and non-negative, it must vanish identically:\n$$|f(z_0 + r e^{i\\theta})| = |f(z_0)| \\quad \\text{for all } \\theta \\in [0, 2\\pi]$$\n<br><b>Step 4: Extension to connected domain</b><br>\nThis proves $|f(z)|$ is constant on $D(z_0, \\delta)$. By Problem 9, a holomorphic function with constant modulus is constant. By the Identity Theorem, $f(z)$ is constant throughout the entire connected domain $D$. $\\blacksquare$",
      "answer": "Proved: Mean value equality forces $|f(z)| \\equiv |f(z_0)| \\implies f(z)$ is constant."
    },
    {
      "id": "prob-19",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Proof of the Casorati-Weierstrass Theorem",
      "statement": "Prove the Casorati-Weierstrass Theorem: If $z_0$ is an isolated essential singularity of $f(z)$, then $f(D(z_0, \\delta) \\setminus \\{z_0\\})$ is dense in $\\mathbb{C}$.",
      "solution": "<b>Step 1: Proof by Contradiction</b><br>\nSuppose the image is NOT dense in $\\mathbb{C}$.\nThen there exists some complex number $w \\in \\mathbb{C}$ and $\\epsilon > 0$ such that $f(z)$ never enters the $\\epsilon$-neighborhood $D(w, \\epsilon)$ for any $z$ in some punctured disk $D^*(z_0, \\delta) = D(z_0, \\delta) \\setminus \\{z_0\\}$.\nThat is:\n$$|f(z) - w| \\ge \\epsilon \\quad \\text{for all } z \\in D^*(z_0, \\delta)$$\n<br><b>Step 2: Construct auxiliary function $g(z)$</b><br>\nDefine:\n$$g(z) = \\frac{1}{f(z) - w}$$\nSince $f(z) - w \\ne 0$ on $D^*(z_0, \\delta)$, $g(z)$ is holomorphic on $D^*(z_0, \\delta)$.\nFurthermore, $g(z)$ is <b>bounded</b> on $D^*(z_0, \\delta)$:\n$$|g(z)| = \\frac{1}{|f(z) - w|} \\le \\frac{1}{\\epsilon}$$\n<br><b>Step 3: Apply Riemann's Removable Singularity Theorem</b><br>\nSince $g(z)$ is bounded on $D^*(z_0, \\delta)$, the singularity at $z_0$ is <b>removable</b>!\nThus $g(z)$ can be extended to a holomorphic function on the entire disk $D(z_0, \\delta)$.<br><br>\n<b>Step 4: Analyze roots of $g(z)$ at $z_0$</b><br>\n- Case A: $g(z_0) \\ne 0$. Then $\\lim_{z \\to z_0} f(z) = w + \\frac{1}{g(z_0)}$ exists and is finite, meaning $z_0$ was a removable singularity of $f(z)$. Contradiction!\n- Case B: $g(z_0) = 0$ with zero of order $m \\ge 1$. Then $g(z) = (z - z_0)^m h(z)$ with $h(z_0) \\ne 0$, so $f(z) - w = \\frac{1}{(z - z_0)^m h(z)}$ has a pole of order $m$ at $z_0$. Contradiction!<br><br>\nBoth cases contradict that $z_0$ is an essential singularity. Hence the image must be dense in $\\mathbb{C}$. $\\blacksquare$",
      "answer": "Proved: Boundedness of $\\frac{1}{f(z)-w}$ implies removable/pole, contradicting essential singularity."
    },
    {
      "id": "prob-20",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Evaluation of Fresnel Integrals via Sector Contour",
      "statement": "Evaluate the Fresnel integrals $\\int_0^\\infty \\cos(x^2)\\,dx = \\int_0^\\infty \\sin(x^2)\\,dx = \\frac{\\sqrt{2\\pi}}{4}$ by integrating $f(z) = e^{iz^2}$ over an octant sector contour.",
      "solution": "<b>Step 1: Contour setup</b><br>\nConsider $f(z) = e^{iz^2}$ integrated along the sector $\\Gamma$ of radius $R$ from angle $0$ to $\\pi/4$:\n1. Leg 1: $z = x, x \\in [0, R]$ on the real axis.\n2. Leg 2: Circular arc $C_R: z = R e^{i\\theta}, \\theta \\in [0, \\pi/4]$.\n3. Leg 3: Ray $z = r e^{i\\pi/4}, r \\in [R, 0]$.<br>\nSince $e^{iz^2}$ is entire, Cauchy's Theorem gives $\\oint_\\Gamma e^{iz^2}\\,dz = 0$.<br><br>\n<b>Step 2: Circular arc $C_R$ as $R \\to \\infty$</b><br>\nOn $C_R$, $z^2 = R^2 e^{2i\\theta} = R^2(\\cos 2\\theta + i\\sin 2\\theta) \\implies iz^2 = -R^2\\sin 2\\theta + i R^2\\cos 2\\theta$.\n$$|e^{iz^2}| = e^{-R^2 \\sin 2\\theta}$$\nSince $\\sin 2\\theta \\ge \\frac{4\\theta}{\\pi}$ for $\\theta \\in [0, \\pi/4]$ (Jordan's inequality):\n$$\\left| \\int_{C_R} e^{iz^2}\\,dz \\right| \\le R \\int_0^{\\pi/4} e^{-R^2 (4\\theta/\\pi)}\\,d\\theta = R \\frac{\\pi}{4R^2} (1 - e^{-R^2}) \\to 0 \\quad \\text{as } R \\to \\infty$$\n<br><b>Step 3: Ray at $\\pi/4$</b><br>\n$z = r e^{i\\pi/4} \\implies z^2 = r^2 e^{i\\pi/2} = i r^2 \\implies i z^2 = -r^2$, and $dz = e^{i\\pi/4} dr$.\n$$\\int_{\\text{Leg 3}} e^{iz^2}\\,dz = \\int_R^0 e^{-r^2} e^{i\\pi/4}\\,dr = -e^{i\\pi/4} \\int_0^R e^{-r^2}\\,dr \\to -e^{i\\pi/4} \\frac{\\sqrt{\\pi}}{2}$$\n<br><b>Step 4: Sum of integrals</b><br>\n$$\\int_0^\\infty e^{ix^2}\\,dx + 0 - e^{i\\pi/4} \\frac{\\sqrt{\\pi}}{2} = 0 \\implies \\int_0^\\infty (\\cos x^2 + i\\sin x^2)\\,dx = e^{i\\pi/4} \\frac{\\sqrt{\\pi}}{2}$$\nSince $e^{i\\pi/4} = \\frac{\\sqrt{2}}{2} + i\\frac{\\sqrt{2}}{2}$:\n$$\\int_0^\\infty \\cos(x^2)\\,dx = \\frac{\\sqrt{2\\pi}}{4}, \\qquad \\int_0^\\infty \\sin(x^2)\\,dx = \\frac{\\sqrt{2\\pi}}{4}$$",
      "answer": "$\\int_0^\\infty \\cos(x^2)dx = \\int_0^\\infty \\sin(x^2)dx = \\frac{\\sqrt{2\\pi}}{4}$"
    },
    {
      "id": "prob-21",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Mellin-Type Branch Cut Integral via Keyhole Contour",
      "statement": "Evaluate $\\int_0^\\infty \\frac{x^{a-1}}{1 + x}\\,dx = \\frac{\\pi}{\\sin(\\pi a)}$ for $0 < a < 1$ using a keyhole contour around the positive real axis.",
      "solution": "<b>Step 1: Complex extension and branch cut</b><br>\nConsider $f(z) = \\frac{z^{a-1}}{1 + z}$. We choose the branch cut along $[0, \\infty)$ with $0 \\le \\arg z < 2\\pi$.\nPoles: simple pole at $z = -1 = e^{i\\pi}$.<br><br>\n<b>Step 2: Residue at $z = -1$</b><br>\n$$\\text{Res}(f, -1) = \\lim_{z \\to -1} (z + 1) \\frac{z^{a-1}}{1 + z} = (-1)^{a-1} = (e^{i\\pi})^{a-1} = e^{i\\pi(a - 1)} = -e^{i\\pi a}$$\n<br><b>Step 3: Keyhole contour integration</b><br>\nLet the keyhole contour consist of:\n1. Upper edge $L_1$: $z = x + i0^+ \\implies z^{a-1} = x^{a-1}$.\n2. Large circle $C_R$: $|f(z)| \\le \\frac{R^{a-1}}{R - 1} \\implies \\int_{C_R} \\to 0$ as $R \\to \\infty$ since $a < 1$.\n3. Lower edge $L_2$: $z = x - i0^+ \\implies z = x e^{2\\pi i} \\implies z^{a-1} = x^{a-1} e^{2\\pi i (a - 1)} = x^{a-1} e^{2\\pi i a}$.\n4. Small circle $C_\\epsilon$: $|f(z)| \\le \\frac{\\epsilon^{a-1}}{1 - \\epsilon} \\implies \\int_{C_\\epsilon} \\to 0$ as $\\epsilon \\to 0$ since $a > 0$.<br><br>\n<b>Step 4: Combine the edges</b><br>\n$$\\int_0^\\infty \\frac{x^{a-1}}{1 + x}\\,dx - e^{2\\pi i a} \\int_0^\\infty \\frac{x^{a-1}}{1 + x}\\,dx = 2\\pi i\\, \\text{Res}(f, -1)$$\n$$(1 - e^{2\\pi i a}) \\int_0^\\infty \\frac{x^{a-1}}{1 + x}\\,dx = 2\\pi i (-e^{i\\pi a})$$\nDivide both sides by $-e^{i\\pi a}$:\n$$(e^{i\\pi a} - e^{-i\\pi a}) \\int_0^\\infty \\frac{x^{a-1}}{1 + x}\\,dx = 2\\pi i$$\nSince $e^{i\\pi a} - e^{-i\\pi a} = 2i\\sin(\\pi a)$:\n$$2i\\sin(\\pi a) \\int_0^\\infty \\frac{x^{a-1}}{1 + x}\\,dx = 2\\pi i \\implies \\int_0^\\infty \\frac{x^{a-1}}{1 + x}\\,dx = \\frac{\\pi}{\\sin(\\pi a)}$$",
      "answer": "$\\int_0^\\infty \\frac{x^{a-1}}{1 + x}\\,dx = \\frac{\\pi}{\\sin(\\pi a)}$"
    },
    {
      "id": "prob-22",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Schwarz-Pick Lemma & Hyperbolic Automorphisms of Unit Disk",
      "statement": "Prove the Schwarz-Pick Lemma: For any holomorphic self-map $f: \\mathbb{D} \\to \\mathbb{D}$ of the unit disk, $\\left|\\frac{f'(z)}{1 - |f(z)|^2}\\right| \\le \\frac{1}{1 - |z|^2}$.",
      "solution": "<b>Step 1: Automorphisms of the unit disk $\\mathbb{D}$</b><br>\nFor any point $\\alpha \\in \\mathbb{D}$, the Blaschke factor:\n$$\\phi_\\alpha(z) = \\frac{z - \\alpha}{1 - \\bar{\\alpha} z}$$\nis a holomorphic bijection from $\\mathbb{D}$ to $\\mathbb{D}$ with $\\phi_\\alpha(\\alpha) = 0$ and $\\phi_\\alpha^{-1}(w) = \\phi_{-\\alpha}(w)$.<br><br>\n<b>Step 2: Composition with Blaschke factors</b><br>\nFix $z_0 \\in \\mathbb{D}$ and let $w_0 = f(z_0) \\in \\mathbb{D}$. Define the composite map:\n$$F(z) = (\\phi_{w_0} \\circ f \\circ \\phi_{-z_0})(z)$$\nNotice that $F(0) = \\phi_{w_0}(f(\\phi_{-z_0}(0))) = \\phi_{w_0}(f(z_0)) = \\phi_{w_0}(w_0) = 0$.\nSince $\\phi_{w_0}$ and $\\phi_{-z_0}$ map $\\mathbb{D}$ into $\\mathbb{D}$, $F: \\mathbb{D} \\to \\mathbb{D}$.<br><br>\n<b>Step 3: Apply Schwarz's Lemma</b><br>\nBy Schwarz's Lemma (Theorem 4.7), $|F'(0)| \\le 1$.<br>\nUsing the chain rule:\n$$F'(0) = \\phi_{w_0}'(w_0) \\cdot f'(z_0) \\cdot \\phi_{-z_0}'(0)$$\nCompute derivatives of Blaschke factors:\n$$\\phi_\\alpha'(z) = \\frac{(1 - \\bar{\\alpha} z)(1) - (z - \\alpha)(-\\bar{\\alpha})}{(1 - \\bar{\\alpha} z)^2} = \\frac{1 - |\\alpha|^2}{(1 - \\bar{\\alpha} z)^2}$$\nAt $z = \\alpha$: $\\phi_{w_0}'(w_0) = \\frac{1 - |w_0|^2}{(1 - |w_0|^2)^2} = \\frac{1}{1 - |w_0|^2} = \\frac{1}{1 - |f(z_0)|^2}$.<br>\nAt $z = 0$: $\\phi_{-z_0}'(0) = 1 - |-z_0|^2 = 1 - |z_0|^2$.<br><br>\n<b>Step 4: Combine into $|F'(0)| \\le 1$</b><br>\n$$|F'(0)| = \\frac{1}{1 - |f(z_0)|^2} \\cdot |f'(z_0)| \\cdot (1 - |z_0|^2) \\le 1 \\implies \\frac{|f'(z_0)|}{1 - |f(z_0)|^2} \\le \\frac{1}{1 - |z_0|^2}$$\nThis proves that every holomorphic self-map of the unit disk is a contraction with respect to the Poincaré hyperbolic metric $ds = \\frac{|dz|}{1 - |z|^2}$! $\\blacksquare$",
      "answer": "Proved: $\\frac{|f'(z)|}{1 - |f(z)|^2} \\le \\frac{1}{1 - |z|^2}$ (Poincaré Hyperbolic Contraction)."
    },
    {
      "id": "prob-23",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Joukowsky Transformation & Trailing Edge Singularity Analysis",
      "statement": "For the Joukowsky map $w = z + \\frac{c^2}{z}$ ($c > 0$), prove that a circle $C$ passing through $z = -c$ and containing $z = c$ is mapped onto a streamlined airfoil profile with a cusped trailing edge of interior angle zero.",
      "solution": "<b>Step 1: Derivative and critical points</b><br>\n$$\\frac{dw}{dz} = 1 - \\frac{c^2}{z^2} = \\frac{z^2 - c^2}{z^2} = \\frac{(z - c)(z + c)}{z^2}$$\nThe critical points where $w'(z) = 0$ are $z = c$ and $z = -c$.<br><br>\n<b>Step 2: Circle through $z = -c$</b><br>\nLet $C$ be a circle centered at $z_0 = -\\mu + i\\eta$ ($\\mu > 0, \\eta > 0$) with radius $R = |z_0 - (-c)|$ so that $z = -c$ lies on $C$, and $z = c$ lies strictly inside $C$.\nAt $z = -c$, $w(-c) = -c - c = -2c$, which forms the <b>trailing edge</b> of the airfoil.<br><br>\n<b>Step 3: Expansion near the critical point $z = -c$</b><br>\nLet $z = -c + \\Delta z$.\n$$w(z) = (-c + \\Delta z) + \\frac{c^2}{-c + \\Delta z} = -c + \\Delta z - c \\left(1 + \\frac{\\Delta z}{c} + \\frac{(\\Delta z)^2}{c^2} + \\dots\\right)$$\n$$= -2c + \\frac{(\\Delta z)^2}{c} + O((\\Delta z)^3)$$\nNotice that the linear term $\\Delta z$ is absent!\n$$w - (-2c) \\approx \\frac{1}{c} (\\Delta z)^2$$\n<br><b>Step 4: Angle doubling and cusped trailing edge</b><br>\nTaking the argument:\n$$\\arg(w + 2c) \\approx 2 \\arg(\\Delta z)$$\nAs the circle $C$ passes smoothly through $z = -c$, the tangent vector has angle difference $\\pi$ between arriving and departing branches.\nMultiplying by 2 maps the angle $\\pi$ to $2\\pi$!\nThis wraps the upper and lower surfaces together tangentially, creating a <b>sharp cusp</b> (interior angle $0^\\circ$) at the trailing edge $w = -2c$. This geometric property satisfies the physical Kutta condition of fluid circulation!",
      "answer": "Proved: $w + 2c \\approx \\frac{(\\Delta z)^2}{c}$ doubles the angle, forming a cusp at trailing edge $w = -2c$."
    },
    {
      "id": "prob-24",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Analytic Continuation & Euler's Reflection Formula for Gamma Function",
      "statement": "Derive Euler's reflection formula $\\Gamma(z)\\Gamma(1 - z) = \\frac{\\pi}{\\sin(\\pi z)}$ via contour integration.",
      "solution": "<b>Step 1: Relation to the Beta Function</b><br>\nFrom Euler's integral definitions for $0 < \\text{Re}(z) < 1$:\n$$B(z, 1 - z) = \\frac{\\Gamma(z)\\Gamma(1 - z)}{\\Gamma(z + 1 - z)} = \\frac{\\Gamma(z)\\Gamma(1 - z)}{\\Gamma(1)} = \\Gamma(z)\\Gamma(1 - z)$$\n<br><b>Step 2: Integral representation of Beta function</b><br>\n$$B(z, 1 - z) = \\int_0^1 t^{z - 1} (1 - t)^{-z}\\,dt$$\nSubstitute $t = \\frac{x}{1 + x} \\implies 1 - t = \\frac{1}{1 + x}$ and $dt = \\frac{dx}{(1 + x)^2}$:\n$$B(z, 1 - z) = \\int_0^\\infty \\left( \\frac{x}{1 + x} \\right)^{z - 1} \\left( \\frac{1}{1 + x} \\right)^{-z} \\frac{dx}{(1 + x)^2} = \\int_0^\\infty \\frac{x^{z - 1}}{1 + x}\\,dx$$\n<br><b>Step 3: Evaluate integral via Problem 21</b><br>\nIn Problem 21, we proved rigorously via keyhole contour integration that for any $0 < \\text{Re}(z) < 1$:\n$$\\int_0^\\infty \\frac{x^{z - 1}}{1 + x}\\,dx = \\frac{\\pi}{\\sin(\\pi z)}$$\nTherefore:\n$$\\Gamma(z)\\Gamma(1 - z) = \\frac{\\pi}{\\sin(\\pi z)} \\quad \\text{for } 0 < \\text{Re}(z) < 1$$\n<br><b>Step 4: Analytic Continuation to $\\mathbb{C} \\setminus \\mathbb{Z}$</b><br>\nBoth $\\Gamma(z)\\Gamma(1 - z)$ and $\\frac{\\pi}{\\sin(\\pi z)}$ are meromorphic functions on $\\mathbb{C}$ with simple poles at every integer $z = n \\in \\mathbb{Z}$.\nSince they agree on the vertical strip $0 < \\text{Re}(z) < 1$, by the Identity Theorem for meromorphic functions, the reflection identity holds for all $z \\in \\mathbb{C} \\setminus \\mathbb{Z}$! $\\blacksquare$",
      "answer": "$\\Gamma(z)\\Gamma(1 - z) = \\frac{\\pi}{\\sin(\\pi z)}$ for all $z \\in \\mathbb{C} \\setminus \\mathbb{Z}$."
    }
  ]
};
window.BOOK_DATA = window.COURSE_DATA;
