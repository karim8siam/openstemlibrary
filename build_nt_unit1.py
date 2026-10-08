# -*- coding: utf-8 -*-
"""
build_nt_unit1.py
Constructs Unit 1: Divisibility Theory & The Fundamental Theorem of Arithmetic
"""

def get_unit1():
    u1 = {
        "number": 1,
        "title": "Divisibility Theory & The Fundamental Theorem of Arithmetic",
        "leadSummary": "Foundations of elementary number theory: the Well-Ordering Principle of natural numbers, the Division Algorithm with unique quotient and remainder, greatest common divisors and Bézout's Identity, the Extended Euclidean Algorithm, complete parametric characterization of linear Diophantine equations $ax + by = c$, Euclid's Lemma, Euclid's proof of the infinitude of primes, and the Fundamental Theorem of Arithmetic establishing the existence and uniqueness of prime factorizations.",
        "simulations": ["sim_nt_euclidean_bezout"],
        "sections": [
            {
                "secNumber": "1.1",
                "title": "The Well-Ordering Principle & The Division Algorithm",
                "content": r"""### 1. The Well-Ordering Principle of $\mathbb{N}$

Number theory rests upon the foundational structure of the set of integers $\mathbb{Z} = \{0, \pm 1, \pm 2, \dots\}$ and positive integers (natural numbers) $\mathbb{N} = \{1, 2, 3, \dots\}$.

> **Axiom 1.1 (The Well-Ordering Principle):**
> Every non-empty subset $S \subseteq \mathbb{N}$ contains a least element (or minimum element):
> $$\exists m \in S \quad \text{such that} \quad m \le s \quad \forall s \in S$$

The Well-Ordering Principle is logically equivalent to the Principle of Mathematical Induction and the Principle of Strong Mathematical Induction. It provides the fundamental deductive bedrock for proving existence, termination of algorithms, and impossibility via the method of infinite descent.

---

### 2. Divisibility in the Integers

> **Definition 1.1 (Divisibility):**
> Let $a, b \in \mathbb{Z}$ with $a \ne 0$. We say that $a$ **divides** $b$ (or that $b$ is a **multiple** of $a$), denoted $a \mid b$, if there exists an integer $c \in \mathbb{Z}$ such that:
> $$b = a c$$
> If $a$ does not divide $b$, we write $a \nmid b$.

> **Theorem 1.1 (Elementary Properties of Divisibility):**
> For all $a, b, c, d \in \mathbb{Z}$:
> 1. Reflexivity: $a \mid a$ for all $a \ne 0$.
> 2. Transitivity: If $a \mid b$ and $b \mid c$, then $a \mid c$.
> 3. Linearity: If $a \mid b$ and $a \mid c$, then $a \mid (bx + cy)$ for any integers $x, y \in \mathbb{Z}$.
> 4. Cancellation: If $a \mid b$, then $ac \mid bc$ for all $c \ne 0$.
> 5. Size constraint: If $a \mid b$ and $b \ne 0$, then $|a| \le |b|$.

---

### 3. The Division Algorithm

> **Theorem 1.2 (The Division Algorithm):**
> Let $a, b \in \mathbb{Z}$ with $b > 0$. Then there exist unique integers $q, r \in \mathbb{Z}$ such that:
> $$a = b q + r \quad \text{with} \quad 0 \le r < b$$
> Here $q$ is called the **quotient** ($q = \lfloor a/b \rfloor$) and $r$ is called the **remainder** ($r = a \bmod b$).

> **Proof (Existence):**
> Consider the set of non-negative integers of the form $a - b k$:
> $$S = \{a - b k : k \in \mathbb{Z} \text{ and } a - b k \ge 0\}$$
> First, we verify that $S$ is non-empty.
> - If $a \ge 0$, setting $k = 0$ gives $a - b(0) = a \ge 0 \in S$.
> - If $a < 0$, setting $k = a$ gives $a - b a = a(1 - b)$. Since $b \ge 1$, $1 - b \le 0$, so $a(1 - b) \ge 0 \in S$.
> Since $S \subseteq \mathbb{Z}_{\ge 0}$ is non-empty, by the Well-Ordering Principle, $S$ has a smallest element, which we denote by $r \ge 0$.
> Since $r \in S$, there exists some $q \in \mathbb{Z}$ such that:
> $$r = a - b q \implies a = b q + r$$
> We must now show that $r < b$.
> Suppose for contradiction that $r \ge b$.
> Then consider the integer:
> $$r' = r - b = (a - b q) - b = a - b(q + 1)$$
> Since $r \ge b$, $r' \ge 0$, so $r' \in S$.
> But $b > 0 \implies r' = r - b < r$, which contradicts the minimality of $r$ in $S$!
> Thus, $0 \le r < b$.

> **Proof (Uniqueness):**
> Suppose there exist two representations:
> $$a = b q_1 + r_1 \quad \text{and} \quad a = b q_2 + r_2$$
> with $0 \le r_1 < b$ and $0 \le r_2 < b$.
> Equating the two expressions:
> $$b q_1 + r_1 = b q_2 + r_2 \implies b(q_1 - q_2) = r_2 - r_1$$
> Taking absolute values:
> $$b |q_1 - q_2| = |r_2 - r_1|$$
> Since $0 \le r_1 < b$ and $0 \le r_2 < b$, we have $-b < r_2 - r_1 < b$, which implies:
> $$|r_2 - r_1| < b$$
> Thus:
> $$b |q_1 - q_2| < b \implies |q_1 - q_2| < 1$$
> Since $|q_1 - q_2|$ is a non-negative integer, we must have $|q_1 - q_2| = 0$, so $q_1 = q_2$.
> Consequently, $r_2 - r_1 = b(0) = 0 \implies r_1 = r_2$. $\blacksquare$"""
            },
            {
                "secNumber": "1.2",
                "title": "Greatest Common Divisors, Bézout's Identity & The Euclidean Algorithm",
                "content": r"""### 1. The Greatest Common Divisor

> **Definition 1.2 (Greatest Common Divisor):**
> Let $a, b \in \mathbb{Z}$, not both zero. The **greatest common divisor** of $a$ and $b$, denoted $\gcd(a, b)$ or simply $(a, b)$, is the unique positive integer $d \in \mathbb{N}$ satisfying:
> 1. Common divisor: $d \mid a$ and $d \mid b$.
> 2. Greatest property: If $c \in \mathbb{Z}$ is any common divisor of $a$ and $b$ ($c \mid a$ and $c \mid b$), then $c \le d$ (and $c \mid d$).
> If $\gcd(a, b) = 1$, the integers $a$ and $b$ are called **relatively prime** (or **coprime**).

---

### 2. Bézout's Identity

> **Theorem 1.3 (Bézout's Identity, 1730–1783):**
> Let $a, b \in \mathbb{Z}$, not both zero. Then their greatest common divisor $d = \gcd(a, b)$ can be expressed as a linear combination of $a$ and $b$:
> $$d = \gcd(a, b) = a x + b y \quad \text{for some } x, y \in \mathbb{Z}$$
> In fact, $\gcd(a, b)$ is the smallest positive integer in the set of all integer linear combinations:
> $$\mathcal{L}(a, b) = \{a u + b v : u, v \in \mathbb{Z}\}$$

> **Proof:**
> Consider the set of all positive linear combinations:
> $$S = \{a u + b v : u, v \in \mathbb{Z} \text{ and } a u + b v > 0\}$$
> Since not both $a, b$ are zero, $a^2 + b^2 = a(a) + b(b) > 0 \in S$, so $S$ is non-empty.
> By the Well-Ordering Principle, $S$ contains a smallest element $d = a x + b y > 0$.
> We claim that $d = \gcd(a, b)$.
> 1. **Show $d \mid a$:**
>    By the Division Algorithm, divide $a$ by $d$:
>    $$a = q d + r \quad \text{with } 0 \le r < d$$
>    Substitute $d = ax + by$:
>    $$r = a - q d = a - q(a x + b y) = a(1 - q x) + b(-q y)$$
>    Thus, $r$ is an integer linear combination of $a$ and $b$.
>    If $r > 0$, then $r \in S$ and $r < d$, contradicting the minimality of $d$ in $S$!
>    Therefore, we must have $r = 0$, which proves $d \mid a$.
> 2. **Show $d \mid b$:**
>    An identical argument shows that $d \mid b$.
> 3. **Show $d$ is greatest:**
>    Let $c$ be any common divisor of $a$ and $b$ ($c \mid a$ and $c \mid b$).
>    By linearity of divisibility (Theorem 1.1), $c \mid (a x + b y) = d$.
>    Since $d > 0$, this implies $c \le |c| \le d$.
> Hence, $d = \gcd(a, b) = a x + b y$. $\blacksquare$

> **Corollary 1.1 (Coprimality Criterion):**
> Two integers $a$ and $b$ are coprime ($\gcd(a, b) = 1$) if and only if there exist integers $x, y \in \mathbb{Z}$ such that:
> $$a x + b y = 1$$

---

### 3. The Euclidean Algorithm

The Euclidean algorithm is an ancient, highly efficient iterative method for computing $\gcd(a, b)$ and the Bézout coefficients $(x, y)$.

> **Lemma 1.1 (Euclidean Invariance):**
> If $a = b q + r$, then:
> $$\gcd(a, b) = \gcd(b, r)$$

> **Proof:**
> Let $d_1 = \gcd(a, b)$ and $d_2 = \gcd(b, r)$.
> Since $d_1 \mid a$ and $d_1 \mid b$, we have $d_1 \mid (a - b q) = r$, so $d_1$ is a common divisor of $b$ and $r \implies d_1 \mid d_2$.
> Conversely, since $d_2 \mid b$ and $d_2 \mid r$, we have $d_2 \mid (b q + r) = a$, so $d_2$ is a common divisor of $a$ and $b \implies d_2 \mid d_1$.
> Since both $d_1, d_2 > 0$, we conclude $d_1 = d_2$. $\blacksquare$

By repeatedly applying the Division Algorithm:
$$\begin{aligned}
a &= b q_1 + r_1, \quad & 0 < r_1 < b \\
b &= r_1 q_2 + r_2, \quad & 0 < r_2 < r_1 \\
r_1 &= r_2 q_3 + r_3, \quad & 0 < r_3 < r_2 \\
&\;\; \vdots \\
r_{k-2} &= r_{k-1} q_k + r_k, \quad & 0 < r_k < r_{k-1} \\
r_{k-1} &= r_k q_{k+1} + 0
\end{aligned}$$
Since $b > r_1 > r_2 > \dots \ge 0$ is a strictly decreasing sequence of non-negative integers, the process must terminate in a finite number of steps with remainder $0$.
The last non-zero remainder $r_k$ is precisely $\gcd(a, b)$!
Back-substituting through the steps yields the Bézout coefficients $x, y$ (Extended Euclidean Algorithm)."""
            },
            {
                "secNumber": "1.3",
                "title": "Linear Diophantine Equations in Two Variables",
                "content": r"""### 1. Formulation of the Problem

A **Diophantine equation** is an algebraic equation in which integer solutions are sought.
The simplest Diophantine equation is the linear equation in two unknowns:
$$a x + b y = c$$
where $a, b, c \in \mathbb{Z}$ are given integer constants, with $a, b$ not both zero.

---

### 2. The Solvability Criterion

> **Theorem 1.4 (Solvability of $a x + b y = c$):**
> The linear Diophantine equation $a x + b y = c$ has an integer solution $(x, y) \in \mathbb{Z}^2$ if and only if:
> $$d = \gcd(a, b) \mid c$$

> **Proof:**
> **Forward direction ($\implies$):**
> Suppose an integer solution $(x_0, y_0)$ exists, so that $a x_0 + b y_0 = c$.
> Let $d = \gcd(a, b)$. By definition, $d \mid a$ and $d \mid b$.
> By linearity of divisibility, $d \mid (a x_0 + b y_0)$, which means $d \mid c$.
>
> **Reverse direction ($\impliedby$):**
> Suppose $d \mid c$. Then $c = d \cdot k$ for some integer $k \in \mathbb{Z}$.
> By Bézout's Identity (Theorem 1.3), there exist integers $u, v \in \mathbb{Z}$ such that:
> $$a u + b v = d$$
> Multiplying both sides by $k$:
> $$a(u k) + b(v k) = d k = c$$
> Setting $x_0 = u k$ and $y_0 = v k$ gives an explicit integer solution $(x_0, y_0)$. $\blacksquare$

---

### 3. Complete Solution Family

> **Theorem 1.5 (General Solution Family):**
> If $d = \gcd(a, b) \mid c$ and $(x_0, y_0)$ is any particular integer solution to $a x + b y = c$, then all integer solutions are given parametrically by:
> $$x = x_0 + \left(\frac{b}{d}\right) t, \qquad y = y_0 - \left(\frac{a}{d}\right) t \quad (t \in \mathbb{Z})$$

> **Proof:**
> First, verify that every pair $(x, y)$ of this form is a solution:
> $$a\left[ x_0 + \frac{b}{d} t \right] + b\left[ y_0 - \frac{a}{d} t \right] = (a x_0 + b y_0) + \left(\frac{ab}{d} - \frac{ba}{d}\right)t = c + 0 = c$$
>
> Conversely, let $(x, y)$ be any arbitrary solution, so $a x + b y = c$.
> Subtracting $a x_0 + b y_0 = c$ gives:
> $$a(x - x_0) + b(y - y_0) = 0 \iff a(x - x_0) = -b(y - y_0)$$
> Dividing through by $d = \gcd(a, b)$:
> $$\left(\frac{a}{d}\right)(x - x_0) = -\left(\frac{b}{d}\right)(y - y_0)$$
> Note that $\gcd\left(\frac{a}{d}, \frac{b}{d}\right) = 1$.
> Therefore, $\frac{b}{d} \mid \left(\frac{a}{d}\right)(x - x_0)$.
> By Euclid's Lemma (Theorem 1.6), since $\gcd\left(\frac{a}{d}, \frac{b}{d}\right) = 1$, we must have:
> $$\frac{b}{d} \;\middle|\; (x - x_0) \implies x - x_0 = \left(\frac{b}{d}\right) t \quad \text{for some } t \in \mathbb{Z}$$
> Substituting this back:
> $$\left(\frac{a}{d}\right)\left(\frac{b}{d} t\right) = -\left(\frac{b}{d}\right)(y - y_0) \implies y - y_0 = -\left(\frac{a}{d}\right) t$$
> Thus:
> $$x = x_0 + \left(\frac{b}{d}\right) t, \qquad y = y_0 - \left(\frac{a}{d}\right) t \quad \blacksquare$$"""
            },
            {
                "secNumber": "1.4",
                "title": "Prime Numbers, Euclid's Lemma & The Infinitude of Primes",
                "content": r"""### 1. Definition of Prime and Composite Numbers

> **Definition 1.3 (Prime and Composite Integers):**
> An integer $p > 1$ is called a **prime number** if its only positive divisors are $1$ and $p$.
> An integer $n > 1$ that is not prime is called a **composite number**.
> The number $1$ is considered neither prime nor composite (it is a unit).

---

### 2. Euclid's Lemma

> **Theorem 1.6 (Euclid's Lemma):**
> If $p$ is a prime number and $p \mid a b$, then $p \mid a$ or $p \mid b$.

> **Proof:**
> Suppose $p \mid a b$ and $p \nmid a$.
> Since $p$ is prime, its only positive divisors are $1$ and $p$.
> Because $p \nmid a$, the greatest common divisor $\gcd(a, p)$ must be $1$.
> By Bézout's Identity (Theorem 1.3), there exist integers $x, y \in \mathbb{Z}$ such that:
> $$a x + p y = 1$$
> Multiply this equation across by $b$:
> $$(a b) x + p (b y) = b$$
> Since $p \mid a b$, there exists an integer $k$ such that $a b = p k$.
> Substituting this in:
> $$(p k) x + p (b y) = b \implies p(k x + b y) = b$$
> Since $k x + b y \in \mathbb{Z}$, this directly shows that $p \mid b$. $\blacksquare$

> **Corollary 1.2 (Generalization to Finite Products):**
> If a prime $p$ divides a product of integers $a_1 a_2 \cdots a_k$, then $p \mid a_i$ for at least one index $i \in \{1, 2, \dots, k\}$.
> In particular, if $p \mid q_1 q_2 \cdots q_k$ where all $q_i$ are primes, then $p = q_i$ for some $i$.

---

### 3. Euclid's Proof of the Infinitude of Primes

> **Theorem 1.7 (Euclid, Book IX, Proposition 20):**
> There are infinitely many prime numbers.

> **Proof:**
> Suppose for contradiction that there are only finitely many prime numbers, which can be enumerated completely as:
> $$p_1, p_2, p_3, \dots, p_k$$
> Consider the integer:
> $$N = p_1 p_2 p_3 \cdots p_k + 1$$
> Since $N > 1$, $N$ must possess at least one prime factor $q$ (by the Well-Ordering Principle, the smallest divisor of $N$ greater than $1$ is prime).
> Since $p_1, \dots, p_k$ is the list of all primes, $q$ must be equal to $p_i$ for some $1 \le i \le k$.
> Consequently, $q \mid (p_1 p_2 \cdots p_k)$.
> But by definition, $q \mid N = (p_1 p_2 \cdots p_k + 1)$.
> By linearity of divisibility:
> $$q \mid (N - p_1 p_2 \cdots p_k) = 1$$
> But the only positive divisor of $1$ is $1$, so $q = 1$, which contradicts the fact that $q$ is a prime ($q > 1$)!
> Thus, the collection of primes cannot be finite. $\blacksquare$"""
            },
            {
                "secNumber": "1.5",
                "title": "The Fundamental Theorem of Arithmetic & Canonical Factorization",
                "content": r"""### 1. Statement of the Fundamental Theorem of Arithmetic

The Fundamental Theorem of Arithmetic (Unique Factorization Theorem) states that every integer greater than $1$ can be represented uniquely as a product of prime numbers.

> **Theorem 1.8 (The Fundamental Theorem of Arithmetic):**
> Every integer $n > 1$ can be represented as a product of prime numbers:
> $$n = p_1 p_2 \cdots p_k$$
> Furthermore, this factorization is **unique** up to the order of the prime factors.

---

### 2. Line-by-Line Mathematical Proof

> **Proof of Existence (by Strong Mathematical Induction):**
> **Base case ($n = 2$):** $2$ is prime, so it is a product of a single prime.
> **Inductive hypothesis:** Assume every integer $k$ with $2 \le k < n$ can be factored into a product of primes.
> **Inductive step for $n$:**
> - If $n$ is prime, we are done.
> - If $n$ is composite, there exist integers $a, b$ such that $n = a b$ with $1 < a < n$ and $1 < b < n$.
>   By the inductive hypothesis, both $a$ and $b$ can be factored into primes:
>   $$a = p_1 p_2 \cdots p_r, \qquad b = q_1 q_2 \cdots q_s$$
>   Multiplying them gives:
>   $$n = a b = p_1 p_2 \cdots p_r q_1 q_2 \cdots q_s$$
>   which is a prime factorization of $n$.
> This proves existence for all $n \ge 2$.

> **Proof of Uniqueness:**
> Suppose for contradiction that there exists at least one integer greater than $1$ that possesses two distinct prime factorizations.
> By the Well-Ordering Principle, let $m$ be the **smallest** such integer:
> $$m = p_1 p_2 \cdots p_r = q_1 q_2 \cdots q_s$$
> where all $p_i$ and $q_j$ are primes.
> Clearly, $p_1 \mid (p_1 p_2 \cdots p_r) = m$, so:
> $$p_1 \mid (q_1 q_2 \cdots q_s)$$
> By Corollary 1.2 (Euclid's Lemma), $p_1$ must divide some $q_j$.
> Since $q_j$ is prime, its only divisors are $1$ and $q_j$, so:
> $$p_1 = q_j$$
> Relabeling indices if necessary, let $p_1 = q_1$.
> Dividing both sides of the factorization of $m$ by $p_1 = q_1$:
> $$m' = \frac{m}{p_1} = p_2 p_3 \cdots p_r = q_2 q_3 \cdots q_s$$
> If $r = 1$, then $m = p_1 = q_1 \cdots q_s$, which forces $s = 1$ and $p_1 = q_1$, so the factorizations were identical.
> If $r > 1$, then $m' < m$.
> But $m'$ now has two distinct prime factorizations!
> This directly contradicts the minimality of $m$.
> Therefore, every integer $n > 1$ has a strictly unique prime factorization. $\blacksquare$

---

### 3. Canonical Form and Divisor Formulas

Collecting identical primes together, every integer $n > 1$ has a unique canonical representation:
$$n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k} = \prod_{i=1}^k p_i^{a_i} \quad (a_i \ge 1, \; p_1 < p_2 < \dots < p_k)$$
For two integers $a = \prod p_i^{\alpha_i}$ and $b = \prod p_i^{\beta_i}$:
$$\gcd(a, b) = \prod_{i=1}^k p_i^{\min(\alpha_i, \beta_i)}, \qquad \operatorname{lcm}(a, b) = \prod_{i=1}^k p_i^{\max(\alpha_i, \beta_i)}$$
Since $\min(\alpha, \beta) + \max(\alpha, \beta) = \alpha + \beta$, this yields the classical relation:
$$\gcd(a, b) \cdot \operatorname{lcm}(a, b) = |a b|$$"""
            }
        ],
        "problems": [
            {
                "id": "nt-prob-1-1",
                "tier": "Foundational",
                "title": "Extended Euclidean Algorithm & Bézout Coefficients",
                "statement": r"""Apply the Extended Euclidean Algorithm to the integers $a = 1044$ and $b = 468$:
1. Compute the greatest common divisor $d = \gcd(1044, 468)$ using the Division Algorithm.
2. Express $d$ as an integer linear combination:
   $$d = 1044 x + 468 y$$
   finding explicit integer values for the Bézout coefficients $x$ and $y$.
3. Compute the least common multiple $\operatorname{lcm}(1044, 468)$.""",
                "hints": [
                    "Perform successive divisions 1044 = 468 * q_1 + r_1.",
                    "Trace backwards from the last non-zero remainder to express gcd as a combination.",
                    "Use the identity gcd(a, b) * lcm(a, b) = a * b."
                ],
                "solution": r"""### 1. The Euclidean Algorithm
Divide $1044$ by $468$:
$$1044 = 2 \times 468 + 108 \quad (r_1 = 108)$$
Divide $468$ by $108$:
$$468 = 4 \times 108 + 36 \quad (r_2 = 36)$$
Divide $108$ by $36$:
$$108 = 3 \times 36 + 0 \quad (r_3 = 0)$$
Since the last non-zero remainder is $36$:
$$\gcd(1044, 468) = 36 \quad \blacksquare$$

---

### 2. Back-Substitution for Bézout Coefficients
From the second division equation:
$$36 = 468 - 4 \times 108$$
From the first division equation, $108 = 1044 - 2 \times 468$.
Substitute this into the expression for $36$:
$$36 = 468 - 4 \times (1044 - 2 \times 468)$$
$$36 = 468 - 4 \times 1044 + 8 \times 468$$
$$36 = 1044 \times (-4) + 468 \times (9)$$
Thus, the Bézout coefficients are:
$$x = -4, \qquad y = 9$$
Verification:
$$1044(-4) + 468(9) = -4176 + 4212 = 36 \quad \blacksquare$$

---

### 3. Least Common Multiple
Using $\gcd(a, b) \times \operatorname{lcm}(a, b) = a \times b$:
$$\operatorname{lcm}(1044, 468) = \frac{1044 \times 468}{36} = \frac{1044 \times 468}{36} = 1044 \times 13 = 13572 \quad \blacksquare$$"""
            },
            {
                "id": "nt-prob-1-2",
                "tier": "Advanced",
                "title": "Positive Integer Solutions to a Linear Diophantine Equation",
                "statement": r"""Consider the linear Diophantine equation:
$$17 x + 23 y = 2026$$
1. Verify that the equation is solvable in integers.
2. Find a particular integer solution $(x_0, y_0)$ using Bézout's identity.
3. Write down the complete general solution in integers $(x(t), y(t))$.
4. Determine all solutions in **positive integers** ($x > 0, y > 0$) and find the total number of such solutions.""",
                "hints": [
                    "Check gcd(17, 23). Since 17 and 23 are primes, gcd(17, 23) = 1.",
                    "Find u, v such that 17u + 23v = 1, then multiply by 2026.",
                    "Set x(t) > 0 and y(t) > 0 to find the allowable range for integer parameter t."
                ],
                "solution": r"""### 1. Solvability Verification
Both $17$ and $23$ are prime numbers, so:
$$\gcd(17, 23) = 1$$
Since $1 \mid 2026$, the equation is guaranteed to have infinitely many integer solutions. $\blacksquare$

---

### 2. Particular Solution via Bézout's Identity
Apply the Euclidean algorithm to $23$ and $17$:
$$23 = 1 \times 17 + 6$$
$$17 = 2 \times 6 + 5$$
$$6 = 1 \times 5 + 1$$
Back-substituting for $1$:
$$1 = 6 - 1 \times 5 = 6 - (17 - 2 \times 6) = 3 \times 6 - 17$$
$$1 = 3 \times (23 - 17) - 17 = 3 \times 23 - 4 \times 17 = 17(-4) + 23(3)$$
Multiplying through by $2026$:
$$17(-4 \times 2026) + 23(3 \times 2026) = 2026$$
$$17(-8104) + 23(6078) = 2026$$
A particular integer solution is:
$$x_0 = -8104, \qquad y_0 = 6078 \quad \blacksquare$$

---

### 3. General Integer Solution Family
With $d = \gcd(17, 23) = 1$:
$$x(t) = -8104 + 23 t$$
$$y(t) = 6078 - 17 t \quad (t \in \mathbb{Z}) \quad \blacksquare$$

---

### 4. Positive Integer Solutions ($x > 0, y > 0$)
We require simultaneously:
$$x(t) > 0 \implies -8104 + 23 t > 0 \implies 23 t > 8104 \implies t > \frac{8104}{23} \approx 352.3478$$
$$y(t) > 0 \implies 6078 - 17 t > 0 \implies 17 t < 6078 \implies t < \frac{6078}{17} \approx 357.5294$$
Since $t$ must be an integer, the allowable range for $t$ is:
$$353 \le t \le 357$$
This gives exactly $5$ solutions in positive integers, corresponding to $t \in \{353, 354, 355, 356, 357\}$:
- For $t = 353$: $x = -8104 + 23(353) = 15$, $y = 6078 - 17(353) = 77 \implies (15, 77)$
- For $t = 354$: $x = 15 + 23 = 38$, $y = 77 - 17 = 60 \implies (38, 60)$
- For $t = 355$: $x = 38 + 23 = 61$, $y = 60 - 17 = 43 \implies (61, 43)$
- For $t = 356$: $x = 61 + 23 = 84$, $y = 43 - 17 = 26 \implies (84, 26)$
- For $t = 357$: $x = 84 + 23 = 107$, $y = 26 - 17 = 9 \implies (107, 9)$

Thus, there are exactly **5 positive integer solutions**:
$$\{(15, 77), (38, 60), (61, 43), (84, 26), (107, 9)\} \quad \blacksquare$$"""
            },
            {
                "id": "nt-prob-1-3",
                "tier": "Honors / Proof Challenge",
                "title": "Rigorous Proof of Euclid's Lemma & Factorization Uniqueness",
                "statement": r"""Let $\mathbb{Z}$ denote the ring of integers.
1. Prove that if $a, b \in \mathbb{Z}$ with $\gcd(a, b) = 1$ and $a \mid bc$, then $a \mid c$.
2. Use this result to prove **Euclid's Lemma**: if $p$ is prime and $p \mid a_1 a_2 \cdots a_n$, then $p \mid a_i$ for some $1 \le i \le n$.
3. Prove rigorously that the prime factorization of any integer $n > 1$ into primes:
   $$n = p_1 p_2 \cdots p_r = q_1 q_2 \cdots q_s$$
   is unique up to permutation of factors (i.e., $r = s$ and each $p_i = q_{\pi(i)}$ for some permutation $\pi$).""",
                "hints": [
                    "By Bezout, gcd(a, b) = 1 implies ax + by = 1. Multiply by c.",
                    "Proceed by induction on n for the prime product extension.",
                    "Assume there exists a minimal counterexample and derive a contradiction."
                ],
                "solution": r"""### 1. Proof of Gauss's Lemma ($\gcd(a, b) = 1$ and $a \mid bc \implies a \mid c$)
Suppose $\gcd(a, b) = 1$ and $a \mid bc$.
By Bézout's Identity (Theorem 1.3), there exist integers $x, y \in \mathbb{Z}$ such that:
$$a x + b y = 1$$
Multiply this equation across by $c$:
$$a c x + b c y = c$$
Since $a \mid bc$, there exists an integer $k \in \mathbb{Z}$ such that $bc = a k$.
Substituting this into the equation:
$$a c x + (a k) y = c \implies a(c x + k y) = c$$
Since $c x + k y$ is an integer, this proves directly that $a \mid c$. $\blacksquare$

---

### 2. Generalization to Finite Products
Let $p$ be a prime and $p \mid a_1 a_2 \cdots a_n$.
We proceed by induction on $n \ge 1$.
- **Base case ($n = 1$):** $p \mid a_1$, which is trivially true.
- **Base case ($n = 2$):** If $p \mid a_1 a_2$, either $p \mid a_1$ (done) or $p \nmid a_1$.
  If $p \nmid a_1$, since $p$ is prime, $\gcd(p, a_1) = 1$.
  By Part 1 with $a = p, b = a_1, c = a_2$, since $\gcd(p, a_1) = 1$ and $p \mid a_1 a_2$, we have $p \mid a_2$.
- **Inductive Step:** Suppose the result holds for products of length $k \ge 2$.
  Consider $p \mid (a_1 \cdots a_k) a_{k+1}$.
  By the $n=2$ case, either $p \mid a_{k+1}$ (done) or $p \mid (a_1 \cdots a_k)$.
  By the induction hypothesis, $p \mid a_i$ for some $1 \le i \le k$.
Thus, by mathematical induction, $p \mid a_i$ for some $1 \le i \le n$. $\blacksquare$

---

### 3. Uniqueness of Prime Factorization
Suppose the set of integers $n > 1$ with non-unique prime factorizations is non-empty:
$$S = \{n \in \mathbb{Z}_{>1} : n \text{ has at least two distinct prime factorizations}\}$$
By the Well-Ordering Principle of $\mathbb{N}$, $S$ must contain a minimal element $m \in S$.
Let:
$$m = p_1 p_2 \cdots p_r = q_1 q_2 \cdots q_s$$
be two distinct factorizations, where $p_i$ and $q_j$ are primes arranged in non-decreasing order:
$$p_1 \le p_2 \le \dots \le p_r, \qquad q_1 \le q_2 \le \dots \le q_s$$
Since $p_1 \mid m = q_1 q_2 \cdots q_s$, by Part 2, $p_1 \mid q_j$ for some $j \in \{1, \dots, s\}$.
Since $q_j$ is prime, its only divisors are $1$ and $q_j$, so $p_1 = q_j$.
Since $q_1 \le q_j$, we have $p_1 \ge q_1$.
By symmetry, $q_1 \mid p_1 p_2 \cdots p_r \implies q_1 \mid p_i$ for some $i \implies q_1 = p_i \ge p_1$.
Since $p_1 \ge q_1$ and $q_1 \ge p_1$, we must have:
$$p_1 = q_1$$
Now divide $m$ by $p_1 = q_1$:
$$m' = \frac{m}{p_1} = p_2 \cdots p_r = q_2 \cdots q_s$$
If $r = 1$, then $m = p_1$, so $q_1 \cdots q_s = p_1$, forcing $s = 1$ and $q_1 = p_1$, which means the original factorizations were identical, contradicting $m \in S$.
If $r > 1$, then $1 < m' < m$.
Because $m$ was the **smallest** element with distinct factorizations, $m' \notin S$.
Thus, $m'$ has a **unique** prime factorization!
This implies $r - 1 = s - 1 \implies r = s$, and $p_i = q_i$ for all $i = 2, \dots, r$.
Together with $p_1 = q_1$, this proves:
$$r = s \quad \text{and} \quad p_i = q_i \quad \forall i \in \{1, \dots, r\}$$
This contradicts the assumption that the two factorizations of $m$ were distinct!
Hence, $S = \emptyset$, and the prime factorization of every integer $n > 1$ is strictly unique. $\blacksquare$"""
            }
        ]
    }
    return u1

if __name__ == "__main__":
    u = get_unit1()
    print(f"Loaded Unit 1: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
