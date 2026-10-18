# -*- coding: utf-8 -*-
"""
build_fuzzy_unit1.py
Constructs Unit 1: Crisp Sets, Fuzzy Sets & Membership Foundations
Strictly ZERO course numbers.
"""

def get_unit1():
    u1 = {
        "number": 1,
        "title": "Crisp Sets, Fuzzy Sets & Membership Foundations",
        "leadSummary": "Foundational transition from classical set theory to fuzzy set theory: characteristic functions vs continuous membership functions \\mu_A(x) \\in [0, 1], support, core, height, and boundary of fuzzy sets, classical bivalent logic vs infinite-valued fuzzy logic, standard parametric families of membership functions (triangular, trapezoidal, Gaussian, generalized bell, sigmoidal), fuzzy singletons, convex fuzzy sets, and normal vs subnormal fuzzy sets.",
        "simulations": ["sim_fuzzy_membership_designer"],
        "sections": [
            {
                "secNumber": "1.1",
                "title": "Foundations of Classical (Crisp) Sets, Characteristic Functions & Power Sets",
                "content": r"""### 1. Classical Set Theory and the Law of Excluded Middle
In classical (Cantorian) set theory, an element $x$ from a universe of discourse $X$ either strictly belongs to a subset $A$ or does not. This rigid binarism is grounded in Aristotle's classical laws of thought:
1. **The Law of Contradiction:** $A \cap A^c = \emptyset$ (nothing can be both $A$ and not-$A$).
2. **The Law of Excluded Middle (Tertium Non Datur):** $A \cup A^c = X$ (everything must be either $A$ or not-$A$; there is no middle ground).

---

### 2. The Characteristic Function
Formally, any classical ("crisp") set $A \subseteq X$ is uniquely identified by its **characteristic function** $\chi_A: X \to \{0, 1\}$:

$$\chi_A(x) = \begin{cases} 1, & \text{if } x \in A \\ 0, & \text{if } x \notin A \end{cases}$$

The set of all subsets of $X$ is the **power set** $\mathcal{P}(X) = 2^X$.
The classical set operations are completely isomorphic to Boolean operations on characteristic functions:
- **Intersection:** $\chi_{A \cap B}(x) = \min(\chi_A(x), \chi_B(x)) = \chi_A(x) \cdot \chi_B(x)$
- **Union:** $\chi_{A \cup B}(x) = \max(\chi_A(x), \chi_B(x)) = \chi_A(x) + \chi_B(x) - \chi_A(x)\chi_B(x)$
- **Complement:** $\chi_{A^c}(x) = 1 - \chi_A(x)$

---

### 3. Limitations in Modeling Real-World Vagueness
While crisp sets are ideal for exact mathematics and discrete computing, human cognition and natural language deal inherently with **imprecision, vagueness, and continuous gradation**.
Concepts such as *"high temperature"*, *"young person"*, *"fast vehicle"*, or *"safe following distance"* do not possess abrupt, crisp boundaries:
- Is a person aged 29 years and 364 days "young", but instantaneously "not young" at midnight of their 30th birthday?
- This classical dilemma is known as the **Sorites Paradox** (the paradox of the heap).
To model such gradual transitions rigorously, Lotfi A. Zadeh (1965) generalized the characteristic function from the discrete binary codomain $\{0, 1\}$ to the real continuous unit interval $[0, 1]$."""
            },
            {
                "secNumber": "1.2",
                "title": "The Notion of Fuzzy Sets, Membership Functions $\\mu_A(x) \\in [0, 1]$ & Support/Core/Boundary",
                "content": r"""### 1. Definition of a Fuzzy Set
In his seminal 1965 paper *"Fuzzy Sets"*, Lotfi A. Zadeh introduced the fundamental concept:

> **Definition 1.1 (Fuzzy Set):**
> Let $X$ be a non-empty classical set called the **universe of discourse**. A **fuzzy set** $A$ in $X$ is characterized by a **membership function**:
> $$\mu_A: X \to [0, 1]$$
> where the real number $\mu_A(x)$ represents the **degree of membership** (or grade of belonging) of element $x$ in the fuzzy set $A$.
> - $\mu_A(x) = 1$ denotes full, unequivocal membership.
> - $\mu_A(x) = 0$ denotes absolute non-membership.
> - $0 < \mu_A(x) < 1$ represents intermediate, gradual degrees of membership.

#### Representation Notations:
1. **Discrete Universe:** If $X = \{x_1, x_2, \dots, x_n\}$ is discrete:
   $$A = \sum_{i=1}^n \frac{\mu_A(x_i)}{x_i} = \frac{\mu_A(x_1)}{x_1} + \frac{\mu_A(x_2)}{x_2} + \dots + \frac{\mu_A(x_n)}{x_n}$$
   *(Note: The summation $\sum$ and slash $/$ denote collection and pairing, NOT arithmetic addition or division!)*
2. **Continuous Universe:** If $X$ is a continuous real domain (e.g. $\mathbb{R}$):
   $$A = \int_X \frac{\mu_A(x)}{x}$$

---

### 2. Fundamental Geometric Regions of a Fuzzy Set

> **Definition 1.2 (Support, Core, Height, and Boundary):**
> Let $A$ be a fuzzy set in universe $X$ with membership function $\mu_A(x)$.
> 1. **Support of $A$:** The crisp subset of $X$ containing all elements with strictly positive membership:
>    $$\text{Supp}(A) = \{x \in X \mid \mu_A(x) > 0\}$$
> 2. **Core (Kernel) of $A$:** The crisp subset of $X$ containing all elements with full membership:
>    $$\text{Core}(A) = \{x \in X \mid \mu_A(x) = 1\}$$
> 3. **Height of $A$:** The supremum of the membership grades over the entire universe:
>    $$h(A) = \sup_{x \in X} \mu_A(x)$$
> 4. **Boundary of $A$:** The region of intermediate, uncertain membership:
>    $$\text{Bnd}(A) = \{x \in X \mid 0 < \mu_A(x) < 1\} = \text{Supp}(A) \setminus \text{Core}(A)$$

#### Normal vs Subnormal Fuzzy Sets:
- A fuzzy set $A$ is called **normal** if its height is exactly 1:
  $$h(A) = \sup_{x \in X} \mu_A(x) = 1 \iff \text{Core}(A) \ne \emptyset$$
- Otherwise, if $h(A) < 1$, the fuzzy set is called **subnormal**. Any subnormal set with $h(A) > 0$ can be normalized via:
  $$\mu_{A_{\text{norm}}}(x) = \frac{\mu_A(x)}{h(A)}$$"""
            },
            {
                "secNumber": "1.3",
                "title": "Classical Propositional Logic vs Many-Valued & Fuzzy Logic (Łukasiewicz, Gödel, Zadeh)",
                "content": r"""### 1. From Boolean Logic to Infinite-Valued Logic
Classical Boolean logic is restricted to truth values $T = \{0, 1\}$.
In 1920, Jan Łukasiewicz introduced 3-valued logic ($T_3 = \{0, \frac{1}{2}, 1\}$) and subsequently generalized it to the continuum of truth values $T_\infty = [0, 1]$.
Fuzzy logic is an infinite-valued logic in which truth values are degrees of truth in the closed interval $[0, 1]$.

---

### 2. Major Fuzzy Logic Valuations
Let $v(P) \in [0, 1]$ and $v(Q) \in [0, 1]$ denote the truth values of propositions $P$ and $Q$.

#### 1. Standard Zadeh Logic:
- **Negation:** $v(\neg P) = 1 - v(P)$
- **Conjunction ($\wedge$):** $v(P \wedge Q) = \min(v(P), v(Q))$
- **Disjunction ($\vee$):** $v(P \vee Q) = \max(v(P), v(Q))$
- **Implication (Kleene-Dienes):** $v(P \implies Q) = \max(1 - v(P), v(Q))$

#### 2. Łukasiewicz Logic:
- **Conjunction (Bounded Product):** $v(P \wedge_L Q) = \max(0, v(P) + v(Q) - 1)$
- **Disjunction (Bounded Sum):** $v(P \vee_L Q) = \min(1, v(P) + v(Q))$
- **Implication (Łukasiewicz Implication):**
  $$v(P \implies_L Q) = \min(1, 1 - v(P) + v(Q))$$

#### 3. Gödel-Dummett Logic:
- **Implication (Gödel Residuated Implication):**
  $$v(P \implies_G Q) = \begin{cases} 1, & \text{if } v(P) \le v(Q) \\ v(Q), & \text{if } v(P) > v(Q) \end{cases}$$

#### 4. Product (Goguen) Logic:
- **Conjunction:** $v(P \cdot Q) = v(P) \cdot v(Q)$
- **Implication (Goguen Implication):**
  $$v(P \implies_P Q) = \begin{cases} 1, & \text{if } v(P) \le v(Q) \\ \frac{v(Q)}{v(P)}, & \text{if } v(P) > v(Q) \end{cases}$$

---

### 3. Failure of Classical Tautologies in Fuzzy Logic
In classical logic, $P \vee \neg P \equiv 1$ (Law of Excluded Middle) and $P \wedge \neg P \equiv 0$ (Law of Contradiction) are universal tautologies.
In Zadeh fuzzy logic with $v(P) = 0.5$:
$$v(P \vee \neg P) = \max(0.5, 1 - 0.5) = \max(0.5, 0.5) = 0.5 \ne 1$$
$$v(P \wedge \neg P) = \min(0.5, 1 - 0.5) = \min(0.5, 0.5) = 0.5 \ne 0$$
Thus, **fuzzy sets do NOT generally satisfy the Law of Excluded Middle or the Law of Contradiction**! This non-trivial property reflects the presence of inherent fuzziness."""
            },
            {
                "secNumber": "1.4",
                "title": "Types of Membership Functions: Triangular, Trapezoidal, Gaussian, Sigmoidal & Generalized Bell",
                "content": r"""### 1. Parametric Membership Function Families
In applications to engineering, control theory, and expert systems, membership functions are parameterized mathematically to enable efficient computation and gradient-based tuning.

---

### 2. Piecewise Linear Membership Functions

#### 1. Triangular Membership Function $\text{trimf}(x; a, b, c)$:
Defined by three parameters $a < b < c$ where $b$ is the peak (core) and $[a, c]$ is the support:
$$\mu(x; a, b, c) = \begin{cases} 
0, & x \le a \\ 
\frac{x - a}{b - a}, & a \le x \le b \\ 
\frac{c - x}{c - b}, & b \le x \le c \\ 
0, & x \ge c 
\end{cases} = \max\left( 0, \min\left( \frac{x - a}{b - a}, \frac{c - x}{c - b} \right) \right)$$

#### 2. Trapezoidal Membership Function $\text{trapmf}(x; a, b, c, d)$:
Defined by four parameters $a < b \le c < d$, where $[b, c]$ is the core and $[a, d]$ is the support:
$$\mu(x; a, b, c, d) = \begin{cases} 
0, & x \le a \\ 
\frac{x - a}{b - a}, & a \le x \le b \\ 
1, & b \le x \le c \\ 
\frac{d - x}{d - c}, & c \le x \le d \\ 
0, & x \ge d 
\end{cases} = \max\left( 0, \min\left( \frac{x - a}{b - a}, 1, \frac{d - x}{d - c} \right) \right)$$

---

### 3. Smooth Differentiable Membership Functions

#### 3. Gaussian Membership Function $\text{gaussmf}(x; c, \sigma)$:
Characterized by center $c$ and standard deviation $\sigma > 0$:
$$\mu(x; c, \sigma) = \exp\left( -\frac{(x - c)^2}{2\sigma^2} \right)$$
- Core: $\{c\}$
- Support: $\mathbb{R}$ (infinitely supported, but practically localized within $c \pm 3\sigma$)
- Strictly smooth ($C^\infty$) and non-zero everywhere.

#### 4. Generalized Bell Membership Function $\text{gbellmf}(x; a, b, c)$:
Characterized by half-width $a$, slope parameter $b > 0$, and center $c$:
$$\mu(x; a, b, c) = \frac{1}{1 + \left| \frac{x - c}{a} \right|^{2b}}$$

#### 5. Sigmoidal Membership Function $\text{sigmf}(x; a, c)$:
Used for representing open-ended linguistic concepts such as *"large"* or *"high"*:
$$\mu(x; a, c) = \frac{1}{1 + \exp(-a(x - c))}$$
where $a$ governs the steepness of the transition at inflection point $c$."""
            },
            {
                "secNumber": "1.5",
                "title": "Fuzzy Singletons, Convex Fuzzy Sets, and Normal vs Subnormal Fuzzy Sets",
                "content": r"""### 1. Fuzzy Singletons
> **Definition 1.3 (Fuzzy Singleton):**
> A fuzzy set $A$ on universe $X$ whose support is a single point $x_0 \in X$ with membership grade $\mu_A(x_0) = \alpha \in (0, 1]$ is called a **fuzzy singleton**:
> $$\mu_A(x) = \begin{cases} \alpha, & x = x_0 \\ 0, & x \ne x_0 \end{cases}$$
> If $\alpha = 1$, it represents the crisp point $x_0$ embedded into fuzzy set theory.

---

### 2. Convex Fuzzy Sets
In classical geometry, a set $S \subseteq \mathbb{R}^n$ is convex if for any two points $x_1, x_2 \in S$, the entire line segment connecting them lies in $S$: $\lambda x_1 + (1 - \lambda) x_2 \in S$ for all $\lambda \in [0, 1]$.
In fuzzy set theory on $\mathbb{R}^n$, convexity is generalized through membership grades:

> **Definition 1.4 (Convex Fuzzy Set):**
> A fuzzy set $A$ in $\mathbb{R}^n$ is called **fuzzy convex** if and only if for all $x_1, x_2 \in \mathbb{R}^n$ and all $\lambda \in [0, 1]$:
> $$\mu_A(\lambda x_1 + (1 - \lambda) x_2) \ge \min(\mu_A(x_1), \mu_A(x_2))$$

#### Critical Distinction:
A fuzzy convex membership function $\mu_A(x)$ is **quasiconcave** in the terminology of real analysis! Its graph does NOT need to be a convex curve; rather, its upper contour sets (level sets) must be convex crisp sets.
- If $X = \mathbb{R}$, a fuzzy set is convex if and only if its membership function is monotonically non-decreasing up to the core, and monotonically non-increasing thereafter (i.e. single-peaked or plateau-topped).

---

### 3. The Convexity Theorem for $\alpha$-Cuts

> **Theorem 1.1 (Equivalence with Convex $\alpha$-Cuts):**
> A fuzzy set $A$ on $\mathbb{R}^n$ is fuzzy convex if and only if every crisp $\alpha$-cut:
> $$A_\alpha = \{x \in \mathbb{R}^n \mid \mu_A(x) \ge \alpha\}$$
> is a classical convex set for all $\alpha \in (0, 1]$.

#### Proof:
1. **Necessity ($\implies$):** Assume $A$ is fuzzy convex. Let $\alpha \in (0, 1]$ and choose $x_1, x_2 \in A_\alpha$.
   Then $\mu_A(x_1) \ge \alpha$ and $\mu_A(x_2) \ge \alpha$.
   By fuzzy convexity, for any $\lambda \in [0, 1]$:
   $$\mu_A(\lambda x_1 + (1 - \lambda) x_2) \ge \min(\mu_A(x_1), \mu_A(x_2)) \ge \min(\alpha, \alpha) = \alpha$$
   Therefore, $\lambda x_1 + (1 - \lambda) x_2 \in A_\alpha$, proving $A_\alpha$ is a convex set.
2. **Sufficiency ($\impliedby$):** Assume $A_\alpha$ is convex for all $\alpha \in (0, 1]$.
   For any $x_1, x_2 \in \mathbb{R}^n$, set $\alpha_0 = \min(\mu_A(x_1), \mu_A(x_2))$.
   If $\alpha_0 = 0$, then $\mu_A(\lambda x_1 + (1 - \lambda) x_2) \ge 0 = \alpha_0$ trivially.
   If $\alpha_0 > 0$, then $x_1 \in A_{\alpha_0}$ and $x_2 \in A_{\alpha_0}$.
   Since $A_{\alpha_0}$ is convex, $\lambda x_1 + (1 - \lambda) x_2 \in A_{\alpha_0}$ for all $\lambda \in [0, 1]$.
   This implies $\mu_A(\lambda x_1 + (1 - \lambda) x_2) \ge \alpha_0 = \min(\mu_A(x_1), \mu_A(x_2))$. $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "tier": "Fundamentals",
                "title": "Problem 1.1: Core, Support, and Membership of Triangular and Gaussian Fuzzy Sets",
                "statement": r"""Consider the universe of discourse $X = \mathbb{R}$.
1. Let $A$ be a triangular fuzzy set $\text{trimf}(x; 10, 20, 35)$.
   Determine explicitly its Core, Support, Height, and the membership grade at $x = 15$ and $x = 30$.
2. Let $B$ be a Gaussian fuzzy set $\text{gaussmf}(x; 25, 4)$.
   Determine its Height, Core, Support, and calculate the points $x$ where $\mu_B(x) = 0.5$ (the crossover points).
3. State whether $A$ and $B$ are normal and fuzzy convex, justifying your answer from first principles.""",
                "hints": [
                    "For triangular fuzzy set, Core is $\{b\}$ where $\\mu(b) = 1$.",
                    "Support is open interval $(a, c)$ where $\\mu(x) > 0$.",
                    "For crossover points of Gaussian, solve $\\exp(-(x-c)^2 / (2\\sigma^2)) = 0.5$."
                ],
                "solution": r"""### 1. Analysis of Triangular Fuzzy Set $A = \text{trimf}(x; 10, 20, 35)$
- **Core:** The set of points where $\mu_A(x) = 1$:
  $$\text{Core}(A) = \{20\}$$
- **Support:** The set of points where $\mu_A(x) > 0$:
  $$\text{Supp}(A) = (10, 35)$$
- **Height:** The maximum membership grade:
  $$h(A) = \mu_A(20) = 1.0$$
- **Membership at $x = 15$:** Since $10 \le 15 \le 20$:
  $$\mu_A(15) = \frac{15 - 10}{20 - 10} = \frac{5}{10} = 0.5$$
- **Membership at $x = 30$:** Since $20 \le 30 \le 35$:
  $$\mu_A(30) = \frac{35 - 30}{35 - 20} = \frac{5}{15} = \frac{1}{3} \approx 0.3333 \qquad \blacksquare$$

---

### 2. Analysis of Gaussian Fuzzy Set $B = \text{gaussmf}(x; 25, 4)$
$$\mu_B(x) = \exp\left( -\frac{(x - 25)^2}{2(4^2)} \right) = \exp\left( -\frac{(x - 25)^2}{32} \right)$$
- **Height:** Maximum occurs at $x = 25$:
  $$h(B) = \mu_B(25) = \exp(0) = 1.0$$
- **Core:** $\text{Core}(B) = \{25\}$.
- **Support:** Since $\exp(-y) > 0$ for all finite $y \in \mathbb{R}$:
  $$\text{Supp}(B) = \mathbb{R} = (-\infty, \infty)$$
- **Crossover Points ($\mu_B(x) = 0.5$):**
  $$\exp\left( -\frac{(x - 25)^2}{32} \right) = \frac{1}{2} \implies -\frac{(x - 25)^2}{32} = -\ln 2$$
  $$(x - 25)^2 = 32 \ln 2 \approx 32(0.69315) \approx 22.1807$$
  $$x - 25 = \pm \sqrt{32 \ln 2} \approx \pm 4.7096$$
  $$x_1 \approx 20.2904, \qquad x_2 \approx 29.7096 \qquad \blacksquare$$

---

### 3. Normality and Convexity
- **Normality:** Both $A$ and $B$ are **normal** because $h(A) = 1$ and $h(B) = 1$.
- **Convexity:**
  - For $A$, the function strictly increases on $[10, 20]$ and strictly decreases on $[20, 35]$. Every $\alpha$-cut is a closed bounded interval $[10 + 10\alpha, 35 - 15\alpha]$, which is a convex subset of $\mathbb{R}$. Hence $A$ is **fuzzy convex**.
  - For $B$, $\mu_B(x)$ is strictly increasing for $x \le 25$ and strictly decreasing for $x \ge 25$. Every $\alpha$-cut is an interval $[25 - 4\sqrt{2\ln(1/\alpha)}, 25 + 4\sqrt{2\ln(1/\alpha)}]$, which is convex. Hence $B$ is **fuzzy convex**. $\blacksquare$"""
            },
            {
                "tier": "Computational Triad",
                "title": "Problem 1.2: Discrete Universe Operations and Non-Excluded Middle Verification",
                "statement": r"""Let the universe of discourse be $X = \{1, 2, 3, 4, 5, 6, 7\}$.
Two fuzzy sets $A$ and $B$ are defined on $X$ by:
$$A = \frac{0.1}{1} + \frac{0.4}{2} + \frac{0.8}{3} + \frac{1.0}{4} + \frac{0.7}{5} + \frac{0.3}{6} + \frac{0.0}{7}$$
$$B = \frac{0.0}{1} + \frac{0.2}{2} + \frac{0.6}{3} + \frac{0.9}{4} + \frac{1.0}{5} + \frac{0.5}{6} + \frac{0.2}{7}$$

1. Compute the standard complement $A^c$.
2. Compute the standard union $A \cup B$ and intersection $A \cap B$.
3. Compute the algebraic product $A \cdot B$ and algebraic sum $A \oplus B$.
4. Evaluate $A \cap A^c$ and $A \cup A^c$. Verify whether the Law of Contradiction and the Law of Excluded Middle hold.""",
                "hints": [
                    "Standard complement: $\\mu_{A^c}(x) = 1 - \\mu_A(x)$.",
                    "Algebraic product: $\\mu_{A \\cdot B}(x) = \\mu_A(x) \\mu_B(x)$.",
                    "Algebraic sum: $\\mu_{A \\oplus B}(x) = \\mu_A(x) + \\mu_B(x) - \\mu_A(x)\\mu_B(x)$."
                ],
                "solution": r"""### 1. Standard Complement $A^c$
Using $\mu_{A^c}(x) = 1 - \mu_A(x)$:
- $x=1: 1 - 0.1 = 0.9$
- $x=2: 1 - 0.4 = 0.6$
- $x=3: 1 - 0.8 = 0.2$
- $x=4: 1 - 1.0 = 0.0$
- $x=5: 1 - 0.7 = 0.3$
- $x=6: 1 - 0.3 = 0.7$
- $x=7: 1 - 0.0 = 1.0$
$$A^c = \frac{0.9}{1} + \frac{0.6}{2} + \frac{0.2}{3} + \frac{0.0}{4} + \frac{0.3}{5} + \frac{0.7}{6} + \frac{1.0}{7} \qquad \blacksquare$$

---

### 2. Standard Union and Intersection
Using $\mu_{A \cup B}(x) = \max(\mu_A(x), \mu_B(x))$ and $\mu_{A \cap B}(x) = \min(\mu_A(x), \mu_B(x))$:
$$A \cup B = \frac{\max(0.1, 0.0)}{1} + \frac{\max(0.4, 0.2)}{2} + \frac{\max(0.8, 0.6)}{3} + \frac{\max(1.0, 0.9)}{4} + \frac{\max(0.7, 1.0)}{5} + \frac{\max(0.3, 0.5)}{6} + \frac{\max(0.0, 0.2)}{7}$$
$$A \cup B = \frac{0.1}{1} + \frac{0.4}{2} + \frac{0.8}{3} + \frac{1.0}{4} + \frac{1.0}{5} + \frac{0.5}{6} + \frac{0.2}{7} \qquad \blacksquare$$

$$A \cap B = \frac{\min(0.1, 0.0)}{1} + \frac{\min(0.4, 0.2)}{2} + \frac{\min(0.8, 0.6)}{3} + \frac{\min(1.0, 0.9)}{4} + \frac{\min(0.7, 1.0)}{5} + \frac{\min(0.3, 0.5)}{6} + \frac{\min(0.0, 0.2)}{7}$$
$$A \cap B = \frac{0.0}{1} + \frac{0.2}{2} + \frac{0.6}{3} + \frac{0.9}{4} + \frac{0.7}{5} + \frac{0.3}{6} + \frac{0.0}{7} \qquad \blacksquare$$

---

### 3. Algebraic Product and Sum
- **Algebraic Product $A \cdot B$:** $\mu_{A \cdot B}(x) = \mu_A(x) \mu_B(x)$
  $$A \cdot B = \frac{0.0}{1} + \frac{0.08}{2} + \frac{0.48}{3} + \frac{0.90}{4} + \frac{0.70}{5} + \frac{0.15}{6} + \frac{0.0}{7} \qquad \blacksquare$$
- **Algebraic Sum $A \oplus B$:** $\mu_{A \oplus B}(x) = \mu_A(x) + \mu_B(x) - \mu_A(x)\mu_B(x)$
  - $x=1: 0.1 + 0.0 - 0.0 = 0.10$
  - $x=2: 0.4 + 0.2 - 0.08 = 0.52$
  - $x=3: 0.8 + 0.6 - 0.48 = 0.92$
  - $x=4: 1.0 + 0.9 - 0.90 = 1.00$
  - $x=5: 0.7 + 1.0 - 0.70 = 1.00$
  - $x=6: 0.3 + 0.5 - 0.15 = 0.65$
  - $x=7: 0.0 + 0.2 - 0.0 = 0.20$
  $$A \oplus B = \frac{0.10}{1} + \frac{0.52}{2} + \frac{0.92}{3} + \frac{1.00}{4} + \frac{1.00}{5} + \frac{0.65}{6} + \frac{0.20}{7} \qquad \blacksquare$$

---

### 4. Verification of Classical Laws
- **Law of Contradiction ($A \cap A^c = \emptyset$):**
  $$\mu_{A \cap A^c}(x) = \min(\mu_A(x), 1 - \mu_A(x))$$
  $$A \cap A^c = \frac{0.1}{1} + \frac{0.4}{2} + \frac{0.2}{3} + \frac{0.0}{4} + \frac{0.3}{5} + \frac{0.3}{6} + \frac{0.0}{7} \ne \emptyset$$
  Because $\mu_{A \cap A^c}(x) \ne 0$ for $x \in \{1, 2, 3, 5, 6\}$, **the Law of Contradiction FAILS**!
- **Law of Excluded Middle ($A \cup A^c = X$):**
  $$\mu_{A \cup A^c}(x) = \max(\mu_A(x), 1 - \mu_A(x))$$
  $$A \cup A^c = \frac{0.9}{1} + \frac{0.6}{2} + \frac{0.8}{3} + \frac{1.0}{4} + \frac{0.7}{5} + \frac{0.7}{6} + \frac{1.0}{7} \ne X$$
  Because $\mu_{A \cup A^c}(x) < 1$ for $x \in \{1, 2, 3, 5, 6\}$, **the Law of Excluded Middle FAILS**! $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 1.3: Rigorous Characterization of Fuzzy Convexity via Quasiconcavity",
                "statement": r"""Let $X = \mathbb{R}^n$ and let $A$ be a fuzzy set on $X$ with membership function $\mu_A: \mathbb{R}^n \to [0, 1]$.

1. Prove that $A$ is fuzzy convex if and only if for every finite convex combination $\sum_{i=1}^m \lambda_i x_i$ with $\sum_{i=1}^m \lambda_i = 1$ ($\lambda_i \ge 0$, $x_i \in \mathbb{R}^n$):
   $$\mu_A\left( \sum_{i=1}^m \lambda_i x_i \right) \ge \min_{1 \le i \le m} \mu_A(x_i)$$
2. Let $f: [0, 1] \to [0, 1]$ be a strictly increasing function. Prove that if $A$ is a fuzzy convex set, then the modified fuzzy set $B$ defined by $\mu_B(x) = f(\mu_A(x))$ is also fuzzy convex.
3. Show by counterexample that the union of two fuzzy convex sets is NOT necessarily fuzzy convex, but prove that the intersection of an arbitrary family of fuzzy convex sets $\{A_i\}_{i \in I}$ is always fuzzy convex.""",
                "hints": [
                    "For part 1, use mathematical induction on $m \\ge 2$.",
                    "For part 2, strictly increasing functions preserve the $\\min$ operator: $f(\\min(u, v)) = \\min(f(u), f(v))$.",
                    "For part 3, recall that the intersection of convex sets is convex, but union of disjoint intervals is disconnected."
                ],
                "solution": r"""### 1. Proof of General Convex Combination Property
We prove by mathematical induction on $m \ge 2$ that:
$$P(m): \mu_A\left( \sum_{i=1}^m \lambda_i x_i \right) \ge \min_{1 \le i \le m} \mu_A(x_i), \quad \text{where } \lambda_i \ge 0, \; \sum_{i=1}^m \lambda_i = 1$$

- **Base Case ($m = 2$):** By Definition 1.4 of fuzzy convexity:
  $$\mu_A(\lambda_1 x_1 + \lambda_2 x_2) = \mu_A(\lambda_1 x_1 + (1 - \lambda_1) x_2) \ge \min(\mu_A(x_1), \mu_A(x_2))$$
  Thus $P(2)$ holds.
- **Inductive Step:** Assume $P(k)$ holds for some $k \ge 2$. Consider $m = k + 1$ points $x_1, \dots, x_{k+1}$ with coefficients $\lambda_1, \dots, \lambda_{k+1} \ge 0$ summing to 1.
  If $\lambda_{k+1} = 1$, then all other $\lambda_i = 0$, and the inequality holds trivially.
  Assume $\lambda_{k+1} < 1$, so $1 - \lambda_{k+1} > 0$.
  Rewrite the convex combination:
  $$\sum_{i=1}^{k+1} \lambda_i x_i = (1 - \lambda_{k+1}) \left( \sum_{i=1}^k \frac{\lambda_i}{1 - \lambda_{k+1}} x_i \right) + \lambda_{k+1} x_{k+1}$$
  Let $y = \sum_{i=1}^k \frac{\lambda_i}{1 - \lambda_{k+1}} x_i$. The weights $\frac{\lambda_i}{1 - \lambda_{k+1}}$ are non-negative and sum to 1:
  $$\sum_{i=1}^k \frac{\lambda_i}{1 - \lambda_{k+1}} = \frac{1}{1 - \lambda_{k+1}} \sum_{i=1}^k \lambda_i = \frac{1 - \lambda_{k+1}}{1 - \lambda_{k+1}} = 1$$
  Applying the base case ($m = 2$) to $(1 - \lambda_{k+1}) y + \lambda_{k+1} x_{k+1}$:
  $$\mu_A\left( \sum_{i=1}^{k+1} \lambda_i x_i \right) \ge \min\left( \mu_A(y), \mu_A(x_{k+1}) \right)$$
  By the induction hypothesis $P(k)$, $\mu_A(y) \ge \min_{1 \le i \le k} \mu_A(x_i)$.
  Therefore:
  $$\mu_A\left( \sum_{i=1}^{k+1} \lambda_i x_i \right) \ge \min\left( \min_{1 \le i \le k} \mu_A(x_i), \mu_A(x_{k+1}) \right) = \min_{1 \le i \le k+1} \mu_A(x_i)$$
  Hence $P(k+1)$ holds, completing the induction. $\blacksquare$

---

### 2. Preservation under Monotonic Rescaling
Let $f: [0, 1] \to [0, 1]$ be strictly increasing.
Then for any $u, v \in [0, 1]$:
$$f(\min(u, v)) = \min(f(u), f(v))$$
Let $A$ be fuzzy convex, and $\mu_B(x) = f(\mu_A(x))$.
For any $x_1, x_2 \in \mathbb{R}^n$ and $\lambda \in [0, 1]$:
$$\begin{aligned}
\mu_B(\lambda x_1 + (1 - \lambda) x_2) &= f\left( \mu_A(\lambda x_1 + (1 - \lambda) x_2) \right) \\
&\ge f\left( \min(\mu_A(x_1), \mu_A(x_2)) \right) \quad (\text{since } f \text{ is non-decreasing}) \\
&= \min(f(\mu_A(x_1)), f(\mu_A(x_2))) \\
&= \min(\mu_B(x_1), \mu_B(x_2))
\end{aligned}$$
Thus $B$ is fuzzy convex. $\blacksquare$

---

### 3. Union Counterexample & Arbitrary Intersection Proof

#### Counterexample for Union:
Let $X = \mathbb{R}$. Define two triangular fuzzy sets:
- $A = \text{trimf}(x; 0, 1, 2)$
- $B = \text{trimf}(x; 4, 5, 6)$
Both $A$ and $B$ are individually fuzzy convex.
Consider their standard union $C = A \cup B$ with $\mu_C(x) = \max(\mu_A(x), \mu_B(x))$.
Evaluate at $x_1 = 1$ and $x_2 = 5$:
$\mu_C(1) = 1$, $\mu_C(5) = 1$.
Now consider the midpoint $x_{\text{mid}} = \frac{1}{2}(1) + \frac{1}{2}(5) = 3$:
$\mu_C(3) = \max(\mu_A(3), \mu_B(3)) = \max(0, 0) = 0$.
However:
$$\min(\mu_C(1), \mu_C(5)) = \min(1, 1) = 1$$
Since $\mu_C(3) = 0 < 1$, fuzzy convexity is violated! Hence the union is NOT fuzzy convex.

#### Proof for Arbitrary Intersection:
Let $\{A_i\}_{i \in I}$ be an arbitrary collection of fuzzy convex sets in $\mathbb{R}^n$.
Their standard intersection $D = \bigcap_{i \in I} A_i$ has membership function:
$$\mu_D(x) = \inf_{i \in I} \mu_{A_i}(x)$$
For any $x_1, x_2 \in \mathbb{R}^n$ and $\lambda \in [0, 1]$:
Since each $A_i$ is fuzzy convex:
$$\mu_{A_i}(\lambda x_1 + (1 - \lambda) x_2) \ge \min(\mu_{A_i}(x_1), \mu_{A_i}(x_2)) \quad (\forall i \in I)$$
Taking the infimum over all $i \in I$ on both sides:
$$\inf_{i \in I} \mu_{A_i}(\lambda x_1 + (1 - \lambda) x_2) \ge \inf_{i \in I} \min(\mu_{A_i}(x_1), \mu_{A_i}(x_2))$$
Since the infimum commutes with the minimum of two quantities:
$$\inf_{i \in I} \min(u_i, v_i) = \min\left( \inf_{i \in I} u_i, \inf_{i \in I} v_i \right)$$
we have:
$$\mu_D(\lambda x_1 + (1 - \lambda) x_2) \ge \min\left( \inf_{i \in I} \mu_{A_i}(x_1), \inf_{i \in I} \mu_{A_i}(x_2) \right) = \min(\mu_D(x_1), \mu_D(x_2))$$
This rigorously proves that the intersection of any arbitrary family of fuzzy convex sets is always fuzzy convex! $\blacksquare$"""
            }
        ]
    }
    return u1

if __name__ == "__main__":
    u1 = get_unit1()
    print(f"Loaded Unit 1: {u1['title']} with {len(u1['sections'])} sections and {len(u1['problems'])} problems.")
