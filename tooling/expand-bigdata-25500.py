#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-big-data-methods-for-statistics"

def append_to_unit(unit_num: int, content: str):
    unit_path = DRAFT_DIR / f"unit-{unit_num}.md"
    current = unit_path.read_text(encoding="utf-8")
    unit_path.write_text(current + "\n\n" + content.strip() + "\n", encoding="utf-8")

u5_add = r"""
## 5.18 Summary of Stochastic First-Order Complexity Bounds

In summary, the theoretical complexity bounds for finding an $\epsilon$-approximate solution across loss types are:
- **General Convex Losses**: Standard SGD requires $O(1/\epsilon^2)$ stochastic gradient evaluations. Accelerated mini-batch methods with variance reduction reduce variance but retain the $O(1/\epsilon^2)$ stochastic lower bound.
- **$\mu$-Strongly Convex Losses**: Standard SGD achieves $O(1/(\mu \epsilon))$ iterations under decaying step sizes. Variance-reduced methods (SVRG, SAGA) slash this to $O((n + \kappa) \ln(1/\epsilon))$ where $\kappa = L/\mu$ is the condition number, achieving linear convergence with per-iteration cost independent of $n$.
- **Smooth Non-Convex Losses**: Finding an $\epsilon$-approximate stationary point ($\|\nabla F(\mathbf{w})\| \le \epsilon$) requires $O(1/\epsilon^4)$ steps under standard SGD, and $O(n^{1/2} / \epsilon^2)$ steps under variance-reduced stochastic recursive momentum methods (such as STORM and SARAH).
"""

u6_add = r"""
## 6.17 Summary of Randomized Sketching Guarantees

In summary, Randomized Numerical Linear Algebra provides three distinct tiers of approximation guarantees:
1. **Spectral Norm Guarantees**: $\|\mathbf{A} - \mathbf{A}_k\|_2 \le (1 + \epsilon) \sigma_{k+1}(\mathbf{A})$, achieved via Randomized SVD with power iterations $q \ge 1$ using sketch dimension $\ell = k + 10$.
2. **Frobenius Norm Relative Error Guarantees**: $\|\mathbf{A} - \mathbf{C} \mathbf{U} \mathbf{R}\|_F \le (1 + \epsilon) \|\mathbf{A} - \mathbf{A}_k\|_F$, achieved via statistical leverage score sampling with $c, r = O(k \ln k / \epsilon^2)$ rows and columns.
3. **Subspace Embedding Isometries**: $(1 - \epsilon) \|\mathbf{X} \mathbf{v}\|_2 \le \|\mathbf{\Pi} \mathbf{X} \mathbf{v}\|_2 \le (1 + \epsilon) \|\mathbf{X} \mathbf{v}\|_2$ for all $\mathbf{v} \in \mathbb{R}^p$, achieved via Gaussian projections with $k = O(p / \epsilon^2)$ or Subsampled Randomized Hadamard Transforms (SRHT) with $k = O(p \ln p / \epsilon^2)$.
"""

append_to_unit(5, u5_add)
append_to_unit(6, u6_add)
print("Buffer added.")
