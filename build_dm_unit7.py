# -*- coding: utf-8 -*-
"""
build_dm_unit7.py
Constructs Unit 7: Trees, Spanning Trees & Shortest Path Algorithms
Strictly ZERO course numbers.
"""

def get_unit7():
    u7 = {
        "number": 7,
        "title": "Trees, Spanning Trees & Shortest Path Algorithms",
        "leadSummary": "Acyclic graph structures and network path optimization: axiomatic characterizations of trees, Cayley's theorem for labeled trees, rooted trees and Huffman optimal prefix codes, the Cut and Cycle properties of Minimum Spanning Trees (MST), Kruskal's greedy algorithm with Disjoint Set Union (DSU) vs Prim's priority queue algorithm, Dijkstra's single-source shortest path algorithm, and the Floyd-Warshall dynamic programming all-pairs shortest path matrix reduction.",
        "simulations": ["sim_dm_mst_kruskal_prim"],
        "sections": [
            {
                "secNumber": "7.1",
                "title": "Tree Characterizations, Centers, Radii & Cayley's Formula",
                "content": r"""### 1. Equivalent Characterizations of Trees

> **Definition 7.1 (Tree):**
> A **tree** $T$ is an undirected graph that is connected and contains no simple cycles (acyclic). A **forest** is a disjoint union of trees.

> **Theorem 7.1 (The Six Equivalent Tree Theorems):**
> Let $G = (V, E)$ be an undirected graph of order $|V| = n \ge 1$. The following statements are mathematically equivalent:
> 1. $G$ is a tree (connected and acyclic).
> 2. Between any two distinct vertices in $G$, there exists a **unique simple path**.
> 3. $G$ is connected, and removing any edge disconnects $G$ (every edge is a bridge).
> 4. $G$ is minimally connected (adding any edge creates a unique cycle).
> 5. $G$ is connected and has exactly $|E| = n - 1$ edges.
> 6. $G$ is acyclic and has exactly $|E| = n - 1$ edges.

---

### 2. Eccentricity, Center, and Jordan's Theorem

For any vertex $v \in V(T)$, its **eccentricity** is the maximum distance to any other vertex:
$$\epsilon(v) = \max_{u \in V} d(v, u)$$
- The **radius** is $R(T) = \min_{v \in V} \epsilon(v)$.
- The **diameter** is $D(T) = \max_{v \in V} \epsilon(v)$.
- The **center** of $T$ is the set of vertices achieving the minimum eccentricity:
  $$\text{Center}(T) = \{v \in V \mid \epsilon(v) = R(T)\}$$

> **Theorem 7.2 (Jordan's Theorem, 1869):**
> Every tree $T$ has a center consisting of either a **single vertex** or **two adjacent vertices**.
> *Proof:* Pruning all leaves of $T$ simultaneously reduces the eccentricity of every non-leaf vertex by exactly 1. Repeating leaf pruning preserves the center until either a single vertex $K_1$ or two adjacent vertices $K_2$ remain. $\blacksquare$

---

### 3. Cayley's Labeled Tree Enumeration Formula

> **Theorem 7.3 (Cayley's Formula):**
> The number of labeled trees on $n$ vertices $\{1, 2, \dots, n\}$ is:
> $$T_n = n^{n - 2}$$

*Proof via Prüfer Sequences (Bijective Proof):*
- Heinz Prüfer (1918) established a bijection between labeled trees on $n$ vertices and sequences of length $n - 2$ with entries from $\{1, 2, \dots, n\}$.
- At each step, find the leaf with the smallest label, record the label of its unique neighbor, and remove the leaf. Repeat $n - 2$ times.
- Since there are $n$ choices for each of the $n - 2$ positions in the sequence, there are exactly $n^{n-2}$ distinct sequences, proving Cayley's formula. $\blacksquare$"""
            },
            {
                "secNumber": "7.2",
                "title": "Rooted Trees, Traversals & Huffman Optimal Prefix Coding",
                "content": r"""### 1. Rooted Trees and Hierarchies

A **rooted tree** is a tree in which a designated vertex $r$ is distinguished as the **root**.
- Every edge is directed away from the root.
- If $(u, v)$ is a directed edge, $u$ is the **parent** and $v$ is the **child**.
- Vertices with no children are **leaves** (external nodes).
- The **depth** of $v$ is the path length from $r$ to $v$. The **height** of $T$ is the maximum depth.

#### Systematic Traversals (Binary Trees):
1. **Pre-order:** Visit Root $\to$ Traverse Left Subtree $\to$ Traverse Right Subtree.
2. **In-order:** Traverse Left Subtree $\to$ Visit Root $\to$ Traverse Right Subtree.
3. **Post-order:** Traverse Left Subtree $\to$ Traverse Right Subtree $\to$ Visit Root.

---

### 2. Huffman's Optimal Prefix Coding Algorithm

Given an alphabet $\Sigma = \{a_1, \dots, a_n\}$ with symbol frequencies $w_1, \dots, w_n$, we seek a prefix-free binary code minimizing the **expected code length**:
$$L(C) = \sum_{i=1}^n w_i \cdot \text{length}(c_i)$$

> **Greedy Algorithm (David Huffman, 1952):**
> 1. Insert all $n$ symbol leaf nodes into a min-priority queue keyed by frequency $w_i$.
> 2. While the priority queue contains more than one node:
>    - Extract the two nodes $u, v$ with the lowest frequencies.
>    - Create a new parent node $z$ with weight $w(z) = w(u) + w(v)$.
>    - Set $u$ as the left child (bit 0) and $v$ as the right child (bit 1).
>    - Insert $z$ back into the priority queue.
> 3. The single remaining node is the root of the optimal prefix tree. Runs in $O(n \log n)$ time."""
            },
            {
                "secNumber": "7.3",
                "title": "Minimum Spanning Trees: Cut Property, Kruskal's & Prim's Algorithms",
                "content": r"""### 1. The Minimum Spanning Tree (MST) Problem

Let $G = (V, E)$ be a connected undirected graph with a real-valued edge weight function $w: E \to \mathbb{R}$. A **spanning tree** $T \subseteq E$ is an acyclic subgraph connecting all $n$ vertices with $n - 1$ edges.
The **Minimum Spanning Tree (MST)** minimizes the total edge weight:
$$w(T) = \sum_{e \in T} w(e)$$

---

### 2. Fundamental Properties of MSTs

> **Theorem 7.4 (The Cut Property):**
> Let $S \subset V$ be any proper subset of vertices, and let $(S, V \setminus S)$ be the cut separating $S$ from its complement. If edge $e = \{u, v\}$ is a **strictly minimum-weight edge** crossing the cut ($u \in S, v \in V \setminus S$), then $e$ **must belong to every MST** of $G$.

*Proof by Exchange Argument:*
Let $T$ be an MST that does not contain $e$. Adding $e$ to $T$ creates a unique cycle $C$. Since $u \in S$ and $v \in V \setminus S$, the cycle $C$ must cross the cut at least once more via another edge $e' \ne e$ with $e' \in T$.
Consider the replacement tree $T' = (T \setminus \{e'\}) \cup \{e\}$.
The new tree $T'$ is connected and has $n-1$ edges, so it is a valid spanning tree.
Its total weight is:
$$w(T') = w(T) - w(e') + w(e)$$
Since $e$ is the strictly minimum weight edge crossing the cut, $w(e) < w(e')$, so $w(T') < w(T)$, contradicting the optimality of $T$. Thus $e$ must belong to $T$. $\blacksquare$

> **Theorem 7.5 (The Cycle Property):**
> For any simple cycle $C$ in $G$, the strictly heaviest edge on $C$ **cannot belong to any MST**.

---

### 3. Comparison of Greedy MST Algorithms

| Feature | Kruskal's Algorithm | Prim's Algorithm |
| :--- | :--- | :--- |
| **Strategy** | Edge-centric: global greedy edge sorting | Vertex-centric: grows a single tree component |
| **Data Structure** | Disjoint Set Union (DSU with rank & path compression) | Min-Heap / Binary Priority Queue |
| **Time Complexity** | $O(|E| \log |E|) = O(|E| \log |V|)$ | $O(|E| \log |V|)$ (or $O(|E| + |V| \log |V|)$ with Fibonacci heap) |
| **Optimal For** | Sparse graphs ($|E| \approx |V|$) | Dense graphs ($|E| \approx |V|^2$) |"""
            },
            {
                "secNumber": "7.4",
                "title": "Single-Source Shortest Paths: Dijkstra's Priority Queue Algorithm",
                "content": r"""### 1. The Shortest Path Problem

Given a directed or undirected graph $G = (V, E)$ with non-negative edge weights $w(u, v) \ge 0$ and a source vertex $s \in V$, find the shortest path distance $\delta(s, v)$ from $s$ to every vertex $v \in V$.

---

### 2. Dijkstra's Algorithm (Greedy Relaxation)

Dijkstra's algorithm maintains:
- Distance estimates $d[v]$ for each $v \in V$ (initialized to $d[s] = 0$ and $d[v] = \infty$ for $v \ne s$).
- A set $S$ of vertices whose final shortest-path weights have already been determined.
- A priority queue $Q$ containing vertices in $V \setminus S$ keyed by $d[v]$.

```text
Algorithm Dijkstra(G, w, s):
1. For each v in V: d[v] := infinity, parent[v] := null
2. d[s] := 0; Insert all v in V into min-priority queue Q
3. While Q is not empty:
4.     u := Extract-Min(Q)
5.     S := S union {u}
6.     For each neighbor v of u:
7.         If d[u] + w(u, v) < d[v]:    // Edge Relaxation
8.             d[v] := d[u] + w(u, v)
9.             parent[v] := u
10.            Decrease-Key(Q, v, d[v])
```

> **Theorem 7.6 (Correctness Invariant of Dijkstra):**
> Whenever a vertex $u$ is extracted from the priority queue ($u \in S$), its distance estimate is exact:
> $$d[u] = \delta(s, u)$$
>
> *Proof:* Assume for contradiction that $u$ is the first vertex extracted with $d[u] > \delta(s, u)$.
> Consider the true shortest path $P$ from $s$ to $u$. Let $(x, y)$ be the first edge on $P$ that leaves $S$ (so $x \in S$ and $y \notin S$).
> Because $x \in S$ was extracted earlier, $d[x] = \delta(s, x)$. Relaxing $(x, y)$ set $d[y] = \delta(s, y)$.
> Since all edge weights are **non-negative** ($w \ge 0$), subpaths have non-decreasing lengths:
> $$d[y] = \delta(s, y) \le \delta(s, u) < d[u]$$
> Thus $d[y] < d[u]$, which means the priority queue must have extracted $y$ before $u$, contradicting that $u$ was extracted! $\blacksquare$

> **Critical Warning on Negative Weights:**
> If any edge weight $w(e) < 0$, Dijkstra's greedy invariant fails, and the algorithm can yield completely incorrect shortest path values."""
            },
            {
                "secNumber": "7.5",
                "title": "All-Pairs Shortest Paths: Floyd-Warshall & Bellman-Ford Algorithms",
                "content": r"""### 1. The Floyd-Warshall Dynamic Programming Algorithm

Finds the shortest paths between **all pairs** of vertices $(i, j)$ in $O(|V|^3)$ time, accommodating negative edge weights provided there are no negative-weight cycles.

#### Dynamic Programming Formulation:
Let $d_{i,j}^{(k)}$ denote the shortest path distance from $i$ to $j$ using only intermediate vertices from the subset $\{1, 2, \dots, k\}$.
- **Base Case ($k=0$):**
  $$d_{i,j}^{(0)} = \begin{cases} 0 & \text{if } i = j \\ w(i, j) & \text{if } (i, j) \in E \\ \infty & \text{otherwise} \end{cases}$$
- **State Transition ($k \ge 1$):**
  $$d_{i,j}^{(k)} = \min\left( d_{i,j}^{(k-1)}, \; d_{i,k}^{(k-1)} + d_{k,j}^{(k-1)} \right)$$

---

### 2. Negative Cycle Detection

A **negative cycle** is a cycle whose total edge weight is strictly negative. If a negative cycle is reachable from $i$ to $j$, distances can be decreased indefinitely to $-\infty$.
- **Floyd-Warshall:** A negative cycle exists if and only if any diagonal entry becomes negative:
  $$\exists i \in V, \quad d_{i,i}^{(n)} < 0$$
- **Bellman-Ford Algorithm:** Solves single-source shortest paths in $O(|V| \cdot |E|)$ time by relaxing all edges $|V| - 1$ times. A $|V|$-th relaxation pass that further decreases any distance signals the presence of a reachable negative-weight cycle."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 7.1: Characterization of Trees and Edge-Count Induction",
                "statement": r"""Let $G = (V, E)$ be an undirected graph with $n$ vertices.
1. Prove by mathematical induction on $n$ that if $G$ is a connected graph with no simple cycles (a tree), then $G$ has exactly $n - 1$ edges:
$$|E| = |V| - 1$$
2. Prove that in every tree with $n \ge 2$ vertices, there exist at least **two vertices of degree 1** (leaves).
3. Prove that removing an edge from a tree produces a disconnected graph with exactly two connected components.""",
                "hints": [
                    "For part 1, select a leaf $v$ of degree 1 and delete it to apply induction.",
                    "For part 2, use Euler's Handshaking lemma $\\sum \\deg(v) = 2(n - 1) = 2n - 2$.",
                    "For part 3, recall that an edge $e = \\{u, v\\}$ lies on no cycles, so its removal destroys the unique path between $u$ and $v$."
                ],
                "solution": r"""### 1. Proof that a Tree on $n$ Vertices has $n-1$ Edges
We prove by mathematical induction on $n = |V|$:
- **Base Case ($n=1$):** A tree on 1 vertex contains no edges: $|E| = 0 = 1 - 1$. The formula holds.
- **Inductive Step:** Assume that every tree on $k$ vertices has $k - 1$ edges for $k \ge 1$.
  Let $T$ be a tree on $k + 1 \ge 2$ vertices.
  Since $T$ is acyclic and finite, start at any vertex and follow edges without backtracking. Because $T$ has no cycles, vertices cannot be revisited, so the path must terminate at a vertex $v$ with no other incident edges, meaning $\deg(v) = 1$ (a leaf).
  Consider the subgraph $T' = T - v$ formed by removing leaf $v$ and its single incident edge $e$.
  - $T'$ remains acyclic (removing a vertex cannot create cycles).
  - $T'$ remains connected (any path between vertices other than $v$ did not pass through $v$ because $v$ had degree 1).
  Thus $T'$ is a tree on $(k + 1) - 1 = k$ vertices!
  By the inductive hypothesis, $T'$ has $k - 1$ edges.
  The original tree $T$ has:
  $$|E(T)| = |E(T')| + 1 = (k - 1) + 1 = k = (k + 1) - 1$$
  This completes the inductive step.
By mathematical induction, every tree on $n$ vertices has $n - 1$ edges.

---

### 2. Existence of at Least Two Leaves
Let $T$ have $n \ge 2$ vertices. Since $T$ is connected, no vertex can have degree 0 ($\deg(v) \ge 1$ for all $v$).
By Euler's Handshaking lemma:
$$\sum_{v \in V} \deg(v) = 2|E| = 2(n - 1) = 2n - 2$$
Suppose for contradiction that $T$ has at most one leaf ($\le 1$ vertex of degree 1).
Then at least $n - 1$ vertices have degree $\ge 2$:
$$\sum_{v \in V} \deg(v) \ge 1 \cdot 1 + (n - 1) \cdot 2 = 1 + 2n - 2 = 2n - 1$$
This implies $2n - 2 \ge 2n - 1 \implies -2 \ge -1$, an absurd contradiction!
Therefore, $T$ must contain at least **two vertices of degree 1** (leaves).

---

### 3. Removal of an Edge Creates Exactly Two Components
Let $e = \{u, v\} \in E(T)$.
1. In $T$, there is a unique simple path between $u$ and $v$ (which is the single edge $e$).
2. In $T - e$, there is no path between $u$ and $v$ (since any alternative path in $T$ would have formed a cycle with $e$, contradicting that $T$ is acyclic).
3. Thus $T - e$ is disconnected, so it has at least 2 connected components.
4. For any vertex $w \in V$:
   - The path in $T$ from $w$ to $u$ either contained edge $e$ or did not.
   - If it did not contain $e$, $w$ remains connected to $u$ in $T - e$.
   - If it did contain $e$, its last step before reaching $u$ was crossing $e$ from $v$, which means the subpath from $w$ to $v$ does not contain $e$, so $w$ is connected to $v$ in $T - e$.
5. Hence every vertex in $T - e$ belongs to either the component containing $u$ or the component containing $v$.
6. Therefore, $T - e$ consists of **exactly two connected components**. $\blacksquare$"""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 7.2: Comparative Trace: Kruskal (DSU) vs Prim on a 7-Vertex Network",
                "statement": r"""Consider the connected weighted undirected graph $G = (V, E)$ with vertices $V = \{A, B, C, D, E, F, G\}$ and edges:
- $(A, B): 7$, $(A, D): 5$
- $(B, C): 8$, $(B, D): 9$, $(B, E): 7$
- $(C, E): 5$
- $(D, E): 15$, $(D, F): 6$
- $(E, F): 8$, $(E, G): 9$
- $(F, G): 11$

1. Trace **Kruskal's Algorithm** step-by-step:
   - Sort all edges in ascending order of weight.
   - Show the Disjoint Set Union (DSU) parent pointers and detect which edges are accepted vs rejected.
2. Trace **Prim's Algorithm** starting at vertex $A$:
   - Show the state of priority queue keys and the growing tree $V_T$ at each step.
3. Verify that both algorithms produce an identical total MST weight.""",
                "hints": [
                    "Kruskal accepts an edge if and only if Find(u) != Find(v).",
                    "Prim selects the minimum weight edge connecting $V_T$ to $V \\setminus V_T$.",
                    "The number of vertices is 7, so the MST must contain exactly $7 - 1 = 6$ edges."
                ],
                "solution": r"""### 1. Kruskal's Algorithm Trace

#### Step A: Sort Edges Ascending by Weight
1. $(A, D): 5$
2. $(C, E): 5$
3. $(D, F): 6$
4. $(A, B): 7$
5. $(B, E): 7$
6. $(B, C): 8$
7. $(E, F): 8$
8. $(B, D): 9$
9. $(E, G): 9$
10. $(F, G): 11$
11. $(D, E): 15$

#### Step B: Edge Processing with DSU
Initial sets: $\{A\}, \{B\}, \{C\}, \{D\}, \{E\}, \{F\}, \{G\}$.

1. **Edge $(A, D): 5$**: $\text{Find}(A) \ne \text{Find}(D) \implies$ **ACCEPT**.
   Merge $\{A, D\}$. Total weight $= 5$.
2. **Edge $(C, E): 5$**: $\text{Find}(C) \ne \text{Find}(E) \implies$ **ACCEPT**.
   Merge $\{C, E\}$. Total weight $= 5 + 5 = 10$.
3. **Edge $(D, F): 6$**: $\text{Find}(D) = \{A, D\} \ne \text{Find}(F) = \{F\} \implies$ **ACCEPT**.
   Merge $\{A, D, F\}$. Total weight $= 10 + 6 = 16$.
4. **Edge $(A, B): 7$**: $\text{Find}(A) = \{A, D, F\} \ne \text{Find}(B) = \{B\} \implies$ **ACCEPT**.
   Merge $\{A, B, D, F\}$. Total weight $= 16 + 7 = 23$.
5. **Edge $(B, E): 7$**: $\text{Find}(B) = \{A, B, D, F\} \ne \text{Find}(E) = \{C, E\} \implies$ **ACCEPT**.
   Merge $\{A, B, C, D, E, F\}$. Total weight $= 23 + 7 = 30$.
6. **Edge $(B, C): 8$**: $\text{Find}(B) = \text{Find}(C) \implies$ **REJECT** (forms cycle $B-C-E-B$).
7. **Edge $(E, F): 8$**: $\text{Find}(E) = \text{Find}(F) \implies$ **REJECT** (forms cycle).
8. **Edge $(B, D): 9$**: $\text{Find}(B) = \text{Find}(D) \implies$ **REJECT** (forms cycle).
9. **Edge $(E, G): 9$**: $\text{Find}(E) \ne \text{Find}(G) = \{G\} \implies$ **ACCEPT**.
   Merge to form all 7 vertices. Total weight $= 30 + 9 = 39$.

Kruskal's MST edges: $\{(A, D), (C, E), (D, F), (A, B), (B, E), (E, G)\}$.
Total MST Weight $= 39$.

---

### 2. Prim's Algorithm Trace (Starting at $A$)
- **Init:** $V_T = \{A\}$. Fringe edges from $A$: $(A, D): 5$, $(A, B): 7$.
- **Step 1:** Min fringe edge is $(A, D): 5$. Add $D$ to $V_T$.
  $V_T = \{A, D\}$. Fringe edges: $(A, B): 7$, $(D, F): 6$, $(D, B): 9$, $(D, E): 15$.
- **Step 2:** Min fringe edge is $(D, F): 6$. Add $F$ to $V_T$.
  $V_T = \{A, D, F\}$. Fringe edges: $(A, B): 7$, $(F, E): 8$, $(F, G): 11$.
- **Step 3:** Min fringe edge is $(A, B): 7$. Add $B$ to $V_T$.
  $V_T = \{A, B, D, F\}$. Fringe edges: $(B, E): 7$, $(B, C): 8$, $(F, E): 8$, $(F, G): 11$.
- **Step 4:** Min fringe edge is $(B, E): 7$. Add $E$ to $V_T$.
  $V_T = \{A, B, D, E, F\}$. Fringe edges: $(E, C): 5$, $(B, C): 8$, $(E, G): 9$, $(F, G): 11$.
- **Step 5:** Min fringe edge is $(E, C): 5$. Add $C$ to $V_T$.
  $V_T = \{A, B, C, D, E, F\}$. Fringe edges: $(E, G): 9$, $(F, G): 11$.
- **Step 6:** Min fringe edge is $(E, G): 9$. Add $G$ to $V_T$.
  $V_T = \{A, B, C, D, E, F, G\}$.

Prim's MST edges: $\{(A, D), (D, F), (A, B), (B, E), (E, C), (E, G)\}$.
Total MST Weight: $5 + 6 + 7 + 7 + 5 + 9 = 39$.

---

### 3. Conclusion
Both Kruskal and Prim produced the identical set of 6 edges and an identical total MST weight of **39**. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 7.3: Proof of the Floyd-Warshall DP Invariant & Negative Cycle Detection",
                "statement": r"""Let $G = (V, E)$ be a directed graph with arbitrary real edge weights $w: E \to \mathbb{R}$.
1. Rigorously prove by induction on $k$ the correctness of the **Floyd-Warshall dynamic programming recurrence**:
$$d_{i,j}^{(k)} = \min\left( d_{i,j}^{(k-1)}, \; d_{i,k}^{(k-1)} + d_{k,j}^{(k-1)} \right)$$
where $d_{i,j}^{(k)}$ is the weight of a shortest path from $i$ to $j$ using only intermediate vertices from $\{1, 2, \dots, k\}$.
2. Prove that $G$ contains a negative-weight cycle if and only if there exists some vertex $i \in \{1, \dots, n\}$ such that:
$$d_{i,i}^{(n)} < 0$$
3. Construct an explicit 3-vertex example with a negative edge demonstrating why Dijkstra's greedy algorithm produces an erroneous distance while Floyd-Warshall succeeds.""",
                "hints": [
                    "Consider a shortest path $p$ from $i$ to $j$ with intermediate vertices in $\\{1, \\dots, k\\}$. Does $p$ visit vertex $k$ or not?",
                    "If $p$ visits $k$, show it can visit $k$ at most once if there are no negative cycles.",
                    "For Dijkstra failure, construct a graph where a path through an edge with weight $-5$ is discovered after Dijkstra marks a node as visited."
                ],
                "solution": r"""### 1. Inductive Proof of Floyd-Warshall Recurrence

Let $V = \{1, 2, \dots, n\}$.
Define $d_{i,j}^{(k)}$ as the length of the shortest path from $i$ to $j$ whose intermediate vertices all belong to the prefix set $V_k = \{1, 2, \dots, k\}$.

#### Base Case ($k=0$):
$V_0 = \emptyset$. A path with no intermediate vertices consists of at most a single direct edge:
$$d_{i,j}^{(0)} = \begin{cases} 0 & \text{if } i = j \\ w(i, j) & \text{if } (i, j) \in E \\ \infty & \text{otherwise} \end{cases}$$
This matches the base definition.

#### Inductive Step:
Assume the invariant holds for $k - 1$.
Consider a shortest path $P$ from $i$ to $j$ with intermediate vertices in $V_k = \{1, 2, \dots, k\}$.
There are two mutually exhaustive possibilities:
1. **Vertex $k$ is NOT an intermediate vertex on $P$:**
   Then all intermediate vertices on $P$ belong to $V_{k-1}$.
   By the inductive hypothesis, the shortest such path has weight $d_{i,j}^{(k-1)}$.
2. **Vertex $k$ IS an intermediate vertex on $P$:**
   If $G$ contains no negative cycles, a shortest path never visits any vertex more than once (it is simple).
   Therefore, $P$ passes through vertex $k$ exactly once.
   We can decompose $P$ into two subpaths:
   $$P: \quad i \xrightarrow{P_1} k \xrightarrow{P_2} j$$
   - Subpath $P_1$ goes from $i$ to $k$, with intermediate vertices in $V_{k-1}$.
   - Subpath $P_2$ goes from $k$ to $j$, with intermediate vertices in $V_{k-1}$.
   By the optimal substructure property of shortest paths, $P_1$ must be a shortest path from $i$ to $k$ with intermediate vertices in $V_{k-1}$, and $P_2$ must be a shortest path from $k$ to $j$ with intermediate vertices in $V_{k-1}$.
   By the inductive hypothesis:
   $$\text{weight}(P_1) = d_{i,k}^{(k-1)}, \qquad \text{weight}(P_2) = d_{k,j}^{(k-1)}$$
   The combined weight is:
   $$\text{weight}(P) = d_{i,k}^{(k-1)} + d_{k,j}^{(k-1)}$$

Taking the minimum over both disjoint possibilities yields:
$$d_{i,j}^{(k)} = \min\left( d_{i,j}^{(k-1)}, \; d_{i,k}^{(k-1)} + d_{k,j}^{(k-1)} \right)$$
This proves the dynamic programming recurrence for all $k \in \{1, \dots, n\}$.

---

### 2. Negative Cycle Detection via Diagonal Entries
- **If a negative cycle exists:** Let $C$ be a negative cycle containing vertex $i$. Then $C$ is a closed walk from $i$ to $i$ with total weight $w(C) < 0$. Since all vertices on $C$ belong to $\{1, \dots, n\}$, after $n$ iterations the algorithm will consider paths along $C$, driving $d_{i,i}^{(n)} \le w(C) < 0$.
- **If no negative cycle exists:** Every cycle in $G$ has weight $\ge 0$. The shortest path from any vertex $i$ to itself is the empty path of length 0. Thus $d_{i,i}^{(k)} = 0$ for all $k$.
Therefore, a negative cycle exists if and only if $\exists i \in V, d_{i,i}^{(n)} < 0$.

---

### 3. Concrete Counterexample: Failure of Dijkstra with Negative Weights
Consider the 3-vertex directed graph $V = \{S, A, B\}$:
- Edge $(S, A)$ with weight $w(S, A) = 4$.
- Edge $(S, B)$ with weight $w(S, B) = 3$.
- Edge $(B, A)$ with weight $w(B, A) = -2$.

#### Dijkstra Execution (Source $S$):
1. Initialize $d[S] = 0, d[A] = \infty, d[B] = \infty$.
2. Extract $S$ from priority queue. Relax edges $(S, A)$ and $(S, B)$:
   $$d[A] = 4, \qquad d[B] = 3$$
3. Priority queue has $B$ (key 3) and $A$ (key 4).
   Min is $B$. Extract $B$ and mark as finalized ($B \in S_{\text{visited}}$).
   Relax edge $(B, A)$: $d[B] + w(B, A) = 3 + (-2) = 1 < d[A] = 4$.
   Update $d[A] = 1$.
4. Extract $A$ (key 1) and finalize ($A \in S_{\text{visited}}$).
In this example, if we modify the graph so that $A$ relaxes an edge to $B$ with negative weight:
Suppose edge $(A, B)$ has weight $-5$, and edges are $(S, A): 2$, $(S, B): 5$.
1. Relax from $S$: $d[A] = 2, d[B] = 5$.
2. Dijkstra extracts $A$ (key 2). Relax $(A, B)$: $d[B] = 2 + (-5) = -3$.
3. Dijkstra extracts $B$ (key -3).
Now suppose edge $(B, C): 2$ was already finalized:
Because Dijkstra finalizes vertices greedily, once a vertex is marked visited, Dijkstra never re-evaluates it. If a later path with negative edges reduces a predecessor's distance, the updated distance never cascades through already-visited successors, yielding invalid shortest paths.
In contrast, Floyd-Warshall evaluates all vertex combinations symmetrically, guaranteeing exact distances:
$d_{S,A} = \min(4, 3 + (-2)) = 1$. $\blacksquare$"""
            }
        ]
    }
    return u7

if __name__ == "__main__":
    u7 = get_unit7()
    print(f"Loaded Unit 7: {u7['title']} with {len(u7['sections'])} sections and {len(u7['problems'])} problems.")
