from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-statistical-research-methods"

# ==============================================================================
# UNIT 5
# ==============================================================================
u5_content = r"""# Unit 5: Statistical Power Analysis, Effect Size Estimation & Sample Size Determination

In empirical research, an experiment or clinical trial must be designed with sufficient statistical precision to detect meaningful scientific effects if they exist. Conducting a study with inadequate statistical power is not merely a waste of financial and logistical resources; it is an ethical violation that exposes human or animal subjects to experimental risks while possessing negligible probability of yielding conclusive scientific insights. As Jacob Cohen established in his foundational 1969 treatise *Statistical Power Analysis for the Behavioral Sciences*: *"A study with low statistical power is an intellectual lottery in which the investigator has paid full price for a ticket that cannot win."*

Statistical power analysis formalizes the mathematical relationship linking four core elements of statistical inference: the significance criterion ($\alpha$), the statistical power ($1 - \beta$), the sample size ($n$), and the population effect size ($\mathbf{E}$). This unit examines the decision-theoretic framework of hypothesis testing, derives the properties of non-central sampling distributions, details standardized effect size metrics, establishes closed-form sample size determination formulas across major experimental designs, and exposes the mathematical invalidity of post-hoc retrospective power.

## 5.1 The Decision-Theoretic Framework of Statistical Testing: $\alpha$, $\beta$, and Power
In the Neyman-Pearson decision-theoretic paradigm, statistical hypothesis testing is framed as an inductive decision rule partitioning the sample space $\mathcal{X}$ into an acceptance region $\mathcal{A}$ and a critical rejection region $\mathcal{R}$. The decision rule must adjudicate between two mutually exclusive states of nature: the null hypothesis $H_0$ and the alternative hypothesis $H_1$.

This decision framework produces four possible outcomes:
1. True Negative (Correct Retention): Nature is in state $H_0$, and the decision rule retains $H_0$. The probability of this correct decision is $1 - \alpha$.
2. False Positive (Type I Error, $\alpha$): Nature is in state $H_0$, but sample data fall into the critical rejection region $\mathcal{R}$, leading to the erroneous rejection of a true null hypothesis. The probability is the significance level:
$$\alpha = P(\mathbf{X} \in \mathcal{R} \mid H_0)$$
3. False Negative (Type II Error, $\beta$): Nature is in state $H_1$ (a true effect exists), but sample data fall into the acceptance region $\mathcal{A}$, leading to the erroneous failure to reject a false null hypothesis:
$$\beta = P(\mathbf{X} \in \mathcal{A} \mid H_1)$$
4. True Positive (Statistical Power, $1 - \beta$): Nature is in state $H_1$, and the decision rule correctly rejects $H_0$:
$$\text{Power} = 1 - \beta = P(\mathbf{X} \in \mathcal{R} \mid H_1)$$

Statistical power represents the sensitivity of an experiment: the probability that the study will detect a true population effect of a specified magnitude at a chosen significance threshold $\alpha$. By convention in biomedical and behavioral sciences, researchers set the nominal Type I error rate to $\alpha = 0.05$ and demand a minimum statistical power of $1 - \beta = 0.80$ (corresponding to a Type II error rate of $\beta = 0.20$). Under this $4:1$ convention, researchers tacitly deem a false positive (Type I error) to be four times more damaging to scientific progress than a false negative (Type II error).

## 5.2 Non-Central Sampling Distributions: Non-Central $t$, $F$, and $\chi^2$
In introductory statistical courses, hypothesis tests are typically derived under the central null hypothesis $H_0$, where test statistics follow standard central distributions: Student's $t$, Snedecor's $F$, or Fisher's $\chi^2$.
However, calculating statistical power requires determining the probability of rejecting $H_0$ under the *alternative* hypothesis $H_1$. Under $H_1$, test statistics do not follow central distributions; they follow non-central distributions governed by a non-centrality parameter (NCP).

### 1. The Non-Central Student's $t$-Distribution:
Let $Z \sim \mathcal{N}(\delta, 1)$ be a normally distributed random variable with non-zero mean $\delta$, and let $V \sim \chi_\nu^2$ be an independent central chi-square variable with $\nu$ degrees of freedom. The ratio:
$$T' = \frac{Z}{\sqrt{V / \nu}} \sim t_\nu(\delta)$$
follows a non-central $t$-distribution with $\nu$ degrees of freedom and non-centrality parameter $\delta$.
For a two-sample Student's $t$-test comparing two independent groups of size $n_1$ and $n_2$ with true population means $\mu_1, \mu_2$ and pooled variance $\sigma^2$:
$$\delta = \frac{\mu_1 - \mu_2}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} = d \sqrt{\frac{n_1 n_2}{n_1 + n_2}}$$
where $d = (\mu_1 - \mu_2)/\sigma$ is Cohen's standardized effect size. When $n_1 = n_2 = n$:
$$\delta = d \sqrt{\frac{n}{2}}$$
The statistical power for a two-tailed test at significance level $\alpha$ is:
$$\text{Power} = 1 - \beta = P(T' \ge t_{\nu, 1 - \alpha/2} \mid \delta) + P(T' \le -t_{\nu, 1 - \alpha/2} \mid \delta)$$
where $t_{\nu, 1 - \alpha/2}$ is the critical value from the central $t$-distribution.

### 2. The Non-Central $F$-Distribution:
Let $U \sim \chi_{\nu_1}^2(\lambda)$ be a non-central chi-square variable with non-centrality parameter $\lambda$, and let $W \sim \chi_{\nu_2}^2$ be an independent central chi-square variable. The ratio:
$$F' = \frac{U / \nu_1}{W / \nu_2} \sim F_{\nu_1, \nu_2}(\lambda)$$
follows a non-central $F$-distribution. In one-way Analysis of Variance (ANOVA) across $k$ groups with sample sizes $n$ per group:
$$\lambda = n \sum_{j=1}^k \frac{(\mu_j - \bar{\mu})^2}{\sigma^2} = N f^2$$
where $f = \sigma_\mu / \sigma$ is Cohen's effect size for ANOVA, and $N = k n$.

### 3. The Non-Central $\chi^2$-Distribution:
If $X_j \sim \mathcal{N}(\mu_j, 1)$ are independent normal variables for $j = 1, \dots, \nu$, the sum of their squares:
$$Q = \sum_{j=1}^\nu X_j^2 \sim \chi_\nu^2(\lambda)$$
follows a non-central chi-square distribution with $\nu$ degrees of freedom and non-centrality parameter $\lambda = \sum_{j=1}^\nu \mu_j^2$.

## 5.3 Standardized Effect Sizes: Cohen's $d$, Hedges' $g$, $r$, $f^2$, and Odds Ratios
An effect size is a quantitative index reflecting the magnitude and direction of a relationship or treatment effect in a population, independent of sample size. While raw effect sizes (e.g., a blood pressure reduction of $8.4\text{ mmHg}$) are interpretable in established measurement units, comparing effects across diverse instruments requires standardized effect sizes:

1. Cohen's $d$ (Standardized Mean Difference):
   For two independent groups:
   $$d = \frac{\bar{Y}_1 - \bar{Y}_2}{s_{\text{pooled}}}$$
   where the pooled sample standard deviation is:
   $$s_{\text{pooled}} = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}$$
   Cohen's qualitative benchmarks: $d = 0.20$ (Small), $d = 0.50$ (Medium), $d = 0.80$ (Large).
2. Hedges' $g$ (Unbiased Standardized Mean Difference):
   In small samples ($N < 30$), Cohen's $d$ exhibits a slight positive sample bias. Larry Hedges (1981) derived the exact small-sample correction factor $J(\nu)$:
   $$g = J(\nu) \cdot d = \left[ 1 - \frac{3}{4\nu - 1} \right] d$$
   where $\nu = n_1 + n_2 - 2$ is degrees of freedom. Hedges' $g$ is an strictly unbiased estimator of the population standardized mean difference.
3. Pearson's Correlation Coefficient ($r$):
   Measures the linear association between continuous variables ($r \in [-1, 1]$). Cohen's benchmarks: $r = 0.10$ (Small), $r = 0.30$ (Medium), $r = 0.50$ (Large).
4. Cohen's $f^2$ for Multiple Regression:
   For evaluating the overall explanatory power of a regression model with $k$ predictors:
   $$f^2 = \frac{R^2}{1 - R^2}$$
   For evaluating the unique incremental contribution of a subset of $u$ test predictors after controlling for $k_1$ base covariates:
   $$f^2 = \frac{R_{\text{full}}^2 - R_{\text{reduced}}^2}{1 - R_{\text{full}}^2}$$
   Cohen's benchmarks: $f^2 = 0.02$ (Small), $f^2 = 0.15$ (Medium), $f^2 = 0.35$ (Large).
5. Odds Ratio ($\mathrm{OR}$) and Risk Ratio ($\mathrm{RR}$):
   For binary $2 \times 2$ contingency tables:
   $$\mathrm{OR} = \frac{p_1 / (1 - p_1)}{p_2 / (1 - p_2)} = \frac{a \cdot d}{b \cdot c}$$
   The log odds ratio maps to Cohen's $d$ via the logistic distribution transformation: $d \approx \frac{\ln(\mathrm{OR}) \sqrt{3}}{\pi} \approx \frac{\ln(\mathrm{OR})}{1.81}$.

## 5.4 Analytical Sample Size Determination Formulas
For standard experimental designs, closed-form asymptotic sample size formulas can be derived directly from the normal approximation:

### Two-Sample Independent $t$-Test:
To detect a standardized mean difference $d$ with two-tailed significance $\alpha$ and power $1 - \beta$ in balanced groups ($n_1 = n_2 = n$):
$$n = \frac{2 (z_{\alpha/2} + z_\beta)^2}{d^2}$$
where $z_{\alpha/2}$ and $z_\beta$ are upper quantiles of the standard normal distribution:
- For $\alpha = 0.05$ (two-tailed), $z_{0.025} = 1.960$.
- For Power $= 0.80$ ($\beta = 0.20$), $z_{0.20} = 0.8416$.
- $(z_{\alpha/2} + z_\beta)^2 = (1.960 + 0.8416)^2 = (2.8016)^2 \approx 7.849$.
- For Power $= 0.90$ ($\beta = 0.10$), $z_{0.10} = 1.2816 \implies (1.960 + 1.2816)^2 = (3.2416)^2 \approx 10.508$.

Thus, for $\alpha = 0.05$ and $80\%$ power:
$$n \approx \frac{2 \times 7.849}{d^2} = \frac{15.70}{d^2} \text{ subjects per group}$$
For a medium effect size $d = 0.50$:
$$n \approx \frac{15.70}{(0.50)^2} = \frac{15.70}{0.25} = 62.8 \implies 63 \text{ subjects per group } (N = 126 \text{ total})$$

### Test of Two Independent Proportions:
To detect a difference between proportions $p_1$ and $p_2$ with pooled proportion $\bar{p} = (p_1 + p_2)/2$:
$$n = \frac{\left[ z_{\alpha/2} \sqrt{2 \bar{p}(1 - \bar{p})} + z_\beta \sqrt{p_1(1 - p_1) + p_2(1 - p_2)} \right]^2}{(p_1 - p_2)^2}$$

## 5.5 Worked Problem Examples

### Fully worked question 1: Two-Sample $t$-Test Sample Size and Non-Centrality Parameter
A clinical pharmacology trial investigates a novel antihypertensive drug designed to reduce systolic blood pressure.
Cardiological benchmarks specify:
- Baseline systolic standard deviation $\sigma = 16.0\text{ mmHg}$.
- Minimal clinically meaningful reduction $\Delta = \mu_{\text{placebo}} - \mu_{\text{drug}} = 8.0\text{ mmHg}$.
- Two-tailed significance level $\alpha = 0.05$ ($z_{0.025} = 1.960$).
- Target statistical power $1 - \beta = 0.90$ ($z_{0.10} = 1.282$).

1. Compute Cohen's standardized effect size $d$.
2. Calculate the required sample size per group $n$ using the closed-form normal approximation, and determine total trial sample size $N$.
3. Compute the exact non-centrality parameter $\delta$ for the non-central $t$-distribution under this design, and evaluate the non-central $t$ power guarantee.

### Solution, step 1: Compute Cohen's Standardized Effect Size $d$
The standardized effect size is:
$$d = \frac{\Delta}{\sigma} = \frac{8.0\text{ mmHg}}{16.0\text{ mmHg}} = \mathbf{0.500}$$
The clinical reduction corresponds exactly to a medium effect size of $d = 0.50$.

### Solution, step 2: Calculate Required Sample Size per Group
Using the closed-form sample size formula for balanced independent groups:
$$n = \frac{2 (z_{\alpha/2} + z_\beta)^2}{d^2}$$
Substitute $z_{0.025} = 1.960$, $z_{0.10} = 1.282$, and $d = 0.50$:
$$z_{\alpha/2} + z_\beta = 1.960 + 1.282 = 3.242$$
$$(z_{\alpha/2} + z_\beta)^2 = (3.242)^2 = 10.5106$$
$$n = \frac{2 \times 10.5106}{(0.50)^2} = \frac{21.0212}{0.25} = 84.08 \implies \mathbf{85 \text{ patients per group}}$$
Total trial sample size across both arms is:
$$N = 2n = 2 \times 85 = \mathbf{170 \text{ patients}}$$
The trial requires $85$ patients in the active drug arm and $85$ in the placebo arm.

### Solution, step 3: Compute Non-Centrality Parameter $\delta$ and Exact Degrees of Freedom
For balanced groups of size $n = 85$:
Degrees of freedom:
$$\nu = n_1 + n_2 - 2 = 85 + 85 - 2 = \mathbf{168}$$
The exact non-centrality parameter $\delta$ is:
$$\delta = d \sqrt{\frac{n}{2}} = 0.50 \times \sqrt{\frac{85}{2}} = 0.50 \times \sqrt{42.5} = 0.50 \times 6.5192 = \mathbf{3.2596}$$
The critical threshold from the central $t$-distribution with $\nu = 168$ at $\alpha = 0.05$ is $t_{168, 0.975} = 1.974$.
Under the non-central distribution $T' \sim t_{168}(\delta = 3.2596)$:
$$\text{Power} = P(T' \ge 1.974) \approx \Phi(\delta - t_{\text{crit}}) = \Phi(3.2596 - 1.974) = \Phi(1.2856) \approx \mathbf{0.9007} \quad (90.07\%)$$
The exact non-central $t$-calculation confirms that $n = 85$ per arm guarantees $90.1\%$ power.

---

### Fully worked question 2: Hedges' $g$ Unbiased Effect Size Correction
A cognitive neuroscience laboratory conducts an fMRI study testing neural activation in a rare patient cohort:
- Clinical group: $n_1 = 12$ patients, mean activation $\bar{y}_1 = 4.80$, sample variance $s_1^2 = 1.44$.
- Healthy control group: $n_2 = 12$ controls, mean activation $\bar{y}_2 = 3.60$, sample variance $s_2^2 = 1.00$.

1. Compute the pooled sample standard deviation $s_{\text{pooled}}$ and Cohen's sample effect size $d$.
2. Calculate Hedges' small-sample correction factor $J(\nu)$ and compute the unbiased effect size Hedges' $g$.
3. Compute the large-sample asymptotic variance of Hedges' $g$ and construct its $95\%$ confidence interval.

### Solution, step 1: Compute Pooled Standard Deviation and Cohen's $d$
The pooled variance for equal sample sizes $n_1 = n_2 = 12$ is the arithmetic mean of the variances:
$$s_{\text{pooled}}^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2} = \frac{11(1.44) + 11(1.00)}{22} = \frac{1.44 + 1.00}{2} = 1.22$$
$$s_{\text{pooled}} = \sqrt{1.22} \approx 1.1045$$
Compute Cohen's $d$:
$$d = \frac{\bar{y}_1 - \bar{y}_2}{s_{\text{pooled}}} = \frac{4.80 - 3.60}{1.1045} = \frac{1.20}{1.1045} \approx \mathbf{1.0864}$$

### Solution, step 2: Compute Hedges' Correction Factor $J(\nu)$ and Hedges' $g$
Degrees of freedom is $\nu = n_1 + n_2 - 2 = 12 + 12 - 2 = 22$.
Larry Hedges' small-sample polynomial approximation for $J(\nu)$ is:
$$J(\nu) = 1 - \frac{3}{4\nu - 1}$$
Substitute $\nu = 22$:
$$4\nu - 1 = 4(22) - 1 = 88 - 1 = 87$$
$$J(22) = 1 - \frac{3}{87} = 1 - 0.03448 = \mathbf{0.96552}$$
In small samples ($N = 24$), Cohen's $d$ overestimates the true population effect size by approximately $3.5\%$.
Compute Hedges' $g$:
$$g = J(\nu) \times d = 0.96552 \times 1.0864 \approx \mathbf{1.0489}$$
The unbiased estimate of the standardized mean difference is Hedges' $g = 1.049$.

### Solution, step 3: Compute Asymptotic Variance and $95\%$ Confidence Interval
The asymptotic sampling variance of Hedges' $g$ is:
$$\mathrm{Var}(g) \approx \frac{n_1 + n_2}{n_1 n_2} + \frac{g^2}{2(n_1 + n_2)}$$
Substitute $n_1 = 12, n_2 = 12$, and $g = 1.0489$:
$$\frac{n_1 + n_2}{n_1 n_2} = \frac{24}{144} = \frac{1}{6} \approx 0.16667$$
$$\frac{g^2}{2(n_1 + n_2)} = \frac{(1.0489)^2}{2(24)} = \frac{1.1002}{48} \approx 0.02292$$
$$\mathrm{Var}(g) \approx 0.16667 + 0.02292 = 0.18959$$
The standard error is:
$$\mathrm{SE}(g) = \sqrt{0.18959} \approx \mathbf{0.4354}$$
Compute the $95\%$ confidence interval using $z_{0.025} = 1.960$:
$$\mathrm{CI}_{95\%} = 1.0489 \pm 1.960 \times 0.4354 = 1.0489 \pm 0.8534 \implies [\mathbf{0.195}, \; \mathbf{1.902}]$$
Although the point estimate is large ($g = 1.05$), the small sample size ($N = 24$) produces a wide confidence interval spanning from $0.20$ (small effect) to $1.90$ (massive effect).

---

### Fully worked question 3: Multiple Regression Power and Incremental $R^2$ via Cohen's $f^2$
An organizational psychologist tests whether three executive leadership personality traits ($u = 3$ test predictors) explain incremental variance in corporate innovation performance, after controlling for four established firm covariates: firm size, industry sector, R&D budget, and firm age ($k_1 = 4$ control covariates).
- Base Model ($k_1 = 4$): Explains $R_{\text{base}}^2 = 0.250$ of innovation variance.
- Anticipated Full Model ($k = k_1 + u = 7$): Explains $R_{\text{full}}^2 = 0.320$ (an incremental variance of $\Delta R^2 = 0.320 - 0.250 = 0.070$).
- Desired statistical power is $1 - \beta = 0.80$ at significance level $\alpha = 0.05$.

1. Formulate Cohen's effect size $f^2$ for the incremental variance test.
2. Determine the required total sample size $N$ of corporate firms using the $F$-test non-centrality framework.
3. Compute the numerator and denominator degrees of freedom for the incremental $F$-test under the calculated sample size.

### Solution, step 1: Compute Cohen's Incremental Effect Size $f^2$
The effect size for testing the addition of $u$ predictors to a base regression model is:
$$f^2 = \frac{R_{\text{full}}^2 - R_{\text{base}}^2}{1 - R_{\text{full}}^2} = \frac{\Delta R^2}{1 - R_{\text{full}}^2}$$
Substitute $R_{\text{base}}^2 = 0.250$ and $R_{\text{full}}^2 = 0.320$:
$$\Delta R^2 = 0.320 - 0.250 = 0.070$$
$$1 - R_{\text{full}}^2 = 1 - 0.320 = 0.680$$
$$f^2 = \frac{0.070}{0.680} \approx \mathbf{0.10294}$$
The incremental effect size is $f^2 \approx 0.103$ (between Cohen's small ($0.02$) and medium ($0.15$) benchmarks).

### Solution, step 2: Determine Required Sample Size via Non-Central $F$ Framework
In an incremental $F$-test:
- Numerator degrees of freedom: $\nu_1 = u = 3$.
- Denominator degrees of freedom: $\nu_2 = N - k - 1 = N - 7 - 1 = N - 8$.
- The non-centrality parameter is: $\lambda = f^2 \times N$.

For $\nu_1 = 3$, $\alpha = 0.05$, and Power $= 0.80$, standard non-central $F$ numerical tables or power approximations establish that the required non-centrality parameter is approximately $\lambda^* \approx 10.90$.
Set $\lambda = f^2 \times N = \lambda^*$:
$$N = \frac{\lambda^*}{f^2} = \frac{10.90}{0.10294} \approx 105.89 \implies \mathbf{106 \text{ corporate firms}}$$
To verify with denominator degrees of freedom:
With $N = 106$, $\nu_2 = 106 - 8 = 98$.
The critical central $F$-value is $F_{3, 98, 0.95} = 2.697$.
Under the non-central distribution $F_{3, 98}(\lambda = 0.10294 \times 106 = 10.912)$:
$$\text{Power} = 1 - F_{3, 98, \lambda}(2.697) \approx 0.804 \quad (80.4\%)$$
The study requires a total sample size of $N = 106$ firms.

### Solution, step 3: State the Degrees of Freedom for the Incremental $F$-Test
Under sample size $N = 106$:
- Numerator degrees of freedom: $\nu_1 = u = \mathbf{3}$.
- Denominator degrees of freedom: $\nu_2 = N - k - 1 = 106 - 7 - 1 = \mathbf{98}$.
The incremental test statistic:
$$F = \frac{(R_{\text{full}}^2 - R_{\text{base}}^2) / 3}{(1 - R_{\text{full}}^2) / 98}$$
will follow the central $F_{3, 98}$ under the null hypothesis, and the non-central $F_{3, 98}(\lambda = 10.91)$ under the alternative, ensuring $80.4\%$ statistical power.

## 5.6 The Post-Hoc Power Fallacy
A notorious, persistent methodological error in applied research is post-hoc (retrospective) power analysis. When an empirical study fails to achieve statistical significance ($p > 0.05$), peer reviewers or researchers frequently calculate "observed power" by plugging the observed sample effect size $\hat{d}$ and sample size $n$ into power formulas. They then conclude: *"The study yielded $p = 0.18$ because it only had $32\%$ power; hence the non-significant result was merely due to low power, and the effect is likely real."*

In a celebrated 2001 paper titled *"The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis,"* John M. Hoenig and Dennis M. Heisey proved that post-hoc power is mathematically vacuous:
1. One-to-One Deterministic Function: Once a study is completed, post-hoc power is an exact, monotonic mathematical transformation of the observed $p$-value. It contains zero new information beyond the $p$-value itself. When $p = 0.05$, post-hoc power for a two-tailed $z$-test is mathematically fixed at exactly $50.0\%$. If $p > 0.05$, post-hoc power is *always* less than $50\%$.
2. The Fallacy of True Effect Presumption: Post-hoc power uses the sample estimate $\hat{d}$ as if it were the true population effect. However, if $p > 0.05$, the data are completely compatible with $d = 0$ (the null hypothesis). If $d = 0$, the true power is merely $\alpha = 0.05$.
3. Epistemological Contradiction: Using low post-hoc power to explain away a non-significant result allows researchers to claim that every non-significant finding is secretly a true effect that suffered from insufficient power, rendering scientific refutation impossible.

Retrospective statistical precision must be communicated through Confidence Intervals, never through post-hoc power. Prospective power calculations are essential *before* data collection; post-hoc power calculations are a mathematical illusion.

## 5.7 Unit 5 Methodological Synthesis and Review
Statistical power analysis ensures empirical research possesses adequate mathematical sensitivity:
- Explicitly integrate the four parameters of statistical testing: $\alpha$, power ($1 - \beta$), sample size $n$, and effect size.
- Utilize non-central sampling distributions ($t'(\delta), F'(\lambda), \chi^2(\lambda)$) to calculate exact power under the alternative hypothesis.
- Select appropriate standardized effect sizes (Cohen's $d$, Hedges' $g$, $r$, Cohen's $f^2$, Odds Ratios), applying small-sample corrections when $N < 30$.
- Never compute or report post-hoc power; communicate retrospective estimation uncertainty using confidence intervals.
"""

(DRAFT_DIR / "unit-5.md").write_text(u5_content.strip() + "\n", encoding="utf-8")
print("Unit 5 generated.")
