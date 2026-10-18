import json

def build_unit_3():
    return {
        "id": "geom3d-u3",
        "title": "Unit 3: The Straight Line in Space & Skew Lines",
        "description": "Comprehensive analysis of lines in three dimensions: vector, symmetric, and general two-plane representations, coplanarity criteria, and the complete derivation and computation of the shortest distance between skew lines.",
        "sections": [
            {
                "id": "sec-geom3d-3-1",
                "title": "3.1 Parametric, Symmetric, and General (Two-Plane) Forms of a 3D Line",
                "content": r"""A straight line in $\mathbb{R}^3$ is uniquely determined either by:
1. A point through which it passes and its direction in space (specified by a direction vector or direction cosines).
2. The intersection of two non-parallel planes.

---

### 1. Vector and Parametric Equations

Let a line $\mathcal{L}$ pass through a fixed point $A$ with position vector $\vec{a} = x_1\hat{i} + y_1\hat{j} + z_1\hat{k}$ and be parallel to a direction vector $\vec{d} = l\hat{i} + m\hat{j} + n\hat{k}$.

If $P$ with position vector $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$ is any arbitrary point on the line, the vector $\vec{AP} = \vec{r} - \vec{a}$ is collinear with $\vec{d}$. Hence, there exists a scalar parameter $t \in \mathbb{R}$ such that:

$$\vec{r} - \vec{a} = t\vec{d} \implies \vec{r} = \vec{a} + t\vec{d}$$

Equating components along the standard basis vectors:

$$\begin{cases} x = x_1 + lt \\ y = y_1 + mt \\ z = z_1 + nt \end{cases}$$

These are the **parametric equations** of the straight line.

---

### 2. Symmetrical (Standard) Cartesian Form

Eliminating the scalar parameter $t$ from the parametric equations (assuming $l, m, n \neq 0$):

$$t = \frac{x - x_1}{l} = \frac{y - y_1}{m} = \frac{z - z_1}{n}$$

This is the canonical **symmetrical form** of a line passing through $(x_1, y_1, z_1)$ with direction ratios $(l, m, n)$.

> **Convention when a direction ratio vanishes:**  
> If one direction ratio is zero, say $n = 0$, the line lies in a plane parallel to the $xy$-plane ($z = z_1$). We write:
> $$\frac{x - x_1}{l} = \frac{y - y_1}{m}, \quad z = z_1$$

If $l, m, n$ are normalized to actual direction cosines $(\cos\alpha, \cos\beta, \cos\gamma)$, then the parameter $r = t$ represents the actual **directed algebraic distance** along the line from $(x_1, y_1, z_1)$ to $(x, y, z)$.

---

### 3. Two-Point Form of a Line

If the line passes through two distinct points $A(x_1, y_1, z_1)$ and $B(x_2, y_2, z_2)$, its direction vector is $\vec{d} = \vec{AB} = (x_2 - x_1)\hat{i} + (y_2 - y_1)\hat{j} + (z_2 - z_1)\hat{k}$. The symmetric equations become:

$$\frac{x - x_1}{x_2 - x_1} = \frac{y - y_1}{y_2 - y_1} = \frac{z - z_1}{z_2 - z_1}$$

---

### 4. Non-Symmetric Form (General Equation as Two Planes)

A straight line in $\mathbb{R}^3$ can also be represented as the simultaneous intersection of two non-parallel planes:

$$\begin{cases} \Pi_1: a_1 x + b_1 y + c_1 z + d_1 = 0 \\ \Pi_2: a_2 x + b_2 y + c_2 z + d_2 = 0 \end{cases}$$

where the normal vectors $\vec{n}_1 = (a_1, b_1, c_1)$ and $\vec{n}_2 = (a_2, b_2, c_2)$ are not proportional ($\vec{n}_1 \times \vec{n}_2 \neq \vec{0}$).

#### Algorithm: Reduction from General Form to Symmetrical Form

To convert the two-plane system into symmetrical form $\frac{x - x_0}{l} = \frac{y - y_0}{m} = \frac{z - z_0}{n}$:

1. **Find the Direction Ratios $(l, m, n)$:**  
   Since the line lies entirely in both $\Pi_1$ and $\Pi_2$, its direction vector $\vec{d}$ must be perpendicular to both normals $\vec{n}_1$ and $\vec{n}_2$. Thus:
   $$\vec{d} = \vec{n}_1 \times \vec{n}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \end{vmatrix} = (b_1 c_2 - b_2 c_1)\hat{i} + (c_1 a_2 - c_2 a_1)\hat{j} + (a_1 b_2 - a_2 b_1)\hat{k}$$
   Hence, $(l, m, n) = (b_1 c_2 - b_2 c_1, \; c_1 a_2 - c_2 a_1, \; a_1 b_2 - a_2 b_1)$.

2. **Find a Specific Point $(x_0, y_0, z_0)$ on the Line:**  
   Set one coordinate to a convenient constant (frequently $z = 0$, provided $a_1 b_2 - a_2 b_1 \neq 0$) and solve the resulting system of two linear equations in two variables:
   $$\begin{cases} a_1 x + b_1 y = -d_1 \\ a_2 x + b_2 y = -d_2 \end{cases}$$
   Using Cramer's Rule:
   $$x_0 = \frac{-d_1 b_2 + d_2 b_1}{a_1 b_2 - a_2 b_1}, \quad y_0 = \frac{-a_1 d_2 + a_2 d_1}{a_1 b_2 - a_2 b_1}, \quad z_0 = 0$$
   The symmetrical equation is then immediately established."""
            },
            {
                "id": "sec-geom3d-3-2",
                "title": "3.2 Intersection, Angle, and Coplanarity of Two Straight Lines",
                "content": r"""### 1. Angle Between Two Straight Lines

Let two lines $\mathcal{L}_1$ and $\mathcal{L}_2$ have direction ratios $(l_1, m_1, n_1)$ and $(l_2, m_2, n_2)$ respectively. The angle $\theta$ between them is the angle between their direction vectors:

$$\cos\theta = \frac{l_1 l_2 + m_1 m_2 + n_1 n_2}{\sqrt{l_1^2 + m_1^2 + n_1^2}\sqrt{l_2^2 + m_2^2 + n_2^2}}$$

- **Perpendicularity:** $l_1 l_2 + m_1 m_2 + n_1 n_2 = 0$.
- **Parallelism:** $\frac{l_1}{l_2} = \frac{m_1}{m_2} = \frac{n_1}{n_2}$.

---

### 2. Coplanarity Criterion for Two Lines

Consider two lines in space given in symmetric form:

$$\mathcal{L}_1: \frac{x - x_1}{l_1} = \frac{y - y_1}{m_1} = \frac{z - z_1}{n_1}, \qquad \mathcal{L}_2: \frac{x - x_2}{l_2} = \frac{y - y_2}{m_2} = \frac{z - z_2}{n_2}$$

Let $A(x_1, y_1, z_1)$ lie on $\mathcal{L}_1$ and $B(x_2, y_2, z_2)$ lie on $\mathcal{L}_2$. Their direction vectors are $\vec{d}_1 = (l_1, m_1, n_1)$ and $\vec{d}_2 = (l_2, m_2, n_2)$.

Two straight lines are **coplanar** (lie in a single shared plane) if and only if they either intersect at a unique point or are strictly parallel. In both cases, the displacement vector connecting points on the two lines, $\vec{AB} = (x_2 - x_1)\hat{i} + (y_2 - y_1)\hat{j} + (z_2 - z_1)\hat{k}$, must lie in the plane spanned by $\vec{d}_1$ and $\vec{d}_2$.

Consequently, the scalar triple product of $\vec{AB}$, $\vec{d}_1$, and $\vec{d}_2$ must vanish:

$$\vec{AB} \cdot (\vec{d}_1 \times \vec{d}_2) = 0$$

Expanding this into determinant form yields the **fundamental condition of coplanarity**:

$$\begin{vmatrix} x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \\ l_1 & m_1 & n_1 \\ l_2 & m_2 & n_2 \end{vmatrix} = 0$$

---

### 3. Equation of the Plane Containing Coplanar Lines

If the coplanarity determinant vanishes and the lines are not parallel ($\vec{d}_1 \times \vec{d}_2 \neq \vec{0}$), they span a unique plane $\Pi$. Since the plane contains point $(x_1, y_1, z_1)$ and both direction vectors $\vec{d}_1$ and $\vec{d}_2$, the equation of the plane is:

$$\begin{vmatrix} x - x_1 & y - y_1 & z - z_1 \\ l_1 & m_1 & n_1 \\ l_2 & m_2 & n_2 \end{vmatrix} = 0$$

Alternatively, using the reference point $(x_2, y_2, z_2)$ yields an identical plane."""
            },
            {
                "id": "sec-geom3d-3-3",
                "title": "3.3 Skew Lines and the Shortest Distance",
                "content": r"""In two dimensions, any two non-parallel lines must intersect. In three dimensions, this is no longer true.

### 1. Definition of Skew Lines

Two straight lines in $\mathbb{R}^3$ are defined as **skew lines** if they are **neither parallel nor intersecting**. Skew lines do not lie in any common plane; they exist in distinct, non-parallel planes.

$$\mathcal{L}_1 \text{ and } \mathcal{L}_2 \text{ are skew} \iff \begin{vmatrix} x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \\ l_1 & m_1 & n_1 \\ l_2 & m_2 & n_2 \end{vmatrix} \neq 0$$

---

### 2. Derivation of the Shortest Distance (S.D.) Formula

Let $\mathcal{L}_1$ pass through $A(\vec{a}_1)$ with direction $\vec{d}_1$, and $\mathcal{L}_2$ pass through $B(\vec{a}_2)$ with direction $\vec{d}_2$.

The **shortest distance** between $\mathcal{L}_1$ and $\mathcal{L}_2$ is measured along their **common perpendicular** — the unique line that intersects both $\mathcal{L}_1$ and $\mathcal{L}_2$ at right angles.

Let $\vec{n}$ be a vector perpendicular to both lines. By definition:

$$\vec{n} = \vec{d}_1 \times \vec{d}_2$$

The unit vector in this common normal direction is:

$$\hat{n} = \frac{\vec{d}_1 \times \vec{d}_2}{|\vec{d}_1 \times \vec{d}_2|}$$

Consider the connecting vector $\vec{AB} = \vec{a}_2 - \vec{a}_1$. The shortest distance $d$ is precisely the absolute length of the orthogonal projection of $\vec{AB}$ onto the common normal $\hat{n}$:

$$d = |\vec{AB} \cdot \hat{n}| = \frac{|(\vec{a}_2 - \vec{a}_1) \cdot (\vec{d}_1 \times \vec{d}_2)|}{|\vec{d}_1 \times \vec{d}_2|}$$

---

### 3. Cartesian Determinant Form of Shortest Distance

Substituting $\vec{a}_1 = (x_1, y_1, z_1)$, $\vec{a}_2 = (x_2, y_2, z_2)$, $\vec{d}_1 = (l_1, m_1, n_1)$, and $\vec{d}_2 = (l_2, m_2, n_2)$:

The numerator is the determinant:

$$\Delta = \begin{vmatrix} x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \\ l_1 & m_1 & n_1 \\ l_2 & m_2 & n_2 \end{vmatrix}$$

The cross product in the denominator is:

$$\vec{d}_1 \times \vec{d}_2 = (m_1 n_2 - m_2 n_1)\hat{i} + (n_1 l_2 - n_2 l_1)\hat{j} + (l_1 m_2 - l_2 m_1)\hat{k}$$

Its magnitude is:

$$|\vec{d}_1 \times \vec{d}_2| = \sqrt{(m_1 n_2 - m_2 n_1)^2 + (n_1 l_2 - n_2 l_1)^2 + (l_1 m_2 - l_2 m_1)^2}$$

Thus, the exact Cartesian formula for the shortest distance is:

$$d = \frac{\left| \begin{vmatrix} x_2 - x_1 & y_2 - y_1 & z_2 - z_1 \\ l_1 & m_1 & n_1 \\ l_2 & m_2 & n_2 \end{vmatrix} \right|}{\sqrt{(m_1 n_2 - m_2 n_1)^2 + (n_1 l_2 - n_2 l_1)^2 + (l_1 m_2 - l_2 m_1)^2}}$$

---

### 4. Equations of the Line of Shortest Distance

The line of shortest distance (the common perpendicular $\mathcal{L}_{SD}$) can be represented as the intersection of two planes:
1. The plane containing $\mathcal{L}_1$ and parallel to the common normal $\vec{n} = \vec{d}_1 \times \vec{d}_2$.
2. The plane containing $\mathcal{L}_2$ and parallel to the common normal $\vec{n} = \vec{d}_1 \times \vec{d}_2$.

Let $(l, m, n)$ be the direction ratios of the common perpendicular $\vec{n} = \vec{d}_1 \times \vec{d}_2$. Then the two defining planes are:

$$\begin{vmatrix} x - x_1 & y - y_1 & z - z_1 \\ l_1 & m_1 & n_1 \\ l & m & n \end{vmatrix} = 0 \quad \text{and} \quad \begin{vmatrix} x - x_2 & y - y_2 & z - z_2 \\ l_2 & m_2 & n_2 \\ l & m & n \end{vmatrix} = 0$$

The simultaneous solution of these two plane equations defines the exact straight line of shortest distance in $\mathbb{R}^3$."""
            }
        ],
        "simulations": [
            {
                "id": "sim_geom3d_skew_lines",
                "title": "3D Interactive Skew Lines & Shortest Distance Engine",
                "description": "Rotate and manipulate two 3D straight lines in real time. Inspect the common normal vector, projection distance d, and orthogonal planes enclosing the skew system.",
                "controls": [
                    {"param": "rotY", "label": "Orbit Yaw (°)", "min": -180, "max": 180, "step": 1, "default": 35},
                    {"param": "rotX", "label": "Orbit Pitch (°)", "min": -85, "max": 85, "step": 1, "default": 20},
                    {"param": "offsetZ", "label": "Line 2 Z-Offset", "min": -5, "max": 5, "step": 0.2, "default": 2.5},
                    {"param": "skewAngle", "label": "Relative Skew Angle (°)", "min": 0, "max": 180, "step": 5, "default": 65}
                ]
            }
        ],
        "problems": [
            {
                "id": "prob-geom3d-3-1",
                "tier": 1,
                "title": "Symmetrical Reduction of Non-Symmetrical Plane Form",
                "statement": r"""Find the symmetrical form of the line given as the intersection of the two planes:
$$\begin{cases} \Pi_1: x + 2y - z - 3 = 0 \\ \Pi_2: 2x - y + z - 1 = 0 \end{cases}$$
Hence, find its direction ratios and a specific point on the line.""",
                "solution": r"""**Step 1: Compute the direction vector of the line**  
The normal vectors to the planes are:
$$\vec{n}_1 = (1, 2, -1), \qquad \vec{n}_2 = (2, -1, 1)$$

The direction vector $\vec{d} = (l, m, n)$ of the line is perpendicular to both $\vec{n}_1$ and $\vec{n}_2$:
$$\vec{d} = \vec{n}_1 \times \vec{n}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 2 & -1 \\ 2 & -1 & 1 \end{vmatrix}$$

Expanding by components:
$$l = (2)(1) - (-1)(-1) = 2 - 1 = 1$$
$$m = (-1)(2) - (1)(1) = -2 - 1 = -3$$
$$n = (1)(-1) - (2)(2) = -1 - 4 = -5$$

Thus, the direction ratios are $(l, m, n) = (1, -3, -5)$.

---

**Step 2: Find a point on the line**  
Set $z = 0$ in both plane equations:
$$\begin{cases} x + 2y = 3 \\ 2x - y = 1 \end{cases}$$

Multiply the second equation by 2 and add to the first:
$$x + 2y + 4x - 2y = 3 + 2 \implies 5x = 5 \implies x = 1$$
Substitute $x = 1$ back:
$$2(1) - y = 1 \implies y = 1$$

Thus, the point $P_0(1, 1, 0)$ lies on the line.

---

**Step 3: Write the symmetrical equation**  
$$\frac{x - 1}{1} = \frac{y - 1}{-3} = \frac{z}{-5}$$

Or equivalently, multiplying direction ratios by $-1$:
$$\frac{x - 1}{-1} = \frac{y - 1}{3} = \frac{z}{5}$$"""
            },
            {
                "id": "prob-geom3d-3-2",
                "tier": 2,
                "title": "Shortest Distance Between Two Skew Lines",
                "statement": r"""Find the shortest distance between the two skew lines:
$$\mathcal{L}_1: \frac{x - 3}{1} = \frac{y - 5}{-2} = \frac{z - 7}{1}$$
$$\mathcal{L}_2: \frac{x + 1}{7} = \frac{y + 1}{-6} = \frac{z + 1}{1}$$
Determine also whether the lines intersect.""",
                "solution": r"""**Step 1: Identify reference points and direction vectors**  
- Line $\mathcal{L}_1$: passes through $A(x_1, y_1, z_1) = (3, 5, 7)$ with direction $\vec{d}_1 = (1, -2, 1)$.
- Line $\mathcal{L}_2$: passes through $B(x_2, y_2, z_2) = (-1, -1, -1)$ with direction $\vec{d}_2 = (7, -6, 1)$.

The connecting vector $\vec{AB} = \vec{r}_2 - \vec{r}_1$ is:
$$\vec{AB} = (-1 - 3)\hat{i} + (-1 - 5)\hat{j} + (-1 - 7)\hat{k} = (-4, -6, -8)$$

---

**Step 2: Compute the cross product $\vec{d}_1 \times \vec{d}_2$**  
$$\vec{d}_1 \times \vec{d}_2 = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & -2 & 1 \\ 7 & -6 & 1 \end{vmatrix}$$

$$l = (-2)(1) - (1)(-6) = -2 + 6 = 4$$
$$m = (1)(7) - (1)(1) = 7 - 1 = 6$$
$$n = (1)(-6) - (-2)(7) = -6 + 14 = 8$$

Thus, $\vec{d}_1 \times \vec{d}_2 = 4\hat{i} + 6\hat{j} + 8\hat{k}$.

Its magnitude is:
$$|\vec{d}_1 \times \vec{d}_2| = \sqrt{4^2 + 6^2 + 8^2} = \sqrt{16 + 36 + 64} = \sqrt{116} = 2\sqrt{29}$$

---

**Step 3: Evaluate the scalar triple product (numerator)**  
$$\Delta = \vec{AB} \cdot (\vec{d}_1 \times \vec{d}_2) = (-4)(4) + (-6)(6) + (-8)(8)$$
$$\Delta = -16 - 36 - 64 = -116$$

---

**Step 4: Compute the shortest distance**  
$$d = \frac{|\Delta|}{|\vec{d}_1 \times \vec{d}_2|} = \frac{|-116|}{2\sqrt{29}} = \frac{116}{2\sqrt{29}} = \frac{58}{\sqrt{29}} = 2\sqrt{29}$$

Numerically, $2\sqrt{29} \approx 2 \times 5.3852 = 10.77$ units.  
Since $d \neq 0$, the lines do not intersect; they are skew."""
            },
            {
                "id": "prob-geom3d-3-3",
                "tier": 3,
                "title": "Coplanarity Proof, Common Plane, and Point of Intersection",
                "statement": r"""Prove that the two lines:
$$\mathcal{L}_1: \frac{x - 1}{2} = \frac{y - 2}{3} = \frac{z - 3}{4}$$
$$\mathcal{L}_2: \frac{x - 2}{3} = \frac{y - 3}{4} = \frac{z - 4}{5}$$
are coplanar. Find:
(a) The coordinates of their unique point of intersection.  
(b) The Cartesian equation of the plane containing both lines.""",
                "solution": r"""**Part (a): Test for Coplanarity**  
From $\mathcal{L}_1$: $A(x_1, y_1, z_1) = (1, 2, 3)$, direction $(l_1, m_1, n_1) = (2, 3, 4)$.  
From $\mathcal{L}_2$: $B(x_2, y_2, z_2) = (2, 3, 4)$, direction $(l_2, m_2, n_2) = (3, 4, 5)$.

Difference vector:
$$x_2 - x_1 = 2 - 1 = 1, \quad y_2 - y_1 = 3 - 2 = 1, \quad z_2 - z_1 = 4 - 3 = 1$$

Construct the coplanarity determinant:
$$\Delta = \begin{vmatrix} 1 & 1 & 1 \\ 2 & 3 & 4 \\ 3 & 4 & 5 \end{vmatrix}$$

Perform row operations: $R_2 \to R_2 - 2R_1$ and $R_3 \to R_3 - 3R_1$:
$$\Delta = \begin{vmatrix} 1 & 1 & 1 \\ 0 & 1 & 2 \\ 0 & 1 & 2 \end{vmatrix} = 1 \cdot (1 \cdot 2 - 2 \cdot 1) = 0$$

Since $\Delta = 0$ and the direction vectors are linearly independent ($\frac{2}{3} \neq \frac{3}{4}$), the two lines are coplanar and intersect at a unique point.

---

**Part (b): Coordinates of the Point of Intersection**  
Express general points on both lines using parameters $s$ and $t$:
$$P_1(s) = (1 + 2s, \; 2 + 3s, \; 3 + 4s)$$
$$P_2(t) = (2 + 3t, \; 3 + 4t, \; 4 + 5t)$$

Equating coordinates:
$$1 + 2s = 2 + 3t \implies 2s - 3t = 1 \quad \text{--- (1)}$$
$$2 + 3s = 3 + 4t \implies 3s - 4t = 1 \quad \text{--- (2)}$$

From $3 \times (1) - 2 \times (2)$:
$$6s - 9t - (6s - 8t) = 3 - 2 \implies -t = 1 \implies t = -1$$
Substituting $t = -1$ into (1):
$$2s - 3(-1) = 1 \implies 2s + 3 = 1 \implies 2s = -2 \implies s = -1$$

Check third coordinate for consistency:
$$z_1 = 3 + 4(-1) = -1, \qquad z_2 = 4 + 5(-1) = -1 \quad \checkmark$$

Substituting $s = -1$ into $P_1$:
$$x = 1 + 2(-1) = -1, \quad y = 2 + 3(-1) = -1, \quad z = 3 + 4(-1) = -1$$

Thus, the lines intersect at $(-1, -1, -1)$.

---

**Part (c): Equation of the Common Plane**  
The plane contains point $A(1, 2, 3)$ and direction vectors $(2, 3, 4)$ and $(3, 4, 5)$:
$$\begin{vmatrix} x - 1 & y - 2 & z - 3 \\ 2 & 3 & 4 \\ 3 & 4 & 5 \end{vmatrix} = 0$$

Expanding along the first row:
$$(x - 1)(15 - 16) - (y - 2)(10 - 12) + (z - 3)(8 - 9) = 0$$
$$-(x - 1) + 2(y - 2) - (z - 3) = 0$$
$$-x + 1 + 2y - 4 - z + 3 = 0 \implies -x + 2y - z = 0$$

Multiplying by $-1$:
$$x - 2y + z = 0$$

This is the exact Cartesian equation of the plane containing both lines."""
            }
        ]
    }

def build_unit_4():
    return {
        "id": "geom3d-u4",
        "title": "Unit 4: The Sphere in Space",
        "description": "Complete study of spheres in 3D: general quadratic form, circular plane sections, tangent and polar planes, orthogonality condition, and radical planes, lines, and centers.",
        "sections": [
            {
                "id": "sec-geom3d-4-1",
                "title": "4.1 Standard and General Equations of a Sphere",
                "content": r"""A **sphere** is the locus of a point in three-dimensional space that moves such that its Euclidean distance from a fixed point (the center) remains constant (the radius).

---

### 1. Standard Center-Radius Form

Let $C(a, b, c)$ be the center and $R > 0$ be the radius. If $P(x, y, z)$ is any point on the sphere, then by the distance formula:

$$|\vec{CP}|^2 = (x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$$

Expanding this expression:

$$x^2 + y^2 + z^2 - 2ax - 2by - 2cz + (a^2 + b^2 + c^2 - R^2) = 0$$

---

### 2. General Second-Degree Equation of a Sphere

The general equation of second degree in $x, y, z$:

$$A x^2 + B y^2 + C z^2 + 2F yz + 2G zx + 2H xy + 2ux + 2vy + 2wz + d = 0$$

represents a sphere if and only if:
1. The coefficients of $x^2, y^2, z^2$ are equal: $A = B = C \neq 0$.
2. The product terms vanish: $F = G = H = 0$ (no $yz, zx, xy$ terms).

Dividing through by $A$, the standard general equation of a sphere is:

$$x^2 + y^2 + z^2 + 2ux + 2vy + 2wz + d = 0$$

Completing the square in each variable:

$$(x + u)^2 + (y + v)^2 + (z + w)^2 = u^2 + v^2 + w^2 - d$$

From this canonical form, we deduce:
- **Center:** $(-u, -v, -w)$
- **Radius:** $R = \sqrt{u^2 + v^2 + w^2 - d}$

**Classification based on the radicand:**
- If $u^2 + v^2 + w^2 - d > 0$: **Real sphere** with non-zero radius.
- If $u^2 + v^2 + w^2 - d = 0$: **Point sphere** (degenerate sphere of radius 0).
- If $u^2 + v^2 + w^2 - d < 0$: **Virtual / Imaginary sphere** (no real points satisfy the equation).

---

### 3. Sphere with Given Diameter Endpoints

If $A(x_1, y_1, z_1)$ and $B(x_2, y_2, z_2)$ are the diametrically opposite extremities of a sphere, then for any point $P(x, y, z)$ on the surface, the vectors $\vec{AP}$ and $\vec{BP}$ are orthogonal (Thales' theorem in 3D):

$$\vec{AP} \cdot \vec{BP} = 0$$

In Cartesian components:

$$(x - x_1)(x - x_2) + (y - y_1)(y - y_2) + (z - z_1)(z - z_2) = 0$$

---

### 4. Sphere Passing Through Four Given Points

Four non-coplanar points $P_i(x_i, y_i, z_i)$ for $i = 1, 2, 3, 4$ uniquely specify a sphere. The equation can be represented compactly as a $5 \times 5$ determinant:

$$\begin{vmatrix}
x^2 + y^2 + z^2 & x & y & z & 1 \\
x_1^2 + y_1^2 + z_1^2 & x_1 & y_1 & z_1 & 1 \\
x_2^2 + y_2^2 + z_2^2 & x_2 & y_2 & z_2 & 1 \\
x_3^2 + y_3^2 + z_3^2 & x_3 & y_3 & z_3 & 1 \\
x_4^2 + y_4^2 + z_4^2 & x_4 & y_4 & z_4 & 1
\end{vmatrix} = 0$$"""
            },
            {
                "id": "sec-geom3d-4-2",
                "title": "4.2 Plane Section of a Sphere and Tangent Planes",
                "content": r"""### 1. Plane Section of a Sphere

Every planar section of a sphere is a **circle**.

Let a sphere have center $C$ and radius $R$. Let a plane $\Pi$ be at perpendicular distance $p$ from $C$.
- If $p < R$: The intersection is a **real circle** with radius $r = \sqrt{R^2 - p^2}$.
- If $p = R$: The plane is tangent to the sphere, intersecting at a single point (radius 0).
- If $p > R$: The intersection is virtual (no real intersection).

#### Determining the Center and Radius of the Circular Section:
1. **Center of Circle ($K$):** The foot of the perpendicular dropped from sphere center $C(-u, -v, -w)$ onto the intersecting plane $\Pi: ax + by + cz + d = 0$.
2. **Perpendicular distance $p$:**
   $$p = \frac{|a(-u) + b(-v) + c(-w) + d|}{\sqrt{a^2 + b^2 + c^2}}$$
3. **Radius of Circle:** $r = \sqrt{R^2 - p^2}$.
4. **Great Circle:** When $p = 0$ (the intersecting plane passes through the center of the sphere), $r = R$. This is a **great circle**; all other sections with $0 < p < R$ are **small circles**.

---

### 2. Tangent Plane to a Sphere

Let $P(x_1, y_1, z_1)$ be a point lying on the sphere $S: x^2 + y^2 + z^2 + 2ux + 2vy + 2wz + d = 0$.

The normal to the tangent plane at $P$ is directed along the radius vector $\vec{CP} = (x_1 + u)\hat{i} + (y_1 + v)\hat{j} + (z_1 + w)\hat{k}$.

Using the point-normal form of a plane $\vec{CP} \cdot (\vec{r} - \vec{r}_1) = 0$ and the fact that $P$ satisfies the sphere equation, the **tangent plane** at $(x_1, y_1, z_1)$ is:

$$x x_1 + y y_1 + z z_1 + u(x + x_1) + v(y + y_1) + w(z + z_1) + d = 0$$

> **Rule of Thumb (Quadratic Substitution):**  
> Replace $x^2 \to x x_1$, $y^2 \to y y_1$, $z^2 \to z z_1$, $2x \to x + x_1$, $2y \to y + y_1$, $2z \to z + z_1$.

#### Condition of Tangency of a Plane
A plane $l x + m y + n z = p$ is tangent to the sphere $(x-a)^2 + (y-b)^2 + (z-c)^2 = R^2$ if and only if the perpendicular distance from the center $(a, b, c)$ to the plane equals the radius $R$:

$$\frac{|l a + m b + n c - p|}{\sqrt{l^2 + m^2 + n^2}} = R \implies (la + mb + nc - p)^2 = R^2(l^2 + m^2 + n^2)$$"""
            },
            {
                "id": "sec-geom3d-4-3",
                "title": "4.3 Orthogonal Spheres and Radical Systems",
                "content": r"""### 1. Orthogonality Condition for Two Spheres

Two spheres are defined to be **orthogonal** if their tangent planes at any point of intersection are perpendicular to each other. Equivalently, the radii drawn to a point of intersection are mutually perpendicular.

Let $S_1$ and $S_2$ be two spheres with centers $C_1(-u_1, -v_1, -w_1)$ and $C_2(-u_2, -v_2, -w_2)$, and radii $R_1, R_2$:

$$S_1: x^2 + y^2 + z^2 + 2u_1 x + 2v_1 y + 2w_1 z + d_1 = 0 \quad (R_1^2 = u_1^2 + v_1^2 + w_1^2 - d_1)$$
$$S_2: x^2 + y^2 + z^2 + 2u_2 x + 2v_2 y + 2w_2 z + d_2 = 0 \quad (R_2^2 = u_2^2 + v_2^2 + w_2^2 - d_2)$$

At any point of intersection $P$, the triangle $C_1 P C_2$ is a right-angled triangle with hypotenuse $C_1 C_2$. By the Pythagorean Theorem:

$$|C_1 C_2|^2 = R_1^2 + R_2^2$$

Computing the square of the distance between centers:
$$|C_1 C_2|^2 = (-u_1 + u_2)^2 + (-v_1 + v_2)^2 + (-w_1 + w_2)^2$$
$$= (u_1 - u_2)^2 + (v_1 - v_2)^2 + (w_1 - w_2)^2$$
$$= (u_1^2 + v_1^2 + w_1^2) + (u_2^2 + v_2^2 + w_2^2) - 2(u_1 u_2 + v_1 v_2 + w_1 w_2)$$

Substitute $R_1^2 = u_1^2 + v_1^2 + w_1^2 - d_1$ and $R_2^2 = u_2^2 + v_2^2 + w_2^2 - d_2$:

$$(u_1^2 + v_1^2 + w_1^2) + (u_2^2 + v_2^2 + w_2^2) - 2(u_1 u_2 + v_1 v_2 + w_1 w_2) = (u_1^2 + v_1^2 + w_1^2 - d_1) + (u_2^2 + v_2^2 + w_2^2 - d_2)$$

Canceling common squared terms:

$$-2(u_1 u_2 + v_1 v_2 + w_1 w_2) = -d_1 - d_2$$

$$\mathbf{2u_1 u_2 + 2v_1 v_2 + 2w_1 w_2 = d_1 + d_2}$$

This is the **fundamental condition for orthogonality** of two spheres.

---

### 2. Radical Plane

The **power** of a point $P(x, y, z)$ with respect to a sphere $S = x^2 + y^2 + z^2 + 2ux + 2vy + 2wz + d = 0$ is the value $S(x, y, z)$. Geometrically, if tangents are drawn from $P$ to the sphere, the square of the length of each tangent equals the power of $P$.

The **radical plane** of two spheres $S_1 = 0$ and $S_2 = 0$ is the locus of points whose powers with respect to both spheres are equal:

$$S_1 - S_2 = 0$$

Subtracting the two equations eliminates the quadratic terms $x^2 + y^2 + z^2$:

$$2(u_1 - u_2)x + 2(v_1 - v_2)y + 2(w_1 - w_2)z + (d_1 - d_2) = 0$$

#### Fundamental Properties:
1. **Perpendicularity to Line of Centers:** The normal vector to the radical plane is $(u_1 - u_2, v_1 - v_2, w_1 - w_2)$. The vector joining centers $C_1$ and $C_2$ is $(u_1 - u_2, v_1 - v_2, w_1 - w_2)$. Hence, the radical plane is always perpendicular to the line joining the centers of the two spheres.
2. **Intersection Circle:** If two spheres intersect, their radical plane is the plane containing their common circular curve of intersection.

---

### 3. Radical Line and Radical Center

- **Radical Line:** For three spheres $S_1, S_2, S_3$, the three radical planes taken in pairs ($S_1 - S_2 = 0$, $S_2 - S_3 = 0$, $S_3 - S_1 = 0$) intersect in a single common line called the **radical line**.
- **Radical Center:** For four spheres whose centers are non-coplanar, the radical planes taken in pairs intersect at a single unique point called the **radical center**. Tangents drawn from the radical center to all four spheres are equal in length."""
            }
        ],
        "simulations": [
            {
                "id": "sim_geom3d_spheres",
                "title": "3D Interactive Spheres, Orthogonality & Radical Plane Engine",
                "description": "Visualize two spheres intersecting in 3D space. Adjust radii, center separation, and toggle between orthogonal intersection angle and the dynamic radical cutting plane.",
                "controls": [
                    {"param": "r1", "label": "Sphere 1 Radius", "min": 1.0, "max": 4.0, "step": 0.1, "default": 2.5},
                    {"param": "r2", "label": "Sphere 2 Radius", "min": 1.0, "max": 4.0, "step": 0.1, "default": 2.0},
                    {"param": "dist", "label": "Center Distance d", "min": 1.5, "max": 6.0, "step": 0.1, "default": 3.2},
                    {"param": "showRadical", "label": "Show Radical Plane", "min": 0, "max": 1, "step": 1, "default": 1}
                ]
            }
        ],
        "problems": [
            {
                "id": "prob-geom3d-4-1",
                "tier": 1,
                "title": "Sphere Passing Through Origin and Three Axis Intercepts",
                "statement": r"""Find the equation of the sphere passing through the origin $O(0, 0, 0)$ and the three coordinate intercept points $A(a, 0, 0)$, $B(0, b, 0)$, and $C(0, 0, c)$ where $a, b, c \neq 0$. Find its center and radius.""",
                "solution": r"""**Step 1: Set up the general equation**  
Let the sphere equation be:
$$x^2 + y^2 + z^2 + 2ux + 2vy + 2wz + d = 0$$

---

**Step 2: Apply the four point conditions**  
1. Passes through $(0, 0, 0)$:
   $$0 + 0 + 0 + 0 + 0 + 0 + d = 0 \implies d = 0$$

2. Passes through $A(a, 0, 0)$:
   $$a^2 + 0 + 0 + 2ua + 0 + 0 + 0 = 0 \implies a(a + 2u) = 0$$
   Since $a \neq 0$, $2u = -a \implies u = -\frac{a}{2}$.

3. Passes through $B(0, b, 0)$:
   $$b^2 + 2vb = 0 \implies 2v = -b \implies v = -\frac{b}{2}$$.

4. Passes through $C(0, 0, c)$:
   $$c^2 + 2wc = 0 \implies 2w = -c \implies w = -\frac{c}{2}$$.

---

**Step 3: Construct the sphere equation**  
$$x^2 + y^2 + z^2 - ax - by - cz = 0$$

---

**Step 4: Find center and radius**  
- **Center:** $(-u, -v, -w) = \left(\frac{a}{2}, \frac{b}{2}, \frac{c}{2}\right)$.
- **Radius:**
  $$R = \sqrt{u^2 + v^2 + w^2 - d} = \sqrt{\left(-\frac{a}{2}\right)^2 + \left(-\frac{b}{2}\right)^2 + \left(-\frac{c}{2}\right)^2 - 0}$$
  $$R = \frac{1}{2}\sqrt{a^2 + b^2 + c^2}$$"""
            },
            {
                "id": "prob-geom3d-4-2",
                "tier": 2,
                "title": "Center and Radius of a Circular Section of a Sphere",
                "statement": r"""Find the center and the radius of the circular section produced by cutting the sphere:
$$S: x^2 + y^2 + z^2 - 2y - 4z - 11 = 0$$
with the plane:
$$\Pi: x + 2y + 2z - 15 = 0$$""",
                "solution": r"""**Step 1: Find the center and radius of the sphere**  
Comparing with $x^2 + y^2 + z^2 + 2ux + 2vy + 2wz + d = 0$:
$$u = 0, \quad v = -1, \quad w = -2, \quad d = -11$$

- **Center $C$:** $(-u, -v, -w) = (0, 1, 2)$.
- **Radius $R$:**
  $$R = \sqrt{0^2 + (-1)^2 + (-2)^2 - (-11)} = \sqrt{1 + 4 + 11} = \sqrt{16} = 4$$

---

**Step 2: Perpendicular distance $p$ from center to plane**  
Plane equation is $x + 2y + 2z - 15 = 0$.
$$p = \frac{|1(0) + 2(1) + 2(2) - 15|}{\sqrt{1^2 + 2^2 + 2^2}} = \frac{|0 + 2 + 4 - 15|}{\sqrt{1 + 4 + 4}} = \frac{|-9|}{\sqrt{9}} = \frac{9}{3} = 3$$

Since $p = 3 < R = 4$, the intersection is a real circle.

---

**Step 3: Radius of the circular section**  
$$r = \sqrt{R^2 - p^2} = \sqrt{4^2 - 3^2} = \sqrt{16 - 9} = \sqrt{7}$$

---

**Step 4: Center of the circular section (foot of perpendicular)**  
The line through center $C(0, 1, 2)$ perpendicular to plane $\Pi$ has direction ratios $(1, 2, 2)$:
$$\frac{x - 0}{1} = \frac{y - 1}{2} = \frac{z - 2}{2} = k$$

Any point on this normal line is $(k, 1 + 2k, 2 + 2k)$.  
Substitute into the plane equation:
$$k + 2(1 + 2k) + 2(2 + 2k) - 15 = 0$$
$$k + 2 + 4k + 4 + 4k - 15 = 0$$
$$9k - 9 = 0 \implies k = 1$$

Substitute $k = 1$ to get the center $K$:
$$x = 1, \quad y = 1 + 2(1) = 3, \quad z = 2 + 2(1) = 4$$

Thus, the circular section has **center $(1, 3, 4)$** and **radius $\sqrt{7}$**."""
            },
            {
                "id": "prob-geom3d-4-3",
                "tier": 3,
                "title": "Orthogonality and Radical Plane Verification",
                "statement": r"""Consider two spheres:
$$S_1: x^2 + y^2 + z^2 + 6x - 2y + 2z - 14 = 0$$
$$S_2: x^2 + y^2 + z^2 - 4x + 4y - 6z + 4 = 0$$
(a) Determine whether the two spheres intersect orthogonally.  
(b) Find the Cartesian equation of their radical plane.  
(c) Prove analytically that the radical plane is strictly perpendicular to the line of centers $\vec{C_1 C_2}$.""",
                "solution": r"""**Part (a): Orthogonality Test**  
Extract coefficients from $S_1$:
$$2u_1 = 6 \implies u_1 = 3, \quad 2v_1 = -2 \implies v_1 = -1, \quad 2w_1 = 2 \implies w_1 = 1, \quad d_1 = -14$$
Center $C_1 = (-3, 1, -1)$.

Extract coefficients from $S_2$:
$$2u_2 = -4 \implies u_2 = -2, \quad 2v_2 = 4 \implies v_2 = 2, \quad 2w_2 = -6 \implies w_2 = -3, \quad d_2 = 4$$
Center $C_2 = (2, -2, 3)$.

Evaluate the orthogonality condition $2u_1 u_2 + 2v_1 v_2 + 2w_1 w_2 = d_1 + d_2$:
$$\text{LHS} = 2(3)(-2) + 2(-1)(2) + 2(1)(-3) = -12 - 4 - 6 = -22$$
$$\text{RHS} = d_1 + d_2 = -14 + 4 = -10$$

Since $\text{LHS} \neq \text{RHS}$ ($-22 \neq -10$), the spheres are **not orthogonal**.

---

**Part (b): Equation of Radical Plane**  
The radical plane is given by $S_1 - S_2 = 0$:
$$(x^2 + y^2 + z^2 + 6x - 2y + 2z - 14) - (x^2 + y^2 + z^2 - 4x + 4y - 6z + 4) = 0$$
$$(6 - (-4))x + (-2 - 4)y + (2 - (-6))z + (-14 - 4) = 0$$
$$10x - 6y + 8z - 18 = 0$$

Dividing by 2:
$$5x - 3y + 4z - 9 = 0$$

---

**Part (c): Perpendicularity to the Line of Centers**  
The normal vector to the radical plane $\Pi_{rad}$ is:
$$\vec{n}_{rad} = (5, -3, 4)$$

The line of centers connects $C_1(-3, 1, -1)$ and $C_2(2, -2, 3)$:
$$\vec{C_1 C_2} = (2 - (-3))\hat{i} + (-2 - 1)\hat{j} + (3 - (-1))\hat{k} = (5, -3, 4)$$

Notice that:
$$\vec{n}_{rad} = \vec{C_1 C_2} = (5, -3, 4)$$

Since the normal vector of the radical plane is parallel (in fact, identical) to the line connecting the centers, the radical plane is **strictly perpendicular** to the line of centers. $\blacksquare$"""
            }
        ]
    }

if __name__ == "__main__":
    print("Building 3D Geometry: Units 3 & 4...")
    u3 = build_unit_3()
    with open("geom3d_u3.json", "w", encoding="utf-8") as f:
        json.dump(u3, f, indent=2, ensure_ascii=False)
    print("Saved geom3d_u3.json successfully.")

    u4 = build_unit_4()
    with open("geom3d_u4.json", "w", encoding="utf-8") as f:
        json.dump(u4, f, indent=2, ensure_ascii=False)
    print("Saved geom3d_u4.json successfully.")
