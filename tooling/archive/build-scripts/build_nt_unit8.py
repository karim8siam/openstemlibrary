# -*- coding: utf-8 -*-
"""
build_nt_unit8.py
Constructs Unit 8: Representation of Integers as Sums of Squares
"""

def get_unit8():
    u8 = {
        "number": 8,
        "title": "Representation of Integers as Sums of Squares",
        "leadSummary": "Additive number theory and the geometry of numbers: Fermat's Christmas Theorem on sums of two squares, the arithmetic and prime factorization of Gaussian integers $\\mathbb{Z}[i]$, the complete characterization of two-square integers and the divisor excess formula $r_2(n) = 4(d_1(n) - d_3(n))$, Euler's four-square identity and Hamilton quaternions $\\mathbb{H}$, Lagrange's Four-Square Theorem via minimal descent, and Legendre's Three-Square criterion $n \\ne 4^a(8b + 7)$.",
        "simulations": ["sim_nt_sums_of_squares_lagrange"],
        "sections": [
            {
                "secNumber": "8.1",
                "title": "Sums of Two Squares: Fermat's Christmas Theorem",
                "content": r"""### 1. The Two-Square Problem

The problem of representing integers as sums of two squares traces back to Diophantus of Alexandria, but the first definitive modern breakthrough was announced by Pierre de Fermat in a famous letter to Father Marin Mersenne dated December 25, 1640 (hence the name **Fermat's Christmas Theorem**).

> **Fundamental Question:**
> Which positive integers $n \in \mathbb{N}$ can be represented as the sum of two integer squares:
> $$n = x^2 + y^2, \qquad x, y \in \mathbb{Z}?$$

Before resolving the general question, we examine the behavior of prime numbers.

---

### 2. Parity and Quadratic Residue Obstruction

> **Lemma 8.1 (Modulo 4 Obstruction):**
> Let $x \in \mathbb{Z}$. Then:
> $$x^2 \equiv \begin{cases} 0 \pmod 4 & \text{if } x \text{ is even} \\ 1 \pmod 4 & \text{if } x \text{ is odd} \end{cases}$$
> Consequently, for any $x, y \in \mathbb{Z}$:
> $$x^2 + y^2 \equiv 0, 1, \text{ or } 2 \pmod 4$$
> In particular, no integer $n \equiv 3 \pmod 4$ can ever be represented as the sum of two squares.

> **Proof:**
> If $x = 2k$, $x^2 = 4k^2 \equiv 0 \pmod 4$. If $x = 2k+1$, $x^2 = 4(k^2 + k) + 1 \equiv 1 \pmod 4$.
> Taking all four combinations of $x^2, y^2 \in \{0, 1\} \pmod 4$:
> - $0 + 0 = 0 \pmod 4$
> - $0 + 1 = 1 \pmod 4$
> - $1 + 0 = 1 \pmod 4$
> - $1 + 1 = 2 \pmod 4$
> The residue $3 \pmod 4$ is completely unattainable. $\blacksquare$

For prime numbers $p$:
- If $p = 2$: $2 = 1^2 + 1^2$ is a sum of two squares.
- If $p$ is an odd prime and $p = x^2 + y^2$, then since $p$ is odd, one of $x, y$ is even and the other is odd, so $p \equiv 0 + 1 = 1 \pmod 4$.

Thus, a necessary condition for an odd prime $p$ to be a sum of two squares is:
$$p \equiv 1 \pmod 4$$

---

### 3. Fermat's Two-Square Theorem

Fermat claimed, and Leonhard Euler proved in 1749 (after 7 years of effort), that this necessary condition is also sufficient!

> **Theorem 8.1 (Fermat's Christmas Theorem):**
> An odd prime number $p$ can be expressed as the sum of two integer squares:
> $$p = x^2 + y^2, \qquad x, y \in \mathbb{Z}$$
> if and only if:
> $$p \equiv 1 \pmod 4$$
> Furthermore, this representation is **unique** up to the order of the summands and signs of $x$ and $y$.

---

### 4. Quadratic Residues: The Root of $-1$ Modulo $p$

The central algebraic lever underlying all proofs of Fermat's theorem is the existence of an integer whose square is congruent to $-1$ modulo $p$.

> **Lemma 8.2 (Square Root of $-1$):**
> Let $p$ be an odd prime. The congruence:
> $$z^2 \equiv -1 \pmod p$$
> has an integer solution $z \in \mathbb{Z}$ if and only if $p \equiv 1 \pmod 4$.
> An explicit solution is given by:
> $$z \equiv \left(\frac{p-1}{2}\right)! \pmod p$$

> **Proof:**
> By Euler's Criterion for quadratic residues:
> $$\left(\frac{-1}{p}\right) \equiv (-1)^{\frac{p-1}{2}} \pmod p$$
> - If $p \equiv 1 \pmod 4$, then $\frac{p-1}{2} = 2k$ is even, so $(-1)^{\frac{p-1}{2}} = 1$. Hence $-1$ is a quadratic residue modulo $p$.
> - If $p \equiv 3 \pmod 4$, then $\frac{p-1}{2} = 2k+1$ is odd, so $(-1)^{\frac{p-1}{2}} = -1$. Hence $-1$ is a quadratic non-residue modulo $p$.
>
> To obtain the explicit formula, by Wilson's Theorem $(p-1)! \equiv -1 \pmod p$.
> Grouping the product $(p-1)! = 1 \cdot 2 \cdots \left(\frac{p-1}{2}\right) \cdot \left(\frac{p+1}{2}\right) \cdots (p-1)$:
> Notice that for $1 \le j \le \frac{p-1}{2}$:
> $$p - j \equiv -j \pmod p$$
> Thus:
> $$(p-1)! = \prod_{j=1}^{(p-1)/2} j \cdot \prod_{j=1}^{(p-1)/2} (p - j) \equiv \left(\prod_{j=1}^{(p-1)/2} j\right) \cdot \left(\prod_{j=1}^{(p-1)/2} (-j)\right) = (-1)^{\frac{p-1}{2}} \left[ \left(\frac{p-1}{2}\right)! \right]^2 \pmod p$$
> For $p \equiv 1 \pmod 4$, $(-1)^{(p-1)/2} = 1$, giving:
> $$-1 \equiv \left[ \left(\frac{p-1}{2}\right)! \right]^2 \pmod p$$
> Letting $z = \left(\frac{p-1}{2}\right)!$, we have $z^2 \equiv -1 \pmod p$. $\blacksquare$

---

### 5. Thue's Lemma: The Pigeonhole Bridge to Squares

In 1902, Axel Thue gave an ingenious proof using the Dirichlet Pigeonhole Principle that bridges modular congruences to Diophantine equations.

> **Lemma 8.3 (Thue's Lemma):**
> Let $n > 1$ and let $a \in \mathbb{Z}$ with $\gcd(a, n) = 1$.
> Then there exist integers $x, y$ such that:
> $$a x \equiv y \pmod n, \qquad 0 < |x| < \sqrt{n}, \quad 0 < |y| < \sqrt{n}$$

> **Proof:**
> Let $k = \lfloor \sqrt{n} \rfloor$. Then $k < \sqrt{n} < k+1$, which means $(k+1)^2 > n$.
> Consider the set of pairs:
> $$S = \{(u, v) \in \mathbb{Z}^2 : 0 \le u \le k, \; 0 \le v \le k\}$$
> The total number of pairs in $S$ is $|S| = (k+1)^2 > n$.
> To each pair $(u, v) \in S$, associate the residue:
> $$f(u, v) = a u - v \pmod n$$
> Since there are $(k+1)^2 > n$ pairs and only $n$ possible residues modulo $n$, by the **Pigeonhole Principle**, there exist two distinct pairs $(u_1, v_1) \ne (u_2, v_2) \in S$ such that:
> $$a u_1 - v_1 \equiv a u_2 - v_2 \pmod n \implies a(u_1 - u_2) \equiv v_1 - v_2 \pmod n$$
> Set $x = u_1 - u_2$ and $y = v_1 - v_2$.
> - Since $(u_1, v_1) \ne (u_2, v_2)$, $(x, y) \ne (0, 0)$.
> - Since $0 \le u_1, u_2 \le k$, we have $-k \le x \le k$, so $|x| \le k < \sqrt{n}$.
> - Similarly, $|y| \le k < \sqrt{n}$.
> - If $x = 0$, then $y \equiv a(0) = 0 \pmod n$, and since $|y| < \sqrt{n} < n$, this forces $y = 0$, contradicting $(x, y) \ne (0, 0)$. Thus $x \ne 0$.
> - Similarly, if $y = 0$, then $a x \equiv 0 \pmod n \implies n \mid x$ (since $\gcd(a, n) = 1$), which contradicts $0 < |x| < n$. Thus $y \ne 0$.
>
> Hence $0 < |x| < \sqrt{n}$ and $0 < |y| < \sqrt{n}$. $\blacksquare$

---

### 6. Rigorous Proof of Fermat's Theorem via Thue's Lemma

> **Proof of Theorem 8.1:**
> Let $p$ be a prime with $p \equiv 1 \pmod 4$.
> By Lemma 8.2, there exists $z \in \mathbb{Z}$ such that $z^2 \equiv -1 \pmod p$.
> Applying Thue's Lemma (Lemma 8.3) with $n = p$ and $a = z$:
> There exist integers $x, y$ such that:
> $$z x \equiv y \pmod p, \qquad 0 < |x| < \sqrt{p}, \quad 0 < |y| < \sqrt{p}$$
> Squaring both sides of the congruence:
> $$z^2 x^2 \equiv y^2 \pmod p$$
> Substituting $z^2 \equiv -1 \pmod p$:
> $$-x^2 \equiv y^2 \pmod p \implies x^2 + y^2 \equiv 0 \pmod p$$
> Thus, $p \mid (x^2 + y^2)$.
>
> Now evaluate the size of $x^2 + y^2$:
> Since $0 < |x| < \sqrt{p}$ and $0 < |y| < \sqrt{p}$:
> $$x^2 < p \quad \text{and} \quad y^2 < p \implies 0 < x^2 + y^2 < 2p$$
> Since $x^2 + y^2$ is a positive integer multiple of $p$ strictly between $0$ and $2p$, the only possible multiple is $1 \cdot p$!
> $$x^2 + y^2 = p$$
> This completes the existence proof. $\blacksquare$"""
            },
            {
                "secNumber": "8.2",
                "title": "Gaussian Integers $\\mathbb{Z}[i]$, Norms & Prime Factorization",
                "content": r"""### 1. The Ring of Gaussian Integers

A profound algebraic perspective on sums of two squares was opened by Carl Friedrich Gauss in 1828–1832 with the introduction of **Gaussian integers**.

> **Definition 8.1 (Gaussian Integers):**
> The ring of Gaussian integers, denoted $\mathbb{Z}[i]$, is the subring of the complex numbers $\mathbb{C}$ defined by:
> $$\mathbb{Z}[i] = \{a + b i : a, b \in \mathbb{Z}\}, \qquad i^2 = -1$$
> Addition and multiplication follow the standard field operations of $\mathbb{C}$:
> $$(a + b i) + (c + d i) = (a + c) + (b + d) i$$
> $$(a + b i)(c + d i) = (a c - b d) + (a d + b c) i$$

Geometrically, $\mathbb{Z}[i]$ is the square lattice of points with integer coordinates in the complex plane $\mathbb{C} \cong \mathbb{R}^2$.

---

### 2. The Field Norm

> **Definition 8.2 (Field Norm):**
> For $\alpha = a + b i \in \mathbb{Z}[i]$, the **norm** $N(\alpha)$ is the squared modulus:
> $$N(\alpha) = |\alpha|^2 = \alpha \bar{\alpha} = (a + b i)(a - b i) = a^2 + b^2$$
> where $\bar{\alpha} = a - b i$ is the complex conjugate.

> **Proposition 8.1 (Properties of the Norm):**
> 1. **Non-negativity:** $N(\alpha) \ge 0$ for all $\alpha \in \mathbb{Z}[i]$, with $N(\alpha) = 0 \iff \alpha = 0$.
> 2. **Multiplicativity:** For all $\alpha, \beta \in \mathbb{Z}[i]$:
>    $$N(\alpha \beta) = N(\alpha) N(\beta)$$
> 3. **Integer Values:** $N(\alpha) \in \mathbb{Z}_{\ge 0}$.

> **Proof of Multiplicativity:**
> $$N(\alpha \beta) = (\alpha \beta) \overline{(\alpha \beta)} = (\alpha \beta)(\bar{\alpha} \bar{\beta}) = (\alpha \bar{\alpha})(\beta \bar{\beta}) = N(\alpha) N(\beta) \quad \blacksquare$$

---

### 3. Units in $\mathbb{Z}[i]$

> **Proposition 8.2 (Units):**
> An element $u \in \mathbb{Z}[i]$ is invertible (a **unit**) if and only if $N(u) = 1$.
> The group of units $\mathbb{Z}[i]^\times$ is cyclic of order $4$:
> $$\mathbb{Z}[i]^\times = \{1, -1, i, -i\}$$

> **Proof:**
> If $u$ is a unit, there exists $v \in \mathbb{Z}[i]$ such that $u v = 1$.
> Taking norms: $N(u) N(v) = N(1) = 1$.
> Since $N(u), N(v) \in \mathbb{Z}_{\ge 0}$, we must have $N(u) = 1$.
> Conversely, if $u = a + b i$ and $N(u) = a^2 + b^2 = 1$, then since $a, b \in \mathbb{Z}$:
> Either $a = \pm 1, b = 0$ (giving $\pm 1$) or $a = 0, b = \pm 1$ (giving $\pm i$).
> In all four cases, $u$ has an inverse in $\mathbb{Z}[i]$. $\blacksquare$

---

### 4. Euclidean Division Algorithm in $\mathbb{Z}[i]$

The ring $\mathbb{Z}[i]$ shares the fundamental Euclidean division property with $\mathbb{Z}$.

> **Theorem 8.2 (Division Algorithm for Gaussian Integers):**
> Given $\alpha, \beta \in \mathbb{Z}[i]$ with $\beta \ne 0$, there exist $q, r \in \mathbb{Z}[i]$ such that:
> $$\alpha = \beta q + r \qquad \text{with} \quad N(r) \le \frac{1}{2} N(\beta) < N(\beta)$$

> **Proof:**
> Consider the quotient in the field of fractions $\mathbb{Q}(i) \subset \mathbb{C}$:
> $$\frac{\alpha}{\beta} = x + y i, \qquad x, y \in \mathbb{Q}$$
> Choose integers $u, v \in \mathbb{Z}$ that are closest to the rational numbers $x, y$:
> $$|x - u| \le \frac{1}{2}, \qquad |y - v| \le \frac{1}{2}$$
> Set $q = u + v i \in \mathbb{Z}[i]$ and define the remainder $r = \alpha - \beta q \in \mathbb{Z}[i]$.
> Then:
> $$\frac{r}{\beta} = \frac{\alpha}{\beta} - q = (x - u) + (y - v) i$$
> Taking the norm of both sides:
> $$\frac{N(r)}{N(\beta)} = (x - u)^2 + (y - v)^2 \le \left(\frac{1}{2}\right)^2 + \left(\frac{1}{2}\right)^2 = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}$$
> Multiplying through by $N(\beta) > 0$:
> $$N(r) \le \frac{1}{2} N(\beta) < N(\beta) \quad \blacksquare$$

> **Corollary 8.1 (UFD Property):**
> Because $\mathbb{Z}[i]$ is a Euclidean Domain (ED), it is a Principal Ideal Domain (PID), and therefore a **Unique Factorization Domain (UFD)**.
> Every nonzero, non-unit Gaussian integer factors uniquely into a product of irreducible Gaussian primes, up to multiplication by units $\{\pm 1, \pm i\}$.

---

### 5. Classification of Gaussian Primes

Which elements in $\mathbb{Z}[i]$ are prime?
A rational prime $p \in \mathbb{Z}$ behaves in one of three ways inside $\mathbb{Z}[i]$:

> **Theorem 8.3 (Classification of Gaussian Primes):**
> Up to unit associates, the primes of $\mathbb{Z}[i]$ are precisely:
> 1. **Ramified Prime:**
>    $$2 = -i(1 + i)^2$$
>    The element $1 + i$ is a Gaussian prime of norm $N(1 + i) = 1^2 + 1^2 = 2$.
> 2. **Inert Primes:**
>    Every rational prime $q \equiv 3 \pmod 4$ remains prime (inert) in $\mathbb{Z}[i]$, with norm $N(q) = q^2$.
> 3. **Split Primes:**
>    Every rational prime $p \equiv 1 \pmod 4$ splits into two non-associate conjugate Gaussian primes:
>    $$p = \pi \bar{\pi} = (a + b i)(a - b i)$$
>    where $N(\pi) = N(\bar{\pi}) = a^2 + b^2 = p$.

> **Direct Proof of Split Behavior:**
> Let $p$ be a prime with $p \equiv 1 \pmod 4$.
> As proved in Lemma 8.2, there exists $z \in \mathbb{Z}$ such that $z^2 \equiv -1 \pmod p$.
> This means $p \mid (z^2 + 1)$ in $\mathbb{Z}$.
> In $\mathbb{Z}[i]$, we can factor:
> $$z^2 + 1 = (z + i)(z - i)$$
> Thus $p \mid (z + i)(z - i)$ in $\mathbb{Z}[i]$.
>
> Now, suppose for a contradiction that $p$ were prime (irreducible) in $\mathbb{Z}[i]$.
> By Euclid's Lemma in the UFD $\mathbb{Z}[i]$, $p$ must divide either $z + i$ or $z - i$.
> But if $p \mid (z + i)$, then there exists $c + d i \in \mathbb{Z}[i]$ such that:
> $$z + i = p(c + d i) = p c + p d i \implies p d = 1$$
> Since $p \ge 5$ and $d \in \mathbb{Z}$, $p d = 1$ has no integer solution!
> Hence $p$ does NOT divide $z + i$, and by the same argument $p \nmid (z - i)$.
>
> Therefore, $p$ is **not prime** in $\mathbb{Z}[i]$!
> Since $p$ is reducible and not a unit, it factors as:
> $$p = \pi \beta$$
> where $\pi, \beta \in \mathbb{Z}[i]$ are neither units.
> Taking norms:
> $$p^2 = N(p) = N(\pi) N(\beta)$$
> Since $\pi, \beta$ are not units, $N(\pi) > 1$ and $N(\beta) > 1$.
> Since $p$ is a rational prime, the only integer factorization of $p^2$ into factors $> 1$ is:
> $$N(\pi) = p \quad \text{and} \quad N(\beta) = p$$
> Writing $\pi = a + b i$, we immediately obtain:
> $$a^2 + b^2 = N(\pi) = p$$
> This gives an exceptionally beautiful, purely ring-theoretic proof of Fermat's Christmas Theorem! $\blacksquare$"""
            },
            {
                "secNumber": "8.3",
                "title": "General Two-Square Characterization & Counting Representations",
                "content": r"""### 1. The Brahmagupta-Fibonacci Identity

How do sums of two squares behave under multiplication?

> **Identity 8.1 (Brahmagupta-Fibonacci Identity):**
> For any real or complex numbers $a, b, c, d$:
> $$(a^2 + b^2)(c^2 + d^2) = (a c - b d)^2 + (a d + b c)^2$$
> $$= (a c + b d)^2 + (a d - b c)^2$$

> **Proof:**
> In the Gaussian integers, let $\alpha = a + b i$ and $\beta = c + d i$.
> The multiplicativity of the norm states:
> $$N(\alpha) N(\beta) = N(\alpha \beta)$$
> Expanding both sides:
> $$N(\alpha) = a^2 + b^2, \qquad N(\beta) = c^2 + d^2$$
> $$\alpha \beta = (a c - b d) + (a d + b c) i \implies N(\alpha \beta) = (a c - b d)^2 + (a d + b c)^2$$
> The second variant follows by replacing $\beta$ with $\bar{\beta} = c - d i$, since $N(\bar{\beta}) = N(\beta)$. $\blacksquare$

The identity proves that the set of integers representable as sums of two squares is **closed under multiplication**.

---

### 2. Complete Classification of Two-Square Integers

> **Theorem 8.4 (Two-Square Characterization):**
> A positive integer $n \in \mathbb{N}$ can be expressed as the sum of two squares:
> $$n = x^2 + y^2, \qquad x, y \in \mathbb{Z}$$
> if and only if in the canonical prime factorization of $n$:
> $$n = 2^{a_0} \prod_{p_j \equiv 1 \,(4)} p_j^{a_j} \prod_{q_k \equiv 3 \,(4)} q_k^{b_k}$$
> every prime factor $q_k \equiv 3 \pmod 4$ appears with an **even exponent** (i.e., $b_k \equiv 0 \pmod 2$ for all $k$).

> **Proof:**
> **Sufficiency ($\Leftarrow$):**
> Suppose each $b_k = 2 c_k$. Then:
> $$n = 2^{a_0} \left( \prod p_j^{a_j} \right) \cdot \left( \prod q_k^{c_k} \right)^2$$
> - $2 = 1^2 + 1^2$ is a sum of two squares.
> - Each prime $p_j \equiv 1 \pmod 4$ is a sum of two squares by Fermat's Theorem (Theorem 8.1).
> - By Identity 8.1, the product of sums of two squares is again a sum of two squares.
>   Thus $2^{a_0} \prod p_j^{a_j} = u^2 + v^2$.
> - Multiplying by the perfect square $M^2 = \left( \prod q_k^{c_k} \right)^2$:
>   $$n = (u^2 + v^2) M^2 = (u M)^2 + (v M)^2$$
> which is a sum of two squares.
>
> **Necessity ($\Rightarrow$):**
> Suppose $n = x^2 + y^2$. Let $q$ be any prime divisor of $n$ with $q \equiv 3 \pmod 4$.
> We must prove that the exact power of $q$ dividing $n$, denoted $v_q(n)$, is even.
>
> Let $g = \gcd(x, y)$, and write $x = g x_1, y = g y_1$ with $\gcd(x_1, y_1) = 1$.
> Then:
> $$n = g^2 (x_1^2 + y_1^2)$$
> Suppose for contradiction that $q \mid (x_1^2 + y_1^2)$.
> Then $x_1^2 + y_1^2 \equiv 0 \pmod q \implies x_1^2 \equiv -y_1^2 \pmod q$.
> If $q \mid y_1$, then $q \mid x_1^2 \implies q \mid x_1$, contradicting $\gcd(x_1, y_1) = 1$.
> Thus $q \nmid y_1$, so $y_1$ has a modular inverse $y_1^{-1}$ modulo $q$.
> Multiplying by $(y_1^{-1})^2$:
> $$(x_1 y_1^{-1})^2 \equiv -1 \pmod q$$
> This implies that $-1$ is a quadratic residue modulo $q$, so $\left(\frac{-1}{q}\right) = 1$.
> But by Lemma 8.2, for $q \equiv 3 \pmod 4$:
> $$\left(\frac{-1}{q}\right) = (-1)^{\frac{q-1}{2}} = -1$$
> This contradiction proves that $q \nmid (x_1^2 + y_1^2)$!
> Therefore, all factors of $q$ in $n$ must come from $g^2$:
> $$v_q(n) = v_q(g^2) = 2 v_q(g) \equiv 0 \pmod 2$$
> Hence, every prime factor $q \equiv 3 \pmod 4$ appears with an even exponent. $\blacksquare$

---

### 3. Number of Representations: Jacobi's Two-Square Formula

How many integer pairs $(x, y) \in \mathbb{Z}^2$ satisfy $x^2 + y^2 = n$?

> **Definition 8.3 (Representation Function $r_2(n)$):**
> $$r_2(n) = \#\{(x, y) \in \mathbb{Z}^2 : x^2 + y^2 = n\}$$
> Note that order matters ($(x, y) \ne (y, x)$ if $x \ne y$) and signs matter ($(\pm x, \pm y)$).

> **Theorem 8.5 (Jacobi's Two-Square Formula):**
> Let $d_1(n)$ denote the number of divisors of $n$ congruent to $1 \pmod 4$, and $d_3(n)$ denote the number of divisors congruent to $3 \pmod 4$:
> $$d_1(n) = \sum_{\substack{d \mid n \\ d \equiv 1 \,(4)}} 1, \qquad d_3(n) = \sum_{\substack{d \mid n \\ d \equiv 3 \,(4)}} 1$$
> Then:
> $$r_2(n) = 4 \left( d_1(n) - d_3(n) \right) = 4 \sum_{d \mid n} \chi_4(d)$$
> where $\chi_4$ is the non-principal Dirichlet character modulo 4:
> $$\chi_4(d) = \begin{cases} 0 & \text{if } d \text{ is even} \\ 1 & \text{if } d \equiv 1 \pmod 4 \\ -1 & \text{if } d \equiv 3 \pmod 4 \end{cases}$$

> **Proof:**
> Finding pairs $(x, y) \in \mathbb{Z}^2$ with $x^2 + y^2 = n$ is identical to finding Gaussian integers $\alpha = x + i y \in \mathbb{Z}[i]$ with $N(\alpha) = n$.
> Factor $n$ in $\mathbb{Z}$:
> $$n = 2^{a_0} \prod_{j=1}^r p_j^{a_j} \prod_{k=1}^s q_k^{b_k}$$
> In $\mathbb{Z}[i]$:
> - $2 = -i (1 + i)^2$, with $N(1 + i) = 2$.
> - Each $p_j = \pi_j \bar{\pi}_j$, with $N(\pi_j) = N(\bar{\pi}_j) = p_j$.
> - Each $q_k$ is inert, with $N(q_k) = q_k^2$.
>
> Any Gaussian integer $\alpha$ with $N(\alpha) = n$ must have prime factorization:
> $$\alpha = u (1 + i)^{a_0} \left( \prod_{j=1}^r \pi_j^{c_j} \bar{\pi}_j^{a_j - c_j} \right) \left( \prod_{k=1}^s q_k^{b_k / 2} \right)$$
> where $u \in \{1, -1, i, -i\}$ is one of the $4$ units.
> - If any $b_k$ is odd, no such $\alpha$ exists, so $r_2(n) = 0$.
> - For each $p_j$, the power $c_j$ can be chosen in $a_j + 1$ ways: $c_j \in \{0, 1, \dots, a_j\}$.
> - There are $4$ choices for the unit $u$.
>
> Thus:
> $$r_2(n) = 4 \prod_{j=1}^r (a_j + 1) \quad (\text{if all } b_k \text{ are even}, \text{else } 0)$$
> On the other hand, the arithmetic function $f(n) = d_1(n) - d_3(n) = (\chi_4 * \mathbf{1})(n)$ is multiplicative!
> Evaluating $f$ on prime powers:
> - $f(2^a) = \chi_4(1) + \chi_4(2) + \dots + \chi_4(2^a) = 1 + 0 + \dots = 1$.
> - For $p \equiv 1 \pmod 4$: $f(p^a) = \sum_{m=0}^a \chi_4(p^m) = \sum_{m=0}^a 1 = a + 1$.
> - For $q \equiv 3 \pmod 4$: $f(q^b) = \sum_{m=0}^b \chi_4(q^m) = 1 - 1 + 1 - 1 + \dots = \begin{cases} 1 & \text{if } b \text{ is even} \\ 0 & \text{if } b \text{ is odd} \end{cases}$
>
> Multiplying over all prime factors, $4 f(n)$ matches $r_2(n)$ exactly on all positive integers! $\blacksquare$

---

### 4. Geometric Interpretation: The Gauss Circle Problem

The value $r_2(n)$ represents the number of integer lattice points on the circle of radius $\sqrt{n}$ centered at the origin:
$$x^2 + y^2 = n$$
The total number of lattice points inside and on the closed disk of radius $R$ is:
$$N(R) = \sum_{n \le R^2} r_2(n) = \#\{(x, y) \in \mathbb{Z}^2 : x^2 + y^2 \le R^2\}$$
Since each lattice point corresponds to a unit square of area $1$, the number of points approximates the area of the disk:
$$N(R) = \pi R^2 + E(R)$$
Gauss proved the elementary bound for the error term:
$$|E(R)| \le 2\sqrt{2} \pi R = \mathcal{O}(R)$$
The problem of determining the infimum exponent $\theta$ such that $E(R) = \mathcal{O}(R^{\theta})$ is the celebrated **Gauss Circle Problem** (conjectured to be $\theta = 1/2 + \varepsilon$)."""
            },
            {
                "secNumber": "8.4",
                "title": "Euler's Four-Square Identity & Hamilton Quaternions",
                "content": r"""### 1. Beyond Two Squares

While not every integer is a sum of two squares (e.g., $3, 6, 7, 11, 12, 14, 15$), and not every integer is a sum of three squares (e.g., $7, 15, 23, 28$), Leonhard Euler suspected that **four squares suffice for every integer**.

The linchpin of Euler's attack was discovered in 1748: a 4-variable analogue of the Brahmagupta-Fibonacci identity.

---

### 2. Euler's Four-Square Identity

> **Theorem 8.6 (Euler's Four-Square Identity):**
> For any real or complex numbers $a_1, a_2, a_3, a_4$ and $b_1, b_2, b_3, b_4$:
> $$(a_1^2 + a_2^2 + a_3^2 + a_4^2)(b_1^2 + b_2^2 + b_3^2 + b_4^2) = c_1^2 + c_2^2 + c_3^2 + c_4^2$$
> where:
> $$\begin{aligned}
> c_1 &= a_1 b_1 - a_2 b_2 - a_3 b_3 - a_4 b_4 \\
> c_2 &= a_1 b_2 + a_2 b_1 + a_3 b_4 - a_4 b_3 \\
> c_3 &= a_1 b_3 - a_2 b_4 + a_3 b_1 + a_4 b_2 \\
> c_4 &= a_1 b_4 + a_2 b_3 - a_3 b_2 + a_4 b_1
> \end{aligned}$$

While verifying this algebraic identity by brute-force expansion involves 16 products of squares and 24 cross-terms that cancel in pairs, the true structural origin of the identity remained mysterious for nearly a century until William Rowan Hamilton discovered the **quaternions** in 1843.

---

### 3. The Algebra of Quaternions $\mathbb{H}$

> **Definition 8.4 (Hamilton Quaternions):**
> The quaternion algebra $\mathbb{H}$ is the 4-dimensional associative division algebra over $\mathbb{R}$ with basis $\{1, i, j, k\}$ satisfying the fundamental relations:
> $$i^2 = j^2 = k^2 = i j k = -1$$
> from which it follows that:
> $$i j = k = -j i, \qquad j k = i = -k j, \qquad k i = j = -i k$$
> Any quaternion $q \in \mathbb{H}$ is written as:
> $$q = a_1 + a_2 i + a_3 j + a_4 k, \qquad a_1, a_2, a_3, a_4 \in \mathbb{R}$$

Multiplication in $\mathbb{H}$ is non-commutative ($i j \ne j i$).

---

### 4. Quaternion Conjugation and Norm

> **Definition 8.5 (Quaternion Conjugate and Norm):**
> For $q = a_1 + a_2 i + a_3 j + a_4 k \in \mathbb{H}$, the **quaternion conjugate** is:
> $$\bar{q} = a_1 - a_2 i - a_3 j - a_4 k$$
> The **quaternion norm** is defined by:
> $$\|q\|^2 = q \bar{q} = \bar{q} q = a_1^2 + a_2^2 + a_3^2 + a_4^2$$

> **Theorem 8.7 (Multiplicativity of Quaternion Norm):**
> For any two quaternions $p, q \in \mathbb{H}$:
> $$\overline{p q} = \bar{q} \bar{p}$$
> and consequently:
> $$\|p q\|^2 = \|p\|^2 \|q\|^2$$

> **Proof:**
> To verify anti-automorphism $\overline{p q} = \bar{q} \bar{p}$, check on basis elements:
> - $\overline{i j} = \bar{k} = -k$. Meanwhile $\bar{j} \bar{i} = (-j)(-i) = j i = -k$. Matches!
> - The linearity over $\mathbb{R}$ extends this to all $p, q \in \mathbb{H}$.
>
> Now evaluate the squared norm:
> $$\|p q\|^2 = (p q) \overline{(p q)} = (p q)(\bar{q} \bar{p})$$
> By associativity of quaternion multiplication:
> $$= p (q \bar{q}) \bar{p} = p (\|q\|^2) \bar{p}$$
> Since $\|q\|^2 \in \mathbb{R}$ is a real scalar, it commutes with all elements of $\mathbb{H}$:
> $$= \|q\|^2 (p \bar{p}) = \|q\|^2 \|p\|^2 = \|p\|^2 \|q\|^2 \quad \blacksquare$$

> **Remark (Euler's Identity as Quaternion Norm):**
> Let $p = a_1 + a_2 i + a_3 j + a_4 k$ and $q = b_1 + b_2 i + b_3 j + b_4 k$.
> Direct computation of the product $p q$ gives:
> $$p q = c_1 + c_2 i + c_3 j + c_4 k$$
> where $c_1, c_2, c_3, c_4$ are precisely the expressions in Theorem 8.6!
> Since $\|p q\|^2 = c_1^2 + c_2^2 + c_3^2 + c_4^2$ and $\|p\|^2 \|q\|^2 = (a_1^2 + a_2^2 + a_3^2 + a_4^2)(b_1^2 + b_2^2 + b_3^2 + b_4^2)$, the multiplicativity of the quaternion norm proves Euler's four-square identity in a single stroke!

---

### 5. Hurwitz Integers and Maximal Orders

In 1896, Adolf Hurwitz discovered that to develop a Euclidean division algorithm for quaternions, the naive ring $\mathbb{Z}[i, j, k]$ is insufficient (its lattice points are too sparse to guarantee remainders of norm $< 1$).
Instead, one must include the body-centered points:

> **Definition 8.6 (Hurwitz Quaternions):**
> The ring of Hurwitz quaternions $\mathcal{H}$ is:
> $$\mathcal{H} = \left\{ a_1 + a_2 i + a_3 j + a_4 k : \text{all } a_m \in \mathbb{Z} \text{ or all } a_m \in \mathbb{Z} + \tfrac{1}{2} \right\}$$
> The ring $\mathcal{H}$ has exactly $24$ units (the binary tetrahedral group):
> $$\mathcal{H}^\times = \{\pm 1, \pm i, \pm j, \pm k\} \cup \left\{ \tfrac{\pm 1 \pm i \pm j \pm k}{2} \right\}$$
> and satisfies a left- and right-Euclidean division algorithm."""
            },
            {
                "secNumber": "8.5",
                "title": "Lagrange's Four-Square Theorem & Legendre's Three-Square Theorem",
                "content": r"""### 1. Lagrange's Four-Square Theorem

In 1770, Joseph-Louis Lagrange proved what Fermat had claimed more than a century earlier: every positive integer is the sum of at most four squares.

> **Theorem 8.8 (Lagrange's Four-Square Theorem):**
> Every positive integer $n \in \mathbb{N}$ can be expressed as the sum of four integer squares:
> $$n = x_1^2 + x_2^2 + x_3^2 + x_4^2, \qquad x_1, x_2, x_3, x_4 \in \mathbb{Z}$$

---

### 2. Line-by-Line Proof of Lagrange's Theorem

Thanks to Euler's identity (Theorem 8.6), the product of any two sums of four squares is another sum of four squares.
Since every integer $n > 1$ factors into prime numbers, **it suffices to prove the theorem for prime numbers $p$**.

- For $p = 2$: $2 = 1^2 + 1^2 + 0^2 + 0^2$.
- Hence, let $p$ be an odd prime. The proof proceeds in two steps:
  1. **Solvability of a Congruence:** Show that there exists a multiple $m p$ with $1 \le m < p$ that is a sum of four squares.
  2. **Method of Infinite Descent:** Show that if $m p = x_1^2 + x_2^2 + x_3^2 + x_4^2$ with $m > 1$, we can construct a smaller multiple $m' p = y_1^2 + y_2^2 + y_3^2 + y_4^2$ with $1 \le m' < m$.

---

#### Step 1: The Pigeonhole Lemma

> **Lemma 8.4 (Modular Solvability):**
> For any odd prime $p$, there exist integers $x, y$ such that:
> $$x^2 + y^2 + 1 \equiv 0 \pmod p$$
> Consequently, there exists an integer $m$ with $1 \le m < p$ such that:
> $$m p = x^2 + y^2 + 1^2 + 0^2$$

> **Proof:**
> Consider the two sets of residue classes modulo $p$:
> $$S_1 = \{x^2 \pmod p : 0 \le x \le \tfrac{p-1}{2}\}$$
> $$S_2 = \{-1 - y^2 \pmod p : 0 \le y \le \tfrac{p-1}{2}\}$$
> - In $S_1$, all elements are distinct: if $x_1^2 \equiv x_2^2 \pmod p$, then $p \mid (x_1 - x_2)(x_1 + x_2)$.
>   Since $0 \le x_1, x_2 \le \frac{p-1}{2}$, we have $|x_1 - x_2| < p$ and $0 \le x_1 + x_2 \le p-1 < p$.
>   Thus $x_1 = x_2$. Hence $|S_1| = \frac{p-1}{2} + 1 = \frac{p+1}{2}$.
> - By the identical reasoning, all elements in $S_2$ are distinct, so $|S_2| = \frac{p+1}{2}$.
>
> Now sum their cardinalities:
> $$|S_1| + |S_2| = \frac{p+1}{2} + \frac{p+1}{2} = p + 1 > p$$
> Since there are only $p$ distinct residue classes modulo $p$, by the **Pigeonhole Principle**, $S_1$ and $S_2$ must have at least one residue in common!
> That is, there exist $0 \le x, y \le \frac{p-1}{2}$ such that:
> $$x^2 \equiv -1 - y^2 \pmod p \implies x^2 + y^2 + 1 \equiv 0 \pmod p$$
> Therefore, $x^2 + y^2 + 1^2 + 0^2 = m p$ for some integer $m \ge 1$.
> Moreover:
> $$m p = x^2 + y^2 + 1 \le \left(\frac{p-1}{2}\right)^2 + \left(\frac{p-1}{2}\right)^2 + 1 < \frac{p^2}{4} + \frac{p^2}{4} + 1 < \frac{p^2}{2} + 1 < p^2$$
> Dividing by $p$, we obtain $m < p$. $\blacksquare$

---

#### Step 2: Minimal Descent on the Multiplier $m$

> **Proof of Descent (Step 2):**
> By Step 1, the set of integers $m \in \{1, 2, \dots, p-1\}$ such that $m p$ is a sum of four squares is non-empty.
> By the Well-Ordering Principle of $\mathbb{N}$, there exists a **minimal** such integer $m$.
> We claim that $m = 1$.
>
> Suppose for contradiction that $m > 1$.
> Let $m p = x_1^2 + x_2^2 + x_3^2 + x_4^2$.
>
> **Case A: $m$ is even.**
> If $m$ is even, then $m p$ is even.
> Thus $x_1^2 + x_2^2 + x_3^2 + x_4^2 \equiv 0 \pmod 2$.
> This means either:
> 1. All four $x_j$ are of the same parity (all even or all odd), or
> 2. Exactly two are even and two are odd.
>
> In either case, we can pair them up, say $(x_1, x_2)$ and $(x_3, x_4)$, such that $x_1 \equiv x_2 \pmod 2$ and $x_3 \equiv x_4 \pmod 2$.
> Then $\frac{x_1 \pm x_2}{2}$ and $\frac{x_3 \pm x_4}{2}$ are all integers.
> Observe the algebraic identity:
> $$\left(\frac{x_1 + x_2}{2}\right)^2 + \left(\frac{x_1 - x_2}{2}\right)^2 + \left(\frac{x_3 + x_4}{2}\right)^2 + \left(\frac{x_3 - x_4}{2}\right)^2 = \frac{x_1^2 + x_2^2 + x_3^2 + x_4^2}{2} = \left(\frac{m}{2}\right) p$$
> Setting $m' = m/2 < m$, we have expressed $m' p$ as a sum of four integer squares, contradicting the minimality of $m$!
>
> **Case B: $m$ is odd and $m > 1$.**
> For each $j \in \{1, 2, 3, 4\}$, choose $y_j \in \mathbb{Z}$ such that:
> $$y_j \equiv x_j \pmod m \quad \text{and} \quad -\frac{m-1}{2} \le y_j \le \frac{m-1}{2}$$
> Then:
> $$\sum_{j=1}^4 y_j^2 \equiv \sum_{j=1}^4 x_j^2 = m p \equiv 0 \pmod m$$
> Thus:
> $$y_1^2 + y_2^2 + y_3^2 + y_4^2 = k m$$
> for some integer $k \ge 0$.
>
> - Could $k = 0$? If $k = 0$, then each $y_j = 0$, which means $x_j \equiv 0 \pmod m$.
>   Then $m \mid x_j$ for all $j$, so $m^2 \mid \sum x_j^2 = m p \implies m \mid p$.
>   Since $p$ is prime and $1 < m < p$, this is impossible! Thus $k > 0$.
> - How large can $k$ be?
>   $$k m = \sum_{j=1}^4 y_j^2 \le 4 \left(\frac{m-1}{2}\right)^2 < 4 \left(\frac{m}{2}\right)^2 = m^2$$
>   Dividing by $m$: $k < m$.
>
> Now multiply $(m p)$ and $(k m)$ using Euler's Four-Square Identity (Theorem 8.6):
> $$(m p)(k m) = m^2 (k p) = z_1^2 + z_2^2 + z_3^2 + z_4^2$$
> where:
> $$\begin{aligned}
> z_1 &= x_1 y_1 + x_2 y_2 + x_3 y_3 + x_4 y_4 \\
> z_2 &= x_1 y_2 - x_2 y_1 + x_3 y_4 - x_4 y_3 \\
> z_3 &= x_1 y_3 - x_3 y_1 - x_2 y_4 + x_4 y_2 \\
> z_4 &= x_1 y_4 - x_4 y_1 + x_2 y_3 - x_3 y_2
> \end{aligned}$$
> Modulo $m$, since $y_j \equiv x_j \pmod m$:
> $$z_1 \equiv x_1^2 + x_2^2 + x_3^2 + x_4^2 = m p \equiv 0 \pmod m$$
> $$z_2 \equiv x_1 x_2 - x_2 x_1 + x_3 x_4 - x_4 x_3 = 0 \pmod m$$
> $$z_3 \equiv x_1 x_3 - x_3 x_1 - x_2 x_4 + x_4 x_2 = 0 \pmod m$$
> $$z_4 \equiv x_1 x_4 - x_4 x_1 + x_2 x_3 - x_3 x_2 = 0 \pmod m$$
> Thus, every $z_j$ is divisible by $m$!
> Dividing both sides of $m^2 (k p) = \sum z_j^2$ by $m^2$:
> $$k p = \left(\frac{z_1}{m}\right)^2 + \left(\frac{z_2}{m}\right)^2 + \left(\frac{z_3}{m}\right)^2 + \left(\frac{z_4}{m}\right)^2$$
> Since each $z_j / m \in \mathbb{Z}$, we have represented $k p$ as a sum of four integer squares with $1 \le k < m$.
> This contradicts the minimality of $m$!
>
> Therefore, $m = 1$, and $p = x_1^2 + x_2^2 + x_3^2 + x_4^2$. $\blacksquare$

---

### 3. Number of Representations: Jacobi's Four-Square Theorem

In 1834, Carl Gustav Jacob Jacobi derived the exact formula for $r_4(n) = \#\{(x_1, x_2, x_3, x_4) \in \mathbb{Z}^4 : \sum x_j^2 = n\}$ using theta functions.

> **Theorem 8.9 (Jacobi's Four-Square Formula):**
> For every positive integer $n \in \mathbb{N}$:
> $$r_4(n) = 8 \sum_{\substack{d \mid n \\ 4 \nmid d}} d = \begin{cases} 8 \sigma(n) & \text{if } n \text{ is odd} \\ 24 \sigma(m) & \text{if } n = 2^k m \text{ with } m \text{ odd, } k \ge 1 \end{cases}$$

Since $1 \mid n$ and $4 \nmid 1$, the sum is always at least $8 \cdot 1 = 8 > 0$, giving an independent proof that $r_4(n) \ge 8$ for all $n \ge 1$.

---

### 4. Legendre's Three-Square Theorem

Which integers can be written as the sum of **three** squares?

> **Theorem 8.10 (Legendre's Three-Square Theorem, 1798):**
> A positive integer $n$ can be expressed as the sum of three integer squares:
> $$n = x^2 + y^2 + z^2, \qquad x, y, z \in \mathbb{Z}$$
> if and only if $n$ is **not** of the form:
> $$n = 4^a (8 b + 7), \qquad a, b \in \mathbb{Z}_{\ge 0}$$

> **Proof of Necessity ($\Rightarrow$):**
> For any integer $w$, $w^2 \equiv 0, 1, \text{ or } 4 \pmod 8$.
> The possible sums of three squares modulo $8$ are:
> - $0+0+0 = 0$
> - $0+0+1 = 1$
> - $0+1+1 = 2$
> - $1+1+1 = 3$
> - $0+0+4 = 4$
> - $0+1+4 = 5$
> - $1+1+4 = 6$
> The residues $7 \pmod 8$ is completely missing!
> Thus, no integer $n \equiv 7 \pmod 8$ can be a sum of three squares.
>
> Now suppose $n = 4^a (8 b + 7) = x^2 + y^2 + z^2$ for some $a \ge 1$.
> Modulo $4$:
> $$x^2 + y^2 + z^2 \equiv 0 \pmod 4$$
> Since squares modulo 4 are 0 or 1, the only way their sum can be $0 \pmod 4$ is if all three are $0 \pmod 4$:
> $$x^2 \equiv y^2 \equiv z^2 \equiv 0 \pmod 4 \implies 2 \mid x, \; 2 \mid y, \; 2 \mid z$$
> Dividing by 4:
> $$\frac{n}{4} = 4^{a-1}(8b + 7) = \left(\frac{x}{2}\right)^2 + \left(\frac{y}{2}\right)^2 + \left(\frac{z}{2}\right)^2$$
> By induction on $a$, descending $a$ times yields:
> $$8 b + 7 = \left(\frac{x}{2^a}\right)^2 + \left(\frac{y}{2^a}\right)^2 + \left(\frac{z}{2^a}\right)^2$$
> which is impossible because $8b+7 \equiv 7 \pmod 8$ is not a sum of three squares!
> This proves necessity. $\blacksquare$

> **Remark on Sufficiency:**
> Proving that *every* integer not of the form $4^a(8b+7)$ is indeed a sum of three squares is notoriously difficult; Adrien-Marie Legendre published an incomplete proof in 1798, and Carl Friedrich Gauss gave the first complete proof in 1801 (*Disquisitiones Arithmeticae*, Art. 291) using his deep theory of ternary quadratic forms.

---

### 5. Hierarchy of Sums of Squares

| Number of Squares | Solvability Condition | Representation Count Formula |
| :--- | :--- | :--- |
| **Two Squares** ($x^2 + y^2$) | All prime factors $q \equiv 3 \pmod 4$ have even powers | $r_2(n) = 4(d_1(n) - d_3(n))$ |
| **Three Squares** ($x^2 + y^2 + z^2$) | $n \ne 4^a(8b + 7)$ | Proportional to class numbers of binary quadratic forms |
| **Four Squares** ($x_1^2 + x_2^2 + x_3^2 + x_4^2$) | **All integers $n \ge 0$** (Unconditional!) | $r_4(n) = 8 \sum_{d \mid n, 4 \nmid d} d$ |"""
            }
        ],
        "problems": [
            {
                "id": "prob_8_1",
                "tier": "Foundational",
                "title": "Hermite-Serret Two-Square Decomposition of Primes",
                "statement": r"""Apply the Hermite-Serret / Extended Euclidean Descent algorithm to decompose the following primes congruent to $1 \pmod 4$ into explicit sums of two squares $p = x^2 + y^2$:
1. $p = 13$
2. $p = 29$
3. $p = 41$

For each prime, show:
- The determination of a modular square root $z$ satisfying $z^2 \equiv -1 \pmod p$.
- The Euclidean algorithm steps dividing $p$ by $z$ until the first remainder $r < \sqrt{p}$ appears.
- Verification that $p = r^2 + q^2$ where $q$ is the next remainder.""",
                "solution": r"""### Step 1: Prime $p = 13$

1. **Modular root of $-1$:**
   $13 \equiv 1 \pmod 4$. We need $z^2 \equiv -1 \equiv 12 \pmod{13}$.
   Testing small values:
   $$5^2 = 25 = 2 \times 13 - 1 \equiv -1 \pmod{13}$$
   Thus $z = 5$.
2. **Euclidean Descent:**
   We divide $p = 13$ by $z = 5$:
   $$\sqrt{13} \approx 3.605$$
   - $13 = 2 \times 5 + 3$ (remainder $r_1 = 3 < \sqrt{13}$)
   - $5 = 1 \times 3 + 2$ (remainder $r_2 = 2 < \sqrt{13}$)
3. **Decomposition:**
   Here $r_1 = 3$ and $r_2 = 2$.
   Checking:
   $$3^2 + 2^2 = 9 + 4 = 13$$
   Thus $13 = 3^2 + 2^2$.

---

### Step 2: Prime $p = 29$

1. **Modular root of $-1$:**
   $29 \equiv 1 \pmod 4$. We need $z^2 \equiv -1 \equiv 28 \pmod{29}$.
   Testing values:
   $$12^2 = 144 = 5 \times 29 - 1 = 145 - 1 \implies 12^2 \equiv -1 \pmod{29}$$
   Thus $z = 12$.
2. **Euclidean Descent:**
   $$\sqrt{29} \approx 5.385$$
   Divide $p = 29$ by $z = 12$:
   - $29 = 2 \times 12 + 5$ (remainder $r_1 = 5 < \sqrt{29}$)
   - $12 = 2 \times 5 + 2$ (remainder $r_2 = 2 < \sqrt{29}$)
3. **Decomposition:**
   Here $r_1 = 5$ and $r_2 = 2$.
   Checking:
   $$5^2 + 2^2 = 25 + 4 = 29$$
   Thus $29 = 5^2 + 2^2$.

---

### Step 3: Prime $p = 41$

1. **Modular root of $-1$:**
   $41 \equiv 1 \pmod 4$. We need $z^2 \equiv -1 \equiv 40 \pmod{41}$.
   Testing values:
   $$9^2 = 81 = 2 \times 41 - 1 = 82 - 1 \implies 9^2 \equiv -1 \pmod{41}$$
   Thus $z = 9$.
2. **Euclidean Descent:**
   $$\sqrt{41} \approx 6.403$$
   Divide $p = 41$ by $z = 9$:
   - $41 = 4 \times 9 + 5$ (remainder $r_1 = 5 < \sqrt{41}$)
   - $9 = 1 \times 5 + 4$ (remainder $r_2 = 4 < \sqrt{41}$)
3. **Decomposition:**
   Here $r_1 = 5$ and $r_2 = 4$.
   Checking:
   $$5^2 + 4^2 = 25 + 16 = 41$$
   Thus $41 = 5^2 + 4^2$.

The Hermite-Serret algorithm is guaranteed by the geometry of the Euclidean algorithm: the two consecutive remainders bounding $\sqrt{p}$ always satisfy $r_k^2 + r_{k+1}^2 = p$."""
            },
            {
                "probNumber": "8.2",
                "tier": "Advanced",
                "title": "Full Representation Lattice & Gaussian Decompositions of $n = 1105$",
                "statement": r"""Consider the integer $n = 1105 = 5 \times 13 \times 17$.
1. Compute the total number of representations $r_2(1105)$ as the sum of two squares in $\mathbb{Z}^2$.
2. Find the Gaussian prime factorization of each factor $5, 13, 17 \in \mathbb{Z}[i]$.
3. Use the product of Gaussian primes with all possible conjugate pairings to find all distinct unordered pairs of positive integers $\{x, y\}$ such that $x^2 + y^2 = 1105$.
4. Classify each representation as primitive ($\gcd(x, y) = 1$) or imprimitive.""",
                "solution": r"""### 1. Total Number of Representations $r_2(1105)$

The prime factorization of $1105$ is:
$$1105 = 5^1 \times 13^1 \times 17^1$$
All prime factors are congruent to $1 \pmod 4$:
$$5 \equiv 1, \quad 13 \equiv 1, \quad 17 \equiv 1 \pmod 4$$
No prime factors congruent to $3 \pmod 4$ appear ($s = 0$).
By Jacobi's formula:
$$r_2(n) = 4 (a_1 + 1)(a_2 + 1)(a_3 + 1) = 4(1 + 1)(1 + 1)(1 + 1) = 4 \times 8 = 32$$
There are $32$ pairs $(x, y) \in \mathbb{Z}^2$.

---

### 2. Gaussian Prime Factorizations

Each prime splits into conjugate Gaussian primes:
- $5 = (2 + i)(2 - i)$
- $13 = (3 + 2i)(3 - 2i)$
- $17 = (4 + i)(4 - i)$

---

### 3. All Distinct Pairs $\{x, y\}$ via Conjugate Sign Combinations

Any Gaussian integer $\alpha$ of norm $1105$ has the form:
$$\alpha = u \cdot (2 \pm i)(3 \pm 2i)(4 \pm i), \qquad u \in \{\pm 1, \pm i\}$$
Fixing $u = 1$ and choosing the sign of $i$ for the three factors gives $2^3 = 8$ choices:
Let $\pi_1 = 2 + i$, $\pi_2 = 3 + 2i$, $\pi_3 = 4 + i$.
Taking conjugate pairings $\alpha$ and $\bar{\alpha}$ yields the same pair $\{|x|, |y|\}$.
Thus there are $8 / 2 = 4$ fundamentally distinct unordered pairs of positive integers $\{x, y\}$!

Let us compute the 4 products explicitly:

1. **Choice 1: $\pi_1 \pi_2 \pi_3 = (2 + i)(3 + 2i)(4 + i)$**
   $$(2 + i)(3 + 2i) = (6 - 2) + (4 + 3)i = 4 + 7i$$
   $$(4 + 7i)(4 + i) = (16 - 7) + (4 + 28)i = 9 + 32i$$
   Check: $9^2 + 32^2 = 81 + 1024 = 1105$. $\checkmark$
   **Pair 1:** $\{9, 32\}$.

2. **Choice 2: $\pi_1 \bar{\pi}_2 \pi_3 = (2 + i)(3 - 2i)(4 + i)$**
   $$(2 + i)(3 - 2i) = (6 + 2) + (-4 + 3)i = 8 - i$$
   $$(8 - i)(4 + i) = (32 + 1) + (8 - 4)i = 33 + 4i$$
   Check: $33^2 + 4^2 = 1089 + 16 = 1105$. $\checkmark$
   **Pair 2:** $\{4, 33\}$.

3. **Choice 3: $\bar{\pi}_1 \pi_2 \pi_3 = (2 - i)(3 + 2i)(4 + i)$**
   $$(2 - i)(3 + 2i) = (6 + 2) + (4 - 3)i = 8 + i$$
   $$(8 + i)(4 + i) = (32 - 1) + (8 + 4)i = 31 + 12i$$
   Check: $31^2 + 12^2 = 961 + 144 = 1105$. $\checkmark$
   **Pair 3:** $\{12, 31\}$.

4. **Choice 4: $\pi_1 \pi_2 \bar{\pi}_3 = (2 + i)(3 + 2i)(4 - i)$**
   $$(4 + 7i)(4 - i) = (16 + 7) + (-4 + 28)i = 23 + 24i$$
   Check: $23^2 + 24^2 = 529 + 576 = 1105$. $\checkmark$
   **Pair 4:** $\{23, 24\}$.

---

### 4. Classification of Pairs

- $\{9, 32\}$: $\gcd(9, 32) = 1 \implies$ **Primitive**
- $\{4, 33\}$: $\gcd(4, 33) = 1 \implies$ **Primitive**
- $\{12, 31\}$: $\gcd(12, 31) = 1 \implies$ **Primitive**
- $\{23, 24\}$: $\gcd(23, 24) = 1 \implies$ **Primitive**

All four representations are primitive because no rational prime factor divides $\alpha$ (which would require taking both $\pi_j$ and $\bar{\pi}_j$).
Accounting for 4 unit rotations $\times$ 2 orderings $\times$ 4 sign configurations gives $4 \times 8 = 32$ ordered integer pairs in $\mathbb{Z}^2$, exactly matching $r_2(1105)$."""
            },
            {
                "probNumber": "8.3",
                "tier": "Honors / Proof Challenge",
                "title": "Complete Descent in Lagrange's Four-Square Theorem",
                "statement": r"""Provide the complete, rigorous algebraic proof of the minimal descent step in Lagrange's Four-Square Theorem:

Given an odd prime $p$ and an odd integer $m$ satisfying $1 < m < p$ such that:
$$m p = x_1^2 + x_2^2 + x_3^2 + x_4^2, \qquad x_j \in \mathbb{Z}$$

Prove with full mathematical rigor that:
1. Choosing $y_j \in \left(-\frac{m}{2}, \frac{m}{2}\right]$ with $y_j \equiv x_j \pmod m$ ensures that $\sum_{j=1}^4 y_j^2 = k m$ where $1 \le k < m$.
2. Under Euler's Four-Square Identity:
   $$(m p)(k m) = z_1^2 + z_2^2 + z_3^2 + z_4^2$$
   every integer $z_j$ ($j = 1, 2, 3, 4$) is divisible by $m$.
3. Setting $w_j = z_j / m \in \mathbb{Z}$ yields:
   $$k p = w_1^2 + w_2^2 + w_3^2 + w_4^2, \qquad 1 \le k < m$$
   thereby completing the descent induction that forces $m = 1$.""",
                "solution": r"""### 1. Construction and Bounds on $k$

For each $j \in \{1, 2, 3, 4\}$, choose $y_j$ as the unique representative of $x_j$ modulo $m$ in the centered range:
$$-\frac{m-1}{2} \le y_j \le \frac{m-1}{2}$$
Since $y_j \equiv x_j \pmod m$, we have $y_j^2 \equiv x_j^2 \pmod m$.
Summing over $j = 1, 2, 3, 4$:
$$\sum_{j=1}^4 y_j^2 \equiv \sum_{j=1}^4 x_j^2 = m p \equiv 0 \pmod m$$
Thus, there exists an integer $k \ge 0$ such that:
$$\sum_{j=1}^4 y_j^2 = k m$$

**Lower bound on $k$ ($k \ge 1$):**
If $k = 0$, then $\sum y_j^2 = 0$. Since each $y_j \in \mathbb{R}$, this forces $y_1 = y_2 = y_3 = y_4 = 0$.
Then $x_j \equiv y_j = 0 \pmod m$, meaning $m \mid x_j$ for all $j \in \{1, 2, 3, 4\}$.
This implies $m^2 \mid x_j^2$, and hence:
$$m^2 \mid \sum_{j=1}^4 x_j^2 = m p \implies m \mid p$$
Since $p$ is prime and $1 < m < p$, $m$ cannot divide $p$.
This contradiction proves that $k > 0$, so $k \ge 1$.

**Upper bound on $k$ ($k < m$):**
Using the bound $|y_j| \le \frac{m-1}{2} < \frac{m}{2}$:
$$k m = \sum_{j=1}^4 y_j^2 \le 4 \left(\frac{m-1}{2}\right)^2 = (m - 1)^2 < m^2$$
Dividing by $m > 0$ gives:
$$k < m$$
Thus $1 \le k < m$.

---

### 2. Divisibility of $z_j$ by $m$ via Euler's Identity

Using Euler's Four-Square Identity:
$$(m p)(k m) = \left( \sum_{j=1}^4 x_j^2 \right) \left( \sum_{j=1}^4 y_j^2 \right) = z_1^2 + z_2^2 + z_3^2 + z_4^2$$
where:
$$\begin{aligned}
z_1 &= x_1 y_1 + x_2 y_2 + x_3 y_3 + x_4 y_4 \\
z_2 &= x_1 y_2 - x_2 y_1 + x_3 y_4 - x_4 y_3 \\
z_3 &= x_1 y_3 - x_3 y_1 - x_2 y_4 + x_4 y_2 \\
z_4 &= x_1 y_4 - x_4 y_1 + x_2 y_3 - x_3 y_2
\end{aligned}$$

Now substitute $y_j \equiv x_j \pmod m$ into each $z_j$:

1. For $z_1$:
   $$z_1 \equiv x_1(x_1) + x_2(x_2) + x_3(x_3) + x_4(x_4) = x_1^2 + x_2^2 + x_3^2 + x_4^2 = m p \equiv 0 \pmod m$$
2. For $z_2$:
   $$z_2 \equiv x_1(x_2) - x_2(x_1) + x_3(x_4) - x_4(x_3) = (x_1 x_2 - x_1 x_2) + (x_3 x_4 - x_3 x_4) = 0 \pmod m$$
3. For $z_3$:
   $$z_3 \equiv x_1(x_3) - x_3(x_1) - x_2(x_4) + x_4(x_2) = (x_1 x_3 - x_1 x_3) + (x_2 x_4 - x_2 x_4) = 0 \pmod m$$
4. For $z_4$:
   $$z_4 \equiv x_1(x_4) - x_4(x_1) + x_2(x_3) - x_3(x_2) = (x_1 x_4 - x_1 x_4) + (x_2 x_3 - x_2 x_3) = 0 \pmod m$$

Every $z_j$ is an exact integer multiple of $m$:
$$z_j \equiv 0 \pmod m \implies \frac{z_j}{m} \in \mathbb{Z} \quad \text{for all } j \in \{1, 2, 3, 4\}$$

---

### 3. Conclusion of the Descent

Divide the Euler product equation by $m^2$:
$$\frac{(m p)(k m)}{m^2} = \frac{z_1^2 + z_2^2 + z_3^2 + z_4^2}{m^2}$$
$$k p = \left(\frac{z_1}{m}\right)^2 + \left(\frac{z_2}{m}\right)^2 + \left(\frac{z_3}{m}\right)^2 + \left(\frac{z_4}{m}\right)^2$$
Defining $w_j = z_j / m \in \mathbb{Z}$, we have:
$$k p = w_1^2 + w_2^2 + w_3^2 + w_4^2$$
Since $1 \le k < m$, this produces a strictly smaller positive integer multiple of $p$ that is expressible as the sum of four squares.

By the Well-Ordering Principle, this descent process cannot continue indefinitely through the positive integers. It must terminate when $m = 1$, which proves:
$$p = x_1^2 + x_2^2 + x_3^2 + x_4^2$$
This completes the rigorous descent proof. $\blacksquare$"""
            }
        ]
    }
    return u8

if __name__ == "__main__":
    u8 = get_unit8()
    print(f"Loaded Unit 8: {u8['title']} with {len(u8['sections'])} sections and {len(u8['problems'])} problems.")
