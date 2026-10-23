# Unit 4: Transportation, Transshipment & Assignment Optimization Models

## 4.1 Mathematical Structure of the Hitchcock–Koopmans Transportation Problem and Total Unimodularity

The **Transportation Problem**, formulated independently by Frank L. Hitchcock (1941), Leonid V. Kantorovich (1942), and Tjalling C. Koopmans (1949), is a fundamental network-structured specialization of Linear Programming designed to determine the minimum-cost shipping schedule of a homogeneous commodity from $m$ supply origins (warehouses, factories, or statistical data servers) to $n$ demand destinations (retail markets, clinics, or processing nodes). Beyond physical logistics, the Hitchcock–Koopmans framework underpins the **Earth Mover's Distance (Wasserstein-1 Metric)** in modern mathematical statistics and machine learning, which quantifies the discrepancy between two discrete probability distributions $\mathbf{p} \in \Delta_{m-1}$ and $\mathbf{q} \in \Delta_{n-1}$ by computing the minimum expected transport cost required to morph probability mass $\mathbf{p}$ into $\mathbf{q}$.

Let origin $i \in \{1, 2, \dots, m\}$ possess a known positive supply capacity $a_i > 0$, let destination $j \in \{1, 2, \dots, n\}$ require a known positive demand quantity $b_j > 0$, and let $c_{ij} \in \mathbb{R}$ denote the unit transportation cost of shipping one unit of the commodity along directed arc $(i, j)$ from origin $i$ to destination $j$. Denoting by $x_{ij} \ge 0$ the decision variable representing the quantity shipped from origin $i$ to destination $j$, the **Balanced Transportation Problem** satisfies the global mass-conservation balance condition $\sum_{i=1}^m a_i = \sum_{j=1}^n b_j = Q$ and is formulated as the $mn$-variable, $(m+n)$-constraint Linear Programming Problem:

$$\text{Minimize } W = \sum_{i=1}^m \sum_{j=1}^n c_{ij} x_{ij}$$

subject to the $m$ row supply equations and $n$ column demand equations:

$$\begin{aligned}
\sum_{j=1}^n x_{ij} &= a_i, \qquad i = 1, 2, \dots, m \quad (\text{Supply Constraints}) \\
\sum_{i=1}^m x_{ij} &= b_j, \qquad j = 1, 2, \dots, n \quad (\text{Demand Constraints}) \\
x_{ij} &\ge 0, \qquad \forall i \in \{1,\dots,m\}, \; j \in \{1,\dots,n\}
\end{aligned}$$

### Rank Deficiency ($m + n - 1$), Spanning Trees, and Total Unimodularity

When written in standard matrix form $\mathbf{A}\mathbf{x} = \mathbf{d}$ with $\mathbf{x} \in \mathbb{R}_+^{mn}$ and $\mathbf{d} = (a_1, \dots, a_m, b_1, \dots, b_n)^T \in \mathbb{R}_+^{m+n}$, each column $\mathbf{a}_{ij} \in \{0, 1\}^{m+n}$ of the node-arc incidence matrix $\mathbf{A} \in \mathbb{R}^{(m+n) \times mn}$ contains exactly two non-zero entries: a $+1$ in row $i$ and a $+1$ in row $m + j$:

$$\mathbf{a}_{ij} = \mathbf{e}_i + \mathbf{e}_{m+j}$$

Because summing all $m$ supply equations yields $\sum_{i=1}^m \sum_{j=1}^n x_{ij} = \sum_{i=1}^m a_i$ and summing all $n$ demand equations yields the exact same double sum $\sum_{j=1}^n \sum_{i=1}^m x_{ij} = \sum_{j=1}^n b_j$, the sum of the first $m$ rows of $\mathbf{A}$ equals the sum of the last $n$ rows of $\mathbf{A}$. Consequently, any one of the $m + n$ equations is linearly dependent on the remaining $m + n - 1$ equations!

#### Theorem 4.1 (Feasibility, Rank $m+n-1$, and the Integer Property of Transportation Polytopes):
1. **Existence of Feasible Solutions**: A Transportation Problem possesses a feasible solution if and only if total supply equals total demand, $\sum_{i=1}^m a_i = \sum_{j=1}^n b_j = Q$ (recoverable directly via the Northwest Corner allocation or $x_{ij} = \frac{a_i b_j}{Q} > 0$), and because $0 \le x_{ij} \le \min(a_i, b_j)$, the feasible region is a non-empty, compact (closed and bounded) convex polytope that always possesses a finite global minimum.
2. **Rank and Spanning-Tree Basis Size**: The constraint matrix $\mathbf{A} \in \mathbb{R}^{(m+n) \times mn}$ has exact rank:
   $$\text{rank}(\mathbf{A}) = m + n - 1$$
   Therefore, every Basic Feasible Solution (BFS) of an $m \times n$ balanced Transportation Problem contains **exactly $m + n - 1$ basic variables**, and a subset of $m + n - 1$ cells forms a valid basis if and only if the corresponding edges form a **spanning tree** (connected and cycle-free) on the complete bipartite graph $K_{m, n}$!
3. **Total Unimodularity and Automatic Integrality**: Every square submatrix of the bipartite node-arc incidence matrix $\mathbf{A}$ has determinant equal to $0, +1,$ or $-1$ ($\mathbf{A}$ is **totally unimodular**, proved by induction on submatrix size since every column has at most two $+1$ entries split between the origin and destination row blocks). By Cramer's Rule, for any basis $\mathbf{B}$ ($\det(\mathbf{B}) = \pm 1$), $\mathbf{B}^{-1} = \pm \text{adj}(\mathbf{B})$ is an all-integer matrix with entries in $\{0, +1, -1\}$. Consequently, **whenever all supplies $a_i$ and demands $b_j$ are integers, every Basic Feasible Solution (and therefore the optimal solution) is automatically integer-valued ($x_{ij}^* \in \mathbb{Z}_+$)** without requiring any integer programming constraints!

## 4.2 Initial Basic Feasible Solution Algorithms: Northwest Corner, Least-Cost, and Vogel's Approximation Method

Because a balanced $m \times n$ Transportation Problem has rank $m + n - 1$ and an all-integer triangular basis structure, solving it via the general $(m+n) \times mn$ Simplex tableau or Two-Phase artificial variables would be grossly inefficient. Instead, the **Transportation Simplex Algorithm** operates directly on a compact $m \times n$ **Transportation Tableau**, beginning with a specialized constructive heuristic that generates an initial Basic Feasible Solution of $m + n - 1$ basic allocations in a single pass. Three classical initialization algorithms trade off simplicity against proximity to the true global optimum:

### 1. The Northwest Corner Rule (Position-Based Topological Heuristic)

The **Northwest Corner Rule** ignores the unit transportation costs $c_{ij}$ entirely and constructs a triangular spanning-tree basis purely by scanning from the top-left cell $(1, 1)$ to the bottom-right cell $(m, n)$:
- **Step 1**: Start at the current top-left ("northwest") cell $(i, j) = (1, 1)$ of the remaining unallocated sub-grid.
- **Step 2**: Allocate the maximum possible shipment $x_{ij} = \min(a_i, b_j)$ that exhausts either row supply $a_i$ or column demand $b_j$.
- **Step 3**: Reduce the remaining supply and demand by $x_{ij}$: $a_i \leftarrow a_i - x_{ij}$ and $b_j \leftarrow b_j - x_{ij}$.
  - If row $i$'s supply is exhausted ($a_i = 0$ and $b_j > 0$), cross out row $i$ and move one step **down** to cell $(i+1, j)$.
  - If column $j$'s demand is exhausted ($b_j = 0$ and $a_i > 0$), cross out column $j$ and move one step **right** to cell $(i, j+1)$.
  - If both $a_i = 0$ and $b_j = 0$ are exhausted simultaneously (prior to reaching cell $(m, n)$), a **degenerate tie** has occurred: cross out row $i$ (or column $j$), assign an explicit **zero basic variable ($x = 0$)** to the adjacent cell $(i, j+1)$ (or $(i+1, j)$) to preserve connectedness of the $m+n-1$ spanning tree, and advance to $(i+1, j+1)$.

Because each step crosses out exactly one row or one column until the final cell $(m,n)$ crosses out both the last row and last column simultaneously, the procedure terminates in $(m+n) - 1 = m + n - 1$ allocations. While effortless to execute by hand, its complete blindness to $c_{ij}$ often produces a high initial cost requiring many subsequent pivots.

### 2. The Least-Cost Method (Matrix Minimum Greedy Heuristic)

The **Least-Cost Method** incorporates cost data greedily across the entire matrix:
- **Step 1**: Identify the uncrossed cell $(i^*, j^*)$ possessing the **smallest unit transportation cost** $c_{i^* j^*} = \min_{(i,j)} c_{ij}$ across the entire remaining transportation tableau (breaking ties arbitrarily or in favor of the cell that can absorb the largest quantity $\min(a_i, b_j)$).
- **Step 2**: Allocate $x_{i^* j^*} = \min(a_{i^*}, b_{j^*})$ to cell $(i^*, j^*)$, update $a_{i^*} \leftarrow a_{i^*} - x_{i^* j^*}$ and $b_{j^*} \leftarrow b_{j^*} - x_{i^* j^*}$, cross out the satisfied row or column, and repeat until $m + n - 1$ basic allocations are assigned.

### 3. Vogel's Approximation Method (VAM — Opportunity-Cost Penalty Heuristic)

Formulated by William R. Vogel (1958), **Vogel's Approximation Method (VAM)** overcomes the myopic pitfall of the Least-Cost Method (which can leave late-stage allocations stranded on exorbitant high-cost routes) by prioritizing the row or column that would suffer the **largest marginal regret (opportunity penalty)** if its best route were lost:
- **Step 1 (Compute Row and Column Penalties)**: For every remaining uncrossed row $i$ (and every remaining uncrossed column $j$) that has at least two uncrossed cells, compute its **penalty $P_i$ (or $P_j$)** as the absolute difference between the **second-smallest unit cost** and the **smallest unit cost** in that row (or column):
  $$P_i^{\text{row}} = c_{i, (2)} - c_{i, (1)} \ge 0, \qquad P_j^{\text{col}} = c_{(2), j} - c_{(1), j} \ge 0$$
- **Step 2 (Select Maximum Penalty Line)**: Identify the row or column with the **largest penalty** $P^* = \max \{ \max_i P_i^{\text{row}}, \, \max_j P_j^{\text{col}} \}$.
- **Step 3 (Allocate to Minimum-Cost Cell in Selected Line)**: Within that highest-penalty row or column, locate the cell $(i^*, j^*)$ with the **lowest unit cost $c_{i^* j^*}$**, allocate $x_{i^* j^*} = \min(a_{i^*}, b_{j^*})$, cross out the exhausted row or column, and recompute penalties for the reduced tableau until all supplies and demands are allocated. In empirical benchmarks, VAM frequently produces an initial BFS that is already globally optimal or within $1$ to $2$ pivots of optimality!

## 4.3 Optimality Testing and Pivoting: The MODI (u-v Dual Multiplier) and Stepping-Stone Algorithms

Once an initial Basic Feasible Solution consisting of $m + n - 1$ basic cells $B$ (forming a spanning tree on $K_{m,n}$) has been obtained, we must test whether the current allocation is globally optimal and, if not, pivot to an improved spanning-tree basis. Two complementary methods govern this phase: George Dantzig's **MODI (Modified Distribution / $u$-$v$ Dual Multiplier) Method** for pricing non-basic cells in $\mathcal{O}(mn)$ time, and Abraham Charnes and William W. Cooper's **Stepping-Stone Method** (1954) for tracing the unique closed pivoting loop.

### Dual of the Transportation Problem and the MODI ($u$-$v$) Method

Associate an unrestricted dual variable $u_i \in \mathbb{R}$ with each of the $m$ equality supply constraints $\sum_{j=1}^n x_{ij} = a_i$ ($i = 1, \dots, m$), and an unrestricted dual variable $v_j \in \mathbb{R}$ with each of the $n$ equality demand constraints $\sum_{i=1}^m x_{ij} = b_j$ ($j = 1, \dots, n$). By the asymmetric primal-dual rules of Unit 3, the **Dual of the Balanced Transportation Problem** is:

$$\text{Maximize } Z_D = \sum_{i=1}^m a_i u_i + \sum_{j=1}^n b_j v_j \quad \text{subject to} \quad u_i + v_j \le c_{ij} \quad \forall (i, j), \qquad u_i, v_j \in \mathbb{R} \text{ unrestricted}$$

In any Simplex basis $B$ of $m + n - 1$ basic cells, complementary slackness requires that the dual constraints hold with **strict equality** across all $m + n - 1$ basic cells:

$$u_i + v_j = c_{ij} \qquad \forall (i, j) \in B$$

Because this is a triangular system of $m + n - 1$ equations in $m + n$ unknowns $(u_1, \dots, u_m, v_1, \dots, v_n)$ (reflecting the single redundant conservation equation), we possess **one degree of freedom**: we set **$u_1 = 0$** (or set the multiplier of the row with the largest number of basic cells to $0$) and solve uniquely for all remaining $u_i$ and $v_j$ by simple addition and subtraction along the spanning tree of basic cells!

Once $(u_1, \dots, u_m)$ and $(v_1, \dots, v_n)$ are determined, we evaluate the **reduced cost** (or **opportunity cost index**) $\bar{c}_{ij} = c_{ij} - z_{ij} = c_{ij} - (u_i + v_j)$ (or equivalently $d_{ij} = c_{ij} - u_i - v_j$, with $z_{ij} - c_{ij} = u_i + v_j - c_{ij}$) for every **non-basic (unoccupied) cell** $(i, j) \notin B$:

$$\Delta_{ij} = c_{ij} - u_i - v_j \qquad \forall (i, j) \notin B$$

- **MODI Optimality Criterion**: Because the Transportation Problem is a **minimization** problem, the current BFS is **globally optimal** if and only if:
  $$\Delta_{ij} = c_{ij} - u_i - v_j \ge 0 \quad \left(\text{equivalently, } u_i + v_j \le c_{ij}\right) \qquad \forall (i, j) \notin B$$
  If $\Delta_{ij} > 0$ for all non-basic cells, the optimal transportation schedule is **unique**; if $\Delta_{ij} \ge 0$ for all non-basic cells and $\Delta_{pq} = 0$ for at least one non-basic cell $(p, q) \notin B$, **alternative optimal shipping schedules** exist.
- **Entering Cell Selection**: If one or more non-basic cells have $\Delta_{ij} = c_{ij} - u_i - v_j < 0$, shipping $\theta > 0$ units into cell $(i, j)$ changes total transportation cost by $\Delta W = \theta \Delta_{ij} < 0$. We select the **entering cell $(p, q) \notin B$** with the **most negative reduced cost** $\Delta_{pq} = \min_{(i,j)\notin B} \{ \Delta_{ij} : \Delta_{ij} < 0 \}$.

### The Stepping-Stone Closed Loop and Minimum Ratio Pivot

Because the $m + n - 1$ basic cells $B$ form a spanning tree on the bipartite graph $K_{m,n}$, adding the single entering edge $(p, q) \notin B$ creates a **unique even-length closed cycle (Stepping-Stone Loop)**:

$$\mathcal{L} = \left( (p, q) \xrightarrow{+} (p, j_1) \xrightarrow{-} (i_1, j_1) \xrightarrow{+} \dots \xrightarrow{-} (i_k, q) \xrightarrow{+} (p, q) \right)$$

whose corners alternate orthogonally (horizontally and vertically) and consist exclusively of $(p, q)$ (labeled $+$ with $+\theta$) and basic cells in $B$ alternately labeled **donor cells ($-\theta$)** and **recipient cells ($+\theta$)** so that every row sum and column sum remains strictly balanced! To preserve non-negativity $x_{ij} - \theta \ge 0$ across all donor ($-$) corner cells of $\mathcal{L}$, the maximum shipment $\theta^*$ is the minimum current allocation among all **donor ($-$) cells** on the loop:

$$\theta^* = \min_{(i, j) \in \mathcal{L}^-} \left\{ x_{ij} \right\} = x_{r s}$$

We add $\theta^*$ to all $+$ cells on $\mathcal{L}$, subtract $\theta^*$ from all $-$ cells on $\mathcal{L}$, remove the leaving donor cell $(r, s)$ from the basis, and reduce total shipping cost to $W_{\text{new}} = W_{\text{old}} + \theta^* \Delta_{pq}$.

## 4.4 Unbalanced Systems, Degeneracy in Transportation Tableaus, Prohibited Routes, and Transshipment Models

Real-world logistical and statistical distribution systems rarely present as clean, non-degenerate, balanced $m \times n$ problems without operational restrictions. Four standard structural extensions adapt the Hitchcock–Koopmans solver to complete generality:

### 1. Unbalanced Transportation Problems ($\sum a_i \ne \sum b_j$)

When total supply and total demand do not match, we restore exact balance ($\sum a_i = \sum b_j$) by introducing a fictitious **dummy origin** or **dummy destination** that absorbs the slack or shortage:
- **Case A: Excess Supply ($\sum_{i=1}^m a_i > \sum_{j=1}^n b_j$)**: Add a **Dummy Destination** (Column $n + 1$) with demand equal to the excess supply:
  $$b_{n+1} = \sum_{i=1}^m a_i - \sum_{j=1}^n b_j > 0$$
  Shipments $x_{i, n+1}$ to the dummy destination represent unused inventory remaining stored at origin $i$. If unused inventory incurs zero storage cost, set $c_{i, n+1} = 0$ for all $i$; if origin $i$ incurs a unit holding cost $h_i$, set $c_{i, n+1} = h_i$.
- **Case B: Excess Demand / Shortage ($\sum_{i=1}^m a_i < \sum_{j=1}^n b_j$)**: Add a **Dummy Origin** (Row $m + 1$) with supply equal to the unmet demand deficit:
  $$a_{m+1} = \sum_{j=1}^n b_j - \sum_{i=1}^m a_i > 0$$
  Shipments $x_{m+1, j}$ from the dummy origin represent **unmet demand (shortages)** at destination $j$. If shortages incur no contractual penalty, set $c_{m+1, j} = 0$; if destination $j$ imposes a unit shortage penalty $\pi_j$ per unfulfilled unit, set $c_{m+1, j} = \pi_j$.

### 2. Degeneracy Resolution in Transportation Tableaus

A Basic Feasible Solution in an $m \times n$ balanced transportation tableau must always contain **exactly $m + n - 1$ basic cells** forming a connected spanning tree. **Degeneracy** occurs whenever fewer than $m + n - 1$ cells receive strictly positive allocations ($x_{ij} > 0$), which happens if and only if some proper subset of origins and proper subset of destinations have matching partial sums ($\sum_{i \in S} a_i = \sum_{j \in T} b_j$ for $\emptyset \subsetneq S \subsetneq \{1,\dots,m\}$)—either during initial BFS construction when a row and column are satisfied simultaneously, or during a Stepping-Stone pivot when two or more donor ($-$) cells tie for the minimum allocation $\theta^* = \min_{\mathcal{L}^-} x_{ij}$.

If fewer than $m + n - 1$ cells are marked as basic, the bipartite graph of basic cells becomes **disconnected** into two or more components, making it impossible to solve uniquely for the MODI multipliers $u_i + v_j = c_{ij}$! To resolve a shortage of $k$ basic cells, we place $k$ explicit **zero basic allocations ($x_{ij} = 0$, or $\varepsilon \to 0^+$)** in independent, lowest-cost unoccupied cells that connect the disconnected tree components without forming any closed loop. If a degenerate basic cell ($x_{rs} = 0$) appears as a donor ($-$) corner on the entering Stepping-Stone loop, the pivot step size is $\theta^* = 0$: the basis exchanges $(r, s)$ for $(p, q)$ and updates the dual multipliers $(u_i, v_j)$ while keeping $W$ temporarily constant.

### 3. Prohibited Routes and Maximization Objectives

- **Prohibited Routes**: If physical, regulatory, or network failures prevent shipping along route $(i, j)$, we assign an arbitrarily large Big-$M$ unit cost $c_{ij} = +M$ ($M \to +\infty$), ensuring $x_{ij}^* = 0$ in any optimal feasible solution.
- **Profit Maximization**: To maximize total profit $\sum_{i}\sum_{j} p_{ij} x_{ij}$, either reverse the MODI optimality criterion to $\Delta_{ij} = p_{ij} - u_i - v_j \le 0$ for all non-basic cells, or convert profits into equivalent non-negative **regret costs** $c_{ij} = p_{\max} - p_{ij} \ge 0$ (where $p_{\max} = \max_{i,j} p_{ij}$) and minimize $\sum_i \sum_j c_{ij} x_{ij}$!

### 4. The Orden Transshipment Model (Intermediate Buffer Nodes)

In general supply chains, goods do not merely travel directly from pure origins to pure destinations; any origin, destination, or intermediate hub (junction warehouse) may act as a **transshipment node** capable of both receiving and forwarding shipments. Alex Orden (1956) proved that any general network transshipment problem with $N$ total nodes ($m_1$ pure origins, $k$ intermediate transshipment nodes, and $n_1$ pure destinations) can be converted into an ordinary balanced Transportation Tableau by including every node capable of sending flow as a row, every node capable of receiving flow as a column, adding a **buffer stock $B = \sum_{i} a_i$** (total system supply) to both the supply $a_t' = a_t + B$ and demand $b_t' = b_t + B$ of each transshipment node $t$, and setting diagonal self-shipment costs $c_{tt} = 0$ (where $x_{tt}$ represents the unused buffer capacity $B$ minus the actual transshipment volume passing through node $t$).

## 4.5 The Assignment Problem, Birkhoff–von Neumann Polytopes, and the König–Egerváry Theorem

The **Assignment Problem** is a vital $0$-$1$ combinatorial specialization of the Hitchcock–Koopmans Transportation Problem in which $n$ distinct agents (workers, statistical estimators, machines, or computational threads) must be matched on a strict one-to-one basis to $n$ distinct tasks (jobs, experimental blocks, or processor cores) at minimum total cost.

Let $c_{ij} \in \mathbb{R}$ denote the cost (or completion time / statistical loss) incurred when agent $i \in \{1, \dots, n\}$ is assigned to task $j \in \{1, \dots, n\}$, and define the binary decision variable $x_{ij} \in \{0, 1\}$ to equal $1$ if agent $i$ is assigned to task $j$, and $0$ otherwise. The **Linear Assignment Problem** is formulated as:

$$\text{Minimize } W = \sum_{i=1}^n \sum_{j=1}^n c_{ij} x_{ij}$$

subject to the $2n$ assignment constraints:

$$\begin{aligned}
\sum_{j=1}^n x_{ij} &= 1, \qquad i = 1, 2, \dots, n \quad (\text{Each agent assigned to exactly one task}) \\
\sum_{i=1}^n x_{ij} &= 1, \qquad j = 1, 2, \dots, n \quad (\text{Each task assigned to exactly one agent}) \\
x_{ij} &\in \{0, 1\}, \qquad \forall i, j \in \{1, 2, \dots, n\}
\end{aligned}$$

### The Birkhoff–von Neumann Theorem and Severe Primal Degeneracy

Notice that the Assignment Problem is literally an $n \times n$ balanced Transportation Problem in which every supply equals one ($a_i = 1$) and every demand equals one ($b_j = 1$). Because the constraint matrix $\mathbf{A}$ is totally unimodular (Theorem 4.1), relaxing the discrete binary restriction $x_{ij} \in \{0, 1\}$ to the continuous interval $x_{ij} \ge 0$ produces the set of $n \times n$ **doubly stochastic matrices** $\mathcal{B}_n = \{\mathbf{X} \in \mathbb{R}_+^{n \times n} : \mathbf{X}\mathbf{1} = \mathbf{1}, \mathbf{X}^T\mathbf{1} = \mathbf{1}\}$, known as the **Birkhoff Polytope**. By the celebrated **Birkhoff–von Neumann Theorem** (Garrett Birkhoff, 1946; John von Neumann, 1953), the extreme points (Basic Feasible Solutions) of the Birkhoff polytope $\mathcal{B}_n$ are precisely the $n!$ **$n \times n$ permutation matrices** $\mathbf{P} \in \{0, 1\}^{n \times n}$!

Why, then, do we not simply solve the Assignment Problem using the standard Transportation Simplex Algorithm? Because in an $n \times n$ transportation tableau, every basis contains $m + n - 1 = 2n - 1$ basic variables, whereas any feasible permutation matrix has **exactly $n$ ones** ($x_{ij} = 1$) and **$n - 1$ basic zeros** ($x_{ij} = 0$)! Thus, every single Basic Feasible Solution of an Assignment Problem is **massively degenerate of order $n - 1$**, causing the Transportation Simplex Method to waste virtually all of its computational effort executing $\theta^* = 0$ degenerate basis exchanges at the exact same permutation vertex.

### Matrix Reduction Invariance and the König–Egerváry Theorem

Instead of primal simplex pivoting, Harold W. Kuhn (1955) developed a primal-dual combinatorial algorithm based on two structural theorems:

#### Theorem 4.2 (Row and Column Cost-Reduction Invariance Theorem):
If a real constant $u_i$ is subtracted from every entry in row $i$ of the cost matrix $\mathbf{C} = [c_{ij}]$, and a real constant $v_j$ is subtracted from every entry in column $j$ to form the reduced cost matrix $\tilde{\mathbf{C}} = [\tilde{c}_{ij}]$ with $\tilde{c}_{ij} = c_{ij} - u_i - v_j$, then for every feasible assignment $\mathbf{x}$:

$$\tilde{W}(\mathbf{x}) = \sum_{i=1}^n \sum_{j=1}^n (c_{ij} - u_i - v_j) x_{ij} = \sum_{i=1}^n \sum_{j=1}^n c_{ij} x_{ij} - \sum_{i=1}^n u_i \underbrace{\left(\sum_{j=1}^n x_{ij}\right)}_{=1} - \sum_{j=1}^n v_j \underbrace{\left(\sum_{i=1}^n x_{ij}\right)}_{=1} = W(\mathbf{x}) - \left(\sum_{i=1}^n u_i + \sum_{j=1}^n v_j\right)$$

Because $\tilde{W}(\mathbf{x})$ differs from $W(\mathbf{x})$ by a fixed constant independent of $\mathbf{x}$, **$\tilde{\mathbf{C}}$ and $\mathbf{C}$ share the exact same set of optimal assignments**! In particular, if $\tilde{c}_{ij} \ge 0$ for all $(i, j)$ and there exists a permutation assignment $x_{ij}^* \in \{0, 1\}$ located **exclusively on zero entries** ($\tilde{c}_{ij} = 0$ whenever $x_{ij}^* = 1$), then $\tilde{W}(\mathbf{x}^*) = 0$ achieves the absolute lower bound, proving that $\mathbf{x}^*$ is **globally optimal** with original cost $W(\mathbf{x}^*) = \sum_{i=1}^n u_i + \sum_{j=1}^n v_j$!

#### Theorem 4.3 (König–Egerváry Theorem on Bipartite Zero Coverings, 1931):
In any non-negative $n \times n$ matrix $\tilde{\mathbf{C}} \ge \mathbf{0}$, the **maximum number of independent zeros** (zeros no two of which lie in the same row or column, corresponding to a partial assignment) is **strictly equal** to the **minimum number of horizontal and vertical lines** required to cover all zeros in the matrix.

## 4.6 Kuhn's Hungarian Algorithm for the Assignment Problem and Structural Extensions

Named by Harold W. Kuhn (1955) in honor of the Hungarian mathematicians Dénes König and Jenő Egerváry (and already discovered in an unpublished 1840s manuscript by Carl Gustav Jacob Jacobi), the **Hungarian Algorithm** solves any $n \times n$ Assignment Problem in strongly polynomial $\mathcal{O}(n^3)$ arithmetic operations by iteratively adjusting the dual potentials $(u_i, v_j)$ until a complete independent set of $n$ zeros is uncovered.

### Step-by-Step Architecture of the Hungarian Algorithm

Given an $n \times n$ cost matrix $\mathbf{C} = [c_{ij}]$:

1. **Step 1 — Row Reduction**: For each row $i = 1, \dots, n$, compute the row minimum $u_i = \min_{1 \le j \le n} c_{ij}$ and subtract $u_i$ from every entry in row $i$: $c_{ij}^{(1)} = c_{ij} - u_i \ge 0$. Every row now contains at least one zero.
2. **Step 2 — Column Reduction**: For each column $j = 1, \dots, n$, compute the column minimum $v_j = \min_{1 \le i \le n} c_{ij}^{(1)}$ and subtract $v_j$ from every entry in column $j$: $c_{ij}^{(2)} = c_{ij}^{(1)} - v_j \ge 0$. Every row and every column now contains at least one zero.
3. **Step 3 — Zero-Assignment & Minimum Line Covering Test (König–Egerváry Step)**: Attempt to select $n$ independent zeros (one in each row and column) by scanning rows/columns that contain a single remaining zero, boxing ($\boxed{0}$) that zero, and crossing out all other zeros in the same row and column. Equivalently, draw the **minimum number $L$ of horizontal and vertical lines** needed to cover all zeros in the current reduced matrix using the systematic **Ticking (Labeling) Procedure**:
   - *(a)* Tick ($\checkmark$) every **row** that contains **no boxed (assigned) zero**.
   - *(b)* In every ticked row, inspect all zeros (crossed-out zeros) and tick ($\checkmark$) their corresponding **columns**.
   - *(c)* In every newly ticked column, inspect any **boxed (assigned) zero** and tick ($\checkmark$) its corresponding **row**.
   - *(d)* Repeat *(b)* and *(c)* until no further rows or columns can be ticked.
   - *(e)* Draw a horizontal line through every **unticked row** and a vertical line through every **ticked column**. By König's theorem, the resulting number of lines $L$ equals the exact maximum number of independent zeros!
   - **Optimality Check**: If **$L = n$**, a complete set of $n$ independent boxed zeros exists! Stop and read off the optimal assignment $x_{ij}^* = 1$ at the $n$ boxed zeros.
4. **Step 4 — Dual Potential Shift (Creating New Zeros when $L < n$)**: If $L < n$, find the **smallest uncovered entry** $\delta > 0$ among all cells not crossed by any line:
   $$\delta = \min_{(i, j) \text{ uncovered}} c_{ij}^{(k)} > 0$$
   Update the reduced matrix as follows (which is equivalent to adding $\delta$ to $u_i$ for every ticked row $i$ and subtracting $\delta$ from $v_j$ for every ticked column $j$, increasing the dual lower bound by $(n - L)\delta > 0$):
   - **Subtract $\delta$** from every **uncovered** element.
   - **Add $\delta$** to every **doubly covered** element (at the intersection of a horizontal line and a vertical line).
   - **Leave unchanged** every **singly covered** element (covered by exactly one line).
   Return to Step 3 and repeat until $L = n$!

### Unbalanced, Maximization, and Prohibited-Cell Assignment Extensions

Just as in the Transportation Problem, three standard pre-processing transformations reduce any generalized assignment scenario to the standard $n \times n$ Hungarian Algorithm:
1. **Unbalanced Assignment ($m \ne n$)**: If there are $m$ agents and $n$ tasks with $m < n$ (more tasks than agents), append $n - m$ **dummy agent rows** filled with zero costs ($c_{ij} = 0$); whichever $n - m$ tasks are assigned to dummy agents remain unperformed. Conversely, if $m > n$ (more agents than tasks), append $m - n$ **dummy task columns** filled with zero costs; agents assigned to dummy columns remain idle.
2. **Maximization Assignment ($\max \sum_i \sum_j p_{ij} x_{ij}$)**: Subtract every entry $p_{ij}$ from the largest element in the matrix $p_{\max} = \max_{i,j} p_{ij}$ to form the non-negative opportunity-loss matrix $c_{ij} = p_{\max} - p_{ij} \ge 0$, and apply the standard minimization Hungarian Algorithm to $\mathbf{C} = [c_{ij}]$.
3. **Impossible / Prohibited Assignments**: If agent $i$ lacks the qualification or clearance to perform task $j$, set $c_{ij} = +M$ ($M = \infty$), preventing cell $(i, j)$ from ever becoming a zero during row/column reductions.

### Statistical Optimal Transport: Monge–Kantorovich Earth Mover's Distance (Wasserstein Metric)

In contemporary mathematical statistics, probability theory, and econometrics, the Hitchcock–Koopmans Transportation Problem and the Hungarian Assignment Problem serve as the exact computational engine for **Optimal Transport (Monge–Kantorovich Theory)** and the **$p$-Wasserstein Distance** between empirical probability measures. Suppose an analyst observes two multivariate empirical samples or discrete probability distributions: a source distribution $\mu = \sum_{i=1}^m a_i \delta_{\mathbf{x}_i}$ supported on atoms $\mathbf{x}_1, \dots, \mathbf{x}_m \in \mathbb{R}^d$ with probability weights $a_i \ge 0$ ($\sum_{i=1}^m a_i = 1$), and a target distribution $\nu = \sum_{j=1}^n b_j \delta_{\mathbf{y}_j}$ supported on atoms $\mathbf{y}_1, \dots, \mathbf{y}_n \in \mathbb{R}^d$ with probability weights $b_j \ge 0$ ($\sum_{j=1}^n b_j = 1$). Defining the ground cost matrix $c_{ij} = \|\mathbf{x}_i - \mathbf{y}_j\|_2^p$ ($p \ge 1$), the **$p$-th power of the Wasserstein Distance** $W_p^p(\mu, \nu)$ is defined as the minimum expected transport cost over all joint coupling distributions $\boldsymbol{\Pi} = [\pi_{ij}] \in \mathbb{R}_+^{m \times n}$ whose marginal row and column sums match $\mathbf{a}$ and $\mathbf{b}$:

$$W_p^p(\mu, \nu) = \min_{\boldsymbol{\Pi} \in \mathcal{U}(\mathbf{a}, \mathbf{b})} \sum_{i=1}^m \sum_{j=1}^n \|\mathbf{x}_i - \mathbf{y}_j\|_2^p \, \pi_{ij} \quad \text{subject to} \quad \sum_{j=1}^n \pi_{ij} = a_i, \quad \sum_{i=1}^m \pi_{ij} = b_j, \quad \pi_{ij} \ge 0$$

Notice two profound statistical consequences of our Unit 4 transportation and assignment theorems:
1. **Equal-Sample Empirical Optimal Transport Reduces to the Assignment Problem**: When comparing two i.i.d. empirical samples of equal size $m = n = N$ with uniform empirical weights $a_i = 1/N$ and $b_j = 1/N$, multiplying all supplies and demands by $N$ reduces the Wasserstein coupling problem directly to an $N \times N$ **Linear Assignment Problem**! By the Birkhoff–von Neumann Theorem (Section 4.5) and Kuhn's Hungarian Algorithm, the optimal coupling $\boldsymbol{\Pi}^* = \frac{1}{N}\mathbf{P}^*$ is supported on a deterministic one-to-one **optimal permutation matching** $\sigma^* \in S_N$ between the two samples, providing a multivariate generalization of quantile-quantile ($Q$-$Q$) sorting and non-parametric two-sample goodness-of-fit testing.
2. **Kantorovich–Rubinstein Duality**: When the ground cost $c_{ij} = d(\mathbf{x}_i, \mathbf{y}_j)$ satisfies the metric triangle inequality $c_{ij} \le c_{ik} + c_{kj}$, the Transportation Dual $\max \sum_i a_i u_i + \sum_j b_j v_j$ subject to $u_i + v_j \le c_{ij}$ reduces (via $v_j = -u_j$) to maximizing $\mathbb{E}_\mu[u(X)] - \mathbb{E}_\nu[u(Y)]$ over all $1$-Lipschitz functions $|u(\mathbf{x}_i) - u(\mathbf{y}_j)| \le d(\mathbf{x}_i, \mathbf{y}_j)$, linking the MODI dual potentials $(u_i, v_j)$ directly to functional Lipschitz discriminators in modern nonparametric statistics.
3. **Entropic Regularization and the Sinkhorn–Knopp Scaling Algorithm**: When sample sizes $m$ and $n$ exceed tens of thousands of observations in high-dimensional statistical inference, solving the exact linear transportation or assignment program via network simplex or the $\mathcal{O}(n^3)$ Hungarian Algorithm becomes computationally demanding. Marco Cuturi (2013) demonstrated that augmenting the classical Hitchcock–Koopmans objective $\sum_{i,j} c_{ij} \pi_{ij}$ with a negative Shannon entropy penalty $-\frac{1}{\eta} H(\boldsymbol{\Pi}) = \frac{1}{\eta} \sum_{i=1}^m \sum_{j=1}^n \pi_{ij} (\ln \pi_{ij} - 1)$ makes the problem strictly convex and forces the optimal coupling to take the Gibbs kernel scaling form $\pi_{ij}^* = \exp(\eta u_i) \exp(-\eta c_{ij}) \exp(\eta v_j)$. The exponential dual multipliers $(\exp(\eta u_i), \exp(\eta v_j))$ can then be computed in $\mathcal{O}(mn)$ parallel matrix-vector multiplications via Richard Sinkhorn's iterative row-and-column proportional scaling algorithm (also known in contingency-table statistics as Deming–Stephan Iterative Proportional Fitting), converging smoothly to the classical unregularized Hitchcock–Koopmans vertex solution as the inverse temperature parameter $\eta \to +\infty$.

## Worked Questions and Solutions

### Question 1: Comparative Initial Basic Feasible Solutions: Northwest Corner, Least-Cost, and Vogel's Approximation Method (VAM)

A regional biobank distributes cryo-preserved blood plasma units from $m = 3$ central processing centers ($O_1, O_2, O_3$) with supplies $a_1 = 30, a_2 = 50, a_3 = 20$ to $n = 4$ metropolitan hospital networks ($D_1, D_2, D_3, D_4$) with demands $b_1 = 20, b_2 = 40, b_3 = 30, b_4 = 10$. The unit shipping costs $c_{ij}$ (in $\$10^2$ per batch) are given in the table below:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Origin \ Destination</th><th>$D_1$</th><th>$D_2$</th><th>$D_3$</th><th>$D_4$</th><th>Supply ($a_i$)</th></tr></thead><tbody><tr><td>$O_1$</td><td>$2$</td><td>$3$</td><td>$11$</td><td>$7$</td><td>$30$</td></tr><tr><td>$O_2$</td><td>$1$</td><td>$0$</td><td>$6$</td><td>$1$</td><td>$50$</td></tr><tr><td>$O_3$</td><td>$5$</td><td>$8$</td><td>$15$</td><td>$9$</td><td>$20$</td></tr><tr><td><strong>Demand ($b_j$)</strong></td><td>$20$</td><td>$40$</td><td>$30$</td><td>$10$</td><td><strong>Total $= 100$</strong></td></tr></tbody></table></div>

1. Verify that the system is balanced and determine the exact number of basic variables required in any Basic Feasible Solution.
2. Compute the initial Basic Feasible Solution and total shipping cost $W_{\text{NWC}}$ using the **Northwest Corner Rule**.
3. Compute the initial Basic Feasible Solution and total shipping cost $W_{\text{VAM}}$ using **Vogel's Approximation Method (VAM)**, and compare the cost savings achieved by VAM over the Northwest Corner Rule.

### Solution, step 1: Check system balance and compute Northwest Corner BFS

Total supply is $\sum_{i=1}^3 a_i = 30 + 50 + 20 = 100$ and total demand is $\sum_{j=1}^4 b_j = 20 + 40 + 30 + 10 = 100$. Because $\sum a_i = \sum b_j = 100$, the transportation problem is balanced, and every Basic Feasible Solution requires $m + n - 1 = 3 + 4 - 1 = 6$ basic variables.

**Northwest Corner Rule Execution**:
1. Cell $(1,1)$: $x_{11} = \min(30, 20) = 20$ ($D_1$ satisfied; $a_1$ becomes $10$). Move right to $(1,2)$.
2. Cell $(1,2)$: $x_{12} = \min(10, 40) = 10$ ($O_1$ exhausted; $b_2$ becomes $30$). Move down to $(2,2)$.
3. Cell $(2,2)$: $x_{22} = \min(50, 30) = 30$ ($D_2$ satisfied; $a_2$ becomes $20$). Move right to $(2,3)$.
4. Cell $(2,3)$: $x_{23} = \min(20, 30) = 20$ ($O_2$ exhausted; $b_3$ becomes $10$). Move down to $(3,3)$.
5. Cell $(3,3)$: $x_{33} = \min(20, 10) = 10$ ($D_3$ satisfied; $a_3$ becomes $10$). Move right to $(3,4)$.
6. Cell $(3,4)$: $x_{34} = \min(10, 10) = 10$ ($O_3$ and $D_4$ satisfied).

Total cost under the Northwest Corner Rule is:

$$W_{\text{NWC}} = 2(20) + 3(10) + 0(30) + 6(20) + 15(10) + 9(10) = 40 + 30 + 0 + 120 + 150 + 90 = 430$$

### Solution, step 2: Execute Vogel's Approximation Method (VAM)

We compute the row and column opportunity-cost penalties (second-smallest cost minus smallest cost) at each stage:
- **Iteration 1**: Row penalties: $P_{O_1} = 3 - 2 = 1$, $P_{O_2} = 1 - 0 = 1$, $P_{O_3} = 8 - 5 = 3$. Column penalties: $P_{D_1} = 2 - 1 = 1$, $P_{D_2} = 3 - 0 = 3$, $P_{D_3} = 11 - 6 = 5$ (Max!), $P_{D_4} = 7 - 1 = 6$ (Overall Max = $6$ in Column $D_4$).
  In Column $D_4$, the minimum cost cell is $(2, 4)$ with $c_{24} = 1$. Allocate **$x_{24} = \min(50, 10) = 10$** ($D_4$ satisfied and crossed out; $a_2$ becomes $40$).
- **Iteration 2** (Cols $D_1, D_2, D_3$ remain): Row penalties: $P_{O_1} = 3 - 2 = 1$, $P_{O_2} = 1 - 0 = 1$, $P_{O_3} = 8 - 5 = 3$. Column penalties: $P_{D_1} = 2 - 1 = 1$, $P_{D_2} = 3 - 0 = 3$, $P_{D_3} = 11 - 6 = 5$ (Max!).
  In Column $D_3$, the minimum cost cell is $(2, 3)$ with $c_{23} = 6$. Allocate **$x_{23} = \min(40, 30) = 30$** ($D_3$ satisfied and crossed out; $a_2$ becomes $10$).
- **Iteration 3** (Cols $D_1, D_2$ remain): Row penalties: $P_{O_1} = 3 - 2 = 1$, $P_{O_2} = 1 - 0 = 1$, $P_{O_3} = 8 - 5 = 3$. Column penalties: $P_{D_1} = 2 - 1 = 1$, $P_{D_2} = 3 - 0 = 3$. Choosing Row $O_3$ (or Col $D_2$):
  In Col $D_2$, minimum cost is $c_{22} = 0$: allocate **$x_{22} = \min(10, 40) = 10$** ($O_2$ exhausted; $b_2$ becomes $30$).
- **Remaining Allocations on Rows $O_1, O_3$ and Cols $D_1, D_2$**: In Row $O_3$ ($c_{31}=5, c_{32}=8$), penalty is $3$: allocate **$x_{31} = \min(20, 20) = 20$** to cell $(3,1)$ ($O_3$ and $D_1$ satisfied simultaneously; assign degenerate basic **$x_{11} = 0$** to connect the tree) and allocate **$x_{12} = 30$** to cell $(1,2)$.

### Solution, step 3: Compare VAM Total Cost against Northwest Corner Cost

Evaluating the total transportation cost of the VAM Basic Feasible Solution $\{x_{11}=0, x_{12}=30, x_{22}=10, x_{23}=30, x_{24}=10, x_{31}=20\}$:

$$W_{\text{VAM}} = 2(0) + 3(30) + 0(10) + 6(30) + 1(10) + 5(20) = 0 + 90 + 0 + 180 + 10 + 100 = 380$$

By avoiding the expensive routes $(3,3)$ ($c_{33}=15$) and $(3,4)$ ($c_{34}=9$), Vogel's Approximation Method immediately reduces the initial shipping cost from $W_{\text{NWC}} = 430$ down to $W_{\text{VAM}} = 380$—an immediate **$11.63\%$ cost reduction** before a single Simplex pivot is even performed!

### Question 2: MODI (u-v) Optimality Verification and Stepping-Stone Loop Pivoting

Consider a $3 \times 3$ balanced Transportation Problem with supplies $a_1 = 20, a_2 = 30, a_3 = 25$ and demands $b_1 = 25, b_2 = 30, b_3 = 20$ (Total $= 75$), cost matrix $\mathbf{C}$, and a proposed Basic Feasible Solution of $m+n-1 = 5$ basic allocations:

$$x_{11} = 20, \quad x_{21} = 5, \quad x_{22} = 25, \quad x_{32} = 5, \quad x_{33} = 20$$

where the unit cost matrix $\mathbf{C} = [c_{ij}]$ is:

$$\mathbf{C} = \begin{pmatrix} 4 & 8 & 8 \\ 16 & 24 & 16 \\ 8 & 16 & 24 \end{pmatrix}$$

1. Calculate the total cost $W_0$ of the initial Basic Feasible Solution and solve for the MODI dual multipliers $(u_1, u_2, u_3)$ and $(v_1, v_2, v_3)$ by setting $u_1 = 0$.
2. Compute the reduced cost $\Delta_{ij} = c_{ij} - u_i - v_j$ for all four non-basic cells and identify the entering cell.
3. Trace the closed Stepping-Stone loop, execute the minimum-ratio pivot to find the improved BFS, and verify by recomputing MODI multipliers that the new solution is globally optimal.

### Solution, step 1: Compute Initial Cost and MODI Dual Multipliers (u_i, v_j)

The initial shipping cost is:

$$W_0 = 4(20) + 16(5) + 24(25) + 16(5) + 24(20) = 80 + 80 + 600 + 80 + 480 = 1320$$

Setting $u_1 = 0$ and enforcing $u_i + v_j = c_{ij}$ across the $5$ basic cells $(1,1), (2,1), (2,2), (3,2), (3,3)$:
1. Basic $(1,1)$: $u_1 + v_1 = c_{11} = 4 \implies 0 + v_1 = 4 \implies v_1 = 4$.
2. Basic $(2,1)$: $u_2 + v_1 = c_{21} = 16 \implies u_2 + 4 = 16 \implies u_2 = 12$.
3. Basic $(2,2)$: $u_2 + v_2 = c_{22} = 24 \implies 12 + v_2 = 24 \implies v_2 = 12$.
4. Basic $(3,2)$: $u_3 + v_2 = c_{32} = 16 \implies u_3 + 12 = 16 \implies u_3 = 4$.
5. Basic $(3,3)$: $u_3 + v_3 = c_{33} = 24 \implies 4 + v_3 = 24 \implies v_3 = 20$.

Thus $\mathbf{u} = (0, 12, 4)^T$ and $\mathbf{v} = (4, 12, 20)^T$.

### Solution, step 2: Price Non-Basic Cells and Trace the Stepping-Stone Loop

Compute $\Delta_{ij} = c_{ij} - u_i - v_j$ for the four unoccupied cells $(1,2), (1,3), (2,3), (3,1)$:
- Cell $(1,2)$: $\Delta_{12} = 8 - (0 + 12) = -4 < 0$
- Cell $(1,3)$: $\Delta_{13} = 8 - (0 + 20) = -12 < 0$
- Cell $(2,3)$: $\Delta_{23} = 16 - (12 + 20) = -16 < 0$ (**Most Negative $\implies$ Enter!**)
- Cell $(3,1)$: $\Delta_{31} = 8 - (4 + 4) = 0$

Cell $(2,3)$ enters the basis with $\Delta_{23} = -16$. Tracing the unique closed Stepping-Stone cycle starting at $(2,3)$ through basic cells $(2,2), (3,2), (3,3)$:

$$\mathcal{L} = (2, 3)^{+\theta} \longrightarrow (2, 2)^{-\theta} \longrightarrow (3, 2)^{+\theta} \longrightarrow (3, 3)^{-\theta} \longrightarrow (2, 3)$$

The donor ($-$) cells are $(2,2)$ ($x_{22} = 25$) and $(3,3)$ ($x_{33} = 20$). The maximum feasible pivot quantity is:

$$\theta^* = \min \{ x_{22}, \, x_{33} \} = \min \{ 25, \, 20 \} = 20 \quad \left(\text{Cell } (3,3) \text{ leaves the basis}\right)$$

### Solution, step 3: Update Allocations and Verify Global Optimality via MODI

Updating allocations around the loop by $\theta^* = 20$ gives the new BFS:
- $x_{11} = 20$, $x_{21} = 5$, $x_{22} = 25 - 20 = 5$, $x_{23} = 0 + 20 = 20$, $x_{32} = 5 + 20 = 25$ (with $x_{33} = 0$ non-basic).
- New Total Cost: $W_1 = W_0 + \theta^* \Delta_{23} = 1320 + 20(-16) = 1320 - 320 = 1000$.

Recomputing MODI multipliers for the new basis $B_1 = \{(1,1), (2,1), (2,2), (2,3), (3,2)\}$ with $u_1 = 0$:
- $(1,1) \implies v_1 = 4$; $(2,1) \implies u_2 = 12$; $(2,2) \implies v_2 = 12$; $(2,3) \implies v_3 = 16 - 12 = 4$; $(3,2) \implies u_3 = 16 - 12 = 4$.
Now check $\Delta_{ij} = c_{ij} - u_i - v_j$ for all four non-basic cells:
- $\Delta_{12} = 8 - (0 + 12) = -4 < 0$ (Still negative! Pivot $(1,2)$ in!).
- $\Delta_{13} = 8 - (0 + 4) = +4 \ge 0$; $\Delta_{31} = 8 - (4 + 4) = 0 \ge 0$; $\Delta_{33} = 24 - (4 + 4) = +16 \ge 0$.

Pivoting cell $(1,2)$ ($\Delta_{12} = -4$) into the basis along loop $(1,2)^{+\theta} \to (1,1)^{-\theta} \to (2,1)^{+\theta} \to (2,2)^{-\theta}$ with $\theta^* = \min\{x_{11}=20, x_{22}=5\} = 5$ (so $(2,2)$ leaves) yields:
- **$x_{11}^* = 15, \; x_{12}^* = 5, \; x_{21}^* = 10, \; x_{23}^* = 20, \; x_{32}^* = 25$**, reducing cost to **$W^* = 1000 + 5(-4) = 980$**.
- Updated multipliers ($u_1 = 0$): $v_1 = 4, v_2 = 8, u_2 = 12, v_3 = 4, u_3 = 8$. Non-basic reduced costs: $\Delta_{13} = 8 - 4 = 4 \ge 0$, $\Delta_{22} = 24 - 20 = 4 \ge 0$, $\Delta_{31} = 8 - 12 = -4$... wait: let us check $\Delta_{31} = 8 - (8 + 4) = -4 < 0$! Pivoting $(3,1)$ along $(3,1)^{+\theta} \to (2,1)^{-\theta} \to (2,3)^{+\theta}$? No, $(3,1)^{+\theta} \to (1,1)^{-\theta} \to (1,2)^{+\theta} \to (3,2)^{-\theta}$ has $\Delta = 8 - 4 + 8 - 16 = -4$ with $\theta^* = \min\{x_{11}=15, x_{32}=25\} = 15$, yielding $x_{12}^*=20, x_{21}^*=10, x_{23}^*=20, x_{31}^*=15, x_{32}^*=10$ and **$W^* = 980 + 15(-4) = 920$**, where $u = (0, 8, 8)^T, v = (0, 8, 8)^T$ gives $\Delta_{11}=4 \ge 0, \Delta_{13}=0 \ge 0, \Delta_{22}=8 \ge 0, \Delta_{33}=8 \ge 0$, proving global optimality at **$W^* = 920$**!

### Question 3: Complete Execution of Kuhn's Hungarian Algorithm on a 4x4 Assignment Problem

Four statistical analysts ($A_1, A_2, A_3, A_4$) are to be assigned on a one-to-one basis to four specialized data-auditing tasks ($T_1, T_2, T_3, T_4$). The processing costs $c_{ij}$ (in hours) are given by the $4 \times 4$ matrix:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Analyst \ Task</th><th>$T_1$</th><th>$T_2$</th><th>$T_3$</th><th>$T_4$</th></tr></thead><tbody><tr><td>$A_1$</td><td>$10$</td><td>$19$</td><td>$8$</td><td>$15$</td></tr><tr><td>$A_2$</td><td>$10$</td><td>$18$</td><td>$7$</td><td>$17$</td></tr><tr><td>$A_3$</td><td>$13$</td><td>$16$</td><td>$9$</td><td>$14$</td></tr><tr><td>$A_4$</td><td>$12$</td><td>$19$</td><td>$8$</td><td>$18$</td></tr></tbody></table></div>

1. Perform Step 1 (Row Reduction) and Step 2 (Column Reduction) of the Hungarian Algorithm and display the reduced matrix.
2. Apply the König–Egerváry Minimum Line Covering Test to show that fewer than $n = 4$ lines cover all zeros, and execute Step 4 (Dual Potential Shift by $\delta$) to generate new zeros.
3. Determine the optimal one-to-one assignment $(x_{ij}^*)$ and verify that the minimum total cost $W^*$ equals the sum of all row reductions, column reductions, and dual shifts.

### Solution, step 1: Step 1 (Row Reduction) and Step 2 (Column Reduction)

**Row Reduction**: The row minimums are $u_1 = 8, u_2 = 7, u_3 = 9, u_4 = 8$. Subtracting $u_i$ from each row $i$ gives $\mathbf{C}^{(1)}$:

$$\mathbf{C}^{(1)} = \begin{pmatrix} 2 & 11 & 0 & 7 \\ 3 & 11 & 0 & 10 \\ 4 & 7 & 0 & 5 \\ 4 & 11 & 0 & 10 \end{pmatrix}$$

**Column Reduction**: The column minimums of $\mathbf{C}^{(1)}$ are $v_1 = 2, v_2 = 7, v_3 = 0, v_4 = 5$. Subtracting $v_j$ from each column $j$ gives $\mathbf{C}^{(2)}$:

$$\mathbf{C}^{(2)} = \begin{pmatrix} 0 & 4 & 0 & 2 \\ 1 & 4 & 0 & 5 \\ 2 & 0 & 0 & 0 \\ 2 & 4 & 0 & 5 \end{pmatrix}$$

### Solution, step 2: Step 3 (Line Covering) and Step 4 (Dual Potential Shift)

Inspecting $\mathbf{C}^{(2)}$: Row 1 has a zero in Col 1 ($\boxed{0}$ at $(1,1)$), Row 2 has its only zero at $(2,3)$ ($\boxed{0}$ at $(2,3)$, crossing out zeros at $(1,3),(3,3),(4,3)$), Row 3 has a zero at $(3,2)$ or $(3,4)$ ($\boxed{0}$ at $(3,2)$), leaving Row 4 with **no unassigned zero**!
Covering all zeros with the minimum number of lines requires $L = 3 < 4$ lines:
- Horizontal line through **Row 1**, Horizontal line through **Row 3**, and Vertical line through **Column 3**.

The uncovered cells sit in Rows 2 and 4 across Columns 1, 2, and 4: $\{1, 4, 5, 2, 4, 5\}$. The **smallest uncovered element** is $\delta = 1$ (at cell $(2,1)$).
Subtracting $\delta = 1$ from all uncovered elements and adding $\delta = 1$ to the doubly covered intersections $(1,3)$ and $(3,3)$ yields $\mathbf{C}^{(3)}$:

$$\mathbf{C}^{(3)} = \begin{pmatrix} 0 & 4 & 1 & 2 \\ 0 & 3 & 0 & 4 \\ 2 & 0 & 1 & 0 \\ 1 & 3 & 0 & 4 \end{pmatrix}$$

### Solution, step 3: Extract Optimal Assignment and Verify Total Cost

In $\mathbf{C}^{(3)}$, we now have $L = 4$ independent zeros—one in each row and column:
- Row 4 has a unique zero at **$(4, 3)$** $\implies$ Assign **$A_4 \to T_3$** ($x_{43}^* = 1$, cross out $(2,3)$).
- Row 2 now has a unique zero at **$(2, 1)$** $\implies$ Assign **$A_2 \to T_1$** ($x_{21}^* = 1$, cross out $(1,1)$... wait: if $(1,1)$ is crossed out, Row 1 has no zero!).
Let us check $L$ on $\mathbf{C}^{(3)}$: the zeros of $\mathbf{C}^{(3)}$ in Rows 1, 2, 4 all lie solely in Columns 1 and 3! Thus $L = 3$ lines (Vertical Col 1, Vertical Col 3, Horizontal Row 3) cover all zeros of $\mathbf{C}^{(3)}$!
Applying one more Dual Shift on $\mathbf{C}^{(3)}$: the uncovered cells are in Rows 1, 2, 4 and Columns 2, 4: $\{4, 2, 3, 4, 3, 4\}$, with minimum **$\delta_2 = 2$** (at cell $(1,4)$). Subtracting $2$ from uncovered cells and adding $2$ to doubly covered cells $(3,1), (3,3)$ gives $\mathbf{C}^{(4)}$:

$$\mathbf{C}^{(4)} = \begin{pmatrix} 0 & 2 & 1 & \mathbf{0} \\ \mathbf{0} & 1 & 0 & 2 \\ 4 & \mathbf{0} & 3 & 0 \\ 1 & 1 & \mathbf{0} & 2 \end{pmatrix}$$

Now $L = 4$ independent zeros exist!
- **$A_1 \to T_4$** ($c_{14} = 15$)
- **$A_2 \to T_1$** ($c_{21} = 10$)
- **$A_3 \to T_2$** ($c_{32} = 16$)
- **$A_4 \to T_3$** ($c_{43} = 8$)

The minimum total assignment cost is:

$$W^* = 15 + 10 + 16 + 8 = 49\text{ hours}$$

(And notice that an alternative optimal assignment is $A_1 \to T_1 (10), A_2 \to T_3 (7), A_3 \to T_4 (14), A_4 \to T_3$—wait: $A_2 \to T_1 (10), A_4 \to T_3 (8), A_1 \to T_4 (15), A_3 \to T_2 (16)$ is the unique zero-assignment on $\mathbf{C}^{(4)}$, with dual bound $\sum u_i + \sum v_j + (4-3)\delta_1 + (4-3)\delta_2 = (8+7+9+8) + (2+7+0+5) + 1 + 2 = 32 + 14 + 3 = 49$, confirming $W^* = 49$ with exact equality!).
