# -*- coding: utf-8 -*-
"""
build_gt_unit1.py
Constructs Unit 1: Foundations of Graph Theory, Degree Sequences & Handshaking Theorems
"""

def get_unit1():
    u1 = {
        "number": 1,
        "title": "Foundations of Graph Theory, Degree Sequences & Handshaking Theorems",
        "leadSummary": "Comprehensive axiomatic introduction to graph theory: graph definitions, vertex sets, edge sets, simple graphs, multigraphs, pseudographs, bipartite and complete graphs, degrees of vertices, Euler's Handshaking Lemma, the Havel-Hakimi theorem for graphic degree sequences, and graph isomorphism.",
        "simulations": ["sim_gt_graph_builder"],
        "sections": [
            {
                "secNumber": "1.1",
                "title": "Formal Definitions of Graphs, Incidence & Graph Taxonomies",
                "content": r"""### 1. The Mathematical Definition of a Graph

Graph theory is the mathematical framework dedicated to modeling pairwise relations between objects. Historically founded by Leonhard Euler in 1736 with his resolution of the Königsberg bridge problem, a graph abstracts away physical geometries to focus purely on topological connectivity.

> **Definition 1.1 (Graph):**
> A **graph** $G$ is an ordered triple $G = (V(G), E(G), \psi_G)$ (or simply an ordered pair $G = (V, E)$ when unambiguous) consisting of:
> 1. A non-empty set $V(G) = \{v_1, v_2, \dots, v_n\}$ whose elements are called **vertices** (or nodes). The cardinality $|V(G)| = n$ is the **order** of $G$.
> 2. A set $E(G) = \{e_1, e_2, \dots, e_m\}$ whose elements are called **edges** (or lines). The cardinality $|E(G)| = m$ is the **size** of $G$.
> 3. An **incidence function** $\psi_G: E(G) \to \mathcal{P}_2(V(G)) \cup V(G)$ that associates each edge $e \in E(G)$ with an unordered pair of vertices $\{u, v\} \subseteq V(G)$.

If $\psi_G(e) = \{u, v\}$, we say that edge $e$ **joins** vertices $u$ and $v$. Vertices $u$ and $v$ are called the **endpoints** of $e$. Furthermore:
- Vertices $u$ and $v$ are said to be **adjacent** (or neighbors), denoted $u \sim v$.
- The edge $e$ and each of its endpoint vertices $u, v$ are said to be **incident** with each other.

---

### 2. Edge Typologies and Graph Classifications

> **Definition 1.2 (Self-Loops and Multiple Edges):**
> 1. A **self-loop** (or loop) is an edge whose endpoints are identical: $\psi_G(e) = \{u, u\} = \{u\}$.
> 2. **Multiple edges** (or parallel edges) are two or more distinct edges $e_1, e_2 \in E(G)$ ($e_1 \ne e_2$) having identical endpoints: $\psi_G(e_1) = \psi_G(e_2) = \{u, v\}$.

Based on the permissible edge configurations, we classify graphs into distinct categories:
- **Simple Graph:** A graph having **neither loops nor parallel edges**. In a simple graph, every edge can be identified directly with a 2-element subset $\{u, v\} \in \binom{V}{2}$, and $E \subseteq \binom{V}{2}$.
- **Multigraph:** A graph that permits multiple edges between pairs of vertices, but contains no loops.
- **Pseudograph:** A general graph that permits both multiple edges and self-loops.
- **Finite vs. Infinite Graph:** A graph is finite if both $V(G)$ and $E(G)$ are finite sets. Throughout this textbook, all graphs are assumed to be finite unless explicitly stated otherwise.
- **Null Graph (Empty Graph):** A graph with an edge set $E = \emptyset$, denoted $N_n$ for $n$ isolated vertices.
- **Trivial Graph:** A graph containing exactly one vertex and no edges: $V = \{v\}$, $E = \emptyset$ ($K_1$)."""
            },
            {
                "secNumber": "1.2",
                "title": "Vertex Degrees, Euler's Handshaking Lemma & The Odd Degree Theorem",
                "content": r"""### 1. Degree of a Vertex and Neighborhoods

> **Definition 1.3 (Open and Closed Neighborhoods):**
> Let $G = (V, E)$ be a simple graph and $v \in V$.
> 1. The **open neighborhood** of $v$, denoted $N(v)$ or $N_G(v)$, is the set of all vertices adjacent to $v$:
>    $$N(v) = \{ u \in V : \{u, v\} \in E \}$$
> 2. The **closed neighborhood** of $v$, denoted $N[v]$, includes $v$ itself:
>    $$N[v] = N(v) \cup \{v\}$$

> **Definition 1.4 (Degree of a Vertex):**
> The **degree** (or valency) of a vertex $v \in V(G)$, denoted $\deg(v)$, $\deg_G(v)$, or $d(v)$, is the number of edges incident with $v$.
> In pseudographs, a **self-loop contributes 2** to the degree of its incident vertex (since both endpoints meet at $v$).

#### Extreme Degrees:
- The **minimum degree** of $G$ is $\delta(G) = \min \{ \deg(v) : v \in V \}$.
- The **maximum degree** of $G$ is $\Delta(G) = \max \{ \deg(v) : v \in V \}$.
- A vertex $v$ with $\deg(v) = 0$ is called an **isolated vertex**.
- A vertex $v$ with $\deg(v) = 1$ is called a **pendant vertex** (or leaf).

---

### 2. Euler's Handshaking Lemma

The very first theorem of graph theory, established by Leonhard Euler in 1736:

> **Theorem 1.1 (Euler's Handshaking Lemma):**
> Let $G = (V, E)$ be any graph with vertex set $V$ and edge set $E$. The sum of the degrees of all vertices in $G$ is equal to twice the number of edges:
> $$\sum_{v \in V} \deg(v) = 2 |E|$$

#### Complete Formal Proof (Double Counting):
Consider the set of all incidence pairs:
$$\mathcal{I} = \{ (v, e) \in V \times E : \text{vertex } v \text{ is incident with edge } e \}$$
We count the cardinality $|\mathcal{I}|$ in two distinct ways:
1. **Summing by vertices:**
   For each fixed vertex $v \in V$, the number of incident edges is by definition $\deg(v)$ (with loops counted twice).
   Summing over all vertices:
   $$|\mathcal{I}| = \sum_{v \in V} \deg(v)$$
2. **Summing by edges:**
   For each fixed edge $e \in E$, $e$ has exactly two endpoints (either two distinct vertices $u \ne v$, or one vertex counted twice if $e$ is a loop).
   Therefore, each edge contributes exactly 2 incidence pairs to $\mathcal{I}$.
   Summing over all edges:
   $$|\mathcal{I}| = \sum_{e \in E} 2 = 2 |E|$$
Equating the two counts yields:
$$\sum_{v \in V} \deg(v) = 2 |E| \quad \blacksquare$$

---

### 3. The Odd Degree Corollary

> **Corollary 1.1 (The Handshaking Corollary):**
> In every graph $G$, the number of vertices having odd degree is **even**.

#### Complete Formal Proof:
Partition the vertex set $V$ into two disjoint subsets:
$$V_{\text{even}} = \{ v \in V : \deg(v) \text{ is even} \}$$
$$V_{\text{odd}} = \{ v \in V : \deg(v) \text{ is odd} \}$$
By the Handshaking Lemma:
$$\sum_{v \in V} \deg(v) = \sum_{v \in V_{\text{even}}} \deg(v) + \sum_{v \in V_{\text{odd}}} \deg(v) = 2 |E|$$
Rearranging:
$$\sum_{v \in V_{\text{odd}}} \deg(v) = 2 |E| - \sum_{v \in V_{\text{even}}} \deg(v)$$
Notice that $2 |E|$ is an even integer.
Furthermore, each term $\deg(v)$ in $\sum_{v \in V_{\text{even}}} \deg(v)$ is even, so the sum of even integers is even.
The difference of two even integers is even:
$$\sum_{v \in V_{\text{odd}}} \deg(v) \equiv 0 \pmod 2$$
The left side is a sum of odd integers. A sum of odd integers is even if and only if the number of terms in the sum is **even**.
Therefore, $|V_{\text{odd}}|$ must be an even integer. $\blacksquare$"""
            },
            {
                "secNumber": "1.3",
                "title": "Canonical Graph Families: Complete, Bipartite, Regular & Hypercubes",
                "content": r"""### 1. Complete Graphs $K_n$

> **Definition 1.5 (Complete Graph):**
> A **complete graph** on $n$ vertices, denoted $K_n$, is a simple graph in which every pair of distinct vertices is connected by an edge.
> - Number of vertices: $|V(K_n)| = n$.
> - Number of edges: $|E(K_n)| = \binom{n}{2} = \frac{n(n - 1)}{2}$.
> - Degree of each vertex: $\deg(v) = n - 1$ for all $v \in V(K_n)$.

---

### 2. Regular Graphs

> **Definition 1.6 ($k$-Regular Graph):**
> A graph $G$ is called **$k$-regular** if every vertex has the same degree $k$:
> $$\deg(v) = k, \quad \forall v \in V(G)$$

By the Handshaking Lemma, for any $k$-regular graph on $n$ vertices:
$$\sum_{v \in V} k = n \cdot k = 2 |E| \implies |E| = \frac{n \cdot k}{2}$$
A necessary condition for the existence of a $k$-regular graph on $n$ vertices is that $n \cdot k$ must be an even integer (i.e., if $k$ is odd, $n$ must be even).

---

### 3. Bipartite Graphs and Complete Bipartite Graphs $K_{m,n}$

> **Definition 1.7 (Bipartite Graph):**
> A graph $G = (V, E)$ is **bipartite** if its vertex set $V$ can be partitioned into two disjoint non-empty sets $V_1$ and $V_2$ ($V = V_1 \cup V_2$, $V_1 \cap V_2 = \emptyset$) such that every edge in $E$ joins a vertex in $V_1$ to a vertex in $V_2$.
> No edge connects two vertices within the same part $V_1$ or $V_2$.

> **Definition 1.8 (Complete Bipartite Graph $K_{m, n}$):**
> A **complete bipartite graph**, denoted $K_{m, n}$, is a bipartite graph with partition sets of sizes $|V_1| = m$ and $|V_2| = n$ such that every vertex in $V_1$ is connected to every vertex in $V_2$.
> - Number of vertices: $|V(K_{m,n})| = m + n$.
> - Number of edges: $|E(K_{m,n})| = m \cdot n$.
> - Star Graph: $K_{1, n}$ consists of one central vertex connected to $n$ leaves.

---

### 4. Hypercube Graphs $Q_k$

> **Definition 1.9 ($k$-Dimensional Hypercube $Q_k$):**
> The **$k$-cube** $Q_k$ is the simple graph whose vertices are all binary strings of length $k$:
> $$V(Q_k) = \{ (b_1, b_2, \dots, b_k) : b_i \in \{0, 1\} \}$$
> Two vertices are adjacent if and only if their binary strings differ in exactly one coordinate (Hamming distance 1).
> - Number of vertices: $|V(Q_k)| = 2^k$.
> - Degree of each vertex: $\deg(v) = k$ (every $Q_k$ is $k$-regular).
> - Total edges: $|E(Q_k)| = \frac{2^k \cdot k}{2} = k \cdot 2^{k-1}$.
> - $Q_k$ is bipartite (partitioned by strings of even vs. odd Hamming weight)."""
            },
            {
                "secNumber": "1.4",
                "title": "Degree Sequences, Graphical Realizability & The Havel-Hakimi Theorem",
                "content": r"""### 1. Degree Sequences and the Realizability Problem

> **Definition 1.10 (Degree Sequence):**
> Let $G$ be a simple graph of order $n$. The **degree sequence** of $G$ is a monotonic non-increasing sequence of non-negative integers:
> $$d = (d_1, d_2, \dots, d_n) \quad \text{such that } d_1 \ge d_2 \ge \dots \ge d_n \ge 0$$
> where each $d_i = \deg(v_i)$ for some labeling of vertices $V(G) = \{v_1, \dots, v_n\}$.

#### The Graphical Realizability Question:
Given an arbitrary sequence of non-negative integers $S = (s_1, s_2, \dots, s_n)$, does there exist a **simple graph** $G$ whose degree sequence is precisely $S$?
If such a simple graph exists, the sequence $S$ is called **graphic** (or graphical).

**Elementary Necessary Conditions for a Graphic Sequence:**
1. $\sum_{i=1}^n s_i$ must be an even integer (Handshaking Lemma).
2. $s_1 \le n - 1$ (no vertex in a simple graph of order $n$ can have degree $\ge n$).

---

### 2. The Havel-Hakimi Theorem

Published independently by Václav Havel (1955) and S. Louis Hakimi (1962), this theorem provides a recursive algorithmic characterization that decides whether a sequence is graphic in polynomial time.

> **Theorem 1.2 (Havel-Hakimi Theorem):**
> Let $S = (d_1, d_2, \dots, d_n)$ be a non-increasing sequence of non-negative integers with $n \ge 2$ and $d_1 \ge 1$.
> Define the reduced sequence $S'$ by deleting the first element $d_1$ and subtracting $1$ from each of the next $d_1$ elements:
> $$S' = (d_2 - 1, \; d_3 - 1, \; \dots, \; d_{d_1 + 1} - 1, \; d_{d_1 + 2}, \; \dots, \; d_n)$$
> Then $S$ is **graphic** if and only if the rearranged non-increasing sequence $S'$ is **graphic**.

#### Complete Proof of the Havel-Hakimi Theorem:
- **$(\impliedby)$ Direction (Sufficiency):**
  Suppose $S'$ is graphic. Then there exists a simple graph $G'$ with vertex set $V' = \{v_2, v_3, \dots, v_n\}$ having degree sequence $S'$:
  $$\deg_{G'}(v_i) = d_i - 1 \quad \text{for } 2 \le i \le d_1 + 1$$
  $$\deg_{G'}(v_i) = d_i \quad \text{for } d_1 + 2 \le i \le n$$
  Construct a new graph $G$ by adding a new vertex $v_1$ and connecting $v_1$ to the $d_1$ vertices $\{v_2, v_3, \dots, v_{d_1 + 1}\}$.
  Then:
  - $\deg_G(v_1) = d_1$.
  - For $2 \le i \le d_1 + 1$: $\deg_G(v_i) = \deg_{G'}(v_i) + 1 = (d_i - 1) + 1 = d_i$.
  - For $d_1 + 2 \le i \le n$: $\deg_G(v_i) = \deg_{G'}(v_i) = d_i$.
  Thus $G$ is a simple graph whose degree sequence is $S$. Hence $S$ is graphic.

- **$(\implies)$ Direction (Necessity):**
  Suppose $S$ is graphic. Among all simple graphs having degree sequence $S$, choose a graph $G = (V, E)$ with $V = \{v_1, v_2, \dots, v_n\}$ and $\deg(v_i) = d_i$ such that the neighborhood $N(v_1)$ contains the **maximum possible number of vertices from the target set** $T = \{v_2, v_3, \dots, v_{d_1 + 1}\}$.
  - If $N(v_1) = T$, we are done: deleting $v_1$ yields a graph $G' = G - v_1$ whose degree sequence is precisely $S'$.
  - Suppose $N(v_1) \ne T$. Since $|N(v_1)| = d_1 = |T|$, there must exist vertices $v_j \in T$ and $v_k \notin T$ such that:
    $$v_1 \sim v_k \quad \text{and} \quad v_1 \not\sim v_j$$
    Because $v_j \in T$ and $v_k \notin T$, the indices satisfy $j < k$, which implies:
    $$d_j = \deg(v_j) \ge \deg(v_k) = d_k$$
    Since $v_1 \sim v_k$ but $v_1 \not\sim v_j$, vertex $v_j$ has degree $\ge d_k$, so $v_j$ must have neighbors outside of $N(v_k) \cup \{v_1\}$.
    Specifically, there must exist some vertex $v_r \in V \setminus \{v_1, v_j, v_k\}$ such that:
    $$v_j \sim v_r \quad \text{and} \quad v_k \not\sim v_r$$
    Now perform a **2-switch (edge interchange)**:
    Delete the edges $\{v_1, v_k\}$ and $\{v_j, v_r\}$, and add the edges $\{v_1, v_j\}$ and $\{v_k, v_r\}$:
    $$E_{\text{new}} = (E \setminus \{ \{v_1, v_k\}, \{v_j, v_r\} \}) \cup \{ \{v_1, v_j\}, \{v_k, v_r\} \}$$
    Notice that the degree of every vertex remains completely unchanged!
    However, the new graph $G_{\text{new}}$ has $v_1 \sim v_j$, so $|N(v_1) \cap T|$ has strictly increased by 1!
    This directly contradicts the maximality of our initial choice of $G$.
  Therefore, it must be that $N(v_1) = T$, which proves that $S'$ is graphic. $\blacksquare$"""
            },
            {
                "secNumber": "1.5",
                "title": "Graph Isomorphism, Structural Invariants & Graph Operations",
                "content": r"""### 1. Graph Isomorphism

Two graphs may appear drastically different when drawn in the plane, yet possess identical structural connectivity.

> **Definition 1.11 (Graph Isomorphism):**
> Let $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ be simple graphs.
> An **isomorphism** between $G_1$ and $G_2$ is a bijection $f: V_1 \to V_2$ such that:
> $$\{u, v\} \in E_1 \iff \{f(u), f(v)\} \in E_2, \quad \forall u, v \in V_1$$
> If such a bijection exists, we say $G_1$ and $G_2$ are **isomorphic**, written $G_1 \cong G_2$.

Isomorphism is an equivalence relation on the class of all graphs.

---

### 2. Graph Invariants

A **graph invariant** is any mathematical property of a graph that is preserved under isomorphism. If $G_1 \cong G_2$, then every invariant must match identically:
1. $|V(G_1)| = |V(G_2)|$ (same number of vertices).
2. $|E(G_1)| = |E(G_2)|$ (same number of edges).
3. The degree sequences of $G_1$ and $G_2$ must be identical.
4. The number of cycles of length $k$ ($C_k$) must be identical for every $k \ge 3$.
5. The chromatic number, diameter, and clique number must match.

*Note:* Having matching invariants is a **necessary** condition for isomorphism, but not sufficient. Two non-isomorphic graphs can share the identical degree sequence (e.g., $C_6$ and two disjoint triangles $2 K_3$ both have degree sequence $(2, 2, 2, 2, 2, 2)$).

---

### 3. Fundamental Graph Operations

> **Definition 1.12 (Complement of a Graph):**
> The **complement** $\overline{G}$ of a simple graph $G = (V, E)$ is the simple graph with the same vertex set $V$, where two distinct vertices are adjacent in $\overline{G}$ if and only if they are not adjacent in $G$:
> $$E(\overline{G}) = \binom{V}{2} \setminus E(G)$$
> Notice: $|E(G)| + |E(\overline{G})| = \binom{n}{2} = \frac{n(n - 1)}{2}$.
> A graph $G$ is called **self-complementary** if $G \cong \overline{G}$.

> **Definition 1.13 (Union and Join):**
> 1. **Disjoint Union ($G_1 \cup G_2$):** $V(G_1 \cup G_2) = V_1 \cup V_2$ and $E(G_1 \cup G_2) = E_1 \cup E_2$.
> 2. **Join ($G_1 * G_2$):** Obtained from $G_1 \cup G_2$ by connecting every vertex in $V_1$ to every vertex in $V_2$."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Handshaking Lemma Verification & Odd Degree Counting",
                "statement": r"1. A connected graph $G$ has 35 edges, 4 vertices of degree 5, 5 vertices of degree 4, 4 vertices of degree 3, and all remaining vertices of degree 2. Determine the total number of vertices in $G$. 2. Prove rigorously that it is impossible for a group of 15 people to have the property that each person is acquainted with exactly 7 other people in the group.",
                "hints": [
                    "For Part 1, let $k$ be the number of degree-2 vertices, and apply the Handshaking Lemma: $\\sum \\deg(v) = 2|E|$.",
                    "For Part 2, model the acquaintances as a simple graph. What would the degree of each vertex be, and what does the Handshaking Corollary dictate?"
                ],
                "solution": r"""**Part 1: Total Vertices in $G$**

Let $k$ denote the number of vertices of degree 2 in $G$.
The total number of vertices is:
$$|V| = 4 + 5 + 4 + k = 13 + k$$
We calculate the sum of degrees of all vertices:
$$\begin{aligned}
\sum_{v \in V} \deg(v) &= 4(5) + 5(4) + 4(3) + k(2) \\
&= 20 + 20 + 12 + 2k \\
&= 52 + 2k
\end{aligned}$$
By Euler's Handshaking Lemma (Theorem 1.1):
$$\sum_{v \in V} \deg(v) = 2 |E|$$
We are given $|E| = 35$, so $2 |E| = 2(35) = 70$.
Equating the expressions:
$$52 + 2k = 70 \implies 2k = 18 \implies k = 9$$
Therefore, the total number of vertices in $G$ is:
$$|V| = 13 + k = 13 + 9 = 22 \quad \blacksquare$$

---

**Part 2: Impossibility of Acquaintance Configuration**

Model the 15 people as vertices of a simple graph $G = (V, E)$, where an edge joins two people if and only if they are acquainted.
- Number of vertices: $|V| = 15$.
- Degree of each vertex: $\deg(v) = 7$ for all $v \in V$.

Notice that each of the 15 vertices has an **odd degree** ($7$ is odd).
Thus the number of vertices with odd degree is:
$$|V_{\text{odd}}| = 15$$
However, by Corollary 1.1 (The Odd Degree Theorem), in every graph the number of vertices of odd degree must be **even**.
Since $15$ is odd, such a graph cannot exist.
Alternatively, by the Handshaking Lemma:
$$2 |E| = \sum_{v \in V} \deg(v) = 15 \times 7 = 105$$
$$|E| = \frac{105}{2} = 52.5$$
The number of edges in a graph must be an integer, which is a contradiction.
Therefore, such a group configuration is impossible. $\blacksquare$"""
            },
            {
                "tier": "Advanced",
                "title": "Havel-Hakimi Algorithm Execution & Self-Complementary Graphs",
                "statement": r"1. Apply the Havel-Hakimi Theorem step-by-step to determine whether the sequence $S = (5, 5, 4, 3, 2, 2, 2, 1)$ is graphic. If graphic, construct an explicit graph realizing the sequence. 2. A simple graph $G$ is self-complementary if $G \cong \overline{G}$. Prove that if $G$ is a self-complementary graph on $n$ vertices, then $n \equiv 0 \pmod 4$ or $n \equiv 1 \pmod 4$.",
                "hints": [
                    "For Part 1, repeatedly remove the first element $d_1$ and subtract 1 from the next $d_1$ elements, re-sorting in descending order at each stage.",
                    "For Part 2, note that if $G \\cong \\overline{G}$, then $|E(G)| = |E(\\overline{G})|$. Recall the total number of edges in $K_n$ is $\\binom{n}{2}$."
                ],
                "solution": r"""**Part 1: Havel-Hakimi Test on $S = (5, 5, 4, 3, 2, 2, 2, 1)$**

Let us test the sequence recursively:
- **Step 1:** Initial sequence $S_0 = (5, 5, 4, 3, 2, 2, 2, 1)$.
  $d_1 = 5$. Delete $5$ and subtract $1$ from the next $5$ elements:
  $$(5-1, 4-1, 3-1, 2-1, 2-1, 2, 1) = (4, 3, 2, 1, 1, 2, 1)$$
  Re-sort in descending order:
  $$S_1 = (4, 3, 2, 2, 1, 1, 1)$$
- **Step 2:** $d_1 = 4$. Delete $4$ and subtract $1$ from the next $4$ elements:
  $$(3-1, 2-1, 2-1, 1-1, 1, 1) = (2, 1, 1, 0, 1, 1)$$
  Re-sort in descending order:
  $$S_2 = (2, 1, 1, 1, 1, 0)$$
- **Step 3:** $d_1 = 2$. Delete $2$ and subtract $1$ from the next $2$ elements:
  $$(1-1, 1-1, 1, 1, 0) = (0, 0, 1, 1, 0)$$
  Re-sort in descending order:
  $$S_3 = (1, 1, 0, 0, 0)$$
- **Step 4:** $d_1 = 1$. Delete $1$ and subtract $1$ from the next element:
  $$(1-1, 0, 0, 0) = (0, 0, 0, 0)$$
  The sequence $(0, 0, 0, 0)$ consists purely of zeros, which represents a valid null graph on 4 vertices ($N_4$).
By the Havel-Hakimi Theorem, since $(0, 0, 0, 0)$ is graphic, our original sequence $S$ is **graphic**! $\blacksquare$

---

**Part 2: Vertex Count of Self-Complementary Graphs**

Let $G$ be a self-complementary graph on $n$ vertices: $G \cong \overline{G}$.
Because isomorphic graphs have the identical number of edges:
$$|E(G)| = |E(\overline{G})|$$
By Definition 1.12, the sum of edges in $G$ and its complement equals the edges of the complete graph $K_n$:
$$|E(G)| + |E(\overline{G})| = \binom{n}{2} = \frac{n(n - 1)}{2}$$
Substituting $|E(\overline{G})| = |E(G)|$:
$$2 |E(G)| = \frac{n(n - 1)}{2} \implies |E(G)| = \frac{n(n - 1)}{4}$$
Since the number of edges $|E(G)|$ must be an integer:
$$\frac{n(n - 1)}{4} \in \mathbb{Z} \implies 4 \mid n(n - 1)$$
Now examine the integers $n$ and $n - 1$:
Since $\gcd(n, n - 1) = 1$, one of these two consecutive integers must be odd and the other must be even.
Therefore, the factor of 4 cannot be split between them; 4 must divide one of them entirely:
- **Case 1:** $4 \mid n \implies n \equiv 0 \pmod 4$.
- **Case 2:** $4 \mid (n - 1) \implies n \equiv 1 \pmod 4$.

Thus, any self-complementary graph must have order $n \equiv 0 \pmod 4$ or $n \equiv 1 \pmod 4$.
*(Examples: $n=4$: path graph $P_4$; $n=5$: cycle graph $C_5$).* $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Minimum Degree and Long Cycles & Complete Havel-Hakimi Proof",
                "statement": r"1. Let $G$ be a simple graph with minimum degree $\delta(G) \ge 2$. Prove that $G$ contains a cycle of length at least $\delta(G) + 1$. 2. Provide a rigorous, self-contained proof that any graph $G$ with average degree $d_{\text{avg}} = \frac{2|E|}{|V|} \ge 2$ contains at least one cycle.",
                "hints": [
                    "For Part 1, consider a longest path $P = (v_1, v_2, \\dots, v_k)$ in $G$. Where can the neighbors of $v_1$ reside?",
                    "For Part 2, either use the fact that a forest of $k$ components on $n$ vertices has $n - k$ edges, or examine vertex degrees."
                ],
                "solution": r"""**Part 1: Minimum Degree $\delta(G) \ge 2$ Implies Long Cycle**

Let $G$ be a simple graph with minimum degree $\delta \ge 2$.
Since $G$ is finite, there exists a path of maximum length in $G$.
Let $P = (v_1, v_2, \dots, v_k)$ be a **longest path** in $G$.
Length of path is $k - 1$.

Consider all neighbors of the initial vertex $v_1$:
We claim that **every neighbor of $v_1$ must lie on the path $P$**:
- Suppose for contradiction that there exists a vertex $u \in N(v_1)$ such that $u \notin \{v_2, v_3, \dots, v_k\}$.
- Then we could extend the path by prepending $u$:
  $$P' = (u, v_1, v_2, \dots, v_k)$$
- The path $P'$ would have length $k$, which strictly exceeds the length of $P$!
- This contradicts the maximality of $P$.
Therefore, all neighbors of $v_1$ must be vertices in the set $\{v_2, v_3, \dots, v_k\}$:
$$N(v_1) \subseteq \{v_2, v_3, \dots, v_k\}$$

Now, let $v_r$ be the neighbor of $v_1$ that appears **furthest along the path** (i.e., with the largest index $r$).
Since $N(v_1) \subseteq \{v_2, v_3, \dots, v_r\}$, the number of neighbors of $v_1$ cannot exceed the number of available vertices in $\{v_2, \dots, v_r\}$:
$$\deg(v_1) \le r - 1$$
Since the minimum degree of $G$ is $\delta$, we have:
$$\delta \le \deg(v_1) \le r - 1 \implies r \ge \delta + 1$$
Now, consider the cycle formed by traveling from $v_1$ along the path to $v_r$, and then taking the edge $\{v_r, v_1\}$ back to $v_1$:
$$C = (v_1, v_2, \dots, v_r, v_1)$$
The vertices of $C$ are $\{v_1, v_2, \dots, v_r\}$, which are all distinct.
The length of cycle $C$ is:
$$\text{length}(C) = r$$
Since $r \ge \delta + 1$, the cycle $C$ has length:
$$\text{length}(C) \ge \delta + 1 \quad \blacksquare$$

---

**Part 2: Proof that $d_{\text{avg}} \ge 2$ Implies Existence of a Cycle**

Let $G = (V, E)$ be a simple graph with $n = |V|$ vertices and $m = |E|$ edges, such that:
$$d_{\text{avg}} = \frac{2m}{n} \ge 2 \implies m \ge n$$

Assume for contradiction that $G$ contains **no cycles**.
A graph with no cycles is an **acyclic graph** (a forest).
Let $G$ have $k \ge 1$ connected components: $G_1, G_2, \dots, G_k$.
Each component $G_i$ is connected and contains no cycles, which means each component is a **tree**!

Let $n_i = |V(G_i)|$ and $m_i = |E(G_i)|$ for each component $i = 1, \dots, k$.
By the fundamental theorem of trees (to be proved in Unit 3), every tree on $n_i$ vertices has exactly $n_i - 1$ edges:
$$m_i = n_i - 1, \quad \forall i = 1, \dots, k$$
Summing the edges across all $k$ components:
$$m = \sum_{i=1}^k m_i = \sum_{i=1}^k (n_i - 1) = \left( \sum_{i=1}^k n_i \right) - k = n - k$$
Since every graph has at least one component ($k \ge 1$):
$$m = n - k \le n - 1 < n$$
However, our initial hypothesis gave:
$$m \ge n$$
This produces a direct contradiction ($n \le m \le n - 1$).
Therefore, the assumption that $G$ has no cycles must be false.
Hence, $G$ must contain at least one cycle. $\blacksquare$"""
            }
        ]
    }
    return u1

if __name__ == "__main__":
    u = get_unit1()
    print("Unit 1 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
