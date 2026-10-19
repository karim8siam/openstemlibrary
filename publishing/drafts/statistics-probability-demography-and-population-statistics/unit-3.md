# Unit 3: Measures of Mortality & Standardization Techniques

Mortality is the demographic process that diminishes population numbers through the irreversible biological termination of life. In mathematical demography, measuring mortality requires distinguishing between raw event counts and true exposure to the risk of death. Because the physiological risk of death varies by several orders of magnitude across the human lifespan—exhibiting an asymmetrical U-shaped or J-shaped curve with elevated vulnerability in infancy, minimal risk during late childhood, and exponential increases throughout adult senescence—evaluating mortality requires rigorous age-specific metrics and mathematical standardization techniques to remove the confounding influence of population age structures.

## 3.1 The Concept of Person-Years of Exposure and Central Death Rates

In elementary statistics, a rate is often calculated by dividing the number of events by an initial population. In demography, however, individuals enter and exit populations continuously throughout any observational window through births, deaths, and migrations. To establish a rigorous mathematical denominator, demographers employ the concept of **person-years of exposure**.

### Continuous Exposure Formulation
Let $N(t)$ denote the continuous size of a population at time $t$. Over the calendar interval $[0, T]$, the total person-years lived by the population, denoted by $PY[0, T]$, is the integral of the population trajectory:

$$PY[0, T] = \int_0^T N(t) \, dt$$

If the population changes linearly over a single calendar year ($T = 1$), the integral simplifies to the mid-year population:

$$PY = \int_0^1 \left( N(0) + t \cdot [N(1) - N(0)] \right) dt = N(0) + \frac{1}{2} [N(1) - N(0)] = \frac{N(0) + N(1)}{2} = N(0.5) = P_{\text{mid}}$$

Thus, in annual demographic accounting, the mid-year population enumerated on July 1 serves as the standard empirical approximation for total person-years of exposure.

### The Crude Death Rate (CDR)
The most basic aggregate measure of mortality is the **Crude Death Rate ($CDR$)**, defined as the total number of deaths $D$ occurring in a given geographic territory during a calendar year divided by the total person-years lived (mid-year population $P_{\text{mid}}$), conventionally expressed per $1{,}000$ person-years:

$$CDR = \frac{D}{P_{\text{mid}}} \times 1{,}000$$

While straightforward to calculate from vital statistics and census totals, the Crude Death Rate is notoriously deceptive when used to compare health or living standards across different countries. For example, a prosperous European country with exceptional healthcare (such as Sweden or Germany) frequently records a higher $CDR$ ($10$ to $12$ per $1{,}000$) than a developing nation with far poorer health infrastructure (such as Nicaragua or Jordan, with $CDR \approx 4$ to $5$ per $1{,}000$). This apparent paradox arises because the European population has a large proportion of senior citizens, whereas the developing country has a young population concentrated in childhood and young adulthood where biological death risks are minimal. The Crude Death Rate is heavily confounded by the underlying age composition.

## 3.2 Age-Specific Death Rates (ASDR) and the Force of Mortality

To eliminate the distorting influence of age composition, demographers decompose mortality into narrow, homogeneous age intervals.

### The Age-Specific Death Rate (ASDR)
Let $D_x$ denote the number of deaths occurring to persons aged $x$ to $x+n$ during a calendar year, and let $P_x$ denote the mid-year population in that exact age group. The **Age-Specific Death Rate** (central death rate), denoted by $_n M_x$ or $_n m_x$, is:

$$_n M_x = \frac{_n D_x}{_n P_x} \times 1{,}000$$

When $n = 1$, $_1 M_x$ represents the single-year age-specific death rate. In quinquennial demographic tables, $n = 5$, and $_5 M_x$ represents the five-year central death rate.

Across all human populations, the curve of $_n M_x$ against age $x$ exhibits the classical **Gompertz-Makeham trajectory**:
1. At age 0 (infancy): $_1 M_0$ is elevated due to congenital anomalies, birth trauma, and neonatal vulnerabilities.
2. Ages 1–14: Mortality falls precipitously, reaching its absolute biological minimum around ages 9–11 (where annual risk drops below $0.2$ per $1{,}000$).
3. Ages 15–24: A localized elevation emerges, particularly among males, known as the **accident hump** (driven by motor vehicle injuries, interpersonal violence, and risk-taking behaviors).
4. Ages 30 and above: Mortality increases monotonically at an exponential rate, doubling approximately every seven to eight years (actuarial Gompertz law).

### The Continuous Force of Mortality
In continuous mathematical demography, the instantaneous rate of mortality at exact age $x$ is termed the **Force of Mortality**, denoted by $\mu(x)$.
Let $S(x)$ denote the survival function—the continuous probability that a newborn survives to exact age $x$. The force of mortality is defined as the negative logarithmic derivative of the survival function:

$$\mu(x) = -\frac{1}{S(x)} \frac{d S(x)}{dx} = -\frac{d \ln S(x)}{dx}$$

Integrating both sides from $0$ to $x$ yields the fundamental exponential survival identity:

$$S(x) = \exp\left( -\int_0^x \mu(t) \, dt \right)$$

Benjamin Gompertz (1825) showed that for adult humans ($x > 30$), the force of mortality can be modeled as $\mu(x) = B c^x = B e^{\alpha x}$, where $\alpha \approx 0.08$ to $0.10$ represents the rate of biological senescence. William Makeham (1860) generalized this to $\mu(x) = A + B c^x$, where $A$ represents age-independent background hazard (accidents, homicides) and $B c^x$ captures intrinsic senescence.

## 3.3 Infant, Neonatal, and Maternal Mortality Measurement

Certain developmental stages in the life course present unique biological and environmental hazards, necessitating specialized epidemiological indicators.

### The Infant Mortality Rate (IMR)
The **Infant Mortality Rate ($IMR$)** measures the probability of dying between birth and exact age one. Unlike general death rates which use mid-year population in the denominator, the $IMR$ divides infant deaths by registered live births, expressed per $1{,}000$ live births:

$$IMR = \frac{D_0}{B} \times 1{,}000$$

where $D_0$ is the number of deaths of infants under one year of age ($0$ to $364$ days) occurring during the calendar year, and $B$ is the total number of live births registered in the same calendar year.

Because infants dying in calendar year $t$ may have been born in either year $t$ or year $t-1$, an exact cohort-adjusted infant mortality rate utilizes separation factors $f$:

$$IMR_{\text{adjusted}} = \frac{D_0}{f \cdot B_t + (1 - f) \cdot B_{t-1}} \times 1{,}000$$

In high-mortality settings, $f \approx 0.70$ to $0.80$, because the vast majority of infant deaths occur in the first few weeks of life.

### Sub-Components of Infant Mortality
Infant mortality is decomposed into two distinct physiological periods:
1. **Neonatal Mortality Rate ($NMR$)**: Deaths occurring during the first 28 completed days of life ($0-27$ days), per $1{,}000$ live births:
   $$NMR = \frac{D_{\text{neonatal}}}{B} \times 1{,}000$$
   Neonatal mortality reflects endogenous factors: congenital malformations, chromosomal defects, prematurity, low birth weight, and obstetrical complications during labor.
   - **Early Neonatal Mortality**: Deaths within the first seven days of life ($0-6$ days).
   - **Late Neonatal Mortality**: Deaths occurring between day 7 and day 27 of life.
2. **Post-Neonatal Mortality Rate ($PNMR$)**: Deaths occurring from day 28 up to the first birthday ($28-364$ days), per $1{,}000$ live births:
   $$PNMR = \frac{D_{\text{post-neonatal}}}{B} \times 1{,}000$$
   Post-neonatal mortality reflects exogenous environmental factors: nutritional deficiencies, infectious diarrheal diseases, respiratory infections, and poor sanitary conditions.

The two rates sum to the total infant mortality rate:

$$IMR = NMR + PNMR$$

### Under-Five Mortality Rate ($q_5$ / $U5MR$)
The probability that a newborn child will die before reaching exact age five, expressed per $1{,}000$ live births. Under-five mortality is the primary international benchmark of child survival and public health development.

### The Maternal Mortality Ratio (MMR)
Maternal mortality measures deaths of women resulting from complications of pregnancy, labor, and puerperium (up to 42 days postpartum). The **Maternal Mortality Ratio ($MMR$)** is defined per $100{,}000$ live births:

$$MMR = \frac{D_{\text{maternal}}}{B} \times 100{,}000$$

The denominator uses live births as an operational proxy for the total number of pregnancies, because the total count of pregnancies (including miscarriages, induced abortions, and ectopic pregnancies) is rarely recorded completely in civil registration.

## 3.4 Direct Standardization of Rates: Methodology and Theoretical Foundations

When comparing mortality across two or more populations with divergent age structures, direct rate standardization constructs a hypothetical counterfactual comparison: what death rates would be observed if all compared populations shared the exact same, identical age distribution?

### Mathematical Formulation of Direct Standardization
Let $A$ and $B$ denote two study populations, and let $S$ denote an agreed-upon, fixed **Standard Population** (such as the WHO World Standard Population or a national census total).
Let:
- $_n m_x^A$ denote the observed age-specific death rate in population $A$ for age group $[x, x+n)$.
- $_n m_x^B$ denote the observed age-specific death rate in population $B$ for age group $[x, x+n)$.
- $_n P_x^S$ denote the number of persons in age group $[x, x+n)$ in the standard population $S$.
- $P^S = \sum_x {_n P_x^S}$ denote the total size of the standard population.
- $_n c_x^S = \frac{_n P_x^S}{P^S}$ denote the age-composition weights of the standard population, satisfying $\sum_x {_n c_x^S} = 1$.

The **Directly Standardized Death Rate** for population $A$, denoted by $DSDR_A$ (or $SDR_A$), is:

$$DSDR_A = \frac{\sum_x \left( _n m_x^A \cdot {_n P_x^S} \right)}{\sum_x {_n P_x^S}} = \sum_x \left( _n m_x^A \cdot {_n c_x^S} \right)$$

Similarly, for population $B$:

$$DSDR_B = \sum_x \left( _n m_x^B \cdot {_n c_x^S} \right)$$

The **Comparative Mortality Figure ($CMF$)** is the ratio of the directly standardized rates:

$$CMF_{A/B} = \frac{DSDR_A}{DSDR_B}$$

Because both populations are evaluated using the identical set of age weights $_n c_x^S$, any difference between $DSDR_A$ and $DSDR_B$ reflects solely genuine differences in biological mortality schedules $_n m_x$, completely purged of structural age bias.

## 3.5 Indirect Standardization and the Standardized Mortality Ratio (SMR)

Direct standardization requires full knowledge of age-specific death rates $_n m_x^A$ in the study population. In many occupational epidemiological studies, small regional communities, or historical datasets, the study population is too small to yield reliable age-specific death rates (many age cells record zero or one death, producing extreme stochastic noise), or age-specific death counts are unrecorded while total deaths $D_A$ and age-specific population counts $_n P_x^A$ are known.

In such circumstances, mathematical demographers deploy **indirect standardization**.

### Mathematical Formulation of Indirect Standardization
Instead of applying study rates to a standard population, indirect standardization applies the reliable, robust age-specific death rates of a large standard population ($m_x^S$) to the age structure of the study population ($P_x^A$) to calculate the **Expected Deaths** ($E_A$).

The expected number of deaths in study population $A$, denoted by $E_A$, is:

$$E_A = \sum_x \left( _n m_x^S \cdot {_n P_x^A} \right)$$

The **Standardized Mortality Ratio ($SMR$)** is the ratio of the total observed deaths $D_A$ to the total expected deaths $E_A$, conventionally expressed as a percentage or decimal:

$$SMR_A = \frac{D_A}{E_A} = \frac{\sum_x {_n D_x^A}}{\sum_x \left( _n m_x^S \cdot {_n P_x^A} \right)}$$

### Interpretation of the SMR
- If $SMR = 1.00$ ($100\%$): Mortality in the study population is exactly identical to the mortality regime of the standard population, after adjusting for age composition.
- If $SMR > 1.00$: Mortality in the study population is elevated relative to the standard (an $SMR$ of $1.35$ indicates $35\%$ excess mortality).
- If $SMR < 1.00$: Mortality in the study population is lower than the standard (frequently observed in occupational health studies as the **Healthy Worker Effect**, where employed persons exhibit $SMR \approx 0.75-0.85$ relative to the general population).

The **Indirectly Standardized Death Rate** ($ISDR_A$) is obtained by multiplying the $SMR$ by the crude death rate of the standard population:

$$ISDR_A = SMR_A \times CDR_S$$

## 3.6 Cause-Deleted Mortality Analysis and Competing Risks

Human mortality is composed of multiple competing causes of death (cardiovascular diseases, neoplasms, respiratory infections, external injuries). When medical interventions eliminate or reduce a specific pathology, how does life expectancy change?

In 1975, Nathan Keyfitz formalized **cause-deleted life table analysis**. Under the assumption of independent competing risks, let the total force of mortality be the sum of cause-specific forces:

$$\mu(x) = \sum_{j=1}^J \mu_j(x)$$

Let cause $i$ (e.g., all malignant neoplasms) be completely eliminated from the population. The cause-deleted force of mortality is:

$$\mu_{-i}(x) = \mu(x) - \mu_i(x)$$

Let $R_i(x) = \frac{\mu_i(x)}{\mu(x)}$ denote the proportion of deaths attributable to cause $i$ at age $x$. Then the cause-deleted survival probability across age interval $[x, x+n)$ is related to the all-cause survival probability $_n p_x$ by the power law:

$$_n p_x^{-i} = \left( _n p_x \right)^{1 - R_i(x)}$$

This power relationship enables demographers to construct hypothetical cause-deleted life tables and compute the **Potential Gain in Life Expectancy** attributable to eradicating a specific disease category.


### Unobserved Heterogeneity, Frailty Models, and the Mortality Crossover Paradox
A perplexing empirical phenomenon that fascinated classical actuaries is the **Mortality Crossover**. When comparing the age-specific death rates of two socially or economically distinct sub-populations, the disadvantaged group (e.g., lower socioeconomic status, racial minorities, or historical populations with high childhood infectious mortality) exhibits substantially higher death rates throughout youth, middle age, and early old age. However, at extreme advanced ages (ages 85, 90, and above), the mortality curves frequently intersect, and the disadvantaged group records lower age-specific mortality rates than the historically privileged population!

In 1979, James W. Vaupel, Kenneth G. Manton, and Eric Stallard resolved this puzzle by formulating the **Mathematical Theory of Frailty**. They demonstrated that mortality crossovers are an inevitable consequence of **unobserved heterogeneity and selective survival**.

Let individuals within a population possess an unobserved, lifelong biological frailty variable Z > 0, representing individual genetic resilience, immune robustness, and metabolic vigor. The force of mortality for an individual with frailty z at age x is:

$$\mu(x \mid z) = z \cdot \mu_0(x)$$

where mu_0(x) is the baseline standard force of mortality for a person of standard frailty (z = 1).
Assume frailty Z is distributed across the initial birth cohort according to a Gamma distribution with mean E[Z] = 1 and variance sigma^2:

$$f(z) = \frac{k^k}{\Gamma(k)} z^{k-1} e^{-k z} \quad \text{where } k = \frac{1}{\sigma^2}$$

As the birth cohort ages, individuals with high frailty (z >> 1) die at much younger ages, whereas individuals with low frailty (z << 1, biologically exceptionally robust individuals) survive. Consequently, the mean frailty of the surviving cohort decreases continuously with age:

$$\bar{z}(x) = \frac{1}{1 + \sigma^2 \int_0^x \mu_0(t) \, dt} = \frac{1}{1 + \sigma^2 H_0(x)}$$

where H_0(x) is the cumulative baseline hazard.
The observed population force of mortality is the average across survivors:

$$\bar{\mu}(x) = \bar{z}(x) \cdot \mu_0(x) = \frac{\mu_0(x)}{1 + \sigma^2 H_0(x)}$$

In a disadvantaged population subject to severe environmental hazards in early life, the attrition of frail individuals is intense and brutal, purging the cohort of high-frailty members early. By age 85, the survivors of the disadvantaged group represent an elite, biologically hyper-selected sub-sample whose mean frailty is significantly lower than that of the protected group, where modern medicine kept higher-frailty individuals alive into old age. This survival selection creates the apparent mortality crossover without requiring any late-life biological reversal.

## Fully worked question 1: Direct and Indirect Mortality Standardization with Structural Age Confounding

### Question
An international epidemiological research team compares the mortality regimes of two populations: Country Alpha (a developed European territory with an aged population) and Country Beta (a developing South American nation with a young population). Quinquennial demographic data and a recognized World Standard Population are recorded below:

| Age Bracket | Country Alpha Pop ($P_x^A$) | Country Alpha Deaths ($D_x^A$) | Country Beta Pop ($P_x^B$) | Country Beta Deaths ($D_x^B$) | World Standard Pop ($P_x^S$) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **0–14** | $1{,}500{,}000$ | $1{,}500$ | $4{,}000{,}000$ | $12{,}000$ | $3{,}000{,}000$ |
| **15–39** | $3{,}000{,}000$ | $3{,}000$ | $3{,}500{,}000$ | $7{,}000$ | $3{,}500{,}000$ |
| **40–64** | $3{,}500{,}000$ | $14{,}000$ | $2{,}000{,}000$ | $16{,}000$ | $2{,}500{,}000$ |
| **65+** | $2{,}000{,}000$ | $80{,}000$ | $500{,}000$ | $30{,}000$ | $1{,}000{,}000$ |
| **Total** | $10{,}000{,}000$ | $98{,}500$ | $10{,}000{,}000$ | $65{,}000$ | $10{,}000{,}000$ |

1. Calculate the Crude Death Rate ($CDR$) for both Country Alpha and Country Beta per $1{,}000$ population. Compare the raw rates.
2. Compute the age-specific death rates ($m_x$) for each age group in both countries.
3. Compute the Directly Standardized Death Rate ($DSDR$) for both countries using the World Standard Population, and determine the Comparative Mortality Figure ($CMF_{B/A}$).
4. Using Country Alpha as the standard population, calculate the expected deaths in Country Beta and determine Country Beta's Standardized Mortality Ratio ($SMR_B$). Explain the apparent reversal of mortality rankings.

### Solution, step 1: Calculate Crude Death Rates
The total populations of both Country Alpha and Country Beta are $N_A = N_B = 10{,}000{,}000$.
- Total deaths in Country Alpha: $D_A = 1{,}500 + 3{,}000 + 14{,}000 + 80{,}000 = 98{,}500$
- Total deaths in Country Beta: $D_B = 12{,}000 + 7{,}000 + 16{,}000 + 30{,}000 = 65{,}000$

The Crude Death Rates are:

$$CDR_A = \frac{D_A}{N_A} \times 1{,}000 = \frac{98{,}500}{10{,}000{,}000} \times 1{,}000 = 9.85 \text{ per 1,000}$$

$$CDR_B = \frac{D_B}{N_B} \times 1{,}000 = \frac{65{,}000}{10{,}000{,}000} \times 1{,}000 = 6.50 \text{ per 1,000}$$

A superficial inspection of Crude Death Rates indicates that Country Beta has a substantially lower death rate ($6.50$ vs $9.85$ per $1{,}000$), which might naively lead an observer to conclude that health conditions are superior in Country Beta.

### Solution, step 2: Calculate Age-Specific Death Rates
We calculate the age-specific death rates per $1{,}000$ ($m_x = \frac{D_x}{P_x} \times 1{,}000$) for each cohort:

1. **Age 0–14**:
   - Alpha: $m_{0-14}^A = \frac{1{,}500}{1{,}500{,}000} \times 1{,}000 = 1.00 \text{ per 1,000}$
   - Beta: $m_{0-14}^B = \frac{12{,}000}{4{,}000{,}000} \times 1{,}000 = 3.00 \text{ per 1,000}$
   *(Beta mortality is 3 times higher in childhood)*

2. **Age 15–39**:
   - Alpha: $m_{15-39}^A = \frac{3{,}000}{3{,}000{,}000} \times 1{,}000 = 1.00 \text{ per 1,000}$
   - Beta: $m_{15-39}^B = \frac{7{,}000}{3{,}500{,}000} \times 1{,}000 = 2.00 \text{ per 1,000}$
   *(Beta mortality is 2 times higher in young adulthood)*

3. **Age 40–64**:
   - Alpha: $m_{40-64}^A = \frac{14{,}000}{3{,}500{,}000} \times 1{,}000 = 4.00 \text{ per 1,000}$
   - Beta: $m_{40-64}^B = \frac{16{,}000}{2{,}000{,}000} \times 1{,}000 = 8.00 \text{ per 1,000}$
   *(Beta mortality is 2 times higher in middle age)*

4. **Age 65+**:
   - Alpha: $m_{65+}^A = \frac{80{,}000}{2{,}000{,}000} \times 1{,}000 = 40.00 \text{ per 1,000}$
   - Beta: $m_{65+}^B = \frac{30{,}000}{500{,}000} \times 1{,}000 = 60.00 \text{ per 1,000}$
   *(Beta mortality is 1.5 times higher in older age)*

Remarkably, in **every single age group**, Country Beta suffers from substantially higher mortality than Country Alpha! The apparent advantage in the crude death rate was an artifact of age composition.

### Solution, step 3: Directly Standardized Death Rates
Using the World Standard Population ($P^S = 10{,}000{,}000$):
The formula for expected deaths under standard age distribution is:
$$E^S = \sum_x \left( m_x \cdot P_x^S \right)$$

**For Country Alpha:**
- Age 0–14: $1.00 \times 3{,}000{,}000 / 1{,}000 = 3{,}000$
- Age 15–39: $1.00 \times 3{,}500{,}000 / 1{,}000 = 3{,}500$
- Age 40–64: $4.00 \times 2{,}500{,}000 / 1{,}000 = 10{,}000$
- Age 65+: $40.00 \times 1{,}000{,}000 / 1{,}000 = 40{,}000$
- Total Expected Deaths in Standard: $3{,}000 + 3{,}500 + 10{,}000 + 40{,}000 = 56{,}500$

$$DSDR_A = \frac{56{,}500}{10{,}000{,}000} \times 1{,}000 = 5.65 \text{ per 1,000}$$

**For Country Beta:**
- Age 0–14: $3.00 \times 3{,}000{,}000 / 1{,}000 = 9{,}000$
- Age 15–39: $2.00 \times 3{,}500{,}000 / 1{,}000 = 7{,}000$
- Age 40–64: $8.00 \times 2{,}500{,}000 / 1{,}000 = 20{,}000$
- Age 65+: $60.00 \times 1{,}000{,}000 / 1{,}000 = 60{,}000$
- Total Expected Deaths in Standard: $9{,}000 + 7{,}000 + 20{,}000 + 60{,}000 = 96{,}000$

$$DSDR_B = \frac{96{,}000}{10{,}000{,}000} \times 1{,}000 = 9.60 \text{ per 1,000}$$

The Comparative Mortality Figure is:

$$CMF_{B/A} = \frac{DSDR_B}{DSDR_A} = \frac{9.60}{5.65} \approx 1.6991 \implies 1.70$$

Once age composition is standardized, Country Beta's true mortality is **$70\%$ higher** than Country Alpha's!

### Solution, step 4: Indirect Standardization and the SMR
We now perform indirect standardization on Country Beta using Country Alpha as the standard ($m_x^S = m_x^A$):
Expected deaths in Country Beta are calculated by applying Alpha's age-specific death rates to Beta's population:

$$E_B = \sum_x \left( m_x^A \cdot P_x^B \right)$$

- Age 0–14: $1.00 \times 4{,}000{,}000 / 1{,}000 = 4{,}000$
- Age 15–39: $1.00 \times 3{,}500{,}000 / 1{,}000 = 3{,}500$
- Age 40–64: $4.00 \times 2{,}000{,}000 / 1{,}000 = 8{,}000$
- Age 65+: $40.00 \times 500{,}000 / 1{,}000 = 20{,}000$
- Total Expected Deaths in Beta: $E_B = 4{,}000 + 3{,}500 + 8{,}000 + 20{,}000 = 35{,}500$

The observed deaths in Country Beta were $D_B = 65{,}000$.
The Standardized Mortality Ratio of Country Beta is:

$$SMR_B = \frac{D_B}{E_B} = \frac{65{,}000}{35{,}500} \approx 1.8310 \implies 183.1\%$$

Country Beta experienced $183.1\%$ of the deaths expected under Country Alpha's mortality regime—an excess mortality of $83.1\%$.

**Demographic Conclusion**:
This classic empirical demonstration highlights **Simpson's Paradox** in demographic statistics: although Country Beta's crude death rate is $34\%$ lower than Alpha's, its age-standardized mortality is between $70\%$ and $83\%$ higher. Country Beta's low crude death rate was entirely a demographic optical illusion created by the fact that $75\%$ of its population is under age 40, compared to only $45\%$ in Country Alpha.


### Kitagawa's Exact Decomposition of Differences Between Two Crude Rates
When comparing two crude death rates $CDR_A$ and $CDR_B$, demographers seek to quantify exactly how much of the raw difference $\Delta = CDR_B - CDR_A$ is attributable to genuine differences in age-specific mortality rates versus differences in population age composition. In 1955, Evelyn M. Kitagawa formulated an exact mathematical decomposition.

Let $m_x^A$ and $m_x^B$ be the age-specific death rates, and let $c_x^A = P_x^A / N_A$ and $c_x^B = P_x^B / N_B$ be the age-composition proportions. The crude rates are:

$$CDR_A = \sum_x m_x^A c_x^A \quad \text{and} \quad CDR_B = \sum_x m_x^B c_x^B$$

Kitagawa established the exact two-component identity:

$$CDR_B - CDR_A = \sum_x \left( \frac{c_x^A + c_x^B}{2} \right) (m_x^B - m_x^A) + \sum_x \left( \frac{m_x^A + m_x^B}{2} \right) (c_x^B - c_x^A)$$

The first summation represents the **Rate Effect** (the change in aggregate mortality caused strictly by differences in biological mortality schedules, weighted by the average age structure). The second summation represents the **Composition Effect** (the change in aggregate mortality caused strictly by differences in age composition, weighted by the average mortality schedule). The sum of the two components equals the raw difference $\Delta$ with exact algebraic precision, eliminating the arbitrary residual term found in older decomposition methods.

### The Brass Relational Logit Mortality System
In many developing regions, civil registration is incomplete, precluding direct calculation of age-specific death rates. In 1971, William Brass formulated the first **relational model life table system**, demonstrating that any empirical survival function $l(x)$ can be mathematically related to a standard reference life table $l^*(x)$ through a simple linear logit transformation.

Define the logit transformation of the survival probability $l(x)$ (with radix $l(0) = 1$):

$$\text{logit}[l(x)] = \frac{1}{2} \ln\left( \frac{1 - l(x)}{l(x)} \right) = \frac{1}{2} \ln\left( \frac{q(x)}{p(x)} \right)$$

Brass discovered the profound empirical regularity that for almost all human populations:

$$\text{logit}[l(x)] = \alpha + \beta \cdot \text{logit}[l^*(x)]$$

where:
- $\alpha$ represents the overall level of mortality. When $\alpha > 0$, the study population experiences higher overall mortality than the standard; when $\alpha < 0$, mortality is lower.
- $\beta$ represents the relationship between child mortality and adult mortality (the mortality slope). When $\beta = 1$, the age pattern of mortality is identical to the standard; when $\beta > 1$, adult mortality is elevated relative to child mortality; when $\beta < 1$, child mortality is elevated relative to adult mortality.

The Brass relational model enables demographers to graduate erratic mortality schedules and generate complete survival curves from just two empirical anchor points (such as infant mortality from birth histories and adult orphanhood reports).

### The Lee–Carter Stochastic Mortality Forecasting Model
For forecasting future mortality trends, Ronald D. Lee and Lawrence R. Carter (1992) introduced the standard stochastic model used by actuaries, social security administrations, and the United Nations. The model decomposes the matrix of log-central death rates $\ln m(x, t)$ across age $x$ and calendar year $t$:

$$\ln m(x, t) = a_x + b_x k_t + \varepsilon_{x, t}$$

where:
- $a_x$ represents the baseline general shape of the mortality schedule across age, estimated as the empirical temporal average: $a_x = \frac{1}{T} \sum_t \ln m(x, t)$.
- $k_t$ is the time-varying mortality index tracking the overall secular decline in mortality over time.
- $b_x$ indicates the sensitivity of mortality at age $x$ to changes in the overall index $k_t$. Ages where $b_x$ is large experience rapid mortality reductions as $k_t$ declines.
- $\varepsilon_{x, t}$ represents mean-zero idiosyncratic historical error.

The model parameters are estimated via Singular Value Decomposition (SVD) of the matrix of centered log-rates, and the time index $k_t$ is modeled as a random walk with drift:

$$k_t = k_{t-1} + d + e_t$$

This formulation provides probabilistic confidence intervals for future life expectancy projections.

## Fully worked question 2: Cause-Deleted Competing Risks Analysis for Cardiovascular Disease

### Question
In a high-income nation, actuarial mortality surveillance models the impact of eliminating cardiovascular disease (CVD) upon survival schedules. The total quinquennial survival probabilities ($_5 p_x$) and the proportion of deaths attributable to cardiovascular disease ($R_{\text{CVD}}(x) = \frac{D_x^{\text{CVD}}}{D_x}$) across adult age intervals are given below:

| Age Interval ($x$ to $x+5$) | Total Survival Prob ($_5 p_x$) | CVD Death Proportion ($R_{\text{CVD}}(x)$) |
| :---: | :---: | :---: |
| **50–54** | $0.9700$ | $0.250$ |
| **55–59** | $0.9500$ | $0.300$ |
| **60–64** | $0.9200$ | $0.350$ |
| **65–69** | $0.8700$ | $0.400$ |
| **70–74** | $0.8000$ | $0.450$ |

1. Formulate the competing risks assumption and state the mathematical relationship between the cause-deleted survival probability $_5 p_x^{-\text{CVD}}$ and the all-cause survival probability $_5 p_x$.
2. Compute the cause-deleted five-year survival probability $_5 p_x^{-\text{CVD}}$ and five-year mortality probability $_5 q_x^{-\text{CVD}}$ for each age cohort.
3. For a hypothetical cohort of $100{,}000$ individuals reaching exact age 50, calculate the cumulative probability of surviving to exact age 75 under the observed mortality regime ($S(75) / S(50)$) and under the counterfactual regime where cardiovascular disease is completely eradicated ($S^{-\text{CVD}}(75) / S^{-\text{CVD}}(50)$).

### Solution, step 1: Competing Risks Formulation
Under the Chiang and Keyfitz assumption of independent competing risks, the forces of mortality are additive:

$$\mu(x) = \mu_{\text{CVD}}(x) + \mu_{-\text{CVD}}(x)$$

Assuming that the ratio of the cause-specific force of mortality to the total force of mortality is constant across each five-year age interval:

$$R_{\text{CVD}}(x) = \frac{\mu_{\text{CVD}}(t)}{\mu(t)} = \text{constant} \quad \forall t \in [x, x+5)$$

The cause-deleted survival probability is:

$$_5 p_x^{-\text{CVD}} = \exp\left( -\int_x^{x+5} \mu_{-\text{CVD}}(t) \, dt \right) = \exp\left( -\int_x^{x+5} [1 - R_{\text{CVD}}(x)] \mu(t) \, dt \right)$$

$$\_5 p_x^{-\text{CVD}} = \left[ \exp\left( -\int_x^{x+5} \mu(t) \, dt \right) \right]^{1 - R_{\text{CVD}}(x)} = \left( _5 p_x \right)^{1 - R_{\text{CVD}}(x)}$$

The cause-deleted mortality probability is:

$$_5 q_x^{-\text{CVD}} = 1 - {_5 p_x^{-\text{CVD}}}$$

### Solution, step 2: Compute Cause-Deleted Survival Probabilities by Age Group
We apply the power formula to each interval:
1. **Age 50–54**:
   - Power: $1 - R = 1 - 0.250 = 0.750$
   - $_5 p_{50}^{-\text{CVD}} = (0.9700)^{0.750} = \exp(0.750 \times \ln(0.9700)) = \exp(0.750 \times -0.030459) = \exp(-0.022844) \approx 0.977415$
   - $_5 q_{50}^{-\text{CVD}} = 1 - 0.977415 = 0.022585$

2. **Age 55–59**:
   - Power: $1 - R = 1 - 0.300 = 0.700$
   - $_5 p_{55}^{-\text{CVD}} = (0.9500)^{0.700} = \exp(0.700 \times -0.051293) = \exp(-0.035905) \approx 0.964732$
   - $_5 q_{55}^{-\text{CVD}} = 1 - 0.964732 = 0.035268$

3. **Age 60–64**:
   - Power: $1 - R = 1 - 0.350 = 0.650$
   - $_5 p_{60}^{-\text{CVD}} = (0.9200)^{0.650} = \exp(0.650 \times -0.083382) = \exp(-0.054198) \approx 0.947244$
   - $_5 q_{60}^{-\text{CVD}} = 1 - 0.947244 = 0.052756$

4. **Age 65–69**:
   - Power: $1 - R = 1 - 0.400 = 0.600$
   - $_5 p_{65}^{-\text{CVD}} = (0.8700)^{0.600} = \exp(0.600 \times -0.139262) = \exp(-0.083557) \approx 0.919835$
   - $_5 q_{65}^{-\text{CVD}} = 1 - 0.919835 = 0.080165$

5. **Age 70–74**:
   - Power: $1 - R = 1 - 0.450 = 0.550$
   - $_5 p_{70}^{-\text{CVD}} = (0.8000)^{0.550} = \exp(0.550 \times -0.223144) = \exp(-0.122729) \approx 0.884501$
   - $_5 q_{70}^{-\text{CVD}} = 1 - 0.884501 = 0.115499$

### Solution, step 3: Cumulative Survival from Age 50 to Age 75
The cumulative probability of surviving from exact age 50 to exact age 75 is the product of the five successive five-year survival probabilities:

**Under the Observed (All-Cause) Mortality Regime:**

$$\frac{S(75)}{S(50)} = \prod_{k=0}^4 {_5 p_{50 + 5k}} = 0.9700 \times 0.9500 \times 0.9200 \times 0.8700 \times 0.8000$$

Multiplying step by step:
- $0.9700 \times 0.9500 = 0.92150$
- $0.92150 \times 0.9200 = 0.84778$
- $0.84778 \times 0.8700 = 0.73757$
- $0.73757 \times 0.8000 = 0.590055 \approx 0.5901 \implies 59.01\%$

Under observed conditions, $59.01\%$ of 50-year-olds survive to celebrate their 75th birthday ($40.99\%$ die before age 75).

**Under the Cause-Deleted Regime (CVD Eradicated):**

$$\frac{S^{-\text{CVD}}(75)}{S^{-\text{CVD}}(50)} = \prod_{k=0}^4 {_5 p_{50 + 5k}^{-\text{CVD}}}$$

$$\frac{S^{-\text{CVD}}(75)}{S^{-\text{CVD}}(50)} = 0.977415 \times 0.964732 \times 0.947244 \times 0.919835 \times 0.884501$$

Multiplying step by step:
- $0.977415 \times 0.964732 = 0.942944$
- $0.942944 \times 0.947244 = 0.893198$
- $0.893198 \times 0.919835 = 0.821594$
- $0.821594 \times 0.884501 = 0.726699 \approx 0.7267 \implies 72.67\%$

**Actuarial Interpretation**:
Eradicating cardiovascular disease elevates the 25-year survival probability from $59.01\%$ to $72.67\%$—an absolute gain of $13.66$ percentage points. In a cohort of $100{,}000$ 50-year-olds, $72{,}670$ survive to age 75 instead of $59{,}006$, preserving $13{,}664$ lives over this 25-year window.


### Epidemiological Transition Theory and the Changing Architecture of Causes of Death
To place mortality measures and cause-deleted life tables into long-term historical context, demographers rely upon Abdel Omran's celebrated **Epidemiological Transition Theory** (1971). Omran conceptualized human mortality history as progressing through three distinct evolutionary stages, subsequently expanded by S. Jay Olshansky and A. Brian Ault (1986) into four stages:

1. **The Age of Pestilence and Famine**: Characterized by catastrophic, volatile mortality driven by infectious pandemics (such as the Black Death, cholera, typhus, and smallpox), endemic tuberculosis, and malnutrition. Life expectancy at birth fluctuated violently between twenty and thirty-five years, and children under age five accounted for nearly half of all deaths.
2. **The Age of Receding Pandemics**: Spanning the mid-nineteenth through early twentieth centuries in industrializing territories. Public health engineering—including piped chlorinated water supplies, modern municipal sewage treatment, pasteurization of commercial milk supplies, swamp drainage for malaria control, and improved residential ventilation—dramatically curtailed waterborne and airborne pathogens prior to the widespread commercial availability of antibiotics. Mortality stabilized, and life expectancy rose steadily toward fifty and sixty years.
3. **The Age of Degenerative and Man-Made Diseases**: Infectious diseases retreated to minor causes of death, replaced by chronic degenerative conditions associated with biological aging, sedentary occupations, high-calorie processed diets, and tobacco usage. Cardiovascular diseases (coronary artery disease, myocardial infarction, ischemic stroke) and malignant neoplasms (cancers) became responsible for over seventy percent of all recorded deaths.
4. **The Age of Delayed Degenerative Diseases**: Emerging in the late twentieth century across advanced industrial economies. Breakthroughs in medical technology (such as coronary artery bypass grafting, statins, antihypertensive pharmacotherapy, thrombolysis, and targeted oncology treatments), coupled with dramatic declines in adult tobacco smoking, postponed the fatal onset of cardiovascular disease and stroke into extreme old age. The mortality curve underwent substantial rectangularization, pushing median age at death into the eighties and nineties.

Understanding these epidemiological transitions is essential for mathematical demographers constructing Cause-Deleted Life Tables. In Stage 3 societies, eliminating cardiovascular disease generates immense gains in life expectancy because deaths occur in mid-adulthood. In Stage 4 societies, eliminating a single disease yields smaller gains because older individuals suffer from multiple competing comorbidities (frailty, cognitive dementia, multiple organ failure), so that preventing a cardiovascular death quickly exposes the surviving individual to mortality from another degenerative pathology.


### Poisson Log-Linear Regression for Age-Specific Death Rates and Excess Mortality
In modern public health surveillance and biostatistical modeling, age-specific mortality is modeled using Generalized Linear Models (GLMs), specifically **Poisson Log-Linear Regression**.

Let D_x denote the observed number of deaths in age group x, and let P_x denote the person-years of exposure. Because death is a rare event occurring within a large exposed population, the count of deaths follows a Poisson distribution:

$$D_x \sim \text{Poisson}(\mu_x \cdot P_x)$$

where mu_x is the true underlying mortality rate. Taking the natural logarithm of the expected death count:

$$\ln(\mathbb{E}[D_x]) = \ln(P_x) + \ln(\mu_x)$$

Here, ln(P_x) enters the regression model as an **offset variable** with a fixed coefficient of unity, transforming the model into a regression on log-rates.
By expressing ln(mu_x) as a linear combination of age factors, calendar periods, sex indicators, and environmental covariates, statisticians can estimate adjusted rate ratios and test epidemiological hypotheses with full maximum likelihood rigor.

#### Measuring Excess Mortality in Epidemiological Crises
During infectious pandemic waves (such as the 1918 influenza pandemic or the 2020–2022 COVID-19 pandemic) or extreme heatwaves, registered cause-of-death reporting is frequently lagged, under-reported, or distorted by diagnostic testing capacity constraints. Demographers measure the true lethal impact through **Excess Mortality**.

Excess mortality is defined as the difference between the total observed deaths from all causes during a crisis period and the baseline expected deaths projected from pre-crisis historical seasonal trends:

$$\text{Excess Deaths} = D_{\text{observed}} - \hat{D}_{\text{expected}}$$

Because total all-cause mortality requires no cause-of-death certification, excess mortality provides an objective, unvarnished measure of total pandemic mortality, capturing both direct viral fatalities and indirect deaths caused by healthcare system collapse.

## Fully worked question 3: Multi-Component Separation of Infant, Neonatal, and Post-Neonatal Hazards

### Question
A provincial health ministry in a developing territory establishes a digital vital registration surveillance system. During calendar year 2024, the civil registration office records:
- Total registered live births: $B_{2024} = 250{,}000$
- Registered live births in preceding year: $B_{2023} = 240{,}000$
- Total deaths of infants under one year of age ($D_0$): $11{,}250$
- Deaths occurring during days 0–6 of life (early neonatal, $D_{\text{en}}$): $4{,}500$
- Deaths occurring during days 7–27 of life (late neonatal, $D_{\text{ln}}$): $2{,}500$
- Deaths occurring during days 28–364 of life (post-neonatal, $D_{\text{pn}}$): $4{,}250$

1. Compute the unadjusted Infant Mortality Rate ($IMR$), the Neonatal Mortality Rate ($NMR$), the Early Neonatal Mortality Rate ($ENMR$), and the Post-Neonatal Mortality Rate ($PNMR$), all expressed per $1{,}000$ live births. Verify the additive decomposition.
2. Given that historical record linkage establishes an infant separation factor of $f = 0.78$ (indicating that $78\%$ of infant deaths in 2024 were born in 2024, and $22\%$ were born in 2023), calculate the cohort-adjusted Infant Mortality Rate.
3. Formulate the public health diagnosis based on the ratio $\frac{NMR}{IMR}$ and recommend strategic healthcare interventions.

### Solution, step 1: Compute Mortality Rates and Verify Additive Decomposition
All basic rates use registered live births $B_{2024} = 250{,}000$ in the denominator:

1. **Early Neonatal Mortality Rate ($ENMR$, days 0–6)**:
   $$ENMR = \frac{D_{\text{en}}}{B_{2024}} \times 1{,}000 = \frac{4{,}500}{250{,}000} \times 1{,}000 = 18.00 \text{ per 1,000 live births}$$

2. **Late Neonatal Mortality Rate ($LNMR$, days 7–27)**:
   $$LNMR = \frac{D_{\text{ln}}}{B_{2024}} \times 1{,}000 = \frac{2{,}500}{250{,}000} \times 1{,}000 = 10.00 \text{ per 1,000 live births}$$

3. **Total Neonatal Mortality Rate ($NMR$, days 0–27)**:
   $$D_{\text{neonatal}} = D_{\text{en}} + D_{\text{ln}} = 4{,}500 + 2{,}500 = 7{,}000$$
   $$NMR = \frac{7{,}000}{250{,}000} \times 1{,}000 = 28.00 \text{ per 1,000 live births}$$
   Notice that $ENMR + LNMR = 18.00 + 10.00 = 28.00 = NMR$.

4. **Post-Neonatal Mortality Rate ($PNMR$, days 28–364)**:
   $$PNMR = \frac{D_{\text{pn}}}{B_{2024}} \times 1{,}000 = \frac{4{,}250}{250{,}000} \times 1{,}000 = 17.00 \text{ per 1,000 live births}$$

5. **Total Infant Mortality Rate ($IMR$)**:
   $$IMR = \frac{D_0}{B_{2024}} \times 1{,}000 = \frac{11{,}250}{250{,}000} \times 1{,}000 = 45.00 \text{ per 1,000 live births}$$

**Verification of Additive Identity:**

$$NMR + PNMR = 28.00 + 17.00 = 45.00 = IMR$$

The mathematical decomposition is verified.

### Solution, step 2: Calculate Cohort-Adjusted Infant Mortality Rate
Because annual births expanded from $240{,}000$ in 2023 to $250{,}000$ in 2024, infant deaths in 2024 drew from two birth cohorts. Using separation factor $f = 0.78$:
The adjusted exposure base is:

$$B_{\text{adjusted}} = f \cdot B_{2024} + (1 - f) \cdot B_{2023}$$

$$B_{\text{adjusted}} = 0.78 \times 250{,}000 + 0.22 \times 240{,}000 = 195{,}000 + 52{,}800 = 247{,}800$$

The cohort-adjusted Infant Mortality Rate is:

$$IMR_{\text{adjusted}} = \frac{D_0}{B_{\text{adjusted}}} \times 1{,}000 = \frac{11{,}250}{247{,}800} \times 1{,}000 \approx 45.40 \text{ per 1,000 live births}$$

Because the preceding cohort was slightly smaller ($240{,}000$), the unadjusted rate ($45.00$) slightly understated the true cohort mortality risk by $0.40$ per $1{,}000$.

### Solution, step 3: Epidemiological Ratio and Policy Diagnosis
We evaluate the structural proportion of neonatal deaths:

$$\frac{NMR}{IMR} = \frac{28.00}{45.00} = 0.6222 \implies 62.22\%$$

Early neonatal deaths alone account for:

$$\frac{ENMR}{IMR} = \frac{18.00}{45.00} = 0.4000 \implies 40.00\%$$

**Epidemiological Diagnosis**:
1. Over $62\%$ of all infant deaths occur in the first 28 days of life, and $40\%$ occur in the first 7 days.
2. In early stages of public health development, infant mortality is dominated by post-neonatal deaths ($PNMR > 60\%$) driven by infectious diarrhea, water-borne pathogens, and pneumonia. As clean water, oral rehydration therapy, and immunization expand, post-neonatal deaths collapse rapidly.
3. When neonatal mortality accounts for $>60\%$ of total infant deaths (as in this province), further progress cannot be achieved through general child health programs alone. The primary bottleneck has shifted to **obstetrical and perinatal care**: maternal nutrition, emergency obstetrical facilities, trained birth attendants, sterile cord clamping, neonatal resuscitation, and specialized neonatal intensive care units (NICUs) for preterm neonates.
