# tooling/add-depth-all.py
import re

# 1. Expand Unit 8
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-8.md", "r", encoding="utf-8") as f:
    u8 = f.read()

u8_addition = r"""

---

## 8.6 Advanced Survival and Hierarchical Formula Specifications: Counting Processes and Frailty Models

In biostatistics, oncology trials, and econometric duration analysis, event-time data requires specialized formula specifications that accommodate right-censoring, left-truncation, time-varying covariates, and clustered random effects. David Cox (1972) and Odd Aalen (1978) formalized the counting process approach to survival analysis, which is implemented in R's `survival` package and Python's `lifelines` and `scikit-survival`.

### The Counting Process Formula Syntax: `Surv(time1, time2, event)`

In classical survival models, an observation is characterized by a single duration $T$ and a binary censoring indicator $\delta \in \{0, 1\}$. However, when subjects experience recurrent events or covariates change over time (e.g., patient blood pressure recorded at sequential clinic visits), the data must be structured into discontinuous risk intervals $[t_{start}, t_{stop})$.

The Wilkinson–Rogers formula is extended via the `Surv()` response constructor:

$$\text{Surv}(t_{start}, t_{stop}, \text{event}) \sim \mathbf{x}_1 + \mathbf{x}_2 + \dots$$

#### The Cox Proportional Hazards Model:
The hazard function for subject $i$ at time $t$ is formulated as:

$$\lambda_i(t) = \lambda_0(t) \exp(\mathbf{x}_i(t)^\top \boldsymbol{\beta})$$

where $\lambda_0(t)$ is the non-parametric baseline hazard function, and $\mathbf{x}_i(t)$ is the vector of possibly time-dependent covariates.

#### Partial Likelihood Estimation:
Because the baseline hazard $\lambda_0(t)$ is arbitrary, standard maximum likelihood fails. David Cox (1975) introduced the **Partial Likelihood**:
Let $t_1 < t_2 < \dots < t_D$ denote the ordered distinct uncensored event times. Let $\mathcal{R}(t_d) = \{ j : t_{start, j} \le t_d \le t_{stop, j} \}$ denote the **risk set** of individuals alive and under observation immediately prior to time $t_d$.

The partial log-likelihood is:

$$\ell_p(\boldsymbol{\beta}) = \sum_{d=1}^D \left[ \mathbf{x}_{(d)}^\top \boldsymbol{\beta} - \ln\left( \sum_{j \in \mathcal{R}(t_d)} \exp(\mathbf{x}_j^\top \boldsymbol{\beta}) \right) \right]$$

Notice that the baseline hazard $\lambda_0(t)$ **cancels out completely** from the partial likelihood! Parameter estimation is executed via Newton–Raphson, where evaluating the inner risk set sum across all failure times requires sorting observations by time and maintaining running risk accumulators in $\mathcal{O}(n \log n)$ time.

### Shared Frailty and Random Effects in Formula Syntax

When observations are clustered within clinical centers, families, or geographic regions, survival times within the same cluster exhibit unobserved latent correlation. This is modeled using **Shared Frailty Models**:

$$\lambda_{ij}(t) = \lambda_0(t) w_i \exp(\mathbf{x}_{ij}^\top \boldsymbol{\beta}) = \lambda_0(t) \exp(\mathbf{x}_{ij}^\top \boldsymbol{\beta} + u_i)$$

where $w_i = \exp(u_i) > 0$ is the unobserved frailty of cluster $i$, typically distributed as $\text{Gamma}(1/\theta, 1/\theta)$ or log-normal.
In formula syntax, frailty terms are specified via `+ frailty(center)` in R `survival` or `+ (1 | center)` in `coxme`.

---

## 8.7 Apache Arrow Flight RPC and Distributed In-Memory Data Streaming

While the Arrow C Data Interface enables zero-copy sharing within the same physical machine, large-scale enterprise statistical systems often operate across distributed cluster nodes. Traditionally, transferring data frames across a local network requires serializing to JSON, Parquet, or CSV, sending over HTTP REST or gRPC, and deserializing on the receiving machine.

In 2019, the Apache Arrow project released **Arrow Flight RPC**, a high-performance data streaming framework built atop gRPC and Protocol Buffers.

### Architecture of Arrow Flight
1. **Direct RecordBatch Streaming**: Arrow Flight transmits Arrow RecordBatches directly in their native binary columnar format over TCP/IP sockets without serializing or rearranging memory bytes.
2. **Parallel Multi-Stream Endpoints**: A Flight client querying a cluster receives a `FlightInfo` ticket detailing multiple independent `FlightEndpoint` servers. The client can open parallel TCP connections to all cluster worker nodes simultaneously, saturating 100 Gbps network bandwidth.
3. **Flight SQL**: Provides a standardized, high-speed wire protocol for executing SQL queries on remote analytical databases (DuckDB, ClickHouse, Apache DataFusion) and pulling results directly into pandas or R data.frames at memory-bus speeds.
"""

marker = "## Fully worked question 1:"
idx = u8.find(marker)
u8_new = u8[:idx] + u8_addition.strip() + "\n\n" + u8[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-8.md", "w", encoding="utf-8") as f:
    f.write(u8_new)
print("Expanded Unit 8!")

# 2. Expand Unit 7
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-7.md", "r", encoding="utf-8") as f:
    u7 = f.read()

u7_addition = r"""

---

## 7.8 Constrained Optimization: Karush–Kuhn–Tucker Conditions, Barrier Methods, and Augmented Lagrangians

Many statistical estimation problems impose physical, biological, or mathematical constraints on the parameter vector:
- Non-negativity: $\beta_j \ge 0$ (e.g. concentrations, non-negative matrix factorization).
- Probability simplex: $\sum \pi_k = 1, \pi_k \ge 0$ (mixture proportions, Markov transition matrices).
- Bounded parameter domains: $L_j \le \theta_j \le U_j$.
- Covariance positive definiteness: $\boldsymbol{\Sigma} \succ 0$.

### The Karush–Kuhn–Tucker (KKT) Necessary Conditions

Consider the general constrained statistical optimization problem:

$$\min_{\boldsymbol{\theta}} f(\boldsymbol{\theta}) \quad \text{subject to } \begin{cases} g_i(\boldsymbol{\theta}) \le 0, & i = 1, \dots, m \\ h_j(\boldsymbol{\theta}) = 0, & j = 1, \dots, r \end{cases}$$

Define the **Lagrangian function**:

$$\mathcal{L}(\boldsymbol{\theta}, \boldsymbol{\lambda}, \boldsymbol{\nu}) = f(\boldsymbol{\theta}) + \sum_{i=1}^m \lambda_i g_i(\boldsymbol{\theta}) + \sum_{j=1}^r \nu_j h_j(\boldsymbol{\theta})$$

where $\lambda_i \ge 0$ are the Lagrange multipliers for inequality constraints and $\nu_j \in \mathbb{R}$ are multipliers for equality constraints.

#### The KKT First-Order Conditions:
At any local constrained minimum $\boldsymbol{\theta}^*$, under standard constraint qualifications (e.g. Slater's condition for convex problems), there exist multiplier vectors $\boldsymbol{\lambda}^*$ and $\boldsymbol{\nu}^*$ satisfying:
1. **Stationarity**:
   $$\nabla_{\boldsymbol{\theta}} \mathcal{L}(\boldsymbol{\theta}^*, \boldsymbol{\lambda}^*, \boldsymbol{\nu}^*) = \nabla f(\boldsymbol{\theta}^*) + \sum_{i=1}^m \lambda_i^* \nabla g_i(\boldsymbol{\theta}^*) + \sum_{j=1}^r \nu_j^* \nabla h_j(\boldsymbol{\theta}^*) = \mathbf{0}$$
2. **Primal Feasibility**:
   $$g_i(\boldsymbol{\theta}^*) \le 0 \quad (i = 1, \dots, m), \quad h_j(\boldsymbol{\theta}^*) = 0 \quad (j = 1, \dots, r)$$
3. **Dual Feasibility**:
   $$\lambda_i^* \ge 0 \quad (i = 1, \dots, m)$$
4. **Complementary Slackness**:
   $$\lambda_i^* g_i(\boldsymbol{\theta}^*) = 0 \quad \text{for all } i = 1, \dots, m$$

The complementary slackness condition implies that either the constraint is strictly active (binding: $g_i(\boldsymbol{\theta}^*) = 0$), in which case its shadow price $\lambda_i^* \ge 0$; or the constraint is inactive ($g_i(\boldsymbol{\theta}^*) < 0$), in which case $\lambda_i^* = 0$.

### Interior Point and Logarithmic Barrier Methods

For inequality constraints $g_i(\boldsymbol{\theta}) \le 0$, **Interior Point Methods** replace the hard constraints with a smooth **Logarithmic Barrier Function**:

$$\phi(\boldsymbol{\theta}) = -\sum_{i=1}^m \ln(-g_i(\boldsymbol{\theta}))$$

The algorithm solves a sequence of unconstrained problems indexed by barrier parameter $\mu > 0$:

$$\min_{\boldsymbol{\theta}} f_\mu(\boldsymbol{\theta}) = f(\boldsymbol{\theta}) + \mu \phi(\boldsymbol{\theta}) = f(\boldsymbol{\theta}) - \mu \sum_{i=1}^m \ln(-g_i(\boldsymbol{\theta}))$$

As $\boldsymbol{\theta}$ approaches the boundary of the feasible region ($g_i(\boldsymbol{\theta}) \to 0^-$), the logarithmic term $-\ln(-g_i) \to +\infty$, erecting an impassable barrier that prevents iterates from leaving the interior.
By systematically shrinking $\mu \to 0$ (e.g. $\mu_{t+1} = 0.2 \mu_t$) and solving each sub-problem via Newton's method, the trajectory (central path) converges to the exact constrained optimum.

### Coordinate Descent for Elastic Net and High-Dimensional Regression

For high-dimensional regularized regression models (Lasso, Elastic Net: $\lambda_1 \|\boldsymbol{\beta}\|_1 + \frac{\lambda_2}{2} \|\boldsymbol{\beta}\|_2^2$), Jerome Friedman, Trevor Hastie, and Robert Tibshirani (2007) popularized **Coordinate Descent** (the engine of the `glmnet` package in R and Python).

Instead of updating all $p$ coefficients simultaneously:
1. Cycle through predictors $j = 1, 2, \dots, p$ one at a time.
2. Holding all other coefficients $\boldsymbol{\beta}_{-j}$ fixed, solve the exact univariate sub-problem for $\beta_j$:
   $$\hat{\beta}_j = \frac{\mathcal{S}_{\lambda_1}( \mathbf{x}_j^\top (\mathbf{y} - \sum_{k \ne j} \mathbf{x}_k \beta_k) )}{\mathbf{x}_j^\top \mathbf{x}_j + \lambda_2}$$
Because the univariate solution has a closed-form soft-thresholding expression, Coordinate Descent sweeps through thousands of variables in milliseconds, delivering state-of-the-art performance for sparse genomic regressions.
"""

marker = "## Fully worked question 1:"
idx = u7.find(marker)
u7_new = u7[:idx] + u7_addition.strip() + "\n\n" + u7[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-7.md", "w", encoding="utf-8") as f:
    f.write(u7_new)
print("Expanded Unit 7!")

# 3. Expand Unit 5
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-5.md", "r", encoding="utf-8") as f:
    u5 = f.read()

u5_addition = r"""

---

## 5.8 Hamiltonian Monte Carlo and the No-U-Turn Sampler (NUTS)

While random-walk Metropolis–Hastings and Gibbs sampling enabled Bayesian computation in the 1990s, they fail when applied to high-dimensional models ($p > 100$) with complex correlation structures. In high dimensions, random-walk proposals suffer from diffusive behavior, requiring small proposal steps to maintain acceptance rates, which leads to slow $\mathcal{O}(p^2)$ exploration of the parameter space.

To overcome diffusive random walks, Radford Neal (2011) introduced **Hamiltonian Monte Carlo (HMC)** to statistics, translating concepts from classical Hamiltonian mechanics into an ultra-efficient sampling engine. HMC forms the core computational backbone of modern probabilistic programming languages, including **Stan**, **PyMC**, and **Turing.jl**.

### Physical Analogy: Phase Space and Symplectic Dynamics

HMC augments the continuous parameter vector of interest $\boldsymbol{\theta} \in \mathbb{R}^p$ (the position) with an auxiliary momentum vector $\mathbf{p} \sim \mathcal{N}(\mathbf{0}, \mathbf{M})$:
- The target probability density defines a **Potential Energy**:
  $$V(\boldsymbol{\theta}) = -\ln p(\boldsymbol{\theta}, \mathbf{y})$$
- The momentum defines a **Kinetic Energy**:
  $$K(\mathbf{p}) = \frac{1}{2} \mathbf{p}^\top \mathbf{M}^{-1} \mathbf{p}$$
where $\mathbf{M}$ is a symmetric positive-definite mass matrix.

The **Hamiltonian function** is the total energy of the physical system:

$$H(\boldsymbol{\theta}, \mathbf{p}) = V(\boldsymbol{\theta}) + K(\mathbf{p}) = -\ln p(\boldsymbol{\theta}, \mathbf{y}) + \frac{1}{2} \mathbf{p}^\top \mathbf{M}^{-1} \mathbf{p}$$

The joint probability density over phase space $(\boldsymbol{\theta}, \mathbf{p})$ is:
$$p(\boldsymbol{\theta}, \mathbf{p}) \propto \exp(-H(\boldsymbol{\theta}, \mathbf{p})) = p(\boldsymbol{\theta}, \mathbf{y}) \exp\left( -\frac{1}{2} \mathbf{p}^\top \mathbf{M}^{-1} \mathbf{p} \right)$$
Notice that $\boldsymbol{\theta}$ and $\mathbf{p}$ are independent. Marginally, the positions $\boldsymbol{\theta}$ follow the exact target posterior distribution!

### Hamilton's Equations of Motion
The physical trajectory of a frictionless particle gliding across the potential energy surface is governed by Hamilton's differential equations:

$$\frac{d\boldsymbol{\theta}}{dt} = \frac{\partial H}{\partial \mathbf{p}} = \mathbf{M}^{-1} \mathbf{p}$$

$$\frac{d\mathbf{p}}{dt} = -\frac{\partial H}{\partial \boldsymbol{\theta}} = -\nabla V(\boldsymbol{\theta}) = \nabla_{\boldsymbol{\theta}} \ln p(\boldsymbol{\theta}, \mathbf{y})$$

#### Fundamental Conservation Properties:
1. **Conservation of Energy**: Along any trajectory, $\frac{dH}{dt} = 0$. The Hamiltonian remains constant.
2. **Reversibility**: Reversing the sign of momentum ($\mathbf{p} \leftarrow -\mathbf{p}$) traces the exact same path backward in time.
3. **Volume Preservation (Liouville's Theorem)**: Phase space volume is invariant under Hamiltonian vector fields: $|\det(\mathbf{J})| = 1$.

### The Numerical Leapfrog Integrator
Because continuous differential equations cannot be solved exactly in digital computers, HMC discretizes time using a **Symplectic Leapfrog Integrator** with step size $\epsilon$:

1. Half-step update for momentum:
   $$\mathbf{p}\left( t + \frac{\epsilon}{2} \right) = \mathbf{p}(t) + \frac{\epsilon}{2} \nabla_{\boldsymbol{\theta}} \ln p(\boldsymbol{\theta}(t), \mathbf{y})$$
2. Full-step update for position:
   $$\boldsymbol{\theta}(t + \epsilon) = \boldsymbol{\theta}(t) + \epsilon \mathbf{M}^{-1} \mathbf{p}\left( t + \frac{\epsilon}{2} \right)$$
3. Half-step update for momentum:
   $$\mathbf{p}(t + \epsilon) = \mathbf{p}\left( t + \frac{\epsilon}{2} \right) + \frac{\epsilon}{2} \nabla_{\boldsymbol{\theta}} \ln p(\boldsymbol{\theta}(t + \epsilon), \mathbf{y})$$

Because the leapfrog integrator is strictly symplectic and time-reversible, small discretization errors are accounted for by a final **Metropolis filter**:
$$\alpha = \min\left( 1, \, \exp(-H(\boldsymbol{\theta}^*, \mathbf{p}^*) + H(\boldsymbol{\theta}^{(0)}, \mathbf{p}^{(0)})) \right)$$
Because energy is approximately conserved along leapfrog trajectories, acceptance probabilities routinely exceed **$85\%$ to $95\%$**, even across trajectories spanning hundreds of dimensions!

### The No-U-Turn Sampler (NUTS)
A critical limitation of standard HMC is tuning the trajectory length $L$ (number of leapfrog steps): if $L$ is too small, exploration is diffusive; if $L$ is too large, the trajectory loops back on itself (making a "U-turn"), wasting CPU cycles.

In 2014, Matthew Hoffman and Andrew Gelman formulated the **No-U-Turn Sampler (NUTS)**. NUTS uses a recursive binary tree to integrate leapfrog steps forward and backward in time until the trajectory begins to turn back on itself:
$$\frac{d}{dt} \|\boldsymbol{\theta}_{end} - \boldsymbol{\theta}_{start}\|_2^2 < 0$$
NUTS automatically identifies the optimal trajectory length at every iteration, eliminating manual tuning and providing the industry standard for production Bayesian computation.
"""

marker = "## Fully worked question 1:"
idx = u5.find(marker)
u5_new = u5[:idx] + u5_addition.strip() + "\n\n" + u5[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-5.md", "w", encoding="utf-8") as f:
    f.write(u5_new)
print("Expanded Unit 5!")

# 4. Expand Unit 4
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-4.md", "r", encoding="utf-8") as f:
    u4 = f.read()

u4_addition = r"""

---

## 4.8 Spectral Graph Theory, Graph Laplacians, and Spectral Clustering

In modern spatial statistics, network analytics, and manifold learning, data relationships are naturally modeled as graphs $\mathcal{G} = (\mathcal{V}, \mathcal{E})$. Spectral graph theory investigates the structural properties of graphs through the eigenvalues and eigenvectors of associated matrices, providing the foundation for **Spectral Clustering** and Laplacian Eigenmaps.

### The Graph Adjacency, Degree, and Laplacian Matrices

Let $\mathcal{G}$ be an undirected, weighted graph with $n$ vertices.
1. **Adjacency (Affinity) Matrix $\mathbf{W} \in \mathbb{R}^{n \times n}$**:
   For continuous spatial data, weights are typically constructed via a Gaussian radial basis function (RBF) kernel:
   $$W_{ij} = \exp\left( -\frac{\|\mathbf{x}_i - \mathbf{x}_j\|_2^2}{2 \sigma^2} \right) \quad \text{for } i \ne j, \quad W_{ii} = 0$$
2. **Degree Matrix $\mathbf{D} \in \mathbb{R}^{n \times n}$**:
   A diagonal matrix containing the degree (total connectivity weight) of each vertex:
   $$D_{ii} = d_i = \sum_{j=1}^n W_{ij}$$
3. **Unnormalized Graph Laplacian $\mathbf{L} \in \mathbb{R}^{n \times n}$**:
   $$\mathbf{L} = \mathbf{D} - \mathbf{W}$$

#### Fundamental Mathematical Properties of the Graph Laplacian:
1. **Quadratic Energy Form**:
   For any vector $\mathbf{f} \in \mathbb{R}^n$:
   $$\mathbf{f}^\top \mathbf{L} \mathbf{f} = \mathbf{f}^\top \mathbf{D} \mathbf{f} - \mathbf{f}^\top \mathbf{W} \mathbf{f} = \sum_{i=1}^n d_i f_i^2 - \sum_{i, j=1}^n f_i f_j W_{ij}$$
   $$= \frac{1}{2} \left[ \sum_{i=1}^n \left( \sum_{j=1}^n W_{ij} \right) f_i^2 - 2 \sum_{i, j=1}^n f_i f_j W_{ij} + \sum_{j=1}^n \left( \sum_{i=1}^n W_{ij} \right) f_j^2 \right]$$
   $$= \frac{1}{2} \sum_{i, j=1}^n W_{ij} (f_i - f_j)^2 \ge 0$$
   Because $W_{ij} \ge 0$, the quadratic form is strictly non-negative, proving that $\mathbf{L}$ is **symmetric positive semi-definite (PSD)**.

2. **Trivial Eigenvalue and Multiplicity**:
   Notice that $\mathbf{L} \mathbf{1}_n = \mathbf{D} \mathbf{1}_n - \mathbf{W} \mathbf{1}_n = \mathbf{d} - \mathbf{d} = \mathbf{0}$.
   Therefore, $\lambda_1 = 0$ is always an eigenvalue of $\mathbf{L}$ with corresponding eigenvector $\mathbf{v}_1 = \mathbf{1}_n$.
   **Connected Components Theorem**: The multiplicity $k$ of the eigenvalue $\lambda = 0$ equals the exact number of connected components in the graph $\mathcal{G}$.

### Normalized Graph Laplacians and Normalized Cuts

In graph partitioning, dividing a graph into disjoint subsets $A$ and $B$ by minimizing the cross-cluster edge weights $\text{cut}(A, B) = \sum_{i \in A, j \in B} W_{ij}$ suffers from a severe size bias: it frequently isolates a single outlier vertex.
To enforce balanced clusters, Jianbo Shi and Jitendra Malik (2000) formulated the **Normalized Cut (NCut)** problem, which relaxes to finding the eigenvectors of the **Symmetric Normalized Laplacian**:

$$\mathbf{L}_{sym} = \mathbf{D}^{-1/2} \mathbf{L} \mathbf{D}^{-1/2} = \mathbf{I} - \mathbf{D}^{-1/2} \mathbf{W} \mathbf{D}^{-1/2}$$

#### The Ng–Jordan–Weiss (NJW) Spectral Clustering Algorithm:
1. Form affinity matrix $\mathbf{W}$ and degree matrix $\mathbf{D}$.
2. Compute the normalized Laplacian $\mathbf{L}_{sym} = \mathbf{I} - \mathbf{D}^{-1/2} \mathbf{W} \mathbf{D}^{-1/2}$.
3. Compute the $k$ smallest eigenvectors $\mathbf{u}_1, \dots, \mathbf{u}_k$ of $\mathbf{L}_{sym}$.
4. Construct matrix $\mathbf{U} \in \mathbb{R}^{n \times k}$ and normalize its rows to unit Euclidean length: $Y_{ij} = U_{ij} / \|\mathbf{U}_{i, :}\|_2$.
5. Cluster the rows of $\mathbf{Y}$ into $k$ groups using standard $k$-means.

Spectral clustering maps complex, non-linearly separable manifold structures (e.g. concentric circles or intertwining spirals) into linearly separable orthogonal coordinates, demonstrating the immense power of numerical linear algebra in exploratory data science.
"""

marker = "## Fully worked question 1:"
idx = u4.find(marker)
u4_new = u4[:idx] + u4_addition.strip() + "\n\n" + u4[idx:]
with open("publishing/drafts/statistics-probability-statistical-computing-with-python-and-r/unit-4.md", "w", encoding="utf-8") as f:
    f.write(u4_new)
print("Expanded Unit 4!")
