# -*- coding: utf-8 -*-
"""
build_ra_unit2.py
Constructs Unit 2: Topology of the Real Line: Open Sets, Compactness & Heine-Borel
"""

def get_unit2():
    u2 = {
        "number": 2,
        "title": "Topology of the Real Line: Open Sets, Compactness & Heine-Borel",
        "leadSummary": "Comprehensive topological analysis of the real line: open and closed sets, limit points, interior, boundary, closure, the Bolzano-Weierstrass theorem for bounded sets, open covers and the Heine-Borel compactness theorem, and topological connectedness.",
        "simulations": ["sim_ra_topology_heine_borel"],
        "sections": [
            {
                "secNumber": "2.1",
                "title": "Metric Structure of R: Open and Closed Sets, Neighborhoods & Limit Points",
                "content": r"""### 1. The Standard Metric on the Real Line

The topological structure of $\mathbb{R}$ is induced by the Euclidean metric (distance function):
$$d: \mathbb{R} \times \mathbb{R} \to [0, \infty), \quad d(x, y) = |x - y|$$
This distance function satisfies the three axioms of a metric:
1. **Positivity & Identity of Indiscernibles:** $d(x, y) \ge 0$, and $d(x, y) = 0 \iff x = y$.
2. **Symmetry:** $d(x, y) = d(y, x)$.
3. **Triangle Inequality:** $d(x, z) \le d(x, y) + d(y, z)$.

> **Definition 2.1 ($\epsilon$-Neighborhoods and Open Balls):**
> For any point $x_0 \in \mathbb{R}$ and radius $\epsilon > 0$, the **$\epsilon$-neighborhood** (or open ball) centered at $x_0$ is defined as:
> $$V_\epsilon(x_0) = B(x_0, \epsilon) = \{ x \in \mathbb{R} : |x - x_0| < \epsilon \} = (x_0 - \epsilon, x_0 + \epsilon)$$
> The **deleted $\epsilon$-neighborhood** is:
> $$V_\epsilon^*(x_0) = V_\epsilon(x_0) \setminus \{x_0\} = (x_0 - \epsilon, x_0) \cup (x_0, x_0 + \epsilon)$$

---

### 2. Open Sets and Their Fundamental Properties

> **Definition 2.2 (Open Set):**
> A subset $U \subseteq \mathbb{R}$ is called an **open set** if every point of $U$ is an interior point:
> $$\forall x \in U, \; \exists \epsilon > 0 \text{ such that } V_\epsilon(x) \subseteq U$$

> **Theorem 2.1 (Topological Properties of Open Sets in $\mathbb{R}$):**
> 1. The empty set $\emptyset$ and the whole space $\mathbb{R}$ are open sets.
> 2. The union of an arbitrary (finite or infinite) collection of open sets is open:
>    $$\text{If } \{U_\lambda\}_{\lambda \in \Lambda} \text{ are open, then } \bigcup_{\lambda \in \Lambda} U_\lambda \text{ is open.}$$
> 3. The intersection of any *finite* collection of open sets is open:
>    $$\text{If } U_1, U_2, \dots, U_n \text{ are open, then } \bigcap_{i=1}^n U_i \text{ is open.}$$

#### Rigorous Proof of Finite Intersection Property:
Let $x \in \bigcap_{i=1}^n U_i$.
Then $x \in U_i$ for each $i \in \{1, 2, \dots, n\}$.
Since each $U_i$ is open, there exist positive radii $\epsilon_i > 0$ such that $V_{\epsilon_i}(x) \subseteq U_i$.
Define:
$$\epsilon = \min \{ \epsilon_1, \epsilon_2, \dots, \epsilon_n \}$$
Since this is a minimum of finitely many strictly positive numbers, $\epsilon > 0$.
Now, for any $y \in V_\epsilon(x)$, $|y - x| < \epsilon \le \epsilon_i$ for all $i \in \{1, \dots, n\}$.
Hence $y \in V_{\epsilon_i}(x) \subseteq U_i$ for every $i$, which implies $y \in \bigcap_{i=1}^n U_i$.
Thus $V_\epsilon(x) \subseteq \bigcap_{i=1}^n U_i$, proving that the finite intersection is open. $\blacksquare$

> **Remark (Counterexample for Infinite Intersections):**
> An arbitrary intersection of open sets is not necessarily open.
> For example, let $U_n = \left(-\frac{1}{n}, \frac{1}{n}\right)$ for $n \in \mathbb{N}$.
> Each $U_n$ is an open interval. However:
> $$\bigcap_{n=1}^\infty U_n = \{0\}$$
> The single-point set $\{0\}$ is closed, not open!

---

### 3. Limit Points, Isolated Points & Closed Sets

> **Definition 2.3 (Limit Point / Accumulation Point):**
> Let $A \subseteq \mathbb{R}$. A point $p \in \mathbb{R}$ is a **limit point** (or accumulation point) of $A$ if every deleted neighborhood of $p$ contains at least one point of $A$:
> $$\forall \epsilon > 0, \; V_\epsilon^*(p) \cap A \ne \emptyset \iff (V_\epsilon(p) \setminus \{p\}) \cap A \ne \emptyset$$
> Note that $p$ need not be an element of $A$.
> The set of all limit points of $A$ is called the **derived set** of $A$, denoted $A'$.

> **Definition 2.4 (Isolated Point):**
> A point $a \in A$ is an **isolated point** of $A$ if there exists $\epsilon > 0$ such that $V_\epsilon(a) \cap A = \{a\}$. That is, $a \in A$ but $a \notin A'$.

> **Definition 2.5 (Closed Set):**
> A subset $F \subseteq \mathbb{R}$ is **closed** if its complement $\mathbb{R} \setminus F = F^c$ is open.

> **Theorem 2.2 (Characterization of Closed Sets via Limit Points):**
> A subset $F \subseteq \mathbb{R}$ is closed if and only if it contains all of its limit points:
> $$F \text{ is closed} \iff F' \subseteq F$$

#### Line-by-Line Proof:
$(\implies)$ Assume $F$ is closed, so $F^c$ is open.
Let $p \in F'$ be a limit point of $F$. Suppose for contradiction that $p \notin F$.
Then $p \in F^c$.
Since $F^c$ is open, there exists $\epsilon > 0$ such that $V_\epsilon(p) \subseteq F^c$.
This implies $V_\epsilon(p) \cap F = \emptyset$.
Consequently, $V_\epsilon^*(p) \cap F = \emptyset$, which contradicts the definition of $p$ being a limit point of $F$!
Therefore, $p \in F$, showing $F' \subseteq F$.

$(\impliedby)$ Assume $F' \subseteq F$. We must show that $F^c$ is open.
Let $x \in F^c$. Since $x \notin F$ and $F' \subseteq F$, $x \notin F'$.
Because $x$ is not a limit point of $F$, there exists some $\epsilon > 0$ such that:
$$V_\epsilon^*(x) \cap F = \emptyset \iff (V_\epsilon(x) \setminus \{x\}) \cap F = \emptyset$$
Since $x \notin F$, this implies $V_\epsilon(x) \cap F = \emptyset$, which means $V_\epsilon(x) \subseteq F^c$.
Thus every $x \in F^c$ is an interior point of $F^c$, so $F^c$ is open and $F$ is closed. $\blacksquare$"""
            },
            {
                "secNumber": "2.2",
                "title": "Interior, Boundary, Closure, Derived Sets & Dense Subsets",
                "content": r"""### 1. Interior, Exterior, and Boundary

> **Definition 2.6 (Interior, Exterior, Boundary):**
> Let $A \subseteq \mathbb{R}$.
> 1. The **interior** of $A$, denoted $\operatorname{int}(A)$ or $A^\circ$, is the set of all interior points of $A$:
>    $$\operatorname{int}(A) = \{ x \in A : \exists \epsilon > 0 \text{ s.t. } V_\epsilon(x) \subseteq A \}$$
>    It is the largest open set contained within $A$, and is equal to the union of all open sets contained in $A$.
> 2. The **exterior** of $A$, denoted $\operatorname{ext}(A)$, is the interior of its complement: $\operatorname{ext}(A) = \operatorname{int}(A^c)$.
> 3. The **boundary** of $A$, denoted $\partial A$ or $\operatorname{bd}(A)$, is the set of points whose neighborhoods intersect both $A$ and $A^c$:
>    $$\partial A = \{ x \in \mathbb{R} : \forall \epsilon > 0, \; V_\epsilon(x) \cap A \ne \emptyset \text{ and } V_\epsilon(x) \cap A^c \ne \emptyset \}$$

> **Theorem 2.3 (Partition of the Real Line):**
> For any subset $A \subseteq \mathbb{R}$, the ambient space decomposes into the disjoint union:
> $$\mathbb{R} = \operatorname{int}(A) \cup \partial A \cup \operatorname{ext}(A)$$

---

### 2. Topological Closure and Kuratowski Axioms

> **Definition 2.7 (Closure):**
> The **closure** of $A$, denoted $\overline{A}$ or $\operatorname{cl}(A)$, is defined as the union of $A$ and its derived set:
> $$\overline{A} = A \cup A'$$

> **Theorem 2.4 (Properties of Closure):**
> 1. $\overline{A}$ is closed.
> 2. $\overline{A}$ is the smallest closed set containing $A$:
>    $$\overline{A} = \bigcap \{ F \subseteq \mathbb{R} : A \subseteq F \text{ and } F \text{ is closed} \}$$
> 3. $A$ is closed if and only if $A = \overline{A}$.
> 4. $\overline{A} = \operatorname{int}(A) \cup \partial A$.
> 5. A point $x \in \overline{A}$ if and only if every neighborhood $V_\epsilon(x)$ contains at least one point of $A$:
>    $$x \in \overline{A} \iff \forall \epsilon > 0, \; V_\epsilon(x) \cap A \ne \emptyset$$

---

### 3. Dense Sets and Nowhere Dense Sets

> **Definition 2.8 (Dense and Nowhere Dense Subsets):**
> 1. A subset $D \subseteq \mathbb{R}$ is **dense** in $\mathbb{R}$ if $\overline{D} = \mathbb{R}$.
>    Equivalently, every non-empty open interval $(a, b)$ contains a point of $D$.
> 2. A subset $E \subseteq \mathbb{R}$ is **nowhere dense** (or rare) if the interior of its closure is empty:
>    $$\operatorname{int}(\overline{E}) = \emptyset$$

#### Classical Examples:
- The rationals $\mathbb{Q}$ and irrationals $\mathbb{R} \setminus \mathbb{Q}$ are both dense in $\mathbb{R}$: $\overline{\mathbb{Q}} = \mathbb{R}$ and $\overline{\mathbb{R} \setminus \mathbb{Q}} = \mathbb{R}$.
- The integers $\mathbb{Z}$ have $\overline{\mathbb{Z}} = \mathbb{Z}$ and $\operatorname{int}(\mathbb{Z}) = \emptyset$, so $\mathbb{Z}$ is nowhere dense in $\mathbb{R}$.
- The Cantor ternary set $\mathcal{C}$ is closed and contains no intervals: $\operatorname{int}(\mathcal{C}) = \emptyset$, making it nowhere dense."""
            },
            {
                "secNumber": "2.3",
                "title": "The Bolzano-Weierstrass Theorem for Sets & Accumulation Points",
                "content": r"""### 1. Infinite Sets in Bounded Regions

A fundamental question asked by Bernard Bolzano and Karl Weierstrass was: what conditions guarantee that a set has at least one accumulation point? Finite sets clearly cannot have accumulation points, since any finite set can be isolated by taking $\epsilon$ smaller than the minimal distance between any two distinct points. What happens when an infinite set is confined to a bounded domain?

> **Theorem 2.5 (Bolzano-Weierstrass Theorem for Sets):**
> Every bounded, infinite subset of $\mathbb{R}$ has at least one limit point in $\mathbb{R}$.

#### Complete Rigorous Proof (Bisection Method & Completeness):
Let $S \subset \mathbb{R}$ be an infinite and bounded set.
Since $S$ is bounded, there exists a closed bounded interval $I_0 = [a_0, b_0]$ such that $S \subseteq I_0$.
Let $L_0 = b_0 - a_0 > 0$ be the length of $I_0$.

We construct a nested sequence of closed intervals $\{I_n\}_{n=0}^\infty$ by induction:
1. Divide $I_0 = [a_0, b_0]$ at its midpoint $m_0 = \frac{a_0 + b_0}{2}$ into two equal subintervals:
   $$[a_0, m_0] \quad \text{and} \quad [m_0, b_0]$$
2. Since $S \cap I_0$ is infinite, at least one of these two subintervals must contain infinitely many points of $S$ (if both were finite, their union would be finite, a contradiction).
3. Select one subinterval containing infinitely many points of $S$, and denote it $I_1 = [a_1, b_1]$. Its length is $L_1 = \frac{L_0}{2}$.
4. Continuing this bisection inductively, for each $n \in \mathbb{N}$, we obtain a closed interval $I_n = [a_n, b_n]$ satisfying:
   - $I_{n} \subseteq I_{n-1}$.
   - $I_n$ contains infinitely many points of $S$.
   - The length of $I_n$ is $b_n - a_n = \frac{b_0 - a_0}{2^n}$.

Now, observe the sequence of left endpoints $\{a_n\}_{n=0}^\infty$:
- Since $I_n \subseteq I_{n-1}$, we have $a_{n-1} \le a_n \le b_n \le b_0$ for all $n$.
- Thus, the set $A = \{a_n : n \ge 0\}$ is non-empty and bounded above by $b_0$.
By the Completeness Axiom, $A$ has a supremum:
$$p = \sup \{a_n : n \ge 0\} \in \mathbb{R}$$
Similarly, $p = \inf \{b_n : n \ge 0\}$, and by the Nested Interval Property:
$$\bigcap_{n=0}^\infty I_n = \{p\}$$

We claim that $p$ is a limit point of $S$.
Let $\epsilon > 0$ be arbitrary.
By the Archimedean property, choose $N \in \mathbb{N}$ large enough such that:
$$\frac{b_0 - a_0}{2^N} < \epsilon$$
Since $p \in I_N = [a_N, b_N]$ and the length of $I_N$ is strictly less than $\epsilon$, for any $x \in I_N$:
$$|x - p| \le b_N - a_N < \epsilon \implies I_N \subset V_\epsilon(p)$$
Because $I_N$ contains infinitely many points of $S$, the neighborhood $V_\epsilon(p)$ contains infinitely many points of $S$.
In particular, $V_\epsilon^*(p) \cap S$ contains infinitely many points, so it is certainly non-empty.
Since $\epsilon > 0$ was arbitrary, $p$ is a limit point of $S$. $\blacksquare$"""
            },
            {
                "secNumber": "2.4",
                "title": "Compact Sets in R & The Heine-Borel Covering Theorem",
                "content": r"""### 1. Open Covers and Topological Compactness

In classical Euclidean analysis, compactness is the ultimate finiteness property. It allows mathematicians to pass from local properties (which hold in small $\epsilon$-neighborhoods of points) to global properties (which hold uniformly over an entire set).

> **Definition 2.9 (Open Cover and Subcover):**
> Let $K \subseteq \mathbb{R}$.
> 1. A collection of open sets $\mathcal{U} = \{ U_\alpha \}_{\alpha \in \Lambda}$ is an **open cover** of $K$ if:
>    $$K \subseteq \bigcup_{\alpha \in \Lambda} U_\alpha$$
> 2. A **subcover** is a sub-collection $\mathcal{U}' \subseteq \mathcal{U}$ that still covers $K$:
>    $$K \subseteq \bigcup_{i=1}^m U_{\alpha_i}$$
> 3. If $\mathcal{U}'$ contains only finitely many sets, it is a **finite subcover**.

> **Definition 2.10 (Compact Set):**
> A subset $K \subseteq \mathbb{R}$ is **compact** if every open cover of $K$ has a finite subcover.

---

### 2. The Heine-Borel Theorem

> **Theorem 2.6 (Heine-Borel Theorem):**
> A subset $K \subseteq \mathbb{R}$ is compact if and only if $K$ is **closed and bounded**.

#### Line-by-Line Proof:
$(\implies)$ **Compactness implies Closed and Bounded.**
1. **$K$ is bounded:**
   For each $n \in \mathbb{N}$, define the open interval $U_n = (-n, n)$.
   Then $\bigcup_{n=1}^\infty U_n = \mathbb{R} \supset K$. Thus $\{U_n\}_{n=1}^\infty$ is an open cover of $K$.
   Since $K$ is compact, there exists a finite subcover:
   $$K \subseteq U_{n_1} \cup U_{n_2} \cup \dots \cup U_{n_k}$$
   Let $M = \max \{n_1, n_2, \dots, n_k\}$. Then $K \subseteq (-M, M)$, which proves that $K$ is bounded.
2. **$K$ is closed:**
   We show $K^c = \mathbb{R} \setminus K$ is open.
   Let $y \in K^c$. For each $x \in K$, since $x \ne y$, let $r_x = \frac{|x - y|}{2} > 0$.
   Define the disjoint open neighborhoods:
   $$V_x = B\left(x, r_x\right) \quad \text{and} \quad W_x = B\left(y, r_x\right)$$
   Notice that $V_x \cap W_x = \emptyset$.
   The family $\{V_x\}_{x \in K}$ forms an open cover of $K$: $K \subseteq \bigcup_{x \in K} V_x$.
   Since $K$ is compact, there exists a finite subcover:
   $$K \subseteq V_{x_1} \cup V_{x_2} \cup \dots \cup V_{x_m}$$
   Define $W = \bigcap_{i=1}^m W_{x_i}$.
   Since $W$ is a finite intersection of open balls centered at $y$, $W$ is an open neighborhood of $y$.
   Moreover, for each $i \in \{1, \dots, m\}$, $W \cap V_{x_i} \subseteq W_{x_i} \cap V_{x_i} = \emptyset$.
   Therefore, $W \cap \left(\bigcup_{i=1}^m V_{x_i}\right) = \emptyset \implies W \cap K = \emptyset$.
   Hence $W \subseteq K^c$, proving that $K^c$ is open. Thus $K$ is closed.

$(\impliedby)$ **Closed and Bounded implies Compact.**
Let $K \subseteq \mathbb{R}$ be closed and bounded.
Since $K$ is bounded, there exists a closed bounded interval $[a, b]$ such that $K \subseteq [a, b]$.
We first prove that the closed interval $[a, b]$ is compact (this is the core lemma):

*Lemma:* Every closed interval $[a, b]$ is compact.
*Proof of Lemma:* Let $\mathcal{U} = \{U_\alpha\}$ be an open cover of $[a, b]$. Define the set:
$$S = \{ x \in [a, b] : [a, x] \text{ is covered by a finite sub-collection of } \mathcal{U} \}$$
- $a \in S$ because $a \in [a, b]$, so $a \in U_{\alpha_0}$ for some $\alpha_0$, hence $[a, a] = \{a\} \subseteq U_{\alpha_0}$. Thus $S \ne \emptyset$.
- $S$ is bounded above by $b$.
By the Completeness Axiom, $c = \sup S$ exists and $a \le c \le b$.
Since $c \in [a, b]$, $c \in U_{\alpha_c}$ for some open set $U_{\alpha_c} \in \mathcal{U}$.
Since $U_{\alpha_c}$ is open, there is $\epsilon > 0$ such that $(c - \epsilon, c + \epsilon) \subseteq U_{\alpha_c}$.
By the definition of supremum, there exists $x_1 \in S$ with $c - \epsilon < x_1 \le c$.
Since $x_1 \in S$, $[a, x_1]$ is covered by finitely many sets $U_1, \dots, U_k \in \mathcal{U}$.
Then $[a, x_1] \cup (c - \epsilon, c + \epsilon)$ is covered by $\{U_1, \dots, U_k, U_{\alpha_c}\}$.
Thus, any point $x \in [a, c + \epsilon) \cap [a, b]$ has $[a, x]$ covered by finitely many sets.
If $c < b$, we could choose $x \in (c, c + \epsilon) \cap [a, b]$, contradicting that $c = \sup S$.
Hence $c = b$. Furthermore, $b \in S$ because $[a, b]$ is covered by $\{U_1, \dots, U_k, U_{\alpha_c}\}$.
Thus $[a, b]$ is compact.

Finally, since $K \subseteq [a, b]$ is closed, $K^c$ is open.
If $\mathcal{U}$ is an open cover of $K$, then $\mathcal{U} \cup \{K^c\}$ is an open cover of $[a, b]$.
Since $[a, b]$ is compact, there exists a finite subcover of $[a, b]$ from $\mathcal{U} \cup \{K^c\}$.
Discarding $K^c$ leaves a finite sub-collection of $\mathcal{U}$ that still covers $K$.
Therefore, $K$ is compact. $\blacksquare$"""
            },
            {
                "secNumber": "2.5",
                "title": "Connectedness, Separated Sets & Connected Subsets of the Real Line",
                "content": r"""### 1. Topological Connectedness and Separations

> **Definition 2.11 (Separated Sets and Connectedness):**
> 1. Two non-empty subsets $A, B \subset \mathbb{R}$ are **separated** if:
>    $$\overline{A} \cap B = \emptyset \quad \text{and} \quad A \cap \overline{B} = \emptyset$$
> 2. A subset $E \subseteq \mathbb{R}$ is **disconnected** (or separated) if it can be written as the union of two non-empty separated sets:
>    $$E = A \cup B, \quad A \ne \emptyset, \; B \ne \emptyset, \quad \overline{A} \cap B = \emptyset, \quad A \cap \overline{B} = \emptyset$$
> 3. A subset $E \subseteq \mathbb{R}$ is **connected** if it is not disconnected.

> **Remark (Clopen Sets):**
> An equivalent definition states that a subset $E$ is connected if the only subsets of $E$ that are both open and closed in the subspace topology of $E$ are $\emptyset$ and $E$ itself. In $\mathbb{R}$, the only sets that are both open and closed (clopen) are $\emptyset$ and $\mathbb{R}$.

---

### 2. Characterization of Connected Subsets of $\mathbb{R}$

The geometry of the real line imposes a very strict condition on connectedness: a subset of $\mathbb{R}$ is connected if and only if it has no "gaps" — that is, if it is an interval!

> **Theorem 2.7 (Connected Subsets of $\mathbb{R}$ are Intervals):**
> A subset $E \subseteq \mathbb{R}$ is connected if and only if $E$ is an interval.
> That is, $E$ has the intermediate point property:
> $$\forall x, y \in E \text{ with } x < y, \; [x, y] \subseteq E$$

#### Complete Proof:
$(\impliedby)$ We prove that if $E$ satisfies the intermediate point property, then $E$ is connected.
Assume for contradiction that $E$ is disconnected.
Then $E = A \cup B$ where $A, B$ are non-empty and separated ($\overline{A} \cap B = \emptyset = A \cap \overline{B}$).
Choose $a \in A$ and $b \in B$. Without loss of generality, assume $a < b$.
Since $E$ has the intermediate point property, $[a, b] \subseteq E$.
Define the set:
$$S = A \cap [a, b]$$
Since $a \in S$, $S \ne \emptyset$.
Moreover, $S$ is bounded above by $b$.
By the Completeness Axiom, $c = \sup S$ exists, and $a \le c \le b$.
Thus $c \in [a, b] \subseteq E = A \cup B$.
Therefore, either $c \in A$ or $c \in B$.

- **Case 1: $c \in A$.**
  Since $\overline{A} \cap B = \emptyset$, $c \notin \overline{B}$.
  Thus $c \ne b$, so $c < b$.
  Since $c \notin \overline{B}$, there exists $\epsilon > 0$ such that $(c - \epsilon, c + \epsilon) \cap B = \emptyset$.
  Can choose $\epsilon < b - c$, so $(c, c + \epsilon) \subseteq [a, b]$.
  Since $(c, c + \epsilon) \cap B = \emptyset$ and $[a, b] \subseteq A \cup B$, we must have $(c, c + \epsilon) \subseteq A$.
  This contradicts that $c = \sup S$, because any point in $(c, c + \epsilon)$ is an element of $S$ strictly greater than $c$!

- **Case 2: $c \in B$.**
  Since $A \cap \overline{B} = \emptyset$, $c \notin \overline{A}$.
  Thus $c \ne a$ (since $a \in A$).
  Since $c \notin \overline{A}$, there exists $\epsilon > 0$ such that $(c - \epsilon, c + \epsilon) \cap A = \emptyset$.
  This means that for all $x \in (c - \epsilon, c]$, $x \notin A$.
  Hence $c - \epsilon$ is an upper bound for $S = A \cap [a, b]$, which strictly contradicts that $c = \sup S$!

In both cases we reach a contradiction. Hence $E$ must be connected.

$(\implies)$ Suppose $E$ is connected. Assume for contradiction that $E$ is not an interval.
Then there exist $x, y \in E$ with $x < y$, and some point $z \in (x, y)$ such that $z \notin E$.
Define:
$$A = E \cap (-\infty, z) \quad \text{and} \quad B = E \cap (z, \infty)$$
Since $x \in A$ and $y \in B$, both $A$ and $B$ are non-empty, and $E = A \cup B$.
Furthermore, $\overline{A} \subseteq (-\infty, z]$ so $\overline{A} \cap B \subseteq (-\infty, z] \cap (z, \infty) = \emptyset$.
Similarly, $A \cap \overline{B} \subseteq (-\infty, z) \cap [z, \infty) = \emptyset$.
Thus $A$ and $B$ are separated, so $E$ is disconnected, contradicting the premise.
Therefore, $E$ must be an interval. $\blacksquare$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational / Problem 2.1",
                "title": "Topological Classification: Interior, Boundary, Closure & Limit Points",
                "statement": r"""Consider the following subset of the real line:
$$A = (0, 1] \cup \{2\} \cup ((3, 4) \cap \mathbb{Q})$$
1. Determine whether $A$ is open, closed, or neither.
2. Find the set of all limit points $A'$ (the derived set).
3. Find the interior $\operatorname{int}(A)$, the closure $\overline{A}$, and the boundary $\partial A$.
4. Identify any isolated points of $A$.""",
                "hints": [
                    "Recall that the set of limit points of (3, 4) \\cap Q is [3, 4] due to density of rationals.",
                    "An isolated point is a point in A that is not in A'."
                ],
                "solution": r"""### 1. Determining Openness and Closedness

To determine if $A$ is open:
- A point $x \in A$ must have an $\epsilon$-neighborhood contained entirely in $A$.
- Consider $x = 1 \in A$. For any $\epsilon > 0$, the interval $(1, 1 + \epsilon)$ contains points not in $A$. Hence $1 \notin \operatorname{int}(A)$.
- Similarly, $x = 2 \in A$ is an isolated point; no open interval around 2 is contained in $A$.
- For any rational point $q \in (3, 4) \cap \mathbb{Q}$, any neighborhood $V_\epsilon(q)$ contains irrational numbers, which do not belong to $A$.
Thus $A$ is **not open**.

To determine if $A$ is closed:
- A set is closed if and only if it contains all of its limit points ($A' \subseteq A$).
- As shown below, $0 \in A'$ but $0 \notin A$.
- Also, any irrational number in $(3, 4)$ is a limit point of $(3, 4) \cap \mathbb{Q}$, but does not belong to $A$.
Thus $A$ does not contain all its limit points, so $A$ is **not closed**.
Conclusion: $A$ is **neither open nor closed**.

---

### 2. Finding the Derived Set $A'$
We find the limit points of each component:
- Limit points of $(0, 1]$: $[0, 1]$.
- Limit points of $\{2\}$: $\emptyset$ (finite sets have no limit points).
- Limit points of $(3, 4) \cap \mathbb{Q}$: since $\mathbb{Q}$ is dense in $\mathbb{R}$, every point in $[3, 4]$ is a limit point.
Taking the union of limit points:
$$A' = [0, 1] \cup [3, 4]$$

---

### 3. Finding Interior, Closure, and Boundary
- **Interior $\operatorname{int}(A)$:**
  - $(0, 1)$ contains only interior points.
  - The point $1$ is not interior.
  - The point $2$ is isolated, hence not interior.
  - The set $(3, 4) \cap \mathbb{Q}$ contains no open intervals (every open interval contains irrationals).
  Therefore:
  $$\operatorname{int}(A) = (0, 1)$$

- **Closure $\overline{A}$:**
  By definition, $\overline{A} = A \cup A'$:
  $$\overline{A} = [0, 1] \cup \{2\} \cup [3, 4]$$

- **Boundary $\partial A$:**
  Using $\partial A = \overline{A} \setminus \operatorname{int}(A)$:
  $$\partial A = ([0, 1] \cup \{2\} \cup [3, 4]) \setminus (0, 1) = \{0, 1, 2\} \cup [3, 4]$$

---

### 4. Isolated Points of $A$
A point $p \in A$ is isolated if $p \in A \setminus A'$.
- Points in $(0, 1]$ are in $A'$, so they are not isolated.
- The point $2 \in A$ but $2 \notin A'$. Thus $2$ is an isolated point.
- Points in $(3, 4) \cap \mathbb{Q}$ are all limit points (in $[3, 4] = A'$), so they are not isolated.
Therefore, the only isolated point is $\{2\}$."""
            },
            {
                "tier": "Advanced / Problem 2.2",
                "title": "Comprehensive Construction and Analytical Rigor of the Cantor Ternary Set",
                "statement": r"""The Cantor Ternary Set $\mathcal{C} \subset [0, 1]$ is constructed by setting $C_0 = [0, 1]$ and inductively removing the open middle third of each remaining interval:
$$C_{n+1} = \frac{1}{3} C_n \cup \left( \frac{2}{3} + \frac{1}{3} C_n \right), \quad \mathcal{C} = \bigcap_{n=0}^\infty C_n$$
1. Prove that $\mathcal{C}$ is compact.
2. Prove that the total length (Lebesgue measure) of the removed intervals is 1, so $\operatorname{m}(\mathcal{C}) = 0$.
3. Prove that $\mathcal{C}$ is nowhere dense: $\operatorname{int}(\mathcal{C}) = \emptyset$.
4. Prove that $\mathcal{C}$ is uncountable by establishing a surjection onto $[0, 1]$ via ternary representations.""",
                "hints": [
                    "For compactness, show C is bounded and express C as an intersection of closed sets.",
                    "For total length, sum the geometric series: 1/3 + 2/9 + 4/27 + ...",
                    "For uncountability, represent elements in base 3 using only digits 0 and 2."
                ],
                "solution": r"""### 1. Proof that $\mathcal{C}$ is Compact

$C_0 = [0, 1]$ is closed and bounded.
At each step $n$, $C_n$ is a finite union of $2^n$ disjoint closed intervals:
$$C_n = \bigcup_{k=1}^{2^n} I_{n, k}$$
Since a finite union of closed sets is closed, each $C_n$ is closed in $\mathbb{R}$.
The Cantor set $\mathcal{C} = \bigcap_{n=0}^\infty C_n$ is an arbitrary intersection of closed sets, so $\mathcal{C}$ is **closed**.
Furthermore, $\mathcal{C} \subset [0, 1]$, so $\mathcal{C}$ is **bounded**.
By the Heine-Borel Theorem (Theorem 2.6), since $\mathcal{C}$ is closed and bounded in $\mathbb{R}$, $\mathcal{C}$ is **compact**. $\blacksquare$

---

### 2. Measure of the Cantor Set
At step 1, we remove 1 interval of length $\frac{1}{3}$.
At step 2, we remove 2 intervals of length $\frac{1}{3^2}$.
At step $n$, we remove $2^{n-1}$ intervals of length $\frac{1}{3^n}$.
The total length $L$ of the removed open intervals is given by the geometric series:
$$L = \sum_{n=1}^\infty \frac{2^{n-1}}{3^n} = \frac{1}{3} \sum_{k=0}^\infty \left(\frac{2}{3}\right)^k = \frac{1}{3} \cdot \frac{1}{1 - 2/3} = \frac{1}{3} \cdot 3 = 1$$
Since the initial interval $[0, 1]$ has length 1 and the removed disjoint intervals have total length 1, the Lebesgue measure of the Cantor set is:
$$\operatorname{m}(\mathcal{C}) = 1 - 1 = 0 \quad \blacksquare$$

---

### 3. Proof that $\mathcal{C}$ is Nowhere Dense
We must show $\operatorname{int}(\overline{\mathcal{C}}) = \emptyset$. Since $\mathcal{C}$ is closed, $\overline{\mathcal{C}} = \mathcal{C}$, so we must prove $\operatorname{int}(\mathcal{C}) = \emptyset$.
Suppose for contradiction that $\operatorname{int}(\mathcal{C}) \ne \emptyset$.
Then there exists an open interval $(a, b) \subseteq \mathcal{C}$ with $b - a = \delta > 0$.
Recall that at stage $n$, $C_n$ consists of $2^n$ intervals, each of length $\left(\frac{1}{3}\right)^n$.
By the Archimedean property, choose $n \in \mathbb{N}$ sufficiently large that:
$$\left(\frac{1}{3}\right)^n < \delta$$
Since $(a, b) \subseteq \mathcal{C} \subseteq C_n$, the interval $(a, b)$ must be completely contained within one of the constituent intervals of $C_n$.
However, the maximum length of any interval in $C_n$ is $\left(\frac{1}{3}\right)^n < \delta = b - a$, which is impossible!
Therefore, $\mathcal{C}$ contains no open interval, so $\operatorname{int}(\mathcal{C}) = \emptyset$.
Thus $\mathcal{C}$ is nowhere dense in $\mathbb{R}$. $\blacksquare$

---

### 4. Proof of Uncountability (Ternary Representation)
Every number $x \in [0, 1]$ can be written in base 3 (ternary):
$$x = \sum_{k=1}^\infty \frac{a_k}{3^k}, \quad a_k \in \{0, 1, 2\}$$
The points removed at step 1 are those with $a_1 = 1$ in their non-terminating ternary expansion.
At step $n$, the points removed are those requiring $a_n = 1$.
Therefore, a point $x \in [0, 1]$ belongs to the Cantor set $\mathcal{C}$ if and only if it possesses a ternary expansion using **only the digits 0 and 2**:
$$\mathcal{C} = \left\{ x = \sum_{k=1}^\infty \frac{a_k}{3^k} : a_k \in \{0, 2\} \right\}$$
Define a map $\phi: \mathcal{C} \to [0, 1]$ by replacing each digit 2 with 1 and interpreting the result as a binary number:
$$\phi\left( \sum_{k=1}^\infty \frac{a_k}{3^k} \right) = \sum_{k=1}^\infty \frac{a_k / 2}{2^k}, \quad \text{where } \frac{a_k}{2} \in \{0, 1\}$$
Since every number in $[0, 1]$ has a binary representation using digits $\{0, 1\}$, the function $\phi$ is **surjective** from $\mathcal{C}$ onto $[0, 1]$.
Because $[0, 1]$ is uncountable (Cantor's Theorem 1.8), any set that maps surjectively onto $[0, 1]$ must also be uncountable.
Thus, $|\mathcal{C}| \ge |[0, 1]| = \mathfrak{c}$, proving that $\mathcal{C}$ is uncountable! $\blacksquare$"""
            },
            {
                "tier": "Honors / Problem 2.3",
                "title": "Comprehensive Proof of the Heine-Borel Theorem & The Finite Intersection Characterization",
                "statement": r"""1. State the Finite Intersection Property (FIP) definition of compactness for topological spaces.
2. Prove that a metric space $(X, d)$ is compact if and only if every family of closed sets with the Finite Intersection Property has a non-empty intersection.
3. Use the Heine-Borel theorem and the FIP to deduce Cantor's Intersection Theorem: If $\{K_n\}_{n=1}^\infty$ is a decreasing sequence of non-empty compact sets in $\mathbb{R}$ ($K_{n+1} \subseteq K_n$), then:
   $$\bigcap_{n=1}^\infty K_n \ne \emptyset$$""",
                "hints": [
                    "Use De Morgan's laws to translate between open covers and collections of closed sets.",
                    "For Cantor's intersection theorem, show that any finite subcollection of {K_n} has non-empty intersection."
                ],
                "solution": r"""### 1. Statement of the Finite Intersection Property (FIP)

A collection of sets $\mathcal{F} = \{ F_\alpha \}_{\alpha \in \Lambda}$ has the **Finite Intersection Property (FIP)** if the intersection of any finite sub-collection of $\mathcal{F}$ is non-empty:
$$\forall \{\alpha_1, \alpha_2, \dots, \alpha_k\} \subseteq \Lambda, \quad \bigcap_{i=1}^k F_{\alpha_i} \ne \emptyset$$

---

### 2. Proof of Equivalence: Open Covers vs. FIP of Closed Sets

**Assertion:** A topological space $X$ is compact if and only if for every collection of closed sets $\mathcal{F} = \{F_\alpha\}_{\alpha \in \Lambda}$ possessing the FIP, $\bigcap_{\alpha \in \Lambda} F_\alpha \ne \emptyset$.

#### Proof:
We prove the contrapositive in both directions using De Morgan's laws.
For any collection $\mathcal{F} = \{F_\alpha\}_{\alpha \in \Lambda}$ of closed sets, define the collection of open sets $\mathcal{U} = \{U_\alpha\}_{\alpha \in \Lambda}$ where $U_\alpha = X \setminus F_\alpha = F_\alpha^c$.

By De Morgan's Laws:
$$\bigcap_{\alpha \in \Lambda} F_\alpha = \emptyset \iff \left( \bigcap_{\alpha \in \Lambda} F_\alpha \right)^c = X \iff \bigcup_{\alpha \in \Lambda} U_\alpha = X$$
Thus, $\bigcap_{\alpha \in \Lambda} F_\alpha = \emptyset$ if and only if $\{U_\alpha\}$ is an open cover of $X$.

Similarly, for any finite sub-collection $\{\alpha_1, \dots, \alpha_k\} \subseteq \Lambda$:
$$\bigcap_{i=1}^k F_{\alpha_i} = \emptyset \iff \bigcup_{i=1}^k U_{\alpha_i} = X$$
Thus, a finite sub-collection has empty intersection if and only if the corresponding open sets form a finite subcover of $X$.

Now:
- $X$ is compact $\iff$ every open cover $\{U_\alpha\}$ has a finite subcover $\bigcup_{i=1}^k U_{\alpha_i} = X$.
- Taking the contrapositive: if no finite sub-collection covers $X$ ($\bigcup_{i=1}^k U_{\alpha_i} \ne X$ for all finite subsets), then $\{U_\alpha\}$ cannot be a valid open cover ($\bigcup_{\alpha \in \Lambda} U_\alpha \ne X$).
- Translating through complements: if every finite intersection of closed sets is non-empty ($\bigcap_{i=1}^k F_{\alpha_i} \ne \emptyset$, i.e., $\mathcal{F}$ has the FIP), then the total intersection cannot be empty:
$$\bigcap_{\alpha \in \Lambda} F_\alpha \ne \emptyset$$
This completes the equivalence proof. $\blacksquare$

---

### 3. Proof of Cantor's Intersection Theorem

Let $\{K_n\}_{n=1}^\infty$ be a nested sequence of non-empty compact subsets of $\mathbb{R}$:
$$K_1 \supseteq K_2 \supseteq K_3 \supseteq \dots \supseteq K_n \supseteq K_{n+1} \supseteq \dots$$
By the Heine-Borel Theorem, each $K_n$ is closed and bounded.
Since each $K_n \subseteq K_1$, we can view all $K_n$ as closed subsets of the compact space $K_1$.

Consider the family of closed sets $\mathcal{F} = \{K_n\}_{n=1}^\infty$ within $K_1$.
Let $\{n_1, n_2, \dots, n_k\}$ be any finite set of indices, and let $m = \max\{n_1, \dots, n_k\}$.
Since the sets are nested ($K_{j} \supseteq K_m$ for all $j \le m$):
$$\bigcap_{i=1}^k K_{n_i} = K_m$$
Since each $K_n$ is given to be non-empty, $K_m \ne \emptyset$.
Thus, any finite intersection of sets from $\mathcal{F}$ is non-empty!
This means the family $\mathcal{F}$ satisfies the **Finite Intersection Property** on the compact space $K_1$.

By Part 2, since $K_1$ is compact, the entire infinite intersection must be non-empty:
$$\bigcap_{n=1}^\infty K_n \ne \emptyset \quad \blacksquare$$"""
            }
        ]
    }
    return u2

if __name__ == "__main__":
    u = get_unit2()
    print(f"Loaded Unit 2: {u['title']} with {len(u['sections'])} sections and {len(u['problems'])} problems.")
