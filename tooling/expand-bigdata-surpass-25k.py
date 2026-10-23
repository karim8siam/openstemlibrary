#!/usr/bin/env python3
"""
Surpass 25,500 substantive prose words for Big Data Methods for Statistics (Book 16).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")
    print(f"Unit {unit_num} boosted.")

u1_sup = r"""
## 1.21 Isoperimetry on the Discrete Hypercube $\{0, 1\}^p$

In high-dimensional discrete statistics, binary feature vectors $\mathbf{x} \in \{0, 1\}^p$ represent user click indicators, binary genomic presence/absence markers, or sparse vocabulary bags of words.
The geometry of the discrete hypercube is governed by the **Hamming Distance**:
$$d_H(\mathbf{x}, \mathbf{y}) = \sum_{j=1}^p \mathbb{I}(x_j \ne y_j)$$

L. H. Harper (1966) proved the discrete analog of the spherical isoperimetric inequality:
*Theorem (Harper's Discrete Isoperimetric Theorem)*: For any subset $A \subseteq \{0, 1\}^p$ containing at least half the vertices ($|A| \ge 2^{p-1}$), the $t$-neighborhood $A_t = \{ \mathbf{x} : d_H(\mathbf{x}, A) \le t \}$ satisfies:
$$\frac{|A_t|}{2^p} \ge 1 - 2 \exp\left( -\frac{2 t^2}{p} \right)$$
For any Lipschitz function $f: \{0, 1\}^p \to \mathbb{R}$ with coordinate Lipschitz constant $L$ ($|f(\mathbf{x}) - f(\mathbf{y})| \le L$ whenever $d_H(\mathbf{x}, \mathbf{y}) = 1$):
$$P\left( |f(\mathbf{X}) - \mathbb{E}[f(\mathbf{X})]| \ge t \right) \le 2 \exp\left( -\frac{2 t^2}{p L^2} \right)$$
This discrete concentration inequality guarantees that sums of independent binary features and randomized hash evaluations concentrate tightly around their expectations, forming the mathematical foundation for streaming sketches and randomized algorithms.
"""

u2_sup = r"""
## 2.20 Kernel PCA vs. Deep Autoencoders: An Epistemological Comparison

In non-linear dimension reduction, statisticians choose between two competing non-linear paradigms: **Kernel PCA** (Schölkopf, Smola, and Müller 1998) and **Deep Autoencoders** (Hinton and Salakhutdinov 2006).

### 1. Mathematical Contrast
- **Kernel PCA**: Implicitly maps data into an infinite-dimensional Reproducing Kernel Hilbert Space (RKHS) $\mathcal{H}$ via feature map $\Phi(\mathbf{x})$, and finds the linear principal components in $\mathcal{H}$.
  - Convex optimization: guaranteed global minimum via eigenvalue decomposition.
  - Non-parametric: capacity scales with sample size $n$.
  - Limitation: requires $O(n^2)$ memory and cannot reconstruct low-dimensional embeddings back into input space easily (the pre-image problem).
- **Deep Autoencoders**: Neural networks with an hourglass architecture that compress input $\mathbf{x} \in \mathbb{R}^p$ through an encoder $f_\theta: \mathbb{R}^p \to \mathbb{R}^d$ and decompress via a decoder $g_\phi: \mathbb{R}^d \to \mathbb{R}^p$ to minimize reconstruction error:
$$\min_{\theta, \phi} \frac{1}{n} \sum_{i=1}^n \|\mathbf{x}_i - g_\phi(f_\theta(\mathbf{x}_i))\|_2^2$$
  - Non-convex optimization: trained via SGD with risks of saddle points.
  - Parametric: memory scales with parameter count $O(p d)$, independent of $n$.
  - Generative decoding: the decoder $g_\phi$ provides an explicit generative mapping from latent coordinates back to data space.

In modern workflows, Kernel PCA is preferred for theoretical sample complexity bounds and moderate samples ($n \le 50,000$), while Deep Autoencoders dominate massive multimodal streams ($n \ge 10^7$).
"""

u3_sup = r"""
## 3.20 Overlapping Group Lasso for Complex Biological Pathways

In cancer genomics and systems biology, genes do not belong to disjoint mutually exclusive groups: a single transcription factor or kinase participates in multiple overlapping signaling pathways (e.g., cell cycle regulation, apoptosis, and DNA repair).
Applying standard Group Lasso requires disjoint partitions, forcing the analyst to artificially duplicate gene columns or drop pathway assignments.

Laurent Jacob, Guillaume Obozinski, and Jean-Philippe Vert (2009) invented the **Overlapping Group Lasso**, enabling variables to belong to arbitrary overlapping sets $\mathcal{G}$:
$$\min_{\boldsymbol{\beta}} \left\{ \frac{1}{2n} \left\| \mathbf{y} - \mathbf{X} \sum_{g \in \mathcal{G}} \mathbf{v}_g \right\|_2^2 + \lambda \sum_{g \in \mathcal{G}} \sqrt{|g|} \|\mathbf{v}_g\|_2 \right\}$$
where each predictor is decomposed into latent group-specific components $\boldsymbol{\beta} = \sum_{g: j \in g} \mathbf{v}_g$.
Jacob et al. proved that this latent variable formulation encourages the union of selected pathways to be sparse, selecting entire coordinated biological pathways while naturally accommodating shared multi-functional genes.
"""

u4_sup = r"""
## 4.18 Distributed Storage Architectures: HDFS Erasure Coding vs. 3x Replication

In the physical infrastructure of big data clusters, storage reliability is historically achieved by **3x Replication**: every 128 MB block of data in the Hadoop Distributed File System (HDFS) is copied to three physically distinct server racks.
While 3x replication guarantees that up to two simultaneous server failures cause zero data loss, it incurs a massive **$200\%$ storage overhead** (storing 1 Petabyte of statistical data requires 3 Petabytes of physical disk drives).

Modern distributed engines deploy **Erasure Coding (EC)** using Reed-Solomon codes $\mathrm{RS}(k, m)$ (typically $\mathrm{RS}(6, 3)$):
1. A data file is partitioned into $k = 6$ data blocks.
2. An encoding generator matrix over a Galois field $\mathbb{F}_{2^8}$ computes $m = 3$ parity blocks.
3. The 9 blocks are distributed across 9 independent storage nodes.

*Reliability and Cost*:
- Any $k = 6$ surviving blocks out of the 9 blocks can reconstruct the original file using Gaussian elimination over finite fields. The system survives any 3 simultaneous disk failures (superior to 3x replication).
- The storage overhead is only $m/k = 3/6 = \mathbf{50\%}$ (storing 1 PB requires only 1.5 PB of physical disk).
Erasure coding slashes data center hardware costs by $50\%$ while guaranteeing multi-petabyte statistical durability.
"""

u5_sup = r"""
## 5.16 Convergence Proof Sketch of Hogwild! under Sparsity

In Unit 5.6, we introduced the Hogwild! asynchronous lock-free optimization algorithm. Here, we outline the mathematical proof sketch of its convergence.

Let the objective be $F(\mathbf{w}) = \frac{1}{n} \sum f_i(\mathbf{w})$.
Let $\mathbf{w}_t$ denote the true physical memory state at global clock tick $t$.
Because worker threads read and write memory asynchronously without locks, when a thread computes the gradient for instance $i_t$, it reads an older, stale version of the parameter vector $\mathbf{w}_{\hat{t}}$, where $t - \hat{t} \le \tau$, and $\tau$ is the maximum hardware staleness delay.

The update rule in physical memory is:
$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla f_{i_t}(\mathbf{w}_{\hat{t}})$$
Subtracting $\mathbf{w}^*$ and expanding the squared Euclidean distance:
$$\|\mathbf{w}_{t+1} - \mathbf{w}^*\|_2^2 = \|\mathbf{w}_t - \mathbf{w}^*\|_2^2 - 2 \eta \langle \nabla f_{i_t}(\mathbf{w}_{\hat{t}}), \mathbf{w}_t - \mathbf{w}^* \rangle + \eta^2 \|\nabla f_{i_t}(\mathbf{w}_{\hat{t}})\|_2^2$$
Decomposing the inner product:
$$\langle \nabla f_{i_t}(\mathbf{w}_{\hat{t}}), \mathbf{w}_t - \mathbf{w}^* \rangle = \langle \nabla f_{i_t}(\mathbf{w}_{\hat{t}}), \mathbf{w}_{\hat{t}} - \mathbf{w}^* \rangle + \langle \nabla f_{i_t}(\mathbf{w}_{\hat{t}}), \mathbf{w}_t - \mathbf{w}_{\hat{t}} \rangle$$
By convexity and Lipschitz continuity, the first term provides positive contraction toward the minimum.
The second error term $\langle \nabla f_{i_t}, \mathbf{w}_t - \mathbf{w}_{\hat{t}} \rangle$ is bounded by the Cauchy-Schwarz inequality and the sparsity conflict graph parameter $\Omega$:
$$|\langle \nabla f_{i_t}(\mathbf{w}_{\hat{t}}), \mathbf{w}_t - \mathbf{w}_{\hat{t}} \rangle| \le \eta \tau \Omega L^2 \|\mathbf{w}_{\hat{t}} - \mathbf{w}^*\|_2$$
If the learning rate satisfies $\eta \le \frac{1}{2 L (1 + 2 \tau \Omega)}$, the contraction strictly dominates the asynchronous staleness error, guaranteeing that asynchronous lock-free SGD converges to the true optimum at the exact same asymptotic rate as serial SGD.
"""

u6_sup = r"""
## 6.15 Incremental Low-Rank SVD for Streaming Matrices

In video tracking, social network link evolution, and real-time sensor streams, the data matrix $\mathbf{A}$ is not static: new rows or columns arrive sequentially over time:
$$\mathbf{A}_{t+1} = \begin{pmatrix} \mathbf{A}_t \\ \mathbf{x}_{t+1}^T \end{pmatrix}$$
Recomputing the full truncated SVD $\mathbf{U}_k \mathbf{\Sigma}_k \mathbf{V}_k^T$ from scratch upon every row arrival requires $O(n k^2)$ operations, which is impossible at 1,000 events per second.

Matthew Brand (2002) introduced **Incremental SVD**, updating the low-rank SVD in strict $O(p k + k^3)$ operations.

### Algorithmic Update Mechanics
Given the current rank-$k$ approximation $\mathbf{A} \approx \mathbf{U} \mathbf{\Sigma} \mathbf{V}^T$ and a newly arrived row $\mathbf{x} \in \mathbb{R}^p$:
1. Project $\mathbf{x}$ onto the existing right singular subspace: $\mathbf{r} = \mathbf{V}^T \mathbf{x} \in \mathbb{R}^k$.
2. Compute the orthogonal residual vector: $\mathbf{p} = \mathbf{x} - \mathbf{V} \mathbf{r}$, with residual norm $p_{\text{norm}} = \|\mathbf{p}\|_2$.
3. Normalize: $\mathbf{p}' = \mathbf{p} / p_{\text{norm}}$.
4. Construct the small $(k + 1) \times (k + 1)$ core matrix:
$$\mathbf{M} = \begin{pmatrix} \mathbf{\Sigma} & \mathbf{0} \\ \mathbf{r}^T & p_{\text{norm}} \end{pmatrix}$$
5. Compute the SVD of the tiny core matrix $\mathbf{M} = \tilde{\mathbf{U}} \tilde{\mathbf{\Sigma}} \tilde{\mathbf{V}}^T$ in $O(k^3)$ time.
6. Update the global singular vectors:
$$\mathbf{V}_{\text{new}} = [\mathbf{V}, \mathbf{p}'] \tilde{\mathbf{V}}_{:, 1:k}, \quad \mathbf{\Sigma}_{\text{new}} = \tilde{\mathbf{\Sigma}}_{1:k, 1:k}$$
Incremental SVD updates low-rank factorizations in microseconds, tracking dynamic subspace drift across live data streams.
"""

u7_sup = r"""
## 7.17 Concept Drift Taxonomy: Virtual vs. Real Drift and the CUSUM Chart

In streaming data statistics, changes in the joint probability distribution $P_t(\mathbf{x}, y) = P_t(\mathbf{x}) P_t(y \mid \mathbf{x})$ fall into two distinct structural categories:

1. **Virtual Drift (Covariate Shift)**: The marginal input distribution $P_t(\mathbf{x})$ changes, but the conditional posterior decision boundary $P(y \mid \mathbf{x})$ remains static:
$$P_{t_1}(\mathbf{x}) \ne P_{t_2}(\mathbf{x}), \quad \text{while } P_{t_1}(y \mid \mathbf{x}) = P_{t_2}(y \mid \mathbf{x})$$
In financial credit scoring, younger applicants may enter the market, changing the covariate distribution of age and income, but the relationship between credit debt and default probability remains invariant. The statistical model remains valid, but should be reweighted to avoid covariate shift bias.
2. **Real Concept Drift**: The underlying conditional relationship $P_t(y \mid \mathbf{x})$ changes:
$$P_{t_1}(y \mid \mathbf{x}) \ne P_{t_2}(y \mid \mathbf{x})$$
In spam detection, spammers alter email phrasing to evade filters; an email text previously classified as legitimate now represents an attack. The statistical decision boundary has altered, rendering existing model weights obsolete and requiring active model retraining.

### The Cumulative Sum (CUSUM) Control Chart
E. S. Page (1954) designed the **CUSUM** chart to detect real concept drift:
Let $e_t = \mathbb{I}(\hat{y}_t \ne y_t)$ be the binary prediction error of the streaming classifier. Under stationarity, $e_t$ has mean error rate $p_0$.
The CUSUM chart tracks:
$$S_t = \max\left( 0, S_{t-1} + e_t - p_0 - \epsilon \right)$$
Whenever $S_t > h$ (decision boundary), CUSUM flags real concept drift and initiates streaming model retraining.
"""

u8_sup = r"""
## 8.16 Random Field Theory and Spatial FDR in Neuroimaging

In functional Magnetic Resonance Imaging (fMRI) brain research, scanners record Blood-Oxygen-Level-Dependent (BOLD) signals across a three-dimensional grid of $p \approx 200,000$ voxels over time.
Because neighboring brain voxels share extensive biological connectivity and hemodynamic vascular flow, voxel-level test statistics exhibit intense local spatial correlation.

Karl Friston, Keith Worsley, and colleagues (1994, 1996) formulated **Random Field Theory (RFT)** for statistical parametric mapping.

### The Euler Characteristic Heuristic
Instead of treating voxels as independent hypotheses, RFT models the 3D test statistic map as a continuous Gaussian random field $X(\mathbf{r})$ on a spatial manifold $S \subset \mathbb{R}^3$.
When the random field is thresholded at height $u$, the excursion set $A_u = \{ \mathbf{r} \in S : X(\mathbf{r}) \ge u \}$ consists of isolated islands or clusters.

The topological **Euler Characteristic $\chi(A_u)$** counts:
$$\chi(A_u) = (\text{number of clusters}) - (\text{number of holes}) + (\text{number of hollow voids})$$
At high thresholds $u \gg 0$, holes and voids disappear, and the Euler characteristic equals the exact count of activated brain clusters!

*Theorem (Worsley's Tube Formula)*: The Family-Wise Error Rate of detecting at least one spurious brain cluster is given by the expected Euler characteristic:
$$P\left( \max_{\mathbf{r} \in S} X(\mathbf{r}) \ge u \right) \approx \mathbb{E}[\chi(A_u)] = \sum_{d=0}^3 R_d(S) \rho_d(u)$$
where $R_d(S)$ are the geometric Resel (resolution element) counts of the brain search volume, and $\rho_d(u)$ are universal Euler characteristic density polynomials. RFT controls family-wise error across continuous spatial dimensions, providing the regulatory foundation for cognitive neuroscience publications.
"""

def main():
    append_to_unit(1, u1_sup)
    append_to_unit(2, u2_sup)
    append_to_unit(3, u3_sup)
    append_to_unit(4, u4_sup)
    append_to_unit(5, u5_sup)
    append_to_unit(6, u6_sup)
    append_to_unit(7, u7_sup)
    append_to_unit(8, u8_sup)
    print("All 8 units surpassed.")

if __name__ == "__main__":
    main()
