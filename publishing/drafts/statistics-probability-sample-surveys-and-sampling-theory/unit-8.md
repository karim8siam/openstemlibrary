# Unit 8: Complex-Survey Inference and Replicate Variance Estimation

## The Architecture of Complex Multistage Probability Surveys

Throughout the previous units, we examined individual foundational sampling principles in isolation: finite population correction under simple random sampling, variance reduction through stratification, logistical efficiency through clustering, variance minimization via probability proportional to size (PPS), and demographic benchmarking through calibration weighting. In actual scientific and official practice—such as the United States National Health and Nutrition Examination Survey (NHANES), the Demographic and Health Surveys (DHS), the European Social Survey (ESS), and national labor force surveys—no single design is deployed alone. Instead, modern empirical inquiries combine all these principles into an integrated **complex multistage survey design**.

A canonical complex survey design exhibits a four-tier architecture:
1. **Multidimensional Stratification**: The national territory is stratified into homogeneous partitions crossing geographic regions (provinces, divisions), urbanicity strata (metropolitan cities, secondary towns, rural villages), and socioeconomic indices. Stratification guarantees balanced geographical representation and eliminates between-stratum variance.
2. **Multistage Clustering**: Within each stratum, Primary Sampling Units (PSUs)—typically census enumeration areas containing 100 to 300 households—are selected. In three-stage designs, secondary sampling units (SSUs, such as residential dwelling blocks) are sampled within PSUs, and ultimate observation units (individuals or households) are selected at the final stage. Clustering drastically reduces travel overhead and field listing expenditures.
3. **Unequal Probability Selection (PPS)**: PSUs are selected with probability proportional to estimated size (measures of size derived from the most recent national decennial census). Certainty units are isolated for mega-cities, while small demographic subgroups (such as indigenous populations or minority language groups) are oversampled with elevated inclusion probabilities to ensure adequate sample sizes for sub-national domain analysis.
4. **Post-Survey Weight Adjustments**: Raw design weights $d_i = 1 / \pi_i$ are sequentially multiplied by nonresponse adjustment factors $f_{nr,i}$ (derived from weighting classes or logistic response propensity models) and calibration adjustment factors $g_i$ (derived from Deville–Särndal distance minimization against administrative registry benchmarks).

The final **analytic survey weight** for sampled unit $i$ is:
$$w_i = d_i \times f_{nr,i} \times g_i$$

This composite weight represents the actual number of individuals in the target finite universe represented by unit $i$ in all published statistical tables and econometric models.

---

## The Failure of Classical IID Statistics in Complex Surveys

The paramount inferential danger in quantitative research is the naive application of classical statistical methods to complex survey data. Standard statistical theory—as embedded in elementary software routines for ordinary least squares (OLS) regression, Student's $t$-tests, analysis of variance (ANOVA), and Pearson's chi-square tests—rests upon the foundational assumption that observations are **independent and identically distributed (IID)**:
$$y_1, y_2, \dots, y_n \stackrel{\text{iid}}{\sim} F(\cdot)$$

In a complex survey, the IID assumption fails completely on every dimension:
- **Clustering Destroys Independence**: Observations residing within the same Primary Sampling Unit are positively correlated due to shared neighborhood environments, local infrastructure, and common enumerator interviewer effects ($\rho > 0$).
- **Unequal Weights Destroy Identical Distributions**: Units have vastly different inclusion probabilities and design weights; treating an oversampled minority respondent with weight $w_i = 50$ identically to an undersampled majority respondent with weight $w_j = 2,000$ induces severe selection bias.
- **Stratification Constrains Sampling Realizations**: Stratified selection restricts sampling variability by forcing fixed sample takes within strata, introducing negative covariances across stratum boundaries.

### The Consequences of Software Misspecification

If an investigator imports complex survey data into standard software and executes unweighted or naive IID statistical routines, three catastrophic errors occur:

1. **Severe Underestimation of Standard Errors**:
   The variance of an estimator is inflated by the **Design Effect ($\text{Deff}$)**:
   $$\text{Deff}(\hat{\theta}) = \frac{V_{complex}(\hat{\theta})}{V_{srs}(\hat{\theta})}$$
   In nationwide household surveys, typical design effects range from $2.0$ to $6.0$ for health variables, and up to $10.0$ or $15.0$ for clustered poverty and environmental indicators. 
   Naive software computes standard errors based on $V_{srs} = V_{complex} / \text{Deff}$. When $\text{Deff} = 4.0$, naive software reports a standard error that is $\sqrt{4} = 2.0$ times too small! The reported standard error is cut in half purely by software blindness.

2. **Catastrophic Confidence Interval Undercoverage**:
   Because the standard error is underestimated by half, nominal 95% confidence intervals constructed as $\hat{\theta} \pm 1.96 \times \text{SE}_{naive}$ are far too narrow. Empirical simulation proves that under a design effect of $4.0$, a nominal 95% confidence interval achieves an actual empirical coverage rate of only **$68\%$ to $75\%$**. One out of every four published confidence intervals fails to cover the true population parameter!

3. **Explosion of Type I Error Rates (Spurious Statistical Significance)**:
   Hypothesis test statistics are inflated by the design effect:
   $$t_{naive} = \frac{\hat{\theta} - \theta_0}{\text{SE}_{naive}} = \sqrt{\text{Deff}} \times t_{complex}$$
   Under a design effect of $4.0$, test statistics are doubled. An empirical difference that is completely attributable to random sampling noise ($t_{complex} = 1.25, p = 0.21$) produces a naive test statistic of $t_{naive} = 2.50$, yielding a falsely significant $p$-value of $0.012$! Researchers falsely claim "statistically significant discoveries" that are artifacts of clustered sampling.

4. **Failure of Contingency Table Chi-Square Tests**:
   The classical Pearson goodness-of-fit and independence test statistic:
   $$X^2 = \sum_{r,c} \frac{(n_{rc} - E_{rc})^2}{E_{rc}}$$
   no longer follows a central $\chi^2$ distribution under the null hypothesis. It behaves asymptotically as a weighted sum of independent $\chi_1^2$ variates whose weights are the eigenvalues of a generalized design effect matrix. To salvage categorical analysis, survey statisticians deploy the **Rao–Scott First- and Second-Order Corrections** (Rao and Scott, 1981, 1984), which adjust the chi-square statistic by the mean eigenvalue and Satterthwaite degrees of freedom.

---

## Taylor Series Linearization (The Delta Method) for Complex Estimators

To obtain design-consistent standard errors for non-linear statistics—such as ratio estimators, regression coefficients, odds ratios, and poverty gap indices—survey theory deploys two rigorous computational methodologies: **Taylor Series Linearization** and **Replication Resampling**.

### Mathematical Formulation of Linearization

Let $\hat{\boldsymbol{\theta}} = (\hat{\theta}_1, \dots, \hat{\theta}_k)^\top$ be an estimator of a population parameter $\boldsymbol{\theta}$. Suppose $\hat{\boldsymbol{\theta}}$ can be expressed as a smooth, continuously differentiable vector-valued function $g(\cdot)$ of a set of estimated population totals $\hat{\mathbf{Y}} = (\hat{Y}_1, \dots, \hat{Y}_p)^\top$:
$$\hat{\boldsymbol{\theta}} = g(\hat{\mathbf{Y}}) = g(\hat{Y}_1, \hat{Y}_2, \dots, \hat{Y}_p)$$
where each total is estimated using standard linear survey weights:
$$\hat{Y}_k = \sum_{i \in s} w_i y_{ki}$$

The true population parameter is $\boldsymbol{\theta} = g(\mathbf{Y})$, where $\mathbf{Y} = (Y_1, \dots, Y_p)^\top$ are the true population totals.

We expand $g(\hat{\mathbf{Y}})$ in a first-order multivariate Taylor series around the true population total vector $\mathbf{Y}$:
$$g(\hat{\mathbf{Y}}) \approx g(\mathbf{Y}) + \sum_{k=1}^p \left. \frac{\partial g}{\partial Y_k} \right|_{\mathbf{Y}} (\hat{Y}_k - Y_k)$$

Let $D_k = \left. \frac{\partial g}{\partial Y_k} \right|_{\mathbf{Y}}$ denote the partial derivative of $g$ with respect to the $k$-th total, evaluated at the true population values.
The estimation error is approximated as:
$$\hat{\boldsymbol{\theta}} - \boldsymbol{\theta} \approx \sum_{k=1}^p D_k (\hat{Y}_k - Y_k)$$

### The Linearized Synthetic Variable

Now express each estimated total in terms of unit-level observations:
$$\sum_{k=1}^p D_k \hat{Y}_k = \sum_{k=1}^p D_k \sum_{i \in s} w_i y_{ki} = \sum_{i \in s} w_i \left( \sum_{k=1}^p D_k y_{ki} \right)$$

Define the **linearized synthetic variable** for unit $i$:
$$z_i = \sum_{k=1}^p D_k y_{ki}$$

In empirical practice, because the true totals $\mathbf{Y}$ and derivatives $D_k$ are unknown, we substitute the sample estimates $\hat{\mathbf{Y}}$:
$$\hat{D}_k = \left. \frac{\partial g}{\partial Y_k} \right|_{\hat{\mathbf{Y}}} \implies z_i = \sum_{k=1}^p \hat{D}_k y_{ki}$$

With this construction, the non-linear estimation error is linearized into the error of an ordinary linear total estimator:
$$\hat{\boldsymbol{\theta}} - \boldsymbol{\theta} \approx \sum_{i \in s} w_i z_i - Z = \hat{Z} - Z$$

### Variance Estimation under Stratified Multistage Designs

Once the linearized variable $z_i$ is evaluated for every respondent in the dataset, the variance of $\hat{\boldsymbol{\theta}}$ is simply the variance of the linear estimator $\hat{Z}$ under the complex stratified multistage design!

Let the survey design contain $H$ strata. Within stratum $h$ ($h = 1, \dots, H$), suppose $n_h$ Primary Sampling Units (PSUs) are selected.
Let $w_{hij}$ and $z_{hij}$ denote the analytic weight and linearized value for observation unit $j$ within PSU $i$ of stratum $h$.

Define the weighted aggregate for PSU $(h, i)$:
$$z_{hi} = \sum_{j \in \text{PSU}_{hi}} w_{hij} z_{hij}$$
The stratum total is:
$$\hat{Z}_h = \sum_{i=1}^{n_h} z_{hi}$$
The average per PSU in stratum $h$ is:
$$\bar{z}_h = \frac{1}{n_h} \sum_{i=1}^{n_h} z_{hi} = \frac{\hat{Z}_h}{n_h}$$

Applying the Ultimate Cluster principle, the design-consistent Taylor series variance estimator is:
$$\hat{V}_{linear}(\hat{\boldsymbol{\theta}}) = \sum_{h=1}^H \frac{n_h}{n_h - 1} \sum_{i=1}^{n_h} (z_{hi} - \bar{z}_h)^2$$

If the first-stage finite population correction factor $f_h = n_h / N_h$ is non-negligible, the term is multiplied by $(1 - f_h)$:
$$\hat{V}_{linear}(\hat{\boldsymbol{\theta}}) = \sum_{h=1}^H (1 - f_h) \frac{n_h}{n_h - 1} \sum_{i=1}^{n_h} (z_{hi} - \bar{z}_h)^2$$

The design degrees of freedom for statistical inference under Taylor linearization are:
$$\text{df} = \sum_{h=1}^H n_h - H = (\text{Total Sampled PSUs}) - (\text{Number of Strata})$$

---

## Replication Variance Estimation: Resampling Frameworks

While Taylor series linearization is computationally fast, it requires deriving analytical partial derivatives for every new statistic. For non-differentiable estimators—such as sample medians, percentiles, and Gini inequality coefficients—derivatives do not exist. Furthermore, linearization does not automatically account for the stochastic variation introduced during imputation and calibration.

To overcome these limitations, survey statisticians deploy **Replication Variance Estimation**. In replication methods, the sample is repeatedly re-weighted to mimic the original complex selection mechanism.

### 1. Jackknife Repeated Replication (JRR)

The delete-one-PSU Jackknife is the most versatile replication method for stratified multistage designs.

#### Construction of Jackknife Replicate Weights:
Suppose the design contains $H$ strata with $n_h \ge 2$ PSUs in each stratum. The total number of PSUs across the entire survey is:
$$A = \sum_{h=1}^H n_h$$

The Jackknife generates exactly $A$ distinct replicate weight vectors. Each replicate $(h, j)$ corresponds to temporarily deleting the $j$-th PSU from the $h$-th stratum:

For replicate $(h, j)$ (where PSU $j$ in stratum $h$ is deleted):
$$w_i^{(hj)} = \begin{cases} 
0 & \text{if unit } i \text{ belongs to the deleted PSU } (h, j) \\
\left( \frac{n_h}{n_h - 1} \right) w_i & \text{if unit } i \text{ belongs to an un-deleted PSU in stratum } h \\
w_i & \text{if unit } i \text{ belongs to any other stratum } h' \ne h 
\end{cases}$$

Notice what occurs: 
- In the affected stratum $h$, the deletion of one PSU is compensated for by scaling up the weights of the remaining $n_h - 1$ PSUs by the factor $\frac{n_h}{n_h - 1}$, preserving the stratum total weight.
- All other strata are left completely untouched.

#### Parameter Re-Estimation:
The full statistical estimation process (including calibration, if applicable) is re-executed on each of the $A$ replicate weight vectors, producing $A$ replicate point estimates:
$$\hat{\theta}^{(hj)} = \hat{\theta}(\mathbf{w}^{(hj)}) \quad \left( h = 1, \dots, H; \; j = 1, \dots, n_h \right)$$

#### Jackknife Variance Formula:
The delete-one-PSU Jackknife variance estimator is:
$$\hat{V}_{JRR}(\hat{\theta}) = \sum_{h=1}^H \frac{n_h - 1}{n_h} \sum_{j=1}^{n_h} (\hat{\theta}^{(hj)} - \hat{\theta})^2$$
where $\hat{\theta}$ is the full-sample point estimate.

In the special case of a two-PSU-per-stratum design ($n_h = 2$ for all $h$), forming $H$ replicates by deleting one PSU per stratum simplifies the multiplier:
$$\hat{V}_{JRR}(\hat{\theta}) = \sum_{h=1}^H (\hat{\theta}^{(h)} - \hat{\theta})^2$$

### 2. Balanced Repeated Replication (BRR) and Hadamard Matrices

Balanced Repeated Replication (McCarthy, 1966) is designed specifically for **paired designs**, where exactly two Primary Sampling Units are selected per stratum ($n_h = 2$ for all $h = 1, \dots, H$). Paired designs are exceptionally common in national master frames (e.g., the U.S. National Health Interview Survey) because allocating two PSUs per stratum maximizes the number of distinct strata that can be formed within a fixed budget.

#### Half-Sample Allocation:
In a design with $H$ strata and $n_h = 2$, a **half-sample** is formed by selecting exactly one of the two PSUs from each of the $H$ strata. There are $2^H$ possible half-samples. Evaluating all $2^H$ half-samples is computationally impossible when $H \ge 30$ ($2^{30} > 10^9$).

McCarthy proved that full precision is achieved by selecting a small, mathematically **orthogonal subset of $K$ half-samples**, where $K$ is the smallest multiple of 4 satisfying:
$$K \ge H + 1$$

The orthogonal balance is defined by a **Hadamard Matrix** $\mathbf{H}_K$ of dimension $K \times K$. A Hadamard matrix contains entries $\pm 1$ whose columns are mutually orthogonal:
$$\mathbf{H}_K^\top \mathbf{H}_K = K \mathbf{I}_K$$

For each replicate $k \in \{1, 2, \dots, K\}$:
Let $a_{kh} \in \{+1, -1\}$ denote the entry in row $k$ and column $h$ of the Hadamard matrix.
The BRR replicate weight for unit $i$ in stratum $h$ is:
$$w_i^{(k)} = \begin{cases} 
2 w_i & \text{if } a_{kh} = +1 \text{ and unit } i \text{ belongs to PSU 1} \\
0 & \text{if } a_{kh} = +1 \text{ and unit } i \text{ belongs to PSU 2} \\
0 & \text{if } a_{kh} = -1 \text{ and unit } i \text{ belongs to PSU 1} \\
2 w_i & \text{if } a_{kh} = -1 \text{ and unit } i \text{ belongs to PSU 2}
\end{cases}$$

#### The BRR Variance Formula:
The parameter is re-estimated on each of the $K$ orthogonal half-samples: $\hat{\theta}^{(k)} = \hat{\theta}(\mathbf{w}^{(k)})$.
The BRR variance estimator is:
$$\hat{V}_{BRR}(\hat{\theta}) = \frac{1}{K} \sum_{k=1}^K (\hat{\theta}^{(k)} - \hat{\theta})^2$$

#### Fay's Perturbation Variant of BRR:
A practical limitation of standard BRR is that setting weights to zero ($w_i^{(k)} = 0$) can cause non-convergence in non-linear models (such as logistic regression) if an entire demographic subgroup disappears in a half-sample.
Robert Fay (1989) developed a perturbation variant: Instead of setting weights to $0$ and $2$, weights are perturbed by a factor $k_\epsilon \in [0, 1)$ (typically $k_\epsilon = 0.50$ or $0.70$):
$$w_i^{(k)} = \begin{cases} 
[1 + (1 - k_\epsilon)] w_i & \text{if selected} \\
[1 - (1 - k_\epsilon)] w_i & \text{if unselected}
\end{cases}$$
The Fay variance formula scales the deviations accordingly:
$$\hat{V}_{Fay}(\hat{\theta}) = \frac{1}{K (1 - k_\epsilon)^2} \sum_{k=1}^K (\hat{\theta}^{(k)} - \hat{\theta})^2$$

### 3. The Survey Bootstrap

The survey bootstrap (Rao and Wu, 1988) resamples PSUs within each stratum with replacement. For stratum $h$ with $n_h$ PSUs, a bootstrap sample of $m_h = n_h - 1$ PSUs is drawn with replacement. The bootstrap replicate weight is:
$$w_i^{(b)} = w_i \left[ \frac{n_h}{n_h - 1} \frac{m_{hi}^*}{m_h} \right]$$
where $m_{hi}^*$ is the number of times PSU $(h, i)$ was selected in bootstrap draw $b$. Repeating this $B = 500$ or $1,000$ times yields bootstrap variance estimates and percentile confidence intervals that naturally handle non-smooth estimators.

---

## Domain and Subpopulation Estimation

A ubiquitous requirement in survey analysis is estimating parameters for specific subpopulations (domains), such as female wage earners aged 25–34, rural minority farmers, or patients diagnosed with Type II diabetes.

### The Random Sample Size Problem

Let $U_d \subset U$ denote the subpopulation domain of interest, with population size $N_d$.
Define the domain indicator for unit $i$:
$$I_{di} = \begin{cases} 1 & \text{if unit } i \in U_d \\ 0 & \text{if unit } i \notin U_d \end{cases}$$

The true domain total is:
$$Y_d = \sum_{i \in U_d} y_i = \sum_{i \in U} I_{di} y_i$$
The true domain mean is:
$$\bar{Y}_d = \frac{Y_d}{N_d} = \frac{\sum_{i \in U} I_{di} y_i}{\sum_{i \in U} I_{di}}$$

When a probability sample $s$ is drawn, the number of sampled units that happen to fall into domain $d$ is:
$$n_d = \sum_{i \in s} I_{di}$$

Notice the critical distinction: Unless the survey was explicitly stratified on domain $d$ at the design stage, **the domain sample size $n_d$ is a random variable, not a fixed constant**. 

### The Estimator of the Domain Mean

The sample estimator of the domain mean is:
$$\hat{\bar{Y}}_d = \frac{\sum_{i \in s} w_i I_{di} y_i}{\sum_{i \in s} w_i I_{di}} = \frac{\hat{Y}_d}{\hat{N}_d}$$

This is structurally a **ratio of two random variables**: the estimated domain total $\hat{Y}_d$ divided by the estimated domain size $\hat{N}_d$. 

### The Fatal Practice of Subset Deletion

A widespread error among researchers is subsetting (filtering) the microdata dataset to domain $d$ prior to computing standard errors in software:
```python
# FATAL FLAW: Subsetting before variance estimation
domain_data = survey_data[survey_data['age'] < 25]
compute_survey_mean(domain_data, 'income')
```

When software is fed a subsetted dataset:
1. It treats the domain sample size $n_d$ as fixed, ignoring the stochastic sampling variability of which units enter the domain.
2. It miscalculates degrees of freedom by counting only PSUs that happen to contain domain members, frequently dropping entire strata that have no domain members, violating the design structure.
3. The resulting variance estimate is **systematically incorrect**.

**The Universal Law of Domain Estimation**:
To obtain valid unconditional standard errors, domain estimation must always be executed across the **entire dataset of $n$ observations**, using domain indicator variables $I_{di}$:
$$\hat{V}(\hat{\bar{Y}}_d) \approx \frac{1}{\hat{N}_d^2} \hat{V}\left( \sum_{i \in s} w_i I_{di} (y_i - \hat{\bar{Y}}_d) \right)$$
Only units with $I_{di} = 1$ contribute to the sum, but the variance is computed using the complete design structure across all strata and PSUs.

---

## Fully worked question 1: Taylor Series Linearization for the Variance of a Complex Ratio Estimator in a Stratified Multistage Design

**Question.** A national agricultural economic survey is conducted using a stratified two-stage design across $H = 2$ agricultural zones. In each zone, $n_h = 2$ Primary Sampling Units (districts) are selected via probability sampling. Within each selected district, agricultural holdings are sampled and weighted.

The survey estimates the economic efficiency ratio:
$$\hat{R} = \frac{\hat{Y}}{\hat{X}}$$
where:
- $Y$ is total commercial agricultural revenue (in millions of dollars).
- $X$ is total operational input expenditure (in millions of dollars).

The weighted summary totals for revenue ($y_{hi} = \sum_{j} w_{hij} y_{hij}$) and expenditure ($x_{hi} = \sum_{j} w_{hij} x_{hij}$) for each sampled district $(h, i)$ are:

$$\begin{array}{c|c|cc}
\text{Stratum } h & \text{PSU (District) } i & \text{Expenditure } x_{hi} & \text{Revenue } y_{hi} \\
\hline
\text{Stratum 1 (Northern)} & \text{PSU 1} & 120.0 & 180.0 \\
\text{Stratum 1 (Northern)} & \text{PSU 2} & 160.0 & 260.0 \\
\hline
\text{Stratum 2 (Southern)} & \text{PSU 1} & 80.0 & 110.0 \\
\text{Stratum 2 (Southern)} & \text{PSU 2} & 140.0 & 210.0 \\
\hline
\text{Total Sample} & & \hat{X} = 500.0 & \hat{Y} = 760.0
\end{array}$$

1. Compute the estimated population totals $\hat{X}$, $\hat{Y}$, and the estimated overall efficiency ratio $\hat{R}$.
2. Derive the mathematical formula for the linearized synthetic variable $z_{hij}$ for the ratio $\hat{R}$. Compute the linearized PSU aggregate values $z_{hi}$ for each of the 4 districts.
3. Compute the Taylor series linearized variance $\hat{V}(\hat{R})$, the standard error $\text{SE}(\hat{R})$, and the 95% confidence interval using the design degrees of freedom.

**Solution, step 1: Computing overall totals and the ratio estimate.**
Summing across all strata and PSUs:
$$\hat{X} = 120.0 + 160.0 + 80.0 + 140.0 = 500.0 \text{ million dollars}$$
$$\hat{Y} = 180.0 + 260.0 + 110.0 + 210.0 = 760.0 \text{ million dollars}$$

The estimated ratio is:
$$\hat{R} = \frac{\hat{Y}}{\hat{X}} = \frac{760.0}{500.0} = 1.5200$$
Every dollar of operational input expenditure yields an estimated 1.52 dollars in gross agricultural revenue.

**Solution, step 2: Deriving linearized variable and computing PSU values.**
The ratio estimator is $g(X, Y) = Y / X$.
Evaluate the partial derivatives at the estimated totals:
$$\hat{D}_Y = \left. \frac{\partial g}{\partial Y} \right|_{(\hat{X}, \hat{Y})} = \frac{1}{\hat{X}} = \frac{1}{500.0} = 0.0020$$
$$\hat{D}_X = \left. \frac{\partial g}{\partial X} \right|_{(\hat{X}, \hat{Y})} = -\frac{\hat{Y}}{\hat{X}^2} = -\frac{\hat{R}}{\hat{X}} = -\frac{1.5200}{500.0} = -0.00304$$

The linearized synthetic variable for unit $k$ is:
$$z_k = \hat{D}_Y y_k + \hat{D}_X x_k = \frac{1}{\hat{X}} y_k - \frac{\hat{R}}{\hat{X}} x_k = \frac{1}{\hat{X}} (y_k - \hat{R} x_k)$$

For an entire PSU $(h, i)$, the weighted aggregate is:
$$z_{hi} = \frac{1}{\hat{X}} \sum_{j} w_{hij} (y_{hij} - \hat{R} x_{hij}) = \frac{1}{\hat{X}} (y_{hi} - \hat{R} x_{hi})$$

Now compute the residual $(y_{hi} - \hat{R} x_{hi})$ and the linearized value $z_{hi}$ for each of the 4 PSUs:

1. **Stratum 1 (Northern Zone)**:
   - PSU 1:
     $$\hat{R} x_{11} = 1.5200 \times 120.0 = 182.40$$
     $$y_{11} - \hat{R} x_{11} = 180.0 - 182.40 = -2.40$$
     $$z_{11} = \frac{-2.40}{500.0} = -0.00480$$
   - PSU 2:
     $$\hat{R} x_{12} = 1.5200 \times 160.0 = 243.20$$
     $$y_{12} - \hat{R} x_{12} = 260.0 - 243.20 = +16.80$$
     $$z_{12} = \frac{+16.80}{500.0} = +0.03360$$

   Stratum 1 Mean:
   $$\bar{z}_1 = \frac{z_{11} + z_{12}}{2} = \frac{-0.00480 + 0.03360}{2} = \frac{0.02880}{2} = 0.01440$$

2. **Stratum 2 (Southern Zone)**:
   - PSU 1:
     $$\hat{R} x_{21} = 1.5200 \times 80.0 = 121.60$$
     $$y_{21} - \hat{R} x_{21} = 110.0 - 121.60 = -11.60$$
     $$z_{21} = \frac{-11.60}{500.0} = -0.02320$$
   - PSU 2:
     $$\hat{R} x_{22} = 1.5200 \times 140.0 = 212.80$$
     $$y_{22} - \hat{R} x_{22} = 210.0 - 212.80 = -2.80$$
     $$z_{22} = \frac{-2.80}{500.0} = -0.00560$$

   Stratum 2 Mean:
   $$\bar{z}_2 = \frac{z_{21} + z_{22}}{2} = \frac{-0.02320 - 0.00560}{2} = \frac{-0.02880}{2} = -0.01440$$

Notice that the overall sum across all 4 PSUs is:
$$\sum_{h=1}^2 \sum_{i=1}^2 z_{hi} = (-0.00480 + 0.03360) + (-0.02320 - 0.00560) = 0.02880 - 0.02880 = 0.000$$
The sum of the linearized residuals across the sample is identically zero! This provides an immediate mathematical verification of the linearization arithmetic.

**Solution, step 3: Computing linearized variance, standard error and confidence interval.**
Under the stratified multistage variance formula:
$$\hat{V}_{linear}(\hat{R}) = \sum_{h=1}^H \frac{n_h}{n_h - 1} \sum_{i=1}^{n_h} (z_{hi} - \bar{z}_h)^2$$

For $n_h = 2$, $\frac{n_h}{n_h - 1} = \frac{2}{1} = 2$.
Furthermore, for two values, $(z_{h1} - \bar{z}_h)^2 + (z_{h2} - \bar{z}_h)^2 = \frac{1}{2} (z_{h1} - z_{h2})^2$.
Therefore:
$$2 \times \frac{1}{2} (z_{h1} - z_{h2})^2 = (z_{h1} - z_{h2})^2$$

Compute the stratum variance contributions:
1. **Stratum 1 Contribution**:
   $$z_{11} - z_{12} = -0.00480 - 0.03360 = -0.03840$$
   $$V_1 = (-0.03840)^2 = 0.00147456$$

2. **Stratum 2 Contribution**:
   $$z_{21} - z_{22} = -0.02320 - (-0.00560) = -0.02320 + 0.00560 = -0.01760$$
   $$V_2 = (-0.01760)^2 = 0.00030976$$

Summing across both strata:
$$\hat{V}(\hat{R}) = V_1 + V_2 = 0.00147456 + 0.00030976 = 0.00178432$$

The standard error of the estimated ratio is:
$$\text{SE}(\hat{R}) = \sqrt{0.00178432} \approx 0.04224$$

Now compute the design degrees of freedom:
$$\text{df} = \sum_{h=1}^2 n_h - H = (2 + 2) - 2 = 4 - 2 = 2 \text{ degrees of freedom}$$

For $\text{df} = 2$, the critical value from the Student's $t$-distribution at the 95% confidence level ($\alpha = 0.05$) is:
$$t_{2, 0.025} = 4.303$$
Notice how crucial the design degrees of freedom are: using a normal critical value ($1.96$) with only 2 design degrees of freedom would severely understate uncertainty.

The 95% confidence interval half-width is:
$$E = t_{2, 0.025} \times \text{SE}(\hat{R}) = 4.303 \times 0.04224 \approx 0.1818$$

The 95% confidence interval for the agricultural revenue-to-expenditure ratio is:
$$1.5200 \pm 0.1818 \implies [1.3382, \quad 1.7018]$$
We are 95% confident that the true population efficiency ratio lies between $1.34$ and $1.70$.

---

## Fully worked question 2: Jackknife Repeated Replication (JRR) Weight Construction and Variance Estimation

**Question.** Consider the exact same agricultural survey data from Worked Question 1:
- Stratum 1: PSU 1 ($x_{11} = 120, y_{11} = 180$), PSU 2 ($x_{12} = 160, y_{12} = 260$)
- Stratum 2: PSU 1 ($x_{21} = 80, y_{21} = 110$), PSU 2 ($x_{22} = 140, y_{22} = 210$)
- Full-sample estimates: $\hat{X} = 500.0, \hat{Y} = 760.0, \hat{R} = 1.5200$

1. Formulate the delete-one-PSU Jackknife replicate weights for each of the $A = 4$ replicates:
   - Replicate $(1, 1)$: Delete PSU 1 in Stratum 1.
   - Replicate $(1, 2)$: Delete PSU 2 in Stratum 1.
   - Replicate $(2, 1)$: Delete PSU 1 in Stratum 2.
   - Replicate $(2, 2)$: Delete PSU 2 in Stratum 2.
2. For each of the 4 replicates, compute the replicate totals $\hat{X}^{(hj)}$ and $\hat{Y}^{(hj)}$, and calculate the replicate ratio estimate $\hat{R}^{(hj)}$.
3. Compute the Jackknife Repeated Replication variance $\hat{V}_{JRR}(\hat{R})$ and compare the result with the Taylor series linearization variance obtained in Question 1.

**Solution, step 1: Constructing Jackknife replicate weights and totals.**
Since each stratum contains $n_h = 2$ PSUs, deleting one PSU requires scaling the weight of the remaining PSU in that stratum by:
$$\frac{n_h}{n_h - 1} = \frac{2}{2 - 1} = 2$$
The remaining stratum is multiplied by $1$ (unchanged).

Let us compute the replicate totals for each of the 4 replicates:

1. **Replicate $(1, 1)$ [Delete PSU 1 in Stratum 1]**:
   - In Stratum 1: PSU 1 is deleted ($0$ weight). PSU 2 weight is doubled ($\times 2$):
     $x_{1}^{(1,1)} = 2 \times 160.0 = 320.0$
     $y_{1}^{(1,1)} = 2 \times 260.0 = 520.0$
   - In Stratum 2: Weights unchanged:
     $x_{2}^{(1,1)} = 80.0 + 140.0 = 220.0$
     $y_{2}^{(1,1)} = 110.0 + 210.0 = 320.0$
   - Total Replicate 1:
     $$\hat{X}^{(1,1)} = 320.0 + 220.0 = 540.0$$
     $$\hat{Y}^{(1,1)} = 520.0 + 320.0 = 840.0$$

2. **Replicate $(1, 2)$ [Delete PSU 2 in Stratum 1]**:
   - In Stratum 1: PSU 2 is deleted ($0$ weight). PSU 1 weight is doubled ($\times 2$):
     $x_{1}^{(1,2)} = 2 \times 120.0 = 240.0$
     $y_{1}^{(1,2)} = 2 \times 180.0 = 360.0$
   - In Stratum 2: Weights unchanged:
     $x_{2}^{(1,2)} = 220.0, \; y_{2}^{(1,2)} = 320.0$
   - Total Replicate 2:
     $$\hat{X}^{(1,2)} = 240.0 + 220.0 = 460.0$$
     $$\hat{Y}^{(1,2)} = 360.0 + 320.0 = 680.0$$

3. **Replicate $(2, 1)$ [Delete PSU 1 in Stratum 2]**:
   - In Stratum 1: Weights unchanged:
     $x_{1}^{(2,1)} = 120.0 + 160.0 = 280.0$
     $y_{1}^{(2,1)} = 180.0 + 260.0 = 440.0$
   - In Stratum 2: PSU 1 is deleted ($0$ weight). PSU 2 weight is doubled ($\times 2$):
     $x_{2}^{(2,1)} = 2 \times 140.0 = 280.0$
     $y_{2}^{(2,1)} = 2 \times 210.0 = 420.0$
   - Total Replicate 3:
     $$\hat{X}^{(2,1)} = 280.0 + 280.0 = 560.0$$
     $$\hat{Y}^{(2,1)} = 440.0 + 420.0 = 860.0$$

4. **Replicate $(2, 2)$ [Delete PSU 2 in Stratum 2]**:
   - In Stratum 1: Weights unchanged:
     $x_{1}^{(2,2)} = 280.0, \; y_{1}^{(2,2)} = 440.0$
   - In Stratum 2: PSU 2 is deleted ($0$ weight). PSU 1 weight is doubled ($\times 2$):
     $x_{2}^{(2,2)} = 2 \times 80.0 = 160.0$
     $y_{2}^{(2,2)} = 2 \times 110.0 = 220.0$
   - Total Replicate 4:
     $$\hat{X}^{(2,2)} = 280.0 + 160.0 = 440.0$$
     $$\hat{Y}^{(2,2)} = 440.0 + 220.0 = 660.0$$

**Solution, step 2: Computing replicate ratio estimates.**
Now compute the ratio estimate $\hat{R}^{(hj)} = \hat{Y}^{(hj)} / \hat{X}^{(hj)}$ for each replicate:
- Replicate $(1, 1)$:
  $$\hat{R}^{(1,1)} = \frac{840.0}{540.0} = \frac{14}{9} \approx 1.555556$$
- Replicate $(1, 2)$:
  $$\hat{R}^{(1,2)} = \frac{680.0}{460.0} = \frac{34}{23} \approx 1.478261$$
- Replicate $(2, 1)$:
  $$\hat{R}^{(2,1)} = \frac{860.0}{560.0} = \frac{43}{28} \approx 1.535714$$
- Replicate $(2, 2)$:
  $$\hat{R}^{(2,2)} = \frac{660.0}{440.0} = \frac{3}{2} = 1.500000$$

**Solution, step 3: Computing Jackknife variance and comparing with Taylor linearization.**
The delete-one-PSU Jackknife variance formula is:
$$\hat{V}_{JRR}(\hat{R}) = \sum_{h=1}^H \frac{n_h - 1}{n_h} \sum_{j=1}^{n_h} (\hat{R}^{(hj)} - \hat{R})^2$$
For $n_h = 2$, $\frac{n_h - 1}{n_h} = \frac{1}{2}$.
Therefore:
$$\hat{V}_{JRR}(\hat{R}) = \frac{1}{2} \left[ (\hat{R}^{(1,1)} - \hat{R})^2 + (\hat{R}^{(1,2)} - \hat{R})^2 \right] + \frac{1}{2} \left[ (\hat{R}^{(2,1)} - \hat{R})^2 + (\hat{R}^{(2,2)} - \hat{R})^2 \right]$$

Recall the full-sample estimate is $\hat{R} = 1.520000$.
Compute deviations from $\hat{R}$:
1. **Stratum 1 Replicates**:
   $$\hat{R}^{(1,1)} - \hat{R} = 1.555556 - 1.520000 = +0.035556$$
   Squared: $(+0.035556)^2 \approx 0.00126423$

   $$\hat{R}^{(1,2)} - \hat{R} = 1.478261 - 1.520000 = -0.041739$$
   Squared: $(-0.041739)^2 \approx 0.00174214$

   Stratum 1 Contribution:
   $$\text{JRR}_1 = \frac{1}{2} [0.00126423 + 0.00174214] = \frac{1}{2} [0.00300637] = 0.00150319$$

2. **Stratum 2 Replicates**:
   $$\hat{R}^{(2,1)} - \hat{R} = 1.535714 - 1.520000 = +0.015714$$
   Squared: $(+0.015714)^2 \approx 0.00024693$

   $$\hat{R}^{(2,2)} - \hat{R} = 1.500000 - 1.520000 = -0.020000$$
   Squared: $(-0.020000)^2 = 0.00040000$

   Stratum 2 Contribution:
   $$\text{JRR}_2 = \frac{1}{2} [0.00024693 + 0.00040000] = \frac{1}{2} [0.00064693] = 0.00032347$$

Summing both strata:
$$\hat{V}_{JRR}(\hat{R}) = \text{JRR}_1 + \text{JRR}_2 = 0.00150319 + 0.00032347 = 0.00182666$$

The standard error under Jackknife replication is:
$$\text{SE}_{JRR}(\hat{R}) = \sqrt{0.00182666} \approx 0.04274$$

**Comparison with Taylor Series Linearization**:
- Taylor Linearization: $\hat{V}_{linear} = 0.00178432$, $\text{SE}_{linear} = 0.04224$
- Jackknife Replication: $\hat{V}_{JRR} = 0.00182666$, $\text{SE}_{JRR} = 0.04274$
$$\frac{\hat{V}_{JRR}}{\hat{V}_{linear}} = \frac{0.00182666}{0.00178432} \approx 1.0237$$

The Jackknife variance is within $2.3\%$ of the Taylor linearization variance! This minor difference occurs because the Jackknife includes second-order curvature terms of the non-linear ratio function, whereas Taylor linearization truncates at first order. Both methods provide rigorous, design-consistent standard errors.

---

## Fully worked question 3: Domain Estimation for a Subpopulation and Unconditional Variance Penalty

**Question.** A national labor force survey draws a simple random sample without replacement (SRSWOR) of $n = 500$ individuals from a regional population of $N = 50,000$ working-age citizens ($f = 500 / 50,000 = 0.01$, so $1 - f = 0.99$).

The objective is to estimate the average hourly wage $\bar{Y}_d$ for a specific demographic domain $U_d$ (young tech workers aged 18–24). 
In the population, the proportion of individuals belonging to this domain is $P_d = N_d / N = 0.20$ ($N_d = 10,000$ workers).

The population parameters within the domain are:
- True domain mean wage: $\bar{Y}_d = 35.0 \text{ dollars/hour}$
- True domain variance: $S_d^2 = 100.0 \text{ (dollars/hour)}^2 \implies S_d = 10.0$

1. In a sample of $n = 500$, the observed domain sample count $n_d$ is a random variable. State the exact distribution and compute the expected value $E(n_d)$ and variance $V(n_d)$.
2. Calculate the **Conditional Variance** $V_{cond}(\hat{\bar{Y}}_d \mid n_d = 100)$ that a naive analyst would compute by assuming the sample size of 100 domain members was fixed prior to sampling.
3. Derive the **Unconditional Variance** $V_{uncond}(\hat{\bar{Y}}_d)$ accounting for the random sample size $n_d$. Compute the numerical variance, standard error, and the exact percentage variance penalty induced by the stochastic domain sample size.

**Solution, step 1: Distribution and moments of the domain sample size $n_d$.**
In SRSWOR of $n = 500$ from $N = 50,000$ with $N_d = 10,000$ domain members:
$n_d$ follows an exact Hypergeometric distribution:
$$n_d \sim \text{Hypergeometric}(N = 50,000, N_d = 10,000, n = 500)$$

1. **Expected Value**:
   $$E(n_d) = n \frac{N_d}{N} = n P_d = 500 \times 0.20 = 100 \text{ workers}$$

2. **Variance of $n_d$**:
   $$V(n_d) = n P_d (1 - P_d) \left( \frac{N - n}{N - 1} \right) = 500 \times 0.20 \times 0.80 \times \left( \frac{49,500}{49,999} \right)$$
   $$= 80.0 \times 0.99002 \approx 79.2016$$
   The standard deviation of the domain sample count is $\sigma(n_d) = \sqrt{79.2016} \approx 8.90$.
   In any given sample, the number of young tech workers could easily fluctuate between 82 and 118!

**Solution, step 2: Computing the conditional variance (fixed $n_d = 100$).**
If an analyst conditions on $n_d = 100$ (treating the 100 observed workers as if an SRSWOR of size 100 had been drawn directly from the domain population $N_d = 10,000$):
The conditional sampling fraction is $f_d = \frac{n_d}{N_d} = \frac{100}{10,000} = 0.01$, so $1 - f_d = 0.99$.

The conditional variance is:
$$V_{cond}(\hat{\bar{Y}}_d \mid n_d = 100) = \frac{1 - f_d}{n_d} S_d^2 = \frac{0.99}{100} \times 100.0 = 0.9900 \text{ (dollars/hour)}^2$$
The conditional standard error is:
$$\text{SE}_{cond} = \sqrt{0.9900} \approx 0.9950 \text{ dollars/hour}$$

**Solution, step 3: Deriving and computing the unconditional variance.**
Under design-based survey theory, the domain mean is a ratio estimator:
$$\hat{\bar{Y}}_d = \frac{\sum_{i \in s} I_{di} y_i}{\sum_{i \in s} I_{di}} = \frac{\hat{Y}_d}{\hat{N}_d} = \frac{\bar{y}_d^*}{\bar{I}_d}$$
where $y_i^* = I_{di} y_i$ is the synthetic zero-padded variable:
$$y_i^* = \begin{cases} y_i & \text{if } i \in U_d \\ 0 & \text{if } i \notin U_d \end{cases}$$

Using Taylor series linearization for the ratio of the two means $\bar{y}_d^*$ and $\bar{I}_d$:
$$\hat{\bar{Y}}_d - \bar{Y}_d \approx \frac{1}{P_d} (\bar{y}_d^* - \bar{Y}_d \bar{I}_d) = \frac{1}{P_d} \frac{1}{n} \sum_{i \in s} I_{di} (y_i - \bar{Y}_d)$$

Define the linearized variable:
$$u_i = I_{di} (y_i - \bar{Y}_d)$$
Notice that:
- For domain members ($i \in U_d$): $u_i = y_i - \bar{Y}_d$
- For non-domain members ($i \notin U_d$): $u_i = 0$

The population mean of $u_i$ across the entire population of $N$ units is:
$$\bar{U} = \frac{1}{N} \sum_{i \in U} u_i = \frac{1}{N} \left[ \sum_{i \in U_d} (y_i - \bar{Y}_d) + \sum_{i \notin U_d} 0 \right] = \frac{1}{N} [0 + 0] = 0$$

The population variance of $u_i$ across all $N$ units is:
$$S_u^2 = \frac{1}{N - 1} \sum_{i=1}^N (u_i - \bar{U})^2 \approx \frac{1}{N} \sum_{i \in U_d} (y_i - \bar{Y}_d)^2 = \frac{N_d}{N} \left( \frac{1}{N_d} \sum_{i \in U_d} (y_i - \bar{Y}_d)^2 \right) \approx P_d S_d^2$$

Now apply the standard SRSWOR variance formula to $\bar{u} = \frac{1}{n} \sum_{i \in s} u_i$:
$$V(\bar{u}) = \frac{1 - f}{n} S_u^2 \approx \frac{1 - f}{n} P_d S_d^2$$

Since $\hat{\bar{Y}}_d - \bar{Y}_d \approx \frac{1}{P_d} \bar{u}$:
$$V_{uncond}(\hat{\bar{Y}}_d) \approx \frac{1}{P_d^2} V(\bar{u}) \approx \frac{1}{P_d^2} \left( \frac{1 - f}{n} P_d S_d^2 \right) = \frac{1 - f}{n P_d} S_d^2$$

Notice the denominator: $n P_d = E(n_d) = 100$!
Now let us compute the exact second-order Taylor term. Cochran (1977) and Särndal, Swensson, and Wretman (1992) showed that when $n_d$ is random, conditioning on $n_d > 0$ yields:
$$E\left( \frac{1}{n_d} \right) \approx \frac{1}{n P_d} + \frac{1 - P_d}{n^2 P_d^2}$$

The exact unconditional variance of the domain mean is:
$$V_{uncond}(\hat{\bar{Y}}_d) \approx (1 - f) S_d^2 \left[ \frac{1}{n P_d} + \frac{1 - P_d}{n^2 P_d^2} \right]$$

Substitute our numerical parameters:
- $1 - f = 0.99$
- $S_d^2 = 100.0$
- $n P_d = 500 \times 0.20 = 100$
- $1 - P_d = 0.80$
- $n^2 P_d^2 = 100^2 = 10,000$

Compute the two terms inside the bracket:
$$\frac{1}{n P_d} = \frac{1}{100} = 0.01000$$
$$\frac{1 - P_d}{n^2 P_d^2} = \frac{0.80}{10,000} = 0.00008$$

Sum:
$$0.01000 + 0.00008 = 0.01008$$

Multiply by $(1 - f) S_d^2 = 0.99 \times 100.0 = 99.0$:
$$V_{uncond}(\hat{\bar{Y}}_d) \approx 99.0 \times 0.01008 = 0.99792 \text{ (dollars/hour)}^2$$

The unconditional standard error is:
$$\text{SE}_{uncond} = \sqrt{0.99792} \approx 0.99896 \text{ dollars/hour}$$

Now compare the unconditional variance with the conditional variance:
$$\Delta V = V_{uncond} - V_{cond} = 0.99792 - 0.99000 = 0.00792 \text{ (dollars/hour)}^2$$
$$\text{Penalty} = \frac{0.99792 - 0.99000}{0.99000} \times 100\% = \frac{0.00792}{0.99000} \times 100\% = +0.80\%$$

When the expected domain sample size is $E(n_d) = 100$, the stochastic fluctuation in $n_d$ adds a modest $0.80\%$ variance penalty.
However, consider what happens if the domain is small—for example, $P_d = 0.02$ ($E(n_d) = 10$ workers):
$$\frac{1 - P_d}{n P_d} = \frac{0.98}{10} = 0.098$$
For rare domains, the random sample size penalty inflates the variance by **nearly $10\%$**! This proves why subsetting datasets is mathematically indefensible in complex survey inference.

---

## Generalized Linear Models and Pseudo-Maximum Likelihood in Complex Surveys

In modern econometric, sociological, and epidemiological investigations, research questions frequently require fitting multivariate regression models—such as binary logistic regression for disease prevalence, Poisson or negative binomial regression for healthcare utilization counts, or Cox proportional hazards models for employment duration. 

In classical mathematical statistics, regression parameters $\boldsymbol{\beta}$ are estimated via Maximum Likelihood Estimation (MLE) under the assumption of independent and identically distributed (IID) observations. When data originate from a complex multistage survey with clustering, stratification, and unequal weights, standard maximum likelihood fails. To resolve this, David Binder (1983) formulated the foundational theory of **Pseudo-Maximum Likelihood Estimation (PMLE)**.

### The Census Likelihood and the Pseudo-Likelihood Estimator

Consider a finite population $U$ of $N$ units. Associated with unit $i$ is a response variable $y_i$ and a vector of explanatory covariates $\mathbf{x}_i$. Under a parametric model, the probability density or mass function of $y_i$ given $\mathbf{x}_i$ is $f(y_i \mid \mathbf{x}_i; \boldsymbol{\beta})$, where $\boldsymbol{\beta} = (\beta_1, \dots, \beta_p)^\top$ is a $p$-dimensional parameter vector.

If the statistician had access to the complete census of all $N$ units in the population, the **Census Log-Likelihood** would be:
$$\ell_{census}(\boldsymbol{\beta}) = \sum_{i=1}^N \log f(y_i \mid \mathbf{x}_i; \boldsymbol{\beta})$$
The true finite-population parameter $\mathbf{B}$ is the vector that maximizes the census log-likelihood, satisfying the **Census Score Equations**:
$$\mathbf{S}_{census}(\mathbf{B}) = \sum_{i=1}^N \mathbf{s}_i(\mathbf{B}) = \sum_{i=1}^N \frac{\partial \log f(y_i \mid \mathbf{x}_i; \mathbf{B})}{\partial \mathbf{B}} = \mathbf{0}$$

In a survey inquiry, we observe only a complex probability sample $s$ with analytic weights $w_i = d_i \times f_{nr,i} \times g_i$. The census score vector $\mathbf{S}_{census}(\boldsymbol{\beta})$ is a population total of the unit scores $\mathbf{s}_i(\boldsymbol{\beta})$.
Following the Horvitz–Thompson principle, we estimate this unknown population total by weighting the sample scores:
$$\hat{\mathbf{S}}_w(\boldsymbol{\beta}) = \sum_{i \in s} w_i \mathbf{s}_i(\boldsymbol{\beta}) = \sum_{i \in s} w_i \frac{\partial \log f(y_i \mid \mathbf{x}_i; \boldsymbol{\beta})}{\partial \boldsymbol{\beta}}$$

The **Pseudo-Maximum Likelihood Estimator (PMLE)** $\hat{\boldsymbol{\beta}}_w$ is the solution to the sample estimating equations:
$$\hat{\mathbf{S}}_w(\hat{\boldsymbol{\beta}}_w) = \mathbf{0}$$

### Binary Logistic Regression Example
Under a survey logistic regression model where $y_i \in \{0, 1\}$ and $P(y_i = 1 \mid \mathbf{x}_i) = \pi_i(\boldsymbol{\beta}) = \frac{1}{1 + \exp(-\mathbf{x}_i^\top \boldsymbol{\beta})}$:
The unit score vector is:
$$\mathbf{s}_i(\boldsymbol{\beta}) = \mathbf{x}_i (y_i - \pi_i(\boldsymbol{\beta}))$$
The sample pseudo-score equations are:
$$\sum_{i \in s} w_i \mathbf{x}_i \left[ y_i - \frac{1}{1 + \exp(-\mathbf{x}_i^\top \hat{\boldsymbol{\beta}}_w)} \right] = \mathbf{0}$$
These equations are solved numerically via survey-weighted Newton–Raphson iterations.

### Asymptotic Normality and the Sandwich (Godambe) Variance Estimator

To derive the sampling distribution of $\hat{\boldsymbol{\beta}}_w$, Binder deployed a first-order Taylor series expansion of the sample score equations around the true census parameter $\mathbf{B}$:
$$\mathbf{0} = \hat{\mathbf{S}}_w(\hat{\boldsymbol{\beta}}_w) \approx \hat{\mathbf{S}}_w(\mathbf{B}) + \left. \frac{\partial \hat{\mathbf{S}}_w}{\partial \boldsymbol{\beta}^\top} \right|_{\mathbf{B}} (\hat{\boldsymbol{\beta}}_w - \mathbf{B})$$

Solving for the estimation error:
$$\hat{\boldsymbol{\beta}}_w - \mathbf{B} \approx - \left[ \left. \frac{\partial \hat{\mathbf{S}}_w}{\partial \boldsymbol{\beta}^\top} \right|_{\mathbf{B}} \right]^{-1} \hat{\mathbf{S}}_w(\mathbf{B})$$

Define the sample weighted Hessian matrix (the empirical Fisher information):
$$\hat{\mathbf{J}}(\hat{\boldsymbol{\beta}}_w) = - \sum_{i \in s} w_i \frac{\partial^2 \log f(y_i \mid \mathbf{x}_i; \hat{\boldsymbol{\beta}}_w)}{\partial \boldsymbol{\beta} \partial \boldsymbol{\beta}^\top}$$
For logistic regression:
$$\hat{\mathbf{J}}(\hat{\boldsymbol{\beta}}_w) = \sum_{i \in s} w_i \hat{\pi}_i (1 - \hat{\pi}_i) \mathbf{x}_i \mathbf{x}_i^\top$$

Now evaluate the sampling variance. The sample score vector $\hat{\mathbf{S}}_w(\mathbf{B}) = \sum_{i \in s} w_i \mathbf{s}_i(\mathbf{B})$ is a linear total of the vectors $\mathbf{u}_i = \mathbf{s}_i(\mathbf{B})$.
Let $\hat{\boldsymbol{\Sigma}}_S$ denote the design-based variance-covariance matrix of $\hat{\mathbf{S}}_w$, computed under the complex multistage stratified design across all strata and PSUs:
$$\hat{\boldsymbol{\Sigma}}_S = \sum_{h=1}^H \frac{n_h}{n_h - 1} \sum_{i=1}^{n_h} (\mathbf{u}_{hi} - \bar{\mathbf{u}}_h)(\mathbf{u}_{hi} - \bar{\mathbf{u}}_h)^\top$$
where $\mathbf{u}_{hi} = \sum_{j \in \text{PSU}_{hi}} w_{hij} \mathbf{s}_{hij}(\hat{\boldsymbol{\beta}}_w)$ is the weighted score aggregate for PSU $i$ in stratum $h$.

This yields the celebrated **Sandwich Variance Estimator** (also known as the Godambe Information Matrix or Huber–White cluster-robust covariance matrix):
$$\hat{\mathbf{V}}(\hat{\boldsymbol{\beta}}_w) = \hat{\mathbf{J}}^{-1} \hat{\boldsymbol{\Sigma}}_S \hat{\mathbf{J}}^{-1}$$

#### Structural Architecture of the Sandwich:
- **The Bread ($\hat{\mathbf{J}}^{-1}$)**: The inverse of the information matrix, reflecting the curvature of the likelihood surface.
- **The Meat ($\hat{\boldsymbol{\Sigma}}_S$)**: The design-based variance of the score totals, capturing the true clustering, stratification, and unequal weighting of the multistage sample.

The sandwich covariance matrix guarantees that hypothesis tests and confidence intervals for regression coefficients are asymptotically valid and design-consistent, even when the underlying parametric distribution is misspecified.

---

## Hypothesis Testing under Complex Sampling: The Rao–Scott and Adjusted Wald Tests

When testing scientific hypotheses in complex survey data, classical test statistics must be modified to prevent catastrophic false-positive inflation.

### 1. The Adjusted Wald Test

Consider testing a general linear hypothesis on the regression coefficient vector:
$$H_0: \mathbf{C} \boldsymbol{\beta} = \mathbf{0} \quad \text{versus} \quad H_1: \mathbf{C} \boldsymbol{\beta} \ne \mathbf{0}$$
where $\mathbf{C}$ is a $q \times p$ matrix of linear contrast restrictions with $\text{rank}(\mathbf{C}) = q \le p$.

The standard Wald chi-square test statistic is:
$$W = (\mathbf{C} \hat{\boldsymbol{\beta}}_w)^\top \left[ \mathbf{C} \hat{\mathbf{V}}(\hat{\boldsymbol{\beta}}_w) \mathbf{C}^\top \right]^{-1} (\mathbf{C} \hat{\boldsymbol{\beta}}_w)$$

In classical infinite-sample theory, $W \sim \chi_q^2$. In complex surveys, however, the degrees of freedom are limited by the number of Primary Sampling Units:
$$d = \sum_{h=1}^H n_h - H$$

When $d$ is modest (e.g., $d \le 40$), the random noise in the estimated covariance matrix $\hat{\mathbf{V}}$ inflates the upper tail of the Wald statistic, causing classical chi-square critical values to over-reject the null hypothesis.

To correct for this, survey statisticians deploy the **Thomas–Rao and Korn–Graubard Adjusted $F$-Statistic**:
$$F_{adj} = \left( \frac{d - q + 1}{d \cdot q} \right) W$$
Under the null hypothesis, $F_{adj}$ follows an $F$-distribution with $q$ numerator degrees of freedom and $d - q + 1$ denominator degrees of freedom:
$$F_{adj} \sim F_{q, \; d - q + 1}$$

This degrees-of-freedom adjustment dampens test statistics, ensuring that the empirical Type I error rate matches the nominal significance level $\alpha = 0.05$.

### 2. The Rao–Scott Corrections for Categorical Contingency Tables

When analyzing two-way contingency tables (such as testing the association between smoking status and household poverty), the classical Pearson chi-square statistic:
$$X^2 = n \sum_{r=1}^R \sum_{c=1}^C \frac{(\hat{p}_{rc} - \hat{p}_{r\cdot} \hat{p}_{\cdot c})^2}{\hat{p}_{r\cdot} \hat{p}_{\cdot c}}$$
does not follow a central $\chi_{(R-1)(C-1)}^2$ distribution under complex sampling.

J. N. K. Rao and Alastair Scott (1981, 1984) proved that under $H_0$, $X^2$ is asymptotically distributed as a weighted sum of independent 1-degree-of-freedom chi-square variates:
$$X^2 \xrightarrow{d} \sum_{k=1}^{(R-1)(C-1)} \delta_k Z_k^2 \quad \text{where } Z_k \stackrel{\text{iid}}{\sim} \mathcal{N}(0, 1)$$
where $\delta_1, \dots, \delta_{(R-1)(C-1)}$ are the eigenvalues of a generalized design effect matrix $\boldsymbol{\Delta}$.

Rao and Scott derived two celebrated corrections:

1. **Rao–Scott First-Order Correction**:
   Divides the Pearson statistic by the mean eigenvalue $\bar{\delta} = \frac{1}{(R-1)(C-1)} \sum \delta_k$:
   $$X_{RS1}^2 = \frac{X^2}{\bar{\delta}}$$
   The mean eigenvalue $\bar{\delta}$ is easily computed as an average of univariate cell and marginal design effects, without requiring full covariance matrix inversion. $X_{RS1}^2$ is referred to a standard $\chi_{(R-1)(C-1)}^2$ distribution.

2. **Rao–Scott Second-Order (Satterthwaite) Correction**:
   Adjusts both the scale and the degrees of freedom to match the second moment of the distribution:
   $$X_{RS2}^2 = \frac{X^2}{\bar{\delta} (1 + a^2)}$$
   where $a^2 = \frac{1}{(R-1)(C-1)} \sum \left( \frac{\delta_k - \bar{\delta}}{\bar{\delta}} \right)^2$ is the squared coefficient of variation of the eigenvalues.
   The corrected degrees of freedom are:
   $$\nu = \frac{(R-1)(C-1)}{1 + a^2}$$
   $X_{RS2}^2$ is referred to an $F$-distribution with $\nu$ and $\nu \times d$ degrees of freedom.

The Rao–Scott corrections are the gold standard for categorical analysis in all major survey packages (R `survey::svychisq`, SAS `PROC SURVEYFREQ`, and Stata `svy: tabulate`).

---

## Small Area Estimation (SAE): Area-Level and Unit-Level Models

A pervasive challenge confronting modern statistical systems is the demand for reliable statistical indicators for small geographic domains (e.g., individual municipalities, school districts, health sub-districts) or detailed demographic domains. 

When national surveys are disaggregated to small local domains, direct design-based estimators—such as the domain Horvitz–Thompson estimator $\hat{\bar{Y}}_d$ analyzed in Section 8.4—suffer from small sample sizes ($n_d \le 10$) or empty sampling cells ($n_d = 0$). The direct sample variance is astronomically large, producing coefficients of variation exceeding $50\%$ or $100\%$, rendering direct survey estimates unusable for policy administration or resource allocation.

To overcome the sample size barrier, survey theory deploys **Small Area Estimation (SAE)** (Rao and Molina, 2015). Small area estimation resolves data sparsity by **"borrowing strength"** across related geographic areas and auxiliary administrative registers through statistical models.

### The Fay–Herriot Area-Level Model (1979)

The foundational model in small area estimation is the area-level linear mixed model formulated by Robert Fay and Roger Herriot (1979) to estimate per-capita income in small American municipalities with populations under 1,000.

Suppose there are $D$ small geographic areas in the country.
For each area $d \in \{1, 2, \dots, D\}$:
- $\theta_d$: The true, unobserved small area parameter (e.g., true area poverty rate or mean income).
- $\hat{\theta}_d$: The direct design-based survey estimate computed from the sample data.
- $\mathbf{x}_d = (x_{d1}, \dots, x_{dp})^\top$: A vector of area-level auxiliary covariates derived from national censuses, administrative tax registers, or satellite remote sensing.

The Fay–Herriot model decomposes the problem into two hierarchical stages:

1. **Sampling Model (Survey Measurement Error)**:
   $$\hat{\theta}_d = \theta_d + e_d \quad \text{where } e_d \stackrel{ind}{\sim} \mathcal{N}(0, \psi_d)$$
   where $\psi_d = V(\hat{\theta}_d \mid \theta_d)$ is the design-based sampling variance of the direct estimator in area $d$. In SAE practice, $\psi_d$ is treated as known, smoothed using generalized variance functions (GVF).

2. **Linking Model (Cross-Area Structural Law)**:
   $$\theta_d = \mathbf{x}_d^\top \boldsymbol{\beta} + u_d \quad \text{where } u_d \stackrel{iid}{\sim} \mathcal{N}(0, \sigma_u^2)$$
   where $\mathbf{x}_d^\top \boldsymbol{\beta}$ is the synthetic regression prediction based on auxiliary registers, $u_d$ is an area-specific random effect capturing unobserved local spatial heterogeneity, and $\sigma_u^2$ is the between-area variance.

Combining both stages yields the linear mixed model:
$$\hat{\theta}_d = \mathbf{x}_d^\top \boldsymbol{\beta} + u_d + e_d$$

### The Empirical Best Linear Unbiased Predictor (EBLUP)

Under this model, the **Best Linear Unbiased Predictor (BLUP)** of the small area parameter $\theta_d$ is a weighted compromise between the direct survey estimate and the synthetic regression prediction:
$$\tilde{\theta}_d = \gamma_d \hat{\theta}_d + (1 - \gamma_d) \mathbf{x}_d^\top \tilde{\boldsymbol{\beta}}$$
where:
$$\tilde{\boldsymbol{\beta}} = \left( \sum_{d=1}^D \frac{\mathbf{x}_d \mathbf{x}_d^\top}{\sigma_u^2 + \psi_d} \right)^{-1} \sum_{d=1}^D \frac{\mathbf{x}_d \hat{\theta}_d}{\sigma_u^2 + \psi_d}$$
and the shrinkage factor $\gamma_d \in [0, 1]$ is:
$$\gamma_d = \frac{\sigma_u^2}{\sigma_u^2 + \psi_d}$$

#### The Mechanics of Shrinkage:
The shrinkage factor $\gamma_d$ is the ratio of model variance to total variance:
- **Data-Rich Areas (Large $n_d$)**: When an area has a large survey sample, the direct sampling variance is tiny ($\psi_d \to 0$). Then $\gamma_d \to 1.0$. The EBLUP gives almost $100\%$ weight to the direct survey estimate $\hat{\theta}_d$, ignoring the regression model.
- **Data-Poor Areas (Tiny $n_d$)**: When an area has very few sampled units, direct sampling variance is huge ($\psi_d \gg \sigma_u^2$). Then $\gamma_d \to 0$. The EBLUP shrinks the direct estimate toward the stable synthetic regression prediction $\mathbf{x}_d^\top \tilde{\boldsymbol{\beta}}$.
- **Unsampled Areas ($n_d = 0$)**: If an area was completely omitted from the survey sample, $\psi_d = \infty \implies \gamma_d = 0$. The EBLUP automatically outputs the pure synthetic regression prediction:
  $$\tilde{\theta}_d = \mathbf{x}_d^\top \tilde{\boldsymbol{\beta}}$$

When the between-area variance $\sigma_u^2$ is unknown, it is estimated via Restricted Maximum Likelihood (REML) or Prasad–Rao moment estimation, yielding the **Empirical BLUP (EBLUP)**:
$$\hat{\theta}_d^{EBLUP} = \hat{\gamma}_d \hat{\theta}_d + (1 - \hat{\gamma}_d) \mathbf{x}_d^\top \hat{\boldsymbol{\beta}}$$

### Prasad–Rao Mean Squared Error Estimation

The Mean Squared Error of the EBLUP is decomposed into three distinct components:
$$\text{MSE}(\hat{\theta}_d^{EBLUP}) = g_{1d}(\hat{\sigma}_u^2) + g_{2d}(\hat{\sigma}_u^2) + 2 g_{3d}(\hat{\sigma}_u^2)$$
where:
- $g_{1d}(\sigma_u^2) = \gamma_d \psi_d = \frac{\sigma_u^2 \psi_d}{\sigma_u^2 + \psi_d}$ accounts for the primary shrinkage variance.
- $g_{2d}(\sigma_u^2) = (1 - \gamma_d)^2 \mathbf{x}_d^\top \left[ \sum \frac{\mathbf{x}_k \mathbf{x}_k^\top}{\sigma_u^2 + \psi_k} \right]^{-1} \mathbf{x}_d$ accounts for the uncertainty in estimating the regression slope vector $\boldsymbol{\beta}$.
- $g_{3d}(\sigma_u^2)$ is a second-order term accounting for the uncertainty in estimating the variance component $\sigma_u^2$.

Prasad and Rao (1990) proved that this MSE estimator is strictly unbiased to order $O(1/D)$, providing honest, defensible confidence intervals for local municipal estimates.

---

## Practical Synthesis: Survey Quality Reporting Standards

To ensure that secondary analysts and public policymakers interpret empirical survey results correctly, international statistical bodies (such as the United Nations Statistics Division, Eurostat, and the U.S. Federal Committee on Statistical Methodology) mandate standardized technical documentation.

### The Five Pillars of Survey Microdata Documentation:
1. **Analytic Weight Documentation**: Transparent explanation of how base design weights $d_i$, nonresponse adjustments $f_{nr,i}$, and calibration factors $g_i$ were derived, accompanied by summary distributions (mean, min, max, coefficient of variation).
2. **Design Variable Provision**: Inclusion of masked stratum identifiers (`STRATA`) and masked primary sampling unit identifiers (`PSU`) in public-use microdata files. Masking scrambles geographical names to prevent deductive respondent disclosure while strictly preserving the variance-covariance matrix.
3. **Replicate Weights**: In many public-use datasets (such as the American Community Survey or the Current Population Survey), agencies provide 80 to 160 pre-calculated Jackknife or BRR replicate weight columns (`REPWT1` through `REPWT80`). Replicate weights enable users to compute exact complex survey standard errors without needing access to sensitive geographical cluster identifiers.
4. **Design Degrees of Freedom Reporting**: Explicit statement of design degrees of freedom ($\text{df} = \sum n_h - H$) to guide hypothesis testing and small-sample $t$-approximations.
5. **Quality Flags and Imputation Indicators**: Every imputed item must be accompanied by an imputation flag variable (`ITEM_FLG`) distinguishing observed empirical values from imputed synthetic values, empowering researchers to conduct sensitivity audits.

With this rigorous synthesis of complex survey inference, we conclude the theoretical and computational architecture of *Sample Surveys and Sampling Theory*.
