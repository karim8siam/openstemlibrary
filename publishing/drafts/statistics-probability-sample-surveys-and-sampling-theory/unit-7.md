# Unit 7: Survey Nonresponse, Imputation and Total Survey Error

## The Reality of Nonresponse in Contemporary Survey Research

In the classical mathematical formulations of survey sampling theory developed by Neyman, Cochran, and Hansen, the statistical investigator selects a probability sample $s$ and measures the survey attributes for every sampled element without error. In modern empirical science, this pristine assumption has completely collapsed. Across the globe, statistical agencies, academic survey centers, and private opinion research institutes are confronting a profound, secular decline in public participation. Response rates in random-digit-dial (RDD) telephone surveys in North America and Western Europe have plunged from over $80\%$ in the 1970s to below $10\%$ today. In face-to-face national household surveys, escalating urbanization, gated communities, heightened privacy sensitivities, and hectic work schedules have driven nonresponse rates to between $25\%$ and $50\%$.

When selected sample units fail to provide data, the integrity of the randomized sampling design is compromised. Nonresponse destroys the known mathematical inclusion probabilities established at the design stage. In survey terminology, nonresponse manifests in two distinct operational forms:

1. **Unit Nonresponse**: The designated sampling unit (such as a household, individual, or business enterprise) is completely absent from the final dataset. Unit nonresponse arises from three distinct field mechanisms:
   - **Non-Contact**: Field interviewers fail to establish physical or telephonic contact with any adult household member despite repeated, randomized contact attempts across different days of the week and times of day.
   - **Refusal**: Contact is successfully established, but the sampled individual declines to participate due to survey burden, lack of interest, skepticism regarding institutional confidentiality, or general hostility toward research inquiries.
   - **Inability / Incapacity**: The sampled unit cannot complete the interview due to acute physical or cognitive illness, severe language barriers, mental impairment, or geographic inaccessibility (such as seasonal flooding or conflict zones).

2. **Item Nonresponse**: The sampled unit agrees to participate and completes the bulk of the survey instrument, but specific individual survey items are left blank. Item nonresponse occurs when respondents find a question intrusive or sensitive (such as personal income, sexual behavior, substance use, or political affiliations), when they genuinely do not know the answer (such as detailed annual energy expenditures or corporate depreciation allowances), or when interviewers accidentally skip a questionnaire module.

### Response Rates versus Nonresponse Bias: The Groves Paradox

A widespread misconception among naive survey practitioners and the popular media is that a low response rate automatically invalidates a survey, while a high response rate guarantees statistical accuracy. In a landmark meta-analysis of nonresponse experiments, Robert Groves (2006) proved that the empirical correlation between the nonresponse rate and the nonresponse bias across hundreds of survey estimates is virtually zero ($r \approx 0.10$). 

A survey with an $80\%$ response rate can suffer from catastrophic nonresponse bias if the $20\%$ non-respondents are concentrated in an extreme tail of the distribution (e.g., millionaires refusing to report wealth). Conversely, a survey with a $20\%$ response rate can produce near-zero nonresponse bias if the probability of participation is completely uncorrelated with the substantive survey variables. Nonresponse bias is governed not simply by the nonresponse rate itself, but by the mathematical covariance between the propensity to participate and the survey variable of interest.

---

## Missing Data Mechanisms in Survey Sampling: Rubin's Taxonomy

To formalize the mathematical analysis of nonresponse, survey theory adopts the classical missing data taxonomy formulated by Donald Rubin (1976). 

Let $U = \{1, 2, \dots, N\}$ denote the finite population. Attached to each unit $i$ is:
- $y_i$: The target survey characteristic.
- $\mathbf{x}_i = (x_{i1}, \dots, x_{ip})^\top$: A vector of auxiliary characteristics available for all units in the selected sample (derived from the sampling frame, geographical databases, or field observations).
- $R_i$: A binary response indicator variable:
  $$R_i = \begin{cases} 1 & \text{if unit } i \text{ responds when sampled} \\ 0 & \text{if unit } i \text{ fails to respond} \end{cases}$$

The joint distribution of the data and the response mechanism determines the inferential validity of post-survey adjustments:

### 1. Missing Completely at Random (MCAR)
Under Missing Completely at Random, the probability of response is completely independent of both observed auxiliary covariates $\mathbf{x}$ and the unobserved survey variable $y$:
$$P(R_i = 1 \mid y_i, \mathbf{x}_i) = P(R_i = 1) = \bar{R}$$

Under MCAR, the subset of responding units $s_r = \{i \in s : R_i = 1\}$ represents an unskewed, miniature simple random sub-sample of the original sample $s$. 
- **Consequences**: Unweighted respondent sample means $\bar{y}_r = \frac{1}{n_r} \sum_{i \in s_r} y_i$ remain strictly design-unbiased for the population mean $\bar{Y}$.
- **Penalty**: The only loss is statistical precision: because the sample size is reduced from $n$ to $n_r$, the sampling variance increases by the factor $n / n_r = 1 / \bar{R}$.
- **Empirical Reality**: In practical human and economic surveys, true MCAR almost never holds.

### 2. Missing at Random (MAR)
Under Missing at Random, the probability of response depends upon observed auxiliary characteristics $\mathbf{x}$, but conditional on those observed covariates, response is completely independent of the unobserved survey variable $y$:
$$P(R_i = 1 \mid y_i, \mathbf{x}_i) = P(R_i = 1 \mid \mathbf{x}_i) = \phi(\mathbf{x}_i)$$

For example, younger adults and highly educated urban professionals may have systematically lower response propensities than retired rural residents. If age, education, and geography are fully recorded on the sampling frame or collected during household screening, and if conditional on those three variables, a responding young adult has the same expected income as a non-responding young adult, then the missing data mechanism is MAR.
- **Consequences**: The naive respondent mean $\bar{y}_r$ is systematically biased. However, because the response mechanism is fully explained by observable covariates $\mathbf{x}$, the nonresponse bias can be **completely eliminated** through weighting class adjustments, propensity score weighting, calibration, or regression imputation.
- MAR is the foundational assumption underlying all standard post-survey nonresponse adjustments.

### 3. Missing Not at Random (MNAR / Non-Ignorable Nonresponse)
Under Missing Not at Random, the probability of response depends directly on the unobserved survey variable $y$ itself, even after conditioning on all available auxiliary covariates $\mathbf{x}$:
$$P(R_i = 1 \mid y_i, \mathbf{x}_i) \ne P(R_i = 1 \mid \mathbf{x}_i)$$

For example, in a survey of household wealth, ultra-high-net-worth individuals refuse to disclose financial assets specifically because of privacy concerns regarding their extreme wealth, even when comparing individuals of the exact same age, education, and neighborhood. Similarly, in an epidemiological survey of alcohol consumption, heavy binge drinkers systematically avoid participation because of social stigma.
- **Consequences**: Standard weighting adjustments and imputation models fail to eliminate nonresponse bias. Standard estimators remain biased regardless of sample size. Resolving MNAR requires explicit structural econometric selection models (such as the Heckman two-step selection model) or formal pattern-mixture sensitivity bounds.

---

## Mathematical Derivation of Nonresponse Bias

Survey statisticians analyze nonresponse bias through two complementary mathematical models: the deterministic two-stratum model and the stochastic response propensity model.

### 1. The Deterministic Two-Stratum Model

In the deterministic formulation (Cochran, 1977), the finite population $U$ of $N$ units is partitioned into two fixed, unobserved sub-populations:
- The **Response Stratum** $U_R$ of size $N_R$, containing units that would respond with certainty if sampled.
- The **Nonresponse Stratum** $U_M$ of size $N_M$, containing units that would refuse or evade observation if sampled.

Let $W_R = \frac{N_R}{N}$ and $W_M = \frac{N_M}{N}$ denote the population response and nonresponse proportions ($W_R + W_M = 1$).
Let $\bar{Y}_R$ and $\bar{Y}_M$ denote the true finite-population means in the response and nonresponse strata, respectively.

The overall finite-population mean $\bar{Y}$ is the weighted average of the two strata:
$$\bar{Y} = W_R \bar{Y}_R + W_M \bar{Y}_M$$

When a probability sample is drawn, data are collected exclusively from the responding units, yielding the respondent sample mean $\bar{y}_r$, which has expectation $E(\bar{y}_r) = \bar{Y}_R$.

The nonresponse bias of the respondent mean is:
$$\text{Bias}(\bar{y}_r) = E(\bar{y}_r) - \bar{Y} = \bar{Y}_R - (W_R \bar{Y}_R + W_M \bar{Y}_M) = (1 - W_R) \bar{Y}_R - W_M \bar{Y}_M$$
Since $1 - W_R = W_M$:
$$\text{Bias}(\bar{y}_r) = W_M (\bar{Y}_R - \bar{Y}_M) = \frac{N_M}{N} (\bar{Y}_R - \bar{Y}_M)$$

#### Decomposition of the Bias:
This classical identity proves that nonresponse bias is the exact mathematical product of two distinct structural components:
1. **The Nonresponse Rate ($W_M$)**: The fraction of the population that fails to respond.
2. **The Substantive Contrast ($\bar{Y}_R - \bar{Y}_M$)**: The difference in the true mean between respondents and non-respondents.

If the nonresponse rate $W_M$ is large (e.g., $W_M = 0.50$), but the non-respondents have the exact same mean as the respondents ($\bar{Y}_R - \bar{Y}_M = 0$), the bias is identically zero! Conversely, even if the nonresponse rate is modest ($W_M = 0.10$), an extreme contrast between respondents and non-respondents (such as rare disease prevalence) will induce substantial bias.

### 2. The Stochastic Response Propensity Model (Bethlehem's Theory)

In modern survey methodology, deterministic participation is replaced by the more realistic stochastic response model developed by Jelke Bethlehem (1988). Each unit $i \in U$ is assumed to possess an intrinsic, latent response propensity $\rho_i \in (0, 1]$.

When unit $i$ is sampled ($I_i = 1$), an independent Bernoulli trial is conducted with success probability:
$$P(R_i = 1 \mid I_i = 1) = \rho_i$$

Under this two-phase randomization mechanism (Phase 1: sample selection $I_i$; Phase 2: response trial $R_i$), the observed respondent sample mean is:
$$\bar{y}_r = \frac{\sum_{i=1}^N I_i R_i y_i}{\sum_{i=1}^N I_i R_i}$$

Taking expectations over the response mechanism conditional on the sample, and then over the sampling design:
$$E(\bar{y}_r) \approx \frac{\sum_{i=1}^N \rho_i y_i}{\sum_{i=1}^N \rho_i} = \frac{\frac{1}{N} \sum_{i=1}^N \rho_i y_i}{\bar{\rho}}$$
where $\bar{\rho} = \frac{1}{N} \sum_{i=1}^N \rho_i$ is the average response propensity across the entire population.

Now evaluate the covariance between the response propensities $\boldsymbol{\rho}$ and the survey characteristic $\mathbf{y}$:
$$S_{\rho y} = \frac{1}{N - 1} \sum_{i=1}^N (\rho_i - \bar{\rho})(y_i - \bar{Y}) \approx \frac{1}{N} \sum_{i=1}^N \rho_i y_i - \bar{\rho} \bar{Y}$$

Solving for the numerator term:
$$\frac{1}{N} \sum_{i=1}^N \rho_i y_i \approx \bar{\rho} \bar{Y} + S_{\rho y}$$

Substituting this into the expectation of $\bar{y}_r$:
$$E(\bar{y}_r) \approx \frac{\bar{\rho} \bar{Y} + S_{\rho y}}{\bar{\rho}} = \bar{Y} + \frac{S_{\rho y}}{\bar{\rho}}$$

Therefore, Bethlehem's fundamental **Nonresponse Bias Formula** is:
$$\text{Bias}(\bar{y}_r) \approx \frac{S_{\rho y}}{\bar{\rho}} = \frac{\text{Cov}(\rho, Y)}{\bar{\rho}}$$

Using the definition of the correlation coefficient $\rho_{\rho y} = \frac{S_{\rho y}}{S_\rho S_y}$:
$$\text{Bias}(\bar{y}_r) \approx \frac{\rho_{\rho y} S_\rho S_y}{\bar{\rho}} = \rho_{\rho y} \left( \frac{S_\rho}{\bar{\rho}} \right) S_y = \rho_{\rho y} C_\rho S_y$$
where $C_\rho = S_\rho / \bar{\rho}$ is the coefficient of variation of the response propensities.

#### Deep Insights from Bethlehem's Formulation:
1. **The Three Drivers of Bias**: Nonresponse bias is the direct product of:
   - The correlation between response propensity and the survey variable ($\rho_{\rho y}$).
   - The relative dispersion of response propensities across the population ($C_\rho = S_\rho / \bar{\rho}$).
   - The population standard deviation of the survey variable ($S_y$).
2. **Zero Bias Conditions**: Nonresponse bias vanishes if and only if either:
   - $\rho_{\rho y} = 0$: Participation is uncorrelated with the survey attribute (MCAR).
   - $S_\rho = 0$: Every unit in the population has the exact same response propensity ($\rho_i = \bar{\rho}$ for all $i$).
3. **The Danger of Uniform Nonresponse Chasing**: If an agency spends massive field resources converting easy refusals while neglecting hard refusals, it may inflate the average response rate $\bar{\rho}$ while simultaneously widening the variance $S_\rho^2$, potentially **increasing** nonresponse bias despite achieving a higher headline response rate!

---

## Unit Nonresponse Adjustment Strategies

To eliminate or mitigate nonresponse bias under the MAR assumption, survey statisticians modify the survey weights. The final nonresponse-adjusted weight $w_i^*$ for respondent $i$ is constructed by multiplying the initial design weight $d_i = 1 / \pi_i$ by a nonresponse adjustment factor $f_{nr,i}$:
$$w_i^* = d_i \times f_{nr,i}$$

Two primary methodologies govern the construction of $f_{nr,i}$:

### 1. Weighting Class Adjustments

In the weighting class methodology (Little, 1986), the sample is partitioned into $C$ mutually exclusive and collectively exhaustive adjustment cells (or classes) based on auxiliary frame variables $\mathbf{x}$ (e.g., age-by-sex-by-region cells).

Let $s_c$ denote the set of all sampled units belonging to cell $c$, and let $s_{r,c}$ denote the responding units in cell $c$.
Let:
$$n_c = \sum_{i \in s_c} 1 \quad \text{and} \quad n_{r,c} = \sum_{i \in s_{r,c}} 1$$
denote the total sample size and responding sample size in cell $c$.

The design-weighted sample counts are:
$$\hat{N}_c = \sum_{i \in s_c} d_i \quad \text{and} \quad \hat{N}_{r,c} = \sum_{i \in s_{r,c}} d_i$$

The estimated response rate in cell $c$ is:
$$\hat{\phi}_c = \frac{\hat{N}_{r,c}}{\hat{N}_c}$$

The **Weighting Class Adjustment Factor** for every respondent in cell $c$ is:
$$f_{nr,c} = \frac{1}{\hat{\phi}_c} = \frac{\hat{N}_c}{\hat{N}_{r,c}}$$

The nonresponse-adjusted weight for unit $i \in s_{r,c}$ is:
$$w_i^* = d_i \times \frac{1}{\hat{\phi}_c} = d_i \frac{\hat{N}_c}{\hat{N}_{r,c}}$$

Notice that summing the adjusted weights of respondents in cell $c$ reproduces the original design-weighted total for that cell:
$$\sum_{i \in s_{r,c}} w_i^* = \sum_{i \in s_{r,c}} d_i \frac{\hat{N}_c}{\hat{N}_{r,c}} = \hat{N}_c \left( \frac{\sum_{i \in s_{r,c}} d_i}{\hat{N}_{r,c}} \right) = \hat{N}_c$$
Weighting class adjustments redistribute the weight of non-respondents onto the respondents within the exact same adjustment cell.

#### Condition for Unbiasedness:
The weighting class estimator is design-unbiased if the MAR assumption holds within each cell: conditional on cell membership $c$, the response indicator $R_i$ is completely independent of the survey variable $y_i$.

### 2. Propensity Score Weighting (Inverse Propensity Weighting - IPW)

When the auxiliary vector $\mathbf{x}$ is high-dimensional or contains continuous covariates, creating discrete weighting cells causes cell counts to dwindle, producing unstable estimates. Rosenbaum and Rubin (1983) and David, Little, Samuhel, and Triest (1983) proposed estimating individual response propensities via parametric modeling.

A binary logistic regression model is fitted on the full selected sample $s$:
$$\text{logit}(\hat{\rho}_i) = \log\left( \frac{\hat{\rho}_i}{1 - \hat{\rho}_i} \right) = \mathbf{x}_i^\top \hat{\boldsymbol{\gamma}}$$
where the binary outcome is the response indicator $R_i \in \{0, 1\}$.

The estimated response propensity for respondent $i$ is:
$$\hat{\rho}_i = \frac{1}{1 + \exp(-\mathbf{x}_i^\top \hat{\boldsymbol{\gamma}})}$$

Under **Inverse Propensity Weighting (IPW)**, the nonresponse adjustment factor is the inverse of the predicted response propensity:
$$f_{nr,i} = \frac{1}{\hat{\rho}_i} \implies w_i^* = d_i \times \frac{1}{\hat{\rho}_i}$$

The IPW estimator of the population total is:
$$\hat{Y}_{IPW} = \sum_{i \in s_r} w_i^* y_i = \sum_{i \in s_r} \frac{d_i}{\hat{\rho}_i} y_i$$

#### Weight Trimming:
If any sampled respondent has an estimated propensity $\hat{\rho}_i$ very close to zero (e.g., $\hat{\rho}_i = 0.01$), its weight multiplier $1 / \hat{\rho}_i = 100$ explodes, inflating sampling variance. Survey practitioners apply **weight trimming**, capping $f_{nr,i}$ at an upper threshold (e.g., $f_{nr,max} = 3.0$ or $5.0$) and redistributing the trimmed weight across the remaining cases.

---

## Item Nonresponse and Imputation Techniques

While unit nonresponse is addressed by reweighting the responding records, **item nonresponse** cannot be solved by reweighting. If a respondent answers 95 questions on a 100-question instrument, discarding the entire record via listwise deletion (complete-case analysis) discards massive amounts of valid data, slashes effective sample size, and introduces severe nonresponse bias if item missingness is not MCAR.

Instead, statistical agencies handle item nonresponse through **imputation**—the process of replacing missing item values with synthetic, mathematically plausible values.

### Classical Imputation Paradigms:

1. **Deductive / Logical Imputation**:
   Using logical consistency constraints or deterministic structural relationships to deduce the missing value with absolute certainty. For example, if a respondent leaves "Spouse's Age" blank, but reports in a marital module that the spouse was born in March 1980, the missing age is deduced deterministically.

2. **Mean / Median Imputation**:
   Replacing missing values within an imputation class with the class sample mean $\bar{y}_{obs}$.
   - **Fatal Flaw**: Mean imputation artificially spikes the empirical distribution at a single point, destroying the variance:
     $$\hat{S}_{imp}^2 = \frac{n_{obs} - 1}{n - 1} s_{obs}^2 < s_{obs}^2$$
     Mean imputation severely underestimates the true population variance, artificially suppresses standard errors, and distorts covariance structures with other variables. It should never be used in scientific practice.

3. **Hot-Deck Imputation**:
   A foundational method in official statistics (pioneered by the U.S. Census Bureau). For each non-respondent record requiring imputation ("recipient"), an observed respondent record ("donor") that matches the recipient on a set of conditioning variables (imputation classes) is identified. The donor's observed value $y_{donor}$ is copied directly into the recipient's missing field.
   - **Advantages**: Preserves the realistic multivariate distribution and ensures that imputed values conform to valid physical domain bounds (e.g., whole integer counts, valid categorical codes).

4. **Deterministic versus Stochastic Regression Imputation**:
   A regression model is fitted on the observed respondents: $\hat{y}_i = \mathbf{x}_i^\top \hat{\boldsymbol{\beta}}$.
   - **Deterministic Regression Imputation**: Imputes the exact conditional fitted value:
     $$y_i^* = \mathbf{x}_i^\top \hat{\boldsymbol{\beta}}$$
     This artificially inflates the correlation between $y$ and $\mathbf{x}$, while underestimating the residual variance because the error term $\varepsilon_i$ is omitted.
   - **Stochastic Regression Imputation**: Adds a randomly drawn residual to the fitted value:
     $$y_i^* = \mathbf{x}_i^\top \hat{\boldsymbol{\beta}} + e_i^* \quad \text{where } e_i^* \sim N(0, s_e^2)$$
     Stochastic regression imputation restores natural statistical dispersion and preserves the true underlying covariance structure.

---

## Multiple Imputation and Rubin's Combining Rules

Even when stochastic regression or hot-deck imputation is deployed, **single imputation** suffers from a fundamental mathematical flaw: Standard statistical software packages treat the imputed values as if they were true, known observations collected from actual interviews. 

By pretending that imputed values are real data, single imputation fails to account for **imputation uncertainty**—the inevitable statistical noise arising because the missing values are unknown predictions rather than empirical facts. Consequently, single imputation produces standard errors that are falsely small, test statistics that are falsely inflated, and confidence intervals that fail to achieve their nominal coverage rates.

### The Multiple Imputation (MI) Framework

To solve this problem, Donald Rubin (1987) developed **Multiple Imputation**. Instead of creating a single completed dataset, the statistician generates $M$ independent completed datasets ($M \ge 5$ in classical practice, and $M \ge 20$ in modern high-precision applications).

The Multiple Imputation procedure follows three distinct phases:
1. **Imputation Phase**: Draw $M$ independent sets of imputed values from the posterior predictive distribution of the missing data given the observed data $P(Y_{mis} \mid Y_{obs}, \mathbf{X})$, generating $M$ distinct completed datasets: $\mathcal{D}^{(1)}, \mathcal{D}^{(2)}, \dots, \mathcal{D}^{(M)}$.
2. **Analysis Phase**: Apply the desired statistical analysis (e.g., mean estimation, regression, odds ratio calculation) separately to each of the $M$ completed datasets using standard complete-data methods. This produces $M$ point estimates $\hat{Q}^{(m)}$ and $M$ corresponding variance estimates $\hat{U}^{(m)}$ ($m = 1, 2, \dots, M$).
3. **Pooling Phase**: Combine the $M$ individual estimates into a single overall point estimate and an honest total variance estimate using **Rubin's Combining Rules**.

### Rubin's Combining Rules

Let $\hat{Q}^{(m)}$ denote the point estimate of a scalar parameter $Q$ from dataset $m$, and let $\hat{U}^{(m)}$ denote its estimated sampling variance.

1. **Overall Combined Point Estimate**:
   $$\bar{Q}_M = \frac{1}{M} \sum_{m=1}^M \hat{Q}^{(m)}$$

2. **Within-Imputation Variance ($\bar{U}_M$)**:
   The average of the $M$ sampling variance estimates:
   $$\bar{U}_M = \frac{1}{M} \sum_{m=1}^M \hat{U}^{(m)}$$
   This represents ordinary sampling variability due to collecting a finite sample of size $n$.

3. **Between-Imputation Variance ($B_M$)**:
   The sample variance among the $M$ point estimates:
   $$B_M = \frac{1}{M - 1} \sum_{m=1}^M (\hat{Q}^{(m)} - \bar{Q}_M)^2$$
   This represents the additional uncertainty introduced by the missing data and the imputation process.

4. **Total Variance ($T_M$)**:
   The total variance of the combined estimator $\bar{Q}_M$ is:
   $$T_M = \bar{U}_M + \left( 1 + \frac{1}{M} \right) B_M$$
   The term $\frac{1}{M} B_M$ is a finite-imputation correction factor accounting for the fact that $M$ is finite rather than infinite.

5. **Fraction of Missing Information (FMI)**:
   The relative increase in variance due to nonresponse is:
   $$r_M = \frac{(1 + 1/M) B_M}{\bar{U}_M}$$
   The estimated Fraction of Missing Information is:
   $$\hat{\lambda}_M = \frac{r_M + 2/(\nu + 3)}{1 + r_M} \approx \frac{(1 + 1/M) B_M}{T_M}$$

6. **Degrees of Freedom for Inference**:
   Hypothesis tests and confidence intervals are computed using the Student's $t$-distribution:
   $$\frac{\bar{Q}_M - Q}{\sqrt{T_M}} \sim t_{\nu}$$
   where the degrees of freedom $\nu$ are given by the Barnard–Rubin (1999) formula:
   $$\nu = \frac{\nu_{old} \nu_{obs}}{\nu_{old} + \nu_{obs}}$$
   where $\nu_{old} = (M - 1)(1 + r_M^{-1})^2$ and $\nu_{obs} = \frac{\nu_0 + 1}{\nu_0 + 3} \nu_0 (1 - \hat{\lambda}_M)$, and $\nu_0$ is the complete-data degrees of freedom.

---

## Fully worked question 1: Mathematical Derivation of Nonresponse Bias Under Stochastic Response Propensities

**Question.** A national socioeconomic survey of $N = 3,000$ households is conducted in an urban center to estimate average monthly household income (in dollars). The population is composed of three distinct socioeconomic strata:

$$\begin{array}{c|cccc}
\text{Stratum } h & \text{Households } (N_h) & \text{Mean Income } (\bar{Y}_h) & \text{Response Propensity } (\rho_h) \\
\hline
1 \text{ (Low Income)} & 1,500 & 1,200 & 0.80 \\
2 \text{ (Middle Income)} & 1,000 & 2,500 & 0.60 \\
3 \text{ (High Income)} & 500 & 6,000 & 0.30 \\
\hline
\text{Total Population} & N = 3,000 & &
\end{array}$$

Within each stratum, all households share the exact same response propensity $\rho_h$, and individual household income has negligible within-stratum variance ($S_{h}^2 \approx 0$). An equal-probability sample is drawn across the population.

1. Compute the true finite-population mean income $\bar{Y}$ and the overall average population response propensity $\bar{\rho}$.
2. Using Bethlehem's theoretical formula:
   - Compute the population covariance $S_{\rho y}$ between response propensity and household income.
   - Derive the expected value of the unweighted respondent sample mean $E(\bar{y}_r)$.
   - Calculate the exact nonresponse bias $\text{Bias}(\bar{y}_r)$ and the percentage relative bias.
3. If the survey agency applies weighting class adjustments using the three strata as adjustment cells, prove mathematically and numerically that the nonresponse bias is reduced to exactly zero.

**Solution, step 1: Computing true population mean income and average response propensity.**
Given:
- Stratum 1: $N_1 = 1,500$, proportion $W_1 = 1,500 / 3,000 = 0.50$, $\bar{Y}_1 = 1,200$, $\rho_1 = 0.80$
- Stratum 2: $N_2 = 1,000$, proportion $W_2 = 1,000 / 3,000 = 1/3 \approx 0.333333$, $\bar{Y}_2 = 2,500$, $\rho_2 = 0.60$
- Stratum 3: $N_3 = 500$, proportion $W_3 = 500 / 3,000 = 1/6 \approx 0.166667$, $\bar{Y}_3 = 6,000$, $\rho_3 = 0.30$

1. **True Population Mean Income ($\bar{Y}$)**:
   $$\bar{Y} = \sum_{h=1}^3 W_h \bar{Y}_h = 0.50(1,200) + \frac{1}{3}(2,500) + \frac{1}{6}(6,000)$$
   $$= 600 + 833.3333 + 1,000 = 2,433.3333 \text{ dollars}$$

2. **Average Population Response Propensity ($\bar{\rho}$)**:
   $$\bar{\rho} = \sum_{h=1}^3 W_h \rho_h = 0.50(0.80) + \frac{1}{3}(0.60) + \frac{1}{6}(0.30)$$
   $$= 0.40 + 0.20 + 0.05 = 0.650$$
   On average, $65\%$ of the sampled households will participate in the survey.

**Solution, step 2: Computing covariance, expected respondent mean, and nonresponse bias.**
1. **Population Covariance $S_{\rho y}$**:
   Using the definition:
   $$S_{\rho y} \approx \sum_{h=1}^3 W_h (\rho_h - \bar{\rho})(\bar{Y}_h - \bar{Y})$$

   Compute stratum deviations:
   - Stratum 1:
     $\rho_1 - \bar{\rho} = 0.80 - 0.65 = +0.15$
     $\bar{Y}_1 - \bar{Y} = 1,200 - 2,433.3333 = -1,233.3333$
     Product term: $0.50 \times (+0.15) \times (-1,233.3333) = 0.075 \times (-1,233.3333) = -92.50$
   - Stratum 2:
     $\rho_2 - \bar{\rho} = 0.60 - 0.65 = -0.05$
     $\bar{Y}_2 - \bar{Y} = 2,500 - 2,433.3333 = +66.6667$
     Product term: $\frac{1}{3} \times (-0.05) \times (+66.6667) = -0.016667 \times 66.6667 = -1.1111$
   - Stratum 3:
     $\rho_3 - \bar{\rho} = 0.30 - 0.65 = -0.35$
     $\bar{Y}_3 - \bar{Y} = 6,000 - 2,433.3333 = +3,566.6667$
     Product term: $\frac{1}{6} \times (-0.35) \times (+3,566.6667) = -0.058333 \times 3,566.6667 = -208.0556$

   Summing all three terms:
   $$S_{\rho y} = -92.50 - 1.1111 - 208.0556 = -301.6667$$
   Notice that the covariance is strongly **negative**: households with higher incomes have substantially lower response propensities.

2. **Expected Value of the Unweighted Respondent Mean $E(\bar{y}_r)$**:
   Under Bethlehem's formula:
   $$E(\bar{y}_r) \approx \frac{\sum_{h=1}^3 W_h \rho_h \bar{Y}_h}{\bar{\rho}}$$
   Compute the weighted sum of products:
   - Stratum 1: $W_1 \rho_1 \bar{Y}_1 = 0.50 \times 0.80 \times 1,200 = 480$
   - Stratum 2: $W_2 \rho_2 \bar{Y}_2 = \frac{1}{3} \times 0.60 \times 2,500 = 0.20 \times 2,500 = 500$
   - Stratum 3: $W_3 \rho_3 \bar{Y}_3 = \frac{1}{6} \times 0.30 \times 6,000 = 0.05 \times 6,000 = 300$
   Sum of numerator: $480 + 500 + 300 = 1,280$.

   Dividing by $\bar{\rho} = 0.65$:
   $$E(\bar{y}_r) = \frac{1,280}{0.65} \approx 1,969.2308 \text{ dollars}$$

3. **Nonresponse Bias and Relative Bias**:
   $$\text{Bias}(\bar{y}_r) = E(\bar{y}_r) - \bar{Y} = 1,969.2308 - 2,433.3333 = -464.1025 \text{ dollars}$$
   Alternatively, using the covariance identity:
   $$\text{Bias}(\bar{y}_r) = \frac{S_{\rho y}}{\bar{\rho}} = \frac{-301.6667}{0.65} = -464.1026 \text{ dollars}$$
   The two calculations match identically.

   The percentage relative bias is:
   $$\text{RelBias} = \frac{\text{Bias}}{\bar{Y}} \times 100\% = \frac{-464.1026}{2,433.3333} \times 100\% = -19.07\%$$
   Because high-income households participate at only a $30\%$ rate while low-income households participate at an $80\%$ rate, the unweighted survey underestimate the true municipal average income by nearly $20\%$!

**Solution, step 3: Proving bias elimination via weighting class adjustments.**
Now suppose the agency partitions respondents into the three socioeconomic adjustment cells ($c = 1, 2, 3$).
In cell $c$, the observed response rate converges to $\phi_c = \rho_c$.
The weighting class adjustment factor for respondents in cell $c$ is:
$$f_{nr,c} = \frac{1}{\rho_c}$$

The adjusted weight for a respondent in cell $c$ (under equal design weights $d_i = N/n$) is:
$$w_{i,c}^* = d_i \times \frac{1}{\rho_c}$$

The weighting class estimator of the population total is:
$$\hat{Y}_{wc} = \sum_{c=1}^3 \sum_{i \in s_{r,c}} w_{i,c}^* y_i = \sum_{c=1}^3 \frac{1}{\rho_c} \sum_{i \in s_{r,c}} d_i y_i$$

Taking the expectation over the response mechanism conditional on the sample:
$$E_R\left[ \sum_{i \in s_{r,c}} d_i y_i \;\middle|\; s \right] = \sum_{i \in s_c} d_i y_i E(R_i) = \sum_{i \in s_c} d_i y_i \rho_c = \rho_c \sum_{i \in s_c} d_i y_i$$

Substitute this back into the expectation:
$$E(\hat{Y}_{wc}) = E_s\left[ \sum_{c=1}^3 \frac{1}{\rho_c} \left( \rho_c \sum_{i \in s_c} d_i y_i \right) \right] = E_s\left[ \sum_{c=1}^3 \sum_{i \in s_c} d_i y_i \right] = E_s\left[ \sum_{i \in s} d_i y_i \right] = Y$$
Dividing by $N$:
$$E(\bar{y}_{wc}) = \bar{Y}$$

Let us verify numerically:
The expected respondent count in each stratum from a sample of $n = 300$ households ($n_1 = 150, n_2 = 100, n_3 = 50$):
- Stratum 1: $n_{r,1} = 150 \times 0.80 = 120$ respondents, each with income $1,200$.
- Stratum 2: $n_{r,2} = 100 \times 0.60 = 60$ respondents, each with income $2,500$.
- Stratum 3: $n_{r,3} = 50 \times 0.30 = 15$ respondents, each with income $6,000$.

Compute weighting class adjusted weights $w_c^* = d \times \frac{n_c}{n_{r,c}} = 10 \times \frac{1}{\rho_c}$:
- Stratum 1: $w_1^* = 10 / 0.80 = 12.50$
- Stratum 2: $w_2^* = 10 / 0.60 = 16.6667$
- Stratum 3: $w_3^* = 10 / 0.30 = 33.3333$

Now compute the weighted sum of income:
$$\hat{Y}_{wc} = 120(12.50 \times 1,200) + 60(16.6667 \times 2,500) + 15(33.3333 \times 6,000)$$
$$= 120(15,000) + 60(41,666.67) + 15(200,000) = 1,800,000 + 2,500,000 + 3,000,000 = 7,300,000$$

Dividing by $N = 3,000$:
$$\bar{y}_{wc} = \frac{7,300,000}{3,000} = 2,433.3333 \text{ dollars}$$
Notice that $\bar{y}_{wc} = 2,433.33 = \bar{Y}$ exactly! Weighting class adjustment has completely eradicated the -464.10 dollars nonresponse bias.

---

## Fully worked question 2: Weighting Class Nonresponse Adjustments and Variance Inflation

**Question.** A health research organization conducts a patient satisfaction survey following outpatient clinic visits. An equal-probability sample of $n = 400$ patients is selected from an administrative roster of $N = 4,000$ visits (design weights $d_i = 10$).

The sample is classified into two demographic weighting classes:
- Class 1 (Adults $< 65$ years): $n_1 = 250$ sampled patients.
- Class 2 (Seniors $\ge 65$ years): $n_2 = 150$ sampled patients.

Due to nonresponse, field interviewers obtain completed questionnaires from:
- Class 1: $n_{r,1} = 125$ completed interviews (response rate $\hat{\phi}_1 = 125 / 250 = 0.50$).
  Sample statistics among respondents: mean satisfaction score $\bar{y}_{r,1} = 72.0$, sample variance $s_1^2 = 100.0$.
- Class 2: $n_{r,2} = 120$ completed interviews (response rate $\hat{\phi}_2 = 120 / 150 = 0.80$).
  Sample statistics among respondents: mean satisfaction score $\bar{y}_{r,2} = 88.0$, sample variance $s_2^2 = 64.0$.

1. Compute the unweighted respondent mean $\bar{y}_r$.
2. Compute the nonresponse adjustment factors $f_{nr,c}$ and the calibrated nonresponse weights $w_c^*$ for each class.
3. Compute the weighting class adjusted mean $\bar{y}_{wc}$.
4. Compute the estimated variance of $\bar{y}_{wc}$ and calculate Kish's Weight Design Effect ($\text{Deff}_w$) measuring the variance inflation induced by the unequal nonresponse weights.

**Solution, step 1: Computing unweighted respondent mean.**
Total respondents:
$$n_r = n_{r,1} + n_{r,2} = 125 + 120 = 245 \text{ respondents}$$

The unweighted respondent mean is:
$$\bar{y}_r = \frac{n_{r,1} \bar{y}_{r,1} + n_{r,2} \bar{y}_{r,2}}{n_r} = \frac{125(72.0) + 120(88.0)}{245} = \frac{9,000 + 10,560}{245} = \frac{19,560}{245} \approx 79.8367$$

**Solution, step 2: Computing adjustment factors and nonresponse weights.**
Design weight for all units: $d_i = N/n = 4,000 / 400 = 10.0$.
1. **Class 1 ($< 65$)**:
   $$\hat{\phi}_1 = \frac{n_{r,1}}{n_1} = \frac{125}{250} = 0.50$$
   $$f_{nr,1} = \frac{1}{\hat{\phi}_1} = \frac{1}{0.50} = 2.00$$
   $$w_1^* = d_i \times f_{nr,1} = 10.0 \times 2.00 = 20.0$$

2. **Class 2 ($\ge 65$)**:
   $$\hat{\phi}_2 = \frac{n_{r,2}}{n_2} = \frac{120}{150} = 0.80$$
   $$f_{nr,2} = \frac{1}{\hat{\phi}_2} = \frac{1}{0.80} = 1.25$$
   $$w_2^* = d_i \times f_{nr,2} = 10.0 \times 1.25 = 12.5$$

Verify total represented population:
$$\sum_{i \in s_r} w_i^* = 125(20.0) + 120(12.5) = 2,500 + 1,500 = 4,000 = N$$
The adjusted weights strictly reconstitute the original population size.

**Solution, step 3: Computing weighting class adjusted mean.**
The weighting class adjusted mean is:
$$\bar{y}_{wc} = \frac{\sum_{i \in s_r} w_i^* y_i}{\sum_{i \in s_r} w_i^*} = \frac{2,500(72.0) + 1,500(88.0)}{4,000} = \frac{180,000 + 132,000}{4,000} = \frac{312,000}{4,000} = 78.000$$

Comparing the two estimates:
$$\bar{y}_{wc} - \bar{y}_r = 78.000 - 79.837 = -1.837 \text{ points}$$
Because older patients (who gave higher satisfaction scores, $88.0$) responded at a higher rate ($80\%$ vs $50\%$), the unweighted mean was artificially inflated by nearly $2$ full points. Weighting class adjustment corrects this upward distortion.

**Solution, step 4: Computing estimated variance and Kish's design effect.**
1. **Sampling Variance of $\bar{y}_{wc}$**:
   Treating the weighting classes as post-strata:
   $$\hat{V}(\bar{y}_{wc}) = \sum_{c=1}^2 \left( \frac{n_c}{n} \right)^2 \left( 1 - \frac{n_{r,c}}{N_c} \right) \frac{s_c^2}{n_{r,c}}$$
   Here $n_1/n = 250/400 = 0.625$, $n_2/n = 150/400 = 0.375$.
   Population sizes: $N_1 = 2,500, N_2 = 1,500$.
   - Class 1:
     $$\left( 1 - \frac{125}{2,500} \right) = 1 - 0.05 = 0.95$$
     $$\text{Term}_1 = (0.625)^2 \times 0.95 \times \frac{100.0}{125} = 0.390625 \times 0.95 \times 0.80 = 0.296875$$
   - Class 2:
     $$\left( 1 - \frac{120}{1,500} \right) = 1 - 0.08 = 0.92$$
     $$\text{Term}_2 = (0.375)^2 \times 0.92 \times \frac{64.0}{120} = 0.140625 \times 0.92 \times 0.533333 \approx 0.069000$$

   Summing both terms:
   $$\hat{V}(\bar{y}_{wc}) = 0.296875 + 0.069000 = 0.365875$$
   The standard error is:
   $$\text{SE}(\bar{y}_{wc}) = \sqrt{0.365875} \approx 0.6049$$

2. **Kish's Weight Design Effect ($\text{Deff}_w$)**:
   The unequal weights ($w_1^* = 20.0, w_2^* = 12.5$) introduce variance inflation.
   Across the $n_r = 245$ respondents:
   - Mean weight: $\bar{w}^* = \frac{4,000}{245} \approx 16.3265$
   - Sum of weights: $\sum w_i^* = 4,000$
   - Sum of squared weights:
     $$\sum (w_i^*)^2 = 125(20.0)^2 + 120(12.5)^2 = 125(400) + 120(156.25) = 50,000 + 18,750 = 68,750$$

   Kish's formula is:
   $$\text{Deff}_w = \frac{n_r \sum (w_i^*)^2}{(\sum w_i^*)^2} = \frac{245 \times 68,750}{(4,000)^2} = \frac{16,843,750}{16,000,000} \approx 1.0527$$

   The unequal nonresponse weights inflate sampling variance by only $5.27\%$. This minor variance penalty is a tiny price to pay for eliminating the systematic $1.84$-point nonresponse bias.

---

## Fully worked question 3: Imputation Variance Distortion and Rubin's Multiple Imputation Rules

**Question.** A nutritional survey measures daily caloric intake among $n = 10$ selected children. Due to item nonresponse, $n_{obs} = 6$ children have observed caloric intake values, while $n_{mis} = 4$ children have missing data.

The 6 observed caloric intake values (in kilocalories, kcal) are:
$$y_{obs} = \{1,600, \quad 1,800, \quad 2,000, \quad 2,100, \quad 2,200, \quad 2,300\}$$

Sample statistics for the observed data:
- Observed mean: $\bar{y}_{obs} = \frac{1,600 + 1,800 + 2,000 + 2,100 + 2,200 + 2,300}{6} = \frac{12,000}{6} = 2,000 \text{ kcal}$
- Observed sample variance: $s_{obs}^2 = \frac{1}{5} [(-400)^2 + (-200)^2 + 0^2 + 100^2 + 200^2 + 300^2] = \frac{160,000 + 40,000 + 0 + 10,000 + 40,000 + 90,000}{5} = \frac{340,000}{5} = 68,000 \text{ (kcal)}^2$

1. **Single Mean Imputation**: If the survey agency imputes the missing 4 values using the observed sample mean ($y_i^* = 2,000$ for all 4 missing cases):
   - Compute the completed-sample mean $\bar{y}_{smi}$ and sample variance $s_{smi}^2$.
   - Calculate the percentage by which single mean imputation underestimates the true sample variance.
2. **Multiple Imputation**: To honestly capture imputation uncertainty, the agency conducts $M = 3$ multiple imputations using a stochastic predictive model. The imputed values for the 4 missing cases across the $M = 3$ imputations are:
   - Imputation 1: $y_{mis}^{(1)} = \{1,750, \quad 1,950, \quad 2,150, \quad 2,350\}$
   - Imputation 2: $y_{mis}^{(2)} = \{1,650, \quad 1,850, \quad 2,050, \quad 2,250\}$
   - Imputation 3: $y_{mis}^{(3)} = \{1,800, \quad 1,900, \quad 2,200, \quad 2,500\}$

   For each of the 3 completed datasets:
   - Compute the completed-sample mean $\hat{Q}^{(m)}$ and within-imputation variance $\hat{U}^{(m)} = s_{(m)}^2 / 10$.
3. Apply Rubin's Combining Rules:
   - Compute the overall point estimate $\bar{Q}_3$.
   - Compute the within-imputation variance $\bar{U}_3$, the between-imputation variance $B_3$, and the honest total variance $T_3$.
   - Evaluate the Fraction of Missing Information (FMI).

**Solution, step 1: Evaluating single mean imputation and variance destruction.**
Under single mean imputation, the 4 missing values are set to $2,000$.
The completed dataset is:
$$y_{smi} = \{1,600, 1,800, 2,000, 2,100, 2,200, 2,300, 2,000, 2,000, 2,000, 2,000\}$$

1. **Completed Mean**:
   $$\bar{y}_{smi} = \frac{12,000 + 4(2,000)}{10} = \frac{20,000}{10} = 2,000 \text{ kcal}$$

2. **Completed Sample Variance**:
   The deviations from $2,000$ for the 4 imputed values are identically zero ($0^2 = 0$).
   $$\sum_{i=1}^{10} (y_i - \bar{y}_{smi})^2 = 340,000 + 0 = 340,000$$
   Dividing by $n - 1 = 9$:
   $$s_{smi}^2 = \frac{340,000}{9} \approx 37,777.78 \text{ (kcal)}^2$$

3. **Variance Underestimation**:
   Comparing $s_{smi}^2$ with the true observed variance $s_{obs}^2 = 68,000$:
   $$\text{Underestimation} = \frac{68,000 - 37,777.78}{68,000} \times 100\% = \frac{30,222.22}{68,000} \times 100\% = 44.44\%$$
   Single mean imputation has destroyed **$44.4\%$ of the true sample variance**! Naive variance estimation would report $\hat{V}(\bar{y}) = s_{smi}^2 / 10 = 3,778$, yielding a standard error of $\sqrt{3,778} = 61.5$ kcal, which is drastically deflated.

**Solution, step 2: Analyzing each of the $M = 3$ multiply imputed datasets.**
Each completed dataset contains the 6 fixed observed values (sum $12,000$, sum of squares $\sum y_{obs}^2 = 24,340,000$) plus the 4 imputed values.

1. **Dataset 1**:
   - Imputed values: $\{1,750, 1,950, 2,150, 2,350\}$. Sum $= 8,200$.
   - Total sum: $12,000 + 8,200 = 20,200$.
   - Point estimate:
     $$\hat{Q}^{(1)} = \frac{20,200}{10} = 2,020.0 \text{ kcal}$$
   - Deviations from $2,020$:
     Observed values: $(1,600 - 2,020)^2 = 176,400$; $(1,800 - 2,020)^2 = 48,400$; $(2,000 - 2,020)^2 = 400$; $(2,100 - 2,020)^2 = 6,400$; $(2,200 - 2,020)^2 = 32,400$; $(2,300 - 2,020)^2 = 78,400$. Sum $= 342,400$.
     Imputed values: $(1,750 - 2,020)^2 = 72,900$; $(1,950 - 2,020)^2 = 4,900$; $(2,150 - 2,020)^2 = 16,900$; $(2,350 - 2,020)^2 = 108,900$. Sum $= 203,600$.
     Total sum of squares $= 342,400 + 203,600 = 546,000$.
     $$s_{(1)}^2 = \frac{546,000}{9} = 60,666.67 \text{ (kcal)}^2$$
     $$\hat{U}^{(1)} = \frac{s_{(1)}^2}{10} = 6,066.67$$

2. **Dataset 2**:
   - Imputed values: $\{1,650, 1,850, 2,050, 2,250\}$. Sum $= 7,800$.
   - Total sum: $12,000 + 7,800 = 19,800$.
   - Point estimate:
     $$\hat{Q}^{(2)} = \frac{19,800}{10} = 1,980.0 \text{ kcal}$$
   - Deviations from $1,980$:
     Observed: $(1,600-1,980)^2 = 144,400$; $(1,800-1,980)^2 = 32,400$; $(2,000-1,980)^2 = 400$; $(2,100-1,980)^2 = 14,400$; $(2,200-1,980)^2 = 48,400$; $(2,300-1,980)^2 = 102,400$. Sum $= 342,400$.
     Imputed: $(1,650-1,980)^2 = 108,900$; $(1,850-1,980)^2 = 16,900$; $(2,050-1,980)^2 = 4,900$; $(2,250-1,980)^2 = 72,900$. Sum $= 203,600$.
     Total sum of squares $= 342,400 + 203,600 = 546,000$.
     $$s_{(2)}^2 = \frac{546,000}{9} = 60,666.67 \text{ (kcal)}^2$$
     $$\hat{U}^{(2)} = \frac{s_{(2)}^2}{10} = 6,066.67$$

3. **Dataset 3**:
   - Imputed values: $\{1,800, 1,900, 2,200, 2,500\}$. Sum $= 8,400$.
   - Total sum: $12,000 + 8,400 = 20,400$.
   - Point estimate:
     $$\hat{Q}^{(3)} = \frac{20,400}{10} = 2,040.0 \text{ kcal}$$
   - Deviations from $2,040$:
     Observed: $(1,600-2,040)^2 = 193,600$; $(1,800-2,040)^2 = 57,600$; $(2,000-2,040)^2 = 1,600$; $(2,100-2,040)^2 = 3,600$; $(2,200-2,040)^2 = 25,600$; $(2,300-2,040)^2 = 67,600$. Sum $= 349,600$.
     Imputed: $(1,800-2,040)^2 = 57,600$; $(1,900-2,040)^2 = 19,600$; $(2,200-2,040)^2 = 25,600$; $(2,500-2,040)^2 = 211,600$. Sum $= 314,400$.
     Total sum of squares $= 349,600 + 314,400 = 664,000$.
     $$s_{(3)}^2 = \frac{664,000}{9} \approx 73,777.78 \text{ (kcal)}^2$$
     $$\hat{U}^{(3)} = \frac{s_{(3)}^2}{10} = 7,377.78$$

Summary of the $M = 3$ Imputations:
$$\begin{array}{c|cc}
\text{Dataset } m & \text{Estimate } \hat{Q}^{(m)} & \text{Within Variance } \hat{U}^{(m)} \\
\hline
1 & 2,020.0 & 6,066.67 \\
2 & 1,980.0 & 6,066.67 \\
3 & 2,040.0 & 7,377.78 \\
\hline
\end{array}$$

**Solution, step 3: Applying Rubin's combining rules.**
1. **Overall Combined Point Estimate ($\bar{Q}_3$)**:
   $$\bar{Q}_3 = \frac{1}{3} (2,020.0 + 1,980.0 + 2,040.0) = \frac{6,040.0}{3} \approx 2,013.3333 \text{ kcal}$$

2. **Within-Imputation Variance ($\bar{U}_3$)**:
   $$\bar{U}_3 = \frac{1}{3} (6,066.67 + 6,066.67 + 7,377.78) = \frac{19,511.12}{3} \approx 6,503.7067$$

3. **Between-Imputation Variance ($B_3$)**:
   Deviations from $\bar{Q}_3 = 2,013.3333$:
   - $m = 1$: $(2,020 - 2,013.3333)^2 = (6.6667)^2 = 44.4449$
   - $m = 2$: $(1,980 - 2,013.3333)^2 = (-33.3333)^2 = 1,111.1089$
   - $m = 3$: $(2,040 - 2,013.3333)^2 = (26.6667)^2 = 711.1129$
   Sum $= 44.4449 + 1,111.1089 + 711.1129 = 1,866.6667$.
   Dividing by $M - 1 = 2$:
   $$B_3 = \frac{1,866.6667}{2} = 933.3333$$

4. **Honest Total Variance ($T_3$)**:
   $$T_3 = \bar{U}_3 + \left( 1 + \frac{1}{M} \right) B_3 = 6,503.7067 + \left( 1 + \frac{1}{3} \right) (933.3333)$$
   $$= 6,503.7067 + \frac{4}{3} (933.3333) = 6,503.7067 + 1,244.4444 = 7,748.1511$$
   The honest standard error is:
   $$\text{SE}(\bar{Q}_3) = \sqrt{7,748.1511} \approx 88.0236 \text{ kcal}$$

Notice the difference:
- Single Mean Imputation reported $\text{SE} = \sqrt{3,778} = 61.47$ kcal.
- Rubin's Multiple Imputation reports honest $\text{SE} = 88.02$ kcal.
Single imputation produced a standard error that was underestimated by $30.2\%$, which would have generated falsely narrow confidence intervals with unacceptably low coverage.

5. **Fraction of Missing Information (FMI)**:
   The relative increase in variance due to nonresponse is:
   $$r_3 = \frac{(1 + 1/3) B_3}{\bar{U}_3} = \frac{1,244.4444}{6,503.7067} \approx 0.19134$$
   The estimated Fraction of Missing Information is approximately:
   $$\hat{\lambda} \approx \frac{(1 + 1/3) B_3}{T_3} = \frac{1,244.4444}{7,748.1511} \approx 0.1606 \approx 16.1\%$$
   Approximately $16.1\%$ of the total inferential uncertainty in estimating mean caloric intake is attributable to missing data rather than finite sampling error.

---

## Practical Synthesis: The Total Survey Error (TSE) Audit

In modern survey institutions, the mitigation of nonresponse and measurement errors is unified under the **Total Survey Error (TSE)** paradigm. Survey statisticians conduct comprehensive quality audits across five critical dimensions:

1. **R-Indicators (Representativeness Indicators)**:
   To evaluate whether a responding sample is representative of the selected sample, Schouten, Cobben, and Bethlehem (2009) formulated the **R-indicator**:
   $$R(\boldsymbol{\rho}) = 1 - 2 S_\rho$$
   where $S_\rho$ is the standard deviation of the estimated response propensities.
   - If response is MCAR ($S_\rho = 0$), $R = 1.0$ (perfect representativeness).
   - As response propensities diverge across demographic groups ($S_\rho \uparrow$), $R$ declines toward zero.
   - International statistical standards require $R(\hat{\boldsymbol{\rho}}) \ge 0.80$ for high-quality official publications.

2. **Nonresponse Bias Benchmarking**:
   Comparing survey estimates against pristine administrative registers (tax returns, vital statistics, census benchmarks) on known variables. If discrepancy exceeds $5\%$, calibration or raking adjustments must be enhanced.

3. **Imputation Quality Diagnostics**:
   - Kolmogorv–Smirnov two-sample tests comparing observed versus imputed distributions to ensure that imputation does not introduce unnatural peaks or distort tail percentiles.
   - Cross-validation of imputation models by artificially censoring known values and calculating Root Mean Squared Prediction Error (RMSPE).

In the final unit, we synthesize all these components into **Complex-Survey Inference and Replicate Variance Estimation**, examining how stratification, clustering, unequal weighting, calibration, and nonresponse adjustments are unified into defensible scientific inferences.
