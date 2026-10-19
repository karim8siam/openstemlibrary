# Unit 1: Sources, Evaluation & Quality of Demographic Data

Demography is the quantitative science of human populations, investigating their size, geographical distribution, age-sex composition, and the dynamic temporal processes of fertility, mortality, nuptiality, and migration that govern their structural evolution. The foundational integrity of demographic analysis depends critically upon the quality, precision, completeness, and reliability of the underlying empirical data systems. Because public policy, macro-social planning, epidemiological surveillance, economic resource allocation, and parliamentary representation depend fundamentally on demographic counts, quantifying errors in demographic data is of paramount importance in mathematical statistics.

## 1.1 Primary Demographic Data Systems: Censuses, Vital Registration, and Sample Surveys

Demographic information originates from three primary operational data collection systems, each exhibiting distinctive operational characteristics, temporal cadences, institutional frameworks, and susceptibility to observational errors.

### The Decennial Population Census
The population census represents the total enumeration of an entire national territory at a specified point in temporal reference. By international standards defined by the United Nations Statistics Division, a modern census possesses four essential cardinal criteria:
1. **Individual Enumeration**: Each individual inhabitant is separately enumerated and their demographic, social, and economic attributes are individually recorded, rather than aggregated at the household head level.
2. **Universality within a Defined Territory**: The enumeration covers every person present or residing within the geographic boundaries of the state without omission or duplication.
3. **Simultaneity**: The data refer strictly to a well-defined single reference instant, typically midnight of the designated census night.
4. **Defined Periodicity**: Censuses are conducted at regular intervals, usually decennially (every ten years), to establish comparable secular longitudinal series.

Demographic censuses employ two distinct enumeration conventions:
- **De Facto Enumeration**: Persons are enumerated strictly at the physical location where they spent census night, regardless of their habitual or permanent residence. While de facto counts simplify field verification and avoid subjective interpretations of residence, they introduce artificial distortions in areas with transient tourist, commuting, or seasonal worker populations.
- **De Jure Enumeration**: Persons are enumerated at their legal or usual place of residence, regardless of where they were physically situated on census night. De jure enumeration provides a more stable baseline for long-term regional planning and fiscal distribution, but it complicates fieldwork through proxy reporting and creates severe hazards of omission or duplicate counting of individuals with multiple residences.

### The Civil Registration and Vital Statistics (CRVS) System
While a census provides a static snapshot of population stocks at discrete decennial moments, the Civil Registration and Vital Statistics (CRVS) system provides a continuous, dynamic, and legal recording of vital events as they occur. Vital events encompass live births, deaths, fetal deaths, marriages, divorces, annulments, and legal adoptions.

In a fully developed CRVS system, vital registration is universal, compulsory, and statutory. The continuous recording of births $B(t)$ and deaths $D(t)$ over calendar interval $[t_1, t_2]$ allows the continuous tracking of natural increase $B(t) - D(t)$ without awaiting the next decennial census. However, in many developing economies and transitional territories, CRVS systems suffer from substantial under-registration, late registration, and geographic coverage gaps, necessitating indirect demographic estimation techniques.

### Specialized Demographic Sample Surveys
Demographic sample surveys (such as the Demographic and Health Surveys [DHS], Multiple Indicator Cluster Surveys [MICS], and national labor force surveys) complement censuses and vital registration by collecting intensive, high-resolution micro-data on a representative probability sample of households. Unlike nationwide censuses, sample surveys can administer extensive retrospective questionnaires covering complete birth histories, contraceptive practices, infant morbidity, maternal mortality, and internal migration patterns. While subject to sampling variability, well-designed probability surveys benefit from highly trained interviewers, rigorous supervision, and sophisticated non-sampling quality control mechanisms.

## 1.2 Taxonomy of Demographic Errors: Coverage and Content Errors

Errors in demographic data are rigorously classified into two overarching conceptual categories: coverage errors and content errors.

### Coverage Errors
Coverage errors occur when individuals or households are entirely omitted from enumeration, erroneously enumerated multiple times, or improperly included in the target population universe:
- **Under-enumeration (Omissions)**: The failure to count eligible persons. Omissions are systematically concentrated among marginalized populations, highly mobile urban youth, unhoused individuals, infants under age one (who are frequently overlooked by household respondents who do not perceive neonates as full family members), and remote rural communities.
- **Over-enumeration (Duplications and Fabrications)**: The duplicate counting of individuals (for example, college students enumerated both at university dormitories and at their parents' residences) or the fraudulent entry of fictitious persons by enumerators seeking to inflate performance metrics.
- **Gross vs Net Coverage Error**: Let $N_{\text{true}}$ denote the true population size, $N_{\text{enum}}$ the enumerated population count, $O$ the total number of omitted persons, and $D$ the total number of duplicated or erroneously included persons. Then the enumerated count is related to the true count by:

$$N_{\text{enum}} = N_{\text{true}} - O + D$$

The **Net Coverage Error** is defined as $E_{\text{net}} = N_{\text{enum}} - N_{\text{true}} = D - O$. The net coverage rate is:

$$r_{\text{net}} = \frac{N_{\text{enum}} - N_{\text{true}}}{N_{\text{true}}} = \frac{D - O}{N_{\text{true}}}$$

If $O > D$, the census exhibits net under-coverage ($r_{\text{net}} < 0$).

### Content Errors
Content errors occur when an individual is successfully enumerated, but the characteristics recorded on the questionnaire (such as age, sex, marital status, educational attainment, or relationship to household head) are inaccurate or misclassified. Content errors stem from respondent ignorance, recall decay in retrospective reporting, proxy respondent inaccuracies, enumerator bias, or cultural superstitions surrounding particular numerical values.

## 1.3 Post-Enumeration Surveys and Dual-System Estimation (Capture-Recapture)

The gold standard for evaluating census coverage error is the **Post-Enumeration Survey (PES)**, coupled mathematically with the **Dual-System Estimation (DSE)** methodology, also known in ecological statistics as the Lincoln-Petersen capture-recapture estimator.

### The Chandrasekaran–Deming Dual-System Model
Let the entire population of an enumerated area be cross-classified into a $2 \times 2$ contingency table representing capture status across two independent enumeration systems: the original Census (System 1) and an independent Post-Enumeration Survey (System 2):

| System 1 (Census) | In System 2 (PES: Yes) | Out of System 2 (PES: No) | Total System 1 |
| :--- | :--- | :--- | :--- |
| **In Census (Yes)** | $N_{11}$ (Matched Cases) | $N_{12}$ (Census Only) | $N_{1+} = N_{\text{census}}$ |
| **Out of Census (No)** | $N_{21}$ (PES Only) | $N_{22}$ (Missed by Both) | $N_{2+}$ |
| **Total System 2** | $N_{+1} = N_{\text{pes}}$ | $N_{+2}$ | $N_{\text{true}}$ |

In the table above:
- $N_{11}$ denotes individuals enumerated in both the census and the PES (identified via rigorous one-to-one record linkage).
- $N_{12}$ denotes individuals counted in the census but omitted from the PES.
- $N_{21}$ denotes individuals caught in the PES who were omitted from the census.
- $N_{22}$ denotes the unobservable latent count of individuals omitted by both systems.

### Mathematical Derivation of the Dual-System Estimator
Assume the following fundamental regularity conditions:
1. **Statistical Independence**: The probability that an individual is enumerated in the census is statistically independent of whether that individual is enumerated in the PES:

$$\mathbb{P}(\text{Census} \cap \text{PES}) = \mathbb{P}(\text{Census}) \cdot \mathbb{P}(\text{PES})$$

2. **Closure**: The population is closed between the census date and the PES date (or adjusted for vital events and migration).
3. **No Erroneous Enumerations in $N_{1+}$**: The census count $N_{1+}$ has been corrected for duplicate and fictitious records.
4. **Perfect Matching**: There are no false matches or false non-matches in record linkage.

Under statistical independence, the cell probabilities satisfy:

$$p_{11} = p_{1+} \cdot p_{+1}$$

In terms of expected cell counts:

$$\frac{\mathbb{E}[N_{11}]}{N_{\text{true}}} = \left( \frac{\mathbb{E}[N_{1+}]}{N_{\text{true}}} \right) \cdot \left( \frac{\mathbb{E}[N_{+1}]}{N_{\text{true}}} \right)$$

Rearranging this identity yields the celebrated **Chandrasekaran–Deming Estimator** for the true total population:

$$\hat{N}_{\text{DSE}} = \frac{N_{1+} \cdot N_{+1}}{N_{11}} = \frac{N_{\text{census}} \cdot N_{\text{pes}}}{N_{11}}$$

The unobserved population missed by both systems is estimated as:

$$\hat{N}_{22} = \frac{N_{12} \cdot N_{21}}{N_{11}}$$

The estimated net undercount rate of the census is:

$$\hat{U} = \frac{\hat{N}_{\text{DSE}} - N_{\text{census}}}{\hat{N}_{\text{DSE}}} = 1 - \frac{N_{11}}{N_{\text{pes}}}$$

Notice that $\frac{N_{11}}{N_{\text{pes}}}$ represents the empirical coverage rate of the census among the sample of individuals independently verified in the PES.

## 1.4 Age Reporting Errors: Heaping, Digit Preference, and Distortion Mechanisms

Among all content variables collected in demographic inquiries, age is universally the most critical, because mortality, fertility, economic productivity, and nuptiality vary dramatically across the life course. Unfortunately, age is also extraordinarily prone to systematic reporting errors.

Age errors manifest through two distinct behavioral mechanisms:
1. **Age Heaping (Digit Preference)**: The tendency of respondents or enumerators to report chronological ages ending in specific favorite terminal digits—most prominently digits ending in '0' and '5', and to a lesser extent even digits ('2', '4', '6', '8')—while avoiding terminal odd digits ('1', '3', '7', '9'). In South Asian and Middle Eastern demographic datasets, severe age heaping is observed at terminal digits 0 and 5 due to low literacy and rounding heuristics.
2. **Age Shifting (Systematic Bias)**: The deliberate or unconscious distortion of age in a specific directional orientation. Classical examples include:
   - Young men understating or overstating their age to avoid or qualify for compulsory military conscription.
   - Young adolescent girls being reported as older (over age 15 or 18) to disguise illegal child marriages, or reported as younger to preserve marriageability.
   - Elderly individuals systematically exaggerating their attained age beyond 80, 90, or 100 years (centenarian exaggeration) due to the social prestige and veneration accorded to extreme longevity.

To quantify digit preference rigorously, mathematical demographers formulate diagnostic summary indices.

## 1.5 Whipple's Index: Formulation, Mathematical Boundaries, and Demographic Interpretation

Whipple's Index is the classic demographic metric designed specifically to measure digit preference for ages ending in 0 and 5 within the adult lifespan.

### Mathematical Formulation of Whipple's Index
Because childhood ages under 20 are distorted by school enrollment documentation, and ages 65 and above are distorted by mortality selection and age exaggeration, Whipple's Index restricts its evaluation window to the age span from 23 to 62 years inclusive (a 40-year interval containing exactly four complete decades).

Let $P_x$ denote the enumerated population at single year of age $x$. Whipple's Index $W$ is defined as the percentage ratio of the population reporting ages ending in 0 and 5 to one-fifth of the total population in the age range $[23, 62]$:

$$W = \frac{\sum_{k=5}^{12} P_{5k}}{\frac{1}{5} \sum_{x=23}^{62} P_x} \times 100 = \frac{5 \cdot \sum_{k=5}^{12} P_{5k}}{\sum_{x=23}^{62} P_x} \times 100$$

The numerator sums the population reporting ages 25, 30, 35, 40, 45, 50, 55, and 60 (eight terminal 0 and 5 cohorts). The denominator contains the total population across all 40 single-year ages from 23 through 62.

### Theoretical Bounds of Whipple's Index
1. **Zero Heaping (Perfect Uniformity)**: If there is no digit preference and the population is smoothly and uniformly distributed across single years of age within each five-year band, then exactly one-fifth ($20\%$) of the population in the age span $[23, 62]$ will report terminal digits 0 and 5. Under this ideal condition:
   $$W = \frac{5 \cdot (0.20 \cdot \sum P_x)}{\sum P_x} \times 100 = 100$$
2. **Complete Avoidance of Digits 0 and 5**: If no individuals report ages ending in 0 or 5 (absolute repulsion):
   $$W = 0$$
3. **Absolute Total Heaping**: If every single person within the age span $[23, 62]$ reports an age ending in 0 or 5, so that the numerator equals the total population $\sum_{x=23}^{62} P_x$:
   $$W = \frac{5 \cdot \sum P_x}{\sum P_x} \times 100 = 500$$

Thus, Whipple's Index varies over the mathematical range $[0, 500]$.

### United Nations Standard Quality Scale for Whipple's Index
The United Nations Department of Economic and Social Affairs classifies data quality according to the following thresholds:
- $W < 105$: Highly accurate demographic data (virtually no digit preference).
- $105 \le W < 110$: Fairly accurate data.
- $110 \le W < 125$: Approximate data (moderate digit preference).
- $125 \le W < 175$: Rough data (substantial age heaping).
- $W \ge 175$: Very rough data (severe, pervasive digit preference).

In historical censuses of developing regions, values of $W > 250$ or $300$ were frequently observed, indicating that more than half of all adult respondents rounded their age to the nearest 0 or 5.

## 1.6 Myers' Blended Index: Theoretical Foundations and Non-Parametric Blending

While Whipple's Index tests exclusively for attraction to digits 0 and 5, it cannot determine whether digit 0 is preferred over digit 5, nor can it detect digit preference for other terminal digits (such as digit 2 or 8). In 1940, Robert J. Myers formulated the **Myers' Blended Index**, which provides an unbiased test of digit preference for all ten terminal digits $0, 1, 2, \dots, 9$.

### The Problem of Mortality Bias in Unblended Digit Sums
If one simply sums the enumerated population across all ages ending in digit $d \in \{0, 1, \dots, 9\}$:

$$S_d = \sum_{k} P_{10k + d}$$

the sum $S_0$ (corresponding to ages $10, 20, 30, \dots$) will naturally exceed $S_9$ (corresponding to ages $19, 29, 39, \dots$), even in the complete absence of digit preference! This occurs because biological mortality reduces population sizes continuously as age advances: each cohort is smaller than the preceding cohort. Consequently, lower terminal digits will always systematically outnumber higher terminal digits due to the universal negative slope of the population age pyramid.

### Myers' Blending Algorithm
To neutralize this confounding mortality gradient, Myers developed an ingenious weighting scheme known as **blended populations**.

Myers selects an age span spanning several decades, typically age 10 to age 89 (an 80-year span consisting of 8 complete cycles of 10 digits).
1. Compute the unweighted sums of populations ending in digit $d$ beginning at age 10:
   $$U_d = \sum_{k=1}^7 P_{10k + d} = P_{10+d} + P_{20+d} + \dots + P_{70+d}$$
2. Compute the unweighted sums of populations ending in digit $d$ beginning at age 20:
   $$V_d = \sum_{k=2}^8 P_{10k + d} = P_{20+d} + P_{30+d} + \dots + P_{80+d}$$
3. Define the **Blended Population** $B_d$ for terminal digit $d$ by applying linear counter-balancing weights:
   $$B_d = (d + 1) \cdot U_d + (9 - d) \cdot V_d \quad \text{for } d = 0, 1, 2, \dots, 9$$

Notice how the weights operate:
- For $d = 0$: $B_0 = 1 \cdot U_0 + 9 \cdot V_0$
- For $d = 1$: $B_1 = 2 \cdot U_1 + 8 \cdot V_1$
- $\dots$
- For $d = 9$: $B_9 = 10 \cdot U_9 + 0 \cdot V_9$

By scaling $U_d$ by $(d + 1)$ and $V_d$ by $(9 - d)$, each single year of age in the overlapping range $[20, 79]$ receives exactly $(d + 1) + (9 - d) = 10$ units of total weight! The differential linear weighting on the boundary decades exactly neutralizes the mortality slope.

### Calculation of Myers' Summary Index
In the absence of digit preference, the blended population for each of the ten digits should account for exactly $10\%$ of the total blended population $B_{\text{total}} = \sum_{d=0}^9 B_d$.
1. Compute the percentage proportion of the blended population for each digit:
   $$p_d = \frac{B_d}{B_{\text{total}}} \times 100$$
2. Compute the absolute deviation of each digit's proportion from the theoretical $10.0\%$ baseline:
   $$\Delta_d = |p_d - 10.0|$$
3. **Myers' Blended Index** $M$ is defined as one-half the sum of these absolute deviations:

$$M = \frac{1}{2} \sum_{d=0}^9 |p_d - 10.0|$$

### Theoretical Interpretation of Myers' Index
- The theoretical minimum of $M$ is $0.0$, representing complete uniformity across all ten digits.
- The theoretical maximum of $M$ is $90.0$, representing total concentration where $100\%$ of the entire population reports ages ending in a single solitary terminal digit (such as 0), so that $|100 - 10| + 9 \cdot |0 - 10| = 90 + 90 = 180$, and $\frac{1}{2}(180) = 90$.
- A Myers' index below 10 indicates reliable age data; values between 10 and 20 indicate moderate distortion; values exceeding 20 indicate severe age misreporting.

## 1.7 Bachi's Index and the United Nations Age-Sex Accuracy Index

In addition to Whipple and Myers, demographers deploy Bachi's Index and the United Nations Age-Sex Accuracy Index to evaluate multi-dimensional reporting fidelity.

### Bachi's Index
Developed by Roberto Bachi in 1951, Bachi's Index applies a slightly different weighting methodology to achieve the same objective as Myers. Bachi computes the theoretical expected population at each terminal digit $d$ by fitting a moving average across five adjacent years centered at each age, and then computes the mean absolute percentage excess or deficit across all ages from 30 to 79. Like Myers' index, Bachi's index has a theoretical range from 0 to 90.

### The United Nations Age-Sex Accuracy Index (UN Joint Score)
While Whipple and Myers evaluate single-year age data, many demographic tables are published only in conventional **five-year age groups** ($0-4, 5-9, 10-14, \dots$). Age heaping at digits 0 and 5 does not disappear when data are grouped into five-year categories; instead, it causes alternating surpluses and deficits between adjacent five-year age intervals.

The United Nations formulated the **Age-Sex Accuracy Index** (also known as the **UN Joint Score**), which evaluates five-year age data using three component sub-indices:

1. **Sex Ratio Score (SRS)**: The sex ratio in five-year age group $x$ to $x+4$ is defined as $SR_x = \frac{M_x}{F_x} \times 100$, where $M_x$ and $F_x$ are enumerated males and females. The Sex Ratio Score is the mean absolute successive difference between adjacent age-specific sex ratios across all ages from age 0 to 70:
   $$SRS = \frac{1}{K} \sum_{x} |SR_{x+5} - SR_x|$$
   In an error-free population without extreme sex-selective migration or wartime mortality, sex ratios decline smoothly and gradually with age due to higher male mortality. Sudden fluctuations between adjacent five-year groups reflect sex-differential age misreporting.

2. **Male Age Ratio Score (ARS_M)**: The age ratio for males in age group $x$ is defined as the ratio of the population in that age group to the arithmetic mean of the preceding and succeeding five-year groups:
   $$AR_x^M = \frac{M_x}{\frac{1}{2}(M_{x-5} + M_{x+5})} \times 100$$
   The deviation from $100$ is $|AR_x^M - 100|$. The Male Age Ratio Score is the average absolute deviation across all evaluated age groups:
   $$ARS_M = \frac{1}{K} \sum_x |AR_x^M - 100|$$

3. **Female Age Ratio Score (ARS_F)**: Defined identically for females:
   $$ARS_F = \frac{1}{K} \sum_x |AR_x^F - 100|$$

### The UN Joint Score Formula:
Based on empirical calibrations across hundreds of national censuses, the United Nations established the composite **Joint Score (JS)**:

$$JS = 3 \cdot SRS + ARS_M + ARS_F$$

The factor of 3 reflects the mathematical sensitivity of the sex ratio to differential coverage and age shifting between sexes.
- **UN Quality Categories**:
  - $JS < 20$: Accurate data.
  - $20 \le JS < 40$: Inaccurate data.
  - $JS \ge 40$: Highly inaccurate data.

## 1.8 Mathematical Graduation and Smoothing of Distorted Age Distributions

When demographic analyses or life table constructions require reliable single-year or five-year age baselines, demographers must mathematically correct for age heaping through **graduation** (smoothing).

### The Carrier–Farrag Split Formula
The Carrier-Farrag method (1959) is an algebraic technique for splitting enumerated ten-year age groups into two constituent five-year age groups without altering the ten-year totals.
Let $T_1, T_2, T_3$ be three successive ten-year population totals centered on $T_2$ (for example, ages 20–29, 30–39, 40–49). Let $T_2$ be composed of two five-year groups $F_1$ (ages 30–34) and $F_2$ (ages 35–39), such that $T_2 = F_1 + F_2$.

Assuming a quadratic or geometric progression of cohort decay across the three decades, Carrier and Farrag proved that the first five-year component can be graduated via the formula:

$$F_1 = T_2 \cdot \left[ \frac{1}{2} + \frac{1}{16} \left( \frac{T_1 - T_3}{T_2} \right) \right]$$

and the second component is obtained by subtraction:

$$F_2 = T_2 - F_1 = T_2 \cdot \left[ \frac{1}{2} - \frac{1}{16} \left( \frac{T_1 - T_3}{T_2} \right) \right]$$

This graduation formula preserves the ten-year empirical total $T_2$ exactly while removing digit heaping that artificially inflates the group containing terminal digit 0 relative to terminal digit 5.

### Sprague's Fifth-Difference Osculatory Interpolation Formula
For single-year graduation from five-year age data, demographers utilize Sprague's osculatory interpolation formulas. Sprague's coefficients represent a fifth-degree polynomial that matches both the empirical five-year totals and enforces continuity of the first and second derivatives at the boundaries between adjacent age groups, preventing artificial serration in graduated single-year survival schedules.


### Algebraic Derivation of the Carrier–Farrag Graduation Coefficients
To understand the mathematical foundation of the Carrier–Farrag splitting formula, consider three consecutive ten-year age cohorts $T_1, T_2, T_3$. Let $x$ denote the continuous age variable measured from the midpoint of $T_2$. Suppose that the true underlying demographic distribution of the population across the thirty-year span can be approximated by a second-degree polynomial (parabola):

$$p(x) = a + b x + c x^2$$

Integrating $p(x)$ over each ten-year interval of width $h = 10$:
- Over $T_1 = [-15, -5]$: $T_1 = \int_{-15}^{-5} (a + bx + cx^2) dx = 10a - 100b + \frac{2150}{3} c$
- Over $T_2 = [-5, 5]$: $T_2 = \int_{-5}^5 (a + bx + cx^2) dx = 10a + \frac{250}{3} c$
- Over $T_3 = [5, 15]$: $T_3 = \int_5^{15} (a + bx + cx^2) dx = 10a + 100b + \frac{2150}{3} c$

Subtracting $T_1$ from $T_3$ isolates the linear slope parameter $b$:

$$T_3 - T_1 = 200 b \implies b = \frac{T_3 - T_1}{200}$$

Now consider splitting the central decade $T_2$ into its first five-year component $F_1 = [-5, 0]$ and second five-year component $F_2 = [0, 5]$:

$$F_1 = \int_{-5}^0 (a + bx + cx^2) dx = 5a - \frac{25}{2} b + \frac{125}{3} c$$

Notice that:

$$\frac{1}{2} T_2 = 5a + \frac{125}{3} c$$

Therefore, substituting $\frac{1}{2} T_2$ into the expression for $F_1$:

$$F_1 = \frac{1}{2} T_2 - \frac{25}{2} b = \frac{1}{2} T_2 - \frac{25}{2} \left( \frac{T_3 - T_1}{200} \right) = \frac{1}{2} T_2 + \frac{25}{400} (T_1 - T_3) = \frac{1}{2} T_2 + \frac{1}{16} (T_1 - T_3)$$

Factoring out $T_2$:

$$F_1 = T_2 \left[ \frac{1}{2} + \frac{1}{16} \left( \frac{T_1 - T_3}{T_2} \right) \right]$$

This completes the formal proof. The term $\frac{1}{16} (T_1 - T_3)$ represents the exact parabolic gradient adjustment. If mortality causes the population to decline ($T_1 > T_3$), the first five-year cohort $F_1$ will naturally receive slightly more than half of the decade total $T_2$, precisely reflecting continuous mortality selection without succumbing to digit preference.

## Fully worked question 1: Dual-System Census Undercount Estimation via Post-Enumeration Survey

### Question
A national statistical agency conducts a decennial population census and enumerates $N_{\text{census}} = 48{,}500{,}000$ individuals across the national territory. Independent field auditing reveals that among these enumerated records, $D = 850{,}000$ were duplicate or fictitious records erroneously included by over-zealous field staff.

To evaluate census coverage, an independent, high-precision Post-Enumeration Survey (PES) is conducted across a nationally representative sample of blocks three months later. The PES enumerates an estimated population of $N_{\text{pes}} = 49{,}200{,}000$ individuals. Rigorous automated and manual one-to-one record linkage matches $N_{11} = 45{,}600{,}000$ individuals as being verified in both the census and the PES.

1. Formulate the Chandrasekaran–Deming contingency table and estimate the total number of individuals missed by both the census and the PES ($N_{22}$).
2. Compute the Dual-System Estimate (DSE) of the true population of the nation ($\hat{N}_{\text{true}}$).
3. Determine the net undercount (or overcount), the net undercount rate of the census, and compute the 95% asymptotic confidence interval for the true population size using the large-sample variance of the capture-recapture estimator.

### Solution, step 1: Formulate the Contingency Table and Calculate Valid Census Counts
Before computing the dual-system estimate, we must adjust the raw census total $N_{\text{census}}$ for the known erroneous enumerations $D$.
The valid, non-erroneous census count is:

$$N_{1+} = N_{\text{census}} - D = 48{,}500{,}000 - 850{,}000 = 47{,}650{,}000$$

From the record linkage audit, the number of matched individuals present in both systems is $N_{11} = 45{,}600{,}000$.
We now deduce the remaining marginal cells of the $2 \times 2$ system:
- Number of valid census records not matched in the PES:
  $$N_{12} = N_{1+} - N_{11} = 47{,}650{,}000 - 45{,}600{,}000 = 2{,}050{,}000$$
- Number of PES individuals omitted from the valid census:
  $$N_{21} = N_{+1} - N_{11} = 49{,}200{,}000 - 45{,}600{,}000 = 3{,}600{,}000$$

Under the assumption of statistical independence between the census and the PES enumeration probabilities, the unobserved cell $N_{22}$ (individuals missed by both enumeration systems) is given by:

$$N_{22} = \frac{N_{12} \cdot N_{21}}{N_{11}}$$

Substituting the empirical cell frequencies:

$$N_{22} = \frac{2{,}050{,}000 \times 3{,}600{,}000}{45{,}600{,}000} = \frac{7{,}380{,}000{,}000{,}000}{45{,}600{,}000} \approx 161{,}842.11$$

Rounding to the nearest integer, approximately $161{,}842$ individuals were omitted by both the census and the PES.

### Solution, step 2: Compute the Dual-System Estimate of the True National Population
The Chandrasekaran–Deming Dual-System Estimate of the true population size is:

$$\hat{N}_{\text{true}} = \frac{N_{1+} \cdot N_{+1}}{N_{11}} = \frac{47{,}650{,}000 \times 49{,}200{,}000}{45{,}600{,}000}$$

Carrying out the calculation:

$$\hat{N}_{\text{true}} = \frac{2{,}344{,}380{,}000{,}000{,}000}{45{,}600{,}000} = 51{,}411{,}842.11 \approx 51{,}411{,}842$$

Equivalently, summing all four cells of the completed contingency matrix:

$$\hat{N}_{\text{true}} = N_{11} + N_{12} + N_{21} + N_{22} = 45{,}600{,}000 + 2{,}050{,}000 + 3{,}600{,}000 + 161{,}842 = 51{,}411{,}842$$

Both mathematical formulations coincide perfectly. The estimated true population of the country is $51{,}411{,}842$ inhabitants.

### Solution, step 3: Determine Undercount Rates and Construct Asymptotic Confidence Intervals
We now assess the completeness of the original census:
The net undercount in absolute numbers is:

$$\text{Net Undercount} = \hat{N}_{\text{true}} - N_{\text{census}} = 51{,}411{,}842 - 48{,}500{,}000 = 2{,}911{,}842$$

The net undercount rate relative to the true population is:

$$\hat{U} = \frac{\hat{N}_{\text{true}} - N_{\text{census}}}{\hat{N}_{\text{true}}} = \frac{2{,}911{,}842}{51{,}411{,}842} = 0.056639 \implies 5.66\%$$

Thus, the decennial census suffered from an estimated net undercount of $5.66\%$.

To compute the $95\%$ confidence interval for $\hat{N}_{\text{true}}$, we employ the asymptotic variance formula for the Lincoln-Petersen / Chandrasekaran-Deming estimator derived from the hypergeometric Fisher information:

$$\widehat{\text{Var}}(\hat{N}_{\text{true}}) = \frac{N_{1+} \cdot N_{+1} \cdot N_{12} \cdot N_{21}}{(N_{11})^3}$$

Substituting the known values:

$$\widehat{\text{Var}}(\hat{N}_{\text{true}}) = \frac{47{,}650{,}000 \times 49{,}200{,}000 \times 2{,}050{,}000 \times 3{,}600{,}000}{(45{,}600{,}000)^3}$$

Evaluating the numerator:

$$\text{Num} = 2{,}344{,}380{,}000{,}000{,}000 \times 7{,}380{,}000{,}000{,}000 = 1.73015244 \times 10^{28}$$

The denominator is:

$$(45{,}600{,}000)^3 = 9.4818816 \times 10^{22}$$

Dividing the two quantities:

$$\widehat{\text{Var}}(\hat{N}_{\text{true}}) = \frac{1.73015244 \times 10^{28}}{9.4818816 \times 10^{22}} \approx 182{,}469{,}299.7$$

Taking the square root yields the standard error:

$$\text{SE}(\hat{N}_{\text{true}}) = \sqrt{182{,}469{,}299.7} \approx 13{,}508.12$$

The margin of error at the $95\%$ confidence level ($z_{0.025} = 1.95996$) is:

$$ME = 1.95996 \times 13{,}508.12 \approx 26{,}475$$

The $95\%$ confidence interval for the true national population size is:

$$[51{,}411{,}842 - 26{,}475, \; 51{,}411{,}842 + 26{,}475] = [51{,}385{,}367, \; 51{,}438{,}317]$$

This narrow analytical interval confirms that with massive sample sizes, the Dual-System Estimator provides an exceptionally precise adjustment for census omissions.


### Systematic Comparison of Sprague, Beers, and Greville Interpolation Methods
When demographers must reconstruct single-year population distributions from five-year age data, osculatory interpolation techniques provide the mathematical bridge between aggregate reporting and fine-grained demographic analysis. Osculatory interpolation differs from ordinary Lagrange polynomial interpolation in that adjacent polynomial arcs not only intersect at the boundary points between age groups, but also share identical first and second derivatives. This smooth tangential blending eliminates artificial kinks, discontinuous jumps, and negative values at group boundaries.

1. **Sprague's Fifth-Difference Formula**: Developed by Thomas Bond Sprague in 1880, this classical formula fits a fourth-degree or fifth-degree polynomial through six consecutive five-year age groups. The central age group is subdivided into five single-year ages using pre-calculated matrix weights. Sprague ensures that the graduated single-year counts sum exactly to the observed five-year total while minimizing the third and fifth differences across boundaries. However, Sprague formulas can occasionally produce slight oscillations or negative numbers near extreme boundaries (e.g., ages 0–4 or ages 85+).
2. **Beers' Modified Interpolation Coefficients**: In 1945, Henry Beers developed two sets of interpolation coefficients: the "ordinary" formula (which maintains exact group totals) and the "minimized fifth-difference" formula (which permits slight smoothing adjustments to the group totals themselves to eliminate boundary distortions). Beers formulas are widely recognized as superior for graduating data from developing nations where the initial five-year groups already suffer from age-heaping leakage across boundaries.
3. **Greville's Method**: Thomas N. E. Greville integrated actuarial graduation theory with cubic spline interpolation. Greville established that by minimizing a linear combination of squared third differences, one obtains a smoothing operator that preserves the underlying linear demographic trend while effectively dampening observational noise.

Applying these graduation techniques before constructing life tables prevents spurious oscillations in central death rates and ensures that infant and child mortality estimates are not corrupted by digit heaping at ages 5, 10, and 15.

## Fully worked question 2: Computation and Structural Diagnosis of Whipple's Index

### Question
An undergraduate statistical fieldwork team analyzes single-year age data collected during a municipal census in an urbanizing district. The reported population counts for each single year of age in the critical adult evaluation bracket $[23, 62]$ are summarized below in quinquennial clusters:

- Ages 23–24: $P_{23} = 18{,}200, P_{24} = 19{,}100$
- Ages 25–29: $P_{25} = 44{,}800, P_{26} = 20{,}100, P_{27} = 19{,}400, P_{28} = 21{,}200, P_{29} = 18{,}600$
- Ages 30–34: $P_{30} = 56{,}200, P_{31} = 16{,}500, P_{32} = 17{,}800, P_{33} = 16{,}900, P_{34} = 17{,}400$
- Ages 35–39: $P_{35} = 48{,}500, P_{36} = 15{,}800, P_{37} = 15{,}100, P_{38} = 16{,}200, P_{39} = 14{,}900$
- Ages 40–44: $P_{40} = 51{,}300, P_{41} = 13{,}700, P_{42} = 14{,}500, P_{43} = 13{,}800, P_{44} = 14{,}100$
- Ages 45–49: $P_{45} = 41{,}700, P_{46} = 12{,}400, P_{47} = 11{,}900, P_{48} = 12{,}800, P_{49} = 11{,}600$
- Ages 50–54: $P_{50} = 45{,}600, P_{51} = 10{,}200, P_{52} = 10{,}900, P_{53} = 10{,}400, P_{54} = 10{,}700$
- Ages 55–59: $P_{55} = 34{,}900, P_{56} = 8{,}900, P_{57} = 8{,}500, P_{58} = 9{,}200, P_{59} = 8{,}300$
- Ages 60–62: $P_{60} = 38{,}200, P_{61} = 7{,}100, P_{62} = 7{,}400$

1. Calculate the total population in the age range $[23, 62]$ and the sum of populations reporting terminal digits 0 and 5.
2. Calculate the classical Whipple's Index $W$ for the combined population.
3. Decompose Whipple's Index separately into digit-0 preference ($W_0$) and digit-5 preference ($W_5$), and classify the data quality according to United Nations criteria.

### Solution, step 1: Compute Total Population and Target Digits (0 and 5) Sums
First, we sum the populations reporting ages ending in 0:

$$\sum P_0 = P_{30} + P_{40} + P_{50} + P_{60} = 56{,}200 + 51{,}300 + 45{,}600 + 38{,}200 = 191{,}300$$

Next, we sum the populations reporting ages ending in 5:

$$\sum P_5 = P_{25} + P_{35} + P_{45} + P_{55} = 44{,}800 + 48{,}500 + 41{,}700 + 34{,}900 = 169{,}900$$

The total population reporting ages ending in 0 and 5 combined is:

$$\sum P_{0,5} = \sum P_0 + \sum P_5 = 191{,}300 + 169{,}900 = 361{,}200$$

Now, we sum all 40 individual age cohorts from 23 through 62:
- Ages 23–24: $18{,}200 + 19{,}100 = 37{,}300$
- Ages 25–29: $44{,}800 + 20{,}100 + 19{,}400 + 21{,}200 + 18{,}600 = 124{,}100$
- Ages 30–34: $56{,}200 + 16{,}500 + 17{,}800 + 16{,}900 + 17{,}400 = 124{,}800$
- Ages 35–39: $48{,}500 + 15{,}800 + 15{,}100 + 16{,}200 + 14{,}900 = 110{,}500$
- Ages 40–44: $51{,}300 + 13{,}700 + 14{,}500 + 13{,}800 + 14{,}100 = 107{,}400$
- Ages 45–49: $41{,}700 + 12{,}400 + 11{,}900 + 12{,}800 + 11{,}600 = 90{,}400$
- Ages 50–54: $45{,}600 + 10{,}200 + 10{,}900 + 10{,}400 + 10{,}700 = 87{,}800$
- Ages 55–59: $34{,}900 + 8{,}900 + 8{,}500 + 9{,}200 + 8{,}300 = 69{,}800$
- Ages 60–62: $38{,}200 + 7{,}100 + 7{,}400 = 52{,}700$

Summing all groups:

$$\sum_{x=23}^{62} P_x = 37{,}300 + 124{,}100 + 124{,}800 + 110{,}500 + 107{,}400 + 90{,}400 + 87{,}800 + 69{,}800 + 52{,}700 = 804{,}800$$

The total population in the age bracket $[23, 62]$ is $804{,}800$.

### Solution, step 2: Compute Classical Whipple's Index
Using the classical United Nations formula:

$$W = \frac{5 \cdot \sum P_{0,5}}{\sum_{x=23}^{62} P_x} \times 100$$

Substitute the calculated sums:

$$W = \frac{5 \times 361{,}200}{804{,}800} \times 100 = \frac{1{,}806{,}000}{804{,}800} \times 100 = 2.2440358 \times 100 \approx 224.40$$

Whipple's Index is $224.40$.

### Solution, step 3: Decompose into Digit-0 and Digit-5 Components and Classify
To understand the relative pull of digits 0 versus 5, demographers decompose Whipple's Index. Because digits ending in 0 occur four times in $[23, 62]$ (at 30, 40, 50, 60), the expected proportion of digit 0 under uniformity is $4 / 40 = 1/10 = 10\%$.
Therefore, the digit-0 index is:

$$W_0 = \frac{10 \cdot \sum P_0}{\sum_{x=23}^{62} P_x} \times 100 = \frac{10 \times 191{,}300}{804{,}800} \times 100 = \frac{1{,}913{,}000}{804{,}800} \times 100 \approx 237.70$$

Similarly, digit 5 occurs four times in $[23, 62]$ (at 25, 35, 45, 55). Its index is:

$$W_5 = \frac{10 \cdot \sum P_5}{\sum_{x=23}^{62} P_x} \times 100 = \frac{10 \times 169{,}900}{804{,}800} \times 100 = \frac{1{,}699{,}000}{804{,}800} \times 100 \approx 211.11$$

Observe that:

$$\frac{W_0 + W_5}{2} = \frac{237.70 + 211.11}{2} = 224.405 = W$$

The decomposition reveals:
1. Both terminal digits exhibit colossal age heaping, far exceeding the baseline of 100.
2. Digit 0 ($W_0 = 237.70$) exerts a substantially stronger gravitational attraction than digit 5 ($W_5 = 211.11$).
3. Under the United Nations quality categorization scale:
   - $W = 224.40 > 175$, which places this municipal dataset unambiguously in the **Very Rough Data** category. Over $44.88\%$ of the adult population in this interval reported an age ending in 0 or 5, compared to the expected $20\%$. Direct single-year use of these data without rigorous mathematical graduation will introduce severe bias into demographic indicators.

## Fully worked question 3: Rigorous Step-by-Step Construction of Myers' Blended Index

### Question
To analyze digit preference across all ten digits $0, 1, 2, \dots, 9$, a demographic research institute extracts single-year age data from a provincial census covering ages 10 through 89. The unweighted sums of populations starting at age 10 ($U_d = \sum_{k=1}^7 P_{10k+d}$) and starting at age 20 ($V_d = \sum_{k=2}^8 P_{10k+d}$) for each terminal digit $d$ are obtained as follows:

| Terminal Digit ($d$) | $U_d$ (Ages 10–79) | $V_d$ (Ages 20–89) |
| :---: | :---: | :---: |
| **0** | $542{,}000$ | $468{,}000$ |
| **1** | $215{,}000$ | $176{,}000$ |
| **2** | $328{,}000$ | $271{,}000$ |
| **3** | $234{,}000$ | $191{,}000$ |
| **4** | $256{,}000$ | $208{,}000$ |
| **5** | $482{,}000$ | $398{,}000$ |
| **6** | $268{,}000$ | $217{,}000$ |
| **7** | $221{,}000$ | $178{,}000$ |
| **8** | $341{,}000$ | $279{,}000$ |
| **9** | $198{,}000$ | $159{,}000$ |

1. Apply Myers' linear blending coefficients $(d+1)$ and $(9-d)$ to compute the blended population $B_d$ for each terminal digit $d \in \{0, 1, \dots, 9\}$.
2. Calculate the total blended population $B_{\text{total}}$ and the percentage share $p_d$ of each terminal digit.
3. Compute the absolute deviations from the $10.0\%$ theoretical uniform expectation, determine Myers' Blended Index $M$, and provide a complete diagnostic assessment of digit attraction and digit avoidance.

### Solution, step 1: Compute Blended Populations for Each Terminal Digit
Myers' blending formula is:

$$B_d = (d + 1) \cdot U_d + (9 - d) \cdot V_d$$

We calculate $B_d$ systematically for each digit $d = 0, 1, \dots, 9$:
- Digit 0: $B_0 = (0 + 1) \times 542{,}000 + (9 - 0) \times 468{,}000 = 1 \times 542{,}000 + 9 \times 468{,}000 = 542{,}000 + 4{,}212{,}000 = 4{,}754{,}000$
- Digit 1: $B_1 = (1 + 1) \times 215{,}000 + (9 - 1) \times 176{,}000 = 2 \times 215{,}000 + 8 \times 176{,}000 = 430{,}000 + 1{,}408{,}000 = 1{,}838{,}000$
- Digit 2: $B_2 = (2 + 1) \times 328{,}000 + (9 - 2) \times 271{,}000 = 3 \times 328{,}000 + 7 \times 271{,}000 = 984{,}000 + 1{,}897{,}000 = 2{,}881{,}000$
- Digit 3: $B_3 = (3 + 1) \times 234{,}000 + (9 - 3) \times 191{,}000 = 4 \times 234{,}000 + 6 \times 191{,}000 = 936{,}000 + 1{,}146{,}000 = 2{,}082{,}000$
- Digit 4: $B_4 = (4 + 1) \times 256{,}000 + (9 - 4) \times 208{,}000 = 5 \times 256{,}000 + 5 \times 208{,}000 = 1{,}280{,}000 + 1{,}040{,}000 = 2{,}320{,}000$
- Digit 5: $B_5 = (5 + 1) \times 482{,}000 + (9 - 5) \times 398{,}000 = 6 \times 482{,}000 + 4 \times 398{,}000 = 2{,}892{,}000 + 1{,}592{,}000 = 4{,}484{,}000$
- Digit 6: $B_6 = (6 + 1) \times 268{,}000 + (9 - 6) \times 217{,}000 = 7 \times 268{,}000 + 3 \times 217{,}000 = 1{,}876{,}000 + 651{,}000 = 2{,}527{,}000$
- Digit 7: $B_7 = (7 + 1) \times 221{,}000 + (9 - 7) \times 178{,}000 = 8 \times 221{,}000 + 2 \times 178{,}000 = 1{,}768{,}000 + 356{,}000 = 2{,}124{,}000$
- Digit 8: $B_8 = (8 + 1) \times 341{,}000 + (9 - 8) \times 279{,}000 = 9 \times 341{,}000 + 1 \times 279{,}000 = 3{,}069{,}000 + 279{,}000 = 3{,}348{,}000$
- Digit 9: $B_9 = (9 + 1) \times 198{,}000 + (9 - 9) \times 159{,}000 = 10 \times 198{,}000 + 0 \times 159{,}000 = 1{,}980{,}000 + 0 = 1{,}980{,}000$

### Solution, step 2: Compute Total Blended Population and Percent Shares
We sum the blended populations across all ten digits:

$$B_{\text{total}} = \sum_{d=0}^9 B_d$$

$$B_{\text{total}} = 4{,}754{,}000 + 1{,}838{,}000 + 2{,}881{,}000 + 2{,}082{,}000 + 2{,}320{,}000 + 4{,}484{,}000 + 2{,}527{,}000 + 2{,}124{,}000 + 3{,}348{,}000 + 1{,}980{,}000$$

$$B_{\text{total}} = 28{,}338{,}000$$

Now compute the percentage distribution $p_d = \frac{B_d}{B_{\text{total}}} \times 100$:
- $p_0 = \frac{4{,}754{,}000}{28{,}338{,}000} \times 100 = 16.7761\%$
- $p_1 = \frac{1{,}838{,}000}{28{,}338{,}000} \times 100 = 6.4860\%$
- $p_2 = \frac{2{,}881{,}000}{28{,}338{,}000} \times 100 = 10.1666\%$
- $p_3 = \frac{2{,}082{,}000}{28{,}338{,}000} \times 100 = 7.3470\%$
- $p_4 = \frac{2{,}320{,}000}{28{,}338{,}000} \times 100 = 8.1869\%$
- $p_5 = \frac{4{,}484{,}000}{28{,}338{,}000} \times 100 = 15.8233\%$
- $p_6 = \frac{2{,}527{,}000}{28{,}338{,}000} \times 100 = 8.9174\%$
- $p_7 = \frac{2{,}124{,}000}{28{,}338{,}000} \times 100 = 7.4952\%$
- $p_8 = \frac{3{,}348{,}000}{28{,}338{,}000} \times 100 = 11.8145\%$
- $p_9 = \frac{1{,}980{,}000}{28{,}338{,}000} \times 100 = 6.9871\%$

Sum check: $16.7761 + 6.4860 + 10.1666 + 7.3470 + 8.1869 + 15.8233 + 8.9174 + 7.4952 + 11.8145 + 6.9871 = 100.00\%$.

### Solution, step 3: Compute Absolute Deviations and Myers' Index
Under uniform distribution, each digit is expected to constitute exactly $10.0\%$.
We compute the signed deviations $\delta_d = p_d - 10.0$ and absolute deviations $|\delta_d|$:
- Digit 0: $16.7761 - 10.0 = +6.7761 \implies |\delta_0| = 6.7761$ (Attraction)
- Digit 1: $6.4860 - 10.0 = -3.5140 \implies |\delta_1| = 3.5140$ (Avoidance)
- Digit 2: $10.1666 - 10.0 = +0.1666 \implies |\delta_2| = 0.1666$ (Slight Attraction)
- Digit 3: $7.3470 - 10.0 = -2.6530 \implies |\delta_3| = 2.6530$ (Avoidance)
- Digit 4: $8.1869 - 10.0 = -1.8131 \implies |\delta_4| = 1.8131$ (Avoidance)
- Digit 5: $15.8233 - 10.0 = +5.8233 \implies |\delta_5| = 5.8233$ (Attraction)
- Digit 6: $8.9174 - 10.0 = -1.0826 \implies |\delta_6| = 1.0826$ (Avoidance)
- Digit 7: $7.4952 - 10.0 = -2.5048 \implies |\delta_7| = 2.5048$ (Avoidance)
- Digit 8: $11.8145 - 10.0 = +1.8145 \implies |\delta_8| = 1.8145$ (Attraction)
- Digit 9: $6.9871 - 10.0 = -3.0129 \implies |\delta_9| = 3.0129$ (Avoidance)

Sum of positive deviations (total excess):
$$\sum \delta^+ = 6.7761 + 0.1666 + 5.8233 + 1.8145 = 14.5805$$

Sum of negative deviations (total deficit):
$$\sum |\delta^-| = 3.5140 + 2.6530 + 1.8131 + 1.0826 + 2.5048 + 3.0129 = 14.5804$$

Total absolute deviation sum:
$$\sum_{d=0}^9 |\delta_d| = 14.5805 + 14.5804 = 29.1609$$

Myers' Blended Index is one-half of the total sum of absolute deviations:

$$M = \frac{1}{2} \sum_{d=0}^9 |p_d - 10.0| = \frac{1}{2} \times 29.1609 \approx 14.58$$

### Diagnostic Interpretation:
1. **Index Magnitude**: Myers' Index is $M = 14.58$. Values between 10 and 20 signify **moderate to substantial age misreporting**.
2. **Preferred Digits**: The population exhibits massive positive attraction to terminal digits 0 ($+6.78\%$) and 5 ($+5.82\%$), with secondary preference for even digit 8 ($+1.81\%$) and digit 2 ($+0.17\%$).
3. **Avoided Digits**: Severe avoidance is recorded for odd terminal digits 1 ($-3.51\%$), 9 ($-3.01\%$), 3 ($-2.65\%$), and 7 ($-2.50\%$).
4. **Demographic Implication**: Approximately $14.58\%$ of the total population reported an age ending in an incorrect digit. This empirical finding mandates the application of five-year age grouping and Carrier-Farrag graduation prior to life table generation.
