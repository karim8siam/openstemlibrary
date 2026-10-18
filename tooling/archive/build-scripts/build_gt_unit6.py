# -*- coding: utf-8 -*-
"""
build_gt_unit6.py
Constructs Unit 6: Directed Graphs, Tournaments, DAGs & Topological Sorting
"""

def get_unit6():
    u6 = {
        "number": 6,
        "title": "Directed Graphs, Tournaments, DAGs & Topological Sorting",
        "leadSummary": "Comprehensive theory of directed graphs (digraphs): in-degree and out-degree balance, digraph connectedness (weak, unilateral, strong), strongly connected components (SCCs) and Tarjan/Kosaraju algorithms, Eulerian digraphs, tournaments and Landau's theorem, Directed Acyclic Graphs (DAGs), decyclization, and Kahn's topological sorting algorithm.",
        "simulations": ["sim_gt_digraph_dag"],
        "sections": [
            {
                "secNumber": "6.1",
                "title": "Digraph Axioms, In/Out-Degrees & Directed Handshaking",
                "content": r"""### 1. Axiomatic Definition of a Directed Graph (Digraph)

A directed graph introduces orientation to relationships, reflecting asymmetry such as one-way roads, prerequisite structures, or state transitions.

> **Definition 6.1 (Directed Graph / Digraph):**
> A **directed graph** (or digraph) $D = (V, E)$ consists of:
> 1. A non-empty set of vertices $V(D) = \{v_1, \dots, v_n\}$.
> 2. A set of **directed edges** (or arcs) $E(D) = \{e_1, \dots, e_m\}$, where each arc $e$ is an **ordered pair** of vertices:
>    $$e = (u, v) \in V \times V$$
> Vertex $u$ is called the **initial vertex** (or tail), and $v$ is called the **terminal vertex** (or head). We say $e$ is directed from $u$ to $v$.

- A **self-loop** in a digraph is an arc of the form $(u, u)$.
- A **simple digraph** contains no self-loops and no duplicate directed edges $(u, v)$ with identical orientation.
- The **underlying undirected graph** of $D$, denoted $U(D)$, is obtained by replacing each directed arc $(u, v)$ with an undirected edge $\{u, v\}$ and consolidating multiple edges.

---

### 2. In-Degrees, Out-Degrees & The Digraph Handshaking Theorem

> **Definition 6.2 (In-Degree and Out-Degree):**
> For any vertex $v \in V(D)$:
> 1. The **out-degree** $d^+(v)$ (or $\deg^+(v)$) is the number of arcs directed away from $v$:
>    $$d^+(v) = |\{ u \in V : (v, u) \in E \}|$$
> 2. The **in-degree** $d^-(v)$ (or $\deg^-(v)$) is the number of arcs directed into $v$:
>    $$d^-(v) = |\{ u \in V : (u, v) \in E \}|$$
> 3. The **total degree** of $v$ is $\deg(v) = d^+(v) + d^-(v)$.
> 4. A vertex with $d^-(v) = 0$ is called a **source**; a vertex with $d^+(v) = 0$ is called a **sink**.

> **Theorem 6.1 (The Directed Handshaking Theorem):**
> In any directed graph $D = (V, E)$, the sum of the out-degrees equals the sum of the in-degrees, and both equal the total number of arcs:
> $$\sum_{v \in V} d^+(v) = \sum_{v \in V} d^-(v) = |E|$$

#### Proof:
Every directed arc $e = (u, v) \in E$ has exactly one initial vertex $u$ and exactly one terminal vertex $v$.
Therefore, each arc contributes exactly 1 to $\sum d^+(v)$ (at its tail) and exactly 1 to $\sum d^-(v)$ (at its head).
Summing across all $m = |E|$ arcs proves the identity. $\blacksquare$"""
            },
            {
                "secNumber": "6.2",
                "title": "Connectedness Levels & Strongly Connected Components (SCCs)",
                "content": r"""### 1. Hierarchy of Connectedness in Digraphs

Because edges in a digraph can only be traversed in the forward direction, connectivity is nuanced into three hierarchical levels:

> **Definition 6.3 (Connectedness Categories):**
> Let $D = (V, E)$ be a digraph.
> 1. **Weakly Connected:** $D$ is weakly connected if its underlying undirected graph $U(D)$ is connected.
> 2. **Unilaterally Connected:** $D$ is unilaterally connected if for every pair of distinct vertices $u, v \in V$, there exists a directed path from $u$ to $v$ **OR** a directed path from $v$ to $u$.
> 3. **Strongly Connected (Strong):** $D$ is strongly connected if for every pair of distinct vertices $u, v \in V$, there exists a directed path from $u$ to $v$ **AND** a directed path from $v$ to $u$.

$$\text{Strongly Connected} \implies \text{Unilaterally Connected} \implies \text{Weakly Connected}$$
None of the reverse implications hold in general.

---

### 2. Strongly Connected Components (SCCs)

> **Definition 6.4 (SCC):**
> A **strongly connected component (SCC)** of a digraph $D$ is a maximal strongly connected subgraph of $D$.

> **Theorem 6.2 (Strong Connectivity Equivalence Relation):**
> The relation $u \approx v \iff (u \leadsto v \text{ and } v \leadsto u)$ is an equivalence relation on $V(D)$.
> The equivalence classes are the vertex sets of the strongly connected components.

#### The Condensation Digraph:
Shrinking each SCC into a single super-vertex yields the **condensation** of $D$, denoted $D^*$.
The condensation $D^*$ is **always a Directed Acyclic Graph (DAG)**."""
            },
            {
                "secNumber": "6.3",
                "title": "Eulerian Digraphs & De Bruijn Sequences",
                "content": r"""### 1. Characterization of Eulerian Digraphs

> **Definition 6.5 (Eulerian Digraph):**
> A directed graph $D$ is **Eulerian** if it contains a closed directed trail that traverses **every directed arc of $D$ exactly once** (a directed Euler circuit).

> **Theorem 6.3 (Eulerian Digraph Theorem):**
> A weakly connected digraph $D$ is Eulerian if and only if it is **balanced** at every vertex:
> $$d^+(v) = d^-(v), \quad \forall v \in V(D)$$

#### Proof:
- $(\implies)$ In any directed Euler circuit, each entry into $v$ via an incoming arc must be paired with an immediate departure via an outgoing arc. Thus $d^+(v) = d^-(v)$.
- $(\impliedby)$ If $d^+(v) = d^-(v) \ge 1$ everywhere, start at any vertex $v_0$ and follow outgoing arcs. Since out-degree equals in-degree, we can never get stuck until returning to $v_0$, producing a directed cycle. Removing this cycle preserves balance. Splicing components together as in Theorem 2.2 produces an Euler circuit. $\blacksquare$

---

### 2. De Bruijn Sequences

A **De Bruijn sequence** $B(k, n)$ of order $n$ on an alphabet of size $k$ is a cyclic sequence of length $k^n$ in which every possible substring of length $n$ appears exactly once as a contiguous block!
De Bruijn sequences are constructed as Eulerian circuits in the **De Bruijn graph**, where vertices are strings of length $n - 1$ and directed edges represent string overlaps of length $n$."""
            },
            {
                "secNumber": "6.4",
                "title": "Tournaments, Rédei's Theorem & Landau's Score Theorem",
                "content": r"""### 1. Definition of Tournaments

> **Definition 6.6 (Tournament):**
> A **tournament** $T_n$ is an orientation of a complete graph $K_n$.
> That is, for every pair of distinct vertices $u, v \in V(T_n)$, there is **exactly one** directed arc between them: either $(u, v) \in E$ or $(v, u) \in E$, but not both.
> A tournament models a round-robin competition where every player plays every other player and ties are impossible.

---

### 2. Rédei's Theorem on Hamiltonian Paths

> **Theorem 6.4 (Rédei's Theorem, 1934):**
> Every tournament contains a **directed Hamiltonian path**.

#### Complete Formal Proof (by induction on $n$):
- **Base Case ($n = 1, 2$):** $T_1$ is a single vertex. $T_2$ has one arc $(u, v)$, which is a path of length 1 visiting both vertices. Holds.
- **Inductive Step:** Assume every tournament on $n - 1$ vertices contains a directed Hamiltonian path.
  Let $T$ be a tournament on $n$ vertices.
  Choose any vertex $v \in V(T)$, and consider the sub-tournament $T' = T - v$ on $n - 1$ vertices.
  By the induction hypothesis, $T'$ contains a directed Hamiltonian path:
  $$P = (u_1, u_2, \dots, u_{n-1})$$
  Now consider the position of vertex $v$ relative to path $P$:
  - **Case 1:** $(v, u_1) \in E(T)$.
    Then $(v, u_1, u_2, \dots, u_{n-1})$ is a directed Hamiltonian path in $T$.
  - **Case 2:** $(u_{n-1}, v) \in E(T)$.
    Then $(u_1, u_2, \dots, u_{n-1}, v)$ is a directed Hamiltonian path in $T$.
  - **Case 3:** Neither Case 1 nor Case 2 holds.
    Then $(u_1, v) \in E(T)$ and $(v, u_{n-1}) \in E(T)$.
    As we travel along $P$ from $u_1$ to $u_{n-1}$, the arcs from the path vertices to $v$ start by pointing toward $v$ and end by pointing away from $v$.
    Therefore, there must exist an index $i \in \{1, 2, \dots, n - 2\}$ such that:
    $$(u_i, v) \in E(T) \quad \text{and} \quad (v, u_{i+1}) \in E(T)$$
    We can insert $v$ directly between $u_i$ and $u_{i+1}$ on the path:
    $$P_{\text{new}} = (u_1, \dots, u_i, v, u_{i+1}, \dots, u_{n-1})$$
    This is a valid directed path visiting all $n$ vertices of $T$.
Thus every tournament has a directed Hamiltonian path. $\blacksquare$

---

### 3. Landau's Theorem on Tournament Score Sequences

> **Definition 6.7 (Score Sequence):**
> The **score sequence** of a tournament $T_n$ is the sequence of out-degrees sorted in non-decreasing order: $s = (s_1 \le s_2 \le \dots \le s_n)$.

> **Theorem 6.5 (Landau's Theorem, 1953):**
> A non-decreasing sequence of non-negative integers $(s_1, s_2, \dots, s_n)$ is the score sequence of a tournament on $n$ vertices if and only if:
> 1. $\sum_{i=1}^k s_i \ge \binom{k}{2}$ for all $1 \le k \le n - 1$.
> 2. $\sum_{i=1}^n s_i = \binom{n}{2}$."""
            },
            {
                "secNumber": "6.5",
                "title": "Directed Acyclic Graphs (DAGs), Decyclization & Topological Sorting",
                "content": r"""### 1. Directed Acyclic Graphs (DAGs)

> **Definition 6.8 (DAG):**
> A **Directed Acyclic Graph (DAG)** is a directed graph containing **no directed cycles**.

DAGs model dependency networks, task scheduling, compilation order, and causal relationships.

> **Lemma 6.1 (Every Finite DAG Contains a Source and a Sink):**
> Every finite DAG contains at least one vertex with in-degree 0 (a source) and at least one vertex with out-degree 0 (a sink).

#### Proof:
Pick any vertex $v_1 \in V$. If $d^+(v_1) = 0$, $v_1$ is a sink.
Otherwise, choose an outgoing arc $(v_1, v_2)$. If $d^+(v_2) = 0$, $v_2$ is a sink.
Repeat this process. Since the graph is finite and contains no directed cycles, we can never repeat a vertex.
Thus the path must eventually terminate at some vertex $v_k$ with no outgoing arcs ($d^+(v_k) = 0$).
Hence $v_k$ is a sink. A symmetric backwards search establishes the existence of a source. $\blacksquare$

---

### 2. Topological Sorting

> **Definition 6.9 (Topological Sort):**
> A **topological sort** (or topological ordering) of a directed graph $D = (V, E)$ is a linear ordering of its vertices $v_{\pi(1)}, v_{\pi(2)}, \dots, v_{\pi(n)}$ such that for every directed arc $(u, v) \in E$, $u$ appears before $v$ in the ordering:
> $$(u, v) \in E \implies \pi(u) < \pi(v)$$

> **Theorem 6.6 (Topological Sort Existence Theorem):**
> A directed graph $D$ admits a topological sort if and only if $D$ is a **DAG**.

#### Kahn's Algorithm for Topological Sort ($\mathcal{O}(|V| + |E|)$):
1. Compute the in-degree $d^-(v)$ for every vertex $v \in V$.
2. Initialize a queue $Q$ with all vertices having $d^-(v) = 0$ (all sources).
3. Initialize an empty list $L = []$.
4. While $Q$ is not empty:
   - Dequeue a vertex $u$ from $Q$.
   - Append $u$ to $L$.
   - For each outgoing neighbor $v$ of $u$ (arc $(u, v) \in E$):
     - Decrement $d^-(v) \leftarrow d^-(v) - 1$.
     - If $d^-(v) == 0$, enqueue $v$ into $Q$.
5. If $|L| = |V|$, $L$ is a valid topological ordering!
   If $|L| < |V|$, the graph contains a directed cycle (not a DAG)."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Connectivity Level Classification & Eulerian Digraph Verification",
                "statement": r"1. Consider a digraph on 4 vertices with arcs: $E = \{(1, 2), (2, 3), (3, 4), (4, 2)\}$. Determine whether this digraph is weakly connected, unilaterally connected, or strongly connected. 2. A directed graph $D$ has in-degrees $d^- = (2, 1, 3, 2)$ for vertices $v_1, v_2, v_3, v_4$. If $D$ is Eulerian, determine the out-degrees of all vertices and the total number of arcs.",
                "hints": [
                    "For Part 1, check whether there is a path from 1 to 2, 3, 4, and whether there is any path from 2 back to 1.",
                    "For Part 2, recall Theorem 6.3: a weakly connected digraph is Eulerian if and only if $d^+(v) = d^-(v)$ for every vertex."
                ],
                "solution": r"""**Part 1: Connectivity Analysis**

Vertices: $\{1, 2, 3, 4\}$.
Arcs: $(1, 2), (2, 3), (3, 4), (4, 2)$.

Let us test the connectivity categories:
1. **Is it Weakly Connected?**
   The underlying undirected graph has edges $\{1, 2\}, \{2, 3\}, \{3, 4\}$.
   Vertices $2, 3, 4$ form a triangle, and vertex 1 is connected to 2.
   The underlying graph is connected.
   Therefore, $D$ is **weakly connected**.
2. **Is it Unilaterally Connected?**
   We check if for every pair $\{u, v\}$, there is a directed path $u \leadsto v$ OR $v \leadsto u$:
   - Between 1 and 2: path $1 \to 2$.
   - Between 1 and 3: path $1 \to 2 \to 3$.
   - Between 1 and 4: path $1 \to 2 \to 3 \to 4$.
   - Between 2 and 3: path $2 \to 3$.
   - Between 2 and 4: path $2 \to 3 \to 4$.
   - Between 3 and 4: path $3 \to 4$.
   For every pair of distinct vertices, there exists a directed path in at least one direction!
   Therefore, $D$ is **unilaterally connected**.
3. **Is it Strongly Connected?**
   Vertex 1 has in-degree $d^-(1) = 0$ (no arcs enter vertex 1).
   Therefore, no vertex in $\{2, 3, 4\}$ can reach vertex 1!
   There is no path from 2 to 1, no path from 3 to 1, and no path from 4 to 1.
   Therefore, $D$ is **NOT strongly connected**.

**Conclusion:** The digraph is **unilaterally connected** (and weakly connected), but not strongly connected.

---

**Part 2: Eulerian Digraph In/Out-Degrees**

We are given the in-degrees:
$$d^-(v_1) = 2, \quad d^-(v_2) = 1, \quad d^-(v_3) = 3, \quad d^-(v_4) = 2$$
By Theorem 6.3 (Eulerian Digraph Theorem), a digraph is Eulerian if and only if it is weakly connected and **in-degree equals out-degree for every vertex**:
$$d^+(v_i) = d^-(v_i), \quad \forall i \in \{1, 2, 3, 4\}$$
Therefore, the out-degrees must be:
$$d^+(v_1) = 2, \quad d^+(v_2) = 1, \quad d^+(v_3) = 3, \quad d^+(v_4) = 2$$
The total number of directed arcs is given by the Directed Handshaking Theorem (Theorem 6.1):
$$|E| = \sum_{i=1}^4 d^-(v_i) = 2 + 1 + 3 + 2 = 8 \quad \blacksquare$$"""
            },
            {
                "tier": "Advanced",
                "title": "Kahn's Topological Sort Execution & Tournament Path Construction",
                "statement": r"1. Consider the task dependency DAG with vertices $A, B, C, D, E, F$ and directed arcs: $(A, B), (A, C), (B, D), (C, D), (C, E), (D, F), (E, F)$. Execute Kahn's algorithm step-by-step to find a valid topological ordering. 2. A tournament $T_4$ has vertices $\{1, 2, 3, 4\}$ and arcs: $(1, 2), (2, 3), (3, 1), (1, 4), (2, 4), (4, 3)$. Find an explicit directed Hamiltonian path in $T_4$.",
                "hints": [
                    "For Part 1, compute initial in-degrees for all tasks, enqueue sources, and update degrees as vertices are output.",
                    "For Part 2, check Rédei's theorem by tracing paths through the vertices."
                ],
                "solution": r"""**Part 1: Kahn's Algorithm on Dependency DAG**

Vertices: $\{A, B, C, D, E, F\}$.
Arcs: $(A, B), (A, C), (B, D), (C, D), (C, E), (D, F), (E, F)$.

Compute initial in-degrees $d^-$:
- $d^-(A) = 0$
- $d^-(B) = 1$ (from $A$)
- $d^-(C) = 1$ (from $A$)
- $d^-(D) = 2$ (from $B, C$)
- $d^-(E) = 1$ (from $C$)
- $d^-(F) = 2$ (from $D, E$)

**Step-by-Step Execution:**
1. **Queue initialization:** $Q = [A]$ (since $d^-(A) = 0$). Output list $L = []$.
2. **Dequeue $A$:**
   - Append $A$ to $L$: $L = [A]$.
   - Outgoing arcs from $A$: $(A, B)$ and $(A, C)$.
   - Decrement: $d^-(B) = 1 - 1 = 0 \implies$ Enqueue $B$.
   - Decrement: $d^-(C) = 1 - 1 = 0 \implies$ Enqueue $C$.
   - Queue: $Q = [B, C]$.
3. **Dequeue $B$:**
   - Append $B$ to $L$: $L = [A, B]$.
   - Outgoing arc from $B$: $(B, D)$.
   - Decrement: $d^-(D) = 2 - 1 = 1$. (Not 0, do not enqueue).
   - Queue: $Q = [C]$.
4. **Dequeue $C$:**
   - Append $C$ to $L$: $L = [A, B, C]$.
   - Outgoing arcs from $C$: $(C, D)$ and $(C, E)$.
   - Decrement: $d^-(D) = 1 - 1 = 0 \implies$ Enqueue $D$.
   - Decrement: $d^-(E) = 1 - 1 = 0 \implies$ Enqueue $E$.
   - Queue: $Q = [D, E]$.
5. **Dequeue $D$:**
   - Append $D$ to $L$: $L = [A, B, C, D]$.
   - Outgoing arc from $D$: $(D, F)$.
   - Decrement: $d^-(F) = 2 - 1 = 1$.
   - Queue: $Q = [E]$.
6. **Dequeue $E$:**
   - Append $E$ to $L$: $L = [A, B, C, D, E]$.
   - Outgoing arc from $E$: $(E, F)$.
   - Decrement: $d^-(F) = 1 - 1 = 0 \implies$ Enqueue $F$.
   - Queue: $Q = [F]$.
7. **Dequeue $F$:**
   - Append $F$ to $L$: $L = [A, B, C, D, E, F]$.
   - No outgoing arcs.
   - Queue empty.

All 6 vertices are ordered:
$$\text{Topological Order: } A \to B \to C \to D \to E \to F$$
*(Another valid order is $A \to C \to B \to D \to E \to F$ depending on queue tie-breaking).*

---

**Part 2: Finding a Hamiltonian Path in $T_4$**

Vertices: $\{1, 2, 3, 4\}$.
Arcs: $(1, 2), (2, 3), (3, 1), (1, 4), (2, 4), (4, 3)$.
Notice that $\{1, 2, 3\}$ forms a directed cycle: $1 \to 2 \to 3 \to 1$.
We also have:
- Arc from 2 to 4: $(2, 4)$.
- Arc from 4 to 3: $(4, 3)$.
- Arc from 3 to 1: $(3, 1)$.

Construct the path:
$$1 \xrightarrow{(1, 2)} 2 \xrightarrow{(2, 4)} 4 \xrightarrow{(4, 3)} 3$$
Let us check each step:
1. $(1, 2) \in E$ (given).
2. $(2, 4) \in E$ (given).
3. $(4, 3) \in E$ (given).
This directed path visits vertices $(1, 2, 4, 3)$—all 4 vertices of $T_4$ exactly once!
Therefore, $P = (1, 2, 4, 3)$ is a valid directed Hamiltonian path in $T_4$. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Complete Formal Proof of Landau's Theorem on Tournament Scores",
                "statement": r"Provide a complete, mathematically rigorous proof of Landau's Theorem (Theorem 6.5): A non-decreasing sequence of non-negative integers $s_1 \le s_2 \le \dots \le s_n$ is the score sequence of a tournament on $n$ vertices if and only if $\sum_{i=1}^k s_i \ge \binom{k}{2}$ for all $1 \le k \le n - 1$, and $\sum_{i=1}^n s_i = \binom{n}{2}$.",
                "hints": [
                    "For the necessity $(\\implies)$ direction, consider any subset of $k$ vertices. How many total matches must be played among these $k$ vertices?",
                    "For the sufficiency $(\\impliedby)$ direction, use a network flow argument or a majorization/transshipment minimum contradiction argument."
                ],
                "solution": r"""**Complete Proof of Landau's Theorem (Theorem 6.5)**

Let $s = (s_1 \le s_2 \le \dots \le s_n)$ be a sequence of non-negative integers.

---

**Part 1: Proof of Necessity $(\implies)$**
Suppose $s$ is the score sequence of a tournament $T$ with vertices $V = \{v_1, v_2, \dots, v_n\}$ labeled such that $d^+(v_i) = s_i$.

1. **Total Edge Identity ($k = n$):**
   In a tournament on $n$ vertices, there is exactly one directed arc between every pair of vertices.
   The total number of edges is:
   $$|E| = \binom{n}{2}$$
   By the Directed Handshaking Theorem (Theorem 6.1):
   $$\sum_{i=1}^n s_i = \sum_{i=1}^n d^+(v_i) = |E| = \binom{n}{2}$$
   Condition (2) is verified!

2. **Partial Sum Inequality ($1 \le k \le n - 1$):**
   Let $K = \{v_1, v_2, \dots, v_k\}$ be the set of the first $k$ vertices (having the smallest scores).
   Consider the sub-tournament $T[K]$ induced by these $k$ vertices.
   Inside $T[K]$, there are $\binom{k}{2}$ directed arcs between pairs of vertices in $K$.
   For each arc in $T[K]$, its tail lies in $K$, so it contributes to the out-degree of some vertex in $K$.
   In addition, vertices in $K$ may have outgoing arcs pointing to vertices outside $K$ (in $V \setminus K$).
   Therefore:
   $$\sum_{i=1}^k s_i = \sum_{v \in K} d^+(v) = (\text{arcs within } K) + (\text{arcs from } K \text{ to } V \setminus K) = \binom{k}{2} + |E(K, V \setminus K)|$$
   Since the number of arcs pointing from $K$ to $V \setminus K$ is non-negative ($|E(K, V \setminus K)| \ge 0$):
   $$\sum_{i=1}^k s_i \ge \binom{k}{2}$$
   This holds for all $k \in \{1, 2, \dots, n - 1\}$.
Hence the conditions are strictly necessary.

---

**Part 2: Proof of Sufficiency $(\impliedby)$**
Assume $s = (s_1 \le s_2 \le \dots \le s_n)$ satisfies:
(1) $\sum_{i=1}^k s_i \ge \binom{k}{2}$ for all $1 \le k \le n - 1$.
(2) $\sum_{i=1}^n s_i = \binom{n}{2}$.

We construct a tournament $T$ realizing $s$ using a **Max-Flow Network Construction**:
Construct a flow network $N = (V^*, E^*)$ with:
- Source $S$ and sink $T^*$.
- A middle layer of $\binom{n}{2}$ match nodes $M = \{ (i, j) : 1 \le i < j \le n \}$.
- A layer of $n$ player nodes $P = \{ p_1, p_2, \dots, p_n \}$.

**Edge Capacities:**
1. Connect source $S$ to each match node $(i, j)$ with capacity $c(S, (i, j)) = 1$.
   (Total source capacity $= \binom{n}{2}$).
2. Connect each match node $(i, j)$ to player $p_i$ and player $p_j$, each with capacity $1$.
   (Directing flow from $(i, j)$ to $p_i$ means player $i$ beats player $j$).
3. Connect each player node $p_i$ to sink $T^*$ with capacity $c(p_i, T^*) = s_i$.
   (Total sink capacity $= \sum_{i=1}^n s_i = \binom{n}{2}$).

A valid tournament with score sequence $s$ exists if and only if there is a feasible flow of value:
$$F = \binom{n}{2}$$
By the Max-Flow Min-Cut Theorem (Theorem 8.5), a maximum flow of value $\binom{n}{2}$ exists if and only if **every cut separating $S$ from $T^*$ has capacity $\ge \binom{n}{2}$**.

Consider any cut $(A, B)$ with $S \in A$ and $T^* \in B$.
Let $P_B = P \cap B$ be the set of player nodes assigned to $B$, and let $k = |P_B|$.
The cut capacity is minimized when match nodes $(i, j)$ are in $A$ if both $p_i, p_j \in A$, and in $B$ otherwise.
The capacity evaluates to:
$$\text{cap}(A, B) = \binom{n}{2} - \binom{k}{2} + \sum_{p_i \in P_B} s_i$$
To ensure $\text{cap}(A, B) \ge \binom{n}{2}$, we require:
$$\sum_{p_i \in P_B} s_i \ge \binom{k}{2}$$
Since $s_1 \le s_2 \le \dots \le s_n$, the sum $\sum_{p_i \in P_B} s_i$ over any subset of $k$ players is minimized when $P_B$ consists of the $k$ players with the smallest scores:
$$\sum_{p_i \in P_B} s_i \ge \sum_{i=1}^k s_i$$
By condition (1), $\sum_{i=1}^k s_i \ge \binom{k}{2}$!
Therefore, every cut has capacity $\ge \binom{n}{2}$.
By the Max-Flow Min-Cut Theorem, a maximum flow of $\binom{n}{2}$ exists.
Because all edge capacities are integers, the Integrality Theorem guarantees an integer flow where each match node $(i, j)$ routes its 1 unit of flow to either $p_i$ or $p_j$.
This integer flow explicitly defines a tournament with out-degrees $(s_1, \dots, s_n)$.
This completes the proof of Landau's Theorem. $\blacksquare$"""
            }
        ]
    }
    return u6

if __name__ == "__main__":
    u = get_unit6()
    print("Unit 6 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
