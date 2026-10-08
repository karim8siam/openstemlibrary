# -*- coding: utf-8 -*-
"""
build_ra_unit7.py
Constructs Unit 7: Riemann & Riemann-Stieltjes Integration & Sequences of Functions
"""

def get_unit7():
    u7 = {
        "number": 7,
        "title": "Riemann & Riemann-Stieltjes Integration & Sequences of Functions",
        "leadSummary": "Exhaustive theory of integration and function spaces: partitions and Darboux sums, the Riemann integrability criterion, Lebesgue's characterization of Riemann integrability via sets of measure zero, the Fundamental Theorem of Calculus (Parts 1 & 2), the Riemann-Stieltjes integral, pointwise versus uniform convergence, the Weierstrass M-test, and interchange theorems for limits, integrals, and derivatives.",
        "simulations": ["sim_ra_riemann_uniform_conv"],
        "sections": [
            {
                "secNumber": "7.1",
                "title": "Partitions, Darboux Upper and Lower Sums & The Riemann Criterion",
                "content": r"""### 1. Partitions and Tagged Partitions

Let $[a, b] \subset \mathbb{R}$ be a compact interval.

> **Definition 7.1 (Partition and Mesh):**
> A **partition** $P$ of $[a, b]$ is a finite ordered set of points:
> $$P = \{ x_0, x_1, x_2, \dots, x_n \}, \quad \text{where } a = x_0 < x_1 < x_2 < \dots < x_n = b$$
> The subintervals are $\Delta x_i = x_i - x_{i-1}$ for $i \in \{1, 2, \dots, n\}$.
> The **mesh** (or norm) of $P$ is the length of its longest subinterval:
> $$\|P\| = \max_{1 \le i \le n} \Delta x_i$$
> A partition $P^*$ is a **refinement** of $P$ if $P \subseteq P^*$.

---

### 2. Darboux Upper and Lower Sums

Let $f: [a, b] \to \mathbb{R}$ be a bounded function.
On each subinterval $[x_{i-1}, x_i]$, define:
$$M_i = \sup \{ f(x) : x \in [x_{i-1}, x_i] \} \quad \text{and} \quad m_i = \inf \{ f(x) : x \in [x_{i-1}, x_i] \}$$

> **Definition 7.2 (Darboux Sums):**
> 1. The **Upper Darboux Sum** is:
>    $$U(f, P) = \sum_{i=1}^n M_i \Delta x_i$$
> 2. The **Lower Darboux Sum** is:
>    $$L(f, P) = \sum_{i=1}^n m_i \Delta x_i$$
> 3. Clearly, $L(f, P) \le U(f, P)$ for every partition $P$.

> **Lemma 7.1 (Refinement Lemma):**
> If $P^*$ is a refinement of $P$ ($P \subseteq P^*$), then:
> $$L(f, P) \le L(f, P^*) \le U(f, P^*) \le U(f, P)$$
> That is, refining a partition increases the lower sum and decreases the upper sum.

#### Proof Sketch:
If $P^*$ adds one point $c \in (x_{k-1}, x_k)$, the term $M_k \Delta x_k$ splits into $M_{k,1}(c - x_{k-1}) + M_{k,2}(x_k - c)$.
Since $M_{k,1} \le M_k$ and $M_{k,2} \le M_k$, the sum can only decrease or stay equal. $\blacksquare$

> **Corollary 7.1:** For any two arbitrary partitions $P_1$ and $P_2$:
> $$L(f, P_1) \le U(f, P_2)$$
> *Proof:* Take the common refinement $P^* = P_1 \cup P_2$. Then $L(f, P_1) \le L(f, P^*) \le U(f, P^*) \le U(f, P_2)$. $\blacksquare$

---

### 3. Darboux Upper and Lower Integrals & The Riemann Criterion

> **Definition 7.3 (Darboux Integrals):**
> 1. The **Upper Integral** is:
>    $$\overline{\int_a^b} f(x) \, dx = \inf \{ U(f, P) : P \text{ is a partition of } [a, b] \}$$
> 2. The **Lower Integral** is:
>    $$\underline{\int_a^b} f(x) \, dx = \sup \{ L(f, P) : P \text{ is a partition of } [a, b] \}$$
> By Corollary 7.1, $\underline{\int_a^b} f \le \overline{\int_a^b} f$ always.

> **Definition 7.4 (Riemann Integrability):**
> A bounded function $f: [a, b] \to \mathbb{R}$ is **Riemann integrable** on $[a, b]$, denoted $f \in \mathcal{R}[a, b]$, if:
> $$\underline{\int_a^b} f(x) \, dx = \overline{\int_a^b} f(x) \, dx$$
> This common value is the **Riemann integral**, denoted $\int_a^b f(x) \, dx$.

> **Theorem 7.1 (Riemann / Darboux Integrability Criterion):**
> A bounded function $f: [a, b] \to \mathbb{R}$ is Riemann integrable if and only if for every $\epsilon > 0$, there exists a partition $P_\epsilon$ of $[a, b]$ such that:
> $$U(f, P_\epsilon) - L(f, P_\epsilon) < \epsilon$$

#### Proof:
$(\implies)$ If $\underline{\int} f = \overline{\int} f = I$, by definition of infimum and supremum, for any $\epsilon > 0$ there exist $P_1, P_2$ such that $U(f, P_1) < I + \epsilon/2$ and $L(f, P_2) > I - \epsilon/2$.
Let $P_\epsilon = P_1 \cup P_2$. Then $U(f, P_\epsilon) - L(f, P_\epsilon) \le U(f, P_1) - L(f, P_2) < \epsilon$.
$(\impliedby)$ For any partition $P$, $0 \le \overline{\int} f - \underline{\int} f \le U(f, P) - L(f, P) < \epsilon$. Since this holds for all $\epsilon > 0$, $\overline{\int} f = \underline{\int} f$. $\blacksquare$"""
            },
            {
                "secNumber": "7.2",
                "title": "Properties of the Integral & Lebesgue's Integrability Criterion",
                "content": r"""### 1. Classes of Riemann Integrable Functions

> **Theorem 7.2 (Integrability of Continuous Functions):**
> If $f: [a, b] \to \mathbb{R}$ is continuous on $[a, b]$, then $f \in \mathcal{R}[a, b]$.

#### Proof:
Since $[a, b]$ is compact and $f$ is continuous, by the Heine-Cantor Theorem (Theorem 5.7), $f$ is **uniformly continuous** on $[a, b]$.
Let $\epsilon > 0$ be given.
Choose $\delta > 0$ such that $|x - y| < \delta \implies |f(x) - f(y)| < \frac{\epsilon}{b - a}$.
Choose any partition $P$ with mesh $\|P\| < \delta$.
On each subinterval $[x_{i-1}, x_i]$, by the Extreme Value Theorem, $f$ attains its maximum at some $u_i$ and minimum at some $v_i$.
Since $|u_i - v_i| \le \Delta x_i \le \|P\| < \delta$, we have:
$$M_i - m_i = f(u_i) - f(v_i) < \frac{\epsilon}{b - a}$$
Now evaluate the Darboux difference:
$$U(f, P) - L(f, P) = \sum_{i=1}^n (M_i - m_i) \Delta x_i < \frac{\epsilon}{b - a} \sum_{i=1}^n \Delta x_i = \frac{\epsilon}{b - a} (b - a) = \epsilon$$
By the Riemann Criterion (Theorem 7.1), $f \in \mathcal{R}[a, b]$. $\blacksquare$

> **Theorem 7.3 (Integrability of Monotone Functions):**
> If $f: [a, b] \to \mathbb{R}$ is monotonic on $[a, b]$, then $f \in \mathcal{R}[a, b]$.
> *(Proof uses regular partition with equal subintervals $\Delta x = \frac{b - a}{n}$, leading to telescoping sum $(M_i - m_i)$).*

---

### 2. Lebesgue's Criterion for Riemann Integrability

The definitive characterization of Riemann integrability was discovered by Henri Lebesgue using measure theory:

> **Definition 7.5 (Set of Measure Zero):**
> A set $E \subset \mathbb{R}$ has **Lebesgue measure zero** if for every $\epsilon > 0$, there exists a countable collection of open intervals $\{ (a_k, b_k) \}_{k=1}^\infty$ covering $E$ such that:
> $$\sum_{k=1}^\infty (b_k - a_k) < \epsilon$$

> **Theorem 7.4 (Lebesgue-Vitali Integrability Theorem):**
> A bounded function $f: [a, b] \to \mathbb{R}$ is Riemann integrable if and only if the set of its discontinuities has Lebesgue measure zero:
> $$f \in \mathcal{R}[a, b] \iff \operatorname{m}(\{ x \in [a, b] : f \text{ is discontinuous at } x \}) = 0$$

#### Implications:
- Any continuous function is integrable (discontinuity set is empty, measure 0).
- Any function with countably many discontinuities is integrable (every countable set has measure 0).
- Thomae's popcorn function is Riemann integrable on $[0, 1]$ (discontinuous only on $\mathbb{Q}$, which is countable).
- The Dirichlet indicator function $\mathbf{1}_\mathbb{Q}$ is discontinuous everywhere on $[0, 1]$. Its discontinuity set has measure 1, so it is **not Riemann integrable**."""
            },
            {
                "secNumber": "7.3",
                "title": "The Fundamental Theorem of Calculus & The Riemann-Stieltjes Integral",
                "content": r"""### 1. Fundamental Theorem of Calculus (Part 1)

> **Theorem 7.5 (FTC Part 1 - Differentiation of the Integral):**
> Let $f \in \mathcal{R}[a, b]$ and define the accumulation function:
> $$F(x) = \int_a^x f(t) \, dt \quad \text{for } x \in [a, b]$$
> 1. $F$ is uniformly continuous (in fact, Lipschitz continuous) on $[a, b]$.
> 2. If $f$ is continuous at a point $x_0 \in (a, b)$, then $F$ is differentiable at $x_0$ and:
>    $$F'(x_0) = f(x_0)$$

#### Complete Line-by-Line Proof:
Let $x_0 \in (a, b)$ be a point where $f$ is continuous.
Consider the difference quotient of $F$ at $x_0$:
$$\frac{F(x_0 + h) - F(x_0)}{h} - f(x_0) = \frac{1}{h} \int_{x_0}^{x_0 + h} f(t) \, dt - f(x_0) = \frac{1}{h} \int_{x_0}^{x_0 + h} [f(t) - f(x_0)] \, dt$$
Let $\epsilon > 0$ be given.
Since $f$ is continuous at $x_0$, there exists $\delta > 0$ such that:
$$|t - x_0| < \delta \implies |f(t) - f(x_0)| < \epsilon$$
For any $h$ with $0 < |h| < \delta$, all points $t$ between $x_0$ and $x_0 + h$ satisfy $|t - x_0| < \delta$.
Therefore:
$$\left| \frac{F(x_0 + h) - F(x_0)}{h} - f(x_0) \right| \le \frac{1}{|h|} \left| \int_{x_0}^{x_0 + h} |f(t) - f(x_0)| \, dt \right| \le \frac{1}{|h|} \epsilon |h| = \epsilon$$
Since $\epsilon > 0$ was arbitrary, we conclude:
$$\lim_{h \to 0} \frac{F(x_0 + h) - F(x_0)}{h} = f(x_0) \iff F'(x_0) = f(x_0) \quad \blacksquare$$

---

### 2. Fundamental Theorem of Calculus (Part 2)

> **Theorem 7.6 (FTC Part 2 - Evaluation Theorem):**
> If $f: [a, b] \to \mathbb{R}$ is differentiable on $[a, b]$ and $f' \in \mathcal{R}[a, b]$, then:
> $$\int_a^b f'(t) \, dt = f(b) - f(a)$$

#### Line-by-Line Proof:
Let $P = \{x_0, x_1, \dots, x_n\}$ be any partition of $[a, b]$.
We express $f(b) - f(a)$ as a telescoping sum:
$$f(b) - f(a) = \sum_{i=1}^n [f(x_i) - f(x_{i-1})]$$
On each subinterval $[x_{i-1}, x_i]$, $f$ is continuous on $[x_{i-1}, x_i]$ and differentiable on $(x_{i-1}, x_i)$.
By Lagrange's Mean Value Theorem (Theorem 6.6), there exists $c_i \in (x_{i-1}, x_i)$ such that:
$$f(x_i) - f(x_{i-1}) = f'(c_i) \Delta x_i$$
Therefore:
$$f(b) - f(a) = \sum_{i=1}^n f'(c_i) \Delta x_i$$
Notice that on $[x_{i-1}, x_i]$, $m_i \le f'(c_i) \le M_i$, where $m_i = \inf_{[x_{i-1}, x_i]} f'$ and $M_i = \sup_{[x_{i-1}, x_i]} f'$.
Multiplying by $\Delta x_i > 0$ and summing:
$$L(f', P) = \sum_{i=1}^n m_i \Delta x_i \le f(b) - f(a) \le \sum_{i=1}^n M_i \Delta x_i = U(f', P)$$
This inequality holds for **every** partition $P$ of $[a, b]$.
Taking the supremum over all lower sums and infimum over all upper sums:
$$\underline{\int_a^b} f'(t) \, dt \le f(b) - f(a) \le \overline{\int_a^b} f'(t) \, dt$$
Since $f' \in \mathcal{R}[a, b]$, the upper and lower integrals coincide and equal $\int_a^b f'(t) \, dt$.
Therefore:
$$\int_a^b f'(t) \, dt = f(b) - f(a) \quad \blacksquare$$

---

### 3. The Riemann-Stieltjes Integral

> **Definition 7.6 (Riemann-Stieltjes Integral):**
> Let $\alpha: [a, b] \to \mathbb{R}$ be a monotonically increasing integrator function.
> For partition $P$, define $\Delta \alpha_i = \alpha(x_i) - \alpha(x_{i-1}) \ge 0$.
> The Riemann-Stieltjes sums are formed by weighting by $\Delta \alpha_i$.
> If $\alpha$ is continuously differentiable ($\alpha \in C^1[a, b]$), the Stieltjes integral reduces to:
> $$\int_a^b f(x) \, d\alpha(x) = \int_a^b f(x) \alpha'(x) \, dx$$"""
            },
            {
                "secNumber": "7.4",
                "title": "Sequences of Functions: Uniform Convergence & The Weierstrass M-Test",
                "content": r"""### 1. Pointwise vs. Uniform Convergence

> **Definition 7.7 (Pointwise Convergence):**
> A sequence of functions $f_n: E \to \mathbb{R}$ converges **pointwise** to $f: E \to \mathbb{R}$ if for every $x \in E$:
> $$\lim_{n \to \infty} f_n(x) = f(x)$$
> That is, $\forall \epsilon > 0$ and $\forall x \in E$, $\exists N(\epsilon, x) \in \mathbb{N}$ such that $\forall n \ge N$, $|f_n(x) - f(x)| < \epsilon$.

> **Definition 7.8 (Uniform Convergence):**
> A sequence of functions $f_n: E \to \mathbb{R}$ converges **uniformly** to $f$ on $E$, denoted $f_n \rightrightarrows f$, if for every $\epsilon > 0$, there exists an index $N \in \mathbb{N}$ (**independent of $x$**) such that:
> $$\forall n \ge N \text{ and } \forall x \in E, \quad |f_n(x) - f(x)| < \epsilon$$
> Equivalently, in terms of the uniform norm (supremum norm):
> $$\lim_{n \to \infty} \|f_n - f\|_\infty = \lim_{n \to \infty} \sup_{x \in E} |f_n(x) - f(x)| = 0$$

---

### 2. The Uniform Cauchy Criterion

> **Theorem 7.7 (Uniform Cauchy Criterion):**
> A sequence of functions $(f_n)$ converges uniformly on $E$ if and only if for every $\epsilon > 0$, there exists $N \in \mathbb{N}$ such that:
> $$\forall n, m \ge N \text{ and } \forall x \in E, \quad |f_n(x) - f_m(x)| < \epsilon$$

---

### 3. The Weierstrass $M$-Test for Infinite Series of Functions

> **Theorem 7.8 (Weierstrass $M$-Test):**
> Let $\sum_{n=1}^\infty f_n(x)$ be an infinite series of functions defined on $E \subseteq \mathbb{R}$.
> Suppose there exists a sequence of positive real constants $(M_n)_{n=1}^\infty$ such that:
> 1. $|f_n(x)| \le M_n$ for all $x \in E$ and all $n \in \mathbb{N}$.
> 2. The numerical series $\sum_{n=1}^\infty M_n$ converges.
> Then the series of functions $\sum_{n=1}^\infty f_n(x)$ converges **uniformly and absolutely** on $E$.

#### Complete Proof:
Let $\epsilon > 0$.
Since the scalar series $\sum M_n$ converges, by the Cauchy Criterion for series (Theorem 4.2), there exists $N \in \mathbb{N}$ such that:
$$\forall m > n \ge N, \quad \sum_{k=n+1}^m M_k < \epsilon$$
Now consider the partial sums of the function series: $S_n(x) = \sum_{k=1}^n f_k(x)$.
For any $m > n \ge N$ and for **all** $x \in E$:
$$|S_m(x) - S_n(x)| = \left| \sum_{k=n+1}^m f_k(x) \right| \le \sum_{k=n+1}^m |f_k(x)| \le \sum_{k=n+1}^m M_k < \epsilon$$
By the Uniform Cauchy Criterion (Theorem 7.7), the sequence of partial sums $(S_n(x))$ converges uniformly on $E$.
Therefore, $\sum_{n=1}^\infty f_n(x)$ converges uniformly on $E$. $\blacksquare$"""
            },
            {
                "secNumber": "7.5",
                "title": "Interchange Theorems: Limits, Integrals & Derivatives",
                "content": r"""### 1. Uniform Limit of Continuous Functions is Continuous

Does the limit of continuous functions have to be continuous? For pointwise convergence, the answer is NO: $f_n(x) = x^n$ on $[0, 1]$ is continuous for each $n$, but converges pointwise to $f(x) = 0$ ($x < 1$) and $f(1) = 1$, which is discontinuous at $x = 1$.
Under **uniform convergence**, continuity is preserved!

> **Theorem 7.9 (Uniform Convergence Preserves Continuity):**
> If $f_n: E \to \mathbb{R}$ is continuous on $E$ for each $n$, and $f_n \rightrightarrows f$ uniformly on $E$, then the limit function $f$ is continuous on $E$.

#### Rigorous "$\epsilon/3$" Proof:
Let $c \in E$ and let $\epsilon > 0$ be given.
Since $f_n \rightrightarrows f$ uniformly, choose $N \in \mathbb{N}$ such that:
$$\forall x \in E, \quad |f_N(x) - f(x)| < \frac{\epsilon}{3}$$
Since $f_N$ is continuous at $c$, choose $\delta > 0$ such that:
$$\forall x \in E \text{ with } |x - c| < \delta, \quad |f_N(x) - f_N(c)| < \frac{\epsilon}{3}$$
Now, for any $x \in E$ with $|x - c| < \delta$, apply the Triangle Inequality:
$$\begin{aligned}
|f(x) - f(c)| &= |(f(x) - f_N(x)) + (f_N(x) - f_N(c)) + (f_N(c) - f(c))| \\
&\le |f(x) - f_N(x)| + |f_N(x) - f_N(c)| + |f_N(c) - f(c)| \\
&< \frac{\epsilon}{3} + \frac{\epsilon}{3} + \frac{\epsilon}{3} = \epsilon
\end{aligned}$$
Thus $f$ is continuous at $c$. Since $c$ was arbitrary, $f$ is continuous on $E$. $\blacksquare$

---

### 2. Interchange of Limit and Integral

> **Theorem 7.10 (Uniform Convergence & Integration):**
> Let $f_n \in \mathcal{R}[a, b]$ for each $n$, and suppose $f_n \rightrightarrows f$ uniformly on $[a, b]$.
> Then $f \in \mathcal{R}[a, b]$ and:
> $$\lim_{n \to \infty} \int_a^b f_n(x) \, dx = \int_a^b \left( \lim_{n \to \infty} f_n(x) \right) \, dx = \int_a^b f(x) \, dx$$

#### Proof:
Let $\epsilon > 0$. Choose $N$ such that $\forall n \ge N$ and $\forall x \in [a, b]$, $|f_n(x) - f(x)| < \frac{\epsilon}{b - a}$.
Then for any $n \ge N$:
$$\left| \int_a^b f_n(x) \, dx - \int_a^b f(x) \, dx \right| = \left| \int_a^b [f_n(x) - f(x)] \, dx \right| \le \int_a^b |f_n(x) - f(x)| \, dx < \frac{\epsilon}{b - a}(b - a) = \epsilon \quad \blacksquare$$

---

### 3. Interchange of Limit and Derivative

> **Theorem 7.11 (Uniform Convergence & Differentiation):**
> Let $f_n: [a, b] \to \mathbb{R}$ be differentiable on $[a, b]$. Suppose:
> 1. There exists at least one point $x_0 \in [a, b]$ where $(f_n(x_0))$ converges.
> 2. The sequence of derivatives $(f'_n)$ converges **uniformly** on $[a, b]$ to some function $g$.
> Then $(f_n)$ converges uniformly on $[a, b]$ to a differentiable function $f$, and:
> $$f'(x) = \lim_{n \to \infty} f'_n(x) = g(x) \quad \forall x \in [a, b]$$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational / Problem 7.1",
                "title": "Exact Darboux Sum Computation & Riemann Integrability of x^2",
                "statement": r"""Consider the quadratic function $f(x) = x^2$ on the interval $[0, b]$ where $b > 0$.
1. Using the uniform partition $P_n = \{0, \frac{b}{n}, \frac{2b}{n}, \dots, \frac{nb}{n}\}$, compute explicit closed-form expressions for the Upper Darboux sum $U(f, P_n)$ and Lower Darboux sum $L(f, P_n)$ in terms of $b$ and $n$.
2. Compute $\lim_{n \to \infty} U(f, P_n)$ and $\lim_{n \to \infty} L(f, P_n)$.
3. Conclude by the Darboux Integrability Criterion that $f \in \mathcal{R}[0, b]$ and find $\int_0^b x^2 \, dx$.""",
                "hints": [
                    "Recall the sum of squares formula: sum_{k=1}^n k^2 = n(n+1)(2n+1)/6.",
                    "On subinterval [(k-1)b/n, kb/n], infimum is ((k-1)b/n)^2 and supremum is (kb/n)^2."
                ],
                "solution": r"""### 1. Closed-Form Expressions for Darboux Sums
For the regular partition $P_n$, $\Delta x_i = \frac{b}{n}$ for all $i \in \{1, 2, \dots, n\}$.
Since $f(x) = x^2$ is strictly increasing on $[0, b]$:
- On the $k$-th subinterval $\left[ \frac{(k-1)b}{n}, \frac{kb}{n} \right]$:
  $$M_k = f\left(\frac{kb}{n}\right) = \frac{k^2 b^2}{n^2} \quad \text{and} \quad m_k = f\left(\frac{(k-1)b}{n}\right) = \frac{(k-1)^2 b^2}{n^2}$$

#### Upper Darboux Sum:
$$U(f, P_n) = \sum_{k=1}^n M_k \Delta x_k = \sum_{k=1}^n \frac{k^2 b^2}{n^2} \cdot \frac{b}{n} = \frac{b^3}{n^3} \sum_{k=1}^n k^2$$
Using $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$:
$$U(f, P_n) = \frac{b^3}{n^3} \cdot \frac{n(n+1)(2n+1)}{6} = \frac{b^3}{6} \left(1 + \frac{1}{n}\right)\left(2 + \frac{1}{n}\right)$$

#### Lower Darboux Sum:
$$L(f, P_n) = \sum_{k=1}^n m_k \Delta x_k = \frac{b^3}{n^3} \sum_{k=1}^n (k-1)^2 = \frac{b^3}{n^3} \sum_{j=0}^{n-1} j^2$$
Using $\sum_{j=0}^{n-1} j^2 = \frac{(n-1)n(2n-1)}{6}$:
$$L(f, P_n) = \frac{b^3}{n^3} \cdot \frac{(n-1)n(2n-1)}{6} = \frac{b^3}{6} \left(1 - \frac{1}{n}\right)\left(2 - \frac{1}{n}\right)$$

---

### 2. Limits as $n \to \infty$
Taking the limit as $n \to \infty$:
$$\lim_{n \to \infty} U(f, P_n) = \frac{b^3}{6} (1 + 0)(2 + 0) = \frac{2b^3}{6} = \frac{b^3}{3}$$
$$\lim_{n \to \infty} L(f, P_n) = \frac{b^3}{6} (1 - 0)(2 - 0) = \frac{2b^3}{6} = \frac{b^3}{3}$$

---

### 3. Conclusion of Integrability
Evaluating the difference:
$$U(f, P_n) - L(f, P_n) = \frac{b^3}{6} \left[ \left(2 + \frac{3}{n} + \frac{1}{n^2}\right) - \left(2 - \frac{3}{n} + \frac{1}{n^2}\right) \right] = \frac{b^3}{6} \cdot \frac{6}{n} = \frac{b^3}{n}$$
For any $\epsilon > 0$, choosing $n > \frac{b^3}{\epsilon}$ guarantees $U(f, P_n) - L(f, P_n) < \epsilon$.
By the Darboux Integrability Criterion (Theorem 7.1), $f \in \mathcal{R}[0, b]$.
Furthermore:
$$\overline{\int_0^b} x^2 \, dx \le U(f, P_n) \to \frac{b^3}{3} \quad \text{and} \quad \underline{\int_0^b} x^2 \, dx \ge L(f, P_n) \to \frac{b^3}{3}$$
Therefore:
$$\int_0^b x^2 \, dx = \frac{b^3}{3} \quad \blacksquare$$"""
            },
            {
                "tier": "Advanced / Problem 7.2",
                "title": "Complete Deductive Chain: Fundamental Theorem of Calculus Parts 1 & 2",
                "statement": r"""1. Let $f \in \mathcal{R}[a, b]$ and $F(x) = \int_a^x f(t) \, dt$. Prove that $F$ is Lipschitz continuous on $[a, b]$.
2. Prove that if $f$ is continuous at $c \in [a, b]$, then $F'(c) = f(c)$.
3. Use Part 1 and Part 2 to evaluate:
   $$\frac{d}{dx} \int_{\sin x}^{x^3} \sqrt{1 + t^4} \, dt$$""",
                "hints": [
                    "Since f is Riemann integrable, f is bounded: |f(t)| <= M.",
                    "Use the Leibniz Integral Rule and Chain Rule for part 3."
                ],
                "solution": r"""### 1. Proof that $F$ is Lipschitz Continuous
Since $f \in \mathcal{R}[a, b]$, $f$ is bounded on $[a, b]$ by definition of the Riemann integral.
Thus there exists $M > 0$ such that $|f(t)| \le M$ for all $t \in [a, b]$.
For any $x, y \in [a, b]$ with $x < y$:
$$|F(y) - F(x)| = \left| \int_a^y f(t) \, dt - \int_a^x f(t) \, dt \right| = \left| \int_x^y f(t) \, dt \right| \le \int_x^y |f(t)| \, dt \le M(y - x) = M|y - x|$$
Thus $F$ is Lipschitz continuous on $[a, b]$ with Lipschitz constant $M$. $\blacksquare$

---

### 2. Proof that $F'(c) = f(c)$
Let $f$ be continuous at $c$.
Let $\epsilon > 0$ be given.
By continuity of $f$ at $c$, there exists $\delta > 0$ such that $|t - c| < \delta \implies |f(t) - f(c)| < \epsilon$.
For any $h$ with $0 < |h| < \delta$:
$$\frac{F(c + h) - F(c)}{h} - f(c) = \frac{1}{h} \int_c^{c+h} f(t) \, dt - \frac{1}{h} \int_c^{c+h} f(c) \, dt = \frac{1}{h} \int_c^{c+h} [f(t) - f(c)] \, dt$$
Taking absolute values:
$$\left| \frac{F(c + h) - F(c)}{h} - f(c) \right| \le \frac{1}{|h|} \left| \int_c^{c+h} |f(t) - f(c)| \, dt \right| < \frac{1}{|h|} \epsilon |h| = \epsilon$$
Therefore:
$$\lim_{h \to 0} \frac{F(c + h) - F(c)}{h} = f(c) \iff F'(c) = f(c) \quad \blacksquare$$

---

### 3. Evaluation of the Derivative via Leibniz Rule
Let $I(x) = \int_{\sin x}^{x^3} \sqrt{1 + t^4} \, dt$.
Let $g(t) = \sqrt{1 + t^4}$. Since $g$ is continuous on $\mathbb{R}$, by FTC Part 1, it has an antiderivative $G(u) = \int_0^u g(t) \, dt$ with $G'(u) = g(u)$.
We rewrite:
$$I(x) = \int_0^{x^3} g(t) \, dt - \int_0^{\sin x} g(t) \, dt = G(x^3) - G(\sin x)$$
Differentiating with respect to $x$ using the Chain Rule:
$$I'(x) = G'(x^3) \cdot \frac{d}{dx}[x^3] - G'(\sin x) \cdot \frac{d}{dx}[\sin x] = g(x^3)(3x^2) - g(\sin x)(\cos x)$$
Substituting $g(t) = \sqrt{1 + t^4}$:
$$I'(x) = 3x^2 \sqrt{1 + (x^3)^4} - \cos x \sqrt{1 + (\sin x)^4} = 3x^2 \sqrt{1 + x^{12}} - \cos x \sqrt{1 + \sin^4 x} \quad \blacksquare$$"""
            },
            {
                "tier": "Honors / Problem 7.3",
                "title": "Comprehensive Proof of the Uniform Limit Integration Theorem & Failure Cases",
                "statement": r"""1. Prove Theorem 7.10: If $f_n \in \mathcal{R}[a, b]$ and $f_n \rightrightarrows f$ uniformly on $[a, b]$, then $f \in \mathcal{R}[a, b]$ and $\lim_{n \to \infty} \int_a^b f_n = \int_a^b f$.
2. Construct an explicit counterexample demonstrating that the conclusion can completely fail if convergence is merely pointwise. Specifically, analyze $f_n(x) = n x (1 - x^2)^n$ on $[0, 1]$.
3. Use the Weierstrass $M$-Test to prove that $g(x) = \sum_{n=1}^\infty \frac{\cos(n x)}{n^2}$ is continuous on $\mathbb{R}$ and evaluate $\int_0^\pi g(x) \, dx$ term by term.""",
                "hints": [
                    "For part 1, use Darboux criterion: |f_n - f| < eps implies bounds on upper and lower sums.",
                    "For part 2, find the pointwise limit of f_n(x) on [0, 1] and compare its integral with lim int f_n.",
                    "For part 3, bound |cos(nx)/n^2| <= 1/n^2 and use sum 1/n^2 < infty."
                ],
                "solution": r"""### 1. Rigorous Proof of Theorem 7.10

**Step 1: Prove $f \in \mathcal{R}[a, b]$.**
Let $\epsilon > 0$.
Since $f_n \rightrightarrows f$, choose $N \in \mathbb{N}$ such that:
$$\forall x \in [a, b], \quad |f(x) - f_N(x)| < \frac{\epsilon}{3(b - a)}$$
This means:
$$f_N(x) - \frac{\epsilon}{3(b - a)} < f(x) < f_N(x) + \frac{\epsilon}{3(b - a)}$$
Since $f_N \in \mathcal{R}[a, b]$, choose a partition $P$ such that $U(f_N, P) - L(f_N, P) < \frac{\epsilon}{3}$.
For this partition $P$:
$$U(f, P) \le U\left(f_N + \frac{\epsilon}{3(b - a)}, P\right) = U(f_N, P) + \frac{\epsilon}{3}$$
$$L(f, P) \ge L\left(f_N - \frac{\epsilon}{3(b - a)}, P\right) = L(f_N, P) - \frac{\epsilon}{3}$$
Subtracting:
$$U(f, P) - L(f, P) \le U(f_N, P) - L(f_N, P) + \frac{2\epsilon}{3} < \frac{\epsilon}{3} + \frac{2\epsilon}{3} = \epsilon$$
By the Riemann criterion, $f \in \mathcal{R}[a, b]$.

**Step 2: Prove $\int_a^b f_n \to \int_a^b f$.**
For any $n \ge N$:
$$\left| \int_a^b f_n(x) \, dx - \int_a^b f(x) \, dx \right| \le \int_a^b |f_n(x) - f(x)| \, dx \le \int_a^b \frac{\epsilon}{3(b - a)} \, dx = \frac{\epsilon}{3} < \epsilon$$
Thus $\lim_{n \to \infty} \int_a^b f_n = \int_a^b f$. $\blacksquare$

---

### 2. Failure of Interchange Under Mere Pointwise Convergence
Consider $f_n(x) = n x (1 - x^2)^n$ on $[0, 1]$.
- At $x = 0$: $f_n(0) = 0 \to 0$.
- At $x = 1$: $f_n(1) = 0 \to 0$.
- For $x \in (0, 1)$: $0 < 1 - x^2 < 1$. By standard exponential decay, $\lim_{n \to \infty} n (1 - x^2)^n = 0$.
Thus, $f_n(x) \to 0$ pointwise for all $x \in [0, 1]$.
Therefore:
$$\int_0^1 \left(\lim_{n \to \infty} f_n(x)\right) \, dx = \int_0^1 0 \, dx = 0$$
Now compute the integral of $f_n$ before taking the limit:
$$\int_0^1 n x (1 - x^2)^n \, dx$$
Substitute $u = 1 - x^2$, $du = -2x \, dx$:
$$\int_0^1 n x (1 - x^2)^n \, dx = -\frac{n}{2} \int_1^0 u^n \, du = \frac{n}{2} \int_0^1 u^n \, du = \frac{n}{2} \left[ \frac{u^{n+1}}{n+1} \right]_0^1 = \frac{n}{2(n+1)}$$
Taking the limit as $n \to \infty$:
$$\lim_{n \to \infty} \int_0^1 f_n(x) \, dx = \lim_{n \to \infty} \frac{n}{2(n+1)} = \frac{1}{2}$$
Notice that:
$$\frac{1}{2} = \lim_{n \to \infty} \int_0^1 f_n(x) \, dx \ne \int_0^1 \lim_{n \to \infty} f_n(x) \, dx = 0$$
The limit and integral **cannot be interchanged** because the convergence is not uniform! $\blacksquare$

---

### 3. Application of Weierstrass $M$-Test
Let $u_n(x) = \frac{\cos(nx)}{n^2}$ on $\mathbb{R}$.
For all $x \in \mathbb{R}$:
$$|u_n(x)| = \left| \frac{\cos(nx)}{n^2} \right| \le \frac{1}{n^2} = M_n$$
The scalar series $\sum_{n=1}^\infty M_n = \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6} < \infty$ converges ($p$-series with $p = 2$).
By the Weierstrass $M$-Test (Theorem 7.8), the series $\sum_{n=1}^\infty \frac{\cos(nx)}{n^2}$ converges **uniformly** on $\mathbb{R}$.
Since each $\frac{\cos(nx)}{n^2}$ is continuous, by Theorem 7.9, the sum function $g(x)$ is **continuous** on $\mathbb{R}$.
By Theorem 7.10, we can integrate term by term on $[0, \pi]$:
$$\int_0^\pi g(x) \, dx = \sum_{n=1}^\infty \int_0^\pi \frac{\cos(nx)}{n^2} \, dx = \sum_{n=1}^\infty \left[ \frac{\sin(nx)}{n^3} \right]_0^\pi = \sum_{n=1}^\infty (0 - 0) = 0 \quad \blacksquare$$"""
            }
        ]
    }
    return u7

if __name__ == "__main__":
    u = get_unit7()
    print(f"Loaded Unit 7: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
