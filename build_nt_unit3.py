# -*- coding: utf-8 -*-
"""
build_nt_unit3.py
Constructs Unit 3: Theory of Congruences & The Chinese Remainder Theorem
"""

def get_unit3():
    u3 = {
        "number": 3,
        "title": "Theory of Congruences & The Chinese Remainder Theorem",
        "leadSummary": "Foundations of modular arithmetic: congruence relations and the residue class ring $\\mathbb{Z}/m\\mathbb{Z}$, complete and reduced residue systems, linear congruences $ax \\equiv b \\pmod m$, modular multiplicative inverses, the Chinese Remainder Theorem for simultaneous congruence systems, Lagrange's Theorem on polynomial congruences modulo primes, and Hensel's Lemma for $p$-adic root lifting.",
        "simulations": ["sim_nt_chinese_remainder_crt"],
        "sections": [
            {
                "secNumber": "3.1",
                "title": "Congruence Relations, Residue Classes & The Ring Z/mZ",
                "content": r"""### 1. The Congruence Relation

The concept of congruence, introduced by Carl Friedrich Gauss in his masterpiece *Disquisitiones Arithmeticae* (1801), revolutionized number theory by framing divisibility in algebraic terms.

> **Definition 3.1 (Congruence Modulo $m$):**
> Let $m \in \mathbb{N}$ be a positive integer (called the **modulus**).
> Two integers $a, b \in \mathbb{Z}$ are said to be **congruent modulo $m$**, written:
> $$a \equiv b \pmod m$$
> if $m$ divides their difference: $m \mid (a - b)$.
> If $m \nmid (a - b)$, they are **incongruent**, written $a \not\equiv b \pmod m$.

> **Theorem 3.1 (Equivalence Relation):**
> Congruence modulo $m$ is an **equivalence relation** on the set of integers $\mathbb{Z}$:
> 1. Reflexivity: $a \equiv a \pmod m$ for all $a \in \mathbb{Z}$.
> 2. Symmetry: If $a \equiv b \pmod m$, then $b \equiv a \pmod m$.
> 3. Transitivity: If $a \equiv b \pmod m$ and $b \equiv c \pmod m$, then $a \equiv c \pmod m$.

---

### 2. Arithmetic of Congruences

> **Theorem 3.2 (Compatibility with Arithmetic Operations):**
> If $a \equiv b \pmod m$ and $c \equiv d \pmod m$, then:
> 1. Addition: $a + c \equiv b + d \pmod m$.
> 2. Subtraction: $a - c \equiv b - d \pmod m$.
> 3. Multiplication: $a c \equiv b d \pmod m$.
> 4. Exponentiation: $a^k \equiv b^k \pmod m$ for every positive integer $k \ge 1$.
> 5. Polynomial evaluation: If $P(x) \in \mathbb{Z}[x]$ is a polynomial with integer coefficients, then $P(a) \equiv P(b) \pmod m$.

> **Theorem 3.3 (Cancellation Law for Congruences):**
> If $a c \equiv b c \pmod m$, then:
> $$a \equiv b \pmod{\frac{m}{\gcd(c, m)}}$$
> In particular, if $\gcd(c, m) = 1$, we can cancel $c$ directly: $a \equiv b \pmod m$.

---

### 3. Residue Classes and the Ring $\mathbb{Z}/m\mathbb{Z}$

The equivalence classes of $\mathbb{Z}$ modulo $m$ are called **residue classes** (or congruence classes):
$$[a] = \bar{a} = \{x \in \mathbb{Z} : x \equiv a \pmod m\} = \{a + k m : k \in \mathbb{Z}\}$$
There are exactly $m$ pairwise disjoint residue classes:
$$\mathbb{Z}/m\mathbb{Z} = \{[0], [1], [2], \dots, [m-1]\}$$
Endowed with class addition $[a] + [b] = [a + b]$ and multiplication $[a][b] = [ab]$, $\mathbb{Z}/m\mathbb{Z}$ forms a commutative ring with identity $[1]$."""
            },
            {
                "secNumber": "3.2",
                "title": "Complete & Reduced Residue Systems & The Unit Group (Z/mZ)*",
                "content": r"""### 1. Complete Residue Systems

> **Definition 3.2 (Complete Residue System):**
> A set of $m$ integers $\{r_1, r_2, \dots, r_m\}$ is called a **complete residue system modulo $m$** (CRS) if every integer $x \in \mathbb{Z}$ is congruent to exactly one element of the set modulo $m$.
> The standard CRS is $\{0, 1, 2, \dots, m - 1\}$ (least non-negative residues).

> **Theorem 3.4 (Linear Transformation of a CRS):**
> If $\{r_1, r_2, \dots, r_m\}$ is a CRS modulo $m$ and $\gcd(a, m) = 1$, then for any integer $b \in \mathbb{Z}$, the set:
> $$\{a r_1 + b, a r_2 + b, \dots, a r_m + b\}$$
> is also a complete residue system modulo $m$.

---

### 2. Reduced Residue Systems and Euler's Totient $\phi(m)$

> **Definition 3.3 (Reduced Residue System):**
> A set of integers $\{r_1, r_2, \dots, r_k\}$ is called a **reduced residue system modulo $m$** (RRS) if:
> 1. $\gcd(r_i, m) = 1$ for all $1 \le i \le k$.
> 2. $r_i \not\equiv r_j \pmod m$ for all $i \ne j$.
> 3. Every integer $x$ with $\gcd(x, m) = 1$ is congruent to some $r_i$ modulo $m$.

The number of elements in any RRS modulo $m$ is denoted by $\phi(m)$ (Euler's totient function):
$$\phi(m) = \#\{a \in \mathbb{N} : 1 \le a \le m \text{ and } \gcd(a, m) = 1\}$$

---

### 3. The Multiplicative Unit Group $(\mathbb{Z}/m\mathbb{Z})^\times$

> **Theorem 3.5 (Invertible Elements Modulo $m$):**
> A residue class $[a] \in \mathbb{Z}/m\mathbb{Z}$ has a **multiplicative inverse** $[x]$ (meaning $[a][x] = [1] \iff ax \equiv 1 \pmod m$) if and only if:
> $$\gcd(a, m) = 1$$
> The set of all invertible residue classes forms an abelian group of order $\phi(m)$ under modular multiplication, denoted $(\mathbb{Z}/m\mathbb{Z})^\times$ or $U(m)$."""
            },
            {
                "secNumber": "3.3",
                "title": "Linear Congruences ax = b (mod m) & Modular Inverses",
                "content": r"""### 1. The General Linear Congruence

> **Definition 3.4 (Linear Congruence):**
> A **linear congruence** in one unknown $x$ is an equation of the form:
> $$a x \equiv b \pmod m$$
> where $a, b \in \mathbb{Z}$ and $m \in \mathbb{N}$.
> A solution is an integer $x_0$ such that $a x_0 \equiv b \pmod m$. Two solutions $x_1, x_2$ are regarded as identical if $x_1 \equiv x_2 \pmod m$.

---

### 2. Solvability and Number of Solutions

> **Theorem 3.6 (Complete Solution of $a x \equiv b \pmod m$):**
> Let $d = \gcd(a, m)$.
> 1. If $d \nmid b$, the congruence $a x \equiv b \pmod m$ has **no solutions**.
> 2. If $d \mid b$, the congruence has **exactly $d$ mutually incongruent solutions** modulo $m$.
> 3. If $x_0$ is any particular solution, the complete set of $d$ incongruent solutions modulo $m$ is:
>    $$x_k = x_0 + k \left(\frac{m}{d}\right), \quad k = 0, 1, 2, \dots, d - 1$$

> **Proof:**
> The congruence $a x \equiv b \pmod m$ is equivalent to the statement:
> $$m \mid (a x - b) \iff a x - b = m y \iff a x - m y = b$$
> for some integer $y \in \mathbb{Z}$.
> This is precisely the linear Diophantine equation in two variables studied in Unit 1 (Theorem 1.4).
> By Theorem 1.4, an integer solution exists if and only if $d = \gcd(a, m) \mid b$.
> When $d \mid b$, let $(x_0, y_0)$ be a particular solution.
> By Theorem 1.5, all integer solutions for $x$ are given by:
> $$x = x_0 + \left(\frac{m}{d}\right) t \quad (t \in \mathbb{Z})$$
> Now we determine how many of these solutions are distinct modulo $m$.
> Two solutions $x(t_1)$ and $x(t_2)$ are congruent modulo $m$ if and only if:
> $$x_0 + \left(\frac{m}{d}\right) t_1 \equiv x_0 + \left(\frac{m}{d}\right) t_2 \pmod m \iff \left(\frac{m}{d}\right) t_1 \equiv \left(\frac{m}{d}\right) t_2 \pmod m$$
> Dividing through by $\frac{m}{d}$:
> $$t_1 \equiv t_2 \pmod{\frac{m}{m/d}} \iff t_1 \equiv t_2 \pmod d$$
> Therefore, the values $t = 0, 1, 2, \dots, d - 1$ yield mutually incongruent solutions modulo $m$, and any other integer $t$ produces a solution congruent to one of these $d$ values! $\blacksquare$

> **Corollary 3.1 (Unique Modular Inverse):**
> If $\gcd(a, m) = 1$, the congruence $a x \equiv 1 \pmod m$ has a **unique solution** modulo $m$, called the **modular inverse** of $a$, denoted $a^{-1}$ or $\bar{a}$.
> The solution to $a x \equiv b \pmod m$ is then simply $x \equiv a^{-1} b \pmod m$."""
            },
            {
                "secNumber": "3.4",
                "title": "Systems of Linear Congruences & The Chinese Remainder Theorem",
                "content": r"""### 1. Statement of the Chinese Remainder Theorem

The Chinese Remainder Theorem (CRT) originated in the 3rd-century work *Sunzi Suanjing* (Master Sun's Mathematical Manual).

> **Theorem 3.7 (The Chinese Remainder Theorem):**
> Let $m_1, m_2, \dots, m_k \in \mathbb{N}$ be pairwise relatively prime positive integers:
> $$\gcd(m_i, m_j) = 1 \quad \forall i \ne j$$
> Let $a_1, a_2, \dots, a_k \in \mathbb{Z}$ be arbitrary integers.
> Then the system of simultaneous congruences:
> $$\begin{cases}
> x \equiv a_1 \pmod{m_1} \\
> x \equiv a_2 \pmod{m_2} \\
> \;\;\vdots \\
> x \equiv a_k \pmod{m_k}
> \end{cases}$$
> has a unique solution modulo the total product $M = m_1 m_2 \cdots m_k = \prod_{i=1}^k m_i$.

---

### 2. Constructive Proof and Algorithm

> **Proof (Existence):**
> Let $M = m_1 m_2 \cdots m_k$.
> For each $i \in \{1, 2, \dots, k\}$, define the partial product:
> $$M_i = \frac{M}{m_i} = m_1 \cdots m_{i-1} m_{i+1} \cdots m_k$$
> Note that $M_i$ is the product of all moduli except $m_i$.
> Since the moduli are pairwise coprime, $\gcd(M_i, m_i) = 1$.
> By Corollary 3.1, $M_i$ has a unique modular multiplicative inverse modulo $m_i$:
> $$M_i y_i \equiv 1 \pmod{m_i} \quad \text{for some } y_i \in \mathbb{Z}$$
> Now construct the integer:
> $$x = \sum_{i=1}^k a_i M_i y_i = a_1 M_1 y_1 + a_2 M_2 y_2 + \dots + a_k M_k y_k$$
> We check this candidate against each congruence $j \in \{1, \dots, k\}$:
> For any $i \ne j$, $m_j$ divides $M_i$, so $a_i M_i y_i \equiv 0 \pmod{m_j}$.
> For $i = j$, $M_j y_j \equiv 1 \pmod{m_j}$, so $a_j M_j y_j \equiv a_j (1) \equiv a_j \pmod{m_j}$.
> Thus:
> $$x \equiv 0 + \dots + a_j(1) + \dots + 0 \equiv a_j \pmod{m_j}$$
> This holds for all $j \in \{1, \dots, k\}$, proving existence.

> **Proof (Uniqueness):**
> Suppose $x_1$ and $x_2$ are two solutions to the system.
> Then $x_1 \equiv a_i \pmod{m_i}$ and $x_2 \equiv a_i \pmod{m_i}$ for all $i$.
> Thus $x_1 - x_2 \equiv 0 \pmod{m_i} \implies m_i \mid (x_1 - x_2)$ for all $i$.
> Since $m_1, \dots, m_k$ are pairwise coprime:
> $$\operatorname{lcm}(m_1, m_2, \dots, m_k) = m_1 m_2 \cdots m_k = M$$
> Therefore, $M \mid (x_1 - x_2) \implies x_1 \equiv x_2 \pmod M$. $\blacksquare$"""
            },
            {
                "secNumber": "3.5",
                "title": "Polynomial Congruences, Lagrange's Theorem & Hensel's Lemma",
                "content": r"""### 1. Lagrange's Theorem on Polynomial Roots Modulo a Prime

> **Theorem 3.8 (Lagrange's Theorem on Polynomial Congruences, 1768):**
> Let $p$ be a prime number and let:
> $$f(x) = c_n x^n + c_{n-1} x^{n-1} + \dots + c_1 x + c_0 \in \mathbb{Z}[x]$$
> be a polynomial of degree $n \ge 1$ with integer coefficients, such that $c_n \not\equiv 0 \pmod p$.
> Then the congruence:
> $$f(x) \equiv 0 \pmod p$$
> has at most $n$ incongruent solutions modulo $p$.

> **Proof (by Mathematical Induction on $n$):**
> **Base case ($n = 1$):**
> $f(x) = c_1 x + c_0 \equiv 0 \pmod p \iff c_1 x \equiv -c_0 \pmod p$.
> Since $c_1 \not\equiv 0 \pmod p$, $\gcd(c_1, p) = 1$.
> By Theorem 3.6, there is exactly $1$ solution modulo $p$.
>
> **Inductive Step:**
> Assume the theorem holds for all polynomials of degree $k < n$.
> Consider a polynomial $f(x)$ of degree $n$.
> If $f(x) \equiv 0 \pmod p$ has no solutions, the theorem holds vacuously ($0 \le n$).
> Suppose it has at least one root $x_0$, so $f(x_0) \equiv 0 \pmod p$.
> By the polynomial division algorithm:
> $$f(x) = (x - x_0) q(x) + R$$
> where $q(x)$ has degree $n - 1$ with leading coefficient $c_n$, and $R$ is a constant.
> Setting $x = x_0$: $f(x_0) = 0 + R \implies R = f(x_0) \equiv 0 \pmod p$.
> Thus:
> $$f(x) \equiv (x - x_0) q(x) \pmod p$$
> Let $x_1$ be any other root of $f(x) \equiv 0 \pmod p$ with $x_1 \not\equiv x_0 \pmod p$.
> Then:
> $$(x_1 - x_0) q(x_1) \equiv 0 \pmod p$$
> By Euclid's Lemma (Theorem 1.6), since $p \nmid (x_1 - x_0)$, we must have:
> $$q(x_1) \equiv 0 \pmod p$$
> Thus, every root of $f(x)$ distinct from $x_0$ must be a root of $q(x) \equiv 0 \pmod p$.
> Since $q(x)$ has degree $n - 1$, by the induction hypothesis it has at most $n - 1$ roots modulo $p$.
> Together with $x_0$, $f(x)$ has at most $1 + (n - 1) = n$ roots modulo $p$. $\blacksquare$

---

### 2. Hensel's Lemma ($p$-Adic Root Lifting)

Hensel's Lemma is the number-theoretic analogue of Newton's method for finding roots of functions.

> **Theorem 3.9 (Hensel's Lemma):**
> Let $f(x) \in \mathbb{Z}[x]$ and let $r$ be a solution to $f(x) \equiv 0 \pmod{p^k}$ for $k \ge 1$.
> Let $f'(x)$ denote the formal derivative of $f(x)$.
> If $f'(r) \not\equiv 0 \pmod p$, then $r$ lifts uniquely to a solution $s$ modulo $p^{k+1}$:
> $$s = r + t p^k \quad \text{where} \quad t \equiv -\frac{f(r)/p^k}{f'(r)} \pmod p$$"""
            }
        ],
        "problems": [
            {
                "id": "nt-prob-3-1",
                "tier": "Foundational",
                "title": "Solving Linear Congruences with Multiple Incongruent Solutions",
                "statement": r"""Consider the linear congruence:
$$14 x \equiv 21 \pmod{35}$$
1. Find $d = \gcd(14, 35)$ and verify the solvability criterion.
2. Determine how many mutually incongruent solutions exist modulo $35$.
3. Find all incongruent solutions modulo $35$ explicitly.""",
                "hints": [
                    "Compute gcd(14, 35) = 7. Verify whether 7 divides 21.",
                    "Divide through by 7 to obtain a simplified congruence: 2x = 3 (mod 5).",
                    "Add multiples of 35/7 = 5 to find all 7 incongruent solutions."
                ],
                "solution": r"""### 1. Solvability Verification
Let $a = 14, b = 21, m = 35$.
Compute the greatest common divisor:
$$d = \gcd(14, 35) = 7$$
Since $7 \mid 21$ ($21 = 7 \times 3$), the congruence is solvable! $\blacksquare$

---

### 2. Number of Incongruent Solutions
By Theorem 3.6, the number of mutually incongruent solutions modulo $35$ is equal to:
$$d = \gcd(14, 35) = 7$$
There are exactly **7 incongruent solutions** modulo $35$. $\blacksquare$

---

### 3. Finding the Complete Solution Set
Divide the congruence $14 x \equiv 21 \pmod{35}$ through by $d = 7$:
$$2 x \equiv 3 \pmod 5$$
Find the modular inverse of $2$ modulo $5$:
$$2 \times 3 = 6 \equiv 1 \pmod 5 \implies 2^{-1} \equiv 3 \pmod 5$$
Multiply through by $3$:
$$x \equiv 3 \times 3 = 9 \equiv 4 \pmod 5$$
Thus, a particular base solution is $x_0 = 4$.
The remaining $6$ incongruent solutions modulo $35$ are obtained by adding multiples of $m/d = 35/7 = 5$:
$$x_k = x_0 + 5 k = 4 + 5 k, \quad k \in \{0, 1, 2, 3, 4, 5, 6\}$$
Evaluating each:
- $k = 0 \implies x_0 = 4$
- $k = 1 \implies x_1 = 4 + 5 = 9$
- $k = 2 \implies x_2 = 4 + 10 = 14$
- $k = 3 \implies x_3 = 4 + 15 = 19$
- $k = 4 \implies x_4 = 4 + 20 = 24$
- $k = 5 \implies x_5 = 4 + 25 = 29$
- $k = 6 \implies x_6 = 4 + 30 = 34$

Thus, the complete set of incongruent solutions modulo $35$ is:
$$\{4, 9, 14, 19, 24, 29, 34\} \quad \blacksquare$$"""
            },
            {
                "id": "nt-prob-3-2",
                "tier": "Advanced",
                "title": "System of Three Congruences via Chinese Remainder Theorem",
                "statement": r"""Solve the system of simultaneous linear congruences:
$$\begin{cases}
x \equiv 2 \pmod 5 \\
x \equiv 4 \pmod 7 \\
x \equiv 3 \pmod{11}
\end{cases}$$
1. Verify that the moduli are pairwise coprime and compute the total modulus $M$.
2. Compute the partial products $M_i$ and their modular inverses $y_i \equiv M_i^{-1} \pmod{m_i}$.
3. Construct the unique minimal positive integer solution $x$ modulo $M$.""",
                "hints": [
                    "Moduli are 5, 7, 11. Check gcd(5, 7) = gcd(5, 11) = gcd(7, 11) = 1.",
                    "M = 5 * 7 * 11 = 385. Compute M_1 = 385/5 = 77, etc.",
                    "Solve 77 y_1 = 1 (mod 5), 55 y_2 = 1 (mod 7), 35 y_3 = 1 (mod 11)."
                ],
                "solution": r"""### 1. Coprimality and Total Modulus
The moduli are $m_1 = 5, m_2 = 7, m_3 = 11$.
Since $5, 7, 11$ are distinct prime numbers:
$$\gcd(5, 7) = 1, \quad \gcd(5, 11) = 1, \quad \gcd(7, 11) = 1$$
The total modulus is:
$$M = m_1 m_2 m_3 = 5 \times 7 \times 11 = 385 \quad \blacksquare$$

---

### 2. Partial Products and Modular Inverses
- For $m_1 = 5$:
  $$M_1 = \frac{385}{5} = 77$$
  We need $77 y_1 \equiv 1 \pmod 5$.
  Since $77 \equiv 2 \pmod 5$:
  $$2 y_1 \equiv 1 \pmod 5 \implies y_1 \equiv 3 \pmod 5 \quad (\text{since } 2 \times 3 = 6 \equiv 1)$$

- For $m_2 = 7$:
  $$M_2 = \frac{385}{7} = 55$$
  We need $55 y_2 \equiv 1 \pmod 7$.
  Since $55 \equiv 6 \equiv -1 \pmod 7$:
  $$-y_2 \equiv 1 \pmod 7 \implies y_2 \equiv -1 \equiv 6 \pmod 7$$

- For $m_3 = 11$:
  $$M_3 = \frac{385}{11} = 35$$
  We need $35 y_3 \equiv 1 \pmod{11}$.
  Since $35 \equiv 2 \pmod{11}$:
  $$2 y_3 \equiv 1 \equiv 12 \pmod{11} \implies y_3 \equiv 6 \pmod{11} \quad (\text{since } 2 \times 6 = 12 \equiv 1)$$

---

### 3. Synthesis of the Solution
Using the Chinese Remainder formula:
$$x = a_1 M_1 y_1 + a_2 M_2 y_2 + a_3 M_3 y_3$$
Substitute $a_1 = 2, a_2 = 4, a_3 = 3$:
$$x = 2(77)(3) + 4(55)(6) + 3(35)(6)$$
Compute each term:
$$2 \times 77 \times 3 = 462$$
$$4 \times 55 \times 6 = 1320$$
$$3 \times 35 \times 6 = 630$$
Summing them:
$$x = 462 + 1320 + 630 = 2412$$
Now reduce modulo $M = 385$:
$$2412 = 6 \times 385 + 102 \quad (6 \times 385 = 2310)$$
$$x \equiv 102 \pmod{385}$$
Verification:
- $102 = 20 \times 5 + 2 \equiv 2 \pmod 5 \quad \checkmark$
- $102 = 14 \times 7 + 4 \equiv 4 \pmod 7 \quad \checkmark$
- $102 = 9 \times 11 + 3 \equiv 3 \pmod{11} \quad \checkmark$

Thus, the unique solution modulo $385$ is:
$$x \equiv 102 \pmod{385} \quad \blacksquare$$"""
            },
            {
                "id": "nt-prob-3-3",
                "tier": "Honors / Proof Challenge",
                "title": "Hensel's Lemma: Lifting Quadratic Solutions to Prime Powers",
                "statement": r"""Consider the polynomial $f(x) = x^2 + 1$.
1. Solve the congruence $f(x) \equiv 0 \pmod 5$.
2. State Hensel's Lemma condition for lifting a root $r$ of $f(x) \equiv 0 \pmod{p^k}$ to modulo $p^{k+1}$.
3. Apply Hensel's Lemma to lift the root $r = 2$ of $x^2 + 1 \equiv 0 \pmod 5$ to an explicit solution modulo $25$ ($5^2$) and then to modulo $125$ ($5^3$).""",
                "hints": [
                    "Roots mod 5 are x = 2 and x = 3 because 2^2 + 1 = 5 = 0.",
                    "f'(x) = 2x. Check f'(2) = 4 != 0 (mod 5).",
                    "Use s = r + t * p^k with t = - [f(r)/p^k] * [f'(r)]^{-1} mod p."
                ],
                "solution": r"""### 1. Solving $x^2 + 1 \equiv 0 \pmod 5$
Evaluate $f(x) = x^2 + 1$ on the residue classes $\{0, 1, 2, 3, 4\}$ modulo $5$:
- $f(0) = 1 \not\equiv 0$
- $f(1) = 2 \not\equiv 0$
- $f(2) = 5 \equiv 0 \pmod 5$
- $f(3) = 10 \equiv 0 \pmod 5$
- $f(4) = 17 \equiv 2 \not\equiv 0$
Thus, the roots modulo $5$ are:
$$r \in \{2, 3\} \pmod 5 \quad \blacksquare$$

---

### 2. Hensel's Lifting Formula
Let $f(r) \equiv 0 \pmod{p^k}$. We seek $s = r + t p^k$ such that $f(s) \equiv 0 \pmod{p^{k+1}}$.
Using Taylor expansion about $r$:
$$f(r + t p^k) = f(r) + f'(r)(t p^k) + \frac{f''(r)}{2}(t p^k)^2 + \dots$$
Modulo $p^{k+1}$, all terms with $(p^k)^2 = p^{2k}$ vanish since $2k \ge k + 1$ for all $k \ge 1$.
Thus:
$$f(r + t p^k) \equiv f(r) + t p^k f'(r) \pmod{p^{k+1}}$$
Dividing through by $p^k$:
$$\frac{f(r)}{p^k} + t f'(r) \equiv 0 \pmod p \iff t f'(r) \equiv -\frac{f(r)}{p^k} \pmod p$$
If $f'(r) \not\equiv 0 \pmod p$, then $f'(r)$ is invertible modulo $p$, giving a unique value of $t$:
$$t \equiv -\left[\frac{f(r)}{p^k}\right] (f'(r))^{-1} \pmod p \quad \blacksquare$$

---

### 3. Step 1: Lifting $r = 2$ from mod $5$ to mod $25$ ($k = 1, p = 5$)
Here $r = 2, p = 5, k = 1$.
- $f(2) = 2^2 + 1 = 5 \implies \frac{f(2)}{5} = 1$.
- $f'(x) = 2x \implies f'(2) = 4 \equiv -1 \pmod 5$.
The inverse of $f'(2) = 4$ modulo $5$ is:
$$(f'(2))^{-1} = 4^{-1} \equiv 4 \equiv -1 \pmod 5$$
Compute $t$:
$$t \equiv -(1)(4) = -4 \equiv 1 \pmod 5$$
The lifted root modulo $25$ is:
$$s_1 = r + t p^1 = 2 + (1)(5) = 7$$
Verification modulo $25$:
$$f(7) = 7^2 + 1 = 49 + 1 = 50 = 2 \times 25 \equiv 0 \pmod{25} \quad \checkmark$$

---

### 4. Step 2: Lifting $s_1 = 7$ from mod $25$ to mod $125$ ($k = 2, p = 5$)
Here $r = 7, p = 5, k = 2$, so $p^k = 25$.
- $f(7) = 50 \implies \frac{f(7)}{25} = 2$.
- $f'(7) = 2(7) = 14 \equiv 4 \equiv -1 \pmod 5 \implies (f'(7))^{-1} \equiv 4 \equiv -1 \pmod 5$.
Compute $t$:
$$t \equiv -(2)(4) = -8 \equiv 2 \pmod 5$$
The lifted root modulo $125$ is:
$$s_2 = 7 + t p^2 = 7 + (2)(25) = 7 + 50 = 57$$
Verification modulo $125$:
$$f(57) = 57^2 + 1 = 3249 + 1 = 3250$$
Divide $3250$ by $125$:
$$3250 = 26 \times 125 \equiv 0 \pmod{125} \quad \checkmark$$
Thus, the lifted root modulo $125$ is $57$ (and its companion root is $125 - 57 = 68$). $\blacksquare$"""
            }
        ]
    }
    return u3

if __name__ == "__main__":
    u = get_unit3()
    print(f"Loaded Unit 3: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
