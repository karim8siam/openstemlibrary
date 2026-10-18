# -*- coding: utf-8 -*-
"""
build_gt_unit7.py
Constructs Unit 7: Planar Graphs, Euler's Formula, Kuratowski's Theorem & Duality
"""

def get_unit7():
    u7 = {
        "number": 7,
        "title": "Planar Graphs, Euler's Formula, Kuratowski's Theorem & Duality",
        "leadSummary": "Comprehensive theory of graph planarity and embeddings: planar embeddings, Jordan curve theorem in planarity, faces/regions, Euler's polyhedral formula V - E + F = 2, maximum edge bounds for planar graphs (E <= 3V - 6), non-planarity of K_5 and K_3,3, Kuratowski's theorem, Wagner's minors, geometric and combinatorial duals, and Whitney's theorem on planar duality.",
        "simulations": ["sim_gt_planar_duality"],
        "sections": [
            {
                "secNumber": "7.1",
                "title": "Planar Embeddings, Jordan Curves & Face Partition",
                "content": r"""### 1. Planar Graphs and Planar Embeddings

A graph is an abstract topological entity. When drawn in a continuous geometric space, edges may or may not cross.

> **Definition 7.1 (Planar Graph and Plane Graph):**
> 1. A graph $G$ is called **planar** if it can be drawn in the Euclidean plane $\mathbb{R}^2$ (or on the 2-sphere $S^2$) such that **no two edges intersect**, except at their common endpoints.
> 2. A specific non-crossing drawing of a planar graph in $\mathbb{R}^2$ is called a **planar embedding** (or a **plane graph**).

---

### 2. Faces and Regions of a Plane Graph

A planar embedding partitions the plane $\mathbb{R}^2 \setminus G$ into topologically connected open domains called **faces** (or regions).

> **Definition 7.2 (Faces and the Outer Face):**
> Let $G$ be a plane graph.
> - The connected components of $\mathbb{R}^2 \setminus G$ are the **faces** of $G$.
> - Exactly one face is unbounded, called the **exterior face** (or infinite face).
> - All other faces are bounded, called **interior faces**.
> - The **boundary** of a face $f$ consists of the vertices and edges that enclose $f$.
> - The **degree of a face** $f$, denoted $\deg(f)$, is the number of edges along its boundary (with cut-edges counted twice).

> **Theorem 7.1 (Handshaking Lemma for Faces):**
> In any plane graph $G$ with edge set $E$ and face set $F$:
> $$\sum_{f \in F} \deg(f) = 2 |E|$$

#### Proof:
Every edge either separates two distinct faces $f_1 \ne f_2$ (contributing 1 to $\deg(f_1)$ and 1 to $\deg(f_2)$), or is a bridge surrounded on both sides by the same face $f$ (contributing 2 to $\deg(f)$).
In either case, each edge contributes exactly 2 to the sum of face degrees. $\blacksquare$"""
            },
            {
                "secNumber": "7.2",
                "title": "Euler's Polyhedral Formula $V - E + F = 2$ & Corollaries",
                "content": r"""### 1. Euler's Formula for Connected Plane Graphs

Published by Leonhard Euler in 1758 for convex 3D polyhedra, this formula forms the bedrock of topological graph theory:

> **Theorem 7.2 (Euler's Formula):**
> Let $G$ be a connected plane graph with $V$ vertices, $E$ edges, and $F$ faces.
> Then:
> $$V - E + F = 2$$

#### Complete Formal Proof (by Induction on Edges):
We prove the formula by induction on the number of edges $E$ for any connected plane graph on $V$ vertices:
- **Base Case (Trees):**
  If $G$ contains no cycles, then $G$ is a tree.
  By Theorem 3.1, $E = V - 1$.
  Since a tree contains no cycles, it does not divide the plane into interior faces; it has only the single unbounded exterior face: $F = 1$.
  Substituting these values:
  $$V - E + F = V - (V - 1) + 1 = 1 + 1 = 2$$
  The base case holds with exact equality!
- **Inductive Step:**
  Assume the formula $V - E + F = 2$ holds for all connected plane graphs with strictly fewer than $E$ edges.
  Let $G$ be a connected plane graph with $E$ edges that is not a tree.
  Since $G$ is not a tree, $G$ must contain at least one simple cycle $C$.
  Choose an edge $e$ lying on the cycle $C$.
  By the Jordan Curve Theorem, the cycle $C$ separates the plane into an interior domain and an exterior domain.
  Therefore, the edge $e$ lies on the boundary of **two distinct faces** $f_1 \ne f_2$.
  Now, remove the edge $e$ from $G$, forming the graph $G' = G - e$.
  Notice:
  1. Since $e$ lay on a cycle, $G'$ remains connected.
  2. The vertex count is unchanged: $V' = V$.
  3. The edge count decreases by 1: $E' = E - 1$.
  4. The two faces $f_1$ and $f_2$ merge into a single unified face in $G'$, so the face count decreases by 1: $F' = F - 1$.
  By the induction hypothesis applied to $G'$:
  $$V' - E' + F' = 2$$
  Substituting $V' = V$, $E' = E - 1$, and $F' = F - 1$:
  $$V - (E - 1) + (F - 1) = V - E + 1 + F - 1 = V - E + F = 2$$
Therefore, $V - E + F = 2$ holds for all connected plane graphs. $\blacksquare$

> **Corollary 7.2.1 (Disconnected Planar Graphs):**
> If a planar graph $G$ has $\omega(G) = k$ connected components:
> $$V - E + F = 1 + k$$"""
            },
            {
                "secNumber": "7.3",
                "title": "Edge Upper Bounds & Non-Planarity of $K_5$ and $K_{3,3}$",
                "content": r"""### 1. Maximum Edges in Simple Planar Graphs

In a simple plane graph, every face boundary must contain at least 3 edges (no self-loops or multiple edges):
$$\deg(f) \ge 3, \quad \forall f \in F$$

> **Theorem 7.3 (Planar Edge Upper Bound):**
> In any simple planar graph $G$ with $V \ge 3$ vertices and $E$ edges:
> $$E \le 3V - 6$$
> If $G$ is triangle-free (contains no $C_3$, such as a bipartite graph):
> $$E \le 2V - 4$$

#### Complete Proof:
1. **General Bound ($E \le 3V - 6$):**
   By the Face Handshaking Lemma (Theorem 7.1) and $\deg(f) \ge 3$:
   $$2E = \sum_{f \in F} \deg(f) \ge \sum_{f \in F} 3 = 3F \implies F \le \frac{2}{3}E$$
   Substitute this into Euler's formula $V - E + F = 2$:
   $$2 = V - E + F \le V - E + \frac{2}{3}E = V - \frac{1}{3}E$$
   $$2 \le V - \frac{1}{3}E \implies \frac{1}{3}E \le V - 2 \implies E \le 3V - 6 \quad \blacksquare$$

2. **Triangle-Free Bound ($E \le 2V - 4$):**
   If $G$ contains no triangles, then every face boundary must have at least 4 edges: $\deg(f) \ge 4$.
   $$2E = \sum_{f \in F} \deg(f) \ge 4F \implies F \le \frac{1}{2}E$$
   Substitute into Euler's formula:
   $$2 = V - E + F \le V - E + \frac{1}{2}E = V - \frac{1}{2}E \implies E \le 2V - 4 \quad \blacksquare$$

---

### 2. The Canonical Non-Planar Graphs: $K_5$ and $K_{3,3}$

> **Theorem 7.4 (Non-Planarity of $K_5$ and $K_{3,3}$):**
> 1. The complete graph $K_5$ is **non-planar**.
> 2. The complete bipartite graph $K_{3,3}$ (the Utility Graph) is **non-planar**.

#### Proof of 1 ($K_5$):
For $K_5$, vertex count $V = 5$, edge count $E = \binom{5}{2} = 10$.
If $K_5$ were planar, it would satisfy Theorem 7.3:
$$E \le 3V - 6 \implies 10 \le 3(5) - 6 = 15 - 6 = 9$$
$10 \le 9$ is a contradiction!
Therefore, $K_5$ is non-planar. $\blacksquare$

#### Proof of 2 ($K_{3,3}$):
For $K_{3,3}$, vertex count $V = 3 + 3 = 6$, edge count $E = 3 \times 3 = 9$.
$K_{3,3}$ is bipartite, so it contains no odd cycles; in particular, it is triangle-free!
If $K_{3,3}$ were planar, it would satisfy the triangle-free bound:
$$E \le 2V - 4 \implies 9 \le 2(6) - 4 = 12 - 4 = 8$$
$9 \le 8$ is a contradiction!
Therefore, $K_{3,3}$ is non-planar. $\blacksquare$"""
            },
            {
                "secNumber": "7.4",
                "title": "Kuratowski's Theorem, Subdivisions & Wagner's Minors",
                "content": r"""### 1. Graph Subdivisions and Homeomorphism

> **Definition 7.3 (Elementary Subdivision):**
> An **elementary subdivision** of an edge $e = \{u, v\}$ is the operation of replacing $e$ with two edges $\{u, w\}$ and $\{w, v\}$ by inserting a new vertex $w$ of degree 2.
> Two graphs $G_1$ and $G_2$ are **homeomorphic** (or topological minors) if both can be obtained from the same graph by a sequence of elementary subdivisions.

A graph $H$ is a **subdivision of $K$** if $H$ can be obtained from $K$ by subdividing zero or more edges.
Notice that subdividing an edge does not change planarity: $G$ is planar if and only if any subdivision of $G$ is planar.

---

### 2. Kuratowski's Theorem

In 1930, Polish mathematician Kazimierz Kuratowski established the definitive characterization of planarity:

> **Theorem 7.5 (Kuratowski's Theorem, 1930):**
> A graph $G$ is **planar** if and only if it contains **no subgraph that is a subdivision of $K_5$ or $K_{3,3}$**.

---

### 3. Wagner's Theorem and Graph Minors

In 1937, Klaus Wagner formulated an alternative characterization based on **minor operations**:
- **Minor Operations:** Edge deletion, vertex deletion, and **edge contraction** (merging the two endpoints of an edge).
- A graph $H$ is a **minor** of $G$ if $H$ can be obtained from $G$ by a finite sequence of deletions and contractions.

> **Theorem 7.6 (Wagner's Theorem, 1937):**
> A graph $G$ is **planar** if and only if it contains **neither $K_5$ nor $K_{3,3}$ as a minor**."""
            },
            {
                "secNumber": "7.5",
                "title": "Geometric Duals, Combinatorial Duality & Whitney's Theorem",
                "content": r"""### 1. Construction of the Geometric Dual $G^*$

Let $G$ be a plane graph with vertex set $V$, edge set $E$, and face set $F$.

> **Definition 7.4 (Geometric Dual $G^*$):**
> The **geometric dual** $G^* = (V^*, E^*)$ is constructed as follows:
> 1. For each face $f_i \in F(G)$, place a corresponding dual vertex $v_i^* \in V^*$.
> 2. For each edge $e \in E(G)$ that separates face $f_i$ and face $f_j$, draw a dual edge $e^* \in E^*$ connecting $v_i^*$ and $v_j^*$, crossing $e$ exactly once.
> (If $e$ is surrounded on both sides by the same face $f_i$, $e^*$ is a self-loop on $v_i^*$).

#### Dual Parameters:
$$V^* = F, \quad E^* = E, \quad F^* = V$$
$$\deg_{G^*}(v_i^*) = \deg_G(f_i)$$
If $G$ is connected, then $(G^*)^* \cong G$ (the dual of the dual is isomorphic to the primal graph).

---

### 2. Whitney's Planar Duality Theorem

> **Theorem 7.7 (Whitney's Duality Theorem, 1932):**
> A graph $G$ is **planar** if and only if it possesses a **combinatorial dual**:
> That is, there exists a graph $G^*$ and an edge bijection $\phi: E(G) \to E(G^*)$ such that for every subset $S \subseteq E(G)$:
> $$S \text{ is a cut-set in } G \iff \phi(S) \text{ is a cycle in } G^*$$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Euler's Formula on Platonic Solids & Maximal Planar Faces",
                "statement": r"1. Verify Euler's formula $V - E + F = 2$ for the 1-skeletons of all five Platonic solids: (a) Regular Tetrahedron, (b) Cube (Hexahedron), (c) Regular Octahedron, (d) Regular Dodecahedron, (e) Regular Icosahedron. 2. A connected planar graph has 10 vertices and 15 edges. Determine the exact number of faces in any planar embedding of $G$.",
                "hints": [
                    "For Part 1, count the vertices, edges, and faces for each polyhedron.",
                    "For Part 2, substitute $V = 10$ and $E = 15$ directly into Euler's formula $V - E + F = 2$."
                ],
                "solution": r"""**Part 1: Verification of Euler's Formula on the Platonic Solids**

**(a) Regular Tetrahedron:**
- $V = 4$, $E = 6$, $F = 4$ (all faces triangular).
- $V - E + F = 4 - 6 + 4 = 2$. Verified!

**(b) Cube (Hexahedron):**
- $V = 8$, $E = 12$, $F = 6$ (all faces quadrilateral).
- $V - E + F = 8 - 12 + 6 = 2$. Verified!

**(c) Regular Octahedron:**
- $V = 6$, $E = 12$, $F = 8$ (all faces triangular).
- $V - E + F = 6 - 12 + 8 = 2$. Verified!

**(d) Regular Dodecahedron:**
- $V = 20$, $E = 30$, $F = 12$ (all faces pentagonal).
- $V - E + F = 20 - 30 + 12 = 2$. Verified!

**(e) Regular Icosahedron:**
- $V = 12$, $E = 30$, $F = 20$ (all faces triangular).
- $V - E + F = 12 - 30 + 20 = 2$. Verified!

Notice the beautiful duality:
- Tetrahedron is self-dual ($V=4, F=4$).
- Cube ($V=8, F=6$) is dual to Octahedron ($V=6, F=8$).
- Dodecahedron ($V=20, F=12$) is dual to Icosahedron ($V=12, F=20$).

---

**Part 2: Face Count for $V = 10, E = 15$**

Given $V = 10$ and $E = 15$ in a connected planar graph.
By Euler's Formula (Theorem 7.2):
$$V - E + F = 2$$
Substitute values:
$$10 - 15 + F = 2 \implies -5 + F = 2 \implies F = 7$$
Any planar embedding of $G$ will contain exactly **7 faces** (6 interior faces and 1 exterior face). $\blacksquare$"""
            },
            {
                "tier": "Advanced",
                "title": "Degrees in Planar Graphs & Non-Planarity via Girth Bounds",
                "statement": r"1. Prove that every simple planar graph must contain at least one vertex of degree at most 5: $\delta(G) \le 5$. 2. The Petersen graph has 10 vertices and 15 edges, and has girth 5 (its shortest cycle has length 5). Use generalized Euler face bounds to prove rigorously that the Petersen graph is non-planar.",
                "hints": [
                    "For Part 1, assume for contradiction that $\\deg(v) \\ge 6$ for all $v \\in V$, and sum the degrees using Handshaking and the bound $E \\le 3V - 6$.",
                    "For Part 2, since the girth is 5, every face boundary must have at least 5 edges: $\\deg(f) \\ge 5$. Derive the bound $E \\le \\frac{5}{3}(V - 2)$."
                ],
                "solution": r"""**Part 1: Proof that $\delta(G) \le 5$ in every Simple Planar Graph**

Let $G = (V, E)$ be a simple planar graph with $V = n$ vertices and $E = m$ edges.
- If $n \le 6$, then $\delta(G) \le n - 1 \le 5$ trivially.
- Assume $n \ge 7$.
Assume for contradiction that $\delta(G) \ge 6$.
Then every vertex in $G$ has degree at least 6:
$$\deg(v) \ge 6, \quad \forall v \in V$$
Summing over all $n$ vertices and applying Euler's Handshaking Lemma:
$$2m = \sum_{v \in V} \deg(v) \ge \sum_{v \in V} 6 = 6n \implies 2m \ge 6n \implies m \ge 3n$$
However, by Theorem 7.3, every simple planar graph must satisfy:
$$m \le 3n - 6$$
Combining both inequalities:
$$3n \le m \le 3n - 6 \implies 3n \le 3n - 6 \implies 0 \le -6$$
This is a direct mathematical impossibility!
Therefore, our assumption that every vertex has degree $\ge 6$ was false.
Hence, every simple planar graph must contain at least one vertex with degree $\le 5$:
$$\delta(G) \le 5 \quad \blacksquare$$

---

**Part 2: Non-Planarity of the Petersen Graph via Girth Bound**

Let $G$ be the Petersen graph:
- Vertices: $V = 10$.
- Edges: $E = 15$ (3-regular graph on 10 vertices).
- Girth: $g(G) = 5$ (contains no 3-cycles or 4-cycles; shortest cycle is $C_5$).

Suppose for contradiction that the Petersen graph were **planar**.
In any planar embedding of $G$, the boundary of every face $f$ must be a cycle.
Because the shortest cycle in $G$ has length 5, every face boundary must contain at least 5 edges:
$$\deg(f) \ge 5, \quad \forall f \in F$$
By the Face Handshaking Lemma (Theorem 7.1):
$$2E = \sum_{f \in F} \deg(f) \ge \sum_{f \in F} 5 = 5F \implies F \le \frac{2}{5}E$$
Now substitute into Euler's Formula $V - E + F = 2$:
$$2 = V - E + F \le V - E + \frac{2}{5}E = V - \frac{3}{5}E$$
Rearranging for $E$:
$$\frac{3}{5}E \le V - 2 \implies E \le \frac{5}{3}(V - 2)$$
Now evaluate this bound for the Petersen graph ($V = 10$):
$$E \le \frac{5}{3}(10 - 2) = \frac{5}{3}(8) = \frac{40}{3} \approx 13.33$$
Since $E = 15$, we have:
$$15 \le 13.33$$
This is an absolute contradiction!
Therefore, the Petersen graph cannot be embedded in the plane without edge crossings.
Hence the Petersen graph is **non-planar**. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Complete Formal Proof of Kuratowski's Minor Equivalence for $K_5$ & $K_{3,3}$",
                "statement": r"1. Prove that any graph $G$ containing a subgraph homeomorphic to $K_5$ or $K_{3,3}$ is non-planar. 2. Demonstrate that the Petersen graph contains a minor isomorphic to $K_5$, and identify the explicit edge contraction sequence.",
                "hints": [
                    "For Part 1, use the fact that elementary subdivisions preserve planarity.",
                    "For Part 2, view the Petersen graph as an outer 5-cycle and inner 5-star connected by 5 spokes. Contract the 5 spokes."
                ],
                "solution": r"""**Part 1: Proof that Kuratowski Subgraphs are Non-Planar**

Let $G$ be a graph containing a subgraph $H \subseteq G$ such that $H$ is a subdivision of $K \in \{K_5, K_{3,3}\}$.
1. In Theorem 7.4, we proved from first principles that $K_5$ and $K_{3,3}$ are non-planar.
2. Consider an elementary subdivision of an edge $e = \{u, v\}$ into $\{u, w\}$ and $\{w, v\}$.
   If a graph $H$ has a planar embedding, placing vertex $w$ on the curve representing edge $e$ preserves the planar embedding.
   Conversely, if $H$ with vertex $w$ has a planar embedding, erasing the degree-2 vertex $w$ and joining the two curve segments preserves planarity.
   Therefore, **a graph is planar if and only if any subdivision of the graph is planar**.
3. Because $K_5$ and $K_{3,3}$ are non-planar, every subdivision of $K_5$ and every subdivision of $K_{3,3}$ is non-planar.
4. If $G$ contains a non-planar subgraph $H$, then $G$ cannot be planar (a planar embedding of $G$ would immediately restrict to a planar embedding of $H$).
Therefore, any graph containing a subdivision of $K_5$ or $K_{3,3}$ is **non-planar**. $\blacksquare$

---

**Part 2: $K_5$ Minor in the Petersen Graph**

The Petersen graph consists of:
- Outer 5-cycle: $V_{\text{out}} = \{u_0, u_1, u_2, u_3, u_4\}$ with edges $\{u_i, u_{i+1 \pmod 5}\}$.
- Inner 5-star: $V_{\text{in}} = \{v_0, v_1, v_2, v_3, v_4\}$ with edges $\{v_i, v_{i+2 \pmod 5}\}$.
- Five spoke edges connecting corresponding vertices: $E_{\text{spokes}} = \{ \{u_i, v_i\} : i = 0, \dots, 4 \}$.

**Edge Contraction Sequence:**
Contract each of the 5 spoke edges $\{u_0, v_0\}, \{u_1, v_1\}, \{u_2, v_2\}, \{u_3, v_3\}, \{u_4, v_4\}$:
- For each $i \in \{0, 1, 2, 3, 4\}$, contracting $\{u_i, v_i\}$ merges $u_i$ and $v_i$ into a single composite vertex $w_i$.
- What edges exist between the composite vertices $w_i$?
  - The outer cycle edges $\{u_i, u_{i+1}\}$ become edges between $w_i$ and $w_{i+1 \pmod 5}$.
  - The inner star edges $\{v_i, v_{i+2}\}$ become edges between $w_i$ and $w_{i+2 \pmod 5}$.
  - Together, for every pair of indices $i \ne j$, either $|i - j| \equiv 1 \pmod 5$ (an outer edge) or $|i - j| \equiv 2 \pmod 5$ (an inner edge)!
  - Every pair of distinct vertices $\{w_i, w_j\}$ ($0 \le i < j \le 4$) is connected by an edge!

The contracted graph has 5 vertices $\{w_0, w_1, w_2, w_3, w_4\}$, and every pair is connected by an edge.
This is precisely the complete graph $K_5$!
$$\text{Petersen} / E_{\text{spokes}} \cong K_5$$
By Wagner's Theorem (Theorem 7.6), because the Petersen graph contains $K_5$ as a minor, the Petersen graph is **non-planar**. $\blacksquare$"""
            }
        ]
    }
    return u7

if __name__ == "__main__":
    u = get_unit7()
    print("Unit 7 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
