# Unit 7: Research Ethics, Data Integrity, Confidentiality & Publication Practices

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

## 7.8 Unit 7 Methodological Synthesis and Review
Ethical integrity and statistical precision are indivisible:
- Uphold professional ethical standards (ASA, ISI), ensuring objective data reporting free from financial or political conflicts.
- Implement human subjects protections (Belmont Report: Respect for Persons, Beneficence, Justice) via rigorous informed consent and IRB oversight.
- Safeguard participant confidentiality using formal statistical disclosure control, including $k$-anonymity and cryptographically grounded $\epsilon$-Differential Privacy.
- Eliminate Questionable Research Practices (QRPs) through study preregistration, strictly separating exploratory data snooping from confirmatory testing.
- Diagnose and adjust for publication bias in meta-analyses using inverted funnel plots, Egger's regression test, and trim-and-fill algorithms.
