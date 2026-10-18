# -*- coding: utf-8 -*-
"""
build_unit6.py
Constructs Unit 6: Convergence & Error Analysis for Initial Value Problems
"""

def get_unit6():
    u6 = {
        "number": 6,
        "title": "Convergence & Error Analysis for Initial Value Problems",
        "leadSummary": "Rigorous framework of Local Truncation Error (LTE) versus Global Truncation Error (GTE), consistency, discrete Gronwall inequality, global convergence theorem for Lipschitz vector fields, and step-size adaptation.",
        "simulations": ["sim_na_convergence_order"],
        "sections": [
            {
                "secNumber": "6.1",
                "title": "Local Truncation Error (LTE), Consistency & Global Truncation Error (GTE)",
                "content": r"""### 1. General One-Step Numerical Integrator

Any autonomous or non-autonomous one-step method can be expressed in the canonical form:
$$y_{n+1} = y_n + h \Phi(t_n, y_n; h)$$
where $\Phi: [t_0, T] \times \mathbb{R}^d \times [0, h_0] \to \mathbb{R}^d$ is the continuous **increment function**.

---

### 2. Formal Definitions of Error and Consistency

Let $y(t)$ denote the exact analytical solution of the IVP $y' = f(t, y), y(t_0) = y_0$.

#### Definition 1: Local Truncation Error (LTE)
The local truncation error $d_{n+1}$ (or residual defect) is the error introduced in a single step starting from the exact trajectory:
$$d_{n+1} = y(t_{n+1}) - \left[ y(t_n) + h \Phi(t_n, y(t_n); h) \right]$$
The **local truncation error per unit step** is defined by:
$$\tau_n(h) = \frac{d_{n+1}}{h} = \frac{y(t_{n+1}) - y(t_n)}{h} - \Phi(t_n, y(t_n); h)$$

#### Definition 2: Consistency
A numerical method is said to be **consistent** with the ODE if the local truncation error per unit step vanishes as $h \to 0$:
$$\lim_{h \to 0} \max_{0 \le n \le N-1} \|\tau_n(h)\| = 0$$
Since $\lim_{h \to 0} \frac{y(t_{n+1}) - y(t_n)}{h} = y'(t_n) = f(t_n, y(t_n))$, consistency is mathematically equivalent to:
$$\Phi(t, y; 0) = f(t, y) \quad \forall (t, y)$$

#### Definition 3: Order of Consistency
A numerical method has **order of consistency $p$** if there exists a constant $C > 0$ such that:
$$\|\tau_n(h)\| \le C h^p \iff \|d_{n+1}\| \le C h^{p+1}$$
as $h \to 0$ for all sufficiently smooth solutions $y(t)$.

---

### 3. Global Truncation Error (GTE)

#### Definition 4: Global Error
The true global error at grid point $t_n = t_0 + n h$ is the accumulated difference:
$$e_n = y(t_n) - y_n$$
A numerical method is **convergent of order $p$** if:
$$\max_{0 \le n \le N} \|e_n\| = \mathcal{O}(h^p) \quad \text{as } h \to 0 \text{ with } N h = T - t_0$$
*The fundamental question of numerical analysis:* Under what mathematical conditions does local consistency of order $p$ ($\tau = \mathcal{O}(h^p)$) guarantee global convergence of order $p$ ($\|e_n\| = \mathcal{O}(h^p)$)?"""
            },
            {
                "secNumber": "6.2",
                "title": "The Discrete Gronwall Lemma & Proof of Global Convergence",
                "content": r"""### 1. The Discrete Gronwall Inequality

The fundamental analytical tool for proving convergence in difference equations is the discrete analog of the Gronwall-Bellman inequality.

> **Lemma (Discrete Gronwall Inequality):**
> Let $\{z_n\}_{n=0}^N$ be a sequence of non-negative real numbers satisfying:
> $$z_{n+1} \le (1 + A) z_n + B, \quad \forall n = 0, 1, \dots, N-1$$
> where $A > 0$ and $B \ge 0$. Then:
> $$z_n \le e^{n A} z_0 + B \frac{e^{n A} - 1}{A}, \quad \forall n = 0, 1, \dots, N$$

#### Proof:
Unrolling the recursion:
$$\begin{aligned}
z_1 &\le (1 + A) z_0 + B \\
z_2 &\le (1 + A)^2 z_0 + B [1 + (1 + A)] \\
&\;\;\vdots \\
z_n &\le (1 + A)^n z_0 + B \sum_{k=0}^{n-1} (1 + A)^k
\end{aligned}$$
Summing the geometric progression $\sum_{k=0}^{n-1} (1 + A)^k = \frac{(1 + A)^n - 1}{A}$:
$$z_n \le (1 + A)^n z_0 + B \frac{(1 + A)^n - 1}{A}$$
Using the elementary inequality $1 + A \le e^A$ for all $A \ge 0$, we have $(1 + A)^n \le e^{n A}$. Substituting this yields the result. $\blacksquare$

---

### 2. The Global Convergence Theorem

> **Theorem (Convergence of One-Step Methods):**
> Consider the IVP $y' = f(t, y), y(t_0) = y_0$ on $[t_0, T]$. Assume:
> 1. The increment function $\Phi(t, y; h)$ is Lipschitz continuous in $y$ with Lipschitz constant $L_\Phi$:
>    $$\|\Phi(t, u; h) - \Phi(t, v; h)\| \le L_\Phi \|u - v\|$$
> 2. The method is consistent of order $p$: $\|\tau_n(h)\| \le C h^p$.
> 3. The initial error satisfies $\|e_0\| = \|y(t_0) - y_0\| \le C_0 h^p$.
> 
> Then the global truncation error satisfies:
> $$\|e_n\| \le e^{L_\Phi (t_n - t_0)} \|e_0\| + \frac{C h^p}{L_\Phi} \left( e^{L_\Phi (t_n - t_0)} - 1 \right) = \mathcal{O}(h^p)$$
> for all $n \le N = (T - t_0)/h$.

#### Proof:
By definition of the numerical method and exact solution:
$$y_{n+1} = y_n + h \Phi(t_n, y_n; h)$$
$$y(t_{n+1}) = y(t_n) + h \Phi(t_n, y(t_n); h) + h \tau_n(h)$$
Subtracting the numerical scheme from the exact expansion:
$$e_{n+1} = e_n + h \left[ \Phi(t_n, y(t_n); h) - \Phi(t_n, y_n; h) \right] + h \tau_n(h)$$
Applying the triangle inequality and Lipschitz property of $\Phi$:
$$\|e_{n+1}\| \le \|e_n\| + h L_\Phi \|e_n\| + h \|\tau_n(h)\| = (1 + h L_\Phi) \|e_n\| + C h^{p+1}$$
Set $z_n = \|e_n\|$, $A = h L_\Phi$, and $B = C h^{p+1}$ in the Discrete Gronwall Lemma:
$$\|e_n\| \le e^{n h L_\Phi} \|e_0\| + C h^{p+1} \frac{e^{n h L_\Phi} - 1}{h L_\Phi}$$
Since $n h = t_n - t_0$:
$$\|e_n\| \le e^{L_\Phi (t_n - t_0)} \|e_0\| + \frac{C h^p}{L_\Phi} \left( e^{L_\Phi (t_n - t_0)} - 1 \right)$$
As $h \to 0$, $\|e_n\| \to 0$ uniformly on $[t_0, T]$. This proves unconditional global convergence of order $p$. $\blacksquare$"""
            },
            {
                "secNumber": "6.3",
                "title": "Propagation of Round-Off Errors & Optimal Step Size Selection",
                "content": r"""### 1. Interplay of Truncation Error and Round-Off Error

In finite-precision floating-point arithmetic (IEEE 754), each evaluation of the increment function introduces a round-off error $\epsilon_n \in \mathbb{R}^d$, bounded by machine epsilon:
$$\|\epsilon_n\| \le \epsilon_{\text{mach}} \approx 1.11 \times 10^{-16} \text{ (double precision)}$$
The actual computed sequence $\{\tilde{y}_n\}$ satisfies:
$$\tilde{y}_{n+1} = \tilde{y}_n + h \Phi(t_n, \tilde{y}_n; h) + \epsilon_n$$
The total computational error $\tilde{e}_n = y(t_n) - \tilde{y}_n$ combines truncation error and floating-point round-off:
$$\|\tilde{e}_{n+1}\| \le (1 + h L) \|\tilde{e}_n\| + C h^{p+1} + \epsilon_{\text{mach}}$$
Applying Gronwall's inequality:
$$\|\tilde{e}_n\| \le \frac{e^{L(T - t_0)} - 1}{L} \left( C h^p + \frac{\epsilon_{\text{mach}}}{h} \right)$$

---

### 2. The Optimal Step Size Trade-Off

The total error bound as a function of step size $h$ is:
$$\mathcal{E}(h) = C_1 h^p + \frac{C_2 \epsilon_{\text{mach}}}{h}$$
- For large $h$, truncation error $C_1 h^p$ dominates.
- For small $h$, round-off error $\frac{C_2 \epsilon_{\text{mach}}}{h}$ blows up as $\mathcal{O}(h^{-1})$ due to accumulation across $N = \mathcal{O}(h^{-1})$ steps!

#### Minimizing Total Error:
Differentiating $\mathcal{E}(h)$ with respect to $h$ and equating to zero:
$$\frac{d\mathcal{E}}{dh} = p C_1 h^{p-1} - \frac{C_2 \epsilon_{\text{mach}}}{h^2} = 0 \implies h_{\text{optimal}} = \left( \frac{C_2 \epsilon_{\text{mach}}}{p C_1} \right)^{\frac{1}{p+1}}$$

| Method | Order $p$ | Scaling of $h_{\text{opt}}$ | Approximate $h_{\text{opt}}$ (Double Prec.) |
| :--- | :--- | :--- | :--- |
| Forward Euler | $p = 1$ | $\sim \sqrt{\epsilon_{\text{mach}}}$ | $\sim 10^{-8}$ |
| Heun / RK2 | $p = 2$ | $\sim \epsilon_{\text{mach}}^{1/3}$ | $\sim 10^{-5.3}$ |
| Classical RK4 | $p = 4$ | $\sim \epsilon_{\text{mach}}^{1/5}$ | $\sim 10^{-3.2}$ |

This confirms why higher-order methods are so computationally superior: RK4 reaches near-machine accuracy with step sizes around $10^{-3}$, while Euler would require $10^8$ steps and suffer devastating round-off accumulation."""
            },
            {
                "secNumber": "6.4",
                "title": "Adaptive Step-Size Control & Embedded Runge-Kutta Pairs",
                "content": r"""### 1. Step Doubling (Richardson Extrapolation)

To dynamically adapt $h$ to maintain a user-specified tolerance $\text{TOL}$, we need an accurate local error estimate $E_n \approx d_{n+1}$.
In **step doubling**:
1. Take one step of size $2h$ from $t_n$ to get $y^{(1)}$.
2. Take two steps of size $h$ from $t_n$ to get $y^{(2)}$.
Assuming order $p$, the local errors satisfy:
$$y(t_n + 2h) - y^{(1)} = C (2h)^{p+1} + \mathcal{O}(h^{p+2}) = 2^{p+1} C h^{p+1}$$
$$y(t_n + 2h) - y^{(2)} = 2 C h^{p+1} + \mathcal{O}(h^{p+2})$$
Subtracting the two solutions isolates the local error:
$$y^{(2)} - y^{(1)} = (2^{p+1} - 2) C h^{p+1} \implies \text{Error Estimate: } E_n = \frac{\|y^{(2)} - y^{(1)}\|}{2^p - 1}$$
*Cost:* Requires $3$ times the work per accepted step!

---

### 2. Embedded Runge-Kutta Pairs (Fehlberg, Dormand-Prince)

Erwin Fehlberg (1969) realized that two Runge-Kutta methods of orders $p$ and $p+1$ (or $p$ and $p-1$) can be constructed that **share the exact same stage evaluations $\{k_i\}$**:
$$\begin{aligned}
y_{n+1} &= y_n + h \sum_{i=1}^s b_i k_i \quad (\text{Order } p) \\
\hat{y}_{n+1} &= y_n + h \sum_{i=1}^s \hat{b}_i k_i \quad (\text{Order } p+1)
\end{aligned}$$
The local truncation error estimate is computed for **zero additional function evaluations**:
$$E_{n+1} = \|\hat{y}_{n+1} - y_{n+1}\| = h \left\| \sum_{i=1}^s (\hat{b}_i - b_i) k_i \right\|$$

#### The Adaptive Step-Size Update Law:
If $E_{n+1} \le \text{TOL}$, the step is **accepted**.
If $E_{n+1} > \text{TOL}$, the step is **rejected** and repeated.
In either case, the optimal next step size $h_{\text{new}}$ is governed by the asymptotic scaling $E \propto h^{p+1}$:
$$h_{\text{new}} = h \cdot \min\left( \text{fac}_{\max}, \, \max\left( \text{fac}_{\min}, \, S \left( \frac{\text{TOL}}{E_{n+1}} \right)^{\frac{1}{p+1}} \right) \right)$$
where $S \approx 0.85 - 0.90$ is a conservative safety factor, and $\text{fac}_{\min} \approx 0.2, \text{fac}_{\max} \approx 5.0$ prevent erratic step fluctuations."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Consistency and Local Truncation Error of a Multi-Stage Increment Function",
                "statement": r"Consider the explicit one-step method: $$y_{n+1} = y_n + h \left[ \frac{1}{4} f(t_n, y_n) + \frac{3}{4} f\left(t_n + \frac{2}{3} h, y_n + \frac{2}{3} h f(t_n, y_n)\right) \right]$$ 1. Identify the increment function $\Phi(t, y; h)$ and prove whether the method is consistent with $y' = f(t, y)$. 2. Expand $\Phi(t, y; h)$ in powers of $h$ and determine the order of consistency $p$ and the principal local truncation error term.",
                "hints": [
                    "Consistency requires $\\Phi(t, y; 0) = f(t, y)$.",
                    "Use bivariate Taylor expansion for $f(t + \\frac{2}{3}h, y + \\frac{2}{3}h f)$."
                ],
                "solution": r"""**Step 1: Increment Function and Consistency**
The increment function is:
$$\Phi(t, y; h) = \frac{1}{4} f(t, y) + \frac{3}{4} f\left(t + \frac{2}{3} h, \, y + \frac{2}{3} h f(t, y)\right)$$
Setting $h = 0$:
$$\Phi(t, y; 0) = \frac{1}{4} f(t, y) + \frac{3}{4} f(t, y) = \left( \frac{1}{4} + \frac{3}{4} \right) f(t, y) = f(t, y)$$
Since $\Phi(t, y; 0) \equiv f(t, y)$, the method is **strictly consistent**.

---

**Step 2: Taylor Expansion of $\Phi$ and Order Determination**
Expand the second evaluation using bivariate Taylor series:
$$f\left(t + \frac{2}{3} h, \, y + \frac{2}{3} h f\right) = f + \frac{2}{3} h f_t + \frac{2}{3} h f f_y + \frac{1}{2} \left( \frac{4}{9} h^2 f_{tt} + \frac{8}{9} h^2 f f_{ty} + \frac{4}{9} h^2 f^2 f_{yy} \right) + \mathcal{O}(h^3)$$
Substitute into $\Phi(t, y; h)$:
$$\begin{aligned}
\Phi(t, y; h) &= \frac{1}{4} f + \frac{3}{4} \left[ f + \frac{2}{3} h (f_t + f f_y) + \frac{2}{9} h^2 (f_{tt} + 2 f f_{ty} + f^2 f_{yy}) + \mathcal{O}(h^3) \right] \\
&= f + \frac{1}{2} h (f_t + f f_y) + \frac{1}{6} h^2 (f_{tt} + 2 f f_{ty} + f^2 f_{yy}) + \mathcal{O}(h^3)
\end{aligned}$$

Now compare with the true Taylor expansion of the exact solution:
$$\frac{y(t + h) - y(t)}{h} = y' + \frac{h}{2} y'' + \frac{h^2}{6} y''' + \mathcal{O}(h^3)$$
where:
$$y' = f$$
$$y'' = f_t + f f_y$$
$$y''' = (f_{tt} + 2 f f_{ty} + f^2 f_{yy}) + f_y (f_t + f f_y)$$

Compute the local truncation error per unit step:
$$\begin{aligned}
\tau(h) &= \frac{y(t + h) - y(t)}{h} - \Phi(t, y; h) \\
&= \left[ f - f \right] + h \left[ \frac{1}{2} (f_t + f f_y) - \frac{1}{2} (f_t + f f_y) \right] \\
&\quad + h^2 \left[ \frac{1}{6} y''' - \frac{1}{6} (f_{tt} + 2 f f_{ty} + f^2 f_{yy}) \right] + \mathcal{O}(h^3) \\
&= \frac{h^2}{6} f_y (f_t + f f_y) + \mathcal{O}(h^3)
\end{aligned}$$
Since $\tau(h) = \mathcal{O}(h^2)$ and does not vanish for general $f$, the method has **order of consistency $p = 2$** (second-order accuracy, matching Ralston's RK2 method)."""
            },
            {
                "tier": "Advanced",
                "title": "Adaptive Step-Size Controller: Rejection, Acceptance and Scaling",
                "statement": r"An embedded Runge-Kutta pair of orders 4 and 5 (such as RKF45) is applied to an IVP with user tolerance $\text{TOL} = 1.0 \times 10^{-5}$ and safety factor $S = 0.9$. 1. At step $n$, using current step size $h_n = 0.1$, the 4th-order solution is $y_{n+1} = 2.451820$ and the 5th-order solution is $\hat{y}_{n+1} = 2.451892$. Determine if the step is accepted or rejected, and compute the adjusted step size $h_{n+1}$. 2. If at the next accepted step the estimated error drops to $E = 1.2 \times 10^{-7}$, compute the accelerated step size proposed for the subsequent interval.",
                "hints": [
                    "Error estimate is $E = |\\hat{y}_{n+1} - y_{n+1}|$.",
                    "For a $(p, p+1)$ pair, the error estimate scales as $h^{p+1}$. Here $p=4$, so exponent is $\\frac{1}{p+1} = \\frac{1}{5} = 0.2$."
                ],
                "solution": r"""**Step 1: Analysis at $h_n = 0.1$**
Compute the local error estimate:
$$E = |\hat{y}_{n+1} - y_{n+1}| = |2.451892 - 2.451820| = 0.000072 = 7.2 \times 10^{-5}$$
Compare with tolerance:
$$\text{TOL} = 1.0 \times 10^{-5}$$
Since $E = 7.2 \times 10^{-5} > 1.0 \times 10^{-5}$, the error violates tolerance.
Therefore, the step is **REJECTED** and must be recomputed!

Compute the scaled step size:
$$h_{\text{retry}} = h_n \cdot S \left( \frac{\text{TOL}}{E} \right)^{1/5} = 0.1 \cdot 0.9 \left( \frac{1.0 \times 10^{-5}}{7.2 \times 10^{-5}} \right)^{0.2} = 0.09 \cdot \left( \frac{1}{7.2} \right)^{0.2}$$
Evaluating:
$$\left( \frac{1}{7.2} \right)^{0.2} \approx 0.6756$$
$$h_{\text{retry}} = 0.09 \times 0.6756 \approx 0.0608$$
The solver shrinks the step size to $h \approx 0.0608$ and repeats the step from $t_n$.

---

**Step 2: Analysis when $E = 1.2 \times 10^{-7}$**
Assuming current step size is $h = 0.0608$:
Since $E = 1.2 \times 10^{-7} \le 1.0 \times 10^{-5}$, the step is **ACCEPTED**.

Compute the expanded step size for the subsequent step:
$$h_{\text{next}} = h \cdot S \left( \frac{\text{TOL}}{E} \right)^{1/5} = 0.0608 \cdot 0.9 \left( \frac{1.0 \times 10^{-5}}{1.2 \times 10^{-7}} \right)^{0.2} = 0.05472 \cdot \left( 83.333 \right)^{0.2}$$
Evaluating:
$$(83.333)^{0.2} \approx 2.418$$
$$h_{\text{next}} = 0.05472 \times 2.418 \approx 0.1323$$
The solver successfully expands the step size from $0.0608$ to $0.1323$ (an increase of $\approx 2.17\times$), maximizing execution efficiency without sacrificing accuracy."""
            },
            {
                "tier": "Rigorous Examination / Derivation",
                "title": "Comprehensive Proof of the Discrete Gronwall Inequality",
                "statement": r"Let $\{z_n\}_{n=0}^N$ be a sequence of real numbers satisfying the linear recurrence: $$z_{n+1} \le (1 + A) z_n + B, \quad n \ge 0$$ where $A > 0$ and $B \ge 0$. 1. Prove by induction that: $$z_n \le (1 + A)^n z_0 + B \frac{(1 + A)^n - 1}{A}, \quad \forall n \ge 0$$ 2. Using the convexity of $e^x$, prove that $(1 + A)^n \le e^{n A}$ for all $A \ge 0$ and establish the exponential upper bound: $$z_n \le e^{n A} z_0 + \frac{B}{A} (e^{n A} - 1)$$ 3. Apply this bound to Forward Euler for $y' = \lambda y, y(0) = 1$ to demonstrate the precise growth of global error.",
                "hints": [
                    "For induction, the base case $n=0$ is trivial since $(1+A)^0 - 1 = 0$.",
                    "Recall that $e^x \\ge 1 + x$ for all $x \\in \\mathbb{R}$ by Taylor's theorem with Lagrange remainder."
                ],
                "solution": r"""**Part 1: Proof of Algebraic Bound by Mathematical Induction**

**Base Case ($n = 0$):**
For $n = 0$:
$$(1 + A)^0 z_0 + B \frac{(1 + A)^0 - 1}{A} = 1 \cdot z_0 + B \frac{1 - 1}{A} = z_0$$
Since $z_0 \le z_0$, the base case holds with equality.

**Inductive Step:**
Assume the hypothesis holds for $n = k$:
$$z_k \le (1 + A)^k z_0 + B \frac{(1 + A)^k - 1}{A}$$
We must show it holds for $n = k + 1$. From the given recurrence:
$$z_{k+1} \le (1 + A) z_k + B$$
Substituting the inductive hypothesis:
$$\begin{aligned}
z_{k+1} &\le (1 + A) \left[ (1 + A)^k z_0 + B \frac{(1 + A)^k - 1}{A} \right] + B \\
&= (1 + A)^{k+1} z_0 + B \left[ \frac{(1 + A)^{k+1} - (1 + A)}{A} + 1 \right] \\
&= (1 + A)^{k+1} z_0 + B \left[ \frac{(1 + A)^{k+1} - 1 - A + A}{A} \right] \\
&= (1 + A)^{k+1} z_0 + B \frac{(1 + A)^{k+1} - 1}{A}
\end{aligned}$$
This completes the induction. Hence the inequality holds for all $n \ge 0$. $\blacksquare$

---

**Part 2: Exponential Upper Bound**

By Taylor's theorem, for any $x \ge 0$:
$$e^x = 1 + x + \frac{x^2}{2} e^\xi \ge 1 + x \quad (\xi \in [0, x])$$
Setting $x = A \ge 0$, we have $1 + A \le e^A$.
Raising both sides to the non-negative integer power $n$:
$$(1 + A)^n \le (e^A)^n = e^{n A}$$
Substituting this into the algebraic bound from Part 1:
$$z_n \le (1 + A)^n z_0 + \frac{B}{A} [(1 + A)^n - 1] \le e^{n A} z_0 + \frac{B}{A} (e^{n A} - 1)$$
This proves the continuous exponential Gronwall bound. $\blacksquare$

---

**Part 3: Application to Forward Euler Global Error**

For $y' = \lambda y$ with Lipschitz constant $L = |\lambda|$, Forward Euler has LTE:
$$d_{n+1} = \frac{h^2}{2} y''(\xi_n) = \frac{h^2}{2} \lambda^2 e^{\lambda \xi_n} \le \frac{h^2}{2} M_2$$
where $M_2 = \max_{t \in [0, T]} |y''(t)|$.
The error recurrence is:
$$|e_{n+1}| \le (1 + h |\lambda|) |e_n| + \frac{h^2}{2} M_2$$
Here $A = h |\lambda|$ and $B = \frac{h^2}{2} M_2$. Since $e_0 = 0$, applying the Gronwall bound at $t_n = n h$:
$$|e_n| \le \frac{B}{A} (e^{n A} - 1) = \frac{\frac{h^2}{2} M_2}{h |\lambda|} \left( e^{n h |\lambda|} - 1 \right) = h \left[ \frac{M_2}{2 |\lambda|} \left( e^{|\lambda| t_n} - 1 \right) \right]$$
This proves conclusively that:
1. The global error is strictly linear in $h$: $|e_n| = \mathcal{O}(h)$.
2. The error growth constant scales exponentially with the length of the time integration interval $e^{|\lambda| T}$, showing why long-time integration requires specialized symplectic or higher-order methods."""
            }
        ]
    }
    return u6

if __name__ == "__main__":
    u = get_unit6()
    print("Unit 6 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
