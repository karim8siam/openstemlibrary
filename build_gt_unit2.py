# -*- coding: utf-8 -*-
"""
build_gt_unit2.py
Constructs Unit 2: Walks, Paths, Circuits, Eulerian Graphs & Hamiltonian Cycles
"""

def get_unit2():
    u2 = {
        "number": 2,
        "title": "Walks, Paths, Circuits, Eulerian Graphs & Hamiltonian Cycles",
        "leadSummary": "Exhaustive exploration of graph traversals: walks, trails, paths, circuits and cycles, connectedness and components, Eulerian graphs, Euler's Theorem, Fleury's algorithm, the Instant Insanity multicolored cubes puzzle, Hamiltonian paths and circuits, Dirac's Theorem, Ore's Theorem, and the Traveling Salesperson Problem (TSP).",
        "simulations": ["sim_gt_euler_hamilton"],
        "sections": [
            {
                "secNumber": "2.1",
                "title": "Walks, Trails, Paths, Circuits & Subgraph Classes",
                "content": r"""### 1. Hierarchy of Graph Traversals

Traversals across vertices and edges are characterized by the restrictions imposed on repeated vertices and repeated edges:

> **Definition 2.1 (Walk):**
> A **walk** $W$ of length $k$ from vertex $u$ to vertex $v$ (a $u$-$v$ walk) in a graph $G$ is an alternating sequence of vertices and edges:
> $$W = (v_0, e_1, v_1, e_2, v_2, \dots, e_k, v_k)$$
> such that $v_0 = u$, $v_k = v$, and each edge $e_i$ has endpoints $v_{i-1}$ and $v_i$.
> In simple graphs, edges are uniquely determined by endpoints, so a walk is denoted simply by the vertex sequence $(v_0, v_1, \dots, v_k)$.

- **Closed Walk:** A walk where $v_0 = v_k$ (starts and terminates at the identical vertex).
- **Open Walk:** A walk where $v_0 \ne v_k$.

> **Definition 2.2 (Trail and Circuit):**
> 1. A **trail** is a walk in which **no edge is repeated** (all $e_i$ are distinct). Vertices may be repeated.
> 2. A **circuit** is a **closed trail** ($v_0 = v_k$ with no repeated edges).

> **Definition 2.3 (Path and Cycle):**
> 1. A **path** (or simple path) is an open walk in which **no vertex is repeated** (and consequently no edge is repeated).
> 2. A **cycle** (or simple circuit) is a closed walk $(v_0, v_1, \dots, v_k = v_0)$ of length $k \ge 3$ in which all intermediate vertices $v_0, v_1, \dots, v_{k-1}$ are distinct.

| Traversal Type | Repeated Vertices? | Repeated Edges? | Open / Closed |
| :--- | :--- | :--- | :--- |
| **Walk** | Allowed | Allowed | Either |
| **Trail** | Allowed | **Forbidden** | Open |
| **Circuit** | Allowed | **Forbidden** | Closed |
| **Path** | **Forbidden** | **Forbidden** | Open |
| **Cycle** | Ends Only ($v_0 = v_k$) | **Forbidden** | Closed ($k \ge 3$) |

---

### 2. The Walk-Path Reduction Lemma

> **Lemma 2.1 (Every Walk Contains a Path):**
> If a graph $G$ contains a walk of length $k$ connecting vertex $u$ to vertex $v$, then $G$ contains a simple path connecting $u$ to $v$ of length at most $k$.

#### Complete Proof (by Well-Ordering Principle):
Let $S$ be the set of lengths of all $u$-$v$ walks in $G$.
By hypothesis, $k \in S$, so $S \subseteq \mathbb{Z}_{\ge 0}$ is non-empty.
By the Well-Ordering Principle of non-negative integers, $S$ contains a minimum element; call it $m \le k$.
Let $P = (u = v_0, v_1, \dots, v_m = v)$ be a $u$-$v$ walk of minimum length $m$.
We claim that $P$ is a simple path (i.e., all vertices are distinct).
Suppose for contradiction that $P$ repeats a vertex: $v_i = v_j$ for some $0 \le i < j \le m$.
Then we can excise the sub-walk between $v_i$ and $v_j$, yielding:
$$P' = (v_0, \dots, v_i, v_{j+1}, \dots, v_m)$$
Notice that $P'$ is a valid $u$-$v$ walk in $G$.
The length of $P'$ is $m - (j - i) < m$.
This directly contradicts the minimality of $m$!
Therefore, $P$ cannot contain any repeated vertices.
Hence $P$ is a simple path of length $m \le k$. $\blacksquare$"""
            },
            {
                "secNumber": "2.2",
                "title": "Connectedness, Components & Equivalence Relations",
                "content": r"""### 1. Connectedness in Undirected Graphs

> **Definition 2.4 (Connected Graph):**
> Two vertices $u, v \in V(G)$ are said to be **connected** if there exists a $u$-$v$ path in $G$.
> A graph $G$ is called a **connected graph** if every pair of distinct vertices in $G$ is connected.
> Otherwise, $G$ is called **disconnected**.

---

### 2. The Connected Component Equivalence Relation

> **Theorem 2.1 (Connectivity as an Equivalence Relation):**
> Define a binary relation $\sim$ on the vertex set $V(G)$ by:
> $$u \sim v \iff \text{there exists a } u\text{-}v \text{ path in } G$$
> (with $u \sim u$ trivially via a path of length 0).
> Then $\sim$ is an **equivalence relation** on $V(G)$.

#### Complete Proof:
1. **Reflexivity:** For any $u \in V$, the trivial single-vertex path $(u)$ shows $u \sim u$.
2. **Symmetry:** Suppose $u \sim v$. Then there exists a path $P = (u = v_0, v_1, \dots, v_k = v)$.
   Reversing the sequence gives $P^{-1} = (v = v_k, v_{k-1}, \dots, v_0 = u)$, which is a valid $v$-$u$ path. Thus $v \sim u$.
3. **Transitivity:** Suppose $u \sim v$ and $v \sim w$.
   Then there exists a $u$-$v$ walk and a $v$-$w$ walk.
   Concatenating these two walks yields a $u$-$w$ walk.
   By Lemma 2.1, this walk contains a simple $u$-$w$ path.
   Thus $u \sim w$.
Therefore, $\sim$ is an equivalence relation. $\blacksquare$

> **Definition 2.5 (Connected Components):**
> The equivalence classes of $V(G) / \sim$ induce maximal connected subgraphs called the **connected components** of $G$.
> The number of connected components of $G$ is denoted by $\omega(G)$ or $k(G)$.
> A graph $G$ is connected if and only if $\omega(G) = 1$."""
            },
            {
                "secNumber": "2.3",
                "title": "Eulerian Graphs: Euler's Theorem & Fleury's Algorithm",
                "content": r"""### 1. Eulerian Circuits and Trails

Named after Leonhard Euler's seminal 1736 paper resolving the Königsberg bridges problem:

> **Definition 2.6 (Eulerian Circuit and Trail):**
> 1. An **Eulerian trail** (or Euler path) in a graph $G$ is a trail that traverses **every edge of $G$ exactly once**.
> 2. An **Eulerian circuit** (or Euler tour) is a closed trail that visits **every edge of $G$ exactly once**.
> 3. A graph $G$ is called **Eulerian** if it contains an Eulerian circuit.
> 4. A graph $G$ is called **semi-Eulerian** if it contains an open Eulerian trail (but no Eulerian circuit).

---

### 2. Euler's Characterization Theorem

> **Theorem 2.2 (Euler's Theorem for Eulerian Graphs):**
> Let $G$ be a connected graph (or a graph whose non-trivial components contain all edges).
> 1. $G$ is **Eulerian** if and only if **every vertex of $G$ has even degree**:
>    $$\deg(v) \equiv 0 \pmod 2, \quad \forall v \in V(G)$$
> 2. $G$ contains an open **Eulerian trail** if and only if it has **exactly two vertices of odd degree**. In this case, the trail must originate at one odd-degree vertex and terminate at the other.

#### Complete Formal Proof of Part 1:
- **$(\implies)$ Necessity:**
  Suppose $G$ has an Eulerian circuit $C$.
  Let $v \in V(G)$.
  Every time the circuit enters vertex $v$ via some edge, it must depart from $v$ via a distinct, previously unused edge.
  Since $C$ traverses every edge of $G$ exactly once, the edges incident with $v$ are partitioned into pairs (one entry edge, one exit edge).
  If $v$ is the starting and ending vertex of $C$, the initial departure and final entry also form a pair.
  Therefore, the number of incident edges $\deg(v)$ is twice the number of times $C$ visits $v$:
  $$\deg(v) = 2 \times (\text{number of visits of } C \text{ to } v)$$
  Hence $\deg(v)$ is even for every vertex.

- **$(\impliedby)$ Sufficiency (by induction on $|E|$):**
  Assume every vertex in the connected graph $G$ has even degree, and $|E| \ge 1$.
  - **Step 1 (Existence of a Cycle):**
    Since $G$ is connected and has at least one edge, and no vertex has degree 0 or 1 (all degrees are even and $\ge 2$), by Theorem 1.3, $G$ must contain at least one simple cycle $C_1$.
  - **Step 2 (Decomposition):**
    Remove all edges of $C_1$ from $G$, forming the subgraph $G' = G - E(C_1)$.
    In $C_1$, each vertex has degree 2 (or 0).
    Thus, for every $v \in V(G')$:
    $$\deg_{G'}(v) = \deg_G(v) - \deg_{C_1}(v) \equiv 0 - 0 \equiv 0 \pmod 2$$
    Every vertex in $G'$ still has even degree!
  - **Step 3 (Inductive Splicing):**
    By induction hypothesis, each connected component of $G'$ has an Eulerian circuit.
    Since $G$ was connected, each component of $G'$ shares at least one vertex with the cycle $C_1$.
    We traverse $C_1$, and whenever we encounter a vertex belonging to a component of $G'$, we detour and traverse that component's Eulerian circuit before resuming $C_1$.
    The combined traversal visits every edge of $G$ exactly once and returns to the origin.
  Thus $G$ contains an Eulerian circuit. $\blacksquare$

---

### 3. Fleury's Algorithm for Constructing an Euler Circuit

> **Definition 2.7 (Bridge):**
> A **bridge** (or cut-edge) in a connected graph is an edge whose deletion increases the number of connected components: $\omega(G - e) > \omega(G)$.

#### Fleury's Algorithm:
1. Start at any vertex $v_0$ (if $G$ has two odd vertices, start at one of them).
2. At current vertex $v_i$, choose an incident edge $e = \{v_i, v_{i+1}\}$ according to the **Golden Rule**:
   > *Never cross a bridge unless there is no alternative edge available.*
3. Traverse edge $e$, erase $e$ from $G$, and remove any isolated vertices produced.
4. Set $v_i \leftarrow v_{i+1}$ and repeat until all edges have been traversed."""
            },
            {
                "secNumber": "2.4",
                "title": "The Instant Insanity Puzzle: Graph-Theoretic Multicolored Cubes",
                "content": r"""### 1. The Instant Insanity Puzzle Formulation

The puzzle consists of four cubes, each having its six faces colored with four distinct colors: Red (R), Green (G), Blue (B), and White (W).
The objective is to stack the four cubes in a vertical $1 \times 1 \times 4$ tower such that all four colors appear on each of the four sides of the tower (Front, Back, Left, Right).

A brute-force search over all orientations requires testing:
$$\frac{24^4}{4} = 82,944 \text{ possible stacks}$$
Using graph theory, the solution can be derived analytically in minutes!

---

### 2. Graph-Theoretic Modeling

Construct a multigraph $G$ where:
- The vertices are the four colors: $V = \{R, G, B, W\}$.
- For each cube $i \in \{1, 2, 3, 4\}$, draw three edges labeled $i$ connecting the colors of opposite pairs of faces:
  - Edge 1: (Top, Bottom) colors of cube $i$.
  - Edge 2: (Front, Back) colors of cube $i$.
  - Edge 3: (Left, Right) colors of cube $i$.

The composite multigraph $G$ has $4$ vertices and $4 \times 3 = 12$ edges (3 edges for each label $1, 2, 3, 4$).

---

### 3. The Decomposition Theorem for Instant Insanity

> **Theorem 2.3 (Solution Criterion):**
> A solution to the Instant Insanity puzzle exists if and only if the graph $G$ contains two **edge-disjoint subgraphs** $H_1$ (Front-Back) and $H_2$ (Left-Right) such that:
> 1. Both $H_1$ and $H_2$ are **2-regular** graphs (spanning all 4 color vertices, where every vertex has degree 2).
> 2. Both $H_1$ and $H_2$ contain **exactly one edge with each label** $1, 2, 3, 4$.
> 3. $E(H_1) \cap E(H_2) = \emptyset$ (no shared edges).

#### Why this yields the solution:
- Since each $H_k$ is 2-regular on 4 vertices, it decomposes into either a 4-cycle $C_4$ or two 2-cycles $2 C_2$.
- Orienting the cycles in $H_1$ specifies which face is Front and which is Back for each cube.
- Because every vertex has in-degree 1 and out-degree 1 in the oriented 2-regular subgraph, each color appears exactly once in the Front column and once in the Back column!
- Similarly, $H_2$ independently determines Left and Right faces with all four colors present."""
            },
            {
                "secNumber": "2.5",
                "title": "Hamiltonian Cycles: Dirac's & Ore's Theorems, Closure & TSP",
                "content": r"""### 1. Hamiltonian Paths and Cycles

In stark contrast to Eulerian paths (which visit every *edge*), Hamiltonian paths visit every *vertex*:

> **Definition 2.8 (Hamiltonian Path and Cycle):**
> 1. A **Hamiltonian path** in a graph $G$ is a simple path that visits every vertex of $G$ exactly once.
> 2. A **Hamiltonian cycle** in $G$ is a simple cycle that visits every vertex of $G$ exactly once and returns to the starting vertex.
> 3. A graph $G$ is called **Hamiltonian** if it contains a Hamiltonian cycle.

While determining whether a graph is Eulerian is solvable in linear time $\mathcal{O}(|V| + |E|)$ via degree parity, determining whether a graph is Hamiltonian is famously **NP-complete**.

---

### 2. Ore's Theorem and Dirac's Theorem

Although no simple necessary and sufficient condition exists, powerful degree conditions guarantee Hamiltonicity:

> **Theorem 2.4 (Ore's Theorem, 1960):**
> Let $G$ be a simple graph with $n \ge 3$ vertices.
> If for every pair of distinct non-adjacent vertices $u, v \in V(G)$:
> $$\deg(u) + \deg(v) \ge n$$
> then $G$ is **Hamiltonian**.

> **Corollary 2.1 (Dirac's Theorem, 1952):**
> Let $G$ be a simple graph with $n \ge 3$ vertices.
> If the minimum degree satisfies:
> $$\delta(G) \ge \frac{n}{2}$$
> then $G$ is **Hamiltonian**.

#### Proof of Dirac's Theorem from Ore's Theorem:
If $\delta(G) \ge n/2$, then for any two non-adjacent vertices $u, v$:
$$\deg(u) + \deg(v) \ge \delta(G) + \delta(G) \ge \frac{n}{2} + \frac{n}{2} = n$$
Ore's condition holds immediately, so $G$ is Hamiltonian. $\blacksquare$

---

### 3. The Bondy-Chvátal Closure Theorem

> **Definition 2.9 (Graph Closure):**
> The **closure** of a graph $G$ of order $n$, denoted $[G]$ or $\text{cl}(G)$, is obtained by repeatedly connecting pairs of non-adjacent vertices $u, v$ satisfying $\deg(u) + \deg(v) \ge n$, until no such pairs remain.

> **Theorem 2.5 (Bondy-Chvátal Theorem, 1976):**
> A graph $G$ is Hamiltonian if and only if its closure $\text{cl}(G)$ is Hamiltonian.
> In particular, if $\text{cl}(G) = K_n$ (the complete graph), then $G$ is Hamiltonian.

---

### 4. The Traveling Salesperson Problem (TSP)

> **Definition 2.10 (Traveling Salesperson Problem):**
> Given a complete weighted graph $K_n$ with non-negative edge costs $c(u, v) \ge 0$, find a Hamiltonian cycle that minimizes the total traversal cost:
> $$\min_{C} \sum_{e \in E(C)} c(e)$$
> - **Metric TSP:** Edge weights satisfy the Triangle Inequality: $c(u, w) \le c(u, v) + c(v, w)$.
> - **Christofides-Serdyukov Algorithm:** Provides a polynomial-time 1.5-approximation ratio for Metric TSP using Minimum Spanning Trees and minimum-weight perfect matchings on odd-degree vertices."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Eulerian Classification & Fleury's Trail Construction",
                "statement": r"1. For which values of $n$ is the complete graph $K_n$ Eulerian? For which values is it semi-Eulerian? 2. For which values of $m, n$ is the complete bipartite graph $K_{m, n}$ Eulerian? 3. Given the envelope graph with vertices $\{v_1, v_2, v_3, v_4, v_5\}$ where $v_1, v_2, v_3, v_4$ form a $K_4$ base and $v_5$ is adjacent to $v_3, v_4$, determine the degrees of all vertices, identify if an Euler path exists, and state its starting and ending vertices.",
                "hints": [
                    "Recall that each vertex in $K_n$ has degree $n - 1$. Apply Euler's Theorem.",
                    "In $K_{m,n}$, the $m$ vertices in one part have degree $n$, and the $n$ vertices in the other have degree $m$.",
                    "For the envelope graph, check which vertices have odd degrees."
                ],
                "solution": r"""**Part 1: Eulerian Nature of $K_n$**

In the complete graph $K_n$, every vertex is adjacent to all other $n - 1$ vertices:
$$\deg(v) = n - 1, \quad \forall v \in V(K_n)$$
By Euler's Theorem (Theorem 2.2):
1. **$K_n$ is Eulerian** $\iff$ all degrees are even $\iff n - 1$ is even $\iff n$ is **odd** ($n \ge 3$).
2. **$K_n$ is semi-Eulerian** $\iff$ exactly 2 vertices have odd degree.
   Since all $n$ vertices have the exact same degree $n - 1$, either all $n$ vertices are odd or all are even.
   Thus, exactly two vertices can be odd if and only if $n = 2$ (which is $K_2$, a single edge).
Therefore:
- $K_n$ is Eulerian $\iff n$ is odd ($n = 1, 3, 5, 7, \dots$).
- $K_n$ is semi-Eulerian $\iff n = 2$.

---

**Part 2: Eulerian Nature of Complete Bipartite Graph $K_{m, n}$**

Let $V = V_1 \cup V_2$ with $|V_1| = m$ and $|V_2| = n$.
- Each vertex in $V_1$ has degree $n$.
- Each vertex in $V_2$ has degree $m$.

By Euler's Theorem:
- **Eulerian:** All degrees must be even. Thus $n$ must be even AND $m$ must be even ($m, n \in \{2, 4, 6, \dots\}$).
- **Semi-Eulerian:** Exactly 2 vertices must have odd degree.
  - If $m = 2$ and $n$ is odd: The 2 vertices in $V_1$ have odd degree $n$, while the $n$ vertices in $V_2$ have even degree $m = 2$. This has exactly 2 odd vertices!
  - By symmetry, if $n = 2$ and $m$ is odd: Exactly 2 odd vertices.
Therefore:
- $K_{m, n}$ is Eulerian $\iff$ both $m$ and $n$ are even.
- $K_{m, n}$ is semi-Eulerian $\iff (m = 2 \text{ and } n \text{ is odd}) \text{ or } (n = 2 \text{ and } m \text{ is odd})$.

---

**Part 3: Analysis of the Envelope Graph**

Let the base vertices be $\{v_1, v_2, v_3, v_4\}$ forming $K_4$, and let the roof peak $v_5$ be connected to $v_3, v_4$.
Compute vertex degrees:
- $v_1, v_2$: Incident to 3 edges each in $K_4 \implies \deg(v_1) = 3, \; \deg(v_2) = 3$ (both ODD).
- $v_3, v_4$: Incident to 3 edges in $K_4$ plus 1 edge to $v_5 \implies \deg(v_3) = 4, \; \deg(v_4) = 4$ (both EVEN).
- $v_5$: Incident to $v_3$ and $v_4 \implies \deg(v_5) = 2$ (EVEN).

Summary of degrees:
$$\deg(v_1) = 3, \quad \deg(v_2) = 3, \quad \deg(v_3) = 4, \quad \deg(v_4) = 4, \quad \deg(v_5) = 2$$
The graph has **exactly two odd-degree vertices**: $v_1$ and $v_2$.
By Euler's Theorem (Part 2), an open Eulerian trail **exists**, and it must **start at $v_1$ and terminate at $v_2$** (or vice versa). $\blacksquare$"""
            },
            {
                "tier": "Advanced",
                "title": "Bipartite Hamiltonicity Obstruction & Instant Insanity Solution",
                "statement": r"1. Let $G = (V_1 \cup V_2, E)$ be a bipartite graph. Prove that if $G$ is Hamiltonian, then $|V_1| = |V_2|$. Deduce that any bipartite graph on an odd number of vertices cannot be Hamiltonian. 2. In a 3-dimensional cube graph $Q_3$, determine whether $Q_3$ is Eulerian, semi-Eulerian, or Hamiltonian.",
                "hints": [
                    "For Part 1, let $C = (v_1, v_2, \\dots, v_{2k}, v_1)$ be a Hamiltonian cycle. What happens to the bipartition sets as you step along the cycle?",
                    "For Part 2, remember that $Q_3$ has $2^3 = 8$ vertices and is 3-regular."
                ],
                "solution": r"""**Part 1: Proof that Hamiltonian Bipartite Graphs have $|V_1| = |V_2|$**

Let $G = (V_1 \cup V_2, E)$ be a bipartite graph, where $V_1 \cap V_2 = \emptyset$, and every edge connects a vertex in $V_1$ to a vertex in $V_2$.
Suppose $G$ contains a Hamiltonian cycle $C$.
Let $C = (u_1, u_2, u_3, \dots, u_n, u_1)$ be the sequence of vertices in the cycle, where $n = |V(G)|$.
Without loss of generality, let $u_1 \in V_1$.
- Since $G$ is bipartite, $u_1 \in V_1 \implies u_2 \in V_2$.
- $u_2 \in V_2 \implies u_3 \in V_1$.
- In general, for every step $i$:
  $$u_i \in V_1 \iff i \text{ is odd}$$
  $$u_i \in V_2 \iff i \text{ is even}$$
Because $C$ is a closed cycle, the edge $\{u_n, u_1\}$ must connect $u_n$ to $u_1 \in V_1$.
By the bipartite property, this requires:
$$u_n \in V_2$$
Thus $n$ must be an **even integer** ($n = 2k$).
Since the cycle alternates strictly between $V_1$ and $V_2$ at every step:
- The vertices in $V_1$ are precisely the odd-indexed vertices: $\{u_1, u_3, u_5, \dots, u_{2k-1}\}$. Total count $= k$.
- The vertices in $V_2$ are precisely the even-indexed vertices: $\{u_2, u_4, u_6, \dots, u_{2k}\}$. Total count $= k$.
Therefore:
$$|V_1| = k = |V_2|$$
This proves that $|V_1| = |V_2|$.

**Corollary for Odd Number of Vertices:**
If $G$ is a bipartite graph with an odd number of vertices $|V| = 2m + 1$:
$$|V_1| + |V_2| = 2m + 1$$
Because $|V_1| + |V_2|$ is odd, $|V_1|$ and $|V_2|$ cannot be equal ($|V_1| \ne |V_2|$).
Therefore, no bipartite graph on an odd number of vertices can contain a Hamiltonian cycle. $\blacksquare$

---

**Part 2: Traversal Properties of the 3-Cube $Q_3$**

The 3-cube $Q_3$ has:
- Order: $|V(Q_3)| = 2^3 = 8$ vertices.
- Regularity: $Q_3$ is 3-regular, so $\deg(v) = 3$ for all $v \in V(Q_3)$.
- Edges: $|E(Q_3)| = \frac{8 \times 3}{2} = 12$.

1. **Eulerian Analysis:**
   Every vertex has degree $3$, which is an **odd integer**.
   Since all 8 vertices have odd degrees:
   - $Q_3$ is **NOT Eulerian** (it has odd vertices).
   - $Q_3$ is **NOT semi-Eulerian** (it has 8 odd vertices, whereas semi-Eulerian requires exactly 2).
2. **Hamiltonian Analysis:**
   Notice that $Q_3$ is bipartite with $|V_1| = 4$ (strings with even Hamming weight: $000, 011, 101, 110$) and $|V_2| = 4$ (strings with odd Hamming weight: $001, 010, 100, 111$).
   We can construct an explicit Gray code cycle traversing all 8 vertices:
   $$C = (000 \to 001 \to 011 \to 010 \to 110 \to 111 \to 101 \to 100 \to 000)$$
   Each consecutive pair differs by exactly 1 bit, representing a valid edge in $Q_3$.
   This cycle visits all 8 vertices and returns to $000$.
   Therefore, $Q_3$ is **Hamiltonian**. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Complete Formal Proof of Ore's Theorem on Hamiltonian Cycles",
                "statement": r"Let $G$ be a simple graph on $n \ge 3$ vertices. Provide a rigorous, unskipped proof of Ore's Theorem: If $\deg(u) + \deg(v) \ge n$ for every pair of distinct non-adjacent vertices $u, v \in V(G)$, then $G$ contains a Hamiltonian cycle.",
                "hints": [
                    "Assume for contradiction that the theorem is false. Consider a maximal counterexample $G$ (a non-Hamiltonian graph on $n$ vertices satisfying Ore's condition to which adding any edge creates a Hamiltonian cycle).",
                    "In this maximal graph, adding an edge $\{u, v\}$ must complete a Hamiltonian path $P = (u = v_1, v_2, \\dots, v_n = v)$.",
                    "Use the Pigeonhole Principle on the sets $S = \\{i : v_1 \\sim v_{i+1}\\}$ and $T = \\{i : v_i \\sim v_n\\}$."
                ],
                "solution": r"""**Complete Proof of Ore's Theorem (Theorem 2.4)**

Let $G$ be a simple graph on $n \ge 3$ vertices satisfying Ore's condition:
$$\deg(u) + \deg(v) \ge n, \quad \forall u, v \in V(G) \text{ with } \{u, v\} \notin E(G)$$
Assume for contradiction that $G$ is **NOT Hamiltonian**.

---

**Step 1: The Maximal Non-Hamiltonian Graph Construction**
If adding edges to $G$ preserves the non-Hamiltonian property, add edges one by one until adding any additional edge produces a Hamiltonian graph.
Let $G^*$ be such a **maximal non-Hamiltonian graph** on the same vertex set $V$.
Notice:
1. $G^*$ still satisfies Ore's condition (adding edges only increases vertex degrees).
2. $G^*$ is not complete ($G^* \ne K_n$, since $K_n$ is trivially Hamiltonian for $n \ge 3$).
3. Therefore, there exist two non-adjacent vertices $u, v \in V(G^*)$ with $\{u, v\} \notin E(G^*)$.
4. By the maximality of $G^*$, the graph $G^* + \{u, v\}$ obtained by adding the edge $\{u, v\}$ **must contain a Hamiltonian cycle**!

---

**Step 2: Existence of a Hamiltonian Path Connecting $u$ and $v$**
Let $C$ be a Hamiltonian cycle in $G^* + \{u, v\}$.
The cycle $C$ must use the newly added edge $\{u, v\}$ (otherwise $C$ would already exist in $G^*$, contradicting that $G^*$ is non-Hamiltonian).
Erasing the edge $\{u, v\}$ from $C$ yields a **Hamiltonian path** in $G^*$ connecting $u$ and $v$:
$$P = (v_1, v_2, v_3, \dots, v_n)$$
where $v_1 = u$ and $v_n = v$.
Since $u \not\sim v$ in $G^*$, the endpoints $v_1$ and $v_n$ are non-adjacent in $G^*$.

---

**Step 3: Index Set Partition and Pigeonhole Analysis**
Consider the indices along the path $P$: $\{1, 2, \dots, n-1\}$.
Define two subsets of indices:
$$S = \{ i \in \{1, 2, \dots, n-1\} : \{v_1, v_{i+1}\} \in E(G^*) \}$$
$$T = \{ i \in \{1, 2, \dots, n-1\} : \{v_i, v_n\} \in E(G^*) \}$$

Let us compute the cardinalities of $S$ and $T$:
- Every neighbor of $v_1$ along the path has the form $v_{i+1}$ for some $i \in \{1, \dots, n-1\}$ (since $v_1$ cannot be adjacent to itself or to $v_n$).
  Therefore:
  $$|S| = \deg_{G^*}(v_1)$$
- Every neighbor of $v_n$ along the path has the form $v_i$ for some $i \in \{1, \dots, n-1\}$.
  Therefore:
  $$|T| = \deg_{G^*}(v_n)$$

Now compute the sum of cardinalities:
$$|S| + |T| = \deg_{G^*}(v_1) + \deg_{G^*}(v_n)$$
Since $v_1$ and $v_n$ are non-adjacent in $G^*$, Ore's condition gives:
$$|S| + |T| \ge n$$

Notice that both $S$ and $T$ are subsets of the identical index set:
$$S, T \subseteq \{1, 2, \dots, n - 1\}$$
The total number of available elements in this index set is:
$$|\{1, 2, \dots, n - 1\}| = n - 1$$
By the **Pigeonhole Principle**:
$$|S \cap T| = |S| + |T| - |S \cup T| \ge n - (n - 1) = 1$$
Therefore, $S$ and $T$ cannot be disjoint:
$$S \cap T \ne \emptyset$$

---

**Step 4: Construction of the Hamiltonian Cycle in $G^*$**
Since $S \cap T \ne \emptyset$, there exists an index $i \in \{1, 2, \dots, n - 1\}$ such that $i \in S$ and $i \in T$.
By definition of $S$ and $T$:
$$\{v_1, v_{i+1}\} \in E(G^*) \quad \text{and} \quad \{v_i, v_n\} \in E(G^*)$$

Now construct the following cycle in $G^*$:
1. Start at $v_1$, travel along the path to $v_i$: $(v_1, v_2, \dots, v_i)$.
2. Take the edge $\{v_i, v_n\}$ to jump to $v_n$.
3. Travel backward along the path from $v_n$ to $v_{i+1}$: $(v_n, v_{n-1}, \dots, v_{i+1})$.
4. Take the edge $\{v_{i+1}, v_1\}$ to return to $v_1$!

Writing this closed sequence:
$$C^* = (v_1, v_2, \dots, v_i, v_n, v_{n-1}, \dots, v_{i+1}, v_1)$$
Let us verify this cycle:
- It uses only edges belonging to $E(G^*)$:
  - Path segments $(v_1 \to v_i)$ and $(v_{i+1} \to v_n)$ are parts of the original path $P \subset G^*$.
  - The cross-edges $\{v_i, v_n\}$ and $\{v_{i+1}, v_1\}$ both belong to $G^*$ by choice of $i \in S \cap T$.
- It visits every single vertex in $\{v_1, \dots, v_n\} = V(G^*)$ exactly once before closing!
Therefore, $C^*$ is a **Hamiltonian cycle in $G^*$**!

This directly contradicts the fact that $G^*$ is non-Hamiltonian!
Hence, our assumption that $G$ is not Hamiltonian was false.
Therefore, $G$ must be Hamiltonian. $\blacksquare$"""
            }
        ]
    }
    return u2

if __name__ == "__main__":
    u = get_unit2()
    print("Unit 2 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
