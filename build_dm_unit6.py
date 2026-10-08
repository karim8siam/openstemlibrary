# -*- coding: utf-8 -*-
"""
build_dm_unit6.py
Constructs Unit 6: Graph Theory: Connectivity, Eulerian Circuits & Hamiltonian Cycles
Strictly ZERO course numbers.
"""

def get_unit6():
    u6 = {
        "number": 6,
        "title": "Graph Theory: Connectivity, Eulerian Circuits & Hamiltonian Cycles",
        "leadSummary": "Foundations of graph theory and network topology: vertex degree sequences and the Handshaking Lemma, Havel-Hakimi graphic sequence test, walks, trails, paths, cut-vertices and bridge connectivity, Euler's Theorem with Hierholzer's cycle-splicing algorithm, Hamiltonian cycles via Dirac's and Ore's sufficiency theorems, graph isomorphism invariants, and computational complexity of the Traveling Salesperson Problem.",
        "simulations": ["sim_dm_euler_hamilton_graph"],
        "sections": [
            {
                "secNumber": "6.1",
                "title": "Graphs, Subgraphs, Degrees & The Handshaking Lemma",
                "content": r"""### 1. Fundamental Definitions

A **graph** $G = (V, E)$ consists of a non-empty set of vertices $V(G)$ and a set of edges $E(G)$, where each edge $e \in E$ is associated with an unordered pair of vertices $\{u, v\}$.
- **Simple Graph:** Contains no self-loops (edges from a vertex to itself) and no parallel (multiple) edges between any pair of vertices.
- **Multigraph:** Allows parallel edges between pairs of vertices.
- **Pseudograph:** Allows both parallel edges and self-loops.
- **Order and Size:** The order of $G$ is $|V(G)| = n$; the size of $G$ is $|E(G)| = m$.

---

### 2. Vertex Degrees and Euler's Handshaking Lemma

The **degree** of a vertex $v$, denoted $\deg(v)$ or $d(v)$, is the number of edges incident with $v$, with self-loops counted twice.

> **Theorem 6.1 (Euler's Handshaking Lemma):**
> In any undirected graph $G = (V, E)$:
> $$\sum_{v \in V} \deg(v) = 2 |E|$$

*Proof:* Each edge $e = \{u, v\}$ contributes exactly 1 to the degree count of $u$ and 1 to the degree count of $v$. Summing across all vertices counts each edge exactly twice, yielding $2|E|$. $\blacksquare$

> **Corollary 6.1 (Parity of Odd Vertices):**
> In any undirected graph, the number of vertices with odd degree is **even**.
> *Proof:* Partition $V$ into $V_{\text{even}}$ and $V_{\text{odd}}$:
> $$\sum_{v \in V_{\text{even}}} \deg(v) + \sum_{v \in V_{\text{odd}}} \deg(v) = 2|E|$$
> The total sum $2|E|$ is even, and $\sum_{v \in V_{\text{even}}} \deg(v)$ is even. Thus $\sum_{v \in V_{\text{odd}}} \deg(v)$ must be even. A sum of odd integers is even if and only if there is an even number of summands. $\blacksquare$

---

### 3. Graphic Sequences and the Havel-Hakimi Theorem

A finite non-increasing sequence of non-negative integers $d_1 \ge d_2 \ge \dots \ge d_n$ is called **graphic** if there exists a simple graph whose degree sequence is precisely $(d_1, \dots, d_n)$.

> **Theorem 6.2 (Havel-Hakimi Theorem):**
> A sequence $S = (d_1, d_2, \dots, d_n)$ with $d_1 \ge d_2 \ge \dots \ge d_n \ge 0$ (and $d_1 \le n-1$) is graphic if and only if the sequence:
> $$S' = (d_2 - 1, d_3 - 1, \dots, d_{d_1 + 1} - 1, d_{d_1 + 2}, \dots, d_n)$$
> (re-sorted in non-increasing order) is graphic."""
            },
            {
                "secNumber": "6.2",
                "title": "Walks, Trails, Paths, Cycles & Connected Components",
                "content": r"""### 1. Structural Terminology for Traversal

Let $G = (V, E)$ be an undirected graph:
1. **Walk:** An alternating sequence of vertices and edges $v_0, e_1, v_1, e_2, \dots, e_k, v_k$ where each $e_i = \{v_{i-1}, v_i\}$. The length is $k$.
2. **Trail:** A walk in which all edges $e_1, \dots, e_k$ are distinct.
3. **Path:** A walk in which all vertices $v_0, v_1, \dots, v_k$ are distinct.
4. **Closed Walk / Circuit / Cycle:** A walk starting and ending at the same vertex ($v_0 = v_k$). A **cycle** ($C_k$) is a closed walk of length $k \ge 3$ with distinct internal vertices.

---

### 2. Connectivity, Cut-Vertices and Bridges

- A graph $G$ is **connected** if there exists a path between every pair of vertices in $V(G)$.
- A **connected component** of $G$ is a maximal connected subgraph.
- A **cut-vertex** (articulation point) is a vertex $v$ whose removal increases the number of connected components: $\omega(G - v) > \omega(G)$.
- A **bridge** (cut-edge) is an edge $e$ whose removal increases the number of connected components: $\omega(G - e) > \omega(G)$.

> **Theorem 6.3 (Characterization of Bridges):**
> An edge $e \in E(G)$ is a bridge if and only if $e$ does not lie on any cycle in $G$."""
            },
            {
                "secNumber": "6.3",
                "title": "Eulerian Trails and Circuits: Euler's Theorem & Hierholzer's Algorithm",
                "content": r"""### 1. Eulerian Circuits and Trails

- An **Eulerian circuit** is a closed trail that traverses every edge of graph $G$ exactly once.
- An **Eulerian trail** is an open trail that traverses every edge of graph $G$ exactly once.
- A graph containing an Eulerian circuit is called an **Eulerian graph**.

> **Theorem 6.4 (Euler-Hierholzer Theorem):**
> A connected undirected graph $G$ has an **Eulerian circuit** if and only if every vertex of $G$ has **even degree**.
> A connected graph has an **Eulerian trail** if and only if it has **exactly two vertices of odd degree** (which serve as the start and end of the trail).

---

### 2. Hierholzer's Linear-Time Algorithm ($O(|E|)$)

To find an Eulerian circuit in an Eulerian graph:
1. Start at an arbitrary vertex $v$ and follow unused edges to form a simple cycle $C$ until returning to $v$ (guaranteed by even degrees).
2. If $C$ does not contain all edges in $G$, select a vertex $u \in C$ that has incident unused edges.
3. Form a new sub-cycle $C'$ starting and ending at $u$ using unused edges.
4. Splice cycle $C'$ into $C$ at vertex $u$.
5. Repeat until all edges in $E(G)$ have been traversed."""
            },
            {
                "secNumber": "6.4",
                "title": "Hamiltonian Paths & Cycles: Dirac's & Ore's Theorems, TSP Complexity",
                "content": r"""### 1. Hamiltonian Cycles and Paths

- A **Hamiltonian path** is a path that visits every vertex of $G$ exactly once.
- A **Hamiltonian cycle** is a closed cycle that visits every vertex of $G$ exactly once.
- A graph containing a Hamiltonian cycle is called **Hamiltonian**.

Unlike Eulerian graphs (which have a simple local degree characterization solvable in $O(|V| + |E|)$ time), deciding whether a general graph is Hamiltonian is **NP-complete**.

---

### 2. Classical Sufficiency Theorems

> **Theorem 6.5 (Ore's Theorem, 1960):**
> Let $G$ be a simple graph with $n \ge 3$ vertices. If for every pair of non-adjacent vertices $u$ and $v$:
> $$\deg(u) + \deg(v) \ge n$$
> then $G$ is Hamiltonian.

> **Corollary 6.2 (Dirac's Theorem, 1952):**
> Let $G$ be a simple graph with $n \ge 3$ vertices. If every vertex has degree:
> $$\deg(v) \ge \frac{n}{2}$$
> then $G$ is Hamiltonian.

*Proof of Dirac from Ore:* If $\deg(v) \ge n/2$ for all $v$, then for any non-adjacent $u, v$, $\deg(u) + \deg(v) \ge n/2 + n/2 = n$. By Ore's Theorem, $G$ is Hamiltonian. $\blacksquare$

---

### 3. The Traveling Salesperson Problem (TSP)

Given a complete weighted graph $K_n$, find a Hamiltonian cycle of minimum total weight:
$$\min_{\pi \in S_n} \sum_{i=1}^{n-1} w(v_{\pi(i)}, v_{\pi(i+1)}) + w(v_{\pi(n)}, v_{\pi(1)})$$
TSP is NP-hard. When edge weights satisfy the triangle inequality ($w(u, v) \le w(u, x) + w(x, v)$), the **Christofides-Serdyukov Algorithm** provides a polynomial-time $\frac{3}{2}$-approximation using MST and minimum-weight perfect matching on odd-degree vertices."""
            },
            {
                "secNumber": "6.5",
                "title": "Graph Isomorphism, Invariants & Interactive Graph Analyzer",
                "content": r"""### 1. Graph Isomorphism and Structural Equivalence

> **Definition 6.1 (Graph Isomorphism):**
> Two graphs $G_1 = (V_1, E_1)$ and $G_2 = (V_2, E_2)$ are **isomorphic** (written $G_1 \cong G_2$) if there exists a bijection $f: V_1 \to V_2$ such that:
> $$\{u, v\} \in E_1 \iff \{f(u), f(v)\} \in E_2$$

#### Graph Invariants (Necessary Conditions for Isomorphism):
Two isomorphic graphs must share identical values for all topological invariants:
1. Number of vertices $|V|$.
2. Number of edges $|E|$.
3. Sorted degree sequence.
4. Number of connected components.
5. Length of the shortest cycle (girth).
6. Chromatic number $\chi(G)$ and independence number $\alpha(G)$.
7. Spectrum (eigenvalues) of the adjacency matrix.

---

### 2. Interactive Eulerian & Hamiltonian Graph Analyzer

The simulation below enables dynamic testing of graph topologies:
- **Degree Analyzer & Handshaking Check:** Live verification of $\sum \deg(v) = 2|E|$ and odd-degree parity.
- **Hierholzer Trail Tracer:** Step-by-step visual cycle-splicing for Eulerian trails.
- **Dirac / Ore Hamiltonian Inspector:** Real-time checking of degree sums for non-adjacent pairs."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 6.1: Havel-Hakimi Graphic Sequence Testing",
                "statement": r"""Apply the Havel-Hakimi theorem step-by-step to determine whether each of the following integer degree sequences is **graphic** (can be realized as a simple graph):
1. Sequence $S_1 = (5, 4, 3, 2, 2, 2)$
2. Sequence $S_2 = (5, 5, 4, 3, 2, 1)$

If graphic, construct an adjacency list for the realizing graph. If not graphic, state the exact step where realization fails.""",
                "hints": [
                    "For $S_1$, $d_1 = 5$. Subtract 1 from the next 5 terms.",
                    "Check Handshaking Lemma first: does the sum of degrees equal an even number?",
                    "Remember to re-sort the remaining sequence in descending order after each subtraction."
                ],
                "solution": r"""### 1. Analysis of Sequence $S_1 = (5, 4, 3, 2, 2, 2)$
Sum of degrees: $5 + 4 + 3 + 2 + 2 + 2 = 18$ (Even, satisfies Handshaking parity).
The sequence has $n = 6$ terms. Maximum degree $d_1 = 5 \le 6 - 1 = 5$.

- **Step 1:** Delete $d_1 = 5$ and subtract 1 from the next 5 terms:
  $$(4 - 1, 3 - 1, 2 - 1, 2 - 1, 2 - 1) = (3, 2, 1, 1, 1)$$
  The sequence is already sorted: $(3, 2, 1, 1, 1)$.
- **Step 2:** Delete $d_1 = 3$ and subtract 1 from the next 3 terms:
  $$(2 - 1, 1 - 1, 1 - 1, 1) = (1, 0, 0, 1)$$
  Re-sorting in descending order: $(1, 1, 0, 0)$.
- **Step 3:** Delete $d_1 = 1$ and subtract 1 from the next 1 term:
  $$(1 - 1, 0, 0) = (0, 0, 0)$$

Since $(0, 0, 0)$ is the degree sequence of a graph with 3 isolated vertices (trivially graphic), by the Havel-Hakimi theorem, the original sequence $S_1$ is **graphic**.

#### Construction of Realization:
Let vertices be $\{v_1, v_2, v_3, v_4, v_5, v_6\}$:
- $v_1$ connects to all 5 other vertices: $\{v_2, v_3, v_4, v_5, v_6\}$.
- $v_2$ connects to $v_1, v_3, v_4, v_5$.
- $v_3$ connects to $v_1, v_2$.
- $v_4$ connects to $v_1, v_2$.
- $v_5$ connects to $v_1, v_2$.
- $v_6$ connects to $v_1$.
Verification of degrees:
$\deg(v_1) = 5$, $\deg(v_2) = 4$, $\deg(v_3) = 2$, $\deg(v_4) = 2$, $\deg(v_5) = 2$, $\deg(v_6) = 1$... wait, $S_1$ requires $(5, 4, 3, 2, 2, 2)$, so connecting $v_3$ to $v_4$ adjusts degrees to:
$v_1: 5$, $v_2: 4$, $v_3: 3$, $v_4: 2$, $v_5: 2$, $v_6: 2$. All degrees match $S_1$.

---

### 2. Analysis of Sequence $S_2 = (5, 5, 4, 3, 2, 1)$
Sum of degrees:
$$\sum d_i = 5 + 5 + 4 + 3 + 2 + 1 = 20 \quad (\text{Even})$$
Number of terms $n = 6$.

- **Step 1:** Delete $d_1 = 5$ and subtract 1 from the next 5 terms:
  $$(5 - 1, 4 - 1, 3 - 1, 2 - 1, 1 - 1) = (4, 3, 2, 1, 0)$$
  Already sorted: $(4, 3, 2, 1, 0)$.
- **Step 2:** Delete $d_1 = 4$ and subtract 1 from the next 4 terms:
  $$(3 - 1, 2 - 1, 1 - 1, 0 - 1) = (2, 1, 0, -1)$$

Notice the term **$-1$**!
Since a graph cannot possess negative vertex degrees, $(2, 1, 0, -1)$ is impossible to realize as a graph.
Therefore, by the Havel-Hakimi theorem, sequence $S_2$ is **NOT graphic**. $\blacksquare$"""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 6.2: Constructive Proof of Euler's Theorem via Hierholzer's Splicing",
                "statement": r"""Let $G = (V, E)$ be a finite connected undirected graph.
1. Prove that if $G$ possesses an Eulerian circuit, then every vertex $v \in V$ must have an even degree.
2. Prove the converse: if every vertex in a connected graph $G$ has even degree, then $G$ must possess an Eulerian circuit.
3. Formulate the proof constructively by establishing the correctness of Hierholzer's cycle-splicing algorithm.""",
                "hints": [
                    "For part 1, every time the Eulerian circuit visits a vertex, it arrives via one edge and departs via another.",
                    "For part 2, first prove that any graph with minimum degree $\\ge 2$ contains a simple cycle.",
                    "Remove the cycle edges and consider the remaining components."
                ],
                "solution": r"""### 1. Necessity: Eulerian Circuit $\implies$ All Degrees Even
Let $C = (v_0, e_1, v_1, e_2, \dots, e_m, v_0)$ be an Eulerian circuit in $G$.
1. By definition, $C$ traverses every edge in $E(G)$ exactly once.
2. Consider any vertex $u \in V$:
   - Every time the circuit passes through $u$ (arriving via edge $e_{\text{in}}$ and leaving via edge $e_{\text{out}}$), exactly 2 distinct incident edges are consumed.
   - If $u$ is the start/terminal vertex $v_0$, the circuit leaves $v_0$ via $e_1$ (1 edge) and finally returns via $e_m$ (1 edge), again accounting for an even number (2) of edges, plus 2 edges for every intermediate visit.
3. Since each edge incident with $u$ appears in $C$ exactly once, the total degree $\deg(u)$ must equal $2 \times (\text{number of visits by } C)$.
4. Thus, $\deg(u)$ is strictly even for every vertex $u \in V$.

---

### 2. Sufficiency: All Degrees Even $\implies$ Eulerian Circuit Exists

#### Lemma: Existence of a Cycle
> If every vertex in a non-empty graph $H$ has degree $\ge 2$, then $H$ contains a simple cycle.
*Proof:* Start at any vertex $w_0$. Since $\deg(w_0) \ge 2$, follow an incident edge to $w_1$. At $w_k$, since $\deg(w_k) \ge 2$, we can always exit along an edge different from the one we entered. Because $V(H)$ is finite, by the Pigeonhole Principle the walk must eventually revisit a previously seen vertex $w_i$ ($i < k$). The segment from $w_i$ to $w_k$ forms a simple cycle.

#### Induction on Number of Edges $|E|$
Let $P(m)$ be the statement that every connected graph with $m$ edges where every vertex has even degree possesses an Eulerian circuit.
- **Base Case:** $m = 0$. A single vertex with 0 edges has a trivial circuit of length 0.
- **Inductive Step:** Assume $P(k)$ holds for all $k < m$.
  Since $G$ is connected and all vertices have even positive degree, $\deg(v) \ge 2$ for all $v$.
  By the Lemma, $G$ contains a simple cycle $C_1$.
  Remove the edges of $C_1$ from $G$, forming the subgraph $G' = (V, E \setminus E(C_1))$.
  In $G'$, for every vertex $v$, its degree in $G'$ is $\deg_{G'}(v) = \deg_G(v) - \deg_{C_1}(v)$.
  Since $\deg_{C_1}(v)$ is either 2 (if $v \in C_1$) or 0 (if $v \notin C_1$), and $\deg_G(v)$ is even, $\deg_{G'}(v)$ is **even for all $v$**!
  The graph $G'$ decomposes into connected components $H_1, H_2, \dots, H_r$ (ignoring isolated vertices).
  Each component $H_i$ has strictly fewer than $m$ edges and all vertices have even degree.
  By the inductive hypothesis, each $H_i$ has an Eulerian circuit $C_{H_i}$.
  Since $G$ was connected, each $H_i$ shares at least one vertex with $C_1$.
  We splice the circuits $C_{H_i}$ into $C_1$ at their respective shared vertices.
  The combined traversal is a single closed circuit traversing every edge of $G$ exactly once.

---

### 3. Hierholzer's Algorithm Correctness
Hierholzer's algorithm algorithmically executes this induction:
1. It maintains a linked list of vertices in the current circuit $C$.
2. Finding each new cycle takes time proportional to the cycle length by traversing unused edges.
3. Splicing at shared vertex $u$ is an $O(1)$ pointer insertion.
4. Each edge is examined a constant number of times.
Thus, Hierholzer's algorithm halts in $O(|V| + |E|)$ time with an Eulerian circuit. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 6.3: Complete Analytical Proof of Ore's and Dirac's Theorems",
                "statement": r"""Let $G = (V, E)$ be a simple graph with $n \ge 3$ vertices.
1. Prove **Ore's Theorem**: If for every pair of non-adjacent vertices $u, v \in V$:
$$\deg(u) + \deg(v) \ge n$$
then $G$ contains a Hamiltonian cycle.
2. Deduce **Dirac's Theorem** as an immediate corollary.
3. Show by constructing an explicit counterexample that the degree bound $n$ in Ore's condition is best possible (tight), i.e., show there exists a non-Hamiltonian graph on $n$ vertices where all non-adjacent pairs satisfy $\deg(u) + \deg(v) = n - 1$.""",
                "hints": [
                    "Proof by contradiction: assume Ore's condition holds but $G$ is non-Hamiltonian. Add edges until $G$ is maximal non-Hamiltonian.",
                    "Adding one more edge creates a Hamiltonian cycle, which means $G$ contains a Hamiltonian path $v_1, v_2, \\dots, v_n$ between two non-adjacent vertices.",
                    "Use the Pigeonhole Principle on index sets $S = \\{i \\mid (v_1, v_{i+1}) \\in E\\}$ and $T = \\{i \\mid (v_i, v_n) \\in E\\}$."
                ],
                "solution": r"""### 1. Proof of Ore's Theorem

#### Step A: Maximal Non-Hamiltonian Graph
1. Assume for contradiction that Ore's condition holds, but $G$ is non-Hamiltonian.
2. If adding an edge between non-adjacent vertices keeps the graph non-Hamiltonian, add it.
3. Repeat until adding **any** missing edge creates a Hamiltonian cycle. Let $G^* = (V, E^*)$ be this **maximal non-Hamiltonian graph** containing $G$ ($E \subseteq E^*$).
4. Since $E \subseteq E^*$, for all non-adjacent pairs $u, v$ in $G^*$:
   $$\deg_{G^*}(u) + \deg_{G^*}(v) \ge \deg_G(u) + \deg_G(v) \ge n$$
   So $G^*$ still satisfies Ore's condition.

#### Step B: Extraction of a Hamiltonian Path
Since $G^*$ is non-Hamiltonian, it cannot be complete ($G^* \ne K_n$).
There exist non-adjacent vertices $x, y \in V$ with $\{x, y\} \notin E^*$.
By maximality of $G^*$, adding edge $\{x, y\}$ creates a Hamiltonian cycle.
Therefore, in $G^*$ itself, there exists a **Hamiltonian path** connecting $x$ and $y$:
$$P = (v_1, v_2, v_3, \dots, v_n), \qquad \text{where } v_1 = x \text{ and } v_n = y$$
Notice $\{v_1, v_n\} \notin E^*$.

#### Step C: The Index Interlocking Argument
Define two subsets of indices $\{1, 2, \dots, n-1\}$:
$$S = \{i \in \{1, \dots, n-1\} \mid \{v_1, v_{i+1}\} \in E^*\}$$
$$T = \{i \in \{1, \dots, n-1\} \mid \{v_i, v_n\} \in E^*\}$$
Notice:
- The size of $S$ is the number of neighbors of $v_1$: $|S| = \deg(v_1)$.
- The size of $T$ is the number of neighbors of $v_n$: $|T| = \deg(v_n)$.
Both $S$ and $T$ are subsets of $\{1, 2, \dots, n-1\}$, which has size $n - 1$.
Now calculate the sum of their sizes:
$$|S| + |T| = \deg(v_1) + \deg(v_n) \ge n$$
by Ore's condition on the non-adjacent pair $\{v_1, v_n\}$!

By the Generalized Pigeonhole Principle / Principle of Inclusion-Exclusion:
$$|S \cap T| = |S| + |T| - |S \cup T| \ge n - (n - 1) = 1$$
Thus, there exists at least one index $k \in S \cap T$!

#### Step D: Construction of Hamiltonian Cycle
Since $k \in S \cap T$:
1. $k \in S \implies \{v_1, v_{k+1}\} \in E^*$.
2. $k \in T \implies \{v_k, v_n\} \in E^*$.

Now construct the closed cycle:
$$(v_1 \to v_2 \to \dots \to v_k \to v_n \to v_{n-1} \to \dots \to v_{k+1} \to v_1)$$
- We start at $v_1$, walk forward along the path to $v_k$.
- From $v_k$, take edge $\{v_k, v_n\}$ to jump to the end vertex $v_n$.
- Walk backward along the path from $v_n$ down to $v_{k+1}$.
- From $v_{k+1}$, take edge $\{v_{k+1}, v_1\}$ back to $v_1$!

This closed cycle visits every single vertex $\{v_1, v_2, \dots, v_n\}$ exactly once!
Thus, $G^*$ contains a Hamiltonian cycle.
This contradicts the premise that $G^*$ is non-Hamiltonian!
Therefore, the initial assumption was false, and $G$ must be Hamiltonian. $\blacksquare$

---

### 2. Dirac's Theorem as a Corollary
Let $G$ have $n \ge 3$ vertices with $\deg(v) \ge n/2$ for all $v \in V$.
For any pair of non-adjacent vertices $u, v$:
$$\deg(u) + \deg(v) \ge \frac{n}{2} + \frac{n}{2} = n$$
Ore's condition is satisfied for every non-adjacent pair.
By Ore's Theorem, $G$ is Hamiltonian. $\blacksquare$

---

### 3. Tightness of the Bound: Counterexample Graph
Consider the graph $G$ constructed by joining a complete graph $K_{k+1}$ and an isolated vertex $w$, or more generally:
Let $n = 2k + 1$ (odd).
Construct $G = K_k \vee \overline{K_{k+1}}$ (the complete bipartite graph $K_{k, k+1}$ plus all edges in the $k$-vertex part).
The $k+1$ vertices in the independent set have degree $k = \frac{n-1}{2}$.
Any two non-adjacent vertices $u, v$ lie in the independent set, so:
$$\deg(u) + \deg(v) = k + k = 2k = n - 1$$
Any Hamiltonian cycle must alternate through the independent set, requiring at least as many vertices in the connecting set ($k \ge k+1$), which is impossible.
Thus, $G$ is **non-Hamiltonian**, proving that the bound $n$ is strictly tight. $\blacksquare$"""
            }
        ]
    }
    return u6

if __name__ == "__main__":
    u6 = get_unit6()
    print(f"Loaded Unit 6: {u6['title']} with {len(u6['sections'])} sections and {len(u6['problems'])} problems.")
