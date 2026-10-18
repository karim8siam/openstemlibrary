# -*- coding: utf-8 -*-
"""
build_dg_unit3.py
Constructs Unit 3: Helices, Involutes, Evolutes & Bertrand Curves
"""

def get_unit3():
    u3 = {
        "number": 3,
        "title": "Helices, Involutes, Evolutes & Bertrand Curves",
        "leadSummary": "Advanced geometric analysis of special space curve classes: general and cylindrical helices, Lancret's theorem, circular helices, spherical indicatrices of the Frenet frame on the unit sphere S^2, string unwinding construction of involutes and evolutes, and the complete characterization of Bertrand curve pairs.",
        "simulations": ["sim_dg_helix_bertrand"],
        "sections": [
            {
                "secNumber": "3.1",
                "title": "Cylindrical and General Helices: Lancret's Theorem",
                "content": r"""### 1. General and Cylindrical Helices

A helix is one of the most fundamental curved structures in mathematics, nature (DNA double helix), and mechanical engineering.

> **Definition 3.1 (General Helix):**
> A regular space curve $\mathbf{r}(s)$ of class $C^3$ with $\kappa(s) > 0$ is called a **general helix** (or cylindrical helix) if its tangent lines make a constant angle $\alpha$ with a fixed non-zero direction vector $\mathbf{u} \in \mathbb{R}^3$:
> $$\mathbf{T}(s) \cdot \mathbf{u} = \cos \alpha = \text{constant} \quad \forall s \in I$$
> where $\mathbf{u}$ is a unit vector ($\|\mathbf{u}\| = 1$) called the **axis** of the helix, and $0 < \alpha < \pi/2$.

---

### 2. Lancret's Theorem

In 1802, Michel Ange Lancret formulated the definitive criterion characterizing all general helices through their curvature and torsion.

> **Theorem 3.1 (Lancret's Theorem):**
> A regular space curve $\mathbf{r}(s)$ with $\kappa(s) > 0$ is a general helix if and only if the ratio of its torsion to its curvature is **constant**:
> $$\frac{\tau(s)}{\kappa(s)} = c = \cot \alpha = \text{constant} \quad \forall s \in I$$

#### Complete Line-by-Line Proof:
$(\implies)$ Assume $\mathbf{r}(s)$ is a general helix.
Then there exists a constant unit vector $\mathbf{u}$ and an angle $\alpha$ such that:
$$\mathbf{T}(s) \cdot \mathbf{u} = \cos \alpha = \text{const}$$
Differentiating with respect to arc-length $s$:
$$\mathbf{T}'(s) \cdot \mathbf{u} = 0 \iff (\kappa(s) \mathbf{N}(s)) \cdot \mathbf{u} = 0$$
Since $\kappa(s) > 0$, this implies:
$$\mathbf{N}(s) \cdot \mathbf{u} = 0 \quad \forall s \in I$$
Thus, the fixed axis vector $\mathbf{u}$ is strictly orthogonal to the principal normal $\mathbf{N}(s)$ at every point!
Because $\{\mathbf{T}, \mathbf{N}, \mathbf{B}\}$ forms an orthonormal basis, $\mathbf{u}$ must lie entirely in the rectifying plane (the plane spanned by $\mathbf{T}$ and $\mathbf{B}$):
$$\mathbf{u} = (\mathbf{u} \cdot \mathbf{T}) \mathbf{T} + (\mathbf{u} \cdot \mathbf{B}) \mathbf{B} = (\cos \alpha) \mathbf{T}(s) + (\sin \alpha) \mathbf{B}(s)$$
Since $\mathbf{u}$ is a constant vector, its derivative with respect to $s$ must be zero:
$$\frac{d\mathbf{u}}{ds} = (\cos \alpha) \frac{d\mathbf{T}}{ds} + (\sin \alpha) \frac{d\mathbf{B}}{ds} = \mathbf{0}$$
Applying the Frenet-Serret formulas $\mathbf{T}' = \kappa \mathbf{N}$ and $\mathbf{B}' = -\tau \mathbf{N}$:
$$\cos \alpha (\kappa(s) \mathbf{N}(s)) + \sin \alpha (-\tau(s) \mathbf{N}(s)) = \mathbf{0}$$
$$[\kappa(s) \cos \alpha - \tau(s) \sin \alpha] \mathbf{N}(s) = \mathbf{0}$$
Since $\|\mathbf{N}(s)\| = 1 \ne 0$:
$$\kappa(s) \cos \alpha - \tau(s) \sin \alpha = 0 \iff \frac{\tau(s)}{\kappa(s)} = \frac{\cos \alpha}{\sin \alpha} = \cot \alpha = \text{constant} \quad \blacksquare$$

$(\impliedby)$ Assume $\frac{\tau(s)}{\kappa(s)} = c = \text{constant}$.
Choose an angle $\alpha \in (0, \pi/2)$ such that $\cot \alpha = c$, so $\cos \alpha = \frac{c}{\sqrt{1 + c^2}}$ and $\sin \alpha = \frac{1}{\sqrt{1 + c^2}}$.
Define the vector field:
$$\mathbf{u}(s) = (\cos \alpha) \mathbf{T}(s) + (\sin \alpha) \mathbf{B}(s)$$
Differentiating $\mathbf{u}(s)$ with respect to $s$:
$$\mathbf{u}'(s) = (\cos \alpha) \mathbf{T}'(s) + (\sin \alpha) \mathbf{B}'(s) = (\cos \alpha) \kappa(s) \mathbf{N}(s) - (\sin \alpha) \tau(s) \mathbf{N}(s)$$
$$= [\kappa(s) \cos \alpha - \tau(s) \sin \alpha] \mathbf{N}(s) = \kappa(s) \left[ \cos \alpha - \frac{\tau(s)}{\kappa(s)} \sin \alpha \right] \mathbf{N}(s) = \kappa(s) [\cos \alpha - (\cot \alpha) \sin \alpha] \mathbf{N}(s) = \mathbf{0}$$
Since $\mathbf{u}'(s) = \mathbf{0}$, $\mathbf{u}$ is a **constant unit vector**!
Finally:
$$\mathbf{T}(s) \cdot \mathbf{u} = \mathbf{T}(s) \cdot [(\cos \alpha) \mathbf{T}(s) + (\sin \alpha) \mathbf{B}(s)] = \cos \alpha \|\mathbf{T}\|^2 + 0 = \cos \alpha = \text{constant}$$
Thus, $\mathbf{r}(s)$ is a general helix with axis $\mathbf{u}$. $\blacksquare$"""
            },
            {
                "secNumber": "3.2",
                "title": "The Circular Helix: Metrics, Intrinsic Equations & Geodesic Property",
                "content": r"""### 1. Parametrization and Metric Relations

A **circular helix** is a general helix drawn on the surface of a right circular cylinder of radius $a$:
$$\mathbf{r}(t) = \begin{pmatrix} a \cos t \\ a \sin t \\ b t \end{pmatrix}, \quad a > 0, \; b > 0$$
- The cylinder radius is $a$.
- The **pitch** (vertical ascent per full revolution $t \in [0, 2\pi]$) is:
  $$h = 2\pi b$$
- The speed is constant $c = \sqrt{a^2 + b^2}$, so arc-length is $s = c t$.

---

### 2. Intrinsic Curvatures of the Circular Helix

As derived in Unit 2:
$$\kappa = \frac{a}{a^2 + b^2} = \text{constant}, \quad \tau = \frac{b}{a^2 + b^2} = \text{constant}$$
Notice that:
- As $b \to 0$, the helix flattens into a circle of radius $a$: $\kappa \to 1/a$, $\tau \to 0$.
- As $a \to 0$, the helix straightens into a vertical line: $\kappa \to 0$, $\tau \to 0$.

> **Theorem 3.2 (Characterization of Circular Helices):**
> A space curve is a circular helix if and only if **both its curvature $\kappa$ and its torsion $\tau$ are non-zero constants**.
> 
> *Proof:* By Lancret's theorem, $\tau/\kappa = \text{const}$ implies it is a general helix. If $\kappa = \text{const}$, then the radius of curvature $\rho = 1/\kappa = \text{const}$. The projection of the curve onto a plane perpendicular to the axis is a planar curve of constant curvature, which is a circle of radius $a = \frac{\kappa}{\kappa^2 + \tau^2}$. Thus the curve is a circular helix. $\blacksquare$

---

### 3. Geodesic Property on the Cylinder
If we slit the circular cylinder along a vertical generator and flatten it onto the Euclidean plane, the circular helix unrolls into a **straight line**!
Because straight lines minimize distance on the Euclidean plane, the circular helix is a **geodesic** (shortest path) on the cylindrical surface."""
            },
            {
                "secNumber": "3.3",
                "title": "Spherical Indicatrices of the Frenet Frame",
                "content": r"""### 1. The Concept of a Spherical Indicatrix

Given a space curve $\mathbf{r}(s)$, we can map the vectors of its moving Frenet frame $\{\mathbf{T}, \mathbf{N}, \mathbf{B}\}$ to points on the unit sphere $S^2 = \{ \mathbf{x} \in \mathbb{R}^3 : \|\mathbf{x}\| = 1 \}$.

> **Definition 3.2 (The Three Spherical Indicatrices):**
> 1. **Tangent Spherical Indicatrix:**
>    The curve traced on $S^2$ by the unit tangent vector:
>    $$\mathbf{r}_T(s) = \mathbf{T}(s)$$
> 2. **Principal Normal Spherical Indicatrix:**
>    The curve traced on $S^2$ by the principal normal vector:
>    $$\mathbf{r}_N(s) = \mathbf{N}(s)$$
> 3. **Binormal Spherical Indicatrix:**
>    The curve traced on $S^2$ by the binormal vector:
>    $$\mathbf{r}_B(s) = \mathbf{B}(s)$$

---

### 2. Metrics and Curvatures of the Indicatrices

> **Theorem 3.3 (Arc-Length Differentials of Spherical Indicatrices):**
> Let $s_T, s_N, s_B$ denote the arc-lengths of the tangent, normal, and binormal indicatrices, respectively. Then:
> 1. **Tangent Indicatrix:**
>    $$\frac{ds_T}{ds} = \left\| \frac{d\mathbf{T}}{ds} \right\| = \|\kappa \mathbf{N}\| = \kappa(s) \implies ds_T = \kappa(s) \, ds$$
> 2. **Binormal Indicatrix:**
>    $$\frac{ds_B}{ds} = \left\| \frac{d\mathbf{B}}{ds} \right\| = \|-\tau \mathbf{N}\| = |\tau(s)| \implies ds_B = |\tau(s)| \, ds$$
> 3. **Principal Normal Indicatrix:**
>    $$\frac{ds_N}{ds} = \left\| \frac{d\mathbf{N}}{ds} \right\| = \|-\kappa \mathbf{T} + \tau \mathbf{B}\| = \sqrt{\kappa(s)^2 + \tau(s)^2} \implies ds_N = \sqrt{\kappa^2 + \tau^2} \, ds$$

#### Remarkable Geometric Interpretation:
- The total length of the tangent indicatrix is $\int \kappa \, ds$, which is the **total curvature** of the curve.
- The total length of the binormal indicatrix is $\int |\tau| \, ds$, which is the **total torsion** of the curve.
- The principal normal indicatrix advances at the speed of the Darboux vector: $\|\boldsymbol{\omega}\| = \sqrt{\kappa^2 + \tau^2}$!"""
            },
            {
                "secNumber": "3.4",
                "title": "Involutes and Evolutes of Space Curves",
                "content": r"""### 1. Involutes of a Space Curve

An **involute** of a curve $\mathbf{r}(s)$ is the trajectory traced by the end of a taut string being unwound from the curve.

> **Definition 3.3 (Involute):**
> Let $\mathbf{r}(s)$ be an arc-length parametrized $C^2$ curve. An **involute** $\mathbf{r}^*(s)$ is defined by:
> $$\mathbf{r}^*(s) = \mathbf{r}(s) + (c - s) \mathbf{T}(s)$$
> where $c$ is an arbitrary constant (the total length of the unwinding string).

> **Theorem 3.4 (Orthogonality Property of Involutes):**
> The tangent line to the original curve $\mathbf{r}(s)$ is orthogonal to the velocity vector of the involute $\mathbf{r}^*(s)$.
> 
> *Proof:* Differentiating $\mathbf{r}^*(s)$ with respect to $s$:
> $$\frac{d\mathbf{r}^*}{ds} = \mathbf{r}'(s) - \mathbf{T}(s) + (c - s) \mathbf{T}'(s) = \mathbf{T}(s) - \mathbf{T}(s) + (c - s) \kappa(s) \mathbf{N}(s) = (c - s) \kappa(s) \mathbf{N}(s)$$
> Taking the dot product with $\mathbf{T}(s)$:
> $$\frac{d\mathbf{r}^*}{ds} \cdot \mathbf{T}(s) = (c - s) \kappa(s) (\mathbf{N}(s) \cdot \mathbf{T}(s)) = 0 \quad \blacksquare$$

---

### 2. Evolutes of a Space Curve

> **Definition 3.4 (Evolute):**
> A curve $E$ is an **evolute** of a curve $C$ if $C$ is an involute of $E$.
> In space, the tangents to an evolute are normal lines to the original curve.
> An evolute lies on the envelope of normal planes of the original curve and has equation:
> $$\mathbf{r}_E(s) = \mathbf{r}(s) + \rho(s) \mathbf{N}(s) + \rho(s) \cot\left( \int \tau \, ds + c \right) \mathbf{B}(s)$$
> where $\rho = 1/\kappa$ is the radius of curvature."""
            },
            {
                "secNumber": "3.5",
                "title": "Bertrand Curves and Bertrand Mates: Linear Identity a*kappa + b*tau = 1",
                "content": r"""### 1. Definition of Bertrand Curves

In 1850, Joseph Bertrand investigated curve pairs whose principal normal lines coincide everywhere in space.

> **Definition 3.5 (Bertrand Curve and Bertrand Mate):**
> A regular space curve $\mathbf{r}(s)$ is a **Bertrand curve** if there exists another distinct curve $\mathbf{r}^*(s)$ such that the principal normal line to $\mathbf{r}$ at $s$ is identical to the principal normal line to $\mathbf{r}^*$ at the corresponding point $s^*$.
> The curve $\mathbf{r}^*$ is called a **Bertrand mate** (or conjugate curve) of $\mathbf{r}$.

---

### 2. The Bertrand Characterization Theorem

> **Theorem 3.5 (Bertrand Curve Characterization):**
> A regular space curve $\mathbf{r}(s)$ with $\kappa(s) > 0$ and $\tau(s) \ne 0$ is a Bertrand curve if and only if there exist non-zero real constants $a$ and $b$ such that:
> $$a \kappa(s) + b \tau(s) = 1 \quad \forall s \in I$$

#### Complete Line-by-Line Proof:
$(\implies)$ Let $\mathbf{r}^*(s)$ be a Bertrand mate of $\mathbf{r}(s)$.
Since their principal normals coincide, $\mathbf{r}^*(s)$ must lie along the principal normal line of $\mathbf{r}(s)$:
$$\mathbf{r}^*(s) = \mathbf{r}(s) + a(s) \mathbf{N}(s)$$
for some scalar function $a(s)$.
Differentiating with respect to $s$:
$$\frac{d\mathbf{r}^*}{ds} = \mathbf{T}(s) + a'(s) \mathbf{N}(s) + a(s) \mathbf{N}'(s) = \mathbf{T} + a' \mathbf{N} + a(-\kappa \mathbf{T} + \tau \mathbf{B}) = (1 - a\kappa) \mathbf{T} + a' \mathbf{N} + a\tau \mathbf{B}$$
By definition of Bertrand mates, the principal normal $\mathbf{N}^*(s)$ must be collinear with $\mathbf{N}(s)$: $\mathbf{N}^* = \pm \mathbf{N}$.
Since $\mathbf{N}^*$ is orthogonal to the tangent vector $\mathbf{T}^* = \frac{d\mathbf{r}^*/ds}{\|d\mathbf{r}^*/ds\|}$, we have:
$$\frac{d\mathbf{r}^*}{ds} \cdot \mathbf{N}(s) = 0$$
Evaluating the dot product:
$$\left[ (1 - a\kappa) \mathbf{T} + a' \mathbf{N} + a\tau \mathbf{B} \right] \cdot \mathbf{N} = a'(s) = 0 \implies a(s) = a = \text{constant}$$
Thus the distance $a$ between corresponding points of Bertrand mates is **strictly constant**!
Now:
$$\frac{d\mathbf{r}^*}{ds} = (1 - a\kappa) \mathbf{T} + a\tau \mathbf{B}$$
Since $\mathbf{T}^*$ is orthogonal to $\mathbf{N}^* = \pm \mathbf{N}$, $\mathbf{T}^*$ lies in the plane spanned by $\mathbf{T}$ and $\mathbf{B}$.
Let $\alpha$ be the angle between $\mathbf{T}^*$ and $\mathbf{T}$:
$$\mathbf{T}^* = (\cos \alpha) \mathbf{T} + (\sin \alpha) \mathbf{B}$$
One can show (by differentiating $\mathbf{T} \cdot \mathbf{T}^*$) that the angle $\alpha$ is **constant**.
Therefore:
$$\frac{d\mathbf{r}^*}{ds} = \frac{ds^*}{ds} \mathbf{T}^* = \frac{ds^*}{ds} [(\cos \alpha) \mathbf{T} + (\sin \alpha) \mathbf{B}]$$
Equating components:
$$1 - a\kappa(s) = \frac{ds^*}{ds} \cos \alpha \quad \text{and} \quad a\tau(s) = \frac{ds^*}{ds} \sin \alpha$$
Eliminating the term $\frac{ds^*}{ds}$:
$$(1 - a\kappa(s)) \sin \alpha = a\tau(s) \cos \alpha \iff \sin \alpha - a\sin\alpha \kappa(s) - a\cos\alpha \tau(s) = 0$$
Dividing by $\sin \alpha \ne 0$:
$$a \kappa(s) + (a \cot \alpha) \tau(s) = 1$$
Letting $b = a \cot \alpha$, we obtain the universal linear relation:
$$a \kappa(s) + b \tau(s) = 1 \quad \blacksquare$$

$(\impliedby)$ If $a\kappa(s) + b\tau(s) = 1$ with $a \ne 0$, defining $\mathbf{r}^*(s) = \mathbf{r}(s) + a\mathbf{N}(s)$ and differentiating shows that its principal normal $\mathbf{N}^*(s)$ is parallel to $\mathbf{N}(s)$. Thus $\mathbf{r}^*(s)$ is a Bertrand mate. $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational / Problem 3.1",
                "title": "Tangent and Binormal Indicatrices of a Circular Helix",
                "statement": r"""Consider the circular helix:
$$\mathbf{r}(t) = \begin{pmatrix} a \cos t \\ a \sin t \\ b t \end{pmatrix}, \quad a > 0, \; b > 0$$
where $c = \sqrt{a^2 + b^2}$.
1. Find the explicit parametric vector equations for the tangent spherical indicatrix $\mathbf{r}_T(t)$ and binormal spherical indicatrix $\mathbf{r}_B(t)$ on the unit sphere $S^2$.
2. Prove that both the tangent and binormal indicatrices are circles on $S^2$.
3. Compute the radius and the total perimeter of each indicatrix over one full turn $t \in [0, 2\pi]$.""",
                "hints": [
                    "Recall T(t) = (-a sin t, a cos t, b) / c and B(t) = (b sin t, -b cos t, a) / c.",
                    "Examine the third component Z: if Z is constant, the curve lies in a horizontal plane Z = const.",
                    "The intersection of a sphere with a plane Z = const is a circle."
                ],
                "solution": r"""### 1. Parametric Equations of the Indicatrices
From Unit 2, the unit tangent vector is:
$$\mathbf{r}_T(t) = \mathbf{T}(t) = \begin{pmatrix} -\frac{a}{c} \sin t \\ \frac{a}{c} \cos t \\ \frac{b}{c} \end{pmatrix}, \quad \text{where } c = \sqrt{a^2 + b^2}$$
The binormal vector is:
$$\mathbf{r}_B(t) = \mathbf{B}(t) = \begin{pmatrix} \frac{b}{c} \sin t \\ -\frac{b}{c} \cos t \\ \frac{a}{c} \end{pmatrix}$$

---

### 2. Proof that Both Indicatrices are Circles on $S^2$
- **Tangent Indicatrix $\mathbf{r}_T(t)$:**
  The third component is constant: $Z_T = \frac{b}{c}$.
  The first two components satisfy:
  $$X_T^2 + Y_T^2 = \left( -\frac{a}{c} \sin t \right)^2 + \left( \frac{a}{c} \cos t \right)^2 = \frac{a^2}{c^2} (\sin^2 t + \cos^2 t) = \frac{a^2}{c^2}$$
  Thus, $\mathbf{r}_T(t)$ is the intersection of the unit sphere $S^2$ ($X^2 + Y^2 + Z^2 = 1$) with the horizontal plane $Z = \frac{b}{c}$.
  This intersection is a **circle** of radius $R_T = \frac{a}{c} = \frac{a}{\sqrt{a^2 + b^2}}$.

- **Binormal Indicatrix $\mathbf{r}_B(t)$:**
  The third component is constant: $Z_B = \frac{a}{c}$.
  The first two components satisfy:
  $$X_B^2 + Y_B^2 = \left( \frac{b}{c} \sin t \right)^2 + \left( -\frac{b}{c} \cos t \right)^2 = \frac{b^2}{c^2} = \frac{b^2}{a^2 + b^2}$$
  Thus, $\mathbf{r}_B(t)$ is a **circle** of radius $R_B = \frac{b}{c} = \frac{b}{\sqrt{a^2 + b^2}}$ in the plane $Z = \frac{a}{c}$. $\blacksquare$

---

### 3. Radius and Perimeter over One Full Turn
Over $t \in [0, 2\pi]$:
- For the tangent indicatrix:
  $$\text{Radius } R_T = \frac{a}{\sqrt{a^2 + b^2}}$$
  $$\text{Perimeter } L_T = 2\pi R_T = \frac{2\pi a}{\sqrt{a^2 + b^2}} = 2\pi a \kappa$$
- For the binormal indicatrix:
  $$\text{Radius } R_B = \frac{b}{\sqrt{a^2 + b^2}}$$
  $$\text{Perimeter } L_B = 2\pi R_B = \frac{2\pi b}{\sqrt{a^2 + b^2}} = 2\pi b \tau \quad \blacksquare$$"""
            },
            {
                "tier": "Advanced / Problem 3.2",
                "title": "Complete Deductive Chain of Lancret's Theorem for General Helices",
                "statement": r"""Provide a complete, self-contained proof of Lancret's Theorem:
A space curve $\mathbf{r}(s)$ of class $C^3$ with $\kappa(s) > 0$ has the property that its tangent vector makes a constant angle with a fixed non-zero direction $\mathbf{u}$ if and only if $\tau(s) / \kappa(s) = \text{constant}$.
Also demonstrate that if $\tau / \kappa \equiv 0$, the curve is planar, and if both $\kappa$ and $\tau$ are non-zero constants, the curve is a circular helix.""",
                "hints": [
                    "Forward direction: differentiate T(s) . u = cos alpha to show N(s) . u = 0.",
                    "Express u = (cos alpha) T + (sin alpha) B and differentiate.",
                    "Reverse direction: set u(s) = (cos alpha) T(s) + (sin alpha) B(s) where cot alpha = c, and show u'(s) = 0."
                ],
                "solution": r"""### 1. Forward Direction
Let $\mathbf{u}$ be a constant unit vector such that $\mathbf{T}(s) \cdot \mathbf{u} = \cos \alpha$ for constant $\alpha \in (0, \pi/2)$.
Differentiating with respect to arc-length $s$:
$$\mathbf{T}'(s) \cdot \mathbf{u} = 0 \iff (\kappa(s) \mathbf{N}(s)) \cdot \mathbf{u} = 0$$
Since $\kappa(s) > 0$, we have:
$$\mathbf{N}(s) \cdot \mathbf{u} = 0 \quad \forall s$$
Since $\{\mathbf{T}, \mathbf{N}, \mathbf{B}\}$ is an orthonormal basis, $\mathbf{u}$ has zero component along $\mathbf{N}$.
Therefore, $\mathbf{u}$ lies in the plane of $\mathbf{T}$ and $\mathbf{B}$:
$$\mathbf{u} = (\mathbf{u} \cdot \mathbf{T}) \mathbf{T} + (\mathbf{u} \cdot \mathbf{B}) \mathbf{B}$$
Since $\|\mathbf{u}\| = 1$ and $\mathbf{u} \cdot \mathbf{T} = \cos \alpha$, we have $\mathbf{u} \cdot \mathbf{B} = \pm \sin \alpha$.
Choosing orientation so that $\mathbf{u} \cdot \mathbf{B} = \sin \alpha$:
$$\mathbf{u} = (\cos \alpha) \mathbf{T}(s) + (\sin \alpha) \mathbf{B}(s)$$
Since $\mathbf{u}$ is a constant vector:
$$\mathbf{0} = \frac{d\mathbf{u}}{ds} = (\cos \alpha) \mathbf{T}'(s) + (\sin \alpha) \mathbf{B}'(s)$$
Applying Frenet-Serret formulas $\mathbf{T}' = \kappa \mathbf{N}$ and $\mathbf{B}' = -\tau \mathbf{N}$:
$$\mathbf{0} = (\cos \alpha) \kappa(s) \mathbf{N}(s) - (\sin \alpha) \tau(s) \mathbf{N}(s) = [\kappa(s) \cos \alpha - \tau(s) \sin \alpha] \mathbf{N}(s)$$
Since $\|\mathbf{N}(s)\| = 1$:
$$\kappa(s) \cos \alpha - \tau(s) \sin \alpha = 0 \implies \frac{\tau(s)}{\kappa(s)} = \frac{\cos \alpha}{\sin \alpha} = \cot \alpha = \text{constant} \quad \blacksquare$$

---

### 2. Reverse Direction
Suppose $\frac{\tau(s)}{\kappa(s)} = c = \text{constant}$.
Define $\alpha \in (0, \pi/2)$ such that $\cot \alpha = c$.
Define the vector field:
$$\mathbf{u}(s) = (\cos \alpha) \mathbf{T}(s) + (\sin \alpha) \mathbf{B}(s)$$
Differentiating with respect to $s$:
$$\mathbf{u}'(s) = (\cos \alpha) \mathbf{T}'(s) + (\sin \alpha) \mathbf{B}'(s) = [(\cos \alpha) \kappa(s) - (\sin \alpha) \tau(s)] \mathbf{N}(s)$$
Since $\tau(s) = c \kappa(s) = (\cot \alpha) \kappa(s)$:
$$(\cos \alpha) \kappa(s) - (\sin \alpha) (\cot \alpha) \kappa(s) = \kappa(s) [\cos \alpha - \cos \alpha] = 0$$
Hence $\mathbf{u}'(s) = \mathbf{0}$, meaning $\mathbf{u}$ is a constant vector.
Its magnitude is $\|\mathbf{u}\|^2 = \cos^2 \alpha + \sin^2 \alpha = 1$.
Finally, $\mathbf{T}(s) \cdot \mathbf{u} = \cos \alpha = \text{constant}$.
Thus the curve is a general helix. $\blacksquare$

---

### 3. Limiting Cases
- **If $\tau / \kappa \equiv 0$:** Since $\kappa > 0$, this requires $\tau(s) \equiv 0$.
  By Problem 2.2, a curve with $\tau \equiv 0$ lies entirely in a plane. Thus planar curves are degenerate helices with $\alpha = \pi/2$.
- **If $\kappa = \text{const}$ and $\tau = \text{const} \ne 0$:**
  By Theorem 3.2, the curve is a circular helix. $\blacksquare$"""
            },
            {
                "tier": "Honors / Problem 3.3",
                "title": "Comprehensive Proof of the Bertrand Curve Characterization Theorem",
                "statement": r"""Prove the Bertrand Curve Characterization Theorem:
A regular space curve $\mathbf{r}(s)$ of class $C^3$ with $\kappa(s) > 0$ and $\tau(s) \ne 0$ has a Bertrand mate $\mathbf{r}^*(s)$ if and only if there exist real constants $a \ne 0$ and $b$ such that:
$$a \kappa(s) + b \tau(s) = 1 \quad \forall s \in I$$
Furthermore, prove that:
1. The distance between corresponding points of a Bertrand curve and its mate is constant ($a = \text{const}$).
2. The angle $\alpha$ between their corresponding unit tangent vectors $\mathbf{T}$ and $\mathbf{T}^*$ is constant.
3. The product of the torsions of a Bertrand curve and its mate satisfies $\tau(s) \tau^*(s^*) = \frac{\sin^2 \alpha}{a^2} = \text{constant}$.""",
                "hints": [
                    "Write r*(s) = r(s) + a(s) N(s).",
                    "Differentiate and use the fact that N*(s) is parallel to N(s) and orthogonal to T*(s).",
                    "Show a'(s) = 0 and (1 - a kappa) T + a tau B is collinear with T*."
                ],
                "solution": r"""### 1. Proof that Distance $a$ is Constant
Let $\mathbf{r}^*(s^*)$ be a Bertrand mate of $\mathbf{r}(s)$.
Since their principal normals coincide at corresponding points:
$$\mathbf{r}^*(s) = \mathbf{r}(s) + a(s) \mathbf{N}(s)$$
for some scalar function $a(s) \ne 0$.
Differentiating with respect to $s$:
$$\frac{d\mathbf{r}^*}{ds} = \mathbf{T}(s) + a'(s) \mathbf{N}(s) + a(s) [-\kappa(s) \mathbf{T}(s) + \tau(s) \mathbf{B}(s)] = (1 - a\kappa) \mathbf{T} + a' \mathbf{N} + a\tau \mathbf{B}$$
Let $\mathbf{T}^*$ and $\mathbf{N}^*$ be the unit tangent and principal normal of $\mathbf{r}^*$.
By definition of Bertrand mates, $\mathbf{N}^*(s^*) = \pm \mathbf{N}(s)$.
Since $\mathbf{T}^* \perp \mathbf{N}^*$, we must have $\frac{d\mathbf{r}^*}{ds} \perp \mathbf{N}(s)$:
$$\frac{d\mathbf{r}^*}{ds} \cdot \mathbf{N}(s) = 0 \iff a'(s) = 0$$
Therefore, $a(s) = a = \text{constant}$! $\blacksquare$

---

### 2. Proof of Constant Angle $\alpha$ and the Linear Relation
Since $a' = 0$:
$$\frac{d\mathbf{r}^*}{ds} = (1 - a\kappa) \mathbf{T} + a\tau \mathbf{B}$$
Since $\frac{d\mathbf{r}^*}{ds} = \frac{ds^*}{ds} \mathbf{T}^*$, $\mathbf{T}^*$ lies in the span of $\mathbf{T}$ and $\mathbf{B}$.
Let $\alpha(s)$ be the angle between $\mathbf{T}^*$ and $\mathbf{T}$:
$$\mathbf{T}^* = (\cos \alpha) \mathbf{T} + (\sin \alpha) \mathbf{B}$$
Differentiating with respect to $s$:
$$\frac{d\mathbf{T}^*}{ds} = \frac{d\mathbf{T}^*}{ds^*} \frac{ds^*}{ds} = \kappa^* \mathbf{N}^* \frac{ds^*}{ds}$$
Since $\mathbf{N}^* = \pm \mathbf{N}$, $\frac{d\mathbf{T}^*}{ds}$ is entirely parallel to $\mathbf{N}$.
Computing $\frac{d\mathbf{T}^*}{ds}$ from $(\cos \alpha) \mathbf{T} + (\sin \alpha) \mathbf{B}$:
$$\frac{d\mathbf{T}^*}{ds} = (-\alpha' \sin \alpha) \mathbf{T} + (\cos \alpha) \kappa \mathbf{N} + (\alpha' \cos \alpha) \mathbf{B} - (\sin \alpha) \tau \mathbf{N}$$
$$= (-\alpha' \sin \alpha) \mathbf{T} + (\kappa \cos \alpha - \tau \sin \alpha) \mathbf{N} + (\alpha' \cos \alpha) \mathbf{B}$$
For this vector to be parallel to $\mathbf{N}$, the components along $\mathbf{T}$ and $\mathbf{B}$ must vanish:
$$-\alpha' \sin \alpha = 0 \quad \text{and} \quad \alpha' \cos \alpha = 0 \implies \alpha'(s) = 0$$
Thus the angle $\alpha$ is **strictly constant**!
Now equating components in $\frac{ds^*}{ds} \mathbf{T}^* = (1 - a\kappa) \mathbf{T} + a\tau \mathbf{B}$:
$$\frac{ds^*}{ds} \cos \alpha = 1 - a\kappa(s) \quad \text{and} \quad \frac{ds^*}{ds} \sin \alpha = a\tau(s)$$
Dividing the two equations:
$$\tan \alpha = \frac{a\tau(s)}{1 - a\kappa(s)} \iff 1 - a\kappa(s) = a\tau(s) \cot \alpha \iff a\kappa(s) + (a\cot\alpha)\tau(s) = 1$$
Setting $b = a\cot\alpha$ establishes the linear relation:
$$a\kappa(s) + b\tau(s) = 1 \quad \blacksquare$$

---

### 3. Torsion Product Relation
From the dual relation on the Bertrand mate $\mathbf{r}^*(s^*)$, $\mathbf{r}(s) = \mathbf{r}^*(s^*) - a \mathbf{N}^*(s^*)$.
The same analysis applied in reverse yields:
$$-a \kappa^*(s^*) + (a \cot \alpha) \tau^*(s^*) = 1$$
and $\frac{ds}{ds^*} \sin(-\alpha) = -a \tau^*(s^*) \implies \frac{ds}{ds^*} \sin \alpha = a \tau^*(s^*)$.
Multiplying the two differential relations:
$$\left( \frac{ds^*}{ds} \sin \alpha \right) \left( \frac{ds}{ds^*} \sin \alpha \right) = (a\tau(s)) (a\tau^*(s^*))$$
$$\sin^2 \alpha = a^2 \tau(s) \tau^*(s^*) \iff \tau(s) \tau^*(s^*) = \frac{\sin^2 \alpha}{a^2} = \text{constant} \quad \blacksquare$$"""
            }
        ]
    }
    return u3

if __name__ == "__main__":
    u = get_unit3()
    print(f"Loaded Unit 3: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
