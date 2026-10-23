#!/usr/bin/env python3
"""
Deep Expansion Pass 3 for Big Data Methods for Statistics (Book 16) - Units 1 to 4.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")
    print(f"Unit {unit_num} deep pass 3 applied.")

# -------------------------------------------------------------
# UNIT 1
# -------------------------------------------------------------
u1_deep3 = r"""
## 1.12 The Subspace Hypothesis and Intrinsic Dimensionality

While high-dimensional data mathematically reside in an ambient Euclidean coordinate space $\mathbb{R}^p$ where $p \ge 10^5$, empirical big data—such as natural photographic images, human speech spectrograms, single-cell RNA profiles, and financial transaction matrices—do not uniformly populate the entire space.

The **Subspace Hypothesis** (or Manifold Hypothesis) posits that high-dimensional real-world data concentrate with high probability on or near a collection of low-dimensional smooth submanifolds $\mathcal{M} \subset \mathbb{R}^p$ of intrinsic dimension $d \ll p$.

### 1. Estimating Intrinsic Dimension: The Levina-Bickel Maximum Likelihood Estimator
Elizaveta Levina and Peter J. Bickel (2004) developed a celebrated maximum likelihood estimator of intrinsic dimension based on continuous Poisson process models of nearest neighbor distances.

Let $\mathbf{x}$ be a reference point, and let $T_k(\mathbf{x})$ denote the Euclidean distance from $\mathbf{x}$ to its $k$-th nearest neighbor. Modeling the local point arrivals as a homogeneous Poisson process on a $d$-dimensional tangent plane, the local maximum likelihood estimator of dimension $d$ at point $\mathbf{x}$ is:

$$\hat{d}_k(\mathbf{x}) = \left[ \frac{1}{k - 2} \sum_{j=1}^{k-1} \ln\left( \frac{T_k(\mathbf{x})}{T_j(\mathbf{x})} \right) \right]^{-1}$$

Averaging $\hat{d}_k(\mathbf{x}_i)$ across all sample observations produces a global estimate of intrinsic dimensionality. In handwritten digit recognition (MNIST, ambient dimension $p = 784$), the Levina-Bickel estimator reveals that the intrinsic manifold dimension is only $d \approx 10$ to $12$. In modern deep representation learning, this low intrinsic dimension explains why massive neural networks avoid the worst penalties of the curse of dimensionality.

## 1.13 High-Dimensional Covariance Regularization: Thresholding and Banding

In Section 1.9, we proved that the raw empirical covariance matrix $\mathbf{S} = \frac{1}{n} \mathbf{X}^T \mathbf{X}$ is inconsistent when $p > n$. To obtain consistent covariance estimators in high dimensions, Peter Bickel and Elizaveta Levina (2008) introduced regularized non-parametric estimators.

### 1. Universal Hard and Soft Thresholding
When the true population covariance matrix $\mathbf{\Sigma}$ is sparse (meaning most pairs of variables have zero or negligible correlation):
- **Hard Thresholding**: Set entries below a data-driven threshold to zero:
$$T_\lambda(\mathbf{S})_{ij} = S_{ij} \cdot \mathbb{I}(|S_{ij}| \ge \lambda), \quad \forall i \ne j$$
- **Soft Thresholding**: Shrink off-diagonal entries continuously:
$$S_\lambda(\mathbf{S})_{ij} = \mathrm{sign}(S_{ij}) \max(0, |S_{ij}| - \lambda), \quad \forall i \ne j$$
Bickel and Levina proved that with threshold $\lambda \propto \sqrt{\frac{\ln p}{n}}$, the thresholded covariance estimator satisfies:
$$\|T_\lambda(\mathbf{S}) - \mathbf{\Sigma}\|_{\text{op}} = O_p\left( s_0(p) \sqrt{\frac{\ln p}{n}} \right)$$
where $s_0(p) = \max_i \sum_j \mathbb{I}(\Sigma_{ij} \ne 0)$ is the maximum sparsity degree per row.

### 2. Banding and Tapering for Ordered Data
In time series, longitudinal studies, and spatial geostatistics, variables possess a natural temporal or spatial ordering where correlations decay with distance $|i - j|$.
- **Banding**: Retains only the $k$ sub-diagonals and zeroes out the rest:
$$B_k(\mathbf{S})_{ij} = S_{ij} \cdot \mathbb{I}(|i - j| \le k)$$
- **Tapering**: Applies a smooth Schur (element-wise) product with a decaying positive-definite correlation kernel:
$$\mathbf{S}_{\text{taper}} = \mathbf{K} \circ \mathbf{S}, \quad K_{ij} = \kappa\left( \frac{|i - j|}{k} \right)$$
Banding and tapering guarantee that the resulting regularized covariance matrix is strictly positive definite and converges in operator norm at optimal polynomial minimax rates.
"""

# -------------------------------------------------------------
# UNIT 2
# -------------------------------------------------------------
u2_deep3 = r"""
## 2.11 Robust Principal Component Analysis (RPCA) and Principal Component Pursuit

Classical PCA is notoriously fragile to gross outliers and data corruptions: because least squares optimization minimizes squared deviations $\sum \|\mathbf{x}_i - \hat{\mathbf{x}}_i\|_2^2$, even a single corrupted sensor reading or malicious adversarial injection can alter the orientation of the principal component axes by $90^\circ$.

Emmanuel Candès, Xiaodong Li, Yi Ma, and John Wright (2011) introduced **Robust PCA (RPCA)** via **Principal Component Pursuit (PCP)**, decomposing an observed corrupted data matrix $\mathbf{X} \in \mathbb{R}^{n \times p}$ into two separate matrices:
$$\mathbf{X} = \mathbf{L}_0 + \mathbf{S}_0$$
where:
1. $\mathbf{L}_0$ is a low-rank matrix representing the true low-dimensional statistical factor structure.
2. $\mathbf{S}_0$ is a sparse matrix whose non-zero entries represent arbitrary, unbounded corruptions, missing entries, or anomalies.

### 1. Convex Relaxation via Nuclear Norm and $L_1$ Norm
Direct minimization of $\mathrm{rank}(\mathbf{L}) + \lambda \|\mathbf{S}\|_0$ is an NP-hard combinatorial problem. Candès et al. proved that PCP solves this problem via its tightest convex surrogate:

$$\min_{\mathbf{L}, \mathbf{S}} \left\{ \|\mathbf{L}\|_* + \lambda \|\mathbf{S}\|_1 \right\} \quad \text{subject to} \quad \mathbf{L} + \mathbf{S} = \mathbf{X}$$
where:
- $\|\mathbf{L}\|_* = \sum_{j=1}^{\min(n, p)} \sigma_j(\mathbf{L})$ is the **Nuclear Norm** (the sum of singular values), which is the convex envelope of the matrix rank.
- $\|\mathbf{S}\|_1 = \sum_{ij} |S_{ij}|$ is the element-wise $L_1$ norm.
- $\lambda = \frac{1}{\sqrt{\max(n, p)}}$ is a universal tuning parameter.

*Theorem (Exact Matrix Separation)*: Under mild incoherence conditions (ensuring the low-rank singular vectors are not spiky), PCP recovers the exact low-rank matrix $\mathbf{L}_0$ and sparse corruption matrix $\mathbf{S}_0$ with probability $1.0$.

In video surveillance analytics, $\mathbf{L}$ extracts the stationary background scene while $\mathbf{S}$ isolates moving pedestrians. In financial anomaly detection, $\mathbf{L}$ captures macro market factors while $\mathbf{S}$ isolates fraudulent transaction spikes.

## 2.12 Independent Component Analysis (ICA) and Non-Gaussianity

While PCA identifies uncorrelated orthogonal directions that maximize variance (second-order moments), uncorrelatedness implies statistical independence if and only if the underlying data are multivariate Gaussian. In many big data settings—such as electroencephalography (EEG) brain wave recordings, financial market volatility regimes, and audio blind source separation—the observed signals are non-Gaussian mixtures of independent source signals.

Aapo Hyvärinen and Erkki Oja (1997, 2000) formulated **Independent Component Analysis (ICA)**:
$$\mathbf{x} = \mathbf{A} \mathbf{s}$$
where $\mathbf{s} \in \mathbb{R}^d$ are statistically independent, non-Gaussian source components, and $\mathbf{A} \in \mathbb{R}^{p \times d}$ is an unknown mixing matrix.

### 1. The Central Limit Theorem Principle
By the Central Limit Theorem, the sum of independent random variables is always **more Gaussian** than any of the individual components.
Therefore, finding the unmixed independent sources is mathematically equivalent to finding linear combinations $\mathbf{w}^T \mathbf{x}$ that **maximize non-Gaussianity**.

### 2. FastICA and Negentropy Maximization
Non-Gaussianity is quantified via **Negentropy**:
$$J(y) = H(y_{\text{Gauss}}) - H(y)$$
where $H(y) = -\int f(y) \ln f(y)\,dy$ is differential entropy. A Gaussian variable maximizes entropy, so $J(y) \ge 0$, with equality if and only if $y$ is Gaussian.

The **FastICA** fixed-point algorithm updates the unmixing vector $\mathbf{w}$ using non-linear contrast functions $G(u)$ (such as $G(u) = \frac{1}{a} \ln \cosh(a u)$):
$$\mathbf{w}_{k+1} = \mathbb{E}\left[ \mathbf{x} g(\mathbf{w}_k^T \mathbf{x}) \right] - \mathbb{E}\left[ g'(\mathbf{w}_k^T \mathbf{x}) \right] \mathbf{w}_k$$
$$\mathbf{w}_{k+1} \leftarrow \frac{\mathbf{w}_{k+1}}{\|\mathbf{w}_{k+1}\|_2}$$
FastICA converges cubically, separating independent biological and economic signals in seconds.
"""

# -------------------------------------------------------------
# UNIT 3
# -------------------------------------------------------------
u3_deep3 = r"""
## 3.11 The Fused Lasso and Total Variation Denoising

In genomic array comparative genomic hybridization (aCGH), time series segmentation, and image processing, predictor variables or signal coordinates possess an inherent ordering. A standard Lasso regression treats feature indices as an unstructured set, ignoring spatial or temporal adjacency.

Robert Tibshirani et al. (2005) introduced the **Fused Lasso**, penalizing both the magnitude of individual coefficients and the differences between successive coordinates:

$$\min_{\boldsymbol{\beta}} \left\{ \frac{1}{2} \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2 + \lambda_1 \sum_{j=1}^p |\beta_j| + \lambda_2 \sum_{j=2}^p |\beta_j - \beta_{j-1}| \right\}$$

- The first penalty $\lambda_1 \|\boldsymbol{\beta}\|_1$ encourages overall sparsity (setting non-essential coefficients to zero).
- The second penalty $\lambda_2 \sum |\beta_j - \beta_{j-1}|$ is the **Total Variation (TV)** penalty, which encourages adjacent coefficients to take identical values ($\beta_j = \beta_{j-1}$).

In signal processing where $\mathbf{X} = \mathbf{I}_n$, the problem reduces to **1D Total Variation Denoising** (Rudin, Osher, Fatemi 1992):
$$\min_{\boldsymbol{\beta}} \frac{1}{2} \|\mathbf{y} - \boldsymbol{\beta}\|_2^2 + \lambda \sum_{j=2}^n |\beta_j - \beta_{j-1}|$$
Nick Johnson (2013) proved that 1D TV denoising can be solved in exact $O(n)$ time using a taut-string dynamic programming algorithm. The resulting signal estimate is a sparse, piecewise constant step function that preserves sharp jump boundaries (e.g., DNA copy number variations, economic regime shifts) without blurring edges.

## 3.12 The SLOPE Estimator: Sorted $L_1$ Penalization for FDR Control

While the Lasso controls prediction error, selecting an optimal tuning parameter $\lambda$ that simultaneously prevents false discoveries is difficult: tuning $\lambda$ to minimize cross-validation error typically includes dozens of noise variables, while tuning $\lambda$ large enough to eliminate all false positives causes severe attenuation of true signals.

Małgorzata Bogdan et al. (2015) introduced **SLOPE (Sorted L-One Penalized Estimation)**, replacing the constant penalty $\lambda$ with a sorted, rank-dependent sequence of penalties:

$$\min_{\boldsymbol{\beta}} \left\{ \frac{1}{2} \|\mathbf{y} - \mathbf{X} \boldsymbol{\beta}\|_2^2 + \sum_{j=1}^p \lambda_j |\beta|_{(j)} \right\}$$
where $|\beta|_{(1)} \ge |\beta|_{(2)} \ge \dots \ge |\beta|_{(p)}$ are the sorted absolute values of the coefficients, and $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_p > 0$ is a non-increasing sequence of regularization weights.

Bogdan et al. designed the sequence $\lambda_j$ using the quantiles of the standard normal distribution:
$$\lambda_j = \sigma \Phi^{-1}\left( 1 - \frac{j \cdot q^*}{2p} \right)$$
which mirrors the Benjamini-Hochberg critical thresholds in multiple testing!

*Theorem (SLOPE FDR Control)*: In an orthogonal design matrix, the SLOPE estimator guarantees that the **False Discovery Rate of selected variables is strictly bounded by $q^*$**:
$$\mathrm{FDR} = \mathbb{E}\left[ \frac{\#\{ j : \hat{\beta}_j \ne 0 \text{ and } \beta_j^* = 0 \}}{\max(1, \#\{ j : \hat{\beta}_j \ne 0 \})} \right] \le q^*$$
SLOPE provides a seamless bridge between sparse penalization and multiple testing theory, delivering exact variable-selection false discovery rate control in high dimensions.
"""

# -------------------------------------------------------------
# UNIT 4
# -------------------------------------------------------------
u4_deep3 = r"""
## 4.10 Local Differential Privacy (LDP) in Distributed Statistics

When training statistical machine learning models across distributed consumer devices (such as smart phones or hospital patient registries in Federated Learning), transmitting raw individual data or exact gradients exposes sensitive private information: an adversarial observer intercepting gradient transmissions can reconstruct original text messages or patient health records using gradient inversion attacks.

Cynthia Dwork (2006) formulated **Differential Privacy**, adapted into **Local Differential Privacy (LDP)** by John Duchi, Michael I. Jordan, and Martin J. Wainwright (2013).

### 1. Mathematical Definition of Local Differential Privacy
A randomized mechanism $\mathcal{M}: \mathcal{X} \to \mathcal{Z}$ satisfies **$\epsilon$-Local Differential Privacy** if for any two input values $x, x' \in \mathcal{X}$ and any measurable subset of outputs $S \subseteq \mathcal{Z}$:

$$P(\mathcal{M}(x) \in S) \le e^\epsilon P(\mathcal{M}(x') \in S)$$
where $\epsilon > 0$ is the **privacy budget**. A smaller $\epsilon$ guarantees stronger privacy protection, ensuring that an attacker observing output $\mathcal{M}(x)$ cannot distinguish whether the input was $x$ or $x'$.

### 2. The Laplace and Gaussian Perturbation Mechanisms
In distributed statistical estimation of a vector-valued statistic $\boldsymbol{\theta}(\mathbf{X}) \in \mathbb{R}^d$, workers inject calibrated random noise before transmitting updates:
1. **The Laplace Mechanism**:
$$\mathcal{M}(\boldsymbol{\theta}) = \boldsymbol{\theta} + \mathbf{w}, \quad w_j \sim \text{Laplace}\left( 0, \frac{\Delta_1}{\epsilon} \right)$$
where $\Delta_1 = \max_{\mathbf{x}, \mathbf{x}'} \|\boldsymbol{\theta}(\mathbf{x}) - \boldsymbol{\theta}(\mathbf{x}')\|_1$ is the $L_1$ global sensitivity.
2. **The Gaussian Mechanism**:
$$\mathcal{M}(\boldsymbol{\theta}) = \boldsymbol{\theta} + \mathcal{N}\left( \mathbf{0}, \sigma^2 \mathbf{I}_d \right), \quad \sigma = \frac{\Delta_2 \sqrt{2 \ln(1.25/\delta)}}{\epsilon}$$
satisfying $(\epsilon, \delta)$-differential privacy, where $\Delta_2$ is the $L_2$ global sensitivity.

*Statistical Minimax Privacy Trade-Off*: Duchi, Jordan, and Wainwright proved that under $\epsilon$-LDP, the minimax estimation rate for estimating a $d$-dimensional mean vector drops from the classical rate $O(d/n)$ to:
$$\mathbb{E}[\|\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}^*\|_2^2] = \Theta\left( \frac{d}{n \epsilon^2} \right)$$
Privacy imposes an unavoidable statistical cost: achieving high privacy ($\epsilon \ll 1$) requires scaling sample size $n$ by $1/\epsilon^2$.

## 4.11 Query Optimization in Big Data Engines: Broadcast vs. Shuffle Joins

In distributed SQL and DataFrame engines (such as Spark SQL, Trino, and Google BigQuery), computing a database join between two distributed tables $\mathbf{A} \bowtie \mathbf{B}$ on a common key is the most communication-intensive operation in big data systems.

Engines deploy two fundamentally distinct join strategies:
1. **Shuffle Hash Join**: Both tables $\mathbf{A}$ and $\mathbf{B}$ are repartitioned across all $P$ cluster nodes by computing a hash of the join key $h(\text{key}) \pmod P$. Records with identical keys are transmitted over the physical cluster network to the same destination node, which performs a local hash join.
*Network Cost*: $O(|\mathbf{A}| + |\mathbf{B}|)$ full network transmission volume. If both tables contain terabytes of data, shuffling saturates the network switches.
2. **Broadcast Hash Join (Map-Side Join)**: When one table is small (e.g., table $\mathbf{B}$ is a dimension table of 50 MB, while table $\mathbf{A}$ is a fact table of 2 TB), the engine avoids shuffling table $\mathbf{A}$ entirely. The master node **broadcasts** a complete copy of table $\mathbf{B}$ to the local RAM of every worker node. Each worker performs the join locally against its existing partition of table $\mathbf{A}$.
*Network Cost*: $O(P \cdot |\mathbf{B}|)$ network transmission. Zero shuffle traffic for table $\mathbf{A}$.

Catalyst query optimizers inspect table statistics automatically: if a table size falls below `spark.sql.autoBroadcastJoinThreshold` (default 10 MB), it automatically promotes the query to a Broadcast Hash Join, accelerating distributed queries by factors of 10 to 100.
"""

def main():
    append_to_unit(1, u1_deep3)
    append_to_unit(2, u2_deep3)
    append_to_unit(3, u3_deep3)
    append_to_unit(4, u4_deep3)
    print("Units 1-4 deep pass 3 applied.")

if __name__ == "__main__":
    main()
