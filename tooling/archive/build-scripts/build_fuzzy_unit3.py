# -*- coding: utf-8 -*-
"""
build_fuzzy_unit3.py
Constructs Unit 3: α-Cuts, Decomposition Theorems & The Extension Principle
Strictly ZERO course numbers.
"""

def get_unit3():
    u3 = {
        "number": 3,
        "title": "α-Cuts, Decomposition Theorems & The Extension Principle",
        "leadSummary": "The fundamental bridge between crisp mathematics and fuzzy set theory: crisp α-cuts A_α and strong α-cuts A_{α^+}, cut monotonicity, preservation of set intersections and unions across cuts, the First Decomposition Theorem (representation via special fuzzy sets α · A_α), the Second Decomposition Theorem (continuous integral representation A = ∪_{α ∈ [0, 1]} α A_α), and Zadeh's Extension Principle for lifting crisp point mappings f: X → Y and multi-argument functions f: X_1 × ... × X_n → Y to fuzzy domains.",
        "simulations": ["sim_fuzzy_alpha_cuts_decomposition"],
        "sections": [
            {
                "secNumber": "3.1",
                "title": "Crisp $\\alpha$-Cuts and Strong $\\alpha$-Cuts ($A_\\alpha$ and $A_{\\alpha^+}$)",
                "content": r"""### 1. Connecting Fuzzy Sets to Classical Subsets
One of the most powerful and fruitful methodologies in fuzzy mathematics is the **$\alpha$-cut representation**.
Rather than treating a fuzzy set as an exotic non-classical entity, $\alpha$-cuts decompose any fuzzy set into an ordered family of standard, crisp subsets.

> **Definition 3.1 ($\alpha$-Cut and Strong $\alpha$-Cut):**
> Let $A$ be a fuzzy set on universe $X$ with membership function $\mu_A(x)$, and let $\alpha \in [0, 1]$.
> 1. The **$\alpha$-cut** (or weak $\alpha$-cut / $\alpha$-level set) of $A$, denoted $A_\alpha$ or $[A]_\alpha$, is the crisp set of all elements whose membership grade is at least $\alpha$:
>    $$A_\alpha = \{x \in X \mid \mu_A(x) \ge \alpha\}$$
> 2. The **strong $\alpha$-cut** of $A$, denoted $A_{\alpha^+}$ or $(A)_\alpha$, is the crisp set of all elements whose membership grade strictly exceeds $\alpha$:
>    $$A_{\alpha^+} = \{x \in X \mid \mu_A(x) > \alpha\}$$

#### Boundary Cases:
- For $\alpha = 0$: $A_0 = \{x \in X \mid \mu_A(x) \ge 0\} = X$ (the entire universe).
- The strong 0-cut is the **Support**: $A_{0^+} = \{x \in X \mid \mu_A(x) > 0\} = \text{Supp}(A)$.
- The 1-cut is the **Core**: $A_1 = \{x \in X \mid \mu_A(x) = 1\} = \text{Core}(A)$.
- The strong 1-cut is always empty: $A_{1^+} = \{x \in X \mid \mu_A(x) > 1\} = \emptyset$.

---

### 2. Level Set of a Fuzzy Set
The set of all distinct values assumed by the membership function $\mu_A(x)$ is called the **level set** (or spectrum) of $A$:
$$\Lambda(A) = \{\alpha \in [0, 1] \mid \exists x \in X, \; \mu_A(x) = \alpha\}$$
If $X$ is finite, $\Lambda(A) = \{\alpha_1, \alpha_2, \dots, \alpha_k\}$ is a finite ordered subset of $[0, 1]$."""
            },
            {
                "secNumber": "3.2",
                "title": "Algebraic Properties of $\\alpha$-Cuts: Monotonicity, Intersection & Union Preservation",
                "content": r"""### 1. The Monotonicity Property of Cuts

> **Theorem 3.1 (Cut Monotonicity):**
> For any fuzzy set $A$ and any $\alpha, \beta \in [0, 1]$:
> $$\alpha \le \beta \implies A_\beta \subseteq A_\alpha \quad \text{and} \quad A_{\beta^+} \subseteq A_{\alpha^+}$$
> Furthermore, for any $\alpha \in [0, 1)$:
> $$A_\alpha \supseteq A_{\alpha^+}$$

#### Proof:
Let $x \in A_\beta$. Then $\mu_A(x) \ge \beta$.
Since $\beta \ge \alpha$, transitivity yields $\mu_A(x) \ge \alpha$, which means $x \in A_\alpha$.
Hence $A_\beta \subseteq A_\alpha$.
Similarly, if $x \in A_{\alpha^+}$, then $\mu_A(x) > \alpha \ge \alpha$, so $x \in A_\alpha$. $\blacksquare$

---

### 2. Commutativity with Set Theoretic Operations

> **Theorem 3.2 (Preservation of Intersections and Unions):**
> For any fuzzy sets $A$ and $B$ under standard Zadeh operations, and for any $\alpha \in [0, 1]$:
> 1. $(A \cap B)_\alpha = A_\alpha \cap B_\alpha$
> 2. $(A \cup B)_\alpha = A_\alpha \cup B_\alpha$
> 3. $(A \cap B)_{\alpha^+} = A_{\alpha^+} \cap B_{\alpha^+}$
> 4. $(A \cup B)_{\alpha^+} = A_{\alpha^+} \cup B_{\alpha^+}$

#### Proof of (1):
$$\begin{aligned}
x \in (A \cap B)_\alpha &\iff \mu_{A \cap B}(x) \ge \alpha \\
&\iff \min(\mu_A(x), \mu_B(x)) \ge \alpha \\
&\iff \mu_A(x) \ge \alpha \text{ and } \mu_B(x) \ge \alpha \\
&\iff x \in A_\alpha \text{ and } x \in B_\alpha \\
&\iff x \in A_\alpha \cap B_\alpha \qquad \blacksquare
\end{aligned}$$

#### Non-Preservation of Complements:
Does $(A^c)_\alpha = (A_\alpha)^c$? **NO!**
In fact:
$$x \in (A^c)_\alpha \iff 1 - \mu_A(x) \ge \alpha \iff \mu_A(x) \le 1 - \alpha \iff x \notin A_{(1-\alpha)^+}$$
Therefore:
$$(A^c)_\alpha = (A_{(1-\alpha)^+})^c$$
Complementation inverts the cut level and swaps weak cuts with strong cuts!"""
            },
            {
                "secNumber": "3.3",
                "title": "First and Second Decomposition Theorems (Representation of Fuzzy Sets via Cuts)",
                "content": r"""### 1. Scaling a Crisp Set by a Scalar $\alpha$
To reconstruct a fuzzy set from its crisp cuts, we define the product of a scalar $\alpha \in [0, 1]$ and a crisp set $C \subseteq X$:

> **Definition 3.2 (Special Fuzzy Set $\alpha C$):**
> For $\alpha \in [0, 1]$ and $C \subseteq X$, the fuzzy set $\alpha C$ (or $\alpha \cdot C$) is defined by the membership function:
> $$\mu_{\alpha C}(x) = \alpha \cdot \chi_C(x) = \begin{cases} \alpha, & \text{if } x \in C \\ 0, & \text{if } x \notin C \end{cases}$$

---

### 2. The First Decomposition Theorem

> **Theorem 3.3 (First Decomposition Theorem):**
> For any fuzzy set $A$ on universe $X$:
> $$A = \bigcup_{\alpha \in [0, 1]} \alpha A_\alpha$$
> where $\bigcup$ denotes the standard fuzzy union ($\sup$ operator).
> That is, for all $x \in X$:
> $$\mu_A(x) = \sup_{\alpha \in [0, 1]} \mu_{\alpha A_\alpha}(x) = \sup_{\alpha \in [0, 1]} \left( \alpha \cdot \chi_{A_\alpha}(x) \right)$$

#### Proof:
For any chosen point $x \in X$, let $\mu_A(x) = a \in [0, 1]$.
Evaluate the right-hand supremum:
$$\sup_{\alpha \in [0, 1]} \left( \alpha \cdot \chi_{A_\alpha}(x) \right)$$
Recall that $x \in A_\alpha \iff \mu_A(x) \ge \alpha \iff a \ge \alpha$.
Therefore:
$$\chi_{A_\alpha}(x) = \begin{cases} 1, & \text{if } \alpha \le a \\ 0, & \text{if } \alpha > a \end{cases}$$
Substituting into the product:
$$\alpha \cdot \chi_{A_\alpha}(x) = \begin{cases} \alpha, & \text{if } \alpha \le a \\ 0, & \text{if } \alpha > a \end{cases}$$
Taking the supremum over all $\alpha \in [0, 1]$:
$$\sup_{\alpha \in [0, 1]} \left( \alpha \cdot \chi_{A_\alpha}(x) \right) = \sup_{\alpha \in [0, a]} \alpha = a = \mu_A(x) \qquad \blacksquare$$

---

### 3. The Second Decomposition Theorem

> **Theorem 3.4 (Second Decomposition Theorem):**
> For any fuzzy set $A$ on universe $X$:
> $$A = \bigcup_{\alpha \in [0, 1]} \alpha A_{\alpha^+} = \bigcup_{\alpha \in \Lambda(A)} \alpha A_\alpha$$
> where $\Lambda(A)$ is the level set of $A$.

This proves that ANY fuzzy set is completely and losslessly determined by its crisp $\alpha$-cuts!
Every theorem in fuzzy set theory can be proved by proving it for its crisp cuts."""
            },
            {
                "secNumber": "3.4",
                "title": "Zadeh's Extension Principle: Mapping Fuzzy Sets Through Crisp Functions $f: X \\to Y$",
                "content": r"""### 1. Motivation of the Extension Principle
Suppose we have a crisp mathematical function $f: X \to Y$ (for example, $f(x) = x^2$ or $f(x) = \sin x$), and we wish to evaluate $f$ when the input is not a crisp number, but a **fuzzy set** $A$ on $X$.
How do we compute the induced fuzzy set $B = f(A)$ on $Y$?
In 1975, Lotfi A. Zadeh formulated the **Extension Principle**, which is considered the single most important operational engine in fuzzy mathematics.

---

### 2. Formal Definition of the Extension Principle

> **Definition 3.3 (Zadeh's Extension Principle):**
> Let $f: X \to Y$ be a crisp mapping from universe $X$ to universe $Y$. Let $A$ be a fuzzy set on $X$ with membership function $\mu_A(x)$.
> The mapping $f$ induces a fuzzy set $B = f(A)$ on $Y$ whose membership function $\mu_B(y)$ is defined for all $y \in Y$ by:
> $$\mu_B(y) = \mu_{f(A)}(y) = \begin{cases} 
> \sup_{x \in f^{-1}(y)} \mu_A(x), & \text{if } f^{-1}(y) \ne \emptyset \\ 
> 0, & \text{if } f^{-1}(y) = \emptyset 
> \end{cases}$$
> where $f^{-1}(y) = \{x \in X \mid f(x) = y\}$ is the preimage of $y$.

#### Special Cases:
1. **One-to-One (Invertible) Mapping:** If $f$ is injective, each $y \in f(X)$ has a unique preimage $x = f^{-1}(y)$, so:
   $$\mu_B(y) = \mu_A(f^{-1}(y))$$
2. **Many-to-One Mapping:** If multiple distinct points $x_1, x_2, \dots$ map to the same $y$, the principle assigns $y$ the **maximum** (or supremum) of their membership grades:
   $$\mu_B(y) = \max_{x \in f^{-1}(y)} \mu_A(x)$$
   *(Optimistic principle: an outcome $y$ is as possible as the most possible input that can produce it!)*"""
            },
            {
                "secNumber": "3.5",
                "title": "Extended Functions on Cartesian Products and Verification via $\\alpha$-Cuts",
                "content": r"""### 1. Extension Principle for Multi-Argument Functions
Let $f: X_1 \times X_2 \times \dots \times X_n \to Y$ be a crisp multi-variable function (e.g. addition $f(x_1, x_2) = x_1 + x_2$, or multiplication $f(x_1, x_2) = x_1 \cdot x_2$).
Let $A_1, A_2, \dots, A_n$ be fuzzy sets defined on universes $X_1, X_2, \dots, X_n$.

> **Definition 3.4 (Multi-Variable Extension Principle):**
> The image fuzzy set $B = f(A_1, \dots, A_n)$ on $Y$ has membership function:
> $$\mu_B(y) = \begin{cases}
> \sup_{(x_1, \dots, x_n) \in f^{-1}(y)} \min\left( \mu_{A_1}(x_1), \mu_{A_2}(x_2), \dots, \mu_{A_n}(x_n) \right), & \text{if } f^{-1}(y) \ne \emptyset \\
> 0, & \text{if } f^{-1}(y) = \emptyset
> \end{cases}$$
> where $f^{-1}(y) = \{(x_1, \dots, x_n) \mid f(x_1, \dots, x_n) = y\}$.

---

### 2. Cut-Level Preservation of the Extension Principle

> **Theorem 3.5 (Nguyen's Theorem / Cut Preservation):**
> If $X$ and $Y$ are Euclidean spaces and $f: X \to Y$ is continuous, and if $A$ has compact $\alpha$-cuts, then the $\alpha$-cut of the extended fuzzy set $f(A)$ is identically the crisp image of the $\alpha$-cut of $A$:
> $$[f(A)]_\alpha = f(A_\alpha) \quad (\forall \alpha \in (0, 1])$$
> Similarly, for multi-argument functions:
> $$[f(A_1, \dots, A_n)]_\alpha = f([A_1]_\alpha, \dots, [A_n]_\alpha)$$

#### Profound Consequence:
This theorem guarantees that evaluating complicated non-linear functions of fuzzy sets via the extension principle is **completely mathematically equivalent to evaluating standard interval analysis on each $\alpha$-cut level**!
This is the foundational cornerstone of all fuzzy arithmetic."""
            }
        ],
        "problems": [
            {
                "tier": "Fundamentals",
                "title": "Problem 3.1: Explicit Calculation of $\\alpha$-Cuts for Triangular and Trapezoidal Fuzzy Sets",
                "statement": r"""Consider the real universe $X = \mathbb{R}$.
1. Let $A = \text{trimf}(x; 2, 5, 9)$ be a triangular fuzzy set.
   Derive the closed-form expression for the $\alpha$-cut interval $A_\alpha = [a_1(\alpha), a_2(\alpha)]$ as a function of $\alpha \in [0, 1]$.
   Evaluate $A_0$, $A_{0.5}$, and $A_1$.
2. Let $B = \text{trapmf}(x; 1, 4, 7, 10)$ be a trapezoidal fuzzy set.
   Derive the closed-form expression for $B_\alpha$.
   Evaluate $B_{0.25}$ and $B_{0.8}$.
3. For $A$, find the strong $\alpha$-cut $A_{0.5^+}$ and verify that $A_{0.5^+} \subset A_{0.5}$.""",
                "hints": [
                    "Set the left branch $(x - a)/(b - a) = \\alpha$ to find $a_1(\\alpha) = a + \\alpha(b - a)$.",
                    "Set the right branch $(c - x)/(c - b) = \\alpha$ to find $a_2(\\alpha) = c - \\alpha(c - b)$.",
                    "Strong cut excludes the boundary points where $\\mu(x) = \\alpha$."
                ],
                "solution": r"""### 1. Triangular Fuzzy Set $A = \text{trimf}(x; 2, 5, 9)$
The membership function is:
$$\mu_A(x) = \begin{cases} 
\frac{x - 2}{5 - 2} = \frac{x - 2}{3}, & 2 \le x \le 5 \\ 
\frac{9 - x}{9 - 5} = \frac{9 - x}{4}, & 5 \le x \le 9 \\ 
0, & \text{otherwise} 
\end{cases}$$

#### Derivation of $\alpha$-cut $A_\alpha$:
- Left bound: $\frac{x - 2}{3} = \alpha \implies x = 2 + 3\alpha$.
- Right bound: $\frac{9 - x}{4} = \alpha \implies x = 9 - 4\alpha$.
Thus, for $\alpha \in (0, 1]$:
$$A_\alpha = [2 + 3\alpha, \; 9 - 4\alpha] \qquad \blacksquare$$

#### Specific Evaluations:
- $\alpha = 0$: $A_0 = [2, 9]$ (the support closure).
- $\alpha = 0.5$: $A_{0.5} = [2 + 3(0.5), 9 - 4(0.5)] = [3.5, 7.0]$.
- $\alpha = 1.0$: $A_1 = [2 + 3(1), 9 - 4(1)] = [5, 5] = \{5\}$ (the core). $\blacksquare$

---

### 2. Trapezoidal Fuzzy Set $B = \text{trapmf}(x; 1, 4, 7, 10)$
- Left branch ($1 \le x \le 4$): $\frac{x - 1}{4 - 1} = \frac{x - 1}{3} = \alpha \implies x = 1 + 3\alpha$.
- Core ($4 \le x \le 7$): $\mu_B(x) = 1 \ge \alpha$.
- Right branch ($7 \le x \le 10$): $\frac{10 - x}{10 - 7} = \frac{10 - x}{3} = \alpha \implies x = 10 - 3\alpha$.
Thus:
$$B_\alpha = [1 + 3\alpha, \; 10 - 3\alpha] \qquad \blacksquare$$

#### Specific Evaluations:
- $\alpha = 0.25$: $B_{0.25} = [1 + 3(0.25), 10 - 3(0.25)] = [1.75, 9.25]$.
- $\alpha = 0.80$: $B_{0.80} = [1 + 3(0.8), 10 - 3(0.8)] = [3.4, 7.6]$. $\blacksquare$

---

### 3. Strong $\alpha$-Cut $A_{0.5^+}$
The strong cut requires $\mu_A(x) > 0.5$:
- For $x \in [2, 5]$: $\frac{x - 2}{3} > 0.5 \implies x > 3.5$.
- For $x \in [5, 9]$: $\frac{9 - x}{4} > 0.5 \implies 9 - x > 2 \implies x < 7.0$.
Therefore, the strong cut is the open interval:
$$A_{0.5^+} = (3.5, 7.0)$$
Comparing with the weak cut $A_{0.5} = [3.5, 7.0]$, the boundary points $\{3.5, 7.0\}$ where $\mu_A(x) = 0.5$ belong to $A_{0.5}$ but not to $A_{0.5^+}$.
Thus $A_{0.5^+} \subset A_{0.5}$ strictly. $\blacksquare$"""
            },
            {
                "tier": "Computational Triad",
                "title": "Problem 3.2: Applying the Extension Principle to Non-Linear Functions",
                "statement": r"""Let $X = [-4, 4]$ and let $A$ be a triangular fuzzy set on $X$ defined by $A = \text{trimf}(x; -2, 1, 3)$.
Consider the non-linear crisp function $f(x) = x^2$.
1. Using Zadeh's Extension Principle, determine the membership function $\mu_B(y)$ of the induced fuzzy set $B = f(A)$ on $Y = [0, 16]$.
2. Identify the core, support, and height of $B$.
3. Verify your result using the $\alpha$-cut method ($B_\alpha = f(A_\alpha)$).""",
                "hints": [
                    "Notice that $f(x) = x^2$ is not one-to-one on $[-2, 3]$: for $y \\in [0, 4]$, both $+\\sqrt{y}$ and $-\\sqrt{y}$ map to $y$.",
                    "For $y \\in [0, 4]$, $\\mu_B(y) = \\max(\\mu_A(-\\sqrt{y}), \\mu_A(\\sqrt{y}))$.",
                    "For $\\alpha$-cuts: $A_\\alpha = [-2 + 3\\alpha, 3 - 2\\alpha]$. Square this interval using interval arithmetic."
                ],
                "solution": r"""### 1. Evaluation via Extension Principle
$$\mu_B(y) = \sup_{x \in f^{-1}(y)} \mu_A(x) = \sup_{x: x^2 = y} \mu_A(x)$$
For $y \ge 0$, the preimages are $x = +\sqrt{y}$ and $x = -\sqrt{y}$.
The membership function of $A$ is:
$$\mu_A(x) = \begin{cases} 
\frac{x - (-2)}{1 - (-2)} = \frac{x + 2}{3}, & -2 \le x \le 1 \\ 
\frac{3 - x}{3 - 1} = \frac{3 - x}{2}, & 1 \le x \le 3 \\ 
0, & \text{otherwise} 
\end{cases}$$

#### Case 1: $y \in [0, 1]$
Here $x = +\sqrt{y} \in [0, 1]$ and $x = -\sqrt{y} \in [-1, 0]$.
Both preimages fall in the rising branch $[-2, 1]$:
- $\mu_A(+\sqrt{y}) = \frac{\sqrt{y} + 2}{3}$
- $\mu_A(-\sqrt{y}) = \frac{-\sqrt{y} + 2}{3}$
Since $\frac{\sqrt{y} + 2}{3} \ge \frac{-\sqrt{y} + 2}{3}$ for all $y \ge 0$:
$$\mu_B(y) = \frac{\sqrt{y} + 2}{3}, \quad y \in [0, 1]$$
At $y = 1$: $\mu_B(1) = \frac{1 + 2}{3} = 1.0$.

#### Case 2: $y \in [1, 4]$
Here $x = +\sqrt{y} \in [1, 2]$ falls in the falling branch:
$$\mu_A(+\sqrt{y}) = \frac{3 - \sqrt{y}}{2}$$
While $x = -\sqrt{y} \in [-2, -1]$ falls in the rising branch:
$$\mu_A(-\sqrt{y}) = \frac{-\sqrt{y} + 2}{3}$$
Compare the two values:
$$\frac{3 - \sqrt{y}}{2} - \frac{2 - \sqrt{y}}{3} = \frac{3(3 - \sqrt{y}) - 2(2 - \sqrt{y})}{6} = \frac{9 - 3\sqrt{y} - 4 + 2\sqrt{y}}{6} = \frac{5 - \sqrt{y}}{6}$$
Since $y \le 4 \implies \sqrt{y} \le 2$, we have $5 - \sqrt{y} \ge 3 > 0$.
Thus $\mu_A(+\sqrt{y}) > \mu_A(-\sqrt{y})$ everywhere on $[1, 4]$!
Therefore:
$$\mu_B(y) = \frac{3 - \sqrt{y}}{2}, \quad y \in [1, 4]$$

#### Case 3: $y \in [4, 9]$
Here $-\sqrt{y} \le -2$, so $\mu_A(-\sqrt{y}) = 0$.
Only $+\sqrt{y} \in [2, 3]$ has positive membership:
$$\mu_B(y) = \frac{3 - \sqrt{y}}{2}, \quad y \in [4, 9]$$

#### Case 4: $y > 9$
$\mu_B(y) = 0$.

#### Final Piecewise Expression:
$$\mu_B(y) = \begin{cases} 
\frac{\sqrt{y} + 2}{3}, & 0 \le y \le 1 \\ 
\frac{3 - \sqrt{y}}{2}, & 1 \le y \le 9 \\ 
0, & \text{otherwise} 
\end{cases} \qquad \blacksquare$$

---

### 2. Core, Support, and Height
- **Core:** $\{y \in [0, 16] \mid \mu_B(y) = 1\} = \{1\}$.
- **Support:** $\{y \in [0, 16] \mid \mu_B(y) > 0\} = [0, 9)$.
- **Height:** $h(B) = \mu_B(1) = 1.0$ (normal fuzzy set). $\blacksquare$

---

### 3. Verification via $\alpha$-Cuts
For $A = \text{trimf}(x; -2, 1, 3)$:
$$A_\alpha = [-2 + 3\alpha, \; 3 - 2\alpha]$$
Applying $f(x) = x^2$ to the interval $[a_1, a_2] = [-2 + 3\alpha, 3 - 2\alpha]$:
Since the interval contains $x = 0$ for $\alpha \le 2/3$, the minimum square is 0 for small $\alpha$, and $(-2 + 3\alpha)^2$ for $\alpha > 2/3$.
The maximum square is achieved at $(3 - 2\alpha)^2$.
Thus:
- Right boundary: $y = (3 - 2\alpha)^2 \implies \sqrt{y} = 3 - 2\alpha \implies \alpha = \frac{3 - \sqrt{y}}{2}$.
- Left boundary (when $\alpha > 2/3$): $y = (3\alpha - 2)^2 \implies \sqrt{y} = 3\alpha - 2 \implies \alpha = \frac{\sqrt{y} + 2}{3}$.
This matches the Extension Principle derivation identically! $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 3.3: Complete Proof of the Second Decomposition Theorem",
                "statement": r"""The Second Decomposition Theorem states that any fuzzy set $A$ on universe $X$ can be reconstructed from its strong $\alpha$-cuts:
$$A = \bigcup_{\alpha \in [0, 1]} \alpha A_{\alpha^+}$$
and also from the finite set of distinct levels if $X$ is finite:
$$A = \bigcup_{i=1}^k \alpha_i A_{\alpha_i}$$
where $\Lambda(A) = \{\alpha_1, \alpha_2, \dots, \alpha_k\}$ with $0 = \alpha_0 < \alpha_1 < \dots < \alpha_k \le 1$.

1. Provide a rigorous, line-by-line mathematical proof that for all $x \in X$:
   $$\mu_A(x) = \sup_{\alpha \in [0, 1]} \left( \alpha \cdot \chi_{A_{\alpha^+}}(x) \right)$$
2. For a discrete universe $X = \{x_1, \dots, x_n\}$, prove that:
   $$\mu_A(x) = \max_{1 \le i \le k} \left( \alpha_i \cdot \chi_{A_{\alpha_i}}(x) \right)$$
3. Illustrate this theorem explicitly for the fuzzy set:
   $$A = \frac{0.2}{x_1} + \frac{0.5}{x_2} + \frac{0.8}{x_3} + \frac{1.0}{x_4}$$
   by expressing $A$ as an explicit union of four crisp cut sets.""",
                "hints": [
                    "For part 1, let $a = \\mu_A(x)$. Note that $x \\in A_{\\alpha^+} \\iff \\alpha < a$.",
                    "Evaluate $\\sup_{\\alpha < a} \\alpha = a$.",
                    "For part 3, write each term $\\alpha_i A_{\\alpha_i}$ explicitly as a fuzzy subset."
                ],
                "solution": r"""### 1. Proof of the Second Decomposition Theorem (Strong Cuts)
Let $x \in X$ be arbitrary, and let $a = \mu_A(x) \in [0, 1]$.
We must evaluate:
$$S(x) \equiv \sup_{\alpha \in [0, 1]} \mu_{\alpha A_{\alpha^+}}(x) = \sup_{\alpha \in [0, 1]} \left( \alpha \cdot \chi_{A_{\alpha^+}}(x) \right)$$

Recall Definition 3.1:
$$x \in A_{\alpha^+} \iff \mu_A(x) > \alpha \iff a > \alpha \iff \alpha \in [0, a)$$
Therefore, the characteristic function is:
$$\chi_{A_{\alpha^+}}(x) = \begin{cases} 1, & \text{if } 0 \le \alpha < a \\ 0, & \text{if } \alpha \ge a \end{cases}$$
Substituting this into the product:
$$\alpha \cdot \chi_{A_{\alpha^+}}(x) = \begin{cases} \alpha, & \text{if } 0 \le \alpha < a \\ 0, & \text{if } \alpha \ge a \end{cases}$$
Now take the supremum over all $\alpha \in [0, 1]$:
- If $a = 0$: the set $\{\alpha \in [0, 1] \mid \alpha < 0\} = \emptyset$, so the product is 0 for all $\alpha$, and the supremum is 0, which equals $a = \mu_A(x)$.
- If $a > 0$:
  $$S(x) = \sup_{\alpha \in [0, a)} \alpha = a = \mu_A(x)$$
In all cases, $S(x) = \mu_A(x)$.
Since $x \in X$ was arbitrary, we have proven:
$$A = \bigcup_{\alpha \in [0, 1]} \alpha A_{\alpha^+} \qquad \blacksquare$$

---

### 2. Proof for Finite Level Sets
Let $\Lambda(A) = \{\alpha_1, \alpha_2, \dots, \alpha_k\}$ be the set of distinct non-zero membership grades, with:
$$0 < \alpha_1 < \alpha_2 < \dots < \alpha_k = h(A) \le 1$$
For any $x \in X$, there exists some $j \in \{1, \dots, k\}$ such that $\mu_A(x) = \alpha_j$ (or $\mu_A(x) = 0$).
If $\mu_A(x) = \alpha_j > 0$:
Then $x \in A_{\alpha_i} \iff \mu_A(x) \ge \alpha_i \iff \alpha_j \ge \alpha_i \iff i \le j$.
Therefore:
$$\chi_{A_{\alpha_i}}(x) = \begin{cases} 1, & 1 \le i \le j \\ 0, & i > j \end{cases}$$
Then:
$$\max_{1 \le i \le k} \left( \alpha_i \cdot \chi_{A_{\alpha_i}}(x) \right) = \max_{1 \le i \le j} \alpha_i = \alpha_j = \mu_A(x)$$
If $\mu_A(x) = 0$, $x \notin A_{\alpha_i}$ for all $i \ge 1$, so the maximum is 0.
Thus:
$$A = \bigcup_{i=1}^k \alpha_i A_{\alpha_i} \qquad \blacksquare$$

---

### 3. Explicit Demonstration
Let $A = \frac{0.2}{x_1} + \frac{0.5}{x_2} + \frac{0.8}{x_3} + \frac{1.0}{x_4}$.
The level set is $\Lambda(A) = \{0.2, 0.5, 0.8, 1.0\}$.

#### Step A: Determine the Crisp Cuts:
- $A_{0.2} = \{x_1, x_2, x_3, x_4\}$
- $A_{0.5} = \{x_2, x_3, x_4\}$
- $A_{0.8} = \{x_3, x_4\}$
- $A_{1.0} = \{x_4\}$

#### Step B: Construct the Scaled Fuzzy Sets $\alpha_i A_{\alpha_i}$:
- $0.2 A_{0.2} = \frac{0.2}{x_1} + \frac{0.2}{x_2} + \frac{0.2}{x_3} + \frac{0.2}{x_4}$
- $0.5 A_{0.5} = \frac{0.0}{x_1} + \frac{0.5}{x_2} + \frac{0.5}{x_3} + \frac{0.5}{x_4}$
- $0.8 A_{0.8} = \frac{0.0}{x_1} + \frac{0.0}{x_2} + \frac{0.8}{x_3} + \frac{0.8}{x_4}$
- $1.0 A_{1.0} = \frac{0.0}{x_1} + \frac{0.0}{x_2} + \frac{0.0}{x_3} + \frac{1.0}{x_4}$

#### Step C: Take the Standard Union (Max):
$$\begin{aligned}
\bigcup_{i=1}^4 \alpha_i A_{\alpha_i} &= \frac{\max(0.2, 0, 0, 0)}{x_1} + \frac{\max(0.2, 0.5, 0, 0)}{x_2} + \frac{\max(0.2, 0.5, 0.8, 0)}{x_3} + \frac{\max(0.2, 0.5, 0.8, 1.0)}{x_4} \\
&= \frac{0.2}{x_1} + \frac{0.5}{x_2} + \frac{0.8}{x_3} + \frac{1.0}{x_4} = A
\end{aligned}$$
The reconstructed fuzzy set equals $A$ exactly! $\blacksquare$"""
            }
        ]
    }
    return u3

if __name__ == "__main__":
    u3 = get_unit3()
    print(f"Loaded Unit 3: {u3['title']} with {len(u3['sections'])} sections and {len(u3['problems'])} problems.")
