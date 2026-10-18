import json

print("Building Calculus II: Units 3 & 4...")

# ==========================================
# UNIT 3: GEOMETRIC APPLICATIONS IN CARTESIAN COORDINATES
# ==========================================
u3_sections = [
    {
        "id": "u3-sec1",
        "title": "Plane Areas Between Intersecting Curves: Vertical vs Horizontal Slicing",
        "content": r"""<h4>1. General Area Formulation as an Integral</h4>
<p>Let $f, g: [a, b] \to \mathbb{R}$ be two continuous functions on the closed interval $[a, b]$ such that $f(x) \ge g(x)$ for all $x \in [a, b]$. The area $A$ of the planar region bounded above by $y = f(x)$, below by $y = g(x)$, and laterally by vertical lines $x = a$ and $x = b$ is the Riemann integral of the differential height element:</p>
<div class="math-display">
$$dA = \Big( f(x) - g(x) \Big) \, dx \implies \mathbf{A = \int_a^b \Big( f(x) - g(x) \Big) \, dx}$$
</div>

<h4>2. Signed Area vs Total Geometric Area</h4>
<p>If the curves intersect multiple times within $[a, b]$ at roots $c_1, c_2, \dots \in (a, b)$, the relative ordering $f(x) \ge g(x)$ flips. The total geometric area is given by the integral of the absolute difference:</p>
<div class="math-display">
$$A_{\text{total}} = \int_a^b |f(x) - g(x)| \, dx = \sum_{k} \int_{c_k}^{c_{k+1}} \Big| f(x) - g(x) \Big| \, dx$$
</div>

<h4>3. Horizontal Slicing ($dy$ Integration)</h4>
<p>When the boundary curves are more naturally parameterized as functions of $y$, say $x = w_R(y)$ (right boundary) and $x = w_L(y)$ (left boundary) for $y \in [c, d]$ with $w_R(y) \ge w_L(y)$, horizontal slicing avoids piecewise decomposition:</p>
<div class="math-display">
$$dA = \Big( w_R(y) - w_L(y) \Big) \, dy \implies \mathbf{A = \int_c^d \Big( w_R(y) - w_L(y) \Big) \, dy}$$
</div>"""
    },
    {
        "id": "u3-sec2",
        "title": "Volumes of Revolution: The Disk and Washer Methods",
        "content": r"""<h4>1. Rotational Symmetry & The Differential Disk Element</h4>
<p>Let a region bounded by $y = f(x) \ge 0$, the $x$-axis, and lines $x = a, x = b$ be rotated through $2\pi$ radians about the $x$-axis. Slicing perpendicular to the axis of rotation produces circular cross-sectional disks of radius $R(x) = f(x)$ and thickness $dx$.</p>
<div class="math-display">
$$dV = A(x) \, dx = \pi [R(x)]^2 \, dx \implies \mathbf{V = \pi \int_a^b [f(x)]^2 \, dx}$$
</div>

<h4>2. The Washer Method for Annular Cross-Sections</h4>
<p>When the planar region is bounded between an outer curve $y = f(x)$ and an inner curve $y = g(x)$ ($0 \le g(x) \le f(x)$), rotation generates an annular washer with outer radius $R(x) = f(x)$ and inner hole radius $r(x) = g(x)$:</p>
<div class="math-display">
$$dV = \Big( \pi R(x)^2 - \pi r(x)^2 \Big) dx = \pi \Big( [f(x)]^2 - [g(x)]^2 \Big) dx$$
</div>
<div class="math-display">
$$\mathbf{V = \pi \int_a^b \Big( [f(x)]^2 - [g(x)]^2 \Big) \, dx}$$
</div>

<h4>3. Rotation About Non-Origin Axes</h4>
<p>If the rotation axis is shifted to the horizontal line $y = k$:</p>
<div class="math-display">
$$R(x) = |f(x) - k|, \qquad r(x) = |g(x) - k| \implies V = \pi \int_a^b \Big( [R(x)]^2 - [r(x)]^2 \Big) \, dx$$
</div>
<p>Similarly, for rotation about a vertical line $x = h$ using horizontal slices perpendicular to the axis of rotation:</p>
<div class="math-display">
$$V = \pi \int_c^d \Big( [R(y)]^2 - [r(y)]^2 \Big) \, dy$$
</div>"""
    },
    {
        "id": "u3-sec3",
        "title": "Volumes of Revolution: The Method of Cylindrical Shells",
        "content": r"""<h4>1. When Washer Integration is Pathological</h4>
<p>When solving for $x$ in terms of $y$ is algebraically intractable (e.g., $y = 3x^2 - 2x^5$) or requires decomposing the domain into difficult sub-regions, revolving about a vertical axis is vastly superior using <strong>cylindrical shells</strong> parallel to the axis of revolution.</p>

<h4>2. Unrolling the Differential Cylindrical Shell</h4>
<p>Consider revolving a thin vertical strip of width $dx$ at distance $x$ from the vertical axis of rotation $x = 0$, having height $h(x) = f(x) - g(x)$. When revolved through $2\pi$, this strip traces a thin hollow cylindrical shell of radius $r = x$, height $h = f(x) - g(x)$, and wall thickness $dx$.</p>
<p>Unrolling this shell into a flat rectangular prism yields the volume element:</p>
<div class="math-display">
$$dV = (\text{Circumference}) \times (\text{Height}) \times (\text{Thickness}) = 2\pi x \cdot h(x) \cdot dx$$
</div>
<div class="math-display">
$$\mathbf{V = 2\pi \int_a^b x \Big( f(x) - g(x) \Big) \, dx}$$
</div>

<h4>3. General Axis of Rotation ($x = h$)</h4>
<p>If the axis of rotation is the vertical line $x = h$:</p>
<div class="math-display">
$$\text{Radius } r(x) = |x - h| \implies \mathbf{V = 2\pi \int_a^b |x - h| \Big( f(x) - g(x) \Big) \, dx}$$
</div>
<p>For horizontal axis rotation revolving about $y = k$ with horizontal strips of thickness $dy$:</p>
<div class="math-display">
$$\mathbf{V = 2\pi \int_c^d |y - k| \Big( w_R(y) - w_L(y) \Big) \, dy}$$
</div>"""
    },
    {
        "id": "u3-sec4",
        "title": "Volumes by Slicing with General Cross-Sections & Cavalieri's Principle",
        "content": r"""<h4>1. Cavalieri's Principle</h4>
<p>If two three-dimensional solids have the same height and equal cross-sectional areas at every cutting plane parallel to their bases, then their total volumes are identical.</p>

<h4>2. General Volume by Parallel Slicing</h4>
<p>Let a solid extend along the $x$-axis from $x = a$ to $x = b$. If the area of the cross-section perpendicular to the $x$-axis at point $x$ is given by a continuous function $A(x)$, the differential slab volume is $dV = A(x) \, dx$:</p>
<div class="math-display">
$$\mathbf{V = \int_a^b A(x) \, dx}$$
</div>

<h4>3. Common Cross-Sectional Geometry over a Planar Base</h4>
<p>Suppose the base of a solid is bounded between $y = f(x)$ and $y = g(x)$, so the cross-sectional base length is $s(x) = f(x) - g(x)$. Standard geometric cross-sections perpendicular to the $x$-axis have areas:</p>
<ul>
  <li><strong>Squares:</strong> $A(x) = [s(x)]^2$</li>
  <li><strong>Equilateral Triangles:</strong> $A(x) = \frac{\sqrt{3}}{4} [s(x)]^2$</li>
  <li><strong>Semicircles with diameter $s(x)$:</strong> $A(x) = \frac{\pi}{8} [s(x)]^2$</li>
  <li><strong>Isosceles Right Triangles (hypotenuse on base):</strong> $A(x) = \frac{1}{4} [s(x)]^2$</li>
</ul>"""
    },
    {
        "id": "u3-sec5",
        "title": "Arc Length of Smooth Curves, Surface Areas of Revolution & Pappus's Theorems",
        "content": r"""<h4>1. Differential Arc Length Element $ds$</h4>
<p>By the Pythagorean theorem applied to an infinitesimal segment on a smooth curve $y = f(x) \in C^1([a, b])$:</p>
<div class="math-display">
$$(ds)^2 = (dx)^2 + (dy)^2 = (dx)^2 \left( 1 + \left(\frac{dy}{dx}\right)^2 \right) \implies ds = \sqrt{1 + [f'(x)]^2} \, dx$$
</div>
<p>The total <strong>Arc Length</strong> of the curve from $x = a$ to $x = b$ is:</p>
<div class="math-display">
$$\mathbf{L = \int_a^b \sqrt{1 + [f'(x)]^2} \, dx}$$
</div>
<p>For a parametric curve $(x(t), y(t))$ for $t \in [t_0, t_1]$, $ds = \sqrt{\dot{x}(t)^2 + \dot{y}(t)^2} \, dt$, so $L = \int_{t_0}^{t_1} \sqrt{\dot{x}^2 + \dot{y}^2} \, dt$.</p>

<h4>2. Area of a Surface of Revolution</h4>
<p>Revolving the differential arc element $ds$ about an axis sweeps a frustum of a cone of surface area $dS = 2\pi r \, ds$, where $r$ is the perpendicular distance from the curve to the axis of rotation:</p>
<ul>
  <li><strong>Rotation About the $x$-axis ($r = y = f(x)$):</strong>
    $$\mathbf{S = 2\pi \int_a^b f(x) \sqrt{1 + [f'(x)]^2} \, dx}$$
  </li>
  <li><strong>Rotation About the $y$-axis ($r = x$):</strong>
    $$\mathbf{S = 2\pi \int_a^b x \sqrt{1 + [f'(x)]^2} \, dx}$$
  </li>
</ul>

<h4>3. The Centroid Theorems of Pappus</h4>
<p>Let a planar curve of length $L$ and centroid distance $\bar{y}$ from an axis in its plane (not crossing the curve) be revolved through $2\pi$:</p>
<div class="math-display">
$$\mathbf{S = 2\pi \bar{y} L}$$
</div>
<p>Let a planar region of area $A$ and centroid distance $\bar{y}$ be revolved through $2\pi$:</p>
<div class="math-display">
$$\mathbf{V = 2\pi \bar{y} A}$$
</div>"""
    }
]

u3_problems = [
    {
        "id": "calc2-p3-1",
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Cylindrical Shells vs Washer Method Verification",
        "statement": r"""Find the volume of the solid generated by revolving the region bounded by $y = \sqrt{x}$, the $x$-axis ($y = 0$), and the line $x = 4$ about the line $x = 6$ using the method of cylindrical shells.""",
        "solution": r"""<h4>Step 1: Identify Shell Geometry</h4>
<p>The region is bounded for $x \in [0, 4]$. A vertical strip at position $x$ has:</p>
<ul>
  <li><strong>Height:</strong> $h(x) = \sqrt{x} - 0 = \sqrt{x}$</li>
  <li><strong>Radius of rotation:</strong> The distance from $x$ to the rotation line $x = 6$ is $r(x) = 6 - x$</li>
  <li><strong>Thickness:</strong> $dx$</li>
</ul>

<h4>Step 2: Formulate the Shell Volume Integral</h4>
<div class="math-display">
$$V = 2\pi \int_0^4 r(x) h(x) \, dx = 2\pi \int_0^4 (6 - x)\sqrt{x} \, dx = 2\pi \int_0^4 \Big( 6x^{1/2} - x^{3/2} \Big) dx$$
</div>

<h4>Step 3: Evaluate the Antiderivative</h4>
<div class="math-display">
$$\begin{aligned}
V &= 2\pi \left[ 6 \cdot \frac{2}{3} x^{3/2} - \frac{2}{5} x^{5/2} \right]_0^4 = 2\pi \left[ 4 x^{3/2} - \frac{2}{5} x^{5/2} \right]_0^4 \\
&= 2\pi \left( 4(4^{3/2}) - \frac{2}{5}(4^{5/2}) \right) = 2\pi \left( 4(8) - \frac{2}{5}(32) \right) \\
&= 2\pi \left( 32 - \frac{64}{5} \right) = 2\pi \left( \frac{160 - 64}{5} \right) = 2\pi \left( \frac{96}{5} \right) = \frac{192\pi}{5}
\end{aligned}$$
</div>""",
        "answer": r"""$V = \frac{192\pi}{5}$"""
    },
    {
        "id": "calc2-p3-2",
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Arc Length and Surface Area of the Catenary",
        "statement": r"""Consider the catenary curve $y = a \cosh(x/a)$ on the symmetric interval $[-a, a]$.
(a) Compute the exact arc length $L$ of this catenary arc.
(b) Compute the surface area $S$ generated by revolving this catenary about the $x$-axis.""",
        "solution": r"""<h4>Part (a): Compute the Arc Length $L$</h4>
<p>Differentiating $y = a\cosh(x/a)$ with respect to $x$:</p>
<div class="math-display">
$$y' = a \cdot \frac{1}{a} \sinh(x/a) = \sinh(x/a)$$
</div>
<p>Using the fundamental hyperbolic identity $1 + \sinh^2(u) = \cosh^2(u)$:</p>
<div class="math-display">
$$ds = \sqrt{1 + (y')^2} \, dx = \sqrt{1 + \sinh^2(x/a)} \, dx = \cosh(x/a) \, dx$$
</div>
<p>Integrating from $-a$ to $a$ (using symmetry about $x = 0$):</p>
<div class="math-display">
$$L = \int_{-a}^a \cosh(x/a) \, dx = 2 \int_0^a \cosh(x/a) \, dx = 2 \Big[ a \sinh(x/a) \Big]_0^a = 2a \sinh(1)$$
</div>

<h4>Part (b): Surface Area of Revolution about $x$-axis</h4>
<p>The differential surface area element is $dS = 2\pi y \, ds$:</p>
<div class="math-display">
$$dS = 2\pi \Big( a \cosh(x/a) \Big) \Big( \cosh(x/a) \, dx \Big) = 2\pi a \cosh^2(x/a) \, dx$$
</div>
<p>Applying the hyperbolic power-reduction identity $\cosh^2(u) = \frac{\cosh(2u) + 1}{2}$:</p>
<div class="math-display">
$$\begin{aligned}
S &= 2\pi a \int_{-a}^a \left( \frac{\cosh(2x/a) + 1}{2} \right) dx = 2\pi a \int_0^a \Big( \cosh(2x/a) + 1 \Big) dx \\
&= 2\pi a \left[ \frac{a}{2}\sinh(2x/a) + x \right]_0^a = 2\pi a \left( \frac{a}{2}\sinh(2) + a \right) = \pi a^2 \Big( \sinh(2) + 2 \Big)
\end{aligned}$$
</div>""",
        "answer": r"""$L = 2a\sinh(1)$, \quad $S = \pi a^2 (\sinh(2) + 2)$"""
    },
    {
        "id": "calc2-p3-3",
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Gabriel's Horn (Torricelli's Trumpet) Paradox",
        "statement": r"""Consider the curve $y = \frac{1}{x}$ for $x \in [1, \infty)$ revolved about the $x$-axis.
(a) Prove that the resulting solid has finite volume $V = \pi$.
(b) Prove that its surface area $S$ is strictly infinite ($S \to \infty$).
(c) Resolve the physical painter's paradox: How can a horn hold a finite volume of paint ($\pi$ units) yet require an infinite amount of paint to coat its inner surface?""",
        "solution": r"""<h4>Part (a): Volume Evaluation</h4>
<p>Using the disk method with $R(x) = \frac{1}{x}$ on $[1, \infty)$:</p>
<div class="math-display">
$$V = \pi \int_1^\infty [R(x)]^2 \, dx = \pi \lim_{M \to \infty} \int_1^M \frac{1}{x^2} \, dx = \pi \lim_{M \to \infty} \left[ -\frac{1}{x} \right]_1^M = \pi \lim_{M \to \infty} \left( 1 - \frac{1}{M} \right) = \mathbf{\pi}$$
</div>
<p>The volume is strictly finite and equal to $\pi$.</p>

<h4>Part (b): Surface Area Divergence Proof</h4>
<p>The derivative is $y' = -\frac{1}{x^2}$. The surface area is:</p>
<div class="math-display">
$$S = 2\pi \int_1^\infty y \sqrt{1 + (y')^2} \, dx = 2\pi \int_1^\infty \frac{1}{x} \sqrt{1 + \frac{1}{x^4}} \, dx$$
</div>
<p>Since $\sqrt{1 + \frac{1}{x^4}} > 1$ for all $x \ge 1$:</p>
<div class="math-display">
$$S > 2\pi \int_1^\infty \frac{1}{x} \, dx = 2\pi \lim_{M \to \infty} \Big[ \ln(x) \Big]_1^M = 2\pi \lim_{M \to \infty} \ln(M) = \mathbf{\infty}$$
</div>
<p>By the Direct Comparison Test, the surface area $S$ diverges to infinity.</p>

<h4>Part (c): Resolution of the Painter's Paradox</h4>
<p>The paradox arises from treating "paint" as a mathematical zero-thickness 2D coating versus a physical 3D fluid with non-zero molecular thickness $\delta > 0$:</p>
<ol>
  <li>In physical reality, paint molecules have a finite non-zero diameter $\delta$. Once the neck of the trumpet narrows such that the radius $r(x) = 1/x < \delta$ (i.e. for $x > 1/\delta$), no paint molecules can enter the throat, making it physically impossible to coat the entire infinite surface.</li>
  <li>Mathematically, the volume of a 3D coating of constant normal thickness $\delta$ is an integral over an expanded 3D shell, which itself diverges to infinity. Thus, a finite volume of paint can only produce a coating whose thickness vanishes as $x \to \infty$ at a rate faster than $1/x$, which is impossible for physical matter.</li>
</ol>""",
        "answer": r"""$V = \pi$ (finite), while $S = \infty$ (divergent); resolved because physical paint has finite molecular thickness $\delta > 0$."""
    }
]

u3_data = {
    "id": "unit3",
    "unit_number": 3,
    "title": "Geometric Applications of Integration in Cartesian Coordinates",
    "subtitle": "Plane Areas, Disks & Washers, Cylindrical Shells, Arc Length & Gabriel's Horn",
    "sections": u3_sections,
    "simulations": ["sim_calc2_solids"],
    "problems": u3_problems
}


# ==========================================
# UNIT 4: POLAR COORDINATES & GEOMETRIC APPLICATIONS
# ==========================================
u4_sections = [
    {
        "id": "u4-sec1",
        "title": "The Polar Coordinate Frame & Classical Curve Tracing",
        "content": r"""<h4>1. Coordinate Transformation Equations</h4>
<p>In the plane $\mathbb{R}^2$, a point $P$ is determined by its directed distance $r$ from the origin (pole) and counterclockwise angle $\theta$ from the positive horizontal axis (polar axis):</p>
<div class="math-display">
$$x = r \cos\theta, \qquad y = r \sin\theta \quad \Longleftrightarrow \quad r^2 = x^2 + y^2, \qquad \tan\theta = \frac{y}{x}$$
</div>

<h4>2. Symmetry Criteria for Polar Curves $r = f(\theta)$</h4>
<ol>
  <li><strong>Symmetry about Polar Axis (Horizontal Axis):</strong> The equation is unchanged when replacing $(r, \theta)$ with $(r, -\theta)$ or $(-r, \pi - \theta)$.</li>
  <li><strong>Symmetry about Normal Axis $\theta = \pi/2$ (Vertical Axis):</strong> The equation is unchanged when replacing $(r, \theta)$ with $(r, \pi - \theta)$ or $(-r, -\theta)$.</li>
  <li><strong>Symmetry about the Pole (Origin):</strong> The equation is unchanged when replacing $(r, \theta)$ with $(-r, \theta)$ or $(r, \theta + \pi)$.</li>
</ol>

<h4>3. Zoology of Classical Polar Curves</h4>
<ul>
  <li><strong>Cardioids:</strong> $r = a(1 \pm \cos\theta)$ or $r = a(1 \pm \sin\theta)$ ($a > 0$). Heart-shaped curves passing through the pole with a cusp at $r = 0$.</li>
  <li><strong>Limaçons:</strong> $r = a + b\cos\theta$. If $a < b$, it features an inner loop; if $a = b$, it is a cardioid; if $a > b$, it is dimpled or convex.</li>
  <li><strong>Rose Curves:</strong> $r = a\cos(n\theta)$ or $r = a\sin(n\theta)$. If $n \in \mathbb{N}$ is odd, the curve has $n$ petals; if $n$ is even, the curve has $2n$ petals.</li>
  <li><strong>Lemniscates:</strong> $r^2 = a^2\cos(2\theta)$. Figure-eight curves with nodal tangents at $\theta = \pm \pi/4$.</li>
</ul>"""
    },
    {
        "id": "u4-sec2",
        "title": "Tangents to Polar Curves & Angle Between Radius Vector and Tangent",
        "content": r"""<h4>1. Slope of the Cartesian Tangent $\frac{dy}{dx}$</h4>
<p>Treating $\theta$ as a parametric variable with $x(\theta) = r(\theta)\cos\theta$ and $y(\theta) = r(\theta)\sin\theta$:</p>
<div class="math-display">
$$\frac{dx}{d\theta} = \frac{dr}{d\theta}\cos\theta - r\sin\theta, \qquad \frac{dy}{d\theta} = \frac{dr}{d\theta}\sin\theta + r\cos\theta$$
</div>
<div class="math-display">
$$\mathbf{\frac{dy}{dx} = \frac{\frac{dy}{d\theta}}{\frac{dx}{d\theta}} = \frac{\frac{dr}{d\theta}\sin\theta + r\cos\theta}{\frac{dr}{d\theta}\cos\theta - r\sin\theta}}$$
</div>

<h4>2. The Polar Angle $\psi$ (Angle Between Radius Vector and Tangent)</h4>
<p>Let $\phi$ be the inclination angle of the tangent line with the polar axis ($\tan\phi = \frac{dy}{dx}$) and $\theta$ be the vectorial angle of $P$. The angle $\psi = \phi - \theta$ between the radius vector $OP$ and the tangent line satisfies:</p>
<div class="math-display">
$$\tan\psi = \tan(\phi - \theta) = \frac{\tan\phi - \tan\theta}{1 + \tan\phi \tan\theta}$$
</div>
<p>Substituting $\tan\phi = \frac{r' \sin\theta + r \cos\theta}{r' \cos\theta - r \sin\theta}$ and $\tan\theta = \frac{\sin\theta}{\cos\theta}$:</p>
<div class="math-display">
$$\tan\psi = \frac{\frac{r' \sin\theta + r \cos\theta}{r' \cos\theta - r \sin\theta} - \frac{\sin\theta}{\cos\theta}}{1 + \left(\frac{r' \sin\theta + r \cos\theta}{r' \cos\theta - r \sin\theta}\right)\frac{\sin\theta}{\cos\theta}} = \frac{r(\cos^2\theta + \sin^2\theta)}{r'(\cos^2\theta + \sin^2\theta)} = \frac{r}{r'}$$
</div>
<div class="math-display">
$$\mathbf{\tan\psi = \frac{r}{\frac{dr}{d\theta}} = r \frac{d\theta}{dr}}$$
</div>
<p>This remarkably elegant identity proves that the geometry of polar tangents depends solely on $r$ and its angular rate of change.</p>"""
    },
    {
        "id": "u4-sec3",
        "title": "Areas Enclosed by Polar Curves & Multi-Looped Sectors",
        "content": r"""<h4>1. Derivation of the Polar Area Element</h4>
<p>Consider an infinitesimal sector between rays $\theta$ and $\theta + d\theta$ bounded by $r = f(\theta)$. Approximating this sector by a circular sector of radius $r$ and central angle $d\theta$:</p>
<div class="math-display">
$$dA = \frac{1}{2} r^2 \, d\theta$$
</div>
<p>Integrating from $\theta = \alpha$ to $\theta = \beta$ yields the total swept area:</p>
<div class="math-display">
$$\mathbf{A = \frac{1}{2} \int_\alpha^\beta [r(\theta)]^2 \, d\theta}$$
</div>

<h4>2. Area Between Two Polar Curves</h4>
<p>If $r_{\text{outer}}(\theta) \ge r_{\text{inner}}(\theta) \ge 0$ for $\theta \in [\alpha, \beta]$:</p>
<div class="math-display">
$$\mathbf{A = \frac{1}{2} \int_\alpha^\beta \Big( [r_{\text{outer}}(\theta)]^2 - [r_{\text{inner}}(\theta)]^2 \Big) \, d\theta}$$
</div>

<h4>3. Critical Precaution: Multi-Loop & Overlapping Limits</h4>
<p>For rose curves $r = a\cos(n\theta)$, a single petal is bounded between adjacent roots where $r = 0$. For $r = a\cos(2\theta)$, setting $2\theta = \pm \frac{\pi}{2} \implies \theta \in [-\frac{\pi}{4}, \frac{\pi}{4}]$ bounds exactly one petal. Integrating over $[0, 2\pi]$ directly without symmetry can count overlapping loops multiple times.</p>"""
    },
    {
        "id": "u4-sec4",
        "title": "Arc Length in Polar Coordinates",
        "content": r"""<h4>1. Analytical Derivation of $ds$</h4>
<p>Recall $dx = (r'\cos\theta - r\sin\theta)d\theta$ and $dy = (r'\sin\theta + r\cos\theta)d\theta$. Squaring and summing:</p>
<div class="math-display">
$$\begin{aligned}
(dx)^2 + (dy)^2 &= \left[ (r')^2 \cos^2\theta - 2r r' \sin\theta\cos\theta + r^2 \sin^2\theta \right] (d\theta)^2 \\
&\quad + \left[ (r')^2 \sin^2\theta + 2r r' \sin\theta\cos\theta + r^2 \cos^2\theta \right] (d\theta)^2 \\
&= \Big( r^2 (\sin^2\theta + \cos^2\theta) + (r')^2 (\sin^2\theta + \cos^2\theta) \Big) (d\theta)^2 \\
&= \left( r^2 + \left(\frac{dr}{d\theta}\right)^2 \right) (d\theta)^2
\end{aligned}$$
</div>
<div class="math-display">
$$\mathbf{ds = \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} \, d\theta}$$
</div>

<h4>2. Total Arc Length Integral</h4>
<div class="math-display">
$$\mathbf{L = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} \, d\theta}$$
</div>"""
    },
    {
        "id": "u4-sec5",
        "title": "Surfaces and Volumes of Revolution in Polar Coordinates",
        "content": r"""<h4>1. Revolution About the Polar Axis ($x$-axis)</h4>
<p>When revolving about the polar axis ($y = 0$), the perpendicular distance to the rotation axis is $y = r\sin\theta$.</p>
<ul>
  <li><strong>Surface Area of Revolution:</strong>
    $$\mathbf{S = 2\pi \int_\alpha^\beta r\sin\theta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} \, d\theta}$$
  </li>
  <li><strong>Volume of Revolution:</strong> Revolving differential triangular sectors $dA$ gives conical rings:
    $$\mathbf{V = \frac{2}{3}\pi \int_\alpha^\beta r^3 \sin\theta \, d\theta}$$
  </li>
</ul>

<h4>2. Revolution About the Normal Axis $\theta = \pi/2$ ($y$-axis)</h4>
<p>The perpendicular distance is $x = r\cos\theta$:</p>
<div class="math-display">
$$\mathbf{S = 2\pi \int_\alpha^\beta r\cos\theta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} \, d\theta}$$
</div>"""
    }
]

u4_problems = [
    {
        "id": "calc2-p4-1",
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Tangent and Radius Angle for the Cardioid",
        "statement": r"""For the cardioid $r = 2(1 + \cos\theta)$:
(a) Find the angle $\psi$ between the radius vector and the tangent line at $\theta = \frac{\pi}{3}$.
(b) Find the Cartesian slope $\frac{dy}{dx}$ of the tangent line at this point.""",
        "solution": r"""<h4>Part (a): Compute the Angle $\psi$</h4>
<p>Differentiating $r = 2(1 + \cos\theta)$ with respect to $\theta$:</p>
<div class="math-display">
$$\frac{dr}{d\theta} = -2\sin\theta$$
</div>
<p>Using the polar tangent identity $\tan\psi = \frac{r}{dr/d\theta}$:</p>
<div class="math-display">
$$\tan\psi = \frac{2(1 + \cos\theta)}{-2\sin\theta} = -\frac{2\cos^2(\theta/2)}{2\sin(\theta/2)\cos(\theta/2)} = -\cot\left(\frac{\theta}{2}\right) = \tan\left( \frac{\pi}{2} + \frac{\theta}{2} \right)$$
</div>
<p>Thus, $\psi = \frac{\pi}{2} + \frac{\theta}{2}$. Evaluating at $\theta = \frac{\pi}{3}$:</p>
<div class="math-display">
$$\psi = \frac{\pi}{2} + \frac{\pi/3}{2} = \frac{\pi}{2} + \frac{\pi}{6} = \frac{2\pi}{3} = 120^\circ$$
</div>

<h4>Part (b): Compute the Cartesian Slope $\frac{dy}{dx}$</h4>
<p>The inclination angle of the tangent is $\phi = \theta + \psi = \frac{\pi}{3} + \frac{2\pi}{3} = \pi$.</p>
<p>Therefore, the Cartesian slope is:</p>
<div class="math-display">
$$\frac{dy}{dx} = \tan\phi = \tan(\pi) = \mathbf{0}$$
</div>
<p>The tangent line to the cardioid at $\theta = \frac{\pi}{3}$ is perfectly horizontal.</p>""",
        "answer": r"""$\psi = \frac{2\pi}{3}$ ($120^\circ$); \quad $\frac{dy}{dx} = 0$ (horizontal tangent)"""
    },
    {
        "id": "calc2-p4-2",
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Area and Perimeter of a Rose Petal",
        "statement": r"""Consider the four-petaled rose $r = 4\cos(2\theta)$.
(a) Find the exact area of one complete petal.
(b) Find the total area enclosed by all four petals.""",
        "solution": r"""<h4>Part (a): Area of One Petal</h4>
<p>The tip of the petal on the positive polar axis occurs at $\theta = 0$ where $r = 4$. The boundaries of this petal occur where $r = 0$:</p>
<div class="math-display">
$$\cos(2\theta) = 0 \implies 2\theta = \pm \frac{\pi}{2} \implies \theta = -\frac{\pi}{4} \text{ and } \theta = \frac{\pi}{4}$$
</div>
<p>The area of this petal is:</p>
<div class="math-display">
$$A_{\text{petal}} = \frac{1}{2} \int_{-\pi/4}^{\pi/4} [4\cos(2\theta)]^2 \, d\theta = \frac{16}{2} \int_{-\pi/4}^{\pi/4} \cos^2(2\theta) \, d\theta = 8 \int_{-\pi/4}^{\pi/4} \left( \frac{1 + \cos(4\theta)}{2} \right) d\theta$$
</div>
<div class="math-display">
$$A_{\text{petal}} = 4 \left[ \theta + \frac{\sin(4\theta)}{4} \right]_{-\pi/4}^{\pi/4} = 4 \left( \left(\frac{\pi}{4} + 0\right) - \left(-\frac{\pi}{4} + 0\right) \right) = 4\left(\frac{\pi}{2}\right) = \mathbf{2\pi}$$
</div>

<h4>Part (b): Total Area of All Four Petals</h4>
<p>By fourfold rotational symmetry, the total enclosed area is:</p>
<div class="math-display">
$$A_{\text{total}} = 4 \times A_{\text{petal}} = 4 \times 2\pi = \mathbf{8\pi}$$
</div>""",
        "answer": r"""$A_{\text{petal}} = 2\pi$; \quad $A_{\text{total}} = 8\pi$"""
    },
    {
        "id": "calc2-p4-3",
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Total Perimeter and Surface Area of the Revolved Cardioid",
        "statement": r"""For the complete cardioid $r = a(1 + \cos\theta)$ ($a > 0$):
(a) Prove that its total perimeter is $L = 8a$.
(b) Find the total surface area generated by revolving this cardioid about the initial polar axis.""",
        "solution": r"""<h4>Part (a): Total Perimeter of the Cardioid</h4>
<p>We compute $r' = -a\sin\theta$. The arc length element is:</p>
<div class="math-display">
$$\begin{aligned}
ds &= \sqrt{r^2 + (r')^2} \, d\theta = \sqrt{a^2(1 + \cos\theta)^2 + a^2\sin^2\theta} \, d\theta \\
&= a \sqrt{1 + 2\cos\theta + \cos^2\theta + \sin^2\theta} \, d\theta = a \sqrt{2 + 2\cos\theta} \, d\theta \\
&= a \sqrt{4\cos^2(\theta/2)} \, d\theta = 2a |\cos(\theta/2)| \, d\theta
\end{aligned}$$
</div>
<p>Using symmetry about the polar axis, integrate from $\theta = 0$ to $\pi$ where $\cos(\theta/2) \ge 0$:</p>
<div class="math-display">
$$L = 2 \int_0^\pi 2a \cos(\theta/2) \, d\theta = 4a \Big[ 2\sin(\theta/2) \Big]_0^\pi = 8a \Big( \sin(\pi/2) - 0 \Big) = \mathbf{8a} \quad \blacksquare$$
</div>

<h4>Part (b): Surface Area Revolved About the Polar Axis</h4>
<p>The surface area element is $dS = 2\pi y \, ds = 2\pi (r\sin\theta) ds$:</p>
<div class="math-display">
$$dS = 2\pi \Big( a(1 + \cos\theta)\sin\theta \Big) \Big( 2a\cos(\theta/2) \, d\theta \Big)$$
</div>
<p>Using $1 + \cos\theta = 2\cos^2(\theta/2)$ and $\sin\theta = 2\sin(\theta/2)\cos(\theta/2)$:</p>
<div class="math-display">
$$dS = 2\pi a^2 \left( 2\cos^2\frac{\theta}{2} \right) \left( 2\sin\frac{\theta}{2}\cos\frac{\theta}{2} \right) \left( 2\cos\frac{\theta}{2} \right) d\theta = 16\pi a^2 \cos^4\left(\frac{\theta}{2}\right)\sin\left(\frac{\theta}{2}\right) d\theta$$
</div>
<p>Integrating over $\theta \in [0, \pi]$ with substitution $u = \cos(\theta/2) \implies du = -\frac{1}{2}\sin(\theta/2)d\theta$:</p>
<div class="math-display">
$$S = 16\pi a^2 \int_0^\pi \cos^4\left(\frac{\theta}{2}\right) \sin\left(\frac{\theta}{2}\right) d\theta = 16\pi a^2 \int_0^1 u^4 (2 du) = 32\pi a^2 \left[ \frac{u^5}{5} \right]_0^1 = \mathbf{\frac{32}{5}\pi a^2}$$
</div>""",
        "answer": r"""$L = 8a$; \quad $S = \frac{32}{5}\pi a^2$"""
    }
]

u4_data = {
    "id": "unit4",
    "unit_number": 4,
    "title": "Graphing in Polar Coordinates & Geometric Applications",
    "subtitle": "Cardioids, Limaçons, Rose Curves, Polar Tangents, Sector Areas & Revolved Surfaces",
    "sections": u4_sections,
    "simulations": ["sim_calc2_polar"],
    "problems": u4_problems
}

# Write files
with open("calc2_u3.json", "w", encoding="utf-8") as f:
    json.dump(u3_data, f, indent=2, ensure_ascii=False)
print("Saved calc2_u3.json successfully.")

with open("calc2_u4.json", "w", encoding="utf-8") as f:
    json.dump(u4_data, f, indent=2, ensure_ascii=False)
print("Saved calc2_u4.json successfully.")
