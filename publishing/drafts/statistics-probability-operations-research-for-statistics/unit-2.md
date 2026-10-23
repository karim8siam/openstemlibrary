# Unit 2: The Simplex Algorithm, Artificial Variable Architectures & Degeneracy Resolution

## 2.1 Algebraic Architecture of the Simplex Method: Basis Matrices, Canonical Dictionaries, and Reduced Costs

Although the Fundamental Theorem of Linear Programming (Theorem 1.3) guarantees that an optimal solution of $\max Z = \mathbf{c}^T\mathbf{x}$ subject to $\mathbf{A}\mathbf{x} = \mathbf{b}, \mathbf{x} \ge \mathbf{0}$ occurs at a Basic Feasible Solution (BFS), brute-force enumeration of all $\binom{n}{m}$ candidate bases is computationally intractable even for moderate dimensions (for instance, $m = 50$ equations in $n = 100$ variables yields $\binom{100}{50} \approx 1.0089 \times 10^{29}$ bases). Invented by George B. Dantzig in 1947, the **Simplex Algorithm** circumvents exhaustive enumeration by moving systematically along edges of the feasible polyhedron $\mathcal{F}$ from one extreme point (BFS) to an **adjacent** extreme point in a direction that monotonically improves (or leaves non-decreasing) the objective function $Z$, terminating in a finite number of steps at a global optimum or a certificate of unboundedness.

Let the standard-form linear program be specified by $\mathbf{A} \in \mathbb{R}^{m \times n}$ with $\text{rank}(\mathbf{A}) = m < n$ and $\mathbf{b} \in \mathbb{R}_+^m$. At any iteration of the Simplex Algorithm, we partition the column indices $\{1, 2, \dots, n\}$ into a **basic index set** $B = \{B(1), B(2), \dots, B(m)\}$ of $m$ indices whose columns form an invertible $m \times m$ basis matrix $\mathbf{B} = [\mathbf{a}_{B(1)}, \dots, \mathbf{a}_{B(m)}]$, and a **non-basic index set** $N$ of the remaining $n - m$ indices with matrix $\mathbf{N}$. Partitioning the variable vector $\mathbf{x}$ and cost vector $\mathbf{c}$ conformably into $(\mathbf{x}_B, \mathbf{x}_N)$ and $(\mathbf{c}_B, \mathbf{c}_N)$, the structural equations $\mathbf{A}\mathbf{x} = \mathbf{b}$ and objective $Z = \mathbf{c}^T\mathbf{x}$ take the partitioned form:

$$\mathbf{B}\mathbf{x}_B + \mathbf{N}\mathbf{x}_N = \mathbf{b}, \qquad Z = \mathbf{c}_B^T \mathbf{x}_B + \mathbf{c}_N^T \mathbf{x}_N$$

Because $\mathbf{B}$ is nonsingular, we premultiply the constraint system by $\mathbf{B}^{-1}$ to express the basic variables $\mathbf{x}_B$ explicitly as affine functions of the non-basic variables $\mathbf{x}_N$ (often termed Dantzig's **canonical dictionary** representation):

$$\mathbf{x}_B = \mathbf{B}^{-1}\mathbf{b} - \mathbf{B}^{-1}\mathbf{N}\mathbf{x}_N = \bar{\mathbf{b}} - \sum_{j \in N} \mathbf{y}_j x_j$$

where $\bar{\mathbf{b}} = \mathbf{B}^{-1}\mathbf{b} \in \mathbb{R}_+^m$ is the current basic feasible right-hand-side vector, and $\mathbf{y}_j = \mathbf{B}^{-1}\mathbf{a}_j = (y_{1j}, y_{2j}, \dots, y_{mj})^T \in \mathbb{R}^m$ is the representation (coordinate vector) of column $\mathbf{a}_j$ with respect to the current basis $\mathbf{B}$, since $\mathbf{a}_j = \mathbf{B}\mathbf{y}_j = \sum_{i=1}^m y_{ij} \mathbf{a}_{B(i)}$.

Substituting this representation of $\mathbf{x}_B$ into the objective functional eliminates the basic variables from $Z$:

$$Z = \mathbf{c}_B^T \left( \mathbf{B}^{-1}\mathbf{b} - \sum_{j \in N} \mathbf{y}_j x_j \right) + \sum_{j \in N} c_j x_j = \mathbf{c}_B^T \bar{\mathbf{b}} - \sum_{j \in N} \left( \mathbf{c}_B^T \mathbf{B}^{-1}\mathbf{a}_j - c_j \right) x_j$$

For every variable index $j \in \{1, \dots, n\}$, we define the scalar quantity $z_j$ as the **imputed resource value** (the opportunity cost of the resources consumed by one unit of activity $j$ under basis $\mathbf{B}$):

$$z_j = \mathbf{c}_B^T \mathbf{y}_j = \mathbf{c}_B^T \mathbf{B}^{-1} \mathbf{a}_j = \sum_{i=1}^m c_{B(i)} y_{ij}$$

This allows us to write the fundamental **Simplex Objective Identity** holding for every feasible vector $\mathbf{x} \in \mathcal{F}$:

$$Z(\mathbf{x}) = Z_0 - \sum_{j \in N} (z_j - c_j) x_j = Z_0 + \sum_{j \in N} (c_j - z_j) x_j$$

where $Z_0 = \mathbf{c}_B^T \bar{\mathbf{b}}$ is the objective value at the current BFS $(\mathbf{x}_B = \bar{\mathbf{b}}, \mathbf{x}_N = \mathbf{0})$. Notice that for any basic variable $j = B(i) \in B$, since $\mathbf{y}_{B(i)} = \mathbf{B}^{-1}\mathbf{a}_{B(i)} = \mathbf{e}_i$ (the $i$-th standard unit vector), we always have $z_{B(i)} = \mathbf{c}_B^T \mathbf{e}_i = c_{B(i)}$, so the net evaluation $z_j - c_j = 0$ identically for all basic variables. For non-basic variables $j \in N$, the quantity $\bar{c}_j = c_j - z_j$ is called the **relative profit** (or **reduced cost** in minimization), while $z_j - c_j = -\bar{c}_j$ is the standard **net evaluation row** entry in the classical Simplex tableau.

## 2.2 Optimality Criterion, Entering Variable Pricing, and the Minimum Ratio Feasibility Test

The Simplex Objective Identity $Z(\mathbf{x}) = Z_0 - \sum_{j \in N} (z_j - c_j) x_j$ immediately yields both the sufficient condition for global optimality and the exact geometric rule for moving to a superior adjacent vertex when the current BFS is suboptimal.

### Theorem 2.1 (Simplex Optimality Criterion):
In a maximization Linear Programming Problem with current Basic Feasible Solution $\mathbf{x}^{(0)} = (\bar{\mathbf{b}}^T, \mathbf{0}^T)^T$, if the net evaluation row satisfies:

$$z_j - c_j \ge 0 \quad (\text{equivalently, reduced profit } \bar{c}_j = c_j - z_j \le 0) \qquad \forall j \in N$$

then $\mathbf{x}^{(0)}$ is a **globally optimal Basic Feasible Solution** over the entire feasible polyhedron $\mathcal{F}$, with maximum objective value $Z^* = Z_0 = \mathbf{c}_B^T \mathbf{B}^{-1}\mathbf{b}$. (For a minimization problem $\min W = \mathbf{c}^T\mathbf{x}$, the optimality condition is reversed: $z_j - c_j \le 0$, or $\bar{c}_j = c_j - z_j \ge 0$, for all $j \in N$.)

#### Proof:
Let $\mathbf{x} \in \mathcal{F}$ be any arbitrary feasible vector in the polyhedron. Because $\mathbf{x} \in \mathcal{F}$, all components of $\mathbf{x}$ satisfy non-negativity, so in particular $x_j \ge 0$ for every non-basic index $j \in N$. Since $z_j - c_j \ge 0$ and $x_j \ge 0$ for all $j \in N$, each product $(z_j - c_j)x_j \ge 0$. Summing over $j \in N$ gives $\sum_{j \in N} (z_j - c_j)x_j \ge 0$, and therefore:

$$Z(\mathbf{x}) = Z_0 - \sum_{j \in N} (z_j - c_j) x_j \le Z_0 = Z(\mathbf{x}^{(0)}) \qquad \forall \mathbf{x} \in \mathcal{F}$$

Thus no feasible solution in $\mathcal{F}$ can exceed $Z_0$, proving global optimality of $\mathbf{x}^{(0)}$.

### Entering Variable Selection (Dantzig's Steepest-Edge-Coefficient Rule)

Suppose the optimality condition fails at the current BFS, so there exists at least one non-basic index $k \in N$ with $z_k - c_k < 0$ (i.e., $c_k - z_k > 0$). Increasing $x_k$ from $0$ to a positive step length $\theta > 0$ while holding all other non-basic variables $x_j = 0$ ($j \in N \setminus \{k\}$) increases the objective function at the positive marginal rate $\frac{\partial Z}{\partial x_k} = c_k - z_k > 0$:

$$Z(\theta) = Z_0 - (z_k - c_k)\theta = Z_0 + (c_k - z_k)\theta > Z_0$$

Under **Dantzig's Most Negative $z_j - c_j$ Rule** (largest positive $\bar{c}_j = c_j - z_k$), the entering column index $k \in N$ is chosen to maximize the marginal rate of objective improvement per unit of $x_k$:

$$z_k - c_k = \min_{j \in N} \left\{ z_j - c_j : z_j - c_j < 0 \right\}$$

### Leaving Variable Selection: The Minimum Ratio Test

As the entering variable $x_k$ increases from $0$ to $\theta \ge 0$ (with all other non-basic variables kept at $0$), the $m$ basic variables $\mathbf{x}_B(\theta)$ adjust linearly along the **simplex edge direction** $\mathbf{d}_B = -\mathbf{y}_k = -\mathbf{B}^{-1}\mathbf{a}_k$ to maintain $\mathbf{A}\mathbf{x}(\theta) = \mathbf{b}$:

$$x_{B(i)}(\theta) = \bar{b}_i - y_{ik} \theta, \qquad i = 1, 2, \dots, m$$

To preserve primal feasibility ($\mathbf{x}_B(\theta) \ge \mathbf{0}$), every basic component $x_{B(i)}(\theta)$ must remain non-negative:
- If $y_{ik} \le 0$, then as $\theta > 0$ increases, $-y_{ik}\theta \ge 0$, so $x_{B(i)}(\theta) = \bar{b}_i - y_{ik}\theta \ge \bar{b}_i \ge 0$ grows or remains constant and **never blocks** the increase of $\theta$.
- If $y_{ik} > 0$, then $x_{B(i)}(\theta) = \bar{b}_i - y_{ik}\theta$ decreases linearly with $\theta$ and hits zero at the critical ratio $\theta_i = \bar{b}_i / y_{ik} \ge 0$.

Therefore, the largest permissible step size $\theta^*$ that preserves non-negativity across **all** $m$ basic variables simultaneously is determined by the **Simplex Minimum Ratio Test**:

$$\theta^* = \min_{1 \le i \le m} \left\{ \frac{\bar{b}_i}{y_{ik}} : y_{ik} > 0 \right\} = \frac{\bar{b}_r}{y_{rk}} \ge 0$$

The basic variable $x_{B(r)}$ achieving this minimum ratio is driven to zero at $\theta = \theta^*$ and becomes the **leaving variable** (departing the basis), while $x_k = \theta^*$ enters the basis in row $r$. The intersection entry $y_{rk} > 0$ is the **pivot element**. Performing a Gauss–Jordan row operation (dividing pivot row $r$ by $y_{rk}$ and eliminating column $k$ in all other rows $i \ne r$ and the $z_j - c_j$ row) updates the basis to $\mathbf{B}_{\text{new}} = \mathbf{B} + (\mathbf{a}_k - \mathbf{a}_{B(r)})\mathbf{e}_r^T$ and increases the objective to $Z_{\text{new}} = Z_0 + \theta^*(c_k - z_k) \ge Z_0$.

## 2.3 Unboundedness Certificates, Extreme Rays, and Alternative Optimal Solutions

Beyond converging to a unique optimal vertex, the Simplex tableau provides complete algebraic certificates for two important geometric phenomena: **unboundedness** of the objective functional and **alternative (multiple) optimal solutions** along a polyhedral face.

### Algebraic Certificate of Unboundedness

Suppose at some iteration of the Simplex Algorithm there exists a non-basic entering candidate $x_k$ with $z_k - c_k < 0$ (so increasing $x_k$ strictly increases $Z$), but every entry in its updated tableau column is non-positive:

$$\mathbf{y}_k = \mathbf{B}^{-1}\mathbf{a}_k \le \mathbf{0} \quad \left(\text{i.e., } y_{ik} \le 0 \text{ for all } i = 1, 2, \dots, m\right)$$

Then the Minimum Ratio Test set $\{ \bar{b}_i / y_{ik} : y_{ik} > 0 \}$ is empty ($\theta^* = +\infty$)! Let us construct the full $n$-dimensional ray trajectory $\mathbf{x}(\theta) = \mathbf{x}^{(0)} + \theta \mathbf{d}$ for $\theta \ge 0$, where $\mathbf{x}^{(0)}$ is the current BFS and the direction vector $\mathbf{d} \in \mathbb{R}^n$ is defined by:

$$d_{B(i)} = -y_{ik} \ge 0 \quad (i = 1, \dots, m), \qquad d_k = 1, \qquad d_j = 0 \quad (j \in N \setminus \{k\})$$

Notice three remarkable properties of this direction vector $\mathbf{d}$:
1. **Non-negativity**: Because $y_{ik} \le 0$ for all $i$, every component of $\mathbf{d}$ is non-negative ($\mathbf{d} \ge \mathbf{0}, \mathbf{d} \ne \mathbf{0}$), so $\mathbf{x}(\theta) = \mathbf{x}^{(0)} + \theta\mathbf{d} \ge \mathbf{0}$ for all $\theta \ge 0$.
2. **Null-space invariance**: Multiplying $\mathbf{d}$ by the constraint matrix $\mathbf{A}$ gives:
   $$\mathbf{A}\mathbf{d} = \mathbf{B}\mathbf{d}_B + \mathbf{a}_k (1) = \mathbf{B}(-\mathbf{B}^{-1}\mathbf{a}_k) + \mathbf{a}_k = -\mathbf{a}_k + \mathbf{a}_k = \mathbf{0}$$
   Therefore, $\mathbf{A}\mathbf{x}(\theta) = \mathbf{A}\mathbf{x}^{(0)} + \theta \mathbf{A}\mathbf{d} = \mathbf{b} + \mathbf{0} = \mathbf{b}$ for all $\theta \ge 0$. Thus $\mathbf{d}$ is an **extreme ray** of the recession cone $\mathcal{R} = \{\mathbf{d} \ge \mathbf{0} : \mathbf{A}\mathbf{d} = \mathbf{0}\}$, and $\mathbf{x}(\theta) \in \mathcal{F}$ is feasible for arbitrarily large $\theta \to +\infty$.
3. **Strict objective growth**: Evaluating the objective function along the ray yields:
   $$\mathbf{c}^T \mathbf{x}(\theta) = \mathbf{c}^T\mathbf{x}^{(0)} + \theta (\mathbf{c}_B^T \mathbf{d}_B + c_k) = Z_0 + \theta (c_k - \mathbf{c}_B^T\mathbf{y}_k) = Z_0 + \theta (c_k - z_k) \xrightarrow{\theta \to +\infty} +\infty$$
   since $c_k - z_k > 0$. Thus $z_k - c_k < 0$ with $\mathbf{y}_k \le \mathbf{0}$ is a necessary and sufficient certificate that the LP is **unbounded above** on $\mathcal{F}$.

### Characterization of Alternative Optimal Solutions

Now suppose the Simplex Algorithm reaches an optimal tableau where $z_j - c_j \ge 0$ for all $j \in N$, achieving the finite maximum $Z^* = Z_0$. Recall the Simplex Objective Identity:

$$Z(\mathbf{x}) = Z^* - \sum_{j \in N} (z_j - c_j) x_j$$

If $z_j - c_j > 0$ for **every** non-basic variable $j \in N$, then any feasible point $\mathbf{x} \in \mathcal{F}$ distinct from the current BFS must have $x_j > 0$ for at least one $j \in N$ (since $\mathbf{B}$ is nonsingular, $\mathbf{x}_N = \mathbf{0}$ uniquely forces $\mathbf{x}_B = \bar{\mathbf{b}}$), which strictly reduces $Z(\mathbf{x}) < Z^*$. Hence, **strict positivity $z_j - c_j > 0$ for all non-basic variables $j \in N$ is a sufficient condition for the current optimal BFS to be the unique global optimal solution**!

Conversely, suppose that in the optimal tableau ($z_j - c_j \ge 0$ for all $j \in N$), there exists at least one **non-basic variable** $x_k$ ($k \in N$) whose net evaluation is zero:

$$z_k - c_k = 0 \qquad (k \in N)$$

Increasing $x_k$ from $0$ to $\theta > 0$ changes the objective value by $\Delta Z = -\theta(z_k - c_k) = 0$, leaving $Z(\theta) = Z^*$ completely unchanged!
- If at least one entry $y_{ik} > 0$ (and $\bar{b}_i > 0$), performing a standard Simplex pivot to bring $x_k$ into the basis yields a second, distinct **optimal Basic Feasible Solution** $\mathbf{x}^{(2)} \ne \mathbf{x}^{(1)}$ with $Z(\mathbf{x}^{(2)}) = Z^*$. Every convex combination $\mathbf{x}(\lambda) = \lambda \mathbf{x}^{(1)} + (1-\lambda)\mathbf{x}^{(2)}$ for $\lambda \in [0, 1]$ is then an optimal solution.
- If $y_{ik} \le 0$ for all $i = 1, \dots, m$, then the ray $\mathbf{x}(\theta) = \mathbf{x}^{(1)} + \theta\mathbf{d}$ ($\theta \ge 0$) is an **unbounded optimal ray** along which $Z(\mathbf{x}(\theta)) = Z^*$ remains constant out to infinity.

## 2.4 Artificial Variable Architectures I: Charnes' Big-M Penalty Method

When a Linear Programming Problem consists exclusively of less-than-or-equal-to ($\le$) constraints with non-negative right-hand sides $b_i \ge 0$, introducing $m$ slack variables $s_1, \dots, s_m \ge 0$ immediately furnishes an $m \times m$ identity submatrix $\mathbf{B} = \mathbf{I}_m$ within $\mathbf{A}$ and an obvious initial Basic Feasible Solution at the origin ($\mathbf{x} = \mathbf{0}, \mathbf{s} = \mathbf{b} \ge \mathbf{0}$). However, whenever the standard-form model contains **greater-than-or-equal-to ($\ge$) constraints** (which become $\sum_{j=1}^n a_{ij}x_j - e_i = b_i$ with coefficient $-1$ on surplus $e_i$) or **strict equality ($=$) constraints** ($\sum_{j=1}^n a_{ij}x_j = b_i$), setting the structural variables $\mathbf{x} = \mathbf{0}$ yields $e_i = -b_i < 0$ (infeasible) or leaves no basic variable at all for the equality row.

To construct a starting $m \times m$ identity basis matrix $\mathbf{I}_m$ without guessing an initial feasible vertex, we augment each constraint $i \in M_2 \cup M_3$ that lacks a positive unit slack column by adding a non-negative **artificial variable** $A_i \ge 0$:

$$\sum_{j=1}^n a_{ij} x_j - e_i + A_i = b_i \quad (\text{for } \ge \text{ rows}), \qquad \sum_{j=1}^n a_{ij} x_j + A_i = b_i \quad (\text{for } = \text{ rows})$$

Unlike slack and surplus variables—which have genuine physical interpretations as unused capacity or excess production—artificial variables $A_i$ are purely mathematical scaffolding. A solution of the augmented system is feasible for the original Linear Program **if and only if every artificial variable equals zero ($A_i = 0$ for all $i$)**.

### Charnes' Big-M Method (Method of Penalties)

Developed by Abraham Charnes (1952), the **Big-M Penalty Method** drives artificial variables out of the basis in a single unified Simplex run by assigning an overwhelmingly large penalty coefficient $M \gg \max_{i,j} \{|c_j|, |a_{ij}|, |b_i|\}$ ($M \to +\infty$) to every artificial variable in the objective function:
- For a **Maximization** problem: assign objective coefficient $-M$ to each $A_i$:
  $$\text{Maximize } Z_M = \sum_{j=1}^n c_j x_j - M \sum_{i=1}^p A_i$$
- For a **Minimization** problem: assign objective coefficient $+M$ to each $A_i$:
  $$\text{Minimize } W_M = \sum_{j=1}^n c_j x_j + M \sum_{i=1}^p A_i$$

Because $M$ is treated symbolically as an arbitrarily large positive constant, each net evaluation entry $z_j - c_j$ splits into a linear polynomial in $M$:

$$z_j - c_j = \alpha_j + \beta_j M$$

During Simplex iterations, whenever two columns are compared or tested for optimality, the coefficient $\beta_j$ of $M$ dominates completely over the finite part $\alpha_j$: $\alpha_j + \beta_j M < 0$ if and only if $\beta_j < 0$, or ($\beta_j = 0$ and $\alpha_j < 0$). Once an artificial variable $A_i$ leaves the basis, it need never be considered for re-entry and its column can be dropped immediately.

### Exhaustive Termination Diagnostics of the Big-M Method

When the Big-M Simplex tableau satisfies the optimality condition ($z_j - c_j \ge 0$ for all columns in maximization):
1. **Feasible Optimal Solution**: If all artificial variables have left the basis (or any artificial variable remaining in the basis has value $A_i^* = 0$ at a degenerate vertex), the resulting structural vector $\mathbf{x}^*$ is the true optimal BFS of the original LP.
2. **Infeasibility Certificate ($\mathcal{F} = \emptyset$)**: If the optimality criterion $z_j - c_j \ge 0$ is satisfied for all columns, yet **at least one artificial variable remains in the basis at a strictly positive level ($A_i^* > 0$)**, then the original Linear Programming Problem is **infeasible** ($\mathcal{F} = \emptyset$); no vector $\mathbf{x} \ge \mathbf{0}$ can ever drive $\sum A_i$ to zero.
3. **Pseudo-Unboundedness vs True Unboundedness**: If an unbounded column ($\mathbf{y}_k \le \mathbf{0}$ with $z_k - c_k < 0$) is encountered while artificial variables are still positive in the basis, the original problem may actually be infeasible rather than unbounded; this numerical and logical drawback motivates Dantzig's Two-Phase Method.

## 2.5 Artificial Variable Architectures II: Dantzig's Two-Phase Simplex Algorithm

In digital floating-point computation on modern computers, Charnes' Big-M method suffers from a severe numerical stability flaw: choosing $M$ too small fails to expel artificial variables from the basis, whereas choosing $M$ excessively large (e.g., $M = 10^{12}$ when structural coefficients $c_j \sim 10^0$) causes catastrophic **floating-point round-off cancellation** when adding $c_j - M y_{ij}$, swamping the true objective coefficients $c_j$ below machine epsilon ($\epsilon_{\text{mach}} \approx 2.22 \times 10^{-16}$). To eliminate arbitrary penalty constants entirely, George Dantzig, Alex Orden, and Philip Wolfe introduced the **Two-Phase Simplex Method**, which decouples feasibility discovery (Phase I) from objective optimization (Phase II).

### Phase I: Minimizing the Sum of Artificial Variables

In **Phase I**, we temporarily ignore the original objective function $Z = \mathbf{c}^T\mathbf{x}$ and replace it with an auxiliary Phase I linear program whose sole purpose is to minimize the sum of all $p$ artificial variables (or equivalently, maximize $Z_{\text{I}} = -\sum_{i=1}^p A_i$):

$$\text{Maximize } Z_{\text{I}} = -\sum_{i=1}^p A_i \quad \left(\text{equivalently, Minimize } W_{\text{I}} = \sum_{i=1}^p A_i\right)$$

subject to the augmented constraint system $\mathbf{A}\mathbf{x} + \mathbf{E}\mathbf{s} + \mathbf{A}_{\text{art}}\mathbf{A} = \mathbf{b}, \quad \mathbf{x}, \mathbf{s}, \mathbf{A} \ge \mathbf{0}$.

Notice three remarkable mathematical properties of the Phase I linear program:
1. **Guaranteed Initial BFS**: Setting $\mathbf{x} = \mathbf{0}$, slack variables $s_i = b_i \ge 0$, surplus variables $e_i = 0$, and artificial variables $A_i = b_i \ge 0$ provides an immediate, exact initial Basic Feasible Solution for Phase I.
2. **Guaranteed Boundedness**: Because every artificial variable satisfies $A_i \ge 0$, their sum is bounded below by zero ($W_{\text{I}} = \sum_{i=1}^p A_i \ge 0$, or $Z_{\text{I}} \le 0$). Therefore, Phase I can **never** be unbounded; assuming an anti-cycling rule, the Simplex Algorithm applied to Phase I is mathematically guaranteed to terminate at a finite optimal objective value $W_{\text{I}}^* \ge 0$.
3. **Exact Feasibility Dichotomy**:
   - **Case A ($W_{\text{I}}^* > 0$, i.e., $Z_{\text{I}}^* < 0$)**: If the minimum possible sum of artificial variables is strictly positive, then no vector in the non-negative orthant satisfies $\mathbf{A}\mathbf{x} = \mathbf{b}$ with $\mathbf{A} = \mathbf{0}$. The original Linear Programming Problem is **strictly infeasible** ($\mathcal{F} = \emptyset$), and computation terminates immediately at the end of Phase I.
   - **Case B ($W_{\text{I}}^* = 0$, i.e., $Z_{\text{I}}^* = 0$)**: Since $A_i \ge 0$ for all $i$ and $\sum_{i=1}^p A_i^* = 0$, every single artificial variable has been driven to zero ($A_1^* = \dots = A_p^* = 0$)! The resulting structural and slack/surplus vector $(\mathbf{x}^*, \mathbf{s}^*)$ is a genuine **Basic Feasible Solution** of the original Linear Program, initiating Phase II.

### Transition from Phase I to Phase II and Redundant Equation Detection

When Phase I terminates with $W_{\text{I}}^* = 0$, two subcases govern the transition to **Phase II**:
- **Subcase B1 (No artificial variables remain in the basis)**: We delete all artificial columns completely, restore the original objective coefficients $c_j$ into $\mathbf{c}_B$ and $\mathbf{c}_N$, recompute the Phase II net evaluation row $z_j - c_j = \mathbf{c}_B^T \mathbf{y}_j - c_j$ for the current basis, and proceed with standard Simplex iterations to optimize the original objective $Z = \mathbf{c}^T\mathbf{x}$.
- **Subcase B2 (One or more artificial variables remain in the basis at degenerate zero level, $A_r^* = 0$)**: Suppose artificial variable $A_r = 0$ is still basic in row $r$ at the end of Phase I.
  1. If row $r$ contains at least one non-zero entry $y_{rj} \ne 0$ in a non-artificial structural or slack/surplus column $j$, we perform a **degenerate zero-step pivot** on $y_{rj} \ne 0$ (even if $y_{rj} < 0$, since $\bar{b}_r = 0$, the step size is $\theta^* = 0 / y_{rj} = 0$, preserving feasibility $\bar{\mathbf{b}} \ge \mathbf{0}$) to exchange $A_r$ out of the basis for $x_j$.
  2. If $y_{rj} = 0$ for **every** non-artificial column $j$, then row $r$ of the current tableau reads $0 x_1 + \dots + 0 x_n + 1 A_r = 0$. This proves algebraically that the $r$-th original constraint is a **linearly dependent redundant equation** ($\text{rank}(\mathbf{A}) < m$), so the entire $r$-th row and $A_r$ column can be deleted from the tableau before beginning Phase II!

## 2.6 Primal Degeneracy, Cycling Phenomena, Lexicographic Perturbation, and Bland's Anti-Cycling Rule

In the proof of finite termination of the Simplex Algorithm, a crucial step assumes that every Simplex pivot achieves a strict increase in the objective function ($Z_{\text{new}} = Z_0 + \theta^*(c_k - z_k) > Z_0$). Because there are only finitely many bases $\binom{n}{m}$, if $Z$ strictly increases at every iteration, no basis can ever be visited twice, guaranteeing termination in at most $\binom{n}{m}$ pivots. However, this strict monotonicity relies on $\theta^* = \min_{i: y_{ik}>0} (\bar{b}_i / y_{ik}) > 0$, which holds automatically when the current BFS is **non-degenerate** ($\bar{b}_i > 0$ for all $i=1,\dots,m$).

### Primal Degeneracy, Tie-Induced Degeneracy, and Cycling

A Basic Feasible Solution is **degenerate** if one or more basic variables equal zero ($\bar{b}_i = 0$ for at least one $i \in \{1, \dots, m\}$). Degeneracy arises in two ways:
1. In the initial tableau, if a right-hand side $b_i = 0$.
2. During any Simplex iteration, if **two or more basic variables tie in the Minimum Ratio Test**:
   $$\theta^* = \frac{\bar{b}_{r_1}}{y_{r_1, k}} = \frac{\bar{b}_{r_2}}{y_{r_2, k}}$$
   When $x_{B(r_1)}$ is chosen to leave the basis, the remaining tied basic variable $x_{B(r_2)}$ stays in the basis but its updated right-hand side becomes $\bar{b}_{r_2}^{\text{new}} = \bar{b}_{r_2} - \theta^* y_{r_2, k} = 0$, creating a **degenerate BFS** in the next tableau!

At a degenerate BFS where $\bar{b}_r = 0$ and $y_{rk} > 0$, the Minimum Ratio Test yields step size $\theta^* = 0 / y_{rk} = 0$. Performing the pivot changes the algebraic basis matrix $\mathbf{B}$ to $\mathbf{B}_{\text{new}}$, but the geometric point $\mathbf{x}$ does not move at all ($\Delta \mathbf{x} = \mathbf{0}$) and the objective function stalls ($\Delta Z = \theta^*(c_k - z_k) = 0$). A sequence of consecutive zero-step pivots ($\theta^* = 0$) at the same geometric vertex is called **stalling**. Worse yet, as first demonstrated by E. M. L. Beale (1955) with a 3-constraint, 7-variable counterexample, it is possible for a sequence of degenerate pivots ($\theta^* = 0$) to repeat a closed loop of bases $\mathbf{B}^{(1)} \to \mathbf{B}^{(2)} \to \dots \to \mathbf{B}^{(L)} \to \mathbf{B}^{(1)}$ indefinitely—a phenomenon known as **cycling**—preventing the Simplex Algorithm from ever terminating!

### Resolution 1: Charnes' $\varepsilon$-Perturbation and the Lexicographic Method

To eliminate degeneracy geometrically, Abraham Charnes (1952) and Dantzig, Orden, and Wolfe (1955) perturbed the right-hand-side vector $\mathbf{b}$ by adding powers of an infinitesimally small positive scalar $0 < \varepsilon \ll 1$ along the columns of the initial basis $\mathbf{B}_0 = \mathbf{I}_m$:

$$\mathbf{b}(\varepsilon) = \mathbf{b} + \sum_{k=1}^m \varepsilon^k \mathbf{e}_k = \begin{pmatrix} b_1 + \varepsilon \\ b_2 + \varepsilon^2 \\ \vdots \\ b_m + \varepsilon^m \end{pmatrix}$$

Because $1 \gg \varepsilon \gg \varepsilon^2 \gg \dots \gg \varepsilon^m > 0$ are algebraically independent over the rational numbers, no basic variable can ever equal zero and no two ratios can ever tie! In practice, $\varepsilon$ is never assigned a numerical value; instead, each row $i$ is represented by the $(m+1)$-dimensional **lexicographic vector** $\mathbf{r}_i = (\bar{b}_i, y_{i1}, y_{i2}, \dots, y_{im})$. When comparing candidate leaving rows $i$ with $y_{ik} > 0$, we divide the entire row vector $\mathbf{r}_i$ by $y_{ik}$ and select the unique row $r$ whose scaled vector $\frac{1}{y_{rk}}(\bar{b}_r, y_{r1}, \dots, y_{rm})$ is **lexicographically smallest** (comparing the first component $\bar{b}_i/y_{ik}$, then on a tie comparing $y_{i1}/y_{ik}$, then $y_{i2}/y_{ik}$, and so on). Because the matrix $[\mathbf{y}_1, \dots, \mathbf{y}_m] = \mathbf{B}^{-1}$ has full rank $m$, no two rows can be proportional, so the lexicographic tie-break is always **unique** and strictly increases the objective rows lexicographically, making cycling mathematically impossible!

### Resolution 2: Bland's Smallest-Subscript Anti-Cycling Rule (1977)

Robert G. Bland (1977) proved a remarkably simple combinatorial anti-cycling theorem that requires zero extra tableau storage:

#### Theorem 2.2 (Bland's Anti-Cycling Theorem):
Order all variables with fixed indices $x_1, x_2, \dots, x_n$. The Simplex Algorithm is guaranteed never to cycle (and therefore terminates in a finite number of pivots on any LP) if both entering and leaving ties are broken by choosing the **smallest subscript**:
1. **Entering Rule**: Among all non-basic variables with $z_j - c_j < 0$, choose the entering variable $x_k$ with the **smallest index $k$**: $k = \min \{ j \in N : z_j - c_j < 0 \}$.
2. **Leaving Rule**: Among all basic variables $x_{B(i)}$ that tie for the minimum ratio $\theta^* = \min_{i: y_{ik}>0} (\bar{b}_i / y_{ik})$, choose the leaving basic variable $x_{B(r)}$ with the **smallest variable subscript $B(r)$** (not the smallest row number $i$, but the smallest original variable index $B(r)$!).

### Steepest-Edge and Devex Pricing Rules against Stalling

While Bland's rule guarantees finite termination, its strict adherence to index order often selects entering variables with tiny objective improvements, causing long sequences of slow pivots. In modern statistical and commercial optimization solvers, stalling and poor pivot trajectories are mitigated by **Steepest-Edge Pricing** (Goldfarb and Reid, 1977) and Paula Harris's **Devex Pricing** (1973). Rather than maximizing the coordinate derivative $c_j - z_j = \frac{\partial Z}{\partial x_j}$ (which depends on arbitrary column scaling), Steepest-Edge Pricing normalizes the reduced cost by the Euclidean norm of the actual $n$-dimensional edge displacement vector $\boldsymbol{\eta}^{(j)} = (-\mathbf{y}_j^T, \mathbf{e}_j^T)^T$, selecting the non-basic column $k \in N$ that maximizes the true directional derivative in $\mathbb{R}^n$:

$$k = \arg\max_{j \in N: c_j - z_j > 0} \frac{c_j - z_j}{\|\boldsymbol{\eta}^{(j)}\|_2} = \arg\max_{j \in N: c_j - z_j > 0} \frac{c_j - z_j}{\sqrt{1 + \sum_{i=1}^m y_{ij}^2}}$$

Because edge norms $\|\boldsymbol{\eta}^{(j)}\|_2^2 = 1 + \|\mathbf{y}_j\|_2^2$ can be updated recursively from iteration to iteration without recomputing all columns $\mathbf{y}_j$, Steepest-Edge Pricing dramatically reduces both degenerate stalling and total iteration counts across large-scale linear programs.

### The Revised Simplex Method in Matrix Form and Computational Complexity

In large-scale industrial and statistical optimization problems, a standard LP may involve $m = 10,000$ constraints and $n = 500,000$ variables. In the standard tableau Simplex method, every pivot updates all $m \times n$ entries $y_{ij}$ of the non-basic columns $\mathbf{B}^{-1}\mathbf{N}$ at a cost of $\mathcal{O}(mn)$ arithmetic operations per iteration, even though **only a single column $\mathbf{y}_k = \mathbf{B}^{-1}\mathbf{a}_k$** (the entering column) is actually needed to perform the Minimum Ratio Test! Furthermore, real-world constraint matrices $\mathbf{A}$ are typically ultra-sparse (with fewer than $0.1\%$ non-zero entries), whereas standard tableau pivoting rapidly destroys sparsity through dense fill-in.

### Architecture of the Revised Simplex Method

Developed by Dantzig and William Orchard-Hays (1953), the **Revised Simplex Method** computes and stores only the current basis inverse $\mathbf{B}^{-1} \in \mathbb{R}^{m \times m}$ (or, in modern numerical linear algebra, a sparse $LU$ factorization of $\mathbf{B}$), the basic variable values $\bar{\mathbf{b}} = \mathbf{B}^{-1}\mathbf{b} \in \mathbb{R}^m$, and the **simplex multiplier (dual price) vector** $\mathbf{w}^T \in \mathbb{R}^{1 \times m}$:

$$\mathbf{w}^T = \mathbf{c}_B^T \mathbf{B}^{-1} \iff \mathbf{B}^T \mathbf{w} = \mathbf{c}_B$$

Each iteration of the Revised Simplex Method executes four compact matrix-vector steps:
1. **Compute Simplex Multipliers (BTRAN — Backward Transformation)**: Solve the $m \times m$ transposed system $\mathbf{B}^T \mathbf{w} = \mathbf{c}_B$ for the dual multiplier vector $\mathbf{w} = (\mathbf{B}^{-1})^T \mathbf{c}_B$.
2. **Price Non-Basic Columns (Entering Selection)**: For non-basic indices $j \in N$, compute the reduced cost directly from the original sparse column $\mathbf{a}_j$:
   $$z_j - c_j = \mathbf{w}^T \mathbf{a}_j - c_j$$
   If $z_j - c_j \ge 0$ for all $j \in N$, stop; the current BFS $\mathbf{x}_B = \bar{\mathbf{b}}$ is optimal! Otherwise, select an entering index $k \in N$ with $z_k - c_k < 0$.
3. **FTRAN (Forward Transformation & Minimum Ratio Test)**: Compute **only** the entering updated column $\mathbf{y}_k$ by solving $\mathbf{B}\mathbf{y}_k = \mathbf{a}_k$ (i.e., $\mathbf{y}_k = \mathbf{B}^{-1}\mathbf{a}_k$). If $\mathbf{y}_k \le \mathbf{0}$, stop (the LP is unbounded). Otherwise, compute the Minimum Ratio Test $\theta^* = \min_{i: y_{ik}>0} (\bar{b}_i / y_{ik}) = \bar{b}_r / y_{rk}$ to identify the leaving basic variable $x_{B(r)}$ in position $r$.
4. **Basis Inverse Update via Product Form of the Inverse (Eta Matrix)**: Replace column $r$ of $\mathbf{B}$ by $\mathbf{a}_k$. Because $\mathbf{B}_{\text{new}}$ differs from $\mathbf{B}$ in only the $r$-th column, $\mathbf{B}_{\text{new}} = \mathbf{B} \mathbf{E}_r^{-1}$, so the new basis inverse is obtained by premultiplying $\mathbf{B}^{-1}$ by an elementary **Eta matrix** $\mathbf{E}_r \in \mathbb{R}^{m \times m}$ that differs from the identity matrix $\mathbf{I}_m$ solely in column $r$:
   $$\mathbf{B}_{\text{new}}^{-1} = \mathbf{E}_r \mathbf{B}^{-1}, \qquad \text{where column } r \text{ of } \mathbf{E}_r \text{ is } \boldsymbol{\eta}_r = \begin{pmatrix} -y_{1k} / y_{rk} \\ \vdots \\ +1 / y_{rk} \\ \vdots \\ -y_{mk} / y_{rk} \end{pmatrix} \begin{matrix} \\ \\ \leftarrow \text{row } r \\ \\ \\ \end{matrix}$$
   The compact $(m+1) \times (m+1)$ Revised Simplex array tracks $\begin{pmatrix} 1 & \mathbf{w}^T & Z_0 \\ \mathbf{0} & \mathbf{B}^{-1} & \bar{\mathbf{b}} \end{pmatrix}$ and updates via a single Gauss–Jordan pivot on the appended column $\begin{pmatrix} z_k - c_k \\ \mathbf{y}_k \end{pmatrix}$.

### Computational Complexity: The Klee–Minty Cube vs. Polynomial Interior-Point Algorithms

In practical applications, the Simplex Method typically terminates in $1.5m$ to $3m$ iterations—linear in the number of constraints! However, in 1972 Victor Klee and George J. Minty settled a major open problem in theoretical computer science by constructing the **Klee–Minty Cube**, a perturbed $n$-dimensional hypercube defined for $0 < \varepsilon < 1/2$ by:

$$\text{Maximize } \sum_{j=1}^n 10^{n-j} x_j \quad \text{subject to} \quad 2 \sum_{j=1}^{i-1} 10^{i-j} x_j + x_i \le 100^{i-1} \quad (i = 1, \dots, n), \quad \mathbf{x} \ge \mathbf{0}$$

Klee and Minty proved that on this deformed $n$-cube with $n$ variables and $n$ constraints, the Simplex Algorithm under Dantzig's most-negative reduced-cost rule visits **every single one of the $2^n$ vertices**, requiring $2^n - 1$ pivots! Thus, the **worst-case time complexity of the Simplex Algorithm is exponential, $\mathcal{O}(2^n)$**. Why, then, is Simplex so fast in practice? In 2001, Daniel Spielman and Shang-Hua Teng introduced **Smoothed Analysis**, proving that under tiny Gaussian random perturbations $\tilde{\mathbf{A}} = \mathbf{A} + \mathbf{G}$ of variance $\sigma^2$, the expected number of Simplex pivots is strictly **polynomial in $n, m,$ and $1/\sigma$**, explaining why pathological Klee–Minty geometries vanish under real-world statistical noise. Furthermore, Linear Programming was proven to belong to the complexity class $\mathbf{P}$ (deterministic polynomial time) through Leonid Khachiyan's **Ellipsoid Method** (1979) and Narendra Karmarkar's **Projective Interior-Point Method** (1984), which traverse the interior of the polyhedron $\mathcal{F}$ along a central logarithmic-barrier path $\max \mathbf{c}^T\mathbf{x} + \mu \sum_{j=1}^n \ln(x_j)$ in $\mathcal{O}(n^{3.5} L)$ bit operations.

### Bounded-Variable Simplex Architecture and Sparse Bartels–Golub LU Updates

In statistical and industrial linear programs—such as stratified survey sample allocation where sample sizes $n_h$ must satisfy $l_h \le n_h \le N_h$, or financial portfolio optimization with asset weight caps $0 \le x_j \le u_j$—almost every decision variable is subject to explicit **box constraints** (lower and upper bounds):

$$\text{Maximize } Z = \mathbf{c}^T\mathbf{x} \quad \text{subject to} \quad \mathbf{A}\mathbf{x} = \mathbf{b}, \quad \mathbf{l} \le \mathbf{x} \le \mathbf{u}$$

If one naively treats the $n$ upper-bound inequalities $x_j \le u_j$ as ordinary structural rows by adding $n$ slack variables $x_j + s_j' = u_j$, the constraint matrix dimension explodes from $m \times n$ to $(m+n) \times 2n$, and the basis matrix $\mathbf{B}$ balloons from $m \times m$ to $(m+n) \times (m+n)$. Because $n$ is frequently an order of magnitude larger than $m$, expanding the basis size to $m+n$ would catastrophically degrade computational speed.

### The Bounded-Variable (Upper-Bound) Simplex Method

Introduced by George Dantzig (1955), the **Bounded-Variable Simplex Algorithm** handles lower and upper bounds $\mathbf{0} \le \mathbf{x} \le \mathbf{u}$ implicitly while keeping the working basis matrix $\mathbf{B}$ at its compact $m \times m$ structural dimension! In this generalized architecture, the $n$ variables are partitioned into three disjoint sets:
1. **$m$ Basic Variables ($\mathbf{x}_B$)**: Taking continuous values strictly or weakly within their intervals, $0 \le x_{B(i)} \le u_{B(i)}$, determined uniquely by the $m$ equations $\mathbf{B}\mathbf{x}_B = \mathbf{b} - \mathbf{N}_L \mathbf{0} - \mathbf{N}_U \mathbf{u}_U$.
2. **Non-Basic Variables at Lower Bound ($N_L$)**: Fixed at $x_j = 0$. A variable $j \in N_L$ can only **increase** from $0$, so it is eligible to enter the basis when its reduced profit $\bar{c}_j = c_j - z_j > 0$ ($z_j - c_j < 0$).
3. **Non-Basic Variables at Upper Bound ($N_U$)**: Fixed at their upper capacity $x_j = u_j$ (or replaced via the complementation substitution $x_j = u_j - \tilde{x}_j$ with $\tilde{x}_j = 0$). A variable $j \in N_U$ can only **decrease** from $u_j$, so it is eligible to enter the basis when decreasing $x_j$ increases $Z$, which occurs when $\bar{c}_j = c_j - z_j < 0$ ($z_j - c_j > 0$)!

When an entering variable $x_k \in N_L$ increases from $0$ by step $\theta \ge 0$, the basic variables vary as $x_{B(i)}(\theta) = \bar{b}_i - y_{ik}\theta$. Now, feasibility requires $0 \le x_{B(i)}(\theta) \le u_{B(i)}$ and $0 \le \theta \le u_k$. Thus, the **Generalized Minimum Ratio Test** computes the minimum of three competing blocking thresholds:
- **Threshold 1 (Basic variable hits lower bound $0$)**: For rows with $y_{ik} > 0$, $\theta_1 = \min_{i: y_{ik}>0} \frac{\bar{b}_i}{y_{ik}}$.
- **Threshold 2 (Basic variable hits upper bound $u_{B(i)}$)**: For rows with $y_{ik} < 0$, $x_{B(i)}(\theta) = \bar{b}_i + |y_{ik}|\theta$ increases toward $u_{B(i)}$, yielding $\theta_2 = \min_{i: y_{ik}<0} \frac{u_{B(i)} - \bar{b}_i}{-y_{ik}}$.
- **Threshold 3 (Entering variable hits its own upper bound $u_k$)**: $\theta_3 = u_k$.

The maximum feasible step is $\theta^* = \min\{\theta_1, \theta_2, \theta_3\}$. Remarkably, if $\theta^* = \theta_3 = u_k$, the entering variable $x_k$ simply flips from $N_L$ ($x_k = 0$) to $N_U$ ($x_k = u_k$) **without any basis matrix pivot at all**, updating $\bar{\mathbf{b}} \leftarrow \bar{\mathbf{b}} - u_k \mathbf{y}_k$ in $\mathcal{O}(m)$ time!

### Bartels–Golub and Forrest–Tomlin Sparse LU Updates

Finally, in production Revised Simplex implementations (such as CPLEX, Gurobi, and HiGHS), accumulating hundreds of elementary Eta matrices $\mathbf{B}_t^{-1} = \mathbf{E}_t \mathbf{E}_{t-1} \cdots \mathbf{E}_1 \mathbf{B}_0^{-1}$ causes numerical instability when a pivot element $y_{rk}$ is small, and slows down FTRAN/BTRAN solves. Following Richard Bartels and Gene Golub (1969) and John Forrest and John Tomlin (1972), modern solvers maintain a sparse **permuted triangular factorization** $\mathbf{P}\mathbf{B}\mathbf{Q} = \mathbf{L}\mathbf{U}$, where replacing a column of $\mathbf{B}$ produces a ** rank-one spike** in $\mathbf{U}$ that is restored to upper-triangular form via sparse row/column permutations and threshold partial pivoting, periodically refactoring $\mathbf{B} = \mathbf{L}\mathbf{U}$ from scratch every $50$ to $100$ iterations to purge accumulated floating-point round-off errors.

## Worked Questions and Solutions

### Question 1: Complete Tabular Simplex Solution of a Three-Variable Resource Allocation Problem

A statistical computing center allocates processor hours, high-speed memory bandwidth, and storage I/O channels across three classes of analytical workloads: Bayesian MCMC simulation ($x_1$), bootstrap resampling ($x_2$), and high-dimensional penalized regression ($x_3$). The net scientific utility (in $10^3$ credits) and resource constraints are formulated as the Linear Programming Problem:

$$\text{Maximize } Z = 3x_1 + 5x_2 + 4x_3$$

subject to:

$$\begin{aligned}
2x_1 + 3x_2 &\le 8 \quad (\text{Processor Cluster Capacity}) \\
2x_2 + 5x_3 &\le 10 \quad (\text{Memory Bandwidth Limit}) \\
3x_1 + 2x_2 + 4x_3 &\le 15 \quad (\text{Storage I/O Channel Limit}) \\
x_1, x_2, x_3 &\ge 0
\end{aligned}$$

1. Introduce slack variables $s_1, s_2, s_3 \ge 0$ and construct the initial Simplex tableau at the origin BFS.
2. Execute the Simplex Algorithm step-by-step using Dantzig's entering rule and the Minimum Ratio Test, displaying the complete HTML Simplex tableau at each iteration.
3. Verify the global optimality of the final tableau and state the optimal workload vector $(x_1^*, x_2^*, x_3^*)$, slack vector $(s_1^*, s_2^*, s_3^*)$, and maximum utility $Z^*$.

### Solution, step 1: Initial Simplex Tableau (Iteration 0) and First Pivot Selection

Adding slack variables $s_1, s_2, s_3 \ge 0$ with zero objective coefficients gives the standard system with initial basis $B_0 = \{s_1, s_2, s_3\}$ and $\mathbf{x}_B^{(0)} = (8, 10, 15)^T, Z_0 = 0$:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Basic Var</th><th>$c_B$</th><th>$x_1$ ($3$)</th><th>$x_2$ ($5$)</th><th>$x_3$ ($4$)</th><th>$s_1$ ($0$)</th><th>$s_2$ ($0$)</th><th>$s_3$ ($0$)</th><th>RHS ($\bar{b}_i$)</th><th>Ratio $\theta_i = \bar{b}_i / y_{i2}$</th></tr></thead><tbody><tr><td>$s_1$</td><td>$0$</td><td>$2$</td><td>$\mathbf{3}^*$</td><td>$0$</td><td>$1$</td><td>$0$</td><td>$0$</td><td>$8$</td><td>$8/3 \approx 2.667$ (Min $\to$ Leave)</td></tr><tr><td>$s_2$</td><td>$0$</td><td>$0$</td><td>$2$</td><td>$5$</td><td>$0$</td><td>$1$</td><td>$0$</td><td>$10$</td><td>$10/2 = 5.000$</td></tr><tr><td>$s_3$</td><td>$0$</td><td>$3$</td><td>$2$</td><td>$4$</td><td>$0$</td><td>$0$</td><td>$1$</td><td>$15$</td><td>$15/2 = 7.500$</td></tr><tr><td>$z_j - c_j$</td><td>—</td><td>$-3$</td><td>$\mathbf{-5}$ (Enter)</td><td>$-4$</td><td>$0$</td><td>$0$</td><td>$0$</td><td>$Z_0 = 0$</td><td>$\theta^* = 8/3$</td></tr></tbody></table></div>

- **Entering Variable**: The most negative $z_j - c_j$ is $z_2 - c_2 = -5 < 0$, so $x_2$ enters the basis.
- **Leaving Variable**: The Minimum Ratio Test gives $\theta^* = \min \{8/3, 10/2, 15/2\} = 8/3$ in Row 1, so $s_1$ leaves the basis and the pivot element is $y_{12} = 3$.

### Solution, step 2: Iterations 1 and 2: Gauss-Jordan Pivoting

**Iteration 1**: Divide Row 1 by $3$, then apply $R_2 \leftarrow R_2 - 2R_1^{\text{new}}$, $R_3 \leftarrow R_3 - 2R_1^{\text{new}}$, and $R_z \leftarrow R_z + 5R_1^{\text{new}}$:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Basic Var</th><th>$c_B$</th><th>$x_1$ ($3$)</th><th>$x_2$ ($5$)</th><th>$x_3$ ($4$)</th><th>$s_1$ ($0$)</th><th>$s_2$ ($0$)</th><th>$s_3$ ($0$)</th><th>RHS ($\bar{b}_i$)</th><th>Ratio $\theta_i = \bar{b}_i / y_{i3}$</th></tr></thead><tbody><tr><td>$x_2$</td><td>$5$</td><td>$2/3$</td><td>$1$</td><td>$0$</td><td>$1/3$</td><td>$0$</td><td>$0$</td><td>$8/3$</td><td>— ($y_{13} = 0$)</td></tr><tr><td>$s_2$</td><td>$0$</td><td>$-4/3$</td><td>$0$</td><td>$\mathbf{5}^*$</td><td>$-2/3$</td><td>$1$</td><td>$0$</td><td>$14/3$</td><td>$(14/3)/5 = 14/15 \approx 0.933$ (Min $\to$ Leave)</td></tr><tr><td>$s_3$</td><td>$0$</td><td>$5/3$</td><td>$0$</td><td>$4$</td><td>$-2/3$</td><td>$0$</td><td>$1$</td><td>$29/3$</td><td>$(29/3)/4 = 29/12 \approx 2.417$</td></tr><tr><td>$z_j - c_j$</td><td>—</td><td>$1/3$</td><td>$0$</td><td>$\mathbf{-4}$ (Enter)</td><td>$5/3$</td><td>$0$</td><td>$0$</td><td>$Z_1 = 40/3$</td><td>$\theta^* = 14/15$</td></tr></tbody></table></div>

Here $z_3 - c_3 = -4 < 0$, so $x_3$ enters and $s_2$ leaves ($\theta^* = 14/15$, pivot $y_{23} = 5$).

**Iteration 2**: Divide Row 2 by $5$, then apply $R_3 \leftarrow R_3 - 4R_2^{\text{new}}$ and $R_z \leftarrow R_z + 4R_2^{\text{new}}$:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Basic Var</th><th>$c_B$</th><th>$x_1$ ($3$)</th><th>$x_2$ ($5$)</th><th>$x_3$ ($4$)</th><th>$s_1$ ($0$)</th><th>$s_2$ ($0$)</th><th>$s_3$ ($0$)</th><th>RHS ($\bar{b}_i$)</th><th>Ratio $\theta_i = \bar{b}_i / y_{i1}$</th></tr></thead><tbody><tr><td>$x_2$</td><td>$5$</td><td>$2/3$</td><td>$1$</td><td>$0$</td><td>$1/3$</td><td>$0$</td><td>$0$</td><td>$8/3 = 40/15$</td><td>$(8/3)/(2/3) = 4.000$</td></tr><tr><td>$x_3$</td><td>$4$</td><td>$-4/15$</td><td>$0$</td><td>$1$</td><td>$-2/15$</td><td>$1/5$</td><td>$0$</td><td>$14/15$</td><td>— ($y_{21} = -4/15 < 0$)</td></tr><tr><td>$s_3$</td><td>$0$</td><td>$\mathbf{41/15}^*$</td><td>$0$</td><td>$0$</td><td>$-2/15$</td><td>$-4/5$</td><td>$1$</td><td>$89/15$</td><td>$(89/15)/(41/15) = 89/41 \approx 2.171$ (Min $\to$ Leave)</td></tr><tr><td>$z_j - c_j$</td><td>—</td><td>$\mathbf{-11/15}$ (Enter)</td><td>$0$</td><td>$0$</td><td>$17/15$</td><td>$4/5$</td><td>$0$</td><td>$Z_2 = 256/15$</td><td>$\theta^* = 89/41$</td></tr></tbody></table></div>

Notice that importing $x_3$ reduced $x_2$ when $x_1$ increases, making $z_1 - c_1 = 1/3 + 4(-4/15) = -11/15 < 0$! Thus $x_1$ now enters the basis and $s_3$ leaves in Row 3 with pivot $y_{31} = 41/15$.

### Solution, step 3: Iteration 3: Final Optimal Tableau and Solution Verification

Multiply Row 3 by $15/41$ and eliminate column $x_1$ from Rows 1, 2, and $z_j - c_j$:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Basic Var</th><th>$c_B$</th><th>$x_1$ ($3$)</th><th>$x_2$ ($5$)</th><th>$x_3$ ($4$)</th><th>$s_1$ ($0$)</th><th>$s_2$ ($0$)</th><th>$s_3$ ($0$)</th><th>RHS ($\bar{b}_i$)</th></tr></thead><tbody><tr><td>$x_2$</td><td>$5$</td><td>$0$</td><td>$1$</td><td>$0$</td><td>$15/41$</td><td>$8/41$</td><td>$-10/41$</td><td>$50/41$</td></tr><tr><td>$x_3$</td><td>$4$</td><td>$0$</td><td>$0$</td><td>$1$</td><td>$-6/41$</td><td>$5/41$</td><td>$4/41$</td><td>$62/41$</td></tr><tr><td>$x_1$</td><td>$3$</td><td>$1$</td><td>$0$</td><td>$0$</td><td>$-2/41$</td><td>$-12/41$</td><td>$15/41$</td><td>$89/41$</td></tr><tr><td>$z_j - c_j$</td><td>—</td><td>$0$</td><td>$0$</td><td>$0$</td><td>$45/41$</td><td>$24/41$</td><td>$11/41$</td><td>$Z^* = 765/41$</td></tr></tbody></table></div>

Because all non-basic net evaluations are strictly positive ($z_{s_1}-c_{s_1} = 45/41 > 0$, $z_{s_2}-c_{s_2} = 24/41 > 0$, $z_{s_3}-c_{s_3} = 11/41 > 0$), this tableau is the **unique global optimum**!
- **Optimal Decision Vector**: $x_1^* = \frac{89}{41} \approx 2.171$, $x_2^* = \frac{50}{41} \approx 1.220$, $x_3^* = \frac{62}{41} \approx 1.512$, with $s_1^* = s_2^* = s_3^* = 0$ (all three resource constraints are actively binding).
- **Maximum Objective Value**: $Z^* = 3\left(\frac{89}{41}\right) + 5\left(\frac{50}{41}\right) + 4\left(\frac{62}{41}\right) = \frac{267 + 250 + 248}{41} = \frac{765}{41} \approx 18.659$.

### Question 2: Dantzig's Two-Phase Simplex Algorithm on a Mixed Equality-Inequality System

Solve the following Linear Programming Problem using **Dantzig's Two-Phase Simplex Method**:

$$\text{Minimize } W = 4x_1 + x_2$$

subject to:

$$\begin{aligned}
3x_1 + x_2 &= 3 \\
4x_1 + 3x_2 &\ge 6 \\
x_1 + 2x_2 &\le 4 \\
x_1, x_2 &\ge 0
\end{aligned}$$

1. Introduce the required surplus, slack, and artificial variables to construct the Phase I auxiliary problem $\max Z_{\text{I}} = -A_1 - A_2$.
2. Execute Phase I to completion and verify whether a feasible solution exists ($Z_{\text{I}}^* = 0$).
3. Transition to Phase II, restore the original objective function, and compute the optimal solution $(x_1^*, x_2^*, W^*)$.

### Solution, step 1: Formulate the Phase I auxiliary system and initial tableau

Constraint 1 ($=$) requires an artificial variable $A_1 \ge 0$; Constraint 2 ($\ge$) requires a surplus variable $e_2 \ge 0$ and an artificial variable $A_2 \ge 0$; Constraint 3 ($\le$) requires only a slack variable $s_3 \ge 0$:

$$\begin{aligned}
3x_1 + x_2 + A_1 &= 3 \\
4x_1 + 3x_2 - e_2 + A_2 &= 6 \\
x_1 + 2x_2 + s_3 &= 4
\end{aligned}$$

In Phase I, we maximize $Z_{\text{I}} = -A_1 - A_2$ (so $c_{A_1} = -1, c_{A_2} = -1$, and all other Phase I costs are $0$). With initial basis $B_0 = \{A_1, A_2, s_3\}$, $\mathbf{c}_B = (-1, -1, 0)^T$, so $z_j^{\text{I}} - c_j^{\text{I}} = -(a_{1j} + a_{2j})$:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Basic Var</th><th>$c_B^{\text{I}}$</th><th>$x_1$ ($0$)</th><th>$x_2$ ($0$)</th><th>$e_2$ ($0$)</th><th>$s_3$ ($0$)</th><th>$A_1$ ($-1$)</th><th>$A_2$ ($-1$)</th><th>RHS ($\bar{b}_i$)</th><th>Ratio</th></tr></thead><tbody><tr><td>$A_1$</td><td>$-1$</td><td>$\mathbf{3}^*$</td><td>$1$</td><td>$0$</td><td>$0$</td><td>$1$</td><td>$0$</td><td>$3$</td><td>$3/3 = 1$ (Leave)</td></tr><tr><td>$A_2$</td><td>$-1$</td><td>$4$</td><td>$3$</td><td>$-1$</td><td>$0$</td><td>$0$</td><td>$1$</td><td>$6$</td><td>$6/4 = 1.5$</td></tr><tr><td>$s_3$</td><td>$0$</td><td>$1$</td><td>$2$</td><td>$0$</td><td>$1$</td><td>$0$</td><td>$0$</td><td>$4$</td><td>$4/1 = 4$</td></tr><tr><td>$z_j^{\text{I}} - c_j^{\text{I}}$</td><td>—</td><td>$\mathbf{-7}$ (Enter)</td><td>$-4$</td><td>$1$</td><td>$0$</td><td>$0$</td><td>$0$</td><td>$Z_{\text{I}} = -9$</td><td>$\theta^* = 1$</td></tr></tbody></table></div>

### Solution, step 2: Execute Phase I pivots to drive artificial variables to zero

**Phase I, Iteration 1**: $x_1$ enters and $A_1$ leaves (Row 1 divided by $3$; drop $A_1$ column):

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Basic Var</th><th>$c_B^{\text{I}}$</th><th>$x_1$ ($0$)</th><th>$x_2$ ($0$)</th><th>$e_2$ ($0$)</th><th>$s_3$ ($0$)</th><th>$A_2$ ($-1$)</th><th>RHS ($\bar{b}_i$)</th><th>Ratio</th></tr></thead><tbody><tr><td>$x_1$</td><td>$0$</td><td>$1$</td><td>$1/3$</td><td>$0$</td><td>$0$</td><td>$0$</td><td>$1$</td><td>$1/(1/3) = 3$</td></tr><tr><td>$A_2$</td><td>$-1$</td><td>$0$</td><td>$\mathbf{5/3}^*$</td><td>$-1$</td><td>$0$</td><td>$1$</td><td>$2$</td><td>$2/(5/3) = 6/5 = 1.2$ (Leave)</td></tr><tr><td>$s_3$</td><td>$0$</td><td>$0$</td><td>$5/3$</td><td>$0$</td><td>$1$</td><td>$0$</td><td>$3$</td><td>$3/(5/3) = 9/5 = 1.8$</td></tr><tr><td>$z_j^{\text{I}} - c_j^{\text{I}}$</td><td>—</td><td>$0$</td><td>$\mathbf{-5/3}$ (Enter)</td><td>$1$</td><td>$0$</td><td>$0$</td><td>$Z_{\text{I}} = -2$</td><td>$\theta^* = 6/5$</td></tr></tbody></table></div>

**Phase I, Iteration 2**: $x_2$ enters and $A_2$ leaves (multiply Row 2 by $3/5$ and drop $A_2$ column):

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Basic Var</th><th>$c_B^{\text{I}}$</th><th>$x_1$ ($0$)</th><th>$x_2$ ($0$)</th><th>$e_2$ ($0$)</th><th>$s_3$ ($0$)</th><th>RHS ($\bar{b}_i$)</th></tr></thead><tbody><tr><td>$x_1$</td><td>$0$</td><td>$1$</td><td>$0$</td><td>$1/5$</td><td>$0$</td><td>$3/5$</td></tr><tr><td>$x_2$</td><td>$0$</td><td>$0$</td><td>$1$</td><td>$-3/5$</td><td>$0$</td><td>$6/5$</td></tr><tr><td>$s_3$</td><td>$0$</td><td>$0$</td><td>$0$</td><td>$1$</td><td>$1$</td><td>$1$</td></tr><tr><td>$z_j^{\text{I}} - c_j^{\text{I}}$</td><td>—</td><td>$0$</td><td>$0$</td><td>$0$</td><td>$0$</td><td>$Z_{\text{I}}^* = 0$</td></tr></tbody></table></div>

Phase I terminates with $Z_{\text{I}}^* = 0$ and both artificial variables expelled from the basis! The initial Basic Feasible Solution for Phase II is $x_1 = 3/5, x_2 = 6/5, s_3 = 1, e_2 = 0$.

### Solution, step 3: Transition to Phase II and optimize the original objective

In **Phase II**, we minimize $W = 4x_1 + x_2$, or equivalently maximize $Z = -W = -4x_1 - x_2$ with Phase II cost coefficients $c_1 = -4, c_2 = -1, c_{e_2} = 0, c_{s_3} = 0$. Using the final Phase I basis $B = \{x_1, x_2, s_3\}$ with $\mathbf{c}_B = (-4, -1, 0)^T$, we compute $z_j - c_j = \mathbf{c}_B^T \mathbf{y}_j - c_j$:
- For non-basic $e_2$: $z_{e_2} - c_{e_2} = (-4)(1/5) + (-1)(-3/5) + (0)(1) - 0 = -1/5 < 0$.
- Current objective: $Z = (-4)(3/5) + (-1)(6/5) = -18/5$ (so $W = 18/5 = 3.6$).

Since $z_{e_2} - c_{e_2} = -1/5 < 0$, $e_2$ enters the basis! Applying the Minimum Ratio Test on the $e_2$ column $\mathbf{y}_{e_2} = (1/5, -3/5, 1)^T$:
- Row 1 ($x_1$): $(3/5)/(1/5) = 3$
- Row 2 ($x_2$): $y_{2, e_2} = -3/5 < 0$ (not eligible)
- Row 3 ($s_3$): $1 / 1 = 1$ (Minimum $\implies s_3$ leaves the basis!)

Pivoting on $y_{3, e_2} = 1$ in Row 3 ($R_1 \leftarrow R_1 - \frac{1}{5}R_3$, $R_2 \leftarrow R_2 + \frac{3}{5}R_3$, $R_z \leftarrow R_z + \frac{1}{5}R_3$) gives the final Phase II tableau:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Basic Var</th><th>$c_B$</th><th>$x_1$ ($-4$)</th><th>$x_2$ ($-1$)</th><th>$e_2$ ($0$)</th><th>$s_3$ ($0$)</th><th>RHS ($\bar{b}_i$)</th></tr></thead><tbody><tr><td>$x_1$</td><td>$-4$</td><td>$1$</td><td>$0$</td><td>$0$</td><td>$-1/5$</td><td>$2/5$</td></tr><tr><td>$x_2$</td><td>$-1$</td><td>$0$</td><td>$1$</td><td>$0$</td><td>$3/5$</td><td>$9/5$</td></tr><tr><td>$e_2$</td><td>$0$</td><td>$0$</td><td>$0$</td><td>$1$</td><td>$1$</td><td>$1$</td></tr><tr><td>$z_j - c_j$</td><td>—</td><td>$0$</td><td>$0$</td><td>$0$</td><td>$1/5$</td><td>$Z^* = -17/5$</td></tr></tbody></table></div>

Since $z_{s_3} - c_{s_3} = 1/5 > 0$, the Phase II tableau is globally optimal! The optimal solution is $x_1^* = 2/5 = 0.4$, $x_2^* = 9/5 = 1.8$, surplus $e_2^* = 1$, slack $s_3^* = 0$, and minimum cost $W^* = -Z^* = 4(2/5) + 1(9/5) = 17/5 = 3.4$.

### Question 3: Revised Simplex Method Execution with Explicit Basis Inverse and Eta Matrix Updates

Consider the Linear Programming Problem in standard form:

$$\text{Maximize } Z = 6x_1 + 5x_2$$

subject to:

$$\begin{aligned}
x_1 + x_2 + x_3 &= 5 \\
3x_1 + 2x_2 + x_4 &= 12 \\
x_1, x_2, x_3, x_4 &\ge 0
\end{aligned}$$

where $x_3, x_4$ are slack variables. Solve this problem using the **Revised Simplex Method** in explicit matrix form, showing at each iteration:
1. The current basis matrix $\mathbf{B}$, its inverse $\mathbf{B}^{-1}$, the basic variable vector $\bar{\mathbf{b}} = \mathbf{B}^{-1}\mathbf{b}$, and the simplex multiplier vector $\mathbf{w}^T = \mathbf{c}_B^T \mathbf{B}^{-1}$.
2. The matrix pricing step $z_j - c_j = \mathbf{w}^T\mathbf{a}_j - c_j$ for all non-basic variables and the FTRAN column computation $\mathbf{y}_k = \mathbf{B}^{-1}\mathbf{a}_k$.
3. The explicit elementary **Eta matrix** $\mathbf{E}_r$ used to update $\mathbf{B}_{\text{new}}^{-1} = \mathbf{E}_r \mathbf{B}^{-1}$ until optimality is proved.

### Solution, step 1: Iteration 0: Initial Basis Inverse, Pricing, FTRAN, and First Eta Matrix

Here $\mathbf{a}_1 = \begin{pmatrix} 1 \\ 3 \end{pmatrix}, \mathbf{a}_2 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}, \mathbf{a}_3 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \mathbf{a}_4 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \mathbf{b} = \begin{pmatrix} 5 \\ 12 \end{pmatrix}$, and $\mathbf{c} = (6, 5, 0, 0)^T$.
- **Initial Basis**: $B_0 = \{x_3, x_4\}$, $\mathbf{B}_0 = \mathbf{I}_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, $\mathbf{B}_0^{-1} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, $\bar{\mathbf{b}}_0 = \begin{pmatrix} 5 \\ 12 \end{pmatrix}$, $\mathbf{c}_{B_0} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$.
- **Simplex Multipliers**: $\mathbf{w}_0^T = \mathbf{c}_{B_0}^T \mathbf{B}_0^{-1} = (0, 0)$.
- **Pricing Non-Basic Columns** $N_0 = \{x_1, x_2\}$:
  $$z_1 - c_1 = \mathbf{w}_0^T\mathbf{a}_1 - c_1 = 0 - 6 = -6, \qquad z_2 - c_2 = \mathbf{w}_0^T\mathbf{a}_2 - c_2 = 0 - 5 = -5$$
  Choose $x_1$ to enter ($z_1 - c_1 = -6 < 0$).
- **FTRAN & Minimum Ratio Test**: Compute $\mathbf{y}_1 = \mathbf{B}_0^{-1}\mathbf{a}_1 = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$. Ratios: $\min \{ 5/1, 12/3 \} = \min \{5, 4\} = 4$ in Row $r = 2$ ($x_4$ leaves the basis, $y_{21} = 3$).
- **Eta Matrix Update**: Column $r=2$ of $\mathbf{E}_2$ is $\boldsymbol{\eta}_2 = \begin{pmatrix} -y_{11}/y_{21} \\ 1/y_{21} \end{pmatrix} = \begin{pmatrix} -1/3 \\ 1/3 \end{pmatrix}$:
  $$\mathbf{E}_2 = \begin{pmatrix} 1 & -1/3 \\ 0 & 1/3 \end{pmatrix} \implies \mathbf{B}_1^{-1} = \mathbf{E}_2 \mathbf{B}_0^{-1} = \begin{pmatrix} 1 & -1/3 \\ 0 & 1/3 \end{pmatrix}, \qquad \bar{\mathbf{b}}_1 = \mathbf{E}_2 \bar{\mathbf{b}}_0 = \begin{pmatrix} 5 - 12/3 \\ 12/3 \end{pmatrix} = \begin{pmatrix} 1 \\ 4 \end{pmatrix}$$

### Solution, step 2: Iteration 1: Updated Multipliers, Pricing, FTRAN, and Second Eta Matrix

Now $B_1 = \{x_3, x_1\}$ with $\mathbf{c}_{B_1} = (0, 6)^T$ and $N_1 = \{x_2, x_4\}$.
- **Simplex Multipliers**:
  $$\mathbf{w}_1^T = \mathbf{c}_{B_1}^T \mathbf{B}_1^{-1} = \begin{pmatrix} 0 & 6 \end{pmatrix} \begin{pmatrix} 1 & -1/3 \\ 0 & 1/3 \end{pmatrix} = \begin{pmatrix} 0 & 2 \end{pmatrix}$$
- **Pricing Non-Basic Columns** $N_1 = \{x_2, x_4\}$:
  $$z_2 - c_2 = \mathbf{w}_1^T\mathbf{a}_2 - c_2 = \begin{pmatrix} 0 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix} - 5 = 4 - 5 = -1 < 0$$
  $$z_4 - c_4 = \mathbf{w}_1^T\mathbf{a}_4 - c_4 = \begin{pmatrix} 0 & 2 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} - 0 = 2 > 0$$
  Since $z_2 - c_2 = -1 < 0$, $x_2$ enters the basis!
- **FTRAN & Minimum Ratio Test**: Compute $\mathbf{y}_2 = \mathbf{B}_1^{-1}\mathbf{a}_2$:
  $$\mathbf{y}_2 = \begin{pmatrix} 1 & -1/3 \\ 0 & 1/3 \end{pmatrix} \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 1/3 \\ 2/3 \end{pmatrix}$$
  Ratios against $\bar{\mathbf{b}}_1 = (1, 4)^T$: Row 1 gives $1 / (1/3) = 3$; Row 2 gives $4 / (2/3) = 6$. The minimum is $\theta^* = 3$ in Row $r = 1$ ($x_3$ leaves the basis, pivot $y_{12} = 1/3$).
- **Eta Matrix Update**: Column $r=1$ of $\mathbf{E}_1$ is $\boldsymbol{\eta}_1 = \begin{pmatrix} 1/y_{12} \\ -y_{22}/y_{12} \end{pmatrix} = \begin{pmatrix} 3 \\ -2 \end{pmatrix}$:
  $$\mathbf{E}_1 = \begin{pmatrix} 3 & 0 \\ -2 & 1 \end{pmatrix} \implies \mathbf{B}_2^{-1} = \mathbf{E}_1 \mathbf{B}_1^{-1} = \begin{pmatrix} 3 & 0 \\ -2 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1/3 \\ 0 & 1/3 \end{pmatrix} = \begin{pmatrix} 3 & -1 \\ -2 & 1 \end{pmatrix}$$
  $$\bar{\mathbf{b}}_2 = \mathbf{E}_1 \bar{\mathbf{b}}_1 = \begin{pmatrix} 3 & 0 \\ -2 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 4 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}$$

### Solution, step 3: Iteration 2: Optimality Verification via Dual Multipliers

Now $B_2 = \{x_2, x_1\}$ with $\mathbf{c}_{B_2} = (5, 6)^T$, $\mathbf{x}_{B_2} = \begin{pmatrix} x_2 \\ x_1 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}$, and $N_2 = \{x_3, x_4\}$.
- **Simplex Multipliers**:
  $$\mathbf{w}_2^T = \mathbf{c}_{B_2}^T \mathbf{B}_2^{-1} = \begin{pmatrix} 5 & 6 \end{pmatrix} \begin{pmatrix} 3 & -1 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} 3 & 1 \end{pmatrix}$$
- **Pricing Non-Basic Columns** $N_2 = \{x_3, x_4\}$:
  $$z_3 - c_3 = \mathbf{w}_2^T\mathbf{a}_3 - c_3 = 3 - 0 = 3 > 0, \qquad z_4 - c_4 = \mathbf{w}_2^T\mathbf{a}_4 - c_4 = 1 - 0 = 1 > 0$$
Because $z_j - c_j \ge 0$ for all $j \in N_2$, the Revised Simplex Method terminates at the unique global optimum: $x_1^* = 2, x_2^* = 3, x_3^* = 0, x_4^* = 0$, with maximum objective value $Z^* = \mathbf{c}_{B_2}^T \bar{\mathbf{b}}_2 = 5(3) + 6(2) = 27$.
