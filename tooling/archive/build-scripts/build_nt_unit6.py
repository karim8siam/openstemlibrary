# -*- coding: utf-8 -*-
"""
build_nt_unit6.py
Constructs Unit 6: Möbius Inversion, Average Orders & Ramanujan Sums
"""

def get_unit6():
    u6 = {
        "number": 6,
        "title": "Möbius Inversion, Average Orders & Ramanujan Sums",
        "leadSummary": "Advanced arithmetical function transforms and asymptotic distribution theory: the Möbius function $\\mu(n)$ as the Dirichlet inverse of the constant function, the Möbius Inversion Formula and its multiplicative analogue, Ramanujan's trigonometric sums $c_q(n)$ and their structural identities, the von Mangoldt function $\\Lambda(n)$ and Chebyshev's prime counting functions, and Dirichlet's hyperbola method for the average order of the divisor function.",
        "simulations": ["sim_nt_mobius_ramanujan"],
        "sections": [
            {
                "secNumber": "6.1",
                "title": "The Möbius Function mu(n) & The Möbius Inversion Formula",
                "content": r"""### 1. The Möbius Function

August Ferdinand Möbius introduced this fundamental function in 1832.

> **Definition 6.1 (The Möbius Function):**
> The **Möbius function** $\mu: \mathbb{N} \to \{-1, 0, 1\}$ is defined by:
> $$\mu(n) = \begin{cases}
> 1 & \text{if } n = 1 \\
> (-1)^k & \text{if } n = p_1 p_2 \cdots p_k \text{ is a product of } k \text{ distinct primes (square-free)} \\
> 0 & \text{if } n \text{ is divisible by a square of a prime } (p^2 \mid n)
> \end{cases}$$

> **Theorem 6.1 (Fundamental Divisor Sum Identity of $\mu$):**
> For every positive integer $n \ge 1$:
> $$\sum_{d \mid n} \mu(d) = \epsilon(n) = \begin{cases} 1 & \text{if } n = 1 \\ 0 & \text{if } n > 1 \end{cases}$$
> In the language of Dirichlet convolution, $\mu$ is the **Dirichlet inverse** of the constant function $u(n) = 1$:
> $$\mu * u = \epsilon \iff u^{-1} = \mu$$

> **Proof:**
> For $n = 1$: $\sum_{d \mid 1} \mu(d) = \mu(1) = 1$.
> For $n > 1$: let $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$ with $k \ge 1$.
> Any divisor $d \mid n$ with a square factor contributes $\mu(d) = 0$.
> Thus, only square-free divisors $d = p_{i_1} p_{i_2} \cdots p_{i_j}$ contribute non-zero values $\mu(d) = (-1)^j$.
> The number of such divisors having exactly $j$ prime factors is $\binom{k}{j}$.
> Therefore, summing over all possible counts of prime factors $j \in \{0, 1, \dots, k\}$:
> $$\sum_{d \mid n} \mu(d) = \sum_{j=0}^k \binom{k}{j} (-1)^j = \binom{k}{0} - \binom{k}{1} + \binom{k}{2} - \dots + (-1)^k \binom{k}{k}$$
> By the Binomial Theorem:
> $$\sum_{j=0}^k \binom{k}{j} (-1)^j = (1 - 1)^k = 0^k = 0 \quad (\text{since } k \ge 1)$$
> This establishes the identity completely. $\blacksquare$

---

### 2. The Möbius Inversion Formula

> **Theorem 6.2 (The Möbius Inversion Formula):**
> Let $f$ and $F$ be arithmetical functions. Then:
> $$F(n) = \sum_{d \mid n} f(d) \iff f(n) = \sum_{d \mid n} \mu(d) F\left(\frac{n}{d}\right)$$

> **Proof (via Dirichlet Convolution):**
> The relation $F(n) = \sum_{d \mid n} f(d)$ is expressed concisely as:
> $$F = f * u$$
> Convolving both sides with the Möbius function $\mu$:
> $$F * \mu = (f * u) * \mu$$
> By associativity and commutativity of Dirichlet convolution (Theorem 5.8):
> $$F * \mu = f * (u * \mu) = f * \epsilon = f$$
> Thus:
> $$f(n) = (F * \mu)(n) = \sum_{d \mid n} \mu(d) F\left(\frac{n}{d}\right)$$
> The reverse implication follows symmetrically by convolving with $u$. $\blacksquare$"""
            },
            {
                "secNumber": "6.2",
                "title": "Applications to Euler's Function & Multiplicative Inversion",
                "content": r"""### 1. Inversion of Euler's Totient Identity

> **Theorem 6.3 (Gauss's Totient Divisor Sum):**
> For every positive integer $n \ge 1$:
> $$\sum_{d \mid n} \phi(d) = n$$

> **Proof:**
> Partition the set of integers $\{1, 2, \dots, n\}$ into classes based on their greatest common divisor with $n$:
> $$S_d = \{k \in \{1, 2, \dots, n\} : \gcd(k, n) = d\} \quad \text{for each } d \mid n$$
> Notice that $\gcd(k, n) = d \iff \gcd(k/d, n/d) = 1$.
> Letting $k' = k/d$, the number of such integers is the number of $1 \le k' \le n/d$ with $\gcd(k', n/d) = 1$, which is precisely $\phi(n/d)$.
> Summing the sizes of all disjoint subsets $S_d$:
> $$n = \sum_{d \mid n} |S_d| = \sum_{d \mid n} \phi\left(\frac{n}{d}\right) = \sum_{d \mid n} \phi(d) \quad \blacksquare$$

Applying the Möbius Inversion Formula to $F(n) = n$ and $f(n) = \phi(n)$:

> **Theorem 6.4 (Möbius Inversion Formula for $\phi(n)$):**
> $$\phi(n) = \sum_{d \mid n} \mu(d) \frac{n}{d} = n \sum_{d \mid n} \frac{\mu(d)}{d}$$

---

### 2. Multiplicative Form of Möbius Inversion

For multiplicative relationships involving products rather than sums:

> **Theorem 6.5 (Product Form of Möbius Inversion):**
> Let $g$ and $G$ be functions from $\mathbb{N}$ to $\mathbb{C}^\times$. Then:
> $$G(n) = \prod_{d \mid n} g(d) \iff g(n) = \prod_{d \mid n} G\left(\frac{n}{d}\right)^{\mu(d)}$$

> **Proof:**
> Take the complex logarithm on both sides: $\ln G(n) = \sum_{d \mid n} \ln g(d)$.
> Applying standard additive Möbius Inversion to $\ln G$ and $\ln g$:
> $$\ln g(n) = \sum_{d \mid n} \mu(d) \ln G\left(\frac{n}{d}\right) = \ln \left[ \prod_{d \mid n} G\left(\frac{n}{d}\right)^{\mu(d)} \right]$$
> Exponentiating both sides establishes the result. $\blacksquare$"""
            },
            {
                "secNumber": "6.3",
                "title": "Ramanujan's Trigonometric Sums cq(n) & Explicit Closed Forms",
                "content": r"""### 1. Definition of Ramanujan's Sum

Srinivasa Ramanujan introduced these sums in his 1918 paper *On Certain Trigonometrical Sums and their Applications in the Theory of Numbers*.

> **Definition 6.2 (Ramanujan's Trigonometric Sum):**
> For positive integers $q, n \in \mathbb{N}$, **Ramanujan's sum** $c_q(n)$ is defined as the sum of the $n$-th powers of the primitive $q$-th roots of unity:
> $$c_q(n) = \sum_{\substack{a=1 \\ \gcd(a, q) = 1}}^q e^{2\pi i \frac{a n}{q}} = \sum_{\substack{a=1 \\ \gcd(a, q) = 1}}^q \cos\left(\frac{2\pi a n}{q}\right)$$
> (the imaginary sine components cancel out by symmetry).

---

### 2. The Fundamental Identity of Ramanujan's Sum

> **Theorem 6.6 (Ramanujan's Divisor Sum Identity):**
> For all positive integers $q$ and $n$:
> $$c_q(n) = \sum_{d \mid \gcd(q, n)} d \, \mu\left(\frac{q}{d}\right)$$

> **Proof:**
> Recall the fundamental character orthogonality sum for roots of unity:
> $$\eta_q(n) = \sum_{a=1}^q e^{2\pi i \frac{a n}{q}} = \begin{cases} q & \text{if } q \mid n \\ 0 & \text{if } q \nmid n \end{cases}$$
> Every residue $a \in \{1, 2, \dots, q\}$ satisfies $\gcd(a, q) = d$ for some unique divisor $d \mid q$.
> Writing $a = d a'$ and $q = d q'$ with $\gcd(a', q') = 1$:
> $$\eta_q(n) = \sum_{d \mid q} \sum_{\substack{a'=1 \\ \gcd(a', q/d) = 1}}^{q/d} e^{2\pi i \frac{a' n}{q/d}} = \sum_{d \mid q} c_{q/d}(n) = \sum_{k \mid q} c_k(n)$$
> Applying Möbius Inversion (Theorem 6.2) with respect to the variable $q$:
> $$c_q(n) = \sum_{d \mid q} \mu\left(\frac{q}{d}\right) \eta_d(n)$$
> Since $\eta_d(n) = d$ when $d \mid n$ and $0$ otherwise, the sum runs only over divisors $d$ that divide **both** $q$ and $n$, that is, $d \mid \gcd(q, n)$:
> $$c_q(n) = \sum_{d \mid \gcd(q, n)} d \, \mu\left(\frac{q}{d}\right) \quad \blacksquare$$

> **Corollary 6.1 (Special Values):**
> 1. When $n = 1$: $c_q(1) = \mu(q)$.
> 2. When $q \mid n$: $c_q(n) = \phi(q)$.
> 3. For any prime $p$:
>    $$c_p(n) = \begin{cases} p - 1 & \text{if } p \mid n \\ -1 & \text{if } p \nmid n \end{cases}$$"""
            },
            {
                "secNumber": "6.4",
                "title": "The von Mangoldt Function & Chebyshev's Counting Functions",
                "content": r"""### 1. The von Mangoldt Function $\Lambda(n)$

> **Definition 6.3 (The von Mangoldt Function):**
> The **von Mangoldt function** $\Lambda: \mathbb{N} \to \mathbb{R}$ is defined by:
> $$\Lambda(n) = \begin{cases}
> \ln p & \text{if } n = p^k \text{ for some prime } p \text{ and integer } k \ge 1 \\
> 0 & \text{otherwise}
> \end{cases}$$

> **Theorem 6.7 (Logarithmic Divisor Sum Identity):**
> For every positive integer $n \ge 1$:
> $$\sum_{d \mid n} \Lambda(d) = \ln n$$

> **Proof:**
> Let $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$ be the prime factorization.
> The only divisors $d \mid n$ for which $\Lambda(d) \ne 0$ are the prime powers $p_i^j$ ($1 \le j \le a_i$).
> Therefore:
> $$\sum_{d \mid n} \Lambda(d) = \sum_{i=1}^k \sum_{j=1}^{a_i} \Lambda(p_i^j) = \sum_{i=1}^k \sum_{j=1}^{a_i} \ln p_i = \sum_{i=1}^k a_i \ln p_i = \ln \left( \prod_{i=1}^k p_i^{a_i} \right) = \ln n \quad \blacksquare$$

By Möbius Inversion:
$$\Lambda(n) = \sum_{d \mid n} \mu(d) \ln\left(\frac{n}{d}\right) = -\sum_{d \mid n} \mu(d) \ln d$$

---

### 2. Chebyshev's Functions $\psi(x)$ and $\theta(x)$

Pafnuty Chebyshev introduced these functions to study the distribution of primes.

> **Definition 6.4 (Chebyshev Functions):**
> For $x \ge 1$:
> 1. **Chebyshev's theta function:** $\theta(x) = \sum_{p \le x} \ln p$
> 2. **Chebyshev's psi function:** $\psi(x) = \sum_{n \le x} \Lambda(n) = \sum_{p^k \le x} \ln p$

> **Theorem 6.8 (Equivalence with Prime Number Theorem):**
> The Prime Number Theorem $\pi(x) \sim \frac{x}{\ln x}$ is logically equivalent to:
> $$\psi(x) \sim x \quad \text{and} \quad \theta(x) \sim x \quad \text{as } x \to \infty$$"""
            },
            {
                "secNumber": "6.5",
                "title": "Average Orders of Arithmetical Functions & Dirichlet's Hyperbola Method",
                "content": r"""### 1. The Concept of Average Order

Many arithmetical functions (like $\tau(n)$ or $\mu(n)$) fluctuate wildly from point to point.
To understand their macroscopic behavior, number theorists study their **average order**:
$$\bar{f}(x) = \frac{1}{x} \sum_{n \le x} f(n)$$
We say $f(n)$ has average order $g(n)$ if $\sum_{n \le x} f(n) \sim \sum_{n \le x} g(n)$.

---

### 2. Dirichlet's Divisor Problem & The Hyperbola Method

Consider the summatory function of the divisor function:
$$D(x) = \sum_{n \le x} \tau(n) = \sum_{n \le x} \sum_{d \mid n} 1$$
This counts the total number of integer lattice points $(u, v) \in \mathbb{N}^2$ lying under the hyperbola:
$$u \cdot v \le x$$

> **Theorem 6.9 (Dirichlet's Divisor Asymptotic, 1849):**
> As $x \to \infty$:
> $$\sum_{n \le x} \tau(n) = x \ln x + (2\gamma - 1)x + O(\sqrt{x})$$
> where $\gamma \approx 0.57721566...$ is the **Euler-Mascheroni constant**.

> **Proof (Dirichlet's Hyperbola Method):**
> Consider the hyperbolic region $\mathcal{R} = \{(u, v) \in \mathbb{R}^2 : u \ge 1, v \ge 1, uv \le x\}$.
> By symmetry across the line $u = v$, split the region into three pieces:
> 1. Region I: $u \le \sqrt{x}$ and $v \le x/u$.
> 2. Region II: $v \le \sqrt{x}$ and $u \le x/v$.
> 3. Overlap (square): $u \le \sqrt{x}$ and $v \le \sqrt{x}$.
> Counting lattice points by inclusion-exclusion:
> $$D(x) = 2 \sum_{u \le \sqrt{x}} \left\lfloor \frac{x}{u} \right\rfloor - \lfloor \sqrt{x} \rfloor^2$$
> Replace $\lfloor x/u \rfloor = x/u - \{x/u\}$:
> $$\sum_{u \le \sqrt{x}} \left\lfloor \frac{x}{u} \right\rfloor = x \sum_{u \le \sqrt{x}} \frac{1}{u} + O(\sqrt{x})$$
> Recall the asymptotic for harmonic numbers $H_N = \sum_{k=1}^N \frac{1}{k} = \ln N + \gamma + O(1/N)$.
> Setting $N = \lfloor \sqrt{x} \rfloor$:
> $$\sum_{u \le \sqrt{x}} \frac{1}{u} = \ln(\sqrt{x}) + \gamma + O\left(\frac{1}{\sqrt{x}}\right) = \frac{1}{2}\ln x + \gamma + O\left(\frac{1}{\sqrt{x}}\right)$$
> Multiplying by $2x$:
> $$2 x \sum_{u \le \sqrt{x}} \frac{1}{u} = 2x \left(\frac{1}{2}\ln x + \gamma\right) + O(\sqrt{x}) = x \ln x + 2\gamma x + O(\sqrt{x})$$
> Now subtract the overlap square $\lfloor \sqrt{x} \rfloor^2 = (\sqrt{x} + O(1))^2 = x + O(\sqrt{x})$:
> $$D(x) = [x \ln x + 2\gamma x] - x + O(\sqrt{x}) = x \ln x + (2\gamma - 1)x + O(\sqrt{x}) \quad \blacksquare$$"""
            }
        ],
        "problems": [
            {
                "id": "nt-prob-6-1",
                "tier": "Foundational",
                "title": "Möbius Inversion Verification for Euler's Totient at n = 30",
                "statement": r"""Consider the integer $n = 30$:
1. List all positive divisors $d$ of $30$.
2. Compute the value of the Möbius function $\mu(d)$ for each divisor.
3. Apply the Möbius inversion identity $\phi(n) = \sum_{d \mid n} d \, \mu(n/d)$ to explicitly compute $\phi(30)$ and verify that it matches the product formula.""",
                "hints": [
                    "Factor 30 = 2 * 3 * 5. It has 8 divisors.",
                    "Check which divisors are square-free to compute mu(d).",
                    "Evaluate the sum sum_{d | 30} d * mu(30/d)."
                ],
                "solution": r"""### 1. Divisors of $30$
The prime factorization is $30 = 2 \times 3 \times 5$.
The positive divisors are:
$$\{1, 2, 3, 5, 6, 10, 15, 30\} \quad \blacksquare$$

---

### 2. Values of the Möbius Function
- $\mu(1) = 1$
- $\mu(2) = (-1)^1 = -1$
- $\mu(3) = (-1)^1 = -1$
- $\mu(5) = (-1)^1 = -1$
- $\mu(6) = \mu(2 \times 3) = (-1)^2 = 1$
- $\mu(10) = \mu(2 \times 5) = (-1)^2 = 1$
- $\mu(15) = \mu(3 \times 5) = (-1)^2 = 1$
- $\mu(30) = \mu(2 \times 3 \times 5) = (-1)^3 = -1 \quad \blacksquare$$

---

### 3. Möbius Inversion Evaluation
Using $\phi(30) = \sum_{d \mid 30} d \, \mu(30/d)$:
$$\begin{aligned}
\phi(30) &= 1 \times \mu(30) + 2 \times \mu(15) + 3 \times \mu(10) + 5 \times \mu(6) \\
&\quad + 6 \times \mu(5) + 10 \times \mu(3) + 15 \times \mu(2) + 30 \times \mu(1) \\
&= 1(-1) + 2(1) + 3(1) + 5(1) + 6(-1) + 10(-1) + 15(-1) + 30(1) \\
&= -1 + 2 + 3 + 5 - 6 - 10 - 15 + 30 \\
&= 9 - 31 + 30 = 8
\end{aligned}$$
Verification via Euler's product formula:
$$\phi(30) = 30 \left(1 - \frac{1}{2}\right)\left(1 - \frac{1}{3}\right)\left(1 - \frac{1}{5}\right) = 30 \times \frac{1}{2} \times \frac{2}{3} \times \frac{4}{5} = 30 \times \frac{8}{30} = 8 \quad \checkmark$$
The two calculations match identically! $\blacksquare$$"""
            },
            {
                "id": "nt-prob-6-2",
                "tier": "Advanced",
                "title": "Evaluation of Ramanujan's Trigonometric Sum c_6(n)",
                "statement": r"""Consider Ramanujan's trigonometric sum $c_6(n) = \sum_{\substack{a=1 \\ \gcd(a, 6)=1}}^6 e^{2\pi i a n / 6}$:
1. Identify all reduced residues modulo $6$.
2. State Ramanujan's identity $c_q(n) = \sum_{d \mid \gcd(q, n)} d \, \mu(q/d)$.
3. Evaluate $c_6(n)$ explicitly for each integer $n \in \{1, 2, 3, 4, 5, 6\}$.""",
                "hints": [
                    "The residues coprime to 6 are 1 and 5.",
                    "Evaluate gcd(6, n) for each n.",
                    "Compute the divisor sum for each gcd."
                ],
                "solution": r"""### 1. Reduced Residues Modulo $6$
The integers in $\{1, 2, 3, 4, 5, 6\}$ coprime to $6$ are:
$$\{1, 5\}$$
Thus, $\phi(6) = 2$, and the sum has exactly two terms:
$$c_6(n) = e^{2\pi i (1) n / 6} + e^{2\pi i (5) n / 6} = e^{i \pi n / 3} + e^{-i \pi n / 3} = 2 \cos\left(\frac{\pi n}{3}\right) \quad \blacksquare$$

---

### 2. Divisor Formula
By Theorem 6.6:
$$c_6(n) = \sum_{d \mid \gcd(6, n)} d \, \mu\left(\frac{6}{d}\right) \quad \blacksquare$$

---

### 3. Explicit Values for $n = 1, 2, 3, 4, 5, 6$
- **For $n = 1$:** $\gcd(6, 1) = 1$.
  $$c_6(1) = 1 \cdot \mu(6/1) = \mu(6) = 1$$
  Trigonometric check: $2 \cos(\pi/3) = 2(1/2) = 1 \quad \checkmark$
- **For $n = 2$:** $\gcd(6, 2) = 2$. Divisors: $\{1, 2\}$.
  $$c_6(2) = 1 \cdot \mu(6) + 2 \cdot \mu(3) = 1(1) + 2(-1) = 1 - 2 = -1$$
  Trigonometric check: $2 \cos(2\pi/3) = 2(-1/2) = -1 \quad \checkmark$
- **For $n = 3$:** $\gcd(6, 3) = 3$. Divisors: $\{1, 3\}$.
  $$c_6(3) = 1 \cdot \mu(6) + 3 \cdot \mu(2) = 1(1) + 3(-1) = 1 - 3 = -2$$
  Trigonometric check: $2 \cos(\pi) = 2(-1) = -2 \quad \checkmark$
- **For $n = 4$:** $\gcd(6, 4) = 2$.
  $$c_6(4) = c_6(2) = -1$$
  Trigonometric check: $2 \cos(4\pi/3) = 2(-1/2) = -1 \quad \checkmark$
- **For $n = 5$:** $\gcd(6, 5) = 1$.
  $$c_6(5) = c_6(1) = 1$$
  Trigonometric check: $2 \cos(5\pi/3) = 2(1/2) = 1 \quad \checkmark$
- **For $n = 6$:** $\gcd(6, 6) = 6$. Divisors: $\{1, 2, 3, 6\}$.
  $$c_6(6) = 1 \cdot \mu(6) + 2 \cdot \mu(3) + 3 \cdot \mu(2) + 6 \cdot \mu(1) = 1(1) + 2(-1) + 3(-1) + 6(1) = 1 - 2 - 3 + 6 = 2 = \phi(6)$$
  Trigonometric check: $2 \cos(2\pi) = 2(1) = 2 \quad \checkmark$

Summary of values:
$$(c_6(1), c_6(2), c_6(3), c_6(4), c_6(5), c_6(6)) = (1, -1, -2, -1, 1, 2) \quad \blacksquare$$"""
            },
            {
                "id": "nt-prob-6-3",
                "tier": "Honors / Proof Challenge",
                "title": "Dirichlet's Hyperbola Method: Detailed Error Term Derivation",
                "statement": r"""Prove Dirichlet's asymptotic formula for the sum of the divisor function:
$$\sum_{n \le x} \tau(n) = x \ln x + (2\gamma - 1)x + O(\sqrt{x})$$
1. Express $\sum_{n \le x} \tau(n)$ as the count of integer lattice points $(u, v) \in \mathbb{N}^2$ such that $u v \le x$.
2. Decompose the counting sum using Dirichlet's hyperbola symmetry across $u = v = \sqrt{x}$.
3. Use the Euler-Maclaurin expansion for harmonic numbers $\sum_{u \le K} \frac{1}{u} = \ln K + \gamma + O(1/K)$ to evaluate the principal terms and rigorously establish the $O(\sqrt{x})$ error bound.""",
                "hints": [
                    "Split into u <= sqrt(x) and v <= sqrt(x), with overlap [sqrt(x)]^2.",
                    "Use sum_{u <= sqrt(x)} floor(x/u) = sum_{u <= sqrt(x)} (x/u - {x/u}).",
                    "Bound sum_{u <= sqrt(x)} {x/u} <= sqrt(x)."
                ],
                "solution": r"""### 1. Lattice Point Representation
Recall that $\tau(n) = \sum_{d \mid n} 1 = \sum_{u v = n} 1$.
Therefore:
$$D(x) = \sum_{n \le x} \tau(n) = \sum_{n \le x} \sum_{u v = n} 1 = \sum_{\substack{u, v \in \mathbb{N} \\ u v \le x}} 1$$
This counts the total number of integer points in the first quadrant lying on or beneath the rectangular hyperbola $u v = x$. $\blacksquare$

---

### 2. Dirichlet's Hyperbola Decomposition
Let $K = \lfloor \sqrt{x} \rfloor$.
The hyperbola region can be split into three parts:
1. Points with $u \le K$: for each fixed $u$, $v$ can range from $1$ to $\lfloor x/u \rfloor$.
   Count $= \sum_{u=1}^K \lfloor x/u \rfloor$.
2. Points with $v \le K$: by symmetry between $u$ and $v$, this also equals $\sum_{v=1}^K \lfloor x/v \rfloor$.
3. Points in the square $[1, K] \times [1, K]$ were counted in both (1) and (2).
   Their count is $K^2 = \lfloor \sqrt{x} \rfloor^2$.
By inclusion-exclusion:
$$D(x) = 2 \sum_{u=1}^K \left\lfloor \frac{x}{u} \right\rfloor - K^2 \quad \blacksquare$$

---

### 3. Evaluation of the Sums and Error Bounding
Write $\lfloor x/u \rfloor = \frac{x}{u} - \left\{ \frac{x}{u} \right\}$ where $\{t\} \in [0, 1)$ denotes the fractional part:
$$\sum_{u=1}^K \left\lfloor \frac{x}{u} \right\rfloor = \sum_{u=1}^K \left( \frac{x}{u} - \left\{ \frac{x}{u} \right\} \right) = x \sum_{u=1}^K \frac{1}{u} - \sum_{u=1}^K \left\{ \frac{x}{u} \right\}$$
Since $0 \le \{x/u\} < 1$:
$$0 \le \sum_{u=1}^K \left\{ \frac{x}{u} \right\} < K \le \sqrt{x} \implies \sum_{u=1}^K \left\{ \frac{x}{u} \right\} = O(\sqrt{x})$$
Now use the classical asymptotic expansion of the harmonic sum:
$$\sum_{u=1}^K \frac{1}{u} = \ln K + \gamma + O\left(\frac{1}{K}\right)$$
Since $K = \sqrt{x} + O(1)$, we have:
$$\ln K = \ln(\sqrt{x} + O(1)) = \ln\left( \sqrt{x}\left(1 + O\left(\frac{1}{\sqrt{x}}\right)\right) \right) = \frac{1}{2}\ln x + O\left(\frac{1}{\sqrt{x}}\right)$$
Thus:
$$\sum_{u=1}^K \frac{1}{u} = \frac{1}{2}\ln x + \gamma + O\left(\frac{1}{\sqrt{x}}\right)$$
Multiplying by $x$:
$$x \sum_{u=1}^K \frac{1}{u} = \frac{1}{2} x \ln x + \gamma x + O(\sqrt{x})$$
Subtracting the fractional error:
$$\sum_{u=1}^K \left\lfloor \frac{x}{u} \right\rfloor = \frac{1}{2} x \ln x + \gamma x + O(\sqrt{x})$$

Now multiply by $2$:
$$2 \sum_{u=1}^K \left\lfloor \frac{x}{u} \right\rfloor = x \ln x + 2\gamma x + O(\sqrt{x})$$

Finally, evaluate the subtracted square $K^2$:
$$K = \sqrt{x} + O(1) \implies K^2 = (\sqrt{x} + O(1))^2 = x + O(\sqrt{x})$$
Subtracting $K^2$:
$$D(x) = [x \ln x + 2\gamma x + O(\sqrt{x})] - [x + O(\sqrt{x})] = x \ln x + (2\gamma - 1)x + O(\sqrt{x}) \quad \blacksquare$$

This complete proof confirms Dirichlet's landmark result!"""
            }
        ]
    }
    return u6

if __name__ == "__main__":
    u = get_unit6()
    print(f"Loaded Unit 6: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
