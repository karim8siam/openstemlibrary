# tooling/expand-unit-7.py
import re

content = r"""

---

## Multiple Imputation: Rubin's Theory and Variance Combining Rules

While single imputation techniques—such as mean imputation, regression imputation, or deterministic hot deck—restore a complete dataset suitable for point estimation, they suffer from a fatal inferential flaw: **single imputation treats imputed synthetic values as if they were true, observed empirical measurements**. By replacing missing values with deterministic predictions, single imputation artificially suppresses variability, overstates sample precision, and shrinks standard errors, leading to artificially narrow confidence intervals and inflated Type I error rates.

To resolve this fundamental defect, Donald Rubin (1978, 1987) formulated **Multiple Imputation (MI)**. Multiple imputation replaces each missing value not with a single deterministic value, but with a vector of $M \ge 2$ independent simulated values drawn from the posterior predictive distribution of the missing data given the observed data:
$$P(Y_{mis} \mid Y_{obs})$$

This creates $M$ distinct, complete data matrices:
$$\mathbf{D}^{(1)}, \mathbf{D}^{(2)}, \dots, \mathbf{D}^{(M)}$$

Each completed dataset is analyzed independently using identical, standard full-sample statistical methods. Finally, Rubin's combining rules aggregate the $M$ individual estimates and standard errors into a single, valid scientific inference that honestly reflects both sampling variability and the added uncertainty due to missingness.

### The Three Phases of Multiple Imputation

1. **Imputation Phase**: The statistician fits an imputation model relating the missing variables to the observed covariates. Drawing from the posterior predictive distribution, $M$ imputed values are generated for every missing item, reflecting both model estimation uncertainty (drawing parameter values from their posterior) and idiosyncratic residual uncertainty.
2. **Analysis Phase**: The analyst fits the desired substantive model (e.g. regression, survey mean, or domain contrast) to each of the $M$ completed datasets separately. For imputation $m$ ($m = 1, \dots, M$), this yields a point estimate $\hat{Q}^{(m)}$ and its corresponding estimated design-based sampling variance $U^{(m)} = \hat{V}(\hat{Q}^{(m)})$.
3. **Pooling Phase**: The $M$ pairs $(\hat{Q}^{(m)}, U^{(m)})$ are combined using Rubin's mathematical formulas.

### Rubin's Mathematical Combining Rules

Let $Q$ denote the scalar population quantity of interest (such as a population mean, a regression slope, or a log-odds ratio).

#### 1. The Combined Point Estimator
The overall multiple imputation point estimate is the simple unweighted average of the $M$ separate point estimates:
$$\bar{Q}_M = \frac{1}{M} \sum_{m=1}^M \hat{Q}^{(m)}$$
Under proper imputation models, $\bar{Q}_M$ is an unbiased and consistent estimator of $Q$.

#### 2. The Within-Imputation Variance
The within-imputation variance measures the average conventional sampling uncertainty across the $M$ completed datasets:
$$\bar{U}_M = \frac{1}{M} \sum_{m=1}^M U^{(m)}$$
where $U^{(m)}$ is the design-based variance estimator computed on dataset $m$ (accounting for strata, clusters, and survey weights).

#### 3. The Between-Imputation Variance
The between-imputation variance measures the extra variability induced by the missing data process, captured by the variance of the point estimates across the $M$ imputations:
$$B_M = \frac{1}{M - 1} \sum_{m=1}^M (\hat{Q}^{(m)} - \bar{Q}_M)^2$$
If there are no missing data, the $M$ completed datasets are identical, and $B_M = 0$. As the proportion of missing data increases, the estimates $\hat{Q}^{(m)}$ diverge across imputations, and $B_M$ expands.

#### 4. The Total Variance Formula
Rubin established that the total estimated variance of the combined estimator $\bar{Q}_M$ is:
$$T_M = \bar{U}_M + \left( 1 + \frac{1}{M} \right) B_M$$

Notice the multiplier $(1 + 1/M)$:
- The first term, $\bar{U}_M$, is the average sampling variance if the data were complete.
- The second term, $B_M$, is the variance inflation due to missing data.
- The factor $1/M \times B_M$ is a finite-sample correction accounting for the simulation Monte Carlo noise resulting from using a finite number $M$ of imputed datasets rather than an infinite number ($M \to \infty$).

#### 5. Relative Increase in Variance (RIV) and Fraction of Missing Information (FMI)
To quantify the impact of missingness on the parameter estimate, Rubin defined:
- **Relative Increase in Variance (RIV)**:
  $$r_M = \frac{(1 + 1/M) B_M}{\bar{U}_M}$$
  The RIV represents the proportional inflation of sampling variance attributable entirely to missing values.
- **Fraction of Missing Information (FMI)**:
  $$\hat{\lambda}_M = \frac{r_M + \frac{2}{\nu + 3}}{1 + r_M}$$
  In large samples, this simplifies to the intuitive variance ratio:
  $$\hat{\lambda}_M \approx \frac{B_M + B_M / M}{T_M}$$
  The FMI measures the proportion of total inferential uncertainty that is caused by missing values rather than sampling design constraints.

### Degrees of Freedom and Hypothesis Testing

In standard large-sample theory, Rubin and Schenker (1986) derived the reference degrees of freedom for $t$-tests and confidence intervals:
$$\nu_{Rubin} = (M - 1) \left( 1 + \frac{1}{r_M} \right)^2 = (M - 1) \left( 1 + \frac{\bar{U}_M}{(1 + 1/M) B_M} \right)^2$$

When $B_M$ is small relative to $\bar{U}_M$ ($r_M \to 0$), $\nu_{Rubin} \to \infty$. However, in sample surveys with finite complex designs, the complete-data degrees of freedom are not infinite, but bounded by the design degrees of freedom:
$$\nu_{com} = \sum_{h=1}^H n_h - H$$

If $\nu_{Rubin}$ exceeds $\nu_{com}$, confidence intervals will be artificially narrow. To resolve this, Barnard and Rubin (1999) formulated the **small-sample adjusted degrees of freedom for complex surveys**:
$$\nu_{obs} = \left( \frac{\nu_{com} + 1}{\nu_{com} + 3} \right) \nu_{com} (1 - \hat{\lambda}_M)$$
$$\nu_{BR} = \left( \frac{1}{\nu_{Rubin}} + \frac{1}{\nu_{obs}} \right)^{-1} = \frac{\nu_{Rubin} \nu_{obs}}{\nu_{Rubin} + \nu_{obs}}$$

The $(1 - \alpha) \times 100\%$ confidence interval for the population parameter $Q$ is:
$$\bar{Q}_M \pm t_{\nu_{BR}, 1 - \alpha/2} \sqrt{T_M}$$
This small-sample correction delivers exact nominal coverage across complex multistage survey designs.

---

### Step-by-Step Numerical Walkthrough: Rubin's Combining Rules

To solidify the algebraic mechanics, let us work through a complete numerical calculation of Rubin's pooling rules for a survey estimate of the gender wage differential $\Delta = \bar{Y}_{male} - \bar{Y}_{female}$ evaluated across $M = 5$ imputed survey datasets.

Suppose a complex stratified survey has complete-data design degrees of freedom $\nu_{com} = 40$ (e.g. 50 PSUs across 10 strata, so $50 - 10 = 40$). The five imputed datasets produce the following point estimates and estimated variances:

| Imputation ($m$) | Point Estimate $\hat{Q}^{(m)}$ (dollars/hr) | Variance $U^{(m)}$ | Standard Error $\sqrt{U^{(m)}}$ |
|:---:|:---:|:---:|:---:|
| 1 | 4.80 | 0.220 | 0.4690 |
| 2 | 5.25 | 0.235 | 0.4848 |
| 3 | 4.95 | 0.215 | 0.4637 |
| 4 | 5.40 | 0.240 | 0.4899 |
| 5 | 5.10 | 0.230 | 0.4796 |

#### Step 1: Compute the Combined Point Estimate $\bar{Q}_5$
$$\bar{Q}_5 = \frac{1}{5} \sum_{m=1}^5 \hat{Q}^{(m)} = \frac{4.80 + 5.25 + 4.95 + 5.40 + 5.10}{5} = \frac{25.50}{5} = 5.100 \text{ dollars/hour}$$

#### Step 2: Compute the Within-Imputation Variance $\bar{U}_5$
$$\bar{U}_5 = \frac{1}{5} \sum_{m=1}^5 U^{(m)} = \frac{0.220 + 0.235 + 0.215 + 0.240 + 0.230}{5} = \frac{1.140}{5} = 0.2280$$

#### Step 3: Compute the Between-Imputation Variance $B_5$
Compute the deviation of each point estimate from $\bar{Q}_5 = 5.100$:
- $m = 1$: $(4.80 - 5.10)^2 = (-0.30)^2 = 0.0900$
- $m = 2$: $(5.25 - 5.10)^2 = (+0.15)^2 = 0.0225$
- $m = 3$: $(4.95 - 5.10)^2 = (-0.15)^2 = 0.0225$
- $m = 4$: $(5.40 - 5.10)^2 = (+0.30)^2 = 0.0900$
- $m = 5$: $(5.10 - 5.10)^2 = (0.00)^2 = 0.0000$

Sum of squared deviations:
$$\sum_{m=1}^5 (\hat{Q}^{(m)} - \bar{Q}_5)^2 = 0.0900 + 0.0225 + 0.0225 + 0.0900 + 0.0000 = 0.2250$$

Dividing by $M - 1 = 5 - 1 = 4$:
$$B_5 = \frac{0.2250}{4} = 0.05625$$

#### Step 4: Compute the Total Variance $T_5$ and Standard Error
The finite-sample Monte Carlo multiplier is:
$$1 + \frac{1}{M} = 1 + \frac{1}{5} = 1 + 0.20 = 1.20$$

The total variance is:
$$T_5 = \bar{U}_5 + \left( 1 + \frac{1}{5} \right) B_5 = 0.2280 + 1.20 \times 0.05625 = 0.2280 + 0.0675 = 0.2955$$

The total standard error is:
$$\text{SE}(\bar{Q}_5) = \sqrt{T_5} = \sqrt{0.2955} \approx 0.5436 \text{ dollars/hour}$$

Compare this with naive single imputation: if an analyst had simply analyzed the first imputed dataset, they would have reported a standard error of $\sqrt{0.220} \approx 0.4690$. Multiple imputation reveals that the true uncertainty is $0.5436$—a **$16\%$ increase in standard error** caused by item nonresponse!

#### Step 5: Compute RIV and FMI
The Relative Increase in Variance is:
$$r_5 = \frac{(1 + 1/5) B_5}{\bar{U}_5} = \frac{0.0675}{0.2280} \approx 0.29605 \quad (\approx 29.61\%)$$

The Fraction of Missing Information is:
$$\hat{\lambda}_5 \approx \frac{B_5 + B_5 / 5}{T_5} = \frac{0.0675}{0.2955} \approx 0.22843 \quad (\approx 22.84\%)$$
Approximately $22.84\%$ of the total inferential uncertainty about the wage gap is attributable to missing survey data.

#### Step 6: Compute Barnard–Rubin Small-Sample Degrees of Freedom
First, compute the standard Rubin large-sample degrees of freedom:
$$\nu_{Rubin} = (M - 1) \left( 1 + \frac{1}{r_5} \right)^2 = (5 - 1) \left( 1 + \frac{1}{0.29605} \right)^2 = 4 \times (1 + 3.3778)^2 = 4 \times (4.3778)^2 = 4 \times 19.165 \approx 76.66$$

Next, compute the observed data degrees of freedom using the complete design degrees of freedom $\nu_{com} = 40$:
$$\nu_{obs} = \left( \frac{\nu_{com} + 1}{\nu_{com} + 3} \right) \nu_{com} (1 - \hat{\lambda}_5) = \left( \frac{41}{43} \right) \times 40 \times (1 - 0.22843) = 0.95349 \times 40 \times 0.77157 \approx 29.43$$

Finally, combine $\nu_{Rubin}$ and $\nu_{obs}$ into the Barnard–Rubin degrees of freedom:
$$\nu_{BR} = \frac{\nu_{Rubin} \times \nu_{obs}}{\nu_{Rubin} + \nu_{obs}} = \frac{76.66 \times 29.43}{76.66 + 29.43} = \frac{2,256.1}{106.09} \approx 21.27 \approx 21 \text{ degrees of freedom}$$

For a two-sided $95\%$ confidence interval with $\nu = 21$, the Student-$t$ critical value is $t_{21, 0.975} = 2.0796$.
The honest $95\%$ confidence interval for the wage differential is:
$$\bar{Q}_5 \pm t_{21, 0.975} \times \text{SE}(\bar{Q}_5) = 5.100 \pm 2.0796 \times 0.5436 = 5.100 \pm 1.130 = [3.970, 6.230] \text{ dollars/hour}$$

Because zero is well outside this interval, we conclude with $95\%$ confidence that there is a statistically significant gender wage gap between $3.97$ and $6.23$ dollars per hour, fully accounting for complex survey clustering, stratification, and missing data imputation uncertainty.
"""

filepath = 'publishing/drafts/statistics-probability-sample-surveys-and-sampling-theory/unit-7.md'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

split_phrase = '## Sensitivity Analysis for Non-Ignorable Nonresponse (MNAR)'
if split_phrase in text:
    parts = text.split(split_phrase)
    new_text = parts[0] + content + '\n---\n\n## Sensitivity Analysis for Non-Ignorable Nonresponse (MNAR)' + parts[1]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("SUCCESSFULLY EXPANDED UNIT 7!")
else:
    print("Split phrase not found!")
