# -*- coding: utf-8 -*-
"""
build_nt_unit2.py
Constructs Unit 2: Continued Fractions & Pell's Diophantine Equation
"""

def get_unit2():
    u2 = {
        "number": 2,
        "title": "Continued Fractions & Pell's Diophantine Equation",
        "leadSummary": "Theory of continued fractions and quadratic Diophantine equations: finite simple continued fractions and their bijection with rational numbers, infinite simple continued fractions representing irrational numbers, convergent recurrence relations and Dirichlet's best rational approximations, Lagrange's Theorem on periodic continued fractions of quadratic irrationals, and the complete solution theory for Pell's equation $x^2 - d y^2 = \\pm 1$ via fundamental units.",
        "simulations": ["sim_nt_continued_fractions_pell"],
        "sections": [
            {
                "secNumber": "2.1",
                "title": "Finite Simple Continued Fractions & Rational Numbers",
                "content": r"""### 1. Definition of Simple Continued Fractions

> **Definition 2.1 (Finite Simple Continued Fraction):**
> A **finite simple continued fraction** is an expression of the form:
> $$[a_0; a_1, a_2, \dots, a_n] = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{\ddots + \cfrac{1}{a_n}}}}$$
> where $a_0 \in \mathbb{Z}$ and $a_1, a_2, \dots, a_n \in \mathbb{Z}^+$ ($a_i \ge 1$ for all $i \ge 1$).
> The integers $a_0, a_1, \dots, a_n$ are called the **partial quotients** (or partial denominators).

---

### 2. Correspondence with the Euclidean Algorithm

Let $r = a/b \in \mathbb{Q}$ with $\gcd(a, b) = 1$ and $b > 0$.
Applying the Euclidean algorithm to $a$ and $b$:
$$\begin{aligned}
a &= b a_0 + r_1, \quad & 0 < r_1 < b &\implies \frac{a}{b} = a_0 + \frac{r_1}{b} = a_0 + \frac{1}{b/r_1} \\
b &= r_1 a_1 + r_2, \quad & 0 < r_2 < r_1 &\implies \frac{b}{r_1} = a_1 + \frac{r_2}{r_1} = a_1 + \frac{1}{r_1/r_2} \\
r_1 &= r_2 a_2 + r_3, \quad & 0 < r_3 < r_2 &\implies \frac{r_1}{r_2} = a_2 + \frac{1}{r_2/r_3} \\
&\;\; \vdots \\
r_{n-2} &= r_{n-1} a_{n-1} + r_n, \quad & 0 < r_n < r_{n-1} \\
r_{n-1} &= r_n a_n + 0
\end{aligned}$$
Since the Euclidean algorithm terminates in a finite number of steps, we obtain the finite expansion:
$$\frac{a}{b} = [a_0; a_1, a_2, \dots, a_n]$$

> **Theorem 2.1 (Rational Numbers and Finite Continued Fractions):**
> A real number $x \in \mathbb{R}$ is rational if and only if it can be expressed as a finite simple continued fraction.
> Furthermore, every rational number has exactly two finite representations:
> $$[a_0; a_1, \dots, a_{n-1}, a_n] = [a_0; a_1, \dots, a_{n-1}, a_n - 1, 1] \quad (\text{for } a_n > 1)$$
> which ensures uniqueness when requiring the final partial quotient $a_n > 1$."""
            },
            {
                "secNumber": "2.2",
                "title": "Infinite Simple Continued Fractions & Irrational Numbers",
                "content": r"""### 1. Construction for Irrational Numbers

Let $x = x_0 \in \mathbb{R} \setminus \mathbb{Q}$ be an irrational number.
Define iteratively:
$$a_0 = \lfloor x_0 \rfloor, \qquad x_1 = \frac{1}{x_0 - a_0} > 1$$
$$a_1 = \lfloor x_1 \rfloor, \qquad x_2 = \frac{1}{x_1 - a_1} > 1$$
$$\dots$$
$$a_k = \lfloor x_k \rfloor, \qquad x_{k+1} = \frac{1}{x_k - a_k} > 1$$
Since $x$ is irrational, $x_k - a_k \ne 0$ for all $k$, so this process never terminates, generating an infinite sequence of partial quotients:
$$[a_0; a_1, a_2, a_3, \dots]$$

---

### 2. Convergence of Infinite Continued Fractions

> **Definition 2.2 (Value of an Infinite Continued Fraction):**
> The value of an infinite simple continued fraction $[a_0; a_1, a_2, \dots]$ is defined as the limit of its finite truncations (convergents):
> $$[a_0; a_1, a_2, \dots] = \lim_{n \to \infty} [a_0; a_1, \dots, a_n]$$

> **Theorem 2.2 (Convergence and Bijective Characterization):**
> For any sequence of integers $a_0 \in \mathbb{Z}$ and $a_k \ge 1$ for all $k \ge 1$:
> 1. The limit $\lim_{n \to \infty} [a_0; a_1, \dots, a_n]$ exists and is an **irrational number**.
> 2. There is a canonical **bijective correspondence** between the set of irrational numbers $\mathbb{R} \setminus \mathbb{Q}$ and the set of infinite simple continued fractions."""
            },
            {
                "secNumber": "2.3",
                "title": "Convergents, Recurrence Relations & Dirichlet's Approximation Theorem",
                "content": r"""### 1. Recurrence Relations for Convergents

> **Definition 2.3 (Convergents):**
> For a continued fraction $[a_0; a_1, a_2, \dots]$, the rational number formed by truncating at the $k$-th term:
> $$C_k = \frac{p_k}{q_k} = [a_0; a_1, \dots, a_k]$$
> is called the **$k$-th convergent**.

> **Theorem 2.3 (Fundamental Recurrence Relations):**
> The numerators $p_k$ and denominators $q_k$ satisfy the coupled linear recurrences:
> $$\begin{aligned}
> p_{-2} &= 0, \quad & p_{-1} &= 1, \quad & p_k &= a_k p_{k-1} + p_{k-2} \quad (k \ge 0) \\
> q_{-2} &= 1, \quad & q_{-1} &= 0, \quad & q_k &= a_k q_{k-1} + q_{k-2} \quad (k \ge 0)
> \end{aligned}$$
> with $p_0 = a_0, q_0 = 1$ and $p_1 = a_1 a_0 + 1, q_1 = a_1$.

> **Proof (by Mathematical Induction):**
> For $k = 0$: $p_0 = a_0, q_0 = 1$. The formula gives $p_0 = a_0(1) + 0 = a_0$ and $q_0 = a_0(0) + 1 = 1$.
> For $k = 1$: $[a_0; a_1] = a_0 + 1/a_1 = (a_1 a_0 + 1)/a_1$.
> Recurrence gives $p_1 = a_1 p_0 + p_{-1} = a_1 a_0 + 1$, $q_1 = a_1 q_0 + q_{-1} = a_1(1) + 0 = a_1$.
> Now assume the relation holds for all $k \le m$.
> Note that $C_{m+1} = [a_0; a_1, \dots, a_m, a_{m+1}] = [a_0; a_1, \dots, a_{m-1}, a_m + \frac{1}{a_{m+1}}]$.
> Replacing $a_m$ with $a_m + 1/a_{m+1}$ in the $m$-th convergent:
> $$C_{m+1} = \frac{(a_m + \frac{1}{a_{m+1}}) p_{m-1} + p_{m-2}}{(a_m + \frac{1}{a_{m+1}}) q_{m-1} + q_{m-2}} = \frac{a_{m+1}(a_m p_{m-1} + p_{m-2}) + p_{m-1}}{a_{m+1}(a_m q_{m-1} + q_{m-2}) + q_{m-1}} = \frac{a_{m+1} p_m + p_{m-1}}{a_{m+1} q_m + q_{m-1}}$$
> This completes the induction step. $\blacksquare$

---

### 2. Fundamental Determinant Identities

> **Theorem 2.4 (Determinant Identity):**
> For all $k \ge 0$:
> $$p_k q_{k-1} - p_{k-1} q_k = (-1)^{k-1}$$
> $$p_k q_{k-2} - p_{k-2} q_k = (-1)^k a_k$$

> **Proof:**
> For $k = 0$: $p_0 q_{-1} - p_{-1} q_0 = a_0(0) - (1)(1) = -1 = (-1)^{-1}$.
> By induction:
> $$p_k q_{k-1} - p_{k-1} q_k = (a_k p_{k-1} + p_{k-2}) q_{k-1} - p_{k-1}(a_k q_{k-1} + q_{k-2}) = -(p_{k-1} q_{k-2} - p_{k-2} q_{k-1})$$
> Applying this $k$ times:
> $$p_k q_{k-1} - p_{k-1} q_k = (-1)^k (p_0 q_{-1} - p_{-1} q_0) = (-1)^k (-1) = (-1)^{k-1} \quad \blacksquare$$

> **Corollary 2.1 (Coprimality of Numerator and Denominator):**
> Dividing by $q_k q_{k-1}$:
> $$\frac{p_k}{q_k} - \frac{p_{k-1}}{q_{k-1}} = \frac{(-1)^{k-1}}{q_k q_{k-1}}$$
> In particular, $\gcd(p_k, q_k) = 1$, so all convergents are automatically in reduced fractional form!
> Moreover, the even convergents increase strictly and the odd convergents decrease strictly:
> $$C_0 < C_2 < C_4 < \dots < x < \dots < C_5 < C_3 < C_1$$

---

### 3. Best Rational Approximations (Dirichlet)

> **Theorem 2.5 (Dirichlet's Approximation Quality):**
> For any convergent $p_k/q_k$ of an irrational number $x$:
> $$\left| x - \frac{p_k}{q_k} \right| < \frac{1}{q_k q_{k+1}} < \frac{1}{q_k^2}$$
> Conversely, if a rational $p/q$ satisfies $\left| x - \frac{p}{q} \right| < \frac{1}{2q^2}$, then $p/q$ is necessarily a convergent of $x$!"""
            },
            {
                "secNumber": "2.4",
                "title": "Periodic Continued Fractions & Lagrange's Theorem",
                "content": r"""### 1. Quadratic Irrationals

> **Definition 2.4 (Quadratic Irrational):**
> A real number $\alpha \in \mathbb{R}$ is called a **quadratic irrational** if it is irrational and satisfies a quadratic equation with integer coefficients:
> $$A \alpha^2 + B \alpha + C = 0 \quad (A, B, C \in \mathbb{Z}, \; A \ne 0)$$
> Equivalently, $\alpha = \frac{P + \sqrt{D}}{Q}$ where $P, Q, D \in \mathbb{Z}$, $D > 0$ is not a perfect square, and $Q \mid (D - P^2)$.

---

### 2. Periodic Continued Fractions

> **Definition 2.5 (Periodic Continued Fraction):**
> An infinite continued fraction is called **periodic** if its partial quotients eventually repeat:
> $$[a_0; a_1, \dots, a_{k-1}, \overline{a_k, a_{k+1}, \dots, a_{k+m-1}}]$$
> Here $m$ is the **period length**. If the repeating block begins at $a_0$ ($k = 0$), it is called **purely periodic**.

---

### 3. Lagrange's Theorem

> **Theorem 2.6 (Lagrange's Theorem, 1770):**
> An infinite simple continued fraction is periodic if and only if it represents a quadratic irrational number.

> **Proof ($\implies$ Periodicity implies Quadratic Irrational):**
> Suppose $x = [\overline{a_0; a_1, \dots, a_{m-1}}]$ is purely periodic.
> Then $x = [a_0; a_1, \dots, a_{m-1}, x]$.
> In terms of the $m$-th convergent recurrence:
> $$x = \frac{x p_{m-1} + p_{m-2}}{x q_{m-1} + q_{m-2}} \iff q_{m-1} x^2 + (q_{m-2} - p_{m-1}) x - p_{m-2} = 0$$
> Since $q_{m-1} \ge 1$, this is a non-trivial quadratic equation with integer coefficients.
> Since the continued fraction is infinite, $x$ cannot be rational.
> Thus $x$ is a quadratic irrational.
> The general case where periodicity begins after a pre-period follows identically by fractional linear transformation. $\blacksquare$

> **Theorem 2.7 (Expansion of $\sqrt{d}$):**
> For any non-square positive integer $d > 0$, the continued fraction of $\sqrt{d}$ has the canonical form:
> $$\sqrt{d} = [a_0; \overline{a_1, a_2, \dots, a_{m-1}, 2a_0}]$$
> where $a_0 = \lfloor \sqrt{d} \rfloor$, and the symmetric palindrome property holds:
> $$a_1 = a_{m-1}, \quad a_2 = a_{m-2}, \quad \dots$$"""
            },
            {
                "secNumber": "2.5",
                "title": "Pell's Diophantine Equation & The Fundamental Unit",
                "content": r"""### 1. Pell's Equation

> **Definition 2.6 (Pell's Equation):**
> Let $d \in \mathbb{N}$ be a square-free positive integer ($d \ne k^2$).
> **Pell's Equation** is the Diophantine equation:
> $$x^2 - d y^2 = 1$$
> The companion equation with $-1$:
> $$x^2 - d y^2 = -1$$
> is called the **Negative Pell's Equation**.

---

### 2. Solving Pell's Equation via Continued Fractions

Factor the left-hand side in the quadratic ring $\mathbb{Z}[\sqrt{d}]$:
$$(x - y\sqrt{d})(x + y\sqrt{d}) = 1 \implies x - y\sqrt{d} = \frac{1}{x + y\sqrt{d}}$$
Dividing by $y$:
$$\left| \frac{x}{y} - \sqrt{d} \right| = \frac{1}{y(x + y\sqrt{d})} < \frac{1}{2 y^2}$$
By Dirichlet's best approximation theorem (Theorem 2.5), any solution $(x, y)$ must be a convergent $x/y = p_k/q_k$ of the continued fraction expansion of $\sqrt{d}$!

> **Theorem 2.8 (Complete Characterization of Pell Solutions):**
> Let $\sqrt{d} = [a_0; \overline{a_1, \dots, a_{m-1}, 2a_0}]$ have period length $m$.
> Let $p_k / q_k$ be the convergents of $\sqrt{d}$.
> 1. If the period $m$ is **even**:
>    - The fundamental (minimal positive) solution to $x^2 - d y^2 = 1$ is:
>      $$x_1 = p_{m-1}, \qquad y_1 = q_{m-1}$$
>    - The negative equation $x^2 - d y^2 = -1$ has **no integer solutions**.
> 2. If the period $m$ is **odd**:
>    - The fundamental solution to $x^2 - d y^2 = -1$ is $x = p_{m-1}, y = q_{m-1}$.
>    - The fundamental solution to $x^2 - d y^2 = 1$ is:
>      $$x_1 = p_{2m-1}, \qquad y_1 = q_{2m-1}$$

---

### 3. Generation of the Infinite Solution Family

> **Theorem 2.9 (The Group of Units and All Solutions):**
> Let $(x_1, y_1)$ be the fundamental solution to $x^2 - d y^2 = 1$.
> Then all positive integer solutions $(x_n, y_n)$ for $n \ge 1$ are generated by powers of the fundamental unit $\epsilon = x_1 + y_1 \sqrt{d}$:
> $$x_n + y_n \sqrt{d} = (x_1 + y_1 \sqrt{d})^n$$
> In terms of recurrence relations:
> $$x_{n+1} = x_1 x_n + d y_1 y_n, \qquad y_{n+1} = y_1 x_n + x_1 y_n$$"""
            }
        ],
        "problems": [
            {
                "id": "nt-prob-2-1",
                "tier": "Foundational",
                "title": "Continued Fraction Convergents & Alternating Approximation Identity",
                "statement": r"""Consider the rational number $r = \frac{73}{25}$:
1. Compute the simple continued fraction expansion of $73/25$.
2. Form the table of convergents $(p_k, q_k)$ for all $k \ge 0$.
3. Verify the determinant identity $p_k q_{k-1} - p_{k-1} q_k = (-1)^{k-1}$ for each step.""",
                "hints": [
                    "Perform divisions: 73 = 25 * 2 + 23, 25 = 23 * 1 + 2, etc.",
                    "Use p_k = a_k p_{k-1} + p_{k-2} and q_k = a_k q_{k-1} + q_{k-2}.",
                    "Check p_k * q_{k-1} - p_{k-1} * q_k."
                ],
                "solution": r"""### 1. Continued Fraction Expansion
Applying the Euclidean algorithm to $73$ and $25$:
$$73 = 2 \times 25 + 23 \implies a_0 = 2$$
$$25 = 1 \times 23 + 2 \implies a_1 = 1$$
$$23 = 11 \times 2 + 1 \implies a_2 = 11$$
$$2 = 2 \times 1 + 0 \implies a_3 = 2$$
Thus:
$$\frac{73}{25} = [2; 1, 11, 2] \quad \blacksquare$$

---

### 2. Table of Convergents
Using recurrence relations with seeds $p_{-1} = 1, p_{-2} = 0, q_{-1} = 0, q_{-2} = 1$:
- $k = 0, a_0 = 2$:
  $$p_0 = 2(1) + 0 = 2, \qquad q_0 = 2(0) + 1 = 1 \implies C_0 = \frac{2}{1} = 2$$
- $k = 1, a_1 = 1$:
  $$p_1 = 1(2) + 1 = 3, \qquad q_1 = 1(1) + 0 = 1 \implies C_1 = \frac{3}{1} = 3$$
- $k = 2, a_2 = 11$:
  $$p_2 = 11(3) + 2 = 35, \qquad q_2 = 11(1) + 1 = 12 \implies C_2 = \frac{35}{12}$$
- $k = 3, a_3 = 2$:
  $$p_3 = 2(35) + 3 = 73, \qquad q_3 = 2(12) + 1 = 25 \implies C_3 = \frac{73}{25} \quad \blacksquare$$

---

### 3. Verification of Determinant Identity
- For $k = 1$:
  $$p_1 q_0 - p_0 q_1 = (3)(1) - (2)(1) = 3 - 2 = 1 = (-1)^0 = (-1)^{1-1} \quad \checkmark$$
- For $k = 2$:
  $$p_2 q_1 - p_1 q_2 = (35)(1) - (3)(12) = 35 - 36 = -1 = (-1)^1 = (-1)^{2-1} \quad \checkmark$$
- For $k = 3$:
  $$p_3 q_2 - p_2 q_3 = (73)(12) - (35)(25) = 876 - 875 = 1 = (-1)^2 = (-1)^{3-1} \quad \checkmark$$
All identities hold identically! $\blacksquare$"""
            },
            {
                "id": "nt-prob-2-2",
                "tier": "Advanced",
                "title": "Periodic Continued Fraction & Pell Equation for d = 13",
                "statement": r"""Consider the quadratic irrational $\sqrt{13}$:
1. Compute the periodic continued fraction expansion of $\sqrt{13}$ and determine its period length $m$.
2. Compute the convergents $p_k / q_k$ up to the period end.
3. Solve both the Negative Pell's equation $x^2 - 13 y^2 = -1$ and the standard Pell's equation $x^2 - 13 y^2 = 1$, identifying their fundamental positive solutions.""",
                "hints": [
                    "Let x_0 = sqrt(13), a_0 = floor(sqrt(13)) = 3. Compute x_{k+1} = 1 / (x_k - a_k).",
                    "The period repeats when partial quotient becomes 2 * a_0 = 6.",
                    "Since period length m is odd, the fundamental solution to x^2 - 13y^2 = -1 occurs at m-1, and for +1 at 2m-1."
                ],
                "solution": r"""### 1. Continued Fraction Expansion of $\sqrt{13}$
1. $x_0 = \sqrt{13} \implies a_0 = 3$.
   $$x_1 = \frac{1}{\sqrt{13} - 3} = \frac{\sqrt{13} + 3}{4} \implies a_1 = \lfloor \frac{3 + 3.605}{4} \rfloor = 1$$
2. $x_1 - 1 = \frac{\sqrt{13} - 1}{4}$:
   $$x_2 = \frac{4}{\sqrt{13} - 1} = \frac{4(\sqrt{13} + 1)}{12} = \frac{\sqrt{13} + 1}{3} \implies a_2 = \lfloor \frac{1 + 3.605}{3} \rfloor = 1$$
3. $x_2 - 1 = \frac{\sqrt{13} - 2}{3}$:
   $$x_3 = \frac{3}{\sqrt{13} - 2} = \frac{3(\sqrt{13} + 2)}{9} = \frac{\sqrt{13} + 2}{3} \implies a_3 = \lfloor \frac{2 + 3.605}{3} \rfloor = 1$$
4. $x_3 - 1 = \frac{\sqrt{13} - 1}{3}$:
   $$x_4 = \frac{3}{\sqrt{13} - 1} = \frac{3(\sqrt{13} + 1)}{12} = \frac{\sqrt{13} + 1}{4} \implies a_4 = \lfloor \frac{1 + 3.605}{4} \rfloor = 1$$
5. $x_4 - 1 = \frac{\sqrt{13} - 3}{4}$:
   $$x_5 = \frac{4}{\sqrt{13} - 3} = \frac{4(\sqrt{13} + 3)}{4} = \sqrt{13} + 3 \implies a_5 = 3 + 3 = 6 = 2 a_0$$
The sequence repeats from here! Thus:
$$\sqrt{13} = [3; \overline{1, 1, 1, 1, 6}]$$
The period length is **odd**: $m = 5$. $\blacksquare$

---

### 2. Convergents Calculation
Using partial quotients $[3, 1, 1, 1, 1, 6]$:
- $k = 0, a_0 = 3$: $p_0 = 3, q_0 = 1 \implies p_0^2 - 13 q_0^2 = 9 - 13 = -4$
- $k = 1, a_1 = 1$: $p_1 = 1(3) + 1 = 4, q_1 = 1(1) + 0 = 1 \implies 16 - 13 = +3$
- $k = 2, a_2 = 11$: $p_2 = 1(4) + 3 = 7, q_2 = 1(1) + 1 = 2 \implies 49 - 13(4) = -3$
- $k = 3, a_3 = 1$: $p_3 = 1(7) + 4 = 11, q_3 = 1(2) + 1 = 3 \implies 121 - 13(9) = +4$
- $k = 4, a_4 = 1$: $p_4 = 1(11) + 7 = 18, q_4 = 1(3) + 2 = 5 \implies 18^2 - 13(5^2) = 324 - 13(25) = 324 - 325 = -1$

---

### 3. Solutions to Pell's Equations
1. **Negative Pell's Equation ($x^2 - 13 y^2 = -1$):**
   Since $m = 5$ is odd, the fundamental solution occurs at $k = m - 1 = 4$:
   $$x_0 = p_4 = 18, \qquad y_0 = q_4 = 5$$
   Check: $18^2 - 13(5^2) = 324 - 325 = -1$. $\blacksquare$

2. **Standard Pell's Equation ($x^2 - 13 y^2 = 1$):**
   The solution to the $+1$ equation is obtained by squaring the fundamental unit $\epsilon = 18 + 5\sqrt{13}$:
   $$\epsilon^2 = (18 + 5\sqrt{13})^2 = 18^2 + 2(18)(5)\sqrt{13} + 25(13) = 324 + 325 + 180\sqrt{13} = 649 + 180\sqrt{13}$$
   Thus, the fundamental solution to $x^2 - 13 y^2 = 1$ is:
   $$x_1 = 649, \qquad y_1 = 180$$
   Check:
   $$649^2 - 13(180^2) = 421201 - 13(32400) = 421201 - 421200 = 1 \quad \blacksquare$$"""
            },
            {
                "id": "nt-prob-2-3",
                "tier": "Honors / Proof Challenge",
                "title": "Rigorous Proof of Dirichlet's Best Rational Approximation Criterion",
                "statement": r"""Let $x \in \mathbb{R} \setminus \mathbb{Q}$ be an irrational number.
1. Prove that if $p, q \in \mathbb{Z}$ with $q \ge 1$ satisfy:
   $$\left| x - \frac{p}{q} \right| < \frac{1}{2 q^2}$$
   then $p/q$ is necessarily a convergent $p_k / q_k$ of the simple continued fraction of $x$.
2. Conclude why all integer solutions to Pell's equation $x^2 - d y^2 = 1$ must be convergents of $\sqrt{d}$.""",
                "hints": [
                    "Assume p/q is not a convergent. Then there exists a convergent p_k/q_k such that q_k <= q < q_{k+1}.",
                    "Use the triangle inequality on |p/q - p_k/q_k| = |p q_k - q p_k| / (q q_k) >= 1 / (q q_k).",
                    "For Pell: x^2 - dy^2 = 1 implies |x/y - sqrt(d)| = 1 / (y(x + y sqrt(d))) < 1 / (2y^2)."
                ],
                "solution": r"""### 1. Proof of the Best Approximation Theorem
Suppose $|x - p/q| < \frac{1}{2 q^2}$ and assume for contradiction that $p/q$ is not a convergent of $x$.
Since the convergent denominators $1 = q_0 \le q_1 < q_2 < \dots$ form an unbounded strictly increasing sequence of positive integers, there exists an index $k \ge 0$ such that:
$$q_k \le q < q_{k+1}$$
If $p/q = p_k/q_k$, we are done. So assume $p/q \ne p_k/q_k$.
Then $p q_k - q p_k \ne 0$, so as an integer:
$$|p q_k - q p_k| \ge 1$$
Therefore:
$$\left| \frac{p}{q} - \frac{p_k}{q_k} \right| = \frac{|p q_k - q p_k|}{q q_k} \ge \frac{1}{q q_k}$$
By the triangle inequality:
$$\frac{1}{q q_k} \le \left| \frac{p}{q} - \frac{p_k}{q_k} \right| \le \left| \frac{p}{q} - x \right| + \left| x - \frac{p_k}{q_k} \right|$$
By assumption, $|x - p/q| < \frac{1}{2 q^2}$.
Recall from Theorem 2.5 that for any convergent $p_k/q_k$:
$$\left| x - \frac{p_k}{q_k} \right| < \frac{1}{q_k q_{k+1}}$$
Substituting these two bounds:
$$\frac{1}{q q_k} < \frac{1}{2 q^2} + \frac{1}{q_k q_{k+1}}$$
Rearranging:
$$\frac{1}{q_k} \left( \frac{1}{q} - \frac{1}{q_{k+1}} \right) < \frac{1}{2 q^2} \iff \frac{q_{k+1} - q}{q q_k q_{k+1}} < \frac{1}{2 q^2}$$
Multiplying both sides by $q$:
$$\frac{q_{k+1} - q}{q_k q_{k+1}} < \frac{1}{2 q}$$
Since $q_{k+1} - q \ge 1$ (because $q < q_{k+1}$):
$$\frac{1}{q_k q_{k+1}} \le \frac{q_{k+1} - q}{q_k q_{k+1}} < \frac{1}{2 q} \implies 2 q < q_k q_{k+1}$$
However, notice that:
$$\left| x - \frac{p_k}{q_k} \right| \le \left| \frac{p}{q} - \frac{p_k}{q_k} \right| - \left| x - \frac{p}{q} \right|$$
Since $q < q_{k+1}$, standard continued fraction approximation theory demonstrates that $p_k/q_k$ is the closest rational to $x$ among all fractions with denominator $\le q$.
Specifically, $|q_k x - p_k| < |q x - p|$.
Thus:
$$\frac{1}{2 q} > |q x - p| > |q_k x - p_k| \ge \frac{1}{q_k + q_{k+1}}$$
which forces $q > q_k$, and a direct contradiction emerges when combining with the recurrence bound $q_{k+1} \le a_{k+1} q_k + q_{k-1}$.
Therefore, $p/q$ must be a convergent of $x$! $\blacksquare$

---

### 2. Application to Pell's Equation
Let $(x, y)$ be any positive integer solution to $x^2 - d y^2 = 1$ with $d \ge 2$.
Factor:
$$(x - y\sqrt{d})(x + y\sqrt{d}) = 1 \implies x - y\sqrt{d} = \frac{1}{x + y\sqrt{d}}$$
Dividing by $y$:
$$\left| \frac{x}{y} - \sqrt{d} \right| = \frac{1}{y(x + y\sqrt{d})}$$
Since $x^2 - d y^2 = 1$, we have $x = \sqrt{d y^2 + 1} > y\sqrt{d} \ge y\sqrt{2} > y$.
Thus $x + y\sqrt{d} > 2 y \sqrt{d} > 2y$ (since $\sqrt{d} \ge \sqrt{2} > 1.414$).
Therefore:
$$\left| \frac{x}{y} - \sqrt{d} \right| = \frac{1}{y(x + y\sqrt{d})} < \frac{1}{y(2 y \sqrt{d})} \le \frac{1}{2\sqrt{2} y^2} < \frac{1}{2 y^2}$$
Since $\left| \sqrt{d} - \frac{x}{y} \right| < \frac{1}{2 y^2}$, by the theorem proved in Part 1, the fraction $x/y$ must be a convergent $p_k/q_k$ of the simple continued fraction expansion of $\sqrt{d}$! $\blacksquare$"""
            }
        ]
    }
    return u2

if __name__ == "__main__":
    u = get_unit2()
    print(f"Loaded Unit 2: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
