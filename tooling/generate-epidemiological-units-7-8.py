#!/usr/bin/env python3
"""
Generate Units 7 and 8 of Epidemiological Statistics with high academic depth.
"""
from pathlib import Path

OUT_DIR = Path("publishing/drafts/statistics-probability-epidemiological-statistics")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# UNIT 7
# -------------------------------------------------------------
unit7 = r"""# Unit 7: Infectious Disease Epidemiology: Transmission Dynamics, Compartmental Models & Outbreak Investigation

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
"""

# -------------------------------------------------------------
# UNIT 8
# -------------------------------------------------------------
unit8 = r"""# Unit 8: Survival Analysis in Epidemiology & Causal Inference Frameworks

In longitudinal epidemiology and clinical research, the primary scientific outcome of interest is often not merely whether a disease event occurs, but the exact duration of time that elapses before its occurrence. In oncology, cardiovascular epidemiology, and infectious disease mortality studies, participants enter observation at varying calendar dates, accumulate heterogeneous tracking periods, and may experience censoring due to study termination, migration, or competing risks. To analyze time-to-event data without introducing attrition bias, modern epidemiology relies on **Survival Analysis**. Concurrently, observational epidemiology has undergone a foundational epistemological transformation through the formalization of modern **Causal Inference**. In this culminating unit, we establish the mathematical structures of time-to-event outcomes, formulate right censoring and left truncation, derive the non-parametric Kaplan-Meier product-limit estimator and Greenwood’s variance formula, contrast survival curves using the log-rank test, develop the semi-parametric Cox Proportional Hazards model via partial likelihood, evaluate proportional hazards diagnostics using Schoenfeld residuals, formalize the Neyman-Rubin Potential Outcomes framework, explore causal Directed Acyclic Graphs, and formulate Marginal Structural Models with Inverse Probability of Treatment Weighting (IPTW).

## 8.1 Time-to-Event Data Structures: Hazard Functions, Censoring, and Truncation

Let $T \ge 0$ denote a non-negative continuous random variable representing the time from a well-defined baseline origin (such as date of cancer diagnosis, cardiac surgery, or study enrollment) until the occurrence of a pre-specified clinical event of interest (such as death, relapse, or recovery).

### The Four Fundamental Mathematical Representations
The probability distribution of $T$ is uniquely characterized by four mathematically equivalent functions:
1. **Cumulative Distribution Function** ($F(t)$): The probability that the event occurs on or before time $t$:
   $$F(t) = P(T \le t) = \int_0^t f(u) \, du$$
2. **Survival Function** ($S(t)$): The probability that an individual survives longer than time $t$ (remains event-free):
   $$S(t) = P(T > t) = 1 - F(t) = \int_t^\infty f(u) \, du$$
   Properties: $S(0) = 1$, $\lim_{t \to \infty} S(t) = 0$, and $S(t)$ is non-increasing.
3. **Probability Density Function** ($f(t)$): The unconditional rate of event occurrence per unit time:
   $$f(t) = \frac{dF(t)}{dt} = -\frac{dS(t)}{dt}$$
4. **Hazard Function** ($h(t)$ or $\lambda(t)$): The instantaneous rate of event occurrence at time $t$, conditional upon having survived up to time $t$:
   $$h(t) = \lim_{\Delta t \to 0} \frac{P(t \le T < t + \Delta t \mid T \ge t)}{\Delta t} = \frac{f(t)}{S(t)} = -\frac{1}{S(t)} \frac{dS(t)}{dt} = -\frac{d}{dt} \ln S(t)$$

Integrating the hazard function yields the **Cumulative Hazard Function** ($H(t)$):

$$H(t) = \int_0^t h(u) \, du = -\ln S(t)$$

Exponentiating yields the universal mathematical link connecting survival and hazard:

$$S(t) = \exp(-H(t)) = \exp\left( -\int_0^t h(u) \, du \right)$$

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Parametric Model</th><th>Hazard Function $h(t)$</th><th>Survival Function $S(t)$</th><th>Biological / Clinical Characterization</th></tr>
</thead>
<tbody>
<tr><td><strong>Exponential</strong></td><td>$h(t) = \lambda$ (Constant)</td><td>$S(t) = \exp(-\lambda t)$</td><td>Memoryless process; constant failure risk over time.</td></tr>
<tr><td><strong>Weibull</strong></td><td>$h(t) = \lambda \alpha (\lambda t)^{\alpha - 1}$</td><td>$S(t) = \exp(-(\lambda t)^\alpha)$</td><td>Wear-out ($\alpha > 1$), infant mortality ($\alpha < 1$), or constant ($\alpha = 1$).</td></tr>
<tr><td><strong>Gompertz</strong></td><td>$h(t) = B c^t = B \exp(\alpha t)$</td><td>$S(t) = \exp\left(-\frac{B}{\alpha}(e^{\alpha t} - 1)\right)$</td><td>Human actuarial aging; exponential hazard escalation with age.</td></tr>
</tbody>
</table></div>

### Censoring and Truncation Mechanisms
Survival data are almost never fully observed; they are subject to incomplete observation mechanisms:
- **Right Censoring**: The most prevalent mechanism. The true event time $T_i$ is known only to exceed a recorded censoring time $C_i$ ($T_i > C_i$). Right censoring occurs when a participant reaches the administrative study end date without experiencing the event, migrates away, or dies from an unrelated competing cause. The observed data pair is $(Y_i, \delta_i)$, where:
  $$Y_i = \min(T_i, C_i), \qquad \delta_i = I(T_i \le C_i) \in \{0, 1\}$$
- **Left Truncation (Delayed Entry)**: Occurs when individuals enter observation at an age or time $L_i > 0$ subsequent to the natural origin. Individuals who experience the event prior to $L_i$ are never observed, introducing severe survival selection unless conditioned upon via staggered risk sets ($T_i > L_i$).
- **Informative vs Independent Censoring**: Standard survival methods assume **independent (non-informative) censoring**: conditional on observed covariates $\mathbf{X}$, the event time $T$ and censoring time $C$ are statistically independent ($T \perp C \mid \mathbf{X}$).

## 8.2 Non-Parametric Survival Estimation: The Kaplan-Meier Product-Limit Estimator

When the mathematical functional form of the hazard rate is unknown, imposing parametric distributions (such as the exponential or Weibull) risks severe model misspecification. In 1958, Edward L. Kaplan and Paul Meier formulated the non-parametric **Product-Limit Estimator**.

### Mathematical Derivation of the Kaplan-Meier Estimator
Suppose that in a sample of $n$ individuals, distinct failure events occur at $k$ ordered calendar times:

$$0 < t_1 < t_2 < t_3 < \dots < t_k$$

At each distinct event time $t_j$:
- $d_j$: The number of individuals who experience the event at exactly time $t_j$.
- $Y_j$: The number of individuals who are alive, uncensored, and under active observation immediately prior to time $t_j$ (the **risk set** at $t_j$).
- $c_j$: The number of individuals censored in the half-open interval $[t_j, t_{j+1})$.

The conditional probability of surviving past $t_j$, given survival up to $t_j$, is non-parametrically estimated as:

$$p_j = 1 - \frac{d_j}{Y_j} = \frac{Y_j - d_j}{Y_j}$$

By the chain rule of conditional probabilities, the overall probability of surviving past any arbitrary time $t$ is the product of all conditional survival probabilities up to time $t$:

$$\widehat{S}_{KM}(t) = \prod_{j : t_j \le t} \left( 1 - \frac{d_j}{Y_j} \right) = \prod_{j : t_j \le t} \left( \frac{Y_j - d_j}{Y_j} \right)$$

The Kaplan-Meier curve is a step function that starts at $\widehat{S}(0) = 1.0$ and steps downward exclusively at each observed failure time $t_j$, with vertical step magnitude proportional to $d_j / Y_j$. Censored observations do not trigger steps; instead, they reduce the size of the risk set $Y_{j+1}$ for subsequent intervals.

### Greenwood's Formula for Sampling Variance
Major Greenwood (1926) derived the asymptotic sampling variance of the product-limit survival estimator using the delta method on the log-transformed survival function $\ln \widehat{S}(t) = \sum_{j : t_j \le t} \ln(1 - d_j / Y_j)$. Treating each conditional failure count as an independent binomial realization:

$$\text{Var}(\ln \widehat{S}(t)) \approx \sum_{j : t_j \le t} \text{Var}\left( \ln\left(1 - \frac{d_j}{Y_j}\right) \right) \approx \sum_{j : t_j \le t} \frac{d_j}{Y_j (Y_j - d_j)}$$

Applying the delta method again to $\exp(\ln \widehat{S}(t))$ yields **Greenwood’s Formula**:

$$\widehat{\text{Var}}(\widehat{S}_{KM}(t)) = [\widehat{S}_{KM}(t)]^2 \sum_{j : t_j \le t} \frac{d_j}{Y_j (Y_j - d_j)}$$

The standard Greenwood 95% Wald confidence interval is $\widehat{S}(t) \pm 1.96 \sqrt{\widehat{\text{Var}}(\widehat{S}(t))}$. To prevent confidence intervals from overshooting the unit boundaries $[0, 1]$, modern software applies the log-log transformation $g(S) = \ln(-\ln S)$.

## 8.3 Group Comparisons: The Non-Parametric Log-Rank Hypothesis Test

In randomized oncology trials and comparative cohort studies, a central task is testing whether two or more survival curves differ significantly across the entire follow-up history ($H_0: S_1(t) = S_2(t) \quad \forall t$).

### The Mantel-Cox Log-Rank Test
Nathan Mantel (1966) and David Cox (1972) formulated the **Log-Rank Test** by constructing a $2 \times 2$ contingency table at each distinct failure time $t_j$:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Group</th><th>Events at $t_j$</th><th>Surviving at $t_j$</th><th>Risk Set at $t_j$</th></tr>
</thead>
<tbody>
<tr><td><strong>Group 1 (Treatment)</strong></td><td>$d_{1j}$</td><td>$Y_{1j} - d_{1j}$</td><td>$Y_{1j}$</td></tr>
<tr><td><strong>Group 2 (Control)</strong></td><td>$d_{2j}$</td><td>$Y_{2j} - d_{2j}$</td><td>$Y_{2j}$</td></tr>
<tr><td><strong>Total</strong></td><td>$d_j = d_{1j} + d_{2j}$</td><td>$Y_j - d_j$</td><td>$Y_j = Y_{1j} + Y_{2j}$</td></tr>
</tbody>
</table></div>

Under the null hypothesis of equal hazard rates ($H_0: h_1(t) = h_2(t)$), the number of events in Group 1 at time $t_j$ follows a hypergeometric distribution conditional upon marginal totals. The expected number of events in Group 1 is:

$$E_{1j} = \mathbb{E}[d_{1j} \mid H_0] = d_j \frac{Y_{1j}}{Y_j}$$

The conditional hypergeometric variance is:

$$V_{1j} = \text{Var}(d_{1j} \mid H_0) = \frac{Y_{1j} Y_{2j} d_j (Y_j - d_j)}{Y_j^2 (Y_j - 1)}$$

Summing over all distinct failure times $t_1, \dots, t_k$:
$$O_1 = \sum_{j=1}^k d_{1j}, \qquad E_1 = \sum_{j=1}^k E_{1j}, \qquad V_1 = \sum_{j=1}^k V_{1j}$$

The **Log-Rank Test Statistic** is:

$$\chi^2_{\text{log-rank}} = \frac{(O_1 - E_1)^2}{V_1}$$

Under $H_0$, $\chi^2_{\text{log-rank}}$ asymptotically follows a chi-square distribution with $1$ degree of freedom. An approximate estimate of the Hazard Ratio is obtained as:

$$\widehat{HR} \approx \frac{O_1 / E_1}{O_2 / E_2}$$

The log-rank test places equal weight on events across all time points, making it the most statistically powerful test under proportional hazards alternatives.

## 8.4 The Cox Proportional Hazards Semi-Parametric Regression Model

While the log-rank test evaluates binary or categorical group differences, it cannot adjust for continuous confounders or evaluate multiple prognostic variables simultaneously. In 1972, Sir David Cox revolutionized survival analysis by formulating the **Proportional Hazards Regression Model**.

### Model Specification
The Cox model postulates that the hazard of disease for an individual with covariate vector $\mathbf{x}_i = (x_{i1}, \dots, x_{ip})^T$ is the product of an unspecified non-parametric baseline hazard and an exponential parametric function:

$$h(t \mid \mathbf{x}_i) = h_0(t) \exp(\mathbf{x}_i^T \boldsymbol{\beta}) = h_0(t) \exp(\beta_1 x_{i1} + \dots + \beta_p x_{ip})$$

where:
- $h_0(t)$: The **baseline hazard function**, representing the hazard for an individual whose covariates are all zero ($\mathbf{x} = \mathbf{0}$). It is left completely unspecified, requiring no parametric distributional assumptions!
- $\exp(\mathbf{x}_i^T \boldsymbol{\beta})$: The relative hazard (risk multiplier), which is strictly parametric and time-invariant.

The model is **semi-parametric** because it pairs an infinite-dimensional non-parametric baseline hazard $h_0(t)$ with finite-dimensional regression coefficients $\boldsymbol{\beta}$.

### The Proportional Hazards Property
Consider two individuals with covariate vectors $\mathbf{x}_1$ and $\mathbf{x}_0$. The ratio of their hazards is:

$$\frac{h(t \mid \mathbf{x}_1)}{h(t \mid \mathbf{x}_0)} = \frac{h_0(t) \exp(\mathbf{x}_1^T \boldsymbol{\beta})}{h_0(t) \exp(\mathbf{x}_0^T \boldsymbol{\beta})} = \exp((\mathbf{x}_1 - \mathbf{x}_0)^T \boldsymbol{\beta})$$

Notice that the baseline hazard $h_0(t)$ cancels out completely! The **Hazard Ratio** ($HR$) is strictly constant over time: the hazard curves for any two individuals remain strictly proportional across the entire observational horizon.

### Maximum Partial Likelihood Estimation
Cox’s mathematical genius lay in demonstrating that $\boldsymbol{\beta}$ can be estimated without knowing or estimating $h_0(t)$ through the method of **Partial Likelihood**.

Suppose failure events occur at $k$ distinct ordered times $t_1 < \dots < t_k$. At failure time $t_j$, let $\mathcal{R}(t_j)$ denote the risk set of all individuals alive and under observation immediately prior to $t_j$. Conditional on an event occurring at $t_j$, the probability that the event occurs to the specific individual $j$ who actually failed is:

$$P(\text{Individual } j \text{ fails} \mid \text{One failure in } \mathcal{R}(t_j)) = \frac{h(t_j \mid \mathbf{x}_j)}{\sum_{m \in \mathcal{R}(t_j)} h(t_j \mid \mathbf{x}_m)} = \frac{h_0(t_j) \exp(\mathbf{x}_j^T \boldsymbol{\beta})}{\sum_{m \in \mathcal{R}(t_j)} h_0(t_j) \exp(\mathbf{x}_m^T \boldsymbol{\beta})}$$

Canceling $h_0(t_j)$:

$$L_j(\boldsymbol{\beta}) = \frac{\exp(\mathbf{x}_j^T \boldsymbol{\beta})}{\sum_{m \in \mathcal{R}(t_j)} \exp(\mathbf{x}_m^T \boldsymbol{\beta})}$$

The **Partial Likelihood** is the product across all $k$ failure events:

$$L_{\text{partial}}(\boldsymbol{\beta}) = \prod_{j=1}^k \frac{\exp(\mathbf{x}_j^T \boldsymbol{\beta})}{\sum_{m \in \mathcal{R}(t_j)} \exp(\mathbf{x}_m^T \boldsymbol{\beta})}$$

Maximizing the partial log-likelihood $\ell_{\text{partial}}(\boldsymbol{\beta})$ via Newton-Raphson yields estimators that are asymptotically unbiased, normally distributed, and achieve full semiparametric efficiency.

## 8.5 Model Diagnostics for Proportional Hazards: Schoenfeld Residuals

The validity of the Cox model depends on the strict satisfaction of the **Proportional Hazards (PH) assumption**. If the true hazard ratio varies over time (for example, if a surgical intervention carries high immediate perioperative mortality but strong long-term survival benefit), the baseline model fails.

### Schoenfeld Residuals
David Schoenfeld (1982) formulated residuals defined exclusively at observed failure times. For covariate $k$ and failure event $j$:

$$r_{jk} = x_{jk} - \mathbb{E}[X_k \mid \mathcal{R}(t_j)] = x_{jk} - \frac{\sum_{m \in \mathcal{R}(t_j)} x_{mk} \exp(\mathbf{x}_m^T \widehat{\boldsymbol{\beta}})}{\sum_{m \in \mathcal{R}(t_j)} \exp(\mathbf{x}_m^T \widehat{\boldsymbol{\beta}})}$$

The Schoenfeld residual represents the difference between the actual covariate value of the failing individual and the risk-weighted average of that covariate across the active risk set at that moment.

Under the proportional hazards assumption:
- Schoenfeld residuals have an expected value of zero ($\mathbb{E}[r_{jk}] = 0$) across all failure times.
- A plot of scaled Schoenfeld residuals against time (or log-time) should trace a flat, horizontal line with slope zero.
- Grambsch and Therneau (1994) formulated a formal score test of non-zero slope: if $p < 0.05$, the proportional hazards assumption is rejected.

When the PH assumption is violated, epidemiologists resolve the non-proportionality by:
1. Including time-varying covariates ($x_j \times \ln t$).
2. Fitting **Stratified Cox Models**, allowing the baseline hazard $h_{0g}(t)$ to differ across strata.
3. Fitting Accelerated Failure Time (AFT) models.

## 8.6 Counterfactual Causal Inference: Potential Outcomes, Exchangeability & IPTW

Observational epidemiology has increasingly embraced the formal mathematical language of **Causal Inference**, rooted in Donald Rubin’s Potential Outcomes model and Judea Pearl’s structural causal frameworks.

### The Three Identifiability Conditions
To identify the Average Causal Effect ($ACE = \mathbb{E}[Y(1)] - \mathbb{E}[Y(0)]$) from observational data, three foundational conditions must hold:
1. **Consistency**: An individual's observed outcome under observed exposure $A = a$ equals their potential counterfactual outcome under that exposure level: $Y = Y(a)$. This requires well-defined interventions with no hidden variations of treatment.
2. **Conditional Exchangeability (No Unmeasured Confounding)**: Conditional on a measured set of baseline covariates $\mathbf{L}$, the potential outcomes are statistically independent of the treatment assignment:
   $$Y(a) \perp A \mid \mathbf{L} \quad \forall a \in \{0, 1\}$$
3. **Positivity**: Every individual in the population has a non-zero probability of receiving every treatment level:
   $$0 < P(A = 1 \mid \mathbf{L} = \mathbf{l}) < 1 \quad \forall \mathbf{l} \text{ such that } P(\mathbf{L} = \mathbf{l}) > 0$$

### Marginal Structural Models and Inverse Probability of Treatment Weighting (IPTW)
When an observational study involves time-varying exposures and time-varying confounders that are themselves affected by prior exposure (such as CD4 counts in longitudinal HIV studies), standard multivariable regression models fail catastrophically: conditioning on the time-varying confounder introduces collider bias, while omitting it leaves confounding unadjusted.

James Robins (2000) resolved this dilemma through **Inverse Probability of Treatment Weighting (IPTW)**. The **propensity score** is the conditional probability of receiving treatment given baseline covariates:

$$e(\mathbf{L}_i) = P(A_i = 1 \mid \mathbf{L}_i)$$

Each participant is assigned a statistical weight equal to the inverse of the probability of receiving the treatment they actually received:

$$W_i = \frac{A_i}{e(\mathbf{L}_i)} + \frac{1 - A_i}{1 - e(\mathbf{L}_i)}$$

Weighting creates a **pseudo-population** in which the association between confounders $\mathbf{L}$ and exposure $A$ is completely severed. In this re-weighted pseudo-population, a simple unadjusted regression of outcome $Y$ on exposure $A$ (a **Marginal Structural Model**) yields a mathematically unconfounded, asymptotically unbiased estimate of the true average causal effect.

## Fully worked question 1: Complete Kaplan-Meier Survival Analysis with Greenwood Confidence Bands and Median Survival

### Question
A phase II randomized oncology trial at the National Institute of Cancer Research and Hospital (NICRH) in Dhaka evaluates a novel targeted tyrosine kinase inhibitor (TKI) in $n = 10$ advanced non-small cell lung cancer patients. Patients are enrolled and monitored over a 36-month follow-up window. The recorded event and censoring times (in months from treatment initiation) are:
- Patient 1: Died at $t = 4.0\text{ months}$
- Patient 2: Died at $t = 7.0\text{ months}$
- Patient 3: Censored (loss to follow-up) at $t = 9.0\text{ months}$
- Patient 4: Died at $t = 12.0\text{ months}$
- Patient 5: Censored (study termination) at $t = 15.0\text{ months}$
- Patient 6: Died at $t = 18.0\text{ months}$
- Patient 7: Died at $t = 22.0\text{ months}$
- Patient 8: Censored (withdrew consent) at $t = 26.0\text{ months}$
- Patient 9: Died at $t = 30.0\text{ months}$
- Patient 10: Censored (study termination) at $t = 36.0\text{ months}$

1. Construct the complete Kaplan-Meier life table: for each distinct failure time, record the risk set $Y_j$, event count $d_j$, conditional survival probability $p_j$, and cumulative survival probability $\widehat{S}_{KM}(t)$.
2. Calculate Greenwood’s standard error and construct the 95% Wald confidence interval for the 18-month survival probability $\widehat{S}(18)$.
3. Determine the empirical median survival time with its definition, and calculate the cumulative hazard $\widehat{H}(30)$ via the Nelson-Aalen estimator.

### Solution, step 1: Construct the Kaplan-Meier life table
Chronologically order all event times and censoring times:
- $t = 4.0$: 1 death ($d=1$)
- $t = 7.0$: 1 death ($d=1$)
- $t = 9.0$: 1 censored ($c=1$)
- $t = 12.0$: 1 death ($d=1$)
- $t = 15.0$: 1 censored ($c=1$)
- $t = 18.0$: 1 death ($d=1$)
- $t = 22.0$: 1 death ($d=1$)
- $t = 26.0$: 1 censored ($c=1$)
- $t = 30.0$: 1 death ($d=1$)
- $t = 36.0$: 1 censored ($c=1$)

Evaluate the distinct failure times $t_j$:
1. **$t_1 = 4.0$**: Risk set $Y_1 = 10$, deaths $d_1 = 1$.
   $$p_1 = 1 - 1/10 = 0.9000 \implies \widehat{S}(4) = 0.9000 \quad (90.00\%)$$
2. **$t_2 = 7.0$**: Risk set $Y_2 = 9$, deaths $d_2 = 1$.
   $$p_2 = 1 - 1/9 = 8/9 \approx 0.8889 \implies \widehat{S}(7) = 0.9000 \times (8/9) = 0.8000 \quad (80.00\%)$$
   *(Note: at $t = 9.0$, Patient 3 is censored; risk set drops from 8 to 7 without altering $\widehat{S}$)*
3. **$t_3 = 12.0$**: Risk set $Y_3 = 7$, deaths $d_3 = 1$.
   $$p_3 = 1 - 1/7 = 6/7 \approx 0.8571 \implies \widehat{S}(12) = 0.8000 \times (6/7) = 0.6857 \quad (68.57\%)$$
   *(Note: at $t = 15.0$, Patient 5 is censored; risk set drops from 6 to 5)*
4. **$t_4 = 18.0$**: Risk set $Y_4 = 5$, deaths $d_4 = 1$.
   $$p_4 = 1 - 1/5 = 0.8000 \implies \widehat{S}(18) = 0.6857 \times 0.8000 \approx 0.5486 \quad (54.86\%)$$
5. **$t_5 = 22.0$**: Risk set $Y_5 = 4$, deaths $d_5 = 1$.
   $$p_5 = 1 - 1/4 = 0.7500 \implies \widehat{S}(22) = 0.5486 \times 0.7500 \approx 0.4114 \quad (41.14\%)$$
   *(Note: at $t = 26.0$, Patient 8 is censored; risk set drops from 3 to 2)*
6. **$t_6 = 30.0$**: Risk set $Y_6 = 2$, deaths $d_6 = 1$.
   $$p_6 = 1 - 1/2 = 0.5000 \implies \widehat{S}(30) = 0.4114 \times 0.5000 \approx 0.2057 \quad (20.57\%)$$

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Failure Time $t_j$</th><th>Risk Set $Y_j$</th><th>Deaths $d_j$</th><th>Censored $c_j$</th><th>Conditional Survival $p_j$</th><th>Cumulative Survival $\widehat{S}_{KM}(t)$</th></tr>
</thead>
<tbody>
<tr><td>$0.0$</td><td>$10$</td><td>$0$</td><td>$0$</td><td>$1.0000$</td><td>$1.0000$</td></tr>
<tr><td>$4.0$</td><td>$10$</td><td>$1$</td><td>$0$</td><td>$0.9000$</td><td>$0.9000$</td></tr>
<tr><td>$7.0$</td><td>$9$</td><td>$1$</td><td>$1$ ($t=9$)</td><td>$0.8889$</td><td>$0.8000$</td></tr>
<tr><td>$12.0$</td><td>$7$</td><td>$1$</td><td>$1$ ($t=15$)</td><td>$0.8571$</td><td>$0.6857$</td></tr>
<tr><td>$18.0$</td><td>$5$</td><td>$1$</td><td>$0$</td><td>$0.8000$</td><td>$0.5486$</td></tr>
<tr><td>$22.0$</td><td>$4$</td><td>$1$</td><td>$1$ ($t=26$)</td><td>$0.7500$</td><td>$0.4114$</td></tr>
<tr><td>$30.0$</td><td>$2$</td><td>$1$</td><td>$1$ ($t=36$)</td><td>$0.5000$</td><td>$0.2057$</td></tr>
</tbody>
</table></div>

### Solution, step 2: Greenwood variance and 95% confidence interval at t = 18 months
At $t = 18.0\text{ months}$, $\widehat{S}(18) = 0.5486$. We evaluate the Greenwood summation across the four failure events up to month 18:

$$\sum_{j=1}^4 \frac{d_j}{Y_j (Y_j - d_j)} = \frac{1}{10(9)} + \frac{1}{9(8)} + \frac{1}{7(6)} + \frac{1}{5(4)}$$
$$= \frac{1}{90} + \frac{1}{72} + \frac{1}{42} + \frac{1}{20} = 0.01111 + 0.01389 + 0.02381 + 0.05000 = 0.09881$$

Applying Greenwood's formula:
$$\widehat{\text{Var}}(\widehat{S}(18)) = [\widehat{S}(18)]^2 \times 0.09881 = (0.5486)^2 \times 0.09881 = (0.30096) \times 0.09881 \approx 0.029738$$

The standard error is:
$$\text{SE}(\widehat{S}(18)) = \sqrt{0.029738} \approx 0.1724 \quad (17.24\%)$$

The 95% Wald confidence interval is:
$$\widehat{S}(18) \pm 1.96 \times \text{SE}(\widehat{S}(18)) = 0.5486 \pm 1.96(0.1724) = 0.5486 \pm 0.3379 = [0.2107, \, 0.8865]$$
We estimate with 95% confidence that the 18-month survival probability lies between $21.1\%$ and $88.7\%$.

### Solution, step 3: Median survival time and Nelson-Aalen cumulative hazard
1. **Median Survival Time**:
   The median survival time $\hat{t}_{\text{med}}$ is defined as the earliest time at which the survival probability drops to or below $0.50$ ($\widehat{S}(t) \le 0.50$).
   From the life table:
   - At $t = 18.0\text{ months}$, $\widehat{S}(18) = 0.5486 > 0.50$.
   - At $t = 22.0\text{ months}$, $\widehat{S}(22) = 0.4114 \le 0.50$.
   Therefore, the empirical median survival time is **$22.0\text{ months}$**.

2. **Nelson-Aalen Cumulative Hazard at 30 Months**:
   The Nelson-Aalen estimator sums the hazard increments $d_j / Y_j$ across all six failure times:
   $$\widehat{H}_{NA}(30) = \sum_{j=1}^6 \frac{d_j}{Y_j} = \frac{1}{10} + \frac{1}{9} + \frac{1}{7} + \frac{1}{5} + \frac{1}{4} + \frac{1}{2}$$
   $$= 0.1000 + 0.1111 + 0.1429 + 0.2000 + 0.2500 + 0.5000 = 1.3040$$
   The estimated cumulative hazard at 30 months is $1.304$. (Notice that $\exp(-\widehat{H}_{NA}(30)) = \exp(-1.3040) \approx 0.2714$, closely tracking the Kaplan-Meier estimate).

## Fully worked question 2: The Log-Rank Hypothesis Test for Stratified Survival Curves in Clinical Oncology

### Question
A phase III multicenter randomized clinical trial compares a combination immunotherapy regimen (Nivolumab + Ipilimumab, Group 1) against standard chemotherapy (Dacarbazine, Group 2) in $N = 40$ metastatic melanoma patients. Patients are monitored until death or censoring. Over the observation period, 10 distinct failure times occur. The recorded event data across the risk sets are:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Failure Time ($t_j$, months)</th><th>Total Risk Set ($Y_j$)</th><th>Total Deaths ($d_j$)</th><th>Group 1 Risk Set ($Y_{1j}$)</th><th>Group 1 Deaths ($d_{1j}$)</th><th>Group 2 Risk Set ($Y_{2j}$)</th><th>Group 2 Deaths ($d_{2j}$)</th></tr>
</thead>
<tbody>
<tr><td>$2.0$</td><td>$40$</td><td>$2$</td><td>$20$</td><td>$0$</td><td>$20$</td><td>$2$</td></tr>
<tr><td>$4.0$</td><td>$38$</td><td>$3$</td><td>$20$</td><td>$1$</td><td>$18$</td><td>$2$</td></tr>
<tr><td>$6.0$</td><td>$34$</td><td>$2$</td><td>$19$</td><td>$0$</td><td>$15$</td><td>$2$</td></tr>
<tr><td>$8.0$</td><td>$30$</td><td>$4$</td><td>$18$</td><td>$1$</td><td>$12$</td><td>$3$</td></tr>
<tr><td>$12.0$</td><td>$25$</td><td>$3$</td><td>$17$</td><td>$1$</td><td>$8$</td><td>$2$</td></tr>
<tr><td>$15.0$</td><td>$20$</td><td>$2$</td><td>$15$</td><td>$0$</td><td>$5$</td><td>$2$</td></tr>
<tr><td>$18.0$</td><td>$16$</td><td>$2$</td><td>$14$</td><td>$1$</td><td>$2$</td><td>$1$</td></tr>
<tr><td>$24.0$</td><td>$13$</td><td>$1$</td><td>$12$</td><td>$0$</td><td>$1$</td><td>$1$</td></tr>
<tr><td>$30.0$</td><td>$11$</td><td>$1$</td><td>$11$</td><td>$1$</td><td>$0$</td><td>$0$</td></tr>
<tr><td>$36.0$</td><td>$8$</td><td>$1$</td><td>$8$</td><td>$1$</td><td>$0$</td><td>$0$</td></tr>
</tbody>
</table></div>

1. Under the null hypothesis of identical survival curves ($H_0: S_1(t) = S_2(t)$), calculate the expected number of deaths in Group 1 ($E_{1j}$) and the conditional hypergeometric variance ($V_{1j}$) for each failure time.
2. Sum these quantities to evaluate total observed deaths ($O_1$), total expected deaths ($E_1$), and total variance ($V_1$). Compute the Mantel-Cox **Log-Rank Test Statistic** $\chi^2_{\text{log-rank}}$.
3. Formulate the statistical hypothesis, determine the critical value at significance level $\alpha = 0.01$, and estimate the approximate Hazard Ratio ($HR$) comparing immunotherapy to chemotherapy.

### Solution, step 1: Calculate expected deaths and hypergeometric variances
For each failure time $j$, evaluate:
$$E_{1j} = d_j \frac{Y_{1j}}{Y_j}, \qquad V_{1j} = \frac{Y_{1j} Y_{2j} d_j (Y_j - d_j)}{Y_j^2 (Y_j - 1)}$$

1. **$t = 2.0$**: $Y=40, d=2, Y_1=20, Y_2=20, d_1=0$.
   $$E_{11} = 2 \times \frac{20}{40} = 1.0000$$
   $$V_{11} = \frac{(20)(20)(2)(38)}{(40)^2 (39)} = \frac{30,400}{62,400} \approx 0.4872$$
2. **$t = 4.0$**: $Y=38, d=3, Y_1=20, Y_2=18, d_1=1$.
   $$E_{12} = 3 \times \frac{20}{38} \approx 1.5789$$
   $$V_{12} = \frac{(20)(18)(3)(35)}{(38)^2 (37)} = \frac{37,800}{53,428} \approx 0.7075$$
3. **$t = 6.0$**: $Y=34, d=2, Y_1=19, Y_2=15, d_1=0$.
   $$E_{13} = 2 \times \frac{19}{34} \approx 1.1176$$
   $$V_{13} = \frac{(19)(15)(2)(32)}{(34)^2 (33)} = \frac{18,240}{38,148} \approx 0.4781$$
4. **$t = 8.0$**: $Y=30, d=4, Y_1=18, Y_2=12, d_1=1$.
   $$E_{14} = 4 \times \frac{18}{30} = 2.4000$$
   $$V_{14} = \frac{(18)(12)(4)(26)}{(30)^2 (29)} = \frac{22,464}{26,100} \approx 0.8607$$
5. **$t = 12.0$**: $Y=25, d=3, Y_1=17, Y_2=8, d_1=1$.
   $$E_{15} = 3 \times \frac{17}{25} = 2.0400$$
   $$V_{15} = \frac{(17)(8)(3)(22)}{(25)^2 (24)} = \frac{8,976}{15,000} \approx 0.5984$$
6. **$t = 15.0$**: $Y=20, d=2, Y_1=15, Y_2=5, d_1=0$.
   $$E_{16} = 2 \times \frac{15}{20} = 1.5000$$
   $$V_{16} = \frac{(15)(5)(2)(18)}{(20)^2 (19)} = \frac{2,700}{7,600} \approx 0.3553$$
7. **$t = 18.0$**: $Y=16, d=2, Y_1=14, Y_2=2, d_1=1$.
   $$E_{17} = 2 \times \frac{14}{16} = 1.7500$$
   $$V_{17} = \frac{(14)(2)(2)(14)}{(16)^2 (15)} = \frac{784}{3,840} \approx 0.2042$$
8. **$t = 24.0$**: $Y=13, d=1, Y_1=12, Y_2=1, d_1=0$.
   $$E_{18} = 1 \times \frac{12}{13} \approx 0.9231$$
   $$V_{18} = \frac{(12)(1)(1)(12)}{(13)^2 (12)} = \frac{144}{2,028} \approx 0.0710$$
9. **$t = 30.0$**: $Y=11, d=1, Y_1=11, Y_2=0, d_1=1$.
   $$E_{19} = 1 \times \frac{11}{11} = 1.0000, \quad V_{19} = 0$$
10. **$t = 36.0$**: $Y=8, d=1, Y_1=8, Y_2=0, d_1=1$.
    $$E_{1,10} = 1 \times \frac{8}{8} = 1.0000, \quad V_{1,10} = 0$$

### Solution, step 2: Sum totals and log-rank test statistic
Total observed deaths in Group 1:
$$O_1 = \sum_{j=1}^{10} d_{1j} = 0 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 = 6 \text{ deaths}$$

Total expected deaths in Group 1:
$$E_1 = \sum_{j=1}^{10} E_{1j} = 1.0000 + 1.5789 + 1.1176 + 2.4000 + 2.0400 + 1.5000 + 1.7500 + 0.9231 + 1.0000 + 1.0000 = 14.3096$$

Total hypergeometric variance:
$$V_1 = \sum_{j=1}^{10} V_{1j} = 0.4872 + 0.7075 + 0.4781 + 0.8607 + 0.5984 + 0.3553 + 0.2042 + 0.0710 + 0 + 0 = 3.7624$$

The Log-Rank Test Statistic is:
$$\chi^2_{\text{log-rank}} = \frac{(O_1 - E_1)^2}{V_1} = \frac{(6 - 14.3096)^2}{3.7624} = \frac{(-8.3096)^2}{3.7624} = \frac{69.0495}{3.7624} \approx 18.352$$

### Solution, step 3: Hypothesis testing and Hazard Ratio estimation
- Null Hypothesis: $H_0: S_1(t) = S_2(t)$ (no survival difference).
- Alternative Hypothesis: $H_1: S_1(t) \neq S_2(t)$.
- Critical Value at $\alpha = 0.01$ with $df = 1$: $\chi^2_{0.01, 1} = 6.635$.

Since $\chi^2_{\text{log-rank}} = 18.35 \gg 6.635$ ($p = 1.8 \times 10^{-5}$), we decisively reject the null hypothesis at the $1\%$ significance level.

**Approximate Hazard Ratio Estimation**:
Total deaths in the study: $D_{\text{total}} = 2 + 3 + 2 + 4 + 3 + 2 + 2 + 1 + 1 + 1 = 21$.
- Group 1: $O_1 = 6, E_1 = 14.31$
- Group 2: $O_2 = 21 - 6 = 15, \quad E_2 = 21 - 14.3096 = 6.6904$

$$\widehat{HR} \approx \frac{O_1 / E_1}{O_2 / E_2} = \frac{6 / 14.3096}{15 / 6.6904} = \frac{0.4193}{2.2420} \approx 0.1870 \approx 0.19$$

The combination immunotherapy reduces the instantaneous hazard of death by approximately $81.3\%$ ($\widehat{HR} \approx 0.19$, $p < 0.0001$) compared to standard chemotherapy in metastatic melanoma.

## Fully worked question 3: Cox Proportional Hazards Model: Partial Likelihood, Hazard Ratios, and Schoenfeld Diagnostics

### Question
A specialized cardiovascular epidemiologic study tracks $N = 1,200$ post-percutaneous coronary intervention (PCI) patients over 5 years to evaluate the impact of diabetes mellitus ($X_1 = 1$ for diabetic, $0$ for non-diabetic) on all-cause mortality, adjusting for age in years ($X_2$) and left ventricular ejection fraction percentage ($X_3$, LVEF%). A multivariable Cox proportional hazards model is fitted:
$$h(t \mid \mathbf{X}) = h_0(t) \exp(\beta_1 X_1 + \beta_2 X_2 + \beta_3 X_3)$$

The Maximum Partial Likelihood estimation results are:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Covariate</th><th>Parameter</th><th>Estimate $\widehat{\beta}_j$</th><th>Standard Error $\text{SE}(\widehat{\beta}_j)$</th><th>Wald $z$</th><th>$p$-value</th></tr>
</thead>
<tbody>
<tr><td>Diabetes ($X_1$)</td><td>$\beta_1$</td><td>$+0.6931$</td><td>$0.1450$</td><td>$4.780$</td><td>$< 0.0001$</td></tr>
<tr><td>Age per Year ($X_2$)</td><td>$\beta_2$</td><td>$+0.0488$</td><td>$0.0120$</td><td>$4.067$</td><td>$< 0.0001$</td></tr>
<tr><td>LVEF per 5% Increase ($X_3$)</td><td>$\beta_3$</td><td>$-0.2231$</td><td>$0.0510$</td><td>$-4.375$</td><td>$< 0.0001$</td></tr>
</tbody>
</table></div>

1. Compute the adjusted Hazard Ratios ($HR$) and 95% confidence intervals for diabetes, a 10-year increase in age ($\Delta X_2 = 10$), and a 10% increase in LVEF ($\Delta X_3 = 2$ units of 5%).
2. Interpret the biological and clinical meaning of each estimated hazard ratio.
3. To evaluate the proportional hazards assumption for Diabetes, the biostatistician plots the scaled Schoenfeld residuals against time and runs Grambsch-Therneau tests:
   - For Diabetes ($X_1$): Test correlation $\rho = 0.032, \quad \chi^2 = 0.22, \quad p = 0.639$.
   - For Age ($X_2$): Test correlation $\rho = -0.015, \quad \chi^2 = 0.05, \quad p = 0.823$.
   - For LVEF ($X_3$): Test correlation $\rho = 0.041, \quad \chi^2 = 0.36, \quad p = 0.548$.
   - Global test: $\chi^2 = 0.68, \quad df = 3, \quad p = 0.878$.
   Interpret these diagnostic tests: is the proportional hazards assumption satisfied?

### Solution, step 1: Compute adjusted Hazard Ratios and 95% confidence intervals
1. **Diabetes Mellitus ($X_1$)**:
   $$\widehat{HR}_1 = \exp(\widehat{\beta}_1) = \exp(0.6931) = 2.000$$
   $$\text{95\% CI} = \exp(0.6931 \pm 1.96 \times 0.1450) = \exp(0.6931 \pm 0.2842) = [\exp(0.4089), \, \exp(0.9773)] = [1.505, \, 2.657]$$
   $$\text{Adjusted } HR = 2.00 \quad (95\%\text{ CI}: [1.51, \, 2.66])$$

2. **Age per 10-Year Increase ($\Delta X_2 = 10$)**:
   $$\widehat{\beta}_{2, \, 10\text{ yr}} = 10 \times 0.0488 = 0.4880$$
   $$\text{SE}(10 \widehat{\beta}_2) = 10 \times 0.0120 = 0.1200$$
   $$\widehat{HR}_{2, \, 10\text{ yr}} = \exp(0.4880) \approx 1.629$$
   $$\text{95\% CI} = \exp(0.4880 \pm 1.96 \times 0.1200) = \exp(0.4880 \pm 0.2352) = [\exp(0.2528), \, \exp(0.7232)] = [1.288, \, 2.061]$$
   $$\text{Adjusted } HR = 1.63 \quad (95\%\text{ CI}: [1.29, \, 2.06])$$

3. **LVEF per 10% Increase ($\Delta X_3 = 2$ units of $5\%$)**:
   $$\widehat{\beta}_{3, \, 10\%} = 2 \times (-0.2231) = -0.4462$$
   $$\text{SE}(2 \widehat{\beta}_3) = 2 \times 0.0510 = 0.1020$$
   $$\widehat{HR}_{3, \, 10\%} = \exp(-0.4462) \approx 0.6401$$
   $$\text{95\% CI} = \exp(-0.4462 \pm 1.96 \times 0.1020) = \exp(-0.4462 \pm 0.1999) = [\exp(-0.6461), \, \exp(-0.2463)] = [0.524, \, 0.782]$$
   $$\text{Adjusted } HR = 0.64 \quad (95\%\text{ CI}: [0.52, \, 0.78])$$

### Solution, step 2: Epidemiological and clinical interpretation
1. **Diabetes**: Holding age and ejection fraction constant, diabetic post-PCI patients suffer **twice the instantaneous hazard of all-cause mortality** at any given point in time compared to non-diabetics ($HR = 2.00, p < 0.0001$).
2. **Age**: Each 10-year advance in patient age increases the instantaneous mortality hazard by $62.9\%$ ($HR = 1.63, p < 0.0001$).
3. **Ejection Fraction (LVEF)**: LVEF is strongly protective: every $10\%$ absolute preservation in left ventricular ejection fraction reduces the mortality hazard by $36.0\%$ ($HR = 0.64, p < 0.0001$).

### Solution, step 3: Evaluation of Schoenfeld residual diagnostics
The Grambsch-Therneau test evaluates the correlation between scaled Schoenfeld residuals and survival time:
- The null hypothesis $H_0$ states that the correlation is zero (the hazard ratio is strictly constant over time).
- For Diabetes ($X_1$), the test yields $\chi^2 = 0.22, p = 0.639$.
- For Age ($X_2$), $\chi^2 = 0.05, p = 0.823$.
- For LVEF ($X_3$), $\chi^2 = 0.36, p = 0.548$.
- The global test across all covariates simultaneously yields $\chi^2 = 0.68, p = 0.878$.

**Diagnostic Conclusion**:
Because all individual $p$-values and the global test $p$-value are far greater than $\alpha = 0.05$, there is **zero evidence of non-proportional hazards**. The hazard ratios for diabetes, age, and ejection fraction remain remarkably stable across the entire 5-year observation period, confirming the complete mathematical and clinical validity of the fitted Cox model.
"""

(OUT_DIR / "unit-7.md").write_text(unit7.strip() + "\n", encoding="utf-8")
(OUT_DIR / "unit-8.md").write_text(unit8.strip() + "\n", encoding="utf-8")
print("Units 7 and 8 written.")
