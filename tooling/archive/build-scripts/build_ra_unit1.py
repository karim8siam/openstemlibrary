# -*- coding: utf-8 -*-
"""
build_ra_unit1.py
Constructs Unit 1: The Real Field: Completeness, Supremum Principle & Dedekind Cuts
"""

def get_unit1():
    u1 = {
        "number": 1,
        "title": "The Real Field: Completeness, Supremum Principle & Dedekind Cuts",
        "leadSummary": "Axiomatic foundations of the real number system: ordered field axioms, least upper bound property, Dedekind cut construction of R, the Archimedean property, denseness of rational and irrational numbers, and Cantor's cardinality and uncountability theorems.",
        "simulations": ["sim_ra_dedekind_completeness"],
        "sections": [
            {
                "secNumber": "1.1",
                "title": "Axiomatic Foundation of Real Numbers: Ordered Field Axioms & Inequalities",
                "content": r"""### 1. The Need for an Axiomatic Real Number System

Elementary calculus relies heavily on geometric intuition about the "real line." However, intuition fails in delicate limiting arguments, where pathological sets or functions defy visual reasoning. Mathematical analysis demands an unambiguous, purely axiomatic construction of the real number continuum $\mathbb{R}$.

Historically, the rational numbers $\mathbb{Q}$ proved inadequate. The ancient Pythagoreans discovered that the hypotenuse of a right isosceles triangle with legs of unit length cannot be expressed as a ratio of integers: $\sqrt{2} \notin \mathbb{Q}$. In modern analytical terms, the set
$$S = \{ x \in \mathbb{Q} : x > 0 \text{ and } x^2 < 2 \}$$
is bounded above in $\mathbb{Q}$, but possesses no supremum within $\mathbb{Q}$. The continuum has "punctures" or "holes." Analysis bridges these gaps by completing $\mathbb{Q}$ into the complete ordered field $\mathbb{R}$.

---

### 2. Field Axioms and Order Axioms

> **Definition 1.1 (Field Axioms):**
> A set $F$ endowed with two binary operations, addition $(+)$ and multiplication $(\cdot)$, is a **field** if it satisfies the following nine axioms for all $x, y, z \in F$:
> 1. **Closure:** $x + y \in F$ and $x \cdot y \in F$.
> 2. **Commutativity:** $x + y = y + x$ and $x \cdot y = y \cdot x$.
> 3. **Associativity:** $(x + y) + z = x + (y + z)$ and $(x \cdot y) \cdot z = x \cdot (y \cdot z)$.
> 4. **Distributivity:** $x \cdot (y + z) = (x \cdot y) + (x \cdot z)$.
> 5. **Additive Identity:** There exists a unique element $0 \in F$ such that $x + 0 = x$.
> 6. **Multiplicative Identity:** There exists a unique element $1 \in F$ ($1 \ne 0$) such that $x \cdot 1 = x$.
> 7. **Additive Inverses:** For every $x \in F$, there exists a unique $-x \in F$ such that $x + (-x) = 0$.
> 8. **Multiplicative Inverses:** For every $x \in F \setminus \{0\}$, there exists a unique $x^{-1} = \frac{1}{x} \in F$ such that $x \cdot x^{-1} = 1$.

> **Definition 1.2 (Ordered Field):**
> A field $F$ is an **ordered field** if there exists a strict linear order relation $<$ on $F$ satisfying:
> 1. **Trichotomy:** For any $x, y \in F$, exactly one of the following holds:
>    $$x < y, \quad x = y, \quad \text{or} \quad y < x$$
> 2. **Transitivity:** If $x < y$ and $y < z$, then $x < z$.
> 3. **Compatibility with Addition:** If $x < y$, then $x + z < y + z$ for all $z \in F$.
> 4. **Compatibility with Multiplication:** If $x < y$ and $0 < z$, then $x \cdot z < y \cdot z$.

Both $\mathbb{Q}$ and $\mathbb{R}$ satisfy all field and order axioms. Hence, algebraic and order axioms alone cannot distinguish $\mathbb{R}$ from $\mathbb{Q}$. The definitive distinguishing property is the **Completeness Axiom**.

---

### 3. Fundamental Algebraic Inequalities

> **Definition 1.3 (Absolute Value):**
> For any element $x$ in an ordered field $F$, the **absolute value** $|x|$ is defined as:
> $$|x| = \begin{cases} x & \text{if } x \ge 0 \\ -x & \text{if } x < 0 \end{cases}$$

> **Theorem 1.1 (Properties of Absolute Value & The Triangle Inequality):**
> For all $x, y \in \mathbb{R}$:
> 1. $|x| \ge 0$, and $|x| = 0 \iff x = 0$.
> 2. $|x \cdot y| = |x| \cdot |y|$.
> 3. $-|x| \le x \le |x|$.
> 4. **Triangle Inequality:** $|x + y| \le |x| + |y|$.
> 5. **Reverse Triangle Inequality:** $||x| - |y|| \le |x - y|$.

#### Rigorous Proof of the Triangle Inequality:
From property 3, we have:
$$-|x| \le x \le |x| \quad \text{and} \quad -|y| \le y \le |y|$$
Adding these two ordered inequalities via compatibility with addition:
$$-(|x| + |y|) \le x + y \le (|x| + |y|)$$
Recall that for any real numbers $u, c$ with $c \ge 0$, the inequality $-c \le u \le c$ is logically equivalent to $|u| \le c$. Letting $u = x + y$ and $c = |x| + |y|$, we conclude:
$$|x + y| \le |x| + |y| \quad \blacksquare$$

#### Proof of the Reverse Triangle Inequality:
Write $x = (x - y) + y$. By the triangle inequality:
$$|x| = |(x - y) + y| \le |x - y| + |y| \implies |x| - |y| \le |x - y|$$
Similarly, write $y = (y - x) + x$:
$$|y| \le |y - x| + |x| = |x - y| + |x| \implies -|x - y| \le |x| - |y|$$
Combining these two inequalities:
$$-|x - y| \le |x| - |y| \le |x - y| \iff ||x| - |y|| \le |x - y| \quad \blacksquare$$"""
            },
            {
                "secNumber": "1.2",
                "title": "Bounded Sets, Supremum, Infimum & The Completeness Axiom",
                "content": r"""### 1. Bounds in Ordered Sets

> **Definition 1.4 (Upper Bounds, Lower Bounds & Boundedness):**
> Let $S \subseteq \mathbb{R}$ be a non-empty subset.
> 1. An element $M \in \mathbb{R}$ is an **upper bound** of $S$ if $x \le M$ for every $x \in S$. If such an $M$ exists, $S$ is said to be **bounded above**.
> 2. An element $m \in \mathbb{R}$ is a **lower bound** of $S$ if $m \le x$ for every $x \in S$. If such an $m$ exists, $S$ is said to be **bounded below**.
> 3. The set $S$ is **bounded** if it is bounded both above and below, which is equivalent to saying there exists $K > 0$ such that $|x| \le K$ for all $x \in S$.

---

### 2. Supremum and Infimum

> **Definition 1.5 (Supremum / Least Upper Bound):**
> Let $S \subseteq \mathbb{R}$ be non-empty and bounded above. A real number $L$ is the **supremum** (or least upper bound) of $S$, denoted $L = \sup S$ or $\operatorname{lub}(S)$, if:
> 1. $L$ is an upper bound of $S$: $\forall x \in S, \; x \le L$.
> 2. No number strictly less than $L$ is an upper bound of $S$: if $M < L$, then there exists some $x_0 \in S$ such that $x_0 > M$.

Equivalently, the second condition is formulated in standard $\epsilon$-analysis as:
$$\forall \epsilon > 0, \; \exists x_\epsilon \in S \text{ such that } x_\epsilon > L - \epsilon$$

> **Definition 1.6 (Infimum / Greatest Lower Bound):**
> Let $S \subseteq \mathbb{R}$ be non-empty and bounded below. A real number $\ell$ is the **infimum** (or greatest lower bound) of $S$, denoted $\ell = \inf S$ or $\operatorname{glb}(S)$, if:
> 1. $\ell$ is a lower bound of $S$: $\forall x \in S, \; \ell \le x$.
> 2. For every $\epsilon > 0$, there exists some $x_\epsilon \in S$ such that $x_\epsilon < \ell + \epsilon$.

> **Remark (Maximum vs. Supremum):**
> If $L = \sup S$ and $L \in S$, then $L$ is called the **maximum** of $S$, denoted $\max S$. Unlike the maximum, the supremum does not need to belong to $S$. For example, if $S = (0, 1)$, then $\sup S = 1 \notin S$, and $\max S$ does not exist.

---

### 3. The Completeness Axiom (Axiom of Continuity)

> **Axiom 1.1 (The Completeness Axiom / Least Upper Bound Property):**
> Every non-empty subset $S \subset \mathbb{R}$ that is bounded above has a supremum in $\mathbb{R}$:
> $$\emptyset \ne S \subset \mathbb{R} \text{ and } \exists M \in \mathbb{R} \text{ s.t. } (\forall x \in S, x \le M) \implies \exists L \in \mathbb{R} \text{ s.t. } L = \sup S$$

> **Theorem 1.2 (Greatest Lower Bound Property):**
> Every non-empty subset $T \subset \mathbb{R}$ that is bounded below has an infimum in $\mathbb{R}$.

#### Rigorous Proof:
Let $T \subset \mathbb{R}$ be non-empty and bounded below by $m \in \mathbb{R}$. Define the reflected set:
$$-T = \{ -x : x \in T \}$$
Since $T \ne \emptyset$, $-T \ne \emptyset$.
For any $y \in -T$, $y = -x$ for some $x \in T$. Since $m \le x$, multiplying by $-1$ reverses the inequality:
$$y = -x \le -m$$
Thus, $-T$ is bounded above by $-m$.
By the Completeness Axiom, $-T$ has a supremum $L = \sup(-T) \in \mathbb{R}$.
We claim that $\inf T = -L$.
1. **Lower bound:** For any $x \in T$, $-x \in -T$, so $-x \le L$. Multiplying by $-1$ gives $x \ge -L$. Hence $-L$ is a lower bound of $T$.
2. **Greatest lower bound:** Let $\epsilon > 0$. Since $L = \sup(-T)$, there exists $y \in -T$ such that $y > L - \epsilon$.
   Writing $y = -x$ for $x \in T$, this becomes $-x > L - \epsilon \implies x < -L + \epsilon$.
Therefore, $\inf T = -L = -\sup(-T) \in \mathbb{R}$, completing the proof. $\blacksquare$"""
            },
            {
                "secNumber": "1.3",
                "title": "Dedekind Cuts Construction & Rigorous Equivalence with Completeness",
                "content": r"""### 1. Dedekind's Vision: Constructing $\mathbb{R}$ from $\mathbb{Q}$

In 1872, Richard Dedekind published *Stetigkeit und irrationale Zahlen* (Continuity and Irrational Numbers), resolving a millennium-old foundational crisis by constructing the continuum $\mathbb{R}$ directly from the rational field $\mathbb{Q}$.

Dedekind observed that any point on a geometric line divides all other points into two classes: those lying to its left and those lying to its right. If we partition $\mathbb{Q}$ into two non-empty sets $A$ and $B$ where every element of $A$ is strictly less than every element of $B$, then:
- Either $A$ has a maximum or $B$ has a minimum (corresponding to a rational cut point, like $1/2$), or
- $A$ has no maximum AND $B$ has no minimum (such as when partitioning by $x^2 < 2$ and $x^2 > 2$).

Dedekind defined a **real number** precisely as this partition!

---

### 2. Formal Definition of a Dedekind Cut

> **Definition 1.7 (Dedekind Cut):**
> A **Dedekind cut** in $\mathbb{Q}$ is a subset $\alpha \subset \mathbb{Q}$ satisfying three conditions:
> 1. **Non-triviality:** $\alpha \ne \emptyset$ and $\alpha \ne \mathbb{Q}$.
> 2. **Downward Closure:** If $p \in \alpha$, $q \in \mathbb{Q}$, and $q < p$, then $q \in \alpha$.
> 3. **No Maximum Element:** If $p \in \alpha$, there exists some $r \in \alpha$ such that $p < r$.

The set of all Dedekind cuts is defined to be $\mathbb{R}$. We embed $\mathbb{Q}$ into $\mathbb{R}$ via the canonical injection:
$$q \in \mathbb{Q} \longmapsto q^* = \{ r \in \mathbb{Q} : r < q \} \in \mathbb{R}$$

> **Definition 1.8 (Order on Cuts):**
> For two cuts $\alpha, \beta \in \mathbb{R}$, we define:
> $$\alpha < \beta \iff \alpha \subsetneq \beta$$
> That is, $\alpha$ is a proper subset of $\beta$.

---

### 3. Theorem: Dedekind Cuts Form a Complete Ordered Continuum

> **Theorem 1.3 (Dedekind Completeness Theorem):**
> The set of Dedekind cuts $\mathbb{R}$, ordered by proper set inclusion $\subsetneq$, possesses the Least Upper Bound Property.

#### Line-by-Line Proof:
Let $\mathcal{S} \subset \mathbb{R}$ be a non-empty collection of cuts that is bounded above by a cut $\beta \in \mathbb{R}$.
This means:
1. $\mathcal{S} \ne \emptyset$, so there exists at least one cut $\alpha_0 \in \mathcal{S}$.
2. There exists a cut $\beta \in \mathbb{R}$ such that for every $\alpha \in \mathcal{S}$, $\alpha \subseteq \beta$.

Define the candidate supremum set $\gamma$ as the set-theoretic union of all cuts in $\mathcal{S}$:
$$\gamma = \bigcup_{\alpha \in \mathcal{S}} \alpha$$

We must rigorously demonstrate two assertions:
**Step 1: $\gamma$ is a valid Dedekind cut ($\gamma \in \mathbb{R}$).**
- *Non-emptiness:* Since $\alpha_0 \in \mathcal{S}$ and $\alpha_0 \ne \emptyset$, there exists $p \in \alpha_0$. Thus $p \in \gamma$, so $\gamma \ne \emptyset$.
- *Proper subset of $\mathbb{Q}$:* Since $\beta$ is an upper bound, every $\alpha \in \mathcal{S}$ satisfies $\alpha \subseteq \beta$. Hence $\gamma = \bigcup_{\alpha \in \mathcal{S}} \alpha \subseteq \beta$. Since $\beta \ne \mathbb{Q}$, there exists $q \in \mathbb{Q} \setminus \beta$. Then $q \notin \gamma$, which proves $\gamma \ne \mathbb{Q}$.
- *Downward closure:* Let $p \in \gamma$ and $q \in \mathbb{Q}$ with $q < p$. Since $p \in \gamma$, there is some cut $\alpha_1 \in \mathcal{S}$ with $p \in \alpha_1$. Because $\alpha_1$ is a Dedekind cut, $q < p \implies q \in \alpha_1$. Therefore $q \in \bigcup_{\alpha \in \mathcal{S}} \alpha = \gamma$.
- *No maximum:* Let $p \in \gamma$. Then $p \in \alpha_2$ for some $\alpha_2 \in \mathcal{S}$. Since $\alpha_2$ has no maximum element, there exists $r \in \alpha_2$ such that $p < r$. Since $\alpha_2 \subseteq \gamma$, we have $r \in \gamma$. Thus $\gamma$ has no maximum element.

Hence, $\gamma$ satisfies all three axioms of a Dedekind cut, so $\gamma \in \mathbb{R}$.

**Step 2: $\gamma$ is the least upper bound of $\mathcal{S}$.**
- *$\gamma$ is an upper bound:* For every $\alpha \in \mathcal{S}$, by definition of union, $\alpha \subseteq \gamma$. Hence $\alpha \le \gamma$ in the cut order.
- *$\gamma$ is the least upper bound:* Suppose $\delta \in \mathbb{R}$ is any upper bound of $\mathcal{S}$. Then $\alpha \subseteq \delta$ for all $\alpha \in \mathcal{S}$. By basic set theory, the union of subsets is contained in any set containing each subset:
$$\gamma = \bigcup_{\alpha \in \mathcal{S}} \alpha \subseteq \delta \implies \gamma \le \delta$$

Therefore, $\gamma = \sup \mathcal{S}$. This establishes that the Dedekind cut construction yields a complete ordered field. $\blacksquare$"""
            },
            {
                "secNumber": "1.4",
                "title": "The Archimedean Property & Denseness of Rational and Irrational Numbers",
                "content": r"""### 1. The Archimedean Property

The Completeness Axiom has profound structural consequences. It guarantees that the natural numbers $\mathbb{N}$ are not bounded above within $\mathbb{R}$, ruling out infinitesimal elements.

> **Theorem 1.4 (Archimedean Property of $\mathbb{R}$):**
> 1. The set of natural numbers $\mathbb{N} = \{1, 2, 3, \dots\}$ is not bounded above in $\mathbb{R}$.
> 2. For any $x \in \mathbb{R}$, there exists an integer $n \in \mathbb{N}$ such that $n > x$.
> 3. For any $\epsilon > 0$, there exists an integer $n \in \mathbb{N}$ such that $\frac{1}{n} < \epsilon$.
> 4. For any $x, y \in \mathbb{R}$ with $x > 0$, there exists $n \in \mathbb{N}$ such that $n x > y$.

#### Rigorous Proof:
We prove statement 1 by contradiction.
Assume $\mathbb{N}$ is bounded above in $\mathbb{R}$.
Since $\mathbb{N} \ne \emptyset$ and is bounded above, by the Completeness Axiom, $\mathbb{N}$ has a supremum $L = \sup \mathbb{N} \in \mathbb{R}$.
Consider the real number $L - 1$. Since $L - 1 < L$, $L - 1$ cannot be an upper bound for $\mathbb{N}$.
Therefore, there exists some natural number $m \in \mathbb{N}$ such that:
$$m > L - 1$$
Adding 1 to both sides gives:
$$m + 1 > L$$
However, since $m \in \mathbb{N}$, we have $m + 1 \in \mathbb{N}$.
This contradicts the premise that $L$ is an upper bound for $\mathbb{N}$!
Thus, $\mathbb{N}$ is not bounded above in $\mathbb{R}$.

To prove statement 3:
Let $\epsilon > 0$. Then $\frac{1}{\epsilon} \in \mathbb{R}$. By statement 2, there exists $n \in \mathbb{N}$ such that $n > \frac{1}{\epsilon}$.
Taking reciprocals (which reverses the inequality for positive numbers) yields $\frac{1}{n} < \epsilon$. $\blacksquare$

---

### 2. Denseness of the Rational Numbers in $\mathbb{R}$

A subset $D \subset \mathbb{R}$ is said to be **dense** in $\mathbb{R}$ if every open interval $(a, b)$ contains at least one point of $D$.

> **Theorem 1.5 (Density of $\mathbb{Q}$ in $\mathbb{R}$):**
> If $x, y \in \mathbb{R}$ with $x < y$, then there exists a rational number $r \in \mathbb{Q}$ such that:
> $$x < r < y$$

#### Line-by-Line Proof:
Since $y > x$, we have $y - x > 0$.
By the Archimedean Property (statement 3 with $\epsilon = y - x$), there exists an integer $n \in \mathbb{N}$ such that:
$$\frac{1}{n} < y - x \iff n y - n x > 1$$
We now seek an integer $m \in \mathbb{Z}$ such that $n x < m < n y$.
Consider the set $S = \{ k \in \mathbb{Z} : k > n x \}$.
- By the Archimedean property, $S$ is non-empty.
- The set is bounded below by $n x$.
By the Well-Ordering Principle of integers (or greatest lower bound for $\mathbb{Z}$), $S$ possesses a smallest element, which we denote by $m$:
$$m \in S \implies m > n x$$
Since $m$ is the smallest integer strictly greater than $n x$, the preceding integer $m - 1$ is not in $S$:
$$m - 1 \le n x \implies m \le n x + 1$$
Using the inequality $n y - n x > 1$, we see that $n x + 1 < n y$.
Stringing these inequalities together:
$$n x < m \le n x + 1 < n y \implies n x < m < n y$$
Dividing by $n > 0$ preserves the inequality:
$$x < \frac{m}{n} < y$$
Setting $r = \frac{m}{n} \in \mathbb{Q}$ completes the proof. $\blacksquare$

---

### 3. Denseness of the Irrational Numbers

> **Theorem 1.6 (Density of $\mathbb{R} \setminus \mathbb{Q}$ in $\mathbb{R}$):**
> If $x, y \in \mathbb{R}$ with $x < y$, then there exists an irrational number $w \in \mathbb{R} \setminus \mathbb{Q}$ such that $x < w < y$.

#### Proof:
Since $x < y$, divide both sides by $\sqrt{2} > 0$:
$$\frac{x}{\sqrt{2}} < \frac{y}{\sqrt{2}}$$
By Theorem 1.5, there exists a rational number $r \in \mathbb{Q}$ with $r \ne 0$ such that:
$$\frac{x}{\sqrt{2}} < r < \frac{y}{\sqrt{2}}$$
(If the rational found happens to be 0, we can simply apply the density theorem to the subinterval $(0, y/\sqrt{2})$).
Multiplying by $\sqrt{2} > 0$:
$$x < r \sqrt{2} < y$$
Define $w = r \sqrt{2}$. Since $r \in \mathbb{Q} \setminus \{0\}$ and $\sqrt{2} \notin \mathbb{Q}$, $w$ must be irrational (if $w$ were rational, then $\sqrt{2} = w/r$ would be rational, a contradiction).
Hence, between any two real numbers lies an irrational number. $\blacksquare$"""
            },
            {
                "secNumber": "1.5",
                "title": "Cardinality of Real Sets, Countability & Cantor's Diagonalization Theorem",
                "content": r"""### 1. Equinumerosity and Countability

In the late 19th century, Georg Cantor revolutionized mathematical foundations by introducing set cardinality, showing that infinite sets can have different "sizes."

> **Definition 1.9 (Equinumerosity and Countability):**
> 1. Two sets $A$ and $B$ are **equinumerous** (or have the same cardinality), written $|A| = |B|$, if there exists a bijection $f: A \to B$.
> 2. A set $A$ is **countably infinite** if $|A| = |\mathbb{N}|$.
> 3. A set $A$ is **countable** if it is either finite or countably infinite.
> 4. A set that is not countable is called **uncountable**.

> **Theorem 1.7 (Countability of $\mathbb{Q}$):**
> The set of rational numbers $\mathbb{Q}$ is countably infinite: $|\mathbb{Q}| = |\mathbb{N}| = \aleph_0$.

#### Proof Sketch:
Every positive rational number can be written uniquely in lowest terms as $p/q$ with $p, q \in \mathbb{N}$ and $\gcd(p, q) = 1$. Arrange all pairs $(p, q)$ in an infinite two-dimensional grid and trace diagonally:
$$(1,1), (1,2), (2,1), (3,1), (2,2), (1,3), \dots$$
Skipping non-coprime fractions defines an explicit injection $\mathbb{Q}^+ \to \mathbb{N}$. Interleaving negative rationals extends this to a bijection $\mathbb{Q} \to \mathbb{N}$. $\blacksquare$

---

### 2. Cantor's Diagonalization Theorem: Uncountability of $\mathbb{R}$

> **Theorem 1.8 (Cantor's Theorem on the Continuum):**
> The open interval $(0, 1)$ is uncountable. Consequently, $\mathbb{R}$ is uncountable.

#### Full Formal Proof (Cantor's Diagonal Argument):
We prove the theorem by contradiction.
Suppose $(0, 1)$ is countable. Then its elements can be listed in an exhaustive sequence:
$$(0, 1) = \{ x_1, x_2, x_3, \dots, x_n, \dots \}$$
Express each real number $x_n \in (0, 1)$ in its unique decimal expansion (avoiding trailing infinite 9s to ensure uniqueness):
$$\begin{aligned}
x_1 &= 0.d_{11} d_{12} d_{13} d_{14} \dots \\
x_2 &= 0.d_{21} d_{22} d_{23} d_{24} \dots \\
x_3 &= 0.d_{31} d_{32} d_{33} d_{34} \dots \\
&\;\;\vdots \\
x_n &= 0.d_{n1} d_{n2} d_{n3} \dots d_{nn} \dots
\end{aligned}$$
where each $d_{ij} \in \{0, 1, 2, \dots, 9\}$.

We construct a new real number $y = 0.c_1 c_2 c_3 \dots c_n \dots$ by defining its $n$-th decimal digit $c_n$ along the diagonal:
$$c_n = \begin{cases} 4 & \text{if } d_{nn} \ne 4 \\ 5 & \text{if } d_{nn} = 4 \end{cases}$$
Notice:
1. Since each $c_n \in \{4, 5\}$, the decimal representation does not terminate in infinite zeros or infinite nines, making its representation unique.
2. Clearly, $0 < y < 1$, so $y \in (0, 1)$.
3. However, for every index $k \in \mathbb{N}$, the $k$-th decimal digit of $y$ is $c_k$, whereas the $k$-th decimal digit of $x_k$ is $d_{kk}$.
   By construction, $c_k \ne d_{kk}$, which implies:
   $$y \ne x_k \quad \forall k \in \mathbb{N}$$

Therefore, $y$ cannot appear anywhere in the enumerated sequence $\{x_1, x_2, x_3, \dots\}$.
This directly contradicts the assumption that the sequence was an exhaustive enumeration of $(0, 1)$!
Thus, $(0, 1)$ is uncountable, and since $(0, 1) \subset \mathbb{R}$, $\mathbb{R}$ is uncountable. $\blacksquare$

> **Corollary 1.2 (Uncountability of Irrational Numbers):**
> The set of irrational numbers $\mathbb{R} \setminus \mathbb{Q}$ is uncountable.
> 
> *Proof:* If $\mathbb{R} \setminus \mathbb{Q}$ were countable, then $\mathbb{R} = \mathbb{Q} \cup (\mathbb{R} \setminus \mathbb{Q})$ would be the union of two countable sets, and hence countable, contradicting Theorem 1.8. $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational / Problem 1.1",
                "title": "Exact Verification of Supremum and Infimum with Epsilon Proof",
                "statement": r"""Consider the set of real numbers:
$$S = \left\{ \frac{2n}{3n + 1} : n \in \mathbb{N} \right\} = \left\{ \frac{2}{4}, \frac{4}{7}, \frac{6}{10}, \frac{8}{13}, \dots \right\}$$
1. Determine $\inf S$ and prove whether $\min S$ exists.
2. Determine $\sup S$ and provide a complete, rigorous $\epsilon$-verification of your claim.
3. Does $\max S$ exist? Justify rigorously.""",
                "hints": [
                    "Examine the monotonicity of the function f(x) = 2x / (3x + 1) for x >= 1.",
                    "To prove L = sup S, show L is an upper bound and that for any eps > 0, L - eps < 2n/(3n+1) for sufficiently large n."
                ],
                "solution": r"""### 1. Determining and Proving the Infimum

Let $f(x) = \frac{2x}{3x+1}$ for $x \ge 1$. Computing its derivative:
$$f'(x) = \frac{2(3x+1) - 2x(3)}{(3x+1)^2} = \frac{6x + 2 - 6x}{(3x+1)^2} = \frac{2}{(3x+1)^2} > 0$$
Since $f'(x) > 0$ for all $x \ge 1$, $f$ is strictly increasing on $[1, \infty)$.
Consequently, for all $n \in \mathbb{N}$:
$$\frac{2(1)}{3(1)+1} = \frac{2}{4} = \frac{1}{2} \le \frac{2n}{3n+1}$$
Thus, $m = \frac{1}{2}$ is a lower bound for $S$. Since $\frac{1}{2} = \frac{2(1)}{3(1)+1} \in S$, it follows directly that:
$$\inf S = \min S = \frac{1}{2}$$

---

### 2. Determining and Rigorously Proving the Supremum

As $n \to \infty$, $\frac{2n}{3n+1} = \frac{2}{3 + 1/n} \to \frac{2}{3}$. We claim that $\sup S = \frac{2}{3}$.

#### Part A: $\frac{2}{3}$ is an Upper Bound
We must show $\frac{2n}{3n+1} \le \frac{2}{3}$ for all $n \in \mathbb{N}$.
Subtracting:
$$\frac{2}{3} - \frac{2n}{3n+1} = \frac{2(3n+1) - 6n}{3(3n+1)} = \frac{6n + 2 - 6n}{3(3n+1)} = \frac{2}{3(3n+1)}$$
Since $n \ge 1$, $3(3n+1) > 0$, so $\frac{2}{3(3n+1)} > 0$, which implies:
$$\frac{2n}{3n+1} < \frac{2}{3} \quad \forall n \in \mathbb{N}$$
Thus, $\frac{2}{3}$ is an upper bound for $S$.

#### Part B: $\epsilon$-Verification of the Least Upper Bound
Let $\epsilon > 0$ be arbitrary. We must show there exists $n \in \mathbb{N}$ such that:
$$\frac{2n}{3n+1} > \frac{2}{3} - \epsilon \iff \frac{2}{3} - \frac{2n}{3n+1} < \epsilon$$
From our previous algebraic calculation:
$$\frac{2}{3(3n+1)} < \epsilon \iff 3(3n+1) > \frac{2}{\epsilon} \iff 9n + 3 > \frac{2}{\epsilon} \iff n > \frac{2 - 3\epsilon}{9\epsilon}$$
By the Archimedean Property of $\mathbb{R}$, there exists an integer $N \in \mathbb{N}$ such that:
$$N > \max\left\{1, \left\lceil \frac{2 - 3\epsilon}{9\epsilon} \right\rceil \right\}$$
For this choice of $N \in \mathbb{N}$:
$$\frac{2N}{3N+1} > \frac{2}{3} - \epsilon$$
Since $\epsilon > 0$ was arbitrary, no number less than $\frac{2}{3}$ can be an upper bound.
Therefore, $\sup S = \frac{2}{3}$.

---

### 3. Existence of the Maximum
In Part A, we proved that $\frac{2n}{3n+1} < \frac{2}{3}$ for all $n \in \mathbb{N}$.
Hence, $\frac{2}{3} \notin S$.
Since the supremum is not an element of $S$, $\max S$ does not exist."""
            },
            {
                "tier": "Advanced / Problem 1.2",
                "title": "Complete Deductive Chain: Archimedean Property to Denseness of Rationals",
                "statement": r"""Prove the following fundamental deductive sequence entirely from the Completeness Axiom:
1. Prove that for any positive real number $y > 0$, there exists a unique integer $m \in \mathbb{Z}$ such that:
   $$m - 1 \le y < m$$
2. Using Part 1 and the Archimedean Property, give a complete, self-contained proof that if $a, b \in \mathbb{R}$ with $a < b$, there exists $q \in \mathbb{Q}$ such that $a < q < b$.
3. Deduce that the open interval $(a, b)$ contains infinitely many distinct rational numbers.""",
                "hints": [
                    "For Part 1, consider the set K = {k in Z : k > y}. Show K is bounded below and non-empty.",
                    "For Part 3, use proof by contradiction: if there were only finitely many rationals, consider the minimum distance to a."
                ],
                "solution": r"""### 1. Proof of the Floor/Ceiling Integer Existence

Let $y > 0$. Consider the set:
$$K = \{ k \in \mathbb{Z} : k > y \}$$
- **Non-emptiness:** By the Archimedean property, there exists $n \in \mathbb{N} \subset \mathbb{Z}$ such that $n > y$. Thus $n \in K$, so $K \ne \emptyset$.
- **Bounded below:** Every element $k \in K$ satisfies $k > y > 0$. Thus $K$ is bounded below by 0.

By the Well-Ordering Principle of the positive integers, any non-empty subset of $\mathbb{N}$ has a least element. Let:
$$m = \min K$$
Since $m \in K$, we have $m > y$.
Because $m$ is the minimal element of $K$, the integer immediately preceding it is not in $K$:
$$m - 1 \notin K \implies m - 1 \le y$$
Combining both inequalities gives:
$$m - 1 \le y < m$$
Uniqueness: If there were two integers $m_1 < m_2$ satisfying the condition, then $m_1 \le m_2 - 1 \le y < m_1$, a contradiction ($m_1 < m_1$). Thus $m$ is unique.

---

### 2. Proof of Denseness of Rationals

Let $a, b \in \mathbb{R}$ with $a < b$, so that $b - a > 0$.
By the Archimedean property, there exists $n \in \mathbb{N}$ such that:
$$\frac{1}{n} < b - a \iff n b - n a > 1$$
Now apply Part 1 to the real number $y = n a$:
There exists a unique integer $m \in \mathbb{Z}$ such that:
$$m - 1 \le n a < m$$
From $n a < m$, we get $a < \frac{m}{n}$.
From $m - 1 \le n a$, we add 1 to both sides:
$$m \le n a + 1$$
Since $n b - n a > 1$, we have $n a + 1 < n b$. Thus:
$$m < n b \implies \frac{m}{n} < b$$
Combining the bounds:
$$a < \frac{m}{n} < b$$
Setting $q = \frac{m}{n} \in \mathbb{Q}$, we have found a rational number in $(a, b)$.

---

### 3. Infinitude of Rationals in Any Open Interval

Assume for contradiction that $(a, b) \cap \mathbb{Q}$ is finite:
$$(a, b) \cap \mathbb{Q} = \{ q_1, q_2, \dots, q_k \}$$
Since each $q_i \in (a, b)$, we have $a < q_i$ for all $i$.
Define:
$$q^* = \min \{ q_1, q_2, \dots, q_k \}$$
Since the set is finite and non-empty, the minimum exists and satisfies $a < q^* < b$.
Now consider the sub-interval $(a, q^*)$.
Since $a < q^*$, by Part 2 there exists a rational number $r \in \mathbb{Q}$ such that:
$$a < r < q^*$$
Since $a < r < q^* < b$, $r$ lies in $(a, b)$.
Thus $r \in (a, b) \cap \mathbb{Q}$.
However, $r < q^* = \min \{q_1, \dots, q_k\}$, meaning $r \notin \{q_1, \dots, q_k\}$.
This contradicts the assumption that $\{q_1, \dots, q_k\}$ contained all rational numbers in $(a, b)$!
Hence, $(a, b)$ contains infinitely many rational numbers."""
            },
            {
                "tier": "Honors / Problem 1.3",
                "title": "Constructive Dedekind Cut Verification of the Least Upper Bound Property",
                "statement": r"""Let $\mathbb{R}$ be defined as the set of all Dedekind cuts in $\mathbb{Q}$. Let $\mathcal{A}$ be a non-empty family of cuts that is bounded above by a cut $\beta \in \mathbb{R}$.
Define:
$$\gamma = \bigcup_{\alpha \in \mathcal{A}} \alpha$$
1. Prove with full axiomatic rigor that $\gamma$ satisfies property (2) of a Dedekind cut: if $p \in \gamma$ and $q < p$ with $q \in \mathbb{Q}$, then $q \in \gamma$.
2. Prove that $\gamma$ satisfies property (3): $\gamma$ contains no maximal element.
3. Prove that if $\delta$ is another cut such that $\alpha \le \delta$ for all $\alpha \in \mathcal{A}$, then $\gamma \le \delta$. Conclude that $\gamma = \sup \mathcal{A}$.""",
                "hints": [
                    "Recall that p in gamma means p in alpha for at least one cut alpha in A.",
                    "Use the fact that every cut alpha in A is already a valid Dedekind cut."
                ],
                "solution": r"""### 1. Proof of Downward Closure for $\gamma$

Let $p \in \gamma$ and let $q \in \mathbb{Q}$ such that $q < p$.
By the definition of the set-theoretic union:
$$p \in \gamma = \bigcup_{\alpha \in \mathcal{A}} \alpha \implies \exists \alpha_0 \in \mathcal{A} \text{ such that } p \in \alpha_0$$
Since $\alpha_0 \in \mathcal{A}$, $\alpha_0$ is by definition a Dedekind cut.
By the downward closure property of the cut $\alpha_0$:
$$\text{Since } p \in \alpha_0 \text{ and } q \in \mathbb{Q} \text{ with } q < p, \text{ it follows that } q \in \alpha_0$$
Now, since $\alpha_0 \subseteq \bigcup_{\alpha \in \mathcal{A}} \alpha = \gamma$, we have:
$$q \in \alpha_0 \implies q \in \gamma$$
This establishes that $\gamma$ is downward closed in $\mathbb{Q}$.

---

### 2. Proof that $\gamma$ Has No Maximum Element

Let $p \in \gamma$.
Again, by definition of the union, there exists some cut $\alpha_1 \in \mathcal{A}$ such that $p \in \alpha_1$.
Because $\alpha_1$ is a Dedekind cut, it contains no maximum element.
Therefore, there exists a rational number $r \in \alpha_1$ such that:
$$p < r$$
Since $\alpha_1 \subseteq \gamma$, we have $r \in \gamma$.
We have thus demonstrated that for every $p \in \gamma$, there exists $r \in \gamma$ with $p < r$.
Hence, $\gamma$ contains no maximum element.

---

### 3. Proof of the Minimality of the Upper Bound ($\gamma = \sup \mathcal{A}$)

Let $\delta \in \mathbb{R}$ be any upper bound for $\mathcal{A}$.
In the Dedekind cut ordering, this means:
$$\alpha \le \delta \iff \alpha \subseteq \delta \quad \forall \alpha \in \mathcal{A}$$
We must show that $\gamma \le \delta$, which translates to $\gamma \subseteq \delta$.

Let $x \in \gamma$.
Then $x \in \alpha$ for some $\alpha \in \mathcal{A}$.
Since $\alpha \subseteq \delta$ (because $\delta$ is an upper bound for $\mathcal{A}$), it immediately follows that:
$$x \in \delta$$
Since this holds for every $x \in \gamma$, we have:
$$\gamma \subseteq \delta \iff \gamma \le \delta$$
Finally, for any $\alpha \in \mathcal{A}$, by definition of union we have $\alpha \subseteq \gamma$, so $\alpha \le \gamma$.
Thus, $\gamma$ is an upper bound for $\mathcal{A}$, and any other upper bound $\delta$ satisfies $\gamma \le \delta$.
Therefore, $\gamma$ is the least upper bound:
$$\gamma = \sup \mathcal{A} \quad \blacksquare$$"""
            }
        ]
    }
    return u1

if __name__ == "__main__":
    u = get_unit1()
    print(f"Loaded Unit 1: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
