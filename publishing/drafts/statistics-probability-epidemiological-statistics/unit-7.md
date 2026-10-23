# Unit 7: Infectious Disease Epidemiology: Transmission Dynamics, Compartmental Models & Outbreak Investigation

Infectious disease epidemiology occupies a unique mathematical domain within population health. While chronic disease epidemiology primarily investigates isolated, independent individuals exposed to static risk factors (such as dietary sodium, tobacco smoke, or genetic polymorphisms), infectious epidemiology studies dynamic, dependent systems where one person's disease status directly determines another person’s exposure probability. An infected individual acts simultaneously as a health outcome and as an infectious exposure vector for the rest of the community. Consequently, classical statistical assumptions of independent and identically distributed (i.i.d.) observations collapse, necessitating dynamic non-linear systems modeling. In this unit, we formalize the biological and mathematical mechanisms of pathogen transmission, establish field outbreak investigation methodologies and epidemic curve deconvolution, derive the classic Kermack-McKendrick deterministic SIR and SEIR compartmental differential systems, formalize the Basic Reproduction Number ($R_0$) and its derivation via the Next-Generation Matrix approach, examine real-time effective reproduction numbers ($R_t$) based on generation intervals, derive the Herd Immunity Threshold ($HIT$) and critical vaccination coverage fractions, and solve the transcendental Epidemic Final Size equation.

## 7.1 Principles of Infectious Disease Epidemiology: The Dynamic Transmission Paradigm

The quantitative study of infectious pathogens is framed around the classical **Epidemiological Triad**:
1. **Agent**: The biological pathogen (virus, bacterium, protozoan, helminth, or prion) characterized by intrinsic virulence, infectivity, pathogenicity, antigenic mutability, and environmental stability.
2. **Host**: The human or animal organism harboring the pathogen, characterized by age, immune competence, nutritional status, behavioral contact patterns, and genetic susceptibility (such as HLA haplotypes).
3. **Environment**: The physical, ecological, and socio-economic surroundings—including ambient temperature, absolute humidity, population density, sanitation infrastructure, and housing ventilation—that mediate contact between agent and host.

### The Fundamental Concepts of Infectivity, Pathogenicity, and Virulence
Epidemiologists distinguish three hierarchical stages of host-pathogen interaction:
- **Infectivity**: The capacity of an agent to enter, survive, and multiply within a susceptible host. Mathematically quantified by the **Secondary Attack Rate** ($SAR$): the proportion of susceptible household or close contacts who develop infection following exposure to an index case.
- **Pathogenicity**: The capacity of an infectious agent to induce overt clinical disease among infected individuals. Quantified as the ratio of clinically symptomatic cases to total infected individuals ($P(\text{Symptoms} \mid \text{Infection})$).
- **Virulence**: The severity of the clinical disease produced by the agent once clinical illness is established. Quantified by the **Case Fatality Rate** ($CFR$): the proportion of clinically diagnosed cases who die from the condition ($P(\text{Death} \mid \text{Clinical Disease})$), or the **Infection Fatality Rate** ($IFR$), which includes subclinical infections.

### Temporal Dynamics: Latent, Incubation, and Infectious Periods
Infectious disease timelines involve two parallel biological clocks:
1. **The Pathologic / Clinical Timeline**: Begins at the instant of biological infection. The **Incubation Period** is the time elapsed between infection and the manifestation of initial clinical signs or symptoms.
2. **The Transmission / Virologic Timeline**: Begins at biological infection. The **Latent Period** is the duration between infection and the onset of viral shedding or infectiousness to others. The **Infectious Period** is the duration during which the infected individual actively sheds infectious pathogen and can transmit the disease to susceptible contacts.

When the latent period is shorter than the incubation period, **asymptomatic or presymptomatic transmission** occurs (as observed in SARS-CoV-2 and influenza), presenting immense logistical challenges for public health isolation strategies. Conversely, when symptoms precede infectiousness (as in Smallpox and SARS-CoV-1), simple symptomatic temperature screening and immediate patient isolation are sufficient to halt epidemic expansion.

## 7.2 Outbreak Investigation Protocols and Epidemic Curve Deconvolution

An **outbreak** (or epidemic) is defined as the occurrence of cases of an illness, specific health-related behavior, or other health-related events in a community or region clearly in excess of normal baseline expectancy.

### The Ten-Step Field Outbreak Investigation Protocol
Field epidemiologists, pioneered by the Epidemic Intelligence Service (EIS) of the US Centers for Disease Control and Prevention (CDC), adhere to a systematic operational protocol:
1. Prepare for field work (logistics, biosafety, inter-agency agreements).
2. Establish the existence of an outbreak (verifying that observed counts exceed historical seasonal baselines and ruling out pseudo-epidemics caused by altered diagnostic coding or sudden reporting surges).
3. Verify the clinical diagnosis through definitive laboratory microbiological testing.
4. Construct an objective, standardized **Case Definition** (stratified into Confirmed, Probable, and Suspect cases based on clinical criteria, time, place, and person parameters).
5. Execute systematic case finding and record standardized case data onto an active master line listing.
6. Perform descriptive epidemiology: characterize the outbreak by Time (epidemic curve), Place (spatial GIS spot maps), and Person (attack rates by age, sex, occupation).
7. Formulate etiologic causal hypotheses regarding the transmission vehicle, source, and reservoir.
8. Evaluate hypotheses through analytical epidemiology (retrospective cohort study for closed events such as foodborne banquet outbreaks; case-control study for open community outbreaks).
9. Implement immediate, decisive public health control and prevention measures (recalling contaminated food products, repairing municipal water chlorination, closing contaminated air-conditioning cooling towers, administering emergency ring vaccinations).
10. Initiate ongoing active surveillance, communicate findings to public stakeholders through transparent scientific reporting, and document policy recommendations.

### Epidemic Curves and Transmission Architectures
An **Epidemic Curve** (Epi Curve) is a histogram displaying the frequency of newly diagnosed incident cases plotted over time on the horizontal axis, with the time interval conventionally chosen as one-fourth to one-half of the agent’s median incubation period. The geometric shape of an epidemic curve reveals the underlying transmission mechanism:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Epidemic Pattern</th><th>Transmission Mechanism</th><th>Geometric Shape of Epi Curve</th><th>Typical Epidemiological Examples</th></tr>
</thead>
<tbody>
<tr><td><strong>Point-Source Outbreak</strong></td><td>Susceptible population exposed simultaneously to a single, common vehicle over a very brief window.</td><td>Sharp, steep upward trajectory, solitary acute peak, followed by a gradual, log-normal downward tail.</td><td>Foodborne staphylococcal enterotoxin poisoning at a wedding reception; chemical leak.</td></tr>
<tr><td><strong>Continuous Common-Source</strong></td><td>Prolonged, ongoing exposure to a shared vehicle over an extended time interval.</td><td>Plateau-like profile without a sharp individual peak; cases continue until source is terminated.</td><td>Broad Street pump cholera outbreak; contaminated municipal municipal water supply.</td></tr>
<tr><td><strong>Intermittent Common-Source</strong></td><td>Irregular, episodic release of pathogen from a recurring vehicle.</td><td>Irregular series of jagged spikes reflecting intermittent contamination events.</td><td>Industrial plant intermittently discharging toxic effluent or contaminated dairy batches.</td></tr>
<tr><td><strong>Propagated (Person-to-Person)</strong></td><td>Serial transmission from person to person through respiratory droplets, direct contact, or vectors.</td><td>Progressively taller, broadening waves spaced roughly one incubation period apart.</td><td>Measles, influenza, varicella, SARS-CoV-2 community transmission waves.</td></tr>
</tbody>
</table></div>

## 7.3 Compartmental Mathematical Modeling: The Kermack-McKendrick SIR and SEIR Systems

Mathematical modeling of infectious diseases provides a predictive framework for forecasting hospital bed requirements, evaluating vaccination thresholds, and designing non-pharmaceutical interventions (such as lockdowns, contact tracing, and mask mandates).

### The Classical Kermack-McKendrick SIR Differential System
In 1927, William Ogilvy Kermack and Anderson Gray McKendrick formulated the foundational **SIR Model**. Consider a closed population of constant total size $N$, where demographic vital dynamics (births and natural deaths) are negligible over the epidemic duration:

$$N = S(t) + I(t) + R(t) = \text{Constant}$$

The population is partitioned into three mutually exclusive compartments:
- $S(t)$: Susceptible individuals who are disease-free but capable of contracting infection.
- $I(t)$: Infectious individuals who currently harbor the pathogen and are capable of transmitting it to susceptibles.
- $R(t)$: Removed / Recovered individuals who have recovered with permanent sterilizing immunity or have died from the disease.

Let $\beta$ denote the **transmission rate coefficient**, representing the average number of adequate, transmission-producing contacts per infectious individual per unit time in a fully susceptible population. Let $\gamma = 1 / \bar{D}$ denote the **recovery rate**, where $\bar{D}$ is the average duration of the infectious period. Under the principle of mass action (homogeneous mixing), the deterministic system of non-linear ordinary differential equations is:

$$\frac{dS}{dt} = -\frac{\beta S I}{N}$$

$$\frac{dI}{dt} = \frac{\beta S I}{N} - \gamma I = I \left( \frac{\beta S}{N} - \gamma \right)$$

$$\frac{dR}{dt} = \gamma I$$

Adding the three equations:
$$\frac{dS}{dt} + \frac{dI}{dt} + \frac{dR}{dt} = -\frac{\beta S I}{N} + \frac{\beta S I}{N} - \gamma I + \gamma I = 0 \implies S(t) + I(t) + R(t) = N$$

### The SEIR Model: Incorporating the Latent Period
For pathogens where biological infection is followed by a substantial non-infectious latent phase (such as measles, tuberculosis, or COVID-19), the SIR model is extended by inserting an **Exposed (Latent)** compartment $E(t)$. Let $\sigma = 1 / \bar{T}_{\text{latent}}$ denote the rate at which exposed individuals progress to active infectiousness:

$$\frac{dS}{dt} = -\frac{\beta S I}{N}, \qquad \frac{dE}{dt} = \frac{\beta S I}{N} - \sigma E, \qquad \frac{dI}{dt} = \sigma E - \gamma I, \qquad \frac{dR}{dt} = \gamma I$$

The inclusion of the $E$ compartment introduces a realistic phase delay into the epidemic wave, slowing the initial growth rate of case notifications without altering the ultimate final epidemic size.

## 7.4 The Basic Reproduction Number (R_0): Biological Definition and Mathematical Derivation

The **Basic Reproduction Number**, universally designated as $R_0$ ("R-naught"), is the single most important parameter in infectious disease epidemiology.

### Biological Definition
$R_0$ is defined as the **expected number of secondary infections generated by a single typical infectious individual introduced into a completely susceptible population throughout that individual’s entire infectious period**.

Notice the three strict conditions:
1. It is a mathematical expectation (average) across heterogeneous host contacts.
2. The index case must be typical in infectiousness.
3. The surrounding population must be **$100\%$ susceptible** ($S(0) = N$).

### Mathematical Derivation from the SIR Differential System
From the second differential equation of the SIR system:

$$\frac{dI}{dt} = I \left( \frac{\beta S}{N} - \gamma \right)$$

At the introduction of the primary case into a pristine population, $S(0) \approx N$, so $S(0) / N \approx 1$. Thus:

$$\left. \frac{dI}{dt} \right|_{t=0} = I(0) (\beta - \gamma) = I(0) \gamma \left( \frac{\beta}{\gamma} - 1 \right)$$

An epidemic outbreak can ignite and expand if and only if the number of infectious individuals is strictly increasing ($\frac{dI}{dt} > 0$), which requires:

$$\frac{\beta}{\gamma} - 1 > 0 \implies \frac{\beta}{\gamma} > 1$$

We define the Basic Reproduction Number for the classical mass-action SIR model as:

$$R_0 = \frac{\beta}{\gamma} = \beta \times \bar{D}$$

This definition decomposes $R_0$ into intuitive biological determinants ($R_0 = c \times p \times d$):
- $c$: Contact rate (average number of social or physical contacts per unit time).
- $p$: Probability of transmission per contact given an encounter with a susceptible person.
- $d = \bar{D} = 1 / \gamma$: Duration of infectiousness.

### The Threshold Phenomenon
The numerical value of $R_0$ dictates the qualitative fate of the pathogen:
- $R_0 < 1.0$: Subcritical. Each case produces less than one replacement case. The chain of transmission cannot sustain itself; the pathogen inevitably dies out naturally without causing an epidemic.
- $R_0 = 1.0$: Endemic equilibrium. Each case replaces itself with exactly one secondary case. The disease persists in the population at a constant baseline prevalence.
- $R_0 > 1.0$: Supercritical. Each case produces more than one replacement case. The disease grows exponentially in the susceptible population, igniting an epidemic wave.

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Infectious Disease</th><th>Primary Mode of Transmission</th><th>Estimated Historical $R_0$</th><th>Required Herd Immunity Threshold ($HIT$)</th></tr>
</thead>
<tbody>
<tr><td><strong>Measles</strong></td><td>Airborne aerosol droplet nuclei</td><td>$12.0 – 18.0$</td><td>$92\% – 95\%$</td></tr>
<tr><td><strong>Pertussis (Whooping Cough)</strong></td><td>Respiratory droplets</td><td>$12.0 – 17.0$</td><td>$92\% – 94\%$</td></tr>
<tr><td><strong>Smallpox</strong></td><td>Respiratory droplets / fomites</td><td>$5.0 – 7.0$</td><td>$80\% – 86\%$</td></tr>
<tr><td><strong>Polio</strong></td><td>Fecal-oral transmission</td><td>$5.0 – 7.0$</td><td>$80\% – 86\%$</td></tr>
<tr><td><strong>SARS-CoV-2 (Omicron Variant)</strong></td><td>Airborne aerosol / respiratory droplets</td><td>$8.0 – 12.0$</td><td>$88\% – 92\%$</td></tr>
<tr><td><strong>Seasonal Influenza</strong></td><td>Respiratory droplets</td><td>$1.3 – 1.8$</td><td>$23\% – 44\%$</td></tr>
<tr><td><strong>Ebola Virus</strong></td><td>Direct contact with infected body fluids</td><td>$1.5 – 2.0$</td><td>$33\% – 50\%$</td></tr>
</tbody>
</table></div>

### The Next-Generation Matrix Approach for Heterogeneous Systems
In complex models with multiple host compartments (e.g., vector-borne malaria models with mosquito and human vectors, or age-structured contact matrices), $R_0$ cannot be derived by inspection. Odo Diekmann, J.A.P. Heesterbeek, and Johan Metz (1990) formulated the **Next-Generation Matrix (NGM)** approach.

Let $\mathbf{x} = (x_1, \dots, x_m)^T$ denote the $m$ infected compartments. The linearized system near the disease-free equilibrium (DFE) is partitioned into new infection flows $\mathcal{F}_i(\mathbf{x})$ and transitions $\mathcal{V}_i(\mathbf{x})$:
$$\frac{d\mathbf{x}}{dt} = \mathcal{F}(\mathbf{x}) - \mathcal{V}(\mathbf{x})$$
Evaluating the Jacobian matrices at the disease-free equilibrium $\mathbf{x}_0$:
$$\mathbf{F} = \left[ \frac{\partial \mathcal{F}_i}{\partial x_j}(\mathbf{x}_0) \right], \qquad \mathbf{V} = \left[ \frac{\partial \mathcal{V}_i}{\partial x_j}(\mathbf{x}_0) \right]$$
The **Next-Generation Matrix** is defined as $\mathbf{K} = \mathbf{F} \mathbf{V}^{-1}$. The Basic Reproduction Number is defined as the **spectral radius** (dominant eigenvalue) of the Next-Generation Matrix:

$$R_0 = \rho(\mathbf{F} \mathbf{V}^{-1}) = \max \{ |\lambda| : \lambda \in \sigma(\mathbf{F} \mathbf{V}^{-1}) \}$$

## 7.5 Real-Time Tracking: The Effective Reproduction Number (R_t) and Serial Intervals

While $R_0$ is a fixed theoretical property of a pathogen entering a pristine, non-immune population under baseline social behavior, real-world epidemics unfold across changing landscapes of declining susceptibility, public health interventions, behavioral adaptations, and seasonal climate shifts.

### The Effective Reproduction Number (R_t)
The **Effective Reproduction Number** ($R_t$), or the **Time-Varying Reproduction Number**, represents the average number of secondary cases generated by an infectious individual at calendar time $t$.

In a simple mass-action population where the proportion of susceptible individuals has dropped to $s(t) = S(t) / N$:

$$R_t = R_0 \times \frac{S(t)}{N} = R_0 \cdot s(t)$$

As an epidemic spreads, susceptible individuals become infected and transition to the recovered immune state. Consequently, $S(t) / N$ declines monotonically. Even if transmission parameters $\beta$ remain unchanged, the epidemic reaches its peak when:

$$R_t = 1.0 \implies R_0 \frac{S(t_{\text{peak}})}{N} = 1.0 \implies \frac{S(t_{\text{peak}})}{N} = \frac{1}{R_0}$$

At this critical peak date $t_{\text{peak}}$, each case produces exactly one secondary case. Thereafter, $S(t) / N < 1 / R_0 \implies R_t < 1.0$, and the epidemic wave enters a phase of natural contraction!

### Estimation of R_t from Daily Notification Streams: The Wallinga-Teunis and Cori Methods
In modern pandemic surveillance, public health authorities track $R_t$ in real time from daily incidence time series $I_t$. Anneke Wallinga and Jacco Teunis (2004) and Anne Cori et al. (2013) developed renewal equation estimators:

$$I_t = R_t \sum_{s=1}^t I_{t-s} w_s$$

where $w_s$ is the probability mass function of the **generation interval** (or serial interval): the time distribution between the symptom onset of an index case and the symptom onset of their secondary case. Under a Bayesian Poisson likelihood framework with a gamma prior on $R_t$, the instantaneous reproduction number averaged over a sliding time window of length $\tau$ is estimated as:

$$\widehat{R}_t = \frac{\sum_{k=t-\tau+1}^t I_k}{\sum_{k=t-\tau+1}^t \Lambda_k}$$

where $\Lambda_k = \sum_{s=1}^k I_{k-s} w_s$ is the total infectiousness of the population at day $k$. When $\widehat{R}_t < 1.0$, control measures are successfully suppressing transmission; if $\widehat{R}_t > 1.0$, transmission is accelerating.

## 7.6 The Herd Immunity Threshold (HIT) and the Epidemic Final Size Equation

### Derivation of the Herd Immunity Threshold
**Herd immunity** (community immunity) refers to the indirect protection conferred upon unvaccinated or non-immune vulnerable individuals when a critical proportion of the population possesses sterilizing immunity, thereby disrupting chains of transmission.

Suppose a proportion $p$ of the population is successfully immunized through vaccination or natural recovery, leaving a susceptible fraction $1 - p$. The effective reproduction number in this population is:

$$R_{\text{eff}} = R_0 (1 - p)$$

To prevent an outbreak from expanding upon the re-introduction of an infected traveler, we must guarantee that $R_{\text{eff}} \le 1.0$:

$$R_0 (1 - p) \le 1.0 \implies 1 - p \le \frac{1}{R_0} \implies p \ge 1 - \frac{1}{R_0}$$

The minimum immune fraction required to prevent sustained epidemic transmission is the **Herd Immunity Threshold** ($HIT$):

$$HIT = 1 - \frac{1}{R_0}$$

If a vaccine has imperfect biological efficacy $V_e < 1.0$ in preventing infection, the **Critical Vaccination Coverage** ($V_c$) required to achieve herd immunity is:

$$V_c = \frac{HIT}{V_e} = \frac{1 - 1/R_0}{V_e}$$

For example, for measles with $R_0 = 15.0$ and vaccine effectiveness $V_e = 0.95$:
$$HIT = 1 - \frac{1}{15} = \frac{14}{15} \approx 0.9333 \quad (93.33\%)$$
$$V_c = \frac{0.9333}{0.95} \approx 0.9825 \quad (98.25\%)$$
Thus, over $98\%$ of the eligible population must be vaccinated to achieve community-wide elimination of measles!

### The Transcendental Epidemic Final Size Equation
A common misconception is that an epidemic ends only when every susceptible person has become infected ($S(\infty) = 0$). In reality, an epidemic burns out long before susceptibles are exhausted, because transmission collapses once $R_t < 1.0$.

To calculate the ultimate proportion of the population that contracts the disease over the entire epidemic, we divide the first differential equation of the SIR system by the third:

$$\frac{dS / dt}{dR / dt} = \frac{-\beta S I / N}{\gamma I} = -\frac{\beta}{\gamma N} S = -\frac{R_0}{N} S$$

Integrating both sides from $t = 0$ to $t = \infty$:

$$\int_{S(0)}^{S(\infty)} \frac{1}{S} \, dS = -\frac{R_0}{N} \int_{R(0)}^{R(\infty)} dR$$

$$\ln\left( \frac{S(\infty)}{S(0)} \right) = -\frac{R_0}{N} [R(\infty) - R(0)]$$

Assuming an initially pristine population where $S(0) \approx N$ and $R(0) = 0$, and noting that at the conclusion of the outbreak $I(\infty) = 0 \implies R(\infty) = N - S(\infty)$:

$$\ln\left( \frac{S(\infty)}{N} \right) = -R_0 \left( 1 - \frac{S(\infty)}{N} \right)$$

Let $s_\infty = S(\infty) / N$ denote the final fraction remaining susceptible, and let $z = 1 - s_\infty = R(\infty) / N$ denote the **final epidemic attack rate** (the total proportion of the population infected). Substituting $s_\infty = 1 - z$:

$$\ln(1 - z) = -R_0 z \implies 1 - z = \exp(-R_0 z)$$

Rearranging yields the celebrated **Transcendental Final Size Equation**:

$$z = 1 - \exp(-R_0 z)$$

This non-linear equation has no closed-form solution in terms of elementary functions, but its unique positive root is readily evaluated using Newton-Raphson iteration. For $R_0 = 2.0$, solving $z = 1 - e^{-2z}$ yields $z \approx 0.7968$ ($79.68\%$). Even with zero public health intervention, over $20\%$ of the population naturally escapes infection!

## Fully worked question 1: Field Outbreak Investigation: Attack Rates, Food-Specific Risk Ratios, and Epidemic Curve Deconvolution

### Question
An acute outbreak of severe gastrointestinal gastroenteritis occurs among attendees of an international medical alumni banquet at a convention center in Dhaka. A total of $N = 250$ individuals attended the event, which took place on Friday evening (dinner served at 8:00 PM). Over the subsequent 72 hours, 120 attendees developed acute nausea, vomiting, and profuse diarrhea. A field investigation team surveys all 250 attendees, recording clinical symptoms, exact hour of symptom onset, and food consumption logs across four primary dishes: Roast Chicken, Beef Kacchi Biryani, Mixed Vegetable Salad, and Custard Dessert.

The survey cross-tabulations are:
- **Roast Chicken**:
  - Ate Chicken: 150 attendees; 80 became ill, 70 remained healthy.
  - Did Not Eat Chicken: 100 attendees; 40 became ill, 60 remained healthy.
- **Beef Kacchi Biryani**:
  - Ate Biryani: 180 attendees; 90 became ill, 90 remained healthy.
  - Did Not Eat Biryani: 70 attendees; 30 became ill, 40 remained healthy.
- **Mixed Vegetable Salad**:
  - Ate Salad: 120 attendees; 102 became ill, 18 remained healthy.
  - Did Not Eat Salad: 130 attendees; 18 became ill, 112 remained healthy.
- **Custard Dessert**:
  - Ate Custard: 160 attendees; 80 became ill, 80 remained healthy.
  - Did Not Eat Custard: 90 attendees; 40 became ill, 50 remained healthy.

The distribution of incubation periods for the 120 ill individuals (measured from Friday 8:00 PM) reveals:
- 0–12 hours: 2 cases
- 13–24 hours: 18 cases
- 25–36 hours: 64 cases (Peak: Saturday midnight to Sunday 8:00 AM)
- 37–48 hours: 26 cases
- 49–60 hours: 8 cases
- 61–72 hours: 2 cases

1. For all four food items, calculate the food-specific attack rate in attendees who ate the food ($AR_{\text{ate}}$), the attack rate in attendees who did not eat the food ($AR_{\text{did not eat}}$), and the food-specific **Risk Ratio** ($RR$).
2. Identify the contaminated vehicle responsible for the outbreak. Compute the 95% confidence interval for its Risk Ratio, calculate the Attributable Fraction in the Exposed ($AF_e$), and calculate the Population Attributable Fraction ($PAF$).
3. Analyze the epidemic curve: calculate the median incubation period, identify the outbreak pattern (point-source vs propagated), and compare against typical foodborne pathogens (e.g., *Staphylococcus aureus* [2–6 hr], *Salmonella enterica* [12–36 hr], *Campylobacter jejuni* [48–96 hr]) to suggest the likely etiologic agent.

### Solution, step 1: Calculate food-specific attack rates and risk ratios
Evaluate attack rates ($AR = \text{Ill} / \text{Total}$) and Risk Ratios ($RR = AR_{\text{ate}} / AR_{\text{not ate}}$) for each food:

1. **Roast Chicken**:
   $$AR_{\text{ate}} = \frac{80}{150} \approx 0.5333 \quad (53.33\%)$$
   $$AR_{\text{not ate}} = \frac{40}{100} = 0.4000 \quad (40.00\%)$$
   $$RR_{\text{chicken}} = \frac{0.5333}{0.4000} \approx 1.333 \quad (95\%\text{ CI}: [1.00, \, 1.78])$$

2. **Beef Kacchi Biryani**:
   $$AR_{\text{ate}} = \frac{90}{180} = 0.5000 \quad (50.00\%)$$
   $$AR_{\text{not ate}} = \frac{30}{70} \approx 0.4286 \quad (42.86\%)$$
   $$RR_{\text{biryani}} = \frac{0.5000}{0.4286} \approx 1.167 \quad (95\%\text{ CI}: [0.86, \, 1.58])$$

3. **Mixed Vegetable Salad**:
   $$AR_{\text{ate}} = \frac{102}{120} = 0.8500 \quad (85.00\%)$$
   $$AR_{\text{not ate}} = \frac{18}{130} \approx 0.1385 \quad (13.85\%)$$
   $$RR_{\text{salad}} = \frac{0.8500}{0.1385} \approx 6.139 \approx 6.14$$

4. **Custard Dessert**:
   $$AR_{\text{ate}} = \frac{80}{160} = 0.5000 \quad (50.00\%)$$
   $$AR_{\text{not ate}} = \frac{40}{90} \approx 0.4444 \quad (44.44\%)$$
   $$RR_{\text{custard}} = \frac{0.5000}{0.4444} \approx 1.125 \quad (95\%\text{ CI}: [0.85, \, 1.48])$$

### Solution, step 2: Causal vehicle identification, confidence intervals, and PAF
The **Mixed Vegetable Salad** is decisively identified as the vehicle:
- Attendees who consumed the salad suffered an $85.0\%$ attack rate, compared to only $13.8\%$ in those who did not.
- The Risk Ratio is massive: $RR = 6.14$.

1. **95% Confidence Interval for Salad Risk Ratio**:
   $$\text{SE}(\ln \widehat{RR}) = \sqrt{\frac{1}{102} - \frac{1}{120} + \frac{1}{18} - \frac{1}{130}} = \sqrt{0.009804 - 0.008333 + 0.055556 - 0.007692} = \sqrt{0.049335} \approx 0.2221$$
   $$\ln(6.139) = 1.8146$$
   $$\text{Log Limits} = 1.8146 \pm 1.96(0.2221) = 1.8146 \pm 0.4353 = [1.3793, \, 2.2499]$$
   $$CI_{0.95}(RR) = [\exp(1.3793), \, \exp(2.2499)] = [3.97, \, 9.49]$$
   The lower bound of $3.97$ confirms an overwhelming, statistically significant excess risk.

2. **Attributable Fractions**:
   $$\widehat{AF}_e = \frac{RR - 1}{RR} = \frac{6.139 - 1}{6.139} = \frac{5.139}{6.139} \approx 0.8371 \quad (83.71\%)$$
   Among salad consumers, $83.7\%$ of gastroenteritis cases were directly attributable to eating the salad.

   $$\widehat{PAF} = \frac{R_{\text{total}} - R_0}{R_{\text{total}}} = \frac{120 / 250 - 18 / 130}{120 / 250} = \frac{0.4800 - 0.1385}{0.4800} = \frac{0.3415}{0.4800} \approx 0.7115 \quad (71.15\%)$$
   Over $71\%$ of all gastroenteritis cases occurring at the banquet were attributable to the contaminated vegetable salad!

### Solution, step 3: Epidemic curve deconvolution and pathogen identification
1. **Outbreak Pattern**:
   The epidemic curve exhibits a classic **Point-Source** geometry: a sharp, explosive ascent beginning 12 hours post-dinner, a single acute peak clustered between 25 and 36 hours (over half the cases), and a steep, tapered resolution by 72 hours. There are no secondary waves.

2. **Median Incubation Period**:
   With 120 cases ordered chronologically:
   - Cumulative cases up to 24 hr: $2 + 18 = 20$ cases.
   - Cumulative cases up to 36 hr: $20 + 64 = 84$ cases.
   The 60th case falls within the 25–36 hour window. The median incubation period is approximately **$30\text{ hours}$** (range: 10 to 68 hours).

3. **Etiologic Agent**:
   - Pre-formed *Staphylococcus aureus* or *Bacillus cereus* enterotoxins have incubation periods of 1–6 hours (too rapid).
   - Viral Norovirus typically exhibits a 24–48 hour incubation, but salad consumption with watery diarrhea at 30 hours is quintessential for **non-typhoidal *Salmonella enterica*** or **Enterotoxigenic *Escherichia coli* (ETEC)** introduced via contaminated raw salad vegetables washed with unchlorinated water.

## Fully worked question 2: The Basic Reproduction Number R_0, Herd Immunity Threshold, and Critical Vaccination Coverage

### Question
Public health epidemiologists at the Institute of Epidemiology, Disease Control and Research (IEDCR) in Dhaka evaluate transmission dynamics and vaccine targets for three contrasting infectious pathogens circulating in an urban population:
- **Pathogen 1 (Measles Virus)**: Highly contagious airborne paramyxovirus with an estimated transmission coefficient $\beta_1 = 1.50 \text{ day}^{-1}$ and an average infectious period duration of $\bar{D}_1 = 10.0 \text{ days}$. The available live attenuated MMR vaccine confers sterilizing immunity with vaccine effectiveness $V_{e1} = 0.95$ ($95\%$).
- **Pathogen 2 (SARS-CoV-2 Delta Variant)**: Respiratory aerosol coronavirus with transmission coefficient $\beta_2 = 1.00 \text{ day}^{-1}$ and mean infectious period $\bar{D}_2 = 6.0 \text{ days}$. mRNA vaccine effectiveness against infection transmission is $V_{e2} = 0.75$ ($75\%$).
- **Pathogen 3 (Rubella Virus)**: Aerosol virus with transmission coefficient $\beta_3 = 0.45 \text{ day}^{-1}$ and mean infectious duration $\bar{D}_3 = 14.0 \text{ days}$. Vaccine effectiveness is $V_{e3} = 0.98$ ($98\%$).

1. For each of the three pathogens, compute the recovery rate $\gamma$, calculate the Basic Reproduction Number $R_0$, and compute the theoretical Herd Immunity Threshold ($HIT$).
2. Taking into account the imperfect vaccine effectiveness $V_e$, calculate the Critical Vaccination Coverage ($V_c$) required to achieve population elimination for all three pathogens. Determine which of these pathogens can achieve elimination through vaccination alone, and which cannot.
3. If an urban district achieves an $80\%$ vaccination coverage ($p = 0.80$) with the MMR vaccine against Measles, calculate the Effective Reproduction Number ($R_t$) when a primary index case is imported into the district. Will a major epidemic wave occur?

### Solution, step 1: Compute recovery rates, R_0, and theoretical HIT
The recovery rate is $\gamma = 1 / \bar{D}$. The Basic Reproduction Number under the mass-action assumption is $R_0 = \beta / \gamma = \beta \times \bar{D}$. The Herd Immunity Threshold is $HIT = 1 - 1/R_0$.

1. **Pathogen 1 (Measles)**:
   $$\gamma_1 = \frac{1}{10.0} = 0.10 \text{ day}^{-1}$$
   $$R_{0, 1} = \beta_1 \times \bar{D}_1 = 1.50 \times 10.0 = 15.0$$
   $$HIT_1 = 1 - \frac{1}{15.0} = 1 - 0.0667 = 0.9333 \quad (93.33\%)$$

2. **Pathogen 2 (SARS-CoV-2 Delta)**:
   $$\gamma_2 = \frac{1}{6.0} \approx 0.1667 \text{ day}^{-1}$$
   $$R_{0, 2} = \beta_2 \times \bar{D}_2 = 1.00 \times 6.0 = 6.0$$
   $$HIT_2 = 1 - \frac{1}{6.0} = 1 - 0.1667 = 0.8333 \quad (83.33\%)$$

3. **Pathogen 3 (Rubella)**:
   $$\gamma_3 = \frac{1}{14.0} \approx 0.07143 \text{ day}^{-1}$$
   $$R_{0, 3} = \beta_3 \times \bar{D}_3 = 0.45 \times 14.0 = 6.30$$
   $$HIT_3 = 1 - \frac{1}{6.30} = 1 - 0.1587 = 0.8413 \quad (84.13\%)$$

### Solution, step 2: Critical vaccination coverage and elimination feasibility
To account for imperfect vaccine effectiveness $V_e$, the required vaccination fraction is:
$$V_c = \frac{HIT}{V_e} = \frac{1 - 1/R_0}{V_e}$$

1. **Measles ($HIT_1 = 93.33\%, V_{e1} = 0.95$)**:
   $$V_{c1} = \frac{0.9333}{0.95} \approx 0.9825 \quad (98.25\%)$$
   Elimination is theoretically possible, but requires an extraordinary $98.25\%$ population vaccination coverage.

2. **SARS-CoV-2 Delta ($HIT_2 = 83.33\%, V_{e2} = 0.75$)**:
   $$V_{c2} = \frac{0.8333}{0.75} \approx 1.1111 \quad (111.11\%)$$
   **Elimination is mathematically impossible through vaccination alone!**
   Even if $100\%$ of the human population is vaccinated ($p = 1.0$), the maximum achievable immune fraction is only $1.0 \times 0.75 = 75.0\%$, which falls short of the required $83.33\%$ threshold. SARS-CoV-2 cannot be eradicated solely by a vaccine that provides only $75\%$ protection against transmission; non-pharmaceutical interventions or updated mucosal vaccines are required.

3. **Rubella ($HIT_3 = 84.13\%, V_{e3} = 0.98$)**:
   $$V_{c3} = \frac{0.8413}{0.98} \approx 0.8584 \quad (85.84\%)$$
   Achieving an $85.8\%$ coverage will successfully eradicate Rubella transmission.

### Solution, step 3: Effective reproduction number in partially vaccinated district
In the urban district where $p = 0.80$ are vaccinated against measles with $V_{e1} = 0.95$:
$$\text{Proportion Immune} = p \times V_{e1} = 0.80 \times 0.95 = 0.7600 \quad (76.00\%)$$
$$\text{Proportion Susceptible } s(t) = 1 - 0.7600 = 0.2400 \quad (24.00\%)$$

The Effective Reproduction Number is:
$$R_t = R_0 \times s(t) = 15.0 \times 0.2400 = 3.60$$

**Epidemic Forecast**:
Because $R_t = 3.60 \gg 1.0$, the population does **not** possess herd immunity. An imported index case will produce an average of $3.6$ secondary infections. An explosive epidemic wave will ignite through the unimmunized minority ($24\%$ of the population), demonstrating why partial vaccination coverage fails to protect communities against highly transmissible pathogens like measles.

## Fully worked question 3: Kermack-McKendrick SIR Differential System and Epidemic Final Size Calculation

### Question
An isolated island penal colony with a stable, homogeneous population of $N = 10,000$ susceptible individuals experiences an outbreak of a novel respiratory influenza virus. An infectious guard ($I(0) = 1$) introduces the virus at day $t = 0$. Public health biostatisticians model the outbreak using the Kermack-McKendrick SIR model:
$$\frac{dS}{dt} = -\frac{\beta S I}{N}, \qquad \frac{dI}{dt} = \frac{\beta S I}{N} - \gamma I, \qquad \frac{dR}{dt} = \gamma I$$
Laboratory epidemiological parameters are determined to be:
- Transmission rate: $\beta = 0.60 \text{ day}^{-1}$
- Recovery rate: $\gamma = 0.25 \text{ day}^{-1}$ (average infectious duration $\bar{D} = 4.0 \text{ days}$)

1. Compute the Basic Reproduction Number $R_0$. Determine the peak day condition: what is the exact number of susceptible individuals remaining ($S_{\text{peak}}$) at the instant the epidemic achieves its maximum number of active infections?
2. Derive the transcendental equation for the final epidemic size $z = R(\infty) / N$.
3. Using the Newton-Raphson numerical algorithm starting from an initial guess $z_0 = 0.80$, compute successive approximations ($z_1, z_2, z_3$) to evaluate the final attack rate $z$ to four decimal places. Exactly how many island residents contract the disease, and how many escape infection entirely?

### Solution, step 1: Basic Reproduction Number and peak susceptibility condition
The Basic Reproduction Number is:
$$R_0 = \frac{\beta}{\gamma} = \frac{0.60}{0.25} = 2.40$$

The rate of change of active infections is:
$$\frac{dI}{dt} = I \left( \frac{\beta S}{N} - \gamma \right)$$

Active infections achieve their global peak ($I_{\max}$) when $\frac{dI}{dt} = 0$:
$$\frac{\beta S_{\text{peak}}}{N} - \gamma = 0 \implies \frac{S_{\text{peak}}}{N} = \frac{\gamma}{\beta} = \frac{1}{R_0}$$
$$S_{\text{peak}} = \frac{N}{R_0} = \frac{10,000}{2.40} \approx 4,166.67 \approx 4,167 \text{ individuals}$$

At the exact peak of the epidemic wave, exactly $4,167$ susceptible individuals remain. The remaining $5,833$ individuals have already been infected ($I + R$). Once the susceptible pool drops below $4,167$, $R_t < 1.0$, and the daily number of active cases begins its irreversible decline.

### Solution, step 2: Derivation of the final size transcendental equation
Dividing the differential equation for $S$ by that for $R$:
$$\frac{dS}{dR} = -\frac{\beta S I / N}{\gamma I} = -\frac{R_0}{N} S$$

Separating variables and integrating from $t = 0$ to $t = \infty$:
$$\int_{S(0)}^{S(\infty)} \frac{1}{S} \, dS = -\frac{R_0}{N} \int_{R(0)}^{R(\infty)} dR$$
$$\ln\left(\frac{S(\infty)}{S(0)}\right) = -\frac{R_0}{N} [R(\infty) - R(0)]$$

With $S(0) \approx N, R(0) = 0$, and $R(\infty) = N - S(\infty) = N z$ where $z = R(\infty) / N$ is the final attack rate:
$$\ln(1 - z) = -R_0 z \implies 1 - z = \exp(-R_0 z) \implies z = 1 - \exp(-R_0 z)$$

For this island population with $R_0 = 2.40$:
$$f(z) = z - 1 + \exp(-2.40 z) = 0$$

### Solution, step 3: Newton-Raphson numerical solution for final attack rate
To solve $f(z) = 0$, the derivative is:
$$f'(z) = 1 - 2.40 \exp(-2.40 z)$$

The Newton-Raphson recursion is:
$$z_{k+1} = z_k - \frac{f(z_k)}{f'(z_k)}$$

- **Iteration 0**: Initial guess $z_0 = 0.80$.
  $$\exp(-2.40 \times 0.80) = \exp(-1.92) \approx 0.146607$$
  $$f(z_0) = 0.80 - 1 + 0.146607 = -0.053393$$
  $$f'(z_0) = 1 - 2.40(0.146607) = 1 - 0.351857 = 0.648143$$
  $$z_1 = 0.80 - \frac{-0.053393}{0.648143} = 0.80 + 0.082378 = 0.882378$$

- **Iteration 1**: $z_1 = 0.882378$.
  $$\exp(-2.40 \times 0.882378) = \exp(-2.117707) \approx 0.120306$$
  $$f(z_1) = 0.882378 - 1 + 0.120306 = 0.002684$$
  $$f'(z_1) = 1 - 2.40(0.120306) = 1 - 0.288734 = 0.711266$$
  $$z_2 = 0.882378 - \frac{0.002684}{0.711266} = 0.882378 - 0.003774 = 0.878604$$

- **Iteration 2**: $z_2 = 0.878604$.
  $$\exp(-2.40 \times 0.878604) = \exp(-2.108650) \approx 0.121401$$
  $$f(z_2) = 0.878604 - 1 + 0.121401 = 0.000005$$
  $$f'(z_2) = 1 - 2.40(0.121401) = 1 - 0.291362 = 0.708638$$
  $$z_3 = 0.878604 - \frac{0.000005}{0.708638} \approx 0.878597 \approx 0.8786$$

**Final Epidemic Outcome**:
The final attack rate converges to $z = 0.8786$ ($87.86\%$).
- Total island residents infected: $N \times z = 10,000 \times 0.8786 = 8,786 \text{ individuals}$.
- Total residents who escape infection completely: $N(1 - z) = 10,000 - 8,786 = 1,214 \text{ individuals}$ ($12.14\%$).

Even with zero medical interventions, isolation, or behavioral changes, the epidemic naturally terminates with $1,214$ healthy people never catching the virus because transmission chains exhaust themselves once population immunity drops effective contact velocity below replacement.
