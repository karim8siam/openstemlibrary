from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-statistical-research-methods"

# 1. Expand Unit 5
p5 = DRAFT_DIR / "unit-5.md"
t5 = p5.read_text(encoding="utf-8")

extra_u5 = r"""
## 5.8 Group Sequential Designs and $\alpha$-Spending Functions
In modern clinical trials and large-scale industrial experiments, waiting until the entire target sample size $N$ is recruited before performing any statistical analysis can be unethical or economically inefficient. If an experimental oncology drug produces dramatic survival benefits, continuing to administer placebo to control patients violates the principle of beneficence. Conversely, if a drug causes severe adverse events or exhibits complete futility, terminating the trial early protects participants and conserves capital.

However, performing multiple interim analyses (peeking at the data) without mathematical adjustments causes catastrophic inflation of the overall Family-Wise Error Rate. In 1983, David DeMets and K. K. Gordon Lan established the flexible $\alpha$-Spending Function methodology, liberating sequential testing from rigid, predetermined interim sample sizes.

Let $t \in [0, 1]$ denote the Information Fraction: the proportion of total planned trial information observed at an interim review (typically $t = n_{\text{current}} / N_{\text{planned}}$).
An $\alpha$-spending function $\alpha(t)$ is any monotonically increasing function satisfying:
$$\alpha(0) = 0 \quad \text{and} \quad \alpha(1) = \alpha_{\text{total}}$$
The incremental alpha allocated (spent) between interim look $k - 1$ and look $k$ is:
$$\Delta \alpha_k = \alpha(t_k) - \alpha(t_{k-1})$$
Two canonical spending functions dominate clinical biostatistics:
1. O'Brien-Fleming Type Spending Function:
$$\alpha_{\text{OBF}}(t) = 2 - 2 \Phi\left( \frac{z_{\alpha/2}}{\sqrt{t}} \right)$$
Spends virtually zero alpha early in the trial ($t < 0.50$), demanding extraordinarily conservative critical values for early stopping (e.g., $z > 4.0, p < 0.0001$), thereby preserving nearly the entire nominal $\alpha = 0.05$ for the final primary analysis.
2. Pocock Type Spending Function:
$$\alpha_{\text{Pocock}}(t) = \alpha \ln(1 + (e - 1)t)$$
Spends alpha at a constant, linear rate throughout the trial lifecycle, yielding identical critical thresholds at every interim look (e.g., $z_{\text{crit}} \approx 2.41$ across four looks).

## 5.9 Statistical Power in Hierarchical and Multilevel Designs
In educational, epidemiological, and organizational research, data exhibit intrinsic hierarchical nested clustering: students are nested within classrooms, classrooms within schools, and schools within administrative districts. When treatments are randomized at the cluster level (Cluster-Randomized Trials), sample size determination requires navigating the trade-off between the number of clusters $J$ and the number of individuals per cluster $n$.

The total variance of outcome $Y_{ij}$ decomposes into between-cluster variance $\tau^2$ and within-cluster variance $\sigma^2$:
$$\mathrm{Var}(Y_{ij}) = \tau^2 + \sigma^2$$
The Intraclass Correlation Coefficient (ICC, $\rho$) is:
$$\rho = \frac{\tau^2}{\tau^2 + \sigma^2}$$
For a cluster-randomized trial with $J$ clusters allocated to treatment and $J$ clusters allocated to control ($2J$ total clusters), with $n$ individuals per cluster, the variance of the estimated treatment effect $\hat{\beta}_1$ is:
$$\mathrm{Var}(\hat{\beta}_1) = \frac{4 (\tau^2 + \sigma^2 / n)}{J} = \frac{4 \sigma_{\text{total}}^2 [1 + (n - 1)\rho]}{J n}$$
Notice that as individual cluster size $n \to \infty$:
$$\lim_{n \to \infty} \mathrm{Var}(\hat{\beta}_1) = \frac{4 \tau^2}{J}$$
This fundamental mathematical asymptotic bound establishes that once a cluster reaches a modest size (e.g., $n = 30$ students per classroom), recruiting additional individuals within existing clusters yields diminishing returns. Increasing statistical power requires recruiting more *clusters* ($J$), not more individuals per cluster.

## 5.10 Compromise Power Analysis and Error-Cost Minimax Allocation
The classical Neyman-Pearson convention fixing $\alpha = 0.05$ and targeting $\beta = 0.20$ presumes that Type I errors are four times more severe than Type II errors:
$$q = \frac{\text{Cost}(\text{Type I Error})}{\text{Cost}(\text{Type II Error})} = 4.0$$
In many high-stakes research domains, this $4:1$ asymmetry is irrational or counterproductive:
- In Environmental Toxicology: Failing to detect that an industrial pesticide contaminates municipal groundwater (Type II error) causes catastrophic public health crises, while falsely suspecting a safe chemical (Type I error) merely causes minor regulatory re-testing. Here, $\text{Cost}(\text{Type II}) \gg \text{Cost}(\text{Type I}) \implies q < 0.20$.
- In Preclinical Drug Screening: Discarding a promising cancer compound due to a false negative terminates a potentially lifesaving therapy, whereas a false positive is easily weeded out in subsequent Phase I trials.

Compromise Power Analysis (Erdfelder, 1984) rejects arbitrary fixed thresholds. Given a fixed sample size $N$ dictated by logistical constraints, and an estimated effect size, the researcher specifies the relative cost ratio $q = \beta / \alpha$. The optimal critical threshold $z_{\text{crit}}$ is determined simultaneously by solving:
$$\frac{\beta(z_{\text{crit}})}{\alpha(z_{\text{crit}})} = q$$
This ensures that the decision rule minimizes the total expected loss:
$$\mathbb{E}[\mathcal{L}] = \pi_0 \alpha \mathcal{L}_{\text{Type I}} + (1 - \pi_0) \beta \mathcal{L}_{\text{Type II}}$$
yielding an optimal, rational decision boundary.
"""

t5 = t5.replace("## 5.7 Unit 5 Methodological Synthesis and Review", extra_u5.strip() + "\n\n## 5.7 Unit 5 Methodological Synthesis and Review")
p5.write_text(t5, encoding="utf-8")
print("Unit 5 expanded.")

# 2. Expand Unit 6
p6 = DRAFT_DIR / "unit-6.md"
t6 = p6.read_text(encoding="utf-8")

extra_u6 = r"""
## 6.9 Sensitivity Analysis for Unmeasured Confounding: Rosenbaum's $\Gamma$ and the E-Value
Because observational causal inference relies on the untestable assumption of no unmeasured confounding (unconfoundedness), rigorous research methodology requires quantitative Sensitivity Analysis: assessing how strong an unmeasured confounder would need to be to overturn the study's conclusions.

1. Rosenbaum's Bounding Method ($\Gamma$):
   Paul Rosenbaum (2002) formulated sensitivity bounds for matched observational studies. Let $\Gamma \ge 1$ denote the odds ratio of receiving treatment between two individuals matched on all observed covariates $\mathbf{X}$, caused by an unobserved confounder $U$:
   $$\frac{1}{\Gamma} \le \frac{P(D_i = 1 \mid \mathbf{X}, U_i) / [1 - P(D_i = 1 \mid \mathbf{X}, U_i)]}{P(D_j = 1 \mid \mathbf{X}, U_j) / [1 - P(D_j = 1 \mid \mathbf{X}, U_j)]} \le \Gamma$$
   When $\Gamma = 1.0$, there is zero unmeasured confounding. Rosenbaum bounds compute the threshold $\Gamma^*$ at which the $p$-value for the treatment effect crosses the non-significance boundary $\alpha = 0.05$. If a study achieves $\Gamma^* = 3.5$, an unobserved confounder would need to multiply the odds of treatment by $350\%$ to explain away the observed effect, demonstrating exceptional robustness.
2. The E-Value Metric (Ding & VanderWeele, 2016):
   Tyler VanderWeele and Peng Ding introduced the E-value, defining the minimum strength of association that an unmeasured confounder $U$ must have with *both* the treatment $D$ and the outcome $Y$, conditional on observed covariates, to fully explain away the observed treatment-outcome risk ratio $\mathrm{RR}$:
   $$\mathrm{E\text{-}value} = \mathrm{RR} + \sqrt{\mathrm{RR}(\mathrm{RR} - 1)}$$
   For an observed risk ratio of $\mathrm{RR} = 3.0$:
   $$\mathrm{E\text{-}value} = 3.0 + \sqrt{3.0(2.0)} = 3.0 + \sqrt{6.0} \approx 3.0 + 2.45 = \mathbf{5.45}$$
   To nullify the finding, an unmeasured confounder would have to be associated with both the treatment and the outcome by a risk ratio of at least $5.45$-fold each, beyond all measured controls.

## 6.10 Staggered Difference-in-Differences and the Goodman-Bacon Decomposition
In classical Difference-in-Differences, all treated units receive intervention at the identical calendar time. In real-world policy research, however, interventions adopt a Staggered Rollout architecture: different states, municipalities, or hospitals enact policies at different times.

Historically, researchers estimated staggered DiD using Two-Way Fixed Effects (TWFE) regression:
$$Y_{it} = \alpha_i + \lambda_t + \beta_{\text{TWFE}} D_{it} + \epsilon_{it}$$
In a groundbreaking 2021 econometrics paper, Andrew Goodman-Bacon proved the Goodman-Bacon Decomposition Theorem:
Under staggered timing, the TWFE coefficient $\hat{\beta}_{\text{TWFE}}$ is a weighted average of all possible $2 \times 2$ DiD comparisons across timing cohorts:
$$\hat{\beta}_{\text{TWFE}} = \sum_{k \ne l} w_{k, l} \hat{\beta}_{k, l}^{2 \times 2}$$
Critically, Goodman-Bacon proved that the comparison pairs include:
1. Early-treated units versus never-treated controls (Clean comparison).
2. Late-treated units versus never-treated controls (Clean comparison).
3. Late-treated units versus *already-treated* early units, where the early-treated units serve as the control group ("Forbidden Comparison")!

If the causal treatment effect evolves, grows, or decays over time (dynamic treatment heterogeneity), using already-treated units as controls subtracts the ongoing treatment trajectory of the early cohort, producing negative weights! In fact, $\hat{\beta}_{\text{TWFE}}$ can be negative even when every individual unit experiences a positive causal effect!
Modern causal econometrics resolves this bias using robust staggered estimators: Callaway and Sant'Anna (2021) and Sun and Abraham (2021), which estimate group-time Average Treatment Effects $\mathrm{ATT}(g, t)$ using strictly clean, untreated comparison cohorts.
"""

t6 = t6.replace("## 6.8 Unit 6 Methodological Synthesis and Review", extra_u6.strip() + "\n\n## 6.8 Unit 6 Methodological Synthesis and Review")
p6.write_text(t6, encoding="utf-8")
print("Unit 6 expanded.")

# 3. Expand Unit 7
p7 = DRAFT_DIR / "unit-7.md"
t7 = p7.read_text(encoding="utf-8")

extra_u7 = r"""
## 7.9 Open Science and Registered Reports: Structural Solution to Publication Bias
While post-hoc statistical corrections (such as trim-and-fill and Egger's regression) attempt to diagnose publication bias after the literature has been corrupted, the Open Science movement introduced a structural editorial innovation that eliminates publication bias at its root: Registered Reports.

In traditional academic publishing, a study is reviewed and evaluated by peer reviewers and journal editors *after* the study has been completed and the results are known. This creates an irresistible structural incentive for authors to $p$-hack, selectively report outcomes, and suppress null findings to ensure the manuscript appears "exciting" and publishable.

The Registered Reports format (Chambers, 2013) decouples the publication decision from the study's empirical results through a Two-Stage Peer Review architecture:
1. Stage 1 Review (Before Data Collection):
   Authors submit a detailed protocol containing the scientific rationale, formal conceptual hypotheses, power analysis, sampling design, and exact step-by-step statistical analysis scripts. Peer reviewers evaluate whether the research question is substantive, whether the design is rigorous, and whether statistical power is adequate ($\ge 90\%$).
   - If approved, the journal issues an in-principle acceptance (IPA): a binding contractual guarantee that the journal *will publish the manuscript regardless of the final empirical outcome* (whether the findings are statistically significant, null, or inconclusive).
2. Stage 2 Review (After Data Collection):
   Authors collect data according to the preregistered protocol, execute the scripted analysis, and submit the final manuscript. Reviewers verify only that the authors adhered to the registered protocol; they cannot reject the manuscript based on whether $p < 0.05$.

Empirical evaluations demonstrate that Registered Reports eliminate the file-drawer effect: while traditional psychology literature reports statistically significant positive results in over $90\%$ of papers, Registered Reports publish null findings in approximately $60\%$ of studies, accurately reflecting the stochastic reality of empirical science.

## 7.10 Algorithmic Fairness and Disparate Impact in Predictive Modeling
As statistical machine learning models increasingly automate high-stakes societal decisions—credit lending, criminal bail risk scoring, medical triage, child welfare interventions—ethical statisticians must address Algorithmic Fairness and Disparate Impact.

Let $Y \in \{0, 1\}$ denote the true favorable outcome, $\hat{Y} \in \{0, 1\}$ denote the algorithm's binary prediction, and $A \in \{0, 1\}$ denote a protected demographic attribute (e.g., race or gender).
Computer scientists and statisticians have formalized three competing criteria of algorithmic fairness:
1. Demographic Parity (Statistical Parity):
   The probability of a positive prediction is equal across demographic groups:
   $$P(\hat{Y} = 1 \mid A = 0) = P(\hat{Y} = 1 \mid A = 1)$$
2. Equalized Odds (Predictive Equality):
   True positive rates and false positive rates are equal across groups:
   $$P(\hat{Y} = 1 \mid Y = 1, A = 0) = P(\hat{Y} = 1 \mid Y = 1, A = 1) \quad (\text{Equal Sensitivity})$$
   $$P(\hat{Y} = 1 \mid Y = 0, A = 0) = P(\hat{Y} = 1 \mid Y = 0, A = 1) \quad (\text{Equal False Positive Rate})$$
3. Predictive Value Parity (Calibration within Groups):
   The positive predictive value (probability of true success given a positive prediction) is equal across groups:
   $$P(Y = 1 \mid \hat{Y} = 1, A = 0) = P(Y = 1 \mid \hat{Y} = 1, A = 1)$$

### Chouldechova's Impossibility Theorem of Fairness Metrics (2017)
Alexandra Chouldechova and Jon Kleinberg independently proved a foundational mathematical impossibility theorem:
If baseline base rates differ across groups ($P(Y = 1 \mid A = 0) \ne P(Y = 1 \mid A = 1)$), and the predictive model is imperfect ($\text{AUC} < 1.0$), it is mathematically impossible for an algorithm to satisfy Equalized Odds and Predictive Value Parity simultaneously!
Choosing a fairness metric is not a neutral mathematical calculation; it is an explicit ethical value judgment that requires domain expertise, legal compliance, and stakeholder consultation.
"""

t7 = t7.replace("## 7.8 Unit 7 Methodological Synthesis and Review", extra_u7.strip() + "\n\n## 7.8 Unit 7 Methodological Synthesis and Review")
p7.write_text(t7, encoding="utf-8")
print("Unit 7 expanded.")

# 4. Expand Unit 8
p8 = DRAFT_DIR / "unit-8.md"
t8 = p8.read_text(encoding="utf-8")

extra_u8 = r"""
## 8.9 The "Abandon Statistical Significance" Movement
Following the 2016 ASA Statement, an international coalition of over 800 statisticians and scientists published an influential commentary in *Nature* in 2019 titled *"Scientists Rise Up Against Statistical Significance"* (Amrhein, Greenland, & McShane), calling for the complete retirement of the concept of "statistically significant" dichotomous labeling.

The core argument against dichotomous thresholding is that nature does not operate on a step-function discontinuity at $p = 0.05$:
- A study yielding an estimated odds ratio of $\mathrm{OR} = 1.25$ with $95\%\text{ CI } [1.01, 1.55]$ ($p = 0.041$) is labeled "statistically significant effect confirmed."
- A second study yielding the identical point estimate $\mathrm{OR} = 1.25$ with $95\%\text{ CI } [0.99, 1.58]$ ($p = 0.059$) is labeled "no effect observed; failed to replicate."
To declare that these two nearly identical studies contradict each other is a profound mathematical fallacy. The difference between "statistically significant" and "not statistically significant" is itself not statistically significant (Gelman & Stern, 2006).

Methodologists recommend the ATOM framework:
- Accept uncertainty: Recognize that all statistical estimators possess random variability; never present a confidence interval as an absolute boundary.
- Thoughtful: Evaluate research questions in light of prior biological, physical, or social theory, sample quality, and experimental design, not just automated algorithmic metrics.
- Open: Practice open science by sharing raw data, analytical scripts, computational environments, and preregistrations.
- Modest: Acknowledge the boundaries of external validity; do not generalize findings beyond the sampled population without empirical warrant.

## 8.10 Data Management Plans (DMPs) and FAIR Data Principles
Modern scientific funding bodies (NIH, NSF, European Research Council) mandate that all quantitative research projects incorporate a formal Data Management Plan (DMP) adhering to the international FAIR Data Principles (Wilkinson et al., 2016):

1. Findable:
   Metadata and data are assigned a globally unique, persistent resolvable identifier (such as a Digital Object Identifier, DOI) and indexed in searchable public data repositories (e.g., Zenodo, Harvard Dataverse, Dryad).
2. Accessible:
   Data and metadata can be retrieved via standardized, open communication protocols without proprietary paywalls. Where privacy or ethical considerations restrict open public access (e.g., clinical patient genomes), explicit, transparent data-use agreements and restricted enclave protocols are defined.
3. Interoperable:
   Data are encoded using open, standardized, non-proprietary file formats (e.g., CSV, JSON, NetCDF, Parquet) rather than locked proprietary spreadsheet formats. Variables and measurement units are documented using standardized community ontologies (e.g., SNOMED CT for clinical phenotypes, Dublin Core for general metadata).
4. Reusable:
   Data are accompanied by comprehensive machine-readable and human-readable documentation, detailing data provenance, collection instrumentation, sampling weights, cleaning algorithms, and clear intellectual property licensing (e.g., Creative Commons CC0 or CC-BY) enabling other researchers to build upon the work.
"""

t8 = t8.replace("## 8.8 Unit 8 Methodological Synthesis and Review", extra_u8.strip() + "\n\n## 8.8 Unit 8 Methodological Synthesis and Review")
p8.write_text(t8, encoding="utf-8")
print("Unit 8 expanded.")
