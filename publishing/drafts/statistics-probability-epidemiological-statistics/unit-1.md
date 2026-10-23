# Unit 1: Foundations of Epidemiology, Surveillance & Measures of Disease Frequency

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

## 1.8 Dynamic Equilibrium: The Exact Mathematical Relation Between Prevalence and Incidence

In descriptive epidemiology and public health surveillance, distinguishing between prevalence (the proportion of existing disease cases in a population) and incidence (the rate of newly emerging cases) is fundamental. While introductory textbooks present the crude approximation $P \approx I \times D$ (where $I$ is incidence rate and $D$ is mean disease duration), rigorous mathematical epidemiology derives the exact relationship under stationary dynamic equilibrium.

### 1. The Differential Equation of Disease Dynamics
Consider a dynamic, open population of size $N(t)$. Let $S(t)$ denote the number of disease-free (susceptible) individuals, and let $C(t)$ denote the number of active disease cases, so that $N(t) = S(t) + C(t)$.
The point prevalence at time $t$ is:
$$P(t) = \frac{C(t)}{N(t)}$$

Assume the following transition parameters:
- New cases emerge from the susceptible pool at instantaneous incidence rate $I(t)$ per person-year:
  $$\text{New cases in } [t, t + dt] = I(t) \cdot S(t)\,dt = I(t) \cdot N(t)(1 - P(t))\,dt$$
- Active cases exit the disease pool through recovery or disease-specific mortality at total recovery/exit hazard rate $\lambda_{\text{exit}} = 1 / D$, where $D$ is the mean duration of illness:
  $$\text{Exits in } [t, t + dt] = \frac{1}{D} \cdot C(t)\,dt = \frac{1}{D} \cdot N(t) P(t)\,dt$$

Under demographic stationarity ($N(t) \equiv N$ is constant), the rate of change of active cases satisfies:
$$\frac{dC(t)}{dt} = I \cdot N(1 - P(t)) - \frac{1}{D} N P(t)$$
Dividing both sides by total population $N$ yields the fundamental differential equation of prevalence dynamics:

$$\frac{dP(t)}{dt} = I(1 - P(t)) - \frac{1}{D} P(t) = I - \left( I + \frac{1}{D} \right) P(t)$$

### 2. Stationary Dynamic Equilibrium
When the epidemic process reaches dynamic steady state ($\frac{dP(t)}{dt} = 0$):
$$I(1 - P) - \frac{1}{D} P = 0 \implies I = P \left( I + \frac{1}{D} \right)$$

Solving explicitly for equilibrium prevalence $P$:

$$P = \frac{I}{I + \frac{1}{D}} = \frac{I \cdot D}{1 + I \cdot D}$$

Expressing this relation in terms of the **Prevalence Odds** ($\frac{P}{1 - P}$):

$$\text{Prevalence Odds} = \frac{P}{1 - P} = \frac{\frac{I \cdot D}{1 + I \cdot D}}{\frac{1}{1 + I \cdot D}} = I \cdot D$$

The prevalence odds is *identically equal* to the product of incidence rate and mean disease duration without any approximation error!
When the disease is rare in the general population ($P < 0.05$), the denominator $1 + I \cdot D \approx 1$, recovering the classical approximation:
$$P \approx I \cdot D$$

### 3. Epidemiological Implications for Intervention Evaluation
This exact mathematical relation explains a critical public health phenomenon: **the treatment paradox**.
- If a medical breakthrough discovers a highly curative therapy (e.g., direct-acting antivirals for Hepatitis C), mean duration $D$ contracts dramatically, driving prevalence $P$ down rapidly.
- Conversely, if an intervention is life-prolonging but not curative (e.g., antiretroviral therapy for HIV or insulin for Type 1 diabetes), case fatality drops, which significantly *lengthens* mean duration $D$. Consequently, point prevalence $P$ rises substantially even while incidence rate $I$ remains stable or declines. Epidemiologists must therefore never interpret rising disease prevalence as an indication of failing disease prevention programs.

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
