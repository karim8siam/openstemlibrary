import re
from pathlib import Path

# Expand Unit 6
p6 = Path("publishing/drafts/statistics-probability-big-data-methods-for-statistics/unit-6.md")
t6 = p6.read_text(encoding="utf-8")

extra_u6 = r"""

## 6.19 Streaming Sketching for Dynamic Graph Laplacians
In modern large-scale network analysis, graph topologies arrive as edge insertion and deletion streams. Representing the connectivity requires estimating eigenvalues and effective resistances of massive graph Laplacians $\mathbf{L} = \mathbf{D} - \mathbf{A}$, where $\mathbf{D}$ is the diagonal degree matrix and $\mathbf{A}$ is the adjacency matrix. When vertices number in the millions ($n > 10^7$), computing spectral embeddings directly becomes prohibitive. 

The Spielman-Srivastava spectral sparsification framework applies randomized leverage score sampling to graph edges. The statistical leverage score of an edge $e = (u, v)$ is mathematically equivalent to its effective electrical resistance $R_e$ when each edge is treated as a 1-ohm resistor:
$$w_e^{\text{eff}} = (\mathbf{e}_u - \mathbf{e}_v)^T \mathbf{L}^\dagger (\mathbf{e}_u - \mathbf{e}_v) = R_e$$
By sampling edges with probability proportional to their effective resistances $p_e \propto w_e R_e$, one constructs an ultra-sparse graph $\tilde{\mathbf{L}}$ having only $\mathcal{O}(n \log n / \epsilon^2)$ edges that satisfies the spectral approximation guarantee:
$$(1 - \epsilon) \mathbf{x}^T \mathbf{L} \mathbf{x} \le \mathbf{x}^T \tilde{\mathbf{L}} \mathbf{x} \le (1 + \epsilon) \mathbf{x}^T \mathbf{L} \mathbf{x} \quad \forall \mathbf{x} \in \mathbb{R}^n$$
This guarantees that all graph cuts, random walk hitting times, and Laplacian linear system solutions $\mathbf{L} \mathbf{x} = \mathbf{b}$ are preserved within relative error $\epsilon$, reducing computational complexity from $\mathcal{O}(n^3)$ to nearly linear time $\tilde{\mathcal{O}}(m \log^c n)$.

## 6.20 High-Dimensional Random Projection Diagnostics and Metric Verification
When practitioners deploy random projections in production data pipelines, verifying the preservation of pairwise distances without calculating all $\mathcal{O}(n^2)$ distances is a critical quality assurance task. A principled diagnostic methodology relies on extreme-value subsampling:
1. Select a stratified anchor subset of $m \ll n$ representative sample points across the empirical feature domain.
2. For each anchor, identify its $k$-nearest neighbors in both the ambient space $\mathbb{R}^p$ and the projected subspace $\mathbb{R}^d$.
3. Compute the rank correlation (Spearman's $\rho$ or Kendall's $\tau$) between ambient and projected pairwise distances.
4. If the empirical distortion $\max_{i, j} \left| \frac{\|\mathbf{P} \mathbf{x}_i - \mathbf{P} \mathbf{x}_j\|_2^2}{\|\mathbf{x}_i - \mathbf{x}_j\|_2^2} - 1 \right|$ exceeds tolerance $\epsilon$, incrementally increase the target sketch dimension $d$ according to the theoretical bound $d \ge 8 \epsilon^{-2} \ln(n / \sqrt{\delta})$.
"""

t6 += extra_u6
p6.write_text(t6, encoding="utf-8")
print("Expanded Unit 6")

# Expand Unit 7
p7 = Path("publishing/drafts/statistics-probability-big-data-methods-for-statistics/unit-7.md")
t7 = p7.read_text(encoding="utf-8")

extra_u7 = r"""

## 7.19 Asymmetric Loss and Online Quantile Tracking
In financial streaming telemetry and real-time infrastructure monitoring, operators must track extreme percentiles (such as the 99th or 99.9th percentile of request latencies) rather than simple running averages. Traditional streaming quantiles such as Greenwald-Khanna maintain deterministic error bounds $\epsilon N$ at the cost of dynamic tree rebalancing. An elegant alternative is online stochastic gradient tracking under pinball loss.

The pinball (check) loss function for quantile $\tau \in (0, 1)$ is defined as:
$$\rho_\tau(u) = u (\tau - \mathbb{I}(u < 0)) = \begin{cases} \tau u & \text{if } u \ge 0 \\ (\tau - 1) u & \text{if } u < 0 \end{cases}$$
The subgradient with respect to candidate quantile estimate $q$ given streaming observation $x_t$ is simply:
$$\partial_q \rho_\tau(x_t - q) = \begin{cases} -\tau & \text{if } x_t > q \\ 1 - \tau & \text{if } x_t < q \end{cases}$$
The online stochastic update rule is remarkably simple:
$$q_{t+1} = q_t + \eta_t (\mathbb{I}(x_t > q_t) - (1 - \tau))$$
When combined with Robbins-Monro step decay $\eta_t = c / t^\alpha$ or adaptive learning rates, this one-line update tracks non-stationary extreme quantiles with negligible CPU cycles and $\mathcal{O}(1)$ memory.

## 7.20 Stream Deduplication and Sliding-Window HyperLogLog
Standard HyperLogLog accumulates distinct cardinality over unbounded streams from epoch zero. In streaming operational environments, however, queries frequently demand sliding-window cardinality: "How many unique visitors were active within the past 60 minutes?" 

Directly subtracting two HyperLogLog sketches is mathematically impossible because the maximum-zero operation $\max(M[j], \rho(w))$ is idempotent and non-invertible. To solve this challenge, Sliding HyperLogLog replaces each 6-bit register with a timestamped record $(v, t_{\text{last}})$, storing the latest arrival timestamp $t_{\text{last}}$ that yielded value $v$. When evaluating the sliding window $[T - W, T]$, the estimator discards any entries with $t_{\text{last}} < T - W$ before computing the harmonic mean. This sliding-window architecture provides accurate streaming deduplication and unique visitor metrics across moving time horizons with constant bounded memory.
"""

t7 += extra_u7
p7.write_text(t7, encoding="utf-8")
print("Expanded Unit 7")

# Expand Unit 8
p8 = Path("publishing/drafts/statistics-probability-big-data-methods-for-statistics/unit-8.md")
t8 = p8.read_text(encoding="utf-8")

extra_u8 = r"""

## 8.18 Adaptive False Discovery Control in Spatial and Structured Domains
Standard high-dimensional multiple testing procedures assume exchangeability among hypotheses or treat hypothesis indices as an unordered set. In biological imaging, geospatial surveillance, and neuroimaging (fMRI), test statistics exhibit prominent spatial autocorrelation: neighboring voxels or coordinates share latent physiological noise and true signals form contiguous clusters rather than isolated spikes.

Applying standard BH under spatial clustering can lead to high variability in empirical false discoveries. Topological approaches based on Gaussian Random Fields establish cluster-extent thresholding:
1. Define a primary voxel-level intensity threshold $u$ (such as $p < 0.001$).
2. Identify contiguous connected clusters of suprathreshold voxels exceeding spatial volume threshold $k$.
3. Compute cluster-level significance using the Euler characteristic heuristic of Gaussian excursion sets:
$$\mathbb{E}[\chi(A_u)] = \sum_{d=0}^D \mathcal{L}_d(\Omega) \rho_d(u)$$
where $\mathcal{L}_d(\Omega)$ represents the Lipschitz-Killing curvature measures of the spatial search domain $\Omega$, and $\rho_d(u)$ represents the Euler characteristic density of dimension $d$. This spatial topological correction achieves rigorous Family-Wise Error Rate or Cluster-FDR control while multiplying statistical power relative to unadjusted voxelwise testing.
"""

t8 += extra_u8
p8.write_text(t8, encoding="utf-8")
print("Expanded Unit 8")
