#!/usr/bin/env python3
"""
Generate Units 1 and 2 of Epidemiological Statistics with high academic depth.
"""
from pathlib import Path

OUT_DIR = Path("publishing/drafts/statistics-probability-epidemiological-statistics")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# UNIT 1
# -------------------------------------------------------------
unit1 = r"""# Unit 1: Foundations of Epidemiology, Surveillance & Measures of Disease Frequency

Epidemiology represents the core quantitative foundation of public health and preventive medicine. As a rigorous scientific discipline, it investigates the distribution, historical patterns, and etiologic determinants of health-related states or events across specified populations, applying these discoveries to control disease and optimize human welfare. Unlike clinical medicine, where the diagnostic and therapeutic focus is fixed upon the individual patient, the primary unit of observation in epidemiological statistics is the population. In this opening unit, we trace the conceptual genesis of epidemiologic reasoning, formalize the mathematical taxonomy of open and closed cohorts, establish rigorous metrics of person-time accounting, examine the mathematical relationship linking incidence and prevalence under stationary dynamic equilibrium, contrast direct and indirect standardization techniques, and evaluate the architectural designs of public health surveillance systems.

## 1.1 Historical Evolution, Epidemiologic Paradigms, and Population Definitions

The historical emergence of epidemiologic thinking represents an intellectual transition from superstitious or miasmatic conceptions of illness toward empirical, population-based causal reasoning. Hippocrates of Kos (c. 460–370 BCE) first proposed in *On Airs, Waters, and Places* that human disease is shaped by environmental circumstances—including seasonal climate, water sources, and topography—rather than divine retribution. However, quantitative population epidemiology began in earnest in seventeenth-century London with John Graunt (1620–1674). In his seminal *Natural and Political Observations Made upon the Bills of Mortality* (1662), Graunt constructed the first rudimentary life tables, observed recurring statistical regularities in infant mortality and sex ratios at birth, and demonstrated that aggregate mortality patterns exhibit striking mathematical stability despite individual unpredictability.

In the mid-nineteenth century, William Farr (1807–1883), serving as the first compiler of statistical abstracts in the General Register Office of England and Wales, transformed routine vital statistics into a powerful instrument of epidemiologic surveillance. Farr established systemic case definitions, calculated cause-specific mortality rates across distinct occupational groups, and articulated what is now termed *Farr’s Law*: an epidemic outbreak tends to rise and fall in a roughly symmetrical bell-shaped curve. Concurrently, Ignaz Semmelweis (1818–1865) conducted pioneering intervention studies in Vienna, demonstrating that chlorine handwashing among obstetricians drastically reduced maternal puerperal fever mortality from eighteen percent to less than two percent.

The paradigm defining modern field epidemiology was established by John Snow (1813–1858) during the 1854 cholera epidemics in London. Rejecting the prevailing miasma theory, Snow hypothesized waterborne fecal-oral transmission. In his celebrated investigation of the Broad Street pump outbreak in Soho, Snow mapped cholera fatalities geographically, identifying a dramatic spatial clustering centered precisely on a single public water pump. Crucially, Snow conducted a natural experiment in south London: two competing municipal water companies, the Lambeth Company and the Southwark and Vauxhall Company, delivered water to houses located on the very same streets. Because Lambeth had moved its intake pipe upriver to Thames water free of London sewage, whereas Southwark and Vauxhall drew water downstream, Snow compared cholera mortality rates between households sharing identical socio-demographic environments but differing in water supply. His comparative table demonstrated that customers of Southwark and Vauxhall suffered a cholera death rate more than eight times higher than customers of the Lambeth Company, providing conclusive empirical evidence of waterborne transmission decades before Robert Koch isolated *Vibrio cholerae*.

In modern epidemiological statistics, we formalize the substrate of observation by distinguishing three fundamental population types:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Population Category</th><th>Boundary Definition</th><th>Inflow &amp; Outflow Dynamics</th><th>Typical Epidemiological Setting</th></tr>
</thead>
<tbody>
<tr><td><strong>Closed Population (Cohort)</strong></td><td>Defined by a single defining historical event at baseline (e.g., date of surgery or vaccination).</td><td>No additions permitted over time; membership decreases exclusively through death, migration, or loss to follow-up.</td><td>Clinical trial cohorts, wartime military exposures, birth cohorts.</td></tr>
<tr><td><strong>Fixed Cohort with Attrition</strong></td><td>Baseline entry window fixed; loss to follow-up and competing mortality deplete the denominator.</td><td>Monotonically declining person-time at risk; requires life-table or survival tracking.</td><td>Longitudinal observational studies with incomplete ascertainment.</td></tr>
<tr><td><strong>Open (Dynamic) Population</strong></td><td>Defined by an ongoing geographic, administrative, or biological state (e.g., residents of Dhaka city).</td><td>Continuous entry (birth, immigration) and continuous exit (death, emigration, cure).</td><td>Municipal health registries, national cancer registries, vital statistics.</td></tr>
</tbody>
</table></div>

Understanding these definitions is essential because the mathematical formulation of disease frequency depends fundamentally on whether the denominator reflects a static cohort followed through time or an open dynamic population experiencing continuous demographic flux.

## 1.2 Measures of Disease Frequency: Cumulative Incidence, Incidence Rate, and Person-Time

To quantify the occurrence of health outcomes in a target population, epidemiologists rely on three distinct mathematical structures: counts, proportions, and true rates. A **count** is simply the absolute number of events observed in a specified window; although vital for hospital resource allocation and logistical planning, counts lack a population denominator and cannot characterize individual risk or comparative disease force.

A **risk** or **cumulative incidence** ($CI$), also termed the **incidence proportion**, is the probability that an individual initially free of the disease experiences the outcome during a designated follow-up interval $[0, \Delta t]$. Formally, in a closed cohort of $N_0$ disease-free individuals observed throughout the entire interval without competing mortality or loss to follow-up:

$$CI(\Delta t) = \frac{d}{N_0}$$

where $d$ is the number of incident cases occurring during $[0, \Delta t]$. Cumulative incidence is dimensionless, strictly bounded within the unit interval $[0, 1]$, and mathematically interpretable as an empirical probability. However, cumulative incidence assumes that all $N_0$ individuals are tracked over the exact same duration. When members enter at staggered calendar dates, migrate away, or die from competing hazards, cumulative incidence cannot be calculated by simple division.

In open dynamic populations or cohorts with unequal follow-up durations, the fundamental measure of disease occurrence is the **incidence rate** ($IR$), also known as the **incidence density** or **hazard rate**. The incidence rate measures the instantaneous velocity of disease onset per unit of person-time at risk:

$$IR = \lim_{\Delta t \to 0} \frac{P(\text{event occurs in } [t, t + \Delta t) \mid \text{event-free at } t)}{\Delta t}$$

In empirical epidemiology across an observational interval, the sample incidence rate is estimated by dividing the count of newly diagnosed incident cases $d$ by the total sum of person-time accumulated across all individuals while at risk:

$$\widehat{IR} = \frac{d}{\sum_{i=1}^n \Delta t_i} = \frac{d}{PT}$$

where $\Delta t_i$ is the time contributed by the $i$-th individual before developing the disease, becoming lost to follow-up, dying from competing causes, or reaching the administrative end of the study. Person-time is expressed in units such as person-years ($PY$), person-months, or person-days.

The dimensional units of the incidence rate are $[\text{Time}]^{-1}$. Consequently, an incidence rate is not a probability; its numerical value can exceed $1.0$ if the time unit is chosen sufficiently large (e.g., an incidence rate of $1.5$ cases per person-century).

### Mathematical Relationship Between Incidence Rate and Cumulative Incidence
Consider a closed cohort subject to a constant instantaneous hazard rate $\lambda$ across the follow-up interval $[0, T]$. Let $S(t) = P(T > t)$ denote the probability of remaining disease-free up to time $t$. By definition of the instantaneous hazard:

$$\lambda(t) = -\frac{1}{S(t)} \frac{dS(t)}{dt} = -\frac{d}{dt} \ln S(t)$$

Assuming $\lambda(t) = \lambda$ is constant over $t \in [0, T]$ and integrating with initial boundary condition $S(0) = 1$:

$$\int_0^T \lambda \, dt = -\int_0^T d \ln S(t) \implies \lambda T = -\ln S(T) \implies S(T) = \exp(-\lambda T)$$

Because cumulative incidence $CI(T)$ represents the complementary probability of developing the disease by time $T$:

$$CI(T) = 1 - S(T) = 1 - \exp(-\lambda T)$$

When the disease is rare or the observation window is short such that $\lambda T \ll 1$, Taylor series expansion yields:

$$1 - \exp(-\lambda T) \approx 1 - (1 - \lambda T) = \lambda T$$

This linear approximation confirms that for rare health outcomes, cumulative incidence is approximately equal to the product of the incidence rate and the duration of observation. When rates are high or observation times are extended, the full exponential transformation must be utilized to preserve the mathematical constraint that probabilities cannot exceed unity.

## 1.3 Prevalence, Duration, and Stationary State Dynamic Equilibrium

While incidence measures the rate of new flow into the disease state, **prevalence** measures the existing stock of disease within a population at a designated cross-section of time. We distinguish between two formulations:
1. **Point Prevalence** ($P$): The proportion of a population that possesses the disease at a single specific instant $t_0$:
   $$P(t_0) = \frac{\text{Number of existing cases at } t_0}{\text{Total population size at } t_0}$$
2. **Period Prevalence**: The proportion of a population exhibiting the disease at any point during a specified calendar interval (e.g., annual period prevalence), combining point prevalence at baseline with subsequent incident cases.

Prevalence is a dimensionless proportion bounded in $[0, 1]$. It depends simultaneously upon the rate at which new cases develop (incidence) and the duration for which individuals survive with the condition before recovery or death.

### Derivation of the Fundamental Steady-State Equilibrium Identity
Consider a stationary population in dynamic equilibrium, where the total population size $N$, the number of diseased individuals $D$, and the number of healthy individuals $H = N - D$ remain constant over time. Let $I$ denote the constant incidence rate among the healthy susceptible population, and let $\bar{T}_D$ denote the mean duration of the disease state before cure or death.

Because the system is stationary, the inflow of new incident cases into the diseased pool per unit time must exactly equal the outflow of cases leaving through recovery or mortality:

$$\text{Inflow} = I \times H = I \times (N - D)$$

Under an exponential survival law in the diseased state with exit rate $\gamma = 1 / \bar{T}_D$, the outflow per unit time is:

$$\text{Outflow} = \gamma \times D = \frac{D}{\bar{T}_D}$$

Equating inflow and outflow under dynamic equilibrium:

$$I (N - D) = \frac{D}{\bar{T}_D} \implies I \cdot \bar{T}_D = \frac{D}{N - D}$$

Notice that the point prevalence is $P = D / N$, which implies that the odds of prevalence is:

$$\text{Prevalence Odds} = \frac{P}{1 - P} = \frac{D / N}{1 - D / N} = \frac{D}{N - D}$$

Therefore, we arrive at the exact mathematical identity governing stationary epidemiology:

$$\frac{P}{1 - P} = I \times \bar{T}_D$$

Solving for prevalence $P$ explicitly:

$$P = \frac{I \cdot \bar{T}_D}{1 + I \cdot \bar{T}_D}$$

When the disease is rare in the general population ($P < 0.05$), the denominator $1 + I \cdot \bar{T}_D \approx 1$, yielding the classical epidemiological approximation:

$$P \approx I \times \bar{T}_D$$

This relationship illustrates that therapeutic interventions that prolong survival without achieving complete biological cure (such as antiretroviral therapy in HIV or insulin in type 1 diabetes) will paradoxically increase disease prevalence, even when preventive public health measures successfully reduce incidence. Conversely, a rapidly lethal epidemic may exhibit a low point prevalence despite astronomical incidence rates.

## 1.4 Age-Standardization: Direct and Indirect Methods, SMR, and Reference Populations

Because mortality and chronic disease incidence rates rise precipitously with advancing age, comparing crude summary rates across distinct populations can be profoundly misleading if the underlying demographic age pyramids differ. For example, a retirement community may exhibit a crude all-cause mortality rate far higher than an impoverished urban slum, purely because the retirement community has a much larger proportion of elderly residents.

To remove the confounding artifact of disparate age structures, epidemiologists employ **standardization**.

### Direct Age-Standardization
In direct standardization, we apply the stratum-specific rates observed in the study population to the demographic age distribution of an external, pre-specified **standard population** (such as the WHO World Standard Population).

Let the age span be partitioned into $K$ mutually exclusive strata $k = 1, 2, \dots, K$. For each stratum $k$:
- $r_k = d_k / n_k$ is the observed stratum-specific rate in the study population.
- $N_k^*$ is the number of individuals in stratum $k$ within the standard population.
- $N^* = \sum_{k=1}^K N_k^*$ is the total size of the standard population.
- $w_k^* = N_k^* / N^*$ is the proportion of the standard population residing in stratum $k$, satisfying $\sum w_k^* = 1$.

The **Directly Standardized Rate** ($DSR$) is defined as the weighted average:

$$DSR = \sum_{k=1}^K w_k^* r_k = \frac{\sum_{k=1}^K N_k^* r_k}{N^*}$$

Assuming the observed death count in each stratum follows an independent Poisson distribution $d_k \sim \text{Poisson}(n_k r_k)$, the variance of $r_k$ is $\text{Var}(r_k) = r_k / n_k$. Because strata are independent, the sampling variance of the $DSR$ is:

$$\text{Var}(DSR) = \sum_{k=1}^K (w_k^*)^2 \text{Var}(r_k) = \sum_{k=1}^K (w_k^*)^2 \frac{r_k}{n_k} = \sum_{k=1}^K (w_k^*)^2 \frac{d_k}{n_k^2}$$

A $100(1 - \alpha)\%$ asymptotic Wald confidence interval for the $DSR$ is:

$$DSR \pm z_{1 - \alpha/2} \sqrt{\text{Var}(DSR)}$$

### Indirect Age-Standardization and the Standardized Mortality Ratio (SMR)
When the study population is small, stratum-specific death counts $d_k$ may be sparse or subject to substantial Poisson variability. In such circumstances, direct standardization yields unstable rates. Instead, **indirect standardization** applies the stable stratum-specific rates of a large reference population to the observed demographic structure of the study group.

Let $R_k^*$ denote the stratum-specific rate in the standard reference population, and let $n_k$ denote the person-time observed in stratum $k$ of the study group. The **expected number of events** ($E$) in the study population, had it experienced the reference rates, is:

$$E = \sum_{k=1}^K n_k R_k^*$$

Let $O = \sum_{k=1}^K d_k$ denote the total observed number of events in the study population. The **Standardized Mortality Ratio** ($SMR$) is defined as:

$$SMR = \frac{O}{E} = \frac{\sum_{k=1}^K d_k}{\sum_{k=1}^K n_k R_k^*}$$

If $SMR = 1.0$, observed mortality matches reference expectations; if $SMR = 1.35$, the study group experiences a thirty-five percent excess mortality after controlling for age composition. Treating $E$ as a fixed constant and modeling $O \sim \text{Poisson}(\mu)$, the asymptotic variance of $\ln(SMR)$ by the delta method is:

$$\text{Var}(\ln SMR) \approx \frac{1}{O}$$

yielding the log-transformed $95\%$ confidence interval:

$$SMR \cdot \exp\left( \pm 1.96 \frac{1}{\sqrt{O}} \right) = \left[ SMR \cdot e^{-1.96/\sqrt{O}}, \, SMR \cdot e^{1.96/\sqrt{O}} \right]$$

## 1.5 Public Health Surveillance Systems: Architecture, Completeness, and Sensitivity

Public health surveillance is defined by the World Health Organization as the continuous, systematic collection, analysis, interpretation, and dissemination of health-related data for planning, implementation, and evaluation of public health practice. A surveillance system operates as an information loop: data collected at primary clinical interfaces must be synthesized rapidly to inform policy interventions and disease outbreak countermeasures.

We classify public health surveillance into core operational modalities:
1. **Passive Surveillance**: Routine, mandatory reporting by healthcare providers, diagnostic laboratories, and hospitals of designated notifiable infectious diseases (e.g., cholera, tuberculosis, measles). Passive systems are inexpensive and cover broad geographic jurisdictions, but suffer from systemic under-reporting, diagnostic delays, and inconsistent case verification.
2. **Active Surveillance**: Public health personnel physically visit clinics, contact laboratory directors, and review medical registries to identify every diagnosed case during an active outbreak or disease elimination campaign (e.g., wild poliovirus surveillance). Active surveillance achieves high sensitivity and completeness, but demands substantial administrative and financial resources.
3. **Sentinel Surveillance**: A pre-selected network of reporting healthcare facilities (sentinel clinics) reporting detailed diagnostic data on specific conditions (such as influenza-like illness). Rather than attempting complete national enumeration, sentinel systems provide high-quality, timely tracking of viral strain evolution and proportional disease burdens.
4. **Syndromic Surveillance**: Real-time automated monitoring of pre-diagnostic clinical data streams—including emergency room chief complaints, pharmacy sales of over-the-counter anti-diarrheal medications, and ambulance dispatch logs—to detect early signals of bioterrorism or novel viral emergence before laboratory confirmation.

The statistical performance of a surveillance system is evaluated along critical technical axes:
- **Sensitivity**: The proportion of all true cases in the population that are successfully captured by the surveillance registry.
- **Positive Predictive Value (PPV)**: The proportion of reported cases that represent true biological disease after diagnostic auditing.
- **Timeliness**: The time lag between the biological onset of symptoms, clinical presentation, laboratory verification, and administrative reporting.
- **Completeness and Capture-Recapture Estimation**: To estimate the true population disease count $N$ when surveillance lists are incomplete, epidemiologists employ two-source **capture-recapture methods** (the Lincoln-Petersen estimator). If list 1 captures $n_1$ cases, list 2 captures $n_2$ cases, and $m$ individuals appear simultaneously on both independent lists, the total population case count is estimated by:
  $$\widehat{N} = \frac{n_1 n_2}{m}$$
  with Chapman's finite-sample unbiasing correction:
  $$\widehat{N}_C = \frac{(n_1 + 1)(n_2 + 1)}{m + 1} - 1$$

Statistical monitoring in surveillance often employs quality control algorithms, such as cumulative sum (CUSUM) charts and Serfling regression models, to detect aberrations above seasonal baseline activity.

## Fully worked question 1: Person-Time Accounting, Incidence Density & Cumulative Incidence

### Question
A specialized cardiovascular occupational epidemiology study tracks an initial cohort of $N_0 = 10$ high-stress industrial managers over a 5-year observation period (calendar years 2021 to 2025 inclusive). Each manager enters the study on January 1, 2021, and is tracked until they develop acute myocardial infarction (AMI), withdraw from the study, or reach the study termination date of December 31, 2025. The individual event timelines recorded in years from baseline are:
- Subjects 1, 2, and 3 remain healthy and event-free throughout the entire 5.0 years.
- Subject 4 develops an AMI at $t = 1.5$ years.
- Subject 5 is lost to follow-up (migrated abroad) at $t = 2.0$ years without AMI.
- Subject 6 develops an AMI at $t = 3.2$ years.
- Subject 7 withdraws consent at $t = 3.5$ years without AMI.
- Subject 8 dies in a motor vehicle accident (competing non-cardiac death) at $t = 4.0$ years.
- Subject 9 develops an AMI at $t = 4.5$ years.
- Subject 10 remains event-free throughout the entire 5.0 years.

1. Calculate the total person-years ($PY$) at risk contributed by this cohort, and compute the empirical incidence rate ($\widehat{IR}$) of AMI per 1,000 person-years.
2. Assuming a constant hazard rate equal to the estimated incidence rate, calculate the 5-year cumulative incidence of AMI ($CI(5)$) and compare it against the naive crude proportion of cases observed.
3. Compute the 95% Poisson confidence interval for the incidence rate.

### Solution, step 1: Tally cumulative person-years and calculate incidence density
To calculate the total person-years at risk, we sum the exact follow-up durations contributed by each individual prior to disease onset, censoring, or study conclusion:

$$PT = \sum_{i=1}^{10} \Delta t_i = 5.0 + 5.0 + 5.0 + 1.5 + 2.0 + 3.2 + 3.5 + 4.0 + 4.5 + 5.0 = 38.7 \text{ person-years}$$

During these $38.7$ person-years of observation, exactly $d = 3$ incident cases of acute myocardial infarction occurred (Subjects 4, 6, and 9). The empirical incidence rate is:

$$\widehat{IR} = \frac{d}{PT} = \frac{3}{38.7} \approx 0.077519 \text{ cases per person-year}$$

Expressing this rate per 1,000 person-years:

$$\widehat{IR} = 0.077519 \times 1000 \approx 77.52 \text{ cases per 1,000 person-years}$$

### Solution, step 2: Exponential survival model for cumulative incidence vs naive proportion
Under the exponential model with constant hazard rate $\lambda = \widehat{IR} = 0.077519 \text{ yr}^{-1}$, the estimated 5-year cumulative incidence is:

$$CI(5) = 1 - \exp(-\lambda \cdot T) = 1 - \exp(-0.077519 \times 5) = 1 - \exp(-0.387597) \approx 1 - 0.678683 = 0.3213 \quad (32.13\%)$$

By contrast, the naive crude proportion simply divides the 3 cases by the initial 10 participants:

$$\text{Crude Proportion} = \frac{3}{10} = 0.3000 \quad (30.00\%)$$

The naive proportion understates true 5-year risk because it treats the censored participants (Subjects 5, 7, and 8), who were followed for only $2.0, 3.5,$ and $4.0$ years, as though they had completed a full 5 years of disease-free observation. The exponential model correctly adjusts for unequal follow-up time.

### Solution, step 3: Construct exact 95% Poisson confidence interval for incidence rate
For an observed count $d = 3$, the exact 95% Poisson confidence limits for the expected count $\mu$ are based on chi-square distribution percentiles:

$$\mu_{\text{lower}} = \frac{1}{2} \chi^2_{0.025, \, 2d} = \frac{1}{2} \chi^2_{0.025, \, 6} = \frac{1}{2} (1.2373) = 0.6187$$

$$\mu_{\text{upper}} = \frac{1}{2} \chi^2_{0.975, \, 2(d+1)} = \frac{1}{2} \chi^2_{0.975, \, 8} = \frac{1}{2} (17.5345) = 8.7673$$

Dividing these limits by $PT = 38.7 \text{ PY}$ yields the exact 95% confidence interval for the true incidence rate:

$$IR_{\text{lower}} = \frac{0.6187}{38.7} \approx 0.01599 \text{ per PY} = 15.99 \text{ per 1,000 PY}$$

$$IR_{\text{upper}} = \frac{8.7673}{38.7} \approx 0.22655 \text{ per PY} = 226.55 \text{ per 1,000 PY}$$

The 95% confidence interval for the incidence rate is $[15.99, \, 226.55]$ cases per 1,000 person-years.

## Fully worked question 2: Direct Age-Standardization & Comparative Mortality Figures

### Question
To investigate regional disparities in cerebrovascular disease, public health statisticians compare stroke mortality in District A (an aging coastal district) and District B (a rapidly industrializing urban district). The population data, observed stroke deaths, and the demographic structure of the National Standard Population across three age strata are:

- **Younger (&lt;45 years)**:
  - District A: Population $n_{A, 1} = 20,000$, stroke deaths $d_{A, 1} = 10$.
  - District B: Population $n_{B, 1} = 60,000$, stroke deaths $d_{B, 1} = 42$.
  - National Standard Population: $N_1^* = 500,000$.
- **Middle-aged (45–64 years)**:
  - District A: Population $n_{A, 2} = 30,000$, stroke deaths $d_{A, 2} = 90$.
  - District B: Population $n_{B, 2} = 30,000$, stroke deaths $d_{B, 2} = 120$.
  - National Standard Population: $N_2^* = 300,000$.
- **Older (65+ years)**:
  - District A: Population $n_{A, 3} = 50,000$, stroke deaths $d_{A, 3} = 500$.
  - District B: Population $n_{B, 3} = 10,000$, stroke deaths $d_{B, 3} = 150$.
  - National Standard Population: $N_3^* = 200,000$.

1. Compute the crude stroke mortality rate per 1,000 residents in District A and District B.
2. Calculate the Directly Standardized Mortality Rate ($DSR$) per 1,000 residents for both districts using the National Standard Population.
3. Compute the Comparative Mortality Figure ($CMF = DSR_A / DSR_B$) and construct the 95% confidence interval for the $DSR$ of District A.

### Solution, step 1: Compute crude stroke mortality rates
First, evaluate total population and total stroke deaths for each district:
- **District A**:
  $$n_A = 20,000 + 30,000 + 50,000 = 100,000$$
  $$d_A = 10 + 90 + 500 = 600 \text{ deaths}$$
  $$\text{Crude Rate}_A = \frac{600}{100,000} = 0.0060 = 6.00 \text{ deaths per 1,000}$$

- **District B**:
  $$n_B = 60,000 + 30,000 + 10,000 = 100,000$$
  $$d_B = 42 + 120 + 150 = 312 \text{ deaths}$$
  $$\text{Crude Rate}_B = \frac{312}{100,000} = 0.00312 = 3.12 \text{ deaths per 1,000}$$

The crude mortality rate in District A ($6.00$ per 1,000) is nearly double that of District B ($3.12$ per 1,000).

### Solution, step 2: Calculate stratum-specific rates and directly standardized rates
The total size of the National Standard Population is:
$$N^* = 500,000 + 300,000 + 200,000 = 1,000,000$$

The standard stratum weights are:
$$w_1^* = \frac{500,000}{1,000,000} = 0.50, \quad w_2^* = \frac{300,000}{1,000,000} = 0.30, \quad w_3^* = \frac{200,000}{1,000,000} = 0.20$$

Now evaluate the stratum-specific mortality rates (per 1,000) in each district:
- **District A**:
  $$r_{A, 1} = \frac{10}{20,000} \times 1,000 = 0.50 \text{ per 1,000}$$
  $$r_{A, 2} = \frac{90}{30,000} \times 1,000 = 3.00 \text{ per 1,000}$$
  $$r_{A, 3} = \frac{500}{50,000} \times 1,000 = 10.00 \text{ per 1,000}$$
  $$DSR_A = (0.50 \times 0.50) + (3.00 \times 0.30) + (10.00 \times 0.20) = 0.25 + 0.90 + 2.00 = 3.15 \text{ per 1,000}$$

- **District B**:
  $$r_{B, 1} = \frac{42}{60,000} \times 1,000 = 0.70 \text{ per 1,000}$$
  $$r_{B, 2} = \frac{120}{30,000} \times 1,000 = 4.00 \text{ per 1,000}$$
  $$r_{B, 3} = \frac{150}{10,000} \times 1,000 = 15.00 \text{ per 1,000}$$
  $$DSR_B = (0.70 \times 0.50) + (4.00 \times 0.30) + (15.00 \times 0.20) = 0.35 + 1.20 + 3.00 = 4.55 \text{ per 1,000}$$

Upon age standardization, District B actually exhibits a substantially higher stroke mortality rate ($4.55$ per 1,000) than District A ($3.15$ per 1,000)! The crude rate reversal was entirely an artifact of confounding by age: District A had half its population in the highest-risk elderly category, whereas District B was overwhelmingly youthful.

### Solution, step 3: Comparative mortality figure and variance estimation for DSR_A
The Comparative Mortality Figure comparing District A to District B is:

$$CMF = \frac{DSR_A}{DSR_B} = \frac{3.15}{4.55} \approx 0.6923 \quad (69.23\%)$$

To construct the 95% confidence interval for $DSR_A$, we compute its sampling variance:

$$\text{Var}(DSR_A) = \sum_{k=1}^3 (w_k^*)^2 \frac{d_{A, k}}{n_{A, k}^2}$$

Expressed on the scale per person (where $w_1 = 0.50, w_2 = 0.30, w_3 = 0.20$):
$$\text{Var}(DSR_A) = (0.50)^2 \frac{10}{(20,000)^2} + (0.30)^2 \frac{90}{(30,000)^2} + (0.20)^2 \frac{500}{(50,000)^2}$$
$$= 0.25 \frac{10}{400,000,000} + 0.09 \frac{90}{900,000,000} + 0.04 \frac{500}{2,500,000,000}$$
$$= 6.25 \times 10^{-9} + 9.00 \times 10^{-9} + 8.00 \times 10^{-9} = 23.25 \times 10^{-9}$$

The standard error on the per-person scale is:
$$\text{SE}(DSR_A) = \sqrt{23.25 \times 10^{-9}} \approx 1.5248 \times 10^{-4}$$

Multiplying by 1,000 to convert to rates per 1,000 population:
$$\text{SE}(DSR_A) \approx 0.1525 \text{ per 1,000}$$

Thus, the 95% confidence interval for District A's standardized rate is:
$$DSR_A \pm 1.96 \times \text{SE}(DSR_A) = 3.15 \pm 1.96(0.1525) = 3.15 \pm 0.2989 = [2.851, \, 3.449] \text{ per 1,000}$$

## Fully worked question 3: Capture-Recapture Estimation of Surveillance Completeness

### Question
An urban district in Dhaka conducts active epidemiological surveillance for pediatric Dengue fever admissions across a 3-month epidemic season. Two independent surveillance systems record confirmed cases:
- System 1 (Central Hospital Inpatient Registry) identifies $n_1 = 450$ confirmed pediatric dengue cases.
- System 2 (District Laboratory Diagnostic Serology Network) identifies $n_2 = 380$ confirmed pediatric dengue cases.
- Cross-matching patient national identification numbers and municipal birth registrations reveals that exactly $m = 190$ cases appeared simultaneously in both systems.

1. Using the Lincoln–Petersen capture-recapture estimator, estimate the total number of pediatric dengue cases $\widehat{N}$ occurring in the district, and calculate Chapman’s bias-corrected estimate $\widehat{N}_C$.
2. Estimate the completeness (sensitivity) of System 1 and System 2 relative to the total estimated population cases.
3. Compute the estimated variance of $\widehat{N}_C$ and construct the 95% confidence interval for the total dengue case burden using Seber's variance estimator.

### Solution, step 1: Lincoln-Petersen and Chapman population size estimation
The Lincoln–Petersen estimator of the total population size is:

$$\widehat{N} = \frac{n_1 \cdot n_2}{m} = \frac{450 \times 380}{190} = \frac{171,000}{190} = 900 \text{ cases}$$

To eliminate small-sample upward bias, Chapman's unbiasing formula adds 1 to each count:

$$\widehat{N}_C = \frac{(n_1 + 1)(n_2 + 1)}{m + 1} - 1 = \frac{(451)(381)}{191} - 1 = \frac{171,831}{191} - 1 \approx 899.64 - 1 = 898.64 \approx 899 \text{ cases}$$

Both methods yield an estimated total disease burden of approximately 900 cases in the municipal district during the season.

### Solution, step 2: Calculate reporting completeness (sensitivity) for each registry
The estimated reporting completeness (sensitivity) of each system is the ratio of observed cases to the estimated true population total $\widehat{N}_C = 899$:

$$\text{Completeness}_1 = \frac{n_1}{\widehat{N}_C} = \frac{450}{899} \approx 0.5006 \quad (50.06\%)$$

$$\text{Completeness}_2 = \frac{n_2}{\widehat{N}_C} = \frac{380}{899} \approx 0.4227 \quad (42.27\%)$$

Notice that the combined union of both systems captured:
$$\text{Total Unique Identified} = n_1 + n_2 - m = 450 + 380 - 190 = 640 \text{ cases}$$

$$\text{Overall Combined Completeness} = \frac{640}{899} \approx 0.7119 \quad (71.19\%)$$

Thus, even combining both registries missed approximately $28.8\%$ ($259$ cases) of all true pediatric dengue cases in the community.

### Solution, step 3: Seber variance estimator and 95% confidence interval
Seber's formula for the variance of the Chapman estimator is:

$$\text{Var}(\widehat{N}_C) = \frac{(n_1 + 1)(n_2 + 1)(n_1 - m)(n_2 - m)}{(m + 1)^2 (m + 2)}$$

Substitute the observed counts:
- $n_1 - m = 450 - 190 = 260$
- $n_2 - m = 380 - 190 = 190$
- $m + 1 = 191$
- $m + 2 = 192$

$$\text{Var}(\widehat{N}_C) = \frac{(451)(381)(260)(190)}{(191)^2 (192)} = \frac{8,488,451,400}{36,481 \times 192} = \frac{8,488,451,400}{7,004,352} \approx 1211.88$$

The standard error of the estimated population size is:

$$\text{SE}(\widehat{N}_C) = \sqrt{1211.88} \approx 34.81 \text{ cases}$$

Applying the asymptotic Gaussian approximation yields the 95% confidence interval:

$$\widehat{N}_C \pm 1.96 \times \text{SE}(\widehat{N}_C) = 898.64 \pm 1.96(34.81) = 898.64 \pm 68.23 = [830.4, \, 966.9]$$

Rounding to integer case counts, we estimate with 95% statistical confidence that the true pediatric dengue burden lies between 830 and 967 cases.
"""

# -------------------------------------------------------------
# UNIT 2
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

## 2.4 Clinical Metrics: Number Needed to Treat (NNT) and Number Needed to Harm (NNH)

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

The $NNH$ represents the number of individuals exposed to the agent required for exactly one additional person to experience the harmful adverse outcome. Comparing $NNT$ for therapeutic benefit against $NNH$ for severe adverse drug reactions provides the fundamental quantitative basis for risk-benefit clinical decision analysis.

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

(OUT_DIR / "unit-1.md").write_text(unit1.strip() + "\n", encoding="utf-8")
(OUT_DIR / "unit-2.md").write_text(unit2.strip() + "\n", encoding="utf-8")
print("Units 1 and 2 written.")
