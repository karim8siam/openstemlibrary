from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-statistical-research-methods"

# ==============================================================================
# UNIT 7
# ==============================================================================
u7_content = r"""# Unit 7: Research Ethics, Data Integrity, Confidentiality & Publication Practices

Statistical practice is not conducted in an ethical vacuum. Data represent real human lives, patient clinical outcomes, economic livelihoods, social vulnerabilities, and natural ecosystems. The manipulation of a statistical algorithm, the covert deletion of inconvenient data points, or the selective withholding of non-significant clinical trials can lead to catastrophic real-world harms: dangerous pharmaceutical drugs approved for public consumption, biased criminal justice sentencing algorithms deployed against marginalized communities, or fraudulent scientific theories receiving millions in public funding. As the American Statistical Association (ASA) emphasizes in its Ethical Guidelines: *"The professional statistician has an ethical responsibility to maintain scientific integrity, uphold human rights, and ensure transparent, reproducible, and unbiased methodology."*

This unit examines the ethical codes governing statistical science, traces the history of human subjects protections from the Nuremberg Code to the Belmont Report, details protocols for informed consent and data privacy, formalizes mathematical disclosure control including Differential Privacy, analyzes Questionable Research Practices (QRPs) such as $p$-hacking and HARKing, and dissects the mathematical methodologies used to detect and adjust for publication bias in meta-analyses.

## 7.1 Ethical Codes and Standards in Statistical Practice
Professional statistical societies have established formal ethical standards to govern the conduct of quantitative research:

1. The American Statistical Association (ASA) Ethical Guidelines for Statistical Practice:
   Organized around eight core ethical pillars:
   - Professional Integrity and Accountability: Statisticians must report all methodological choices, potential conflicts of interest, and data limitations without distortion.
   - Integrity of Data and Methods: Data collection procedures must be documented; researchers must not cherry-pick models, selectively trim outliers, or manipulate algorithms to produce desired conclusions.
   - Responsibilities to Science, the Public, and Funders: Findings must be communicated clearly, distinguishing between exploratory analyses and confirmatory tests.
   - Responsibilities to Research Subjects: Participant confidentiality, informed consent, and data protection must be preserved throughout the research lifecycle.
2. The International Statistical Institute (ISI) Declaration on Professional Ethics:
   Emphasizes the societal obligations of statisticians: pursuing objective truth, resisting political or commercial pressure to alter findings, safeguarding vulnerable populations, and maintaining public trust in official national statistics.

A central principle across all ethical declarations is that a statistician must never accept a professional engagement where the compensation or continuation of employment is contingent upon obtaining a pre-specified statistical result (e.g., guaranteeing $p < 0.05$).

## 7.2 Human Subjects Protections: From Nuremberg to the Belmont Report
The contemporary architecture of human research ethics emerged in response to horrific historical abuses:
1. The Nuremberg Code (1947): Drafted following the Nuremberg Military Tribunals prosecuting Nazi physicians for lethal experiments on concentration camp prisoners. Established that voluntary, informed human consent is absolutely essential, experiments must yield fruitful societal benefits unprocurable by other means, and unnecessary physical or mental suffering must be avoided.
2. The Declaration of Helsinki (1964, World Medical Association): Established international ethical principles for biomedical research involving human subjects, mandating protocol review by independent ethics committees and declaring that the health of the individual participant must always take precedence over the interests of science and society.
3. The Tuskegee Syphilis Study (1932–1972): An infamous, unethical observational study conducted by the U.S. Public Health Service on 600 impoverished African American sharecroppers in Alabama. Researchers deceived participants into believing they were receiving medical care, deliberately withholding penicillin treatment for decades after it was proven curative in the 1940s, so researchers could study the fatal progression of untreated syphilis.

The public exposure of Tuskegee led the United States Congress to pass the National Research Act of 1974, establishing the National Commission for the Protection of Human Subjects of Biomedical and Behavioral Research. In 1979, the commission issued the foundational Belmont Report, establishing three overarching ethical principles:
1. Respect for Persons:
   Individuals must be treated as autonomous agents capable of making their own decisions. Persons with diminished autonomy (e.g., children, prisoners, cognitively impaired individuals, impoverished refugees) are entitled to enhanced structural protections. Operationalized through Informed Consent.
2. Beneficence:
   Researchers have an active obligation to "do no harm" and maximize potential societal benefits while minimizing physical, psychological, and informational risks. Operationalized through Risk-Benefit Assessments.
3. Justice:
   Fairness in the distribution of research burdens and benefits. Vulnerable populations must not be exploited as research subjects simply for logistical convenience, nor should the benefits of scientific discoveries be denied to marginalized groups. Operationalized through Equitable Subject Selection.

### Institutional Review Boards (IRBs)
Research involving human subjects must be reviewed and approved by an independent Institutional Review Board (IRB) or Research Ethics Committee (REC) prior to data collection. IRBs classify proposed studies into three review categories based on risk:
- Exempt Review: Minimal risk research involving anonymous surveys, non-invasive educational testing, or analysis of publicly available de-identified records.
- Expedited Review: Minimal risk research involving non-invasive physiological monitoring (e.g., blood draws, fMRI, cognitive tests) where participant identities are confidential.
- Full Board Review: Greater than minimal risk research, studies involving vulnerable populations (e.g., clinical drug trials, invasive surgical interventions, psychological trauma elicitation).

## 7.3 Data Privacy, Confidentiality, and Statistical Disclosure Control
In modern empirical research, collecting massive personal datasets—electronic health records, genomic sequences, mobile GPS telemetry, financial transactions—creates unprecedented privacy risks. Simply stripping obvious direct identifiers (names, Social Security numbers) is completely insufficient to protect privacy.

In 1997, computer scientist Latanya Sweeney demonstrated the fragility of naive de-identification: by cross-referencing an "anonymized" public health dataset with a publicly available voter registration list using merely three non-sensitive quasi-identifiers—ZIP code, birthdate, and gender—she successfully re-identified the personal medical records of the Governor of Massachusetts. Sweeney proved that $87\%$ of the entire United States population can be uniquely re-identified by the combination of 5-digit ZIP code, gender, and date of birth alone.

### Formal Disclosure Control Models:
1. $k$-Anonymity (Sweeney, 2002):
   A dataset satisfies $k$-anonymity if every individual's quasi-identifiers (e.g., ZIP code, age, sex) are identical to at least $k - 1$ other individuals in the dataset. Every demographic combination forms an equivalence class of size at least $k$. Achieved through generalization (e.g., replacing exact age with 10-year age bins) and suppression.
2. $l$-Diversity (Machanavajjhala et al., 2007):
   $k$-Anonymity fails if all $k$ individuals in an equivalence class share the identical sensitive medical attribute (Homogeneity Attack). A dataset satisfies $l$-diversity if every equivalence class contains at least $l$ "well-represented" distinct values for each sensitive attribute.
3. $\epsilon$-Differential Privacy (Dwork, 2006):
   The mathematical gold standard of cryptographically guaranteed privacy. A randomized algorithm $\mathcal{M}$ satisfies $\epsilon$-Differential Privacy if for any two neighboring datasets $D_1$ and $D_2$ differing by only a single individual's record, and for any set of query outputs $\mathcal{S}$:
   $$P(\mathcal{M}(D_1) \in \mathcal{S}) \le e^\epsilon P(\mathcal{M}(D_2) \in \mathcal{S})$$
   Differential privacy guarantees that an adversary observing the statistical output cannot determine whether any specific individual participated in the dataset, regardless of what auxiliary background information the adversary possesses. The privacy parameter $\epsilon$ (privacy budget) governs the mathematical trade-off between privacy preservation and statistical accuracy.

The Laplace Mechanism achieves $\epsilon$-differential privacy for a numerical query function $f(D)$ by adding zero-mean noise drawn from a Laplace distribution:
$$\mathcal{M}(D) = f(D) + W, \quad W \sim \mathrm{Laplace}\left( 0, \frac{\Delta f}{\epsilon} \right)$$
where $\Delta f = \max_{D_1, D_2} \|f(D_1) - f(D_2)\|_1$ is the Global Sensitivity of the query function.

## 7.4 Questionable Research Practices (QRPs): $p$-Hacking and HARKing
Questionable Research Practices (QRPs) are research behaviors that fall between honest human error and blatant scientific fraud (such as outright data fabrication). While often rationalized by investigators as "data exploration," QRPs corrupt the statistical validity of hypothesis tests:

1. $p$-Hacking (Data Snooping / Researcher Degrees of Freedom):
   Iteratively manipulating data preprocessing steps, outlier exclusion rules, variable transformations, and covariate adjustments until the $p$-value falls just below the nominal threshold $p < 0.05$. Joseph Simmons, Leif Nelson, and Uri Simonsohn (2011) demonstrated in *"False-Positive Psychology"* that exploiting common researcher degrees of freedom inflates the true Type I error rate from nominal $\alpha = 0.05$ to over $60.0\%$.
2. Selective Outcome Reporting:
   Measuring multiple outcome variables in a study, but selectively reporting only the few that achieve statistical significance while concealing the non-significant outcomes.
3. Optional Stopping (Data Peeking):
   Repeatedly inspecting sample data as participants are recruited, performing a hypothesis test at each step, and stopping data collection the moment $p < 0.05$, while continuing collection if $p > 0.05$. Under optional stopping, the true false positive rate approaches $100\%$ as the number of peeks increases.
4. HARKing (Hypothesizing After Results are Known):
   Formulated by Norbert Kerr (1998): presenting an exploratory post-hoc finding discovered through data mining as if it were an antecedent theoretical hypothesis derived before data collection. HARKing deceptively presents inductive exploratory pattern discovery as confirmatory deductive testing, violating the mathematical axioms of frequentist testing.

The primary antidote to QRPs is Study Preregistration: registering the complete study design, explicit hypotheses, sample size calculations, exclusion criteria, and exact statistical analysis plans on a public, immutable, timestamped registry (such as the Open Science Framework or ClinicalTrials.gov) prior to observing any data.

## 7.5 Publication Bias and the File-Drawer Problem
A systemic structural failure of academic publishing is Publication Bias: the editorial reality that academic journals are substantially more likely to publish studies reporting statistically significant positive findings ($p < 0.05$) than studies reporting null, non-significant, or inconclusive findings ($p > 0.05$).

In 1979, psychologist Robert Rosenthal coined the term the "File-Drawer Problem":
If 100 independent laboratories test an ineffective drug (where $H_0$ is true), approximately 5 laboratories will, by pure random sampling error ($\alpha = 0.05$), obtain a spurious statistically significant result ($p < 0.05$). The 95 laboratories obtaining null results tuck their papers into filing cabinets, deeming them unpublishable. The 5 false-positive studies are published in prestigious medical journals. An external reader reviewing the published literature concludes that the drug is unequivocally efficacious, completely unaware of the 95 buried null studies.

Publication bias distorts systematic literature reviews, inflates effect size estimates in meta-analyses, and corrupts evidence-based clinical medicine.

## 7.6 Methods for Detecting and Adjusting for Publication Bias
Meta-analysts deploy mathematical and graphical diagnostics to detect and correct for publication bias:

1. Inverted Funnel Plots:
   A scatter plot of estimated study effect sizes ($\hat{\theta}_i$, horizontal axis) plotted against a measure of study precision (sample size $N$ or inverse standard error $1/\mathrm{SE}_i$, vertical axis).
   - In the absence of publication bias: Precision is high at the top, yielding narrow scatter around the true effect; precision is low at the bottom, yielding broad scatter. The plot resembles an inverted, symmetrical funnel.
   - In the presence of publication bias: The bottom corner corresponding to small sample studies with non-significant or negative effects is conspicuously empty, creating visual asymmetry.
2. Egger's Linear Regression Test:
   Matthias Egger (1997) formalized funnel asymmetry into an analytical linear regression of the standardized effect estimate ($Z_i = \hat{\theta}_i / \mathrm{SE}_i$) on precision ($1/\mathrm{SE}_i$):
   $$\frac{\hat{\theta}_i}{\mathrm{SE}_i} = \beta_0 + \beta_1 \left( \frac{1}{\mathrm{SE}_i} \right) + \epsilon_i$$
   Under the null hypothesis of symmetry (no publication bias), the regression line passes through the origin ($\beta_0 = 0$). A statistically significant intercept ($\beta_0 \ne 0, p < 0.05$) provides objective quantitative evidence of funnel plot asymmetry and small-study bias.
3. Begg-Mazumdar Rank Correlation Test:
   Computes Kendall's rank correlation $\tau$ between standardized effect sizes and their variances.
4. Duval and Tweedie's Trim-and-Fill Method (2000):
   A non-parametric, iterative algorithm that:
   - Step 1 (Trim): Identifies and temporarily removes the extreme asymmetric small studies responsible for funnel plot skewness until the funnel becomes symmetrical.
   - Step 2 (Center): Re-estimates the true symmetrical pooled effect size using the remaining trimmed studies.
   - Step 3 (Fill): Imputes (mirrors) the missing counterfactual studies across the center line to create an artificially balanced funnel plot.
   - Step 4: Re-computes the final pooled meta-analytic effect size including the imputed studies, yielding a bias-adjusted effect estimate.

## 7.7 Worked Problem Examples

### Fully worked question 1: Rosenthal's Fail-Safe $N$ Calculation
A clinical meta-analysis pools $k = 15$ published clinical trials evaluating an herbal cognitive supplement.
The combined meta-analytic test of significance across the $k = 15$ studies yields an overall $z$-score sum of:
$$\sum_{i=1}^{15} z_i = 36.40$$
The overall combined Stouffer's $z$-statistic is:
$$Z_{\text{combined}} = \frac{\sum z_i}{\sqrt{k}} = \frac{36.40}{\sqrt{15}} = \frac{36.40}{3.873} \approx 9.398 \quad (p < 10^{-20})$$
The supplement manufacturers claim the evidence is overwhelmingly conclusive.
An independent methodologist suspects publication bias (file-drawer suppression of negative trials).
1. State the mathematical formula for Robert Rosenthal's Fail-Safe $N$ ($N_{\text{fs}}$) based on the Stouffer $z$-method.
2. Compute the exact Fail-Safe $N_{\text{fs}}$: the minimum number of unpublished null studies ($z = 0$) that would need to exist in file drawers to reduce the overall combined significance to the nominal boundary $\alpha = 0.05$ ($z_{\text{crit}} = 1.645$).
3. Evaluate Rosenthal's empirical tolerance criterion ($5k + 10$) and determine whether the meta-analytic finding is robust against publication bias.

### Solution, step 1: State Rosenthal's Fail-Safe $N$ Formula
In 1979, Robert Rosenthal formulated the Fail-Safe $N$ using the Stouffer combined $z$-score method.
Suppose there are $k$ published studies with sum of $z$-scores $\sum_{i=1}^k z_i$.
Suppose there exist $N_{\text{fs}}$ unpublished, file-drawered studies whose average $z$-score is zero ($\bar{z}_{\text{null}} = 0$).
If all $k + N_{\text{fs}}$ studies were combined, the new overall $z$-statistic would be:
$$Z_{\text{new}} = \frac{\sum_{i=1}^k z_i + \sum_{j=1}^{N_{\text{fs}}} 0}{\sqrt{k + N_{\text{fs}}}} = \frac{\sum_{i=1}^k z_i}{\sqrt{k + N_{\text{fs}}}}$$
To find the number of null studies required to reduce the combined significance to nominal level $\alpha = 0.05$ (one-tailed critical value $z_\alpha = 1.645$, where $z_\alpha^2 = (1.645)^2 = 2.706$):
$$\frac{\sum z_i}{\sqrt{k + N_{\text{fs}}}} = z_\alpha$$
Square both sides:
$$\frac{\left( \sum z_i \right)^2}{k + N_{\text{fs}}} = z_\alpha^2$$
$$k + N_{\text{fs}} = \frac{\left( \sum z_i \right)^2}{z_\alpha^2}$$
Solve for $N_{\text{fs}}$:
$$N_{\text{fs}} = \frac{\left( \sum z_i \right)^2}{z_\alpha^2} - k = \frac{\left( \sum z_i \right)^2}{2.706} - k$$

### Solution, step 2: Compute Rosenthal's Fail-Safe $N$
Substitute $\sum z_i = 36.40$, $z_\alpha = 1.645$ ($z_\alpha^2 = 2.706$), and $k = 15$:
$$\left( \sum z_i \right)^2 = (36.40)^2 = 1324.96$$
$$\frac{1324.96}{2.706} \approx 489.638$$
$$N_{\text{fs}} = 489.638 - 15 = \mathbf{474.64} \implies \mathbf{475 \text{ unpublished null studies}}$$
It would require at least $475$ completely unpublished, hidden studies with zero effect to overturn the statistical significance of the $15$ published trials.

### Solution, step 3: Evaluate Against Rosenthal's Tolerance Benchmark
Rosenthal proposed a rule of thumb for evaluating whether a finding is robust against the file-drawer effect:
A meta-analytic result is considered robust against publication bias if the fail-safe $N$ exceeds the threshold:
$$N_{\text{tolerance}} = 5k + 10$$
Evaluate the benchmark for $k = 15$ published studies:
$$N_{\text{tolerance}} = 5(15) + 10 = 75 + 10 = \mathbf{85 \text{ studies}}$$
Compare $N_{\text{fs}}$ to $N_{\text{tolerance}}$:
$$N_{\text{fs}} = 475 \gg 85$$
Because $N_{\text{fs}} = 475$ is more than five times higher than the tolerance threshold of $85$, it is implausible that nearly $500$ hidden negative studies exist in filing cabinets for only $15$ published ones. The meta-analytic finding is declared highly robust against file-drawer publication bias.

---

### Fully worked question 2: Egger's Linear Regression Test for Funnel Plot Asymmetry
A meta-analysis evaluates the risk of cardiovascular events across $k = 10$ randomized trials.
The meta-analyst runs Egger's linear regression test to detect publication bias:
$$Z_i = \beta_0 + \beta_1 \left( \frac{1}{\mathrm{SE}_i} \right) + \epsilon_i$$
where $Z_i = \hat{\theta}_i / \mathrm{SE}_i$ is the standardized effect size, and $1/\mathrm{SE}_i$ is precision.
The Ordinary Least Squares (OLS) regression yields:
- Intercept estimate: $\hat{\beta}_0 = 2.150$.
- Intercept standard error: $\mathrm{SE}(\hat{\beta}_0) = 0.620$.
- Slope estimate: $\hat{\beta}_1 = 0.380$.
- Number of studies: $k = 10$ (degrees of freedom $\nu = k - 2 = 8$).

1. Explain the theoretical rationale of Egger's test and interpret the meaning of intercept $\beta_0$.
2. Formulate the null and alternative hypotheses for Egger's test, compute the test statistic $t$, and evaluate significance at $\alpha = 0.05$ (two-tailed critical value $t_{8, 0.975} = 2.306$).
3. State the substantive epidemiological conclusion regarding publication bias in this meta-analysis.

### Solution, step 1: Explain the Theoretical Rationale of Egger's Regression
In a meta-analysis free from publication bias, studies with small sample sizes (low precision, small $1/\mathrm{SE}_i$) scatter symmetrically around the true pooled effect $\theta$, while large studies (high precision) concentrate tightly around $\theta$.
Multiplying the basic effect equation $\hat{\theta}_i = \theta + \epsilon_i$ by precision $1/\mathrm{SE}_i$ yields:
$$Z_i = \frac{\hat{\theta}_i}{\mathrm{SE}_i} = \theta \left( \frac{1}{\mathrm{SE}_i} \right) + \frac{\epsilon_i}{\mathrm{SE}_i} = 0 + \beta_1 \left( \frac{1}{\mathrm{SE}_i} \right) + \nu_i$$
In the absence of bias, the regression line MUST pass through the origin ($\beta_0 = 0$). The slope $\beta_1$ represents the true underlying effect size.
If small studies are selectively published only when they obtain large, positive effect sizes, the small-study effect pulls the regression line upward as precision $1/\mathrm{SE} \to 0$. The intercept $\beta_0$ directly measures the magnitude and direction of funnel plot asymmetry and publication bias.

### Solution, step 2: Execute the Hypothesis Test
The formal statistical hypotheses are:
$$H_0: \beta_0 = 0 \quad (\text{Funnel plot is symmetrical; zero publication bias})$$
$$H_1: \beta_0 \ne 0 \quad (\text{Funnel plot is asymmetric; publication bias present})$$
Compute the $t$-statistic for the intercept:
$$t = \frac{\hat{\beta}_0 - 0}{\mathrm{SE}(\hat{\beta}_0)} = \frac{2.150}{0.620} \approx \mathbf{3.468}$$
Degrees of freedom is $\nu = k - 2 = 10 - 2 = 8$.
Compare the calculated test statistic with the critical value:
$$t_{\text{calculated}} = 3.468 > t_{8, 0.975} = 2.306$$
The two-tailed $p$-value is $P(|t_8| \ge 3.468) \approx 0.0084$ ($p < 0.01$).
We strictly reject the null hypothesis of symmetry at the $\alpha = 0.05$ level.

### Solution, step 3: State the Substantive Conclusion
The intercept is positive and statistically significant ($\hat{\beta}_0 = 2.15, p = 0.0084$). This provides strong empirical evidence of funnel plot asymmetry: small studies in this literature report disproportionately large, favorable treatment effects compared to larger, higher-powered studies.
The meta-analyst concludes that substantial publication bias (small-study bias) is distorting the published record. The naive pooled effect size is artificially inflated. The researcher must apply Duval and Tweedie's trim-and-fill method or selection models to adjust for the missing null studies before reporting treatment efficacy.

---

### Fully worked question 3: Differential Privacy Laplace Mechanism
A national health ministry publishes an aggregated public database containing records from $n = 100,000$ diabetic patients.
A researcher queries the exact count of patients diagnosed with Stage 4 Diabetic Nephropathy: $f(D) = 1,420$ patients.
To guarantee mathematical privacy for individual patients, the ministry requires all statistical queries to satisfy $\epsilon$-Differential Privacy with privacy budget $\epsilon = 0.50$ via the Laplace Mechanism.
1. Determine the Global Sensitivity $\Delta f$ of a counting query.
2. Formulate the probability density function of the Laplace noise distribution $\mathrm{Lap}(\Delta f / \epsilon)$ and calculate its variance $\sigma^2$.
3. Compute the $95\%$ privacy confidence interval around the perturbed query output, quantifying the privacy-accuracy trade-off.

### Solution, step 1: Determine the Global Sensitivity ($\Delta f$)
The Global $L_1$-Sensitivity of a query function $f: \mathcal{D} \to \mathbb{R}$ across all pairs of neighboring datasets $D_1, D_2$ differing by at most one individual record ($|D_1 \oplus D_2| = 1$) is:
$$\Delta f = \max_{D_1, D_2} \|f(D_1) - f(D_2)\|_1$$
For any counting query ("How many patients satisfy criterion $C$?"), the addition or removal of a single individual can change the count by at most $1$:
$$\Delta f = \mathbf{1.0}$$

### Solution, step 2: State the Laplace Mechanism and Noise Variance
The Laplace Mechanism releases the perturbed query:
$$\mathcal{M}(D) = f(D) + W, \quad W \sim \mathrm{Laplace}(0, b)$$
where the scale parameter $b$ is:
$$b = \frac{\Delta f}{\epsilon} = \frac{1.0}{0.50} = \mathbf{2.0}$$
The probability density function of the zero-mean Laplace noise is:
$$f_W(w) = \frac{1}{2b} \exp\left( -\frac{|w|}{b} \right) = \frac{1}{4} \exp\left( -\frac{|w|}{2.0} \right)$$
The variance of a Laplace distribution with scale $b$ is:
$$\mathrm{Var}(W) = 2b^2 = 2 \times (2.0)^2 = 2 \times 4.0 = \mathbf{8.0}$$
The standard deviation of the injected privacy noise is:
$$\mathrm{SD}(W) = \sqrt{8.0} = 2\sqrt{2} \approx \mathbf{2.828}$$

### Solution, step 3: Compute the $95\%$ Privacy Error Bound and Output Interval
The cumulative distribution function of the Laplace distribution is $F(w) = 1 - \frac{1}{2} e^{-w/b}$ for $w \ge 0$.
To find the two-tailed $95\%$ critical quantile $w_{0.975}$ where $P(|W| \le w_{0.975}) = 0.95$:
$$1 - \exp(-w_{0.975} / b) = 0.95 \implies \exp(-w_{0.975} / b) = 0.05$$
$$-\frac{w_{0.975}}{b} = \ln(0.05) \approx -2.9957$$
$$w_{0.975} = b \ln(20) = 2.0 \times 2.99573 \approx \mathbf{5.991}$$
With $95\%$ probability, the random privacy noise added to the count will not exceed $\pm 5.99$ individuals:
$$P(|\mathcal{M}(D) - 1420| \le 5.99) = 0.95$$
The release output is guaranteed to fall in the range:
$$\text{Output Interval} = 1420 \pm 5.99 \implies [\mathbf{1414}, \; \mathbf{1426}]$$
In a dataset of $n = 100,000$ patients, an error of approximately $\pm 6$ individuals represents a negligible relative statistical error of $\frac{6}{1420} \approx 0.42\%$, while mathematically guaranteeing that no attacker can ever determine with certainty whether any specific individual patient is present in the nephropathy registry.

## 7.8 Unit 7 Methodological Synthesis and Review
Ethical integrity and statistical precision are indivisible:
- Uphold professional ethical standards (ASA, ISI), ensuring objective data reporting free from financial or political conflicts.
- Implement human subjects protections (Belmont Report: Respect for Persons, Beneficence, Justice) via rigorous informed consent and IRB oversight.
- Safeguard participant confidentiality using formal statistical disclosure control, including $k$-anonymity and cryptographically grounded $\epsilon$-Differential Privacy.
- Eliminate Questionable Research Practices (QRPs) through study preregistration, strictly separating exploratory data snooping from confirmatory testing.
- Diagnose and adjust for publication bias in meta-analyses using inverted funnel plots, Egger's regression test, and trim-and-fill algorithms.
"""

(DRAFT_DIR / "unit-7.md").write_text(u7_content.strip() + "\n", encoding="utf-8")
print("Unit 7 generated.")

# ==============================================================================
# UNIT 8
# ==============================================================================
u8_content = r"""# Unit 8: Scientific Communication, Reproducible Research & Technical Reporting

A scientific discovery does not truly exist until it has been clearly, accurately, and reproducibly communicated to the scientific community and the broader public. The ultimate objective of statistical research is not the computation of a $p$-value or the generation of an isolated tabular output; it is the generation of durable, verifiable scientific knowledge that can withstand adversarial scrutiny, independent replication, and real-world deployment. In the words of cognitive psychologist and Nobel laureate Daniel Kahneman: *"A reliable science must be a replicable science. If our findings cannot be reproduced by independent laboratories following our exact methods, our theories are nothing more than elaborate academic fiction."*

In the second decade of the twenty-first century, empirical science was shaken by the Replication Crisis—a systemic reckoning revealing that large percentages of landmark published findings across psychology, oncology, genetics, and economics fail to replicate in independent experiments. In response, modern statistical research methodology has embraced the Open Science and Reproducible Research paradigms. This unit examines the diagnostic causes of the reproducibility crisis, details the architectures of literate programming and automated data pipelines, articulates principles of technical reporting and graphical integrity, and provides international guidelines for ethical scientific communication.

## 8.1 The Replication Crisis in Empirical Science
In 2005, John P. A. Ioannidis published a landmark paper in *PLOS Medicine* boldly titled *"Why Most Published Research Findings Are False."* Using a formal Bayesian decision model, Ioannidis proved mathematically that whenever:
1. The prior probability of a research hypothesis being true is low (low pre-study odds $R$);
2. Empirical studies are conducted with small sample sizes and low statistical power ($1 - \beta$);
3. Investigators possess flexibility in data analysis and outcome definitions (researcher degrees of freedom);
4. High financial, political, or career incentives favor statistically significant discoveries;
the Positive Predictive Value (PPV)—the probability that a statistically significant research finding ($p < 0.05$) represents a true scientific effect—is less than $50\%$. Under standard academic conditions, a published "statistically significant discovery" is more likely to be a false-positive artifact than a true effect.

Ioannidis' theoretical proof was empirically confirmed a decade later:
- The Open Science Collaboration (2015): Replicated 100 empirical psychology studies published in top-tier journals. While $97\%$ of the original landmark papers reported statistically significant effects, only $36\%$ of the independent replications achieved statistical significance, and the average replicated effect size was less than half of the original published magnitude.
- The Reproducibility Project: Cancer Biology (2021): Attempted to replicate 193 experiments from 53 high-impact preclinical cancer research papers. Effect sizes in replications were, on average, $85\%$ smaller than original published findings, and only $46\%$ of evaluated experiments successfully replicated.

The diagnosis was clear: the reproducibility crisis was not driven by widespread criminal fraud, but by pervasive structural flaws in statistical research practices: severe underpowering, publication bias, unadjusted multiple testing, and non-transparent, irreproducible analysis workflows.

## 8.2 The Reproducible Research Paradigm: Literate Programming and Containerization
Historically, scientific communication relied on the "paper-and-pencil" narrative report: an academic manuscript describing methods in qualitative prose, accompanied by static tables and figures. The underlying raw data, data-cleaning scripts, and statistical code remained sequestered on private laboratory hard drives.

In 1992, Stanford geophysicist Jon Claerbout formulated the central maxim of reproducible computational research:
*"An article about computational science in a scientific publication is not the scholarship itself, it is merely advertising of the scholarship. The actual scholarship is the complete software development environment and the complete set of instructions which generated the figures."*

The reproducible research paradigm operationalizes Claerbout's maxim through three foundational computational architectures:
1. Literate Programming:
   Pioneered by computer scientist Donald Knuth in 1984. Instead of writing computer code with occasional comments, the author writes a human-readable scientific essay into which executable code chunks are embedded. Modern platforms—such as Quarto, R Markdown, and Jupyter Notebooks—weave narrative text, mathematical LaTeX equations, dynamic data transformations, and rendered graphics into a unified plain-text source document (`.qmd` or `.ipynb`). When the document is compiled, code executes directly against raw data, dynamically generating all numerical statistics and plots. If the underlying dataset is updated, re-compiling the document automatically regenerates every table and figure without manual copying and pasting.
2. Scripted Automated Pipelines:
   Data engineering workflows should be executed via dependency-directed workflow DAGs (Directed Acyclic Graphs) using tools such as GNU Make, Snakemake, or Nextflow. Every data ingestion, cleaning, transformation, and modeling step is scripted; manual spreadsheet manipulation ("pointing and clicking" in Excel) is strictly prohibited because manual actions are unversioned, undocumented, and irreproducible.
3. Computational Environment Containerization:
   Even identical code can produce disparate numerical outputs when executed on different operating systems or with different library versions. Containerization platforms (Docker, Singularity) bundle the complete operating system, specific programming language binaries (Python, R), exact dependency package versions, and configuration files into an immutable, portable software container. Running the container guarantees identical computational execution across any computer worldwide.

## 8.3 Structuring Academic Statistical Research Papers: The IMRaD Architecture
Scientific manuscripts reporting empirical quantitative investigations are traditionally structured according to the IMRaD architecture (Introduction, Methods, Results, and Discussion):

1. Introduction (The Scientific Rationale):
   - Establishes the broad substantive domain problem and theoretical background.
   - Synthesizes existing literature, identifying a critical empirical gap or unresolved tension.
   - States the precise research questions and formal conceptual hypotheses.
2. Methods (The Operational Blueprint):
   - Must provide sufficient operational detail to enable an independent investigator to replicate the entire investigation without consulting the original authors.
   - Participants and Sampling: Target population, sampling frame, recruitment procedures, inclusion/exclusion criteria, informed consent protocols, and demographic composition.
   - Experimental/Quasi-Experimental Design: Explicit structural architecture (e.g., Randomized Block Design, Regression Discontinuity), allocation concealment, blinding procedures (single, double, or triple blind).
   - Measurement Instrumentation: Operational definitions, psychometric scale properties, reliability coefficients ($\omega_{\text{total}}$), and calibration procedures.
   - Statistical Analysis Protocol: Complete mathematical specification of models, verification of distributional assumptions, missing data mechanisms and imputations, software package versions, and preregistration registration links.
3. Results (Empirical Evidence):
   - Presents findings objectively, without speculative theoretical interpretation.
   - Participant flow (CONSORT flow diagram documenting enrollment, randomization, allocation, drop-outs, and analyzed sample).
   - Baseline equivalence checks across groups.
   - Primary and secondary model outputs: point estimates, exact standard errors, standardized effect sizes, and exact $95\%$ confidence intervals.
   - Sensitivity audits and robustness checks demonstrating that inferential conclusions are invariant to modeling choices.
4. Discussion (Epistemic Interpretation):
   - Directly answers the core research questions in light of the empirical findings.
   - Contextualizes results within existing scientific theory and prior literature.
   - Thoroughly articulates methodological limitations, unmeasured confounders, measurement error, and constraints on generalizability (external validity).
   - Outlines actionable policy implications and directions for future research.

## 8.4 Principles of Graphical Integrity and Scientific Data Visualization
Data visualization is an essential component of scientific communication. Poorly designed graphics obscure patterns, mislead readers, and distort statistical conclusions. In his 1983 masterwork *The Visual Display of Quantitative Information*, Edward R. Tufte established the core principles of graphical excellence and data integrity:

1. The Data-Ink Ratio:
   The proportion of a graphic's total ink devoted to the non-redundant display of data information:
   $$\text{Data-Ink Ratio} = \frac{\text{Data-Ink}}{\text{Total Ink Used to Print the Graphic}} = 1.0 - \text{Proportion of Erasable Ink}$$
   Maximizing the data-ink ratio requires ruthlessly eliminating "chartjunk": decorative 3D effects, artificial drop shadows, heavy gridlines, superfluous background textures, and redundant legends. Every pixel or drop of ink should communicate substantive empirical variation.
2. Graphical Integrity and the Lie Factor:
   A graphic possesses graphical integrity when the visual representation of data points is strictly proportional to the numerical quantities being represented. Tufte defined the Lie Factor ($\mathrm{LF}$) as:
   $$\mathrm{Lie Factor} = \frac{\text{Size of Effect Shown in Graphic}}{\text{Size of Effect in Data}}$$
   where:
   $$\text{Size of Effect in Graphic} = \frac{|\text{Graphic Value}_2 - \text{Graphic Value}_1|}{\text{Graphic Value}_1}$$
   $$\text{Size of Effect in Data} = \frac{|\text{Data Value}_2 - \text{Data Value}_1|}{\text{Data Value}_1}$$
   - $\mathrm{LF} = 1.0$: Perfect graphical fidelity; visual changes mirror numerical changes exactly.
   - $\mathrm{LF} > 1.05$: Substantial graphical exaggeration; the graphic distorts the visual effect to appear larger than the underlying data warrants (e.g., truncating the vertical axis to make a $1\%$ change appear like a $500\%$ surge).
   - $\mathrm{LF} < 0.95$: Graphical suppression; the graphic visually minimizes real-world changes.
3. Perceptual Accessibility and Color Integrity (William Cleveland):
   - Never encode continuous quantitative scales using rainbow or jet colormaps, which introduce artificial perceptual boundaries due to non-linear luminance profiles. Use perceptually uniform sequential palettes (e.g., Viridis, Magma, Cividis).
   - Use diverging palettes only for data possessing a meaningful, natural neutral midpoint (e.g., zero change, balance).
   - Ensure color palettes are accessible to individuals with color vision deficiencies (deuteranopia, protanopia).

## 8.5 Communicating Statistical Uncertainty: Beyond Dichotomous $p$-Values
In 2016, the American Statistical Association (ASA) took the unprecedented step of publishing a formal consensus statement on statistical significance and $p$-values (Wasserstein & Lazar, 2016), repudiating the widespread scientific dogma surrounding the arbitrary threshold $p < 0.05$:

### The Six Foundational ASA Principles:
1. $p$-Values can indicate how incompatible the data are with a specified statistical model (usually the null hypothesis).
2. $p$-Values do *not* measure the probability that the studied hypothesis is true, nor the probability that the data were produced by random chance alone ($P(H_0 \mid \text{Data}) \ne P(\text{Data} \mid H_0)$).
3. Scientific conclusions and business or policy decisions should not be based solely on whether a $p$-value passes a specific threshold (such as $p < 0.05$).
4. Proper inference requires full reporting and transparency; cherry-picking models or omitting non-significant tests renders $p$-values uninterpretable.
5. A $p$-value, or statistical significance, does *not* measure the size of an effect or the importance of a result. A minuscule, clinically trivial effect can achieve $p < 0.0001$ in an enormous sample ($n = 1,000,000$), while a massive, lifesaving effect can yield $p = 0.12$ in a small trial ($n = 15$).
6. By itself, a $p$-value does not provide a good measure of evidence regarding a model or hypothesis.

Methodologists strongly advise replacing dichotomous declarations ("significant" versus "non-significant") with continuous estimation: reporting effect sizes (Cohen's $d$, odds ratios, regression slopes) accompanied by exact, narrow Confidence Intervals and complete posterior distributions.

## 8.6 International Reporting Guidelines: CONSORT, STROBE, PRISMA, and SAMPL
To combat non-transparent reporting, international consortia of methodologists and medical editors have developed standardized reporting checklists that authors must satisfy:

1. CONSORT (Consolidated Standards of Reporting Trials):
   Mandatory 25-item checklist and 4-stage participant flow diagram for randomized controlled trials (Enrollment, Intervention Allocation, Follow-up, and Analysis). Requires explicit reporting of randomization mechanisms, blinding procedures, primary outcomes, and intention-to-treat analyses.
2. STROBE (Strengthening the Reporting of Observational Studies in Epidemiology):
   Standardized guidelines for cohort, case-control, and cross-sectional observational studies, requiring explicit descriptions of participant selection, confounding adjustment, missing data methods, and sensitivity audits.
3. PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses):
   Standardized 27-item checklist and 4-phase flow diagram documenting the identification, screening, eligibility, and inclusion of studies in systematic reviews, including risk-of-bias assessments and publication bias evaluations.
4. SAMPL (Statistical Analyses and Methods in the Published Literature):
   Comprehensive reporting guidelines specifically targeting statistical modeling: requiring exact model equations, verification of assumptions, precise variable operationalizations, and exact $p$-values and confidence intervals.

## 8.7 Worked Problem Examples

### Fully worked question 1: Positive Predictive Value (PPV) of Research Findings
John Ioannidis' Bayesian mathematical framework evaluates the probability that a statistically significant finding ($p < 0.05$) reflects a true scientific relationship (the Positive Predictive Value, PPV).
Let:
- $\pi = P(H_1 \text{ is true})$ be the prior probability that a tested hypothesis is true in a given scientific domain.
- $R = \frac{\pi}{1 - \pi}$ be the pre-study odds of a true relationship.
- $\alpha$ be the nominal Type I error rate (significance threshold, $\alpha = 0.05$).
- $1 - \beta$ be the statistical power of the research study.

Consider a cutting-edge exploratory scientific discipline (e.g., candidate gene discovery for complex behavioral traits):
- Pre-study prior probability of a true biological association is $\pi = 0.010$ ($1.0\%$, corresponding to odds $R = 0.01 / 0.99 \approx 0.0101$).
- Typical studies are severely underpowered: statistical power is $1 - \beta = 0.20$ ($20.0\%$, $\beta = 0.80$).
- Studies are evaluated at nominal significance $\alpha = 0.05$.

1. Derive the mathematical formula for Positive Predictive Value (PPV) as a function of power $1 - \beta$, Type I error $\alpha$, and pre-study odds $R$.
2. Compute the exact PPV for this exploratory discipline in the absence of researcher bias.
3. If an investigator achieves $80\%$ power ($1 - \beta = 0.80$) in a confirmatory discipline where $\pi = 0.50$ ($R = 1.0$), compute the resulting PPV and contrast the two epistemological environments.

### Solution, step 1: Derive the Formula for Positive Predictive Value (PPV)
Let $T$ denote the event that a study yields a statistically significant result ($p < \alpha$, rejecting $H_0$).
By Bayes' Theorem:
$$\mathrm{PPV} = P(H_1 \text{ is true} \mid T) = \frac{P(T \mid H_1) P(H_1)}{P(T)}$$
The numerator is the probability of a True Positive:
$$P(T \mid H_1) P(H_1) = (1 - \beta) \pi$$
The denominator is the total probability of obtaining a statistically significant result (True Positives + False Positives):
$$P(T) = P(T \mid H_1) P(H_1) + P(T \mid H_0) P(H_0) = (1 - \beta)\pi + \alpha(1 - \pi)$$
Therefore:
$$\mathrm{PPV} = \frac{(1 - \beta)\pi}{(1 - \beta)\pi + \alpha(1 - \pi)}$$
Divide numerator and denominator by $1 - \pi$, noting that $R = \pi / (1 - \pi)$:
$$\mathrm{PPV} = \frac{(1 - \beta) R}{(1 - \beta) R + \alpha}$$

### Solution, step 2: Compute PPV in the Exploratory Scientific Discipline
Substitute the parameters:
- Power $1 - \beta = 0.20$
- Significance level $\alpha = 0.05$
- Prior probability $\pi = 0.010 \implies 1 - \pi = 0.990 \implies R = \frac{0.010}{0.990} \approx 0.010101$

Compute numerator:
$$\text{Numerator} = (1 - \beta) R = 0.20 \times 0.010101 \approx 0.002020$$
Compute denominator:
$$\text{Denominator} = 0.002020 + \alpha = 0.002020 + 0.050 = 0.052020$$
Compute PPV:
$$\mathrm{PPV} = \frac{0.002020}{0.052020} \approx \mathbf{0.0388} \quad (3.88\%)$$
In this exploratory research environment, when an investigator reports a "statistically significant discovery" at $p < 0.05$, there is only a $3.88\%$ probability that the discovery is a true biological effect! Over $96.1\%$ of all published statistically significant findings in this discipline are false-positive noise artifacts. This proves mathematically why underpowered exploratory science suffers catastrophic non-replication.

### Solution, step 3: Compute PPV in a High-Powered Confirmatory Discipline
In a mature confirmatory discipline testing strong theoretical hypotheses:
- $\pi = 0.50 \implies R = \frac{0.50}{0.50} = 1.0$ (even pre-study odds).
- High statistical power: $1 - \beta = 0.80$.
- Significance level: $\alpha = 0.05$.

Compute PPV:
$$\mathrm{PPV} = \frac{(1 - \beta) R}{(1 - \beta) R + \alpha} = \frac{0.80 \times 1.0}{(0.80 \times 1.0) + 0.05} = \frac{0.80}{0.80 + 0.05} = \frac{0.80}{0.85} \approx \mathbf{0.9412} \quad (94.12\%)$$
In this high-powered confirmatory environment, $94.1\%$ of published discoveries are true scientific effects. High statistical power combined with strong prior theoretical plausibility guarantees scientific reliability.

---

### Fully worked question 2: Edward Tufte's Lie Factor Calculation in Statistical Graphics
A national newspaper publishes an infographic illustrating the increase in annual municipal tax revenue from 2020 to 2024:
- In 2020, revenue was $D_1 = \$100\text{ million}$.
- In 2024, revenue was $D_2 = \$120\text{ million}$ (a genuine increase of $20.0\%$).

To represent this change graphically, the graphic designer drew two three-dimensional stacks of gold coins:
- The 2020 revenue is represented by a coin graphic with height $H_1 = 20\text{ mm}$ and width $W_1 = 10\text{ mm}$ (visual area $A_1 = 200\text{ mm}^2$).
- The designer scaled *both* the height and width of the 2024 coin graphic by a factor of $2.0$: height $H_2 = 40\text{ mm}$ and width $W_2 = 20\text{ mm}$ (visual surface area $A_2 = 800\text{ mm}^2$).
- Furthermore, because the graphic is rendered in 3D perspective, readers perceive visual volume: $V_1 = 10 \times 20 \times 10 = 2,000\text{ mm}^3$ versus $V_2 = 20 \times 40 \times 20 = 16,000\text{ mm}^3$.

1. Calculate the percentage change in the actual numerical data.
2. Calculate the perceived visual percentage change based on 2D surface area ($A$), and compute Edward Tufte's Lie Factor ($\mathrm{LF}_{\text{area}}$).
3. Calculate the perceived visual percentage change based on 3D volumetric perception ($V$), compute the volumetric Lie Factor ($\mathrm{LF}_{\text{volume}}$), and evaluate the graphic's integrity.

### Solution, step 1: Calculate the Real Percentage Change in Data
The actual numerical change in tax revenue is:
$$\Delta_{\text{data}} = \frac{D_2 - D_1}{D_1} = \frac{120 - 100}{100} = \frac{20}{100} = \mathbf{0.200} \quad (20.0\%)$$

### Solution, step 2: Calculate Surface Area Effect and Area Lie Factor
The visual surface area occupied by the 2020 graphic is:
$$A_1 = 20\text{ mm} \times 10\text{ mm} = 200\text{ mm}^2$$
The visual surface area occupied by the 2024 graphic is:
$$A_2 = 40\text{ mm} \times 20\text{ mm} = 800\text{ mm}^2$$
The percentage change shown visually in surface area is:
$$\Delta_{\text{graphic, area}} = \frac{A_2 - A_1}{A_1} = \frac{800 - 200}{200} = \frac{600}{200} = \mathbf{3.000} \quad (300.0\%)$$
Compute Edward Tufte's Lie Factor:
$$\mathrm{LF}_{\text{area}} = \frac{\text{Size of Effect in Graphic}}{\text{Size of Effect in Data}} = \frac{\Delta_{\text{graphic, area}}}{\Delta_{\text{data}}} = \frac{3.000}{0.200} = \mathbf{15.00}$$
By scaling both horizontal and vertical dimensions by $2.0$, the surface area grew by $300\%$. The Lie Factor is $15.0$, meaning the graphic visually exaggerates the true tax increase by a factor of 15!

### Solution, step 3: Calculate Volumetric Effect and Volumetric Lie Factor
Human visual perception naturally interprets 3D perspective cues as physical volume:
$$V_1 = 2,000\text{ mm}^3$$
$$V_2 = 16,000\text{ mm}^3$$
The percentage change shown in perceived visual volume is:
$$\Delta_{\text{graphic, volume}} = \frac{V_2 - V_1}{V_1} = \frac{16000 - 2000}{2000} = \frac{14000}{2000} = \mathbf{7.000} \quad (700.0\%)$$
Compute the Volumetric Lie Factor:
$$\mathrm{LF}_{\text{volume}} = \frac{\Delta_{\text{graphic, volume}}}{\Delta_{\text{data}}} = \frac{7.000}{0.200} = \mathbf{35.00}$$
Tufte established that any graphic with a Lie Factor outside $[0.95, 1.05]$ is unacceptable. A Lie Factor of $35.0$ represents severe graphical deception: a modest $20\%$ revenue increase is visually perceived as a massive $700\%$ explosion. The graphic violates fundamental scientific and ethical visualization standards.

---

### Fully worked question 3: Confidence Interval Overlap Fallacy in Two-Group Comparisons
A widespread statistical misconception among researchers is the "eyeball test" for comparing two independent group means: assuming that if the $95\%$ confidence intervals of two independent groups overlap, the difference between them cannot be statistically significant at $\alpha = 0.05$.
Consider two independent samples of size $n_1 = n_2 = 100$:
- Group 1: Sample mean $\bar{y}_1 = 10.0$, sample standard deviation $s_1 = 5.0$, standard error $\mathrm{SE}_1 = 5.0 / \sqrt{100} = 0.50$.
- Group 2: Sample mean $\bar{y}_2 = 11.4$, sample standard deviation $s_2 = 5.0$, standard error $\mathrm{SE}_2 = 5.0 / \sqrt{100} = 0.50$.

1. Construct the independent $95\%$ confidence intervals for $\mu_1$ and $\mu_2$, and verify that they visually overlap.
2. Conduct the formal independent two-sample $z$-test testing $H_0: \mu_2 - \mu_1 = 0$ at $\alpha = 0.05$ (two-tailed critical value $z_{0.025} = 1.960$).
3. Prove mathematically why two independent $95\%$ confidence intervals can overlap substantially while their difference remains statistically significant at $p < 0.05$.

### Solution, step 1: Construct Independent Group Confidence Intervals
For Group 1 ($\bar{y}_1 = 10.0, \mathrm{SE}_1 = 0.50$):
$$\mathrm{CI}_1 = 10.0 \pm 1.960 \times 0.50 = 10.0 \pm 0.980 \implies [\mathbf{9.02}, \; \mathbf{10.98}]$$
For Group 2 ($\bar{y}_2 = 11.4, \mathrm{SE}_2 = 0.50$):
$$\mathrm{CI}_2 = 11.4 \pm 1.960 \times 0.50 = 11.4 \pm 0.980 \implies [\mathbf{10.42}, \; \mathbf{12.38}]$$
Examine the numerical bounds:
The upper bound of $\mathrm{CI}_1$ ($10.98$) is strictly greater than the lower bound of $\mathrm{CI}_2$ ($10.42$).
The two intervals overlap across the region $[10.42, 10.98]$ (an overlap of $0.56$ units).
A naive researcher relying on visual inspection would incorrectly conclude: *"The confidence intervals overlap; therefore, there is no statistically significant difference between the groups."*

### Solution, step 2: Conduct the Formal Two-Sample Hypothesis Test
The difference between the two sample means is:
$$\hat{\Delta} = \bar{y}_2 - \bar{y}_1 = 11.4 - 10.0 = \mathbf{1.40}$$
By the independence of the two groups, the standard error of the difference is:
$$\mathrm{SE}_{\text{diff}} = \sqrt{\mathrm{SE}_1^2 + \mathrm{SE}_2^2} = \sqrt{(0.50)^2 + (0.50)^2} = \sqrt{0.25 + 0.25} = \sqrt{0.50} \approx \mathbf{0.7071}$$
Compute the test statistic:
$$z = \frac{\hat{\Delta} - 0}{\mathrm{SE}_{\text{diff}}} = \frac{1.40}{0.7071} \approx \mathbf{1.9799}$$
Compare with the critical threshold at $\alpha = 0.05$:
$$z_{\text{calculated}} = 1.980 > z_{0.025} = 1.960$$
The two-tailed $p$-value is $P(|Z| \ge 1.980) \approx \mathbf{0.0477} \quad (p < 0.05)$.
The difference is statistically significant at the $\alpha = 0.05$ level!

### Solution, step 3: Mathematical Proof of the Overlap Fallacy
Let the standard errors be equal: $\mathrm{SE}_1 = \mathrm{SE}_2 = \mathrm{SE}$.
The half-width of each individual $95\%$ confidence interval is $W_{\text{single}} = 1.96 \cdot \mathrm{SE}$.
Two intervals just touch (zero overlap) when:
$$\bar{y}_2 - \bar{y}_1 = 2 \times W_{\text{single}} = 2 \times (1.96 \cdot \mathrm{SE}) = 3.92 \cdot \mathrm{SE}$$
However, the standard error of the difference is:
$$\mathrm{SE}_{\text{diff}} = \sqrt{\mathrm{SE}^2 + \mathrm{SE}^2} = \sqrt{2} \cdot \mathrm{SE} \approx 1.414 \cdot \mathrm{SE}$$
The difference is statistically significant at $\alpha = 0.05$ whenever:
$$\bar{y}_2 - \bar{y}_1 \ge 1.96 \cdot \mathrm{SE}_{\text{diff}} = 1.96 \times (\sqrt{2} \cdot \mathrm{SE}) \approx 2.772 \cdot \mathrm{SE}$$
Observe the critical boundary comparison:
$$2.772 \cdot \mathrm{SE} < 3.920 \cdot \mathrm{SE}$$
A difference of $2.772 \cdot \mathrm{SE}$ is statistically significant at $p = 0.05$, yet it allows the individual confidence intervals to overlap by:
$$\text{Overlap} = 3.920 \cdot \mathrm{SE} - 2.772 \cdot \mathrm{SE} = 1.148 \cdot \mathrm{SE}$$
In fact, two individual $95\%$ confidence intervals can overlap by up to approximately $29\%$ of their length and still remain statistically significantly different at $p < 0.05$! Inspecting individual confidence interval overlap is an invalid heuristic; researchers must construct the Confidence Interval of the Difference:
$$\mathrm{CI}_{\text{diff}} = 1.40 \pm 1.960(0.7071) = 1.40 \pm 1.3859 \implies [\mathbf{0.014}, \; \mathbf{2.786}]$$
Because $\mathrm{CI}_{\text{diff}}$ excludes zero, the difference is strictly significant at $p < 0.05$.

## 8.8 Unit 8 Methodological Synthesis and Review
Scientific communication is the final, decisive stage of the research enterprise:
- Recognize the structural causes of the replication crisis (low power, publication bias, researcher degrees of freedom), and deploy preregistration to preserve evidentiary validity.
- Implement the reproducible research paradigm using literate programming (Quarto, R Markdown), automated DAG pipelines, and containerization (Docker).
- Structure research manuscripts according to the IMRaD framework, providing comprehensive operational details enabling full independent replication.
- Maintain graphical integrity (Tufte's Lie Factor $\approx 1.0$, high data-ink ratio, perceptual color uniformity).
- Abandon dichotomous $p$-value declarations in favor of continuous estimation, effect sizes, and exact confidence intervals.
- Adhere strictly to international reporting guidelines (CONSORT, STROBE, PRISMA, SAMPL).
"""

(DRAFT_DIR / "unit-8.md").write_text(u8_content.strip() + "\n", encoding="utf-8")
print("Unit 8 generated.")
