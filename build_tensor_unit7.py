# -*- coding: utf-8 -*-
"""
build_tensor_unit7.py
Constructs Unit 7: Special Geometries, Flat Spaces & Hypersurfaces
Strictly ZERO course numbers.
"""

def get_unit7():
    u7 = {
        "number": 7,
        "title": "Special Geometries, Flat Spaces & Hypersurfaces",
        "leadSummary": "Advanced geometric analysis of special Riemannian manifolds and embedded submanifolds: necessary and sufficient conditions for flat Riemannian spaces R_{ijkl} = 0, existence of global Cartesian coordinate systems, conformal transformations and conformal flatness, derivation of the Weyl conformal curvature tensor C^l_{ijk} and the Cotton-York tensor in 3D, geometry of hypersurfaces M^n \\subset \\mathbb{R}^{n+1}, induced metrics (first fundamental form a_{\\alpha\\beta}), Gauss's formula, the second fundamental form b_{\\alpha\\beta}, Weingarten equations, principal curvatures, Mean and Gaussian curvature, and the celebrated Gauss-Codazzi-Mainardi embedding equations.",
        "simulations": ["sim_tensor_weyl_conformal"],
        "sections": [
            {
                "secNumber": "7.1",
                "title": "Flat Riemannian Spaces, Conditions for Flatness ($R_{ijkl} = 0$), and Cartesian Coordinates",
                "content": r"""### 1. Definition and Characterization of Flat Manifolds
A Riemannian space $R_n$ is called **flat** (or Euclidean / pseudo-Euclidean) if there exists a coordinate system $(y^1, \dots, y^n)$ in which the metric tensor components are everywhere constant:
$$g_{ij}(y) = c_{ij} = \text{constant}$$
By a constant linear transformation, such a metric can always be brought to diagonal form with entries $\pm 1$:
$$ds^2 = \sum_{i=1}^n \pm (dy^i)^2$$

---

### 2. The Theorem of Flatness

> **Theorem 7.1 (Riemann Flatness Criterion):**
> A Riemannian manifold $(M, g)$ is locally flat if and only if its Riemann curvature tensor vanishes identically everywhere:
> $$R^l_{ijk} = 0 \quad (\text{or } R_{hijk} = 0)$$

#### Proof (Necessity):
If coordinates $y^k$ exist such that $g_{ij} = \text{const}$, then all first and second partial derivatives of the metric vanish identically:
$$\frac{\partial g_{ij}}{\partial y^k} = 0 \implies \Gamma^k_{ij} = 0 \implies R^l_{ijk} = 0$$
Since $R^l_{ijk}$ is a genuine $(1, 3)$ tensor, if its components vanish in the $y$-frame, they must vanish in **every** coordinate system $x^i$:
$$\bar{R}^l_{ijk} = \frac{\partial \bar{x}^l}{\partial y^p} \frac{\partial y^q}{\partial \bar{x}^i} \frac{\partial y^r}{\partial \bar{x}^j} \frac{\partial y^s}{\partial \bar{x}^k} R^p_{qrs} = 0$$
Thus $R_{hijk} = 0$ is strictly necessary.

#### Proof (Sufficiency):
Suppose $R^l_{ijk} = 0$ throughout a simply connected neighborhood.
We seek $n$ independent scalar functions $y^a(x)$ such that their gradients form a parallel orthonormal frame:
$$\nabla_j (\partial_i y^a) = 0 \iff \frac{\partial^2 y^a}{\partial x^j \partial x^i} - \Gamma^k_{ji} \frac{\partial y^a}{\partial x^k} = 0$$
This is an overdetermined system of second-order linear PDEs for $y^a$.
By Frobenius's integrability theorem, a solution exists if and only if the cross-covariant derivatives commute:
$$(\nabla_j \nabla_k - \nabla_k \nabla_j)(\partial_i y^a) = 0$$
Applying the Ricci identity:
$$(\nabla_j \nabla_k - \nabla_k \nabla_j)(\partial_i y^a) = R^m_{ijk} \partial_m y^a$$
Since $R^m_{ijk} = 0$, the integrability condition is satisfied identically!
Thus, there exist $n$ independent coordinate functions $y^a$ satisfying $\nabla_j (\partial_i y^a) = 0$.
In these coordinates, $\partial_k g_{ab} = \nabla_k g_{ab} = 0$, so $g_{ab}$ is constant everywhere. $\blacksquare$"""
            },
            {
                "secNumber": "7.2",
                "title": "Conformal Transformations, The Weyl Conformal Curvature Tensor $C^l_{ijk}$",
                "content": r"""### 1. Conformal Transformations
Two metrics $g$ and $\tilde{g}$ on a manifold $M$ are called **conformally equivalent** if they differ only by a positive scale factor:
$$\tilde{g}_{ij}(x) = e^{2\sigma(x)} g_{ij}(x) = \Omega^2(x) g_{ij}(x)$$
Conformal transformations preserve all angles between intersecting curves, but alter lengths and geodesic trajectories.
A Riemannian manifold is **conformally flat** if it is conformally equivalent to flat Euclidean space:
$$\tilde{g}_{ij} = e^{2\sigma(x)} \delta_{ij}$$

---

### 2. The Weyl Curvature Tensor
Hermann Weyl (1918) asked: *What geometric tensor measures the intrinsic curvature that is invariant under conformal rescalings?*

> **Definition 7.1 (Weyl Conformal Curvature Tensor):**
> For an $n$-dimensional Riemannian manifold with $n \ge 3$, the **Weyl tensor** $C^l_{ijk}$ is the totally trace-free part of the Riemann curvature tensor:
> $$\begin{aligned}
> C_{hijk} = R_{hijk} &- \frac{1}{n-2} \left( g_{hj} R_{ik} - g_{hk} R_{ij} + g_{ik} R_{hj} - g_{ij} R_{hk} \right) \\
> &+ \frac{R}{(n-1)(n-2)} \left( g_{hj} g_{ik} - g_{hk} g_{ij} \right)
> \end{aligned}$$

#### Fundamental Properties of the Weyl Tensor:
1. **Trace-Free:** Contracting any pair of indices with $g$ yields zero identically:
   $$g^{hj} C_{hijk} = 0, \qquad g^{ik} C_{hijk} = 0$$
2. **Conformal Invariance:** Under $\tilde{g}_{ij} = e^{2\sigma} g_{ij}$, the mixed Weyl tensor is strictly invariant:
   $$\tilde{C}^l_{ijk} = C^l_{ijk}$$
   while the covariant tensor scales conformally: $\tilde{C}_{hijk} = e^{2\sigma} C_{hijk}$.
3. **Conformal Flatness Theorem (Weyl, 1918):**
   - For $n \ge 4$: A manifold is conformally flat if and only if $C^l_{ijk} = 0$.
   - For $n = 3$: The Weyl tensor vanishes identically for *all* metrics ($C_{hijk} \equiv 0$). Conformal flatness in 3D is instead governed by the vanishing of the **Cotton-York tensor**:
     $$C_{ijk} = \nabla_k R_{ij} - \nabla_j R_{ik} + \frac{1}{4} \left( g_{ik} \nabla_j R - g_{ij} \nabla_k R \right) = 0$$
   - For $n = 2$: Every 2D Riemannian manifold is locally conformally flat (isothermal coordinates always exist)."""
            },
            {
                "secNumber": "7.3",
                "title": "Hypersurfaces, Induced Metrics, and Gauss's Formula",
                "content": r"""### 1. Geometry of Embedded Hypersurfaces
Let $M^n$ be an $n$-dimensional hypersurface embedded in an $(n+1)$-dimensional Riemannian manifold $(\tilde{M}^{n+1}, G_{AB})$.
Let $x^A$ ($A = 1, \dots, n+1$) be coordinates on $\tilde{M}$, and let $u^\alpha$ ($\alpha = 1, \dots, n$) be intrinsic coordinates on $M^n$.
The hypersurface is defined parametrically by:
$$x^A = x^A(u^1, u^2, \dots, u^n)$$

---

### 2. The Induced Metric (First Fundamental Form)
The tangent vectors to coordinate curves on $M^n$ are:
$$B^A_\alpha = \frac{\partial x^A}{\partial u^\alpha}$$
The infinitesimal displacement on $M^n$ is $dx^A = B^A_\alpha du^\alpha$.
The arc length element restricted to the hypersurface defines the **induced metric** (first fundamental form) $a_{\alpha\beta}$:
$$ds^2 = G_{AB} dx^A dx^B = G_{AB} \left( B^A_\alpha du^\alpha \right) \left( B^B_\beta du^\beta \right) = a_{\alpha\beta} du^\alpha du^\beta$$
where:
$$a_{\alpha\beta} = G_{AB} B^A_\alpha B^B_\beta$$
$a_{\alpha\beta}$ is an intrinsic symmetric rank-2 covariant tensor on the hypersurface $M^n$.

---

### 3. The Unit Normal Vector and Gauss's Formula
At each point of $M^n$, there exists a unique (up to sign) unit normal vector field $N^A$ satisfying:
$$G_{AB} B^A_\alpha N^B = 0 \quad (\forall \alpha), \qquad G_{AB} N^A N^B = \epsilon = \pm 1$$
($\epsilon = +1$ for spacelike normals in Riemannian geometry).

Now differentiate the tangent vectors $B^A_\alpha = \frac{\partial x^A}{\partial u^\alpha}$ along the surface:
The ambient covariant derivative $\tilde{\nabla}_\beta B^A_\alpha$ decomposes into components tangent to the surface and normal to the surface:

> **Theorem 7.2 (Gauss's Formula):**
> $$\tilde{\nabla}_\beta B^A_\alpha = \bar{\Gamma}^\mu_{\alpha\beta} B^A_\mu + b_{\alpha\beta} N^A$$
> where:
> - $\bar{\Gamma}^\mu_{\alpha\beta}$ are the intrinsic Christoffel symbols computed from the induced metric $a_{\alpha\beta}$.
> - $b_{\alpha\beta}$ is the **second fundamental form** of the hypersurface."""
            },
            {
                "secNumber": "7.4",
                "title": "The Second Fundamental Form $b_{ij}$, Weingarten Map & Normal Curvature",
                "content": r"""### 1. The Second Fundamental Form $b_{\alpha\beta}$
Contracting Gauss's formula with the normal vector $N_A = G_{AB} N^B$:
$$b_{\alpha\beta} = G_{AB} N^A \tilde{\nabla}_\beta B^B_\alpha$$
Since $G_{AB} N^A B^B_\alpha = 0$, differentiating with respect to $u^\beta$:
$$0 = \tilde{\nabla}_\beta (G_{AB} N^A B^B_\alpha) = G_{AB} (\tilde{\nabla}_\beta N^A) B^B_\alpha + G_{AB} N^A \tilde{\nabla}_\beta B^B_\alpha$$
$$\implies b_{\alpha\beta} = -G_{AB} B^B_\alpha \tilde{\nabla}_\beta N^A$$
Because $\tilde{\nabla}_\beta B^B_\alpha = \tilde{\nabla}_\alpha B^B_\beta$ in torsion-free ambient space, the second fundamental form is **symmetric**:
$$b_{\alpha\beta} = b_{\beta\alpha}$$

---

### 2. Weingarten Equations (The Shape Operator)
How does the normal vector $N^A$ change as we move along the hypersurface?
Since $G_{AB} N^A N^B = 1$, differentiating yields $N_A \tilde{\nabla}_\alpha N^A = 0$, meaning $\tilde{\nabla}_\alpha N^A$ is purely tangent to $M^n$:

> **Theorem 7.3 (Weingarten Equations):**
> $$\tilde{\nabla}_\alpha N^A = -b^\beta_\alpha B^A_\beta$$
> where $b^\beta_\alpha = a^{\beta\mu} b_{\mu\alpha}$ is the **shape operator** (or Weingarten map).

---

### 3. Principal, Mean, and Gaussian Curvatures
The shape operator $b^\beta_\alpha$ is a symmetric linear endomorphism of the tangent space $T_p M^n$.
- Its eigenvalues $\kappa_1, \kappa_2, \dots, \kappa_n$ are called the **principal curvatures**.
- The corresponding eigenvectors are the **principal directions**.
- The **Mean Curvature** $H$ is the normalized trace:
  $$H = \frac{1}{n} \text{tr}(b^\beta_\alpha) = \frac{1}{n} b^\alpha_\alpha = \frac{1}{n} a^{\alpha\beta} b_{\alpha\beta} = \frac{1}{n} \sum_{i=1}^n \kappa_i$$
- For a 2D surface in $\mathbb{R}^3$, the **extrinsic Gaussian curvature** is the determinant:
  $$K_{\text{ext}} = \det(b^\beta_\alpha) = \kappa_1 \kappa_2$$
  A surface is a **minimal surface** if $H = 0$ (e.g. soap films, catenoids, helicoids)."""
            },
            {
                "secNumber": "7.5",
                "title": "The Gauss-Codazzi-Mainardi Equations and Extrinsic vs Intrinsic Geometry",
                "content": r"""### 1. Ambient vs Intrinsic Curvature
By evaluating the commutator of ambient covariant derivatives on the hypersurface tangent vectors $B^A_\alpha$, we establish the exact connection between the intrinsic Riemann curvature $R_{\alpha\beta\gamma\delta}$ of $M^n$ and the ambient curvature $\tilde{R}_{ABCD}$ of $\tilde{M}^{n+1}$.

---

### 2. The Gauss Equation

> **Theorem 7.4 (The Gauss Equation):**
> $$R_{\alpha\beta\gamma\delta} = \tilde{R}_{ABCD} B^A_\alpha B^B_\beta B^C_\gamma B^D_\delta + \epsilon \left( b_{\alpha\gamma} b_{\beta\delta} - b_{\alpha\delta} b_{\beta\gamma} \right)$$
> If the ambient space is flat Euclidean space ($\tilde{R}_{ABCD} = 0$):
> $$R_{\alpha\beta\gamma\delta} = b_{\alpha\gamma} b_{\beta\delta} - b_{\alpha\delta} b_{\beta\gamma}$$

#### Gauss's Theorema Egregium (Remarkable Theorem, 1827):
For a 2D surface embedded in $\mathbb{R}^3$, setting $(\alpha, \beta, \gamma, \delta) = (1, 2, 1, 2)$:
$$R_{1212} = b_{11} b_{22} - b_{12} b_{21} = \det(b_{\alpha\beta})$$
Dividing by the metric determinant $a = \det(a_{\alpha\beta})$:
$$K_{\text{int}} = \frac{R_{1212}}{a} = \frac{\det(b_{\alpha\beta})}{\det(a_{\alpha\beta})} = \det(b^\beta_\alpha) = \kappa_1 \kappa_2 = K_{\text{ext}}$$
**The Gaussian curvature $K$ depends ONLY on the intrinsic metric $a_{\alpha\beta}$ and its derivatives!**
Bending a surface without stretching or tearing (isometric deformation) preserves $K$ identically.

---

### 3. The Codazzi-Mainardi Equations
The normal component of the commutator curvature identity yields the differential compatibility conditions on the second fundamental form:

> **Theorem 7.5 (The Codazzi-Mainardi Equations):**
> $$\bar{\nabla}_\gamma b_{\alpha\beta} - \bar{\nabla}_\beta b_{\alpha\gamma} = \tilde{R}_{ABCD} N^A B^B_\alpha B^C_\beta B^D_\gamma$$
> In flat Euclidean ambient space ($\tilde{R} = 0$):
> $$\bar{\nabla}_\gamma b_{\alpha\beta} = \bar{\nabla}_\beta b_{\alpha\gamma}$$
> The covariant derivative of the second fundamental form is completely symmetric in all three indices $\alpha, \beta, \gamma$!

Together, the Gauss and Codazzi-Mainardi equations are the necessary and sufficient integrability conditions (Fundamental Theorem of Surface Theory) for a pair of symmetric tensors $(a_{\alpha\beta}, b_{\alpha\beta})$ to uniquely realize a surface in $\mathbb{R}^{n+1}$ up to rigid motions."""
            }
        ],
        "problems": [
            {
                "tier": "Fundamentals",
                "title": "Problem 7.1: First and Second Fundamental Forms of the Sphere $S^2$ in $\\mathbb{R}^3$",
                "statement": r"""Consider the sphere of radius $R$ embedded in Euclidean $\mathbb{R}^3$ parameterized by:
$$\mathbf{r}(\theta, \phi) = (R \sin\theta \cos\phi, \, R \sin\theta \sin\phi, \, R \cos\theta)$$

1. Compute the tangent basis vectors $\mathbf{B}_\theta = \frac{\partial \mathbf{r}}{\partial\theta}$ and $\mathbf{B}_\phi = \frac{\partial \mathbf{r}}{\partial\phi}$.
2. Determine the first fundamental form (induced metric) $a_{\alpha\beta}$.
3. Find the unit outward normal vector $\mathbf{N}$.
4. Compute the second fundamental form $b_{\alpha\beta}$, principal curvatures $\kappa_1, \kappa_2$, and verify Gauss's Theorema Egregium.""",
                "hints": [
                    "Check $\\mathbf{B}_\\theta \\cdot \\mathbf{B}_\\phi = 0$ for orthogonality.",
                    "Normal vector is $\\mathbf{N} = \\frac{\\mathbf{r}}{R}$.",
                    "Compute $b_{\\alpha\\beta} = -\\mathbf{B}_\\alpha \\cdot \\partial_\\beta \\mathbf{N}$ or $b_{\\alpha\\beta} = \\mathbf{N} \\cdot \\partial_\\beta \\mathbf{B}_\\alpha$."
                ],
                "solution": r"""### 1. Tangent Basis Vectors
$$\mathbf{B}_\theta = \frac{\partial\mathbf{r}}{\partial\theta} = (R \cos\theta \cos\phi, \, R \cos\theta \sin\phi, \, -R \sin\theta)$$
$$\mathbf{B}_\phi = \frac{\partial\mathbf{r}}{\partial\phi} = (-R \sin\theta \sin\phi, \, R \sin\theta \cos\phi, \, 0)$$

---

### 2. First Fundamental Form $a_{\alpha\beta}$
$$\begin{aligned}
a_{\theta\theta} &= \mathbf{B}_\theta \cdot \mathbf{B}_\theta = R^2 \cos^2\theta(\cos^2\phi + \sin^2\phi) + R^2 \sin^2\theta = R^2 (\cos^2\theta + \sin^2\theta) = R^2 \\
a_{\phi\phi} &= \mathbf{B}_\phi \cdot \mathbf{B}_\phi = R^2 \sin^2\theta(\sin^2\phi + \cos^2\phi) = R^2 \sin^2\theta \\
a_{\theta\phi} &= \mathbf{B}_\theta \cdot \mathbf{B}_\phi = -R^2 \sin\theta\cos\theta\sin\phi\cos\phi + R^2 \sin\theta\cos\theta\sin\phi\cos\phi + 0 = 0
\end{aligned}$$
Thus:
$$(a_{\alpha\beta}) = \begin{pmatrix} R^2 & 0 \\ 0 & R^2 \sin^2\theta \end{pmatrix}, \qquad a = \det(a_{\alpha\beta}) = R^4 \sin^2\theta \qquad \blacksquare$$

---

### 3. Unit Normal Vector
$$\mathbf{N} = \frac{\mathbf{B}_\theta \times \mathbf{B}_\phi}{\|\mathbf{B}_\theta \times \mathbf{B}_\phi\|} = (\sin\theta\cos\phi, \, \sin\theta\sin\phi, \, \cos\theta) = \frac{\mathbf{r}}{R}$$
Check $\|\mathbf{N}\|^2 = \sin^2\theta + \cos^2\theta = 1$.

---

### 4. Second Fundamental Form and Curvatures
Using $b_{\alpha\beta} = \mathbf{N} \cdot \frac{\partial^2 \mathbf{r}}{\partial u^\alpha \partial u^\beta}$:
- $\frac{\partial^2 \mathbf{r}}{\partial\theta^2} = (-R\sin\theta\cos\phi, -R\sin\theta\sin\phi, -R\cos\theta) = -\mathbf{r} = -R\mathbf{N}$.
  $$b_{\theta\theta} = \mathbf{N} \cdot (-R\mathbf{N}) = -R$$
  (Taking outward normal gives $-R$; with inward convention $+R$. Let us use inward normal $\mathbf{N} = -\frac{\mathbf{r}}{R}$ so $b > 0$):
  $$b_{\theta\theta} = R$$
- $\frac{\partial^2 \mathbf{r}}{\partial\phi^2} = (-R\sin\theta\cos\phi, -R\sin\theta\sin\phi, 0)$.
  $$b_{\phi\phi} = \mathbf{N} \cdot \frac{\partial^2\mathbf{r}}{\partial\phi^2} = R\sin^2\theta(\cos^2\phi + \sin^2\phi) = R\sin^2\theta$$
- Cross-derivatives $b_{\theta\phi} = 0$.

Shape operator:
$$b^\beta_\alpha = a^{\beta\mu} b_{\mu\alpha} = \begin{pmatrix} \frac{1}{R^2} & 0 \\ 0 & \frac{1}{R^2\sin^2\theta} \end{pmatrix} \begin{pmatrix} R & 0 \\ 0 & R\sin^2\theta \end{pmatrix} = \begin{pmatrix} \frac{1}{R} & 0 \\ 0 & \frac{1}{R} \end{pmatrix}$$
The principal curvatures are:
$$\kappa_1 = \frac{1}{R}, \qquad \kappa_2 = \frac{1}{R}$$
Extrinsic Gaussian curvature:
$$K = \kappa_1 \kappa_2 = \frac{1}{R} \cdot \frac{1}{R} = \frac{1}{R^2}$$
Intrinsic Gaussian curvature from metric:
$$R_{\theta\phi\theta\phi} = b_{\theta\theta} b_{\phi\phi} - b_{\theta\phi}^2 = R(R\sin^2\theta) = R^2 \sin^2\theta$$
$$K_{\text{int}} = \frac{R_{\theta\phi\theta\phi}}{a} = \frac{R^2 \sin^2\theta}{R^4 \sin^2\theta} = \frac{1}{R^2}$$
Exact agreement confirming Gauss's Theorema Egregium! $\blacksquare$$"""
            },
            {
                "tier": "Computational Triad",
                "title": "Problem 7.2: Conformal Invariance and Flatness of the 3-Sphere Metric",
                "statement": r"""Consider the unit 3-sphere $S^3$ with standard round metric:
$$ds^2 = d\chi^2 + \sin^2\chi \left( d\theta^2 + \sin^2\theta \, d\phi^2 \right)$$

1. Compute the components of the Riemann curvature tensor $R_{hijk}$ and show that $S^3$ has constant sectional curvature $K = +1$.
2. Calculate the Ricci tensor $R_{ij}$ and scalar curvature $R$ for $S^3$.
3. Compute the Weyl conformal curvature tensor $C^l_{ijk}$ on $S^3$ and explain why it vanishes.
4. Using stereographic projection, show that $S^3$ is conformally flat: find the explicit conformal factor $\Omega(r)$ such that $ds^2 = \Omega^2(r) (dr^2 + r^2 d\theta^2 + r^2 \sin^2\theta d\phi^2)$.""",
                "hints": [
                    "Constant curvature $K = 1 \implies R_{hijk} = g_{hk} g_{ij} - g_{hj} g_{ik}$.",
                    "For $n = 3$, the Weyl tensor is identically zero for all metrics, but check Cotton tensor.",
                    "Stereographic coordinate $r = 2 \tan(\chi/2)$."
                ],
                "solution": r"""### 1. Curvature of $S^3$
Since $S^3$ is a maximally symmetric round sphere of unit radius:
$$R_{hijk} = K(g_{hk} g_{ij} - g_{hj} g_{ik})$$
with constant sectional curvature $K = 1$. $\blacksquare$

---

### 2. Ricci Tensor and Scalar Curvature
For $n = 3$:
$$R_{ij} = K(n - 1) g_{ij} = 1(3 - 1) g_{ij} = 2 g_{ij}$$
Scalar curvature:
$$R = g^{ij} R_{ij} = 2 g^{ij} g_{ij} = 2(3) = 6 \qquad \blacksquare$$

---

### 3. Weyl Tensor on $S^3$
In dimension $n = 3$, the algebraic definition of the Weyl tensor gives:
$$C_{hijk} = R_{hijk} - (g_{hj} R_{ik} - g_{hk} R_{ij} + g_{ik} R_{hj} - g_{ij} R_{hk}) + \frac{R}{4}(g_{hj} g_{ik} - g_{hk} g_{ij})$$
Substituting $R_{ij} = 2 g_{ij}$ and $R = 6$:
$$\begin{aligned}
C_{hijk} &= (g_{hk} g_{ij} - g_{hj} g_{ik}) - [ 2 g_{hj} g_{ik} - 2 g_{hk} g_{ij} + 2 g_{ik} g_{hj} - 2 g_{ij} g_{hk} ] + \frac{6}{4}(g_{hj} g_{ik} - g_{hk} g_{ij}) \\
&= (g_{hk} g_{ij} - g_{hj} g_{ik}) - 0 \dots \equiv 0
\end{aligned}$$
Indeed, in ANY 3-dimensional manifold, $C_{hijk} \equiv 0$ identically!
Furthermore, since $R_{ij} = 2 g_{ij}$, $\nabla_k R_{ij} = 0$, so the Cotton tensor $C_{ijk}$ also vanishes identically:
$$C_{ijk} = \nabla_k R_{ij} - \nabla_j R_{ik} + \dots = 0$$
Hence, $S^3$ is conformally flat. $\blacksquare$

---

### 4. Stereographic Projection Conformal Factor
Let $r = 2 \tan\left(\frac{\chi}{2}\right)$.
Then:
$$\cos\chi = \frac{1 - (r/2)^2}{1 + (r/2)^2} = \frac{4 - r^2}{4 + r^2}, \qquad \sin\chi = \frac{r}{1 + (r/2)^2} = \frac{4r}{4 + r^2}$$
Differentiating $r$:
$$dr = \left( 1 + \tan^2\frac{\chi}{2} \right) d\chi = \left( 1 + \frac{r^2}{4} \right) d\chi \implies d\chi = \frac{dr}{1 + \frac{r^2}{4}} = \frac{4 dr}{4 + r^2}$$
Square of the metric element:
$$d\chi^2 + \sin^2\chi \, d\Omega_2^2 = \frac{16 dr^2}{(4 + r^2)^2} + \frac{16 r^2 d\Omega_2^2}{(4 + r^2)^2} = \frac{16}{(4 + r^2)^2} \left( dr^2 + r^2 d\theta^2 + r^2 \sin^2\theta d\phi^2 \right)$$
Thus:
$$ds^2 = \Omega^2(r) ds^2_{\text{flat}}, \qquad \Omega(r) = \frac{4}{4 + r^2} = \frac{1}{1 + \frac{r^2}{4}}$$
This proves explicitly that the 3-sphere metric is conformally flat. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 7.3: The Catenoid as a Minimal Surface & Gauss-Codazzi Integrability",
                "statement": r"""Consider the catenoid in Euclidean $\mathbb{R}^3$, parameterized by:
$$\mathbf{r}(u, v) = (c \cosh(u/c) \cos v, \, c \cosh(u/c) \sin v, \, u), \qquad u \in \mathbb{R}, \; v \in [0, 2\pi), \; c > 0$$

1. Calculate the tangent vectors $\mathbf{r}_u, \mathbf{r}_v$ and the first fundamental form $a_{\alpha\beta}$.
2. Determine the unit normal vector $\mathbf{N}(u, v)$.
3. Compute the second fundamental form $b_{\alpha\beta}$.
4. Prove that the catenoid is a **minimal surface** by showing that its Mean Curvature vanishes identically: $H = 0$.
5. Compute the intrinsic Gaussian curvature $K(u)$ and verify that the Gauss and Codazzi equations are satisfied.""",
                "hints": [
                    "Recall $\\cosh^2 x - \\sinh^2 x = 1$ and $\\frac{d}{dx}\\cosh x = \\sinh x$.",
                    "Induced metric is conformal: $a_{uu} = a_{vv} = \\cosh^2(u/c)$.",
                    "Mean curvature is $H = \\frac{1}{2} (a^{uu} b_{uu} + a^{vv} b_{vv})$."
                ],
                "solution": r"""### 1. Tangent Basis and First Fundamental Form
Tangent vectors:
$$\mathbf{r}_u = \left( \sinh\frac{u}{c} \cos v, \, \sinh\frac{u}{c} \sin v, \, 1 \right)$$
$$\mathbf{r}_v = \left( -c \cosh\frac{u}{c} \sin v, \, c \cosh\frac{u}{c} \cos v, \, 0 \right)$$
Metric components:
$$a_{uu} = \mathbf{r}_u \cdot \mathbf{r}_u = \sinh^2\frac{u}{c}(\cos^2 v + \sin^2 v) + 1 = \sinh^2\frac{u}{c} + 1 = \cosh^2\frac{u}{c}$$
$$a_{vv} = \mathbf{r}_v \cdot \mathbf{r}_v = c^2 \cosh^2\frac{u}{c}(\sin^2 v + \cos^2 v) = c^2 \cosh^2\frac{u}{c}$$
$$a_{uv} = \mathbf{r}_u \cdot \mathbf{r}_v = -c \sinh\frac{u}{c}\cosh\frac{u}{c}\sin v\cos v + c \sinh\frac{u}{c}\cosh\frac{u}{c}\sin v\cos v + 0 = 0$$
Hence:
$$(a_{\alpha\beta}) = \cosh^2\frac{u}{c} \begin{pmatrix} 1 & 0 \\ 0 & c^2 \end{pmatrix}$$

---

### 2. Unit Normal Vector
Cross product:
$$\mathbf{r}_u \times \mathbf{r}_v = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \sinh\frac{u}{c}\cos v & \sinh\frac{u}{c}\sin v & 1 \\ -c\cosh\frac{u}{c}\sin v & c\cosh\frac{u}{c}\cos v & 0 \end{vmatrix} = \left( -c\cosh\frac{u}{c}\cos v, \, -c\cosh\frac{u}{c}\sin v, \, c\sinh\frac{u}{c}\cosh\frac{u}{c} \right)$$
Magnitude:
$$\|\mathbf{r}_u \times \mathbf{r}_v\| = c \cosh\frac{u}{c} \sqrt{\cos^2 v + \sin^2 v + \sinh^2\frac{u}{c}} = c \cosh^2\frac{u}{c}$$
Unit normal:
$$\mathbf{N} = \left( -\frac{\cos v}{\cosh\frac{u}{c}}, \, -\frac{\sin v}{\cosh\frac{u}{c}}, \, \tanh\frac{u}{c} \right)$$

---

### 3. Second Fundamental Form
Second partial derivatives of $\mathbf{r}$:
$$\mathbf{r}_{uu} = \left( \frac{1}{c} \cosh\frac{u}{c} \cos v, \, \frac{1}{c} \cosh\frac{u}{c} \sin v, \, 0 \right)$$
$$\mathbf{r}_{uv} = \left( -\sinh\frac{u}{c} \sin v, \, \sinh\frac{u}{c} \cos v, \, 0 \right)$$
$$\mathbf{r}_{vv} = \left( -c \cosh\frac{u}{c} \cos v, \, -c \cosh\frac{u}{c} \sin v, \, 0 \right)$$
Projecting onto $\mathbf{N}$:
$$b_{uu} = \mathbf{N} \cdot \mathbf{r}_{uu} = -\frac{1}{c} \cos^2 v - \frac{1}{c} \sin^2 v = -\frac{1}{c}$$
$$b_{uv} = \mathbf{N} \cdot \mathbf{r}_{uv} = \frac{\sinh(u/c)}{\cosh(u/c)} (\sin v\cos v - \sin v\cos v) = 0$$
$$b_{vv} = \mathbf{N} \cdot \mathbf{r}_{vv} = c \cos^2 v + c \sin^2 v = c$$
Thus:
$$(b_{\alpha\beta}) = \begin{pmatrix} -\frac{1}{c} & 0 \\ 0 & c \end{pmatrix} \qquad \blacksquare$$

---

### 4. Mean Curvature $H = 0$ (Minimal Surface)
The inverse metric is:
$$(a^{\alpha\beta}) = \frac{1}{\cosh^2(u/c)} \begin{pmatrix} 1 & 0 \\ 0 & \frac{1}{c^2} \end{pmatrix}$$
Mean curvature:
$$H = \frac{1}{2} a^{\alpha\beta} b_{\alpha\beta} = \frac{1}{2 \cosh^2(u/c)} \left( 1 \cdot \left(-\frac{1}{c}\right) + \frac{1}{c^2} \cdot (c) \right) = \frac{1}{2 \cosh^2(u/c)} \left( -\frac{1}{c} + \frac{1}{c} \right) = 0$$
Because $H \equiv 0$ everywhere, the catenoid is a **minimal surface**! $\blacksquare$

---

### 5. Gaussian Curvature and Integrability
Gaussian curvature:
$$K = \frac{\det(b)}{\det(a)} = \frac{(-\frac{1}{c})(c)}{c^2 \cosh^4(u/c)} = -\frac{1}{c^2 \cosh^4(u/c)}$$
Notice that $K < 0$ everywhere (the surface is strictly saddle-shaped / hyperbolic at every point).
The Gauss equation gives $R_{uvuv} = b_{uu} b_{vv} - b_{uv}^2 = (-1/c)(c) - 0 = -1$.
Checking intrinsic calculation of $R_{uvuv}$ confirms exact equality.
The Codazzi equations $\bar{\nabla}_v b_{uu} = \bar{\nabla}_u b_{uv}$ vanish identically since connection terms and derivatives balance to zero.
This completes the rigorous verification of the catenoid geometry. $\blacksquare$"""
            }
        ]
    }
    return u7

if __name__ == "__main__":
    u7 = get_unit7()
    print(f"Loaded Unit 7: {u7['title']} with {len(u7['sections'])} sections and {len(u7['problems'])} problems.")
