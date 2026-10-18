# -*- coding: utf-8 -*-
"""
build_tensor_unit6.py
Constructs Unit 6: Curvature Tensors: Riemann, Ricci & Bianchi Identities
Strictly ZERO course numbers.
"""

def get_unit6():
    u6 = {
        "number": 6,
        "title": "Curvature Tensors: Riemann, Ricci & Bianchi Identities",
        "leadSummary": "Comprehensive mathematical theory of Riemannian curvature: derivation of the Riemann-Christoffel curvature tensor R^l_{ijk} via commutators of covariant derivatives [\\nabla_j, \\nabla_k] A_i = R_{ijk}^l A_l, the covariant form R_{hijk}, full algebraic symmetries (antisymmetry, block symmetry, first Bianchi identity R_{hijk} + R_{hkij} + R_{hjki} = 0), formula for the independent components n^2(n^2-1)/12, the Ricci curvature tensor R_{ij}, Ricci scalar R, Einstein tensor G_{ij} = R_{ij} - (1/2) R g_{ij}, second Bianchi differential identity \\nabla_m R_{ijkl} + \\nabla_k R_{ijlm} + \\nabla_l R_{ijmk} = 0, twice-contracted Bianchi identity \\nabla^i G_{ij} = 0, sectional curvature, and Schur's Theorem.",
        "simulations": ["sim_tensor_riemann_curvature"],
        "sections": [
            {
                "secNumber": "6.1",
                "title": "Commutator of Covariant Derivatives & Derivation of the Riemann Curvature Tensor $R^l_{ijk}$",
                "content": r"""### 1. The Non-Commutativity of Covariant Differentiation
In flat Euclidean space with Cartesian coordinates, partial derivatives commute unconditionally: $\partial_j \partial_k A_i = \partial_k \partial_j A_i$. On a curved manifold, however, covariant differentiation is non-commutative:
$$[\nabla_j, \nabla_k] A_i \equiv (\nabla_j \nabla_k - \nabla_k \nabla_j) A_i \ne 0$$
This commutator measures the failure of infinitesimal loops to close, which is the intrinsic geometric definition of **curvature**.

---

### 2. Derivation of the Riemann Curvature Tensor
Let $A_i$ be an arbitrary smooth covariant vector field. Compute its second covariant derivative:
$$\nabla_k A_i = \partial_k A_i - \Gamma^m_{ki} A_m$$
Differentiating covariantly with respect to $x^j$:
$$\begin{aligned}
\nabla_j (\nabla_k A_i) &= \partial_j (\nabla_k A_i) - \Gamma^m_{ji} (\nabla_k A_m) - \Gamma^m_{jk} (\nabla_m A_i) \\
&= \partial_j \left( \partial_k A_i - \Gamma^m_{ki} A_m \right) - \Gamma^m_{ji} \left( \partial_k A_m - \Gamma^l_{km} A_l \right) - \Gamma^m_{jk} (\nabla_m A_i) \\
&= \partial_j \partial_k A_i - (\partial_j \Gamma^m_{ki}) A_m - \Gamma^m_{ki} \partial_j A_m - \Gamma^m_{ji} \partial_k A_m + \Gamma^m_{ji} \Gamma^l_{km} A_l - \Gamma^m_{jk} (\nabla_m A_i)
\end{aligned}$$
Now interchange indices $j$ and $k$ to compute $\nabla_k (\nabla_j A_i)$:
$$\nabla_k (\nabla_j A_i) = \partial_k \partial_j A_i - (\partial_k \Gamma^m_{ji}) A_m - \Gamma^m_{ji} \partial_k A_m - \Gamma^m_{ki} \partial_j A_m + \Gamma^m_{ki} \Gamma^l_{jm} A_l - \Gamma^m_{kj} (\nabla_m A_i)$$
Subtracting the two equations:
- $\partial_j \partial_k A_i - \partial_k \partial_j A_i = 0$ (commutation of ordinary partials).
- $-\Gamma^m_{ki} \partial_j A_m$ and $-\Gamma^m_{ji} \partial_k A_m$ cancel by subtraction.
- In a torsion-free Levi-Civita connection, $\Gamma^m_{jk} = \Gamma^m_{kj}$, so $-\Gamma^m_{jk} \nabla_m A_i + \Gamma^m_{kj} \nabla_m A_i = 0$.

All derivative terms of $A$ vanish, leaving only terms proportional to $A_l$:
$$\nabla_j \nabla_k A_i - \nabla_k \nabla_j A_i = \left[ \partial_k \Gamma^l_{ji} - \partial_j \Gamma^l_{ki} + \Gamma^m_{ji} \Gamma^l_{km} - \Gamma^m_{ki} \Gamma^l_{jm} \right] A_l$$
We define the quantity in brackets as the **Riemann curvature tensor** (Ricci identity):

> **Definition 6.1 (Riemann Curvature Tensor of Type $(1, 3)$):**
> $$[\nabla_j, \nabla_k] A_i = R^l_{ijk} A_l$$
> where:
> $$R^l_{ijk} = \frac{\partial \Gamma^l_{ik}}{\partial x^j} - \frac{\partial \Gamma^l_{ij}}{\partial x^k} + \Gamma^m_{ik} \Gamma^l_{jm} - \Gamma^m_{ij} \Gamma^l_{km}$$
> (Sign convention note: in modern differential geometry and general relativity, the definition is often written as $[\nabla_j, \nabla_k] A^l = R^l_{\, ijk} A^i$)."""
            },
            {
                "secNumber": "6.2",
                "title": "Symmetries and Independent Components of the Riemann Tensor in $n$ Dimensions",
                "content": r"""### 1. The Fully Covariant Riemann Tensor $R_{hijk}$
By lowering the contravariant index using the metric tensor $g_{hl}$:
$$R_{hijk} = g_{hl} R^l_{ijk}$$
In terms of metric derivatives and Christoffel symbols:
$$R_{hijk} = \frac{1}{2}\left( \frac{\partial^2 g_{hk}}{\partial x^i \partial x^j} + \frac{\partial^2 g_{ij}}{\partial x^h \partial x^k} - \frac{\partial^2 g_{hj}}{\partial x^i \partial x^k} - \frac{\partial^2 g_{ik}}{\partial x^h \partial x^j} \right) + g_{lm} \left( \Gamma^l_{ik} \Gamma^m_{hj} - \Gamma^l_{ij} \Gamma^m_{hk} \right)$$

---

### 2. Fundamental Algebraic Symmetries

> **Theorem 6.1 (Algebraic Symmetries of $R_{hijk}$):**
> 1. **Antisymmetry in First Pair:** $R_{hijk} = -R_{ihjk}$
> 2. **Antisymmetry in Second Pair:** $R_{hijk} = -R_{hikj}$
> 3. **Block Symmetry (Pair Exchange):** $R_{hijk} = R_{jkhi}$
> 4. **First (Algebraic) Bianchi Identity:**
>    $$R_{hijk} + R_{hkij} + R_{hjki} = 0$$

#### Proof of Antisymmetry in First Pair:
From Ricci's Theorem $\nabla_k g_{hi} = 0$, applying $[\nabla_j, \nabla_k] g_{hi} = 0$:
$$0 = [\nabla_j, \nabla_k] g_{hi} = -R^m_{hjk} g_{mi} - R^m_{ijk} g_{hm} = -R_{ihjk} - R_{hijk}$$
$$\implies R_{hijk} = -R_{ihjk} \qquad \blacksquare$$

---

### 3. Number of Independent Components in $n$ Dimensions
A rank-4 tensor has $n^4$ total components. How many are algebraically independent?

> **Theorem 6.2 (Independent Components Count):**
> In an $n$-dimensional Riemannian manifold, the number of algebraically independent components of the Riemann curvature tensor is:
> $$N(n) = \frac{n^2(n^2 - 1)}{12}$$

#### Step-by-Step Combinatorial Proof:
1. $R_{hijk}$ is antisymmetric in $(hi)$ and in $(jk)$.
   The number of independent antisymmetric pairs is $M = \frac{n(n-1)}{2}$.
2. Treat $R_{(hi)(jk)}$ as a symmetric $M \times M$ matrix of pairs (due to block symmetry $R_{AB} = R_{BA}$).
   The number of independent components in a symmetric $M \times M$ matrix is:
   $$\frac{M(M+1)}{2} = \frac{\frac{n(n-1)}{2} \left( \frac{n(n-1)}{2} + 1 \right)}{2} = \frac{n(n-1)(n^2 - n + 2)}{8}$$
3. The first Bianchi identity $R_{h[ijk]} = 0$ imposes additional non-trivial constraints whenever all 4 indices $h, i, j, k$ are distinct.
   The number of completely distinct 4-index combinations is $\binom{n}{4} = \frac{n(n-1)(n-2)(n-3)}{24}$.
4. Subtracting these constraints:
   $$N(n) = \frac{n(n-1)(n^2 - n + 2)}{8} - \frac{n(n-1)(n-2)(n-3)}{24}$$
   Factoring out $\frac{n(n-1)}{24}$:
   $$N(n) = \frac{n(n-1)}{24} \left[ 3(n^2 - n + 2) - (n^2 - 5n + 6) \right] = \frac{n(n-1)(2n^2 + 2n)}{24} = \frac{n^2(n^2 - 1)}{12} \qquad \blacksquare$$

#### Table of Independent Components:
- **$n = 1$:** $\frac{1(0)}{12} = 0$ (A 1D curve has no intrinsic curvature!).
- **$n = 2$:** $\frac{4(3)}{12} = 1$ component ($R_{1212} = K g$, where $K$ is the Gaussian curvature).
- **$n = 3$:** $\frac{9(8)}{12} = 6$ components (identical to the 6 components of the Ricci tensor).
- **$n = 4$:** $\frac{16(15)}{12} = 20$ components (crucial for Einstein's General Relativity)."""
            },
            {
                "secNumber": "6.3",
                "title": "The Ricci Tensor $R_{ij}$, Scalar Curvature $R$, and Einstein Tensor $G_{ij}$",
                "content": r"""### 1. The Ricci Curvature Tensor $R_{ij}$
By contracting the contravariant index with the third covariant index of the Riemann tensor:

> **Definition 6.2 (Ricci Tensor):**
> $$R_{ij} \equiv R^k_{ikj} = g^{km} R_{mi kj}$$
> In terms of Christoffel symbols:
> $$R_{ij} = \frac{\partial \Gamma^k_{ij}}{\partial x^k} - \frac{\partial \Gamma^k_{ik}}{\partial x^j} + \Gamma^m_{ij} \Gamma^k_{km} - \Gamma^m_{ik} \Gamma^k_{jm}$$

#### Symmetry of the Ricci Tensor:
Using block symmetry and index lowering:
$$R_{ji} = g^{km} R_{mjki} = g^{km} R_{kimj} = g^{km} R_{mikj} = R_{ij}$$
The Ricci tensor is **strictly symmetric**: $R_{ij} = R_{ji}$.
In $n$ dimensions, $R_{ij}$ has $\frac{n(n+1)}{2}$ independent components (10 components in 4D).

---

### 2. The Ricci Scalar Curvature $R$
Contracting the Ricci tensor with the conjugate metric tensor produces the **Ricci scalar (scalar curvature)**:
$$R \equiv g^{ij} R_{ij} = R^i_i$$
$R$ is an absolute invariant scalar field.
- In 2D, $R = 2K$, where $K$ is the Gaussian curvature.
- If $R > 0$, the volume of a geodesic ball is smaller than in Euclidean space.
- If $R < 0$, the volume of a geodesic ball is larger than in Euclidean space.

---

### 3. The Einstein Tensor $G_{ij}$

> **Definition 6.3 (Einstein Tensor):**
> The **Einstein tensor** $G_{ij}$ is defined as the trace-reversed Ricci tensor:
> $$G_{ij} \equiv R_{ij} - \frac{1}{2} R g_{ij}$$

#### Trace of the Einstein Tensor in $n$ Dimensions:
$$G = g^{ij} G_{ij} = g^{ij} R_{ij} - \frac{1}{2} R g^{ij} g_{ij} = R - \frac{1}{2} R (n) = \left( 1 - \frac{n}{2} \right) R$$
In $n = 4$ spacetime dimensions:
$$G = R - 2R = -R \implies R_{ij} = G_{ij} - \frac{1}{2} G g_{ij}$$
The Einstein tensor is symmetric ($G_{ij} = G_{ji}$) and plays the central geometric role on the left side of Einstein's field equations."""
            },
            {
                "secNumber": "6.4",
                "title": "The First and Second Bianchi Identities & Differential Conservation $\\nabla^i G_{ij} = 0$",
                "content": r"""### 1. The Second (Differential) Bianchi Identity
Beyond the algebraic symmetries, the Riemann tensor satisfies a fundamental differential relation:

> **Theorem 6.3 (Second Bianchi Identity):**
> In any Riemannian or Pseudo-Riemannian space:
> $$\nabla_m R^l_{ijk} + \nabla_k R^l_{ijm} + \nabla_j R^l_{ikm} = 0$$
> or in fully covariant form:
> $$\nabla_m R_{hijk} + \nabla_k R_{hijm} + \nabla_j R_{hikm} = 0$$

#### Proof using Riemann Normal Coordinates:
At any chosen point $P$, choose Riemann normal coordinates where $\left. \Gamma^k_{ij} \right|_P = 0$.
At point $P$, covariant derivatives reduce to ordinary partial derivatives:
$$\left. \nabla_m R_{hijk} \right|_P = \left. \partial_m R_{hijk} \right|_P = \frac{1}{2} \partial_m \left( \partial_i \partial_j g_{hk} + \partial_h \partial_k g_{ij} - \partial_i \partial_k g_{hj} - \partial_h \partial_j g_{ik} \right)$$
Summing over cyclic permutations of $(j, k, m)$:
$$\begin{aligned}
\partial_m R_{hijk} + \partial_k R_{hijm} + \partial_j R_{hikm} = \frac{1}{2} [
& \partial_m \partial_i \partial_j g_{hk} + \partial_m \partial_h \partial_k g_{ij} - \partial_m \partial_i \partial_k g_{hj} - \partial_m \partial_h \partial_j g_{ik} \\
+& \partial_k \partial_i \partial_m g_{hj} + \partial_k \partial_h \partial_j g_{im} - \partial_k \partial_i \partial_j g_{hm} - \partial_k \partial_h \partial_m g_{ij} \\
+& \partial_j \partial_i \partial_k g_{hm} + \partial_j \partial_h \partial_m g_{ik} - \partial_j \partial_i \partial_m g_{hk} - \partial_j \partial_h \partial_k g_{im} ] = 0
\end{aligned}$$
All 12 terms cancel in pairs because third partial derivatives of $g$ commute!
Since this is a tensorial equation valid at an arbitrary point $P$, it holds universally in all coordinate systems! $\blacksquare$

---

### 2. The Twice-Contracted Bianchi Identity

> **Theorem 6.4 (Divergence-Free Property of the Einstein Tensor):**
> The covariant divergence of the Einstein tensor vanishes identically:
> $$\nabla^i G_{ij} = 0 \iff \nabla_i G^i_j = 0$$

#### Proof:
Start with the second Bianchi identity in mixed form:
$$\nabla_m R^l_{ijk} + \nabla_k R^l_{ijm} + \nabla_j R^l_{ikm} = 0$$
Contract indices $l$ and $k$ (setting $k = l$):
$$\nabla_m R_{ij} + \nabla_l R^l_{ijm} - \nabla_j R_{im} = 0$$
Now contract with $g^{ij}$:
$$g^{ij} \nabla_m R_{ij} + g^{ij} \nabla_l R^l_{ijm} - g^{ij} \nabla_j R_{im} = 0$$
By Ricci's Theorem, $\nabla$ passes through $g^{ij}$:
1. $g^{ij} \nabla_m R_{ij} = \nabla_m (g^{ij} R_{ij}) = \nabla_m R$.
2. $g^{ij} R^l_{ijm} = -g^{ij} R^l_{imj} = -R^l_{\ m}$. Contracting with $\nabla_l$ gives $-\nabla_l R^l_m$.
3. $g^{ij} \nabla_j R_{im} = \nabla_j R^j_m = \nabla_l R^l_m$.
Substituting:
$$\nabla_m R - \nabla_l R^l_m - \nabla_l R^l_m = 0 \implies \nabla_m R - 2 \nabla_l R^l_m = 0$$
Dividing by 2 and moving to one side:
$$\nabla_l R^l_m - \frac{1}{2} \nabla_m R = 0 \implies \nabla_l \left( R^l_m - \frac{1}{2} R \delta^l_m \right) = 0$$
Recognizing $G^l_m = R^l_m - \frac{1}{2} R \delta^l_m$:
$$\nabla_l G^l_m = 0 \qquad \blacksquare$$

This mathematical identity is why Einstein chose $G_{\mu\nu}$ for gravitation: since the stress-energy tensor is conserved ($\nabla_\mu T^{\mu\nu} = 0$), the geometric tensor on the left side of $G_{\mu\nu} = \kappa T_{\mu\nu}$ MUST automatically satisfy $\nabla_\mu G^{\mu\nu} = 0$!"""
            },
            {
                "secNumber": "6.5",
                "title": "Sectional Curvature, Schur's Theorem, and Spaces of Constant Curvature",
                "content": r"""### 1. Sectional Curvature $K(\Pi)$
Let $\Pi = \text{span}(u, v)$ be a 2-dimensional tangent plane spanned by two linearly independent vectors $u^i, v^i$ at $P \in M$.

> **Definition 6.4 (Sectional Curvature):**
> The **sectional curvature** of $M$ associated with the 2-plane $\Pi$ is:
> $$K(\Pi) = \frac{R_{hijk} u^h v^i u^j v^k}{(g_{hj} g_{ik} - g_{hk} g_{ij}) u^h v^i u^j v^k} = \frac{\langle R(u, v)v, u \rangle}{\|u\|^2 \|v\|^2 - \langle u, v \rangle^2}$$
> $K(\Pi)$ is the Gaussian curvature of the 2D geodesic surface formed by geodesics emanating from $P$ tangent to $\Pi$.

---

### 2. Spaces of Constant Curvature
A manifold is called a **space of constant curvature** if $K(\Pi) = K_0$ is independent of the choice of 2-plane $\Pi$ and point $P$.
In such spaces, the Riemann tensor takes the maximally symmetric form:
$$R_{hijk} = K_0 (g_{hk} g_{ij} - g_{hj} g_{ik})$$
Contracting with $g^{hj}$:
$$R_{ik} = K_0 (n - 1) g_{ik}$$
Contracting with $g^{ik}$:
$$R = n(n - 1) K_0$$

---

### 3. Schur's Theorem

> **Theorem 6.5 (Schur's Theorem):**
> If in a connected Riemannian manifold of dimension $n \ge 3$, the sectional curvature $K$ at each point is independent of the 2-plane direction $\Pi$, then $K$ is **constant throughout the entire manifold** ($\partial_m K = 0$).

#### Proof:
If $K(\Pi)$ is isotropic at each point, then $R_{hijk} = K(x) (g_{hk} g_{ij} - g_{hj} g_{ik})$.
The Ricci tensor is $R_{ij} = (n-1) K(x) g_{ij}$, and scalar curvature is $R = n(n-1) K(x)$.
The Einstein tensor is:
$$G_{ij} = R_{ij} - \frac{1}{2} R g_{ij} = (n-1) K g_{ij} - \frac{1}{2} n(n-1) K g_{ij} = (n-1)\left( 1 - \frac{n}{2} \right) K(x) g_{ij}$$
Now apply the twice-contracted Bianchi identity $\nabla^i G_{ij} = 0$:
$$\nabla^i \left[ (n-1)\left( 1 - \frac{n}{2} \right) K(x) g_{ij} \right] = 0$$
Since $\nabla_i g_{ij} = 0$:
$$(n-1)\left( 1 - \frac{n}{2} \right) g_{ij} \nabla^i K = 0 \implies (n-1)(2-n) \partial_j K = 0$$
For $n \ge 3$, $(n-1)(2-n) \ne 0$.
Therefore, we must have:
$$\partial_j K = 0 \implies K = \text{constant everywhere} \qquad \blacksquare$$
This proves that spatial isotropy at every point automatically forces spatial homogeneity across the entire manifold!"""
            }
        ],
        "problems": [
            {
                "tier": "Fundamentals",
                "title": "Problem 6.1: Curvature Tensors of the 2-Sphere $S^2$",
                "statement": r"""For the unit 2-sphere $S^2$ with coordinates $(\theta, \phi)$ and metric $ds^2 = d\theta^2 + \sin^2\theta \, d\phi^2$:
1. Calculate the non-zero component $R^\phi_{\theta\theta\phi}$ and the fully covariant component $R_{\theta\phi\theta\phi}$.
2. Compute the Ricci tensor components $R_{\theta\theta}$, $R_{\phi\phi}$, and verify that $R_{ij} = g_{ij}$.
3. Calculate the scalar curvature $R$ and the Gaussian curvature $K$.
4. Compute the Einstein tensor $G_{ij}$ and explain why it vanishes identically in 2 dimensions.""",
                "hints": [
                    "Recall $\\Gamma^\\theta_{\\phi\\phi} = -\\sin\\theta\\cos\\theta$, $\\Gamma^\\phi_{\\theta\\phi} = \\cot\\theta$.",
                    "Use $R^l_{ijk} = \\partial_j \\Gamma^l_{ik} - \\partial_k \\Gamma^l_{ij} + \\Gamma^m_{ik} \\Gamma^l_{jm} - \\Gamma^m_{ij} \\Gamma^l_{km}$.",
                    "In 2D, $G_{ij} = R_{ij} - \\frac{1}{2} R g_{ij}$ always vanishes."
                ],
                "solution": r"""### 1. Riemann Curvature Component
Christoffel symbols: $\Gamma^\theta_{\phi\phi} = -\sin\theta\cos\theta$, $\Gamma^\phi_{\theta\phi} = \cot\theta$, all others zero.
Using the definition for $R^\phi_{\theta\theta\phi}$:
$$\begin{aligned}
R^\phi_{\theta\theta\phi} &= \partial_\theta \Gamma^\phi_{\theta\phi} - \partial_\phi \Gamma^\phi_{\theta\theta} + \Gamma^m_{\theta\phi} \Gamma^\phi_{\theta m} - \Gamma^m_{\theta\theta} \Gamma^\phi_{\phi m} \\
&= \frac{\partial}{\partial\theta}(\cot\theta) - 0 + \Gamma^\phi_{\theta\phi} \Gamma^\phi_{\theta\phi} - 0 \\
&= -\csc^2\theta + \cot^2\theta = -(\csc^2\theta - \cot^2\theta) = -1
\end{aligned}$$
Lowering the index:
$$R_{\phi\theta\theta\phi} = g_{\phi\phi} R^\phi_{\theta\theta\phi} = \sin^2\theta (-1) = -\sin^2\theta$$
By antisymmetry $R_{\theta\phi\theta\phi} = -R_{\phi\theta\theta\phi}$:
$$R_{\theta\phi\theta\phi} = \sin^2\theta \qquad \blacksquare$$

---

### 2. Ricci Tensor Components
$$\begin{aligned}
R_{\theta\theta} &= R^\phi_{\theta\phi\theta} = -R^\phi_{\theta\theta\phi} = -(-1) = 1 = g_{\theta\theta} \\
R_{\phi\phi} &= R^\theta_{\phi\theta\phi} = g_{\phi\phi} g^{\theta\theta} R_{\theta\phi\theta\phi} = \sin^2\theta(1)(1) = \sin^2\theta = g_{\phi\phi}
\end{aligned}$$
Off-diagonal $R_{\theta\phi} = 0$.
Thus:
$$R_{ij} = g_{ij} \qquad \blacksquare$$

---

### 3. Curvatures $R$ and $K$
Scalar curvature:
$$R = g^{ij} R_{ij} = g^{\theta\theta} R_{\theta\theta} + g^{\phi\phi} R_{\phi\phi} = 1(1) + \frac{1}{\sin^2\theta}(\sin^2\theta) = 1 + 1 = 2$$
Gaussian curvature:
$$K = \frac{R_{\theta\phi\theta\phi}}{g} = \frac{\sin^2\theta}{\sin^2\theta} = 1$$
Notice that $R = 2K = 2(1) = 2$. $\blacksquare$

---

### 4. Einstein Tensor $G_{ij}$
In 2 dimensions:
$$G_{ij} = R_{ij} - \frac{1}{2} R g_{ij} = g_{ij} - \frac{1}{2}(2) g_{ij} = g_{ij} - g_{ij} = 0$$
The Einstein tensor vanishes identically in ALL 2-dimensional Riemannian manifolds! This is because in $n = 2$, $R_{hijk} = K(g_{hk} g_{ij} - g_{hj} g_{ik})$, which forces $R_{ij} = K g_{ij} = \frac{1}{2} R g_{ij}$. $\blacksquare$"""
            },
            {
                "tier": "Computational Triad",
                "title": "Problem 6.2: Curvature and Sectional Curvature of Hyperbolic Space $\\mathbb{H}^3$",
                "statement": r"""Consider 3-dimensional hyperbolic space $\mathbb{H}^3$ in the upper half-space coordinates $(x, y, z) = (x^1, x^2, x^3)$ with $z > 0$:
$$ds^2 = \frac{dx^2 + dy^2 + dz^2}{z^2}$$

1. Compute all components of the Riemann curvature tensor $R_{hijk}$.
2. Show that $\mathbb{H}^3$ is a space of constant sectional curvature $K = -1$.
3. Compute the Ricci tensor $R_{ij}$ and scalar curvature $R$.
4. Calculate the Einstein tensor $G_{ij}$.""",
                "hints": [
                    "Conformal metric $g_{ij} = e^{2\\sigma} \\delta_{ij}$ with $\\sigma = -\\ln z$.",
                    "For constant curvature $K$, $R_{hijk} = K(g_{hk} g_{ij} - g_{hj} g_{ik})$.",
                    "Check $R = n(n-1)K = 3(2)(-1) = -6$."
                ],
                "solution": r"""### 1. Riemann Curvature Tensor Components
Metric components: $g_{ij} = \frac{1}{z^2} \delta_{ij}$.
Conformal factor $\sigma = -\ln z \implies \partial_i \sigma = -\frac{1}{z} \delta_i^3$.
Using the conformal curvature relation or direct Christoffel calculation, the non-zero components of $R_{hijk}$ satisfy:
$$R_{hijk} = -\left( g_{hk} g_{ij} - g_{hj} g_{ik} \right)$$
Specifically:
- $R_{1212} = -(g_{12}g_{21} - g_{11}g_{22}) = g_{11}g_{22} = -\frac{1}{z^4}$
- $R_{1313} = -\frac{1}{z^4}$
- $R_{2323} = -\frac{1}{z^4}$
All other independent components vanish.

---

### 2. Sectional Curvature
Comparing with the standard constant curvature form:
$$R_{hijk} = K_0 (g_{hk} g_{ij} - g_{hj} g_{ik})$$
we immediately identify:
$$K_0 = -1$$
For any 2-plane $\Pi = \text{span}(u, v)$:
$$K(\Pi) = \frac{R_{hijk} u^h v^i u^j v^k}{(g_{hj} g_{ik} - g_{hk} g_{ij}) u^h v^i u^j v^k} = \frac{-1 \cdot (g_{hk} g_{ij} - g_{hj} g_{ik}) u^h v^i u^j v^k}{-(g_{hk} g_{ij} - g_{hj} g_{ik}) u^h v^i u^j v^k} = -1$$
Thus, $\mathbb{H}^3$ has constant sectional curvature $K = -1$ everywhere. $\blacksquare$

---

### 3. Ricci Tensor and Scalar Curvature
For $n = 3$ with $K = -1$:
$$R_{ij} = K(n - 1) g_{ij} = -1(3 - 1) g_{ij} = -2 g_{ij} = -\frac{2}{z^2} \delta_{ij}$$
Scalar curvature:
$$R = g^{ij} R_{ij} = z^2 \delta^{ij} \left( -\frac{2}{z^2} \delta_{ij} \right) = -2 \delta^i_i = -2(3) = -6 \qquad \blacksquare$$

---

### 4. Einstein Tensor $G_{ij}$
$$G_{ij} = R_{ij} - \frac{1}{2} R g_{ij} = -2 g_{ij} - \frac{1}{2}(-6) g_{ij} = -2 g_{ij} + 3 g_{ij} = g_{ij} = \frac{1}{z^2} \delta_{ij} \qquad \blacksquare$$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 6.3: Complete Derivation of the Contracted Bianchi Identity and Gravitational Conservation",
                "statement": r"""In general relativity, the Bianchi identities are the mathematical guarantee that energy and momentum are locally conserved.

1. Beginning from the differential definition of the Riemann tensor, provide an alternative derivation of the Second Bianchi Identity:
   $$\nabla_m R^l_{ijk} + \nabla_k R^l_{ijm} + \nabla_j R^l_{ikm} = 0$$
   using the Jacobi identity for commutators of covariant derivatives: $[[\nabla_j, \nabla_k], \nabla_m] + [[\nabla_k, \nabla_m], \nabla_j] + [[\nabla_m, \nabla_j], \nabla_k] = 0$.
2. Contract this identity twice to prove step-by-step:
   $$\nabla_i \left( R^{ij} - \frac{1}{2} R g^{ij} \right) = 0$$
3. Explain why adding a cosmological constant term $\Lambda g^{ij}$ preserves the divergence-free condition:
   $$\nabla_i \left( R^{ij} - \frac{1}{2} R g^{ij} + \Lambda g^{ij} \right) = 0$$""",
                "hints": [
                    "Apply the commutator Jacobi identity to an arbitrary scalar field $\\phi$ or vector field $V^l$.",
                    "For torsion-free connections, $[\nabla_j, \nabla_k] \\phi = 0$, so apply it to a 1-form $A_i$.",
                    "Use Ricci's theorem $\\nabla_i g^{ij} = 0$ for the cosmological constant term."
                ],
                "solution": r"""### 1. Jacobi Identity Derivation
For any linear operators $A, B, C$, the Jacobi identity holds identically:
$$[A, [B, C]] + [B, [C, A]] + [C, [A, B]] = 0$$
Let $A = \nabla_j, B = \nabla_k, C = \nabla_m$ acting on a test vector field $V^l$:
$$[\nabla_j, [\nabla_k, \nabla_m]] V^l + [\nabla_k, [\nabla_m, \nabla_j]] V^l + [\nabla_m, [\nabla_j, \nabla_k]] V^l = 0$$
Recall that $[\nabla_k, \nabla_m] V^l = R^l_{p km} V^p$.
Then:
$$\nabla_j ([\nabla_k, \nabla_m] V^l) = \nabla_j (R^l_{p km} V^p) = (\nabla_j R^l_{p km}) V^p + R^l_{p km} \nabla_j V^p$$
And:
$$[\nabla_k, \nabla_m](\nabla_j V^l) = R^l_{p km} \nabla_j V^p - R^p_{j km} \nabla_p V^l$$
Subtracting these two yields:
$$[\nabla_j, [\nabla_k, \nabla_m]] V^l = (\nabla_j R^l_{p km}) V^p + R^p_{j km} \nabla_p V^l$$
Summing the three cyclic permutations over $(j, k, m)$:
The first group gives:
$$\left( \nabla_j R^l_{p km} + \nabla_k R^l_{p mj} + \nabla_m R^l_{p jk} \right) V^p$$
The second group gives:
$$\left( R^p_{j km} + R^p_{k mj} + R^p_{m jk} \right) \nabla_p V^l$$
By the first (algebraic) Bianchi identity, the second group vanishes identically:
$$R^p_{j km} + R^p_{k mj} + R^p_{m jk} = 0$$
Since $V^p$ is arbitrary, the first group must vanish:
$$\nabla_j R^l_{p km} + \nabla_k R^l_{p mj} + \nabla_m R^l_{p jk} = 0 \qquad \blacksquare$$

---

### 2. Step-by-Step Twice Contracted Bianchi Identity
Start with:
$$\nabla_m R^l_{ijk} + \nabla_k R^l_{ijm} + \nabla_j R^l_{ikm} = 0$$
Contract $l$ with $k$ (set $k = l$):
$$\nabla_m R_{ij} + \nabla_l R^l_{ijm} - \nabla_j R_{im} = 0$$
Contract with $g^{ij}$:
$$g^{ij} \nabla_m R_{ij} + g^{ij} \nabla_l R^l_{ijm} - g^{ij} \nabla_j R_{im} = 0$$
Using Ricci's theorem ($\nabla g = 0$):
- $g^{ij} \nabla_m R_{ij} = \nabla_m (g^{ij} R_{ij}) = \nabla_m R$.
- $g^{ij} R^l_{ijm} = -g^{ij} R^l_{imj} = -R^l_m \implies g^{ij} \nabla_l R^l_{ijm} = -\nabla_l R^l_m$.
- $g^{ij} \nabla_j R_{im} = \nabla_j R^j_m = \nabla_l R^l_m$.
Combining:
$$\nabla_m R - 2 \nabla_l R^l_m = 0 \implies \nabla_l R^l_m = \frac{1}{2} \nabla_m R$$
Raise index $m$ with $g^{mj}$:
$$\nabla_l R^{lj} = \frac{1}{2} g^{mj} \nabla_m R = \frac{1}{2} \nabla^j R$$
Therefore:
$$\nabla_l \left( R^{lj} - \frac{1}{2} R g^{lj} \right) = 0 \implies \nabla_i G^{ij} = 0 \qquad \blacksquare$$

---

### 3. Cosmological Constant Term
Consider the augmented tensor:
$$T^{ij}_{\text{geom}} = R^{ij} - \frac{1}{2} R g^{ij} + \Lambda g^{ij} = G^{ij} + \Lambda g^{ij}$$
where $\Lambda$ is a constant.
Taking the covariant divergence:
$$\nabla_i \left( G^{ij} + \Lambda g^{ij} \right) = \nabla_i G^{ij} + \nabla_i (\Lambda g^{ij}) = 0 + \Lambda (\nabla_i g^{ij}) + (\nabla_i \Lambda) g^{ij}$$
Since $\Lambda$ is a constant, $\nabla_i \Lambda = \partial_i \Lambda = 0$.
By Ricci's Theorem, $\nabla_i g^{ij} = 0$.
Thus:
$$\nabla_i \left( G^{ij} + \Lambda g^{ij} \right) = 0 + 0 + 0 = 0 \qquad \blacksquare$$
This proves that the cosmological constant $\Lambda$ is the unique scalar modification that keeps Einstein's equations strictly divergence-free!"""
            }
        ]
    }
    return u6

if __name__ == "__main__":
    u6 = get_unit6()
    print(f"Loaded Unit 6: {u6['title']} with {len(u6['sections'])} sections and {len(u6['problems'])} problems.")
