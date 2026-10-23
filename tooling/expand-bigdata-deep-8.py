#!/usr/bin/env python3
"""
Deep Expansion Pass 8 for Big Data Methods for Statistics (Book 16) - Units 5 to 8.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")
    print(f"Unit {unit_num} deep pass 8 applied.")

# -------------------------------------------------------------
# UNIT 5
# -------------------------------------------------------------
u5_deep8 = r"""
## 5.13 Federated Learning Optimizers: FedAvg and FedProx

In modern mobile statistical learning and healthcare hospital consortia, data cannot be pooled into a centralized data center due to data privacy laws (GDPR, HIPAA) and communication costs. In **Federated Learning**, a global statistical model is trained cooperatively across thousands of decentralized edge client devices without transferring local data.

### 1. The Federated Averaging (FedAvg) Algorithm
H. Brendan McMahan et al. (2017) formulated **FedAvg**:
1. At communication round $t$, the central server broadcasts the current global parameter vector $\mathbf{w}_t$ to a random subset of $K$ active client devices.
2. Each client $k \in \{1, \dots, K\}$ runs $E$ epochs of local SGD on its private local dataset $\mathcal{D}_k$:
$$\mathbf{w}_{t, k}^{(0)} = \mathbf{w}_t$$
$$\mathbf{w}_{t, k}^{(e+1)} = \mathbf{w}_{t, k}^{(e)} - \eta \nabla f_k(\mathbf{w}_{t, k}^{(e)})$$
3. Clients transmit their updated weights $\mathbf{w}_{t, k}^{(E)}$ back to the central server.
4. The server aggregates the client weights proportional to local sample sizes $n_k = |\mathcal{D}_k|$:
$$\mathbf{w}_{t+1} = \sum_{k=1}^K \frac{n_k}{N} \mathbf{w}_{t, k}^{(E)}$$

### 2. Client Heterogeneity and FedProx
In real-world networks, FedAvg encounters two severe real-world challenges:
- **Statistical Heterogeneity (Non-IID Data)**: The local data distributions $P_k(\mathbf{x}, y)$ vary drastically across clients. When clients take multiple local steps ($E \gg 1$), their local trajectories drift toward distinct local minima (**Client Drift**), causing the aggregated global model to diverge.
- **System Heterogeneity (Stragglers)**: Slower devices fail to complete all $E$ epochs before communication deadlines.

Tian Li et al. (2020) resolved these issues with **FedProx**, adding a proximal regularization term to the local client objective:
$$\min_{\mathbf{w}} h_k(\mathbf{w}; \mathbf{w}_t) = f_k(\mathbf{w}) + \frac{\mu}{2} \|\mathbf{w} - \mathbf{w}_t\|_2^2$$
The proximal term $\frac{\mu}{2} \|\mathbf{w} - \mathbf{w}_t\|_2^2$ pulls the client trajectory back toward the global model, provably bounding client drift while allowing partial epoch execution for stragglers.
"""

# -------------------------------------------------------------
# UNIT 6
# -------------------------------------------------------------
u6_deep8 = r"""
## 6.12 Randomized Trace Estimation: Hutchinson's Trace Estimator

In Gaussian process hyperparameter optimization, graph spectral theory, and log-determinant estimation, statisticians must compute the trace of a massive matrix $\mathbf{A} \in \mathbb{R}^{n \times n}$:
$$\mathrm{Tr}(\mathbf{A}) = \sum_{i=1}^n A_{ii}$$
In many cases, the matrix $\mathbf{A}$ is not stored explicitly in memory: it is accessible only as a black-box matrix-vector multiplication oracle $\mathbf{x} \mapsto \mathbf{A} \mathbf{x}$ (e.g., matrix inverses $\mathbf{A} = (\mathbf{K} + \lambda \mathbf{I})^{-1}$ or graph Laplacians). Computing the diagonal elements $A_{ii} = \mathbf{e}_i^T \mathbf{A} \mathbf{e}_i$ requires $n$ matrix-vector multiplications, which is impossible when $n = 10^6$.

Michael F. Hutchinson (1990) invented the **Randomized Trace Estimator**, computing $\mathrm{Tr}(\mathbf{A})$ in a tiny number of matrix-vector products.

### 1. Mathematical Formulation
Let $\mathbf{v} \in \mathbb{R}^n$ be a random vector whose coordinates $v_1, \dots, v_n$ are independent and identically distributed with mean $0$ and variance $1$:
$$\mathbb{E}[\mathbf{v}] = \mathbf{0}, \quad \mathrm{Cov}(\mathbf{v}) = \mathbb{E}[\mathbf{v} \mathbf{v}^T] = \mathbf{I}_n$$
The quadratic form $\mathbf{v}^T \mathbf{A} \mathbf{v}$ is an unbiased estimator of the trace:
$$\mathbb{E}[\mathbf{v}^T \mathbf{A} \mathbf{v}] = \mathbb{E}[\mathrm{Tr}(\mathbf{v}^T \mathbf{A} \mathbf{v})] = \mathbb{E}[\mathrm{Tr}(\mathbf{A} \mathbf{v} \mathbf{v}^T)] = \mathrm{Tr}(\mathbf{A} \mathbb{E}[\mathbf{v} \mathbf{v}^T]) = \mathrm{Tr}(\mathbf{A} \mathbf{I}_n) = \mathrm{Tr}(\mathbf{A})$$

### 2. Optimal Distribution and Variance Minimization
Hutchinson proved that the variance of the estimator is:
$$\mathrm{Var}(\mathbf{v}^T \mathbf{A} \mathbf{v}) = (\mathbb{E}[v_i^4] - 3) \sum_{i=1}^n A_{ii}^2 + 2 \mathrm{Tr}(\mathbf{A}^2)$$
- If $\mathbf{v} \sim \mathcal{N}(\mathbf{0}, \mathbf{I}_n)$, then $\mathbb{E}[v_i^4] = 3$, so $\mathrm{Var} = 2 \mathrm{Tr}(\mathbf{A}^2)$.
- If $\mathbf{v}$ is a **Rademacher vector** ($v_i \in \{-1, +1\}$ with equal probability), then $v_i^2 = 1$ identically, so $\mathbb{E}[v_i^4] = 1$. The variance simplifies to:
$$\mathrm{Var}_{\text{Rademacher}} = 2 \sum_{i \ne j} A_{ij}^2 = 2 \|\mathbf{A} - \mathrm{diag}(\mathbf{A})\|_F^2$$
Rademacher vectors achieve minimal variance! Averaging $m \approx 30$ to $50$ random matrix-vector multiplications estimates the trace of a million-dimensional matrix to within $1\%$ relative error in seconds.
"""

# -------------------------------------------------------------
# UNIT 7
# -------------------------------------------------------------
u7_deep8 = r"""
## 7.14 The Page-Hinkley Test for Streaming Anomaly Detection

In industrial telemetry, fraud monitoring, and automated trading, statisticians must detect instantaneous structural shifts in the mean level of a continuous data stream.
E. S. Page (1954) and D. V. Hinkley (1970) formulated the **Page-Hinkley (PH) Test**, a sequential cumulative sum diagnostic for detecting abrupt changes in streaming data.

### Algorithmic Execution
Let $x_1, x_2, \dots$ be a continuous data stream with expected baseline mean $\mu_0$.
1. Maintain the running cumulative deviation from the target:
$$U_t = \sum_{i=1}^t (x_i - \mu_0 - \delta)$$
where $\delta > 0$ is a tolerance parameter representing the minimum magnitude of shift to detect.
2. Track the historical minimum of the cumulative sum:
$$m_t = \min_{1 \le s \le t} U_s$$
3. Compute the Page-Hinkley test statistic:
$$P H_t = U_t - m_t$$
4. If $P H_t \ge \lambda$ (where $\lambda > 0$ is a user-defined threshold), **trigger an alarm**: an upward structural shift has occurred!
5. Reset the statistic: $U_t \leftarrow 0, m_t \leftarrow 0$.

The Page-Hinkley test requires storing only two scalar values ($U_t, m_t$), executes in strict $O(1)$ time per stream arrival, and provides optimal sequential detection bounds minimizing mean time to detection subject to fixed false alarm rates.
"""

# -------------------------------------------------------------
# UNIT 8
# -------------------------------------------------------------
u8_deep8 = r"""
## 8.13 Conformalized Quantile Regression (CQR)

In Unit 8.10, we examined Split Conformal Prediction, which constructs prediction intervals by adding and subtracting a constant residual scalar: $\hat{\mu}(\mathbf{x}) \pm q_\alpha$.
While mathematically exact in marginal coverage, this constant-width interval fails under **Heteroskedasticity**: if the data variance $\sigma^2(\mathbf{x})$ is small when $x \approx 0$ but large when $x \gg 0$, a constant-width interval will be unnecessarily wide for small $x$ and dangerously narrow for large $x$, failing **conditional coverage**.

Yaniv Romano, Matteo Sesia, and Emmanuel Candès (2019) introduced **Conformalized Quantile Regression (CQR)**, marrying quantile regression with conformal prediction to deliver variable-width adaptive intervals with exact finite-sample guarantees.

### 1. Dual Quantile Training
1. Train two non-parametric quantile regressors on the training set:
   - $\hat{q}_{\alpha/2}(\mathbf{x})$: estimates the lower conditional quantile $\tau_1 = \alpha/2$ (e.g., $2.5\%$).
   - $\hat{q}_{1 - \alpha/2}(\mathbf{x})$: estimates the upper conditional quantile $\tau_2 = 1 - \alpha/2$ (e.g., $97.5\%$).
   These models can be fitted via Pinball loss minimization using Gradient Boosting (LightGBM/XGBoost) or deep neural networks.

### 2. Conformal Non-Conformity Scoring
For each observation $i$ in the calibration set $\mathcal{D}_{\text{cal}}$, evaluate the signed conformity score measuring how far the observation falls outside the quantile band:
$$E_i = \max\left( \hat{q}_{\alpha/2}(\mathbf{x}_i) - Y_i, \, Y_i - \hat{q}_{1 - \alpha/2}(\mathbf{x}_i) \right)$$
- If $Y_i$ falls inside the predicted band $[\hat{q}_{\alpha/2}, \hat{q}_{1-\alpha/2}]$, $E_i \le 0$.
- If $Y_i$ falls outside the band, $E_i > 0$ measures the distance to the nearest boundary.

### 3. Conformalized Adaptive Prediction Interval
Let $Q_{1-\alpha}(E, \mathcal{D}_{\text{cal}})$ be the $(1-\alpha)(1 + 1/|\mathcal{D}_{\text{cal}}|)$ empirical quantile of the calibration scores.
For any new query point $\mathbf{x}_{n+1}$, the CQR prediction interval is:
$$\mathcal{C}(\mathbf{x}_{n+1}) = \left[ \hat{q}_{\alpha/2}(\mathbf{x}_{n+1}) - Q_{1-\alpha}, \, \hat{q}_{1 - \alpha/2}(\mathbf{x}_{n+1}) + Q_{1-\alpha} \right]$$

*Theoretical Guarantee*: The CQR interval guarantees exact finite-sample coverage $P(Y_{n+1} \in \mathcal{C}(\mathbf{x}_{n+1})) \ge 1 - \alpha$, while dynamically expanding in volatile regions and contracting in quiet regions, providing the state-of-the-art framework for uncertainty quantification in modern machine learning.
"""

def main():
    append_to_unit(5, u5_deep8)
    append_to_unit(6, u6_deep8)
    append_to_unit(7, u7_deep8)
    append_to_unit(8, u8_deep8)
    print("Units 5-8 deep pass 8 applied.")

if __name__ == "__main__":
    main()
