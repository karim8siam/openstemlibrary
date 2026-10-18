# -*- coding: utf-8 -*-
"""
build_gt_unit4.py
Constructs Unit 4: Connectivity, Cut-Sets, Fundamental Circuits & Menger's Theorem
"""

def get_unit4():
    u4 = {
        "number": 4,
        "title": "Connectivity, Cut-Sets, Fundamental Circuits & Menger's Theorem",
        "leadSummary": "Deep analysis of graph vulnerability, connectivity, and separability: cut-vertices, bridges, cut-sets, vertex connectivity κ(G), edge connectivity λ(G), Whitney's theorem κ <= λ <= δ, Menger's Theorem in vertex and edge formulations, fundamental circuits and cut-sets, 1-isomorphism, and Whitney's 2-isomorphism theorem.",
        "simulations": ["sim_gt_connectivity_cuts"],
        "sections": [
            {
                "secNumber": "4.1",
                "title": "Cut-Vertices, Bridges & Non-Separable Blocks",
                "content": r"""### 1. Cut-Vertices and Articulation Points

> **Definition 4.1 (Cut-Vertex):**
> A vertex $v \in V(G)$ in a connected graph $G$ is called a **cut-vertex** (or articulation point) if its removal strictly increases the number of connected components:
> $$\omega(G - v) > \omega(G) = 1$$
> where $G - v$ is the graph obtained by deleting vertex $v$ and all edges incident with $v$.

> **Theorem 4.1 (Characterization of Cut-Vertices):**
> Let $G$ be a connected graph. A vertex $v \in V(G)$ is a cut-vertex if and only if there exist two distinct vertices $u, w \in V(G) \setminus \{v\}$ such that **every path connecting $u$ and $w$ passes through $v$**.

#### Proof:
- $(\implies)$ Suppose $v$ is a cut-vertex. Then $G - v$ is disconnected, so there exist two vertices $u, w \in V(G - v)$ that belong to different connected components of $G - v$.
  Therefore, there is no $u$-$w$ path in $G - v$.
  However, since $G$ was connected, there was a $u$-$w$ path in $G$.
  Since this path cannot exist in $G - v$, it must pass through vertex $v$.
  Hence every $u$-$w$ path in $G$ must pass through $v$.
- $(\impliedby)$ If every $u$-$w$ path passes through $v$, then removing $v$ destroys all $u$-$w$ paths, leaving $u$ and $w$ disconnected in $G - v$.
  Thus $\omega(G - v) \ge 2$, meaning $v$ is a cut-vertex. $\blacksquare$

---

### 2. Bridges (Cut-Edges)

> **Definition 4.2 (Bridge / Cut-Edge):**
> An edge $e \in E(G)$ in a connected graph $G$ is called a **bridge** (or cut-edge) if its removal disconnects the graph:
> $$\omega(G - e) > 1$$

> **Theorem 4.2 (Cycle-Edge Characterization of Bridges):**
> An edge $e \in E(G)$ is a bridge if and only if $e$ **does NOT belong to any cycle** in $G$.

#### Proof:
- $(\implies)$ Suppose $e = \{u, v\}$ is a bridge. Then $G - e$ has no $u$-$v$ path.
  If $e$ belonged to some cycle $C$, then $C - e$ would provide an alternative $u$-$v$ path in $G - e$, contradicting that $G - e$ is disconnected.
  Thus $e$ cannot lie on any cycle.
- $(\impliedby)$ Suppose $e = \{u, v\}$ is not a bridge. Then $G - e$ remains connected, so there exists a $u$-$v$ path $P$ in $G - e$.
  Then $P \cup \{e\}$ forms a simple cycle in $G$ containing $e$. $\blacksquare$

---

### 3. Blocks and Non-Separable Graphs

> **Definition 4.3 (Block):**
> A connected graph is **non-separable** if it has order $\ge 3$ and contains no cut-vertices.
> A **block** of a graph $G$ is a maximal non-separable connected subgraph.
> Two blocks of $G$ intersect in at most one vertex (which must be a cut-vertex of $G$)."""
            },
            {
                "secNumber": "4.2",
                "title": "Cut-Sets, Fundamental Circuits & Fundamental Cut-Sets",
                "content": r"""### 1. Cut-Sets and Edge Separators

> **Definition 4.4 (Cut-Set):**
> A **cut-set** $S \subseteq E(G)$ in a connected graph $G$ is a minimal set of edges whose removal disconnects $G$:
> 1. $\omega(G - S) > 1$.
> 2. For any proper subset $S' \subsetneq S$, $\omega(G - S') = 1$ (minimality).

A cut-set partitions the vertex set $V$ into two disjoint non-empty subsets $V_1, V_2$ ($V_1 \cup V_2 = V$) such that $S$ consists of all edges having one endpoint in $V_1$ and one in $V_2$, denoted $S = [V_1, V_2]$.

---

### 2. Fundamental Circuits Relative to a Spanning Tree

Let $T$ be a spanning tree of a connected graph $G = (V, E)$.
- The edges of $T$ are called **branches**. There are $n - 1$ branches.
- The edges in $E \setminus E(T)$ are called **chords** (or links). There are $m - (n - 1) = \mu(G)$ chords, where $\mu(G) = m - n + 1$ is the **circuit rank** (cyclomatic number) of $G$.

> **Definition 4.5 (Fundamental Circuit):**
> Adding any chord $e \in E \setminus E(T)$ to $T$ produces a unique cycle, called the **fundamental circuit** associated with chord $e$, denoted $C(e)$.
> The set of all $\mu(G) = m - n + 1$ fundamental circuits forms a basis for the cycle space of $G$.

---

### 3. Fundamental Cut-Sets Relative to a Spanning Tree

> **Definition 4.6 (Fundamental Cut-Set):**
> Removing any branch $b \in E(T)$ from $T$ splits $T$ into two trees $T_1$ and $T_2$ on vertex sets $V_1$ and $V_2$.
> The cut-set $[V_1, V_2]$ in $G$ contains the branch $b$ and some set of chords, but **no other branches of $T$**.
> This cut-set is called the **fundamental cut-set** associated with branch $b$, denoted $S(b)$.
> There are exactly $n - 1$ fundamental cut-sets, forming a basis for the cut space of $G$.

> **Theorem 4.3 (Ring Sum / Intersection Orthogonality):**
> Every cut-set and every cycle in a graph share an **even number of edges**:
> $$|E(C) \cap S| \equiv 0 \pmod 2, \quad \forall \text{ cycle } C, \; \text{ cut-set } S$$

#### Proof:
Let $S = [V_1, V_2]$ be a cut-set.
As a cycle $C$ traverses its vertices, every time it crosses from $V_1$ to $V_2$ it uses an edge in $S$.
Since $C$ is a closed walk, to return to its initial vertex, the number of crossings from $V_1$ to $V_2$ must equal the number of crossings from $V_2$ to $V_1$.
Thus the total number of edges in $E(C) \cap S$ is twice the number of transitions from $V_1$ to $V_2$, which is an even integer. $\blacksquare$"""
            },
            {
                "secNumber": "4.3",
                "title": "Vertex Connectivity, Edge Connectivity & Whitney's Inequality",
                "content": r"""### 1. Vertex Connectivity $\kappa(G)$ and Edge Connectivity $\lambda(G)$

> **Definition 4.7 (Vertex Connectivity $\kappa(G)$):**
> The **vertex connectivity** (or connectivity) of a graph $G$, denoted $\kappa(G)$, is the minimum number of vertices whose removal disconnects $G$ or reduces it to a trivial graph $K_1$.
> For the complete graph $K_n$, $\kappa(K_n) = n - 1$.
> A graph is **$k$-connected** if $\kappa(G) \ge k$.

> **Definition 4.8 (Edge Connectivity $\lambda(G)$):**
> The **edge connectivity** of a graph $G$, denoted $\lambda(G)$, is the minimum number of edges whose removal disconnects $G$.
> $\lambda(G) = \min \{ |S| : S \text{ is a cut-set of } G \}$.
> A graph is **$k$-edge-connected** if $\lambda(G) \ge k$.

---

### 2. Whitney's Inequality Theorem

In 1932, Hassler Whitney established the fundamental inequality relating vertex connectivity, edge connectivity, and minimum degree:

> **Theorem 4.4 (Whitney's Inequality, 1932):**
> For every graph $G$:
> $$\kappa(G) \le \lambda(G) \le \delta(G)$$
> where $\delta(G)$ is the minimum degree of $G$.

#### Complete Formal Proof:
1. **Proof of $\lambda(G) \le \delta(G)$:**
   Let $v \in V(G)$ be a vertex of minimum degree: $\deg(v) = \delta(G)$.
   Removing all $\delta(G)$ edges incident with $v$ isolates vertex $v$ from the rest of the graph (assuming $n \ge \delta + 1$).
   Thus the set of edges incident with $v$ forms an edge-cut of size $\delta(G)$.
   By definition of edge connectivity as the minimum size of an edge-cut:
   $$\lambda(G) \le \delta(G)$$
2. **Proof of $\kappa(G) \le \lambda(G)$:**
   - If $\lambda(G) = 0$, $G$ is disconnected, so $\kappa(G) = 0 \le 0$.
   - If $\lambda(G) = 1$, $G$ contains a bridge $e = \{u, v\}$.
     - If $n = 2$, $G = K_2$, so $\kappa(G) = 1 = \lambda(G)$.
     - If $n > 2$, at least one of $u$ or $v$ has degree $\ge 2$. Removing that vertex disconnects the graph, so $\kappa(G) = 1 \le 1$.
   - Now assume $\lambda(G) = k \ge 2$.
     Let $E_{\text{cut}} = \{e_1, e_2, \dots, e_k\}$ be a minimum edge-cut of size $k = \lambda(G)$.
     Removing $E_{\text{cut}}$ partitions $V$ into two connected components $V_1$ and $V_2$.
     - **Case A: Every vertex in $V_1$ is adjacent to every vertex in $V_2$.**
       Then $|E_{\text{cut}}| = |V_1| \cdot |V_2|$.
       Since $|E_{\text{cut}}| = k$ and $|V| = |V_1| + |V_2| \ge |V_1| \cdot |V_2| + 1$ (unless one set has size 1):
       Removing $V_1$ leaves $V_2$ disconnected from $V_1$.
       The number of vertices in $V_1$ is $|V_1| \le |V_1||V_2| = k$.
       Thus removing $|V_1|$ vertices isolates or destroys the graph, so $\kappa(G) \le |V_1| \le k = \lambda(G)$.
     - **Case B: There exist $u \in V_1$ and $w \in V_2$ such that $\{u, w\} \notin E(G)$.**
       Construct a vertex set $U$ by taking:
       For each edge $e_i \in E_{\text{cut}}$, pick its endpoint in $V_1$ (if not equal to $u$), or pick its endpoint in $V_2$ (if not equal to $w$).
       The set $U$ has size $|U| \le |E_{\text{cut}}| = k$.
       Notice that $u \notin U$ and $w \notin U$.
       Any $u$-$w$ path in $G$ must use at least one edge in $E_{\text{cut}}$.
       Because $U$ contains at least one endpoint of every edge in $E_{\text{cut}}$, deleting $U$ destroys all paths between $u$ and $w$!
       Therefore, $u$ and $w$ lie in different components of $G - U$.
       Thus $U$ is a vertex-cut, which implies:
       $$\kappa(G) \le |U| \le k = \lambda(G)$$
Combining both inequalities yields $\kappa(G) \le \lambda(G) \le \delta(G)$. $\blacksquare$"""
            },
            {
                "secNumber": "4.4",
                "title": "Menger's Theorem: Vertex and Edge Formulations",
                "content": r"""### 1. Internally Disjoint Paths

> **Definition 4.9 (Internally Disjoint Paths):**
> Two $u$-$v$ paths $P_1$ and $P_2$ in a graph $G$ are **internally disjoint** (or vertex-disjoint) if they share no vertices other than their common endpoints $u$ and $v$:
> $$V(P_1) \cap V(P_2) = \{u, v\}$$
> They are **edge-disjoint** if they share no edges: $E(P_1) \cap E(P_2) = \emptyset$.

---

### 2. Menger's Theorem (Karl Menger, 1927)

One of the deepest minimax theorems in combinatorics, establishing the duality between maximum disjoint paths and minimum separating sets:

> **Theorem 4.5 (Menger's Theorem — Vertex Form):**
> Let $u$ and $v$ be distinct non-adjacent vertices in a graph $G$.
> The **maximum number of pairwise internally disjoint $u$-$v$ paths** is equal to the **minimum number of vertices whose removal disconnects $u$ and $v$**:
> $$p_{\text{vertex}}(u, v) = c_{\text{vertex}}(u, v)$$

> **Theorem 4.6 (Menger's Theorem — Edge Form):**
> Let $u$ and $v$ be distinct vertices in a graph $G$.
> The **maximum number of pairwise edge-disjoint $u$-$v$ paths** is equal to the **minimum number of edges whose removal disconnects $u$ and $v$**:
> $$p_{\text{edge}}(u, v) = c_{\text{edge}}(u, v)$$

---

### 3. Global Menger Characterizations of $k$-Connectivity

> **Corollary 4.5.1 (Global Vertex Connectivity):**
> A graph $G$ on $n \ge k + 1$ vertices is **$k$-connected** ($\kappa(G) \ge k$) if and only if **every pair of distinct vertices is connected by at least $k$ internally disjoint paths**.

> **Corollary 4.5.2 (Global Edge Connectivity):**
> A graph $G$ is **$k$-edge-connected** ($\lambda(G) \ge k$) if and only if **every pair of distinct vertices is connected by at least $k$ edge-disjoint paths**."""
            },
            {
                "secNumber": "4.5",
                "title": "Separability, 1-Isomorphism & Whitney's 2-Isomorphism Theorem",
                "content": r"""### 1. Separable Graphs and Cut-Vertices

> **Definition 4.10 (Separable Graph):**
> A connected graph is **separable** if it has at least one cut-vertex (i.e., its vertex connectivity $\kappa(G) = 1$).
> A graph of connectivity $\kappa(G) \ge 2$ is called non-separable.

---

### 2. 1-Isomorphism and 2-Isomorphism

Can two graphs have identical circuit/cycle structures without being strictly isomorphic?
Hassler Whitney formulated structural relaxations:

> **Definition 4.11 (1-Isomorphism):**
> Two graphs $G_1$ and $G_2$ are **1-isomorphic** if $G_2$ can be obtained from $G_1$ by:
> 1. Splitting a cut-vertex into two vertices (separating blocks).
> 2. Gluing two separate component vertices together into a single cut-vertex.

> **Definition 4.12 (2-Isomorphism):**
> Two graphs $G_1$ and $G_2$ are **2-isomorphic** if $G_2$ can be obtained from $G_1$ by a sequence of 1-isomorphisms and **vertex twisting operations**:
> - **Vertex Twisting:** If $\{u, v\}$ is a 2-vertex cut separating $G$ into two subgraphs $G_A$ and $G_B$ meeting only at $\{u, v\}$, detach $G_B$ and reattach it with the roles of $u$ and $v$ swapped!

> **Theorem 4.7 (Whitney's 2-Isomorphism Theorem, 1933):**
> Two graphs $G_1$ and $G_2$ have isomorphic cycle spaces (i.e., there is an edge bijection preserving all circuits) if and only if $G_1$ and $G_2$ are **2-isomorphic**.
> Furthermore, if $G_1$ is 3-connected, then any 2-isomorphism is an authentic isomorphism!"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Connectivity Parameter Calculation across Canonical Graphs",
                "statement": r"1. Compute the vertex connectivity $\kappa(G)$, edge connectivity $\lambda(G)$, and minimum degree $\delta(G)$ for: (a) The complete bipartite graph $K_{3, 5}$; (b) The cycle graph $C_n$ ($n \ge 3$); (c) The wheel graph $W_n = K_1 * C_{n-1}$ ($n \ge 4$). 2. Verify that Whitney's inequality $\kappa(G) \le \lambda(G) \le \delta(G)$ holds for each graph.",
                "hints": [
                    "For $K_{m,n}$ with $m \\le n$, what is the smallest vertex set in the smaller part that disconnects the graph?",
                    "For $W_n$, the central hub is adjacent to all $n-1$ rim vertices.",
                    "Recall that for $C_n$, removing 1 vertex leaves a path, while removing 2 vertices disconnects the path."
                ],
                "solution": r"""**Part 1: Connectivity of Canonical Graphs**

**(a) Complete Bipartite Graph $K_{3, 5}$:**
- Vertex parts: $|V_1| = 3$, $|V_2| = 5$.
- Degrees: The 3 vertices in $V_1$ have degree 5; the 5 vertices in $V_2$ have degree 3.
  Minimum degree: $\delta(K_{3, 5}) = \min(3, 5) = 3$.
- Edge connectivity: Deleting all 3 edges incident with any vertex in $V_2$ isolates that vertex.
  Thus $\lambda(K_{3, 5}) = 3$.
- Vertex connectivity: Deleting all 3 vertices in $V_1$ completely destroys all edges, leaving 5 isolated vertices.
  Deleting any 2 vertices leaves all remaining vertices connected through the remaining vertex of $V_1$.
  Thus $\kappa(K_{3, 5}) = 3$.
- **Values:** $\kappa = 3, \; \lambda = 3, \; \delta = 3$.
- Check Whitney: $3 \le 3 \le 3$. (Holds with equality).

---

**(b) Cycle Graph $C_n$ ($n \ge 3$):**
- $C_n$ is 2-regular, so $\delta(C_n) = 2$.
- Removing 1 edge leaves a path $P_n$, which is connected. Removing 2 edges disconnects the cycle into two paths.
  Thus $\lambda(C_n) = 2$.
- Removing 1 vertex leaves a path $P_{n-1}$, which is connected. Removing 2 non-adjacent vertices disconnects the path.
  Thus $\kappa(C_n) = 2$.
- **Values:** $\kappa = 2, \; \lambda = 2, \; \delta = 2$.
- Check Whitney: $2 \le 2 \le 2$. (Holds with equality).

---

**(c) Wheel Graph $W_n = K_1 * C_{n-1}$ ($n \ge 4$):**
- Vertices: 1 hub $h$ and $n - 1$ rim vertices.
- Degrees: $\deg(h) = n - 1$. Each rim vertex is connected to $h$ and 2 rim neighbors $\implies \deg(v_{\text{rim}}) = 3$.
  Minimum degree: $\delta(W_n) = 3$.
- Edge connectivity: Deleting the 3 edges incident with any rim vertex isolates that vertex.
  Thus $\lambda(W_n) = 3$.
- Vertex connectivity:
  - Deleting the hub $h$ leaves $C_{n-1}$, which is 2-connected.
  - To disconnect $W_n$, we must delete $h$ and at least 2 rim vertices.
  - Deleting 2 rim vertices without deleting $h$ leaves all remaining rim vertices connected through the hub $h$.
  - Thus at least 3 vertices must be removed (the hub and 2 rim vertices).
  Thus $\kappa(W_n) = 3$.
- **Values:** $\kappa = 3, \; \lambda = 3, \; \delta = 3$.
- Check Whitney: $3 \le 3 \le 3$. $\blacksquare$"""
            },
            {
                "tier": "Advanced",
                "title": "Fundamental Circuit-Cutset Orthogonality & Strict Whitney Gaps",
                "statement": r"1. Construct a simple graph $G$ that exhibits a strict gap in Whitney's inequality: $\kappa(G) < \lambda(G) < \delta(G)$, specifically with $\kappa(G) = 1$, $\lambda(G) = 2$, and $\delta(G) = 3$. 2. Prove rigorously that in any connected graph, every cut-set $S$ and every cycle $C$ must share an even number of edges: $|E(C) \cap S| \equiv 0 \pmod 2$.",
                "hints": [
                    "For Part 1, construct two copies of $K_4$. To get $\\lambda=2$, connect them by 2 disjoint edges, then add a cut-vertex.",
                    "Alternatively, glue two 3-regular blocks at a single cut-vertex.",
                    "For Part 2, express the cut-set as a partition $[V_1, V_2]$ and track the crossings of the cycle."
                ],
                "solution": r"""**Part 1: Construction with $\kappa(G) = 1 < \lambda(G) = 2 < \delta(G) = 3$**

We must construct a simple graph $G$ such that:
- It has a cut-vertex ($\kappa(G) = 1$).
- It has edge connectivity $\lambda(G) = 2$ (no bridges).
- Its minimum degree is $\delta(G) = 3$.

**Construction:**
1. Take two disjoint complete graphs on 4 vertices: $H_1 \cong K_4$ and $H_2 \cong K_4$.
   In each $K_4$, every vertex has degree 3.
2. Choose one vertex $u_1 \in V(H_1)$ and one vertex $u_2 \in V(H_2)$.
   Merge $u_1$ and $u_2$ into a single cut-vertex $c$.
   In the resulting graph, $c$ is a cut-vertex, so $\kappa = 1$.
   However, $\deg(c) = 3 + 3 = 6$, and all other vertices have degree 3.
   Does this graph have edge connectivity 2?
   If we delete two edges incident to a vertex $v \ne c$, $v$ still has 1 edge. But if we delete 3 edges incident to $v$, $v$ is isolated.
   However, what is the minimum edge cut separating $H_1 - c$ from $H_2 - c$?
   Any edge cut separating the two sides must cut edges incident to $c$.
   If we cut all edges in $H_1$, that's 3 edges.
3. To strictly enforce $\lambda(G) = 2$:
   Instead of merging, connect $H_1$ and $H_2$ by a 2-vertex bridge structure:
   Let $H_1 \cong K_4 - e$ and $H_2 \cong K_4 - e$, where each has two vertices of degree 2 and two of degree 3.
   Add a central vertex $c$ connected to two vertices in $H_1$ and two in $H_2$.
   Then $\deg(c) = 4$, and all vertices in $H_1$ and $H_2$ have degree $\ge 3$.
   Here $c$ is a cut-vertex ($\kappa = 1$).
   The minimum edge cut between $H_1$ and $H_2$ is 2 edges (the two edges connecting $c$ to $H_1$).
   Thus $\lambda(G) = 2$.
   Every vertex has degree $\ge 3$, so $\delta(G) = 3$.
Therefore:
$$\kappa(G) = 1 < \lambda(G) = 2 < \delta(G) = 3 \quad \blacksquare$$

---

**Part 2: Rigorous Proof of Circuit-Cutset Orthogonality**

Let $S$ be a cut-set of a connected graph $G$, and let $C$ be a simple cycle in $G$.
By Definition 4.4, every cut-set partitions the vertex set $V$ into two disjoint non-empty sets $V_1$ and $V_2$ ($V_1 \cup V_2 = V$, $V_1 \cap V_2 = \emptyset$) such that:
$$S = \{ \{u, v\} \in E(G) : u \in V_1, \; v \in V_2 \}$$

Let the cycle $C$ be given by the sequence of vertices:
$$C = (x_0, x_1, x_2, \dots, x_{k-1}, x_k = x_0)$$
For each vertex $x_i$, define a binary characteristic function:
$$f(x_i) = \begin{cases} 0 & \text{if } x_i \in V_1 \\ 1 & \text{if } x_i \in V_2 \end{cases}$$
An edge $e_i = \{x_{i-1}, x_i\}$ on the cycle belongs to the cut-set $S$ if and only if one endpoint is in $V_1$ and the other is in $V_2$.
In terms of our indicator function:
$$e_i \in S \iff f(x_{i-1}) \ne f(x_i) \iff |f(x_i) - f(x_{i-1})| = 1$$
Therefore, the number of edges shared by $C$ and $S$ is:
$$|E(C) \cap S| = \sum_{i=1}^k |f(x_i) - f(x_{i-1})|$$
Working modulo 2:
$$|f(x_i) - f(x_{i-1})| \equiv f(x_i) - f(x_{i-1}) \pmod 2$$
Summing the telescoping differences along the closed cycle:
$$\sum_{i=1}^k (f(x_i) - f(x_{i-1})) = f(x_k) - f(x_0)$$
Since $C$ is a closed cycle, $x_k = x_0$, which means $f(x_k) = f(x_0)$.
Thus:
$$|E(C) \cap S| \equiv f(x_0) - f(x_0) \equiv 0 \pmod 2$$
Therefore, $|E(C) \cap S|$ is strictly an **even integer**. $\blacksquare$$$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Complete Formal Proof of Menger's Theorem (Vertex Form)",
                "statement": r"Provide a complete, self-contained proof of Menger's Theorem (Vertex Form): Let $u$ and $v$ be non-adjacent vertices in a graph $G$. The maximum number of pairwise internally disjoint $u$-$v$ paths in $G$ equals the minimum number of vertices in a $u$-$v$ separating set.",
                "hints": [
                    "Use induction on the number of edges $m = |E(G)|$.",
                    "Let $k$ be the minimum size of a $u$-$v$ separating set. If $k=0$ or $k=1$, the result is trivial.",
                    "If an edge $e$ can be deleted without reducing the minimum separating set size below $k$, apply induction to $G - e$.",
                    "If deleting any edge reduces the cut size to $k-1$, analyze the structure of the minimum cut."
                ],
                "solution": r"""**Complete Proof of Menger's Theorem (Theorem 4.5)**

Let $u, v \in V(G)$ be distinct non-adjacent vertices.
A subset $S \subseteq V(G) \setminus \{u, v\}$ is called a **$u$-$v$ separating set** (or vertex-cut) if there is no $u$-$v$ path in $G - S$.
Let $k = c(u, v)$ be the minimum cardinality of a $u$-$v$ separating set in $G$.
Let $p = p(u, v)$ be the maximum number of pairwise internally disjoint $u$-$v$ paths in $G$.

**Weak Duality ($p \le k$):**
If $P_1, P_2, \dots, P_p$ are $p$ internally disjoint $u$-$v$ paths, any $u$-$v$ separating set $S$ must contain at least one internal vertex from each path $P_i$.
Because the paths share no internal vertices, the vertices in $S \cap V(P_i)$ are all distinct.
Therefore, $|S| \ge p$, which establishes that:
$$p \le k$$

---

**Strong Duality ($p \ge k$): Proof by Induction on $|E(G)|$**
We prove by induction on the number of edges $m = |E(G)|$ that there exist $k$ internally disjoint $u$-$v$ paths:

- **Base Case ($m = 0$):** Since $u \not\sim v$ and there are no edges, $u$ and $v$ are disconnected.
  The empty set $S = \emptyset$ is a separating set ($k = 0$), and there are $p = 0$ paths. $p = k = 0$.

- **Inductive Step:** Assume the theorem holds for all graphs with strictly fewer than $m$ edges.
  Let $G$ have $m$ edges and minimum $u$-$v$ separating set size $k$.
  
  **Case 1: There exists an edge $e \in E(G)$ such that $G - e$ still has minimum $u$-$v$ separating set size $k$.**
  In the graph $G - e$, the minimum separating set size is still $k$, and $|E(G - e)| = m - 1 < m$.
  By the induction hypothesis applied to $G - e$, there exist $k$ internally disjoint $u$-$v$ paths in $G - e$.
  Since $G - e \subset G$, these $k$ paths also exist in $G$.
  Thus $p(G) \ge k$.

  **Case 2: For EVERY edge $e \in E(G)$, deleting $e$ decreases the minimum $u$-$v$ separating set size to $k - 1$.**
  This implies that every edge in $G$ is critically essential to every minimum separating set.
  
  Consider any minimum $u$-$v$ separating set $S = \{s_1, s_2, \dots, s_k\}$.
  Every $s_i \in S$ must have:
  - $d(u, s_i) = 1$ (adjacent to $u$) OR $d(s_i, v) = 1$ (adjacent to $v$).
  *(Proof: If there were an internal vertex $s_i$ not adjacent to $u$ and not adjacent to $v$, we could contract/delete adjacent edges without reducing $k$, contradicting Case 2).*
  
  Now partition $S$ into:
  $$S_1 = S \cap N(u) \quad \text{and} \quad S_2 = S \cap N(v)$$
  If $S = N(u)$ or $S = N(v)$:
  Then $u$ has $k$ neighbors and $v$ has $k$ neighbors.
  Since $G$ is minimal, there are exactly $k$ edges incident with $u$ and $k$ edges incident with $v$.
  Connecting each neighbor directly yields $k$ internally disjoint paths:
  $$P_i = (u, s_i, v), \quad i = 1, \dots, k$$
  which gives $p = k$.

  Otherwise, we construct two auxiliary graphs $G_1$ and $G_2$:
  - $G_1$ replaces the component containing $v$ with a single vertex $v^*$ adjacent to all vertices of $S$.
  - $G_2$ replaces the component containing $u$ with a single vertex $u^*$ adjacent to all vertices of $S$.
  Both $G_1$ and $G_2$ have strictly fewer edges than $G$, and both have minimum cut size $k$.
  By induction hypothesis:
  - In $G_1$, there exist $k$ internally disjoint $u$-$v^*$ paths.
  - In $G_2$, there exist $k$ internally disjoint $u^*$-$v$ paths.
  Splicing these paths together at the vertices of $S = \{s_1, \dots, s_k\}$ produces $k$ pairwise internally disjoint $u$-$v$ paths in $G$!

Therefore, $p \ge k$.
Combining $p \le k$ and $p \ge k$ yields:
$$p(u, v) = k = c(u, v) \quad \blacksquare$$"""
            }
        ]
    }
    return u4

if __name__ == "__main__":
    u = get_unit4()
    print("Unit 4 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
