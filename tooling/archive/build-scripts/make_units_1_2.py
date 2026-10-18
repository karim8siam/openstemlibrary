import json

# Unit 1: The Complex Number Field & Geometry of the Complex Plane
u1 = {
  "unit_id": "unit_1",
  "unit_title": "The Complex Number Field & Geometry of the Complex Plane",
  "unit_subtitle": "Field Axioms, Modulus-Conjugate Algebra, Triangle Inequalities, Polar Forms & Complex Loci",
  "sections": [
    {
      "id": "sec_1_1",
      "title": "Axiomatic Construction of the Complex Number Field",
      "content": r"""
<h3>1. Algebraic Construction of $\mathbb{C}$</h3>
<p>
The set of real numbers $\mathbb{R}$ is algebraically incomplete: polynomial equations such as $x^2 + 1 = 0$ possess no real roots. We construct the <strong>field of complex numbers</strong> $\mathbb{C}$ as the set of ordered pairs of real numbers:
$$\mathbb{C} \equiv \{(x, y) \in \mathbb{R}^2\}$$
equipped with two binary operations, <em>addition</em> ($+$) and <em>multiplication</em> ($\cdot$):
</p>
<div class="math-display">
$$(x_1, y_1) + (x_2, y_2) \equiv (x_1 + x_2, \; y_1 + y_2)$$
$$(x_1, y_1) \cdot (x_2, y_2) \equiv (x_1 x_2 - y_1 y_2, \; x_1 y_2 + x_2 y_1)$$
</div>

<h3>2. Verification of Field Axioms</h3>
<p>
The algebraic structure $(\mathbb{C}, +, \cdot)$ satisfies all nine field axioms:
<ul>
  <li><strong>Additive Identity:</strong> $0_{\mathbb{C}} = (0, 0)$. For any $z = (x, y)$, $z + 0_{\mathbb{C}} = (x+0, y+0) = z$.</li>
  <li><strong>Additive Inverse:</strong> For each $z = (x, y)$, $-z = (-x, -y)$, yielding $z + (-z) = (0, 0)$.</li>
  <li><strong>Multiplicative Identity:</strong> $1_{\mathbb{C}} = (1, 0)$. For any $z = (x, y)$, $(x, y)(1, 0) = (x\cdot 1 - y\cdot 0, x\cdot 0 + y\cdot 1) = (x, y)$.</li>
  <li><strong>Multiplicative Inverse:</strong> For every non-zero $z = (x, y) \ne (0, 0)$, $x^2 + y^2 > 0$. The inverse is:
  $$z^{-1} = \left(\frac{x}{x^2 + y^2}, \; \frac{-y}{x^2 + y^2}\right)$$
  Direct calculation yields $z \cdot z^{-1} = \left(\frac{x^2 + y^2}{x^2 + y^2}, \; \frac{-xy + yx}{x^2 + y^2}\right) = (1, 0)$.</li>
  <li><strong>Distributivity & Commutativity:</strong> Multiplication distributes over addition, and both operations are commutative and associative.</li>
</ul>
</p>

<h3>3. Canonical Form and the Imaginary Unit</h3>
<p>
The map $\iota: \mathbb{R} \hookrightarrow \mathbb{C}$ defined by $\iota(x) = (x, 0)$ is an injective field homomorphism, allowing us to identify $\mathbb{R}$ as a subfield of $\mathbb{C}$. Defining the <strong>imaginary unit</strong> $i \equiv (0, 1)$:
$$i^2 = (0, 1) \cdot (0, 1) = (0\cdot 0 - 1\cdot 1, \; 0\cdot 1 + 1\cdot 0) = (-1, 0) \equiv -1$$
Any element $z = (x, y)$ can be written in the canonical Cartesian form:
$$\mathbf{z = (x, 0) + (0, y) = x(1, 0) + y(0, 1) = x + iy}$$
where $x = \text{Re}(z) \in \mathbb{R}$ is the <strong>real part</strong> and $y = \text{Im}(z) \in \mathbb{R}$ is the <strong>imaginary part</strong>.
</p>

<h3>4. Non-Orderability of $\mathbb{C}$</h3>
<p>
<strong>Theorem:</strong> The complex field $\mathbb{C}$ cannot be endowed with the structure of an ordered field.<br>
<em>Proof:</em> In any ordered field, squares of non-zero elements are strictly positive: $a \ne 0 \implies a^2 > 0$. Consequently, $1^2 = 1 > 0$, which implies $-1 < 0$. If $\mathbb{C}$ were ordered, $i \ne 0$ would force $i^2 > 0 \implies -1 > 0$, contradicting $-1 < 0$. Hence, no compatible total order exists on $\mathbb{C}$. $\blacksquare$
</p>
"""
    },
    {
      "id": "sec_1_2",
      "title": "The Argand Plane, Modulus & Complex Conjugation",
      "content": r"""
<h3>1. The Argand Representation</h3>
<p>
Jean-Robert Argand and Carl Friedrich Gauss introduced the geometric representation of $\mathbb{C}$ as a two-dimensional Euclidean plane $\mathbb{R}^2$: the horizontal axis represents the <strong>real axis</strong> ($\text{Re}$), and the vertical axis represents the <strong>imaginary axis</strong> ($\text{Im}$). Every complex number $z = x + iy$ corresponds to the unique point $P(x, y)$ or the position vector $\vec{OP}$.
</p>

<h3>2. The Complex Conjugate</h3>
<p>
For $z = x + iy \in \mathbb{C}$, its <strong>complex conjugate</strong> $\bar{z}$ is defined by:
$$\mathbf{\bar{z} \equiv x - iy}$$
Geometrically, $\bar{z}$ is the orthogonal reflection of $z$ across the real axis.
<strong>Fundamental Properties of Conjugation:</strong>
<ul>
  <li>$\overline{z_1 \pm z_2} = \bar{z}_1 \pm \bar{z}_2$ and $\overline{z_1 z_2} = \bar{z}_1 \bar{z}_2$.</li>
  <li>$\overline{(z_1 / z_2)} = \bar{z}_1 / \bar{z}_2$ for $z_2 \ne 0$.</li>
  <li>$\overline{\bar{z}} = z$.</li>
  <li>$\text{Re}(z) = \frac{z + \bar{z}}{2}, \quad \text{Im}(z) = \frac{z - \bar{z}}{2i}$.</li>
  <li>$z \in \mathbb{R} \iff z = \bar{z}; \quad z \text{ is purely imaginary} \iff z = -\bar{z}$.</li>
</ul>
</p>

<h3>3. The Modulus (Absolute Value)</h3>
<p>
The <strong>modulus</strong> of $z = x + iy$, denoted $|z|$, is the Euclidean distance from the origin to $(x, y)$:
$$\mathbf{|z| \equiv \sqrt{x^2 + y^2} = \sqrt{z \bar{z}}}$$
Key algebraic properties:
<ul>
  <li>$|z| \ge 0$, and $|z| = 0 \iff z = 0$.</li>
  <li>$|z| = |\bar{z}| = |-z| = |-\bar{z}|$.</li>
  <li>$z \bar{z} = |z|^2$. Thus, division can be computed algebraically as $\frac{w}{z} = \frac{w \bar{z}}{|z|^2}$.</li>
  <li>$|z_1 z_2| = |z_1| |z_2|$. <em>Proof:</em> $|z_1 z_2|^2 = (z_1 z_2)\overline{(z_1 z_2)} = z_1 z_2 \bar{z}_1 \bar{z}_2 = (z_1 \bar{z}_1)(z_2 \bar{z}_2) = |z_1|^2 |z_2|^2$. Taking non-negative square roots gives $|z_1 z_2| = |z_1||z_2|$.</li>
  <li>$\left|\frac{z_1}{z_2}\right| = \frac{|z_1|}{|z_2|}$ for $z_2 \ne 0$.</li>
</ul>
</p>
"""
    },
    {
      "id": "sec_1_3",
      "title": "The Triangle Inequality & Vector Geometry",
      "content": r"""
<h3>1. The Fundamental Triangle Inequality</h3>
<p>
<strong>Theorem:</strong> For any two complex numbers $z_1, z_2 \in \mathbb{C}$:
$$\mathbf{|z_1 + z_2| \le |z_1| + |z_2|}$$
<em>Rigorous Proof:</em>
Expanding the squared modulus:
$$|z_1 + z_2|^2 = (z_1 + z_2)\overline{(z_1 + z_2)} = (z_1 + z_2)(\bar{z}_1 + \bar{z}_2) = z_1 \bar{z}_1 + z_1 \bar{z}_2 + z_2 \bar{z}_1 + z_2 \bar{z}_2$$
Since $z_2 \bar{z}_1 = \overline{z_1 \bar{z}_2}$, their sum is $2\text{Re}(z_1 \bar{z}_2)$:
$$|z_1 + z_2|^2 = |z_1|^2 + 2\text{Re}(z_1 \bar{z}_2) + |z_2|^2$$
For any complex number $w$, $\text{Re}(w) \le |w|$. Therefore:
$$\text{Re}(z_1 \bar{z}_2) \le |z_1 \bar{z}_2| = |z_1||\bar{z}_2| = |z_1||z_2|$$
Substituting this upper bound:
$$|z_1 + z_2|^2 \le |z_1|^2 + 2|z_1||z_2| + |z_2|^2 = (|z_1| + |z_2|)^2$$
Taking the positive square root on both sides yields:
$$|z_1 + z_2| \le |z_1| + |z_2| \quad \blacksquare$$
</p>

<h3>2. Condition for Equality</h3>
<p>
Equality holds if and only if $\text{Re}(z_1 \bar{z}_2) = |z_1 \bar{z}_2|$, which requires $z_1 \bar{z}_2$ to be a non-negative real number. If $z_2 \ne 0$, this means:
$$\frac{z_1}{z_2} = \frac{z_1 \bar{z}_2}{|z_2|^2} = \lambda \ge 0$$
Geometrically, equality holds if and only if the vectors $z_1$ and $z_2$ lie on the same ray emanating from the origin (same direction).
</p>

<h3>3. The Reverse Triangle Inequality</h3>
<p>
<strong>Theorem:</strong> For any $z_1, z_2 \in \mathbb{C}$:
$$\mathbf{||z_1| - |z_2|| \le |z_1 - z_2|}$$
<em>Proof:</em> Write $z_1 = (z_1 - z_2) + z_2$. By the triangle inequality:
$$|z_1| = |(z_1 - z_2) + z_2| \le |z_1 - z_2| + |z_2| \implies |z_1| - |z_2| \le |z_1 - z_2|$$
Similarly, interchanging $z_1$ and $z_2$:
$$|z_2| - |z_1| \le |z_2 - z_1| = |z_1 - z_2| \implies -(|z_1| - |z_2|) \le |z_1 - z_2|$$
Combining these two inequalities gives $||z_1| - |z_2|| \le |z_1 - z_2|$. $\blacksquare$
</p>
<p>
Combining both results yields the complete bounds:
$$\mathbf{||z_1| - |z_2|| \le |z_1 \pm z_2| \le |z_1| + |z_2|}$$
</p>
"""
    },
    {
      "id": "sec_1_4",
      "title": "Polar Form, Euler's Formula & Argument Geometry",
      "content": r"""
<h3>1. Modulus-Argument (Polar) Representation</h3>
<p>
Let $z = x + iy \ne 0$. Introducing plane polar coordinates $x = r\cos\theta$ and $y = r\sin\theta$, where $r = |z| = \sqrt{x^2 + y^2} > 0$:
$$\mathbf{z = r(\cos\theta + i\sin\theta)}$$
The angle $\theta$ is the <strong>argument</strong> of $z$, denoted $\arg(z)$. Because $\sin$ and $\cos$ are $2\pi$-periodic, the argument is multi-valued:
$$\arg(z) = \text{Arg}(z) + 2k\pi, \quad k \in \mathbb{Z}$$
The <strong>principal argument</strong> $\text{Arg}(z)$ is uniquely chosen in the interval $(-\pi, \pi]$:
$$\text{Arg}(z) = \begin{cases} \arctan(y/x) & x > 0 \\ \arctan(y/x) + \pi & x < 0, \; y \ge 0 \\ \arctan(y/x) - \pi & x < 0, \; y < 0 \\ \pi/2 & x = 0, \; y > 0 \\ -\pi/2 & x = 0, \; y < 0 \end{cases}$$
</p>

<h3>2. Euler's Formula</h3>
<p>
By expanding the complex exponential function via its Taylor series:
$$e^{i\theta} = \sum_{n=0}^\infty \frac{(i\theta)^n}{n!} = \sum_{k=0}^\infty \frac{(-1)^k \theta^{2k}}{(2k)!} + i \sum_{k=0}^\infty \frac{(-1)^k \theta^{2k+1}}{(2k+1)!} = \cos\theta + i\sin\theta$$
This gives Euler's celebrated representation:
$$\mathbf{z = r e^{i\theta}}$$
</p>

<h3>3. Multiplication and Division in Polar Form</h3>
<p>
Let $z_1 = r_1 e^{i\theta_1}$ and $z_2 = r_2 e^{i\theta_2}$. Then:
$$z_1 z_2 = r_1 r_2 e^{i(\theta_1 + \theta_2)} = r_1 r_2 [\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2)]$$
$$\frac{z_1}{z_2} = \frac{r_1}{r_2} e^{i(\theta_1 - \theta_2)} = \frac{r_1}{r_2} [\cos(\theta_1 - \theta_2) + i\sin(\theta_1 - \theta_2)]$$
<strong>Geometric Interpretation:</strong>
Multiplying $z_1$ by $z_2$ scales the magnitude of $z_1$ by $r_2$ and rotates the vector counterclockwise by angle $\theta_2$. In particular, multiplying any complex number by $i = e^{i\pi/2}$ performs an exact $90^\circ$ counterclockwise rotation.
</p>
"""
    },
    {
      "id": "sec_1_5",
      "title": "Complex Equations of Lines, Circles & Apollonian Loci",
      "content": r"""
<h3>1. Equation of a Straight Line in $\mathbb{C}$</h3>
<p>
A line in the Cartesian plane has the equation $Ax + By + C = 0$ ($A, B, C \in \mathbb{R}$). Substituting $x = \frac{z + \bar{z}}{2}$ and $y = \frac{z - \bar{z}}{2i}$:
$$A\left(\frac{z + \bar{z}}{2}\right) + B\left(\frac{z - \bar{z}}{2i}\right) + C = 0 \iff \left(\frac{A - iB}{2}\right)z + \left(\frac{A + iB}{2}\right)\bar{z} + C = 0$$
Defining the complex coefficient $\alpha \equiv \frac{A + iB}{2} \in \mathbb{C}$ and real constant $\beta \equiv C \in \mathbb{R}$:
$$\mathbf{\bar{\alpha} z + \alpha \bar{z} + \beta = 0}$$
</p>

<h3>2. Equation of a Circle in $\mathbb{C}$</h3>
<p>
A circle centered at $z_0 \in \mathbb{C}$ with radius $R > 0$ is the locus $|z - z_0| = R$. Squaring both sides:
$$(z - z_0)\overline{(z - z_0)} = R^2 \iff z \bar{z} - \bar{z}_0 z - z_0 \bar{z} + (|z_0|^2 - R^2) = 0$$
The general circle equation in $\mathbb{C}$ is:
$$\mathbf{z \bar{z} + \bar{\alpha} z + \alpha \bar{z} + k = 0, \quad k \in \mathbb{R}, \; |\alpha|^2 - k > 0}$$
with center $z_c = -\alpha$ and radius $R = \sqrt{|\alpha|^2 - k}$.
</p>

<h3>3. Apollonian Circles in the Complex Plane</h3>
<p>
<strong>Theorem:</strong> For two distinct points $z_1, z_2 \in \mathbb{C}$ and a constant $k > 0$, the locus of points satisfying:
$$\left|\frac{z - z_1}{z - z_2}\right| = k$$
is:
<ul>
  <li>For $k = 1$: The perpendicular bisector of the segment connecting $z_1$ and $z_2$.</li>
  <li>For $k \ne 1$: A circle (termed the <em>Apollonian circle</em>) with center $z_c$ and radius $R$:
  $$\mathbf{z_c = \frac{z_1 - k^2 z_2}{1 - k^2}, \qquad R = \frac{k |z_1 - z_2|}{|1 - k^2|}}$$
  </li>
</ul>
</p>
"""
    }
  ],
  "simulation": {
    "sim_id": "algebra-complex-plane-sim",
    "title": "Interactive Argand Diagram & Complex Operation Visualizer",
    "description": "Drag complex numbers z₁ and z₂ in the Gauss plane to interactively inspect vector addition (parallelogram rule), complex multiplication (moduli scaling and argument addition), and dynamic triangle inequality bounds."
  },
  "problems": [
    {
      "difficulty": "Tier 1: Foundational",
      "difficultyLabel": "Foundational Mechanics",
      "title": "Example 1.1: Modulus, Conjugate & Polar Transformation",
      "statement": r"Given the complex expression $z = \frac{(1 + i\sqrt{3})^3}{(1 - i)^2}$: (a) Express $z$ in polar exponential form $r e^{i\theta}$. (b) Compute the exact Cartesian form $x + iy$. (c) Determine $|z|$ and $\bar{z}$.",
      "steps": [
        {
          "step": "Step 1: Convert Numerator and Denominator to Polar Form",
          "math": r"1 + i\sqrt{3} = 2\left(\frac{1}{2} + i\frac{\sqrt{3}}{2}\right) = 2 e^{i\pi/3} \\ 1 - i = \sqrt{2}\left(\frac{1}{\sqrt{2}} - \frac{i}{\sqrt{2}}\right) = \sqrt{2} e^{-i\pi/4}",
          "explanation": "Compute modulus and argument for both numerator base and denominator base."
        },
        {
          "step": "Step 2: Apply Powers and Divide",
          "math": r"(1 + i\sqrt{3})^3 = (2 e^{i\pi/3})^3 = 8 e^{i\pi} \\ (1 - i)^2 = (\sqrt{2} e^{-i\pi/4})^2 = 2 e^{-i\pi/2} \\ z = \frac{8 e^{i\pi}}{2 e^{-i\pi/2}} = 4 e^{i(\pi - (-\pi/2))} = 4 e^{i(3\pi/2)} = 4 e^{-i\pi/2}",
          "explanation": "Subtract the argument of the denominator from the numerator argument, normalizing to $(-\\pi, \\pi]$."
        },
        {
          "step": "Step 3: Convert to Cartesian Form and Find Conjugate",
          "math": r"z = 4[\cos(-\pi/2) + i\sin(-\pi/2)] = 4[0 - i] = -4i \\ \bar{z} = 4i, \quad |z| = 4",
          "explanation": "Expanding $e^{-i\\pi/2}$ gives a purely imaginary result $-4i$."
        }
      ],
      "answer": r"z = 4 e^{-i\pi/2} = -4i; \quad |z| = 4, \quad \bar{z} = 4i"
    },
    {
      "difficulty": "Tier 2: Intermediate Exam",
      "difficultyLabel": "Intermediate University Exam",
      "title": "Example 1.2: Equilateral Triangle Inscribed in the Unit Circle",
      "statement": r"Let $z_1, z_2, z_3 \in \mathbb{C}$ satisfy $|z_1| = |z_2| = |z_3| = 1$ and $z_1 + z_2 + z_3 = 0$. Prove that $z_1, z_2, z_3$ form the vertices of an equilateral triangle, and calculate $|z_1 - z_2|^2 + |z_2 - z_3|^2 + |z_3 - z_1|^2$.",
      "steps": [
        {
          "step": "Step 1: Compute Centroid and Circumcentre",
          "math": r"\text{Centroid } z_G = \frac{z_1 + z_2 + z_3}{3} = \frac{0}{3} = 0",
          "explanation": "Since $|z_1| = |z_2| = |z_3| = 1$, the circumcentre $z_O$ of the triangle is at the origin $0$. Thus the circumcentre and centroid coincide at the origin."
        },
        {
          "step": "Step 2: Equilateral Geometry via Coincident Centers",
          "math": r"z_O = z_G = 0 \implies \text{The triangle is strictly equilateral!}",
          "explanation": "In Euclidean geometry, a triangle whose circumcentre and centroid coincide is necessarily equilateral."
        },
        {
          "step": "Step 3: Expand the Sum of Squared Side Lengths",
          "math": r"|z_1 - z_2|^2 = (z_1 - z_2)(\bar{z}_1 - \bar{z}_2) = |z_1|^2 + |z_2|^2 - (z_1 \bar{z}_2 + z_2 \bar{z}_1) = 2 - 2\text{Re}(z_1 \bar{z}_2) \\ \sum_{\text{cyclic}} |z_1 - z_2|^2 = 6 - 2\text{Re}(z_1 \bar{z}_2 + z_2 \bar{z}_3 + z_3 \bar{z}_1) \\ |z_1 + z_2 + z_3|^2 = 0 \implies |z_1|^2 + |z_2|^2 + |z_3|^2 + 2\text{Re}(z_1 \bar{z}_2 + z_2 \bar{z}_3 + z_3 \bar{z}_1) = 0 \\ 3 + 2\text{Re}(z_1 \bar{z}_2 + z_2 \bar{z}_3 + z_3 \bar{z}_1) = 0 \implies 2\text{Re}(\dots) = -3 \\ \sum_{\text{cyclic}} |z_1 - z_2|^2 = 6 - (-3) = 9",
          "explanation": "The sum of the squares of the sides of the inscribed equilateral triangle equals 9, corresponding to individual side lengths of $\\sqrt{3}$."
        }
      ],
      "answer": r"\text{The vertices form an equilateral triangle with side lengths } \sqrt{3}, \text{ and the sum of squared sides is } 9."
    },
    {
      "difficulty": "Tier 3: Honors / Proof Challenge",
      "difficultyLabel": "Honors / Proof Challenge",
      "title": "Example 1.3: Derivation of the Apollonian Circle & Conjugate Orthogonality",
      "statement": r"Given two distinct points $z_1, z_2 \in \mathbb{C}$ and $k \in \mathbb{R}^+ \setminus \{1\}$: (a) Derive the equation of the Apollonius locus $|z - z_1| = k |z - z_2|$ in the form $|z - z_c|^2 = R^2$, explicitly finding the center $z_c$ and radius $R$. (b) Prove that any circle passing through $z_1$ and $z_2$ intersects this Apollonian circle orthogonally.",
      "steps": [
        {
          "step": "Step 1: Algebraic Reduction of the Locus",
          "math": r"|z - z_1|^2 = k^2 |z - z_2|^2 \iff (z - z_1)(\bar{z} - \bar{z}_1) = k^2 (z - z_2)(\bar{z} - \bar{z}_2) \\ z\bar{z} - \bar{z}_1 z - z_1 \bar{z} + |z_1|^2 = k^2 [z\bar{z} - \bar{z}_2 z - z_2 \bar{z} + |z_2|^2] \\ (1 - k^2) z\bar{z} - (\bar{z}_1 - k^2 \bar{z}_2) z - (z_1 - k^2 z_2) \bar{z} + (|z_1|^2 - k^2 |z_2|^2) = 0",
          "explanation": "Expand squared moduli and collect terms into the general complex circle equation."
        },
        {
          "step": "Step 2: Complete the Square to Determine Center and Radius",
          "math": r"z\bar{z} - \bar{z}_c z - z_c \bar{z} + \frac{|z_1|^2 - k^2 |z_2|^2}{1 - k^2} = 0 \quad \text{where } z_c = \frac{z_1 - k^2 z_2}{1 - k^2} \\ |z - z_c|^2 = |z_c|^2 - \frac{|z_1|^2 - k^2 |z_2|^2}{1 - k^2} = \frac{|z_1 - k^2 z_2|^2 - (1 - k^2)(|z_1|^2 - k^2 |z_2|^2)}{(1 - k^2)^2} \\ \text{Numerator simplifies to: } k^2 |z_1 - z_2|^2 \\ R = \frac{k |z_1 - z_2|}{|1 - k^2|}",
          "explanation": "Complete the square to obtain the canonical center $z_c$ and radius $R$."
        },
        {
          "step": "Step 3: Prove Orthogonality with Circles Passing Through z_1 and z_2",
          "math": r"\text{Power of } z_c \text{ with respect to any circle } C_{12} \text{ through } z_1, z_2 \text{ is } (z_c - z_1)(z_c - z_2) \\ z_c - z_1 = \frac{z_1 - k^2 z_2 - z_1(1 - k^2)}{1 - k^2} = \frac{-k^2(z_2 - z_1)}{1 - k^2} = \frac{k^2(z_1 - z_2)}{1 - k^2} \\ z_c - z_2 = \frac{z_1 - k^2 z_2 - z_2(1 - k^2)}{1 - k^2} = \frac{z_1 - z_2}{1 - k^2} \\ (z_c - z_1)(\overline{z_c - z_2}) = \frac{k^2 |z_1 - z_2|^2}{(1 - k^2)^2} = R^2",
          "explanation": "Because the product of distances from the center $z_c$ to the collinear points $z_1, z_2$ equals $R^2$, the points $z_1, z_2$ are inverse points with respect to the Apollonian circle. Consequently, any circle through $z_1, z_2$ cuts the Apollonian circle orthogonally."
        }
      ],
      "answer": r"\mathbf{z_c = \frac{z_1 - k^2 z_2}{1 - k^2}}, \quad \mathbf{R = \frac{k |z_1 - z_2|}{|1 - k^2|}}; \quad \text{Orthogonality follows from } (z_c - z_1)(\overline{z_c - z_2}) = R^2."
    }
  ]
}

# Unit 2: De Moivre’s Theorem, Roots of Unity & Trigonometric Expansions
u2 = {
  "unit_id": "unit_2",
  "unit_title": "De Moivre’s Theorem, Roots of Unity & Trigonometric Expansions",
  "unit_subtitle": "Inductive Proof, Multiple-Angle Expansions, Power Reductions, Complex n-th Roots & Cyclotomic Geometry",
  "sections": [
    {
      "id": "sec_2_1",
      "title": "Statement and Rigorous Proof of De Moivre’s Theorem",
      "content": r"""
<h3>1. Statement of De Moivre's Theorem</h3>
<p>
Abraham de Moivre established one of the foundational bridges between complex analysis and trigonometry:
$$\mathbf{(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta)}$$
In compact Euler notation, this expresses the exponential property $(e^{i\theta})^n = e^{in\theta}$.
</p>

<h3>2. Rigorous Proof for Positive Integers ($n \in \mathbb{N}$)</h3>
<p>
We prove the theorem by the Principle of Mathematical Induction on $n$:<br>
<strong>Base Step ($n = 1$):</strong> $(\cos\theta + i\sin\theta)^1 = \cos(1\cdot\theta) + i\sin(1\cdot\theta)$, which is trivially true.<br>
<strong>Inductive Hypothesis:</strong> Assume the identity holds for some positive integer $k \ge 1$:
$$(\cos\theta + i\sin\theta)^k = \cos(k\theta) + i\sin(k\theta)$$
<strong>Inductive Step:</strong> Consider $n = k + 1$:
$$(\cos\theta + i\sin\theta)^{k+1} = (\cos\theta + i\sin\theta)^k \cdot (\cos\theta + i\sin\theta)$$
Using the inductive hypothesis:
$$= [\cos(k\theta) + i\sin(k\theta)] [\cos\theta + i\sin\theta]$$
Expanding the complex multiplication:
$$= [\cos(k\theta)\cos\theta - \sin(k\theta)\sin\theta] + i[\sin(k\theta)\cos\theta + \cos(k\theta)\sin\theta]$$
Applying standard trigonometric angle-addition identities:
$$\cos(k\theta)\cos\theta - \sin(k\theta)\sin\theta = \cos((k+1)\theta)$$
$$\sin(k\theta)\cos\theta + \cos(k\theta)\sin\theta = \sin((k+1)\theta)$$
Thus:
$$(\cos\theta + i\sin\theta)^{k+1} = \cos((k+1)\theta) + i\sin((k+1)\theta)$$
By induction, the theorem is proved for all $n \in \mathbb{N}$. $\blacksquare$
</p>

<h3>3. Extension to Negative Integers and Rational Powers</h3>
<p>
<strong>Case $n = 0$:</strong> $(\cos\theta + i\sin\theta)^0 = 1 = \cos 0 + i\sin 0$.<br>
<strong>Case $n = -m$ where $m \in \mathbb{N}$:</strong>
$$(\cos\theta + i\sin\theta)^{-m} = \frac{1}{(\cos\theta + i\sin\theta)^m} = \frac{1}{\cos(m\theta) + i\sin(m\theta)}$$
Multiplying numerator and denominator by $\cos(m\theta) - i\sin(m\theta)$:
$$= \frac{\cos(m\theta) - i\sin(m\theta)}{\cos^2(m\theta) + \sin^2(m\theta)} = \cos(-m\theta) + i\sin(-m\theta) = \cos(n\theta) + i\sin(n\theta)$$
<strong>Rational Powers $n = p/q$ ($q > 0$):</strong> One of the values of $(\cos\theta + i\sin\theta)^{p/q}$ is $\cos(p\theta/q) + i\sin(p\theta/q)$, with exactly $q$ distinct complex values given by $\cos\left(\frac{p\theta + 2k\pi}{q}\right) + i\sin\left(\frac{p\theta + 2k\pi}{q}\right)$ for $k = 0, 1, \dots, q-1$.
</p>
"""
    },
    {
      "id": "sec_2_2",
      "title": "Expansions of $\cos(n\theta)$ and $\sin(n\theta)$ in Powers of $\cos\theta$ and $\sin\theta$",
      "content": r"""
<h3>1. Binomial Expansion Technique</h3>
<p>
By De Moivre's theorem, $\cos(n\theta) + i\sin(n\theta) = (\cos\theta + i\sin\theta)^n$. Expanding the right-hand side using the Binomial Theorem:
$$(\cos\theta + i\sin\theta)^n = \sum_{k=0}^n \binom{n}{k} \cos^{n-k}\theta \, (i\sin\theta)^k$$
Since $i^k$ alternates signs for even powers ($i^0 = 1, i^2 = -1, i^4 = 1$) and yields imaginary units for odd powers ($i^1 = i, i^3 = -i, i^5 = i$), we equate real and imaginary parts.
</p>

<h3>2. Explicit Formulas</h3>
<p>
<strong>Expansion of $\cos(n\theta)$ (Real Part):</strong>
$$\mathbf{\cos(n\theta) = \cos^n\theta - \binom{n}{2}\cos^{n-2}\theta\sin^2\theta + \binom{n}{4}\cos^{n-4}\theta\sin^4\theta - \dots}$$
Substituting $\sin^2\theta = 1 - \cos^2\theta$ expresses $\cos(n\theta)$ purely as a polynomial in $\cos\theta$ of degree $n$, matching the celebrated <strong>Chebyshev Polynomial of the First Kind</strong> $T_n(x)$ where $x = \cos\theta$: $\cos(n\theta) = T_n(\cos\theta)$.
</p>
<p>
<strong>Expansion of $\sin(n\theta)$ (Imaginary Part):</strong>
$$\mathbf{\sin(n\theta) = \binom{n}{1}\cos^{n-1}\theta\sin\theta - \binom{n}{3}\cos^{n-3}\theta\sin^3\theta + \binom{n}{5}\cos^{n-5}\theta\sin^5\theta - \dots}$$
Dividing by $\sin\theta$ yields the <strong>Chebyshev Polynomial of the Second Kind</strong> $U_{n-1}(\cos\theta)$.
</p>

<h3>3. Expansion of $\tan(n\theta)$</h3>
<p>
Taking the quotient $\frac{\sin(n\theta)}{\cos(n\theta)}$ and dividing both numerator and denominator by $\cos^n\theta$:
$$\mathbf{\tan(n\theta) = \frac{\binom{n}{1}\tan\theta - \binom{n}{3}\tan^3\theta + \binom{n}{5}\tan^5\theta - \dots}{1 - \binom{n}{2}\tan^2\theta + \binom{n}{4}\tan^4\theta - \dots}}$$
</p>
"""
    },
    {
      "id": "sec_2_3",
      "title": "Expansions of $\cos^n\theta$ and $\sin^n\theta$ in Terms of Sines and Cosines of Multiple Angles",
      "content": r"""
<h3>1. The Reciprocal Exponential Variables</h3>
<p>
Let $x = e^{i\theta} = \cos\theta + i\sin\theta$. Then $\frac{1}{x} = e^{-i\theta} = \cos\theta - i\sin\theta$.<br>
Adding and subtracting these relations:
$$\mathbf{2\cos\theta = x + \frac{1}{x}, \qquad 2i\sin\theta = x - \frac{1}{x}}$$
More generally, for any integer $k \ge 1$:
$$\mathbf{2\cos(k\theta) = x^k + \frac{1}{x^k}, \qquad 2i\sin(k\theta) = x^k - \frac{1}{x^k}}$$
</p>

<h3>2. Systematic Power Reduction for $\cos^n\theta$</h3>
<p>
Raising $2\cos\theta$ to the $n$-th power and applying the Binomial Theorem:
$$(2\cos\theta)^n = \left(x + \frac{1}{x}\right)^n = \sum_{k=0}^n \binom{n}{k} x^{n-k} \left(\frac{1}{x}\right)^k = \sum_{k=0}^n \binom{n}{k} x^{n-2k}$$
Pairing terms symmetrically from the ends: $\binom{n}{k} = \binom{n}{n-k}$, so:
$$x^{n-2k} + \frac{1}{x^{n-2k}} = 2\cos((n - 2k)\theta)$$
For example, for $n = 4$:
$$2^4 \cos^4\theta = \left(x + \frac{1}{x}\right)^4 = \left(x^4 + \frac{1}{x^4}\right) + 4\left(x^2 + \frac{1}{x^2}\right) + 6$$
$$16\cos^4\theta = 2\cos(4\theta) + 4[2\cos(2\theta)] + 6 \implies \mathbf{\cos^4\theta = \frac{1}{8}[\cos(4\theta) + 4\cos(2\theta) + 3]}$$
</p>

<h3>3. Systematic Power Reduction for $\sin^n\theta$</h3>
<p>
Similarly, raising $2i\sin\theta$ to the $n$-th power:
$$(2i\sin\theta)^n = \left(x - \frac{1}{x}\right)^n = \sum_{k=0}^n (-1)^k \binom{n}{k} x^{n-2k}$$
For odd $n$, the terms pair into $2i\sin((n-2k)\theta)$. For even $n$, the terms pair into $2\cos((n-2k)\theta)$, providing closed forms essential for calculus and physics integrals!
</p>
"""
    },
    {
      "id": "sec_2_4",
      "title": "The $n$-th Roots of Arbitrary Complex Numbers",
      "content": r"""
<h3>1. The Fundamental Root Equation</h3>
<p>
Let $w = R e^{i\phi}$ be a given non-zero complex number, where $R = |w| > 0$ and $\phi = \text{Arg}(w)$. We seek all complex solutions $z = r e^{i\theta}$ to the polynomial equation:
$$z^n = w \iff r^n e^{in\theta} = R e^{i\phi}$$
Equating moduli and arguments:
$$r^n = R \implies r = \sqrt[n]{R} \in \mathbb{R}^+$$
$$n\theta = \phi + 2k\pi \implies \theta_k = \frac{\phi + 2k\pi}{n}, \quad k \in \mathbb{Z}$$
</p>

<h3>2. The Exactly $n$ Distinct Complex Roots</h3>
<p>
As $k$ ranges through $0, 1, 2, \dots, n-1$, we obtain $n$ distinct values of $\theta_k$ within a span of $2\pi$. For $k \ge n$, the arguments differ from previous ones by multiples of $2\pi$, producing the identical complex numbers.
Thus, the equation $z^n = w$ possesses exactly $n$ distinct roots:
$$\mathbf{z_k = \sqrt[n]{R} \exp\left(i \frac{\phi + 2k\pi}{n}\right) = \sqrt[n]{R} \left[ \cos\left(\frac{\phi + 2k\pi}{n}\right) + i\sin\left(\frac{\phi + 2k\pi}{n}\right) \right]}$$
for $k = 0, 1, 2, \dots, n-1$.
</p>

<h3>3. Geometric Configuration of Roots</h3>
<p>
In the Argand plane:
<ul>
  <li>All $n$ roots have identical modulus $r = \sqrt[n]{R}$, placing them on a circle of radius $\sqrt[n]{R}$ centered at the origin.</li>
  <li>The angular separation between adjacent roots is constantly $\Delta\theta = \frac{2\pi}{n}$.</li>
  <li>The roots form the vertices of a <strong>regular $n$-sided polygon</strong> inscribed in the circle $|z| = \sqrt[n]{R}$.</li>
</ul>
</p>
"""
    },
    {
      "id": "sec_2_5",
      "title": "The $n$-th Roots of Unity & Cyclotomic Geometry",
      "content": r"""
<h3>1. The Roots of Unity</h3>
<p>
Setting $w = 1 = 1 \cdot e^{i\cdot 0}$, the solutions to $z^n = 1$ are the <strong>$n$-th roots of unity</strong>:
$$\mathbf{\omega_k = e^{i\frac{2k\pi}{n}} = \cos\left(\frac{2k\pi}{n}\right) + i\sin\left(\frac{2k\pi}{n}\right), \quad k = 0, 1, \dots, n-1}$$
Defining the fundamental root $\omega \equiv \omega_1 = e^{i 2\pi/n}$, the complete set of roots is:
$$U_n = \{1, \omega, \omega^2, \omega^3, \dots, \omega^{n-1}\}$$
Under complex multiplication, $(U_n, \cdot)$ forms a finite <strong>cyclic group</strong> of order $n$ isomorphic to $\mathbb{Z}/n\mathbb{Z}$.
</p>

<h3>2. The Fundamental Algebraic Identities</h3>
<p>
<ul>
  <li><strong>Sum of Roots Identity:</strong>
  Since $z^n - 1 = (z - 1)(z^{n-1} + z^{n-2} + \dots + z + 1) = 0$, for any root $\omega \ne 1$:
  $$\mathbf{1 + \omega + \omega^2 + \dots + \omega^{n-1} = \sum_{k=0}^{n-1} \omega^k = 0}$$
  Geometrically, the centroid of the regular $n$-gon is at the origin $\sum z_k / n = 0$.</li>
  <li><strong>Product of Roots Identity:</strong>
  $$\prod_{k=0}^{n-1} \omega_k = (-1)^{n-1}$$</li>
</ul>
</p>

<h3>3. Primitive Roots and Cyclotomic Polynomials</h3>
<p>
A root $\omega_k$ is a <strong>primitive $n$-th root of unity</strong> if its multiplicative order is exactly $n$—that is, $\omega_k^m \ne 1$ for all $1 \le m < n$.<br>
<strong>Theorem:</strong> $\omega_k = e^{i 2k\pi/n}$ is primitive if and only if $\gcd(k, n) = 1$. The number of primitive $n$-th roots of unity is given by Euler's totient function $\phi(n)$.<br>
The $n$-th <strong>cyclotomic polynomial</strong> $\Phi_n(x)$ is defined as the monic polynomial whose roots are precisely the primitive $n$-th roots of unity:
$$\Phi_n(x) \equiv \prod_{\substack{1 \le k \le n \\ \gcd(k, n) = 1}} \left(x - e^{i\frac{2k\pi}{n}}\right)$$
Remarkably, $\Phi_n(x)$ always has integer coefficients and is irreducible over $\mathbb{Q}$, with $x^n - 1 = \prod_{d | n} \Phi_d(x)$.
</p>
"""
    }
  ],
  "simulation": {
    "sim_id": "algebra-demoivre-roots-sim",
    "title": "Interactive n-th Roots of Unity & Regular Polygon Generator",
    "description": "Adjust the order slider n from 2 to 12 to visualize the n-th roots of unity forming regular polygons on the unit circle. Highlights primitive roots, root multiplication dynamics, and verified algebraic sums equal to zero."
  },
  "problems": [
    {
      "difficulty": "Tier 1: Foundational",
      "difficultyLabel": "Foundational Mechanics",
      "title": "Example 2.1: Expansions of Multiple Angles via Binomial De Moivre",
      "statement": r"Use De Moivre's theorem to: (a) Express $\cos(5\theta)$ in terms of powers of $\cos\theta$. (b) Find all complex solutions to the equation $z^3 + 8 = 0$.",
      "steps": [
        {
          "step": "Step 1: Expand cos(5θ) via Binomial Theorem",
          "math": r"\cos(5\theta) + i\sin(5\theta) = (\cos\theta + i\sin\theta)^5 = \cos^5\theta + 5i\cos^4\theta\sin\theta - 10\cos^3\theta\sin^2\theta - 10i\cos^2\theta\sin^3\theta + 5\cos\theta\sin^4\theta + i\sin^5\theta",
          "explanation": "Expand $(\\cos\\theta + i\\sin\\theta)^5$ using binomial coefficients $(1, 5, 10, 10, 5, 1)$."
        },
        {
          "step": "Step 2: Equate Real Parts and Eliminate sin²θ",
          "math": r"\cos(5\theta) = \cos^5\theta - 10\cos^3\theta\sin^2\theta + 5\cos\theta\sin^4\theta \\ = \cos^5\theta - 10\cos^3\theta(1 - \cos^2\theta) + 5\cos\theta(1 - \cos^2\theta)^2 \\ = \cos^5\theta - 10\cos^3\theta + 10\cos^5\theta + 5\cos\theta(1 - 2\cos^2\theta + \cos^4\theta) \\ = 16\cos^5\theta - 20\cos^3\theta + 5\cos\theta",
          "explanation": "Substitute $\\sin^2\\theta = 1 - \\cos^2\\theta$ and collect like powers of $\\cos\\theta$."
        },
        {
          "step": "Step 3: Solve z³ + 8 = 0",
          "math": r"z^3 = -8 = 8 e^{i\pi} \implies z_k = \sqrt[3]{8} e^{i(\pi + 2k\pi)/3} = 2 e^{i(2k+1)\pi/3}, \quad k = 0, 1, 2 \\ z_0 = 2 e^{i\pi/3} = 2\left(\frac{1}{2} + i\frac{\sqrt{3}}{2}\right) = 1 + i\sqrt{3} \\ z_1 = 2 e^{i\pi} = -2 \\ z_2 = 2 e^{i 5\pi/3} = 2\left(\frac{1}{2} - i\frac{\sqrt{3}}{2}\right) = 1 - i\sqrt{3}",
          "explanation": "Compute the three cube roots of $-8$ on the circle of radius 2."
        }
      ],
      "answer": r"\cos(5\theta) = 16\cos^5\theta - 20\cos^3\theta + 5\cos\theta; \quad \text{Roots: } z \in \{-2, \; 1 \pm i\sqrt{3}\}."
    },
    {
      "difficulty": "Tier 2: Intermediate Exam",
      "difficultyLabel": "Intermediate University Exam",
      "title": "Example 2.2: Rational Fraction Polynomial Roots via De Moivre",
      "statement": r"Solve the polynomial equation $(z + 1)^5 + (z - 1)^5 = 0$ over $\mathbb{C}$, proving that all roots are purely imaginary.",
      "steps": [
        {
          "step": "Step 1: Rewrite into Ratio Form",
          "math": r"(z + 1)^5 = -(z - 1)^5 \iff \left(\frac{z + 1}{z - 1}\right)^5 = -1 = e^{i\pi}",
          "explanation": "Note that $z = 1$ is not a solution, so dividing by $(z - 1)^5$ is valid."
        },
        {
          "step": "Step 2: Find the 5th Roots of -1",
          "math": r"\frac{z + 1}{z - 1} = e^{i(2k + 1)\pi/5}, \quad k = 0, 1, 2, 3, 4",
          "explanation": "The five roots of $-1$ have unit magnitude and odd multiples of $\\pi/5$."
        },
        {
          "step": "Step 3: Solve for z and Prove Pure Imaginariness",
          "math": r"\text{Let } w_k = e^{i(2k+1)\pi/5}. \quad z_k = \frac{w_k + 1}{w_k - 1} = \frac{e^{i\theta_k} + 1}{e^{i\theta_k} - 1} \\ z_k = \frac{e^{i\theta_k/2}(e^{i\theta_k/2} + e^{-i\theta_k/2})}{e^{i\theta_k/2}(e^{i\theta_k/2} - e^{-i\theta_k/2})} = \frac{2\cos(\theta_k/2)}{2i\sin(\theta_k/2)} = -i \cot\left(\frac{(2k+1)\pi}{10}\right) \\ \text{For } k = 0, 1, 2, 3, 4: \quad z_k \in \left\{ -i\cot(\pi/10), \; -i\cot(3\pi/10), \; -i\cot(5\pi/10), \; -i\cot(7\pi/10), \; -i\cot(9\pi/10) \right\} \\ \text{Since } \cot(5\pi/10) = \cot(\pi/2) = 0: \quad z_2 = 0 \\ \text{Since } \cot(\theta) \in \mathbb{R}, \text{ every root } z_k \text{ has zero real part and is purely imaginary!}",
          "explanation": "Express $z$ as $-i\\cot(\\theta_k/2)$, confirming that $\\text{Re}(z_k) = 0$ for all roots."
        }
      ],
      "answer": r"z_k = -i\cot\left(\frac{(2k+1)\pi}{10}\right) \implies z \in \{0, \; \pm i\cot(\pi/10), \; \pm i\cot(3\pi/10)\}; \quad \text{All roots are purely imaginary}."
    },
    {
      "difficulty": "Tier 3: Honors / Proof Challenge",
      "difficultyLabel": "Honors / Proof Challenge",
      "title": "Example 2.3: Closed Product Identity for Primitive Roots of Unity",
      "statement": r"Let $\omega_k = e^{i 2k\pi/n}$ be the $n$-th roots of unity for $n \ge 2$. (a) Prove that $\prod_{k=1}^{n-1} (1 - \omega_k) = n$. (b) Deduce the celebrated trigonometric product theorem: $\prod_{k=1}^{n-1} \sin\left(\frac{k\pi}{n}\right) = \frac{n}{2^{n-1}}$.",
      "steps": [
        {
          "step": "Step 1: Factor Polynomial zⁿ - 1",
          "math": r"z^n - 1 = (z - 1)\prod_{k=1}^{n-1} (z - \omega_k) \\ \frac{z^n - 1}{z - 1} = z^{n-1} + z^{n-2} + \dots + z + 1 = \prod_{k=1}^{n-1} (z - \omega_k)",
          "explanation": "Divide $z^n - 1$ by $z - 1$ to form the cyclotomic product of the non-trivial roots."
        },
        {
          "step": "Step 2: Evaluate at z = 1",
          "math": r"\lim_{z \to 1} \frac{z^n - 1}{z - 1} = 1^{n-1} + 1^{n-2} + \dots + 1 = n \\ \prod_{k=1}^{n-1} (1 - \omega_k) = n",
          "explanation": "Setting $z = 1$ establishes the first fundamental product identity."
        },
        {
          "step": "Step 3: Relate (1 - ω_k) to Sine Function",
          "math": r"1 - \omega_k = 1 - e^{i 2k\pi/n} = e^{i k\pi/n} (e^{-i k\pi/n} - e^{i k\pi/n}) = -2i e^{i k\pi/n} \sin\left(\frac{k\pi}{n}\right) \\ |1 - \omega_k| = |-2i| |e^{i k\pi/n}| \left|\sin\left(\frac{k\pi}{n}\right)\right| = 2\sin\left(\frac{k\pi}{n}\right) \quad \left(\text{since } 0 < \frac{k\pi}{n} < \pi \implies \sin > 0\right) \\ \prod_{k=1}^{n-1} |1 - \omega_k| = \prod_{k=1}^{n-1} \left[2\sin\left(\frac{k\pi}{n}\right)\right] = 2^{n-1} \prod_{k=1}^{n-1} \sin\left(\frac{k\pi}{n}\right)",
          "explanation": "Take the absolute value of both sides and isolate the trigonometric product."
        },
        {
          "step": "Step 4: Conclude the Product Value",
          "math": r"2^{n-1} \prod_{k=1}^{n-1} \sin\left(\frac{k\pi}{n}\right) = n \implies \prod_{k=1}^{n-1} \sin\left(\frac{k\pi}{n}\right) = \frac{n}{2^{n-1}} \quad \blacksquare",
          "explanation": "Divide by $2^{n-1}$ to complete the proof."
        }
      ],
      "answer": r"\prod_{k=1}^{n-1} (1 - \omega_k) = n; \qquad \prod_{k=1}^{n-1} \sin\left(\frac{k\pi}{n}\right) = \frac{n}{2^{n-1}}."
    }
  ]
}

with open("algebra_u1.json", "w", encoding="utf-8") as f:
    json.dump(u1, f, indent=2, ensure_ascii=False)
print("algebra_u1.json written successfully!")

with open("algebra_u2.json", "w", encoding="utf-8") as f:
    json.dump(u2, f, indent=2, ensure_ascii=False)
print("algebra_u2.json written successfully!")
