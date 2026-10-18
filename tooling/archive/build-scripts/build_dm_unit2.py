# -*- coding: utf-8 -*-
"""
build_dm_unit2.py
Constructs Unit 2: Mathematical Induction, Well-Ordering & Program Verification
Strictly ZERO course numbers.
"""

def get_unit2():
    u2 = {
        "number": 2,
        "title": "Mathematical Induction, Well-Ordering & Program Verification",
        "leadSummary": "Foundations of inductive reasoning and program semantics: the Principle of Mathematical Induction (weak induction), strong/complete induction, the Well-Ordering Principle of the natural numbers and proof of their mutual equivalence, structural induction over inductively defined trees and strings, formal program correctness with Hoare triples $\{P\} C \{Q\}$, loop invariants, and termination proofs via well-founded measure functions.",
        "simulations": ["sim_dm_induction_towers"],
        "sections": [
            {
                "secNumber": "2.1",
                "title": "Principle of Mathematical Induction (Weak Induction) & Inductive Step Rigor",
                "content": r"""### 1. The Axiomatic Basis of Induction

The **Principle of Mathematical Induction (PMI)** is one of the foundational Peano axioms governing the structure of the natural numbers $\mathbb{N} = \{0, 1, 2, 3, \dots\}$ (or positive integers $\mathbb{Z}^+$). It provides a mechanism for establishing that a predicate $P(n)$ is true for all integers $n \ge n_0$.

> **Axiom 2.1 (Weak Mathematical Induction):**
> Let $P(n)$ be a predicate defined for all integers $n \ge n_0$. If:
> 1. **Base Case:** $P(n_0)$ is true.
> 2. **Inductive Step:** For every integer $k \ge n_0$, the implication $P(k) \implies P(k+1)$ is true.
>
> Then $P(n)$ is true for all integers $n \ge n_0$:
> $$\Big( P(n_0) \land \forall k \ge n_0 \, [P(k) \implies P(k+1)] \Big) \implies \forall n \ge n_0 \, P(n)$$

---

### 2. Anatomy of the Inductive Step

The most critical part of an induction proof is the **inductive step**. Beginners often commit logical fallacies by assuming what they are trying to prove for $n=k+1$, or by working backwards without establishing bidirectional equivalences.

The correct, rigorous procedure for the inductive step is:
1. **State the Inductive Hypothesis (IH):** Explicitly assume that $P(k)$ holds for an arbitrary fixed integer $k \ge n_0$.
2. **Target Goal:** Clearly identify the target statement $P(k+1)$ to be proven.
3. **Algebraic / Logical Bridge:** Express the structure of $P(k+1)$ in terms of $P(k)$ plus the $(k+1)$-th incremental contribution.
4. **Invoke IH:** Substitute the assumption guaranteed by $P(k)$.
5. **Deduce Target:** Complete the derivation to show $P(k+1)$ follows necessarily.

> **Example 2.1 (Sum of Consecutive Integers):**
> Prove that for all $n \ge 1$:
> $$\sum_{i=1}^n i = \frac{n(n+1)}{2}$$
> - **Base Case ($n=1$):** LHS $= \sum_{i=1}^1 i = 1$. RHS $= \frac{1(2)}{2} = 1$. LHS $=$ RHS. True.
> - **Inductive Step:** Assume $P(k)$ holds for $k \ge 1$: $\sum_{i=1}^k i = \frac{k(k+1)}{2}$ (Inductive Hypothesis).
> - We examine the LHS for $n = k+1$:
>   $$\sum_{i=1}^{k+1} i = \left(\sum_{i=1}^k i\right) + (k+1)$$
> - By the Inductive Hypothesis:
>   $$\sum_{i=1}^{k+1} i = \frac{k(k+1)}{2} + (k+1) = (k+1)\left( \frac{k}{2} + 1 \right) = (k+1)\left(\frac{k+2}{2}\right) = \frac{(k+1)((k+1)+1)}{2}$$
> - This is precisely $P(k+1)$. By the Principle of Mathematical Induction, the formula holds for all $n \ge 1$. $\blacksquare$"""
            },
            {
                "secNumber": "2.2",
                "title": "Strong Induction & The Well-Ordering Principle Equivalence",
                "content": r"""### 1. Strong (Complete) Induction

In many mathematical and algorithmic contexts, the hypothesis $P(k)$ alone is insufficient to deduce $P(k+1)$; instead, one needs the cumulative truth of **all** preceding cases $P(n_0), P(n_0+1), \dots, P(k)$.

> **Principle of Strong Induction:**
> Let $P(n)$ be a predicate on integers $n \ge n_0$. If:
> 1. **Base Case:** $P(n_0)$ is true.
> 2. **Inductive Step:** For every $k \ge n_0$, if $P(j)$ is true for all $n_0 \le j \le k$, then $P(k+1)$ is true.
>
> Then $P(n)$ is true for all $n \ge n_0$:
> $$\Big( P(n_0) \land \forall k \ge n_0 \, [(\forall j \, (n_0 \le j \le k \implies P(j))) \implies P(k+1)] \Big) \implies \forall n \ge n_0 \, P(n)$$

---

### 2. The Well-Ordering Principle (WOP)

> **Axiom 2.2 (The Well-Ordering Principle of $\mathbb{N}$):**
> Every non-empty subset $S \subseteq \mathbb{N}$ has a **least element** (minimum):
> $$\forall S \subseteq \mathbb{N} \; (S \ne \emptyset \implies \exists m \in S \; \forall x \in S \; [m \le x])$$

The Well-Ordering Principle distinguishes the discrete integers from the dense real numbers $\mathbb{R}$ or rational numbers $\mathbb{Q}$ (for instance, the open interval $(0, 1) \subset \mathbb{R}$ has an infimum 0, but no least element in the set).

---

### 3. Equivalence of Weak Induction, Strong Induction, and WOP

Remarkably, Weak Induction, Strong Induction, and the Well-Ordering Principle are mathematically **equivalent** in second-order arithmetic:

$$\text{Weak Induction} \iff \text{Strong Induction} \iff \text{Well-Ordering Principle}$$

```
                ┌───────────────────────────────────┐
                │      Weak Induction (PMI)         │
                └───────────────┬───────────────────┘
                                ▲   ▲
                       (Trivial)│   │(WOP ⟹ PMI)
                                │   │
                                ▼   │
                ┌───────────────────┴───────────────┐
                │      Strong Induction             │
                └───────────────┬───────────────────┘
                                ▲
                       (WOP ⟹) │ (Strong ⟹ WOP)
                                ▼
                ┌───────────────────────────────────┐
                │    Well-Ordering Principle (WOP)  │
                └───────────────────────────────────┘
```

> **Theorem 2.1 (WOP Implies Strong Induction):**
> Assume the Well-Ordering Principle holds. Then Strong Induction is valid.
>
> *Proof:*
> 1. Let $P(n)$ satisfy the hypotheses of Strong Induction for $n \ge n_0$.
> 2. Assume for contradiction that $P(n)$ is false for some $n \ge n_0$.
> 3. Define the set of counterexamples:
>    $$S = \{n \in \mathbb{N} \mid n \ge n_0 \land \neg P(n)\}$$
> 4. By our contradiction assumption, $S$ is non-empty ($S \ne \emptyset$).
> 5. By the Well-Ordering Principle, $S$ has a least element $m = \min(S)$.
> 6. Since $P(n_0)$ is true by the base case, $m > n_0$.
> 7. Because $m$ is the **minimal** element of $S$, every integer $j$ strictly less than $m$ with $n_0 \le j < m$ does **not** belong to $S$.
> 8. Therefore, $P(j)$ is true for all $n_0 \le j \le m - 1$.
> 9. But by the Inductive Step of Strong Induction, if $P(j)$ holds for all $n_0 \le j \le m - 1$, then $P(m)$ must be true!
> 10. This implies $m \notin S$, directly contradicting $m \in S$.
> 11. Hence the counterexample set $S$ must be empty, proving $\forall n \ge n_0 P(n)$. $\blacksquare$"""
            },
            {
                "secNumber": "2.3",
                "title": "Structural Induction & Inductively Defined Data Types",
                "content": r"""### 1. Inductively Defined Sets and Data Types

An **inductive definition** of a set $S$ consists of:
1. **Basis Clause:** Specifies elementary seed elements initially in $S$.
2. **Inductive Clause:** Specifies constructor rules for generating new elements from existing elements of $S$.
3. **Extremal Clause:** States that no other elements belong to $S$ unless obtained by finitely many applications of clauses 1 and 2.

#### Example: Full Binary Trees
The set $\mathcal{T}$ of full binary trees is defined inductively:
- **Basis:** A single isolated vertex $r$ is a full binary tree ($\text{root}(r) \in \mathcal{T}$).
- **Inductive Step:** If $T_1, T_2 \in \mathcal{T}$ are full binary trees and $r$ is a new vertex, then the tree $T = r(T_1, T_2)$ formed by attaching $T_1$ as the left subtree and $T_2$ as the right subtree of $r$ is a full binary tree.

---

### 2. The Principle of Structural Induction

> **Principle of Structural Induction:**
> To prove that a property $P(t)$ holds for all elements $t$ of an inductively defined set $S$:
> 1. **Basis Step:** Show $P(b)$ is true for all basis elements $b \in S$.
> 2. **Inductive Step:** For every constructor rule, show that if $P(s)$ is true for all existing sub-elements $s \in S$, then $P$ also holds for the newly constructed element.

> **Theorem 2.2 (Leaves vs Internal Vertices in Full Binary Trees):**
> Let $T \in \mathcal{T}$ be a full binary tree. Let $L(T)$ denote the number of leaves and $I(T)$ denote the number of internal (non-leaf) vertices. Then:
> $$L(T) = I(T) + 1$$
>
> *Proof by Structural Induction:*
> - **Basis Step:** Let $T$ be the single vertex tree. Then $L(T) = 1$ and $I(T) = 0$.
>   $$L(T) = 1 = 0 + 1 = I(T) + 1$$
>   The base case holds.
> - **Inductive Step:** Let $T = r(T_1, T_2)$ where $T_1, T_2 \in \mathcal{T}$ satisfy the inductive hypothesis:
>   $$L(T_1) = I(T_1) + 1, \qquad L(T_2) = I(T_2) + 1$$
>   The leaves of $T$ are the union of the leaves of $T_1$ and $T_2$:
>   $$L(T) = L(T_1) + L(T_2)$$
>   The internal vertices of $T$ are the root $r$ plus the internal vertices of $T_1$ and $T_2$:
>   $$I(T) = I(T_1) + I(T_2) + 1$$
>   Substituting the inductive hypothesis into the leaf count:
>   $$L(T) = (I(T_1) + 1) + (I(T_2) + 1) = [I(T_1) + I(T_2) + 1] + 1 = I(T) + 1$$
>   The property holds for $T$. By structural induction, $L(T) = I(T) + 1$ for all full binary trees. $\blacksquare$"""
            },
            {
                "secNumber": "2.4",
                "title": "Program Correctness, Hoare Triples & Partial vs Total Correctness",
                "content": r"""### 1. Formal Program Semantics and Hoare Logic

Formal program verification replaces empirical testing with rigorous mathematical proof that a computer program satisfies its formal functional specification. Founded by C. A. R. Hoare in 1969, **Hoare Logic** uses assertions on the program state.

> **Definition 2.1 (Hoare Triple):**
> A **Hoare Triple** is an expression of the form:
> $$\{P\} \; C \; \{Q\}$$
> where:
> - $P$ is the **precondition**: an assertion on program state before execution.
> - $C$ is the **command** (code block or algorithm).
> - $Q$ is the **postcondition**: an assertion on program state after execution.

---

### 2. Partial Correctness vs Total Correctness

1. **Partial Correctness ($\models_{\text{partial}} \{P\} C \{Q\}$):**
   If the precondition $P$ holds before the execution of $C$, **and if** $C$ halts (terminates), then the postcondition $Q$ will hold in the terminal state. Partial correctness does *not* guarantee termination (an infinite loop trivially satisfies partial correctness!).

2. **Total Correctness ($\models_{\text{total}} [P] C [Q]$):**
   If the precondition $P$ holds before execution, then $C$ is **guaranteed to terminate**, and upon termination, $Q$ holds:
   $$\text{Total Correctness} = \text{Partial Correctness} + \text{Termination Proof}$$

---

### 3. Core Deduction Rules of Hoare Logic

- **Axiom of Assignment:**
  $$\{P[e / x]\} \; x := e \; \{P\}$$
  where $P[e / x]$ denotes the assertion $P$ with all free occurrences of variable $x$ replaced by expression $e$.

- **Rule of Composition (Sequence):**
  $$\frac{\{P\} C_1 \{R\} \quad \{R\} C_2 \{Q\}}{\{P\} C_1; C_2 \{Q\}}$$

- **Rule of Conditional (If-Else):**
  $$\frac{\{P \land B\} C_1 \{Q\} \quad \{P \land \neg B\} C_2 \{Q\}}{\{P\} \text{ if } B \text{ then } C_1 \text{ else } C_2 \{Q\}}$$

- **Rule of Consequence (Strengthening Precondition / Weakening Postcondition):**
  $$\frac{P \implies P' \quad \{P'\} C \{Q'\} \quad Q' \implies Q}{\{P\} C \{Q\}}$$"""
            },
            {
                "secNumber": "2.5",
                "title": "Loop Invariants, Termination Proofs & Interactive Towers of Hanoi",
                "content": r"""### 1. The While-Loop Invariant Rule

The central challenge in verifying iterative algorithms is proving correctness for unbounded loops $\text{while } B \text{ do } C$.

> **Rule of the While Loop (Hoare):**
> $$\frac{\{I \land B\} \; C \; \{I\}}{\{I\} \; \text{while } B \text{ do } C \; \{I \land \neg B\}}$$
> where $I$ is the **Loop Invariant**.

A predicate $I$ is a valid **Loop Invariant** if it satisfies three essential conditions:
1. **Initialization:** $I$ is true immediately prior to the first iteration of the loop (established by the loop's preamble code).
2. **Maintenance:** If $I$ and loop condition $B$ are true before an iteration, then $I$ remains true after executing the loop body $C$: $\{I \land B\} C \{I\}$.
3. **Termination Utility:** When the loop terminates ($\neg B$ holds), the conjunction $I \land \neg B$ logically implies the desired postcondition $Q$: $(I \land \neg B) \implies Q$.

---

### 2. Termination Proofs via Well-Founded Measure Functions

To upgrade partial correctness to total correctness, one must prove the loop cannot iterate infinitely.

> **Method of Variant Functions (Ranking Functions):**
> Let $V: \text{State} \to \mathbb{Z}$ be an integer-valued function of program variables such that:
> 1. While the loop continues ($B$ is true), $V(\text{state}) \ge 0$.
> 2. Each execution of the loop body $C$ strictly decreases the variant:
>    $$V(\text{state}_{\text{after}}) \le V(\text{state}_{\text{before}}) - 1$$
>
> By the Well-Ordering Principle of $\mathbb{N}$, a sequence of non-negative integers cannot decrease indefinitely. Therefore, the loop must terminate in at most $V(\text{initial state})$ steps.

---

### 3. The Tower of Hanoi & Recursive Verification

The classic Tower of Hanoi with $n$ disks on 3 pegs ($A, B, C$) requires moving all disks from peg $A$ to peg $C$ without ever placing a larger disk atop a smaller disk.
- **Recurrence:** $T(n) = 2 T(n-1) + 1$, with $T(1) = 1$.
- **Closed Form:** $T(n) = 2^n - 1$ moves.
- **Inductive Invariant:** The recursive decomposition guarantees that after $2^{n-1} - 1$ steps, disk $n$ is clear to move to $C$, and the remaining steps successfully reposition all $n-1$ disks atop $C$."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 2.1: Sum of Squares and Bernoulli's Generalized Inequality",
                "statement": r"""1. Prove by mathematical induction that for every positive integer $n \ge 1$:
$$\sum_{i=1}^n i^2 = 1^2 + 2^2 + \dots + n^2 = \frac{n(n + 1)(2n + 1)}{6}$$
2. Prove by induction that for any real number $x > -1$ with $x \ne 0$ and any integer $n \ge 2$:
$$(1 + x)^n > 1 + n x \quad \text{(Strict Bernoulli's Inequality)}$$""",
                "hints": [
                    "For part 1, in the inductive step add $(k+1)^2$ to the RHS and factor out $(k+1)$.",
                    "For part 2, note that since $x > -1$, the factor $(1 + x) > 0$, preserving the direction of the inequality when multiplying."
                ],
                "solution": r"""### 1. Proof of Sum of Squares Formula
Let $P(n)$ be the proposition $\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$.

- **Base Case ($n=1$):**
  $$\text{LHS} = 1^2 = 1$$
  $$\text{RHS} = \frac{1(1+1)(2(1)+1)}{6} = \frac{1 \cdot 2 \cdot 3}{6} = 1$$
  Since $\text{LHS} = \text{RHS}$, $P(1)$ is true.

- **Inductive Step:**
  Assume $P(k)$ holds for an arbitrary integer $k \ge 1$:
  $$\sum_{i=1}^k i^2 = \frac{k(k+1)(2k+1)}{6} \quad \text{(Inductive Hypothesis)}$$
  We evaluate the sum for $n = k + 1$:
  $$\sum_{i=1}^{k+1} i^2 = \left( \sum_{i=1}^k i^2 \right) + (k+1)^2$$
  Substitute the Inductive Hypothesis:
  $$\sum_{i=1}^{k+1} i^2 = \frac{k(k+1)(2k+1)}{6} + (k+1)^2$$
  Factor out common term $(k+1)$:
  $$\begin{aligned}
  \sum_{i=1}^{k+1} i^2 &= (k+1) \left[ \frac{k(2k+1)}{6} + (k+1) \right] \\
  &= (k+1) \left[ \frac{2k^2 + k + 6k + 6}{6} \right] \\
  &= (k+1) \left[ \frac{2k^2 + 7k + 6}{6} \right]
  \end{aligned}$$
  Factoring the quadratic numerator $2k^2 + 7k + 6 = (k+2)(2k+3)$:
  $$\sum_{i=1}^{k+1} i^2 = \frac{(k+1)(k+2)(2k+3)}{6} = \frac{(k+1)((k+1)+1)(2(k+1)+1)}{6}$$
  This is precisely the formula for $P(k+1)$. By the Principle of Mathematical Induction, $P(n)$ is true for all $n \ge 1$.

---

### 2. Proof of Strict Bernoulli's Inequality
Let $Q(n)$ be $(1+x)^n > 1 + nx$ for $x > -1, x \ne 0$, and integer $n \ge 2$.

- **Base Case ($n=2$):**
  $$\text{LHS} = (1+x)^2 = 1 + 2x + x^2$$
  $$\text{RHS} = 1 + 2x$$
  Since $x \ne 0$, $x^2 > 0$. Therefore:
  $$(1+x)^2 = 1 + 2x + x^2 > 1 + 2x$$
  Hence $Q(2)$ is true.

- **Inductive Step:**
  Assume $Q(k)$ holds for $k \ge 2$:
  $$(1+x)^k > 1 + kx$$
  Since $x > -1$, we have $1 + x > 0$. Multiplying an inequality by a strictly positive number preserves the strict inequality:
  $$(1+x)^{k+1} = (1+x)^k (1+x) > (1 + kx)(1 + x)$$
  Expanding the right-hand product:
  $$(1 + kx)(1 + x) = 1 + x + kx + kx^2 = 1 + (k+1)x + kx^2$$
  Since $k \ge 2 > 0$ and $x \ne 0$, we have $kx^2 > 0$. Therefore:
  $$1 + (k+1)x + kx^2 > 1 + (k+1)x$$
  Combining the strict inequalities via transitivity:
  $$(1+x)^{k+1} > 1 + (k+1)x$$
  This completes the inductive step $Q(k+1)$.
  By mathematical induction, Bernoulli's inequality holds for all integers $n \ge 2$. $\blacksquare$"""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 2.2: Strong Induction and the Fundamental Theorem of Arithmetic",
                "statement": r"""1. Use Strong (Complete) Induction to prove the Existence Part of the Fundamental Theorem of Arithmetic:
Every integer $n \ge 2$ can be factored into a product of one or more prime numbers.
2. Provide an alternate proof of the same theorem using the Well-Ordering Principle (WOP) of the natural numbers.
3. Explain why Weak Induction is unnatural and awkward for this proof compared to Strong Induction.""",
                "hints": [
                    "A prime number is already a product of one prime (itself).",
                    "A composite number $n$ factors into $a \cdot b$ where $2 \le a, b < n$.",
                    "For WOP, define the set of integers $n \ge 2$ that cannot be written as a product of primes, and show its minimum leads to a contradiction."
                ],
                "solution": r"""### 1. Proof by Strong Mathematical Induction
Let $P(n)$ be the statement: "$n$ can be written as a product of prime numbers."

- **Base Case ($n=2$):**
  The integer 2 is prime, so it is trivially the product of a single prime number. Hence $P(2)$ is true.

- **Inductive Step:**
  Assume that $P(j)$ is true for all integers $j$ with $2 \le j \le k$, where $k \ge 2$ (Strong Inductive Hypothesis).
  We must prove that $P(k+1)$ is true.
  Consider the integer $k+1$:
  - **Case 1: $k+1$ is prime.**
    If $k+1$ is prime, it is trivially written as the product of one prime (itself), so $P(k+1)$ holds.
  - **Case 2: $k+1$ is composite.**
    By definition of composite numbers, there exist integers $a$ and $b$ such that:
    $$k+1 = a \cdot b, \qquad \text{where } 2 \le a \le k \text{ and } 2 \le b \le k$$
    Since $2 \le a \le k$ and $2 \le b \le k$, both $a$ and $b$ fall strictly within the range of our Strong Inductive Hypothesis!
    Therefore, both $a$ and $b$ can be factored into products of primes:
    $$a = p_1 p_2 \dots p_r, \qquad b = q_1 q_2 \dots q_s$$
    where each $p_i$ and $q_j$ is prime.
    Consequently:
    $$k+1 = a \cdot b = (p_1 p_2 \dots p_r)(q_1 q_2 \dots q_s)$$
    which is an explicit product of $(r + s)$ prime numbers!
    Thus $P(k+1)$ holds in both cases.

By the Principle of Strong Mathematical Induction, every integer $n \ge 2$ can be factored into a product of primes.

---

### 2. Alternate Proof using the Well-Ordering Principle (WOP)
1. Assume for contradiction that there exist integers $n \ge 2$ that cannot be written as a product of primes.
2. Define the set of non-factorable integers:
   $$\mathcal{C} = \{n \in \mathbb{Z} \mid n \ge 2 \text{ and } n \text{ cannot be written as a product of primes}\}$$
3. By our contradiction assumption, $\mathcal{C}$ is a non-empty subset of the natural numbers ($\mathcal{C} \ne \emptyset$).
4. By the Well-Ordering Principle, $\mathcal{C}$ contains a least element, say $m = \min(\mathcal{C})$.
5. The number $m$ cannot be prime (since every prime is a product of one prime, so $m \notin \mathcal{C}$).
6. Since $m \ge 2$ is not prime, $m$ must be composite. Thus there exist integers $a, b$ such that:
   $$m = a \cdot b, \qquad \text{with } 1 < a < m \text{ and } 1 < b < m$$
7. Because $m$ is the **minimal** element of $\mathcal{C}$ and $2 \le a < m$ and $2 \le b < m$, neither $a$ nor $b$ can belong to $\mathcal{C}$!
8. Therefore, both $a$ and $b$ must be factorable into products of primes:
   $$a = \prod_{i=1}^r p_i, \qquad b = \prod_{j=1}^s q_j$$
9. Then $m = a \cdot b = \left(\prod_{i=1}^r p_i\right) \left(\prod_{j=1}^s q_j\right)$, meaning $m$ IS a product of primes!
10. This implies $m \notin \mathcal{C}$, directly contradicting $m \in \mathcal{C}$.
11. Hence $\mathcal{C} = \emptyset$, and every integer $n \ge 2$ has a prime factorization.

---

### 3. Comparison with Weak Induction
Weak induction requires deriving $P(k+1)$ solely from knowledge of $P(k)$. When $k+1$ is composite, its factors $a$ and $b$ are typically **much smaller** than $k$ (for example, if $k+1 = 100$, its factors might be $10 \times 10$, nowhere near $k = 99$). Knowing that $99$ has a prime factorization provides zero direct algebraic insight into the factorization of $100$. Strong induction gives access to all prior integers, which is the natural mathematical structure required. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 2.3: Formal Hoare Logic Verification of Euclidean GCD Algorithm",
                "statement": r"""Consider the classic iterative Euclidean algorithm for computing the greatest common divisor $\gcd(A, B)$ of two positive integers $A, B \in \mathbb{Z}^+$:

```text
x := A;
y := B;
while y != 0 do
    r := x mod y;
    x := y;
    y := r;
end while;
```

1. Formulate the precise precondition $P$, postcondition $Q$, and candidate Loop Invariant $I(x, y)$.
2. Rigorously prove the **Partial Correctness** of the algorithm using the Hoare while-loop rule:
   - Prove **Initialization**: $P \implies I$.
   - Prove **Maintenance**: $\{I \land (y \ne 0)\} \; \text{body} \; \{I\}$.
   - Prove **Utility**: $(I \land (y = 0)) \implies Q$.
3. Prove **Total Correctness** by defining an explicit variant (ranking) function $V(x, y)$ and proving finite termination using the Well-Ordering Principle.""",
                "hints": [
                    "Recall the Euclidean division lemma: $\\gcd(x, y) = \\gcd(y, x \\bmod y)$.",
                    "For the loop invariant, state that $\\gcd(x, y) = \\gcd(A, B)$ and $x > 0, y \\ge 0$.",
                    "For termination, the value of $y$ strictly decreases at each iteration."
                ],
                "solution": r"""### 1. Specification and Loop Invariant Formulation
- **Precondition $P$:** $A > 0 \land B > 0 \land A, B \in \mathbb{Z}^+$.
- **Postcondition $Q$:** $x = \gcd(A, B)$.
- **Loop Invariant $I(x, y)$:**
  $$I(x, y) \equiv \Big( \gcd(x, y) = \gcd(A, B) \Big) \land (x > 0) \land (y \ge 0)$$

---

### 2. Proof of Partial Correctness

#### Phase A: Initialization
Before entering the while loop, the initialization code executes: $x := A; \; y := B$.
Under precondition $P$ ($A > 0, B > 0$):
$$\gcd(x, y) = \gcd(A, B), \qquad x = A > 0, \qquad y = B > 0 \ge 0$$
Thus $I(x, y)$ holds immediately prior to loop entry.

#### Phase B: Maintenance
Assume $I(x, y)$ and loop guard condition $B \equiv (y \ne 0)$ hold at the start of an iteration:
$$I \land (y \ne 0) \equiv (\gcd(x, y) = \gcd(A, B)) \land (x > 0) \land (y > 0)$$
The loop body executes:
```text
r := x mod y;
x := y;
y := r;
```
Let $(x', y')$ denote the values after the iteration:
$$x' = y, \qquad y' = r = x \bmod y$$
We verify all components of $I(x', y')$:
1. **GCD Invariance:**
   By the fundamental Euclidean Division Theorem, $x = q \cdot y + r$ with $0 \le r < y$.
   Any common divisor of $x$ and $y$ must divide $r = x - q y$.
   Conversely, any common divisor of $y$ and $r$ must divide $x = q y + r$.
   Therefore:
   $$\gcd(x', y') = \gcd(y, x \bmod y) = \gcd(x, y)$$
   By the inductive hypothesis $I$, $\gcd(x, y) = \gcd(A, B)$, hence:
   $$\gcd(x', y') = \gcd(A, B)$$
2. **Positivity of $x'$:**
   $x' = y$. Since the loop guard guaranteed $y > 0$, we have $x' > 0$.
3. **Non-negativity of $y'$:**
   $y' = x \bmod y$. By definition of integer modulus with divisor $y > 0$, $0 \le y' < y$.
   Thus $y' \ge 0$.

All conditions of $I(x', y')$ hold. Hence $\{I \land (y \ne 0)\} \text{ body } \{I\}$ is verified.

#### Phase C: Utility upon Termination
When the loop terminates, the guard condition is false, so $y = 0$, while the invariant $I(x, y)$ still holds:
$$I(x, 0) \implies \gcd(x, 0) = \gcd(A, B) \land x > 0$$
By the definition of the greatest common divisor:
$$\gcd(x, 0) = |x| = x \quad (\text{since } x > 0)$$
Therefore:
$$x = \gcd(A, B)$$
which is precisely the required postcondition $Q$.
This proves **Partial Correctness**.

---

### 3. Termination Proof (Total Correctness)
Define the integer ranking function:
$$V(x, y) = y$$
1. **Bounded Below:**
   While the loop continues ($y \ne 0$), by invariant condition $y \ge 0$, we have $y \in \mathbb{Z}^+$, so $V(x, y) \ge 1 > 0$.
2. **Strict Monotonic Decrease:**
   In each iteration, the new value $y'$ is $r = x \bmod y$.
   By the Euclidean division theorem with positive divisor $y > 0$:
   $$0 \le r < y \implies y' < y \implies V(x', y') \le V(x, y) - 1$$
   Thus, the ranking function strictly decreases by at least 1 in every iteration.
3. **Finite Termination:**
   Suppose for contradiction that the loop does not terminate. Then it generates an infinite sequence of non-negative integers $y_0 > y_1 > y_2 > \dots \ge 0$.
   The set of values $\{y_k \mid k \ge 0\}$ is a non-empty subset of $\mathbb{N}$.
   By the Well-Ordering Principle of $\mathbb{N}$, this set must have a least element $y_{min}$.
   However, if the loop does not terminate at $y_{min}$, the subsequent iteration produces $y_{next} < y_{min}$, contradicting the minimality of $y_{min}$.
   Therefore, the loop must terminate in at most $B$ iterations.

This completes the proof of **Total Correctness**. $\blacksquare$"""
            }
        ]
    }
    return u2

if __name__ == "__main__":
    u2 = get_unit2()
    print(f"Loaded Unit 2: {u2['title']} with {len(u2['sections'])} sections and {len(u2['problems'])} problems.")
