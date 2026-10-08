# -*- coding: utf-8 -*-
"""
build_ra_unit8.py
Constructs Unit 8: Multivariable Analysis: Euclidean Topology, Fréchet Derivatives & Multiple Integrals
"""

def get_unit8():
    u8 = {
        "number": 8,
        "title": "Multivariable Analysis: Euclidean Topology, Fréchet Derivatives & Multiple Integrals",
        "leadSummary": "Comprehensive mathematical theory of multivariable real analysis in Euclidean space R^n: inner product spaces, norms, Cauchy-Schwarz inequality, topology of R^n, multivariable limits and continuity, partial derivatives, the total Fréchet derivative and Jacobian matrix, the Multivariable Chain Rule, the Inverse Function Theorem, the Implicit Function Theorem, and multiple Riemann integrals, Fubini's Theorem, and the Change of Variables theorem with Jacobian determinants.",
        "simulations": ["sim_ra_multivariable_jacobian"],
        "sections": [
            {
                "secNumber": "8.1",
                "title": "Euclidean Space R^n: Inner Product, Norms, Cauchy-Schwarz & Open Balls",
                "content": r"""### 1. Vector Space Structure of $\mathbb{R}^n$

Euclidean $n$-space is the Cartesian product $\mathbb{R}^n = \mathbb{R} \times \dots \times \mathbb{R}$ of all ordered $n$-tuples of real numbers:
$$\mathbf{x} = (x_1, x_2, \dots, x_n), \quad x_i \in \mathbb{R}$$
Endowed with componentwise addition $\mathbf{x} + \mathbf{y}$ and scalar multiplication $c \mathbf{x}$, $\mathbb{R}^n$ forms an $n$-dimensional real vector space.

> **Definition 8.1 (Euclidean Inner Product and Norm):**
> 1. The **inner product** (or dot product) of $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n$ is:
>    $$\langle \mathbf{x}, \mathbf{y} \rangle = \mathbf{x} \cdot \mathbf{y} = \sum_{i=1}^n x_i y_i$$
> 2. The standard **Euclidean norm** (magnitude) is:
>    $$\|\mathbf{x}\| = \sqrt{\langle \mathbf{x}, \mathbf{x} \rangle} = \sqrt{\sum_{i=1}^n x_i^2}$$

---

### 2. The Cauchy-Schwarz Inequality

> **Theorem 8.1 (Cauchy-Schwarz Inequality):**
> For all $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n$:
> $$|\langle \mathbf{x}, \mathbf{y} \rangle| \le \|\mathbf{x}\| \|\mathbf{y}\|$$
> with equality holding if and only if $\mathbf{x}$ and $\mathbf{y}$ are linearly dependent (parallel).

#### Complete Line-by-Line Proof:
If $\mathbf{y} = \mathbf{0}$, both sides equal zero, and equality trivially holds.
Assume $\mathbf{y} \ne \mathbf{0}$, so $\|\mathbf{y}\|^2 > 0$.
For any scalar $t \in \mathbb{R}$, consider the vector $\mathbf{x} - t \mathbf{y}$.
By positive-definiteness of the inner product:
$$\|\mathbf{x} - t \mathbf{y}\|^2 = \langle \mathbf{x} - t \mathbf{y}, \mathbf{x} - t \mathbf{y} \rangle \ge 0$$
Expanding via bilinearity and symmetry:
$$\langle \mathbf{x}, \mathbf{x} \rangle - 2t \langle \mathbf{x}, \mathbf{y} \rangle + t^2 \langle \mathbf{y}, \mathbf{y} \rangle \ge 0$$
$$\|\mathbf{x}\|^2 - 2t \langle \mathbf{x}, \mathbf{y} \rangle + t^2 \|\mathbf{y}\|^2 \ge 0$$
This is a quadratic polynomial $q(t) = A t^2 + B t + C$ in the variable $t$, where $A = \|\mathbf{y}\|^2 > 0$, $B = -2\langle \mathbf{x}, \mathbf{y} \rangle$, and $C = \|\mathbf{x}\|^2$.
Since $q(t) \ge 0$ for all real $t$, this parabola cannot have two distinct real roots.
Therefore, its discriminant $\Delta = B^2 - 4AC$ must be non-positive:
$$\Delta = (-2\langle \mathbf{x}, \mathbf{y} \rangle)^2 - 4 \|\mathbf{y}\|^2 \|\mathbf{x}\|^2 \le 0$$
$$4 \langle \mathbf{x}, \mathbf{y} \rangle^2 \le 4 \|\mathbf{x}\|^2 \|\mathbf{y}\|^2 \iff |\langle \mathbf{x}, \mathbf{y} \rangle|^2 \le \|\mathbf{x}\|^2 \|\mathbf{y}\|^2$$
Taking square roots yields:
$$|\langle \mathbf{x}, \mathbf{y} \rangle| \le \|\mathbf{x}\| \|\mathbf{y}\| \quad \blacksquare$$

> **Corollary 8.1 (Triangle Inequality in $\mathbb{R}^n$):**
> For all $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n$:
> $$\|\mathbf{x} + \mathbf{y}\| \le \|\mathbf{x}\| + \|\mathbf{y}\|$$
> *Proof:* $\|\mathbf{x} + \mathbf{y}\|^2 = \|\mathbf{x}\|^2 + 2\langle \mathbf{x}, \mathbf{y} \rangle + \|\mathbf{y}\|^2 \le \|\mathbf{x}\|^2 + 2\|\mathbf{x}\|\|\mathbf{y}\| + \|\mathbf{y}\|^2 = (\|\mathbf{x}\| + \|\mathbf{y}\|)^2$. $\blacksquare$

---

### 3. Topology of $\mathbb{R}^n$

The metric on $\mathbb{R}^n$ is $d(\mathbf{x}, \mathbf{y}) = \|\mathbf{x} - \mathbf{y}\|$.
- An **open ball** centered at $\mathbf{x}_0$ with radius $r > 0$ is $B(\mathbf{x}_0, r) = \{ \mathbf{x} \in \mathbb{R}^n : \|\mathbf{x} - \mathbf{x}_0\| < r \}$.
- A subset $U \subseteq \mathbb{R}^n$ is open if every point is interior: $\forall \mathbf{x} \in U, \; \exists r > 0 \text{ s.t. } B(\mathbf{x}, r) \subseteq U$.
- The **Heine-Borel Theorem** holds verbatim in $\mathbb{R}^n$: A subset $K \subset \mathbb{R}^n$ is compact if and only if it is closed and bounded.
- The space $\mathbb{R}^n$ is complete: every Cauchy sequence in $\mathbb{R}^n$ converges."""
            },
            {
                "secNumber": "8.2",
                "title": "Limits, Continuity, Partial Derivatives & The Total Fréchet Derivative",
                "content": r"""### 1. Limits and Continuity in Multivariable Spaces

> **Definition 8.2 (Multivariable Limit):**
> Let $E \subseteq \mathbb{R}^n$, $\mathbf{f}: E \to \mathbb{R}^m$, and $\mathbf{c}$ be a limit point of $E$.
> We write $\lim_{\mathbf{x} \to \mathbf{c}} \mathbf{f}(\mathbf{x}) = \mathbf{L} \in \mathbb{R}^m$ if:
> $$\forall \epsilon > 0, \; \exists \delta > 0 \text{ such that } 0 < \|\mathbf{x} - \mathbf{c}\| < \delta \implies \|\mathbf{f}(\mathbf{x}) - \mathbf{L}\| < \epsilon$$

---

### 2. Directional and Partial Derivatives

> **Definition 8.3 (Directional Derivative):**
> Let $U \subseteq \mathbb{R}^n$ be open, $f: U \to \mathbb{R}$, $\mathbf{x} \in U$, and $\mathbf{v} \in \mathbb{R}^n$ be a unit vector ($\|\mathbf{v}\| = 1$).
> The **directional derivative** of $f$ at $\mathbf{x}$ in the direction of $\mathbf{v}$ is:
> $$D_{\mathbf{v}} f(\mathbf{x}) = \lim_{t \to 0} \frac{f(\mathbf{x} + t \mathbf{v}) - f(\mathbf{x})}{t}$$
> If $\mathbf{v} = \mathbf{e}_j$ (the $j$-th standard basis vector), this is the **partial derivative**:
> $$\frac{\partial f}{\partial x_j}(\mathbf{x}) = D_{\mathbf{e}_j} f(\mathbf{x})$$

> **Cautionary Insight:**
> The existence of ALL partial derivatives (and even all directional derivatives) at a point **does NOT imply continuity**!
> For example: $f(x, y) = \frac{x y^2}{x^2 + y^4}$ ($f(0, 0) = 0$) has directional derivatives in every direction at $(0, 0)$, yet is discontinuous along the parabola $x = y^2$ where $f(y^2, y) = 1/2 \ne 0$.
> Differentiability in several variables requires a stronger, linear-algebraic concept: the **Fréchet derivative**.

---

### 3. The Total Fréchet Derivative

> **Definition 8.4 (Total Derivative / Fréchet Derivative):**
> Let $U \subseteq \mathbb{R}^n$ be open, $\mathbf{f}: U \to \mathbb{R}^m$, and $\mathbf{x}_0 \in U$.
> The function $\mathbf{f}$ is **differentiable at $\mathbf{x}_0$** if there exists a linear transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ (denoted $D\mathbf{f}(\mathbf{x}_0)$) such that:
> $$\lim_{\mathbf{h} \to \mathbf{0}} \frac{\|\mathbf{f}(\mathbf{x}_0 + \mathbf{h}) - \mathbf{f}(\mathbf{x}_0) - T(\mathbf{h})\|}{\|\mathbf{h}\|} = 0$$
> Equivalently:
> $$\mathbf{f}(\mathbf{x}_0 + \mathbf{h}) = \mathbf{f}(\mathbf{x}_0) + D\mathbf{f}(\mathbf{x}_0)(\mathbf{h}) + \mathbf{R}(\mathbf{h}), \quad \text{where } \lim_{\mathbf{h} \to \mathbf{0}} \frac{\|\mathbf{R}(\mathbf{h})\|}{\|\mathbf{h}\|} = 0$$

> **Theorem 8.2 (Differentiability Implies Continuity):**
> If $\mathbf{f}$ is differentiable at $\mathbf{x}_0$, then $\mathbf{f}$ is continuous at $\mathbf{x}_0$."""
            },
            {
                "secNumber": "8.3",
                "title": "The Jacobian Matrix, Multivariable Chain Rule & C^1 Functions",
                "content": r"""### 1. Matrix Representation: The Jacobian Matrix

> **Theorem 8.3 (Uniqueness of Derivative & Jacobian Representation):**
> If $\mathbf{f} = (f_1, f_2, \dots, f_m)^T: U \subseteq \mathbb{R}^n \to \mathbb{R}^m$ is differentiable at $\mathbf{x}_0$, then all partial derivatives $\frac{\partial f_i}{\partial x_j}(\mathbf{x}_0)$ exist, and the matrix representation of $D\mathbf{f}(\mathbf{x}_0)$ with respect to the standard bases is the $m \times n$ **Jacobian matrix**:
> $$J_{\mathbf{f}}(\mathbf{x}_0) = \begin{pmatrix}
> \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \dots & \frac{\partial f_1}{\partial x_n} \\
> \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \dots & \frac{\partial f_2}{\partial x_n} \\
> \vdots & \vdots & \ddots & \vdots \\
> \frac{\partial f_m}{\partial x_1} & \frac{\partial f_m}{\partial x_2} & \dots & \frac{\partial f_m}{\partial x_n}
> \end{pmatrix}$$
> That is, $D\mathbf{f}(\mathbf{x}_0)(\mathbf{h}) = J_{\mathbf{f}}(\mathbf{x}_0) \mathbf{h}$.

---

### 2. Sufficient Condition for Differentiability ($C^1$)

> **Theorem 8.4 (Continuously Differentiable implies Differentiable):**
> Let $U \subseteq \mathbb{R}^n$ be open and $\mathbf{f}: U \to \mathbb{R}^m$.
> If all partial derivatives $\frac{\partial f_i}{\partial x_j}$ exist on $U$ and are **continuous** at $\mathbf{x}_0$ (i.e., $\mathbf{f} \in C^1(U)$), then $\mathbf{f}$ is differentiable at $\mathbf{x}_0$.

#### Proof:
By considering each component function $f_i$ separately, it suffices to prove this for $f: U \subseteq \mathbb{R}^n \to \mathbb{R}$.
Let $\mathbf{h} = (h_1, h_2, \dots, h_n)$.
Express the difference $f(\mathbf{x}_0 + \mathbf{h}) - f(\mathbf{x}_0)$ as a telescoping sum across coordinate axes:
$$f(\mathbf{x}_0 + \mathbf{h}) - f(\mathbf{x}_0) = \sum_{j=1}^n \left[ f\left(\mathbf{x}_0 + \sum_{k=1}^j h_k \mathbf{e}_k\right) - f\left(\mathbf{x}_0 + \sum_{k=1}^{j-1} h_k \mathbf{e}_k\right) \right]$$
In each step, only the $j$-th coordinate varies.
By the single-variable Mean Value Theorem (Theorem 6.6), there exists $\theta_j \in (0, 1)$ such that:
$$f\left(\mathbf{x}_0 + \sum_{k=1}^j h_k \mathbf{e}_k\right) - f\left(\mathbf{x}_0 + \sum_{k=1}^{j-1} h_k \mathbf{e}_k\right) = \frac{\partial f}{\partial x_j}(\mathbf{p}_j) h_j$$
where $\mathbf{p}_j$ lies on the line segment between $\mathbf{x}_0$ and $\mathbf{x}_0 + \mathbf{h}$.
Now subtract the candidate linear approximation $\sum_{j=1}^n \frac{\partial f}{\partial x_j}(\mathbf{x}_0) h_j$:
$$\frac{|f(\mathbf{x}_0 + \mathbf{h}) - f(\mathbf{x}_0) - \sum_{j=1}^n \frac{\partial f}{\partial x_j}(\mathbf{x}_0) h_j|}{\|\mathbf{h}\|} \le \sum_{j=1}^n \left| \frac{\partial f}{\partial x_j}(\mathbf{p}_j) - \frac{\partial f}{\partial x_j}(\mathbf{x}_0) \right| \frac{|h_j|}{\|\mathbf{h}\|}$$
Since $|h_j| \le \|\mathbf{h}\|$, the ratio $\frac{|h_j|}{\|\mathbf{h}\|} \le 1$.
As $\mathbf{h} \to \mathbf{0}$, $\mathbf{p}_j \to \mathbf{x}_0$.
Since each partial derivative is continuous at $\mathbf{x}_0$, $\left| \frac{\partial f}{\partial x_j}(\mathbf{p}_j) - \frac{\partial f}{\partial x_j}(\mathbf{x}_0) \right| \to 0$.
Thus the error quotient vanishes as $\mathbf{h} \to \mathbf{0}$.
Therefore, $f$ is differentiable at $\mathbf{x}_0$. $\blacksquare$

---

### 3. The Multivariable Chain Rule

> **Theorem 8.5 (Multivariable Chain Rule):**
> Let $U \subseteq \mathbb{R}^n$ and $V \subseteq \mathbb{R}^m$ be open sets.
> If $\mathbf{f}: U \to V$ is differentiable at $\mathbf{x}_0 \in U$ and $\mathbf{g}: V \to \mathbb{R}^p$ is differentiable at $\mathbf{y}_0 = \mathbf{f}(\mathbf{x}_0) \in V$,
> then the composite mapping $\mathbf{h} = \mathbf{g} \circ \mathbf{f}: U \to \mathbb{R}^p$ is differentiable at $\mathbf{x}_0$, and:
> $$D(\mathbf{g} \circ \mathbf{f})(\mathbf{x}_0) = D\mathbf{g}(\mathbf{f}(\mathbf{x}_0)) \circ D\mathbf{f}(\mathbf{x}_0)$$
> In matrix notation:
> $$J_{\mathbf{g} \circ \mathbf{f}}(\mathbf{x}_0) = J_{\mathbf{g}}(\mathbf{f}(\mathbf{x}_0)) \cdot J_{\mathbf{f}}(\mathbf{x}_0)$$
> The Jacobian matrix of a composite function is the matrix product of their respective Jacobian matrices!"""
            },
            {
                "secNumber": "8.4",
                "title": "The Inverse Function Theorem & The Implicit Function Theorem in R^n",
                "content": r"""### 1. The Inverse Function Theorem

The Inverse Function Theorem provides the definitive criterion under which a non-linear mapping can be locally inverted, generalizing the 1D condition $f'(x_0) \ne 0$.

> **Theorem 8.6 (Inverse Function Theorem):**
> Let $U \subseteq \mathbb{R}^n$ be an open set and let $\mathbf{f}: U \to \mathbb{R}^n$ be a continuously differentiable ($C^1$) mapping.
> Suppose that at a point $\mathbf{x}_0 \in U$, the total derivative $D\mathbf{f}(\mathbf{x}_0)$ is invertible:
> $$\det J_{\mathbf{f}}(\mathbf{x}_0) \ne 0$$
> Then:
> 1. There exists an open neighborhood $V$ containing $\mathbf{x}_0$ and an open neighborhood $W$ containing $\mathbf{y}_0 = \mathbf{f}(\mathbf{x}_0)$ such that $\mathbf{f}: V \to W$ is a **bijection** (a local $C^1$-diffeomorphism).
> 2. The inverse function $\mathbf{g} = \mathbf{f}^{-1}: W \to V$ is also continuously differentiable ($C^1$).
> 3. For every $\mathbf{y} \in W$, the derivative of the inverse is the matrix inverse of the derivative:
>    $$D\mathbf{g}(\mathbf{y}) = [D\mathbf{f}(\mathbf{g}(\mathbf{y}))]^{-1} \iff J_{\mathbf{f}^{-1}}(\mathbf{y}) = [J_{\mathbf{f}}(\mathbf{x})]^{-1}$$

---

### 2. The Implicit Function Theorem

In applications, equations often define variables implicitly, such as $F(x, y, z) = 0$. Under what conditions can we solve for some variables in terms of the others: $z = g(x, y)$?

> **Theorem 8.7 (Implicit Function Theorem):**
> Let $U \subseteq \mathbb{R}^n \times \mathbb{R}^m$ be open, and let $\mathbf{F}: U \to \mathbb{R}^m$ be a $C^1$ function, with coordinates $(\mathbf{x}, \mathbf{y}) = (x_1, \dots, x_n, y_1, \dots, y_m)$.
> Suppose $(\mathbf{x}_0, \mathbf{y}_0) \in U$ satisfies:
> 1. $\mathbf{F}(\mathbf{x}_0, \mathbf{y}_0) = \mathbf{0}$.
> 2. The $m \times m$ partial Jacobian matrix with respect to $\mathbf{y}$ is invertible:
>    $$\det \left( \frac{\partial \mathbf{F}}{\partial \mathbf{y}}(\mathbf{x}_0, \mathbf{y}_0) \right) = \det \begin{pmatrix}
>    \frac{\partial F_1}{\partial y_1} & \dots & \frac{\partial F_1}{\partial y_m} \\
>    \vdots & \ddots & \vdots \\
>    \frac{\partial F_m}{\partial y_1} & \dots & \frac{\partial F_m}{\partial y_m}
>    \end{pmatrix} \ne 0$$
> Then:
> 1. There exists an open neighborhood $V \subseteq \mathbb{R}^n$ of $\mathbf{x}_0$ and an open neighborhood $W \subseteq \mathbb{R}^m$ of $\mathbf{y}_0$ such that for each $\mathbf{x} \in V$, there exists a unique $\mathbf{y} = \mathbf{g}(\mathbf{x}) \in W$ satisfying:
>    $$\mathbf{F}(\mathbf{x}, \mathbf{g}(\mathbf{x})) = \mathbf{0}$$
> 2. The function $\mathbf{g}: V \to W$ is continuously differentiable ($C^1$).
> 3. The derivative of $\mathbf{g}$ is given by:
>    $$D\mathbf{g}(\mathbf{x}_0) = - \left[ \frac{\partial \mathbf{F}}{\partial \mathbf{y}}(\mathbf{x}_0, \mathbf{y}_0) \right]^{-1} \cdot \left[ \frac{\partial \mathbf{F}}{\partial \mathbf{x}}(\mathbf{x}_0, \mathbf{y}_0) \right]$$"""
            },
            {
                "secNumber": "8.5",
                "title": "Multiple Integrals, Fubini's Theorem & Change of Variables",
                "content": r"""### 1. Multiple Integrals in $\mathbb{R}^n$

Let $R = [a_1, b_1] \times [a_2, b_2] \times \dots \times [a_n, b_n]$ be a compact $n$-dimensional rectangle (box) in $\mathbb{R}^n$.
Partitions $P = P_1 \times \dots \times P_n$ divide $R$ into sub-rectangles $R_k$ of volume $\operatorname{vol}(R_k) = \prod_{j=1}^n \Delta x_{j, k}$.
Darboux upper and lower sums are defined analogously:
$$U(f, P) = \sum_k M_k \operatorname{vol}(R_k), \quad L(f, P) = \sum_k m_k \operatorname{vol}(R_k)$$
A bounded function $f: R \to \mathbb{R}$ is Riemann integrable if $\inf U(f, P) = \sup L(f, P)$, denoted $\int_R f(\mathbf{x}) \, d\mathbf{x}$.

---

### 2. Fubini's Theorem: Reduction to Iterated Integrals

> **Theorem 8.8 (Fubini's Theorem for Continuous Functions):**
> Let $A \subset \mathbb{R}^n$ and $B \subset \mathbb{R}^m$ be compact rectangles, and let $f: A \times B \to \mathbb{R}$ be continuous.
> Then:
> $$\int_{A \times B} f(\mathbf{x}, \mathbf{y}) \, d(\mathbf{x}, \mathbf{y}) = \int_A \left( \int_B f(\mathbf{x}, \mathbf{y}) \, d\mathbf{y} \right) d\mathbf{x} = \int_B \left( \int_A f(\mathbf{x}, \mathbf{y}) \, d\mathbf{x} \right) d\mathbf{y}$$
> The multiple integral equals the iterated single integrals, and the order of integration can be freely interchanged.

---

### 3. The Multivariable Change of Variables Theorem

> **Theorem 8.9 (Change of Variables Theorem in $\mathbb{R}^n$):**
> Let $U \subseteq \mathbb{R}^n$ be open, and let $\mathbf{g}: U \to \mathbb{R}^n$ be an injective $C^1$ mapping such that $\det J_{\mathbf{g}}(\mathbf{u}) \ne 0$ for all $\mathbf{u} \in U$.
> Let $E \subset U$ be a compact Jordan-measurable set, and let $f: \mathbf{g}(E) \to \mathbb{R}$ be continuous.
> Then:
> $$\int_{\mathbf{g}(E)} f(\mathbf{x}) \, d\mathbf{x} = \int_E f(\mathbf{g}(\mathbf{u})) \left| \det J_{\mathbf{g}}(\mathbf{u}) \right| \, d\mathbf{u}$$
> The absolute value of the Jacobian determinant $|\det J_{\mathbf{g}}(\mathbf{u})|$ represents the local volume distortion factor under the non-linear transformation $\mathbf{g}$."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational / Problem 8.1",
                "title": "Total Fréchet Derivative & Jacobian Matrix Computation",
                "statement": r"""Consider the vector-valued function $\mathbf{f}: \mathbb{R}^2 \to \mathbb{R}^2$ defined by:
$$\mathbf{f}(x, y) = \begin{pmatrix} e^{x y} \\ \sin(x^2 + y^2) \end{pmatrix}$$
1. Compute all four first-order partial derivatives $\frac{\partial f_i}{\partial x_j}$ for $(x, y) \in \mathbb{R}^2$.
2. Form the Jacobian matrix $J_{\mathbf{f}}(x, y)$ and evaluate it at the point $\mathbf{x}_0 = (1, 0)$.
3. Compute the linear Fréchet approximation $D\mathbf{f}(1, 0)(\mathbf{h})$ for $\mathbf{h} = (h_1, h_2)^T$ and approximate $\mathbf{f}(1.02, -0.01)$.""",
                "hints": [
                    "Recall that f_1(x, y) = e^(xy) and f_2(x, y) = sin(x^2 + y^2).",
                    "Linear approximation: f(x_0 + h) approx f(x_0) + J_f(x_0) h."
                ],
                "solution": r"""### 1. Partial Derivatives Computation
Let $f_1(x, y) = e^{x y}$ and $f_2(x, y) = \sin(x^2 + y^2)$.
- Component 1:
  $$\frac{\partial f_1}{\partial x} = y e^{x y}, \quad \frac{\partial f_1}{\partial y} = x e^{x y}$$
- Component 2:
  $$\frac{\partial f_2}{\partial x} = 2x \cos(x^2 + y^2), \quad \frac{\partial f_2}{\partial y} = 2y \cos(x^2 + y^2)$$

---

### 2. Jacobian Matrix Formation and Evaluation at $(1, 0)$
The general Jacobian matrix is:
$$J_{\mathbf{f}}(x, y) = \begin{pmatrix}
y e^{x y} & x e^{x y} \\
2x \cos(x^2 + y^2) & 2y \cos(x^2 + y^2)
\end{pmatrix}$$
Evaluating at $\mathbf{x}_0 = (1, 0)$:
$$f_1(1, 0) = e^0 = 1, \quad f_2(1, 0) = \sin(1 + 0) = \sin(1)$$
$$J_{\mathbf{f}}(1, 0) = \begin{pmatrix}
0 \cdot e^0 & 1 \cdot e^0 \\
2(1) \cos(1) & 2(0) \cos(1)
\end{pmatrix} = \begin{pmatrix}
0 & 1 \\
2 \cos(1) & 0
\end{pmatrix}$$

---

### 3. Fréchet Linear Approximation
The Fréchet differential applied to $\mathbf{h} = (h_1, h_2)^T$ is:
$$D\mathbf{f}(1, 0)(\mathbf{h}) = \begin{pmatrix} 0 & 1 \\ 2 \cos(1) & 0 \end{pmatrix} \begin{pmatrix} h_1 \\ h_2 \end{pmatrix} = \begin{pmatrix} h_2 \\ 2 h_1 \cos(1) \end{pmatrix}$$
The first-order affine approximation is:
$$\mathbf{f}(\mathbf{x}_0 + \mathbf{h}) \approx \mathbf{f}(\mathbf{x}_0) + D\mathbf{f}(\mathbf{x}_0)(\mathbf{h}) = \begin{pmatrix} 1 \\ \sin(1) \end{pmatrix} + \begin{pmatrix} h_2 \\ 2 h_1 \cos(1) \end{pmatrix}$$
For $\mathbf{x} = (1.02, -0.01)$, the displacement is $\mathbf{h} = (0.02, -0.01)^T$:
$$\mathbf{f}(1.02, -0.01) \approx \begin{pmatrix} 1 \\ \sin(1) \end{pmatrix} + \begin{pmatrix} -0.01 \\ 2(0.02) \cos(1) \end{pmatrix} = \begin{pmatrix} 0.99 \\ \sin(1) + 0.04 \cos(1) \end{pmatrix}$$
Using $\sin(1) \approx 0.84147$ and $\cos(1) \approx 0.54030$:
$$\mathbf{f}(1.02, -0.01) \approx \begin{pmatrix} 0.99 \\ 0.84147 + 0.02161 \end{pmatrix} = \begin{pmatrix} 0.9900 \\ 0.8631 \end{pmatrix} \quad \blacksquare$$"""
            },
            {
                "tier": "Advanced / Problem 8.2",
                "title": "Rigorous Proof of the Multivariable Chain Rule via Error Analysis",
                "statement": r"""Provide a complete, self-contained proof of the Multivariable Chain Rule (Theorem 8.5):
Let $\mathbf{f}: U \subseteq \mathbb{R}^n \to \mathbb{R}^m$ be differentiable at $\mathbf{x}_0 \in U$, and let $\mathbf{g}: V \subseteq \mathbb{R}^m \to \mathbb{R}^p$ be differentiable at $\mathbf{y}_0 = \mathbf{f}(\mathbf{x}_0) \in V$.
Prove that $\mathbf{h} = \mathbf{g} \circ \mathbf{f}$ is differentiable at $\mathbf{x}_0$, and:
$$D\mathbf{h}(\mathbf{x}_0) = D\mathbf{g}(\mathbf{y}_0) \circ D\mathbf{f}(\mathbf{x}_0)$$""",
                "hints": [
                    "Let A = Df(x_0) and B = Dg(y_0).",
                    "Write f(x_0 + h) - f(x_0) = A h + r_1(h) with ||r_1(h)|| / ||h|| -> 0.",
                    "Write g(y_0 + k) - g(y_0) = B k + r_2(k) with ||r_2(k)|| / ||k|| -> 0.",
                    "Substitute k = A h + r_1(h) and use the triangle inequality to bound the total error quotient."
                ],
                "solution": r"""### 1. Setting Up Linear Approximations and Remainder Terms
Let $A = D\mathbf{f}(\mathbf{x}_0) \in \mathcal{L}(\mathbb{R}^n, \mathbb{R}^m)$ and $B = D\mathbf{g}(\mathbf{y}_0) \in \mathcal{L}(\mathbb{R}^m, \mathbb{R}^p)$.
By differentiability of $\mathbf{f}$ at $\mathbf{x}_0$:
$$\mathbf{f}(\mathbf{x}_0 + \mathbf{h}) - \mathbf{f}(\mathbf{x}_0) = A \mathbf{h} + \mathbf{r}_1(\mathbf{h}), \quad \text{where } \lim_{\mathbf{h} \to \mathbf{0}} \frac{\|\mathbf{r}_1(\mathbf{h})\|}{\|\mathbf{h}\|} = 0$$
Let $\mathbf{k} = \mathbf{f}(\mathbf{x}_0 + \mathbf{h}) - \mathbf{f}(\mathbf{x}_0) = A \mathbf{h} + \mathbf{r}_1(\mathbf{h})$.
Since differentiability implies continuity (Theorem 8.2), $\lim_{\mathbf{h} \to \mathbf{0}} \mathbf{k} = \mathbf{0}$.
By differentiability of $\mathbf{g}$ at $\mathbf{y}_0$:
$$\mathbf{g}(\mathbf{y}_0 + \mathbf{k}) - \mathbf{g}(\mathbf{y}_0) = B \mathbf{k} + \mathbf{r}_2(\mathbf{k}), \quad \text{where } \lim_{\mathbf{k} \to \mathbf{0}} \frac{\|\mathbf{r}_2(\mathbf{k})\|}{\|\mathbf{k}\|} = 0$$
Define the error rate function $\eta(\mathbf{k})$ for $\mathbf{k} \ne \mathbf{0}$ by $\eta(\mathbf{k}) = \frac{\|\mathbf{r}_2(\mathbf{k})\|}{\|\mathbf{k}\|}$ and $\eta(\mathbf{0}) = 0$.
Then $\lim_{\mathbf{k} \to \mathbf{0}} \eta(\mathbf{k}) = 0$, and $\|\mathbf{r}_2(\mathbf{k})\| = \eta(\mathbf{k}) \|\mathbf{k}\|$ for all $\mathbf{k}$.

---

### 2. Expanding the Composite Difference
Now examine the composite increment:
$$\begin{aligned}
\mathbf{h}(\mathbf{x}_0 + \mathbf{h}) - \mathbf{h}(\mathbf{x}_0) &= \mathbf{g}(\mathbf{f}(\mathbf{x}_0 + \mathbf{h})) - \mathbf{g}(\mathbf{f}(\mathbf{x}_0)) \\
&= \mathbf{g}(\mathbf{y}_0 + \mathbf{k}) - \mathbf{g}(\mathbf{y}_0) \\
&= B \mathbf{k} + \mathbf{r}_2(\mathbf{k}) \\
&= B(A \mathbf{h} + \mathbf{r}_1(\mathbf{h})) + \mathbf{r}_2(\mathbf{k}) \\
&= (B A) \mathbf{h} + B \mathbf{r}_1(\mathbf{h}) + \mathbf{r}_2(\mathbf{k})
\end{aligned}$$
The candidate derivative is the linear operator $B A = D\mathbf{g}(\mathbf{y}_0) \circ D\mathbf{f}(\mathbf{x}_0)$.
The total error term is:
$$\mathbf{R}(\mathbf{h}) = B \mathbf{r}_1(\mathbf{h}) + \mathbf{r}_2(\mathbf{k})$$

---

### 3. Rigorous Error Bound Verification
We must show that $\lim_{\mathbf{h} \to \mathbf{0}} \frac{\|\mathbf{R}(\mathbf{h})\|}{\|\mathbf{h}\|} = 0$.
Applying the Triangle Inequality:
$$\frac{\|\mathbf{R}(\mathbf{h})\|}{\|\mathbf{h}\|} \le \frac{\|B \mathbf{r}_1(\mathbf{h})\|}{\|\mathbf{h}\|} + \frac{\|\mathbf{r}_2(\mathbf{k})\|}{\|\mathbf{h}\|}$$
- **First term:** By the operator norm bound $\|B \mathbf{v}\| \le \|B\|_{\text{op}} \|\mathbf{v}\|$:
  $$\frac{\|B \mathbf{r}_1(\mathbf{h})\|}{\|\mathbf{h}\|} \le \|B\|_{\text{op}} \frac{\|\mathbf{r}_1(\mathbf{h})\|}{\|\mathbf{h}\|} \to \|B\|_{\text{op}} \cdot 0 = 0 \quad \text{as } \mathbf{h} \to \mathbf{0}$$
- **Second term:** Recall $\|\mathbf{r}_2(\mathbf{k})\| = \eta(\mathbf{k}) \|\mathbf{k}\|$, so:
  $$\frac{\|\mathbf{r}_2(\mathbf{k})\|}{\|\mathbf{h}\|} = \eta(\mathbf{k}) \frac{\|\mathbf{k}\|}{\|\mathbf{h}\|}$$
  Now bound the ratio $\frac{\|\mathbf{k}\|}{\|\mathbf{h}\|}$:
  $$\frac{\|\mathbf{k}\|}{\|\mathbf{h}\|} = \frac{\|A \mathbf{h} + \mathbf{r}_1(\mathbf{h})\|}{\|\mathbf{h}\|} \le \frac{\|A \mathbf{h}\|}{\|\mathbf{h}\|} + \frac{\|\mathbf{r}_1(\mathbf{h})\|}{\|\mathbf{h}\|} \le \|A\|_{\text{op}} + \frac{\|\mathbf{r}_1(\mathbf{h})\|}{\|\mathbf{h}\|}$$
  As $\mathbf{h} \to \mathbf{0}$, $\frac{\|\mathbf{r}_1(\mathbf{h})\|}{\|\mathbf{h}\|} \to 0$, so for all sufficiently small $\mathbf{h}$:
  $$\frac{\|\mathbf{k}\|}{\|\mathbf{h}\|} \le \|A\|_{\text{op}} + 1 < \infty$$
  Furthermore, since $\lim_{\mathbf{h} \to \mathbf{0}} \mathbf{k} = \mathbf{0}$, we have $\lim_{\mathbf{h} \to \mathbf{0}} \eta(\mathbf{k}) = 0$.
  Therefore:
  $$\lim_{\mathbf{h} \to \mathbf{0}} \frac{\|\mathbf{r}_2(\mathbf{k})\|}{\|\mathbf{h}\|} \le \lim_{\mathbf{h} \to \mathbf{0}} \left[ \eta(\mathbf{k}) (\|A\|_{\text{op}} + 1) \right] = 0 \cdot (\|A\|_{\text{op}} + 1) = 0$$

Combining both terms:
$$\lim_{\mathbf{h} \to \mathbf{0}} \frac{\|\mathbf{R}(\mathbf{h})\|}{\|\mathbf{h}\|} = 0$$
This rigorously proves that $\mathbf{h} = \mathbf{g} \circ \mathbf{f}$ is differentiable at $\mathbf{x}_0$, and $D\mathbf{h}(\mathbf{x}_0) = D\mathbf{g}(\mathbf{y}_0) \circ D\mathbf{f}(\mathbf{x}_0)$. $\blacksquare$"""
            },
            {
                "tier": "Honors / Problem 8.3",
                "title": "Comprehensive Proof of the Implicit Function Theorem in R^2 to R",
                "statement": r"""1. State the Implicit Function Theorem for a scalar equation $F(x, y) = 0$ in $\mathbb{R}^2$.
2. Provide a rigorous, complete proof using the Mean Value Theorem, Bolzano's Intermediate Value Theorem, and the single-variable Inverse Function Theorem.
3. Apply the theorem to the algebraic equation:
   $$F(x, y) = x^3 + y^3 - 3 x y = 0 \quad \text{(Folium of Descartes)}$$
   at the point $(x_0, y_0) = \left(\frac{3}{2}, \frac{3}{2}\right)$. Verify that $y$ can be expressed as a function of $x$ and compute $\frac{dy}{dx}$ at that point.""",
                "hints": [
                    "For part 2, assume F_y(x_0, y_0) > 0. Use continuity to find a rectangle where F_y > 0.",
                    "By IVT, for each x near x_0, there is a unique y with F(x, y) = 0.",
                    "Use differentiability to calculate the derivative dy/dx = - F_x / F_y."
                ],
                "solution": r"""### 1. Statement of the Implicit Function Theorem in $\mathbb{R}^2$
Let $U \subseteq \mathbb{R}^2$ be open, and let $F: U \to \mathbb{R}$ be $C^1(U)$.
Suppose $(x_0, y_0) \in U$ satisfies:
1. $F(x_0, y_0) = 0$.
2. $\frac{\partial F}{\partial y}(x_0, y_0) \ne 0$.
Then there exists an open interval $I = (x_0 - \delta, x_0 + \delta)$ and an open interval $J = (y_0 - \epsilon, y_0 + \epsilon)$ such that for every $x \in I$, there exists a **unique** $y = g(x) \in J$ satisfying $F(x, g(x)) = 0$.
Furthermore, $g: I \to J$ is $C^1$ and:
$$g'(x) = -\frac{\frac{\partial F}{\partial x}(x, g(x))}{\frac{\partial F}{\partial y}(x, g(x))}$$

---

### 2. Rigorous Proof

Assume without loss of generality that $\frac{\partial F}{\partial y}(x_0, y_0) > 0$.
- **Step 1: Constructing the isolator rectangle.**
  Since $F \in C^1$, $\frac{\partial F}{\partial y}$ is continuous.
  There exists $\epsilon > 0$ such that $\frac{\partial F}{\partial y}(x_0, y) > 0$ for all $y \in [y_0 - \epsilon, y_0 + \epsilon]$.
  Thus the one-variable function $y \mapsto F(x_0, y)$ is strictly increasing on $[y_0 - \epsilon, y_0 + \epsilon]$.
  Since $F(x_0, y_0) = 0$:
  $$F(x_0, y_0 - \epsilon) < 0 \quad \text{and} \quad F(x_0, y_0 + \epsilon) > 0$$
  By continuity of $x \mapsto F(x, y)$, there exists $\delta > 0$ such that for all $x \in (x_0 - \delta, x_0 + \delta)$:
  $$F(x, y_0 - \epsilon) < 0 \quad \text{and} \quad F(x, y_0 + \epsilon) > 0$$
  Furthermore, choose $\delta$ small enough that $\frac{\partial F}{\partial y}(x, y) > 0$ on the entire rectangle $R = (x_0 - \delta, x_0 + \delta) \times [y_0 - \epsilon, y_0 + \epsilon]$.

- **Step 2: Existence and uniqueness of $g(x)$.**
  Fix any $x \in (x_0 - \delta, x_0 + \delta)$.
  The function $y \mapsto F(x, y)$ is continuous on $[y_0 - \epsilon, y_0 + \epsilon]$ and takes values of opposite signs at the endpoints: $F(x, y_0 - \epsilon) < 0 < F(x, y_0 + \epsilon)$.
  By Bolzano's Intermediate Value Theorem (Theorem 5.6), there exists at least one $y \in (y_0 - \epsilon, y_0 + \epsilon)$ such that $F(x, y) = 0$.
  Since $\frac{\partial F}{\partial y} > 0$ on $R$, $y \mapsto F(x, y)$ is strictly increasing, so this zero is **unique**!
  Define $g(x) = y$.

- **Step 3: Differentiability of $g(x)$.**
  Let $x, x + h \in (x_0 - \delta, x_0 + \delta)$ and let $k = g(x + h) - g(x)$.
  Then $F(x + h, g(x) + k) = 0$ and $F(x, g(x)) = 0$.
  By the multivariable Mean Value Theorem:
  $$0 = F(x + h, g(x) + k) - F(x, g(x)) = \frac{\partial F}{\partial x}(\xi, \eta) h + \frac{\partial F}{\partial y}(\xi, \eta) k$$
  where $(\xi, \eta)$ lies on the segment connecting $(x, g(x))$ and $(x+h, g(x)+k)$.
  Solving for the difference quotient:
  $$\frac{k}{h} = \frac{g(x + h) - g(x)}{h} = -\frac{\frac{\partial F}{\partial x}(\xi, \eta)}{\frac{\partial F}{\partial y}(\xi, \eta)}$$
  As $h \to 0$, $k \to 0$ by continuity, so $(\xi, \eta) \to (x, g(x))$.
  Since the partial derivatives are continuous and $\frac{\partial F}{\partial y} \ne 0$:
  $$g'(x) = \lim_{h \to 0} \frac{g(x + h) - g(x)}{h} = -\frac{\frac{\partial F}{\partial x}(x, g(x))}{\frac{\partial F}{\partial y}(x, g(x))} \quad \blacksquare$$

---

### 3. Application to the Folium of Descartes
$F(x, y) = x^3 + y^3 - 3 x y = 0$ at $\left(\frac{3}{2}, \frac{3}{2}\right)$.
Verify the point satisfies the equation:
$$\left(\frac{3}{2}\right)^3 + \left(\frac{3}{2}\right)^3 - 3\left(\frac{3}{2}\right)\left(\frac{3}{2}\right) = \frac{27}{8} + \frac{27}{8} - \frac{27}{4} = \frac{54}{8} - \frac{54}{8} = 0$$
Compute partial derivatives:
$$\frac{\partial F}{\partial x} = 3x^2 - 3y, \quad \frac{\partial F}{\partial y} = 3y^2 - 3x$$
Evaluating at $(x_0, y_0) = (3/2, 3/2)$:
$$\frac{\partial F}{\partial x}\left(\frac{3}{2}, \frac{3}{2}\right) = 3\left(\frac{9}{4}\right) - 3\left(\frac{3}{2}\right) = \frac{27}{4} - \frac{18}{4} = \frac{9}{4}$$
$$\frac{\partial F}{\partial y}\left(\frac{3}{2}, \frac{3}{2}\right) = 3\left(\frac{9}{4}\right) - 3\left(\frac{3}{2}\right) = \frac{27}{4} - \frac{18}{4} = \frac{9}{4} \ne 0$$
Since $\frac{\partial F}{\partial y} = \frac{9}{4} \ne 0$, the hypotheses of the Implicit Function Theorem are satisfied.
Thus $y$ can be expressed as a unique $C^1$ function $y = g(x)$ in a neighborhood of $x = 3/2$.
The derivative is:
$$\frac{dy}{dx}\left(\frac{3}{2}\right) = -\frac{\frac{\partial F}{\partial x}}{\frac{\partial F}{\partial y}} = -\frac{9/4}{9/4} = -1 \quad \blacksquare$$"""
            }
        ]
    }
    return u8

if __name__ == "__main__":
    u = get_unit8()
    print(f"Loaded Unit 8: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
