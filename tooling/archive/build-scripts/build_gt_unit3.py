# -*- coding: utf-8 -*-
"""
build_gt_unit3.py
Constructs Unit 3: Trees, Spanning Trees, Center Theorems & Tree Metric Algorithms
"""

def get_unit3():
    u3 = {
        "number": 3,
        "title": "Trees, Spanning Trees, Center Theorems & Tree Metric Algorithms",
        "leadSummary": "Comprehensive theory of tree structures: definition and equivalent axiomatic characterizations of trees, metric properties (distance, eccentricity, diameter, radius), Jordan's center theorem, rooted and binary trees, Cayley's tree enumeration formula n^(n-2), Prüfer sequences, and minimum spanning trees via Kruskal's and Prim's algorithms.",
        "simulations": ["sim_gt_spanning_tree"],
        "sections": [
            {
                "secNumber": "3.1",
                "title": "Axiomatic Characterizations of Trees & The Six Equivalent Conditions",
                "content": r"""### 1. Definition of a Tree and a Forest

> **Definition 3.1 (Tree and Forest):**
> 1. A **tree** $T$ is a connected, acyclic simple graph.
> 2. A **forest** is an acyclic simple graph (each of whose connected components is a tree).
> 3. A vertex of degree 1 in a tree is called a **leaf** (or pendant vertex).

---

### 2. The Fundamental Characterization Theorem

> **Theorem 3.1 (Six Equivalent Characterizations of Trees):**
> Let $T = (V, E)$ be a simple graph on $n = |V|$ vertices. The following statements are mutually equivalent:
> 1. $T$ is a tree (connected and acyclic).
> 2. For any two distinct vertices $u, v \in V$, there is a **unique simple path** connecting $u$ and $v$.
> 3. $T$ is connected and has exactly $n - 1$ edges: $|E| = n - 1$.
> 4. $T$ is acyclic and has exactly $n - 1$ edges: $|E| = n - 1$.
> 5. $T$ is minimally connected (connected, but deleting any edge disconnects the graph: $\forall e \in E, \; \omega(T - e) = 2$).
> 6. $T$ is maximally acyclic (acyclic, but adding an edge between any two non-adjacent vertices creates a unique cycle).

#### Complete Formal Proof of Equivalence ($1 \implies 2 \implies 5 \implies 3 \implies 4 \implies 6 \implies 1$):
- **$1 \implies 2$:** Since $T$ is connected, there exists at least one $u$-$v$ path for all $u \ne v$.
  Suppose there exist two distinct paths $P_1 \ne P_2$ from $u$ to $v$.
  Let $x$ be the first vertex where $P_1$ and $P_2$ diverge, and let $y$ be the first vertex after $x$ where they recombine.
  The segment of $P_1$ from $x$ to $y$ together with the segment of $P_2$ from $y$ to $x$ forms a simple cycle in $T$.
  This contradicts $T$ being acyclic! Thus the path is unique.
- **$2 \implies 5$:** By (2), $T$ is connected. Let $e = \{u, v\} \in E$.
  The edge $e$ is the unique path between $u$ and $v$.
  Deleting $e$ leaves no $u$-$v$ path in $T - e$.
  Thus $u$ and $v$ lie in different components, so $\omega(T - e) = 2$.
  Hence $T$ is minimally connected.
- **$5 \implies 3$ (by induction on $n$):**
  - Base case $n = 1$: $m = 0 = n - 1$. True.
  - Assume true for all minimally connected graphs with $< n$ vertices.
  - In a minimally connected graph on $n \ge 2$ vertices, deleting any edge $e = \{u, v\}$ splits $T$ into exactly two connected components $T_1$ and $T_2$.
  - Each $T_i$ is itself minimally connected (if deleting an edge in $T_1$ didn't disconnect $T_1$, it wouldn't disconnect $T$).
  - Let $n_1 = |V(T_1)|$ and $n_2 = |V(T_2)|$ with $n_1 + n_2 = n$.
  - By induction hypothesis: $|E(T_1)| = n_1 - 1$ and $|E(T_2)| = n_2 - 1$.
  - Total edges in $T$:
    $$|E(T)| = |E(T_1)| + |E(T_2)| + 1 = (n_1 - 1) + (n_2 - 1) + 1 = n_1 + n_2 - 1 = n - 1$$
- **$3 \implies 4$:** Suppose $T$ is connected and $|E| = n - 1$.
  If $T$ contained a cycle, removing an edge from the cycle would leave the graph connected.
  We could repeatedly remove edges until an acyclic connected graph (a tree) remains with $k$ edges.
  By our proof of $1 \implies 3$, this tree must have $n - 1$ edges.
  Thus $n - 1 = k < |E| = n - 1$, a contradiction!
  Hence $T$ is acyclic.
- **$4 \implies 6$:** Suppose $T$ is acyclic and $|E| = n - 1$.
  Let $k$ be the number of components of $T$. Each component is a tree, so:
  $$|E| = \sum (n_i - 1) = n - k$$
  Since $|E| = n - 1$, we have $n - 1 = n - k \implies k = 1$.
  Thus $T$ is connected.
  For any two non-adjacent vertices $u, v$, there already exists a unique path $P$ between them.
  Adding the edge $\{u, v\}$ closes this path, producing a cycle $P \cup \{\{u, v\}\}$.
  Since $P$ was unique, this cycle is unique. Thus $T$ is maximally acyclic.
- **$6 \implies 1$:** By (6), $T$ is acyclic. If $T$ were disconnected, adding an edge between vertices in different components would not create a cycle.
  Thus $T$ must be connected. Hence $T$ is a tree. $\blacksquare$"""
            },
            {
                "secNumber": "3.2",
                "title": "Tree Metrics: Distances, Eccentricity & Jordan's Center Theorem",
                "content": r"""### 1. Distance Metrics in Graphs

Let $G = (V, E)$ be a connected graph.

> **Definition 3.2 (Distance, Eccentricity, Diameter, Radius):**
> 1. The **distance** $d(u, v)$ between vertices $u, v \in V$ is the length of a shortest $u$-$v$ path in $G$.
>    Distance satisfies the metric axioms: $d(u, v) \ge 0$, $d(u, v) = 0 \iff u = v$, $d(u, v) = d(v, u)$, and the triangle inequality $d(u, w) \le d(u, v) + d(v, w)$.
> 2. The **eccentricity** $\epsilon(v)$ of a vertex $v \in V$ is the maximum distance from $v$ to any other vertex:
>    $$\epsilon(v) = \max_{u \in V} d(v, u)$$
> 3. The **diameter** $\text{diam}(G)$ is the maximum eccentricity:
>    $$\text{diam}(G) = \max_{v \in V} \epsilon(v) = \max_{u, v \in V} d(u, v)$$
> 4. The **radius** $\text{rad}(G)$ is the minimum eccentricity:
>    $$\text{rad}(G) = \min_{v \in V} \epsilon(v)$$
> 5. A vertex $c \in V$ is called a **central vertex** (or center) if $\epsilon(c) = \text{rad}(G)$.
>    The **center** of $G$, denoted $Z(G)$, is the set of all central vertices.

In general graphs, the center can consist of any number of vertices. In trees, however, Camille Jordan proved an extraordinary structural restriction in 1869:

---

### 2. Jordan's Center Theorem

> **Theorem 3.2 (Jordan's Center Theorem, 1869):**
> Every tree $T$ has a center consisting of **either a single vertex** (a central tree) **or two adjacent vertices** (a bicentral tree):
> $$|Z(T)| \in \{1, 2\}$$

#### Complete Formal Proof (by Leaf Pruning):
Let $T$ be a tree on $n$ vertices.
- If $n = 1$, $T = K_1$, and the single vertex is the center.
- If $n = 2$, $T = K_2$, and both vertices have eccentricity 1; the center consists of both adjacent vertices.
- Assume $n \ge 3$.
  Let $L$ be the set of all leaves (vertices of degree 1) in $T$.
  Since $n \ge 3$, $|L| \ge 2$, and $T' = T - L$ is a non-empty sub-tree.
  
  **Key Claim:** For every non-leaf vertex $v \in V(T) \setminus L$, its eccentricity in $T'$ is strictly 1 less than in $T$:
  $$\epsilon_{T'}(v) = \epsilon_T(v) - 1$$
  *Proof of Claim:* In $T$, the vertex $u$ achieving the maximum distance $d(v, u) = \epsilon_T(v)$ must be a leaf! (If $u$ were not a leaf, we could extend the path along an incident edge away from $v$, strictly increasing the distance).
  The path from $v$ to $u$ in $T$ passes through the unique neighbor $w$ of $u$.
  In $T'$, the leaf $u$ has been removed, so the furthest reachable vertex along this branch is $w$.
  Thus $d_{T'}(v, w) = d_T(v, u) - 1$.
  This holds for all non-leaf vertices. $\blacksquare$

Since the eccentricity of **every** vertex in $V(T')$ decreases by exactly 1:
$$\min_{v \in V(T')} \epsilon_{T'}(v) = \left( \min_{v \in V(T')} \epsilon_T(v) \right) - 1$$
Therefore, the vertices achieving the minimum eccentricity in $T'$ are **precisely the same vertices** that achieved the minimum eccentricity in $T$:
$$Z(T) = Z(T - L)$$
We repeatedly prune all leaves from the tree.
At each iteration, the number of vertices strictly decreases, while the center set $Z(T)$ is preserved invariant!
Eventually, the process terminates at either:
1. A single vertex $K_1 \implies |Z(T)| = 1$.
2. An edge $K_2 \implies |Z(T)| = 2$ (two adjacent vertices).
Thus, every tree has either 1 center or 2 adjacent bicenters. $\blacksquare$"""
            },
            {
                "secNumber": "3.3",
                "title": "Rooted Trees, Binary Trees & Tree Traversals",
                "content": r"""### 1. Rooted Trees and Hierarchical Terminology

> **Definition 3.3 (Rooted Tree):**
> A **rooted tree** $(T, r)$ is a tree $T$ in which one distinguished vertex $r \in V(T)$ is designated as the **root**.
> The choice of root imposes a natural parent-child directed orientation away from $r$.

For any vertex $v \in V(T)$:
- **Level (Depth):** The distance from the root: $\text{level}(v) = d(r, v)$. $\text{level}(r) = 0$.
- **Height:** The maximum level among all vertices in $T$.
- **Parent:** The unique neighbor of $v$ on the path from $v$ to $r$.
- **Children:** Any neighbor of $v$ having level $\text{level}(v) + 1$.
- **Ancestors / Descendants:** Formed by the transitive closure of parent / child relations.

---

### 2. $m$-ary Trees and Binary Trees

> **Definition 3.4 ($m$-ary Tree):**
> A rooted tree is called an **$m$-ary tree** if every internal vertex has at most $m$ children.
> If $m = 2$, it is called a **binary tree**.
> - **Full (Strict) $m$-ary Tree:** Every internal vertex has **exactly $m$ children**.

> **Theorem 3.3 (Properties of Full $m$-ary Trees):**
> Let $T$ be a full $m$-ary tree with $n$ vertices, $i$ internal vertices, and $\ell$ leaves.
> 1. $n = m \cdot i + 1$.
> 2. $\ell = (m - 1)i + 1$.
> 3. $i = \frac{n - 1}{m} = \frac{\ell - 1}{m - 1}$.

#### Proof:
Each of the $i$ internal vertices has exactly $m$ children.
Every vertex in $T$ except the root is the child of exactly one internal vertex.
Thus:
$$n - 1 = m \cdot i \implies n = m \cdot i + 1$$
Since every vertex is either an internal vertex or a leaf ($n = i + \ell$):
$$i + \ell = m \cdot i + 1 \implies \ell = (m - 1)i + 1 \quad \blacksquare$$"""
            },
            {
                "secNumber": "3.4",
                "title": "Cayley's Tree Formula $n^{n-2}$ & Prüfer Encoding",
                "content": r"""### 1. Cayley's Theorem on Labeled Trees

How many distinct labeled trees can be formed on $n$ designated vertices $V = \{1, 2, \dots, n\}$?

> **Theorem 3.4 (Cayley's Formula, 1889):**
> The number of labeled trees on $n$ vertices ($n \ge 2$) is:
> $$T_n = n^{n - 2}$$

Examples:
- $n = 2: 2^{2-2} = 2^0 = 1$ tree (a single edge).
- $n = 3: 3^{3-2} = 3^1 = 3$ trees (each choosing a different central vertex).
- $n = 4: 4^{4-2} = 4^2 = 16$ trees (4 star graphs $K_{1,3} + 12$ path graphs $P_4$).

---

### 2. The Prüfer Encoding Bijection

In 1918, Heinz Prüfer discovered an elegant bijective proof establishing Cayley's formula by encoding every labeled tree on $n$ vertices into a unique sequence of length $n - 2$ over the alphabet $\{1, 2, \dots, n\}$.

#### Algorithm 1: Tree $\to$ Prüfer Sequence $P(T)$
Input: A labeled tree $T$ on vertices $\{1, 2, \dots, n\}$ with $n \ge 3$.
Initialize: Empty sequence $P = ()$.
1. While $T$ has more than 2 vertices:
   - Identify the leaf with the **smallest numerical label**; call it $v$.
   - Let $u$ be the unique neighbor of $v$.
   - Append $u$ to the sequence: $P \leftarrow (P, u)$.
   - Remove vertex $v$ and edge $\{v, u\}$ from $T$.
2. Return $P$, which has length exactly $n - 2$.

#### Algorithm 2: Prüfer Sequence $\to$ Labeled Tree
Input: A sequence $P = (p_1, p_2, \dots, p_{n-2})$ with entries from $S = \{1, 2, \dots, n\}$.
1. Compute the degree of each label in the target tree:
   $$\deg(v) = 1 + (\text{number of times } v \text{ appears in } P)$$
2. For $i = 1$ to $n - 2$:
   - Let $x$ be the smallest element in $S$ having $\deg(x) = 1$.
   - Add edge $\{x, p_i\}$ to the tree.
   - Decrement $\deg(x)$ and $\deg(p_i)$ by 1.
   - Remove $x$ from $S$.
3. At the end, exactly two elements remain in $S$ with degree 1. Add an edge between them.

Since every labeled tree produces a unique Prüfer sequence, and every sequence of length $n - 2$ with entries from $\{1, \dots, n\}$ uniquely reconstructs a tree:
$$T_n = n^{n - 2} \quad \blacksquare$$"""
            },
            {
                "secNumber": "3.5",
                "title": "Minimum Spanning Trees: Kruskal's & Prim's Algorithms",
                "content": r"""### 1. Spanning Trees in Connected Graphs

> **Definition 3.5 (Spanning Tree):**
> A **spanning tree** $T$ of a connected graph $G = (V, E)$ is a subgraph that is a tree and contains **every vertex** of $G$: $V(T) = V(G)$.

Every connected graph contains at least one spanning tree.

---

### 2. The Minimum Spanning Tree (MST) Problem

Given a connected undirected graph $G = (V, E)$ with edge weights $w: E \to \mathbb{R}$, find a spanning tree $T$ that minimizes the total weight:
$$w(T) = \sum_{e \in E(T)} w(e)$$

#### The Cut Property:
For any cut $(S, V \setminus S)$ in $G$, if an edge $e$ is a strictly minimum-weight edge crossing the cut, then $e$ **must belong to every minimum spanning tree** of $G$.

---

### 3. Kruskal's Algorithm (Greedy by Edges)

1. Sort all edges in non-decreasing order of weight: $w(e_1) \le w(e_2) \le \dots \le w(e_m)$.
2. Initialize $T = (V, \emptyset)$.
3. For each edge $e_i$ in the sorted list:
   - If adding $e_i$ to $T$ does **not create a cycle** (tested via Disjoint-Set / Union-Find in $\mathcal{O}(\alpha(V))$ time), add $e_i$ to $T$: $T \leftarrow T \cup \{e_i\}$.
4. Terminate when $|E(T)| = n - 1$.
Total Time Complexity: $\mathcal{O}(|E| \log |E|)$.

---

### 4. Prim's Algorithm (Greedy by Vertices)

1. Initialize $S = \{s\}$ starting at an arbitrary root vertex $s$, and $T = \emptyset$.
2. While $S \ne V$:
   - Find the minimum-weight edge $e = \{u, v\}$ such that $u \in S$ and $v \in V \setminus S$.
   - Add $e$ to $T$ and add $v$ to $S$.
3. Terminate when $S = V$.
Total Time Complexity: $\mathcal{O}(|E| + |V| \log |V|)$ using Fibonacci Heaps."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Tree Centers, Radius, Diameter & Kruskal MST Execution",
                "statement": r"1. Consider a tree $T$ with 9 vertices labeled $1, \dots, 9$ and edge set $E = \{\{1, 2\}, \{2, 3\}, \{3, 4\}, \{4, 5\}, \{3, 6\}, \{6, 7\}, \{7, 8\}, \{7, 9\}\}$. Determine the eccentricity of every vertex, the radius $\text{rad}(T)$, the diameter $\text{diam}(T)$, and all center vertices $Z(T)$. 2. Execute Kruskal's algorithm on a 5-vertex network with edges: $\{A, B\}: 1$, $\{B, C\}: 4$, $\{A, C\}: 3$, $\{C, D\}: 2$, $\{D, E\}: 5$, $\{C, E\}: 6$, $\{B, D\}: 7$. List the edges added in order and state the total MST weight.",
                "hints": [
                    "For Part 1, compute the longest path from each vertex. Identify the longest path in the tree to determine the diameter.",
                    "For Part 2, sort edges by weight and greedily accept edges that do not form a cycle."
                ],
                "solution": r"""**Part 1: Tree Metric Calculation**

Examine the paths in $T$:
- Path from 1 to 5: $1 - 2 - 3 - 4 - 5$ (length 4).
- Path from 1 to 8: $1 - 2 - 3 - 6 - 7 - 8$ (length 5).
- Path from 1 to 9: $1 - 2 - 3 - 6 - 7 - 9$ (length 5).
- Path from 5 to 8: $5 - 4 - 3 - 6 - 7 - 8$ (length 5).

The furthest pair of vertices are between $\{1, 5\}$ and $\{8, 9\}$ with distance 5.
Let us compute the eccentricity $\epsilon(v) = \max_u d(v, u)$:
- $\epsilon(1) = d(1, 8) = 5$
- $\epsilon(2) = d(2, 8) = 4$
- $\epsilon(3) = \max(d(3, 1), d(3, 5), d(3, 8)) = \max(2, 2, 3) = 3$
- $\epsilon(4) = d(4, 8) = 4$
- $\epsilon(5) = d(5, 8) = 5$
- $\epsilon(6) = \max(d(6, 1), d(6, 5), d(6, 8)) = \max(3, 3, 2) = 3$
- $\epsilon(7) = \max(d(7, 1), d(7, 5), d(7, 8)) = \max(4, 4, 1) = 4$
- $\epsilon(8) = d(8, 1) = 5$
- $\epsilon(9) = d(9, 1) = 5$

**Summary of Metrics:**
- **Diameter:** $\text{diam}(T) = \max \epsilon(v) = 5$.
- **Radius:** $\text{rad}(T) = \min \epsilon(v) = 3$.
- **Center Vertices:** $Z(T) = \{ v : \epsilon(v) = 3 \} = \{3, 6\}$.
Notice that vertices $3$ and $6$ are adjacent ($\{3, 6\} \in E$).
Thus $T$ is **bicentral**, with $|Z(T)| = 2$, perfectly confirming Jordan's Center Theorem!

---

**Part 2: Kruskal's MST Execution**

Sorted edge list by weight:
1. $\{A, B\}$, weight $1$
2. $\{C, D\}$, weight $2$
3. $\{A, C\}$, weight $3$
4. $\{B, C\}$, weight $4$
5. $\{D, E\}$, weight $5$
6. $\{C, E\}$, weight $6$
7. $\{B, D\}$, weight $7$

**Execution Steps:**
- **Step 1:** Consider $\{A, B\}$ (wt 1). Components: $\{A, B\}, \{C\}, \{D\}, \{E\}$. **Add $\{A, B\}$**.
- **Step 2:** Consider $\{C, D\}$ (wt 2). Components: $\{A, B\}, \{C, D\}, \{E\}$. **Add $\{C, D\}$**.
- **Step 3:** Consider $\{A, C\}$ (wt 3). Connects $\{A, B\}$ and $\{C, D\}$. Components: $\{A, B, C, D\}, \{E\}$. **Add $\{A, C\}$**.
- **Step 4:** Consider $\{B, C\}$ (wt 4). Both $B$ and $C$ already belong to the same component $\{A, B, C, D\}$. Adding $\{B, C\}$ creates cycle $(A-B-C-A)$. **Reject $\{B, C\}$**.
- **Step 5:** Consider $\{D, E\}$ (wt 5). Connects $\{A, B, C, D\}$ and $\{E\}$. **Add $\{D, E\}$**.

We have added $4 = 5 - 1$ edges. The spanning tree is complete!
- Edges selected: $\{A, B\}, \{C, D\}, \{A, C\}, \{D, E\}$.
- Total MST weight: $1 + 2 + 3 + 5 = 11$. $\blacksquare$"""
            },
            {
                "tier": "Advanced",
                "title": "Prüfer Sequence Encoding & Decoding & Tree Leaf Bound",
                "statement": r"1. Given the Prüfer sequence $P = (3, 3, 4, 1, 4)$, reconstruct the unique labeled tree on 7 vertices. 2. Encode the tree with edges $\{\{1, 4\}, \{2, 4\}, \{3, 4\}, \{4, 5\}, \{5, 6\}\}$ into its Prüfer sequence. 3. Prove that in every tree on $n \ge 2$ vertices, there are at least two leaves (vertices of degree 1).",
                "hints": [
                    "For Part 1, length of $P$ is 5, so $n = 5 + 2 = 7$. Count occurrences in $P$ to determine initial degrees $\\deg(v) = 1 + \\text{count}$.",
                    "For Part 2, repeatedly remove the smallest leaf and record its neighbor.",
                    "For Part 3, use the Handshaking Lemma $\\sum \\deg(v) = 2(n - 1)$ or consider a longest path."
                ],
                "solution": r"""**Part 1: Decoding Prüfer Sequence $P = (3, 3, 4, 1, 4)$**

The sequence length is $5 \implies n = 5 + 2 = 7$.
Vertices are $S = \{1, 2, 3, 4, 5, 6, 7\}$.
Compute initial degrees: $\deg(v) = 1 + \text{count in } P$:
- $1$ appears 1 time $\implies \deg(1) = 1 + 1 = 2$
- $2$ appears 0 times $\implies \deg(2) = 1 + 0 = 1$
- $3$ appears 2 times $\implies \deg(3) = 1 + 2 = 3$
- $4$ appears 2 times $\implies \deg(4) = 1 + 2 = 3$
- $5$ appears 0 times $\implies \deg(5) = 1 + 0 = 1$
- $6$ appears 0 times $\implies \deg(6) = 1 + 0 = 1$
- $7$ appears 0 times $\implies \deg(7) = 1 + 0 = 1$

**Reconstruction Steps:**
- **Step 1 ($p_1 = 3$):** Smallest degree 1 vertex is $2$.
  **Add edge $\{2, 3\}$**.
  Decrement $\deg(2) \to 0$, $\deg(3) \to 2$.
- **Step 2 ($p_2 = 3$):** Smallest degree 1 vertex is $5$.
  **Add edge $\{5, 3\}$**.
  Decrement $\deg(5) \to 0$, $\deg(3) \to 1$.
- **Step 3 ($p_3 = 4$):** Smallest degree 1 vertex is $3$.
  **Add edge $\{3, 4\}$**.
  Decrement $\deg(3) \to 0$, $\deg(4) \to 2$.
- **Step 4 ($p_4 = 1$):** Smallest degree 1 vertex is $6$.
  **Add edge $\{6, 1\}$**.
  Decrement $\deg(6) \to 0$, $\deg(1) \to 1$.
- **Step 5 ($p_5 = 4$):** Smallest degree 1 vertex is $1$.
  **Add edge $\{1, 4\}$**.
  Decrement $\deg(1) \to 0$, $\deg(4) \to 1$.
- **Final Step:** Remaining vertices with degree 1 are $4$ and $7$.
  **Add edge $\{4, 7\}$**.

Reconstructed Edge Set:
$$E = \{ \{2, 3\}, \; \{5, 3\}, \; \{3, 4\}, \; \{6, 1\}, \; \{1, 4\}, \; \{4, 7\} \}$$

---

**Part 2: Encoding Tree to Prüfer Sequence**

Tree on 6 vertices: $E = \{\{1, 4\}, \{2, 4\}, \{3, 4\}, \{4, 5\}, \{5, 6\}\}$.
Leaves: $1, 2, 3, 6$.
- Smallest leaf is $1$. Neighbor is $4$. Record **4**. Remove $1$.
- Remaining leaves: $2, 3, 6$. Smallest is $2$. Neighbor is $4$. Record **4**. Remove $2$.
- Remaining leaves: $3, 6$. Smallest is $3$. Neighbor is $4$. Record **4**. Remove $3$.
- Remaining vertices: $\{4, 5, 6\}$ with edges $\{4, 5\}, \{5, 6\}$.
  Leaves: $4, 6$. Smallest is $4$. Neighbor is $5$. Record **5**. Remove $4$.
- 2 vertices remain ($\{5, 6\}$). Terminate.

Resulting Prüfer sequence:
$$P = (4, 4, 4, 5) \quad \blacksquare$$

---

**Part 3: Proof that every Tree ($n \ge 2$) has at least 2 Leaves**

**Method 1 (Handshaking Lemma):**
Let $T$ be a tree on $n \ge 2$ vertices.
By Theorem 3.1, $|E| = n - 1$.
By the Handshaking Lemma:
$$\sum_{v \in V} \deg(v) = 2 |E| = 2(n - 1) = 2n - 2$$
Since $T$ is connected and $n \ge 2$, no vertex can have degree $0$.
Thus $\deg(v) \ge 1$ for all $v \in V$.
Let $k$ be the number of leaves (vertices with $\deg(v) = 1$).
The remaining $n - k$ vertices must each have degree $\ge 2$:
$$\sum_{v \in V} \deg(v) = \sum_{\text{leaves}} 1 + \sum_{\text{non-leaves}} \deg(v) \ge k(1) + (n - k)(2) = 2n - k$$
Substituting the degree sum:
$$2n - 2 \ge 2n - k \implies -2 \ge -k \implies k \ge 2$$
Therefore, $T$ contains at least 2 leaves. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Complete Formal Proof of Cayley's Tree Formula via Prüfer Bijection",
                "statement": r"Provide a complete, mathematically rigorous proof of Cayley's Theorem: The number of labeled trees on $n$ vertices ($n \ge 2$) is exactly $n^{n-2}$, by proving that the Prüfer encoding algorithm is a strict bijection between the set of labeled trees on $n$ vertices and the set of sequences of length $n - 2$ with entries from $\{1, 2, \dots, n\}$.",
                "hints": [
                    "Define the set $\\mathcal{T}_n$ of labeled trees and $\\mathcal{P}_n = \\{1, \\dots, n\\}^{n-2}$.",
                    "Prove that the encoding map $\\Phi: \\mathcal{T}_n \\to \\mathcal{P}_n$ is injective by showing that the leaves removed at each step are uniquely reconstructible.",
                    "Prove that the decoding map $\\Psi: \\mathcal{P}_n \\to \\mathcal{T}_n$ produces a valid tree and satisfies $\\Phi \\circ \\Psi = \\text{id}$."
                ],
                "solution": r"""**Complete Proof of Cayley's Formula via the Prüfer Bijection**

Let $\mathcal{T}_n$ denote the set of all labeled trees with vertex set $V = \{1, 2, \dots, n\}$ ($n \ge 2$).
Let $\mathcal{P}_n = \{ (a_1, a_2, \dots, a_{n-2}) : a_i \in \{1, 2, \dots, n\} \}$.
The cardinality of $\mathcal{P}_n$ is:
$$|\mathcal{P}_n| = n^{n-2}$$
To prove $|\mathcal{T}_n| = n^{n-2}$, it suffices to establish a **bijection** $\Phi: \mathcal{T}_n \to \mathcal{P}_n$.

---

**Step 1: The Degree Identity of the Prüfer Encoding**
Let $T \in \mathcal{T}_n$, and let $P = \Phi(T) = (p_1, p_2, \dots, p_{n-2})$ be the Prüfer sequence obtained by Algorithm 1.
Notice:
- A vertex $v$ is placed into the sequence $P$ every time one of its incident edges is removed due to the deletion of an adjacent leaf.
- When $v$ itself becomes a leaf, it is deleted, but its label is **not** written to $P$ (its neighbor's label is written instead).
- The process terminates when 2 vertices remain. Neither of these 2 final vertices is deleted.
Therefore, a vertex $v$ appears in $P$ exactly $\deg_T(v) - 1$ times:
$$\text{count}_P(v) = \deg_T(v) - 1 \iff \deg_T(v) = 1 + \text{count}_P(v)$$
In particular, the leaves of $T$ are **precisely the vertices that do NOT appear in $P$**!

---

**Step 2: Injectivity of the Encoding $\Phi$**
Suppose $T_1, T_2 \in \mathcal{T}_n$ such that $\Phi(T_1) = \Phi(T_2) = (p_1, p_2, \dots, p_{n-2})$.
We show $T_1 = T_2$ by induction on $n$:
- **Base case ($n = 2$):** Both $T_1$ and $K_2$ have 0-length sequences, and there is only 1 labeled tree on 2 vertices.
- **Inductive Step:** Assume that for any two trees on $n - 1$ vertices, identical Prüfer sequences imply identical trees.
  For $T_1$ and $T_2$, by the Degree Identity, the set of leaves in both trees is identical:
  $$L = \{1, \dots, n\} \setminus \{p_1, \dots, p_{n-2}\}$$
  The leaf removed in the very first step of encoding is the smallest element in $L$; call it $\ell = \min(L)$.
  The neighbor of $\ell$ in $T_1$ must be $p_1$, so $\{\ell, p_1\} \in E(T_1)$.
  Similarly, the neighbor of $\ell$ in $T_2$ must be $p_1$, so $\{\ell, p_1\} \in E(T_2)$.
  Now consider the reduced trees $T_1' = T_1 - \ell$ and $T_2' = T_2 - \ell$ on $n - 1$ vertices.
  Both $T_1'$ and $T_2'$ have the remaining Prüfer sequence $(p_2, \dots, p_{n-2})$.
  By the induction hypothesis, $T_1' = T_2'$.
  Adding back the common edge $\{\ell, p_1\}$ yields $T_1 = T_2$.
Therefore, $\Phi$ is strictly **injective**.

---

**Step 3: Surjectivity of the Encoding $\Phi$**
Let $P = (p_1, p_2, \dots, p_{n-2}) \in \mathcal{P}_n$ be any arbitrary sequence.
Apply Algorithm 2 to construct a graph $T$:
1. At each step $i$, we connect the smallest vertex $x$ of current degree 1 to $p_i$, and decrement their degrees.
2. The graph constructed at each step has no cycles because $x$ has degree 1 and is eliminated from future connections.
3. After $n - 2$ steps, exactly two vertices remain of degree 1, which are connected by an edge.
The resulting graph $T$ has $n$ vertices and $(n - 2) + 1 = n - 1$ edges and is connected and acyclic.
By Theorem 3.1, $T$ is a valid tree in $\mathcal{T}_n$.
Running the encoding algorithm $\Phi$ on $T$ will at step 1 identify $\min(L) = x$ and record its neighbor $p_1$, matching the sequence step-by-step.
Thus $\Phi(T) = P$.
Therefore, $\Phi$ is **surjective**.

---

**Conclusion:**
$\Phi: \mathcal{T}_n \to \mathcal{P}_n$ is a bijection.
Therefore:
$$|\mathcal{T}_n| = |\mathcal{P}_n| = n^{n-2} \quad \blacksquare$$"""
            }
        ]
    }
    return u3

if __name__ == "__main__":
    u = get_unit3()
    print("Unit 3 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
