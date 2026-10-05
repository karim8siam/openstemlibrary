# -*- coding: utf-8 -*-
"""
Builder for 2D Geometry Units 5 to 8:
Unit 5: In-Depth Study of the Parabola
Unit 6: In-Depth Study of the Ellipse
Unit 7: In-Depth Study of the Hyperbola & Rectangular Hyperbola
Unit 8: Polar Equations of Conics & Celestial Orbital Geometry
"""
import json

# -------------------------------------------------------------
# UNIT 5
# -------------------------------------------------------------
u5_sections = [
    {
        "id": "u5-sec1",
        "title": "The Parabola: Focus-Directrix Definition, Canonical Forms & Latus Rectum",
        "content": r"""
<h3>1. The Focus-Directrix Locus Definition</h3>
<p>
A <strong>parabola</strong> is defined geometrically as the planar locus of a point $P(x, y)$ that moves such that its distance from a fixed point $S$ (the <em>focus</em>) is strictly equal to its perpendicular distance from a fixed straight line $D$ (the <em>directrix</em>):
$$\frac{SP}{PM} = e = 1 \iff SP = PM$$
where $M$ is the foot of the perpendicular from $P$ to directrix $D$.
</p>
<p>
To derive the canonical Cartesian equation:
<ol>
  <li>Choose the focus at $S(a, 0)$ with $a > 0$.</li>
  <li>Choose the directrix as the vertical line $D: x + a = 0 \iff x = -a$.</li>
  <li>The point $M$ has coordinates $(-a, y)$.</li>
  <li>Equating distances:
  $$SP^2 = PM^2 \implies (x - a)^2 + (y - 0)^2 = (x - (-a))^2 + (y - y)^2$$
  $$x^2 - 2ax + a^2 + y^2 = (x + a)^2 = x^2 + 2ax + a^2$$
  Canceling $x^2 + a^2$ on both sides yields the classical canonical equation:
  $$\mathbf{y^2 = 4ax}$$
  </li>
</ol>
</p>

<h3>2. Geometric Elements of the Standard Parabola ($y^2 = 4ax$)</h3>
<p>
<ul>
  <li><strong>Vertex ($V$):</strong> The origin $V(0, 0)$, midpoint of the perpendicular from focus to directrix.</li>
  <li><strong>Axis of Symmetry:</strong> The $x$-axis ($y = 0$). The curve is symmetric about this line because $y = \pm 2\sqrt{ax}$.</li>
  <li><strong>Focus ($S$):</strong> $S(a, 0)$.</li>
  <li><strong>Directrix ($D$):</strong> The vertical line $x = -a$.</li>
  <li><strong>Focal Distance:</strong> For any point $P(x_1, y_1)$ on the curve:
  $$SP = x_1 + a$$</li>
  <li><strong>Latus Rectum ($LL'$):</strong> The focal chord perpendicular to the axis of symmetry. Substituting $x = a$ into $y^2 = 4ax$ yields $y^2 = 4a^2 \implies y = \pm 2a$.
  The extremities are $L(a, 2a)$ and $L'(a, -2a)$, and its total length is:
  $$\mathbf{Length(LL') = 4a}$$</li>
</ul>
</p>

<h3>3. Canonical Orientations of the Parabola</h3>
<p>
Depending on the direction of opening and orientation of the axis:
<table style="width:100%; border-collapse:collapse; margin:16px 0; font-size:0.95em;">
<thead>
<tr style="border-bottom:2px solid var(--border-color); text-align:left;">
<th style="padding:8px;">Equation</th>
<th style="padding:8px;">Axis</th>
<th style="padding:8px;">Opens</th>
<th style="padding:8px;">Focus</th>
<th style="padding:8px;">Directrix</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid var(--border-color);"><td style="padding:8px;">$y^2 = 4ax$</td><td style="padding:8px;">$y = 0$</td><td style="padding:8px;">Right ($x \ge 0$)</td><td style="padding:8px;">$(a, 0)$</td><td style="padding:8px;">$x = -a$</td></tr>
<tr style="border-bottom:1px solid var(--border-color);"><td style="padding:8px;">$y^2 = -4ax$</td><td style="padding:8px;">$y = 0$</td><td style="padding:8px;">Left ($x \le 0$)</td><td style="padding:8px;">$(-a, 0)$</td><td style="padding:8px;">$x = a$</td></tr>
<tr style="border-bottom:1px solid var(--border-color);"><td style="padding:8px;">$x^2 = 4ay$</td><td style="padding:8px;">$x = 0$</td><td style="padding:8px;">Upward ($y \ge 0$)</td><td style="padding:8px;">$(0, a)$</td><td style="padding:8px;">$y = -a$</td></tr>
<tr><td style="padding:8px;">$x^2 = -4ay$</td><td style="padding:8px;">$x = 0$</td><td style="padding:8px;">Downward ($y \le 0$)</td><td style="padding:8px;">$(0, -a)$</td><td style="padding:8px;">$y = a$</td></tr>
</tbody>
</table>
</p>
"""
    },
    {
        "id": "u5-sec2",
        "title": "Parametric Representation & Focal Chord Geometry",
        "content": r"""
<h3>1. The Standard Rational Parametrization</h3>
<p>
The equation $y^2 = 4ax$ can be parametrized rationally without radicals by setting $y = 2at$:
$$(2at)^2 = 4ax \implies 4a^2 t^2 = 4ax \implies x = at^2$$
Thus, any point on the parabola is uniquely identified by the real parameter $t \in \mathbb{R}$:
$$P(t) = (a t^2, 2 a t)$$
Notice that the parameter $t$ is the reciprocal of the slope of the tangent at $P$ ($m = 1/t$).
</p>

<h3>2. Chord Joining Two Points & The Focal Chord Theorem</h3>
<p>
Let $P(t_1) = (a t_1^2, 2 a t_1)$ and $Q(t_2) = (a t_2^2, 2 a t_2)$ be two distinct points on the parabola. The slope of the secant chord $PQ$ is:
$$m_{PQ} = \frac{2a t_2 - 2a t_1}{a t_2^2 - a t_1^2} = \frac{2a(t_2 - t_1)}{a(t_2 - t_1)(t_2 + t_1)} = \frac{2}{t_1 + t_2}$$
The equation of the chord $PQ$ in point-slope form is:
$$y - 2a t_1 = \frac{2}{t_1 + t_2}(x - a t_1^2) \iff (t_1 + t_2)y = 2x + 2a t_1 t_2$$
</p>
<p>
<strong>The Fundamental Focal Chord Condition:</strong>
If the chord $PQ$ passes through the focus $S(a, 0)$, substituting $x = a, y = 0$ yields:
$$(t_1 + t_2)(0) = 2a + 2a t_1 t_2 \implies 2a(1 + t_1 t_2) = 0 \iff \mathbf{t_1 t_2 = -1 \iff t_2 = -\frac{1}{t_1}}$$
This theorem leads to two crucial geometric properties:
<ul>
  <li><strong>Harmonic Mean Property:</strong> The semi-latus rectum $2a$ is the harmonic mean of the two focal segments $SP$ and $SQ$:
  $$SP = a(t_1^2 + 1), \quad SQ = a(t_2^2 + 1) = a\left(\frac{1}{t_1^2} + 1\right) = a\frac{t_1^2 + 1}{t_1^2}$$
  $$\frac{1}{SP} + \frac{1}{SQ} = \frac{1}{a(t_1^2 + 1)} + \frac{t_1^2}{a(t_1^2 + 1)} = \frac{1 + t_1^2}{a(1 + t_1^2)} = \frac{1}{a} \iff \mathbf{\frac{2}{PQ_{\text{harm}}} = \frac{1}{a}}$$</li>
  <li><strong>Total Length of Focal Chord:</strong>
  $$PQ = SP + SQ = a\left(t_1 + \frac{1}{t_1}\right)^2 \ge 4a$$
  with minimum length $4a$ occurring when $t_1 = 1$ (the latus rectum).</li>
</ul>
</p>
"""
    },
    {
        "id": "u5-sec3",
        "title": "Tangents to the Parabola: Point, Slope & Parametric Forms",
        "content": r"""
<h3>1. The Three Canonical Forms of Tangents</h3>
<p>
For the parabola $y^2 = 4ax$:
<ol>
  <li><strong>Point Form:</strong> Tangent at $P(x_1, y_1)$ on the curve:
  $$y y_1 = 2a(x + x_1)$$</li>
  <li><strong>Parametric Form:</strong> Tangent at $P(t) = (at^2, 2at)$:
  $$y(2at) = 2a(x + at^2) \iff \mathbf{t y = x + a t^2}$$
  The slope of this tangent is $m = 1/t$.</li>
  <li><strong>Slope Form:</strong> Replacing $t = 1/m$:
  $$\frac{y}{m} = x + \frac{a}{m^2} \iff \mathbf{y = m x + \frac{a}{m} \quad (m \ne 0)}$$
  The point of tangency is $\left(\frac{a}{m^2}, \frac{2a}{m}\right)$.</li>
</ol>
</p>

<h3>2. Point of Intersection of Two Tangents</h3>
<p>
Let the tangents be drawn at $P(t_1)$ and $Q(t_2)$:
$$t_1 y = x + a t_1^2, \qquad t_2 y = x + a t_2^2$$
Subtracting the equations:
$$(t_1 - t_2)y = a(t_1^2 - t_2^2) = a(t_1 - t_2)(t_1 + t_2) \implies y = a(t_1 + t_2)$$
Substituting back into $x = t_1 y - a t_1^2$:
$$x = t_1[a(t_1 + t_2)] - a t_1^2 = a t_1^2 + a t_1 t_2 - a t_1^2 = a t_1 t_2$$
Thus, the intersection of tangents at $t_1$ and $t_2$ is:
$$\mathbf{T = (a t_1 t_2, \; a(t_1 + t_2))}$$
Notice: The $x$-coordinate is the geometric mean of the abscissae, and the $y$-coordinate is the arithmetic mean of the ordinates of $P$ and $Q$!
</p>

<h3>3. Orthoptic Property (The Director Circle is the Directrix)</h3>
<p>
If the tangents at $P(t_1)$ and $Q(t_2)$ are mutually perpendicular, the product of their slopes is $-1$:
$$m_1 m_2 = \left(\frac{1}{t_1}\right)\left(\frac{1}{t_2}\right) = -1 \iff t_1 t_2 = -1$$
Substituting $t_1 t_2 = -1$ into the intersection coordinate:
$$x_T = a(t_1 t_2) = a(-1) = -a$$
<strong>The Orthoptic Theorem:</strong> The locus of the point of intersection of two mutually perpendicular tangents to a parabola is its directrix $x = -a$! (For a parabola, the director circle degenerates into its directrix).
</p>
"""
    },
    {
        "id": "u5-sec4",
        "title": "Normals to the Parabola & The Three Co-Normal Points",
        "content": r"""
<h3>1. Equations of the Normal</h3>
<p>
The normal at point $P(x_1, y_1)$ on $y^2 = 4ax$ has slope $m_N = -y_1/(2a)$:
$$y - y_1 = -\frac{y_1}{2a}(x - x_1)$$
In terms of the parameter $t$ ($m_N = -t$):
$$y - 2at = -t(x - at^2) \iff \mathbf{y + t x = 2 a t + a t^3}$$
Setting slope $m = -t$:
$$\mathbf{y = m x - 2 a m - a m^3}$$
</p>

<h3>2. The Three Co-Normal Points Theorem</h3>
<p>
If a normal passes through a given point $(\alpha, \beta)$, then:
$$\beta = m \alpha - 2am - am^3 \iff a m^3 + (2a - \alpha)m + \beta = 0$$
This is a cubic polynomial in the slope $m$. By the Fundamental Theorem of Algebra, it has three roots $m_1, m_2, m_3$ (at least one of which must be real). Thus, <strong>from any point in the plane, up to three normals can be drawn to a parabola</strong>!
</p>
<p>
By Viète's formulas for $a m^3 + 0 m^2 + (2a - \alpha)m + \beta = 0$:
$$m_1 + m_2 + m_3 = 0$$
$$m_1 m_2 + m_2 m_3 + m_3 m_1 = \frac{2a - \alpha}{a}$$
$$m_1 m_2 m_3 = -\frac{\beta}{a}$$
Since the ordinate of the feet of the normals is $y_i = 2am_i$ (using $m_i = -t_i$):
$$y_1 + y_2 + y_3 = -2a(m_1 + m_2 + m_3) = -2a(0) = \mathbf{0}$$
<strong>Theorem:</strong> The algebraic sum of the ordinates of the feet of three co-normal points on a parabola is always identically zero! Consequently, the centroid of the triangle formed by the three co-normal points always lies strictly on the axis of the parabola.
</p>
"""
    },
    {
        "id": "u5-sec5",
        "title": "Optical Reflection Property & Subtangent/Subnormal Invariants",
        "content": r"""
<h3>1. The Optical Reflection Property of the Parabola</h3>
<p>
Let $P(at^2, 2at)$ be a point on the parabola $y^2 = 4ax$. Let a light ray traveling parallel to the axis of symmetry (horizontal) strike the parabolic mirror at $P$.
The tangent at $P$ makes an angle $\alpha$ with the axis where $\tan \alpha = 1/t$.
The vector from the focus $S(a, 0)$ to $P$ makes an angle $\theta$ with the axis:
$$\tan \theta = \frac{2at}{at^2 - a} = \frac{2t}{t^2 - 1} = \tan(2\alpha)$$
Therefore, the angle of the focal ray is exactly twice the angle of the tangent ray: $\theta = 2\alpha$.
This proves that the tangent line bisects the angle between the focal ray $SP$ and the horizontal incident ray!
By the law of specular reflection (angle of incidence equals angle of reflection):
$$\mathbf{\text{All rays parallel to the axis of symmetry reflect precisely through the focus } S!}$$
This profound property is the physical foundation of satellite dishes, solar concentrators, radio telescopes, and automotive parabolic headlamps.
</p>

<h3>2. Subtangent and Subnormal Lengths</h3>
<p>
Let the tangent and normal at $P(x_1, y_1)$ intersect the $x$-axis at $T$ and $N$ respectively, and let $M(x_1, 0)$ be the projection of $P$ on the axis:
<ul>
  <li><strong>Subtangent ($TM$):</strong> The tangent is $y y_1 = 2a(x + x_1)$. Setting $y = 0 \implies x_T = -x_1$. Thus:
  $$TM = |x_1 - (-x_1)| = \mathbf{2 x_1}$$
  The vertex $V(0, 0)$ is the exact midpoint of $TM$!</li>
  <li><strong>Subnormal ($MN$):</strong> The normal is $y - y_1 = -\frac{y_1}{2a}(x - x_1)$. Setting $y = 0 \implies -y_1 = -\frac{y_1}{2a}(x_N - x_1) \implies x_N - x_1 = 2a$. Thus:
  $$MN = x_N - x_1 = \mathbf{2a = \text{Constant Everywhere!}}$$
  The subnormal of a parabola is constant at all points on the curve and equal to the semi-latus rectum!</li>
</ul>
</p>
""",
        "simulation": "geom2d-parabola-optics-sim",
        "simulations": ["geom2d-parabola-optics-sim"]
    }
]

u5_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Standard Parabola Geometric Elements and Tangent Equation",
        "statement": r"For the parabola $y^2 = 12x$: (a) Determine the coordinates of the focus, equation of the directrix, and length of the latus rectum. (b) Find the parametric value $t$ for the point $P(3, 6)$. (c) Formulate the equations of the tangent and normal lines at $P(3, 6)$.",
        "steps": [
            {
                "step": "Step 1: Identify Standard Parameters",
                "math": r"y^2 = 4ax = 12x \implies 4a = 12 \implies a = 3 \\ \text{Focus: } S(a, 0) = (3, 0) \\ \text{Directrix: } x = -a \implies x = -3 \iff x + 3 = 0 \\ \text{Latus Rectum: } 4a = 12",
                "explanation": "Comparing with $y^2 = 4ax$ yields $a = 3$."
            },
            {
                "step": "Step 2: Find Parametric Value $t$ at $P(3, 6)$",
                "math": r"P(at^2, 2at) = (3t^2, 6t) = (3, 6) \implies 6t = 6 \implies t = 1",
                "explanation": "Check: $3(1)^2 = 3 = x_P$. Thus $t = 1$."
            },
            {
                "step": "Step 3: Tangent and Normal at $P(3, 6)$",
                "math": r"\text{Tangent: } ty = x + at^2 \implies (1)y = x + 3(1)^2 \implies x - y + 3 = 0 \\ \text{Normal: } y + tx = 2at + at^3 \implies y + (1)x = 2(3)(1) + 3(1)^3 = 6 + 3 = 9 \implies x + y - 9 = 0",
                "explanation": "The tangent is $x - y + 3 = 0$ (slope $1$) and the normal is $x + y - 9 = 0$ (slope $-1$, mutually perpendicular)."
            }
        ],
        "answer": r"\text{Focus: } (3, 0); \quad \text{Directrix: } x = -3; \quad \text{Latus Rectum: } 12; \quad \text{Tangent: } x - y + 3 = 0; \quad \text{Normal: } x + y - 9 = 0"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Intersection of Tangents and Orthoptic Property Verification",
        "statement": r"Tangents are drawn to the parabola $y^2 = 8x$ from the external point $P(-2, 3)$. (a) Verify that point $P$ lies on the directrix of the parabola. (b) Find the individual equations of the two tangents. (c) Prove that the two tangents are mutually perpendicular.",
        "steps": [
            {
                "step": "Step 1: Verify Position on Directrix",
                "math": r"y^2 = 4ax = 8x \implies a = 2 \\ \text{Directrix: } x = -a = -2 \\ \text{Point } P(-2, 3) \text{ has abscissa } x = -2, \text{ so it lies strictly on the directrix!}",
                "explanation": "By the Orthoptic Theorem, tangents drawn from any point on the directrix must be mutually perpendicular."
            },
            {
                "step": "Step 2: Use Slope Form of Tangents",
                "math": r"y = mx + \frac{a}{m} \implies y = mx + \frac{2}{m} \implies m y = m^2 x + 2 \\ \text{Passing through } (-2, 3): \quad 3m = m^2(-2) + 2 \implies 2m^2 + 3m - 2 = 0 \\ (2m - 1)(m + 2) = 0 \implies m_1 = \frac{1}{2}, \quad m_2 = -2",
                "explanation": "The two slopes are $m_1 = 1/2$ and $m_2 = -2$."
            },
            {
                "step": "Step 3: Tangent Equations and Perpendicularity",
                "math": r"\text{Tangent 1 } (m = 1/2): \quad y = \frac{1}{2}x + \frac{2}{1/2} = \frac{1}{2}x + 4 \implies x - 2y + 8 = 0 \\ \text{Tangent 2 } (m = -2): \quad y = -2x + \frac{2}{-2} = -2x - 1 \implies 2x + y + 1 = 0 \\ m_1 \cdot m_2 = \left(\frac{1}{2}\right)(-2) = -1 \implies \text{Strictly Perpendicular!}",
                "explanation": "The product of the slopes is $-1$, confirming the Orthoptic Theorem."
            }
        ],
        "answer": r"\text{Directrix: } x = -2 \implies P \text{ lies on directrix}; \quad \text{Tangents: } x - 2y + 8 = 0 \text{ and } 2x + y + 1 = 0; \quad m_1 m_2 = -1 \implies \text{Orthogonal}"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Co-Normal Points: Locus of Points Subtending Orthogonal Normals",
        "statement": r"Prove that the locus of a point $(\alpha, \beta)$ from which two of the three normals to the parabola $y^2 = 4ax$ are mutually perpendicular is the parabola $y^2 = a(x - 3a)$.",
        "steps": [
            {
                "step": "Step 1: Cubic Equation for Normal Slopes",
                "math": r"\text{The cubic equation in normal slope } m \text{ is: } a m^3 + (2a - \alpha)m + \beta = 0 \\ m_1 + m_2 + m_3 = 0, \quad m_1 m_2 + m_2 m_3 + m_3 m_1 = \frac{2a - \alpha}{a}, \quad m_1 m_2 m_3 = -\frac{\beta}{a}",
                "explanation": "Viète's relations govern the three normal slopes."
            },
            {
                "step": "Step 2: Apply the Orthogonality Condition $m_1 m_2 = -1$",
                "math": r"m_1 m_2 = -1 \implies (-1)m_3 = -\frac{\beta}{a} \implies m_3 = \frac{\beta}{a}",
                "explanation": "Substituting $m_1 m_2 = -1$ into the product of roots gives the third root $m_3 = \beta/a$."
            },
            {
                "step": "Step 3: Substitute $m_3$ into the Cubic Equation",
                "math": r"a \left(\frac{\beta}{a}\right)^3 + (2a - \alpha)\left(\frac{\beta}{a}\right) + \beta = 0 \\ \frac{\beta^3}{a^2} + \frac{(2a - \alpha)\beta}{a} + \beta = 0 \implies \beta \left[ \frac{\beta^2}{a^2} + \frac{2a - \alpha}{a} + 1 \right] = 0",
                "explanation": "Since $\beta \ne 0$ for non-trivial solutions: $\frac{\beta^2}{a^2} + \frac{2a - \alpha + a}{a} = 0 \implies \frac{\beta^2}{a^2} + \frac{3a - \alpha}{a} = 0$."
            },
            {
                "step": "Step 4: Simplify to Locus Equation",
                "math": r"\frac{\beta^2}{a^2} = \frac{\alpha - 3a}{a} \implies \beta^2 = a(\alpha - 3a)",
                "explanation": "Replacing $(\alpha, \beta)$ with current coordinates $(x, y)$ gives the locus $y^2 = a(x - 3a)$."
            }
        ],
        "answer": r"\text{Locus: } y^2 = a(x - 3a) \text{ (Parabola with vertex at } (3a, 0) \text{ and latus rectum } a\text{)}"
    }
]

u5_data = {
    "unitNumber": 5,
    "number": 5,
    "title": "In-Depth Study of the Parabola",
    "description": "Exhaustive geometrical and analytical treatment of the parabola: focus-directrix definition SP = PM and canonical derivation y^2 = 4ax; geometric elements and alternative coordinate orientations; rational parametrization (at^2, 2at) and the focal chord theorem t_1 t_2 = -1; semi-latus rectum as harmonic mean of focal segments; tangents in point, slope, and parametric forms; intersection of tangents (at_1 t_2, a(t_1 + t_2)) and the orthoptic theorem; normal equations y = mx - 2am - am^3 and the three co-normal points theorem; optical reflection property of parabolic mirrors; and constancy of the subnormal MN = 2a.",
    "sections": u5_sections,
    "problems": u5_problems
}

# -------------------------------------------------------------
# UNIT 6
# -------------------------------------------------------------
u6_sections = [
    {
        "id": "u6-sec1",
        "title": "The Ellipse: Focus-Directrix Definition, Canonical Form & Metric Relations",
        "content": r"""
<h3>1. The Focus-Directrix Definition ($e < 1$)</h3>
<p>
An <strong>ellipse</strong> is the planar locus of a point $P(x, y)$ that moves such that the ratio of its distance from a fixed focus $S(ae, 0)$ to its distance from a fixed directrix line $D: x = a/e$ is a constant eccentricity $e \in (0, 1)$:
$$\frac{SP}{PM} = e \iff SP = e \cdot PM$$
Let $P(x, y)$ be any point on the curve. Then:
$$SP^2 = e^2 PM^2 \implies (x - ae)^2 + y^2 = e^2 \left(x - \frac{a}{e}\right)^2 = (ex - a)^2$$
$$x^2 - 2aex + a^2 e^2 + y^2 = e^2 x^2 - 2aex + a^2$$
Canceling $-2aex$ and grouping terms:
$$(1 - e^2)x^2 + y^2 = a^2(1 - e^2) \iff \frac{x^2}{a^2} + \frac{y^2}{a^2(1 - e^2)} = 1$$
Defining the minor semi-axis $b > 0$ by the fundamental relation:
$$\mathbf{b^2 \equiv a^2(1 - e^2) \iff e = \sqrt{1 - \frac{b^2}{a^2}} < 1}$$
yields the universal canonical equation of the ellipse:
$$\mathbf{\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \quad (a > b > 0)}$$
</p>

<h3>2. The Two Foci and The Constant Sum of Focal Radii</h3>
<p>
By symmetry about the $y$-axis, the ellipse possesses a second focus $S'(-ae, 0)$ and a second directrix $D': x = -a/e$.
The focal distances to any point $P(x, y)$ on the ellipse are:
$$SP = a - ex, \qquad S'P = a + ex$$
Adding the two distances:
$$SP + S'P = (a - ex) + (a + ex) = \mathbf{2a = \text{Constant Everywhere!}}$$
<strong>The Gardener's / Focal Distance Theorem:</strong> An ellipse is the locus of all points whose sum of distances from two fixed foci $S$ and $S'$ is constant and equal to the major axis $2a$.
</p>

<h3>3. Canonical Geometric Elements</h3>
<p>
<ul>
  <li><strong>Center ($C$):</strong> Origin $(0, 0)$.</li>
  <li><strong>Major Axis:</strong> Segment $A'A$ along the $x$-axis, length $2a$.</li>
  <li><strong>Minor Axis:</strong> Segment $B'B$ along the $y$-axis, length $2b$.</li>
  <li><strong>Foci:</strong> $S(ae, 0)$ and $S'(-ae, 0)$, distance between foci $SS' = 2ae$.</li>
  <li><strong>Directrices:</strong> $x = \pm a/e$, distance between directrices $2a/e$.</li>
  <li><strong>Latus Rectum:</strong> Chord through focus perpendicular to major axis. Substituting $x = ae$:
  $$\frac{a^2 e^2}{a^2} + \frac{y^2}{b^2} = 1 \implies \frac{y^2}{b^2} = 1 - e^2 = \frac{b^2}{a^2} \implies y = \pm \frac{b^2}{a} \implies \mathbf{Length = \frac{2b^2}{a}}$$</li>
</ul>
</p>
"""
    },
    {
        "id": "u6-sec2",
        "title": "Auxiliary Circle, Eccentric Angle & Parametric Coordinates",
        "content": r"""
<h3>1. The Auxiliary Circle</h3>
<p>
The circle described on the major axis $A'A$ of the ellipse as diameter is termed the <strong>auxiliary circle</strong>.
Its equation is:
$$x^2 + y^2 = a^2$$
Let $P(x, y)$ be any point on the ellipse. Draw a vertical ordinate through $P$ and extend it to meet the auxiliary circle at $Q(x, Y)$.
Because $Q$ lies on the auxiliary circle, $x = a \cos \phi$, where $\phi$ is the angle $\angle OCQ$ measured from the major axis.
Substituting $x = a \cos \phi$ into the ellipse equation:
$$\frac{a^2 \cos^2 \phi}{a^2} + \frac{y^2}{b^2} = 1 \implies \cos^2 \phi + \frac{y^2}{b^2} = 1 \implies \frac{y^2}{b^2} = \sin^2 \phi \implies y = b \sin \phi$$
The angle $\phi \in [0, 2\pi)$ is termed the <strong>eccentric angle</strong> of point $P$.
</p>

<h3>2. Standard Parametric Form</h3>
<p>
The parametric coordinates of any point on the ellipse are:
$$\mathbf{P(\phi) = (a \cos \phi, \; b \sin \phi)}$$
Notice the vertical scaling relation between the ellipse and its auxiliary circle:
$$\frac{y_P}{Y_Q} = \frac{b \sin \phi}{a \sin \phi} = \frac{b}{a} = \text{Constant}$$
An ellipse is an auxiliary circle uniformly compressed vertically by the factor $b/a$!
Consequently, the area of the ellipse is:
$$\operatorname{Area}(\text{Ellipse}) = \frac{b}{a} \times \operatorname{Area}(\text{Auxiliary Circle}) = \frac{b}{a}(\pi a^2) = \mathbf{\pi a b}$$
</p>
"""
    },
    {
        "id": "u6-sec3",
        "title": "Tangents, Normals & The Director Circle",
        "content": r"""
<h3>1. Equations of the Tangent</h3>
<p>
<ol>
  <li><strong>Point Form:</strong> Tangent at $P(x_1, y_1)$ on the ellipse:
  $$\mathbf{\frac{x x_1}{a^2} + \frac{y y_1}{b^2} = 1}$$</li>
  <li><strong>Parametric Form:</strong> Tangent at $P(\phi) = (a\cos\phi, b\sin\phi)$:
  $$\mathbf{\frac{x \cos \phi}{a} + \frac{y \sin \phi}{b} = 1}$$</li>
  <li><strong>Slope Form:</strong> A line $y = mx + c$ is tangent to $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ if and only if $c^2 = a^2 m^2 + b^2$:
  $$\mathbf{y = m x \pm \sqrt{a^2 m^2 + b^2}}$$</li>
</ol>
</p>

<h3>2. The Director Circle of the Ellipse</h3>
<p>
Let $P(h, k)$ be the point of intersection of two mutually perpendicular tangents to the ellipse.
The slope form of a tangent passing through $(h, k)$ is:
$$k - mh = \pm \sqrt{a^2 m^2 + b^2} \iff (k - mh)^2 = a^2 m^2 + b^2$$
Expanding and grouping as a quadratic in the slope $m$:
$$(h^2 - a^2)m^2 - 2hk m + (k^2 - b^2) = 0$$
If the two tangents are perpendicular, the product of their slopes must be $-1$:
$$m_1 m_2 = \frac{k^2 - b^2}{h^2 - a^2} = -1 \iff k^2 - b^2 = -(h^2 - a^2) \iff h^2 + k^2 = a^2 + b^2$$
Replacing $(h, k)$ with current coordinates $(x, y)$:
$$\mathbf{x^2 + y^2 = a^2 + b^2}$$
<strong>The Director Circle Theorem:</strong> The locus of the point of intersection of two mutually perpendicular tangents to an ellipse is a concentric circle of radius $R = \sqrt{a^2 + b^2}$, termed the <em>director circle</em>!
</p>

<h3>3. Equation of the Normal</h3>
<p>
The normal line at $P(x_1, y_1)$ is perpendicular to the tangent:
$$\mathbf{\frac{a^2 x}{x_1} - \frac{b^2 y}{y_1} = a^2 - b^2}$$
In parametric coordinates $P(\phi)$:
$$\mathbf{a x \sec \phi - b y \csc \phi = a^2 - b^2}$$
</p>
"""
    },
    {
        "id": "u6-sec4",
        "title": "Conjugate Diameters & Apollonius' Theorems",
        "content": r"""
<h3>1. Definition of Conjugate Diameters</h3>
<p>
A diameter of an ellipse is a chord passing through its center $C(0, 0)$.
Two diameters $y = m_1 x$ and $y = m_2 x$ are said to be <strong>conjugate diameters</strong> if each bisects all chords parallel to the other.
The algebraic condition for conjugacy is:
$$\mathbf{m_1 m_2 = -\frac{b^2}{a^2}}$$
In parametric terms, if $CP$ is a semi-diameter with endpoint $P(\phi) = (a\cos\phi, b\sin\phi)$, its conjugate semi-diameter $CD$ has endpoint $D$ whose eccentric angle differs by $\pi/2$:
$$\phi_D = \phi + \frac{\pi}{2} \implies \mathbf{D = (-a \sin \phi, \; b \cos \phi)}$$
</p>

<h3>2. Apollonius' First Theorem (Sum of Squared Semi-Diameters)</h3>
<p>
The sum of the squares of any two conjugate semi-diameters is constant and equal to the sum of the squares of the semi-axes:
$$CP^2 = a^2 \cos^2 \phi + b^2 \sin^2 \phi$$
$$CD^2 = a^2 \sin^2 \phi + b^2 \cos^2 \phi$$
Adding the two equations:
$$CP^2 + CD^2 = a^2(\cos^2 \phi + \sin^2 \phi) + b^2(\sin^2 \phi + \cos^2 \phi) = \mathbf{a^2 + b^2 = \text{Constant!}}$$
</p>

<h3>3. Apollonius' Second Theorem (Area of Circumscribing Parallelogram)</h3>
<p>
The area of the parallelogram formed by the tangents drawn at the extremities of any pair of conjugate diameters is constant and equal to the area of the rectangle formed by the principal axes:
$$\mathcal{A} = 4 \left| x_P y_D - x_D y_P \right| = 4 |(a\cos\phi)(b\cos\phi) - (-a\sin\phi)(b\sin\phi)| = 4 a b(\cos^2 \phi + \sin^2 \phi) = \mathbf{4 a b}$$
</p>
"""
    },
    {
        "id": "u6-sec5",
        "title": "Optical Reflection Property & Product of Focal Perpendiculars",
        "content": r"""
<h3>1. The Optical/Acoustic Reflection Property</h3>
<p>
Let $P(x_1, y_1)$ be any point on the ellipse with foci $S(ae, 0)$ and $S'(-ae, 0)$.
Let the normal at $P$ meet the major axis at $G$. By the properties of the normal:
$$CG = e^2 x_1 \implies SG = ae - e^2 x_1 = e(a - ex_1) = e \cdot SP, \quad S'G = ae + e^2 x_1 = e(a + ex_1) = e \cdot S'P$$
Therefore:
$$\frac{SG}{S'G} = \frac{SP}{S'P}$$
By the angle bisector theorem, the normal $PG$ is the internal bisector of the focal angle $\angle SPS'$!
Consequently, the tangent at $P$ is the external bisector of $\angle SPS'$.
$$\mathbf{\angle S P T = \angle S' P T}$$
<strong>Physical Consequence:</strong> Any light ray or acoustic wave emitted from one focus $S$ reflects off the elliptical boundary directly to the other focus $S'$! This is the physical mechanism of whispering galleries (such as St. Paul's Cathedral in London and the National Statuary Hall in Washington, D.C.).
</p>

<h3>2. Product of Perpendiculars from Foci onto Any Tangent</h3>
<p>
Let $p_1$ and $p_2$ be the lengths of perpendiculars dropped from the two foci $S(ae, 0)$ and $S'(-ae, 0)$ onto any tangent line $y - mx - \sqrt{a^2 m^2 + b^2} = 0$:
$$p_1 = \frac{|-mae - \sqrt{a^2 m^2 + b^2}|}{\sqrt{1 + m^2}}, \qquad p_2 = \frac{|mae - \sqrt{a^2 m^2 + b^2}|}{\sqrt{1 + m^2}}$$
Multiplying the two perpendiculars:
$$p_1 p_2 = \frac{|(a^2 m^2 + b^2) - m^2 a^2 e^2|}{1 + m^2} = \frac{|a^2 m^2(1 - e^2) + b^2|}{1 + m^2} = \frac{|a^2 m^2 (b^2/a^2) + b^2|}{1 + m^2} = \frac{b^2(m^2 + 1)}{1 + m^2} = \mathbf{b^2}$$
<strong>Theorem:</strong> The product of the perpendiculars from the foci onto any tangent to an ellipse is constant and equal to the square of the semi-minor axis $b^2$!
</p>
""",
        "simulation": "geom2d-ellipse-conjugate-sim",
        "simulations": ["geom2d-ellipse-conjugate-sim"]
    }
]

u6_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Standard Ellipse Geometric Elements and Parametric Tangent",
        "statement": r"For the ellipse $9x^2 + 16y^2 = 144$: (a) Find the lengths of the major and minor axes, eccentricity $e$, and coordinates of the foci and directrices. (b) Find the equation of the tangent line at the point where the eccentric angle is $\phi = \pi/4$.",
        "steps": [
            {
                "step": "Step 1: Reduce to Canonical Form",
                "math": r"\frac{9x^2}{144} + \frac{16y^2}{144} = 1 \implies \frac{x^2}{16} + \frac{y^2}{9} = 1 \implies a^2 = 16, \; b^2 = 9 \implies a = 4, \; b = 3",
                "explanation": "Major axis length is $2a = 8$; minor axis length is $2b = 6$."
            },
            {
                "step": "Step 2: Compute Eccentricity, Foci and Directrices",
                "math": r"e = \sqrt{1 - \frac{b^2}{a^2}} = \sqrt{1 - \frac{9}{16}} = \frac{\sqrt{7}}{4} \\ \text{Foci: } (\pm ae, 0) = \left(\pm 4\cdot\frac{\sqrt{7}}{4}, 0\right) = (\pm\sqrt{7}, 0) \\ \text{Directrices: } x = \pm\frac{a}{e} = \pm\frac{4}{\sqrt{7}/4} = \pm\frac{16}{\sqrt{7}}",
                "explanation": "Focal distance is $ae = \sqrt{7}$ and directrix distance is $a/e = 16/\sqrt{7}$."
            },
            {
                "step": "Step 3: Tangent Equation at $\phi = \pi/4$",
                "math": r"\frac{x\cos\phi}{a} + \frac{y\sin\phi}{b} = 1 \implies \frac{x\cos(\pi/4)}{4} + \frac{y\sin(\pi/4)}{3} = 1 \implies \frac{x}{4\sqrt{2}} + \frac{y}{3\sqrt{2}} = 1 \\ 3x + 4y = 12\sqrt{2}",
                "explanation": "Multiplying by $12\sqrt{2}$ yields the linear tangent equation $3x + 4y - 12\sqrt{2} = 0$."
            }
        ],
        "answer": r"a = 4, \; b = 3; \quad e = \frac{\sqrt{7}}{4}; \quad \text{Foci: } (\pm\sqrt{7}, 0); \quad \text{Directrices: } x = \pm\frac{16}{\sqrt{7}}; \quad \text{Tangent: } 3x + 4y = 12\sqrt{2}"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Director Circle and Mutual Perpendicular Tangents",
        "statement": r"Given the ellipse $\frac{x^2}{25} + \frac{y^2}{9} = 1$: (a) Write the equation of its director circle. (b) Find the equations of the tangents drawn from the point $P(0, \sqrt{34})$. (c) Verify that the two tangents are mutually perpendicular.",
        "steps": [
            {
                "step": "Step 1: Equation of Director Circle",
                "math": r"x^2 + y^2 = a^2 + b^2 = 25 + 9 = 34 \implies x^2 + y^2 = 34",
                "explanation": "Notice that the point $P(0, \sqrt{34})$ satisfies $0^2 + (\sqrt{34})^2 = 34$, so $P$ lies strictly on the director circle!"
            },
            {
                "step": "Step 2: Slope Form of Tangents through $P(0, \sqrt{34})$",
                "math": r"y = mx \pm \sqrt{a^2 m^2 + b^2} = mx \pm \sqrt{25m^2 + 9} \\ \sqrt{34} = m(0) \pm \sqrt{25m^2 + 9} \implies 34 = 25m^2 + 9 \implies 25m^2 = 25 \implies m^2 = 1 \implies m = \pm 1",
                "explanation": "The slopes of the two tangents are $m_1 = 1$ and $m_2 = -1$."
            },
            {
                "step": "Step 3: Tangent Equations and Orthogonality",
                "math": r"\text{Tangent 1 } (m = 1): \quad y = x + \sqrt{34} \implies x - y + \sqrt{34} = 0 \\ \text{Tangent 2 } (m = -1): \quad y = -x + \sqrt{34} \implies x + y - \sqrt{34} = 0 \\ m_1 \cdot m_2 = (1)(-1) = -1 \implies \text{Strictly Perpendicular!}",
                "explanation": "The product of the slopes is $-1$, verifying the Director Circle Theorem."
            }
        ],
        "answer": r"\text{Director Circle: } x^2 + y^2 = 34; \quad \text{Tangents: } y = x + \sqrt{34} \text{ and } y = -x + \sqrt{34}; \quad m_1 m_2 = -1 \implies \text{Orthogonal}"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Rigorous Proof of Apollonius' Conjugate Diameter Theorems",
        "statement": r"Let $CP$ and $CD$ be a pair of conjugate semi-diameters of the ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$. Prove analytically: (a) $CP^2 + CD^2 = a^2 + b^2$ (Apollonius' First Theorem). (b) The area of the parallelogram formed by the tangents at the extremities of the conjugate diameters is constant and equal to $4ab$ (Apollonius' Second Theorem).",
        "steps": [
            {
                "step": "Step 1: Express Endpoints in Parametric Form",
                "math": r"\text{Let } P = (a\cos\phi, b\sin\phi). \quad \text{Then } D \text{ has eccentric angle } \phi + \pi/2: \\ D = (a\cos(\phi + \pi/2), b\sin(\phi + \pi/2)) = (-a\sin\phi, b\cos\phi)",
                "explanation": "This establishes the exact coordinates of conjugate extremities."
            },
            {
                "step": "Step 2: Proof of Apollonius' First Theorem",
                "math": r"CP^2 = (a\cos\phi)^2 + (b\sin\phi)^2 = a^2\cos^2\phi + b^2\sin^2\phi \\ CD^2 = (-a\sin\phi)^2 + (b\cos\phi)^2 = a^2\sin^2\phi + b^2\cos^2\phi \\ CP^2 + CD^2 = a^2(\cos^2\phi + \sin^2\phi) + b^2(\sin^2\phi + \cos^2\phi) = a^2(1) + b^2(1) = a^2 + b^2",
                "explanation": "Since $\phi$ cancels completely, $CP^2 + CD^2 = a^2 + b^2$ holds for every conjugate pair."
            },
            {
                "step": "Step 3: Proof of Apollonius' Second Theorem",
                "math": r"\text{Area of } \triangle CPD = \frac{1}{2}|x_P y_D - x_D y_P| = \frac{1}{2}|(a\cos\phi)(b\cos\phi) - (-a\sin\phi)(b\sin\phi)| \\ = \frac{1}{2}|ab\cos^2\phi + ab\sin^2\phi| = \frac{1}{2}ab(\cos^2\phi + \sin^2\phi) = \frac{1}{2}ab \\ \text{Total parallelogram area} = 8 \times \operatorname{Area}(\triangle CPD) \text{ (or } 4 \times 2\triangle) = 4ab",
                "explanation": "The circumscribing parallelogram has constant area $4ab$ everywhere."
            }
        ],
        "answer": r"CP^2 + CD^2 = a^2 + b^2 \text{ (Apollonius' 1st)}; \quad \text{Parallelogram Area} = 4ab \text{ (Apollonius' 2nd)}"
    }
]

u6_data = {
    "unitNumber": 6,
    "number": 6,
    "title": "In-Depth Study of the Ellipse",
    "description": "Exhaustive treatment of the ellipse: focus-directrix definition e < 1 and canonical derivation x^2/a^2 + y^2/b^2 = 1; sum of focal distances SP + S'P = 2a and the gardener's construction; auxiliary circle x^2 + y^2 = a^2 and eccentric angle phi; area pi*a*b; tangents in point, slope, and parametric forms; director circle x^2 + y^2 = a^2 + b^2 and orthogonal tangent loci; normal equation a^2 x/x_1 - b^2 y/y_1 = a^2 - b^2; conjugate diameters and Apollonius' first (CP^2 + CD^2 = a^2 + b^2) and second (area = 4ab) theorems; optical and acoustic reflection properties; and the product of focal perpendiculars to any tangent p_1 p_2 = b^2.",
    "sections": u6_sections,
    "problems": u6_problems
}

# -------------------------------------------------------------
# UNIT 7
# -------------------------------------------------------------
u7_sections = [
    {
        "id": "u7-sec1",
        "title": "The Hyperbola: Canonical Equation, Eccentricity & Metric Relations",
        "content": r"""
<h3>1. The Focus-Directrix Locus Definition ($e > 1$)</h3>
<p>
A <strong>hyperbola</strong> is the planar locus of a point $P(x, y)$ that moves such that the ratio of its distance from a fixed focus $S(ae, 0)$ to its distance from a fixed directrix line $D: x = a/e$ is a constant eccentricity $e > 1$:
$$\frac{SP}{PM} = e \iff SP = e \cdot PM$$
Using the Euclidean distance formula:
$$(x - ae)^2 + y^2 = e^2 \left(x - \frac{a}{e}\right)^2 = (ex - a)^2$$
Expanding and simplifying:
$$(e^2 - 1)x^2 - y^2 = a^2(e^2 - 1) \iff \frac{x^2}{a^2} - \frac{y^2}{a^2(e^2 - 1)} = 1$$
Defining the conjugate semi-axis $b > 0$ by the fundamental relation:
$$\mathbf{b^2 \equiv a^2(e^2 - 1) \iff e = \sqrt{1 + \frac{b^2}{a^2}} > 1}$$
yields the canonical equation of the hyperbola:
$$\mathbf{\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1}$$
</p>

<h3>2. The Difference of Focal Radii</h3>
<p>
Like the ellipse, the hyperbola possesses two foci $S(ae, 0)$ and $S'(-ae, 0)$.
The focal distances to any point $P(x, y)$ on the right branch are $SP = ex - a$ and $S'P = ex + a$.
Their difference is:
$$S'P - SP = (ex + a) - (ex - a) = \mathbf{2a = \text{Constant Everywhere!}}$$
<strong>The Focal Difference Theorem:</strong> A hyperbola is the locus of all points whose difference of distances from two fixed foci $S$ and $S'$ is constant and equal to the transverse axis: $|S'P - SP| = 2a$.
</p>

<h3>3. Canonical Geometric Elements</h3>
<p>
<ul>
  <li><strong>Center ($C$):</strong> $(0, 0)$.</li>
  <li><strong>Transverse Axis:</strong> Segment along the $x$-axis connecting vertices $A(a, 0)$ and $A'(-a, 0)$, length $2a$.</li>
  <li><strong>Conjugate Axis:</strong> Segment along the $y$-axis of length $2b$.</li>
  <li><strong>Foci:</strong> $S(ae, 0)$ and $S'(-ae, 0)$, distance $SS' = 2ae$.</li>
  <li><strong>Directrices:</strong> $x = \pm a/e$, distance $2a/e$.</li>
  <li><strong>Latus Rectum:</strong> Length $2b^2/a$.</li>
</ul>
</p>
"""
    },
    {
        "id": "u7-sec2",
        "title": "Asymptotes & The Conjugate Hyperbola",
        "content": r"""
<h3>1. Asymptotes of the Hyperbola</h3>
<p>
An <strong>asymptote</strong> to a curve is a straight line such that the perpendicular distance from a point on the curve to the line approaches zero as the point recedes to infinity.
Solving the canonical hyperbola for $y$:
$$y = \pm \frac{b}{a}\sqrt{x^2 - a^2} = \pm \frac{b}{a}x \sqrt{1 - \frac{a^2}{x^2}} = \pm \frac{b}{a}x \left(1 - \frac{a^2}{2x^2} - \dots\right) \to \pm \frac{b}{a}x \quad \text{as } |x| \to \infty$$
Thus, the hyperbola possesses two real asymptotes passing through the center:
$$\mathbf{y = \frac{b}{a}x \quad \text{and} \quad y = -\frac{b}{a}x \iff \frac{x^2}{a^2} - \frac{y^2}{b^2} = 0}$$
The angle between the asymptotes is $2\theta$, where $\tan \theta = b/a \implies 2\theta = 2\arctan(b/a)$.
</p>

<h3>2. The Conjugate Hyperbola</h3>
<p>
The hyperbola whose transverse and conjugate axes are respectively the conjugate and transverse axes of the given hyperbola is termed the <strong>conjugate hyperbola</strong>:
$$\mathbf{\frac{y^2}{b^2} - \frac{x^2}{a^2} = 1 \iff -\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1}$$
<strong>Remarkable Properties:</strong>
<ul>
  <li>The hyperbola and its conjugate hyperbola share the <em>exact same pair of asymptotes</em>: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 0$.</li>
  <li>If $e_1$ is the eccentricity of the original hyperbola and $e_2$ is the eccentricity of the conjugate hyperbola:
  $$e_1^2 = 1 + \frac{b^2}{a^2} = \frac{a^2 + b^2}{a^2} \implies \frac{1}{e_1^2} = \frac{a^2}{a^2 + b^2}$$
  $$e_2^2 = 1 + \frac{a^2}{b^2} = \frac{a^2 + b^2}{b^2} \implies \frac{1}{e_2^2} = \frac{b^2}{a^2 + b^2}$$
  Adding these reciprocals establishes the celebrated theorem:
  $$\mathbf{\frac{1}{e_1^2} + \frac{1}{e_2^2} = 1}$$</li>
</ul>
</p>
"""
    },
    {
        "id": "u7-sec3",
        "title": "Tangents, Normals & The Director Circle",
        "content": r"""
<h3>1. Equations of the Tangent</h3>
<p>
<ol>
  <li><strong>Point Form:</strong> Tangent at $P(x_1, y_1)$ on $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$:
  $$\mathbf{\frac{x x_1}{a^2} - \frac{y y_1}{b^2} = 1}$$</li>
  <li><strong>Parametric Form:</strong> Using $x = a\sec\theta, y = b\tan\theta$:
  $$\mathbf{\frac{x \sec \theta}{a} - \frac{y \tan \theta}{b} = 1}$$</li>
  <li><strong>Slope Form:</strong> A line $y = mx + c$ is tangent if and only if $c^2 = a^2 m^2 - b^2$:
  $$\mathbf{y = m x \pm \sqrt{a^2 m^2 - b^2} \quad (|m| > b/a)}$$</li>
</ol>
</p>

<h3>2. The Director Circle of the Hyperbola</h3>
<p>
Repeating the orthogonal tangent locus derivation for the hyperbola yields:
$$\mathbf{x^2 + y^2 = a^2 - b^2}$$
<ul>
  <li><strong>Real Circle ($a > b$):</strong> A real concentric circle of radius $\sqrt{a^2 - b^2}$.</li>
  <li><strong>Point Circle ($a = b$):</strong> Concentrates to the origin $(0, 0)$.</li>
  <li><strong>Virtual / Imaginary ($a < b$):</strong> No pair of real mutually perpendicular tangents can be drawn to the hyperbola!</li>
</ul>
</p>
"""
    },
    {
        "id": "u7-sec4",
        "title": "The Rectangular (Equilateral) Hyperbola & xy = c^2",
        "content": r"""
<h3>1. The Equilateral Hyperbola ($a = b$)</h3>
<p>
When the semi-axes are equal ($a = b$), the hyperbola is termed <strong>rectangular</strong> or <strong>equilateral</strong>:
$$x^2 - y^2 = a^2$$
Key characteristics:
<ul>
  <li>Eccentricity: $e = \sqrt{1 + a^2/a^2} = \mathbf{\sqrt{2}}$. Every rectangular hyperbola has eccentricity exactly $\sqrt{2}$!</li>
  <li>Asymptotes: $y = \pm x \iff x^2 - y^2 = 0$. The asymptotes intersect at right angles ($\pi/2 = 90^\circ$).</li>
</ul>
</p>

<h3>2. Rotation of Axes to Asymptotic Coordinates ($xy = c^2$)</h3>
<p>
Because the asymptotes of a rectangular hyperbola are mutually perpendicular, they can be chosen as the coordinate axes!
Rotating the axes clockwise through $45^\circ$ ($\theta = -\pi/4$):
$$x = X \cos(-\pi/4) - Y \sin(-\pi/4) = \frac{X + Y}{\sqrt{2}}$$
$$y = X \sin(-\pi/4) + Y \cos(-\pi/4) = \frac{-X + Y}{\sqrt{2}}$$
Substituting into $x^2 - y^2 = a^2$:
$$\left(\frac{X + Y}{\sqrt{2}}\right)^2 - \left(\frac{Y - X}{\sqrt{2}}\right)^2 = a^2 \implies \frac{(X+Y)^2 - (Y-X)^2}{2} = a^2$$
$$\frac{4XY}{2} = a^2 \implies 2XY = a^2 \iff \mathbf{XY = \frac{a^2}{2} \equiv c^2}$$
This is the widely used standard canonical form of the rectangular hyperbola:
$$\mathbf{xy = c^2 \quad \left(c = \frac{a}{\sqrt{2}}\right)}$$
</p>
"""
    },
    {
        "id": "u7-sec5",
        "title": "Geometric Properties of the Asymptotic Hyperbola xy = c^2",
        "content": r"""
<h3>1. Parametric Form & Tangents</h3>
<p>
Setting $x = ct$, the curve $xy = c^2$ gives $y = c/t$. The standard parametrization is:
$$\mathbf{P(t) = \left(c t, \; \frac{c}{t}\right) \quad (t \ne 0)}$$
Differentiating implicitly: $y + x \frac{dy}{dx} = 0 \implies \frac{dy}{dx} = -\frac{y}{x} = -\frac{c/t}{ct} = -\frac{1}{t^2}$.
The equation of the tangent at $P(t)$ is:
$$y - \frac{c}{t} = -\frac{1}{t^2}(x - ct) \iff t^2 y - ct = -x + ct \iff \mathbf{x + t^2 y = 2ct \iff \frac{x}{t} + yt = 2c}$$
</p>

<h3>2. The Constant Area Tangent Triangle Theorem</h3>
<p>
The tangent at $P(t)$ intersects the asymptotes ($x$-axis and $y$-axis) at:
$$A: y = 0 \implies x_A = 2ct \implies A(2ct, 0)$$
$$B: x = 0 \implies y_B = \frac{2c}{t} \implies B\left(0, \frac{2c}{t}\right)$$
Notice:
<ol>
  <li><strong>Midpoint Property:</strong> The midpoint of the tangent segment $AB$ is $\left(\frac{2ct + 0}{2}, \frac{0 + 2c/t}{2}\right) = (ct, c/t) = P$.
  <strong>Theorem:</strong> The point of contact $P$ bisects the segment of the tangent intercepted between the asymptotes!</li>
  <li><strong>Constant Triangle Area:</strong> The area of the right triangle $\triangle OAB$ formed by the tangent and the two coordinate asymptotes is:
  $$\operatorname{Area}(\triangle OAB) = \frac{1}{2} OA \cdot OB = \frac{1}{2}(2ct)\left(\frac{2c}{t}\right) = \mathbf{2c^2 = \text{Constant Everywhere!}}$$
  The area is completely independent of the parameter $t$!</li>
</ol>
</p>
""",
        "simulation": "geom2d-hyperbola-asymptotes-sim",
        "simulations": ["geom2d-hyperbola-asymptotes-sim"]
    }
]

u7_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Standard Hyperbola Elements and Asymptote Equations",
        "statement": r"For the hyperbola $9x^2 - 16y^2 = 144$: (a) Find the lengths of the transverse and conjugate axes, eccentricity $e$, coordinates of the foci, and directrices. (b) Find the equations of the two asymptotes and the angle between them.",
        "steps": [
            {
                "step": "Step 1: Reduce to Canonical Form",
                "math": r"\frac{9x^2}{144} - \frac{16y^2}{144} = 1 \implies \frac{x^2}{16} - \frac{y^2}{9} = 1 \implies a^2 = 16, \; b^2 = 9 \implies a = 4, \; b = 3",
                "explanation": "Transverse axis is $2a = 8$; conjugate axis is $2b = 6$."
            },
            {
                "step": "Step 2: Eccentricity, Foci and Directrices",
                "math": r"e = \sqrt{1 + \frac{b^2}{a^2}} = \sqrt{1 + \frac{9}{16}} = \frac{5}{4} = 1.25 \\ \text{Foci: } (\pm ae, 0) = \left(\pm 4\cdot\frac{5}{4}, 0\right) = (\pm 5, 0) \\ \text{Directrices: } x = \pm\frac{a}{e} = \pm\frac{4}{5/4} = \pm\frac{16}{5} = \pm 3.2",
                "explanation": "Eccentricity is $1.25$, foci are at $(\pm 5, 0)$, directrices are $x = \pm 3.2$."
            },
            {
                "step": "Step 3: Asymptotes and Included Angle",
                "math": r"y = \pm\frac{b}{a}x = \pm\frac{3}{4}x \iff 3x - 4y = 0 \quad \text{and} \quad 3x + 4y = 0 \\ \tan\theta = \frac{3}{4} \implies \text{Angle between asymptotes } 2\theta = 2\arctan\left(\frac{3}{4}\right) \approx 73.74^\circ",
                "explanation": "The asymptotes are $y = \pm \frac{3}{4}x$."
            }
        ],
        "answer": r"a = 4, \; b = 3; \quad e = 1.25; \quad \text{Foci: } (\pm 5, 0); \quad \text{Directrices: } x = \pm 3.2; \quad \text{Asymptotes: } y = \pm\frac{3}{4}x"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Conjugate Hyperbolas and Eccentricity Reciprocal Theorem",
        "statement": r"A hyperbola $H_1$ has equation $16x^2 - 9y^2 = 144$. (a) Write the equation of its conjugate hyperbola $H_2$. (b) Find the eccentricities $e_1$ and $e_2$ of both hyperbolas. (c) Rigorously verify that $\frac{1}{e_1^2} + \frac{1}{e_2^2} = 1$.",
        "steps": [
            {
                "step": "Step 1: Canonical Form of $H_1$ and $H_2$",
                "math": r"H_1: \frac{x^2}{9} - \frac{y^2}{16} = 1 \implies a^2 = 9, \; b^2 = 16 \\ H_2 \text{ (Conjugate)}: -\frac{x^2}{9} + \frac{y^2}{16} = 1 \iff \frac{y^2}{16} - \frac{x^2}{9} = 1 \implies 9y^2 - 16x^2 = 144",
                "explanation": "The conjugate hyperbola is obtained by switching signs of terms."
            },
            {
                "step": "Step 2: Compute Eccentricities $e_1$ and $e_2$",
                "math": r"e_1 = \sqrt{1 + \frac{b^2}{a^2}} = \sqrt{1 + \frac{16}{9}} = \sqrt{\frac{25}{9}} = \frac{5}{3} \\ e_2 = \sqrt{1 + \frac{a^2}{b^2}} = \sqrt{1 + \frac{9}{16}} = \sqrt{\frac{25}{16}} = \frac{5}{4}",
                "explanation": "Thus $e_1 = 5/3$ and $e_2 = 5/4$."
            },
            {
                "step": "Step 3: Verify the Reciprocal Identity",
                "math": r"\frac{1}{e_1^2} + \frac{1}{e_2^2} = \frac{1}{(5/3)^2} + \frac{1}{(5/4)^2} = \frac{9}{25} + \frac{16}{25} = \frac{9 + 16}{25} = \frac{25}{25} = 1",
                "explanation": "The sum of reciprocals of squared eccentricities equals exactly 1."
            }
        ],
        "answer": r"H_2: \frac{y^2}{16} - \frac{x^2}{9} = 1; \quad e_1 = \frac{5}{3}, \; e_2 = \frac{5}{4}; \quad \frac{1}{e_1^2} + \frac{1}{e_2^2} = \frac{9}{25} + \frac{16}{25} = 1"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Rectangular Hyperbola $xy = c^2$: Concurrency of Circle Intersections",
        "statement": r"A circle $x^2 + y^2 + 2gx + 2fy + k = 0$ intersects the rectangular hyperbola $xy = c^2$ in four points $P_i(x_i, y_i)$ with parameters $t_i$ ($i = 1, 2, 3, 4$). (a) Derive the quartic equation in $t$. (b) Prove that $t_1 t_2 t_3 t_4 = 1$. (c) Prove that the product of the four abscissae is $c^4$, the product of the four ordinates is $c^4$, and the center of mean position of the four points is $(-g/2, -f/2)$.",
        "steps": [
            {
                "step": "Step 1: Substitute Parametric Coordinates into Circle",
                "math": r"x = ct, \quad y = \frac{c}{t} \\ (ct)^2 + \left(\frac{c}{t}\right)^2 + 2g(ct) + 2f\left(\frac{c}{t}\right) + k = 0 \\ c^2 t^2 + \frac{c^2}{t^2} + 2gct + \frac{2fc}{t} + k = 0",
                "explanation": "Multiply by $t^2$ to clear the denominator."
            },
            {
                "step": "Step 2: Form the Quartic Polynomial in $t$",
                "math": r"c^2 t^4 + 2gc t^3 + k t^2 + 2fc t + c^2 = 0",
                "explanation": "Dividing by $c^2$: $t^4 + \frac{2g}{c}t^3 + \frac{k}{c^2}t^2 + \frac{2f}{c}t + 1 = 0$."
            },
            {
                "step": "Step 3: Apply Viète's Formulas",
                "math": r"\sum t_i = t_1 + t_2 + t_3 + t_4 = -\frac{2g}{c} \\ \sum t_i t_j t_k = -\frac{2f}{c} \\ t_1 t_2 t_3 t_4 = \frac{c^2}{c^2} = 1",
                "explanation": "The product of the parameters is identically $t_1 t_2 t_3 t_4 = 1$."
            },
            {
                "step": "Step 4: Prove Coordinate Products and Centroid",
                "math": r"x_1 x_2 x_3 x_4 = (ct_1)(ct_2)(ct_3)(ct_4) = c^4(t_1 t_2 t_3 t_4) = c^4(1) = c^4 \\ y_1 y_2 y_3 y_4 = \left(\frac{c}{t_1}\right)\left(\frac{c}{t_2}\right)\left(\frac{c}{t_3}\right)\left(\frac{c}{t_4}\right) = \frac{c^4}{t_1 t_2 t_3 t_4} = c^4 \\ \bar{x} = \frac{\sum x_i}{4} = \frac{c \sum t_i}{4} = \frac{c(-2g/c)}{4} = -\frac{g}{2}, \quad \bar{y} = \frac{\sum y_i}{4} = \frac{c \sum(1/t_i)}{4} = -\frac{f}{2}",
                "explanation": "The centroid of the four intersection points is $(-g/2, -f/2)$, which is the exact midpoint of the line joining the origin to the circle's center $(-g, -f)$."
            }
        ],
        "answer": r"t_1 t_2 t_3 t_4 = 1; \quad \prod x_i = c^4, \; \prod y_i = c^4; \quad \text{Centroid: } \left(-\frac{g}{2}, -\frac{f}{2}\right)"
    }
]

u7_data = {
    "unitNumber": 7,
    "number": 7,
    "title": "In-Depth Study of the Hyperbola & Rectangular Hyperbola",
    "description": "Exhaustive treatment of the hyperbola: focus-directrix definition e > 1 and canonical derivation x^2/a^2 - y^2/b^2 = 1; focal distance difference |S'P - SP| = 2a; asymptotes y = +/- (b/a)x; conjugate hyperbola y^2/b^2 - x^2/a^2 = 1 and the eccentricity relation 1/e_1^2 + 1/e_2^2 = 1; tangents in point, slope, and parametric forms; director circle x^2 + y^2 = a^2 - b^2; rectangular (equilateral) hyperbola x^2 - y^2 = a^2 with e = sqrt(2); rotation to asymptotic canonical form xy = c^2; and the constant triangle area 2c^2 and midpoint bisection properties.",
    "sections": u7_sections,
    "problems": u7_problems
}

# -------------------------------------------------------------
# UNIT 8
# -------------------------------------------------------------
u8_sections = [
    {
        "id": "u8-sec1",
        "title": "Universal Polar Equation of a Conic with Focus at the Pole",
        "content": r"""
<h3>1. Unified Focus-Directrix Derivation</h3>
<p>
A remarkable triumph of analytic geometry is that all non-degenerate conic sections (circles, ellipses, parabolas, and hyperbolas) can be described by a <strong>single unified equation</strong> in polar coordinates when one focus is chosen as the pole $O$.
</p>
<p>
Let the pole $O$ be the focus of the conic, and let the polar axis be chosen along the axis of symmetry, perpendicular to directrix $D$.
Let the directrix $D$ be located at a distance $d$ to the left of the pole, so its Cartesian equation is $x = -d$, or in polar coordinates:
$$r \cos(\pi - \theta) = d \iff -r \cos \theta = d \iff r \cos \theta = -d$$
For any point $P(r, \theta)$ on the conic, the distance to the focus is $SP = r$.
The perpendicular distance from $P$ to the directrix is:
$$PM = d + r \cos \theta$$
By the universal conic definition $SP = e \cdot PM$:
$$r = e(d + r \cos \theta) = ed + er \cos \theta$$
$$r(1 - e \cos \theta) = ed \iff \frac{ed}{r} = 1 - e \cos \theta$$
Defining the <strong>semi-latus rectum</strong> $l \equiv ed$ (the value of $r$ when $\theta = \pi/2$):
$$\mathbf{\frac{l}{r} = 1 - e \cos \theta}$$
If the directrix is chosen to the right ($x = +d$), the equation becomes:
$$\mathbf{\frac{l}{r} = 1 + e \cos \theta}$$
If the axis of the conic is tilted by an angle $\alpha$ relative to the polar axis:
$$\mathbf{\frac{l}{r} = 1 + e \cos(\theta - \alpha)}$$
</p>
"""
    },
    {
        "id": "u8-sec2",
        "title": "Unified Geometric Classification via Polar Eccentricity",
        "content": r"""
<h3>1. Conic Morphing via Eccentricity $e$</h3>
<p>
In the universal polar equation $\frac{l}{r} = 1 + e \cos \theta$, the geometric nature of the curve is determined purely by the parameter $e$:
<ul>
  <li><strong>Circle ($e = 0$):</strong>
  $$\frac{l}{r} = 1 \iff r = l$$
  The radial distance is constant for all $\theta$, representing a circle of radius $l$ centered at the pole.</li>
  <li><strong>Ellipse ($0 < e < 1$):</strong>
  Because $e < 1$, the denominator $1 + e \cos \theta > 0$ for all $\theta \in [0, 2\pi)$. The curve is closed and bounded:
  $$\text{Periapsis (closest approach): } \theta = 0 \implies r_{\min} = \frac{l}{1 + e}$$
  $$\text{Apoapsis (furthest distance): } \theta = \pi \implies r_{\max} = \frac{l}{1 - e}$$
  The major axis length is $2a = r_{\min} + r_{\max} = \frac{l}{1+e} + \frac{l}{1-e} = \frac{2l}{1 - e^2} \implies l = a(1 - e^2)$.</li>
  <li><strong>Parabola ($e = 1$):</strong>
  $$\frac{l}{r} = 1 + \cos \theta = 2 \cos^2(\theta/2) \implies r = \frac{l}{2}\sec^2(\theta/2)$$
  As $\theta \to \pm \pi$, $r \to \infty$. The curve is open, escaping to infinity along a single direction.</li>
  <li><strong>Hyperbola ($e > 1$):</strong>
  The denominator $1 + e \cos \theta$ vanishes when $\cos \theta = -1/e$.
  The directions $\theta_0 = \pm \arccos(-1/e)$ define the <strong>directions of the asymptotes</strong>!
  The curve splits into two branches extending to infinity.</li>
</ul>
</p>
"""
    },
    {
        "id": "u8-sec3",
        "title": "Tangents, Normals & Chords in Polar Coordinates",
        "content": r"""
<h3>1. Equation of the Chord Joining Two Points</h3>
<p>
Let $P(\alpha - \beta)$ and $Q(\alpha + \beta)$ be two points on the conic $\frac{l}{r} = 1 + e \cos \theta$.
The straight line passing through both points is:
$$\mathbf{\frac{l}{r} = e \cos \theta + \sec \beta \cos(\theta - \alpha)}$$
Notice:
When $\theta = \alpha - \beta$: $\frac{l}{r} = e\cos(\alpha - \beta) + \sec\beta\cos(-\beta) = e\cos(\alpha - \beta) + 1$, which satisfies the conic equation!
When $\theta = \alpha + \beta$: $\frac{l}{r} = e\cos(\alpha + \beta) + \sec\beta\cos(\beta) = e\cos(\alpha + \beta) + 1$, which also satisfies the conic equation!
</p>

<h3>2. Equation of the Tangent Line</h3>
<p>
Taking the limit as $\beta \to 0$, the points $P$ and $Q$ coalesce at $\theta = \alpha$.
Since $\sec(0) = 1$, the equation of the tangent to the conic at $\theta = \alpha$ is:
$$\mathbf{\frac{l}{r} = e \cos \theta + \cos(\theta - \alpha)}$$
This is the universally famous polar tangent formula!
</p>

<h3>3. Perpendicular Focal Chords Theorem</h3>
<p>
Let $PSQ$ be a focal chord passing through the pole. The extremities are at $\theta = \alpha$ and $\theta = \alpha + \pi$.
$$SP = r_1 = \frac{l}{1 + e \cos \alpha}, \qquad SQ = r_2 = \frac{l}{1 + e \cos(\alpha + \pi)} = \frac{l}{1 - e \cos \alpha}$$
Adding their reciprocals:
$$\frac{1}{SP} + \frac{1}{SQ} = \frac{1 + e \cos \alpha}{l} + \frac{1 - e \cos \alpha}{l} = \mathbf{\frac{2}{l} = \text{Constant Everywhere!}}$$
<strong>Theorem:</strong> The semi-latus rectum $l$ is the harmonic mean of the segments of any focal chord in any conic!
</p>
"""
    },
    {
        "id": "u8-sec4",
        "title": "Confocal Conics & Orthogonal Intersections",
        "content": r"""
<h3>1. Confocal Conics</h3>
<p>
A family of conics having the same foci is termed <strong>confocal</strong>.
In Cartesian coordinates, the confocal family through foci $(\pm c, 0)$ is:
$$\frac{x^2}{a^2 + \lambda} + \frac{y^2}{b^2 + \lambda} = 1 \quad (\lambda \in \mathbb{R})$$
In polar coordinates with a common focus at the pole, the confocal family with a common axis is:
$$\frac{l}{r} = 1 + e \cos \theta$$
where $l$ and $e$ vary such that the second focus $S'$ is fixed.
</p>

<h3>2. Orthogonal Intersection Theorem</h3>
<p>
<strong>Fundamental Theorem of Confocal Conics:</strong>
Through any point $P(x_0, y_0)$ in the plane (not on the axes), there pass exactly two conics of a confocal family: one ellipse and one hyperbola.
Furthermore, these two conics intersect each other <strong>at strictly right angles ($90^\circ$)</strong> at point $P$!
This property is the foundation of elliptic coordinate systems used to solve Laplace's and Helmholtz's equations in mathematical physics.
</p>
"""
    },
    {
        "id": "u8-sec5",
        "title": "Celestial Orbital Geometry & Keplerian Trajectories",
        "content": r"""
<h3>1. Kepler's First Law and Newton's Gravitational Potential</h3>
<p>
In celestial mechanics and orbital astrophysics, a satellite or planet orbiting a central gravitational mass $M$ under Newton's inverse-square gravitational force $\mathbf{F} = -\frac{G M m}{r^2}\hat{\mathbf{r}}$ obeys the Binet differential equation:
$$\frac{d^2 u}{d\theta^2} + u = \frac{G M}{h^2} = \frac{\mu}{h^2}$$
where $u = 1/r$, $\mu = GM$ is the gravitational parameter, and $h = r^2 \dot{\theta}$ is the specific angular momentum.
The exact general solution of this linear differential equation is:
$$u = \frac{\mu}{h^2}(1 + e \cos(\theta - \omega)) \iff \mathbf{r(\theta) = \frac{p}{1 + e \cos(\theta - \omega)}}$$
where $p = h^2/\mu$ is the semi-latus rectum and $e$ is the orbital eccentricity!
</p>

<h3>2. The Energy-Eccentricity Correspondence (Vis-Viva Equation)</h3>
<p>
The total specific orbital energy $\mathcal{E} = \frac{1}{2}v^2 - \frac{\mu}{r}$ is conserved along the trajectory:
$$\mathcal{E} = -\frac{\mu^2(1 - e^2)}{2h^2} = -\frac{\mu}{2a}$$
The sign of the orbital energy determines the conic geometry:
<ul>
  <li><strong>Bound Elliptical Orbit ($\mathcal{E} < 0, \; 0 \le e < 1$):</strong> Periodic planetary orbits (Keplerian orbits).</li>
  <li><strong>Parabolic Escape Trajectory ($\mathcal{E} = 0, \; e = 1$):</strong> Critical escape velocity $v_{\text{esc}} = \sqrt{2\mu/r}$. The spacecraft possesses just enough energy to escape to infinity with zero residual velocity.</li>
  <li><strong>Hyperbolic Flyby / Interstellar Trajectory ($\mathcal{E} > 0, \; e > 1$):</strong> Gravity-assist planetary flybys and interstellar objects (e.g., 1I/'Oumuamua and 2I/Borisov). The spacecraft escapes to infinity with hyperbolic excess speed $v_\infty = \sqrt{2\mathcal{E}} = \sqrt{\mu/a}$.</li>
</ul>
</p>
""",
        "simulation": "geom2d-polar-conic-kepler-sim",
        "simulations": ["geom2d-polar-conic-kepler-sim"]
    }
]

u8_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Polar Conic Geometric Elements and Periapsis/Apoapsis",
        "statement": r"A conic has the polar equation $\frac{12}{r} = 3 + 2\cos\theta$: (a) Reduce the equation to standard form $\frac{l}{r} = 1 + e\cos\theta$ and identify the conic. (b) Find the semi-latus rectum $l$, eccentricity $e$, and periapsis and apoapsis distances. (c) Determine the length of the major axis $2a$.",
        "steps": [
            {
                "step": "Step 1: Reduce to Standard Form",
                "math": r"\frac{12}{r} = 3\left(1 + \frac{2}{3}\cos\theta\right) \implies \frac{12/3}{r} = 1 + \frac{2}{3}\cos\theta \implies \frac{4}{r} = 1 + \frac{2}{3}\cos\theta",
                "explanation": "Comparing with $\frac{l}{r} = 1 + e\cos\theta$ yields $l = 4$ and $e = 2/3$."
            },
            {
                "step": "Step 2: Identify Conic and Focal Extrema",
                "math": r"e = \frac{2}{3} < 1 \implies \text{The conic is an Ellipse!} \\ \text{Periapsis } (\theta = 0): \quad r_{\min} = \frac{l}{1 + e} = \frac{4}{1 + 2/3} = \frac{4}{5/3} = \frac{12}{5} = 2.4 \\ \text{Apoapsis } (\theta = \pi): \quad r_{\max} = \frac{l}{1 - e} = \frac{4}{1 - 2/3} = \frac{4}{1/3} = 12",
                "explanation": "The closest approach is $2.4$ and the furthest distance is $12$."
            },
            {
                "step": "Step 3: Length of Major Axis",
                "math": r"2a = r_{\min} + r_{\max} = 2.4 + 12 = 14.4 \implies a = 7.2",
                "explanation": "Check: $l = a(1 - e^2) \implies 4 = a(1 - 4/9) = a(5/9) \implies a = 36/5 = 7.2$. (Exact match!)"
            }
        ],
        "answer": r"\text{Ellipse: } \frac{4}{r} = 1 + \frac{2}{3}\cos\theta; \quad l = 4, \; e = \frac{2}{3}; \quad r_{\min} = 2.4, \; r_{\max} = 12; \quad 2a = 14.4"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Tangent to a Polar Conic and Perpendicular Tangents",
        "statement": r"Given the polar conic $\frac{l}{r} = 1 + e\cos\theta$: (a) Write the equation of the tangent at point $P(\alpha)$. (b) For the parabola $e = 1$, find the tangents at the ends of the latus rectum ($\alpha = \pi/2$ and $\alpha = -\pi/2$). (c) Prove that these two tangents intersect on the directrix at right angles.",
        "steps": [
            {
                "step": "Step 1: General Tangent Equation",
                "math": r"\frac{l}{r} = e\cos\theta + \cos(\theta - \alpha)",
                "explanation": "This is the general polar tangent formula."
            },
            {
                "step": "Step 2: Tangents at $\alpha = \pm\pi/2$ for Parabola ($e = 1$)",
                "math": r"\text{At } \alpha = \pi/2: \quad \frac{l}{r} = \cos\theta + \cos(\theta - \pi/2) = \cos\theta + \sin\theta \\ \text{At } \alpha = -\pi/2: \quad \frac{l}{r} = \cos\theta + \cos(\theta + \pi/2) = \cos\theta - \sin\theta",
                "explanation": "In Cartesian coordinates ($x = r\cos\theta, y = r\sin\theta$): $l = x + y \implies x + y = l$, and $l = x - y \implies x - y = l$."
            },
            {
                "step": "Step 3: Intersection and Perpendicularity",
                "math": r"x + y = l \quad (m_1 = -1) \\ x - y = l \quad (m_2 = +1) \\ m_1 m_2 = (-1)(1) = -1 \implies \text{Mutually Perpendicular!} \\ \text{Adding: } 2x = 2l \implies x = l, \quad y = 0",
                "explanation": "Since the directrix of $\frac{l}{r} = 1 + \cos\theta$ is $x = -l$ (or $x = l$ depending on orientation), the tangents are orthogonal and intersect on the directrix axis."
            }
        ],
        "answer": r"\text{Tangents: } x + y = l \text{ and } x - y = l; \quad m_1 m_2 = -1 \implies \text{Orthogonal}; \quad \text{Intersection: } (l, 0)"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Sum of Reciprocals of Mutually Perpendicular Focal Chords",
        "statement": r"If $PQ$ and $RS$ are two mutually perpendicular focal chords of a conic $\frac{l}{r} = 1 + e\cos\theta$, prove that the sum $\frac{1}{PQ} + \frac{1}{RS}$ is strictly constant and independent of the chord orientations.",
        "steps": [
            {
                "step": "Step 1: Length of a Focal Chord $PQ$",
                "math": r"\text{Let the inclination of chord } PQ \text{ be } \alpha. \quad \text{Then } P \text{ is at } \alpha \text{ and } Q \text{ is at } \alpha + \pi: \\ SP = \frac{l}{1 + e\cos\alpha}, \qquad SQ = \frac{l}{1 + e\cos(\alpha + \pi)} = \frac{l}{1 - e\cos\alpha} \\ PQ = SP + SQ = \frac{l}{1 + e\cos\alpha} + \frac{l}{1 - e\cos\alpha} = \frac{l(1 - e\cos\alpha + 1 + e\cos\alpha)}{1 - e^2\cos^2\alpha} = \frac{2l}{1 - e^2\cos^2\alpha}",
                "explanation": "Thus the reciprocal of $PQ$ is: $\frac{1}{PQ} = \frac{1 - e^2\cos^2\alpha}{2l}$."
            },
            {
                "step": "Step 2: Length of the Perpendicular Focal Chord $RS$",
                "math": r"\text{Since } RS \perp PQ, \text{ the inclination of chord } RS \text{ is } \alpha + \pi/2: \\ \frac{1}{RS} = \frac{1 - e^2\cos^2(\alpha + \pi/2)}{2l} = \frac{1 - e^2(-\sin\alpha)^2}{2l} = \frac{1 - e^2\sin^2\alpha}{2l}",
                "explanation": "This expresses $1/RS$ in terms of $\sin^2\alpha$."
            },
            {
                "step": "Step 3: Sum the Reciprocals",
                "math": r"\frac{1}{PQ} + \frac{1}{RS} = \frac{1 - e^2\cos^2\alpha}{2l} + \frac{1 - e^2\sin^2\alpha}{2l} = \frac{2 - e^2(\cos^2\alpha + \sin^2\alpha)}{2l} = \frac{2 - e^2(1)}{2l} = \frac{2 - e^2}{2l}",
                "explanation": "Because $\alpha$ cancels out entirely, the sum is strictly invariant!"
            }
        ],
        "answer": r"\frac{1}{PQ} + \frac{1}{RS} = \frac{2 - e^2}{2l} = \text{Constant Everywhere}"
    }
]

u8_data = {
    "unitNumber": 8,
    "number": 8,
    "title": "Polar Equations of Conics & Celestial Orbital Geometry",
    "description": "Unified universal polar formulation of conic sections: focus-at-pole derivation l/r = 1 + e cos theta; geometric classification and morphing across eccentricity e (circle e=0, ellipse 0<e<1, parabola e=1, hyperbola e>1); periapsis and apoapsis relations; chords, tangents l/r = e cos theta + cos(theta - alpha), and normals in polar coordinates; harmonic mean property of focal chord segments; confocal conics and orthogonal intersection theorems; and celestial orbital mechanics via Binet's equation, orbital energy, vis-viva equation, and hyperbolic escape flybys.",
    "sections": u8_sections,
    "problems": u8_problems
}

# -------------------------------------------------------------
# WRITE OUT JSON FILES
# -------------------------------------------------------------
for i, data in enumerate([u5_data, u6_data, u7_data, u8_data], 5):
    fn = f"geom2d_u{i}.json"
    with open(fn, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"{fn} created successfully!")
