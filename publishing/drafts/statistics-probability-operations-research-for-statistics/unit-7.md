# Unit 7: Game Theory, Saddle Points, Mixed Strategies & Minimax Linear Programming Equivalence

## 7.1 Two-Person Zero-Sum Matrix Games, Strategic Normal Form, and Rational Minimax-Maximin Criteria

Mathematical **Game Theory**, founded as a rigorous axiomatic discipline by John von Neumann in his landmark 1928 paper *Zur Theorie der Gesellschaftsspiele* and expanded in the monumental 1944 treatise *Theory of Games and Economic Behavior* co-authored with Oskar Morgenstern, analyzes multiperson decision situations in which the payoff received by each rational decision-maker depends not only on their own chosen action and exogenous stochastic states, but also on the strategic actions selected by competing rational agents with conflicting or partially aligned objectives. Within Operations Research and Mathematical Statistics (Course Stat H-205), **Two-Person Zero-Sum Matrix Games** occupy a foundational position for two intertwined reasons: first, as established by George Dantzig and John von Neumann in 1947, solving any finite two-person zero-sum matrix game is mathematically isomorphic to solving a pair of **Primal-Dual Linear Programming Problems**; second, as proven by Abraham Wald in *Statistical Decision Functions* (1950), frequentist minimax statistical estimation and Neyman–Pearson hypothesis testing are formally equivalent to a two-person zero-sum game played between the **Statistician** (who selects a measurable decision rule $\delta(\mathbf{X})$ to minimize risk) and **Nature** (who selects an adversarial prior distribution $\pi(\theta)$ over the parameter space $\Theta$ to maximize expected risk).

### Strategic Normal Form and the Zero-Sum Payoff Identity

A finite two-person zero-sum game in strategic (normal) form is defined by a triplet $(\mathcal{S}_I, \mathcal{S}_{II}, \mathbf{A})$:
1. **Row Player $I$ (The Maximizer)**: Possesses a finite set of $m$ pure strategies $\mathcal{S}_I = \{\alpha_1, \alpha_2, \dots, \alpha_m\}$, corresponding to the $m$ rows of an $m \times n$ matrix.
2. **Column Player $II$ (The Minimizer)**: Possesses a finite set of $n$ pure strategies $\mathcal{S}_{II} = \{\beta_1, \beta_2, \dots, \beta_n\}$, corresponding to the $n$ columns of the matrix.
3. **Payoff Matrix $\mathbf{A} = [a_{ij}] \in \mathbb{R}^{m \times n}$**: By universal convention in Operations Research, the matrix $\mathbf{A}$ is written from the perspective of **Player $I$**. When Player $I$ selects row strategy $\alpha_i$ ($i \in \{1, \dots, m\}$) and Player $II$ simultaneously (and without prior knowledge of Player $I$'s choice) selects column strategy $\beta_j$ ($j \in \{1, \dots, n\}$), Player $I$ receives the scalar utility payoff $u_I(\alpha_i, \beta_j) = a_{ij}$ and Player $II$ receives the utility payoff $u_{II}(\alpha_i, \beta_j) = -a_{ij}$.

The game is **zero-sum** (or strictly competitive) because the algebraic sum of the payoffs to the two players equals zero identically across every possible outcome cell $(i, j)$:

$$u_I(\alpha_i, \beta_j) + u_{II}(\alpha_i, \beta_j) = a_{ij} + (-a_{ij}) = 0 \qquad \forall i \in \{1,\dots,m\}, \; j \in \{1,\dots,n\}$$

Consequently, $a_{ij} > 0$ represents a net gain of $a_{ij}$ utility units paid by Player $II$ to Player $I$, whereas $a_{ij} < 0$ represents a net loss of $|a_{ij}|$ paid by Player $I$ to Player $II$. More generally, any **constant-sum game** in which $u_I(\alpha_i, \beta_j) + u_{II}(\alpha_i, \beta_j) = K$ for a fixed constant $K \in \mathbb{R}$ (such as two competing firms splitting a fixed $100\%$ market share) is strategically identical to a zero-sum game via the affine utility shift $\tilde{u}_{II} = u_{II} - K = -u_I$.

### Wald's Conservative Security Levels: Maximin and Minimax Pure Criteria

How do two rational, mutually distrustful adversaries evaluate pure strategies in $\mathbf{A}$ when each assumes the opponent will act as intelligently and malevolently as possible?
- **Player $I$'s Security Level and Maximin Pure Strategy**: If Player $I$ selects row $i$, the worst-case (minimum) payoff Player $I$ could possibly receive across all columns $j \in \{1, \dots, n\}$ that Player $II$ might choose is the **row minimum** $\min_{1 \le j \le n} a_{ij}$. To guarantee the largest possible floor (security level) regardless of Player $II$'s response, a conservative Player $I$ maximizes this worst-case minimum over all rows $i \in \{1, \dots, m\}$, defining the **Lower Value of the Game ($\underline{v}$)**:
  $$\underline{v} = \max_{1 \le i \le m} \left( \min_{1 \le j \le n} a_{ij} \right)$$
  Any row strategy $\alpha_{i^*}$ achieving $\underline{v}$ is called a **maximin pure strategy** for Player $I$; by playing $\alpha_{i^*}$, Player $I$ is guaranteed to win **at least $\underline{v}$** no matter what column Player $II$ plays.
- **Player $II$'s Security Ceiling and Minimax Pure Strategy**: Symmetrically, if Player $II$ selects column $j$, the worst-case (maximum) loss Player $II$ could suffer across all rows $i \in \{1, \dots, m\}$ is the **column maximum** $\max_{1 \le i \le m} a_{ij}$. To ensure the smallest possible ceiling on maximum loss, Player $II$ minimizes this maximum loss over all columns $j \in \{1, \dots, n\}$, defining the **Upper Value of the Game ($\overline{v}$)**:
  $$\overline{v} = \min_{1 \le j \le n} \left( \max_{1 \le i \le m} a_{ij} \right)$$
  Any column strategy $\beta_{j^*}$ achieving $\overline{v}$ is called a **minimax pure strategy** for Player $II$; by playing $\beta_{j^*}$, Player $II$ is guaranteed to lose **at most $\overline{v}$** no matter what row Player $I$ plays.

### Lemma 7.1 (The Fundamental Maximin–Minimax Inequality):
For any real $m \times n$ matrix $\mathbf{A} = [a_{ij}] \in \mathbb{R}^{m \times n}$, the lower value never exceeds the upper value:

$$\underline{v} = \max_{1 \le i \le m} \min_{1 \le j \le n} a_{ij} \le \min_{1 \le j \le n} \max_{1 \le i \le m} a_{ij} = \overline{v}$$

#### Proof:
For every specific pair of indices $(i_0, j_0) \in \{1,\dots,m\} \times \{1,\dots,n\}$, the entry $a_{i_0 j_0}$ is at least the minimum of row $i_0$ and at most the maximum of column $j_0$:

$$\min_{1 \le j \le n} a_{i_0 j} \le a_{i_0 j_0} \le \max_{1 \le i \le m} a_{i j_0}$$

Because the left-hand side depends only on $i_0$ and the right-hand side depends only on $j_0$, this inequality holds for every $i_0$ and every $j_0$. Taking the maximum over $i_0 \in \{1, \dots, m\}$ on the left and the minimum over $j_0 \in \{1, \dots, n\}$ on the right yields $\underline{v} = \max_{i_0} \min_j a_{i_0 j} \le \min_{j_0} \max_i a_{i j_0} = \overline{v}$.

## 7.2 Saddle-Point Equilibria in Pure Strategies and Iterative Elimination of Dominated Strategies

When the weak inequality $\underline{v} \le \overline{v}$ of Lemma 7.1 holds with **strict equality** ($\underline{v} = \overline{v} = v$), the conservative security levels of Player $I$ and Player $II$ meet at a single common value $v$, and the game is said to be **strictly determined** (solvable in pure strategies).

### Saddle Points of Payoff Matrices

An entry $(i^*, j^*)$ of the payoff matrix $\mathbf{A} = [a_{ij}]$ is defined as a **saddle point** (or pure-strategy Nash equilibrium) of $\mathbf{A}$ if $a_{i^* j^*}$ is simultaneously the **minimum element in its row $i^*$** and the **maximum element in its column $j^*$**:

$$a_{i j^*} \le a_{i^* j^*} \le a_{i^* j} \qquad \forall i \in \{1, \dots, m\}, \quad \forall j \in \{1, \dots, n\}$$

The metaphor of a horse's saddle (or hyperbolic paraboloid $z = y^2 - x^2$) is exact: along the north-south direction (changing rows $i$ within column $j^*$), $(i^*, j^*)$ sits at the highest peak of the pass, whereas along the east-west direction (changing columns $j$ within row $i^*$), $(i^*, j^*)$ sits at the lowest trough! Notice the stability of a saddle point against unilateral espionage: even if Player $I$ announces in advance that row $i^*$ will be played, Player $II$'s best response to minimize loss in row $i^*$ is still column $j^*$ ($a_{i^* j^*} = \min_j a_{i^* j}$); symmetrically, even if Player $II$ announces column $j^*$ in advance, Player $I$'s best response to maximize gain in column $j^*$ is still row $i^*$ ($a_{i^* j^*} = \max_i a_{i j^*}$). Neither player has any unilateral incentive to deviate!

### Theorem 7.1 (Necessary and Sufficient Condition for Saddle Points and Rectangular Interchangeability):
1. A matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$ possesses a saddle point $(i^*, j^*)$ **if and only if** its lower value equals its upper value: $\underline{v} = \overline{v} = v = a_{i^* j^*}$.
2. **Rectangular (Interchangeability) Property of Multiple Saddle Points**: If $(i_1, j_1)$ and $(i_2, j_2)$ are both saddle points of $\mathbf{A}$, then the cross-paired cells $(i_1, j_2)$ and $(i_2, j_1)$ are **also saddle points** of $\mathbf{A}$, and all four cells share the exact same game value:
   $$a_{i_1 j_1} = a_{i_2 j_2} = a_{i_1 j_2} = a_{i_2 j_1} = v$$

#### Proof:
First, if $(i^*, j^*)$ is a saddle point, then $\overline{v} = \min_j \max_i a_{ij} \le \max_i a_{i j^*} = a_{i^* j^*} = \min_j a_{i^* j} \le \max_i \min_j a_{ij} = \underline{v}$; combining $\overline{v} \le \underline{v}$ with Lemma 7.1 ($\underline{v} \le \overline{v}$) forces $\underline{v} = \overline{v} = a_{i^* j^*}$. Conversely, if $\underline{v} = \overline{v} = v$, let $i^*$ achieve $\max_i \min_j a_{ij} = \underline{v}$ and let $j^*$ achieve $\min_j \max_i a_{ij} = \overline{v}$. Then for all $i$ and $j$: $a_{i j^*} \le \max_k a_{k j^*} = \overline{v} = \underline{v} = \min_l a_{i^* l} \le a_{i^* j}$. Setting $i = i^*$ and $j = j^*$ shows $a_{i^* j^*} = v$ and $a_{i j^*} \le a_{i^* j^*} \le a_{i^* j}$ for all $i, j$.
Second, if $(i_1, j_1)$ and $(i_2, j_2)$ are both saddle points, then by row-minimality and column-maximality:

$$a_{i_1 j_1} \le a_{i_1 j_2} \le a_{i_2 j_2} \le a_{i_2 j_1} \le a_{i_1 j_1}$$

Since the first and last terms are identical ($a_{i_1 j_1}$), all four entries must be equal to $v$, and both $(i_1, j_2)$ and $(i_2, j_1)$ satisfy the saddle-point inequalities.

### Iterative Elimination of Dominated Strategies (Dominance Reduction Rules)

Before solving a large $m \times n$ matrix game analytically or via Linear Programming, its dimension can frequently be reduced dramatically by deleting rows and columns that a rational player would never need to use—a procedure known as **Iterative Elimination of Dominated Strategies (IEDS)**:

1. **Row Dominance Rule (Player $I$ Maximizes)**: Row $r$ is **dominated** by row $i$ (or by a convex combination of rows $\sum_{k \ne r} \lambda_k \mathbf{a}_{k*}$ with $\lambda_k \ge 0, \sum \lambda_k = 1$) if every entry in row $r$ is **less than or equal to** the corresponding entry in row $i$:
   $$a_{rj} \le a_{ij} \quad \forall j \in \{1, \dots, n\} \qquad \left(\text{or } a_{rj} \le \sum_{k \ne r} \lambda_k a_{kj} \quad \forall j\right)$$
   Because Player $I$ seeks to maximize payoff, playing row $i$ (or the mixed combination $\boldsymbol{\lambda}$) yields at least as large a payoff as row $r$ in every column $j$. Therefore, **dominated row $r$ can be deleted from $\mathbf{A}$** without altering the value of the game!
2. **Column Dominance Rule (Player $II$ Minimizes)**: Column $s$ is **dominated** by column $j$ (or by a convex combination of columns $\sum_{l \ne s} \mu_l \mathbf{a}_{*l}$ with $\mu_l \ge 0, \sum \mu_l = 1$) if every entry in column $s$ is **greater than or equal to** the corresponding entry in column $j$:
   $$a_{is} \ge a_{ij} \quad \forall i \in \{1, \dots, m\} \qquad \left(\text{or } a_{is} \ge \sum_{l \ne s} \mu_l a_{il} \quad \forall i\right)$$
   Because Player $II$ seeks to minimize loss, column $s$ inflicts a loss at least as large as column $j$ in every row $i$. Therefore, **dominated (high-loss) column $s$ can be deleted from $\mathbf{A}$**! Notice that deleting a row may create a newly dominated column, and deleting a column may create a newly dominated row, allowing alternating row-and-column reductions.

## 7.3 Mixed Strategies, Bilinear Expected Payoffs, and John von Neumann's Minimax Theorem

What happens when the strict inequality $\underline{v} < \overline{v}$ holds, so that the payoff matrix $\mathbf{A}$ possesses **no saddle point in pure strategies**? Consider the classic $2 \times 2$ **Matching Pennies** game $\mathbf{A} = \begin{pmatrix} +1 & -1 \\ -1 & +1 \end{pmatrix}$, where $\underline{v} = -1 < +1 = \overline{v}$. If either player adopts any deterministic pure strategy, the opponent can exploit that predictability to inflict a loss of $-1$. To protect against exploitation while maximizing expected utility, each player must **randomize** their choice of pure strategies according to an optimal probability distribution—termed a **Mixed Strategy**.

### Probability Simplices and the Expected Payoff Bilinear Form

- A **mixed strategy for Player $I$** is a probability vector $\mathbf{x} = (x_1, x_2, \dots, x_m)^T$ residing in the $(m-1)$-dimensional **unit probability simplex** $\Delta_{m-1} \subseteq \mathbb{R}_+^m$:
  $$\Delta_{m-1} = \left\{ \mathbf{x} \in \mathbb{R}^m : \sum_{i=1}^m x_i = \mathbf{1}_m^T \mathbf{x} = 1, \quad x_i \ge 0 \;\; \forall i = 1, \dots, m \right\}$$
  where $x_i = \mathbb{P}(\text{Player } I \text{ selects row } \alpha_i)$. Notice that the $m$ pure strategies $\alpha_1, \dots, \alpha_m$ correspond exactly to the $m$ standard unit extreme vertices $\mathbf{e}_1, \dots, \mathbf{e}_m$ of the simplex $\Delta_{m-1}$.
- Symmetrically, a **mixed strategy for Player $II$** is a probability vector $\mathbf{y} = (y_1, y_2, \dots, y_n)^T$ residing in the $(n-1)$-dimensional probability simplex $\Delta_{n-1} \subseteq \mathbb{R}_+^n$:
  $$\Delta_{n-1} = \left\{ \mathbf{y} \in \mathbb{R}^n : \sum_{j=1}^n y_j = \mathbf{1}_n^T \mathbf{y} = 1, \quad y_j \ge 0 \;\; \forall j = 1, \dots, n \right\}$$
  where $y_j = \mathbb{P}(\text{Player } II \text{ selects column } \beta_j)$.

Because Player $I$ and Player $II$ randomize independently, the joint probability that cell $(i, j)$ occurs is $x_i y_j$. Therefore, the **Expected Payoff $E(\mathbf{x}, \mathbf{y})$** to Player $I$ (and expected loss to Player $II$) is the **bilinear quadratic form**:

$$E(\mathbf{x}, \mathbf{y}) = \sum_{i=1}^m \sum_{j=1}^n x_i a_{ij} y_j = \mathbf{x}^T \mathbf{A} \mathbf{y}$$

### Simplification of Worst-Case Mixed Security Levels to Finite Pure Responses

Suppose Player $I$ commits to a mixed strategy $\mathbf{x} \in \Delta_{m-1}$. What is the worst-case (minimum) expected payoff $\min_{\mathbf{y} \in \Delta_{n-1}} \mathbf{x}^T\mathbf{A}\mathbf{y}$ that Player $II$ can force upon Player $I$? Notice that for fixed $\mathbf{x}$, $E(\mathbf{x}, \mathbf{y}) = \sum_{j=1}^n (\mathbf{x}^T \mathbf{a}_{*j}) y_j$ is a **linear function (convex combination)** of the $n$ pure-column expected payoffs $\mathbf{x}^T\mathbf{a}_{*j}$ over the simplex $\mathbf{y} \in \Delta_{n-1}$! By the Fundamental Theorem of Linear Programming (Unit 1), the minimum of a linear function over the probability simplex $\Delta_{n-1}$ occurs at one of its $n$ extreme vertices $\mathbf{y} = \mathbf{e}_j$ (pure column strategies $j \in \{1,\dots,n\}$):

$$\min_{\mathbf{y} \in \Delta_{n-1}} \mathbf{x}^T \mathbf{A} \mathbf{y} = \min_{1 \le j \le n} \left( \mathbf{x}^T \mathbf{a}_{*j} \right) = \min_{1 \le j \le n} \left( \sum_{i=1}^m a_{ij} x_i \right)$$

and symmetrically, for fixed $\mathbf{y} \in \Delta_{n-1}$, Player $II$'s maximum expected loss occurs against one of Player $I$'s $m$ pure row strategies $i \in \{1, \dots, m\}$:

$$\max_{\mathbf{x} \in \Delta_{m-1}} \mathbf{x}^T \mathbf{A} \mathbf{y} = \max_{1 \le i \le m} \left( \mathbf{a}_{i*} \mathbf{y} \right) = \max_{1 \le i \le m} \left( \sum_{j=1}^n a_{ij} y_j \right)$$

### Theorem 7.2 (John von Neumann's Fundamental Minimax Theorem, 1928):
For every finite $m \times n$ matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$, the mixed-strategy maximin value for Player $I$ and the mixed-strategy minimax value for Player $II$ both exist (since $\Delta_{m-1}$ and $\Delta_{n-1}$ are non-empty compact convex polytopes and $\mathbf{x} \mapsto \min_j \mathbf{x}^T\mathbf{a}_{*j}$ is continuous) and are **strictly equal**:

$$v_I = \max_{\mathbf{x} \in \Delta_{m-1}} \min_{\mathbf{y} \in \Delta_{n-1}} \mathbf{x}^T \mathbf{A} \mathbf{y} = \min_{\mathbf{y} \in \Delta_{n-1}} \max_{\mathbf{x} \in \Delta_{m-1}} \mathbf{x}^T \mathbf{A} \mathbf{y} = v_{II} = v$$

That is, there exists a saddle-point pair of optimal mixed strategies $(\mathbf{x}^*, \mathbf{y}^*) \in \Delta_{m-1} \times \Delta_{n-1}$ and a unique real number $v \in [\underline{v}, \overline{v}]$, called the **Value of the Game**, such that:

$$\mathbf{x}^T \mathbf{A} \mathbf{y}^* \le (\mathbf{x}^*)^T \mathbf{A} \mathbf{y}^* = v \le (\mathbf{x}^*)^T \mathbf{A} \mathbf{y} \qquad \forall \mathbf{x} \in \Delta_{m-1}, \quad \forall \mathbf{y} \in \Delta_{n-1}$$

A game with $v = 0$ is called a **fair game**; a game with $\mathbf{A}^T = -\mathbf{A}$ ($m = n$, skew-symmetric payoff matrix) is called a **symmetric game**, which always has value $v = 0$ and identical optimal strategy sets ($\mathbf{x}^* = \mathbf{y}^*$).

### Theorem 7.3 (Complementary Slackness / Equalizing Property of Active Pure Strategies):
At any optimal mixed-strategy pair $(\mathbf{x}^*, \mathbf{y}^*)$ with game value $v$:
1. Every pure column $j \in \{1, \dots, n\}$ played with **strictly positive probability ($y_j^* > 0$)** by Player $II$ must yield an expected payoff against $\mathbf{x}^*$ **strictly equal to $v$**: $\sum_{i=1}^m a_{ij} x_i^* = v$. Conversely, if $\sum_{i=1}^m a_{ij} x_i^* > v$, then $y_j^* = 0$.
2. Every pure row $i \in \{1, \dots, m\}$ played with **strictly positive probability ($x_i^* > 0$)** by Player $I$ must yield an expected payoff against $\mathbf{y}^*$ **strictly equal to $v$**: $\sum_{j=1}^n a_{ij} y_j^* = v$. Conversely, if $\sum_{j=1}^n a_{ij} y_j^* < v$, then $x_i^* = 0$.

## 7.4 Analytical 2x2 Odds Method and Graphical Envelope Solution of 2xn and mx2 Matrix Games

When at least one player possesses only two pure strategies (or after dominance reduction leaves a $2 \times 2$, $2 \times n$, or $m \times 2$ matrix without a pure saddle point), the optimal mixed strategies $(\mathbf{x}^*, \mathbf{y}^*)$ and game value $v$ can be derived in exact closed form without executing the full Simplex Algorithm.

### 1. Closed-Form Algebraic Formulas and the Method of Oddments for $2 \times 2$ Games

Consider a $2 \times 2$ matrix game $\mathbf{A} = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$ that has **no pure saddle point** (which occurs if and only if the two diagonal elements strictly bracket the two off-diagonal elements: either $a_{11}, a_{22} > a_{12}, a_{21}$ or $a_{11}, a_{22} < a_{12}, a_{21}$). Because no pure saddle point exists, both pure strategies must be active ($0 < x_1^*, x_2^* < 1$ with $x_2^* = 1 - x_1^*$, and $0 < y_1^*, y_2^* < 1$ with $y_2^* = 1 - y_1^*$). By the Equalizing Property (Theorem 7.3), Player $I$ chooses $(x_1^*, 1 - x_1^*)$ so that Player $II$'s expected loss is identical whether Player $II$ plays Column 1 or Column 2:

$$E(\mathbf{x}^*, \beta_1) = E(\mathbf{x}^*, \beta_2) = v \implies a_{11} x_1^* + a_{21} (1 - x_1^*) = a_{12} x_1^* + a_{22} (1 - x_1^*)$$

Solving this linear equation for $x_1^*$, $x_2^* = 1 - x_1^*$, and symmetrically solving $E(\alpha_1, \mathbf{y}^*) = E(\alpha_2, \mathbf{y}^*)$ for $y_1^*, y_2^*$ and $v$ yields the **Exact $2 \times 2$ Mixed-Strategy Formulas**:

$$x_1^* = \frac{a_{22} - a_{21}}{(a_{11} + a_{22}) - (a_{12} + a_{21})}, \qquad x_2^* = \frac{a_{11} - a_{12}}{(a_{11} + a_{22}) - (a_{12} + a_{21})}$$

$$y_1^* = \frac{a_{22} - a_{12}}{(a_{11} + a_{22}) - (a_{12} + a_{21})}, \qquad y_2^* = \frac{a_{11} - a_{21}}{(a_{11} + a_{22}) - (a_{12} + a_{21})}$$

$$v = \frac{a_{11} a_{22} - a_{12} a_{21}}{(a_{11} + a_{22}) - (a_{12} + a_{21})} = \frac{\det(\mathbf{A})}{\mathbf{1}^T \text{adj}(\mathbf{A}) \mathbf{1}}$$

Notice the rapid mnemonic known as **Williams' Method of Oddments**:
- The unnormalized odds (oddments) $(|a_{22} - a_{21}| : |a_{11} - a_{12}|)$ for Row 1 and Row 2 equal the absolute row differences **swapped across the two rows**!
- The unnormalized odds $(|a_{22} - a_{12}| : |a_{11} - a_{21}|)$ for Column 1 and Column 2 equal the absolute column differences **swapped across the two columns**!

### 2. Graphical Envelope Solution of $2 \times n$ and $m \times 2$ Matrix Games

When Player $I$ has $m = 2$ rows and Player $II$ has $n \ge 3$ columns ($2 \times n$ game), Player $I$'s mixed strategy $\mathbf{x} = (x_1, 1 - x_1)^T$ depends on a **single scalar probability parameter** $x_1 \in [0, 1]$!
- Against each pure column $j \in \{1, 2, \dots, n\}$ of Player $II$, Player $I$'s expected payoff is a linear function of $x_1 \in [0, 1]$:
  $$E_j(x_1) = a_{1j} x_1 + a_{2j} (1 - x_1) = a_{2j} + (a_{1j} - a_{2j}) x_1, \qquad x_1 \in [0, 1]$$
  Plotted on two vertical parallel axes at $x_1 = 0$ (height $a_{2j}$) and $x_1 = 1$ (height $a_{1j}$), each column $j$ is a straight line segment connecting $(0, a_{2j})$ to $(1, a_{1j})$.
- Because Player $I$ seeks to **maximize the minimum** expected payoff over all $n$ columns:
  $$v = \max_{x_1 \in [0, 1]} \underbrace{\left( \min_{1 \le j \le n} E_j(x_1) \right)}_{\text{Lower Envelope } \underline{E}(x_1)}$$
  the pointwise minimum $\underline{E}(x_1) = \min_{1 \le j \le n} E_j(x_1)$ forms a **piecewise-linear concave lower envelope** across $x_1 \in [0, 1]$! The global maximum $v$ of this lower envelope occurs at its **highest peak vertex** $x_1^*$, which is the intersection of **two active column lines $j_1$ and $j_2$**! Thus, any $2 \times n$ game reduces to a **$2 \times 2$ subgame** on the two columns $(j_1, j_2)$ intersecting at the peak of the lower envelope (with $y_j^* = 0$ for all other $n - 2$ columns!).
- Symmetrically, in an **$m \times 2$ game** where Player $II$ has $2$ columns $\mathbf{y} = (y_1, 1 - y_1)^T$ and Player $I$ has $m \ge 3$ rows, each row $i \in \{1, \dots, m\}$ plots as a line $E_i(y_1) = a_{i1} y_1 + a_{i2}(1 - y_1)$ for $y_1 \in [0, 1]$. Because Player $II$ seeks to **minimize the maximum** expected loss:
  $$v = \min_{y_1 \in [0, 1]} \underbrace{\left( \max_{1 \le i \le m} E_i(y_1) \right)}_{\text{Upper Envelope } \overline{E}(y_1)}$$
  the pointwise maximum $\overline{E}(y_1) = \max_{1 \le i \le m} E_i(y_1)$ forms a **piecewise-linear convex upper envelope**, and the game value $v$ occurs at the **lowest trough vertex** $y_1^*$ of the upper envelope, reducing the $m \times 2$ game to a $2 \times 2$ subgame on the two active rows $(i_1, i_2)$ intersecting at that lowest vertex!

## 7.5 Equivalence of Arbitrary mxn Matrix Games and Primal-Dual Linear Programming Systems

For general $m \times n$ matrix games where $\min(m, n) \ge 3$, graphical envelope methods are no longer applicable. Here we establish one of the most celebrated theorems of twentieth-century applied mathematics: **every finite two-person zero-sum matrix game is completely equivalent to a pair of mutually dual Linear Programming Problems**, and conversely, any primal-dual pair of Linear Programs can be embedded into a single skew-symmetric zero-sum matrix game!

### Step 1: Ensuring Strict Positivity of the Game Value ($v > 0$)

To transform Player $I$'s maximin problem and Player $II$'s minimax problem into standard-form Linear Programs by dividing through by the game value $v$, we must ensure that $v > 0$ (strictly positive). Suppose the payoff matrix $\mathbf{A} = [a_{ij}]$ contains negative or zero entries so that its lower value $\underline{v} \le 0$. By adding a fixed positive shift constant $k > |\min_{i,j} a_{ij}|$ (for instance, $k = 1 - \min_{i,j} a_{ij} > 0$ whenever $\min_{i,j} a_{ij} \le 0$) to every entry of $\mathbf{A}$ to form the shifted matrix $\tilde{\mathbf{A}} = [a_{ij} + k] > \mathbf{0}$, for any mixed strategies $\mathbf{x} \in \Delta_{m-1}$ and $\mathbf{y} \in \Delta_{n-1}$:

$$\mathbf{x}^T \tilde{\mathbf{A}} \mathbf{y} = \sum_{i=1}^m \sum_{j=1}^n x_i (a_{ij} + k) y_j = \mathbf{x}^T \mathbf{A} \mathbf{y} + k \underbrace{\left(\sum_{i=1}^m x_i\right)}_{=1} \underbrace{\left(\sum_{j=1}^n y_j\right)}_{=1} = \mathbf{x}^T \mathbf{A} \mathbf{y} + k$$

Thus **adding a constant $k$ to every entry of $\mathbf{A}$ leaves the optimal mixed strategies $(\mathbf{x}^*, \mathbf{y}^*)$ completely invariant and simply shifts the game value from $v$ to $\tilde{v} = v + k > 0$**! Once $\tilde{v}$ is found, the original game value is recovered via $v = \tilde{v} - k$. Henceforth we assume without loss of generality that $a_{ij} > 0$ and $v > 0$.

### Step 2: Deriving the Primal-Dual Linear Programs via Change of Variables

1. **Player $I$'s Maximin Problem**: Player $I$ seeks $\mathbf{x} \in \Delta_{m-1}$ and the largest scalar floor $v > 0$ such that every column's expected payoff is at least $v$:
   $$\text{Maximize } v \quad \text{subject to} \quad \sum_{i=1}^m a_{ij} x_i \ge v \;\; (j = 1, \dots, n), \quad \sum_{i=1}^m x_i = 1, \quad x_i \ge 0$$
   Because $v > 0$, divide every constraint by $v$ and define the scaled non-negative variables **$X_i = \frac{x_i}{v} \ge 0$** for $i = 1, \dots, m$. Notice that summing $X_i$ over all $i=1,\dots,m$ yields:
   $$\sum_{i=1}^m X_i = \sum_{i=1}^m \frac{x_i}{v} = \frac{1}{v} \sum_{i=1}^m x_i = \frac{1}{v}$$
   Because $v > 0$, **maximizing $v$ is strictly equivalent to minimizing $\frac{1}{v} = \sum_{i=1}^m X_i$**! Thus Player $I$'s problem becomes the standard-form **Minimization Linear Program (Dual LP)**:
   $$\text{(Player } I \text{ LP)} \quad \text{Minimize } W = \frac{1}{v} = \sum_{i=1}^m X_i \quad \text{subject to} \quad \sum_{i=1}^m a_{ij} X_i \ge 1 \;\; (j = 1, \dots, n), \quad X_i \ge 0 \;\; (\forall i)$$
2. **Player $II$'s Minimax Problem**: Symmetrically, Player $II$ seeks $\mathbf{y} \in \Delta_{n-1}$ and the smallest scalar ceiling $v > 0$ such that every row's expected loss is at most $v$:
   $$\text{Minimize } v \quad \text{subject to} \quad \sum_{j=1}^n a_{ij} y_j \le v \;\; (i = 1, \dots, m), \quad \sum_{j=1}^n y_j = 1, \quad y_j \ge 0$$
   Dividing by $v > 0$, defining **$Y_j = \frac{y_j}{v} \ge 0$** for $j = 1, \dots, n$, and noting that minimizing $v > 0$ is equivalent to **maximizing $\frac{1}{v} = \sum_{j=1}^n Y_j$**, Player $II$'s problem becomes the canonical **Maximization Linear Program (Primal LP)**:
   $$\text{(Player } II \text{ LP)} \quad \text{Maximize } Z = \frac{1}{v} = \sum_{j=1}^n Y_j \quad \text{subject to} \quad \sum_{j=1}^n a_{ij} Y_j \le 1 \;\; (i = 1, \dots, m), \quad Y_j \ge 0 \;\; (\forall j)$$

### Theorem 7.4 (Primal-Dual Identity of Matrix Games and Proof of the Minimax Theorem):
Player $II$'s Maximization LP ($\max Z = \mathbf{1}_n^T \mathbf{Y}$ s.t. $\mathbf{A}\mathbf{Y} \le \mathbf{1}_m, \mathbf{Y} \ge \mathbf{0}$) and Player $I$'s Minimization LP ($\min W = \mathbf{1}_m^T \mathbf{X}$ s.t. $\mathbf{A}^T\mathbf{X} \ge \mathbf{1}_n, \mathbf{X} \ge \mathbf{0}$) are **exact Symmetric Primal-Dual Linear Programs**! Because $a_{ij} > 0$, $\mathbf{Y} = \mathbf{0}$ is primal feasible and $\mathbf{X}$ is bounded below by $\mathbf{0}$ (and dual feasible for large $\mathbf{X}$), so by the **Strong Duality Theorem of Linear Programming (Theorem 3.2)**, both LPs possess finite optimal solutions $(\mathbf{Y}^*, \mathbf{X}^*)$ with:

$$Z^* = \sum_{j=1}^n Y_j^* = \sum_{i=1}^m X_i^* = W^* = \frac{1}{v} \implies v_I = v_{II} = v = \frac{1}{Z^*}, \qquad x_i^* = v X_i^*, \qquad y_j^* = v Y_j^*$$

Thus Strong Duality of Linear Programming provides an immediate, constructive algebraic proof of John von Neumann's Minimax Theorem! Furthermore, by solving **just one** of the two LPs (typically Player $II$'s Maximization LP via the standard Simplex Algorithm with slack variables $s_1, \dots, s_m \ge 0$ and zero artificial variables!), we read off $\mathbf{Y}^*$ from the optimal RHS column and read off Player $I$'s optimal scaled vector $\mathbf{X}^*$ directly from the optimal $z_j - c_j$ row under the $m$ slack variables!

## 7.6 Statistical Decision Theory as a Zero-Sum Game: Minimax Estimation, Bayes Priors, and Brown's Fictitious Play

The mathematical equivalence between zero-sum games and linear programming extends directly into the foundations of **Statistical Decision Theory**, as formulated by Abraham Wald (1945, 1950), David Blackwell, and Meyer Girshick (1954).

### Wald's Statistical Game against Nature: Minimax Risk and Least Favorable Priors

In a parametric statistical decision problem, a statistician observes a random sample $\mathbf{X} \sim P_\theta$, where the unknown true parameter $\theta$ belongs to a finite parameter space $\Theta = \{\theta_1, \theta_2, \dots, \theta_m\}$ (the pure strategies of **Nature**, Player $I$), and must select a decision rule $d_j$ from a finite set of non-randomized estimators or hypothesis tests $\mathcal{D} = \{d_1, d_2, \dots, d_n\}$ (the pure strategies of the **Statistician**, Player $II$). If the true state of nature is $\theta_i$ and the statistician employs decision rule $d_j$, the statistician incurs expected statistical loss (risk) $R(\theta_i, d_j) = \mathbb{E}_{\theta_i}[L(\theta_i, d_j(\mathbf{X}))] = a_{ij}$.
- A **randomized decision rule** for the Statistician is a probability vector $\mathbf{y} = (y_1, \dots, y_n)^T \in \Delta_{n-1}$ over $\mathcal{D}$.
- A **prior probability distribution** selected by Nature is a probability vector $\boldsymbol{\pi} = (\pi_1, \dots, \pi_m)^T \in \Delta_{m-1}$ over the parameter space $\Theta$.
- For any prior $\boldsymbol{\pi} \in \Delta_{m-1}$ and randomized decision rule $\mathbf{y} \in \Delta_{n-1}$, the **Bayes Risk** is the bilinear form $r(\boldsymbol{\pi}, \mathbf{y}) = \boldsymbol{\pi}^T \mathbf{R} \mathbf{y} = \sum_{i=1}^m \sum_{j=1}^n \pi_i R(\theta_i, d_j) y_j$.

By von Neumann's Minimax Theorem (Theorem 7.2) applied to the risk matrix $\mathbf{R} = [R(\theta_i, d_j)]$:

$$\max_{\boldsymbol{\pi} \in \Delta_{m-1}} \underbrace{\left( \min_{\mathbf{y} \in \Delta_{n-1}} \boldsymbol{\pi}^T \mathbf{R} \mathbf{y} \right)}_{\text{Minimum Bayes Risk } r^*(\boldsymbol{\pi})} = \min_{\mathbf{y} \in \Delta_{n-1}} \underbrace{\left( \max_{\boldsymbol{\pi} \in \Delta_{m-1}} \boldsymbol{\pi}^T \mathbf{R} \mathbf{y} \right)}_{\text{Maximum Risk } \max_i R(\theta_i, \mathbf{y})} = v$$

This yields **Wald's Fundamental Theorem of Minimax Statistical Inference**:
1. The Statistician's optimal mixed strategy $\mathbf{y}^* \in \Delta_{n-1}$ is the **Minimax Randomized Decision Rule**, which minimizes the worst-case frequentist risk $\max_{1 \le i \le m} R(\theta_i, \mathbf{y})$ across the entire parameter space $\Theta$.
2. Nature's optimal mixed strategy $\boldsymbol{\pi}^* \in \Delta_{m-1}$ is the **Least Favorable Prior Distribution**, which maximizes the minimum achievable Bayes risk $r^*(\boldsymbol{\pi}) = \min_{\mathbf{y}} \boldsymbol{\pi}^T\mathbf{R}\mathbf{y}$.
3. By Complementary Slackness (Theorem 7.3), every minimax decision rule $\mathbf{y}^*$ is a **Bayes rule with respect to the least favorable prior $\boldsymbol{\pi}^*$**, and achieves a **constant risk $R(\theta_i, \mathbf{y}^*) = v$** across all parameter states $\theta_i$ in the support of $\boldsymbol{\pi}^*$ ($\pi_i^* > 0$)—the celebrated **Equalizer Rule Theorem** of mathematical statistics!

### Iterative Learning in Games: George Brown's Fictitious Play and Robinson's Convergence Theorem

Besides exact Simplex pivoting, George W. Brown (1951) proposed an intuitive statistical learning algorithm for solving $m \times n$ matrix games known as **Fictitious Play** (the direct precursor to modern online regret-minimization and reinforcement learning). In Fictitious Play, the two players play the game repeatedly over discrete rounds $t = 1, 2, \dots, T$. In round $t+1$, Player $I$ forms the empirical frequency distribution $\hat{\mathbf{y}}^{(t)} = \frac{1}{t}\sum_{s=1}^t \mathbf{e}_{j_s} \in \Delta_{n-1}$ of Player $II$'s historical column choices over the first $t$ rounds and plays a pure row $i_{t+1} \in \arg\max_i (\mathbf{A}\hat{\mathbf{y}}^{(t)})_i$ that maximizes expected payoff against $\hat{\mathbf{y}}^{(t)}$; simultaneously, Player $II$ tracks the empirical frequency distribution $\hat{\mathbf{x}}^{(t)} = \frac{1}{t}\sum_{s=1}^t \mathbf{e}_{i_s} \in \Delta_{m-1}$ of Player $I$'s past row choices and plays a pure column $j_{t+1} \in \arg\min_j ((\hat{\mathbf{x}}^{(t)})^T\mathbf{A})_j$ that minimizes expected loss against $\hat{\mathbf{x}}^{(t)}$. Notice that at every step $t$, the empirical strategies provide rigorous two-sided bounds on the true game value $v$:

$$\min_{1 \le j \le n} \left( (\hat{\mathbf{x}}^{(t)})^T \mathbf{A} \right)_j \le v \le \max_{1 \le i \le m} \left( \mathbf{A} \hat{\mathbf{y}}^{(t)} \right)_i$$

In a celebrated 1951 paper in the *Annals of Mathematics*, Julia Robinson proved that as $t \to \infty$, the upper and lower bounds converge to $v$ and the empirical frequency vectors $(\hat{\mathbf{x}}^{(t)}, \hat{\mathbf{y}}^{(t)})$ converge to the set of optimal minimax mixed strategies $(\mathbf{x}^*, \mathbf{y}^*)$ for any finite zero-sum matrix game!

## Worked Questions and Solutions

### Question 1: Dominance Reduction, Saddle-Point Testing, and Exact 2x2 Oddments Solution

Consider the two-person zero-sum $4 \times 4$ matrix game with payoff matrix $\mathbf{A}$ (written as payoffs to Row Player $I$):

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Player $I$ \ Player $II$</th><th>$\beta_1$</th><th>$\beta_2$</th><th>$\beta_3$</th><th>$\beta_4$</th></tr></thead><tbody><tr><td>$\alpha_1$</td><td>$3$</td><td>$2$</td><td>$4$</td><td>$0$</td></tr><tr><td>$\alpha_2$</td><td>$3$</td><td>$4$</td><td>$2$</td><td>$4$</td></tr><tr><td>$\alpha_3$</td><td>$4$</td><td>$2$</td><td>$4$</td><td>$0$</td></tr><tr><td>$\alpha_4$</td><td>$0$</td><td>$4$</td><td>$0$</td><td>$8$</td></tr></tbody></table></div>

1. Compute the pure-strategy lower value $\underline{v} = \max_i \min_j a_{ij}$ and upper value $\overline{v} = \min_j \max_i a_{ij}$, and verify whether the game possesses a pure-strategy saddle point.
2. Apply **Iterative Elimination of Dominated Strategies** (using pure and convex-combination dominance) to reduce the $4 \times 4$ matrix step-by-step to a $2 \times 2$ active submatrix.
3. Solve the reduced $2 \times 2$ game analytically to determine the full $4$-dimensional optimal mixed strategies $\mathbf{x}^* = (x_1^*, x_2^*, x_3^*, x_4^*)^T$, $\mathbf{y}^* = (y_1^*, y_2^*, y_3^*, y_4^*)^T$, and the exact Value of the Game $v$.

### Solution, step 1: Compute Maximin and Minimax Pure Security Levels

We compute the row minimums and column maximums of $\mathbf{A}$:
- **Row minimums**: $\min_j a_{1j} = 0$, $\min_j a_{2j} = 2$, $\min_j a_{3j} = 0$, $\min_j a_{4j} = 0$.
  $$\underline{v} = \max \{0, \, 2, \, 0, \, 0\} = 2 \quad (\text{attained at Row } \alpha_2)$$
- **Column maximums**: $\max_i a_{i1} = 4$, $\max_i a_{i2} = 4$, $\max_i a_{i3} = 4$, $\max_i a_{i4} = 8$.
  $$\overline{v} = \min \{4, \, 4, \, 4, \, 8\} = 4 \quad (\text{attained at Columns } \beta_1, \beta_2, \beta_3)$$

Because $\underline{v} = 2 < 4 = \overline{v}$, **no pure-strategy saddle point exists**, and the true mixed-strategy value $v$ must lie strictly in the interval $2 \le v \le 4$.

### Solution, step 2: Iterative Elimination of Dominated Rows and Columns

1. **Pure Row Dominance ($\alpha_1$ dominated by $\alpha_3$)**: Compare Row $\alpha_1 = (3, 2, 4, 0)$ with Row $\alpha_3 = (4, 2, 4, 0)$. Since $a_{1j} \le a_{3j}$ for every column $j \in \{1,2,3,4\}$ (with strict inequality $3 < 4$ in Column 1), Player $I$ will never play $\alpha_1$ ($x_1^* = 0$). Delete Row $\alpha_1$, leaving rows $\{\alpha_2, \alpha_3, \alpha_4\}$.
2. **Pure Column Dominance ($\beta_1$ dominated by $\beta_3$)**: In the remaining $3 \times 4$ matrix on rows $\{\alpha_2, \alpha_3, \alpha_4\}$, compare Column $\beta_1 = (3, 4, 0)^T$ with Column $\beta_3 = (2, 4, 0)^T$. Since $a_{i1} \ge a_{i3}$ for all remaining rows $i \in \{2,3,4\}$ (with $3 > 2$ in Row $\alpha_2$), Player $II$ (the minimizer) prefers $\beta_3$ over $\beta_1$ ($y_1^* = 0$). Delete Column $\beta_1$, leaving columns $\{\beta_2, \beta_3, \beta_4\}$:
   $$\mathbf{A}_{\text{red}, 1} = \begin{pmatrix} 4 & 2 & 4 \\ 2 & 4 & 0 \\ 4 & 0 & 8 \end{pmatrix} \begin{matrix} \leftarrow \alpha_2 \\ \leftarrow \alpha_3 \\ \leftarrow \alpha_4 \end{matrix}$$
3. **Convex-Combination Column Dominance ($\beta_2$ dominated by $\frac{1}{2}\beta_3 + \frac{1}{2}\beta_4$)**: Compare Column $\beta_2 = (4, 2, 4)^T$ against the $50$-$50$ average of Columns $\beta_3$ and $\beta_4$:
   $$\frac{1}{2}\begin{pmatrix} 2 \\ 4 \\ 0 \end{pmatrix} + \frac{1}{2}\begin{pmatrix} 4 \\ 0 \\ 8 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \\ 4 \end{pmatrix} \le \begin{pmatrix} 4 \\ 2 \\ 4 \end{pmatrix} = \beta_2$$
   Because the convex combination $\frac{1}{2}\beta_3 + \frac{1}{2}\beta_4$ inflicts a smaller or equal loss in every row ($3 < 4$ in $\alpha_2$, $2 = 2$ in $\alpha_3$, $4 = 4$ in $\alpha_4$), Column $\beta_2$ is dominated ($y_2^* = 0$)! Delete Column $\beta_2$, leaving columns $\{\beta_3, \beta_4\}$:
   $$\mathbf{A}_{\text{red}, 2} = \begin{pmatrix} 2 & 4 \\ 4 & 0 \\ 0 & 8 \end{pmatrix} \begin{matrix} \leftarrow \alpha_2 \\ \leftarrow \alpha_3 \\ \leftarrow \alpha_4 \end{matrix}$$
4. **Convex-Combination Row Dominance ($\alpha_2$ dominated by $\frac{1}{2}\alpha_3 + \frac{1}{2}\alpha_4$)**: Compare Row $\alpha_2 = (2, 4)$ against the $50$-$50$ average of Rows $\alpha_3 = (4, 0)$ and $\alpha_4 = (0, 8)$:
   $$\frac{1}{2}(4, 0) + \frac{1}{2}(0, 8) = (2, 4) = \alpha_2$$
   Since Row $\alpha_2$ is an exact convex combination of Rows $\alpha_3$ and $\alpha_4$, we can delete $\alpha_2$ ($x_2^* = 0$) to obtain a $2 \times 2$ active subgame on rows $\{\alpha_3, \alpha_4\}$ and columns $\{\beta_3, \beta_4\}$:
   $$\mathbf{A}_{2 \times 2} = \begin{pmatrix} 4 & 0 \\ 0 & 8 \end{pmatrix}$$

### Solution, step 3: Solve the 2x2 Subgame and Verify Optimal Mixed Strategies

Applying the exact $2 \times 2$ mixed-strategy formulas (Section 7.4) to $\mathbf{A}_{2\times 2} = \begin{pmatrix} 4 & 0 \\ 0 & 8 \end{pmatrix}$ on $\{\alpha_3, \alpha_4\} \times \{\beta_3, \beta_4\}$:
- Denominator: $(a_{11} + a_{22}) - (a_{12} + a_{21}) = (4 + 8) - (0 + 0) = 12$.
- Active probabilities for Player $I$:
  $$x_3^* = \frac{8 - 0}{12} = \frac{8}{12} = \frac{2}{3}, \qquad x_4^* = \frac{4 - 0}{12} = \frac{4}{12} = \frac{1}{3}$$
- Active probabilities for Player $II$:
  $$y_3^* = \frac{8 - 0}{12} = \frac{8}{12} = \frac{2}{3}, \qquad y_4^* = \frac{4 - 0}{12} = \frac{4}{12} = \frac{1}{3}$$
- Value of the Game:
  $$v = \frac{4(8) - 0(0)}{12} = \frac{32}{12} = \frac{8}{3} \approx 2.667$$

Assembling the full $4$-dimensional strategy vectors:
- **Player $I$ Optimal Strategy**: $\mathbf{x}^* = \left(0, \, 0, \, \frac{2}{3}, \, \frac{1}{3}\right)^T$ (Note: because $\alpha_2 = \frac{1}{2}\alpha_3 + \frac{1}{2}\alpha_4$, any convex combination with $\mathbf{x}^{**} = \left(0, \, \frac{2}{3}, \, \frac{1}{3}, \, 0\right)^T$ is also optimal!).
- **Player $II$ Optimal Strategy**: $\mathbf{y}^* = \left(0, \, 0, \, \frac{2}{3}, \, \frac{1}{3}\right)^T$, with exact game value **$v = \frac{8}{3}$**.

### Question 2: Graphical Lower-Envelope Solution of a 2x4 Matrix Game

Solve the following $2 \times 4$ matrix game graphically and algebraically using the **Lower Envelope Method**:

<div class="table-wrapper"><table class="data-table"><thead><tr><th>Player $I$ \ Player $II$</th><th>$\beta_1$</th><th>$\beta_2$</th><th>$\beta_3$</th><th>$\beta_4$</th></tr></thead><tbody><tr><td>$\alpha_1$ ($x_1$)</td><td>$2$</td><td>$2$</td><td>$3$</td><td>$-1$</td></tr><tr><td>$\alpha_2$ ($1 - x_1$)</td><td>$4$</td><td>$3$</td><td>$2$</td><td>$6$</td></tr></tbody></table></div>

1. Express Player $I$'s expected payoff $E_j(x_1)$ against each of the four pure columns $\beta_1, \beta_2, \beta_3, \beta_4$ as an explicit linear function of $x_1 \in [0, 1]$, and check for any pure column dominance.
2. Determine the piecewise-linear concave **Lower Envelope** $\underline{E}(x_1) = \min_{1 \le j \le 4} E_j(x_1)$ across $x_1 \in [0, 1]$ and find the exact abscissa $x_1^*$ and height $v$ of its maximum peak vertex.
3. Solve the dual $2 \times 2$ system on the two active columns intersecting at $x_1^*$ to determine Player $II$'s complete optimal mixed strategy $\mathbf{y}^* = (y_1^*, y_2^*, y_3^*, y_4^*)^T$.

### Solution, step 1: Formulate Column Payoff Lines E_j(x_1) and Eliminate Dominated Columns

First, compare Column $\beta_1 = (2, 4)^T$ and Column $\beta_2 = (2, 3)^T$. Since $a_{i1} \ge a_{i2}$ for both rows ($2 \ge 2$ and $4 > 3$), Column $\beta_1$ is strictly dominated by Column $\beta_2$, so Player $II$ sets $y_1^* = 0$.

For Player $I$'s mixed strategy $\mathbf{x} = (x_1, 1 - x_1)^T$ with $x_1 \in [0, 1]$, the four column expected payoff lines $E_j(x_1) = a_{1j}x_1 + a_{2j}(1 - x_1)$ are:
1. $E_1(x_1) = 2x_1 + 4(1 - x_1) = 4 - 2x_1$ (Dominated: lies entirely above $E_2(x_1) = 3 - x_1$ on $[0, 1]$)
2. $E_2(x_1) = 2x_1 + 3(1 - x_1) = 3 - x_1$ (Decreasing from $3$ at $x_1=0$ to $2$ at $x_1=1$)
3. $E_3(x_1) = 3x_1 + 2(1 - x_1) = 2 + x_1$ (Increasing from $2$ at $x_1=0$ to $3$ at $x_1=1$)
4. $E_4(x_1) = -1x_1 + 6(1 - x_1) = 6 - 7x_1$ (Steeply decreasing from $6$ at $x_1=0$ to $-1$ at $x_1=1$)

### Solution, step 2: Construct the Piecewise-Linear Lower Envelope and Find the Peak Vertex

We trace the minimum $\underline{E}(x_1) = \min \{ E_2(x_1), E_3(x_1), E_4(x_1) \}$ from $x_1 = 0$ to $x_1 = 1$:
- At $x_1 = 0$: $E_2(0) = 3, E_3(0) = 2, E_4(0) = 6$, so $E_3(x_1) = 2 + x_1$ starts as the lowest line.
- Intersection of rising line $E_3(x_1) = 2 + x_1$ with falling line $E_2(x_1) = 3 - x_1$:
  $$2 + x_1 = 3 - x_1 \implies 2x_1 = 1 \implies x_1 = 0.5, \quad E_2(0.5) = E_3(0.5) = 2.5$$
  However, check $E_4(0.5) = 6 - 7(0.5) = 2.5$! Remarkably, all three lines $E_2, E_3, E_4$ intersect at the **exact same point** $(x_1^*, v) = (0.5, 2.5)$!
- Specifically:
  - For $x_1 \in [0, 0.5]$, $E_3(x_1) = 2 + x_1$ is the minimum (increasing from $2$ to $2.5$).
  - For $x_1 \in [0.5, 1]$, $E_4(x_1) = 6 - 7x_1$ is the minimum (decreasing from $2.5$ to $-1$).

Thus the concave lower envelope is:

$$\underline{E}(x_1) = \begin{cases} 2 + x_1, & 0 \le x_1 \le 0.5 \\ 6 - 7x_1, & 0.5 \le x_1 \le 1 \end{cases}$$

which attains its unique global maximum at **$x_1^* = \frac{1}{2}$** (so $\mathbf{x}^* = (1/2, 1/2)^T$) with game value **$v = \frac{5}{2} = 2.5$**!

### Solution, step 3: Determine Player II's Optimal Mixed Strategy Subset

Because the lower envelope peak at $x_1^* = 1/2$ is formed by the rising line $E_3(x_1)$ (slope $+1$) and Either of the falling lines $E_2(x_1)$ (slope $-1$) or $E_4(x_1)$ (slope $-7$), Player $II$ possesses **two extreme optimal mixed strategies** (and all convex combinations between them):
1. **Using Active Columns $\{\beta_2, \beta_3\}$** ($\mathbf{A}_{23} = \begin{pmatrix} 2 & 3 \\ 3 & 2 \end{pmatrix}$):
   $$2y_2 + 3y_3 = 2.5, \quad y_2 + y_3 = 1 \implies y_2^* = \frac{1}{2}, \quad y_3^* = \frac{1}{2} \implies \mathbf{y}^{(1)} = \left(0, \, \frac{1}{2}, \, \frac{1}{2}, \, 0\right)^T$$
2. **Using Active Columns $\{\beta_3, \beta_4\}$** ($\mathbf{A}_{34} = \begin{pmatrix} 3 & -1 \\ 2 & 6 \end{pmatrix}$):
   $$3y_3 - 1y_4 = 2.5, \quad y_3 + y_4 = 1 \implies 4y_3 = 3.5 \implies y_3^* = \frac{7}{8}, \quad y_4^* = \frac{1}{8} \implies \mathbf{y}^{(2)} = \left(0, \, 0, \, \frac{7}{8}, \, \frac{1}{8}\right)^T$$

Any convex combination $\mathbf{y}^*(\lambda) = \lambda \mathbf{y}^{(1)} + (1-\lambda)\mathbf{y}^{(2)}$ for $\lambda \in [0, 1]$ is globally optimal for Player $II$, guaranteeing expected loss at most $v = 2.5$.

### Question 3: Simplex Linear Programming Solution of a 3x3 Symmetric Zero-Sum Game (Generalized Rock-Paper-Scissors)

Consider a weighted $3 \times 3$ zero-sum matrix game in which each player chooses among three strategies ($\{1, 2, 3\}$), with payoff matrix $\mathbf{A}$:

$$\mathbf{A} = \begin{pmatrix} 0 & -1 & 2 \\ 1 & 0 & -3 \\ -2 & 3 & 0 \end{pmatrix}$$

1. Verify that $\mathbf{A}$ has no pure-strategy saddle point, and determine the shift constant $k > 0$ required to transform $\mathbf{A}$ into a strictly positive matrix $\tilde{\mathbf{A}} = [a_{ij} + k] > \mathbf{0}$.
2. Formulate Player $II$'s Maximization Linear Program ($\max Z = Y_1 + Y_2 + Y_3$ subject to $\tilde{\mathbf{A}}\mathbf{Y} \le \mathbf{1}$) and Player $I$'s Dual Minimization Linear Program ($\min W = X_1 + X_2 + X_3$ subject to $\tilde{\mathbf{A}}^T\mathbf{X} \ge \mathbf{1}$).
3. Solve the Linear Programming system (and verify by skew-symmetry $\mathbf{A}^T = -\mathbf{A}$) to determine the exact optimal mixed strategies $\mathbf{x}^*, \mathbf{y}^*$ and the game value $v$.

### Solution, step 1: Check Saddle Point Absence and Shift Matrix to Positive Entries

- Row minimums of $\mathbf{A}$ are $(-1, -3, -2) \implies \underline{v} = -1$.
- Column maximums of $\mathbf{A}$ are $(1, 3, 2) \implies \overline{v} = 1$.
Since $\underline{v} = -1 < 1 = \overline{v}$, there is no pure-strategy saddle point.
Notice further that $\mathbf{A}^T = -\mathbf{A}$ is a **skew-symmetric matrix**, so the game is symmetric ($v = 0$ and $\mathbf{x}^* = \mathbf{y}^*$)—which we now verify directly via Linear Programming!

Because the smallest entry of $\mathbf{A}$ is $a_{23} = -3$, we choose shift constant **$k = 4$** so that every entry of $\tilde{\mathbf{A}} = [a_{ij} + 4]$ is strictly positive:

$$\tilde{\mathbf{A}} = \begin{pmatrix} 4 & 3 & 6 \\ 5 & 4 & 1 \\ 2 & 7 & 4 \end{pmatrix} > \mathbf{0}$$

### Solution, step 2: Formulate the Primal-Dual Linear Programming Pair

With shifted game value $\tilde{v} = v + 4 > 0$, define $Y_j = y_j / \tilde{v} \ge 0$ and $X_i = x_i / \tilde{v} \ge 0$:
- **Player $II$'s Maximization LP (Primal)**:
  $$\text{Maximize } Z = \frac{1}{\tilde{v}} = Y_1 + Y_2 + Y_3$$
  subject to:
  $$\begin{aligned}
  4Y_1 + 3Y_2 + 6Y_3 &\le 1 \\
  5Y_1 + 4Y_2 + 1Y_3 &\le 1 \\
  2Y_1 + 7Y_2 + 4Y_3 &\le 1 \\
  Y_1, Y_2, Y_3 &\ge 0
  \end{aligned}$$
- **Player $I$'s Minimization LP (Dual)**:
  $$\text{Minimize } W = \frac{1}{\tilde{v}} = X_1 + X_2 + X_3$$
  subject to:
  $$\begin{aligned}
  4X_1 + 5X_2 + 2X_3 &\ge 1 \\
  3X_1 + 4X_2 + 7X_3 &\ge 1 \\
  6X_1 + 1X_2 + 4X_3 &\ge 1 \\
  X_1, X_2, X_3 &\ge 0
  \end{aligned}$$

### Solution, step 3: Solve the Linear System and Recover (x*, y*, v)

Solving the $3 \times 3$ active equality system $\tilde{\mathbf{A}}\mathbf{Y} = \mathbf{1}$ (subtracting Row 2 from Row 1 gives $-Y_1 - Y_2 + 5Y_3 = 0 \implies Y_1 + Y_2 = 5Y_3$; subtracting $2\times$Row 2 from Row 3 gives $-8Y_1 - Y_2 + 2Y_3 = -1$; and using the unshifted null-space equation $\mathbf{A}\mathbf{y}^* = \mathbf{0}$):

$$\begin{aligned}
-y_2^* + 2y_3^* &= 0 \implies y_2^* = 2y_3^* \\
y_1^* - 3y_3^* &= 0 \implies y_1^* = 3y_3^* \\
-2y_1^* + 3y_2^* &= 0 \implies -6y_3^* + 6y_3^* = 0
\end{aligned}$$

Normalizing via $y_1^* + y_2^* + y_3^* = 3y_3^* + 2y_3^* + y_3^* = 6y_3^* = 1$ yields $y_3^* = \frac{1}{6}, y_2^* = \frac{2}{6} = \frac{1}{3}, y_1^* = \frac{3}{6} = \frac{1}{2}$!
Checking in the shifted LP $\tilde{\mathbf{A}}\mathbf{Y}^* = \mathbf{1}$ with $\tilde{v} = 4$:
- $Y_1^* = \frac{1/2}{4} = \frac{3}{24} = \frac{1}{8}, \quad Y_2^* = \frac{1/3}{4} = \frac{2}{24} = \frac{1}{12}, \quad Y_3^* = \frac{1/6}{4} = \frac{1}{24}$.
- Row 1: $4(3/24) + 3(2/24) + 6(1/24) = (12 + 6 + 6)/24 = 24/24 = 1$.
- Row 2: $5(3/24) + 4(2/24) + 1(1/24) = (15 + 8 + 1)/24 = 24/24 = 1$.
- Row 3: $2(3/24) + 7(2/24) + 4(1/24) = (6 + 14 + 4)/24 = 24/24 = 1$.
- Identically, $\mathbf{X}^* = \mathbf{Y}^* = (3/24, 2/24, 1/24)^T$ satisfies $\tilde{\mathbf{A}}^T\mathbf{X}^* = \mathbf{1}$ with $Z^* = W^* = \frac{3+2+1}{24} = \frac{6}{24} = \frac{1}{4}$.

Therefore, $\tilde{v} = \frac{1}{Z^*} = 4 \implies$ the original Value of the Game is **$v = \tilde{v} - k = 4 - 4 = 0$** (a fair game), and both players share the unique optimal mixed strategy:

$$\mathbf{x}^* = \mathbf{y}^* = \begin{pmatrix} 1/2 \\ 1/3 \\ 1/6 \end{pmatrix}$$
