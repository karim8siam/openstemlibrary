# -*- coding: utf-8 -*-
"""
build_aa_unit6.py
Constructs Unit 6: Ring Theory: Subrings, Ideals, Quotient Rings & Ring Homomorphisms
"""

def get_unit6():
    u6 = {
        "number": 6,
        "title": "Ring Theory: Subrings, Ideals, Quotient Rings & Ring Homomorphisms",
        "leadSummary": "Comprehensive axiomatization of rings, commutative rings, integral domains, division rings and fields, characteristic of a ring, subrings, two-sided ideals, principal ideals, quotient rings R/I, ring homomorphisms, and the decisive distinction between prime ideals and maximal ideals.",
        "simulations": ["sim_aa_ring_ideals"],
        "sections": [
            {
                "secNumber": "6.1",
                "title": "Axioms of Rings, Ring Classes & Basic Properties",
                "content": r"""### 1. Axiomatic Definition of a Ring

A **ring** is an algebraic system endowed with two binary operations: addition $(+)$ and multiplication $(\cdot)$.

> **Definition 6.1 (Ring):**
> A set $R$ equipped with two binary operations $+: R \times R \to R$ and $\cdot: R \times R \to R$ is called a **ring** $(R, +, \cdot)$ if it satisfies:
> 1. **$(R, +)$ is an Abelian Group:**
>    - **Associativity:** $(a + b) + c = a + (b + c)$ for all $a, b, c \in R$.
>    - **Additive Identity:** There exists an element $0 \in R$ such that $a + 0 = 0 + a = a$ for all $a \in R$.
>    - **Additive Inverses:** For every $a \in R$, there exists $-a \in R$ such that $a + (-a) = (-a) + a = 0$.
>    - **Commutativity of Addition:** $a + b = b + a$ for all $a, b \in R$.
> 2. **$(R, \cdot)$ is a Semigroup:**
>    - **Associativity:** $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ for all $a, b, c \in R$.
> 3. **Distributive Laws (Addition over Multiplication):**
>    - **Left Distributivity:** $a \cdot (b + c) = a \cdot b + a \cdot c$ for all $a, b, c \in R$.
>    - **Right Distributivity:** $(a + b) \cdot c = a \cdot c + b \cdot c$ for all $a, b, c \in R$.

---

### 2. Ring Classifications

- **Ring with Unity (Identity):** There exists an element $1 \in R$ ($1 \ne 0$) such that $a \cdot 1 = 1 \cdot a = a$ for all $a \in R$.
- **Commutative Ring:** Multiplication is commutative: $a \cdot b = b \cdot a$ for all $a, b \in R$.
- **Division Ring (Skew Field):** A ring with unity $1 \ne 0$ in which every non-zero element $a \in R \setminus \{0\}$ has a multiplicative inverse $a^{-1} \in R$ such that $a \cdot a^{-1} = a^{-1} \cdot a = 1$. (e.g., the Quaternions $\mathbb{H}$).
- **Field:** A commutative division ring. (e.g., $\mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{F}_p$).

---

### 3. Fundamental Arithmetic Properties

> **Proposition 6.1 (Elementary Ring Arithmetic):**
> In any ring $(R, +, \cdot)$, for all $a, b, c \in R$:
> 1. $a \cdot 0 = 0 \cdot a = 0$.
> 2. $a \cdot (-b) = (-a) \cdot b = -(a \cdot b)$.
> 3. $(-a) \cdot (-b) = a \cdot b$.
> 4. $a \cdot (b - c) = a \cdot b - a \cdot c$.
> 5. If $R$ has unity $1$, then $(-1) \cdot a = -a$ and $(-1) \cdot (-1) = 1$.

#### Complete Proof of 1 and 2:
- **Proof of 1 ($a \cdot 0 = 0$):**
  We have $0 + 0 = 0$.
  Multiplying on the left by $a$:
  $$a \cdot (0 + 0) = a \cdot 0$$
  By left distributivity:
  $$a \cdot 0 + a \cdot 0 = a \cdot 0 = a \cdot 0 + 0$$
  By additive cancellation in the abelian group $(R, +)$:
  $$a \cdot 0 = 0 \quad \blacksquare$$
- **Proof of 2 ($a \cdot (-b) = -(a \cdot b)$):**
  Consider $a \cdot b + a \cdot (-b)$:
  $$a \cdot b + a \cdot (-b) = a \cdot (b + (-b)) = a \cdot 0 = 0$$
  By uniqueness of additive inverses in $(R, +)$, $a \cdot (-b)$ must be the additive inverse of $a \cdot b$:
  $$a \cdot (-b) = -(a \cdot b) \quad \blacksquare$$"""
            },
            {
                "secNumber": "6.2",
                "title": "Subrings, The Subring Test & Ring Characteristic",
                "content": r"""### 1. Subrings and the Subring Criterion

> **Definition 6.2 (Subring):**
> A subset $S \subseteq R$ of a ring $(R, +, \cdot)$ is a **subring** if $S$ is itself a ring under the operations of addition and multiplication restricted from $R$.

> **Theorem 6.1 (The Subring Test):**
> A non-empty subset $S \subseteq R$ is a subring of $R$ if and only if for all $a, b \in S$:
> 1. $a - b \in S$ (closed under subtraction / additive group test).
> 2. $a \cdot b \in S$ (closed under multiplication).
> If $R$ has unity $1_R$, a subring with unity often requires $1_R \in S$.

#### Proof:
By the one-step subgroup test (Theorem 2.1), condition 1 guarantees that $(S, +)$ is a subgroup of $(R, +)$. Since $(R, +)$ is abelian, $(S, +)$ is automatically abelian.
Condition 2 ensures that multiplication is a closed binary operation on $S$.
Associativity of multiplication and both distributive laws hold on $R$, and hence automatically hold on the subset $S$.
Therefore, $S$ satisfies all ring axioms. $\blacksquare$

---

### 2. The Characteristic of a Ring

> **Definition 6.3 (Characteristic):**
> The **characteristic** of a ring $R$, denoted $\text{char}(R)$, is the smallest positive integer $n \in \mathbb{Z}^+$ such that:
> $$n \cdot a = \underbrace{a + a + \dots + a}_{n \text{ times}} = 0, \quad \forall a \in R$$
> If no such positive integer exists, we define $\text{char}(R) = 0$.

> **Theorem 6.2 (Characteristic in Rings with Unity):**
> Let $R$ be a ring with unity $1_R$.
> 1. $\text{char}(R) = n > 0 \iff n$ is the additive order of $1_R$ in $(R, +)$.
> 2. If $R$ has no zero divisors (in particular, if $R$ is an integral domain or field), then $\text{char}(R)$ is either $0$ or a prime number $p$.

#### Complete Proof of Part 2:
Suppose $R$ has no zero divisors and $\text{char}(R) = n > 0$.
Suppose for contradiction that $n$ is composite: $n = a \cdot b$ where $1 < a, b < n$.
Then:
$$n \cdot 1_R = 0 \implies (a \cdot b) \cdot 1_R = 0$$
Using the distributive law in rings with unity:
$$(a \cdot 1_R) \cdot (b \cdot 1_R) = (a \cdot b) \cdot 1_R = n \cdot 1_R = 0$$
Since $R$ has no zero divisors, the product of two non-zero elements cannot be zero.
Therefore, either $a \cdot 1_R = 0$ or $b \cdot 1_R = 0$.
However, $1 < a, b < n$, and $n$ was defined as the **smallest** positive integer such that $n \cdot 1_R = 0$!
This is a direct contradiction.
Thus $n$ cannot be composite; $n$ must be a prime number $p$. $\blacksquare$"""
            },
            {
                "secNumber": "6.3",
                "title": "Ideals: Left, Right, Two-Sided & Principal Ideals",
                "content": r"""### 1. Why Subrings Fail to Form Quotients

In group theory, we needed *normal subgroups* to ensure that coset multiplication $(aN)(bN) = (ab)N$ was well-defined.
In ring theory, if $S$ is merely a subring, coset multiplication on $R/S$:
$$(r + S)(s + S) \stackrel{?}{=} rs + S$$
fails!
Let $s_1 \in S$. Then $(r + s_1)(s) = rs + s_1 s$. For $(rs + s_1 s) \in rs + S$, we require $s_1 s \in S$ for all $s \in R$.
A subring is only closed under multiplication by elements of *itself* ($S \cdot S \subseteq S$), but to absorb coset representatives, it must "absorb" multiplication from the entire ring $R$!
This motivates the concept of an **ideal**.

---

### 2. Definition of Ideals

> **Definition 6.4 (Ideals):**
> Let $R$ be a ring. A non-empty subset $I \subseteq R$ is called:
> 1. A **left ideal** if $(I, +) \le (R, +)$ and for all $r \in R, x \in I$, $r x \in I$ ($R \cdot I \subseteq I$).
> 2. A **right ideal** if $(I, +) \le (R, +)$ and for all $r \in R, x \in I$, $x r \in I$ ($I \cdot R \subseteq I$).
> 3. A **two-sided ideal** (or simply an **ideal**, denoted $I \trianglelefteq R$) if it is both a left ideal and a right ideal:
>    $$r x \in I \quad \text{and} \quad x r \in I, \quad \forall r \in R, \; x \in I$$

In a commutative ring, every left ideal is a right ideal, so all ideals are two-sided.

---

### 3. Principal Ideals

> **Definition 6.5 (Principal Ideal):**
> Let $R$ be a commutative ring with unity. The **principal ideal** generated by an element $a \in R$, denoted $\langle a \rangle$ or $(a)$, is:
> $$\langle a \rangle = R a = \{ r a : r \in R \}$$

More generally, the ideal generated by a set $X = \{a_1, a_2, \dots, a_k\}$ is:
$$\langle a_1, \dots, a_k \rangle = \{ r_1 a_1 + \dots + r_k a_k : r_i \in R \}$$

> **Theorem 6.3 (Ideals in $\mathbb{Z}$):**
> Every ideal in the ring of integers $\mathbb{Z}$ is principal. That is, for every ideal $I \trianglelefteq \mathbb{Z}$, there exists an integer $n \ge 0$ such that:
> $$I = n\mathbb{Z} = \langle n \rangle$$

#### Complete Proof:
If $I = \{0\}$, then $I = \langle 0 \rangle = 0\mathbb{Z}$.
Suppose $I \ne \{0\}$. Since $I$ is an additive subgroup, if $x \in I$ then $-x \in I$.
Thus $I$ contains positive integers.
By the Well-Ordering Principle of $\mathbb{Z}^+$, the set $I \cap \mathbb{Z}^+$ has a smallest element; call it $n$.
We claim $I = n\mathbb{Z}$:
- Since $n \in I$ and $I$ is an ideal, $k \cdot n \in I$ for all $k \in \mathbb{Z}$. Thus $n\mathbb{Z} \subseteq I$.
- Conversely, let $m \in I$ be any element.
  By the Division Algorithm in $\mathbb{Z}$:
  $$m = q \cdot n + r, \quad \text{where } 0 \le r < n$$
  Then $r = m - qn$.
  Since $m \in I$ and $qn \in I$, and $I$ is closed under subtraction:
  $$r = m - qn \in I$$
  If $r > 0$, then $r \in I \cap \mathbb{Z}^+$ with $r < n$, contradicting the minimality of $n$!
  Therefore, $r = 0$, which implies $m = qn \in n\mathbb{Z}$.
  Thus $I \subseteq n\mathbb{Z}$.
Combining both inclusions gives $I = n\mathbb{Z} = \langle n \rangle$. $\blacksquare$"""
            },
            {
                "secNumber": "6.4",
                "title": "Quotient Rings & The First Isomorphism Theorem for Rings",
                "content": r"""### 1. Construction of the Quotient Ring $R/I$

Let $I$ be a two-sided ideal of a ring $R$. The set of additive cosets:
$$R/I = \{ r + I : r \in R \}$$
forms a ring under the natural coset operations:
- **Addition:** $(a + I) + (b + I) = (a + b) + I$
- **Multiplication:** $(a + I) \cdot (b + I) = (ab) + I$

> **Theorem 6.4 (Well-Definedness and Ring Axioms of $R/I$):**
> If $I \trianglelefteq R$, then $R/I$ is a well-defined ring under coset addition and multiplication.
> Its zero element is $0 + I = I$.
> If $R$ has unity $1_R$, then $1_R + I$ is the unity of $R/I$.
> If $R$ is commutative, then $R/I$ is commutative.

#### Proof of Well-Definedness of Multiplication:
Suppose $a_1 + I = a_2 + I$ and $b_1 + I = b_2 + I$.
Then $a_2 = a_1 + i_1$ and $b_2 = b_1 + i_2$ for some $i_1, i_2 \in I$.
Compute the product $a_2 b_2$:
$$a_2 b_2 = (a_1 + i_1)(b_1 + i_2) = a_1 b_1 + a_1 i_2 + i_1 b_1 + i_1 i_2$$
Because $I$ is a two-sided ideal:
- $a_1 \in R$ and $i_2 \in I \implies a_1 i_2 \in I$.
- $b_1 \in R$ and $i_1 \in I \implies i_1 b_1 \in I$.
- $i_1 \in I$ and $i_2 \in I \implies i_1 i_2 \in I$.
Thus $i_3 = a_1 i_2 + i_1 b_1 + i_1 i_2 \in I$ (by additive closure of $I$).
Therefore:
$$a_2 b_2 = a_1 b_1 + i_3 \in a_1 b_1 + I \implies a_2 b_2 + I = a_1 b_1 + I$$
Thus coset multiplication is strictly well-defined! $\blacksquare$

---

### 2. Ring Homomorphisms & The First Isomorphism Theorem

> **Definition 6.6 (Ring Homomorphism):**
> A map $\phi: R \to S$ between rings is a **ring homomorphism** if for all $a, b \in R$:
> 1. $\phi(a + b) = \phi(a) + \phi(b)$
> 2. $\phi(a \cdot b) = \phi(a) \cdot \phi(b)$
> If $R$ and $S$ have unity, we require $\phi(1_R) = 1_S$.

The kernel is $\ker(\phi) = \{ r \in R : \phi(r) = 0_S \}$.
Just as in group theory, $\ker(\phi)$ is a two-sided ideal of $R$, and $\text{im}(\phi)$ is a subring of $S$.

> **Theorem 6.5 (First Isomorphism Theorem for Rings):**
> Let $\phi: R \to S$ be a ring homomorphism.
> Then:
> $$\frac{R}{\ker(\phi)} \cong \text{im}(\phi)$$
> via the isomorphism $\Phi(r + \ker(\phi)) = \phi(r)$.

#### Proof:
Since $\phi$ is an additive group homomorphism, by Theorem 5.2, $\Phi$ is an isomorphism of abelian groups $(R/\ker(\phi), +) \to (\text{im}(\phi), +)$.
It remains only to verify multiplicativity:
$$\Phi((a + \ker(\phi)) \cdot (b + \ker(\phi))) = \Phi(ab + \ker(\phi)) = \phi(ab) = \phi(a)\phi(b) = \Phi(a+\ker(\phi))\Phi(b+\ker(\phi))$$
Thus $\Phi$ is a ring isomorphism. $\blacksquare$"""
            },
            {
                "secNumber": "6.5",
                "title": "Prime Ideals vs. Maximal Ideals & Field Quotient Criteria",
                "content": r"""### 1. Definitions of Prime and Maximal Ideals

Let $R$ be a commutative ring with unity $1_R$.

> **Definition 6.7 (Prime Ideal):**
> A proper ideal $P \subsetneq R$ is called a **prime ideal** if whenever $a, b \in R$ with $a \cdot b \in P$, then either $a \in P$ or $b \in P$.

> **Definition 6.8 (Maximal Ideal):**
> A proper ideal $M \subsetneq R$ is called a **maximal ideal** if there are no ideals strictly between $M$ and $R$. That is, if $I \trianglelefteq R$ such that $M \subseteq I \subseteq R$, then either $I = M$ or $I = R$.

---

### 2. The Grand Quotient Characterization Theorems

The structural power of prime and maximal ideals lies in how they classify quotient rings:

> **Theorem 6.6 ($R/P$ is an Integral Domain $\iff P$ is Prime):**
> Let $R$ be a commutative ring with unity $1 \ne 0$, and let $P \subsetneq R$ be an ideal.
> Then $R/P$ is an **integral domain** if and only if $P$ is a **prime ideal**.

#### Proof:
- $(\implies)$ Suppose $R/P$ is an integral domain. Let $a, b \in R$ such that $ab \in P$.
  Then $(a + P)(b + P) = ab + P = 0 + P$.
  Since $R/P$ has no zero divisors, either $a + P = 0 + P$ or $b + P = 0 + P$.
  This means $a \in P$ or $b \in P$.
  Hence $P$ is prime.
- $(\impliedby)$ Suppose $P$ is prime. Since $P \ne R$, $1 + P \ne 0 + P$ in $R/P$, so $R/P$ is a commutative ring with non-zero unity.
  Suppose $(a + P)(b + P) = 0 + P$.
  Then $ab + P = 0 + P \implies ab \in P$.
  Because $P$ is prime, $a \in P$ or $b \in P$.
  Therefore, $a + P = 0 + P$ or $b + P = 0 + P$.
  Thus $R/P$ has no zero divisors, making $R/P$ an integral domain. $\blacksquare$

> **Theorem 6.7 ($R/M$ is a Field $\iff M$ is Maximal):**
> Let $R$ be a commutative ring with unity $1 \ne 0$, and let $M \subsetneq R$ be an ideal.
> Then $R/M$ is a **field** if and only if $M$ is a **maximal ideal**.

#### Complete Proof:
- $(\implies)$ Suppose $R/M$ is a field. Let $I \trianglelefteq R$ such that $M \subsetneq I \subseteq R$.
  Since $M \subsetneq I$, there exists an element $x \in I \setminus M$.
  Then $x + M \ne 0 + M$ in $R/M$.
  Because $R/M$ is a field, every non-zero element has a multiplicative inverse.
  Thus there exists $y + M \in R/M$ such that:
  $$(x + M)(y + M) = 1 + M \implies xy + M = 1 + M \implies 1 - xy \in M$$
  Since $M \subseteq I$, $1 - xy \in I$.
  Also $x \in I \implies xy \in I$ (by ideal property).
  Therefore:
  $$1 = (1 - xy) + xy \in I$$
  If an ideal contains the unity $1$, then for any $r \in R$, $r = r \cdot 1 \in I$, so $I = R$.
  Thus no ideal exists strictly between $M$ and $R$. $M$ is maximal.
- $(\impliedby)$ Suppose $M$ is maximal. Let $a + M \in R/M$ with $a + M \ne 0 + M$, so $a \notin M$.
  Consider the ideal generated by $M$ and $a$:
  $$I = M + \langle a \rangle = \{ m + r a : m \in M, r \in R \}$$
  Clearly $M \subseteq I$, and since $a = 0 + 1 \cdot a \in I$ with $a \notin M$, $M \subsetneq I$.
  By maximality of $M$, it must be that $I = R$.
  In particular, the unity $1 \in I$.
  Thus there exist $m \in M$ and $r \in R$ such that:
  $$m + r a = 1 \implies r a - 1 = -m \in M \implies ra + M = 1 + M$$
  $$(r + M)(a + M) = 1 + M$$
  Thus $r + M$ is the multiplicative inverse of $a + M$ in $R/M$.
  Since every non-zero element of $R/M$ is invertible, $R/M$ is a field. $\blacksquare$

> **Corollary 6.7.1 (Maximal Ideals are Prime):**
> In any commutative ring with unity, every maximal ideal is a prime ideal:
> $$M \text{ maximal} \implies M \text{ prime}$$

#### Proof:
If $M$ is maximal, then $R/M$ is a field.
Since every field is an integral domain, $R/M$ is an integral domain.
By Theorem 6.6, $M$ is a prime ideal. $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Ideals, Quotients and Matrix Rings in Direct Products",
                "statement": r"1. In the direct product ring $R = \mathbb{Z} \times \mathbb{Z}$, consider the subset $I = \{(a, 0) : a \in \mathbb{Z}\}$. Prove that $I$ is an ideal of $R$. Determine whether $I$ is a prime ideal or a maximal ideal by analyzing the quotient ring $R/I$. 2. In the ring of $2 \times 2$ real matrices $M_2(\mathbb{R})$, prove that the only two-sided ideals are $\{0\}$ and $M_2(\mathbb{R})$ itself (i.e., $M_2(\mathbb{R})$ is a simple ring).",
                "hints": [
                    "For Part 1, construct a projection homomorphism $\\pi: \\mathbb{Z} \\times \\mathbb{Z} \\to \\mathbb{Z}$ by $\\pi(a, b) = b$. Apply the First Isomorphism Theorem.",
                    "For Part 2, if a two-sided ideal $J$ contains a non-zero matrix $A$, multiply $A$ on the left and right by elementary matrices $E_{ij}$ to isolate a non-zero diagonal entry, then multiply to obtain the identity matrix $I_2$."
                ],
                "solution": r"""**Part 1: The Ideal $I = \mathbb{Z} \times \{0\}$ in $\mathbb{Z} \times \mathbb{Z}$**

Define the projection map:
$$\pi: \mathbb{Z} \times \mathbb{Z} \to \mathbb{Z}, \quad \pi(a, b) = b$$
1. **Ring Homomorphism:**
   - $\pi((a, b) + (c, d)) = \pi(a+c, b+d) = b + d = \pi(a, b) + \pi(c, d)$
   - $\pi((a, b) \cdot (c, d)) = \pi(ac, bd) = bd = \pi(a, b) \cdot \pi(c, d)$
   - $\pi(1, 1) = 1$
   Thus $\pi$ is a surjective ring homomorphism.
2. **Kernel:**
   $$\ker(\pi) = \{ (a, b) \in \mathbb{Z} \times \mathbb{Z} : \pi(a, b) = 0 \} = \{ (a, b) : b = 0 \} = I$$
   Since $I = \ker(\pi)$, $I$ is an ideal of $R$.
3. **Application of First Isomorphism Theorem:**
   By Theorem 6.5:
   $$\frac{\mathbb{Z} \times \mathbb{Z}}{I} \cong \text{im}(\pi) = \mathbb{Z}$$
4. **Prime vs. Maximal Analysis:**
   - The quotient ring is isomorphic to $\mathbb{Z}$.
   - $\mathbb{Z}$ is an integral domain (it has no zero divisors). Therefore, by Theorem 6.6, $I$ is a **prime ideal**.
   - However, $\mathbb{Z}$ is **not a field** (e.g., $2 \in \mathbb{Z}$ has no multiplicative inverse in $\mathbb{Z}$).
   - Therefore, by Theorem 6.7, $I$ is **not a maximal ideal**!
   (For example, $I \subsetneq \mathbb{Z} \times 2\mathbb{Z} \subsetneq \mathbb{Z} \times \mathbb{Z}$).

---

**Part 2: Simplicity of the Matrix Ring $M_2(\mathbb{R})$**

Let $J \trianglelefteq M_2(\mathbb{R})$ be a non-zero two-sided ideal. We must prove $J = M_2(\mathbb{R})$.
Since $J \ne \{0\}$, there exists a non-zero matrix $A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} \in J$.
At least one entry $a_{ij} \ne 0$.
Let $E_{kl}$ be the matrix with $1$ in row $k$, column $l$, and $0$ elsewhere.
Recall the fundamental matrix unit multiplication rule:
$$E_{pi} E_{kl} = \delta_{ik} E_{pl}$$
Now compute $E_{1i} A E_{j1}$:
$$E_{1i} A E_{j1} = E_{1i} \left( \sum_{r, s} a_{rs} E_{rs} \right) E_{j1} = a_{ij} E_{11}$$
Since $J$ is a two-sided ideal and $A \in J$, for all $P, Q \in M_2(\mathbb{R})$, $P A Q \in J$.
Choosing $P = E_{1i}$ and $Q = E_{j1}$:
$$a_{ij} E_{11} \in J$$
Since $a_{ij} \ne 0$ is a real scalar, we can multiply by the scalar $\frac{1}{a_{ij}} I_2 \in M_2(\mathbb{R})$:
$$E_{11} = \frac{1}{a_{ij}} (a_{ij} E_{11}) \in J$$
Now we can generate all matrix units:
- $E_{22} = E_{21} E_{11} E_{12} \in J$
Summing them:
$$I_2 = E_{11} + E_{22} \in J$$
Since the identity matrix $I_2 \in J$, for any matrix $M \in M_2(\mathbb{R})$:
$$M = M \cdot I_2 \in J \implies J = M_2(\mathbb{R})$$
Therefore, the only two-sided ideals of $M_2(\mathbb{R})$ are $\{0\}$ and $M_2(\mathbb{R})$. $\blacksquare$"""
            },
            {
                "tier": "Advanced",
                "title": "Ideals in $\\mathbb{R}[x]$ and $\\mathbb{Z}[x]$: Constructing $\\mathbb{C}$ and Distinguishing Prime from Maximal",
                "statement": r"1. In the polynomial ring $\mathbb{R}[x]$, let $I = \langle x^2 + 1 \rangle$. Prove that $I$ is a maximal ideal and deduce that $\mathbb{R}[x] / \langle x^2 + 1 \rangle \cong \mathbb{C}$. 2. In the polynomial ring $\mathbb{Z}[x]$, let $J = \langle x^2 + 1 \rangle$. Prove that $J$ is a prime ideal, but NOT a maximal ideal, by explicitly exhibiting an ideal strictly between $J$ and $\mathbb{Z}[x]$.",
                "hints": [
                    "For Part 1, define the evaluation homomorphism $\\text{ev}_i: \\mathbb{R}[x] \\to \\mathbb{C}$ sending $p(x) \\mapsto p(i)$. Compute its kernel and image.",
                    "For Part 2, compute the quotient $\\mathbb{Z}[x]/\\langle x^2+1 \\rangle \\cong \\mathbb{Z}[i]$. Is $\\mathbb{Z}[i]$ an integral domain? Is it a field?"
                ],
                "solution": r"""**Part 1: $\mathbb{R}[x] / \langle x^2 + 1 \rangle \cong \mathbb{C}$**

Define the evaluation homomorphism at the imaginary unit $i \in \mathbb{C}$:
$$\phi: \mathbb{R}[x] \to \mathbb{C}, \quad \phi(p(x)) = p(i)$$
1. **Homomorphism:**
   Evaluation preserves polynomial addition and multiplication:
   $$\phi(p + q) = p(i) + q(i) = \phi(p) + \phi(q)$$
   $$\phi(p \cdot q) = p(i) \cdot q(i) = \phi(p) \cdot \phi(q)$$
   $$\phi(1) = 1$$
2. **Surjectivity:**
   Any complex number has the form $a + bi$ with $a, b \in \mathbb{R}$.
   Consider the linear polynomial $p(x) = bx + a \in \mathbb{R}[x]$.
   Then $\phi(p(x)) = bi + a = a + bi$.
   Thus $\phi$ is surjective: $\text{im}(\phi) = \mathbb{C}$.
3. **Kernel:**
   $$\ker(\phi) = \{ p(x) \in \mathbb{R}[x] : p(i) = 0 \}$$
   Clearly $x^2 + 1 \in \ker(\phi)$ since $i^2 + 1 = -1 + 1 = 0$.
   Thus $\langle x^2 + 1 \rangle \subseteq \ker(\phi)$.
   Conversely, let $p(x) \in \ker(\phi)$.
   By the division algorithm in $\mathbb{R}[x]$:
   $$p(x) = q(x)(x^2 + 1) + (rx + s), \quad \text{where } r, s \in \mathbb{R}$$
   Evaluating at $x = i$:
   $$0 = p(i) = q(i)(i^2 + 1) + (ri + s) = 0 + (s + ri) \implies s + ri = 0$$
   Since $r, s \in \mathbb{R}$, this requires $s = 0$ and $r = 0$.
   Therefore, the remainder is identically zero, so $p(x) = q(x)(x^2 + 1) \in \langle x^2 + 1 \rangle$.
   Thus $\ker(\phi) = \langle x^2 + 1 \rangle$.
4. **Application of First Isomorphism Theorem:**
   By Theorem 6.5:
   $$\frac{\mathbb{R}[x]}{\langle x^2 + 1 \rangle} \cong \text{im}(\phi) = \mathbb{C}$$
   Since $\mathbb{C}$ is a field, Theorem 6.7 implies that $\langle x^2 + 1 \rangle$ is a **maximal ideal** of $\mathbb{R}[x]$. $\blacksquare$

---

**Part 2: The Ideal $J = \langle x^2 + 1 \rangle$ in $\mathbb{Z}[x]$**

Consider the same evaluation map restricted to integer polynomials:
$$\psi: \mathbb{Z}[x] \to \mathbb{Z}[i] = \{ a + bi : a, b \in \mathbb{Z} \}, \quad \psi(p(x)) = p(i)$$
The image is the ring of Gaussian integers $\mathbb{Z}[i]$.
By the identical division algorithm argument, $\ker(\psi) = \langle x^2 + 1 \rangle = J$.
By the First Isomorphism Theorem:
$$\frac{\mathbb{Z}[x]}{\langle x^2 + 1 \rangle} \cong \mathbb{Z}[i]$$

#### Analysis:
1. **Is $J$ a prime ideal?**
   $\mathbb{Z}[i]$ is a subring of the field $\mathbb{C}$.
   Since $\mathbb{C}$ has no zero divisors, $\mathbb{Z}[i]$ has no zero divisors, making $\mathbb{Z}[i]$ an **integral domain**.
   By Theorem 6.6, $J = \langle x^2 + 1 \rangle$ is a **prime ideal** in $\mathbb{Z}[x]$.
2. **Is $J$ a maximal ideal?**
   The quotient $\mathbb{Z}[i]$ is **not a field**!
   For example, $2 \in \mathbb{Z}[i]$ is not invertible, since $\frac{1}{2} \notin \mathbb{Z}[i]$.
   By Theorem 6.7, $J$ is **not a maximal ideal**.
3. **Explicit Intermediate Ideal:**
   Consider the ideal generated by $x^2 + 1$ and $2$:
   $$K = \langle 2, x^2 + 1 \rangle = \{ 2 f(x) + (x^2+1) g(x) : f, g \in \mathbb{Z}[x] \}$$
   - Clearly $J \subseteq K$.
   - $2 \in K$, but $2 \notin J$ (since any element in $J$ has degree $\ge 2$ or is 0). Thus $J \subsetneq K$.
   - Is $K = \mathbb{Z}[x]$? If $1 \in K$, then $2 f(x) + (x^2+1)g(x) = 1$. Evaluating at $x=i$ gives $2f(i) = 1 \implies f(i) = 1/2$, impossible in $\mathbb{Z}[i]$!
   Thus $J \subsetneq K \subsetneq \mathbb{Z}[x]$.
   This confirms explicitly that $J$ is not maximal. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "The Nilradical $\\text{Nil}(R)$ and Krull's Theorem on Prime Ideals",
                "statement": r"Let $R$ be a commutative ring with unity $1 \ne 0$. An element $x \in R$ is called nilpotent if $x^n = 0$ for some positive integer $n \ge 1$. 1. Prove that the set of all nilpotent elements, $\text{Nil}(R) = \{ x \in R : \exists n \ge 1, \; x^n = 0 \}$, forms an ideal of $R$ (called the nilradical of $R$). 2. Prove that if $P$ is any prime ideal of $R$, then $\text{Nil}(R) \subseteq P$. 3. Prove that the nilradical of $R$ is equal to the intersection of all prime ideals of $R$: $\text{Nil}(R) = \bigcap_{P \text{ prime}} P$.",
                "hints": [
                    "For Part 1, use the Binomial Theorem for $(x+y)^{n+m}$, which holds because $R$ is commutative.",
                    "For Part 2, if $x^n = 0 \\in P$, use induction on $n$ with the prime ideal definition.",
                    "For Part 3, to show the reverse inclusion $\\bigcap P \\subseteq \\text{Nil}(R)$, assume $x \\notin \\text{Nil}(R)$, consider the multiplicative set $S = \\{1, x, x^2, \\dots\\}$, and use Zorn's Lemma on the set of ideals disjoint from $S$."
                ],
                "solution": r"""**Part 1: Proof that $\text{Nil}(R)$ is an Ideal**

1. **Non-emptiness:** $0^1 = 0 \implies 0 \in \text{Nil}(R)$.
2. **Additive closure:** Let $x, y \in \text{Nil}(R)$. Then there exist $n, m \ge 1$ such that $x^n = 0$ and $y^m = 0$.
   Since $R$ is commutative, we expand $(x - y)^{n + m}$ using the Binomial Theorem:
   $$(x - y)^{n + m} = \sum_{k=0}^{n+m} \binom{n+m}{k} x^k (-y)^{n+m-k}$$
   For each term in the sum:
   - If $k \ge n$, then $x^k = x^{k-n} x^n = x^{k-n} \cdot 0 = 0$.
   - If $k < n$, then $(n + m - k) > (n + m - n) = m$, so $(-y)^{n+m-k} = \pm y^{n+m-k-m} y^m = 0$.
   Thus every single term in the sum is $0$!
   Therefore, $(x - y)^{n+m} = 0$, which proves $x - y \in \text{Nil}(R)$.
3. **Ideal absorption:** Let $r \in R$ and $x \in \text{Nil}(R)$ with $x^n = 0$.
   Since $R$ is commutative:
   $$(rx)^n = r^n x^n = r^n \cdot 0 = 0$$
   Thus $rx \in \text{Nil}(R)$.
Therefore, $\text{Nil}(R)$ is an ideal of $R$. $\blacksquare$

---

**Part 2: $\text{Nil}(R) \subseteq P$ for every Prime Ideal $P$**

Let $P$ be a prime ideal of $R$, and let $x \in \text{Nil}(R)$.
Then $x^n = 0$ for some $n \ge 1$.
Since $0 \in P$, we have $x^n \in P$.
We prove $x \in P$ by induction on $n$:
- If $n = 1$, $x \in P$ immediately.
- Assume that for any $k < n$, $x^k \in P \implies x \in P$.
- Write $x^n = x \cdot x^{n-1} \in P$.
- Since $P$ is a prime ideal, $a b \in P \implies a \in P$ or $b \in P$.
- Here $x \in P$ or $x^{n-1} \in P$.
- In either case, by induction hypothesis, $x \in P$.
Therefore, every nilpotent element belongs to every prime ideal:
$$\text{Nil}(R) \subseteq \bigcap_{P \text{ prime}} P \quad \blacksquare$$

---

**Part 3: Krull's Theorem: $\text{Nil}(R) = \bigcap_{P \text{ prime}} P$**

To prove $\bigcap_{P \text{ prime}} P \subseteq \text{Nil}(R)$, we prove the contrapositive:
Suppose $f \in R$ and $f \notin \text{Nil}(R)$.
We must construct a prime ideal $P$ such that $f \notin P$.

Consider the multiplicative set generated by powers of $f$:
$$S = \{ f^k : k \ge 0 \} = \{ 1, f, f^2, f^3, \dots \}$$
Since $f \notin \text{Nil}(R)$, $0 \notin S$.
Let $\Sigma$ be the collection of all ideals of $R$ that are disjoint from $S$:
$$\Sigma = \{ I \trianglelefteq R : I \cap S = \emptyset \}$$
- **$\Sigma \ne \emptyset$:** The zero ideal $\{0\} \in \Sigma$, because $0 \notin S$.
- **Partially ordered set:** $\Sigma$ is partially ordered by set inclusion $\subseteq$.
- **Zorn's Lemma hypothesis:** Let $\{I_\alpha\}_{\alpha \in A}$ be a totally ordered chain of ideals in $\Sigma$.
  Let $J = \bigcup_{\alpha \in A} I_\alpha$.
  $J$ is an ideal of $R$, and if $J \cap S \ne \emptyset$, then some $f^k \in I_\alpha$, contradicting $I_\alpha \in \Sigma$.
  Thus $J \in \Sigma$, serving as an upper bound for the chain.
By Zorn's Lemma, $\Sigma$ contains a **maximal element**; call it $P$.
By definition of $\Sigma$, $P \cap S = \emptyset$, so in particular $f \notin P$.

#### We claim $P$ is a prime ideal of $R$:
Suppose for contradiction that $P$ is not prime.
Then there exist $a, b \in R$ such that $ab \in P$, but $a \notin P$ and $b \notin P$.
Consider the strictly larger ideals:
$$I_a = P + \langle a \rangle \quad \text{and} \quad I_b = P + \langle b \rangle$$
Since $a, b \notin P$, we have $P \subsetneq I_a$ and $P \subsetneq I_b$.
By the maximality of $P$ in $\Sigma$, neither $I_a$ nor $I_b$ can belong to $\Sigma$!
Therefore, both must intersect $S$:
$$\exists s_1 = f^u \in I_a \quad \text{and} \quad \exists s_2 = f^v \in I_b$$
Thus we can write:
$$f^u = p_1 + r_1 a \quad \text{and} \quad f^v = p_2 + r_2 b \quad (p_1, p_2 \in P, \; r_1, r_2 \in R)$$
Now multiply these two elements:
$$f^{u+v} = (p_1 + r_1 a)(p_2 + r_2 b) = p_1 p_2 + p_1 r_2 b + p_2 r_1 a + r_1 r_2 (ab)$$
Examine each term:
- $p_1 p_2 \in P$ (since $p_1 \in P$).
- $p_1 r_2 b \in P$ (since $p_1 \in P$).
- $p_2 r_1 a \in P$ (since $p_2 \in P$).
- $r_1 r_2 (ab) \in P$ (since by hypothesis $ab \in P$!).
Thus the entire sum lies in $P$:
$$f^{u+v} \in P$$
However, $f^{u+v} \in S$, which means $P \cap S \ne \emptyset$, a direct contradiction!

Therefore, our assumption was false: $P$ **must be a prime ideal**.
Since $f \notin P$, we have found a prime ideal $P$ not containing $f$.
Consequently, $f \notin \bigcap_{P \text{ prime}} P$.
This completes the proof:
$$\text{Nil}(R) = \bigcap_{P \text{ prime}} P \quad \blacksquare$$"""
            }
        ]
    }
    return u6

if __name__ == "__main__":
    u = get_unit6()
    print("Unit 6 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
