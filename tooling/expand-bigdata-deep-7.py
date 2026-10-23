#!/usr/bin/env python3
"""
Deep Expansion Pass 7 for Big Data Methods for Statistics (Book 16) - Units 1 to 4.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")
    print(f"Unit {unit_num} deep pass 7 applied.")

# -------------------------------------------------------------
# UNIT 1
# -------------------------------------------------------------
u1_deep7 = r"""
## 1.17 High-Dimensional Classification: The Independence Rule and FAIR

In classical discriminant analysis, Fisher's Linear Discriminant Analysis (LDA) classifies observations $\mathbf{x} \in \mathbb{R}^p$ between two Gaussian populations $\mathcal{N}(\boldsymbol{\mu}_1, \mathbf{\Sigma})$ and $\mathcal{N}(\boldsymbol{\mu}_2, \mathbf{\Sigma})$ using the rule:
$$\delta(\mathbf{x}) = (\boldsymbol{\mu}_1 - \boldsymbol{\mu}_2)^T \mathbf{\Sigma}^{-1} \left( \mathbf{x} - \frac{\boldsymbol{\mu}_1 + \boldsymbol{\mu}_2}{2} \right) > 0$$

Peter Bickel and Elizaveta Levina (2004) proved a shocking theorem: in high dimensions where $p/n \to \infty$, **classical Fisher's LDA is no better than a random coin flip**: its asymptotic classification error rate approaches $50\%$!
Because inverting the empirical covariance matrix $\mathbf{S}^{-1}$ accumulates excessive estimation noise across $p$ dimensions, the estimated discriminant vector diverges away from the true separating hyperplane.

### 1. Bickel and Levina's Independence Rule
Bickel and Levina proposed ignoring all correlations between features entirely, replacing $\mathbf{S}$ with its diagonal matrix $\mathbf{D} = \mathrm{diag}(S_{11}, \dots, S_{pp})$:
$$\delta_{\text{ind}}(\mathbf{x}) = \sum_{j=1}^p \frac{(\bar{X}_{1j} - \bar{X}_{2j})}{S_{jj}} \left( X_j - \frac{\bar{X}_{1j} + \bar{X}_{2j}}{2} \right)$$
Even when the true population features are correlated, setting off-diagonal covariances to zero dramatically suppresses variance, outperforming full Fisher LDA in high dimensions.

### 2. The Feature Annealed Independence Rule (FAIR)
Jianqing Fan and Yingying Fan (2008) observed that while the Independence Rule eliminates covariance estimation noise, summing across thousands of uninformative noise features still degrades accuracy.

Fan and Fan formulated **FAIR (Feature Annealed Independence Rule)**:
1. Compute the two-sample $t$-statistic for each individual feature:
$$T_j = \frac{\bar{X}_{1j} - \bar{X}_{2j}}{\sqrt{S_{jj} (1/n_1 + 1/n_2)}}$$
2. Select only the subset of features whose marginal $t$-statistics exceed an annealed threshold $|T_j| \ge \tau$:
$$\hat{S} = \{ j : |T_j| \ge \tau \}$$
3. Apply the independence rule exclusively to the filtered subset $\hat{S}$.

FAIR discards thousands of irrelevant noise features, restoring optimal classification consistency even when $p$ is exponentially larger than $n$.

## 1.18 Asymptotic Normality of High-Dimensional Projections: Diaconis-Freedman Theorem

Persi Diaconis and David Freedman (1984) established a beautiful and reassuring theorem about random projections of high-dimensional data points:

*Theorem (Diaconis-Freedman Projection Theorem)*: Let $\mathbf{x}_1, \dots, \mathbf{x}_n$ be deterministic points in $\mathbb{R}^p$ satisfying mild dispersion conditions ($\frac{1}{n} \sum \|\mathbf{x}_i\|_2^2 \approx p$). If a 1-dimensional projection vector $\mathbf{v}$ is chosen uniformly at random from the unit hypersphere $\mathbb{S}^{p-1}$, then as $p \to \infty$:
The empirical distribution of the projected coordinates $\{\langle \mathbf{v}, \mathbf{x}_1 \rangle, \dots, \langle \mathbf{v}, \mathbf{x}_n \rangle\}$ converges weakly to a **Standard Gaussian Distribution $\mathcal{N}(0, 1)$**.

*Statistical Intuition*: No matter how wildly non-Gaussian, multimodal, or structured the original dataset is in $\mathbb{R}^p$, almost every 1D or 2D linear projection of the dataset appears as a Gaussian bell curve! This explains why linear dimension reduction techniques often uncover Gaussian-like clouds, and underscores why non-linear manifold learning (such as t-SNE and UMAP) is necessary to reveal non-Gaussian manifold geometry.
"""

# -------------------------------------------------------------
# UNIT 2
# -------------------------------------------------------------
u2_deep7 = r"""
## 2.16 Multidimensional Scaling (MDS) and Landmark Approximations

When data relationships are provided not as coordinate vectors $\mathbf{x} \in \mathbb{R}^p$, but as an $n \times n$ matrix of pairwise dissimilarities or distances $\mathbf{D} = [d_{ij}]$ (such as psychological confusion matrices, genetic sequence alignment edit distances, or graph shortest-path geodesic hops), classical vector space techniques cannot be applied directly.

Warren S. Torgerson (1952) and Joseph Kruskal (1964) formulated **Multidimensional Scaling (MDS)**, finding low-dimensional Euclidean points $\mathbf{y}_1, \dots, \mathbf{y}_n \in \mathbb{R}^d$ such that $\|\mathbf{y}_i - \mathbf{y}_j\|_2 \approx d_{ij}$.

### 1. Classical Metric MDS
1. Compute the squared distance matrix $\mathbf{D}^{(2)}$ where $D_{ij}^{(2)} = d_{ij}^2$.
2. Apply double centering via the centering matrix $\mathbf{H} = \mathbf{I}_n - \frac{1}{n} \mathbf{1} \mathbf{1}^T$:
$$\mathbf{B} = -\frac{1}{2} \mathbf{H} \mathbf{D}^{(2)} \mathbf{H}$$
By the law of cosines, $\mathbf{B}$ is the inner product Gram matrix $\mathbf{Y} \mathbf{Y}^T$.
3. Compute the spectral decomposition of $\mathbf{B} = \mathbf{V} \mathbf{\Lambda} \mathbf{V}^T$.
4. The optimal $d$-dimensional Euclidean coordinates are:
$$\mathbf{Y} = \mathbf{V}_d \mathbf{\Lambda}_d^{1/2}$$

### 2. Landmark MDS for Massive Datasets
When $n \ge 100,000$, classical MDS requires storing the $100,000 \times 100,000$ matrix $\mathbf{D}$ (80 GB) and computing its full eigendecomposition in $O(n^3)$ operations.
Vin de Silva and Joshua B. Tenenbaum (2004) developed **Landmark MDS (LMDS)**:
1. Select $m \ll n$ landmark points (e.g., $m = 1,000$).
2. Compute the $m \times m$ distance matrix between landmarks and run classical MDS to obtain landmark coordinates $\mathbf{Y}_m \in \mathbb{R}^{m \times d}$.
3. For all remaining $n - m$ points, project them into the coordinate system via distance-based triangulation in $O(n m d)$ operations.

LMDS enables real-time metric embedding of multi-million point distance graphs on standard laptops.

## 2.17 Spectral Clustering and Cheeger's Inequality

In big data graph analytics, clustering data points into cohesive communities is framed as finding a minimal cut across the data affinity graph $G = (V, E)$.

Jianbo Shi and Jitendra Malik (2000), alongside Andrew Y. Ng, Michael I. Jordan, and Yair Weiss (2001), developed **Spectral Clustering**:
1. Construct the normalized graph Laplacian $\mathbf{L}_{\text{sym}} = \mathbf{D}^{-1/2} (\mathbf{D} - \mathbf{W}) \mathbf{D}^{-1/2} = \mathbf{I} - \mathbf{D}^{-1/2} \mathbf{W} \mathbf{D}^{-1/2}$.
2. Compute the $k$ eigenvectors $\mathbf{v}_1, \dots, \mathbf{v}_k$ corresponding to the $k$ smallest eigenvalues of $\mathbf{L}_{\text{sym}}$.
3. Normalize the rows of the resulting $n \times k$ matrix to unit length.
4. Run standard $k$-means clustering on the low-dimensional spectral embedding.

*Cheeger's Inequality for Graphs*: The second eigenvalue $\lambda_2$ (the Fiedler value) governs the graph conductances $\phi(G)$:
$$\frac{\lambda_2}{2} \le \phi(G) \le \sqrt{2 \lambda_2}$$
Spectral clustering provides a polynomial-time relaxation to the NP-hard Normalized Cut objective, reliably discovering non-convex, intertwining clusters where classical $k$-means fails completely.
"""

# -------------------------------------------------------------
# UNIT 3
# -------------------------------------------------------------
u3_deep7 = r"""
## 3.16 The Adaptive Lasso and Minimax Optimal Oracle Recovery

In Unit 3.2, we established that while the standard Lasso performs variable selection, it applies uniform shrinkage $\lambda$ to all coefficients, introducing asymptotic bias into large coefficients and requiring strict irrepresentable conditions to select the exact true model.

Hui Zou (2006) introduced the **Adaptive Lasso**, assigning data-driven weights $w_j$ to individual feature penalties:

$$\min_{\boldsymbol{\beta}} \left\{ \frac{1}{2n} \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2 + \lambda \sum_{j=1}^p w_j |\beta_j| \right\}$$
where the adaptive weights are defined using an initial consistent estimator $\hat{\boldsymbol{\beta}}_{\text{init}}$ (such as OLS when $p < n$ or Ridge when $p > n$):
$$w_j = \frac{1}{|\hat{\beta}_{j, \text{init}}|^\gamma}, \quad \text{for } \gamma > 0 \text{ (typically } \gamma = 1 \text{ or } 2\text{)}$$

### The Adaptive Penalty Mechanism
- If a predictor has a large true effect ($|\beta_j^*| \gg 0$), the initial estimate $|\hat{\beta}_{j, \text{init}}|$ is large, causing weight $w_j \to 0$. The variable experiences **virtually zero shrinkage**, eliminating bias!
- If a predictor is a null noise variable ($\beta_j^* = 0$), the initial estimate $|\hat{\beta}_{j, \text{init}}| \to 0$, causing weight $w_j \to \infty$. The variable is aggressively shrunk to zero with high probability.

*Theorem (Zou's Oracle Property Theorem)*: Under mild regularity conditions, if $\lambda_n \to 0$ and $\lambda_n n^{\gamma/2} \to \infty$, the Adaptive Lasso satisfies the **Oracle Properties**:
1. **Model Selection Consistency**: $P(\hat{S}_{\text{alasso}} = S^*) \to 1.0$ as $n \to \infty$.
2. **Asymptotic Normality**: The non-zero coefficients converge to the true parameters at the optimal parametric rate, with the exact asymptotic covariance matrix of the true sub-model:
$$\sqrt{n}(\hat{\boldsymbol{\beta}}_{S^*} - \boldsymbol{\beta}_{S^*}^*) \xrightarrow{d} \mathcal{N}\left( \mathbf{0}, \sigma^2 (\mathbf{X}_{S^*}^T \mathbf{X}_{S^*})^{-1} \right)$$
The Adaptive Lasso achieves the theoretical gold standard of statistical estimation while retaining the computational speed of convex coordinate descent.

## 3.17 The Non-Negative Garrote

Before the invention of the Lasso, Leo Breiman (1995) introduced the **Non-Negative Garrote**, providing the earliest continuous shrinkage and variable selection algorithm.

Starting from the unconstrained Ordinary Least Squares estimates $\hat{\boldsymbol{\beta}}^{\text{OLS}}$, the garrote introduces non-negative scaling factors $c_j \ge 0$:
$$\beta_j(c) = c_j \hat{\beta}_j^{\text{OLS}}$$
The scaling vector $\mathbf{c} = (c_1, \dots, c_p)^T$ is obtained by solving the constrained optimization:
$$\min_{\mathbf{c}} \sum_{i=1}^n \left( y_i - \sum_{j=1}^p c_j X_{ij} \hat{\beta}_j^{\text{OLS}} \right)^2 \quad \text{subject to} \quad c_j \ge 0, \, \sum_{j=1}^p c_j \le s$$

As the tuning budget $s$ decreases, some $c_j$ hit the boundary constraint $c_j = 0$ exactly, dropping variable $j$ from the model. Breiman demonstrated that the garrote yields lower prediction error than subset selection while exhibiting lower bias than ridge regression, inspiring the subsequent development of the Lasso.
"""

# -------------------------------------------------------------
# UNIT 4
# -------------------------------------------------------------
u4_deep7 = r"""
## 4.15 Distributed Generalized Linear Models (GLMs) via Iterative Reweighted Least Squares

In large-scale biostatistics, epidemiology, and risk modeling, response variables are discrete or non-Gaussian (e.g., binary disease status, Poisson infection counts), modeled via **Generalized Linear Models (GLMs)**:
$$g(\mu_i) = \mathbf{x}_i^T \boldsymbol{\beta}, \quad \mu_i = \mathbb{E}[Y_i \mid \mathbf{x}_i]$$
Fitting GLMs relies on the **Iteratively Reweighted Least Squares (IRLS)** algorithm, which updates parameters via Fisher scoring:
$$\boldsymbol{\beta}_{t+1} = (\mathbf{X}^T \mathbf{W}_t \mathbf{X})^{-1} \mathbf{X}^T \mathbf{W}_t \mathbf{z}_t$$
where $\mathbf{W}_t$ is an $N \times N$ diagonal weight matrix with entries $W_{ii} = \frac{1}{\mathrm{Var}(Y_i) (g'(\mu_i))^2}$, and $\mathbf{z}_t = \mathbf{X} \boldsymbol{\beta}_t + (\mathbf{y} - \boldsymbol{\mu}_t) \odot g'(\boldsymbol{\mu}_t)$ is the working response vector.

### Distributed IRLS in Apache Spark MLlib
When dataset $\mathbf{X}$ has $N = 10^8$ rows partitioned across $K$ worker nodes:
1. Each worker node $k$ holds local partition $(\mathbf{X}^{(k)}, \mathbf{y}^{(k)})$.
2. Worker $k$ receives current parameter vector $\boldsymbol{\beta}_t$ from the driver.
3. In a single parallel pass over local data, worker $k$ computes the local $p \times p$ weighted Gram matrix $\mathbf{G}_k$ and local working vector $\mathbf{h}_k$:
$$\mathbf{G}_k = \mathbf{X}^{(k)T} \mathbf{W}_k \mathbf{X}^{(k)} = \sum_{i \in \mathcal{S}_k} W_{ii} \mathbf{x}_i \mathbf{x}_i^T$$
$$\mathbf{h}_k = \mathbf{X}^{(k)T} \mathbf{W}_k \mathbf{z}_k = \sum_{i \in \mathcal{S}_k} W_{ii} z_i \mathbf{x}_i$$
4. A **Tree-Aggregate** network reduction sums the local matrices across all workers:
$$\mathbf{G} = \sum_{k=1}^K \mathbf{G}_k, \quad \mathbf{h} = \sum_{k=1}^K \mathbf{h}_k$$
5. The central driver solves the $p \times p$ linear system $\mathbf{G} \boldsymbol{\beta}_{t+1} = \mathbf{h}$ in $O(p^3)$ time and broadcasts $\boldsymbol{\beta}_{t+1}$ back to the workers.

Because network communication is $O(p^2 \log K)$ per iteration, distributed IRLS fits exact logistic, Poisson, and Gamma GLMs across hundreds of millions of records in 5 to 8 iterations.
"""

def main():
    append_to_unit(1, u1_deep7)
    append_to_unit(2, u2_deep7)
    append_to_unit(3, u3_deep7)
    append_to_unit(4, u4_deep7)
    print("Units 1-4 deep pass 7 applied.")

if __name__ == "__main__":
    main()
