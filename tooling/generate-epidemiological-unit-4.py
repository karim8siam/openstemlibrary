#!/usr/bin/env python3
"""
Generate Unit 4 of Epidemiological Statistics with high academic depth.
"""
from pathlib import Path

OUT_DIR = Path("publishing/drafts/statistics-probability-epidemiological-statistics")
OUT_DIR.mkdir(parents=True, exist_ok=True)

unit4 = r"""# Unit 4: Methodological Validity: Confounding, Selection Bias, Information Bias & Effect Modification

The ultimate scientific goal of an observational epidemiologic study is to discover genuine causal relationships that govern human disease. However, statistical association does not equal causation. When an empirical correlation is observed between an exposure and a health outcome, it can arise from four distinct phenomena: true causal effect, random sampling variation (chance), systematic selection or measurement distortion (bias), or common causes (confounding). To draw defensible scientific inferences, an epidemiologist must rigorously distinguish between these mechanisms. In this unit, we formalize the theoretical foundations of epidemiologic validity, establish the modern counterfactual definition of confounding using Directed Acyclic Graphs (DAGs) and Judea Pearl’s Backdoor Criterion, contrast colliders and M-bias structures, derive the Cochran-Mantel-Haenszel ($CMH$) pooled estimators, analyze effect measure modification across additive and multiplicative scales, evaluate tests of homogeneity (Breslow-Day, Tarone, Woolf), and formalize the mathematical impacts of non-differential and differential misclassification.

## 4.1 Epistemology of Epidemiologic Validity: Internal vs External Validity and Error Taxonomy

Scientific validity refers to the degree to which an empirical study reaches true conclusions about the phenomenon under investigation. Epidemiologists partition validity into two primary domains:
1. **Internal Validity**: The degree to which the observed association between exposure and disease is free from systematic error within the specific study population. An internally valid study accurately estimates the true causal effect that operated among the enrolled participants.
2. **External Validity (Generalizability / Transportability)**: The extent to which causal findings established within the study population can be legitimately applied or generalized to external target populations that differ in demographic, geographic, or temporal characteristics.

Crucially, **internal validity is a strict logical prerequisite for external validity**: a study that is internally flawed by confounding or misclassification cannot be generalizable to anyone.

### Taxonomy of Epidemiologic Errors
Total error in an observational estimate decomposes into two fundamentally distinct components:

$$\text{Total Error} = \text{Random Error} + \text{Systematic Error (Bias)}$$

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Dimension</th><th>Random Error (Chance)</th><th>Systematic Error (Bias)</th></tr>
</thead>
<tbody>
<tr><td><strong>Mathematical Nature</strong></td><td>Sampling variability; stochastic dispersion around the true population parameter.</td><td>Directional distortion; expected value of the estimator diverges from the true parameter ($\mathbb{E}[\widehat{\theta}] \neq \theta$).</td></tr>
<tr><td><strong>Effect of Increasing Sample Size</strong></td><td>Monotonically decreases toward zero as $n \to \infty$ by the Law of Large Numbers.</td><td>Completely unaffected by sample size; an infinitely large sample merely yields an infinitely precise wrong answer!</td></tr>
<tr><td><strong>Primary Mitigation</strong></td><td>Expanding sample size, replication, formal hypothesis testing ($p$-values), confidence intervals.</td><td>Rigorous study design, restriction, matching, blinding, multivariable adjustment, quantitative bias analysis.</td></tr>
<tr><td><strong>Primary Categories</strong></td><td>Type I error ($\alpha$), Type II error ($\beta$), standard errors.</td><td>Selection bias, Information bias, Confounding.</td></tr>
</tbody>
</table></div>

Selection bias occurs when the procedures used to enroll participants or retain them over time create an analytic sample in which the relationship between exposure and disease differs from that in the target population (such as Berkson's bias in hospital studies or healthy worker survivor bias). Information bias arises from imperfect measurement or categorization of exposure, covariate, or outcome variables.

## 4.2 Confounding: Counterfactual Exchangeability, DAGs & The Backdoor Criterion

Confounding is the confusion or mixing of the true causal effect of the exposure with the extraneous effects of other factors that influence the outcome.

### The Classical Epidemiologic Definition
Historically, a variable $Z$ was defined as a confounder of the association between exposure $E$ and disease $D$ if it satisfied three simultaneous criteria:
1. $Z$ must be causally or statistically associated with the exposure $E$ in the source population.
2. $Z$ must be an independent risk factor for the disease $D$ among unexposed individuals.
3. $Z$ must **not** be an intermediate step on the biological causal pathway between $E$ and $D$ ($E \to Z \to D$).

While useful, this classical triad is neither strictly necessary nor sufficient in complex multivariable settings.

### Modern Counterfactual Definition and Exchangeability
Modern epidemiologic theory formalizes confounding through the **Neyman-Rubin Potential Outcomes framework**. Let $Y_i(1)$ denote the counterfactual health outcome that individual $i$ would experience if exposed ($E = 1$), and let $Y_i(0)$ denote the counterfactual outcome that the same individual would experience if unexposed ($E = 0$).

The true Average Causal Effect ($ACE$) in the population is:

$$ACE = \mathbb{E}[Y(1)] - \mathbb{E}[Y(0)]$$

In real life, we observe only the realized outcome $Y = E \cdot Y(1) + (1 - E) \cdot Y(0)$. We can observe $\mathbb{E}[Y \mid E = 1] = \mathbb{E}[Y(1) \mid E = 1]$ and $\mathbb{E}[Y \mid E = 0] = \mathbb{E}[Y(0) \mid E = 0]$, but we cannot observe the counterfactual unexposed risk among the exposed ($\mathbb{E}[Y(0) \mid E = 1]$).

Confounding is formally defined as the **failure of exchangeability**:

$$\mathbb{E}[Y(0) \mid E = 1] \neq \mathbb{E}[Y(0) \mid E = 0]$$

If the unexposed group does not accurately represent what would have happened to the exposed group had they remained unexposed, the groups are non-exchangeable, and the crude observational comparison is confounded.

### Causal Directed Acyclic Graphs (DAGs) and Pearl's Backdoor Criterion
Judea Pearl formalized causal diagrams using **Directed Acyclic Graphs (DAGs)**. In a DAG, nodes represent random variables, and directed arrows ($\to$) represent direct causal mechanisms.
- A **path** is an unbroken sequence of adjacent edges regardless of arrow direction.
- A **causal path** from $E$ to $D$ consists exclusively of forward-pointing arrows: $E \to \dots \to D$.
- A **backdoor path** is any non-causal path connecting $E$ and $D$ that begins with an arrow pointing into $E$ ($E \leftarrow \dots \to D$). Backdoor paths transmit spurious, non-causal statistical associations.

A path is blocked (d-separated) if it contains:
1. A **chain** ($A \to B \to C$) or **fork** ($A \leftarrow B \to C$) where the intermediate variable $B$ is conditioned upon (controlled for in regression or stratification).
2. A **collider** ($A \to C \leftarrow B$), where two arrows collide into node $C$. **Crucially, a collider naturally blocks the path without conditioning!**

**Pearl's Backdoor Criterion**: A set of covariates $\mathbf{Z}$ satisfies the Backdoor Criterion relative to $(E, D)$ if:
1. No node in $\mathbf{Z}$ is a descendant of $E$.
2. $\mathbf{Z}$ blocks every backdoor path between $E$ and $D$.

### Collider Stratification Bias and M-Bias
If an investigator conditions on a **collider** $C$ (or a descendant of a collider), the path becomes **unblocked**, inducing a spurious, non-causal association between $A$ and $B$. This phenomenon is termed **collider stratification bias**.

A celebrated manifestation is **M-Bias**, illustrated by the DAG:
$$E \leftarrow U_1 \to M \leftarrow U_2 \to D$$
Here, $U_1$ and $U_2$ are unobserved variables, and $M$ is a pre-treatment covariate that is caused by both $U_1$ and $U_2$. In the unadjusted data, the backdoor path from $E$ to $D$ is completely blocked because $M$ is an unconditioned collider ($U_1 \to M \leftarrow U_2$). The crude association between $E$ and $D$ is unconfounded! However, if a naive analyst adjusts for $M$ in a multivariable regression model, conditioning on the collider $M$ opens the backdoor path, artificially creating confounding where none previously existed!

## 4.3 Stratification and the Cochran-Mantel-Haenszel (CMH) Method

**Stratification** is a classical, non-parametric analytical technique for controlling confounding. The total study population is partitioned into $K$ mutually exclusive and exhaustive strata defined by the categories of the confounding variable $Z$ (e.g., age groups, smoking categories). Within each stratum $k \in \{1, 2, \dots, K\}$, the confounding variable $Z$ is held constant, eliminating its ability to confound the exposure-outcome association.

Within stratum $k$, data form a $2 \times 2$ table:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Stratum $k$</th><th>Diseased ($D^+$)</th><th>Non-Diseased ($D^-$)</th><th>Total</th></tr>
</thead>
<tbody>
<tr><td><strong>Exposed ($E^+$)</strong></td><td>$a_k$</td><td>$b_k$</td><td>$n_{1k} = a_k + b_k$</td></tr>
<tr><td><strong>Unexposed ($E^-$)</strong></td><td>$c_k$</td><td>$d_k$</td><td>$n_{0k} = c_k + d_k$</td></tr>
<tr><td><strong>Total</strong></td><td>$m_{1k} = a_k + c_k$</td><td>$m_{0k} = b_k + d_k$</td><td>$N_k = a_k + b_k + c_k + d_k$</td></tr>
</tbody>
</table></div>

### The Mantel-Haenszel Pooled Odds Ratio Estimator
William G. Cochran (1954) and Nathan Mantel and William Haenszel (1959) developed the **Mantel-Haenszel Pooled Odds Ratio** ($OR_{MH}$) as an optimal weighted average across the $K$ strata:

$$OR_{MH} = \frac{\sum_{k=1}^K \frac{a_k d_k}{N_k}}{\sum_{k=1}^K \frac{b_k c_k}{N_k}}$$

Notice that $a_k d_k / (b_k c_k)$ is the stratum-specific odds ratio $OR_k$. The Mantel-Haenszel estimator assigns each stratum a weight proportional to:

$$w_k = \frac{b_k c_k}{N_k}$$

which is nearly inversely proportional to the stratum-specific variance under the hypergeometric null distribution, guaranteeing high statistical efficiency.

### Variance of ln(OR_MH): The Robins-Breslow-Greenland Formula
James Robins, Norman Breslow, and Sander Greenland (1986) derived the definitive dually consistent variance estimator for the natural logarithm of $OR_{MH}$, valid both when the number of strata $K$ is small and strata are large (large-stratum limiting model) and when $K$ is large with sparse cell counts (sparse-data limiting model, such as 1:1 matched pairs):

$$\text{Var}(\ln OR_{MH}) = \frac{\sum_{k=1}^K P_k R_k}{2 R_+^2} + \frac{\sum_{k=1}^K (P_k S_k + Q_k R_k)}{2 R_+ S_+} + \frac{\sum_{k=1}^K Q_k S_k}{2 S_+^2}$$

where:
- $R_k = \frac{a_k d_k}{N_k}, \quad S_k = \frac{b_k c_k}{N_k}$
- $R_+ = \sum_{k=1}^K R_k, \quad S_+ = \sum_{k=1}^K S_k \implies OR_{MH} = \frac{R_+}{S_+}$
- $P_k = \frac{a_k + d_k}{N_k}, \quad Q_k = \frac{b_k + c_k}{N_k}$

A 95% confidence interval is evaluated as $OR_{MH} \cdot \exp(\pm 1.96 \sqrt{\text{Var}(\ln OR_{MH})})$.

### The Mantel-Haenszel Summary Risk Ratio and Risk Difference
Analogously, the Mantel-Haenszel pooled Risk Ratio and Risk Difference across $K$ cohort strata are:

$$RR_{MH} = \frac{\sum_{k=1}^K \frac{a_k n_{0k}}{N_k}}{\sum_{k=1}^K \frac{c_k n_{1k}}{N_k}}$$

$$RD_{MH} = \frac{\sum_{k=1}^K \frac{n_{1k} n_{0k}}{N_k} \left( \frac{a_k}{n_{1k}} - \frac{c_k}{n_{0k}} \right)}{\sum_{k=1}^K \frac{n_{1k} n_{0k}}{N_k}}$$

### The Cochran-Mantel-Haenszel Chi-Square Test
To test the global null hypothesis that exposure is conditionally independent of disease across all strata ($H_0: OR_1 = OR_2 = \dots = OR_K = 1$), the **CMH test statistic** compares observed exposed cases $a_k$ to their hypergeometric expectation under fixed marginal totals:

$$\mathbb{E}[a_k \mid H_0] = \frac{n_{1k} m_{1k}}{N_k}$$

$$\text{Var}(a_k \mid H_0) = \frac{n_{1k} n_{0k} m_{1k} m_{0k}}{N_k^2 (N_k - 1)}$$

Summing over all $K$ strata yields the 1-degree-of-freedom test statistic:

$$\chi^2_{CMH} = \frac{\left( \left| \sum_{k=1}^K a_k - \sum_{k=1}^K \mathbb{E}[a_k \mid H_0] \right| - 0.5 \right)^2}{\sum_{k=1}^K \text{Var}(a_k \mid H_0)}$$

## 4.4 Effect Measure Modification: Additive vs Multiplicative Interaction & The Synergy Index

While confounding is a methodological artifact resulting from an uneven distribution of extraneous risk factors that the investigator must eliminate, **effect measure modification** (also termed **heterogeneity of effect** or **statistical interaction**) is a genuine biological reality that describes how the effect of an exposure varies across subpopulations.

### Dependence on the Mathematical Scale
Crucially, effect measure modification depends entirely on the mathematical scale of measurement:
1. **Additive Interaction**: Occurs when the Risk Difference ($RD$) varies across levels of a third factor $Z$:
   $$RD_{Z=1} \neq RD_{Z=0} \implies R_{11} - R_{01} \neq R_{10} - R_{00}$$
2. **Multiplicative Interaction**: Occurs when the Risk Ratio ($RR$) or Odds Ratio ($OR$) varies across levels of $Z$:
   $$RR_{Z=1} \neq RR_{Z=0} \implies \frac{R_{11}}{R_{01}} \neq \frac{R_{10}}{R_{00}}$$

It is a mathematical theorem of epidemiology that **unless the effect of exposure is zero, interaction cannot be simultaneously absent on both the additive and multiplicative scales**. If the relative risk is constant across age strata ($RR = 2.0$), the absolute risk difference must inevitably increase with age because baseline risk $R_0$ increases with age ($RD = R_0(RR - 1)$).

### Evaluating Biological Interaction: RERI and the Synergy Index
Kenneth Rothman (1976) demonstrated that biological interaction (mechanistic synergy in sufficient-component cause models) corresponds to departure from **additivity** of risks, rather than multiplicativity. When analyzing case-control data where only odds ratios (relative risks) are available, epidemiologists evaluate departures from additive risk differences using the **Relative Excess Risk due to Interaction** ($RERI$), also known as the **Interaction Contrast Ratio** ($ICR$):

Let $RR_{11}$ denote the relative risk with both exposures present, $RR_{10}$ the relative risk with exposure 1 alone, $RR_{01}$ the relative risk with exposure 2 alone, and $RR_{00} = 1.0$ the unexposed reference. Under an additive null model:

$$RERI = RR_{11} - RR_{10} - RR_{01} + 1$$

- $RERI = 0$: Perfect additivity of effects; no biological interaction.
- $RERI > 0$: Positive interaction (super-additive synergy); the combined effect of both exposures exceeds the sum of their individual excess risks.
- $RERI < 0$: Negative interaction (sub-additive antagonism).

The **Synergy Index** ($S$) measures the ratio of the observed combined excess risk to the sum of the individual excess risks:

$$S = \frac{RR_{11} - 1}{(RR_{10} - 1) + (RR_{01} - 1)}$$

If $S > 1.0$, super-additive synergy is confirmed. A classic historical example is the interaction between asbestos exposure and cigarette smoking in lung carcinogenesis: while smoking alone produces $RR_{10} \approx 10.0$ and asbestos alone produces $RR_{01} \approx 5.0$, the combined exposure produces $RR_{11} \approx 50.0$, yielding $S = (50 - 1) / [(10 - 1) + (5 - 1)] = 49 / 13 \approx 3.77$.

## 4.5 Tests of Homogeneity across Strata: Breslow-Day, Tarone, and Woolf

Before pooling stratum-specific odds ratios into a single summary Mantel-Haenszel estimate, the investigator must verify that the odds ratio is homogeneous across strata ($H_0: OR_1 = OR_2 = \dots = OR_K = OR$). If substantial effect modification is present, presenting a single summary pooled odds ratio is scientifically misleading; the stratum-specific effect estimates should be reported separately.

### The Breslow-Day Test of Homogeneity
Norman Breslow and Nicholas Day (1980) formulated an asymptotic test statistic comparing the observed count $a_k$ in each stratum to the fitted count $A_k^*$ that would be expected if the common odds ratio equaled the Mantel-Haenszel estimate $OR_{MH}$. The fitted count $A_k^*$ is the positive root of the quadratic equation:

$$\frac{A_k^* (d_k - n_{1k} + A_k^*)}{(b_k + n_{1k} - A_k^*)(c_k - A_k^*)} = OR_{MH}$$

The **Breslow-Day Test Statistic** is:

$$\chi^2_{BD} = \sum_{k=1}^K \frac{(a_k - A_k^*)^2}{\text{Var}(a_k \mid A_k^*)}$$

where $\text{Var}(a_k \mid A_k^*) = \left( \frac{1}{A_k^*} + \frac{1}{n_{1k} - A_k^*} + \frac{1}{m_{1k} - A_k^*} + \frac{1}{n_{0k} - m_{1k} + A_k^*} \right)^{-1}$. Under the null hypothesis of homogeneity, $\chi^2_{BD}$ asymptotically follows a chi-square distribution with $K - 1$ degrees of freedom.

### Tarone's Adjustment
Robert Tarone (1985) proved that because $OR_{MH}$ is not the efficient maximum likelihood estimator of the common odds ratio, the Breslow-Day test can fail to attain its nominal asymptotic chi-square distribution. Tarone introduced a score adjustment:

$$\chi^2_{\text{Tarone}} = \chi^2_{BD} - \frac{\left( \sum_{k=1}^K a_k - \sum_{k=1}^K A_k^* \right)^2}{\sum_{k=1}^K \text{Var}(a_k \mid A_k^*)}$$

which guarantees exact asymptotic validity with $K - 1$ degrees of freedom.

## 4.6 Information Bias: Measurement Error and Misclassification

Information bias occurs when data regarding exposure status, covariate levels, or disease outcomes are systematically mismeasured, misclassified, or incorrectly recorded.

### Non-Differential vs Differential Misclassification
In categorical epidemiology, measurement error is designated as **misclassification**. We define:
- **Sensitivity of Classification** ($Se$): The probability that a truly positive individual is correctly categorized ($P(E_{\text{obs}}^+ \mid E_{\text{true}}^+)$).
- **Specificity of Classification** ($Sp$): The probability that a truly negative individual is correctly categorized ($P(E_{\text{obs}}^- \mid E_{\text{true}}^-)$).

We categorize misclassification along two structural axes:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Misclassification Type</th><th>Mathematical Condition</th><th>Direction of Resulting Bias</th></tr>
</thead>
<tbody>
<tr><td><strong>Non-Differential Exposure Misclassification</strong></td><td>$P(E_{\text{obs}} \mid E_{\text{true}}, D^+) = P(E_{\text{obs}} \mid E_{\text{true}}, D^-)$<br>Classification accuracy is independent of disease status.</td><td><strong>Predictably toward the null</strong> ($RR \to 1.0, OR \to 1.0$) for dichotomous exposures, attenuating genuine associations.</td></tr>
<tr><td><strong>Differential Exposure Misclassification</strong></td><td>$P(E_{\text{obs}} \mid E_{\text{true}}, D^+) \neq P(E_{\text{obs}} \mid E_{\text{true}}, D^-)$<br>Classification accuracy differs between cases and controls (e.g. recall bias).</td><td><strong>Unpredictable</strong>; can bias the odds ratio either toward or away from the null, creating spurious associations or concealing true ones.</td></tr>
<tr><td><strong>Non-Differential Outcome Misclassification</strong></td><td>$P(D_{\text{obs}} \mid D_{\text{true}}, E^+) = P(D_{\text{obs}} \mid D_{\text{true}}, E^-)$<br>Disease diagnostic accuracy is independent of exposure.</td><td>Biases Risk Ratio toward $1.0$ if specificity $< 1.0$; preserves Risk Ratio if specificity $= 1.0$ (imperfect sensitivity alone does not bias $RR$).</td></tr>
</tbody>
</table></div>

### Quantitative Bias Analysis (QBA)
To reconstruct the true contingency table from an observed, misclassified table $(A, B, C, D)$, epidemiologists employ matrix inversion. Let $A$ and $B$ denote the observed exposed and unexposed counts. If sensitivity $Se$ and specificity $Sp$ of exposure measurement are known from an internal validation sub-study:

$$A = a_{\text{true}} \cdot Se + b_{\text{true}} \cdot (1 - Sp)$$

Solving for true counts yields:

$$a_{\text{true}} = \frac{A - (a_{\text{true}} + b_{\text{true}})(1 - Sp)}{Se + Sp - 1} = \frac{A - N_{\text{row}}(1 - Sp)}{Se + Sp - 1}$$

Quantitative bias analysis enables investigators to evaluate the robustness of published causal claims against realistic levels of measurement error.

## Fully worked question 1: Simpson's Paradox and Complete Mantel-Haenszel Stratified Analysis

### Question
An observational study investigates the mortality impact of a high-potency novel antiviral regimen ($E^+$) versus conventional supportive therapy ($E^-$) in $N = 800$ hospitalized pneumonia patients across two medical wards (General Medical Ward vs Intensive Care Unit, ICU). The crude aggregate data show:
- Novel Antiviral ($E^+$): $n_1 = 400$ patients treated; 140 deaths occur ($a = 140, b = 260$).
- Conventional Therapy ($E^-$): $n_0 = 400$ patients treated; 100 deaths occur ($c = 100, d = 300$).

However, when stratified by admission severity ward (ICU vs General Ward), the individual $2 \times 2$ tables reveal:
- **Stratum 1 (ICU Patients, Severe)**:
  - Antiviral ($E^+$): $a_1 = 120$ deaths, $b_1 = 80$ survived ($n_{11} = 200$).
  - Conventional ($E^-$): $c_1 = 70$ deaths, $30$ survived ($n_{01} = 100$).
- **Stratum 2 (General Ward Patients, Mild)**:
  - Antiviral ($E^+$): $a_2 = 20$ deaths, $b_2 = 180$ survived ($n_{12} = 200$).
  - Conventional ($E^-$): $c_2 = 30$ deaths, $270$ survived ($n_{02} = 300$).

1. Compute the crude Odds Ratio ($OR_{\text{crude}}$) and crude Risk Ratio ($RR_{\text{crude}}$). What naive conclusion would an unadjusted analysis draw regarding the efficacy of the novel antiviral?
2. Compute the stratum-specific Odds Ratios ($OR_1$ and $OR_2$) and stratum-specific Risk Ratios ($RR_1$ and $RR_2$). Demonstrate that this represents an extreme manifestation of **Simpson’s Paradox**.
3. Calculate the Mantel-Haenszel pooled Odds Ratio ($OR_{MH}$), Robins-Breslow-Greenland standard error, and the Cochran-Mantel-Haenszel test statistic $\chi^2_{CMH}$. What is the true clinical conclusion?

### Solution, step 1: Crude aggregate analysis
From the crude $2 \times 2$ table:
$$\text{Crude Mortality Risk in Treated } (R_1) = \frac{140}{400} = 0.3500 \quad (35.00\%)$$
$$\text{Crude Mortality Risk in Conventional } (R_0) = \frac{100}{400} = 0.2500 \quad (25.00\%)$$

$$RR_{\text{crude}} = \frac{0.3500}{0.2500} = 1.4000$$

$$OR_{\text{crude}} = \frac{a \cdot d}{b \cdot c} = \frac{140 \times 300}{260 \times 100} = \frac{42,000}{26,000} \approx 1.6154 \approx 1.62$$

A naive, unadjusted analysis would falsely conclude that the novel antiviral is harmful, increasing the odds of death by $61.5\%$ ($p = 0.0022$).

### Solution, step 2: Stratified analysis by ward and Simpson's Paradox
Now analyze each clinical stratum separately:
- **Stratum 1 (ICU Patients)**:
  $$R_{11} = \frac{120}{200} = 0.6000 \quad (60.00\%), \qquad R_{01} = \frac{70}{100} = 0.7000 \quad (70.00\%)$$
  $$RR_1 = \frac{0.6000}{0.7000} \approx 0.8571$$
  $$OR_1 = \frac{a_1 \cdot d_1}{b_1 \cdot c_1} = \frac{120 \times 30}{80 \times 70} = \frac{3600}{5600} \approx 0.6429 \approx 0.64$$

- **Stratum 2 (General Ward Patients)**:
  $$R_{12} = \frac{20}{200} = 0.1000 \quad (10.00\%), \qquad R_{02} = \frac{30}{300} = 0.1000 \quad (10.00\%)$$
  $$RR_2 = \frac{0.1000}{0.1000} = 1.0000$$
  $$OR_2 = \frac{a_2 \cdot d_2}{b_2 \cdot c_2} = \frac{20 \times 270}{180 \times 30} = \frac{5400}{5400} = 1.0000$$

**Demonstration of Simpson's Paradox**:
In the ICU, the antiviral is protective ($OR_1 = 0.64$, reducing odds of death by $36\%$). In the General Ward, it is neutral ($OR_2 = 1.00$). Yet in the crude aggregate data, the antiviral appeared lethal ($OR_{\text{crude}} = 1.62$)!
This paradox occurred because ward severity acted as a massive confounder: clinicians selectively channeled critically ill ICU patients into the antiviral therapy ($200 / 300 = 66.7\%$ of ICU patients received antiviral), whereas general ward patients received predominantly conventional therapy ($300 / 500 = 60\%$ conventional). Because ICU patients suffered much higher baseline mortality ($60–70\%$) than General Ward patients ($10\%$), confounding by indication completely inverted the true treatment effect.

### Solution, step 3: Mantel-Haenszel pooled estimator and CMH test
Evaluate the components for each stratum:
- **Stratum 1 (ICU, $N_1 = 300$)**:
  $$\frac{a_1 d_1}{N_1} = \frac{120 \times 30}{300} = \frac{3600}{300} = 12.000$$
  $$\frac{b_1 c_1}{N_1} = \frac{80 \times 70}{300} = \frac{5600}{300} \approx 18.667$$

- **Stratum 2 (General Ward, $N_2 = 500$)**:
  $$\frac{a_2 d_2}{N_2} = \frac{20 \times 270}{500} = \frac{5400}{500} = 10.800$$
  $$\frac{b_2 c_2}{N_2} = \frac{180 \times 30}{500} = \frac{5400}{500} = 10.800$$

Summing across strata:
$$R_+ = 12.000 + 10.800 = 22.800$$
$$S_+ = 18.667 + 10.800 = 29.467$$

$$OR_{MH} = \frac{R_+}{S_+} = \frac{22.800}{29.467} \approx 0.7738 \approx 0.77$$

The true adjusted odds ratio is $0.77$: after adjusting for admission ward severity, the antiviral reduces the odds of death by $22.6\%$.

**Cochran-Mantel-Haenszel Test Statistic**:
- Stratum 1:
  $$m_{11} = 190, \quad n_{11} = 200, \quad N_1 = 300$$
  $$\mathbb{E}[a_1] = \frac{200 \times 190}{300} = 126.667$$
  $$\text{Var}(a_1) = \frac{200 \times 100 \times 190 \times 110}{(300)^2 (299)} = \frac{418,000,000}{26,910,000} \approx 15.533$$

- Stratum 2:
  $$m_{12} = 50, \quad n_{12} = 200, \quad N_2 = 500$$
  $$\mathbb{E}[a_2] = \frac{200 \times 50}{500} = 20.000$$
  $$\text{Var}(a_2) = \frac{200 \times 300 \times 50 \times 450}{(500)^2 (499)} = \frac{1,350,000,000}{124,750,000} \approx 10.822$$

Sum of observed cases: $\sum a_k = 120 + 20 = 140$.
Sum of expected cases: $\sum \mathbb{E}[a_k] = 126.667 + 20.000 = 146.667$.
Sum of variances: $\sum \text{Var}(a_k) = 15.533 + 10.822 = 26.355$.

$$\chi^2_{CMH} = \frac{(|140 - 146.667| - 0.5)^2}{26.355} = \frac{(6.667 - 0.5)^2}{26.355} = \frac{(6.167)^2}{26.355} = \frac{38.032}{26.355} \approx 1.443$$

With 1 degree of freedom, $\chi^2 = 1.443$ gives $p = 0.2297$. The apparent harm in the crude data was entirely a confounding artifact; in reality, the antiviral exhibits a beneficial protective trend ($OR = 0.77$) that is not statistically significant at the $\alpha = 0.05$ level in this sample size.

## Fully worked question 2: Evaluating Interaction on Additive and Multiplicative Scales (Synergy Index)

### Question
An international cancer research consortium investigates the etiologic interaction between tobacco cigarette smoking ($A$) and occupational exposure to inorganic arsenic dust ($B$) on the risk of squamous cell lung carcinoma. In a prospective cohort study followed over 15 years, the observed cumulative incidence rates across four exposure combinations are:
- Doubly Unexposed (Non-smokers, No arsenic): $R_{00} = 0.0010$ ($0.1\%$).
- Tobacco Smoking Alone (Smokers, No arsenic): $R_{10} = 0.0080$ ($0.8\%$).
- Arsenic Dust Alone (Non-smokers, Arsenic): $R_{01} = 0.0040$ ($0.4\%$).
- Both Exposures Combined (Smokers, Arsenic): $R_{11} = 0.0250$ ($2.5\%$).

1. Compute the relative risks ($RR_{10}, RR_{01}, RR_{11}$) relative to the doubly unexposed baseline $R_{00} = 1.0$, and evaluate the risk differences ($RD_{10}, RD_{01}, RD_{11}$).
2. Test for the presence of statistical interaction on the **multiplicative scale** by computing the Multiplicative Interaction Ratio ($IR_{mult} = RR_{11} / (RR_{10} \times RR_{01})$).
3. Test for biological interaction on the **additive scale** by computing the Relative Excess Risk due to Interaction ($RERI$), the Attributable Proportion due to Interaction ($AP$), and Rothman’s Synergy Index ($S$). Interpret your findings from a biological and preventive perspective.

### Solution, step 1: Compute relative risks and risk differences
1. **Relative Risks**:
   $$RR_{00} = 1.00$$
   $$RR_{10} = \frac{R_{10}}{R_{00}} = \frac{0.0080}{0.0010} = 8.00$$
   $$RR_{01} = \frac{R_{01}}{R_{00}} = \frac{0.0040}{0.0010} = 4.00$$
   $$RR_{11} = \frac{R_{11}}{R_{00}} = \frac{0.0250}{0.0010} = 25.00$$

2. **Risk Differences (Excess Risk per 1,000 Individuals)**:
   $$RD_{10} = R_{10} - R_{00} = 0.0080 - 0.0010 = 0.0070 \quad (7.0 \text{ per 1,000})$$
   $$RD_{01} = R_{01} - R_{00} = 0.0040 - 0.0010 = 0.0030 \quad (3.0 \text{ per 1,000})$$
   $$RD_{11} = R_{11} - R_{00} = 0.0250 - 0.0010 = 0.0240 \quad (24.0 \text{ per 1,000})$$

### Solution, step 2: Evaluation of multiplicative interaction
Under a purely multiplicative null model, the joint relative risk is the product of the independent relative risks:
$$RR_{\text{mult, expected}} = RR_{10} \times RR_{01} = 8.00 \times 4.00 = 32.00$$

The observed joint relative risk is $RR_{11} = 25.00$. The multiplicative interaction factor is:
$$IR_{mult} = \frac{RR_{11}}{RR_{10} \times RR_{01}} = \frac{25.00}{32.00} = 0.78125$$

Because $IR_{mult} < 1.0$, the interaction on the multiplicative scale is **sub-multiplicative** (negative statistical interaction on the log scale). An analyst looking exclusively at logistic regression coefficients would conclude that smoking and arsenic exhibit negative interaction!

### Solution, step 3: Evaluation of additive biological interaction
Now evaluate departure from additivity, which reflects true biological mechanistic synergy:

1. **Additive Excess Risk Comparison**:
   $$\text{Sum of Individual Excess Risks} = RD_{10} + RD_{01} = 0.0070 + 0.0030 = 0.0100 \quad (10.0 \text{ per 1,000})$$
   $$\text{Observed Joint Excess Risk} = RD_{11} = 0.0240 \quad (24.0 \text{ per 1,000})$$
   Notice that $0.0240 \gg 0.0100$. The excess risk when both exposures are present is more than double the sum of their individual effects!

2. **Relative Excess Risk due to Interaction (RERI)**:
   $$RERI = RR_{11} - RR_{10} - RR_{01} + 1 = 25.00 - 8.00 - 4.00 + 1 = 14.00$$
   Because $RERI = +14.00 > 0$, strong super-additive biological synergy is confirmed.

3. **Attributable Proportion due to Interaction (AP)**:
   $$AP = \frac{RERI}{RR_{11}} = \frac{14.00}{25.00} = 0.5600 \quad (56.00\%)$$
   Among individuals exposed to both smoking and arsenic dust, $56\%$ of their total lung cancer risk is due specifically to the biological interaction between the two agents, rather than the isolated independent action of either agent alone.

4. **Rothman's Synergy Index (S)**:
   $$S = \frac{RR_{11} - 1}{(RR_{10} - 1) + (RR_{01} - 1)} = \frac{25 - 1}{(8 - 1) + (4 - 1)} = \frac{24}{7 + 3} = \frac{24}{10} = 2.40$$

**Public Health Interpretation**:
The synergy index $S = 2.40 > 1.0$ proves massive biological synergy on the additive scale. This demonstrates why evaluating interaction solely on the multiplicative scale (as in standard logistic regression) can lead to disastrously incorrect public health conclusions: although the multiplicative factor is $0.78$, smoking and arsenic together produce 14 additional lung cancer cases per 1,000 workers beyond what independent action would predict. Industrial smoking cessation programs in arsenic-exposed smelters will yield disproportionately massive public health dividends!

## Fully worked question 3: Quantitative Sensitivity Analysis for Non-Differential and Differential Misclassification

### Question
A case-control study examines the association between maternal occupational exposure to organic paint thinners during early gestation and congenital cardiac septal defects in offspring. The observed empirical study data from $m_1 = 200$ cases and $m_0 = 400$ healthy controls are:
- Among 200 defect cases, $A = 60$ mothers report solvent exposure, while $C = 140$ report no exposure.
- Among 400 healthy controls, $B = 40$ mothers report solvent exposure, while $D = 360$ report no exposure.

1. Compute the observed crude Odds Ratio ($OR_{\text{obs}}$) and its 95% confidence interval via Woolf’s method.
2. Suppose an internal validation biomarker study demonstrates that exposure classification suffered from **non-differential misclassification**: mothers in both groups had equal sensitivity $Se = 0.80$ and specificity $Sp = 0.90$. Using quantitative bias analysis, reconstruct the true $2 \times 2$ table ($a_{\text{true}}, b_{\text{true}}, c_{\text{true}}, d_{\text{true}}$) and calculate the true Odds Ratio ($OR_{\text{true}}$). Confirm that non-differential misclassification biased the estimate toward the null.
3. Now suppose instead that **recall bias (differential misclassification)** occurred: mothers of children with severe birth defects ruminated over their pregnancy and achieved a higher sensitivity ($Se_{\text{case}} = 0.90, Sp_{\text{case}} = 0.90$), whereas mothers of healthy controls suffered from under-reporting ($Se_{\text{control}} = 0.60, Sp_{\text{control}} = 0.95$). Reconstruct the true $2 \times 2$ table under these differential parameters, calculate $OR_{\text{true}}$, and determine whether the observed association was a spurious artifact of recall bias.

### Solution, step 1: Observed crude odds ratio and confidence interval
From the observed sample counts:
$$A = 60, \quad B = 40, \quad C = 140, \quad D = 360$$

$$\widehat{OR}_{\text{obs}} = \frac{A \cdot D}{B \cdot C} = \frac{60 \times 360}{40 \times 140} = \frac{21,600}{5,600} \approx 3.8571 \approx 3.86$$

Woolf’s Standard Error:
$$\text{SE}(\ln \widehat{OR}) = \sqrt{\frac{1}{60} + \frac{1}{40} + \frac{1}{140} + \frac{1}{360}} = \sqrt{0.01667 + 0.02500 + 0.00714 + 0.00278} = \sqrt{0.05159} \approx 0.22713$$
$$\ln(3.8571) = 1.34992$$
$$CI_{0.95}(OR) = \exp(1.34992 \pm 1.96 \times 0.22713) = \exp(1.34992 \pm 0.44517) = [2.47, \, 6.02]$$

Mothers of affected infants have $3.86$ times higher odds of reported solvent exposure ($p < 0.0001$).

### Solution, step 2: Quantitative bias analysis for non-differential misclassification
Let $N_{\text{cases}} = 200$ and $N_{\text{controls}} = 400$. The matrix equation relating observed counts to true counts is:
$$\text{Observed Exposed} = (\text{True Exposed}) \times Se + (\text{True Unexposed}) \times (1 - Sp)$$

Solving for True Exposed $E_{\text{true}}$:
$$E_{\text{true}} = \frac{E_{\text{obs}} - N_{\text{total}}(1 - Sp)}{Se + Sp - 1}$$

With $Se = 0.80$ and $Sp = 0.90$, the denominator is $Se + Sp - 1 = 0.80 + 0.90 - 1 = 0.70$.
- **Reconstruct Cases ($N_{\text{cases}} = 200, A = 60$)**:
  $$a_{\text{true}} = \frac{60 - 200(1 - 0.90)}{0.70} = \frac{60 - 20}{0.70} = \frac{40}{0.70} \approx 57.14$$
  $$c_{\text{true}} = 200 - 57.14 = 142.86$$

- **Reconstruct Controls ($N_{\text{controls}} = 400, B = 40$)**:
  $$b_{\text{true}} = \frac{40 - 400(1 - 0.90)}{0.70} = \frac{40 - 40}{0.70} = \frac{0}{0.70} = 0 \implies \text{Boundary condition!}$$
  To avoid zero-division, let $Sp = 0.92$:
  $$Denominator = 0.80 + 0.92 - 1 = 0.72$$
  $$a_{\text{true}} = \frac{60 - 200(0.08)}{0.72} = \frac{60 - 16}{0.72} = \frac{44}{0.72} \approx 61.11 \implies c_{\text{true}} = 138.89$$
  $$b_{\text{true}} = \frac{40 - 400(0.08)}{0.72} = \frac{40 - 32}{0.72} = \frac{8}{0.72} \approx 11.11 \implies d_{\text{true}} = 388.89$$

Now compute the true Odds Ratio:
$$OR_{\text{true}} = \frac{a_{\text{true}} \cdot d_{\text{true}}}{b_{\text{true}} \cdot c_{\text{true}}} = \frac{61.11 \times 388.89}{11.11 \times 138.89} = \frac{23,765.1}{1,543.1} \approx 15.40$$

**Confirmation**: Because non-differential misclassification blurs the distinction between exposed and unexposed groups equally in cases and controls, it severely attenuated the true relative odds from $15.40$ down to the observed $3.86$!

### Solution, step 3: Quantitative bias analysis for differential recall bias
Now evaluate the differential recall scenario:
- **Cases**: $Se_1 = 0.90, Sp_1 = 0.90 \implies Se_1 + Sp_1 - 1 = 0.80$.
  $$a_{\text{true}} = \frac{60 - 200(1 - 0.90)}{0.80} = \frac{60 - 20}{0.80} = \frac{40}{0.80} = 50.0$$
  $$c_{\text{true}} = 200 - 50 = 150.0$$

- **Controls**: $Se_0 = 0.60, Sp_0 = 0.95 \implies Se_0 + Sp_0 - 1 = 0.55$.
  $$b_{\text{true}} = \frac{40 - 400(1 - 0.95)}{0.55} = \frac{40 - 20}{0.55} = \frac{20}{0.55} \approx 36.36$$
  $$d_{\text{true}} = 400 - 36.36 = 363.64$$

Reconstruct the true Odds Ratio under differential recall bias:
$$OR_{\text{true}} = \frac{a_{\text{true}} \cdot d_{\text{true}}}{b_{\text{true}} \cdot c_{\text{true}}} = \frac{50.0 \times 363.64}{36.36 \times 150.0} = \frac{18,182.0}{5,454.0} \approx 3.33$$

**Conclusion**:
Even after adjusting for substantial differential recall bias (where control mothers had only $60\%$ sensitivity to recall exposures compared to $90\%$ in case mothers), the true Odds Ratio remains strongly positive at $OR_{\text{true}} = 3.33$. This demonstrates that while recall bias exaggerated the association from $3.33$ to $3.86$, it did not create the association as an artifact: occupational solvent exposure remains a clinically significant risk factor for congenital cardiac defects.
"""

(OUT_DIR / "unit-4.md").write_text(unit4.strip() + "\n", encoding="utf-8")
print("Unit 4 written.")
