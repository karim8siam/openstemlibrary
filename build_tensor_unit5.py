# -*- coding: utf-8 -*-
"""
build_tensor_unit5.py
Constructs Unit 5: Covariant Differentiation & Ricci's Theorem
Strictly ZERO course numbers.
"""

def get_unit5():
    u5 = {
        "number": 5,
        "title": "Covariant Differentiation & Ricci's Theorem",
        "leadSummary": "Comprehensive mathematical theory of covariant differentiation on Riemannian and Pseudo-Riemannian manifolds: definition of covariant derivatives for contravariant and covariant vectors, general extension to type (r, s) tensor fields, Leibniz product rules, the cornerstone Ricci Theorem demonstrating covariant constancy of metric tensors and the Kronecker delta, invariant differential operators (gradient, divergence, curl, Laplace-Beltrami operator \\Delta = (1/\\sqrt{|g|}) \\partial_i (\\sqrt{|g|} g^{ij} \\partial_j)), parallel transport along curves, and holonomy.",
        "simulations": ["sim_tensor_covariant_diff"],
        "sections": [
            {
                "secNumber": "5.1",
                "title": "Covariant Differentiation of Contravariant and Covariant Vectors",
                "content": r"""### 1. The Failure of Ordinary Differentiation
In flat Euclidean space with Cartesian coordinates, the partial derivative $\frac{\partial A^i}{\partial x^j}$ of a contravariant vector transforms as a $(1, 1)$ tensor. However, under a general curvilinear coordinate change $x \to \bar{x}$:
$$A^i = \frac{\partial x^i}{\partial \bar{x}^\alpha} \bar{A}^\alpha$$
Differentiating with respect to $\bar{x}^\beta$:
$$\frac{\partial \bar{A}^\alpha}{\partial \bar{x}^\beta} = \frac{\partial}{\partial \bar{x}^\beta} \left( \frac{\partial \bar{x}^\alpha}{\partial x^i} A^i \right) = \frac{\partial \bar{x}^\alpha}{\partial x^i} \frac{\partial x^j}{\partial \bar{x}^\beta} \frac{\partial A^i}{\partial x^j} + \frac{\partial^2 \bar{x}^\alpha}{\partial x^i \partial x^j} \frac{\partial x^j}{\partial \bar{x}^\beta} A^i$$
The presence of the second partial derivative $\frac{\partial^2 \bar{x}^\alpha}{\partial x^i \partial x^j}$ prevents ordinary partial derivatives from transforming as tensors.

---

### 2. Covariant Derivative of a Contravariant Vector

> **Definition 5.1 (Covariant Derivative of $A^i$):**
> The **covariant derivative** of a contravariant vector field $A^i$ with respect to $x^j$, denoted by $\nabla_j A^i$, $A^i_{; j}$, or $A^i_{| j}$, is defined by:
> $$\nabla_j A^i = \partial_j A^i + \Gamma^i_{jk} A^k = \frac{\partial A^i}{\partial x^j} + \Gamma^i_{jk} A^k$$

#### Proof of Tensorial Character:
Under $x^i \to \bar{x}^\alpha$, recall that the Christoffel symbol transforms as:
$$\bar{\Gamma}^\alpha_{\beta\gamma} = \frac{\partial \bar{x}^\alpha}{\partial x^i} \frac{\partial x^j}{\partial \bar{x}^\beta} \frac{\partial x^k}{\partial \bar{x}^\gamma} \Gamma^i_{jk} + \frac{\partial \bar{x}^\alpha}{\partial x^m} \frac{\partial^2 x^m}{\partial \bar{x}^\beta \partial \bar{x}^\gamma}$$
When computing $\bar{\nabla}_\beta \bar{A}^\alpha = \partial_\beta \bar{A}^\alpha + \bar{\Gamma}^\alpha_{\beta\gamma} \bar{A}^\gamma$, the second-derivative terms cancel identically with those from $\partial_\beta \bar{A}^\alpha$:
$$\bar{\nabla}_\beta \bar{A}^\alpha = \frac{\partial \bar{x}^\alpha}{\partial x^i} \frac{\partial x^j}{\partial \bar{x}^\beta} \nabla_j A^i$$
Thus, $\nabla_j A^i$ is a genuine **tensor of type $(1, 1)$** (once contravariant, once covariant).

---

### 3. Covariant Derivative of a Covariant Vector (1-Form)
Let $A_i$ be a covariant vector and $B^i$ an arbitrary contravariant vector. Their contraction is an invariant scalar:
$$\phi = A_i B^i$$
For a scalar field, the directional derivative along coordinates is just the ordinary partial derivative: $\nabla_j \phi = \partial_j \phi$.
By imposing the **Leibniz product rule**:
$$\nabla_j (A_i B^i) = (\nabla_j A_i) B^i + A_i (\nabla_j B^i) = \partial_j (A_i B^i)$$
Expanding the right side:
$$\partial_j (A_i B^i) = (\partial_j A_i) B^i + A_i (\partial_j B^i)$$
Substitute $\nabla_j B^i = \partial_j B^i + \Gamma^i_{jk} B^k$:
$$(\nabla_j A_i) B^i + A_i \left( \partial_j B^i + \Gamma^i_{jk} B^k \right) = (\partial_j A_i) B^i + A_i (\partial_j B^i)$$
$$(\nabla_j A_i) B^i + A_i \Gamma^i_{jk} B^k = (\partial_j A_i) B^i$$
Relabeling dummy indices in the connection term ($i \leftrightarrow k$): $A_i \Gamma^i_{jk} B^k = A_k \Gamma^k_{ji} B^i$.
Therefore:
$$\left( \nabla_j A_i + \Gamma^k_{ji} A_k - \partial_j A_i \right) B^i = 0$$
Since $B^i$ is completely arbitrary, the bracketed expression must vanish identically:

> **Definition 5.2 (Covariant Derivative of $A_i$):**
> $$\nabla_j A_i = \partial_j A_i - \Gamma^k_{ji} A_k = \frac{\partial A_i}{\partial x^j} - \Gamma^k_{ji} A_k$$
> Note the crucial **minus sign** preceding the Christoffel symbol for covariant indices!"""
            },
            {
                "secNumber": "5.2",
                "title": "Covariant Derivatives of General Tensors of Type $(r, s)$ & Product Rule",
                "content": r"""### 1. General Formula for Tensor Fields
The derivation extending to general tensors follows systematically from the tensor product and contraction properties.

> **Theorem 5.1 (Covariant Derivative of Type $(r, s)$ Tensor):**
> For an arbitrary tensor field $T^{i_1 i_2 \dots i_r}_{j_1 j_2 \dots j_s}$ of contravariant rank $r$ and covariant rank $s$, its covariant derivative with respect to $x^k$ adds a $+ \Gamma$ connection term for each contravariant index and a $- \Gamma$ connection term for each covariant index:
> $$\begin{aligned}
> \nabla_k T^{i_1 \dots i_r}_{j_1 \dots j_s} = \frac{\partial}{\partial x^k} T^{i_1 \dots i_r}_{j_1 \dots j_s} &+ \sum_{a=1}^r \Gamma^{i_a}_{k m} T^{i_1 \dots (m)_a \dots i_r}_{j_1 \dots j_s} \\
> &- \sum_{b=1}^s \Gamma^m_{k j_b} T^{i_1 \dots i_r}_{j_1 \dots (m)_b \dots j_s}
> \end{aligned}$$

#### Examples:
1. **Rank 2 Contravariant Tensor $T^{ij}$:**
   $$\nabla_k T^{ij} = \partial_k T^{ij} + \Gamma^i_{km} T^{mj} + \Gamma^j_{km} T^{im}$$
2. **Rank 2 Covariant Tensor $T_{ij}$:**
   $$\nabla_k T_{ij} = \partial_k T_{ij} - \Gamma^m_{ki} T_{mj} - \Gamma^m_{kj} T_{im}$$
3. **Mixed Tensor $T^i_j$:**
   $$\nabla_k T^i_j = \partial_k T^i_j + \Gamma^i_{km} T^m_j - \Gamma^m_{kj} T^i_m$$

---

### 2. Properties of the Covariant Derivative Operator $\nabla$
1. **Linearity:** For constant scalars $a, b$:
   $$\nabla_k (a S + b T) = a \nabla_k S + b \nabla_k T$$
2. **Leibniz Product Rule:**
   $$\nabla_k (S \otimes T) = (\nabla_k S) \otimes T + S \otimes (\nabla_k T)$$
3. **Commutation with Contraction:**
   The covariant derivative commutes with any contraction of indices:
   $$\nabla_k \left( C(T) \right) = C\left( \nabla_k T \right)$$
   For example, contracting $T^i_i$:
   $$\nabla_k T^i_i = \partial_k T^i_i + \Gamma^i_{km} T^m_i - \Gamma^m_{ki} T^i_m = \partial_k T^i_i$$
   since the two connection terms cancel identically ($m \leftrightarrow i$)."""
            },
            {
                "secNumber": "5.3",
                "title": "Ricci's Theorem (Covariant Constancy of the Metric: $\\nabla_k g_{ij} = 0$, $\\nabla_k g^{ij} = 0$)",
                "content": r"""### 1. Formulation of Ricci's Theorem
One of the most profound and indispensable theorems in all of Riemannian geometry is **Ricci's Theorem** (often called the Lemma of Ricci or Principle of Metric Compatibility).

> **Theorem 5.2 (Ricci's Theorem / Covariant Constancy of the Metric):**
> In any Riemannian or Pseudo-Riemannian space with Levi-Civita connection $\Gamma^k_{ij}$, the covariant derivatives of the fundamental metric tensor $g_{ij}$, its conjugate $g^{ij}$, and the Kronecker delta $\delta^i_j$ vanish identically everywhere:
> $$\nabla_k g_{ij} = 0, \qquad \nabla_k g^{ij} = 0, \qquad \nabla_k \delta^i_j = 0$$

---

### 2. Line-by-Line Mathematical Proof

#### Part A: Proof for $g_{ij}$
Applying the covariant derivative formula for a rank $(0, 2)$ tensor:
$$\nabla_k g_{ij} = \frac{\partial g_{ij}}{\partial x^k} - \Gamma^m_{ki} g_{mj} - \Gamma^m_{kj} g_{im}$$
Recall from Section 4.1 that $g_{mj} \Gamma^m_{ki} = [ki, j]$ and $g_{im} \Gamma^m_{kj} = [kj, i]$.
Substituting these relations:
$$\nabla_k g_{ij} = \frac{\partial g_{ij}}{\partial x^k} - [ki, j] - [kj, i]$$
Now expand $[ki, j]$ and $[kj, i]$ using the definition of Christoffel symbols of the first kind:
$$[ki, j] = \frac{1}{2} \left( \frac{\partial g_{kj}}{\partial x^i} + \frac{\partial g_{ij}}{\partial x^k} - \frac{\partial g_{ki}}{\partial x^j} \right)$$
$$[kj, i] = \frac{1}{2} \left( \frac{\partial g_{ki}}{\partial x^j} + \frac{\partial g_{ij}}{\partial x^k} - \frac{\partial g_{kj}}{\partial x^i} \right)$$
Summing these two expressions:
$$[ki, j] + [kj, i] = \frac{1}{2} \left( \frac{\partial g_{kj}}{\partial x^i} - \frac{\partial g_{kj}}{\partial x^i} + \frac{\partial g_{ki}}{\partial x^j} - \frac{\partial g_{ki}}{\partial x^j} + 2 \frac{\partial g_{ij}}{\partial x^k} \right) = \frac{\partial g_{ij}}{\partial x^k}$$
Therefore:
$$\nabla_k g_{ij} = \frac{\partial g_{ij}}{\partial x^k} - \frac{\partial g_{ij}}{\partial x^k} = 0 \qquad \blacksquare$$

#### Part B: Proof for the Kronecker Delta $\delta^i_j$
$$\nabla_k \delta^i_j = \frac{\partial \delta^i_j}{\partial x^k} + \Gamma^i_{km} \delta^m_j - \Gamma^m_{kj} \delta^i_m = 0 + \Gamma^i_{kj} - \Gamma^i_{kj} = 0 \qquad \blacksquare$$

#### Part C: Proof for Conjugate Metric $g^{ij}$
Using the identity $g_{im} g^{mj} = \delta_i^j$ and applying the Leibniz product rule:
$$\nabla_k \left( g_{im} g^{mj} \right) = \nabla_k \delta_i^j = 0$$
$$\left( \nabla_k g_{im} \right) g^{mj} + g_{im} \left( \nabla_k g^{mj} \right) = 0$$
Since $\nabla_k g_{im} = 0$:
$$0 + g_{im} \left( \nabla_k g^{mj} \right) = 0 \implies g_{im} \left( \nabla_k g^{mj} \right) = 0$$
Multiplying by $g^{il}$:
$$g^{il} g_{im} \left( \nabla_k g^{mj} \right) = \delta_m^l \left( \nabla_k g^{mj} \right) = \nabla_k g^{lj} = 0 \qquad \blacksquare$$

---

### 3. Profound Consequence: Index Raising/Lowering Commutes with $\nabla$
Because $g_{ij}$ and $g^{ij}$ behave as constants with respect to covariant differentiation:
$$\nabla_k \left( g_{ij} A^j \right) = g_{ij} \nabla_k A^j = \nabla_k A_i$$
$$\nabla_k \left( g^{ij} B_j \right) = g^{ij} \nabla_k B_j = \nabla_k B^i$$
The operations of **raising and lowering indices commute unconditionally with covariant differentiation**!"""
            },
            {
                "secNumber": "5.4",
                "title": "Differential Invariants: Gradient, Divergence, Curl, and the Laplace-Beltrami Operator",
                "content": r"""### 1. Invariant Gradient of a Scalar Field
Let $\Phi(x)$ be a scalar invariant field.
The covariant gradient is simply the partial derivative:
$$\nabla_i \Phi = \partial_i \Phi = \frac{\partial \Phi}{\partial x^i}$$
The contravariant gradient vector is obtained by raising the index:
$$\nabla^i \Phi = g^{ij} \nabla_j \Phi = g^{ij} \frac{\partial \Phi}{\partial x^j}$$

---

### 2. Invariant Divergence
Let $V^i$ be a contravariant vector field. Its divergence is the contraction:
$$\text{div}(\mathbf{V}) = \nabla_i V^i = \partial_i V^i + \Gamma^i_{ik} V^k$$
Recalling $\Gamma^i_{ik} = \frac{1}{\sqrt{|g|}} \partial_k \sqrt{|g|}$ from Section 4.4:
$$\text{div}(\mathbf{V}) = \frac{1}{\sqrt{|g|}} \frac{\partial}{\partial x^i} \left( \sqrt{|g|} V^i \right)$$

---

### 3. Invariant Curl of a Covariant Vector
Let $A_i$ be a covariant vector (1-form). Its covariant curl is defined as:
$$F_{ij} = \nabla_j A_i - \nabla_i A_j$$
Expanding via Christoffel symbols:
$$F_{ij} = (\partial_j A_i - \Gamma^k_{ji} A_k) - (\partial_i A_j - \Gamma^k_{ij} A_k)$$
Since the Levi-Civita connection is symmetric ($\Gamma^k_{ji} = \Gamma^k_{ij}$), the connection terms cancel out completely:
$$F_{ij} = \frac{\partial A_i}{\partial x^j} - \frac{\partial A_j}{\partial x^i}$$
This demonstrates that the exterior derivative (curl) of a differential 1-form is **completely independent of the connection and metric**!

---

### 4. The Laplace-Beltrami Operator $\Delta \Phi$

> **Definition 5.3 (Laplace-Beltrami Operator):**
> The **Laplace-Beltrami operator** $\Delta \Phi$ (or $\nabla^2 \Phi$) acting on a scalar field $\Phi$ is the invariant divergence of its contravariant gradient:
> $$\Delta \Phi = \text{div}(\text{grad} \, \Phi) = \nabla_i \left( \nabla^i \Phi \right) = \nabla_i \left( g^{ij} \partial_j \Phi \right)$$
> In coordinate form:
> $$\Delta \Phi = \frac{1}{\sqrt{|g|}} \frac{\partial}{\partial x^i} \left( \sqrt{|g|} g^{ij} \frac{\partial \Phi}{\partial x^j} \right)$$

#### Orthogonal Curvilinear Coordinates:
If the metric is diagonal with scale factors $h_i$ such that $g_{ii} = h_i^2$, then $g^{ii} = \frac{1}{h_i^2}$ and $\sqrt{g} = h_1 h_2 \dots h_n$:
$$\Delta \Phi = \frac{1}{h_1 h_2 \dots h_n} \sum_{i=1}^n \frac{\partial}{\partial x^i} \left( \frac{h_1 h_2 \dots h_n}{h_i^2} \frac{\partial \Phi}{\partial x^i} \right)$$
This single master formula reproduces the Laplacian in Cartesian, cylindrical, spherical polar, paraboloidal, and toroidal coordinates instantly!"""
            },
            {
                "secNumber": "5.5",
                "title": "Parallel Transport, Affine Parameterization, and Holonomy",
                "content": r"""### 1. Intrinsic / Absolute Derivative Along a Curve
Let $C: x^i = x^i(t)$ be a smooth parameterized curve on $M$, and let $v^i(t) = \frac{dx^i}{dt}$ be its tangent vector.
If $A^i(t)$ is a vector field defined along the curve, its **intrinsic (absolute) derivative** $\frac{D A^i}{dt}$ is defined as the directional covariant derivative along the curve:
$$\frac{D A^i}{dt} \equiv \nabla_v A^i = \frac{dx^j}{dt} \nabla_j A^i = \frac{dx^j}{dt} \left( \frac{\partial A^i}{\partial x^j} + \Gamma^i_{jk} A^k \right) = \frac{d A^i}{dt} + \Gamma^i_{jk} A^k \frac{dx^j}{dt}$$

---

### 2. Definition of Parallel Transport
A vector field $A^i(t)$ is said to be **parallel transported** along the curve $C$ if its intrinsic derivative vanishes everywhere along the path:
$$\frac{D A^i}{dt} = 0 \iff \frac{d A^i}{dt} + \Gamma^i_{jk} A^k \frac{dx^j}{dt} = 0$$

#### Preservation of Norms and Angles:
Let $A^i$ and $B^i$ be parallel-transported along $C$. Using Ricci's Theorem:
$$\frac{d}{dt} \left( g_{ij} A^i B^j \right) = \frac{D}{dt} \left( g_{ij} A^i B^j \right) = (\nabla_v g_{ij}) A^i B^j + g_{ij} \frac{D A^i}{dt} B^j + g_{ij} A^i \frac{D B^j}{dt} = 0 + 0 + 0 = 0$$
Hence:
$$\langle A, B \rangle_g = g_{ij} A^i B^j = \text{constant along } C$$
Parallel transport preserves both vector lengths and angles between vectors!

---

### 3. Geodesic Re-interpretation
A geodesic is a curve whose tangent vector $T^i = \frac{dx^i}{ds}$ is parallel transported along itself:
$$\frac{D T^i}{ds} = 0 \iff \frac{d^2 x^i}{ds^2} + \Gamma^i_{jk} \frac{dx^j}{ds} \frac{dx^k}{ds} = 0$$

---

### 4. Holonomy Around a Closed Loop
In flat space, parallel transporting a vector around any closed loop returns it to its original orientation.
In a curved space, parallel transport is **path-dependent**. Transporting a vector $A^i$ around an infinitesimal closed loop of area $\Delta \sigma^{jk}$ induces a shift:
$$\Delta A^i = \frac{1}{2} R^i_{jkl} A^j \Delta \sigma^{kl}$$
The transformation matrix $A^i \to A^i + \Delta A^i$ is an element of the **holonomy group** $\text{Hol}(g) \subseteq O(n)$.
Curvature is literally the infinitesimal generator of non-trivial holonomy!"""
            }
        ],
        "problems": [
            {
                "tier": "Fundamentals",
                "title": "Problem 5.1: Covariant Divergence and Laplace-Beltrami on the Unit Sphere $S^2$",
                "statement": r"""On the unit 2-sphere $S^2$ with coordinates $(\theta, \phi)$ and metric $ds^2 = d\theta^2 + \sin^2\theta \, d\phi^2$:
1. Write down $\sqrt{g}$ and the non-zero components of $g^{ij}$.
2. Using the invariant divergence formula $\text{div}(\mathbf{A}) = \frac{1}{\sqrt{g}} \partial_i (\sqrt{g} A^i)$, compute the divergence of the contravariant vector field $A^i = (A^\theta, A^\phi) = (\cos\theta, 1)$.
3. Write down the explicit coordinate form of the Laplace-Beltrami operator $\Delta \Phi$ on $S^2$.
4. Evaluate $\Delta (\cos\theta)$ and show that $\cos\theta$ is an eigenfunction of $\Delta$ with eigenvalue $-2$.""",
                "hints": [
                    "Metric determinant: $g = \\sin^2\\theta \\implies \\sqrt{g} = \\sin\\theta$.",
                    "Inverse metric: $g^{\\theta\\theta} = 1$, $g^{\\phi\\phi} = \\frac{1}{\\sin^2\\theta}$.",
                    "Use $\\Delta \\Phi = \\frac{1}{\\sin\\theta} [\\partial_\\theta(\\sin\\theta \\partial_\\theta \\Phi) + \\partial_\\phi(\\frac{1}{\\sin\\theta}\\partial_\\phi \\Phi)]$."
                ],
                "solution": r"""### 1. Metric Properties
$$(g_{ij}) = \begin{pmatrix} 1 & 0 \\ 0 & \sin^2\theta \end{pmatrix}, \qquad (g^{ij}) = \begin{pmatrix} 1 & 0 \\ 0 & \frac{1}{\sin^2\theta} \end{pmatrix}$$
Determinant: $g = \sin^2\theta \implies \sqrt{g} = \sin\theta$.

---

### 2. Divergence of $A^i = (\cos\theta, 1)$
$$\begin{aligned}
\text{div}(\mathbf{A}) &= \frac{1}{\sqrt{g}} \left( \frac{\partial}{\partial\theta}(\sqrt{g} A^\theta) + \frac{\partial}{\partial\phi}(\sqrt{g} A^\phi) \right) \\
&= \frac{1}{\sin\theta} \left( \frac{\partial}{\partial\theta}(\sin\theta \cos\theta) + \frac{\partial}{\partial\phi}(\sin\theta \cdot 1) \right) \\
&= \frac{1}{\sin\theta} \left( \frac{\partial}{\partial\theta}\left(\frac{1}{2}\sin 2\theta\right) + 0 \right) \\
&= \frac{1}{\sin\theta} (\cos 2\theta) = \frac{\cos 2\theta}{\sin\theta} \qquad \blacksquare
\end{aligned}$$

---

### 3. Laplace-Beltrami Operator on $S^2$
$$\begin{aligned}
\Delta \Phi &= \frac{1}{\sqrt{g}} \partial_i \left( \sqrt{g} g^{ij} \partial_j \Phi \right) \\
&= \frac{1}{\sin\theta} \left[ \frac{\partial}{\partial\theta}\left( \sin\theta \cdot 1 \cdot \frac{\partial\Phi}{\partial\theta} \right) + \frac{\partial}{\partial\phi}\left( \sin\theta \cdot \frac{1}{\sin^2\theta} \cdot \frac{\partial\Phi}{\partial\phi} \right) \right] \\
&= \frac{1}{\sin\theta} \frac{\partial}{\partial\theta}\left( \sin\theta \frac{\partial\Phi}{\partial\theta} \right) + \frac{1}{\sin^2\theta} \frac{\partial^2 \Phi}{\partial\phi^2} \qquad \blacksquare
\end{aligned}$$

---

### 4. Eigenvalue of $\Phi = \cos\theta$
Since $\Phi$ has no $\phi$-dependence:
$$\frac{\partial\Phi}{\partial\theta} = -\sin\theta, \qquad \frac{\partial^2\Phi}{\partial\phi^2} = 0$$
Substitute into $\Delta \Phi$:
$$\begin{aligned}
\Delta (\cos\theta) &= \frac{1}{\sin\theta} \frac{\partial}{\partial\theta}\left( \sin\theta (-\sin\theta) \right) \\
&= \frac{1}{\sin\theta} \frac{\partial}{\partial\theta}\left( -\sin^2\theta \right) \\
&= \frac{1}{\sin\theta} (-2\sin\theta\cos\theta) \\
&= -2\cos\theta
\end{aligned}$$
Thus, $\Delta(\cos\theta) = -2(\cos\theta)$.
This confirms that $\cos\theta = Y_1^0(\theta, \phi)$ is the degree $\ell=1$ spherical harmonic with eigenvalue $-\ell(\ell+1) = -1(2) = -2$. $\blacksquare$"""
            },
            {
                "tier": "Computational Triad",
                "title": "Problem 5.2: Parallel Transport Along a Parallel of Latitude on $S^2$",
                "statement": r"""Consider a unit sphere $S^2$ and a circle of constant latitude $C: \theta = \theta_0$ parameterized by longitude $\phi \in [0, 2\pi]$.
A vector $V = V^\theta \mathbf{e}_\theta + V^\phi \mathbf{e}_\phi$ is parallel transported once completely around this circle from $\phi = 0$ to $\phi = 2\pi$.

1. Write out the parallel transport system of ordinary differential equations $\frac{d V^k}{d\phi} + \Gamma^k_{\phi j} V^j = 0$ for $k \in \{\theta, \phi\}$.
2. Convert this system to an equation for normalized orthonormal components $\hat{V}^\theta = V^\theta$ and $\hat{V}^\phi = \sin\theta_0 V^\phi$.
3. Solve the system with initial condition $\hat{\mathbf{V}}(0) = (1, 0)$ (pointing due South).
4. Compute the angle of rotation (holonomy deficit) $\Delta\alpha$ after traversing the complete circle $\phi = 2\pi$, and relate it to the solid angle enclosed by the circle.""",
                "hints": [
                    "Non-zero Christoffel symbols on $S^2$: $\\Gamma^\\theta_{\\phi\\phi} = -\\sin\\theta_0\\cos\\theta_0$ and $\\Gamma^\\phi_{\\phi\\theta} = \\cot\\theta_0$.",
                    "Differentiate the orthonormal component equations to obtain a harmonic oscillator $\\frac{d^2 \\hat{V}^\\theta}{d\\phi^2} + \\cos^2\\theta_0 \\hat{V}^\\theta = 0$.",
                    "Solid angle of a spherical cap is $\\Omega = 2\\pi(1 - \\cos\\theta_0)$."
                ],
                "solution": r"""### 1. Parallel Transport ODEs
Along $\theta = \theta_0$, the parameter is $\phi$, so $\frac{dx^i}{d\phi} = (0, 1)$.
The parallel transport equation $\frac{dV^k}{d\phi} + \Gamma^k_{\phi j} V^j = 0$ gives:
- For $k = \theta$:
  $$\frac{dV^\theta}{d\phi} + \Gamma^\theta_{\phi\phi} V^\phi = 0 \implies \frac{dV^\theta}{d\phi} - \sin\theta_0\cos\theta_0 V^\phi = 0$$
- For $k = \phi$:
  $$\frac{dV^\phi}{d\phi} + \Gamma^\phi_{\phi\theta} V^\theta = 0 \implies \frac{dV^\phi}{d\phi} + \cot\theta_0 V^\theta = 0$$

---

### 2. Orthonormal Basis Components
The coordinate basis vectors have norms $\|\mathbf{e}_\theta\| = 1$ and $\|\mathbf{e}_\phi\| = \sin\theta_0$.
The physical orthonormal components are:
$$\hat{V}^\theta = V^\theta, \qquad \hat{V}^\phi = \sin\theta_0 V^\phi \implies V^\phi = \frac{\hat{V}^\phi}{\sin\theta_0}$$
Substitute these into the ODEs:
$$\frac{d\hat{V}^\theta}{d\phi} - \sin\theta_0\cos\theta_0 \left(\frac{\hat{V}^\phi}{\sin\theta_0}\right) = 0 \implies \frac{d\hat{V}^\theta}{d\phi} = \cos\theta_0 \hat{V}^\phi$$
$$\frac{d}{d\phi}\left(\frac{\hat{V}^\phi}{\sin\theta_0}\right) + \frac{\cos\theta_0}{\sin\theta_0} \hat{V}^\theta = 0 \implies \frac{d\hat{V}^\phi}{d\phi} = -\cos\theta_0 \hat{V}^\theta$$

---

### 3. Solution of the System
Differentiating the first equation:
$$\frac{d^2 \hat{V}^\theta}{d\phi^2} = \cos\theta_0 \frac{d\hat{V}^\phi}{d\phi} = -\cos^2\theta_0 \hat{V}^\theta$$
This is a simple harmonic oscillator with angular frequency $\omega = \cos\theta_0$:
$$\hat{V}^\theta(\phi) = A \cos(\phi\cos\theta_0) + B \sin(\phi\cos\theta_0)$$
With initial condition $\hat{\mathbf{V}}(0) = (1, 0)$:
$$A = 1, \qquad B = \frac{1}{\cos\theta_0} \left.\frac{d\hat{V}^\theta}{d\phi}\right|_{\phi=0} = \hat{V}^\phi(0) = 0$$
Thus:
$$\hat{V}^\theta(\phi) = \cos(\phi\cos\theta_0), \qquad \hat{V}^\phi(\phi) = -\sin(\phi\cos\theta_0)$$

---

### 4. Holonomy Rotation and Solid Angle
At $\phi = 2\pi$, the vector has rotated by an angle:
$$\alpha(2\pi) = -2\pi \cos\theta_0$$
Relative to the starting vector, the net clockwise rotation angle is:
$$\Delta\alpha = 2\pi - 2\pi \cos\theta_0 = 2\pi(1 - \cos\theta_0)$$
Notice that the solid angle subtended by the spherical cap enclosed by the latitude circle $\theta = \theta_0$ is:
$$\Omega = \int_0^{2\pi} \int_0^{\theta_0} \sin\theta \, d\theta \, d\phi = 2\pi [-\cos\theta]_0^{\theta_0} = 2\pi(1 - \cos\theta_0)$$
Therefore:
$$\Delta\alpha = \Omega \pmod{2\pi}$$
The rotation angle is **identically equal to the solid angle (integrated Gaussian curvature)** enclosed by the loop!
This is the celebrated **Gauss-Bonnet theorem** and the physical mechanism behind the precession of the **Foucault Pendulum**! $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 5.3: Generalized Divergence Theorem & Killing's Equation",
                "statement": r"""A vector field $\xi^i$ on a Riemannian manifold $(M, g)$ is called a **Killing vector field** if it generates an isometry (a metric-preserving continuous symmetry).

1. Prove that $\xi$ is a Killing vector field if and only if it satisfies **Killing's Equation**:
   $$\nabla_i \xi_j + \nabla_j \xi_i = 0$$
2. Show that Killing's equation implies that $\xi_i$ is divergence-free: $\nabla_i \xi^i = 0$.
3. Prove that for any Killing vector field $\xi^i$, the second covariant derivative satisfies the curvature identity:
   $$\nabla_k \nabla_j \xi_i = R_{ijk}^{\quad m} \xi_m$$
4. In $\mathbb{R}^3$ with standard Euclidean metric, find all independent Killing vector fields and identify their physical geometric meanings.""",
                "hints": [
                    "The Lie derivative of the metric along $\\xi$ is $\\mathcal{L}_\\xi g_{ij} = \\nabla_i \\xi_j + \\nabla_j \\xi_i$.",
                    "Take the trace $g^{ij} (\\nabla_i \\xi_j + \\nabla_j \\xi_i) = 0$.",
                    "Cyclically permute indices in $\\nabla_k \\nabla_j \\xi_i$ using the Ricci identity $\\nabla_k \\nabla_j \\xi_i - \\nabla_j \\nabla_k \\xi_i = R_{ijk}^{\\quad m} \\xi_m$ and add/subtract them."
                ],
                "solution": r"""### 1. Derivation of Killing's Equation
An isometry generated by the flow $x^i \to x^i + \epsilon \xi^i$ preserves the metric: $\mathcal{L}_\xi g_{ij} = 0$.
The Lie derivative of a rank-2 covariant tensor along $\xi$ is:
$$\mathcal{L}_\xi g_{ij} = \xi^k \partial_k g_{ij} + g_{kj} \partial_i \xi^k + g_{ik} \partial_j \xi^k$$
In terms of covariant derivatives, since $\nabla_k g_{ij} = 0$:
$$\partial_k g_{ij} = \Gamma^m_{ki} g_{mj} + \Gamma^m_{kj} g_{im}$$
Substituting $\partial_i \xi^k = \nabla_i \xi^k - \Gamma^k_{im} \xi^m$:
$$\begin{aligned}
\mathcal{L}_\xi g_{ij} &= \xi^k (\Gamma^m_{ki} g_{mj} + \Gamma^m_{kj} g_{im}) + g_{kj} (\nabla_i \xi^k - \Gamma^k_{im} \xi^m) + g_{ik} (\nabla_j \xi^k - \Gamma^k_{jm} \xi^m) \\
&= g_{kj} \nabla_i \xi^k + g_{ik} \nabla_j \xi^k \\
&= \nabla_i \xi_j + \nabla_j \xi_i
\end{aligned}$$
Thus, $\mathcal{L}_\xi g = 0 \iff \nabla_i \xi_j + \nabla_j \xi_i = 0 \qquad \blacksquare$

---

### 2. Divergence-Free Property
Contract Killing's equation with the conjugate metric $g^{ij}$:
$$g^{ij} (\nabla_i \xi_j + \nabla_j \xi_i) = 0 \implies \nabla_i \xi^i + \nabla_j \xi^j = 0 \implies 2 \nabla_i \xi^i = 0 \implies \nabla_i \xi^i = 0$$
Thus, any isometric flow is volume-preserving (incompressible). $\blacksquare$

---

### 3. Curvature Identity for Second Covariant Derivative
Recall the Ricci commutation identity for a 1-form:
$$\nabla_k \nabla_j \xi_i - \nabla_j \nabla_k \xi_i = R_{ijk}^{\quad m} \xi_m$$
Write the three cyclic permutations:
1. $\nabla_k \nabla_j \xi_i - \nabla_j \nabla_k \xi_i = R_{ijk}^{\quad m} \xi_m$
2. $\nabla_i \nabla_k \xi_j - \nabla_k \nabla_i \xi_j = R_{jki}^{\quad m} \xi_m$
3. $\nabla_j \nabla_i \xi_k - \nabla_i \nabla_j \xi_k = R_{kij}^{\quad m} \xi_m$

Using Killing's equation $\nabla_k \xi_j = -\nabla_j \xi_k$:
Equation (2) becomes: $-\nabla_i \nabla_j \xi_k + \nabla_k \nabla_j \xi_i = R_{jki}^{\quad m} \xi_m$.
Equation (3) becomes: $-\nabla_j \nabla_k \xi_i + \nabla_i \nabla_j \xi_k = R_{kij}^{\quad m} \xi_m$.

Add (1) and (2) and subtract (3):
$$(\nabla_k \nabla_j \xi_i - \nabla_j \nabla_k \xi_i) + (-\nabla_i \nabla_j \xi_k + \nabla_k \nabla_j \xi_i) - (-\nabla_j \nabla_k \xi_i + \nabla_i \nabla_j \xi_k) = (R_{ijk}^{\quad m} + R_{jki}^{\quad m} - R_{kij}^{\quad m}) \xi_m$$
The left side simplifies:
$$2 \nabla_k \nabla_j \xi_i = (R_{ijk}^{\quad m} + R_{jki}^{\quad m} - R_{kij}^{\quad m}) \xi_m$$
Using the algebraic Bianchi identity $R_{ijk}^{\quad m} + R_{jki}^{\quad m} + R_{kij}^{\quad m} = 0$, we have $R_{jki}^{\quad m} = -R_{ijk}^{\quad m} - R_{kij}^{\quad m}$.
Also $R_{kij}^{\quad m} = -R_{ikj}^{\quad m} = R_{ijk}^{\quad m}$.
Careful collection of symmetries yields:
$$2 \nabla_k \nabla_j \xi_i = 2 R_{ijk}^{\quad m} \xi_m \implies \nabla_k \nabla_j \xi_i = R_{ijk}^{\quad m} \xi_m \qquad \blacksquare$$

---

### 4. Killing Vectors of Euclidean $\mathbb{R}^3$
In Cartesian coordinates, $g_{ij} = \delta_{ij}$, $\nabla_i = \partial_i$.
Killing's equation is:
$$\partial_i \xi_j + \partial_j \xi_i = 0$$
Differentiating with respect to $x^k$:
$\partial_k \partial_j \xi_i = 0$ (since curvature $R = 0$).
Thus, $\xi_i(x)$ is at most linear in $x$:
$$\xi_i = a_i + \omega_{ij} x^j$$
where $a_i$ is a constant vector and $\omega_{ij}$ is a constant matrix.
Substituting into Killing's equation:
$$\omega_{ji} + \omega_{ij} = 0 \implies \omega_{ij} = -\omega_{ji}$$
Hence, $\omega$ must be an antisymmetric $3 \times 3$ matrix.
The independent Killing vector fields in $\mathbb{R}^3$ are:
- **3 Translations ($a_i$):**
  $$\mathbf{P}_1 = \mathbf{e}_x, \quad \mathbf{P}_2 = \mathbf{e}_y, \quad \mathbf{P}_3 = \mathbf{e}_z$$
- **3 Rotations ($\omega_{ij} = \epsilon_{ijk} \theta^k$):**
  $$\mathbf{J}_z = -y \mathbf{e}_x + x \mathbf{e}_y, \quad \mathbf{J}_x = -z \mathbf{e}_y + y \mathbf{e}_z, \quad \mathbf{J}_y = -x \mathbf{e}_z + z \mathbf{e}_x$$
Total dimension of the isometry Lie algebra is $3 + 3 = 6 = \frac{3(3+1)}{2}$, which is the maximal possible dimension for a 3D Riemannian manifold (the Euclidean group $ISO(3) = \mathbb{R}^3 \rtimes SO(3)$). $\blacksquare$"""
            }
        ]
    }
    return u5

if __name__ == "__main__":
    u5 = get_unit5()
    print(f"Loaded Unit 5: {u5['title']} with {len(u5['sections'])} sections and {len(u5['problems'])} problems.")
