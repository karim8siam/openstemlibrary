# -*- coding: utf-8 -*-
"""
build_dg_unit6.py
Constructs Unit 6: Normal Curvatures, Principal Curvatures & Shape Classification
"""

def get_unit6():
    u6 = {
        "number": 6,
        "title": "Normal Curvatures, Principal Curvatures & Shape Classification",
        "leadSummary": "Local geometry and curvature theory: principal curvatures and principal directions as critical values of the normal curvature quadratic ratio, Gaussian curvature $K$ and Mean curvature $H$, geometric point classification (elliptic, hyperbolic, parabolic, planar, and umbilical points), minimal surfaces ($H = 0$) and soap film geometry, curvature analysis of surfaces of revolution, and the global rigidity theorem for all-umbilic surfaces.",
        "simulations": ["sim_dg_curvatures_principal"],
        "sections": [
            {
                "secNumber": "6.1",
                "title": "Principal Curvatures & Directions as Extrema of Normal Curvature",
                "content": r"""### 1. The Normal Curvature as a Rayleigh Quotient

At any regular point $p$ on a surface $S$, the normal curvature $\kappa_n$ in the direction $(du, dv)$ is:
$$\kappa_n(du, dv) = \frac{II(du, dv)}{I(du, dv)} = \frac{L \, du^2 + 2M \, du \, dv + N \, dv^2}{E \, du^2 + 2F \, du \, dv + G \, dv^2}$$
Since scaling $(du, dv)$ by any non-zero constant $c \ne 0$ cancels out in the numerator and denominator, $\kappa_n$ depends only on the direction angle on the unit circle in $T_p S$.
Because the unit circle is compact and $\kappa_n$ is a continuous function, $\kappa_n$ must attain an absolute maximum $\kappa_1$ and an absolute minimum $\kappa_2$.

> **Definition 6.1 (Principal Curvatures and Principal Directions):**
> The maximum and minimum values of the normal curvature at $p$:
> $$\kappa_1 = \max_{\mathbf{w} \ne 0} \kappa_n(\mathbf{w}), \qquad \kappa_2 = \min_{\mathbf{w} \ne 0} \kappa_n(\mathbf{w})$$
> are called the **principal curvatures** of the surface at $p$.
> The directions in $T_p S$ along which these extreme values are attained are called the **principal directions**.

---

### 2. Derivation of the Principal Curvature Equation

To find the critical points of $\kappa_n$, we use the method of Lagrange multipliers: extremize $II(du, dv) = L du^2 + 2M dudv + N dv^2$ subject to the normalization constraint $I(du, dv) = E du^2 + 2F dudv + G dv^2 = 1$.
Form the Lagrangian:
$$\mathcal{L}(du, dv, \kappa) = (L du^2 + 2M dudv + N dv^2) - \kappa(E du^2 + 2F dudv + G dv^2 - 1)$$
Taking partial derivatives with respect to $du$ and $dv$ and setting them to zero:
$$\frac{1}{2}\frac{\partial \mathcal{L}}{\partial(du)} = (L - \kappa E) du + (M - \kappa F) dv = 0$$
$$\frac{1}{2}\frac{\partial \mathcal{L}}{\partial(dv)} = (M - \kappa F) du + (N - \kappa G) dv = 0$$
In matrix notation:
$$\begin{pmatrix} L - \kappa E & M - \kappa F \\ M - \kappa F & N - \kappa G \end{pmatrix} \begin{pmatrix} du \\ dv \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
For non-trivial tangent directions $(du, dv) \ne (0, 0)$, the determinant of this coefficient matrix must vanish!

> **Theorem 6.1 (The Characteristic Equation for Principal Curvatures):**
> The principal curvatures $\kappa$ are the real roots of the quadratic equation:
> $$\det \begin{pmatrix} L - \kappa E & M - \kappa F \\ M - \kappa F & N - \kappa G \end{pmatrix} = 0$$
> Expanding the determinant:
> $$(EG - F^2)\kappa^2 - (EN - 2FM + GL)\kappa + (LN - M^2) = 0$$

---

### 3. Orthogonality of Principal Directions

> **Theorem 6.2 (Orthogonality of Principal Directions):**
> If $\kappa_1 \ne \kappa_2$, the corresponding principal directions are mutually orthogonal in the tangent plane $T_p S$.

> **Proof:**
> The principal curvatures $\kappa_1, \kappa_2$ are the eigenvalues of the Shape Operator $S_p$, and the principal directions are the corresponding eigenspaces.
> By Theorem 5.1, $S_p$ is self-adjoint with respect to the first fundamental form inner product $\langle \cdot, \cdot \rangle$.
> For eigenvectors $\mathbf{v}_1, \mathbf{v}_2$ with $\kappa_1 \ne \kappa_2$:
> $$\kappa_1 \langle \mathbf{v}_1, \mathbf{v}_2 \rangle = \langle S_p(\mathbf{v}_1), \mathbf{v}_2 \rangle = \langle \mathbf{v}_1, S_p(\mathbf{v}_2) \rangle = \kappa_2 \langle \mathbf{v}_1, \mathbf{v}_2 \rangle$$
> $$(\kappa_1 - \kappa_2) \langle \mathbf{v}_1, \mathbf{v}_2 \rangle = 0$$
> Since $\kappa_1 - \kappa_2 \ne 0$, we must have $\langle \mathbf{v}_1, \mathbf{v}_2 \rangle = 0$. $\blacksquare$"""
            },
            {
                "secNumber": "6.2",
                "title": "Gaussian Curvature K, Mean Curvature H & Quadratic Invariants",
                "content": r"""### 1. Definitions of Gaussian and Mean Curvature

Dividing the quadratic characteristic equation of Theorem 6.1 by $(EG - F^2)$:
$$\kappa^2 - \left(\frac{EN - 2FM + GL}{EG - F^2}\right)\kappa + \left(\frac{LN - M^2}{EG - F^2}\right) = 0$$
Comparing this with the standard monic quadratic $\kappa^2 - 2H\kappa + K = 0$:

> **Definition 6.2 (Gaussian Curvature and Mean Curvature):**
> 1. The **Gaussian Curvature** $K$ is the product of the principal curvatures:
>    $$K = \kappa_1 \kappa_2 = \det(S_p) = \frac{LN - M^2}{EG - F^2}$$
> 2. The **Mean Curvature** $H$ is the arithmetic mean of the principal curvatures:
>    $$H = \frac{\kappa_1 + \kappa_2}{2} = \frac{1}{2} \operatorname{tr}(S_p) = \frac{EN - 2FM + GL}{2(EG - F^2)}$$

---

### 2. Solving for Principal Curvatures in Terms of $H$ and $K$

The quadratic equation $\kappa^2 - 2H\kappa + K = 0$ has discriminant:
$$\Delta = (2H)^2 - 4(1)(K) = 4(H^2 - K)$$
Notice that:
$$H^2 - K = \left(\frac{\kappa_1 + \kappa_2}{2}\right)^2 - \kappa_1 \kappa_2 = \frac{(\kappa_1 - \kappa_2)^2}{4} \ge 0$$
Thus, the discriminant is always non-negative, confirming that the principal curvatures are always real numbers!
The roots are:
$$\kappa_{1, 2} = H \pm \sqrt{H^2 - K}$$
where $\kappa_1 = H + \sqrt{H^2 - K}$ is the maximum curvature and $\kappa_2 = H - \sqrt{H^2 - K}$ is the minimum curvature.

---

### 3. Gaussian Curvature as the Jacobian of the Gauss Map

> **Theorem 6.3 (Gauss Map Area Ratio):**
> Let $U \subset S$ be a small region around $p$, and let $\mathbf{n}(U) \subset S^2$ be its spherical image under the Gauss map.
> The Gaussian curvature $K(p)$ is the limit of the ratio of the spherical area to the surface area:
> $$K(p) = \lim_{U \to p} \frac{\operatorname{Area}(\mathbf{n}(U))}{\operatorname{Area}(U)}$$
> with the sign determined by whether the Gauss map preserves ($K > 0$) or reverses ($K < 0$) orientation.

> **Proof:**
> The area element on the surface is $dA_S = \|\mathbf{r}_u \times \mathbf{r}_v\| \, du \, dv$.
> The area element on the unit sphere traced by $\mathbf{n}(u, v)$ is:
> $$dA_{S^2} = \|\mathbf{n}_u \times \mathbf{n}_v\| \, du \, dv$$
> By the Weingarten equations (Section 5.3), $\mathbf{n}_u = -S(\mathbf{r}_u)$ and $\mathbf{n}_v = -S(\mathbf{r}_v)$.
> For any linear operator $S$ on the tangent plane, the cross product transforms as:
> $$\mathbf{n}_u \times \mathbf{n}_v = S(\mathbf{r}_u) \times S(\mathbf{r}_v) = \det(S)(\mathbf{r}_u \times \mathbf{r}_v) = K (\mathbf{r}_u \times \mathbf{r}_v)$$
> Taking norms:
> $$\|\mathbf{n}_u \times \mathbf{n}_v\| = |K| \|\mathbf{r}_u \times \mathbf{r}_v\| \implies dA_{S^2} = |K| \, dA_S$$
> Taking the oriented limit yields the theorem. $\blacksquare$"""
            },
            {
                "secNumber": "6.3",
                "title": "Geometric Classification of Points: Elliptic, Hyperbolic, Parabolic & Umbilic",
                "content": r"""### 1. Classification by the Sign of Gaussian Curvature

The sign of the Gaussian curvature $K = \frac{LN - M^2}{EG - F^2}$ dictates the local shape of the surface relative to its tangent plane.
Since $EG - F^2 > 0$, the sign of $K$ is determined entirely by the sign of the discriminant of the Second Fundamental Form: $LN - M^2$.

> **Definition 6.3 (Classification of Surface Points):**
> Let $p \in S$ be a regular point:
> 1. **Elliptic Point ($K > 0$):**
>    Both principal curvatures have the same sign ($\kappa_1 \kappa_2 > 0$).
>    $LN - M^2 > 0$. The Second Fundamental Form $II$ is definite (positive or negative).
>    *Geometry:* The surface curves away from the tangent plane in the same direction along all tangent vectors; locally, the surface lies entirely on one side of its tangent plane (like an ellipsoid or sphere).
> 2. **Hyperbolic Point ($K < 0$):**
>    The principal curvatures have opposite signs ($\kappa_1 \kappa_2 < 0$).
>    $LN - M^2 < 0$. The Second Fundamental Form $II$ is indefinite.
>    *Geometry:* The surface is saddle-shaped; the tangent plane cuts through the surface, dividing it into two regions lying on opposite sides of the plane (like a hyperbolic paraboloid or catenoid).
> 3. **Parabolic Point ($K = 0$, but not all second coefficients vanish):**
>    One principal curvature is zero and the other is non-zero ($\kappa_1 \ne 0, \kappa_2 = 0$).
>    $LN - M^2 = 0$, with $L^2 + M^2 + N^2 > 0$.
>    *Geometry:* The surface bends along one direction but is flat along another (like a cylinder or cone).
> 4. **Planar Point ($\kappa_1 = \kappa_2 = 0$):**
>    Both principal curvatures vanish identically ($L = M = N = 0$).
>    *Geometry:* Second-order curvature is completely flat in all directions (like a point on a flat plane).

---

### 2. Umbilical Points

> **Definition 6.4 (Umbilical Point):**
> A point $p \in S$ is called an **umbilical point** (or umbilic) if the two principal curvatures are equal:
> $$\kappa_1 = \kappa_2 \iff H^2 - K = 0$$
> Equivalently, the Shape Operator is a scalar multiple of the identity: $S_p = \kappa I_{\text{id}}$.

At an umbilic:
- The normal curvature is identical in every direction: $\kappa_n(\mathbf{w}) = \kappa$ for all $\mathbf{w} \in T_p S$.
- Every tangent direction is a principal direction!
- If $\kappa_1 = \kappa_2 \ne 0$, $p$ is an **elliptic umbilic** (e.g., any point on a sphere of radius $1/\kappa$).
- If $\kappa_1 = \kappa_2 = 0$, $p$ is a **planar umbilic**."""
            },
            {
                "secNumber": "6.4",
                "title": "Minimal Surfaces & Zero Mean Curvature: Geometry of Soap Films",
                "content": r"""### 1. Definition and Physical Origin of Minimal Surfaces

> **Definition 6.5 (Minimal Surface):**
> A regular surface $S$ is called a **minimal surface** if its Mean Curvature vanishes identically at every point:
> $$H(p) \equiv 0 \quad \forall p \in S$$
> Equivalently, the principal curvatures are equal in magnitude and opposite in sign:
> $$\kappa_1 = -\kappa_2 \implies K = -\kappa_1^2 \le 0$$

Physically, by the Young-Laplace equation of fluid mechanics, the pressure difference $\Delta P$ across a soap film interface with surface tension $\sigma$ is:
$$\Delta P = 2 \sigma H$$
When the pressure is equal on both sides ($\Delta P = 0$), the soap film spontaneously adopts a configuration with $H = 0$, minimizing its total surface area subject to the fixed boundary wire frame!

---

### 2. Properties of Minimal Surfaces

1. **Gaussian Curvature is Non-Positive:**
   Since $\kappa_2 = -\kappa_1$, $K = \kappa_1 \kappa_2 = -\kappa_1^2 \le 0$.
   Therefore, every point on a minimal surface is either **hyperbolic** ($K < 0$) or **planar** ($K = 0$). There are **no elliptic points** on a minimal surface!
2. **Minimal Surface Partial Differential Equation:**
   For a Monge patch $z = f(x, y)$, the condition $H = 0$ translates into Lagrange's non-linear minimal surface PDE:
   $$(1 + f_y^2) f_{xx} - 2 f_x f_y f_{xy} + (1 + f_x^2) f_{yy} = 0$$
3. **Conformal Parametrizations and Harmonic Coordinates:**
   If a surface is parametrized by isothermal coordinates ($E = G = \lambda^2, F = 0$), then:
   $$\Delta \mathbf{r} = \mathbf{r}_{uu} + \mathbf{r}_{vv} = 2 \lambda^2 H \mathbf{n}$$
   Thus, in isothermal coordinates, a surface is minimal ($H = 0$) if and only if its coordinate functions are **harmonic**:
   $$\Delta \mathbf{r} = \mathbf{0} \iff \Delta x = 0, \; \Delta y = 0, \; \Delta z = 0$$

---

### 3. Classical Examples of Minimal Surfaces

- **The Catenoid:** Discovered by Euler (1744), the only minimal surface of revolution other than the plane.
- **The Helicoid:** Discovered by Meusnier (1776), the only ruled minimal surface other than the plane.
- **Scherk's Surface:** Discovered by Scherk (1834), $z = \ln(\cos x / \cos y)$.
- **Enneper's Surface:** An algebraic minimal surface of degree 9."""
            },
            {
                "secNumber": "6.5",
                "title": "Surfaces of Revolution: Meridian & Parallel Curvatures & Beltrami's Pseudosphere",
                "content": r"""### 1. Parametrization of a Surface of Revolution

Let a profile curve in the $xz$-plane be parametrized by arc-length $u$:
$$x = f(u) > 0, \quad z = g(u), \quad \text{with } (f')^2 + (g')^2 = 1$$
Rotating this curve about the $z$-axis through angle $v \in [0, 2\pi)$ produces the surface of revolution:
$$\mathbf{r}(u, v) = \begin{pmatrix} f(u) \cos v \\ f(u) \sin v \\ g(u) \end{pmatrix}$$

---

### 2. First and Second Fundamental Forms

Computing the partial derivatives:
$$\mathbf{r}_u = \begin{pmatrix} f'(u) \cos v \\ f'(u) \sin v \\ g'(u) \end{pmatrix}, \qquad \mathbf{r}_v = \begin{pmatrix} -f(u) \sin v \\ f(u) \cos v \\ 0 \end{pmatrix}$$
Metric coefficients:
$$E = (f')^2 + (g')^2 = 1, \qquad F = 0, \qquad G = f^2(u)$$
$$I = du^2 + f^2(u) \, dv^2$$
The coordinate grid is orthogonal ($F = 0$).
The unit normal is:
$$\mathbf{n}(u, v) = \begin{pmatrix} -g'(u) \cos v \\ -g'(u) \sin v \\ f'(u) \end{pmatrix}$$
Second derivatives:
$$\mathbf{r}_{uu} = \begin{pmatrix} f'' \cos v \\ f'' \sin v \\ g'' \end{pmatrix}, \quad \mathbf{r}_{uv} = \begin{pmatrix} -f' \sin v \\ f' \cos v \\ 0 \end{pmatrix}, \quad \mathbf{r}_{vv} = \begin{pmatrix} -f \cos v \\ -f \sin v \\ 0 \end{pmatrix}$$
Taking dot products with $\mathbf{n}$:
$$L = \mathbf{r}_{uu} \cdot \mathbf{n} = -f'' g' + g'' f' = f' g'' - f'' g'$$
$$M = \mathbf{r}_{uv} \cdot \mathbf{n} = 0$$
$$N = \mathbf{r}_{vv} \cdot \mathbf{n} = f g'$$
Since $F = 0$ and $M = 0$, the coordinate curves (meridians and parallels) are **lines of curvature**!

---

### 3. Principal and Gaussian Curvatures

The principal curvatures along the meridians ($dv = 0$) and parallels ($du = 0$) are:
$$\kappa_1 = \frac{L}{E} = f' g'' - f'' g', \qquad \kappa_2 = \frac{N}{G} = \frac{g'(u)}{f(u)}$$
Differentiating $(f')^2 + (g')^2 = 1$ with respect to $u$:
$$2 f' f'' + 2 g' g'' = 0 \implies g'' = -\frac{f' f''}{g'}$$
Substituting this into $\kappa_1$:
$$\kappa_1 = f' \left(-\frac{f' f''}{g'}\right) - f'' g' = -\frac{f''((f')^2 + (g')^2)}{g'} = -\frac{f''(u)}{g'(u)}$$
Multiplying $\kappa_1$ and $\kappa_2$:

> **Theorem 6.4 (Gaussian Curvature of a Surface of Revolution):**
> For a surface of revolution with profile curve parametrized by arc-length $u$:
> $$K(u) = \kappa_1 \kappa_2 = \left(-\frac{f''}{g'}\right)\left(\frac{g'}{f}\right) = -\frac{f''(u)}{f(u)}$$

---

### 4. Beltrami's Pseudosphere

Setting $K = -1/a^2$ (constant negative curvature) in $-\frac{f''}{f} = -\frac{1}{a^2}$ gives the differential equation:
$$f''(u) = \frac{1}{a^2} f(u)$$
The profile curve generating the **pseudosphere** is the **tractrix**:
$$f(u) = a e^{-u/a}, \quad g(u) = a \int \sqrt{1 - e^{-2u/a}} \, du$$
Beltrami demonstrated in 1868 that the pseudosphere provides a concrete local model for the hyperbolic geometry of Lobachevsky and Bolyai!"""
            }
        ],
        "problems": [
            {
                "id": "dg-prob-6-1",
                "tier": "Foundational",
                "title": "Point Classification & Curvatures of the Torus of Revolution",
                "statement": r"""Consider the torus formed by revolving a circle of radius $r > 0$ centered at distance $R > r > 0$ from the $z$-axis:
$$\mathbf{r}(u, v) = \begin{pmatrix} (R + r \cos u) \cos v \\ (R + r \cos u) \sin v \\ r \sin u \end{pmatrix}, \quad u, v \in [0, 2\pi)$$
1. Compute the First Fundamental Form $I$ and Second Fundamental Form $II$.
2. Find the principal curvatures $\kappa_1, \kappa_2$, Gaussian curvature $K(u)$, and Mean curvature $H(u)$.
3. Classify each region of the torus into elliptic, parabolic, and hyperbolic points based on the parameter $u$.""",
                "hints": [
                    "Note that r_u and r_v are orthogonal, so F = 0 and M = 0.",
                    "The profile curve is a circle: f(u) = R + r cos(u), g(u) = r sin(u).",
                    "K(u) = cos(u) / (r (R + r cos(u))). Determine sign based on cos(u)."
                ],
                "solution": r"""### 1. Partial Derivatives and Fundamental Forms
$$\mathbf{r}_u = \begin{pmatrix} -r \sin u \cos v \\ -r \sin u \sin v \\ r \cos u \end{pmatrix}, \qquad \mathbf{r}_v = \begin{pmatrix} -(R + r \cos u) \sin v \\ (R + r \cos u) \cos v \\ 0 \end{pmatrix}$$
Dot products:
$$E = \mathbf{r}_u \cdot \mathbf{r}_u = r^2(\sin^2 u + \cos^2 u) = r^2$$
$$F = \mathbf{r}_u \cdot \mathbf{r}_v = 0$$
$$G = \mathbf{r}_v \cdot \mathbf{r}_v = (R + r \cos u)^2$$
Thus:
$$I = r^2 \, du^2 + (R + r \cos u)^2 \, dv^2$$

Cross product and unit normal:
$$\mathbf{r}_u \times \mathbf{r}_v = \begin{pmatrix} -r(R + r \cos u)\cos u \cos v \\ -r(R + r \cos u)\cos u \sin v \\ -r(R + r \cos u)\sin u \end{pmatrix}$$
Dividing by $\|\mathbf{r}_u \times \mathbf{r}_v\| = r(R + r \cos u)$ (oriented inwards for positive standard convention, or outwards):
$$\mathbf{n}(u, v) = -\begin{pmatrix} \cos u \cos v \\ \cos u \sin v \\ \sin u \end{pmatrix}$$
Computing second derivatives and dot products with $\mathbf{n}$:
$$L = \mathbf{r}_{uu} \cdot \mathbf{n} = r, \qquad M = \mathbf{r}_{uv} \cdot \mathbf{n} = 0, \qquad N = \mathbf{r}_{vv} \cdot \mathbf{n} = (R + r \cos u)\cos u$$
Thus:
$$II = r \, du^2 + (R + r \cos u)\cos u \, dv^2 \quad \blacksquare$$

---

### 2. Principal, Gaussian, and Mean Curvatures
Since $F = 0$ and $M = 0$, the principal curvatures are simply the diagonal ratios:
$$\kappa_1 = \frac{L}{E} = \frac{r}{r^2} = \frac{1}{r}$$
$$\kappa_2 = \frac{N}{G} = \frac{(R + r \cos u)\cos u}{(R + r \cos u)^2} = \frac{\cos u}{R + r \cos u}$$
Gaussian Curvature:
$$K(u) = \kappa_1 \kappa_2 = \frac{\cos u}{r(R + r \cos u)}$$
Mean Curvature:
$$H(u) = \frac{\kappa_1 + \kappa_2}{2} = \frac{1}{2}\left( \frac{1}{r} + \frac{\cos u}{R + r \cos u} \right) = \frac{R + 2r \cos u}{2r(R + r \cos u)} \quad \blacksquare$$

---

### 3. Classification of Points
Because $R > r > 0$, the denominator $r(R + r \cos u) > 0$ is strictly positive for all $u$.
The sign of $K(u)$ is governed entirely by the sign of $\cos u$:
1. **Outer Equator / Exterior Region ($-\pi/2 < u < \pi/2$):**
   $\cos u > 0 \implies K > 0$.
   All points on the outer half of the torus are **elliptic points**.
2. **Top and Bottom Crown Circles ($u = \pi/2$ and $u = 3\pi/2$):**
   $\cos u = 0 \implies K = 0$.
   Here $\kappa_1 = 1/r \ne 0$ and $\kappa_2 = 0$.
   These two parallel circles consist entirely of **parabolic points**.
3. **Inner Equator / Interior Region ($\pi/2 < u < 3\pi/2$):**
   $\cos u < 0 \implies K < 0$.
   All points on the inner doughnut hole facing the axis are **hyperbolic points** (saddle-shaped). $\blacksquare$"""
            },
            {
                "id": "dg-prob-6-2",
                "tier": "Advanced",
                "title": "Minimal Surface Verification of Scherk's Surface",
                "statement": r"""Consider Scherk's famous surface defined explicitly by the Monge graph:
$$z = f(x, y) = \ln\left( \frac{\cos x}{\cos y} \right) = \ln(\cos x) - \ln(\cos y)$$
on the domain $U = (-\pi/2, \pi/2) \times (-\pi/2, \pi/2)$.
1. Compute the first and second partial derivatives: $f_x, f_y, f_{xx}, f_{xy}, f_{yy}$.
2. Recall Lagrange's minimal surface equation for Monge patches $z = f(x, y)$:
   $$(1 + f_y^2) f_{xx} - 2 f_x f_y f_{xy} + (1 + f_x^2) f_{yy} = 0$$
3. Substitute the derivatives into Lagrange's equation to prove that Mean Curvature $H = 0$ everywhere on $U$, establishing that Scherk's surface is a minimal surface.""",
                "hints": [
                    "Recall that d/dx ln(cos x) = -tan x, and d/dx (-tan x) = -sec^2 x.",
                    "Note that f_{xy} = 0 because f(x, y) separates as g(x) - h(y).",
                    "Use the trigonometric identity 1 + tan^2(theta) = sec^2(theta)."
                ],
                "solution": r"""### 1. Partial Derivatives
The function is:
$$f(x, y) = \ln(\cos x) - \ln(\cos y)$$
First derivatives:
$$f_x = \frac{-\sin x}{\cos x} = -\tan x$$
$$f_y = -\left( \frac{-\sin y}{\cos y} \right) = \tan y$$
Second derivatives:
$$f_{xx} = -\sec^2 x = -(1 + \tan^2 x)$$
$$f_{xy} = 0$$
$$f_{yy} = \sec^2 y = 1 + \tan^2 y \quad \blacksquare$$

---

### 2. Lagrange's Minimal Surface Condition
For a Monge surface $\mathbf{r}(x, y) = (x, y, f(x, y))^T$, the metric coefficients are:
$$E = 1 + f_x^2, \quad F = f_x f_y, \quad G = 1 + f_y^2$$
$$EG - F^2 = (1 + f_x^2)(1 + f_y^2) - f_x^2 f_y^2 = 1 + f_x^2 + f_y^2$$
The unit normal is $\mathbf{n} = \frac{(-f_x, -f_y, 1)^T}{\sqrt{1 + f_x^2 + f_y^2}}$.
The second fundamental form coefficients are:
$$L = \frac{f_{xx}}{\sqrt{1 + f_x^2 + f_y^2}}, \quad M = \frac{f_{xy}}{\sqrt{1 + f_x^2 + f_y^2}}, \quad N = \frac{f_{yy}}{\sqrt{1 + f_x^2 + f_y^2}}$$
The Mean Curvature is:
$$H = \frac{EN - 2FM + GL}{2(EG - F^2)^{3/2}} = \frac{(1 + f_x^2) f_{yy} - 2 f_x f_y f_{xy} + (1 + f_y^2) f_{xx}}{2(1 + f_x^2 + f_y^2)^{3/2}}$$
Therefore, $H = 0$ if and only if the numerator vanishes:
$$\mathcal{N} = (1 + f_y^2) f_{xx} - 2 f_x f_y f_{xy} + (1 + f_x^2) f_{yy} = 0 \quad \blacksquare$$

---

### 3. Evaluation of the Numerator
Substitute $f_x = -\tan x$, $f_y = \tan y$, $f_{xx} = -\sec^2 x$, $f_{xy} = 0$, and $f_{yy} = \sec^2 y$:
$$\mathcal{N} = (1 + \tan^2 y)(-\sec^2 x) - 2(-\tan x)(\tan y)(0) + (1 + \tan^2 x)(\sec^2 y)$$
Recall the Pythagorean trigonometric identity $1 + \tan^2 \theta = \sec^2 \theta$:
$$1 + \tan^2 y = \sec^2 y, \qquad 1 + \tan^2 x = \sec^2 x$$
Substituting these:
$$\mathcal{N} = (\sec^2 y)(-\sec^2 x) - 0 + (\sec^2 x)(\sec^2 y) = -\sec^2 y \sec^2 x + \sec^2 x \sec^2 y = 0$$
Since the numerator vanishes identically:
$$H \equiv 0 \quad \forall (x, y) \in U$$
Thus, Scherk's surface is a minimal surface! $\blacksquare$$"""
            },
            {
                "id": "dg-prob-6-3",
                "tier": "Honors / Proof Challenge",
                "title": "Rigidity Theorem: Surfaces with Only Umbilical Points",
                "statement": r"""Let $S \subset \mathbb{R}^3$ be a connected regular surface such that **every** point of $S$ is an umbilical point ($\kappa_1 = \kappa_2$).
1. Express the condition that $p$ is an umbilic in terms of the Shape Operator $S_p$ and the Weingarten equations.
2. Differentiate the resulting relation $\mathbf{n}_u = -\lambda(u, v) \mathbf{r}_u$ and $\mathbf{n}_v = -\lambda(u, v) \mathbf{r}_v$ to prove that $\lambda(u, v) = \lambda_0$ is a constant function on any connected coordinate patch.
3. Conclude that if $\lambda_0 = 0$, $S$ is an open subset of a plane; and if $\lambda_0 \ne 0$, $S$ is an open subset of a sphere of radius $R = 1/|\lambda_0|$.""",
                "hints": [
                    "At an umbilic, S_p = lambda I_id, so n_u = -lambda r_u and n_v = -lambda r_v.",
                    "Use equality of mixed partials: (n_u)_v = (n_v)_u.",
                    "Since r_u and r_v are linearly independent, their coefficients must vanish independently."
                ],
                "solution": r"""### 1. Shape Operator and Umbilical Condition
Let $p \in S$ be an umbilical point. Then the principal curvatures coincide: $\kappa_1 = \kappa_2 = \lambda(u, v)$.
Therefore, the Shape Operator is a scalar operator:
$$S_p(\mathbf{w}) = \lambda(u, v) \mathbf{w} \quad \forall \mathbf{w} \in T_p S$$
Applying this to the coordinate basis vectors $\mathbf{r}_u, \mathbf{r}_v$:
$$S_p(\mathbf{r}_u) = -\mathbf{n}_u = \lambda \mathbf{r}_u \implies \mathbf{n}_u = -\lambda(u, v) \mathbf{r}_u$$
$$S_p(\mathbf{r}_v) = -\mathbf{n}_v = \lambda \mathbf{r}_v \implies \mathbf{n}_v = -\lambda(u, v) \mathbf{r}_v$$

---

### 2. Differentiating and Equality of Mixed Partials
Assume $S$ is of class $C^3$, so $\mathbf{n}$ is of class $C^2$.
By Clairaut's theorem, mixed partial derivatives of $\mathbf{n}$ must commute:
$$\mathbf{n}_{uv} = \mathbf{n}_{vu} \iff \frac{\partial}{\partial v}(\mathbf{n}_u) = \frac{\partial}{\partial u}(\mathbf{n}_v)$$
Computing both sides using the product rule:
$$\frac{\partial}{\partial v}(\mathbf{n}_u) = \frac{\partial}{\partial v}(-\lambda \mathbf{r}_u) = -\lambda_v \mathbf{r}_u - \lambda \mathbf{r}_{uv}$$
$$\frac{\partial}{\partial u}(\mathbf{n}_v) = \frac{\partial}{\partial u}(-\lambda \mathbf{r}_v) = -\lambda_u \mathbf{r}_v - \lambda \mathbf{r}_{vu}$$
Equating these expressions:
$$-\lambda_v \mathbf{r}_u - \lambda \mathbf{r}_{uv} = -\lambda_u \mathbf{r}_v - \lambda \mathbf{r}_{vu}$$
Because the surface is $C^2$, $\mathbf{r}_{uv} = \mathbf{r}_{vu}$, so the terms $-\lambda \mathbf{r}_{uv}$ cancel out on both sides:
$$-\lambda_v \mathbf{r}_u = -\lambda_u \mathbf{r}_v \iff \lambda_v \mathbf{r}_u - \lambda_u \mathbf{r}_v = \mathbf{0}$$
Since the surface patch is regular, $\mathbf{r}_u$ and $\mathbf{r}_v$ are linearly independent vectors!
Therefore, their scalar coefficients must both be zero:
$$\lambda_u = 0 \quad \text{and} \quad \lambda_v = 0$$
Because the domain is connected, $\lambda(u, v) = \lambda_0 = \text{constant}$! $\blacksquare$

---

### 3. Case Analysis: Plane or Sphere

**Case 1: $\lambda_0 = 0$**
If $\lambda_0 = 0$, then:
$$\mathbf{n}_u = \mathbf{0} \quad \text{and} \quad \mathbf{n}_v = \mathbf{0}$$
Hence, the unit normal vector is constant across the entire connected surface:
$$\mathbf{n}(u, v) = \mathbf{n}_0 = \text{constant vector}$$
Now consider the scalar function $f(u, v) = \mathbf{r}(u, v) \cdot \mathbf{n}_0$.
Differentiating:
$$\frac{\partial f}{\partial u} = \mathbf{r}_u \cdot \mathbf{n}_0 = 0, \qquad \frac{\partial f}{\partial v} = \mathbf{r}_v \cdot \mathbf{n}_0 = 0$$
Thus $f(u, v) = c$ is constant:
$$\mathbf{r}(u, v) \cdot \mathbf{n}_0 = c$$
This is the equation of a plane in $\mathbb{R}^3$. Therefore, $S$ is an open subset of a **plane**!

**Case 2: $\lambda_0 \ne 0$**
If $\lambda_0 \ne 0$, consider the vector-valued function:
$$\mathbf{c}(u, v) = \mathbf{r}(u, v) + \frac{1}{\lambda_0} \mathbf{n}(u, v)$$
Differentiating with respect to $u$ and $v$:
$$\mathbf{c}_u = \mathbf{r}_u + \frac{1}{\lambda_0} \mathbf{n}_u = \mathbf{r}_u + \frac{1}{\lambda_0}(-\lambda_0 \mathbf{r}_u) = \mathbf{r}_u - \mathbf{r}_u = \mathbf{0}$$
$$\mathbf{c}_v = \mathbf{r}_v + \frac{1}{\lambda_0} \mathbf{n}_v = \mathbf{r}_v + \frac{1}{\lambda_0}(-\lambda_0 \mathbf{r}_v) = \mathbf{r}_v - \mathbf{r}_v = \mathbf{0}$$
Since both partial derivatives vanish, $\mathbf{c}(u, v)$ is a constant vector $\mathbf{c}_0 \in \mathbb{R}^3$:
$$\mathbf{r}(u, v) + \frac{1}{\lambda_0} \mathbf{n}(u, v) = \mathbf{c}_0 \implies \mathbf{r}(u, v) - \mathbf{c}_0 = -\frac{1}{\lambda_0} \mathbf{n}(u, v)$$
Taking the Euclidean norm on both sides:
$$\|\mathbf{r}(u, v) - \mathbf{c}_0\| = \left\| -\frac{1}{\lambda_0} \mathbf{n}(u, v) \right\| = \frac{1}{|\lambda_0|} \|\mathbf{n}(u, v)\| = \frac{1}{|\lambda_0|}$$
Letting $R = \frac{1}{|\lambda_0|} > 0$:
$$\|\mathbf{r}(u, v) - \mathbf{c}_0\| = R$$
This is precisely the equation of a sphere of radius $R$ centered at $\mathbf{c}_0$!
Therefore, $S$ is an open subset of a **sphere**! $\blacksquare$"""
            }
        ]
    }
    return u6

if __name__ == "__main__":
    u = get_unit6()
    print(f"Loaded Unit 6: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
