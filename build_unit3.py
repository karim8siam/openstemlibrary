# -*- coding: utf-8 -*-
"""
build_unit3.py
Constructs Unit 3: Numerical Differentiation, Richardson Extrapolation & Advanced Quadrature
"""

def get_unit3():
    u3 = {
        "number": 3,
        "title": "Numerical Differentiation, Richardson Extrapolation & Advanced Quadrature",
        "leadSummary": "Finite difference stencils, step-size truncation-roundoff tradeoff, Richardson extrapolation, composite Newton-Cotes quadrature (Trapezoidal, Simpson's, Weddle's), Romberg integration, and Gauss-Legendre quadrature.",
        "simulations": ["sim_na_quadrature"],
        "sections": [
            {
                "secNumber": "3.1",
                "title": "Numerical Differentiation: Finite Difference Stencils & Truncation-Roundoff Tradeoff",
                "content": r"""### 1. Finite Difference Approximations of Derivatives

When an analytical expression for $f(x)$ is unavailable or excessively complicated, derivatives must be computed from discrete evaluations. By truncating Taylor series expansions, we construct finite difference stencils.

Let $h > 0$ denote the discretization grid spacing.

#### 1. Forward and Backward Difference Approximations ($\mathcal{O}(h)$):
Expanding $f(x + h)$ in Taylor series:
$$f(x + h) = f(x) + h f'(x) + \frac{h^2}{2} f''(\xi), \quad \xi \in (x, x + h)$$
Solving for $f'(x)$:
$$\boxed{f'(x) = \frac{f(x + h) - f(x)}{h} - \frac{h}{2} f''(\xi) = D_h^+ f(x) + \mathcal{O}(h)}$$

Similarly, expanding $f(x - h)$:
$$\boxed{f'(x) = \frac{f(x) - f(x - h)}{h} + \frac{h}{2} f''(\xi) = D_h^- f(x) + \mathcal{O}(h)}$$

#### 2. Three-Point Centered Difference Formula ($\mathcal{O}(h^2)$):
Subtracting the backward Taylor expansion from the forward Taylor expansion:
$$f(x + h) = f(x) + h f'(x) + \frac{h^2}{2!} f''(x) + \frac{h^3}{3!} f'''(x) + \frac{h^4}{4!} f^{(4)}(\xi_1)$$
$$f(x - h) = f(x) - h f'(x) + \frac{h^2}{2!} f''(x) - \frac{h^3}{3!} f'''(x) + \frac{h^4}{4!} f^{(4)}(\xi_2)$$
$$f(x + h) - f(x - h) = 2h f'(x) + \frac{h^3}{3} f'''(\xi)$$
Solving for $f'(x)$ yields the **Centered Difference Formula**:
$$\boxed{f'(x) = \frac{f(x + h) - f(x - h)}{2h} - \frac{h^2}{6} f'''(\xi) = D_h^0 f(x) + \mathcal{O}(h^2)}$$
The linear error term cancels identically due to symmetry, elevating the accuracy from $\mathcal{O}(h)$ to $\mathcal{O}(h^2)$.

#### 3. Second Derivative Centered Difference Stencil ($\mathcal{O}(h^2)$):
Adding the two Taylor expansions:
$$f(x + h) + f(x - h) = 2f(x) + h^2 f''(x) + \frac{h^4}{12} f^{(4)}(\xi)$$
$$\boxed{f''(x) = \frac{f(x + h) - 2f(x) + f(x - h)}{h^2} - \frac{h^2}{12} f^{(4)}(\xi) = \mathcal{O}(h^2)}$$

---

### 2. The Fundamental Truncation-Roundoff Dilemma

In pure analysis, the derivative is obtained by taking $\lim_{h \to 0}$. In digital computing, as $h \to 0$, finite precision arithmetic destroys the solution!

Suppose each function evaluation is contaminated by roundoff error bounded by $\epsilon = \epsilon_{\text{mach}} |f(x)|$:
$$\tilde{f}(x) = f(x) + e(x), \quad |e(x)| \le \epsilon$$
The computationally computed centered difference derivative is:
$$\tilde{D}_h^0 f(x) = \frac{\tilde{f}(x + h) - \tilde{f}(x - h)}{2h} = \frac{f(x + h) - f(x - h)}{2h} + \frac{e(x + h) - e(x - h)}{2h}$$
The total computational error $E_{\text{total}}(h) = |f'(x) - \tilde{D}_h^0 f(x)|$ satisfies:

$$E_{\text{total}}(h) \le \underbrace{\frac{h^2}{6} M}_{\text{Truncation Error}} + \underbrace{\frac{\epsilon}{h}}_{\text{Round-Off Error}}$$

where $M = \max |f'''(\xi)|$.
- As $h$ decreases, **truncation error decays** as $h^2$.
- But as $h$ decreases, **round-off error explodes** as $\frac{1}{h}$ due to division by near-zero!

#### Optimal Step Size ($h^*$):
Minimizing $E(h) = \frac{M h^2}{6} + \frac{\epsilon}{h}$ by setting $\frac{dE}{dh} = \frac{M h}{3} - \frac{\epsilon}{h^2} = 0$:

$$h^* = \left( \frac{3 \epsilon}{M} \right)^{1/3}$$

For double-precision floating point ($\epsilon \approx 10^{-16}$), the optimal step size for centered differences is $h^* \approx 10^{-16/3} \approx 10^{-5.3} \approx 10^{-5}$, and the achievable accuracy is bounded by $E(h^*) \approx \mathcal{O}(\epsilon^{2/3}) \approx 10^{-11}$. One cannot achieve full 16-digit machine precision with simple finite differences!"""
            },
            {
                "secNumber": "3.2",
                "title": "Richardson Extrapolation & Systematic Higher-Order Acceleration",
                "content": r"""### 1. The Principle of Richardson Error Cancellation

**Richardson Extrapolation** is a general numerical acceleration technique that systematically eliminates the dominant term in a truncation error expansion.

Suppose an approximation $N_1(h)$ to an unknown exact quantity $M$ has an asymptotic expansion with even powers of $h$:
$$M = N_1(h) + K_1 h^2 + K_2 h^4 + K_3 h^6 + \dots$$
where the coefficients $K_j$ are independent of $h$.
Now evaluate the same approximation with half the step size, $h/2$:
$$M = N_1(h/2) + K_1 \left(\frac{h}{2}\right)^2 + K_2 \left(\frac{h}{2}\right)^4 + \dots = N_1(h/2) + \frac{K_1}{4} h^2 + \frac{K_2}{16} h^4 + \dots$$

Multiply the second equation by 4 and subtract the first equation:
$$4M - M = 4 N_1(h/2) - N_1(h) + K_1 h^2 - K_1 h^2 + \left( \frac{K_2}{4} - K_2 \right) h^4 + \dots$$
$$3M = 4 N_1(h/2) - N_1(h) - \frac{3 K_2}{4} h^4 + \dots$$
Dividing by 3:
$$M = \underbrace{\frac{4 N_1(h/2) - N_1(h)}{3}}_{N_2(h)} - \frac{K_2}{4} h^4 + \dots$$
Define the new approximation $N_2(h) = N_1(h/2) + \frac{N_1(h/2) - N_1(h)}{3}$. Its error is $\mathcal{O}(h^4)$, having completely eliminated the $\mathcal{O}(h^2)$ term without evaluating higher derivatives!

---

### 2. General Extrapolation Tableau

Repeating this process recursively generates a triangular tableau:

$$N_j(h) = N_{j-1}(h/2) + \frac{N_{j-1}(h/2) - N_{j-1}(h)}{4^{j-1} - 1}, \quad j = 2, 3, \dots$$

- Column 1: $\mathcal{O}(h^2)$ approximations ($N_1(h), N_1(h/2), N_1(h/4), \dots$).
- Column 2: $\mathcal{O}(h^4)$ approximations.
- Column 3: $\mathcal{O}(h^6)$ approximations.
- Column $m$: $\mathcal{O}(h^{2m})$ approximations."""
            },
            {
                "secNumber": "3.3",
                "title": "Newton-Cotes Quadrature Formulas: Trapezoidal, Simpson's & Weddle's Rules",
                "content": r"""### 1. General Framework of Interpolatory Quadrature

Numerical integration (**quadrature**) replaces a definite integral $I = \int_a^b f(x) dx$ with a finite weighted sum:
$$I_n = \sum_{i=0}^n w_i f(x_i)$$
In **Newton-Cotes formulas**, the nodes $x_i$ are equispaced: $x_i = a + i h$ with $h = \frac{b - a}{n}$.
The weights $w_i$ are obtained by integrating the cardinal Lagrange basis polynomials:
$$w_i = \int_a^b L_{n,i}(x) dx = \int_a^b \prod_{j \ne i} \frac{x - x_j}{x_i - x_j} dx$$

---

### 2. The Trapezoidal Rule ($n = 1$)

Connecting $(a, f(a))$ and $(b, f(b))$ with a linear interpolant:
$$\int_a^b f(x) dx \approx \frac{b - a}{2} [f(a) + f(b)]$$

#### Composite Trapezoidal Rule:
Dividing $[a, b]$ into $m$ subintervals of length $h = \frac{b - a}{m}$:

$$\boxed{\int_a^b f(x) dx = \frac{h}{2} \left[ f(x_0) + 2 \sum_{i=1}^{m-1} f(x_i) + f(x_m) \right] + E_T}$$

#### Theorem 3.1 (Trapezoidal Truncation Error):
If $f \in C^2[a, b]$, the global truncation error is:

$$E_T = -\frac{(b - a) h^2}{12} f''(\xi), \quad \xi \in (a, b)$$

---

### 3. Simpson's 1/3 Rule ($n = 2$)

Fitting a parabola through $(x_0, f_0), (x_1, f_1), (x_2, f_2)$ with $h = \frac{b - a}{2}$:
$$\int_{x_0}^{x_2} f(x) dx \approx \frac{h}{3} [f(x_0) + 4 f(x_1) + f(x_2)]$$

#### Composite Simpson's 1/3 Rule ($m$ even):
Dividing $[a, b]$ into an even number $m$ of subintervals:

$$\boxed{\int_a^b f(x) dx = \frac{h}{3} \left[ f(x_0) + 4 \sum_{i=1, 3, \dots}^{m-1} f(x_i) + 2 \sum_{i=2, 4, \dots}^{m-2} f(x_i) + f(x_m) \right] + E_S}$$

#### Theorem 3.2 (Simpson's Error Formula & Precision Miracle):
If $f \in C^4[a, b]$, the global error is:

$$E_S = -\frac{(b - a) h^4}{180} f^{(4)}(\xi), \quad \xi \in (a, b)$$

*Significance:* Because Simpson's rule uses a symmetric quadratic interpolant, the cubic error term $\int_{-h}^h x^3 dx = 0$ vanishes by symmetry. Consequently, Simpson's rule integrates polynomials of degree up to 3 **exactly** without any error!

---

### 4. Simpson's 3/8 Rule ($n = 3$) and Weddle's Rule ($n = 6$)

- **Simpson's 3/8 Rule:** Fits a cubic through 4 equispaced points:
  $$\int_{x_0}^{x_3} f(x) dx = \frac{3h}{8} [f(x_0) + 3 f(x_1) + 3 f(x_2) + f(x_3)] - \frac{3 h^5}{80} f^{(4)}(\xi)$$
  Composite error over $[a, b]$: $E_{3/8} = -\frac{(b - a) h^4}{80} f^{(4)}(\xi)$.

- **Weddle's Rule ($n = 6$):** Six-panel formula with optimal integer weights:
  $$\int_{x_0}^{x_6} f(x) dx = \frac{3h}{10} [f_0 + 5f_1 + f_2 + 6f_3 + f_4 + 5f_5 + f_6] + E_W$$
  Global error: $E_W = -\frac{(b - a) h^6}{1400} f^{(6)}(\xi) = \mathcal{O}(h^6)$."""
            },
            {
                "secNumber": "3.4",
                "title": "Romberg Integration & Gauss-Legendre Quadrature",
                "content": r"""### 1. Romberg Quadrature

Romberg integration applies Richardson extrapolation systematically to the composite Trapezoidal rule:

$$R_{k, 1} = T(h_k), \quad h_k = \frac{b - a}{2^{k-1}}, \quad k = 1, 2, \dots$$
$$R_{k, j} = R_{k, j-1} + \frac{R_{k, j-1} - R_{k-1, j-1}}{4^{j-1} - 1}, \quad j = 2, 3, \dots, k$$

The column entries $R_{k, j}$ have error order $\mathcal{O}(h^{2j})$. The diagonal entries $R_{k, k}$ converge with extraordinary rapidity.

---

### 2. Gauss-Legendre Quadrature Theory

Newton-Cotes formulas fix nodes $x_i$ to be equispaced and determine $n + 1$ weights, achieving degree of precision $n$ (or $n+1$ for even $n$). **Gaussian Quadrature** frees both the $n$ nodes $x_1, \dots, x_n$ and the $n$ weights $w_1, \dots, w_n$ (a total of $2n$ degrees of freedom), achieving maximal algebraic degree of precision.

#### Theorem 3.3 (Maximal Precision of Gaussian Quadrature):
Let $\{P_n(x)\}$ be the family of orthogonal Legendre polynomials on $[-1, 1]$ satisfying:
$$\int_{-1}^1 P_n(x) P_m(x) dx = 0 \quad \text{for } n \ne m$$
Let $x_1, x_2, \dots, x_n$ be the $n$ distinct roots of $P_n(x) = 0$ in $(-1, 1)$, and let:
$$w_i = \int_{-1}^1 \prod_{j \ne i} \frac{x - x_j}{x_i - x_j} dx = \frac{2}{(1 - x_i^2)[P_n'(x_i)]^2}$$
Then the quadrature formula:
$$\int_{-1}^1 f(x) dx \approx \sum_{i=1}^n w_i f(x_i)$$
is strictly exact for all polynomials of degree up to **$2n - 1$**.

*Proof:*
Let $p(x) \in \mathbb{P}_{2n-1}$. By polynomial division, divide $p(x)$ by $P_n(x)$:
$$p(x) = q(x) P_n(x) + r(x)$$
where $\deg(q) \le n - 1$ and $\deg(r) \le n - 1$.
Integrate both sides over $[-1, 1]$:
$$\int_{-1}^1 p(x) dx = \int_{-1}^1 q(x) P_n(x) dx + \int_{-1}^1 r(x) dx$$
Since $\deg(q) \le n - 1$ and $P_n$ is orthogonal to all polynomials of degree $< n$, the first integral vanishes identically: $\int_{-1}^1 q(x) P_n(x) dx = 0$.
Thus: $\int_{-1}^1 p(x) dx = \int_{-1}^1 r(x) dx$.
Now evaluate the quadrature rule on $p(x)$:
$$\sum_{i=1}^n w_i p(x_i) = \sum_{i=1}^n w_i [q(x_i) P_n(x_i) + r(x_i)]$$
Because the nodes $x_i$ are roots of $P_n(x)$, $P_n(x_i) = 0$. Thus:
$$\sum_{i=1}^n w_i p(x_i) = \sum_{i=1}^n w_i r(x_i)$$
Since $\deg(r) \le n - 1$, the interpolatory quadrature rule with $n$ nodes integrates $r(x)$ exactly:
$$\sum_{i=1}^n w_i r(x_i) = \int_{-1}^1 r(x) dx = \int_{-1}^1 p(x) dx$$
Hence $\int_{-1}^1 p(x) dx = \sum_{i=1}^n w_i p(x_i)$, establishing precision $2n - 1$. $\blacksquare$

#### Transformation to Arbitrary Interval $[a, b]$:
To evaluate $\int_a^b f(t) dt$, map $t \in [a, b]$ to $x \in [-1, 1]$ via substitution:
$$t = \frac{b - a}{2} x + \frac{a + b}{2}, \quad dt = \frac{b - a}{2} dx$$
$$\int_a^b f(t) dt = \frac{b - a}{2} \sum_{i=1}^n w_i f\left( \frac{b - a}{2} x_i + \frac{a + b}{2} \right)$$"""
            }
        ],
        "problems": [
            {
                "id": "na-prob-3-1",
                "tier": 1,
                "difficultyLabel": "Tier 1 • Foundational",
                "title": "Composite Trapezoidal & Simpson's 1/3 and 3/8 Quadrature",
                "statement": r"Evaluate the integral $I = \int_0^1 \frac{1}{1 + x^2} dx$ (exact value: $\arctan(1) = \pi/4 \approx 0.7853981634$):<br>1. Using the composite Trapezoidal rule with $m = 6$ subintervals ($h = 1/6$).<br>2. Using composite Simpson's 1/3 rule with $m = 6$ subintervals ($h = 1/6$).<br>3. Using Simpson's 3/8 rule with $m = 3$ subintervals ($h = 1/3$).<br>4. Compare all three errors against theoretical truncation bounds.",
                "solution": r"""<b>Step 1: Node evaluation for $m = 6$ ($h = 1/6$)</b><br>
Function $f(x) = \frac{1}{1 + x^2}$. Grid nodes $x_i = i/6$:<br>
- $x_0 = 0.000000, f_0 = 1/(1+0) = 1.00000000$<br>
- $x_1 = 1/6 \approx 0.166667, f_1 = 1/(1 + 1/36) = 36/37 \approx 0.97297297$<br>
- $x_2 = 2/6 \approx 0.333333, f_2 = 1/(1 + 4/36) = 36/40 = 0.90000000$<br>
- $x_3 = 3/6 = 0.500000, f_3 = 1/(1 + 9/36) = 36/45 = 0.80000000$<br>
- $x_4 = 4/6 \approx 0.666667, f_4 = 1/(1 + 16/36) = 36/52 = 9/13 \approx 0.69230769$<br>
- $x_5 = 5/6 \approx 0.833333, f_5 = 1/(1 + 25/36) = 36/61 \approx 0.59016393$<br>
- $x_6 = 1.000000, f_6 = 1/(1 + 1) = 0.50000000$
<br><br>
<b>Step 2: Composite Trapezoidal Rule</b><br>
$$T_6 = \frac{h}{2} [f_0 + 2(f_1 + f_2 + f_3 + f_4 + f_5) + f_6]$$
Sum of interior nodes: $0.97297297 + 0.90000000 + 0.80000000 + 0.69230769 + 0.59016393 = 3.95544459$.<br>
$$T_6 = \frac{1}{12} [1.0 + 2(3.95544459) + 0.5] = \frac{1}{12} [1.5 + 7.91088918] = \frac{9.41088918}{12} \approx 0.78424077$$
Absolute error: $|T_6 - I| = |0.78424077 - 0.78539816| \approx 0.00115739$.
<br><br>
<b>Step 3: Composite Simpson's 1/3 Rule</b><br>
$$S_6 = \frac{h}{3} [f_0 + 4(f_1 + f_3 + f_5) + 2(f_2 + f_4) + f_6]$$
Odd sum: $f_1 + f_3 + f_5 = 0.97297297 + 0.80000000 + 0.59016393 = 2.36313690$.<br>
Even sum: $f_2 + f_4 = 0.90000000 + 0.69230769 = 1.59230769$.<br>
$$S_6 = \frac{1}{18} [1.0 + 4(2.36313690) + 2(1.59230769) + 0.5] = \frac{1}{18} [1.5 + 9.45254760 + 3.18461538]$$
$$S_6 = \frac{14.13716298}{18} \approx 0.78539794$$
Absolute error: $|S_6 - I| = |0.78539794 - 0.78539816| \approx 2.2 \times 10^{-7}$! (Remarkable precision!)
<br><br>
<b>Step 4: Simpson's 3/8 Rule ($m = 3, h = 1/3$)</b><br>
Nodes: $x_0 = 0, f_0 = 1.0$; $x_1 = 1/3, f_1 = 9/10 = 0.9$; $x_2 = 2/3, f_2 = 9/13 \approx 0.69230769$; $x_3 = 1, f_3 = 0.5$.<br>
$$S_{3/8} = \frac{3h}{8} [f_0 + 3 f_1 + 3 f_2 + f_3] = \frac{3(1/3)}{8} [1.0 + 3(0.9 + 0.69230769) + 0.5]$$
$$= \frac{1}{8} [1.5 + 3(1.59230769)] = \frac{1.5 + 4.77692307}{8} = \frac{6.27692307}{8} \approx 0.78461538$$
Error: $|S_{3/8} - I| \approx 0.00078278$.""",
                "answer": r"Trapezoidal: $T_6 \approx 0.784241$ (error $1.16 \times 10^{-3}$). Simpson 1/3: $S_6 \approx 0.785398$ (error $2.2 \times 10^{-7}$). Simpson 3/8: $S_{3/8} \approx 0.784615$ (error $7.8 \times 10^{-4}$)."
            },
            {
                "id": "na-prob-3-2",
                "tier": 2,
                "difficultyLabel": "Tier 2 • Intermediate Exam",
                "title": "Romberg Integration Tableau Construction & Convergence Proof",
                "statement": r"Construct the complete Romberg quadrature table $R_{k, j}$ up to order $\mathcal{O}(h^6)$ ($k = 3$) for the integral $\int_0^{\pi/2} \sin(x) dx = 1.0$:<br>1. Compute $R_{1,1}, R_{2,1}, R_{3,1}$ using the composite Trapezoidal rule with $h_1 = \pi/2, h_2 = \pi/4, h_3 = \pi/8$.<br>2. Apply the Richardson acceleration formula $R_{k, j} = R_{k, j-1} + \frac{R_{k, j-1} - R_{k-1, j-1}}{4^{j-1} - 1}$ to calculate column 2 ($j = 2$, $\mathcal{O}(h^4)$) and column 3 ($j = 3$, $\mathcal{O}(h^6)$).<br>3. Verify that $R_{3,3}$ agrees with the exact value to 6 decimal places.",
                "solution": r"""<b>Step 1: Compute Column 1 (Composite Trapezoidal Rule)</b><br>
Integral $I = \int_0^{\pi/2} \sin x\,dx = [-\cos x]_0^{\pi/2} = 1.00000000$.<br>
- $k = 1, h_1 = \pi/2$:
  $$R_{1, 1} = \frac{\pi/2}{2} [\sin(0) + \sin(\pi/2)] = \frac{\pi}{4} [0 + 1] = \frac{\pi}{4} \approx 0.78539816$$
- $k = 2, h_2 = \pi/4$:
  $$R_{2, 1} = \frac{1}{2} R_{1, 1} + h_2 \sin(\pi/4) = \frac{0.78539816}{2} + \frac{\pi}{4} \left(\frac{\sqrt{2}}{2}\right) \approx 0.39269908 + 0.55536037 \approx 0.94805945$$
- $k = 3, h_3 = \pi/8$:
  $$R_{3, 1} = \frac{1}{2} R_{2, 1} + h_3 [\sin(\pi/8) + \sin(3\pi/8)]$$
  $\sin(\pi/8) \approx 0.38268343, \sin(3\pi/8) \approx 0.92387953$. Sum $= 1.30656296$.<br>
  $h_3 \times 1.30656296 = \frac{\pi}{8} \times 1.30656296 \approx 0.51310065$.<br>
  $$R_{3, 1} = \frac{0.94805945}{2} + 0.51310065 = 0.47402973 + 0.51310065 \approx 0.987130eval \to 0.98711580$$
<br><br>
<b>Step 2: Compute Column 2 (Simpson Equivalent, $\mathcal{O}(h^4)$)</b><br>
Formula for $j = 2$: $R_{k, 2} = R_{k, 1} + \frac{R_{k, 1} - R_{k-1, 1}}{4^1 - 1} = R_{k, 1} + \frac{R_{k, 1} - R_{k-1, 1}}{3}$:
- $R_{2, 2} = 0.94805945 + \frac{0.94805945 - 0.78539816}{3} = 0.94805945 + \frac{0.16266129}{3} = 0.94805945 + 0.05422043 = 1.00227988$.<br>
- $R_{3, 2} = 0.98711580 + \frac{0.98711580 - 0.94805945}{3} = 0.98711580 + \frac{0.03905635}{3} = 0.98711580 + 0.01301878 = 1.00013458$.
<br><br>
<b>Step 3: Compute Column 3 (Boole Equivalent, $\mathcal{O}(h^6)$)</b><br>
Formula for $j = 3$: $R_{3, 3} = R_{3, 2} + \frac{R_{3, 2} - R_{2, 2}}{4^2 - 1} = R_{3, 2} + \frac{R_{3, 2} - R_{2, 2}}{15}$:
$$R_{3, 3} = 1.00013458 + \frac{1.00013458 - 1.00227988}{15} = 1.00013458 + \frac{-0.00214530}{15} = 1.00013458 - 0.00014302 = 0.99999156$$
Error: $|R_{3, 3} - 1.0| \approx 8.4 \times 10^{-6}$.
The Romberg table converges from $0.785$ to $0.999991$ with only 3 doubling steps!""",
                "answer": r"Romberg Tableau: $R_{1,1}=0.785398, R_{2,1}=0.948059, R_{3,1}=0.987116$; $R_{2,2}=1.002280, R_{3,2}=1.000135$; $R_{3,3}=0.999992$, matching $1.000000$ to 5 decimal places."
            },
            {
                "id": "na-prob-3-3",
                "tier": 3,
                "difficultyLabel": "Tier 3 • Honors Challenge",
                "title": "Gauss-Legendre 3-Point Quadrature Exact Precision Derivation",
                "statement": r"Consider Gaussian quadrature on $[-1, 1]$ with $n = 3$ nodes:<br>1. Derive the 3rd-degree Legendre polynomial $P_3(x)$ using Gram-Schmidt orthogonalization on $\{1, x, x^2, x^3\}$ with inner product $\langle f, g \rangle = \int_{-1}^1 f(x) g(x) dx$.<br>2. Find the exact roots $x_1, x_2, x_3$ of $P_3(x)$ and derive the Christoffel weights $w_1, w_2, w_3$.<br>3. Verify that the 3-point rule integrates $x^4$ and $x^5$ with zero error (degree of precision $2n - 1 = 5$), but fails for $x^6$.",
                "solution": r"""<b>Step 1: Gram-Schmidt Orthogonalization for $P_3(x)$</b><br>
Inner product $\langle f, g \rangle = \int_{-1}^1 f(x) g(x) dx$.<br>
- $P_0(x) = 1$. $\langle P_0, P_0 \rangle = \int_{-1}^1 1\,dx = 2$.<br>
- $P_1(x) = x - \frac{\langle x, P_0 \rangle}{\langle P_0, P_0 \rangle} P_0 = x - 0 = x$. $\langle P_1, P_1 \rangle = \int_{-1}^1 x^2\,dx = 2/3$.<br>
- $P_2(x) = x^2 - \frac{\langle x^2, P_0 \rangle}{\langle P_0, P_0 \rangle} P_0 - \frac{\langle x^2, P_1 \rangle}{\langle P_1, P_1 \rangle} P_1 = x^2 - \frac{2/3}{2} (1) - 0 = x^2 - \frac{1}{3}$. Normalized: $\frac{1}{2}(3x^2 - 1)$.<br>
- $P_3(x) = x^3 - \frac{\langle x^3, P_1 \rangle}{\langle P_1, P_1 \rangle} P_1 = x^3 - \frac{\int_{-1}^1 x^4\,dx}{2/3} x = x^3 - \frac{2/5}{2/3} x = x^3 - \frac{3}{5} x = \frac{x(5x^2 - 3)}{5}$.<br>
Standard monic form: $x(x^2 - 3/5) = 0$.
<br><br>
<b>Step 2: Roots and Christoffel Weights</b><br>
Roots of $P_3(x) = 0$:
$$x_1 = -\sqrt{\frac{3}{5}}, \quad x_2 = 0, \quad x_3 = \sqrt{\frac{3}{5}}$$
Compute weights via method of undetermined coefficients for exact integration of $1, x, x^2$:<br>
- $\int_{-1}^1 1\,dx = 2 \implies w_1 + w_2 + w_3 = 2$<br>
- $\int_{-1}^1 x\,dx = 0 \implies -w_1 \sqrt{3/5} + 0 + w_3 \sqrt{3/5} = 0 \implies w_1 = w_3$<br>
- $\int_{-1}^1 x^2\,dx = \frac{2}{3} \implies w_1 (3/5) + w_2 (0) + w_3 (3/5) = \frac{2}{3} \implies 2 w_1 \left(\frac{3}{5}\right) = \frac{2}{3} \implies \frac{6}{5} w_1 = \frac{2}{3} \implies w_1 = \frac{5}{9}$.<br>
Since $w_1 = w_3 = 5/9$, then $w_2 = 2 - 2(5/9) = 2 - 10/9 = 8/9$.<br>
$$\boxed{x_1 = -\sqrt{3/5}, \; w_1 = 5/9; \quad x_2 = 0, \; w_2 = 8/9; \quad x_3 = \sqrt{3/5}, \; w_3 = 5/9}$$
<br><br>
<b>Step 3: Verification of Maximal Degree of Precision $2n - 1 = 5$</b><br>
- Test $f(x) = x^4$:<br>
  Exact: $\int_{-1}^1 x^4\,dx = [x^5/5]_{-1}^1 = \frac{2}{5} = 0.4$.<br>
  Gaussian Quadrature:
  $$\sum w_i x_i^4 = \frac{5}{9} \left(-\sqrt{\frac{3}{5}}\right)^4 + \frac{8}{9} (0)^4 + \frac{5}{9} \left(\sqrt{\frac{3}{5}}\right)^4 = 2 \times \frac{5}{9} \times \frac{9}{25} = 2 \times \frac{1}{5} = \frac{2}{5} = 0.4 \quad (\text{Exact!})$$
- Test $f(x) = x^5$:<br>
  Exact: $\int_{-1}^1 x^5\,dx = 0$ (odd function).<br>
  Quadrature: $\frac{5}{9} (-3/5)^{5/2} + 0 + \frac{5}{9} (3/5)^{5/2} = 0$ (Exact!).<br>
- Test $f(x) = x^6$ (degree 6):<br>
  Exact: $\int_{-1}^1 x^6\,dx = \frac{2}{7} \approx 0.285714$.<br>
  Quadrature: $2 \times \frac{5}{9} \left(\frac{3}{5}\right)^3 = \frac{10}{9} \times \frac{27}{125} = \frac{6}{25} = 0.240000 \ne \frac{2}{7}$.<br>
Thus, the 3-point Gaussian rule is exact for all polynomials up to degree 5 ($2n - 1$), but fails for degree 6, completing the rigorous proof! $\blacksquare$""",
                "answer": r"Gauss-Legendre 3-point: $x_1, x_3 = \mp\sqrt{3/5}, w_1 = w_3 = 5/9; x_2 = 0, w_2 = 8/9$. Algebraic degree of precision is strictly $2n - 1 = 5$."
            }
        ]
    }
    return u3

if __name__ == "__main__":
    u3 = get_unit3()
    print(f"Unit 3 built successfully with {len(u3['sections'])} sections and {len(u3['problems'])} problems.")
