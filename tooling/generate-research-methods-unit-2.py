from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-statistical-research-methods"

u2_content = r"""# Unit 2: Problem Formulation, Conceptualization & Research Design Architectures

The architectural integrity of an empirical study is established long before the first data point is collected, transformed, or analyzed. No sophisticated mathematical algorithm, Bayesian hierarchical model, or machine learning ensemble can salvage an empirical study plagued by a fundamentally flawed research design. As the eminent statistician Sir Ronald A. Fisher famously declared in 1938 to the Indian Statistical Congress: *"To consult the statistician after an experiment is finished is often merely to ask him to conduct a post mortem examination. He can perhaps say what the experiment died of."*

Research design constitutes the deliberate structural blueprint for collecting, organizing, and analyzing empirical data in a manner that maximizes evidentiary validity while minimizing bias, systematic distortion, and random error. This unit investigates the rigorous formalization of scientific research questions into operational hypotheses, examines the classical taxonomy of research designs, dissects threats to validity, and provides the mathematical principles governing modern experimental and quasi-experimental architectures.

## 2.1 Translating Substantive Research Inquiries into Formal Statistical Hypotheses
Scientific inquiry begins with a substantive domain question—a conceptual curiosity regarding a real-world phenomenon. Examples include:
- "Does maternal dietary supplementation with micronutrients improve infant cognitive development in rural communities?"
- "Does reducing corporate tax rates stimulate domestic private sector capital investment?"
- "Does algorithmic content moderation suppress political discourse on digital social platforms?"

While substantive domain questions inspire research, they cannot be tested directly in their raw conceptual form. They lack mathematical specificity. A substantive research question must undergo formal translation into operational statistical hypotheses.

This translation proceeds through a rigorous four-stage hierarchy:
1. Substantive Theory: A conceptual framework proposing mechanisms connecting abstract constructs (e.g., "Maternal Nutritional Status" $\to$ "Infant Neurological Maturation").
2. Conceptual Research Hypothesis ($H_{\text{research}}$): A directional proposition specifying expected relationships between theoretical concepts (e.g., "Increased maternal intake of folate and iron during the second trimester increases infant working memory capacity at 12 months").
3. Operational Statistical Hypotheses ($H_0$ and $H_1$): Formal mathematical statements regarding the parameters of a well-defined probability distribution or statistical model:
$$H_0: \mu_{\text{treatment}} - \mu_{\text{control}} \le 0 \quad \text{versus} \quad H_1: \mu_{\text{treatment}} - \mu_{\text{control}} > 0$$
or in a generalized regression formulation:
$$H_0: \beta_{\text{supplement}} = 0 \quad \text{versus} \quad H_1: \beta_{\text{supplement}} > 0$$
4. Test Statistic and Decision Rule: The mathematical function of sample data $T(\mathbf{X})$ and rejection region $\mathcal{R}_\alpha$ that dictates whether $H_0$ is rejected.

A severe error in research methodology is construct mismatch: formulating an operational hypothesis that fails to represent the substantive theory. For example, if a researcher tests whether maternal supplements increase infant birth weight, finding no significant effect on birth weight does not refute the hypothesis that supplements improve *cognitive development*, because fetal physical mass is not an isomorphic indicator of neurological synaptic density.

## 2.2 Conceptualization, Operationalization, and Latent Construct Indicators
Most foundational entities in social, behavioral, and biomedical sciences are unobservable latent constructs: abstract conceptual entities that cannot be measured directly with physical sensors. Examples include intelligence, socio-economic status, depression, organizational culture, patient well-being, and brand loyalty.

Empirical investigation requires operationalization: the formal process of defining the exact measurement operations, behavioral indicators, and computational instruments used to quantify a latent construct:
- Conceptual Definition: A theoretical description of the construct's essential properties, scope, and boundaries (e.g., "Depression is a mood state characterized by persistent sadness, anhedonia, neurovegetative disruption, and feelings of worthlessness").
- Operational Definition: The explicit measurement protocol that assigns numerical scores to subjects (e.g., "A subject's depression score is the sum of integer responses on the 21 items of the Beck Depression Inventory-II administered at baseline").

Let $\xi$ denote the true, unobserved latent construct, and let $X_1, X_2, \dots, X_p$ represent observable empirical indicators (manifest variables). In psychometrics and structural equation modeling (SEM), the operational relationship between constructs and indicators is categorized into two distinct architectural typologies:
1. Reflective (Effect) Indicator Model: The latent construct $\xi$ is conceived as an existing real entity that causally generates the observed responses on manifest indicators:
$$X_j = \lambda_j \xi + \delta_j, \quad j = 1, \dots, p$$
where $\lambda_j$ is the factor loading and $\delta_j$ is measurement error. For example, clinical depression ($\xi$) causes symptoms such as insomnia ($X_1$), suicidal ideation ($X_2$), and appetite loss ($X_3$). If $\xi$ increases, all indicators are expected to increase simultaneously, exhibiting positive inter-item correlation.
2. Formative (Causal) Indicator Model: The construct $\eta$ is an algebraic composite or index formed as a mathematical function of its constituent components:
$$\eta = \sum_{j=1}^p \gamma_j X_j + \zeta$$
For example, Socio-Economic Status (SES) is formed by combining household income ($X_1$), educational attainment ($X_2$), and occupational prestige ($X_3$). The indicators do not necessarily correlate with each other (e.g., an individual can possess high education but low income), and the construct does not exist independently of its defining components.

Misclassifying a formative construct as reflective—or vice versa—leads to severe structural specification errors, rendering statistical model parameters meaningless.

## 2.3 The Campbell-Stanley Taxonomy of Research Designs: Pre-Experimental, Quasi-Experimental, and True Experimental
In their seminal 1963 monograph *Experimental and Quasi-Experimental Designs for Research*, Donald T. Campbell and Julian C. Stanley established the foundational taxonomy of research design architectures. Using Campbell's symbolic notation—where $R$ represents random assignment, $O_k$ represents an observation or measurement occasion, and $X$ represents the administration of an experimental treatment or intervention—designs are classified into three overarching structural families:

### 1. Pre-Experimental Designs
These primitive architectures lack comparison control groups or pre-intervention baseline measurements. They possess virtually zero scientific validity:
- One-Shot Case Study:
$$X \quad O_1$$
A single group is exposed to an intervention and measured afterward. Without a baseline measurement or an unexposed control group, it is logically impossible to know whether $O_1$ represents a change, let alone whether the change was caused by $X$.
- One-Group Pretest-Posttest Design:
$$O_1 \quad X \quad O_2$$
A single group is measured at baseline ($O_1$), exposed to treatment ($X$), and re-measured ($O_2$). While change $\Delta = O_2 - O_1$ can be quantified, attributing $\Delta$ to $X$ is completely confounded by historical events, natural biological maturation, and statistical regression to the mean.
- Static-Group Comparison:
$$\begin{array}{cc} X & O_1 \\ \hline & O_2 \end{array}$$
An exposed group is compared to an unexposed group post-treatment. Without random assignment or baseline equivalence checks, observed differences $O_1 - O_2$ may reflect pre-existing selection biases rather than the causal efficacy of $X$.

### 2. True Experimental Designs
True experimental designs isolate causal treatment effects through explicit manipulation and algorithmic random assignment ($R$) of experimental units:
- Pretest-Posttest Control Group Design (Randomized Controlled Trial):
$$\begin{array}{cccc} R & O_{11} & X & O_{12} \\ R & O_{21} & & O_{22} \end{array}$$
Randomization ensures that the treatment and control groups are stochastically equivalent in expectation across all observed and unobserved baseline covariates. The causal treatment effect is identified via the difference-in-differences estimator:
$$\hat{\tau} = (O_{12} - O_{11}) - (O_{22} - O_{21})$$
- Posttest-Only Control Group Design:
$$\begin{array}{ccc} R & X & O_1 \\ R & & O_2 \end{array}$$
By virtue of randomization, $\mathbb{E}[O_1 \mid \text{Control}] = \mathbb{E}[O_2]$, eliminating the necessity of pretests when pretesting is intrusive, reactive, or logistically infeasible.
- Solomon Four-Group Design:
$$\begin{array}{cccc} R & O_1 & X & O_2 \\ R & O_3 & & O_4 \\ R & & X & O_5 \\ R & & & O_6 \end{array}$$
The gold standard for controlling and quantifying testing reactivity: it explicitly identifies the main effect of treatment $X$, the main effect of pretesting, and the interaction between pretesting and treatment.

### 3. Quasi-Experimental Designs
When ethical, legal, or logistical constraints prevent random assignment, researchers deploy quasi-experimental designs, which substitute structural statistical adjustments and longitudinal temporal tracking for physical randomization:
- Non-Equivalent Control Group Pretest-Posttest Design:
$$\begin{array}{ccc} O_{11} & X & O_{12} \\ \hline O_{21} & & O_{22} \end{array}$$
- Interrupted Time-Series Design:
$$O_1 \quad O_2 \quad O_3 \quad O_4 \quad X \quad O_5 \quad O_6 \quad O_7 \quad O_8$$
Repeated observations before and after the intervention allow estimation of secular underlying trends, seasonal cycles, and abrupt level/slope changes caused by $X$.

## 2.4 Internal Validity vs. External Validity: The Fundamental Design Tension
In any empirical investigation, research design requires navigating the fundamental trade-off between internal validity and external validity:
- Internal Validity: The degree to which an observed empirical relationship between an independent variable $X$ and a dependent variable $Y$ can be unequivocally interpreted as a true causal relationship, free from confounding, alternative explanations, or methodological artifacts within the specific context of the study.
- External Validity: The degree to which the causal relationship established within the specific study can be generalized across diverse target populations, alternative operationalizations of treatments and outcomes, different geographic and temporal settings, and real-world conditions.

This creates an inherent structural tension in scientific research:
- Maximizing internal validity demands stringent laboratory control: highly homogeneous participant samples, rigidly standardized environmental conditions, artificial scripted treatments, and blind algorithmic randomization. However, this clinical artificiality severely attenuates external validity: findings established in a pristine university laboratory on 19-year-old undergraduate volunteers may fail completely when deployed in complex, heterogeneous real-world settings.
- Maximizing external validity demands naturalistic field experiments, observational registry studies, and pragmatic clinical trials embedded in routine community practice. However, naturalistic environments introduce unmeasured confounders, treatment non-compliance, measurement error, and environmental perturbations, compromising internal validity.

A methodologically rigorous research program does not prioritize one validity type to the absolute exclusion of the other. Rather, it adopts an intentional two-stage strategy: first establishing internal validity and causal mechanisms through tightly controlled efficacy trials, followed by pragmatic effectiveness trials and multi-site replications to establish generalizability.

## 2.5 Classical Threats to Internal Validity
Campbell and Stanley identified eight classical threats to internal validity that can produce spurious apparent treatment effects in non-randomized or inadequately controlled studies:

1. History: Specific historical events, external environmental shocks, or policy shifts occurring between pretest and posttest measurements that influence the outcome independently of the experimental treatment.
2. Maturation: Biological, psychological, or physiological processes operating within individual participants as a natural function of the passage of time (e.g., spontaneous recovery from illness, cognitive development in children, fatigue, aging).
3. Testing Effects: The direct impact of taking an initial measurement on the scores of a subsequent measurement. Participants frequently improve on cognitive or educational tests simply due to familiarity with the test format, reduced test anxiety, or memorization of items, entirely in the absence of any educational intervention.
4. Instrumentation Decay: Unintended changes in the calibration of physical measuring instruments, shifts in survey administration procedures, or cognitive drift among human raters/coders over time.
5. Statistical Regression to the Mean: The mathematical phenomenon whereby units selected for treatment because they scored at an extreme end of a baseline distribution (e.g., selecting the lowest $10\%$ of students on a reading test) naturally score closer to the population mean upon re-testing, purely as a consequence of imperfect measurement reliability.
6. Selection Bias: Systematic, non-random differences in the baseline characteristics, prognoses, or risk factors of participants who end up in the treatment group compared to those in the control group.
7. Differential Attrition (Experimental Mortality): Non-random loss of participants from the study over time. If participants who drop out of the treatment group differ systematically from those who remain (e.g., sicker patients dropping out of an intensive medical therapy due to adverse side effects), the surviving treatment sample becomes biased toward positive outcomes.
8. Selection-Maturation Interaction: A compound threat occurring when the treatment and control groups mature, develop, or change at different intrinsic rates due to baseline selection disparities (e.g., comparing an intervention group of high-socioeconomic schools with a control group of low-socioeconomic schools).

## 2.6 Worked Problem Examples

### Fully worked question 1: Statistical Regression to the Mean in Educational Interventions
A school district evaluates a remedial mathematics tutoring program. From a cohort of $N = 1,000$ students, they select the lowest-scoring $n = 100$ students on a baseline mathematics examination $X$.
The examination scores follow a bivariate normal distribution $(X, Y) \sim \mathcal{N}_2(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ across the entire cohort of $N = 1,000$ students, where:
- Baseline test mean $\mu_X = 60.0$, standard deviation $\sigma_X = 12.0$.
- Post-intervention test mean $\mu_Y = 60.0$, standard deviation $\sigma_Y = 12.0$.
- Test-retest reliability correlation $\rho = \mathrm{Corr}(X, Y) = 0.70$.

The selected $n = 100$ students had an average baseline score of $\bar{x} = 36.0$ (exactly $2.0$ standard deviations below the population mean).
After 8 weeks of tutoring (during which no control group was maintained), the remedial students took the post-test $Y$ and achieved an average score of $\bar{y} = 44.4$.
The school superintendent proudly announces an average educational gain of $\Delta = 44.4 - 36.0 = +8.4$ points, declaring the tutoring program an overwhelming success.
1. Formulate the conditional expectation of $Y$ given $X = x$ under bivariate normality.
2. Calculate the expected post-test score $\mathbb{E}[Y \mid X = 36.0]$ in the absolute absence of any tutoring effect (pure regression to the mean).
3. Determine the true causal treatment effect of the remedial tutoring program.

### Solution, step 1: State the Bivariate Normal Conditional Expectation Formula
For bivariate normally distributed random variables $(X, Y)$ with means $\mu_X, \mu_Y$, standard deviations $\sigma_X, \sigma_Y$, and Pearson correlation $\rho$, the conditional distribution of $Y$ given $X = x$ is strictly normal:
$$Y \mid (X = x) \sim \mathcal{N}\left( \mu_Y + \rho \frac{\sigma_Y}{\sigma_X}(x - \mu_X), \; \sigma_Y^2 (1 - \rho^2) \right)$$
The expected value of the post-test score is:
$$\mathbb{E}[Y \mid X = x] = \mu_Y + \rho \frac{\sigma_Y}{\sigma_X}(x - \mu_X)$$

### Solution, step 2: Calculate Expected Score Under Pure Regression to the Mean
In the absolute absence of any tutoring intervention (the pure null state where the students merely re-take the test after 8 weeks), the parameters are:
- $\mu_X = 60.0, \; \mu_Y = 60.0$
- $\sigma_X = 12.0, \; \sigma_Y = 12.0 \implies \frac{\sigma_Y}{\sigma_X} = 1.0$
- $\rho = 0.70$
- Selected baseline average $x = 36.0$

Evaluate the conditional expectation:
$$\mathbb{E}[Y \mid X = 36.0] = 60.0 + 0.70 \times (1.0) \times (36.0 - 60.0)$$
$$\mathbb{E}[Y \mid X = 36.0] = 60.0 + 0.70 \times (-24.0)$$
$$\mathbb{E}[Y \mid X = 36.0] = 60.0 - 16.8 = \mathbf{43.2 \text{ points}}$$
Purely as a mathematical consequence of imperfect test-retest reliability ($\rho = 0.70 < 1.0$), any student cohort selected with baseline average $36.0$ is expected to score $43.2$ on the post-test without receiving any tutoring whatsoever!
The expected gain due purely to statistical regression to the mean is:
$$\Delta_{\text{RTM}} = 43.2 - 36.0 = \mathbf{+7.2 \text{ points}}$$

### Solution, step 3: Determine the True Causal Treatment Effect
The observed total gain in the remedial cohort was:
$$\Delta_{\text{observed}} = \bar{y} - \bar{x} = 44.4 - 36.0 = +8.4 \text{ points}$$
Decompose the observed change into its constituent components:
$$\Delta_{\text{observed}} = \Delta_{\text{RTM}} + \tau_{\text{causal}}$$
$$\tau_{\text{causal}} = \Delta_{\text{observed}} - \Delta_{\text{RTM}} = 8.4 - 7.2 = \mathbf{+1.2 \text{ points}}$$
Of the celebrated $+8.4$ point improvement, exactly $7.2$ points ($85.7\%$) was pure statistical artifact resulting from selecting extreme performers under an imperfectly reliable test. The true causal efficacy of the tutoring intervention is a meager $+1.2$ points (or $+0.10$ standard deviations), not the $+8.4$ points claimed. Without a randomized or matched control group, the school district conflated mathematical regression to the mean with educational progress.

---

### Fully worked question 2: Threats to Internal Validity in Before-After Quasi-Experiments
A state department of transportation installs automated speed enforcement cameras along a notorious 20-kilometer highway stretch. They observe the number of fatal traffic accidents:
- Baseline Year (Before cameras): $Y_{\text{pre}} = 48$ fatal accidents.
- Post-Installation Year (After cameras): $Y_{\text{post}} = 28$ fatal accidents.
The agency claims the automated camera system caused a $41.7\%$ reduction in fatal accidents.

However, an independent research statistician reviews statewide highway records and discovers:
1. Across the entire rest of the state (where no cameras were installed), fatal accidents declined from $1,200$ to $960$ during the identical time window, primarily due to higher gasoline prices reducing overall vehicle miles traveled.
2. The specific highway stretch had experienced an unprecedented spike in accidents during the baseline year ($48$ accidents vs. a 10-year historical average of $32$ accidents/year), which was the exact political motivation for installing the cameras.

Formally evaluate:
1. The history threat and quantify the expected post-intervention accident count based on the statewide secular trend.
2. The regression to the mean threat based on the historical baseline.
3. Compute the Difference-in-Differences (DiD) estimate of the camera intervention's true causal effect relative to the statewide comparison group.

### Solution, step 1: Quantify the History Threat via Statewide Trend
The secular trend occurring across the unexposed rest of the state reflects macroeconomic and environmental history (gasoline prices, vehicle miles traveled).
The proportionate secular decline in the control environment is:
$$\text{Trend Factor} = \frac{Y_{\text{control, post}}}{Y_{\text{control, pre}}} = \frac{960}{1200} = 0.80 \quad (20.0\% \text{ reduction})$$
In the absence of the speed camera intervention, if the target highway stretch followed the general statewide history trend, its expected accident count would have been:
$$\hat{Y}_{\text{target, counterfactual}} = Y_{\text{target, pre}} \times 0.80 = 48 \times 0.80 = \mathbf{38.4 \text{ accidents}}$$
Therefore, at least $48 - 38.4 = 9.6$ of the observed $20$ accident reduction was caused by external history, not by the speed cameras.

### Solution, step 2: Evaluate the Regression to the Mean Threat
The highway was selected for intervention because of an anomalous baseline spike: $48$ accidents, compared to its historical mean of $32$.
When an extreme outlier year triggers an intervention, subsequent years naturally regress toward the long-term historical mean even without intervention.
Combining the historical mean of $32$ with the $20\%$ statewide secular reduction predicts a post-intervention count of:
$$\hat{Y}_{\text{baseline-adjusted}} = 32 \times 0.80 = 25.6 \text{ accidents}$$
The observed count of $28$ is actually higher than the $25.6$ predicted by historical regression plus macroeconomic trend!

### Solution, step 3: Calculate the Difference-in-Differences (DiD) Estimator
Formulate the standard Difference-in-Differences estimator on the log-scale (or proportionate scale) using the statewide control group:
$$\ln(\text{DiD}) = \left[ \ln(Y_{\text{treat, post}}) - \ln(Y_{\text{treat, pre}}) \right] - \left[ \ln(Y_{\text{ctrl, post}}) - \ln(Y_{\text{ctrl, pre}}) \right]$$
Compute each component:
$$\Delta_{\text{treat}} = \ln(28) - \ln(48) = 3.3322 - 3.8712 = -0.5390$$
$$\Delta_{\text{ctrl}} = \ln(960) - \ln(1200) = 6.8669 - 7.0901 = -0.2231$$
$$\ln(\text{DiD}) = -0.5390 - (-0.2231) = -0.3159$$
Exponentiate to find the causal incidence rate ratio (IRR):
$$\mathrm{IRR}_{\text{DiD}} = \exp(-0.3159) = \mathbf{0.729} \quad (27.1\% \text{ relative reduction})$$
While the raw naive before-after comparison reported a $41.7\%$ reduction, rigorous control for statewide historical trends via Difference-in-Differences reveals that the cameras reduced accidents by approximately $27.1\%$. The remaining $14.6\%$ was an artifact of external historical macroeconomic trends.

---

### Fully worked question 3: Factorial Design Efficiency and Interaction Effects
An agricultural research station investigates the effects of two fertilizer additives on crop yield $Y$ (in metric tons/hectare):
- Factor A (Nitrogen Enhancer): Levels $a_0$ (Standard) and $a_1$ (Enhanced).
- Factor B (Phosphorus Solubilizer): Levels $b_0$ (Standard) and $b_1$ (Enhanced).

An investigator proposes testing Factor A using $n = 40$ plots ($20$ with $a_0$, $20$ with $a_1$, holding Factor B constant at $b_0$). They then propose testing Factor B using a separate study of $n = 40$ plots holding Factor A constant at $a_0$ (Two separate One-Factor-at-a-Time studies, requiring $N = 80$ total plots).
A biometrician recommends a $2 \times 2$ Factorial Design using only $N = 40$ plots total ($10$ plots randomly allocated to each of the four treatment combinations: $(a_0, b_0), (a_0, b_1), (a_1, b_0), (a_1, b_1)$).
1. State the cell means model for a $2 \times 2$ factorial experiment.
2. Demonstrate Fisher's principle of Hidden Replication: prove that the $2 \times 2$ factorial design with $N = 40$ plots achieves the identical statistical precision for testing main effects as the two One-Factor-at-a-Time experiments requiring $N = 80$ plots.
3. Formulate the mathematical definition of a two-factor interaction and explain why the One-Factor-at-a-Time approach is incapable of detecting synergy or antagonism.

### Solution, step 1: Formulate the $2 \times 2$ Factorial Cell Means Model
Let $\mu_{ij}$ denote the population mean yield under treatment combination Factor A at level $i \in \{0, 1\}$ and Factor B at level $j \in \{0, 1\}$.
The four cell means are $\mu_{00}, \mu_{01}, \mu_{10}, \mu_{11}$.
The linear model for individual plot observation $k \in \{1, \dots, n\}$ is:
$$Y_{ijk} = \mu_{ij} + \epsilon_{ijk}, \quad \epsilon_{ijk} \overset{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2)$$
with $n = 10$ plots per cell, and total sample size $N = 4n = 40$.
The main effect of Factor A is the marginal contrast:
$$\theta_A = \frac{\mu_{11} + \mu_{10}}{2} - \frac{\mu_{01} + \mu_{00}}{2} = \bar{\mu}_{1\cdot} - \bar{\mu}_{0\cdot}$$
The main effect of Factor B is:
$$\theta_B = \frac{\mu_{11} + \mu_{01}}{2} - \frac{\mu_{10} + \mu_{00}}{2} = \bar{\mu}_{\cdot 1} - \bar{\mu}_{\cdot 0}$$
The interaction effect $(\text{AB})$ is:
$$\theta_{AB} = (\mu_{11} - \mu_{10}) - (\mu_{01} - \mu_{00}) = \mu_{11} - \mu_{10} - \mu_{01} + \mu_{00}$$

### Solution, step 2: Prove Fisher's Hidden Replication Theorem
In the proposed One-Factor-at-a-Time (OFAT) design for Factor A, $20$ plots receive $(a_1, b_0)$ and $20$ receive $(a_0, b_0)$.
The estimator is $\hat{\theta}_{A, \text{OFAT}} = \bar{Y}_{10} - \bar{Y}_{00}$.
The variance of this estimator is:
$$\mathrm{Var}(\hat{\theta}_{A, \text{OFAT}}) = \frac{\sigma^2}{20} + \frac{\sigma^2}{20} = \frac{2\sigma^2}{20} = \mathbf{\frac{\sigma^2}{10} = 0.10 \sigma^2}$$
In the $2 \times 2$ factorial design with $n = 10$ plots per cell ($N = 40$ plots total):
$$\hat{\theta}_{A, \text{Factorial}} = \frac{\bar{Y}_{11} + \bar{Y}_{10}}{2} - \frac{\bar{Y}_{01} + \bar{Y}_{00}}{2}$$
Since all four cell sample means are statistically independent with variance $\sigma^2 / 10$:
$$\mathrm{Var}(\hat{\theta}_{A, \text{Factorial}}) = \left(\frac{1}{2}\right)^2 \frac{\sigma^2}{10} + \left(\frac{1}{2}\right)^2 \frac{\sigma^2}{10} + \left(\frac{1}{2}\right)^2 \frac{\sigma^2}{10} + \left(\frac{1}{2}\right)^2 \frac{\sigma^2}{10}$$
$$\mathrm{Var}(\hat{\theta}_{A, \text{Factorial}}) = 4 \times \frac{1}{4} \times \frac{\sigma^2}{10} = \mathbf{\frac{\sigma^2}{10} = 0.10 \sigma^2}$$
The variance of the main effect estimator in the factorial design using $N = 40$ plots is *identical* to that of the OFAT design requiring $N = 40$ plots per factor ($N = 80$ plots total).
Every plot in the factorial experiment serves a dual purpose: it contributes to evaluating the main effect of Factor A *and* simultaneously contributes to evaluating Factor B. This is Fisher's principle of Hidden Replication, yielding a $100\%$ gain in statistical efficiency.

### Solution, step 3: Mathematical Formulation of Interaction and OFAT Failure
An interaction occurs when the effect of one factor depends upon the level of another factor:
$$\theta_{AB} = (\mu_{11} - \mu_{10}) - (\mu_{01} - \mu_{00}) \ne 0$$
In the OFAT approach, Factor B was held fixed at $b_0$. Thus, OFAT only estimates the simple effect of A at $b_0$: $\mu_{10} - \mu_{00}$.
If the two additives are synergistic (e.g., Nitrogen only enhances yield when Phosphorus solubilizer is present, such that $\mu_{10} - \mu_{00} \approx 0$ but $\mu_{11} - \mu_{01} = +4.0$), the OFAT experimenter concludes that Nitrogen has zero effect, completely missing the multi-ton yield increase available when both additives are applied together. OFAT designs implicitly assume zero interaction—an assumption that nature routinely violates. Factorial designs are mathematically required to detect and model synergistic and antagonistic biological interactions.

## 2.7 Selection Bias and Attrition: Mathematical Modeling of Selective Drop-Out
Selection bias occurs when the probability of inclusion in a study sample—or the probability of remaining in the study until completion—is statistically dependent on the outcome variable $Y$, conditional on observed covariates.

James Heckman formulated the econometric model of sample selection (the Heckman Two-Step Selection Model), earning the 2000 Nobel Prize in Economic Sciences. Consider a substantive outcome equation of interest:
$$Y_i = \mathbf{x}_i^T \boldsymbol{\beta} + \epsilon_i$$
where $Y_i$ is observed if and only if a latent selection indicator $D_i^* > 0$:
$$D_i^* = \mathbf{z}_i^T \boldsymbol{\gamma} + u_i, \quad D_i = \mathbb{I}(D_i^* > 0)$$
Assume the error terms $(\epsilon_i, u_i)$ follow a bivariate normal distribution:
$$\begin{pmatrix} \epsilon_i \\ u_i \end{pmatrix} \sim \mathcal{N}_2\left( \begin{pmatrix} 0 \\ 0 \end{pmatrix}, \begin{pmatrix} \sigma_\epsilon^2 & \rho \sigma_\epsilon \\ \rho \sigma_\epsilon & 1 \end{pmatrix} \right)$$
If a researcher fits an Ordinary Least Squares (OLS) regression of $Y$ on $\mathbf{X}$ using only the observed complete-case sample ($D_i = 1$), the conditional expectation is:
$$\mathbb{E}[Y_i \mid \mathbf{x}_i, D_i = 1] = \mathbf{x}_i^T \boldsymbol{\beta} + \mathbb{E}[\epsilon_i \mid u_i > -\mathbf{z}_i^T \boldsymbol{\gamma}]$$
Using the properties of the truncated standard normal distribution:
$$\mathbb{E}[\epsilon_i \mid u_i > -\mathbf{z}_i^T \boldsymbol{\gamma}] = \rho \sigma_\epsilon \lambda(\mathbf{z}_i^T \boldsymbol{\gamma})$$
where $\lambda(\cdot)$ is the Inverse Mills Ratio:
$$\lambda(v) = \frac{\phi(v)}{\Phi(v)}$$
Here, $\phi(v)$ is the standard normal density and $\Phi(v)$ is the cumulative distribution function.
Consequently, the complete-case regression equation is:
$$Y_i = \mathbf{x}_i^T \boldsymbol{\beta} + (\rho \sigma_\epsilon) \lambda(\mathbf{z}_i^T \boldsymbol{\gamma}) + \nu_i$$
If $\rho \ne 0$ (the unobserved determinants of study retention are correlated with the outcome error), standard OLS suffers from omitted variable bias: the estimate $\hat{\boldsymbol{\beta}}_{\text{OLS}}$ is asymptotically biased and inconsistent. Heckman's solution estimates $\boldsymbol{\gamma}$ via probit regression in Step 1, computes the estimated inverse Mills ratio $\hat{\lambda}_i = \lambda(\mathbf{z}_i^T \hat{\boldsymbol{\gamma}})$, and includes $\hat{\lambda}_i$ as an auxiliary control variable in Step 2.

## 2.8 Construct Validity and the Nomological Network
Construct validity represents the degree to which an operationalized measurement instrument, scale, or manipulation actually reflects the theoretical construct it purports to measure. In their foundational 1955 paper, Lee Cronbach and Paul Meehl introduced the concept of the Nomological Network.

A nomological network is an interconnected theoretical system specifying:
1. The theoretical relationships between abstract constructs (e.g., "General Cognitive Ability leads to faster learning of statistical algorithms").
2. The operational relationships between constructs and their manifest indicators (e.g., "Performance on Raven's Progressive Matrices reflects General Cognitive Ability").
3. The empirical relationships observed between the manifest indicators themselves.

Establishing construct validity requires demonstrating that an operationalized instrument behaves in exact concordance with theoretical predictions derived from the nomological network:
- Convergent Validity: The instrument correlates strongly with alternative instruments and behavioral indicators measuring the identical or theoretically allied constructs.
- Discriminant Validity: The instrument exhibits low or near-zero correlations with instruments designed to measure distinct, unrelated constructs (e.g., a scale measuring depression must not simply measure generalized neuroticism or physical fatigue).

## 2.9 Statistical Conclusion Validity: Type I/II Error Trade-offs and Violated Assumptions
Statistical conclusion validity concerns whether the conclusions reached about statistical relationships (e.g., presence of correlation, difference in means) are correct and mathematically warranted.

Major threats to statistical conclusion validity include:
1. Low Statistical Power: Deploying sample sizes insufficient to detect substantively meaningful effect sizes, resulting in Type II error inflation ($\beta > 0.20$).
2. Violated Model Assumptions: Fitting parametric models when fundamental distributional prerequisites fail (e.g., assuming independent errors when clustering or spatial autocorrelation exists, assuming homoscedasticity under severe heteroscedasticity).
3. Fishing and Error Rate Inflation: Executing multiple post-hoc statistical comparisons without adjusting nominal $\alpha$ thresholds, inflating the Family-Wise Error Rate.
4. Unreliable Measurement: Using instruments with low reliability ($\rho_{XX'} < 0.70$), which attenuates observed effect sizes toward zero according to Spearman's attenuation theorem:
$$r_{XY, \text{observed}} = r_{T_X T_Y, \text{true}} \sqrt{\rho_{XX'} \rho_{YY'}}$$
masking genuine physical and social phenomena under measurement noise.

## 2.10 Randomized Controlled Trials (RCTs): Randomization Architectures
Randomized Controlled Trials represent the gold standard of causal inference because physical randomization breaks the confounding causal pathways connecting baseline participant characteristics with treatment allocation:
$$P(X_i = 1 \mid \mathbf{Z}_i) = P(X_i = 1) = \pi$$
This ensures that the treatment and control cohorts are asymptotically identical across both observable covariates and unobservable confounders.

### Common Randomization Architectures:
1. Simple (Complete) Randomization: Each participant is assigned to treatment via independent Bernoulli trials with probability $\pi = 0.50$. While theoretically pristine, simple randomization can produce severe sample size imbalances ($n_{\text{treat}} \ne n_{\text{control}}$) in small cohorts ($N < 100$).
2. Permuted Block Randomization: Participants are allocated in predefined blocks of size $B$ (e.g., $B = 4$ or $B = 6$), where each block contains an equal number of treatment and control slots in random permutations (e.g., $T-C-T-C$, $C-T-T-C$). This guarantees exact numerical balance throughout the recruitment lifecycle.
3. Stratified Block Randomization: Participants are categorized into discrete prognostic strata based on critical baseline covariates (e.g., Age $< 50$ vs. $\ge 50$, Cancer Stage I vs. II), and permuted block randomization is executed independently within each stratum. This prevents accidental covariate imbalance across high-stakes prognostic dimensions.
4. Cluster Randomization: Entire intact social or geographical units (e.g., schools, hospitals, villages) are randomized to treatment or control, rather than individual subjects. Cluster designs prevent treatment contamination (spillover), but introduce intra-cluster correlation.

In cluster randomized designs, individual observations within the same cluster are statistically dependent. This dependence is quantified by the Intraclass Correlation Coefficient (ICC, $\rho$):
$$\rho = \frac{\sigma_b^2}{\sigma_b^2 + \sigma_w^2}$$
where $\sigma_b^2$ is between-cluster variance and $\sigma_w^2$ is within-cluster variance. The variance of the estimated treatment effect is inflated by the Design Effect (VIF):
$$\mathrm{Deff} = 1 + (m - 1)\rho$$
where $m$ is the average cluster size. Failing to account for cluster randomization in sample size calculations results in severe statistical underpowering and massively inflated Type I error rates.

## 2.11 Quasi-Experimental Matching and Cohort Designs
When physical randomization is impossible, quasi-experimental matching attempts to construct a synthetic control cohort that emulates the balanced covariate distribution of a randomized trial.

Under the conditional independence assumption (unconfoundedness or selection on observables):
$$(Y(1), Y(0)) \perp\!\!\perp X \mid \mathbf{Z}$$
the causal Average Treatment Effect on the Treated (ATT) is non-parametrically identified. Paul Rosenbaum and Donald Rubin proved in 1983 that conditioning on the one-dimensional Propensity Score:
$$e(\mathbf{Z}) = P(X = 1 \mid \mathbf{Z})$$
is mathematically sufficient to balance all multi-dimensional covariates $\mathbf{Z}$:
$$\mathbf{Z} \perp\!\!\perp X \mid e(\mathbf{Z})$$
Matching algorithms pair each treated unit with one or more control units possessing nearly identical propensity scores (Nearest-Neighbor Matching, Caliper Matching, or Optimal Full Matching). Covariate balance is evaluated using the Standardized Mean Difference (SMD):
$$\mathrm{SMD} = \frac{\bar{Z}_{\text{treat}} - \bar{Z}_{\text{control}}}{\sqrt{\frac{s_{\text{treat}}^2 + s_{\text{control}}^2}{2}}}$$
Covariates achieving $|\mathrm{SMD}| < 0.10$ are considered adequately balanced.

## 2.12 Unit 2 Methodological Synthesis and Review
Scientific research design requires a systematic, proactive architectural strategy:
- Clearly define the operational translation connecting abstract substantive constructs to formal statistical hypotheses.
- Scrutinize all potential threats to internal validity, recognizing that simple before-and-after improvements are routinely confounded by history, maturation, and regression to the mean.
- Exploit factorial designs and the principle of hidden replication to maximize statistical efficiency and estimate interaction effects.
- In observational and quasi-experimental settings, deploy formal econometric and psychometric corrections (Heckman selection models, propensity score matching, Difference-in-Differences) to adjust for non-random selection and attrition.
"""

(DRAFT_DIR / "unit-2.md").write_text(u2_content.strip() + "\n", encoding="utf-8")
print("Unit 2 generated.")
