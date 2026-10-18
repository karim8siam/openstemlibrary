# -*- coding: utf-8 -*-
"""
build_nt_unit5.py
Constructs Unit 5: Arithmetical Functions & Dirichlet Convolution
"""

def get_unit5():
    u5 = {
        "number": 5,
        "title": "Arithmetical Functions & Dirichlet Convolution",
        "leadSummary": "Structural theory of arithmetical functions: multiplicative and completely multiplicative functions, divisor functions $\\tau(n)$ and $\\sigma(n)$, the Euclid-Euler Theorem completely characterizing even perfect numbers, Fermat numbers $F_n = 2^{2^n} + 1$ and Pepin's test, and the algebraic ring of arithmetical functions endowed with the Dirichlet convolution product $(f * g)(n) = \\sum_{d \\mid n} f(d) g(n/d)$ and Dirichlet inverses.",
        "simulations": ["sim_nt_arithmetic_functions_sigma"],
        "sections": [
            {
                "secNumber": "5.1",
                "title": "Multiplicative Functions & Divisor Sum Transforms",
                "content": r"""### 1. Definition of Arithmetical Functions

> **Definition 5.1 (Arithmetical Function):**
> An **arithmetical function** (or number-theoretic function) is any complex-valued function defined on the set of positive integers:
> $$f: \mathbb{N} \to \mathbb{C}$$

---

### 2. Multiplicative and Completely Multiplicative Functions

> **Definition 5.2 (Multiplicativity):**
> An arithmetical function $f$ is called:
> 1. **Multiplicative** if $f$ is not identically zero and:
>    $$f(m n) = f(m) f(n) \quad \text{whenever } \gcd(m, n) = 1$$
> 2. **Completely Multiplicative** (or strongly multiplicative) if:
>    $$f(m n) = f(m) f(n) \quad \text{for all } m, n \in \mathbb{N}$$

> **Theorem 5.1 (Canonical Evaluation of Multiplicative Functions):**
> If $f$ is multiplicative:
> 1. $f(1) = 1$.
> 2. For any positive integer with prime factorization $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$:
>    $$f(n) = f(p_1^{a_1}) f(p_2^{a_2}) \cdots f(p_k^{a_k}) = \prod_{i=1}^k f(p_i^{a_i})$$
> Thus, any multiplicative function is completely determined by its values on prime powers!

---

### 3. Divisor Sum Transforms

> **Theorem 5.2 (Preservation of Multiplicativity under Divisor Sums):**
> If $f$ is a multiplicative function, then its **summatory function** (divisor sum transform):
> $$F(n) = \sum_{d \mid n} f(d)$$
> is also a multiplicative function.

> **Proof:**
> Let $m, n \in \mathbb{N}$ with $\gcd(m, n) = 1$.
> Any divisor $d$ of $m n$ can be uniquely factored as $d = d_1 d_2$ where $d_1 \mid m$, $d_2 \mid n$, and $\gcd(d_1, d_2) = 1$.
> Therefore:
> $$F(m n) = \sum_{d \mid m n} f(d) = \sum_{d_1 \mid m} \sum_{d_2 \mid n} f(d_1 d_2)$$
> Since $f$ is multiplicative and $\gcd(d_1, d_2) = 1$:
> $$f(d_1 d_2) = f(d_1) f(d_2)$$
> Substituting this in:
> $$F(m n) = \sum_{d_1 \mid m} \sum_{d_2 \mid n} f(d_1) f(d_2) = \left( \sum_{d_1 \mid m} f(d_1) \right) \left( \sum_{d_2 \mid n} f(d_2) \right) = F(m) F(n)$$
> Hence, $F$ is multiplicative. $\blacksquare$"""
            },
            {
                "secNumber": "5.2",
                "title": "The Divisor Functions tau(n) and sigma(n)",
                "content": r"""### 1. The Number of Divisors $\tau(n)$ and Sum of Divisors $\sigma(n)$

> **Definition 5.3 (Divisor Functions):**
> For any real or complex number $\alpha$, the **generalized divisor function** $\sigma_\alpha(n)$ is:
> $$\sigma_\alpha(n) = \sum_{d \mid n} d^\alpha$$
> Two special cases are of paramount importance:
> 1. **Divisor count function ($\alpha = 0$):**
>    $$\tau(n) = d(n) = \sigma_0(n) = \sum_{d \mid n} 1 = \text{number of positive divisors of } n$$
> 2. **Divisor sum function ($\alpha = 1$):**
>    $$\sigma(n) = \sigma_1(n) = \sum_{d \mid n} d = \text{sum of positive divisors of } n$$

---

### 2. Multiplicativity and Prime-Power Formulas

Both constant function $u(n) = 1$ and identity function $N(n) = n$ are completely multiplicative.
By Theorem 5.2, $\tau(n) = \sum_{d \mid n} 1$ and $\sigma(n) = \sum_{d \mid n} d$ are **multiplicative functions**.

> **Theorem 5.3 (Formulas for $\tau(n)$ and $\sigma(n)$):**
> For a prime power $p^a$ ($a \ge 1$):
> 1. Divisors of $p^a$ are $\{1, p, p^2, \dots, p^a\}$:
>    $$\tau(p^a) = a + 1$$
> 2. Sum of divisors is a finite geometric series:
>    $$\sigma(p^a) = 1 + p + p^2 + \dots + p^a = \frac{p^{a+1} - 1}{p - 1}$$
> For any integer $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$:
> $$\tau(n) = \prod_{i=1}^k (a_i + 1)$$
> $$\sigma(n) = \prod_{i=1}^k \frac{p_i^{a_i + 1} - 1}{p_i - 1}$$

*Example:* For $n = 12 = 2^2 \times 3^1$:
$$\tau(12) = (2 + 1)(1 + 1) = 3 \times 2 = 6 \quad (\text{divisors: } 1, 2, 3, 4, 6, 12)$$
$$\sigma(12) = \frac{2^3 - 1}{2 - 1} \times \frac{3^2 - 1}{3 - 1} = 7 \times 4 = 28$$"""
            },
            {
                "secNumber": "5.3",
                "title": "Perfect Numbers, Mersenne Primes & The Euclid-Euler Theorem",
                "content": r"""### 1. Perfect Numbers

The study of perfect numbers dates back to the Pythagoreans (c. 500 BCE).

> **Definition 5.4 (Perfect Number):**
> A positive integer $n$ is called a **perfect number** if the sum of its proper positive divisors equals $n$:
> $$\sum_{\substack{d \mid n \\ d < n}} d = n \iff \sigma(n) = 2 n$$
> - If $\sigma(n) < 2n$, $n$ is called **deficient**.
> - If $\sigma(n) > 2n$, $n$ is called **abundant**.
> The first four perfect numbers known since antiquity are:
> $$6, \quad 28, \quad 496, \quad 8128$$

---

### 2. Mersenne Primes

> **Definition 5.5 (Mersenne Number and Prime):**
> A number of the form:
> $$M_p = 2^p - 1$$
> is called a **Mersenne number**. If $M_p$ is prime, it is called a **Mersenne prime**.

> **Lemma 5.1 (Exponent Divisibility):**
> If $2^m - 1$ is a prime number, then $m$ must itself be a prime number.

> **Proof:**
> Suppose $m$ is composite: $m = a b$ with $1 < a, b < m$.
> Then $2^m - 1 = 2^{ab} - 1 = (2^a)^b - 1$.
> Factoring as a difference of $b$-th powers:
> $$2^{ab} - 1 = (2^a - 1)(2^{a(b-1)} + 2^{a(b-2)} + \dots + 2^a + 1)$$
> Since $a > 1$, $2^a - 1 > 1$. Since $b > 1$, the second factor is $> 1$.
> Thus $2^m - 1$ is composite, contradicting primality! Hence, $m$ is prime. $\blacksquare$

---

### 3. The Euclid-Euler Theorem

> **Theorem 5.4 (Euclid-Euler Theorem):**
> An even positive integer $n$ is a perfect number if and only if it has the form:
> $$n = 2^{p-1}(2^p - 1)$$
> where $2^p - 1$ is a Mersenne prime.

*Open Problem in Number Theory:* Whether any **odd** perfect numbers exist remains one of the oldest unsolved problems in mathematics."""
            },
            {
                "secNumber": "5.4",
                "title": "Fermat Numbers, Pairwise Coprimality & Pepin's Test",
                "content": r"""### 1. Fermat Numbers

In 1640, Pierre de Fermat conjectured that all numbers of the form $2^{2^n} + 1$ are prime.

> **Definition 5.6 (Fermat Number):**
> The $n$-th **Fermat number** ($n \ge 0$) is defined by:
> $$F_n = 2^{2^n} + 1$$
> The first five Fermat numbers are prime:
> $$F_0 = 3, \quad F_1 = 5, \quad F_2 = 17, \quad F_3 = 257, \quad F_4 = 65537$$
> In 1732, Euler shattered Fermat's conjecture by showing that $F_5$ is composite:
> $$F_5 = 2^{32} + 1 = 4294967297 = 641 \times 6700417$$
> To this day, no other Fermat primes beyond $F_4$ have ever been found!

---

### 2. Pairwise Coprimality and the Infinitude of Primes

> **Theorem 5.5 (Fundamental Fermat Recurrence):**
> For all $n \ge 1$:
> $$F_n - 2 = \prod_{k=0}^{n-1} F_k$$

> **Proof (by Mathematical Induction on $n$):**
> For $n = 1$: $F_1 - 2 = 5 - 2 = 3 = F_0$.
> Assume the identity holds for $n$: $\prod_{k=0}^{n-1} F_k = F_n - 2$.
> Multiply both sides by $F_n$:
> $$\prod_{k=0}^n F_k = (F_n - 2) F_n = (2^{2^n} - 1)(2^{2^n} + 1) = (2^{2^n})^2 - 1 = 2^{2^{n+1}} - 1 = F_{n+1} - 2$$
> This completes the induction. $\blacksquare$

> **Theorem 5.6 (Pairwise Coprimality of Fermat Numbers):**
> For any distinct non-negative integers $m \ne n$:
> $$\gcd(F_m, F_n) = 1$$

> **Proof:**
> Without loss of generality, let $m < n$.
> By Theorem 5.5, $F_m$ divides $\prod_{k=0}^{n-1} F_k = F_n - 2$.
> Let $d = \gcd(F_m, F_n)$.
> Then $d \mid F_m \implies d \mid (F_n - 2)$.
> Also $d \mid F_n$.
> By linearity of divisibility, $d \mid [F_n - (F_n - 2)] = 2$.
> Since all Fermat numbers $F_k = 2^{2^k} + 1$ are odd, $d$ cannot be divisible by $2$.
> Therefore, $d = 1$. $\blacksquare$

> **Pólya's Proof of Infinitely Many Primes:**
> Since the infinite sequence $F_0, F_1, F_2, \dots$ consists of pairwise coprime integers, and each $F_n$ has at least one prime divisor, there must be at least as many primes as there are Fermat numbers: infinitely many!

---

### 3. Pepin's Primality Test for Fermat Numbers

> **Theorem 5.7 (Pépin's Test, 1877):**
> For $n \ge 1$, the Fermat number $F_n$ is prime if and only if:
> $$3^{(F_n - 1)/2} \equiv -1 \pmod{F_n}$$"""
            },
            {
                "secNumber": "5.5",
                "title": "The Dirichlet Convolution Product & Algebraic Ring of Arithmetic Functions",
                "content": r"""### 1. Definition of Dirichlet Convolution

> **Definition 5.7 (Dirichlet Convolution):**
> Let $f, g: \mathbb{N} \to \mathbb{C}$ be two arithmetical functions.
> The **Dirichlet convolution** (or Dirichlet product) of $f$ and $g$, denoted $f * g$, is the arithmetical function defined by:
> $$(f * g)(n) = \sum_{d \mid n} f(d) g\left(\frac{n}{d}\right) = \sum_{a b = n} f(a) g(b)$$

---

### 2. Algebraic Properties of the Dirichlet Ring

> **Theorem 5.8 (Algebraic Structure):**
> Let $\mathcal{A}$ denote the set of all arithmetical functions $f: \mathbb{N} \to \mathbb{C}$.
> Then $(\mathcal{A}, +, *)$ forms a **commutative ring with identity**:
> 1. **Commutativity:** $f * g = g * f$.
> 2. **Associativity:** $(f * g) * h = f * (g * h)$.
> 3. **Distributivity:** $f * (g + h) = (f * g) + (f * h)$.
> 4. **Identity Element:** The function $\epsilon(n)$ defined by:
>    $$\epsilon(n) = \begin{cases} 1 & \text{if } n = 1 \\ 0 & \text{if } n > 1 \end{cases}$$
>    serves as the multiplicative identity:
>    $$f * \epsilon = \epsilon * f = f \quad \forall f \in \mathcal{A}$$

---

### 3. Dirichlet Inverses

> **Theorem 5.9 (Existence and Uniqueness of Dirichlet Inverses):**
> An arithmetical function $f$ possesses a **Dirichlet inverse** $f^{-1}$ (satisfying $f * f^{-1} = \epsilon$) if and only if:
> $$f(1) \ne 0$$
> If $f(1) \ne 0$, the inverse $f^{-1}$ is unique and can be computed recursively by:
> $$f^{-1}(1) = \frac{1}{f(1)}$$
> $$f^{-1}(n) = -\frac{1}{f(1)} \sum_{\substack{d \mid n \\ d > 1}} f(d) f^{-1}\left(\frac{n}{d}\right) \quad (n > 1)$$

> **Theorem 5.10 (Preservation of Multiplicativity):**
> If $f$ and $g$ are multiplicative, then their Dirichlet convolution $f * g$ is also **multiplicative**.
> Furthermore, if $f$ is multiplicative, then its Dirichlet inverse $f^{-1}$ is also **multiplicative**."""
            }
        ],
        "problems": [
            {
                "id": "nt-prob-5-1",
                "tier": "Foundational",
                "title": "Computation of Divisor Functions tau(n) and sigma(n)",
                "statement": r"""Consider the integer $n = 3600$:
1. Determine the canonical prime factorization of $3600$.
2. Compute the number of positive divisors $\tau(3600)$ using the multiplicative formula.
3. Compute the sum of all positive divisors $\sigma(3600)$.
4. Determine whether $3600$ is deficient, abundant, or perfect.""",
                "hints": [
                    "Factor 3600 = 36 * 100 = 6^2 * 10^2 = 2^4 * 3^2 * 5^2.",
                    "Use tau(n) = (a_1 + 1)(a_2 + 1)(a_3 + 1).",
                    "Use sigma(n) = product (p^{a+1} - 1)/(p - 1)."
                ],
                "solution": r"""### 1. Canonical Factorization
Factor $3600$:
$$3600 = 36 \times 100 = (4 \times 9) \times (4 \times 25) = (2^2 \times 3^2) \times (2^2 \times 5^2)$$
Collecting powers of identical primes:
$$3600 = 2^4 \times 3^2 \times 5^2 \quad \blacksquare$$

---

### 2. Number of Divisors $\tau(3600)$
By Theorem 5.3:
$$\tau(3600) = (4 + 1)(2 + 1)(2 + 1) = 5 \times 3 \times 3 = 45$$
Thus, $3600$ has exactly **45 positive divisors**. $\blacksquare$

---

### 3. Sum of Divisors $\sigma(3600)$
By Theorem 5.3:
$$\sigma(3600) = \left( \frac{2^{4+1} - 1}{2 - 1} \right) \left( \frac{3^{2+1} - 1}{3 - 1} \right) \left( \frac{5^{2+1} - 1}{5 - 1} \right)$$
Evaluate each geometric factor:
- For $p = 2$: $\frac{2^5 - 1}{1} = \frac{32 - 1}{1} = 31$
- For $p = 3$: $\frac{3^3 - 1}{2} = \frac{27 - 1}{2} = \frac{26}{2} = 13$
- For $p = 5$: $\frac{5^3 - 1}{4} = \frac{125 - 1}{4} = \frac{124}{4} = 31$
Multiplying these together:
$$\sigma(3600) = 31 \times 13 \times 31 = 31^2 \times 13 = 961 \times 13 = 12493 \quad \blacksquare$$

---

### 4. Classification
Compare $\sigma(n)$ with $2n$:
$$2 n = 2 \times 3600 = 7200$$
Since $\sigma(3600) = 12493 > 7200$:
$$3600 \text{ is an } \textbf{abundant number}! \quad \blacksquare$$"""
            },
            {
                "id": "nt-prob-5-2",
                "tier": "Advanced",
                "title": "Mersenne Primes & Generation of the First Four Perfect Numbers",
                "statement": r"""1. Prove that if $2^p - 1$ is prime, then the exponent $p$ must be a prime number.
2. Verify that $M_p = 2^p - 1$ is prime for $p \in \{2, 3, 5, 7\}$.
3. Compute the four even perfect numbers $n = 2^{p-1}(2^p - 1)$ generated by these Mersenne primes and verify $\sigma(n) = 2n$ for the first two.""",
                "hints": [
                    "If p = a * b with a, b > 1, factor 2^{ab} - 1 using difference of b-th powers.",
                    "Compute M_2 = 3, M_3 = 7, M_5 = 31, M_7 = 127.",
                    "Verify sigma(6) = 12 and sigma(28) = 56."
                ],
                "solution": r"""### 1. Proof that $2^p - 1 \text{ Prime} \implies p \text{ Prime}$
Suppose $p$ is composite: $p = a b$ with $1 < a < p$ and $1 < b < p$.
Then:
$$2^p - 1 = 2^{a b} - 1 = (2^a)^b - 1$$
Using the algebraic polynomial identity $x^b - 1 = (x - 1)(x^{b-1} + x^{b-2} + \dots + x + 1)$ with $x = 2^a$:
$$2^p - 1 = (2^a - 1)(2^{a(b-1)} + 2^{a(b-2)} + \dots + 2^a + 1)$$
Since $a > 1$, $2^a - 1 \ge 2^2 - 1 = 3 > 1$.
Since $b > 1$, the second factor has at least two positive terms, so it is $> 1$.
Thus, $2^p - 1$ has two non-trivial factors $> 1$, meaning it is composite.
This contradicts the assumption that $2^p - 1$ is prime.
Therefore, the exponent $p$ must be prime! $\blacksquare$

---

### 2. Verification of Mersenne Primes
- For $p = 2$: $M_2 = 2^2 - 1 = 3$ (prime)
- For $p = 3$: $M_3 = 2^3 - 1 = 7$ (prime)
- For $p = 5$: $M_5 = 2^5 - 1 = 31$ (prime)
- For $p = 7$: $M_7 = 2^7 - 1 = 127$ (prime) $\blacksquare$

---

### 3. Generating the First Four Perfect Numbers
Applying Euclid's formula $n = 2^{p-1}(2^p - 1)$:
1. For $p = 2$:
   $$n_1 = 2^{2-1}(2^2 - 1) = 2^1 \times 3 = 6$$
   Verification: $\sigma(6) = 1 + 2 + 3 + 6 = 12 = 2(6) \quad \checkmark$
2. For $p = 3$:
   $$n_2 = 2^{3-1}(2^3 - 1) = 2^2 \times 7 = 4 \times 7 = 28$$
   Verification: $\sigma(28) = 1 + 2 + 4 + 7 + 14 + 28 = 56 = 2(28) \quad \checkmark$
3. For $p = 5$:
   $$n_3 = 2^{5-1}(2^5 - 1) = 2^4 \times 31 = 16 \times 31 = 496$$
4. For $p = 7$:
   $$n_4 = 2^{7-1}(2^7 - 1) = 2^6 \times 127 = 64 \times 127 = 8128 \quad \blacksquare$$"""
            },
            {
                "id": "nt-prob-5-3",
                "tier": "Honors / Proof Challenge",
                "title": "Complete Rigorous Proof of the Euclid-Euler Theorem",
                "statement": r"""Let $n$ be an even positive integer.
1. Prove Euclid's half: If $n = 2^{p-1}(2^p - 1)$ where $2^p - 1$ is prime, then $\sigma(n) = 2n$, so $n$ is perfect.
2. Prove Euler's converse half: If $n$ is any even perfect number, it must have the form $n = 2^{p-1}(2^p - 1)$ where $2^p - 1$ is a Mersenne prime.""",
                "hints": [
                    "For Euclid's part, use the multiplicativity of sigma and gcd(2^{p-1}, 2^p - 1) = 1.",
                    "For Euler's part, write n = 2^{k-1} m with m odd and k >= 2. Compute sigma(n) = sigma(2^{k-1}) sigma(m).",
                    "Set sigma(n) = 2n = 2^k m and deduce that m has only two divisors: 1 and m."
                ],
                "solution": r"""### 1. Euclid's Direction: $n = 2^{p-1}(2^p - 1)$ is Perfect
Suppose $n = 2^{p-1}(2^p - 1)$ where $q = 2^p - 1$ is a prime.
Notice that $q = 2^p - 1$ is odd, while $2^{p-1}$ is a power of $2$, so:
$$\gcd(2^{p-1}, q) = 1$$
Because $\sigma$ is a multiplicative function (Theorem 5.2):
$$\sigma(n) = \sigma(2^{p-1} q) = \sigma(2^{p-1}) \sigma(q)$$
Compute each factor:
- Since $2^{p-1}$ is a prime power:
  $$\sigma(2^{p-1}) = \frac{2^{(p-1)+1} - 1}{2 - 1} = 2^p - 1 = q$$
- Since $q$ is prime, its only divisors are $1$ and $q$:
  $$\sigma(q) = 1 + q = 1 + (2^p - 1) = 2^p$$
Multiplying the two factors:
$$\sigma(n) = q \times 2^p = (2^p - 1) \times 2^p = 2 \times [2^{p-1}(2^p - 1)] = 2 n$$
Thus, $\sigma(n) = 2n$, proving that $n$ is a perfect number! $\blacksquare$

---

### 2. Euler's Converse Direction: All Even Perfect Numbers Have This Form
Let $n$ be an **even** perfect number.
Since $n$ is even, we can factor out the highest power of $2$:
$$n = 2^{k-1} m$$
where $k \ge 2$ and $m$ is an **odd** integer.
Since $\gcd(2^{k-1}, m) = 1$ and $\sigma$ is multiplicative:
$$\sigma(n) = \sigma(2^{k-1}) \sigma(m) = (2^k - 1) \sigma(m)$$
Because $n$ is perfect, $\sigma(n) = 2n$:
$$(2^k - 1) \sigma(m) = 2(2^{k-1} m) = 2^k m$$
From this equality:
$$\sigma(m) = \frac{2^k m}{2^k - 1} = \frac{(2^k - 1 + 1) m}{2^k - 1} = m + \frac{m}{2^k - 1}$$
Since $\sigma(m)$ is an integer, the fraction $\frac{m}{2^k - 1}$ must be an integer.
Let:
$$c = \frac{m}{2^k - 1} \implies m = c(2^k - 1)$$
Then:
$$\sigma(m) = m + c$$
Notice that $c = \frac{m}{2^k - 1}$ is a divisor of $m$.
Also, $m$ is always a divisor of $m$.
Since $k \ge 2$, $2^k - 1 \ge 3 > 1$, so $c < m$.
Therefore, $m$ and $c$ are two distinct positive divisors of $m$.
Consequently, the sum of all divisors of $m$ must satisfy:
$$\sigma(m) \ge m + c$$
However, we derived above that $\sigma(m) = m + c$ exactly!
This equality means that $m$ and $c$ are the **only** positive divisors of $m$!
Since $1$ is always a divisor of any positive integer, we must have:
$$c = 1$$
Thus:
$$\sigma(m) = m + 1$$
An integer whose only divisors are $1$ and itself is, by definition, a **prime number**!
Therefore, $m$ is prime, and:
$$m = c(2^k - 1) = 1(2^k - 1) = 2^k - 1$$
By Lemma 5.1, since $m = 2^k - 1$ is prime, the exponent $k$ must be a prime, say $k = p$.
Substituting $m = 2^p - 1$ back into $n = 2^{k-1} m$:
$$n = 2^{p-1}(2^p - 1)$$
where $2^p - 1$ is a Mersenne prime.
This establishes Euler's theorem completely. $\blacksquare$"""
            }
        ]
    }
    return u5

if __name__ == "__main__":
    u = get_unit5()
    print(f"Loaded Unit 5: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
