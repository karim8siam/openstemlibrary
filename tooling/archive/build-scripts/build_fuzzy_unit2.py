# -*- coding: utf-8 -*-
"""
build_fuzzy_unit2.py
Constructs Unit 2: Operations on Fuzzy Sets: Complements, Unions & Intersections
Strictly ZERO course numbers.
"""

def get_unit2():
    u2 = {
        "number": 2,
        "title": "Operations on Fuzzy Sets: Complements, Unions & Intersections",
        "leadSummary": "Comprehensive mathematical axiomatics of fuzzy set operations: classical Zadeh operators (min, max, 1-c), the axiomatic foundation of fuzzy complements (monotonicity, boundary conditions, continuous involutions, equilibrium points c(e) = e), triangular norms (t-norms) for intersection (minimum, algebraic product, bounded difference, drastic product, Hamacher, Frank, Schweizer-Sklar families), triangular conorms (s-norms) for union, generalized De Morgan duality, and compensatory averaging operators including ordered weighted averaging (OWA).",
        "simulations": ["sim_fuzzy_set_operations"],
        "sections": [
            {
                "secNumber": "2.1",
                "title": "Standard Zadeh Operators (Min, Max, Standard Inversion) & De Morgan's Laws",
                "content": r"""### 1. Zadeh's Original Set Theoretic Operations
In 1965, Lotfi A. Zadeh defined the elementary operations on fuzzy sets $A$ and $B$ in universe $X$ point-by-point through their membership functions:

> **Definition 2.1 (Standard Fuzzy Operations):**
> For all $x \in X$:
> 1. **Fuzzy Complement ($A^c$):**
>    $$\mu_{A^c}(x) = 1 - \mu_A(x)$$
> 2. **Fuzzy Intersection ($A \cap B$):**
>    $$\mu_{A \cap B}(x) = \min(\mu_A(x), \mu_B(x)) = \mu_A(x) \wedge \mu_B(x)$$
> 3. **Fuzzy Union ($A \cup B$):**
>    $$\mu_{A \cup B}(x) = \max(\mu_A(x), \mu_B(x)) = \mu_A(x) \vee \mu_B(x)$$
> 4. **Fuzzy Inclusion ($A \subseteq B$):**
>    $$A \subseteq B \iff \mu_A(x) \le \mu_B(x) \quad (\forall x \in X)$$

---

### 2. Preservation of Algebraic Lattice Properties
Under standard operations $(\min, \max, 1 - \cdot)$, the set of all fuzzy subsets $\mathcal{F}(X)$ forms a **distributive, bounded pseudo-complemented lattice** (a de Morgan algebra / Kleene algebra).

#### Satisfied Properties ($\forall A, B, C \in \mathcal{F}(X)$):
1. **Involution (Double Negation):** $(A^c)^c = A$
2. **Idempotence:** $A \cup A = A$, and $A \cap A = A$
3. **Commutativity:** $A \cup B = B \cup A$, and $A \cap B = B \cap A$
4. **Associativity:** $(A \cup B) \cup C = A \cup (B \cup C)$, and $(A \cap B) \cap C = A \cap (B \cap C)$
5. **Absorption:** $A \cup (A \cap B) = A$, and $A \cap (A \cup B) = A$
6. **Distributivity:**
   $$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$$
   $$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$$
7. **Identity Elements:** $A \cup \emptyset = A$, and $A \cap X = A$

---

### 3. De Morgan's Laws for Fuzzy Sets

> **Theorem 2.1 (De Morgan's Laws):**
> For any fuzzy sets $A, B \in \mathcal{F}(X)$:
> $$(A \cup B)^c = A^c \cap B^c$$
> $$(A \cap B)^c = A^c \cup B^c$$

#### Proof:
For any $x \in X$, let $a = \mu_A(x)$ and $b = \mu_B(x)$.
For the first identity:
$$\mu_{(A \cup B)^c}(x) = 1 - \mu_{A \cup B}(x) = 1 - \max(a, b)$$
Notice that if $a \ge b$, then $\max(a, b) = a$, so $1 - \max(a, b) = 1 - a$.
At the same time, $1 - a \le 1 - b$, so $\min(1 - a, 1 - b) = 1 - a$.
In general, for any two real numbers $a, b$:
$$1 - \max(a, b) = \min(1 - a, 1 - b)$$
Therefore:
$$\mu_{(A \cup B)^c}(x) = \min(1 - \mu_A(x), 1 - \mu_B(x)) = \min(\mu_{A^c}(x), \mu_{B^c}(x)) = \mu_{A^c \cap B^c}(x)$$
Since this holds for all $x \in X$, $(A \cup B)^c = A^c \cap B^c$.
The second identity follows symmetrically from $1 - \min(a, b) = \max(1 - a, 1 - b)$. $\blacksquare$"""
            },
            {
                "secNumber": "2.2",
                "title": "Axiomatic Skeleton of Fuzzy Complements: Involution, Monotonicity & Equilibrium Points",
                "content": r"""### 1. General Axioms of Fuzzy Complements
Why must a complement be $1 - a$? In 1980, mathematicians generalized the notion of complementation by defining an axiomatic system for mapping $c: [0, 1] \to [0, 1]$.

> **Definition 2.2 (Axiomatic Fuzzy Complement):**
> A function $c: [0, 1] \to [0, 1]$ is a **fuzzy complement** if it satisfies the following two axiomatic requirements:
> - **Axiom C1 (Boundary Conditions):** $c(0) = 1$ and $c(1) = 0$.
> - **Axiom C2 (Monotonicity):** For all $a, b \in [0, 1]$, if $a \le b$, then $c(a) \ge c(b)$ (strictly non-increasing).
>
> A complement is called **involutive** if it satisfies:
> - **Axiom C3 (Involution):** $c(c(a)) = a$ for all $a \in [0, 1]$.
> - **Axiom C4 (Continuity):** $c$ is a continuous function.

*(Theorem: Any involutive complement satisfying C1-C2 is strictly decreasing and continuous!)*

---

### 2. Parameterized Families of Fuzzy Complements

#### 1. Sugeno's Complement Family:
For parameter $\lambda \in (-1, \infty)$:
$$c_\lambda(a) = \frac{1 - a}{1 + \lambda a}$$
- When $\lambda = 0$: $c_0(a) = 1 - a$ (Zadeh's standard complement).
- When $\lambda \to \infty$: $c_\infty(a) \to 0$ for all $a > 0$.
- When $\lambda \to -1$: $c_{-1}(a) \to 1$ for all $a < 1$.

#### 2. Yager's Complement Family:
For parameter $w \in (0, \infty)$:
$$c_w(a) = \left( 1 - a^w \right)^{1/w}$$
- When $w = 1$: $c_1(a) = 1 - a$ (standard complement).
- Every member of Yager's family is strictly involutive: $c_w(c_w(a)) = (1 - (1 - a^w))^{1/w} = a$.

---

### 3. Equilibrium Points

> **Definition 2.3 (Equilibrium Point):**
> An **equilibrium point** of a fuzzy complement $c$ is a value $e \in [0, 1]$ that is its own complement:
> $$c(e) = e$$

> **Theorem 2.2 (Existence and Uniqueness of Equilibrium):**
> Every continuous fuzzy complement $c$ possesses a **unique** equilibrium point $e \in (0, 1)$.

#### Proof:
Define the auxiliary function $g(a) = c(a) - a$ on the domain $[0, 1]$.
1. At $a = 0$: $g(0) = c(0) - 0 = 1 - 0 = 1 > 0$.
2. At $a = 1$: $g(1) = c(1) - 1 = 0 - 1 = -1 < 0$.
3. Since $c$ is continuous, $g$ is continuous on $[0, 1]$.
By the Intermediate Value Theorem, there exists at least one $e \in (0, 1)$ such that $g(e) = 0 \implies c(e) = e$.
Because $c$ is strictly decreasing, $g(a) = c(a) - a$ is strictly decreasing, so the root $e$ is **strictly unique**! $\blacksquare$

- For Zadeh's complement $c(a) = 1 - a$: $1 - e = e \implies e = 0.5$.
- For Sugeno's complement: $\frac{1 - e}{1 + \lambda e} = e \implies \lambda e^2 + 2e - 1 = 0 \implies e = \frac{\sqrt{1 + \lambda} - 1}{\lambda}$."""
            },
            {
                "secNumber": "2.3",
                "title": "Triangular Norms (t-Norms): Product, Łukasiewicz, Drastic, Hamacher & Frank Families",
                "content": r"""### 1. The Axiomatization of Fuzzy Intersections
The concept of a **triangular norm** ($t$-norm) was introduced by Karl Menger (1942) in the study of probabilistic metric spaces and later adopted by Schweizer and Sklar to generalize fuzzy intersections.

> **Definition 2.4 (Triangular Norm / t-Norm):**
> A binary operator $i: [0, 1] \times [0, 1] \to [0, 1]$ (often denoted $T(a, b)$ or $a \top b$) is a **t-norm** if it satisfies for all $a, b, c, d \in [0, 1]$:
> 1. **Boundary Condition:** $T(a, 1) = a$ (1 is the neutral identity element).
> 2. **Monotonicity:** If $a \le c$ and $b \le d$, then $T(a, b) \le T(c, d)$.
> 3. **Commutativity:** $T(a, b) = T(b, a)$.
> 4. **Associativity:** $T(T(a, b), c) = T(a, T(b, c))$.

Note: From boundary and monotonicity: $T(a, 0) \le T(1, 0) = T(0, 1) = 0 \implies T(a, 0) = 0$.

---

### 2. The Four Fundamental Archetypal t-Norms

#### 1. Minimum (Standard Zadeh Intersection):
$$T_{\min}(a, b) = \min(a, b)$$
This is the **largest possible t-norm**: for any t-norm $T$, $T(a, b) \le \min(a, b)$.
It is the unique idempotent t-norm: $T(a, a) = a \iff T = T_{\min}$.

#### 2. Algebraic Product:
$$T_{\text{prod}}(a, b) = a \cdot b$$
Strictly positive for all $a, b > 0$.

#### 3. Bounded Difference (Łukasiewicz t-Norm):
$$T_{\text{Luk}}(a, b) = \max(0, a + b - 1)$$
Nilpotent t-norm: $T(a, b) = 0$ can occur even when $a > 0$ and $b > 0$.

#### 4. Drastic Product:
$$T_D(a, b) = \begin{cases} a, & b = 1 \\ b, & a = 1 \\ 0, & \text{otherwise} \end{cases}$$
This is the **smallest possible t-norm**: for any t-norm $T$, $T_D(a, b) \le T(a, b)$.

---

### 3. Universal Ordering Chain of Archetypal t-Norms

> **Theorem 2.3 (Ordering of Fundamental t-Norms):**
> For all $a, b \in [0, 1]$:
> $$T_D(a, b) \le T_{\text{Luk}}(a, b) \le T_{\text{prod}}(a, b) \le T_{\min}(a, b)$$

#### Proof:
1. $T_D \le T$ is immediate from Definition 2.4.
2. For $T_{\text{Luk}} \le T_{\text{prod}}$:
   Notice that $(1 - a)(1 - b) \ge 0 \implies 1 - a - b + ab \ge 0 \implies ab \ge a + b - 1$.
   Since $ab \ge 0$, we have $ab \ge \max(0, a + b - 1) = T_{\text{Luk}}(a, b)$.
3. For $T_{\text{prod}} \le T_{\min}$:
   Since $b \le 1$, $ab \le a$. Since $a \le 1$, $ab \le b$.
   Thus $ab \le \min(a, b) = T_{\min}(a, b)$. $\blacksquare$"""
            },
            {
                "secNumber": "2.4",
                "title": "Triangular Conorms (t-Conorms / s-Norms): Algebraic Sum, Bounded Sum, Drastic Sum",
                "content": r"""### 1. The Axiomatization of Fuzzy Unions
The dual operation to a $t$-norm is a **triangular conorm** ($t$-conorm or $s$-norm).

> **Definition 2.5 (Triangular Conorm / s-Norm):**
> A binary operator $u: [0, 1] \times [0, 1] \to [0, 1]$ (denoted $S(a, b)$ or $a \bot b$) is an **s-norm** if it satisfies for all $a, b, c, d \in [0, 1]$:
> 1. **Boundary Condition:** $S(a, 0) = a$ (0 is the neutral identity element).
> 2. **Monotonicity:** If $a \le c$ and $b \le d$, then $S(a, b) \le S(c, d)$.
> 3. **Commutativity:** $S(a, b) = S(b, a)$.
> 4. **Associativity:** $S(S(a, b), c) = S(a, S(b, c))$.

Note: $S(a, 1) = 1$ for all $a \in [0, 1]$.

---

### 2. The Four Fundamental Archetypal s-Norms

#### 1. Maximum (Standard Zadeh Union):
$$S_{\max}(a, b) = \max(a, b)$$
This is the **smallest possible s-norm**: for any s-norm $S$, $\max(a, b) \le S(a, b)$.
It is the unique idempotent s-norm: $S(a, a) = a \iff S = S_{\max}$.

#### 2. Algebraic Sum (Probabilistic Sum):
$$S_{\text{sum}}(a, b) = a + b - ab$$

#### 3. Bounded Sum (Łukasiewicz s-Norm):
$$S_{\text{Luk}}(a, b) = \min(1, a + b)$$

#### 4. Drastic Sum:
$$S_D(a, b) = \begin{cases} a, & b = 0 \\ b, & a = 0 \\ 1, & \text{otherwise} \end{cases}$$
This is the **largest possible s-norm**: for any s-norm $S$, $S(a, b) \le S_D(a, b)$.

---

### 3. Generalized De Morgan Duality

> **Theorem 2.4 (Duality Theorem):**
> Let $c$ be an involutive fuzzy complement. For every t-norm $T$, the dual operator defined by:
> $$S(a, b) = c\left( T(c(a), c(b)) \right)$$
> is an s-norm. Conversely, for every s-norm $S$:
> $$T(a, b) = c\left( S(c(a), c(b)) \right)$$
> is a t-norm. The pair $(T, S, c)$ satisfies generalized De Morgan's laws.

#### Universal Ordering Chain of Archetypal s-Norms:
$$S_{\max}(a, b) \le S_{\text{sum}}(a, b) \le S_{\text{Luk}}(a, b) \le S_D(a, b)$$"""
            },
            {
                "secNumber": "2.5",
                "title": "Averaging Operators, Generalized Means & Ordered Weighted Averaging (OWA)",
                "content": r"""### 1. The Spectrum Between Intersection and Union
Notice the strict bounds governing norm operations:
$$T(a, b) \le \min(a, b) \le \max(a, b) \le S(a, b)$$
$t$-norms represent strict conjunction ("AND"), while $s$-norms represent full disjunction ("OR").
However, human decision-making frequently requires **compensatory aggregation** (a trade-off where a high score in one criterion compensates for a lower score in another).
This motivates **averaging operators** $M(a, b)$ that lie strictly between min and max:
$$\min(a, b) \le M(a, b) \le \max(a, b)$$

---

### 2. Generalized Means (Power Means)
For elements $a_1, a_2, \dots, a_n \in [0, 1]$ and weights $w_i \ge 0$ with $\sum w_i = 1$:
$$M_p(a; w) = \left( \sum_{i=1}^n w_i a_i^p \right)^{1/p}, \qquad p \in \mathbb{R} \setminus \{0\}$$
- $p \to -\infty$: $M_{-\infty} = \min(a_1, \dots, a_n)$ (pure intersection).
- $p = -1$: Harmonic Mean $M_{-1} = \frac{1}{\sum \frac{w_i}{a_i}}$.
- $p \to 0$: Geometric Mean $M_0 = \prod_{i=1}^n a_i^{w_i}$.
- $p = 1$: Arithmetic Mean $M_1 = \sum_{i=1}^n w_i a_i$.
- $p = 2$: Quadratic (RMS) Mean $M_2 = \sqrt{\sum w_i a_i^2}$.
- $p \to +\infty$: $M_{+\infty} = \max(a_1, \dots, a_n)$ (pure union).

---

### 3. Ordered Weighted Averaging (OWA) Operators
Introduced by Ronald R. Yager (1988), the **OWA operator** decouples weights from individual criteria and associates them with *magnitudes*:

> **Definition 2.6 (OWA Operator):**
> An OWA operator of dimension $n$ is a mapping $F_w: [0, 1]^n \to [0, 1]$ associated with weighting vector $w = (w_1, \dots, w_n)$ where $w_i \in [0, 1]$ and $\sum w_i = 1$:
> $$F_w(a_1, \dots, a_n) = \sum_{j=1}^n w_j b_j$$
> where $b_j$ is the **$j$-th largest element** of the collection $\{a_1, \dots, a_n\}$ ($b_1 \ge b_2 \ge \dots \ge b_n$).

#### Extreme Cases:
- $w = (1, 0, \dots, 0) \implies F_w(a) = b_1 = \max(a_i)$ (Pure OR).
- $w = (0, 0, \dots, 1) \implies F_w(a) = b_n = \min(a_i)$ (Pure AND).
- $w = (1/n, 1/n, \dots, 1/n) \implies F_w(a) = \frac{1}{n} \sum a_i$ (Standard Arithmetic Mean).

The degree of "orness" of an OWA operator is measured by:
$$\text{orness}(w) = \frac{1}{n - 1} \sum_{j=1}^n (n - j) w_j \in [0, 1]$$
- $\text{orness} = 1$ for Max; $\text{orness} = 0$ for Min; $\text{orness} = 0.5$ for Arithmetic Mean."""
            }
        ],
        "problems": [
            {
                "tier": "Fundamentals",
                "title": "Problem 2.1: Comparison of t-Norms and s-Norms for Specific Truth Grades",
                "statement": r"""Let two fuzzy propositions have truth values $a = 0.7$ and $b = 0.4$.
1. Compute their intersection using the four fundamental t-norms:
   - Minimum $T_{\min}(a, b)$
   - Algebraic Product $T_{\text{prod}}(a, b)$
   - Łukasiewicz Bounded Difference $T_{\text{Luk}}(a, b)$
   - Drastic Product $T_D(a, b)$
   and verify the ordering chain $T_D \le T_{\text{Luk}} \le T_{\text{prod}} \le T_{\min}$.
2. Compute their union using the four fundamental s-norms:
   - Maximum $S_{\max}(a, b)$
   - Algebraic Sum $S_{\text{sum}}(a, b)$
   - Łukasiewicz Bounded Sum $S_{\text{Luk}}(a, b)$
   - Drastic Sum $S_D(a, b)$
   and verify the ordering chain $S_{\max} \le S_{\text{sum}} \le S_{\text{Luk}} \le S_D$.
3. Compute the standard Yager complement with parameter $w = 2$ for $a = 0.7$.""",
                "hints": [
                    "Recall $T_{\\text{Luk}}(a, b) = \\max(0, a + b - 1)$.",
                    "Recall $S_{\\text{sum}}(a, b) = a + b - ab$.",
                    "Yager complement: $c_w(a) = (1 - a^w)^{1/w}$."
                ],
                "solution": r"""### 1. Calculation of t-Norms ($a = 0.7, b = 0.4$)
1. **Minimum:**
   $$T_{\min}(0.7, 0.4) = \min(0.7, 0.4) = 0.40$$
2. **Algebraic Product:**
   $$T_{\text{prod}}(0.7, 0.4) = 0.7 \times 0.4 = 0.28$$
3. **Łukasiewicz Bounded Difference:**
   $$T_{\text{Luk}}(0.7, 0.4) = \max(0, 0.7 + 0.4 - 1) = \max(0, 0.10) = 0.10$$
4. **Drastic Product:**
   Since neither $a = 1$ nor $b = 1$:
   $$T_D(0.7, 0.4) = 0.00$$

#### Verification of Ordering:
$$0.00 \le 0.10 \le 0.28 \le 0.40 \iff T_D \le T_{\text{Luk}} \le T_{\text{prod}} \le T_{\min}$$
Holds with strict inequalities! $\blacksquare$

---

### 2. Calculation of s-Norms ($a = 0.7, b = 0.4$)
1. **Maximum:**
   $$S_{\max}(0.7, 0.4) = \max(0.7, 0.4) = 0.70$$
2. **Algebraic Sum:**
   $$S_{\text{sum}}(0.7, 0.4) = 0.7 + 0.4 - (0.7)(0.4) = 1.10 - 0.28 = 0.82$$
3. **Łukasiewicz Bounded Sum:**
   $$S_{\text{Luk}}(0.7, 0.4) = \min(1, 0.7 + 0.4) = \min(1, 1.10) = 1.00$$
4. **Drastic Sum:**
   Since neither $a = 0$ nor $b = 0$:
   $$S_D(0.7, 0.4) = 1.00$$

#### Verification of Ordering:
$$0.70 \le 0.82 \le 1.00 \le 1.00 \iff S_{\max} \le S_{\text{sum}} \le S_{\text{Luk}} \le S_D$$
Holds identically! $\blacksquare$

---

### 3. Yager Complement for $w = 2, a = 0.7$
$$c_2(0.7) = \left( 1 - 0.7^2 \right)^{1/2} = \sqrt{1 - 0.49} = \sqrt{0.51} \approx 0.7141 \qquad \blacksquare$$"""
            },
            {
                "tier": "Computational Triad",
                "title": "Problem 2.2: Equilibrium Points of Sugeno and Yager Complements",
                "statement": r"""An equilibrium point $e \in [0, 1]$ of a fuzzy complement satisfies $c(e) = e$.
1. For the Sugeno complement $c_\lambda(a) = \frac{1 - a}{1 + \lambda a}$ with parameter $\lambda \in (-1, \infty)$:
   - Show that the equilibrium point is given by $e_\lambda = \frac{\sqrt{1 + \lambda} - 1}{\lambda}$ for $\lambda \ne 0$.
   - Evaluate $\lim_{\lambda \to 0} e_\lambda$ and show it matches Zadeh's standard equilibrium point $0.5$.
   - Calculate $e_\lambda$ for $\lambda = 3$ and $\lambda = -0.75$.
2. For the Yager complement $c_w(a) = (1 - a^w)^{1/w}$ with parameter $w \in (0, \infty)$:
   - Find the exact analytical expression for the equilibrium point $e_w$.
   - Evaluate $e_w$ for $w = 1, 2, 3$.""",
                "hints": [
                    "Set $c(e) = e$ and solve the quadratic $\\lambda e^2 + 2e - 1 = 0$.",
                    "Use L'Hopital's rule or binomial expansion for the limit $\\lambda \\to 0$.",
                    "For Yager, solve $(1 - e^w)^{1/w} = e \\implies 1 - e^w = e^w$."
                ],
                "solution": r"""### 1. Sugeno Complement Equilibrium Point

#### Step A: Quadratic Derivation
Set $c_\lambda(e) = e$:
$$\frac{1 - e}{1 + \lambda e} = e \implies 1 - e = e(1 + \lambda e) \implies 1 - e = e + \lambda e^2$$
Rearranging into standard quadratic form:
$$\lambda e^2 + 2e - 1 = 0$$
Using the quadratic formula (for $\lambda \ne 0$):
$$e = \frac{-2 \pm \sqrt{4 - 4(\lambda)(-1)}}{2\lambda} = \frac{-2 \pm \sqrt{4 + 4\lambda}}{2\lambda} = \frac{-1 \pm \sqrt{1 + \lambda}}{\lambda}$$
Since $\lambda > -1$, $\sqrt{1 + \lambda} > 0$.
To ensure $e \in [0, 1]$, we take the positive root:
$$e_\lambda = \frac{\sqrt{1 + \lambda} - 1}{\lambda} \qquad \blacksquare$$

#### Step B: Limit as $\lambda \to 0$
Using rationalization:
$$e_\lambda = \frac{(\sqrt{1 + \lambda} - 1)(\sqrt{1 + \lambda} + 1)}{\lambda (\sqrt{1 + \lambda} + 1)} = \frac{(1 + \lambda) - 1}{\lambda (\sqrt{1 + \lambda} + 1)} = \frac{\lambda}{\lambda (\sqrt{1 + \lambda} + 1)} = \frac{1}{\sqrt{1 + \lambda} + 1}$$
Taking the limit as $\lambda \to 0$:
$$\lim_{\lambda \to 0} e_\lambda = \frac{1}{\sqrt{1 + 0} + 1} = \frac{1}{1 + 1} = \frac{1}{2} = 0.5 \qquad \blacksquare$$

#### Step C: Specific Evaluations
- For $\lambda = 3$:
  $$e_3 = \frac{\sqrt{1 + 3} - 1}{3} = \frac{2 - 1}{3} = \frac{1}{3} \approx 0.3333$$
- For $\lambda = -0.75$:
  $$e_{-0.75} = \frac{\sqrt{1 - 0.75} - 1}{-0.75} = \frac{\sqrt{0.25} - 1}{-0.75} = \frac{0.5 - 1}{-0.75} = \frac{-0.5}{-0.75} = \frac{2}{3} \approx 0.6667 \qquad \blacksquare$$

---

### 2. Yager Complement Equilibrium Point
Set $c_w(e) = e$:
$$\left( 1 - e^w \right)^{1/w} = e$$
Raise both sides to power $w$:
$$1 - e^w = e^w \implies 2e^w = 1 \implies e^w = \frac{1}{2}$$
Taking the $w$-th root:
$$e_w = \left(\frac{1}{2}\right)^{1/w} = 2^{-1/w} \qquad \blacksquare$$

#### Evaluations:
- For $w = 1$:
  $$e_1 = 2^{-1} = 0.5$$
- For $w = 2$:
  $$e_2 = 2^{-1/2} = \frac{1}{\sqrt{2}} \approx 0.7071$$
- For $w = 3$:
  $$e_3 = 2^{-1/3} \approx 0.7937 \qquad \blacksquare$$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 2.3: Uniqueness of Min/Max via Idempotence and OWA Optimization",
                "statement": r"""1. Prove that the minimum operator $T_{\min}(a, b) = \min(a, b)$ is the **ONLY** idempotent t-norm:
   $$\forall a \in [0, 1], \; T(a, a) = a \iff T(a, b) = \min(a, b)$$
2. Let $F_w(a_1, \dots, a_n) = \sum_{j=1}^n w_j b_j$ be an OWA operator with inputs $a = (0.9, 0.4, 0.8, 0.2)$.
   - Evaluate $F_w$ with weights $w = (0.4, 0.3, 0.2, 0.1)$.
   - Compute the degree of orness: $\text{orness}(w) = \frac{1}{n-1} \sum_{j=1}^n (n-j) w_j$.
   - Compute the dispersion (entropy) of the weights: $H(w) = -\sum_{j=1}^n w_j \ln w_j$.
3. Show that as $\text{orness}(w) \to 1$, $H(w) \to 0$.""",
                "hints": [
                    "For part 1, use monotonicity: if $a \\le b$, then $T(a, a) \\le T(a, b) \\le T(a, 1)$.",
                    "For part 2, first sort the inputs in descending order: $b = (0.9, 0.8, 0.4, 0.2)$.",
                    "For part 3, examine the weight vector $(1, 0, 0, 0)$."
                ],
                "solution": r"""### 1. Proof of the Uniqueness of $T_{\min}$ via Idempotence

#### Step A: Verification that $\min$ is Idempotent
$\min(a, a) = a$ holds trivially for all $a \in [0, 1]$.

#### Step B: Uniqueness Proof
Assume $T$ is an arbitrary t-norm satisfying the idempotence axiom:
$$T(x, x) = x \quad (\forall x \in [0, 1])$$
Let $a, b \in [0, 1]$. Without loss of generality, assume $a \le b$.
Then $\min(a, b) = a$.
Now use the axioms of t-norms:
1. By monotonicity (Axiom 2), since $a \le b$:
   $$T(a, a) \le T(a, b)$$
   By idempotence, $T(a, a) = a$, so:
   $$a \le T(a, b)$$
2. On the other hand, since $b \le 1$, by monotonicity:
   $$T(a, b) \le T(a, 1)$$
   By the boundary condition (Axiom 1), $T(a, 1) = a$, so:
   $$T(a, b) \le a$$
Combining (1) and (2):
$$a \le T(a, b) \le a \implies T(a, b) = a = \min(a, b)$$
If $b \le a$, by commutativity $T(a, b) = T(b, a) = b = \min(a, b)$.
Therefore, $T(a, b) = \min(a, b)$ for all $a, b \in [0, 1]$.
$T_{\min}$ is the **unique** idempotent t-norm! $\blacksquare$

---

### 2. OWA Operator Calculations
Inputs: $a = (0.9, 0.4, 0.8, 0.2)$.
Dimension $n = 4$.
Weights: $w = (0.4, 0.3, 0.2, 0.1)$.

#### Step A: Sort in Descending Order
$$b_1 = 0.9, \quad b_2 = 0.8, \quad b_3 = 0.4, \quad b_4 = 0.2$$
$$b = (0.9, 0.8, 0.4, 0.2)$$

#### Step B: Evaluate OWA Aggregation
$$\begin{aligned}
F_w(a) &= w_1 b_1 + w_2 b_2 + w_3 b_3 + w_4 b_4 \\
&= (0.4)(0.9) + (0.3)(0.8) + (0.2)(0.4) + (0.1)(0.2) \\
&= 0.36 + 0.24 + 0.08 + 0.02 \\
&= 0.70 \qquad \blacksquare
\end{aligned}$$

#### Step C: Degree of Orness
With $n = 4$:
$$\begin{aligned}
\text{orness}(w) &= \frac{1}{4 - 1} \sum_{j=1}^4 (4 - j) w_j \\
&= \frac{1}{3} \left[ 3 w_1 + 2 w_2 + 1 w_3 + 0 w_4 \right] \\
&= \frac{1}{3} \left[ 3(0.4) + 2(0.3) + 1(0.2) + 0(0.1) \right] \\
&= \frac{1}{3} \left[ 1.2 + 0.6 + 0.2 + 0 \right] = \frac{2.0}{3} \approx 0.6667 \qquad \blacksquare
\end{aligned}$$

#### Step D: Dispersion (Entropy)
$$H(w) = -\sum_{j=1}^4 w_j \ln w_j$$
- $w_1 = 0.4 \implies 0.4 \ln(0.4) \approx 0.4(-0.9163) = -0.3665$
- $w_2 = 0.3 \implies 0.3 \ln(0.3) \approx 0.3(-1.2040) = -0.3612$
- $w_3 = 0.2 \implies 0.2 \ln(0.2) \approx 0.2(-1.6094) = -0.3219$
- $w_4 = 0.1 \implies 0.1 \ln(0.1) \approx 0.1(-2.3026) = -0.2303$
Sum:
$$H(w) = -(-0.3665 - 0.3612 - 0.3219 - 0.2303) = 1.2799 \text{ nats} \qquad \blacksquare$$

---

### 3. Asymptotic Behavior as $\text{orness} \to 1$
When $\text{orness}(w) = 1$, all weight is concentrated on the first component:
$$w^* = (1, 0, \dots, 0)$$
Then:
$$H(w^*) = -1 \ln(1) - \lim_{p \to 0^+} \sum_{j=2}^n p \ln p = 0 - 0 = 0$$
This demonstrates that pure disjunction (Max) has zero entropy, representing maximum certainty of relying strictly on the best score, whereas equal weights $w = (1/n, \dots, 1/n)$ achieve maximum entropy $\ln n$ with neutral $\text{orness} = 0.5$. $\blacksquare$"""
            }
        ]
    }
    return u2

if __name__ == "__main__":
    u2 = get_unit2()
    print(f"Loaded Unit 2: {u2['title']} with {len(u2['sections'])} sections and {len(u2['problems'])} problems.")
