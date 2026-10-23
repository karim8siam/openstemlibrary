#!/usr/bin/env python3
"""
Generate Units 2, 3, and 4 of Epidemiological Statistics with high academic depth.
"""
from pathlib import Path

OUT_DIR = Path("publishing/drafts/statistics-probability-epidemiological-statistics")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# UNIT 2 (Expanded for >= 3300 words)
# -------------------------------------------------------------
unit2 = r"""# Unit 2: Measures of Association & Public Health Impact: Risk Ratios, Odds Ratios & Attributable Fractions

Once disease frequency is quantified across distinct subpopulations, the central scientific goal of analytical epidemiology is to assess whether exposure to an environmental agent, behavioral habit, occupational hazard, or medical intervention alters the likelihood of developing disease. To accomplish this, epidemiologists construct **measures of association**, which contrast disease frequency across exposed and unexposed groups on either a multiplicative (relative) or an additive (absolute) scale. While relative measures provide insight into biologic etiology and causal strength, absolute difference measures quantify the public health burden and the preventable fraction of disease in the community. In this unit, we formalize the mathematics of the Risk Ratio ($RR$), Rate Ratio, and Odds Ratio ($OR$), establish the rare disease condition under which the odds ratio approximates relative risk, derive the asymptotic sampling distributions and confidence intervals via the multivariate Delta method and Woolf's logit method, examine Attributable Risk ($AR$), Population Attributable Fraction ($PAF$), and evaluate the clinical metrics of Number Needed to Treat ($NNT$) and Number Needed to Harm ($NNH$).

## 2.1 The 2x2 Contingency Table and Relative Measures: Risk Ratio and Rate Ratio

The standard analytic format for evaluating dichotomous exposures and binary disease outcomes is the classical $2 \times 2$ contingency table. In a prospective cohort study of $N$ participants initially free of disease, participants are classified by exposure status ($E^+$ vs $E^-$) and subsequently monitored for disease occurrence ($D^+$ vs $D^-$):

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Exposure Classification</th><th>Diseased ($D^+$)</th><th>Non-Diseased ($D^-$)</th><th>Total Cohort at Risk</th><th>Cumulative Risk ($R$)</th></tr>
</thead>
<tbody>
<tr><td><strong>Exposed ($E^+$)</strong></td><td>$a$</td><td>$b$</td><td>$n_1 = a + b$</td><td>$R_1 = a / n_1$</td></tr>
<tr><td><strong>Unexposed ($E^-$)</strong></td><td>$c$</td><td>$d$</td><td>$n_0 = c + d$</td><td>$R_0 = c / n_0$</td></tr>
<tr><td><strong>Total Population</strong></td><td>$m_1 = a + c$</td><td>$m_0 = b + d$</td><td>$N = a + b + c + d$</td><td>$R_{\text{total}} = m_1 / N$</td></tr>
</tbody>
</table></div>

### Mathematical Definition of the Risk Ratio
The **Risk Ratio** ($RR$), also universally designated as the **Relative Risk**, is the ratio of the cumulative incidence of disease in the exposed group to that in the unexposed group over the designated time interval:

$$RR = \frac{R_1}{R_0} = \frac{a / n_1}{c / n_0} = \frac{a(c + d)}{c(a + b)}$$

The risk ratio is a non-negative dimensionless scalar spanning $[0, \infty)$:
- $RR = 1.0$: Null hypothesis of no association; the exposure neither increases nor decreases disease risk.
- $RR > 1.0$: Positive association; the exposure increases disease risk (harmful exposure / risk factor). For example, $RR = 2.5$ indicates that exposed individuals experience $2.5$ times the risk of unexposed individuals.
- $RR < 1.0$: Negative (inverse) association; the exposure reduces disease risk (protective factor / intervention efficacy).

When disease occurrence is measured using incidence density across person-time denominators ($PT_1$ and $PT_0$), the corresponding relative measure is the **Rate Ratio** ($IRR$):

$$IRR = \frac{IR_1}{IR_0} = \frac{a / PT_1}{c / PT_0}$$

### Asymptotic Sampling Distribution of ln(RR) via the Delta Method
Because the empirical ratio $\widehat{RR} = \widehat{R}_1 / \widehat{R}_0$ is constrained to be non-negative, its finite-sample sampling distribution is severely skewed right. To perform valid statistical inference, we apply a logarithmic transformation $\theta = \ln(RR) = \ln(R_1) - \ln(R_0)$, which maps the parameter onto the entire real line $(-\infty, \infty)$ and accelerates convergence to Gaussian normality.

Assuming independent binomial sampling in the two exposed cohorts:
$$a \sim \text{Binomial}(n_1, R_1), \quad c \sim \text{Binomial}(n_0, R_0)$$

The sample estimates $\widehat{R}_1 = a / n_1$ and $\widehat{R}_0 = c / n_0$ have variances:
$$\text{Var}(\widehat{R}_1) = \frac{R_1(1 - R_1)}{n_1}, \quad \text{Var}(\widehat{R}_0) = \frac{R_0(1 - R_0)}{n_0}$$

Applying the first-order **Delta Method** to the transformation $g(p) = \ln(p)$, where $g'(p) = 1/p$:
$$\text{Var}(\ln \widehat{R}_1) \approx [g'(R_1)]^2 \text{Var}(\widehat{R}_1) = \frac{1}{R_1^2} \frac{R_1(1 - R_1)}{n_1} = \frac{1 - R_1}{n_1 R_1} = \frac{1 - a/n_1}{a} = \frac{1}{a} - \frac{1}{n_1}$$

Because the two cohorts are statistically independent:
$$\text{Var}(\ln \widehat{RR}) = \text{Var}(\ln \widehat{R}_1) + \text{Var}(\ln \widehat{R}_0) \approx \left(\frac{1}{a} - \frac{1}{n_1}\right) + \left(\frac{1}{c} - \frac{1}{n_0}\right)$$

The standard error on the natural logarithmic scale is:
$$\text{SE}(\ln \widehat{RR}) = \sqrt{\frac{1}{a} - \frac{1}{n_1} + \frac{1}{c} - \frac{1}{n_0}} = \sqrt{\frac{b}{a n_1} + \frac{d}{c n_0}}$$

A $100(1 - \alpha)\%$ confidence interval for $\ln(RR)$ is $\ln \widehat{RR} \pm z_{1 - \alpha/2} \text{SE}(\ln \widehat{RR})$. Exponentiating both bounds yields the exact confidence limits for the Risk Ratio:

$$CI_{1 - \alpha}(RR) = \left[ \widehat{RR} \cdot \exp\left(-z_{1 - \alpha/2} \text{SE}(\ln \widehat{RR})\right), \, \widehat{RR} \cdot \exp\left(z_{1 - \alpha/2} \text{SE}(\ln \widehat{RR})\right) \right]$$

## 2.2 The Odds Ratio: Retrospective Sampling Invariance and Rare Disease Approximation

The **odds** of an event is defined as the probability that the event occurs divided by the probability that it does not occur: $\text{Odds} = p / (1 - p)$. In the $2 \times 2$ table, the odds of disease among exposed individuals is:

$$\text{Odds}_1 = \frac{R_1}{1 - R_1} = \frac{a / n_1}{b / n_1} = \frac{a}{b}$$

Similarly, the odds of disease among unexposed individuals is:

$$\text{Odds}_0 = \frac{R_0}{1 - R_0} = \frac{c / n_0}{d / n_0} = \frac{c}{d}$$

The **Disease Odds Ratio** ($OR$) is defined as the ratio of these two odds:

$$OR = \frac{\text{Odds}_1}{\text{Odds}_0} = \frac{a / b}{c / d} = \frac{a \cdot d}{b \cdot c}$$

Because this algebraic formula multiplies the diagonal cells and divides by the off-diagonal cells, the odds ratio is universally termed the **cross-product ratio**.

### Mathematical Invariance Under Retrospective Case-Control Sampling
The odds ratio possesses a profound mathematical property that makes it the cornerstone of case-control studies: **directional symmetry**. Suppose that instead of sampling prospectively forward from exposure to disease, we sample retrospectively based on disease status, recruiting a fixed sample of $m_1 = a + c$ cases and $m_0 = b + d$ controls.

In this retrospective case-control design, the **Exposure Odds** among diseased individuals is:
$$\text{Exposure Odds}_{\text{cases}} = \frac{P(E^+ \mid D^+)}{P(E^- \mid D^+)} = \frac{a / m_1}{c / m_1} = \frac{a}{c}$$

The exposure odds among healthy controls is:
$$\text{Exposure Odds}_{\text{controls}} = \frac{P(E^+ \mid D^-)}{P(E^- \mid D^-)} = \frac{b / m_0}{d / m_0} = \frac{b}{d}$$

Evaluating the ratio of exposure odds:

$$\text{Exposure Odds Ratio} = \frac{a / c}{b / d} = \frac{a \cdot d}{b \cdot c} \equiv \text{Disease Odds Ratio}$$

Thus, the odds ratio calculated from a retrospective case-control study is mathematically identical to the odds ratio that would have been obtained had the entire underlying population been followed prospectively in a cohort study! Neither cumulative risk nor the risk ratio can be computed directly from a case-control study because the investigator artificially fixes the ratio of cases to controls ($m_1 / m_0$), completely distorting the marginal disease probability $R$. The odds ratio circumvent this limitation entirely.

### The Rare Disease Assumption
How does the Odds Ratio relate to the Risk Ratio? Expanding the ratio:

$$OR = \frac{a / (a + b)}{c / (c + d)} \times \frac{1 - R_0}{1 - R_1} = RR \times \left(\frac{1 - R_0}{1 - R_1}\right)$$

When the disease is rare in both the exposed and unexposed populations—specifically, when $R_1 < 0.05$ and $R_0 < 0.05$—the proportions of non-cases approach unity: $1 - R_1 \approx 1$ and $1 - R_0 \approx 1$. Consequently:

$$\frac{1 - R_0}{1 - R_1} \approx 1 \implies OR \approx RR$$

Under the **rare disease assumption**, the odds ratio calculated from a case-control study serves as an extraordinarily accurate numerical proxy for the true population relative risk. However, if the outcome is common (e.g., childhood obesity with $R_1 = 0.40$ and $R_0 = 0.20$), the odds ratio severely exaggerates the relative risk:
$$RR = \frac{0.40}{0.20} = 2.00, \qquad OR = \frac{0.40 / 0.60}{0.20 / 0.80} = \frac{0.667}{0.250} = 2.67$$

### Woolf's Logit Method for Odds Ratio Confidence Intervals
By the multivariate delta method applied to the natural logarithm of the cross-product ratio $\ln(\widehat{OR}) = \ln(a) - \ln(b) - \ln(c) + \ln(d)$, the asymptotic variance under a multinomial or product-binomial model is:

$$\text{Var}(\ln \widehat{OR}) \approx \frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d}$$

This elegant formulation, derived by Barnet Woolf (1955), yields the standard error:

$$\text{SE}(\ln \widehat{OR}) = \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d}}$$

A $95\%$ asymptotic confidence interval for the odds ratio is:

$$CI_{0.95}(OR) = \left[ \widehat{OR} \cdot \exp\left(-1.96 \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d}}\right), \, \widehat{OR} \cdot \exp\left(+1.96 \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d}}\right) \right]$$

If any cell count is small, Haldane and Gart's correction adds $0.5$ to each cell to reduce finite-sample bias.

## 2.3 Measures of Absolute Impact: Risk Difference, Attributable Risk, and Attributable Fractions

While relative measures ($RR, OR$) evaluate the strength of an etiologic association and are essential for biological causal inference, public health policymakers require measures on the **additive scale** to assess the actual human burden of disease that could be eliminated by eradicating an exposure.

### Risk Difference (Attributable Risk)
The **Risk Difference** ($RD$), historically termed the **Attributable Risk** ($AR$) or **Excess Risk**, is the arithmetic difference between the cumulative incidence in the exposed group and the cumulative incidence in the unexposed group:

$$RD = R_1 - R_0 = \frac{a}{n_1} - \frac{c}{n_0}$$

The risk difference represents the absolute excess probability of disease attributable specifically to the exposure among exposed individuals. Its units are the same as risk (a proportion per time interval), and it spans the interval $[-1.0, +1.0]$:
- $RD = 0$: Null hypothesis of no excess risk.
- $RD > 0$: The exposure inflicts an absolute excess disease burden.
- $RD < 0$: The exposure is protective, representing an **absolute risk reduction** ($ARR = R_0 - R_1$).

Because $\widehat{R}_1$ and $\widehat{R}_0$ are independent binomial proportions, the variance of the risk difference is simply the sum of their independent sampling variances:

$$\text{Var}(\widehat{RD}) = \frac{R_1(1 - R_1)}{n_1} + \frac{R_0(1 - R_0)}{n_0}$$

The standard Wald 95% confidence interval is $\widehat{RD} \pm 1.96 \sqrt{\text{Var}(\widehat{RD})}$.

### Attributable Fraction Among the Exposed (Etiologic Fraction)
The **Attributable Fraction in the Exposed** ($AF_e$), also termed the **Attributable Proportion in the Exposed** or **Etiologic Fraction**, measures the proportion of disease occurrences among exposed individuals that would be prevented if the exposure were entirely removed:

$$AF_e = \frac{R_1 - R_0}{R_1} = \frac{RD}{R_1} = \frac{RR - 1}{RR} = 1 - \frac{1}{RR}$$

For example, if cigarette smoking produces a lung cancer relative risk of $RR = 10.0$ among heavy smokers, then $AF_e = (10 - 1) / 10 = 0.90$ ($90\%$). This means that ninety percent of lung cancer cases diagnosed in heavy smokers are directly attributable to their tobacco exposure, and would not have occurred had they remained lifelong non-smokers (assuming causal exchangeability).

### Population Attributable Risk (PAR) and Population Attributable Fraction (PAF)
From the standpoint of municipal or national healthcare planning, exposed individuals represent only a subset of the total population. The **Population Attributable Risk** ($PAR$) measures the excess disease incidence observed in the total combined population ($R_{\text{total}}$) compared to the unexposed baseline:

$$PAR = R_{\text{total}} - R_0$$

Let $p_e = n_1 / N$ denote the prevalence of the exposure in the total population. By the Law of Total Probability, the total population incidence is a weighted average:

$$R_{\text{total}} = p_e R_1 + (1 - p_e) R_0$$

Subtracting $R_0$ yields:

$$PAR = p_e R_1 + (1 - p_e) R_0 - R_0 = p_e (R_1 - R_0) = p_e \times RD$$

The **Population Attributable Fraction** ($PAF$), originally derived by Morton L. Levin (1953), expresses this excess as a percentage of the total population disease burden:

$$PAF = \frac{R_{\text{total}} - R_0}{R_{\text{total}}} = \frac{PAR}{R_{\text{total}}}$$

Substituting $R_{\text{total}} = p_e R_1 + (1 - p_e) R_0$ and dividing numerator and denominator by $R_0$ yields **Levin’s Classical Formula**:

$$PAF = \frac{p_e (RR - 1)}{p_e (RR - 1) + 1}$$

Alternatively, when working from case-control studies where exposure prevalence among diseased cases ($p_{e \mid D} = a / m_1$) is readily available, **Miettinen’s Formula** (1974) provides an identical calculation:

$$PAF = p_{e \mid D} \left( \frac{RR - 1}{RR} \right) \approx p_{e \mid D} \left( \frac{OR - 1}{OR} \right)$$

The PAF is arguably the most vital metric for setting public health priorities: an exposure with a modest relative risk ($RR = 1.3$) that is pervasive throughout the population ($p_e = 0.60$, such as physical inactivity) may produce a vastly larger PAF than an exposure with a gigantic relative risk ($RR = 20.0$) that is extraordinarily rare ($p_e = 0.001$, such as an industrial chemical).

## 2.4 Geometric Interpretations, Logarithmic Scales, and Score Intervals

The mathematical geometry of epidemiological effect measures reveals deep structural dualities between additive risk differences and multiplicative risk ratios. When risks are plotted in a Cartesian unit square with coordinates $(R_0, R_1) \in [0, 1]^2$, iso-relative risk contours represent straight rays emanating from the origin $(0, 0)$ with slope $RR$:
$$R_1 = RR \cdot R_0$$
By contrast, iso-risk difference contours represent parallel lines with slope $+1$ and intercept $RD$:
$$R_1 = R_0 + RD$$
Because human survival probabilities are bounded within $[0, 1]$, an exposure that produces a large relative risk (say, $RR = 5.0$) cannot mathematically maintain that constant multiplier across high baseline risks; if $R_0 = 0.30$, $RR = 5.0$ would imply an impossible risk $R_1 = 1.50$. Consequently, biological mechanisms frequently conform to additive limits, emphasizing why epidemiologists evaluate both additive and multiplicative scales when assessing public health interventions.

### Score-Based Confidence Intervals
While Woolf's Wald-type interval for the odds ratio and the delta-method interval for the risk ratio are computationally simple, they rely on first-order Taylor series approximations that can exhibit poor coverage in small samples or when proportions approach $0$ or $1$. The **Score Test Confidence Interval**, originated by E. B. Wilson (1927) for a single proportion and extended by Miettinen and Nurminen (1985) for risk differences and risk ratios, test-inverts the efficient profile score statistic without relying on estimated standard errors in the denominator. For the Risk Difference, the score statistic enforces the null constraint $R_1 - R_0 = \Delta_0$ in the variance calculation:
$$\widetilde{\text{Var}}(RD \mid \Delta_0) = \frac{\tilde{R}_1(\Delta_0)(1 - \tilde{R}_1(\Delta_0))}{n_1} + \frac{\tilde{R}_0(\Delta_0)(1 - \tilde{R}_0(\Delta_0))}{n_0}$$
where $\tilde{R}_1(\Delta_0)$ and $\tilde{R}_0(\Delta_0)$ are constrained maximum likelihood estimates under $H_0$. Inverting this quadratic score equation yields confidence intervals that never overshoot $[0, 1]$ and maintain exact nominal coverage across skewed contingency tables.

## 2.5 Clinical Metrics: Number Needed to Treat (NNT) and Number Needed to Harm (NNH)

In clinical epidemiology, evidence-based medicine, and randomized controlled trial reporting, abstract proportions and logarithmic ratios can obscure direct clinical utility. To bridge this communication gap, Laupacis, Sackett, and Roberts (1988) introduced the **Number Needed to Treat** ($NNT$).

### Number Needed to Treat (NNT)
When an experimental intervention reduces disease risk relative to a control or placebo ($R_1 < R_0$), the Absolute Risk Reduction is $ARR = R_0 - R_1 > 0$. The $NNT$ is defined as the mathematical reciprocal of the absolute risk reduction:

$$NNT = \frac{1}{ARR} = \frac{1}{R_0 - R_1}$$

The $NNT$ represents the expected number of patients who must receive the medical therapy over a designated treatment duration in order to prevent exactly one additional adverse clinical outcome. For example, if a novel antihypertensive agent reduces 5-year stroke risk from $R_0 = 0.10$ ($10\%$) in the standard control group to $R_1 = 0.06$ ($6\%$) in the treatment group:
$$ARR = 0.10 - 0.06 = 0.04 \quad (4\%)$$
$$NNT = \frac{1}{0.04} = 25$$
A clinician must treat 25 hypertensive patients for five years to prevent exactly one stroke.

### Number Needed to Harm (NNH)
Conversely, when an exposure or pharmaceutical side effect increases the risk of an adverse event ($R_1 > R_0$), the absolute risk increase is $ARI = R_1 - R_0 > 0$. The **Number Needed to Harm** ($NNH$) is:

$$NNH = \frac{1}{ARI} = \frac{1}{R_1 - R_0}$$

The $NNH$ represents the number of individuals exposed to the agent required for exactly one additional person to experience the harmful adverse outcome. Comparing $NNT$ for therapeutic benefit against $NNH$ for severe adverse drug reactions provides the fundamental quantitative basis for risk-benefit clinical decision analysis. When communicating with patients, presenting $NNT$ alongside baseline risks prevents framing biases that frequently arise when pharmaceuticals are marketed using relative risk reductions alone.

## Fully worked question 1: Comprehensive Cohort Analysis: RR, OR, AR, PAF & Delta CIs

### Question
A large prospective cohort study in cardiovascular epidemiology tracks $N = 10,000$ middle-aged civil servants over a 10-year follow-up period to assess the etiologic role of severe physical inactivity on incident coronary heart disease (CHD). At baseline, $n_1 = 3,000$ individuals are classified as physically inactive (exposed), while $n_0 = 7,000$ are classified as physically active (unexposed). Over the 10-year period, 240 incident CHD events occur among the inactive cohort, and 210 incident CHD events occur among the active cohort. No participants were lost to follow-up.

1. Construct the complete $2 \times 2$ contingency table. Calculate the 10-year cumulative risk of CHD in the exposed ($R_1$) and unexposed ($R_0$) groups, the Risk Ratio ($RR$), and the Odds Ratio ($OR$).
2. Using the Delta method and Woolf's method, compute the standard errors on the logarithmic scale and construct the 95% confidence intervals for both the Risk Ratio and the Odds Ratio.
3. Calculate the Risk Difference ($RD$), the Attributable Fraction in the Exposed ($AF_e$), the Population Attributable Risk ($PAR$), and the Population Attributable Fraction ($PAF$) using both Levin’s and Miettinen’s formulas.

### Solution, step 1: Construct contingency table and evaluate point estimates
From the study data:
- Exposed diseased: $a = 240$, exposed non-diseased: $b = 3000 - 240 = 2760$. Total exposed: $n_1 = 3000$.
- Unexposed diseased: $c = 210$, unexposed non-diseased: $d = 7000 - 210 = 6790$. Total unexposed: $n_0 = 7000$.
- Total diseased: $m_1 = 240 + 210 = 450$. Total non-diseased: $m_0 = 2760 + 6790 = 9550$. Total cohort: $N = 10000$.

Now evaluate the 10-year cumulative incidence risks:
$$R_1 = \frac{a}{n_1} = \frac{240}{3000} = 0.0800 \quad (8.00\%)$$
$$R_0 = \frac{c}{n_0} = \frac{210}{7000} = 0.0300 \quad (3.00\%)$$

The Risk Ratio is:
$$\widehat{RR} = \frac{R_1}{R_0} = \frac{0.0800}{0.0300} = 2.6667 \approx 2.67$$

Physically inactive individuals experience $2.67$ times the risk of developing coronary heart disease compared to physically active individuals.

The Odds Ratio is:
$$\widehat{OR} = \frac{a \cdot d}{b \cdot c} = \frac{240 \times 6790}{2760 \times 210} = \frac{1,629,600}{579,600} \approx 2.8116 \approx 2.81$$

Notice that because the baseline risk is low ($3\%$ to $8\%$), the Odds Ratio ($2.81$) is moderately close to the Risk Ratio ($2.67$), though slightly higher due to the mathematical properties of odds.

### Solution, step 2: Logarithmic standard errors and 95% confidence intervals
1. **Confidence Interval for the Risk Ratio**:
   $$\text{SE}(\ln \widehat{RR}) = \sqrt{\frac{1}{a} - \frac{1}{n_1} + \frac{1}{c} - \frac{1}{n_0}} = \sqrt{\frac{1}{240} - \frac{1}{3000} + \frac{1}{210} - \frac{1}{7000}}$$
   $$= \sqrt{0.0041667 - 0.0003333 + 0.0047619 - 0.0001429} = \sqrt{0.0084524} \approx 0.091937$$

   Evaluate the 95% log-limits:
   $$\ln(2.6667) = 0.98083$$
   $$\text{Log Limits} = 0.98083 \pm 1.96(0.091937) = 0.98083 \pm 0.18020 = [0.80063, \, 1.16103]$$

   Exponentiating:
   $$RR_{\text{lower}} = \exp(0.80063) \approx 2.227, \qquad RR_{\text{upper}} = \exp(1.16103) \approx 3.193$$
   $$CI_{0.95}(RR) = [2.23, \, 3.19]$$

2. **Confidence Interval for the Odds Ratio via Woolf's Method**:
   $$\text{SE}(\ln \widehat{OR}) = \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d}} = \sqrt{\frac{1}{240} + \frac{1}{2760} + \frac{1}{210} + \frac{1}{6790}}$$
   $$= \sqrt{0.0041667 + 0.0003623 + 0.0047619 + 0.0001473} = \sqrt{0.0094382} \approx 0.097150$$

   Evaluate log-limits:
   $$\ln(2.8116) = 1.03375$$
   $$\text{Log Limits} = 1.03375 \pm 1.96(0.097150) = 1.03375 \pm 0.19041 = [0.84334, \, 1.22416]$$

   Exponentiating:
   $$OR_{\text{lower}} = \exp(0.84334) \approx 2.324, \qquad OR_{\text{upper}} = \exp(1.22416) \approx 3.401$$
   $$CI_{0.95}(OR) = [2.32, \, 3.40]$$

Both intervals completely exclude the null value $1.0$, confirming a statistically significant elevated risk at the $\alpha = 0.05$ level.

### Solution, step 3: Absolute impact measures: RD, AF_e, PAR, and PAF
1. **Risk Difference (Attributable Risk)**:
   $$\widehat{RD} = R_1 - R_0 = 0.0800 - 0.0300 = 0.0500 \quad (5.00\%)$$
   Every 100 physically inactive individuals experience an excess of $5$ heart disease cases over 10 years directly attributable to inactivity.

2. **Attributable Fraction in the Exposed**:
   $$\widehat{AF}_e = \frac{R_1 - R_0}{R_1} = \frac{0.0500}{0.0800} = 0.6250 \quad (62.50\%)$$
   Alternatively, using the Risk Ratio:
   $$\widehat{AF}_e = \frac{RR - 1}{RR} = \frac{2.6667 - 1}{2.6667} = \frac{1.6667}{2.6667} = 0.6250 \quad (62.50\%)$$
   Among inactive people, $62.5\%$ of all coronary heart disease cases are attributable to physical inactivity.

3. **Population Attributable Risk (PAR)**:
   The total population risk is $R_{\text{total}} = 450 / 10000 = 0.0450$ ($4.50\%$).
   $$\widehat{PAR} = R_{\text{total}} - R_0 = 0.0450 - 0.0300 = 0.0150 \quad (1.50\%)$$
   In the general population, $15$ cases per 1,000 individuals over 10 years are attributable to inactivity.

4. **Population Attributable Fraction (PAF)**:
   Direct definition:
   $$\widehat{PAF} = \frac{PAR}{R_{\text{total}}} = \frac{0.0150}{0.0450} = 0.3333 \quad (33.33\%)$$

   Levin's Formula ($p_e = 3000 / 10000 = 0.30$):
   $$PAF = \frac{p_e (RR - 1)}{p_e (RR - 1) + 1} = \frac{0.30(2.6667 - 1)}{0.30(2.6667 - 1) + 1} = \frac{0.30(1.6667)}{0.30(1.6667) + 1} = \frac{0.50}{1.50} = 0.3333 \quad (33.33\%)$$

   Miettinen's Formula ($p_{e \mid D} = a / m_1 = 240 / 450 \approx 0.53333$):
   $$PAF = p_{e \mid D} \left( \frac{RR - 1}{RR} \right) = 0.53333 \times 0.6250 = 0.3333 \quad (33.33\%)$$

Completely eradicating physical inactivity from this population would prevent exactly one-third ($33.33\%$) of all coronary heart disease cases occurring over the decade!

## Fully worked question 2: Retrospective Case-Control Design & Rare Disease Validity

### Question
To study the etiologic link between exposure to occupational benzene solvents and acute myeloid leukemia (AML), an environmental health team executes a retrospective matched hospital-based case-control study:
- $m_1 = 150$ newly diagnosed, histologically confirmed AML cases are recruited.
- $m_0 = 450$ age- and sex-matched hospital controls admitted for acute orthopedic trauma are recruited.
- Systematic occupational exposure history reveals that $a = 45$ of the AML cases had substantial benzene exposure, whereas $b = 45$ of the controls had substantial benzene exposure.

1. Display the $2 \times 2$ table, determine the exposure odds among cases and controls, and calculate the sample Odds Ratio ($\widehat{OR}$).
2. Demonstrate why the Risk Ratio cannot be legitimately calculated directly from these sample proportions. If external cancer registry data indicates that the true cumulative incidence of AML over working lifetimes in unexposed workers is $R_0 = 0.002$ ($0.2\%$), compute the true Risk Ratio implied by the estimated Odds Ratio.
3. Compute the 95% confidence interval for the Odds Ratio using Woolf’s logit method and test the null hypothesis $H_0: OR = 1$ via the Pearson chi-square test with continuity correction.

### Solution, step 1: 2x2 table and retrospective odds ratio calculation
The $2 \times 2$ retrospective table is:
- Cases ($D^+$): Exposed $a = 45$, Unexposed $c = 150 - 45 = 105$. Total cases $m_1 = 150$.
- Controls ($D^-$): Exposed $b = 45$, Unexposed $d = 450 - 45 = 405$. Total controls $m_0 = 450$.

Evaluate exposure odds:
$$\text{Exposure Odds}_{\text{cases}} = \frac{a}{c} = \frac{45}{105} \approx 0.42857$$
$$\text{Exposure Odds}_{\text{controls}} = \frac{b}{d} = \frac{45}{405} \approx 0.11111$$

The sample Odds Ratio is:
$$\widehat{OR} = \frac{\text{Exposure Odds}_{\text{cases}}}{\text{Exposure Odds}_{\text{controls}}} = \frac{45 / 105}{45 / 405} = \frac{405}{105} = \frac{27}{7} \approx 3.8571 \approx 3.86$$

Workers diagnosed with acute myeloid leukemia have $3.86$ times the odds of having been exposed to benzene compared to control patients.

### Solution, step 2: Illegitimacy of naive relative risk and calculation under rare disease model
If an untrained analyst naively computed a "cohort risk ratio" from this table:
$$\text{"Risk"}_1 = \frac{a}{a + b} = \frac{45}{45 + 45} = 0.50, \quad \text{"Risk"}_0 = \frac{c}{c + d} = \frac{105}{105 + 405} = \frac{105}{510} \approx 0.2059$$
$$\text{"Naive RR"} = \frac{0.50}{0.2059} \approx 2.43$$

This calculation is completely invalid because the denominator $a + b = 90$ is an artifact of the investigator recruiting $3$ controls per case ($450 / 150 = 3$). If the investigator had instead chosen $1$ control per case, or $10$ controls per case, the "naive RR" would shift arbitrarily.

However, using the external registry baseline risk $R_0 = 0.002$ ($0.2\%$), we can reconstruct the true implied risk $R_1$:
$$\text{Odds}_0 = \frac{R_0}{1 - R_0} = \frac{0.002}{0.998} \approx 0.002004$$
$$\text{Odds}_1 = OR \times \text{Odds}_0 \approx 3.8571 \times 0.002004 \approx 0.0077296$$
$$R_1 = \frac{\text{Odds}_1}{1 + \text{Odds}_1} = \frac{0.0077296}{1.0077296} \approx 0.007670$$

The true Risk Ratio in the population is:
$$RR = \frac{R_1}{R_0} = \frac{0.007670}{0.002000} \approx 3.835 \approx 3.84$$

Notice how exceptionally close the sample Odds Ratio ($3.86$) is to the true Risk Ratio ($3.84$)! Because acute myeloid leukemia is biologically rare ($0.2\%$), the rare disease assumption holds with remarkable precision.

### Solution, step 3: Woolf's confidence interval and Yates-corrected chi-square test
1. **Woolf's 95% Confidence Interval**:
   $$\text{SE}(\ln \widehat{OR}) = \sqrt{\frac{1}{45} + \frac{1}{45} + \frac{1}{105} + \frac{1}{405}} = \sqrt{0.02222 + 0.02222 + 0.00952 + 0.00247} = \sqrt{0.05643} \approx 0.23755$$
   $$\ln(3.8571) = 1.34992$$
   $$\text{Log Limits} = 1.34992 \pm 1.96(0.23755) = 1.34992 \pm 0.46560 = [0.88432, \, 1.81552]$$
   $$OR_{\text{lower}} = \exp(0.88432) \approx 2.421, \qquad OR_{\text{upper}} = \exp(1.81552) \approx 6.144$$
   $$CI_{0.95}(OR) = [2.42, \, 6.14]$$

2. **Yates-Corrected Pearson Chi-Square Test**:
   $$\chi^2_{\text{Yates}} = \frac{N \left( |a d - b c| - N/2 \right)^2}{m_1 m_0 n_1 n_0}$$
   Here $N = 600$, $a d = 45 \times 405 = 18,225$, $b c = 45 \times 105 = 4,725$, $a d - b c = 13,500$.
   $$|13,500| - 300 = 13,200$$
   $$\chi^2_{\text{Yates}} = \frac{600 \times (13,200)^2}{(150)(450)(90)(510)} = \frac{600 \times 174,240,000}{3,098,250,000} = \frac{104,544,000,000}{3,098,250,000} \approx 33.74$$

With $1$ degree of freedom, the critical value at $\alpha = 0.001$ is $\chi^2_{0.001, 1} = 10.83$. Since $\chi^2_{\text{Yates}} = 33.74 \gg 10.83$ ($p < 10^{-8}$), we overwhelmingly reject the null hypothesis of no association.

## Fully worked question 3: Clinical Trial Risk Reductions, NNT & NNH Benefit-Harm Tradeoffs

### Question
A multi-center randomized controlled trial evaluates a potent antiplatelet drug (Ticagrelor) versus standard Aspirin monotherapy in $N = 10,000$ acute coronary syndrome patients followed for 1 year. The study is powered to evaluate both ischemic efficacy and bleeding toxicity:
- **Efficacy Endpoint (Major Adverse Cardiac Events, MACE)**:
  - Ticagrelor group ($n_1 = 5,000$): 400 patients experience MACE.
  - Aspirin group ($n_0 = 5,000$): 550 patients experience MACE.
- **Safety Endpoint (Major Gastrointestinal Hemorrhage)**:
  - Ticagrelor group ($n_1 = 5,000$): 150 patients suffer major hemorrhage.
  - Aspirin group ($n_0 = 5,000$): 100 patients suffer major hemorrhage.

1. For the efficacy endpoint, calculate the cumulative event risks ($R_1, R_0$), the Relative Risk ($RR$), the Relative Risk Reduction ($RRR$), the Absolute Risk Reduction ($ARR$), and the Number Needed to Treat ($NNT$).
2. For the safety endpoint, calculate the event risks, Absolute Risk Increase ($ARI$), Relative Risk of harm, and the Number Needed to Harm ($NNH$).
3. In a clinical population of $50,000$ acute coronary syndrome patients treated for 1 year with Ticagrelor instead of Aspirin, estimate the net balance of clinical events: how many cardiac events are prevented, how many major bleeding events are induced, and what is the benefit-harm ratio?

### Solution, step 1: Efficacy endpoint: RRR, ARR, and NNT
1. **Risks of MACE**:
   $$R_{1, \text{mace}} = \frac{400}{5000} = 0.0800 \quad (8.00\%)$$
   $$R_{0, \text{mace}} = \frac{550}{5000} = 0.1100 \quad (11.00\%)$$

2. **Relative Risk and Relative Risk Reduction**:
   $$RR_{\text{mace}} = \frac{R_{1, \text{mace}}}{R_{0, \text{mace}}} = \frac{0.0800}{0.1100} \approx 0.7273$$
   $$RRR = 1 - RR = 1 - 0.7273 = 0.2727 \quad (27.27\%)$$
   Ticagrelor reduces the relative risk of MACE by $27.27\%$.

3. **Absolute Risk Reduction and NNT**:
   $$ARR = R_{0, \text{mace}} - R_{1, \text{mace}} = 0.1100 - 0.0800 = 0.0300 \quad (3.00\%)$$
   $$NNT = \frac{1}{ARR} = \frac{1}{0.0300} = 33.33 \approx 34 \text{ patients}$$
   Treating approximately 34 patients for 1 year with Ticagrelor prevents exactly 1 major adverse cardiac event.

### Solution, step 2: Safety endpoint: ARI, relative risk of harm, and NNH
1. **Risks of Major Hemorrhage**:
   $$R_{1, \text{bleed}} = \frac{150}{5000} = 0.0300 \quad (3.00\%)$$
   $$R_{0, \text{bleed}} = \frac{100}{5000} = 0.0200 \quad (2.00\%)$$

2. **Relative Risk of Harm**:
   $$RR_{\text{harm}} = \frac{R_{1, \text{bleed}}}{R_{0, \text{bleed}}} = \frac{0.0300}{0.0200} = 1.5000$$
   Ticagrelor increases the relative risk of major bleeding by $50\%$.

3. **Absolute Risk Increase and NNH**:
   $$ARI = R_{1, \text{bleed}} - R_{0, \text{bleed}} = 0.0300 - 0.0200 = 0.0100 \quad (1.00\%)$$
   $$NNH = \frac{1}{ARI} = \frac{1}{0.0100} = 100 \text{ patients}$$
   For every 100 patients treated with Ticagrelor, exactly 1 additional patient suffers a major bleeding event.

### Solution, step 3: Net clinical benefit in 50,000 patients
For a treated cohort of $N_{\text{pop}} = 50,000$ patients over 1 year:
1. **Cardiac Events Prevented**:
   $$\text{MACE Prevented} = N_{\text{pop}} \times ARR = 50,000 \times 0.0300 = 1,500 \text{ cardiac events prevented}$$
   (Equivalently: $50,000 / NNT = 50,000 / 33.33 = 1,500$).

2. **Excess Bleeding Events Induced**:
   $$\text{Bleeds Induced} = N_{\text{pop}} \times ARI = 50,000 \times 0.0100 = 500 \text{ excess major bleeds}$$
   (Equivalently: $50,000 / NNH = 50,000 / 100 = 500$).

3. **Net Clinical Balance and Benefit-Harm Ratio**:
   $$\text{Benefit-Harm Ratio} = \frac{\text{Events Prevented}}{\text{Events Induced}} = \frac{1,500}{500} = 3.00$$
   For every major bleeding event caused by Ticagrelor, exactly 3 major cardiovascular ischemic events (fatal myocardial infarctions or strokes) are prevented. Because the mortality hazard of MACE typically exceeds that of non-fatal gastrointestinal hemorrhage, the clinical evidence demonstrates a favorable net benefit profile.
"""

(OUT_DIR / "unit-2.md").write_text(unit2.strip() + "\n", encoding="utf-8")
print("Unit 2 updated.")
