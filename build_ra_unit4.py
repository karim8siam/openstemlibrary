# -*- coding: utf-8 -*-
"""
build_ra_unit4.py
Constructs Unit 4: Infinite Series of Real Numbers: Rigorous Convergence Tests
"""

def get_unit4():
    u4 = {
        "number": 4,
        "title": "Infinite Series of Real Numbers: Rigorous Convergence Tests",
        "leadSummary": "Comprehensive mathematical theory of infinite series: sequences of partial sums, the Cauchy convergence criterion for series, tests for non-negative series (Comparison, Limit Comparison, Cauchy Condensation), absolute convergence, Ratio and Root tests, the Integral Test, delicate tests (Raabe's and Gauss's tests), Dirichlet and Abel tests, and Riemann's Rearrangement Theorem.",
        "simulations": ["sim_ra_series_convergence"],
        "sections": [
            {
                "secNumber": "4.1",
                "title": "Infinite Series, Sequence of Partial Sums & The Cauchy Criterion for Series",
                "content": r"""### 1. The Concept of an Infinite Series

An infinite series is the formal addition of countably infinitely many real numbers:
$$\sum_{n=1}^\infty a_n = a_1 + a_2 + a_3 + \dots + a_n + \dots$$
Because infinity is not a real number, addition cannot be performed term-by-term infinitely. Instead, analysis rigorously reduces the convergence of an infinite series to the convergence of a sequence of finite partial sums.

> **Definition 4.1 (Partial Sums and Series Convergence):**
> Given a sequence of real numbers $(a_n)_{n=1}^\infty$, the **$k$-th partial sum** is:
> $$s_k = \sum_{n=1}^k a_n = a_1 + a_2 + \dots + a_k$$
> The infinite series $\sum_{n=1}^\infty a_n$ is said to **converge** to the sum $S \in \mathbb{R}$ if the sequence of partial sums $(s_k)_{k=1}^\infty$ converges to $S$:
> $$\sum_{n=1}^\infty a_n = \lim_{k \to \infty} s_k = S$$
> If $(s_k)$ diverges, the series is said to **diverge**.

---

### 2. The $n$-th Term Test for Divergence

> **Theorem 4.1 ($n$-th Term Divergence Test):**
> If the series $\sum_{n=1}^\infty a_n$ converges, then:
> $$\lim_{n \to \infty} a_n = 0$$
> Equivalently, if $\lim_{n \to \infty} a_n \ne 0$ or does not exist, the series diverges.

#### Proof:
Suppose $\sum_{n=1}^\infty a_n = S$.
Then $\lim_{k \to \infty} s_k = S$ and $\lim_{k \to \infty} s_{k-1} = S$.
For any $n \ge 2$, the $n$-th term is the difference between consecutive partial sums:
$$a_n = s_n - s_{n-1}$$
By the algebraic limit theorem for differences:
$$\lim_{n \to \infty} a_n = \lim_{n \to \infty} (s_n - s_{n-1}) = \lim_{n \to \infty} s_n - \lim_{n \to \infty} s_{n-1} = S - S = 0 \quad \blacksquare$$

> **Warning (Non-Sufficiency of $a_n \to 0$):**
> The condition $\lim a_n = 0$ is strictly necessary, but **not sufficient** for convergence!
> The canonical counterexample is the **Harmonic Series**:
> $$\sum_{n=1}^\infty \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \dots$$
> Here $a_n = \frac{1}{n} \to 0$, yet the series diverges to $\infty$.

---

### 3. The Cauchy Criterion for Series

> **Theorem 4.2 (Cauchy Convergence Criterion for Series):**
> A series $\sum_{n=1}^\infty a_n$ converges in $\mathbb{R}$ if and only if for every $\epsilon > 0$, there exists an index $N \in \mathbb{N}$ such that:
> $$\forall m > n \ge N, \quad \left| \sum_{k=n+1}^m a_k \right| = |a_{n+1} + a_{n+2} + \dots + a_m| < \epsilon$$

#### Proof:
The series converges if and only if the sequence of partial sums $(s_k)$ converges.
By the Cauchy Completeness Theorem (Theorem 3.10), $(s_k)$ converges in $\mathbb{R}$ if and only if $(s_k)$ is a Cauchy sequence:
$$\forall \epsilon > 0, \; \exists N \in \mathbb{N} \text{ s.t. } \forall m > n \ge N, \; |s_m - s_n| < \epsilon$$
Since $s_m - s_n = \sum_{k=n+1}^m a_k$, the assertion is proven. $\blacksquare$"""
            },
            {
                "secNumber": "4.2",
                "title": "Series with Non-Negative Terms: Comparison & Cauchy Condensation Tests",
                "content": r"""### 1. Monotonicity of Partial Sums

For series where all terms are non-negative ($a_n \ge 0$), the sequence of partial sums is monotonically increasing:
$$s_{k+1} = s_k + a_{k+1} \ge s_k$$
By the Monotone Convergence Theorem, a non-negative series **converges if and only if its sequence of partial sums is bounded above**.

---

### 2. Direct and Limit Comparison Tests

> **Theorem 4.3 (Direct Comparison Test):**
> Let $0 \le a_n \le b_n$ for all $n \ge N_0$.
> 1. If $\sum_{n=1}^\infty b_n$ converges, then $\sum_{n=1}^\infty a_n$ converges.
> 2. If $\sum_{n=1}^\infty a_n$ diverges, then $\sum_{n=1}^\infty b_n$ diverges.

> **Theorem 4.4 (Limit Comparison Test):**
> Let $a_n > 0$ and $b_n > 0$ for all $n$, and suppose:
> $$L = \lim_{n \to \infty} \frac{a_n}{b_n}$$
> 1. If $0 < L < \infty$, then either both series converge or both diverge.
> 2. If $L = 0$ and $\sum b_n$ converges, then $\sum a_n$ converges.
> 3. If $L = \infty$ and $\sum b_n$ diverges, then $\sum a_n$ diverges.

#### Rigorous Proof of Case 1 ($0 < L < \infty$):
Let $\epsilon = \frac{L}{2} > 0$. By definition of limit, there exists $N \in \mathbb{N}$ such that for all $n \ge N$:
$$\left| \frac{a_n}{b_n} - L \right| < \frac{L}{2} \iff \frac{L}{2} < \frac{a_n}{b_n} < \frac{3L}{2}$$
Multiplying through by $b_n > 0$:
$$\frac{L}{2} b_n < a_n < \frac{3L}{2} b_n \quad \forall n \ge N$$
- If $\sum b_n$ converges, then $\sum \frac{3L}{2} b_n$ converges. By the Direct Comparison Test, $\sum a_n$ converges.
- If $\sum b_n$ diverges, then $\sum \frac{L}{2} b_n$ diverges. By the Direct Comparison Test, $\sum a_n$ diverges. $\blacksquare$

---

### 3. The Cauchy Condensation Test

> **Theorem 4.5 (Cauchy Condensation Test):**
> Let $(a_n)_{n=1}^\infty$ be a monotonically decreasing sequence of non-negative real numbers ($a_1 \ge a_2 \ge a_3 \ge \dots \ge 0$).
> Then the series $\sum_{n=1}^\infty a_n$ converges if and only if the "condensed" series:
> $$\sum_{k=0}^\infty 2^k a_{2^k} = a_1 + 2 a_2 + 4 a_4 + 8 a_8 + 16 a_{16} + \dots$$
> converges.

#### Line-by-Line Proof:
Let $s_n = \sum_{j=1}^n a_j$ and $t_k = \sum_{j=0}^k 2^j a_{2^j}$.
Both $(s_n)$ and $(t_k)$ are monotonically increasing sequences.

**Part 1: If $\sum 2^k a_{2^k}$ converges, then $\sum a_n$ converges.**
For any $n \le 2^k - 1$, group the terms of $s_n$ into dyadic blocks:
$$\begin{aligned}
s_n \le s_{2^k - 1} &= a_1 + (a_2 + a_3) + (a_4 + a_5 + a_6 + a_7) + \dots + (a_{2^{k-1}} + \dots + a_{2^k - 1}) \\
&\le a_1 + 2 a_2 + 4 a_4 + \dots + 2^{k-1} a_{2^{k-1}} \\
&= t_{k-1} \le \sum_{j=0}^\infty 2^j a_{2^j} = M < \infty
\end{aligned}$$
Thus the sequence of partial sums $(s_n)$ is bounded above by $M$. By MCT, $\sum a_n$ converges.

**Part 2: If $\sum a_n$ converges, then $\sum 2^k a_{2^k}$ converges.**
For any $k$, consider the partial sum $s_{2^k}$:
$$\begin{aligned}
s_{2^k} &= a_1 + a_2 + (a_3 + a_4) + (a_5 + a_6 + a_7 + a_8) + \dots + (a_{2^{k-1}+1} + \dots + a_{2^k}) \\
&\ge a_1 + a_2 + 2 a_4 + 4 a_8 + \dots + 2^{k-1} a_{2^k} \\
&= \frac{1}{2} (2 a_1 + 2 a_2 + 4 a_4 + 8 a_8 + \dots + 2^k a_{2^k}) \\
&\ge \frac{1}{2} (a_1 + 2 a_2 + 4 a_4 + \dots + 2^k a_{2^k}) = \frac{1}{2} t_k
\end{aligned}$$
Thus $t_k \le 2 s_{2^k} \le 2 \sum_{n=1}^\infty a_n < \infty$.
Hence $(t_k)$ is bounded above, so the condensed series converges. $\blacksquare$

> **Application: The $p$-Series Theorem:**
> The series $\sum_{n=1}^\infty \frac{1}{n^p}$ converges if and only if $p > 1$.
> *Proof:* By condensation, the condensed series is $\sum 2^k \frac{1}{(2^k)^p} = \sum (2^{1-p})^k$, which is a geometric series with ratio $r = 2^{1-p}$.
> This converges iff $r < 1 \iff 1 - p < 0 \iff p > 1$. $\blacksquare$"""
            },
            {
                "secNumber": "4.3",
                "title": "Absolute Convergence, Ratio Test, Root Test & The Integral Test",
                "content": r"""### 1. Absolute vs. Conditional Convergence

> **Definition 4.2 (Absolute Convergence):**
> A series $\sum_{n=1}^\infty a_n$ is said to **converge absolutely** if the series of absolute values converges:
> $$\sum_{n=1}^\infty |a_n| < \infty$$
> If $\sum a_n$ converges but $\sum |a_n|$ diverges, the series is said to **converge conditionally**.

> **Theorem 4.6 (Absolute Convergence Implies Convergence):**
> If $\sum_{n=1}^\infty |a_n|$ converges, then $\sum_{n=1}^\infty a_n$ converges.
> 
> *Proof:* By the Cauchy Criterion for series, since $\sum |a_n|$ converges:
> $$\forall \epsilon > 0, \; \exists N \text{ s.t. } \forall m > n \ge N, \; \sum_{k=n+1}^m |a_k| < \epsilon$$
> By the generalized triangle inequality:
> $$\left| \sum_{k=n+1}^m a_k \right| \le \sum_{k=n+1}^m |a_k| < \epsilon$$
> By Theorem 4.2, $\sum a_n$ converges. $\blacksquare$

---

### 2. The Cauchy Root Test and d'Alembert Ratio Test

> **Theorem 4.7 (Cauchy Root Test):**
> Let $\alpha = \limsup_{n \to \infty} \sqrt[n]{|a_n|}$.
> 1. If $\alpha < 1$, the series $\sum a_n$ converges absolutely.
> 2. If $\alpha > 1$, the series $\sum a_n$ diverges.
> 3. If $\alpha = 1$, the test is inconclusive.

#### Rigorous Proof of Case 1 ($\alpha < 1$):
Since $\alpha < 1$, choose $r$ such that $\alpha < r < 1$.
Let $\epsilon = r - \alpha > 0$.
By the definition of $\limsup$, there exists $N \in \mathbb{N}$ such that for all $n \ge N$:
$$\sqrt[n]{|a_n|} < \alpha + \epsilon = r \implies |a_n| < r^n$$
Since $0 < r < 1$, the geometric series $\sum_{n=N}^\infty r^n$ converges.
By the Direct Comparison Test, $\sum |a_n|$ converges, so $\sum a_n$ converges absolutely. $\blacksquare$

> **Theorem 4.8 (d'Alembert Ratio Test):**
> Let $a_n \ne 0$ and suppose $\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = L$.
> 1. If $L < 1$, the series converges absolutely.
> 2. If $L > 1$, the series diverges.
> 3. If $L = 1$, the test is inconclusive.

---

### 3. The Maclaurin-Cauchy Integral Test

> **Theorem 4.9 (The Integral Test):**
> Let $f: [1, \infty) \to [0, \infty)$ be a continuous, non-negative, and monotonically decreasing function such that $f(n) = a_n$ for all $n \in \mathbb{N}$.
> Then the series $\sum_{n=1}^\infty a_n$ converges if and only if the improper Riemann integral converges:
> $$\int_1^\infty f(x) \, dx < \infty$$
> 
> *Proof Sketch:* On each interval $[k, k+1]$, since $f$ is decreasing:
> $$f(k+1) \le \int_k^{k+1} f(x) \, dx \le f(k)$$
> Summing from $k=1$ to $n-1$:
> $$\sum_{k=2}^n a_k \le \int_1^n f(x) \, dx \le \sum_{k=1}^{n-1} a_k$$
> The partial sums are bounded if and only if the improper integral is bounded. $\blacksquare$"""
            },
            {
                "secNumber": "4.4",
                "title": "Refined Convergence Tests: Raabe's Test, Gauss's Test & Kummer's Criterion",
                "content": r"""### 1. When the Ratio Test Fails ($L = 1$)

When $\lim |a_{n+1}/a_n| = 1$, the Ratio Test provides no information. This occurs for all $p$-series, since $\frac{n^p}{(n+1)^p} = (1 + 1/n)^{-p} \to 1$. To handle these delicate boundary cases, higher-order asymptotic tests are required.

---

### 2. Raabe's Test

> **Theorem 4.10 (Raabe's Test):**
> Let $a_n > 0$ and suppose:
> $$R = \lim_{n \to \infty} n \left( \frac{a_n}{a_{n+1}} - 1 \right)$$
> 1. If $R > 1$, the series $\sum a_n$ converges.
> 2. If $R < 1$, the series $\sum a_n$ diverges.
> 3. If $R = 1$, the test is inconclusive.

#### Proof Sketch:
Compare $a_n$ against the $p$-series $b_n = \frac{1}{n^p}$.
Using the binomial expansion:
$$\frac{b_n}{b_{n+1}} = \left( 1 + \frac{1}{n} \right)^p = 1 + \frac{p}{n} + O\left(\frac{1}{n^2}\right)$$
So $n \left( \frac{b_n}{b_{n+1}} - 1 \right) \to p$.
If $R > 1$, choose $p$ such that $R > p > 1$. For large $n$, $\frac{a_n}{a_{n+1}} > \frac{b_n}{b_{n+1}}$, which forces $\sum a_n$ to converge by comparison with the convergent $p$-series. $\blacksquare$

---

### 3. Gauss's Test

> **Theorem 4.11 (Gauss's Hypergeometric Test):**
> Let $a_n > 0$. Suppose the ratio can be expanded asymptotically as:
> $$\frac{a_n}{a_{n+1}} = 1 + \frac{h}{n} + \frac{B_n}{n^{1 + \delta}}$$
> where $\delta > 0$ and $(B_n)$ is a bounded sequence.
> Then:
> 1. The series converges if $h > 1$.
> 2. The series diverges if $h \le 1$.
> Note that Gauss's test completely resolves the critical boundary $h = 1$ where Raabe's test is inconclusive!"""
            },
            {
                "secNumber": "4.5",
                "title": "Alternating Series, Dirichlet & Abel Tests, and Riemann Rearrangements",
                "content": r"""### 1. The Leibniz Alternating Series Test

> **Theorem 4.12 (Leibniz Alternating Series Test):**
> Let $(b_n)_{n=1}^\infty$ be a sequence such that:
> 1. $b_n > 0$ for all $n$.
> 2. $b_{n+1} \le b_n$ for all $n$ (monotonically decreasing).
> 3. $\lim_{n \to \infty} b_n = 0$.
> Then the alternating series $\sum_{n=1}^\infty (-1)^{n+1} b_n = b_1 - b_2 + b_3 - b_4 + \dots$ converges.
> Furthermore, the remainder satisfies $|R_n| = |S - s_n| \le b_{n+1}$.

---

### 2. Dirichlet's and Abel's Tests for Convergence

Both tests rely on the technique of **Abel summation by parts**:
$$\sum_{k=1}^n a_k b_k = s_n b_{n+1} - \sum_{k=1}^n s_k (b_{k+1} - b_k), \quad \text{where } s_k = \sum_{j=1}^k a_j$$

> **Theorem 4.13 (Dirichlet's Test):**
> If the partial sums $s_n = \sum_{k=1}^n a_k$ are bounded (i.e., $|s_n| \le M$ for all $n$), and $(b_n)$ decreases monotonically to 0 ($b_n \ge b_{n+1} \ge 0$ and $b_n \to 0$), then $\sum_{n=1}^\infty a_n b_n$ converges.

> **Theorem 4.14 (Abel's Test):**
> If $\sum a_n$ converges, and $(b_n)$ is a monotone bounded sequence, then $\sum a_n b_n$ converges.

---

### 3. Riemann's Rearrangement Theorem

One of the most astonishing theorems in classical analysis, demonstrating the fundamental fragility of conditional convergence:

> **Theorem 4.15 (Riemann Rearrangement Theorem):**
> Let $\sum_{n=1}^\infty a_n$ be a **conditionally convergent** series of real numbers.
> For any extended real number $S \in [-\infty, \infty]$, there exists a bijection (permutation) $\sigma: \mathbb{N} \to \mathbb{N}$ such that the rearranged series:
> $$\sum_{n=1}^\infty a_{\sigma(n)} = S$$
> (In stark contrast, if $\sum a_n$ converges *absolutely*, every rearrangement converges to the exact same sum).

#### Line-by-Line Proof:
Decompose each term into positive and negative parts:
$$p_n = \max\{a_n, 0\} \ge 0 \quad \text{and} \quad q_n = \max\{-a_n, 0\} \ge 0$$
So $a_n = p_n - q_n$ and $|a_n| = p_n + q_n$.
Since $\sum a_n$ converges conditionally:
- $\sum a_n = \sum (p_n - q_n)$ converges.
- $\sum |a_n| = \sum (p_n + q_n)$ diverges.
If either $\sum p_n$ or $\sum q_n$ converged, the other would have to converge as well, forcing $\sum |a_n|$ to converge.
Thus, **both $\sum p_n = \infty$ and $\sum q_n = \infty$ must diverge to $+\infty$!**
Furthermore, since $\sum a_n$ converges, $\lim p_n = 0$ and $\lim q_n = 0$.

Let $S \in \mathbb{R}$ be any target number.
1. Take positive terms $p_1, p_2, \dots, p_{k_1}$ in original order just until the partial sum strictly exceeds $S$:
   $$\sum_{j=1}^{k_1} p_j > S$$
   (This is always possible because $\sum p_n = \infty$).
2. Now take negative terms $-q_1, -q_2, \dots, -q_{m_1}$ in original order just until the total sum falls strictly below $S$:
   $$\sum_{j=1}^{k_1} p_j - \sum_{j=1}^{m_1} q_j < S$$
   (This is always possible because $\sum q_n = \infty$).
3. Continue alternating: add subsequent positive terms until exceeding $S$, then subsequent negative terms until falling below $S$.
At each turn, the difference between the partial sum and $S$ is bounded by the last term added:
$$|s_N - S| \le \max\{ p_{k_r}, q_{m_r} \}$$
Since $p_n \to 0$ and $q_n \to 0$, the overshoot and undershoot shrink to 0 as $N \to \infty$.
Therefore, the rearranged series converges precisely to $S$! $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational / Problem 4.1",
                "title": "Rigorous Determination of Series Convergence via Ratio and Integral Tests",
                "statement": r"""Test the convergence of the following two series with complete analytical justification:
1. $\sum_{n=1}^\infty \frac{n^2 2^n}{(2n)!}$
2. $\sum_{n=2}^\infty \frac{1}{n (\ln n)^p}$ for all real parameter values $p \in \mathbb{R}$.""",
                "hints": [
                    "For part 1, apply the d'Alembert Ratio Test and simplify the factorial (2n+2)!.",
                    "For part 2, use the Cauchy Condensation Test or the Integral Test with substitution u = ln(x)."
                ],
                "solution": r"""### 1. Convergence of $\sum_{n=1}^\infty \frac{n^2 2^n}{(2n)!}$
Let $a_n = \frac{n^2 2^n}{(2n)!}$. Since all terms are positive, we apply the d'Alembert Ratio Test:
$$\begin{aligned}
\frac{a_{n+1}}{a_n} &= \frac{(n+1)^2 2^{n+1}}{(2n+2)!} \cdot \frac{(2n)!}{n^2 2^n} \\
&= \frac{(n+1)^2}{n^2} \cdot \frac{2^{n+1}}{2^n} \cdot \frac{(2n)!}{(2n+2)(2n+1)(2n)!} \\
&= \left( 1 + \frac{1}{n} \right)^2 \cdot 2 \cdot \frac{1}{(2n+2)(2n+1)}
\end{aligned}$$
Taking the limit as $n \to \infty$:
$$L = \lim_{n \to \infty} \frac{a_{n+1}}{a_n} = 1^2 \cdot 2 \cdot 0 = 0$$
Since $L = 0 < 1$, by the Ratio Test (Theorem 4.8), the series **converges absolutely**.

---

### 2. Convergence of $\sum_{n=2}^\infty \frac{1}{n (\ln n)^p}$
Let $f(x) = \frac{1}{x (\ln x)^p}$ on $[2, \infty)$.
For $x \ge 2$:
- $f(x) > 0$.
- For $p \ge 0$, both $x$ and $(\ln x)^p$ are strictly increasing, so $f(x)$ is strictly decreasing.
We apply the Maclaurin-Cauchy Integral Test (Theorem 4.9):
$$I = \int_2^\infty \frac{1}{x (\ln x)^p} \, dx$$
Make the substitution $u = \ln x$, with $du = \frac{1}{x} \, dx$:
$$I = \int_{\ln 2}^\infty \frac{1}{u^p} \, du = \lim_{M \to \infty} \int_{\ln 2}^M u^{-p} \, du$$
We evaluate the three cases:
- **Case 1: $p > 1$:**
  $$I = \lim_{M \to \infty} \left[ \frac{u^{1-p}}{1-p} \right]_{\ln 2}^M = 0 - \frac{(\ln 2)^{1-p}}{1-p} = \frac{1}{(p-1)(\ln 2)^{p-1}} < \infty$$
  The integral converges, so the series **converges**.
- **Case 2: $p = 1$:**
  $$I = \lim_{M \to \infty} [\ln u]_{\ln 2}^M = \lim_{M \to \infty} (\ln M - \ln(\ln 2)) = \infty$$
  The integral diverges, so the series **diverges**.
- **Case 3: $p < 1$:**
  Since $u^{-p}$ has an exponent $1 - p > 0$, $\lim_{M \to \infty} M^{1-p} = \infty$.
  The integral diverges, so the series **diverges**.
- **Case 4: $p \le 0$:**
  Here $\frac{1}{n (\ln n)^p} \ge \frac{1}{n}$, which diverges by direct comparison with the harmonic series.
Conclusion: The series converges **if and only if $p > 1$**."""
            },
            {
                "tier": "Advanced / Problem 4.2",
                "title": "Cauchy Condensation Proof & The Logarithmic Hierarchy",
                "statement": r"""1. Provide a rigorous, self-contained proof of the Cauchy Condensation Test (Theorem 4.5).
2. Apply the test to rigorously investigate the convergence of the iterated logarithmic series:
   $$\sum_{n=3}^\infty \frac{1}{n \ln n \ln(\ln n)}$$""",
                "hints": [
                    "Condense the series once: replace n with 2^k and multiply by 2^k.",
                    "Then apply condensation a second time to the resulting sequence."
                ],
                "solution": r"""### 1. Rigorous Proof of the Cauchy Condensation Test
Let $a_n \ge 0$ with $a_1 \ge a_2 \ge a_3 \ge \dots \ge 0$.
Define $s_n = \sum_{j=1}^n a_j$ and $t_k = \sum_{j=0}^k 2^j a_{2^j}$.

**Direction 1: If $(t_k)$ converges to $T$, then $(s_n)$ converges.**
For any $n \in \mathbb{N}$, choose $k$ such that $n \le 2^k - 1$.
Group $s_n$ into powers-of-two intervals:
$$\begin{aligned}
s_n \le s_{2^k - 1} &= a_1 + (a_2 + a_3) + (a_4 + a_5 + a_6 + a_7) + \dots + (a_{2^{k-1}} + \dots + a_{2^k-1}) \\
&\le a_1 + 2 a_2 + 4 a_4 + \dots + 2^{k-1} a_{2^{k-1}} = t_{k-1} \le T
\end{aligned}$$
Since $(s_n)$ is non-decreasing and bounded above by $T$, by the Monotone Convergence Theorem, $(s_n)$ converges.

**Direction 2: If $(s_n)$ converges to $S$, then $(t_k)$ converges.**
For any $k \in \mathbb{N}$, consider the index $2^k$:
$$\begin{aligned}
s_{2^k} &= a_1 + a_2 + (a_3 + a_4) + (a_5 + a_6 + a_7 + a_8) + \dots + (a_{2^{k-1}+1} + \dots + a_{2^k}) \\
&\ge a_1 + a_2 + 2 a_4 + 4 a_8 + \dots + 2^{k-1} a_{2^k} \\
&= \frac{1}{2} (2 a_1 + 2 a_2 + 4 a_4 + \dots + 2^k a_{2^k}) \\
&\ge \frac{1}{2} (a_1 + 2 a_2 + 4 a_4 + \dots + 2^k a_{2^k}) = \frac{1}{2} t_k
\end{aligned}$$
Thus $t_k \le 2 s_{2^k} \le 2S$.
Being non-decreasing and bounded above by $2S$, $(t_k)$ converges. $\blacksquare$

---

### 2. Application to the Iterated Logarithmic Series
Let $a_n = \frac{1}{n \ln n \ln(\ln n)}$ for $n \ge 3$.
Since $n$, $\ln n$, and $\ln(\ln n)$ are all strictly increasing positive functions for $n \ge 3$, $(a_n)$ is strictly decreasing and non-negative.
By Cauchy Condensation, $\sum a_n$ converges if and only if $\sum 2^k a_{2^k}$ converges:
$$2^k a_{2^k} = 2^k \frac{1}{2^k \ln(2^k) \ln(\ln 2^k)} = \frac{1}{(k \ln 2) \ln(k \ln 2)}$$
Factoring out the constant $\frac{1}{\ln 2}$:
$$\sum 2^k a_{2^k} \sim \frac{1}{\ln 2} \sum_{k} \frac{1}{k (\ln k + \ln(\ln 2))}$$
For large $k$, by limit comparison with $b_k = \frac{1}{k \ln k}$:
$$\lim_{k \to \infty} \frac{\frac{1}{k (\ln k + \ln(\ln 2))}}{\frac{1}{k \ln k}} = 1$$
Now condense a second time on $b_k = \frac{1}{k \ln k}$:
$$2^j b_{2^j} = 2^j \frac{1}{2^j \ln(2^j)} = \frac{1}{j \ln 2} = \frac{1}{\ln 2} \cdot \frac{1}{j}$$
The series $\sum \frac{1}{j}$ is the harmonic series, which diverges!
Therefore, by condensation:
- $\sum \frac{1}{j}$ diverges $\implies \sum \frac{1}{k \ln k}$ diverges $\implies \sum 2^k a_{2^k}$ diverges $\implies \sum_{n=3}^\infty \frac{1}{n \ln n \ln(\ln n)}$ **diverges**. $\blacksquare$"""
            },
            {
                "tier": "Honors / Problem 4.3",
                "title": "Comprehensive Proof of the Riemann Rearrangement Theorem",
                "statement": r"""Let $\sum_{n=1}^\infty a_n$ be a conditionally convergent series.
Let $M \in \mathbb{R}$ be an arbitrary real number.
1. Prove that both the sub-series of strictly positive terms and strictly negative terms diverge:
   $$\sum_{n: a_n > 0} a_n = +\infty \quad \text{and} \quad \sum_{n: a_n < 0} a_n = -\infty$$
2. Construct an explicit bijection $\pi: \mathbb{N} \to \mathbb{N}$ such that:
   $$\sum_{k=1}^\infty a_{\pi(k)} = M$$
3. Prove that for any $\epsilon > 0$, the partial sums of the rearranged series satisfy $|s_N - M| < \epsilon$ for all sufficiently large $N$.""",
                "hints": [
                    "Express a_n = p_n - q_n with p_n, q_n >= 0.",
                    "Show that if either sum converged, absolute convergence would result.",
                    "Bound the partial sum deviation by the magnitude of the last term added, and use the fact that a_n -> 0."
                ],
                "solution": r"""### 1. Divergence of Positive and Negative Sub-series
Define:
$$p_n = \frac{|a_n| + a_n}{2} = \begin{cases} a_n & \text{if } a_n > 0 \\ 0 & \text{if } a_n \le 0 \end{cases}$$
$$q_n = \frac{|a_n| - a_n}{2} = \begin{cases} -a_n & \text{if } a_n < 0 \\ 0 & \text{if } a_n \ge 0 \end{cases}$$
Notice that $p_n \ge 0$, $q_n \ge 0$, $a_n = p_n - q_n$, and $|a_n| = p_n + q_n$.
Suppose for contradiction that $\sum p_n = P < \infty$.
Since $\sum a_n = S$ converges, the sequence of partial sums of $q_n$ satisfies:
$$\sum_{n=1}^k q_n = \sum_{n=1}^k p_n - \sum_{n=1}^k a_n \implies \sum_{n=1}^\infty q_n = P - S < \infty$$
Then:
$$\sum_{n=1}^\infty |a_n| = \sum_{n=1}^\infty (p_n + q_n) = P + (P - S) < \infty$$
This would mean $\sum a_n$ converges absolutely, contradicting that it converges conditionally!
By identical reasoning, $\sum q_n$ cannot converge.
Since both have non-negative terms and diverge, we have:
$$\sum_{n=1}^\infty p_n = +\infty \quad \text{and} \quad \sum_{n=1}^\infty q_n = +\infty \quad \blacksquare$$

---

### 2. Algorithmic Construction of the Permutation $\pi$
Let $(u_i)_{i=1}^\infty$ be the sequence of positive terms of $(a_n)$ in their original relative order.
Let $(-v_j)_{j=1}^\infty$ be the sequence of negative terms of $(a_n)$ in their original relative order (so $v_j > 0$).
Since $\sum a_n$ converges, $\lim u_i = 0$ and $\lim v_j = 0$.

We define the rearrangement iteratively:
- **Phase 1:** Since $\sum u_i = \infty$, choose the smallest integer $k_1$ such that:
  $$\sum_{i=1}^{k_1} u_i > M$$
- **Phase 2:** Since $\sum v_j = \infty$, choose the smallest integer $m_1$ such that:
  $$\sum_{i=1}^{k_1} u_i - \sum_{j=1}^{m_1} v_j < M$$
- **Inductive Step:** Having chosen $k_1 < k_2 < \dots < k_{r-1}$ and $m_1 < m_2 < \dots < m_{r-1}$, choose the smallest $k_r > k_{r-1}$ such that:
  $$\sum_{i=1}^{k_r} u_i - \sum_{j=1}^{m_{r-1}} v_j > M$$
  Then choose the smallest $m_r > m_{r-1}$ such that:
  $$\sum_{i=1}^{k_r} u_i - \sum_{j=1}^{m_r} v_j < M$$

This defines a permutation $\pi: \mathbb{N} \to \mathbb{N}$ that includes every term of $(a_n)$ exactly once without omission or repetition.

---

### 3. Proof of Convergence to $M$
Let $\epsilon > 0$ be arbitrary.
Since $u_i \to 0$ and $v_j \to 0$, there exists an index $N_0$ such that:
$$\forall i \ge N_0, \; u_i < \epsilon \quad \text{and} \quad \forall j \ge N_0, \; v_j < \epsilon$$
Choose $R$ large enough that $k_R \ge N_0$ and $m_R \ge N_0$.
Now consider any partial sum $s_N$ of the rearranged series for $N \ge k_R + m_R$.
- During an upward phase (adding positive terms):
  The partial sum never exceeds $M + u_{k_r} < M + \epsilon$ because we stop as soon as we cross $M$.
  The lowest it can be is $M - v_{m_{r-1}} > M - \epsilon$.
- During a downward phase (adding negative terms):
  The partial sum never falls below $M - v_{m_r} > M - \epsilon$ because we stop as soon as we fall below $M$.
  The highest it can be is $M + u_{k_r} < M + \epsilon$.
Therefore, for all $N \ge k_R + m_R$:
$$M - \epsilon < s_N < M + \epsilon \iff |s_N - M| < \epsilon$$
Thus:
$$\lim_{N \to \infty} s_N = M \quad \blacksquare$$"""
            }
        ]
    }
    return u4

if __name__ == "__main__":
    u = get_unit4()
    print(f"Loaded Unit 4: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
