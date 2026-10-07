# -*- coding: utf-8 -*-
"""
build_aa_unit1.py
Constructs Unit 1: Foundations of Algebraic Structures, Relations & Modular Arithmetic
"""

def get_unit1():
    u1 = {
        "number": 1,
        "title": "Foundations of Algebraic Structures, Relations & Modular Arithmetic",
        "leadSummary": "Rigorous introduction to abstract algebraic structures, binary relations, equivalence classes, set partitions, congruence modulo n, the ring structure of Z_n, Bézout's identity, modular multiplicative inverses, monoids, semi-groups, and axiomatic group theory.",
        "simulations": ["sim_aa_modular_cayley"],
        "sections": [
            {
                "secNumber": "1.1",
                "title": "Binary Relations, Equivalence Relations & Set Partitions",
                "content": r"""### 1. Cartesian Products and Binary Relations

Let $A$ and $B$ be non-empty sets. The **Cartesian product** $A \times B$ is the set of all ordered pairs:
$$A \times B = \{ (a, b) : a \in A, \; b \in B \}$$
A **binary relation** $R$ from $A$ to $B$ is a subset $R \subseteq A \times B$. When $A = B$, we say $R$ is a binary relation on $A$. If $(a, b) \in R$, we write $a \sim b$ or $a \, R \, b$.

---

### 2. Axioms of an Equivalence Relation

> **Definition 1.1 (Equivalence Relation):**
> A binary relation $\sim$ on a set $A$ is an **equivalence relation** if it satisfies the following three fundamental axioms for all elements $a, b, c \in A$:
> 1. **Reflexivity:** $a \sim a, \quad \forall a \in A$.
> 2. **Symmetry:** If $a \sim b$, then $b \sim a$.
> 3. **Transitivity:** If $a \sim b$ and $b \sim c$, then $a \sim c$.

#### Definition 1.2 (Equivalence Class):
Let $\sim$ be an equivalence relation on set $A$. For any $a \in A$, the **equivalence class** of $a$, denoted by $[a]$ or $\text{cl}(a)$, is the set of all elements in $A$ related to $a$:
$$[a] = \{ x \in A : x \sim a \}$$
Any element $x \in [a]$ is called a **representative** of the equivalence class $[a]$.

---

### 3. The Fundamental Theorem of Equivalence Relations

A **partition** of a set $A$ is a collection $\mathcal{P} = \{A_i\}_{i \in I}$ of non-empty subsets of $A$ such that:
1. $A_i \cap A_j = \emptyset$ whenever $i \ne j$ (pairwise disjoint).
2. $\bigcup_{i \in I} A_i = A$ (exhaustive union).

> **Theorem 1.1 (The Fundamental Theorem of Equivalence Relations):**
> Let $A$ be a non-empty set.
> 1. If $\sim$ is an equivalence relation on $A$, the set of all equivalence classes $A / \sim \;= \{ [a] : a \in A \}$ forms a partition of $A$.
> 2. Conversely, every partition $\mathcal{P}$ of $A$ induces a unique equivalence relation $\sim$ on $A$ whose equivalence classes are precisely the cells of $\mathcal{P}$.

#### Complete Proof of Part 1:
- **Non-emptiness:** For every $a \in A$, by reflexivity $a \sim a$, so $a \in [a]$. Thus no equivalence class is empty: $[a] \ne \emptyset$.
- **Exhaustive coverage:** Since $a \in [a]$ for all $a \in A$, we have:
  $$A = \bigcup_{a \in A} \{a\} \subseteq \bigcup_{a \in A} [a] \subseteq A \implies \bigcup_{a \in A} [a] = A$$
- **Pairwise disjointness:** Let $a, b \in A$. We must prove that either $[a] = [b]$ or $[a] \cap [b] = \emptyset$.
  Suppose $[a] \cap [b] \ne \emptyset$. Then there exists $z \in [a] \cap [b]$.
  By definition of equivalence class:
  $$z \in [a] \implies z \sim a \implies a \sim z \quad (\text{by symmetry})$$
  $$z \in [b] \implies z \sim b$$
  Now take any $x \in [a]$. Then $x \sim a$.
  Applying transitivity sequentially:
  $$x \sim a \text{ and } a \sim z \implies x \sim z$$
  $$x \sim z \text{ and } z \sim b \implies x \sim b \implies x \in [b]$$
  Hence $[a] \subseteq [b]$. By symmetrical reasoning, $[b] \subseteq [a]$. Therefore $[a] = [b]$.
  Consequently, distinct equivalence classes are strictly disjoint. $\blacksquare$"""
            },
            {
                "secNumber": "1.2",
                "title": "Congruence Modulo n, The Ring Z_n & Modular Inverses",
                "content": r"""### 1. Congruence Modulo $n$

Let $n$ be a positive integer ($n \in \mathbb{Z}^+$).

> **Definition 1.3 (Congruence Modulo $n$):**
> Two integers $a, b \in \mathbb{Z}$ are **congruent modulo $n$**, written:
> $$a \equiv b \pmod n$$
> if $n$ divides their difference: $n \mid (a - b)$, or equivalently, there exists $k \in \mathbb{Z}$ such that $a - b = k n$.

#### Proposition 1.1:
Congruence modulo $n$ is an equivalence relation on $\mathbb{Z}$.
- **Reflexivity:** $a - a = 0 = 0 \cdot n \implies a \equiv a \pmod n$.
- **Symmetry:** If $a \equiv b \pmod n$, then $a - b = kn \implies b - a = (-k)n \implies b \equiv a \pmod n$.
- **Transitivity:** If $a \equiv b \pmod n$ and $b \equiv c \pmod n$, then $a - b = kn$ and $b - c = jn$.
  Adding: $(a - b) + (b - c) = a - c = (k + j)n \implies a \equiv c \pmod n$. $\blacksquare$

---

### 2. The Set of Residue Classes $\mathbb{Z}_n$

The equivalence classes are the **residue classes modulo $n$**:
$$[a] = \{ x \in \mathbb{Z} : x \equiv a \pmod n \} = \{ a + kn : k \in \mathbb{Z} \}$$
By the Division Algorithm, for every $a \in \mathbb{Z}$ there exist unique $q, r \in \mathbb{Z}$ with $0 \le r < n$ such that $a = qn + r$.
Hence, there are exactly $n$ distinct equivalence classes:
$$\mathbb{Z}_n = \{ [0], [1], [2], \dots, [n-1] \}$$

#### Well-Defined Modular Operations:
Define addition and multiplication on residue classes by:
$$[a] + [b] = [a + b], \qquad [a] \cdot [b] = [a \cdot b]$$
*Proof of Well-Definedness:*
Suppose $[a] = [a']$ and $[b] = [b']$. Then $a' = a + kn$ and $b' = b + jn$.
Then:
$$a' + b' = (a + b) + (k + j)n \equiv a + b \pmod n \implies [a' + b'] = [a + b]$$
$$a' b' = (a + kn)(b + jn) = ab + n(aj + bk + kjn) \equiv ab \pmod n \implies [a' b'] = [ab]$$
Thus, the operations are completely independent of class representatives!

---

### 3. Bézout's Identity & Modular Multiplicative Inverses

> **Theorem 1.2 (Bézout's Identity):**
> Let $a, b \in \mathbb{Z}$ with $\gcd(a, b) = d$. Then there exist integers $x, y \in \mathbb{Z}$ such that:
> $$a x + b y = d$$

> **Theorem 1.3 (Existence of Modular Inverse):**
> A residue class $[a] \in \mathbb{Z}_n$ possesses a multiplicative inverse $[a]^{-1} \in \mathbb{Z}_n$ such that $[a] \cdot [x] = [1]$ if and only if:
> $$\gcd(a, n) = 1$$

#### Proof:
$(\implies)$ If $[a][x] = [1]$, then $a x \equiv 1 \pmod n \implies a x - 1 = k n \implies a x - n k = 1$.
Any divisor of both $a$ and $n$ must divide $a x - n k = 1$. Hence $\gcd(a, n) = 1$.

$(\impliedby)$ If $\gcd(a, n) = 1$, by Bézout's Identity there exist integers $x, y \in \mathbb{Z}$ such that:
$$a x + n y = 1 \implies a x - 1 = (-y) n \implies a x \equiv 1 \pmod n \implies [a][x] = [1]$$
Thus $[x]$ is the required modular inverse. $\blacksquare$

The set of all invertible elements forms the **Group of Units Modulo $n$**:
$$U(n) = \mathbb{Z}_n^\times = \{ [a] \in \mathbb{Z}_n : \gcd(a, n) = 1 \}$$
with order given by **Euler's totient function**: $|U(n)| = \phi(n)$."""
            },
            {
                "secNumber": "1.3",
                "title": "Binary Operations, Monoids & Axiomatic Definition of Groups",
                "content": r"""### 1. Binary Operations and Algebraic Structures

Let $S$ be a non-empty set.

> **Definition 1.4 (Binary Operation):**
> A **binary operation** $*$ on $S$ is a function $*: S \times S \to S$.
> That is, for every ordered pair $(a, b) \in S \times S$, $*$ assigns a unique element $a * b \in S$.
> This property is termed **Closure**: $\forall a, b \in S, \; a * b \in S$.

#### Hierarchy of Algebraic Structures:
1. **Magma / Groupoid:** A set $S$ equipped with a closed binary operation $*$.
2. **Semigroup:** A magma $(S, *)$ that satisfies **Associativity**:
   $$\forall a, b, c \in S, \quad (a * b) * c = a * (b * c)$$
3. **Monoid:** A semigroup $(S, *)$ possessing an **Identity Element** $e \in S$:
   $$\forall a \in S, \quad a * e = e * a = a$$

---

### 2. The Axiomatic Definition of a Group

A group is the foundational algebraic structure of modern symmetry and mathematical physics.

> **Definition 1.5 (Group):**
> A **group** is an ordered pair $(G, *)$ consisting of a non-empty set $G$ and a binary operation $*$ on $G$ that satisfies the following four **Group Axioms**:
> 1. **Closure ($G_1$):**
>    $$\forall a, b \in G, \quad a * b \in G$$
> 2. **Associativity ($G_2$):**
>    $$\forall a, b, c \in G, \quad (a * b) * c = a * (b * c)$$
> 3. **Identity Element ($G_3$):**
>    There exists an element $e \in G$ such that:
>    $$\forall a \in G, \quad a * e = e * a = a$$
> 4. **Inverse Element ($G_4$):**
>    For every element $a \in G$, there exists an element $a^{-1} \in G$ such that:
>    $$a * a^{-1} = a^{-1} * a = e$$

#### Definition 1.6 (Abelian / Commutative Group):
A group $(G, *)$ is called **Abelian** (named in honor of Niels Henrik Abel) if the binary operation satisfies commutativity:
$$\forall a, b \in G, \quad a * b = b * a$$
If there exist elements $x, y \in G$ such that $x * y \ne y * x$, the group is **Non-Abelian**."""
            },
            {
                "secNumber": "1.4",
                "title": "Group Axiom Consequences, Inverses & Cancellation Laws",
                "content": r"""### 1. Uniqueness Theorems

While the group axioms state the existence of an identity and inverses, their uniqueness is a mathematical consequence of the axioms.

> **Theorem 1.4 (Uniqueness of the Identity Element):**
> In any group $(G, *)$, the identity element is unique.

#### Proof:
Suppose $e$ and $e'$ are both identity elements in $G$.
Since $e$ is an identity: $e * e' = e'$.
Since $e'$ is an identity: $e * e' = e$.
Therefore:
$$e = e * e' = e'$$
Thus, there can be only one identity element. $\blacksquare$

---

> **Theorem 1.5 (Uniqueness of Inverse Elements):**
> In any group $(G, *)$, every element $a \in G$ possesses a unique inverse $a^{-1}$.

#### Proof:
Suppose $b$ and $c$ are both inverses of $a$. Then:
$$a * b = b * a = e \quad \text{and} \quad a * c = c * a = e$$
Using associativity:
$$b = b * e = b * (a * c) = (b * a) * c = e * c = c$$
Hence $b = c$. The inverse is strictly unique. $\blacksquare$

---

### 2. The Cancellation Laws

> **Theorem 1.6 (Cancellation Laws):**
> In any group $(G, *)$, for all $a, b, c \in G$:
> 1. **Left Cancellation:** If $a * b = a * c$, then $b = c$.
> 2. **Right Cancellation:** If $b * a = c * a$, then $b = c$.

#### Proof of Left Cancellation:
Since $a \in G$, its inverse $a^{-1}$ exists. Multiply both sides on the left by $a^{-1}$:
$$a^{-1} * (a * b) = a^{-1} * (a * c)$$
By associativity:
$$(a^{-1} * a) * b = (a^{-1} * a) * c$$
$$e * b = e * c \implies b = c \quad \blacksquare$$

---

### 3. The Shoes-and-Socks Property and Involutions

> **Theorem 1.7 (Inverse of Products):**
> For any elements $a, b \in G$:
> $$(a * b)^{-1} = b^{-1} * a^{-1}$$

#### Proof:
We verify that multiplying $(a * b)$ by $(b^{-1} * a^{-1})$ yields the identity $e$:
$$(a * b) * (b^{-1} * a^{-1}) = a * (b * b^{-1}) * a^{-1} = a * e * a^{-1} = a * a^{-1} = e$$
Similarly, on the left:
$$(b^{-1} * a^{-1}) * (a * b) = b^{-1} * (a^{-1} * a) * b = b^{-1} * e * b = b^{-1} * b = e$$
By uniqueness of the inverse, $(a * b)^{-1} = b^{-1} * a^{-1}$. $\blacksquare$
*(Physical analogy: You put on socks then shoes ($a * b$); to reverse the process, you must remove shoes then socks ($b^{-1} * a^{-1}$)!)*

#### Proposition 1.2 (Double Inverse Law):
For every $a \in G$:
$$(a^{-1})^{-1} = a$$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Modular Multiplicative Units and Bézout Inverses in Z_n",
                "statement": r"Consider the algebraic ring $\mathbb{Z}_{28}$. 1. Determine the cardinality $|U(28)|$ of the group of units $U(28)$ using Euler's totient formula. 2. Verify whether $[11] \in U(28)$, and if so, compute its multiplicative inverse $[11]^{-1} \in \mathbb{Z}_{28}$ using the Extended Euclidean Algorithm. 3. Solve the linear congruence $11x \equiv 15 \pmod{28}$.",
                "hints": [
                    "Recall that $28 = 2^2 \\times 7$. Use the multiplicative property of Euler's totient: $\\phi(p^k) = p^k - p^{k-1}$.",
                    "Apply the Extended Euclidean Algorithm: divide 28 by 11 to write $\\gcd(28, 11) = 1 = 28x + 11y$."
                ],
                "solution": r"""**Step 1: Compute $|U(28)| = \phi(28)$**
Prime factorization of $28$:
$$28 = 2^2 \times 7^1$$
Using Euler's totient product formula:
$$\phi(28) = 28 \left(1 - \frac{1}{2}\right) \left(1 - \frac{1}{7}\right) = 28 \times \frac{1}{2} \times \frac{6}{7} = 14 \times \frac{6}{7} = 12$$
Thus, the group of units $U(28)$ has order $|U(28)| = 12$.

---

**Step 2: Extended Euclidean Algorithm for $[11]^{-1}$**
Since $\gcd(11, 28) = 1$, $[11]$ is a unit in $\mathbb{Z}_{28}$.
Perform forward division:
$$\begin{aligned}
28 &= 2 \times 11 + 6 \\
11 &= 1 \times 6 + 5 \\
6 &= 1 \times 5 + 1 \\
5 &= 5 \times 1 + 0
\end{aligned}$$
Back-substitute to express $1$ as a linear combination of $28$ and $11$:
$$\begin{aligned}
1 &= 6 - 1 \times 5 \\
&= 6 - 1 \times (11 - 1 \times 6) = 2 \times 6 - 1 \times 11 \\
&= 2 \times (28 - 2 \times 11) - 1 \times 11 \\
&= 2 \times 28 - 4 \times 11 - 1 \times 11 \\
&= 2 \times 28 - 5 \times 11
\end{aligned}$$
Taking this identity modulo $28$:
$$-5 \times 11 \equiv 1 \pmod{28}$$
Since $-5 \equiv 28 - 5 = 23 \pmod{28}$:
$$11 \times 23 = 253 = 9 \times 28 + 1 \equiv 1 \pmod{28}$$
Therefore, the multiplicative inverse is:
$$[11]^{-1} = [23] \in \mathbb{Z}_{28}$$

---

**Step 3: Solve $11x \equiv 15 \pmod{28}$**
Multiply both sides by $[11]^{-1} = 23$:
$$x \equiv 23 \times 15 \pmod{28}$$
Compute product:
$$23 \times 15 = 345$$
Divide by $28$:
$$345 = 12 \times 28 + 9 \implies 345 \equiv 9 \pmod{28}$$
The unique solution modulo $28$ is:
$$x \equiv 9 \pmod{28}$$
Verification: $11(9) = 99 = 3(28) + 15 \equiv 15 \pmod{28}$. Correct!"""
            },
            {
                "tier": "Advanced",
                "title": "Equivalence Relations on Real Matrices and Trace-Rank Partitions",
                "statement": r"Let $M_n(\mathbb{R})$ denote the set of all $n \times n$ real matrices. 1. Define the relation $\sim$ on $M_n(\mathbb{R})$ by $A \sim B \iff \exists P \in GL_n(\mathbb{R})$ such that $B = P^{-1} A P$ (matrix similarity). Prove rigorously that similarity is an equivalence relation. 2. Define the relation $\approx$ by $A \approx B \iff \text{rank}(A) = \text{rank}(B)$. Prove that $\approx$ is an equivalence relation and determine the exact number of equivalence classes in $M_n(\mathbb{R}) / \approx$.",
                "hints": [
                    "For similarity, use the properties of matrix inversion: $I^{-1} = I$, $(P^{-1})^{-1} = P$, and $(PQ)^{-1} = Q^{-1} P^{-1}$.",
                    "For the rank relation, consider all possible rank values for an $n \\times n$ matrix."
                ],
                "solution": r"""**Part 1: Proof that Matrix Similarity is an Equivalence Relation**

Let $A, B, C \in M_n(\mathbb{R})$.
1. **Reflexivity:**
   The identity matrix $I_n \in GL_n(\mathbb{R})$ satisfies $I_n^{-1} = I_n$.
   Then $A = I_n^{-1} A I_n$.
   Hence $A \sim A$.

2. **Symmetry:**
   Suppose $A \sim B$. Then there exists $P \in GL_n(\mathbb{R})$ such that $B = P^{-1} A P$.
   Multiplying on the left by $P$ and on the right by $P^{-1}$:
   $$P B P^{-1} = A$$
   Let $Q = P^{-1} \in GL_n(\mathbb{R})$. Then $Q^{-1} = (P^{-1})^{-1} = P$.
   Substituting gives:
   $$A = Q^{-1} B Q$$
   Hence $B \sim A$.

3. **Transitivity:**
   Suppose $A \sim B$ and $B \sim C$.
   Then there exist $P, Q \in GL_n(\mathbb{R})$ such that:
   $$B = P^{-1} A P \quad \text{and} \quad C = Q^{-1} B Q$$
   Substituting $B$ into the equation for $C$:
   $$C = Q^{-1} (P^{-1} A P) Q = (Q^{-1} P^{-1}) A (P Q) = (P Q)^{-1} A (P Q)$$
   Since $P, Q \in GL_n(\mathbb{R})$, their product $R = P Q \in GL_n(\mathbb{R})$ is invertible.
   Therefore $A \sim C$.
   This proves that similarity $\sim$ is an equivalence relation on $M_n(\mathbb{R})$. $\blacksquare$

---

**Part 2: Proof for the Rank Relation and Cardinality of Partition**

Define $A \approx B \iff \text{rank}(A) = \text{rank}(B)$.
1. **Reflexivity:** $\text{rank}(A) = \text{rank}(A) \implies A \approx A$.
2. **Symmetry:** $\text{rank}(A) = \text{rank}(B) \implies \text{rank}(B) = \text{rank}(A) \implies B \approx A$.
3. **Transitivity:** $\text{rank}(A) = \text{rank}(B)$ and $\text{rank}(B) = \text{rank}(C) \implies \text{rank}(A) = \text{rank}(C) \implies A \approx C$.
Hence $\approx$ is an equivalence relation.

#### Number of Equivalence Classes:
For any $n \times n$ matrix $A \in M_n(\mathbb{R})$, the rank is an integer bounded by:
$$0 \le \text{rank}(A) \le n$$
Every integer $k \in \{0, 1, 2, \dots, n\}$ is realized as the rank of the diagonal projection matrix $D_k = \text{diag}(\underbrace{1, \dots, 1}_{k \text{ times}}, 0, \dots, 0)$.
Therefore, the equivalence classes are:
$$C_k = \{ A \in M_n(\mathbb{R}) : \text{rank}(A) = k \}, \quad k \in \{0, 1, 2, \dots, n\}$$
The total number of equivalence classes is:
$$|M_n(\mathbb{R}) / \approx| = n + 1$$"""
            },
            {
                "tier": "Rigorous Examination / Derivation",
                "title": "Minimal Group Axioms & Independence Proof via Counterexamples",
                "statement": r"A student proposes a weaker definition of a group: A set $G$ with an associative binary operation $*$ is a group if: (1) There exists a left identity $e \in G$ such that $e * a = a$ for all $a \in G$; and (2) For every $a \in G$, there exists a left inverse $a_L^{-1} \in G$ such that $a_L^{-1} * a = e$. 1. Prove rigorously that this weaker set of axioms is sufficient to guarantee that $G$ is a full group (i.e., that $e$ is also a right identity and $a_L^{-1}$ is also a right inverse). 2. Construct an explicit counterexample demonstrating that if (1) is a left identity but (2) is a right inverse ($a * a_R^{-1} = e$), the resulting structure is NOT necessarily a group.",
                "hints": [
                    "For Part 1, start by showing $a * a_L^{-1} = e$ by multiplying by the left inverse of $a_L^{-1}$.",
                    "For Part 2, construct a non-trivial set with operation $x * y = y$ or $x * y = x$."
                ],
                "solution": r"""**Part 1: Proof that Left Identity + Left Inverses imply a Full Group**

Let $(G, *)$ be an associative magma with:
(A1) $\exists e \in G$ such that $e * a = a, \; \forall a \in G$ (left identity).
(A2) $\forall a \in G, \; \exists a' \in G$ such that $a' * a = e$ (left inverse).

**Claim 1: Every left inverse is also a right inverse ($a * a' = e$).**
Let $a \in G$, and let $a'$ be its left inverse ($a' * a = e$).
By (A2), the element $a'$ itself must possess a left inverse $a'' \in G$ such that:
$$a'' * a' = e$$
Now compute:
$$\begin{aligned}
a * a' &= e * (a * a') \quad (\text{by A1}) \\
&= (a'' * a') * (a * a') \\
&= a'' * (a' * a) * a' \quad (\text{by associativity}) \\
&= a'' * e * a' \quad (\text{since } a' * a = e) \\
&= a'' * a' \quad (\text{since } e * a' = a') \\
&= e
\end{aligned}$$
Thus, $a * a' = e$. Hence, the left inverse is also a right inverse!

**Claim 2: The left identity is also a right identity ($a * e = a$).**
For any $a \in G$:
$$\begin{aligned}
a * e &= a * (a' * a) \quad (\text{since } a' * a = e) \\
&= (a * a') * a \quad (\text{by associativity}) \\
&= e * a \quad (\text{by Claim 1, } a * a' = e) \\
&= a \quad (\text{by A1})
\end{aligned}$$
Thus, $a * e = a$. The left identity is also a right identity.

Therefore, $(G, *)$ satisfies all standard two-sided group axioms. $\blacksquare$

---

**Part 2: Counterexample for Left Identity + Right Inverse**

Consider a set $G$ containing at least two distinct elements, say $G = \{e, x\}$ with $x \ne e$.
Define the binary operation $*$ by:
$$a * b = b, \quad \forall a, b \in G$$
(Every operation returns the right element).

Let us check the axioms:
1. **Associativity:**
   $(a * b) * c = b * c = c$, while $a * (b * c) = a * c = c$.
   Associativity holds for all triples!
2. **Left Identity:**
   $e * a = a$ for all $a \in G$.
   Thus $e$ is indeed a left identity!
3. **Right Inverses:**
   We require for every $a \in G$, there exists $b \in G$ such that $a * b = e$.
   By definition of our operation, $a * b = b$.
   Choosing $b = e$, we have $a * e = e$ for all $a \in G$!
   Hence every element has $e$ as its right inverse!

**Why this structure FAILS to be a group:**
Examine the right identity property:
$$x * e = e \ne x$$
The element $e$ is **not a right identity**!
Furthermore, left cancellation fails:
$$e * e = e \quad \text{and} \quad x * e = e$$
So $e * e = x * e$, but $e \ne x$!
Thus, a system with a left identity and right inverses does NOT necessarily form a group. $\blacksquare$"""
            }
        ]
    }
    return u1

if __name__ == "__main__":
    u = get_unit1()
    print("Unit 1 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
