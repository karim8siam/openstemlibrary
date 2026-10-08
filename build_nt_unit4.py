# -*- coding: utf-8 -*-
"""
build_nt_unit4.py
Constructs Unit 4: Classical Theorems: Fermat, Euler, Wilson & Primitive Roots
"""

def get_unit4():
    u4 = {
        "number": 4,
        "title": "Classical Theorems: Fermat, Euler, Wilson & Primitive Roots",
        "leadSummary": "Landmark classical theorems of modular arithmetic: Fermat's Little Theorem, pseudoprimes and Carmichael numbers, Euler's totient function $\\phi(n)$ and Euler's Totient Theorem, Wilson's Theorem characterizing prime numbers, the multiplicative order of an integer modulo $m$, Gauss's Primitive Root Theorem characterizing moduli with cyclic unit groups ($2, 4, p^k, 2p^k$), and the theory of indices (discrete logarithms).",
        "simulations": ["sim_nt_primitive_roots_indices"],
        "sections": [
            {
                "secNumber": "4.1",
                "title": "Fermat's Little Theorem, Pseudoprimes & Primality Testing",
                "content": r"""### 1. Statement and Proof of Fermat's Little Theorem

Pierre de Fermat stated this celebrated theorem in 1640, with the first published proof provided by Leonhard Euler in 1736.

> **Theorem 4.1 (Fermat's Little Theorem):**
> Let $p$ be a prime number.
> 1. If $a \in \mathbb{Z}$ is not divisible by $p$ ($\gcd(a, p) = 1$), then:
>    $$a^{p-1} \equiv 1 \pmod p$$
> 2. For any integer $a \in \mathbb{Z}$:
>    $$a^p \equiv a \pmod p$$

> **Proof:**
> Consider the set of multiples of $a$ by the first $p - 1$ positive integers:
> $$S = \{a, 2a, 3a, \dots, (p-1)a\}$$
> We make two critical observations:
> 1. **No element is divisible by $p$:** For any $1 \le k \le p - 1$, $p \nmid k$ and $p \nmid a$, so by Euclid's Lemma, $p \nmid ka$.
> 2. **All elements are pairwise incongruent modulo $p$:**
>    If $j a \equiv k a \pmod p$ with $1 \le j \le k \le p - 1$, then $p \mid (k - j)a$.
>    Since $\gcd(a, p) = 1$, by Euclid's Lemma $p \mid (k - j)$.
>    Since $0 \le k - j < p$, this forces $k - j = 0 \implies j = k$.
> Therefore, the residues of the elements of $S$ modulo $p$ must be a permutation of the set $\{1, 2, 3, \dots, p - 1\}$.
> Multiplying all $p - 1$ congruences together:
> $$a \cdot (2a) \cdot (3a) \cdots ((p-1)a) \equiv 1 \cdot 2 \cdot 3 \cdots (p-1) \pmod p$$
> Factoring out $a$ on the left-hand side:
> $$a^{p-1} (p - 1)! \equiv (p - 1)! \pmod p$$
> Since $p$ is prime, none of the integers $1, 2, \dots, p - 1$ share any common factor with $p$, so $\gcd((p - 1)!, p) = 1$.
> By the cancellation law (Theorem 3.3), we divide both sides by $(p - 1)!$:
> $$a^{p-1} \equiv 1 \pmod p \quad \blacksquare$$

---

### 2. Pseudoprimes and Carmichael Numbers

The converse of Fermat's Little Theorem is false: if $a^{n-1} \equiv 1 \pmod n$, $n$ is not necessarily prime!

> **Definition 4.1 (Fermat Pseudoprime):**
> A composite integer $n$ is called a **Fermat pseudoprime to base $a$** if:
> $$a^{n-1} \equiv 1 \pmod n$$
> *Example:* $341 = 11 \times 31$ is composite, but $2^{340} \equiv 1 \pmod{341}$. Thus $341$ is a pseudoprime to base $2$.

> **Definition 4.2 (Carmichael Number / Absolute Pseudoprime):**
> A composite integer $n$ is called a **Carmichael number** if $a^{n-1} \equiv 1 \pmod n$ for **all** integers $a$ with $\gcd(a, n) = 1$.

> **Theorem 4.2 (Korselt's Criterion, 1899):**
> A positive composite integer $n$ is a Carmichael number if and only if $n$ is square-free and for every prime divisor $p \mid n$:
> $$(p - 1) \mid (n - 1)$$
> The smallest Carmichael number is $561 = 3 \times 11 \times 17$ ($2 \mid 560, 10 \mid 560, 16 \mid 560$)."""
            },
            {
                "secNumber": "4.2",
                "title": "Euler's Totient Function phi(n) & Euler's Generalization",
                "content": r"""### 1. Euler's Totient Function $\phi(n)$

Leonhard Euler generalized Fermat's theorem in 1760 to arbitrary composite moduli $m$ by introducing the totient function $\phi(n)$.

> **Definition 4.3 (Euler's Totient Function):**
> For $n \in \mathbb{N}$, $\phi(n)$ denotes the number of integers in $\{1, 2, \dots, n\}$ that are coprime to $n$:
> $$\phi(n) = \sum_{\substack{k=1 \\ \gcd(k, n) = 1}}^n 1$$

> **Theorem 4.3 (Values of $\phi$ on Prime Powers):**
> 1. For a prime $p$: $\phi(p) = p - 1$.
> 2. For a prime power $p^k$ ($k \ge 1$):
>    $$\phi(p^k) = p^k - p^{k-1} = p^k \left(1 - \frac{1}{p}\right)$$

> **Proof:**
> The positive integers $\le p^k$ that are NOT coprime to $p^k$ are precisely the multiples of $p$:
> $$p, 2p, 3p, \dots, p^{k-1} p = p^k$$
> There are exactly $p^{k-1}$ such multiples.
> Subtracting these from the total $p^k$ elements:
> $$\phi(p^k) = p^k - p^{k-1} = p^k \left(1 - \frac{1}{p}\right) \quad \blacksquare$$

---

### 2. Multiplicativity of Euler's Function

> **Theorem 4.4 (Multiplicativity of $\phi$):**
> If $\gcd(m, n) = 1$, then:
> $$\phi(m n) = \phi(m) \phi(n)$$
> Consequently, for any integer $n = \prod_{i=1}^r p_i^{a_i}$:
> $$\phi(n) = n \prod_{p \mid n} \left(1 - \frac{1}{p}\right) = \prod_{i=1}^r p_i^{a_i - 1}(p_i - 1)$$

---

### 3. Euler's Totient Theorem

> **Theorem 4.5 (Euler's Totient Theorem, 1760):**
> If $a, m \in \mathbb{Z}$ with $m \ge 1$ and $\gcd(a, m) = 1$, then:
> $$a^{\phi(m)} \equiv 1 \pmod m$$

> **Proof:**
> Let $\{r_1, r_2, \dots, r_{\phi(m)}\}$ be a reduced residue system modulo $m$.
> Since $\gcd(a, m) = 1$, the set $\{a r_1, a r_2, \dots, a r_{\phi(m)}\}$ is also a reduced residue system modulo $m$ (Theorem 3.4).
> Therefore, their products modulo $m$ must be congruent:
> $$(a r_1)(a r_2) \cdots (a r_{\phi(m)}) \equiv r_1 r_2 \cdots r_{\phi(m)} \pmod m$$
> Factoring out $a$:
> $$a^{\phi(m)} \prod_{i=1}^{\phi(m)} r_i \equiv \prod_{i=1}^{\phi(m)} r_i \pmod m$$
> Since each $r_i$ is coprime to $m$, their product $P = \prod r_i$ is coprime to $m$.
> Dividing both sides by $P$ via Theorem 3.3 yields:
> $$a^{\phi(m)} \equiv 1 \pmod m \quad \blacksquare$$"""
            },
            {
                "secNumber": "4.3",
                "title": "Wilson's Theorem & Exact Prime Characterization",
                "content": r"""### 1. Statement and Proof of Wilson's Theorem

John Wilson stated this property in 1770, with the first rigorous proof published by Joseph-Louis Lagrange in 1771.

> **Theorem 4.6 (Wilson's Theorem):**
> An integer $p > 1$ is a prime number if and only if:
> $$(p - 1)! \equiv -1 \pmod p$$

> **Proof ($\implies$ Forward Direction):**
> Suppose $p$ is prime.
> - For $p = 2$: $(2 - 1)! = 1! = 1 \equiv -1 \pmod 2$ (since $1 \equiv -1 \equiv 1 \pmod 2$).
> - For $p = 3$: $(3 - 1)! = 2! = 2 \equiv -1 \pmod 3$.
> Now assume $p \ge 5$ is an odd prime.
> Consider the set of integers $S = \{1, 2, 3, \dots, p - 1\}$.
> For each $a \in S$, $\gcd(a, p) = 1$, so by Corollary 3.1 there exists a unique modular inverse $a' \in S$ such that:
> $$a a' \equiv 1 \pmod p$$
> Which elements in $S$ are their own modular inverses ($a = a'$)?
> $$a^2 \equiv 1 \pmod p \iff a^2 - 1 \equiv 0 \pmod p \iff (a - 1)(a + 1) \equiv 0 \pmod p$$
> By Euclid's Lemma, $p \mid (a - 1)$ or $p \mid (a + 1)$.
> Since $1 \le a \le p - 1$:
> - $a \equiv 1 \pmod p \implies a = 1$.
> - $a \equiv -1 \pmod p \implies a = p - 1$.
> Thus, $1$ and $p - 1$ are the **only** self-inverse elements in $S$!
> The remaining $p - 3$ elements $\{2, 3, \dots, p - 2\}$ can be grouped into $(p - 3)/2$ disjoint pairs $\{a, a'\}$ with $a \ne a'$ such that $a a' \equiv 1 \pmod p$.
> Multiplying all elements of $S$:
> $$(p - 1)! = 1 \cdot \left[ \prod_{\{a, a'\}} (a a') \right] \cdot (p - 1) \equiv 1 \cdot [1 \cdot 1 \cdots 1] \cdot (p - 1) \equiv p - 1 \equiv -1 \pmod p \quad \blacksquare$$

> **Proof ($\impliedby$ Reverse Direction):**
> Suppose $(n - 1)! \equiv -1 \pmod n$ for some $n > 1$.
> We must show that $n$ is prime.
> Suppose for contradiction that $n$ is composite.
> Then $n$ has a proper divisor $d$ such that $1 < d < n$.
> Since $1 < d \le n - 1$, $d$ appears as one of the factors in the product:
> $$(n - 1)! = 1 \cdot 2 \cdots d \cdots (n - 1) \implies d \mid (n - 1)!$$
> By assumption, $n \mid ((n - 1)! + 1)$.
> Since $d \mid n$, by transitivity $d \mid ((n - 1)! + 1)$.
> Since $d \mid (n - 1)!$ and $d \mid ((n - 1)! + 1)$, by linearity:
> $$d \mid [((n - 1)! + 1) - (n - 1)!] = 1$$
> But $d > 1$, which is impossible!
> Thus, $n$ must be prime. $\blacksquare$"""
            },
            {
                "secNumber": "4.4",
                "title": "The Order of an Integer Modulo m & Multiplicative Cyclic Structure",
                "content": r"""### 1. Definition of Order

By Euler's Totient Theorem, if $\gcd(a, m) = 1$, then $a^{\phi(m)} \equiv 1 \pmod m$.
Therefore, the set of positive integers $k$ such that $a^k \equiv 1 \pmod m$ is non-empty.
By the Well-Ordering Principle, this set contains a smallest element.

> **Definition 4.4 (Order of an Integer Modulo $m$):**
> Let $a, m \in \mathbb{Z}$ with $m \ge 1$ and $\gcd(a, m) = 1$.
> The **order** of $a$ modulo $m$, denoted $\operatorname{ord}_m(a)$, is the smallest positive integer $d \in \mathbb{N}$ such that:
> $$a^d \equiv 1 \pmod m$$

---

### 2. Fundamental Properties of Order

> **Theorem 4.7 (Division Property of Order):**
> Let $\gcd(a, m) = 1$ and $d = \operatorname{ord}_m(a)$.
> 1. $a^k \equiv 1 \pmod m$ if and only if $d \mid k$.
> 2. In particular, $d \mid \phi(m)$.
> 3. $a^i \equiv a^j \pmod m$ if and only if $i \equiv j \pmod d$.
> 4. The powers $a^0, a^1, a^2, \dots, a^{d-1}$ are pairwise incongruent modulo $m$.

> **Proof:**
> To prove Part 1:
> Suppose $a^k \equiv 1 \pmod m$. By the Division Algorithm, divide $k$ by $d$:
> $$k = q d + r \quad \text{with } 0 \le r < d$$
> Then:
> $$1 \equiv a^k = a^{q d + r} = (a^d)^q \cdot a^r \equiv (1)^q \cdot a^r \equiv a^r \pmod m$$
> Thus $a^r \equiv 1 \pmod m$.
> If $r > 0$, this contradicts the minimality of $d = \operatorname{ord}_m(a)$ (since $r < d$).
> Therefore, $r = 0$, which proves $d \mid k$.
> Conversely, if $d \mid k$, then $k = d c$, so $a^k = (a^d)^c \equiv 1^c \equiv 1 \pmod m$.
> Part 2 follows immediately by applying Part 1 to $k = \phi(m)$. $\blacksquare$

> **Theorem 4.8 (Order of Powers):**
> If $\operatorname{ord}_m(a) = d$, then for any positive integer $k \ge 1$:
> $$\operatorname{ord}_m(a^k) = \frac{d}{\gcd(k, d)}$$
> In particular, $\operatorname{ord}_m(a^k) = d$ if and only if $\gcd(k, d) = 1$."""
            },
            {
                "secNumber": "4.5",
                "title": "Primitive Roots, Gauss's Moduli Theorem & Theory of Indices",
                "content": r"""### 1. Primitive Roots Modulo $m$

> **Definition 4.5 (Primitive Root):**
> An integer $g$ is called a **primitive root modulo $m$** if:
> $$\operatorname{ord}_m(g) = \phi(m)$$
> Equivalently, $g$ is a primitive root if its powers $\{g^1, g^2, \dots, g^{\phi(m)}\}$ generate the entire reduced residue system modulo $m$ (so that the unit group $(\mathbb{Z}/m\mathbb{Z})^\times$ is cyclic).

---

### 2. Gauss's Primitive Root Characterization

Not every modulus possesses primitive roots!

> **Theorem 4.9 (Gauss's Moduli Theorem):**
> A positive integer $m \ge 2$ possesses a primitive root if and only if:
> $$m \in \{2, 4, p^k, 2p^k\}$$
> where $p$ is an **odd prime** and $k \ge 1$.
> Moduli with two or more distinct odd prime factors or divisible by $8$ have non-cyclic unit groups and **no primitive roots**.

> **Theorem 4.10 (Number of Primitive Roots):**
> If a modulus $m$ possesses a primitive root, then the total number of mutually incongruent primitive roots modulo $m$ is exactly:
> $$\phi(\phi(m))$$

---

### 3. Theory of Indices (Discrete Logarithms)

Let $g$ be a fixed primitive root modulo $m$.
Every integer $a$ coprime to $m$ is congruent to exactly one power $g^k$ with $0 \le k < \phi(m)$.

> **Definition 4.6 (Index / Discrete Logarithm):**
> The exponent $k \in \{0, 1, \dots, \phi(m) - 1\}$ such that $g^k \equiv a \pmod m$ is called the **index** (or **discrete logarithm**) of $a$ to base $g$ modulo $m$, written:
> $$\operatorname{ind}_g(a) \equiv k \pmod{\phi(m)}$$

> **Theorem 4.11 (Arithmetic Properties of Indices):**
> 1. $\operatorname{ind}_g(a b) \equiv \operatorname{ind}_g(a) + \operatorname{ind}_g(b) \pmod{\phi(m)}$
> 2. $\operatorname{ind}_g(a^k) \equiv k \cdot \operatorname{ind}_g(a) \pmod{\phi(m)}$
> 3. $\operatorname{ind}_g(1) \equiv 0 \pmod{\phi(m)}$ and $\operatorname{ind}_g(g) \equiv 1 \pmod{\phi(m)}$

Indices transform exponential congruences $x^k \equiv a \pmod m$ into simple linear congruences:
$$k \cdot \operatorname{ind}_g(x) \equiv \operatorname{ind}_g(a) \pmod{\phi(m)}$$"""
            }
        ],
        "problems": [
            {
                "id": "nt-prob-4-1",
                "tier": "Foundational",
                "title": "Application of Euler's Totient Theorem to Terminal Digits",
                "statement": r"""Find the last two digits of the large power:
$$7^{2026}$$
1. Formulate the problem as a modular arithmetic congruence modulo $100$.
2. Compute Euler's totient function $\phi(100)$.
3. Apply Euler's Totient Theorem to reduce the exponent and determine the exact terminal two digits.""",
                "hints": [
                    "The last two digits of a positive integer N are given by N mod 100.",
                    "Compute phi(100) = phi(4 * 25) = 100 * (1 - 1/2) * (1 - 1/5).",
                    "Reduce the exponent 2026 modulo phi(100) = 40."
                ],
                "solution": r"""### 1. Modular Formulation
The last two decimal digits of $7^{2026}$ are given by the remainder when divided by $100$:
$$x \equiv 7^{2026} \pmod{100} \quad (0 \le x < 100) \quad \blacksquare$$

---

### 2. Computation of Euler's Totient $\phi(100)$
The prime factorization of $100$ is:
$$100 = 2^2 \times 5^2$$
Using the product formula for Euler's totient function:
$$\phi(100) = 100 \left(1 - \frac{1}{2}\right)\left(1 - \frac{1}{5}\right) = 100 \times \frac{1}{2} \times \frac{4}{5} = 100 \times \frac{4}{10} = 40 \quad \blacksquare$$

---

### 3. Exponent Reduction via Euler's Theorem
Notice that $\gcd(7, 100) = 1$.
By Euler's Totient Theorem (Theorem 4.5):
$$7^{\phi(100)} = 7^{40} \equiv 1 \pmod{100}$$
Now divide the exponent $2026$ by $40$:
$$2026 = 50 \times 40 + 26 \implies 2026 \equiv 26 \pmod{40}$$
Therefore:
$$7^{2026} = 7^{50 \times 40 + 26} = (7^{40})^{50} \times 7^{26} \equiv 1^{50} \times 7^{26} \equiv 7^{26} \pmod{100}$$

Now compute $7^{26} \pmod{100}$ by successive modular squaring:
- $7^2 = 49$
- $7^4 = (49)^2 = 2401 \equiv 1 \pmod{100}$ (since $2401 = 24 \times 100 + 1$!)
This makes the computation remarkably simple:
$$7^4 \equiv 1 \pmod{100}$$
Divide the exponent $26$ by $4$:
$$26 = 6 \times 4 + 2$$
Therefore:
$$7^{26} = (7^4)^6 \times 7^2 \equiv (1)^6 \times 49 \equiv 49 \pmod{100}$$
Thus, the last two digits of $7^{2026}$ are **49**. $\blacksquare$"""
            },
            {
                "id": "nt-prob-4-2",
                "tier": "Advanced",
                "title": "Korselt's Criterion & Carmichael Number Verification for n = 561",
                "statement": r"""Consider the integer $n = 561$:
1. Find the complete prime factorization of $561$ and verify that $n$ is square-free.
2. State Korselt's criterion for a composite number to be a Carmichael number.
3. Prove that for every prime divisor $p \mid 561$, $(p - 1) \mid (561 - 1)$.
4. Deduce using Fermat's Little Theorem and the Chinese Remainder Theorem that $a^{560} \equiv 1 \pmod{561}$ for all integers $a$ with $\gcd(a, 561) = 1$.""",
                "hints": [
                    "Check 561 = 3 * 11 * 17.",
                    "Verify 2 | 560, 10 | 560, and 16 | 560.",
                    "Show a^{560} = 1 mod 3, mod 11, and mod 17, then apply CRT."
                ],
                "solution": r"""### 1. Factorization and Square-Free Verification
Divide $561$ by successive primes:
- $561 / 3 = 187$
- $187 / 11 = 17$
Thus:
$$561 = 3 \times 11 \times 17$$
Since all prime factors $3, 11, 17$ have exponent $1$, $561$ is **square-free**. $\blacksquare$

---

### 2. Korselt's Criterion
A composite integer $n$ is a Carmichael number if and only if:
1. $n$ is square-free, and
2. For every prime factor $p$ dividing $n$, $(p - 1) \mid (n - 1)$. $\blacksquare$

---

### 3. Verification of Korselt's Divisibility Conditions
Here $n - 1 = 561 - 1 = 560$.
We test each prime divisor $p \in \{3, 11, 17\}$:
1. For $p = 3$: $p - 1 = 2$.
   $$560 = 2 \times 280 \implies 2 \mid 560 \quad \checkmark$$
2. For $p = 11$: $p - 1 = 10$.
   $$560 = 10 \times 56 \implies 10 \mid 560 \quad \checkmark$$
3. For $p = 17$: $p - 1 = 16$.
   $$560 = 16 \times 35 \implies 16 \mid 560 \quad \checkmark$$
All three conditions are satisfied! $\blacksquare$

---

### 4. Deduction of the Carmichael Property
Let $a \in \mathbb{Z}$ with $\gcd(a, 561) = 1$.
Then $\gcd(a, 3) = 1, \gcd(a, 11) = 1,$ and $\gcd(a, 17) = 1$.
By Fermat's Little Theorem (Theorem 4.1):
1. Modulo $3$: $a^2 \equiv 1 \pmod 3 \implies a^{560} = (a^2)^{280} \equiv 1^{280} \equiv 1 \pmod 3$.
2. Modulo $11$: $a^{10} \equiv 1 \pmod{11} \implies a^{560} = (a^{10})^{56} \equiv 1^{56} \equiv 1 \pmod{11}$.
3. Modulo $17$: $a^{16} \equiv 1 \pmod{17} \implies a^{560} = (a^{16})^{35} \equiv 1^{35} \equiv 1 \pmod{17}$.

Thus:
$$a^{560} - 1 \text{ is divisible by } 3, 11, \text{ and } 17$$
Since $3, 11, 17$ are pairwise coprime primes, their product $3 \times 11 \times 17 = 561$ must divide $a^{560} - 1$:
$$a^{560} \equiv 1 \pmod{561}$$
This holds for **every** $a$ coprime to $561$, confirming that $561$ is indeed an absolute Fermat pseudoprime (Carmichael number)! $\blacksquare$"""
            },
            {
                "id": "nt-prob-4-3",
                "tier": "Honors / Proof Challenge",
                "title": "Rigorous Proof of the Existence of Primitive Roots Modulo Odd Primes",
                "statement": r"""Let $p$ be an odd prime.
1. Prove that for any divisor $d$ of $p - 1$, the polynomial congruence $x^d - 1 \equiv 0 \pmod p$ has **exactly $d$ solutions** modulo $p$.
2. Prove that the number of elements in $(\mathbb{Z}/p\mathbb{Z})^\times$ having order $d$ is either $0$ or $\phi(d)$.
3. Use the divisor sum identity $\sum_{d \mid (p - 1)} \phi(d) = p - 1$ to prove that for every divisor $d \mid (p - 1)$, there exist **exactly $\phi(d)$** elements of order $d$.
4. Conclude that $(\mathbb{Z}/p\mathbb{Z})^\times$ has exactly $\phi(p - 1) > 0$ primitive roots, proving that the unit group modulo any prime is cyclic.""",
                "hints": [
                    "Factor x^{p-1} - 1 = (x^d - 1) g(x) where g(x) has degree p-1-d.",
                    "Apply Lagrange's theorem on polynomial roots.",
                    "If an element of order d exists, say a, its powers a^k have order d / gcd(k, d)."
                ],
                "solution": r"""### 1. Exactly $d$ Roots of $x^d - 1 \equiv 0 \pmod p$
Let $d \mid (p - 1)$, so $p - 1 = d k$.
Algebraically factor $x^{p-1} - 1 = (x^d)^k - 1$:
$$x^{p-1} - 1 = (x^d - 1)(x^{d(k-1)} + x^{d(k-2)} + \dots + x^d + 1) = (x^d - 1) g(x)$$
where $g(x) \in \mathbb{Z}[x]$ has degree $p - 1 - d$.
By Fermat's Little Theorem, every $a \in \{1, 2, \dots, p - 1\}$ satisfies:
$$a^{p-1} - 1 \equiv 0 \pmod p$$
Thus, $x^{p-1} - 1 \equiv 0 \pmod p$ has exactly $p - 1$ distinct roots modulo $p$.
By Lagrange's Theorem (Theorem 3.8):
- $g(x) \equiv 0 \pmod p$ has at most $\deg g = p - 1 - d$ roots.
- $x^d - 1 \equiv 0 \pmod p$ has at most $d$ roots.
Since every root of $x^{p-1} - 1$ must satisfy $x^d - 1 \equiv 0$ or $g(x) \equiv 0$, the sum of their root counts must be at least $p - 1$:
$$\text{roots}(x^d - 1) \ge (p - 1) - \text{roots}(g(x)) \ge (p - 1) - (p - 1 - d) = d$$
Combining this with Lagrange's upper bound $\text{roots}(x^d - 1) \le d$:
$$\text{roots}(x^d - 1 \pmod p) = d \quad \blacksquare$$

---

### 2. Elements of Order $d$
Let $\psi(d)$ denote the number of elements in $\{1, 2, \dots, p - 1\}$ having order $d$.
If $\psi(d) = 0$, the claim holds.
Suppose $\psi(d) > 0$. Then there exists at least one element $a$ with $\operatorname{ord}_p(a) = d$.
Then the $d$ powers:
$$a, a^2, a^3, \dots, a^d \equiv 1 \pmod p$$
are pairwise incongruent modulo $p$ (Theorem 4.7), and each satisfies $(a^k)^d = (a^d)^k \equiv 1^k \equiv 1 \pmod p$.
By Part 1, $x^d - 1 \equiv 0 \pmod p$ has exactly $d$ roots.
Therefore, these $d$ powers $\{a, a^2, \dots, a^d\}$ constitute the **entire** set of roots of $x^d - 1 \equiv 0 \pmod p$!
Any element of order $d$ must satisfy $x^d \equiv 1 \pmod p$, hence must be in this set.
By Theorem 4.8:
$$\operatorname{ord}_p(a^k) = \frac{d}{\gcd(k, d)} = d \iff \gcd(k, d) = 1$$
The number of exponents $k \in \{1, 2, \dots, d\}$ with $\gcd(k, d) = 1$ is precisely $\phi(d)$.
Thus, if $\psi(d) > 0$, then $\psi(d) = \phi(d)$. $\blacksquare$

---

### 3. Exhaustion via Divisor Sum
Every element in $\{1, 2, \dots, p - 1\}$ has an order that divides $\phi(p) = p - 1$.
Partitioning the $p - 1$ elements by their order:
$$\sum_{d \mid (p - 1)} \psi(d) = p - 1$$
Recall Gauss's divisor sum identity for Euler's totient function (Unit 6, Theorem 6.2):
$$\sum_{d \mid (p - 1)} \phi(d) = p - 1$$
Subtracting the two equations:
$$\sum_{d \mid (p - 1)} [\phi(d) - \psi(d)] = 0$$
From Part 2, we know that for each $d \mid (p - 1)$, either $\psi(d) = 0$ (so $\phi(d) - \psi(d) = \phi(d) > 0$) or $\psi(d) = \phi(d)$ (so $\phi(d) - \psi(d) = 0$).
Thus, each term in the sum is non-negative:
$$\phi(d) - \psi(d) \ge 0 \quad \forall d \mid (p - 1)$$
A sum of non-negative integers can be zero if and only if **every** term is zero:
$$\phi(d) - \psi(d) = 0 \implies \psi(d) = \phi(d) \quad \forall d \mid (p - 1) \quad \blacksquare$$

---

### 4. Conclusion
Setting $d = p - 1$:
The number of elements of order $p - 1 = \phi(p)$ is:
$$\psi(p - 1) = \phi(p - 1) > 0$$
Since $\phi(p - 1) \ge 1$ for all primes $p \ge 2$, there exists at least one primitive root $g$ modulo $p$.
The powers $\{g, g^2, \dots, g^{p-1}\}$ generate all of $(\mathbb{Z}/p\mathbb{Z})^\times$, proving that the unit group is **cyclic**! $\blacksquare$"""
            }
        ]
    }
    return u4

if __name__ == "__main__":
    u = get_unit4()
    print(f"Loaded Unit 4: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
