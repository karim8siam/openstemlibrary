# -*- coding: utf-8 -*-
"""
build_aa_unit7.py
Constructs Unit 7: Integral Domains, Euclidean Domains, PIDs & UFDs
"""

def get_unit7():
    u7 = {
        "number": 7,
        "title": "Integral Domains, Euclidean Domains, PIDs & UFDs",
        "leadSummary": "Deep structural analysis of commutativity and factorization: zero divisors, integral domains, field of fractions construction Q(R), units, associates, irreducibles vs primes, Euclidean domains (ED), principal ideal domains (PID), unique factorization domains (UFD), complete proofs of ED => PID => UFD, and explicit counterexamples delineating every boundary.",
        "simulations": ["sim_aa_domain_hierarchy"],
        "sections": [
            {
                "secNumber": "7.1",
                "title": "Zero Divisors, Integral Domains & Finite Domains",
                "content": r"""### 1. Zero Divisors and Integral Domains

In standard high-school arithmetic, if $a \cdot b = 0$, we conclude that $a = 0$ or $b = 0$. In general abstract rings, this property can fail dramatically (e.g., in $\mathbb{Z}_6$, $2 \cdot 3 \equiv 0 \pmod 6$ even though neither $2$ nor $3$ is zero).

> **Definition 7.1 (Zero Divisor):**
> Let $R$ be a ring. A non-zero element $a \in R \setminus \{0\}$ is called a **left zero divisor** (resp. **right zero divisor**) if there exists a non-zero element $b \in R \setminus \{0\}$ such that $a \cdot b = 0$ (resp. $b \cdot a = 0$).

> **Definition 7.2 (Integral Domain):**
> A commutative ring $R$ with unity $1_R \ne 0$ is called an **integral domain** if it contains no zero divisors:
> $$a \cdot b = 0 \implies a = 0 \quad \text{or} \quad b = 0$$

Examples of integral domains: $\mathbb{Z}$, any field $\mathbb{F}$ (such as $\mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{Z}_p$), polynomial rings over domains $R[x]$, and the Gaussian integers $\mathbb{Z}[i]$.
Non-examples: $\mathbb{Z}_n$ for composite $n$, $M_n(\mathbb{R})$ for $n \ge 2$, and direct products $R_1 \times R_2$.

---

### 2. The Cancellation Law

> **Theorem 7.1 (Equivalence of Domain Property and Cancellation):**
> A commutative ring $R$ with $1 \ne 0$ is an integral domain if and only if the **cancellation law** holds:
> $$\text{For all } a, b, c \in R \text{ with } a \ne 0: \quad a \cdot b = a \cdot c \implies b = c$$

#### Proof:
- $(\implies)$ Let $R$ be an integral domain. If $ab = ac$, then $ab - ac = 0 \implies a(b - c) = 0$.
  Since $a \ne 0$ and $R$ has no zero divisors, $b - c = 0 \implies b = c$.
- $(\impliedby)$ Suppose cancellation holds. If $ab = 0$, and $a \ne 0$, we write $ab = a \cdot 0$.
  By cancellation of $a$, $b = 0$.
  Thus $R$ contains no zero divisors. $\blacksquare$

---

### 3. Finite Integral Domains are Fields

A remarkable bridge connecting finiteness, algebra, and number theory:

> **Theorem 7.2 (Finite Integral Domains are Fields):**
> Every finite integral domain is a field.

#### Complete Proof:
Let $D$ be a finite integral domain with unity $1 \ne 0$, and let $n = |D| < \infty$.
Let $a \in D$ be any non-zero element ($a \ne 0$).
We must show that $a$ has a multiplicative inverse $a^{-1} \in D$.

Consider the left-multiplication mapping:
$$\lambda_a: D \to D, \quad \lambda_a(x) = a \cdot x$$
1. **Injectivity of $\lambda_a$:**
   Suppose $\lambda_a(x) = \lambda_a(y)$. Then $ax = ay$.
   Since $a \ne 0$ and $D$ is an integral domain, the cancellation law (Theorem 7.1) implies $x = y$.
   Thus $\lambda_a$ is an injective mapping.
2. **Surjectivity by Pigeonhole Principle:**
   Since $D$ is a **finite** set, any injective map from $D$ to itself is automatically surjective!
   Therefore, $\lambda_a(D) = D$.
3. **Existence of Inverse:**
   Since $\lambda_a$ is surjective and $1 \in D$, there must exist some element $b \in D$ such that:
   $$\lambda_a(b) = 1 \implies a \cdot b = 1$$
   Since $D$ is commutative, $b \cdot a = a \cdot b = 1$.
   Thus $b = a^{-1}$ is the multiplicative inverse of $a$.
Since every non-zero element of $D$ is invertible, $D$ is a field. $\blacksquare$"""
            },
            {
                "secNumber": "7.2",
                "title": "The Field of Fractions Construction $Q(R)$",
                "content": r"""### 1. Generalizing $\mathbb{Z} \hookrightarrow \mathbb{Q}$

Just as the rational numbers $\mathbb{Q}$ are formed from the integers $\mathbb{Z}$ by introducing formal fractions $a/b$ ($b \ne 0$), any integral domain $R$ can be canonically embedded into a minimal field called its **field of fractions** (or quotient field), denoted $\text{Frac}(R)$ or $Q(R)$.

---

### 2. Formal Rigorous Construction

Let $R$ be an integral domain. Let $S = R \setminus \{0\}$.
Consider the Cartesian product $R \times S = \{ (a, b) : a \in R, b \in R, b \ne 0 \}$.

> **Definition 7.3 (Fraction Equivalence Relation):**
> Define a binary relation $\sim$ on $R \times S$ by:
> $$(a, b) \sim (c, d) \iff a \cdot d = b \cdot c$$

> **Lemma 7.1:** $\sim$ is an equivalence relation on $R \times S$.

#### Proof of Transitivity (where domain property is essential):
Suppose $(a, b) \sim (c, d)$ and $(c, d) \sim (e, f)$.
Then $ad = bc$ and $cf = de$.
Multiply the first equation by $f$ and the second by $b$:
$$(ad)f = (bc)f \implies adf = bcf$$
$$(cf)b = (de)b \implies bcf = bde$$
Equating them yields:
$$adf = bde \implies (af - be)d = 0$$
Since $d \in S$, $d \ne 0$.
Because $R$ is an integral domain (no zero divisors), $(af - be)d = 0$ forces:
$$af - be = 0 \implies af = be \implies (a, b) \sim (e, f) \quad \blacksquare$$

We denote the equivalence class of $(a, b)$ by $\frac{a}{b}$ or $[a, b]$, and the set of classes by $Q(R) = (R \times S) / \sim$.

---

### 3. Field Operations on $Q(R)$

Define addition and multiplication on $Q(R)$ by:
$$\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}, \qquad \frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}$$
Notice $bd \ne 0$ because $R$ has no zero divisors, so $bd \in S$.
Both operations are easily verified to be well-defined.

> **Theorem 7.3 (Properties of $Q(R)$):**
> 1. $(Q(R), +, \cdot)$ is a field, with zero element $0_{Q(R)} = \frac{0}{1}$ and unity $1_{Q(R)} = \frac{1}{1}$.
> 2. The inverse of any non-zero element $\frac{a}{b} \ne \frac{0}{1}$ ($a \ne 0$) is $\left(\frac{a}{b}\right)^{-1} = \frac{b}{a}$.
> 3. The canonical map $\iota: R \to Q(R)$ defined by $\iota(r) = \frac{r}{1}$ is an injective ring homomorphism (embedding).
> 4. **Universal Property:** If $K$ is any field and $\phi: R \hookrightarrow K$ is an injective ring homomorphism, there exists a unique field homomorphism $\widetilde{\phi}: Q(R) \hookrightarrow K$ such that $\widetilde{\phi} \circ \iota = \phi$, given by $\widetilde{\phi}\left(\frac{a}{b}\right) = \phi(a)\phi(b)^{-1}$."""
            },
            {
                "secNumber": "7.3",
                "title": "Divisibility, Units, Irreducibles vs. Primes",
                "content": r"""### 1. Divisibility, Units and Associates

Let $R$ be an integral domain with unity $1$.

> **Definition 7.4 (Divisibility, Units, Associates):**
> 1. **Divisibility:** For $a, b \in R$, we say $a$ divides $b$ (written $a \mid b$) if there exists $c \in R$ such that $b = ac$. Equivalently, $\langle b \rangle \subseteq \langle a \rangle$.
> 2. **Unit:** An element $u \in R$ is a **unit** if $u \mid 1$, meaning $\exists v \in R$ such that $uv = 1$. The set of all units forms a multiplicative group $R^\times = U(R)$.
> 3. **Associates:** Elements $a, b \in R$ are called **associates** (written $a \sim b$) if $a = ub$ for some unit $u \in R^\times$. Equivalently, $a \mid b$ and $b \mid a \iff \langle a \rangle = \langle b \rangle$.

---

### 2. Irreducible Elements vs. Prime Elements

In elementary arithmetic in $\mathbb{Z}$, the terms "prime" and "irreducible" are used interchangeably. In general rings, however, they represent two fundamentally distinct concepts!

> **Definition 7.5 (Irreducible Element):**
> A non-zero element $p \in R \setminus \{0\}$ that is not a unit ($p \notin R^\times$) is called **irreducible** if whenever $p = ab$ for $a, b \in R$, then either $a$ is a unit or $b$ is a unit.
> *(Irreducible elements cannot be factored non-trivially.)*

> **Definition 7.6 (Prime Element):**
> A non-zero element $p \in R \setminus \{0\}$ that is not a unit ($p \notin R^\times$) is called **prime** if whenever $p \mid ab$ for $a, b \in R$, then $p \mid a$ or $p \mid b$.
> *(Prime elements preserve the Euclid's Lemma divisibility property; equivalently, the principal ideal $\langle p \rangle$ is a prime ideal.)*

---

### 3. The Prime $\implies$ Irreducible Theorem

> **Theorem 7.4 (Primes are Always Irreducible in a Domain):**
> In any integral domain $R$, every prime element is irreducible:
> $$p \text{ is prime} \implies p \text{ is irreducible}$$

#### Complete Proof:
Let $p \in R$ be a prime element. Suppose $p = ab$ for some $a, b \in R$.
Since $p = ab$, $p \mid ab$.
Because $p$ is prime, by Definition 7.6, $p \mid a$ or $p \mid b$.
Without loss of generality, assume $p \mid a$.
Then there exists $c \in R$ such that $a = pc$.
Substituting this into $p = ab$:
$$p = (pc)b = p(cb)$$
Using the cancellation law in the domain $R$ (since $p \ne 0$):
$$1 = cb$$
This equation proves that $b$ is a unit in $R$ (with inverse $c$)!
Similarly, if $p \mid b$, then $a$ is a unit.
Thus any factorization of $p$ involves a unit factor.
Therefore, $p$ is irreducible. $\blacksquare$

> **Warning (The Converse Fails in General!):**
> An irreducible element is **NOT necessarily prime** in an arbitrary integral domain!
> In $\mathbb{Z}[\sqrt{-5}]$, the element $2$ is irreducible, but $2 \mid (1+\sqrt{-5})(1-\sqrt{-5}) = 6$, while $2 \nmid (1+\sqrt{-5})$ and $2 \nmid (1-\sqrt{-5})$.
> Thus $2$ is irreducible but NOT prime!"""
            },
            {
                "secNumber": "7.4",
                "title": "Euclidean Domains, Principal Ideal Domains & UFDs",
                "content": r"""### 1. Euclidean Domains (ED)

A **Euclidean Domain** is an integral domain equipped with a notion of "size" that allows division with remainder.

> **Definition 7.7 (Euclidean Domain):**
> An integral domain $R$ is called a **Euclidean Domain (ED)** if there exists a function $d: R \setminus \{0\} \to \mathbb{Z}_{\ge 0}$ (called a **Euclidean norm** or **degree function**) such that:
> 1. For all $a, b \in R \setminus \{0\}$, $d(a) \le d(ab)$.
> 2. (**Division Algorithm**): For any $a \in R$ and $b \in R \setminus \{0\}$, there exist $q, r \in R$ such that:
>    $$a = q b + r, \quad \text{where either } r = 0 \text{ or } d(r) < d(b)$$

Classic Examples:
- $\mathbb{Z}$ with $d(n) = |n|$.
- Polynomial ring $F[x]$ over any field $F$ with $d(f) = \deg(f)$.
- Gaussian integers $\mathbb{Z}[i]$ with $d(a+bi) = a^2 + b^2$.

---

### 2. Principal Ideal Domains (PID)

> **Definition 7.8 (Principal Ideal Domain):**
> An integral domain $R$ is called a **Principal Ideal Domain (PID)** if every ideal of $R$ is principal (generated by a single element):
> $$\forall I \trianglelefteq R, \quad \exists a \in R \text{ such that } I = \langle a \rangle$$

Examples: $\mathbb{Z}, F[x], \mathbb{Z}[i]$. Non-example: $\mathbb{Z}[x]$ (the ideal $\langle 2, x \rangle$ is not principal).

---

### 3. Unique Factorization Domains (UFD)

> **Definition 7.9 (Unique Factorization Domain):**
> An integral domain $R$ is called a **Unique Factorization Domain (UFD)** if:
> 1. (**Factorization Existence**): Every non-zero non-unit $a \in R \setminus (R^\times \cup \{0\})$ can be written as a product of irreducible elements:
>    $$a = p_1 p_2 \cdots p_r$$
> 2. (**Uniqueness up to Associates**): If $a = p_1 p_2 \cdots p_r = q_1 q_2 \cdots q_s$ are two factorizations into irreducibles, then $r = s$, and after reordering, $p_i$ is associate to $q_i$ for all $i$ ($p_i = u_i q_i$ for some $u_i \in R^\times$)."""
            },
            {
                "secNumber": "7.5",
                "title": "The Grand Domain Hierarchy: $\\text{ED} \\implies \\text{PID} \\implies \\text{UFD}$",
                "content": r"""### 1. The Master Hierarchy Chain

The fundamental relationships among commutative domains form a strict linear hierarchy:
$$\text{Fields} \subsetneq \text{Euclidean Domains (ED)} \subsetneq \text{Principal Ideal Domains (PID)} \subsetneq \text{Unique Factorization Domains (UFD)} \subsetneq \text{Integral Domains (ID)}$$

---

### 2. Proof 1: Every Euclidean Domain is a PID ($\text{ED} \implies \text{PID}$)

> **Theorem 7.5:** If $R$ is a Euclidean Domain, then $R$ is a Principal Ideal Domain.

#### Complete Proof:
Let $I \trianglelefteq R$ be any ideal.
- If $I = \{0\}$, then $I = \langle 0 \rangle$, which is principal.
- If $I \ne \{0\}$, consider the set of norms of non-zero elements:
  $$S = \{ d(x) : x \in I \setminus \{0\} \} \subseteq \mathbb{Z}_{\ge 0}$$
  Since $I \ne \{0\}$, $S$ is a non-empty subset of non-negative integers.
  By the Well-Ordering Principle of $\mathbb{Z}$, $S$ contains a minimum element.
  Choose $b \in I \setminus \{0\}$ such that $d(b) = \min(S)$.

We claim $I = \langle b \rangle$:
- Since $b \in I$ and $I$ is an ideal, $rb \in I$ for all $r \in R$, so $\langle b \rangle \subseteq I$.
- Now let $a \in I$ be any element.
  By the Division Algorithm in the Euclidean Domain $R$, there exist $q, r \in R$ such that:
  $$a = q b + r, \quad \text{where } r = 0 \text{ or } d(r) < d(b)$$
  Rearranging gives:
  $$r = a - qb$$
  Since $a \in I$ and $b \in I$, and $I$ is an ideal, $r \in I$.
  If $r \ne 0$, then $d(r) < d(b)$, which contradicts the minimality of $d(b)$ among all non-zero elements in $I$!
  Therefore, $r$ must be $0$.
  This implies $a = qb \in \langle b \rangle$.
  Thus $I \subseteq \langle b \rangle$.
Combining both inclusions gives $I = \langle b \rangle$.
Hence every ideal of $R$ is principal, proving that $R$ is a PID. $\blacksquare$

---

### 3. Proof 2: In a PID, Irreducible Elements are Prime

> **Lemma 7.2:** If $R$ is a PID and $p \in R$ is irreducible, then $p$ is prime.

#### Complete Proof:
Let $p \in R$ be irreducible, and suppose $p \mid ab$ for $a, b \in R$.
Consider the ideal $I = \langle p, a \rangle$.
Since $R$ is a PID, $I$ is principal: $\langle p, a \rangle = \langle d \rangle$ for some $d \in R$.
Since $p \in \langle d \rangle$, $d \mid p$.
Because $p$ is irreducible, its only divisors are units and associates of $p$.
- **Case 1: $d$ is associate to $p$.**
  Then $\langle d \rangle = \langle p \rangle$, which means $\langle p, a \rangle = \langle p \rangle$.
  This implies $a \in \langle p \rangle \implies p \mid a$.
- **Case 2: $d$ is a unit.**
  Then $\langle d \rangle = R$, so $\langle p, a \rangle = R = \langle 1 \rangle$.
  By Bézout's identity in a PID, there exist $x, y \in R$ such that:
  $$xp + ya = 1$$
  Multiplying both sides by $b$:
  $$xpb + yab = b \implies p(xb) + (ab)y = b$$
  Since $p \mid p$ and $p \mid ab$, $p$ divides the entire left-hand side:
  $$p \mid (p(xb) + (ab)y) \implies p \mid b$$
Thus either $p \mid a$ or $p \mid b$. Hence $p$ is prime. $\blacksquare$

---

### 4. Proof 3: Every PID is a UFD ($\text{PID} \implies \text{UFD}$)

> **Theorem 7.6:** If $R$ is a Principal Ideal Domain, then $R$ is a Unique Factorization Domain.

#### Outline of Complete Proof:
1. **Factorization Existence (Ascending Chain Condition on Principal Ideals - ACCP):**
   In a PID, any ascending chain of ideals $\langle a_1 \rangle \subseteq \langle a_2 \rangle \subseteq \langle a_3 \rangle \subseteq \dots$ must stabilize.
   *(Proof: The union $J = \bigcup \langle a_i \rangle$ is an ideal, hence $J = \langle c \rangle$ for some $c \in R$. Then $c \in \langle a_N \rangle$ for some $N$, so the chain stabilizes at $N$.)*
   This ACCP property guarantees that the process of factoring into irreducibles cannot continue indefinitely, ensuring the existence of irreducible factorizations.
2. **Uniqueness:**
   By Lemma 7.2, every irreducible element in a PID is prime.
   Using Euclid's Lemma repeatedly on $p_1 \cdots p_r = q_1 \cdots q_s$, $p_1 \mid q_j$ for some $j$. Since $q_j$ is irreducible, $p_1$ and $q_j$ are associates.
   Cancelling $p_1$ and proceeding by induction establishes uniqueness up to associates. $\blacksquare$

---

### 5. Counterexamples Delineating the Strict Inclusions

| Strict Inclusion | Counterexample | Why the Inversion Fails |
| :--- | :--- | :--- |
| $\text{ED} \subsetneq \text{PID}$ | $\mathbb{Z}\left[\frac{1 + \sqrt{-19}}{2}\right]$ | Is a PID (every ideal is principal), but admits NO Euclidean norm function. |
| $\text{PID} \subsetneq \text{UFD}$ | $\mathbb{Z}[x]$ | Is a UFD (by Gauss's Lemma), but $\langle 2, x \rangle$ is not principal, so NOT a PID. |
| $\text{UFD} \subsetneq \text{ID}$ | $\mathbb{Z}[\sqrt{-5}]$ | Is an integral domain, but $6 = 2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$ shows non-unique factorization. |"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "The Gaussian Integers $\\mathbb{Z}[i]$ as a Euclidean Domain & GCD Computation",
                "statement": r"1. Let $\mathbb{Z}[i] = \{ a + bi : a, b \in \mathbb{Z} \}$ be the ring of Gaussian integers. Define the norm function $N: \mathbb{Z}[i] \to \mathbb{Z}_{\ge 0}$ by $N(a+bi) = a^2 + b^2$. Prove that $\mathbb{Z}[i]$ is a Euclidean Domain with respect to this norm. 2. Use the Euclidean Algorithm in $\mathbb{Z}[i]$ to compute the greatest common divisor $\gcd(11 + 7i, \; 3 + 7i)$.",
                "hints": [
                    "For Part 1, to perform division of $\\alpha$ by $\\beta \\ne 0$, compute the quotient in $\\mathbb{C}$: $\\frac{\\alpha}{\\beta} = x + yi \\in \\mathbb{Q}[i]$. Choose integers $q_1, q_2$ closest to $x, y$ such that $|x - q_1| \\le 1/2$ and $|y - q_2| \\le 1/2$. Set $q = q_1 + q_2 i$ and $r = \\alpha - q\\beta$. Show $N(r) < N(\\beta)$.",
                    "For Part 2, compute the complex division $\\frac{11+7i}{3+7i}$, round to the nearest Gaussian integer $q$, and calculate the remainder $r$."
                ],
                "solution": r"""**Part 1: Proof that $\mathbb{Z}[i]$ is a Euclidean Domain**

The norm $N(z) = |z|^2 = z \bar{z}$ satisfies $N(z_1 z_2) = N(z_1) N(z_2)$.
For any non-zero $\alpha, \beta \in \mathbb{Z}[i]$:
$$N(\alpha \beta) = N(\alpha) N(\beta) \ge N(\alpha) \cdot 1 = N(\alpha) \quad (\text{since } N(\beta) \ge 1)$$
Now let $\alpha, \beta \in \mathbb{Z}[i]$ with $\beta \ne 0$.
In the field of complex numbers $\mathbb{C}$, compute the quotient:
$$\frac{\alpha}{\beta} = x + yi, \quad \text{where } x, y \in \mathbb{Q}$$
Choose integers $q_1, q_2 \in \mathbb{Z}$ that are closest to $x$ and $y$, respectively:
$$|x - q_1| \le \frac{1}{2} \quad \text{and} \quad |y - q_2| \le \frac{1}{2}$$
Define $q = q_1 + q_2 i \in \mathbb{Z}[i]$.
Define the remainder:
$$r = \alpha - q \beta \in \mathbb{Z}[i]$$
We now estimate the norm of $r$:
$$\frac{r}{\beta} = \frac{\alpha - q\beta}{\beta} = \frac{\alpha}{\beta} - q = (x - q_1) + (y - q_2) i$$
Taking the complex norm:
$$N\left(\frac{r}{\beta}\right) = (x - q_1)^2 + (y - q_2)^2 \le \left(\frac{1}{2}\right)^2 + \left(\frac{1}{2}\right)^2 = \frac{1}{4} + \frac{1}{4} = \frac{1}{2} < 1$$
Using multiplicativity of the norm:
$$N(r) = N(\beta) \cdot N\left(\frac{r}{\beta}\right) \le \frac{1}{2} N(\beta) < N(\beta)$$
Thus $\alpha = q \beta + r$ with $N(r) \le \frac{1}{2} N(\beta) < N(\beta)$.
Therefore, $\mathbb{Z}[i]$ is a Euclidean Domain. $\blacksquare$

---

**Part 2: Computing $\gcd(11 + 7i, \; 3 + 7i)$ via Euclidean Algorithm**

Let $\alpha = 11 + 7i$ and $\beta = 3 + 7i$.

**Step 1: Divide $\alpha$ by $\beta$**
$$\frac{\alpha}{\beta} = \frac{11 + 7i}{3 + 7i} = \frac{(11 + 7i)(3 - 7i)}{(3 + 7i)(3 - 7i)} = \frac{33 - 77i + 21i - 49i^2}{3^2 + 7^2} = \frac{33 + 49 - 56i}{9 + 49} = \frac{82 - 56i}{58}$$
Simplify:
$$\frac{\alpha}{\beta} = \frac{82}{58} - \frac{56}{58} i = \frac{41}{29} - \frac{28}{29} i \approx 1.4138 - 0.9655 i$$
Round to nearest integers:
$$q_1 = 1, \quad q_2 = -1 \implies q^{(1)} = 1 - i$$
Compute remainder $r^{(1)}$:
$$\begin{aligned}
r^{(1)} &= \alpha - q^{(1)} \beta = (11 + 7i) - (1 - i)(3 + 7i) \\
&= (11 + 7i) - (3 + 7i - 3i - 7i^2) = (11 + 7i) - (10 + 4i) \\
&= 1 + 3i
\end{aligned}$$
Norm check: $N(r^{(1)}) = 1^2 + 3^2 = 10$, while $N(\beta) = 3^2 + 7^2 = 58$. Indeed $10 < 58$.

**Step 2: Divide $\beta = 3 + 7i$ by $r^{(1)} = 1 + 3i$**
$$\frac{\beta}{r^{(1)}} = \frac{3 + 7i}{1 + 3i} = \frac{(3 + 7i)(1 - 3i)}{1^2 + 3^2} = \frac{3 - 9i + 7i - 21i^2}{10} = \frac{3 + 21 - 2i}{10} = \frac{24 - 2i}{10} = 2.4 - 0.2 i$$
Round to nearest integers:
$$q_1 = 2, \quad q_2 = 0 \implies q^{(2)} = 2$$
Compute remainder $r^{(2)}$:
$$r^{(2)} = (3 + 7i) - 2(1 + 3i) = (3 + 7i) - (2 + 6i) = 1 + i$$
Norm check: $N(r^{(2)}) = 1^2 + 1^2 = 2 < N(r^{(1)}) = 10$.

**Step 3: Divide $r^{(1)} = 1 + 3i$ by $r^{(2)} = 1 + i$**
$$\frac{r^{(1)}}{r^{(2)}} = \frac{1 + 3i}{1 + i} = \frac{(1 + 3i)(1 - i)}{1^2 + 1^2} = \frac{1 - i + 3i - 3i^2}{2} = \frac{4 + 2i}{2} = 2 + i$$
Since this is an exact Gaussian integer:
$$q^{(3)} = 2 + i, \quad r^{(3)} = 0$$
The last non-zero remainder is $r^{(2)} = 1 + i$.

Therefore:
$$\gcd(11 + 7i, \; 3 + 7i) = 1 + i \quad (\text{up to units } \pm 1, \pm i) \quad \blacksquare$$"""
            },
            {
                "tier": "Advanced",
                "title": "Failure of Unique Factorization in $\\mathbb{Z}[\\sqrt{-5}]$",
                "statement": r"Consider the quadratic integer ring $\mathbb{Z}[\sqrt{-5}] = \{ a + b\sqrt{-5} : a, b \in \mathbb{Z} \}$ with norm $N(a + b\sqrt{-5}) = a^2 + 5b^2$. 1. Determine all units in $\mathbb{Z}[\sqrt{-5}]$. 2. In $\mathbb{Z}[\sqrt{-5}]$, consider the two factorizations of 6: $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$. Prove that the elements $2, 3, 1 + \sqrt{-5}$, and $1 - \sqrt{-5}$ are all irreducible in $\mathbb{Z}[\sqrt{-5}]$. 3. Prove that $2$ is not associate to either $1 + \sqrt{-5}$ or $1 - \sqrt{-5}$, and deduce that $\mathbb{Z}[\sqrt{-5}]$ is NOT a Unique Factorization Domain (UFD).",
                "hints": [
                    "For Part 1, $u$ is a unit iff $N(u) = 1$.",
                    "For Part 2, if an element factors as $\\alpha = \\beta \\gamma$, then $N(\\alpha) = N(\\beta)N(\\gamma)$. Show that no element in $\\mathbb{Z}[\\sqrt{-5}]$ can have norm 2 or 3.",
                    "For Part 3, check whether 2 divides $(1+\\sqrt{-5})(1-\\sqrt{-5})$. Does 2 divide either factor?"
                ],
                "solution": r"""**Step 1: Units of $\mathbb{Z}[\sqrt{-5}]$**

The norm is $N(\alpha) = a^2 + 5b^2 \in \mathbb{Z}_{\ge 0}$, which is strictly multiplicative: $N(\alpha \beta) = N(\alpha) N(\beta)$.
If $u$ is a unit, there exists $v$ such that $uv = 1$.
Then $N(u) N(v) = N(1) = 1$.
Since $N(u) \in \mathbb{Z}_{\ge 0}$, this forces $N(u) = 1$.
Let $u = a + b\sqrt{-5}$. Then:
$$a^2 + 5b^2 = 1$$
If $b \ne 0$, then $5b^2 \ge 5 > 1$, which is impossible.
Thus $b = 0$, giving $a^2 = 1 \implies a = \pm 1$.
Therefore, the only units in $\mathbb{Z}[\sqrt{-5}]$ are:
$$\mathbb{Z}[\sqrt{-5}]^\times = \{1, -1\}$$

---

**Step 2: Irreducibility of the Factors**

Compute the norms of the four elements:
- $N(2) = 2^2 + 5(0)^2 = 4$
- $N(3) = 3^2 + 5(0)^2 = 9$
- $N(1 + \sqrt{-5}) = 1^2 + 5(1)^2 = 6$
- $N(1 - \sqrt{-5}) = 1^2 + 5(-1)^2 = 6$

**Crucial Observation: Are there elements of norm 2 or 3?**
If $a^2 + 5b^2 = 2$, then $b$ must be 0, so $a^2 = 2$, which has no integer solutions!
If $a^2 + 5b^2 = 3$, then $b$ must be 0, so $a^2 = 3$, which has no integer solutions!
Thus, **no element in $\mathbb{Z}[\sqrt{-5}]$ has norm 2 or 3**.

- **Irreducibility of 2:**
  Suppose $2 = \alpha \beta$. Then $N(2) = 4 = N(\alpha) N(\beta)$.
  The integer factorizations of 4 are $1 \times 4$ and $2 \times 2$.
  If $N(\alpha) = 2$, impossible since no elements have norm 2.
  Thus $N(\alpha) = 1$ or $N(\beta) = 1$, which means $\alpha$ or $\beta$ is a unit ($\pm 1$).
  Hence $2$ is irreducible.
- **Irreducibility of 3:**
  Suppose $3 = \alpha \beta$. Then $N(3) = 9 = N(\alpha) N(\beta)$.
  Since no element has norm 3, $N(\alpha)$ cannot be 3.
  Thus $N(\alpha) = 1$ or $N(\beta) = 1$, so $\alpha$ or $\beta$ is a unit.
  Hence $3$ is irreducible.
- **Irreducibility of $1 \pm \sqrt{-5}$:**
  Suppose $1 \pm \sqrt{-5} = \alpha \beta$. Then $N(1 \pm \sqrt{-5}) = 6 = N(\alpha) N(\beta)$.
  The integer factorizations of 6 are $1 \times 6$ and $2 \times 3$.
  Since no elements have norm 2 or 3, neither factor can have norm 2 or 3.
  Thus $N(\alpha) = 1$ or $N(\beta) = 1$.
  Hence $1 \pm \sqrt{-5}$ is irreducible.

---

**Step 3: Failure of Unique Factorization**

We have two factorizations of $6$ into irreducible elements:
$$6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$$
Are any of the irreducibles on the left associate to those on the right?
The only units are $\pm 1$.
The associates of $2$ are $\pm 2$.
Clearly:
$$2 \ne \pm (1 + \sqrt{-5}) \quad \text{and} \quad 2 \ne \pm (1 - \sqrt{-5})$$
Indeed, $N(2) = 4$, whereas $N(1 \pm \sqrt{-5}) = 6 \ne 4$.
Since associates must have identical norms ($N(\pm \alpha) = N(\alpha)$), $2$ is not associate to $1 + \sqrt{-5}$ or $1 - \sqrt{-5}$.

Moreover, $2 \mid (1 + \sqrt{-5})(1 - \sqrt{-5}) = 6$.
Does $2$ divide $1 + \sqrt{-5}$?
If $2 \mid (1 + \sqrt{-5})$, then $\frac{1 + \sqrt{-5}}{2} = \frac{1}{2} + \frac{1}{2}\sqrt{-5} \notin \mathbb{Z}[\sqrt{-5}]$.
So $2 \nmid (1 + \sqrt{-5})$ and similarly $2 \nmid (1 - \sqrt{-5})$.
Thus $2$ is an irreducible element that is **NOT prime**!

Because $6$ has two genuinely distinct factorizations into irreducible elements that cannot be matched up as associates, unique factorization fails.
Therefore, $\mathbb{Z}[\sqrt{-5}]$ is **NOT a UFD**. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Maximal Ideals in PIDs and the ACCP Characterization of UFDs",
                "statement": r"1. Let $R$ be a Principal Ideal Domain (PID). Prove that every non-zero prime ideal of $R$ is a maximal ideal: $P \ne \{0\} \text{ prime} \implies P \text{ maximal}$. 2. Define the Ascending Chain Condition on Principal Ideals (ACCP). Prove that every PID satisfies ACCP. 3. Prove the overarching characterization: An integral domain $R$ is a UFD if and only if $R$ satisfies ACCP and every irreducible element in $R$ is prime.",
                "hints": [
                    "For Part 1, let $P = \\langle p \\rangle \\ne \\{0\\}$ be a prime ideal in a PID. Show that $p$ is an irreducible element, and that if $\\langle p \\rangle \\subseteq \\langle m \\rangle$, then $m$ divides $p$.",
                    "For Part 2, for any chain $\\langle a_1 \\rangle \\subseteq \\langle a_2 \\rangle \\subseteq \\dots$, consider the union $I = \\bigcup \\langle a_i \\rangle$. Since $R$ is a PID, $I = \\langle a \\rangle$ for some $a$.",
                    "For Part 3, use ACCP to show existence of irreducible factorizations (by contradiction, assume a non-empty set of non-factorable elements), and use primes to prove uniqueness."
                ],
                "solution": r"""**Part 1: Non-Zero Prime Ideals in a PID are Maximal**

Let $R$ be a PID, and let $P \ne \{0\}$ be a non-zero prime ideal.
Since $R$ is a PID, $P$ is principal:
$$P = \langle p \rangle \quad \text{for some non-zero } p \in R$$
Since $P$ is a prime ideal, $p$ is a prime element.
By Theorem 7.4, every prime element in an integral domain is irreducible.
Thus $p$ is irreducible.

Now suppose there is an ideal $M \trianglelefteq R$ such that:
$$P = \langle p \rangle \subseteq M \subseteq R$$
Since $R$ is a PID, $M$ is also principal: $M = \langle m \rangle$ for some $m \in R$.
Then:
$$\langle p \rangle \subseteq \langle m \rangle \implies m \mid p$$
This means there exists $c \in R$ such that $p = mc$.
Because $p$ is irreducible, one of the factors $m$ or $c$ must be a unit:
- **Case 1: $m$ is a unit.**
  Then $\langle m \rangle = R$, so $M = R$.
- **Case 2: $c$ is a unit.**
  Then $m = c^{-1} p$, so $m$ is associate to $p$.
  This implies $\langle m \rangle = \langle p \rangle$, so $M = P$.

Therefore, there are no ideals strictly between $P$ and $R$.
Hence $P$ is a **maximal ideal**. $\blacksquare$

---

**Part 2: PIDs Satisfy the Ascending Chain Condition on Principal Ideals (ACCP)**

> **Definition (ACCP):** A domain $R$ satisfies ACCP if every ascending chain of principal ideals:
> $$\langle a_1 \rangle \subseteq \langle a_2 \rangle \subseteq \langle a_3 \rangle \subseteq \dots$$
> eventually terminates (stabilizes): $\exists N \in \mathbb{Z}^+$ such that $\langle a_n \rangle = \langle a_N \rangle$ for all $n \ge N$.

#### Proof that a PID satisfies ACCP:
Let $\langle a_1 \rangle \subseteq \langle a_2 \rangle \subseteq \langle a_3 \rangle \subseteq \dots$ be an ascending chain of principal ideals in a PID $R$.
Consider their union:
$$I = \bigcup_{n=1}^\infty \langle a_n \rangle$$
1. **$I$ is an ideal of $R$:**
   - Non-empty: $0 \in \langle a_1 \rangle \subseteq I$.
   - Addition: If $x, y \in I$, then $x \in \langle a_j \rangle$ and $y \in \langle a_k \rangle$. Let $m = \max(j, k)$. Then $x, y \in \langle a_m \rangle$, so $x - y \in \langle a_m \rangle \subseteq I$.
   - Multiplication: If $r \in R$ and $x \in I$, $x \in \langle a_j \rangle \implies rx \in \langle a_j \rangle \subseteq I$.
2. **Since $R$ is a PID, $I$ is principal:**
   There exists $c \in R$ such that $I = \langle c \rangle$.
3. **Stabilization:**
   Since $c \in I = \bigcup_{n=1}^\infty \langle a_n \rangle$, there exists some positive integer $N$ such that:
   $$c \in \langle a_N \rangle$$
   Therefore:
   $$I = \langle c \rangle \subseteq \langle a_N \rangle$$
   On the other hand, for all $n \ge N$:
   $$\langle a_N \rangle \subseteq \langle a_n \rangle \subseteq I = \langle c \rangle$$
   Hence:
   $$\langle a_n \rangle = \langle a_N \rangle \quad \forall n \ge N$$
The chain stabilizes at step $N$.
Thus every PID satisfies ACCP. $\blacksquare$

---

**Part 3: $R$ is a UFD $\iff$ ACCP Holds and Irreducibles are Prime**

#### $(\implies)$ Direction:
If $R$ is a UFD:
1. Every irreducible element is prime (standard property of UFDs: if $p \mid ab$, write $ab$ in prime factorizations; by uniqueness, $p$ must be associate to one of the factors of $a$ or $b$).
2. Any proper divisor chain $a_1, a_2, \dots$ where $a_{n+1} \mid a_n$ strictly decreases the number of irreducible factors in the factorization. Since the number of irreducible factors is finite, the chain must terminate. Thus ACCP holds.

#### $(\impliedby)$ Direction:
Assume $R$ satisfies ACCP and every irreducible element in $R$ is prime.

**1. Existence of Factorization:**
Suppose there exists a non-zero non-unit $x \in R$ that cannot be factored into irreducibles.
Let $\mathcal{S}$ be the set of principal ideals $\langle y \rangle$ such that $y$ is a non-zero non-unit that cannot be written as a product of irreducibles.
By assumption, $\langle x \rangle \in \mathcal{S}$, so $\mathcal{S} \ne \emptyset$.
By ACCP, any chain in $\mathcal{S}$ has an upper bound, so by Zorn's Lemma (or directly by ACCP), $\mathcal{S}$ contains a maximal element; call it $\langle m \rangle$.
- Since $m$ cannot be factored into irreducibles, $m$ itself cannot be irreducible (an irreducible element is a product of 1 irreducible).
- Thus $m$ must factor non-trivially: $m = a b$, where neither $a$ nor $b$ is a unit.
- Then $\langle m \rangle \subsetneq \langle a \rangle$ and $\langle m \rangle \subsetneq \langle b \rangle$.
- By the maximality of $\langle m \rangle$ in $\mathcal{S}$, neither $\langle a \rangle$ nor $\langle b \rangle$ can belong to $\mathcal{S}$!
- Therefore, both $a$ and $b$ can be factored into irreducibles:
  $$a = p_1 \cdots p_r \quad \text{and} \quad b = q_1 \cdots q_s$$
- Then $m = a b = p_1 \cdots p_r q_1 \cdots q_s$ is a product of irreducibles!
This contradicts $m$ being non-factorable.
Therefore, $\mathcal{S} = \emptyset$: **every non-zero non-unit can be factored into irreducibles**.

**2. Uniqueness of Factorization:**
Suppose $x = p_1 p_2 \cdots p_r = q_1 q_2 \cdots q_s$ are two factorizations into irreducibles.
By hypothesis, every irreducible element is prime.
Therefore, $p_1$ is prime.
Since $p_1 \mid (q_1 q_2 \cdots q_s)$, by Euclid's lemma for primes, $p_1 \mid q_j$ for some $j$.
Reordering the $q$'s if necessary, assume $p_1 \mid q_1$.
Since $q_1$ is irreducible and $p_1$ is not a unit, $p_1$ and $q_1$ must be associates:
$$q_1 = u_1 p_1 \quad \text{for some unit } u_1 \in R^\times$$
Cancelling $p_1$ using the domain cancellation law:
$$p_2 \cdots p_r = u_1 q_2 \cdots q_s$$
We proceed by induction on $r$.
Eventually, all factors are paired as associates, and $r = s$.
Uniqueness up to associates is established.

**Conclusion:** $R$ is a Unique Factorization Domain. $\blacksquare$"""
            }
        ]
    }
    return u7

if __name__ == "__main__":
    u = get_unit7()
    print("Unit 7 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
