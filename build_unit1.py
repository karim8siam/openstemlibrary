# -*- coding: utf-8 -*-
"""
build_unit1.py
Constructs Unit 1: Non-Linear Equations in a Single Variable & Foundations of Numerical Error
"""

def get_unit1():
    u1 = {
        "number": 1,
        "title": "Non-Linear Equations in a Single Variable & Foundations of Numerical Error",
        "leadSummary": "Algorithmic root-finding methods, IEEE floating-point arithmetic, loss of significance, Banach fixed-point contraction mappings, and complete proof of quadratic convergence for the Newton-Raphson method.",
        "simulations": ["sim_na_root_finding"],
        "sections": [
            {
                "secNumber": "1.1",
                "title": "Foundations of Numerical Error: Round-Off, Truncation, Forward-Backward Error & Conditioning",
                "content": r"""### 1. The Nature of Numerical Computation and Error Taxonomy

In analytical mathematics, equations are resolved symbolically to yield exact closed-form expressions. In physical engineering and scientific computing, closed-form solutions rarely exist. Numerical analysis replaces continuous analytical operations with discrete algorithmic sequences executed on finite-precision digital computers. Consequently, numerical solutions are inherently approximations. A rigorous understanding of error taxonomy is essential to assess algorithm reliability.

Let $x$ denote the true, exact mathematical quantity and let $\hat{x}$ denote its computational approximation.

#### Definition 1.1 (Absolute, Relative, and Percentage Errors):
1. **Absolute Error:**
   $$\Delta x = |\hat{x} - x|$$
   Absolute error retains the physical dimensions of $x$, measuring the absolute magnitude of deviation.

2. **Relative Error:**
   For $x \ne 0$:
   $$\delta_x = \frac{|\hat{x} - x|}{|x|}$$
   Relative error is dimensionless and quantifies the fractional deviation relative to the scale of the true quantity.

3. **Percentage Error:**
   $$\text{PE} = \delta_x \times 100\% = \frac{|\hat{x} - x|}{|x|} \times 100\%$$

---

### 2. Digital Representation and Round-Off Error

Modern digital computing relies on the **IEEE 754 Floating-Point Standard**. A real number $x \in \mathbb{R}$ is represented in normalized binary floating-point form as:

$$x = (-1)^s \times (1.m_1 m_2 \dots m_p)_2 \times 2^{e - B}$$

where $s \in \{0, 1\}$ is the sign bit, $m = 1.m_1 m_2 \dots m_p$ is the significand (mantissa) with precision $p$, $e$ is the stored biased exponent, and $B$ is the exponent bias.
- **Single Precision (IEEE 754 float32):** 1 sign bit, 8 exponent bits ($B = 127$), 23 fraction bits ($p = 24$ bits total precision), providing approximately $7$ significant decimal digits.
- **Double Precision (IEEE 754 float64):** 1 sign bit, 11 exponent bits ($B = 1023$), 52 fraction bits ($p = 53$ bits total precision), providing approximately $16$ significant decimal digits.

#### Machine Epsilon ($\epsilon_{\text{mach}}$):
The **machine epsilon** $\epsilon_{\text{mach}}$ (or unit roundoff $\mathbf{u}$) is defined as the upper bound on relative rounding error incurred when representing a non-zero real number in the floating-point system:

$$\text{fl}(x) = x(1 + \delta), \quad |\delta| \le \mathbf{u} = \frac{1}{2} 2^{1 - p}$$

For IEEE 754 double precision:
$$\mathbf{u} = 2^{-53} \approx 1.1102 \times 10^{-16}$$

#### Catastrophic Cancellation (Loss of Significance):
A severe hazard in scientific computing occurs when subtracting two nearly equal numbers. Let $x = 1.23456789012345$ and $y = 1.23456789000000$. Both numbers have 16 digits of precision. Their difference:
$$x - y = 0.00000000012345 = 1.2345 \times 10^{-10}$$
The computed result retains only 5 significant digits; 11 digits of precision have been permanently destroyed.

*Classical Remedy Example:* In computing the roots of $a x^2 + b x + c = 0$ when $b > 0$ and $b^2 \gg 4ac$:
The standard formula $x_1 = \frac{-b + \sqrt{b^2 - 4ac}}{2a}$ suffers catastrophic cancellation. Multiplying the numerator and denominator by its conjugate algebraic form eliminates cancellation:
$$x_1 = \frac{(-b + \sqrt{b^2 - 4ac})(-b - \sqrt{b^2 - 4ac})}{2a(-b - \sqrt{b^2 - 4ac})} = \frac{-2c}{b + \sqrt{b^2 - 4ac}}$$

---

### 3. Truncation Error and Taylor Series

**Truncation error** arises from replacing an infinite mathematical process (an infinite series, a derivative limit, or an integral) with a finite discrete algebraic approximation.

#### Theorem 1.1 (Taylor's Theorem with Lagrange Remainder):
Let $f \in C^{n+1}[a, b]$ and $x_0 \in [a, b]$. For any $x \in [a, b]$:

$$f(x) = \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!} (x - x_0)^k + R_n(x)$$

where the **Lagrange Truncation Remainder** $R_n(x)$ is given by:

$$R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} (x - x_0)^{n+1}, \quad \text{for some } \xi \text{ strictly between } x_0 \text{ and } x$$

In asymptotic Big-$\mathcal{O}$ notation, with step size $h = x - x_0$:
$$R_n(h) = \mathcal{O}(h^{n+1})$$

---

### 4. Conditioning of Problems vs. Stability of Algorithms

A mathematical problem is **well-conditioned** if small perturbations in input data produce proportionally small perturbations in the solution. A problem is **ill-conditioned** if small input perturbations produce immense variations in output.

#### Definition 1.2 (Relative Condition Number of a Differentiable Function):
For a differentiable mapping $y = f(x)$, the relative condition number $\kappa(x)$ measures output sensitivity:

$$\kappa(x) = \lim_{\Delta x \to 0} \frac{|\Delta f(x) / f(x)|}{|\Delta x / x|} = \frac{|x f'(x)|}{|f(x)|}$$

If $\kappa(x) \gg 1$, the function evaluation is fundamentally ill-conditioned near $x$ regardless of how stable the numerical algorithm is."""
            },
            {
                "secNumber": "1.2",
                "title": "Bracketing Methods: The Bisection Method, Regula Falsi & Rigorous Convergence Analysis",
                "content": r"""### 1. The Root-Finding Formulation and Intermediate Value Theorem

Let $f: [a, b] \to \mathbb{R}$ be a continuous function. A point $r \in [a, b]$ is called a **root (zero)** of $f$ if:
$$f(r) = 0$$

#### Theorem 1.2 (Intermediate Value Theorem):
If $f \in C[a, b]$ and $f(a) f(b) < 0$, then there exists at least one root $r \in (a, b)$ such that $f(r) = 0$.

Bracketing methods systematically reduce the length of an initial bracket $[a_0, b_0]$ satisfying $f(a_0)f(b_0) < 0$ such that the root remains trapped within the subinterval at every step.

---

### 2. The Bisection Method

The Bisection method repeatedly bisects the search interval and selects the subinterval where the sign change persists:
1. Initialize $a_0 = a, b_0 = b$ such that $f(a_0) f(b_0) < 0$.
2. At iteration $n \ge 0$, compute the midpoint:
   $$c_n = \frac{a_n + b_n}{2}$$
3. Evaluate $f(c_n)$:
   - If $f(c_n) = 0$, then $c_n$ is the exact root; terminate.
   - If $f(a_n) f(c_n) < 0$, set $a_{n+1} = a_n$ and $b_{n+1} = c_n$.
   - If $f(a_n) f(c_n) > 0$, set $a_{n+1} = c_n$ and $b_{n+1} = b_n$.

#### Theorem 1.3 (Error Bound & Guaranteed Convergence of Bisection):
Let $f \in C[a, b]$ with $f(a) f(b) < 0$. The sequence of midpoints $\{c_n\}_{n=0}^\infty$ generated by the Bisection method converges unconditionally to a root $r \in (a, b)$, and the absolute error after $n$ iterations satisfies:

$$|c_n - r| \le \frac{b - a}{2^{n+1}}$$

*Rigorous Proof:*
At each iteration, the interval length is halved:
$$b_n - a_n = \frac{b_0 - a_0}{2^n} = \frac{b - a}{2^n}$$
Since the root $r$ and the midpoint $c_n$ both reside in the interval $[a_n, b_n]$, the maximum distance between $c_n$ and $r$ cannot exceed half the interval length:
$$|c_n - r| \le \frac{b_n - a_n}{2} = \frac{b - a}{2^{n+1}}$$
Taking the limit as $n \to \infty$:
$$\lim_{n \to \infty} |c_n - r| \le \lim_{n \to \infty} \frac{b - a}{2^{n+1}} = 0$$
Hence $\lim_{n \to \infty} c_n = r$. $\blacksquare$

#### Corollary 1.1 (Iteration Count for Prescribed Tolerance):
To guarantee an absolute error $|c_n - r| < \epsilon$, the required number of bisection iterations $n$ satisfies:

$$\frac{b - a}{2^{n+1}} < \epsilon \iff 2^{n+1} > \frac{b - a}{\epsilon} \iff n > \frac{\ln(b - a) - \ln \epsilon}{\ln 2} - 1$$

---

### 3. Method of False Position (Regula Falsi)

While Bisection chooses the geometric midpoint $c_n = \frac{a_n + b_n}{2}$ regardless of function values, Regula Falsi constructs the secant line connecting $(a_n, f(a_n))$ and $(b_n, f(b_n))$:

$$y - f(b_n) = \frac{f(b_n) - f(a_n)}{b_n - a_n} (x - b_n)$$

Setting $y = 0$ yields the $x$-intercept:

$$c_n = b_n - f(b_n) \frac{b_n - a_n}{f(b_n) - f(a_n)} = \frac{a_n f(b_n) - b_n f(a_n)}{f(b_n) - f(a_n)}$$

#### The Stagnant Endpoint Phenomenon:
If $f''(x) > 0$ on $[a, b]$ (convex curve), one endpoint remains stationary for all subsequent iterations, degrading convergence to linear rate with ratio $\lambda \approx 1 - \frac{f'(r)(b - r)}{f(b)}$.

**The Illinois Modification:** If an endpoint remains stagnant for two consecutive steps, its function value is halved ($f(a_{n+1}) \leftarrow \frac{1}{2} f(a_n)$), restoring superlinear convergence ($\mathcal{O}(h^{\sqrt[3]{3}}) \approx \mathcal{O}(h^{1.442})$)."""
            },
            {
                "secNumber": "1.3",
                "title": "Fixed-Point Iteration & The Banach Contraction Mapping Principle on R",
                "content": r"""### 1. Transformation into Fixed-Point Form

A non-linear equation $f(x) = 0$ can always be algebraically rearranged into an equivalent **fixed-point problem**:
$$x = g(x)$$
A point $r$ satisfying $r = g(r)$ is called a **fixed point** of $g$. The simplest iterative scheme starting from an initial guess $x_0$ is Picard iteration:
$$x_{n+1} = g(x_n), \quad n = 0, 1, 2, \dots$$

---

### 2. The Banach Contraction Mapping Theorem on $\mathbb{R}$

#### Definition 1.3 (Contraction Mapping):
A function $g: [a, b] \to [a, b]$ is called a **contraction** on $[a, b]$ if there exists a constant $k \in [0, 1)$ such that for all $x, y \in [a, b]$:
$$|g(x) - g(y)| \le k |x - y|$$
The constant $k$ is called the **Lipschitz contraction factor**.

#### Theorem 1.4 (Banach Fixed-Point Theorem on $\mathbb{R}$):
Let $g \in C[a, b]$ satisfy:
1. **Self-Mapping:** $g(x) \in [a, b]$ for all $x \in [a, b]$.
2. **Contraction Criterion:** If $g \in C^1[a, b]$, there exists $k \in (0, 1)$ such that $|g'(x)| \le k < 1$ for all $x \in [a, b]$.

Then:
1. $g$ has a unique fixed point $r \in [a, b]$.
2. For any arbitrary initial guess $x_0 \in [a, b]$, the sequence $x_{n+1} = g(x_n)$ converges to $r$:
   $$\lim_{n \to \infty} x_n = r$$
3. The error satisfies the bounds:
   $$|x_n - r| \le \frac{k^n}{1 - k} |x_1 - x_0|$$
   $$|x_n - r| \le k |x_{n-1} - r|$$

*Rigorous Proof:*
**Part A (Existence):** Define $h(x) = x - g(x)$. Since $g([a, b]) \subseteq [a, b]$, $h(a) = a - g(a) \le 0$ and $h(b) = b - g(b) \ge 0$. By the Intermediate Value Theorem, there exists $r \in [a, b]$ such that $h(r) = 0 \implies r = g(r)$.

**Part B (Uniqueness):** Suppose $r_1, r_2 \in [a, b]$ are both fixed points. Then:
$$|r_1 - r_2| = |g(r_1) - g(r_2)| \le k |r_1 - r_2| \implies (1 - k) |r_1 - r_2| \le 0$$
Since $k < 1$, $1 - k > 0$. Non-negativity of absolute values forces $|r_1 - r_2| = 0 \implies r_1 = r_2$.

**Part C (Convergence):** Using the Mean Value Theorem on $g$:
$$|x_{n+1} - r| = |g(x_n) - g(r)| = |g'(\xi_n)| |x_n - r| \le k |x_n - r|$$
By induction:
$$|x_n - r| \le k^n |x_0 - r|$$
Since $k \in [0, 1)$, $\lim_{n \to \infty} k^n = 0$, establishing $\lim_{n \to \infty} x_n = r$.

**Part D (A Priori Bound):** For any $m > n$:
$$|x_m - x_n| \le \sum_{j=n}^{m-1} |x_{j+1} - x_j| \le \sum_{j=n}^{m-1} k^j |x_1 - x_0| = k^n |x_1 - x_0| \sum_{i=0}^{m-n-1} k^i$$
Summing the geometric series and taking $m \to \infty$ (since $x_m \to r$):
$$|r - x_n| \le \frac{k^n}{1 - k} |x_1 - x_0| \quad \blacksquare$$"""
            },
            {
                "secNumber": "1.4",
                "title": "Newton-Raphson Method, Quadratic Convergence Proof & Acceleration Techniques",
                "content": r"""### 1. Derivation of the Newton-Raphson Scheme

The Newton-Raphson method is the premier open root-finding method in scientific computing. Expanding $f(x)$ about the current iterate $x_n$ using a first-order Taylor polynomial:

$$f(x) \approx f(x_n) + f'(x_n)(x - x_n)$$

Setting $f(x) = 0$ and solving for $x = x_{n+1}$:

$$0 = f(x_n) + f'(x_n)(x_{n+1} - x_n) \implies x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

Geometrically, $x_{n+1}$ is the $x$-intercept of the tangent line to the curve $y = f(x)$ at $(x_n, f(x_n))$.

---

### 2. Rigorous Proof of Quadratic Convergence

#### Definition 1.4 (Order of Convergence):
An iterative sequence $x_{n+1} = g(x_n)$ converging to $r$ with error $e_n = x_n - r$ is said to converge with **order $p \ge 1$** if:
$$\lim_{n \to \infty} \frac{|e_{n+1}|}{|e_n|^p} = C > 0$$
where $C$ is the asymptotic error constant. If $p = 1$, convergence is linear; if $p = 2$, convergence is **quadratic**.

#### Theorem 1.5 (Quadratic Convergence of Newton-Raphson):
Let $f \in C^2[a, b]$ and let $r \in (a, b)$ be a simple root such that $f(r) = 0$ and $f'(r) \ne 0$. Then there exists a neighborhood $\delta > 0$ such that for any initial guess $x_0 \in [r - \delta, r + \delta]$, the Newton-Raphson sequence converges to $r$ quadratically:

$$e_{n+1} = \frac{f''(\xi_n)}{2 f'(x_n)} e_n^2$$

and:
$$\lim_{n \to \infty} \frac{|e_{n+1}|}{e_n^2} = \left| \frac{f''(r)}{2 f'(r)} \right|$$

*Rigorous Line-by-Line Proof:*
Expand $f(r)$ about $x_n$ using Taylor's Theorem with exact second-order Lagrange remainder:
$$0 = f(r) = f(x_n) + f'(x_n)(r - x_n) + \frac{f''(\xi_n)}{2}(r - x_n)^2$$
where $\xi_n$ lies strictly between $x_n$ and $r$.
Recall that $e_n = x_n - r \implies r - x_n = -e_n$. Substituting:
$$0 = f(x_n) - f'(x_n) e_n + \frac{f''(\xi_n)}{2} e_n^2$$
Divide both sides by $f'(x_n)$ (valid since $f'(x_n) \ne 0$ for $x_n$ sufficiently close to $r$):
$$0 = \frac{f(x_n)}{f'(x_n)} - e_n + \frac{f''(\xi_n)}{2 f'(x_n)} e_n^2$$
From the Newton-Raphson definition:
$$\frac{f(x_n)}{f'(x_n)} = x_n - x_{n+1} = (x_n - r) - (x_{n+1} - r) = e_n - e_{n+1}$$
Substitute this relation into the Taylor expression:
$$0 = (e_n - e_{n+1}) - e_n + \frac{f''(\xi_n)}{2 f'(x_n)} e_n^2$$
The $e_n$ terms cancel algebraically:
$$-e_{n+1} + \frac{f''(\xi_n)}{2 f'(x_n)} e_n^2 = 0 \implies e_{n+1} = \frac{f''(\xi_n)}{2 f'(x_n)} e_n^2$$
Taking absolute values and the limit as $n \to \infty$: Since $x_n \to r$, by continuity $\xi_n \to r$:
$$\lim_{n \to \infty} \frac{|e_{n+1}|}{|e_n|^2} = \left| \frac{f''(r)}{2 f'(r)} \right| = C$$
The power of $e_n$ is strictly $p = 2$. Hence Newton-Raphson achieves quadratic convergence. $\blacksquare$

---

### 3. Multiple Roots and Failure Modes

If $r$ is a root of multiplicity $m > 1$, then $f(r) = f'(r) = \dots = f^{(m-1)}(r) = 0$ while $f^{(m)}(r) \ne 0$.
The standard Newton-Raphson scheme degrades to linear convergence with ratio $\lim \frac{e_{n+1}}{e_n} = 1 - \frac{1}{m}$.
To restore quadratic convergence, apply the **Modified Newton-Raphson formula**:
$$x_{n+1} = x_n - m \frac{f(x_n)}{f'(x_n)}$$

---

### 4. Convergence Acceleration: Aitken's $\Delta^2$ Process

For any linearly converging sequence $x_n \to r$ with $e_{n+1} \approx \lambda e_n$:
$$x_{n+1} - r \approx \lambda (x_n - r), \quad x_{n+2} - r \approx \lambda (x_{n+1} - r)$$
Eliminating the unknown ratio $\lambda$ yields **Aitken's $\Delta^2$ extrapolated formula**:

$$\hat{x}_n = x_n - \frac{(\Delta x_n)^2}{\Delta^2 x_n} = x_n - \frac{(x_{n+1} - x_n)^2}{x_{n+2} - 2x_{n+1} + x_n}$$

Steffensen's method applies Aitken's extrapolation iteratively to fixed-point iteration, achieving quadratic convergence without evaluating derivatives."""
            }
        ],
        "problems": [
            {
                "id": "na-prob-1-1",
                "tier": 1,
                "difficultyLabel": "Tier 1 • Foundational",
                "title": "Bisection & False Position Bound on Transcendental Root",
                "statement": r"Given the transcendental equation $f(x) = x \ln(x) - 1.2 = 0$ on the interval $[1.0, 3.0]$:<br>1. Verify that $f(x)$ has a unique root in $[1.0, 3.0]$.<br>2. Calculate the exact minimum number of Bisection iterations $n$ required to guarantee an absolute error $|c_n - r| < 10^{-5}$.<br>3. Compute the first three iterations of the Bisection method and the first two iterations of the Regula Falsi (False Position) method.",
                "solution": r"""<b>Step 1: Verify existence and uniqueness of the root</b><br>
$f(x) = x \ln x - 1.2$ is continuous on $[1, 3]$.<br>
$f(1) = 1 \cdot \ln(1) - 1.2 = -1.2 < 0$.<br>
$f(3) = 3 \ln(3) - 1.2 = 3(1.098612) - 1.2 = 3.295837 - 1.2 = 2.095837 > 0$.<br>
Since $f(1) f(3) < 0$, by the Intermediate Value Theorem, there exists at least one root $r \in (1, 3)$.<br>
Derivative: $f'(x) = \ln x + x \cdot \frac{1}{x} = \ln x + 1$.<br>
For all $x \in [1, 3]$, $\ln x \ge 0 \implies f'(x) \ge 1 > 0$. Since $f'(x)$ is strictly positive, $f(x)$ is strictly monotonically increasing, proving the root is strictly <b>unique</b>.
<br><br>
<b>Step 2: Minimum Bisection iterations for tolerance $\epsilon = 10^{-5}$</b><br>
The theoretical bisection error bound is:
$$\frac{b - a}{2^{n+1}} < 10^{-5} \implies \frac{3 - 1}{2^{n+1}} < 10^{-5} \implies \frac{2}{2^{n+1}} = \frac{1}{2^n} < 10^{-5}$$
Taking base-10 logarithms:
$$2^n > 10^5 \implies n \ln(2) > 5 \ln(10) \implies n > \frac{5 \ln(10)}{\ln(2)} = \frac{11.512925}{0.693147} \approx 16.6096$$
Since $n$ must be an integer: $n = 17$ iterations.
<br><br>
<b>Step 3: First three Bisection iterations</b><br>
- Iteration 1: $c_0 = \frac{1 + 3}{2} = 2.0$.<br>
  $f(2) = 2 \ln(2) - 1.2 = 2(0.693147) - 1.2 = 1.386294 - 1.2 = +0.186294 > 0$.<br>
  Since $f(1) < 0$ and $f(2) > 0$, the root lies in $[1.0, 2.0]$.<br>
- Iteration 2: $c_1 = \frac{1 + 2}{2} = 1.5$.<br>
  $f(1.5) = 1.5 \ln(1.5) - 1.2 = 1.5(0.405465) - 1.2 = 0.608198 - 1.2 = -0.591802 < 0$.<br>
  Since $f(1.5) < 0$ and $f(2) > 0$, the root lies in $[1.5, 2.0]$.<br>
- Iteration 3: $c_2 = \frac{1.5 + 2}{2} = 1.75$.<br>
  $f(1.75) = 1.75 \ln(1.75) - 1.2 = 1.75(0.559616) - 1.2 = 0.979328 - 1.2 = -0.220672 < 0$.<br>
  Root bracket after 3 steps: $[1.75, 2.0]$.
<br><br>
<b>Step 4: Regula Falsi iterations</b><br>
With $a_0 = 1.0, f(a_0) = -1.2$ and $b_0 = 3.0, f(b_0) = 2.095837$:<br>
$$c_0 = \frac{a_0 f(b_0) - b_0 f(a_0)}{f(b_0) - f(a_0)} = \frac{1.0(2.095837) - 3.0(-1.2)}{2.095837 - (-1.2)} = \frac{2.095837 + 3.6}{3.295837} = \frac{5.695837}{3.295837} \approx 1.72819$$
$f(1.72819) = 1.72819 \ln(1.72819) - 1.2 = 1.72819(0.547073) - 1.2 = 0.945447 - 1.2 = -0.254553 < 0$.<br>
Update: $a_1 = 1.72819, f(a_1) = -0.254553$, while $b_1 = 3.0, f(b_1) = 2.095837$.<br>
$$c_1 = \frac{1.72819(2.095837) - 3.0(-0.254553)}{2.095837 - (-0.254553)} = \frac{3.621996 + 0.763659}{2.350390} = \frac{4.385655}{2.350390} \approx 1.86593$$""",
                "answer": r"$n = 17$ bisection iterations required. Bisection estimates: $c_0 = 2.0, c_1 = 1.5, c_2 = 1.75$. Regula Falsi estimates: $c_0 \approx 1.72819, c_1 \approx 1.86593$."
            },
            {
                "id": "na-prob-1-2",
                "tier": 2,
                "difficultyLabel": "Tier 2 • Intermediate Exam",
                "title": "Newton-Raphson Fast Reciprocal Square-Root & Quadratic Verification",
                "statement": r"In real-time 3D physics graphics, computing $1/\sqrt{a}$ without division is vital.<br>1. Derive an iteration formula to compute $1/\sqrt{a}$ for $a > 0$ using the Newton-Raphson method applied to $f(x) = \frac{1}{x^2} - a = 0$ that requires only multiplications and subtractions (zero divisions).<br>2. Prove analytically that the error $e_n = x_n - 1/\sqrt{a}$ satisfies $e_{n+1} = -\frac{3\sqrt{a}}{2} e_n^2 - \frac{a}{2} e_n^3$, verifying quadratic convergence.<br>3. Compute 3 iterations for $a = 5$ starting from $x_0 = 0.4$.",
                "solution": r"""<b>Step 1: Newton-Raphson derivation</b><br>
Target equation: $f(x) = x^{-2} - a = 0$.<br>
Derivative: $f'(x) = -2 x^{-3}$.<br>
Applying the Newton-Raphson formula:
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} = x_n - \frac{x_n^{-2} - a}{-2 x_n^{-3}} = x_n + \frac{x_n^3 (x_n^{-2} - a)}{2} = x_n + \frac{x_n - a x_n^3}{2} = \frac{x_n(3 - a x_n^2)}{2}$$
This is the celebrated formula requiring strictly multiplications and subtractions, forming the foundation of the Fast Inverse Square Root algorithm!
<br><br>
<b>Step 2: Analytical Error Derivation</b><br>
Let $r = a^{-1/2}$, so $a r^2 = 1$ and $a = r^{-2}$.<br>
Define error $e_n = x_n - r \implies x_n = r + e_n$. Substitute into the recurrence:
$$x_{n+1} = \frac{(r + e_n)[3 - a(r + e_n)^2]}{2} = \frac{(r + e_n)[3 - a(r^2 + 2r e_n + e_n^2)]}{2}$$
Since $a r^2 = 1$:
$$3 - a r^2 - 2a r e_n - a e_n^2 = 3 - 1 - 2 a r e_n - a e_n^2 = 2 - 2a r e_n - a e_n^2$$
Substitute back:
$$x_{n+1} = \frac{(r + e_n)(2 - 2a r e_n - a e_n^2)}{2} = (r + e_n)(1 - a r e_n - \frac{a}{2} e_n^2)$$
Expanding the product:
$$x_{n+1} = r - a r^2 e_n - \frac{a r}{2} e_n^2 + e_n - a r e_n^2 - \frac{a}{2} e_n^3$$
Since $a r^2 = 1$, the linear terms $-a r^2 e_n + e_n = -e_n + e_n = 0$ cancel completely!
$$x_{n+1} = r - \frac{3 a r}{2} e_n^2 - \frac{a}{2} e_n^3$$
Subtracting $r$:
$$e_{n+1} = x_{n+1} - r = -\frac{3 a r}{2} e_n^2 - \frac{a}{2} e_n^3 = -\frac{3\sqrt{a}}{2} e_n^2 - \frac{a}{2} e_n^3$$
For small $e_n$, the leading term is strictly proportional to $e_n^2$, proving asymptotic <b>quadratic convergence</b> with constant $C = \frac{3\sqrt{a}}{2}$.
<br><br>
<b>Step 3: Numerical iterations for $a = 5$ with $x_0 = 0.4$</b><br>
Exact root $r = 1/\sqrt{5} \approx 0.4472135955$.<br>
- Iteration 1: $x_1 = \frac{0.4 [3 - 5(0.4)^2]}{2} = \frac{0.4 [3 - 5(0.16)]}{2} = \frac{0.4 [3 - 0.8]}{2} = 0.2 \times 2.2 = 0.4400000000$.<br>
- Iteration 2: $x_2 = \frac{0.44 [3 - 5(0.44)^2]}{2} = 0.22 [3 - 5(0.1936)] = 0.22 [3 - 0.968] = 0.22 \times 2.032 = 0.4470400000$.<br>
- Iteration 3: $x_3 = \frac{0.44704 [3 - 5(0.44704)^2]}{2} \approx 0.4472135003$.<br>
Error after 3 steps: $|x_3 - r| \approx 9.5 \times 10^{-8}$. Notice the digits of precision double each step!""",
                "answer": r"Recurrence: $x_{n+1} = \frac{x_n(3 - a x_n^2)}{2}$. Iterates for $a=5$: $x_0 = 0.4, x_1 = 0.440000, x_2 = 0.447040, x_3 = 0.44721350$, verifying quadratic doubling of accurate digits."
            },
            {
                "id": "na-prob-1-3",
                "tier": 3,
                "difficultyLabel": "Tier 3 • Honors Challenge",
                "title": "Aitken Extrapolation Acceleration & Multiplicity Root Proof",
                "statement": r"Consider a root $r$ of $f(x) = 0$ having multiplicity $m \ge 2$, such that $f(x) = (x - r)^m h(x)$ with $h(r) \ne 0$.<br>1. Prove rigorously that standard Newton-Raphson $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$ converges linearly with asymptotic error constant $C = 1 - \frac{1}{m}$.<br>2. Prove that applying Aitken's $\Delta^2$ acceleration $\hat{x}_n = x_n - \frac{(\Delta x_n)^2}{\Delta^2 x_n}$ to this linearly converging sequence restores superlinear convergence.<br>3. Test this on $f(x) = (x - 2)^3 e^x = 0$ with $x_0 = 2.5$.",
                "solution": r"""<b>Step 1: Proof of linear convergence for multiple root</b><br>
Let $f(x) = (x - r)^m h(x)$ with $h(r) \ne 0$ and $h \in C^1$.<br>
Differentiating via product rule:
$$f'(x) = m(x - r)^{m-1} h(x) + (x - r)^m h'(x) = (x - r)^{m-1}[m h(x) + (x - r) h'(x)]$$
Substitute $f(x)$ and $f'(x)$ into the fixed-point function $g(x) = x - \frac{f(x)}{f'(x)}$:
$$g(x) = x - \frac{(x - r)^m h(x)}{(x - r)^{m-1}[m h(x) + (x - r) h'(x)]} = x - (x - r) \frac{h(x)}{m h(x) + (x - r) h'(x)}$$
Differentiating $g(x)$ with respect to $x$:
$$g'(x) = 1 - \frac{h(x)}{m h(x) + (x - r) h'(x)} - (x - r) \frac{d}{dx}\left[ \frac{h(x)}{m h(x) + (x - r) h'(x)} \right]$$
Evaluating at $x = r$:
The third term vanishes because of the factor $(r - r) = 0$. Thus:
$$g'(r) = 1 - \frac{h(r)}{m h(r) + 0} = 1 - \frac{1}{m}$$
Since $m \ge 2$, $0 < 1 - \frac{1}{m} < 1$. By Taylor expansion of $g(x_n)$ around $r$:
$$e_{n+1} = x_{n+1} - r = g(x_n) - g(r) = g'(r) e_n + \mathcal{O}(e_n^2) = \left(1 - \frac{1}{m}\right) e_n + \mathcal{O}(e_n^2)$$
Thus $\lim_{n \to \infty} \frac{e_{n+1}}{e_n} = 1 - \frac{1}{m} \ne 0$, proving that standard Newton-Raphson suffers <b>linear convergence</b> when $m \ge 2$. $\blacksquare$
<br><br>
<b>Step 2: Proof of Aitken's $\Delta^2$ Acceleration</b><br>
Since $e_n = x_n - r$, write $x_n = r + e_n$ where $e_{n+1} = \lambda e_n + \mathcal{O}(e_n^2)$ with $\lambda = 1 - 1/m$.<br>
Compute forward differences:
$$\Delta x_n = x_{n+1} - x_n = e_{n+1} - e_n = (\lambda - 1) e_n + \mathcal{O}(e_n^2)$$
$$\Delta x_{n+1} = x_{n+2} - x_{n+1} = (\lambda - 1) e_{n+1} + \mathcal{O}(e_{n+1}^2) = \lambda(\lambda - 1) e_n + \mathcal{O}(e_n^2)$$
$$\Delta^2 x_n = \Delta x_{n+1} - \Delta x_n = (\lambda - 1)^2 e_n + \mathcal{O}(e_n^2)$$
Now evaluate Aitken's correction:
$$\frac{(\Delta x_n)^2}{\Delta^2 x_n} = \frac{[(\lambda - 1) e_n + \mathcal{O}(e_n^2)]^2}{(\lambda - 1)^2 e_n + \mathcal{O}(e_n^2)} = \frac{(\lambda - 1)^2 e_n^2 + \mathcal{O}(e_n^3)}{(\lambda - 1)^2 e_n [1 + \mathcal{O}(e_n)]} = e_n + \mathcal{O}(e_n^2)$$
Substitute into the Aitken formula:
$$\hat{x}_n = x_n - \frac{(\Delta x_n)^2}{\Delta^2 x_n} = (r + e_n) - [e_n + \mathcal{O}(e_n^2)] = r + \mathcal{O}(e_n^2)$$
Hence:
$$\frac{\hat{x}_n - r}{e_n} = \frac{\mathcal{O}(e_n^2)}{e_n} \to 0 \quad \text{as } n \to \infty$$
The first-order error is completely eliminated, converting linear convergence into quadratic error damping! $\blacksquare$
<br><br>
<b>Step 3: Numerical Demonstration for $f(x) = (x - 2)^3 e^x$ ($r = 2, m = 3$)</b><br>
$\lambda = 1 - 1/3 = 2/3 \approx 0.6667$.<br>
Start $x_0 = 2.5 \implies e_0 = 0.5$.<br>
- $x_1 = 2.5 - \frac{(0.5)^3 e^{2.5}}{3(0.5)^2 e^{2.5} + (0.5)^3 e^{2.5}} = 2.5 - \frac{0.5}{3 + 0.5} = 2.5 - \frac{0.5}{3.5} = 2.5 - 0.142857 = 2.357143$ ($e_1 \approx 0.357143$).<br>
- Ratio $e_1 / e_0 = 0.357143 / 0.5 \approx 0.7143 \approx 2/3$.<br>
- $x_2 \approx 2.247253$ ($e_2 \approx 0.247253$, ratio $e_2/e_1 \approx 0.692$).<br>
Applying Aitken's formula to $x_0, x_1, x_2$:
$$\Delta x_0 = x_1 - x_0 = -0.142857, \quad \Delta x_1 = x_2 - x_1 = -0.109890$$
$$\Delta^2 x_0 = \Delta x_1 - \Delta x_0 = -0.109890 - (-0.142857) = 0.032967$$
$$\hat{x}_0 = x_0 - \frac{(\Delta x_0)^2}{\Delta^2 x_0} = 2.5 - \frac{(-0.142857)^2}{0.032967} = 2.5 - \frac{0.020408}{0.032967} = 2.5 - 0.619048 = 1.880952$$
Error jumps from $0.5$ directly to $-0.119$, accelerating convergence dramatically!"""
            }
        ]
    }
    return u1

if __name__ == '__main__':
    u = get_unit1()
    print('Unit 1 generated successfully:', u['title'])
    print('Sections:', len(u['sections']))
    print('Problems:', len(u['problems']))
