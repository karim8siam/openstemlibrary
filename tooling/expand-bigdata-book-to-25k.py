#!/usr/bin/env python3
"""
Comprehensive expansion script for Big Data Methods for Statistics (Book 16)
to bring the book draft past 25,000 substantive prose words across all 8 units.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")
    print(f"Unit {unit_num} expanded.")

# -------------------------------------------------------------
# UNIT 1 EXPANSION
# -------------------------------------------------------------
u1_exp = r"""
## 1.7 Concentration of Measure and Isoperimetric Inequalities

The counter-intuitive geometry of high-dimensional Euclidean space is governed by a universal mathematical principle known as the **Concentration of Measure Phenomenon**, formulated by Vitali Milman in the 1970s and developed extensively by Michel Talagrand and Michel Ledoux.

In informal terms, concentration of measure states that any well-behaved function defined on a high-dimensional probability space that does not depend too sensitively on any single coordinate fluctuates negligibly around its median or expectation.

### 1. Lévy's Lemma on the Hypersphere
Let $\mathbb{S}^{p-1} = \{ \mathbf{x} \in \mathbb{R}^p : \|\mathbf{x}\|_2 = 1 \}$ be the $(p-1)$-dimensional unit sphere equipped with the normalized uniform surface measure $\sigma$. Let $f: \mathbb{S}^{p-1} \to \mathbb{R}$ be an $L$-Lipschitz function:
$$|f(\mathbf{x}) - f(\mathbf{y})| \le L \|\mathbf{x} - \mathbf{y}\|_2 \quad \forall \mathbf{x}, \mathbf{y} \in \mathbb{S}^{p-1}$$
Let $M_f$ be the median of $f$, defined such that $\sigma(\mathbf{x} : f(\mathbf{x}) \le M_f) \ge 1/2$ and $\sigma(\mathbf{x} : f(\mathbf{x}) \ge M_f) \ge 1/2$.

*Theorem (Lévy's Lemma)*: For any $t > 0$:
$$\sigma\left( \mathbf{x} \in \mathbb{S}^{p-1} : |f(\mathbf{x}) - M_f| \ge t \right) \le 2 \exp\left( -\frac{(p-2) t^2}{2 L^2} \right)$$

*Profound Implication*: As dimension $p$ expands, the probability that an $L$-Lipschitz function deviates from its median by more than an infinitesimal threshold $t$ decays exponentially fast with $p$. In 1,000 dimensions, virtually every point on the sphere evaluates to within $M_f \pm 0.05$. In high dimensions, random continuous functions appear almost completely deterministic!

### 2. The Gaussian Isoperimetric Inequality and Borell-TIS Bound
The concentration of measure extends directly to high-dimensional Gaussian spaces. Let $\gamma_p$ denote the standard Gaussian measure on $\mathbb{R}^p$ with density $(2\pi)^{-p/2} e^{-\|\mathbf{x}\|_2^2/2}$.

*Theorem (Gaussian Concentration Inequality)*: Let $f: \mathbb{R}^p \to \mathbb{R}$ be an $L$-Lipschitz function with respect to the Euclidean norm, and let $\mathbf{X} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_p)$. Then:
$$P\left( |f(\mathbf{X}) - \mathbb{E}[f(\mathbf{X})]| \ge t \right) \le 2 \exp\left( -\frac{t^2}{2 L^2} \right)$$
Notice that the right-hand bound is **completely independent of dimension $p$**! Whether $p = 10$ or $p = 10,000,000$, an $L$-Lipschitz functional of a Gaussian random vector deviates from its mean by more than $t$ with probability bounded strictly by $2 e^{-t^2 / 2L^2}$.

Consider the Euclidean norm functional $f(\mathbf{x}) = \|\mathbf{x}\|_2$. By the triangle inequality:
| \|\mathbf{x}\|_2 - \|\mathbf{y}\|_2 | \le \|\mathbf{x} - \mathbf{y}\|_2 \implies L = 1
Therefore, for $\mathbf{X} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_p)$:
$$P\left( \left| \|\mathbf{X}\|_2 - \sqrt{p} \right| \ge t \right) \le 2 e^{-t^2 / 2}$$
The length of a standard normal random vector in $\mathbb{R}^p$ is concentrated inside a thin spherical shell of thickness $O(1)$ around radius $\sqrt{p}$, with Gaussian tail decay.

## 1.8 High-Dimensional Convex Geometry: Dvoretzky's Theorem and John's Ellipsoid

In low dimensions, convex bodies exhibit varied shapes: cubes have sharp vertices, tetrahedra have triangular faces, and cylinders have flat caps. In high dimensions, however, Aryeh Dvoretzky (1961) proved that all convex bodies behave essentially like Euclidean spheres when sliced along low-dimensional subspaces.

### 1. Dvoretzky's Theorem on Spherical Sections
Let $K \subset \mathbb{R}^p$ be an arbitrary centrally symmetric convex body (such as a high-dimensional hypercube $[-1, 1]^p$ or cross-polytope). 

*Theorem (Dvoretzky 1961, Milman 1971)*: For any distortion $\epsilon \in (0, 1)$, there exists a subspace $E \subset \mathbb{R}^p$ of dimension:
$$k \ge c(\epsilon) \ln p$$
such that the intersection $K \cap E$ is $(1 + \epsilon)$-isomorphic to a Euclidean ball:
$$(1 - \epsilon) r B_2^k \subseteq K \cap E \subseteq (1 + \epsilon) r B_2^k$$
where $B_2^k$ is the standard $k$-dimensional Euclidean unit ball.

Every symmetric convex body in high dimensions possesses lower-dimensional cross-sections that are almost perfectly spherical. In statistical machine learning, this guarantees that linear projections of arbitrary bounded data features onto logarithmic subspaces produce isotropic, spherically symmetric distributions.

### 2. John's Ellipsoid Theorem
Fritz John (1948) established the maximal containment of Euclidean ellipsoids within arbitrary convex bodies.

*Theorem (John's Theorem)*: For any convex body $K \subset \mathbb{R}^p$, there exists a unique ellipsoid of maximal volume $E_J \subseteq K$ (the John Ellipsoid). Furthermore, if $K$ is centrally symmetric about the origin, dilating $E_J$ by a factor of $\sqrt{p}$ completely encloses $K$:
$$E_J \subseteq K \subseteq \sqrt{p} \, E_J$$

This theorem provides the fundamental theoretical bound for preconditioning high-dimensional convex optimization problems and volume estimation algorithms.

## 1.9 Non-Asymptotic Random Matrix Bounds: Covariance Concentration

In Section 1.2, we noted that empirical sample covariance matrices $\mathbf{S} = \frac{1}{n} \mathbf{X}^T \mathbf{X}$ are inconsistent when $p/n \to \gamma > 0$. Roman Vershynin (2012) and Joel Tropp (2015) developed non-asymptotic matrix concentration inequalities that quantify the exact sample size $n$ required to guarantee that $\mathbf{S}$ approximates the population covariance $\mathbf{\Sigma} = \mathbf{I}_p$ in operator norm.

*Theorem (Vershynin's Sub-Gaussian Covariance Theorem)*: Let $\mathbf{x}_1, \dots, \mathbf{x}_n$ be independent sub-Gaussian random vectors in $\mathbb{R}^p$ with $\mathbb{E}[\mathbf{x}] = \mathbf{0}$ and covariance $\mathbb{E}[\mathbf{x} \mathbf{x}^T] = \mathbf{I}_p$. Let the sub-Gaussian norm be $\|\mathbf{x}\|_{\psi_2} \le K$.
Then for any $\epsilon \in (0, 1)$ and $t \ge 0$, with probability at least $1 - 2 e^{-t^2}$:
$$\left\| \frac{1}{n} \sum_{i=1}^n \mathbf{x}_i \mathbf{x}_i^T - \mathbf{I}_p \right\|_{\text{op}} \le C K^2 \left( \sqrt{\frac{p}{n}} + \frac{t}{\sqrt{n}} \right)$$
where $\|\mathbf{A}\|_{\text{op}} = \sup_{\|\mathbf{v}\|_2 = 1} \|\mathbf{A} \mathbf{v}\|_2 = \sigma_{\max}(\mathbf{A})$ is the operator (spectral) norm.

*Fundamental Sample Complexity Law*: To guarantee that the sample covariance matrix approximates the true covariance within spectral relative error $\epsilon$ ($\|\mathbf{S} - \mathbf{I}_p\|_{\text{op}} \le \epsilon$), the required sample size must scale linearly with dimension:
$$n \ge C \left( \frac{K^2}{\epsilon} \right)^2 p = O(p)$$
If $n < p$, the operator norm error $\|\mathbf{S} - \mathbf{I}_p\|_{\text{op}} \ge 1.0$, confirming that unregularized covariance estimation fails completely whenever sample size is smaller than the feature dimension.
"""

# -------------------------------------------------------------
# UNIT 2 EXPANSION
# -------------------------------------------------------------
u2_exp = r"""
## 2.6 The Tracy-Widom Distribution and the Spectral Edge

In Section 2.2, we established that the empirical eigenvalues of a null sample covariance matrix $\mathbf{S} = \frac{1}{n} \mathbf{X}^T \mathbf{X}$ are asymptotically bounded by the Marchenko-Pastur upper edge $\lambda_+ = \sigma^2 (1 + \sqrt{\gamma})^2$.
However, in finite samples, what is the exact distribution of the maximum eigenvalue $\hat{\lambda}_1 = \lambda_{\max}(\mathbf{S})$ around this boundary?

Craig Tracy and Harold Widom (1994, 1996) proved a landmark theorem in mathematical physics and random matrix theory, establishing the universal limiting distribution of the largest eigenvalue of Gaussian random matrices.

### 1. The Tracy-Widom $F_1$ Distribution
Let $\mathbf{X}$ be an $n \times p$ matrix with independent standard Gaussian entries $\mathcal{N}(0, 1)$, and let $\hat{\lambda}_1$ be the largest eigenvalue of the sample covariance matrix $\mathbf{S} = \frac{1}{n} \mathbf{X}^T \mathbf{X}$.
Define the centering and scaling constants:
$$\mu_{n, p} = \left( 1 + \sqrt{\frac{p}{n}} \right)^2$$
$$\sigma_{n, p} = \left( 1 + \sqrt{\frac{p}{n}} \right) \left( 1 + \sqrt{\frac{n}{p}} \right)^{1/3} n^{-2/3}$$

*Theorem (Johnstone 2001)*: As $n, p \to \infty$ with $p/n \to \gamma > 0$, the normalized leading eigenvalue converges weakly to the **Tracy-Widom $F_1$ Law**:

$$\frac{\hat{\lambda}_1 - \mu_{n, p}}{\sigma_{n, p}} \xrightarrow{d} \mathrm{TW}_1$$

The cumulative distribution function $F_1(s)$ is given by the Painlevé II non-linear differential equation:
$$F_1(s) = \exp\left( -\frac{1}{2} \int_s^\infty q(x) + (x - s) q^2(x)\,dx \right)$$
where $q(x)$ satisfies the Painlevé II differential equation $q''(x) = x q(x) + 2 q^3(x)$ with boundary condition $q(x) \sim \text{Ai}(x)$ as $x \to \infty$, where $\text{Ai}(x)$ is the classical Airy function.

*Statistical Testing Implication*: The Tracy-Widom distribution replaces the classical Student's $t$ or Fisher's $F$ distribution when testing for the existence of low-rank signals in high dimensions. If the normalized test statistic exceeds the $95\%$ critical quantile of $\mathrm{TW}_1$ ($s_{0.95} \approx 0.979$ or $s_{0.99} \approx 2.023$), the analyst rigorously rejects the null hypothesis of pure noise and declares the presence of a genuine latent factor.

## 2.7 Sparse PCA for High-Dimensional Variable Selection

While standard PCA finds linear combinations $\mathbf{z}_1 = \mathbf{X} \mathbf{v}_1$ that maximize variance, the resulting eigenvector $\mathbf{v}_1 \in \mathbb{R}^p$ is dense: all $p$ features receive non-zero weights. In genomics or finance with $p = 20,000$ variables, interpreting a linear combination of 20,000 genes is impossible.

Hui Zou, Trevor Hastie, and Robert Tibshirani (2006) formulated **Sparse PCA**, using $L_1$ regularization to force most eigenvector loadings to zero.

### 1. Regression Formulation of PCA
Zou, Hastie, and Tibshirani demonstrated that PCA can be formulated as a self-reconstruction regression problem:
$$\min_{\mathbf{A}, \mathbf{B}} \sum_{i=1}^n \|\mathbf{x}_i - \mathbf{A} \mathbf{B}^T \mathbf{x}_i\|_2^2 \quad \text{subject to} \quad \mathbf{A}^T \mathbf{A} = \mathbf{I}_k$$
where $\mathbf{A}, \mathbf{B} \in \mathbb{R}^{p \times k}$. For unconstrained optimization, the columns of $\mathbf{B}$ are proportional to the standard principal component eigenvectors.

### 2. The Sparse PCA Objective
Sparse PCA imposes an Elastic Net penalty on the reconstruction matrix $\mathbf{B}$:
$$\min_{\mathbf{A}, \mathbf{B}} \left\{ \sum_{i=1}^n \|\mathbf{x}_i - \mathbf{A} \mathbf{B}^T \mathbf{x}_i\|_2^2 + \lambda \sum_{j=1}^k \|\boldsymbol{\beta}_j\|_2^2 + \sum_{j=1}^k \lambda_{1, j} \|\boldsymbol{\beta}_j\|_1 \right\} \quad \text{subject to} \quad \mathbf{A}^T \mathbf{A} = \mathbf{I}_k$$
This non-convex optimization is solved via alternating minimization:
1. For fixed $\mathbf{A}$, updating each column $\boldsymbol{\beta}_j$ is an Elastic Net regression, solved rapidly via coordinate descent.
2. For fixed $\mathbf{B}$, updating $\mathbf{A}$ is a Procrustes problem solved via SVD: $\mathbf{X}^T \mathbf{X} \mathbf{B} = \mathbf{U} \mathbf{D} \mathbf{V}^T \implies \mathbf{A} = \mathbf{U} \mathbf{V}^T$.

Sparse PCA produces orthogonal principal directions driven by a small, interpretable subset of 10 to 50 active genes, providing clear biological discovery attribution.

## 2.8 Uniform Manifold Approximation and Projection (UMAP)

In Section 2.4, we examined t-SNE for non-linear manifold visualization. While t-SNE produces compelling 2D cluster maps, it has two significant drawbacks:
1. It scales as $O(n^2)$ (or $O(n \log n)$ via Barnes-Hut quad-trees), taking hours on datasets with $n \ge 10^6$ rows.
2. It destroys **global manifold structure**: the relative distances between distant clusters in a t-SNE plot are arbitrary and carry zero statistical meaning.

Leland McInnes, John Healy, and James Melville (2018) developed **UMAP**, grounded in Riemannian geometry and algebraic topology (fuzzy simplicial sets).

### 1. Theoretical Foundations of UMAP
UMAP assumes that data reside on a local Riemannian manifold $\mathcal{M}$ where the metric space is locally connected.
1. **Local Metric Scaling**: In high dimensions, the local geodesic distance around each point $\mathbf{x}_i$ is normalized by its distance to its nearest neighbor $\rho_i$ and a local scale $\sigma_i$:
$$p_{i|j} = \exp\left( -\frac{\max(0, d(\mathbf{x}_i, \mathbf{x}_j) - \rho_i)}{\sigma_i} \right)$$
Setting $\rho_i = \min_{k} d(\mathbf{x}_i, \mathbf{x}_k)$ guarantees that the local graph is connected at each point, overcoming density disparities.
2. **Fuzzy Union**: Symmetrized high-dimensional affinities are constructed via the algebraic t-conorm:
$$p_{ij} = p_{i|j} + p_{j|i} - p_{i|j} p_{j|i}$$
3. **Low-Dimensional Embeddings**: In the target 2D space, the similarity is modeled via a smooth family of curves:
$$q_{ij} = \left( 1 + a \|\mathbf{y}_i - \mathbf{y}_j\|_2^{2b} \right)^{-1}$$
where $a, b$ are hyperparameters chosen to match the target min-dist setting.
4. **Fuzzy Set Cross-Entropy Minimization**: UMAP optimizes the coordinates $\mathbf{y}_i$ by minimizing the fuzzy set cross-entropy:
$$\mathcal{C}(P, Q) = \sum_{i \ne j} \left[ p_{ij} \log\left(\frac{p_{ij}}{q_{ij}}\right) + (1 - p_{ij}) \log\left(\frac{1 - p_{ij}}{1 - q_{ij}}\right) \right]$$
Because the second term penalizes pairs where $p_{ij} = 0$ but $q_{ij} > 0$, UMAP actively pushes disconnected clusters apart, preserving global topological hierarchies while executing 10 to 50 times faster than t-SNE via stochastic gradient descent and negative sampling.
"""

# -------------------------------------------------------------
# UNIT 3 EXPANSION
# -------------------------------------------------------------
u3_exp = r"""
## 3.6 Theoretical Oracle Properties and the Restricted Isometry Property

In Section 3.2, we established that the Lasso performs simultaneous variable selection and shrinkage. But under what mathematical conditions does the Lasso select the **exact true subset of active variables** with probability approaching 1.0 as $n \to \infty$?

Peter Bickel, Ya'acov Ritov, and Alexandre Tsybakov (2009), alongside Emmanuel Candès and Terence Tao (2007), established the non-asymptotic oracle theory of high-dimensional sparse recovery.

### 1. The Restricted Isometry Property (RIP)
Let $\mathbf{X} \in \mathbb{R}^{n \times p}$ be the design matrix. For an integer $s \le p$, the matrix $\mathbf{X}$ satisfies the **Restricted Isometry Property (RIP)** of order $s$ with constant $\delta_s \in (0, 1)$ if for all $s$-sparse vectors $\mathbf{v} \in \mathbb{R}^p$ ($\|\mathbf{v}\|_0 \le s$):

$$(1 - \delta_s) \|\mathbf{v}\|_2^2 \le \frac{1}{n} \|\mathbf{X} \mathbf{v}\|_2^2 \le (1 + \delta_s) \|\mathbf{v}\|_2^2$$

*Intuition*: Although $\mathbf{X}^T \mathbf{X}$ is singular when viewed over the entire $p$-dimensional space, when restricted to any small sub-collection of $s$ columns, the sub-matrix $\mathbf{X}_S$ acts as a near-isometry (all sub-matrix singular values lie inside $[\sqrt{1 - \delta_s}, \sqrt{1 + \delta_s}]$).

### 2. The Restricted Eigenvalue (RE) Condition
A slightly weaker, more general condition that guarantees optimal Lasso estimation is the **Restricted Eigenvalue Condition**:
$$\kappa(s, c_0) = \min_{|S| \le s} \min_{\mathbf{v} \in \mathcal{C}(S, c_0), \mathbf{v} \ne \mathbf{0}} \frac{\|\mathbf{X} \mathbf{v}\|_2}{\sqrt{n} \|\mathbf{v}_S\|_2} > 0$$
where $\mathcal{C}(S, c_0) = \{ \mathbf{v} \in \mathbb{R}^p : \|\mathbf{v}_{S^c}\|_1 \le c_0 \|\mathbf{v}_S\|_1 \}$ is the cone of vectors whose $L_1$ mass is concentrated on the active support set $S$.

*Theorem (Bickel, Ritov, Tsybakov 2009)*: Suppose the linear model is truly sparse with active set $S = \{j : \beta_j^* \ne 0\}$ of cardinality $s = |S|$, and the design matrix satisfies the RE condition with constant $\kappa > 0$. If the regularization parameter is chosen as:
$$\lambda = 4 \sigma \sqrt{\frac{2 \ln p}{n}}$$
then with probability at least $1 - p^{-1}$, the Lasso estimator satisfies the **Oracle Prediction and Estimation Bounds**:

$$\frac{1}{n} \|\mathbf{X}(\hat{\boldsymbol{\beta}}_{\text{lasso}} - \boldsymbol{\beta}^*)\|_2^2 \le \frac{16 \sigma^2}{\kappa^2} \frac{s \ln p}{n}$$
$$\|\hat{\boldsymbol{\beta}}_{\text{lasso}} - \boldsymbol{\beta}^*\|_2 \le \frac{4 \sigma}{\kappa^2} \sqrt{\frac{s \ln p}{n}}$$
$$\|\hat{\boldsymbol{\beta}}_{\text{lasso}} - \boldsymbol{\beta}^*\|_1 \le \frac{16 \sigma}{\kappa^2} s \sqrt{\frac{\ln p}{n}}$$

*Profound Takeaway*: The estimation error depends logarithmically on the total number of candidate variables ($\ln p$) and linearly on the true intrinsic sparsity $s$. In a dataset with $p = 1,000,000$ variables where only $s = 10$ genes drive disease, the effective dimension is governed by $s \ln p = 10 \times \ln(10^6) \approx 138$, enabling accurate estimation with modest sample sizes ($n \approx 1,000$).

## 3.7 Non-Convex Penalties: SCAD and MCP

While the Lasso achieves sparsity, its $L_1$ penalty $|\beta_j|$ has a fundamental theoretical defect: it applies constant penalization $\lambda$ regardless of the magnitude of $|\beta_j|$. For large coefficients ($|\beta_j| \gg 0$), the Lasso continues to shrink them toward zero by $\lambda$, introducing non-vanishing estimation bias.

Jianqing Fan and Runze Li (2001) established the **Oracle Criteria** for penalized likelihood estimators:
1. **Unbiasedness**: The penalty derivative $p'_\lambda(|\beta|) \to 0$ as $|\beta| \to \infty$, ensuring zero bias on large coefficients.
2. **Sparsity**: The thresholding operator produces exact zeros for small coefficients.
3. **Continuity**: The thresholding rule is continuous to avoid instability in model prediction.

The $L_1$ penalty satisfies sparsity and continuity, but fails unbiasedness. $L_0$ penalization (AIC/BIC) satisfies unbiasedness and sparsity, but fails continuity.

### 1. The SCAD Penalty (Smoothly Clipped Absolute Deviation)
Fan and Li designed the **SCAD** penalty with derivative:
$$p'_\lambda(\theta) = \lambda \left\{ \mathbb{I}(\theta \le \lambda) + \frac{(a \lambda - \theta)_+}{(a - 1) \lambda} \mathbb{I}(\theta > \lambda) \right\}, \quad \text{for } a > 2 \text{ (typically } a = 3.7\text{)}$$
SCAD transitions smoothly from an $L_1$ penalty for small values $|\theta| \le \lambda$, to a quadratic spline for intermediate values, to a flat constant for large values $|\theta| > a \lambda$. Large coefficients experience **zero shrinkage**, eliminating asymptotic bias.

### 2. The MCP Penalty (Minimax Concave Penalty)
Cun-Hui Zhang (2010) formulated the **MCP** penalty:
$$p_\lambda(\theta) = \lambda \int_0^{|\theta|} \left( 1 - \frac{x}{\gamma \lambda} \right)_+ dx$$
MCP relaxes penalization continuously from $\lambda$ down to $0$ as $|\theta|$ reaches the threshold $\gamma \lambda$, providing the minimax optimal bound on maximum shrinkage bias while preserving exact sparsity.

## 3.8 The Graphical Lasso (Glasso) for High-Dimensional Precision Matrices

In multivariate analysis, the inverse covariance matrix $\mathbf{\Theta} = \mathbf{\Sigma}^{-1}$ is known as the **Precision Matrix** (or Concentration Matrix). Under a multivariate Gaussian distribution $\mathbf{X} \sim \mathcal{N}(\mathbf{0}, \mathbf{\Sigma})$, the off-diagonal entries $\Theta_{jk}$ have an exact conditional independence interpretation:
$$\Theta_{jk} = 0 \iff X_j \perp X_k \mid \mathbf{X}_{-(j, k)}$$
Variables $X_j$ and $X_k$ are conditionally independent given all remaining variables if and only if $\Theta_{jk} = 0$.

In high dimensions ($p \gg n$), the sample covariance matrix $\mathbf{S}$ is singular, so it cannot be inverted to compute precision.
Jerome Friedman, Trevor Hastie, and Robert Tibshirani (2008) formulated the **Graphical Lasso (Glasso)**, maximizing the penalized Gaussian log-likelihood:

$$\max_{\mathbf{\Theta} \succ 0} \left\{ \ln \det \mathbf{\Theta} - \mathrm{Tr}(\mathbf{S} \mathbf{\Theta}) - \lambda \|\mathbf{\Theta}\|_{1, \text{off}} \right\}$$
where $\|\mathbf{\Theta}\|_{1, \text{off}} = \sum_{j \ne k} |\Theta_{jk}|$ penalizes off-diagonal precision entries.

Friedman et al. proved that solving this matrix optimization is equivalent to solving $p$ coupled Lasso regression problems. The algorithm cycles sequentially through variables $j = 1, \dots, p$, regressing variable $j$ onto all other $p-1$ variables using coordinate descent. The resulting zero entries $\Theta_{jk} = 0$ reconstruct the sparse conditional independence network (e.g., gene regulatory networks, financial contagion graphs) in seconds.
"""

# -------------------------------------------------------------
# UNIT 4 EXPANSION
# -------------------------------------------------------------
u4_exp = r"""
## 4.6 Statistical Theory of Distributed M-Estimation

When data are partitioned across $K$ worker machines, running iterative gradient algorithms requiring frequent communication is often impractical over high-latency networks. 

A natural distributed strategy is **One-Shot Parameter Averaging** (Divide-and-Conquer):
1. Distribute $N$ observations across $K$ nodes, so each node holds a local sample of size $n = N/K$.
2. Each worker computes its local M-estimator independently:
$$\hat{\boldsymbol{\theta}}_k = \arg\min_{\boldsymbol{\theta}} \frac{1}{n} \sum_{i \in \mathcal{S}_k} \ell(\mathbf{x}_i; \boldsymbol{\theta})$$
3. Transmit the $K$ local vectors to a central coordinator and compute the simple average:
$$\bar{\boldsymbol{\theta}} = \frac{1}{K} \sum_{k=1}^K \hat{\boldsymbol{\theta}}_k$$

Yuchen Zhang, John C. Duchi, and Martin J. Wainwright (2013) established the exact statistical efficiency bounds of this one-shot scheme.

### Asymptotic Mean Squared Error Expansion
Let $\boldsymbol{\theta}^*$ be the true parameter, and let $\ell$ be a smooth loss function with Fisher information matrix $\mathbf{I}(\boldsymbol{\theta}^*)$.
The local M-estimator on worker $k$ admits a second-order Taylor expansion:
$$\hat{\boldsymbol{\theta}}_k - \boldsymbol{\theta}^* = \frac{1}{n} \sum_{i \in \mathcal{S}_k} \mathbf{I}^{-1} \nabla \ell(\mathbf{x}_i; \boldsymbol{\theta}^*) + \frac{1}{n^2} \mathbf{b}(\boldsymbol{\theta}^*) + O_p(n^{-3/2})$$
where $\mathbf{b}(\boldsymbol{\theta}^*)$ is the second-order bias term originating from the non-linearity of the score function.

Averaging across the $K$ workers:
$$\bar{\boldsymbol{\theta}} - \boldsymbol{\theta}^* = \frac{1}{N} \sum_{i=1}^N \mathbf{I}^{-1} \nabla \ell(\mathbf{x}_i; \boldsymbol{\theta}^*) + \frac{1}{n^2} \mathbf{b}(\boldsymbol{\theta}^*) + O_p\left( \frac{1}{K n^{3/2}} \right)$$
The Mean Squared Error (MSE) decomposes into variance and squared bias:
$$\mathbb{E}[\|\bar{\boldsymbol{\theta}} - \boldsymbol{\theta}^*\|_2^2] = \underbrace{\frac{\mathrm{Tr}(\mathbf{I}^{-1})}{N}}_{\text{Optimal Centralized Variance } O(1/N)} + \underbrace{\frac{\|\mathbf{b}\|_2^2}{n^4}}_{\text{Accumulated Bias Squared } O(K^4 / N^4)}$$

*Theorem (Zhang, Duchi, Wainwright 2013)*: If the number of worker nodes satisfies:
$$K \le \sqrt{N}$$
(meaning local sample size $n = N/K \ge \sqrt{N}$), then the squared bias term $O(n^{-4})$ is asymptotically dominated by the variance $O(1/N)$.
Under this condition, **one-shot parameter averaging achieves the exact minimax optimal statistical efficiency of a centralized supercomputer** while transmitting data across the network exactly once!

## 4.7 Columnar In-Memory Formats: Apache Parquet and Apache Arrow

In big data analytics, the physical layout of statistical tables in memory and on disk dictates computational performance.
Historically, database systems stored data in **Row-Oriented** formats (e.g., CSV, JSON, relational database rows):
`Record 1: [ID, Age, Income, Diagnosis]`
`Record 2: [ID, Age, Income, Diagnosis]`

### 1. The Columnar Revolution: Apache Parquet
In statistical analysis, queries rarely access all columns: an econometric regression model $Y \sim X_1 + X_2$ extracts 3 columns out of a dataset containing 2,000 columns.
In a row-oriented file, the computer must read every byte of all 2,000 columns from disk, discarding $99.8\%$ of data in memory.

**Apache Parquet** stores data in **Columnar Format**:
`Age:     [25, 42, 67, ...]`
`Income:  [55000, 82000, 110000, ...]`
`Disease: [0, 1, 0, ...]`

Advantages for statisticians:
1. **Projection Pushdown (Column Pruning)**: Disk reads fetch only the exact bytes corresponding to variables included in the model, slashing disk I/O by $95\%$ to $99\%$.
2. **Homogeneous Data Compression**: Because all values in a column share the identical data type, specialized columnar encoding algorithms (Run-Length Encoding - RLE, Dictionary Encoding, Delta Encoding) achieve $10\times$ higher compression ratios than row-based formats.
3. **Predicate Pushdown**: Parquet files record the minimum and maximum values (`min/max` metadata) for every block of data. If a query filters `WHERE Age > 65`, blocks where `max(Age) < 65` are skipped entirely without reading a single record.

### 2. Zero-Copy In-Memory Interoperability: Apache Arrow
Even when data are stored efficiently on disk, moving data between different statistical environments (e.g., passing a Spark DataFrame to Python Pandas or R) historically required expensive serialization and deserialization (copying memory and converting types), consuming $80\%$ of runtime.

**Apache Arrow** standardizes an in-memory columnar memory specification across languages (C++, Python, R, Java, Rust). Because all engines adhere to the identical memory layout:
- Data are shared via shared-memory pointers (**Zero-Copy Data Transfer**).
- Computational routines execute SIMD (Single Instruction Multiple Data) vector instructions directly over contiguous memory arrays, processing billions of rows per second.
"""

def main():
    append_to_unit(1, u1_exp)
    append_to_unit(2, u2_exp)
    append_to_unit(3, u3_exp)
    append_to_unit(4, u4_exp)
    print("Units 1-4 expanded.")

if __name__ == "__main__":
    main()
