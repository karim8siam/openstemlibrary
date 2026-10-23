# Unit 1: Foundations of Operations Research, Linear Programming Formulations & Convex Polyhedral Geometry

## 1.1 Historical Evolution, Systems Methodology, and Statistical Decision Frameworks in Operations Research

Operations Research (OR), known equivalently as operational research in British scientific nomenclature and management science in industrial analytics, is the mathematical discipline dedicated to determining optimal or near-optimal resource allocation decisions within complex, constrained systems. While isolated precursors of mathematical optimization appeared in the eighteenth and nineteenth centuries—most notably Gaspard Monge's 1781 geometric treatise on earth-moving (the precursor to optimal transport theory), Jean-Baptiste Joseph Fourier's 1826 investigation of linear inequalities, Charles Babbage's 1832 quantitative study of postal sorting and factory workflows, and Leon Walras's 1874 general equilibrium equations—the formal birth of Operations Research occurred during the late 1930s and World War II. British military planners assembled interdisciplinary scientific directorates, notably Patrick Blackett's "Circus" and Bawdsey Research Station teams, to analyze Chain Home radar network deployment, anti-aircraft fire control, antisubmarine depth-charge detonation depths, and North Atlantic merchant convoy sizing. Concurrently in the Soviet Union, Leonid Vitaliyevich Kantorovich published his seminal 1939 monograph on the mathematical organization and planning of industrial production, introducing dual shadow valuations ("resolving multipliers") for scarce factory capacities, a discovery for which he later shared the 1975 Nobel Memorial Prize in Economic Sciences with Tjalling Koopmans. Following the war, George Bernard Dantzig, working as mathematical advisor to the United States Air Force Comptroller under Project SCOOP (Scientific Computation of Optimal Programs) in 1947, formulated the general Linear Programming Problem and invented the Simplex Algorithm, igniting a computational revolution that linked linear algebra, convex geometry, and statistical decision theory.

From the perspective of mathematical statistics and Course Stat H-205, Operations Research is not merely a collection of deterministic engineering heuristics; rather, it forms the normative prescription layer of statistical decision theory. Whereas inferential statistics focuses on estimating unknown population parameters $\boldsymbol{\theta} \in \Theta$ from noisy empirical samples $\mathbf{X} = (X_1, \dots, X_n)^T$ and testing structural hypotheses, Operations Research takes estimated technological coefficients, cost parameters, and probability laws and asks how a decision-maker should choose an action vector $\mathbf{x} \in \mathcal{F} \subseteq \mathbb{R}^n$ to optimize a well-defined objective functional. In Abraham Wald's decision-theoretic synthesis, both statistical inference and operational optimization share the identical mathematical foundation: minimizing expected loss or maximizing expected utility over a constrained feasible action space. Furthermore, modern statistical estimation problems—including least-absolute-deviations ($L_1$) median regression, quantile regression (Koenker and Bassett, 1978), Chebyshev ($L_\infty$) minimax approximation, optimal experimental design, and Chebyshev-type probability bounds—can be cast directly as linear programming problems.

The methodological architecture of an Operations Research investigation proceeds through six rigorous, interconnected analytical stages:

1. **System Boundary Definition and Problem Formulation**: The analyst delineates the operational system under investigation, separating controllable endogenous decision variables $x_1, x_2, \dots, x_n$ from exogenous environmental parameters, technological consumption rates $a_{ij}$, resource capacities $b_i$, and economic valuations $c_j$. Conflicting institutional objectives—such as maximizing manufacturing throughput while minimizing defect variance, carbon emissions, or capital expenditure—are reconciled into a primary scalar objective function or converted into explicit aspiration constraints.
2. **Mathematical and Statistical Model Construction**: The physical, economic, or logistical relationships governing the system are abstracted into a formal system of algebraic equations, inequalities, or stochastic balance laws. In a statistical environment, the model parameters $(\mathbf{A}, \mathbf{b}, \mathbf{c})$ are rarely known constants given by oracle; they are point estimates $(\hat{\mathbf{A}}, \hat{\mathbf{b}}, \hat{\mathbf{c}})$ obtained via ordinary or generalized least squares regression, time-series forecasting, design of experiments, or survival analysis.
3. **Analytical and Algorithmic Solution**: Deductive mathematical machinery—such as the Simplex algorithm, interior-point barrier methods, network flow algorithms, dynamic programming recursions, or Markovian birth-death equations—is applied to identify an optimal solution vector $\mathbf{x}^* \in \mathcal{F}$ that satisfies all structural constraints while achieving the supremum or infimum of the objective criterion.
4. **Post-Optimality Sensitivity and Robustness Analysis**: Because input parameters are subject to sampling variance and measurement error, an optimal solution $\mathbf{x}^*$ is incomplete without characterizing its stability region. Sensitivity analysis determines the precise intervals over which cost coefficients $c_j$ and right-hand-side capacities $b_i$ may fluctuate without invalidating the optimal basis or inducing catastrophic feasibility violations.
5. **Model Validation and Statistical Verification**: Before operational deployment, the mathematical model is tested retrospectively against out-of-sample historical data or evaluated via Monte Carlo discrete-event simulation to verify that structural simplifying assumptions (such as linearity, divisibility, or memoryless exponential interarrival times) do not distort real-world performance metrics.
6. **Implementation, Monitoring, and Adaptive Control**: The optimal decision policy is translated into automated scheduling rules, inventory reorder triggers, or routing protocols, accompanied by statistical quality control charts (such as Shewhart, CUSUM, or EWMA charts) that monitor ongoing system outputs and trigger model recalibration whenever structural regime shifts occur.

## 1.2 Mathematical Formulation of Linear Programming Problems: Canonical, General, and Matrix Architectures

Linear Programming (LP) addresses the optimization of a linear objective functional subject to a finite system of linear equality and linear inequality constraints. Let $\mathbf{x} = (x_1, x_2, \dots, x_n)^T \in \mathbb{R}^n$ denote a column vector of $n$ real-valued decision variables, where each $x_j$ represents the quantitative level of competing economic, industrial, agricultural, or statistical activity $j$. A mathematical optimization problem qualifies as a Linear Programming Problem (LPP) if and only if it satisfies four foundational structural axioms:

1. **Proportionality**: The contribution of each activity $j$ to the objective function, $c_j x_j$, and its consumption of each scarce resource $i$, $a_{ij} x_j$, are strictly proportional to the activity level $x_j$. No startup fixed charges, economies of scale, power-law elasticities, or diminishing marginal returns are permitted within a single linear term. Formally, each term $f_j(x_j)$ is homogeneous of degree one, satisfying $f_j(\alpha x_j) = \alpha f_j(x_j)$ for all $\alpha \in \mathbb{R}$.
2. **Additivity**: The total objective value $Z(\mathbf{x})$ and the total consumption of every resource $i$ equal the exact algebraic sum of the individual contributions across all $n$ activities, precluding cross-product interaction terms $x_j x_k$ or synergistic couplings. Together, proportionality and additivity establish superposition: the objective function $Z(\mathbf{x}) = \mathbf{c}^T\mathbf{x}$ and all constraint left-hand sides $\mathbf{a}_i^T\mathbf{x}$ are linear functionals on the vector space $\mathbb{R}^n$.
3. **Divisibility (Continuity)**: Decision variables $x_j$ are permitted to assume any continuous fractional (real) value within their feasible bounds, rather than being restricted to discrete integer lattices. When divisibility is relaxed in favor of discrete integrality ($x_j \in \mathbb{Z}_+$), the problem transitions into Integer Linear Programming (Unit 6), which exhibits fundamentally different computational complexity.
4. **Certainty (Deterministic Parameters)**: All objective coefficients $c_j$, technological input-output coefficients $a_{ij}$, and resource availability capacities $b_i$ are treated as known, deterministic real numbers during the execution of the optimization algorithm. When uncertainty in $(\mathbf{A}, \mathbf{b}, \mathbf{c})$ is modeled explicitly via probability distributions, the framework extends to stochastic programming and chance-constrained optimization.

Under these four axioms, the **General Linear Programming Problem** is written in algebraic summation form as seeking to maximize (or minimize) the linear functional:

$$\text{Optimize } Z = \sum_{j=1}^n c_j x_j = c_1 x_1 + c_2 x_2 + \dots + c_n x_n$$

subject to $m$ structural linear constraints partitioned into index sets $M_1$ (less-than-or-equal-to inequalities), $M_2$ (greater-than-or-equal-to inequalities), and $M_3$ (strict linear equalities):

$$\sum_{j=1}^n a_{ij} x_j \le b_i, \quad i \in M_1$$

$$\sum_{j=1}^n a_{ij} x_j \ge b_i, \quad i \in M_2$$

$$\sum_{j=1}^n a_{ij} x_j = b_i, \quad i \in M_3$$

and variable sign restrictions partitioned across $N_1$ (non-negative variables), $N_2$ (non-positive variables), and $N_3$ (unrestricted or free variables):

$$x_j \ge 0 \quad (j \in N_1), \qquad x_j \le 0 \quad (j \in N_2), \qquad x_j \in \mathbb{R} \text{ unrestricted} \quad (j \in N_3)$$

### Canonical Form and Archetypal Statistical Formulations

For theoretical analysis and duality pairings (Unit 3), it is exceptionally convenient to express a linear program in **Symmetric Canonical Form**. A maximization linear program is in canonical form when all structural constraints are less-than-or-equal-to inequalities ($\le$) and all decision variables are restricted to be non-negative:

$$\text{Maximize } Z = \mathbf{c}^T \mathbf{x} \quad \text{subject to} \quad \mathbf{A}\mathbf{x} \le \mathbf{b}, \quad \mathbf{x} \ge \mathbf{0}$$

Conversely, a minimization linear program is in symmetric canonical form when all structural constraints are greater-than-or-equal-to inequalities ($\ge$) and all variables are non-negative:

$$\text{Minimize } W = \mathbf{c}^T \mathbf{x} \quad \text{subject to} \quad \mathbf{A}\mathbf{x} \ge \mathbf{b}, \quad \mathbf{x} \ge \mathbf{0}$$

Here $\mathbf{c} = (c_1, \dots, c_n)^T \in \mathbb{R}^n$ is the cost or profit gradient vector, $\mathbf{b} = (b_1, \dots, b_m)^T \in \mathbb{R}^m$ is the right-hand-side resource requirement vector, and $\mathbf{A} = [a_{ij}] \in \mathbb{R}^{m \times n}$ is the $m \times n$ technological matrix whose columns $\mathbf{a}_j \in \mathbb{R}^m$ represent the activity consumption vectors of the $n$ structural decision variables. Classic real-world and statistical archetypes include the **Stigler Diet Problem** (minimizing feed or nutritional cost $\mathbf{c}^T\mathbf{x}$ subject to minimum daily nutrient intake inequalities $\mathbf{A}\mathbf{x} \ge \mathbf{b}$), the **Product Mix and Portfolio Allocation Problem** (maximizing net return subject to departmental machine-hour, labor, and risk budget bounds $\mathbf{A}\mathbf{x} \le \mathbf{b}$), and **Robust $L_1$ Linear Regression** (minimizing the sum of absolute residuals $\sum_{i=1}^m |y_i - \mathbf{z}_i^T\boldsymbol{\beta}|$ by introducing non-negative positive and negative residual deviations $u_i, v_i \ge 0$ such that $\mathbf{z}_i^T\boldsymbol{\beta} + u_i - v_i = y_i$).

## 1.3 Slack, Surplus, and Unrestricted Variables: Transformations into Standard Equality Form

While the canonical form is ideal for geometric visualization and duality theorems, computational linear algebra algorithms—specifically the Simplex method and interior-point solvers—require solving systems of linear equations rather than inequalities. Consequently, every general linear programming problem must be systematically transformed into **Standard Form** (also termed computational equality form), in which the objective is maximized (or minimized), every structural constraint is a strict linear equation with a non-negative right-hand side ($b_i \ge 0$), and every decision variable satisfies non-negativity ($x_j \ge 0$).

$$\text{Maximize } Z = \mathbf{c}^T \mathbf{x} \quad \text{subject to} \quad \mathbf{A}\mathbf{x} = \mathbf{b} \quad (\mathbf{b} \ge \mathbf{0}), \quad \mathbf{x} \ge \mathbf{0}$$

Every conceivable departure from Standard Form can be eliminated through five exact equivalence transformations that preserve the optimal solution set and objective value:

1. **Objective Sense Conversion**: Because the supremum of a real-valued functional is the negative of the infimum of its negation, minimizing a linear function $W = \mathbf{c}^T \mathbf{x}$ is mathematically identical to maximizing $Z = -W = (-\mathbf{c})^T \mathbf{x}$:
   $$\min_{\mathbf{x} \in \mathcal{F}} \mathbf{c}^T \mathbf{x} = - \max_{\mathbf{x} \in \mathcal{F}} (-\mathbf{c}^T \mathbf{x})$$
   After computing the maximizer $\mathbf{x}^*$, the minimum objective value is recovered by reversing the sign of the maximum objective value, $W^* = -Z^*$.
2. **Elimination of Less-Than-or-Equal-To ($\le$) Inequalities via Slack Variables**: Suppose constraint $i$ takes the form $\sum_{j=1}^n a_{ij} x_j \le b_i$, representing an upper bound on resource consumption. We introduce a non-negative **slack variable** $s_i \ge 0$ defined as the unused or idle quantity of resource $i$:
   $$s_i = b_i - \sum_{j=1}^n a_{ij} x_j \ge 0 \iff \sum_{j=1}^n a_{ij} x_j + s_i = b_i, \quad s_i \ge 0$$
   Because unused capacity generates neither direct profit nor direct penalty in the base model, $s_i$ is assigned a zero objective coefficient ($c_{s_i} = 0$). When $s_i = 0$ at a feasible point $\mathbf{x}$, constraint $i$ is said to be **binding** (active or tight); when $s_i > 0$, constraint $i$ is **non-binding** (inactive or slack).
3. **Elimination of Greater-Than-or-Equal-To ($\ge$) Inequalities via Surplus Variables**: Suppose constraint $i$ takes the form $\sum_{j=1}^n a_{ij} x_j \ge b_i$, representing a minimum performance threshold or dietary requirement. We subtract a non-negative **surplus variable** (or excess variable) $e_i \ge 0$, which measures the amount by which the left-hand side exceeds the minimum requirement $b_i$:
   $$e_i = \sum_{j=1}^n a_{ij} x_j - b_i \ge 0 \iff \sum_{j=1}^n a_{ij} x_j - e_i = b_i, \quad e_i \ge 0$$
   Like slack variables, surplus variables carry a zero coefficient ($c_{e_i} = 0$) in the objective function. Notice carefully that setting structural variables to zero ($\mathbf{x} = \mathbf{0}$) in $\sum a_{ij}x_j - e_i = b_i$ with $b_i > 0$ yields $e_i = -b_i < 0$, which violates non-negativity; this algebraic asymmetry is precisely why $\ge$ and $=$ constraints require artificial variables in Phase I of the Simplex method (Unit 2).
4. **Non-Negativity of Right-Hand-Side Constants**: If any equality constraint $\sum_{j=1}^n a_{ij} x_j = b_i$ possesses a strictly negative right-hand side ($b_i < 0$), multiplying the entire equation by $-1$ yields $\sum_{j=1}^n (-a_{ij}) x_j = -b_i > 0$. If this negation is performed prior to introducing slack or surplus variables, multiplying an inequality by $-1$ reverses the direction of the inequality sign ($\le$ becomes $\ge$, and vice versa).
5. **Transformation of Non-Positive, Bounded-Interval, and Unrestricted (Free) Variables**:
   - If a variable is constrained to be non-positive ($x_j \le 0$), we substitute $x_j = -x_j'$ where $x_j' \ge 0$, negating its column $\mathbf{a}_j$ in $\mathbf{A}$ and its cost $c_j$ in $\mathbf{c}$.
   - If a variable has a non-zero lower bound $x_j \ge l_j$, we apply the affine shift $x_j = l_j + x_j'$ with $x_j' \ge 0$, adjusting the right-hand side to $b_i' = b_i - a_{ij}l_j$.
   - If a variable $x_j \in \mathbb{R}$ is **unrestricted in sign** (as frequently occurs for net financial balances, temperature deviations, or regression parameters $\beta_j$), we leverage the algebraic fact that any real number can be expressed as the difference of two non-negative real numbers:
     $$x_j = x_j^+ - x_j^-, \qquad x_j^+ \ge 0, \quad x_j^- \ge 0$$
     Substituting $x_j^+ - x_j^-$ for $x_j$ throughout the objective and constraints replaces column $\mathbf{a}_j$ with two linearly dependent columns $+\mathbf{a}_j$ and $-\mathbf{a}_j$. Because $\mathbf{a}_j$ and $-\mathbf{a}_j$ are collinear ($\mathbf{a}_j + (-\mathbf{a}_j) = \mathbf{0}$), no basic feasible solution can ever contain both $x_j^+ > 0$ and $x_j^- > 0$ simultaneously in a valid basis! Consequently, at any basic solution, at least one of $x_j^+$ or $x_j^-$ equals zero, ensuring a unique one-to-one mapping $x_j^+ = \max(0, x_j)$ and $x_j^- = \max(0, -x_j)$. If $k$ unrestricted variables $x_1, \dots, x_k$ are present, one may even more compactly replace all $k$ variables with $k+1$ non-negative variables by setting $x_j = x_j' - w$ for $j=1,\dots,k$, where $w = \max(0, -x_1, \dots, -x_k) \ge 0$ is a single shared shift variable.

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Original Structural Element</th><th>Mathematical Expression</th><th>Standard Form Transformation</th><th>Added Variables &amp; Objective Cost</th></tr></thead><tbody><tr><td>Minimization Objective</td><td>$\min W = \mathbf{c}^T\mathbf{x}$</td><td>$\max Z = (-\mathbf{c})^T\mathbf{x}$</td><td>None ($W^* = -Z^*$)</td></tr><tr><td>Resource Upper Bound ($\le$)</td><td>$\mathbf{a}_i^T\mathbf{x} \le b_i$</td><td>$\mathbf{a}_i^T\mathbf{x} + s_i = b_i$</td><td>Slack $s_i \ge 0$, cost $0$</td></tr><tr><td>Requirement Lower Bound ($\ge$)</td><td>$\mathbf{a}_i^T\mathbf{x} \ge b_i$</td><td>$\mathbf{a}_i^T\mathbf{x} - e_i = b_i$</td><td>Surplus $e_i \ge 0$, cost $0$</td></tr><tr><td>Unrestricted Variable</td><td>$x_j \in (-\infty, +\infty)$</td><td>$x_j = x_j^+ - x_j^-$</td><td>$x_j^+ \ge 0, x_j^- \ge 0$, costs $+c_j, -c_j$</td></tr><tr><td>Bounded Interval Variable</td><td>$l_j \le x_j \le u_j$</td><td>$x_j = l_j + x_j'$, $x_j' + s_j' = u_j - l_j$</td><td>Shifted $x_j' \ge 0$, upper slack $s_j' \ge 0$</td></tr><tr><td>Absolute Value Term in Min</td><td>$\min \sum c_j |x_j|$</td><td>$x_j = x_j^+ - x_j^-, |x_j| = x_j^+ + x_j^-$</td><td>$x_j^+, x_j^- \ge 0$ when $c_j > 0$</td></tr></tbody></table></div>

## 1.4 Convex Sets, Hyperplanes, Half-Spaces, Convex Hulls, and Polyhedral Geometry

The remarkable computational tractability of Linear Programming—wherein a local optimum over a continuous multidimensional domain is guaranteed to be a global optimum, and the search over uncountably infinite feasible points reduces to checking a finite set of corners—rests entirely on the geometry of **convex polyhedra** in Euclidean space $\mathbb{R}^n$.

### Hyperplanes and Closed Half-Spaces

A **hyperplane** $H \subseteq \mathbb{R}^n$ is an $(n-1)$-dimensional affine subspace defined by a non-zero normal vector $\mathbf{a} = (a_1, \dots, a_n)^T \in \mathbb{R}^n \setminus \{\mathbf{0}\}$ and a scalar constant $b \in \mathbb{R}$:

$$H(\mathbf{a}, b) = \left\{ \mathbf{x} \in \mathbb{R}^n : \mathbf{a}^T \mathbf{x} = \sum_{j=1}^n a_j x_j = b \right\}$$

Geometrically, the normal vector $\mathbf{a}$ is orthogonal to every displacement vector $\mathbf{x}_1 - \mathbf{x}_2$ lying within $H$, because $\mathbf{a}^T(\mathbf{x}_1 - \mathbf{x}_2) = b - b = 0$, and $\mathbf{a}$ points in the direction of steepest ascent of the linear function $f(\mathbf{x}) = \mathbf{a}^T\mathbf{x}$. Every hyperplane $H(\mathbf{a}, b)$ divides $\mathbb{R}^n$ into two **closed half-spaces**:

$$H^-(\mathbf{a}, b) = \left\{ \mathbf{x} \in \mathbb{R}^n : \mathbf{a}^T \mathbf{x} \le b \right\}, \qquad H^+(\mathbf{a}, b) = \left\{ \mathbf{x} \in \mathbb{R}^n : \mathbf{a}^T \mathbf{x} \ge b \right\}$$

whose intersection $H^-(\mathbf{a}, b) \cap H^+(\mathbf{a}, b) = H(\mathbf{a}, b)$ is the boundary hyperplane itself.

### Convex Sets, Carathéodory's Theorem, and Separating Hyperplanes

A subset $S \subseteq \mathbb{R}^n$ is defined to be a **convex set** if, for every pair of points $\mathbf{x}^{(1)}, \mathbf{x}^{(2)} \in S$, the entire closed line segment connecting $\mathbf{x}^{(1)}$ and $\mathbf{x}^{(2)}$ is contained completely within $S$. Algebraically, $S$ is convex if and only if for all $\mathbf{x}^{(1)}, \mathbf{x}^{(2)} \in S$ and every scalar weight $\lambda \in [0, 1]$:

$$\mathbf{x}(\lambda) = \lambda \mathbf{x}^{(1)} + (1 - \lambda) \mathbf{x}^{(2)} \in S \quad \forall \lambda \in [0, 1]$$

The point $\lambda \mathbf{x}^{(1)} + (1 - \lambda) \mathbf{x}^{(2)}$ is called a **convex combination** of $\mathbf{x}^{(1)}$ and $\mathbf{x}^{(2)}$; when $0 < \lambda < 1$, it is a **strict convex combination**. More generally, given $k$ points $\mathbf{x}^{(1)}, \dots, \mathbf{x}^{(k)} \in \mathbb{R}^n$, any vector of the form $\sum_{i=1}^k \lambda_i \mathbf{x}^{(i)}$ with $\lambda_i \ge 0$ and $\sum_{i=1}^k \lambda_i = 1$ is a convex combination. The **convex hull** of an arbitrary set $X \subseteq \mathbb{R}^n$, denoted $\text{conv}(X)$, is the intersection of all convex sets containing $X$, which equals the set of all finite convex combinations of elements of $X$. By **Carathéodory's Theorem**, if $X \subseteq \mathbb{R}^n$, every point $\mathbf{x} \in \text{conv}(X)$ can be expressed as a convex combination of at most $n + 1$ affinely independent points in $X$. Furthermore, the **Supporting and Separating Hyperplane Theorem** guarantees that if $S \subseteq \mathbb{R}^n$ is a non-empty closed convex set and $\mathbf{y} \notin S$, there exists a hyperplane $H(\mathbf{p}, \alpha)$ strictly separating $\mathbf{y}$ from $S$ such that $\mathbf{p}^T\mathbf{x} \le \alpha < \mathbf{p}^T\mathbf{y}$ for all $\mathbf{x} \in S$.

#### Theorem 1.1 (Convexity of Half-Spaces and Polyhedral Intersections):
1. Every hyperplane $H(\mathbf{a}, b)$ and every closed half-space $H^-(\mathbf{a}, b)$ or $H^+(\mathbf{a}, b)$ in $\mathbb{R}^n$ is a closed convex set.
2. The intersection $S = \bigcap_{i \in I} S_i$ of any arbitrary collection (finite or infinite) of convex sets $S_i \subseteq \mathbb{R}^n$ is a convex set.

#### Formal Proof:
First, let $\mathbf{x}^{(1)}, \mathbf{x}^{(2)} \in H^-(\mathbf{a}, b)$, so $\mathbf{a}^T \mathbf{x}^{(1)} \le b$ and $\mathbf{a}^T \mathbf{x}^{(2)} \le b$. For any $\lambda \in [0, 1]$, since $\lambda \ge 0$ and $1 - \lambda \ge 0$, linearity of the inner product yields:

$$\mathbf{a}^T \left( \lambda \mathbf{x}^{(1)} + (1 - \lambda) \mathbf{x}^{(2)} \right) = \lambda (\mathbf{a}^T \mathbf{x}^{(1)}) + (1 - \lambda) (\mathbf{a}^T \mathbf{x}^{(2)}) \le \lambda b + (1 - \lambda) b = b$$

Thus $\lambda \mathbf{x}^{(1)} + (1 - \lambda) \mathbf{x}^{(2)} \in H^-(\mathbf{a}, b)$, proving that $H^-(\mathbf{a}, b)$ is convex (and identically for $H^+$ and $H$). Second, let $\mathbf{x}^{(1)}, \mathbf{x}^{(2)} \in \bigcap_{i \in I} S_i$, where each $S_i$ is convex. By definition of intersection, $\mathbf{x}^{(1)} \in S_i$ and $\mathbf{x}^{(2)} \in S_i$ for every $i \in I$. Because each $S_i$ is convex, $\lambda \mathbf{x}^{(1)} + (1 - \lambda)\mathbf{x}^{(2)} \in S_i$ for all $\lambda \in [0, 1]$ and all $i \in I$. Therefore, $\lambda \mathbf{x}^{(1)} + (1 - \lambda)\mathbf{x}^{(2)} \in \bigcap_{i \in I} S_i$, establishing that the intersection is convex.

Because the feasible region $\mathcal{F} = \{\mathbf{x} \in \mathbb{R}^n : \mathbf{A}\mathbf{x} = \mathbf{b}, \mathbf{x} \ge \mathbf{0}\}$ of a Linear Programming Problem is the finite intersection of $m$ hyperplanes $\mathbf{a}_i^T \mathbf{x} = b_i$ and $n$ closed half-spaces $x_j \ge 0$, Theorem 1.1 immediately implies that **the feasible region $\mathcal{F}$ of any Linear Programming Problem is a closed convex polyhedron** (and when bounded, a **convex polytope**).

## 1.5 Extreme Points, Basic Feasible Solutions, and Their Algebraic-Geometric Equivalence

Within a convex set $S \subseteq \mathbb{R}^n$, boundary corners play a privileged role. A point $\mathbf{x} \in S$ is defined as an **extreme point** (or **vertex**) of the convex set $S$ if $\mathbf{x}$ cannot be expressed as a strict convex combination of two distinct points in $S$. Formally, $\mathbf{x} \in S$ is an extreme point of $S$ if and only if for all $\mathbf{x}^{(1)}, \mathbf{x}^{(2)} \in S$ and $\lambda \in (0, 1)$:

$$\mathbf{x} = \lambda \mathbf{x}^{(1)} + (1 - \lambda) \mathbf{x}^{(2)} \implies \mathbf{x}^{(1)} = \mathbf{x}^{(2)} = \mathbf{x}$$

Geometrically, an extreme point does not lie in the open interior of any line segment contained in $S$. Two extreme points $\mathbf{v}^{(1)}$ and $\mathbf{v}^{(2)}$ of a polyhedron $\mathcal{F}$ are said to be **adjacent extreme points** if the line segment joining them is a one-dimensional **edge** (a $1$-dimensional face) of $\mathcal{F}$. While extreme points and edges are purely geometric concepts, computational optimization requires an equivalent linear-algebraic characterization.

Consider the standard-form feasible polyhedron $\mathcal{F} = \{\mathbf{x} \in \mathbb{R}^n : \mathbf{A}\mathbf{x} = \mathbf{b}, \mathbf{x} \ge \mathbf{0}\}$, where $\mathbf{A} \in \mathbb{R}^{m \times n}$ has full row rank $\text{rank}(\mathbf{A}) = m \le n$. By permuting the columns of $\mathbf{A}$ if necessary, we can select $m$ linearly independent columns of $\mathbf{A}$ to form an invertible $m \times m$ nonsingular **basis matrix** $\mathbf{B} = [\mathbf{a}_{B(1)}, \dots, \mathbf{a}_{B(m)}] \in \mathbb{R}^{m \times m}$ with $\det(\mathbf{B}) \ne 0$, while the remaining $n - m$ columns form the **non-basic matrix** $\mathbf{N} \in \mathbb{R}^{m \times (n-m)}$. Partitioning the variable vector correspondingly into $\mathbf{x} = (\mathbf{x}_B^T, \mathbf{x}_N^T)^T$, the structural equations $\mathbf{A}\mathbf{x} = \mathbf{b}$ become:

$$\mathbf{B}\mathbf{x}_B + \mathbf{N}\mathbf{x}_N = \mathbf{b}$$

Setting all $n - m$ **non-basic variables** to zero ($\mathbf{x}_N = \mathbf{0}$) and solving uniquely for the $m$ **basic variables** yields a **Basic Solution**:

$$\mathbf{x}_B = \mathbf{B}^{-1} \mathbf{b}, \qquad \mathbf{x}_N = \mathbf{0}$$

Notice that the maximum possible number of basic solutions is bounded above by the combinatorial binomial coefficient $\binom{n}{m} = \frac{n!}{m!(n-m)!}$.
- A basic solution is a **Basic Feasible Solution (BFS)** if all basic variables satisfy non-negativity: $\mathbf{x}_B = \mathbf{B}^{-1}\mathbf{b} \ge \mathbf{0}$.
- A BFS is **non-degenerate** if all $m$ basic variables are strictly positive ($x_{B(i)} > 0$ for all $i=1,\dots,m$), and **degenerate** if at least one basic variable equals zero ($x_{B(i)} = 0$ for some $i$). Geometrically, degeneracy in $\mathbb{R}^n$ occurs when more than $n$ boundary hyperplanes intersect at a single vertex (an overdetermined corner), so that multiple distinct bases $\mathbf{B}_1 \ne \mathbf{B}_2$ represent the exact same geometric extreme point $\mathbf{x}$.

### Theorem 1.2 (Equivalence of Extreme Points and Basic Feasible Solutions):
Let $\mathcal{F} = \{\mathbf{x} \in \mathbb{R}^n : \mathbf{A}\mathbf{x} = \mathbf{b}, \mathbf{x} \ge \mathbf{0}\}$ be non-empty with $\text{rank}(\mathbf{A}) = m \le n$. A vector $\mathbf{x} \in \mathcal{F}$ is an **extreme point** of the convex polyhedron $\mathcal{F}$ if and only if $\mathbf{x}$ is a **Basic Feasible Solution (BFS)** of $\mathbf{A}\mathbf{x} = \mathbf{b}, \mathbf{x} \ge \mathbf{0}$, which occurs if and only if the columns $\{\mathbf{a}_j : x_j > 0\}$ corresponding to the positive components of $\mathbf{x}$ are linearly independent in $\mathbb{R}^m$.

#### Rigorous Proof:
**($\Longleftarrow$ BFS implies Extreme Point)**: Suppose $\mathbf{x} \in \mathcal{F}$ is a BFS, so that the columns $\{\mathbf{a}_j : x_j > 0\}$ are linearly independent (contained within a basis $\mathbf{B}$) and $x_j = 0$ for all non-basic indices $j \in N$. Suppose $\mathbf{x} = \lambda \mathbf{x}^{(1)} + (1-\lambda)\mathbf{x}^{(2)}$ for some $\mathbf{x}^{(1)}, \mathbf{x}^{(2)} \in \mathcal{F}$ and $\lambda \in (0, 1)$. For every non-basic index $j \in N$, we have $0 = x_j = \lambda x_j^{(1)} + (1-\lambda)x_j^{(2)}$. Since $\lambda > 0$, $1-\lambda > 0$, and $x_j^{(1)} \ge 0, x_j^{(2)} \ge 0$, this forces $x_j^{(1)} = x_j^{(2)} = 0$ for all $j \in N$. Consequently, the basic components must satisfy $\mathbf{B}\mathbf{x}_B^{(1)} = \mathbf{b}$ and $\mathbf{B}\mathbf{x}_B^{(2)} = \mathbf{b}$. Since $\mathbf{B}$ is nonsingular, $\mathbf{x}_B^{(1)} = \mathbf{B}^{-1}\mathbf{b} = \mathbf{x}_B^{(2)} = \mathbf{x}_B$. Thus $\mathbf{x}^{(1)} = \mathbf{x}^{(2)} = \mathbf{x}$, proving $\mathbf{x}$ is an extreme point.

**($\implies$ Extreme Point implies BFS)**: Suppose $\mathbf{x} \in \mathcal{F}$ is an extreme point. Without loss of generality, let $x_1, \dots, x_k > 0$ be the strictly positive components of $\mathbf{x}$ and $x_{k+1} = \dots = x_n = 0$. We must prove that the columns $\mathbf{a}_1, \dots, \mathbf{a}_k$ are linearly independent. Suppose to the contrary that they are linearly dependent; then there exists a non-zero vector $\mathbf{d} = (d_1, \dots, d_k, 0, \dots, 0)^T \ne \mathbf{0}$ such that $\sum_{j=1}^k d_j \mathbf{a}_j = \mathbf{A}\mathbf{d} = \mathbf{0}$. Because $x_j > 0$ for $j=1,\dots,k$, we can choose a sufficiently small scalar $\epsilon > 0$ (specifically, $0 < \epsilon < \min_{1 \le j \le k: d_j \ne 0} \frac{x_j}{|d_j|}$) such that $\mathbf{x}^{(1)} = \mathbf{x} + \epsilon \mathbf{d} \ge \mathbf{0}$ and $\mathbf{x}^{(2)} = \mathbf{x} - \epsilon \mathbf{d} \ge \mathbf{0}$. Moreover, $\mathbf{A}\mathbf{x}^{(1)} = \mathbf{A}\mathbf{x} + \epsilon \mathbf{A}\mathbf{d} = \mathbf{b} + \mathbf{0} = \mathbf{b}$, and $\mathbf{A}\mathbf{x}^{(2)} = \mathbf{b}$. Thus $\mathbf{x}^{(1)}, \mathbf{x}^{(2)} \in \mathcal{F}$ are two distinct feasible points ($\mathbf{x}^{(1)} \ne \mathbf{x}^{(2)}$ since $\epsilon \mathbf{d} \ne \mathbf{0}$) whose midpoint is $\mathbf{x} = \frac{1}{2}\mathbf{x}^{(1)} + \frac{1}{2}\mathbf{x}^{(2)}$, contradicting that $\mathbf{x}$ is an extreme point! Hence $\mathbf{a}_1, \dots, \mathbf{a}_k$ are linearly independent ($k \le m$) and can be augmented with $m - k$ additional linearly independent columns from $\mathbf{A}$ (since $\text{rank}(\mathbf{A}) = m$) to form an invertible $m \times m$ basis $\mathbf{B}$, proving $\mathbf{x}$ is a Basic Feasible Solution.

## 1.6 The Fundamental Theorem of Linear Programming and Polyhedral Representation

Theorem 1.2 bridges convex geometry and matrix algebra by identifying the vertices of $\mathcal{F}$ with the Basic Feasible Solutions of $\mathbf{A}\mathbf{x} = \mathbf{b}$. The crowning structural result of Unit 1 is the **Fundamental Theorem of Linear Programming**, which establishes that whenever a linear programming problem admits a finite optimal objective value, that optimum is attained at at least one Basic Feasible Solution (extreme point).

### Polyhedral Representation (Minkowski–Weyl Decomposition)

Consider a non-empty standard-form polyhedron $\mathcal{F} = \{\mathbf{x} \in \mathbb{R}^n : \mathbf{A}\mathbf{x} = \mathbf{b}, \mathbf{x} \ge \mathbf{0}\}$. Because $\mathbf{x} \ge \mathbf{0}$ restricts $\mathcal{F}$ entirely to the non-negative orthant $\mathbb{R}_+^n$, $\mathcal{F}$ is a **pointed polyhedron** (it contains no complete infinite lines $\mathbf{x}_0 + t\mathbf{d}$ for $t \in \mathbb{R}$, because $\mathbf{x}_0 + t\mathbf{d} \ge \mathbf{0}$ for all $t \in \mathbb{R}$ implies $\mathbf{d} = \mathbf{0}$) and therefore possesses at least one extreme point (Basic Feasible Solution). By the **Minkowski–Weyl Representation Theorem**, any point $\mathbf{x} \in \mathcal{F}$ can be decomposed as a convex combination of the finite set of extreme points $\{\mathbf{v}^{(1)}, \dots, \mathbf{v}^{(p)}\}$ of $\mathcal{F}$ plus a non-negative conical combination of the extreme rays $\{\mathbf{r}^{(1)}, \dots, \mathbf{r}^{(q)}\}$ of the recession cone $\mathcal{R} = \{\mathbf{d} \in \mathbb{R}^n : \mathbf{A}\mathbf{d} = \mathbf{0}, \mathbf{d} \ge \mathbf{0}\}$:

$$\mathbf{x} = \sum_{i=1}^p \lambda_i \mathbf{v}^{(i)} + \sum_{k=1}^q \mu_k \mathbf{r}^{(k)}, \qquad \lambda_i \ge 0, \quad \sum_{i=1}^p \lambda_i = 1, \quad \mu_k \ge 0$$

When $\mathcal{F}$ is bounded (a polytope), the recession cone is trivial ($\mathcal{R} = \{\mathbf{0}\}$), so $\mathcal{F}$ is simply the convex hull of its extreme points: $\mathcal{F} = \text{conv}\{\mathbf{v}^{(1)}, \dots, \mathbf{v}^{(p)}\}$, a result also known in functional analysis as the finite-dimensional **Krein–Milman Theorem**.

### Theorem 1.3 (The Fundamental Theorem of Linear Programming):
Given a Linear Programming Problem in standard form: $\max Z = \mathbf{c}^T\mathbf{x}$ subject to $\mathbf{A}\mathbf{x} = \mathbf{b}, \mathbf{x} \ge \mathbf{0}$ with $\text{rank}(\mathbf{A}) = m \le n$:
1. If the feasible polyhedron $\mathcal{F}$ is non-empty, there exists at least one Basic Feasible Solution (extreme point).
2. If the objective function $Z = \mathbf{c}^T\mathbf{x}$ is bounded above on $\mathcal{F}$ (so a finite optimal solution exists), then there exists at least one **optimal Basic Feasible Solution** $\mathbf{v}^* \in \{\mathbf{v}^{(1)}, \dots, \mathbf{v}^{(p)}\}$ that achieves the global maximum $Z^* = \max_{\mathbf{x} \in \mathcal{F}} \mathbf{c}^T\mathbf{x}$.
3. If the global maximum $Z^*$ is achieved at $r \ge 2$ distinct Basic Feasible Solutions $\mathbf{v}^{(1)}, \dots, \mathbf{v}^{(r)}$, then every convex combination $\mathbf{x} = \sum_{i=1}^r \lambda_i \mathbf{v}^{(i)}$ ($\lambda_i \ge 0, \sum \lambda_i = 1$) is also an optimal feasible solution (yielding an infinite family of alternative optima along a face of $\mathcal{F}$).

#### Formal Proof:
First, to prove that $\mathcal{F} \ne \emptyset$ implies the existence of a BFS, pick a feasible vector $\mathbf{x} \in \mathcal{F}$ with the minimum possible number $k$ of strictly positive components $x_1, \dots, x_k > 0$. If the columns $\mathbf{a}_1, \dots, \mathbf{a}_k$ were linearly dependent with $\sum_{j=1}^k d_j \mathbf{a}_j = \mathbf{0}$ ($\mathbf{d} \ne \mathbf{0}$), we could move along $\mathbf{x}(\theta) = \mathbf{x} - \theta \mathbf{d}$ up to the blocking step $\theta^* = \min_{j: d_j > 0} (x_j / d_j) > 0$, producing a new feasible vector $\mathbf{x}(\theta^*) \in \mathcal{F}$ with at most $k - 1$ positive components, contradicting the minimality of $k$! Hence $\mathbf{a}_1, \dots, \mathbf{a}_k$ are linearly independent, and by Theorem 1.2, $\mathbf{x}$ is a BFS.

Second, suppose $\mathcal{F} \ne \emptyset$ and $Z = \mathbf{c}^T\mathbf{x}$ is bounded above on $\mathcal{F}$. For any extreme ray $\mathbf{r}^{(k)}$ of the recession cone, feasibility of $\mathbf{x} + \mu \mathbf{r}^{(k)}$ for arbitrarily large $\mu \to +\infty$ combined with upper boundedness of $\mathbf{c}^T(\mathbf{x} + \mu \mathbf{r}^{(k)}) = \mathbf{c}^T\mathbf{x} + \mu (\mathbf{c}^T\mathbf{r}^{(k)})$ forces $\mathbf{c}^T\mathbf{r}^{(k)} \le 0$ for all $k = 1, \dots, q$. Now let $\mathbf{x} \in \mathcal{F}$ be any arbitrary feasible point. Using the Minkowski–Weyl decomposition and $\mathbf{c}^T\mathbf{r}^{(k)} \le 0$ with $\mu_k \ge 0$:

$$\mathbf{c}^T \mathbf{x} = \sum_{i=1}^p \lambda_i (\mathbf{c}^T \mathbf{v}^{(i)}) + \sum_{k=1}^q \mu_k (\mathbf{c}^T \mathbf{r}^{(k)}) \le \sum_{i=1}^p \lambda_i (\mathbf{c}^T \mathbf{v}^{(i)})$$

Let $\mathbf{v}^* \in \arg\max_{1 \le i \le p} \mathbf{c}^T \mathbf{v}^{(i)}$ be the extreme point with the largest objective value among the finite set of $p$ extreme points. Since $\lambda_i \ge 0$ and $\sum_{i=1}^p \lambda_i = 1$:

$$\mathbf{c}^T \mathbf{x} \le \sum_{i=1}^p \lambda_i (\mathbf{c}^T \mathbf{v}^{(i)}) \le \sum_{i=1}^p \lambda_i (\mathbf{c}^T \mathbf{v}^*) = (\mathbf{c}^T \mathbf{v}^*) \sum_{i=1}^p \lambda_i = \mathbf{c}^T \mathbf{v}^*$$

Because $\mathbf{v}^* \in \mathcal{F}$ and $\mathbf{c}^T\mathbf{x} \le \mathbf{c}^T\mathbf{v}^*$ for every $\mathbf{x} \in \mathcal{F}$, the extreme point (BFS) $\mathbf{v}^*$ is globally optimal! Finally, if $\mathbf{c}^T\mathbf{v}^{(1)} = \dots = \mathbf{c}^T\mathbf{v}^{(r)} = Z^*$, then for any convex combination $\bar{\mathbf{x}} = \sum_{i=1}^r \lambda_i \mathbf{v}^{(i)}$, convexity of $\mathcal{F}$ guarantees $\bar{\mathbf{x}} \in \mathcal{F}$ and linearity gives $\mathbf{c}^T\bar{\mathbf{x}} = \sum_{i=1}^r \lambda_i (\mathbf{c}^T\mathbf{v}^{(i)}) = Z^* \sum_{i=1}^r \lambda_i = Z^*$, completing the proof.

The operational significance of the Fundamental Theorem is monumental: an optimization problem over an uncountably infinite continuous continuum $\mathcal{F} \subseteq \mathbb{R}^n$ is rigorously reduced to a finite combinatorial search over at most $\binom{n}{m}$ Basic Feasible Solutions, laying the exact theoretical foundation for Dantzig's Simplex Algorithm in Unit 2.

### Two-Dimensional Graphical Optimization, Pathological Regimes, and Statistical LP Formulations

When a Linear Programming Problem involves only $n = 2$ structural decision variables $(x_1, x_2)$, the polyhedral geometry of the feasible region $\mathcal{F} \subseteq \mathbb{R}^2$ and the Fundamental Theorem of Linear Programming can be visualized directly in the Cartesian plane. Each linear inequality constraint $a_{i1} x_1 + a_{i2} x_2 \le b_i$ defines a boundary line $a_{i1} x_1 + a_{i2} x_2 = b_i$ and a corresponding closed half-plane. For any fixed trial value $Z_0 \in \mathbb{R}$ of the objective function, the locus of points satisfying $c_1 x_1 + c_2 x_2 = Z_0$ forms a straight **iso-profit line** (for maximization) or **iso-cost line** (for minimization) with slope $m_Z = -c_1 / c_2$, orthogonal to the objective gradient vector $\nabla Z = \mathbf{c} = (c_1, c_2)^T$. Translating the iso-profit line parallel to itself in the direction of $\mathbf{c}$ increases $Z_0$ continuously until the line is about to exit the feasible polygon $\mathcal{F}$ at its last point(s) of contact—which must be a corner vertex (extreme point) or a complete boundary edge joining two adjacent vertices.

### Four Exhaustive Geometric Regimes of a Linear Program

Both in two dimensions and in general $\mathbb{R}^n$, any Linear Programming Problem falls into exactly one of four mutually exclusive mathematical regimes:

1. **Unique Finite Optimal Solution**: The optimal iso-profit hyperplane $H(\mathbf{c}, Z^*)$ intersects the feasible polyhedron $\mathcal{F}$ at a single extreme point $\mathbf{v}^*$, which occurs whenever the slope of the objective function is strictly intermediate between the slopes of the binding boundary hyperplanes intersecting at $\mathbf{v}^*$.
2. **Alternative (Multiple) Optimal Solutions**: When the objective normal vector $\mathbf{c}$ is parallel to one of the binding boundary hyperplanes (or lies in the conical hull of active constraint normals at a face), the optimal iso-profit hyperplane $H(\mathbf{c}, Z^*)$ coincides with an entire edge or higher-dimensional face of $\mathcal{F}$, yielding two or more optimal extreme points and uncountably many optimal convex combinations along that face.
3. **Unbounded Objective Value**: When the feasible polyhedron $\mathcal{F}$ is unbounded in the direction of the objective gradient $\mathbf{c}$—meaning there exists an extreme ray $\mathbf{r} \in \mathcal{R}$ satisfying $\mathbf{A}\mathbf{r} = \mathbf{0}, \mathbf{r} \ge \mathbf{0}$ and $\mathbf{c}^T\mathbf{r} > 0$—translating the iso-profit hyperplane in the direction of $\mathbf{c}$ never leaves $\mathcal{F}$, driving $Z(\mathbf{x}_0 + \mu\mathbf{r}) \to +\infty$ as $\mu \to +\infty$. In practical modeling, unboundedness almost always signals an omitted resource capacity constraint.
4. **Infeasible System ($\mathcal{F} = \emptyset$)**: When contradictory constraints—such as $x_1 + x_2 \le 4$ and $x_1 + x_2 \ge 7$ with $x_1, x_2 \ge 0$—possess mutually disjoint half-spaces, the intersection $\mathcal{F}$ is empty and no feasible vector exists.

### Formulating Statistical Estimation as Linear Programs: $L_1$ and $L_\infty$ Regression

In mathematical statistics, when experimental response data $y_i = \mathbf{z}_i^T \boldsymbol{\beta} + \varepsilon_i$ ($i = 1, \dots, N$) are contaminated by heavy-tailed Cauchy, Laplace, or gross outlier disturbances, classical Ordinary Least Squares ($\min \sum \varepsilon_i^2$) suffers from a zero breakdown point. Operations Research provides two fundamental linear programming alternatives:
- **Least Absolute Deviations ($L_1$ / Median Regression)**: To minimize $\sum_{i=1}^N |y_i - \mathbf{z}_i^T \boldsymbol{\beta}|$, we decompose each unrestricted residual $\varepsilon_i = u_i - v_i$ into a positive vertical deviation $u_i \ge 0$ and a negative vertical deviation $v_i \ge 0$, and decompose the unrestricted regression parameter vector $\boldsymbol{\beta} = \boldsymbol{\beta}^+ - \boldsymbol{\beta}^-$ ($\boldsymbol{\beta}^+, \boldsymbol{\beta}^- \ge \mathbf{0}$). The statistical estimation problem becomes the exact Linear Program:
  $$\text{Minimize } \sum_{i=1}^N (u_i + v_i) \quad \text{subject to} \quad \mathbf{z}_i^T (\boldsymbol{\beta}^+ - \boldsymbol{\beta}^-) + u_i - v_i = y_i \quad (i=1,\dots,N), \quad \boldsymbol{\beta}^+, \boldsymbol{\beta}^-, u_i, v_i \ge 0$$
  By the Fundamental Theorem of Linear Programming, an optimal $L_1$ regression hyperplane in $\mathbb{R}^p$ always passes exactly through at least $p$ observed data points (where $u_i = v_i = 0$)!
- **Chebyshev ($L_\infty$ / Minimax) Regression**: When uniform approximation error must be controlled across bounded-noise instruments, we minimize the maximum absolute residual $r = \max_{1 \le i \le N} |y_i - \mathbf{z}_i^T \boldsymbol{\beta}|$ via the Linear Program:
  $$\text{Minimize } r \quad \text{subject to} \quad -r \le y_i - \mathbf{z}_i^T (\boldsymbol{\beta}^+ - \boldsymbol{\beta}^-) \le r \quad (i=1,\dots,N), \quad r \ge 0, \quad \boldsymbol{\beta}^+, \boldsymbol{\beta}^- \ge \mathbf{0}$$

## Worked Questions and Solutions

### Question 1: Transformation of a Multi-Constraint Linear Program with Unrestricted Variables into Standard Matrix Form

Consider a statistical calibration and resource allocation problem formulated as the following general Linear Programming Problem:

$$\text{Minimize } W = 4x_1 - 6x_2 + 3x_3$$

subject to the structural constraints:

$$\begin{aligned}
2x_1 - x_2 + 3x_3 &\le 18 \\
-x_1 + 4x_2 - 2x_3 &\le -12 \\
3x_1 + 2x_2 - x_3 &= 15
\end{aligned}$$

with variable domain restrictions $x_1 \ge 0$, $x_2 \le 0$, and $x_3 \in \mathbb{R}$ unrestricted in sign.

1. Transform the problem step-by-step into **Standard Form** ($\text{Maximize } Z = \tilde{\mathbf{c}}^T \tilde{\mathbf{x}}$ subject to $\tilde{\mathbf{A}}\tilde{\mathbf{x}} = \tilde{\mathbf{b}}$ with $\tilde{\mathbf{b}} \ge \mathbf{0}$ and $\tilde{\mathbf{x}} \ge \mathbf{0}$).
2. Explicitly write out the transformed decision vector $\tilde{\mathbf{x}}$, the cost vector $\tilde{\mathbf{c}}$, the right-hand-side vector $\tilde{\mathbf{b}}$, and the $3 \times 6$ technological matrix $\tilde{\mathbf{A}}$.
3. Determine the rank of $\tilde{\mathbf{A}}$ and compute the combinatorial upper bound on the number of basic solutions.

### Solution, step 1: Convert variable sign restrictions and objective sense

First, we standardize the variable domains so that every structural variable is restricted to be non-negative:
- $x_1 \ge 0$ is already in standard non-negative form.
- Since $x_2 \le 0$ is non-positive, define $x_2' = -x_2 \ge 0$, so that $x_2 = -x_2'$.
- Since $x_3 \in \mathbb{R}$ is unrestricted in sign, express $x_3$ as the difference of two non-negative variables: $x_3 = x_3^+ - x_3^-$ with $x_3^+ \ge 0$ and $x_3^- \ge 0$.

Second, convert the minimization objective $\min W = 4x_1 - 6x_2 + 3x_3$ into an equivalent maximization objective $Z = -W$:

$$\text{Maximize } Z = -W = -4x_1 + 6x_2 - 3x_3 = -4x_1 - 6x_2' - 3x_3^+ + 3x_3^-$$

### Solution, step 2: Standardize right-hand sides and introduce slack and surplus variables

Substitute $x_2 = -x_2'$ and $x_3 = x_3^+ - x_3^-$ into the three structural constraints:
1. Constraint 1 has $b_1 = 18 \ge 0$ and a $\le$ inequality. Adding a non-negative slack variable $s_1 \ge 0$ gives:
   $$2x_1 + x_2' + 3x_3^+ - 3x_3^- + s_1 = 18$$
2. Constraint 2 initially has a negative right-hand side $b_2 = -12 < 0$:
   $$-x_1 - 4x_2' - 2x_3^+ + 2x_3^- \le -12$$
   Multiply the entire inequality by $-1$ to make the right-hand side positive, which reverses the inequality from $\le$ to $\ge$:
   $$x_1 + 4x_2' + 2x_3^+ - 2x_3^- \ge 12$$
   Now subtract a non-negative surplus variable $e_2 \ge 0$ to convert the $\ge$ inequality into an exact equation:
   $$x_1 + 4x_2' + 2x_3^+ - 2x_3^- - e_2 = 12$$
3. Constraint 3 is already an exact equality with a positive right-hand side $b_3 = 15 > 0$:
   $$3x_1 - 2x_2' - x_3^+ + x_3^- = 15$$

### Solution, step 3: Assemble the matrix components and compute the basic solution bound

The standardized decision vector $\tilde{\mathbf{x}} \in \mathbb{R}_+^6$, objective vector $\tilde{\mathbf{c}} \in \mathbb{R}^6$, right-hand-side vector $\tilde{\mathbf{b}} \in \mathbb{R}_+^3$, and technological matrix $\tilde{\mathbf{A}} \in \mathbb{R}^{3 \times 6}$ are:

$$\tilde{\mathbf{x}} = \begin{pmatrix} x_1 \\ x_2' \\ x_3^+ \\ x_3^- \\ s_1 \\ e_2 \end{pmatrix} \ge \mathbf{0}, \qquad \tilde{\mathbf{c}} = \begin{pmatrix} -4 \\ -6 \\ -3 \\ 3 \\ 0 \\ 0 \end{pmatrix}, \qquad \tilde{\mathbf{b}} = \begin{pmatrix} 18 \\ 12 \\ 15 \end{pmatrix}$$

$$\tilde{\mathbf{A}} = \begin{pmatrix} 2 & 1 & 3 & -3 & 1 & 0 \\ 1 & 4 & 2 & -2 & 0 & -1 \\ 3 & -2 & -1 & 1 & 0 & 0 \end{pmatrix}$$

Notice that the columns corresponding to $x_1, s_1, e_2$ form an upper-triangular-permuted submatrix with determinant $\det \begin{pmatrix} 2 & 1 & 0 \\ 1 & 0 & -1 \\ 3 & 0 & 0 \end{pmatrix} = 3(-1) = -3 \ne 0$. Therefore, $\text{rank}(\tilde{\mathbf{A}}) = m = 3$ with $n = 6$ total variables. The maximum number of candidate basic solutions is bounded by $\binom{6}{3} = \frac{6!}{3!3!} = 20$ (in fact, because columns 3 and 4 for $x_3^+$ and $x_3^-$ are collinear, any 3-column subset containing both $x_3^+$ and $x_3^-$ has determinant zero, leaving at most $\binom{6}{3} - 4 = 16$ nonsingular bases).

### Question 2: Exhaustive Enumeration of Basic Solutions, Feasibility Classification, and Extreme Point Verification

Consider the following two-variable Linear Programming Problem:

$$\text{Maximize } Z = 5x_1 + 4x_2$$

subject to:

$$\begin{aligned}
2x_1 + x_2 &\le 12 \\
x_1 + 2x_2 &\le 9 \\
x_1, x_2 &\ge 0
\end{aligned}$$

1. Convert the problem into standard equality form by introducing slack variables $x_3, x_4 \ge 0$, and determine the total number of candidate subsets of $m=2$ basic variables out of $n=4$.
2. Compute all $\binom{4}{2} = 6$ basic solutions algebraically, classifying each as either a **Basic Feasible Solution (BFS)** or a **Basic Infeasible Solution**.
3. Identify the unique optimal extreme point $(\mathbf{x}^*, Z^*)$ via the Fundamental Theorem of Linear Programming.

### Solution, step 1: Formulate standard equality system and enumerate basis pairs

Introducing slack variables $x_3 \ge 0$ and $x_4 \ge 0$, the standard equality system $\mathbf{A}\mathbf{x} = \mathbf{b}$ with $m = 2$ equations and $n = 4$ variables is:

$$\begin{pmatrix} 2 & 1 & 1 & 0 \\ 1 & 2 & 0 & 1 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} = \begin{pmatrix} 12 \\ 9 \end{pmatrix}, \qquad x_1, x_2, x_3, x_4 \ge 0$$

Since $\text{rank}(\mathbf{A}) = 2$, each basic solution is obtained by selecting $m = 2$ basic variables, setting the remaining $n - m = 2$ non-basic variables to zero, and solving the $2 \times 2$ linear system $\mathbf{B}\mathbf{x}_B = \mathbf{b}$. There are $\binom{4}{2} = 6$ possible pairs of basic variables.

### Solution, step 2: Solve all six 2x2 systems and classify feasibility

Evaluating each of the 6 candidate basis pairs:

1. **Basis $\{x_3, x_4\}$** (Non-basic $x_1 = 0, x_2 = 0$):
   $$x_3 = 12, \quad x_4 = 9 \implies \mathbf{x}^{(1)} = (0, 0, 12, 9)^T \ge \mathbf{0} \quad (\text{BFS, } Z = 0)$$
2. **Basis $\{x_1, x_4\}$** (Non-basic $x_2 = 0, x_3 = 0$):
   $$2x_1 = 12 \implies x_1 = 6; \quad x_1 + x_4 = 9 \implies x_4 = 3 \implies \mathbf{x}^{(2)} = (6, 0, 0, 3)^T \ge \mathbf{0} \quad (\text{BFS, } Z = 30)$$
3. **Basis $\{x_1, x_3\}$** (Non-basic $x_2 = 0, x_4 = 0$):
   $$x_1 = 9; \quad 2(9) + x_3 = 12 \implies x_3 = -6 < 0 \implies \mathbf{x}^{(3)} = (9, 0, -6, 0)^T \quad (\text{Basic Infeasible})$$
4. **Basis $\{x_2, x_3\}$** (Non-basic $x_1 = 0, x_4 = 0$):
   $$2x_2 = 9 \implies x_2 = 4.5; \quad 4.5 + x_3 = 12 \implies x_3 = 7.5 \implies \mathbf{x}^{(4)} = (0, 4.5, 7.5, 0)^T \ge \mathbf{0} \quad (\text{BFS, } Z = 18)$$
5. **Basis $\{x_2, x_4\}$** (Non-basic $x_1 = 0, x_3 = 0$):
   $$x_2 = 12; \quad 2(12) + x_4 = 9 \implies x_4 = -15 < 0 \implies \mathbf{x}^{(5)} = (0, 12, 0, -15)^T \quad (\text{Basic Infeasible})$$
6. **Basis $\{x_1, x_2\}$** (Non-basic $x_3 = 0, x_4 = 0$):
   $$2x_1 + x_2 = 12 \text{ and } x_1 + 2x_2 = 9 \implies x_1 = 5, \quad x_2 = 2 \implies \mathbf{x}^{(6)} = (5, 2, 0, 0)^T \ge \mathbf{0} \quad (\text{BFS, } Z = 33)$$

### Solution, step 3: Summary table and identification of optimal extreme point

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Basis Pair</th><th>Non-Basic Variables</th><th>Solution Vector $(x_1, x_2, x_3, x_4)$</th><th>Feasibility Status</th><th>Objective $Z = 5x_1 + 4x_2$</th></tr></thead><tbody><tr><td>$\{x_3, x_4\}$</td><td>$x_1=0, x_2=0$</td><td>$(0, 0, 12, 9)$</td><td>Feasible (BFS / Origin Vertex)</td><td>$0$</td></tr><tr><td>$\{x_1, x_4\}$</td><td>$x_2=0, x_3=0$</td><td>$(6, 0, 0, 3)$</td><td>Feasible (BFS / Horizontal Vertex)</td><td>$30$</td></tr><tr><td>$\{x_1, x_3\}$</td><td>$x_2=0, x_4=0$</td><td>$(9, 0, -6, 0)$</td><td>Infeasible ($x_3 = -6 < 0$)</td><td>N/A</td></tr><tr><td>$\{x_2, x_3\}$</td><td>$x_1=0, x_4=0$</td><td>$(0, 4.5, 7.5, 0)$</td><td>Feasible (BFS / Vertical Vertex)</td><td>$18$</td></tr><tr><td>$\{x_2, x_4\}$</td><td>$x_1=0, x_3=0$</td><td>$(0, 12, 0, -15)$</td><td>Infeasible ($x_4 = -15 < 0$)</td><td>N/A</td></tr><tr><td>$\{x_1, x_2\}$</td><td>$x_3=0, x_4=0$</td><td>$(5, 2, 0, 0)$</td><td>Feasible (BFS / Intersection Vertex)</td><td>$33$ (Optimal)</td></tr></tbody></table></div>

The feasible polyhedron $\mathcal{F}$ is a bounded quadrilateral with exactly $4$ extreme points: $(0,0)$, $(6,0)$, $(0,4.5)$, and $(5,2)$. By the Fundamental Theorem of Linear Programming, the maximum objective value occurs at the extreme point $\mathbf{x}^* = (x_1^*, x_2^*) = (5, 2)$ with slack variables $x_3^* = 0, x_4^* = 0$ (both constraints actively binding) and maximum objective $Z^* = 5(5) + 4(2) = 33$.

### Question 3: Analytical Proof of Convexity of Level Sets and Convexity of the Optimal Solution Set

Let $\mathcal{F} = \{\mathbf{x} \in \mathbb{R}^n : \mathbf{A}\mathbf{x} \le \mathbf{b}, \mathbf{x} \ge \mathbf{0}\}$ be the non-empty feasible polyhedron of a Linear Programming Problem with objective $Z(\mathbf{x}) = \mathbf{c}^T\mathbf{x}$, and assume $Z^* = \max_{\mathbf{x} \in \mathcal{F}} \mathbf{c}^T\mathbf{x} < \infty$.

1. Prove rigorously that the set of all optimal solutions, $\mathcal{F}^* = \{\mathbf{x} \in \mathcal{F} : \mathbf{c}^T\mathbf{x} = Z^*\}$, is a convex set.
2. Prove that if a Linear Programming Problem possesses two distinct optimal solutions $\mathbf{x}^{(1)} \ne \mathbf{x}^{(2)}$, then it possesses uncountably infinitely many optimal solutions.
3. Prove that no interior point of $\mathcal{F}$ can ever be the unique optimal solution when $\mathbf{c} \ne \mathbf{0}$.

### Solution, step 1: Prove that the optimal solution set F* is convex

Notice that the optimal solution set $\mathcal{F}^*$ can be written as the intersection of the convex feasible polyhedron $\mathcal{F}$ and the optimal iso-profit hyperplane $H(\mathbf{c}, Z^*) = \{\mathbf{x} \in \mathbb{R}^n : \mathbf{c}^T\mathbf{x} = Z^*\}$:

$$\mathcal{F}^* = \mathcal{F} \cap H(\mathbf{c}, Z^*)$$

Directly, let $\mathbf{x}^{(1)}, \mathbf{x}^{(2)} \in \mathcal{F}^*$ be any two optimal solutions, and let $\lambda \in [0, 1]$. Because $\mathbf{x}^{(1)}, \mathbf{x}^{(2)} \in \mathcal{F}$ and $\mathcal{F}$ is convex by Theorem 1.1, their convex combination $\mathbf{x}(\lambda) = \lambda \mathbf{x}^{(1)} + (1-\lambda)\mathbf{x}^{(2)}$ belongs to $\mathcal{F}$. Furthermore, evaluating the linear objective function at $\mathbf{x}(\lambda)$ yields:

$$\mathbf{c}^T \mathbf{x}(\lambda) = \mathbf{c}^T \left( \lambda \mathbf{x}^{(1)} + (1 - \lambda) \mathbf{x}^{(2)} \right) = \lambda (\mathbf{c}^T \mathbf{x}^{(1)}) + (1 - \lambda) (\mathbf{c}^T \mathbf{x}^{(2)}) = \lambda Z^* + (1 - \lambda) Z^* = Z^*$$

Since $\mathbf{x}(\lambda) \in \mathcal{F}$ and $\mathbf{c}^T\mathbf{x}(\lambda) = Z^*$, we have $\mathbf{x}(\lambda) \in \mathcal{F}^*$ for all $\lambda \in [0, 1]$. Thus $\mathcal{F}^*$ is a convex set.

### Solution, step 2: Establish uncountably infinite optima from two distinct optima

Suppose $\mathbf{x}^{(1)}, \mathbf{x}^{(2)} \in \mathcal{F}^*$ with $\mathbf{x}^{(1)} \ne \mathbf{x}^{(2)}$, so the displacement vector $\mathbf{d} = \mathbf{x}^{(1)} - \mathbf{x}^{(2)} \ne \mathbf{0}$. Consider the mapping $\phi: [0, 1] \to \mathcal{F}^*$ defined by:

$$\phi(\lambda) = \lambda \mathbf{x}^{(1)} + (1 - \lambda)\mathbf{x}^{(2)} = \mathbf{x}^{(2)} + \lambda (\mathbf{x}^{(1)} - \mathbf{x}^{(2)})$$

By Step 1, $\phi(\lambda) \in \mathcal{F}^*$ for every real number $\lambda \in [0, 1]$. Moreover, for any two distinct scalars $\lambda_1 \ne \lambda_2$ in $[0, 1]$:

$$\phi(\lambda_1) - \phi(\lambda_2) = (\lambda_1 - \lambda_2)(\mathbf{x}^{(1)} - \mathbf{x}^{(2)}) \ne \mathbf{0}$$

because $\lambda_1 - \lambda_2 \ne 0$ and $\mathbf{x}^{(1)} - \mathbf{x}^{(2)} \ne \mathbf{0}$. Thus $\phi$ is a strictly injective (one-to-one) mapping from the uncountable continuum $[0, 1]$ into $\mathcal{F}^*$, proving that $\mathcal{F}^*$ contains uncountably infinitely many distinct optimal solutions.

### Solution, step 3: Prove that an interior point cannot be a maximizer when c != 0

Suppose $\mathbf{x}_0 \in \text{int}(\mathcal{F})$ is an interior point of $\mathcal{F}$, and assume $\mathbf{c} \ne \mathbf{0}$ (so $\|\mathbf{c}\|_2^2 = \mathbf{c}^T\mathbf{c} > 0$). By definition of an interior point in $\mathbb{R}^n$, there exists an open Euclidean ball $B(\mathbf{x}_0, r) = \{\mathbf{x} \in \mathbb{R}^n : \|\mathbf{x} - \mathbf{x}_0\|_2 < r\}$ of radius $r > 0$ contained entirely within $\mathcal{F}$.

Consider moving from $\mathbf{x}_0$ in the direction of the positive objective gradient $\mathbf{c}$ by setting:

$$\hat{\mathbf{x}} = \mathbf{x}_0 + \frac{r}{2 \|\mathbf{c}\|_2} \mathbf{c}$$

Since $\|\hat{\mathbf{x}} - \mathbf{x}_0\|_2 = \frac{r}{2} < r$, we have $\hat{\mathbf{x}} \in B(\mathbf{x}_0, r) \subseteq \mathcal{F}$, so $\hat{\mathbf{x}}$ is strictly feasible. Evaluating the objective function at $\hat{\mathbf{x}}$ yields:

$$\mathbf{c}^T \hat{\mathbf{x}} = \mathbf{c}^T \mathbf{x}_0 + \frac{r}{2 \|\mathbf{c}\|_2} \mathbf{c}^T \mathbf{c} = \mathbf{c}^T \mathbf{x}_0 + \frac{r}{2} \|\mathbf{c}\|_2 > \mathbf{c}^T \mathbf{x}_0$$

Because $\hat{\mathbf{x}} \in \mathcal{F}$ achieves a strictly higher objective value than $\mathbf{x}_0$, no interior point $\mathbf{x}_0 \in \text{int}(\mathcal{F})$ can ever be an optimal solution when $\mathbf{c} \ne \mathbf{0}$; all optimal solutions must lie on the boundary $\partial \mathcal{F}$ of the feasible polyhedron.
