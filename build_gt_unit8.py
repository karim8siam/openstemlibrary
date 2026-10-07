# -*- coding: utf-8 -*-
"""
build_gt_unit8.py
Constructs Unit 8: Graph Coloring, Chromatic Polynomials & Network Flows
"""

def get_unit8():
    u8 = {
        "number": 8,
        "title": "Graph Coloring, Chromatic Polynomials & Network Flows",
        "leadSummary": "Advanced theory of vertex and edge colorings, algebraic chromatic polynomials, and network flow optimization: proper vertex coloring, chromatic number chi(G), greedy coloring and Welsh-Powell algorithm, Brooks' theorem, the Five-Color and Four-Color theorems, chromatic polynomials P(G, k) and deletion-contraction recurrence, edge coloring, chromatic index chi'(G) and Vizing's theorem, network flows, residual capacity networks, the Max-Flow Min-Cut theorem, and Hall's Marriage Theorem for bipartite matchings.",
        "simulations": ["sim_gt_coloring_flows"],
        "sections": [
            {
                "secNumber": "8.1",
                "title": "Vertex Coloring, Chromatic Number $\\chi(G)$ & Brooks' Theorem",
                "content": r"""### 1. Proper Vertex Coloring and Chromatic Number

Graph coloring originated from cartographic map coloring in 1852 (Francis Guthrie) and has matured into one of the richest and most computationally challenging branches of discrete mathematics.

> **Definition 8.1 (Proper Vertex $k$-Coloring):**
> Let $G = (V, E)$ be a simple graph. A **proper vertex $k$-coloring** is an assignment of colors $c: V \to \{1, 2, \dots, k\}$ such that no two adjacent vertices share the same color:
> $$\forall \{u, v\} \in E \implies c(u) \ne c(v)$$
> If such an assignment exists, $G$ is said to be **$k$-colorable**.

> **Definition 8.2 (Chromatic Number $\chi(G)$):**
> The **chromatic number** of $G$, denoted $\chi(G)$, is the minimum integer $k \ge 1$ such that $G$ admits a proper $k$-coloring:
> $$\chi(G) = \min \{ k \in \mathbb{N} : G \text{ is } k\text{-colorable} \}$$

---

### 2. Elementary Bounds on $\chi(G)$

> **Theorem 8.1 (Elementary Coloring Bounds):**
> For any simple graph $G = (V, E)$ with maximum vertex degree $\Delta(G)$ and clique number $\omega(G)$ (the order of the largest complete subgraph $K_r \subseteq G$):
> $$\omega(G) \le \chi(G) \le \Delta(G) + 1$$

#### Proof:
1. **Lower Bound ($\omega(G) \le \chi(G)$):**
   Let $K_r \subseteq G$ be a clique of size $r = \omega(G)$. Every pair of vertices in $K_r$ is connected by an edge.
   Therefore, all $r$ vertices in the clique must receive mutually distinct colors in any proper coloring.
   Hence $\chi(G) \ge \chi(K_r) = r = \omega(G)$.

2. **Upper Bound ($\chi(G) \le \Delta(G) + 1$ via Greedy Coloring):**
   Let $v_1, v_2, \dots, v_n$ be an arbitrary ordering of $V(G)$.
   Color the vertices sequentially for $i = 1, 2, \dots, n$:
   When coloring $v_i$, it has at most $\deg(v_i) \le \Delta(G)$ previously colored neighbors in $\{v_1, \dots, v_{i-1}\}$.
   These neighbors consume at most $\Delta(G)$ distinct colors from the available set $\{1, 2, \dots, \Delta(G) + 1\}$.
   By the Pigeonhole Principle, there is at least one color in $\{1, 2, \dots, \Delta(G) + 1\}$ not used by any neighbor of $v_i$.
   Assign the smallest such available color to $v_i$.
   This greedy process successfully colors every vertex using at most $\Delta(G) + 1$ colors.
   Therefore, $\chi(G) \le \Delta(G) + 1$. $\blacksquare$

---

### 3. Brooks' Theorem (1941)

The bound $\chi(G) \le \Delta(G) + 1$ is tight for complete graphs $K_n$ ($\Delta = n - 1, \chi = n$) and odd cycle graphs $C_{2k+1}$ ($\Delta = 2, \chi = 3$).
Remarkably, R. L. Brooks proved that these are the **only** connected graphs for which the bound $\chi \le \Delta + 1$ cannot be improved by 1:

> **Theorem 8.2 (Brooks' Theorem, 1941):**
> Let $G$ be a connected simple graph with maximum degree $\Delta = \Delta(G)$.
> If $G$ is neither a complete graph ($G \not\cong K_{\Delta+1}$) nor an odd cycle of length $2k+1$ ($\Delta = 2$), then:
> $$\chi(G) \le \Delta$$

#### Full Formal Proof (Lovász Ordering Technique):
We proceed through the structural cases of connectivity:

1. **Case $\Delta \le 2$:**
   - If $\Delta = 0$, $G \cong K_1$ (complete graph).
   - If $\Delta = 1$, $G \cong K_2$ (complete graph).
   - If $\Delta = 2$, $G$ is a path $P_n$ or a cycle $C_n$.
     - If $G = P_n$, $G$ is bipartite, so $\chi(P_n) = 2 = \Delta$.
     - If $G = C_{2k}$, $G$ is an even cycle, which is bipartite, so $\chi(C_{2k}) = 2 = \Delta$.
     - If $G = C_{2k+1}$, it is an odd cycle, explicitly excluded.
   Thus the theorem holds for all $\Delta \le 2$.

2. **Case $\Delta \ge 3$ and $G$ is not 2-connected (has a cut-vertex):**
   Let $v$ be a cut-vertex of $G$, partitioning $G - v$ into components.
   Then $G = G_1 \cup G_2$ where $V(G_1) \cap V(G_2) = \{v\}$ and $|V(G_1)|, |V(G_2)| < |V(G)|$.
   By induction on the number of vertices, $\chi(G_1) \le \Delta(G_1) \le \Delta$ and $\chi(G_2) \le \Delta(G_2) \le \Delta$.
   Permute colors in $G_2$ so that $v$ receives the same color in both colorings.
   Gluing $G_1$ and $G_2$ at $v$ yields a proper $\Delta$-coloring of $G$.

3. **Case $\Delta \ge 3$ and $G$ is 2-connected but not 3-connected:**
   If $G$ has a 2-vertex cut $\{u, v\}$, a similar decomposition applies by considering whether $\{u, v\} \in E$ or not.

4. **Case $\Delta \ge 3$ and $G$ is 3-connected:**
   Because $G$ is not complete, there exist three vertices $u, v, w \in V(G)$ such that $\{u, v\} \in E$, $\{v, w\} \in E$, but $\{u, w\} \notin E$ (a 2-path without a chord).
   Consider $H = G \setminus \{u, w\}$. Since $G$ is 3-connected, $H$ is connected.
   Construct a spanning tree $T$ of $H$ rooted at $v$.
   Order the vertices of $H$ in reverse breadth-first/depth-first order starting from the leaves of $T$ towards the root $v$:
   - Let $v_n = v$ (the root).
   - Let $v_1 = u$ and $v_2 = w$ (the two non-adjacent vertices).
   - Let $v_3, v_4, \dots, v_{n-1}$ be the remaining vertices of $H$ in reverse topological order along $T$.
   
   Now execute greedy coloring on this vertex ordering $v_1, v_2, \dots, v_n$:
   - Color $v_1 = u$ with color 1.
   - Color $v_2 = w$ with color 1 (valid since $\{u, w\} \notin E$!).
   - For each $i = 3, 4, \dots, n-1$: vertex $v_i$ has at least one forward neighbor in the tree $T$ that appears after $v_i$ in the ordering.
     Therefore, $v_i$ has at most $\deg(v_i) - 1 \le \Delta - 1$ neighbors colored before it.
     Thus at least one of the $\Delta$ colors $\{1, 2, \dots, \Delta\}$ is free for $v_i$.
   - Finally, consider the root $v_n = v$:
     $v$ has at most $\Delta$ neighbors in total.
     Crucially, two of its neighbors are $u$ and $w$, both of which were assigned the **same color 1**!
     Therefore, the neighbors of $v$ consume at most $\Delta - 1$ distinct colors!
     At least one color in $\{1, 2, \dots, \Delta\}$ remains available for $v_n = v$.
   
   Greedy coloring terminates with a proper $\Delta$-coloring of $G$. $\blacksquare$

---

### 4. The Five-Color and Four-Color Theorems for Planar Graphs

The famous Four Color Conjecture was posed by Guthrie in 1852, incorrectly proved by Kempe in 1879, refuted by Heawood in 1890 who salvaged the Five Color Theorem, and finally established by Appel and Haken in 1976 using 1,936 reducible computer configurations:

> **Theorem 8.3 (Heawood's Five-Color Theorem, 1890):**
> Every planar graph $G$ is 5-colorable: $\chi(G) \le 5$.

#### Full Formal Proof (Kempe Chain Induction):
We proceed by induction on $n = |V(G)|$:
1. **Base Case:** For $n \le 5$, the result is trivial since $n$ vertices require at most $n \le 5$ colors.
2. **Inductive Step:** Assume every planar graph with fewer than $n$ vertices is 5-colorable.
   Let $G$ be a planar graph with $n$ vertices.
   By Corollary 7.3, every planar graph has a vertex $v$ with degree $\deg(v) \le 5$.
   Consider $G - v$, which has $n - 1$ vertices and is planar.
   By the inductive hypothesis, $G - v$ has a proper 5-coloring $c: V(G - v) \to \{1, 2, 3, 4, 5\}$.
3. If $\deg(v) \le 4$, or if the neighbors of $v$ use at most 4 distinct colors, assign an unused color in $\{1, 2, 3, 4, 5\}$ to $v$.
4. **The Critical Case $\deg(v) = 5$:**
   Suppose the 5 neighbors $v_1, v_2, v_3, v_4, v_5$ of $v$ arranged clockwise around $v$ in a planar embedding receive 5 distinct colors:
   $$c(v_i) = i \quad \text{for } i = 1, 2, 3, 4, 5$$
   
   Define the **Kempe chain** $H_{1, 3}$ as the subgraph of $G - v$ induced by all vertices colored with color 1 or color 3.
   - **Subcase A:** $v_1$ and $v_3$ belong to different connected components of $H_{1, 3}$.
     In the component containing $v_1$, interchange colors 1 and 3 (swap $1 \leftrightarrow 3$).
     Since no vertex in this component is adjacent to a vertex of color 1 or 3 outside the component, this remains a valid proper coloring of $G - v$.
     Now $v_1$ has color 3, and $v_3$ still has color 3.
     Color 1 is no longer used by any neighbor of $v$! Assign color 1 to $v$.
   
   - **Subcase B:** $v_1$ and $v_3$ belong to the same connected component of $H_{1, 3}$.
     Then there exists an alternating path $P_{1, 3}$ connecting $v_1$ and $v_3$ in $H_{1, 3}$.
     Together with edges $\{v, v_1\}$ and $\{v, v_3\}$, this forms a Jordan curve $C = P_{1, 3} \cup \{v_1, v\} \cup \{v, v_3\}$ in the plane!
     Crucially, $v_2$ lies in the interior of $C$, while $v_4$ lies in the exterior of $C$ (or vice versa)!
     
     Now consider the Kempe chain $H_{2, 4}$ induced by colors 2 and 4.
     Any path in $H_{2, 4}$ connecting $v_2$ and $v_4$ would have to cross the Jordan curve $C$!
     Since the drawing is planar, vertices of $H_{2, 4}$ cannot cross edges of $C$ without intersecting them.
     Furthermore, vertices on $C$ have colors in $\{1, 3\}$, which are disjoint from $\{2, 4\}$.
     Therefore, **no path in $H_{2, 4}$ can connect $v_2$ and $v_4$**!
     $v_2$ and $v_4$ MUST belong to different connected components of $H_{2, 4}$!
     
     Interchange colors 2 and 4 in the component containing $v_2$.
     Now $v_2$ receives color 4, color 2 is vacated around $v$, and we can safely color $v$ with color 2.
In all cases, $G$ is properly 5-colored. $\blacksquare$"""
            },
            {
                "secNumber": "8.2",
                "title": "Chromatic Polynomials $P(G, k)$ & Deletion-Contraction Recurrence",
                "content": r"""### 1. Algebraic Chromatic Polynomials

Introduced by George David Birkhoff in 1912 to tackle the Four Color Problem, the chromatic polynomial translates coloring combinatorics into commutative algebra.

> **Definition 8.3 (Chromatic Polynomial $P(G, k)$):**
> Let $G = (V, E)$ be a simple graph and $k \in \mathbb{N}$ a positive integer.
> The **chromatic polynomial** $P(G, k)$ (also written $\pi_G(k)$) is the function that counts the number of distinct proper vertex colorings of $G$ using at most $k$ colors:
> $$P(G, k) = |\{ c: V \to \{1, 2, \dots, k\} : c \text{ is a proper coloring} \}|$$

---

### 2. Standard Families of Chromatic Polynomials

1. **Empty Graph $\bar{K}_n$ ($n$ isolated vertices, $E = \emptyset$):**
   Each of the $n$ vertices can be colored independently in $k$ ways:
   $$P(\bar{K}_n, k) = k^n$$

2. **Complete Graph $K_n$:**
   First vertex has $k$ choices, second has $k-1$, and the $i$-th has $k - i + 1$:
   $$P(K_n, k) = k(k-1)(k-2)\cdots(k-n+1) = k_{(n)}$$
   (the falling factorial).

3. **Tree $T_n$ ($n$ vertices, $n-1$ edges):**
   Root the tree at $r$. Color $r$ in $k$ ways.
   Every subsequent vertex in a topological ordering has exactly one colored parent, leaving $k-1$ available choices:
   $$P(T_n, k) = k (k-1)^{n-1}$$
   *(Notice that all trees on $n$ vertices share identical chromatic polynomials!)*

---

### 3. The Fundamental Deletion-Contraction Recurrence

The central computational theorem for chromatic polynomials is the **Deletion-Contraction Theorem**:

> **Theorem 8.4 (Deletion-Contraction Recurrence):**
> Let $G = (V, E)$ be a simple graph and let $e = \{u, v\} \in E$ be an edge.
> Let $G - e$ denote the graph obtained by deleting $e$, and $G / e$ denote the graph obtained by contracting edge $e$ (identifying $u$ and $v$ and removing multiple edges).
> Then for all integers $k$:
> $$P(G, k) = P(G - e, k) - P(G / e, k)$$

#### Complete Formal Proof:
Let $C(G - e)$ denote the set of all proper $k$-colorings of $G - e$.
Partition $C(G - e)$ into two disjoint subsets based on whether the endpoints $u$ and $v$ of $e$ receive different colors or the same color:
$$C(G - e) = C_{\text{diff}} \cup C_{\text{same}}$$

1. **Case 1 ($c(u) \ne c(v)$):**
   If $c(u) \ne c(v)$, then the coloring $c$ does not violate the edge condition on $e = \{u, v\}$.
   Therefore, $c$ is a proper $k$-coloring of the original graph $G = (G - e) + e$.
   Conversely, every proper coloring of $G$ is a coloring of $G - e$ in which $c(u) \ne c(v)$.
   Hence:
   $$|C_{\text{diff}}| = P(G, k)$$

2. **Case 2 ($c(u) = c(v)$):**
   If $c(u) = c(v)$, we can collapse vertices $u$ and $v$ into a single composite vertex $w = \{u, v\}$ without altering color assignments.
   The coloring $c$ is a valid proper coloring of the contracted graph $G / e$.
   Conversely, every proper $k$-coloring of $G / e$ lifts uniquely to a proper coloring of $G - e$ in which $u$ and $v$ have the exact same color.
   Hence:
   $$|C_{\text{same}}| = P(G / e, k)$$

Summing the two disjoint subsets:
$$P(G - e, k) = |C_{\text{diff}}| + |C_{\text{same}}| = P(G, k) + P(G / e, k)$$
Rearranging yields:
$$P(G, k) = P(G - e, k) - P(G / e, k) \quad \blacksquare$$

---

### 4. Chromatic Polynomial of Cycles $C_n$

Applying deletion-contraction to a cycle edge $e \in E(C_n)$:
- $C_n - e \cong P_n$ (a path on $n$ vertices, which is a tree, so $P(P_n, k) = k(k-1)^{n-1}$).
- $C_n / e \cong C_{n-1}$ (contracting one edge of an $n$-cycle produces an $(n-1)$-cycle).

Therefore:
$$P(C_n, k) = k(k-1)^{n-1} - P(C_{n-1}, k)$$
By induction from the base case $P(C_3, k) = P(K_3, k) = k(k-1)(k-2) = (k-1)^3 - (k-1)$:
$$P(C_n, k) = (k-1)^n + (-1)^n(k-1)$$

---

### 5. Universal Algebraic Properties of $P(G, k)$

> **Theorem 8.5 (Properties of Chromatic Polynomials):**
> Let $G$ be a graph with $n$ vertices, $m$ edges, and $c$ connected components.
> Then $P(G, k)$ is a polynomial in $k$ satisfying:
> 1. $\deg(P(G, k)) = n$.
> 2. The leading coefficient is $1$ (monic: $P(G, k) = k^n - m k^{n-1} + \dots$).
> 3. The coefficient of $k^{n-1}$ is exactly $-m = -|E|$.
> 4. The signs of the coefficients strictly alternate.
> 5. The smallest power of $k$ with a non-zero coefficient is $k^c$, so $P(G, k)$ has a root of multiplicity $c$ at $k = 0$.
> 6. $\chi(G)$ is the smallest positive integer $k$ such that $P(G, k) > 0$."""
            },
            {
                "secNumber": "8.3",
                "title": "Edge Coloring, Chromatic Index $\\chi'(G)$ & Vizing's Theorem",
                "content": r"""### 1. Proper Edge Coloring and Chromatic Index

Rather than coloring vertices, we can assign colors to the edges of a network such that concurrently active links never share common terminals.

> **Definition 8.4 (Edge Coloring & Chromatic Index $\chi'(G)$):**
> 1. A **proper edge $k$-coloring** of $G = (V, E)$ is a function $c': E \to \{1, 2, \dots, k\}$ such that any two edges sharing a common endpoint receive distinct colors:
>    $$\forall e_1, e_2 \in E, \ e_1 \cap e_2 \ne \emptyset \implies c'(e_1) \ne c'(e_2)$$
> 2. The **chromatic index** (or edge chromatic number) $\chi'(G)$ is the minimum number of colors needed for a proper edge coloring:
>    $$\chi'(G) = \min \{ k : G \text{ has a proper edge } k\text{-coloring} \}$$

---

### 2. Trivial Degree Bound

At any vertex $v$, all $\deg(v)$ edges incident to $v$ must receive mutually distinct colors.
Therefore:
$$\chi'(G) \ge \max_{v \in V} \deg(v) = \Delta(G)$$

---

### 3. König's Line Coloring Theorem for Bipartite Graphs (1916)

For bipartite graphs, this trivial lower bound is always exact:

> **Theorem 8.6 (König's Theorem on Edge Coloring, 1916):**
> If $G$ is a bipartite graph with maximum degree $\Delta$, then:
> $$\chi'(G) = \Delta(G)$$

#### Formal Proof (by Induction on Number of Edges):
1. **Base Case:** For $|E| = 1$, $\Delta = 1$ and $\chi' = 1$.
2. **Inductive Step:** Suppose every bipartite graph with fewer than $m$ edges has $\chi' = \Delta$.
   Let $G$ have $m$ edges and maximum degree $\Delta$.
   Remove an edge $e = \{u, v\}$. In $G - e$, the maximum degree is $\le \Delta$.
   By the inductive hypothesis, $G - e$ has a proper edge coloring using $\Delta$ colors $\{1, 2, \dots, \Delta\}$.
   
   In this coloring of $G - e$:
   - $\deg_{G-e}(u) \le \Delta - 1$, so there is at least one color $\alpha \in \{1, \dots, \Delta\}$ missing at $u$.
   - $\deg_{G-e}(v) \le \Delta - 1$, so there is at least one color $\beta \in \{1, \dots, \Delta\}$ missing at $v$.
   
   - If $\alpha = \beta$: assign color $\alpha$ to edge $e$. This extends to a valid coloring of $G$.
   - If $\alpha \ne \beta$: color $\alpha$ is missing at $u$, and color $\beta$ is missing at $v$.
     Consider the maximal alternating path $P$ starting at $u$ consisting of edges alternately colored $\beta$ and $\alpha$.
     Because $G$ is bipartite, $P$ cannot loop back to $u$ (no odd cycles).
     Furthermore, because $\beta$ is missing at $v$, $P$ cannot end at $v$ with an edge of color $\beta$.
     Therefore, path $P$ does not reach vertex $v$!
     
     Swap colors $\alpha \leftrightarrow \beta$ along path $P$:
     - This preserves valid edge coloring everywhere.
     - At vertex $u$, the first edge of $P$ had color $\beta$, which now becomes $\alpha$.
     - Color $\beta$ is now missing at $u$ as well as at $v$!
     - Assign color $\beta$ to edge $e = \{u, v\}$.
   We have obtained a valid $\Delta$-edge coloring of $G$. Thus $\chi'(G) = \Delta$. $\blacksquare$

---

### 4. Vizing's Theorem (1964)

For general simple graphs, the chromatic index is constrained within a remarkably narrow window:

> **Theorem 8.7 (Vizing's Theorem, 1964):**
> For any simple graph $G$ with maximum degree $\Delta$:
> $$\Delta(G) \le \chi'(G) \le \Delta(G) + 1$$

Graphs fall into two universal structural classes:
- **Class 1 Graphs:** $\chi'(G) = \Delta(G)$ (e.g. bipartite graphs, complete graphs $K_{2n}$).
- **Class 2 Graphs:** $\chi'(G) = \Delta(G) + 1$ (e.g. odd cycles $C_{2k+1}$, complete graphs $K_{2n+1}$, Petersen graph).

> **Theorem 8.8 (Chromatic Index of Complete Graphs):**
> $$\chi'(K_n) = \begin{cases} n - 1 & \text{if } n \text{ is even (Class 1)} \\ n & \text{if } n \text{ is odd (Class 2)} \end{cases}$$"""
            },
            {
                "secNumber": "8.4",
                "title": "Network Flows, Residual Networks & Max-Flow Min-Cut Theorem",
                "content": r"""### 1. Flow Networks and Feasibility Conditions

Formulated by Lester R. Ford and Delbert R. Fulkerson in 1956, network flow theory provides the computational foundation for logistics, transportation, telecommunications, and combinatorial optimization.

> **Definition 8.5 (Flow Network):**
> A **flow network** is a directed graph $D = (V, E)$ with:
> 1. A designated **source** vertex $s \in V$ with indegree 0 (or net supply).
> 2. A designated **sink** vertex $t \in V$ with outdegree 0 (or net demand).
> 3. A non-negative capacity function $c: E \to \mathbb{R}_{\ge 0}$ assigning a maximum throughput $c(u, v)$ to each directed edge $(u, v) \in E$.

> **Definition 8.6 (Feasible Flow):**
> A **flow** is a function $f: E \to \mathbb{R}_{\ge 0}$ satisfying:
> 1. **Capacity Constraint:**
>    $$0 \le f(u, v) \le c(u, v) \quad \forall (u, v) \in E$$
> 2. **Flow Conservation (Kirchhoff's Current Law):**
>    $$\sum_{w \in V : (w, u) \in E} f(w, u) = \sum_{w \in V : (u, w) \in E} f(u, w) \quad \forall u \in V \setminus \{s, t\}$$

The total **value of the flow**, denoted $|f|$, is the net flow leaving the source:
$$|f| = \sum_{v : (s, v) \in E} f(s, v) - \sum_{v : (v, s) \in E} f(v, s)$$

---

### 2. Residual Networks and Augmenting Paths

> **Definition 8.7 (Residual Capacity and Residual Network):**
> Given a flow $f$ in network $D = (V, E)$, the **residual network** $D_f = (V, E_f)$ defines the available capacity on existing edges and reverse flow cancellation:
> - **Forward edge residual:** $c_f(u, v) = c(u, v) - f(u, v)$ (capacity to push more flow).
> - **Backward edge residual:** $c_f(v, u) = f(u, v)$ (capacity to cancel existing flow).
> An edge $(u, v)$ belongs to $E_f$ if and only if $c_f(u, v) > 0$.

An **augmenting path** is a simple directed path from source $s$ to sink $t$ in the residual network $D_f$.
The **bottleneck capacity** of an augmenting path $P$ is:
$$\gamma(P) = \min_{(u, v) \in P} c_f(u, v) > 0$$
Pushing $\gamma(P)$ flow along $P$ increases total flow $|f|$ by exactly $\gamma(P)$.

---

### 3. Cuts in Flow Networks and Weak Duality

> **Definition 8.8 ($s$-$t$ Cut and Cut Capacity):**
> An **$s$-$t$ cut** is a partition of vertices $V = S \cup T$ such that $s \in S$, $t \in T$, and $S \cap T = \emptyset$.
> The **capacity of the cut**, denoted $C(S, T)$, is the sum of capacities of edges directed from $S$ into $T$:
> $$C(S, T) = \sum_{u \in S, v \in T, (u, v) \in E} c(u, v)$$

> **Lemma 8.1 (Weak Duality of Network Flows):**
> For any feasible flow $f$ and any $s$-$t$ cut $(S, T)$:
> $$|f| \le C(S, T)$$

#### Proof:
Summing the flow conservation equations over all vertices $u \in S$:
$$\sum_{u \in S} \left( \sum_{v \in V} f(u, v) - \sum_{v \in V} f(v, u) \right) = |f|$$
Edges with both endpoints in $S$ cancel in the summation:
$$|f| = \sum_{u \in S, v \in T} f(u, v) - \sum_{u \in S, v \in T} f(v, u) \le \sum_{u \in S, v \in T} f(u, v) \le \sum_{u \in S, v \in T} c(u, v) = C(S, T) \quad \blacksquare$$

---

### 4. The Max-Flow Min-Cut Theorem (Ford & Fulkerson, 1956)

> **Theorem 8.9 (Max-Flow Min-Cut Theorem):**
> In any flow network $D = (V, E)$ with source $s$, sink $t$, and non-negative capacities $c$, the maximum value of an $s$-$t$ flow is equal to the minimum capacity of an $s$-$t$ cut:
> $$\max_f |f| = \min_{(S, T)} C(S, T)$$

#### Complete Formal Proof:
We prove the equivalence of the following three statements:
1. $f$ is a maximum flow in $D$.
2. The residual network $D_f$ contains no augmenting path from $s$ to $t$.
3. There exists an $s$-$t$ cut $(S, T)$ such that $|f| = C(S, T)$.

- **(1 $\implies$ 2):** If $D_f$ contained an augmenting path $P$, we could augment $f$ along $P$ by bottleneck $\gamma(P) > 0$, yielding a flow $f'$ with value $|f'| = |f| + \gamma(P) > |f|$, contradicting the maximality of $f$.
- **(2 $\implies$ 3):** Suppose $D_f$ contains no augmenting path from $s$ to $t$.
  Define $S$ as the set of all vertices reachable from $s$ via directed paths in the residual network $D_f$:
  $$S = \{ v \in V : \exists \text{ path from } s \text{ to } v \text{ in } D_f \}$$
  Let $T = V \setminus S$.
  Clearly $s \in S$. Since there is no augmenting path to $t$ in $D_f$, $t \notin S$, so $t \in T$. Thus $(S, T)$ is a valid $s$-$t$ cut.
  
  Now examine any edge $(u, v) \in E$ with $u \in S$ and $v \in T$:
  - If $f(u, v) < c(u, v)$, then $c_f(u, v) = c(u, v) - f(u, v) > 0$, meaning $(u, v) \in E_f$.
    Then since $u \in S$, $v$ would also be reachable from $s$ in $D_f$, placing $v \in S$, contradiction!
    Therefore, $f(u, v) = c(u, v)$ for all $u \in S, v \in T$.
  
  Similarly, examine any edge $(v, u) \in E$ with $v \in T$ and $u \in S$:
  - If $f(v, u) > 0$, then backward residual $c_f(u, v) = f(v, u) > 0$, meaning $(u, v) \in E_f$.
    Again $v$ would be reachable in $D_f$, placing $v \in S$, contradiction!
    Therefore, $f(v, u) = 0$ for all $v \in T, u \in S$.
  
  Substituting into the net flow equation across $(S, T)$:
  $$|f| = \sum_{u \in S, v \in T} f(u, v) - \sum_{v \in T, u \in S} f(v, u) = \sum_{u \in S, v \in T} c(u, v) - 0 = C(S, T)$$
- **(3 $\implies$ 1):** By Weak Duality (Lemma 8.1), $|f'| \le C(S, T)$ for every feasible flow $f'$.
  If $|f| = C(S, T)$, no flow can exceed $|f|$, hence $f$ is maximal. $\blacksquare$"""
            },
            {
                "secNumber": "8.5",
                "title": "Bipartite Matching, Hall's Marriage Theorem & Operations Research Applications",
                "content": r"""### 1. Matchings in Bipartite Graphs

> **Definition 8.9 (Matching and Maximum Matching):**
> Let $G = (V, E)$ be an undirected graph.
> 1. A **matching** $M \subseteq E$ is a set of pairwise non-adjacent edges (no two edges share a common vertex).
> 2. A vertex $v$ is **saturated** (or covered) by $M$ if some edge in $M$ is incident to $v$.
> 3. A matching $M$ is **maximum** if $|M| \ge |M'|$ for all matchings $M'$.
> 4. A matching $M$ is **perfect** if it saturates every vertex of $G$.

---

### 2. Hall's Marriage Theorem (1935)

Philip Hall established the definitive necessary and sufficient condition for the existence of a matching saturating one side of a bipartite graph:

> **Theorem 8.10 (Hall's Marriage Theorem, 1935):**
> Let $G = (X \cup Y, E)$ be a bipartite graph with bipartition sets $X$ and $Y$.
> For any subset $S \subseteq X$, let $N(S) = \bigcup_{v \in S} N(v) \subseteq Y$ denote the open neighborhood of $S$.
> Then $G$ has a matching saturating every vertex in $X$ if and only if **Hall's Condition** holds:
> $$\forall S \subseteq X, \quad |N(S)| \ge |S|$$

#### Complete Formal Proof via Network Flows and Max-Flow Min-Cut:
1. **Necessity ($\implies$):**
   Suppose there exists a matching $M$ saturating all vertices in $X$.
   Let $S \subseteq X$. Each vertex $u \in S$ is matched by $M$ to a distinct vertex $v_u \in Y$.
   Because $M \subseteq E$, each $v_u$ is a neighbor of $u$, so $\{v_u : u \in S\} \subseteq N(S)$.
   Since all $v_u$ are distinct, $|N(S)| \ge |\{v_u : u \in S\}| = |S|$.
   Hall's condition is strictly necessary.

2. **Sufficiency ($\impliedby$):**
   Assume Hall's Condition $|N(S)| \ge |S|$ holds for all $S \subseteq X$.
   Construct a flow network $D = (V', E')$ as follows:
   - Add a source vertex $s$ and a sink vertex $t$: $V' = \{s, t\} \cup X \cup Y$.
   - Add directed edges $(s, x)$ for all $x \in X$, each with capacity $c(s, x) = 1$.
   - For every edge $\{x, y\} \in E$ with $x \in X, y \in Y$, add directed edge $(x, y)$ with capacity $c(x, y) = \infty$.
   - Add directed edges $(y, t)$ for all $y \in Y$, each with capacity $c(y, t) = 1$.
   
   By the Integrality Theorem for Network Flows, the maximum flow value $|f^*|$ equals the size of the maximum bipartite matching in $G$.
   A matching saturating $X$ exists if and only if $|f^*| = |X|$.
   
   Suppose for contradiction that $|f^*| < |X|$.
   By the Max-Flow Min-Cut Theorem (Theorem 8.9), there exists an $s$-$t$ cut $(S', T')$ with capacity:
   $$C(S', T') = |f^*| < |X|$$
   
   Let $S_X = S' \cap X$ and $S_Y = S' \cap Y$.
   Edges crossing the cut from $S'$ to $T'$ consist of:
   - Edges from $s$ to $X \cap T'$: there are $|X \setminus S_X| = |X| - |S_X|$ such edges, each of capacity 1.
   - Edges from $S_X$ to $Y \cap T'$: if any edge $\{x, y\}$ has $x \in S_X$ and $y \in T'$, its capacity is $\infty$, making $C(S', T') = \infty$, which contradicts $C(S', T') < |X|$.
     Therefore, NO edges can go from $S_X$ to $Y \cap T'$, which means $N(S_X) \subseteq S_Y$!
   - Edges from $S_Y$ to $t$: there are $|S_Y|$ such edges, each of capacity 1.
   
   Summing the cut capacity:
   $$C(S', T') = (|X| - |S_X|) + |S_Y|$$
   Since $N(S_X) \subseteq S_Y$, we have $|S_Y| \ge |N(S_X)|$:
   $$C(S', T') \ge |X| - |S_X| + |N(S_X)|$$
   By Hall's Condition applied to the subset $S_X \subseteq X$, we have $|N(S_X)| \ge |S_X|$:
   $$C(S', T') \ge |X| - |S_X| + |S_X| = |X|$$
   This contradicts $C(S', T') < |X|$!
   
   Therefore, the minimum cut capacity must be at least $|X|$.
   Hence $|f^*| = |X|$, and an integral flow of value $|X|$ exists, providing a matching that saturates every vertex in $X$. $\blacksquare$

---

### 3. Operations Research Applications

The Max-Flow Min-Cut and Matching frameworks govern industrial optimization:
1. **Birkhoff-von Neumann Theorem:** Every doubly stochastic matrix is a convex combination of permutation matrices.
2. **Airline Crew & Job Scheduling:** Matching flights to crews subject to qualification constraints.
3. **Image Segmentation:** Min-cut graph cuts partition pixels into foreground and background.
4. **Stable Marriage & Gale-Shapley Algorithm:** Matching medical residents to hospitals under preference rankings."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Chromatic Number Calculation & Welsh-Powell Greedy Coloring",
                "statement": r"""Consider a graph $G = (V, E)$ with 7 vertices $V = \{v_1, v_2, v_3, v_4, v_5, v_6, v_7\}$ having vertex degrees:
$$\deg(v_1) = 5, \quad \deg(v_2) = 4, \quad \deg(v_3) = 4, \quad \deg(v_4) = 3, \quad \deg(v_5) = 3, \quad \deg(v_6) = 2, \quad \deg(v_7) = 1$$
Edges are:
$$\{v_1, v_2\}, \{v_1, v_3\}, \{v_1, v_4\}, \{v_1, v_5\}, \{v_1, v_6\}, \{v_2, v_3\}, \{v_2, v_4\}, \{v_2, v_7\}, \{v_3, v_5\}, \{v_4, v_5\}, \{v_5, v_6\}$$

1. Apply the **Welsh-Powell Algorithm** to find an upper bound on $\chi(G)$.
2. Determine the exact chromatic number $\chi(G)$ by identifying the largest clique $\omega(G)$.
3. Compare the result with Brooks' Theorem bound.""",
                "hints": [
                    "Order vertices in non-increasing order of degrees.",
                    "Assign the first color to the first uncolored vertex and greedily to all subsequent non-adjacent vertices.",
                    "Look for triangles (cliques of size 3) to establish a lower bound."
                ],
                "solution": r"""**Part 1: Welsh-Powell Greedy Algorithm Execution**

**Step 1: Order vertices by descending degree:**
$$\text{Order: } v_1 (\deg 5), \quad v_2 (\deg 4), \quad v_3 (\deg 4), \quad v_4 (\deg 3), \quad v_5 (\deg 3), \quad v_6 (\deg 2), \quad v_7 (\deg 1)$$

**Step 2: Assign Color 1 (Red):**
- Color $v_1$ with **Color 1**.
- Neighbors of $v_1$: $\{v_2, v_3, v_4, v_5, v_6\}$.
- $v_2, v_3, v_4, v_5, v_6$ are adjacent to $v_1$, so none can receive Color 1.
- Next vertex not adjacent to $v_1$ is $v_7$. Edge $\{v_1, v_7\} \notin E$.
- Assign $v_7$ with **Color 1**.
- Vertices colored with Color 1: $\{v_1, v_7\}$.

**Step 3: Assign Color 2 (Blue):**
- First uncolored vertex in the list is $v_2$. Color $v_2$ with **Color 2**.
- Neighbors of $v_2$: $\{v_1, v_3, v_4, v_7\}$.
- Check remaining uncolored vertices in order:
  - $v_3$: adjacent to $v_2$, skip.
  - $v_4$: adjacent to $v_2$, skip.
  - $v_5$: not adjacent to $v_2$ ($\{v_2, v_5\} \notin E$). Assign $v_5$ with **Color 2**!
  - $v_6$: adjacent to $v_5$, so check if adjacent to $v_2$. $\{v_2, v_6\} \notin E$, but $v_6$ is adjacent to $v_5$ which already has Color 2, skip.
- Vertices colored with Color 2: $\{v_2, v_5\}$.

**Step 4: Assign Color 3 (Green):**
- First uncolored vertex is $v_3$. Color $v_3$ with **Color 3**.
- Neighbors of $v_3$: $\{v_1, v_2, v_5\}$.
- Check remaining uncolored vertices:
  - $v_4$: $\{v_3, v_4\} \notin E$. Assign $v_4$ with **Color 3**!
  - $v_6$: $\{v_3, v_6\} \notin E$ and $\{v_4, v_6\} \notin E$. Assign $v_6$ with **Color 3**!
- Vertices colored with Color 3: $\{v_3, v_4, v_6\}$.

All 7 vertices are colored:
- Color 1: $\{v_1, v_7\}$
- Color 2: $\{v_2, v_5\}$
- Color 3: $\{v_3, v_4, v_6\}$

Welsh-Powell gives an upper bound: $\chi(G) \le 3$.

---

**Part 2: Exact Chromatic Number $\chi(G)$**

Observe the triangle induced by $\{v_1, v_2, v_3\}$:
- $\{v_1, v_2\} \in E$, $\{v_2, v_3\} \in E$, $\{v_1, v_3\} \in E$.
This is a clique of size 3: $K_3 \subseteq G$, so $\omega(G) \ge 3$.
By Theorem 8.1:
$$\chi(G) \ge \omega(G) \ge 3$$
Since we found an explicit valid 3-coloring, we have:
$$3 \le \chi(G) \le 3 \implies \chi(G) = 3$$

---

**Part 3: Comparison with Brooks' Theorem Bound**

- Maximum degree $\Delta(G) = \deg(v_1) = 5$.
- $G$ is not a complete graph ($n = 7 \ne \Delta + 1 = 6$) and not an odd cycle ($\Delta = 5 \ne 2$).
- Brooks' Theorem states $\chi(G) \le \Delta(G) = 5$.
Our exact chromatic number $\chi(G) = 3$ easily satisfies $\chi(G) \le 5$. $\blacksquare$"""
            },
            {
                "tier": "Advanced",
                "title": "Chromatic Polynomial Computation for the Wheel Graph $W_5$",
                "statement": r"""The wheel graph $W_n = C_{n-1} * K_1$ is obtained by joining a central apex vertex $w$ to all vertices of an outer cycle $C_{n-1}$.
Consider the wheel graph $W_5$ with 5 vertices (an apex connected to a 4-cycle $C_4$).

1. Compute the chromatic polynomial $P(W_5, k)$ using the apex reduction method.
2. Determine $P(W_5, k)$ via Deletion-Contraction on an outer cycle edge.
3. Find the number of valid proper 3-colorings and 4-colorings of $W_5$.""",
                "hints": [
                    "For apex reduction: if the apex receives 1 of k colors, how many colors remain available for the cycle?",
                    "Recall that P(C_4, m) = (m-1)^4 + (m-1). Substitute m = k - 1."
                ],
                "solution": r"""**Part 1: Apex Reduction Method**

In the wheel graph $W_5 = C_4 * K_1$, the apex vertex $w$ is adjacent to every vertex of the outer cycle $C_4$.
In any proper $k$-coloring of $W_5$:
1. The apex vertex $w$ can be assigned any of the $k$ available colors.
2. Once $w$ is assigned color $c(w)$, all 4 cycle vertices $\{v_1, v_2, v_3, v_4\}$ are adjacent to $w$ and cannot use color $c(w)$.
3. Therefore, the cycle vertices must be properly colored using the remaining $k - 1$ available colors.
4. The number of proper colorings of an outer cycle $C_4$ using $k - 1$ colors is precisely $P(C_4, k - 1)$.

Using the cycle formula from Section 8.2:
$$P(C_4, m) = (m-1)^4 + (-1)^4(m-1) = (m-1)^4 + (m-1)$$
Substitute $m = k - 1$:
$$P(C_4, k - 1) = ((k-1) - 1)^4 + ((k-1) - 1) = (k - 2)^4 + (k - 2)$$
Factoring out $(k - 2)$:
$$P(C_4, k - 1) = (k - 2) \left[ (k - 2)^3 + 1 \right]$$
Now multiply by the $k$ choices for the apex:
$$P(W_5, k) = k (k - 2) \left[ (k - 2)^3 + 1 \right] = k (k - 2) \left[ k^3 - 6k^2 + 12k - 8 + 1 \right]$$
$$P(W_5, k) = k (k - 2) (k^3 - 6k^2 + 12k - 7)$$

Expanding completely:
$$k (k-2) (k^3 - 6k^2 + 12k - 7) = (k^2 - 2k)(k^3 - 6k^2 + 12k - 7)$$
$$= k^5 - 6k^4 + 12k^3 - 7k^2 - 2k^4 + 12k^3 - 24k^2 + 14k$$
$$P(W_5, k) = k^5 - 8k^4 + 24k^3 - 31k^2 + 14k$$

Notice:
- Degree is 5 (matches $|V| = 5$).
- Monic leading coefficient is 1.
- Coefficient of $k^4$ is $-8$, which matches $-|E| = -(4 + 4) = -8$!

---

**Part 2: Verification via Deletion-Contraction**

Let $e$ be an edge of the outer 4-cycle $C_4$:
$$P(W_5, k) = P(W_5 - e, k) - P(W_5 / e, k)$$
- In $W_5 - e$, removing an outer edge turns the outer cycle into a path $P_4$.
  With apex $w$ receiving $k$ choices, $P_4$ has $P(P_4, k - 1) = (k-1)(k-2)^3$ colorings:
  $$P(W_5 - e, k) = k(k-1)(k-2)^3$$
- In $W_5 / e$, contracting an edge of $C_4$ turns $C_4$ into $C_3 \cong K_3$.
  Thus $W_5 / e \cong K_4$.
  $$P(W_5 / e, k) = P(K_4, k) = k(k-1)(k-2)(k-3)$$
- Subtracting:
  $$P(W_5, k) = k(k-1)(k-2)^3 - k(k-1)(k-2)(k-3)$$
  $$= k(k-1)(k-2) \left[ (k-2)^2 - (k-3) \right]$$
  $$= k(k-1)(k-2) \left[ k^2 - 4k + 4 - k + 3 \right]$$
  $$= k(k-1)(k-2) (k^2 - 5k + 7)$$
  $$= (k^3 - 3k^2 + 2k)(k^2 - 5k + 7) = k^5 - 8k^4 + 24k^3 - 31k^2 + 14k$$
Both methods match perfectly!

---

**Part 3: Evaluation for $k = 3$ and $k = 4$**

- For $k = 3$:
  $$P(W_5, 3) = 3(3-1)(3-2)(3^2 - 5(3) + 7) = 3(2)(1)(9 - 15 + 7) = 6(1) = 6$$
  There are exactly **6 proper 3-colorings** of $W_5$.
- For $k = 4$:
  $$P(W_5, 4) = 4(4-1)(4-2)(4^2 - 5(4) + 7) = 4(3)(2)(16 - 20 + 7) = 24(3) = 72$$
  There are exactly **72 proper 4-colorings** of $W_5$. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Complete Formal Proof of the Max-Flow Min-Cut and Menger Equivalence",
                "statement": r"""1. Provide the complete formal proof that the Max-Flow Min-Cut Theorem (Theorem 8.9) with unit capacities implies the edge form of Menger's Theorem (Theorem 4.6): in any directed multigraph, the maximum number of edge-disjoint paths from $s$ to $t$ equals the minimum size of an edge cut separating $s$ and $t$.
2. Prove the Integrality Theorem for Network Flows: if all edge capacities $c(u, v)$ are non-negative integers, then there exists a maximum flow $f^*$ such that $f^*(u, v) \in \mathbb{Z}$ for all edges $(u, v) \in E$.""",
                "hints": [
                    "For Part 1, assign unit capacity c(e) = 1 to every edge. Use flow decomposition into path flows.",
                    "For Part 2, perform induction on the iterations of the Ford-Fulkerson algorithm using integer bottlenecks."
                ],
                "solution": r"""**Part 1: Duality Proof — Max-Flow Min-Cut Implies Edge-Menger Theorem**

Let $D = (V, E)$ be a directed graph, and let $s, t \in V$ be distinct vertices.
Assign capacity $c(e) = 1$ to every directed edge $e \in E$.

**1. Step 1: Max-Flow in the Unit Network:**
By the Integrality Theorem (Part 2), since every capacity $c(e) \in \{1\}$, there exists a maximum flow $f^*$ such that:
$$f^*(e) \in \{0, 1\} \quad \forall e \in E$$
Let $k = |f^*|$ be the maximum flow value.

**2. Step 2: Flow Decomposition into Edge-Disjoint Paths:**
Let $E^* = \{ e \in E : f^*(e) = 1 \}$ be the set of saturated edges.
Because flow is conserved at every vertex $v \notin \{s, t\}$, the in-degree and out-degree within the subgraph $(V, E^*)$ satisfy:
$$\deg_{\text{in}}^*(v) = \deg_{\text{out}}^*(v) \quad \forall v \ne s, t$$
While at $s$: $\deg_{\text{out}}^*(s) - \deg_{\text{in}}^*(s) = k$, and at $t$: $\deg_{\text{in}}^*(t) - \deg_{\text{out}}^*(t) = k$.

By the Flow Decomposition Theorem:
Any non-negative circulatory/acyclic integer flow can be decomposed into a sum of directed path flows and directed cycle flows.
Removing any directed cycles leaves exactly $k$ directed paths $P_1, P_2, \dots, P_k$ from $s$ to $t$.
Because each edge $e$ has $f^*(e) \le 1$, no edge can belong to more than one path $P_i$.
Therefore, $P_1, P_2, \dots, P_k$ are **mutually edge-disjoint directed paths** from $s$ to $t$!
Hence:
$$\text{Max number of edge-disjoint } s\text{-}t \text{ paths} \ge k = |f^*|$$

Conversely, if there exist $p$ edge-disjoint paths from $s$ to $t$, sending 1 unit of flow along each path yields a feasible flow of value $p$, so $|f^*| \ge p$.
Thus:
$$\text{Max number of edge-disjoint } s\text{-}t \text{ paths} = |f^*|$$

**3. Step 3: Equivalence with Min-Cut:**
By the Max-Flow Min-Cut Theorem (Theorem 8.9):
$$|f^*| = \min_{(S, T)} C(S, T)$$
For any $s$-$t$ cut $(S, T)$ with $s \in S, t \in T$, the cut capacity is:
$$C(S, T) = \sum_{u \in S, v \in T, (u, v) \in E} c(u, v) = \sum_{u \in S, v \in T, (u, v) \in E} 1 = |\delta^+(S)|$$
where $\delta^+(S)$ is the set of directed edges directed from $S$ to $T$.
Deleting $\delta^+(S)$ removes all paths from $s$ to $t$, so $\delta^+(S)$ is an edge cut separating $s$ and $t$.
Therefore:
$$\min_{(S, T)} C(S, T) = \text{Min size of an edge cut separating } s \text{ from } t$$
Combining the equalities:
$$\text{Max edge-disjoint paths} = |f^*| = \min_{(S, T)} C(S, T) = \text{Min size of edge cut}$$
This proves Menger's Theorem (Theorem 4.6) as an exact corollary of Max-Flow Min-Cut duality! $\blacksquare$

---

**Part 2: Complete Proof of the Integrality Theorem**

Let $D = (V, E)$ be a network where $c(e) \in \mathbb{Z}_{\ge 0}$ for all $e \in E$.

We prove by induction on the number of augmentations in the Ford-Fulkerson algorithm:
1. **Base Case:** Initialize flow $f_0(e) = 0$ for all $e \in E$.
   Clearly $f_0(e) \in \mathbb{Z}$ for all $e \in E$, and $|f_0| = 0 \in \mathbb{Z}$.
2. **Inductive Step:**
   Assume after $k$ augmentations, the current flow $f_k$ is integer-valued: $f_k(e) \in \mathbb{Z}$ for all $e \in E$.
   In the residual network $D_{f_k}$:
   - Residual capacity for forward edge: $c_{f_k}(u, v) = c(u, v) - f_k(u, v) \in \mathbb{Z}$.
   - Residual capacity for backward edge: $c_{f_k}(v, u) = f_k(u, v) \in \mathbb{Z}$.
   All residual capacities in $D_{f_k}$ are non-negative integers!
   
   If no augmenting path exists from $s$ to $t$, the algorithm terminates, and $f_k$ is an integer maximum flow.
   If an augmenting path $P$ exists:
   The bottleneck capacity is:
   $$\gamma(P) = \min_{e \in P} c_{f_k}(e)$$
   Since the minimum of a finite set of positive integers is a positive integer, $\gamma(P) \in \mathbb{Z}^+ \ge 1$.
   
   The updated flow $f_{k+1}$ satisfies:
   $$f_{k+1}(e) = \begin{cases} f_k(e) + \gamma(P) & \text{if } e \text{ is a forward edge on } P \\ f_k(e) - \gamma(P) & \text{if } e \text{ is a backward edge on } P \\ f_k(e) & \text{otherwise} \end{cases}$$
   Since integers are closed under addition and subtraction, $f_{k+1}(e) \in \mathbb{Z}$ for all $e \in E$.
   Furthermore, the flow value increases by at least 1:
   $$|f_{k+1}| = |f_k| + \gamma(P) \ge |f_k| + 1$$
   Since $|f| \le C(\{s\}, V \setminus \{s\}) < \infty$, the algorithm must terminate in finitely many iterations.
   Upon termination, $f^*$ is an integer maximum flow. $\blacksquare$"""
            }
        ]
    }
    return u8

if __name__ == "__main__":
    u = get_unit8()
    print("Unit 8 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
