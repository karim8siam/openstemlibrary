import json

def build_unit_5():
    return {
        "id": "calc3-u5",
        "title": "Unit 5: Multiple Integration: Double Integrals over General Regions & Polar Coordinates",
        "description": "Rigorous development of double integrals: Riemann sums, Fubini's theorem, Type I and Type II planar domains, reversing limits of integration, laminar centroids, polar sector transformations, and the Gaussian integral.",
        "sections": [
            {
                "id": "u5-sec1",
                "title": "Double Integrals over Rectangles & Fubini's Theorem",
                "content": r"""### 1. Definition via Double Riemann Sums

Let $f(x, y)$ be defined on a closed rectangle $R = [a, b] \times [c, d] = \{ (x, y) \in \mathbb{R}^2 : a \le x \le b, \; c \le y \le d \}$.

Partition $[a, b]$ into $m$ subintervals of width $\Delta x = \frac{b - a}{m}$, and $[c, d]$ into $n$ subintervals of width $\Delta y = \frac{d - c}{n}$. This divides $R$ into $m \times n$ subrectangles $R_{ij}$, each with area $\Delta A = \Delta x \Delta y$.

Choose a sample point $(x_{ij}^*, y_{ij}^*) \in R_{ij}$. The **double Riemann sum** is:

$$S_{mn} = \sum_{i=1}^m \sum_{j=1}^n f(x_{ij}^*, y_{ij}^*) \Delta A$$

**Definition:**  
If the limit exists as $m, n \to \infty$ independently of the choice of sample points, we say $f$ is integrable over $R$, and define the **double integral**:

$$\mathbf{\iint_R f(x, y) \, dA = \lim_{m, n \to \infty} \sum_{i=1}^m \sum_{j=1}^n f(x_{ij}^*, y_{ij}^*) \Delta A}$$

If $f(x, y) \ge 0$, the double integral represents the exact **volume** of the solid that lies above the rectangle $R$ and below the surface $z = f(x, y)$.

---

### 2. Fubini's Theorem on Rectangles

Evaluating a double limit of double sums directly is impractical. Guido Fubini (1907) proved that double integrals can be evaluated through two successive single-variable integrations.

**Theorem (Fubini's Theorem):**  
If $f(x, y)$ is continuous on the rectangle $R = [a, b] \times [c, d]$, then:

$$\mathbf{\iint_R f(x, y) \, dA = \int_a^b \left( \int_c^d f(x, y) \, dy \right) dx = \int_c^d \left( \int_a^b f(x, y) \, dx \right) dy}$$

That is, the double integral can be evaluated as an **iterated integral** in either order ($dy \, dx$ or $dx \, dy$), yielding identical results.

---

### 3. Factorization Property for Separable Integrands

If $f(x, y) = g(x) h(y)$ is separable into independent functions on $R = [a, b] \times [c, d]$:

$$\iint_R g(x) h(y) \, dA = \int_a^b g(x) \left( \int_c^d h(y) \, dy \right) dx = \left( \int_a^b g(x) \, dx \right) \left( \int_c^d h(y) \, dy \right)$$

This allows immediate factorization of 2D integrals into the product of two independent 1D integrals."""
            },
            {
                "id": "u5-sec2",
                "title": "Double Integrals over General Non-Rectangular Regions",
                "content": r"""Most regions of integration in applications are not rectangles. We classify bounded planar regions into two standard categories:

---

### 1. Type I Regions (Vertically Simple)

A planar region $D$ is of **Type I** if it lies between the vertical lines $x = a$ and $x = b$, bounded below by continuous curve $y = g_1(x)$ and above by $y = g_2(x)$:

$$D = \{ (x, y) \in \mathbb{R}^2 : a \le x \le b, \quad g_1(x) \le y \le g_2(x) \}$$

By slicing with vertical lines (integrating with respect to $y$ first):

$$\mathbf{\iint_D f(x, y) \, dA = \int_a^b \left( \int_{g_1(x)}^{g_2(x)} f(x, y) \, dy \right) dx}$$

---

### 2. Type II Regions (Horizontally Simple)

A planar region $D$ is of **Type II** if it lies between the horizontal lines $y = c$ and $y = d$, bounded on the left by $x = h_1(y)$ and on the right by $x = h_2(y)$:

$$D = \{ (x, y) \in \mathbb{R}^2 : c \le y \le d, \quad h_1(y) \le x \le h_2(y) \}$$

By slicing with horizontal lines (integrating with respect to $x$ first):

$$\mathbf{\iint_D f(x, y) \, dA = \int_c^d \left( \int_{h_1(y)}^{h_2(y)} f(x, y) \, dx \right) dy}$$

---

### 3. Reversing the Order of Integration

Certain integrands possess no elementary antiderivative in one variable, but become trivial when integrated in the other order (e.g., $\int e^{y^2} dy$ has no elementary form, but $\int y e^{y^2} dy$ is standard).

#### Procedure to Reverse Order:
1. Extract the inequalities defining the region $D$ from the given integral limits.
2. Sketch the geometric domain $D$ in the $xy$-plane, identifying all boundary intersections.
3. Express the same geometric region from the opposite perspective (convert Type I to Type II, or vice versa).
4. Re-integrate in the reversed order.

---

### 4. Physical Applications of Double Integrals

1. **Planar Area:** $\mathbf{A(D) = \iint_D 1 \, dA}$
2. **Total Mass of a Thin Plate:** If $\rho(x, y)$ is mass density: $\mathbf{M = \iint_D \rho(x, y) \, dA}$
3. **Center of Mass (Centroid):**
   $$\bar{x} = \frac{1}{M}\iint_D x\rho(x, y) \, dA, \qquad \bar{y} = \frac{1}{M}\iint_D y\rho(x, y) \, dA$$
4. **Moments of Inertia:**
   $$I_x = \iint_D y^2 \rho(x, y) \, dA, \quad I_y = \iint_D x^2 \rho(x, y) \, dA, \quad I_0 = I_x + I_y = \iint_D (x^2 + y^2)\rho(x, y) \, dA$$"""
            },
            {
                "id": "u5-sec3",
                "title": "Double Integrals in Polar Coordinates and the Gaussian Integral",
                "content": r"""### 1. The Polar Area Differential Element

When converting from Cartesian coordinates $(x, y)$ to polar coordinates $(r, \theta)$ via $x = r\cos\theta, y = r\sin\theta$:

A polar rectangle is defined by $a \le r \le b, \alpha \le \theta \le \beta$.  
Consider a small polar subrectangle bounded by radius $r$ to $r + \Delta r$ and angle $\theta$ to $\theta + \Delta\theta$.

The area of this circular wedge is:
$$\Delta A = \frac{1}{2}(r + \Delta r)^2 \Delta\theta - \frac{1}{2}r^2 \Delta\theta = \frac{1}{2}(r^2 + 2r\Delta r + (\Delta r)^2 - r^2)\Delta\theta = \left( r + \frac{\Delta r}{2} \right) \Delta r \Delta\theta$$
Letting $\bar{r} = r + \frac{\Delta r}{2}$ denote the average radius, in the infinitesimal limit:

$$\mathbf{dA = r \, dr \, d\theta}$$

> **The Extra Factor of $r$:**  
> The factor $r$ is the Jacobian determinant of the polar coordinate transformation:
> $$J = \frac{\partial(x, y)}{\partial(r, \theta)} = \begin{vmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{vmatrix} = r\cos^2\theta + r\sin^2\theta = r$$

---

### 2. Integration Formula in Polar Coordinates

If a region $R$ is described in polar coordinates by $\alpha \le \theta \le \beta, h_1(\theta) \le r \le h_2(\theta)$:

$$\mathbf{\iint_R f(x, y) \, dA = \int_\alpha^\beta \int_{h_1(\theta)}^{h_2(\theta)} f(r\cos\theta, \; r\sin\theta) \; r \, dr \, d\theta}$$

---

### 3. Rigorous Evaluation of the Gaussian Integral

The improper Gaussian integral $I = \int_{-\infty}^\infty e^{-x^2} dx$ cannot be evaluated in single-variable calculus because $e^{-x^2}$ has no elementary antiderivative.

**Theorem:**  
$$\mathbf{\int_{-\infty}^\infty e^{-x^2} \, dx = \sqrt{\pi}}$$

#### Proof:
Consider the square of the integral:
$$I^2 = \left( \int_{-\infty}^\infty e^{-x^2} \, dx \right) \left( \int_{-\infty}^\infty e^{-y^2} \, dy \right) = \int_{-\infty}^\infty \int_{-\infty}^\infty e^{-(x^2 + y^2)} \, dx \, dy$$

This represents a double integral over the entire infinite plane $\mathbb{R}^2$.  
Transform to polar coordinates $x^2 + y^2 = r^2$ with $0 \le r < \infty$ and $0 \le \theta \le 2\pi$:

$$I^2 = \int_0^{2\pi} \int_0^\infty e^{-r^2} (r \, dr \, d\theta) = \left( \int_0^{2\pi} d\theta \right) \left( \int_0^\infty r e^{-r^2} \, dr \right)$$
$$= 2\pi \lim_{b \to \infty} \left[ -\frac{1}{2} e^{-r^2} \right]_0^b = 2\pi \left( 0 - \left(-\frac{1}{2}\right) \right) = 2\pi \left( \frac{1}{2} \right) = \pi$$

Taking the positive square root:
$$I = \sqrt{\pi} \quad \blacksquare$$"""
            }
        ],
        "simulations": [
            {
                "id": "sim_calc3_double_integrals",
                "title": "Double Riemann Slices & Polar Region Engine",
                "description": "Visualize 3D volumes under surfaces, switch between Cartesian rectangular grid slices and polar sector wedges, and observe double Riemann sum convergence in real time.",
                "controls": [
                    {"param": "gridMode", "label": "Grid (0:Cartesian, 1:Polar)", "min": 0, "max": 1, "step": 1, "default": 0},
                    {"param": "slicesN", "label": "Number of Partitions", "min": 4, "max": 30, "step": 2, "default": 14},
                    {"param": "heightScale", "label": "Surface Amplitude", "min": 0.5, "max": 2.5, "step": 0.1, "default": 1.5},
                    {"param": "rotY", "label": "Orbit Yaw (°)", "min": -180, "max": 180, "step": 2, "default": 35}
                ]
            }
        ],
        "problems": [
            {
                "id": "prob-calc3-5-1",
                "tier": 1,
                "title": "Evaluation by Reversing the Order of Integration",
                "statement": r"""Evaluate the iterated integral:
$$\int_0^1 \int_x^1 \sin(y^2) \, dy \, dx$$
by reversing the order of integration.""",
                "solution": r"""**Step 1: Identify and sketch the region of integration $D$**  
From the given limits:
- Outer integral: $0 \le x \le 1$
- Inner integral: $x \le y \le 1$

The region $D$ is bounded by:
- $y = x$ (bottom boundary)
- $y = 1$ (top boundary)
- $x = 0$ (left boundary, $y$-axis)

This is a triangle with vertices at $(0, 0)$, $(0, 1)$, and $(1, 1)$.

---

**Step 2: Express the region as Type II (horizontal slices)**  
Viewing the triangle horizontally:
- $y$ varies from $0$ to $1$: $0 \le y \le 1$
- For a fixed $y$, $x$ enters at the $y$-axis ($x = 0$) and exits at the line $x = y$: $0 \le x \le y$

---

**Step 3: Re-write and evaluate the integral**  
$$\int_0^1 \int_x^1 \sin(y^2) \, dy \, dx = \int_0^1 \left( \int_0^y \sin(y^2) \, dx \right) dy$$

Integrate with respect to $x$ (treating $\sin(y^2)$ as constant):
$$\int_0^y \sin(y^2) \, dx = [x \sin(y^2)]_{x=0}^{x=y} = y \sin(y^2) - 0 = y \sin(y^2)$$

Now evaluate the outer integral with respect to $y$:
$$\int_0^1 y \sin(y^2) \, dy$$

Let $u = y^2 \implies du = 2y \, dy \implies y \, dy = \frac{1}{2} du$.  
When $y = 0$, $u = 0$; when $y = 1$, $u = 1$:
$$\int_0^1 y \sin(y^2) \, dy = \frac{1}{2} \int_0^1 \sin(u) \, du = \frac{1}{2} [-\cos(u)]_0^1 = \frac{1}{2}(1 - \cos 1)$$

$$\mathbf{\int_0^1 \int_x^1 \sin(y^2) \, dy \, dx = \frac{1 - \cos 1}{2}} \approx 0.2298$$"""
            },
            {
                "id": "prob-calc3-5-2",
                "tier": 2,
                "title": "Volume of Paraboloid Solid via Polar Double Integral",
                "statement": r"""Find the volume of the solid bounded above by the circular paraboloid:
$$z = 4 - x^2 - y^2$$
and bounded below by the $xy$-plane ($z = 0$).""",
                "solution": r"""**Step 1: Determine the region of integration $R$ in the $xy$-plane**  
The surface intersects the $xy$-plane ($z = 0$) when:
$$4 - x^2 - y^2 = 0 \implies x^2 + y^2 = 4$$

This is a circle centered at the origin with radius $R = 2$.  
In polar coordinates:
$$0 \le r \le 2, \qquad 0 \le \theta \le 2\pi$$

---

**Step 2: Express the integrand in polar coordinates**  
$$z = 4 - (x^2 + y^2) = 4 - r^2$$

---

**Step 3: Set up and evaluate the polar double integral**  
Recall that $dA = r \, dr \, d\theta$:
$$V = \iint_R z \, dA = \int_0^{2\pi} \int_0^2 (4 - r^2) r \, dr \, d\theta$$
$$V = \left( \int_0^{2\pi} d\theta \right) \left( \int_0^2 (4r - r^3) \, dr \right)$$

Evaluate the independent integrals:
$$\int_0^{2\pi} d\theta = 2\pi$$
$$\int_0^2 (4r - r^3) \, dr = \left[ 2r^2 - \frac{r^4}{4} \right]_0^2 = \left( 2(4) - \frac{16}{4} \right) - 0 = 8 - 4 = 4$$

Multiply:
$$V = 2\pi \times 4 = \mathbf{8\pi} \text{ cubic units} \approx 25.133$$"""
            },
            {
                "id": "prob-calc3-5-3",
                "tier": 3,
                "title": "Centroid of Semicircular Lamina with Distance-Proportional Density",
                "statement": r"""Find the center of mass of a semicircular lamina of radius $R$ bounded by $x^2 + y^2 \le R^2$ ($y \ge 0$), where the density at any point is directly proportional to its distance from the bounding diameter (the $x$-axis): $\rho(x, y) = k y$ ($k > 0$).""",
                "solution": r"""**Step 1: Set up the Polar Description of the Lamina**  
The upper semicircular region $D$ is:
$$0 \le r \le R, \qquad 0 \le \theta \le \pi$$
Since $y = r\sin\theta$, the density function is:
$$\rho = k r \sin\theta$$

---

**Step 2: Symmetry Analysis for $\bar{x}$**  
The domain $D$ is symmetric with respect to the $y$-axis ($x = 0$), and the density $\rho(x, y) = ky$ is an even function of $x$ (it does not depend on $x$).  
Therefore, by bilateral symmetry:
$$\mathbf{\bar{x} = 0}$$

---

**Step 3: Compute the Total Mass $M$**  
$$M = \iint_D \rho \, dA = \int_0^\pi \int_0^R (k r\sin\theta) (r \, dr \, d\theta) = k \left( \int_0^\pi \sin\theta \, d\theta \right) \left( \int_0^R r^2 \, dr \right)$$

Evaluate the single integrals:
$$\int_0^\pi \sin\theta \, d\theta = [-\cos\theta]_0^\pi = -(-1) - (-1) = 2$$
$$\int_0^R r^2 \, dr = \frac{R^3}{3}$$

Thus:
$$\mathbf{M = k (2) \left(\frac{R^3}{3}\right) = \frac{2k R^3}{3}}$$

---

**Step 4: Compute the Moment about the $x$-axis $M_x$**  
$$M_x = \iint_D y \rho \, dA = \iint_D (r\sin\theta)(k r\sin\theta) r \, dr \, d\theta = k \int_0^\pi \int_0^R r^3 \sin^2\theta \, dr \, d\theta$$
$$M_x = k \left( \int_0^\pi \sin^2\theta \, d\theta \right) \left( \int_0^R r^3 \, dr \right)$$

Evaluate:
$$\int_0^\pi \sin^2\theta \, d\theta = \int_0^\pi \frac{1 - \cos 2\theta}{2} \, d\theta = \frac{\pi}{2}$$
$$\int_0^R r^3 \, dr = \frac{R^4}{4}$$

Thus:
$$\mathbf{M_x = k \left(\frac{\pi}{2}\right) \left(\frac{R^4}{4}\right) = \frac{k\pi R^4}{8}}$$

---

**Step 5: Compute the Center of Mass $\bar{y}$**  
$$\bar{y} = \frac{M_x}{M} = \frac{\frac{k\pi R^4}{8}}{\frac{2k R^3}{3}} = \frac{k\pi R^4}{8} \cdot \frac{3}{2k R^3} = \mathbf{\frac{3\pi}{16} R}$$

Numerically, $\frac{3\pi}{16} \approx 0.589 R$.  
The center of mass is located at:
$$\mathbf{(\bar{x}, \bar{y}) = \left(0, \; \frac{3\pi}{16}R\right)}$$"""
            }
        ]
    }

def build_unit_6():
    return {
        "id": "calc3-u6",
        "title": "Unit 6: Triple Integrals in Cartesian, Cylindrical & Spherical Coordinates",
        "description": "Three-dimensional volume integrals: Fubini's theorem in six permutations, cylindrical and spherical coordinate frames, and general curvilinear coordinate transformations via Jacobian determinants.",
        "sections": [
            {
                "id": "u6-sec1",
                "title": "Triple Integrals over General 3D Bounded Regions",
                "content": r"""### 1. Definition via Riemann Triple Sums

Let $f(x, y, z)$ be defined on a bounded spatial domain $E \subset \mathbb{R}^3$. Enclose $E$ inside a rectangular box $B = [a, b] \times [c, d] \times [r, s]$.

Partition $B$ into $l \times m \times n$ sub-boxes $B_{ijk}$ of dimensions $\Delta x, \Delta y, \Delta z$ with volume $\Delta V = \Delta x \Delta y \Delta z$. The **triple integral** is defined as the limit:

$$\mathbf{\iiint_E f(x, y, z) \, dV = \lim_{l, m, n \to \infty} \sum_{i=1}^l \sum_{j=1}^m \sum_{k=1}^n f(x_{ijk}^*, y_{ijk}^*, z_{ijk}^*) \Delta V}$$

- **Spatial Volume:** When $f(x, y, z) \equiv 1$:
  $$\mathbf{V(E) = \iiint_E 1 \, dV}$$
- **Total Mass:** If $\rho(x, y, z)$ represents density:
  $$\mathbf{M = \iiint_E \rho(x, y, z) \, dV}$$

---

### 2. Iterated Triple Integrals and Fubini's Permutations

A solid region $E$ is of **Type 1** if it lies between the continuous boundary surfaces $z = u_1(x, y)$ and $z = u_2(x, y)$ over a planar projection domain $D$ in the $xy$-plane:

$$\iiint_E f(x, y, z) \, dV = \iint_D \left( \int_{u_1(x, y)}^{u_2(x, y)} f(x, y, z) \, dz \right) dA$$

Depending on which coordinate is integrated first and which planar projection is chosen, there are **six possible orders of integration**:

$$dz \, dy \, dx, \quad dz \, dx \, dy, \quad dy \, dz \, dx, \quad dy \, dx \, dz, \quad dx \, dz \, dy, \quad dx \, dy \, dz$$

Choosing the appropriate order of integration can simplify the algebraic limits substantially and avoid splitting the domain into multiple subregions."""
            },
            {
                "id": "u6-sec2",
                "title": "Triple Integrals in Cylindrical & Spherical Coordinates",
                "content": r"""### 1. Cylindrical Coordinates

In **cylindrical coordinates**, a point $P(x, y, z)$ is represented by $(r, \theta, z)$ where:

$$x = r\cos\theta, \qquad y = r\sin\theta, \qquad z = z$$

The volume element is obtained by multiplying the polar area element by the height $dz$:

$$\mathbf{dV = r \, dr \, d\theta \, dz}$$

#### Transformation Formula:
$$\iiint_E f(x, y, z) \, dV = \int_\alpha^\beta \int_{h_1(\theta)}^{h_2(\theta)} \int_{u_1(r, \theta)}^{u_2(r, \theta)} f(r\cos\theta, r\sin\theta, z) \; r \, dz \, dr \, d\theta$$

> **When to use Cylindrical Coordinates:**  
> When the solid or integrand possesses rotational symmetry around the $z$-axis (cylinders $x^2 + y^2 \le a^2$, circular cones $z^2 = x^2 + y^2$, or paraboloids $z = x^2 + y^2$).

---

### 2. Spherical Polar Coordinates

In **spherical coordinates**, a point is represented by $(\rho, \theta, \phi)$ where:
- $\rho \ge 0$ is the distance from the origin.
- $\theta \in [0, 2\pi)$ is the azimuthal angle in the $xy$-plane.
- $\phi \in [0, \pi]$ is the colatitude/polar angle measured down from the positive $z$-axis.

The Cartesian coordinates are given by:

$$\mathbf{x = \rho \sin\phi \cos\theta, \qquad y = \rho \sin\phi \sin\theta, \qquad z = \rho \cos\phi}$$
$$x^2 + y^2 + z^2 = \rho^2$$

#### The Spherical Volume Element:
Consider a spherical wedge bounded by $\Delta\rho, \Delta\phi, \Delta\theta$.  
The edges of the wedge are:
1. Radial edge: $\Delta\rho$
2. Arc length along meridian: $\rho \Delta\phi$
3. Arc length along parallel of latitude: $(\rho \sin\phi) \Delta\theta$

Multiplying these three mutually orthogonal infinitesimal edges yields:

$$\mathbf{dV = \rho^2 \sin\phi \, d\rho \, d\phi \, d\theta}$$

#### Transformation Formula:
$$\iiint_E f(x, y, z) \, dV = \int_c^d \int_\alpha^\beta \int_a^b f(\rho\sin\phi\cos\theta, \rho\sin\phi\sin\theta, \rho\cos\phi) \; \rho^2 \sin\phi \, d\rho \, d\phi \, d\theta$$

> **When to use Spherical Coordinates:**  
> When the region involves spheres ($\rho = a$), cones ($\phi = \alpha$), or integrands involving $x^2 + y^2 + z^2 = \rho^2$."""
            },
            {
                "id": "u6-sec3",
                "title": "General Change of Variables & The Jacobian Determinant",
                "content": r"""### 1. General Curvilinear Coordinate Transformations

Let $T: S \to R$ be a smooth, invertible transformation mapping a region $S$ in the $uv$-plane onto a region $R$ in the $xy$-plane:

$$x = g(u, v), \qquad y = h(u, v)$$

Carl Gustav Jacobi (1841) discovered that the local area expansion factor under $T$ is given by the determinant of the transformation matrix.

**Definition (The Jacobian in 2D):**  
The **Jacobian** of $x$ and $y$ with respect to $u$ and $v$ is:

$$\mathbf{J(u, v) = \frac{\partial(x, y)}{\partial(u, v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix} = \frac{\partial x}{\partial u}\frac{\partial y}{\partial v} - \frac{\partial x}{\partial v}\frac{\partial y}{\partial u}}$$

#### Change of Variables Theorem in 2D:
$$\mathbf{\iint_R f(x, y) \, dA = \iint_S f(g(u, v), h(u, v)) \left| \frac{\partial(x, y)}{\partial(u, v)} \right| \, du \, dv}$$

---

### 2. The 3D Jacobian and Space Transformations

For a transformation from $uvw$-space to $xyz$-space: $x = g(u, v, w), y = h(u, v, w), z = k(u, v, w)$:

$$\mathbf{\frac{\partial(x, y, z)}{\partial(u, v, w)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w} \\ \frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w} \end{vmatrix}}$$

#### Change of Variables in 3D:
$$\mathbf{\iiint_R f(x, y, z) \, dV = \iiint_S f(x(u,v,w), y(u,v,w), z(u,v,w)) \left| \frac{\partial(x, y, z)}{\partial(u, v, w)} \right| \, du \, dv \, dw}$$

#### Verification for Spherical Coordinates:
$$\frac{\partial(x, y, z)}{\partial(\rho, \phi, \theta)} = \begin{vmatrix} \sin\phi\cos\theta & \rho\cos\phi\cos\theta & -\rho\sin\phi\sin\theta \\ \sin\phi\sin\theta & \rho\cos\phi\sin\theta & \rho\sin\phi\cos\theta \\ \cos\phi & -\rho\sin\phi & 0 \end{vmatrix} = \rho^2 \sin\phi \quad \blacksquare$$"""
            }
        ],
        "simulations": [
            {
                "id": "sim_calc3_triple_integrals",
                "title": "3D Triple Integral Coordinate Slicer Engine",
                "description": "Slice 3D volumes in Cartesian, Cylindrical, and Spherical polar shells. Observe the differential volume element dV and real-time numerical volume summation.",
                "controls": [
                    {"param": "coordSystem", "label": "Frame (0:Cart, 1:Cyl, 2:Sphere)", "min": 0, "max": 2, "step": 1, "default": 2},
                    {"param": "cutSlice", "label": "Cut-Plane / Radius", "min": 0.5, "max": 3.0, "step": 0.1, "default": 2.0},
                    {"param": "coneAngle", "label": "Cone Angle / Height", "min": 15, "max": 80, "step": 5, "default": 45},
                    {"param": "rotY", "label": "Orbit Yaw (°)", "min": -180, "max": 180, "step": 2, "default": 35}
                ]
            }
        ],
        "problems": [
            {
                "id": "prob-calc3-6-1",
                "tier": 1,
                "title": "Volume of a Bounded Tetrahedron via Iterated Triple Integral",
                "statement": r"""Find the volume of the solid tetrahedron $E$ bounded by the coordinate planes $x = 0, y = 0, z = 0$ and the plane:
$$x + 2y + 3z = 6$$""",
                "solution": r"""**Step 1: Determine the Bounds of the Solid**  
From $x + 2y + 3z = 6$:
- Upper boundary for $z$: $z = \frac{6 - x - 2y}{3}$
- Lower boundary for $z$: $z = 0$

Setting $z = 0$ gives the projection region $D$ in the $xy$-plane:
$$x + 2y = 6 \implies y = \frac{6 - x}{2}$$
In the first quadrant ($x \ge 0, y \ge 0$):
- $x$ varies from $0$ to $6$
- For a fixed $x$, $y$ varies from $0$ to $\frac{6 - x}{2}$

Thus:
$$E = \left\{ (x, y, z) : 0 \le x \le 6, \; 0 \le y \le \frac{6 - x}{2}, \; 0 \le z \le \frac{6 - x - 2y}{3} \right\}$$

---

**Step 2: Set up the Iterated Triple Integral**  
$$V = \int_0^6 \int_0^{(6-x)/2} \int_0^{(6-x-2y)/3} 1 \, dz \, dy \, dx$$

---

**Step 3: Evaluate the Inner Integral ($z$)**  
$$\int_0^{(6-x-2y)/3} dz = \frac{6 - x - 2y}{3}$$

---

**Step 4: Evaluate the Middle Integral ($y$)**  
$$\int_0^{(6-x)/2} \frac{6 - x - 2y}{3} \, dy = \frac{1}{3} \left[ (6 - x)y - y^2 \right]_{y=0}^{y=(6-x)/2}$$
$$= \frac{1}{3} \left[ (6 - x)\frac{6 - x}{2} - \left(\frac{6 - x}{2}\right)^2 \right] = \frac{1}{3} \left[ \frac{(6 - x)^2}{2} - \frac{(6 - x)^2}{4} \right] = \frac{1}{3} \frac{(6 - x)^2}{4} = \frac{(6 - x)^2}{12}$$

---

**Step 5: Evaluate the Outer Integral ($x$)**  
$$V = \int_0^6 \frac{(6 - x)^2}{12} \, dx$$
Let $u = 6 - x \implies du = -dx$:
$$V = \frac{1}{12} \left[ -\frac{(6 - x)^3}{3} \right]_0^6 = \frac{1}{36} [ 0 - (-6^3) ] = \frac{216}{36} = \mathbf{6} \text{ cubic units}$$

*(Check via geometry: $V = \frac{1}{6} a b c = \frac{1}{6}(6)(3)(2) = 6$. $\checkmark$)*"""
            },
            {
                "id": "prob-calc3-6-2",
                "tier": 2,
                "title": "Volume of an Ice-Cream Cone Solid in Spherical Coordinates",
                "statement": r"""Find the volume of the solid $E$ that lies within the sphere $x^2 + y^2 + z^2 \le a^2$ and inside the upper cone $z \ge \sqrt{x^2 + y^2}$ ($a > 0$).""",
                "solution": r"""**Step 1: Translate the Boundaries into Spherical Coordinates**  
1. **Sphere:**
   $$x^2 + y^2 + z^2 = a^2 \implies \rho^2 = a^2 \implies \rho = a$$
   Thus, $0 \le \rho \le a$.

2. **Cone:**
   In spherical coordinates:
   $$z = \rho\cos\phi, \qquad \sqrt{x^2 + y^2} = \rho\sin\phi$$
   The cone equation becomes:
   $$\rho\cos\phi = \rho\sin\phi \implies \tan\phi = 1 \implies \phi = \frac{\pi}{4}$$
   The solid lies inside the cone, so $0 \le \phi \le \frac{\pi}{4}$.

3. **Azimuthal Angle:**
   The solid has complete rotational symmetry around the $z$-axis:
   $$0 \le \theta \le 2\pi$$

---

**Step 2: Set up the Spherical Triple Integral**  
Recall $dV = \rho^2 \sin\phi \, d\rho \, d\phi \, d\theta$:
$$V = \int_0^{2\pi} \int_0^{\pi/4} \int_0^a \rho^2 \sin\phi \, d\rho \, d\phi \, d\theta$$

---

**Step 3: Evaluate the Factored Iterated Integrals**  
Because the limits of integration are all constants and the integrand factors completely:
$$V = \left( \int_0^{2\pi} d\theta \right) \left( \int_0^{\pi/4} \sin\phi \, d\phi \right) \left( \int_0^a \rho^2 \, d\rho \right)$$

Evaluate each single integral:
1. $\int_0^{2\pi} d\theta = 2\pi$
2. $\int_0^{\pi/4} \sin\phi \, d\phi = [-\cos\phi]_0^{\pi/4} = -\frac{\sqrt{2}}{2} - (-1) = 1 - \frac{\sqrt{2}}{2}$
3. $\int_0^a \rho^2 \, d\rho = \frac{a^3}{3}$

Multiply:
$$V = 2\pi \left( 1 - \frac{\sqrt{2}}{2} \right) \left( \frac{a^3}{3} \right) = \mathbf{\frac{2\pi a^3}{3} \left( 1 - \frac{\sqrt{2}}{2} \right)} = \frac{\pi a^3}{3}(2 - \sqrt{2}) \approx 0.6134 a^3$$"""
            },
            {
                "id": "prob-calc3-6-3",
                "tier": 3,
                "title": "Volume of the Steinmetz Solid (Intersection of Two Cylinders)",
                "statement": r"""Find the exact volume of the Steinmetz solid formed by the intersection of two solid circular cylinders of equal radius $a$ whose central axes intersect at right angles:
$$x^2 + y^2 \le a^2 \quad \text{and} \quad x^2 + z^2 \le a^2$$""",
                "solution": r"""**Step 1: Exploit Octant Symmetry**  
The solid is invariant under reflections across all three coordinate planes ($x \to -x$, $y \to -y$, $z \to -z$).  
Therefore, the total volume is 8 times the volume in the first octant ($x \ge 0, y \ge 0, z \ge 0$):
$$V = 8 V_{octant}$$

---

**Step 2: Determine First-Octant Limits**  
From the cylinder equations:
- Cylinder 1: $y^2 \le a^2 - x^2 \implies 0 \le y \le \sqrt{a^2 - x^2}$
- Cylinder 2: $z^2 \le a^2 - x^2 \implies 0 \le z \le \sqrt{a^2 - x^2}$
- For both square roots to be real: $0 \le x \le a$

Notice that for any fixed $x \in [0, a]$, the cross-section perpendicular to the $x$-axis is a **square** of side length $\sqrt{a^2 - x^2}$!

---

**Step 3: Set up the Triple Integral**  
$$V_{octant} = \int_0^a \int_0^{\sqrt{a^2 - x^2}} \int_0^{\sqrt{a^2 - x^2}} 1 \, dz \, dy \, dx$$

Evaluate the inner $z$-integral:
$$\int_0^{\sqrt{a^2 - x^2}} dz = \sqrt{a^2 - x^2}$$

Evaluate the middle $y$-integral:
$$\int_0^{\sqrt{a^2 - x^2}} \sqrt{a^2 - x^2} \, dy = (\sqrt{a^2 - x^2}) \cdot (\sqrt{a^2 - x^2}) = a^2 - x^2$$

---

**Step 4: Evaluate the Outer $x$-Integral**  
$$V_{octant} = \int_0^a (a^2 - x^2) \, dx = \left[ a^2 x - \frac{x^3}{3} \right]_0^a = a^3 - \frac{a^3}{3} = \frac{2}{3}a^3$$

---

**Step 5: Compute Total Volume**  
$$V = 8 V_{octant} = 8 \left( \frac{2}{3}a^3 \right) = \mathbf{\frac{16}{3}a^3}$$

This elegant Archimedean result proves that the volume of the intersection of two orthogonal cylinders is $\frac{16}{3}a^3 \approx 5.333 a^3$ cubic units. $\blacksquare$"""
            }
        ]
    }

if __name__ == "__main__":
    print("Building Calculus III: Units 5 & 6...")
    u5 = build_unit_5()
    with open("calc3_u5.json", "w", encoding="utf-8") as f:
        json.dump(u5, f, indent=2, ensure_ascii=False)
    print("Saved calc3_u5.json successfully.")

    u6 = build_unit_6()
    with open("calc3_u6.json", "w", encoding="utf-8") as f:
        json.dump(u6, f, indent=2, ensure_ascii=False)
    print("Saved calc3_u6.json successfully.")
