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
# BOOST UNIT 3: Pitman-Koopman-Darmois Theorem
# ==============================================================================
u3_path = DRAFT_DIR / "unit-3.md"
u3 = u3_path.read_text(encoding="utf-8")
u3_add = """
### The Pitman–Koopman–Darmois Theorem
Can an analyst achieve finite-dimensional data reduction in every distribution family?
In 1935–1936, E. J. G. Pitman, B. O. Koopman, and G. Darmois independently proved a celebrated structural theorem that establishes the unique mathematical supremacy of the exponential family:

#### Theorem (Pitman–Koopman–Darmois):
Let $X_1, X_2, \\dots, X_n$ be an independent, identically distributed sample from a family of continuous distributions $\\mathcal{P} = \\{f(x; \\theta) : \\theta \\in \\Theta\\}$ whose support is independent of $\\theta$, and whose density is continuously differentiable in $x$.
Then there exists a sufficient statistic $T(\\mathbf{X}) = (T_1(\\mathbf{X}), \\dots, T_k(\\mathbf{X}))^T$ whose dimension $k$ remains strictly fixed and bounded as the sample size $n \\to \\infty$ **if and only if** the distribution belongs to an **exponential family**:

$$f(x; \\theta) = h(x) \\exp\\left( \\sum_{j=1}^k \\eta_j(\\theta) T_j(x) - A(\\theta) \\right)$$

If a distribution family does not belong to the exponential family (such as the Cauchy distribution, the Student's $t$-distribution, or the Weibull distribution with unknown shape), then as $n$ grows, the minimal sufficient statistic is the entire order statistic vector $(X_{(1)}, X_{(2)}, \\dots, X_{(n)})$ of dimension $n$! In non-exponential families, no data compression is mathematically possible without discarding essential information regarding $\\theta$.
"""
u3 = u3.replace("## 3.7 The Rao–Blackwell Theorem", u3_add + "\n## 3.7 The Rao–Blackwell Theorem")
u3_path.write_text(u3, encoding="utf-8")
print(f"Updated Unit 3: {prose_count(u3)} words")

# ==============================================================================
# BOOST UNIT 5: Godambe Information and Estimating Functions
# ==============================================================================
u5_path = DRAFT_DIR / "unit-5.md"
u5 = u5_path.read_text(encoding="utf-8")
u5_add = """
### Estimating Functions and the Godambe Information Matrix
In semiparametric inference and econometrics, parameter estimators are frequently defined as solutions to an unbiased estimating equation:

$$\\sum_{i=1}^n \\boldsymbol{\\psi}(X_i; \\boldsymbol{\\theta}) = \\mathbf{0} \\quad \\text{with} \\quad \\mathbb{E}_\\theta[\\boldsymbol{\\psi}(X; \\boldsymbol{\\theta})] = \\mathbf{0}$$

In 1960, V. P. Godambe formulated a general optimality theory for estimating functions. Define:
- The sensitivity matrix: $\\mathbf{S}_\\psi = \\mathbb{E}\\left[ \\nabla_{\\boldsymbol{\\theta}} \\boldsymbol{\\psi}(X; \\boldsymbol{\\theta}) \\right]$
- The variability matrix: $\\mathbf{V}_\\psi = \\mathbb{E}\\left[ \\boldsymbol{\\psi}(X; \\boldsymbol{\\theta}) \\boldsymbol{\\psi}(X; \\boldsymbol{\\theta})^T \\right]$

The **Godambe Information Matrix** is defined as:

$$\\mathbf{I}_{\\text{Godambe}}(\\boldsymbol{\\theta}) = \\mathbf{S}_\\psi^T \\mathbf{V}_\\psi^{-1} \\mathbf{S}_\\psi$$

Godambe proved that the asymptotic covariance of the estimator $\\hat{\\boldsymbol{\\theta}}$ satisfies:

$$\\text{AsyVar}(\\hat{\\boldsymbol{\\theta}}) = [\\mathbf{I}_{\\text{Godambe}}(\\boldsymbol{\\theta})]^{-1} = \\mathbf{S}_\\psi^{-1} \\mathbf{V}_\\psi (\\mathbf{S}_\\psi^T)^{-1}$$

Notice that this is identical to the Huber–White sandwich covariance! Godambe proved that among all regular unbiased estimating functions, the score function $\\boldsymbol{\\psi}^* = \\nabla \\ln f(X; \\boldsymbol{\\theta})$ maximizes the Godambe Information matrix in the Loewner ordering, attaining the classical Fisher Information.
"""
u5 = u5.replace("## 5.8 Asymptotic Equivalence of the Classical Likelihood Trinity", u5_add + "\n## 5.8 Asymptotic Equivalence of the Classical Likelihood Trinity")
u5_path.write_text(u5, encoding="utf-8")
print(f"Updated Unit 5: {prose_count(u5)} words")

# ==============================================================================
# BOOST UNIT 6: Pitman Location-Scale Equivariant Intervals
# ==============================================================================
u6_path = DRAFT_DIR / "unit-6.md"
u6 = u6_path.read_text(encoding="utf-8")
u6_add = """
### Equivariant Interval Estimation in Location-Scale Families
In a location-scale family $f(x; \\mu, \\sigma) = \\frac{1}{\\sigma} f_0\\left( \\frac{x - \\mu}{\\sigma} \\right)$, physical measurements are subject to changes in measurement origin (translation $X \\to X + c$) and scale units (dilation $X \\to a X$ for $a > 0$).
A confidence interval $[L(\\mathbf{X}), U(\\mathbf{X})]$ is said to be **equivariant** under the affine group if:

$$L(a \\mathbf{X} + c \\mathbf{1}) = a L(\\mathbf{X}) + c \\quad \\text{and} \\quad U(a \\mathbf{X} + c \\mathbf{1}) = a U(\\mathbf{X}) + c$$

E. J. G. Pitman (1939) proved that every equivariant estimator and confidence interval can be expressed in terms of the sample mean $\\bar{X}$, sample standard deviation $S$, and the **configuration ancillary statistic**:

$$\\mathbf{C} = \\left( \\frac{X_1 - \\bar{X}}{S}, \\frac{X_2 - \\bar{X}}{S}, \\dots, \\frac{X_n - \\bar{X}}{S} \\right)$$

The optimal equivariant confidence interval conditions on the realized configuration vector $\\mathbf{C} = \\mathbf{c}$, adjusting the interval width to the exact geometric shape of the realized data sample. For non-normal location-scale distributions (such as Cauchy, logistic, or extreme value distributions), Pitman's conditional equivariant intervals provide exact confidence levels that strictly dominate unconditional intervals.
"""
u6 = u6.replace("## 6.9 Shortest Expected Length vs Uniformly Most Accurate (UMA) Confidence Sets", u6_add + "\n## 6.9 Shortest Expected Length vs Uniformly Most Accurate (UMA) Confidence Sets")
u6_path.write_text(u6, encoding="utf-8")
print(f"Updated Unit 6: {prose_count(u6)} words")

# ==============================================================================
# BOOST UNIT 7: Probability-Matching Priors and Calibrated Intervals
# ==============================================================================
u7_path = DRAFT_DIR / "unit-7.md"
u7 = u7_path.read_text(encoding="utf-8")
u7_add = """
### Probability-Matching Priors: The Welch–Peers Synthesis
Can a Bayesian credible interval achieve exact frequentist coverage?
In 1963, B. L. Welch and H. W. Peers investigated what prior distributions $\\pi(\\theta)$ generate Bayesian posterior credible intervals whose frequentist coverage probability matches the nominal level $1 - \\alpha$ to higher orders of asymptotic approximation:

$$\\mathbb{P}_\\theta\\left( \\theta \\le U_{\\text{Bayes}}(\\mathbf{X}) \\right) = 1 - \\alpha + \\mathcal{O}\\left( \\frac{1}{n} \\right)$$

Welch and Peers proved that in a single-parameter regular model, the unique prior that eliminates the $\\mathcal{O}(1/\\sqrt{n})$ frequentist coverage bias is **Jeffreys' invariant prior**:

$$\\pi_{\\text{matching}}(\\theta) = \\pi_J(\\theta) \\propto \\sqrt{I_1(\\theta)}$$

Under Jeffreys' prior, the Bayesian $(1 - \\alpha)$ one-sided credible limit is second-order accurate: its frequentist coverage error decays at rate $\\mathcal{O}(1/n)$ rather than the usual $\\mathcal{O}(1/\\sqrt{n})$!
This celebrated result, known as the **Welch–Peers Theorem**, establishes a deep and satisfying mathematical bridge between the two competing philosophies: objective Bayesian credible intervals constructed using Jeffreys' prior are simultaneously the most accurate frequentist confidence intervals conceivable.
"""
u7 = u7.replace("## 7.10 Interval Estimation under Model Misspecification", u7_add + "\n## 7.10 Interval Estimation under Model Misspecification")
u7_path.write_text(u7, encoding="utf-8")
print(f"Updated Unit 7: {prose_count(u7)} words")
