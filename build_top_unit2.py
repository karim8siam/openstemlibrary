# -*- coding: utf-8 -*-
"""
build_top_unit2.py
Constructs Unit 2: Topological Spaces, Bases, Subbases & Neighborhood Systems
"""

def get_unit2():
    u2 = {
        "number": 2,
        "title": "Topological Spaces, Bases, Subbases & Neighborhood Systems",
        "leadSummary": "Axiomatic foundations of general topology: definition of topological spaces, comparison of topologies (coarser and finer), classical non-metric topologies (co-finite, co-countable, discrete, indiscrete, Sierpiński), closed sets, interior, closure, boundary, Kuratowski Closure Axioms, neighborhood systems and filters, accumulation and derived points, topological bases and subbases, the Basis Criterion Theorem, and the subspace (relative) topology.",
        "simulations": ["sim_top_closure_interior_boundary"],
        "sections": [
            {
                "secNumber": "2.1",
                "title": "Axiomatic Definition of Topological Spaces & Comparison of Topologies",
                "content": r"""### 1. The Axioms of a Topological Space

Felix Hausdorff in 1914 and Kazimierz Kuratowski in 1922 abstracted metric open sets into the general axiomatic framework of topology.

> **Definition 2.1 (Topological Space):**
> Let $X$ be a non-empty set. A **topology** on $X$ is a collection $\mathcal{T}$ of subsets of $X$ (whose members are called **open sets**) satisfying:
> 1. The empty set $\emptyset$ and the whole space $X$ belong to $\mathcal{T}$:
>    $$\emptyset \in \mathcal{T} \quad \text{and} \quad X \in \mathcal{T}$$
> 2. The union of any arbitrary family of sets in $\mathcal{T}$ belongs to $\mathcal{T}$:
>    $$\bigcup_{\alpha \in I} U_\alpha \in \mathcal{T} \quad \text{whenever } U_\alpha \in \mathcal{T} \text{ for all } \alpha \in I$$
> 3. The intersection of any finite collection of sets in $\mathcal{T}$ belongs to $\mathcal{T}$:
>    $$\bigcap_{i=1}^n U_i \in \mathcal{T} \quad \text{whenever } U_1, \dots, U_n \in \mathcal{T}$$
>
> The pair $(X, \mathcal{T})$ is called a **topological space**.

---

### 2. Classical Non-Metric Topologies

> **Example 2.1 (Discrete and Indiscrete Topologies):**
> - **Discrete Topology $\mathcal{T}_{\text{disc}} = \mathcal{P}(X)$:** Every subset of $X$ is open.
> - **Indiscrete (Trivial) Topology $\mathcal{T}_{\text{ind}} = \{\emptyset, X\}$:** Only $\emptyset$ and $X$ are open.

> **Example 2.2 (Co-finite Topology / Finite Complement Topology):**
> Let $X$ be any set. Define:
> $$\mathcal{T}_{\text{cof}} = \{U \subseteq X : X \setminus U \text{ is finite}\} \cup \{\emptyset\}$$
> On an infinite set $X$, $\mathcal{T}_{\text{cof}}$ is **not metrizable**! Any two non-empty open sets must intersect, so disjoint open neighborhoods cannot exist for distinct points!

> **Example 2.3 (Co-countable Topology):**
> $$\mathcal{T}_{\text{coc}} = \{U \subseteq X : X \setminus U \text{ is countable}\} \cup \{\emptyset\}$$
> On an uncountable set like $\mathbb{R}$, sequences converge if and only if they are eventually constant.

> **Example 2.4 (Sierpiński Space):**
> On the two-point set $X = \{0, 1\}$, the topology $\mathcal{T} = \{\emptyset, \{1\}, \{0, 1\}\}$ is called the **Sierpiński topology**. The point $1$ is open but not closed, while $0$ is closed but not open!

---

### 3. Comparison of Topologies

> **Definition 2.2 (Coarser and Finer Topologies):**
> Let $\mathcal{T}_1$ and $\mathcal{T}_2$ be two topologies on the same set $X$.
> - If $\mathcal{T}_1 \subseteq \mathcal{T}_2$, we say that $\mathcal{T}_1$ is **coarser** (or **weaker**, **smaller**) than $\mathcal{T}_2$, and that $\mathcal{T}_2$ is **finer** (or **stronger**, **larger**) than $\mathcal{T}_1$.
> - For any set $X$:
>   $$\mathcal{T}_{\text{ind}} \subseteq \mathcal{T}_{\text{cof}} \subseteq \mathcal{T}_{\text{metric}} \subseteq \mathcal{T}_{\text{disc}}$$
> - If neither $\mathcal{T}_1 \subseteq \mathcal{T}_2$ nor $\mathcal{T}_2 \subseteq \mathcal{T}_1$, the topologies are called **incomparable**."""
            },
            {
                "secNumber": "2.2",
                "title": "Closed Sets, Interior, Closure, Boundary & Kuratowski Axioms",
                "content": r"""### 1. Closed Sets, Closure and Interior

> **Definition 2.3 (Closed Set):**
> A subset $F \subseteq X$ is called **closed** in $(X, \mathcal{T})$ if its complement $X \setminus F$ is open in $(X, \mathcal{T})$.

> **Theorem 2.1 (Properties of Closed Sets):**
> 1. $\emptyset$ and $X$ are closed.
> 2. The intersection of an arbitrary family of closed sets is closed: $\bigcap_{\alpha \in I} F_\alpha$ is closed.
> 3. The union of a finite collection of closed sets is closed: $\bigcup_{i=1}^n F_i$ is closed.

> **Definition 2.4 (Interior, Closure, Boundary):**
> Let $A \subseteq X$.
> 1. The **interior** of $A$, denoted $\operatorname{int}(A)$ or $A^\circ$, is the largest open set contained in $A$:
>    $$\operatorname{int}(A) = \bigcup \{U \in \mathcal{T} : U \subseteq A\}$$
> 2. The **closure** of $A$, denoted $\operatorname{cl}(A)$ or $\bar{A}$, is the smallest closed set containing $A$:
>    $$\operatorname{cl}(A) = \bigcap \{F \subseteq X : F \text{ is closed and } A \subseteq F\}$$
> 3. The **boundary** (or **frontier**) of $A$ is:
>    $$\partial A = \operatorname{cl}(A) \setminus \operatorname{int}(A) = \operatorname{cl}(A) \cap \operatorname{cl}(X \setminus A)$$
> 4. The **exterior** of $A$ is $\operatorname{ext}(A) = \operatorname{int}(X \setminus A) = X \setminus \operatorname{cl}(A)$.

---

### 2. Kuratowski Closure Axioms

Topological spaces can be defined entirely through the closure operator rather than open sets!

> **Theorem 2.2 (Kuratowski Closure Axioms, 1922):**
> Let $X$ be a set. A closure operator is a mapping $c: \mathcal{P}(X) \to \mathcal{P}(X)$ satisfying for all $A, B \subseteq X$:
> 1. **Empty Set:** $c(\emptyset) = \emptyset$.
> 2. **Extension:** $A \subseteq c(A)$.
> 3. **Additivity:** $c(A \cup B) = c(A) \cup c(B)$.
> 4. **Idempotence:** $c(c(A)) = c(A)$.
>
> If an operator $c$ satisfies these four axioms, there exists a **unique topology** $\mathcal{T}$ on $X$ such that for all $A \subseteq X$, $\operatorname{cl}(A) = c(A)$, where closed sets are precisely the fixed points: $F \text{ is closed} \iff c(F) = F$."""
            },
            {
                "secNumber": "2.3",
                "title": "Neighborhood Systems, Neighborhood Filters & Accumulation Points",
                "content": r"""### 1. Neighborhoods and Neighborhood Filters

> **Definition 2.5 (Neighborhood):**
> Let $(X, \mathcal{T})$ be a topological space and $x \in X$.
> A subset $N \subseteq X$ is called a **neighborhood** of $x$ if there exists an open set $U \in \mathcal{T}$ such that:
> $$x \in U \subseteq N$$
> Note that $N$ itself does not need to be open; if $N$ is open, it is called an **open neighborhood**.

> **Theorem 2.3 (Hausdorff Neighborhood Filter Axioms):**
> The collection $\mathcal{N}(x)$ of all neighborhoods of a point $x$ forms a **filter** on $X$:
> 1. **Non-emptiness:** $N \in \mathcal{N}(x) \implies x \in N$.
> 2. **Supersets:** If $N \in \mathcal{N}(x)$ and $N \subseteq M$, then $M \in \mathcal{N}(x)$.
> 3. **Finite Intersections:** If $N_1, N_2 \in \mathcal{N}(x)$, then $N_1 \cap N_2 \in \mathcal{N}(x)$.
> 4. **Open Core:** If $N \in \mathcal{N}(x)$, there exists $U \in \mathcal{N}(x)$ such that $N \in \mathcal{N}(y)$ for every $y \in U$.

---

### 2. Accumulation Points, Derived Sets & Isolated Points

> **Definition 2.6 (Limit / Accumulation Point):**
> Let $A \subseteq X$. A point $x \in X$ is called an **accumulation point** (or **limit point**, **cluster point**) of $A$ if every neighborhood $U$ of $x$ contains at least one point of $A$ different from $x$:
> $$(U \setminus \{x\}) \cap A \ne \emptyset, \qquad \forall U \in \mathcal{N}(x)$$
> - The set of all accumulation points of $A$ is called the **derived set** of $A$, denoted $A'$.
> - Points in $A \setminus A'$ are called **isolated points** of $A$.
> - A point $x \in X$ is an **adherent point** of $A$ if every neighborhood of $x$ intersects $A$: $U \cap A \ne \emptyset$.

> **Theorem 2.4 (Closure via Derived Set):**
> For any subset $A \subseteq X$:
> $$\operatorname{cl}(A) = A \cup A'$$
> Consequently, a subset $A$ is closed if and only if it contains all of its accumulation points ($A' \subseteq A$)."""
            },
            {
                "secNumber": "2.4",
                "title": "Bases and Subbases for a Topology",
                "content": r"""### 1. Bases for a Topology

Specifying every single open set in an infinite topology is practically impossible. Instead, topologies are defined via a smaller collection of generating sets called a **basis**.

> **Definition 2.7 (Basis for a Topology):**
> Let $(X, \mathcal{T})$ be a topological space. A collection $\mathcal{B} \subseteq \mathcal{T}$ of open sets is called a **basis** for $\mathcal{T}$ if every open set $U \in \mathcal{T}$ can be expressed as a union of elements of $\mathcal{B}$:
> $$U = \bigcup \{B \in \mathcal{B} : B \subseteq U\}$$
> Equivalently, for every $U \in \mathcal{T}$ and every $x \in U$, there exists $B \in \mathcal{B}$ such that $x \in B \subseteq U$.

---

### 2. The Basis Criterion Theorem

When does an arbitrary family of subsets $\mathcal{B}$ form a basis for *some* topology on $X$?

> **Theorem 2.5 (Basis Criterion):**
> A collection $\mathcal{B}$ of subsets of $X$ is a basis for a topology on $X$ if and only if:
> 1. **Covering Property:** $\bigcup_{B \in \mathcal{B}} B = X$ (i.e. every point $x \in X$ belongs to at least one $B \in \mathcal{B}$).
> 2. **Intersection Property:** For any two basis elements $B_1, B_2 \in \mathcal{B}$ and any point $x \in B_1 \cap B_2$, there exists a basis element $B_3 \in \mathcal{B}$ such that:
>    $$x \in B_3 \subseteq B_1 \cap B_2$$
>
> If these two conditions hold, the topology $\mathcal{T}(\mathcal{B})$ generated by $\mathcal{B}$ consists of all arbitrary unions of sets in $\mathcal{B}$.

> **Proof:**
> **($\Rightarrow$)** If $\mathcal{B}$ is a basis for $\mathcal{T}$, since $X \in \mathcal{T}$, $X$ is a union of basis elements, so $\bigcup \mathcal{B} = X$.
> Since $B_1, B_2 \in \mathcal{T}$, their intersection $B_1 \cap B_2 \in \mathcal{T}$. Since $\mathcal{B}$ is a basis, for any $x \in B_1 \cap B_2$, there exists $B_3 \in \mathcal{B}$ with $x \in B_3 \subseteq B_1 \cap B_2$.
>
> **($\Leftarrow$)** Define $\mathcal{T}$ as the collection of all unions of subsets of $\mathcal{B}$.
> - $\emptyset$ is the empty union ($\emptyset \in \mathcal{T}$). By condition (1), $X = \bigcup_{B \in \mathcal{B}} B \in \mathcal{T}$.
> - Unions of sets in $\mathcal{T}$ are obviously unions of sets in $\mathcal{B}$, hence in $\mathcal{T}$.
> - For finite intersections: it suffices to check that if $U, V \in \mathcal{T}$, then $U \cap V \in \mathcal{T}$.
>   Let $x \in U \cap V$. Then $x \in B_1 \subseteq U$ and $x \in B_2 \subseteq V$ for some $B_1, B_2 \in \mathcal{B}$.
>   By condition (2), there exists $B_x \in \mathcal{B}$ such that $x \in B_x \subseteq B_1 \cap B_2 \subseteq U \cap V$.
>   Then $U \cap V = \bigcup_{x \in U \cap V} B_x \in \mathcal{T}$. $\blacksquare$

---

### 3. Subbases for a Topology

> **Definition 2.8 (Subbasis):**
> A collection $\mathcal{S}$ of subsets of $X$ is called a **subbasis** for a topology $\mathcal{T}$ if the collection of all **finite intersections** of elements of $\mathcal{S}$:
> $$\mathcal{B} = \left\{ \bigcap_{i=1}^k S_i : k \in \mathbb{N}, \; S_i \in \mathcal{S} \right\}$$
> forms a basis for $\mathcal{T}$ (with the empty intersection defined as $X$).
> Remark: **Any** arbitrary family of subsets $\mathcal{S}$ covering $X$ generates a unique topology $\mathcal{T}$ on $X$ for which $\mathcal{S}$ is a subbasis!"""
            },
            {
                "secNumber": "2.5",
                "title": "Subspace Topology (Relative Topology) & Hereditary Properties",
                "content": r"""### 1. The Subspace Topology

> **Definition 2.9 (Subspace Topology):**
> Let $(X, \mathcal{T})$ be a topological space and let $Y \subseteq X$ be an arbitrary subset.
> The **subspace topology** (or **relative topology**) on $Y$, denoted $\mathcal{T}_Y$, is defined by:
> $$\mathcal{T}_Y = \{U \cap Y : U \in \mathcal{T}\}$$
> The pair $(Y, \mathcal{T}_Y)$ is called a **topological subspace** of $(X, \mathcal{T})$.

---

### 2. Relative Open and Closed Sets

> **Proposition 2.1 (Relative Open and Closed Sets):**
> Let $Y \subseteq X$.
> 1. A set $V \subseteq Y$ is open in $Y$ if and only if $V = U \cap Y$ for some open set $U \subseteq X$.
> 2. A set $K \subseteq Y$ is closed in $Y$ if and only if $K = F \cap Y$ for some closed set $F \subseteq X$.
> 3. If $Y$ is open in $X$, then every set open in $Y$ is also open in $X$.
> 4. If $Y$ is closed in $X$, then every set closed in $Y$ is also closed in $X$.

> **Theorem 2.6 (Relative Closure and Interior):**
> For any subset $A \subseteq Y$:
> 1. The closure of $A$ in $Y$ satisfies:
>    $$\operatorname{cl}_Y(A) = \operatorname{cl}_X(A) \cap Y$$
> 2. The interior of $A$ in $Y$ satisfies:
>    $$\operatorname{int}_X(A) \cap Y \subseteq \operatorname{int}_Y(A)$$
>    (The inclusion can be strict: for example, the interval $[0, 1/2)$ has non-empty interior in the subspace $Y = [0, 1]$, but empty interior in $\mathbb{R}$!).

---

### 3. Hereditary Properties

> **Definition 2.10 (Hereditary Property):**
> A topological property $P$ is called **hereditary** if whenever a space $X$ possesses property $P$, every subspace $Y \subseteq X$ also possesses property $P$.
> It is called **weakly hereditary** (or closed-hereditary) if it is inherited by all closed subspaces.
> - Examples of hereditary properties: Hausdorff ($T_2$), First-countability, Second-countability, Metrizability.
> - Examples of non-hereditary properties: Compactness (a closed interval $[0, 1]$ is compact, but its subspace $(0, 1)$ is not!)."""
            }
        ],
        "problems": [
            {
                "id": "prob_2_1",
                "tier": "Foundational",
                "title": "Topological Interior, Closure and Boundary in Co-finite Topology",
                "statement": r"""Let $X = \mathbb{R}$ be equipped with the co-finite topology $\mathcal{T}_{\text{cof}}$, where non-empty open sets are those with finite complement.
Compute the interior, closure, and boundary in $(X, \mathcal{T}_{\text{cof}})$ for each of the following subsets:
1. $A = \{1, 2, 3, \dots, 10\}$ (a finite set)
2. $B = (0, 1)$ (the open unit interval)
3. $C = \mathbb{Z}$ (the integers)
4. $D = \mathbb{Q}$ (the rational numbers)""",
                "solution": r"""### 1. Closed Sets in $(X, \mathcal{T}_{\text{cof}})$

By definition, a subset $F \subseteq \mathbb{R}$ is closed in $\mathcal{T}_{\text{cof}}$ if and only if $F = \mathbb{R}$ or $F$ is **finite**.
Non-empty open sets $U$ are those where $\mathbb{R} \setminus U$ is finite.

---

### 2. Set $A = \{1, 2, \dots, 10\}$ (Finite Set)

- **Closure:** Since $A$ is finite, $A$ is closed. Thus $\operatorname{cl}(A) = A = \{1, 2, \dots, 10\}$.
- **Interior:** The only open sets in $\mathcal{T}_{\text{cof}}$ are $\emptyset$ and sets with finite complement.
  Since $A$ is finite, its complement $\mathbb{R} \setminus A$ is infinite (uncountable), so $A$ cannot contain any non-empty open set!
  Thus $\operatorname{int}(A) = \emptyset$.
- **Boundary:** $\partial A = \operatorname{cl}(A) \setminus \operatorname{int}(A) = A \setminus \emptyset = A = \{1, 2, \dots, 10\}$.

---

### 3. Set $B = (0, 1)$ (Infinite Set with Infinite Complement)

- **Closure:** The only closed sets containing $B$ are closed sets of $\mathcal{T}_{\text{cof}}$.
  The only closed sets are finite sets and $\mathbb{R}$ itself.
  Since $B$ is infinite, no finite set can contain $B$.
  The only closed set containing $B$ is the whole space $\mathbb{R}$!
  Thus $\operatorname{cl}(B) = \mathbb{R}$.
- **Interior:** For $B$ to contain a non-empty open set $U$, $\mathbb{R} \setminus U$ must be finite.
  Then $\mathbb{R} \setminus B \subseteq \mathbb{R} \setminus U$ would force $\mathbb{R} \setminus B$ to be finite.
  However, $\mathbb{R} \setminus (0, 1) = (-\infty, 0] \cup [1, \infty)$ is infinite!
  Thus $B$ contains no non-empty open set, so $\operatorname{int}(B) = \emptyset$.
- **Boundary:** $\partial B = \operatorname{cl}(B) \setminus \operatorname{int}(B) = \mathbb{R} \setminus \emptyset = \mathbb{R}$.

---

### 4. Sets $C = \mathbb{Z}$ and $D = \mathbb{Q}$

Both $C = \mathbb{Z}$ and $D = \mathbb{Q}$ are infinite subsets with infinite complement:
- $\operatorname{cl}(\mathbb{Z}) = \mathbb{R}$, $\operatorname{int}(\mathbb{Z}) = \emptyset$, $\partial \mathbb{Z} = \mathbb{R}$.
- $\operatorname{cl}(\mathbb{Q}) = \mathbb{R}$, $\operatorname{int}(\mathbb{Q}) = \emptyset$, $\partial \mathbb{Q} = \mathbb{R}$.

In the co-finite topology, every infinite subset is dense ($\bar{S} = X$), and every subset with infinite complement has empty interior!"""
            },
            {
                "id": "prob_2_2",
                "tier": "Advanced",
                "title": "The Kuratowski 14-Set Problem",
                "statement": r"""In 1922, Kazimierz Kuratowski asked: given a subset $A$ of a topological space $(X, \mathcal{T})$, how many distinct sets can be formed by repeatedly applying the closure operator $c(A) = \bar{A}$ and the complement operator $k(A) = X \setminus A$?
1. Prove that at most $14$ distinct sets can be obtained.
2. Construct an explicit subset $A \subset \mathbb{R}$ under the standard Euclidean topology that achieves all $14$ distinct sets.""",
                "solution": r"""### 1. Theoretical Maximum of 14 Sets

Let $c(A) = \operatorname{cl}(A)$ and $k(A) = X \setminus A$.
Note the fundamental relations:
- $k(k(A)) = A$ (involution: $k^2 = \operatorname{id}$).
- $c(c(A)) = c(A)$ (idempotence: $c^2 = c$).
- The interior operator is $i(A) = k(c(k(A)))$. Thus $i^2 = i$.

Any sequence of operations alternates between $c$ and $k$.
Consider words starting with $A$:
- Words of the form $k, ck, kck, ckc, \dots$
- Words of the form $c, kc, ckc, kckc, \dots$

> **Key Identity (Kuratowski):**
> For any subset $A$:
> $$c(k(c(k(c(k(c(A))))))) = c(k(c(A)))$$
> That is:
> $$c i c i(A) = c i(A)$$

**Proof of Identity:**
Since $i(A) \subseteq A$, taking closure gives $c(i(A)) \subseteq c(A)$.
Taking interior gives $i(c(i(A))) \subseteq i(c(A))$.
Taking closure gives $c i c i(A) \subseteq c i(A)$.
Conversely, $i(A)$ is open, so $i(A) \subseteq i(c(i(A)))$, and taking closure yields $c i(A) \subseteq c i c i(A)$.
Thus:
$$c i c i(A) = c i(A)$$
Dualizing with complement gives $i c i c(A) = i c(A)$.

Because the alternating sequences of $c$ and $i$ collapse after 2 iterations:
The only possible operations on $A$ are:
1. $A$
2. $c(A)$
3. $i c(A)$
4. $c i c(A)$
5. $i(A)$
6. $c i(A)$
7. $i c i(A)$
Applying complement $k$ to each of these $7$ sets produces at most $7$ complementary sets:
$$7 + 7 = 14 \text{ distinct sets!}$$

---

### 2. Explicit Subset of $\mathbb{R}$ Achieving 14 Sets

Consider the subset $A \subset \mathbb{R}$ defined by:
$$A = (0, 1) \cup (1, 2) \cup \{3\} \cup (\mathbb{Q} \cap [4, 5])$$

Evaluating the 7 sets containing closure/interior:
1. $A = (0, 1) \cup (1, 2) \cup \{3\} \cup (\mathbb{Q} \cap [4, 5])$
2. $c(A) = [0, 2] \cup \{3\} \cup [4, 5]$
3. $i(c(A)) = (0, 2) \cup (4, 5)$
4. $c(i(c(A))) = [0, 2] \cup [4, 5]$
5. $i(A) = (0, 1) \cup (1, 2)$
6. $c(i(A)) = [0, 2]$
7. $i(c(i(A))) = (0, 2)$

Notice that all 7 sets are **mutually distinct**:
- $A \ne c(A)$ (e.g. $[4, 5] \setminus \mathbb{Q}$ is in $c(A)$ but not $A$).
- $c(A) \ne i(c(A))$ ($3 \in c(A)$, not in $i(c(A))$).
- $i(c(A)) \ne c(i(c(A)))$ (endpoints $0, 2, 4, 5$).
- $c(i(c(A))) \ne c(i(A))$ ($[4, 5]$ is missing from $c(i(A))$).
- $c(i(A)) \ne i(c(i(A)))$ ($0, 2 \in c(i(A))$).
- $i(c(i(A))) \ne i(A)$ ($1 \in (0, 2)$ but $1 \notin i(A)$).

Taking the complements of these 7 sets yields another 7 distinct sets, completely disjoint from the first 7 because no set here is both open and closed!
Thus, $A$ generates **exactly 14 distinct sets**."""
            },
            {
                "id": "prob_2_3",
                "tier": "Honors / Proof Challenge",
                "title": "Subbase Generation & Alexander's Subbase Characterization",
                "statement": r"""1. Let $X$ be a set and let $\mathcal{S} \subseteq \mathcal{P}(X)$ be an arbitrary collection of subsets such that $\bigcup_{S \in \mathcal{S}} S = X$.
Prove rigorously that the collection $\mathcal{B}$ of all finite intersections of elements of $\mathcal{S}$:
$$\mathcal{B} = \left\{ \bigcap_{i=1}^k S_i : k \in \mathbb{N}, \; S_i \in \mathcal{S} \right\}$$
satisfies the Basis Criterion Theorem (Theorem 2.5), and therefore generates a unique topology $\mathcal{T}(\mathcal{S})$ on $X$.
2. Prove that $\mathcal{T}(\mathcal{S})$ is the **coarsest (smallest) topology** on $X$ that contains $\mathcal{S}$.""",
                "solution": r"""### 1. Proof of the Basis Criterion for Finite Intersections

Let $\mathcal{B} = \left\{ \bigcap_{i=1}^k S_i : k \ge 1, S_i \in \mathcal{S} \right\} \cup \{X\}$.
We must verify the two conditions of Theorem 2.5:

**Condition 1 (Covering):**
By hypothesis, $\bigcup_{S \in \mathcal{S}} S = X$.
Since $\mathcal{S} \subseteq \mathcal{B}$, every $x \in X$ belongs to some $S \in \mathcal{S} \subseteq \mathcal{B}$.
Thus $\bigcup_{B \in \mathcal{B}} B = X$.

**Condition 2 (Intersection Property):**
Let $B_1, B_2 \in \mathcal{B}$.
By definition of $\mathcal{B}$:
$$B_1 = \bigcap_{i=1}^m S_i \quad \text{and} \quad B_2 = \bigcap_{j=1}^n S'_j$$
for some $S_1, \dots, S_m, S'_1, \dots, S'_n \in \mathcal{S}$.
Now compute their intersection:
$$B_1 \cap B_2 = \left( \bigcap_{i=1}^m S_i \right) \cap \left( \bigcap_{j=1}^n S'_j \right) = S_1 \cap \cdots \cap S_m \cap S'_1 \cap \cdots \cap S'_n$$
Notice that $B_1 \cap B_2$ is itself a **finite intersection** of $m + n$ elements of $\mathcal{S}$!
Therefore:
$$B_3 = B_1 \cap B_2 \in \mathcal{B}$$
For any $x \in B_1 \cap B_2$, simply choosing $B_3 = B_1 \cap B_2 \in \mathcal{B}$ trivially satisfies:
$$x \in B_3 \subseteq B_1 \cap B_2$$
Condition 2 holds with equality!
By the Basis Criterion (Theorem 2.5), $\mathcal{B}$ forms a valid basis for a topology on $X$.

---

### 2. Minimality of $\mathcal{T}(\mathcal{S})$

Let $\mathcal{T}'$ be any topology on $X$ containing $\mathcal{S}$ (i.e. $\mathcal{S} \subseteq \mathcal{T}'$).
- Since $\mathcal{T}'$ is closed under finite intersections, every finite intersection of sets in $\mathcal{S}$ must belong to $\mathcal{T}'$. Thus $\mathcal{B} \subseteq \mathcal{T}'$.
- Since $\mathcal{T}'$ is closed under arbitrary unions, every union of elements in $\mathcal{B}$ must belong to $\mathcal{T}'$.
- By definition, $\mathcal{T}(\mathcal{S})$ consists precisely of all arbitrary unions of sets in $\mathcal{B}$.
- Therefore:
  $$\mathcal{T}(\mathcal{S}) \subseteq \mathcal{T}'$$
Hence, $\mathcal{T}(\mathcal{S})$ is contained in every topology containing $\mathcal{S}$, which proves that $\mathcal{T}(\mathcal{S})$ is the **unique coarsest topology** on $X$ containing $\mathcal{S}$. $\blacksquare$"""
            }
        ]
    }
    return u2

if __name__ == "__main__":
    u2 = get_unit2()
    print(f"Loaded Unit 2: {u2['title']} with {len(u2['sections'])} sections and {len(u2['problems'])} problems.")
