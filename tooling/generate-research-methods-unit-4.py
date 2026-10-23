from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-statistical-research-methods"

u4_content = r"""# Unit 4: Survey Design, Questionnaire Engineering & Sampling Strategies

Sample surveys constitute the empirical foundation of modern socioeconomic planning, public health surveillance, demographic estimation, and market intelligence. However, inferring population parameters from survey samples is fraught with methodological challenges. Collecting data from human respondents introduces complex psychological, cognitive, sociological, and logistical sources of error. As Robert M. Groves and colleagues established in their landmark formulation of survey methodology: *"A survey is not merely a statistical exercise in random sampling; it is a complex socio-cognitive measurement process embedded in an organizational delivery system."*

This unit examines the Total Survey Error (TSE) paradigm, decomposes the mechanisms of survey representation and measurement errors, analyzes cognitive models of questionnaire response, investigates probability versus non-probability sampling architectures, and provides the mathematical formulas governing sample size determination, non-response adjustments, and sensitive attribute elicitation.

## 4.1 The Total Survey Error (TSE) Framework: Measurement vs. Representation Errors
The Total Survey Error (TSE) framework, formalized by Robert Groves, Paul Biemer, and Lars Lyberg, provides the comprehensive architectural taxonomy for identifying, classifying, and quantifying all sources of error that can separate a survey sample statistic from the true population parameter.

TSE conceptualizes a survey as an intersection of two parallel, interdependent structural lifecycles:
1. The Measurement Lifecycle (Construct $\to$ Observed Score): How accurately do the observed survey responses reflect the underlying substantive constructs of interest?
2. The Representation Lifecycle (Target Population $\to$ Final Respondent Sample): How accurately do the surveyed individuals represent the broader target population about whom inferences are drawn?

Total Survey Error is formally defined as the Mean Squared Error (MSE) of the survey estimator $\hat{\theta}$:
$$\mathrm{MSE}(\hat{\theta}) = \mathbb{E}[(\hat{\theta} - \theta_0)^2] = \mathrm{Var}(\hat{\theta}) + [\mathrm{Bias}(\hat{\theta})]^2$$
where $\theta_0$ is the true population parameter.
Traditional sampling theory focused almost exclusively on minimizing sampling variance ($\mathrm{Var}(\hat{\theta})$) through larger sample sizes $n$. The foundational insight of the TSE framework is that in modern empirical surveys, systematic biases ($[\mathrm{Bias}(\hat{\theta})]^2$)—arising from non-coverage, non-response, questionnaire misinterpretation, and social desirability—frequently dwarf sampling variance. Doubling the sample size $n$ from $1,000$ to $2,000$ reduces sampling variance by $50\%$, but leaves systematic non-response bias completely untouched.

## 4.2 Decomposition of Representation Error: Coverage, Sampling, Nonresponse, and Adjustment
The representation branch of Total Survey Error tracks how well the surveyed units represent the target population across five successive stages:

1. Target Population: The theoretical, finite collection of units about which the research seeks to draw conclusions (e.g., all non-institutionalized adults aged $\ge 18$ residing in Bangladesh).
2. Sampling Frame: The concrete, operational list, database, or directory used to select sample units (e.g., active cellular telephone numbers, postal address registers, electoral registries).
   - Frame Coverage Error: Discrepancies between the target population and the sampling frame.
     - Undercoverage: Eligible target population units missing from the frame (e.g., homeless individuals or adults without phones).
     - Overcoverage / Ineligible Units: Frame entries that do not belong to the target population (e.g., commercial business lines in a residential phone sample).
     - Duplication: Single units appearing multiple times on the frame, distorting selection probabilities.
3. Sample: The subset of frame units selected via an algorithmic sampling mechanism.
   - Sampling Error: Discrepancies between the sample and the frame resulting from observing only a finite fraction of units rather than the complete census. Decomposes into sampling variance (governed by sample size and design architecture) and sampling bias (from non-probability selection).
4. Respondent Sample: The subset of selected sample units that successfully provide data.
   - Nonresponse Error: Discrepancies between the selected sample and the final respondent sample resulting from non-contact, refusal, or incapacity of sampled units.
5. Post-Survey Adjusted Sample: The final data structure after applying statistical adjustments.
   - Adjustment Error: Modeling errors and variance inflation introduced during weighting, post-stratification, raking, and imputation.

## 4.3 Mechanisms of Missing Data: MCAR, MAR, and MNAR in Survey Telemetry
Nonresponse produces missing data, which threatens the validity of all downstream statistical inference. In 1976, Donald B. Rubin established the mathematical taxonomy of missing data mechanisms:

Let $\mathbf{Y} = (\mathbf{Y}_{\text{obs}}, \mathbf{Y}_{\text{mis}})$ denote the complete data matrix, where $\mathbf{Y}_{\text{obs}}$ represents observed values and $\mathbf{Y}_{\text{mis}}$ represents missing values. Let $\mathbf{R}$ denote a binary indicator matrix of the same dimensions, where $R_{ij} = 1$ if $Y_{ij}$ is observed and $R_{ij} = 0$ if $Y_{ij}$ is missing.

Rubin classified missingness into three distinct regimes based on the conditional probability distribution $P(\mathbf{R} \mid \mathbf{Y}_{\text{obs}}, \mathbf{Y}_{\text{mis}}, \boldsymbol{\psi})$:

1. Missing Completely at Random (MCAR):
   Missingness is statistically independent of both observed and unobserved data values:
   $$P(\mathbf{R} \mid \mathbf{Y}_{\text{obs}}, \mathbf{Y}_{\text{mis}}, \boldsymbol{\psi}) = P(\mathbf{R} \mid \boldsymbol{\psi})$$
   Example: A laboratory technician accidentally drops and breaks a randomly selected test tube; a survey page is skipped due to a printer malfunction.
   - Consequence: Complete-case analysis (discarding units with missing values) reduces statistical power, but produces completely unbiased parameter estimates: $\mathbb{E}[\bar{y}_{\text{complete}}] = \mu_Y$.
2. Missing at Random (MAR):
   Missingness depends on observed data $\mathbf{Y}_{\text{obs}}$, but does *not* depend on unobserved missing values $\mathbf{Y}_{\text{mis}}$, conditional on $\mathbf{Y}_{\text{obs}}$:
   $$P(\mathbf{R} \mid \mathbf{Y}_{\text{obs}}, \mathbf{Y}_{\text{mis}}, \boldsymbol{\psi}) = P(\mathbf{R} \mid \mathbf{Y}_{\text{obs}}, \boldsymbol{\psi})$$
   Example: In a health survey, younger men are less likely to report their annual income, but within demographic strata defined by age, sex, and education, the probability of missing income is independent of the income amount itself.
   - Consequence: Complete-case analysis is biased. However, missingness is ignorable under likelihood-based inference: valid, unbiased estimates are recovered using Multiple Imputation (MI) or Full Information Maximum Likelihood (FIML) conditioning on $\mathbf{Y}_{\text{obs}}$.
3. Missing Not at Random (MNAR / Non-Ignorable Missingness):
   Missingness depends directly on the unobserved missing values $\mathbf{Y}_{\text{mis}}$ themselves, even after conditioning on all available observed covariates:
   $$P(\mathbf{R} \mid \mathbf{Y}_{\text{obs}}, \mathbf{Y}_{\text{mis}}, \boldsymbol{\psi}) \ne P(\mathbf{R} \mid \mathbf{Y}_{\text{obs}}, \boldsymbol{\psi})$$
   Example: Ultra-wealthy individuals refuse to report their assets because their assets are extraordinarily high; patients experiencing severe depression fail to attend follow-up clinic visits because their depression has worsened.
   - Consequence: Standard Multiple Imputation and FIML fail. Unbiased estimation requires explicit joint modeling of the outcome and the missingness mechanism (e.g., Heckman selection models, Diggle-Kenward selection models, or pattern-mixture models).

## 4.4 Tourangeau's Cognitive Model of Survey Response
In 1984, Roger Tourangeau formulated the four-stage cognitive model of the survey response process, establishing that answering a survey question is a complex mental operation:

1. Comprehension:
   The respondent reads or hears the survey prompt, decodes semantic meaning, identifies the information requested, and links terms to cognitive categories.
   - Cognitive Failures: Ambiguous vocabulary, unfamiliar technical jargon, overly complex grammar, or double-barreled syntax.
2. Retrieval:
   The respondent searches long-term episodic and semantic memory to retrieve relevant autobiographical memories, facts, beliefs, and experiences.
   - Cognitive Failures: Memory decay, telescoping (recalling distant events as having occurred recently), retrieval cues biasing memory recall.
3. Judgment and Estimation:
   The respondent synthesizes, integrates, and evaluates the retrieved memories to formulate an internal mental answer. If exact recall is impossible, the respondent generates an estimate using cognitive heuristics.
   - Cognitive Failures: Availability heuristic, anchoring on arbitrary reference points provided in the question, rounding bias.
4. Response Editing and Reporting:
   The respondent maps their internal mental judgment onto the response categories provided by the instrument, evaluating social risk and self-presentation before communicating the answer.
   - Cognitive Failures: Social desirability bias (suppressing stigmatized behaviors or exaggerating socially approved behaviors), acquiescence (agreeing regardless of content), extreme response styles.

## 4.5 Questionnaire Engineering: Question Wording, Leading Prompts, and Double-Barreled Pitfalls
Questionnaire engineering is the applied discipline of constructing measurement instruments that minimize cognitive processing errors at each stage of Tourangeau's model.

Key Methodological Principles of Questionnaire Design:
1. Avoid Leading and Loaded Questions:
   A leading question contains unbalanced emotional or rhetorical framing that guides the respondent toward a specific desirable answer:
   - Flawed Leading Prompt: *"Given the devastating economic consequences of inflation, do you agree that government spending should be immediately reduced?"*
   - Methodologically Balanced Prompt: *"Some people believe the government should reduce spending to combat inflation, while others believe government spending should be maintained to protect public services. Which of these views comes closer to your own?"*
2. Eliminate Double-Barreled Prompts:
   A double-barreled question combines two distinct substantive issues into a single prompt requiring a single response:
   - Flawed Prompt: *"Do you believe our university should increase tuition to invest in modern laboratory facilities and expand student mental health services?"*
   - Methodological Solution: Decouple the prompt into two independent items: one evaluating laboratory facilities and one evaluating mental health services.
3. Control for Acquiescence Response Bias:
   Acquiescence bias is the systematic tendency of respondents to agree with statement prompts regardless of their substantive content ("yea-saying"). Questionnaires should employ balanced item batteries containing reverse-keyed (negatively worded) items so that agreeing with all items produces contradictory, detectable responses.
4. Response Order Effects:
   - Primacy Effect: Respondents in visual surveys (self-administered paper or web surveys) disproportionately select options presented early in a vertical list.
   - Recency Effect: Respondents in auditory surveys (telephone or face-to-face interviews) disproportionately select options presented last, because they remain active in short-term auditory memory. Methodologists randomize the presentation order of response options to neutralize order bias.

## 4.6 Worked Problem Examples

### Fully worked question 1: Nonresponse Bias Estimation and Weighting
A public health institute surveys $N = 10,000$ healthcare workers to estimate the proportion $P$ who received an annual influenza vaccination.
From the target population, a simple random sample of $n = 1,000$ workers is selected:
- Responding sample: $n_r = 600$ workers complete the survey.
- Nonresponding sample: $n_m = 400$ workers refuse or fail to respond (Response rate $R = 600 / 1000 = 60.0\%$).

Among the $n_r = 600$ respondents, $y_r = 480$ report receiving the vaccination (observed sample proportion $\hat{P}_r = 480 / 600 = 0.800$ or $80.0\%$).
The researchers conduct an intensive follow-up telephone audit of a random subsample of the nonrespondents and determine that the true vaccination proportion among nonrespondents is $P_m = 0.500$ ($50.0\%$).
1. State the mathematical formula for nonresponse bias in sample means and proportions.
2. Compute the exact nonresponse bias $B(\hat{P}_r)$ and the true overall population proportion $P$.
3. Compute the post-stratification nonresponse adjustment weights for respondents and show that the weighted estimator recovers the true parameter.

### Solution, step 1: Formulate the Nonresponse Bias Equation
Let:
- $N$ be total sample size ($n = 1000$).
- $n_r$ be the number of respondents ($600$), with proportion $W_r = n_r / n = 0.60$.
- $n_m$ be the number of nonrespondents ($400$), with proportion $W_m = n_m / n = 0.40$.
- $\bar{y}_r$ be the respondent mean ($\hat{P}_r = 0.80$).
- $\bar{y}_m$ be the nonrespondent mean ($P_m = 0.50$).

The true overall sample mean is:
$$\bar{y} = W_r \bar{y}_r + W_m \bar{y}_m$$
The nonresponse bias of the unadjusted respondent mean $\bar{y}_r$ is:
$$B(\bar{y}_r) = \mathbb{E}[\bar{y}_r] - \bar{y} = \bar{y}_r - (W_r \bar{y}_r + W_m \bar{y}_m) = (1 - W_r)\bar{y}_r - W_m \bar{y}_m = W_m (\bar{y}_r - \bar{y}_m)$$
$$B(\bar{y}_r) = \frac{n_m}{n} (\bar{y}_r - \bar{y}_m)$$
Nonresponse bias is the product of two distinct components: the nonresponse rate ($W_m = n_m/n$) and the substantive contrast between respondents and nonrespondents ($\bar{y}_r - \bar{y}_m$).

### Solution, step 2: Calculate Nonresponse Bias and True Population Parameter
Substitute the parameters:
- $W_m = 0.40$ (a $40\%$ nonresponse rate)
- Substantive contrast: $\hat{P}_r - P_m = 0.800 - 0.500 = +0.300$

Compute nonresponse bias:
$$B(\hat{P}_r) = 0.40 \times (+0.300) = \mathbf{+0.120} \quad (+12.0\% \text{ percentage points})$$
The true overall vaccination proportion across the complete sample is:
$$P = \hat{P}_r - B(\hat{P}_r) = 0.800 - 0.120 = \mathbf{0.680} \quad (68.0\%)$$
Equivalently:
$$P = W_r \hat{P}_r + W_m P_m = (0.60 \times 0.800) + (0.40 \times 0.500) = 0.480 + 0.200 = \mathbf{0.680}$$
The unadjusted survey report of $80.0\%$ massively overstates vaccine uptake by $12.0$ percentage points because pro-vaccination healthcare workers were substantially more likely to respond to the health survey.

### Solution, step 3: Derive Nonresponse Adjustment Weights
Suppose workers can be stratified into two administrative categories: Permanent Hospital Staff ($h = 1$) and Contract Workers ($h = 2$).
Suppose population administrative records show that $50\%$ of the target population are Permanent Staff and $50\%$ are Contract Workers ($N_1 / N = 0.50, N_2 / N = 0.50$).
Among respondents:
- Permanent Staff comprise $n_{r1} = 450$ respondents ($75\%$).
- Contract Workers comprise $n_{r2} = 150$ respondents ($25\%$).

The post-stratification weight for stratum $h$ is:
$$w_h = \frac{N_h / N}{n_{rh} / n_r}$$
Compute weights:
$$w_1 = \frac{0.50}{450 / 600} = \frac{0.50}{0.75} = \frac{2}{3} \approx \mathbf{0.6667}$$
$$w_2 = \frac{0.50}{150 / 600} = \frac{0.50}{0.25} = \mathbf{2.0000}$$
Contract workers are down-represented among respondents by a factor of 2, so each contract worker respondent receives a weight of $w_2 = 2.0$.
Suppose Permanent Staff have $\hat{P}_1 = 0.8667$ and Contract Workers have $\hat{P}_2 = 0.6000$:
$$\hat{P}_{\text{weighted}} = \frac{w_1 n_{r1} \hat{P}_1 + w_2 n_{r2} \hat{P}_2}{w_1 n_{r1} + w_2 n_{r2}} = \frac{\left(\frac{2}{3} \times 450 \times 0.8667\right) + (2.0 \times 150 \times 0.6000)}{300 + 300}$$
$$\hat{P}_{\text{weighted}} = \frac{(300 \times 0.8667) + (300 \times 0.6000)}{600} = \frac{260 + 180}{600} = \frac{440}{600} = \frac{0.8667 + 0.6000}{2} = 0.7333$$
Post-stratification weighting corrects the sample representation to match population benchmarks, substantially shrinking the bias.

---

### Fully worked question 2: Sample Size Determination for Complex Survey Designs with Design Effect
An international health agency plans a national demographic survey to estimate the prevalence $p$ of childhood stunting in a developing nation.
Epidemiological benchmarks anticipate a true prevalence of approximately $p = 0.30$.
The ministry demands that the survey achieve a margin of error of no more than $E = \pm 0.02$ ($2.0$ percentage points) with $95\%$ confidence ($\alpha = 0.05, z_{\alpha/2} = 1.96$).
Due to geographical dispersion, the agency cannot execute Simple Random Sampling. Instead, they deploy a two-stage Cluster Sampling Design:
- Primary Sampling Units (PSUs): $K$ administrative villages.
- Secondary Sampling Units: $m = 25$ households selected per sampled village.
- The Intraclass Correlation Coefficient for childhood stunting within villages is estimated as $\rho = \mathrm{ICC} = 0.040$.
- Anticipated household nonresponse rate is $15.0\%$.

1. Compute the baseline sample size $n_{\text{SRS}}$ required under Simple Random Sampling.
2. Calculate Kish's Design Effect ($\mathrm{Deff}$) resulting from cluster correlation, and compute the cluster-adjusted effective sample size $n_{\text{cluster}}$.
3. Compute the final gross sample size $n_{\text{gross}}$ required to account for $15\%$ nonresponse, and determine the total number of village clusters $K$ that must be visited.

### Solution, step 1: Compute Baseline Simple Random Sample Size ($n_{\text{SRS}}$)
Under Simple Random Sampling with infinite population, the required sample size is:
$$n_{\text{SRS}} = \frac{z_{\alpha/2}^2 \cdot p(1 - p)}{E^2}$$
Substitute $z_{0.025} = 1.96$, $p = 0.30$, and margin of error $E = 0.02$:
$$p(1 - p) = 0.30 \times 0.70 = 0.210$$
$$z^2 = (1.96)^2 = 3.8416$$
$$E^2 = (0.02)^2 = 0.0004$$
$$n_{\text{SRS}} = \frac{3.8416 \times 0.210}{0.0004} = \frac{0.806736}{0.0004} = \mathbf{2,016.84} \implies \mathbf{2,017 \text{ households}}$$
Under Simple Random Sampling, $2,017$ households are required.

### Solution, step 2: Calculate Kish's Design Effect ($\mathrm{Deff}$) and Cluster Inflation
Leslie Kish formulated the Design Effect ($\mathrm{Deff}$) to quantify the ratio of the variance of an estimator under a complex sampling design to its variance under Simple Random Sampling with the identical sample size:
$$\mathrm{Deff} = \frac{\mathrm{Var}_{\text{complex}}(\hat{p})}{\mathrm{Var}_{\text{SRS}}(\hat{p})}$$
For equal cluster sizes of $m$ units per cluster and intraclass correlation $\rho$:
$$\mathrm{Deff} = 1 + (m - 1)\rho$$
Substitute cluster size $m = 25$ and $\rho = 0.040$:
$$\mathrm{Deff} = 1 + (25 - 1) \times 0.040 = 1 + 24 \times 0.040 = 1 + 0.960 = \mathbf{1.960}$$
Because households within the same village share dietary habits, clean water access, and socioeconomic conditions ($\rho = 0.040$), each additional household sampled within a village provides less independent information. Sampling variance is inflated by nearly $100\%$ ($\mathrm{Deff} = 1.960$).
The cluster-adjusted sample size is:
$$n_{\text{cluster}} = n_{\text{SRS}} \times \mathrm{Deff} = 2,016.84 \times 1.960 = \mathbf{3,953.0} \implies \mathbf{3,953 \text{ households}}$$
Ignoring cluster correlation would have resulted in an investigation that was underpowered by half!

### Solution, step 3: Adjust for Nonresponse and Determine Cluster Allocation
To ensure that $3,953$ completed interviews are obtained when the response rate is $R = 1 - 0.15 = 0.85$ ($85.0\%$):
$$n_{\text{gross}} = \frac{n_{\text{cluster}}}{R} = \frac{3953}{0.85} = \mathbf{4,650.59} \implies \mathbf{4,651 \text{ households}}$$
With $m = 25$ households sampled per village cluster:
$$K = \frac{n_{\text{gross}}}{m} = \frac{4651}{25} = 186.04 \implies \mathbf{187 \text{ village clusters}}$$
The research team must select and visit $K = 187$ distinct village clusters, sampling $25$ households per village ($4,675$ gross households sampled), to guarantee achieving the $\pm 2.0\%$ margin of error at $95\%$ confidence.

---

### Fully worked question 3: Warner's Randomized Response Technique for Sensitive Questions
In an epidemiological survey evaluating intravenous drug abuse in an urban population, asking directly: *"Have you injected illicit drugs within the past 30 days?"* produces severe social desirability refusal and falsification ($P_{\text{lie}} \approx 0.80$).
Stanley L. Warner (1965) invented the Randomized Response Technique (RRT) to eliminate social desirability bias by providing mathematical privacy and unbreachable plausible deniability.
Each respondent is given a private randomization spinner (or coin flip mechanism unseen by the interviewer). The spinner directs the respondent to answer Question A with probability $p = 0.70$ and Question B with probability $1 - p = 0.30$:
- Question A: *"I have injected illicit drugs in the past 30 days."* (True sensitive attribute, true prevalence $\pi$).
- Question B: *"I have NOT injected illicit drugs in the past 30 days."* (Exact negation, prevalence $1 - \pi$).
The respondent merely answers "Yes" or "No" to whichever question was selected by their private spinner. The interviewer records only the binary response ("Yes" or "No") and has zero knowledge of which question was answered.

Across a sample of $n = 1,000$ respondents, $n_{\text{yes}} = 460$ respond "Yes" (observed sample proportion $\lambda = 460 / 1000 = 0.460$).
1. Formulate the total probability of answering "Yes" as a function of the true prevalence $\pi$ and randomization parameter $p$.
2. Derive the closed-form Warner estimator $\hat{\pi}$ for the true population prevalence.
3. Compute the estimated drug abuse prevalence $\hat{\pi}$ and its standard error $\mathrm{SE}(\hat{\pi})$.

### Solution, step 1: Formulate the Total Probability of Answering "Yes"
By the Law of Total Probability:
$$P(\text{Yes}) = P(\text{Yes} \mid \text{Question A}) P(\text{Question A}) + P(\text{Yes} \mid \text{Question B}) P(\text{Question B})$$
Since Question A is the affirmative statement of the sensitive behavior, $P(\text{Yes} \mid \text{Question A}) = \pi$.
Since Question B is the exact logical negation, $P(\text{Yes} \mid \text{Question B}) = 1 - \pi$.
The spinner probabilities are $P(\text{Question A}) = p$ and $P(\text{Question B}) = 1 - p$.
Let $\lambda \equiv P(\text{Yes})$:
$$\lambda = \pi p + (1 - \pi)(1 - p)$$
Expand and collect terms in $\pi$:
$$\lambda = \pi p + 1 - p - \pi + \pi p = (2p - 1)\pi + (1 - p)$$

### Solution, step 2: Derive the Warner Estimator $\hat{\pi}$
Solve the linear equation for the true prevalence $\pi$:
$$\lambda - (1 - p) = (2p - 1)\pi$$
Provided $p \ne 0.50$ (so that $2p - 1 \ne 0$):
$$\pi = \frac{\lambda - (1 - p)}{2p - 1}$$
Replacing the population probability $\lambda$ with the sample proportion of "Yes" responses $\hat{\lambda} = n_{\text{yes}} / n$ yields the Warner Estimator:
$$\hat{\pi} = \frac{\hat{\lambda} - (1 - p)}{2p - 1}$$
Since $\hat{\lambda}$ is an unbiased estimator of $\lambda$ ($\mathbb{E}[\hat{\lambda}] = \lambda$), $\hat{\pi}$ is strictly unbiased:
$$\mathbb{E}[\hat{\pi}] = \frac{\mathbb{E}[\hat{\lambda}] - (1 - p)}{2p - 1} = \frac{\lambda - (1 - p)}{2p - 1} = \pi$$

### Solution, step 3: Compute Prevalence Estimate and Standard Error
Substitute the empirical survey data:
- $\hat{\lambda} = 0.460$
- $p = 0.70 \implies 1 - p = 0.30$
- $2p - 1 = 2(0.70) - 1 = 1.40 - 1 = 0.40$

Compute the estimated prevalence:
$$\hat{\pi} = \frac{0.460 - 0.300}{0.400} = \frac{0.160}{0.400} = \mathbf{0.400} \quad (40.0\%)$$
The true estimated prevalence of illicit intravenous drug injection is $40.0\%$.
Now derive the variance and standard error. Since $n_{\text{yes}} \sim \mathrm{Binomial}(n, \lambda)$:
$$\mathrm{Var}(\hat{\lambda}) = \frac{\lambda(1 - \lambda)}{n}$$
The variance of the Warner estimator is:
$$\mathrm{Var}(\hat{\pi}) = \frac{\mathrm{Var}(\hat{\lambda})}{(2p - 1)^2} = \frac{\lambda(1 - \lambda)}{n (2p - 1)^2}$$
Substitute $\hat{\lambda} = 0.460$, $1 - \hat{\lambda} = 0.540$, $n = 1000$, and $2p - 1 = 0.40$:
$$\lambda(1 - \lambda) = 0.460 \times 0.540 = 0.2484$$
$$(2p - 1)^2 = (0.40)^2 = 0.160$$
$$\mathrm{Var}(\hat{\pi}) = \frac{0.2484}{1000 \times 0.160} = \frac{0.2484}{160} = 0.0015525$$
$$\mathrm{SE}(\hat{\pi}) = \sqrt{0.0015525} \approx \mathbf{0.0394} \quad (3.94\%)$$
The $95\%$ confidence interval for true drug injection prevalence is:
$$\mathrm{CI}_{95\%} = 0.400 \pm 1.96 \times 0.0394 = 0.400 \pm 0.0772 \implies [32.3\%, \; 47.7\%]$$
The Randomized Response Technique provides complete mathematical protection to individual respondents while recovering statistically sound epidemiological prevalence estimates.

## 4.7 Response Scale Optimization: Likert Scales, Visual Analog Scales, and Anchors
When designing structured measurement items, researchers must choose response scale architectures that optimize psychometric discrimination without exceeding human cognitive capacity:

1. Number of Scale Categories:
   Psychometric simulations indicate that reliability and validity increase rapidly as the number of response options increases from 2 to 5, level off between 5 and 7, and decline beyond 9 as respondents struggle to make fine sensory distinctions. A 5-point or 7-point scale represents the psychometric optimum for bipolar constructs (e.g., Strongly Disagree to Strongly Agree).
2. Inclusion of a Neutral Midpoint:
   Providing an odd number of categories (e.g., 5 or 7 with "Neither Agree nor Disagree") permits respondents who genuinely hold neutral attitudes to report them. Omitting the midpoint forces ambivalent respondents to pick a side, artificially inflating false extremity. However, in low-motivation samples, a midpoint can become a cognitive dumping ground for satisficing respondents.
3. Visual Analog Scales (VAS):
   A continuous horizontal line (typically 100 millimeters in length) anchored at the extremes (e.g., "No Pain at All" to "Worst Pain Imaginable"). The respondent marks a point along the line, and the score is measured in millimeters from the left anchor ($0$ to $100$). VAS scales provide continuous interval-level data, eliminating categorical quantization noise, and are standard in clinical pain assessment and psychophysics.

## 4.8 Probability Sampling Designs: SRS, Systematic, Stratified, Cluster, and Multi-Stage
A sampling design is a formal probability sampling mechanism if and only if every unit in the target population has a known, non-zero probability of inclusion ($\pi_i > 0$).

### Foundational Probability Designs:
1. Simple Random Sampling (SRS):
   Every possible subset of size $n$ from population $N$ has an identical probability of selection $\binom{N}{n}^{-1}$, and each individual unit has inclusion probability $\pi_i = n/N$.
2. Systematic Sampling:
   From an ordered list of $N$ units, calculate sampling interval $k = N/n$. Select a random starting integer $r \in [1, k]$, and include units $r, r+k, r+2k, \dots$. Computationally efficient, but vulnerable to catastrophic bias if the list exhibits hidden periodic cycles matching $k$.
3. Stratified Random Sampling:
   The population is partitioned into $H$ mutually exclusive and exhaustive strata. Independent random samples of size $n_h$ are drawn within each stratum.
   - Proportional Allocation: $n_h = n (N_h / N)$.
   - Neyman Optimal Allocation: Maximizes precision for a fixed total sample size $n$ by allocating more samples to strata that are larger and exhibit higher internal variance $\sigma_h$:
   $$n_h = n \frac{N_h \sigma_h}{\sum_{l=1}^H N_l \sigma_l}$$
   Stratification guarantees representation of minority subgroups and always reduces sampling variance relative to SRS ($\mathrm{Var}_{\text{strat}}(\bar{y}_{\text{st}}) \le \mathrm{Var}_{\text{SRS}}(\bar{y})$) because between-strata variance is eliminated from the sampling error.
4. Cluster Sampling:
   The population is divided into natural heterogeneous clusters (e.g., schools, city blocks). A random sample of clusters is drawn, and all units within sampled clusters are enumerated. Reduces travel costs, but increases sampling variance due to intra-cluster correlation ($\mathrm{Deff} > 1.0$).
5. Multi-Stage Sampling:
   Combines stratification and clustering across successive hierarchical administrative levels (e.g., Stage 1: Stratified sampling of districts; Stage 2: Cluster sampling of villages; Stage 3: Systematic sampling of households).

## 4.9 Non-Probability Sampling Pitfalls: Web Panels, Quota Sampling, and Selection Bias
A non-probability sample is one where inclusion probabilities ($\pi_i$) are unknown, and some population members have zero probability of selection. Examples include convenience samples, voluntary opt-in web panels, street-intercept surveys, and snowball samples.

The historical cautionary tale of non-probability sampling is the 1936 *Literary Digest* presidential poll. The magazine mailed $10$ million postcards to individuals selected from automobile registrations and telephone directories, receiving $2.3$ million returned ballots. The poll confidently predicted that Republican Alf Landon would defeat incumbent Franklin D. Roosevelt in a landslide ($57\%$ to $43\%$). In the actual election, Roosevelt won $61\%$ of the popular vote in one of the largest landslides in American history.

The *Literary Digest* failure demonstrates that astronomical sample size ($n = 2.3$ million!) cannot compensate for catastrophic selection bias:
1. Frame Coverage Bias: During the Great Depression, owning an automobile or a home telephone was a luxury restricted to upper-income citizens, who voted disproportionately Republican.
2. Nonresponse Bias: Anti-Roosevelt citizens were far more motivated to return the mail-in postcard than satisfied Roosevelt supporters.

In modern research, commercial opt-in web panels suffer from identical volunteer selection biases: panel participants are younger, more technologically adept, more politically extreme, and more likely to be professional survey-takers than the general population.

## 4.10 Post-Stratification, Raking (Iterative Proportional Fitting), and Calibration Weights
To correct for known sample imbalances resulting from non-coverage and nonresponse, survey statisticians compute post-survey calibration weights.

Let $N$ denote the known population total, and let $N_k$ denote the population counts in demographic cell $k$ obtained from a national census.
1. Post-Stratification Weighting:
   When population counts are known for complete cross-classified demographic cells (e.g., Age $\times$ Sex $\times$ Education):
   $$w_i = \frac{N_k / N}{n_k / n}$$
   Every respondent in cell $k$ receives weight $w_i$.
2. Raking (Iterative Proportional Fitting):
   When census benchmarks are known for marginal distributions (e.g., total population by Age, total population by Sex, total population by Region), but complete multi-way joint cell counts are unavailable, raking executes an iterative proportional adjustment:
   - Step 1: Adjust weights to match the marginal age distribution.
   - Step 2: Adjust weights to match the marginal sex distribution.
   - Step 3: Adjust weights to match the marginal region distribution.
   The algorithm cycles iteratively across all marginal dimensions until the weighted sample margins simultaneously converge to census benchmarks within a specified tolerance $\epsilon$.

The Horvitz-Thompson Estimator uses final calibrated weights $w_i$ to produce unbiased estimates of population totals:
$$\hat{Y}_{\text{HT}} = \sum_{i=1}^n w_i y_i$$

## 4.11 Unit 4 Methodological Synthesis and Review
Survey research methodology is the mathematical science of measuring populations through structured human observation:
- Adopt the Total Survey Error (TSE) perspective, recognizing that unmeasured nonresponse and coverage biases frequently overwhelm sampling error.
- Clarify missing data mechanisms (MCAR, MAR, MNAR) and apply appropriate statistical treatments (multiple imputation, weighting, or selection modeling).
- Engineer questionnaires to minimize cognitive processing failures at comprehension, retrieval, judgment, and reporting stages.
- Account for complex sampling designs (stratification, clustering, multi-stage sampling) using Kish's design effect ($\mathrm{Deff} = 1 + (m-1)\rho$) during sample size planning.
- Protect respondent privacy and elicit honest responses to sensitive attributes using randomized response techniques.
"""

(DRAFT_DIR / "unit-4.md").write_text(u4_content.strip() + "\n", encoding="utf-8")
print("Unit 4 generated.")
