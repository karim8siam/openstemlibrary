# -*- coding: utf-8 -*-
"""
build_ra_unit5.py
Constructs Unit 5: Continuous Real Functions: Epsilon-Delta Rigor, Compactness & Intermediate Values
"""

def get_unit5():
    u5 = {
        "number": 5,
        "title": "Continuous Real Functions: Epsilon-Delta Rigor, Compactness & Intermediate Values",
        "leadSummary": "Comprehensive mathematical theory of continuous functions on R: epsilon-delta functional limits, Heine's sequential characterization, topological continuity via open preimages, classification of discontinuities, continuous mappings on compact sets and the Extreme Value Theorem, continuous mappings on connected sets and the Intermediate Value Theorem, and uniform continuity with the Heine-Cantor theorem.",
        "simulations": ["sim_ra_continuity_epsilon_delta"],
        "sections": [
            {
                "secNumber": "5.1",
                "title": "Functional Limits: The Epsilon-Delta Definition & Heine's Sequential Criterion",
                "content": r"""### 1. The Cauchy-Weierstrass $\epsilon$-$\delta$ Limit Definition

> **Definition 5.1 (Limit of a Function):**
> Let $E \subseteq \mathbb{R}$, $f: E \to \mathbb{R}$, and let $c \in \mathbb{R}$ be a limit point of $E$.
> A real number $L \in \mathbb{R}$ is the **limit** of $f(x)$ as $x$ approaches $c$, denoted:
> $$\lim_{x \to c} f(x) = L$$
> if for every $\epsilon > 0$, there exists a $\delta > 0$ such that for all $x \in E$:
> $$0 < |x - c| < \delta \implies |f(x) - L| < \epsilon$$
> In terms of topological neighborhoods: $x \in V_\delta^*(c) \cap E \implies f(x) \in V_\epsilon(L)$.

---

### 2. Heine's Sequential Characterization of Limits

Karl Weierstrass and Eduard Heine discovered that limits of functions can be completely characterized through limits of sequences, linking differential calculus with sequential analysis.

> **Theorem 5.1 (Heine's Sequential Criterion for Functional Limits):**
> Let $f: E \to \mathbb{R}$ and let $c$ be a limit point of $E$. Then:
> $$\lim_{x \to c} f(x) = L$$
> if and only if for every sequence $(x_n)_{n=1}^\infty$ in $E \setminus \{c\}$ that converges to $c$:
> $$\lim_{n \to \infty} f(x_n) = L$$

#### Complete Rigorous Proof:
$(\implies)$ Assume $\lim_{x \to c} f(x) = L$.
Let $\epsilon > 0$. By Definition 5.1, there exists $\delta > 0$ such that:
$$0 < |x - c| < \delta \implies |f(x) - L| < \epsilon$$
Now let $(x_n)$ be any sequence in $E \setminus \{c\}$ such that $x_n \to c$.
By Definition 3.2 of sequence convergence, corresponding to this $\delta > 0$, there exists an index $N \in \mathbb{N}$ such that for all $n \ge N$:
$$|x_n - c| < \delta$$
Since $x_n \ne c$, we have $0 < |x_n - c| < \delta$ for all $n \ge N$.
Therefore, for all $n \ge N$:
$$|f(x_n) - L| < \epsilon$$
This proves that $f(x_n) \to L$ as $n \to \infty$.

$(\impliedby)$ We prove the contrapositive: if $\lim_{x \to c} f(x) \ne L$, then there exists a sequence $(x_n)$ in $E \setminus \{c\}$ with $x_n \to c$ such that $f(x_n) \not\to L$.
Assume $\lim_{x \to c} f(x) \ne L$.
Negating Definition 5.1:
$$\exists \epsilon_0 > 0 \text{ s.t. } \forall \delta > 0, \; \exists x \in E \text{ with } 0 < |x - c| < \delta \text{ and } |f(x) - L| \ge \epsilon_0$$
For each $n \in \mathbb{N}$, choose $\delta = \frac{1}{n} > 0$.
By the negated condition, there exists a point $x_n \in E$ such that:
$$0 < |x_n - c| < \frac{1}{n} \quad \text{and} \quad |f(x_n) - L| \ge \epsilon_0$$
Since $0 < |x_n - c| < \frac{1}{n}$, by the Squeeze Theorem, $x_n \to c$ with $x_n \ne c$.
However, since $|f(x_n) - L| \ge \epsilon_0$ for all $n$, the sequence $f(x_n)$ cannot converge to $L$.
This establishes the contrapositive, completing the proof. $\blacksquare$

> **Application (Proving Non-Existence of Limits):**
> To prove that $\lim_{x \to 0} \sin\left(\frac{1}{x}\right)$ does not exist:
> Pick $x_n = \frac{1}{2\pi n} \to 0$, so $\sin(1/x_n) = \sin(2\pi n) = 0 \to 0$.
> Pick $y_n = \frac{1}{2\pi n + \pi/2} \to 0$, so $\sin(1/y_n) = \sin(2\pi n + \pi/2) = 1 \to 1$.
> Since two sequences converging to 0 yield different functional limits, $\lim_{x \to 0} \sin(1/x)$ does not exist!"""
            },
            {
                "secNumber": "5.2",
                "title": "Continuity, Preimages of Open Sets & Discontinuity Taxonomies",
                "content": r"""### 1. Continuity at a Point and on Sets

> **Definition 5.2 (Continuity at a Point):**
> Let $f: E \to \mathbb{R}$ and $c \in E$. The function $f$ is **continuous at $c$** if for every $\epsilon > 0$, there exists $\delta > 0$ such that for all $x \in E$:
> $$|x - c| < \delta \implies |f(x) - f(c)| < \epsilon$$
> If $c$ is a limit point of $E$, continuity at $c$ is equivalent to:
> $$\lim_{x \to c} f(x) = f(c)$$
> If $c$ is an isolated point of $E$, $f$ is automatically continuous at $c$.
> The function $f$ is **continuous on $E$** if it is continuous at every point $c \in E$.

---

### 2. Topological Characterization: Preimages of Open Sets

In modern topology, continuity is defined entirely through the geometry of open sets, freeing the concept from metric coordinates.

> **Theorem 5.2 (Topological Continuity Theorem):**
> A function $f: \mathbb{R} \to \mathbb{R}$ is continuous on $\mathbb{R}$ if and only if for every open set $V \subseteq \mathbb{R}$, the preimage $f^{-1}(V)$ is open in $\mathbb{R}$:
> $$f \text{ is continuous} \iff \forall V \text{ open in } \mathbb{R}, \; f^{-1}(V) = \{ x \in \mathbb{R} : f(x) \in V \} \text{ is open in } \mathbb{R}$$

#### Complete Line-by-Line Proof:
$(\implies)$ Assume $f$ is continuous on $\mathbb{R}$.
Let $V \subseteq \mathbb{R}$ be an open set.
To show $f^{-1}(V)$ is open, let $x_0 \in f^{-1}(V)$.
This means $y_0 = f(x_0) \in V$.
Since $V$ is open, there exists an $\epsilon > 0$ such that the ball $B(y_0, \epsilon) = (y_0 - \epsilon, y_0 + \epsilon) \subseteq V$.
Since $f$ is continuous at $x_0$, corresponding to this $\epsilon > 0$, there exists $\delta > 0$ such that:
$$|x - x_0| < \delta \implies |f(x) - f(x_0)| < \epsilon$$
In terms of balls:
$$x \in B(x_0, \delta) \implies f(x) \in B(y_0, \epsilon) \subseteq V$$
Therefore, $B(x_0, \delta) \subseteq f^{-1}(V)$.
Thus, every point of $f^{-1}(V)$ is an interior point, so $f^{-1}(V)$ is open.

$(\impliedby)$ Assume $f^{-1}(V)$ is open for every open set $V \subseteq \mathbb{R}$.
Let $x_0 \in \mathbb{R}$ and let $\epsilon > 0$.
The ball $V = B(f(x_0), \epsilon) = (f(x_0) - \epsilon, f(x_0) + \epsilon)$ is an open set.
By hypothesis, $f^{-1}(V)$ is an open subset of $\mathbb{R}$.
Notice that $x_0 \in f^{-1}(V)$ because $f(x_0) \in V$.
Since $f^{-1}(V)$ is open, there exists $\delta > 0$ such that:
$$B(x_0, \delta) \subseteq f^{-1}(V)$$
This means that for all $x$ with $|x - x_0| < \delta$, $x \in f^{-1}(V) \implies f(x) \in V = B(f(x_0), \epsilon) \implies |f(x) - f(x_0)| < \epsilon$.
Therefore, $f$ is continuous at $x_0$.
Since $x_0$ was arbitrary, $f$ is continuous on $\mathbb{R}$. $\blacksquare$

---

### 3. Classification of Discontinuities

Let $f$ be defined on an interval and let $c$ be an interior point. Let $f(c^+) = \lim_{x \to c^+} f(x)$ and $f(c^-) = \lim_{x \to c^-} f(x)$.
1. **Removable Discontinuity:** Both one-sided limits exist and are equal ($f(c^+) = f(c^-)$), but do not equal $f(c)$ (or $f(c)$ is undefined).
2. **Jump Discontinuity (Discontinuity of the First Kind):** Both one-sided limits exist as finite numbers, but $f(c^+) \ne f(c^-)$.
3. **Essential Discontinuity (Discontinuity of the Second Kind):** At least one of the one-sided limits does not exist (or is infinite), e.g., $\sin(1/x)$ at $x=0$."""
            },
            {
                "secNumber": "5.3",
                "title": "Continuous Functions on Compact Sets: The Extreme Value Theorem",
                "content": r"""### 1. Preservation of Compactness

> **Theorem 5.3 (Compactness Preservation Theorem):**
> Let $K \subset \mathbb{R}$ be compact, and let $f: K \to \mathbb{R}$ be continuous. Then the image $f(K) = \{f(x) : x \in K\}$ is compact.

#### Proof:
Let $\{V_\alpha\}_{\alpha \in \Lambda}$ be an open cover of $f(K)$:
$$f(K) \subseteq \bigcup_{\alpha \in \Lambda} V_\alpha$$
Taking preimages:
$$K \subseteq f^{-1}\left( \bigcup_{\alpha \in \Lambda} V_\alpha \right) = \bigcup_{\alpha \in \Lambda} f^{-1}(V_\alpha)$$
By Theorem 5.2, each $f^{-1}(V_\alpha)$ is open in the subspace topology of $K$.
Thus $\{f^{-1}(V_\alpha)\}$ is an open cover of $K$.
Since $K$ is compact, there exists a finite subcover:
$$K \subseteq \bigcup_{i=1}^m f^{-1}(V_{\alpha_i})$$
Applying $f$ to both sides:
$$f(K) \subseteq f\left( \bigcup_{i=1}^m f^{-1}(V_{\alpha_i}) \right) = \bigcup_{i=1}^m f(f^{-1}(V_{\alpha_i})) \subseteq \bigcup_{i=1}^m V_{\alpha_i}$$
Thus, $\{V_{\alpha_1}, \dots, V_{\alpha_m}\}$ is a finite subcover of $f(K)$.
Therefore, $f(K)$ is compact. $\blacksquare$

---

### 2. The Weierstrass Extreme Value Theorem

> **Theorem 5.4 (Weierstrass Extreme Value Theorem - EVT):**
> If $f: [a, b] \to \mathbb{R}$ is continuous on a closed bounded interval $[a, b]$, then:
> 1. $f$ is bounded on $[a, b]$.
> 2. $f$ attains both its maximum and minimum values on $[a, b]$:
>    $$\exists x_{\min}, x_{\max} \in [a, b] \text{ such that } f(x_{\min}) \le f(x) \le f(x_{\max}) \quad \forall x \in [a, b]$$

#### Complete Line-by-Line Proof:
By the Heine-Borel Theorem, $[a, b]$ is compact.
By Theorem 5.3, the image $f([a, b]) \subset \mathbb{R}$ is compact.
By the Heine-Borel Theorem again, $f([a, b])$ must be **closed and bounded**.
1. Since $f([a, b])$ is bounded, $f$ is bounded on $[a, b]$.
2. Let $M = \sup f([a, b])$ and $m = \inf f([a, b])$.
   By the properties of supremum and infimum, $M$ and $m$ are limit points (or isolated points) of $f([a, b])$.
   In either case, $M, m \in \overline{f([a, b])}$.
   Since $f([a, b])$ is closed, $\overline{f([a, b])} = f([a, b])$.
   Therefore:
   $$M \in f([a, b]) \quad \text{and} \quad m \in f([a, b])$$
   This means there exist points $x_{\max}, x_{\min} \in [a, b]$ such that:
   $$f(x_{\max}) = M = \sup f([a, b]) \quad \text{and} \quad f(x_{\min}) = m = \inf f([a, b])$$
   Consequently, for all $x \in [a, b]$, $f(x_{\min}) \le f(x) \le f(x_{\max})$. $\blacksquare$"""
            },
            {
                "secNumber": "5.4",
                "title": "Continuous Functions on Connected Sets: Intermediate Value Theorem",
                "content": r"""### 1. Preservation of Connectedness

> **Theorem 5.5 (Connectedness Preservation Theorem):**
> Let $E \subseteq \mathbb{R}$ be connected, and let $f: E \to \mathbb{R}$ be continuous. Then the image $f(E)$ is connected.

#### Proof:
We prove this by contradiction.
Suppose $f(E)$ is disconnected.
Then there exist non-empty separated sets $A, B$ such that $f(E) = A \cup B$, with $\overline{A} \cap B = \emptyset$ and $A \cap \overline{B} = \emptyset$.
Define:
$$U = f^{-1}(A) \quad \text{and} \quad V = f^{-1}(B)$$
Since $A \ne \emptyset$ and $B \ne \emptyset$, $U$ and $V$ are non-empty subsets of $E$, and $E = U \cup V$.
Furthermore, by continuity, $f(\overline{U}) \subseteq \overline{f(U)} = \overline{A}$.
Since $\overline{A} \cap B = \emptyset$, we have $f(\overline{U}) \cap B = \emptyset$, which implies $\overline{U} \cap V = \emptyset$.
Similarly, $U \cap \overline{V} = \emptyset$.
Thus $U$ and $V$ form a separation of $E$, which contradicts the hypothesis that $E$ is connected!
Therefore, $f(E)$ is connected. $\blacksquare$

---

### 2. Bolzano's Intermediate Value Theorem

> **Theorem 5.6 (Bolzano's Intermediate Value Theorem - IVT):**
> Let $f: [a, b] \to \mathbb{R}$ be continuous. If $u$ is any number strictly between $f(a)$ and $f(b)$, then there exists at least one $c \in (a, b)$ such that:
> $$f(c) = u$$

#### Elegant Topological Proof:
The interval $[a, b]$ is connected (Theorem 2.7).
By Theorem 5.5, the image $f([a, b])$ is a connected subset of $\mathbb{R}$.
By Theorem 2.7, connected subsets of $\mathbb{R}$ are intervals!
Since $f(a) \in f([a, b])$ and $f(b) \in f([a, b])$, the image interval contains the entire segment between $f(a)$ and $f(b)$.
Since $u$ lies between $f(a)$ and $f(b)$, $u \in f([a, b])$.
Therefore, there exists $c \in [a, b]$ such that $f(c) = u$.
Since $u \ne f(a)$ and $u \ne f(b)$, $c \in (a, b)$. $\blacksquare$"""
            },
            {
                "secNumber": "5.5",
                "title": "Uniform Continuity, The Heine-Cantor Theorem & Lipschitz Functions",
                "content": r"""### 1. Pointwise vs. Uniform Continuity

In standard continuity at a point $c$, the choice of $\delta$ depends on both $\epsilon$ AND the location $c$: $\delta(\epsilon, c)$. For example, for $f(x) = 1/x$ on $(0, 1)$, as $x \to 0$, the function steepens dramatically, forcing $\delta \to 0$ for a fixed $\epsilon$.

> **Definition 5.3 (Uniform Continuity):**
> A function $f: E \to \mathbb{R}$ is **uniformly continuous** on $E$ if for every $\epsilon > 0$, there exists a $\delta > 0$ **independent of the points** such that:
> $$\forall x, y \in E, \quad |x - y| < \delta \implies |f(x) - f(y)| < \epsilon$$

---

### 2. The Heine-Cantor Theorem

> **Theorem 5.7 (Heine-Cantor Theorem):**
> Let $K \subset \mathbb{R}$ be compact. If $f: K \to \mathbb{R}$ is continuous on $K$, then $f$ is **uniformly continuous** on $K$.

#### Complete Proof via Open Covers:
Let $\epsilon > 0$ be given.
Since $f$ is continuous at each point $x \in K$, there exists a $\delta_x > 0$ such that:
$$\forall y \in K, \quad |x - y| < \delta_x \implies |f(x) - f(y)| < \frac{\epsilon}{2}$$
For each $x \in K$, consider the open ball centered at $x$ with half-radius:
$$U_x = B\left( x, \frac{\delta_x}{2} \right) = \left( x - \frac{\delta_x}{2}, x + \frac{\delta_x}{2} \right)$$
The family $\{U_x\}_{x \in K}$ forms an open cover of $K$: $K \subseteq \bigcup_{x \in K} U_x$.
Since $K$ is compact, there exists a finite subcover:
$$K \subseteq U_{x_1} \cup U_{x_2} \cup \dots \cup U_{x_m}$$
Define $\delta$ to be the minimum of these finitely many positive half-radii:
$$\delta = \min \left\{ \frac{\delta_{x_1}}{2}, \frac{\delta_{x_2}}{2}, \dots, \frac{\delta_{x_m}}{2} \right\} > 0$$

Now, let $p, q \in K$ be any two points such that $|p - q| < \delta$.
Since the finite subcover covers $K$, $p \in U_{x_k}$ for some $k \in \{1, 2, \dots, m\}$.
This means:
$$|p - x_k| < \frac{\delta_{x_k}}{2} < \delta_{x_k} \implies |f(p) - f(x_k)| < \frac{\epsilon}{2}$$
Now, using the Triangle Inequality to estimate the distance between $q$ and $x_k$:
$$|q - x_k| \le |q - p| + |p - x_k| < \delta + \frac{\delta_{x_k}}{2} \le \frac{\delta_{x_k}}{2} + \frac{\delta_{x_k}}{2} = \delta_{x_k}$$
Since $|q - x_k| < \delta_{x_k}$, it follows by definition of $\delta_{x_k}$ that:
$$|f(q) - f(x_k)| < \frac{\epsilon}{2}$$
Finally, applying the Triangle Inequality to $|f(p) - f(q)|$:
$$|f(p) - f(q)| \le |f(p) - f(x_k)| + |f(x_k) - f(q)| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$
Since $\delta$ depends solely on $\epsilon$ and the compact set $K$, $f$ is uniformly continuous on $K$. $\blacksquare$

---

### 3. Lipschitz Continuity

> **Definition 5.4 (Lipschitz Continuity):**
> A function $f: E \to \mathbb{R}$ is **Lipschitz continuous** if there exists a constant $L > 0$ such that:
> $$|f(x) - f(y)| \le L |x - y| \quad \forall x, y \in E$$
> 
> *Proposition:* Every Lipschitz function is uniformly continuous (choose $\delta = \epsilon / L$)."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational / Problem 5.1",
                "title": "Rigorous Epsilon-Delta Verification & Analysis of Thomae's Popcorn Function",
                "statement": r"""1. Prove directly from the $\epsilon$-$\delta$ definition that $f(x) = x^3 - 2x$ is continuous at $c = 2$.
2. Thomae's function (the popcorn function) $T: [0, 1] \to \mathbb{R}$ is defined by:
   $$T(x) = \begin{cases} \frac{1}{q} & \text{if } x = \frac{p}{q} \in \mathbb{Q} \cap [0, 1] \text{ in lowest terms} \\ 0 & \text{if } x \in (\mathbb{R} \setminus \mathbb{Q}) \cap [0, 1] \end{cases}$$
   Prove that $T$ is discontinuous at every rational point in $[0, 1]$ and continuous at every irrational point in $[0, 1]$.""",
                "hints": [
                    "For part 1, factor f(x) - f(2) = (x - 2)(x^2 + 2x + 2). Bound the quadratic term by assuming |x - 2| < 1.",
                    "For part 2, at an irrational x_0, notice that for any eps > 0, there are only finitely many rationals with denominator q <= 1/eps."
                ],
                "solution": r"""### 1. $\epsilon$-$\delta$ Continuity of $f(x) = x^3 - 2x$ at $c = 2$
We calculate $f(2) = 2^3 - 2(2) = 8 - 4 = 4$.
We examine the difference $|f(x) - 4|$:
$$f(x) - 4 = x^3 - 2x - 4 = (x - 2)(x^2 + 2x + 2)$$
We bound the factor $|x^2 + 2x + 2|$ by restricting $x$ to a neighborhood around $c = 2$.
Assume $\delta \le 1$, so that $|x - 2| < 1 \implies 1 < x < 3$.
Then:
$$|x^2 + 2x + 2| \le |x|^2 + 2|x| + 2 < 3^2 + 2(3) + 2 = 9 + 6 + 2 = 17$$
Therefore, when $|x - 2| < 1$:
$$|f(x) - 4| = |x - 2| \cdot |x^2 + 2x + 2| < 17 |x - 2|$$
Let $\epsilon > 0$ be arbitrary. Choose:
$$\delta = \min\left\{ 1, \frac{\epsilon}{17} \right\} > 0$$
Then for all $x$ satisfying $|x - 2| < \delta$:
$$|f(x) - f(2)| = |x - 2| \cdot |x^2 + 2x + 2| < \frac{\epsilon}{17} \cdot 17 = \epsilon$$
Thus, $f$ is continuous at $x = 2$. $\blacksquare$

---

### 2. Analytical Verification of Thomae's Function

**Part A: Discontinuity at every rational point $r \in \mathbb{Q} \cap [0, 1]$.**
Let $r = p/q \in \mathbb{Q}$. Then $T(r) = 1/q > 0$.
By the density of irrational numbers (Theorem 1.6), there exists a sequence of irrationals $(x_n)$ converging to $r$.
For all $n$, $T(x_n) = 0$.
Thus:
$$\lim_{n \to \infty} T(x_n) = 0 \ne \frac{1}{q} = T(r)$$
By Heine's Sequential Criterion (Theorem 5.1), $T$ is **discontinuous at $r$**.

**Part B: Continuity at every irrational point $x_0 \in (\mathbb{R} \setminus \mathbb{Q}) \cap [0, 1]$.**
Here $T(x_0) = 0$.
Let $\epsilon > 0$ be given.
By the Archimedean property, choose $N \in \mathbb{N}$ such that $\frac{1}{N} < \epsilon$.
Consider the set of all rational numbers in $[0, 1]$ with denominator $q \le N$:
$$S_N = \left\{ \frac{p}{q} \in [0, 1] : 1 \le q \le N, \; 0 \le p \le q \right\}$$
The set $S_N$ is **finite**!
Since $x_0$ is irrational, $x_0 \notin S_N$.
Define $\delta$ to be the distance from $x_0$ to the closest rational in $S_N$:
$$\delta = \min \{ |x_0 - s| : s \in S_N \} > 0$$
Now let $x \in [0, 1]$ with $|x - x_0| < \delta$:
- If $x$ is irrational: $|T(x) - T(x_0)| = |0 - 0| = 0 < \epsilon$.
- If $x$ is rational: since $|x - x_0| < \delta$, $x \notin S_N$. Therefore, the denominator of $x = p/q$ must satisfy $q > N$.
  Thus:
  $$|T(x) - T(x_0)| = \left| \frac{1}{q} - 0 \right| = \frac{1}{q} < \frac{1}{N} < \epsilon$$
In both cases, $|x - x_0| < \delta \implies |T(x) - T(x_0)| < \epsilon$.
Therefore, $T$ is **continuous at every irrational point** $x_0$. $\blacksquare$"""
            },
            {
                "tier": "Advanced / Problem 5.2",
                "title": "Rigorous Proof of the Heine-Cantor Theorem via Sequential Compactness",
                "statement": r"""Provide a complete, self-contained proof of the Heine-Cantor Theorem using the Bolzano-Weierstrass theorem for sequences:
If $f: K \to \mathbb{R}$ is continuous on a compact set $K \subset \mathbb{R}$, then $f$ is uniformly continuous on $K$.""",
                "hints": [
                    "Argue by contradiction: assume f is not uniformly continuous.",
                    "Negating uniform continuity produces an eps_0 > 0 and two sequences (x_n), (y_n) in K with |x_n - y_n| < 1/n but |f(x_n) - f(y_n)| >= eps_0.",
                    "Use Bolzano-Weierstrass to extract convergent subsequences."
                ],
                "solution": r"""### 1. Setting up the Contradiction
Assume for contradiction that $f$ is continuous on $K$, but $f$ is **not uniformly continuous** on $K$.
Negating the definition of uniform continuity:
$$\exists \epsilon_0 > 0 \text{ s.t. } \forall \delta > 0, \; \exists x, y \in K \text{ with } |x - y| < \delta \text{ and } |f(x) - f(y)| \ge \epsilon_0$$
For each $n \in \mathbb{N}$, set $\delta = \frac{1}{n} > 0$.
This generates two sequences $(x_n)_{n=1}^\infty$ and $(y_n)_{n=1}^\infty$ in $K$ such that:
$$|x_n - y_n| < \frac{1}{n} \quad \text{and} \quad |f(x_n) - f(y_n)| \ge \epsilon_0 \quad \forall n \in \mathbb{N}$$

---

### 2. Extracting Convergent Subsequences via Bolzano-Weierstrass
Since $K$ is compact, $K$ is bounded (Heine-Borel).
The sequence $(x_n)$ is a bounded sequence in $\mathbb{R}$.
By the Bolzano-Weierstrass Theorem (Theorem 3.8), $(x_n)$ possesses a convergent subsequence $(x_{n_k})$:
$$\lim_{k \to \infty} x_{n_k} = p$$
Since $K$ is closed, $p \in K$.
Now consider the corresponding subsequence $(y_{n_k})$ of $(y_n)$:
$$|y_{n_k} - p| \le |y_{n_k} - x_{n_k}| + |x_{n_k} - p| < \frac{1}{n_k} + |x_{n_k} - p|$$
As $k \to \infty$, $\frac{1}{n_k} \to 0$ and $|x_{n_k} - p| \to 0$.
By the Squeeze Theorem:
$$\lim_{k \to \infty} y_{n_k} = p$$

---

### 3. Reaching the Contradiction via Continuity
Since $f$ is continuous on $K$, $f$ is continuous at $p \in K$.
By Heine's Sequential Criterion (Theorem 5.1):
$$\lim_{k \to \infty} f(x_{n_k}) = f(p) \quad \text{and} \quad \lim_{k \to \infty} f(y_{n_k}) = f(p)$$
By the algebraic limit theorem for sequences:
$$\lim_{k \to \infty} |f(x_{n_k}) - f(y_{n_k})| = |f(p) - f(p)| = 0$$
However, by construction, for every $k \in \mathbb{N}$:
$$|f(x_{n_k}) - f(y_{n_k})| \ge \epsilon_0 > 0$$
Taking the limit as $k \to \infty$ yields:
$$0 \ge \epsilon_0 > 0$$
an impossible contradiction!
Therefore, $f$ must be uniformly continuous on $K$. $\blacksquare$"""
            },
            {
                "tier": "Honors / Problem 5.3",
                "title": "Comprehensive Proof of Fixed Point Theorems via Intermediate Value Property",
                "statement": r"""1. State and prove Brouwer's Fixed Point Theorem in one dimension: If $f: [a, b] \to [a, b]$ is continuous, then $f$ has a fixed point $c \in [a, b]$ such that $f(c) = c$.
2. Suppose $g: \mathbb{R} \to \mathbb{R}$ is continuous and satisfies $|g(x) - g(y)| \le k |x - y|$ for all $x, y \in \mathbb{R}$ with $0 \le k < 1$ (Contraction Mapping). Prove that $g$ has a unique fixed point in $\mathbb{R}$.
3. Prove that the antipodal temperature theorem holds on the equator: If temperature $T: S^1 \to \mathbb{R}$ is continuous around a circular equator, there exist two antipodal points with identical temperatures.""",
                "hints": [
                    "For part 1, consider h(x) = f(x) - x on [a, b] and apply Bolzano's IVT.",
                    "For part 2, use the Picard iteration x_{n+1} = g(x_n) and show it is a Cauchy sequence.",
                    "For part 3, let theta in [0, pi] and define D(theta) = T(theta + pi) - T(theta)."
                ],
                "solution": r"""### 1. One-Dimensional Brouwer Fixed Point Theorem
Let $f: [a, b] \to [a, b]$ be continuous.
Define the auxiliary function:
$$h(x) = f(x) - x$$
Since $f(x)$ is continuous and $x$ is continuous, $h$ is continuous on $[a, b]$.
We evaluate $h$ at the endpoints:
- At $x = a$: since $f(a) \in [a, b]$, $f(a) \ge a \implies h(a) = f(a) - a \ge 0$.
- At $x = b$: since $f(b) \in [a, b]$, $f(b) \le b \implies h(b) = f(b) - b \le 0$.

If $h(a) = 0$, then $f(a) = a$ and $a$ is a fixed point.
If $h(b) = 0$, then $f(b) = b$ and $b$ is a fixed point.
If $h(a) > 0$ and $h(b) < 0$, by Bolzano's Intermediate Value Theorem (Theorem 5.6), there exists $c \in (a, b)$ such that:
$$h(c) = 0 \iff f(c) - c = 0 \iff f(c) = c$$
In all cases, there exists $c \in [a, b]$ such that $f(c) = c$. $\blacksquare$

---

### 2. Banach Contraction Principle on $\mathbb{R}$
Let $g: \mathbb{R} \to \mathbb{R}$ with $|g(x) - g(y)| \le k |x - y|$ ($0 \le k < 1$).
- **Uniqueness:** If $c_1, c_2$ are fixed points, $|c_1 - c_2| = |g(c_1) - g(c_2)| \le k |c_1 - c_2|$.
  $(1 - k) |c_1 - c_2| \le 0$. Since $1 - k > 0$, $|c_1 - c_2| = 0 \implies c_1 = c_2$.
- **Existence:** Choose $x_0 \in \mathbb{R}$ arbitrarily, and define $x_{n+1} = g(x_n)$ for $n \ge 0$.
  By induction:
  $$|x_{n+1} - x_n| = |g(x_n) - g(x_{n-1})| \le k |x_n - x_{n-1}| \le \dots \le k^n |x_1 - x_0|$$
  For any $m > n$:
  $$|x_m - x_n| \le \sum_{j=n}^{m-1} |x_{j+1} - x_j| \le |x_1 - x_0| \sum_{j=n}^{m-1} k^j < |x_1 - x_0| \frac{k^n}{1 - k}$$
  Since $0 \le k < 1$, $k^n \to 0$ as $n \to \infty$.
  Thus $(x_n)$ is a Cauchy sequence in $\mathbb{R}$.
  By the Cauchy completeness of $\mathbb{R}$, $x_n \to c \in \mathbb{R}$.
  Taking limits: $c = \lim x_{n+1} = \lim g(x_n) = g(c)$ (by continuity).
  Thus $c$ is the unique fixed point. $\blacksquare$

---

### 3. Antipodal Temperature Theorem (Borsuk-Ulam on $S^1$)
Parameterize the equator by angle $\theta \in [0, 2\pi]$, identifying $\theta + 2\pi \equiv \theta$.
Define the temperature difference between antipodal points:
$$D(\theta) = T(\theta + \pi) - T(\theta) \quad \text{for } \theta \in [0, \pi]$$
Since $T$ is continuous, $D$ is continuous on $[0, \pi]$.
Evaluate at the endpoints:
$$D(0) = T(\pi) - T(0)$$
$$D(\pi) = T(2\pi) - T(\pi) = T(0) - T(\pi) = -(T(\pi) - T(0)) = -D(0)$$
- If $D(0) = 0$, then $T(\pi) = T(0)$, so $\theta = 0$ and $\theta = \pi$ are antipodal points with equal temperature.
- If $D(0) \ne 0$, then $D(0)$ and $D(\pi) = -D(0)$ have opposite signs!
By Bolzano's Intermediate Value Theorem, there exists $\theta^* \in (0, \pi)$ such that:
$$D(\theta^*) = 0 \iff T(\theta^* + \pi) = T(\theta^*)$$
The points $\theta^*$ and $\theta^* + \pi$ are antipodal and share identical temperatures. $\blacksquare$"""
            }
        ]
    }
    return u5

if __name__ == "__main__":
    u = get_unit5()
    print(f"Loaded Unit 5: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
