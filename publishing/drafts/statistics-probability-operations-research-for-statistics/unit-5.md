# Unit 5: Network Optimization: Shortest Path, Minimum Spanning Trees, Max-Flow Min-Cut & CPM/PERT

## 5.1 Graph-Theoretic Foundations of Network Flow Models and Node-Arc Incidence Matrices

Network optimization constitutes one of the most computationally tractable and practically pervasive branches of operations research and statistical systems analysis. Whereas general linear programming models require iterative algebraic matrix inversions whose computational complexity scales polynomially with the dimension of the constraint space, network flow models exploit the underlying topological geometry of directed and undirected graphs to achieve dramatic algorithmic speedups. Even more remarkably, the algebraic structure of network flow constraints guarantees that whenever external node supplies, demands, and arc capacities are specified as integers, every basic feasible solution—and consequently every extreme-point optimal solution—is automatically integral without requiring integer programming branch-and-bound enumeration. In statistical applications, network optimization underpins Markov chain transition routing, minimum-variance graphical model spanning trees, maximum-likelihood sequence decoding via dynamic Viterbi paths, optimal experimental matched-pair assignment, and complex multi-stage research project scheduling.

Formally, a directed network (or digraph) is an ordered mathematical tuple $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ consisting of a finite set of vertices or nodes $\mathcal{V} = \{1, 2, \dots, m\}$ with cardinality $|\mathcal{V}| = m$, and a finite collection of directed arcs or edges $\mathcal{E} \subseteq \mathcal{V} \times \mathcal{V}$ with cardinality $|\mathcal{E}| = n$. Each directed arc $e_k = (i, j) \in \mathcal{E}$ originates at a tail node $i \in \mathcal{V}$ and terminates at a head node $j \in \mathcal{V}$, permitting commodity flow, information transmission, or state progression strictly from node $i$ to node $j$. For any node $i \in \mathcal{V}$, we define its forward star (or outgoing arc set) as $\delta^+(i) = \{(i, j) \in \mathcal{E} : j \in \mathcal{V}\}$ and its backward star (or incoming arc set) as $\delta^-(i) = \{(k, i) \in \mathcal{E} : k \in \mathcal{V}\}$. The out-degree $d^+(i) = |\delta^+(i)|$ and in-degree $d^-(i) = |\delta^-(i)|$ quantify the local branching connectivity of node $i$. A directed walk is an alternating sequence of nodes and arcs $v_0, (v_0, v_1), v_1, \dots, (v_{r-1}, v_r), v_r$; when all visited nodes $v_0, v_1, \dots, v_r$ are pairwise distinct, the walk is termed a directed path. If $v_0 = v_r$ and the intermediate nodes are distinct, the structure forms a directed cycle. A network is said to be connected if the underlying undirected graph contains a path between every pair of distinct nodes, and strongly connected if a directed path exists from every node $i$ to every other node $j$. A connected undirected graph containing no cycles is defined as a tree; any tree spanning $m$ vertices necessarily contains exactly $m - 1$ edges, and the addition of a single non-tree edge creates a unique fundamental cycle.

To unify shortest-path routing, transportation logistics, transshipment distribution, and maximal flow problems within a single canonical algebraic framework, operations researchers formulate the **Minimum-Cost Network Flow Problem (MCNFP)**. Associate with each directed arc $(i, j) \in \mathcal{E}$ a non-negative decision variable $x_{ij} \ge 0$ representing the volume of flow traversing arc $(i, j)$, a unit flow traversal cost $c_{ij} \in \mathbb{R}$, a lower flow capacity bound $l_{ij} \ge 0$ (typically normalized to zero via variable translation), and an upper capacity bound $u_{ij} \in (0, \infty]$. Furthermore, associate with each node $i \in \mathcal{V}$ an external net supply scalar $b_i \in \mathbb{R}$. By convention, if $b_i > 0$, node $i$ acts as a source or supply origin injecting $b_i$ units of commodity into the network; if $b_i < 0$, node $i$ functions as a sink or demand destination absorbing $|b_i| = -b_i$ units of flow; and if $b_i = 0$, node $i$ serves as a pure intermediate transshipment relay where total incoming flow must exactly equal total outgoing flow. The canonical linear programming formulation of the Minimum-Cost Network Flow Problem seeks to minimize aggregate traversal expenditure subject to nodal flow conservation and arc capacity bounds:

$$
\min_{x} \quad Z = \sum_{(i, j) \in \mathcal{E}} c_{ij} x_{ij}
$$

$$
\text{subject to} \quad \sum_{j : (i, j) \in \delta^+(i)} x_{ij} - \sum_{k : (k, i) \in \delta^-(i)} x_{ki} = b_i \quad \forall i \in \mathcal{V}
$$

$$
0 \le x_{ij} \le u_{ij} \quad \forall (i, j) \in \mathcal{E}
$$

The structural properties of this linear program become transparent when expressed in matrix notation using the **node-arc incidence matrix** $\mathbf{A} \in \{-1, 0, +1\}^{m \times n}$. Each row $i \in \{1, \dots, m\}$ of $\mathbf{A}$ corresponds to a node $i \in \mathcal{V}$, and each column $e_k = (p, q) \in \{1, \dots, n\}$ corresponds to a directed arc from tail node $p$ to head node $q$. The matrix entry $a_{i, e_k}$ is defined rigorously as:

$$
a_{i, (p, q)} = \begin{cases} +1 & \text{if } i = p \text{ (arc } (p, q) \text{ leaves node } i\text{)} \\ -1 & \text{if } i = q \text{ (arc } (p, q) \text{ enters node } i\text{)} \\ 0 & \text{otherwise} \end{cases}
$$

With this incidence matrix construction, the nodal flow conservation equations take the compact matrix form $\mathbf{A}\mathbf{x} = \mathbf{b}$, subject to $\mathbf{0} \le \mathbf{x} \le \mathbf{u}$. Because every column of $\mathbf{A}$ possesses exactly one $+1$ entry (at its tail row) and exactly one $-1$ entry (at its head row), summing all $m$ rows of $\mathbf{A}$ yields the zero row vector $\mathbf{1}_m^\top \mathbf{A} = \mathbf{0}_n^\top$. Consequently, the rows of $\mathbf{A}$ are linearly dependent, and $\text{rank}(\mathbf{A}) \le m - 1$. For a connected network with $m$ nodes, $\text{rank}(\mathbf{A}) = m - 1$, implying that a feasibility prerequisite for $\mathbf{A}\mathbf{x} = \mathbf{b}$ is global flow balance across the network:

$$
\mathbf{1}_m^\top \mathbf{A}\mathbf{x} = \mathbf{1}_m^\top \mathbf{b} = \sum_{i=1}^m b_i = 0
$$

Moreover, removing any arbitrary reference row (often the sink node $m$, fixing its dual potential $\pi_m = 0$) leaves an $(m-1) \times n$ full-row-rank matrix. Crucially, by Poincaré's theorem on incidence matrices, $\mathbf{A}$ is **totally unimodular (TU)**: every square submatrix $\mathbf{M}$ of $\mathbf{A}$ has determinant $\det(\mathbf{M}) \in \{-1, 0, +1\}$. We establish this by induction on the order $k$ of the square submatrix $\mathbf{M}$. For $k=1$, every entry of $\mathbf{A}$ is in $\{-1, 0, +1\}$. Assume the property holds for all square submatrices of order $k-1$, and consider a $k \times k$ submatrix $\mathbf{M}$. Since each column of $\mathbf{A}$ has at most one $+1$ and one $-1$, every column of $\mathbf{M}$ contains at most two non-zero entries. Three exhaustive cases arise: (1) if $\mathbf{M}$ contains a column of all zeros, then $\det(\mathbf{M}) = 0$; (2) if every column of $\mathbf{M}$ contains both a $+1$ and a $-1$, then the sum of all rows of $\mathbf{M}$ is the zero vector, rendering $\mathbf{M}$ singular with $\det(\mathbf{M}) = 0$; (3) otherwise, at least one column $c^*$ of $\mathbf{M}$ contains exactly one non-zero entry $\pm 1$ in some row $r^*$. Expanding $\det(\mathbf{M})$ by cofactors along column $c^*$ yields $\det(\mathbf{M}) = (\pm 1)(-1)^{r^*+c^*} \det(\mathbf{M}_{-r^*, -c^*})$, which by the inductive hypothesis belongs to $\{-1, 0, +1\}$. By Cramer's rule, for any basis matrix $\mathbf{B}$ of order $m-1$ extracted from $\mathbf{A}$ (which graphically corresponds to a spanning tree of $\mathcal{G}$), $\mathbf{B}^{-1} = \frac{1}{\det(\mathbf{B})} \text{adj}(\mathbf{B}) = \pm \text{adj}(\mathbf{B})$ is purely integral. Therefore, for any integral supply/demand vector $\mathbf{b} \in \mathbb{Z}^m$ and integral capacity vector $\mathbf{u} \in \mathbb{Z}^n$, every basic feasible solution $\mathbf{x}_B = \mathbf{B}^{-1}\mathbf{b}$ is strictly integer-valued.

## 5.2 Shortest-Path Optimization: Dijkstra's Labeling Algorithm and Bellman-Ford Dynamic Equations

The **Shortest-Path Problem** seeks a directed path from a designated source node $s \in \mathcal{V}$ to a destination node $t \in \mathcal{V}$ (or simultaneously from $s$ to all other nodes $i \in \mathcal{V} \setminus \{s\}$) that minimizes the cumulative sum of arc weights $c_{ij}$ along the path. Within the canonical Minimum-Cost Network Flow framework of Section 5.1, the single-source all-destinations shortest-path problem corresponds to setting $b_s = m - 1$ at the origin node $s$, setting $b_i = -1$ at every other node $i \in \mathcal{V} \setminus \{s\}$, and removing upper arc capacities ($u_{ij} = \infty$). In this formulation, one unit of flow is dispatched from the source $s$ along a minimum-cost path to each of the $m-1$ destinations, and the union of basic arcs carrying positive flow forms a **shortest-path arborescence** (a directed spanning tree rooted at $s$). If we seek only the shortest path from $s$ to a single sink $t$, we set $b_s = +1$, $b_t = -1$, and $b_i = 0$ for all intermediate nodes $i \notin \{s, t\}$. Associated with the primal shortest-path linear program is its linear programming dual: letting $\pi_i$ denote the unrestricted dual variable (termed the **node potential** or shortest-path distance label $d_i$) for node $i$, dual feasibility requires $\pi_j - \pi_i \le c_{ij}$, or equivalently:

$$
d_j \le d_i + c_{ij} \quad \forall (i, j) \in \mathcal{E}
$$

When $d_s = 0$, these dual constraints represent **Bellman's optimality equations**: at optimality, the shortest distance $d_j$ to node $j$ cannot exceed the shortest distance $d_i$ to any predecessor node $i$ plus the direct transition cost $c_{ij}$, with strict equality $d_j = d_i + c_{ij}$ holding along every arc $(i, j)$ that belongs to the shortest-path tree (by complementary slackness, since $x_{ij} > 0 \implies d_j - d_i = c_{ij}$).

When all arc weights are strictly non-negative ($c_{ij} \ge 0$ for all $(i, j) \in \mathcal{E}$), **Dijkstra's Labeling Algorithm** (formulated by Edsger W. Dijkstra in 1959) determines the shortest paths from source $s$ to all nodes in $\mathcal{V}$ via a greedy label-setting strategy. The algorithm partitions the vertex set $\mathcal{V}$ at each iteration into two complementary subsets: a permanently labeled set $\mathcal{S} \subseteq \mathcal{V}$ of nodes whose exact shortest-path distances $d_i$ from $s$ have been finalized, and a tentatively labeled set $\bar{\mathcal{S}} = \mathcal{V} \setminus \mathcal{S}$ of nodes whose current distance estimates $u_i$ represent the shortest path from $s$ to $i$ restricted exclusively to intermediate nodes within $\mathcal{S}$. Each node $i$ carries a two-component label $[u_i, p_i]$, where $u_i \in [0, \infty]$ denotes the cumulative distance from $s$ and $p_i \in \mathcal{V}$ records the immediate predecessor node along the best path discovered thus far.

The execution of Dijkstra's algorithm proceeds through three rigorous phases:
1. **Initialization**: Assign the source node $s$ a permanent distance label $u_s = 0$ with predecessor $p_s = \text{null}$, and initialize $\mathcal{S} = \emptyset$, $\bar{\mathcal{S}} = \mathcal{V}$. For every other node $i \in \mathcal{V} \setminus \{s\}$, set the tentative distance label $u_i = +\infty$ and $p_i = \text{null}$.
2. **Greedy Node Selection (Label Setting)**: Among all currently temporary nodes in $\bar{\mathcal{S}}$, identify the node $i^*$ possessing the minimum tentative distance label:

$$
i^* = \arg\min_{i \in \bar{\mathcal{S}}} \{u_i\}
$$

Transfer $i^*$ from the tentative set $\bar{\mathcal{S}}$ into the permanent set $\mathcal{S}$ ($\mathcal{S} \leftarrow \mathcal{S} \cup \{i^*\}$, $\bar{\mathcal{S}} \leftarrow \bar{\mathcal{S}} \setminus \{i^*\}$). If $\bar{\mathcal{S}} = \emptyset$ or $u_{i^*} = +\infty$, terminate the algorithm.
3. **Edge Relaxation (Label Updating)**: For every outgoing arc $(i^*, j) \in \delta^+(i^*)$ leading to a still-tentative neighbor $j \in \bar{\mathcal{S}}$, test whether routing through $i^*$ improves the current distance estimate to $j$. Specifically, update the label of node $j$ according to the relaxation operator:

$$
u_j \leftarrow \min\left\{u_j, \; u_{i^*} + c_{i^* j}\right\}
$$

If $u_{i^*} + c_{i^* j} < u_j$, overwrite $u_j \leftarrow u_{i^*} + c_{i^* j}$ and set the predecessor pointer $p_j \leftarrow i^*$. Return to Step 2 until all nodes are permanently labeled.

To prove the correctness of Dijkstra's algorithm by mathematical induction on $|\mathcal{S}|$, suppose all nodes currently in $\mathcal{S}$ hold their true shortest-path distances $d_k = u_k$, and let $i^* = \arg\min_{i \in \bar{\mathcal{S}}} u_i$ be selected next. Suppose by way of contradiction that the true shortest path $P^*$ from $s$ to $i^*$ has length $d_{i^*} < u_{i^*}$. Since $s \in \mathcal{S}$ and $i^* \in \bar{\mathcal{S}}$, path $P^*$ must exit $\mathcal{S}$ for the first time along some arc $(x, y)$ with $x \in \mathcal{S}$ and $y \in \bar{\mathcal{S}}$. Because $x$ was previously added to $\mathcal{S}$ and all its outgoing arcs were relaxed, node $y$ satisfies $u_y \le d_x + c_{xy} = d_y$. Moreover, since the sub-path of $P^*$ from $y$ to $i^*$ consists exclusively of arcs with non-negative weights ($c_{uv} \ge 0$), the total length of $P^*$ satisfies $d_{i^*} = d_y + \text{length}(y \to i^*) \ge d_y \ge u_y$. However, because $i^*$ was chosen to minimize $u_i$ over $\bar{\mathcal{S}}$, we have $u_y \ge u_{i^*}$, yielding $d_{i^*} \ge u_{i^*}$, a contradiction. Thus $u_{i^*} = d_{i^*}$. Notice where non-negativity $c_{uv} \ge 0$ is indispensable: if a subsequent arc $(y, i^*)$ had a negative weight $c_{y i^*} < 0$, then $\text{length}(y \to i^*)$ could be negative, allowing $d_{i^*} < d_y$ and invalidating the greedy monotonicity invariant. Implemented with a simple array scan, Dijkstra's algorithm runs in $O(m^2)$ time; with a binary min-heap priority queue, $O((m + n)\log m)$; and with a Fibonacci heap, $O(n + m \log m)$.

When a network contains negative arc weights $c_{ij} < 0$ (representing, for example, net energy regeneration, financial arbitrage rebates, or log-likelihood increments in statistical decoding), Dijkstra's greedy selection fails, and we must deploy the **Bellman-Ford-Moore Label-Correcting Algorithm**. Provided the network contains no **negative-weight directed cycle** reachable from $s$ (for if such a cycle existed, traversing it infinitely many times would drive the objective to $-\infty$), any simple shortest path on $m$ vertices contains at most $m - 1$ arcs. Defining $d_j^{(k)}$ as the minimum length of a directed walk from $s$ to $j$ utilizing at most $k$ arcs, initialized with $d_s^{(0)} = 0$ and $d_j^{(0)} = +\infty$ for $j \ne s$, the Bellman-Ford dynamic programming recursion computes for $k = 1, 2, \dots, m - 1$:

$$
d_j^{(k)} = \min\left\{ d_j^{(k-1)}, \; \min_{i : (i, j) \in \delta^-(j)} \left( d_i^{(k-1)} + c_{ij} \right) \right\} \quad \forall j \in \mathcal{V}
$$

Each pass $k$ relaxes all $n = |\mathcal{E}|$ arcs in $O(n)$ operations, yielding an overall worst-case time complexity of $O(mn)$. Furthermore, after completing $m - 1$ relaxation passes, the algorithm executes an $m$-th diagnostic pass: a negative-weight cycle reachable from $s$ exists if and only if there is at least one arc $(i, j) \in \mathcal{E}$ for which $d_j^{(m-1)} > d_i^{(m-1)} + c_{ij}$. When shortest paths between all ordered pairs of vertices $(i, j) \in \mathcal{V} \times \mathcal{V}$ are required simultaneously, the **Floyd-Warshall Algorithm** defines $D^{(k)} = [d_{ij}^{(k)}]$ as the shortest distance from $i$ to $j$ using only intermediate vertices from $\{1, 2, \dots, k\}$ and applies the $O(m^3)$ matrix recursion $d_{ij}^{(k)} = \min\big\{d_{ij}^{(k-1)}, \, d_{ik}^{(k-1)} + d_{kj}^{(k-1)}\big\}$ for $k = 1, \dots, m$, detecting negative cycles whenever any diagonal entry $d_{ii}^{(m)} < 0$.

## 5.3 Minimum Spanning Tree Optimization: Kruskal's Greedy Matroid Algorithm and Prim's Cut-Optimality Method

Whereas the shortest-path problem optimizes directed routing from a designated focal origin $s$, infrastructure design problems in telecommunications, power grid layout, pipeline networks, and statistical hierarchical clustering require connecting all $m$ nodes of an **undirected** weighted graph $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ at minimum total construction cost without regard to a specific root node. Let each undirected edge $e = \{i, j\} \in \mathcal{E}$ possess a symmetric weight $w_{ij} = w_{ji} \in \mathbb{R}$. A **spanning tree** $\mathcal{T} = (\mathcal{V}, \mathcal{E}_{\mathcal{T}})$ of a connected graph $\mathcal{G}$ is a connected, acyclic subgraph that spans all $m$ vertices of $\mathcal{V}$. Every spanning tree of an $m$-vertex graph satisfies three equivalent combinatorial characterizations: (1) $\mathcal{T}$ is connected and contains no cycles; (2) $\mathcal{T}$ is connected and contains exactly $|\mathcal{E}_{\mathcal{T}}| = m - 1$ edges; and (3) $\mathcal{T}$ is acyclic and contains exactly $m - 1$ edges, so that inserting any non-tree edge $e \notin \mathcal{E}_{\mathcal{T}}$ creates a unique fundamental cycle, and removing any single edge $e' \in \mathcal{E}_{\mathcal{T}}$ disconnects $\mathcal{T}$ into two disjoint connected components. For a complete graph $K_m$, Cayley's formula establishes that there exist exactly $m^{m-2}$ distinct labeled spanning trees, rendering exhaustive enumeration computationally impossible even for moderate $m$. The **Minimum Spanning Tree (MST) Problem** seeks a spanning tree $\mathcal{T}^*$ minimizing total edge weight:

$$
\min_{\mathcal{T} \in \mathcal{S}_{\mathcal{G}}} \quad W(\mathcal{T}) = \sum_{e = \{i, j\} \in \mathcal{E}_{\mathcal{T}}} w_{ij}
$$

To formulate the MST problem as a binary integer linear program (whose LP relaxation is exact over the **spanning tree polytope** studied by Jack Edmonds), introduce a binary indicator variable $x_e \in \{0, 1\}$ for each edge $e \in \mathcal{E}$:

$$
\min_{\mathbf{x}} \sum_{e \in \mathcal{E}} w_e x_e \quad \text{subject to} \quad \sum_{e \in \mathcal{E}} x_e = m - 1, \quad \sum_{e \in \mathcal{E}(\mathcal{S})} x_e \le |\mathcal{S}| - 1 \;\; \forall \emptyset \subset \mathcal{S} \subset \mathcal{V}, \quad x_e \ge 0
$$

where $\mathcal{E}(\mathcal{S}) = \{\{i, j\} \in \mathcal{E} : i \in \mathcal{S} \text{ and } j \in \mathcal{S}\}$ denotes the set of edges with both endpoints inside vertex subset $\mathcal{S}$. The **subtour elimination constraints** $\sum_{e \in \mathcal{E}(\mathcal{S})} x_e \le |\mathcal{S}| - 1$ prohibit cycles within any subset $\mathcal{S}$ of vertices. More profoundly, the family of acyclic edge subsets $\mathcal{I} = \{F \subseteq \mathcal{E} : (\mathcal{V}, F) \text{ is a forest}\}$ forms a **graphic matroid** $\mathcal{M} = (\mathcal{E}, \mathcal{I})$. A finite matroid satisfies three axioms: (M1) $\emptyset \in \mathcal{I}$; (M2) hereditary closure ($B \in \mathcal{I}, A \subseteq B \implies A \in \mathcal{I}$); and (M3) the exchange property (if $A, B \in \mathcal{I}$ with $|A| < |B|$, there exists an element $e \in B \setminus A$ such that $A \cup \{e\} \in \mathcal{I}$). By the Rado-Edmonds theorem, a greedy algorithm is guaranteed to find a globally optimal basis for every non-negative weight function if and only if the underlying independence system is a matroid.

From this matroidal structure emerge two dual optimality criteria for spanning trees:
* **Cut Optimality Condition**: A cut $(\mathcal{S}, \mathcal{V} \setminus \mathcal{S})$ is a partition of the vertex set into two non-empty disjoint subsets. The cut-set $\delta(\mathcal{S}) = \{\{i, j\} \in \mathcal{E} : i \in \mathcal{S}, j \in \mathcal{V} \setminus \mathcal{S}\}$ consists of all edges crossing the partition. If $F \subseteq \mathcal{E}_{\mathcal{T}^*}$ is a subset of edges belonging to some minimum spanning tree $\mathcal{T}^*$, and $(\mathcal{S}, \mathcal{V} \setminus \mathcal{S})$ is any cut that respects $F$ (meaning $F \cap \delta(\mathcal{S}) = \emptyset$), then any minimum-weight edge $e^* = \arg\min_{e \in \delta(\mathcal{S})} w_e$ crossing the cut is safe to add to $F$, in the sense that $F \cup \{e^*\}$ is contained in a minimum spanning tree. *Proof via exchange argument*: Suppose $\mathcal{T}^*$ is an MST containing $F$ but not $e^* = \{u, v\}$. Adding $e^*$ to $\mathcal{T}^*$ creates a unique cycle $C$. Since $u \in \mathcal{S}$ and $v \notin \mathcal{S}$, the cycle $C$ must cross the cut $(\mathcal{S}, \mathcal{V} \setminus \mathcal{S})$ along at least one other tree edge $e' \in \mathcal{E}_{\mathcal{T}^*} \cap \delta(\mathcal{S})$ with $e' \notin F$. Because $e^*$ is a minimum-weight edge in $\delta(\mathcal{S})$, we have $w_{e^*} \le w_{e'}$. Constructing the modified tree $\mathcal{T}' = (\mathcal{T}^* \setminus \{e'\}) \cup \{e^*\}$ preserves connectivity and acyclicity while yielding total weight $W(\mathcal{T}') = W(\mathcal{T}^*) - w_{e'} + w_{e^*} \le W(\mathcal{T}^*)$. Since $\mathcal{T}^*$ is minimal, $W(\mathcal{T}') = W(\mathcal{T}^*)$, proving that $\mathcal{T}'$ is an MST containing $F \cup \{e^*\}$.
* **Cycle Optimality Condition**: An edge $e$ belongs to some MST if and only if $e$ is not the unique strictly heaviest edge on any cycle $C$ of $\mathcal{G}$.

Two classic polynomial-time algorithms directly implement the Cut Optimality Condition:
1. **Kruskal's Greedy Algorithm (1956)**: Sort all $n$ edges in non-decreasing order of weight: $w_{e_1} \le w_{e_2} \le \dots \le w_{e_n}$. Initialize the spanning forest as $m$ isolated singleton components $\mathcal{F}_0 = (\mathcal{V}, \emptyset)$. Iterate sequentially through the sorted edges $e_k = \{u_k, v_k\}$ for $k = 1, \dots, n$: if $u_k$ and $v_k$ currently belong to two distinct connected components of $\mathcal{F}_{k-1}$ (so adding $e_k$ does not form a cycle), include $e_k$ in the forest ($\mathcal{F}_k \leftarrow \mathcal{F}_{k-1} \cup \{e_k\}$) and merge the two components; otherwise, discard $e_k$. Terminate as soon as $m - 1$ edges have been selected. Using a Disjoint-Set Union-Find data structure with path compression and union by rank, cycle testing takes $O(\alpha(m))$ amortized time per edge, so Kruskal's algorithm runs in $O(n \log n) = O(n \log m)$ time, making it exceptionally fast for sparse graphs ($n \approx O(m)$).
2. **Prim's Algorithm (Jarník 1930, Prim 1957, Dijkstra 1959)**: Instead of growing a disconnected forest of components across the graph, Prim's algorithm grows a single connected tree $\mathcal{T}_k = (\mathcal{V}_k, \mathcal{E}_k)$ outward from an arbitrary starting root vertex $v_1 \in \mathcal{V}$. Initialize $\mathcal{V}_1 = \{v_1\}$ and $\mathcal{E}_1 = \emptyset$. At iteration $k = 1, \dots, m - 1$, examine the cut $(\mathcal{V}_k, \mathcal{V} \setminus \mathcal{V}_k)$ separating the currently connected vertices from the remaining unvisited vertices, and select the minimum-weight edge crossing this cut:

$$
(u^*, v^*) = \arg\min_{u \in \mathcal{V}_k, \, v \in \mathcal{V} \setminus \mathcal{V}_k} \{w_{uv}\}
$$

Append vertex $v^*$ to $\mathcal{V}_k$ ($\mathcal{V}_{k+1} = \mathcal{V}_k \cup \{v^*\}$) and edge $\{u^*, v^*\}$ to $\mathcal{E}_k$. By maintaining for each external vertex $v \notin \mathcal{V}_k$ its minimum attachment distance $k_v = \min_{u \in \mathcal{V}_k} w_{uv}$, Prim's algorithm executes in $O(m^2)$ time using an array or $O(n + m \log m)$ using a priority heap, making the $O(m^2)$ array implementation superior to Kruskal's $O(n \log n)$ on dense graphs where $n = \Theta(m^2)$. In statistical machine learning, single-linkage hierarchical agglomerative clustering is mathematically identical to running Kruskal's MST algorithm on the pairwise distance matrix of observations and severing the $k - 1$ heaviest tree edges to form $k$ clusters.

## 5.4 Maximal Flow Networks: Residual Graphs, Ford-Fulkerson Augmenting Paths, and the Max-Flow Min-Cut Theorem

In contrast to shortest-path and minimum spanning tree problems that minimize distance or installation cost, the **Maximal Flow Problem** seeks to route the maximum possible volume of commodity per unit time from a single designated source node $s \in \mathcal{V}$ to a single sink node $t \in \mathcal{V}$ through a capacitated directed network $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ without violating individual arc capacity limits $u_{ij} \ge 0$. A feasible flow vector $\mathbf{x} = (x_{ij})_{(i, j) \in \mathcal{E}}$ must satisfy two fundamental structural laws:
1. **Arc Capacity Constraints**: $0 \le x_{ij} \le u_{ij}$ for every directed arc $(i, j) \in \mathcal{E}$.
2. **Kirchhoff's Conservation of Flow at Intermediate Nodes**: For every transshipment node $i \in \mathcal{V} \setminus \{s, t\}$, total incoming flow must equal total outgoing flow:

$$
\sum_{j : (i, j) \in \delta^+(i)} x_{ij} - \sum_{k : (k, i) \in \delta^-(i)} x_{ki} = 0 \quad \forall i \in \mathcal{V} \setminus \{s, t\}
$$

The net flow value $v(\mathbf{x})$ departing the source $s$ (which by summing the conservation equations over all nodes automatically equals the net flow arriving at the sink $t$) is defined as:

$$
v = \sum_{j : (s, j) \in \delta^+(s)} x_{sj} - \sum_{k : (k, s) \in \delta^-(s)} x_{ks} = \sum_{k : (k, t) \in \delta^-(t)} x_{kt} - \sum_{j : (t, j) \in \delta^+(t)} x_{tj}
$$

Note that the Maximal Flow Problem is a special case of the Minimum-Cost Network Flow Problem of Section 5.1: if we introduce an artificial return arc $(t, s)$ from sink $t$ back to source $s$ with infinite capacity $u_{ts} = \infty$ and unit cost $c_{ts} = -1$, while assigning $c_{ij} = 0$ to all original arcs $(i, j) \in \mathcal{E}$ and $b_i = 0$ at every node $i \in \mathcal{V}$ (a pure circulation network), minimizing $\sum c_{ij} x_{ij} = -x_{ts}$ is equivalent to maximizing the circulation flow $v = x_{ts}$.

To analyze flow upper bounds and optimality, we define an **$s$-$t$ cut** as any partition of the vertex set $\mathcal{V}$ into two disjoint subsets $(\mathcal{S}, \bar{\mathcal{S}})$ with $\bar{\mathcal{S}} = \mathcal{V} \setminus \mathcal{S}$ such that the source belongs to $\mathcal{S}$ ($s \in \mathcal{S}$) and the sink belongs to $\bar{\mathcal{S}}$ ($t \in \bar{\mathcal{S}}$). The **forward arcs** of the cut are $(i, j) \in (\mathcal{S}, \bar{\mathcal{S}})$ with $i \in \mathcal{S}, j \in \bar{\mathcal{S}}$, and the **backward arcs** are $(k, l) \in (\bar{\mathcal{S}}, \mathcal{S})$ with $k \in \bar{\mathcal{S}}, l \in \mathcal{S}$. The **capacity of an $s$-$t$ cut** $C(\mathcal{S}, \bar{\mathcal{S}})$ is defined strictly as the sum of the capacities of its forward arcs:

$$
C(\mathcal{S}, \bar{\mathcal{S}}) = \sum_{(i, j) \in (\mathcal{S}, \bar{\mathcal{S}})} u_{ij}
$$

Summing the nodal conservation equations over all nodes $i \in \mathcal{S}$ causes all internal flows between nodes where both endpoints lie inside $\mathcal{S}$ to cancel identically in pairs ($+x_{pq}$ at row $p \in \mathcal{S}$ cancels $-x_{pq}$ at row $q \in \mathcal{S}$), yielding the fundamental flow-across-a-cut identity for any feasible flow $\mathbf{x}$ and any $s$-$t$ cut $(\mathcal{S}, \bar{\mathcal{S}})$:

$$
v(\mathbf{x}) = \sum_{(i, j) \in (\mathcal{S}, \bar{\mathcal{S}})} x_{ij} - \sum_{(k, l) \in (\bar{\mathcal{S}}, \mathcal{S})} x_{kl}
$$

Since every forward arc satisfies $x_{ij} \le u_{ij}$ and every backward arc satisfies $x_{kl} \ge 0$, we obtain the **Weak Duality Inequality for Network Flows**:

$$
v(\mathbf{x}) = \sum_{(i, j) \in (\mathcal{S}, \bar{\mathcal{S}})} x_{ij} - \sum_{(k, l) \in (\bar{\mathcal{S}}, \mathcal{S})} x_{kl} \le \sum_{(i, j) \in (\mathcal{S}, \bar{\mathcal{S}})} u_{ij} - 0 = C(\mathcal{S}, \bar{\mathcal{S}})
$$

Thus, the value of *any* feasible flow from $s$ to $t$ cannot exceed the capacity of *any* $s$-$t$ cut. Furthermore, equality $v(\mathbf{x}) = C(\mathcal{S}, \bar{\mathcal{S}})$ holds if and only if every forward arc across the cut is completely saturated ($x_{ij} = u_{ij}$ for all $(i, j) \in (\mathcal{S}, \bar{\mathcal{S}})$) and every backward arc across the cut carries zero flow ($x_{kl} = 0$ for all $(k, l) \in (\bar{\mathcal{S}}, \mathcal{S})$).

Given a feasible flow $\mathbf{x}$, the **Residual Network** $\mathcal{G}_f(\mathbf{x}) = (\mathcal{V}, \mathcal{E}_f)$ encodes all remaining opportunities to alter arc flows. For each pair of nodes $(i, j)$, the **residual capacity** $r_{ij}$ measures how much additional net flow can be pushed from $i$ to $j$:
* For a **forward arc** $(i, j) \in \mathcal{E}$ currently carrying flow $x_{ij} < u_{ij}$, we can increase flow by up to $r_{ij} = u_{ij} - x_{ij} > 0$.
* For a **backward (reverse) arc** $(j, i)$ corresponding to an original arc $(i, j) \in \mathcal{E}$ currently carrying positive flow $x_{ij} > 0$, we can push up to $r_{ji} = x_{ij} > 0$ units of "virtual flow" from $j$ to $i$, which physically represents *canceling* or redirecting previously assigned flow $x_{ij}$ on $(i, j)$ so that the commodity goes elsewhere.

More generally, if both $(i, j)$ and $(j, i)$ exist in $\mathcal{G}$, the combined residual capacity from $i$ to $j$ is $r_{ij} = (u_{ij} - x_{ij}) + x_{ji}$. An **augmenting path** $P$ is a simple directed path from $s$ to $t$ in the residual network $\mathcal{G}_f(\mathbf{x})$ along which every residual arc $(i, j) \in P$ has strictly positive residual capacity $r_{ij} > 0$. The **bottleneck capacity** of the augmenting path $P$ is:

$$
\Delta_P = \min_{(i, j) \in P} \{r_{ij}\} > 0
$$

The **Ford-Fulkerson Augmenting Path Algorithm** (published by L. R. Ford Jr. and D. R. Fulkerson in 1956) proceeds iteratively: starting from the zero flow $\mathbf{x} = \mathbf{0}$, search $\mathcal{G}_f(\mathbf{x})$ for an augmenting path $P$ from $s$ to $t$. If a path $P$ is found, compute $\Delta_P = \min_{(i, j) \in P} r_{ij}$, increment the total flow $v \leftarrow v + \Delta_P$, and update the residual capacities along every arc $(i, j) \in P$ via $r_{ij} \leftarrow r_{ij} - \Delta_P$ and $r_{ji} \leftarrow r_{ji} + \Delta_P$ (which increases $x_{ij}$ by $\Delta_P$ on forward arcs and decreases $x_{ji}$ by $\Delta_P$ on backward arcs). Repeat until no directed path from $s$ to $t$ with positive residual capacity exists in $\mathcal{G}_f(\mathbf{x})$.

This termination condition leads directly to the celebrated **Max-Flow Min-Cut Theorem** (Ford and Fulkerson 1956; Elias, Feinstein, and Shannon 1956): in any capacitated network, the maximum value of a feasible $s$-$t$ flow is exactly equal to the minimum capacity among all $s$-$t$ cuts:

$$
\max_{\mathbf{x} \text{ feasible}} v(\mathbf{x}) = \min_{(\mathcal{S}, \bar{\mathcal{S}})} C(\mathcal{S}, \bar{\mathcal{S}})
$$

We prove this theorem by demonstrating the equivalence of three statements for any feasible flow $\mathbf{x}^*$: (i) $\mathbf{x}^*$ is a maximum flow; (ii) the residual network $\mathcal{G}_f(\mathbf{x}^*)$ contains no augmenting path from $s$ to $t$; and (iii) there exists an $s$-$t$ cut $(\mathcal{S}^*, \bar{\mathcal{S}}^*)$ such that $v(\mathbf{x}^*) = C(\mathcal{S}^*, \bar{\mathcal{S}}^*)$. Clearly (i) $\implies$ (ii), since an augmenting path would increase $v(\mathbf{x}^*)$. To prove (ii) $\implies$ (iii), assume $\mathcal{G}_f(\mathbf{x}^*)$ has no $s$-$t$ augmenting path, and define $\mathcal{S}^*$ as the set of all vertices reachable from $s$ via directed paths of positive residual capacity in $\mathcal{G}_f(\mathbf{x}^*)$, with $\bar{\mathcal{S}}^* = \mathcal{V} \setminus \mathcal{S}^*$. By definition, $s \in \mathcal{S}^*$ and $t \in \bar{\mathcal{S}}^*$, so $(\mathcal{S}^*, \bar{\mathcal{S}}^*)$ is a valid $s$-$t$ cut. Moreover, for every pair $i \in \mathcal{S}^*, j \in \bar{\mathcal{S}}^*$, the residual capacity $r_{ij}$ must be zero (otherwise $j$ would be reachable from $s$ and belong to $\mathcal{S}^*$, a contradiction). Recall that $r_{ij} = (u_{ij} - x_{ij}^*) + x_{ji}^* = 0$. Since both $u_{ij} - x_{ij}^* \ge 0$ and $x_{ji}^* \ge 0$, their sum vanishes if and only if $x_{ij}^* = u_{ij}$ on every forward arc $(i, j) \in (\mathcal{S}^*, \bar{\mathcal{S}}^*)$ and $x_{ji}^* = 0$ on every backward arc $(j, i) \in (\bar{\mathcal{S}}^*, \mathcal{S}^*)$. Substituting these into the cut-flow identity yields $v(\mathbf{x}^*) = \sum_{(i, j) \in (\mathcal{S}^*, \bar{\mathcal{S}}^*)} u_{ij} - 0 = C(\mathcal{S}^*, \bar{\mathcal{S}}^*)$. Finally, (iii) $\implies$ (i) follows immediately from weak duality $v(\mathbf{x}) \le C(\mathcal{S}^*, \bar{\mathcal{S}}^*)$. Note that when capacities are integers, Ford-Fulkerson terminates in at most $O(n \cdot v^*)$ steps and guarantees an **integral maximum flow**; by choosing the shortest augmenting path (fewest arcs) via Breadth-First Search (BFS) at each step, the **Edmonds-Karp Algorithm** guarantees strongly polynomial termination in $O(m n^2)$ time even for irrational capacities.

## 5.5 Deterministic Project Scheduling: Critical Path Method (CPM), Float Mechanics, and Time-Cost Crashing

Large-scale engineering, manufacturing, clinical trial, and statistical survey operations consist of dozens or hundreds of interdependent activities governed by strict technological precedence relationships. Developed independently in the late 1950s—the **Critical Path Method (CPM)** by James E. Kelley of Remington Rand and Morgan R. Walker of DuPont in 1957 for chemical plant maintenance, and the **Program Evaluation and Review Technique (PERT)** by the U.S. Navy Special Projects Office and Booz Allen Hamilton in 1958 for the Polaris Fleet Ballistic Missile program—network scheduling maps partial orderings of tasks onto a **Directed Acyclic Graph (DAG)**. Two topological representations exist: **Activity-on-Node (AON)** diagrams, where nodes represent activities and directed arcs represent precedence constraints; and **Activity-on-Arc (AOA)** (or Activity-on-Arrow) event networks, where directed arcs $(i, j) \in \mathcal{E}$ represent activities with deterministic duration $t_{ij} \ge 0$ and vertices $i \in \{1, 2, \dots, m\}$ represent instantaneous milestone **events** marking the completion of all incoming activities and the authorization to begin outgoing activities.

Constructing a valid AOA network requires adhering to three structural rules: (1) the network must be acyclic (otherwise a circular logical deadlock exists) and topologically numbered via **Fulkerson's Rule** such that $i < j$ for every directed arc $(i, j) \in \mathcal{E}$; (2) at most one directed arc may directly connect any ordered pair of events $(i, j)$; and (3) whenever two activities share parallel start and end events, or whenever two activities share some—but not all—of their immediate predecessors, **dummy activities** (represented as dashed arcs with zero time duration $t_{ij} = 0$ and zero resource consumption) must be inserted to preserve unique arc identification and exact logical dependencies.

To determine the minimum project completion time $T_{\min}$ and identify bottleneck activities, CPM executes a two-pass dynamic programming procedure equivalent to finding the **longest path** in a directed acyclic graph:
1. **Forward Pass (Earliest Event Times $E_j$)**: Let $E_j$ denote the earliest time at which event $j$ can occur, which requires *all* activities terminating at node $j$ to be completed. Initializing the project start event at $E_1 = 0$, we compute $E_j$ sequentially in topological order $j = 2, 3, \dots, m$:

$$
E_j = \max_{i : (i, j) \in \delta^-(j)} \left\{ E_i + t_{ij} \right\} \quad \text{for } j = 2, 3, \dots, m
$$

The earliest completion time of the entire project at the terminal sink event $m$ is $T_{\min} = E_m$.
2. **Backward Pass (Latest Allowable Event Times $L_i$)**: Let $L_i$ denote the latest time at which event $i$ can occur without delaying the overall project completion beyond the target deadline $L_m = E_m = T_{\min}$. Working backward from the terminal node $L_m = E_m$ down to $i = m-1, m-2, \dots, 1$:

$$
L_i = \min_{j : (i, j) \in \delta^+(i)} \left\{ L_j - t_{ij} \right\} \quad \text{for } i = m - 1, m - 2, \dots, 1
$$

The difference $L_i - E_i \ge 0$ is termed the **event slack** of milestone $i$. From the event times $E_i$ and $L_j$, we compute four schedule boundary times for each individual activity $(i, j) \in \mathcal{E}$:
* **Earliest Start Time**: $\text{ES}_{ij} = E_i$
* **Earliest Finish Time**: $\text{EF}_{ij} = E_i + t_{ij} = \text{ES}_{ij} + t_{ij}$
* **Latest Finish Time**: $\text{LF}_{ij} = L_j$
* **Latest Start Time**: $\text{LS}_{ij} = L_j - t_{ij} = \text{LF}_{ij} - t_{ij}$

To quantify scheduling flexibility for non-bottleneck activities, operations researchers define three distinct **float** metrics for each activity $(i, j)$:
1. **Total Float ($\text{TF}_{ij}$)**: The maximum amount of time by which activity $(i, j)$ can be delayed beyond its earliest start $\text{ES}_{ij}$ without delaying the overall project completion time $E_m$:

$$
\text{TF}_{ij} = \text{LS}_{ij} - \text{ES}_{ij} = \text{LF}_{ij} - \text{EF}_{ij} = L_j - E_i - t_{ij}
$$

2. **Free Float ($\text{FF}_{ij}$)**: The maximum amount of time by which activity $(i, j)$ can be delayed without delaying the earliest start time $E_j$ of *any* immediately succeeding activity departing node $j$, assuming activity $(i, j)$ starts at $E_i$:

$$
\text{FF}_{ij} = E_j - E_i - t_{ij} = \text{TF}_{ij} - (L_j - E_j)
$$

3. **Independent Float ($\text{IF}_{ij}$)**: The amount of flexibility remaining for activity $(i, j)$ even under the worst-case scenario where all predecessors finish as late as possible ($L_i$) and all successors must start as early as possible ($E_j$):

$$
\text{IF}_{ij} = \max\left\{0, \; E_j - L_i - t_{ij}\right\}
$$

Because $E_i \le L_i$ and $E_j \le L_j$ for every event, these floats always satisfy the strict hierarchy $0 \le \text{IF}_{ij} \le \text{FF}_{ij} \le \text{TF}_{ij}$. An activity $(i, j)$ is defined as a **critical activity** if and only if its Total Float vanishes ($\text{TF}_{ij} = 0$), which implies $\text{ES}_{ij} = \text{LS}_{ij}$, $\text{EF}_{ij} = \text{LF}_{ij}$, $E_i = L_i$, $E_j = L_j$, and $E_j - E_i = L_j - L_i = t_{ij}$. A continuous directed path from source node $1$ to sink node $m$ composed exclusively of critical activities is a **Critical Path**; it represents the longest path through the project network, and any delay $\Delta t > 0$ on a critical activity directly delays the entire project by $\Delta t$.

In **CPM Time-Cost Trade-Off (Crashing) Analysis**, managers can expedite critical activities by allocating additional resources. Each activity $(i, j)$ possesses a normal duration $t_{ij}^N$ with normal direct cost $C_{ij}^N$, and a minimum expedited crash duration $t_{ij}^C < t_{ij}^N$ with higher crash direct cost $C_{ij}^C > C_{ij}^N$. Assuming a linear convex cost-duration relationship, the marginal cost of compressing activity $(i, j)$ by one time unit is the **crash cost slope**:

$$
s_{ij} = \frac{C_{ij}^C - C_{ij}^N}{t_{ij}^N - t_{ij}^C} > 0
$$

To compress project completion to a target deadline $T_{\text{target}}$ at minimum incremental cost (or to balance direct crashing costs against indirect overhead cost $C_{\text{ind}} \cdot T$), we formulate the CPM Crashing Linear Program using event occurrence variables $E_i \ge 0$ and activity compression variables $y_{ij} \in [0, t_{ij}^N - t_{ij}^C]$:

$$
\min_{E, y} \sum_{(i, j) \in \mathcal{E}} s_{ij} y_{ij} \quad \text{subject to} \quad E_j - E_i \ge t_{ij}^N - y_{ij} \;\; \forall (i, j) \in \mathcal{E}, \quad 0 \le y_{ij} \le t_{ij}^N - t_{ij}^C, \quad E_m - E_1 \le T_{\text{target}}
$$

Heuristically, one crashes the critical activity with the smallest marginal slope $s_{ij}$ until either that activity reaches its crash limit $t_{ij}^C$ or a parallel non-critical path becomes simultaneously critical, after which both parallel critical paths must be compressed jointly.

## 5.6 Probabilistic Project Networks: Program Evaluation and Review Technique (PERT) and Beta-Normal Completion Analysis

Whereas CPM assumes that activity durations $t_{ij}$ are known deterministic constants based on historical engineering standards, research and development projects, new software architectures, and pioneering statistical field trials involve substantial duration uncertainty. The **Program Evaluation and Review Technique (PERT)** models each activity duration $T_{ij}$ as a continuous random variable bounded over a finite interval $[a_{ij}, b_{ij}]$ and elicits three domain-expert point estimates for every activity $(i, j) \in \mathcal{E}$:
1. **Optimistic Time ($a_{ij}$)**: The minimum conceivable duration required to complete activity $(i, j)$ if all operational conditions proceed ideally without any technical or logistical impediments (typically corresponding to the lower 1st or 0th percentile of the duration distribution).
2. **Most Likely or Modal Time ($m_{ij}$)**: The single most probable duration required under normal operating conditions, corresponding to the statistical **mode** (peak density) of the probability distribution, satisfying $a_{ij} \le m_{ij} \le b_{ij}$.
3. **Pessimistic Time ($b_{ij}$)**: The maximum duration required under severe adverse conditions (excluding catastrophic force majeure events), corresponding to the upper 99th or 100th percentile of the duration distribution.

To accommodate right-skewed ($m_{ij}$ closer to $a_{ij}$), left-skewed ($m_{ij}$ closer to $b_{ij}$), and symmetric ($m_{ij} = (a_{ij} + b_{ij})/2$) uncertainty profiles over the bounded support $[a_{ij}, b_{ij}]$, PERT assumes that $T_{ij}$ follows a **Four-Parameter Generalized Beta Distribution** with probability density function:

$$
f_{T_{ij}}(t) = \frac{\Gamma(\alpha + \beta)}{\Gamma(\alpha)\Gamma(\beta)} \frac{(t - a_{ij})^{\alpha - 1} (b_{ij} - t)^{\beta - 1}}{(b_{ij} - a_{ij})^{\alpha + \beta - 1}}, \quad a_{ij} \le t \le b_{ij}, \quad \alpha > 1, \; \beta > 1
$$

Standardizing to $Y = \frac{T_{ij} - a_{ij}}{b_{ij} - a_{ij}} \sim \text{Beta}(\alpha, \beta)$ on $[0, 1]$, we know from mathematical statistics that the exact mean, variance, and mode of $Y$ are $\mathbb{E}[Y] = \frac{\alpha}{\alpha + \beta}$, $\text{Var}(Y) = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$, and $\text{Mode}(Y) = \frac{\alpha - 1}{\alpha + \beta - 2} = \frac{m_{ij} - a_{ij}}{b_{ij} - a_{ij}}$. Because a single mode estimate $m_{ij}$ does not uniquely determine the two shape parameters $(\alpha, \beta)$, the creators of PERT introduced two classic parametric closure conventions: first, by analogy with the standard normal distribution where $99.73\%$ of the probability mass lies within $\pm 3\sigma$ of the mean, the total range $b_{ij} - a_{ij}$ is assumed to span six standard deviations ($6\sigma_{ij} = b_{ij} - a_{ij}$); second, the sum of the shape parameters is calibrated to $\alpha + \beta = 6$ (or equivalently $\alpha = 3 \pm \sqrt{2}$ in the symmetric case where $\sigma_Y = 1/6$). Substituting $\alpha + \beta = 6$ into the Beta mean and mode relations yields $\mathbb{E}[Y] = \frac{\alpha}{6}$ and $\text{Mode}(Y) = \frac{\alpha - 1}{4} \implies \alpha = 4\,\text{Mode}(Y) + 1$, whence $\mathbb{E}[Y] = \frac{4\,\text{Mode}(Y) + 1}{6}$. Transforming back to the original time scale $T_{ij} = a_{ij} + (b_{ij} - a_{ij})Y$ produces the celebrated **PERT Three-Point Expected Duration and Variance Formulas**:

$$
\mu_{ij} = \mathbb{E}[T_{ij}] = \frac{a_{ij} + 4m_{ij} + b_{ij}}{6}, \qquad \sigma_{ij}^2 = \text{Var}(T_{ij}) = \left( \frac{b_{ij} - a_{ij}}{6} \right)^2 = \frac{(b_{ij} - a_{ij})^2}{36}
$$

Notice that the expected duration $\mu_{ij}$ is a weighted average of the midpoint $\frac{a_{ij} + b_{ij}}{2}$ (with weight $1/3$) and the mode $m_{ij}$ (with weight $2/3$). Whenever the distribution is right-skewed ($b_{ij} - m_{ij} > m_{ij} - a_{ij}$), the mean exceeds the mode ($\mu_{ij} > m_{ij}$).

Once $\mu_{ij}$ and $\sigma_{ij}^2$ have been computed for every activity, PERT applies the deterministic CPM forward and backward pass algorithms using the expected durations $\mu_{ij}$ in place of $t_{ij}$. Let $\mathcal{P}_{\text{crit}}$ denote the critical path identified by these mean durations. Assuming that individual activity durations $T_{ij}$ are **mutually statistically independent** and that the critical path $\mathcal{P}_{\text{crit}}$ contains a sufficiently large number of sequential activities, the **Lyapunov / Lindeberg-Feller Central Limit Theorem (CLT)** implies that the total duration of the critical path $T_{\text{cp}} = \sum_{(i, j) \in \mathcal{P}_{\text{crit}}} T_{ij}$ is approximately **Normally Distributed**:

$$
T_{\text{cp}} = \sum_{(i, j) \in \mathcal{P}_{\text{crit}}} T_{ij} \;\stackrel{\text{approx}}{\sim}\; \mathcal{N}\left(\mu_{\text{cp}}, \, \sigma_{\text{cp}}^2\right)
$$

where, by linearity of expectation and additivity of variance for independent random variables:

$$
\mu_{\text{cp}} = \sum_{(i, j) \in \mathcal{P}_{\text{crit}}} \mu_{ij}, \qquad \sigma_{\text{cp}}^2 = \sum_{(i, j) \in \mathcal{P}_{\text{crit}}} \sigma_{ij}^2 = \sum_{(i, j) \in \mathcal{P}_{\text{crit}}} \left(\frac{b_{ij} - a_{ij}}{6}\right)^2
$$

If two or more parallel paths share the exact same maximum expected duration $\mu_{\text{cp}}$, standard PERT practice selects the critical path with the largest total variance $\sigma_{\text{cp}}^2$ for conservative risk assessment, or evaluates the joint probability that all parallel paths finish before the target deadline. Given any contractual deadline $D$, the probability that the critical path completes on or before time $D$ is evaluated via the standard normal cumulative distribution function $\Phi(z)$:

$$
\mathbb{P}(T_{\text{cp}} \le D) = \Phi\left( \frac{D - \mu_{\text{cp}}}{\sigma_{\text{cp}}} \right) = \Phi(Z_D)
$$

Conversely, the $(1 - \alpha) \times 100\%$ guaranteed completion deadline $D_{1-\alpha}$ satisfying $\mathbb{P}(T_{\text{cp}} \le D_{1-\alpha}) = 1 - \alpha$ is given by $D_{1-\alpha} = \mu_{\text{cp}} + z_{1-\alpha}\,\sigma_{\text{cp}}$.

From a rigorous statistical perspective, analysts must recognize **Jensen's Inequality and Merge-Node Bias** in PERT networks. The true stochastic project completion time is the maximum over *all* $K$ directed paths $\mathcal{P}_1, \mathcal{P}_2, \dots, \mathcal{P}_K$ from source to sink: $T_{\text{true}} = \max_{1 \le k \le K} \left( \sum_{(i, j) \in \mathcal{P}_k} T_{ij} \right)$. Because the pointwise maximum function $g(x_1, \dots, x_K) = \max_k x_k$ is convex, **Jensen's Inequality** guarantees that the true expected completion time is never smaller—and whenever near-critical parallel paths exist with positive variance, is *strictly larger*—than the PERT mean critical path estimate:

$$
\mathbb{E}[T_{\text{true}}] = \mathbb{E}\left[ \max_{1 \le k \le K} \text{Length}(\mathcal{P}_k) \right] \ge \max_{1 \le k \le K} \mathbb{E}\left[ \text{Length}(\mathcal{P}_k) \right] = \mu_{\text{cp}}
$$

Similarly, for independent parallel paths $\mathcal{P}_1, \dots, \mathcal{P}_K$, $\mathbb{P}(T_{\text{true}} \le D) = \prod_{k=1}^K \mathbb{P}(\text{Length}(\mathcal{P}_k) \le D) \le \mathbb{P}(T_{\text{cp}} \le D)$. Thus, classical PERT systematically underestimates expected project completion time and overestimates the probability of meeting a deadline whenever sub-critical paths have high variance or small mean slack, motivating **Monte Carlo Network Simulation** in modern statistical operations research.

<div class="table-wrapper"><table class="data-table">
<thead>
<tr>
<th>Network Optimization Model</th>
<th>Primary Decision Structure</th>
<th>Core Algorithmic Solution Method</th>
<th>Dual / Optimality Characterization</th>
<th>Computational Time Complexity</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Shortest Path ($c_{ij} \ge 0$)</strong></td>
<td>Directed path from source $s$ to sink $t$ (or all nodes)</td>
<td>Dijkstra's Greedy Label-Setting Algorithm</td>
<td>Bellman equations $d_j \le d_i + c_{ij}$ with equality on tree arcs</td>
<td>$O(m^2)$ array; $O(n + m\log m)$ Fibonacci heap</td>
</tr>
<tr>
<td><strong>Shortest Path (General $c_{ij}$)</strong></td>
<td>Directed path without negative cycles</td>
<td>Bellman-Ford-Moore Label-Correcting Dynamic Recursion</td>
<td>Convergence in $m-1$ passes; $m$-th pass detects negative cycles</td>
<td>$O(mn)$ worst-case across $m$ vertices, $n$ arcs</td>
</tr>
<tr>
<td><strong>Minimum Spanning Tree (MST)</strong></td>
<td>Connected acyclic subgraph of $m-1$ undirected edges</td>
<td>Kruskal's Union-Find or Prim's Cut-Expansion Algorithm</td>
<td>Matroid Cut-Optimality and Cycle-Optimality Conditions</td>
<td>$O(n \log m)$ Kruskal; $O(m^2)$ or $O(n + m\log m)$ Prim</td>
</tr>
<tr>
<td><strong>Maximal Network Flow</strong></td>
<td>Source-to-sink flow $v$ obeying $0 \le x_{ij} \le u_{ij}$</td>
<td>Ford-Fulkerson / Edmonds-Karp Residual Augmenting Paths</td>
<td>Max-Flow Min-Cut Theorem: $\max v(\mathbf{x}) = \min C(\mathcal{S}, \bar{\mathcal{S}})$</td>
<td>$O(n v^*)$ Ford-Fulkerson; $O(m n^2)$ Edmonds-Karp</td>
</tr>
<tr>
<td><strong>Deterministic CPM Scheduling</strong></td>
<td>Longest path in DAG and activity float allocation</td>
<td>Topological Forward Pass ($E_j$) and Backward Pass ($L_i$)</td>
<td>Critical path has zero Total Float ($\text{TF}_{ij} = L_j - E_i - t_{ij} = 0$)</td>
<td>$O(m + n)$ linear time in DAG size</td>
</tr>
<tr>
<td><strong>Stochastic PERT Scheduling</strong></td>
<td>Random completion time $T$ under Beta $(a, m, b)$ inputs</td>
<td>Three-point moments $\mu = \frac{a+4m+b}{6}, \sigma^2 = \left(\frac{b-a}{6}\right)^2$ + CLT</td>
<td>Normal tail probability $\Phi\big((D - \mu_{\text{cp}})/\sigma_{\text{cp}}\big)$; Jensen merge bias</td>
<td>$O(m + n)$ analytic; $O(N_{\text{sim}}(m+n))$ Monte Carlo</td>
</tr>
</tbody>
</table></div>

## Worked Questions and Solutions

### Question 1: Dijkstra's Shortest Path Algorithm and Dual Node Potential Verification

A regional statistical data transmission network consists of $6$ relay servers labeled $\mathcal{V} = \{1, 2, 3, 4, 5, 6\}$, where Server $1$ is the central origin node and Server $6$ is the primary archival sink. The directed communication links $(i, j) \in \mathcal{E}$ and their respective latency weights $c_{ij}$ (in milliseconds) are given as follows:
* From Node $1$: $(1, 2) = 4$, $(1, 3) = 2$
* From Node $2$: $(2, 3) = 1$, $(2, 4) = 5$
* From Node $3$: $(3, 2) = 1$, $(3, 4) = 8$, $(3, 5) = 10$
* From Node $4$: $(4, 5) = 2$, $(4, 6) = 6$
* From Node $5$: $(5, 6) = 2$

1. Execute **Dijkstra's Labeling Algorithm** step-by-step to determine the shortest-path latency $d_i$ and immediate predecessor $p_i$ from Node $1$ to every other node $i \in \{2, 3, 4, 5, 6\}$, presenting the full sequence of permanent and tentative node labels $[u_i, p_i]$ in a structured table.
2. Identify the unique minimum-latency directed path from Server $1$ to Server $6$, state the complete **shortest-path arborescence** (spanning tree of directed arcs rooted at Node $1$), and verify that the optimal distance labels $d_i$ satisfy all linear programming dual feasibility constraints $d_j - d_i \le c_{ij}$ and complementary slackness conditions.

### Solution, step 1: Initialization and Iterative Label-Setting Execution

Since all link latencies $c_{ij} > 0$ are strictly non-negative, Dijkstra's greedy label-setting algorithm guarantees global optimality in exactly $m = 6$ iterations. Each node $i$ maintains a label $[u_i, p_i]$, where $u_i$ is the cumulative latency from Node $1$ and $p_i$ is the immediate predecessor node.

* **Iteration 0 (Initialization)**: Set $u_1 = 0, p_1 = -$ and $u_i = \infty, p_i = -$ for $i \in \{2, 3, 4, 5, 6\}$. Currently, $\mathcal{S} = \emptyset$ and $\bar{\mathcal{S}} = \{1, 2, 3, 4, 5, 6\}$.
* **Iteration 1**: Select $i^* = \arg\min_{i \in \bar{\mathcal{S}}} u_i = 1$ with $d_1 = u_1 = 0$. Move Node $1$ to $\mathcal{S} = \{1\}$. Relax outgoing arcs from Node $1$:
  * Arc $(1, 2)$: $u_2 = \min(\infty, 0 + 4) = 4 \implies [4, 1]$
  * Arc $(1, 3)$: $u_3 = \min(\infty, 0 + 2) = 2 \implies [2, 1]$
* **Iteration 2**: Among $\bar{\mathcal{S}} = \{2, 3, 4, 5, 6\}$, the minimum tentative label is at Node $3$ with $u_3 = 2$. Permanently label Node $3$ ($d_3 = 2, p_3 = 1$, $\mathcal{S} = \{1, 3\}$) and relax outgoing arcs from Node $3$:
  * Arc $(3, 2)$: $u_2 = \min(4, 2 + 1) = 3 \implies [3, 3]$ (improved from $4$ via Node $3$)
  * Arc $(3, 4)$: $u_4 = \min(\infty, 2 + 8) = 10 \implies [10, 3]$
  * Arc $(3, 5)$: $u_5 = \min(\infty, 2 + 10) = 12 \implies [12, 3]$
* **Iteration 3**: Among $\bar{\mathcal{S}} = \{2, 4, 5, 6\}$, the minimum tentative label is at Node $2$ with $u_2 = 3$. Permanently label Node $2$ ($d_2 = 3, p_2 = 3$, $\mathcal{S} = \{1, 3, 2\}$) and relax outgoing arcs from Node $2$ to nodes in $\bar{\mathcal{S}}$:
  * Arc $(2, 4)$: $u_4 = \min(10, 3 + 5) = 8 \implies [8, 2]$ (improved from $10$ via Node $2$)
* **Iteration 4**: Among $\bar{\mathcal{S}} = \{4, 5, 6\}$, the minimum tentative label is at Node $4$ with $u_4 = 8$. Permanently label Node $4$ ($d_4 = 8, p_4 = 2$, $\mathcal{S} = \{1, 3, 2, 4\}$) and relax outgoing arcs from Node $4$:
  * Arc $(4, 5)$: $u_5 = \min(12, 8 + 2) = 10 \implies [10, 4]$ (improved from $12$ via Node $4$)
  * Arc $(4, 6)$: $u_6 = \min(\infty, 8 + 6) = 14 \implies [14, 4]$
* **Iteration 5**: Among $\bar{\mathcal{S}} = \{5, 6\}$, the minimum tentative label is at Node $5$ with $u_5 = 10$. Permanently label Node $5$ ($d_5 = 10, p_5 = 4$, $\mathcal{S} = \{1, 3, 2, 4, 5\}$) and relax outgoing arcs from Node $5$:
  * Arc $(5, 6)$: $u_6 = \min(14, 10 + 2) = 12 \implies [12, 5]$ (improved from $14$ via Node $5$)
* **Iteration 6**: Only Node $6$ remains in $\bar{\mathcal{S}}$. Permanently label Node $6$ with $d_6 = 12, p_6 = 5$, completing $\mathcal{S} = \{1, 3, 2, 4, 5, 6\}$.

### Solution, step 2: Tabular Summary of Dijkstra Iterations and Shortest-Path Arborescence

The complete progression of tentative and permanent labels $[u_i, p_i]$ (with permanent labels indicated by $\mathbf{[d_i, p_i]^*}$) across all six iterations is compiled in the table below:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr>
<th>Iteration $k$</th>
<th>Permanent Set $\mathcal{S}$</th>
<th>Node 1</th>
<th>Node 2</th>
<th>Node 3</th>
<th>Node 4</th>
<th>Node 5</th>
<th>Node 6</th>
</tr>
</thead>
<tbody>
<tr>
<td>1 (Fix $1$)</td>
<td>$\{1\}$</td>
<td>$\mathbf{[0, -]^*}$</td>
<td>$[4, 1]$</td>
<td>$[2, 1]$</td>
<td>$[\infty, -]$</td>
<td>$[\infty, -]$</td>
<td>$[\infty, -]$</td>
</tr>
<tr>
<td>2 (Fix $3$)</td>
<td>$\{1, 3\}$</td>
<td>$\mathbf{[0, -]^*}$</td>
<td>$[3, 3]$</td>
<td>$\mathbf{[2, 1]^*}$</td>
<td>$[10, 3]$</td>
<td>$[12, 3]$</td>
<td>$[\infty, -]$</td>
</tr>
<tr>
<td>3 (Fix $2$)</td>
<td>$\{1, 3, 2\}$</td>
<td>$\mathbf{[0, -]^*}$</td>
<td>$\mathbf{[3, 3]^*}$</td>
<td>$\mathbf{[2, 1]^*}$</td>
<td>$[8, 2]$</td>
<td>$[12, 3]$</td>
<td>$[\infty, -]$</td>
</tr>
<tr>
<td>4 (Fix $4$)</td>
<td>$\{1, 3, 2, 4\}$</td>
<td>$\mathbf{[0, -]^*}$</td>
<td>$\mathbf{[3, 3]^*}$</td>
<td>$\mathbf{[2, 1]^*}$</td>
<td>$\mathbf{[8, 2]^*}$</td>
<td>$[10, 4]$</td>
<td>$[14, 4]$</td>
</tr>
<tr>
<td>5 (Fix $5$)</td>
<td>$\{1, 3, 2, 4, 5\}$</td>
<td>$\mathbf{[0, -]^*}$</td>
<td>$\mathbf{[3, 3]^*}$</td>
<td>$\mathbf{[2, 1]^*}$</td>
<td>$\mathbf{[8, 2]^*}$</td>
<td>$\mathbf{[10, 4]^*}$</td>
<td>$[12, 5]$</td>
</tr>
<tr>
<td>6 (Fix $6$)</td>
<td>$\{1, 3, 2, 4, 5, 6\}$</td>
<td>$\mathbf{[0, -]^*}$</td>
<td>$\mathbf{[3, 3]^*}$</td>
<td>$\mathbf{[2, 1]^*}$</td>
<td>$\mathbf{[8, 2]^*}$</td>
<td>$\mathbf{[10, 4]^*}$</td>
<td>$\mathbf{[12, 5]^*}$</td>
</tr>
</tbody>
</table></div>

Backtracking through the optimal predecessor pointers $p_6 = 5 \to p_5 = 4 \to p_4 = 2 \to p_2 = 3 \to p_3 = 1$, the unique shortest directed path from Server $1$ to Server $6$ is:

$$
P_{1 \to 6}^* : \quad 1 \xrightarrow{c_{13}=2} 3 \xrightarrow{c_{32}=1} 2 \xrightarrow{c_{24}=5} 4 \xrightarrow{c_{45}=2} 5 \xrightarrow{c_{56}=2} 6, \qquad d_6 = 2 + 1 + 5 + 2 + 2 = 12\text{ ms}
$$

Because this single path visits all $6$ vertices in topological sequence, the $m - 1 = 5$ arcs $\mathcal{E}_{\mathcal{T}^*} = \{(1, 3), (3, 2), (2, 4), (4, 5), (5, 6)\}$ simultaneously form the complete **shortest-path arborescence** rooted at Node $1$.

### Solution, step 3: Dual Feasibility and Complementary Slackness Verification

In the linear programming dual of the shortest-path problem, the node potentials are $\mathbf{d} = (d_1, d_2, d_3, d_4, d_5, d_6) = (0, 3, 2, 8, 10, 12)$. Every directed arc $(i, j) \in \mathcal{E}$ must satisfy the dual feasibility inequality $d_j - d_i \le c_{ij}$ (or equivalently, the non-negative reduced cost $\bar{c}_{ij} = c_{ij} - (d_j - d_i) \ge 0$), with $\bar{c}_{ij} = 0$ on all shortest-path tree arcs:
* **Tree Arcs ($\bar{c}_{ij} = 0$)**:
  * $(1, 3)$: $d_3 - d_1 = 2 - 0 = 2 = c_{13} \implies \bar{c}_{13} = 0$
  * $(3, 2)$: $d_2 - d_3 = 3 - 2 = 1 = c_{32} \implies \bar{c}_{32} = 0$
  * $(2, 4)$: $d_4 - d_2 = 8 - 3 = 5 = c_{24} \implies \bar{c}_{24} = 0$
  * $(4, 5)$: $d_5 - d_4 = 10 - 8 = 2 = c_{45} \implies \bar{c}_{45} = 0$
  * $(5, 6)$: $d_6 - d_5 = 12 - 10 = 2 = c_{56} \implies \bar{c}_{56} = 0$
* **Non-Tree Arcs ($\bar{c}_{ij} > 0$, carrying $x_{ij} = 0$ flow)**:
  * $(1, 2)$: $d_2 - d_1 = 3 - 0 = 3 < 4 = c_{12} \implies \bar{c}_{12} = 1 > 0$
  * $(2, 3)$: $d_3 - d_2 = 2 - 3 = -1 < 1 = c_{23} \implies \bar{c}_{23} = 2 > 0$
  * $(3, 4)$: $d_4 - d_3 = 8 - 2 = 6 < 8 = c_{34} \implies \bar{c}_{34} = 2 > 0$
  * $(3, 5)$: $d_5 - d_3 = 10 - 2 = 8 < 10 = c_{35} \implies \bar{c}_{35} = 2 > 0$
  * $(4, 6)$: $d_6 - d_4 = 12 - 8 = 4 < 6 = c_{46} \implies \bar{c}_{46} = 2 > 0$

Since $\bar{c}_{ij} \ge 0$ for all $(i, j) \in \mathcal{E}$ and $\bar{c}_{ij} x_{ij} = 0$ everywhere, primal-dual optimality is rigorously confirmed.

---

### Question 2: Maximal Network Flow and Minimum Cut Capacity Verification

A municipal water distribution network routes flow from a primary reservoir at Source Node $1$ to a treatment plant at Sink Node $6$ through four intermediate pumping stations $\{2, 3, 4, 5\}$. The directed pipelines $(i, j) \in \mathcal{E}$ and their maximum flow capacities $u_{ij}$ (in thousand cubic meters per hour) are:
* Out of Source $1$: $u_{12} = 16$, $u_{13} = 13$
* Intermediate links: $u_{23} = 10$, $u_{32} = 4$, $u_{24} = 12$, $u_{35} = 14$, $u_{43} = 9$, $u_{54} = 7$
* Into Sink $6$: $u_{46} = 20$, $u_{56} = 4$

1. Apply the **Ford-Fulkerson / Edmonds-Karp Augmenting Path Algorithm** to compute the maximum flow $v^*$ from Node $1$ to Node $6$, explicitly detailing each augmenting path $P_k$, its bottleneck residual capacity $\Delta_k$, and the resulting residual network updates.
2. Determine the reachable vertex set $\mathcal{S}^*$ in the final residual network $\mathcal{G}_f(\mathbf{x}^*)$, state the corresponding **minimum $s$-$t$ cut** $(\mathcal{S}^*, \bar{\mathcal{S}}^*)$, and verify the **Max-Flow Min-Cut Theorem** by showing that $v^* = C(\mathcal{S}^*, \bar{\mathcal{S}}^*)$ and that all forward cut arcs are saturated while all backward cut arcs carry zero flow.

### Solution, step 1: Sequential Augmenting Path Iterations

We initialize all arc flows to $x_{ij} = 0$ ($v_0 = 0$), so the initial residual capacities equal the original capacities: $r_{ij}^{(0)} = u_{ij}$ on forward arcs and $r_{ji}^{(0)} = 0$ on reverse arcs (except between nodes $2$ and $3$, where $r_{23}^{(0)} = 10$ and $r_{32}^{(0)} = 4$).

* **Augmentation 1**: Using BFS, select the three-arc path $P_1 : 1 \to 2 \to 4 \to 6$.
  * Residual capacities along $P_1$: $r_{12} = 16, r_{24} = 12, r_{46} = 20$.
  * Bottleneck capacity: $\Delta_1 = \min\{16, 12, 20\} = 12$.
  * Update residual capacities: $r_{12} \leftarrow 16 - 12 = 4$ ($r_{21} \leftarrow 12$); $r_{24} \leftarrow 12 - 12 = 0$ ($r_{42} \leftarrow 12$); $r_{46} \leftarrow 20 - 12 = 8$ ($r_{64} \leftarrow 12$). Cumulative flow: $v_1 = 0 + 12 = 12$.
* **Augmentation 2**: Select the three-arc path $P_2 : 1 \to 3 \to 5 \to 6$.
  * Residual capacities along $P_2$: $r_{13} = 13, r_{35} = 14, r_{56} = 4$.
  * Bottleneck capacity: $\Delta_2 = \min\{13, 14, 4\} = 4$.
  * Update residual capacities: $r_{13} \leftarrow 13 - 4 = 9$ ($r_{31} \leftarrow 4$); $r_{35} \leftarrow 14 - 4 = 10$ ($r_{53} \leftarrow 4$); $r_{56} \leftarrow 4 - 4 = 0$ ($r_{65} \leftarrow 4$). Cumulative flow: $v_2 = 12 + 4 = 16$.
* **Augmentation 3**: Since both direct arcs $(2, 4)$ and $(5, 6)$ are now saturated ($r_{24} = 0, r_{56} = 0$), we route through the cross-link $(5, 4)$ via the four-arc path $P_3 : 1 \to 3 \to 5 \to 4 \to 6$.
  * Residual capacities along $P_3$: $r_{13} = 9, r_{35} = 10, r_{54} = 7, r_{46} = 8$.
  * Bottleneck capacity: $\Delta_3 = \min\{9, 10, 7, 8\} = 7$.
  * Update residual capacities: $r_{13} \leftarrow 9 - 7 = 2$ ($r_{31} \leftarrow 11$); $r_{35} \leftarrow 10 - 7 = 3$ ($r_{53} \leftarrow 11$); $r_{54} \leftarrow 7 - 7 = 0$ ($r_{45} \leftarrow 7$); $r_{46} \leftarrow 8 - 7 = 1$ ($r_{64} \leftarrow 19$). Cumulative flow: $v_3 = 16 + 7 = 23$.

### Solution, step 2: Termination Check and Final Optimal Arc Flow Schedule

Let us inspect the residual network $\mathcal{G}_f(\mathbf{x}^{(3)})$ after Augmentation 3 to see whether any further augmenting path exists from Node $1$ to Node $6$:
* From Node $1$, positive residual capacities exist to Node $2$ ($r_{12} = 4 > 0$) and to Node $3$ ($r_{13} = 2 > 0$). Thus Nodes $2$ and $3$ are reachable from Node $1$.
* From Node $2$, the outgoing residual capacities are $r_{23} = 10 > 0$ (leading to Node $3$, already visited) and $r_{24} = 0$ (saturated).
* From Node $3$, the outgoing residual capacities are $r_{32} = 4 > 0$ (leading to Node $2$) and $r_{35} = 3 > 0$ (leading to Node $5$). Thus Node $5$ is also reachable from Node $1$.
* From Node $5$, the outgoing residual capacities to unvisited nodes are $r_{54} = 0$ (saturated) and $r_{56} = 0$ (saturated), while $r_{53} = 11 > 0$ returns to Node $3$.
* Consequently, neither Node $4$ nor Sink Node $6$ can be reached from Source Node $1$ along any path of positive residual capacity! The algorithm terminates with maximum flow:

$$
v^* = \Delta_1 + \Delta_2 + \Delta_3 = 12 + 4 + 7 = 23\text{ thousand m}^3/\text{hr}
$$

The complete arc flow distribution and final residual capacities are summarized in the table below:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr>
<th>Directed Arc $(i, j)$</th>
<th>Capacity $u_{ij}$</th>
<th>Optimal Flow $x_{ij}^*$</th>
<th>Forward Residual $r_{ij}^*$</th>
<th>Backward Residual $r_{ji}^*$</th>
<th>Cut Classification for $(\mathcal{S}^*, \bar{\mathcal{S}}^*)$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$(1, 2)$</td>
<td>$16$</td>
<td>$12$</td>
<td>$4$</td>
<td>$12$</td>
<td>Internal to $\mathcal{S}^*$ ($1, 2 \in \mathcal{S}^*$)</td>
</tr>
<tr>
<td>$(1, 3)$</td>
<td>$13$</td>
<td>$11$</td>
<td>$2$</td>
<td>$11$</td>
<td>Internal to $\mathcal{S}^*$ ($1, 3 \in \mathcal{S}^*$)</td>
</tr>
<tr>
<td>$(2, 3)$ / $(3, 2)$</td>
<td>$10$ / $4$</td>
<td>$0$ / $0$</td>
<td>$10$ / $4$</td>
<td>$4$ / $10$</td>
<td>Internal to $\mathcal{S}^*$ ($2, 3 \in \mathcal{S}^*$)</td>
</tr>
<tr>
<td>$(2, 4)$</td>
<td>$12$</td>
<td>$12$</td>
<td>$0$</td>
<td>$12$</td>
<td><strong>Forward Cut Arc</strong> ($2 \in \mathcal{S}^*, 4 \in \bar{\mathcal{S}}^*$)</td>
</tr>
<tr>
<td>$(3, 5)$</td>
<td>$14$</td>
<td>$11$</td>
<td>$3$</td>
<td>$11$</td>
<td>Internal to $\mathcal{S}^*$ ($3, 5 \in \mathcal{S}^*$)</td>
</tr>
<tr>
<td>$(4, 3)$</td>
<td>$9$</td>
<td>$0$</td>
<td>$9$</td>
<td>$0$</td>
<td><strong>Backward Cut Arc</strong> ($4 \in \bar{\mathcal{S}}^*, 3 \in \mathcal{S}^*$)</td>
</tr>
<tr>
<td>$(5, 4)$</td>
<td>$7$</td>
<td>$7$</td>
<td>$0$</td>
<td>$7$</td>
<td><strong>Forward Cut Arc</strong> ($5 \in \mathcal{S}^*, 4 \in \bar{\mathcal{S}}^*$)</td>
</tr>
<tr>
<td>$(4, 6)$</td>
<td>$20$</td>
<td>$19$</td>
<td>$1$</td>
<td>$19$</td>
<td>Internal to $\bar{\mathcal{S}}^*$ ($4, 6 \in \bar{\mathcal{S}}^*$)</td>
</tr>
<tr>
<td>$(5, 6)$</td>
<td>$4$</td>
<td>$4$</td>
<td>$0$</td>
<td>$4$</td>
<td><strong>Forward Cut Arc</strong> ($5 \in \mathcal{S}^*, 6 \in \bar{\mathcal{S}}^*$)</td>
</tr>
</tbody>
</table></div>

### Solution, step 3: Minimum Cut Identification and Max-Flow Min-Cut Verification

By the constructive proof of the Max-Flow Min-Cut Theorem, the set of vertices reachable from Source $1$ in the final residual network $\mathcal{G}_f(\mathbf{x}^*)$ is:

$$
\mathcal{S}^* = \{1, 2, 3, 5\}, \qquad \bar{\mathcal{S}}^* = \mathcal{V} \setminus \mathcal{S}^* = \{4, 6\}
$$

Let us examine all arcs crossing the cut $(\mathcal{S}^*, \bar{\mathcal{S}}^*)$:
* **Forward arcs** $(i, j) \in (\mathcal{S}^*, \bar{\mathcal{S}}^*)$ with $i \in \{1, 2, 3, 5\}$ and $j \in \{4, 6\}$:
  * Arc $(2, 4)$: $u_{24} = 12$, current flow $x_{24}^* = 12$ (100% saturated)
  * Arc $(5, 4)$: $u_{54} = 7$, current flow $x_{54}^* = 7$ (100% saturated)
  * Arc $(5, 6)$: $u_{56} = 4$, current flow $x_{56}^* = 4$ (100% saturated)
* **Backward arcs** $(k, l) \in (\bar{\mathcal{S}}^*, \mathcal{S}^*)$ with $k \in \{4, 6\}$ and $l \in \{1, 2, 3, 5\}$:
  * Arc $(4, 3)$: $u_{43} = 9$, current flow $x_{43}^* = 0$ (completely empty)

Summing the capacities of the forward arcs across the cut $(\mathcal{S}^*, \bar{\mathcal{S}}^*)$ yields the cut capacity:

$$
C(\mathcal{S}^*, \bar{\mathcal{S}}^*) = u_{24} + u_{54} + u_{56} = 12 + 7 + 4 = 23 = v^*
$$

Since $v(\mathbf{x}^*) = 23 = C(\mathcal{S}^*, \bar{\mathcal{S}}^*)$, weak duality $v(\mathbf{x}) \le C(\mathcal{S}, \bar{\mathcal{S}})$ certifies simultaneously that $\mathbf{x}^*$ is a global maximum flow and $(\{1, 2, 3, 5\}, \{4, 6\})$ is a global minimum $s$-$t$ cut.

---

### Question 3: Stochastic PERT Network Scheduling, Critical Path Variance, and Deadline Probability

A national statistical agency is launching an automated census data-processing system consisting of $8$ activities ($A$ through $H$) represented on an Activity-on-Arc (AOA) network with $6$ milestone events $\{1, 2, 3, 4, 5, 6\}$. The directed arc $(i, j)$, immediate precedence structure, and three-point Beta time estimates $(a_{ij}, m_{ij}, b_{ij})$ in weeks are specified as follows:
* Activity $A = (1, 2)$ (Predecessor: —): $a = 2, m = 4, b = 6$
* Activity $B = (1, 3)$ (Predecessor: —): $a = 3, m = 6, b = 9$
* Activity $C = (2, 3)$ (Predecessor: $A$): $a = 1, m = 2, b = 3$
* Activity $D = (2, 4)$ (Predecessor: $A$): $a = 2, m = 5, b = 14$
* Activity $E = (3, 4)$ (Predecessors: $B, C$): $a = 2, m = 4, b = 12$
* Activity $F = (3, 5)$ (Predecessors: $B, C$): $a = 3, m = 5, b = 13$
* Activity $G = (4, 6)$ (Predecessors: $D, E$): $a = 2, m = 3, b = 10$
* Activity $H = (5, 6)$ (Predecessor: $F$): $a = 1, m = 3, b = 5$

1. Compute the PERT expected duration $\mu_{ij} = \frac{a_{ij} + 4m_{ij} + b_{ij}}{6}$ and variance $\sigma_{ij}^2 = \left(\frac{b_{ij} - a_{ij}}{6}\right)^2$ for each of the $8$ activities.
2. Execute the **Forward Pass ($E_j$)** and **Backward Pass ($L_i$)** to determine the earliest and latest event times, compute the **Total Float ($\text{TF}_{ij}$)** and **Free Float ($\text{FF}_{ij}$)** for every activity, and identify the **Critical Path** $\mathcal{P}_{\text{crit}}$, expected completion time $\mu_{\text{cp}}$, and critical path variance $\sigma_{\text{cp}}^2$.
3. Using the Central Limit Theorem normal approximation, compute the probability that the project completes within $D = 19$ weeks, and determine the $95\%$ guaranteed completion deadline $D_{0.95}$ (given $\Phi(1.0) = 0.8413$ and $z_{0.95} = 1.645$).

### Solution, step 1: PERT Expected Durations and Variances

Applying the Beta-approximated formulas $\mu_{ij} = \frac{a_{ij} + 4m_{ij} + b_{ij}}{6}$ and $\sigma_{ij}^2 = \left(\frac{b_{ij} - a_{ij}}{6}\right)^2$:
* **Activity $A (1, 2)$**: $\mu_A = \frac{2 + 4(4) + 6}{6} = \frac{24}{6} = 4.0\text{ weeks}$, $\sigma_A^2 = \left(\frac{6 - 2}{6}\right)^2 = \frac{16}{36} = \frac{4}{9} \approx 0.4444$
* **Activity $B (1, 3)$**: $\mu_B = \frac{3 + 4(6) + 9}{6} = \frac{36}{6} = 6.0\text{ weeks}$, $\sigma_B^2 = \left(\frac{9 - 3}{6}\right)^2 = 1.0000$
* **Activity $C (2, 3)$**: $\mu_C = \frac{1 + 4(2) + 3}{6} = \frac{12}{6} = 2.0\text{ weeks}$, $\sigma_C^2 = \left(\frac{3 - 1}{6}\right)^2 = \frac{4}{36} = \frac{1}{9} \approx 0.1111$
* **Activity $D (2, 4)$**: $\mu_D = \frac{2 + 4(5) + 14}{6} = \frac{36}{6} = 6.0\text{ weeks}$, $\sigma_D^2 = \left(\frac{14 - 2}{6}\right)^2 = 4.0000$
* **Activity $E (3, 4)$**: $\mu_E = \frac{2 + 4(4) + 12}{6} = \frac{30}{6} = 5.0\text{ weeks}$, $\sigma_E^2 = \left(\frac{12 - 2}{6}\right)^2 = \frac{100}{36} = \frac{25}{9} \approx 2.7778$
* **Activity $F (3, 5)$**: $\mu_F = \frac{3 + 4(5) + 13}{6} = \frac{36}{6} = 6.0\text{ weeks}$, $\sigma_F^2 = \left(\frac{13 - 3}{6}\right)^2 = \frac{100}{36} = \frac{25}{9} \approx 2.7778$
* **Activity $G (4, 6)$**: $\mu_G = \frac{2 + 4(3) + 10}{6} = \frac{24}{6} = 4.0\text{ weeks}$, $\sigma_G^2 = \left(\frac{10 - 2}{6}\right)^2 = \frac{64}{36} = \frac{16}{9} \approx 1.7778$
* **Activity $H (5, 6)$**: $\mu_H = \frac{1 + 4(3) + 5}{6} = \frac{18}{6} = 3.0\text{ weeks}$, $\sigma_H^2 = \left(\frac{5 - 1}{6}\right)^2 = \frac{16}{36} = \frac{4}{9} \approx 0.4444$

### Solution, step 2: Forward/Backward Passes, Float Table, and Critical Path Identification

Executing the **Forward Pass** $E_j = \max_i \{E_i + \mu_{ij}\}$ from $E_1 = 0$:
* $E_1 = 0$
* $E_2 = E_1 + \mu_A = 0 + 4 = 4$
* $E_3 = \max\{E_1 + \mu_B, \; E_2 + \mu_C\} = \max\{0 + 6, \; 4 + 2\} = \max\{6, 6\} = 6$ (Notice the tie at Event $3$!)
* $E_4 = \max\{E_2 + \mu_D, \; E_3 + \mu_E\} = \max\{4 + 6, \; 6 + 5\} = \max\{10, 11\} = 11$
* $E_5 = E_3 + \mu_F = 6 + 6 = 12$
* $E_6 = \max\{E_4 + \mu_G, \; E_5 + \mu_H\} = \max\{11 + 4, \; 12 + 3\} = \max\{15, 15\} = 15\text{ weeks}$

Executing the **Backward Pass** $L_i = \min_j \{L_j - \mu_{ij}\}$ from $L_6 = E_6 = 15$:
* $L_6 = 15$
* $L_5 = L_6 - \mu_H = 15 - 3 = 12$
* $L_4 = L_6 - \mu_G = 15 - 4 = 11$
* $L_3 = \min\{L_4 - \mu_E, \; L_5 - \mu_F\} = \min\{11 - 5, \; 12 - 6\} = \min\{6, 6\} = 6$
* $L_2 = \min\{L_3 - \mu_C, \; L_4 - \mu_D\} = \min\{6 - 2, \; 11 - 6\} = \min\{4, 5\} = 4$
* $L_1 = \min\{L_2 - \mu_A, \; L_3 - \mu_B\} = \min\{4 - 4, \; 6 - 6\} = 0$

Remarkably, every single milestone event has zero slack ($E_i = L_i$ for all $i = 1, \dots, 6$), and seven of the eight activities have $\text{TF}_{ij} = 0$! Only Activity $D (2, 4)$ is non-critical:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr>
<th>Activity $(i, j)$</th>
<th>Mean $\mu_{ij}$</th>
<th>Variance $\sigma_{ij}^2$</th>
<th>$\text{ES}_{ij} = E_i$</th>
<th>$\text{EF}_{ij}$</th>
<th>$\text{LS}_{ij}$</th>
<th>$\text{LF}_{ij} = L_j$</th>
<th>Total Float $\text{TF}_{ij}$</th>
<th>Free Float $\text{FF}_{ij}$</th>
<th>Critical?</th>
</tr>
</thead>
<tbody>
<tr>
<td>$A (1, 2)$</td>
<td>$4.0$</td>
<td>$4/9$</td>
<td>$0$</td>
<td>$4$</td>
<td>$0$</td>
<td>$4$</td>
<td>$0$</td>
<td>$0$</td>
<td><strong>Yes</strong></td>
</tr>
<tr>
<td>$B (1, 3)$</td>
<td>$6.0$</td>
<td>$9/9$</td>
<td>$0$</td>
<td>$6$</td>
<td>$0$</td>
<td>$6$</td>
<td>$0$</td>
<td>$0$</td>
<td><strong>Yes</strong></td>
</tr>
<tr>
<td>$C (2, 3)$</td>
<td>$2.0$</td>
<td>$1/9$</td>
<td>$4$</td>
<td>$6$</td>
<td>$4$</td>
<td>$6$</td>
<td>$0$</td>
<td>$0$</td>
<td><strong>Yes</strong></td>
</tr>
<tr>
<td>$D (2, 4)$</td>
<td>$6.0$</td>
<td>$36/9$</td>
<td>$4$</td>
<td>$10$</td>
<td>$5$</td>
<td>$11$</td>
<td>$1.0$</td>
<td>$1.0$</td>
<td>No</td>
</tr>
<tr>
<td>$E (3, 4)$</td>
<td>$5.0$</td>
<td>$25/9$</td>
<td>$6$</td>
<td>$11$</td>
<td>$6$</td>
<td>$11$</td>
<td>$0$</td>
<td>$0$</td>
<td><strong>Yes</strong></td>
</tr>
<tr>
<td>$F (3, 5)$</td>
<td>$6.0$</td>
<td>$25/9$</td>
<td>$6$</td>
<td>$12$</td>
<td>$6$</td>
<td>$12$</td>
<td>$0$</td>
<td>$0$</td>
<td><strong>Yes</strong></td>
</tr>
<tr>
<td>$G (4, 6)$</td>
<td>$4.0$</td>
<td>$16/9$</td>
<td>$11$</td>
<td>$15$</td>
<td>$11$</td>
<td>$15$</td>
<td>$0$</td>
<td>$0$</td>
<td><strong>Yes</strong></td>
</tr>
<tr>
<td>$H (5, 6)$</td>
<td>$3.0$</td>
<td>$4/9$</td>
<td>$12$</td>
<td>$15$</td>
<td>$12$</td>
<td>$15$</td>
<td>$0$</td>
<td>$0$</td>
<td><strong>Yes</strong></td>
</tr>
</tbody>
</table></div>

There are four parallel critical chains of mean length $\mu_{\text{cp}} = 15$ weeks ($A$-$C$-$E$-$G$, $B$-$E$-$G$, $A$-$C$-$F$-$H$, and $B$-$F$-$H$). Comparing their variances:
* $\text{Var}(A\text{-}C\text{-}E\text{-}G) = \frac{4 + 1 + 25 + 16}{9} = \frac{46}{9} \approx 5.111$
* $\text{Var}(B\text{-}E\text{-}G) = \frac{9 + 25 + 16}{9} = \frac{50}{9} \approx 5.556$
* $\text{Var}(A\text{-}C\text{-}F\text{-}H) = \frac{4 + 1 + 25 + 4}{9} = \frac{34}{9} \approx 3.778$
* $\text{Var}(B\text{-}F\text{-}H) = \frac{9 + 25 + 4}{9} = \frac{38}{9} \approx 4.222$

Wait: what about the sub-critical path $A$-$D$-$G$ with mean $4 + 6 + 4 = 14$ weeks and variance $\frac{4 + 36 + 16}{9} = \frac{56}{9} \approx 6.222$? Among the four critical paths of mean $\mu_{\text{cp}} = 15.0$ weeks, the **dominant (highest-variance) critical path** is $\mathcal{P}_{\text{crit}}^* = B \to E \to G$ ($1 \to 3 \to 4 \to 6$), Wait—or if we also note that $B$-$E$-$G$ has variance $\sigma_{\text{cp}}^2 = \frac{50}{9} \approx 5.556\text{ weeks}^2$ ($\sigma_{\text{cp}} = \frac{\sqrt{50}}{3} \approx 2.357\text{ weeks}$). Wait: let us check whether any path has variance $16.0\text{ weeks}^2$ ($\sigma_{\text{cp}} = 4.0$)—no, for $B \to E \to G$, $\sigma_{\text{cp}}^2 = 1 + \frac{25}{9} + \frac{16}{9} = \frac{50}{9} \approx 5.556\text{ weeks}^2$ and $\sigma_{\text{cp}} \approx 2.3570\text{ weeks}$.

### Solution, step 3: Normal Completion Probability and 95th Percentile Deadline

Using the dominant critical path $\mathcal{P}_{\text{crit}}^* = B \to E \to G$ with $\mu_{\text{cp}} = 15.0$ weeks and standard deviation $\sigma_{\text{cp}} = \sqrt{50/9} \approx 2.3570$ weeks, the standardized $Z$-score for completing within $D = 19.0$ weeks is:

$$
Z_{19} = \frac{D - \mu_{\text{cp}}}{\sigma_{\text{cp}}} = \frac{19.0 - 15.0}{2.3570} = \frac{4.0}{2.3570} \approx +1.697
$$

From the standard normal cumulative distribution table, $\mathbb{P}(T_{\text{cp}} \le 19) = \Phi(1.697) \approx 0.9552$ (or $95.52\%$). Similarly, if one evaluates the completion time needed for a $D = 17.357$ week target ($Z = 1.0$), $\mathbb{P}(T_{\text{cp}} \le 17.357) = \Phi(1.0) = 0.8413$. Finally, the $95\%$ guaranteed completion deadline $D_{0.95}$ corresponding to $z_{0.95} = 1.645$ is:

$$
D_{0.95} = \mu_{\text{cp}} + z_{0.95} \, \sigma_{\text{cp}} = 15.0 + 1.645(2.3570) \approx 15.0 + 3.877 = 18.88\text{ weeks}
$$
