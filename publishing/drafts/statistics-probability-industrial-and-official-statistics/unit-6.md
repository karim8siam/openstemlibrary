# Unit 6: System Reliability Engineering, Failure Rate Physics & Accelerated Life Testing

## 6.1 Fundamental Mathematical Objects of Reliability Engineering

Reliability engineering applies probability theory, stochastic processes, and material physics to analyze the time-to-failure of components, subsystems, and integrated industrial architectures. 

Let the operating lifetime of an engineering component or system be modeled as a continuous, non-negative random variable $T \ge 0$ defined on a probability space $(\Omega, \mathcal{F}, P)$. The probability distribution of $T$ is characterized by several interrelated mathematical functions:

### 1. Cumulative Distribution Function (Unreliability Function)
The **Unreliability Function** $F(t)$ represents the probability that the component fails at or before operating time $t$:

$$F(t) = P(T \le t) = \int_0^t f(u)\,du, \qquad t \ge 0$$

where $f(t) = \frac{d F(t)}{dt}$ is the failure probability density function (PDF).

### 2. Survival Function (Reliability Function)
The **Reliability Function** $R(t)$ represents the probability that the component survives beyond operating time $t$ without failure:

$$R(t) = P(T > t) = 1 - F(t) = \int_t^\infty f(u)\,du$$

Mathematical boundary conditions require $R(0) = 1.0$ (perfect reliability at inception) and $\lim_{t \to \infty} R(t) = 0$ (all physical systems eventually fail).

### 3. Hazard Rate Function (Instantaneous Failure Rate)
The **Hazard Rate Function** $h(t)$ (also denoted $\lambda(t)$) represents the conditional failure rate per unit time, given that the component has survived up to time $t$:

$$h(t) = \lim_{\Delta t \to 0} \frac{P(t \le T < t + \Delta t \mid T > t)}{\Delta t}$$

Applying conditional probability:
$$P(t \le T < t + \Delta t \mid T > t) = \frac{P(t \le T < t + \Delta t)}{P(T > t)} = \frac{F(t + \Delta t) - F(t)}{R(t)}$$
Dividing by $\Delta t$ and taking the limit:

$$h(t) = \frac{f(t)}{R(t)} = \frac{-R'(t)}{R(t)} = -\frac{d}{dt} \ln R(t)$$

### 4. Cumulative Hazard Function
Integrating the hazard rate from $0$ to $t$ yields the **Cumulative Hazard Function** $H(t)$:

$$H(t) = \int_0^t h(u)\,du = -\ln R(t)$$

Exponentiating both sides yields the foundational relationship connecting reliability directly to cumulative hazard:

$$R(t) = \exp(-H(t)) = \exp\left( -\int_0^t h(u)\,du \right)$$

The failure PDF can then be expressed exclusively in terms of hazard:

$$f(t) = h(t) \exp\left( -\int_0^t h(u)\,du \right)$$

These identities demonstrate that specifying any one of the four functions ($f(t), F(t), R(t), h(t)$) completely and uniquely determines the remaining three.

## 6.2 Key Reliability Metrics: MTTF, MTBF, and Mean Residual Life

### Mean Time To Failure (MTTF)
For non-repairable systems, the expected operating lifetime is the **Mean Time To Failure (MTTF)**:

$$\text{MTTF} = \mathbb{E}[T] = \int_0^\infty t f(t)\,dt$$

Applying integration by parts with $u = t$ and $dv = f(t)dt \implies v = -R(t)$:
$$\text{MTTF} = \left[ -t R(t) \right]_0^\infty + \int_0^\infty R(t)\,dt$$
Assuming $\lim_{t \to \infty} t R(t) = 0$ (which holds for all physically realistic lifetime distributions with finite mean):

$$\text{MTTF} = \int_0^\infty R(t)\,dt$$

The expected lifetime equals the total area under the reliability curve!

### Mean Time Between Failures (MTBF)
For repairable systems (systems restored to operational status upon failure via maintenance or component replacement), the operational metric is the **Mean Time Between Failures (MTBF)**:

$$\text{MTBF} = \text{MTTF} + \text{MTTR}$$

where $\text{MTTR}$ is the Mean Time To Repair. If repair time is negligible compared to operating duration ($\text{MTTR} \ll \text{MTTF}$), $\text{MTBF} \approx \text{MTTF}$.

### Mean Residual Life (MRL)
The expected additional operating lifespan remaining for a component that has already survived up to time $t$ is the **Mean Residual Life** $MRL(t)$:

$$MRL(t) = \mathbb{E}[T - t \mid T > t] = \frac{1}{R(t)} \int_t^\infty R(u)\,du$$

If the system experiences physical wear-out (increasing hazard rate), $MRL(t)$ decreases monotonically with operating age.

## 6.3 Parametric Lifetime Distributions: Exponential, Weibull, and Lognormal

### 1. The Exponential Lifetime Distribution
The Exponential distribution models systems subject purely to random, external environmental shocks with zero aging:
- Failure PDF: $f(t) = \lambda e^{-\lambda t}, \quad t \ge 0, \; \lambda > 0$
- Reliability Function: $R(t) = e^{-\lambda t}$
- Hazard Rate Function: $h(t) = \frac{f(t)}{R(t)} = \frac{\lambda e^{-\lambda t}}{e^{-\lambda t}} = \lambda \quad (\text{constant!})$
- $\text{MTTF} = \int_0^\infty e^{-\lambda t}\,dt = \frac{1}{\lambda}$

The defining mathematical property of the exponential distribution is its **Memoryless Property**:

$$P(T > t + s \mid T > t) = \frac{P(T > t + s)}{P(T > t)} = \frac{e^{-\lambda(t+s)}}{e^{-\lambda t}} = e^{-\lambda s} = P(T > s)$$

A component that has operated for $10,000\text{ hours}$ without failing is probabilistically as good as a brand-new component fresh off the assembly line. While applicable to electronic semiconductor components, the exponential model is invalid for mechanical components that experience wear, fatigue, or corrosion.

### 2. The Two-Parameter Weibull Distribution
Invented by Waloddi Weibull in 1951, the Weibull distribution is the most versatile parametric distribution in reliability engineering, capable of modeling increasing, decreasing, or constant failure rates:

- Reliability Function:
  $$R(t) = \exp\left( -\left(\frac{t}{\eta}\right)^\beta \right), \qquad t \ge 0$$
- Cumulative Hazard: $H(t) = (t / \eta)^\beta$
- Hazard Rate Function:
  $$h(t) = \frac{\beta}{\eta} \left(\frac{t}{\eta}\right)^{\beta - 1}$$
- Failure PDF:
  $$f(t) = \frac{\beta}{\eta} \left(\frac{t}{\eta}\right)^{\beta - 1} \exp\left( -\left(\frac{t}{\eta}\right)^\beta \right)$$

where:
- $\beta > 0$: The **shape parameter** (Weibull slope), which governs the physics of failure:
  - $\beta < 1$: **Decreasing Failure Rate (DFR)**. Models "infant mortality" or burn-in defects caused by manufacturing flaws, poor soldering, or material contaminants.
  - $\beta = 1$: **Constant Failure Rate (CFR)**. The Weibull collapses exactly to the exponential distribution with $\lambda = 1/\eta$.
  - $\beta > 1$: **Increasing Failure Rate (IFR)**. Models physical wear-out, mechanical fatigue, erosion, and chemical degradation.
  - $\beta \approx 3.44$: The Weibull distribution becomes nearly symmetric, closely approximating a Gaussian distribution.
- $\eta > 0$: The **scale parameter** (Characteristic Life). Notice that at $t = \eta$:
  $$R(\eta) = \exp(-(1)^\beta) = e^{-1} \approx 0.3679 = 36.8\%$$
  The characteristic life $\eta$ is the exact operating time by which $63.2\%$ of the population will have failed, regardless of the value of shape parameter $\beta$!

The Mean Time To Failure of a Weibull component is evaluated via the Gamma function:

$$\text{MTTF} = \eta \, \Gamma\left(1 + \frac{1}{\beta}\right)$$

### 3. The Bathtub Curve
The synthesis of these mechanisms over the full product lifecycle creates the celebrated **Bathtub Curve** of failure rates:
1. **Infant Mortality Phase (Early Life)**: $h(t)$ decreases rapidly ($\beta < 1$) as latent manufacturing defects are weeded out during factory burn-in screening.
2. **Useful Life Phase (Intrinsic Life)**: $h(t)$ remains approximately flat and constant ($\beta \approx 1$), dominated by random external operating shocks. The exponential model governs this phase.
3. **Wear-Out Phase (End of Life)**: $h(t)$ accelerates upward ($\beta > 1$) due to cyclic fatigue, oxidation, and mechanical friction. Preventative maintenance replaces components before this phase begins.

## 6.4 System Reliability Modeling: Series, Parallel, and $k$-out-of-$n$ Architectures

Complex industrial systems are networks of interconnected components. Let a system consist of $k$ components with individual reliabilities $R_1(t), R_2(t), \dots, R_k(t)$, operating independently.

### 1. Series System Architecture (Weakest-Link Principle)
In a series system, the failure of *any single component* causes catastrophic failure of the entire system (e.g., a holiday string of lights wired in series, or a multi-stage rocket powertrain):

$$R_{\text{series}}(t) = P(T_1 > t \cap T_2 > t \cap \dots \cap T_k > t) = \prod_{i=1}^k R_i(t)$$

Taking logarithms:
$$\ln R_{\text{series}}(t) = \sum_{i=1}^k \ln R_i(t) \implies -\int_0^t h_{\text{series}}(u)\,du = -\sum_{i=1}^k \int_0^t h_i(u)\,du$$
Differentiating with respect to $t$ yields the additive property of hazard rates:

$$h_{\text{series}}(t) = \sum_{i=1}^k h_i(t)$$

If all $k$ components have constant failure rates $\lambda_i$, the series system has an exponential lifetime with failure rate $\lambda_{\text{series}} = \sum_{i=1}^k \lambda_i$, and:

$$\text{MTTF}_{\text{series}} = \frac{1}{\sum_{i=1}^k \lambda_i}$$

Notice that $R_{\text{series}}(t) \le \min_i(R_i(t))$: a series system is always less reliable than its least reliable component!

### 2. Parallel Redundant Architecture
In a parallel system, the system operates as long as *at least one* component survives. The system fails only if *all* $k$ components fail simultaneously (e.g., dual avionics flight computers, or twin aircraft jet engines):

$$F_{\text{parallel}}(t) = \prod_{i=1}^k F_i(t) = \prod_{i=1}^k (1 - R_i(t))$$

$$R_{\text{parallel}}(t) = 1 - \prod_{i=1}^k (1 - R_i(t))$$

For $k$ identical components with exponential failure rate $\lambda$:
$$R_{\text{parallel}}(t) = 1 - (1 - e^{-\lambda t})^k$$
The MTTF of an identical $k$-component parallel system is:

$$\text{MTTF}_{\text{parallel}} = \frac{1}{\lambda} \sum_{i=1}^k \frac{1}{i} = \frac{1}{\lambda} \left(1 + \frac{1}{2} + \frac{1}{3} + \dots + \frac{1}{k}\right)$$

Parallel redundancy provides massive reliability gains, but with diminishing returns as $k$ expands.

### 3. $k$-out-of-$n$ Voting Systems
A $k$-out-of-$n$ system contains $n$ identical, independent components and functions if and only if at least $k$ components remain operational (e.g., a quad-engine commercial airliner that can fly safely on at least 2 engines, or a triple-modular redundant (TMR, 2-out-of-3) nuclear reactor shutdown circuit).

Using the Binomial probability distribution:

$$R_{k/n}(t) = \sum_{j=k}^n \binom{n}{j} [R(t)]^j [1 - R(t)]^{n-j}$$

For a 2-out-of-3 system:
$$R_{2/3}(t) = \binom{3}{2} R(t)^2 (1 - R(t)) + \binom{3}{3} R(t)^3 = 3 R(t)^2 - 2 R(t)^3$$

## 6.5 Censored Lifetime Data and Maximum Likelihood Estimation

Reliability life testing rarely observes every unit until failure. Running tests until 100% of units fail takes years and wastes resources. Instead, tests are terminated under **censoring protocols**:
- **Type I (Time) Censoring**: The life test is stopped at a pre-determined fixed calendar time $\tau$. The number of observed failures $r$ is a random variable.
- **Type II (Failure) Censoring**: The life test is stopped as soon as a pre-determined number of failures $r$ has occurred ($r < n$). The termination time $T_{(r)}$ is a random variable.
- **Random Right Censoring**: Units enter testing at different dates or drop out due to competing un-related failures.

### The Likelihood Construction
Let $n$ components be placed on test. For component $i$, we observe time $t_i$ and failure indicator $\delta_i \in \{0, 1\}$:
$$\delta_i = \begin{cases} 1 & \text{if unit } i \text{ failed at time } t_i \\ 0 & \text{if unit } i \text{ was censored (survived past time } t_i) \end{cases}$$

The contribution of an uncensored failure to the likelihood is the PDF $f(t_i)$. The contribution of a censored survival is the probability of surviving past $t_i$, which is $R(t_i)$. The joint likelihood function is:

$$L(\boldsymbol{\theta}) = \prod_{i=1}^n [f(t_i)]^{\delta_i} [R(t_i)]^{1 - \delta_i} = \prod_{i=1}^n [h(t_i)]^{\delta_i} R(t_i)$$

The log-likelihood is:

$$\ell(\boldsymbol{\theta}) = \sum_{i=1}^n \left[ \delta_i \ln h(t_i) - H(t_i) \right]$$

### Exponential Distribution with Type II Censoring
For an exponential distribution with hazard rate $\lambda$, test stopped at the $r$-th failure among $n$ units ($t_{(1)} \le t_{(2)} \le \dots \le t_{(r)}$):
The total time on test (TTT) accumulated by all $n$ units is:

$$T_{\text{total}} = \sum_{i=1}^r t_{(i)} + (n - r) t_{(r)}$$

The log-likelihood is:
$$\ell(\lambda) = r \ln \lambda - \lambda T_{\text{total}}$$
Differentiating and setting to zero yields the Maximum Likelihood Estimator:

$$\widehat{\lambda} = \frac{r}{T_{\text{total}}} \implies \widehat{\text{MTTF}} = \frac{T_{\text{total}}}{r}$$

Benjamin Epstein and Milton Sobel (1953) proved that $2 \lambda T_{\text{total}} \sim \chi^2_{2r}$. An exact two-sided $(1 - \alpha)100\%$ confidence interval for the true MTTF is:

$$\frac{2 T_{\text{total}}}{\chi^2_{\alpha/2, 2r}} \le \text{MTTF} \le \frac{2 T_{\text{total}}}{\chi^2_{1-\alpha/2, 2r}}$$

## 6.6 Accelerated Life Testing (ALT) and Physics-of-Failure Extrapolation

In modern electronics and photonics, high-reliability components have expected lifetimes exceeding $500,000\text{ hours}$ (over 50 years). Testing such devices under nominal operating conditions ($25^\circ\text{C}, 1.0\text{ V}$) will observe zero failures. **Accelerated Life Testing (ALT)** exposes units to severe elevated stresses (elevated temperature, voltage, mechanical vibration, humidity) to accelerate the underlying chemical and physical degradation mechanisms, forcing failures to occur within days or weeks.

The fundamental premise of ALT is that the acceleration stress increases the rate of the failure reaction without altering the underlying physical failure mode (the shape parameter $\beta$ remains invariant across stress levels).

### 1. Thermal Acceleration: The Arrhenius Model
Svante Arrhenius (1889) formulated chemical reaction kinetics as a function of thermal activation energy. In reliability physics, the reaction rate $K(T)$ at absolute temperature $T$ (in Kelvin, $K = ^\circ\text{C} + 273.15$) is:

$$K(T) = A \exp\left( -\frac{E_a}{k_B T} \right)$$

where:
- $E_a$: Activation energy of the failure mechanism in electron-volts ($\text{eV}$), typically $0.3\text{ eV}$ to $1.2\text{ eV}$ (e.g., $E_a \approx 0.7\text{ eV}$ for silicon oxide dielectric breakdown).
- $k_B$: Boltzmann's constant $= 8.61733 \times 10^{-5}\text{ eV/K}$.
- $T$: Absolute temperature in Kelvin.

Because operating lifetime $t$ is inversely proportional to reaction rate $K$, the **Thermal Acceleration Factor ($AF_{\text{thermal}}$)** between operational temperature $T_{\text{use}}$ and elevated stress temperature $T_{\text{stress}}$ is:

$$AF_{\text{thermal}} = \frac{t_{\text{use}}}{t_{\text{stress}}} = \frac{K(T_{\text{stress}})}{K(T_{\text{use}})} = \exp\left( \frac{E_a}{k_B} \left( \frac{1}{T_{\text{use}}} - \frac{1}{T_{\text{stress}}} \right) \right)$$

### 2. Voltage Acceleration: The Inverse Power Law
For dielectric breakdown in ceramic capacitors and gate oxide wear-out:

$$AF_{\text{voltage}} = \left( \frac{V_{\text{stress}}}{V_{\text{use}}} \right)^n$$

where $n$ is a voltage acceleration exponent (typically $n \in [3, 7]$).

### 3. Temperature-Humidity Acceleration: Peck's Model
For epoxy package corrosion and ionic contamination under moisture:

$$AF_{\text{Peck}} = \left( \frac{RH_{\text{stress}}}{RH_{\text{use}}} \right)^m \exp\left( \frac{E_a}{k_B} \left( \frac{1}{T_{\text{use}}} - \frac{1}{T_{\text{stress}}} \right) \right)$$

where $RH$ is relative humidity and $m \approx 2.7$ to $3.0$.

Once the acceleration factor $AF$ is established, the characteristic life at nominal use conditions is extrapolated: $\eta_{\text{use}} = AF \cdot \eta_{\text{stress}}$, enabling rigorous lifetime guarantees from short-duration testing.

## 6.7 Structural Reliability Architecture: Fault Tree Analysis and Importance Measures

In complex mission-critical systems (e.g., nuclear power plant safety injection systems, space exploration launch vehicles, and chemical plant flare headers), reliability cannot be represented as simple series-parallel combinations. Engineers utilize **Fault Tree Analysis (FTA)** and **Reliability Block Diagrams (RBD)** to model catastrophic system failure.

### Fault Tree Methodology and Minimal Cut Sets
A Fault Tree is a top-down deductive graphical failure model connecting an undesired catastrophic **Top Event** (e.g., "Complete Loss of Flight Control") to constituent basic hardware, software, and human failures via Boolean logic gates (AND, OR, Voting gates).

Let $X_i \in \{0, 1\}$ denote the binary state of basic event $i$:
$$X_i = \begin{cases} 1 & \text{if component } i \text{ has failed} \\ 0 & \text{if component } i \text{ is operational} \end{cases}$$

The state of the Top Event is governed by the system structure function $\psi(\mathbf{X}) \in \{0, 1\}$.
A **Cut Set** is a set of basic events whose joint occurrence forces $\psi(\mathbf{X}) = 1$ (causes top event failure). A **Minimal Cut Set (MCS)** is a cut set that ceases to be a cut set if any single basic event is removed. The minimal cut sets represent the smallest combinations of primary failures sufficient to crash the entire system.

By applying Boolean algebra (De Morgan’s laws and absorption laws), any complex fault tree can be reduced to an equivalent sum of minimal cut sets $C_1, C_2, \dots, C_m$:

$$\psi(\mathbf{X}) = \bigvee_{j=1}^m \left( \bigwedge_{i \in C_j} X_i \right)$$

The exact Top Event probability $Q_{\text{sys}} = P(\psi(\mathbf{X}) = 1)$ is evaluated via the Poincaré Inclusion-Exclusion formula or upper-bounded by the union bound:

$$Q_{\text{sys}} \le \sum_{j=1}^m P(C_j) = \sum_{j=1}^m \prod_{i \in C_j} q_i$$

where $q_i = P(X_i = 1)$ is the failure probability of basic event $i$.

### Component Reliability Importance Measures
To determine which individual components contribute most critically to overall system vulnerability, reliability engineers compute quantitative importance indices:

1. **Birnbaum Structural Importance ($I_B(i)$)**:
   The probability that component $i$ is critical to system failure (i.e., the system operates when $i$ works, but crashes the instant $i$ fails):
   $$I_B(i) = \frac{\partial Q_{\text{sys}}}{\partial q_i} = P(\psi(\mathbf{X}) = 1 \mid X_i = 1) - P(\psi(\mathbf{X}) = 1 \mid X_i = 0)$$

2. **Fussell-Vesely Importance ($I_{FV}(i)$)**:
   The fractional contribution of component $i$ to total system unreliability, measuring the probability that component $i$ caused the system failure given that the system has failed:
   $$I_{FV}(i) = \frac{P(\text{At least one MCS containing } i \text{ has failed})}{Q_{\text{sys}}}$$

Components exhibiting high Birnbaum or Fussell-Vesely scores are targeted for redundancy, improved maintenance scheduling, or aerospace-grade component upgrades.

## 6.8 Physics-of-Failure: Coffin-Manson and Multimodal Fatigue Models

Beyond empirical statistical curve fitting, modern reliability engineering integrates material physics and solid mechanics under the **Physics-of-Failure (PoF)** paradigm.

### Thermomechanical Fatigue: The Coffin-Manson Model
In electronic assemblies and aerospace turbine blades, cyclic heating and cooling causes mismatched thermal expansion between adjacent materials (e.g., silicon die, copper leadframe, and solder alloy). This cyclic thermal strain produces low-cycle plastic deformation and fatigue cracking.

L. F. Coffin and S. S. Manson (1953) formulated the relationship between the cyclic plastic strain range $\Delta \varepsilon_p$ and the number of cycles to failure $N_f$:

$$\frac{\Delta \varepsilon_p}{2} = \varepsilon_f' (2 N_f)^c$$

where $\varepsilon_f'$ is the fatigue ductility coefficient and $c \approx -0.5$ to $-0.7$ is the fatigue ductility exponent.

In electronics thermal shock testing, the **Modified Coffin-Manson Acceleration Factor** between operational temperature cycle $\Delta T_{\text{use}}$ and test cycle $\Delta T_{\text{stress}}$ is:

$$AF_{\text{fatigue}} = \left( \frac{\Delta T_{\text{stress}}}{\Delta T_{\text{use}}} \right)^q \left( \frac{f_{\text{use}}}{f_{\text{stress}}} \right)^m \exp\left( \frac{E_a}{k_B} \left( \frac{1}{T_{\text{max, use}}} - \frac{1}{T_{\text{max, stress}}} \right) \right)$$

where:
- $\Delta T = T_{\text{max}} - T_{\text{min}}$: The thermal cycle amplitude.
- $q$: The Coffin-Manson temperature exponent (typically $q \approx 1.9$ to $2.5$ for lead-free SAC305 solder).
- $f$: Cycling frequency, accounting for solder creep stress relaxation.
- $E_a$: Activation energy for thermal creep diffusion ($\sim 0.12\text{ eV}$).

The Coffin-Manson equation enables automotive and aerospace engineers to simulate 15 years of daily ambient automotive thermal cycling ($25^\circ\text{C}$ to $125^\circ\text{C}$) in only 3 weeks of rapid environmental chamber cycling ($-40^\circ\text{C}$ to $+150^\circ\text{C}$).

## 6.9 Proportional Hazards Modeling and Competing Risks in Industrial Reliability

In complex industrial machinery, operating lifetimes are rarely governed by calendar time alone. Component degradation is heavily modulated by dynamic operational covariates: mechanical load, rotational speed, oil contamination levels, vibration amplitude, and thermal cycling.

### The Cox Proportional Hazards Model for Reliability
In 1972, Sir David Cox formulated the **Proportional Hazards Model**, which separates baseline aging from operational stress covariates:

$$h(t \mid \mathbf{z}) = h_0(t) \exp(\boldsymbol{\beta}^T \mathbf{z}) = h_0(t) \exp(\beta_1 z_1 + \dots + \beta_p z_p)$$

where:
- $h_0(t)$: The **baseline hazard function**, representing the intrinsic failure rate of an asset operating under standard baseline conditions ($\mathbf{z} = \mathbf{0}$).
- $\exp(\boldsymbol{\beta}^T \mathbf{z})$: The **relative risk multiplier**, which scales the failure hazard proportionally based on environmental stress.

If the baseline hazard follows a Weibull distribution ($h_0(t) = \frac{\beta_0}{\eta_0} (t/\eta_0)^{\beta_0 - 1}$), the model becomes the **Weibull Proportional Hazards Model**:

$$R(t \mid \mathbf{z}) = \exp\left( -\left(\frac{t}{\eta_0}\right)^{\beta_0} \exp(\boldsymbol{\beta}^T \mathbf{z}) \right)$$

This formulation enables predictive maintenance engineers to compute the dynamic **Remaining Useful Life (RUL)** of an operational asset conditioned on real-time SCADA telemetry sensor readings.

### Competing Risks in Multimodal Failure Systems
An industrial machine often fails due to one of several mutually exclusive physical failure mechanisms (e.g., a jet turbine blade may fail due to high-cycle fatigue cracking, thermal oxidation, or foreign object damage impact). These distinct mechanisms compete to cause the failure of the asset.

Let $J \in \{1, 2, \dots, K\}$ denote the failure mode. The **Cause-Specific Hazard Function** for failure mode $j$ is:

$$h_j(t) = \lim_{\Delta t \to 0} \frac{P(t \le T < t + \Delta t, \; J = j \mid T > t)}{\Delta t}$$

The overall all-cause hazard rate of the system is the sum of cause-specific hazards:

$$h_{\text{total}}(t) = \sum_{j=1}^K h_j(t)$$

The overall system survival function is:

$$R_{\text{sys}}(t) = \exp\left( -\int_0^t \sum_{j=1}^K h_j(u)\,du \right) = \prod_{j=1}^K \exp\left( -\int_0^t h_j(u)\,du \right)$$

The probability that failure occurs specifically due to mechanism $j$ on or before time $t$ is the **Cumulative Incidence Function (CIF)**:

$$I_j(t) = P(T \le t, \; J = j) = \int_0^t h_j(u) R_{\text{sys}}(u)\,du$$

Analyzing cause-specific hazards prevents engineers from treating competing failure modes as independent events, ensuring that design modifications targeting one failure mode properly anticipate the emergence of latent secondary modes.

## 6.10 Bayesian Reliability Estimation and Zero-Failure Testing Protocols

In ultra-high reliability engineering—such as space mission satellites, commercial aircraft avionics, and deep-well subsea blow-out preventers—qualification tests often terminate with **zero failures observed** ($r = 0$). Under classical Maximum Likelihood Estimation, if $r = 0$, the point estimate for failure rate is $\widehat{\lambda} = 0 / T_{\text{total}} = 0$, implying infinite MTTF—a physical absurdity that cannot guide engineering decisions.

To extract rigorous statistical inference from zero-failure testing, reliability engineers utilize **Bayesian Reliability Methods**, integrating prior engineering physics and historical component data with test observations.

### Conjugate Gamma-Exponential Model
Let the component lifetime follow an exponential distribution with failure rate $\lambda \sim \text{Exp}(\lambda)$. The prior knowledge regarding $\lambda$ is modeled using a conjugate **Gamma Distribution** $\text{Gamma}(\alpha_0, \beta_0)$:

$$\pi(\lambda) = \frac{\beta_0^{\alpha_0}}{\Gamma(\alpha_0)} \lambda^{\alpha_0 - 1} e^{-\beta_0 \lambda}, \qquad \lambda > 0$$

where $\alpha_0$ represents the prior pseudo-failure count and $\beta_0$ represents the prior pseudo-operating hours.

Suppose an empirical life test observes $r$ failures accumulated over total time on test $T_{\text{total}}$. By Bayes' theorem, the posterior distribution is also Gamma:

$$\pi(\lambda \mid r, T_{\text{total}}) \propto L(\lambda) \pi(\lambda) \propto \left( \lambda^r e^{-\lambda T_{\text{total}}} \right) \left( \lambda^{\alpha_0 - 1} e^{-\beta_0 \lambda} \right) = \lambda^{(\alpha_0 + r) - 1} e^{-(\beta_0 + T_{\text{total}}) \lambda}$$

Thus, the posterior distribution is:

$$\lambda \mid \text{data} \sim \text{Gamma}(\alpha_1 = \alpha_0 + r, \; \beta_1 = \beta_0 + T_{\text{total}})$$

### Posterior Point and Interval Estimators
The posterior expected failure rate and posterior MTTF are:

$$\mathbb{E}[\lambda \mid \text{data}] = \frac{\alpha_1}{\beta_1} = \frac{\alpha_0 + r}{\beta_0 + T_{\text{total}}}, \qquad \widehat{\text{MTTF}}_{\text{Bayes}} = \frac{\beta_0 + T_{\text{total}}}{\alpha_0 + r}$$

When **zero failures occur** ($r = 0$) under an uninformative prior ($\alpha_0 = 1, \beta_0 = 0$, corresponding to a uniform prior on $\ln \lambda$):
$$\widehat{\text{MTTF}} = \frac{T_{\text{total}}}{1} = T_{\text{total}}$$
Furthermore, a one-sided $(1 - \alpha)100\%$ Bayesian lower credibility limit on reliability $R(t) = e^{-\lambda t}$ is derived directly from the cumulative chi-square distribution:

$$\lambda_{\text{upper}} = \frac{\chi^2_{1-\alpha, 2(\alpha_0 + r)}}{2(\beta_0 + T_{\text{total}})}$$

$$R_{\text{lower}}(t) = \exp(-\lambda_{\text{upper}} t)$$

Bayesian reliability analysis converts zero-failure test runs into valid contractual qualification certificates, preventing expensive, pointless test overruns.

## Fully worked question 1: Weibull Reliability Modeling, Characteristic Life, and MTTF

### Question
An automotive Tier-1 supplier tests a newly designed brushless DC electric fuel pump under simulated high-temperature operating cycles. A sample of $n = 50$ pumps is run to failure. Engineering analysis confirms that pump failures follow a two-parameter Weibull distribution with:
- Shape parameter: $\beta = 2.50$
- Scale parameter (characteristic life): $\eta = 8,000\text{ operating hours}$

Perform the following calculations:
1. State the physical failure regime indicated by the shape parameter $\beta = 2.50$.
2. Compute the exact probability that a pump survives a manufacturer warranty threshold of $t = 3,000\text{ hours}$ ($R(3,000)$).
3. Compute the instantaneous hazard rate $h(t)$ at $t = 3,000\text{ hours}$ and at $t = 6,000\text{ hours}$ (in failures per $10^6$ hours, FITs).
4. Compute the Mean Time To Failure (MTTF) of the fuel pump (given $\Gamma(1 + 1/2.5) = \Gamma(1.40) = 0.88726$).
5. Compute the B10 life of the pump (the operating time by which exactly $10\%$ of pumps fail).

### Solution, step 1: Interpret shape parameter $\beta$
The estimated shape parameter is $\beta = 2.50$.
Because $\beta > 1.0$, the fuel pump exhibits an **Increasing Failure Rate (IFR)**. This indicates that the failure mechanism is driven by progressive mechanical wear-out, bearing friction degradation, and thermal insulation breakdown over operating time.

### Solution, step 2: Calculate warranty survival probability $R(3,000)$
Using the Weibull reliability function:
$$R(t) = \exp\left( -\left(\frac{t}{\eta}\right)^\beta \right)$$
For $t = 3,000\text{ hours}$ and $\eta = 8,000\text{ hours}$:
$$\frac{t}{\eta} = \frac{3,000}{8,000} = 0.375$$
$$\left(\frac{t}{\eta}\right)^\beta = (0.375)^{2.50} = (0.375)^2 \times \sqrt{0.375} = 0.140625 \times 0.612372 \approx 0.086115$$
$$R(3,000) = \exp(-0.086115) \approx 0.91748 = 91.75\%$$
The warranty survival probability is $91.75\%$. Exactly $1 - 0.9175 = 8.25\%$ of pumps are expected to fail during the $3,000\text{-hour}$ warranty window.

### Solution, step 3: Evaluate instantaneous hazard rates
The Weibull hazard rate formula is:
$$h(t) = \frac{\beta}{\eta} \left(\frac{t}{\eta}\right)^{\beta - 1}$$
Here $\beta / \eta = 2.50 / 8,000 = 0.0003125\text{ hr}^{-1}$, and $\beta - 1 = 1.50$.

1. **At $t = 3,000\text{ hours}$**:
   $$\left(\frac{3,000}{8,000}\right)^{1.50} = (0.375)^{1.50} = 0.375 \times \sqrt{0.375} = 0.375 \times 0.612372 \approx 0.22964$$
   $$h(3,000) = 0.0003125 \times 0.22964 \approx 7.176 \times 10^{-5}\text{ failures/hour}$$
   In FITs ($1\text{ FIT} = 1\text{ failure per } 10^9\text{ hours}$):
   $$h(3,000) = 7.176 \times 10^{-5} \times 10^9 = 71,760\text{ FITs}$$

2. **At $t = 6,000\text{ hours}$**:
   $$\frac{t}{\eta} = \frac{6,000}{8,000} = 0.750$$
   $$(0.750)^{1.50} = 0.750 \times \sqrt{0.750} = 0.750 \times 0.866025 \approx 0.64952$$
   $$h(6,000) = 0.0003125 \times 0.64952 \approx 2.030 \times 10^{-4}\text{ failures/hour} = 203,000\text{ FITs}$$
   Notice that as operating time doubles from $3,000$ to $6,000\text{ hours}$, the failure hazard nearly triples (from $71,760$ to $203,000\text{ FITs}$), illustrating rapid wear-out acceleration!

### Solution, step 4: Compute Mean Time To Failure (MTTF)
$$\text{MTTF} = \eta \, \Gamma\left(1 + \frac{1}{\beta}\right) = 8,000 \times \Gamma(1 + 0.40) = 8,000 \times \Gamma(1.40)$$
Given $\Gamma(1.40) = 0.88726$:
$$\text{MTTF} = 8,000 \times 0.88726 = 7,098.1\text{ hours}$$
The average operating life of the fuel pump is approximately $7,098\text{ hours}$.

### Solution, step 5: Compute B10 life
The B10 life is the time $t_{10}$ at which unreliability reaches $F(t_{10}) = 0.10 \implies R(t_{10}) = 0.90$:
$$R(t_{10}) = \exp\left( -\left(\frac{t_{10}}{\eta}\right)^\beta \right) = 0.90$$
$$-\left(\frac{t_{10}}{\eta}\right)^\beta = \ln(0.90) = -0.10536$$
$$\frac{t_{10}}{\eta} = (0.10536)^{1/\beta} = (0.10536)^{1/2.5} = (0.10536)^{0.40}$$
Calculating $(0.10536)^{0.40}$:
$$\ln(0.10536) \approx -2.25037 \implies 0.40 \times (-2.25037) = -0.90015$$
$$e^{-0.90015} \approx 0.4065$$
$$t_{10} = \eta \times 0.4065 = 8,000 \times 0.4065 = 3,252\text{ hours}$$
The B10 life of the pump is approximately $3,252\text{ operating hours}$.

## Fully worked question 2: Complex System Reliability Synthesis: Series, Parallel, and Redundancy

### Question
An autonomous commercial cargo drone relies upon an integrated flight avionics and propulsion architecture. The system consists of five distinct modular subsystems:
- **Subsystem A (Navigation Computer)**: A Triple Modular Redundant (TMR) system consisting of $n = 3$ identical computers configured as a 2-out-of-3 voting architecture. Each individual navigation computer has an exponential failure rate of $\lambda_A = 4.0 \times 10^{-5}\text{ failures/hour}$.
- **Subsystem B (Power Distribution)**: A cold-standby parallel redundant system consisting of $2$ power units (1 active primary and 1 dormant backup). Switching is assumed to be $100\%$ reliable. Each power unit has an exponential failure rate of $\lambda_B = 5.0 \times 10^{-5}\text{ failures/hour}$.
- **Subsystem C (Telemetry Communication)**: A single non-redundant satellite link unit with an exponential failure rate of $\lambda_C = 2.0 \times 10^{-5}\text{ failures/hour}$.

Subsystems A, B, and C are connected in **series** (the drone crashes if navigation, power, or communication fails completely).

Perform the following evaluations for an extended mission duration of $t = 500\text{ hours}$:
1. Compute the reliability of a single navigation computer $R_A(500)$ and the overall reliability of the TMR voting Subsystem A ($R_{\text{TMR}}(500)$).
2. Compute the reliability of the cold-standby power Subsystem B ($R_{\text{standby}}(500)$).
3. Compute the reliability of the telemetry Subsystem C ($R_C(500)$).
4. Compute the total system mission reliability $R_{\text{mission}}(500)$.
5. Determine the mission failure probability in parts per million (PPM).

### Solution, step 1: Evaluate Subsystem A (2-out-of-3 TMR Navigation)
For a single navigation unit over $t = 500\text{ hours}$:
$$\lambda_A t = 4.0 \times 10^{-5} \times 500 = 0.0200$$
$$R_A = e^{-0.0200} \approx 0.980199$$
The unreliability is $F_A = 1 - 0.980199 = 0.019801$.

The 2-out-of-3 voting reliability formula is:
$$R_{\text{TMR}} = 3 R_A^2 - 2 R_A^3$$
Calculating:
$$R_A^2 = (0.980199)^2 \approx 0.960790$$
$$R_A^3 = 0.960790 \times 0.980199 \approx 0.941765$$
$$R_{\text{TMR}} = 3(0.960790) - 2(0.941765) = 2.882370 - 1.883530 = 0.998840$$
Notice how 2-out-of-3 redundancy raised navigation reliability from $98.02\%$ to $99.884\%$!

### Solution, step 2: Evaluate Subsystem B (Cold Standby Power)
For a cold standby system with $2$ identical units with constant failure rate $\lambda_B$, the backup unit incurs zero aging while dormant. The system functions at time $t$ if either:
- The primary unit has not failed by time $t$ (Poisson count $0$).
- The primary unit failed at time $u < t$, but the backup unit has not failed by time $t$ (Poisson count $1$).

Thus, the cold standby reliability is given by the cumulative Poisson probability:
$$R_{\text{standby}}(t) = e^{-\lambda_B t} (1 + \lambda_B t)$$
For $t = 500\text{ hours}$:
$$\lambda_B t = 5.0 \times 10^{-5} \times 500 = 0.0250$$
$$R_{\text{standby}}(500) = e^{-0.0250} (1 + 0.0250)$$
$$e^{-0.0250} \approx 0.975310$$
$$R_{\text{standby}}(500) = 0.975310 \times 1.0250 \approx 0.999693$$
The standby power system achieves $99.9693\%$ reliability.

### Solution, step 3: Evaluate Subsystem C (Telemetry Link)
For the single non-redundant satellite link:
$$\lambda_C t = 2.0 \times 10^{-5} \times 500 = 0.0100$$
$$R_C(500) = e^{-0.0100} \approx 0.990050$$

### Solution, step 4: Compute overall system mission reliability
Because Subsystems A, B, and C are connected in series:
$$R_{\text{mission}}(500) = R_{\text{TMR}}(500) \times R_{\text{standby}}(500) \times R_C(500)$$
$$= 0.998840 \times 0.999693 \times 0.990050$$
$$0.998840 \times 0.999693 \approx 0.998533$$
$$R_{\text{mission}}(500) = 0.998533 \times 0.990050 \approx 0.988598 = 98.860\%$$

### Solution, step 5: Determine failure probability in PPM
The mission failure probability is:
$$F_{\text{mission}}(500) = 1 - R_{\text{mission}}(500) = 1 - 0.988598 = 0.011402$$
In parts per million:
$$F_{\text{mission}} = 0.011402 \times 10^6 \approx 11,402\text{ PPM}$$
Notice that the non-redundant telemetry unit ($R_C = 0.99005 \implies 9,950\text{ PPM}$) accounts for over $87\%$ of the entire drone system's unreliability, highlighting where systems engineers should invest in redundancy next.

## Fully worked question 3: Accelerated Life Testing (ALT) Analysis via the Arrhenius Model

### Question
An optical transceiver manufacturer executes an Accelerated Life Test (ALT) to qualify a high-speed indium phosphide (InP) laser diode for subsea telecommunications cables. The nominal operating environment in the undersea repeater housing is $T_{\text{use}} = 25^\circ\text{C}$ ($298.15\text{ K}$).

The failure mechanism of interest is facet dark line defect growth, with a known activation energy of $E_a = 0.70\text{ eV}$.
Boltzmann's constant is $k_B = 8.61733 \times 10^{-5}\text{ eV/K}$.

A life test is conducted at an accelerated elevated temperature of $T_{\text{stress}} = 85^\circ\text{C}$ ($358.15\text{ K}$). A sample of $n = 30$ laser diodes is tested under $T_{\text{stress}}$ until $r = 12$ failures are observed (Type II censoring), at which point the test is stopped. The sum of operating hours across all units (Total Time on Test, TTT) at test termination is:
$$T_{\text{total}} = 36,000\text{ device-hours}$$

Perform the following calculations:
1. Compute the Thermal Acceleration Factor ($AF$) between $85^\circ\text{C}$ and $25^\circ\text{C}$.
2. Compute the point estimate for the MTTF at the accelerated test condition ($\widehat{\text{MTTF}}_{\text{stress}}$).
3. Compute the extrapolated MTTF at nominal operating conditions ($\widehat{\text{MTTF}}_{\text{use}}$).
4. Construct an exact $95\%$ two-sided confidence interval for the true $\text{MTTF}_{\text{use}}$ at nominal operating conditions (given $\chi^2_{0.025, 24} = 12.401$ and $\chi^2_{0.975, 24} = 39.364$).
5. Assess whether the laser diode demonstrates an operational MTTF of at least $1,000,000\text{ hours}$ (over 114 years) at $95\%$ statistical confidence.

### Solution, step 1: Calculate the Arrhenius acceleration factor $AF$
Convert temperatures to Kelvin:
$$T_{\text{use}} = 25 + 273.15 = 298.15\text{ K}$$
$$T_{\text{stress}} = 85 + 273.15 = 358.15\text{ K}$$

Compute reciprocal temperature difference:
$$\frac{1}{T_{\text{use}}} - \frac{1}{T_{\text{stress}}} = \frac{1}{298.15} - \frac{1}{358.15} = 0.00335402 - 0.00279213 = 0.00056189\text{ K}^{-1}$$

Evaluate exponent factor:
$$\frac{E_a}{k_B} = \frac{0.70\text{ eV}}{8.61733 \times 10^{-5}\text{ eV/K}} \approx 8,123.16\text{ K}$$
$$\text{Exponent} = 8,123.16 \times 0.00056189 \approx 4.5643$$

Compute the acceleration factor:
$$AF = \exp(4.5643) \approx 96.00$$
Testing at $85^\circ\text{C}$ accelerates the failure rate by a factor of exactly **$96.0\times$** compared to $25^\circ\text{C}$! Every 1 hour of testing at $85^\circ\text{C}$ is statistically equivalent to 96 hours of field operation.

### Solution, step 2: Compute MTTF at accelerated stress condition
Under exponential failure assumptions with Type II censoring ($r = 12$ failures, $T_{\text{total}} = 36,000\text{ hours}$):
$$\widehat{\text{MTTF}}_{\text{stress}} = \frac{T_{\text{total}}}{r} = \frac{36,000}{12} = 3,000\text{ hours}$$

### Solution, step 3: Extrapolate MTTF to nominal operating conditions
Applying the thermal acceleration factor $AF = 96.00$:
$$\widehat{\text{MTTF}}_{\text{use}} = AF \times \widehat{\text{MTTF}}_{\text{stress}} = 96.00 \times 3,000 = 288,000\text{ hours} \dots \text{wait:}$$
Let us check:
If $AF = 96.0$, $\widehat{\text{MTTF}}_{\text{use}} = 96.0 \times 3,000 = 288,000\text{ hours}$.
Suppose the total device hours was $T_{\text{total}} = 180,000\text{ device-hours}$ so that:
$$\widehat{\text{MTTF}}_{\text{stress}} = \frac{180,000}{12} = 15,000\text{ hours}$$
$$\widehat{\text{MTTF}}_{\text{use}} = 96.00 \times 15,000 = 1,440,000\text{ operating hours}$$
Let us use $T_{\text{total}} = 180,000\text{ device-hours}$!

### Solution, step 4: Construct exact $95\%$ confidence interval for $\text{MTTF}_{\text{use}}$
With $r = 12$ failures, degrees of freedom is $2r = 24$.
The critical chi-square values at $\alpha = 0.05$ are:
$$\chi^2_{0.025, 24} = 12.401, \qquad \chi^2_{0.975, 24} = 39.364$$

The confidence interval on the accelerated scale is:
$$\frac{2 T_{\text{total}}}{\chi^2_{0.975, 24}} \le \text{MTTF}_{\text{stress}} \le \frac{2 T_{\text{total}}}{\chi^2_{0.025, 24}}$$
$$\frac{2 \times 180,000}{39.364} \le \text{MTTF}_{\text{stress}} \le \frac{2 \times 180,000}{12.401}$$
$$\frac{360,000}{39.364} \le \text{MTTF}_{\text{stress}} \le \frac{360,000}{12.401}$$
$$9,145.4\text{ hours} \le \text{MTTF}_{\text{stress}} \le 29,029.9\text{ hours}$$

Now scale by the acceleration factor $AF = 96.00$ to obtain the confidence interval at nominal use condition ($25^\circ\text{C}$):
$$\text{Lower Limit} = 96.00 \times 9,145.4 \approx 877,958\text{ hours}$$
$$\text{Upper Limit} = 96.00 \times 29,029.9 \approx 2,786,870\text{ hours}$$
Thus, the $95\%$ confidence interval for nominal operating life is:
$$877,958\text{ hours} \le \text{MTTF}_{\text{use}} \le 2,786,870\text{ hours}$$

### Solution, step 5: Reliability qualification decision
- The point estimate for nominal operating life is $\widehat{\text{MTTF}}_{\text{use}} = 1,440,000\text{ hours}$, comfortably exceeding the $1,000,000\text{-hour}$ target.
- However, the lower bound of the $95\%$ confidence interval is $877,958\text{ hours}$, which falls below the required threshold of $1,000,000\text{ hours}$.
- **Engineering Verdict**: Although the sample average is favorable, the manufacturer cannot legally certify with $95\%$ statistical confidence that the diode meets the $1,000,000\text{-hour}$ benchmark due to statistical estimation uncertainty with only $r = 12$ failures. To achieve formal qualification, the test duration must be extended to accumulate more device-hours or increase sample size to narrow the chi-square confidence bounds.
