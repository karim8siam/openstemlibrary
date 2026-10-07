# -*- coding: utf-8 -*-
"""
build_unit2.py
Constructs Unit 2: Polynomial Interpolation, Finite Differences & Approximation Theory
"""

def get_unit2():
    u2 = {
        "number": 2,
        "title": "Polynomial Interpolation, Finite Differences & Approximation Theory",
        "leadSummary": "Lagrange interpolation basis, Cauchy remainder error theorem, Newton's divided difference tables, finite difference operators (forward, backward, central), and Runge's phenomenon with Chebyshev optimal nodes.",
        "simulations": ["sim_na_interpolation"],
        "sections": [
            {
                "secNumber": "2.1",
                "title": "Foundations of Interpolation: Existence, Uniqueness & The Lagrange Formulation",
                "content": r"""### 1. The Polynomial Interpolation Problem

Let $f: [a, b] \to \mathbb{R}$ be a continuous function. Suppose we are given $n + 1$ distinct nodes:
$$a \le x_0 < x_1 < x_2 < \dots < x_n \le b$$
along with corresponding function values $y_i = f(x_i)$ for $i = 0, 1, \dots, n$.

The **Polynomial Interpolation Problem** seeks a polynomial $P_n(x) \in \mathbb{P}_n$ of degree at most $n$:
$$P_n(x) = c_0 + c_1 x + c_2 x^2 + \dots + c_n x^n$$
satisfying the $n + 1$ interpolation conditions:
$$P_n(x_i) = y_i, \quad i = 0, 1, \dots, n$$

#### Theorem 2.1 (Existence and Uniqueness of the Interpolating Polynomial):
Given $n + 1$ distinct points $(x_0, y_0), (x_1, y_1), \dots, (x_n, y_n)$, there exists one and only one polynomial $P_n \in \mathbb{P}_n$ of degree at most $n$ passing through all $n + 1$ points.

*Rigorous Proof:*
Expressing the interpolation conditions in matrix form:
$$\begin{pmatrix}
1 & x_0 & x_0^2 & \dots & x_0^n \\
1 & x_1 & x_1^2 & \dots & x_1^n \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_n & x_n^2 & \dots & x_n^n
\end{pmatrix}
\begin{pmatrix} c_0 \\ c_1 \\ \vdots \\ c_n \end{pmatrix} =
\begin{pmatrix} y_0 \\ y_1 \\ \vdots \\ y_n \end{pmatrix}$$
The coefficient matrix $V$ is the **Vandermonde Matrix**. Its determinant satisfies:
$$\det(V) = \prod_{0 \le j < i \le n} (x_i - x_j)$$
Because the nodes $x_i$ are pairwise distinct, $x_i - x_j \ne 0$ for all $i > j$. Consequently, $\det(V) \ne 0$. By Cramer's Rule, $V$ is non-singular and invertible, which guarantees that the coefficient vector $\vec{c} = V^{-1} \vec{y}$ exists and is strictly unique. $\blacksquare$

---

### 2. The Lagrange Basis Formulation

Direct matrix inversion of the Vandermonde matrix is computationally expensive ($\mathcal{O}(n^3)$) and notoriously ill-conditioned. The **Lagrange form** provides an explicit analytical representation by introducing cardinal basis polynomials.

#### Definition 2.1 (Cardinal Lagrange Basis Polynomials):
For $n + 1$ distinct nodes $x_0, x_1, \dots, x_n$, the $k$-th Lagrange basis polynomial $L_{n,k}(x)$ of degree $n$ is defined by:

$$L_{n,k}(x) = \prod_{\substack{j=0 \\ j \ne k}}^n \frac{x - x_j}{x_k - x_j} = \frac{(x - x_0)(x - x_1)\dots(x - x_{k-1})(x - x_{k+1})\dots(x - x_n)}{(x_k - x_0)(x_k - x_1)\dots(x_k - x_{k-1})(x_k - x_{k+1})\dots(x_k - x_n)}$$

The Lagrange polynomials satisfy the fundamental **Kronecker delta property**:
$$L_{n,k}(x_i) = \delta_{ik} = \begin{cases} 1, & \text{if } i = k \\ 0, & \text{if } i \ne k \end{cases}$$

The interpolating polynomial is simply the linear combination:
$$P_n(x) = \sum_{k=0}^n y_k L_{n,k}(x) = \sum_{k=0}^n f(x_k) L_{n,k}(x)$$

---

### 3. Rigorous Error Analysis: The Cauchy Remainder Theorem

#### Theorem 2.2 (Cauchy Interpolation Remainder Formula):
Let $f \in C^{n+1}[a, b]$ and let $P_n \in \mathbb{P}_n$ interpolate $f$ at $n + 1$ distinct nodes $x_0, x_1, \dots, x_n \in [a, b]$. For any point $x \in [a, b]$:

$$f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} \prod_{k=0}^n (x - x_k)$$

where $\xi = \xi(x)$ is a number lying strictly in the interior of the interval spanned by $x_0, x_1, \dots, x_n$ and $x$.

*Rigorous Proof:*
If $x = x_i$ for any node, both sides are $0$ and equality holds trivially. Assume $x \ne x_i$ for all $i$. Fix $x$ and define the node product polynomial:
$$w(t) = \prod_{k=0}^n (t - x_k)$$
Notice that $w(x) \ne 0$ since $x$ is not a node. Define the auxiliary error function $g: [a, b] \to \mathbb{R}$:
$$g(t) = f(t) - P_n(t) - \frac{f(x) - P_n(x)}{w(x)} w(t)$$
Now inspect the zeros of $g(t)$:
1. For each node $t = x_i$ ($i = 0, \dots, n$):
   $$g(x_i) = f(x_i) - P_n(x_i) - \frac{f(x) - P_n(x)}{w(x)} w(x_i) = 0 - 0 = 0$$
2. For $t = x$:
   $$g(x) = f(x) - P_n(x) - \frac{f(x) - P_n(x)}{w(x)} w(x) = 0$$
Thus, $g(t)$ possesses at least $n + 2$ distinct zeros in $[a, b]$.

Since $f \in C^{n+1}[a, b]$ and $P_n, w$ are polynomials, $g \in C^{n+1}[a, b]$.
Applying **Rolle's Theorem** successively:
- $g'(t)$ has at least $n + 1$ zeros between the $n + 2$ zeros of $g(t)$.
- $g''(t)$ has at least $n$ zeros.
- Repeating this $n+1$ times, the $(n+1)$-th derivative $g^{(n+1)}(t)$ has at least one zero $\xi$ in the interior of the domain.

Now compute $g^{(n+1)}(t)$:
$$\frac{d^{n+1}}{dt^{n+1}} [P_n(t)] = 0 \quad (\text{since } \deg P_n \le n)$$
$$\frac{d^{n+1}}{dt^{n+1}} [w(t)] = \frac{d^{n+1}}{dt^{n+1}} [t^{n+1} + \dots] = (n+1)!$$
Therefore:
$$g^{(n+1)}(t) = f^{(n+1)}(t) - 0 - \frac{f(x) - P_n(x)}{w(x)} (n+1)!$$
Evaluating at the zero $t = \xi$:
$$0 = g^{(n+1)}(\xi) = f^{(n+1)}(\xi) - \frac{f(x) - P_n(x)}{w(x)} (n+1)!$$
Rearranging terms yields:
$$f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} w(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} \prod_{k=0}^n (x - x_k) \quad \blacksquare$$"""
            },
            {
                "secNumber": "2.2",
                "title": "Newton's Divided Differences & Incremental Polynomial Representation",
                "content": r"""### 1. Motivation for the Divided Difference Formulation

While the Lagrange form is mathematically elegant, adding a new data point $(x_{n+1}, y_{n+1})$ requires completely recalculating all $n + 2$ basis polynomials $L_{n+1, k}(x)$. **Newton's Divided Differences** overcomes this limitation by expressing $P_n(x)$ in a triangular, incremental hierarchical basis:

$$P_n(x) = a_0 + a_1(x - x_0) + a_2(x - x_0)(x - x_1) + \dots + a_n(x - x_0)(x - x_1)\dots(x - x_{n-1})$$

Adding a new node requires simply computing one additional leading coefficient $a_{n+1}$.

---

### 2. Recursive Definition of Divided Differences

#### Definition 2.2:
The divided differences of a function $f$ with respect to distinct nodes $x_0, x_1, \dots, x_n$ are defined recursively:
- **Zeroth Divided Difference:**
  $$f[x_i] = f(x_i)$$
- **First Divided Difference:**
  $$f[x_i, x_{i+1}] = \frac{f[x_{i+1}] - f[x_i]}{x_{i+1} - x_i}$$
- **Second Divided Difference:**
  $$f[x_i, x_{i+1}, x_{i+2}] = \frac{f[x_{i+1}, x_{i+2}] - f[x_i, x_{i+1}]}{x_{i+2} - x_i}$$
- **General $k$-th Divided Difference:**
  $$f[x_i, x_{i+1}, \dots, x_{i+k}] = \frac{f[x_{i+1}, \dots, x_{i+k}] - f[x_i, \dots, x_{i+k-1}]}{x_{i+k} - x_i}$$

The coefficients $a_k$ in the Newton interpolating polynomial are precisely the top-diagonal entries of the divided difference table: $a_k = f[x_0, x_1, \dots, x_k]$.

$$\boxed{P_n(x) = f[x_0] + \sum_{k=1}^n f[x_0, x_1, \dots, x_k] \prod_{j=0}^{k-1} (x - x_j)}$$

---

### 3. Mean Value Theorem for Divided Differences

#### Theorem 2.3:
Let $f \in C^k[a, b]$ and let $x_0, x_1, \dots, x_k$ be distinct nodes in $[a, b]$. Then there exists a point $\xi$ in the open interval $(\min x_i, \max x_i)$ such that:

$$f[x_0, x_1, \dots, x_k] = \frac{f^{(k)}(\xi)}{k!}$$

*Proof:*
Let $P_k(x)$ be the polynomial of degree $k$ interpolating $f$ at $x_0, \dots, x_k$. The leading coefficient of $P_k(x)$ is $f[x_0, \dots, x_k]$. By Cauchy's remainder theorem:
$$f(x) - P_k(x) = \frac{f^{(k+1)}(\xi(x))}{(k+1)!} \prod_{j=0}^k (x - x_j)$$
Now let $P_{k-1}(x)$ interpolate $f$ at $x_0, \dots, x_{k-1}$. Then $P_k(x) - P_{k-1}(x) = f[x_0, \dots, x_k] \prod_{j=0}^{k-1} (x - x_j)$. Evaluating the error at $x = x_k$ and applying the generalized Rolle's theorem proves $f[x_0, \dots, x_k] = \frac{f^{(k)}(\xi)}{k!}$. $\blacksquare$"""
            },
            {
                "secNumber": "2.3",
                "title": "Finite Difference Calculus: Operators, Gregory-Newton Formulas & Central Differences",
                "content": r"""### 1. Equispaced Grid Finite Difference Operators

When nodes are uniformly spaced with constant step size $h$:
$$x_k = x_0 + k h, \quad k = 0, 1, 2, \dots$$
divided differences simplify into finite difference operator algebra.

#### Definitions of Core Operators:
1. **Forward Difference Operator ($\Delta$):**
   $$\Delta f_k = f_{k+1} - f_k$$
   Higher powers: $\Delta^n f_k = \Delta(\Delta^{n-1} f_k) = \sum_{j=0}^n (-1)^{n-j} \binom{n}{j} f_{k+j}$.

2. **Backward Difference Operator ($\nabla$):**
   $$\nabla f_k = f_k - f_{k-1}$$
   Higher powers: $\nabla^n f_k = \sum_{j=0}^n (-1)^j \binom{n}{j} f_{k-j}$.

3. **Central Difference Operator ($\delta$):**
   $$\delta f_k = f_{k+1/2} - f_{k-1/2}, \quad \delta^2 f_k = f_{k+1} - 2f_k + f_{k-1}$$

4. **Shift Operator ($E$):**
   $$E f_k = f_{k+1}, \quad E^s f(x) = f(x + s h)$$

5. **Averaging Operator ($\mu$):**
   $$\mu f_k = \frac{1}{2}(f_{k+1/2} + f_{k-1/2})$$

#### Fundamental Operator Identities:
From Taylor series: $E f(x) = f(x + h) = \sum \frac{h^k D^k}{k!} f(x) = e^{hD} f(x)$, where $D = \frac{d}{dx}$.
$$E = 1 + \Delta = (1 - \nabla)^{-1} = e^{hD}$$
$$\Delta = E - 1, \quad \nabla = 1 - E^{-1}, \quad \delta = E^{1/2} - E^{-1/2}$$

---

### 2. Newton-Gregory Forward and Backward Formulas

Let $x = x_0 + s h$, so $s = \frac{x - x_0}{h}$ is the non-dimensionalized step parameter.

#### The Newton-Gregory Forward Interpolation Formula:
Suitable for interpolating near the beginning of a tabulated dataset:

$$P_n(x_0 + s h) = \sum_{k=0}^n \binom{s}{k} \Delta^k f_0 = f_0 + s \Delta f_0 + \frac{s(s-1)}{2!} \Delta^2 f_0 + \dots + \frac{s(s-1)\dots(s-k+1)}{k!} \Delta^k f_0$$

#### The Newton-Gregory Backward Interpolation Formula:
Suitable for interpolating near the end of a dataset (or for extrapolation):
Let $x = x_n + s h$, so $s = \frac{x - x_n}{h}$:

$$P_n(x_n + s h) = \sum_{k=0}^n (-1)^k \binom{-s}{k} \nabla^k f_n = f_n + s \nabla f_n + \frac{s(s+1)}{2!} \nabla^2 f_n + \dots + \frac{s(s+1)\dots(s+k-1)}{k!} \nabla^k f_n$$

---

### 3. Central Difference Formulas: Stirling & Bessel

For interpolation near the center of a table, forward and backward formulas exhibit asymmetric error propagation. Central difference formulas provide optimal symmetric precision:
- **Stirling's Formula:** Averages forward and backward expressions about the central node:
  $$P(x_0 + s h) = f_0 + s (\mu \delta f_0) + \frac{s^2}{2!} \delta^2 f_0 + \frac{s(s^2 - 1)}{3!} (\mu \delta^3 f_0) + \frac{s^2(s^2 - 1)}{4!} \delta^4 f_0 + \dots$$
- **Bessel's Formula:** Best suited for $s$ near $0.5$ (midway between nodes):
  $$P(x_0 + s h) = \mu f_{1/2} + (s - 0.5) \delta f_{1/2} + \frac{s(s-1)}{2!} \mu \delta^2 f_{1/2} + \dots$$"""
            },
            {
                "secNumber": "2.4",
                "title": "Runge's Phenomenon, Lebesgue Constants & Chebyshev Optimal Nodes",
                "content": r"""### 1. The Catastrophe of High-Degree Equispaced Interpolation

It is a common intuition that increasing the degree $n$ of an interpolating polynomial on a uniform grid should improve accuracy. In 1901, **Carl Runge** discovered that this intuition fails catastrophically.

Consider the **Runge Function** on $[-1, 1]$:
$$f(x) = \frac{1}{1 + 25 x^2}$$
If $P_n(x)$ interpolates $f$ at $n + 1$ equispaced nodes $x_k = -1 + \frac{2k}{n}$, then as $n \to \infty$:
$$\lim_{n \to \infty} \max_{x \in [-1, 1]} |f(x) - P_n(x)| = \infty$$
Near the boundaries $x = \pm 1$, the polynomial oscillations explode exponentially.

*Mathematical Origin:*
In Cauchy's remainder formula:
$$f(x) - P_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} w_n(x), \quad w_n(x) = \prod_{k=0}^n (x - x_k)$$
On uniform grids, the node product polynomial $w_n(x)$ is highly non-uniform: it is small near the center $x = 0$, but near the boundaries $x \approx \pm 1$, it attains gigantic peaks of order $\mathcal{O}(n^{-1} e^n)$. Combined with the singularity of $f(z)$ in the complex plane at $z = \pm \frac{i}{5}$ (which lies inside the equispaced convergence ellipse), the error diverges.

---

### 2. Chebyshev Polynomials and Optimal Node Clustering

To suppress boundary oscillations, we must choose nodes $x_k$ that minimize the maximum norm of the node product polynomial:
$$\min_{x_0, \dots, x_n \in [-1, 1]} \max_{x \in [-1, 1]} \left| \prod_{k=0}^n (x - x_k) \right|$$

#### Definition 2.3 (Chebyshev Polynomials of the First Kind):
The Chebyshev polynomials $T_n(x)$ are defined on $[-1, 1]$ by:
$$T_n(x) = \cos(n \arccos x), \quad x \in [-1, 1]$$
They satisfy the three-term recurrence relation:
$$T_0(x) = 1, \quad T_1(x) = x, \quad T_{n+1}(x) = 2x T_n(x) - T_{n-1}(x)$$
The leading coefficient of $T_n(x)$ is $2^{n-1}$ for $n \ge 1$.

#### Theorem 2.4 (The Minimax Property of Chebyshev Polynomials):
Among all monic polynomials of degree $n$ on $[-1, 1]$, the monic Chebyshev polynomial $\tilde{T}_n(x) = \frac{T_n(x)}{2^{n-1}}$ has the strictly smallest maximum absolute value on $[-1, 1]$:

$$\max_{x \in [-1, 1]} |\tilde{T}_n(x)| = \frac{1}{2^{n-1}}$$

#### Theorem 2.5 (Chebyshev Optimal Interpolation Nodes):
The roots of $T_{n+1}(x) = 0$ provide the optimal interpolation nodes on $[-1, 1]$:

$$x_k = \cos\left( \frac{2k + 1}{2n + 2} \pi \right), \quad k = 0, 1, \dots, n$$

These nodes are densely clustered near the endpoints $x = \pm 1$ and spread apart near the center $x = 0$. Using Chebyshev nodes, the Lebesgue constant grows only logarithmically ($\Lambda_n \sim \frac{2}{\pi} \ln n$), completely eliminating Runge's phenomenon and guaranteeing uniform convergence for any analytic function!"""
            }
        ],
        "problems": [
            {
                "id": "na-prob-2-1",
                "tier": 1,
                "difficultyLabel": "Tier 1 • Foundational",
                "title": "Lagrange Polynomial & Newton Divided Difference Evaluation",
                "statement": r"Given the dataset: $(-1, 3), (0, -1), (1, 1), (2, 9)$:<br>1. Construct the cardinal Lagrange basis polynomials $L_{3, k}(x)$ for $k = 0, 1, 2, 3$ and write the complete interpolating polynomial $P_3(x)$.<br>2. Construct the Newton divided difference table for the dataset and verify that the resulting polynomial matches the Lagrange form identically.<br>3. Estimate the value of $f(0.5)$.",
                "solution": r"""<b>Step 1: Construct Cardinal Lagrange Basis Polynomials</b><br>
Nodes: $x_0 = -1, x_1 = 0, x_2 = 1, x_3 = 2$. Values: $y_0 = 3, y_1 = -1, y_2 = 1, y_3 = 9$.<br>
- $L_{3,0}(x) = \frac{(x - 0)(x - 1)(x - 2)}{(-1 - 0)(-1 - 1)(-1 - 2)} = \frac{x(x - 1)(x - 2)}{(-1)(-2)(-3)} = -\frac{x(x^2 - 3x + 2)}{6} = -\frac{x^3 - 3x^2 + 2x}{6}$.<br>
- $L_{3,1}(x) = \frac{(x + 1)(x - 1)(x - 2)}{(0 + 1)(0 - 1)(0 - 2)} = \frac{(x^2 - 1)(x - 2)}{(1)(-1)(-2)} = \frac{x^3 - 2x^2 - x + 2}{2}$.<br>
- $L_{3,2}(x) = \frac{(x + 1)(x - 0)(x - 2)}{(1 + 1)(1 - 0)(1 - 2)} = \frac{x(x + 1)(x - 2)}{(2)(1)(-1)} = -\frac{x^3 - x^2 - 2x}{2}$.<br>
- $L_{3,3}(x) = \frac{(x + 1)(x - 0)(x - 1)}{(2 + 1)(2 - 0)(2 - 1)} = \frac{x(x^2 - 1)}{(3)(2)(1)} = \frac{x^3 - x}{6}$.<br>
Combining with values:
$$P_3(x) = 3 L_{3,0}(x) - 1 L_{3,1}(x) + 1 L_{3,2}(x) + 9 L_{3,3}(x)$$
$$= -\frac{x^3 - 3x^2 + 2x}{2} - \frac{x^3 - 2x^2 - x + 2}{2} - \frac{x^3 - x^2 - 2x}{2} + \frac{3(x^3 - x)}{2}$$
Numerator: $(-x^3 + 3x^2 - 2x) + (-x^3 + 2x^2 + x - 2) + (-x^3 + x^2 + 2x) + (3x^3 - 3x)$<br>
$x^3$ coefficient: $(-1 - 1 - 1 + 3) / 2 = 0 / 2 = 0$. (Notice the degree reduces to 2!)<br>
$x^2$ coefficient: $(3 + 2 + 1 + 0) / 2 = 6 / 2 = 3$.<br>
$x$ coefficient: $(-2 + 1 + 2 - 3) / 2 = -2 / 2 = -1$.<br>
Constant term: $(-2) / 2 = -1$.<br>
Thus: $P_3(x) = 2x^3 + \dots = 3x^2 - x - 1$.
<br><br>
<b>Step 2: Construct Newton's Divided Difference Table</b><br>
- $x_0 = -1, f[x_0] = 3$<br>
- $x_1 = 0, f[x_1] = -1 \implies f[x_0, x_1] = \frac{-1 - 3}{0 - (-1)} = -4$<br>
- $x_2 = 1, f[x_2] = 1 \implies f[x_1, x_2] = \frac{1 - (-1)}{1 - 0} = 2$<br>
- $x_3 = 2, f[x_3] = 9 \implies f[x_2, x_3] = \frac{9 - 1}{2 - 1} = 8$<br>
Second divided differences:<br>
- $f[x_0, x_1, x_2] = \frac{2 - (-4)}{1 - (-1)} = \frac{6}{2} = 3$<br>
- $f[x_1, x_2, x_3] = \frac{8 - 2}{2 - 0} = \frac{6}{2} = 3$<br>
Third divided difference:<br>
- $f[x_0, x_1, x_2, x_3] = \frac{3 - 3}{2 - (-1)} = \frac{0}{3} = 0$<br>
Using the Newton formula:
$$P_3(x) = f[x_0] + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1) + f[x_0, x_1, x_2, x_3](x - x_0)(x - x_1)(x - x_2)$$
$$P_3(x) = 3 - 4(x + 1) + 3(x + 1)(x - 0) + 0 = 3 - 4x - 4 + 3x^2 + 3x = 3x^2 - x - 1$$
Both methods match identically!
<br><br>
<b>Step 3: Evaluate at $x = 0.5$</b><br>
$$P_3(0.5) = 3(0.5)^2 - (0.5) - 1 = 3(0.25) - 0.5 - 1 = 0.75 - 1.5 = -0.75$$""",
                "answer": r"Interpolating polynomial: $P_3(x) = 3x^2 - x - 1$. Estimated value: $f(0.5) = -0.75$."
            },
            {
                "id": "na-prob-2-2",
                "tier": 2,
                "difficultyLabel": "Tier 2 • Intermediate Exam",
                "title": "Newton-Gregory Forward Difference & Exact Interpolation Error Bound",
                "statement": r"Given tabulated values of $f(x) = \sin(\pi x)$ at $x = 0.0, 0.2, 0.4, 0.6$ ($h = 0.2$):<br>1. Construct the forward difference table $\Delta^k f_0$.<br>2. Use the Newton-Gregory forward formula to approximate $f(0.1)$ ($s = 0.5$).<br>3. Compute the theoretical Cauchy error bound on $|f(0.1) - P_3(0.1)|$ and compare it with the exact absolute error.",
                "solution": r"""<b>Step 1: Forward Difference Table</b><br>
Nodes and function values:<br>
- $x_0 = 0.0, f_0 = \sin(0) = 0.000000$<br>
- $x_1 = 0.2, f_1 = \sin(0.2\pi) = \sin(0.628319) = 0.587785$<br>
- $x_2 = 0.4, f_2 = \sin(0.4\pi) = \sin(1.256637) = 0.951057$<br>
- $x_3 = 0.6, f_3 = \sin(0.6\pi) = \sin(1.884956) = 0.951057$<br>
Forward differences:<br>
- $\Delta f_0 = 0.587785 - 0 = 0.587785$<br>
- $\Delta f_1 = 0.951057 - 0.587785 = 0.363272$<br>
- $\Delta f_2 = 0.951057 - 0.951057 = 0.000000$<br>
Second differences:<br>
- $\Delta^2 f_0 = 0.363272 - 0.587785 = -0.224513$<br>
- $\Delta^2 f_1 = 0.000000 - 0.363272 = -0.363272$<br>
Third difference:<br>
- $\Delta^3 f_0 = -0.363272 - (-0.224513) = -0.138759$
<br><br>
<b>Step 2: Newton-Gregory Forward Approximation for $x = 0.1$</b><br>
$s = \frac{x - x_0}{h} = \frac{0.1 - 0.0}{0.2} = 0.5$.<br>
$$P_3(0.1) = f_0 + s \Delta f_0 + \frac{s(s-1)}{2} \Delta^2 f_0 + \frac{s(s-1)(s-2)}{6} \Delta^3 f_0$$
$$= 0 + (0.5)(0.587785) + \frac{(0.5)(-0.5)}{2} (-0.224513) + \frac{(0.5)(-0.5)(-1.5)}{6} (-0.138759)$$
$$= 0.293893 + (-0.125)(-0.224513) + (0.0625)(-0.138759)$$
$$= 0.293893 + 0.028064 - 0.008672 = 0.313285$$
<br><br>
<b>Step 3: Error Bound Comparison</b><br>
Exact value: $f(0.1) = \sin(0.1\pi) = \sin(0.314159) = 0.309017$.<br>
Exact error: $|f(0.1) - P_3(0.1)| = |0.309017 - 0.313285| = 0.004268$.<br>
Theoretical Cauchy bound:
$$|R_3(0.1)| \le \frac{\max_{\xi} |f^{(4)}(\xi)|}{4!} |(x - x_0)(x - x_1)(x - x_2)(x - x_3)|$$
Fourth derivative of $f(x) = \sin(\pi x)$: $f^{(4)}(x) = \pi^4 \sin(\pi x) \le \pi^4 \approx 97.409$.<br>
Node product at $x = 0.1$:
$$|(0.1 - 0.0)(0.1 - 0.2)(0.1 - 0.4)(0.1 - 0.6)| = |(0.1)(-0.1)(-0.3)(-0.5)| = 0.0015$$
Error bound:
$$|R_3(0.1)| \le \frac{97.409}{24} \times 0.0015 = 4.0587 \times 0.0015 = 0.006088$$
The exact error $0.004268$ is strictly below the theoretical upper bound $0.006088$, fully confirming Cauchy's theorem!""",
                "answer": r"Approximation $P_3(0.1) \approx 0.313285$. Exact error $= 0.004268 \le 0.006088$ (theoretical bound)."
            },
            {
                "id": "na-prob-2-3",
                "tier": 3,
                "difficultyLabel": "Tier 3 • Honors Challenge",
                "title": "Minimax Optimality Proof of Chebyshev Interpolation Nodes",
                "statement": r"Let $\mathcal{P}_n$ denote the set of all monic polynomials of degree $n$ on $[-1, 1]$ (leading coefficient 1).<br>1. Prove that the monic Chebyshev polynomial $\tilde{T}_n(x) = \frac{1}{2^{n-1}} T_n(x)$ satisfies $\max_{x \in [-1, 1]} |\tilde{T}_n(x)| = \frac{1}{2^{n-1}}$.<br>2. Prove by contradiction that for any monic polynomial $q_n(x) \in \mathcal{P}_n$, $\max_{x \in [-1, 1]} |q_n(x)| \ge \frac{1}{2^{n-1}}$, establishing the Chebyshev Minimax Theorem.<br>3. Deduce that choosing the roots of $T_{n+1}(x)$ as interpolation nodes strictly minimizes the worst-case Cauchy remainder bound.",
                "solution": r"""<b>Step 1: Norm of the Monic Chebyshev Polynomial</b><br>
Recall $T_n(x) = \cos(n \theta)$ where $x = \cos \theta$ for $\theta \in [0, \pi]$.<br>
Since $|\cos(n \theta)| \le 1$ for all $\theta$, $\max_{x \in [-1, 1]} |T_n(x)| = 1$.<br>
The leading coefficient of $T_n(x)$ is $2^{n-1}$ for $n \ge 1$.<br>
Therefore, the monic polynomial is $\tilde{T}_n(x) = \frac{1}{2^{n-1}} T_n(x)$, and its maximum norm is:
$$\|\tilde{T}_n\|_\infty = \max_{x \in [-1, 1]} |\tilde{T}_n(x)| = \frac{1}{2^{n-1}} \max |T_n(x)| = \frac{1}{2^{n-1}}$$
Notice that $\tilde{T}_n(x)$ attains its extreme values $\pm \frac{1}{2^{n-1}}$ at the $n + 1$ Chebyshev alternation points:
$$x_k^* = \cos\left(\frac{k\pi}{n}\right), \quad k = 0, 1, \dots, n$$
with alternating signs: $\tilde{T}_n(x_k^*) = \frac{(-1)^k}{2^{n-1}}$.
<br><br>
<b>Step 2: Proof of Minimax Optimality by Contradiction</b><br>
Suppose there exists a monic polynomial $q_n(x) \in \mathcal{P}_n$ such that:
$$\|q_n\|_\infty = \max_{x \in [-1, 1]} |q_n(x)| < \frac{1}{2^{n-1}}$$
Consider the difference polynomial:
$$r(x) = \tilde{T}_n(x) - q_n(x)$$
Since both $\tilde{T}_n(x)$ and $q_n(x)$ are monic polynomials of degree $n$, their leading terms $x^n$ cancel:
$$\deg(r(x)) \le n - 1$$
Now evaluate $r(x)$ at the $n + 1$ alternation points $x_k^*$:
- For even $k$: $\tilde{T}_n(x_k^*) = \frac{1}{2^{n-1}}$. Since $|q_n(x_k^*)| < \frac{1}{2^{n-1}}$, we have:
  $$r(x_k^*) = \frac{1}{2^{n-1}} - q_n(x_k^*) > 0$$
- For odd $k$: $\tilde{T}_n(x_k^*) = -\frac{1}{2^{n-1}}$. Since $|q_n(x_k^*)| < \frac{1}{2^{n-1}}$, we have:
  $$r(x_k^*) = -\frac{1}{2^{n-1}} - q_n(x_k^*) < 0$$
Thus, $r(x)$ changes sign between every pair of consecutive points $x_k^*$ and $x_{k+1}^*$ for $k = 0, 1, \dots, n - 1$.<br>
By the Intermediate Value Theorem, $r(x)$ must have at least one zero in each open interval $(x_{k+1}^*, x_k^*)$.<br>
Since there are $n$ such disjoint intervals, $r(x)$ must have at least $n$ distinct real zeros in $[-1, 1]$!<br>
However, $\deg(r) \le n - 1$. A non-zero polynomial of degree $\le n - 1$ cannot possess $n$ distinct zeros unless it is identically zero: $r(x) \equiv 0$.<br>
This contradicts $r(x_k^*) \ne 0$. Therefore, no such polynomial $q_n$ can exist, proving:
$$\max_{x \in [-1, 1]} |q_n(x)| \ge \frac{1}{2^{n-1}} \quad \text{for all monic } q_n \in \mathcal{P}_n \quad \blacksquare$$
<br><br>
<b>Step 3: Consequence for the Cauchy Remainder</b><br>
The node product polynomial $w_n(x) = \prod_{k=0}^n (x - x_k)$ is monic of degree $n + 1$.<br>
By the Minimax Theorem, choosing $x_k$ as the roots of $T_{n+1}(x)$ gives $w_n(x) = \tilde{T}_{n+1}(x)$, guaranteeing that:
$$\max_{x \in [-1, 1]} \left| \prod_{k=0}^n (x - x_k) \right| = \frac{1}{2^n}$$
which minimizes the worst-case interpolation error bound globally across all possible node choices, rigorously proving why Chebyshev nodes suppress Runge's phenomenon! $\blacksquare$""",
                "answer": r"$\|\tilde{T}_n\|_\infty = 2^{1-n}$. The Chebyshev nodes minimize the node product norm $\|w_n\|_\infty = 2^{-n}$, establishing the optimal error bound for polynomial interpolation."
            }
        ]
    }
    return u2

if __name__ == "__main__":
    u2 = get_unit2()
    print(f"Unit 2 built successfully with {len(u2['sections'])} sections and {len(u2['problems'])} problems.")
