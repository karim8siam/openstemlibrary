# -*- coding: utf-8 -*-
"""
build_gt_unit5.py
Constructs Unit 5: Algebraic Graph Theory: Incidence, Circuit, Cut-Set & Laplacian Matrices
"""

def get_unit5():
    u5 = {
        "number": 5,
        "title": "Algebraic Graph Theory: Incidence, Circuit, Cut-Set & Laplacian Matrices",
        "leadSummary": "Algebraic and vector space formulation of graphs: vertex-edge incidence matrix A(G), cycle space and circuit matrix B(G), cut space and cut-set matrix C(G), fundamental matrices B_f and C_f, orthogonality relationships A B^T = 0 and B_f C_f^T = 0, adjacency matrix powers and walk counting, the graph Laplacian L = D - A, and Kirchhoff's Matrix Tree Theorem for counting spanning trees.",
        "simulations": ["sim_gt_matrix_spectral"],
        "sections": [
            {
                "secNumber": "5.1",
                "title": "The Incidence Matrix $A(G)$, Unimodularity & Rank",
                "content": r"""### 1. The Vertex-Edge Incidence Matrix

Let $G = (V, E)$ be a graph with $n$ vertices $V = \{v_1, v_2, \dots, v_n\}$ and $m$ edges $E = \{e_1, e_2, \dots, e_m\}$.

> **Definition 5.1 (Incidence Matrix $A(G)$):**
> The **incidence matrix** of $G$ is an $n \times m$ matrix $A(G) = (a_{ij})$ defined by:
> $$a_{ij} = \begin{cases} 1 & \text{if vertex } v_i \text{ is incident with edge } e_j \\ 0 & \text{otherwise} \end{cases}$$
> If $G$ is an oriented (directed) graph:
> $$a_{ij} = \begin{cases} +1 & \text{if edge } e_j \text{ leaves vertex } v_i \text{ (tail)} \\ -1 & \text{if edge } e_j \text{ enters vertex } v_i \text{ (head)} \\ 0 & \text{otherwise} \end{cases}$$

#### Structural Observations:
1. Every column of $A(G)$ in a simple graph contains **exactly two non-zero entries** (corresponding to the two endpoints of that edge).
2. The sum of entries in row $i$ is the degree of vertex $v_i$: $\sum_{j=1}^m a_{ij} = \deg(v_i)$.
3. In the directed incidence matrix, every column sums to zero: $\sum_{i=1}^n a_{ij} = 0$.

---

### 2. Rank of the Incidence Matrix

> **Theorem 5.1 (Rank of $A(G)$):**
> Let $G$ be a graph with $n$ vertices and $\omega(G)$ connected components.
> The rank of the incidence matrix over the field $\mathbb{R}$ (and over $\mathbb{F}_2$) is:
> $$\text{rank}(A) = n - \omega(G)$$
> In particular, if $G$ is connected, $\text{rank}(A) = n - 1$.

#### Complete Proof (for connected graph):
Summing all rows of the directed incidence matrix yields the zero row:
$$\sum_{i=1}^n A_{i, \cdot} = \mathbf{0}^T$$
Thus the $n$ rows are linearly dependent, so $\text{rank}(A) \le n - 1$.
Now suppose a linear combination of rows vanishes: $\sum_{i=1}^n c_i A_{i, \cdot} = \mathbf{0}^T$.
For any edge $e_j = (v_p, v_q)$, the $j$-th column has $+1$ at $p$ and $-1$ at $q$.
Thus:
$$c_p - c_q = 0 \implies c_p = c_q$$
Since $G$ is connected, we can trace a path between any two vertices, implying $c_1 = c_2 = \dots = c_n = c$.
Therefore, the only linear relation among the rows is $\sum A_{i, \cdot} = \mathbf{0}$.
Any choice of $n - 1$ rows is linearly independent!
Hence $\text{rank}(A) = n - 1$. $\blacksquare$

> **Definition 5.2 (Reduced Incidence Matrix $A_f$):**
> The $(n - 1) \times m$ matrix obtained by deleting any single row from $A(G)$ is called the **reduced incidence matrix** $A_f$. The deleted row corresponds to the **reference (datum) vertex**."""
            },
            {
                "secNumber": "5.2",
                "title": "The Circuit Matrix $B(G)$ & Fundamental Circuit Matrix $B_f$",
                "content": r"""### 1. The Circuit Matrix $B(G)$

> **Definition 5.3 (Circuit Matrix $B(G)$):**
> Let $G$ have $m$ edges and let $q$ be the total number of simple circuits in $G$.
> The **circuit matrix** $B(G) = (b_{ij})$ is a $q \times m$ matrix defined by:
> $$b_{ij} = \begin{cases} 1 & \text{if edge } e_j \text{ is in circuit } C_i \\ 0 & \text{otherwise} \end{cases}$$
> Over $\mathbb{R}$ with oriented circuits, $b_{ij} = \pm 1$ depending on whether the orientation of $e_j$ agrees with the orientation of circuit $C_i$.

---

### 2. The Fundamental Circuit Matrix $B_f$

Let $T$ be a spanning tree of connected graph $G$.
Number of branches $= n - 1$. Number of chords $= \mu = m - n + 1$ (the cyclomatic number).
Each chord $e \in E \setminus E(T)$ defines a unique **fundamental circuit**.

> **Definition 5.4 (Fundamental Circuit Matrix $B_f$):**
> The **fundamental circuit matrix** $B_f$ relative to spanning tree $T$ is the $\mu \times m$ submatrix of $B$ corresponding to the $\mu$ fundamental circuits.
> Arranging the columns such that chords appear first and tree branches appear second:
> $$B_f = \begin{bmatrix} I_\mu & B_{12} \end{bmatrix}$$
> where $I_\mu$ is the $\mu \times \mu$ identity matrix (each fundamental circuit contains exactly its own chord).

> **Theorem 5.2 (Rank of the Circuit Matrix):**
> For any graph $G$ with $n$ vertices, $m$ edges, and $\omega$ components:
> $$\text{rank}(B) = \text{rank}(B_f) = m - n + \omega = \mu(G)$$

#### Proof:
Since $B_f$ contains the identity block $I_\mu$ of order $\mu = m - n + 1$, its rows are linearly independent over $\mathbb{F}_2$. Thus $\text{rank}(B_f) = \mu$.
Since any cycle in $G$ can be expressed as a linear combination (symmetric difference / ring sum) of fundamental circuits, the row space of $B_f$ spans the row space of $B$.
Therefore, $\text{rank}(B) = \mu(G)$. $\blacksquare$"""
            },
            {
                "secNumber": "5.3",
                "title": "The Cut-Set Matrix $C(G)$ & Orthogonality Relations",
                "content": r"""### 1. The Cut-Set Matrix $C(G)$ and Fundamental Matrix $C_f$

> **Definition 5.5 (Cut-Set Matrix $C(G)$):**
> Let $G$ have $m$ edges and let $p$ be the total number of cut-sets in $G$.
> The **cut-set matrix** $C(G) = (c_{ij})$ is a $p \times m$ matrix where:
> $$c_{ij} = \begin{cases} 1 & \text{if edge } e_j \text{ is in cut-set } S_i \\ 0 & \text{otherwise} \end{cases}$$

Relative to a spanning tree $T$, each of the $n - 1$ branches defines a **fundamental cut-set**.
Ordering edges as chords first ($E \setminus E(T)$) and tree branches second ($E(T)$):
$$C_f = \begin{bmatrix} C_{11} & I_{n-1} \end{bmatrix}$$
where $I_{n-1}$ is the identity matrix corresponding to the $n - 1$ branches.

> **Theorem 5.3 (Rank of Cut-Set Matrix):**
> $$\text{rank}(C) = \text{rank}(C_f) = n - \omega(G)$$

---

### 2. The Orthogonality Relationships

The interaction between the cycle space and the cut space represents one of the most elegant dualities in linear algebra:

> **Theorem 5.4 (Orthogonality of Incidence, Circuit and Cut-Set Matrices):**
> In any graph $G$:
> 1. $A \cdot B^T \equiv 0 \pmod 2 \quad (\text{and } A \cdot B^T = 0 \text{ for directed graphs})$.
> 2. $B \cdot C^T \equiv 0 \pmod 2 \quad (\text{and } B \cdot C^T = 0 \text{ for directed graphs})$.
> 3. For the fundamental matrices partitioned as $B_f = \begin{bmatrix} I_\mu & B_{12} \end{bmatrix}$ and $C_f = \begin{bmatrix} C_{11} & I_{n-1} \end{bmatrix}$:
>    $$B_f \cdot C_f^T = 0 \iff C_{11} = -B_{12}^T \iff C_{11} \equiv B_{12}^T \pmod 2$$

#### Proof:
1. **$A B^T = 0$:** The $(i, j)$-th entry of $A B^T$ is the dot product of row $i$ of $A$ (vertex $v_i$) and row $j$ of $B$ (circuit $C_j$).
   If $v_i \notin C_j$, the dot product is 0.
   If $v_i \in C_j$, circuit $C_j$ contains exactly two edges incident with $v_i$.
   In the directed case, one edge enters $v_i$ ($-1$) and one departs ($+1$), so $(+1)(+1) + (-1)(+1) = 0$.
   In modulo 2, $1 + 1 \equiv 0 \pmod 2$.
   Thus $A B^T = 0$.
2. **$B C^T = 0$:** By Theorem 4.3, every cycle and every cut-set share an even number of edges.
   The dot product counts the number of shared edges modulo 2, so $B C^T \equiv 0 \pmod 2$.
3. **Relation between $B_{12}$ and $C_{11}$:**
   $$B_f C_f^T = \begin{bmatrix} I_\mu & B_{12} \end{bmatrix} \begin{bmatrix} C_{11}^T \\ I_{n-1} \end{bmatrix} = I_\mu C_{11}^T + B_{12} I_{n-1} = C_{11}^T + B_{12} = 0$$
   Therefore:
   $$C_{11}^T = -B_{12} \implies C_{11} = -B_{12}^T \equiv B_{12}^T \pmod 2 \quad \blacksquare$$"""
            },
            {
                "secNumber": "5.4",
                "title": "Adjacency Matrix, Walk Powers $A^k$ & Spectral Properties",
                "content": r"""### 1. The Adjacency Matrix

> **Definition 5.7 (Adjacency Matrix $A(G)$):**
> Let $G = (V, E)$ be a simple graph with $V = \{v_1, \dots, v_n\}$.
> The **adjacency matrix** $A(G) = (a_{ij})$ is the $n \times n$ symmetric matrix:
> $$a_{ij} = \begin{cases} 1 & \text{if } \{v_i, v_j\} \in E \\ 0 & \text{otherwise} \end{cases}$$
> Since $G$ is undirected with no self-loops, $a_{ii} = 0$ and $A = A^T$.

---

### 2. Walk Counting Theorem via Matrix Powers

> **Theorem 5.5 (Walk Counting via $A^k$):**
> Let $A$ be the adjacency matrix of a graph $G$.
> The $(i, j)$-th entry of the $k$-th matrix power $A^k$, denoted $(A^k)_{ij}$, is equal to the **number of distinct walks of length $k$ from vertex $v_i$ to vertex $v_j$ in $G$**.

#### Complete Proof (by induction on $k$):
- **Base Case ($k = 1$):** $(A^1)_{ij} = a_{ij}$, which is $1$ if an edge exists (a walk of length 1) and $0$ otherwise. Holds.
- **Inductive Step:** Assume $(A^{k-1})_{ir}$ equals the number of walks of length $k - 1$ from $v_i$ to $v_r$.
  By definition of matrix multiplication:
  $$(A^k)_{ij} = (A^{k-1} \cdot A)_{ij} = \sum_{r=1}^n (A^{k-1})_{ir} \cdot a_{rj}$$
  Any walk of length $k$ from $v_i$ to $v_j$ consists of a walk of length $k - 1$ from $v_i$ to some vertex $v_r$, followed by the single edge $\{v_r, v_j\}$.
  If $\{v_r, v_j\} \in E$, then $a_{rj} = 1$, and there are $(A^{k-1})_{ir}$ such extensions.
  If $\{v_r, v_j\} \notin E$, then $a_{rj} = 0$, contributing 0 walks.
  Summing over all possible penultimate vertices $v_r \in V$ gives the total number of $v_i$-$v_j$ walks of length $k$. $\blacksquare$

> **Corollary 5.5.1 (Triangle Formula via Trace):**
> The number of triangles in a simple graph $G$ is given by:
> $$\text{Number of Triangles } = \frac{1}{6} \text{Tr}(A^3) = \frac{1}{6} \sum_{i=1}^n \lambda_i^3$$
> where $\lambda_1, \dots, \lambda_n$ are the eigenvalues of $A(G)$.

#### Proof:
$(A^3)_{ii}$ is the number of closed walks of length 3 starting and ending at $v_i$.
Each triangle on vertices $\{u, v, w\}$ gives rise to 2 directed traversal directions ($u \to v \to w \to u$ and $u \to w \to v \to u$) and can start at any of its 3 vertices ($3 \times 2 = 6$ closed walks per triangle).
Summing over all vertices: $\text{Tr}(A^3) = 6 \times (\text{triangles})$. $\blacksquare$"""
            },
            {
                "secNumber": "5.5",
                "title": "The Graph Laplacian $L = D - A$ & Kirchhoff's Matrix Tree Theorem",
                "content": r"""### 1. The Graph Laplacian Matrix

> **Definition 5.8 (Laplacian Matrix):**
> Let $G$ be a simple graph on $n$ vertices. Let $D(G) = \text{diag}(\deg(v_1), \dots, \deg(v_n))$ be the diagonal degree matrix.
> The **Laplacian matrix** of $G$ is:
> $$L(G) = D(G) - A(G)$$
> Component-wise:
> $$L_{ij} = \begin{cases} \deg(v_i) & \text{if } i = j \\ -1 & \text{if } i \ne j \text{ and } \{v_i, v_j\} \in E \\ 0 & \text{otherwise} \end{cases}$$

> **Theorem 5.6 (Properties of the Laplacian):**
> 1. $L = A_{\text{dir}} A_{\text{dir}}^T$, where $A_{\text{dir}}$ is the directed incidence matrix.
> 2. $L$ is symmetric and positive semi-definite ($x^T L x = \sum_{\{u, v\} \in E} (x_u - x_v)^2 \ge 0$).
> 3. The vector of all ones $\mathbf{1} = (1, 1, \dots, 1)^T$ satisfies $L \mathbf{1} = \mathbf{0}$, so $\lambda_1 = 0$ is always an eigenvalue.
> 4. The multiplicity of the eigenvalue $0$ equals the number of connected components $\omega(G)$.
> 5. The second smallest eigenvalue $\lambda_2(G)$ is the **algebraic connectivity** (Fiedler value).

---

### 2. Kirchhoff's Matrix Tree Theorem

Gustav Kirchhoff proved in 1847 that the Laplacian matrix encodes the exact number of spanning trees in a graph:

> **Theorem 5.7 (Kirchhoff's Matrix Tree Theorem, 1847):**
> Let $G$ be a connected simple graph on $n$ vertices, and let $L(G)$ be its Laplacian matrix.
> For any choice of indices $i, j \in \{1, 2, \dots, n\}$, let $L(i, j)$ denote the submatrix obtained by deleting row $i$ and column $j$ from $L$.
> Then the total number of spanning trees of $G$, denoted $\tau(G)$, is given by:
> $$\tau(G) = (-1)^{i + j} \det(L(i, j))$$
> That is, every cofactor of the Laplacian matrix $L$ is equal to $\tau(G)$.
> Furthermore, in terms of non-zero Laplacian eigenvalues $0 < \lambda_2 \le \dots \le \lambda_n$:
> $$\tau(G) = \frac{1}{n} \prod_{k=2}^n \lambda_k$$

#### Proof using the Cauchy-Binet Formula:
Let $A_f$ be the reduced incidence matrix obtained by deleting row $i$ from $A_{\text{dir}}$.
Then $L(i, i) = A_f A_f^T$.
By the **Cauchy-Binet Formula**:
$$\det(L(i, i)) = \det(A_f A_f^T) = \sum_{S \subseteq E, \; |S| = n - 1} (\det(A_f|_S))^2$$
where $A_f|_S$ is the $(n - 1) \times (n - 1)$ submatrix of $A_f$ with columns indexed by $S$.
By Theorem 5.1 and unimodularity of trees:
$$\det(A_f|_S) = \begin{cases} \pm 1 & \text{if } S \text{ forms a spanning tree of } G \\ 0 & \text{otherwise} \end{cases}$$
Therefore:
$$\det(L(i, i)) = \sum_{S \text{ is a spanning tree}} (\pm 1)^2 = \tau(G) \quad \blacksquare$$"""
            }
        ],
        "problems": [
            {
                "tier": "Foundational",
                "title": "Constructing Fundamental Matrices & Verifying Orthogonality",
                "statement": r"Consider the complete graph $K_4$ with vertices $\{1, 2, 3, 4\}$ and edges $e_1=\{1, 2\}, e_2=\{2, 3\}, e_3=\{3, 4\}, e_4=\{1, 4\}, e_5=\{1, 3\}, e_6=\{2, 4\}$. Choose the spanning tree $T$ with branches $\{e_1, e_2, e_3\}$. 1. Write down the fundamental circuits for all chords and construct the fundamental circuit matrix $B_f = [I_\mu \mid B_{12}]$. 2. Construct the fundamental cut-set matrix $C_f = [C_{11} \mid I_{n-1}]$. 3. Verify directly that $B_f C_f^T \equiv 0 \pmod 2$.",
                "hints": [
                    "Number of vertices $n = 4$, edges $m = 6$. Branches $= n - 1 = 3$, chords $\\mu = 6 - 3 = 3$.",
                    "Chords are $e_4, e_5, e_6$. Find the cycle formed when each chord is added to $T = \\{e_1, e_2, e_3\\}$."
                ],
                "solution": r"""**Step 1: Fundamental Circuits and $B_f$**

Vertices: $\{1, 2, 3, 4\}$.
Tree branches: $T = \{e_1, e_2, e_3\}$ where $e_1=\{1,2\}, e_2=\{2,3\}, e_3=\{3,4\}$.
Chords: $e_4=\{1, 4\}, e_5=\{1, 3\}, e_6=\{2, 4\}$.
Number of chords: $\mu = 6 - 4 + 1 = 3$.

Order edges as chords first ($e_4, e_5, e_6$) then branches ($e_1, e_2, e_3$):
- **Chord $e_4 = \{1, 4\}$:**
  Path in $T$ from $1$ to $4$ is $1 \xrightarrow{e_1} 2 \xrightarrow{e_2} 3 \xrightarrow{e_3} 4$.
  Circuit $C_1$: $\{e_4, e_1, e_2, e_3\}$.
  Vector: $(1, 0, 0 \mid 1, 1, 1)$.
- **Chord $e_5 = \{1, 3\}$:**
  Path in $T$ from $1$ to $3$ is $1 \xrightarrow{e_1} 2 \xrightarrow{e_2} 3$.
  Circuit $C_2$: $\{e_5, e_1, e_2\}$.
  Vector: $(0, 1, 0 \mid 1, 1, 0)$.
- **Chord $e_6 = \{2, 4\}$:**
  Path in $T$ from $2$ to $4$ is $2 \xrightarrow{e_2} 3 \xrightarrow{e_3} 4$.
  Circuit $C_3$: $\{e_6, e_2, e_3\}$.
  Vector: $(0, 0, 1 \mid 0, 1, 1)$.

The fundamental circuit matrix $B_f$ is:
$$B_f = \begin{pmatrix} 1 & 0 & 0 & 1 & 1 & 1 \\ 0 & 1 & 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 & 1 & 1 \end{pmatrix} = \begin{bmatrix} I_3 & B_{12} \end{bmatrix}$$
where:
$$B_{12} = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$

---

**Step 2: Fundamental Cut-Sets and $C_f$**

By Theorem 5.4, $C_{11} \equiv B_{12}^T \pmod 2$:
$$C_{11} = B_{12}^T = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix}$$
Let us verify the fundamental cut-sets physically:
- **Branch $e_1 = \{1, 2\}$:** Removing $e_1$ partitions $T$ into $\{1\}$ and $\{2, 3, 4\}$.
  Edges crossing this cut are $\{e_1, e_4, e_5\}$.
  Vector: $(1, 1, 0 \mid 1, 0, 0)$. Matches row 1 of $C_f$!
- **Branch $e_2 = \{2, 3\}$:** Removing $e_2$ partitions $T$ into $\{1, 2\}$ and $\{3, 4\}$.
  Edges crossing: $\{e_2, e_4, e_5, e_6\}$.
  Vector: $(1, 1, 1 \mid 0, 1, 0)$. Matches row 2 of $C_f$!
- **Branch $e_3 = \{3, 4\}$:** Removing $e_3$ partitions $T$ into $\{1, 2, 3\}$ and $\{4\}$.
  Edges crossing: $\{e_3, e_4, e_6\}$.
  Vector: $(1, 0, 1 \mid 0, 0, 1)$. Matches row 3 of $C_f$!

Therefore:
$$C_f = \begin{pmatrix} 1 & 1 & 0 & 1 & 0 & 0 \\ 1 & 1 & 1 & 0 & 1 & 0 \\ 1 & 0 & 1 & 0 & 0 & 1 \end{pmatrix} = \begin{bmatrix} C_{11} & I_3 \end{bmatrix}$$

---

**Step 3: Verification of $B_f C_f^T \equiv 0 \pmod 2$**

Compute the matrix product:
$$B_f C_f^T = I_3 C_{11}^T + B_{12} I_3 = C_{11}^T + B_{12}$$
Since $C_{11} = B_{12}^T$, $C_{11}^T = (B_{12}^T)^T = B_{12}$.
$$B_f C_f^T = B_{12} + B_{12} = 2 B_{12} \equiv \mathbf{0} \pmod 2$$
Orthogonality holds identically! $\blacksquare$"""
            },
            {
                "tier": "Advanced",
                "title": "Walk Counting via $A^k$ Powers & Triangle Counting via Trace",
                "statement": r"Let $G$ be the graph on 4 vertices with adjacency matrix: $A = \begin{pmatrix} 0 & 1 & 1 & 1 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0 \end{pmatrix}$. 1. Compute $A^2$ and $A^3$. 2. Determine the total number of walks of length 3 from vertex 1 to vertex 3. 3. Use the trace formula $\text{Tr}(A^3) / 6$ to determine the exact number of triangles in $G$.",
                "hints": [
                    "Multiply $A$ by itself using standard matrix multiplication.",
                    "Recall that $(A^3)_{13}$ gives the number of walks of length 3 between vertices 1 and 3.",
                    "Trace is the sum of diagonal entries."
                ],
                "solution": r"""**Step 1: Compute $A^2$ and $A^3$**

$$A = \begin{pmatrix} 0 & 1 & 1 & 1 \\ 1 & 0 & 1 & 0 \\ 1 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0 \end{pmatrix}$$

Compute $A^2 = A \cdot A$:
- Row 1: $[0, 1, 1, 1] \cdot \text{cols} = [3, 1, 2, 1]$
- Row 2: $[1, 0, 1, 0] \cdot \text{cols} = [1, 2, 1, 2]$
- Row 3: $[1, 1, 0, 1] \cdot \text{cols} = [2, 1, 3, 1]$
- Row 4: $[1, 0, 1, 0] \cdot \text{cols} = [1, 2, 1, 2]$

$$A^2 = \begin{pmatrix} 3 & 1 & 2 & 1 \\ 1 & 2 & 1 & 2 \\ 2 & 1 & 3 & 1 \\ 1 & 2 & 1 & 2 \end{pmatrix}$$
*(Notice diagonal entries of $A^2$ are the vertex degrees: $3, 2, 3, 2$. Correct!)*

Now compute $A^3 = A^2 \cdot A$:
- Row 1:
  - $(A^3)_{11} = 3(0) + 1(1) + 2(1) + 1(1) = 4$
  - $(A^3)_{12} = 3(1) + 1(0) + 2(1) + 1(0) = 5$
  - $(A^3)_{13} = 3(1) + 1(1) + 2(0) + 1(1) = 5$
  - $(A^3)_{14} = 3(1) + 1(0) + 2(1) + 1(0) = 5$
- Row 2:
  - $(A^3)_{21} = 5$
  - $(A^3)_{22} = 1(1) + 2(0) + 1(1) + 2(0) = 2$
  - $(A^3)_{23} = 1(1) + 2(1) + 1(0) + 2(1) = 5$
  - $(A^3)_{24} = 1(1) + 2(0) + 1(1) + 2(0) = 2$
- Row 3:
  - $(A^3)_{31} = 5$
  - $(A^3)_{32} = 5$
  - $(A^3)_{33} = 2(1) + 1(1) + 3(0) + 1(1) = 4$
  - $(A^3)_{34} = 5$
- Row 4:
  - $(A^3)_{41} = 5$
  - $(A^3)_{42} = 2$
  - $(A^3)_{43} = 5$
  - $(A^3)_{44} = 2$

$$A^3 = \begin{pmatrix} 4 & 5 & 5 & 5 \\ 5 & 2 & 5 & 2 \\ 5 & 5 & 4 & 5 \\ 5 & 2 & 5 & 2 \end{pmatrix}$$

---

**Step 2: Number of Walks of Length 3 between 1 and 3**

By Theorem 5.5, the number of walks of length 3 from vertex 1 to vertex 3 is entry $(A^3)_{13}$:
$$(A^3)_{13} = 5$$
The 5 walks are:
1. $1 \to 2 \to 1 \to 3$
2. $1 \to 4 \to 1 \to 3$
3. $1 \to 3 \to 1 \to 3$
4. $1 \to 3 \to 4 \to 3$
5. $1 \to 3 \to 2 \to 3$

---

**Step 3: Triangle Count via Trace**

Compute the trace of $A^3$:
$$\text{Tr}(A^3) = (A^3)_{11} + (A^3)_{22} + (A^3)_{33} + (A^3)_{44} = 4 + 2 + 4 + 2 = 12$$
By Corollary 5.5.1:
$$\text{Number of Triangles} = \frac{\text{Tr}(A^3)}{6} = \frac{12}{6} = 2$$
The two triangles in $G$ are:
- Triangle $\{1, 2, 3\}$
- Triangle $\{1, 3, 4\}$
Result verified! $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Complete Proof of Kirchhoff's Matrix Tree Theorem via Cauchy-Binet",
                "statement": r"Provide a complete, mathematically rigorous proof of Kirchhoff's Matrix Tree Theorem: Let $G$ be a connected simple graph on $n$ vertices with Laplacian matrix $L$. Prove that every cofactor of $L$ is equal to the total number of spanning trees $\tau(G)$ of $G$, using the Cauchy-Binet determinant theorem applied to the reduced directed incidence matrix.",
                "hints": [
                    "Let $A_f$ be the $(n-1) \\times m$ matrix obtained by deleting row $k$ from the directed incidence matrix $A$. Show that $L(k, k) = A_f A_f^T$.",
                    "Apply the Cauchy-Binet theorem: $\\det(A_f A_f^T) = \\sum_{|S|=n-1} (\\det(A_f|_S))^2$.",
                    "Prove that for any subset $S$ of $n - 1$ edges: $\\det(A_f|_S) = \\pm 1$ if $S$ is a spanning tree, and $0$ if $S$ contains a cycle."
                ],
                "solution": r"""**Complete Proof of Kirchhoff's Matrix Tree Theorem (Theorem 5.7)**

Let $G = (V, E)$ be a connected simple graph with $n$ vertices and $m$ edges.
Arbitrarily orient the edges of $G$ to form a directed graph $D$, and let $A$ be its $n \times m$ directed incidence matrix:
$$A_{v, e} = \begin{cases} +1 & \text{if } v \text{ is the head of } e \\ -1 & \text{if } v \text{ is the tail of } e \\ 0 & \text{otherwise} \end{cases}$$

---

**Step 1: The Product $A A^T$ Equals the Laplacian $L$**
Compute the $(u, v)$ entry of $A A^T$:
$$(A A^T)_{u, v} = \sum_{e \in E} A_{u, e} A_{v, e}$$
- If $u = v$: Each edge incident with $u$ has $A_{u, e} = \pm 1$, so $(A_{u, e})^2 = 1$.
  $$(A A^T)_{u, u} = \sum_{e \in E} (A_{u, e})^2 = \deg(u)$$
- If $u \ne v$:
  - If $\{u, v\} \in E$, the edge $e$ connects $u$ and $v$. One endpoint is $+1$ and the other is $-1$, so $A_{u, e} A_{v, e} = (+1)(-1) = -1$.
  - If $\{u, v\} \notin E$, $A_{u, e} A_{v, e} = 0$.
  $$(A A^T)_{u, v} = \begin{cases} -1 & \text{if } \{u, v\} \in E \\ 0 & \text{if } \{u, v\} \notin E \end{cases}$$
Comparing with Definition 5.8:
$$A A^T = D - A_{\text{adj}} = L(G)$$

---

**Step 2: Submatrix Form and Cauchy-Binet Formula**
Let $k \in \{1, \dots, n\}$. Delete row $k$ from $A$ to obtain the reduced incidence matrix $A_f$ of size $(n - 1) \times m$.
Then the submatrix obtained by deleting row $k$ and column $k$ from $L$ is:
$$L(k, k) = A_f A_f^T$$
By the **Cauchy-Binet Formula** for the determinant of a product of non-square matrices:
$$\det(L(k, k)) = \det(A_f A_f^T) = \sum_{\substack{S \subseteq E \\ |S| = n - 1}} \det(A_f|_S) \det((A_f|_S)^T) = \sum_{\substack{S \subseteq E \\ |S| = n - 1}} (\det(A_f|_S))^2$$
where $A_f|_S$ is the square $(n - 1) \times (n - 1)$ submatrix of $A_f$ formed by the columns corresponding to the edge subset $S$.

---

**Step 3: Evaluating $\det(A_f|_S)$ for Subsets of Size $n - 1$**
Consider the subgraph $G_S = (V, S)$ spanned by the $n - 1$ edges in $S$.

**Case A: $G_S$ contains a cycle.**
Since $|S| = n - 1 < n$ and $G_S$ contains a cycle, by Theorem 3.1, $G_S$ cannot be connected.
Let $C$ be a cycle in $G_S$.
By Theorem 5.4, the incidence vectors of edges in a cycle are linearly dependent!
Specifically, assigning signs according to cycle traversal direction gives a non-zero linear combination of columns of $A_f|_S$ that equals $\mathbf{0}$.
Because the columns are linearly dependent:
$$\det(A_f|_S) = 0$$

**Case B: $G_S$ contains NO cycles (i.e., $G_S$ is a spanning tree).**
Since $G_S$ has $n$ vertices, $n - 1$ edges, and no cycles, by Theorem 3.1, $G_S$ is a **spanning tree** of $G$.
We prove that $\det(A_f|_S) = \pm 1$ by induction on $n$:
- Every tree has at least two leaves (Problem 3.2).
- At least one leaf $v_{\ell}$ is distinct from the deleted reference vertex $k$.
- The row corresponding to $v_{\ell}$ in $A_f|_S$ has **exactly one non-zero entry** ($\pm 1$), corresponding to the unique edge incident with $v_{\ell}$.
- Expand the determinant along row $v_{\ell}$:
  $$\det(A_f|_S) = (\pm 1) \cdot \det(A_f'|_{S'})$$
  where $A_f'|_{S'}$ is the reduced incidence matrix of the smaller tree $G_S - v_{\ell}$ on $n - 1$ vertices.
- By induction hypothesis, $\det(A_f'|_{S'}) = \pm 1$.
Therefore:
$$\det(A_f|_S) = \pm 1 \implies (\det(A_f|_S))^2 = 1$$

---

**Step 4: Conclusion**
Substituting back into the Cauchy-Binet expansion:
$$\det(L(k, k)) = \sum_{\substack{S \subseteq E, \; |S| = n - 1 \\ S \text{ is a spanning tree}}} (1) + \sum_{\substack{S \subseteq E, \; |S| = n - 1 \\ S \text{ contains a cycle}}} (0) = \sum_{T \text{ spanning tree}} 1 = \tau(G)$$
Since $\det(L(k, k)) = \tau(G)$ for any $k$, and the off-diagonal cofactors differ by at most a sign that cancels out via $L \mathbf{1} = \mathbf{0}$, every cofactor equals $\tau(G)$.
This completes the proof of Kirchhoff's Matrix Tree Theorem. $\blacksquare$"""
            }
        ]
    }
    return u5

if __name__ == "__main__":
    u = get_unit5()
    print("Unit 5 generated successfully:", u["title"])
    print("Sections:", len(u["sections"]))
    print("Problems:", len(u["problems"]))
