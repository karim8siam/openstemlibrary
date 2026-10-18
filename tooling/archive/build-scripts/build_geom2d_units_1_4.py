# -*- coding: utf-8 -*-
"""
Builder for 2D Geometry Units 1 to 4:
Unit 1: Cartesian & Polar Coordinate Systems, Distances & Coordinate Transformations
Unit 2: Pairs of Straight Lines (Homogeneous & Non-Homogeneous Second-Degree Equations)
Unit 3: The Circle: Tangents, Polars & Systems of Coaxial Circles
Unit 4: General Second-Degree Equation & Classification of Conic Sections
"""
import json

# -------------------------------------------------------------
# UNIT 1
# -------------------------------------------------------------
u1_sections = [
    {
        "id": "u1-sec1",
        "title": "Foundations of the Cartesian Plane, Distance Metrics & Section Formulas",
        "content": r"""
<h3>1. The Cartesian Coordinate System & Metric Geometry</h3>
<p>
The foundation of analytic geometry, pioneered by René Descartes and Pierre de Fermat, establishes a bijective correspondence between the Euclidean plane $\mathbb{E}^2$ and the Cartesian product of the real field $\mathbb{R}^2 = \mathbb{R} \times \mathbb{R}$. Any point $P \in \mathbb{E}^2$ is uniquely identified by an ordered pair of real coordinates $(x, y)$, representing signed perpendicular distances from two mutually orthogonal directed axes: the horizontal abscissa ($x$-axis) and the vertical ordinate ($y$-axis).
</p>
<p>
Under the standard Euclidean metric tensor $g_{ij} = \delta_{ij}$, the fundamental distance $d(P_1, P_2)$ between two points $P_1(x_1, y_1)$ and $P_2(x_2, y_2)$ is established directly via the Pythagorean theorem:
$$d(P_1, P_2) = \|\mathbf{r}_2 - \mathbf{r}_1\|_2 = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$
This Euclidean metric satisfies the three formal metric space axioms:
<ul>
  <li><strong>Positive Definiteness:</strong> $d(P_1, P_2) \ge 0$, with $d(P_1, P_2) = 0 \iff P_1 = P_2$.</li>
  <li><strong>Symmetry:</strong> $d(P_1, P_2) = d(P_2, P_1)$ for all $P_1, P_2 \in \mathbb{R}^2$.</li>
  <li><strong>Triangle Inequality:</strong> $d(P_1, P_3) \le d(P_1, P_2) + d(P_2, P_3)$, with equality holding if and only if $P_2$ lies on the straight segment $\overline{P_1 P_3}$.</li>
</ul>
</p>

<h3>2. The General Section Formula (Internal and External Division)</h3>
<p>
Let $P_1(x_1, y_1)$ and $P_2(x_2, y_2)$ be two distinct points in $\mathbb{R}^2$. A point $P(x, y)$ dividing the directed line segment $P_1 P_2$ in the ratio $m : n$ satisfies the vector relationship:
$$\frac{\vec{P_1 P}}{\vec{P P_2}} = \frac{m}{n} \iff n(\mathbf{r} - \mathbf{r}_1) = m(\mathbf{r}_2 - \mathbf{r})$$
Solving for the position vector $\mathbf{r} = (x, y)$:
$$\mathbf{r} = \frac{m \mathbf{r}_2 + n \mathbf{r}_1}{m + n}$$
In scalar Cartesian components:
$$x = \frac{m x_2 + n x_1}{m + n}, \qquad y = \frac{m y_2 + n y_1}{m + n}$$
</p>
<p>
<strong>Classification of Division:</strong>
<ul>
  <li><strong>Internal Division ($m/n > 0$):</strong> The point $P$ lies strictly between $P_1$ and $P_2$. When $m = n = 1$, $P$ is the <em>midpoint</em>:
  $$M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$</li>
  <li><strong>External Division ($m/n < 0$, with $m \ne -n$):</strong> Setting the ratio as $m : -n$, the point $P_{\text{ext}}$ lies on the extension of line segment $P_1 P_2$:
  $$x_{\text{ext}} = \frac{m x_2 - n x_1}{m - n}, \qquad y_{\text{ext}} = \frac{m y_2 - n y_1}{m - n}$$</li>
  <li><strong>Harmonic Conjugates:</strong> The points $P_{\text{int}}$ and $P_{\text{ext}}$ dividing $P_1 P_2$ internally and externally in the same absolute ratio $m:n$ form a <em>harmonic range</em> $(P_1, P_2; P_{\text{int}}, P_{\text{ext}}) = -1$, meaning their distances satisfy the classical harmonic mean relation:
  $$\frac{2}{P_1 P_2} = \frac{1}{P_1 P_{\text{int}}} + \frac{1}{P_1 P_{\text{ext}}}$$</li>
</ul>
</p>

<h3>3. Classic Triangle Centers in the Cartesian Plane</h3>
<p>
For a triangle $\triangle ABC$ with vertices $A(x_1, y_1)$, $B(x_2, y_2)$, $C(x_3, y_3)$ and opposite side lengths $a = BC, b = CA, c = AB$:
<ul>
  <li><strong>Centroid ($G$):</strong> The concurrence point of the three medians, dividing each median in ratio $2:1$:
  $$G = \left(\frac{x_1 + x_2 + x_3}{3}, \frac{y_1 + y_2 + y_3}{3}\right)$$</li>
  <li><strong>Incenter ($I$):</strong> The center of the inscribed circle, concurrence of internal angle bisectors:
  $$I = \left(\frac{a x_1 + b x_2 + c x_3}{a + b + c}, \frac{a y_1 + b y_2 + c y_3}{a + b + c}\right)$$</li>
  <li><strong>Excenters ($I_a, I_b, I_c$):</strong> Centers of the three excircles. The excenter opposite to vertex $A$ is:
  $$I_a = \left(\frac{-a x_1 + b x_2 + c x_3}{-a + b + c}, \frac{-a y_1 + b y_2 + c y_3}{-a + b + c}\right)$$</li>
  <li><strong>Euler Line Theorem:</strong> In any non-equilateral triangle, the orthocenter $H$, centroid $G$, and circumcenter $O$ are strictly collinear, satisfying the constant harmonic segment ratio:
  $$OG : GH = 1 : 2 \iff \mathbf{r}_H = 3\mathbf{r}_G - 2\mathbf{r}_O$$</li>
</ul>
</p>
"""
    },
    {
        "id": "u1-sec2",
        "title": "Area of Polygons, Collinearity & The Shoelace Determinant",
        "content": r"""
<h3>1. Determinant Formulation for the Area of a Triangle</h3>
<p>
Consider a triangle $\triangle ABC$ formed by non-collinear vertices $A(x_1, y_1)$, $B(x_2, y_2)$, and $C(x_3, y_3)$ arranged counterclockwise. The signed area $\mathcal{A}$ is given by the cross product of the edge vectors $\vec{AB} = (x_2 - x_1, y_2 - y_1)$ and $\vec{AC} = (x_3 - x_1, y_3 - y_1)$:
$$\mathcal{A} = \frac{1}{2} \left[ (x_2 - x_1)(y_3 - y_1) - (x_3 - x_1)(y_2 - y_1) \right]$$
Expanding this algebraic expression yields the celebrated $3 \times 3$ determinant formulation:
$$\mathcal{A} = \frac{1}{2} \begin{vmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{vmatrix} = \frac{1}{2} \left[ x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2) \right]$$
The physical unsigned area is given by the absolute value $|\mathcal{A}|$.
</p>

<h3>2. The Exact Criterion for Collinearity</h3>
<p>
Three distinct points $A(x_1, y_1)$, $B(x_2, y_2)$, $C(x_3, y_3)$ lie on a common straight line if and only if the triangle they span degenerates into a segment with zero area:
$$\text{Collinear} \iff \begin{vmatrix} x_1 & y_1 & 1 \\ x_2 & y_2 & 1 \\ x_3 & y_3 & 1 \end{vmatrix} = 0 \iff x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2) = 0$$
Alternatively, collinearity is characterized by equal slopes:
$$m_{AB} = m_{BC} \iff \frac{y_2 - y_1}{x_2 - x_1} = \frac{y_3 - y_2}{x_3 - x_2} \quad (x_1 \ne x_2 \ne x_3)$$
</p>

<h3>3. The Shoelace Formula for General Simple Polygons</h3>
<p>
By applying Green's Theorem $\iint_D dA = \frac{1}{2} \oint_{\partial D} (x \, dy - y \, dx)$ to a planar polygonal domain bounded by $n$ ordered vertices $P_1(x_1, y_1), P_2(x_2, y_2), \dots, P_n(x_n, y_n)$ traversed counterclockwise, the exact area is given by the <strong>Shoelace Formula</strong>:
$$\mathcal{A}_n = \frac{1}{2} \left| \sum_{i=1}^{n} (x_i y_{i+1} - x_{i+1} y_i) \right| = \frac{1}{2} \left| (x_1 y_2 + x_2 y_3 + \dots + x_n y_1) - (y_1 x_2 + y_2 x_3 + \dots + y_n x_1) \right|$$
where cyclic indexing applies such that $(x_{n+1}, y_{n+1}) \equiv (x_1, y_1)$.
</p>
"""
    },
    {
        "id": "u1-sec3",
        "title": "The Polar Coordinate System & Metric Geometry",
        "content": r"""
<h3>1. Coordinate Definition & Bijective Transitions</h3>
<p>
In the <strong>polar coordinate system</strong>, a point $P$ in the Euclidean plane is specified relative to a fixed origin $O$ (termed the <em>pole</em>) and a horizontal directed ray extending to the right (the <em>polar axis</em>). The point is denoted by the ordered pair $(r, \theta)$:
<ul>
  <li><strong>Radial Coordinate ($r$):</strong> The directed Euclidean distance from pole $O$ to point $P$, $r \in [0, \infty)$.</li>
  <li><strong>Angular Coordinate ($\theta$):</strong> The counterclockwise angle measured from the polar axis to the ray $OP$, $\theta \in (-\pi, \pi]$ or $\theta \in [0, 2\pi)$.</li>
</ul>
</p>
<p>
The exact bijective conversion between Cartesian $(x, y)$ and Polar $(r, \theta)$ representations is given by:
$$\begin{cases} x = r \cos \theta \\ y = r \sin \theta \end{cases} \iff \begin{cases} r = \sqrt{x^2 + y^2} \\ \theta = \operatorname{atan2}(y, x) \end{cases}$$
where $\operatorname{atan2}(y, x)$ resolves the proper quadrant of $\theta$ without ambiguity:
$$\operatorname{atan2}(y, x) = \begin{cases} \arctan(y/x) & x > 0 \\ \arctan(y/x) + \pi & x < 0, \, y \ge 0 \\ \arctan(y/x) - \pi & x < 0, \, y < 0 \\ +\pi/2 & x = 0, \, y > 0 \\ -\pi/2 & x = 0, \, y < 0 \\ \text{undefined} & x = 0, \, y = 0 \end{cases}$$
</p>

<h3>2. Distance Formula & Triangle Area in Polar Form</h3>
<p>
Let $P_1(r_1, \theta_1)$ and $P_2(r_2, \theta_2)$ be two points expressed in polar coordinates. In $\triangle O P_1 P_2$, the angle subtended at the pole is $|\theta_2 - \theta_1|$. By the Law of Cosines:
$$d(P_1, P_2)^2 = r_1^2 + r_2^2 - 2 r_1 r_2 \cos(\theta_2 - \theta_1)$$
$$d(P_1, P_2) = \sqrt{r_1^2 + r_2^2 - 2 r_1 r_2 \cos(\theta_2 - \theta_1)}$$
</p>
<p>
The area of the triangle $\triangle O P_1 P_2$ formed by the pole and the two points is:
$$\mathcal{A}_{\triangle O P_1 P_2} = \frac{1}{2} r_1 r_2 \sin|\theta_2 - \theta_1|$$
For three arbitrary points $P_1(r_1, \theta_1), P_2(r_2, \theta_2), P_3(r_3, \theta_3)$, the enclosed area is:
$$\mathcal{A} = \frac{1}{2} \left| r_1 r_2 \sin(\theta_2 - \theta_1) + r_2 r_3 \sin(\theta_3 - \theta_2) + r_3 r_1 \sin(\theta_1 - \theta_3) \right|$$
</p>
"""
    },
    {
        "id": "u1-sec4",
        "title": "Translation of Coordinate Axes & Origin Shifting",
        "content": r"""
<h3>1. Algebraic Mechanics of Axis Translation</h3>
<p>
In many analytical geometric investigations, the mathematical form of a curve simplifies dramatically when the origin of coordinates is shifted to a new point $O'(h, k)$ while maintaining the parallel orientation and direction of the axes.
</p>
<p>
Let $(x, y)$ denote the coordinates of a point $P$ referred to the original axes $Ox, Oy$, and let $(X, Y)$ denote the coordinates of the same physical point $P$ referred to the translated axes $O'X, O'Y$. From vector addition:
$$\mathbf{r} = \mathbf{r}_{O'} + \mathbf{r}' \implies \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} X + h \\ Y + k \end{pmatrix}$$
Conversely, the new coordinates in terms of the old are:
$$\begin{cases} X = x - h \\ Y = y - k \end{cases}$$
</p>

<h3>2. Transformation of Algebraic Curves</h3>
<p>
Given a planar curve described by the implicit polynomial equation $f(x, y) = 0$, its transformed equation in the new coordinate frame $(X, Y)$ is obtained by direct substitution:
$$F(X, Y) = f(X + h, Y + k) = 0$$
</p>
<p>
<strong>Invariance Under Pure Translation:</strong>
<ul>
  <li><strong>Distance Invariance:</strong> $d(P_1, P_2) = \sqrt{(X_2 - X_1)^2 + (Y_2 - Y_1)^2} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.</li>
  <li><strong>Slope Invariance:</strong> $M = \frac{Y_2 - Y_1}{X_2 - X_1} = \frac{(y_2 - k) - (y_1 - k)}{(x_2 - h) - (x_1 - h)} = \frac{y_2 - y_1}{x_2 - x_1} = m$.</li>
  <li><strong>Angle & Area Invariance:</strong> Translation preserves all angles between intersecting curves and all enclosed polygonal and curvilinear areas.</li>
  <li><strong>Second-Degree Coefficient Invariance:</strong> In the general second-degree equation $a x^2 + 2h xy + b y^2 + 2g x + 2f y + c = 0$, pure translation changes only the linear terms ($g, f$) and the constant $c$, leaving the second-degree quadratic coefficients $a, h, b$ strictly invariant!</li>
</ul>
</p>
"""
    },
    {
        "id": "u1-sec5",
        "title": "Rotation of Axes & General Rigid Euclidean Motion",
        "content": r"""
<h3>1. Mathematical Formulation of Axis Rotation</h3>
<p>
Let the Cartesian axes $Ox, Oy$ be rotated counterclockwise through an angle $\theta$ about the fixed origin $O$ to a new coordinate system $OX, OY$.
Let a point $P$ have polar coordinates $(r, \phi)$ with respect to the original system, so that $x = r \cos \phi$ and $y = r \sin \phi$.
In the rotated system, the distance $r$ remains unchanged, but the angle from the $OX$-axis to $OP$ is $\phi - \theta$. Therefore:
$$X = r \cos(\phi - \theta) = r \cos \phi \cos \theta + r \sin \phi \sin \theta = x \cos \theta + y \sin \theta$$
$$Y = r \sin(\phi - \theta) = r \sin \phi \cos \theta - r \cos \phi \sin \theta = -x \sin \theta + y \cos \theta$$
Inverting these linear relations gives the old coordinates $(x, y)$ in terms of the new coordinates $(X, Y)$:
$$\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \begin{pmatrix} X \\ Y \end{pmatrix} \iff \begin{cases} x = X \cos \theta - Y \sin \theta \\ y = X \sin \theta + Y \cos \theta \end{cases}$$
The transformation matrix:
$$\mathbf{R}(\theta) = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$$
is a special orthogonal matrix belonging to the Lie group $\mathrm{SO}(2)$, satisfying $\mathbf{R}^T \mathbf{R} = \mathbf{I}$ and $\det \mathbf{R} = +1$.
</p>

<h3>2. The Elimination of the Cross-Product Term ($xy$)</h3>
<p>
Under rotation of axes through an angle $\theta$, the general second-degree form $a x^2 + 2h xy + b y^2$ transforms into $A X^2 + 2H XY + B Y^2$.
Expanding and grouping terms:
$$A = a \cos^2 \theta + 2h \sin \theta \cos \theta + b \sin^2 \theta$$
$$B = a \sin^2 \theta - 2h \sin \theta \cos \theta + b \cos^2 \theta$$
$$2H = 2(b - a)\sin \theta \cos \theta + 2h(\cos^2 \theta - \sin^2 \theta) = (b - a)\sin 2\theta + 2h \cos 2\theta$$
To eliminate the cross-product term $XY$, we require $H = 0$:
$$(b - a)\sin 2\theta + 2h \cos 2\theta = 0 \iff (a - b)\sin 2\theta = 2h \cos 2\theta$$
$$\tan 2\theta = \frac{2h}{a - b} \quad (a \ne b), \qquad \text{or } \theta = \frac{\pi}{4} \quad (a = b)$$
This fundamental relation is the cornerstone of conic canonical reduction!
</p>

<h3>3. Rotational Invariants of Quadratic Forms</h3>
<p>
For any rotation of axes, the coefficients of the quadratic form satisfy two algebraic invariants:
$$\mathbf{Invariant \; 1:} \quad A + B = a + b \quad (\text{Trace of the matrix})$$
$$\mathbf{Invariant \; 2:} \quad AB - H^2 = ab - h^2 \quad (\text{Determinant of the matrix})$$
These invariants ensure that the geometric nature of the quadratic curve (ellipse, parabola, or hyperbola) is an intrinsic property of the curve, independent of the choice of coordinate axes!
</p>
""",
        "simulation": "geom2d-coord-transform-sim",
        "simulations": ["geom2d-coord-transform-sim"]
    }
]

u1_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Collinearity and Harmonic Division of a Line Segment",
        "statement": r"Given three points $A(-3, -2)$, $B(1, 4)$, and $C(5, 10)$: (a) Prove that the points are collinear using the determinant condition. (b) Find the ratio in which point $B$ divides the line segment $AC$. (c) Determine the coordinates of the harmonic conjugate point $D$ that divides $AC$ externally in the same ratio.",
        "steps": [
            {
                "step": "Step 1: Verify Collinearity via Determinant",
                "math": r"\Delta = \begin{vmatrix} -3 & -2 & 1 \\ 1 & 4 & 1 \\ 5 & 10 & 1 \end{vmatrix} = -3(4 - 10) - (-2)(1 - 5) + 1(10 - 20) = -3(-6) + 2(-4) + 1(-10) = 18 - 8 - 10 = 0",
                "explanation": "Since the determinant vanishes identically, $\Delta = 0$, the points $A, B, C$ are strictly collinear."
            },
            {
                "step": "Step 2: Determine Division Ratio $m:n$",
                "math": r"x_B = \frac{m x_C + n x_A}{m + n} \implies 1 = \frac{5m - 3n}{m + n} \implies m + n = 5m - 3n \implies 4m = 4n \implies \frac{m}{n} = 1",
                "explanation": "Thus $B$ divides $AC$ internally in the ratio $1 : 1$, which means $B$ is the exact midpoint of $AC$ ($y$-coordinate check: $\frac{10 + (-2)}{2} = 4 = y_B$)."
            },
            {
                "step": "Step 3: Find Harmonic Conjugate $D$ (External Division)",
                "math": r"\text{For ratio } 1 : 1, \quad m - n = 0 \implies D \text{ lies at the point at infinity along the line } AC",
                "explanation": "When an internal point is the exact midpoint ($1:1$), its harmonic conjugate lies at the line's point at infinity: $(A, C; B, D_{\infty}) = -1$."
            }
        ],
        "answer": r"\Delta = 0 \implies \text{Collinear}; \quad \text{Internal Ratio } = 1 : 1 \text{ (Midpoint)}; \quad \text{Harmonic Conjugate } D = \text{Point at infinity along } AC"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Area of Triangle and Metric Distance in Polar Coordinates",
        "statement": r"Two points in the polar coordinate plane are given by $P_1\left(6, \frac{\pi}{6}\right)$ and $P_2\left(8, \frac{\pi}{2}\right)$, and the pole is $O(0, 0)$. (a) Compute the exact Euclidean distance $d(P_1, P_2)$. (b) Calculate the exact area of the triangle $\triangle O P_1 P_2$. (c) Find the polar equation of the circumcircle of $\triangle O P_1 P_2$.",
        "steps": [
            {
                "step": "Step 1: Compute Polar Distance",
                "math": r"d^2 = r_1^2 + r_2^2 - 2 r_1 r_2 \cos(\theta_2 - \theta_1) = 6^2 + 8^2 - 2(6)(8)\cos\left(\frac{\pi}{2} - \frac{\pi}{6}\right) = 36 + 64 - 96 \cos\left(\frac{\pi}{3}\right)",
                "explanation": "Using $\cos(\pi/3) = 1/2$: $d^2 = 100 - 96(0.5) = 100 - 48 = 52 \implies d = \sqrt{52} = 2\sqrt{13}$."
            },
            {
                "step": "Step 2: Calculate Area of Triangle $\triangle O P_1 P_2$",
                "math": r"\mathcal{A} = \frac{1}{2} r_1 r_2 \sin(\theta_2 - \theta_1) = \frac{1}{2}(6)(8)\sin\left(\frac{\pi}{3}\right) = 24 \left(\frac{\sqrt{3}}{2}\right) = 12\sqrt{3}",
                "explanation": "The exact area of the polar triangle is $12\sqrt{3}$ square units."
            },
            {
                "step": "Step 3: Circumcircle Polar Equation",
                "math": r"\text{Cartesian coords: } P_1 = (6\cos 30^\circ, 6\sin 30^\circ) = (3\sqrt{3}, 3), \quad P_2 = (0, 8), \quad O = (0, 0) \\ \text{Circle through } O, P_1, P_2: x^2 + y^2 - 3\sqrt{3}x - 8y = 0 \implies r^2 - r(3\sqrt{3}\cos\theta + 8\sin\theta) = 0 \implies r = 3\sqrt{3}\cos\theta + 8\sin\theta",
                "explanation": "Dividing by $r \ne 0$ yields the polar equation of the circle passing through the origin."
            }
        ],
        "answer": r"d(P_1, P_2) = 2\sqrt{13}; \quad \mathcal{A} = 12\sqrt{3}; \quad \text{Circumcircle: } r = 3\sqrt{3}\cos\theta + 8\sin\theta"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Complete Rigid Euclidean Transformation Eliminating Linear and Cross Terms",
        "statement": r"Consider the second-degree curve equation $17x^2 - 12xy + 8y^2 + 46x - 28y + 17 = 0$. (a) Determine the translation $(h, k)$ that eliminates the linear first-degree terms. (b) Find the exact counterclockwise rotation angle $\theta$ that eliminates the cross-product $XY$ term. (c) Write the canonical standard form of the curve and identify its geometric nature.",
        "steps": [
            {
                "step": "Step 1: Determine the Center $(h, k)$ via Partial Derivatives",
                "math": r"F_x = 34x - 12y + 46 = 0 \implies 17h - 6k = -23 \\ F_y = -12x + 16y - 28 = 0 \implies -3h + 4k = 7",
                "explanation": "Multiplying the second equation by 3 and the first by 2: $34h - 12k = -46$, $-9h + 12k = 21 \implies 25h = -25 \implies h = -1$. Substituting: $4k = 7 + 3(-1) = 4 \implies k = 1$. The center is $(-1, 1)$."
            },
            {
                "step": "Step 2: Translate Origin to $(-1, 1)$",
                "math": r"c' = gh + fk + c = 23(-1) + (-14)(1) + 17 = -23 - 14 + 17 = -20 \\ \text{Shifted equation: } 17X^2 - 12XY + 8Y^2 = 20",
                "explanation": "The linear terms are completely eliminated; the quadratic coefficients remain $a = 17, 2h = -12 \implies h = -6, b = 8$."
            },
            {
                "step": "Step 3: Determine Rotation Angle $\theta$ to Eliminate Cross Term",
                "math": r"\tan 2\theta = \frac{2h}{a - b} = \frac{-12}{17 - 8} = \frac{-12}{9} = -\frac{4}{3}",
                "explanation": "Since $\tan 2\theta = -4/3$, we have $\cos 2\theta = -3/5$. Using half-angle formulas: $\sin^2 \theta = \frac{1 - \cos 2\theta}{2} = \frac{1 - (-3/5)}{2} = \frac{4}{5} \implies \sin \theta = \frac{2}{\sqrt{5}}$, $\cos \theta = \frac{1}{\sqrt{5}} \implies \theta = \arctan(2)$."
            },
            {
                "step": "Step 4: Compute Canonical Eigenvalues and Final Equation",
                "math": r"\lambda^2 - (a+b)\lambda + (ab - h^2) = 0 \implies \lambda^2 - 25\lambda + (136 - 36) = \lambda^2 - 25\lambda + 100 = 0 \\ (\lambda - 20)(\lambda - 5) = 0 \implies \lambda_1 = 5, \quad \lambda_2 = 20 \\ \text{Canonical form: } 5X'^2 + 20Y'^2 = 20 \iff \frac{X'^2}{4} + \frac{Y'^2}{1} = 1",
                "explanation": "The equation reduces to an ellipse centered at $(-1, 1)$, with major semi-axis $a = 2$, minor semi-axis $b = 1$, and rotated by $\theta = \arctan(2)$."
            }
        ],
        "answer": r"\text{Translation: } (h, k) = (-1, 1); \quad \text{Rotation: } \theta = \arctan(2) \approx 63.43^\circ; \quad \text{Canonical Form: } \frac{X'^2}{4} + \frac{Y'^2}{1} = 1 \text{ (Ellipse)}"
    }
]

u1_data = {
    "unitNumber": 1,
    "number": 1,
    "title": "Cartesian & Polar Coordinate Systems, Distances & Transformations",
    "description": "Comprehensive analytical foundations of two-dimensional coordinate geometry: Cartesian metric space axioms, distance and section formulas, harmonic ranges, triangle centers and the Euler line, shoelace polygon area determinants, polar coordinates and metric relations, translation of axes and curve transformations, rotation of axes via SO(2) orthogonal matrices, and fundamental quadratic invariants.",
    "sections": u1_sections,
    "problems": u1_problems
}

# -------------------------------------------------------------
# UNIT 2
# -------------------------------------------------------------
u2_sections = [
    {
        "id": "u2-sec1",
        "title": "Homogeneous Quadratic Equations & Line Pairs Through Origin",
        "content": r"""
<h3>1. The Homogeneous Second-Degree Equation</h3>
<p>
The most general homogeneous algebraic equation of second degree in two variables $x$ and $y$ is:
$$a x^2 + 2h xy + b y^2 = 0 \quad (a, h, b \in \mathbb{R}, \; \text{not all zero})$$
Assuming $b \ne 0$, we can divide by $x^2$ (for $x \ne 0$) and set $m = y/x$ (the slope of a line through the origin):
$$b \left(\frac{y}{x}\right)^2 + 2h \left(\frac{y}{x}\right) + a = 0 \iff b m^2 + 2h m + a = 0$$
This is a quadratic equation in the slope $m$. By the quadratic formula, the two roots $m_1$ and $m_2$ are:
$$m_1, m_2 = \frac{-2h \pm \sqrt{4h^2 - 4ab}}{2b} = \frac{-h \pm \sqrt{h^2 - ab}}{b}$$
Therefore, the quadratic expression factors over $\mathbb{R}$ into two linear equations:
$$a x^2 + 2h xy + b y^2 = b(y - m_1 x)(y - m_2 x) = 0$$
representing two straight lines passing through the origin $O(0, 0)$:
$$L_1: y - m_1 x = 0, \qquad L_2: y - m_2 x = 0$$
</p>

<h3>2. The Reality Discriminant ($h^2 - ab$)</h3>
<p>
From Viète's formulas for $b m^2 + 2h m + a = 0$:
$$m_1 + m_2 = -\frac{2h}{b}, \qquad m_1 m_2 = \frac{a}{b}$$
The nature of the lines is completely governed by the discriminant $D_L \equiv h^2 - ab$:
<ul>
  <li><strong>Real and Distinct Lines ($h^2 > ab$):</strong> The quadratic has two distinct real slopes $m_1 \ne m_2$, representing two real intersecting straight lines passing through the origin.</li>
  <li><strong>Real and Coincident Lines ($h^2 = ab$):</strong> The discriminant vanishes, giving a single repeated root $m_1 = m_2 = -h/b$. The equation represents two coincident (identical) lines:
  $$a x^2 + 2h xy + b y^2 = (\sqrt{a}x + \sqrt{b}y)^2 = 0 \iff \sqrt{a}x + \sqrt{b}y = 0$$</li>
  <li><strong>Imaginary Lines with Real Intersection ($h^2 < ab$):</strong> The slopes $m_1, m_2$ are complex conjugates $m = \alpha \pm i \beta$. The equation has no real solutions other than the single isolated real point of intersection $(0, 0)$.</li>
</ul>
</p>
"""
    },
    {
        "id": "u2-sec2",
        "title": "Angle Between Line Pairs & Orthogonality Conditions",
        "content": r"""
<h3>1. Derivation of the Acute Angle Between Lines</h3>
<p>
Let $\theta$ be the acute angle between the two lines $y = m_1 x$ and $y = m_2 x$ represented by $a x^2 + 2h xy + b y^2 = 0$. From elementary trigonometry:
$$\tan \theta = \left| \frac{m_1 - m_2}{1 + m_1 m_2} \right|$$
Using the algebraic identity $(m_1 - m_2)^2 = (m_1 + m_2)^2 - 4 m_1 m_2$:
$$|m_1 - m_2| = \sqrt{\left(-\frac{2h}{b}\right)^2 - 4\left(\frac{a}{b}\right)} = \frac{2\sqrt{h^2 - ab}}{|b|}$$
Substituting into the tangent formula:
$$\tan \theta = \left| \frac{\frac{2\sqrt{h^2 - ab}}{b}}{1 + \frac{a}{b}} \right| = \left| \frac{2\sqrt{h^2 - ab}}{a + b} \right|$$
This is the universally famous formula for the angle between a pair of straight lines!
</p>

<h3>2. The Orthogonality Condition ($a + b = 0$)</h3>
<p>
The two lines are mutually perpendicular ($\theta = \pi/2$) if and only if $\tan \theta \to \infty$, which requires the denominator to vanish:
$$\mathbf{Perpendicularity \iff} \quad a + b = 0 \iff \text{Coefficient of } x^2 + \text{Coefficient of } y^2 = 0$$
Notice that this condition holds regardless of the value of $h$! When $a + b = 0$, the lines are orthogonal.
</p>

<h3>3. The Parallel / Coincidence Condition ($h^2 = ab$)</h3>
<p>
The two lines are parallel or coincident ($\theta = 0$) if and only if $\tan \theta = 0$, which requires the numerator to vanish:
$$\mathbf{Coincidence \iff} \quad h^2 - ab = 0 \iff h^2 = ab$$
</p>
"""
    },
    {
        "id": "u2-sec3",
        "title": "Joint Equation of Angle Bisectors & Orthogonality Proof",
        "content": r"""
<h3>1. Derivation of the Bisector Pair Equation</h3>
<p>
Let the lines be $L_1: y - m_1 x = 0$ and $L_2: y - m_2 x = 0$. Any point $P(x, y)$ on the bisectors of the angles between $L_1$ and $L_2$ is equidistant from both lines:
$$\frac{|y - m_1 x|}{\sqrt{1 + m_1^2}} = \frac{|y - m_2 x|}{\sqrt{1 + m_2^2}}$$
Squaring both sides eliminates the absolute values:
$$\frac{(y - m_1 x)^2}{1 + m_1^2} = \frac{(y - m_2 x)^2}{1 + m_2^2} \iff (1 + m_2^2)(y - m_1 x)^2 - (1 + m_1^2)(y - m_2 x)^2 = 0$$
Expanding and factoring $(m_1 - m_2) \ne 0$:
$$(1 - m_1 m_2)(x^2 - y^2) + 2(m_1 + m_2)xy = 0$$
Substituting $m_1 + m_2 = -2h/b$ and $m_1 m_2 = a/b$:
$$\left(1 - \frac{a}{b}\right)(x^2 - y^2) + 2\left(-\frac{2h}{b}\right)xy = 0 \iff \frac{b - a}{b}(x^2 - y^2) - \frac{4h}{b}xy = 0$$
Dividing by $-(b - a) \cdot 4h$ yields the standard canonical symmetric form:
$$\frac{x^2 - y^2}{a - b} = \frac{xy}{h} \iff h(x^2 - y^2) - (a - b)xy = 0$$
</p>

<h3>2. Proof of Mutual Perpendicularity of Bisectors</h3>
<p>
The joint bisector equation is a homogeneous second-degree equation of the form $A x^2 + 2H xy + B y^2 = 0$, where:
$$A = h, \qquad 2H = -(a - b), \qquad B = -h$$
Applying the orthogonality criterion derived in Section 2.2:
$$A + B = h + (-h) = 0$$
Because the sum of the coefficients of $x^2$ and $y^2$ is identically zero, **the internal and external angle bisectors are always strictly mutually perpendicular**!
</p>
"""
    },
    {
        "id": "u2-sec4",
        "title": "General Second-Degree Equation Representing a Pair of Straight Lines",
        "content": r"""
<h3>1. The Non-Homogeneous General Equation</h3>
<p>
The general non-homogeneous algebraic equation of second degree is:
$$F(x, y) = a x^2 + 2h xy + b y^2 + 2g x + 2f y + c = 0$$
For this equation to represent two distinct or coincident straight lines, it must be factorizable into two linear factors:
$$F(x, y) = (l_1 x + m_1 y + n_1)(l_2 x + m_2 y + n_2) = 0$$
Equating coefficients of identical monomials:
$$l_1 l_2 = a, \quad m_1 m_2 = b, \quad n_1 n_2 = c$$
$$l_1 m_2 + l_2 m_1 = 2h, \quad l_1 n_2 + l_2 n_1 = 2g, \quad m_1 n_2 + m_2 n_1 = 2f$$
</p>

<h3>2. The Determinant Condition $\Delta = 0$</h3>
<p>
Eliminating $l_i, m_i, n_i$ establishes the necessary and sufficient condition for $F(x, y) = 0$ to represent a pair of lines:
$$\Delta \equiv \begin{vmatrix} a & h & g \\ h & b & f \\ g & f & c \end{vmatrix} = 0 \iff abc + 2fgh - af^2 - bg^2 - ch^2 = 0$$
Together with $h^2 \ge ab$ (ensuring the lines are real).
</p>

<h3>3. Point of Intersection via Partial Derivatives</h3>
<p>
When $\Delta = 0$, the two lines intersect at a unique point $(\bar{x}, \bar{y})$ which is the singular point of the algebraic curve. Taking partial derivatives of $F(x, y)$:
$$\frac{\partial F}{\partial x} = 2ax + 2hy + 2g = 0 \implies ax + hy + g = 0$$
$$\frac{\partial F}{\partial y} = 2hx + 2by + 2f = 0 \implies hx + by + f = 0$$
Solving this $2 \times 2$ linear system by Cramer's rule yields the point of intersection:
$$\bar{x} = \frac{hf - bg}{ab - h^2}, \qquad \bar{y} = \frac{gh - af}{ab - h^2} \quad (ab - h^2 \ne 0)$$
</p>
"""
    },
    {
        "id": "u2-sec5",
        "title": "Parallel Line Pairs, Distance & The Homogenization Technique",
        "content": r"""
<h3>1. Condition for Parallel Lines</h3>
<p>
If the lines represented by $ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0$ are parallel, their second-degree terms must form a perfect square:
$$h^2 - ab = 0 \iff \frac{a}{h} = \frac{h}{b} = \frac{g}{f}$$
The perpendicular distance $d$ between the two parallel lines is given by:
$$d = 2\sqrt{\frac{g^2 - ac}{a(a + b)}} = 2\sqrt{\frac{f^2 - bc}{b(a + b)}}$$
</p>

<h3>2. The Method of Homogenization</h3>
<p>
A powerful technique in classical geometry is finding the joint equation of the two straight lines connecting the origin $O(0, 0)$ to the intersection points of a general second-degree curve $S \equiv ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0$ and a line $L \equiv lx + my + n = 0$.
<ol>
  <li>Write the equation of the line in normalized unit form:
  $$\frac{lx + my}{-n} = 1 \quad (n \ne 0)$$</li>
  <li>Make the equation of the curve homogeneous of degree 2 by multiplying the linear terms by $(1)$ and the constant term by $(1)^2$:
  $$ax^2 + 2hxy + by^2 + 2(gx + fy)\left(\frac{lx + my}{-n}\right) + c\left(\frac{lx + my}{-n}\right)^2 = 0$$</li>
  <li>Because this resulting equation is purely homogeneous of degree 2, it represents two straight lines passing through the origin, and since it is satisfied by all points satisfying both $S = 0$ and $L = 0$, it is the exact joint equation of the lines connecting the origin to the intersection points!</li>
</ol>
</p>
""",
        "simulation": "geom2d-line-pair-sim",
        "simulations": ["geom2d-line-pair-sim"]
    }
]

u2_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Angle Between Line Pair and Joint Equation of Bisectors",
        "statement": r"Given the homogeneous second-degree equation $2x^2 + 7xy + 3y^2 = 0$: (a) Find the individual equations of the two lines. (b) Calculate the acute angle $\theta$ between them. (c) Derive the joint equation of the bisectors of the angles between the lines.",
        "steps": [
            {
                "step": "Step 1: Factor the Homogeneous Quadratic",
                "math": r"2x^2 + 7xy + 3y^2 = 2x^2 + 6xy + xy + 3y^2 = 2x(x + 3y) + y(x + 3y) = (2x + y)(x + 3y) = 0",
                "explanation": "The individual lines are $L_1: 2x + y = 0$ (slope $m_1 = -2$) and $L_2: x + 3y = 0$ (slope $m_2 = -1/3$)."
            },
            {
                "step": "Step 2: Calculate the Acute Angle $\theta$",
                "math": r"\tan \theta = \left|\frac{2\sqrt{h^2 - ab}}{a + b}\right| = \left|\frac{2\sqrt{(7/2)^2 - (2)(3)}}{2 + 3}\right| = \frac{2\sqrt{49/4 - 6}}{5} = \frac{2\sqrt{25/4}}{5} = \frac{2(5/2)}{5} = \frac{5}{5} = 1",
                "explanation": "Since $\tan \theta = 1$, the acute angle between the two lines is $\theta = \frac{\pi}{4} = 45^\circ$."
            },
            {
                "step": "Step 3: Joint Equation of Angle Bisectors",
                "math": r"\frac{x^2 - y^2}{a - b} = \frac{xy}{h} \implies \frac{x^2 - y^2}{2 - 3} = \frac{xy}{7/2} \implies \frac{x^2 - y^2}{-1} = \frac{2xy}{7} \implies 7(x^2 - y^2) = -2xy \implies 7x^2 + 2xy - 7y^2 = 0",
                "explanation": "Notice coefficient sum: $7 + (-7) = 0$, confirming mutual perpendicularity of the bisector pair."
            }
        ],
        "answer": r"\text{Lines: } 2x + y = 0 \text{ and } x + 3y = 0; \quad \theta = 45^\circ; \quad \text{Bisectors: } 7x^2 + 2xy - 7y^2 = 0"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "General Second-Degree Equation Verification and Point of Intersection",
        "statement": r"Show that the equation $2x^2 - 5xy + 2y^2 + 7x - 5y + 3 = 0$ represents a pair of straight lines. Find their point of intersection and the acute angle between them.",
        "steps": [
            {
                "step": "Step 1: Verify the Determinant Condition $\Delta = 0$",
                "math": r"a = 2, \; h = -5/2, \; b = 2, \; g = 7/2, \; f = -5/2, \; c = 3 \\ \Delta = \begin{vmatrix} 2 & -5/2 & 7/2 \\ -5/2 & 2 & -5/2 \\ 7/2 & -5/2 & 3 \end{vmatrix} = 2\left(6 - \frac{25}{4}\right) - \left(-\frac{5}{2}\right)\left(-\frac{15}{2} + \frac{35}{4}\right) + \frac{7}{2}\left(\frac{25}{4} - 7\right) \\ = 2\left(-\frac{1}{4}\right) + \frac{5}{2}\left(\frac{5}{4}\right) + \frac{7}{2}\left(-\frac{3}{4}\right) = -\frac{2}{4} + \frac{25}{8} - \frac{21}{8} = -\frac{4}{8} + \frac{4}{8} = 0",
                "explanation": "Since $\Delta = 0$ and $h^2 - ab = 25/4 - 4 = 9/4 > 0$, the equation represents two real intersecting straight lines."
            },
            {
                "step": "Step 2: Find Point of Intersection",
                "math": r"\frac{\partial F}{\partial x} = 4x - 5y + 7 = 0 \\ \frac{\partial F}{\partial y} = -5x + 4y - 5 = 0 \\ \text{Adding: } -x - y + 2 = 0 \implies y = 2 - x \\ 4x - 5(2 - x) + 7 = 0 \implies 9x - 3 = 0 \implies x = \frac{1}{3}, \quad y = \frac{5}{3}",
                "explanation": "The lines intersect at the point $(1/3, 5/3)$."
            },
            {
                "step": "Step 3: Compute Acute Angle $\theta$",
                "math": r"\tan \theta = \left|\frac{2\sqrt{h^2 - ab}}{a + b}\right| = \left|\frac{2\sqrt{25/4 - 4}}{2 + 2}\right| = \frac{2(3/2)}{4} = \frac{3}{4} \implies \theta = \arctan(3/4) \approx 36.87^\circ",
                "explanation": "The acute angle between the lines is $\arctan(3/4)$."
            }
        ],
        "answer": r"\Delta = 0 \implies \text{Represents pair of straight lines}; \quad \text{Intersection: } \left(\frac{1}{3}, \frac{5}{3}\right); \quad \theta = \arctan\left(\frac{3}{4}\right)"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Homogenization: Right-Angled Subtended Chords from a Circle to the Origin",
        "statement": r"A straight line $L \equiv 2x + y = k$ intersects the circle $x^2 + y^2 - 2x - 4y - 4 = 0$ at two distinct points $A$ and $B$. (a) Formulate the joint homogeneous equation of the lines $OA$ and $OB$ joining the origin to $A$ and $B$. (b) Determine the values of the constant $k$ such that the chord $AB$ subtends a right angle at the origin ($OA \perp OB$).",
        "steps": [
            {
                "step": "Step 1: Express the Line in Normalized Unit Form",
                "math": r"2x + y = k \implies \frac{2x + y}{k} = 1 \quad (k \ne 0)",
                "explanation": "This unit expression is substituted into the non-homogeneous terms of the circle equation."
            },
            {
                "step": "Step 2: Homogenize the Circle Equation to Degree 2",
                "math": r"x^2 + y^2 - (2x + 4y)\left(\frac{2x + y}{k}\right) - 4\left(\frac{2x + y}{k}\right)^2 = 0 \\ k^2(x^2 + y^2) - k(2x + 4y)(2x + y) - 4(4x^2 + 4xy + y^2) = 0 \\ = k^2(x^2 + y^2) - k(4x^2 + 10xy + 4y^2) - (16x^2 + 16xy + 4y^2) = 0",
                "explanation": "Grouping by quadratic monomials $x^2, xy, y^2$: $(k^2 - 4k - 16)x^2 - (10k + 16)xy + (k^2 - 4k - 4)y^2 = 0$."
            },
            {
                "step": "Step 3: Apply the Orthogonality Condition $A + B = 0$",
                "math": r"\text{For } OA \perp OB, \quad \text{Coeff}(x^2) + \text{Coeff}(y^2) = 0 \\ (k^2 - 4k - 16) + (k^2 - 4k - 4) = 0 \implies 2k^2 - 8k - 20 = 0 \implies k^2 - 4k - 10 = 0",
                "explanation": "Solving the quadratic equation for $k$: $k = \frac{4 \pm \sqrt{16 - 4(1)(-10)}}{2} = \frac{4 \pm \sqrt{56}}{2} = 2 \pm \sqrt{14}$."
            }
        ],
        "answer": r"\text{Joint Equation: } (k^2 - 4k - 16)x^2 - (10k + 16)xy + (k^2 - 4k - 4)y^2 = 0; \quad k = 2 \pm \sqrt{14}"
    }
]

u2_data = {
    "unitNumber": 2,
    "number": 2,
    "title": "Pairs of Straight Lines (Homogeneous & Non-Homogeneous Equations)",
    "description": "Exhaustive treatment of second-degree equations representing lines: homogeneous quadratic line pairs passing through the origin, slope formulas and reality criteria, angle between lines tan theta = 2 sqrt(h^2 - ab)/(a + b), perpendicularity (a + b = 0) and coincidence (h^2 = ab), joint equation of angle bisectors (x^2 - y^2)/(a - b) = xy/h and mutual orthogonality proof, general second-degree line pairs via the determinant condition Delta = 0, intersection points via partial derivatives, parallel line distances, and the homogenization theorem.",
    "sections": u2_sections,
    "problems": u2_problems
}

# -------------------------------------------------------------
# UNIT 3
# -------------------------------------------------------------
u3_sections = [
    {
        "id": "u3-sec1",
        "title": "Standard, General & Diametric Equations of the Circle",
        "content": r"""
<h3>1. The Locus Definition & General Form</h3>
<p>
A circle is the planar locus of a point $P(x, y)$ that moves such that its Euclidean distance from a fixed center $C(x_0, y_0)$ remains constant and equal to radius $R > 0$:
$$(x - x_0)^2 + (y - y_0)^2 = R^2$$
Expanding this central equation yields the general second-degree equation of a circle:
$$x^2 + y^2 + 2gx + 2fy + c = 0$$
Completing the squares:
$$(x + g)^2 + (y + f)^2 = g^2 + f^2 - c$$
Comparing with the standard form:
$$\mathbf{Center:} \; C(-g, -f), \qquad \mathbf{Radius:} \; R = \sqrt{g^2 + f^2 - c}$$
Classification based on $g^2 + f^2 - c$:
<ul>
  <li><strong>Real Circle ($g^2 + f^2 > c$):</strong> A non-degenerate circle with positive real radius.</li>
  <li><strong>Point Circle ($g^2 + f^2 = c$):</strong> The radius is zero; the locus degenerates to the single point $(-g, -f)$.</li>
  <li><strong>Imaginary / Virtual Circle ($g^2 + f^2 < c$):</strong> No real coordinates satisfy the equation.</li>
</ul>
</p>

<h3>2. Circle on a Given Diameter</h3>
<p>
Let $A(x_1, y_1)$ and $B(x_2, y_2)$ be the endpoints of a diameter. For any point $P(x, y)$ on the circle (other than $A$ or $B$), the inscribed angle $\angle APB = \pi/2$ by Thales' theorem. Hence $\vec{PA} \cdot \vec{PB} = 0$:
$$(x - x_1)(x - x_2) + (y - y_1)(y - y_2) = 0$$
This is the celebrated diametric form of a circle!
</p>
"""
    },
    {
        "id": "u3-sec2",
        "title": "Tangents, Normals & Length of Tangents",
        "content": r"""
<h3>1. Equation of Tangent and Normal at a Point</h3>
<p>
For the general circle $S \equiv x^2 + y^2 + 2gx + 2fy + c = 0$, the equation of the tangent at point $P(x_1, y_1)$ on the circle is obtained by the rule of transformation $x^2 \to x x_1, y^2 \to y y_1, 2x \to x + x_1, 2y \to y + y_1$:
$$T \equiv x x_1 + y y_1 + g(x + x_1) + f(y + y_1) + c = 0$$
Because the normal passes through the center $(-g, -f)$ and point $(x_1, y_1)$, its equation is:
$$\frac{x - x_1}{x_1 + g} = \frac{y - y_1}{y_1 + f} \iff (y_1 + f)(x - x_1) - (x_1 + g)(y - y_1) = 0$$
</p>

<h3>2. Tangents in Slope Form & Condition of Tangency</h3>
<p>
For the central circle $x^2 + y^2 = R^2$, a straight line $y = mx + k$ is tangent to the circle if and only if the perpendicular distance from the center $(0, 0)$ to the line equals the radius:
$$\frac{|k|}{\sqrt{1 + m^2}} = R \iff k = \pm R \sqrt{1 + m^2}$$
Thus the two parallel tangents with slope $m$ are:
$$y = mx \pm R \sqrt{1 + m^2}$$
</p>

<h3>3. Length of Tangents & Pair of Tangents</h3>
<p>
The length $L$ of the tangent drawn from an external point $P(x_1, y_1)$ to the circle $S = 0$ is:
$$L = \sqrt{S_1} = \sqrt{x_1^2 + y_1^2 + 2gx_1 + 2fy_1 + c}$$
The combined joint equation of the pair of tangents drawn from $P(x_1, y_1)$ to the circle is given by the elegant Joachimsthal relation:
$$S S_1 = T^2$$
where $S = x^2 + y^2 + 2gx + 2fy + c$, $S_1 = x_1^2 + y_1^2 + 2gx_1 + 2fy_1 + c$, and $T = xx_1 + yy_1 + g(x+x_1) + f(y+y_1) + c$.
</p>
"""
    },
    {
        "id": "u3-sec3",
        "title": "Chord of Contact, Pole and Polar Theory",
        "content": r"""
<h3>1. Chord of Contact</h3>
<p>
If two tangents are drawn from an external point $P(x_1, y_1)$ touching the circle at $Q$ and $R$, the line segment connecting the points of tangency is the <strong>chord of contact</strong>. Its equation is identically:
$$T \equiv x x_1 + y y_1 + g(x + x_1) + f(y + y_1) + c = 0$$
</p>

<h3>2. Pole and Polar Theory</h3>
<p>
Let $P(x_1, y_1)$ be any point (internal, external, or on the circle). If a variable secant line through $P$ intersects the circle at $A$ and $B$, the locus of the intersection of the tangents drawn at $A$ and $B$ is a straight line termed the <strong>polar</strong> of $P$ with respect to the circle. Point $P$ is called the <strong>pole</strong> of this line.
The equation of the polar of point $P(x_1, y_1)$ is:
$$T \equiv x x_1 + y y_1 + g(x + x_1) + f(y + y_1) + c = 0$$
</p>
<p>
<strong>Key Properties of Polars:</strong>
<ul>
  <li>If $P$ lies outside the circle, the polar is the chord of contact of tangents from $P$.</li>
  <li>If $P$ lies on the circle, the polar is the tangent line at $P$.</li>
  <li>If $P$ lies inside the circle, the polar lies entirely outside the circle.</li>
  <li><strong>Reciprocal Property:</strong> If the polar of point $P$ passes through point $Q$, then the polar of point $Q$ passes through point $P$. Such points $P$ and $Q$ are termed <em>conjugate points</em>.</li>
</ul>
</p>
"""
    },
    {
        "id": "u3-sec4",
        "title": "Radical Axis, Radical Center & Orthogonal Circles",
        "content": r"""
<h3>1. The Radical Axis</h3>
<p>
The <strong>radical axis</strong> of two non-concentric circles $S_1 \equiv x^2 + y^2 + 2g_1 x + 2f_1 y + c_1 = 0$ and $S_2 \equiv x^2 + y^2 + 2g_2 x + 2f_2 y + c_2 = 0$ is the planar locus of points from which the lengths of tangents drawn to both circles are equal:
$$L_1^2 = L_2^2 \iff S_1 - S_2 = 0$$
Subtracting the two equations eliminates the quadratic terms $x^2 + y^2$, yielding a linear equation:
$$2(g_1 - g_2)x + 2(f_1 - f_2)y + (c_1 - c_2) = 0$$
<strong>Geometric Theorem:</strong> The radical axis is always perpendicular to the line joining the centers $C_1(-g_1, -f_1)$ and $C_2(-g_2, -f_2)$ of the two circles!
</p>

<h3>2. The Radical Center</h3>
<p>
For three circles $S_1 = 0, S_2 = 0, S_3 = 0$ whose centers are non-collinear, the three radical axes taken in pairs:
$$S_1 - S_2 = 0, \qquad S_2 - S_3 = 0, \qquad S_3 - S_1 = 0$$
are concurrent at a unique point termed the <strong>radical center</strong>. The lengths of tangents drawn from the radical center to all three circles are equal, so it is the center of a circle orthogonal to all three circles!
</p>

<h3>3. Orthogonal Circles Condition</h3>
<p>
Two circles intersect orthogonally if their tangents at the points of intersection are perpendicular. By the Pythagorean theorem on the triangle formed by the two centers and a point of intersection:
$$C_1 C_2^2 = R_1^2 + R_2^2 \iff (g_1 - g_2)^2 + (f_1 - f_2)^2 = (g_1^2 + f_1^2 - c_1) + (g_2^2 + f_2^2 - c_2)$$
Expanding and simplifying establishes the condition of orthogonality:
$$2 g_1 g_2 + 2 f_1 f_2 = c_1 + c_2$$
</p>
"""
    },
    {
        "id": "u3-sec5",
        "title": "Coaxial Systems of Circles & Limiting Points",
        "content": r"""
<h3>1. Coaxial Systems of Circles</h3>
<p>
A system of circles is said to be <strong>coaxial</strong> if every pair of circles in the system possesses the same common radical axis.
If $S_1 = 0$ and $S_2 = 0$ are two members of the system, any circle in the coaxial family is given by:
$$S_1 + \lambda S_2 = 0 \quad (\lambda \ne -1), \qquad \text{or} \quad S_1 + \mu(S_1 - S_2) = 0$$
By choosing the common radical axis as the $y$-axis ($x = 0$) and the line of centers as the $x$-axis ($y = 0$), the simplest canonical form of a coaxial system is:
$$x^2 + y^2 + 2 k x + c = 0$$
where $c$ is a constant for the entire family and $k$ is a variable parameter identifying individual circles.
The center is $(-k, 0)$ and radius is $R = \sqrt{k^2 - c}$.
</p>

<h3>2. Limiting Points</h3>
<p>
The <strong>limiting points</strong> of a coaxial system are the centers of the circles in the system whose radii vanish identically ($R = 0$):
$$R^2 = k^2 - c = 0 \iff k = \pm \sqrt{c}$$
Thus, if $c > 0$, there exist two real limiting points:
$$L_1(\sqrt{c}, 0), \qquad L_2(-\sqrt{c}, 0)$$
These limiting points are point-circles belonging to the coaxial system. Every circle of the system is orthogonal to any circle passing through the two limiting points!
</p>
""",
        "simulation": "geom2d-circle-radical-sim",
        "simulations": ["geom2d-circle-radical-sim"]
    }
]

u3_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Circle Passing Through Three Points and Tangent at a Given Point",
        "statement": r"Find the equation of the circle passing through the points $(0, 0)$, $(4, 0)$, and $(0, 6)$. Determine its center, radius, and the equation of the tangent line at the origin $(0, 0)$.",
        "steps": [
            {
                "step": "Step 1: Determine Circle Equation",
                "math": r"x^2 + y^2 + 2gx + 2fy + c = 0 \\ \text{Through } (0, 0): \quad c = 0 \\ \text{Through } (4, 0): \quad 16 + 8g = 0 \implies g = -2 \\ \text{Through } (0, 6): \quad 36 + 12f = 0 \implies f = -3 \\ \text{Circle: } x^2 + y^2 - 4x - 6y = 0",
                "explanation": "Substituting the three points determines the unique values of $g, f, c$."
            },
            {
                "step": "Step 2: Find Center and Radius",
                "math": r"\text{Center: } (-g, -f) = (2, 3) \\ \text{Radius: } R = \sqrt{g^2 + f^2 - c} = \sqrt{(-2)^2 + (-3)^2 - 0} = \sqrt{4 + 9} = \sqrt{13}",
                "explanation": "The circle is centered at $(2, 3)$ with radius $\sqrt{13}$."
            },
            {
                "step": "Step 3: Tangent Line at the Origin $(0, 0)$",
                "math": r"T \equiv x(0) + y(0) - 2(x + 0) - 3(y + 0) = 0 \implies -2x - 3y = 0 \implies 2x + 3y = 0",
                "explanation": "Using the transformation rule $T = 0$ gives the tangent line $2x + 3y = 0$."
            }
        ],
        "answer": r"\text{Circle: } x^2 + y^2 - 4x - 6y = 0; \quad \text{Center: } (2, 3); \quad R = \sqrt{13}; \quad \text{Tangent at } (0, 0): 2x + 3y = 0"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Radical Axis and Condition of Orthogonality",
        "statement": r"Given two circles $S_1 \equiv x^2 + y^2 - 6x - 4y + 9 = 0$ and $S_2 \equiv x^2 + y^2 + 4x + 6y - 7 = 0$: (a) Find the equation of their radical axis. (b) Verify that the radical axis is perpendicular to the line of centers. (c) Find the value of $\lambda$ such that the circle $x^2 + y^2 + \lambda x - 2y + 5 = 0$ is orthogonal to $S_1$.",
        "steps": [
            {
                "step": "Step 1: Compute Radical Axis $S_1 - S_2 = 0$",
                "math": r"(x^2 + y^2 - 6x - 4y + 9) - (x^2 + y^2 + 4x + 6y - 7) = 0 \\ -10x - 10y + 16 = 0 \implies 5x + 5y - 8 = 0",
                "explanation": "The radical axis is $5x + 5y - 8 = 0$, having slope $m_{\text{rad}} = -5/5 = -1$."
            },
            {
                "step": "Step 2: Verify Perpendicularity to Line of Centers",
                "math": r"C_1 = (3, 2), \quad C_2 = (-2, -3) \\ m_{\text{centers}} = \frac{-3 - 2}{-2 - 3} = \frac{-5}{-5} = 1 \\ m_{\text{rad}} \times m_{\text{centers}} = (-1)(1) = -1 \implies \text{Strictly Perpendicular!}",
                "explanation": "The product of slopes is $-1$, verifying perpendicularity."
            },
            {
                "step": "Step 3: Condition of Orthogonality for $S_1$ and $S_3$",
                "math": r"S_1: g_1 = -3, f_1 = -2, c_1 = 9 \\ S_3: g_3 = \lambda/2, f_3 = -1, c_3 = 5 \\ 2 g_1 g_3 + 2 f_1 f_3 = c_1 + c_3 \implies 2(-3)\left(\frac{\lambda}{2}\right) + 2(-2)(-1) = 9 + 5 \\ -3\lambda + 4 = 14 \implies -3\lambda = 10 \implies \lambda = -\frac{10}{3}",
                "explanation": "Applying $2g_1 g_2 + 2f_1 f_2 = c_1 + c_2$ yields $\lambda = -10/3$."
            }
        ],
        "answer": r"\text{Radical Axis: } 5x + 5y - 8 = 0; \quad m_1 m_2 = -1 \implies \text{Perpendicular}; \quad \lambda = -\frac{10}{3}"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Coaxial Family Limiting Points and Orthogonal Conjugate System",
        "statement": r"A coaxial system of circles is determined by $S_1 \equiv x^2 + y^2 - 4x - 6y + 9 = 0$ and the radical axis $x - y + 1 = 0$. (a) Write the general equation of the coaxial family. (b) Find the exact coordinates of the limiting points of the system. (c) Derive the equation of the orthogonal conjugate coaxial system passing through the limiting points.",
        "steps": [
            {
                "step": "Step 1: Formulate the Coaxial System $S + \lambda L = 0$",
                "math": r"x^2 + y^2 - 4x - 6y + 9 + \lambda(x - y + 1) = 0 \\ x^2 + y^2 + (\lambda - 4)x - (\lambda + 6)y + (\lambda + 9) = 0",
                "explanation": "Here $g = \frac{\lambda - 4}{2}$, $f = -\frac{\lambda + 6}{2}$, $c = \lambda + 9$."
            },
            {
                "step": "Step 2: Find Limiting Points via $R^2 = g^2 + f^2 - c = 0$",
                "math": r"\left(\frac{\lambda - 4}{2}\right)^2 + \left(\frac{\lambda + 6}{2}\right)^2 - (\lambda + 9) = 0 \\ \frac{\lambda^2 - 8\lambda + 16 + \lambda^2 + 12\lambda + 36}{4} - (\lambda + 9) = 0 \\ \frac{2\lambda^2 + 4\lambda + 52}{4} - (\lambda + 9) = 0 \implies \frac{\lambda^2 + 2\lambda + 26}{2} - (\lambda + 9) = 0 \\ \lambda^2 + 2\lambda + 26 - 2\lambda - 18 = 0 \implies \lambda^2 + 8 = 0",
                "explanation": "Notice $\lambda^2 = -8$, meaning the limiting points are imaginary! When limiting points are imaginary, the coaxial circles intersect in real points $A, B$."
            },
            {
                "step": "Step 3: Find Real Common Points of Intersection",
                "math": r"\text{Substitute } y = x + 1 \text{ into } S_1: \quad x^2 + (x+1)^2 - 4x - 6(x+1) + 9 = 0 \\ x^2 + x^2 + 2x + 1 - 4x - 6x - 6 + 9 = 0 \implies 2x^2 - 8x + 4 = 0 \implies x^2 - 4x + 2 = 0 \\ x = 2 \pm \sqrt{2}, \quad y = 3 \pm \sqrt{2}",
                "explanation": "The common real intersection points of the intersecting coaxial family are $P_1(2 + \sqrt{2}, 3 + \sqrt{2})$ and $P_2(2 - \sqrt{2}, 3 - \sqrt{2})$. The orthogonal conjugate system has these two points as its real limiting points!"
            }
        ],
        "answer": r"\text{Coaxial System: } x^2 + y^2 + (\lambda - 4)x - (\lambda + 6)y + (\lambda + 9) = 0; \quad \text{Limiting Points: Imaginary (Intersecting family)}; \quad \text{Common Points: } (2 \pm \sqrt{2}, 3 \pm \sqrt{2})"
    }
]

u3_data = {
    "unitNumber": 3,
    "number": 3,
    "title": "The Circle: Tangents, Polars & Systems of Coaxial Circles",
    "description": "Comprehensive mathematical theory of circles: standard, general, and diametric representations; tangency conditions, slope equations, and Joachimsthal's pair of tangents SS_1 = T^2; chord of contact and reciprocal pole and polar theory; radical axis locus S_1 - S_2 = 0, perpendicularity proof, and radical centers; orthogonal circle criteria 2g_1 g_2 + 2f_1 f_2 = c_1 + c_2; and coaxial systems of circles, canonical equations, limiting points, and conjugate orthogonal families.",
    "sections": u3_sections,
    "problems": u3_problems
}

# -------------------------------------------------------------
# UNIT 4
# -------------------------------------------------------------
u4_sections = [
    {
        "id": "u4-sec1",
        "title": "General Second-Degree Equation & Discriminant Invariants",
        "content": r"""
<h3>1. The Universal Quadratic Form</h3>
<p>
The most general algebraic equation of the second degree in two variables is:
$$F(x, y) = a x^2 + 2h xy + b y^2 + 2g x + 2f y + c = 0$$
where $a, h, b, g, f, c \in \mathbb{R}$ and $(a, h, b) \ne (0, 0, 0)$.
In matrix notation, this equation can be expressed compactly using homogeneous coordinates $\mathbf{x} = (x, y, 1)^T$:
$$\mathbf{x}^T \mathbf{A} \mathbf{x} = 0, \qquad \mathbf{A} = \begin{pmatrix} a & h & g \\ h & b & f \\ g & f & c \end{pmatrix}$$
</p>

<h3>2. The Fundamental Invariants Under Rigid Euclidean Motion</h3>
<p>
Under any rigid coordinate transformation (arbitrary translation and rotation $\mathbf{x} \mapsto \mathbf{R}\mathbf{x} + \mathbf{t}$), the coefficients of the quadratic curve change, but three algebraic quantities remain <strong>strictly invariant</strong>:
<ol>
  <li><strong>First Invariant (Trace of Quadratic Part):</strong>
  $$I_1 \equiv a + b = \operatorname{tr}(\mathbf{A}_{2 \times 2})$$</li>
  <li><strong>Second Invariant (Discriminant of Quadratic Part):</strong>
  $$I_2 \equiv D \equiv ab - h^2 = \det(\mathbf{A}_{2 \times 2})$$</li>
  <li><strong>Third Invariant (Total Conic Discriminant):</strong>
  $$I_3 \equiv \Delta \equiv \det(\mathbf{A}) = \begin{vmatrix} a & h & g \\ h & b & f \\ g & f & c \end{vmatrix} = abc + 2fgh - af^2 - bg^2 - ch^2$$</li>
</ol>
Because these three quantities are coordinate invariants, they completely characterize the intrinsic geometric classification of the conic!
</p>
"""
    },
    {
        "id": "u4-sec2",
        "title": "Complete Classification Taxonomy of Conic Sections",
        "content": r"""
<h3>1. Non-Degenerate vs. Degenerate Conics</h3>
<p>
The total discriminant $\Delta = \det(\mathbf{A})$ establishes the primary topological branch:
<ul>
  <li><strong>Degenerate Conics ($\Delta = 0$):</strong> The curve factors into lines or a single point:
    <ul>
      <li>$D = ab - h^2 < 0$: Pair of intersecting real straight lines.</li>
      <li>$D = ab - h^2 = 0$: Pair of parallel or coincident straight lines ($g^2 - ac \ge 0$).</li>
      <li>$D = ab - h^2 > 0$: A single isolated point (pair of imaginary intersecting lines).</li>
    </ul>
  </li>
  <li><strong>Non-Degenerate Proper Conics ($\Delta \ne 0$):</strong> The curve represents a genuine conic section:
    <ul>
      <li><strong>Ellipse ($D = ab - h^2 > 0$):</strong>
        <ul>
          <li>Real Ellipse if $\Delta / (a + b) < 0$.</li>
          <li>Imaginary Ellipse if $\Delta / (a + b) > 0$.</li>
          <li>Circle if $a = b$ and $h = 0$.</li>
        </ul>
      </li>
      <li><strong>Parabola ($D = ab - h^2 = 0$):</strong> An open curve extending to infinity with a single axis of symmetry.</li>
      <li><strong>Hyperbola ($D = ab - h^2 < 0$):</strong> An open curve with two separate branches and two real asymptotes.
        <ul>
          <li><strong>Rectangular (Equilateral) Hyperbola</strong> if $a + b = 0$ (asymptotes at right angles).</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>
</p>
"""
    },
    {
        "id": "u4-sec3",
        "title": "Center of Central Conics & Elimination of Linear Terms",
        "content": r"""
<h3>1. Determining the Center $(\bar{x}, \bar{y})$</h3>
<p>
A conic is said to be a <strong>central conic</strong> if it possesses a center of symmetry $(\bar{x}, \bar{y})$ such that any chord passing through the center is bisected by it. This requires $D = ab - h^2 \ne 0$ (holding for all ellipses and hyperbolas).
The center is found by equating partial derivatives to zero:
$$\frac{\partial F}{\partial x} = 2(ax + hy + g) = 0 \implies ax + hy + g = 0$$
$$\frac{\partial F}{\partial y} = 2(hx + by + f) = 0 \implies hx + by + f = 0$$
Solving by Cramer's rule:
$$\bar{x} = \frac{hf - bg}{ab - h^2}, \qquad \bar{y} = \frac{gh - af}{ab - h^2}$$
</p>

<h3>2. Translating Origin to the Center</h3>
<p>
Translating the coordinate axes to the center by substituting $x = X + \bar{x}, y = Y + \bar{y}$ eliminates the linear terms ($gX, fY$). The transformed equation becomes:
$$a X^2 + 2h XY + b Y^2 + c' = 0$$
where the new constant term $c'$ is given by:
$$c' = g\bar{x} + f\bar{y} + c = \frac{\Delta}{ab - h^2} = \frac{\Delta}{D}$$
Notice the immense elegance of this result: the constant term is simply the quotient of the two fundamental invariants $\Delta / D$!
</p>
"""
    },
    {
        "id": "u4-sec4",
        "title": "Elimination of xy Cross-Term & Canonical Eigenvalue Reduction",
        "content": r"""
<h3>1. Rotational Diagonalization via Eigenvalues</h3>
<p>
To reduce the central equation $a X^2 + 2h XY + b Y^2 + c' = 0$ to principal axes, we rotate the axes through angle $\theta$ given by:
$$\tan 2\theta = \frac{2h}{a - b}$$
In matrix terms, this is equivalent to diagonalizing the symmetric matrix $\mathbf{A}_{2 \times 2} = \begin{pmatrix} a & h \\ h & b \end{pmatrix}$.
The eigenvalues $\lambda_1, \lambda_2$ are the roots of the characteristic equation:
$$\det(\lambda \mathbf{I} - \mathbf{A}_{2 \times 2}) = 0 \iff \lambda^2 - (a + b)\lambda + (ab - h^2) = 0$$
$$\lambda_1, \lambda_2 = \frac{(a + b) \pm \sqrt{(a - b)^2 + 4h^2}}{2}$$
</p>

<h3>2. The Standard Canonical Form</h3>
<p>
Referred to the principal axes $(X', Y')$, the cross term vanishes identically:
$$\lambda_1 X'^2 + \lambda_2 Y'^2 + c' = 0 \iff \frac{X'^2}{-c'/\lambda_1} + \frac{Y'^2}{-c'/\lambda_2} = 1$$
<ul>
  <li>If $\lambda_1, \lambda_2$ have the same sign (and opposite to $c'$), the curve is an <strong>ellipse</strong> with semi-axes $A = \sqrt{-c'/\lambda_1}, B = \sqrt{-c'/\lambda_2}$.</li>
  <li>If $\lambda_1, \lambda_2$ have opposite signs, the curve is a <strong>hyperbola</strong>.</li>
</ul>
</p>
"""
    },
    {
        "id": "u4-sec5",
        "title": "Non-Central Conics: The Complete Parabola Reduction Protocol",
        "content": r"""
<h3>1. The Parabola Condition ($ab - h^2 = 0$)</h3>
<p>
When $ab - h^2 = 0$, the quadratic terms form a perfect square:
$$ax^2 + 2hxy + by^2 = (\alpha x + \beta y)^2, \quad \text{where } \alpha = \sqrt{a}, \; \beta = \sqrt{b}, \; \text{and } \alpha\beta = h$$
Because $D = 0$, the conic has no finite center; it is a <strong>non-central conic (parabola)</strong>.
</p>

<h3>2. The Systematic Reduction Algorithm</h3>
<p>
To reduce the parabola to canonical form $Y'^2 = 4AX'$:
<ol>
  <li>Group the perfect square: $(\alpha x + \beta y)^2 = -2gx - 2fy - c$.</li>
  <li>Introduce an arbitrary parameter $\lambda$:
  $$(\alpha x + \beta y + \lambda)^2 = 2(\lambda \alpha - g)x + 2(\lambda \beta - f)y + (\lambda^2 - c)$$</li>
  <li>Choose $\lambda$ so that the lines $\alpha x + \beta y + \lambda = 0$ (axis of the parabola) and $2(\lambda \alpha - g)x + 2(\lambda \beta - f)y + (\lambda^2 - c) = 0$ (tangent at vertex) are strictly perpendicular:
  $$\alpha \cdot 2(\lambda \alpha - g) + \beta \cdot 2(\lambda \beta - f) = 0 \implies \lambda(\alpha^2 + \beta^2) = \alpha g + \beta f \implies \lambda = \frac{\alpha g + \beta f}{a + b}$$</li>
  <li>Divide each side by $\sqrt{\alpha^2 + \beta^2}$ and $\sqrt{4(\lambda\alpha - g)^2 + 4(\lambda\beta - f)^2}$ respectively to obtain normalized perpendicular distances, reducing immediately to the canonical form $Y'^2 = 4AX'$!</li>
</ol>
</p>
""",
        "simulation": "geom2d-conic-discriminant-sim",
        "simulations": ["geom2d-conic-discriminant-sim"]
    }
]

u4_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Conic Identification and Invariant Computation",
        "statement": r"Classify each of the following second-degree equations by computing their discriminant invariants $\Delta$ and $D = ab - h^2$: (a) $x^2 - 4xy + 4y^2 - 2x + 4y - 3 = 0$. (b) $5x^2 + 4xy + 2y^2 - 12x - 6y + 11 = 0$. (c) $x^2 + 4xy + y^2 - 6x - 6y + 5 = 0$.",
        "steps": [
            {
                "step": "Step 1: Analyze Equation (a)",
                "math": r"a = 1, h = -2, b = 4, g = -1, f = 2, c = -3 \\ D = ab - h^2 = 1(4) - (-2)^2 = 4 - 4 = 0 \\ \Delta = \begin{vmatrix} 1 & -2 & -1 \\ -2 & 4 & 2 \\ -1 & 2 & -3 \end{vmatrix} = 1(-12 - 4) - (-2)(6 - (-2)) - 1(-4 - (-4)) = -16 + 16 - 0 = 0",
                "explanation": "Since $\Delta = 0$ and $D = 0$, this represents a degenerate pair of parallel straight lines ($(x - 2y - 3)(x - 2y + 1) = 0$)."
            },
            {
                "step": "Step 2: Analyze Equation (b)",
                "math": r"a = 5, h = 2, b = 2, g = -6, f = -3, c = 11 \\ D = ab - h^2 = 5(2) - 2^2 = 10 - 4 = 6 > 0 \\ \Delta = 5(22 - 9) - 2(22 - 18) - 6(-6 - 12) = 5(13) - 2(4) - 6(-18) \ne 0",
                "explanation": "Since $\Delta \ne 0$ and $D > 0$, equation (b) represents a non-degenerate real Ellipse."
            },
            {
                "step": "Step 3: Analyze Equation (c)",
                "math": r"a = 1, h = 2, b = 1, g = -3, f = -3, c = 5 \\ D = ab - h^2 = 1(1) - 2^2 = 1 - 4 = -3 < 0 \\ \Delta = 1(5 - 9) - 2(10 - 9) - 3(-6 - 3) = -4 - 2 + 27 = 21 \ne 0",
                "explanation": "Since $\Delta \ne 0$ and $D < 0$, equation (c) represents a non-degenerate Hyperbola."
            }
        ],
        "answer": r"\text{(a) Degenerate parallel lines } (\Delta = 0, D = 0); \quad \text{(b) Ellipse } (\Delta \ne 0, D > 0); \quad \text{(c) Hyperbola } (\Delta \ne 0, D < 0)"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Complete Canonical Reduction and Tracing of a Central Ellipse",
        "statement": r"Given the second-degree equation $5x^2 - 4xy + 8y^2 - 36 = 0$: (a) Verify that the conic is an ellipse centered at the origin. (b) Find the characteristic equation and eigenvalues $\lambda_1, \lambda_2$. (c) Determine the canonical form, length of major and minor semi-axes, and eccentricity.",
        "steps": [
            {
                "step": "Step 1: Verify Center and Conic Type",
                "math": r"a = 5, \; h = -2, \; b = 8, \; g = 0, \; f = 0, \; c = -36 \\ D = ab - h^2 = 5(8) - (-2)^2 = 40 - 4 = 36 > 0 \\ \Delta = c(ab - h^2) = -36(36) = -1296 \ne 0",
                "explanation": "Since $g = f = 0$, the center is already at $(0, 0)$. Because $\Delta \ne 0$ and $D > 0$, it is a central ellipse."
            },
            {
                "step": "Step 2: Characteristic Equation and Eigenvalues",
                "math": r"\lambda^2 - (a+b)\lambda + (ab-h^2) = 0 \implies \lambda^2 - 13\lambda + 36 = 0 \implies (\lambda - 4)(\lambda - 9) = 0 \\ \lambda_1 = 4, \qquad \lambda_2 = 9",
                "explanation": "The eigenvalues are $\lambda_1 = 4$ and $\lambda_2 = 9$."
            },
            {
                "step": "Step 3: Canonical Equation and Semi-Axes",
                "math": r"\lambda_1 X^2 + \lambda_2 Y^2 + c = 0 \implies 4X^2 + 9Y^2 = 36 \implies \frac{X^2}{9} + \frac{Y^2}{4} = 1 \\ \text{Major semi-axis: } A = \sqrt{9} = 3, \qquad \text{Minor semi-axis: } B = \sqrt{4} = 2 \\ \text{Eccentricity: } e = \sqrt{1 - \frac{B^2}{A^2}} = \sqrt{1 - \frac{4}{9}} = \frac{\sqrt{5}}{3}",
                "explanation": "The rotation angle satisfies $\tan 2\theta = \frac{2h}{a-b} = \frac{-4}{5-8} = \frac{4}{3} \implies \theta = \frac{1}{2}\arctan(4/3) \approx 26.57^\circ$."
            }
        ],
        "answer": r"\text{Canonical Form: } \frac{X^2}{9} + \frac{Y^2}{4} = 1; \quad A = 3, \; B = 2; \quad e = \frac{\sqrt{5}}{3} \approx 0.745; \quad \theta \approx 26.57^\circ"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Complete Parabolic Reduction Protocol for a Non-Central Conic",
        "statement": r"Reduce the non-central second-degree equation $(x + 2y)^2 - 4x + 2y - 5 = 0 \iff x^2 + 4xy + 4y^2 - 4x + 2y - 5 = 0$ to canonical form $Y'^2 = 4AX'$. Determine the vertex, focus, axis equation, tangent at vertex, and latus rectum.",
        "steps": [
            {
                "step": "Step 1: Parameterize the Perfect Square",
                "math": r"(x + 2y + \lambda)^2 = (x + 2y)^2 + 2\lambda(x + 2y) + \lambda^2 \\ = (4x - 2y + 5) + 2\lambda x + 4\lambda y + \lambda^2 = (2\lambda + 4)x + (4\lambda - 2)y + (\lambda^2 + 5)",
                "explanation": "We rewrite $(x + 2y + \lambda)^2 = (2\lambda + 4)x + (4\lambda - 2)y + (\lambda^2 + 5)$."
            },
            {
                "step": "Step 2: Determine $\lambda$ to Ensure Orthogonality",
                "math": r"\text{Line 1: } x + 2y + \lambda = 0 \quad (\mathbf{n}_1 = (1, 2)) \\ \text{Line 2: } (2\lambda + 4)x + (4\lambda - 2)y + (\lambda^2 + 5) = 0 \quad (\mathbf{n}_2 = (2\lambda + 4, 4\lambda - 2)) \\ \mathbf{n}_1 \cdot \mathbf{n}_2 = 1(2\lambda + 4) + 2(4\lambda - 2) = 2\lambda + 4 + 8\lambda - 4 = 10\lambda = 0 \implies \lambda = 0",
                "explanation": "Remarkably, $\lambda = 0$ satisfies the orthogonality condition!"
            },
            {
                "step": "Step 3: Normalize to Standard Distance Coordinates",
                "math": r"\lambda = 0 \implies (x + 2y)^2 = 4x - 2y + 5 \\ \left(\frac{x + 2y}{\sqrt{1^2 + 2^2}}\right)^2 = \frac{4x - 2y + 5}{5} = \frac{\sqrt{4^2 + (-2)^2}}{5} \left(\frac{4x - 2y + 5}{\sqrt{20}}\right) = \frac{\sqrt{20}}{5} Y' = \frac{2\sqrt{5}}{5} Y' = \frac{2}{\sqrt{5}} X'",
                "explanation": "Let $Y' = \frac{x + 2y}{\sqrt{5}}$ and $X' = \frac{4x - 2y + 5}{\sqrt{20}} = \frac{4x - 2y + 5}{2\sqrt{5}}$. Then $Y'^2 = \frac{2}{\sqrt{5}} X' = 4 \left(\frac{1}{2\sqrt{5}}\right) X'$."
            },
            {
                "step": "Step 4: Extract Geometric Elements",
                "math": r"\text{Axis: } x + 2y = 0 \\ \text{Tangent at Vertex: } 4x - 2y + 5 = 0 \\ \text{Vertex: Intersection of Axis and Tangent: } x = -2y \implies 4(-2y) - 2y + 5 = 0 \implies -10y = -5 \implies y = \frac{1}{2}, \; x = -1 \\ \text{Latus Rectum: } 4A = \frac{2}{\sqrt{5}}",
                "explanation": "The canonical equation is $Y'^2 = \frac{2}{\sqrt{5}}X'$, centered at vertex $(-1, 1/2)$."
            }
        ],
        "answer": r"\text{Canonical Form: } Y'^2 = \frac{2}{\sqrt{5}}X'; \quad \text{Vertex: } \left(-1, \frac{1}{2}\right); \quad \text{Axis: } x + 2y = 0; \quad \text{Latus Rectum: } \frac{2}{\sqrt{5}}"
    }
]

u4_data = {
    "unitNumber": 4,
    "number": 4,
    "title": "General Second-Degree Equation & Classification of Conic Sections",
    "description": "Comprehensive theory of general quadratic equations: universal matrix formulation x^T A x = 0; rigid motion invariants trace I_1 = a + b, discriminant I_2 = ab - h^2, and total determinant I_3 = Delta; complete classification taxonomy for proper conics (ellipse, parabola, hyperbola) and degenerate varieties; center determination via partial derivatives and elimination of linear terms; rotational diagonalization and eigenvalue canonical reduction lambda_1 X^2 + lambda_2 Y^2 + Delta/D = 0; and the complete reduction protocol for non-central parabolas Y'^2 = 4AX'.",
    "sections": u4_sections,
    "problems": u4_problems
}

# -------------------------------------------------------------
# WRITE OUT JSON FILES
# -------------------------------------------------------------
for i, data in enumerate([u1_data, u2_data, u3_data, u4_data], 1):
    fn = f"geom2d_u{i}.json"
    with open(fn, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"{fn} created successfully!")
