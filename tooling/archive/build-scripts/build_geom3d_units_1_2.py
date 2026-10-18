import json

print("Building 3D Geometry: Units 1 & 2...")

# ==========================================
# UNIT 1: 3D COORDINATE SYSTEMS, DIRECTION COSINES & PROJECTIONS
# ==========================================
u1_sections = [
    {
        "id": "u1-sec1",
        "title": "3D Coordinate Systems: Cartesian, Cylindrical & Spherical Frames",
        "content": r"""<h4>1. The Right-Handed Cartesian Frame $\mathbb{R}^3$</h4>
<p>In three-dimensional Euclidean space $\mathbb{R}^3$, three mutually perpendicular oriented lines intersecting at a common origin $O(0, 0, 0)$ define the coordinate axes: the $x$-axis, $y$-axis, and $z$-axis. By standard convention, these axes satisfy the <strong>Right-Hand Rule</strong>: rotating the positive $x$-axis into the positive $y$-axis through $\pi/2$ advances a right-handed screw along the positive $z$-axis ($\hat{i} \times \hat{j} = \hat{k}$).</p>
<p>The three coordinate planes partition space into <strong>eight octants</strong>:</p>
<div class="math-display">
$$\begin{aligned}
xy\text{-plane: } & z = 0 \\
yz\text{-plane: } & x = 0 \\
zx\text{-plane: } & y = 0
\end{aligned}$$
</div>
<p>Any point $P \in \mathbb{R}^3$ is uniquely identified by the ordered triplet of signed perpendicular distances $(x, y, z)$.</p>

<h4>2. Cylindrical Coordinates $(\rho, \phi, z)$</h4>
<p>Cylindrical coordinates combine 2D polar coordinates in the $xy$-plane with the Cartesian altitude $z$:</p>
<div class="math-display">
$$x = \rho \cos\phi, \qquad y = \rho \sin\phi, \qquad z = z$$
</div>
<p>where $\rho = \sqrt{x^2 + y^2} \ge 0$ is the radial distance from the $z$-axis, and $\phi \in [0, 2\pi)$ is the azimuthal angle measured counterclockwise from the positive $x$-axis. The differential volume element is:</p>
<div class="math-display">
$$dV = \rho \, d\rho \, d\phi \, dz$$
</div>

<h4>3. Spherical Polar Coordinates $(r, \theta, \phi)$</h4>
<p>Spherical coordinates specify the Euclidean distance $r$ from the origin, the polar/colatitude angle $\theta$ from the positive $z$-axis, and the azimuthal angle $\phi$ in the $xy$-plane:</p>
<div class="math-display">
$$\begin{aligned}
x &= r \sin\theta \cos\phi \\
y &= r \sin\theta \sin\phi \\
z &= r \cos\theta
\end{aligned} \quad \Longleftrightarrow \quad \begin{aligned}
r &= \sqrt{x^2 + y^2 + z^2} \ge 0 \\
\theta &= \arccos(z / r) \in [0, \pi] \\
\phi &= \operatorname{atan2}(y, x) \in [0, 2\pi)
\end{aligned}$$
</div>
<p>The Jacobian determinant of this transformation yields the spherical volume element:</p>
<div class="math-display">
$$J = \frac{\partial(x, y, z)}{\partial(r, \theta, \phi)} = r^2 \sin\theta \implies \mathbf{dV = r^2 \sin\theta \, dr \, d\theta \, d\phi}$$
</div>"""
    },
    {
        "id": "u1-sec2",
        "title": "Euclidean Distance, Section Formulas & Spatial Centroids",
        "content": r"""<h4>1. Euclidean Distance Metric in $\mathbb{R}^3$</h4>
<p>Let $P_1(x_1, y_1, z_1)$ and $P_2(x_2, y_2, z_2)$ be two distinct points in space. By double application of the Pythagorean theorem across the rectangular box having $P_1 P_2$ as main spatial diagonal:</p>
<div class="math-display">
$$d(P_1, P_2) = \|\vec{r}_2 - \vec{r}_1\| = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$
</div>

<h4>2. Section Formulas (Internal & External Division)</h4>
<p>Let $P(x, y, z)$ divide the line segment joining $P_1(x_1, y_1, z_1)$ and $P_2(x_2, y_2, z_2)$ in the ratio $m : n$:</p>
<ul>
  <li><strong>Internal Division ($m : n > 0$):</strong>
    $$\mathbf{P = \left( \frac{m x_2 + n x_1}{m + n}, \, \frac{m y_2 + n y_1}{m + n}, \, \frac{m z_2 + n z_1}{m + n} \right)}$$
  </li>
  <li><strong>External Division ($m : -n$):</strong>
    $$\mathbf{P = \left( \frac{m x_2 - n x_1}{m - n}, \, \frac{m y_2 - n y_1}{m - n}, \, \frac{m z_2 - n z_1}{m - n} \right)} \quad (m \ne n)$$
  </li>
</ul>

<h4>3. Centroids of Spatial Polygons and Polyhedra</h4>
<ul>
  <li><strong>Triangle Centroid:</strong> For vertices $A, B, C$, the centroid $G$ is the concurrency point of the three medians:
    $$G = \left( \frac{x_A + x_B + x_C}{3}, \, \frac{y_A + y_B + y_C}{3}, \, \frac{z_A + z_B + z_C}{3} \right)$$
  </li>
  <li><strong>Tetrahedron Centroid:</strong> For vertices $A, B, C, D$, the centroid $G$ divides each line segment joining a vertex to the centroid of the opposite face in the ratio $3 : 1$:
    $$G = \left( \frac{x_A + x_B + x_C + x_D}{4}, \, \frac{y_A + y_B + y_C + y_D}{4}, \, \frac{z_A + z_B + z_C + z_D}{4} \right)$$
  </li>
</ul>"""
    },
    {
        "id": "u1-sec3",
        "title": "Direction Angles, Direction Cosines & The Fundamental Pythagorean Identity",
        "content": r"""<h4>1. Direction Angles and Direction Cosines</h4>
<p>Let an oriented ray $L$ pass through the origin $O$ in direction of unit vector $\hat{u}$. Let $\alpha, \beta, \gamma \in [0, \pi]$ be the positive inclination angles made by $L$ with the positive $x$, $y$, and $z$ axes respectively. These are the <strong>direction angles</strong> of $L$.</p>
<p>Their cosines are called the <strong>Direction Cosines (DCs)</strong>, conventionally denoted by $(l, m, n)$:</p>
<div class="math-display">
$$l = \cos\alpha, \qquad m = \cos\beta, \qquad n = \cos\gamma$$
</div>

<h4>2. Rigorous Proof of the Fundamental Identity: $l^2 + m^2 + n^2 = 1$</h4>
<p>Let $P(x, y, z)$ be a point on line $L$ at distance $r = \sqrt{x^2 + y^2 + z^2} > 0$ from origin $O$. Projecting $P$ orthogonally onto the coordinate axes:</p>
<div class="math-display">
$$x = r \cos\alpha = r l, \qquad y = r \cos\beta = r m, \qquad z = r \cos\gamma = r n$$
</div>
<p>Squaring and adding these three projection relations:</p>
<div class="math-display">
$$x^2 + y^2 + z^2 = r^2 l^2 + r^2 m^2 + r^2 n^2 = r^2 (l^2 + m^2 + n^2)$$
</div>
<p>Since $x^2 + y^2 + z^2 = r^2$, dividing both sides by $r^2 \ne 0$ establishes:</p>
<div class="math-display">
$$\mathbf{l^2 + m^2 + n^2 = \cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1} \quad \blacksquare$$
</div>
<p>Consequently, the unit direction vector along the line is identically $\hat{u} = l\hat{i} + m\hat{j} + n\hat{k}$.</p>

<h4>3. Direction Ratios (DRs) & Normalization</h4>
<p>Any three real numbers $(a, b, c)$ proportional to the direction cosines $(l, m, n)$ are called <strong>Direction Ratios (DRs)</strong>:</p>
<div class="math-display">
$$\frac{l}{a} = \frac{m}{b} = \frac{n}{c} = k \implies l = ka, \quad m = kb, \quad n = kc$$
</div>
<p>Substituting into $l^2 + m^2 + n^2 = 1$:</p>
<div class="math-display">
$$k^2 (a^2 + b^2 + c^2) = 1 \implies k = \frac{\pm 1}{\sqrt{a^2 + b^2 + c^2}}$$
</div>
<div class="math-display">
$$\mathbf{l = \frac{a}{\pm\sqrt{a^2 + b^2 + c^2}}, \qquad m = \frac{b}{\pm\sqrt{a^2 + b^2 + c^2}}, \qquad n = \frac{c}{\pm\sqrt{a^2 + b^2 + c^2}}}$$
</div>"""
    },
    {
        "id": "u1-sec4",
        "title": "Projections of Line Segments onto Oriented Lines & Planes",
        "content": r"""<h4>1. Projection of a Line Segment onto an Oriented Line</h4>
<p>Let $AB$ be a directed line segment with initial point $A(x_1, y_1, z_1)$ and terminal point $B(x_2, y_2, z_2)$. Let $L$ be an oriented line with direction cosines $(l, m, n)$.</p>
<p>The vector displacement is $\vec{AB} = (x_2 - x_1)\hat{i} + (y_2 - y_1)\hat{j} + (z_2 - z_1)\hat{k}$. The <strong>orthogonal projection</strong> $p$ of $AB$ onto line $L$ is the scalar dot product with the unit direction vector $\hat{u} = l\hat{i} + m\hat{j} + n\hat{k}$:</p>
<div class="math-display">
$$\mathbf{p = \vec{AB} \cdot \hat{u} = l(x_2 - x_1) + m(y_2 - y_1) + n(z_2 - z_1)}$$
</div>

<h4>2. Length of a Line Segment in Terms of Projections</h4>
<p>Projecting segment $AB$ onto the three orthogonal coordinate axes gives projections $p_x = x_2 - x_1$, $p_y = y_2 - y_1$, and $p_z = z_2 - z_1$. The length of $AB$ is the Euclidean norm of its projections:</p>
<div class="math-display">
$$AB = \sqrt{p_x^2 + p_y^2 + p_z^2}$$
</div>
<p>Furthermore, if $p_1, p_2, p_3$ are projections of $AB$ onto any three mutually orthogonal spatial lines, then $AB^2 = p_1^2 + p_2^2 + p_3^2$.</p>"""
    },
    {
        "id": "u1-sec5",
        "title": "Angle Between Two Lines & Distance of a Point from a Line",
        "content": r"""<h4>1. Angle Between Two Lines</h4>
<p>Let $L_1$ and $L_2$ be two lines with direction cosines $(l_1, m_1, n_1)$ and $(l_2, m_2, n_2)$ and unit vectors $\hat{u}_1, \hat{u}_2$. The angle $\theta \in [0, \pi]$ between them is given by:</p>
<div class="math-display">
$$\cos\theta = \hat{u}_1 \cdot \hat{u}_2 = l_1 l_2 + m_1 m_2 + n_1 n_2$$
</div>
<p>Using Lagrange's trigonometric identity, $\sin^2\theta = 1 - \cos^2\theta = (l_1^2 + m_1^2 + n_1^2)(l_2^2 + m_2^2 + n_2^2) - (l_1 l_2 + m_1 m_2 + n_1 n_2)^2$:</p>
<div class="math-display">
$$\sin\theta = \sqrt{(m_1 n_2 - m_2 n_1)^2 + (n_1 l_2 - n_2 l_1)^2 + (l_1 m_2 - l_2 m_1)^2}$$
</div>
<ul>
  <li><strong>Orthogonality Criterion ($L_1 \perp L_2$):</strong>
    $$\mathbf{l_1 l_2 + m_1 m_2 + n_1 n_2 = 0 \quad \Longleftrightarrow \quad a_1 a_2 + b_1 b_2 + c_1 c_2 = 0}$$
  </li>
  <li><strong>Parallelism Criterion ($L_1 \parallel L_2$):</strong>
    $$\mathbf{\frac{l_1}{l_2} = \frac{m_1}{m_2} = \frac{n_1}{n_2} \quad \Longleftrightarrow \quad \frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}}$$
  </li>
</ul>

<h4>2. Perpendicular Distance of a Point from a Line</h4>
<p>Let $P(x_1, y_1, z_1)$ be a point in space, and let line $L$ pass through $A(x_0, y_0, z_0)$ with direction cosines $(l, m, n)$. Let $M$ be the foot of the perpendicular from $P$ onto $L$. In right triangle $\triangle APM$:</p>
<div class="math-display">
$$AM = \text{proj}_L \vec{AP} = l(x_1 - x_0) + m(y_1 - y_0) + n(z_1 - z_0)$$
</div>
<div class="math-display">
$$AP^2 = (x_1 - x_0)^2 + (y_1 - y_0)^2 + (z_1 - z_0)^2$$
</div>
<div class="math-display">
$$\mathbf{d = PM = \sqrt{AP^2 - AM^2} = \frac{\|\vec{AP} \times \vec{d}\|}{\|\vec{d}\|}}$$
</div>"""
    }
]

u1_problems = [
    {
        "id": "geom3d-p1-1",
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Direction Cosines & Acute Angle Between Lines",
        "statement": r"""Two lines $L_1$ and $L_2$ have direction ratios proportional to $(2, 3, 6)$ and $(1, 2, 2)$ respectively.
(a) Find the normalized direction cosines for both lines.
(b) Find the acute angle $\theta$ between $L_1$ and $L_2$.""",
        "solution": r"""<h4>Part (a): Normalizing Direction Cosines</h4>
<p>For line $L_1$ with direction ratios $(a_1, b_1, c_1) = (2, 3, 6)$:</p>
<div class="math-display">
$$\sqrt{a_1^2 + b_1^2 + c_1^2} = \sqrt{2^2 + 3^2 + 6^2} = \sqrt{4 + 9 + 36} = \sqrt{49} = 7$$
</div>
<div class="math-display">
$$(l_1, m_1, n_1) = \left( \frac{2}{7}, \, \frac{3}{7}, \, \frac{6}{7} \right)$$
</div>
<p>For line $L_2$ with direction ratios $(a_2, b_2, c_2) = (1, 2, 2)$:</p>
<div class="math-display">
$$\sqrt{a_2^2 + b_2^2 + c_2^2} = \sqrt{1^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3$$
</div>
<div class="math-display">
$$(l_2, m_2, n_2) = \left( \frac{1}{3}, \, \frac{2}{3}, \, \frac{2}{3} \right)$$
</div>

<h4>Part (b): Angle Between the Lines</h4>
<div class="math-display">
$$\cos\theta = l_1 l_2 + m_1 m_2 + n_1 n_2 = \left(\frac{2}{7}\right)\left(\frac{1}{3}\right) + \left(\frac{3}{7}\right)\left(\frac{2}{3}\right) + \left(\frac{6}{7}\right)\left(\frac{2}{3}\right)$$
</div>
<div class="math-display">
$$\cos\theta = \frac{2 + 6 + 12}{21} = \frac{20}{21}$$
</div>
<p>The acute angle is:</p>
<div class="math-display">
$$\mathbf{\theta = \arccos\left(\frac{20}{21}\right) \approx 17.75^\circ}$$
</div>""",
        "answer": r"""$(l_1, m_1, n_1) = (2/7, 3/7, 6/7)$; $(l_2, m_2, n_2) = (1/3, 2/3, 2/3)$; $\theta = \arccos(20/21) \approx 17.75^\circ$."""
    },
    {
        "id": "geom3d-p1-2",
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Foot of the Perpendicular & Point-Line Distance",
        "statement": r"""Find the coordinates of the foot of the perpendicular $M$ and the perpendicular distance from point $P(1, 2, 3)$ to the line passing through $A(2, 1, 0)$ and $B(0, 3, 2)$.""",
        "solution": r"""<h4>Step 1: Parametrize the Line $AB$</h4>
<p>The vector displacement $\vec{AB} = (0 - 2)\hat{i} + (3 - 1)\hat{j} + (2 - 0)\hat{k} = -2\hat{i} + 2\hat{j} + 2\hat{k}$.</p>
<p>Direction ratios of the line are proportional to $(-1, 1, 1)$.</p>
<p>Parametric coordinates of any point $M$ on line $AB$ in terms of parameter $\lambda$ are:</p>
<div class="math-display">
$$M(\lambda) = (2 - \lambda, \, 1 + \lambda, \, \lambda)$$
</div>

<h4>Step 2: Enforce Orthogonality Condition</h4>
<p>The vector $\vec{PM}$ connecting $P(1, 2, 3)$ to $M$ is:</p>
<div class="math-display">
$$\vec{PM} = ((2 - \lambda) - 1)\hat{i} + ((1 + \lambda) - 2)\hat{j} + (\lambda - 3)\hat{k} = (1 - \lambda)\hat{i} + (\lambda - 1)\hat{j} + (\lambda - 3)\hat{k}$$
</div>
<p>For $PM \perp AB$, the dot product of $\vec{PM}$ with the direction vector $(-1, 1, 1)$ must vanish:</p>
<div class="math-display">
$$-1(1 - \lambda) + 1(\lambda - 1) + 1(\lambda - 3) = 0$$
</div>
<div class="math-display">
$$-1 + \lambda + \lambda - 1 + \lambda - 3 = 0 \implies 3\lambda - 5 = 0 \implies \lambda = \frac{5}{3}$$
</div>

<h4>Step 3: Compute the Coordinates of Foot $M$</h4>
<div class="math-display">
$$M = \left( 2 - \frac{5}{3}, \, 1 + \frac{5}{3}, \, \frac{5}{3} \right) = \mathbf{\left( \frac{1}{3}, \, \frac{8}{3}, \, \frac{5}{3} \right)}$$
</div>

<h4>Step 4: Compute the Perpendicular Distance</h4>
<div class="math-display">
$$\vec{PM} = \left(1 - \frac{5}{3}\right)\hat{i} + \left(\frac{5}{3} - 1\right)\hat{j} + \left(\frac{5}{3} - 3\right)\hat{k} = -\frac{2}{3}\hat{i} + \frac{2}{3}\hat{j} - \frac{4}{3}\hat{k}$$
</div>
<div class="math-display">
$$d = \|\vec{PM}\| = \sqrt{\left(-\frac{2}{3}\right)^2 + \left(\frac{2}{3}\right)^2 + \left(-\frac{4}{3}\right)^2} = \sqrt{\frac{4 + 4 + 16}{9}} = \sqrt{\frac{24}{9}} = \mathbf{\frac{2\sqrt{6}}{3}}$$
</div>""",
        "answer": r"""Foot $M = (1/3, 8/3, 5/3)$; Perpendicular distance $d = \frac{2\sqrt{6}}{3} \approx 1.633$."""
    },
    {
        "id": "geom3d-p1-3",
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Mutual Equiangular Rays & The Regular Tetrahedral Angle",
        "statement": r"""Let four distinct lines in $\mathbb{R}^3$ through the origin have unit direction vectors $\hat{u}_1, \hat{u}_2, \hat{u}_3, \hat{u}_4$ such that every pair of lines makes the exact same angle $\theta$ with each other ($\hat{u}_i \cdot \hat{u}_j = \cos\theta$ for all $i \ne j$).
(a) Prove that $\cos\theta = -\frac{1}{3}$.
(b) Deduce the exact value of the regular tetrahedral bond angle $\theta = \arccos(-1/3) \approx 109.47^\circ$.
(c) Prove that it is impossible to have five mutually equiangular lines in $\mathbb{R}^3$ with this symmetry.""",
        "solution": r"""<h4>Part (a): Gram Matrix and Vector Sum</h4>
<p>Consider the total vector sum $\vec{S} = \hat{u}_1 + \hat{u}_2 + \hat{u}_3 + \hat{u}_4$. By the symmetry of the configuration, the four unit vectors must be symmetrically distributed about the origin, which implies $\vec{S} = \vec{0}$.</p>
<p>Let us compute the square magnitude $\|\vec{S}\|^2 \ge 0$:</p>
<div class="math-display">
$$\|\vec{S}\|^2 = \left( \sum_{i=1}^4 \hat{u}_i \right) \cdot \left( \sum_{j=1}^4 \hat{u}_j \right) = \sum_{i=1}^4 \|\hat{u}_i\|^2 + \sum_{i \ne j} (\hat{u}_i \cdot \hat{u}_j)$$
</div>
<p>Since each $\hat{u}_i$ is a unit vector, $\|\hat{u}_i\|^2 = 1$ for all 4 vectors. There are $4 \times 3 = 12$ cross-terms $i \ne j$, each equal to $\cos\theta$:</p>
<div class="math-display">
$$\|\vec{S}\|^2 = 4(1) + 12 \cos\theta = 4 + 12\cos\theta$$
</div>
<p>Since the four lines are non-coplanar and span $\mathbb{R}^3$, the symmetric barycentric balance requires $\vec{S} = \vec{0}$:</p>
<div class="math-display">
$$4 + 12\cos\theta = 0 \implies 12\cos\theta = -4 \implies \mathbf{\cos\theta = -\frac{1}{3}} \quad \blacksquare$$
</div>

<h4>Part (b): The Regular Tetrahedral Angle</h4>
<div class="math-display">
$$\mathbf{\theta = \arccos\left(-\frac{1}{3}\right) = \pi - \arccos\left(\frac{1}{3}\right) \approx 109.4712^\circ}$$
</div>
<p>This is the fundamental bonding angle of $sp^3$-hybridized carbon atoms (e.g. methane $\text{CH}_4$, diamond lattice).</p>

<h4>Part (c): Impossibility for $k = 5$ in $\mathbb{R}^3$</h4>
<p>In $\mathbb{R}^n$, the maximum number of vectors that can satisfy $\vec{S} = \sum_{i=1}^k \hat{u}_i = \vec{0}$ with equal pairwise dot products $\cos\theta = -\frac{1}{k-1}$ is $k = n + 1$, representing the vertices of a regular $n$-simplex.</p>
<p>For $n = 3$, $k_{\max} = 3 + 1 = 4$. If there were 5 vectors in $\mathbb{R}^3$, the $5 \times 5$ Gram matrix $G_{ij} = \hat{u}_i \cdot \hat{u}_j$ would have rank at most 3 (since vectors reside in 3D). However, a $5 \times 5$ matrix with $1$ on diagonal and $\cos\theta = -1/4$ off-diagonal has eigenvalues $1 - (-1/4) = 5/4$ (multiplicity 4) and $1 + 4(-1/4) = 0$ (multiplicity 1), meaning its rank is $4 > 3$, a contradiction in $\mathbb{R}^3$.</p>""",
        "answer": r"""Proved: $\cos\theta = -1/3 \implies \theta \approx 109.47^\circ$; 5 such vectors would require $\mathbb{R}^4$."""
    }
]

u1_data = {
    "id": "unit1",
    "unit_number": 1,
    "title": "3D Coordinate Systems, Direction Cosines, Ratios & Projections",
    "subtitle": "Cartesian, Cylindrical & Spherical Coordinates, Fundamental Direction Cosine Identity & Tetrahedral Angles",
    "sections": u1_sections,
    "simulations": ["sim_geom3d_coords"],
    "problems": u1_problems
}


# ==========================================
# UNIT 2: THE PLANE IN THREE DIMENSIONS
# ==========================================
u2_sections = [
    {
        "id": "u2-sec1",
        "title": "The General Linear Equation & Normal Vectors in Space",
        "content": r"""<h4>1. General First-Degree Equation in $\mathbb{R}^3$</h4>
<div class="math-display">
$$\mathbf{\text{Theorem: Every linear equation of the first degree } Ax + By + Cz + D = 0 \text{ (where } A^2 + B^2 + C^2 \ne 0\text{) represents a plane in } \mathbb{R}^3.}$$
</div>
<p><strong>Proof:</strong> Let $P_1(x_1, y_1, z_1)$ and $P_2(x_2, y_2, z_2)$ be any two distinct points on the surface $Ax + By + Cz + D = 0$. Consider any point $P$ dividing $P_1 P_2$ in ratio $k : 1$:</p>
<div class="math-display">
$$P = \left( \frac{x_1 + k x_2}{1 + k}, \, \frac{y_1 + k y_2}{1 + k}, \, \frac{z_1 + k z_2}{1 + k} \right)$$
</div>
<p>Substituting into the equation:</p>
<div class="math-display">
$$A\left(\frac{x_1 + k x_2}{1 + k}\right) + B\left(\frac{y_1 + k y_2}{1 + k}\right) + C\left(\frac{z_1 + k z_2}{1 + k}\right) + D = \frac{(Ax_1 + By_1 + Cz_1 + D) + k(Ax_2 + By_2 + Cz_2 + D)}{1 + k} = \frac{0 + k(0)}{1 + k} = 0$$
</div>
<p>Since every point on the line segment $P_1 P_2$ lies entirely on the surface, the surface is a plane. $\blacksquare$</p>

<h4>2. Geometric Meaning of Coefficients: The Normal Vector $\vec{n}$</h4>
<p>Let $P_1(x_1, y_1, z_1)$ and $P_2(x_2, y_2, z_2)$ lie on the plane. Subtracting their equations:</p>
<div class="math-display">
$$A(x_2 - x_1) + B(y_2 - y_1) + C(z_2 - z_1) = 0 \Longleftrightarrow (A\hat{i} + B\hat{j} + C\hat{k}) \cdot \vec{P_1 P_2} = 0$$
</div>
<p>The vector $\vec{n} = A\hat{i} + B\hat{j} + C\hat{k}$ is perpendicular to <em>every</em> displacement vector lying in the plane, establishing that $(A, B, C)$ are the direction ratios of the <strong>normal vector</strong> to the plane.</p>

<h4>3. Intercept Form of the Plane</h4>
<p>If the plane intersects the coordinate axes at $A(a, 0, 0)$, $B(0, b, 0)$, and $C(0, 0, c)$ ($abc \ne 0$), dividing by $-D$ yields:</p>
<div class="math-display">
$$\mathbf{\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1}$$
</div>"""
    },
    {
        "id": "u2-sec2",
        "title": "Normal Form & Planes Through Specified Points",
        "content": r"""<h4>1. The Hesse Normal Form: $lx + my + nz = p$</h4>
<p>Let $ON$ be the perpendicular drawn from origin $O$ to the plane, of length $p \ge 0$, having direction cosines $(l, m, n)$. For any point $P(x, y, z)$ on the plane, the projection of position vector $\vec{OP} = (x, y, z)$ onto the normal unit vector $\hat{n} = (l, m, n)$ is identically $p$:</p>
<div class="math-display">
$$\mathbf{lx + my + nz = p} \quad (p \ge 0, \quad l^2 + m^2 + n^2 = 1)$$
</div>

<h4>2. Reduction of General Equation to Normal Form</h4>
<p>To convert $Ax + By + Cz + D = 0$ into normal form, transpose $D$ so the RHS is non-negative and divide by $\pm\sqrt{A^2 + B^2 + C^2}$:</p>
<div class="math-display">
$$\frac{-A}{\pm\sqrt{A^2+B^2+C^2}}x + \frac{-B}{\pm\sqrt{A^2+B^2+C^2}}y + \frac{-C}{\pm\sqrt{A^2+B^2+C^2}}z = \frac{D}{\pm\sqrt{A^2+B^2+C^2}}$$
</div>
<p>The sign is chosen opposite to $D$ so the constant distance $p$ is positive.</p>

<h4>3. Plane Passing Through Three Non-Collinear Points</h4>
<p>The plane passing through $P_1(x_1, y_1, z_1)$, $P_2(x_2, y_2, z_2)$, and $P_3(x_3, y_3, z_3)$ is given by the coplanarity determinant:</p>
<div class="math-display">
$$\mathbf{\begin{vmatrix} x - x_1 & y - y_1 & z - z_1 \\ x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \\ x_3 - x_1 & y_3 - y_1 & z_3 - z_1 \end{vmatrix} = 0}$$
</div>"""
    },
    {
        "id": "u2-sec3",
        "title": "Dihedral Angles & Mutual Positions of Two Planes",
        "content": r"""<h4>1. Dihedral Angle Between Two Planes</h4>
<p>The angle $\theta$ between two planes $\Pi_1: A_1 x + B_1 y + C_1 z + D_1 = 0$ and $\Pi_2: A_2 x + B_2 y + C_2 z + D_2 = 0$ is equal to the angle between their normal vectors $\vec{n}_1$ and $\vec{n}_2$:</p>
<div class="math-display">
$$\mathbf{\cos\theta = \frac{|\vec{n}_1 \cdot \vec{n}_2|}{\|\vec{n}_1\| \|\vec{n}_2\|} = \frac{|A_1 A_2 + B_1 B_2 + C_1 C_2|}{\sqrt{A_1^2 + B_1^2 + C_1^2} \sqrt{A_2^2 + B_2^2 + C_2^2}}}$$
</div>

<h4>2. Special Geometric Orientations</h4>
<ul>
  <li><strong>Perpendicular Planes ($\Pi_1 \perp \Pi_2$):</strong>
    $$\mathbf{A_1 A_2 + B_1 B_2 + C_1 C_2 = 0}$$
  </li>
  <li><strong>Parallel Planes ($\Pi_1 \parallel \Pi_2$):</strong>
    $$\mathbf{\frac{A_1}{A_2} = \frac{B_1}{B_2} = \frac{C_1}{C_2} \ne \frac{D_1}{D_2}}$$
  </li>
  <li><strong>Coincident Planes:</strong> The ratios of all four coefficients are identical.</li>
</ul>"""
    },
    {
        "id": "u2-sec4",
        "title": "Perpendicular Distance of a Point & Dihedral Bisector Planes",
        "content": r"""<h4>1. Distance from a Point $P_1(x_1, y_1, z_1)$ to a Plane</h4>
<p>Let the plane be $\Pi: Ax + By + Cz + D = 0$. The perpendicular distance $d$ from $P_1$ to $\Pi$ is given by:</p>
<div class="math-display">
$$\mathbf{d = \frac{|A x_1 + B y_1 + C z_1 + D|}{\sqrt{A^2 + B^2 + C^2}}}$$
</div>
<p><strong>Proof:</strong> Translate the coordinate origin to $P_1(x_1, y_1, z_1)$ via $x = x' + x_1, y = y' + y_1, z = z' + z_1$. The equation becomes $Ax' + By' + Cz' + (Ax_1 + By_1 + Cz_1 + D) = 0$. In this frame, the distance from the new origin $(0, 0, 0)$ is the constant term divided by the normal norm. $\blacksquare$</p>

<h4>2. Distance Between Parallel Planes</h4>
<p>For parallel planes $Ax + By + Cz + D_1 = 0$ and $Ax + By + Cz + D_2 = 0$:</p>
<div class="math-display">
$$\mathbf{d = \frac{|D_1 - D_2|}{\sqrt{A^2 + B^2 + C^2}}}$$
</div>

<h4>3. Equations of the Dihedral Bisector Planes</h4>
<p>The locus of points equidistant from two planes $\Pi_1$ and $\Pi_2$ forms two orthogonal bisector planes:</p>
<div class="math-display">
$$\mathbf{\frac{A_1 x + B_1 y + C_1 z + D_1}{\sqrt{A_1^2 + B_1^2 + C_1^2}} = \pm \frac{A_2 x + B_2 y + C_2 z + D_2}{\sqrt{A_2^2 + B_2^2 + C_2^2}}}$$
</div>
<p>To distinguish the acute from the obtuse bisector: make $D_1, D_2 > 0$. If $A_1 A_2 + B_1 B_2 + C_1 C_2 > 0$, the positive sign gives the obtuse bisector and the negative sign gives the acute bisector.</p>"""
    },
    {
        "id": "u2-sec5",
        "title": "Pencils of Planes & Common Line Intersections",
        "content": r"""<h4>1. Family (Pencil) of Planes Passing Through the Intersection of Two Planes</h4>
<p>Let $\Pi_1: A_1 x + B_1 y + C_1 z + D_1 = 0$ and $\Pi_2: A_2 x + B_2 y + C_2 z + D_2 = 0$ be two non-parallel planes. Their intersection is a straight line $L$. Any plane passing through this line $L$ is represented by the linear combination parameter $\lambda \in \mathbb{R}$:</p>
<div class="math-display">
$$\mathbf{\Pi_1 + \lambda \Pi_2 = 0 \Longleftrightarrow (A_1 + \lambda A_2)x + (B_1 + \lambda B_2)y + (C_1 + \lambda C_2)z + (D_1 + \lambda D_2) = 0}$$
</div>

<h4>2. Geometric Determination of the Parameter $\lambda$</h4>
<p>The parameter $\lambda$ is uniquely fixed by imposing an extra geometric constraint, such as:</p>
<ol>
  <li>Passing through a fourth point $P_0(x_0, y_0, z_0)$.</li>
  <li>Being perpendicular to a third plane $\Pi_3: A_3 x + B_3 y + C_3 z + D_3 = 0$ via $(A_1 + \lambda A_2)A_3 + (B_1 + \lambda B_2)B_3 + (C_1 + \lambda C_2)C_3 = 0$.</li>
  <li>Being parallel to a given line with direction ratios $(l, m, n)$.</li>
</ol>"""
    }
]

u2_problems = [
    {
        "id": "geom3d-p2-1",
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Parallel Plane Equation and Inter-Planar Distance",
        "statement": r"""(a) Find the equation of the plane passing through $P(2, -1, 3)$ that is parallel to the plane $3x - 4y + 5z = 12$.
(b) Find the perpendicular distance between these two parallel planes.""",
        "solution": r"""<h4>Part (a): Find the Parallel Plane</h4>
<p>Any plane parallel to $3x - 4y + 5z = 12$ has the exact same normal vector $(3, -4, 5)$, so its equation is:</p>
<div class="math-display">
$$3x - 4y + 5z = D$$
</div>
<p>Since it passes through $P(2, -1, 3)$:</p>
<div class="math-display">
$$D = 3(2) - 4(-1) + 5(3) = 6 + 4 + 15 = 25$$
</div>
<p>The equation of the parallel plane is:</p>
<div class="math-display">
$$\mathbf{3x - 4y + 5z = 25 \quad \Longleftrightarrow \quad 3x - 4y + 5z - 25 = 0}$$
</div>

<h4>Part (b): Distance Between Parallel Planes</h4>
<p>Rewrite both planes in standard form: $3x - 4y + 5z - 12 = 0$ ($D_1 = -12$) and $3x - 4y + 5z - 25 = 0$ ($D_2 = -25$).</p>
<div class="math-display">
$$d = \frac{|D_1 - D_2|}{\sqrt{A^2 + B^2 + C^2}} = \frac{|(-12) - (-25)|}{\sqrt{3^2 + (-4)^2 + 5^2}} = \frac{|13|}{\sqrt{9 + 16 + 25}} = \frac{13}{\sqrt{50}} = \mathbf{\frac{13}{5\sqrt{2}} = \frac{13\sqrt{2}}{10}}$$
</div>""",
        "answer": r"""Plane: $3x - 4y + 5z = 25$; Distance $d = \frac{13\sqrt{2}}{10} \approx 1.838$."""
    },
    {
        "id": "geom3d-p2-2",
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Dihedral Bisector Planes & Acute/Obtuse Classification",
        "statement": r"""Find the equations of the bisector planes of the dihedral angles between:
$$\Pi_1: x + 2y + 2z - 9 = 0 \quad \text{and} \quad \Pi_2: 4x - 4y + 2z + 3 = 0$$
Identify which equation bisects the acute angle.""",
        "solution": r"""<h4>Step 1: Normalizing the Plane Equations</h4>
<p>For $\Pi_1$: $\sqrt{1^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = 3$.</p>
<p>For $\Pi_2$: $\sqrt{4^2 + (-4)^2 + 2^2} = \sqrt{16 + 16 + 4} = \sqrt{36} = 6$.</p>

<h4>Step 2: Formulate the Bisector Plane Equations</h4>
<div class="math-display">
$$\frac{x + 2y + 2z - 9}{3} = \pm \frac{4x - 4y + 2z + 3}{6}$$
</div>
<p>Multiplying both sides by $6$:</p>
<div class="math-display">
$$2(x + 2y + 2z - 9) = \pm (4x - 4y + 2z + 3)$$
</div>
<p><strong>Case 1 ($+$ sign):</strong></p>
<div class="math-display">
$$2x + 4y + 4z - 18 = 4x - 4y + 2z + 3 \implies 2x - 8y - 2z + 21 = 0$$
</div>
<p><strong>Case 2 ($-$ sign):</strong></p>
<div class="math-display">
$$2x + 4y + 4z - 18 = -4x + 4y - 2z - 3 \implies 6x + 6z - 15 = 0 \implies 2x + 2z - 5 = 0$$
</div>

<h4>Step 3: Test for Acute vs Obtuse Bisector</h4>
<p>Make both constant terms positive by multiplying $\Pi_1$ by $-1$:</p>
<div class="math-display">
$$\Pi_1: -x - 2y - 2z + 9 = 0, \qquad \Pi_2: 4x - 4y + 2z + 3 = 0$$
</div>
<p>Compute the dot product of normals: $A_1 A_2 + B_1 B_2 + C_1 C_2 = (-1)(4) + (-2)(-4) + (-2)(2) = -4 + 8 - 4 = 0$.</p>
<p>Since the normal dot product is identically $0$, the original two planes are <strong>mutually perpendicular ($\theta = 90^\circ$)</strong>!</p>
<p>Therefore, both bisectors bisect right angles of $45^\circ$.</p>""",
        "answer": r"""Bisector planes: $2x - 8y - 2z + 21 = 0$ and $2x + 2z - 5 = 0$; original planes are orthogonal ($90^\circ$), so both bisect at $45^\circ$."""
    },
    {
        "id": "geom3d-p2-3",
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Variable Intercept Plane & The Circumscribing Sphere Center Locus",
        "statement": r"""A variable plane passes through a fixed point $P(a, b, c)$ ($abc \ne 0$) and intersects the three coordinate axes at points $A, B, C$.
Prove that the locus of the center of the sphere circumscribing the tetrahedron $OABC$ is given by:
$$\frac{a}{x} + \frac{b}{y} + \frac{c}{z} = 2$$""",
        "solution": r"""<h4>Step 1: Set up the Variable Plane</h4>
<p>Let the intercepts of the variable plane on the coordinate axes be $(\alpha, 0, 0)$, $(0, \beta, 0)$, and $(0, 0, \gamma)$.</p>
<p>The equation of the plane in intercept form is:</p>
<div class="math-display">
$$\frac{x}{\alpha} + \frac{y}{\beta} + \frac{z}{\gamma} = 1$$
</div>
<p>Since the plane passes through the fixed point $(a, b, c)$:</p>
<div class="math-display">
$$\mathbf{\frac{a}{\alpha} + \frac{b}{\beta} + \frac{c}{\gamma} = 1} \quad \text{--- (Equation 1)}$$
</div>

<h4>Step 2: Sphere Passing Through $O, A, B, C$</h4>
<p>A general sphere equation in $\mathbb{R}^3$ is:</p>
<div class="math-display">
$$x^2 + y^2 + z^2 + 2ux + 2vy + 2wz + d = 0$$
</div>
<p>Since the sphere passes through the origin $O(0, 0, 0)$, $d = 0$.</p>
<p>Since it passes through $A(\alpha, 0, 0)$: $\alpha^2 + 2u\alpha = 0 \implies 2u = -\alpha \implies u = -\frac{\alpha}{2}$.</p>
<p>Similarly, passing through $B(0, \beta, 0)$ and $C(0, 0, \gamma)$ gives $v = -\frac{\beta}{2}$ and $w = -\frac{\gamma}{2}$.</p>
<p>The equation of the sphere is:</p>
<div class="math-display">
$$x^2 + y^2 + z^2 - \alpha x - \beta y - \gamma z = 0$$
</div>

<h4>Step 3: Center of the Sphere and Elimination</h4>
<p>The center $(X, Y, Z)$ of this sphere is:</p>
<div class="math-display">
$$X = -u = \frac{\alpha}{2}, \qquad Y = -v = \frac{\beta}{2}, \qquad Z = -w = \frac{\gamma}{2}$$
</div>
<p>Thus, the intercepts are expressed in terms of the center coordinates as:</p>
<div class="math-display">
$$\alpha = 2X, \qquad \beta = 2Y, \qquad \gamma = 2Z$$
</div>
<p>Substituting $\alpha, \beta, \gamma$ into Equation 1:</p>
<div class="math-display">
$$\frac{a}{2X} + \frac{b}{2Y} + \frac{c}{2Z} = 1 \implies \mathbf{\frac{a}{X} + \frac{b}{Y} + \frac{c}{Z} = 2}$$
</div>
<p>Replacing $(X, Y, Z)$ with current coordinates $(x, y, z)$ establishes the required locus:</p>
<div class="math-display">
$$\mathbf{\frac{a}{x} + \frac{b}{y} + \frac{c}{z} = 2} \quad \blacksquare$$
</div>""",
        "answer": r"""Proved: The locus of the sphere center is $\frac{a}{x} + \frac{b}{y} + \frac{c}{z} = 2$."""
    }
]

u2_data = {
    "id": "unit2",
    "unit_number": 2,
    "title": "The Plane in Three Dimensions: Equations, Dihedral Angles & Distance Metrics",
    "subtitle": "General & Normal Forms, Dihedral Angles, Bisector Planes, Point-Plane Distance & Pencils of Planes",
    "sections": u2_sections,
    "simulations": ["sim_geom3d_planes"],
    "problems": u2_problems
}

# Write files
with open("geom3d_u1.json", "w", encoding="utf-8") as f:
    json.dump(u1_data, f, indent=2, ensure_ascii=False)
print("Saved geom3d_u1.json successfully.")

with open("geom3d_u2.json", "w", encoding="utf-8") as f:
    json.dump(u2_data, f, indent=2, ensure_ascii=False)
print("Saved geom3d_u2.json successfully.")
