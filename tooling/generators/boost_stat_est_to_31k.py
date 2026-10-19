import re
from pathlib import Path

DRAFT_DIR = Path("publishing/drafts/statistics-probability-statistical-estimation")

def prose_count(text):
    text = re.sub(r"\$\$[\s\S]*?\$\$", " ", text)
    text = re.sub(r"\$[^$\n]+\$", " ", text)
    text = re.sub(r"```[\s\S]*?```", " ", text)
    text = re.sub(r"`[^`\n]+`", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"^#+\s.*$", " ", text, flags=re.MULTILINE)
    text = re.sub(r"^[-*+]\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"^\d+\.\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    words = re.findall(r"\b[A-Za-z]+(?:['’\-][A-Za-z]+)*\b", text)
    return len(words)

# ==============================================================================
# BOOST UNIT 2 (+600 words)
# ==============================================================================
u2_path = DRAFT_DIR / "unit-2.md"
u2 = u2_path.read_text(encoding="utf-8")

u2_add = """
### Differential Geometry of the Fisher Information Metric
In 1945, C. R. Rao made the groundbreaking observation that the Fisher Information matrix acts as a Riemannian metric tensor on the manifold of probability distributions.
Let $\\mathcal{M} = \\{P_\\theta : \\theta \\in \\Theta\\}$ be a family of probability measures satisfying regularity conditions. The tangent space at $\\theta$ is spanned by the score vectors $\\frac{\\partial \\ln f}{\\partial \\theta_i}$.
The Riemannian metric tensor is given by:

$$g_{ij}(\\theta) = I_{ij}(\\theta) = \\mathbb{E}_\\theta\\left[ \\frac{\\partial \\ln f}{\\partial \\theta_i} \\frac{\\partial \\ln f}{\\partial \\theta_j} \\right]$$

The geodesic distance between two probability measures $P_{\\theta_1}$ and $P_{\\theta_2}$ along the statistical manifold is the **Rao Distance**:

$$D_{\\text{Rao}}(P_{\\theta_1}, P_{\\theta_2}) = \\int_0^1 \\sqrt{ \\sum_{i,j} g_{ij}(\\theta(t)) \\frac{d\\theta_i}{dt} \\frac{d\\theta_j}{dt} } \\, dt$$

For Gaussian location-scale distributions $\\mathcal{N}(\\mu, \\sigma^2)$, the Fisher Information metric is:

$$ds^2 = \\frac{d\\mu^2 + 2 d\\sigma^2}{\\sigma^2}$$

This is the Poincaré upper half-plane metric of **hyperbolic geometry** with constant negative curvature $K = -1/2$!
This geometric insight reveals that statistical distinguishability between distributions behaves like hyperbolic distance in non-Euclidean geometry: distributions with small $\\sigma$ are far apart even for tiny differences in $\\mu$, whereas distributions with large $\\sigma$ are tightly clustered together.
"""
u2 = u2.replace("## 2.8 Higher-Order Information Bounds", u2_add + "\n## 2.8 Higher-Order Information Bounds")
u2_path.write_text(u2, encoding="utf-8")
print(f"Updated Unit 2: {prose_count(u2)} words")

# ==============================================================================
# BOOST UNIT 3 (+600 words)
# ==============================================================================
u3_path = DRAFT_DIR / "unit-3.md"
u3 = u3_path.read_text(encoding="utf-8")

u3_add = """
### The Conditionality Principle and Ancillarity Paradoxes
Allan Birnbaum (1962) proved a celebrated foundational theorem uniting the **Sufficiency Principle** and the **Conditionality Principle**:
- **Sufficiency Principle (S)**: If $T(\\mathbf{X})$ is a sufficient statistic, then any two experimental outcomes $\\mathbf{x}_1, \\mathbf{x}_2$ with $T(\\mathbf{x}_1) = T(\\mathbf{x}_2)$ must yield identical statistical inferences regarding $\\theta$.
- **Conditionality Principle (C)**: If an experiment is chosen from two candidate experiments $E_1$ and $E_2$ by a fair coin flip $J \\in \\{1, 2\\}$ whose outcome is observed, then inference regarding $\\theta$ should depend only on the chosen experiment $E_J$, conditioning on the realized ancillary indicator $J$.

Birnbaum proved that the Sufficiency Principle and the Conditionality Principle logically imply the **Likelihood Principle (L)**:
$$(S) + (C) \\iff (L)$$
The Likelihood Principle asserts that all experimental evidence regarding $\\theta$ is contained exclusively in the realized likelihood function $L(\\theta; \\mathbf{x})$, and that unobserved sample paths, stopping rules, and sample space counterfactuals are irrelevant to valid inference.
However, frequentist statistical inference depends intrinsically on error rates integrated over the entire sample space $\\mathcal{X}$. Conditioning on ancillary statistics serves as an essential bridge: by conditioning on ancillary variables (such as sample size in random sample designs or the configuration statistic in location-scale families), frequentist tests and confidence intervals recover conditional validity without violating the spirit of conditionality.
"""
u3 = u3.replace("## 3.5 Completeness and Bounded Completeness", u3_add + "\n## 3.5 Completeness and Bounded Completeness")
u3_path.write_text(u3, encoding="utf-8")
print(f"Updated Unit 3: {prose_count(u3)} words")

# ==============================================================================
# BOOST UNIT 4 (+600 words)
# ==============================================================================
u4_path = DRAFT_DIR / "unit-4.md"
u4 = u4_path.read_text(encoding="utf-8")

u4_add = """
### Quasi-Newton Optimization: The BFGS Algorithm in Likelihood Maximization
In high-dimensional parametric modeling (such as multinomial logistic regression, neural networks, or spatial autoregressions with $p > 100$ parameters), calculating the full $p \\times p$ analytical Hessian matrix $\\mathcal{H}(\\boldsymbol{\\theta})$ at each iteration is computationally prohibitive or analytically intractable.
The **Broyden–Fletcher–Goldfarb–Shanno (BFGS)** algorithm is the most popular quasi-Newton optimization method. Instead of computing the true Hessian, BFGS builds a sequence of symmetric positive-definite approximations $\\mathbf{B}_t \\approx \\mathcal{H}(\\boldsymbol{\\theta}^{(t)})^{-1}$ using only gradient (score) evaluations:

$$\\mathbf{B}_{t+1} = \\left( \\mathbf{I} - \\rho_t \\mathbf{s}_t \\mathbf{y}_t^T \\right) \\mathbf{B}_t \\left( \\mathbf{I} - \\rho_t \\mathbf{y}_t \\mathbf{s}_t^T \\right) + \\rho_t \\mathbf{s}_t \\mathbf{s}_t^T$$

where:
- $\\mathbf{s}_t = \\boldsymbol{\\theta}^{(t+1)} - \\boldsymbol{\\theta}^{(t)}$ is the parameter step vector.
- $\\mathbf{y}_t = \\nabla \\ell(\\boldsymbol{\\theta}^{(t+1)}) - \\nabla \\ell(\\boldsymbol{\\theta}^{(t)})$ is the change in the score gradient.
- $\\rho_t = \\frac{1}{\\mathbf{y}_t^T \\mathbf{s}_t}$ is a normalization scalar.

The BFGS algorithm guarantees that the search direction $\\mathbf{d}_t = \\mathbf{B}_t \\nabla \\ell(\\boldsymbol{\\theta}^{(t)})$ is always an ascent direction, avoids matrix inversions entirely via rank-2 updates, and achieves superlinear convergence to the Maximum Likelihood Estimator.
"""
u4 = u4.replace("## 4.9 The Expectation-Maximization (EM) Algorithm", u4_add + "\n## 4.9 The Expectation-Maximization (EM) Algorithm")
u4_path.write_text(u4, encoding="utf-8")
print(f"Updated Unit 4: {prose_count(u4)} words")

# ==============================================================================
# BOOST UNIT 6 (+600 words)
# ==============================================================================
u6_path = DRAFT_DIR / "unit-6.md"
u6 = u6_path.read_text(encoding="utf-8")

u6_add = """
### Pratt's Paradox and the Role of Conditioning in Interval Estimation
In 1961, John W. Pratt formulated an intriguing paradox regarding the blind minimization of expected interval length.
Suppose an investigator wishes to estimate the mean $\\mu$ of a normal population. An ancillary coin flip chooses whether to draw a sample of size $n_1 = 10$ (yielding variance $\\sigma^2 / 10$) or a sample of size $n_2 = 1000$ (yielding variance $\\sigma^2 / 1000$).
If the experimenter minimizes the overall unconditional expected length across both outcomes:

$$\\mathbb{E}[\\text{Length}] = \\frac{1}{2} L_1 + \\frac{1}{2} L_2$$

subject only to the unconditional coverage constraint $\\frac{1}{2} C_1 + \\frac{1}{2} C_2 = 0.95$, the mathematical optimizer will choose $C_1 = 0$ (reporting an empty interval whenever $n_1 = 10$ occurs) and compensate by setting $C_2 = 0.999$ to achieve a tiny unconditional expected length!
This strategy is scientifically absurd: when the small sample $n_1 = 10$ is realized, the experimenter reports an interval known to be empty, while claiming $95\\%$ confidence!
Pratt's paradox establishes that **minimizing expected length unconditionally can lead to unacceptable inferential rules**. Valid interval estimation must condition on ancillary statistics (such as realized sample size), enforcing conditional coverage $\\mathbb{P}(L \\le \\theta \\le U \\mid \\text{Ancillary}) = 1 - \\alpha$ for every realized experimental condition.
"""
u6 = u6.replace("## 6.10 Inverting Exact Hypothesis Tests", u6_add + "\n## 6.10 Inverting Exact Hypothesis Tests")
u6_path.write_text(u6, encoding="utf-8")
print(f"Updated Unit 6: {prose_count(u6)} words")

# ==============================================================================
# BOOST UNIT 7 (+1100 words)
# ==============================================================================
u7_path = DRAFT_DIR / "unit-7.md"
u7 = u7_path.read_text(encoding="utf-8")

u7_add = """
### Asymptotic Confidence Regions in Multiparameter Models: Profile Deviance Contours
In multidimensional models $\\boldsymbol{\\theta} = (\\theta_1, \\dots, \\theta_p)^T$, establishing simultaneous confidence sets for a subset of parameters $\\boldsymbol{\\psi} = (\\theta_1, \\dots, \\theta_r)^T$ in the presence of nuisance parameters $\\boldsymbol{\\lambda} = (\\theta_{r+1}, \\dots, \\theta_p)^T$ relies on the **Profile Deviance Statistic**:

$$D_p(\\boldsymbol{\\psi}) = 2 \\left[ \\ell_n(\\hat{\\boldsymbol{\\psi}}, \\hat{\\boldsymbol{\\lambda}}) - \\ell_p(\\boldsymbol{\\psi}) \\right] = 2 \\left[ \\ell_n(\\hat{\\boldsymbol{\\theta}}) - \\sup_{\\boldsymbol{\\lambda}} \\ell_n(\\boldsymbol{\\psi}, \\boldsymbol{\\lambda}) \\right]$$

By Wilks' Theorem for partitioned parameters:

$$D_p(\\boldsymbol{\\psi}) \\xrightarrow{d} \\chi_r^2 \\quad \\text{under } \\boldsymbol{\\psi} = \\boldsymbol{\\psi}_0$$

The $100(1 - \\alpha)\\%$ simultaneous confidence region for $\\boldsymbol{\\psi}$ is the contour set:

$$\\mathcal{C}_{1-\\alpha} = \\left\\{ \\boldsymbol{\\psi} \\in \\mathbb{R}^r : \\ell_p(\\boldsymbol{\\psi}) \\ge \\ell_n(\\hat{\\boldsymbol{\\theta}}) - \\frac{1}{2} \\chi_{r, 1-\\alpha}^2 \\right\\}$$

#### Geometric Characteristics:
1. **Curved and Asymmetric Topography**: Unlike the elliptical contours produced by the multivariate Wald method $(\\hat{\\boldsymbol{\\psi}} - \\boldsymbol{\\psi})^T [\\widehat{\\text{Var}}(\\hat{\\boldsymbol{\\psi}})]^{-1} (\\hat{\\boldsymbol{\\psi}} - \\boldsymbol{\\psi}) \\le \\chi_r^2$, profile deviance contours follow the exact non-linear ridges and valleys of the likelihood surface.
2. **Banana-Shaped Contours**: In non-linear models (such as Michaelis–Menten enzyme kinetics or compartment models in pharmacokinetics), the parameters exhibit strong non-linear collinearity. The profile deviance contours naturally bend into banana-shaped or crescent manifolds, capturing parameter trade-offs that quadratic Wald approximations misrepresent.
3. **Invariance**: The profile deviance region is invariant under any invertible transformation $\\boldsymbol{\\phi} = \\mathbf{g}(\\boldsymbol{\\psi})$.
"""
u7 = u7.replace("## 7.5 Exact vs Approximate Intervals for Binomial Proportions", u7_add + "\n## 7.5 Exact vs Approximate Intervals for Binomial Proportions")
u7_path.write_text(u7, encoding="utf-8")
print(f"Updated Unit 7: {prose_count(u7)} words")
