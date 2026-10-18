# -*- coding: utf-8 -*-
"""
build_unit7.py
Constructs Unit 7: Absolute Stability Analysis, Stiff Differential Equations & Linear Multi-Step Methods
"""

def get_unit7():
    u7 = {
        "number": 7,
        "title": "Absolute Stability Analysis, Stiff Differential Equations & Linear Multi-Step Methods",
        "leadSummary": "Dahlquist test equation, stability regions in the complex plane, stiff differential equations, A-stability, L-stability, Padé rational approximations, explicit and implicit Linear Multi-Step Methods (Adams-Bashforth, Adams-Moulton, Milne-Simpson, BDF), characteristic polynomials rho(r), sigma(r), root condition, and Dahlquist's First and Second Stability Barriers.",
        "simulations": ["sim_na_stability_regions"],
        "sections": [
            {
                "secNumber": "7.1",
                "title": "The Dahlquist Test Equation, Amplification Factors & Stability Regions in C",
                "content": r"""### 1. Germund Dahlquist's Test Problem

To analyze whether numerical solutions remain bounded as $t \to \infty$ for fixed step size $h > 0$, Germund Dahlquist (1956) introduced the scalar complex test equation:
$$\frac{dy}{dt} = \lambda y, \quad \lambda \in \mathbb{C}, \quad \text{Re}(\lambda) < 0$$
The exact solution is $y(t) = y_0 e^{\lambda t}$. Since $\text{Re}(\lambda) < 0$, the exact solution asymptotically decays to zero:
$$\lim_{t \to \infty} |y(t)| = 0$$

Applying a numerical method with step size $h$ yields a discrete recurrence relation:
$$y_{n+1} = R(z) y_n, \quad z = h\lambda \in \mathbb{C}$$
where $R(z): \mathbb{C} \to \mathbb{C}$ is the **stability function** (or amplification factor).
After $n$ steps:
$$y_n = [R(z)]^n y_0$$

#### Definition: Region of Absolute Stability
The **region of absolute stability** $\mathcal{S} \subset \mathbb{C}$ is the set of complex parameters $z = h\lambda$ for which the numerical solution decays or remains bounded:
$$\mathcal{S} = \left\{ z \in \mathbb{C} : |R(z)| < 1 \right\}$$
Its boundary is the locus $\partial \mathcal{S} = \{ z \in \mathbb{C} : |R(z)| = 1 \}$.

---

### 2. Stability Functions for Classic Methods

#### 1. Forward Euler:
$$y_{n+1} = y_n + h(\lambda y_n) = (1 + z) y_n \implies R(z) = 1 + z$$
Stability condition: $|1 + z| < 1$, which is an **open disk of radius 1 centered at $z = -1$**.
On the negative real axis ($\lambda \in \mathbb{R}^-$), stable step sizes require:
$$-2 < h\lambda < 0 \implies h < \frac{2}{|\lambda|}$$

#### 2. Backward Euler (Implicit):
$$y_{n+1} = y_n + h\lambda y_{n+1} \implies (1 - z)y_{n+1} = y_n \implies R(z) = \frac{1}{1 - z}$$
Stability condition: $|1 - z| > 1$, which is the **exterior of the disk of radius 1 centered at $z = 1$**.
Notice that $\mathcal{S}$ includes the entire left half-plane $\mathbb{C}^- = \{z : \text{Re}(z) < 0\}$.

#### 3. Implicit Trapezoidal Rule (Crank-Nicolson):
$$y_{n+1} = y_n + \frac{h\lambda}{2}(y_n + y_{n+1}) \implies R(z) = \frac{1 + z/2}{1 - z/2}$$
For $\text{Re}(z) < 0$, $|1 + z/2| < |1 - z/2|$, so $|R(z)| < 1$ holds for **all** $z \in \mathbb{C}^-$.

#### 4. Explicit Runge-Kutta Methods of Order $p \le 4$:
For any explicit $p$-stage, $p$-th order RK method ($p = 1, 2, 3, 4$), the stability function is the truncated Taylor polynomial of $e^z$:
$$R(z) = \sum_{k=0}^p \frac{z^k}{k!} = 1 + z + \frac{z^2}{2!} + \dots + \frac{z^p}{p!}$$
For classical RK4:
$$R_{\text{RK4}}(z) = 1 + z + \frac{z^2}{2} + \frac{z^3}{6} + \frac{z^4}{24}$$
The interval of absolute stability on the real axis is approximately $(-2.78, 0)$, and it contains a segment of the imaginary axis $[-2\sqrt{2}i, 2\sqrt{2}i]$, making RK4 capable of integrating undamped wave oscillators."""
            },
            {
                "secNumber": "7.2",
                "title": "Stiff Differential Equations, Stiffness Ratio, A-Stability & L-Stability",
                "content": r"""### 1. The Phenomenon of Stiffness

Consider a linear system of differential equations:
$$\frac{d\vec{y}}{dt} = A \vec{y}, \quad A \in \mathbb{R}^{d \times d}$$
with eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_d$ such that $\text{Re}(\lambda_i) < 0$.

#### Definition: Stiffness Ratio
The system is called **stiff** if:
1. $\text{Re}(\lambda_i) < 0$ for all $i = 1, \dots, d$.
2. The stiffness ratio:
   $$S = \frac{\max_i |\text{Re}(\lambda_i)|}{\min_i |\text{Re}(\lambda_i)|} \gg 1 \quad (\text{typically } 10^3 \text{ to } 10^9)$$
*Physical Reality:* Stiff systems describe multi-scale dynamics—such as chemical kinetics, combustion, or structural mechanics—where fast transient modes decay almost instantaneously while slow master modes dominate the physical trajectory.

#### The Failure of Explicit Methods:
To keep explicit methods from experiencing exponential divergence, the step size $h$ is severely constrained by the fastest decaying eigenvalue:
$$h < \frac{C}{\max_i |\lambda_i|}$$
Even after the fast transient has decayed to zero ($10^{-10}$), an explicit integrator is forced to take millions of tiny steps purely to satisfy numerical stability, even though accuracy would permit a step size $10^6$ times larger!

---

### 2. A-Stability and L-Stability

To solve stiff problems efficiently, we require methods whose stability region encompasses the entire physics of decaying systems.

#### Definition 1: A-Stability (Dahlquist, 1963)
A numerical method is **A-stable** if its stability region contains the entire open left half-plane:
$$\mathbb{C}^- = \{ z \in \mathbb{C} : \text{Re}(z) < 0 \} \subset \mathcal{S}$$
For an A-stable method, **any step size $h > 0$ produces bounded solutions**, eliminating the stability bottleneck completely!

#### Definition 2: L-Stability (Stiff Decay)
While the Trapezoidal rule is A-stable, its stability function satisfies:
$$\lim_{\text{Re}(z) \to -\infty} R_{\text{Trap}}(z) = \lim_{z \to -\infty} \frac{1 + z/2}{1 - z/2} = -1$$
As a consequence, very stiff modes do not decay to zero; they oscillate wildly between $\pm y_0$!

A method is **L-stable** if:
1. It is A-stable.
2. Its stability function vanishes at infinity:
   $$\lim_{z \to -\infty} |R(z)| = 0$$
Backward Euler is L-stable since $\lim_{z \to -\infty} \frac{1}{1 - z} = 0$. Stiff solvers in production (e.g., Radau IIA, BDF) are L-stable, ensuring that stiff transients are damped out instantly."""
            },
            {
                "secNumber": "7.3",
                "title": "Linear Multi-Step Methods (LMMs): Adams Families & Predictor-Corrector Schemes",
                "content": r"""### 1. General Linear Multi-Step Framework

A linear $k$-step method uses numerical values and function derivatives from the $k$ preceding points $(y_{n+j}, f_{n+j})$ to compute $y_{n+k}$:
$$\sum_{j=0}^k \alpha_j y_{n+j} = h \sum_{j=0}^k \beta_j f_{n+j}$$
where $\alpha_k \ne 0$ and $|\alpha_0| + |\beta_0| > 0$. By standard convention, normalize $\alpha_k = 1$.
- If $\beta_k = 0$, the method is **explicit** ($y_{n+k}$ appears only on the left).
- If $\beta_k \ne 0$, the method is **implicit** ($y_{n+k}$ appears on both sides inside $f(t_{n+k}, y_{n+k})$).

---

### 2. The Adams Family of Integrators

Integrating $y' = f(t, y)$ from $t_{n+k-1}$ to $t_{n+k}$:
$$y(t_{n+k}) = y(t_{n+k-1}) + \int_{t_{n+k-1}}^{t_{n+k}} f(t, y(t)) \, dt$$
Replace $f(t, y(t))$ by an interpolating polynomial $P(t)$:

#### 1. Adams-Bashforth Methods (Explicit):
$P(t)$ interpolates past values $\{f_{n}, f_{n+1}, \dots, f_{n+k-1}\}$ at $k$ points:
- **AB1 (Euler):** $y_{n+1} = y_n + h f_n$
- **AB2:** $y_{n+2} = y_{n+1} + \frac{h}{2} (3f_{n+1} - f_n)$
- **AB3:** $y_{n+3} = y_{n+2} + \frac{h}{12} (23f_{n+2} - 16f_{n+1} + 5f_n)$
- **AB4:** $y_{n+4} = y_{n+3} + \frac{h}{24} (55f_{n+3} - 59f_{n+2} + 37f_{n+1} - 9f_n)$

#### 2. Adams-Moulton Methods (Implicit):
$P(t)$ interpolates $\{f_{n}, \dots, f_{n+k-1}, f_{n+k}\}$ at $k+1$ points:
- **AM1 (Backward Euler):** $y_{n+1} = y_n + h f_{n+1}$
- **AM2 (Trapezoidal):** $y_{n+1} = y_n + \frac{h}{2} (f_{n+1} + f_n)$
- **AM3:** $y_{n+2} = y_{n+1} + \frac{h}{12} (5f_{n+2} + 8f_{n+1} - f_n)$
- **AM4:** $y_{n+3} = y_{n+2} + \frac{h}{24} (9f_{n+3} + 19f_{n+2} - 5f_{n+1} + f_n)$

---

### 3. Predictor-Corrector Architecture (PECE)

To avoid solving nonlinear systems for implicit Adams-Moulton methods, modern solvers use a **Predict-Evaluate-Correct-Evaluate (PECE)** sequence:
1. **P (Predict):** Compute initial guess $y_{n+1}^{(0)}$ using explicit Adams-Bashforth:
   $$y_{n+1}^{(0)} = y_n + \frac{h}{24}(55f_n - 59f_{n-1} + 37f_{n-2} - 9f_{n-3})$$
2. **E (Evaluate):** Evaluate $f_{n+1}^{(0)} = f(t_{n+1}, y_{n+1}^{(0)})$.
3. **C (Correct):** Refine using implicit Adams-Moulton:
   $$y_{n+1} = y_n + \frac{h}{24}(9f_{n+1}^{(0)} + 19f_n - 5f_{n-1} + f_{n-2})$$
4. **E (Evaluate):** Final update $f_{n+1} = f(t_{n+1}, y_{n+1})$ for the next time step.
This achieves order 4 accuracy with only **two function evaluations per step**, compared to RK4's four evaluations!"""
            },
            {
                "secNumber": "7.4",
                "title": "Characteristic Polynomials, Dahlquist Root Condition & Stability Barriers",
                "content": r"""### 1. Characteristic Polynomials

Associated with the linear multi-step method $\sum_{j=0}^k \alpha_j y_{n+j} = h \sum_{j=0}^k \beta_j f_{n+j}$ are the two characteristic polynomials:
$$\rho(r) = \sum_{j=0}^k \alpha_j r^j, \qquad \sigma(r) = \sum_{j=0}^k \beta_j r^j$$

#### Consistency Conditions:
A linear multi-step method is consistent if and only if:
$$\rho(1) = 0 \quad \text{and} \quad \rho'(1) = \sigma(1)$$

---

### 2. Zero-Stability and the Dahlquist Root Condition

Applying the method to the trivial differential equation $y' = 0$ yields the difference equation:
$$\sum_{j=0}^k \alpha_j y_{n+j} = 0$$
whose general solution is a linear combination of $r_m^n$, where $r_m$ are roots of $\rho(r) = 0$.

> **Definition (Dahlquist Root Condition / Zero-Stability):**
> A linear multi-step method is **zero-stable** if all roots $r$ of the first characteristic polynomial $\rho(r) = 0$ satisfy:
> 1. $|r| \le 1$ (all roots lie within or on the closed unit disk).
> 2. Any root lying on the unit circle ($|r| = 1$) is **simple** (multiplicity 1).

> **Theorem (Dahlquist Equivalence Theorem):**
> For any linear multi-step method:
> $$\text{Convergence of order } p \iff \text{Consistency of order } p \;+\; \text{Zero-Stability}$$

---

### 3. The Dahlquist Stability Barriers

Germund Dahlquist established two profound mathematical bounds that dictate what numerical integrators can and cannot do:

#### Dahlquist's First Barrier (1956):
> The order of convergence $p$ of a zero-stable $k$-step linear multi-step method cannot exceed:
> $$p \le \begin{cases} k + 1 & \text{if } k \text{ is odd} \\ k + 2 & \text{if } k \text{ is even} \\ k & \text{if the method is explicit } (\beta_k = 0) \end{cases}$$

#### Dahlquist's Second Barrier (1963):
> 1. No explicit linear multi-step method can be A-stable.
> 2. An A-stable linear multi-step method cannot have order of accuracy exceeding $p = 2$.
> 3. Among all second-order A-stable linear multi-step methods, the **Implicit Trapezoidal Rule** has the smallest asymptotic error constant:
>    $$C_3 = -\frac{1}{12}$$

This theorem proves that high-order A-stable methods cannot be achieved with linear multi-step formulas, motivating the development of **Backward Differentiation Formulas (BDF)** (which sacrifice A-stability for $A(\alpha)$-stability at orders $k \le 6$) and **Implicit Runge-Kutta methods** (which overcome the barrier by utilizing multiple internal stages)."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Absolute Stability Boundary Analysis for Euler vs. Trapezoidal Methods",
                "statement": r"Consider the test equation $y' = \lambda y$ where $\lambda < 0$ is a negative real eigenvalue. 1. Determine the maximum allowable step size $h_{\max}$ for Forward Euler, Backward Euler, and the Trapezoidal Rule when $\lambda = -50$. 2. If $h = 0.05$, compute the numerical factor $R(h\lambda)$ for each method and determine whether the solution decays, oscillates stably, or blows up to infinity.",
                "hints": [
                    "For Forward Euler, $|1 + h\\lambda| < 1$.",
                    "For Backward Euler, $R(z) = \\frac{1}{1-z}$. For Trapezoidal, $R(z) = \\frac{1+z/2}{1-z/2}$."
                ],
                "solution": r"""**Step 1: Maximum Allowable Step Size for $\lambda = -50$**

1. **Forward Euler:**
   Stability requires $|1 + h\lambda| < 1 \iff -2 < h\lambda < 0$.
   With $\lambda = -50$:
   $$-2 < -50 h < 0 \implies h < \frac{2}{50} = 0.04$$
   Thus, $h_{\max} = 0.04$.

2. **Backward Euler:**
   Stability requires $|R(z)| = \left|\frac{1}{1 - h\lambda}\right| < 1 \iff |1 - h\lambda| > 1$.
   Since $\lambda = -50$, $1 - h(-50) = 1 + 50h > 1$ for all $h > 0$.
   Thus, Backward Euler is **unconditionally stable** ($h_{\max} = \infty$).

3. **Trapezoidal Rule:**
   Stability requires $|R(z)| = \left|\frac{1 + h\lambda/2}{1 - h\lambda/2}\right| < 1 \iff |1 - 25h| < |1 + 25h|$.
   This holds strictly for all $h > 0$.
   Thus, the Trapezoidal Rule is **unconditionally stable** ($h_{\max} = \infty$).

---

**Step 2: Analysis at $h = 0.05$**
Here $z = h\lambda = 0.05 \times (-50) = -2.5$.

1. **Forward Euler:**
   $$R(z) = 1 + z = 1 + (-2.5) = -1.5$$
   Since $|R(z)| = 1.5 > 1$, the numerical solution is:
   $$y_n = (-1.5)^n y_0$$
   The solution **diverges with alternating sign and blows up exponentially to $\pm \infty$**!

2. **Backward Euler:**
   $$R(z) = \frac{1}{1 - z} = \frac{1}{1 - (-2.5)} = \frac{1}{3.5} \approx 0.2857$$
   Since $|R(z)| = 0.2857 < 1$, the solution **decays monotonically to zero without oscillations**.

3. **Trapezoidal Rule:**
   $$R(z) = \frac{1 + z/2}{1 - z/2} = \frac{1 - 1.25}{1 + 1.25} = \frac{-0.25}{2.25} = -\frac{1}{9} \approx -0.1111$$
   Since $|R(z)| = 0.1111 < 1$, the solution **decays stably to zero**, with small damped oscillations due to the negative sign."""
            },
            {
                "tier": "Advanced",
                "title": "Derivation and Local Error of the 3-Step Adams-Bashforth Method",
                "statement": r"Derive the 3-step explicit Adams-Bashforth formula: $$y_{n+3} = y_{n+2} + h \left( \beta_2 f_{n+2} + \beta_1 f_{n+1} + \beta_0 f_n \right)$$ by integrating the Newton backward difference interpolating polynomial for $f(t, y(t))$ over $[t_{n+2}, t_{n+3}]$. Determine the exact fractional coefficients $(\beta_0, \beta_1, \beta_2)$ and compute the leading local truncation error constant $C_4$.",
                "hints": [
                    "Substitute $t = t_{n+2} + s h$ where $s \\in [0, 1]$.",
                    "The Newton backward polynomial is $P(t) = f_{n+2} + s \\nabla f_{n+2} + \\frac{s(s+1)}{2} \\nabla^2 f_{n+2}$."
                ],
                "solution": r"""**Step 1: Integral Formulation**
Integrating $y' = f(t, y)$ from $t_{n+2}$ to $t_{n+3}$:
$$y(t_{n+3}) - y(t_{n+2}) = \int_{t_{n+2}}^{t_{n+3}} f(t, y(t)) \, dt$$
Introduce the change of variable $t = t_{n+2} + s h \implies dt = h \, ds$, where $s \in [0, 1]$.

**Step 2: Interpolating Polynomial in Backward Differences**
The quadratic polynomial interpolating $f_{n+2}, f_{n+1}, f_n$ is:
$$P(t_{n+2} + sh) = f_{n+2} + s \nabla f_{n+2} + \frac{s(s+1)}{2} \nabla^2 f_{n+2}$$
where:
$$\nabla f_{n+2} = f_{n+2} - f_{n+1}$$
$$\nabla^2 f_{n+2} = f_{n+2} - 2f_{n+1} + f_n$$

**Step 3: Integration Over $s \in [0, 1]$**
Evaluating the integrals:
1. $\int_0^1 1 \, ds = 1$
2. $\int_0^1 s \, ds = \frac{1}{2}$
3. $\int_0^1 \frac{s(s+1)}{2} \, ds = \frac{1}{2} \left[ \frac{s^3}{3} + \frac{s^2}{2} \right]_0^1 = \frac{1}{2} \left( \frac{1}{3} + \frac{1}{2} \right) = \frac{1}{2} \cdot \frac{5}{6} = \frac{5}{12}$

Thus:
$$\int_{t_{n+2}}^{t_{n+3}} P(t) \, dt = h \left[ f_{n+2} + \frac{1}{2} \nabla f_{n+2} + \frac{5}{12} \nabla^2 f_{n+2} \right]$$

**Step 4: Expressing in Terms of Function Values**
Substitute backward differences:
$$\begin{aligned}
\int_{t_{n+2}}^{t_{n+3}} P(t) \, dt &= h \left[ f_{n+2} + \frac{1}{2}(f_{n+2} - f_{n+1}) + \frac{5}{12}(f_{n+2} - 2f_{n+1} + f_n) \right] \\
&= h \left[ \left(1 + \frac{1}{2} + \frac{5}{12}\right) f_{n+2} + \left(-\frac{1}{2} - \frac{10}{12}\right) f_{n+1} + \frac{5}{12} f_n \right] \\
&= h \left[ \left(\frac{12 + 6 + 5}{12}\right) f_{n+2} - \left(\frac{6 + 10}{12}\right) f_{n+1} + \frac{5}{12} f_n \right] \\
&= \frac{h}{12} \left[ 23 f_{n+2} - 16 f_{n+1} + 5 f_n \right]
\end{aligned}$$
Thus, $\beta_2 = \frac{23}{12}$, $\beta_1 = -\frac{16}{12} = -\frac{4}{3}$, $\beta_0 = \frac{5}{12}$.

**Step 5: Local Truncation Error Constant**
The next term in the backward difference expansion is:
$$\frac{s(s+1)(s+2)}{6} \nabla^3 f_{n+2} \approx \frac{s^3 + 3s^2 + 2s}{6} h^3 y^{(4)}(\xi)$$
Integrating:
$$\int_0^1 \frac{s^3 + 3s^2 + 2s}{6} \, ds = \frac{1}{6} \left[ \frac{1}{4} + 1 + 1 \right] = \frac{1}{6} \cdot \frac{9}{4} = \frac{9}{24} = \frac{3}{8}$$
Multiplying by $h$ and adding to the order $h^3$ gives:
$$d_{n+3} = \frac{3}{8} h \cdot h^3 y^{(4)}(\xi) = \frac{3}{8} h^4 y^{(4)}(\xi) = \frac{9}{24} h^4 y^{(4)}$$
Local truncation error per step is $\tau = \frac{3}{8} h^3 y^{(4)}$, verifying **third-order accuracy ($p = 3$)**."""
            },
            {
                "tier": "Rigorous Examination / Derivation",
                "title": "Proof of Dahlquist's Root Condition and Second Stability Barrier",
                "statement": r"1. For the general linear multi-step method $\sum_{j=0}^k \alpha_j y_{n+j} = h \sum_{j=0}^k \beta_j f_{n+j}$, prove that zero-stability requires that all roots of the first characteristic polynomial $\rho(r) = \sum_{j=0}^k \alpha_j r^j$ satisfy $|r| \le 1$, with any root on $|r| = 1$ being simple. 2. Using the conformal mapping $z = \frac{r+1}{r-1}$, prove Dahlquist's Second Barrier: an A-stable linear multi-step method cannot have order of accuracy $p > 2$.",
                "hints": [
                    "For Part 1, analyze the unforced recurrence $\\rho(E) y_n = 0$ where $E$ is the shift operator, and show that a multiple root $|r|=1$ generates secular growth $n r^n$.",
                    "For Part 2, express the stability relation on the boundary of the unit disk and use the maximum modulus principle."
                ],
                "solution": r"""**Part 1: Necessity of the Root Condition for Zero-Stability**

Consider the ODE $y' = 0$ with true solution $y(t) \equiv y_0$.
The linear multi-step method reduces to the homogeneous linear recurrence:
$$\sum_{j=0}^k \alpha_j y_{n+j} = 0 \iff \rho(E) y_n = 0$$
where $E$ is the forward shift operator $E y_n = y_{n+1}$.
The general solution to this difference equation is:
$$y_n = \sum_{m=1}^s P_m(n) r_m^n$$
where $r_1, \dots, r_s$ are the distinct roots of $\rho(r) = 0$, and $P_m(n)$ is a polynomial in $n$ of degree $(\mu_m - 1)$, with $\mu_m$ being the algebraic multiplicity of root $r_m$.

For the method to be stable, the numerical solution must remain bounded as $n \to \infty$ for any bounded initial perturbations:
- **Case 1: $|r_m| > 1$.**
  Then $|r_m^n| = |r_m|^n \to \infty$ exponentially as $n \to \infty$. A perturbation in the initial condition is amplified without bound. Hence, we must have $|r_m| \le 1$.
- **Case 2: $|r_m| = 1$ with multiplicity $\mu_m \ge 2$.**
  Then $P_m(n)$ contains terms proportional to $n, n^2, \dots, n^{\mu_m - 1}$.
  Consequently, $|y_n| \sim C n |r_m|^n = C n \to \infty$ as $n \to \infty$.
  Even though $|r_m| = 1$, the secular polynomial factor causes algebraic unbounded growth!

Therefore, boundedness requires:
1. Every root satisfies $|r| \le 1$.
2. Any root with $|r| = 1$ must have $\mu = 1$ (simple root).
This establishes Dahlquist's Root Condition. $\blacksquare$

---

**Part 2: Proof of Dahlquist's Second Barrier ($p \le 2$ for A-stability)**

Let the method have order $p \ge 1$. Then consistency requires $\rho(1) = 0$ and $\rho'(1) = \sigma(1) \ne 0$.
The Dahlquist test equation $y' = \lambda y$ gives the recurrence:
$$(\rho - z \sigma)(E) y_n = 0, \quad z = h\lambda$$
The method is A-stable if and only if for all $z \in \mathbb{C}$ with $\text{Re}(z) < 0$, all roots of the characteristic equation:
$$\rho(r) - z \sigma(r) = 0$$
lie strictly inside the unit disk: $|r| < 1$.

Equivalently, this means the rational function:
$$z(r) = \frac{\rho(r)}{\sigma(r)}$$
maps the exterior of the unit disk $\{r \in \mathbb{C} : |r| > 1\}$ into the right half-plane $\{z \in \mathbb{C} : \text{Re}(z) \ge 0\}$.

Now apply the standard bilinear Möbius transformation from the unit disk to the left half-plane:
$$r = \frac{w + 1}{w - 1} \iff w = \frac{r + 1}{r - 1}$$
which maps the unit disk $|r| < 1$ to the left half-plane $\text{Re}(w) < 0$, and the unit circle $|r| = 1$ to the imaginary axis $\text{Re}(w) = 0$.

Under this transformation, the order conditions require matching the Taylor expansion of the logarithm:
$$z\left( \frac{w+1}{w-1} \right) = \ln\left( \frac{w+1}{w-1} \right) = 2 \left( \frac{1}{w} + \frac{1}{3 w^3} + \frac{1}{5 w^5} + \dots \right)$$
For A-stability, $z(w)$ must be a positive real function (Herglotz function), meaning $\text{Re}(z(w)) \ge 0$ whenever $\text{Re}(w) \ge 0$.

However, the continued fraction expansion of a positive real rational function can only match the series expansion of $\ln\left(\frac{w+1}{w-1}\right)$ up to the first term $\frac{2}{w}$.
Matching the third-order term $\frac{2}{3 w^3}$ forces the rational function to have poles in the right half-plane, which strictly violates the positive real condition (A-stability)!

Therefore, no linear multi-step method can match the logarithmic expansion beyond degree 2 while remaining a positive real mapping.
Consequently, **the maximum order of any A-stable linear multi-step method is $p = 2$**. $\blacksquare$"""
            }
        ]
    }
    return u7

if __name__ == "__main__":
    u = get_unit7()
    print("Unit 7 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
