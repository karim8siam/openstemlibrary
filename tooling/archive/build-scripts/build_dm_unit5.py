# -*- coding: utf-8 -*-
"""
build_dm_unit5.py
Constructs Unit 5: Relations, Posets, Lattices & Boolean Algebra
Strictly ZERO course numbers.
"""

def get_unit5():
    u5 = {
        "number": 5,
        "title": "Relations, Posets, Lattices & Boolean Algebra",
        "leadSummary": "Structural discrete mathematics: binary relations, reflexive, symmetric, and transitive closures via Warshall's algorithm, equivalence relations and set partitions, partially ordered sets (posets), Hasse diagrams, topological sorting (Kahn's algorithm), lattice theory (complete, distributive, modular lattices), algebraic axiomatization of Boolean algebras, canonical sum-of-products and product-of-sums representations, and algorithmic circuit minimization using 4-variable Karnaugh maps and Quine-McCluskey tabular reduction.",
        "simulations": ["sim_dm_karnaugh_map"],
        "sections": [
            {
                "secNumber": "5.1",
                "title": "Binary Relations, Closures & Equivalence Relations",
                "content": r"""### 1. Binary Relations and Foundational Properties

A **binary relation** $R$ from a set $A$ to a set $B$ is a subset of the Cartesian product $A \times B$. When $A = B$, $R \subseteq A \times A$ is called a binary relation on $A$. We write $a R b$ to denote $(a, b) \in R$.

#### Core Properties on Set $A$:
1. **Reflexive:** $\forall x \in A, \; (x, x) \in R$.
2. **Irreflexive:** $\forall x \in A, \; (x, x) \notin R$.
3. **Symmetric:** $\forall x, y \in A, \; (x, y) \in R \implies (y, x) \in R$.
4. **Antisymmetric:** $\forall x, y \in A, \; [(x, y) \in R \land (y, x) \in R] \implies x = y$.
5. **Transitive:** $\forall x, y, z \in A, \; [(x, y) \in R \land (y, z) \in R] \implies (x, z) \in R$.

---

### 2. Relational Closures and Warshall's Algorithm

The **closure** of a relation $R$ with respect to property $P$ is the minimal relation $R^* \supseteq R$ that satisfies property $P$.
- **Reflexive Closure:** $R \cup \Delta_A$, where $\Delta_A = \{(x, x) \mid x \in A\}$.
- **Symmetric Closure:** $R \cup R^{-1}$, where $R^{-1} = \{(y, x) \mid (x, y) \in R\}$.
- **Transitive Closure ($R^+$):** The reachability relation:
  $$R^+ = \bigcup_{k=1}^\infty R^k = R \cup R^2 \cup \dots \cup R^n \quad (\text{for } |A| = n)$$
  **Warshall's Algorithm** computes the transitive closure boolean matrix $W$ in $O(n^3)$ operations:
  $$W_{i,j}^{(k)} = W_{i,j}^{(k-1)} \lor \left( W_{i,k}^{(k-1)} \land W_{k,j}^{(k-1)} \right)$$

---

### 3. Equivalence Relations and Fundamental Partition Theorem

> **Definition 5.1 (Equivalence Relation):**
> A relation $R$ on a set $A$ is an **equivalence relation** if and only if it is reflexive, symmetric, and transitive.

For any $a \in A$, the **equivalence class** of $a$ modulo $R$ is:
$$[a]_R = \{x \in A \mid (a, x) \in R\}$$

> **Theorem 5.1 (Fundamental Partition Theorem):**
> Let $R$ be an equivalence relation on $A$.
> 1. For any $a, b \in A$, $[a] = [b] \iff (a, b) \in R$.
> 2. Any two equivalence classes are either identical or completely disjoint:
>    $$[a] \cap [b] \ne \emptyset \implies [a] = [b]$$
> 3. The family of equivalence classes partitions $A$ into non-empty, pairwise disjoint blocks whose union is $A$:
>    $$A / R = \{[a] \mid a \in A\}$$
> Conversely, any partition of $A$ uniquely induces an equivalence relation."""
            },
            {
                "secNumber": "5.2",
                "title": "Partially Ordered Sets (Posets), Hasse Diagrams & Topological Sort",
                "content": r"""### 1. Partially Ordered Sets (Posets)

> **Definition 5.2 (Poset):**
> A relation $R$ on set $A$ is a **partial order** (denoted $\le$ or $\preceq$) if it is **reflexive**, **antisymmetric**, and **transitive**. The pair $(A, \preceq)$ is called a **partially ordered set** or **poset**.

If every pair of elements in $A$ is comparable (i.e., $\forall x, y \in A$, either $x \preceq y$ or $y \preceq x$), then $(A, \preceq)$ is a **totally ordered set** (or chain / linear order).

---

### 2. Hasse Diagrams

A **Hasse diagram** is a graphical representation of a finite poset that eliminates redundant reflexive loops and transitive edges:
- Element $y$ **covers** $x$ (written $x \prec\!\!\cdot \; y$) if $x \prec y$ and there is no $z$ such that $x \prec z \prec y$.
- In the Hasse diagram, a directed upward line connects $x$ to $y$ if and only if $y$ covers $x$.

#### Extremal Elements in Posets:
- **Maximal element:** $m \in A$ such that $\forall x \in A, \; m \preceq x \implies x = m$.
- **Minimal element:** $m \in A$ such that $\forall x \in A, \; x \preceq m \implies x = m$.
- **Greatest element (Maximum / Top $\mathbf{1}$):** $g \in A$ such that $\forall x \in A, \; x \preceq g$ (unique if it exists).
- **Least element (Minimum / Bottom $\mathbf{0}$):** $\ell \in A$ such that $\forall x \in A, \; \ell \preceq x$ (unique if it exists).

---

### 3. Topological Sorting

A **topological sort** of a finite poset $(A, \preceq)$ is a linear extension $\le_L$ of $\preceq$ such that:
$$\forall x, y \in A, \quad x \prec y \implies x <_L y$$
Algorithmically, topological sorting arranges the vertices of a Directed Acyclic Graph (DAG) such that every directed edge $(u, v)$ has $u$ appearing before $v$.
- **Kahn's Algorithm:** Repeatedly find a vertex with in-degree 0 (a minimal element), output it, and remove its outgoing edges. Runs in $O(|V| + |E|)$ time."""
            },
            {
                "secNumber": "5.3",
                "title": "Lattices: Semilattices, Distributive & Modular Lattices",
                "content": r"""### 1. Poset-Theoretic Definition of Lattices

Let $(L, \preceq)$ be a poset. For any subset $S \subseteq L$:
- An **upper bound** of $S$ is $u \in L$ such that $\forall s \in S, s \preceq u$. The **least upper bound (lub)** or **join** is denoted $\sup(S)$ or $\bigvee S$. For two elements, $a \lor b = \text{lub}(a, b)$.
- A **lower bound** of $S$ is $\ell \in L$ such that $\forall s \in S, \ell \preceq s$. The **greatest lower bound (glb)** or **meet** is denoted $\inf(S)$ or $\bigwedge S$. For two elements, $a \land b = \text{glb}(a, b)$.

> **Definition 5.3 (Lattice):**
> A poset $(L, \preceq)$ is a **lattice** if every pair of elements $\{a, b\} \subseteq L$ has a unique join ($a \lor b$) and a unique meet ($a \land b$).

---

### 2. Algebraic Definition of Lattices

Equivalently, a lattice is an algebraic structure $(L, \lor, \land)$ with two binary operations satisfying:
1. **Idempotent Laws:** $a \lor a = a, \quad a \land a = a$.
2. **Commutative Laws:** $a \lor b = b \lor a, \quad a \land b = b \land a$.
3. **Associative Laws:** $(a \lor b) \lor c = a \lor (b \lor c), \quad (a \land b) \land c = a \land (b \land c)$.
4. **Absorption Laws:** $a \lor (a \land b) = a, \quad a \land (a \lor b) = a$.

The partial order is recovered algebraically by:
$$a \preceq b \iff a \land b = a \iff a \lor b = b$$

---

### 3. Distributive, Bounded, and Complemented Lattices

- **Distributive Lattice:** Satisfies the distributive identities for all $a, b, c \in L$:
  $$a \land (b \lor c) = (a \land b) \lor (a \land c), \qquad a \lor (b \land c) = (a \lor b) \land (a \lor c)$$
  *(Birkhoff's Theorem: A lattice is distributive iff it does not contain the pentagon lattice $N_5$ or the diamond lattice $M_3$ as a sublattice).*
- **Bounded Lattice:** Contains a bottom element $\mathbf{0}$ and top element $\mathbf{1}$:
  $$a \lor \mathbf{0} = a, \quad a \land \mathbf{0} = \mathbf{0}, \quad a \lor \mathbf{1} = \mathbf{1}, \quad a \land \mathbf{1} = a$$
- **Complemented Lattice:** In a bounded lattice, an element $b$ is a **complement** of $a$ if $a \lor b = \mathbf{1}$ and $a \land b = \mathbf{0}$.
  In a distributive lattice, complements are **unique** whenever they exist."""
            },
            {
                "secNumber": "5.4",
                "title": "Boolean Algebra Axiomatization, Dualities & Canonical SOP/POS",
                "content": r"""### 1. Axiomatic Definition of Boolean Algebra

> **Definition 5.4 (Boolean Algebra):**
> A **Boolean algebra** is a 6-tuple $(B, +, \cdot, ', \mathbf{0}, \mathbf{1})$ consisting of a set $B$, two binary operations $+$ (join / OR) and $\cdot$ (meet / AND), a unary operation $'$ (complement / NOT), and two distinct constants $\mathbf{0}, \mathbf{1} \in B$ satisfying Huntington's axioms:
> 1. **Closure:** $\forall a, b \in B, \; a + b \in B \text{ and } a \cdot b \in B$.
> 2. **Commutativity:** $a + b = b + a$ and $a \cdot b = b \cdot a$.
> 3. **Distributivity:**
>    $$a \cdot (b + c) = (a \cdot b) + (a \cdot c)$$
>    $$a + (b \cdot c) = (a + b) \cdot (a + c)$$
> 4. **Identity Elements:** $a + \mathbf{0} = a$ and $a \cdot \mathbf{1} = a$.
> 5. **Complements:** $a + a' = \mathbf{1}$ and $a \cdot a' = \mathbf{0}$.

---

### 2. Principle of Duality

> **The Duality Principle:**
> Any algebraic theorem in Boolean algebra remains strictly valid if one interchanges $+$ with $\cdot$, and $\mathbf{0}$ with $\mathbf{1}$ throughout the entire statement.

---

### 3. Canonical Representations: SOP and POS

Let $f(x_1, x_2, \dots, x_n)$ be a Boolean function of $n$ variables.

1. **Minterm ($m_i$):** A product (AND) of $n$ literals in which each variable appears once in either uncomplemented or complemented form. There are $2^n$ possible minterms.
2. **Canonical Sum-of-Products (SOP / DNF):**
   $$f(x_1, \dots, x_n) = \sum_{m_i \in \text{ON-set}} m_i = \bigvee_{f(\mathbf{v}) = 1} \left( \prod_{j=1}^n \tilde{x}_j \right)$$
3. **Maxterm ($M_i$):** A sum (OR) of $n$ literals.
4. **Canonical Product-of-Sums (POS / CNF):**
   $$f(x_1, \dots, x_n) = \prod_{M_i \in \text{OFF-set}} M_i = \bigwedge_{f(\mathbf{v}) = 0} \left( \sum_{j=1}^n \tilde{x}_j \right)$$"""
            },
            {
                "secNumber": "5.5",
                "title": "Karnaugh Map Minimization & Quine-McCluskey Algorithm",
                "content": r"""### 1. Karnaugh Map (K-Map) Theory

A **Karnaugh map** is a visual representation of a Boolean function where adjacent cells represent minterms that differ by exactly **one bit** (Hamming distance 1). This is achieved by organizing row and column indices using **Gray code** sequences:
$$\text{Gray Code for 2 bits: } 00 \to 01 \to 11 \to 10$$

```
       CD
  AB   00   01   11   10
  00   m0   m1   m3   m2
  01   m4   m5   m7   m6
  11  m12  m13  m15  m14
  10   m8   m9  m11  m10
```

#### Looping Rules for Minimization:
- Groups (implicants) must be rectangular powers of two ($1, 2, 4, 8, 16$).
- Opposite edges wrap around (toroidal topology: top wraps to bottom, left wraps to right).
- Groups must be as large as possible.
- An **Essential Prime Implicant (EPI)** is an implicant containing at least one minterm $1$ that is not covered by any other prime implicant.

---

### 2. The Quine-McCluskey Algorithmic Reduction

For functions with $\ge 5$ variables, visual K-maps become unwieldy. The **Quine-McCluskey algorithm** provides an exact, tabular algebraic optimization:
1. Group minterms by the number of 1s in their binary representation (Hamming weight).
2. Compare terms in adjacent groups differing by a single bit position; combine them using $x y + x y' = x$ and mark with a dash ($-$).
3. Repeat iteratively until no further combinations are possible. The uncombined terms are the **Prime Implicants (PI)**.
4. Construct the **Prime Implicant Chart** (PI rows $\times$ minterm columns).
5. Identify columns with a single $\times$ to select Essential Prime Implicants, delete covered columns, and solve the remaining minimal covering problem (via Petrick's method)."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 5.1: Rigorous Equivalence Relation Construction for Rational Numbers",
                "statement": r"""Let $S = \mathbb{Z} \times (\mathbb{Z} \setminus \{0\})$, the set of all ordered pairs of integers $(a, b)$ with $b \ne 0$.
Define the binary relation $\sim$ on $S$ by:
$$(a, b) \sim (c, d) \iff a d = b c$$
1. Prove rigorously that $\sim$ is an equivalence relation on $S$.
2. Explain the mathematical significance of the quotient set $S / \sim$ in the formal construction of the rational numbers $\mathbb{Q}$.
3. Prove that addition defined on equivalence classes by $[(a, b)] + [(c, d)] = [(a d + b c, b d)]$ is well-defined (independent of the choice of representative).""",
                "hints": [
                    "Verify Reflexivity, Symmetry, and Transitivity.",
                    "For transitivity, multiply $(ad = bc)$ by $f$ and use $cf = de$ with $c \\ne 0$ or by case analysis.",
                    "Well-definedness requires showing $(a_1, b_1) \\sim (a_2, b_2)$ and $(c_1, d_1) \\sim (c_2, d_2)$ implies $(a_1 d_1 + b_1 c_1, b_1 d_1) \\sim (a_2 d_2 + b_2 c_2, b_2 d_2)$."
                ],
                "solution": r"""### 1. Proof of Equivalence Relation

#### A. Reflexivity
For any $(a, b) \in S$:
$$a \cdot b = b \cdot a$$
by commutativity of integer multiplication.
Therefore, $(a, b) \sim (a, b)$. Reflexivity holds.

#### B. Symmetry
Let $(a, b) \sim (c, d)$. By definition:
$$a d = b c \implies c b = d a \implies c b = a d$$
which means $c b = d a \iff c d = \dots$ specifically $c b = d a$.
Thus $(c, d) \sim (a, b)$. Symmetry holds.

#### C. Transitivity
Let $(a, b) \sim (c, d)$ and $(c, d) \sim (e, f)$ for $(a, b), (c, d), (e, f) \in S$.
By definition:
1. $a d = b c$
2. $c f = d e$

Multiply equation 1 by $f$:
$$(a d) f = (b c) f \implies a d f = b (c f)$$
Substitute equation 2 ($c f = d e$):
$$a d f = b (d e) \implies d (a f) = d (b e) \implies d (a f - b e) = 0$$
Since $(c, d) \in S$, by definition $d \ne 0$.
In the integral domain $\mathbb{Z}$, a product of two integers is zero only if at least one factor is zero. Since $d \ne 0$, we must have:
$$a f - b e = 0 \implies a f = b e$$
Therefore, $(a, b) \sim (e, f)$. Transitivity holds.

Since $\sim$ is reflexive, symmetric, and transitive, it is an equivalence relation.

---

### 2. Quotient Set and $\mathbb{Q}$
The equivalence class $[(a, b)]$ represents the fraction $\frac{a}{b}$.
Different pairs such as $(1, 2), (2, 4), (-3, -6)$ all satisfy $1(4) = 2(2)$, etc., and therefore belong to the exact same equivalence class:
$$[(1, 2)] = [(2, 4)] = [(-3, -6)] = \frac{1}{2}$$
The quotient set $S / \sim$ is precisely the field of rational numbers $\mathbb{Q}$.

---

### 3. Proof of Well-Defined Addition
Suppose $(a_1, b_1) \sim (a_2, b_2)$ and $(c_1, d_1) \sim (c_2, d_2)$.
Then $a_1 b_2 = b_1 a_2$ and $c_1 d_2 = d_1 c_2$.
We must prove that:
$$(a_1 d_1 + b_1 c_1, b_1 d_1) \sim (a_2 d_2 + b_2 c_2, b_2 d_2)$$
which requires showing:
$$(a_1 d_1 + b_1 c_1)(b_2 d_2) = (b_1 d_1)(a_2 d_2 + b_2 c_2)$$
Expand the LHS:
$$\text{LHS} = a_1 d_1 b_2 d_2 + b_1 c_1 b_2 d_2 = (a_1 b_2)(d_1 d_2) + (b_1 b_2)(c_1 d_2)$$
Substitute $a_1 b_2 = b_1 a_2$ and $c_1 d_2 = d_1 c_2$:
$$\text{LHS} = (b_1 a_2)(d_1 d_2) + (b_1 b_2)(d_1 c_2) = a_2 b_1 d_1 d_2 + b_1 b_2 d_1 c_2$$
Expand the RHS:
$$\text{RHS} = b_1 d_1 a_2 d_2 + b_1 d_1 b_2 c_2 = a_2 b_1 d_1 d_2 + b_1 b_2 d_1 c_2$$
Clearly $\text{LHS} = \text{RHS}$.
Thus, the addition operation on equivalence classes is completely well-defined. $\blacksquare$"""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 5.2: Divisor Lattice $D_{36}$, Distributivity, and Complementation",
                "statement": r"""Consider the set $D_{36}$ of all positive integer divisors of $36$, partially ordered by the divisibility relation $|$ (where $x \preceq y \iff x \mid y$).
1. List all 9 elements of $D_{36}$ and sketch its Hasse diagram by identifying covering relations.
2. Define the meet ($\land$) and join ($\lor$) operations in this poset and identify the bottom ($\mathbf{0}$) and top ($\mathbf{1}$) elements.
3. Determine whether $(D_{36}, \mid)$ is a distributive lattice.
4. Determine which elements of $D_{36}$ have complements, and conclude whether $D_{36}$ is a Boolean algebra.""",
                "hints": [
                    "Prime factorization: $36 = 2^2 \\cdot 3^2$. The number of divisors is $(2+1)(2+1) = 9$.",
                    "Meet is $\\gcd(a, b)$ and join is $\\text{lcm}(a, b)$.",
                    "A finite distributive lattice is a Boolean algebra if and only if it is square-free (isomorphic to a power set lattice)."
                ],
                "solution": r"""### 1. Elements and Hasse Diagram of $D_{36}$
Since $36 = 2^2 \times 3^2$, its divisors have the form $2^a 3^b$ with $a \in \{0, 1, 2\}$ and $b \in \{0, 1, 2\}$.
The 9 divisors are:
$$D_{36} = \{1, 2, 3, 4, 6, 9, 12, 18, 36\}$$

#### Covering Relations ($x \prec\!\!\cdot \; y \iff y/x \text{ is prime}$):
- $1 \prec\!\!\cdot \; 2$, $1 \prec\!\!\cdot \; 3$.
- $2 \prec\!\!\cdot \; 4$, $2 \prec\!\!\cdot \; 6$.
- $3 \prec\!\!\cdot \; 6$, $3 \prec\!\!\cdot \; 9$.
- $4 \prec\!\!\cdot \; 12$.
- $6 \prec\!\!\cdot \; 12$, $6 \prec\!\!\cdot \; 18$.
- $9 \prec\!\!\cdot \; 18$.
- $12 \prec\!\!\cdot \; 36$, $18 \prec\!\!\cdot \; 36$.

The Hasse diagram forms a $3 \times 3$ grid rotated 45 degrees, isomorphic to the product poset $\mathbf{3} \times \mathbf{3}$ where $\mathbf{3} = \{0, 1, 2\}$.

---

### 2. Lattice Operations and Bounds
For the divisibility partial order:
- **Meet:** $a \land b = \gcd(a, b)$ (greatest common divisor).
- **Join:** $a \lor b = \text{lcm}(a, b)$ (least common multiple).
- **Bottom Element $\mathbf{0}$:** The divisor dividing all others is $\mathbf{0} = 1$.
- **Top Element $\mathbf{1}$:** The multiple divided by all others is $\mathbf{1} = 36$.

---

### 3. Distributivity of $D_{36}$
In any divisibility lattice $D_n$, prime factorizations determine the exponents:
If $a = 2^{a_1} 3^{a_2}$, $b = 2^{b_1} 3^{b_2}$, $c = 2^{c_1} 3^{c_2}$, then:
- $\gcd(a, b)$ takes $\min(a_i, b_i)$ for each prime exponent.
- $\text{lcm}(a, b)$ takes $\max(a_i, b_i)$ for each prime exponent.
In the real numbers under min and max, the distributive law holds:
$$\min(a_i, \max(b_i, c_i)) = \max(\min(a_i, b_i), \min(a_i, c_i))$$
Since the exponents distribute coordinate-wise, $D_{36}$ is a **distributive lattice**.

---

### 4. Complementation and Boolean Algebra Test
In a bounded lattice with $\mathbf{0} = 1$ and $\mathbf{1} = 36$, a complement $x'$ of $x$ must satisfy:
$$x \land x' = \gcd(x, x') = 1 \quad \text{and} \quad x \lor x' = \text{lcm}(x, x') = 36$$
Let us test the element $x = 2$:
We need $\gcd(2, x') = 1 \implies x'$ cannot be divisible by 2.
Divisors in $D_{36}$ not divisible by 2 are: $\{1, 3, 9\}$.
- $\text{lcm}(2, 1) = 2 \ne 36$.
- $\text{lcm}(2, 3) = 6 \ne 36$.
- $\text{lcm}(2, 9) = 18 \ne 36$.
None of these yield $\text{lcm} = 36$!
Therefore, the element $2$ has **no complement** in $D_{36}$.

**Conclusion:** Although $D_{36}$ is a distributive lattice, it is **not complemented**. Consequently, $D_{36}$ is **not a Boolean algebra** (it is not isomorphic to $\mathcal{P}(S)$ because 36 has square prime factors $2^2$ and $3^2$). $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 5.3: Minimal SOP Optimization via Quine-McCluskey & NAND Gate Synthesis",
                "statement": r"""Consider the four-variable Boolean function:
$$f(A, B, C, D) = \sum m(0, 2, 5, 7, 8, 10, 13, 15)$$

1. Plot $f(A, B, C, D)$ on a 4-variable Gray-coded Karnaugh map. Identify all groupings, prime implicants, and essential prime implicants.
2. Perform the complete tabular **Quine-McCluskey reduction**:
   - Categorize minterms by Hamming weight (number of 1s).
   - Generate size-2 and size-4 implicants.
   - Construct the Prime Implicant Chart and prove whether the minimal SOP is unique.
3. Synthesize the resulting minimal SOP expression using **only 2-input NAND gates**.""",
                "hints": [
                    "Notice the symmetry between minterms: $(0, 2, 8, 10)$ form the four corners of the K-map.",
                    "$(5, 7, 13, 15)$ form a $2 \\times 2$ square in the center.",
                    "Four corners combine to $B' D'$. Center square combines to $B D$."
                ],
                "solution": r"""### 1. Karnaugh Map Grouping
Binary representations of the minterms:
- $m_0 = 0000, \; m_2 = 0010, \; m_8 = 1000, \; m_{10} = 1010$.
- $m_5 = 0101, \; m_7 = 0111, \; m_{13} = 1101, \; m_{15} = 1111$.

Plotting on the $4 \times 4$ K-map ($AB$ rows $\times$ $CD$ columns):
- Row 00 ($A'B'$): $m_0(00) = 1, \; m_2(10) = 1$.
- Row 01 ($A'B$): $m_5(01) = 1, \; m_7(11) = 1$.
- Row 11 ($AB$): $m_{13}(01) = 1, \; m_{15}(11) = 1$.
- Row 10 ($AB'$): $m_8(00) = 1, \; m_{10}(10) = 1$.

#### Identification of Groups:
1. **The Four Corners:** $\{m_0, m_2, m_8, m_{10}\}$:
   - $A$ changes ($0 \to 1$), $B = 0$ ($B'$).
   - $C$ changes ($0 \to 1$), $D = 0$ ($D'$).
   - Simplified implicant: $B' D'$.
2. **The Center 4-Square:** $\{m_5, m_7, m_{13}, m_{15}\}$:
   - Rows: $01, 11 \implies B = 1$.
   - Columns: $01, 11 \implies D = 1$.
   - Simplified implicant: $B D$.

Every minterm is covered by exactly one of these two size-4 groups:
- Corners cover $\{0, 2, 8, 10\}$.
- Center square covers $\{5, 7, 13, 15\}$.
Both groups are **Essential Prime Implicants**.
Minimal Sum-of-Products:
$$f(A, B, C, D) = B' D' + B D$$
Notice that this is precisely the XNOR function: $f = (B \oplus D)'$!

---

### 2. Quine-McCluskey Tabular Reduction

#### Step A: Grouping by Hamming Weight
- **Group 0 (Weight 0):**
  $m_0: 0000$
- **Group 1 (Weight 1):**
  $m_2: 0010$, $m_8: 1000$
- **Group 2 (Weight 2):**
  $m_{10}: 1010$, $m_5: 0101$
- **Group 3 (Weight 3):**
  $m_7: 0111$, $m_{13}: 1101$
- **Group 4 (Weight 4):**
  $m_{15}: 1111$

#### Step B: Size-2 Implicants (Combine Groups Differing by 1 Bit)
- $(0, 2): 00-0$
- $(0, 8): -000$
- $(2, 10): -010$
- $(8, 10): 10-0$
- $(5, 7): 01-1$
- $(5, 13): -101$
- $(7, 15): -111$
- $(13, 15): 11-1$

#### Step C: Size-4 Implicants
- Combine $(0, 2)$ with $(8, 10) \implies (0, 2, 8, 10): -0-0 \implies B' D'$ (Term 1)
- Combine $(0, 8)$ with $(2, 10) \implies (0, 2, 8, 10): -0-0$ (Duplicate)
- Combine $(5, 7)$ with $(13, 15) \implies (5, 7, 13, 15): -1-1 \implies B D$ (Term 2)
- Combine $(5, 13)$ with $(7, 15) \implies (5, 7, 13, 15): -1-1$ (Duplicate)

All size-2 implicants combine into the two size-4 terms.
The Prime Implicants are:
$$P_1 = B' D', \qquad P_2 = B D$$

#### Step D: Prime Implicant Chart

| PI | Minterms Covered | 0 | 2 | 5 | 7 | 8 | 10 | 13 | 15 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $P_1 = B' D'$ | 0, 2, 8, 10 | $\times$ | $\times$ | | | $\times$ | $\times$ | | |
| $P_2 = B D$ | 5, 7, 13, 15 | | | $\times$ | $\times$ | | | $\times$ | $\times$ |

Each minterm column contains exactly one $\times$. Therefore, both $P_1$ and $P_2$ are strictly essential, and the minimal SOP expression is **uniquely**:
$$f = B' D' + B D$$

---

### 3. Synthesis using 2-input NAND Gates
We transform $f = B' D' + B D$ using De Morgan's involution:
$$f = \left( (B' D' + B D)' \right)' = \Big( (B' D')' \cdot (B D)' \Big)' = \text{NAND}\Big( (B' D')', (B D)' \Big)$$

Using only 2-input NAND gates:
1. Generate $B'$: $g_1 = \text{NAND}(B, B)$.
2. Generate $D'$: $g_2 = \text{NAND}(D, D)$.
3. Generate $(B' D')'$: $g_3 = \text{NAND}(g_1, g_2) = \text{NAND}(B', D')$.
4. Generate $(B D)'$: $g_4 = \text{NAND}(B, D)$.
5. Output gate: $f = \text{NAND}(g_3, g_4)$.

Total circuit cost: exactly **5 two-input NAND gates**. $\blacksquare$"""
            }
        ]
    }
    return u5

if __name__ == "__main__":
    u5 = get_unit5()
    print(f"Loaded Unit 5: {u5['title']} with {len(u5['sections'])} sections and {len(u5['problems'])} problems.")
