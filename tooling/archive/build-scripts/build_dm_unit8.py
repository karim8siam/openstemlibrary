# -*- coding: utf-8 -*-
"""
build_dm_unit8.py
Constructs Unit 8: Network Flows, Max-Flow Min-Cut Theorem & Combinatorial Optimization
Strictly ZERO course numbers.
"""

def get_unit8():
    u8 = {
        "number": 8,
        "title": "Network Flows, Max-Flow Min-Cut Theorem & Combinatorial Optimization",
        "leadSummary": "Algorithmic network flow theory and combinatorial duality: flow networks, conservation laws and skew symmetry, residual networks and bottleneck capacities, the Ford-Fulkerson augmenting path method, Edmonds-Karp BFS polynomial bound ($O(V E^2)$), the Max-Flow Min-Cut Theorem with complete duality proof, Dinic's blocking flow algorithm, push-relabel schemes, and reductions to Maximum Bipartite Matching, Hall's Marriage Theorem, and Menger's Theorem for edge-disjoint paths.",
        "simulations": ["sim_dm_network_max_flow"],
        "sections": [
            {
                "secNumber": "8.1",
                "title": "Flow Networks, Capacities, Conservation Laws & Residual Graphs",
                "content": r"""### 1. The Mathematical Flow Network

A **flow network** $G = (V, E, c, s, t)$ is a directed graph where:
- Each directed edge $(u, v) \in E$ has a non-negative **capacity** $c(u, v) \ge 0$. (If $(u, v) \notin E$, $c(u, v) = 0$).
- There is a designated **source** vertex $s \in V$ and **sink** vertex $t \in V$ ($s \ne t$).

> **Definition 8.1 (Feasible Flow):**
> A **flow** is a real-valued function $f: V \times V \to \mathbb{R}$ satisfying two fundamental physical axioms:
> 1. **Capacity Constraint:** For all $u, v \in V$:
>    $$0 \le f(u, v) \le c(u, v)$$
> 2. **Conservation of Flow:** For every vertex $u \in V \setminus \{s, t\}$:
>    $$\sum_{v \in V} f(v, u) = \sum_{w \in V} f(u, w)$$
>    *(Total inflow into $u$ strictly equals total outflow from $u$).*

The **net value of the flow** $|f|$ is the total net flow exiting the source $s$:
$$|f| = \sum_{v \in V} f(s, v) - \sum_{u \in V} f(u, s)$$
By conservation of flow across all intermediate nodes, this equals the net flow entering the sink $t$.

---

### 2. Residual Networks and Augmenting Paths

Given a flow $f$ in network $G$, the **residual network** $G_f = (V, E_f)$ models the remaining capacity available to send additional flow or cancel existing flow:
- The **residual capacity** $c_f(u, v)$ is:
  $$c_f(u, v) = \begin{cases} c(u, v) - f(u, v) & \text{if } (u, v) \in E \quad (\text{Forward Edge: room to add flow}) \\ f(v, u) & \text{if } (v, u) \in E \quad (\text{Backward Edge: room to cancel flow}) \\ 0 & \text{otherwise} \end{cases}$$
- The residual edge set is $E_f = \{(u, v) \in V \times V \mid c_f(u, v) > 0\}$.

An **augmenting path** $p$ is a simple directed path from source $s$ to sink $t$ in the residual graph $G_f$.
The **bottleneck capacity** of an augmenting path $p$ is:
$$c_f(p) = \min_{(u, v) \in p} c_f(u, v) > 0$$"""
            },
            {
                "secNumber": "8.2",
                "title": "The Ford-Fulkerson Method & Edmonds-Karp BFS Algorithm",
                "content": r"""### 1. The Ford-Fulkerson Method

Lester Ford and Delbert Fulkerson (1956) proposed the general augmenting path framework:
1. Initialize flow $f(u, v) = 0$ for all $(u, v) \in E$.
2. While there exists an augmenting path $p$ from $s$ to $t$ in residual network $G_f$:
   - Compute bottleneck $\Delta = c_f(p) = \min_{(u, v) \in p} c_f(u, v)$.
   - Augment flow $f$ along path $p$ by $\Delta$:
     $$f(u, v) \gets f(u, v) + \Delta \quad \text{for forward edges}$$
     $$f(v, u) \gets f(v, u) - \Delta \quad \text{for backward edges}$$
3. Return flow $f$.

> **Caveat on Path Selection:**
> If augmenting paths are chosen arbitrarily using DFS with irrational capacities, the Ford-Fulkerson method may fail to terminate or converge to a value strictly less than the maximum flow! Even with integer capacities, running time is $O(|E| \cdot |f^*|)$, which is pseudo-polynomial.

---

### 2. The Edmonds-Karp Algorithm ($O(|V| |E|^2)$)

Jack Edmonds and Richard Karp (1972) solved the convergence problem by selecting the augmenting path using **Breadth-First Search (BFS)**, choosing the shortest path in terms of the number of edges.

> **Theorem 8.1 (Edmonds-Karp Shortest-Path Monotonicity):**
> When BFS is used to find augmenting paths, for all vertices $v \in V \setminus \{s, t\}$, the shortest-path distance $\delta_f(s, v)$ in the residual network $G_f$ **increases monotonically** with each augmentation:
> $$\delta_{f'}(s, v) \ge \delta_f(s, v)$$

> **Theorem 8.2 (Edmonds-Karp Complexity):**
> The total number of augmentations performed by the Edmonds-Karp algorithm is at most $O(|V| \cdot |E|)$.
> Since each BFS takes $O(|E|)$ time, the total running time is:
> $$O(|V| \cdot |E|^2)$$"""
            },
            {
                "secNumber": "8.3",
                "title": "The Max-Flow Min-Cut Theorem & Capacity Cuts",
                "content": r"""### 1. Cuts in Flow Networks

> **Definition 8.2 (Cut):**
> An $(s, t)$-**cut** in a flow network $G = (V, E)$ is a partition of $V$ into two disjoint subsets $S$ and $T = V \setminus S$ such that $s \in S$ and $t \in T$.

The **capacity** of the cut $(S, T)$ is the sum of the capacities of all edges going from $S$ into $T$:
$$c(S, T) = \sum_{u \in S} \sum_{v \in T} c(u, v)$$
*(Note: Edges going backwards from $T$ to $S$ do NOT contribute to the cut capacity).*

The **net flow** across the cut $(S, T)$ is:
$$f(S, T) = \sum_{u \in S} \sum_{v \in T} f(u, v) - \sum_{u \in S} \sum_{v \in T} f(v, u)$$

> **Lemma 8.1 (Flow Equivalence Across Any Cut):**
> For any feasible flow $f$ and any $(s, t)$-cut $(S, T)$:
> $$f(S, T) = |f|$$

> **Corollary 8.1 (Weak Duality / Cut Capacity Upper Bound):**
> For any feasible flow $f$ and any $(s, t)$-cut $(S, T)$:
> $$|f| \le c(S, T)$$
> *Proof:* $|f| = f(S, T) = \sum_{u \in S, v \in T} f(u, v) - \sum_{v \in T, u \in S} f(v, u) \le \sum_{u \in S, v \in T} f(u, v) \le \sum_{u \in S, v \in T} c(u, v) = c(S, T)$. $\blacksquare$

---

### 2. The Max-Flow Min-Cut Theorem

> **Theorem 8.3 (Max-Flow Min-Cut Theorem - Ford & Fulkerson, 1956):**
> Let $f$ be a flow in a flow network $G = (V, E, c, s, t)$. The following three conditions are logically equivalent:
> 1. $f$ is a **maximum flow** in $G$.
> 2. The residual network $G_f$ contains **no augmenting paths** from $s$ to $t$.
> 3. $|f| = c(S, T)$ for some $(s, t)$-cut $(S, T)$ (which is necessarily a **minimum cut**).
>
> In particular:
> $$\max_{f} |f| = \min_{(S, T)} c(S, T)$$"""
            },
            {
                "secNumber": "8.4",
                "title": "Advanced Flow Algorithms: Dinic's & Push-Relabel Schemes",
                "content": r"""### 1. Dinic's Blocking Flow Algorithm ($O(|V|^2 |E|)$)

Yefim Dinic (1970) introduced the concept of **layered networks** and **blocking flows**:
1. Construct the layered network $G_L$ using BFS from $s$, where vertices are assigned level numbers $\text{level}(v) = \text{dist}(s, v)$. Edges only go from level $k$ to level $k+1$.
2. In the layered network $G_L$, find a **blocking flow** using DFS (a flow where every path from $s$ to $t$ contains at least one saturated edge).
3. Update the residual network and repeat.
Dinic's algorithm requires at most $|V|-1$ phase iterations. Finding a blocking flow takes $O(|V| |E|)$ time, yielding total time:
$$O(|V|^2 |E|)$$
On unit networks (where capacities are 1, e.g., bipartite matching), Dinic runs in $O(|E| \sqrt{|V|})$ time!

---

### 2. Goldberg-Tarjan Push-Relabel Algorithm

Unlike Ford-Fulkerson which maintains flow conservation at all times, the **push-relabel** method allows nodes to store excess flow (**preflow**):
$$e(u) = \sum_{v} f(v, u) - \sum_{w} f(u, w) \ge 0$$
- Vertices are assigned height/distance labels $h(u)$, initialized with $h(s) = |V|$ and $h(t) = 0$.
- **Push Operation:** If $e(u) > 0$, $c_f(u, v) > 0$, and $h(u) = h(v) + 1$, push $\min(e(u), c_f(u, v))$ flow from $u$ to $v$.
- **Relabel Operation:** If $e(u) > 0$ and no push is possible, increase height: $h(u) \gets 1 + \min \{h(v) \mid (u, v) \in E_f\}$.
Running time with highest-label selection is $O(|V|^2 \sqrt{|E|})$, outperforming augmenting paths on dense graphs."""
            },
            {
                "secNumber": "8.5",
                "title": "Bipartite Matching, Hall's Theorem & Interactive Max-Flow Simulator",
                "content": r"""### 1. Reduction: Maximum Bipartite Matching to Max-Flow

Let $G = (X \cup Y, E)$ be an undirected bipartite graph.
Construct directed flow network $G' = (V', E', c)$ by:
1. $V' = X \cup Y \cup \{s, t\}$.
2. Add directed edges $(s, x)$ for all $x \in X$ with capacity $c(s, x) = 1$.
3. Add directed edges $(y, t)$ for all $y \in Y$ with capacity $c(y, t) = 1$.
4. Direct all bipartite edges from $X$ to $Y$: $(x, y)$ with capacity $c(x, y) = \infty$ (or 1).

> **Integrality Theorem:** If all edge capacities are integers, the maximum flow computed by Ford-Fulkerson is strictly integer-valued ($f(e) \in \{0, 1\}$).
> The edges between $X$ and $Y$ with $f(x, y) = 1$ form a **maximum matching** of $G$, and $|f^*| = \text{max matching size}$.

---

### 2. Hall's Marriage Theorem via Max-Flow Min-Cut

> **Theorem 8.4 (Hall's Marriage Theorem, 1935):**
> A bipartite graph $G = (X \cup Y, E)$ has a matching that saturates every vertex in $X$ if and only if **Hall's Condition** holds:
> $$\forall A \subseteq X, \quad |N(A)| \ge |A|$$
> where $N(A) = \{y \in Y \mid \exists x \in A, \{x, y\} \in E\}$ is the neighborhood of $A$.

*Proof via Min-Cut Duality:*
If the max flow is less than $|X|$, then by Max-Flow Min-Cut, there exists a cut $(S, T)$ with capacity $c(S, T) < |X|$.
Let $A = X \setminus S$ (the vertices of $X$ on the sink side of the cut).
The edges crossing the cut are $(s, x)$ for $x \in X \setminus A$ and $(y, t)$ for $y \in N(A) \cap S$.
Calculating capacity: $c(S, T) = (|X| - |A|) + |N(A)|$.
Since $c(S, T) < |X|$, we have $|X| - |A| + |N(A)| < |X| \implies |N(A)| < |A|$, which directly violates Hall's condition! $\blacksquare$

---

### 3. Interactive Max-Flow Min-Cut Simulator

The simulation below demonstrates network flow dynamics:
- **Augmenting Path Tracer:** Step-by-step BFS finding augmenting paths and bottleneck residual capacities.
- **Residual Graph Display:** Toggle between real-time flow and residual edge capacities.
- **Minimum Cut Visualizer:** Visualizes reachable vertices $S$ from source $s$, highlighting the bottleneck saturated edges crossing into $T$."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 8.1: Complete Edmonds-Karp Execution and Min-Cut Bottleneck",
                "statement": r"""Consider the flow network $G = (V, E)$ with vertices $V = \{s, A, B, C, D, t\}$ and directed edge capacities:
- $(s, A): 10$, $(s, C): 10$
- $(A, B): 4$, $(A, C): 2$, $(A, D): 8$
- $(C, D): 9$
- $(B, t): 10$
- $(D, B): 6$, $(D, t): 10$

1. Trace the **Edmonds-Karp algorithm** step-by-step:
   - Identify each augmenting path $p$ selected by Breadth-First Search (BFS).
   - Compute the bottleneck capacity $c_f(p)$ for each path.
   - Update the residual capacities of forward and backward edges.
2. Calculate the final maximum flow value $|f^*|$.
3. Identify the subset $S \subseteq V$ of vertices reachable from $s$ in the final residual graph $G_f$, and compute the capacity of the resulting minimum cut $(S, V \setminus S)$ to verify the Max-Flow Min-Cut theorem.""",
                "hints": [
                    "BFS finds the path with the fewest edges from $s$ to $t$.",
                    "Remember that augmenting along an edge creates a backward edge with residual capacity equal to the augmented flow.",
                    "The minimum cut is formed by $S = \\{v \\in V \\mid v \\text{ is reachable from } s \\text{ in } G_f\\}$."
                ],
                "solution": r"""### 1. Step-by-Step Edmonds-Karp Trace

Initial flow: $f(e) = 0$ for all edges.

#### Augmentation 1:
- BFS searches for the shortest path in edge count from $s$ to $t$:
  Path $p_1: s \to A \to B \to t$ (length 3 edges).
- Capacities along $p_1$:
  $c_f(s, A) = 10, \; c_f(A, B) = 4, \; c_f(B, t) = 10$.
- Bottleneck: $\Delta_1 = \min(10, 4, 10) = 4$.
- Update flow:
  $f(s, A) = 4, \; f(A, B) = 4, \; f(B, t) = 4$.
- Residual capacity updates:
  $c_f(s, A) = 6, \; c_f(A, s) = 4$.
  $c_f(A, B) = 0$ (Saturated!), $c_f(B, A) = 4$.
  $c_f(B, t) = 6, \; c_f(t, B) = 4$.
- Flow value: $|f| = 4$.

#### Augmentation 2:
- BFS finds the next shortest path:
  Path $p_2: s \to C \to D \to t$ (length 3 edges).
- Capacities along $p_2$:
  $c_f(s, C) = 10, \; c_f(C, D) = 9, \; c_f(D, t) = 10$.
- Bottleneck: $\Delta_2 = \min(10, 9, 10) = 9$.
- Update flow:
  $f(s, C) = 9, \; f(C, D) = 9, \; f(D, t) = 9$.
- Residual capacities:
  $c_f(s, C) = 1, \; c_f(C, s) = 9$.
  $c_f(C, D) = 0$ (Saturated!), $c_f(D, C) = 9$.
  $c_f(D, t) = 1, \; c_f(t, D) = 9$.
- Flow value: $|f| = 4 + 9 = 13$.

#### Augmentation 3:
- BFS shortest path:
  Path $p_3: s \to A \to D \to t$ (length 3 edges).
- Capacities along $p_3$:
  $c_f(s, A) = 6, \; c_f(A, D) = 8, \; c_f(D, t) = 1$.
- Bottleneck: $\Delta_3 = \min(6, 8, 1) = 1$.
- Update flow:
  $f(s, A) = 4 + 1 = 5$.
  $f(A, D) = 1$.
  $f(D, t) = 9 + 1 = 10$ (Saturated!).
- Residual capacities:
  $c_f(s, A) = 5, \; c_f(A, s) = 5$.
  $c_f(A, D) = 7, \; c_f(D, A) = 1$.
  $c_f(D, t) = 0$ (Saturated!), $c_f(t, D) = 10$.
- Flow value: $|f| = 13 + 1 = 14$.

#### Augmentation 4:
- BFS shortest path:
  Path $p_4: s \to A \to D \to B \to t$ (length 4 edges).
- Capacities along $p_4$:
  $c_f(s, A) = 5, \; c_f(A, D) = 7, \; c_f(D, B) = 6, \; c_f(B, t) = 6$.
- Bottleneck: $\Delta_4 = \min(5, 7, 6, 6) = 5$.
- Update flow:
  $f(s, A) = 5 + 5 = 10$ (Saturated!).
  $f(A, D) = 1 + 5 = 6$.
  $f(D, B) = 5$.
  $f(B, t) = 4 + 5 = 9$.
- Residual capacities:
  $c_f(s, A) = 0$ (Saturated!), $c_f(A, s) = 10$.
  $c_f(A, D) = 2, \; c_f(D, A) = 6$.
  $c_f(D, B) = 1, \; c_f(B, D) = 5$.
  $c_f(B, t) = 1, \; c_f(t, B) = 9$.
- Flow value: $|f| = 14 + 5 = 19$.

#### Augmentation 5:
- Looking for path from $s$:
  $c_f(s, A) = 0$.
  Only outgoing edge from $s$ with residual capacity $>0$ is $(s, C)$ with $c_f(s, C) = 1$.
- From $C$:
  $c_f(C, D) = 0$.
  No other outgoing edges from $C$.
- BFS terminates: No path exists from $s$ to $t$ in $G_f$!

---

### 2. Maximum Flow Value
The maximum flow achieved is:
$$|f^*| = 19$$

---

### 3. Reachability Set and Minimum Cut Verification
In the final residual network $G_f$, find all vertices reachable from $s$:
- Start at $s$.
- Can reach $C$ via edge $(s, C)$ because $c_f(s, C) = 1 > 0$.
- From $C$: no outgoing residual edges with capacity $> 0$.
- From $s$: edge to $A$ has $c_f(s, A) = 0$.
Thus, the set of reachable vertices from $s$ is:
$$S = \{s, C\}$$
The complement set is:
$$T = V \setminus S = \{A, B, D, t\}$$

Calculate the cut capacity $c(S, T)$:
$$c(S, T) = \sum_{u \in S, v \in T} c(u, v) = c(s, A) + c(C, D)$$
(Note: edge $(A, C)$ goes from $T$ to $S$, so it is NOT included).
$$c(S, T) = c(s, A) + c(C, D) = 10 + 9 = 19$$

Since $|f^*| = 19 = c(S, T)$, the Max-Flow Min-Cut theorem is verified with exact equality! $\blacksquare$"""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 8.2: Rigorous Analytical Proof of the Max-Flow Min-Cut Theorem",
                "statement": r"""Let $G = (V, E, c, s, t)$ be a flow network with real capacities $c: E \to \mathbb{R}^+$.
1. Prove the **Flow Conservation Lemma Across Cuts**: For any feasible flow $f$ and any $(s, t)$-cut $(S, T)$, the net flow across $(S, T)$ satisfies:
$$f(S, T) = |f|$$
2. Prove **Weak Duality**: For any feasible flow $f$ and any $(s, t)$-cut $(S, T)$, $|f| \le c(S, T)$.
3. Prove **Strong Duality (Max-Flow Min-Cut Theorem)**: If a feasible flow $f^*$ admits no augmenting path in the residual network $G_{f^*}$, then there exists an $(s, t)$-cut $(S^*, T^*)$ such that:
$$|f^*| = c(S^*, T^*)$$
thereby proving that $f^*$ is a maximum flow and $(S^*, T^*)$ is a minimum cut.""",
                "hints": [
                    "For part 1, sum the conservation equations $\\sum_{v} f(u, v) - \\sum_{v} f(v, u)$ over all $u \\in S$.",
                    "For part 3, define $S^* = \\{v \\in V \\mid \\text{there exists a directed path from } s \\text{ to } v \\text{ in } G_{f^*}\\}$.",
                    "Show that for every $u \\in S^*$ and $v \\in T^*$, $f^*(u, v) = c(u, v)$ and $f^*(v, u) = 0$."
                ],
                "solution": r"""### 1. Proof of Flow Conservation Lemma Across Cuts
Let $(S, T)$ be any $(s, t)$-cut, so $s \in S$ and $t \in T = V \setminus S$.
By definition of flow value, for the source node $s$:
$$|f| = \sum_{v \in V} f(s, v) - \sum_{v \in V} f(v, s)$$
For every intermediate node $u \in S \setminus \{s\}$ (since $t \notin S$):
$$\sum_{v \in V} f(u, v) - \sum_{v \in V} f(v, u) = 0 \quad (\text{Conservation of Flow})$$
Summing these expressions over all vertices $u \in S$:
$$|f| = \sum_{u \in S} \left( \sum_{v \in V} f(u, v) - \sum_{v \in V} f(v, u) \right)$$
Now split the summation over $v \in V$ into $v \in S$ and $v \in T$:
$$\begin{aligned}
|f| &= \sum_{u \in S} \left( \sum_{v \in S} f(u, v) + \sum_{v \in T} f(u, v) - \sum_{v \in S} f(v, u) - \sum_{v \in T} f(v, u) \right) \\
&= \sum_{u \in S}\sum_{v \in S} f(u, v) - \sum_{u \in S}\sum_{v \in S} f(v, u) + \sum_{u \in S}\sum_{v \in T} f(u, v) - \sum_{u \in S}\sum_{v \in T} f(v, u)
\end{aligned}$$
In the first two double sums, both indices $u$ and $v$ range over $S$. Renaming dummy variables reveals that $\sum_{u \in S}\sum_{v \in S} f(u, v)$ and $\sum_{u \in S}\sum_{v \in S} f(v, u)$ are identical sums of internal edge flows, so they cancel completely!
What remains is:
$$|f| = \sum_{u \in S}\sum_{v \in T} f(u, v) - \sum_{u \in S}\sum_{v \in T} f(v, u) = f(S, T)$$
Thus, the net flow across any cut $(S, T)$ strictly equals $|f|$. $\blacksquare$

---

### 2. Proof of Weak Duality
By part 1:
$$|f| = \sum_{u \in S}\sum_{v \in T} f(u, v) - \sum_{v \in T}\sum_{u \in S} f(v, u)$$
By the capacity constraint, flow is non-negative, so $f(v, u) \ge 0$, which implies $-\sum_{v \in T}\sum_{u \in S} f(v, u) \le 0$.
Furthermore, $f(u, v) \le c(u, v)$ for all edges.
Therefore:
$$|f| \le \sum_{u \in S}\sum_{v \in T} f(u, v) \le \sum_{u \in S}\sum_{v \in T} c(u, v) = c(S, T)$$
Hence, the capacity of **any** cut is an upper bound on the value of **any** feasible flow:
$$|f| \le c(S, T) \blacksquare$$

---

### 3. Proof of Strong Duality (Max-Flow Min-Cut Theorem)
Let $f^*$ be a feasible flow such that the residual network $G_{f^*}$ contains **no augmenting paths** from $s$ to $t$.
Define the set:
$$S^* = \{v \in V \mid \text{there exists a directed path from } s \text{ to } v \text{ in } G_{f^*}\}$$
and let $T^* = V \setminus S^*$.

1. **$(S^*, T^*)$ is a valid $(s, t)$-cut:**
   - Clearly $s \in S^*$ (path of length 0).
   - Since $G_{f^*}$ contains no path from $s$ to $t$, $t \notin S^*$, which means $t \in T^*$.
2. **Analysis of edges crossing from $S^*$ to $T^*$:**
   Let $u \in S^*$ and $v \in T^*$.
   Suppose for contradiction that $(u, v) \in E$ and $f^*(u, v) < c(u, v)$.
   Then the residual capacity is:
   $$c_{f^*}(u, v) = c(u, v) - f^*(u, v) > 0$$
   This implies that $(u, v)$ is an edge in the residual graph $G_{f^*}$!
   Since $u \in S^*$, there is a path from $s$ to $u$ in $G_{f^*}$. Appending edge $(u, v)$ yields a path from $s$ to $v$ in $G_{f^*}$, meaning $v \in S^*$.
   This contradicts $v \in T^*$!
   Therefore, for every edge $(u, v) \in E$ with $u \in S^*, v \in T^*$, we must have:
   $$f^*(u, v) = c(u, v) \quad (\text{Every forward edge is strictly saturated})$$
3. **Analysis of backward edges from $T^*$ to $S^*$:**
   Suppose for contradiction that $(v, u) \in E$ with $v \in T^*, u \in S^*$ and $f^*(v, u) > 0$.
   Then the backward residual capacity is:
   $$c_{f^*}(u, v) = f^*(v, u) > 0$$
   This again implies $(u, v) \in E_{f^*}$, making $v$ reachable from $s$ in $G_{f^*}$ ($v \in S^*$), another contradiction!
   Therefore, for every edge $(v, u) \in E$ with $v \in T^*, u \in S^*$:
   $$f^*(v, u) = 0 \quad (\text{Every backward edge carries zero flow})$$

Now compute the net flow across $(S^*, T^*)$ using Lemma 8.1:
$$|f^*| = f(S^*, T^*) = \sum_{u \in S^*, v \in T^*} f^*(u, v) - \sum_{v \in T^*, u \in S^*} f^*(v, u) = \sum_{u \in S^*, v \in T^*} c(u, v) - 0 = c(S^*, T^*)$$
By Weak Duality, no flow can exceed $c(S^*, T^*)$, so $f^*$ achieves the absolute maximum possible flow, and $(S^*, T^*)$ achieves the absolute minimum possible cut capacity.
Hence:
$$\max_f |f| = \min_{(S, T)} c(S, T) \blacksquare$$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 8.3: Bipartite Matching, Hall's Theorem & Menger's Duality",
                "statement": r"""Let $G = (X \cup Y, E)$ be a finite bipartite graph with vertex bipartition $(X, Y)$.
1. Construct the canonical flow network reduction $G' = (V', E', c)$ for finding a maximum bipartite matching.
2. Prove that the Integrality Theorem guarantees that the maximum flow in $G'$ corresponds to a maximum matching in $G$.
3. Prove **Hall's Marriage Theorem** as an immediate consequence of the Max-Flow Min-Cut Theorem:
$G$ has a matching covering all vertices in $X$ if and only if for all $A \subseteq X$, $|N(A)| \ge |A|$.
4. Show how Menger's Theorem (the maximum number of edge-disjoint paths between $s$ and $t$ equals the minimum size of an edge cut separating $s$ and $t$) follows directly from unit network flow duality.""",
                "hints": [
                    "In the reduction, set capacities $c(s, x) = 1$ for $x \\in X$, $c(y, t) = 1$ for $y \\in Y$, and $c(x, y) = \\infty$ for edges between $X$ and $Y$.",
                    "For Hall's condition, analyze the capacity of a minimum cut $(S, T)$ if $|f^*| < |X|$. Let $A = X \\cap T$.",
                    "Notice that $c(x, y) = \\infty$ prevents any edge from $X \\cap S$ to $Y \\cap T$ from existing, which forces $N(A) \\subseteq Y \\cap S$."
                ],
                "solution": r"""### 1. Construction of Canonical Flow Network $G'$
Given bipartite graph $G = (X \cup Y, E)$:
- Vertex set: $V' = X \cup Y \cup \{s, t\}$, where $s$ is a new source and $t$ is a new sink.
- Directed edge set and capacities:
  1. For each $x \in X$, add edge $(s, x)$ with capacity $c(s, x) = 1$.
  2. For each $y \in Y$, add edge $(y, t)$ with capacity $c(y, t) = 1$.
  3. For each undirected edge $\{x, y\} \in E$ with $x \in X, y \in Y$, add directed edge $(x, y)$ with capacity $c(x, y) = \infty$ (or $c(x, y) = 1$).

---

### 2. Integrality and Matching Equivalence
By the Integrality Theorem for Network Flows:
If all edge capacities are integers, the Ford-Fulkerson algorithm (with integer additions) terminates with a flow where $f(e) \in \mathbb{Z}$ for every edge $e$.
- For each edge $(s, x)$, capacity is 1, so $f(s, x) \in \{0, 1\}$.
- For each edge $(y, t)$, capacity is 1, so $f(y, t) \in \{0, 1\}$.
- By conservation of flow at $x \in X$: $\sum_{y \in Y} f(x, y) = f(s, x) \le 1$. Thus, at most one outgoing edge from $x$ carries flow 1.
- By conservation of flow at $y \in Y$: $\sum_{x \in X} f(x, y) = f(y, t) \le 1$. Thus, at most one incoming edge into $y$ carries flow 1.

Therefore, the set of edges:
$$M = \{\{x, y\} \in E \mid f(x, y) = 1\}$$
is a valid **matching** in $G$ (no two edges share a vertex).
The size of the matching is:
$$|M| = \sum_{x \in X, y \in Y} f(x, y) = |f|$$
Conversely, any matching $M$ of size $k$ yields a valid integer flow of value $k$.
Thus:
$$\text{Maximum Matching Size in } G = \text{Maximum Flow Value } |f^*| \text{ in } G'$$

---

### 3. Proof of Hall's Marriage Theorem via Max-Flow Min-Cut

#### Necessity ($\implies$):
If a matching $M$ saturates all of $X$, then for any subset $A \subseteq X$, the edges of $M$ incident with $A$ match each element of $A$ to a distinct element in $Y$. All these targets belong to $N(A)$.
Therefore, $|N(A)| \ge |A|$.

#### Sufficiency ($\impliedby$):
Assume Hall's condition holds: $\forall A \subseteq X, |N(A)| \ge |A|$.
We must prove that the maximum flow satisfies $|f^*| = |X|$.
Suppose for contradiction that $|f^*| < |X|$.
By the Max-Flow Min-Cut Theorem, there exists an $(s, t)$-cut $(S, T)$ with capacity:
$$c(S, T) = |f^*| < |X|$$
where $s \in S$ and $t \in T$.

Define the partition of $X$ and $Y$ by the cut:
$$X_S = X \cap S, \quad X_T = X \cap T, \quad Y_S = Y \cap S, \quad Y_T = Y \cap T$$
Now examine the edges crossing from $S$ to $T$:
1. Edges from $s$ to $X_T$: Each has capacity 1. There are $|X_T|$ such edges.
2. Edges from $Y_S$ to $t$: Each has capacity 1. There are $|Y_S|$ such edges.
3. Edges from $X_S$ to $Y_T$: Each has capacity $\infty$.
Since $c(S, T) < |X| < \infty$, the cut capacity must be **finite**!
Therefore, there can be **no edges** from $X_S$ to $Y_T$:
$$\text{No edge } (x, y) \text{ exists with } x \in X_S \text{ and } y \in Y_T$$
This implies that all neighbors of $X_S$ in $G$ must lie inside $Y_S$:
$$N(X_S) \subseteq Y_S \implies |N(X_S)| \le |Y_S|$$

Now calculate the capacity of the cut:
$$c(S, T) = |X_T| + |Y_S|$$
Since $X$ is partitioned into $X_S$ and $X_T$, $|X_T| = |X| - |X_S|$.
Substitute this into the inequality:
$$c(S, T) = (|X| - |X_S|) + |Y_S| < |X|$$
Subtracting $|X|$ from both sides:
$$-|X_S| + |Y_S| < 0 \implies |Y_S| < |X_S|$$
Since $|N(X_S)| \le |Y_S|$, we obtain:
$$|N(X_S)| \le |Y_S| < |X_S|$$
Letting $A = X_S \subseteq X$, we have constructed a subset $A$ such that:
$$|N(A)| < |A|$$
This directly contradicts Hall's Condition!
Therefore, the contradiction assumption was false. We must have $|f^*| = |X|$, guaranteeing a matching that saturates all of $X$. $\blacksquare$

---

### 4. Menger's Theorem for Edge-Disjoint Paths
Let $G = (V, E)$ be a directed graph with source $s$ and sink $t$. Assign every edge unit capacity $c(e) = 1$.
1. By the Integrality Theorem, the maximum flow $f^*$ is an integer flow with $f^*(e) \in \{0, 1\}$.
2. By flow decomposition, any $0-1$ flow can be decomposed into $|f^*|$ edge-disjoint directed paths from $s$ to $t$.
3. By the Max-Flow Min-Cut Theorem, $|f^*| = c(S^*, T^*)$.
4. Since every edge has capacity 1, $c(S^*, T^*)$ is precisely the number of edges crossing from $S^*$ to $T^*$, which forms a minimal edge cut disconnecting $s$ from $t$.
Hence, the maximum number of edge-disjoint paths from $s$ to $t$ equals the minimum number of edges whose removal disconnects $s$ and $t$. $\blacksquare$"""
            }
        ]
    }
    return u8

if __name__ == "__main__":
    u8 = get_unit8()
    print(f"Loaded Unit 8: {u8['title']} with {len(u8['sections'])} sections and {len(u8['problems'])} problems.")
