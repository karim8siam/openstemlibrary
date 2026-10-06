window.COURSE_DATA = {
  "courseId": "geometry-2d",
  "courseTitle": "Two-Dimensional Coordinate Geometry & Conic Sections: Systems of Coordinates, Pairs of Lines, Circles & Conics",
  "courseDescription": "An exhaustive, university honors-level digital textbook and interactive geometric laboratory covering plane coordinate geometry and conic sections: Part A establishes analytical coordinate transformations, straight line pairs, and circular systems across four units (Cartesian metric space axioms, distance and section formulas, harmonic ranges, Euler line, shoelace polygon areas, polar coordinates, translation and rotation of axes via SO(2) orthogonal matrices, and quadratic invariants; homogeneous second-degree line pairs ax\u00b2 + 2hxy + by\u00b2 = 0, reality discriminant, angle between lines tan \u03b8 = 2\u221a(h\u00b2 - ab)/(a + b), perpendicularity (a + b = 0), joint angle bisectors (x\u00b2 - y\u00b2)/(a - b) = xy/h, general second-degree line pairs via \u0394 = 0, intersection points, parallel line distance, and the homogenization theorem; standard, general, and diametric circles, tangency conditions, slope equations, Joachimsthal's pair of tangents SS\u2081 = T\u00b2, chord of contact, reciprocal pole/polar theory, radical axis S\u2081 - S\u2082 = 0, radical center, orthogonal circles 2g\u2081g\u2082 + 2f\u2081f\u2082 = c\u2081 + c\u2082, and coaxial circle systems with limiting points). Part B presents the complete theory of conic sections across four comprehensive units (general second-degree equation x^T A x = 0, rigid motion invariants I\u2081, I\u2082, I\u2083 = \u0394, classification taxonomy, center determination, eigenvalue canonical reduction \u03bb\u2081X\u00b2 + \u03bb\u2082Y\u00b2 + \u0394/D = 0, and non-central parabolic reduction Y'\u00b2 = 4AX'; in-depth study of the parabola y\u00b2 = 4ax, parametric form (at\u00b2, 2at), focal chord theorem t\u2081t\u2082 = -1, tangents, intersection of tangents, orthoptic directrix property, co-normal points, optical reflection property, and constant subnormal 2a; in-depth study of the ellipse x\u00b2/a\u00b2 + y\u00b2/b\u00b2 = 1, focal sum SP + S'P = 2a, auxiliary circle, eccentric angle, director circle x\u00b2 + y\u00b2 = a\u00b2 + b\u00b2, conjugate diameters and Apollonius' theorems CP\u00b2 + CD\u00b2 = a\u00b2 + b\u00b2 and area = 4ab, optical reflection, and focal perpendicular product p\u2081p\u2082 = b\u00b2; in-depth study of the hyperbola x\u00b2/a\u00b2 - y\u00b2/b\u00b2 = 1, focal difference |S'P - SP| = 2a, asymptotes y = \u00b1(b/a)x, conjugate hyperbola 1/e\u2081\u00b2 + 1/e\u2082\u00b2 = 1, director circle x\u00b2 + y\u00b2 = a\u00b2 - b\u00b2, rectangular hyperbola x\u00b2 - y\u00b2 = a\u00b2 with e = \u221a2, rotation to asymptotic canonical form xy = c\u00b2, and constant tangent-asymptote triangle area 2c\u00b2; universal polar conic equation l/r = 1 + e cos \u03b8 with focus at pole, unified eccentricity morphing, periapsis/apoapsis, polar tangents l/r = e cos \u03b8 + cos(\u03b8 - \u03b1), confocal orthogonal conics, and celestial orbital mechanics via Binet's equation and vis-viva energy). Accompanied by 8 interactive 60 FPS geometric canvas calculators and 24 tiered solved university examination problems.",
  "units": [
    {
      "unitNumber": 1,
      "number": 1,
      "title": "Cartesian & Polar Coordinate Systems, Distances & Transformations",
      "description": "Comprehensive analytical foundations of two-dimensional coordinate geometry: Cartesian metric space axioms, distance and section formulas, harmonic ranges, triangle centers and the Euler line, shoelace polygon area determinants, polar coordinates and metric relations, translation of axes and curve transformations, rotation of axes via SO(2) orthogonal matrices, and fundamental quadratic invariants.",
      "sections": [
        {
          "id": "u1-sec1",
          "title": "Foundations of the Cartesian Plane, Distance Metrics & Section Formulas",
          "content": "\n<h3>1. The Cartesian Coordinate System & Metric Geometry</h3>\n<p>\nThe foundation of analytic geometry, pioneered by Ren\u00e9 Descartes and Pierre de Fermat, establishes a bijective correspondence between the Euclidean plane $\\mathbb{E}^2$ and the Cartesian product of the real field $\\mathbb{R}^2 = \\mathbb{R} \\times \\mathbb{R}$. Any point $P \\in \\mathbb{E}^2$ is uniquely identified by an ordered pair of real coordinates $(x, y)$, representing signed perpendicular distances from two mutually orthogonal directed axes: the horizontal abscissa ($x$-axis) and the vertical ordinate ($y$-axis).\n</p>\n<p>\nUnder the standard Euclidean metric tensor $g_{ij} = \\delta_{ij}$, the fundamental distance $d(P_1, P_2)$ between two points $P_1(x_1, y_1)$ and $P_2(x_2, y_2)$ is established directly via the Pythagorean theorem:\n$$d(P_1, P_2) = \\|\\mathbf{r}_2 - \\mathbf{r}_1\\|_2 = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$\nThis Euclidean metric satisfies the three formal metric space axioms:\n<ul>\n  <li><strong>Positive Definiteness:</strong> $d(P_1, P_2) \\ge 0$, with $d(P_1, P_2) = 0 \\iff P_1 = P_2$.</li>\n  <li><strong>Symmetry:</strong> $d(P_1, P_2) = d(P_2, P_1)$ for all $P_1, P_2 \\in \\mathbb{R}^2$.</li>\n  <li><strong>Triangle Inequality:</strong> $d(P_1, P_3) \\le d(P_1, P_2) + d(P_2, P_3)$, with equality holding if and only if $P_2$ lies on the straight segment $\\overline{P_1 P_3}$.</li>\n</ul>\n</p>\n\n<h3>2. The General Section Formula (Internal and External Division)</h3>\n<p>\nLet $P_1(x_1, y_1)$ and $P_2(x_2, y_2)$ be two distinct points in $\\mathbb{R}^2$. A point $P(x, y)$ dividing the directed line segment $P_1 P_2$ in the ratio $m : n$ satisfies the vector relationship:\n$$\\frac{\\vec{P_1 P}}{\\vec{P P_2}} = \\frac{m}{n} \\iff n(\\mathbf{r} - \\mathbf{r}_1) = m(\\mathbf{r}_2 - \\mathbf{r})$$\nSolving for the position vector $\\mathbf{r} = (x, y)$:\n$$\\mathbf{r} = \\frac{m \\mathbf{r}_2 + n \\mathbf{r}_1}{m + n}$$\nIn scalar Cartesian components:\n$$x = \\frac{m x_2 + n x_1}{m + n}, \\qquad y = \\frac{m y_2 + n y_1}{m + n}$$\n</p>\n<p>\n<strong>Classification of Division:</strong>\n<ul>\n  <li><strong>Internal Division ($m/n > 0$):</strong> The point $P$ lies strictly between $P_1$ and $P_2$. When $m = n = 1$, $P$ is the <em>midpoint</em>:\n  $$M = \\left(\\frac{x_1 + x_2}{2}, \\frac{y_1 + y_2}{2}\\right)$$</li>\n  <li><strong>External Division ($m/n < 0$, with $m \\ne -n$):</strong> Setting the ratio as $m : -n$, the point $P_{\\text{ext}}$ lies on the extension of line segment $P_1 P_2$:\n  $$x_{\\text{ext}} = \\frac{m x_2 - n x_1}{m - n}, \\qquad y_{\\text{ext}} = \\frac{m y_2 - n y_1}{m - n}$$</li>\n  <li><strong>Harmonic Conjugates:</strong> The points $P_{\\text{int}}$ and $P_{\\text{ext}}$ dividing $P_1 P_2$ internally and externally in the same absolute ratio $m:n$ form a <em>harmonic range</em> $(P_1, P_2; P_{\\text{int}}, P_{\\text{ext}}) = -1$, meaning their distances satisfy the classical harmonic mean relation:\n  $$\\frac{2}{P_1 P_2} = \\frac{1}{P_1 P_{\\text{int}}} + \\frac{1}{P_1 P_{\\text{ext}}}$$</li>\n</ul>\n</p>\n\n<h3>3. Classic Triangle Centers in the Cartesian Plane</h3>\n<p>\nFor a triangle $\\triangle ABC$ with vertices $A(x_1, y_1)$, $B(x_2, y_2)$, $C(x_3, y_3)$ and opposite side lengths $a = BC, b = CA, c = AB$:\n<ul>\n  <li><strong>Centroid ($G$):</strong> The concurrence point of the three medians, dividing each median in ratio $2:1$:\n  $$G = \\left(\\frac{x_1 + x_2 + x_3}{3}, \\frac{y_1 + y_2 + y_3}{3}\\right)$$</li>\n  <li><strong>Incenter ($I$):</strong> The center of the inscribed circle, concurrence of internal angle bisectors:\n  $$I = \\left(\\frac{a x_1 + b x_2 + c x_3}{a + b + c}, \\frac{a y_1 + b y_2 + c y_3}{a + b + c}\\right)$$</li>\n  <li><strong>Excenters ($I_a, I_b, I_c$):</strong> Centers of the three excircles. The excenter opposite to vertex $A$ is:\n  $$I_a = \\left(\\frac{-a x_1 + b x_2 + c x_3}{-a + b + c}, \\frac{-a y_1 + b y_2 + c y_3}{-a + b + c}\\right)$$</li>\n  <li><strong>Euler Line Theorem:</strong> In any non-equilateral triangle, the orthocenter $H$, centroid $G$, and circumcenter $O$ are strictly collinear, satisfying the constant harmonic segment ratio:\n  $$OG : GH = 1 : 2 \\iff \\mathbf{r}_H = 3\\mathbf{r}_G - 2\\mathbf{r}_O$$</li>\n</ul>\n</p>\n"
        },
        {
          "id": "u1-sec2",
          "title": "Area of Polygons, Collinearity & The Shoelace Determinant",
          "content": "\n<h3>1. Determinant Formulation for the Area of a Triangle</h3>\n<p>\nConsider a triangle $\\triangle ABC$ formed by non-collinear vertices $A(x_1, y_1)$, $B(x_2, y_2)$, and $C(x_3, y_3)$ arranged counterclockwise. The signed area $\\mathcal{A}$ is given by the cross product of the edge vectors $\\vec{AB} = (x_2 - x_1, y_2 - y_1)$ and $\\vec{AC} = (x_3 - x_1, y_3 - y_1)$:\n$$\\mathcal{A} = \\frac{1}{2} \\left[ (x_2 - x_1)(y_3 - y_1) - (x_3 - x_1)(y_2 - y_1) \\right]$$\nExpanding this algebraic expression yields the celebrated $3 \\times 3$ determinant formulation:\n$$\\mathcal{A} = \\frac{1}{2} \\begin{vmatrix} x_1 & y_1 & 1 \\\\ x_2 & y_2 & 1 \\\\ x_3 & y_3 & 1 \\end{vmatrix} = \\frac{1}{2} \\left[ x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2) \\right]$$\nThe physical unsigned area is given by the absolute value $|\\mathcal{A}|$.\n</p>\n\n<h3>2. The Exact Criterion for Collinearity</h3>\n<p>\nThree distinct points $A(x_1, y_1)$, $B(x_2, y_2)$, $C(x_3, y_3)$ lie on a common straight line if and only if the triangle they span degenerates into a segment with zero area:\n$$\\text{Collinear} \\iff \\begin{vmatrix} x_1 & y_1 & 1 \\\\ x_2 & y_2 & 1 \\\\ x_3 & y_3 & 1 \\end{vmatrix} = 0 \\iff x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2) = 0$$\nAlternatively, collinearity is characterized by equal slopes:\n$$m_{AB} = m_{BC} \\iff \\frac{y_2 - y_1}{x_2 - x_1} = \\frac{y_3 - y_2}{x_3 - x_2} \\quad (x_1 \\ne x_2 \\ne x_3)$$\n</p>\n\n<h3>3. The Shoelace Formula for General Simple Polygons</h3>\n<p>\nBy applying Green's Theorem $\\iint_D dA = \\frac{1}{2} \\oint_{\\partial D} (x \\, dy - y \\, dx)$ to a planar polygonal domain bounded by $n$ ordered vertices $P_1(x_1, y_1), P_2(x_2, y_2), \\dots, P_n(x_n, y_n)$ traversed counterclockwise, the exact area is given by the <strong>Shoelace Formula</strong>:\n$$\\mathcal{A}_n = \\frac{1}{2} \\left| \\sum_{i=1}^{n} (x_i y_{i+1} - x_{i+1} y_i) \\right| = \\frac{1}{2} \\left| (x_1 y_2 + x_2 y_3 + \\dots + x_n y_1) - (y_1 x_2 + y_2 x_3 + \\dots + y_n x_1) \\right|$$\nwhere cyclic indexing applies such that $(x_{n+1}, y_{n+1}) \\equiv (x_1, y_1)$.\n</p>\n"
        },
        {
          "id": "u1-sec3",
          "title": "The Polar Coordinate System & Metric Geometry",
          "content": "\n<h3>1. Coordinate Definition & Bijective Transitions</h3>\n<p>\nIn the <strong>polar coordinate system</strong>, a point $P$ in the Euclidean plane is specified relative to a fixed origin $O$ (termed the <em>pole</em>) and a horizontal directed ray extending to the right (the <em>polar axis</em>). The point is denoted by the ordered pair $(r, \\theta)$:\n<ul>\n  <li><strong>Radial Coordinate ($r$):</strong> The directed Euclidean distance from pole $O$ to point $P$, $r \\in [0, \\infty)$.</li>\n  <li><strong>Angular Coordinate ($\\theta$):</strong> The counterclockwise angle measured from the polar axis to the ray $OP$, $\\theta \\in (-\\pi, \\pi]$ or $\\theta \\in [0, 2\\pi)$.</li>\n</ul>\n</p>\n<p>\nThe exact bijective conversion between Cartesian $(x, y)$ and Polar $(r, \\theta)$ representations is given by:\n$$\\begin{cases} x = r \\cos \\theta \\\\ y = r \\sin \\theta \\end{cases} \\iff \\begin{cases} r = \\sqrt{x^2 + y^2} \\\\ \\theta = \\operatorname{atan2}(y, x) \\end{cases}$$\nwhere $\\operatorname{atan2}(y, x)$ resolves the proper quadrant of $\\theta$ without ambiguity:\n$$\\operatorname{atan2}(y, x) = \\begin{cases} \\arctan(y/x) & x > 0 \\\\ \\arctan(y/x) + \\pi & x < 0, \\, y \\ge 0 \\\\ \\arctan(y/x) - \\pi & x < 0, \\, y < 0 \\\\ +\\pi/2 & x = 0, \\, y > 0 \\\\ -\\pi/2 & x = 0, \\, y < 0 \\\\ \\text{undefined} & x = 0, \\, y = 0 \\end{cases}$$\n</p>\n\n<h3>2. Distance Formula & Triangle Area in Polar Form</h3>\n<p>\nLet $P_1(r_1, \\theta_1)$ and $P_2(r_2, \\theta_2)$ be two points expressed in polar coordinates. In $\\triangle O P_1 P_2$, the angle subtended at the pole is $|\\theta_2 - \\theta_1|$. By the Law of Cosines:\n$$d(P_1, P_2)^2 = r_1^2 + r_2^2 - 2 r_1 r_2 \\cos(\\theta_2 - \\theta_1)$$\n$$d(P_1, P_2) = \\sqrt{r_1^2 + r_2^2 - 2 r_1 r_2 \\cos(\\theta_2 - \\theta_1)}$$\n</p>\n<p>\nThe area of the triangle $\\triangle O P_1 P_2$ formed by the pole and the two points is:\n$$\\mathcal{A}_{\\triangle O P_1 P_2} = \\frac{1}{2} r_1 r_2 \\sin|\\theta_2 - \\theta_1|$$\nFor three arbitrary points $P_1(r_1, \\theta_1), P_2(r_2, \\theta_2), P_3(r_3, \\theta_3)$, the enclosed area is:\n$$\\mathcal{A} = \\frac{1}{2} \\left| r_1 r_2 \\sin(\\theta_2 - \\theta_1) + r_2 r_3 \\sin(\\theta_3 - \\theta_2) + r_3 r_1 \\sin(\\theta_1 - \\theta_3) \\right|$$\n</p>\n"
        },
        {
          "id": "u1-sec4",
          "title": "Translation of Coordinate Axes & Origin Shifting",
          "content": "\n<h3>1. Algebraic Mechanics of Axis Translation</h3>\n<p>\nIn many analytical geometric investigations, the mathematical form of a curve simplifies dramatically when the origin of coordinates is shifted to a new point $O'(h, k)$ while maintaining the parallel orientation and direction of the axes.\n</p>\n<p>\nLet $(x, y)$ denote the coordinates of a point $P$ referred to the original axes $Ox, Oy$, and let $(X, Y)$ denote the coordinates of the same physical point $P$ referred to the translated axes $O'X, O'Y$. From vector addition:\n$$\\mathbf{r} = \\mathbf{r}_{O'} + \\mathbf{r}' \\implies \\begin{pmatrix} x \\\\ y \\end{pmatrix} = \\begin{pmatrix} X + h \\\\ Y + k \\end{pmatrix}$$\nConversely, the new coordinates in terms of the old are:\n$$\\begin{cases} X = x - h \\\\ Y = y - k \\end{cases}$$\n</p>\n\n<h3>2. Transformation of Algebraic Curves</h3>\n<p>\nGiven a planar curve described by the implicit polynomial equation $f(x, y) = 0$, its transformed equation in the new coordinate frame $(X, Y)$ is obtained by direct substitution:\n$$F(X, Y) = f(X + h, Y + k) = 0$$\n</p>\n<p>\n<strong>Invariance Under Pure Translation:</strong>\n<ul>\n  <li><strong>Distance Invariance:</strong> $d(P_1, P_2) = \\sqrt{(X_2 - X_1)^2 + (Y_2 - Y_1)^2} = \\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.</li>\n  <li><strong>Slope Invariance:</strong> $M = \\frac{Y_2 - Y_1}{X_2 - X_1} = \\frac{(y_2 - k) - (y_1 - k)}{(x_2 - h) - (x_1 - h)} = \\frac{y_2 - y_1}{x_2 - x_1} = m$.</li>\n  <li><strong>Angle & Area Invariance:</strong> Translation preserves all angles between intersecting curves and all enclosed polygonal and curvilinear areas.</li>\n  <li><strong>Second-Degree Coefficient Invariance:</strong> In the general second-degree equation $a x^2 + 2h xy + b y^2 + 2g x + 2f y + c = 0$, pure translation changes only the linear terms ($g, f$) and the constant $c$, leaving the second-degree quadratic coefficients $a, h, b$ strictly invariant!</li>\n</ul>\n</p>\n"
        },
        {
          "id": "u1-sec5",
          "title": "Rotation of Axes & General Rigid Euclidean Motion",
          "content": "\n<h3>1. Mathematical Formulation of Axis Rotation</h3>\n<p>\nLet the Cartesian axes $Ox, Oy$ be rotated counterclockwise through an angle $\\theta$ about the fixed origin $O$ to a new coordinate system $OX, OY$.\nLet a point $P$ have polar coordinates $(r, \\phi)$ with respect to the original system, so that $x = r \\cos \\phi$ and $y = r \\sin \\phi$.\nIn the rotated system, the distance $r$ remains unchanged, but the angle from the $OX$-axis to $OP$ is $\\phi - \\theta$. Therefore:\n$$X = r \\cos(\\phi - \\theta) = r \\cos \\phi \\cos \\theta + r \\sin \\phi \\sin \\theta = x \\cos \\theta + y \\sin \\theta$$\n$$Y = r \\sin(\\phi - \\theta) = r \\sin \\phi \\cos \\theta - r \\cos \\phi \\sin \\theta = -x \\sin \\theta + y \\cos \\theta$$\nInverting these linear relations gives the old coordinates $(x, y)$ in terms of the new coordinates $(X, Y)$:\n$$\\begin{pmatrix} x \\\\ y \\end{pmatrix} = \\begin{pmatrix} \\cos \\theta & -\\sin \\theta \\\\ \\sin \\theta & \\cos \\theta \\end{pmatrix} \\begin{pmatrix} X \\\\ Y \\end{pmatrix} \\iff \\begin{cases} x = X \\cos \\theta - Y \\sin \\theta \\\\ y = X \\sin \\theta + Y \\cos \\theta \\end{cases}$$\nThe transformation matrix:\n$$\\mathbf{R}(\\theta) = \\begin{pmatrix} \\cos \\theta & -\\sin \\theta \\\\ \\sin \\theta & \\cos \\theta \\end{pmatrix}$$\nis a special orthogonal matrix belonging to the Lie group $\\mathrm{SO}(2)$, satisfying $\\mathbf{R}^T \\mathbf{R} = \\mathbf{I}$ and $\\det \\mathbf{R} = +1$.\n</p>\n\n<h3>2. The Elimination of the Cross-Product Term ($xy$)</h3>\n<p>\nUnder rotation of axes through an angle $\\theta$, the general second-degree form $a x^2 + 2h xy + b y^2$ transforms into $A X^2 + 2H XY + B Y^2$.\nExpanding and grouping terms:\n$$A = a \\cos^2 \\theta + 2h \\sin \\theta \\cos \\theta + b \\sin^2 \\theta$$\n$$B = a \\sin^2 \\theta - 2h \\sin \\theta \\cos \\theta + b \\cos^2 \\theta$$\n$$2H = 2(b - a)\\sin \\theta \\cos \\theta + 2h(\\cos^2 \\theta - \\sin^2 \\theta) = (b - a)\\sin 2\\theta + 2h \\cos 2\\theta$$\nTo eliminate the cross-product term $XY$, we require $H = 0$:\n$$(b - a)\\sin 2\\theta + 2h \\cos 2\\theta = 0 \\iff (a - b)\\sin 2\\theta = 2h \\cos 2\\theta$$\n$$\\tan 2\\theta = \\frac{2h}{a - b} \\quad (a \\ne b), \\qquad \\text{or } \\theta = \\frac{\\pi}{4} \\quad (a = b)$$\nThis fundamental relation is the cornerstone of conic canonical reduction!\n</p>\n\n<h3>3. Rotational Invariants of Quadratic Forms</h3>\n<p>\nFor any rotation of axes, the coefficients of the quadratic form satisfy two algebraic invariants:\n$$\\mathbf{Invariant \\; 1:} \\quad A + B = a + b \\quad (\\text{Trace of the matrix})$$\n$$\\mathbf{Invariant \\; 2:} \\quad AB - H^2 = ab - h^2 \\quad (\\text{Determinant of the matrix})$$\nThese invariants ensure that the geometric nature of the quadratic curve (ellipse, parabola, or hyperbola) is an intrinsic property of the curve, independent of the choice of coordinate axes!\n</p>\n",
          "simulation": "geom2d-coord-transform-sim",
          "simulations": [
            "geom2d-coord-transform-sim"
          ]
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "Collinearity and Harmonic Division of a Line Segment",
          "statement": "Given three points $A(-3, -2)$, $B(1, 4)$, and $C(5, 10)$: (a) Prove that the points are collinear using the determinant condition. (b) Find the ratio in which point $B$ divides the line segment $AC$. (c) Determine the coordinates of the harmonic conjugate point $D$ that divides $AC$ externally in the same ratio.",
          "steps": [
            {
              "step": "Step 1: Verify Collinearity via Determinant",
              "math": "\\Delta = \\begin{vmatrix} -3 & -2 & 1 \\\\ 1 & 4 & 1 \\\\ 5 & 10 & 1 \\end{vmatrix} = -3(4 - 10) - (-2)(1 - 5) + 1(10 - 20) = -3(-6) + 2(-4) + 1(-10) = 18 - 8 - 10 = 0",
              "explanation": "Since the determinant vanishes identically, $\\Delta = 0$, the points $A, B, C$ are strictly collinear."
            },
            {
              "step": "Step 2: Determine Division Ratio $m:n$",
              "math": "x_B = \\frac{m x_C + n x_A}{m + n} \\implies 1 = \\frac{5m - 3n}{m + n} \\implies m + n = 5m - 3n \\implies 4m = 4n \\implies \\frac{m}{n} = 1",
              "explanation": "Thus $B$ divides $AC$ internally in the ratio $1 : 1$, which means $B$ is the exact midpoint of $AC$ ($y$-coordinate check: $\\frac{10 + (-2)}{2} = 4 = y_B$)."
            },
            {
              "step": "Step 3: Find Harmonic Conjugate $D$ (External Division)",
              "math": "\\text{For ratio } 1 : 1, \\quad m - n = 0 \\implies D \\text{ lies at the point at infinity along the line } AC",
              "explanation": "When an internal point is the exact midpoint ($1:1$), its harmonic conjugate lies at the line's point at infinity: $(A, C; B, D_{\\infty}) = -1$."
            }
          ],
          "answer": "\\Delta = 0 \\implies \\text{Collinear}; \\quad \\text{Internal Ratio } = 1 : 1 \\text{ (Midpoint)}; \\quad \\text{Harmonic Conjugate } D = \\text{Point at infinity along } AC"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "Area of Triangle and Metric Distance in Polar Coordinates",
          "statement": "Two points in the polar coordinate plane are given by $P_1\\left(6, \\frac{\\pi}{6}\\right)$ and $P_2\\left(8, \\frac{\\pi}{2}\\right)$, and the pole is $O(0, 0)$. (a) Compute the exact Euclidean distance $d(P_1, P_2)$. (b) Calculate the exact area of the triangle $\\triangle O P_1 P_2$. (c) Find the polar equation of the circumcircle of $\\triangle O P_1 P_2$.",
          "steps": [
            {
              "step": "Step 1: Compute Polar Distance",
              "math": "d^2 = r_1^2 + r_2^2 - 2 r_1 r_2 \\cos(\\theta_2 - \\theta_1) = 6^2 + 8^2 - 2(6)(8)\\cos\\left(\\frac{\\pi}{2} - \\frac{\\pi}{6}\\right) = 36 + 64 - 96 \\cos\\left(\\frac{\\pi}{3}\\right)",
              "explanation": "Using $\\cos(\\pi/3) = 1/2$: $d^2 = 100 - 96(0.5) = 100 - 48 = 52 \\implies d = \\sqrt{52} = 2\\sqrt{13}$."
            },
            {
              "step": "Step 2: Calculate Area of Triangle $\triangle O P_1 P_2$",
              "math": "\\mathcal{A} = \\frac{1}{2} r_1 r_2 \\sin(\\theta_2 - \\theta_1) = \\frac{1}{2}(6)(8)\\sin\\left(\\frac{\\pi}{3}\\right) = 24 \\left(\\frac{\\sqrt{3}}{2}\\right) = 12\\sqrt{3}",
              "explanation": "The exact area of the polar triangle is $12\\sqrt{3}$ square units."
            },
            {
              "step": "Step 3: Circumcircle Polar Equation",
              "math": "\\text{Cartesian coords: } P_1 = (6\\cos 30^\\circ, 6\\sin 30^\\circ) = (3\\sqrt{3}, 3), \\quad P_2 = (0, 8), \\quad O = (0, 0) \\\\ \\text{Circle through } O, P_1, P_2: x^2 + y^2 - 3\\sqrt{3}x - 8y = 0 \\implies r^2 - r(3\\sqrt{3}\\cos\\theta + 8\\sin\\theta) = 0 \\implies r = 3\\sqrt{3}\\cos\\theta + 8\\sin\\theta",
              "explanation": "Dividing by $r \ne 0$ yields the polar equation of the circle passing through the origin."
            }
          ],
          "answer": "d(P_1, P_2) = 2\\sqrt{13}; \\quad \\mathcal{A} = 12\\sqrt{3}; \\quad \\text{Circumcircle: } r = 3\\sqrt{3}\\cos\\theta + 8\\sin\\theta"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "Complete Rigid Euclidean Transformation Eliminating Linear and Cross Terms",
          "statement": "Consider the second-degree curve equation $17x^2 - 12xy + 8y^2 + 46x - 28y + 17 = 0$. (a) Determine the translation $(h, k)$ that eliminates the linear first-degree terms. (b) Find the exact counterclockwise rotation angle $\\theta$ that eliminates the cross-product $XY$ term. (c) Write the canonical standard form of the curve and identify its geometric nature.",
          "steps": [
            {
              "step": "Step 1: Determine the Center $(h, k)$ via Partial Derivatives",
              "math": "F_x = 34x - 12y + 46 = 0 \\implies 17h - 6k = -23 \\\\ F_y = -12x + 16y - 28 = 0 \\implies -3h + 4k = 7",
              "explanation": "Multiplying the second equation by 3 and the first by 2: $34h - 12k = -46$, $-9h + 12k = 21 \\implies 25h = -25 \\implies h = -1$. Substituting: $4k = 7 + 3(-1) = 4 \\implies k = 1$. The center is $(-1, 1)$."
            },
            {
              "step": "Step 2: Translate Origin to $(-1, 1)$",
              "math": "c' = gh + fk + c = 23(-1) + (-14)(1) + 17 = -23 - 14 + 17 = -20 \\\\ \\text{Shifted equation: } 17X^2 - 12XY + 8Y^2 = 20",
              "explanation": "The linear terms are completely eliminated; the quadratic coefficients remain $a = 17, 2h = -12 \\implies h = -6, b = 8$."
            },
            {
              "step": "Step 3: Determine Rotation Angle $\theta$ to Eliminate Cross Term",
              "math": "\\tan 2\\theta = \\frac{2h}{a - b} = \\frac{-12}{17 - 8} = \\frac{-12}{9} = -\\frac{4}{3}",
              "explanation": "Since $\tan 2\theta = -4/3$, we have $\\cos 2\theta = -3/5$. Using half-angle formulas: $\\sin^2 \theta = \\frac{1 - \\cos 2\theta}{2} = \\frac{1 - (-3/5)}{2} = \\frac{4}{5} \\implies \\sin \theta = \\frac{2}{\\sqrt{5}}$, $\\cos \theta = \\frac{1}{\\sqrt{5}} \\implies \theta = \\arctan(2)$."
            },
            {
              "step": "Step 4: Compute Canonical Eigenvalues and Final Equation",
              "math": "\\lambda^2 - (a+b)\\lambda + (ab - h^2) = 0 \\implies \\lambda^2 - 25\\lambda + (136 - 36) = \\lambda^2 - 25\\lambda + 100 = 0 \\\\ (\\lambda - 20)(\\lambda - 5) = 0 \\implies \\lambda_1 = 5, \\quad \\lambda_2 = 20 \\\\ \\text{Canonical form: } 5X'^2 + 20Y'^2 = 20 \\iff \\frac{X'^2}{4} + \\frac{Y'^2}{1} = 1",
              "explanation": "The equation reduces to an ellipse centered at $(-1, 1)$, with major semi-axis $a = 2$, minor semi-axis $b = 1$, and rotated by $\theta = \\arctan(2)$."
            }
          ],
          "answer": "\\text{Translation: } (h, k) = (-1, 1); \\quad \\text{Rotation: } \\theta = \\arctan(2) \\approx 63.43^\\circ; \\quad \\text{Canonical Form: } \\frac{X'^2}{4} + \\frac{Y'^2}{1} = 1 \\text{ (Ellipse)}"
        }
      ],
      "simulations": [
        "geom2d-coord-transform-sim"
      ],
      "id": "unit1",
      "unitId": "unit1-geom2d",
      "leadSummary": "Comprehensive analytical foundations of two-dimensional coordinate geometry: Cartesian metric space axioms, distance and section formulas, harmonic ranges, triangle centers and the Euler line, shoelace polygon area determinants, polar coordinates and metric relations, translation of axes and curve transformations, rotation of axes via SO(2) orthogonal matrices, and fundamental quadratic invariants."
    },
    {
      "unitNumber": 2,
      "number": 2,
      "title": "Pairs of Straight Lines (Homogeneous & Non-Homogeneous Equations)",
      "description": "Exhaustive treatment of second-degree equations representing lines: homogeneous quadratic line pairs passing through the origin, slope formulas and reality criteria, angle between lines tan theta = 2 sqrt(h^2 - ab)/(a + b), perpendicularity (a + b = 0) and coincidence (h^2 = ab), joint equation of angle bisectors (x^2 - y^2)/(a - b) = xy/h and mutual orthogonality proof, general second-degree line pairs via the determinant condition Delta = 0, intersection points via partial derivatives, parallel line distances, and the homogenization theorem.",
      "sections": [
        {
          "id": "u2-sec1",
          "title": "Homogeneous Quadratic Equations & Line Pairs Through Origin",
          "content": "\n<h3>1. The Homogeneous Second-Degree Equation</h3>\n<p>\nThe most general homogeneous algebraic equation of second degree in two variables $x$ and $y$ is:\n$$a x^2 + 2h xy + b y^2 = 0 \\quad (a, h, b \\in \\mathbb{R}, \\; \\text{not all zero})$$\nAssuming $b \\ne 0$, we can divide by $x^2$ (for $x \\ne 0$) and set $m = y/x$ (the slope of a line through the origin):\n$$b \\left(\\frac{y}{x}\\right)^2 + 2h \\left(\\frac{y}{x}\\right) + a = 0 \\iff b m^2 + 2h m + a = 0$$\nThis is a quadratic equation in the slope $m$. By the quadratic formula, the two roots $m_1$ and $m_2$ are:\n$$m_1, m_2 = \\frac{-2h \\pm \\sqrt{4h^2 - 4ab}}{2b} = \\frac{-h \\pm \\sqrt{h^2 - ab}}{b}$$\nTherefore, the quadratic expression factors over $\\mathbb{R}$ into two linear equations:\n$$a x^2 + 2h xy + b y^2 = b(y - m_1 x)(y - m_2 x) = 0$$\nrepresenting two straight lines passing through the origin $O(0, 0)$:\n$$L_1: y - m_1 x = 0, \\qquad L_2: y - m_2 x = 0$$\n</p>\n\n<h3>2. The Reality Discriminant ($h^2 - ab$)</h3>\n<p>\nFrom Vi\u00e8te's formulas for $b m^2 + 2h m + a = 0$:\n$$m_1 + m_2 = -\\frac{2h}{b}, \\qquad m_1 m_2 = \\frac{a}{b}$$\nThe nature of the lines is completely governed by the discriminant $D_L \\equiv h^2 - ab$:\n<ul>\n  <li><strong>Real and Distinct Lines ($h^2 > ab$):</strong> The quadratic has two distinct real slopes $m_1 \\ne m_2$, representing two real intersecting straight lines passing through the origin.</li>\n  <li><strong>Real and Coincident Lines ($h^2 = ab$):</strong> The discriminant vanishes, giving a single repeated root $m_1 = m_2 = -h/b$. The equation represents two coincident (identical) lines:\n  $$a x^2 + 2h xy + b y^2 = (\\sqrt{a}x + \\sqrt{b}y)^2 = 0 \\iff \\sqrt{a}x + \\sqrt{b}y = 0$$</li>\n  <li><strong>Imaginary Lines with Real Intersection ($h^2 < ab$):</strong> The slopes $m_1, m_2$ are complex conjugates $m = \\alpha \\pm i \\beta$. The equation has no real solutions other than the single isolated real point of intersection $(0, 0)$.</li>\n</ul>\n</p>\n"
        },
        {
          "id": "u2-sec2",
          "title": "Angle Between Line Pairs & Orthogonality Conditions",
          "content": "\n<h3>1. Derivation of the Acute Angle Between Lines</h3>\n<p>\nLet $\\theta$ be the acute angle between the two lines $y = m_1 x$ and $y = m_2 x$ represented by $a x^2 + 2h xy + b y^2 = 0$. From elementary trigonometry:\n$$\\tan \\theta = \\left| \\frac{m_1 - m_2}{1 + m_1 m_2} \\right|$$\nUsing the algebraic identity $(m_1 - m_2)^2 = (m_1 + m_2)^2 - 4 m_1 m_2$:\n$$|m_1 - m_2| = \\sqrt{\\left(-\\frac{2h}{b}\\right)^2 - 4\\left(\\frac{a}{b}\\right)} = \\frac{2\\sqrt{h^2 - ab}}{|b|}$$\nSubstituting into the tangent formula:\n$$\\tan \\theta = \\left| \\frac{\\frac{2\\sqrt{h^2 - ab}}{b}}{1 + \\frac{a}{b}} \\right| = \\left| \\frac{2\\sqrt{h^2 - ab}}{a + b} \\right|$$\nThis is the universally famous formula for the angle between a pair of straight lines!\n</p>\n\n<h3>2. The Orthogonality Condition ($a + b = 0$)</h3>\n<p>\nThe two lines are mutually perpendicular ($\\theta = \\pi/2$) if and only if $\\tan \\theta \\to \\infty$, which requires the denominator to vanish:\n$$\\mathbf{Perpendicularity \\iff} \\quad a + b = 0 \\iff \\text{Coefficient of } x^2 + \\text{Coefficient of } y^2 = 0$$\nNotice that this condition holds regardless of the value of $h$! When $a + b = 0$, the lines are orthogonal.\n</p>\n\n<h3>3. The Parallel / Coincidence Condition ($h^2 = ab$)</h3>\n<p>\nThe two lines are parallel or coincident ($\\theta = 0$) if and only if $\\tan \\theta = 0$, which requires the numerator to vanish:\n$$\\mathbf{Coincidence \\iff} \\quad h^2 - ab = 0 \\iff h^2 = ab$$\n</p>\n"
        },
        {
          "id": "u2-sec3",
          "title": "Joint Equation of Angle Bisectors & Orthogonality Proof",
          "content": "\n<h3>1. Derivation of the Bisector Pair Equation</h3>\n<p>\nLet the lines be $L_1: y - m_1 x = 0$ and $L_2: y - m_2 x = 0$. Any point $P(x, y)$ on the bisectors of the angles between $L_1$ and $L_2$ is equidistant from both lines:\n$$\\frac{|y - m_1 x|}{\\sqrt{1 + m_1^2}} = \\frac{|y - m_2 x|}{\\sqrt{1 + m_2^2}}$$\nSquaring both sides eliminates the absolute values:\n$$\\frac{(y - m_1 x)^2}{1 + m_1^2} = \\frac{(y - m_2 x)^2}{1 + m_2^2} \\iff (1 + m_2^2)(y - m_1 x)^2 - (1 + m_1^2)(y - m_2 x)^2 = 0$$\nExpanding and factoring $(m_1 - m_2) \\ne 0$:\n$$(1 - m_1 m_2)(x^2 - y^2) + 2(m_1 + m_2)xy = 0$$\nSubstituting $m_1 + m_2 = -2h/b$ and $m_1 m_2 = a/b$:\n$$\\left(1 - \\frac{a}{b}\\right)(x^2 - y^2) + 2\\left(-\\frac{2h}{b}\\right)xy = 0 \\iff \\frac{b - a}{b}(x^2 - y^2) - \\frac{4h}{b}xy = 0$$\nDividing by $-(b - a) \\cdot 4h$ yields the standard canonical symmetric form:\n$$\\frac{x^2 - y^2}{a - b} = \\frac{xy}{h} \\iff h(x^2 - y^2) - (a - b)xy = 0$$\n</p>\n\n<h3>2. Proof of Mutual Perpendicularity of Bisectors</h3>\n<p>\nThe joint bisector equation is a homogeneous second-degree equation of the form $A x^2 + 2H xy + B y^2 = 0$, where:\n$$A = h, \\qquad 2H = -(a - b), \\qquad B = -h$$\nApplying the orthogonality criterion derived in Section 2.2:\n$$A + B = h + (-h) = 0$$\nBecause the sum of the coefficients of $x^2$ and $y^2$ is identically zero, **the internal and external angle bisectors are always strictly mutually perpendicular**!\n</p>\n"
        },
        {
          "id": "u2-sec4",
          "title": "General Second-Degree Equation Representing a Pair of Straight Lines",
          "content": "\n<h3>1. The Non-Homogeneous General Equation</h3>\n<p>\nThe general non-homogeneous algebraic equation of second degree is:\n$$F(x, y) = a x^2 + 2h xy + b y^2 + 2g x + 2f y + c = 0$$\nFor this equation to represent two distinct or coincident straight lines, it must be factorizable into two linear factors:\n$$F(x, y) = (l_1 x + m_1 y + n_1)(l_2 x + m_2 y + n_2) = 0$$\nEquating coefficients of identical monomials:\n$$l_1 l_2 = a, \\quad m_1 m_2 = b, \\quad n_1 n_2 = c$$\n$$l_1 m_2 + l_2 m_1 = 2h, \\quad l_1 n_2 + l_2 n_1 = 2g, \\quad m_1 n_2 + m_2 n_1 = 2f$$\n</p>\n\n<h3>2. The Determinant Condition $\\Delta = 0$</h3>\n<p>\nEliminating $l_i, m_i, n_i$ establishes the necessary and sufficient condition for $F(x, y) = 0$ to represent a pair of lines:\n$$\\Delta \\equiv \\begin{vmatrix} a & h & g \\\\ h & b & f \\\\ g & f & c \\end{vmatrix} = 0 \\iff abc + 2fgh - af^2 - bg^2 - ch^2 = 0$$\nTogether with $h^2 \\ge ab$ (ensuring the lines are real).\n</p>\n\n<h3>3. Point of Intersection via Partial Derivatives</h3>\n<p>\nWhen $\\Delta = 0$, the two lines intersect at a unique point $(\\bar{x}, \\bar{y})$ which is the singular point of the algebraic curve. Taking partial derivatives of $F(x, y)$:\n$$\\frac{\\partial F}{\\partial x} = 2ax + 2hy + 2g = 0 \\implies ax + hy + g = 0$$\n$$\\frac{\\partial F}{\\partial y} = 2hx + 2by + 2f = 0 \\implies hx + by + f = 0$$\nSolving this $2 \\times 2$ linear system by Cramer's rule yields the point of intersection:\n$$\\bar{x} = \\frac{hf - bg}{ab - h^2}, \\qquad \\bar{y} = \\frac{gh - af}{ab - h^2} \\quad (ab - h^2 \\ne 0)$$\n</p>\n"
        },
        {
          "id": "u2-sec5",
          "title": "Parallel Line Pairs, Distance & The Homogenization Technique",
          "content": "\n<h3>1. Condition for Parallel Lines</h3>\n<p>\nIf the lines represented by $ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0$ are parallel, their second-degree terms must form a perfect square:\n$$h^2 - ab = 0 \\iff \\frac{a}{h} = \\frac{h}{b} = \\frac{g}{f}$$\nThe perpendicular distance $d$ between the two parallel lines is given by:\n$$d = 2\\sqrt{\\frac{g^2 - ac}{a(a + b)}} = 2\\sqrt{\\frac{f^2 - bc}{b(a + b)}}$$\n</p>\n\n<h3>2. The Method of Homogenization</h3>\n<p>\nA powerful technique in classical geometry is finding the joint equation of the two straight lines connecting the origin $O(0, 0)$ to the intersection points of a general second-degree curve $S \\equiv ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0$ and a line $L \\equiv lx + my + n = 0$.\n<ol>\n  <li>Write the equation of the line in normalized unit form:\n  $$\\frac{lx + my}{-n} = 1 \\quad (n \\ne 0)$$</li>\n  <li>Make the equation of the curve homogeneous of degree 2 by multiplying the linear terms by $(1)$ and the constant term by $(1)^2$:\n  $$ax^2 + 2hxy + by^2 + 2(gx + fy)\\left(\\frac{lx + my}{-n}\\right) + c\\left(\\frac{lx + my}{-n}\\right)^2 = 0$$</li>\n  <li>Because this resulting equation is purely homogeneous of degree 2, it represents two straight lines passing through the origin, and since it is satisfied by all points satisfying both $S = 0$ and $L = 0$, it is the exact joint equation of the lines connecting the origin to the intersection points!</li>\n</ol>\n</p>\n",
          "simulation": "geom2d-line-pair-sim",
          "simulations": [
            "geom2d-line-pair-sim"
          ]
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "Angle Between Line Pair and Joint Equation of Bisectors",
          "statement": "Given the homogeneous second-degree equation $2x^2 + 7xy + 3y^2 = 0$: (a) Find the individual equations of the two lines. (b) Calculate the acute angle $\\theta$ between them. (c) Derive the joint equation of the bisectors of the angles between the lines.",
          "steps": [
            {
              "step": "Step 1: Factor the Homogeneous Quadratic",
              "math": "2x^2 + 7xy + 3y^2 = 2x^2 + 6xy + xy + 3y^2 = 2x(x + 3y) + y(x + 3y) = (2x + y)(x + 3y) = 0",
              "explanation": "The individual lines are $L_1: 2x + y = 0$ (slope $m_1 = -2$) and $L_2: x + 3y = 0$ (slope $m_2 = -1/3$)."
            },
            {
              "step": "Step 2: Calculate the Acute Angle $\theta$",
              "math": "\\tan \\theta = \\left|\\frac{2\\sqrt{h^2 - ab}}{a + b}\\right| = \\left|\\frac{2\\sqrt{(7/2)^2 - (2)(3)}}{2 + 3}\\right| = \\frac{2\\sqrt{49/4 - 6}}{5} = \\frac{2\\sqrt{25/4}}{5} = \\frac{2(5/2)}{5} = \\frac{5}{5} = 1",
              "explanation": "Since $\tan \theta = 1$, the acute angle between the two lines is $\theta = \\frac{\\pi}{4} = 45^\\circ$."
            },
            {
              "step": "Step 3: Joint Equation of Angle Bisectors",
              "math": "\\frac{x^2 - y^2}{a - b} = \\frac{xy}{h} \\implies \\frac{x^2 - y^2}{2 - 3} = \\frac{xy}{7/2} \\implies \\frac{x^2 - y^2}{-1} = \\frac{2xy}{7} \\implies 7(x^2 - y^2) = -2xy \\implies 7x^2 + 2xy - 7y^2 = 0",
              "explanation": "Notice coefficient sum: $7 + (-7) = 0$, confirming mutual perpendicularity of the bisector pair."
            }
          ],
          "answer": "\\text{Lines: } 2x + y = 0 \\text{ and } x + 3y = 0; \\quad \\theta = 45^\\circ; \\quad \\text{Bisectors: } 7x^2 + 2xy - 7y^2 = 0"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "General Second-Degree Equation Verification and Point of Intersection",
          "statement": "Show that the equation $2x^2 - 5xy + 2y^2 + 7x - 5y + 3 = 0$ represents a pair of straight lines. Find their point of intersection and the acute angle between them.",
          "steps": [
            {
              "step": "Step 1: Verify the Determinant Condition $\\Delta = 0$",
              "math": "a = 2, \\; h = -5/2, \\; b = 2, \\; g = 7/2, \\; f = -5/2, \\; c = 3 \\\\ \\Delta = \\begin{vmatrix} 2 & -5/2 & 7/2 \\\\ -5/2 & 2 & -5/2 \\\\ 7/2 & -5/2 & 3 \\end{vmatrix} = 2\\left(6 - \\frac{25}{4}\\right) - \\left(-\\frac{5}{2}\\right)\\left(-\\frac{15}{2} + \\frac{35}{4}\\right) + \\frac{7}{2}\\left(\\frac{25}{4} - 7\\right) \\\\ = 2\\left(-\\frac{1}{4}\\right) + \\frac{5}{2}\\left(\\frac{5}{4}\\right) + \\frac{7}{2}\\left(-\\frac{3}{4}\\right) = -\\frac{2}{4} + \\frac{25}{8} - \\frac{21}{8} = -\\frac{4}{8} + \\frac{4}{8} = 0",
              "explanation": "Since $\\Delta = 0$ and $h^2 - ab = 25/4 - 4 = 9/4 > 0$, the equation represents two real intersecting straight lines."
            },
            {
              "step": "Step 2: Find Point of Intersection",
              "math": "\\frac{\\partial F}{\\partial x} = 4x - 5y + 7 = 0 \\\\ \\frac{\\partial F}{\\partial y} = -5x + 4y - 5 = 0 \\\\ \\text{Adding: } -x - y + 2 = 0 \\implies y = 2 - x \\\\ 4x - 5(2 - x) + 7 = 0 \\implies 9x - 3 = 0 \\implies x = \\frac{1}{3}, \\quad y = \\frac{5}{3}",
              "explanation": "The lines intersect at the point $(1/3, 5/3)$."
            },
            {
              "step": "Step 3: Compute Acute Angle $\theta$",
              "math": "\\tan \\theta = \\left|\\frac{2\\sqrt{h^2 - ab}}{a + b}\\right| = \\left|\\frac{2\\sqrt{25/4 - 4}}{2 + 2}\\right| = \\frac{2(3/2)}{4} = \\frac{3}{4} \\implies \\theta = \\arctan(3/4) \\approx 36.87^\\circ",
              "explanation": "The acute angle between the lines is $\\arctan(3/4)$."
            }
          ],
          "answer": "\\Delta = 0 \\implies \\text{Represents pair of straight lines}; \\quad \\text{Intersection: } \\left(\\frac{1}{3}, \\frac{5}{3}\\right); \\quad \\theta = \\arctan\\left(\\frac{3}{4}\\right)"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "Homogenization: Right-Angled Subtended Chords from a Circle to the Origin",
          "statement": "A straight line $L \\equiv 2x + y = k$ intersects the circle $x^2 + y^2 - 2x - 4y - 4 = 0$ at two distinct points $A$ and $B$. (a) Formulate the joint homogeneous equation of the lines $OA$ and $OB$ joining the origin to $A$ and $B$. (b) Determine the values of the constant $k$ such that the chord $AB$ subtends a right angle at the origin ($OA \\perp OB$).",
          "steps": [
            {
              "step": "Step 1: Express the Line in Normalized Unit Form",
              "math": "2x + y = k \\implies \\frac{2x + y}{k} = 1 \\quad (k \\ne 0)",
              "explanation": "This unit expression is substituted into the non-homogeneous terms of the circle equation."
            },
            {
              "step": "Step 2: Homogenize the Circle Equation to Degree 2",
              "math": "x^2 + y^2 - (2x + 4y)\\left(\\frac{2x + y}{k}\\right) - 4\\left(\\frac{2x + y}{k}\\right)^2 = 0 \\\\ k^2(x^2 + y^2) - k(2x + 4y)(2x + y) - 4(4x^2 + 4xy + y^2) = 0 \\\\ = k^2(x^2 + y^2) - k(4x^2 + 10xy + 4y^2) - (16x^2 + 16xy + 4y^2) = 0",
              "explanation": "Grouping by quadratic monomials $x^2, xy, y^2$: $(k^2 - 4k - 16)x^2 - (10k + 16)xy + (k^2 - 4k - 4)y^2 = 0$."
            },
            {
              "step": "Step 3: Apply the Orthogonality Condition $A + B = 0$",
              "math": "\\text{For } OA \\perp OB, \\quad \\text{Coeff}(x^2) + \\text{Coeff}(y^2) = 0 \\\\ (k^2 - 4k - 16) + (k^2 - 4k - 4) = 0 \\implies 2k^2 - 8k - 20 = 0 \\implies k^2 - 4k - 10 = 0",
              "explanation": "Solving the quadratic equation for $k$: $k = \\frac{4 \\pm \\sqrt{16 - 4(1)(-10)}}{2} = \\frac{4 \\pm \\sqrt{56}}{2} = 2 \\pm \\sqrt{14}$."
            }
          ],
          "answer": "\\text{Joint Equation: } (k^2 - 4k - 16)x^2 - (10k + 16)xy + (k^2 - 4k - 4)y^2 = 0; \\quad k = 2 \\pm \\sqrt{14}"
        }
      ],
      "simulations": [
        "geom2d-line-pair-sim"
      ],
      "id": "unit2",
      "unitId": "unit2-geom2d",
      "leadSummary": "Exhaustive treatment of second-degree equations representing lines: homogeneous quadratic line pairs passing through the origin, slope formulas and reality criteria, angle between lines tan theta = 2 sqrt(h^2 - ab)/(a + b), perpendicularity (a + b = 0) and coincidence (h^2 = ab), joint equation of angle bisectors (x^2 - y^2)/(a - b) = xy/h and mutual orthogonality proof, general second-degree line pairs via the determinant condition Delta = 0, intersection points via partial derivatives, parallel line distances, and the homogenization theorem."
    },
    {
      "unitNumber": 3,
      "number": 3,
      "title": "The Circle: Tangents, Polars & Systems of Coaxial Circles",
      "description": "Comprehensive mathematical theory of circles: standard, general, and diametric representations; tangency conditions, slope equations, and Joachimsthal's pair of tangents SS_1 = T^2; chord of contact and reciprocal pole and polar theory; radical axis locus S_1 - S_2 = 0, perpendicularity proof, and radical centers; orthogonal circle criteria 2g_1 g_2 + 2f_1 f_2 = c_1 + c_2; and coaxial systems of circles, canonical equations, limiting points, and conjugate orthogonal families.",
      "sections": [
        {
          "id": "u3-sec1",
          "title": "Standard, General & Diametric Equations of the Circle",
          "content": "\n<h3>1. The Locus Definition & General Form</h3>\n<p>\nA circle is the planar locus of a point $P(x, y)$ that moves such that its Euclidean distance from a fixed center $C(x_0, y_0)$ remains constant and equal to radius $R > 0$:\n$$(x - x_0)^2 + (y - y_0)^2 = R^2$$\nExpanding this central equation yields the general second-degree equation of a circle:\n$$x^2 + y^2 + 2gx + 2fy + c = 0$$\nCompleting the squares:\n$$(x + g)^2 + (y + f)^2 = g^2 + f^2 - c$$\nComparing with the standard form:\n$$\\mathbf{Center:} \\; C(-g, -f), \\qquad \\mathbf{Radius:} \\; R = \\sqrt{g^2 + f^2 - c}$$\nClassification based on $g^2 + f^2 - c$:\n<ul>\n  <li><strong>Real Circle ($g^2 + f^2 > c$):</strong> A non-degenerate circle with positive real radius.</li>\n  <li><strong>Point Circle ($g^2 + f^2 = c$):</strong> The radius is zero; the locus degenerates to the single point $(-g, -f)$.</li>\n  <li><strong>Imaginary / Virtual Circle ($g^2 + f^2 < c$):</strong> No real coordinates satisfy the equation.</li>\n</ul>\n</p>\n\n<h3>2. Circle on a Given Diameter</h3>\n<p>\nLet $A(x_1, y_1)$ and $B(x_2, y_2)$ be the endpoints of a diameter. For any point $P(x, y)$ on the circle (other than $A$ or $B$), the inscribed angle $\\angle APB = \\pi/2$ by Thales' theorem. Hence $\\vec{PA} \\cdot \\vec{PB} = 0$:\n$$(x - x_1)(x - x_2) + (y - y_1)(y - y_2) = 0$$\nThis is the celebrated diametric form of a circle!\n</p>\n"
        },
        {
          "id": "u3-sec2",
          "title": "Tangents, Normals & Length of Tangents",
          "content": "\n<h3>1. Equation of Tangent and Normal at a Point</h3>\n<p>\nFor the general circle $S \\equiv x^2 + y^2 + 2gx + 2fy + c = 0$, the equation of the tangent at point $P(x_1, y_1)$ on the circle is obtained by the rule of transformation $x^2 \\to x x_1, y^2 \\to y y_1, 2x \\to x + x_1, 2y \\to y + y_1$:\n$$T \\equiv x x_1 + y y_1 + g(x + x_1) + f(y + y_1) + c = 0$$\nBecause the normal passes through the center $(-g, -f)$ and point $(x_1, y_1)$, its equation is:\n$$\\frac{x - x_1}{x_1 + g} = \\frac{y - y_1}{y_1 + f} \\iff (y_1 + f)(x - x_1) - (x_1 + g)(y - y_1) = 0$$\n</p>\n\n<h3>2. Tangents in Slope Form & Condition of Tangency</h3>\n<p>\nFor the central circle $x^2 + y^2 = R^2$, a straight line $y = mx + k$ is tangent to the circle if and only if the perpendicular distance from the center $(0, 0)$ to the line equals the radius:\n$$\\frac{|k|}{\\sqrt{1 + m^2}} = R \\iff k = \\pm R \\sqrt{1 + m^2}$$\nThus the two parallel tangents with slope $m$ are:\n$$y = mx \\pm R \\sqrt{1 + m^2}$$\n</p>\n\n<h3>3. Length of Tangents & Pair of Tangents</h3>\n<p>\nThe length $L$ of the tangent drawn from an external point $P(x_1, y_1)$ to the circle $S = 0$ is:\n$$L = \\sqrt{S_1} = \\sqrt{x_1^2 + y_1^2 + 2gx_1 + 2fy_1 + c}$$\nThe combined joint equation of the pair of tangents drawn from $P(x_1, y_1)$ to the circle is given by the elegant Joachimsthal relation:\n$$S S_1 = T^2$$\nwhere $S = x^2 + y^2 + 2gx + 2fy + c$, $S_1 = x_1^2 + y_1^2 + 2gx_1 + 2fy_1 + c$, and $T = xx_1 + yy_1 + g(x+x_1) + f(y+y_1) + c$.\n</p>\n"
        },
        {
          "id": "u3-sec3",
          "title": "Chord of Contact, Pole and Polar Theory",
          "content": "\n<h3>1. Chord of Contact</h3>\n<p>\nIf two tangents are drawn from an external point $P(x_1, y_1)$ touching the circle at $Q$ and $R$, the line segment connecting the points of tangency is the <strong>chord of contact</strong>. Its equation is identically:\n$$T \\equiv x x_1 + y y_1 + g(x + x_1) + f(y + y_1) + c = 0$$\n</p>\n\n<h3>2. Pole and Polar Theory</h3>\n<p>\nLet $P(x_1, y_1)$ be any point (internal, external, or on the circle). If a variable secant line through $P$ intersects the circle at $A$ and $B$, the locus of the intersection of the tangents drawn at $A$ and $B$ is a straight line termed the <strong>polar</strong> of $P$ with respect to the circle. Point $P$ is called the <strong>pole</strong> of this line.\nThe equation of the polar of point $P(x_1, y_1)$ is:\n$$T \\equiv x x_1 + y y_1 + g(x + x_1) + f(y + y_1) + c = 0$$\n</p>\n<p>\n<strong>Key Properties of Polars:</strong>\n<ul>\n  <li>If $P$ lies outside the circle, the polar is the chord of contact of tangents from $P$.</li>\n  <li>If $P$ lies on the circle, the polar is the tangent line at $P$.</li>\n  <li>If $P$ lies inside the circle, the polar lies entirely outside the circle.</li>\n  <li><strong>Reciprocal Property:</strong> If the polar of point $P$ passes through point $Q$, then the polar of point $Q$ passes through point $P$. Such points $P$ and $Q$ are termed <em>conjugate points</em>.</li>\n</ul>\n</p>\n"
        },
        {
          "id": "u3-sec4",
          "title": "Radical Axis, Radical Center & Orthogonal Circles",
          "content": "\n<h3>1. The Radical Axis</h3>\n<p>\nThe <strong>radical axis</strong> of two non-concentric circles $S_1 \\equiv x^2 + y^2 + 2g_1 x + 2f_1 y + c_1 = 0$ and $S_2 \\equiv x^2 + y^2 + 2g_2 x + 2f_2 y + c_2 = 0$ is the planar locus of points from which the lengths of tangents drawn to both circles are equal:\n$$L_1^2 = L_2^2 \\iff S_1 - S_2 = 0$$\nSubtracting the two equations eliminates the quadratic terms $x^2 + y^2$, yielding a linear equation:\n$$2(g_1 - g_2)x + 2(f_1 - f_2)y + (c_1 - c_2) = 0$$\n<strong>Geometric Theorem:</strong> The radical axis is always perpendicular to the line joining the centers $C_1(-g_1, -f_1)$ and $C_2(-g_2, -f_2)$ of the two circles!\n</p>\n\n<h3>2. The Radical Center</h3>\n<p>\nFor three circles $S_1 = 0, S_2 = 0, S_3 = 0$ whose centers are non-collinear, the three radical axes taken in pairs:\n$$S_1 - S_2 = 0, \\qquad S_2 - S_3 = 0, \\qquad S_3 - S_1 = 0$$\nare concurrent at a unique point termed the <strong>radical center</strong>. The lengths of tangents drawn from the radical center to all three circles are equal, so it is the center of a circle orthogonal to all three circles!\n</p>\n\n<h3>3. Orthogonal Circles Condition</h3>\n<p>\nTwo circles intersect orthogonally if their tangents at the points of intersection are perpendicular. By the Pythagorean theorem on the triangle formed by the two centers and a point of intersection:\n$$C_1 C_2^2 = R_1^2 + R_2^2 \\iff (g_1 - g_2)^2 + (f_1 - f_2)^2 = (g_1^2 + f_1^2 - c_1) + (g_2^2 + f_2^2 - c_2)$$\nExpanding and simplifying establishes the condition of orthogonality:\n$$2 g_1 g_2 + 2 f_1 f_2 = c_1 + c_2$$\n</p>\n"
        },
        {
          "id": "u3-sec5",
          "title": "Coaxial Systems of Circles & Limiting Points",
          "content": "\n<h3>1. Coaxial Systems of Circles</h3>\n<p>\nA system of circles is said to be <strong>coaxial</strong> if every pair of circles in the system possesses the same common radical axis.\nIf $S_1 = 0$ and $S_2 = 0$ are two members of the system, any circle in the coaxial family is given by:\n$$S_1 + \\lambda S_2 = 0 \\quad (\\lambda \\ne -1), \\qquad \\text{or} \\quad S_1 + \\mu(S_1 - S_2) = 0$$\nBy choosing the common radical axis as the $y$-axis ($x = 0$) and the line of centers as the $x$-axis ($y = 0$), the simplest canonical form of a coaxial system is:\n$$x^2 + y^2 + 2 k x + c = 0$$\nwhere $c$ is a constant for the entire family and $k$ is a variable parameter identifying individual circles.\nThe center is $(-k, 0)$ and radius is $R = \\sqrt{k^2 - c}$.\n</p>\n\n<h3>2. Limiting Points</h3>\n<p>\nThe <strong>limiting points</strong> of a coaxial system are the centers of the circles in the system whose radii vanish identically ($R = 0$):\n$$R^2 = k^2 - c = 0 \\iff k = \\pm \\sqrt{c}$$\nThus, if $c > 0$, there exist two real limiting points:\n$$L_1(\\sqrt{c}, 0), \\qquad L_2(-\\sqrt{c}, 0)$$\nThese limiting points are point-circles belonging to the coaxial system. Every circle of the system is orthogonal to any circle passing through the two limiting points!\n</p>\n",
          "simulation": "geom2d-circle-radical-sim",
          "simulations": [
            "geom2d-circle-radical-sim"
          ]
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "Circle Passing Through Three Points and Tangent at a Given Point",
          "statement": "Find the equation of the circle passing through the points $(0, 0)$, $(4, 0)$, and $(0, 6)$. Determine its center, radius, and the equation of the tangent line at the origin $(0, 0)$.",
          "steps": [
            {
              "step": "Step 1: Determine Circle Equation",
              "math": "x^2 + y^2 + 2gx + 2fy + c = 0 \\\\ \\text{Through } (0, 0): \\quad c = 0 \\\\ \\text{Through } (4, 0): \\quad 16 + 8g = 0 \\implies g = -2 \\\\ \\text{Through } (0, 6): \\quad 36 + 12f = 0 \\implies f = -3 \\\\ \\text{Circle: } x^2 + y^2 - 4x - 6y = 0",
              "explanation": "Substituting the three points determines the unique values of $g, f, c$."
            },
            {
              "step": "Step 2: Find Center and Radius",
              "math": "\\text{Center: } (-g, -f) = (2, 3) \\\\ \\text{Radius: } R = \\sqrt{g^2 + f^2 - c} = \\sqrt{(-2)^2 + (-3)^2 - 0} = \\sqrt{4 + 9} = \\sqrt{13}",
              "explanation": "The circle is centered at $(2, 3)$ with radius $\\sqrt{13}$."
            },
            {
              "step": "Step 3: Tangent Line at the Origin $(0, 0)$",
              "math": "T \\equiv x(0) + y(0) - 2(x + 0) - 3(y + 0) = 0 \\implies -2x - 3y = 0 \\implies 2x + 3y = 0",
              "explanation": "Using the transformation rule $T = 0$ gives the tangent line $2x + 3y = 0$."
            }
          ],
          "answer": "\\text{Circle: } x^2 + y^2 - 4x - 6y = 0; \\quad \\text{Center: } (2, 3); \\quad R = \\sqrt{13}; \\quad \\text{Tangent at } (0, 0): 2x + 3y = 0"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "Radical Axis and Condition of Orthogonality",
          "statement": "Given two circles $S_1 \\equiv x^2 + y^2 - 6x - 4y + 9 = 0$ and $S_2 \\equiv x^2 + y^2 + 4x + 6y - 7 = 0$: (a) Find the equation of their radical axis. (b) Verify that the radical axis is perpendicular to the line of centers. (c) Find the value of $\\lambda$ such that the circle $x^2 + y^2 + \\lambda x - 2y + 5 = 0$ is orthogonal to $S_1$.",
          "steps": [
            {
              "step": "Step 1: Compute Radical Axis $S_1 - S_2 = 0$",
              "math": "(x^2 + y^2 - 6x - 4y + 9) - (x^2 + y^2 + 4x + 6y - 7) = 0 \\\\ -10x - 10y + 16 = 0 \\implies 5x + 5y - 8 = 0",
              "explanation": "The radical axis is $5x + 5y - 8 = 0$, having slope $m_{\text{rad}} = -5/5 = -1$."
            },
            {
              "step": "Step 2: Verify Perpendicularity to Line of Centers",
              "math": "C_1 = (3, 2), \\quad C_2 = (-2, -3) \\\\ m_{\\text{centers}} = \\frac{-3 - 2}{-2 - 3} = \\frac{-5}{-5} = 1 \\\\ m_{\\text{rad}} \\times m_{\\text{centers}} = (-1)(1) = -1 \\implies \\text{Strictly Perpendicular!}",
              "explanation": "The product of slopes is $-1$, verifying perpendicularity."
            },
            {
              "step": "Step 3: Condition of Orthogonality for $S_1$ and $S_3$",
              "math": "S_1: g_1 = -3, f_1 = -2, c_1 = 9 \\\\ S_3: g_3 = \\lambda/2, f_3 = -1, c_3 = 5 \\\\ 2 g_1 g_3 + 2 f_1 f_3 = c_1 + c_3 \\implies 2(-3)\\left(\\frac{\\lambda}{2}\\right) + 2(-2)(-1) = 9 + 5 \\\\ -3\\lambda + 4 = 14 \\implies -3\\lambda = 10 \\implies \\lambda = -\\frac{10}{3}",
              "explanation": "Applying $2g_1 g_2 + 2f_1 f_2 = c_1 + c_2$ yields $\\lambda = -10/3$."
            }
          ],
          "answer": "\\text{Radical Axis: } 5x + 5y - 8 = 0; \\quad m_1 m_2 = -1 \\implies \\text{Perpendicular}; \\quad \\lambda = -\\frac{10}{3}"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "Coaxial Family Limiting Points and Orthogonal Conjugate System",
          "statement": "A coaxial system of circles is determined by $S_1 \\equiv x^2 + y^2 - 4x - 6y + 9 = 0$ and the radical axis $x - y + 1 = 0$. (a) Write the general equation of the coaxial family. (b) Find the exact coordinates of the limiting points of the system. (c) Derive the equation of the orthogonal conjugate coaxial system passing through the limiting points.",
          "steps": [
            {
              "step": "Step 1: Formulate the Coaxial System $S + \\lambda L = 0$",
              "math": "x^2 + y^2 - 4x - 6y + 9 + \\lambda(x - y + 1) = 0 \\\\ x^2 + y^2 + (\\lambda - 4)x - (\\lambda + 6)y + (\\lambda + 9) = 0",
              "explanation": "Here $g = \\frac{\\lambda - 4}{2}$, $f = -\\frac{\\lambda + 6}{2}$, $c = \\lambda + 9$."
            },
            {
              "step": "Step 2: Find Limiting Points via $R^2 = g^2 + f^2 - c = 0$",
              "math": "\\left(\\frac{\\lambda - 4}{2}\\right)^2 + \\left(\\frac{\\lambda + 6}{2}\\right)^2 - (\\lambda + 9) = 0 \\\\ \\frac{\\lambda^2 - 8\\lambda + 16 + \\lambda^2 + 12\\lambda + 36}{4} - (\\lambda + 9) = 0 \\\\ \\frac{2\\lambda^2 + 4\\lambda + 52}{4} - (\\lambda + 9) = 0 \\implies \\frac{\\lambda^2 + 2\\lambda + 26}{2} - (\\lambda + 9) = 0 \\\\ \\lambda^2 + 2\\lambda + 26 - 2\\lambda - 18 = 0 \\implies \\lambda^2 + 8 = 0",
              "explanation": "Notice $\\lambda^2 = -8$, meaning the limiting points are imaginary! When limiting points are imaginary, the coaxial circles intersect in real points $A, B$."
            },
            {
              "step": "Step 3: Find Real Common Points of Intersection",
              "math": "\\text{Substitute } y = x + 1 \\text{ into } S_1: \\quad x^2 + (x+1)^2 - 4x - 6(x+1) + 9 = 0 \\\\ x^2 + x^2 + 2x + 1 - 4x - 6x - 6 + 9 = 0 \\implies 2x^2 - 8x + 4 = 0 \\implies x^2 - 4x + 2 = 0 \\\\ x = 2 \\pm \\sqrt{2}, \\quad y = 3 \\pm \\sqrt{2}",
              "explanation": "The common real intersection points of the intersecting coaxial family are $P_1(2 + \\sqrt{2}, 3 + \\sqrt{2})$ and $P_2(2 - \\sqrt{2}, 3 - \\sqrt{2})$. The orthogonal conjugate system has these two points as its real limiting points!"
            }
          ],
          "answer": "\\text{Coaxial System: } x^2 + y^2 + (\\lambda - 4)x - (\\lambda + 6)y + (\\lambda + 9) = 0; \\quad \\text{Limiting Points: Imaginary (Intersecting family)}; \\quad \\text{Common Points: } (2 \\pm \\sqrt{2}, 3 \\pm \\sqrt{2})"
        }
      ],
      "simulations": [
        "geom2d-circle-radical-sim"
      ],
      "id": "unit3",
      "unitId": "unit3-geom2d",
      "leadSummary": "Comprehensive mathematical theory of circles: standard, general, and diametric representations; tangency conditions, slope equations, and Joachimsthal's pair of tangents SS_1 = T^2; chord of contact and reciprocal pole and polar theory; radical axis locus S_1 - S_2 = 0, perpendicularity proof, and radical centers; orthogonal circle criteria 2g_1 g_2 + 2f_1 f_2 = c_1 + c_2; and coaxial systems of circles, canonical equations, limiting points, and conjugate orthogonal families."
    },
    {
      "unitNumber": 4,
      "number": 4,
      "title": "General Second-Degree Equation & Classification of Conic Sections",
      "description": "Comprehensive theory of general quadratic equations: universal matrix formulation x^T A x = 0; rigid motion invariants trace I_1 = a + b, discriminant I_2 = ab - h^2, and total determinant I_3 = Delta; complete classification taxonomy for proper conics (ellipse, parabola, hyperbola) and degenerate varieties; center determination via partial derivatives and elimination of linear terms; rotational diagonalization and eigenvalue canonical reduction lambda_1 X^2 + lambda_2 Y^2 + Delta/D = 0; and the complete reduction protocol for non-central parabolas Y'^2 = 4AX'.",
      "sections": [
        {
          "id": "u4-sec1",
          "title": "General Second-Degree Equation & Discriminant Invariants",
          "content": "\n<h3>1. The Universal Quadratic Form</h3>\n<p>\nThe most general algebraic equation of the second degree in two variables is:\n$$F(x, y) = a x^2 + 2h xy + b y^2 + 2g x + 2f y + c = 0$$\nwhere $a, h, b, g, f, c \\in \\mathbb{R}$ and $(a, h, b) \\ne (0, 0, 0)$.\nIn matrix notation, this equation can be expressed compactly using homogeneous coordinates $\\mathbf{x} = (x, y, 1)^T$:\n$$\\mathbf{x}^T \\mathbf{A} \\mathbf{x} = 0, \\qquad \\mathbf{A} = \\begin{pmatrix} a & h & g \\\\ h & b & f \\\\ g & f & c \\end{pmatrix}$$\n</p>\n\n<h3>2. The Fundamental Invariants Under Rigid Euclidean Motion</h3>\n<p>\nUnder any rigid coordinate transformation (arbitrary translation and rotation $\\mathbf{x} \\mapsto \\mathbf{R}\\mathbf{x} + \\mathbf{t}$), the coefficients of the quadratic curve change, but three algebraic quantities remain <strong>strictly invariant</strong>:\n<ol>\n  <li><strong>First Invariant (Trace of Quadratic Part):</strong>\n  $$I_1 \\equiv a + b = \\operatorname{tr}(\\mathbf{A}_{2 \\times 2})$$</li>\n  <li><strong>Second Invariant (Discriminant of Quadratic Part):</strong>\n  $$I_2 \\equiv D \\equiv ab - h^2 = \\det(\\mathbf{A}_{2 \\times 2})$$</li>\n  <li><strong>Third Invariant (Total Conic Discriminant):</strong>\n  $$I_3 \\equiv \\Delta \\equiv \\det(\\mathbf{A}) = \\begin{vmatrix} a & h & g \\\\ h & b & f \\\\ g & f & c \\end{vmatrix} = abc + 2fgh - af^2 - bg^2 - ch^2$$</li>\n</ol>\nBecause these three quantities are coordinate invariants, they completely characterize the intrinsic geometric classification of the conic!\n</p>\n"
        },
        {
          "id": "u4-sec2",
          "title": "Complete Classification Taxonomy of Conic Sections",
          "content": "\n<h3>1. Non-Degenerate vs. Degenerate Conics</h3>\n<p>\nThe total discriminant $\\Delta = \\det(\\mathbf{A})$ establishes the primary topological branch:\n<ul>\n  <li><strong>Degenerate Conics ($\\Delta = 0$):</strong> The curve factors into lines or a single point:\n    <ul>\n      <li>$D = ab - h^2 < 0$: Pair of intersecting real straight lines.</li>\n      <li>$D = ab - h^2 = 0$: Pair of parallel or coincident straight lines ($g^2 - ac \\ge 0$).</li>\n      <li>$D = ab - h^2 > 0$: A single isolated point (pair of imaginary intersecting lines).</li>\n    </ul>\n  </li>\n  <li><strong>Non-Degenerate Proper Conics ($\\Delta \\ne 0$):</strong> The curve represents a genuine conic section:\n    <ul>\n      <li><strong>Ellipse ($D = ab - h^2 > 0$):</strong>\n        <ul>\n          <li>Real Ellipse if $\\Delta / (a + b) < 0$.</li>\n          <li>Imaginary Ellipse if $\\Delta / (a + b) > 0$.</li>\n          <li>Circle if $a = b$ and $h = 0$.</li>\n        </ul>\n      </li>\n      <li><strong>Parabola ($D = ab - h^2 = 0$):</strong> An open curve extending to infinity with a single axis of symmetry.</li>\n      <li><strong>Hyperbola ($D = ab - h^2 < 0$):</strong> An open curve with two separate branches and two real asymptotes.\n        <ul>\n          <li><strong>Rectangular (Equilateral) Hyperbola</strong> if $a + b = 0$ (asymptotes at right angles).</li>\n        </ul>\n      </li>\n    </ul>\n  </li>\n</ul>\n</p>\n"
        },
        {
          "id": "u4-sec3",
          "title": "Center of Central Conics & Elimination of Linear Terms",
          "content": "\n<h3>1. Determining the Center $(\\bar{x}, \\bar{y})$</h3>\n<p>\nA conic is said to be a <strong>central conic</strong> if it possesses a center of symmetry $(\\bar{x}, \\bar{y})$ such that any chord passing through the center is bisected by it. This requires $D = ab - h^2 \\ne 0$ (holding for all ellipses and hyperbolas).\nThe center is found by equating partial derivatives to zero:\n$$\\frac{\\partial F}{\\partial x} = 2(ax + hy + g) = 0 \\implies ax + hy + g = 0$$\n$$\\frac{\\partial F}{\\partial y} = 2(hx + by + f) = 0 \\implies hx + by + f = 0$$\nSolving by Cramer's rule:\n$$\\bar{x} = \\frac{hf - bg}{ab - h^2}, \\qquad \\bar{y} = \\frac{gh - af}{ab - h^2}$$\n</p>\n\n<h3>2. Translating Origin to the Center</h3>\n<p>\nTranslating the coordinate axes to the center by substituting $x = X + \\bar{x}, y = Y + \\bar{y}$ eliminates the linear terms ($gX, fY$). The transformed equation becomes:\n$$a X^2 + 2h XY + b Y^2 + c' = 0$$\nwhere the new constant term $c'$ is given by:\n$$c' = g\\bar{x} + f\\bar{y} + c = \\frac{\\Delta}{ab - h^2} = \\frac{\\Delta}{D}$$\nNotice the immense elegance of this result: the constant term is simply the quotient of the two fundamental invariants $\\Delta / D$!\n</p>\n"
        },
        {
          "id": "u4-sec4",
          "title": "Elimination of xy Cross-Term & Canonical Eigenvalue Reduction",
          "content": "\n<h3>1. Rotational Diagonalization via Eigenvalues</h3>\n<p>\nTo reduce the central equation $a X^2 + 2h XY + b Y^2 + c' = 0$ to principal axes, we rotate the axes through angle $\\theta$ given by:\n$$\\tan 2\\theta = \\frac{2h}{a - b}$$\nIn matrix terms, this is equivalent to diagonalizing the symmetric matrix $\\mathbf{A}_{2 \\times 2} = \\begin{pmatrix} a & h \\\\ h & b \\end{pmatrix}$.\nThe eigenvalues $\\lambda_1, \\lambda_2$ are the roots of the characteristic equation:\n$$\\det(\\lambda \\mathbf{I} - \\mathbf{A}_{2 \\times 2}) = 0 \\iff \\lambda^2 - (a + b)\\lambda + (ab - h^2) = 0$$\n$$\\lambda_1, \\lambda_2 = \\frac{(a + b) \\pm \\sqrt{(a - b)^2 + 4h^2}}{2}$$\n</p>\n\n<h3>2. The Standard Canonical Form</h3>\n<p>\nReferred to the principal axes $(X', Y')$, the cross term vanishes identically:\n$$\\lambda_1 X'^2 + \\lambda_2 Y'^2 + c' = 0 \\iff \\frac{X'^2}{-c'/\\lambda_1} + \\frac{Y'^2}{-c'/\\lambda_2} = 1$$\n<ul>\n  <li>If $\\lambda_1, \\lambda_2$ have the same sign (and opposite to $c'$), the curve is an <strong>ellipse</strong> with semi-axes $A = \\sqrt{-c'/\\lambda_1}, B = \\sqrt{-c'/\\lambda_2}$.</li>\n  <li>If $\\lambda_1, \\lambda_2$ have opposite signs, the curve is a <strong>hyperbola</strong>.</li>\n</ul>\n</p>\n"
        },
        {
          "id": "u4-sec5",
          "title": "Non-Central Conics: The Complete Parabola Reduction Protocol",
          "content": "\n<h3>1. The Parabola Condition ($ab - h^2 = 0$)</h3>\n<p>\nWhen $ab - h^2 = 0$, the quadratic terms form a perfect square:\n$$ax^2 + 2hxy + by^2 = (\\alpha x + \\beta y)^2, \\quad \\text{where } \\alpha = \\sqrt{a}, \\; \\beta = \\sqrt{b}, \\; \\text{and } \\alpha\\beta = h$$\nBecause $D = 0$, the conic has no finite center; it is a <strong>non-central conic (parabola)</strong>.\n</p>\n\n<h3>2. The Systematic Reduction Algorithm</h3>\n<p>\nTo reduce the parabola to canonical form $Y'^2 = 4AX'$:\n<ol>\n  <li>Group the perfect square: $(\\alpha x + \\beta y)^2 = -2gx - 2fy - c$.</li>\n  <li>Introduce an arbitrary parameter $\\lambda$:\n  $$(\\alpha x + \\beta y + \\lambda)^2 = 2(\\lambda \\alpha - g)x + 2(\\lambda \\beta - f)y + (\\lambda^2 - c)$$</li>\n  <li>Choose $\\lambda$ so that the lines $\\alpha x + \\beta y + \\lambda = 0$ (axis of the parabola) and $2(\\lambda \\alpha - g)x + 2(\\lambda \\beta - f)y + (\\lambda^2 - c) = 0$ (tangent at vertex) are strictly perpendicular:\n  $$\\alpha \\cdot 2(\\lambda \\alpha - g) + \\beta \\cdot 2(\\lambda \\beta - f) = 0 \\implies \\lambda(\\alpha^2 + \\beta^2) = \\alpha g + \\beta f \\implies \\lambda = \\frac{\\alpha g + \\beta f}{a + b}$$</li>\n  <li>Divide each side by $\\sqrt{\\alpha^2 + \\beta^2}$ and $\\sqrt{4(\\lambda\\alpha - g)^2 + 4(\\lambda\\beta - f)^2}$ respectively to obtain normalized perpendicular distances, reducing immediately to the canonical form $Y'^2 = 4AX'$!</li>\n</ol>\n</p>\n",
          "simulation": "geom2d-conic-discriminant-sim",
          "simulations": [
            "geom2d-conic-discriminant-sim"
          ]
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "Conic Identification and Invariant Computation",
          "statement": "Classify each of the following second-degree equations by computing their discriminant invariants $\\Delta$ and $D = ab - h^2$: (a) $x^2 - 4xy + 4y^2 - 2x + 4y - 3 = 0$. (b) $5x^2 + 4xy + 2y^2 - 12x - 6y + 11 = 0$. (c) $x^2 + 4xy + y^2 - 6x - 6y + 5 = 0$.",
          "steps": [
            {
              "step": "Step 1: Analyze Equation (a)",
              "math": "a = 1, h = -2, b = 4, g = -1, f = 2, c = -3 \\\\ D = ab - h^2 = 1(4) - (-2)^2 = 4 - 4 = 0 \\\\ \\Delta = \\begin{vmatrix} 1 & -2 & -1 \\\\ -2 & 4 & 2 \\\\ -1 & 2 & -3 \\end{vmatrix} = 1(-12 - 4) - (-2)(6 - (-2)) - 1(-4 - (-4)) = -16 + 16 - 0 = 0",
              "explanation": "Since $\\Delta = 0$ and $D = 0$, this represents a degenerate pair of parallel straight lines ($(x - 2y - 3)(x - 2y + 1) = 0$)."
            },
            {
              "step": "Step 2: Analyze Equation (b)",
              "math": "a = 5, h = 2, b = 2, g = -6, f = -3, c = 11 \\\\ D = ab - h^2 = 5(2) - 2^2 = 10 - 4 = 6 > 0 \\\\ \\Delta = 5(22 - 9) - 2(22 - 18) - 6(-6 - 12) = 5(13) - 2(4) - 6(-18) \\ne 0",
              "explanation": "Since $\\Delta \ne 0$ and $D > 0$, equation (b) represents a non-degenerate real Ellipse."
            },
            {
              "step": "Step 3: Analyze Equation (c)",
              "math": "a = 1, h = 2, b = 1, g = -3, f = -3, c = 5 \\\\ D = ab - h^2 = 1(1) - 2^2 = 1 - 4 = -3 < 0 \\\\ \\Delta = 1(5 - 9) - 2(10 - 9) - 3(-6 - 3) = -4 - 2 + 27 = 21 \\ne 0",
              "explanation": "Since $\\Delta \ne 0$ and $D < 0$, equation (c) represents a non-degenerate Hyperbola."
            }
          ],
          "answer": "\\text{(a) Degenerate parallel lines } (\\Delta = 0, D = 0); \\quad \\text{(b) Ellipse } (\\Delta \\ne 0, D > 0); \\quad \\text{(c) Hyperbola } (\\Delta \\ne 0, D < 0)"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "Complete Canonical Reduction and Tracing of a Central Ellipse",
          "statement": "Given the second-degree equation $5x^2 - 4xy + 8y^2 - 36 = 0$: (a) Verify that the conic is an ellipse centered at the origin. (b) Find the characteristic equation and eigenvalues $\\lambda_1, \\lambda_2$. (c) Determine the canonical form, length of major and minor semi-axes, and eccentricity.",
          "steps": [
            {
              "step": "Step 1: Verify Center and Conic Type",
              "math": "a = 5, \\; h = -2, \\; b = 8, \\; g = 0, \\; f = 0, \\; c = -36 \\\\ D = ab - h^2 = 5(8) - (-2)^2 = 40 - 4 = 36 > 0 \\\\ \\Delta = c(ab - h^2) = -36(36) = -1296 \\ne 0",
              "explanation": "Since $g = f = 0$, the center is already at $(0, 0)$. Because $\\Delta \ne 0$ and $D > 0$, it is a central ellipse."
            },
            {
              "step": "Step 2: Characteristic Equation and Eigenvalues",
              "math": "\\lambda^2 - (a+b)\\lambda + (ab-h^2) = 0 \\implies \\lambda^2 - 13\\lambda + 36 = 0 \\implies (\\lambda - 4)(\\lambda - 9) = 0 \\\\ \\lambda_1 = 4, \\qquad \\lambda_2 = 9",
              "explanation": "The eigenvalues are $\\lambda_1 = 4$ and $\\lambda_2 = 9$."
            },
            {
              "step": "Step 3: Canonical Equation and Semi-Axes",
              "math": "\\lambda_1 X^2 + \\lambda_2 Y^2 + c = 0 \\implies 4X^2 + 9Y^2 = 36 \\implies \\frac{X^2}{9} + \\frac{Y^2}{4} = 1 \\\\ \\text{Major semi-axis: } A = \\sqrt{9} = 3, \\qquad \\text{Minor semi-axis: } B = \\sqrt{4} = 2 \\\\ \\text{Eccentricity: } e = \\sqrt{1 - \\frac{B^2}{A^2}} = \\sqrt{1 - \\frac{4}{9}} = \\frac{\\sqrt{5}}{3}",
              "explanation": "The rotation angle satisfies $\tan 2\theta = \\frac{2h}{a-b} = \\frac{-4}{5-8} = \\frac{4}{3} \\implies \theta = \\frac{1}{2}\\arctan(4/3) \\approx 26.57^\\circ$."
            }
          ],
          "answer": "\\text{Canonical Form: } \\frac{X^2}{9} + \\frac{Y^2}{4} = 1; \\quad A = 3, \\; B = 2; \\quad e = \\frac{\\sqrt{5}}{3} \\approx 0.745; \\quad \\theta \\approx 26.57^\\circ"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "Complete Parabolic Reduction Protocol for a Non-Central Conic",
          "statement": "Reduce the non-central second-degree equation $(x + 2y)^2 - 4x + 2y - 5 = 0 \\iff x^2 + 4xy + 4y^2 - 4x + 2y - 5 = 0$ to canonical form $Y'^2 = 4AX'$. Determine the vertex, focus, axis equation, tangent at vertex, and latus rectum.",
          "steps": [
            {
              "step": "Step 1: Parameterize the Perfect Square",
              "math": "(x + 2y + \\lambda)^2 = (x + 2y)^2 + 2\\lambda(x + 2y) + \\lambda^2 \\\\ = (4x - 2y + 5) + 2\\lambda x + 4\\lambda y + \\lambda^2 = (2\\lambda + 4)x + (4\\lambda - 2)y + (\\lambda^2 + 5)",
              "explanation": "We rewrite $(x + 2y + \\lambda)^2 = (2\\lambda + 4)x + (4\\lambda - 2)y + (\\lambda^2 + 5)$."
            },
            {
              "step": "Step 2: Determine $\\lambda$ to Ensure Orthogonality",
              "math": "\\text{Line 1: } x + 2y + \\lambda = 0 \\quad (\\mathbf{n}_1 = (1, 2)) \\\\ \\text{Line 2: } (2\\lambda + 4)x + (4\\lambda - 2)y + (\\lambda^2 + 5) = 0 \\quad (\\mathbf{n}_2 = (2\\lambda + 4, 4\\lambda - 2)) \\\\ \\mathbf{n}_1 \\cdot \\mathbf{n}_2 = 1(2\\lambda + 4) + 2(4\\lambda - 2) = 2\\lambda + 4 + 8\\lambda - 4 = 10\\lambda = 0 \\implies \\lambda = 0",
              "explanation": "Remarkably, $\\lambda = 0$ satisfies the orthogonality condition!"
            },
            {
              "step": "Step 3: Normalize to Standard Distance Coordinates",
              "math": "\\lambda = 0 \\implies (x + 2y)^2 = 4x - 2y + 5 \\\\ \\left(\\frac{x + 2y}{\\sqrt{1^2 + 2^2}}\\right)^2 = \\frac{4x - 2y + 5}{5} = \\frac{\\sqrt{4^2 + (-2)^2}}{5} \\left(\\frac{4x - 2y + 5}{\\sqrt{20}}\\right) = \\frac{\\sqrt{20}}{5} Y' = \\frac{2\\sqrt{5}}{5} Y' = \\frac{2}{\\sqrt{5}} X'",
              "explanation": "Let $Y' = \\frac{x + 2y}{\\sqrt{5}}$ and $X' = \\frac{4x - 2y + 5}{\\sqrt{20}} = \\frac{4x - 2y + 5}{2\\sqrt{5}}$. Then $Y'^2 = \\frac{2}{\\sqrt{5}} X' = 4 \\left(\\frac{1}{2\\sqrt{5}}\\right) X'$."
            },
            {
              "step": "Step 4: Extract Geometric Elements",
              "math": "\\text{Axis: } x + 2y = 0 \\\\ \\text{Tangent at Vertex: } 4x - 2y + 5 = 0 \\\\ \\text{Vertex: Intersection of Axis and Tangent: } x = -2y \\implies 4(-2y) - 2y + 5 = 0 \\implies -10y = -5 \\implies y = \\frac{1}{2}, \\; x = -1 \\\\ \\text{Latus Rectum: } 4A = \\frac{2}{\\sqrt{5}}",
              "explanation": "The canonical equation is $Y'^2 = \\frac{2}{\\sqrt{5}}X'$, centered at vertex $(-1, 1/2)$."
            }
          ],
          "answer": "\\text{Canonical Form: } Y'^2 = \\frac{2}{\\sqrt{5}}X'; \\quad \\text{Vertex: } \\left(-1, \\frac{1}{2}\\right); \\quad \\text{Axis: } x + 2y = 0; \\quad \\text{Latus Rectum: } \\frac{2}{\\sqrt{5}}"
        }
      ],
      "simulations": [
        "geom2d-conic-discriminant-sim"
      ],
      "id": "unit4",
      "unitId": "unit4-geom2d",
      "leadSummary": "Comprehensive theory of general quadratic equations: universal matrix formulation x^T A x = 0; rigid motion invariants trace I_1 = a + b, discriminant I_2 = ab - h^2, and total determinant I_3 = Delta; complete classification taxonomy for proper conics (ellipse, parabola, hyperbola) and degenerate varieties; center determination via partial derivatives and elimination of linear terms; rotational diagonalization and eigenvalue canonical reduction lambda_1 X^2 + lambda_2 Y^2 + Delta/D = 0; and the complete reduction protocol for non-central parabolas Y'^2 = 4AX'."
    },
    {
      "unitNumber": 5,
      "number": 5,
      "title": "In-Depth Study of the Parabola",
      "description": "Exhaustive geometrical and analytical treatment of the parabola: focus-directrix definition SP = PM and canonical derivation y^2 = 4ax; geometric elements and alternative coordinate orientations; rational parametrization (at^2, 2at) and the focal chord theorem t_1 t_2 = -1; semi-latus rectum as harmonic mean of focal segments; tangents in point, slope, and parametric forms; intersection of tangents (at_1 t_2, a(t_1 + t_2)) and the orthoptic theorem; normal equations y = mx - 2am - am^3 and the three co-normal points theorem; optical reflection property of parabolic mirrors; and constancy of the subnormal MN = 2a.",
      "sections": [
        {
          "id": "u5-sec1",
          "title": "The Parabola: Focus-Directrix Definition, Canonical Forms & Latus Rectum",
          "content": "\n<h3>1. The Focus-Directrix Locus Definition</h3>\n<p>\nA <strong>parabola</strong> is defined geometrically as the planar locus of a point $P(x, y)$ that moves such that its distance from a fixed point $S$ (the <em>focus</em>) is strictly equal to its perpendicular distance from a fixed straight line $D$ (the <em>directrix</em>):\n$$\\frac{SP}{PM} = e = 1 \\iff SP = PM$$\nwhere $M$ is the foot of the perpendicular from $P$ to directrix $D$.\n</p>\n<p>\nTo derive the canonical Cartesian equation:\n<ol>\n  <li>Choose the focus at $S(a, 0)$ with $a > 0$.</li>\n  <li>Choose the directrix as the vertical line $D: x + a = 0 \\iff x = -a$.</li>\n  <li>The point $M$ has coordinates $(-a, y)$.</li>\n  <li>Equating distances:\n  $$SP^2 = PM^2 \\implies (x - a)^2 + (y - 0)^2 = (x - (-a))^2 + (y - y)^2$$\n  $$x^2 - 2ax + a^2 + y^2 = (x + a)^2 = x^2 + 2ax + a^2$$\n  Canceling $x^2 + a^2$ on both sides yields the classical canonical equation:\n  $$\\mathbf{y^2 = 4ax}$$\n  </li>\n</ol>\n</p>\n\n<h3>2. Geometric Elements of the Standard Parabola ($y^2 = 4ax$)</h3>\n<p>\n<ul>\n  <li><strong>Vertex ($V$):</strong> The origin $V(0, 0)$, midpoint of the perpendicular from focus to directrix.</li>\n  <li><strong>Axis of Symmetry:</strong> The $x$-axis ($y = 0$). The curve is symmetric about this line because $y = \\pm 2\\sqrt{ax}$.</li>\n  <li><strong>Focus ($S$):</strong> $S(a, 0)$.</li>\n  <li><strong>Directrix ($D$):</strong> The vertical line $x = -a$.</li>\n  <li><strong>Focal Distance:</strong> For any point $P(x_1, y_1)$ on the curve:\n  $$SP = x_1 + a$$</li>\n  <li><strong>Latus Rectum ($LL'$):</strong> The focal chord perpendicular to the axis of symmetry. Substituting $x = a$ into $y^2 = 4ax$ yields $y^2 = 4a^2 \\implies y = \\pm 2a$.\n  The extremities are $L(a, 2a)$ and $L'(a, -2a)$, and its total length is:\n  $$\\mathbf{Length(LL') = 4a}$$</li>\n</ul>\n</p>\n\n<h3>3. Canonical Orientations of the Parabola</h3>\n<p>\nDepending on the direction of opening and orientation of the axis:\n<table style=\"width:100%; border-collapse:collapse; margin:16px 0; font-size:0.95em;\">\n<thead>\n<tr style=\"border-bottom:2px solid var(--border-color); text-align:left;\">\n<th style=\"padding:8px;\">Equation</th>\n<th style=\"padding:8px;\">Axis</th>\n<th style=\"padding:8px;\">Opens</th>\n<th style=\"padding:8px;\">Focus</th>\n<th style=\"padding:8px;\">Directrix</th>\n</tr>\n</thead>\n<tbody>\n<tr style=\"border-bottom:1px solid var(--border-color);\"><td style=\"padding:8px;\">$y^2 = 4ax$</td><td style=\"padding:8px;\">$y = 0$</td><td style=\"padding:8px;\">Right ($x \\ge 0$)</td><td style=\"padding:8px;\">$(a, 0)$</td><td style=\"padding:8px;\">$x = -a$</td></tr>\n<tr style=\"border-bottom:1px solid var(--border-color);\"><td style=\"padding:8px;\">$y^2 = -4ax$</td><td style=\"padding:8px;\">$y = 0$</td><td style=\"padding:8px;\">Left ($x \\le 0$)</td><td style=\"padding:8px;\">$(-a, 0)$</td><td style=\"padding:8px;\">$x = a$</td></tr>\n<tr style=\"border-bottom:1px solid var(--border-color);\"><td style=\"padding:8px;\">$x^2 = 4ay$</td><td style=\"padding:8px;\">$x = 0$</td><td style=\"padding:8px;\">Upward ($y \\ge 0$)</td><td style=\"padding:8px;\">$(0, a)$</td><td style=\"padding:8px;\">$y = -a$</td></tr>\n<tr><td style=\"padding:8px;\">$x^2 = -4ay$</td><td style=\"padding:8px;\">$x = 0$</td><td style=\"padding:8px;\">Downward ($y \\le 0$)</td><td style=\"padding:8px;\">$(0, -a)$</td><td style=\"padding:8px;\">$y = a$</td></tr>\n</tbody>\n</table>\n</p>\n"
        },
        {
          "id": "u5-sec2",
          "title": "Parametric Representation & Focal Chord Geometry",
          "content": "\n<h3>1. The Standard Rational Parametrization</h3>\n<p>\nThe equation $y^2 = 4ax$ can be parametrized rationally without radicals by setting $y = 2at$:\n$$(2at)^2 = 4ax \\implies 4a^2 t^2 = 4ax \\implies x = at^2$$\nThus, any point on the parabola is uniquely identified by the real parameter $t \\in \\mathbb{R}$:\n$$P(t) = (a t^2, 2 a t)$$\nNotice that the parameter $t$ is the reciprocal of the slope of the tangent at $P$ ($m = 1/t$).\n</p>\n\n<h3>2. Chord Joining Two Points & The Focal Chord Theorem</h3>\n<p>\nLet $P(t_1) = (a t_1^2, 2 a t_1)$ and $Q(t_2) = (a t_2^2, 2 a t_2)$ be two distinct points on the parabola. The slope of the secant chord $PQ$ is:\n$$m_{PQ} = \\frac{2a t_2 - 2a t_1}{a t_2^2 - a t_1^2} = \\frac{2a(t_2 - t_1)}{a(t_2 - t_1)(t_2 + t_1)} = \\frac{2}{t_1 + t_2}$$\nThe equation of the chord $PQ$ in point-slope form is:\n$$y - 2a t_1 = \\frac{2}{t_1 + t_2}(x - a t_1^2) \\iff (t_1 + t_2)y = 2x + 2a t_1 t_2$$\n</p>\n<p>\n<strong>The Fundamental Focal Chord Condition:</strong>\nIf the chord $PQ$ passes through the focus $S(a, 0)$, substituting $x = a, y = 0$ yields:\n$$(t_1 + t_2)(0) = 2a + 2a t_1 t_2 \\implies 2a(1 + t_1 t_2) = 0 \\iff \\mathbf{t_1 t_2 = -1 \\iff t_2 = -\\frac{1}{t_1}}$$\nThis theorem leads to two crucial geometric properties:\n<ul>\n  <li><strong>Harmonic Mean Property:</strong> The semi-latus rectum $2a$ is the harmonic mean of the two focal segments $SP$ and $SQ$:\n  $$SP = a(t_1^2 + 1), \\quad SQ = a(t_2^2 + 1) = a\\left(\\frac{1}{t_1^2} + 1\\right) = a\\frac{t_1^2 + 1}{t_1^2}$$\n  $$\\frac{1}{SP} + \\frac{1}{SQ} = \\frac{1}{a(t_1^2 + 1)} + \\frac{t_1^2}{a(t_1^2 + 1)} = \\frac{1 + t_1^2}{a(1 + t_1^2)} = \\frac{1}{a} \\iff \\mathbf{\\frac{2}{PQ_{\\text{harm}}} = \\frac{1}{a}}$$</li>\n  <li><strong>Total Length of Focal Chord:</strong>\n  $$PQ = SP + SQ = a\\left(t_1 + \\frac{1}{t_1}\\right)^2 \\ge 4a$$\n  with minimum length $4a$ occurring when $t_1 = 1$ (the latus rectum).</li>\n</ul>\n</p>\n"
        },
        {
          "id": "u5-sec3",
          "title": "Tangents to the Parabola: Point, Slope & Parametric Forms",
          "content": "\n<h3>1. The Three Canonical Forms of Tangents</h3>\n<p>\nFor the parabola $y^2 = 4ax$:\n<ol>\n  <li><strong>Point Form:</strong> Tangent at $P(x_1, y_1)$ on the curve:\n  $$y y_1 = 2a(x + x_1)$$</li>\n  <li><strong>Parametric Form:</strong> Tangent at $P(t) = (at^2, 2at)$:\n  $$y(2at) = 2a(x + at^2) \\iff \\mathbf{t y = x + a t^2}$$\n  The slope of this tangent is $m = 1/t$.</li>\n  <li><strong>Slope Form:</strong> Replacing $t = 1/m$:\n  $$\\frac{y}{m} = x + \\frac{a}{m^2} \\iff \\mathbf{y = m x + \\frac{a}{m} \\quad (m \\ne 0)}$$\n  The point of tangency is $\\left(\\frac{a}{m^2}, \\frac{2a}{m}\\right)$.</li>\n</ol>\n</p>\n\n<h3>2. Point of Intersection of Two Tangents</h3>\n<p>\nLet the tangents be drawn at $P(t_1)$ and $Q(t_2)$:\n$$t_1 y = x + a t_1^2, \\qquad t_2 y = x + a t_2^2$$\nSubtracting the equations:\n$$(t_1 - t_2)y = a(t_1^2 - t_2^2) = a(t_1 - t_2)(t_1 + t_2) \\implies y = a(t_1 + t_2)$$\nSubstituting back into $x = t_1 y - a t_1^2$:\n$$x = t_1[a(t_1 + t_2)] - a t_1^2 = a t_1^2 + a t_1 t_2 - a t_1^2 = a t_1 t_2$$\nThus, the intersection of tangents at $t_1$ and $t_2$ is:\n$$\\mathbf{T = (a t_1 t_2, \\; a(t_1 + t_2))}$$\nNotice: The $x$-coordinate is the geometric mean of the abscissae, and the $y$-coordinate is the arithmetic mean of the ordinates of $P$ and $Q$!\n</p>\n\n<h3>3. Orthoptic Property (The Director Circle is the Directrix)</h3>\n<p>\nIf the tangents at $P(t_1)$ and $Q(t_2)$ are mutually perpendicular, the product of their slopes is $-1$:\n$$m_1 m_2 = \\left(\\frac{1}{t_1}\\right)\\left(\\frac{1}{t_2}\\right) = -1 \\iff t_1 t_2 = -1$$\nSubstituting $t_1 t_2 = -1$ into the intersection coordinate:\n$$x_T = a(t_1 t_2) = a(-1) = -a$$\n<strong>The Orthoptic Theorem:</strong> The locus of the point of intersection of two mutually perpendicular tangents to a parabola is its directrix $x = -a$! (For a parabola, the director circle degenerates into its directrix).\n</p>\n"
        },
        {
          "id": "u5-sec4",
          "title": "Normals to the Parabola & The Three Co-Normal Points",
          "content": "\n<h3>1. Equations of the Normal</h3>\n<p>\nThe normal at point $P(x_1, y_1)$ on $y^2 = 4ax$ has slope $m_N = -y_1/(2a)$:\n$$y - y_1 = -\\frac{y_1}{2a}(x - x_1)$$\nIn terms of the parameter $t$ ($m_N = -t$):\n$$y - 2at = -t(x - at^2) \\iff \\mathbf{y + t x = 2 a t + a t^3}$$\nSetting slope $m = -t$:\n$$\\mathbf{y = m x - 2 a m - a m^3}$$\n</p>\n\n<h3>2. The Three Co-Normal Points Theorem</h3>\n<p>\nIf a normal passes through a given point $(\\alpha, \\beta)$, then:\n$$\\beta = m \\alpha - 2am - am^3 \\iff a m^3 + (2a - \\alpha)m + \\beta = 0$$\nThis is a cubic polynomial in the slope $m$. By the Fundamental Theorem of Algebra, it has three roots $m_1, m_2, m_3$ (at least one of which must be real). Thus, <strong>from any point in the plane, up to three normals can be drawn to a parabola</strong>!\n</p>\n<p>\nBy Vi\u00e8te's formulas for $a m^3 + 0 m^2 + (2a - \\alpha)m + \\beta = 0$:\n$$m_1 + m_2 + m_3 = 0$$\n$$m_1 m_2 + m_2 m_3 + m_3 m_1 = \\frac{2a - \\alpha}{a}$$\n$$m_1 m_2 m_3 = -\\frac{\\beta}{a}$$\nSince the ordinate of the feet of the normals is $y_i = 2am_i$ (using $m_i = -t_i$):\n$$y_1 + y_2 + y_3 = -2a(m_1 + m_2 + m_3) = -2a(0) = \\mathbf{0}$$\n<strong>Theorem:</strong> The algebraic sum of the ordinates of the feet of three co-normal points on a parabola is always identically zero! Consequently, the centroid of the triangle formed by the three co-normal points always lies strictly on the axis of the parabola.\n</p>\n"
        },
        {
          "id": "u5-sec5",
          "title": "Optical Reflection Property & Subtangent/Subnormal Invariants",
          "content": "\n<h3>1. The Optical Reflection Property of the Parabola</h3>\n<p>\nLet $P(at^2, 2at)$ be a point on the parabola $y^2 = 4ax$. Let a light ray traveling parallel to the axis of symmetry (horizontal) strike the parabolic mirror at $P$.\nThe tangent at $P$ makes an angle $\\alpha$ with the axis where $\\tan \\alpha = 1/t$.\nThe vector from the focus $S(a, 0)$ to $P$ makes an angle $\\theta$ with the axis:\n$$\\tan \\theta = \\frac{2at}{at^2 - a} = \\frac{2t}{t^2 - 1} = \\tan(2\\alpha)$$\nTherefore, the angle of the focal ray is exactly twice the angle of the tangent ray: $\\theta = 2\\alpha$.\nThis proves that the tangent line bisects the angle between the focal ray $SP$ and the horizontal incident ray!\nBy the law of specular reflection (angle of incidence equals angle of reflection):\n$$\\mathbf{\\text{All rays parallel to the axis of symmetry reflect precisely through the focus } S!}$$\nThis profound property is the physical foundation of satellite dishes, solar concentrators, radio telescopes, and automotive parabolic headlamps.\n</p>\n\n<h3>2. Subtangent and Subnormal Lengths</h3>\n<p>\nLet the tangent and normal at $P(x_1, y_1)$ intersect the $x$-axis at $T$ and $N$ respectively, and let $M(x_1, 0)$ be the projection of $P$ on the axis:\n<ul>\n  <li><strong>Subtangent ($TM$):</strong> The tangent is $y y_1 = 2a(x + x_1)$. Setting $y = 0 \\implies x_T = -x_1$. Thus:\n  $$TM = |x_1 - (-x_1)| = \\mathbf{2 x_1}$$\n  The vertex $V(0, 0)$ is the exact midpoint of $TM$!</li>\n  <li><strong>Subnormal ($MN$):</strong> The normal is $y - y_1 = -\\frac{y_1}{2a}(x - x_1)$. Setting $y = 0 \\implies -y_1 = -\\frac{y_1}{2a}(x_N - x_1) \\implies x_N - x_1 = 2a$. Thus:\n  $$MN = x_N - x_1 = \\mathbf{2a = \\text{Constant Everywhere!}}$$\n  The subnormal of a parabola is constant at all points on the curve and equal to the semi-latus rectum!</li>\n</ul>\n</p>\n",
          "simulation": "geom2d-parabola-optics-sim",
          "simulations": [
            "geom2d-parabola-optics-sim"
          ]
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "Standard Parabola Geometric Elements and Tangent Equation",
          "statement": "For the parabola $y^2 = 12x$: (a) Determine the coordinates of the focus, equation of the directrix, and length of the latus rectum. (b) Find the parametric value $t$ for the point $P(3, 6)$. (c) Formulate the equations of the tangent and normal lines at $P(3, 6)$.",
          "steps": [
            {
              "step": "Step 1: Identify Standard Parameters",
              "math": "y^2 = 4ax = 12x \\implies 4a = 12 \\implies a = 3 \\\\ \\text{Focus: } S(a, 0) = (3, 0) \\\\ \\text{Directrix: } x = -a \\implies x = -3 \\iff x + 3 = 0 \\\\ \\text{Latus Rectum: } 4a = 12",
              "explanation": "Comparing with $y^2 = 4ax$ yields $a = 3$."
            },
            {
              "step": "Step 2: Find Parametric Value $t$ at $P(3, 6)$",
              "math": "P(at^2, 2at) = (3t^2, 6t) = (3, 6) \\implies 6t = 6 \\implies t = 1",
              "explanation": "Check: $3(1)^2 = 3 = x_P$. Thus $t = 1$."
            },
            {
              "step": "Step 3: Tangent and Normal at $P(3, 6)$",
              "math": "\\text{Tangent: } ty = x + at^2 \\implies (1)y = x + 3(1)^2 \\implies x - y + 3 = 0 \\\\ \\text{Normal: } y + tx = 2at + at^3 \\implies y + (1)x = 2(3)(1) + 3(1)^3 = 6 + 3 = 9 \\implies x + y - 9 = 0",
              "explanation": "The tangent is $x - y + 3 = 0$ (slope $1$) and the normal is $x + y - 9 = 0$ (slope $-1$, mutually perpendicular)."
            }
          ],
          "answer": "\\text{Focus: } (3, 0); \\quad \\text{Directrix: } x = -3; \\quad \\text{Latus Rectum: } 12; \\quad \\text{Tangent: } x - y + 3 = 0; \\quad \\text{Normal: } x + y - 9 = 0"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "Intersection of Tangents and Orthoptic Property Verification",
          "statement": "Tangents are drawn to the parabola $y^2 = 8x$ from the external point $P(-2, 3)$. (a) Verify that point $P$ lies on the directrix of the parabola. (b) Find the individual equations of the two tangents. (c) Prove that the two tangents are mutually perpendicular.",
          "steps": [
            {
              "step": "Step 1: Verify Position on Directrix",
              "math": "y^2 = 4ax = 8x \\implies a = 2 \\\\ \\text{Directrix: } x = -a = -2 \\\\ \\text{Point } P(-2, 3) \\text{ has abscissa } x = -2, \\text{ so it lies strictly on the directrix!}",
              "explanation": "By the Orthoptic Theorem, tangents drawn from any point on the directrix must be mutually perpendicular."
            },
            {
              "step": "Step 2: Use Slope Form of Tangents",
              "math": "y = mx + \\frac{a}{m} \\implies y = mx + \\frac{2}{m} \\implies m y = m^2 x + 2 \\\\ \\text{Passing through } (-2, 3): \\quad 3m = m^2(-2) + 2 \\implies 2m^2 + 3m - 2 = 0 \\\\ (2m - 1)(m + 2) = 0 \\implies m_1 = \\frac{1}{2}, \\quad m_2 = -2",
              "explanation": "The two slopes are $m_1 = 1/2$ and $m_2 = -2$."
            },
            {
              "step": "Step 3: Tangent Equations and Perpendicularity",
              "math": "\\text{Tangent 1 } (m = 1/2): \\quad y = \\frac{1}{2}x + \\frac{2}{1/2} = \\frac{1}{2}x + 4 \\implies x - 2y + 8 = 0 \\\\ \\text{Tangent 2 } (m = -2): \\quad y = -2x + \\frac{2}{-2} = -2x - 1 \\implies 2x + y + 1 = 0 \\\\ m_1 \\cdot m_2 = \\left(\\frac{1}{2}\\right)(-2) = -1 \\implies \\text{Strictly Perpendicular!}",
              "explanation": "The product of the slopes is $-1$, confirming the Orthoptic Theorem."
            }
          ],
          "answer": "\\text{Directrix: } x = -2 \\implies P \\text{ lies on directrix}; \\quad \\text{Tangents: } x - 2y + 8 = 0 \\text{ and } 2x + y + 1 = 0; \\quad m_1 m_2 = -1 \\implies \\text{Orthogonal}"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "Co-Normal Points: Locus of Points Subtending Orthogonal Normals",
          "statement": "Prove that the locus of a point $(\\alpha, \\beta)$ from which two of the three normals to the parabola $y^2 = 4ax$ are mutually perpendicular is the parabola $y^2 = a(x - 3a)$.",
          "steps": [
            {
              "step": "Step 1: Cubic Equation for Normal Slopes",
              "math": "\\text{The cubic equation in normal slope } m \\text{ is: } a m^3 + (2a - \\alpha)m + \\beta = 0 \\\\ m_1 + m_2 + m_3 = 0, \\quad m_1 m_2 + m_2 m_3 + m_3 m_1 = \\frac{2a - \\alpha}{a}, \\quad m_1 m_2 m_3 = -\\frac{\\beta}{a}",
              "explanation": "Vi\u00e8te's relations govern the three normal slopes."
            },
            {
              "step": "Step 2: Apply the Orthogonality Condition $m_1 m_2 = -1$",
              "math": "m_1 m_2 = -1 \\implies (-1)m_3 = -\\frac{\\beta}{a} \\implies m_3 = \\frac{\\beta}{a}",
              "explanation": "Substituting $m_1 m_2 = -1$ into the product of roots gives the third root $m_3 = \\beta/a$."
            },
            {
              "step": "Step 3: Substitute $m_3$ into the Cubic Equation",
              "math": "a \\left(\\frac{\\beta}{a}\\right)^3 + (2a - \\alpha)\\left(\\frac{\\beta}{a}\\right) + \\beta = 0 \\\\ \\frac{\\beta^3}{a^2} + \\frac{(2a - \\alpha)\\beta}{a} + \\beta = 0 \\implies \\beta \\left[ \\frac{\\beta^2}{a^2} + \\frac{2a - \\alpha}{a} + 1 \\right] = 0",
              "explanation": "Since $\\beta \ne 0$ for non-trivial solutions: $\\frac{\\beta^2}{a^2} + \\frac{2a - \\alpha + a}{a} = 0 \\implies \\frac{\\beta^2}{a^2} + \\frac{3a - \\alpha}{a} = 0$."
            },
            {
              "step": "Step 4: Simplify to Locus Equation",
              "math": "\\frac{\\beta^2}{a^2} = \\frac{\\alpha - 3a}{a} \\implies \\beta^2 = a(\\alpha - 3a)",
              "explanation": "Replacing $(\\alpha, \\beta)$ with current coordinates $(x, y)$ gives the locus $y^2 = a(x - 3a)$."
            }
          ],
          "answer": "\\text{Locus: } y^2 = a(x - 3a) \\text{ (Parabola with vertex at } (3a, 0) \\text{ and latus rectum } a\\text{)}"
        }
      ],
      "simulations": [
        "geom2d-parabola-optics-sim"
      ],
      "id": "unit5",
      "unitId": "unit5-geom2d",
      "leadSummary": "Exhaustive geometrical and analytical treatment of the parabola: focus-directrix definition SP = PM and canonical derivation y^2 = 4ax; geometric elements and alternative coordinate orientations; rational parametrization (at^2, 2at) and the focal chord theorem t_1 t_2 = -1; semi-latus rectum as harmonic mean of focal segments; tangents in point, slope, and parametric forms; intersection of tangents (at_1 t_2, a(t_1 + t_2)) and the orthoptic theorem; normal equations y = mx - 2am - am^3 and the three co-normal points theorem; optical reflection property of parabolic mirrors; and constancy of the subnormal MN = 2a."
    },
    {
      "unitNumber": 6,
      "number": 6,
      "title": "In-Depth Study of the Ellipse",
      "description": "Exhaustive treatment of the ellipse: focus-directrix definition e < 1 and canonical derivation x^2/a^2 + y^2/b^2 = 1; sum of focal distances SP + S'P = 2a and the gardener's construction; auxiliary circle x^2 + y^2 = a^2 and eccentric angle phi; area pi*a*b; tangents in point, slope, and parametric forms; director circle x^2 + y^2 = a^2 + b^2 and orthogonal tangent loci; normal equation a^2 x/x_1 - b^2 y/y_1 = a^2 - b^2; conjugate diameters and Apollonius' first (CP^2 + CD^2 = a^2 + b^2) and second (area = 4ab) theorems; optical and acoustic reflection properties; and the product of focal perpendiculars to any tangent p_1 p_2 = b^2.",
      "sections": [
        {
          "id": "u6-sec1",
          "title": "The Ellipse: Focus-Directrix Definition, Canonical Form & Metric Relations",
          "content": "\n<h3>1. The Focus-Directrix Definition ($e < 1$)</h3>\n<p>\nAn <strong>ellipse</strong> is the planar locus of a point $P(x, y)$ that moves such that the ratio of its distance from a fixed focus $S(ae, 0)$ to its distance from a fixed directrix line $D: x = a/e$ is a constant eccentricity $e \\in (0, 1)$:\n$$\\frac{SP}{PM} = e \\iff SP = e \\cdot PM$$\nLet $P(x, y)$ be any point on the curve. Then:\n$$SP^2 = e^2 PM^2 \\implies (x - ae)^2 + y^2 = e^2 \\left(x - \\frac{a}{e}\\right)^2 = (ex - a)^2$$\n$$x^2 - 2aex + a^2 e^2 + y^2 = e^2 x^2 - 2aex + a^2$$\nCanceling $-2aex$ and grouping terms:\n$$(1 - e^2)x^2 + y^2 = a^2(1 - e^2) \\iff \\frac{x^2}{a^2} + \\frac{y^2}{a^2(1 - e^2)} = 1$$\nDefining the minor semi-axis $b > 0$ by the fundamental relation:\n$$\\mathbf{b^2 \\equiv a^2(1 - e^2) \\iff e = \\sqrt{1 - \\frac{b^2}{a^2}} < 1}$$\nyields the universal canonical equation of the ellipse:\n$$\\mathbf{\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1 \\quad (a > b > 0)}$$\n</p>\n\n<h3>2. The Two Foci and The Constant Sum of Focal Radii</h3>\n<p>\nBy symmetry about the $y$-axis, the ellipse possesses a second focus $S'(-ae, 0)$ and a second directrix $D': x = -a/e$.\nThe focal distances to any point $P(x, y)$ on the ellipse are:\n$$SP = a - ex, \\qquad S'P = a + ex$$\nAdding the two distances:\n$$SP + S'P = (a - ex) + (a + ex) = \\mathbf{2a = \\text{Constant Everywhere!}}$$\n<strong>The Gardener's / Focal Distance Theorem:</strong> An ellipse is the locus of all points whose sum of distances from two fixed foci $S$ and $S'$ is constant and equal to the major axis $2a$.\n</p>\n\n<h3>3. Canonical Geometric Elements</h3>\n<p>\n<ul>\n  <li><strong>Center ($C$):</strong> Origin $(0, 0)$.</li>\n  <li><strong>Major Axis:</strong> Segment $A'A$ along the $x$-axis, length $2a$.</li>\n  <li><strong>Minor Axis:</strong> Segment $B'B$ along the $y$-axis, length $2b$.</li>\n  <li><strong>Foci:</strong> $S(ae, 0)$ and $S'(-ae, 0)$, distance between foci $SS' = 2ae$.</li>\n  <li><strong>Directrices:</strong> $x = \\pm a/e$, distance between directrices $2a/e$.</li>\n  <li><strong>Latus Rectum:</strong> Chord through focus perpendicular to major axis. Substituting $x = ae$:\n  $$\\frac{a^2 e^2}{a^2} + \\frac{y^2}{b^2} = 1 \\implies \\frac{y^2}{b^2} = 1 - e^2 = \\frac{b^2}{a^2} \\implies y = \\pm \\frac{b^2}{a} \\implies \\mathbf{Length = \\frac{2b^2}{a}}$$</li>\n</ul>\n</p>\n"
        },
        {
          "id": "u6-sec2",
          "title": "Auxiliary Circle, Eccentric Angle & Parametric Coordinates",
          "content": "\n<h3>1. The Auxiliary Circle</h3>\n<p>\nThe circle described on the major axis $A'A$ of the ellipse as diameter is termed the <strong>auxiliary circle</strong>.\nIts equation is:\n$$x^2 + y^2 = a^2$$\nLet $P(x, y)$ be any point on the ellipse. Draw a vertical ordinate through $P$ and extend it to meet the auxiliary circle at $Q(x, Y)$.\nBecause $Q$ lies on the auxiliary circle, $x = a \\cos \\phi$, where $\\phi$ is the angle $\\angle OCQ$ measured from the major axis.\nSubstituting $x = a \\cos \\phi$ into the ellipse equation:\n$$\\frac{a^2 \\cos^2 \\phi}{a^2} + \\frac{y^2}{b^2} = 1 \\implies \\cos^2 \\phi + \\frac{y^2}{b^2} = 1 \\implies \\frac{y^2}{b^2} = \\sin^2 \\phi \\implies y = b \\sin \\phi$$\nThe angle $\\phi \\in [0, 2\\pi)$ is termed the <strong>eccentric angle</strong> of point $P$.\n</p>\n\n<h3>2. Standard Parametric Form</h3>\n<p>\nThe parametric coordinates of any point on the ellipse are:\n$$\\mathbf{P(\\phi) = (a \\cos \\phi, \\; b \\sin \\phi)}$$\nNotice the vertical scaling relation between the ellipse and its auxiliary circle:\n$$\\frac{y_P}{Y_Q} = \\frac{b \\sin \\phi}{a \\sin \\phi} = \\frac{b}{a} = \\text{Constant}$$\nAn ellipse is an auxiliary circle uniformly compressed vertically by the factor $b/a$!\nConsequently, the area of the ellipse is:\n$$\\operatorname{Area}(\\text{Ellipse}) = \\frac{b}{a} \\times \\operatorname{Area}(\\text{Auxiliary Circle}) = \\frac{b}{a}(\\pi a^2) = \\mathbf{\\pi a b}$$\n</p>\n"
        },
        {
          "id": "u6-sec3",
          "title": "Tangents, Normals & The Director Circle",
          "content": "\n<h3>1. Equations of the Tangent</h3>\n<p>\n<ol>\n  <li><strong>Point Form:</strong> Tangent at $P(x_1, y_1)$ on the ellipse:\n  $$\\mathbf{\\frac{x x_1}{a^2} + \\frac{y y_1}{b^2} = 1}$$</li>\n  <li><strong>Parametric Form:</strong> Tangent at $P(\\phi) = (a\\cos\\phi, b\\sin\\phi)$:\n  $$\\mathbf{\\frac{x \\cos \\phi}{a} + \\frac{y \\sin \\phi}{b} = 1}$$</li>\n  <li><strong>Slope Form:</strong> A line $y = mx + c$ is tangent to $\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$ if and only if $c^2 = a^2 m^2 + b^2$:\n  $$\\mathbf{y = m x \\pm \\sqrt{a^2 m^2 + b^2}}$$</li>\n</ol>\n</p>\n\n<h3>2. The Director Circle of the Ellipse</h3>\n<p>\nLet $P(h, k)$ be the point of intersection of two mutually perpendicular tangents to the ellipse.\nThe slope form of a tangent passing through $(h, k)$ is:\n$$k - mh = \\pm \\sqrt{a^2 m^2 + b^2} \\iff (k - mh)^2 = a^2 m^2 + b^2$$\nExpanding and grouping as a quadratic in the slope $m$:\n$$(h^2 - a^2)m^2 - 2hk m + (k^2 - b^2) = 0$$\nIf the two tangents are perpendicular, the product of their slopes must be $-1$:\n$$m_1 m_2 = \\frac{k^2 - b^2}{h^2 - a^2} = -1 \\iff k^2 - b^2 = -(h^2 - a^2) \\iff h^2 + k^2 = a^2 + b^2$$\nReplacing $(h, k)$ with current coordinates $(x, y)$:\n$$\\mathbf{x^2 + y^2 = a^2 + b^2}$$\n<strong>The Director Circle Theorem:</strong> The locus of the point of intersection of two mutually perpendicular tangents to an ellipse is a concentric circle of radius $R = \\sqrt{a^2 + b^2}$, termed the <em>director circle</em>!\n</p>\n\n<h3>3. Equation of the Normal</h3>\n<p>\nThe normal line at $P(x_1, y_1)$ is perpendicular to the tangent:\n$$\\mathbf{\\frac{a^2 x}{x_1} - \\frac{b^2 y}{y_1} = a^2 - b^2}$$\nIn parametric coordinates $P(\\phi)$:\n$$\\mathbf{a x \\sec \\phi - b y \\csc \\phi = a^2 - b^2}$$\n</p>\n"
        },
        {
          "id": "u6-sec4",
          "title": "Conjugate Diameters & Apollonius' Theorems",
          "content": "\n<h3>1. Definition of Conjugate Diameters</h3>\n<p>\nA diameter of an ellipse is a chord passing through its center $C(0, 0)$.\nTwo diameters $y = m_1 x$ and $y = m_2 x$ are said to be <strong>conjugate diameters</strong> if each bisects all chords parallel to the other.\nThe algebraic condition for conjugacy is:\n$$\\mathbf{m_1 m_2 = -\\frac{b^2}{a^2}}$$\nIn parametric terms, if $CP$ is a semi-diameter with endpoint $P(\\phi) = (a\\cos\\phi, b\\sin\\phi)$, its conjugate semi-diameter $CD$ has endpoint $D$ whose eccentric angle differs by $\\pi/2$:\n$$\\phi_D = \\phi + \\frac{\\pi}{2} \\implies \\mathbf{D = (-a \\sin \\phi, \\; b \\cos \\phi)}$$\n</p>\n\n<h3>2. Apollonius' First Theorem (Sum of Squared Semi-Diameters)</h3>\n<p>\nThe sum of the squares of any two conjugate semi-diameters is constant and equal to the sum of the squares of the semi-axes:\n$$CP^2 = a^2 \\cos^2 \\phi + b^2 \\sin^2 \\phi$$\n$$CD^2 = a^2 \\sin^2 \\phi + b^2 \\cos^2 \\phi$$\nAdding the two equations:\n$$CP^2 + CD^2 = a^2(\\cos^2 \\phi + \\sin^2 \\phi) + b^2(\\sin^2 \\phi + \\cos^2 \\phi) = \\mathbf{a^2 + b^2 = \\text{Constant!}}$$\n</p>\n\n<h3>3. Apollonius' Second Theorem (Area of Circumscribing Parallelogram)</h3>\n<p>\nThe area of the parallelogram formed by the tangents drawn at the extremities of any pair of conjugate diameters is constant and equal to the area of the rectangle formed by the principal axes:\n$$\\mathcal{A} = 4 \\left| x_P y_D - x_D y_P \\right| = 4 |(a\\cos\\phi)(b\\cos\\phi) - (-a\\sin\\phi)(b\\sin\\phi)| = 4 a b(\\cos^2 \\phi + \\sin^2 \\phi) = \\mathbf{4 a b}$$\n</p>\n"
        },
        {
          "id": "u6-sec5",
          "title": "Optical Reflection Property & Product of Focal Perpendiculars",
          "content": "\n<h3>1. The Optical/Acoustic Reflection Property</h3>\n<p>\nLet $P(x_1, y_1)$ be any point on the ellipse with foci $S(ae, 0)$ and $S'(-ae, 0)$.\nLet the normal at $P$ meet the major axis at $G$. By the properties of the normal:\n$$CG = e^2 x_1 \\implies SG = ae - e^2 x_1 = e(a - ex_1) = e \\cdot SP, \\quad S'G = ae + e^2 x_1 = e(a + ex_1) = e \\cdot S'P$$\nTherefore:\n$$\\frac{SG}{S'G} = \\frac{SP}{S'P}$$\nBy the angle bisector theorem, the normal $PG$ is the internal bisector of the focal angle $\\angle SPS'$!\nConsequently, the tangent at $P$ is the external bisector of $\\angle SPS'$.\n$$\\mathbf{\\angle S P T = \\angle S' P T}$$\n<strong>Physical Consequence:</strong> Any light ray or acoustic wave emitted from one focus $S$ reflects off the elliptical boundary directly to the other focus $S'$! This is the physical mechanism of whispering galleries (such as St. Paul's Cathedral in London and the National Statuary Hall in Washington, D.C.).\n</p>\n\n<h3>2. Product of Perpendiculars from Foci onto Any Tangent</h3>\n<p>\nLet $p_1$ and $p_2$ be the lengths of perpendiculars dropped from the two foci $S(ae, 0)$ and $S'(-ae, 0)$ onto any tangent line $y - mx - \\sqrt{a^2 m^2 + b^2} = 0$:\n$$p_1 = \\frac{|-mae - \\sqrt{a^2 m^2 + b^2}|}{\\sqrt{1 + m^2}}, \\qquad p_2 = \\frac{|mae - \\sqrt{a^2 m^2 + b^2}|}{\\sqrt{1 + m^2}}$$\nMultiplying the two perpendiculars:\n$$p_1 p_2 = \\frac{|(a^2 m^2 + b^2) - m^2 a^2 e^2|}{1 + m^2} = \\frac{|a^2 m^2(1 - e^2) + b^2|}{1 + m^2} = \\frac{|a^2 m^2 (b^2/a^2) + b^2|}{1 + m^2} = \\frac{b^2(m^2 + 1)}{1 + m^2} = \\mathbf{b^2}$$\n<strong>Theorem:</strong> The product of the perpendiculars from the foci onto any tangent to an ellipse is constant and equal to the square of the semi-minor axis $b^2$!\n</p>\n",
          "simulation": "geom2d-ellipse-conjugate-sim",
          "simulations": [
            "geom2d-ellipse-conjugate-sim"
          ]
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "Standard Ellipse Geometric Elements and Parametric Tangent",
          "statement": "For the ellipse $9x^2 + 16y^2 = 144$: (a) Find the lengths of the major and minor axes, eccentricity $e$, and coordinates of the foci and directrices. (b) Find the equation of the tangent line at the point where the eccentric angle is $\\phi = \\pi/4$.",
          "steps": [
            {
              "step": "Step 1: Reduce to Canonical Form",
              "math": "\\frac{9x^2}{144} + \\frac{16y^2}{144} = 1 \\implies \\frac{x^2}{16} + \\frac{y^2}{9} = 1 \\implies a^2 = 16, \\; b^2 = 9 \\implies a = 4, \\; b = 3",
              "explanation": "Major axis length is $2a = 8$; minor axis length is $2b = 6$."
            },
            {
              "step": "Step 2: Compute Eccentricity, Foci and Directrices",
              "math": "e = \\sqrt{1 - \\frac{b^2}{a^2}} = \\sqrt{1 - \\frac{9}{16}} = \\frac{\\sqrt{7}}{4} \\\\ \\text{Foci: } (\\pm ae, 0) = \\left(\\pm 4\\cdot\\frac{\\sqrt{7}}{4}, 0\\right) = (\\pm\\sqrt{7}, 0) \\\\ \\text{Directrices: } x = \\pm\\frac{a}{e} = \\pm\\frac{4}{\\sqrt{7}/4} = \\pm\\frac{16}{\\sqrt{7}}",
              "explanation": "Focal distance is $ae = \\sqrt{7}$ and directrix distance is $a/e = 16/\\sqrt{7}$."
            },
            {
              "step": "Step 3: Tangent Equation at $\\phi = \\pi/4$",
              "math": "\\frac{x\\cos\\phi}{a} + \\frac{y\\sin\\phi}{b} = 1 \\implies \\frac{x\\cos(\\pi/4)}{4} + \\frac{y\\sin(\\pi/4)}{3} = 1 \\implies \\frac{x}{4\\sqrt{2}} + \\frac{y}{3\\sqrt{2}} = 1 \\\\ 3x + 4y = 12\\sqrt{2}",
              "explanation": "Multiplying by $12\\sqrt{2}$ yields the linear tangent equation $3x + 4y - 12\\sqrt{2} = 0$."
            }
          ],
          "answer": "a = 4, \\; b = 3; \\quad e = \\frac{\\sqrt{7}}{4}; \\quad \\text{Foci: } (\\pm\\sqrt{7}, 0); \\quad \\text{Directrices: } x = \\pm\\frac{16}{\\sqrt{7}}; \\quad \\text{Tangent: } 3x + 4y = 12\\sqrt{2}"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "Director Circle and Mutual Perpendicular Tangents",
          "statement": "Given the ellipse $\\frac{x^2}{25} + \\frac{y^2}{9} = 1$: (a) Write the equation of its director circle. (b) Find the equations of the tangents drawn from the point $P(0, \\sqrt{34})$. (c) Verify that the two tangents are mutually perpendicular.",
          "steps": [
            {
              "step": "Step 1: Equation of Director Circle",
              "math": "x^2 + y^2 = a^2 + b^2 = 25 + 9 = 34 \\implies x^2 + y^2 = 34",
              "explanation": "Notice that the point $P(0, \\sqrt{34})$ satisfies $0^2 + (\\sqrt{34})^2 = 34$, so $P$ lies strictly on the director circle!"
            },
            {
              "step": "Step 2: Slope Form of Tangents through $P(0, \\sqrt{34})$",
              "math": "y = mx \\pm \\sqrt{a^2 m^2 + b^2} = mx \\pm \\sqrt{25m^2 + 9} \\\\ \\sqrt{34} = m(0) \\pm \\sqrt{25m^2 + 9} \\implies 34 = 25m^2 + 9 \\implies 25m^2 = 25 \\implies m^2 = 1 \\implies m = \\pm 1",
              "explanation": "The slopes of the two tangents are $m_1 = 1$ and $m_2 = -1$."
            },
            {
              "step": "Step 3: Tangent Equations and Orthogonality",
              "math": "\\text{Tangent 1 } (m = 1): \\quad y = x + \\sqrt{34} \\implies x - y + \\sqrt{34} = 0 \\\\ \\text{Tangent 2 } (m = -1): \\quad y = -x + \\sqrt{34} \\implies x + y - \\sqrt{34} = 0 \\\\ m_1 \\cdot m_2 = (1)(-1) = -1 \\implies \\text{Strictly Perpendicular!}",
              "explanation": "The product of the slopes is $-1$, verifying the Director Circle Theorem."
            }
          ],
          "answer": "\\text{Director Circle: } x^2 + y^2 = 34; \\quad \\text{Tangents: } y = x + \\sqrt{34} \\text{ and } y = -x + \\sqrt{34}; \\quad m_1 m_2 = -1 \\implies \\text{Orthogonal}"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "Rigorous Proof of Apollonius' Conjugate Diameter Theorems",
          "statement": "Let $CP$ and $CD$ be a pair of conjugate semi-diameters of the ellipse $\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1$. Prove analytically: (a) $CP^2 + CD^2 = a^2 + b^2$ (Apollonius' First Theorem). (b) The area of the parallelogram formed by the tangents at the extremities of the conjugate diameters is constant and equal to $4ab$ (Apollonius' Second Theorem).",
          "steps": [
            {
              "step": "Step 1: Express Endpoints in Parametric Form",
              "math": "\\text{Let } P = (a\\cos\\phi, b\\sin\\phi). \\quad \\text{Then } D \\text{ has eccentric angle } \\phi + \\pi/2: \\\\ D = (a\\cos(\\phi + \\pi/2), b\\sin(\\phi + \\pi/2)) = (-a\\sin\\phi, b\\cos\\phi)",
              "explanation": "This establishes the exact coordinates of conjugate extremities."
            },
            {
              "step": "Step 2: Proof of Apollonius' First Theorem",
              "math": "CP^2 = (a\\cos\\phi)^2 + (b\\sin\\phi)^2 = a^2\\cos^2\\phi + b^2\\sin^2\\phi \\\\ CD^2 = (-a\\sin\\phi)^2 + (b\\cos\\phi)^2 = a^2\\sin^2\\phi + b^2\\cos^2\\phi \\\\ CP^2 + CD^2 = a^2(\\cos^2\\phi + \\sin^2\\phi) + b^2(\\sin^2\\phi + \\cos^2\\phi) = a^2(1) + b^2(1) = a^2 + b^2",
              "explanation": "Since $\\phi$ cancels completely, $CP^2 + CD^2 = a^2 + b^2$ holds for every conjugate pair."
            },
            {
              "step": "Step 3: Proof of Apollonius' Second Theorem",
              "math": "\\text{Area of } \\triangle CPD = \\frac{1}{2}|x_P y_D - x_D y_P| = \\frac{1}{2}|(a\\cos\\phi)(b\\cos\\phi) - (-a\\sin\\phi)(b\\sin\\phi)| \\\\ = \\frac{1}{2}|ab\\cos^2\\phi + ab\\sin^2\\phi| = \\frac{1}{2}ab(\\cos^2\\phi + \\sin^2\\phi) = \\frac{1}{2}ab \\\\ \\text{Total parallelogram area} = 8 \\times \\operatorname{Area}(\\triangle CPD) \\text{ (or } 4 \\times 2\\triangle) = 4ab",
              "explanation": "The circumscribing parallelogram has constant area $4ab$ everywhere."
            }
          ],
          "answer": "CP^2 + CD^2 = a^2 + b^2 \\text{ (Apollonius' 1st)}; \\quad \\text{Parallelogram Area} = 4ab \\text{ (Apollonius' 2nd)}"
        }
      ],
      "simulations": [
        "geom2d-ellipse-conjugate-sim"
      ],
      "id": "unit6",
      "unitId": "unit6-geom2d",
      "leadSummary": "Exhaustive treatment of the ellipse: focus-directrix definition e < 1 and canonical derivation x^2/a^2 + y^2/b^2 = 1; sum of focal distances SP + S'P = 2a and the gardener's construction; auxiliary circle x^2 + y^2 = a^2 and eccentric angle phi; area pi*a*b; tangents in point, slope, and parametric forms; director circle x^2 + y^2 = a^2 + b^2 and orthogonal tangent loci; normal equation a^2 x/x_1 - b^2 y/y_1 = a^2 - b^2; conjugate diameters and Apollonius' first (CP^2 + CD^2 = a^2 + b^2) and second (area = 4ab) theorems; optical and acoustic reflection properties; and the product of focal perpendiculars to any tangent p_1 p_2 = b^2."
    },
    {
      "unitNumber": 7,
      "number": 7,
      "title": "In-Depth Study of the Hyperbola & Rectangular Hyperbola",
      "description": "Exhaustive treatment of the hyperbola: focus-directrix definition e > 1 and canonical derivation x^2/a^2 - y^2/b^2 = 1; focal distance difference |S'P - SP| = 2a; asymptotes y = +/- (b/a)x; conjugate hyperbola y^2/b^2 - x^2/a^2 = 1 and the eccentricity relation 1/e_1^2 + 1/e_2^2 = 1; tangents in point, slope, and parametric forms; director circle x^2 + y^2 = a^2 - b^2; rectangular (equilateral) hyperbola x^2 - y^2 = a^2 with e = sqrt(2); rotation to asymptotic canonical form xy = c^2; and the constant triangle area 2c^2 and midpoint bisection properties.",
      "sections": [
        {
          "id": "u7-sec1",
          "title": "The Hyperbola: Canonical Equation, Eccentricity & Metric Relations",
          "content": "\n<h3>1. The Focus-Directrix Locus Definition ($e > 1$)</h3>\n<p>\nA <strong>hyperbola</strong> is the planar locus of a point $P(x, y)$ that moves such that the ratio of its distance from a fixed focus $S(ae, 0)$ to its distance from a fixed directrix line $D: x = a/e$ is a constant eccentricity $e > 1$:\n$$\\frac{SP}{PM} = e \\iff SP = e \\cdot PM$$\nUsing the Euclidean distance formula:\n$$(x - ae)^2 + y^2 = e^2 \\left(x - \\frac{a}{e}\\right)^2 = (ex - a)^2$$\nExpanding and simplifying:\n$$(e^2 - 1)x^2 - y^2 = a^2(e^2 - 1) \\iff \\frac{x^2}{a^2} - \\frac{y^2}{a^2(e^2 - 1)} = 1$$\nDefining the conjugate semi-axis $b > 0$ by the fundamental relation:\n$$\\mathbf{b^2 \\equiv a^2(e^2 - 1) \\iff e = \\sqrt{1 + \\frac{b^2}{a^2}} > 1}$$\nyields the canonical equation of the hyperbola:\n$$\\mathbf{\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1}$$\n</p>\n\n<h3>2. The Difference of Focal Radii</h3>\n<p>\nLike the ellipse, the hyperbola possesses two foci $S(ae, 0)$ and $S'(-ae, 0)$.\nThe focal distances to any point $P(x, y)$ on the right branch are $SP = ex - a$ and $S'P = ex + a$.\nTheir difference is:\n$$S'P - SP = (ex + a) - (ex - a) = \\mathbf{2a = \\text{Constant Everywhere!}}$$\n<strong>The Focal Difference Theorem:</strong> A hyperbola is the locus of all points whose difference of distances from two fixed foci $S$ and $S'$ is constant and equal to the transverse axis: $|S'P - SP| = 2a$.\n</p>\n\n<h3>3. Canonical Geometric Elements</h3>\n<p>\n<ul>\n  <li><strong>Center ($C$):</strong> $(0, 0)$.</li>\n  <li><strong>Transverse Axis:</strong> Segment along the $x$-axis connecting vertices $A(a, 0)$ and $A'(-a, 0)$, length $2a$.</li>\n  <li><strong>Conjugate Axis:</strong> Segment along the $y$-axis of length $2b$.</li>\n  <li><strong>Foci:</strong> $S(ae, 0)$ and $S'(-ae, 0)$, distance $SS' = 2ae$.</li>\n  <li><strong>Directrices:</strong> $x = \\pm a/e$, distance $2a/e$.</li>\n  <li><strong>Latus Rectum:</strong> Length $2b^2/a$.</li>\n</ul>\n</p>\n"
        },
        {
          "id": "u7-sec2",
          "title": "Asymptotes & The Conjugate Hyperbola",
          "content": "\n<h3>1. Asymptotes of the Hyperbola</h3>\n<p>\nAn <strong>asymptote</strong> to a curve is a straight line such that the perpendicular distance from a point on the curve to the line approaches zero as the point recedes to infinity.\nSolving the canonical hyperbola for $y$:\n$$y = \\pm \\frac{b}{a}\\sqrt{x^2 - a^2} = \\pm \\frac{b}{a}x \\sqrt{1 - \\frac{a^2}{x^2}} = \\pm \\frac{b}{a}x \\left(1 - \\frac{a^2}{2x^2} - \\dots\\right) \\to \\pm \\frac{b}{a}x \\quad \\text{as } |x| \\to \\infty$$\nThus, the hyperbola possesses two real asymptotes passing through the center:\n$$\\mathbf{y = \\frac{b}{a}x \\quad \\text{and} \\quad y = -\\frac{b}{a}x \\iff \\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 0}$$\nThe angle between the asymptotes is $2\\theta$, where $\\tan \\theta = b/a \\implies 2\\theta = 2\\arctan(b/a)$.\n</p>\n\n<h3>2. The Conjugate Hyperbola</h3>\n<p>\nThe hyperbola whose transverse and conjugate axes are respectively the conjugate and transverse axes of the given hyperbola is termed the <strong>conjugate hyperbola</strong>:\n$$\\mathbf{\\frac{y^2}{b^2} - \\frac{x^2}{a^2} = 1 \\iff -\\frac{x^2}{a^2} + \\frac{y^2}{b^2} = 1}$$\n<strong>Remarkable Properties:</strong>\n<ul>\n  <li>The hyperbola and its conjugate hyperbola share the <em>exact same pair of asymptotes</em>: $\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 0$.</li>\n  <li>If $e_1$ is the eccentricity of the original hyperbola and $e_2$ is the eccentricity of the conjugate hyperbola:\n  $$e_1^2 = 1 + \\frac{b^2}{a^2} = \\frac{a^2 + b^2}{a^2} \\implies \\frac{1}{e_1^2} = \\frac{a^2}{a^2 + b^2}$$\n  $$e_2^2 = 1 + \\frac{a^2}{b^2} = \\frac{a^2 + b^2}{b^2} \\implies \\frac{1}{e_2^2} = \\frac{b^2}{a^2 + b^2}$$\n  Adding these reciprocals establishes the celebrated theorem:\n  $$\\mathbf{\\frac{1}{e_1^2} + \\frac{1}{e_2^2} = 1}$$</li>\n</ul>\n</p>\n"
        },
        {
          "id": "u7-sec3",
          "title": "Tangents, Normals & The Director Circle",
          "content": "\n<h3>1. Equations of the Tangent</h3>\n<p>\n<ol>\n  <li><strong>Point Form:</strong> Tangent at $P(x_1, y_1)$ on $\\frac{x^2}{a^2} - \\frac{y^2}{b^2} = 1$:\n  $$\\mathbf{\\frac{x x_1}{a^2} - \\frac{y y_1}{b^2} = 1}$$</li>\n  <li><strong>Parametric Form:</strong> Using $x = a\\sec\\theta, y = b\\tan\\theta$:\n  $$\\mathbf{\\frac{x \\sec \\theta}{a} - \\frac{y \\tan \\theta}{b} = 1}$$</li>\n  <li><strong>Slope Form:</strong> A line $y = mx + c$ is tangent if and only if $c^2 = a^2 m^2 - b^2$:\n  $$\\mathbf{y = m x \\pm \\sqrt{a^2 m^2 - b^2} \\quad (|m| > b/a)}$$</li>\n</ol>\n</p>\n\n<h3>2. The Director Circle of the Hyperbola</h3>\n<p>\nRepeating the orthogonal tangent locus derivation for the hyperbola yields:\n$$\\mathbf{x^2 + y^2 = a^2 - b^2}$$\n<ul>\n  <li><strong>Real Circle ($a > b$):</strong> A real concentric circle of radius $\\sqrt{a^2 - b^2}$.</li>\n  <li><strong>Point Circle ($a = b$):</strong> Concentrates to the origin $(0, 0)$.</li>\n  <li><strong>Virtual / Imaginary ($a < b$):</strong> No pair of real mutually perpendicular tangents can be drawn to the hyperbola!</li>\n</ul>\n</p>\n"
        },
        {
          "id": "u7-sec4",
          "title": "The Rectangular (Equilateral) Hyperbola & xy = c^2",
          "content": "\n<h3>1. The Equilateral Hyperbola ($a = b$)</h3>\n<p>\nWhen the semi-axes are equal ($a = b$), the hyperbola is termed <strong>rectangular</strong> or <strong>equilateral</strong>:\n$$x^2 - y^2 = a^2$$\nKey characteristics:\n<ul>\n  <li>Eccentricity: $e = \\sqrt{1 + a^2/a^2} = \\mathbf{\\sqrt{2}}$. Every rectangular hyperbola has eccentricity exactly $\\sqrt{2}$!</li>\n  <li>Asymptotes: $y = \\pm x \\iff x^2 - y^2 = 0$. The asymptotes intersect at right angles ($\\pi/2 = 90^\\circ$).</li>\n</ul>\n</p>\n\n<h3>2. Rotation of Axes to Asymptotic Coordinates ($xy = c^2$)</h3>\n<p>\nBecause the asymptotes of a rectangular hyperbola are mutually perpendicular, they can be chosen as the coordinate axes!\nRotating the axes clockwise through $45^\\circ$ ($\\theta = -\\pi/4$):\n$$x = X \\cos(-\\pi/4) - Y \\sin(-\\pi/4) = \\frac{X + Y}{\\sqrt{2}}$$\n$$y = X \\sin(-\\pi/4) + Y \\cos(-\\pi/4) = \\frac{-X + Y}{\\sqrt{2}}$$\nSubstituting into $x^2 - y^2 = a^2$:\n$$\\left(\\frac{X + Y}{\\sqrt{2}}\\right)^2 - \\left(\\frac{Y - X}{\\sqrt{2}}\\right)^2 = a^2 \\implies \\frac{(X+Y)^2 - (Y-X)^2}{2} = a^2$$\n$$\\frac{4XY}{2} = a^2 \\implies 2XY = a^2 \\iff \\mathbf{XY = \\frac{a^2}{2} \\equiv c^2}$$\nThis is the widely used standard canonical form of the rectangular hyperbola:\n$$\\mathbf{xy = c^2 \\quad \\left(c = \\frac{a}{\\sqrt{2}}\\right)}$$\n</p>\n"
        },
        {
          "id": "u7-sec5",
          "title": "Geometric Properties of the Asymptotic Hyperbola xy = c^2",
          "content": "\n<h3>1. Parametric Form & Tangents</h3>\n<p>\nSetting $x = ct$, the curve $xy = c^2$ gives $y = c/t$. The standard parametrization is:\n$$\\mathbf{P(t) = \\left(c t, \\; \\frac{c}{t}\\right) \\quad (t \\ne 0)}$$\nDifferentiating implicitly: $y + x \\frac{dy}{dx} = 0 \\implies \\frac{dy}{dx} = -\\frac{y}{x} = -\\frac{c/t}{ct} = -\\frac{1}{t^2}$.\nThe equation of the tangent at $P(t)$ is:\n$$y - \\frac{c}{t} = -\\frac{1}{t^2}(x - ct) \\iff t^2 y - ct = -x + ct \\iff \\mathbf{x + t^2 y = 2ct \\iff \\frac{x}{t} + yt = 2c}$$\n</p>\n\n<h3>2. The Constant Area Tangent Triangle Theorem</h3>\n<p>\nThe tangent at $P(t)$ intersects the asymptotes ($x$-axis and $y$-axis) at:\n$$A: y = 0 \\implies x_A = 2ct \\implies A(2ct, 0)$$\n$$B: x = 0 \\implies y_B = \\frac{2c}{t} \\implies B\\left(0, \\frac{2c}{t}\\right)$$\nNotice:\n<ol>\n  <li><strong>Midpoint Property:</strong> The midpoint of the tangent segment $AB$ is $\\left(\\frac{2ct + 0}{2}, \\frac{0 + 2c/t}{2}\\right) = (ct, c/t) = P$.\n  <strong>Theorem:</strong> The point of contact $P$ bisects the segment of the tangent intercepted between the asymptotes!</li>\n  <li><strong>Constant Triangle Area:</strong> The area of the right triangle $\\triangle OAB$ formed by the tangent and the two coordinate asymptotes is:\n  $$\\operatorname{Area}(\\triangle OAB) = \\frac{1}{2} OA \\cdot OB = \\frac{1}{2}(2ct)\\left(\\frac{2c}{t}\\right) = \\mathbf{2c^2 = \\text{Constant Everywhere!}}$$\n  The area is completely independent of the parameter $t$!</li>\n</ol>\n</p>\n",
          "simulation": "geom2d-hyperbola-asymptotes-sim",
          "simulations": [
            "geom2d-hyperbola-asymptotes-sim"
          ]
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "Standard Hyperbola Elements and Asymptote Equations",
          "statement": "For the hyperbola $9x^2 - 16y^2 = 144$: (a) Find the lengths of the transverse and conjugate axes, eccentricity $e$, coordinates of the foci, and directrices. (b) Find the equations of the two asymptotes and the angle between them.",
          "steps": [
            {
              "step": "Step 1: Reduce to Canonical Form",
              "math": "\\frac{9x^2}{144} - \\frac{16y^2}{144} = 1 \\implies \\frac{x^2}{16} - \\frac{y^2}{9} = 1 \\implies a^2 = 16, \\; b^2 = 9 \\implies a = 4, \\; b = 3",
              "explanation": "Transverse axis is $2a = 8$; conjugate axis is $2b = 6$."
            },
            {
              "step": "Step 2: Eccentricity, Foci and Directrices",
              "math": "e = \\sqrt{1 + \\frac{b^2}{a^2}} = \\sqrt{1 + \\frac{9}{16}} = \\frac{5}{4} = 1.25 \\\\ \\text{Foci: } (\\pm ae, 0) = \\left(\\pm 4\\cdot\\frac{5}{4}, 0\\right) = (\\pm 5, 0) \\\\ \\text{Directrices: } x = \\pm\\frac{a}{e} = \\pm\\frac{4}{5/4} = \\pm\\frac{16}{5} = \\pm 3.2",
              "explanation": "Eccentricity is $1.25$, foci are at $(\\pm 5, 0)$, directrices are $x = \\pm 3.2$."
            },
            {
              "step": "Step 3: Asymptotes and Included Angle",
              "math": "y = \\pm\\frac{b}{a}x = \\pm\\frac{3}{4}x \\iff 3x - 4y = 0 \\quad \\text{and} \\quad 3x + 4y = 0 \\\\ \\tan\\theta = \\frac{3}{4} \\implies \\text{Angle between asymptotes } 2\\theta = 2\\arctan\\left(\\frac{3}{4}\\right) \\approx 73.74^\\circ",
              "explanation": "The asymptotes are $y = \\pm \\frac{3}{4}x$."
            }
          ],
          "answer": "a = 4, \\; b = 3; \\quad e = 1.25; \\quad \\text{Foci: } (\\pm 5, 0); \\quad \\text{Directrices: } x = \\pm 3.2; \\quad \\text{Asymptotes: } y = \\pm\\frac{3}{4}x"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "Conjugate Hyperbolas and Eccentricity Reciprocal Theorem",
          "statement": "A hyperbola $H_1$ has equation $16x^2 - 9y^2 = 144$. (a) Write the equation of its conjugate hyperbola $H_2$. (b) Find the eccentricities $e_1$ and $e_2$ of both hyperbolas. (c) Rigorously verify that $\\frac{1}{e_1^2} + \\frac{1}{e_2^2} = 1$.",
          "steps": [
            {
              "step": "Step 1: Canonical Form of $H_1$ and $H_2$",
              "math": "H_1: \\frac{x^2}{9} - \\frac{y^2}{16} = 1 \\implies a^2 = 9, \\; b^2 = 16 \\\\ H_2 \\text{ (Conjugate)}: -\\frac{x^2}{9} + \\frac{y^2}{16} = 1 \\iff \\frac{y^2}{16} - \\frac{x^2}{9} = 1 \\implies 9y^2 - 16x^2 = 144",
              "explanation": "The conjugate hyperbola is obtained by switching signs of terms."
            },
            {
              "step": "Step 2: Compute Eccentricities $e_1$ and $e_2$",
              "math": "e_1 = \\sqrt{1 + \\frac{b^2}{a^2}} = \\sqrt{1 + \\frac{16}{9}} = \\sqrt{\\frac{25}{9}} = \\frac{5}{3} \\\\ e_2 = \\sqrt{1 + \\frac{a^2}{b^2}} = \\sqrt{1 + \\frac{9}{16}} = \\sqrt{\\frac{25}{16}} = \\frac{5}{4}",
              "explanation": "Thus $e_1 = 5/3$ and $e_2 = 5/4$."
            },
            {
              "step": "Step 3: Verify the Reciprocal Identity",
              "math": "\\frac{1}{e_1^2} + \\frac{1}{e_2^2} = \\frac{1}{(5/3)^2} + \\frac{1}{(5/4)^2} = \\frac{9}{25} + \\frac{16}{25} = \\frac{9 + 16}{25} = \\frac{25}{25} = 1",
              "explanation": "The sum of reciprocals of squared eccentricities equals exactly 1."
            }
          ],
          "answer": "H_2: \\frac{y^2}{16} - \\frac{x^2}{9} = 1; \\quad e_1 = \\frac{5}{3}, \\; e_2 = \\frac{5}{4}; \\quad \\frac{1}{e_1^2} + \\frac{1}{e_2^2} = \\frac{9}{25} + \\frac{16}{25} = 1"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "Rectangular Hyperbola $xy = c^2$: Concurrency of Circle Intersections",
          "statement": "A circle $x^2 + y^2 + 2gx + 2fy + k = 0$ intersects the rectangular hyperbola $xy = c^2$ in four points $P_i(x_i, y_i)$ with parameters $t_i$ ($i = 1, 2, 3, 4$). (a) Derive the quartic equation in $t$. (b) Prove that $t_1 t_2 t_3 t_4 = 1$. (c) Prove that the product of the four abscissae is $c^4$, the product of the four ordinates is $c^4$, and the center of mean position of the four points is $(-g/2, -f/2)$.",
          "steps": [
            {
              "step": "Step 1: Substitute Parametric Coordinates into Circle",
              "math": "x = ct, \\quad y = \\frac{c}{t} \\\\ (ct)^2 + \\left(\\frac{c}{t}\\right)^2 + 2g(ct) + 2f\\left(\\frac{c}{t}\\right) + k = 0 \\\\ c^2 t^2 + \\frac{c^2}{t^2} + 2gct + \\frac{2fc}{t} + k = 0",
              "explanation": "Multiply by $t^2$ to clear the denominator."
            },
            {
              "step": "Step 2: Form the Quartic Polynomial in $t$",
              "math": "c^2 t^4 + 2gc t^3 + k t^2 + 2fc t + c^2 = 0",
              "explanation": "Dividing by $c^2$: $t^4 + \\frac{2g}{c}t^3 + \\frac{k}{c^2}t^2 + \\frac{2f}{c}t + 1 = 0$."
            },
            {
              "step": "Step 3: Apply Vi\u00e8te's Formulas",
              "math": "\\sum t_i = t_1 + t_2 + t_3 + t_4 = -\\frac{2g}{c} \\\\ \\sum t_i t_j t_k = -\\frac{2f}{c} \\\\ t_1 t_2 t_3 t_4 = \\frac{c^2}{c^2} = 1",
              "explanation": "The product of the parameters is identically $t_1 t_2 t_3 t_4 = 1$."
            },
            {
              "step": "Step 4: Prove Coordinate Products and Centroid",
              "math": "x_1 x_2 x_3 x_4 = (ct_1)(ct_2)(ct_3)(ct_4) = c^4(t_1 t_2 t_3 t_4) = c^4(1) = c^4 \\\\ y_1 y_2 y_3 y_4 = \\left(\\frac{c}{t_1}\\right)\\left(\\frac{c}{t_2}\\right)\\left(\\frac{c}{t_3}\\right)\\left(\\frac{c}{t_4}\\right) = \\frac{c^4}{t_1 t_2 t_3 t_4} = c^4 \\\\ \\bar{x} = \\frac{\\sum x_i}{4} = \\frac{c \\sum t_i}{4} = \\frac{c(-2g/c)}{4} = -\\frac{g}{2}, \\quad \\bar{y} = \\frac{\\sum y_i}{4} = \\frac{c \\sum(1/t_i)}{4} = -\\frac{f}{2}",
              "explanation": "The centroid of the four intersection points is $(-g/2, -f/2)$, which is the exact midpoint of the line joining the origin to the circle's center $(-g, -f)$."
            }
          ],
          "answer": "t_1 t_2 t_3 t_4 = 1; \\quad \\prod x_i = c^4, \\; \\prod y_i = c^4; \\quad \\text{Centroid: } \\left(-\\frac{g}{2}, -\\frac{f}{2}\\right)"
        }
      ],
      "simulations": [
        "geom2d-hyperbola-asymptotes-sim"
      ],
      "id": "unit7",
      "unitId": "unit7-geom2d",
      "leadSummary": "Exhaustive treatment of the hyperbola: focus-directrix definition e > 1 and canonical derivation x^2/a^2 - y^2/b^2 = 1; focal distance difference |S'P - SP| = 2a; asymptotes y = +/- (b/a)x; conjugate hyperbola y^2/b^2 - x^2/a^2 = 1 and the eccentricity relation 1/e_1^2 + 1/e_2^2 = 1; tangents in point, slope, and parametric forms; director circle x^2 + y^2 = a^2 - b^2; rectangular (equilateral) hyperbola x^2 - y^2 = a^2 with e = sqrt(2); rotation to asymptotic canonical form xy = c^2; and the constant triangle area 2c^2 and midpoint bisection properties."
    },
    {
      "unitNumber": 8,
      "number": 8,
      "title": "Polar Equations of Conics & Celestial Orbital Geometry",
      "description": "Unified universal polar formulation of conic sections: focus-at-pole derivation l/r = 1 + e cos theta; geometric classification and morphing across eccentricity e (circle e=0, ellipse 0<e<1, parabola e=1, hyperbola e>1); periapsis and apoapsis relations; chords, tangents l/r = e cos theta + cos(theta - alpha), and normals in polar coordinates; harmonic mean property of focal chord segments; confocal conics and orthogonal intersection theorems; and celestial orbital mechanics via Binet's equation, orbital energy, vis-viva equation, and hyperbolic escape flybys.",
      "sections": [
        {
          "id": "u8-sec1",
          "title": "Universal Polar Equation of a Conic with Focus at the Pole",
          "content": "\n<h3>1. Unified Focus-Directrix Derivation</h3>\n<p>\nA remarkable triumph of analytic geometry is that all non-degenerate conic sections (circles, ellipses, parabolas, and hyperbolas) can be described by a <strong>single unified equation</strong> in polar coordinates when one focus is chosen as the pole $O$.\n</p>\n<p>\nLet the pole $O$ be the focus of the conic, and let the polar axis be chosen along the axis of symmetry, perpendicular to directrix $D$.\nLet the directrix $D$ be located at a distance $d$ to the left of the pole, so its Cartesian equation is $x = -d$, or in polar coordinates:\n$$r \\cos(\\pi - \\theta) = d \\iff -r \\cos \\theta = d \\iff r \\cos \\theta = -d$$\nFor any point $P(r, \\theta)$ on the conic, the distance to the focus is $SP = r$.\nThe perpendicular distance from $P$ to the directrix is:\n$$PM = d + r \\cos \\theta$$\nBy the universal conic definition $SP = e \\cdot PM$:\n$$r = e(d + r \\cos \\theta) = ed + er \\cos \\theta$$\n$$r(1 - e \\cos \\theta) = ed \\iff \\frac{ed}{r} = 1 - e \\cos \\theta$$\nDefining the <strong>semi-latus rectum</strong> $l \\equiv ed$ (the value of $r$ when $\\theta = \\pi/2$):\n$$\\mathbf{\\frac{l}{r} = 1 - e \\cos \\theta}$$\nIf the directrix is chosen to the right ($x = +d$), the equation becomes:\n$$\\mathbf{\\frac{l}{r} = 1 + e \\cos \\theta}$$\nIf the axis of the conic is tilted by an angle $\\alpha$ relative to the polar axis:\n$$\\mathbf{\\frac{l}{r} = 1 + e \\cos(\\theta - \\alpha)}$$\n</p>\n"
        },
        {
          "id": "u8-sec2",
          "title": "Unified Geometric Classification via Polar Eccentricity",
          "content": "\n<h3>1. Conic Morphing via Eccentricity $e$</h3>\n<p>\nIn the universal polar equation $\\frac{l}{r} = 1 + e \\cos \\theta$, the geometric nature of the curve is determined purely by the parameter $e$:\n<ul>\n  <li><strong>Circle ($e = 0$):</strong>\n  $$\\frac{l}{r} = 1 \\iff r = l$$\n  The radial distance is constant for all $\\theta$, representing a circle of radius $l$ centered at the pole.</li>\n  <li><strong>Ellipse ($0 < e < 1$):</strong>\n  Because $e < 1$, the denominator $1 + e \\cos \\theta > 0$ for all $\\theta \\in [0, 2\\pi)$. The curve is closed and bounded:\n  $$\\text{Periapsis (closest approach): } \\theta = 0 \\implies r_{\\min} = \\frac{l}{1 + e}$$\n  $$\\text{Apoapsis (furthest distance): } \\theta = \\pi \\implies r_{\\max} = \\frac{l}{1 - e}$$\n  The major axis length is $2a = r_{\\min} + r_{\\max} = \\frac{l}{1+e} + \\frac{l}{1-e} = \\frac{2l}{1 - e^2} \\implies l = a(1 - e^2)$.</li>\n  <li><strong>Parabola ($e = 1$):</strong>\n  $$\\frac{l}{r} = 1 + \\cos \\theta = 2 \\cos^2(\\theta/2) \\implies r = \\frac{l}{2}\\sec^2(\\theta/2)$$\n  As $\\theta \\to \\pm \\pi$, $r \\to \\infty$. The curve is open, escaping to infinity along a single direction.</li>\n  <li><strong>Hyperbola ($e > 1$):</strong>\n  The denominator $1 + e \\cos \\theta$ vanishes when $\\cos \\theta = -1/e$.\n  The directions $\\theta_0 = \\pm \\arccos(-1/e)$ define the <strong>directions of the asymptotes</strong>!\n  The curve splits into two branches extending to infinity.</li>\n</ul>\n</p>\n"
        },
        {
          "id": "u8-sec3",
          "title": "Tangents, Normals & Chords in Polar Coordinates",
          "content": "\n<h3>1. Equation of the Chord Joining Two Points</h3>\n<p>\nLet $P(\\alpha - \\beta)$ and $Q(\\alpha + \\beta)$ be two points on the conic $\\frac{l}{r} = 1 + e \\cos \\theta$.\nThe straight line passing through both points is:\n$$\\mathbf{\\frac{l}{r} = e \\cos \\theta + \\sec \\beta \\cos(\\theta - \\alpha)}$$\nNotice:\nWhen $\\theta = \\alpha - \\beta$: $\\frac{l}{r} = e\\cos(\\alpha - \\beta) + \\sec\\beta\\cos(-\\beta) = e\\cos(\\alpha - \\beta) + 1$, which satisfies the conic equation!\nWhen $\\theta = \\alpha + \\beta$: $\\frac{l}{r} = e\\cos(\\alpha + \\beta) + \\sec\\beta\\cos(\\beta) = e\\cos(\\alpha + \\beta) + 1$, which also satisfies the conic equation!\n</p>\n\n<h3>2. Equation of the Tangent Line</h3>\n<p>\nTaking the limit as $\\beta \\to 0$, the points $P$ and $Q$ coalesce at $\\theta = \\alpha$.\nSince $\\sec(0) = 1$, the equation of the tangent to the conic at $\\theta = \\alpha$ is:\n$$\\mathbf{\\frac{l}{r} = e \\cos \\theta + \\cos(\\theta - \\alpha)}$$\nThis is the universally famous polar tangent formula!\n</p>\n\n<h3>3. Perpendicular Focal Chords Theorem</h3>\n<p>\nLet $PSQ$ be a focal chord passing through the pole. The extremities are at $\\theta = \\alpha$ and $\\theta = \\alpha + \\pi$.\n$$SP = r_1 = \\frac{l}{1 + e \\cos \\alpha}, \\qquad SQ = r_2 = \\frac{l}{1 + e \\cos(\\alpha + \\pi)} = \\frac{l}{1 - e \\cos \\alpha}$$\nAdding their reciprocals:\n$$\\frac{1}{SP} + \\frac{1}{SQ} = \\frac{1 + e \\cos \\alpha}{l} + \\frac{1 - e \\cos \\alpha}{l} = \\mathbf{\\frac{2}{l} = \\text{Constant Everywhere!}}$$\n<strong>Theorem:</strong> The semi-latus rectum $l$ is the harmonic mean of the segments of any focal chord in any conic!\n</p>\n"
        },
        {
          "id": "u8-sec4",
          "title": "Confocal Conics & Orthogonal Intersections",
          "content": "\n<h3>1. Confocal Conics</h3>\n<p>\nA family of conics having the same foci is termed <strong>confocal</strong>.\nIn Cartesian coordinates, the confocal family through foci $(\\pm c, 0)$ is:\n$$\\frac{x^2}{a^2 + \\lambda} + \\frac{y^2}{b^2 + \\lambda} = 1 \\quad (\\lambda \\in \\mathbb{R})$$\nIn polar coordinates with a common focus at the pole, the confocal family with a common axis is:\n$$\\frac{l}{r} = 1 + e \\cos \\theta$$\nwhere $l$ and $e$ vary such that the second focus $S'$ is fixed.\n</p>\n\n<h3>2. Orthogonal Intersection Theorem</h3>\n<p>\n<strong>Fundamental Theorem of Confocal Conics:</strong>\nThrough any point $P(x_0, y_0)$ in the plane (not on the axes), there pass exactly two conics of a confocal family: one ellipse and one hyperbola.\nFurthermore, these two conics intersect each other <strong>at strictly right angles ($90^\\circ$)</strong> at point $P$!\nThis property is the foundation of elliptic coordinate systems used to solve Laplace's and Helmholtz's equations in mathematical physics.\n</p>\n"
        },
        {
          "id": "u8-sec5",
          "title": "Celestial Orbital Geometry & Keplerian Trajectories",
          "content": "\n<h3>1. Kepler's First Law and Newton's Gravitational Potential</h3>\n<p>\nIn celestial mechanics and orbital astrophysics, a satellite or planet orbiting a central gravitational mass $M$ under Newton's inverse-square gravitational force $\\mathbf{F} = -\\frac{G M m}{r^2}\\hat{\\mathbf{r}}$ obeys the Binet differential equation:\n$$\\frac{d^2 u}{d\\theta^2} + u = \\frac{G M}{h^2} = \\frac{\\mu}{h^2}$$\nwhere $u = 1/r$, $\\mu = GM$ is the gravitational parameter, and $h = r^2 \\dot{\\theta}$ is the specific angular momentum.\nThe exact general solution of this linear differential equation is:\n$$u = \\frac{\\mu}{h^2}(1 + e \\cos(\\theta - \\omega)) \\iff \\mathbf{r(\\theta) = \\frac{p}{1 + e \\cos(\\theta - \\omega)}}$$\nwhere $p = h^2/\\mu$ is the semi-latus rectum and $e$ is the orbital eccentricity!\n</p>\n\n<h3>2. The Energy-Eccentricity Correspondence (Vis-Viva Equation)</h3>\n<p>\nThe total specific orbital energy $\\mathcal{E} = \\frac{1}{2}v^2 - \\frac{\\mu}{r}$ is conserved along the trajectory:\n$$\\mathcal{E} = -\\frac{\\mu^2(1 - e^2)}{2h^2} = -\\frac{\\mu}{2a}$$\nThe sign of the orbital energy determines the conic geometry:\n<ul>\n  <li><strong>Bound Elliptical Orbit ($\\mathcal{E} < 0, \\; 0 \\le e < 1$):</strong> Periodic planetary orbits (Keplerian orbits).</li>\n  <li><strong>Parabolic Escape Trajectory ($\\mathcal{E} = 0, \\; e = 1$):</strong> Critical escape velocity $v_{\\text{esc}} = \\sqrt{2\\mu/r}$. The spacecraft possesses just enough energy to escape to infinity with zero residual velocity.</li>\n  <li><strong>Hyperbolic Flyby / Interstellar Trajectory ($\\mathcal{E} > 0, \\; e > 1$):</strong> Gravity-assist planetary flybys and interstellar objects (e.g., 1I/'Oumuamua and 2I/Borisov). The spacecraft escapes to infinity with hyperbolic excess speed $v_\\infty = \\sqrt{2\\mathcal{E}} = \\sqrt{\\mu/a}$.</li>\n</ul>\n</p>\n",
          "simulation": "geom2d-polar-conic-kepler-sim",
          "simulations": [
            "geom2d-polar-conic-kepler-sim"
          ]
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "Polar Conic Geometric Elements and Periapsis/Apoapsis",
          "statement": "A conic has the polar equation $\\frac{12}{r} = 3 + 2\\cos\\theta$: (a) Reduce the equation to standard form $\\frac{l}{r} = 1 + e\\cos\\theta$ and identify the conic. (b) Find the semi-latus rectum $l$, eccentricity $e$, and periapsis and apoapsis distances. (c) Determine the length of the major axis $2a$.",
          "steps": [
            {
              "step": "Step 1: Reduce to Standard Form",
              "math": "\\frac{12}{r} = 3\\left(1 + \\frac{2}{3}\\cos\\theta\\right) \\implies \\frac{12/3}{r} = 1 + \\frac{2}{3}\\cos\\theta \\implies \\frac{4}{r} = 1 + \\frac{2}{3}\\cos\\theta",
              "explanation": "Comparing with $\\frac{l}{r} = 1 + e\\cos\theta$ yields $l = 4$ and $e = 2/3$."
            },
            {
              "step": "Step 2: Identify Conic and Focal Extrema",
              "math": "e = \\frac{2}{3} < 1 \\implies \\text{The conic is an Ellipse!} \\\\ \\text{Periapsis } (\\theta = 0): \\quad r_{\\min} = \\frac{l}{1 + e} = \\frac{4}{1 + 2/3} = \\frac{4}{5/3} = \\frac{12}{5} = 2.4 \\\\ \\text{Apoapsis } (\\theta = \\pi): \\quad r_{\\max} = \\frac{l}{1 - e} = \\frac{4}{1 - 2/3} = \\frac{4}{1/3} = 12",
              "explanation": "The closest approach is $2.4$ and the furthest distance is $12$."
            },
            {
              "step": "Step 3: Length of Major Axis",
              "math": "2a = r_{\\min} + r_{\\max} = 2.4 + 12 = 14.4 \\implies a = 7.2",
              "explanation": "Check: $l = a(1 - e^2) \\implies 4 = a(1 - 4/9) = a(5/9) \\implies a = 36/5 = 7.2$. (Exact match!)"
            }
          ],
          "answer": "\\text{Ellipse: } \\frac{4}{r} = 1 + \\frac{2}{3}\\cos\\theta; \\quad l = 4, \\; e = \\frac{2}{3}; \\quad r_{\\min} = 2.4, \\; r_{\\max} = 12; \\quad 2a = 14.4"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "Tangent to a Polar Conic and Perpendicular Tangents",
          "statement": "Given the polar conic $\\frac{l}{r} = 1 + e\\cos\\theta$: (a) Write the equation of the tangent at point $P(\\alpha)$. (b) For the parabola $e = 1$, find the tangents at the ends of the latus rectum ($\\alpha = \\pi/2$ and $\\alpha = -\\pi/2$). (c) Prove that these two tangents intersect on the directrix at right angles.",
          "steps": [
            {
              "step": "Step 1: General Tangent Equation",
              "math": "\\frac{l}{r} = e\\cos\\theta + \\cos(\\theta - \\alpha)",
              "explanation": "This is the general polar tangent formula."
            },
            {
              "step": "Step 2: Tangents at $\\alpha = \\pm\\pi/2$ for Parabola ($e = 1$)",
              "math": "\\text{At } \\alpha = \\pi/2: \\quad \\frac{l}{r} = \\cos\\theta + \\cos(\\theta - \\pi/2) = \\cos\\theta + \\sin\\theta \\\\ \\text{At } \\alpha = -\\pi/2: \\quad \\frac{l}{r} = \\cos\\theta + \\cos(\\theta + \\pi/2) = \\cos\\theta - \\sin\\theta",
              "explanation": "In Cartesian coordinates ($x = r\\cos\theta, y = r\\sin\theta$): $l = x + y \\implies x + y = l$, and $l = x - y \\implies x - y = l$."
            },
            {
              "step": "Step 3: Intersection and Perpendicularity",
              "math": "x + y = l \\quad (m_1 = -1) \\\\ x - y = l \\quad (m_2 = +1) \\\\ m_1 m_2 = (-1)(1) = -1 \\implies \\text{Mutually Perpendicular!} \\\\ \\text{Adding: } 2x = 2l \\implies x = l, \\quad y = 0",
              "explanation": "Since the directrix of $\\frac{l}{r} = 1 + \\cos\theta$ is $x = -l$ (or $x = l$ depending on orientation), the tangents are orthogonal and intersect on the directrix axis."
            }
          ],
          "answer": "\\text{Tangents: } x + y = l \\text{ and } x - y = l; \\quad m_1 m_2 = -1 \\implies \\text{Orthogonal}; \\quad \\text{Intersection: } (l, 0)"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "Sum of Reciprocals of Mutually Perpendicular Focal Chords",
          "statement": "If $PQ$ and $RS$ are two mutually perpendicular focal chords of a conic $\\frac{l}{r} = 1 + e\\cos\\theta$, prove that the sum $\\frac{1}{PQ} + \\frac{1}{RS}$ is strictly constant and independent of the chord orientations.",
          "steps": [
            {
              "step": "Step 1: Length of a Focal Chord $PQ$",
              "math": "\\text{Let the inclination of chord } PQ \\text{ be } \\alpha. \\quad \\text{Then } P \\text{ is at } \\alpha \\text{ and } Q \\text{ is at } \\alpha + \\pi: \\\\ SP = \\frac{l}{1 + e\\cos\\alpha}, \\qquad SQ = \\frac{l}{1 + e\\cos(\\alpha + \\pi)} = \\frac{l}{1 - e\\cos\\alpha} \\\\ PQ = SP + SQ = \\frac{l}{1 + e\\cos\\alpha} + \\frac{l}{1 - e\\cos\\alpha} = \\frac{l(1 - e\\cos\\alpha + 1 + e\\cos\\alpha)}{1 - e^2\\cos^2\\alpha} = \\frac{2l}{1 - e^2\\cos^2\\alpha}",
              "explanation": "Thus the reciprocal of $PQ$ is: $\\frac{1}{PQ} = \\frac{1 - e^2\\cos^2\\alpha}{2l}$."
            },
            {
              "step": "Step 2: Length of the Perpendicular Focal Chord $RS$",
              "math": "\\text{Since } RS \\perp PQ, \\text{ the inclination of chord } RS \\text{ is } \\alpha + \\pi/2: \\\\ \\frac{1}{RS} = \\frac{1 - e^2\\cos^2(\\alpha + \\pi/2)}{2l} = \\frac{1 - e^2(-\\sin\\alpha)^2}{2l} = \\frac{1 - e^2\\sin^2\\alpha}{2l}",
              "explanation": "This expresses $1/RS$ in terms of $\\sin^2\\alpha$."
            },
            {
              "step": "Step 3: Sum the Reciprocals",
              "math": "\\frac{1}{PQ} + \\frac{1}{RS} = \\frac{1 - e^2\\cos^2\\alpha}{2l} + \\frac{1 - e^2\\sin^2\\alpha}{2l} = \\frac{2 - e^2(\\cos^2\\alpha + \\sin^2\\alpha)}{2l} = \\frac{2 - e^2(1)}{2l} = \\frac{2 - e^2}{2l}",
              "explanation": "Because $\\alpha$ cancels out entirely, the sum is strictly invariant!"
            }
          ],
          "answer": "\\frac{1}{PQ} + \\frac{1}{RS} = \\frac{2 - e^2}{2l} = \\text{Constant Everywhere}"
        }
      ],
      "simulations": [
        "geom2d-polar-conic-kepler-sim"
      ],
      "id": "unit8",
      "unitId": "unit8-geom2d",
      "leadSummary": "Unified universal polar formulation of conic sections: focus-at-pole derivation l/r = 1 + e cos theta; geometric classification and morphing across eccentricity e (circle e=0, ellipse 0<e<1, parabola e=1, hyperbola e>1); periapsis and apoapsis relations; chords, tangents l/r = e cos theta + cos(theta - alpha), and normals in polar coordinates; harmonic mean property of focal chord segments; confocal conics and orthogonal intersection theorems; and celestial orbital mechanics via Binet's equation, orbital energy, vis-viva equation, and hyperbolic escape flybys."
    }
  ]
};
