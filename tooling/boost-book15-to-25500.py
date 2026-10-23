#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-statistical-simulation-and-monte-carlo-methods"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")

u2_add = r"""
## 2.18 Fast Sampling from Truncated Multivariate Normals

In constrained econometric models and spatial Gaussian processes with inequality barriers, one must sample from a high-dimensional truncated Gaussian distribution $\mathbf{X} \sim \mathcal{N}(\boldsymbol{\mu}, \mathbf{\Sigma})$ subject to linear constraints $\mathbf{a} \le \mathbf{B} \mathbf{X} \le \mathbf{b}$. Naive rejection sampling fails completely because the probability of an unconstrained Gaussian draw satisfying dozens of joint linear inequalities is virtually zero ($P \le 10^{-15}$).

Zdravko Botev (2017) developed an exact minimax tilting algorithm that combines exponential twisting with smooth unconstrained optimization to achieve acceptance rates bounded away from zero regardless of dimension $d$. Alternatively, componentwise Gibbs sampling updates each scalar coordinate $X_j$ conditional on all remaining coordinates $\mathbf{X}_{-j}$ from a univariate truncated Gaussian distribution using Robert's optimal translated exponential proposal. This allows simulation of thousands of correlated variables under strict convex polyhedral bounds in milliseconds.
"""

u3_add = r"""
## 3.19 Resampling for Clustered and Panel Data Structures

In econometric panel datasets, longitudinal clinical trials, and multi-stage educational surveys, observations are grouped into natural clusters (e.g., patients within hospitals, students within classrooms, or repeated observations across time for a firm). Observations within the same cluster share unobserved random shocks, violating the fundamental mutual independence assumption of the standard bootstrap.

When data exhibit intra-cluster correlation, applying naive observation-level bootstrap resampling severely underestimates standard errors and produces anti-conservative confidence intervals. The **Cluster Bootstrap** (Cameron, Gelbach, and Miller 2008) resamples entire clusters with replacement:
$$\mathcal{C}_1^*, \mathcal{C}_2^*, \dots, \mathcal{C}_G^* \sim \text{Uniform with replacement from } \{\mathcal{C}_1, \dots, \mathcal{C}_G\}$$
By treating each cluster as an independent statistical unit and preserving the entire internal covariance matrix within each cluster, the cluster bootstrap provides asymptotically valid inference for panel regression estimators without requiring parametric specification of the intra-cluster error covariance structure.
"""

u6_add = r"""
## 6.16 Convergence Assessment via the Geweke Spectral Diagnostic

While the Gelman-Rubin $\hat{R}$ statistic requires running multiple independent parallel Markov chains, John Geweke (1992) proposed a spectral time-series diagnostic for evaluating the stationarity of a single MCMC chain.

Geweke's method compares the sample mean of the early portion of the chain (typically the first $10\%$, denoted $\bar{X}_A$) with the sample mean of the concluding portion of the chain (typically the last $50\%$, denoted $\bar{X}_B$), omitting the middle $40\%$ to ensure independence between the two windows. The test statistic is a two-sample asymptotic z-score:
$$Z = \frac{\bar{X}_A - \bar{X}_B}{\sqrt{\frac{\hat{S}_A(0)}{n_A} + \frac{\hat{S}_B(0)}{n_B}}}$$
where $\hat{S}_A(0)$ and $\hat{S}_B(0)$ are spectral density estimates of the asymptotic variance at zero frequency, computed using Parzen or Tukey-Hanning spectral windows to account for serial autocorrelation. Under the null hypothesis that the Markov chain has achieved stationarity, $Z$ is asymptotically distributed as standard normal $\mathcal{N}(0, 1)$. Values of $|Z| > 2$ provide strong statistical evidence of non-stationarity, warning the analyst that burn-in was insufficient.
"""

u7_add = r"""
## 7.18 Simulated Annealing for Global Non-Convex Optimization

In structural bioinformatics, portfolio optimization with cardinality constraints, and neural architecture search, objective loss functions $f(\mathbf{x})$ exhibit complex non-convex landscapes with thousands of deceptive local minima. Deterministic gradient descent gets trapped permanently in the nearest local basin of attraction.

Scott Kirkpatrick, C. Daniel Gelatt, and Mario P. Vecchi (1983) adapted the Metropolis MCMC algorithm into **Simulated Annealing (SA)**, treating optimization as the physical process of slowly cooling molten metal to find its crystalline ground state. 

At cooling iteration $k$, a proposed move $\mathbf{x}_{\text{prop}} \sim q(\cdot \mid \mathbf{x}_k)$ is accepted with probability:
$$\alpha = \min\left( 1, \exp\left( -\frac{f(\mathbf{x}_{\text{prop}}) - f(\mathbf{x}_k)}{T_k} \right) \right)$$
When the temperature $T_k$ is high, the algorithm readily accepts uphill moves ($f(\mathbf{x}_{\text{prop}}) > f(\mathbf{x}_k)$), freely exploring the global state space. As temperature $T_k \to 0$ according to a logarithmic cooling schedule $T_k = T_0 / \log(k + 1)$ (Hajek 1988), the chain freezes into the deepest global minimum with probability approaching 1.0.
"""

u8_add = r"""
## 8.17 Normalizing Flows for Amortized Generative Sampling

In contemporary computational statistics, **Normalizing Flows** provide an expressive class of invertible generative models that bridge parametric density estimation and Monte Carlo simulation. 

A normalizing flow transforms a simple base distribution (such as a standard isotropic Gaussian $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$) into a complex, multimodal target density $\mathbf{x} \in \mathbb{R}^d$ through a sequence of $K$ invertible, differentiable transformations:
$$\mathbf{x} = f_K \circ f_{K-1} \circ \dots \circ f_1(\mathbf{z})$$
By the multivariate change-of-variables theorem, the exact target log-density is computable in closed form:
$$\log p_X(\mathbf{x}) = \log p_Z(\mathbf{z}) - \sum_{k=1}^K \log \left| \det \left( \frac{\partial f_k}{\partial \mathbf{z}_{k-1}} \right) \right|$$
By designing transformations with triangular Jacobian matrices (such as RealNVP or Masked Autoregressive Flows), evaluating the determinant requires only $O(d)$ operations. Once trained on simulation trajectories, normalizing flows generate millions of exact synthetic data draws in milliseconds, amortizing inference across complex physical systems.
"""

append_to_unit(2, u2_add)
append_to_unit(3, u3_add)
append_to_unit(6, u6_add)
append_to_unit(7, u7_add)
append_to_unit(8, u8_add)
print("Boost applied.")
