# -*- coding: utf-8 -*-
"""
build_fuzzy_unit7.py
Constructs Unit 7: Orderings, Morphisms & Fuzzy Relational Equations
Strictly ZERO course numbers.
"""

def get_unit7():
    u7 = {
        "number": 7,
        "title": "Orderings, Morphisms & Fuzzy Relational Equations",
        "leadSummary": "Advanced mathematical study of ordered fuzzy systems, relational mappings, and relational equations: fuzzy partial orderings, quasi-orderings, fuzzy dominance relations, relational morphisms (homomorphisms, strong homomorphisms, isomorphisms), fuzzy relational equations P ∘ R = Q on finite and infinite universes, the fundamental solvability criterion, Sanchez's Theorem for the greatest relational solution R̂ = P α Q via Gödel residuated implication, minimal solutions, and inverse diagnostic systems.",
        "simulations": ["sim_fuzzy_relational_equations"],
        "sections": [
            {
                "secNumber": "7.1",
                "title": "Fuzzy Partial Orderings, Quasi-Orderings & Dominance",
                "content": r"""### 1. Fuzzy Partial Orderings
In classical order theory, a partial ordering is a reflexive, antisymmetric, and transitive relation.
In fuzzy mathematics, this concept generalizes to model gradual precedence and preference:

> **Definition 7.1 (Fuzzy Partial Ordering):**
> A fuzzy relation $R$ on $X \times X$ is called a **fuzzy partial ordering** if it satisfies:
> 1. **Reflexivity:** $\mu_R(x, x) = 1$ for all $x \in X$.
> 2. **Antisymmetry:** For all $x \ne y \in X$:
>    $$\mu_R(x, y) > 0 \implies \mu_R(y, x) = 0$$
>    *(Strong antisymmetry: $\min(\mu_R(x, y), \mu_R(y, x)) = 0$ for $x \ne y$)*.
> 3. **Max-Min Transitivity:** $R \circ R \subseteq R$.

A set $X$ equipped with a fuzzy partial ordering is called a **fuzzy partially ordered set (fuzzy poset)**.

---

### 2. Fuzzy Pre-Orderings (Quasi-Orderings)
If the relation is reflexive and max-min transitive, but NOT antisymmetric, it is called a **fuzzy pre-ordering (quasi-ordering)**.
- Quasi-orderings are used extensively in social choice theory, consumer preference modeling, and multi-criteria decision ranking."""
            },
            {
                "secNumber": "7.2",
                "title": "Fuzzy Morphisms: Homomorphisms and Isomorphisms of Fuzzy Relational Systems",
                "content": r"""### 1. Relational Systems
Let $(X, R)$ and $(Y, S)$ be two fuzzy relational systems, where $R$ is a fuzzy relation on $X \times X$ and $S$ is a fuzzy relation on $Y \times Y$.
A crisp mapping $h: X \to Y$ is called a **homomorphism** if it preserves the relational structure:

> **Definition 7.2 (Fuzzy Homomorphism):**
> A mapping $h: X \to Y$ is a **homomorphism** from $(X, R)$ to $(Y, S)$ if for all $x_1, x_2 \in X$:
> $$\mu_R(x_1, x_2) \le \mu_S(h(x_1), h(x_2))$$
> That is, if two elements are related with strength $\alpha$ in $X$, their images under $h$ must be related with at least strength $\alpha$ in $Y$.

---

### 2. Strong Homomorphisms and Isomorphisms
1. **Strong Homomorphism:** $h$ is surjective and for all $y_1, y_2 \in Y$:
   $$\mu_S(y_1, y_2) = \sup_{x_1 \in h^{-1}(y_1), x_2 \in h^{-1}(y_2)} \mu_R(x_1, x_2)$$
2. **Fuzzy Isomorphism:** $h$ is a bijective mapping and for all $x_1, x_2 \in X$:
   $$\mu_S(h(x_1), h(x_2)) = \mu_R(x_1, x_2)$$
   An isomorphism means the systems $(X, R)$ and $(Y, S)$ have identical relational structures up to relabeling of elements."""
            },
            {
                "secNumber": "7.3",
                "title": "Fuzzy Relational Equations of the Form $P \\circ R = Q$",
                "content": r"""### 1. Formulation of the Problem
Let $X = \{x_1, \dots, x_m\}$, $Y = \{y_1, \dots, y_n\}$, and $Z = \{z_1, \dots, z_p\}$ be finite universes of discourse.
Consider the composition:
$$P \circ R = Q$$
where:
- $P = (p_1, \dots, p_m)$ is a known input fuzzy set (or relation on $U \times X$).
- $Q = (q_1, \dots, q_n)$ is a known observed output fuzzy set (or relation on $U \times Y$).
- $R \in [0, 1]^{m \times n}$ is an **unknown fuzzy relation** (representing the transfer matrix or system model).

Under Max-Min composition:
$$q_j = \max_{i=1}^m \min(p_i, r_{ij}) \quad (\forall j = 1, \dots, n)$$
Each column of $R$ can be solved independently:
$$\max_{i=1}^m \min(p_i, r_{ij}) = q_j$$

---

### 2. Solvability Dilemma
Unlike linear equations $A x = b$ in vector spaces, fuzzy relational equations do not form a field or ring.
Instead, they are governed by idempotent semi-ring lattice theory.
- There may be **no solution** at all.
- When solutions exist, the solution set $\mathcal{S}(P, Q) = \{R \mid P \circ R = Q\}$ is generally **not convex**.
- However, if solutions exist, there is always a **unique GREATEST solution** $\hat{R}$, and a finite set of **minimal solutions**!"""
            },
            {
                "secNumber": "7.4",
                "title": "Solvability Criteria, Greatest and Smallest Solutions via Sanchez's Theorem",
                "content": r"""### 1. The $\alpha$-Operator (Gödel Residuated Implication)
To solve $P \circ R = Q$, Elie Sanchez (1976) introduced the **$\alpha$-operator** (the residuum of the minimum t-norm):

> **Definition 7.3 (Sanchez $\alpha$-Operator):**
> For $a, b \in [0, 1]$:
> $$a \mathbin{\alpha} b \equiv \begin{cases} 1, & \text{if } a \le b \\ b, & \text{if } a > b \end{cases}$$
> Note: $a \mathbin{\alpha} b$ is the largest number $x \in [0, 1]$ satisfying $\min(a, x) \le b$.

---

### 2. Sanchez's Theorem

> **Theorem 7.1 (Sanchez's Theorem, 1976):**
> Let $P$ and $Q$ be fuzzy vectors. Define the candidate relation $\hat{R} = P \mathbin{\alpha} Q$ by:
> $$\hat{r}_{ij} = p_i \mathbin{\alpha} q_j = \begin{cases} 1, & p_i \le q_j \\ q_j, & p_i > q_j \end{cases}$$
> Then:
> 1. The equation $P \circ R = Q$ has a solution if and only if $\hat{R}$ is itself a solution:
>    $$\mathcal{S}(P, Q) \ne \emptyset \iff P \circ \hat{R} = Q$$
> 2. Whenever $\mathcal{S}(P, Q) \ne \emptyset$, $\hat{R}$ is the **unique greatest solution**:
>    $$\forall R \in \mathcal{S}(P, Q), \quad R \subseteq \hat{R}$$

#### Proof of Optimality:
For any $R \in \mathcal{S}(P, Q)$, we have $\min(p_i, r_{ij}) \le \max_k \min(p_k, r_{kj}) = q_j$ for every $i$.
By definition of the $\alpha$-operator, $r_{ij} \le p_i \mathbin{\alpha} q_j = \hat{r}_{ij}$.
Thus $R \subseteq \hat{R}$ for every valid solution! $\blacksquare$

---

### 3. Structure of the Solution Set
When solvable, the solution set forms a upper semi-lattice:
$$\mathcal{S}(P, Q) = \bigcup_{k=1}^s [ \check{R}_k, \; \hat{R} ]$$
where $\check{R}_1, \dots, \check{R}_s$ are the finitely many **minimal solutions**."""
            },
            {
                "secNumber": "7.5",
                "title": "Inverse Relational Problems and Diagnostic Modeling",
                "content": r"""### 1. Medical and Fault Diagnostic Systems
In fault diagnosis and medical expert systems:
- $P$: Fuzzy set of diseases / root causes.
- $R$: Known symptom-disease relationship matrix (knowledge base).
- $Q$: Observed fuzzy set of symptoms exhibited by a patient or machine.
The forward problem is $P \circ R = Q$.
The inverse diagnostic problem is: **Given symptoms $Q$ and relationship $R$, find the disease profile $P$**!

---

### 2. Solving for the Unknown Input ($X \circ R = Q$)
By transposition, $X \circ R = Q \iff R^T \circ X^T = Q^T$.
Applying Sanchez's Theorem to the dual formulation:
$$\hat{X} = (R \mathbin{\alpha} Q^T)^T \implies \hat{x}_i = \min_{j=1}^n (r_{ij} \mathbin{\alpha} q_j)$$
If $\hat{X} \circ R = Q$, then $\hat{X}$ is the largest possible cause profile that can account for symptoms $Q$ without exceeding them!"""
            }
        ],
        "problems": [
            {
                "tier": "Fundamentals",
                "title": "Problem 7.1: Application of the Gödel $\\alpha$-Operator",
                "statement": r"""The Gödel residuum operator is defined by $a \mathbin{\alpha} b = 1$ if $a \le b$, and $b$ if $a > b$.
1. Compute the following scalar values:
   - $0.3 \mathbin{\alpha} 0.7$
   - $0.8 \mathbin{\alpha} 0.5$
   - $0.6 \mathbin{\alpha} 0.6$
   - $0.9 \mathbin{\alpha} 0.0$
2. For $a = 0.8$ and $b = 0.5$, verify that $\min(a, a \mathbin{\alpha} b) = b$.
3. Prove that for any $a, b \in [0, 1]$, $\min(a, a \mathbin{\alpha} b) \le b$ holds unconditionally.""",
                "hints": [
                    "If $a \\le b$, result is 1.",
                    "If $a > b$, result is $b$.",
                    "Evaluate both cases for $\\min(a, a \\mathbin{\\alpha} b)$."
                ],
                "solution": r"""### 1. Scalar Evaluations
- $0.3 \mathbin{\alpha} 0.7$: Since $0.3 \le 0.7$, the value is **$1.0$**.
- $0.8 \mathbin{\alpha} 0.5$: Since $0.8 > 0.5$, the value is **$0.5$**.
- $0.6 \mathbin{\alpha} 0.6$: Since $0.6 \le 0.6$, the value is **$1.0$**.
- $0.9 \mathbin{\alpha} 0.0$: Since $0.9 > 0.0$, the value is **$0.0$**. $\blacksquare$

---

### 2. Verification for $a = 0.8, b = 0.5$
Since $a > b$, $a \mathbin{\alpha} b = 0.5$.
Then:
$$\min(a, a \mathbin{\alpha} b) = \min(0.8, 0.5) = 0.5 = b \qquad \blacksquare$$

---

### 3. General Proof that $\min(a, a \mathbin{\alpha} b) \le b$
Let $a, b \in [0, 1]$.
- **Case 1 ($a \le b$):**
  By definition, $a \mathbin{\alpha} b = 1$.
  Then:
  $$\min(a, a \mathbin{\alpha} b) = \min(a, 1) = a$$
  Since $a \le b$, we have $\min(a, a \mathbin{\alpha} b) = a \le b$.
- **Case 2 ($a > b$):**
  By definition, $a \mathbin{\alpha} b = b$.
  Then:
  $$\min(a, a \mathbin{\alpha} b) = \min(a, b) = b \le b$$
In both exhaustive cases, $\min(a, a \mathbin{\alpha} b) \le b$ holds identically. $\blacksquare$"""
            },
            {
                "tier": "Computational Triad",
                "title": "Problem 7.2: Complete Solution of a Fuzzy Relational Equation $P \\circ R = Q$",
                "statement": r"""Consider the fuzzy relational equation $P \circ R = Q$, where:
$$P = \begin{pmatrix} 0.5 & 0.7 & 0.3 \end{pmatrix}$$
and the observed output is:
$$Q = \begin{pmatrix} 0.6 & 0.4 \end{pmatrix}$$
The unknown relation is a $3 \times 2$ matrix $R = (r_{ij}) \in [0, 1]^{3 \times 2}$.

1. Use Sanchez's Theorem to construct the candidate greatest relation $\hat{R} = P \mathbin{\alpha} Q$.
2. Compute the composition $P \circ \hat{R}$ and verify whether $\hat{R}$ solves the equation.
3. Determine all minimal solutions $\check{R}$ for this system.
4. Give a non-trivial solution matrix $R \in \mathcal{S}(P, Q)$ strictly between a minimal solution and $\hat{R}$.""",
                "hints": [
                    "Compute each entry $\\hat{r}_{ij} = p_i \\mathbin{\\alpha} q_j$.",
                    "Verify $\\max_i \\min(p_i, \\hat{r}_{ij}) = q_j$ for each column $j$.",
                    "For column 1 ($q_1 = 0.6$): since $p_2 = 0.7 > 0.6$, $r_{21} = 0.6$ is required."
                ],
                "solution": r"""### 1. Construction of $\hat{R} = P \mathbin{\alpha} Q$
Input: $P = (0.5, 0.7, 0.3)$.
Output: $Q = (0.6, 0.4)$.
Formula: $\hat{r}_{ij} = p_i \mathbin{\alpha} q_j$.

#### Column 1 ($q_1 = 0.6$):
- $\hat{r}_{11} = p_1 \mathbin{\alpha} q_1 = 0.5 \mathbin{\alpha} 0.6 = 1.0$ (since $0.5 \le 0.6$)
- $\hat{r}_{21} = p_2 \mathbin{\alpha} q_1 = 0.7 \mathbin{\alpha} 0.6 = 0.6$ (since $0.7 > 0.6$)
- $\hat{r}_{31} = p_3 \mathbin{\alpha} q_1 = 0.3 \mathbin{\alpha} 0.6 = 1.0$ (since $0.3 \le 0.6$)

#### Column 2 ($q_2 = 0.4$):
- $\hat{r}_{12} = p_1 \mathbin{\alpha} q_2 = 0.5 \mathbin{\alpha} 0.4 = 0.4$ (since $0.5 > 0.4$)
- $\hat{r}_{22} = p_2 \mathbin{\alpha} q_2 = 0.7 \mathbin{\alpha} 0.4 = 0.4$ (since $0.7 > 0.4$)
- $\hat{r}_{32} = p_3 \mathbin{\alpha} q_2 = 0.3 \mathbin{\alpha} 0.4 = 1.0$ (since $0.3 \le 0.4$)

Therefore, the greatest solution matrix is:
$$\hat{R} = \begin{pmatrix} 1.0 & 0.4 \\ 0.6 & 0.4 \\ 1.0 & 1.0 \end{pmatrix} \qquad \blacksquare$$

---

### 2. Verification of Solvability ($P \circ \hat{R}$)
- **Column 1:**
  $$q_1' = \max(\min(0.5, 1.0), \min(0.7, 0.6), \min(0.3, 1.0)) = \max(0.5, 0.6, 0.3) = 0.6 = q_1$$
- **Column 2:**
  $$q_2' = \max(\min(0.5, 0.4), \min(0.7, 0.4), \min(0.3, 1.0)) = \max(0.4, 0.4, 0.3) = 0.4 = q_2$$

Since $P \circ \hat{R} = (0.6, 0.4) = Q$, **the equation is SOLVABLE**, and $\hat{R}$ is indeed the greatest solution! $\blacksquare$

---

### 3. Finding Minimal Solutions $\check{R}$
To achieve $q_1 = 0.6$:
Notice that $p_1 = 0.5 < 0.6$ and $p_3 = 0.3 < 0.6$. The term $\min(p_1, r_{11}) \le 0.5$ and $\min(p_3, r_{31}) \le 0.3$.
Thus, **only the second term $\min(p_2, r_{21}) = \min(0.7, r_{21})$ can reach $0.6$**!
We MUST have $r_{21} = 0.6$. The other entries in column 1 can be 0.
Minimal column 1: $(0, 0.6, 0)^T$.

To achieve $q_2 = 0.4$:
Notice that $p_3 = 0.3 < 0.4$, so $\min(p_3, r_{32}) \le 0.3$.
We can achieve $0.4$ through EITHER index 1 or index 2:
- Option A: $r_{12} = 0.4$ (since $\min(0.5, 0.4) = 0.4$).
- Option B: $r_{22} = 0.4$ (since $\min(0.7, 0.4) = 0.4$).

Thus, there are **two distinct minimal solutions**:
$$\check{R}_1 = \begin{pmatrix} 0.0 & 0.4 \\ 0.6 & 0.0 \\ 0.0 & 0.0 \end{pmatrix}, \qquad \check{R}_2 = \begin{pmatrix} 0.0 & 0.0 \\ 0.6 & 0.4 \\ 0.0 & 0.0 \end{pmatrix} \qquad \blacksquare$$

---

### 4. Intermediate Solution
Any matrix $R$ satisfying $\check{R}_k \le R \le \hat{R}$ is an exact solution.
For instance:
$$R_{\text{mid}} = \begin{pmatrix} 0.5 & 0.4 \\ 0.6 & 0.2 \\ 0.0 & 0.5 \end{pmatrix}$$
Check:
- $q_1 = \max(\min(0.5, 0.5), \min(0.7, 0.6), \min(0.3, 0.0)) = \max(0.5, 0.6, 0.0) = 0.6$.
- $q_2 = \max(\min(0.5, 0.4), \min(0.7, 0.2), \min(0.3, 0.5)) = \max(0.4, 0.2, 0.3) = 0.4$.
$P \circ R_{\text{mid}} = (0.6, 0.4) = Q$. Verified! $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 7.3: Inconsistency and Solvability Bound for Fuzzy Relational Equations",
                "statement": r"""Consider the fuzzy relational equation $P \circ R = Q$ on finite sets where $P \in [0, 1]^m$ and $Q \in [0, 1]^n$.
1. Prove that if there exists some column index $j \in \{1, \dots, n\}$ such that:
   $$\max_{i=1}^m p_i < q_j$$
   then the equation $P \circ R = Q$ has **NO SOLUTION** ($\mathcal{S}(P, Q) = \emptyset$).
2. Prove that if $Q$ satisfies $\mathcal{S}(P, Q) \ne \emptyset$, then the greatest solution $\hat{R} = P \mathbin{\alpha} Q$ satisfies the equality:
   $$P \circ (P \mathbin{\alpha} Q) = Q$$
3. For an unsolvable equation, define the approximate Chebyshev distance error:
   $$E(R) = \| P \circ R - Q \|_\infty = \max_{j=1}^n | (P \circ R)_j - q_j |$$
   Show that the candidate $\hat{R} = P \mathbin{\alpha} Q$ always produces an underestimation $P \circ \hat{R} \le Q$, and evaluate the error when $P = (0.4, 0.5)$ and $Q = (0.8, 0.9)$.""",
                "hints": [
                    "For part 1, note that $\\min(p_i, r_{ij}) \\le p_i \\le \\max_k p_k$.",
                    "For part 2, use the fact that if a solution $R$ exists, $R \\le \\hat{R} \\implies Q = P \\circ R \\le P \\circ \\hat{R} \\le Q$.",
                    "For part 3, compute $P \\circ \\hat{R}$ and find $\\| P \\circ \\hat{R} - Q \\|_\\infty$."
                ],
                "solution": r"""### 1. Proof of the Necessary Solvability Bound
For any candidate matrix $R \in [0, 1]^{m \times n}$, the $j$-th component of the composed output is:
$$(P \circ R)_j = \max_{i=1}^m \min(p_i, r_{ij})$$
Since $\min(p_i, r_{ij}) \le p_i$ for all $i \in \{1, \dots, m\}$:
$$\max_{i=1}^m \min(p_i, r_{ij}) \le \max_{i=1}^m p_i$$
Therefore, for ANY relation $R$:
$$(P \circ R)_j \le \max_{i=1}^m p_i$$
Now suppose there exists some $j$ such that $\max_{i=1}^m p_i < q_j$.
Then:
$$(P \circ R)_j \le \max_{i=1}^m p_i < q_j \implies (P \circ R)_j \ne q_j$$
It is impossible for $(P \circ R)_j$ to reach $q_j$.
Hence no relation $R$ can satisfy the equation, proving that $\mathcal{S}(P, Q) = \emptyset$. $\blacksquare$

---

### 2. Proof of Equality for Greatest Solution
Assume $\mathcal{S}(P, Q) \ne \emptyset$.
Let $R^*$ be any solution in $\mathcal{S}(P, Q)$, so $P \circ R^* = Q$.
By the definition of the $\alpha$-operator:
For all $i, j$: $\min(p_i, r^*_{ij}) \le (P \circ R^*)_j = q_j$.
Since $p_i \mathbin{\alpha} q_j$ is the largest value $x$ such that $\min(p_i, x) \le q_j$, we have:
$$r^*_{ij} \le p_i \mathbin{\alpha} q_j = \hat{r}_{ij} \implies R^* \subseteq \hat{R}$$
By monotonicity of the max-min composition:
$$Q = P \circ R^* \subseteq P \circ \hat{R}$$
On the other hand, by definition of $\hat{R}$:
$$\min(p_i, \hat{r}_{ij}) = \min(p_i, p_i \mathbin{\alpha} q_j) \le q_j \quad (\forall i)$$
Taking the maximum over $i$:
$$(P \circ \hat{R})_j = \max_{i=1}^m \min(p_i, \hat{r}_{ij}) \le q_j \implies P \circ \hat{R} \subseteq Q$$
Combining both inclusions:
$$Q \subseteq P \circ \hat{R} \subseteq Q \implies P \circ \hat{R} = Q \qquad \blacksquare$$

---

### 3. Approximation Analysis for Inconsistent Systems
Given $P = (0.4, 0.5)$ and $Q = (0.8, 0.9)$.
Here $\max_i p_i = 0.5$.
Since $q_1 = 0.8 > 0.5$ and $q_2 = 0.9 > 0.5$, the system is strictly unsolvable by Part 1!

Compute $\hat{R} = P \mathbin{\alpha} Q$:
- For Column 1 ($q_1 = 0.8$): $p_1 = 0.4 \le 0.8 \implies 1.0$; $p_2 = 0.5 \le 0.8 \implies 1.0$.
- For Column 2 ($q_2 = 0.9$): $p_1 = 0.4 \le 0.9 \implies 1.0$; $p_2 = 0.5 \le 0.9 \implies 1.0$.
$$\hat{R} = \begin{pmatrix} 1.0 & 1.0 \\ 1.0 & 1.0 \end{pmatrix}$$

Now compute $P \circ \hat{R}$:
- $(P \circ \hat{R})_1 = \max(\min(0.4, 1), \min(0.5, 1)) = \max(0.4, 0.5) = 0.5 \le 0.8$.
- $(P \circ \hat{R})_2 = \max(\min(0.4, 1), \min(0.5, 1)) = \max(0.4, 0.5) = 0.5 \le 0.9$.
$$P \circ \hat{R} = (0.5, 0.5)$$

Notice that $P \circ \hat{R} \le Q$ strictly.
The Chebyshev approximation error is:
$$\| P \circ \hat{R} - Q \|_\infty = \max(|0.5 - 0.8|, |0.5 - 0.9|) = \max(0.3, 0.4) = 0.40 \qquad \blacksquare$$"""
            }
        ]
    }
    return u7

if __name__ == "__main__":
    u7 = get_unit7()
    print(f"Loaded Unit 7: {u7['title']} with {len(u7['sections'])} sections and {len(u7['problems'])} problems.")
