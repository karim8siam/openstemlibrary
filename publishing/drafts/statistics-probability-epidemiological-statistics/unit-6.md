# Unit 6: Screening, Diagnostic Testing & Receiver Operating Characteristic (ROC) Analysis

In public health and clinical medicine, the early detection of disease among asymptomatic individuals through population screening offers the promise of secondary prevention: halting pathologic progression before irreversible biological damage or metastatic dissemination occurs. However, no diagnostic or screening test is biologically infallible. Imperfect tests produce false positives that induce psychological distress and unnecessary invasive procedures, as well as false negatives that foster dangerous complacency. To establish the clinical validity of a diagnostic technology, epidemiologists employ formal quantitative criteria. In this unit, we formalize the natural history of disease and the Wilson-Jungner screening criteria, establish the fundamental $2 \times 2$ diagnostic matrix (sensitivity, specificity, false positive and false negative rates), demonstrate the mathematical dominance of disease prevalence over positive predictive values, formulate Bayesian clinical reasoning using diagnostic likelihood ratios and the Fagan nomogram, construct continuous Receiver Operating Characteristic (ROC) curves, prove the mathematical equivalence between the Area Under the Curve (AUC) and the Wilcoxon-Mann-Whitney statistic, evaluate Youden’s $J$ cutpoint optimization, and analyze the methodological biases that distort screening evaluations (lead-time bias, length-biased sampling, and overdiagnosis).

## 6.1 Principles of Secondary Prevention, Natural History & The Wilson-Jungner Criteria

Screening is defined as the presumptive identification of unrecognized disease or defect by the application of tests, examinations, or other procedures that can be applied rapidly to asymptomatic target populations. Screening sorts out apparently well persons who probably have a disease from those who probably do not.

### Natural History of Disease and the Critical Window
The biological trajectory of disease unfolds across distinct phases:
1. **Stage of Susceptibility**: Biological exposure has occurred, but pathologic alterations have not yet initiated.
2. **Pre-symptomatic (Subclinical) Phase**: Pathologic changes have initiated, but the disease remains entirely asymptomatic. Within this phase lies the **Detectably Pre-clinical Phase (DPCP)**: the window of time beginning when the disease first becomes detectable by an objective screening biomarker ($t_d$) and ending when clinical symptoms naturally emerge ($t_s$).
3. **Clinical Phase**: Symptoms manifest, prompting clinical diagnosis and therapy.

For a screening program to be medically effective, there must exist a **critical point** located within the DPCP: an inflection point before which therapeutic intervention confers substantially greater survival or functional recovery than treatment delayed until clinical symptom onset. If the critical point occurs before the screening test can detect the lesion (e.g., highly aggressive pancreatic adenocarcinoma), or if therapy is equally effective whenever applied, screening confers zero mortality benefit.

### The Wilson-Jungner Screening Criteria
In 1968, James Maxwell Glover Wilson and Gunnar Jungner established the foundational ten principles of screening for the World Health Organization:
1. The condition sought should be an important health problem for the individual and community.
2. There should be an accepted treatment for patients with recognized disease.
3. Facilities for diagnosis and treatment should be available.
4. There should be a recognizable latent or early symptomatic stage.
5. There should be a suitable test or examination.
6. The test should be acceptable to the general population.
7. The natural history of the condition, including development from latent to declared disease, should be adequately understood.
8. There should be an agreed policy on whom to treat as patients.
9. The cost of case-finding (including diagnosis and subsequent treatment) should be economically balanced in relation to possible total expenditure on medical care.
10. Case-finding should be a continuous process and not a "once and for all" project.

## 6.2 The Fundamental Diagnostic Matrix: Sensitivity, Specificity, and Error Rates

To evaluate the intrinsic diagnostic accuracy of a binary screening test, test results are cross-tabulated against an independent **Gold Standard** (the definitive diagnostic criterion, such as tissue biopsy, surgical histopathology, or necropsy):

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Screening Test Result</th><th>True Disease Present ($D^+$)</th><th>True Disease Absent ($D^-$)</th><th>Total Tested</th></tr>
</thead>
<tbody>
<tr><td><strong>Test Positive ($T^+$)</strong></td><td>$TP$ (True Positive)</td><td>$FP$ (False Positive)</td><td>$n_{\text{test}+} = TP + FP$</td></tr>
<tr><td><strong>Test Negative ($T^-$)</strong></td><td>$FN$ (False Negative)</td><td>$TN$ (True Negative)</td><td>$n_{\text{test}-} = FN + TN$</td></tr>
<tr><td><strong>Total Reference</strong></td><td>$N_D = TP + FN$</td><td>$N_H = FP + TN$</td><td>$N = TP + FP + FN + TN$</td></tr>
</tbody>
</table></div>

### Sensitivity (True Positive Rate)
**Sensitivity** ($Se$), or the **True Positive Rate** ($TPR$), is the conditional probability that a truly diseased individual tests positive:

$$Se = P(T^+ \mid D^+) = \frac{TP}{TP + FN} = \frac{TP}{N_D}$$

A test with $Se = 0.95$ correctly detects $95\%$ of diseased individuals, while missing $5\%$ ($FN = 5\%$). The complementary probability is the **False Negative Rate** ($FNR = 1 - Se$). High-sensitivity tests are prized for "ruling out" disease (the clinical mnemonic **SnNOut**: High **S**e**n**sitivity, **N**egative test rules **Out** disease).

### Specificity (True Negative Rate)
**Specificity** ($Sp$), or the **True Negative Rate** ($TNR$), is the conditional probability that a truly healthy individual tests negative:

$$Sp = P(T^- \mid D^-) = \frac{TN}{FP + TN} = \frac{TN}{N_H}$$

A test with $Sp = 0.98$ correctly clears $98\%$ of healthy individuals, while incorrectly flagging $2\%$ as false alarms. The complementary probability is the **False Positive Rate** ($FPR = 1 - Sp$). High-specificity tests are prized for "ruling in" disease (the clinical mnemonic **SpPIn**: High **Sp**ecificity, **P**ositive test rules **In** disease).

Crucially, **sensitivity and specificity are intrinsic properties of the diagnostic test technology**: within a defined patient population, they remain mathematically constant regardless of how common or rare the disease is in the community.

## 6.3 Positive and Negative Predictive Values: The Mathematical Dominance of Prevalence

While clinicians evaluate test technology using sensitivity and specificity, the patient who receives a positive test result asks a fundamentally different question: *"Given that my test is positive, what is the actual probability that I truly have the disease?"*

This clinical question is answered by the **predictive values**.

### Positive Predictive Value (PPV)
The **Positive Predictive Value** ($PPV$), or post-test probability of disease following a positive result, is the conditional probability that an individual who tests positive is truly diseased:

$$PPV = P(D^+ \mid T^+) = \frac{TP}{TP + FP}$$

Applying **Bayes' Theorem** decomposes the $PPV$ into the test's operating characteristics and the pre-test disease **prevalence** ($\pi = P(D^+)$):

$$PPV = \frac{P(T^+ \mid D^+) P(D^+)}{P(T^+ \mid D^+) P(D^+) + P(T^+ \mid D^-) P(D^-)} = \frac{Se \cdot \pi}{Se \cdot \pi + (1 - Sp) \cdot (1 - \pi)}$$

### Negative Predictive Value (NPV)
The **Negative Predictive Value** ($NPV$), or post-test probability of health following a negative result, is the conditional probability that an individual who tests negative is truly free of disease:

$$NPV = P(D^- \mid T^-) = \frac{TN}{FN + TN} = \frac{Sp \cdot (1 - \pi)}{(1 - Se) \cdot \pi + Sp \cdot (1 - \pi)}$$

### The Paradox of Rare Disease Screening
Notice the critical algebraic feature of Bayes' formula: **Predictive values are profoundly dependent upon disease prevalence ($\pi$)**.
Even for a test with extraordinary analytical accuracy (e.g., $Se = 99\%$ and $Sp = 99\%$), if the disease is rare in the general screening population ($\pi = 1 / 1,000 = 0.001$), the positive predictive value collapses:

$$PPV = \frac{(0.99)(0.001)}{(0.99)(0.001) + (1 - 0.99)(1 - 0.001)} = \frac{0.00099}{0.00099 + (0.01)(0.999)} = \frac{0.00099}{0.00099 + 0.00999} = \frac{0.00099}{0.01098} \approx 0.0902 \quad (9.02\%)$$

Out of every 100 positive test results, **more than 90 are false positives!** This mathematical reality explains why universal population screening for low-prevalence cancers or rare conditions is counter-productive: the massive flood of false-positive results causes severe patient trauma and overwhelms diagnostic healthcare resources with unnecessary invasive biopsies.

## 6.4 Likelihood Ratios, Diagnostic Odds Ratios & The Bayesian Fagan Nomogram

To overcome the prevalence-dependence of predictive values while maintaining clinically actionable intuition, modern evidence-based medicine utilizes **Likelihood Ratios** ($LR$).

### Positive Likelihood Ratio (LR+)
The **Positive Likelihood Ratio** is the ratio of the probability of a positive test in a diseased person to the probability of a positive test in a non-diseased person:

$$LR^+ = \frac{P(T^+ \mid D^+)}{P(T^+ \mid D^-)} = \frac{Se}{1 - Sp} = \frac{\text{True Positive Rate}}{\text{False Positive Rate}}$$

- $LR^+ = 1.0$: Diagnostic test provides zero information; post-test probability equals pre-test probability.
- $LR^+ > 10.0$: Strong diagnostic evidence; highly effective at ruling in disease.
- $LR^+ \in (5, 10)$: Moderate diagnostic evidence.

### Negative Likelihood Ratio (LR-)
The **Negative Likelihood Ratio** is the ratio of the probability of a negative test in a diseased person to the probability of a negative test in a non-diseased person:

$$LR^- = \frac{P(T^- \mid D^+)}{P(T^- \mid D^-)} = \frac{1 - Se}{Sp} = \frac{\text{False Negative Rate}}{\text{True Negative Rate}}$$

- $LR^- < 0.1$: Strong diagnostic evidence; highly effective at ruling out disease.
- $LR^- \in (0.1, 0.2)$: Moderate diagnostic evidence.

### The Odds Form of Bayes' Theorem and the Fagan Nomogram
Recall that odds is defined as $\text{Odds} = p / (1 - p)$. The **Pre-test Odds** of disease is:

$$\text{Pre-test Odds} = \frac{\pi}{1 - \pi}$$

By Bayes' theorem, multiplying the pre-test odds by the likelihood ratio directly yields the **Post-test Odds**:

$$\text{Post-test Odds}(D^+ \mid T^+) = \text{Pre-test Odds} \times LR^+$$

$$\text{Post-test Odds}(D^+ \mid T^-) = \text{Pre-test Odds} \times LR^-$$

Once the post-test odds are obtained, the post-test probability ($PPV$ or $1 - NPV$) is recovered via:

$$\text{Post-test Probability} = \frac{\text{Post-test Odds}}{1 + \text{Post-test Odds}}$$

In clinical practice, this Bayesian updating is executed instantly using the **Fagan Nomogram**: a graphical three-axis alignment chart linking pre-test probability on the left, likelihood ratio in the center, and post-test probability on the right with a straight line.

### Diagnostic Odds Ratio (DOR)
The overall diagnostic performance of a test is summarized by the **Diagnostic Odds Ratio** ($DOR$):

$$DOR = \frac{LR^+}{LR^-} = \frac{Se / (1 - Sp)}{(1 - Se) / Sp} = \frac{Se \cdot Sp}{(1 - Se)(1 - Sp)} = \frac{TP \cdot TN}{FP \cdot FN}$$

A diagnostic test with $DOR = 1.0$ has zero discriminatory capacity; values exceeding $100$ indicate excellent diagnostic separation.

## 6.5 Continuous Biomarkers and Receiver Operating Characteristic (ROC) Analysis

Many modern diagnostic tests do not generate binary positive/negative outcomes; instead, they output continuous quantitative biomarkers (e.g., serum Prostate-Specific Antigen in $\text{ng/mL}$, fasting blood glucose in $\text{mg/dL}$, or coronary artery calcium scores). To classify an individual as "diseased," the clinician must designate a **decision cutoff threshold** $c$.

Let $X$ denote the continuous test score. By convention, higher biomarker values indicate greater likelihood of disease:
$$\text{Classify } T^+ \text{ if } X \ge c, \qquad \text{Classify } T^- \text{ if } X < c$$

Let $f_D(x)$ and $f_H(x)$ denote the probability density functions of the biomarker in the diseased and healthy populations, respectively. For any designated cutoff $c$:

$$Se(c) = P(X \ge c \mid D^+) = \int_c^\infty f_D(x) \, dx$$

$$Sp(c) = P(X < c \mid D^-) = \int_{-\infty}^c f_H(x) \, dx \implies FPR(c) = 1 - Sp(c) = \int_c^\infty f_H(x) \, dx$$

As the cutoff $c$ shifts:
- If $c \to -\infty$: Every patient is classified positive $\implies Se \to 1.0$, but $Sp \to 0.0$ ($FPR \to 1.0$).
- If $c \to +\infty$: Every patient is classified negative $\implies Se \to 0.0$, but $Sp \to 1.0$ ($FPR \to 0.0$).

### Construction of the ROC Curve
Originated in electrical radar signal detection during World War II, the **Receiver Operating Characteristic (ROC) Curve** is a graphical plot of the **True Positive Rate** ($Se(c)$) on the vertical $y$-axis versus the **False Positive Rate** ($1 - Sp(c)$) on the horizontal $x$-axis, traced continuously as the decision cutoff $c$ varies from $+\infty$ to $-\infty$.

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>ROC Graphic Feature</th><th>Mathematical Meaning</th><th>Epidemiological Interpretation</th></tr>
</thead>
<tbody>
<tr><td><strong>Point $(0, 0)$</strong></td><td>$c = +\infty$: Classify all as negative.</td><td>Zero false alarms, but misses every true case ($Se = 0, Sp = 1$).</td></tr>
<tr><td><strong>Point $(1, 1)$</strong></td><td>$c = -\infty$: Classify all as positive.</td><td>Catches every case, but falsely flags every healthy person ($Se = 1, Sp = 0$).</td></tr>
<tr><td><strong>Point $(0, 1)$</strong></td><td>Ideal diagnostic perfection.</td><td>$100\%$ Sensitivity and $100\%$ Specificity (zero error).</td></tr>
<tr><td><strong>45-Degree Diagonal Line</strong></td><td>$Se(c) = FPR(c)$ for all $c$.</td><td>The test performs no better than random guessing (flipping an unweighted coin).</td></tr>
</tbody>
</table></div>

## 6.6 Area Under the Curve (AUC), Youden's J, and Screening Evaluation Biases

### The Area Under the Curve (AUC / c-statistic)
The global discriminatory accuracy of a continuous diagnostic test is quantified by the **Area Under the ROC Curve** ($AUC$), also known as the **concordance index** ($c$-statistic):

$$AUC = \int_0^1 Se(FPR) \, d(FPR) = \int_{-\infty}^\infty Se(c) \left| \frac{d(1 - Sp(c))}{dc} \right| dc$$

The $AUC$ spans the interval $[0.5, 1.0]$:
- $AUC = 0.50$: Pure chance; zero diagnostic discrimination.
- $AUC \in [0.70, 0.80)$: Acceptable discrimination.
- $AUC \in [0.80, 0.90)$: Excellent discrimination.
- $AUC \ge 0.90$: Outstanding diagnostic accuracy ($AUC = 1.0$ is perfect separation).

### Probabilistic Equivalence to the Wilcoxon-Mann-Whitney Statistic
A celebrated mathematical theorem established by David Green and John Swets (1966) and popularized by James Hanley and Barbara McNeil (1982) proves that the **AUC is mathematically identical to the Wilcoxon-Mann-Whitney U-statistic probability**:

$$AUC = P(X_D > X_H)$$

where $X_D$ is the biomarker score of a randomly chosen diseased individual and $X_H$ is the biomarker score of a randomly chosen healthy individual. Thus, an $AUC$ of $0.85$ means that if one diseased patient and one healthy patient are selected at random, there is an $85\%$ probability that the diseased patient will exhibit a higher biomarker concentration than the healthy patient!

For empirical sample data with $n_D$ cases and $n_H$ controls, the non-parametric trapezoidal $AUC$ is:

$$\widehat{AUC} = \frac{1}{n_D n_H} \sum_{i=1}^{n_D} \sum_{j=1}^{n_H} I(X_{Di} > X_{Hj}) + 0.5 \cdot I(X_{Di} = X_{Hj})$$

### Cutpoint Optimization: Youden's J Statistic
To choose the single "optimal" clinical cutoff threshold $c^*$ that maximizes diagnostic efficacy, William J. Youden (1950) introduced **Youden’s Index** ($J$):

$$J(c) = Se(c) + Sp(c) - 1 = Se(c) - FPR(c)$$

Geometrically, $J(c)$ represents the vertical distance between the ROC curve and the 45-degree chance diagonal at cutoff $c$. The optimal cutoff $c^*$ is the point that maximizes $J(c)$:

$$c^* = \arg\max_c [Se(c) + Sp(c) - 1]$$

### Methodological Biases in Screening Program Evaluation
Evaluating whether a screening program successfully reduces population mortality requires randomized clinical trials with mortality endpoints, because observational comparisons of screened vs unscreened patients are distorted by three insidious survival biases:

1. **Lead-Time Bias**:
   **Lead time** is the duration by which screening advances the date of diagnosis compared to standard clinical symptom presentation. Even if screening and early therapy have zero biological effect on the ultimate date of death, screened patients will survive longer *from the date of diagnosis* purely because their diagnosis was established earlier in time! Comparing 5-year survival rates between screened and unscreened cases creates an illusion of therapeutic benefit caused entirely by clock-resetting.
2. **Length-Biased Sampling (Prognostic Selection)**:
   Screening tests administered at periodic intervals preferentially detect slow-growing, indolent, biologically indolent tumors that spend years in the Detectably Pre-clinical Phase. Highly aggressive, fast-growing malignancies pass rapidly through the DPCP between screening rounds and emerge as symptomatic "interval cancers." Consequently, screened cases have inherently superior biological prognoses, creating false impressions of screening efficacy.
3. **Overdiagnosis Bias**:
   **Overdiagnosis** is the detection of subclinical pseudodisease: microscopic, histologically abnormal lesions that would never have progressed to cause clinical symptoms, impairment, or death during the patient’s natural lifetime (e.g., indolent thyroid papillary microcarcinomas, low-grade prostate cancer, ductal carcinoma in situ). Overdiagnosed patients undergo toxic surgeries and chemotherapy with zero possibility of clinical benefit, while artificially inflating survival statistics.

## 6.7 Clinical Utility and Decision Curve Analysis (DCA)

While Sensitivity, Specificity, and the Area Under the ROC Curve evaluate statistical discrimination, they do not tell a clinician whether using a diagnostic biomarker will actually improve clinical patient outcomes. An expensive or invasive biomarker with an $AUC = 0.82$ might confer zero clinical utility if its false-positive referrals lead to severe biopsy complications.

To quantify clinical utility across varying patient preferences, Andrew Vickers and Elena Elkin (2006) introduced **Decision Curve Analysis (DCA)** based on the concept of **Net Benefit** ($NB$):

$$NB(p_t) = \frac{TP}{N} - \frac{FP}{N} \left( \frac{p_t}{1 - p_t} \right) = \text{True Positive Fraction} - \text{False Positive Fraction} \times \text{Odds}(p_t)$$

where $p_t \in (0, 1)$ is the **decision threshold probability** at which a patient or clinician is indifferent between initiating treatment and withholding treatment.
- The weighting factor $p_t / (1 - p_t)$ explicitly penalizes false-positive decisions relative to true-positive benefits according to the clinical cost-benefit ratio.
- In a Decision Curve plot, the Net Benefit of the diagnostic strategy is plotted against $p_t$ and compared against two default clinical reference policies: "Treat All Patients" and "Treat No Patients".
- A diagnostic biomarker has clinical utility over the threshold range where its Net Benefit curve lies strictly above both default strategies. Decision Curve Analysis provides the quantitative bridge linking epidemiologic diagnostic accuracy with clinical decision-making.

## Fully worked question 1: Bayesian Clinical Diagnosis: Sensitivity, Specificity, Predictive Values, and Fagan Nomogram

### Question
A specialized clinical serology laboratory evaluates a fourth-generation Chemiluminescent Immunoassay (CLIA) for detecting Hepatitis C Virus (HCV) antibodies. Validation against viral RNA PCR gold standard in an analytical laboratory study demonstrates:
- Sensitivity: $Se = 0.980$ ($98.0\%$).
- Specificity: $Sp = 0.995$ ($99.5\%$).

The immunoassay is deployed in two vastly different clinical settings:
- **Setting A (High-Risk Needle-Exchange Addiction Clinic)**: HCV infection prevalence is $\pi_A = 0.200$ ($20.0\%$).
- **Setting B (Low-Risk General Asymptomatic Blood Donor Screening)**: HCV infection prevalence is $\pi_B = 0.001$ ($0.1\%$, 1 per 1,000 donors).

1. For both Setting A and Setting B, calculate the Positive Predictive Value ($PPV$) and the Negative Predictive Value ($NPV$).
2. Compute the Positive Likelihood Ratio ($LR^+$) and Negative Likelihood Ratio ($LR^-$).
3. Using the odds formulation of Bayes' theorem, demonstrate how the pre-test odds in Setting B are updated by $LR^+$ to yield the post-test odds, and show that this matches the $PPV$ computed via Bayes' theorem. What are the clinical and ethical implications for blood donor notification?

### Solution, step 1: Calculate PPV and NPV for Setting A and Setting B
1. **Setting A (High-Risk Clinic, $\pi_A = 0.20$)**:
   Apply Bayes' Theorem:
   $$PPV_A = \frac{Se \cdot \pi_A}{Se \cdot \pi_A + (1 - Sp)(1 - \pi_A)} = \frac{(0.980)(0.200)}{(0.980)(0.200) + (1 - 0.995)(1 - 0.200)}$$
   $$= \frac{0.1960}{0.1960 + (0.005)(0.800)} = \frac{0.1960}{0.1960 + 0.0040} = \frac{0.1960}{0.2000} = 0.9800 \quad (98.00\%)$$

   $$NPV_A = \frac{Sp \cdot (1 - \pi_A)}{(1 - Se)\pi_A + Sp(1 - \pi_A)} = \frac{(0.995)(0.800)}{(1 - 0.980)(0.200) + (0.995)(0.800)}$$
   $$= \frac{0.7960}{(0.020)(0.200) + 0.7960} = \frac{0.7960}{0.0040 + 0.7960} = \frac{0.7960}{0.8000} = 0.9950 \quad (99.50\%)$$

   In Setting A, a positive test is overwhelmingly accurate ($PPV = 98.0\%$).

2. **Setting B (Low-Risk Blood Donors, $\pi_B = 0.001$)**:
   $$PPV_B = \frac{Se \cdot \pi_B}{Se \cdot \pi_B + (1 - Sp)(1 - \pi_B)} = \frac{(0.980)(0.001)}{(0.980)(0.001) + (0.005)(0.999)}$$
   $$= \frac{0.000980}{0.000980 + 0.004995} = \frac{0.000980}{0.005975} \approx 0.1640 \quad (16.40\%)$$

   $$NPV_B = \frac{(0.995)(0.999)}{(0.020)(0.001) + (0.995)(0.999)} = \frac{0.994005}{0.000020 + 0.994005} = \frac{0.994005}{0.994025} \approx 0.99998 \quad (99.998\%)$$

   In Setting B, despite a test specificity of $99.5\%$, **only $16.4\%$ of screen-positive blood donors actually have Hepatitis C!** Fully $83.6\%$ of all positive test results are false positives.

### Solution, step 2: Calculate Likelihood Ratios
$$LR^+ = \frac{Se}{1 - Sp} = \frac{0.980}{1 - 0.995} = \frac{0.980}{0.005} = 196.0$$

$$LR^- = \frac{1 - Se}{Sp} = \frac{1 - 0.980}{0.995} = \frac{0.020}{0.995} \approx 0.0201$$

The test has a massive $LR^+ = 196.0$ (ruling in disease strongly) and a very small $LR^- \approx 0.020$ (ruling out disease strongly).

### Solution, step 3: Bayesian odds formulation and ethical implications
In Setting B ($\pi_B = 0.001$):
$$\text{Pre-test Odds} = \frac{\pi_B}{1 - \pi_B} = \frac{0.001}{0.999} \approx 0.0010010$$

Multiplying by $LR^+ = 196.0$:
$$\text{Post-test Odds} = \text{Pre-test Odds} \times LR^+ = 0.0010010 \times 196.0 \approx 0.196196$$

Converting back to probability:
$$\text{Post-test Probability} = \frac{\text{Post-test Odds}}{1 + \text{Post-test Odds}} = \frac{0.196196}{1 + 0.196196} = \frac{0.196196}{1.196196} \approx 0.1640 \quad (16.40\%)$$
This matches the Bayesian $PPV_B$ precisely.

**Clinical and Ethical Implications**:
In blood banking, blood units testing positive are discarded to guarantee transfusion safety. However, notifying donors that they are "HCV positive" based on a single screening immunoassay is ethically reckless: more than 5 out of 6 positive donors are completely healthy. Standard blood bank protocols mandate that screen-positive samples undergo **confirmatory secondary testing** (such as nucleic acid RT-PCR) before communicating a diagnosis to the donor.

## Fully worked question 2: Empirical ROC Construction, Trapezoidal AUC Integration, and Youden’s J Cutpoint Optimization

### Question
An oncology research laboratory investigates a novel serum microRNA biomarker ($\text{miR-21}$, expressed in relative quantification units) for distinguishing patients with early-stage ovarian carcinoma from benign pelvic masses. The biomarker concentrations measured in $n_D = 6$ confirmed ovarian cancer patients and $n_H = 6$ healthy/benign control patients are:
- **Cancer Patients ($X_D$)**: $2.8, \, 3.4, \, 4.2, \, 5.1, \, 6.0, \, 7.5$
- **Control Patients ($X_H$)**: $1.2, \, 1.8, \, 2.2, \, 3.0, \, 3.8, \, 4.8$

1. For candidate diagnostic cutoff thresholds $c \in \{1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0\}$, determine the Sensitivity ($Se$), Specificity ($Sp$), and False Positive Rate ($FPR = 1 - Sp$). Tabulate the coordinates of the empirical ROC curve.
2. Calculate the non-parametric Area Under the Curve ($\widehat{AUC}$) using both trapezoidal integration and the Mann-Whitney $U$-statistic formulation.
3. Compute Youden’s Index $J(c) = Se(c) + Sp(c) - 1$ across all candidate cutoffs, determine the optimal decision threshold $c^*$, and report the diagnostic sensitivity and specificity achieved at that optimal cutoff.

### Solution, step 1: Tabulate empirical ROC coordinates across cutoffs
A patient tests positive if $X \ge c$.
- Cancer group ($n_D = 6$): $\{2.8, 3.4, 4.2, 5.1, 6.0, 7.5\}$
- Control group ($n_H = 6$): $\{1.2, 1.8, 2.2, 3.0, 3.8, 4.8\}$

Let us evaluate $TP(c)$ (cancer $\ge c$) and $FP(c)$ (control $\ge c$):
- **$c = 1.0$**: All 6 cancers $\ge 1.0 \implies Se = 6/6 = 1.000$. All 6 controls $\ge 1.0 \implies FP = 6 \implies FPR = 6/6 = 1.000, Sp = 0.000$. Point: $(1.0, 1.0)$.
- **$c = 2.0$**: Cancers $\ge 2.0$: all 6 $\implies Se = 6/6 = 1.000$. Controls $\ge 2.0$: $\{2.2, 3.0, 3.8, 4.8\}$ (4 controls) $\implies FPR = 4/6 \approx 0.667, Sp = 2/6 \approx 0.333$. Point: $(0.667, 1.000)$.
- **$c = 3.0$**: Cancers $\ge 3.0$: $\{3.4, 4.2, 5.1, 6.0, 7.5\}$ (5 cancers) $\implies Se = 5/6 \approx 0.833$. Controls $\ge 3.0$: $\{3.0, 3.8, 4.8\}$ (3 controls) $\implies FPR = 3/6 = 0.500, Sp = 0.500$. Point: $(0.500, 0.833)$.
- **$c = 4.0$**: Cancers $\ge 4.0$: $\{4.2, 5.1, 6.0, 7.5\}$ (4 cancers) $\implies Se = 4/6 \approx 0.667$. Controls $\ge 4.0$: $\{4.8\}$ (1 control) $\implies FPR = 1/6 \approx 0.167, Sp = 5/6 \approx 0.833$. Point: $(0.167, 0.667)$.
- **$c = 5.0$**: Cancers $\ge 5.0$: $\{5.1, 6.0, 7.5\}$ (3 cancers) $\implies Se = 3/6 = 0.500$. Controls $\ge 5.0$: 0 controls $\implies FPR = 0/6 = 0.000, Sp = 1.000$. Point: $(0.000, 0.500)$.
- **$c = 6.0$**: Cancers $\ge 6.0$: $\{6.0, 7.5\}$ (2 cancers) $\implies Se = 2/6 \approx 0.333$. Controls $\ge 6.0$: 0 controls $\implies FPR = 0.000, Sp = 1.000$. Point: $(0.000, 0.333)$.
- **$c = 8.0$**: Cancers $\ge 8.0$: 0 cancers $\implies Se = 0.000$. Controls $\ge 8.0$: 0 $\implies FPR = 0.000, Sp = 1.000$. Point: $(0.0, 0.0)$.

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Cutoff $c$</th><th>Sensitivity $Se(c)$</th><th>Specificity $Sp(c)$</th><th>False Positive Rate $FPR(c)$</th><th>ROC Coordinate $(x, y)$</th><th>Youden's Index $J(c)$</th></tr>
</thead>
<tbody>
<tr><td>$\infty$ ($8.0$)</td><td>$0.000$</td><td>$1.000$</td><td>$0.000$</td><td>$(0.000, 0.000)$</td><td>$0.000$</td></tr>
<tr><td>$5.0$</td><td>$0.500$</td><td>$1.000$</td><td>$0.000$</td><td>$(0.000, 0.500)$</td><td>$+0.500$</td></tr>
<tr><td>$4.0$</td><td>$0.667$</td><td>$0.833$</td><td>$0.167$</td><td>$(0.167, 0.667)$</td><td>$+0.500$</td></tr>
<tr><td>$3.0$</td><td>$0.833$</td><td>$0.500$</td><td>$0.500$</td><td>$(0.500, 0.833)$</td><td>$+0.333$</td></tr>
<tr><td>$2.0$</td><td>$1.000$</td><td>$0.333$</td><td>$0.667$</td><td>$(0.667, 1.000)$</td><td>$+0.333$</td></tr>
<tr><td>$-\infty$ ($1.0$)</td><td>$1.000$</td><td>$0.000$</td><td>$1.000$</td><td>$(1.000, 1.000)$</td><td>$0.000$</td></tr>
</tbody>
</table></div>

### Solution, step 2: Area Under the Curve via Mann-Whitney U-statistic and trapezoids
1. **Mann-Whitney U-Statistic Method**:
   We compare each of the 6 cancer values against all 6 control values ($6 \times 6 = 36$ pairwise comparisons). We count how many times $X_{Di} > X_{Hj}$:
   - $X_{D1} = 2.8 > \{1.2, 1.8, 2.2\}$ (3 controls) $\implies 3$
   - $X_{D2} = 3.4 > \{1.2, 1.8, 2.2, 3.0\}$ (4 controls) $\implies 4$
   - $X_{D3} = 4.2 > \{1.2, 1.8, 2.2, 3.0, 3.8\}$ (5 controls) $\implies 5$
   - $X_{D4} = 5.1 > \{1.2, 1.8, 2.2, 3.0, 3.8, 4.8\}$ (all 6 controls) $\implies 6$
   - $X_{D5} = 6.0 > \text{all 6 controls} \implies 6$
   - $X_{D6} = 7.5 > \text{all 6 controls} \implies 6$

   Total pairwise wins $U_D = 3 + 4 + 5 + 6 + 6 + 6 = 30$.
   $$\widehat{AUC} = \frac{U_D}{n_D \times n_H} = \frac{30}{6 \times 6} = \frac{30}{36} \approx 0.8333 \quad (83.33\%)$$

2. **Trapezoidal Rule Integration**:
   Integrating under the empirical ROC step segments from $(0, 0)$ to $(1, 1)$:
   - Segment from $x = 0$ to $x = 1/6$: width $= 1/6$, average height $= (0.500 + 0.667)/2 = 0.5833 \implies \text{Area} = (1/6)(0.5833) = 0.0972$.
   - Segment from $x = 1/6$ to $x = 3/6$: width $= 2/6$, average height $= (0.667 + 0.833)/2 = 0.7500 \implies \text{Area} = (2/6)(0.750) = 0.2500$.
   - Segment from $x = 3/6$ to $x = 4/6$: width $= 1/6$, average height $= (0.833 + 1.000)/2 = 0.9167 \implies \text{Area} = (1/6)(0.9167) = 0.1528$.
   - Segment from $x = 4/6$ to $x = 1$: width $= 2/6$, height $= 1.000 \implies \text{Area} = (2/6)(1.000) = 0.3333$.
   Sum of areas $= 0.0972 + 0.2500 + 0.1528 + 0.3333 = 0.8333$.
   Both methods identically confirm $\widehat{AUC} = 0.833$ (excellent diagnostic discrimination).

### Solution, step 3: Youden's Index optimization
From our table of $J(c) = Se(c) + Sp(c) - 1$:
- Cutoff $c = 5.0$: $J = 0.500 + 1.000 - 1 = +0.500$. (Provides $100\%$ Specificity, $50\%$ Sensitivity).
- Cutoff $c = 4.0$: $J = 0.667 + 0.833 - 1 = +0.500$. (Provides $83.3\%$ Specificity, $66.7\%$ Sensitivity).

**Clinical Decision Rationale**:
In ovarian cancer screening, where false-positive surgery carries high morbidity, the investigator selects **$c^* = 4.0\text{ units}$** (or $c^* = 5.0$ if zero false alarms are demanded). At $c^* = 4.0$, the test achieves $Se = 66.7\%$ and $Sp = 83.3\%$ with maximum Youden Index $J = 0.50$.

## Fully worked question 3: Diagnostic Screening in Populations: Lead-Time Bias, Length Bias, and Overdiagnosis

### Question
A health authority in Scandinavia evaluates a mobile mammography breast cancer screening trial conducted between 2010 and 2025. Two non-randomized cohorts of women aged 50–69 are compared:
- **Screened Cohort ($n_{\text{scr}} = 10,000$)**: Screened biennially. Exactly $300$ invasive breast cancers are diagnosed. Among these 300 women, 240 survive at least 5 years from their date of diagnosis ($5\text{-year survival} = 80.0\%$). Over the 15-year trial, 60 breast cancer deaths occur in the screened cohort ($15\text{-year mortality} = 6.0 \text{ per 1,000 women}$).
- **Unscreened Control Cohort ($n_{\text{unscr}} = 10,000$)**: Routine symptomatic care. Exactly $200$ invasive breast cancers are diagnosed upon clinical symptom presentation. Among these 200 women, 100 survive at least 5 years from diagnosis ($5\text{-year survival} = 50.0\%$). Over the 15-year trial, 60 breast cancer deaths occur in the unscreened cohort ($15\text{-year mortality} = 6.0 \text{ per 1,000 women}$).
- Extensive natural history modeling indicates that screening advances the diagnosis date by an average **lead time of $\bar{L} = 3.0\text{ years}$**.

1. Analyze the apparent 5-year survival statistics: compute the survival improvement ($80\%$ vs $50\%$). Explain why comparing 5-year survival from diagnosis creates a deceptive illusion of screening efficacy, and prove why **disease-specific population mortality** is the only valid primary endpoint.
2. Demonstrate how **lead-time bias** mathematically inflates 5-year survival without delaying death. If an unscreened patient is diagnosed symptomatically at age 55 and dies at age 59 (survival $= 4\text{ years}$, 5-year survivor $=$ No), show what happens if screening detects her cancer at age 52 with the exact same death age of 59.
3. Calculate the excess cancer detection count in the screened arm ($300$ vs $200$). Formally define **overdiagnosis**, estimate the overdiagnosis fraction, and describe the clinical and societal harms of overdiagnosing pseudodisease.

### Solution, step 1: Deceptive 5-year survival vs population mortality
1. **Apparent 5-Year Survival Comparison**:
   $$\text{Survival}_{\text{screened}} = \frac{240}{300} = 0.800 \quad (80.0\%)$$
   $$\text{Survival}_{\text{unscreened}} = \frac{100}{200} = 0.500 \quad (50.0\%)$$
   A naive observer would celebrate an apparent $30.0\%$ absolute increase in 5-year survival ($RRR = 60\%$).

2. **True Population Disease-Specific Mortality**:
   $$\text{Mortality Rate}_{\text{screened}} = \frac{60}{10,000} = 0.0060 = 6.0 \text{ per 1,000 women}$$
   $$\text{Mortality Rate}_{\text{unscreened}} = \frac{60}{10,000} = 0.0060 = 6.0 \text{ per 1,000 women}$$
   $$\text{Mortality Rate Ratio} = \frac{6.0}{6.0} = 1.000$$

**Methodological Conclusion**:
The screening program had **zero effect on saving human lives**: exactly 60 women died of breast cancer in both arms! The apparent leap in 5-year survival from $50\%$ to $80\%$ was entirely a mathematical artifact of **lead-time bias**, **length bias**, and **overdiagnosis**.
Survival calculated from the date of diagnosis is completely invalid because screening artificially changes the starting point of the survival clock. Only **cause-specific population mortality** (deaths divided by total randomized population) has a fixed, uncompromised denominator and serves as the gold standard endpoint.

### Solution, step 2: Mathematical mechanics of lead-time bias
Consider a patient whose tumor has a predetermined biological trajectory:
- Biological inception: Age 45.
- Symptomatic presentation: Age 55.
- Biological death: Age 59.

1. **Under Symptomatic Care (Unscreened)**:
   - Diagnosed at Age 55.
   - Dies at Age 59.
   - Observed Survival: $59 - 55 = 4\text{ years}$.
   - 5-Year Survival Status: **Fails** ($4 < 5\text{ years}$).

2. **Under Screening (with Lead Time $\bar{L} = 3\text{ years}$)**:
   - Diagnosed by mammography at Age 52 ($55 - 3 = 52$).
   - Dies at the exact same Age 59 (treatment had zero biological efficacy).
   - Observed Survival: $59 - 52 = 7\text{ years}$.
   - 5-Year Survival Status: **Succeeds** ($7 \ge 5\text{ years}$)!

Screening did not prolong this woman's life by even one single day. She lived for exactly 59 years. The only consequence of screening was that she lived with the anxiety, fear, and surgical side effects of knowing she had cancer for 7 years instead of 4 years. Yet in the hospital's statistical ledger, she was miraculously converted from a "5-year failure" into a "5-year survival triumph."

### Solution, step 3: Overdiagnosis evaluation and clinical harms
In this cohort:
- Diagnosed in screened arm: $300$ cancers.
- Diagnosed in unscreened arm: $200$ cancers.
- Excess cancers diagnosed: $300 - 200 = 100$ excess cases.

**Formal Definition of Overdiagnosis**:
Overdiagnosis is the detection through screening of indolent, non-progressive, or extremely slow-growing cancers that would never have produced clinical symptoms or threatened the patient's life before she died of unrelated natural causes (e.g., cardiovascular disease or old age).

**Estimated Overdiagnosis Fraction**:
Relative to all screen-detected cancers:
$$\text{Overdiagnosis Fraction} = \frac{\text{Excess Screen-Detected Cancers}}{\text{Total Screened Cancers}} = \frac{100}{300} = 0.3333 \quad (33.33\%)$$
One out of every three breast cancers detected in the screening program represents an overdiagnosed pseudodisease!

**Harms of Overdiagnosis**:
Because pathologists cannot reliably distinguish between lethal and indolent micro-cancers under a microscope, all 100 overdiagnosed women underwent unnecessary partial or total mastectomies, radiation therapy, and systemic endocrine chemotherapy. They suffered physical scarring, chronic lymphedema, sexual dysfunction, and intense psychological trauma—all to treat a disease that was never going to harm them. Balancing true mortality reduction against the grave harms of overdiagnosis is the central ethical dilemma of population cancer screening.
