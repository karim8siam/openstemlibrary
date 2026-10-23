#!/usr/bin/env python3
"""
Deep Expansion Pass 2 for Big Data Methods for Statistics (Book 16) - Units 5 to 8.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")
    print(f"Unit {unit_num} deep pass 2 applied.")

# -------------------------------------------------------------
# UNIT 5 DEEP
# -------------------------------------------------------------
u5_deep = r"""
## 5.7 Natural Gradient Descent and Information Geometry

In standard gradient descent, parameter updates $\Delta \mathbf{w} = -\eta \nabla F(\mathbf{w})$ are defined with respect to the standard Euclidean metric: the update finds the point in a small Euclidean sphere $\|\Delta \mathbf{w}\|_2 \le \epsilon$ that minimizes the loss. 

However, in statistical modeling, parameters $\mathbf{w}$ index probability distributions $p(\mathbf{y} \mid \mathbf{x}; \mathbf{w})$. The Euclidean distance $\|\mathbf{w}_1 - \mathbf{w}_2\|_2$ depends arbitrarily on parameterization: reparameterizing a normal distribution from variance $\sigma^2$ to precision $\tau = 1/\sigma^2$ completely distorts Euclidean distances.

Shun-ichi Amari (1998) introduced **Information Geometry** and **Natural Gradient Descent**, defining step directions invariant to parameterization by measuring distance on the Riemannian manifold of probability distributions using the **Fisher Information Metric**.

### 1. The Fisher Information Metric
The distance between two proximate distributions $p(\cdot; \mathbf{w})$ and $p(\cdot; \mathbf{w} + d\mathbf{w})$ is governed by the second-order Taylor expansion of the Kullback-Leibler divergence:
$$\mathcal{D}_{\text{KL}}(p(\cdot; \mathbf{w}) \parallel p(\cdot; \mathbf{w} + d\mathbf{w})) = \frac{1}{2} d\mathbf{w}^T \mathbf{F}(\mathbf{w}) d\mathbf{w} + O(\|d\mathbf{w}\|_3)$$
where $\mathbf{F}(\mathbf{w})$ is the **Fisher Information Matrix**:
$$\mathbf{F}(\mathbf{w}) = \mathbb{E}_{\mathbf{x}, \mathbf{y}}\left[ \nabla_{\mathbf{w}} \log p(\mathbf{y} \mid \mathbf{x}; \mathbf{w}) \left( \nabla_{\mathbf{w}} \log p(\mathbf{y} \mid \mathbf{x}; \mathbf{w}) \right)^T \right]$$

### 2. The Natural Gradient Update
The direction of steepest descent under the invariant Riemannian metric is:
$$\tilde{\nabla} F(\mathbf{w}) = \mathbf{F}^{-1}(\mathbf{w}) \nabla F(\mathbf{w})$$
The natural gradient parameter update is:
$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \mathbf{F}^{-1}(\mathbf{w}_t) \nabla F(\mathbf{w}_t)$$

James Martens and Roger Grosse (2015) made natural gradients computationally practical for massive deep neural networks via **K-FAC (Kronecker-Factored Approximate Curvature)**: approximating the layer-wise Fisher matrix as the Kronecker product of two small covariance matrices $\mathbf{F}_l \approx \mathbf{A}_l \otimes \mathbf{S}_l$, inverting each factor independently in milliseconds, and accelerating convergence across ill-conditioned loss surfaces by orders of magnitude.

## 5.8 Escaping Saddle Points in Non-Convex Big Data Optimization

In modern high-dimensional non-convex optimization (such as deep learning and non-negative matrix factorization), the primary computational obstacle is not local minima, but **saddle points**: points where $\nabla F(\mathbf{w}) = \mathbf{0}$, but the Hessian $\nabla^2 F(\mathbf{w})$ possesses both positive and negative eigenvalues.

In high dimensions, the probability that a critical point is a local minimum decays exponentially as $2^{-d}$. A 1,000-dimensional landscape contains thousands of saddle points for every true local minimum.

Chi Jin, Rong Ge, Praneeth Netrapalli, Sham M. Kakade, and Michael I. Jordan (2017) proved that **Perturbed Stochastic Gradient Descent** provably escapes strict saddle points in polynomial time.
By injecting isotropic Gaussian noise $\mathbf{\xi} \sim \mathcal{N}(\mathbf{0}, r^2 \mathbf{I})$ whenever the gradient norm is small ($\|\nabla F(\mathbf{w})\| \le \epsilon$), the perturbation destabilizes the trajectory along negative curvature directions (eigenvectors corresponding to $\lambda_{\min}(\nabla^2 F) < 0$). The trajectory rolls down the escape ravine in $O(\log d)$ iterations, guaranteeing convergence to a second-order local minimum.
"""

# -------------------------------------------------------------
# UNIT 6 DEEP
# -------------------------------------------------------------
u6_deep = r"""
## 6.7 Multidimensional Tensor Decompositions at Scale

In multi-way statistical data analysis—such as longitudinal neuroimaging (voxels $\times$ subjects $\times$ time), e-commerce click logs (users $\times$ products $\times$ contextual queries), and multidimensional sensor grids—data do not reside in a 2D matrix, but in an $N$-way array or **Tensor**:
$$\boldsymbol{\mathcal{X}} \in \mathbb{R}^{I_1 \times I_2 \times \dots \times I_N}$$

When array dimensions scale to $10,000 \times 10,000 \times 10,000$, the tensor contains $10^{12}$ entries (terabytes of memory). Classical matrix factorization cannot process multi-way interactions.

### 1. The CANDECOMP/PARAFAC (CP) Decomposition
F. L. Hitchcock (1927) and J. Douglas Carroll and Jih-Jie Chang (1970) formulated the **CP Decomposition**, expressing an $N$-way tensor as a sum of $R$ rank-1 outer products:
$$\boldsymbol{\mathcal{X}} \approx \sum_{r=1}^R \lambda_r \, \mathbf{a}_r^{(1)} \circ \mathbf{a}_r^{(2)} \circ \dots \circ \mathbf{a}_r^{(N)}$$
where $\circ$ denotes the vector outer product, and $\mathbf{A}^{(n)} = [\mathbf{a}_1^{(n)}, \dots, \mathbf{a}_R^{(n)}] \in \mathbb{R}^{I_n \times R}$ are factor matrices.

The standard solver is **Alternating Least Squares (CP-ALS)**: iteratively fixing $N-1$ factor matrices and solving a linear least squares regression for the remaining matrix:
$$\mathbf{A}^{(n)} \leftarrow \mathbf{X}_{(n)} \left( \bigodot_{k \ne n} \mathbf{A}^{(k)} \right) \left( \Asterisk_{k \ne n} (\mathbf{A}^{(k)T} \mathbf{A}^{(k)}) \right)^\dagger$$
where $\bigodot$ denotes the Khatri-Rao product (column-wise Kronecker product) and $\Asterisk$ denotes the Hadamard product.

### 2. Randomized Tensor Sketching
Tamara G. Kolda (2018) and Rasmus Pagh (2013) introduced randomized sketching to CP-ALS via **TensorSketch**.
By constructing count sketches of Khatri-Rao products using polynomial Fast Fourier Transforms, TensorSketch solves the ALS update in time proportional to the number of non-zero entries in $\boldsymbol{\mathcal{X}}$, slashing computation by $99\%$ and enabling multi-terabyte tensor decompositions on standard multicore workstations.
"""

# -------------------------------------------------------------
# UNIT 7 DEEP
# -------------------------------------------------------------
u7_deep = r"""
## 7.8 Follow-The-Regularized-Leader (FTRL-Proximal) for Online Learning

In industrial online advertising (such as Google and Meta ad auction click-through-rate prediction), models evaluate billions of ad impressions per day. Data streams are non-stationary, and memory constraints require that the parameter vector $\mathbf{w} \in \mathbb{R}^d$ ($d \ge 10^9$) be strictly sparse so that non-predictive weights are zeroed out and omitted from fast memory caches.

Standard online SGD with $L_1$ regularization produces dense weights: stochastic noise prevents coordinates from ever staying exactly at zero.
H. Brendan McMahan et al. (2013) formulated the **FTRL-Proximal** algorithm, which generates exact sparsity in streaming online learning.

### Algorithmic Formulation of FTRL-Proximal
FTRL-Proximal maintains two vectors: the accumulated historical gradient sum $\mathbf{z} \in \mathbb{R}^d$ and the squared gradient sum $\mathbf{n} \in \mathbb{R}^d$.
When a streaming instance $(\mathbf{x}_t, y_t)$ arrives with loss gradient $\mathbf{g}_t = \nabla \ell(\mathbf{w}_t; \mathbf{x}_t, y_t)$:
1. For each active coordinate $i$:
$$n_i \leftarrow n_i + g_{t, i}^2$$
$$\sigma_i = \frac{\sqrt{n_i} - \sqrt{n_i - g_{t, i}^2}}{\alpha}$$
$$z_i \leftarrow z_i + g_{t, i} - \sigma_i w_{t, i}$$
2. The coordinate update is computed in closed form:
$$w_{t+1, i} = \begin{cases} 0, & \text{if } |z_i| \le \lambda_1 \\ -\left( \frac{\beta + \sqrt{n_i}}{\alpha} + \lambda_2 \right)^{-1} \left( z_i - \mathrm{sign}(z_i) \lambda_1 \right), & \text{if } |z_i| > \lambda_1 \end{cases}$$
where $\alpha, \beta$ govern per-coordinate adaptive learning rates, $\lambda_1$ is the $L_1$ sparsity penalty, and $\lambda_2$ is the $L_2$ shrinkage weight.

FTRL-Proximal achieves optimal logarithmic regret $O(\sqrt{T})$ under online convex optimization, while forcing over $90\%$ of streaming weights to be exactly zero, enabling multi-billion parameter online predictive models to serve live ad queries in under 5 milliseconds.

## 7.9 Adaptive Windowing (ADWIN) for Concept Drift Detection

In real-world data streams, the underlying data-generating distribution changes over time due to seasonal shifts, macroeconomic fluctuations, or consumer behavior shifts—a phenomenon known as **Concept Drift**:
$$P_t(\mathbf{x}, y) \ne P_{t + \Delta}(\mathbf{x}, y)$$

Albert Bifet and Ricard Gavaldà (2007) introduced **ADWIN (Adaptive Windowing)**, an online algorithm that automatically adapts the size of a sliding historical window without requiring user-defined window length tuning.

### The ADWIN Splitting Criterion
ADWIN maintains a sliding window $W$ of recent stream items. Whenever a new item arrives, ADWIN checks whether there exists any partition of $W$ into two sub-windows $W_0$ and $W_1$ ($W = W_0 \cdot W_1$) whose sample means $\hat{\mu}_0$ and $\hat{\mu}_1$ exhibit a statistically significant difference:

$$|\hat{\mu}_0 - \hat{\mu}_1| \ge \epsilon_{\text{cut}} = \sqrt{\frac{1}{2m} \ln\left( \frac{4 |W|}{\delta} \right)}$$
where $m = \frac{1}{1/|W_0| + 1/|W_1|}$ is the harmonic mean of the sub-window lengths, and $\delta$ is the user-specified false alarm probability.

By the Hoeffding bound, if $|\hat{\mu}_0 - \hat{\mu}_1| \ge \epsilon_{\text{cut}}$, the hypothesis of stationary identical distributions is rejected with confidence $1 - \delta$. ADWIN immediately drops the older sub-window $W_0$, shrinking the window to include only recent post-drift data. When the stream is stationary, the window expands automatically, maximizing statistical power.
"""

# -------------------------------------------------------------
# UNIT 8 DEEP
# -------------------------------------------------------------
u8_deep = r"""
## 8.7 Post-Selection Inference and the Polyhedral Lemma

In high-dimensional scientific research, analysts frequently perform **Data Dredging** or "p-hacking": they run the Lasso on thousands of variables, identify the 5 variables with non-zero coefficients $\hat{S} = \{j : \hat{\beta}_j \ne 0\}$, and then fit an unpenalized OLS model on those 5 selected variables, reporting standard Student's $t$-test $p$-values.

Richard Berk et al. (2013), followed by Jonathan Taylor and Robert Tibshirani (2015), proved that **naive post-selection $p$-values are catastrophically invalid**: because the variables were selected specifically because they had the largest empirical correlations with $\mathbf{y}$, standard $p$-values are biased downward by orders of magnitude, generating massive rates of false scientific publication.

### The Polyhedral Lemma
Taylor, Tibshirani, and collaborators developed **Exact Selective Inference**, conditioning hypothesis tests on the mathematical event that the specific model was selected:
$$P(\text{Test Statistic} \ge t \mid \hat{S} = S, \hat{\mathbf{s}} = \mathbf{s})$$

*The Polyhedral Lemma*: For the Lasso (and many forward-stepwise selection algorithms), the selection event $\{\hat{S} = S, \mathrm{sign}(\hat{\boldsymbol{\beta}}_S) = \mathbf{s}\}$ can be expressed as a set of linear inequality constraints on the response vector $\mathbf{y}$:
$$\mathbf{A} \mathbf{y} \le \mathbf{b}$$
where the matrix $\mathbf{A}$ and vector $\mathbf{b}$ depend on the design matrix $\mathbf{X}$ and active signs $\mathbf{s}$.

Conditioning a multivariate Gaussian observation $\mathbf{y} \sim \mathcal{N}(\boldsymbol{\mu}, \sigma^2 \mathbf{I})$ on lying inside a polyhedron $\{\mathbf{A} \mathbf{y} \le \mathbf{b}\}$ restricts the projected test statistic to a **Truncated Gaussian Distribution**:
$$T = \frac{\boldsymbol{\eta}^T \mathbf{y}}{\sigma \|\boldsymbol{\eta}\|_2} \sim \mathcal{TN}(\mu_0, 1, \mathcal{V}^-, \mathcal{V}^+)$$
where $\mathcal{V}^-$ and $\mathcal{V}^+$ are computable coordinate truncation limits.
Evaluating tail probabilities under this truncated Gaussian distribution produces **exact, uniformly distributed post-selection $p$-values**, restoring rigorous statistical integrity to exploratory model search.

## 8.8 Surrogate Variable Analysis (SVA) and Latent Confounder Adjustment

In large-scale biological and epidemiological testing (e.g., DNA methylation arrays, transcriptomics), test statistics are severely contaminated by unmeasured technical noise and latent confounding factors (e.g., batch effects, laboratory temperature, sample collection time, cell type heterogeneity). If ignored, these latent factors induce widespread spurious correlations across thousands of genes.

Jeffrey T. Leek and John D. Storey (2007) introduced **Surrogate Variable Analysis (SVA)** to estimate and remove latent confounders directly from high-dimensional testing matrices without requiring explicit metadata.

### The SVA Decomposition
Let $\mathbf{Y} \in \mathbb{R}^{m \times n}$ be the gene expression matrix ($m$ genes, $n$ samples), modeled as:
$$Y_{ij} = \mathbf{x}_i^T \boldsymbol{\beta}_j + \mathbf{z}_i^T \boldsymbol{\gamma}_j + \epsilon_{ij}$$
where $\mathbf{x}_i$ are the observed primary clinical variables, and $\mathbf{z}_i \in \mathbb{R}^K$ are unobserved latent surrogate variables with coefficient loadings $\boldsymbol{\gamma}_j$.

1. Fit the primary model $\mathbf{Y} = \mathbf{X} \mathbf{B} + \mathbf{R}$ and compute the residual matrix:
$$\mathbf{R} = \mathbf{Y} (\mathbf{I} - \mathbf{X} (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T)$$
2. Compute the SVD of the residual matrix: $\mathbf{R} = \mathbf{U} \mathbf{D} \mathbf{V}^T$.
3. Identify the number of statistically significant surrogate factors $K$ using permutation tests or the Marchenko-Pastur spectral cutoff.
4. Construct the surrogate variables $\hat{\mathbf{z}}_k$ from the right singular vectors of $\mathbf{R}$.
5. Re-run multiple hypothesis testing including the estimated surrogate variables as nuisance covariates:
$$Y_{ij} = \mathbf{x}_i^T \boldsymbol{\beta}_j + \sum_{k=1}^K \hat{z}_{ik} \gamma_{jk} + \epsilon_{ij}$$

SVA purges unmeasured technical variation and batch effects, eliminating thousands of false positive correlations and rescuing reproducibility in high-dimensional science.
"""

def main():
    append_to_unit(5, u5_deep)
    append_to_unit(6, u6_deep)
    append_to_unit(7, u7_deep)
    append_to_unit(8, u8_deep)
    print("Units 5-8 deep pass 2 applied.")

if __name__ == "__main__":
    main()
