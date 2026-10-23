# Unit 3: Observational & Experimental Study Designs: Cohort, Case-Control, Cross-Sectional & Clinical Trials

The scientific validity of an epidemiologic conclusion depends fundamentally on the architectural rigor of the underlying empirical study design. When assessing whether an environmental exposure, genetic marker, lifestyle behavior, or clinical pharmaceutical causes a given health outcome, investigators cannot rely solely on mathematical modeling; they must gather data through structural protocols that minimize systematic error. In this unit, we formalize the taxonomy of epidemiologic study designs, establishing the theoretical distinctions between observational and experimental investigations, exploring longitudinal tracking in prospective and retrospective cohorts, analyzing case-control sampling paradigms, deriving the mathematics of incidence density sampling in nested case-control studies, examining the prevalence odds ratio in cross-sectional surveys, uncovering the mathematical mechanics of the ecological fallacy, evaluating methodological safeguards in Randomized Controlled Trials (allocation concealment, blinding, intention-to-treat), and assessing the subtle hazards of overmatching.

## 3.1 Taxonomy of Epidemiologic Study Architectures and the Causal Hierarchy

Epidemiologic investigations are classified along three foundational structural axes:
1. **Investigator Manipulation of Exposure**: In **experimental studies** (such as randomized clinical trials and field community trials), the investigator actively assigns the exposure status to each participant according to a predetermined randomization protocol. In **observational studies** (cohort, case-control, cross-sectional, and ecological designs), nature, personal choice, or clinical circumstance dictates exposure, and the investigator observes health trajectories without therapeutic interference.
2. **Timing of Data Collection**: In **prospective studies**, baseline exposure ascertainment precedes the biological occurrence of the disease outcome in real calendar time. In **retrospective studies**, both exposure history and disease outcomes have already occurred before the investigation commences, necessitating historical record abstraction.
3. **Unit of Observation**: In individual-level studies, the data points correspond to distinct individual human beings. In **ecological studies**, the units of observation are aggregate geographic or administrative populations (such as counties, provinces, or nations).

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Study Architecture</th><th>Primary Directionality</th><th>Exposure Ascertainment</th><th>Outcome Measure</th><th>Key Methodological Vulnerability</th></tr>
</thead>
<tbody>
<tr><td><strong>Randomized Trial (RCT)</strong></td><td>Prospective: Exposure $\to$ Outcome</td><td>Investigator-assigned via random allocation</td><td>Risk Ratio, Rate Ratio, Hazard Ratio</td><td>Ethical constraints, non-compliance, limited generalizability.</td></tr>
<tr><td><strong>Prospective Cohort</strong></td><td>Prospective: Exposure $\to$ Outcome</td><td>Measured prior to disease onset in disease-free cohort</td><td>Incidence Rates, Risk Ratio, Hazard Ratio</td><td>Loss to follow-up, high financial cost, long latency periods.</td></tr>
<tr><td><strong>Retrospective Cohort</strong></td><td>Retrospective: Exposure $\to$ Outcome</td><td>Reconstructed from historical employment/medical archives</td><td>Historical Rate Ratio, SMR</td><td>Information quality in archives, healthy worker effect.</td></tr>
<tr><td><strong>Case-Control</strong></td><td>Retrospective: Outcome $\to$ Exposure</td><td>Ascertained after diagnosis among cases and controls</td><td>Exposure Odds Ratio ($OR$)</td><td>Recall bias, selection bias in control recruitment.</td></tr>
<tr><td><strong>Cross-Sectional</strong></td><td>Simultaneous snapshot: Exposure &amp; Outcome</td><td>Concurrent assessment at single point in time</td><td>Prevalence, Prevalence Odds Ratio</td><td>Reverse causality, survivor bias (Neyman bias).</td></tr>
<tr><td><strong>Ecological Study</strong></td><td>Aggregate: Population $\to$ Population</td><td>Group-level averages (e.g. per-capita meat consumption)</td><td>Correlation, Ecological Regression</td><td>Ecological fallacy, unmeasured cross-level confounding.</td></tr>
</tbody>
</table></div>

The classical "evidence hierarchy" positions randomized controlled trials above observational cohort and case-control studies. However, modern causal inference recognizes that observational cohorts often provide far greater external generalizability and represent the only ethically permissible architecture for studying hazardous environmental carcinogens, toxic occupational exposures, or severe social determinants of health.

## 3.2 Prospective and Retrospective Cohort Studies: Design, Tracking, and Attrition

The **cohort design** represents the most intuitive observational architecture for evaluating etiology because its temporal sequence perfectly mirrors biological causation: exposure status is documented among disease-free individuals at baseline, and participants are followed forward through time to measure the subsequent incidence of disease.

### Cohort Assembly and Exposure Measurement
A cohort begins with the identification of an initial population at risk. Any individual who already possesses the study outcome at baseline must be excluded to prevent prevalent cases from contaminating incident event counts. Exposure can be:
- **Dichotomous**: Ever-smoker vs never-smoker; occupational asbestos contact vs unexposed administration.
- **Multilevel Categorical**: Cigarette consumption grouped as zero, 1–10, 11–20, or >20 cigarettes per day.
- **Continuous and Time-Varying**: Cumulative pack-years, annual average serum cholesterol levels, or cumulative radiation millisieverts.

In a **prospective cohort study** (such as the Framingham Heart Study or the Nurses’ Health Study), investigators enroll participants in current calendar time and conduct longitudinal follow-up through periodic clinical examinations, mobile health monitors, questionnaire mailings, and vital statistics linkages. In a **retrospective (historical) cohort study**, the cohort is assembled in current time, but baseline entry occurred at an earlier calendar date (for example, all chemical factory workers employed between 1970 and 1985). So long as exposure records were created before disease diagnosis, retrospective cohorts maintain true forward directionality.

### The Threat of Loss to Follow-Up and Informative Censoring
The primary threat to the internal validity of any longitudinal cohort study is **attrition** (loss to follow-up). If individuals who migrate away or withdraw consent have identical disease risks to those who remain under observation, loss to follow-up merely reduces sample size and statistical power (non-informative censoring). However, if withdrawal is statistically dependent on both exposure and impending disease onset—for instance, if exposed workers who develop subtle early respiratory symptoms emigrate from the study area or retire early—the attrition is **informative**, producing severe selection bias that distorts the estimated rate ratio toward or away from the null.

To handle variable follow-up durations rigorously, epidemiologists compute person-time denominators or construct non-parametric Kaplan-Meier survival curves and Cox proportional hazards regression models.

## 3.3 Case-Control Studies: Case Definition, Control Selection Paradigms & Density Sampling

For rare health outcomes or diseases with multi-decade latency periods (such as mesothelioma or glioblastoma), a prospective cohort study is practically unfeasible: enrolling and tracking $100,000$ healthy individuals for thirty years might yield only ten cases, consuming immense financial resources. The **case-control study** resolves this inefficiency by sampling all diagnosed cases within a defined population base, accompanied by a modest, informative sample of healthy controls who represent the person-time experience that generated those cases.

### Principles of Valid Control Selection
The scientific credibility of a case-control study rests entirely upon the selection of the control series. Modern epidemiologic theory formalizes control selection through the **Study Base Principle**:
1. **The Would-Criterion**: Controls must be sampled from the identical source population (study base) that produced the cases. That is, if a control individual had instead developed the disease under investigation during the study window, they would have been captured as a case in the study's clinical registry.
2. **Exposure Independence**: Control selection must be entirely independent of exposure status. Selecting controls with diseases that share the exposure of interest (e.g., using chronic bronchitis patients as hospital controls in a lung cancer study of cigarette smoking) produces catastrophic bias toward the null.

### Three Paradigms of Control Selection
Depending on the sampling frame within the underlying base population, case-control studies conform to three distinct mathematical structures:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Control Selection Paradigm</th><th>Sampling Mechanics</th><th>Parameter Estimated by $OR$</th><th>Rare Disease Requirement</th></tr>
</thead>
<tbody>
<tr><td><strong>Cumulative (Survivor) Sampling</strong></td><td>Controls sampled from disease-free survivors at the end of the follow-up window.</td><td>Odds Ratio ($OR$); estimates Risk Ratio ($RR$) only if disease is rare.</td><td>Strictly required ($R < 0.05$).</td></tr>
<tr><td><strong>Case-Cohort Sampling</strong></td><td>Controls sampled as a random subcohort from the entire baseline population ($N_0$) at $t = 0$.</td><td>Direct estimate of Risk Ratio ($RR$); cases can also belong to the subcohort.</td><td>Not required; valid for common diseases.</td></tr>
<tr><td><strong>Incidence Density (Risk-Set) Sampling</strong></td><td>Each time a new case arises at $t$, controls are randomly sampled from all disease-free members at that instant.</td><td>Direct, unbiased estimate of the Incidence Rate Ratio ($IRR$).</td><td>Not required; completely distribution-free.</td></tr>
</tbody>
</table></div>

### Incidence Density (Risk-Set) Sampling in Nested Case-Control Studies
In a nested case-control study conducted within a well-defined cohort, whenever a case is diagnosed at failure time $t_j$, one or more controls are randomly selected from the **risk set** $\mathcal{R}(t_j)$ of individuals who are currently alive, under active observation, and free of disease at that exact moment. Under incidence density sampling, an individual who serves as a control at $t_1$ may subsequently develop the disease at a later time $t_2$ and become a case. Furthermore, an individual may be sampled as a control on multiple distinct occasions.

By virtue of this time-matched sampling mechanism, the exposure odds ratio in the case-control sample is a mathematically unbiased estimator of the population incidence rate ratio:

$$\widehat{OR}_{\text{density}} \xrightarrow{p} IRR = \frac{\lambda_1}{\lambda_0}$$

This estimator requires **zero rare disease assumption**, functioning flawlessly regardless of whether the cumulative incidence is $0.1\%$ or $80\%$.

## 3.4 Cross-Sectional Studies, Prevalence Odds Ratios & The Ecological Fallacy

In a **cross-sectional study** (also known as a prevalence survey), exposure status and health outcome are ascertained simultaneously for each participant at a single calendar cross-section. Cross-sectional studies are widely used in public health to assess the burden of chronic conditions (such as diabetes, hypertension, or depression) and evaluate healthcare utilization.

### The Prevalence Odds Ratio (POR) and Length-Biased Sampling
In cross-sectional analysis, the measure of association is the **Prevalence Odds Ratio** ($POR$):

$$POR = \frac{P_1 / (1 - P_1)}{P_0 / (1 - P_0)}$$

Recalling from Unit 1 that $P / (1 - P) = I \times \bar{T}_D$ under stationary equilibrium, substituting the exposure-specific equations gives:

$$POR = \frac{I_1 \cdot \bar{T}_{D1}}{I_0 \cdot \bar{T}_{D0}} = \left(\frac{I_1}{I_0}\right) \times \left(\frac{\bar{T}_{D1}}{\bar{T}_{D0}}\right) = IRR \times \left(\frac{\bar{T}_{D1}}{\bar{T}_{D0}}\right)$$

This identity reveals that the Prevalence Odds Ratio equals the true Incidence Rate Ratio **if and only if** the mean disease duration is identical in exposed and unexposed cases ($\bar{T}_{D1} = \bar{T}_{D0}$). If the exposure affects disease survival—for example, if exposure to a genetic polymorphism accelerates mortality, reducing survival duration from five years to six months—prevalent cases will systematically under-represent exposed individuals. This distortion is termed **length-biased sampling** or **Neyman’s prevalence-incidence bias**. Furthermore, because exposure and disease are measured at the same instant, cross-sectional studies are inherently vulnerable to **reverse causality** (e.g., individuals with severe joint pain ceasing physical exercise, creating a misleading cross-sectional association between inactivity and arthritis).

### The Ecological Fallacy (Robinson's Paradox)
An **ecological study** analyzes relationships between exposure and disease aggregated at the group level (such as countries or administrative districts). While inexpensive and useful for generating etiologic hypotheses, ecological studies are fundamentally vulnerable to the **ecological fallacy**: the logical error of inferring individual-level causal associations from aggregate population-level correlations.

In 1950, William S. Robinson demonstrated this mathematical reality empirically using 1930 US Census data. Robinson examined the correlation between literacy and being an immigrant (foreign-born). Across the 48 states, the aggregate ecological correlation was strongly positive ($r = +0.53$), suggesting that states with higher proportions of foreign-born residents had higher literacy rates. However, when evaluated at the level of the 97 million individual citizens, the correlation was actually negative ($r = -0.11$): foreign-born individuals had a lower individual probability of literacy than native-born citizens. The ecological correlation was confounded because newly arriving immigrants settled overwhelmingly in affluent, industrialized northern states with superior public educational infrastructure. Mathematically, the ecological covariance between aggregate variables $\bar{X}_k$ and $\bar{Y}_k$ across $K$ groups decomposes into:

$$\text{Cov}(\bar{X}, \bar{Y}) = \mathbb{E}[\text{Cov}(X, Y \mid k)] + \text{Cov}(\mathbb{E}[X \mid k], \, \mathbb{E}[Y \mid k])$$

The individual within-group association $\mathbb{E}[\text{Cov}(X, Y \mid k)]$ can possess an entirely opposite sign from the between-group cross-level ecological covariance $\text{Cov}(\mathbb{E}[X \mid k], \, \mathbb{E}[Y \mid k])$.

## 3.5 Randomized Controlled Trials: Allocation Concealment, Blinding & Intention-to-Treat

The **Randomized Controlled Trial** (RCT) is universally recognized as the gold standard for clinical efficacy evaluation because random assignment breaks the statistical dependence between treatment allocation and both measured and unmeasured prognostic baseline confounders.

### Mechanics of Random Allocation and Allocation Concealment
Randomization ensures that each enrolled participant possesses a known, non-zero probability of receiving the experimental therapy. Standard techniques include:
- **Simple Randomization**: Equivalent to an unweighted coin toss; can lead to sample size imbalances in small trials.
- **Permuted Block Randomization**: Constrains treatment assignments within balanced blocks of pre-specified size (e.g., blocks of size 4 or 6), guaranteeing equal group numbers throughout recruitment.
- **Stratified Randomization**: Performs permuted block randomization within distinct clinical strata (e.g., stratified by age <65 vs $\ge 65$ or disease stage), ensuring balance across major prognostic covariates.

Crucially, randomization is completely compromised without **allocation concealment**. Allocation concealment prevents clinical investigators from knowing or predicting which treatment arm the next eligible patient will receive before enrollment. Without strict concealment (e.g., centralized web-based randomization or opaque, sequentially numbered sealed envelopes), clinicians subconsciously steer sicker patients toward preferred therapies, destroying baseline exchangeability.

### Masking (Blinding)
To prevent psychological biases and differential clinical co-interventions:
- **Single-Blind**: The patient is unaware of treatment assignment.
- **Double-Blind**: Both the patient and the treating clinicians / outcome adjudicators are unaware of treatment assignment.
- **Triple-Blind**: The patient, clinicians, outcome adjudicators, and the Data and Safety Monitoring Board (DSMB) biostatisticians analyzing interim data remain masked to treatment identity.

### Intention-to-Treat (ITT) vs Per-Protocol (PP) Analysis
In real-world clinical trials, patients inevitably deviate from assigned protocols: some experience drug intolerance and discontinue medication, others forget doses, and some control patients cross over to receive the active therapy. Epidemiologists analyze such trials using two contrasting paradigms:

1. **Intention-to-Treat (ITT) Principle**:
   Under ITT, every randomized patient is analyzed within the treatment group to which they were originally assigned, regardless of whether they adhered to the protocol, took a single dose of medication, experienced adverse effects, or crossed over:
   $$\text{"Once randomized, always analyzed."}$$
   ITT preserves the pristine baseline exchangeability guaranteed by randomization. It provides a pragmatic estimate of the **effectiveness** of prescribing the therapy in real-world clinical practice, where non-adherence is ubiquitous. Furthermore, ITT prevents informative dropout bias; excluding non-adherent patients who stopped therapy due to early adverse symptoms would falsely exaggerate treatment safety and efficacy.

2. **Per-Protocol (PP) Analysis**:
   PP analysis restricts the analytic cohort exclusively to patients who strictly completed the pre-specified therapeutic regimen without major protocol violations. While PP analysis attempts to evaluate biological **efficacy** under ideal compliance, it is fundamentally an observational comparison: patients who adhere to therapy are systematically healthier, more conscientious, and have better baseline prognoses than non-adherent patients. Consequently, PP analyses are prone to substantial confounding.

## 3.6 Matching Strategies in Design: Individual vs Frequency Matching, Overmatching

In observational case-control and cohort designs, **matching** is an architectural strategy in which the investigator deliberately selects controls so that they resemble cases across designated potential confounding variables (such as age, sex, or socioeconomic status).

### Individual vs Frequency Matching
- **Individual (Pair) Matching**: Each diagnosed case is explicitly linked to one or more designated controls who share identical matching covariates (e.g., a 52-year-old female case is matched to a 52-year-old female control in a 1:1 or 1:$M$ ratio).
- **Frequency (Stratum) Matching**: Controls are selected so that the aggregate distribution of the matching covariate matches that of the cases (e.g., if $40\%$ of cases are female and $30\%$ are over age 60, controls are recruited to exhibit those identical marginal proportions).

### The Paradox of Matching in Case-Control Studies
A common misconception among beginner epidemiologists is that matching in a case-control study automatically controls for confounding. In reality, **matching in a case-control study introduces selection bias**! By forcing controls to possess the same covariate distribution as cases, the investigator artificially distorts the exposure distribution among controls toward that of the cases. If the matched variable $Z$ is positively associated with exposure $E$, matching artificially enriches the control sample with exposed individuals, biasing the crude odds ratio toward the null ($OR \to 1.0$). Therefore, matching in a case-control study requires matched statistical analysis (such as McNemar’s test for 1:1 pairs or conditional logistic regression). Matching is performed primarily to gain statistical efficiency, not to remove confounding without stratified modeling.

### Overmatching
Overmatching occurs when an investigator matches on an improper variable:
1. **Matching on an Intermediate Variable**: If variable $M$ lies on the direct causal pathway between exposure $E$ and outcome $D$ ($E \to M \to D$), matching on $M$ blocks the causal effect, attenuating the observed association toward zero.
2. **Matching on a Non-Confounding Exposure Correlate**: If variable $W$ is associated with exposure $E$ but has no independent causal link to disease $D$, matching on $W$ serves no confounding control purpose but artificially inflates the exposure similarity between cases and controls, destroying statistical efficiency and widening confidence intervals without scientific justification.

## Fully worked question 1: Competing Risks and Life-Table Attrition in Prospective Cohorts

### Question
An occupational health institute conducts an 8-year prospective cohort study monitoring $N_0 = 1,000$ underground hard-rock miners exposed to high levels of respirable crystalline silica to measure the incidence of silicosis. Over the 8-year follow-up, the cohort experiences both incident silicosis events and attrition from competing mortality (accidents, heart disease) and migration. The year-by-year life-table accounting is:

- **Year 1**: 1,000 miners enter; 20 develop silicosis; 10 withdraw/emigrate; 10 die from competing causes.
- **Year 2**: 960 miners enter; 30 develop silicosis; 20 withdraw/emigrate; 10 die from competing causes.
- **Year 3**: 900 miners enter; 45 develop silicosis; 15 withdraw/emigrate; 10 die from competing causes.
- **Year 4**: 830 miners enter; 40 develop silicosis; 10 withdraw/emigrate; 10 die from competing causes.
- **Year 5**: 770 miners enter; 35 develop silicosis; 15 withdraw/emigrate; 10 die from competing causes.
- **Year 6**: 710 miners enter; 30 develop silicosis; 10 withdraw/emigrate; 10 die from competing causes.
- **Year 7**: 660 miners enter; 25 develop silicosis; 15 withdraw/emigrate; 10 die from competing causes.
- **Year 8**: 610 miners enter; 20 develop silicosis; 10 withdraw/emigrate; 10 die from competing causes.

1. Under the standard actuarial assumption that censored and competing-event individuals contribute an average of half a year of observation during their exit year, calculate the effective number of miners at risk $n_t'$ for each of the 8 annual intervals.
2. Calculate the conditional annual risk of silicosis $q_t$, the conditional probability of remaining free of silicosis $p_t = 1 - q_t$, and compute the cumulative probability of remaining silicosis-free over the entire 8-year period using the **Cutler-Ederer actuarial life-table method**.
3. Determine the 8-year cumulative incidence of silicosis, and calculate Greenwood’s standard error and 95% confidence interval for the 8-year cumulative survival probability.

### Solution, step 1: Actuarial effective denominator at risk
Under the actuarial life-table convention, if $l_t$ miners enter interval $t$, $d_t$ develop silicosis, and $w_t$ are censored (combining withdrawals and competing deaths), the effective number at risk is:

$$n_t' = l_t - \frac{w_t}{2}$$

Let $w_t = \text{withdrawals} + \text{competing deaths}$. We evaluate for each year:
- **Year 1**: $l_1 = 1000, d_1 = 20, w_1 = 10 + 10 = 20 \implies n_1' = 1000 - 10 = 990$.
- **Year 2**: $l_2 = 960, d_2 = 30, w_2 = 20 + 10 = 30 \implies n_2' = 960 - 15 = 945$.
- **Year 3**: $l_3 = 900, d_3 = 45, w_3 = 15 + 10 = 25 \implies n_3' = 900 - 12.5 = 887.5$.
- **Year 4**: $l_4 = 830, d_4 = 40, w_4 = 10 + 10 = 20 \implies n_4' = 830 - 10 = 820$.
- **Year 5**: $l_5 = 770, d_5 = 35, w_5 = 15 + 10 = 25 \implies n_5' = 770 - 12.5 = 757.5$.
- **Year 6**: $l_6 = 710, d_6 = 30, w_6 = 10 + 10 = 20 \implies n_6' = 710 - 10 = 700$.
- **Year 7**: $l_7 = 660, d_7 = 25, w_7 = 15 + 10 = 25 \implies n_7' = 660 - 12.5 = 647.5$.
- **Year 8**: $l_8 = 610, d_8 = 20, w_8 = 10 + 10 = 20 \implies n_8' = 610 - 10 = 600$.

### Solution, step 2: Conditional probabilities and cumulative survival
Evaluate the conditional failure probabilities $q_t = d_t / n_t'$ and survival probabilities $p_t = 1 - q_t$:
- Year 1: $q_1 = 20 / 990 \approx 0.020202 \implies p_1 = 0.979798$
- Year 2: $q_2 = 30 / 945 \approx 0.031746 \implies p_2 = 0.968254$
- Year 3: $q_3 = 45 / 887.5 \approx 0.050704 \implies p_3 = 0.949296$
- Year 4: $q_4 = 40 / 820 \approx 0.048780 \implies p_4 = 0.951220$
- Year 5: $q_5 = 35 / 757.5 \approx 0.046205 \implies p_5 = 0.953795$
- Year 6: $q_6 = 30 / 700 \approx 0.042857 \implies p_6 = 0.957143$
- Year 7: $q_7 = 25 / 647.5 \approx 0.038610 \implies p_7 = 0.961390$
- Year 8: $q_8 = 20 / 600 \approx 0.033333 \implies p_8 = 0.966667$

The cumulative probability of remaining free of silicosis at the end of 8 years is the product:

$$\widehat{S}(8) = \prod_{t=1}^8 p_t = (0.979798)(0.968254)(0.949296)(0.951220)(0.953795)(0.957143)(0.961390)(0.966667)$$
$$= 0.71832 \quad (71.83\%)$$

The 8-year cumulative incidence of silicosis, correctly adjusted for competing mortality and loss to follow-up, is:

$$CI(8) = 1 - \widehat{S}(8) = 1 - 0.71832 = 0.28168 \quad (28.17\%)$$

Notice that a naive calculation dividing total cases ($\sum d = 245$) by initial miners ($1,000$) gives $24.5\%$, underestimating true risk because 185 miners were censored before completing 8 years.

### Solution, step 3: Greenwood's formula and 95% confidence interval
Greenwood’s formula for the variance of the actuarial survival estimate is:

$$\text{Var}(\widehat{S}(8)) = [\widehat{S}(8)]^2 \sum_{t=1}^8 \frac{q_t}{n_t' p_t} = [\widehat{S}(8)]^2 \sum_{t=1}^8 \frac{d_t}{n_t'(n_t' - d_t)}$$

Calculate each term:
- Year 1: $20 / (990 \times 970) = 20 / 960,300 \approx 2.0827 \times 10^{-5}$
- Year 2: $30 / (945 \times 915) = 30 / 864,675 \approx 3.4695 \times 10^{-5}$
- Year 3: $45 / (887.5 \times 842.5) = 45 / 747,718.75 \approx 6.0183 \times 10^{-5}$
- Year 4: $40 / (820 \times 780) = 40 / 639,600 \approx 6.2539 \times 10^{-5}$
- Year 5: $35 / (757.5 \times 722.5) = 35 / 547,293.75 \approx 6.3951 \times 10^{-5}$
- Year 6: $30 / (700 \times 670) = 30 / 490,000 \approx 6.1224 \times 10^{-5}$
- Year 7: $25 / (647.5 \times 622.5) = 25 / 403,068.75 \approx 6.2024 \times 10^{-5}$
- Year 8: $20 / (600 \times 580) = 20 / 348,000 \approx 5.7471 \times 10^{-5}$

Summing the components:
$$\sum_{t=1}^8 \frac{q_t}{n_t' p_t} \approx 42.2914 \times 10^{-5} = 0.000422914$$

The variance is:
$$\text{Var}(\widehat{S}(8)) = (0.71832)^2 \times 0.000422914 = (0.51598) \times 0.000422914 \approx 0.00021822$$

The standard error is:
$$\text{SE}(\widehat{S}(8)) = \sqrt{0.00021822} \approx 0.01477 \quad (1.48\%)$$

The 95% Wald confidence interval for 8-year survival is:
$$\widehat{S}(8) \pm 1.96 \times \text{SE}(\widehat{S}(8)) = 0.71832 \pm 1.96(0.01477) = 0.71832 \pm 0.02895 = [0.6894, \, 0.7473]$$

The corresponding 95% confidence interval for 8-year cumulative incidence of silicosis is $[25.27\%, \, 31.06\%]$.

## Fully worked question 2: Nested Case-Control Design with Risk-Set Incidence Density Sampling

### Question
Within a prospective occupational cohort of $N = 25,000$ chemical refinery technicians followed for 20 years, an investigator investigates whether chronic occupational exposure to trichloroethylene (TCE) causes renal cell carcinoma (RCC). Over 400,000 person-years of tracking, exactly $d = 60$ incident RCC cases occur. To avoid the massive expense of retrieving and analyzing historical occupational exposure logs and biobanked urine biomarkers for all 25,000 workers, the epidemiologist implements a **nested case-control study using incidence density (risk-set) sampling**:
- At the failure time of each diagnosed RCC case, exactly $M = 4$ controls are randomly sampled from the active risk set $\mathcal{R}(t)$ (cohort members currently alive, under observation, and free of RCC at that exact date).
- Across the $60$ risk-set matched strata (each containing 1 case and 4 controls, total $N_{\text{sample}} = 60 \times 5 = 300$ worker records), exposure history is abstracted.
- Stratified analysis by case-control discordant pairs reveals that among the 60 cases, 36 were exposed to TCE and 24 were unexposed. Among the 240 matched controls, 60 were exposed to TCE and 180 were unexposed.
- The Mantel-Haenszel summary calculation across the 60 matched risk sets yields $\sum a_i d_i / T_i = 21.6$ and $\sum b_i c_i / T_i = 7.2$.

1. Explain why incidence density sampling directly estimates the population Incidence Rate Ratio ($IRR$) without requiring the rare disease assumption.
2. Calculate the sample Odds Ratio ($\widehat{OR}_{\text{density}}$) from the risk-set matched data. What does this indicate regarding the renal carcinogenicity of TCE?
3. Calculate the conditional maximum likelihood variance $\text{Var}(\ln \widehat{OR}) \approx \frac{1}{\sum a_i d_i / T_i} + \frac{1}{\sum b_i c_i / T_i}$, construct the 95% confidence interval for the $IRR$, and test the null hypothesis $H_0: IRR = 1$ via the matched Mantel-Haenszel score test.

### Solution, step 1: Theoretical justification of incidence density sampling
In a dynamic cohort with hazard rate $\lambda_1(t)$ among exposed and $\lambda_0(t)$ among unexposed workers, the probability that a case arising at time $t$ is exposed is:

$$P(\text{Case is } E^+ \mid \text{Event at } t) = \frac{N_1(t) \lambda_1(t)}{N_1(t) \lambda_1(t) + N_0(t) \lambda_0(t)}$$

where $N_1(t)$ and $N_0(t)$ are the number of exposed and unexposed individuals in the risk set $\mathcal{R}(t)$. When controls are randomly sampled from $\mathcal{R}(t)$ at time $t$, the expected exposure odds among controls is:

$$\text{Expected Control Odds} = \frac{E[b \mid \mathcal{R}(t)]}{E[d \mid \mathcal{R}(t)]} = \frac{N_1(t)}{N_0(t)}$$

The ratio of case exposure odds to control exposure odds at time $t$ is:

$$\frac{P(E^+ \mid \text{Case}) / P(E^- \mid \text{Case})}{E[b] / E[d]} = \frac{N_1(t) \lambda_1(t) / [N_0(t) \lambda_0(t)]}{N_1(t) / N_0(t)} = \frac{\lambda_1(t)}{\lambda_0(t)} = IRR$$

Because controls represent the person-time distribution at the moment cases develop, the ratio $N_1(t) / N_0(t)$ cancels out identically. This cancellation holds regardless of whether the disease is rare or common. Thus, incidence density sampling provides an unbiased estimate of the true continuous-time hazard rate ratio $IRR$.

### Solution, step 2: Calculate matched odds ratio point estimate
Using the Mantel-Haenszel pooled estimator across the 60 risk sets:

$$\widehat{OR}_{\text{density}} = \frac{\sum_{i=1}^{60} \frac{a_i d_i}{T_i}}{\sum_{i=1}^{60} \frac{b_i c_i}{T_i}} = \frac{21.6}{7.2} = 3.00$$

The estimated Incidence Rate Ratio is $\widehat{IRR} = 3.00$. Workers exposed to trichloroethylene experience a three-fold higher rate of incident renal cell carcinoma per person-year at risk compared to unexposed refinery workers.

### Solution, step 3: Variance estimation, 95% confidence interval, and test of significance
1. **Variance and Standard Error on the Log Scale**:
   Using the Robins-Breslow-Greenland matched variance formula:
   $$\text{Var}(\ln \widehat{IRR}) \approx \frac{1}{\sum \frac{a_i d_i}{T_i}} + \frac{1}{\sum \frac{b_i c_i}{T_i}} = \frac{1}{21.6} + \frac{1}{7.2} = 0.046296 + 0.138889 = 0.185185$$
   $$\text{SE}(\ln \widehat{IRR}) = \sqrt{0.185185} \approx 0.43033$$

2. **95% Confidence Interval**:
   $$\ln(\widehat{IRR}) = \ln(3.00) = 1.09861$$
   $$\text{Log Limits} = 1.09861 \pm 1.96(0.43033) = 1.09861 \pm 0.84345 = [0.25516, \, 1.94206]$$
   $$IRR_{\text{lower}} = \exp(0.25516) \approx 1.291, \qquad IRR_{\text{upper}} = \exp(1.94206) \approx 6.973$$
   $$CI_{0.95}(IRR) = [1.29, \, 6.97]$$

3. **Matched Mantel-Haenszel Chi-Square Test**:
   The test statistic contrasts observed case exposures $O = \sum a_i = 36$ against expected exposures under the null $E = \sum \frac{m_{1i} n_{1i}}{T_i}$. In 1:4 matched sets where $m_{1i} = 1$ and $T_i = 5$, the null probability that the case is exposed is $n_{1i} / 5$. The variance under $H_0$ is $\text{Var}(O) = \sum \frac{n_{1i} n_{0i} m_{1i} m_{0i}}{T_i^2 (T_i - 1)}$.
   Here, the score statistic evaluates to:
   $$\chi^2_{\text{MH}} = \frac{(21.6 - 7.2)^2}{21.6 + 7.2} = \frac{(14.4)^2}{28.8} = \frac{207.36}{28.8} = 7.20$$

Comparing $\chi^2 = 7.20$ against the chi-square distribution with $1$ degree of freedom:
$$p = P(\chi^2_1 \ge 7.20) \approx 0.0073$$
Because $p < 0.01$, the positive association between trichloroethylene exposure and renal cell carcinoma is highly statistically significant.

## Fully worked question 3: Randomized Controlled Trial Analysis: Intention-to-Treat vs Per-Protocol

### Question
An international multicenter double-blind randomized clinical trial evaluates a novel biologic monoclonal antibody (Drug X) versus Placebo for preventing Crohn's disease relapses over 52 weeks. Exactly $N = 1,000$ active Crohn's disease patients are randomized in a 1:1 ratio:
- **Assigned to Drug X**: $n_{\text{Drug}} = 500$ patients.
- **Assigned to Placebo**: $n_{\text{Placebo}} = 500$ patients.

During the 52-week trial, protocol non-adherence and side effects occur:
- In the **Drug X arm**: 100 patients experience mild gastrointestinal side effects and stop taking Drug X at week 4, crossing over to conventional therapy. By week 52, 20 of these 100 non-adherent patients relapse. Among the 400 patients who strictly adhered to Drug X for the entire 52 weeks, 80 relapse.
- In the **Placebo arm**: 50 patients withdraw from the study due to lack of efficacy at week 12 and seek alternative biologics outside the trial. By week 52, 30 of these 50 non-adherent patients relapse. Among the 450 patients who strictly adhered to Placebo, 180 relapse.

1. Perform a complete **Intention-to-Treat (ITT)** analysis: calculate the 1-year relapse risk in both randomized arms, the Risk Ratio ($RR_{\text{ITT}}$), the Absolute Risk Reduction ($ARR_{\text{ITT}}$), and the $NNT$.
2. Perform a **Per-Protocol (PP)** analysis restricting the sample exclusively to the adherent patients in both arms: calculate the relapse risks, $RR_{\text{PP}}$, $ARR_{\text{PP}}$, and $NNT$.
3. Compare the findings: explain why the Per-Protocol analysis yields a more optimistic efficacy estimate but introduces potential confounding, and state why regulatory agencies (such as the FDA and EMA) mandate ITT as the primary analysis.

### Solution, step 1: Intention-to-Treat (ITT) analysis
Under the ITT principle, all 500 patients randomized to Drug X are analyzed in the Drug X arm, and all 500 patients randomized to Placebo are analyzed in the Placebo arm, regardless of compliance.

1. **Total Relapses in Drug X Arm**:
   $$\text{Relapses}_{\text{Drug}} = 20 \text{ (non-adherent)} + 80 \text{ (adherent)} = 100 \text{ relapses}$$
   $$R_{\text{ITT, Drug}} = \frac{100}{500} = 0.2000 \quad (20.00\%)$$

2. **Total Relapses in Placebo Arm**:
   $$\text{Relapses}_{\text{Placebo}} = 30 \text{ (non-adherent)} + 180 \text{ (adherent)} = 210 \text{ relapses}$$
   $$R_{\text{ITT, Placebo}} = \frac{210}{500} = 0.4200 \quad (42.00\%)$$

3. **ITT Effect Measures**:
   $$RR_{\text{ITT}} = \frac{R_{\text{ITT, Drug}}}{R_{\text{ITT, Placebo}}} = \frac{0.2000}{0.4200} \approx 0.4762 \quad (47.62\%)$$
   $$ARR_{\text{ITT}} = R_{\text{ITT, Placebo}} - R_{\text{ITT, Drug}} = 0.4200 - 0.2000 = 0.2200 \quad (22.00\%)$$
   $$NNT_{\text{ITT}} = \frac{1}{ARR_{\text{ITT}}} = \frac{1}{0.2200} \approx 4.55 \approx 5 \text{ patients}$$

Under real-world prescription conditions (including non-adherence), Drug X reduces Crohn's relapse risk by $52.38\%$ ($RRR = 1 - 0.4762$), with an $NNT$ of 5 patients.

### Solution, step 2: Per-Protocol (PP) analysis
The Per-Protocol analysis excludes the 100 non-adherent Drug X patients and the 50 non-adherent Placebo patients, evaluating only the $400 + 450 = 850$ compliant patients.

1. **Relapse Risks in Adherent Cohort**:
   $$R_{\text{PP, Drug}} = \frac{80}{400} = 0.2000 \quad (20.00\%)$$
   $$R_{\text{PP, Placebo}} = \frac{180}{450} = 0.4000 \quad (40.00\%)$$

2. **PP Effect Measures**:
   $$RR_{\text{PP}} = \frac{R_{\text{PP, Drug}}}{R_{\text{PP, Placebo}}} = \frac{0.2000}{0.4000} = 0.5000 \quad (50.00\%)$$
   $$ARR_{\text{PP}} = 0.4000 - 0.2000 = 0.2000 \quad (20.00\%)$$
   $$NNT_{\text{PP}} = \frac{1}{0.2000} = 5.00 \text{ patients}$$

### Solution, step 3: Methodological comparison and regulatory rationale
In this trial:
- In the Placebo arm, the non-adherent patients who dropped out had a relapse risk of $30 / 50 = 60\%$, compared to $40\%$ among compliant placebo patients. These patients were experiencing aggressive Crohn's flare-ups that forced them to seek rescue biologics.
- In the Drug X arm, the non-adherent patients dropped out because of mild side effects, yet their relapse risk was only $20 / 100 = 20\%$.

When the Per-Protocol analysis discarded the 50 sicker Placebo dropouts, it artificially lowered the Placebo relapse rate from $42\%$ to $40\%$. In other clinical trials, the distortion is often far worse: discarding non-adherent patients who experience severe adverse drug toxicity creates a fraudulent impression of pharmaceutical safety and efficacy.

**Regulatory Mandate for ITT**:
Regulatory authorities (FDA, EMA) require Intention-to-Treat as the primary analysis because:
1. **Preservation of Randomization**: ITT guarantees that the treatment arms remain strictly exchangeable at baseline, balancing unobserved biological covariates.
2. **Protection Against Selection Bias**: Post-randomization exclusions in Per-Protocol analyses reintroduce observational confounding.
3. **Pragmatic Generalizability**: ITT reflects true clinical effectiveness in human populations where perfect lifelong compliance never occurs.
