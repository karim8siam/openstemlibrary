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
# EXPAND UNIT 5 (Asymptotics)
# ==============================================================================
u5_path = DRAFT_DIR / "unit-5.md"
u5 = u5_path.read_text(encoding="utf-8")

u5_add_bahadur = """
### Bahadur Efficiency and Exact Slopes in Large Deviations
While Pitman asymptotic relative efficiency evaluates the local power of estimators in a $\\mathcal{O}(1/\\sqrt{n})$ neighborhood of the true parameter, R. R. Bahadur (1960) developed a global asymptotic efficiency theory based on large deviation principles.
Let $T_n$ be a sequence of estimators of $\\theta$, and consider the tail probability of estimation error exceeding a fixed non-zero threshold $\\epsilon > 0$:

$$P_\\theta(|T_n - \\theta| \\ge \\epsilon)$$

By Cramér's Large Deviation Theorem, this tail probability decays exponentially fast with sample size:

$$\\lim_{n \\to \\infty} -\\frac{1}{n} \\ln P_\\theta(|T_n - \\theta| \\ge \\epsilon) = c(T, \\epsilon)$$

where $c(T, \\epsilon) > 0$ is the **Bahadur exact slope**.
Bahadur proved that for any regular estimator sequence, the exact slope is fundamentally bounded by the Kullback–Leibler divergence:

$$c(T, \\epsilon) \\le \\inf_{\\theta': |\\theta' - \\theta| \\ge \\epsilon} \\text{KL}(P_\\theta \\| P_{\\theta'})$$

An estimator is defined to be **Bahadur efficient** if its exact slope achieves this theoretical upper bound for all $\\epsilon > 0$.
The Maximum Likelihood Estimator is uniquely Bahadur efficient! The exponential decay rate of large estimation errors is maximized by the MLE, reinforcing its optimality from both local Gaussian and global large-deviation perspectives.
"""

u5_add_vuong = """
### Model Selection via Vuong's Likelihood Ratio Test for Misspecified Models
When an analyst compares two competing non-nested parametric families $\\mathcal{F} = \\{f(x; \\boldsymbol{\\beta})\\}$ and $\\mathcal{G} = \\{g(x; \\boldsymbol{\\gamma})\\}$, neither of which may be the true data-generating distribution $h_0(x)$, Quang Vuong (1989) formulated an asymptotic test based on the difference in Kullback–Leibler information criteria.
Let $\\ell_f(\\hat{\\boldsymbol{\\beta}})$ and $\\ell_g(\\hat{\\boldsymbol{\\gamma}})$ be the maximized log-likelihoods under the two candidate models. The log-likelihood ratio statistic is:

$$LR_n(\\hat{\\boldsymbol{\\beta}}, \\hat{\\boldsymbol{\\gamma}}) = \\sum_{i=1}^n \\ln\\left( \\frac{f(X_i; \\hat{\\boldsymbol{\\beta}})}{g(X_i; \\hat{\\boldsymbol{\\gamma}})} \\right) = \\ell_f(\\hat{\\boldsymbol{\\beta}}) - \\ell_g(\\hat{\\boldsymbol{\\gamma}})$$

Define the sample variance of the individual log-likelihood ratio contributions:

$$\\omega_n^2 = \\frac{1}{n} \\sum_{i=1}^n \\left[ \\ln\\left( \\frac{f(X_i; \\hat{\\boldsymbol{\\beta}})}{g(X_i; \\hat{\\boldsymbol{\\gamma}})} \\right) \\right]^2 - \\left[ \\frac{1}{n} LR_n(\\hat{\\boldsymbol{\\beta}}, \\hat{\\boldsymbol{\\gamma}}) \\right]^2$$

Vuong established that under the null hypothesis that both models are equally close to the true distribution in Kullback–Leibler distance ($H_0: \\text{KL}(h_0 \\| f) = \\text{KL}(h_0 \\| g)$):

$$V_n = \\frac{LR_n(\\hat{\\boldsymbol{\\beta}}, \\hat{\\boldsymbol{\\gamma}})}{\\sqrt{n} \\, \\omega_n} \\xrightarrow{d} \\mathcal{N}(0, 1)$$

If $V_n > +z_{1-\\alpha/2}$, model $\\mathcal{F}$ is statistically significantly closer to the true distribution; if $V_n < -z_{1-\\alpha/2}$, model $\\mathcal{G}$ is preferred. Vuong's test provides an asymptotically rigorous mechanism for discriminating between competing scientific theories under inevitable model misspecification.
"""

u5 = u5.replace("## 5.4 Asymptotic Efficiency", u5_add_bahadur + "\n## 5.4 Asymptotic Efficiency")
u5 = u5.replace("## 5.7 The Huber–White Sandwich Covariance Estimator", u5_add_vuong + "\n## 5.7 The Huber–White Sandwich Covariance Estimator")
u5_path.write_text(u5, encoding="utf-8")
print(f"Updated Unit 5: {prose_count(u5)} words")

# ==============================================================================
# EXPAND UNIT 6 (Interval Estimation)
# ==============================================================================
u6_path = DRAFT_DIR / "unit-6.md"
u6 = u6_path.read_text(encoding="utf-8")

u6_add_paired = """
### Paired-Sample Inferences and Matched-Pairs Design
In many experimental settings, observations in two groups are not independent, but intrinsically linked. For example, in a medical study of an antihypertensive compound, systolic blood pressure is recorded on the same $n$ patients before treatment ($X_i$) and after treatment ($Y_i$).
Because observations $(X_i, Y_i)$ are coupled on the same subject, they exhibit positive correlation $\\text{Cov}(X_i, Y_i) = \\rho \\sigma_X \\sigma_Y > 0$.
Applying a naive two-sample independent pooled $t$-interval would be catastrophic: the variance of the difference under independence is $\\frac{\\sigma_X^2 + \\sigma_Y^2}{n}$, whereas the true variance of the pairwise difference is:

$$\\text{Var}(X_i - Y_i) = \\sigma_X^2 + \\sigma_Y^2 - 2 \\rho \\sigma_X \\sigma_Y < \\sigma_X^2 + \\sigma_Y^2$$

To exploit this variance reduction, we define the univariate difference series:

$$D_i = X_i - Y_i, \\quad i = 1, 2, \\dots, n$$

Assuming $D_i \\stackrel{\\text{i.i.d.}}{\\sim} \\mathcal{N}(\\mu_D, \\sigma_D^2)$ where $\\mu_D = \\mu_X - \\mu_Y$, the problem reduces to a single-sample Student's $t$ inference on the differences:
- Sample mean difference: $\\bar{D} = \\frac{1}{n} \\sum_{i=1}^n D_i = \\bar{X} - \\bar{Y}$
- Sample standard deviation of differences: $S_D = \\sqrt{\\frac{1}{n-1} \\sum_{i=1}^n (D_i - \\bar{D})^2}$

The exact $100(1 - \\alpha)\\%$ paired $t$ confidence interval for $\\mu_D$ is:

$$\\left[ \\bar{D} - t_{n-1, 1 - \\alpha/2} \\frac{S_D}{\\sqrt{n}}, \\quad \\bar{D} + t_{n-1, 1 - \\alpha/2} \\frac{S_D}{\\sqrt{n}} \\right]$$

By subtracting out subject-specific baseline variability, the matched-pairs design dramatically narrows the confidence interval, yielding immense statistical power.
"""

u6_add_fieller = """
### Fieller's Theorem for the Ratio of Two Normal Means
A notoriously difficult problem in bioassay, pharmacokinetics, and econometrics is estimating the ratio of two population means:

$$\\theta = \\frac{\\mu_1}{\\mu_2}$$

for example, the relative potency of two pharmaceutical formulations or the price elasticity of demand.
Let $(\\bar{X}_1, \\bar{X}_2)$ be sample means from bivariate normal data with known or estimated covariance matrix $\\text{Var}(\\bar{X}_1) = v_{11}$, $\\text{Var}(\\bar{X}_2) = v_{22}$, and $\\text{Cov}(\\bar{X}_1, \\bar{X}_2) = v_{12}$.
A naive plug-in estimator $\\hat{\\theta} = \\bar{X}_1 / \\bar{X}_2$ has a Cauchy-like heavy-tailed distribution with infinite mean and infinite variance!
E. C. Fieller (1940, 1954) resolved this problem by constructing an exact linear pivot. Consider the auxiliary quantity:

$$Y(\\theta) = \\bar{X}_1 - \\theta \\bar{X}_2$$

Notice that $\\mathbb{E}[Y(\\theta)] = \\mu_1 - \\theta \\mu_2 = \\mu_1 - \\left( \\frac{\\mu_1}{\\mu_2} \\right) \\mu_2 = 0$.
The variance of $Y(\\theta)$ is:

$$v(\\theta) = \\text{Var}(Y(\\theta)) = v_{11} - 2 \\theta v_{12} + \\theta^2 v_{22}$$

The standardized statistic follows an exact Student's $t$ (or standard normal) distribution:

$$T(\\theta) = \\frac{\\bar{X}_1 - \\theta \\bar{X}_2}{\\sqrt{v_{11} - 2 \\theta v_{12} + \\theta^2 v_{22}}} \\sim t_\\nu$$

Inverting $T(\\theta)^2 \\le t_{\\nu, 1-\\alpha/2}^2 = t^2$ produces a quadratic inequality in $\\theta$:

$$(\\bar{X}_1 - \\theta \\bar{X}_2)^2 \\le t^2 (v_{11} - 2 \\theta v_{12} + \\theta^2 v_{22})$$

$$(\\bar{X}_2^2 - t^2 v_{22}) \\theta^2 - 2(\\bar{X}_1 \\bar{X}_2 - t^2 v_{12}) \\theta + (\\bar{X}_1^2 - t^2 v_{11}) \\le 0$$

Let $A = \\bar{X}_2^2 - t^2 v_{22}$, $B = \\bar{X}_1 \\bar{X}_2 - t^2 v_{12}$, and $C = \\bar{X}_1^2 - t^2 v_{11}$.
Depending on whether $A > 0$ or $A \\le 0$, Fieller's theorem generates three distinct geometric topologies:
1. **Bounded Interval ($A > 0$)**: If the denominator $\\bar{X}_2$ is significantly different from zero at level $\\alpha$ ($t_{\\text{denom}}^2 = \\bar{X}_2^2 / v_{22} > t^2$), the parabola opens upward, yielding a standard finite confidence interval:
   $$\\left[ \\frac{B - \\sqrt{B^2 - AC}}{A}, \\quad \\frac{B + \\sqrt{B^2 - AC}}{A} \\right]$$
2. **Complement of an Interval ($A < 0, B^2 - AC > 0$)**: If the denominator is not significantly different from zero, the confidence set is the union of two unbounded rays $(-\\infty, \\theta_1] \\cup [\\theta_2, \\infty)$.
3. **The Entire Real Line ($A < 0, B^2 - AC < 0$)**: If neither the numerator nor denominator is distinguishable from zero, the confidence set is $(-\\infty, \\infty)$.
Fieller's theorem demonstrates that demanding guaranteed frequentist coverage for non-linear ratios inherently requires accepting unbounded confidence sets when data carry insufficient information.
"""

u6_add_tolerance = """
### Tolerance Intervals and Prediction Intervals vs Confidence Intervals
Practitioners frequently confuse three distinct statistical interval concepts:
1. **Confidence Interval for a Parameter $\\theta$**: Brackets an unobserved, fixed parameter of the population (such as the mean $\\mu$):
   $$\\mathbb{P}\\left( L(\\mathbf{X}) \\le \\mu \\le U(\\mathbf{X}) \\right) = 1 - \\alpha$$
   As $n \\to \\infty$, the length of a confidence interval shrinks to zero: $\\mathcal{O}(1/\\sqrt{n}) \\to 0$.
2. **Prediction Interval for a Future Observation $X_{n+1}$**: Brackets a single future random realization drawn from the same population:
   $$\\mathbb{P}\\left( L(\\mathbf{X}) \\le X_{n+1} \\le U(\\mathbf{X}) \\right) = 1 - \\alpha$$
   For a normal population, the prediction error is $X_{n+1} - \\bar{X} \\sim \\mathcal{N}\\left(0, \\sigma^2(1 + 1/n)\\right)$. The exact prediction interval is:
   $$\\bar{X} \\pm t_{n-1, 1 - \\alpha/2} S \\sqrt{1 + \\frac{1}{n}}$$
   As $n \\to \\infty$, the prediction interval does **not** shrink to zero! Its width converges to the population spread $2 z_{1 - \\alpha/2} \\sigma$.
3. **Statistical Tolerance Interval**: Brackets a specified proportion $\\gamma$ (e.g., $99\\%$) of the entire population with a pre-assigned confidence level $1 - \\alpha$ (e.g., $95\\%$):
   $$\\mathbb{P}_{\\mathbf{X}}\\left( \\int_{L(\\mathbf{X})}^{U(\\mathbf{X})} f(x) \\, dx \\ge \\gamma \\right) = 1 - \\alpha$$
   In industrial manufacturing, tolerance intervals ensure that at least $99\\%$ of manufactured ball bearings meet dimensional specifications with $95\\%$ statistical confidence.
"""

u6 = u6.replace("## 6.5 Exact Confidence Intervals for the Normal Variance", u6_add_paired + "\n## 6.5 Exact Confidence Intervals for the Normal Variance")
u6 = u6.replace("## 6.8 Ratio of Two Normal Variances", u6_add_fieller + "\n## 6.8 Ratio of Two Normal Variances")
u6 = u6.replace("## 6.10 Inverting Exact Hypothesis Tests", u6_add_tolerance + "\n## 6.10 Inverting Exact Hypothesis Tests")
u6_path.write_text(u6, encoding="utf-8")
print(f"Updated Unit 6: {prose_count(u6)} words")

# ==============================================================================
# EXPAND UNIT 7 (Asymptotic Intervals)
# ==============================================================================
u7_path = DRAFT_DIR / "unit-7.md"
u7 = u7_path.read_text(encoding="utf-8")

u7_add_edgeworth = """
### Edgeworth Expansions and Cornish–Fisher Asymptotic Inversions
The Central Limit Theorem guarantees that the standardized studentized statistic $T_n = \\frac{\\sqrt{n}(\\hat{\\theta} - \\theta)}{\\hat{\\sigma}}$ converges in distribution to $\\mathcal{N}(0, 1)$ at rate $\\mathcal{O}(1/\\sqrt{n})$:

$$F_n(x) = \\mathbb{P}(T_n \\le x) = \\Phi(x) + \\mathcal{O}\\left( \\frac{1}{\\sqrt{n}} \\right)$$

To achieve higher-order coverage accuracy, mathematical statisticians employ **Edgeworth Expansions**, which expand the true CDF $F_n(x)$ in terms of the Hermite polynomials $H_k(x)$ and population cumulants:

$$F_n(x) = \\Phi(x) - \\phi(x) \\left[ \\frac{\\kappa_3}{6\\sqrt{n}} H_2(x) + \\frac{\\kappa_4}{24n} H_3(x) + \\frac{\\kappa_3^2}{72n} H_5(x) + \\mathcal{O}\\left( \\frac{1}{n^{3/2}} \\right) \\right]$$

where $\\kappa_3 = \\frac{\\mathbb{E}[(X - \\mu)^3]}{\\sigma^3}$ is the skewness coefficient, and $H_2(x) = x^2 - 1$, $H_3(x) = x^3 - 3x$, $H_5(x) = x^5 - 10x^3 + 15x$.
Notice that the leading error term $-\\phi(x) \\frac{\\kappa_3}{6\\sqrt{n}} (x^2 - 1)$ is driven entirely by population **skewness**!
If the population is skewed ($\\kappa_3 \\ne 0$), the true distribution of $T_n$ is asymmetric, and a naive Gaussian interval $T_n \\pm z_{1 - \\alpha/2}$ experiences asymmetric tail coverage error of order $\\mathcal{O}(1/\\sqrt{n})$.
Inverting the Edgeworth expansion yields the **Cornish–Fisher Expansion** for the exact quantile $w_\\alpha$:

$$w_\\alpha = z_\\alpha + \\frac{\\kappa_3}{6\\sqrt{n}} (z_\\alpha^2 - 1) + \\frac{\\kappa_4}{24n} (z_\\alpha^3 - 3 z_\\alpha) - \\frac{\\kappa_3^2}{36n} (2 z_\\alpha^3 - 5 z_\\alpha) + \\mathcal{O}\\left( \\frac{1}{n^{3/2}} \\right)$$

Using Cornish–Fisher quantiles replaces the standard $z_{\\alpha}$ cutoffs with skewness-adjusted critical values, reducing interval coverage error from $\\mathcal{O}(1/\\sqrt{n})$ down to $\\mathcal{O}(1/n)$ (second-order accuracy).
"""

u7_add_contingency = """
### Asymptotic Confidence Intervals for Odds Ratios and Relative Risk in 2x2 Tables
In clinical epidemiology and medical genetics, the association between an exposure (or treatment) and a binary health outcome is summarized in a $2 \\times 2$ contingency table:

$$\\begin{array}{c|cc|c} & \\text{Outcome (+)} & \\text{Outcome (-)} & \\text{Total} \\\\ \\hline \\text{Exposed} & a & b & n_1 \\\\ \\text{Unexposed} & c & d & n_0 \\\\ \\hline \\text{Total} & m_1 & m_0 & N \\end{array}$$

Two primary metrics quantify the association:
1. **Relative Risk (Risk Ratio, RR)**:
   $$\\widehat{\\text{RR}} = \\frac{a / n_1}{c / n_0}$$
2. **Odds Ratio (OR)**:
   $$\\widehat{\\text{OR}} = \\frac{a / b}{c / d} = \\frac{a d}{b c}$$

Both $\\widehat{\\text{RR}}$ and $\\widehat{\\text{OR}}$ are strictly non-negative ratios whose sampling distributions are severely skewed to the right for small to moderate sample sizes. Direct Wald intervals on the raw ratios produce catastrophic under-coverage and can violate the non-negativity bound.
To achieve rapid Gaussian convergence, statisticians apply the **logarithmic transformation**:

$$\\psi = \\ln(\\widehat{\\text{OR}}) = \\ln(a) - \\ln(b) - \\ln(c) + \\ln(d)$$

By the Multivariate Delta Method, using the multinomial variance-covariance structure, the asymptotic standard error of the log-odds ratio is given by **Woolf's Formula** (1955):

$$\\text{SE}(\\ln \\widehat{\\text{OR}}) = \\sqrt{\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} + \\frac{1}{d}}$$

The asymptotic $100(1 - \\alpha)\\%$ confidence interval for $\\ln(\\text{OR})$ is:

$$\\ln(\\widehat{\\text{OR}}) \\pm z_{1 - \\alpha/2} \\sqrt{\\frac{1}{a} + \\frac{1}{b} + \\frac{1}{c} + \\frac{1}{d}}$$

Exponentiating both endpoints yields the exact multiplicative confidence interval for the Odds Ratio:

$$\\left[ \\widehat{\\text{OR}} \\cdot \\exp\\left( -z_{1 - \\alpha/2} \\, \\text{SE}(\\ln \\widehat{\\text{OR}}) \\right), \\quad \\widehat{\\text{OR}} \\cdot \\exp\\left( +z_{1 - \\alpha/2} \\, \\text{SE}(\\ln \\widehat{\\text{OR}}) \\right) \\right]$$

Similarly, for the Relative Risk, the standard error of $\\ln(\\widehat{\\text{RR}})$ is:

$$\\text{SE}(\\ln \\widehat{\\text{RR}}) = \\sqrt{\\frac{1}{a} - \\frac{1}{n_1} + \\frac{1}{c} - \\frac{1}{n_0}}$$

Exponentiating yields an asymmetric, range-preserving confidence interval for the Relative Risk that naturally respects the $(0, \\infty)$ domain.
"""

u7_add_woodruff = """
### Woodruff's Method for Nonparametric Quantile Confidence Intervals
In econometric surveys of household income and wealth, distributions are heavily skewed and Pareto-tailed, making mean estimation unstable. Policy analysts rely instead on population quantiles $\\xi_p = F^{-1}(p)$ (such as the median $\\xi_{0.5}$ or 90th percentile $\\xi_{0.9}$).
Ralph S. Woodruff (1952) established an ingenious, distribution-free method for constructing confidence intervals for any quantile $\\xi_p$ without requiring density estimation.
Let $\\hat{F}_n(t) = \\frac{1}{n} \\sum_{i=1}^n \\mathbf{1}_{\\{X_i \\le t\\}}$ be the empirical cumulative distribution function.
At the true quantile $\\xi_p$, the indicator $\\mathbf{1}_{\\{X_i \\le \\xi_p\\}}$ is a Bernoulli variable with success probability $p$. By the Central Limit Theorem:

$$\\hat{F}_n(\\xi_p) \\sim \\mathcal{A}\\mathcal{N}\\left( p, \\, \\frac{p(1 - p)}{n} \\right)$$

A $100(1 - \\alpha)\\%$ confidence interval for the probability value $p$ is:

$$[p_L, \\, p_U] = \\left[ p - z_{1 - \\alpha/2} \\sqrt{\\frac{p(1 - p)}{n}}, \\quad p + z_{1 - \\alpha/2} \\sqrt{\\frac{p(1 - p)}{n}} \\right]$$

Woodruff inverted this vertical probability interval horizontally through the sample quantile function $\\hat{F}_n^{-1}$:

$$\\left[ \\hat{\\xi}_{p_L}, \\, \\hat{\\xi}_{p_U} \\right] = \\left[ \\hat{F}_n^{-1}\\left( p - z_{1 - \\alpha/2} \\sqrt{\\frac{p(1 - p)}{n}} \\right), \\quad \\hat{F}_n^{-1}\\left( p + z_{1 - \\alpha/2} \\sqrt{\\frac{p(1 - p)}{n}} \\right) \\right]$$

For an ordered sample $X_{(1)} \\le X_{(2)} \\le \\dots \\le X_{(n)}$, the endpoints are simply the order statistics:

$$L = X_{(k_1)}, \\quad U = X_{(k_2)}$$

where the integer ranks are:

$$k_1 = \\left\\lfloor n p - z_{1 - \\alpha/2} \\sqrt{n p (1 - p)} \\right\\rfloor, \\quad k_2 = \\left\\lceil n p + z_{1 - \\alpha/2} \\sqrt{n p (1 - p)} \\right\\rceil$$

Woodruff's interval requires zero kernel density estimation, avoids bandwidth selection dilemmas, and guarantees exact non-parametric coverage across all continuous distribution shapes.
"""

u7 = u7.replace("## 7.2 The Wald Confidence Interval", u7_add_edgeworth + "\n## 7.2 The Wald Confidence Interval")
u7 = u7.replace("## 7.6 Asymptotic Confidence Intervals for Poisson Arrival Rates", u7_add_contingency + "\n## 7.6 Asymptotic Confidence Intervals for Poisson Arrival Rates")
u7 = u7.replace("## 7.8 Nonparametric Bootstrap Confidence Intervals", u7_add_woodruff + "\n## 7.8 Nonparametric Bootstrap Confidence Intervals")
u7_path.write_text(u7, encoding="utf-8")
print(f"Updated Unit 7: {prose_count(u7)} words")

# ==============================================================================
# EXPAND UNIT 8 (Bayesian Inference)
# ==============================================================================
u8_path = DRAFT_DIR / "unit-8.md"
u8 = u8_path.read_text(encoding="utf-8")

u8_add_reference = """
### Bernardo's Objective Reference Priors in Multiparameter Models
While Jeffreys' prior $\\pi_J(\\boldsymbol{\\theta}) \\propto \\sqrt{\\det(\\mathbf{I}(\\boldsymbol{\\theta}))}$ works exquisitely in single-parameter problems, it can fail catastrophically in multiparameter settings.
In a famous counterexample, Charles Stein considered the normal model:

$$X_i \\sim \\mathcal{N}(\\mu_i, \\sigma^2), \\quad i = 1, 2, \\dots, p$$

where the parameter of interest is the squared length $\\eta = \\sum_{i=1}^p \\mu_i^2$.
Evaluating Jeffreys' joint prior yields $\\pi_J(\\mu_1, \\dots, \\mu_p, \\sigma) \\propto \\sigma^{-(p+1)}$. When $p$ is large (e.g., $p = 50$), the posterior distribution for $\\eta$ suffers from severe marginalization paradoxes, producing posterior credible intervals that are systematically shifted away from the true parameter value.
To overcome this defect, José-Miguel Bernardo (1979), with further developments by James Berger, formulated the theory of **Reference Priors**.
Instead of treating all parameters symmetrically, reference analysis partitions the parameters into ordered groups:

$$\\boldsymbol{\\theta} = (\\theta_1, \\theta_2, \\dots, \\theta_k)$$

where $\\theta_1$ is the primary parameter of interest and $\\theta_2, \\dots, \\theta_k$ are nuisance parameters.
The reference prior is derived by maximizing the expected Kullback–Leibler divergence (Shannon mutual information) between the prior and the posterior distribution:

$$\\pi_R(\\boldsymbol{\\theta}) = \\arg\\max_\\pi \\lim_{k \\to \\infty} \\frac{1}{k} I(\\boldsymbol{\\theta}; \\mathbf{X}^{(k)})$$

subject to a sequence of compact nested subsets. By maximizing information flow sequentially from data to parameter, Bernardo's reference algorithm eliminates marginalization paradoxes and produces objective Bayesian credible intervals that achieve exact frequentist coverage to higher orders of asymptotic approximation.
"""

u8_add_linex = """
### Asymmetric Loss Functions: The LINEX Loss Model
In engineering risk analysis and financial portfolio management, the consequences of overestimation and underestimation are rarely symmetric. For example:
- In dam design, underestimating the 100-year flood level leads to catastrophic structural overtopping and loss of life. Overestimating the flood level merely leads to modest financial expenditure in building a higher concrete wall.
- In pharmaceutical manufacturing, underestimating toxic contaminant concentrations is fatal; overestimating causes harmless batch scrapping.
To accommodate directional penalties, Varian (1975) introduced the **Linear-Exponential (LINEX) Loss Function**:

$$L(\\Delta) = b \\left[ e^{a \\Delta} - a \\Delta - 1 \\right], \\quad a \\ne 0, \\, b > 0$$

where $\\Delta = \\hat{\\theta} - \\theta$ is the estimation error.
Notice the behavior of the LINEX loss:
- If $a > 0$, an overestimation error ($\Delta > 0$) causes exponential penalty growth $e^{a \\Delta}$, while an underestimation error ($\Delta < 0$) causes only linear penalty growth $-a \\Delta$.
- If $a < 0$, underestimation is penalized exponentially.
- As $a \\to 0$, Taylor expanding $e^{a \\Delta} = 1 + a \\Delta + \\frac{a^2 \\Delta^2}{2} + \\mathcal{O}(a^3)$ shows that $L(\\Delta) \\approx \\frac{b a^2}{2} \\Delta^2$, which reproduces standard squared error loss.

### Theorem: The Optimal Bayes Estimator under LINEX Loss
The posterior expected loss is:

$$\\rho(a, \\mathbf{x}) = b \\, \\mathbb{E}_{\\theta \\mid \\mathbf{x}}[e^{a(a - \\theta)}] - a b (a - \\mathbb{E}[\\theta \\mid \\mathbf{x}]) - b$$

Differentiating with respect to $a$ and setting to zero:

$$\\frac{d\\rho}{da} = a b \\, e^{a a} \\mathbb{E}[e^{-a \\theta} \\mid \\mathbf{x}] - a b = 0 \\implies e^{a a} \\mathbb{E}[e^{-a \\theta} \\mid \\mathbf{x}] = 1$$

Taking the natural logarithm on both sides:

$$a a + \\ln \\mathbb{E}[e^{-a \\theta} \\mid \\mathbf{x}] = 0$$

Solving for the optimal point estimate $\\hat{\\theta}_{\\text{LINEX}}$:

$$\\hat{\\theta}_{\\text{LINEX}} = -\\frac{1}{a} \\ln \\mathbb{E}_{\\theta \\mid \\mathbf{x}}\\left[ e^{-a \\theta} \\right]$$

Notice the extraordinary analytical beauty of this result: $\\mathbb{E}[e^{-a \\theta} \\mid \\mathbf{x}] = M_{\\theta \\mid \\mathbf{x}}(-a)$ is precisely the **Moment Generating Function of the posterior distribution** evaluated at $-a$!
If the posterior distribution is Gaussian $\\theta \\mid \\mathbf{x} \\sim \\mathcal{N}(\\mu_n, \\sigma_n^2)$, its MGF is $M(-a) = \\exp\\left( -a \\mu_n + \\frac{a^2 \\sigma_n^2}{2} \\right)$.
Substituting this into the LINEX formula:

$$\\hat{\\theta}_{\\text{LINEX}} = -\\frac{1}{a} \\left( -a \\mu_n + \\frac{a^2 \\sigma_n^2}{2} \\right) = \\mu_n - \\frac{a}{2} \\sigma_n^2$$

The optimal estimate is the posterior mean $\\mu_n$ shifted by an exact risk premium $\\frac{a}{2} \\sigma_n^2$ proportional to the posterior variance! If underestimation is dangerous ($a < 0$), the estimator automatically shifts upward by $\\frac{|a|}{2} \\sigma_n^2$ to safeguard against failure.
"""

u8_add_mcmc_diag = """
### MCMC Convergence Diagnostics: Gelman-Rubin $\\hat{R}$ and Effective Sample Size
When executing MCMC sampling (such as Metropolis–Hastings or Gibbs sampling), the generated Markov chain requires an initial burn-in phase to reach its stationary distribution. Furthermore, successive MCMC draws are autocorrelated rather than independent.
Statisticians deploy two essential convergence diagnostics:

#### 1. The Gelman–Rubin Potential Scale Reduction Factor ($\\hat{R}$)
Andrew Gelman and Donald Rubin (1992) proposed running $M \\ge 3$ independent parallel chains starting from dispersed initial values.
Let $N$ denote the number of iterations per chain after discarding burn-in.
- Calculate the between-chain variance $B$:
  $$B = \\frac{N}{M - 1} \\sum_{m=1}^M (\\bar{\\theta}_m - \\bar{\\theta}_{\\cdot\\cdot})^2$$
- Calculate the average within-chain variance $W$:
  $$W = \\frac{1}{M} \\sum_{m=1}^M s_m^2 = \\frac{1}{M(N - 1)} \\sum_{m=1}^M \\sum_{t=1}^N (\\theta_{mt} - \\bar{\\theta}_m)^2$$
- The pooled marginal posterior variance estimate is:
  $$\\widehat{\\text{Var}}(\\theta \\mid \\mathbf{x}) = \\frac{N - 1}{N} W + \\frac{1}{N} B$$
The potential scale reduction factor is:
$$\\hat{R} = \\sqrt{ \\frac{\\widehat{\\text{Var}}(\\theta \\mid \\mathbf{x})}{W} }$$
If the chains have mixed and converged to the target distribution, between-chain variance matches within-chain variance, so $\\hat{R} \\approx 1.0$. In modern Bayesian practice, convergence is diagnosed only when $\\hat{R} < 1.05$ across all monitored parameters.

#### 2. Effective Sample Size (ESS)
Due to positive autocorrelation $\\rho_k$ between successive iterations, $N$ dependent MCMC draws contain less information than $N$ independent draws.
The integrated autocorrelation time is:
$$\\tau = 1 + 2 \\sum_{k=1}^\\infty \\rho_k$$
The **Effective Sample Size (ESS)** is:
$$\\text{ESS} = \\frac{N}{\\tau} = \\frac{N}{1 + 2 \\sum_{k=1}^\\infty \\rho_k}$$
The ESS quantifies the equivalent number of independent Monte Carlo samples generated by the chain. For reliable posterior credible intervals, practitioners demand $\\text{ESS} \\ge 1,000$.
"""

u8 = u8.replace("## 8.3 Conjugate Prior Distributions", u8_add_reference + "\n## 8.3 Conjugate Prior Distributions")
u8 = u8.replace("## 8.6 Bayesian Credible Intervals", u8_add_linex + "\n## 8.6 Bayesian Credible Intervals")
u8 = u8.replace("## 8.10 Decision-Theoretic Admissibility", u8_add_mcmc_diag + "\n## 8.10 Decision-Theoretic Admissibility")
u8_path.write_text(u8, encoding="utf-8")
print(f"Updated Unit 8: {prose_count(u8)} words")
