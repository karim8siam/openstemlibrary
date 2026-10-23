# Unit 3: Duality Theory, Complementary Slackness & Post-Optimality Sensitivity Analysis

## 3.1 Symmetric and Asymmetric Primal-Dual Formulations and the Involution Theorem

Every Linear Programming Problem, which we designate as the **Primal Problem (P)**, is intrinsically paired with a companion linear optimization problem constructed from the exact same data arrays $(\mathbf{A}, \mathbf{b}, \mathbf{c})$, termed the **Dual Problem (D)**. Originating in John von Neumann's 1947 notes linking linear programming to zero-sum matrix games and formalized by David Gale, Harold Kuhn, and Albert Tucker (1951), Duality Theory reveals that optimizing a primal system in $\mathbb{R}^n$ subject to $m$ constraints is mathematically equivalent to optimizing a dual system in $\mathbb{R}^m$ subject to $n$ constraints.

### Symmetric Primal-Dual Pairings

Consider the **Symmetric Canonical Primal Problem (P)** in $n$ non-negative decision variables $\mathbf{x} = (x_1, \dots, x_n)^T \in \mathbb{R}_+^n$ and $m$ resource inequalities defined by $\mathbf{A} = [a_{ij}] \in \mathbb{R}^{m \times n}$, $\mathbf{b} \in \mathbb{R}^m$, and $\mathbf{c} \in \mathbb{R}^n$:

$$\text{(P)} \quad \text{Maximize } Z = \mathbf{c}^T \mathbf{x} = \sum_{j=1}^n c_j x_j \quad \text{subject to} \quad \mathbf{A}\mathbf{x} \le \mathbf{b} \;\; \left(\sum_{j=1}^n a_{ij} x_j \le b_i, \; i=1,\dots,m\right), \quad \mathbf{x} \ge \mathbf{0}$$

Associated with each of the $m$ primal constraints $i \in \{1, \dots, m\}$, we introduce a scalar **dual variable** $y_i$ to form the dual column vector $\mathbf{y} = (y_1, y_2, \dots, y_m)^T \in \mathbb{R}^m$. The **Symmetric Dual Problem (D)** reverses the sense of optimization from maximization to minimization, interchanges the roles of the right-hand-side capacity vector $\mathbf{b}$ and the objective coefficient vector $\mathbf{c}$, and transposes the technological matrix $\mathbf{A}$ to $\mathbf{A}^T \in \mathbb{R}^{n \times m}$:

$$\text{(D)} \quad \text{Minimize } W = \mathbf{b}^T \mathbf{y} = \sum_{i=1}^m b_i y_i \quad \text{subject to} \quad \mathbf{A}^T \mathbf{y} \ge \mathbf{c} \;\; \left(\sum_{i=1}^m a_{ij} y_i \ge c_j, \; j=1,\dots,n\right), \quad \mathbf{y} \ge \mathbf{0}$$

### Asymmetric Formulations and the General Primal-Dual Correspondence Table

What if the Primal Problem contains a mixture of $\le$ inequalities, $\ge$ inequalities, and strict equalities ($=$), alongside non-negative, non-positive, and unrestricted variables? By converting any general Primal LP into symmetric canonical form (replacing $\mathbf{a}_i^T\mathbf{x} \ge b_i$ by $-\mathbf{a}_i^T\mathbf{x} \le -b_i$, replacing $\mathbf{a}_i^T\mathbf{x} = b_i$ by the pair $\mathbf{a}_i^T\mathbf{x} \le b_i$ and $-\mathbf{a}_i^T\mathbf{x} \le -b_i$ with dual variables $y_i^+, y_i^- \ge 0$ so $y_i = y_i^+ - y_i^- \in \mathbb{R}$ is unrestricted, and splitting unrestricted primal variables $x_j = x_j^+ - x_j^-$), we obtain an exact one-to-one structural correspondence between the $m$ primal constraints and $m$ dual variables, and between the $n$ primal variables and $n$ dual constraints:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Maximization Primal (P)</th><th>Minimization Dual (D)</th><th>Structural Intuition</th></tr></thead><tbody><tr><td>Objective $\max Z = \mathbf{c}^T\mathbf{x}$</td><td>Objective $\min W = \mathbf{b}^T\mathbf{y}$</td><td>Primal RHS $\mathbf{b}$ becomes Dual cost; Primal cost $\mathbf{c}$ becomes Dual RHS</td></tr><tr><td>Constraint $i$ is $\le$ (Sensible)</td><td>Dual variable $y_i \ge 0$ (Sensible)</td><td>Upper resource bound commands a non-negative shadow price</td></tr><tr><td>Constraint $i$ is $=$ (Odd)</td><td>Dual variable $y_i \in \mathbb{R}$ unrestricted (Odd)</td><td>Exact equality constraint can impede objective in either direction</td></tr><tr><td>Constraint $i$ is $\ge$ (Bizarre)</td><td>Dual variable $y_i \le 0$ (Bizarre)</td><td>Reversed primal inequality reverses dual variable sign</td></tr><tr><td>Variable $x_j \ge 0$ (Sensible)</td><td>Dual constraint $j$ is $\ge$ (Sensible)</td><td>Non-negative primal activity requires imputed cost $\ge$ unit return</td></tr><tr><td>Variable $x_j \in \mathbb{R}$ free (Odd)</td><td>Dual constraint $j$ is $=$ (Odd)</td><td>Unrestricted primal activity forces exact zero net arbitrage ($\mathbf{a}_j^T\mathbf{y} = c_j$)</td></tr><tr><td>Variable $x_j \le 0$ (Bizarre)</td><td>Dual constraint $j$ is $\le$ (Bizarre)</td><td>Non-positive primal activity reverses dual inequality</td></tr></tbody></table></div>

#### Theorem 3.1 (Involutory Property: The Dual of the Dual is the Primal):
For any Linear Programming Problem (P), constructing the dual of its dual problem (D) recovers the exact original Primal Problem (P).

#### Proof:
Write the symmetric Dual (D) as a maximization problem by negating its objective and constraints: $\max (-W) = (-\mathbf{b})^T \mathbf{y}$ subject to $(-\mathbf{A}^T)\mathbf{y} \le -\mathbf{c}, \mathbf{y} \ge \mathbf{0}$. Applying the canonical dual transformation to this maximization problem yields a minimization problem in vector $\mathbf{x} \ge \mathbf{0}$: $\min (-\mathbf{c})^T \mathbf{x}$ subject to $(-\mathbf{A}^T)^T \mathbf{x} \ge -\mathbf{b}, \mathbf{x} \ge \mathbf{0}$. Negating the objective back to maximization and multiplying the constraints by $-1$ produces $\max Z = \mathbf{c}^T\mathbf{x}$ subject to $\mathbf{A}\mathbf{x} \le \mathbf{b}, \mathbf{x} \ge \mathbf{0}$, which is identically (P).

## 3.2 Economic Interpretation of Duality: Imputed Resource Valuations and Shadow Prices

Duality Theory is far more than a formal algebraic transposition; as discovered by Leonid Kantorovich (1939) and Tjalling Koopmans (1951), the Dual Linear Program embodies the decentralized price mechanism of competitive economic equilibrium and statistical resource valuation.

Suppose the Primal Problem $\max Z = \sum_{j=1}^n c_j x_j$ subject to $\sum_{j=1}^n a_{ij} x_j \le b_i$ ($i=1,\dots,m$), $x_j \ge 0$, models a manufacturing enterprise or statistical research institute that uses $m$ scarce resources (each available in total quantity $b_i$ units) to produce $n$ distinct outputs (in quantities $x_j$, each generating net revenue $c_j$ dollars per unit and consuming $a_{ij}$ units of resource $i$ per unit of output $j$). Dimensional analysis immediately illuminates the meaning of the dual variables $y_i$:
- Because $b_i$ is measured in `[units of resource i]` and the dual objective $W = \sum_{i=1}^m b_i y_i$ is measured in `[dollars]`, each dual variable $y_i$ must have physical dimensions of **`[dollars per unit of resource i]`**.

Thus, $y_i$ represents the **imputed unit valuation** (or **accounting price** / **shadow price**) assigned internally to one unit of scarce resource $i$. Now consider an outside entrepreneur or resource broker who offers to rent or purchase the entire endowment $(b_1, \dots, b_m)$ of the enterprise's resources at unit prices $\mathbf{y} = (y_1, \dots, y_m)^T \ge \mathbf{0}$:
1. **The Dual Constraint ($\sum_{i=1}^m a_{ij} y_i \ge c_j$)**: To produce one unit of activity $j$, the enterprise consumes bundle $(a_{1j}, a_{2j}, \dots, a_{mj})$ of the $m$ resources. At unit resource prices $y_i$, the total **imputed opportunity cost** of the resources tied up in producing one unit of activity $j$ is $\sum_{i=1}^m a_{ij} y_i$. For the enterprise to be willing to cede its resources rather than operate activity $j$ internally, the imputed value of the resources required to make one unit of product $j$ must be at least as large as the direct profit $c_j$ that product $j$ would generate! If $\sum_{i=1}^m a_{ij} y_i < c_j$, an arbitrage profit opportunity exists: purchasing the required resources at prices $y_i$ and running activity $j$ yields a strictly positive net economic rent $c_j - \sum_{i=1}^m a_{ij} y_i > 0$.
2. **The Dual Objective ($\min W = \sum_{i=1}^m b_i y_i$)**: Subject to offering competitive resource valuations that leave zero excess arbitrage profit across all $n$ production activities ($\mathbf{A}^T\mathbf{y} \ge \mathbf{c}$), the buyer seeks to **minimize the total expenditure** $W = \sum_{i=1}^m b_i y_i$ paid for the resource bundle $\mathbf{b}$.

At the joint primal-dual optimum $(\mathbf{x}^*, \mathbf{y}^*)$, Strong Duality ($\mathbf{c}^T\mathbf{x}^* = \mathbf{b}^T\mathbf{y}^*$) states that the **maximum total profit** achievable by physical production equals the **minimum total imputed value** of the scarce resources! Moreover, if the optimal primal basis $\mathbf{B}$ is non-degenerate, the optimal dual vector $\mathbf{y}^* = (\mathbf{B}^{-1})^T \mathbf{c}_B$ equals the exact **marginal partial derivative (shadow price)** of the optimal objective value function $Z^*(\mathbf{b}) = \mathbf{c}_B^T \mathbf{B}^{-1}\mathbf{b}$ with respect to each resource availability $b_i$:

$$y_i^* = \frac{\partial Z^*(\mathbf{b})}{\partial b_i}, \qquad i = 1, 2, \dots, m$$

That is, $y_i^*$ quantifies the exact rate at which maximum achievable profit $Z^*$ increases per additional unit of resource $i$ made available (within the feasibility range of the current optimal basis $\mathbf{B}$).

## 3.3 The Weak Duality Lemma, Farkas' Lemma, and the Strong Duality Theorem

We now establish the rigorous mathematical theorems governing the relationship between the Primal Problem (P): $\max Z = \mathbf{c}^T\mathbf{x}$ subject to $\mathbf{A}\mathbf{x} \le \mathbf{b}, \mathbf{x} \ge \mathbf{0}$, and the Dual Problem (D): $\min W = \mathbf{b}^T\mathbf{y}$ subject to $\mathbf{A}^T\mathbf{y} \ge \mathbf{c}, \mathbf{y} \ge \mathbf{0}$.

### Lemma 3.1 (The Weak Duality Theorem):
Let $\mathbf{x} \in \mathbb{R}_+^n$ be any feasible solution of the Primal Problem (P) ($\mathbf{A}\mathbf{x} \le \mathbf{b}, \mathbf{x} \ge \mathbf{0}$), and let $\mathbf{y} \in \mathbb{R}_+^m$ be any feasible solution of the Dual Problem (D) ($\mathbf{A}^T\mathbf{y} \ge \mathbf{c}, \mathbf{y} \ge \mathbf{0}$). Then the primal objective value never exceeds the dual objective value:

$$Z(\mathbf{x}) = \mathbf{c}^T \mathbf{x} \le \mathbf{b}^T \mathbf{y} = W(\mathbf{y})$$

#### Proof:
Because $\mathbf{y}$ is dual feasible ($\mathbf{A}^T\mathbf{y} \ge \mathbf{c}$, or $\mathbf{c}^T \le \mathbf{y}^T\mathbf{A}$) and $\mathbf{x} \ge \mathbf{0}$ is non-negative, taking the inner product with $\mathbf{x}$ preserves the direction of inequality:

$$\mathbf{c}^T \mathbf{x} \le (\mathbf{y}^T \mathbf{A}) \mathbf{x} = \mathbf{y}^T (\mathbf{A}\mathbf{x})$$

Similarly, because $\mathbf{x}$ is primal feasible ($\mathbf{A}\mathbf{x} \le \mathbf{b}$) and $\mathbf{y} \ge \mathbf{0}$ is non-negative, taking the inner product with $\mathbf{y}^T$ preserves the inequality:

$$\mathbf{y}^T (\mathbf{A}\mathbf{x}) \le \mathbf{y}^T \mathbf{b} = \mathbf{b}^T \mathbf{y}$$

Chaining these two inequalities together yields $\mathbf{c}^T\mathbf{x} \le \mathbf{y}^T\mathbf{A}\mathbf{x} \le \mathbf{b}^T\mathbf{y}$, completing the proof. The non-negative difference $W(\mathbf{y}) - Z(\mathbf{x}) = \mathbf{b}^T\mathbf{y} - \mathbf{c}^T\mathbf{x} \ge 0$ is called the **duality gap** at the feasible pair $(\mathbf{x}, \mathbf{y})$.

#### Immediate Corollaries of Weak Duality:
1. **Sufficient Certificate of Optimality**: If $\mathbf{x}^*$ is primal feasible, $\mathbf{y}^*$ is dual feasible, and their objectives coincide ($\mathbf{c}^T\mathbf{x}^* = \mathbf{b}^T\mathbf{y}^*$), then $\mathbf{x}^*$ is globally optimal for (P) and $\mathbf{y}^*$ is globally optimal for (D), because for every primal feasible $\mathbf{x}$ and dual feasible $\mathbf{y}$, $\mathbf{c}^T\mathbf{x} \le \mathbf{b}^T\mathbf{y}^* = \mathbf{c}^T\mathbf{x}^* \le \mathbf{b}^T\mathbf{y}$.
2. **Primal Unboundedness Implies Dual Infeasibility**: If (P) is unbounded above ($\sup \mathbf{c}^T\mathbf{x} = +\infty$), then (D) must be strictly infeasible ($\mathcal{F}_D = \emptyset$), since any dual feasible vector $\mathbf{y}$ would provide a finite upper bound $\mathbf{b}^T\mathbf{y} < \infty$ on $\mathbf{c}^T\mathbf{x}$.
3. **Dual Unboundedness Implies Primal Infeasibility**: Symmetrically, if (D) is unbounded below ($\inf \mathbf{b}^T\mathbf{y} = -\infty$), then (P) must be strictly infeasible ($\mathcal{F}_P = \emptyset$). (Note: It is possible for **both** (P) and (D) to be simultaneously infeasible!)

### Farkas' Lemma and the Strong Duality Theorem

The bridge from Weak Duality to zero duality gap at optimality is anchored by **Farkas' Lemma** (Gyula Farkas, 1902), a foundational theorem of the alternative deduced from separating hyperplanes: for any matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$ and vector $\mathbf{b} \in \mathbb{R}^m$, **exactly one** of the following two linear systems possesses a solution:
- **System I**: $\mathbf{A}\mathbf{x} = \mathbf{b}$ and $\mathbf{x} \ge \mathbf{0}$ (meaning $\mathbf{b}$ lies inside the finitely generated convex cone $\text{cone}(\mathbf{a}_1, \dots, \mathbf{a}_n)$).
- **System II**: $\mathbf{A}^T\mathbf{y} \le \mathbf{0}$ and $\mathbf{b}^T\mathbf{y} > 0$ (meaning there exists a hyperplane with normal $\mathbf{y}$ separating $\mathbf{b}$ from $\text{cone}(\mathbf{a}_1, \dots, \mathbf{a}_n)$).

### Theorem 3.2 (The Strong Duality Theorem of Linear Programming):
If either the Primal Problem (P) or the Dual Problem (D) possesses a finite optimal solution, then **so does the other**, and their optimal objective values are **strictly equal** (zero duality gap):

$$Z^* = \max_{\mathbf{x} \in \mathcal{F}_P} \mathbf{c}^T \mathbf{x} = \min_{\mathbf{y} \in \mathcal{F}_D} \mathbf{b}^T \mathbf{y} = W^*$$

Moreover, if $\mathbf{B}$ is an optimal basis matrix for the standard-form Primal Problem ($\max \mathbf{c}^T\mathbf{x} + \mathbf{0}^T\mathbf{s}$ subject to $\mathbf{A}\mathbf{x} + \mathbf{I}_m\mathbf{s} = \mathbf{b}, \mathbf{x},\mathbf{s} \ge \mathbf{0}$), then the **Simplex multiplier vector** $\mathbf{y}^* = (\mathbf{B}^{-1})^T \mathbf{c}_B$ is an **optimal Basic Feasible Solution of the Dual Problem (D)**!

#### Constructive Simplex Proof of Strong Duality:
Suppose (P) has a finite optimal solution. Adding slack variables $\mathbf{s} \ge \mathbf{0}$ with cost $\mathbf{c}_s = \mathbf{0}$, the Simplex Algorithm (with Bland's anti-cycling rule) terminates at an optimal basis $\mathbf{B}$ with primal BFS $\mathbf{x}_B^* = \mathbf{B}^{-1}\mathbf{b} \ge \mathbf{0}$ and optimal objective $Z^* = \mathbf{c}_B^T \mathbf{B}^{-1}\mathbf{b}$. At termination, the Simplex optimality condition holds across all $n$ structural columns $\mathbf{a}_j$ of $\mathbf{A}$ and all $m$ slack columns $\mathbf{e}_i$ of $\mathbf{I}_m$. Define $\mathbf{y}^* = (\mathbf{B}^{-1})^T \mathbf{c}_B$, so $(\mathbf{y}^*)^T = \mathbf{c}_B^T \mathbf{B}^{-1}$.
1. For the $n$ structural columns $j = 1, \dots, n$, the optimal net evaluation satisfies:
   $$z_j - c_j = \mathbf{c}_B^T \mathbf{B}^{-1} \mathbf{a}_j - c_j = (\mathbf{y}^*)^T \mathbf{a}_j - c_j \ge 0 \implies \mathbf{A}^T \mathbf{y}^* \ge \mathbf{c}$$
2. For the $m$ slack columns $s_i$ with unit column $\mathbf{e}_i$ and cost $c_{s_i} = 0$, the optimal net evaluation satisfies:
   $$z_{s_i} - 0 = \mathbf{c}_B^T \mathbf{B}^{-1} \mathbf{e}_i - 0 = (\mathbf{y}^*)^T \mathbf{e}_i = y_i^* \ge 0 \implies \mathbf{y}^* \ge \mathbf{0}$$

Thus $\mathbf{y}^* = (\mathbf{B}^{-1})^T \mathbf{c}_B$ satisfies both $\mathbf{A}^T\mathbf{y}^* \ge \mathbf{c}$ and $\mathbf{y}^* \ge \mathbf{0}$, proving that **$\mathbf{y}^*$ is Dual Feasible**! Notice further that $y_i^* = z_{s_i} - c_{s_i}$, meaning **the optimal dual variables $y_1^*, \dots, y_m^*$ appear directly in the final Simplex $z_j - c_j$ row under the $m$ slack columns**! Finally, evaluating the dual objective at $\mathbf{y}^*$ gives:

$$W(\mathbf{y}^*) = \mathbf{b}^T \mathbf{y}^* = (\mathbf{y}^*)^T \mathbf{b} = \mathbf{c}_B^T \mathbf{B}^{-1} \mathbf{b} = \mathbf{c}_B^T \mathbf{x}_B^* = Z^*$$

By Corollary 1 of Weak Duality, equality $W(\mathbf{y}^*) = Z^*$ proves that $\mathbf{y}^*$ is globally optimal for (D) and $Z^* = W^*$.

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Primal (P) / Dual (D) Status</th><th>Dual Optimal (Finite)</th><th>Dual Unbounded</th><th>Dual Infeasible</th></tr></thead><tbody><tr><td><strong>Primal Optimal (Finite)</strong></td><td><strong>Possible</strong> (Strong Duality $Z^* = W^*$)</td><td>Impossible (violates Weak Duality)</td><td>Impossible (violates Strong Duality)</td></tr><tr><td><strong>Primal Unbounded</strong></td><td>Impossible (violates Weak Duality)</td><td>Impossible (violates Weak Duality)</td><td><strong>Possible</strong> (Primal ray $\implies \mathcal{F}_D = \emptyset$)</td></tr><tr><td><strong>Primal Infeasible</strong></td><td>Impossible (violates Strong Duality)</td><td><strong>Possible</strong> (Dual ray $\implies \mathcal{F}_P = \emptyset$)</td><td><strong>Possible</strong> (Both $\mathcal{F}_P = \emptyset$ and $\mathcal{F}_D = \emptyset$)</td></tr></tbody></table></div>

## 3.4 The Complementary Slackness Theorem and Primal-Dual Optimality Verification

The algebraic chain of inequalities in the proof of the Weak Duality Lemma ($\mathbf{c}^T\mathbf{x} \le \mathbf{y}^T\mathbf{A}\mathbf{x} \le \mathbf{b}^T\mathbf{y}$) yields a powerful necessary and sufficient condition linking the positive variables of one problem to the binding constraints of the other, known as the **Complementary Slackness Theorem**.

Let $\mathbf{x} \in \mathbb{R}_+^n$ be primal feasible for (P) with primal slack vector $\mathbf{s} = \mathbf{b} - \mathbf{A}\mathbf{x} \ge \mathbf{0}$ ($s_i = b_i - \sum_{j=1}^n a_{ij}x_j \ge 0$ for $i=1,\dots,m$), and let $\mathbf{y} \in \mathbb{R}_+^m$ be dual feasible for (D) with dual surplus vector $\mathbf{e} = \mathbf{A}^T\mathbf{y} - \mathbf{c} \ge \mathbf{0}$ ($e_j = \sum_{i=1}^m a_{ij}y_i - c_j \ge 0$ for $j=1,\dots,n$). Expressing the duality gap $W(\mathbf{y}) - Z(\mathbf{x})$ in terms of $\mathbf{s}$ and $\mathbf{e}$, we substitute $\mathbf{b} = \mathbf{A}\mathbf{x} + \mathbf{s}$ and $\mathbf{c} = \mathbf{A}^T\mathbf{y} - \mathbf{e}$:

$$W(\mathbf{y}) - Z(\mathbf{x}) = \mathbf{b}^T\mathbf{y} - \mathbf{c}^T\mathbf{x} = (\mathbf{A}\mathbf{x} + \mathbf{s})^T\mathbf{y} - (\mathbf{A}^T\mathbf{y} - \mathbf{e})^T\mathbf{x} = \mathbf{x}^T\mathbf{A}^T\mathbf{y} + \mathbf{s}^T\mathbf{y} - \mathbf{y}^T\mathbf{A}\mathbf{x} + \mathbf{e}^T\mathbf{x} = \mathbf{s}^T\mathbf{y} + \mathbf{e}^T\mathbf{x}$$

Writing out the two inner products componentwise:

$$W(\mathbf{y}) - Z(\mathbf{x}) = \sum_{i=1}^m s_i y_i + \sum_{j=1}^n e_j x_j = \sum_{i=1}^m \left( b_i - \sum_{j=1}^n a_{ij} x_j \right) y_i + \sum_{j=1}^n \left( \sum_{i=1}^m a_{ij} y_i - c_j \right) x_j \ge 0$$

### Theorem 3.3 (The Complementary Slackness Theorem):
Let $\mathbf{x}$ be feasible for the Primal Problem (P) and $\mathbf{y}$ be feasible for the Dual Problem (D). Then $\mathbf{x}$ and $\mathbf{y}$ are simultaneously optimal for (P) and (D), respectively, **if and only if** they satisfy the **Complementary Slackness Conditions**:

$$\begin{aligned}
\text{1. Primal Complementary Slackness:} \quad & s_i y_i = \left( b_i - \sum_{j=1}^n a_{ij} x_j \right) y_i = 0 \qquad \forall i = 1, 2, \dots, m \\
\text{2. Dual Complementary Slackness:} \quad & e_j x_j = \left( \sum_{i=1}^m a_{ij} y_i - c_j \right) x_j = 0 \qquad \forall j = 1, 2, \dots, n
\end{aligned}$$

Equivalently, in logical implication form at any primal-dual optimal pair $(\mathbf{x}^*, \mathbf{y}^*)$:
- **If a primal constraint is non-binding (has positive slack $s_i^* > 0$), its corresponding dual shadow price must equal zero ($y_i^* = 0$)**. Economically, a resource that is in excess supply (leftover idle capacity at the optimum) is a free good with zero marginal shadow value!
- **If a dual shadow price is strictly positive ($y_i^* > 0$), its corresponding primal resource constraint must be tightly binding ($s_i^* = 0$, i.e., $\sum_{j=1}^n a_{ij}x_j^* = b_i$)**.
- **If a primal activity is operated at a strictly positive level ($x_j^* > 0$), its corresponding dual constraint must hold with exact equality ($e_j^* = 0$, i.e., $\sum_{i=1}^m a_{ij}y_i^* = c_j$)**. Economically, any product actually manufactured at the optimum must break even exactly against the imputed opportunity cost of the resources it consumes.
- **If a dual constraint has positive surplus ($e_j^* > 0$, so imputed resource cost $\sum_{i=1}^m a_{ij}y_i^* > c_j$ exceeds unit revenue), that primal activity must be shut down completely ($x_j^* = 0$)**.

#### Proof:
By Strong Duality, feasible vectors $\mathbf{x}$ and $\mathbf{y}$ are optimal if and only if the duality gap vanishes: $W(\mathbf{y}) - Z(\mathbf{x}) = \sum_{i=1}^m s_i y_i + \sum_{j=1}^n e_j x_j = 0$. Because $s_i \ge 0, y_i \ge 0$ for all $i$ and $e_j \ge 0, x_j \ge 0$ for all $j$, every single product term $s_i y_i \ge 0$ and $e_j x_j \ge 0$ is non-negative. A sum of non-negative real numbers equals zero if and only if **every individual term equals zero**, namely $s_i y_i = 0$ for all $i=1,\dots,m$ and $e_j x_j = 0$ for all $j=1,\dots,n$. (Furthermore, the ** Goldman–Tucker Strict Complementary Slackness Theorem** proves that whenever (P) and (D) are feasible, there exists at least one optimal pair $(\mathbf{x}^*, \mathbf{y}^*)$ that is *strictly complementary*, satisfying $s_i^* + y_i^* > 0$ for all $i$ and $e_j^* + x_j^* > 0$ for all $j$.)

## 3.5 Lemke's Dual Simplex Algorithm: Restoring Primal Feasibility under Dual Optimality

In the standard (Primal) Simplex Algorithm of Unit 2, computation begins at a **primal feasible** basic solution ($\bar{\mathbf{b}} = \mathbf{B}^{-1}\mathbf{b} \ge \mathbf{0}$) that is **dual infeasible** ($z_j - c_j < 0$ for some $j \in N$), and pivots iteratively to achieve dual feasibility ($z_j - c_j \ge 0$) while preserving primal feasibility ($\bar{\mathbf{b}} \ge \mathbf{0}$) at every step.

Frequently, however—especially in post-optimality sensitivity analysis when a right-hand-side capacity $b_i$ is reduced, when a new cutting-plane inequality is appended in Gomory's integer programming algorithm (Unit 6), or in minimization models with $\ge$ constraints ($\sum a_{ij}x_j \ge b_i \iff \sum (-a_{ij})x_j + s_i = -b_i < 0$) and positive costs $c_j \ge 0$—we possess a basis $\mathbf{B}$ that is already **Dual Feasible** (satisfying the Simplex optimality condition $z_j - c_j \ge 0$ for all $j \in N$ in maximization, or $z_j - c_j \le 0$ in minimization), but **Primal Infeasible** because one or more basic variables are strictly negative ($\bar{b}_i < 0$ for some $i \in \{1, \dots, m\}$). Rather than introducing artificial variables and starting over with a costly Two-Phase or Big-M procedure, Carlton E. Lemke (1954) invented the **Dual Simplex Algorithm**, which performs pivots that **preserve dual feasibility ($z_j - c_j \ge 0$) while systematically eliminating negative right-hand sides ($\bar{b}_i < 0$)** until primal feasibility ($\bar{\mathbf{b}} \ge \mathbf{0}$) is attained!

### Algorithmic Mechanics of the Dual Simplex Method (Maximization Form)

Assume the current Simplex tableau is **dual feasible** ($z_j - c_j \ge 0$ for all $j \in \{1, \dots, n\}$), and we wish to achieve primal feasibility ($\bar{b}_i \ge 0$ for all $i = 1, \dots, m$):

1. **Primal Optimality Check**: If $\bar{b}_i \ge 0$ for all $i = 1, \dots, m$, stop! Because the tableau is simultaneously primal feasible ($\bar{\mathbf{b}} \ge \mathbf{0}$) and dual feasible ($z_j - c_j \ge 0$), the current BFS is globally optimal.
2. **Leaving Variable Selection (Most Negative RHS Rule)**: If at least one basic variable is negative, select the **leaving basic variable** $x_{B(r)}$ in row $r$ corresponding to the **most negative right-hand-side constant**:
   $$\bar{b}_r = \min_{1 \le i \le m} \left\{ \bar{b}_i : \bar{b}_i < 0 \right\} < 0$$
3. **Primal Infeasibility Certificate Check**: Inspect the coefficients $y_{rj}$ across row $r$ for all non-basic variables $j \in N$. Because the $r$-th basic equation reads:
   $$x_{B(r)} = \bar{b}_r - \sum_{j \in N} y_{rj} x_j \implies \sum_{j \in N} y_{rj} x_j + x_{B(r)} = \bar{b}_r < 0$$
   if $y_{rj} \ge 0$ for **all** $j \in N$, then for any non-negative vector $\mathbf{x} \ge \mathbf{0}$, the left-hand side $\sum_{j \in N} y_{rj}x_j + x_{B(r)} \ge 0$ is non-negative while the right-hand side $\bar{b}_r < 0$ is strictly negative! This is an impossible contradiction (equivalent to the Dual objective being unbounded above), proving that the **Primal LP is strictly infeasible ($\mathcal{F}_P = \emptyset$)**.
4. **Entering Variable Selection (Dual Minimum Ratio Test)**: To make the new basic variable in row $r$ positive ($\bar{b}_r^{\text{new}} = \bar{b}_r / y_{rk} > 0$ since $\bar{b}_r < 0$), the pivot element $y_{rk}$ must be **strictly negative ($y_{rk} < 0$)**. Furthermore, after pivoting on $y_{rk} < 0$, the updated net evaluation row entries become:
   $$(z_j - c_j)^{\text{new}} = (z_j - c_j) - \frac{z_k - c_k}{y_{rk}} y_{rj}$$
   To preserve dual feasibility $(z_j - c_j)^{\text{new}} \ge 0$ across all columns $j \in N$ with $y_{rj} < 0$, we must choose the **entering variable $x_k$** via the **Dual Minimum Ratio Test**:
   $$\frac{z_k - c_k}{|y_{rk}|} = \min_{j \in N} \left\{ \frac{z_j - c_j}{|y_{rj}|} : y_{rj} < 0 \right\} = \min_{j \in N} \left\{ \left| \frac{z_j - c_j}{y_{rj}} \right| : y_{rj} < 0 \right\}$$
5. **Gauss–Jordan Pivot**: Pivot on $y_{rk} < 0$ to bring $x_k$ into the basis and expel $x_{B(r)}$. Note that in a maximization problem, each Dual Simplex pivot decreases (tightens) the super-optimal upper bound $Z_0$ monotonically down toward $Z^*$: $Z_{\text{new}} = Z_0 - \frac{\bar{b}_r}{y_{rk}}(z_k - c_k) \le Z_0$.

## 3.6 Post-Optimality Sensitivity Analysis I: Right-Hand-Side Perturbations and Shadow Price Intervals

Once an optimal Basic Feasible Solution $\mathbf{x}_B^* = \mathbf{B}^{-1}\mathbf{b} \ge \mathbf{0}$ with optimal basis $\mathbf{B}$, optimal dual shadow prices $\mathbf{y}^* = (\mathbf{B}^{-1})^T\mathbf{c}_B$, and optimal objective $Z^* = \mathbf{c}_B^T \mathbf{B}^{-1}\mathbf{b}$ has been computed, **Post-Optimality Sensitivity Analysis** investigates how perturbations in the model's exogenous data $(\mathbf{b}, \mathbf{c}, \mathbf{A})$ affect the optimal basis and solution—without resolving the Linear Program from scratch! Everything hinges on the **Fundamental Matrix Invariance Principle**: every entry in the final Simplex tableau is a deterministic function of the optimal basis inverse $\mathbf{B}^{-1}$:

$$\bar{\mathbf{b}} = \mathbf{B}^{-1}\mathbf{b}, \qquad \mathbf{y}_j = \mathbf{B}^{-1}\mathbf{a}_j, \qquad (\mathbf{y}^*)^T = \mathbf{c}_B^T \mathbf{B}^{-1}, \qquad z_j - c_j = \mathbf{c}_B^T \mathbf{B}^{-1}\mathbf{a}_j - c_j, \qquad Z^* = \mathbf{c}_B^T \mathbf{B}^{-1}\mathbf{b}$$

### Perturbations in the Right-Hand-Side Resource Vector ($\mathbf{b} \to \mathbf{b} + \Delta \mathbf{b}$)

Suppose the resource capacity vector $\mathbf{b}$ is perturbed to $\hat{\mathbf{b}} = \mathbf{b} + \Delta \mathbf{b}$ (or a single resource $b_r$ is perturbed to $b_r + \Delta b_r$, so $\Delta \mathbf{b} = \Delta b_r \mathbf{e}_r$). Inspect the fundamental tableau formulas above:
- **Dual Feasibility is Completely Unaffected**: Because $\mathbf{b}$ does not appear anywhere in $z_j - c_j = \mathbf{c}_B^T \mathbf{B}^{-1}\mathbf{a}_j - c_j$, changing $\mathbf{b}$ leaves the entire net evaluation row $z_j - c_j \ge 0$ and the dual shadow prices $\mathbf{y}^* = (\mathbf{B}^{-1})^T\mathbf{c}_B$ **completely unchanged**!
- **Primal Feasibility Condition (Stability Range of the Optimal Basis $\mathbf{B}$)**: The current optimal basis $\mathbf{B}$ remains optimal if and only if the perturbed basic variables remain non-negative:
  $$\hat{\mathbf{x}}_B = \mathbf{B}^{-1}(\mathbf{b} + \Delta \mathbf{b}) = \mathbf{B}^{-1}\mathbf{b} + \mathbf{B}^{-1}\Delta \mathbf{b} = \bar{\mathbf{b}} + \mathbf{B}^{-1}\Delta \mathbf{b} \ge \mathbf{0}$$

Specifically, if a single resource $b_r$ is perturbed by $\Delta b_r$, let $\boldsymbol{\beta}_{*r} = (\beta_{1r}, \beta_{2r}, \dots, \beta_{mr})^T$ denote the $r$-th column of $\mathbf{B}^{-1}$ (which is located directly under the $r$-th initial slack/artificial variable in the final Simplex tableau!). Then the $m$ perturbed basic variables are:

$$\hat{x}_{B(i)} = \bar{b}_i + \beta_{ir} \Delta b_r \ge 0, \qquad i = 1, 2, \dots, m$$

Solving these $m$ linear inequalities for $\Delta b_r$ yields the exact **Feasibility (Allowable) Range for $\Delta b_r$** within which the current basis $\mathbf{B}$ and shadow prices $\mathbf{y}^*$ remain invariant:

$$\max_{i : \beta_{ir} > 0} \left\{ -\frac{\bar{b}_i}{\beta_{ir}} \right\} \le \Delta b_r \le \min_{i : \beta_{ir} < 0} \left\{ -\frac{\bar{b}_i}{\beta_{ir}} \right\}$$

Within this allowable interval $[\Delta b_r^{\min}, \Delta b_r^{\max}]$, the optimal objective value is a strictly linear function of $\Delta b_r$ with slope equal to the $r$-th shadow price $y_r^*$:

$$Z^*(\mathbf{b} + \Delta \mathbf{b}) = \mathbf{c}_B^T \mathbf{B}^{-1}(\mathbf{b} + \Delta \mathbf{b}) = Z^*(\mathbf{b}) + (\mathbf{y}^*)^T \Delta \mathbf{b} = Z^*(\mathbf{b}) + y_r^* \Delta b_r$$

If $\Delta b_r$ exceeds this interval, one or more $\hat{x}_{B(i)}$ become negative while $z_j - c_j \ge 0$ remains satisfied; a single iteration of **Lemke's Dual Simplex Algorithm** (Section 3.5) immediately transitions to the new optimal basis, where the slope $\frac{\partial Z^*}{\partial b_r}$ steps down, making the global value function $Z^*(b_r)$ a **piecewise-linear concave function** of $b_r$!

### Post-Optimality Sensitivity Analysis II: Objective Coefficients, New Activities, and New Constraints

Continuing from the Fundamental Matrix Invariance Principle, we now analyze how perturbations in the objective coefficients $\mathbf{c}$, the introduction of a new structural activity $x_{n+1}$, or the addition of a new constraint row affect the optimal solution.

### 1. Perturbation in a Non-Basic Objective Coefficient ($c_k \to c_k + \Delta c_k, \; k \in N$)

Suppose $x_k$ ($k \in N$) is currently a **non-basic variable** ($x_k^* = 0$) at the optimum, so its current activity level is zero because its unit profit $c_k$ is less than or equal to its imputed resource cost $z_k = (\mathbf{y}^*)^T \mathbf{a}_k$ ($z_k - c_k \ge 0$). Because $k \notin B$, $c_k$ does **not** appear in $\mathbf{c}_B$. Therefore, changing $c_k$ to $c_k + \Delta c_k$ leaves $\mathbf{x}_B^* = \mathbf{B}^{-1}\mathbf{b}$, $\mathbf{y}^* = (\mathbf{B}^{-1})^T\mathbf{c}_B$, $Z^*$, and every other column's $z_j - c_j$ ($j \ne k$) **completely unchanged**! Only the single net evaluation entry for column $k$ changes:

$$(\hat{z}_k - \hat{c}_k) = z_k - (c_k + \Delta c_k) = (z_k - c_k) - \Delta c_k \ge 0 \iff \Delta c_k \le z_k - c_k \iff \hat{c}_k \le z_k$$

Thus, for any non-basic variable $x_k$ ($k \in N$), the optimal solution remains completely invariant for all $\Delta c_k \in (-\infty, \, z_k - c_k]$. Only if $c_k$ increases by more than its reduced cost $z_k - c_k$ does $x_k$ become profitable to enter the basis via a standard Primal Simplex pivot.

### 2. Perturbation in a Basic Objective Coefficient ($c_{B(r)} \to c_{B(r)} + \Delta c_{B(r)}, \; B(r) \in B$)

Suppose $x_{B(r)}$ is the $r$-th **basic variable** ($B(r) \in B$). Perturbing $c_{B(r)}$ by $\Delta c_{B(r)}$ changes the basic cost vector to $\hat{\mathbf{c}}_B = \mathbf{c}_B + \Delta c_{B(r)} \mathbf{e}_r$.
- **Primal Feasibility is Unaffected**: $\mathbf{x}_B^* = \mathbf{B}^{-1}\mathbf{b} \ge \mathbf{0}$ does not depend on $\mathbf{c}$, so the vertex coordinates remain $\bar{\mathbf{b}}$.
- **Dual Feasibility Condition (Optimality Range for $\Delta c_{B(r)}$)**: For every basic variable $j \in B$, $\hat{z}_j - \hat{c}_j = 0$ remains zero. However, for every **non-basic variable** $j \in N$, the imputed cost changes by $\Delta c_{B(r)} y_{rj}$, where $y_{rj}$ is the entry in row $r$ and column $j$ of the final Simplex tableau:
  $$\hat{z}_j - c_j = (z_j - c_j) + y_{rj} \Delta c_{B(r)} \ge 0 \qquad \forall j \in N$$
  Solving this system of inequalities over all non-basic columns $j \in N$ yields the exact **Optimality Range for $\Delta c_{B(r)}$**:
  $$\max_{j \in N : y_{rj} > 0} \left\{ -\frac{z_j - c_j}{y_{rj}} \right\} \le \Delta c_{B(r)} \le \min_{j \in N : y_{rj} < 0} \left\{ -\frac{z_j - c_j}{y_{rj}} \right\}$$
  Within this range, the optimal decision vector $\mathbf{x}^*$ is completely unchanged, while the optimal objective value shifts linearly as $\hat{Z}^* = Z^* + \bar{b}_r \Delta c_{B(r)}$.

### 3. Addition of a New Structural Activity ($x_{n+1}$) and Addition of a New Constraint

- **Pricing a New Activity Column**: Suppose management proposes a new product $x_{n+1} \ge 0$ with unit profit $c_{n+1}$ and resource consumption column $\mathbf{a}_{n+1} \in \mathbb{R}^m$. Using the existing optimal shadow prices $\mathbf{y}^* = (\mathbf{B}^{-1})^T\mathbf{c}_B$, we immediately compute its reduced cost:
  $$z_{n+1} - c_{n+1} = (\mathbf{y}^*)^T \mathbf{a}_{n+1} - c_{n+1}$$
  If $z_{n+1} - c_{n+1} \ge 0$, the new activity's imputed resource cost exceeds or equals its revenue, so $x_{n+1}^* = 0$ and the current optimum is unchanged! If $z_{n+1} - c_{n+1} < 0$, we compute its updated tableau column $\mathbf{y}_{n+1} = \mathbf{B}^{-1}\mathbf{a}_{n+1}$ and pivot $x_{n+1}$ into the basis via the Primal Simplex Method.
- **Appending a New Constraint**: Suppose a new regulatory or technological constraint $\mathbf{a}_{m+1}^T \mathbf{x} \le b_{m+1}$ is added. First, substitute the current optimal vector $\mathbf{x}^*$ directly into the new constraint: if $\mathbf{a}_{m+1}^T \mathbf{x}^* \le b_{m+1}$, the current optimal solution already satisfies the new constraint with slack $s_{m+1}^* = b_{m+1} - \mathbf{a}_{m+1}^T \mathbf{x}^* \ge 0$ and remains globally optimal! If $\mathbf{a}_{m+1}^T \mathbf{x}^* > b_{m+1}$, we append the row $\mathbf{a}_{m+1}^T \mathbf{x} + s_{m+1} = b_{m+1}$ with basic variable $s_{m+1}$ to the final tableau, eliminate the basic variables $\mathbf{x}_B$ from row $m+1$ using the existing tableau rows (which leaves $\bar{b}_{m+1} = b_{m+1} - \mathbf{a}_{m+1}^T \mathbf{x}^* < 0$ while maintaining $z_j - c_j \ge 0$), and apply **Lemke's Dual Simplex Method** to restore primal feasibility!

### Parametric Linear Programming, the 100% Simultaneous Perturbation Rule, and Degenerate Shadow Prices

Single-parameter sensitivity intervals characterize how far an individual resource $b_r$ or individual profit coefficient $c_j$ can move while holding all other parameters fixed *ceteris paribus*. In realistic statistical and econometric environments, however, multiple resource capacities $\mathbf{b} + \Delta\mathbf{b}$ or multiple objective coefficients $\mathbf{c} + \Delta\mathbf{c}$ fluctuate simultaneously due to macroeconomic trends, seasonal shifts, or correlated estimation errors.

### Bradley, Hax, and Magnanti's 100% Rule for Simultaneous Perturbations

Suppose several right-hand-side capacities $b_1, \dots, b_m$ are perturbed simultaneously by increments $\Delta b_1, \dots, \Delta b_m$, where each individual increment $\Delta b_i \ne 0$ has a known maximum allowable increase $\Delta b_i^+ > 0$ and maximum allowable decrease $\Delta b_i^- > 0$ (so its single-parameter feasibility interval is $[b_i - \Delta b_i^-, \, b_i + \Delta b_i^+]$). Define the fractional excursion $r_i \ge 0$ of resource $i$ toward its single-parameter stability boundary by:

$$r_i = \begin{cases} \dfrac{\Delta b_i}{\Delta b_i^+}, & \text{if } \Delta b_i > 0 \\[8pt] \dfrac{-\Delta b_i}{\Delta b_i^-}, & \text{if } \Delta b_i < 0 \\[8pt] 0, & \text{if } \Delta b_i = 0 \end{cases}$$

The **100% Rule for Simultaneous RHS Perturbations** states that if the sum of the percentage excursions across all perturbed resources does not exceed $100\%$:

$$\sum_{i=1}^m r_i \le 1 \quad \left(\text{i.e., } \sum_{i=1}^m 100 r_i\% \le 100\%\right)$$

then the current optimal basis $\mathbf{B}$ and its dual shadow price vector $\mathbf{y}^*$ are **guaranteed to remain valid and optimal**! The proof follows directly from convexity of the non-negative orthant in basis space: the unperturbed vector $\Delta \mathbf{b} = \mathbf{0}$ and the $m$ single-axis boundary vectors $\Delta b_i^+ \mathbf{e}_i$ (or $-\Delta b_i^- \mathbf{e}_i$) all satisfy $\bar{\mathbf{b}} + \mathbf{B}^{-1}\Delta\mathbf{b} \ge \mathbf{0}$; whenever $\sum_{i=1}^m r_i \le 1$, the simultaneous perturbation vector $\Delta\mathbf{b} = \sum_{i=1}^m r_i (\pm \Delta b_i^\pm \mathbf{e}_i) + \left(1 - \sum_{i=1}^m r_i\right)\mathbf{0}$ is a convex combination of feasible perturbation vectors, so $\bar{\mathbf{b}} + \mathbf{B}^{-1}\Delta\mathbf{b} \ge \mathbf{0}$ holds automatically! An identical **100% Rule for Simultaneous Objective Perturbations** guarantees that the current optimal solution $\mathbf{x}^*$ remains optimal whenever the fractional excursions of simultaneously perturbed cost coefficients $\Delta c_j$ sum to at most $100\%$. Note carefully that the 100% Rule is a **sufficient** condition, not a necessary condition: if $\sum r_i > 1$, the basis may still remain optimal if oppositely signed matrix entries $\beta_{ki}\Delta b_i$ cancel each other out, which can always be checked exactly via $\bar{\mathbf{b}} + \mathbf{B}^{-1}\Delta\mathbf{b} \ge \mathbf{0}$.

### Parametric Linear Programming along a Continuous Ray

When parameters vary continuously along a prescribed directional ray $\mathbf{b}(\theta) = \mathbf{b} + \theta \mathbf{d}$ or $\mathbf{c}(\theta) = \mathbf{c} + \theta \mathbf{f}$ as a scalar trade-off parameter $\theta \ge 0$ increases from $0$ to $+\infty$ (as in Markowitz mean-variance-linearized efficient frontier tracing or statistical regularization path tracking), **Parametric Linear Programming** traces the entire piecewise-linear family of optimal bases $\{\mathbf{B}_1, \mathbf{B}_2, \dots, \mathbf{B}_K\}$ across consecutive critical breakpoints $0 = \theta_0 < \theta_1 < \theta_2 < \dots < \theta_K$. Within each interval $\theta \in [\theta_{k-1}, \theta_k]$, the basis $\mathbf{B}_k$ remains constant; at the upper breakpoint $\theta_k$, a basic variable $\bar{b}_r(\theta) = \bar{b}_r + \theta (\mathbf{B}_k^{-1}\mathbf{d})_r$ hits zero (for RHS parameterization) or a reduced cost $z_j(\theta) - c_j(\theta)$ hits zero (for objective parameterization), triggering a single Dual Simplex or Primal Simplex pivot to the adjacent basis $\mathbf{B}_{k+1}$.

### Two-Sided Directional Shadow Prices under Primal Degeneracy

Finally, a subtle theoretical distinction arises when the optimal primal BFS $\mathbf{x}^*$ is **degenerate** ($\bar{b}_i = 0$ for some basic variable). At a degenerate primal vertex, multiple distinct optimal bases $\mathbf{B}^{(1)}, \dots, \mathbf{B}^{(L)}$ represent the same geometric corner $\mathbf{x}^*$, corresponding to **alternative optimal solutions** $\mathbf{y}^{(1)}, \dots, \mathbf{y}^{(L)}$ in the Dual Problem! Consequently, the optimal value function $Z^*(b_r)$ exhibits a **kink** (non-differentiability) at the current capacity $b_r$: the right-hand marginal shadow price (for increasing $b_r$, $\Delta b_r > 0$) equals the **minimum** of $y_r$ over the dual optimal face, $\frac{\partial Z^*}{\partial b_r^+} = \min_{\mathbf{y}^* \in \mathcal{F}_D^*} y_r^*$, whereas the left-hand marginal shadow price (for decreasing $b_r$, $\Delta b_r < 0$) equals the **maximum** of $y_r$ over the dual optimal face, $\frac{\partial Z^*}{\partial b_r^-} = \max_{\mathbf{y}^* \in \mathcal{F}_D^*} y_r^*$.

### Statistical Application: Duality in Quantile Regression and Support Vector Classifiers

In modern mathematical statistics, Linear Programming Duality provides the theoretical bridge between primal residual minimization and dual score-function processes. Consider Roger Koenker and Gilbert Bassett's (1978) **Quantile Regression** estimator for the $\tau$-th conditional quantile ($\tau \in (0, 1)$) of a response vector $\mathbf{y} \in \mathbb{R}^N$ given design matrix $\mathbf{X} \in \mathbb{R}^{N \times p}$, which minimizes the asymmetric tilted absolute loss $\sum_{i=1}^N \rho_\tau(y_i - \mathbf{x}_i^T \boldsymbol{\beta})$. Splitting each residual into positive and negative parts $y_i - \mathbf{x}_i^T\boldsymbol{\beta} = u_i - v_i$ ($u_i, v_i \ge 0$), the Primal Quantile Regression Linear Program is:

$$\text{Minimize } \tau \mathbf{1}_N^T \mathbf{u} + (1 - \tau) \mathbf{1}_N^T \mathbf{v} \quad \text{subject to} \quad \mathbf{X}\boldsymbol{\beta} + \mathbf{I}_N \mathbf{u} - \mathbf{I}_N \mathbf{v} = \mathbf{y}, \quad \boldsymbol{\beta} \in \mathbb{R}^p \text{ free}, \quad \mathbf{u}, \mathbf{v} \ge \mathbf{0}$$

By the asymmetric primal-dual rules of Section 3.1, the $N$ equality constraints correspond to an unrestricted dual vector $\mathbf{d} \in \mathbb{R}^N$, the free variable vector $\boldsymbol{\beta} \in \mathbb{R}^p$ yields $p$ strict dual equality constraints $\mathbf{X}^T\mathbf{d} = \mathbf{0}$, and the non-negative deviation vectors $\mathbf{u}, \mathbf{v} \ge \mathbf{0}$ impose box bounds $-(1-\tau)\mathbf{1}_N \le \mathbf{d} \le \tau \mathbf{1}_N$. Reparameterizing via $\mathbf{a} = \mathbf{d} + (1-\tau)\mathbf{1}_N \in [0, 1]^N$ transforms the Dual of Quantile Regression into the compact bounded-variable maximization problem:

$$\text{Maximize } \mathbf{y}^T \mathbf{a} \quad \text{subject to} \quad \mathbf{X}^T \mathbf{a} = (1 - \tau) \mathbf{X}^T \mathbf{1}_N, \qquad \mathbf{a} \in [0, 1]^N$$

By Complementary Slackness, observations lying strictly above the fitted $\tau$-quantile hyperplane ($u_i^* > 0$) have dual rank score $a_i^* = 1$; observations lying strictly below the hyperplane ($v_i^* > 0$) have dual rank score $a_i^* = 0$; and the $p$ interpolated basic observations lying directly on the hyperplane ($u_i^* = v_i^* = 0$) take fractional dual weights $a_i^* \in (0, 1)$, forming the exact generalization of Hájek's **regression rank-score statistics** used for distribution-free hypothesis testing in linear models!

## Worked Questions and Solutions

### Question 1: Asymmetric Primal-Dual Formulation and Optimal Dual Extraction via Complementary Slackness

Consider the following Primal Linear Programming Problem (P):

$$\text{Maximize } Z = 5x_1 + 12x_2 + 4x_3$$

subject to:

$$\begin{aligned}
x_1 + 2x_2 + x_3 &\le 10 \quad (\text{Constraint 1}) \\
2x_1 - x_2 + 3x_3 &= 8 \quad (\text{Constraint 2}) \\
x_1, x_2, x_3 &\ge 0
\end{aligned}$$

1. Formulate the explicit **Dual Linear Programming Problem (D)** in dual variables $(y_1, y_2)$, specifying the exact sign restriction on each dual variable and the direction of each dual constraint.
2. Suppose it is known that in the optimal primal solution, activities $x_1^* > 0$ and $x_2^* > 0$ are strictly positive while $x_3^* = 0$, and Constraint 1 holds with strict equality ($s_1^* = 0$). Use the primal constraints and the **Complementary Slackness Theorem** to solve algebraically for $(x_1^*, x_2^*, x_3^*)$ and the optimal dual vector $(y_1^*, y_2^*)$ without constructing a Simplex tableau.
3. Verify that $(y_1^*, y_2^*)$ satisfies all dual constraints (including the constraint for $x_3$) and verify Strong Duality $Z^* = W^*$.

### Solution, step 1: Formulate the Asymmetric Dual Problem (D)

Associate dual variable $y_1$ with Constraint 1 ($\le 10$) and dual variable $y_2$ with Constraint 2 ($= 8$). By the Primal-Dual Correspondence Table (Section 3.1):
- Because Primal Constraint 1 is a $\le$ inequality in a maximization problem, $y_1 \ge 0$.
- Because Primal Constraint 2 is a strict equality ($=$), $y_2 \in \mathbb{R}$ is **unrestricted in sign**.
- Because all three primal variables satisfy $x_1, x_2, x_3 \ge 0$, all three dual constraints are $\ge$ inequalities.

Thus, the Dual Problem (D) is:

$$\text{Minimize } W = 10y_1 + 8y_2$$

subject to:

$$\begin{aligned}
y_1 + 2y_2 &\ge 5 \quad (\text{Dual Constraint 1, paired with } x_1) \\
2y_1 - y_2 &\ge 12 \quad (\text{Dual Constraint 2, paired with } x_2) \\
y_1 + 3y_2 &\ge 4 \quad (\text{Dual Constraint 3, paired with } x_3) \\
y_1 &\ge 0, \quad y_2 \in \mathbb{R} \text{ unrestricted}
\end{aligned}$$

### Solution, step 2: Apply Complementary Slackness to solve for primal and dual candidates

First, since $x_3^* = 0$ and Constraint 1 is binding ($s_1^* = 0$), the two primal constraints become a $2 \times 2$ linear system in $(x_1^*, x_2^*)$:

$$\begin{aligned}
x_1^* + 2x_2^* &= 10 \\
2x_1^* - x_2^* &= 8
\end{aligned}$$

Multiplying the second equation by $2$ and adding to the first gives $5x_1^* = 26 \implies x_1^* = \frac{26}{5} = 5.2 > 0$, and $x_2^* = 2\left(\frac{26}{5}\right) - 8 = \frac{12}{5} = 2.4 > 0$. Thus $\mathbf{x}^* = \left(\frac{26}{5}, \frac{12}{5}, 0\right)^T \ge \mathbf{0}$ is primal feasible!

Second, by **Dual Complementary Slackness** ($e_j^* x_j^* = 0$), because $x_1^* = 26/5 > 0$ and $x_2^* = 12/5 > 0$, Dual Constraints 1 and 2 must hold with **strict equality** ($e_1^* = 0$ and $e_2^* = 0$):

$$\begin{aligned}
y_1^* + 2y_2^* &= 5 \\
2y_1^* - y_2^* &= 12
\end{aligned}$$

Multiplying the second equation by $2$ and adding to the first yields $5y_1^* = 29 \implies y_1^* = \frac{29}{5} = 5.8$, and $y_2^* = 2\left(\frac{29}{5}\right) - 12 = -\frac{2}{5} = -0.4$.

### Solution, step 3: Verify Dual Feasibility and Strong Duality Z* = W*

Let us verify that $\mathbf{y}^* = \left(\frac{29}{5}, -\frac{2}{5}\right)^T$ is feasible for Dual Problem (D):
1. Sign restrictions: $y_1^* = \frac{29}{5} \ge 0$ (satisfied) and $y_2^* = -\frac{2}{5} \in \mathbb{R}$ (unrestricted, so negative value is valid!).
2. Dual Constraint 3 (paired with $x_3^* = 0$):
   $$y_1^* + 3y_2^* = \frac{29}{5} + 3\left(-\frac{2}{5}\right) = \frac{23}{5} = 4.6 \ge 4 \implies e_3^* = \frac{23}{5} - 4 = \frac{3}{5} > 0$$
   Dual Constraint 3 is satisfied with positive surplus $e_3^* = 3/5 > 0$, which satisfies $e_3^* x_3^* = (3/5)(0) = 0$.
3. Evaluate Primal and Dual Objectives:
   $$Z^* = 5\left(\frac{26}{5}\right) + 12\left(\frac{12}{5}\right) + 4(0) = \frac{130 + 144}{5} = \frac{274}{5} = 54.8$$
   $$W^* = 10\left(\frac{29}{5}\right) + 8\left(-\frac{2}{5}\right) = \frac{290 - 16}{5} = \frac{274}{5} = 54.8$$
Because $Z^* = W^* = 54.8$ and all primal, dual, and complementary slackness conditions hold, $\mathbf{x}^* = (5.2, 2.4, 0)^T$ and $\mathbf{y}^* = (5.8, -0.4)^T$ are proven globally optimal.

### Question 2: Execution of Lemke's Dual Simplex Algorithm on a Minimization System

Solve the following Linear Programming Problem using **Lemke's Dual Simplex Algorithm** (without introducing any artificial variables):

$$\text{Minimize } W = 3x_1 + 2x_2 + 4x_3$$

subject to:

$$\begin{aligned}
2x_1 + x_2 + 3x_3 &\ge 6 \\
3x_1 + 3x_2 + 5x_3 &\ge 12 \\
x_1, x_2, x_3 &\ge 0
\end{aligned}$$

1. Convert the objective to maximization ($Z = -W$) and multiply both $\ge$ constraints by $-1$ to obtain $\le$ inequalities with negative right-hand sides and non-negative slack variables $s_1, s_2 \ge 0$.
2. Verify that the initial tableau at the origin is **dual feasible** ($z_j - c_j \ge 0$) but **primal infeasible** ($\bar{\mathbf{b}} < \mathbf{0}$).
3. Execute Dual Simplex pivots step-by-step using the most negative RHS leaving rule and the Dual Minimum Ratio Test until primal feasibility and global optimality are achieved.

### Solution, step 1: Standardize for Dual Simplex and construct Initial Tableau

Set $\max Z = -W = -3x_1 - 2x_2 - 4x_3$. Multiply both $\ge$ inequalities by $-1$ and add slack variables $s_1, s_2 \ge 0$:

$$\begin{aligned}
-2x_1 - x_2 - 3x_3 + s_1 &= -6 \\
-3x_1 - 3x_2 - 5x_3 + s_2 &= -12
\end{aligned}$$

With initial basis $B_0 = \{s_1, s_2\}$ and $\mathbf{c}_{B_0} = (0, 0)^T$, the net evaluations are $z_1 - c_1 = 3 \ge 0$, $z_2 - c_2 = 2 \ge 0$, $z_3 - c_3 = 4 \ge 0$. Because $z_j - c_j \ge 0$ for all columns, the initial tableau is **Dual Feasible**, while $\bar{b}_1 = -6 < 0$ and $\bar{b}_2 = -12 < 0$ are **Primal Infeasible**:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Basic Var</th><th>$c_B$</th><th>$x_1$ ($-3$)</th><th>$x_2$ ($-2$)</th><th>$x_3$ ($-4$)</th><th>$s_1$ ($0$)</th><th>$s_2$ ($0$)</th><th>RHS ($\bar{b}_i$)</th></tr></thead><tbody><tr><td>$s_1$</td><td>$0$</td><td>$-2$</td><td>$-1$</td><td>$-3$</td><td>$1$</td><td>$0$</td><td>$-6$</td></tr><tr><td>$s_2$ (Leave)</td><td>$0$</td><td>$-3$</td><td>$\mathbf{-3}^*$</td><td>$-5$</td><td>$0$</td><td>$1$</td><td>$\mathbf{-12}$ (Most Neg)</td></tr><tr><td>$z_j - c_j$</td><td>—</td><td>$3$</td><td>$2$</td><td>$4$</td><td>$0$</td><td>$0$</td><td>$Z_0 = 0$</td></tr><tr><td>Dual Ratio $|(z_j-c_j)/y_{2j}|$</td><td>—</td><td>$3/3 = 1$</td><td>$\mathbf{2/3 \approx 0.667}$ (Enter)</td><td>$4/5 = 0.8$</td><td>—</td><td>—</td><td>—</td></tr></tbody></table></div>

### Solution, step 2: Dual Simplex Iteration 1: Pivot to replace s_2 with x_2

- **Leaving Variable**: Row 2 has the most negative RHS ($\bar{b}_2 = -12 < -6$), so $s_2$ leaves the basis.
- **Entering Variable**: Applying the Dual Minimum Ratio Test across negative entries $y_{2j} < 0$ in Row 2:
  $$\min \left\{ \left|\frac{3}{-3}\right|, \, \left|\frac{2}{-3}\right|, \, \left|\frac{4}{-5}\right| \right\} = \min \left\{ 1, \, \frac{2}{3}, \, \frac{4}{5} \right\} = \frac{2}{3} \quad (\text{Column } x_2)$$
  Thus $x_2$ enters the basis with pivot element $y_{22} = -3$. Dividing Row 2 by $-3$ and applying $R_1 \leftarrow R_1 + R_2^{\text{new}}$, $R_z \leftarrow R_z - 2R_2^{\text{new}}$ yields Tableau 1:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Basic Var</th><th>$c_B$</th><th>$x_1$ ($-3$)</th><th>$x_2$ ($-2$)</th><th>$x_3$ ($-4$)</th><th>$s_1$ ($0$)</th><th>$s_2$ ($0$)</th><th>RHS ($\bar{b}_i$)</th></tr></thead><tbody><tr><td>$s_1$ (Leave)</td><td>$0$</td><td>$-1$</td><td>$0$</td><td>$\mathbf{-4/3}^*$</td><td>$1$</td><td>$-1/3$</td><td>$\mathbf{-2}$ (Neg)</td></tr><tr><td>$x_2$</td><td>$-2$</td><td>$1$</td><td>$1$</td><td>$5/3$</td><td>$0$</td><td>$-1/3$</td><td>$4$</td></tr><tr><td>$z_j - c_j$</td><td>—</td><td>$1$</td><td>$0$</td><td>$2/3$</td><td>$0$</td><td>$2/3$</td><td>$Z_1 = -8$</td></tr><tr><td>Dual Ratio $|(z_j-c_j)/y_{1j}|$</td><td>—</td><td>$1/1 = 1$</td><td>—</td><td>$\mathbf{(2/3)/(4/3) = 0.5}$ (Enter)</td><td>—</td><td>$(2/3)/(1/3) = 2$</td><td>—</td></tr></tbody></table></div>

### Solution, step 3: Dual Simplex Iteration 2: Pivot to replace s_1 with x_3 and Verify Optimality

In Tableau 1, Row 1 still has a negative right-hand side ($\bar{b}_1 = -2 < 0$), so $s_1$ leaves the basis. Checking the negative entries $y_{1j} < 0$ in Row 1 ($x_1: -1$, $x_3: -4/3$, $s_2: -1/3$), the Dual Minimum Ratio Test gives:

$$\min \left\{ \frac{1}{1}, \, \frac{2/3}{4/3}, \, \frac{2/3}{1/3} \right\} = \min \{ 1, \, 0.5, \, 2 \} = 0.5 \quad (\text{Column } x_3)$$

Thus $x_3$ enters the basis with pivot element $y_{13} = -4/3$. Multiply Row 1 by $-3/4$ and eliminate $x_3$ from Row 2 and $R_z$:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Basic Var</th><th>$c_B$</th><th>$x_1$ ($-3$)</th><th>$x_2$ ($-2$)</th><th>$x_3$ ($-4$)</th><th>$s_1$ ($0$)</th><th>$s_2$ ($0$)</th><th>RHS ($\bar{b}_i$)</th></tr></thead><tbody><tr><td>$x_3$</td><td>$-4$</td><td>$3/4$</td><td>$0$</td><td>$1$</td><td>$-3/4$</td><td>$1/4$</td><td>$3/2 = 1.5$</td></tr><tr><td>$x_2$</td><td>$-2$</td><td>$-1/4$</td><td>$1$</td><td>$0$</td><td>$5/4$</td><td>$-3/4$</td><td>$3/2 = 1.5$</td></tr><tr><td>$z_j - c_j$</td><td>—</td><td>$1/2$</td><td>$0$</td><td>$0$</td><td>$1/2$</td><td>$1/2$</td><td>$Z^* = -9$</td></tr></tbody></table></div>

Now all basic right-hand sides are strictly positive ($\bar{b}_1 = 3/2 > 0, \bar{b}_2 = 3/2 > 0$) and all $z_j - c_j \ge 0$! The global optimum is $x_1^* = 0, x_2^* = 1.5, x_3^* = 1.5$, with minimum objective $W^* = -Z^* = 3(0) + 2(1.5) + 4(1.5) = 9$.

### Question 3: Comprehensive Post-Optimality Sensitivity Analysis: Shadow Prices, RHS Ranges, Cost Ranges, and New Activity Pricing

A biostatistical assay laboratory produces two diagnostic reagent kits ($x_1, x_2$) using two specialized resources: Automated Pipetting Hours (Resource 1, capacity $b_1 = 60$) and Mass Spectrometry Hours (Resource 2, capacity $b_2 = 48$). The Linear Program is:

$$\text{Maximize } Z = 40x_1 + 30x_2 \quad \text{subject to} \quad \begin{cases} 2x_1 + x_2 + s_1 = 60 \\ x_1 + 2x_2 + s_2 = 48 \end{cases}, \quad x_1, x_2, s_1, s_2 \ge 0$$

At the optimal Basic Feasible Solution with basis $B = \{x_1, x_2\}$, the final Simplex tableau is:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Basic Var</th><th>$c_B$</th><th>$x_1$ ($40$)</th><th>$x_2$ ($30$)</th><th>$s_1$ ($0$)</th><th>$s_2$ ($0$)</th><th>RHS ($\bar{b}_i$)</th></tr></thead><tbody><tr><td>$x_1$</td><td>$40$</td><td>$1$</td><td>$0$</td><td>$2/3$</td><td>$-1/3$</td><td>$24$</td></tr><tr><td>$x_2$</td><td>$30$</td><td>$0$</td><td>$1$</td><td>$-1/3$</td><td>$2/3$</td><td>$12$</td></tr><tr><td>$z_j - c_j$</td><td>—</td><td>$0$</td><td>$0$</td><td>$50/3$</td><td>$20/3$</td><td>$Z^* = 1320$</td></tr></tbody></table></div>

1. Extract the basis inverse $\mathbf{B}^{-1}$ and optimal dual shadow prices $(y_1^*, y_2^*)$ directly from the final tableau, and compute the exact **allowable feasibility ranges** for $b_1$ and $b_2$ within which the current basis remains optimal.
2. Compute the exact **allowable optimality ranges** for the unit profit coefficients $c_1$ (keeping $c_2 = 30$ fixed) and $c_2$ (keeping $c_1 = 40$ fixed) such that $(x_1^*, x_2^*) = (24, 12)$ remains optimal.
3. The laboratory considers introducing a third reagent kit $x_3 \ge 0$ requiring $3$ hours of Resource 1 and $2$ hours of Resource 2 with unit profit $c_3 = 60$. Determine via dual shadow pricing whether $x_3$ should be produced; if so, find the new optimal solution.

### Solution, step 1: Extract B^-1, Shadow Prices, and Right-Hand-Side Feasibility Ranges

From the columns under the initial identity slack variables $(s_1, s_2)$ in the final tableau:

$$\mathbf{B}^{-1} = \begin{pmatrix} 2/3 & -1/3 \\ -1/3 & 2/3 \end{pmatrix}, \qquad \mathbf{y}^* = \begin{pmatrix} y_1^* \\ y_2^* \end{pmatrix} = \begin{pmatrix} z_{s_1} - c_{s_1} \\ z_{s_2} - c_{s_2} \end{pmatrix} = \begin{pmatrix} 50/3 \\ 20/3 \end{pmatrix} \approx \begin{pmatrix} 16.67 \\ 6.67 \end{pmatrix}$$

- **Feasibility Range for $b_1 = 60 + \Delta b_1$**: Using column 1 of $\mathbf{B}^{-1}$, $\boldsymbol{\beta}_{*1} = (2/3, -1/3)^T$:
  $$\begin{aligned}
  \hat{x}_1 &= 24 + \frac{2}{3} \Delta b_1 \ge 0 \implies \Delta b_1 \ge -36 \\
  \hat{x}_2 &= 12 - \frac{1}{3} \Delta b_1 \ge 0 \implies \Delta b_1 \le +36
  \end{aligned}$$
  Thus $-36 \le \Delta b_1 \le 36$, giving the allowable capacity interval **$b_1 \in [24, \, 96]$**.
- **Feasibility Range for $b_2 = 48 + \Delta b_2$**: Using column 2 of $\mathbf{B}^{-1}$, $\boldsymbol{\beta}_{*2} = (-1/3, 2/3)^T$:
  $$\begin{aligned}
  \hat{x}_1 &= 24 - \frac{1}{3} \Delta b_2 \ge 0 \implies \Delta b_2 \le +72 \\
  \hat{x}_2 &= 12 + \frac{2}{3} \Delta b_2 \ge 0 \implies \Delta b_2 \ge -18
  \end{aligned}$$
  Thus $-18 \le \Delta b_2 \le 72$, giving the allowable capacity interval **$b_2 \in [30, \, 120]$**.

### Solution, step 2: Compute Optimality Ranges for Basic Objective Coefficients c_1 and c_2

- **Allowable Range for $c_1 = 40 + \Delta c_1$** (Row $r = 1$, non-basic columns $N = \{s_1, s_2\}$ with $y_{1, s_1} = 2/3, y_{1, s_2} = -1/3$):
  $$\begin{aligned}
  \hat{z}_{s_1} - c_{s_1} &= \frac{50}{3} + \frac{2}{3}\Delta c_1 \ge 0 \implies \Delta c_1 \ge -25 \\
  \hat{z}_{s_2} - c_{s_2} &= \frac{20}{3} - \frac{1}{3}\Delta c_1 \ge 0 \implies \Delta c_1 \le +20
  \end{aligned}$$
  Thus $-25 \le \Delta c_1 \le 20$, giving **$c_1 \in [15, \, 60]$**.
- **Allowable Range for $c_2 = 30 + \Delta c_2$** (Row $r = 2$, non-basic columns $N = \{s_1, s_2\}$ with $y_{2, s_1} = -1/3, y_{2, s_2} = 2/3$):
  $$\begin{aligned}
  \hat{z}_{s_1} - c_{s_1} &= \frac{50}{3} - \frac{1}{3}\Delta c_2 \ge 0 \implies \Delta c_2 \le +50 \\
  \hat{z}_{s_2} - c_{s_2} &= \frac{20}{3} + \frac{2}{3}\Delta c_2 \ge 0 \implies \Delta c_2 \ge -10
  \end{aligned}$$
  Thus $-10 \le \Delta c_2 \le 50$, giving **$c_2 \in [20, \, 80]$**. (Notice geometrically that both intervals correspond to the objective slope ratio $1/2 \le c_1 / c_2 \le 2$, matching the slopes of the two binding constraints!)

### Solution, step 3: Evaluate New Activity x_3 via Shadow Pricing and Update Optimum

For the proposed reagent kit $x_3$ with consumption vector $\mathbf{a}_3 = (3, 2)^T$ and unit profit $c_3 = 60$, we compute its imputed resource cost $z_3 = (\mathbf{y}^*)^T \mathbf{a}_3$ and reduced cost $z_3 - c_3$:

$$z_3 - c_3 = \begin{pmatrix} 50/3 & 20/3 \end{pmatrix} \begin{pmatrix} 3 \\ 2 \end{pmatrix} - 60 = \left(50 + \frac{40}{3}\right) - 60 = \frac{190}{3} - 60 = \frac{10}{3} \approx +3.333 > 0$$

Because $z_3 - c_3 = +10/3 > 0$, the imputed value of the resources consumed by one unit of $x_3$ ($\frac{190}{3} \approx \$63.33$) exceeds its unit revenue ($\$60.00$). Therefore, **kit $x_3$ should NOT be produced ($x_3^* = 0$)** unless its unit profit $c_3$ is raised above the threshold $z_3 = \frac{190}{3} \approx \$63.33$, and the current optimal solution $(x_1^*, x_2^*) = (24, 12)$ with $Z^* = 1320$ remains globally optimal.
