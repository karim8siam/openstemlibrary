# -*- coding: utf-8 -*-
"""
build_dm_unit3.py
Constructs Unit 3: Combinatorial Analysis, Pigeonhole Principle & Inclusion-Exclusion
Strictly ZERO course numbers.
"""

def get_unit3():
    u3 = {
        "number": 3,
        "title": "Combinatorial Analysis, Pigeonhole Principle & Inclusion-Exclusion",
        "leadSummary": "Exhaustive treatment of combinatorial enumerative theory: addition and multiplication principles, permutations, combinations with and without repetition, binomial theorem and Vandermonde convolutions, Dirichlet's pigeonhole principle and generalized pigeonhole with applications to Erdős-Szekeres and Ramsey theory, the Principle of Inclusion-Exclusion (PIE), derangements, Euler's totient function, and stars-and-bars integer partitions.",
        "simulations": ["sim_dm_combinatorics_pigeonhole"],
        "sections": [
            {
                "secNumber": "3.1",
                "title": "Fundamental Counting Principles: Sum, Product, Permutations & Combinations",
                "content": r"""### 1. The Fundamental Rules of Enumeration

Enumerative combinatorics is the rigorous mathematical discipline of counting finite discrete configurations.

1. **The Rule of Sum (Addition Principle):**
   If a task can be done in either one of $n_1$ ways or one of $n_2$ ways, where the two sets of ways are mutually disjoint ($A \cap B = \emptyset$), then the task can be performed in:
   $$|A \cup B| = |A| + |B| = n_1 + n_2 \text{ ways}$$
   More generally, for pairwise disjoint sets $A_1, A_2, \dots, A_k$:
   $$\left| \bigcup_{i=1}^k A_i \right| = \sum_{i=1}^k |A_i|$$

2. **The Rule of Product (Multiplication Principle):**
   If a procedure can be broken down into a sequence of two independent steps, where step 1 can be carried out in $n_1$ ways and subsequent step 2 can be carried out in $n_2$ ways regardless of the choice in step 1, then the total number of ways to execute the sequence is:
   $$|A \times B| = |A| \cdot |B| = n_1 \cdot n_2 \text{ ways}$$

---

### 2. Permutations (Order Matters)

An **$r$-permutation** of a set of $n$ distinct elements is an ordered arrangement of $r$ elements selected from the set.

> **Theorem 3.1 (Permutations without Repetition):**
> The number of $r$-permutations of a set of $n$ distinct elements is:
> $$P(n, r) \equiv {}_n P_r = \frac{n!}{(n - r)!} = n(n-1)(n-2)\cdots(n-r+1)$$

*Proof:* By the product rule, the first position can be filled in $n$ ways, the second in $n-1$ ways, down to the $r$-th position in $n - (r - 1) = n - r + 1$ ways. $\blacksquare$

- **Permutations with Repetition:** If elements can be selected with unlimited replacement, there are $n^r$ distinct ordered sequences of length $r$.
- **Permutations with Indistinguishable Elements:** The number of permutations of $n$ objects of which $n_1$ are of type 1, $n_2$ are of type 2, $\dots$, $n_k$ are of type $k$ (with $\sum n_i = n$) is given by the **multinomial coefficient**:
  $$\binom{n}{n_1, n_2, \dots, n_k} = \frac{n!}{n_1! \, n_2! \cdots n_k!}$$

---

### 3. Combinations (Order Does Not Matter)

An **$r$-combination** of a set of $n$ distinct elements is an unordered selection of $r$ elements from the set.

> **Theorem 3.2 (Combinations without Repetition):**
> The number of $r$-combinations from $n$ distinct elements is:
> $$C(n, r) \equiv \binom{n}{r} = \frac{P(n, r)}{r!} = \frac{n!}{r! \, (n - r)!}$$

*Proof:* Each unordered subset of size $r$ can be ordered in $r!$ distinct ways to form permutations. By the division principle, $\binom{n}{r} \cdot r! = P(n, r) \implies \binom{n}{r} = \frac{n!}{r!(n-r)!}$. $\blacksquare$"""
            },
            {
                "secNumber": "3.2",
                "title": "Binomial Theorem, Multinomial Coefficients & Combinatorial Identities",
                "content": r"""### 1. The Binomial Theorem

> **Theorem 3.3 (Binomial Theorem):**
> Let $x$ and $y$ be real variables and $n \in \mathbb{N}$. Then:
> $$(x + y)^n = \sum_{k=0}^n \binom{n}{k} x^{n-k} y^k = \binom{n}{0} x^n + \binom{n}{1} x^{n-1} y + \dots + \binom{n}{n} y^n$$

*Combinatorial Proof:*
The product $(x + y)^n = (x + y)(x + y)\cdots(x + y)$ contains $n$ factors. When expanding, we choose either $x$ or $y$ from each factor. The term $x^{n-k} y^k$ arises whenever we choose $y$ from exactly $k$ factors and $x$ from the remaining $n-k$ factors. The number of ways to pick $k$ factors out of $n$ to supply $y$ is precisely $\binom{n}{k}$. Summing over all $k \in \{0, 1, \dots, n\}$ yields the theorem. $\blacksquare$

---

### 2. Fundamental Combinatorial Identities

1. **Symmetry Identity:**
   $$\binom{n}{k} = \binom{n}{n - k}$$

2. **Pascal's Identity:**
   $$\binom{n}{k} = \binom{n - 1}{k - 1} + \binom{n - 1}{k} \qquad (1 \le k \le n - 1)$$
   *Combinatorial Proof:* Let $S$ have $n$ elements and distinguish element $x_0 \in S$. Subsets of size $k$ either contain $x_0$ (leaving $k-1$ elements to choose from $n-1$) or do not contain $x_0$ (leaving $k$ elements to choose from $n-1$). Summing these disjoint cases proves the identity.

3. **Sum of Binomial Coefficients:**
   $$\sum_{k=0}^n \binom{n}{k} = 2^n \qquad (\text{evaluate } (1 + 1)^n)$$
   $$\sum_{k=0}^n (-1)^k \binom{n}{k} = 0 \qquad (\text{evaluate } (1 - 1)^n)$$

4. **Vandermonde's Convolution Identity:**
   > **Theorem 3.4 (Vandermonde's Identity):**
   > For positive integers $m, n, r$:
   > $$\binom{m + n}{r} = \sum_{k=0}^r \binom{m}{k} \binom{n}{r - k}$$
   *Proof:* Consider a group of $m$ men and $n$ women. Choosing a committee of $r$ people from the total $m + n$ pool can be partitioned by the number of men $k \in \{0, 1, \dots, r\}$ on the committee, with the remaining $r - k$ chosen from women. $\blacksquare$"""
            },
            {
                "secNumber": "3.3",
                "title": "The Pigeonhole Principle & Generalized Ramsey Bounds",
                "content": r"""### 1. Dirichlet's Pigeonhole Principle

> **Theorem 3.5 (Pigeonhole Principle):**
> If $k + 1$ or more pigeons are placed into $k$ pigeonholes, then there is at least one pigeonhole containing two or more pigeons.

*Proof by Contradiction:*
Assume that no pigeonhole contains two or more pigeons. Then each of the $k$ pigeonholes contains at most 1 pigeon. The total number of pigeons would be at most $k \cdot 1 = k$. But we were given at least $k + 1$ pigeons, a contradiction ($k + 1 \le k$). $\blacksquare$

---

### 2. The Generalized Pigeonhole Principle

> **Theorem 3.6 (Generalized Pigeonhole Principle):**
> If $N$ objects are placed into $k$ boxes, then there is at least one box containing at least:
> $$\left\lceil \frac{N}{k} \right\rceil \text{ objects}$$
> where $\lceil x \rceil$ is the ceiling function (least integer $\ge x$).

*Proof:*
Assume every box contains at most $\lceil N / k \rceil - 1$ objects. Then the total number of objects is at most:
$$k \left( \left\lceil \frac{N}{k} \right\rceil - 1 \right) < k \left( \left( \frac{N}{k} + 1 \right) - 1 \right) = N$$
contradicting the presence of $N$ objects. $\blacksquare$

---

### 3. Erdős-Szekeres Monotonic Subsequence Theorem

> **Theorem 3.7 (Erdős-Szekeres Theorem):**
> Every sequence of $n^2 + 1$ distinct real numbers contains a strictly increasing subsequence of length $n + 1$ or a strictly decreasing subsequence of length $n + 1$.

*Proof using Pigeonhole Principle:*
1. Let the sequence be $a_1, a_2, \dots, a_{n^2 + 1}$.
2. For each index $k \in \{1, \dots, n^2 + 1\}$, associate the ordered pair $(i_k, d_k)$:
   - $i_k$: length of the longest increasing subsequence beginning with $a_k$.
   - $d_k$: length of the longest decreasing subsequence beginning with $a_k$.
3. Assume for contradiction that no increasing or decreasing subsequence of length $n + 1$ exists.
4. Then for all $k$, $1 \le i_k \le n$ and $1 \le d_k \le n$.
5. The number of possible distinct pairs $(i, d)$ is $n \times n = n^2$.
6. There are $n^2 + 1$ indices $k$, which act as pigeons placed into $n^2$ box pairs.
7. By the Pigeonhole Principle, there must exist two distinct indices $j < k$ such that $(i_j, d_j) = (i_k, d_k)$.
8. Since all numbers are distinct, either $a_j < a_k$ or $a_j > a_k$:
   - If $a_j < a_k$: We can prepend $a_j$ to the longest increasing subsequence starting at $a_k$, yielding an increasing subsequence starting at $a_j$ of length $i_k + 1$. Thus $i_j \ge i_k + 1 > i_k$, contradicting $i_j = i_k$!
   - If $a_j > a_k$: We can prepend $a_j$ to the longest decreasing subsequence starting at $a_k$, yielding $d_j \ge d_k + 1 > d_k$, contradicting $d_j = d_k$!
9. In both cases a contradiction arises. Therefore, at least one subsequence of length $n + 1$ must exist. $\blacksquare$"""
            },
            {
                "secNumber": "3.4",
                "title": "Principle of Inclusion-Exclusion (PIE), Surjections & Derangements",
                "content": r"""### 1. The General Principle of Inclusion-Exclusion (PIE)

For two finite sets: $|A \cup B| = |A| + |B| - |A \cap B|$.
For three sets:
$$|A \cup B \cup C| = |A| + |B| + |C| - (|A \cap B| + |A \cap C| + |B \cap C|) + |A \cap B \cap C|$$

> **Theorem 3.8 (General PIE Theorem):**
> Let $A_1, A_2, \dots, A_n$ be finite sets. Then:
> $$\left| \bigcup_{i=1}^n A_i \right| = \sum_{k=1}^n (-1)^{k-1} \sum_{1 \le i_1 < i_2 < \dots < i_k \le n} \left| A_{i_1} \cap A_{i_2} \cap \dots \cap A_{i_k} \right|$$

*Proof:*
Let an arbitrary element $x$ belong to exactly $m$ of the sets $A_1, \dots, A_n$ (where $1 \le m \le n$).
In the RHS summation:
- It is counted $\binom{m}{1}$ times in the single-set terms.
- It is subtracted $\binom{m}{2}$ times in the pairwise intersections.
- In general, it is counted $(-1)^{k-1} \binom{m}{k}$ times in the $k$-wise intersections.
Total times $x$ is counted on the RHS:
$$\sum_{k=1}^m (-1)^{k-1} \binom{m}{k} = -\sum_{k=1}^m (-1)^k \binom{m}{k} = -\left[ (1 - 1)^m - \binom{m}{0} \right] = -[0 - 1] = 1$$
Every element in the union is counted exactly once, and any element outside the union is counted 0 times. $\blacksquare$

---

### 2. The Number of Surjective (Onto) Functions

Let $|A| = m$ and $|B| = n$ with $m \ge n$.
The number of surjective functions $f: A \twoheadrightarrow B$ is:
$$S(m, n) = \sum_{k=0}^n (-1)^k \binom{n}{k} (n - k)^m = n! \cdot S_2(m, n)$$
where $S_2(m, n)$ is the Stirling number of the second kind (partitions of an $m$-set into $n$ non-empty subsets).

---

### 3. Derangements ($D_n$ or $!n$)

A **derangement** is a permutation of $\{1, 2, \dots, n\}$ such that no element appears in its original position ($\forall i, \pi(i) \ne i$).

> **Theorem 3.9 (Derangement Formula):**
> The number of derangements of $n$ elements is:
> $$D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!} = n! \left( 1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \dots + \frac{(-1)^n}{n!} \right)$$
> As $n \to \infty$, the probability that a random permutation is a derangement rapidly converges to:
> $$\lim_{n \to \infty} \frac{D_n}{n!} = \sum_{k=0}^\infty \frac{(-1)^k}{k!} = \frac{1}{e} \approx 0.367879...$$"""
            },
            {
                "secNumber": "3.5",
                "title": "Stars and Bars, Integer Partitions & Interactive PIE Simulator",
                "content": r"""### 1. Stars and Bars Method (Bose-Einstein Statistics)

The problem of distributing $n$ indistinguishable items into $k$ distinguishable bins is isomorphic to counting non-negative integer solutions to:
$$x_1 + x_2 + \dots + x_k = n, \qquad x_i \in \{0, 1, 2, \dots\}$$

> **Theorem 3.10 (Stars and Bars):**
> 1. The number of **non-negative** integer solutions ($x_i \ge 0$) to $x_1 + \dots + x_k = n$ is:
>    $$\binom{n + k - 1}{k - 1} = \binom{n + k - 1}{n}$$
> 2. The number of **strictly positive** integer solutions ($x_i \ge 1$) to $x_1 + \dots + x_k = n$ (with $n \ge k$) is:
>    $$\binom{n - 1}{k - 1}$$

*Proof (Geometric Stars and Bars):*
- Represent the $n$ indistinguishable items as $n$ stars ($*$).
- Bins are demarcated by $k - 1$ divider bars ($|$).
- Any arrangement of $n$ stars and $k-1$ bars represents a unique solution.
- The total number of symbols is $n + (k - 1) = n + k - 1$.
- The number of distinct arrangements is the number of ways to choose the $k-1$ positions for the bars from the total $n + k - 1$ positions: $\binom{n + k - 1}{k - 1}$. $\blacksquare$

---

### 2. Interactive Pigeonhole & PIE Venn Diagram Simulator

The interactive simulation below allows visual exploration of:
- **Pigeonhole Allocation:** Dynamic distribution of pigeons into boxes with real-time detection of overloaded boxes satisfying $\lceil N/k \rceil$.
- **3-Set Inclusion-Exclusion Venn Diagram:** Interactive area computation illustrating how overlapping double and triple intersections are compensated."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 3.1: Constrained Stars and Bars Weak Compositions",
                "statement": r"""Find the number of integer solutions to the equation:
$$x_1 + x_2 + x_3 + x_4 = 25$$
subject to the following individual constraints:
$$x_1 \ge 2, \quad x_2 \ge 0, \quad x_3 \ge 5, \quad 0 \le x_4 \le 6$$""",
                "hints": [
                    "Perform a change of variables to absorb the lower bounds $x_1 \ge 2$ and $x_3 \ge 5$.",
                    "Use the Complement Principle / Inclusion-Exclusion for the upper bound constraint on $x_4$."
                ],
                "solution": r"""### 1. Variable Transformation for Lower Bounds
Let:
- $y_1 = x_1 - 2 \ge 0 \implies x_1 = y_1 + 2$
- $y_2 = x_2 \ge 0$
- $y_3 = x_3 - 5 \ge 0 \implies x_3 = y_3 + 5$
- $y_4 = x_4 \ge 0$

Substitute into the original equation:
$$(y_1 + 2) + y_2 + (y_3 + 5) + y_4 = 25 \implies y_1 + y_2 + y_3 + y_4 = 25 - 7 = 18$$
with the upper bound condition $y_4 \le 6$ (since $y_4 = x_4$).

---

### 2. Total Non-Negative Solutions without Upper Bound Constraint
The total number of non-negative integer solutions to $y_1 + y_2 + y_3 + y_4 = 18$ with $y_i \ge 0$ is:
$$N_{\text{total}} = \binom{n + k - 1}{k - 1} = \binom{18 + 4 - 1}{4 - 1} = \binom{21}{3}$$
Computing the binomial coefficient:
$$\binom{21}{3} = \frac{21 \times 20 \times 19}{3 \times 2 \times 1} = 7 \times 10 \times 19 = 1330$$

---

### 3. Complementary Solutions Violating the Upper Bound
A solution violates the condition if $y_4 \ge 7$.
Let $z_4 = y_4 - 7 \ge 0 \implies y_4 = z_4 + 7$.
Substitute into the equation:
$$y_1 + y_2 + y_3 + (z_4 + 7) = 18 \implies y_1 + y_2 + y_3 + z_4 = 11$$
The number of non-negative solutions with $y_4 \ge 7$ is:
$$N_{\text{violating}} = \binom{11 + 4 - 1}{4 - 1} = \binom{14}{3}$$
Computing the binomial coefficient:
$$\binom{14}{3} = \frac{14 \times 13 \times 12}{3 \times 2 \times 1} = 14 \times 13 \times 2 = 364$$

---

### 4. Final Solution via Subtraction
Applying the complement rule:
$$N = N_{\text{total}} - N_{\text{violating}} = 1330 - 364 = 966$$
There are exactly **966** valid integer solutions. $\blacksquare$"""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 3.2: Complete Derivation and Asymptotics of Derangements",
                "statement": r"""Let $S_n$ be the symmetric group of permutations of $n$ elements.
A permutation $\pi \in S_n$ is a derangement if $\pi(i) \ne i$ for all $i \in \{1, 2, \dots, n\}$.
1. Using the Principle of Inclusion-Exclusion, prove that the number of derangements $D_n$ satisfies:
$$D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!}$$
2. Prove the two-term linear recurrence relation:
$$D_n = (n - 1)(D_{n-1} + D_{n-2}) \quad \text{for } n \ge 3$$
3. Prove that for all $n \ge 1$, $D_n$ is the nearest integer to $\frac{n!}{e}$, i.e.:
$$D_n = \left\lfloor \frac{n!}{e} + \frac{1}{2} \right\rfloor$$""",
                "hints": [
                    "Define $A_i$ as the set of permutations fixing element $i$, so $|A_i| = (n-1)!$.",
                    "For the recurrence, consider where element 1 is mapped, and whether that element maps back to 1.",
                    "Use the alternating series remainder bound $\left| \sum_{k=n+1}^\infty \frac{(-1)^k}{k!} \right| < \frac{1}{(n+1)!}$."
                ],
                "solution": r"""### 1. Derivation via Inclusion-Exclusion
Let the universe $\mathcal{U}$ be all $n!$ permutations of $\{1, 2, \dots, n\}$.
For each $i \in \{1, 2, \dots, n\}$, define the set of permutations fixing $i$:
$$A_i = \{\pi \in S_n \mid \pi(i) = i\}$$
A derangement is a permutation that belongs to none of the sets $A_i$:
$$D_n = \left| \bigcap_{i=1}^n A_i^c \right| = |\mathcal{U}| - \left| \bigcup_{i=1}^n A_i \right|$$

For any selection of $k$ distinct indices $\{i_1, i_2, \dots, i_k\}$:
$$|A_{i_1} \cap A_{i_2} \cap \dots \cap A_{i_k}| = (n - k)!$$
because the $k$ chosen elements are fixed in place, while the remaining $n - k$ elements can be permuted arbitrarily.
There are $\binom{n}{k}$ such intersections. By the Principle of Inclusion-Exclusion:
$$\left| \bigcup_{i=1}^n A_i \right| = \sum_{k=1}^n (-1)^{k-1} \binom{n}{k} (n - k)!$$
Since $\binom{n}{k}(n - k)! = \frac{n!}{k!(n-k)!}(n-k)! = \frac{n!}{k!}$, we obtain:
$$\begin{aligned}
D_n &= n! - \sum_{k=1}^n (-1)^{k-1} \frac{n!}{k!} \\
&= n! + \sum_{k=1}^n (-1)^k \frac{n!}{k!} \\
&= n! \sum_{k=0}^n \frac{(-1)^k}{k!}
\end{aligned}$$

---

### 2. Proof of the Recurrence Relation $D_n = (n-1)(D_{n-1} + D_{n-2})$
Consider the element 1 in a derangement $\pi$.
Since $\pi(1) \ne 1$, $\pi(1)$ can be any of the remaining $n - 1$ elements. Suppose $\pi(1) = j$ where $j \in \{2, 3, \dots, n\}$. There are $n - 1$ choices for $j$.
We partition based on what $\pi(j)$ equals:
- **Case A: $\pi(j) = 1$.**
  Elements 1 and $j$ swap with each other. The remaining $n - 2$ elements must form a derangement among themselves. There are $D_{n-2}$ such permutations.
- **Case B: $\pi(j) \ne 1$.**
  Element $j$ is forbidden from mapping to 1. Think of renaming 1 as $j$'s forbidden target. Then the $n - 1$ elements $\{2, 3, \dots, n\}$ must be permuted such that no element maps to its forbidden target. This is isomorphic to a derangement of $n - 1$ elements, contributing $D_{n-1}$ ways.

Summing these disjoint cases and multiplying by the $n - 1$ choices for $j$:
$$D_n = (n - 1)(D_{n-1} + D_{n-2}) \blacksquare$$

---

### 3. Nearest Integer Proof: $D_n = \lfloor n!/e + 1/2 \rfloor$
Recall the Taylor series for $e^{-1}$:
$$e^{-1} = \sum_{k=0}^\infty \frac{(-1)^k}{k!} = \sum_{k=0}^n \frac{(-1)^k}{k!} + \sum_{k=n+1}^\infty \frac{(-1)^k}{k!}$$
Multiplying by $n!$:
$$\frac{n!}{e} = D_n + n! \sum_{k=n+1}^\infty \frac{(-1)^k}{k!} = D_n + R_n$$
where the remainder is:
$$R_n = \sum_{k=n+1}^\infty (-1)^k \frac{n!}{k!} = \frac{(-1)^{n+1}}{n+1} + \frac{(-1)^{n+2}}{(n+1)(n+2)} + \dots$$
Since this is an alternating series with strictly decreasing terms in magnitude for $n \ge 1$:
$$|R_n| \le \frac{1}{n + 1}$$
For any $n \ge 1$:
$$|R_n| \le \frac{1}{1 + 1} = \frac{1}{2}$$
In fact, for $n \ge 2$, $|R_n| \le \frac{1}{3} < \frac{1}{2}$.
Therefore, the real number $\frac{n!}{e}$ is within distance less than $\frac{1}{2}$ of the integer $D_n$.
Consequently, rounding $\frac{n!}{e}$ to the nearest integer yields precisely $D_n$:
$$D_n = \left\lfloor \frac{n!}{e} + \frac{1}{2} \right\rfloor \blacksquare$$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 3.3: Ramsey Number R(3, 3) and Schur's Theorem Bounds",
                "statement": r"""The Ramsey number $R(s, t)$ denotes the minimum number of vertices $N$ such that every 2-coloring (Red/Blue) of the edges of the complete graph $K_N$ contains either a monochromatic Red clique $K_s$ or a monochromatic Blue clique $K_t$.

1. Prove using the Generalized Pigeonhole Principle that $R(3, 3) \le 6$ (i.e., among any 6 people, there are either 3 mutual acquaintances or 3 mutual strangers).
2. Construct an explicit edge coloring of $K_5$ containing neither a Red $K_3$ nor a Blue $K_3$, proving $R(3, 3) > 5$ and hence $R(3, 3) = 6$.
3. Generalize the bound to prove that for all $s, t \ge 2$:
$$R(s, t) \le R(s - 1, t) + R(s, t - 1)$$""",
                "hints": [
                    "For $K_6$, fix vertex $v_1$. It is incident to 5 edges colored either Red or Blue.",
                    "Apply the Generalized Pigeonhole Principle: $\\lceil 5/2 \\rceil = 3$.",
                    "For $K_5$, color the outer cycle $C_5$ Red and the inner star pentagram Blue."
                ],
                "solution": r"""### 1. Proof that $R(3, 3) \le 6$
Consider a complete graph $K_6$ whose edges are colored with two colors: Red and Blue.
1. Select an arbitrary vertex $v \in V(K_6)$.
2. The vertex $v$ has $\deg(v) = 6 - 1 = 5$ incident edges connected to the other 5 vertices.
3. Each of these 5 edges is colored either Red or Blue (2 colors / pigeonholes).
4. By the Generalized Pigeonhole Principle, at least:
   $$\left\lceil \frac{5}{2} \right\rceil = 3 \text{ edges}$$
   must share the same color.
5. Without loss of generality, assume at least 3 incident edges from $v$ are colored **Red**.
   Let the three endpoints of these red edges be $u_1, u_2, u_3$.
6. Now consider the three edges connecting pairs of $\{u_1, u_2, u_3\}$:
   - **Case A:** If any edge $(u_i, u_j)$ is colored Red, then together with the red edges $(v, u_i)$ and $(v, u_j)$, the triangle $\{v, u_i, u_j\}$ forms a **monochromatic Red $K_3$**.
   - **Case B:** If none of the edges between $\{u_1, u_2, u_3\}$ are Red, then all three edges $(u_1, u_2), (u_2, u_3), (u_3, u_1)$ must be colored **Blue**. This forms a **monochromatic Blue $K_3$**.
7. In both cases, a monochromatic $K_3$ (either Red or Blue) is guaranteed to exist.
Therefore, $R(3, 3) \le 6$.

---

### 2. Proof that $R(3, 3) > 5$ (Counterexample on $K_5$)
Consider the complete graph $K_5$ with vertices labeled $\{0, 1, 2, 3, 4\}$.
Define the 2-coloring rule:
- Color an edge $(i, j)$ **Red** if $|i - j| \equiv 1 \pmod 5$ or $|i - j| \equiv 4 \pmod 5$ (the perimeter cycle $C_5$).
- Color an edge $(i, j)$ **Blue** if $|i - j| \equiv 2 \pmod 5$ or $|i - j| \equiv 3 \pmod 5$ (the interior star pentagram).

Analysis of cliques:
- The Red subgraph is a single 5-cycle $C_5 = (0-1-2-3-4-0)$. A 5-cycle contains no triangles ($K_3$). Thus, there is no Red $K_3$.
- The Blue subgraph is also an isomorphic 5-cycle $C_5 = (0-2-4-1-3-0)$. It likewise contains no triangles ($K_3$). Thus, there is no Blue $K_3$.

Since there exists a 2-coloring of $K_5$ with neither a Red $K_3$ nor a Blue $K_3$, we must have:
$$R(3, 3) > 5$$
Combining with $R(3, 3) \le 6$, we conclude rigorously:
$$R(3, 3) = 6 \blacksquare$$

---

### 3. General Recurrence: $R(s, t) \le R(s - 1, t) + R(s, t - 1)$
Let $N = R(s - 1, t) + R(s, t - 1)$. We prove that any 2-colored $K_N$ contains a Red $K_s$ or a Blue $K_t$.
1. Pick any vertex $v \in V(K_N)$.
2. The degree of $v$ is $N - 1 = R(s - 1, t) + R(s, t - 1) - 1$.
3. Let $N_R$ be the neighbors of $v$ via Red edges, and $N_B$ be the neighbors of $v$ via Blue edges:
   $$|N_R| + |N_B| = N - 1 = R(s - 1, t) + R(s, t - 1) - 1$$
4. We claim that either $|N_R| \ge R(s - 1, t)$ or $|N_B| \ge R(s, t - 1)$.
   If not, then $|N_R| \le R(s - 1, t) - 1$ and $|N_B| \le R(s, t - 1) - 1$, so:
   $$|N_R| + |N_B| \le R(s - 1, t) + R(s, t - 1) - 2$$
   which contradicts the sum being $N - 1$.
5. **Case 1: $|N_R| \ge R(s - 1, t)$.**
   By definition of the Ramsey number, the subgraph induced by $N_R$ contains either:
   - A Blue $K_t$ (in which case we are done), or
   - A Red $K_{s-1}$. Adding vertex $v$ (which is connected to all of $N_R$ by Red edges) forms a Red $K_s$!
6. **Case 2: $|N_B| \ge R(s, t - 1)$.**
   By symmetry, the subgraph induced by $N_B$ contains either:
   - A Red $K_s$ (done), or
   - A Blue $K_{t-1}$, which together with $v$ forms a Blue $K_t$.

In every scenario, we find a Red $K_s$ or Blue $K_t$.
Hence $R(s, t) \le R(s - 1, t) + R(s, t - 1)$. $\blacksquare$"""
            }
        ]
    }
    return u3

if __name__ == "__main__":
    u3 = get_unit3()
    print(f"Loaded Unit 3: {u3['title']} with {len(u3['sections'])} sections and {len(u3['problems'])} problems.")
