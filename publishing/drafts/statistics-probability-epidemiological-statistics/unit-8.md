# Unit 8: Survival Analysis in Epidemiology & Causal Inference Frameworks

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

When the proportional hazards assumption is violated, several analytical remedies exist in contemporary survival epidemiology:

1. **Stratified Cox Models**: If a categorical covariate violates proportional hazards, one can stratify on that variable. In a stratified Cox model, the baseline hazard function is allowed to vary arbitrarily across strata $s \in \{1, \dots, S\}$, while the regression coefficients $\boldsymbol{\beta}$ for the other covariates remain common across all strata:
$$h_s(t \mid \mathbf{x}_i) = h_{0s}(t) \exp(\mathbf{x}_i^T \boldsymbol{\beta})$$
The total partial log-likelihood is simply the sum of the stratum-specific partial log-likelihoods $\ell(\boldsymbol{\beta}) = \sum_{s=1}^S \ell_s(\boldsymbol{\beta})$. This strategy completely eliminates confounding or non-proportionality by the stratifying factor without requiring any parametric modeling of its time-dependent dynamics.

2. **Time-Varying Coefficients and Step Functions**: If an exposure of primary interest exhibits non-proportional hazards, one can model the regression coefficient as an explicit function of time $\beta(t) = \beta + \theta g(t)$, where common choices for $g(t)$ include $\ln(t)$, $t$, or piecewise step functions over clinically meaningful follow-up intervals ($0-1$ year, $1-5$ years, and $>5$ years). Testing whether $\theta = 0$ provides a direct likelihood-ratio or Wald test of proportionality.

3. **Restricted Mean Survival Time (RMST)**: When proportional hazards fails entirely (for instance, when survival curves cross due to early surgical mortality followed by late oncologic curative cure), the hazard ratio becomes an unstable, follow-up-dependent summary. In such settings, the difference in Restricted Mean Survival Time up to a fixed milestone $\tau$, defined as $\Delta \text{RMST}(\tau) = \int_0^{\tau} S_1(t)\,dt - \int_0^{\tau} S_0(t)\,dt$, provides an unconfounded, model-free metric of absolute life expectancy gained.

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

## 8.7 Accelerated Failure Time (AFT) Models & Competing Risks Subdistribution Hazards

While the Cox proportional hazards model is the most widely applied survival model in medical literature, two critical alternative frameworks are essential for comprehensive epidemiological mastery:

### Accelerated Failure Time (AFT) Models
Under the **Accelerated Failure Time (AFT)** formulation, the effect of an exposure is modeled not as a multiplicative hazard shift, but as a direct acceleration or deceleration of the biological survival time clock:

$$\ln(T_i) = \mathbf{x}_i^T \boldsymbol{\beta} + \sigma \varepsilon_i$$

where $\varepsilon_i$ is a random error disturbance with a pre-specified distribution (e.g., standard extreme value yielding the Weibull AFT, logistic yielding log-logistic AFT, or Gaussian yielding log-normal AFT). The exponentiated coefficient $\exp(\beta_1)$ represents the **Acceleration Factor** ($\gamma$):
$$T(X = 1) \stackrel{d}{=} \gamma \cdot T(X = 0)$$
- If $\gamma > 1.0$: The exposure prolongs time-to-event (decelerates aging/progression); the median survival time is multiplied by $\gamma$.
- If $\gamma < 1.0$: The exposure accelerates time-to-failure.
Unlike hazard ratios, acceleration factors are easily communicated to non-statistical clinical audiences as percentage changes in survival time.

### Competing Risks and Fine-Gray Subdistribution Hazards
In aging populations, individuals are simultaneously at risk of multiple mutually exclusive terminating events (e.g., death from cardiovascular disease, death from prostate cancer, or fatal motor vehicle trauma). Treating competing deaths as simple independent censoring violates non-informative censoring, producing severe upward bias in the cumulative incidence of the primary event.

Robert Gray (1988) and Jason Fine and Robert Gray (1999) resolved this by modeling the **Cumulative Incidence Function** ($CIF_k(t) = P(T \le t, \text{Cause} = k)$) directly through the **Subdistribution Hazard**:

$$\bar{h}_k(t) = \lim_{\Delta t \to 0} \frac{P(t \le T < t + \Delta t, \text{Cause} = k \mid T \ge t \text{ or } (T < t \text{ and } \text{Cause} \neq k))}{\Delta t}$$

In the Fine-Gray subdistribution risk set, an individual who dies from a competing cause (e.g., heart disease at month 12) remains in the denominator risk set indefinitely for the cancer outcome, preventing the false inflation of cancer cumulative incidence. Fitting proportional subdistribution hazards regression models ensures mathematically sound risk prediction in the presence of competing terminal events.

## 8.8 The Next Generation Matrix Formulation of the Basic Reproduction Number ($\mathcal{R}_0$)

In Section 8.4, we evaluated the Basic Reproduction Number $\mathcal{R}_0 = \beta / \gamma$ for the simple classical three-compartment SIR model. However, real infectious disease pathogens involve complex multi-compartment transmission pathways—such as latent incubation states ($E$ in SEIR models), asymptomatic transmission compartments ($A$), hospitalized isolation states ($H$), and cross-species vector compartments (mosquitoes in dengue and malaria).

For high-dimensional, heterogeneous compartmental transmission models, calculating $\mathcal{R}_0$ via scalar algebraic manipulation is prone to severe errors. In 1990, Odo Diekmann, Hans Heesterbeek, and Johan Metz introduced the rigorous mathematical standard: **The Next Generation Matrix (NGM)**.

### 1. Classification of Compartments and the Disease-Free Equilibrium
Let the continuous population be divided into $n$ distinct epidemiological compartments $\mathbf{x} = [x_1, x_2, \dots, x_n]^T$.
Sort the compartments such that the first $m$ compartments ($x_1, \dots, x_m$) are **infected compartments** (individuals currently harboring pathogen), while the remaining $n - m$ compartments are uninfected (e.g., susceptible $S$, recovered $R$).

The disease system evolves according to the coupled ordinary differential equations:
$$\frac{dx_i}{dt} = \mathcal{F}_i(\mathbf{x}) - \mathcal{V}_i(\mathbf{x}) \quad \text{for } i = 1, \dots, n$$
where:
- $\mathcal{F}_i(\mathbf{x})$: The rate of appearance of **new infections** into compartment $i$.
- $\mathcal{V}_i(\mathbf{x}) = \mathcal{V}_i^-(\mathbf{x}) - \mathcal{V}_i^+(\mathbf{x})$: The net rate of transfer of individuals out of compartment $i$ via all other biological transitions (recovery, progression to subsequent disease stages, natural mortality, and disease-induced mortality).

Let $\mathbf{x}_0 = [0, \dots, 0, x_{m+1}^*, \dots, x_n^*]^T$ denote the **Disease-Free Equilibrium (DFE)**, where all infected states are identically zero.

### 2. Jacobian Linearization and the Next Generation Operator
Linearizing the infected subsystem about the disease-free equilibrium $\mathbf{x}_0$ yields two $m \times m$ Jacobian matrices:
$$\mathbf{F} = \left[ \frac{\partial \mathcal{F}_i(\mathbf{x}_0)}{\partial x_j} \right]_{1 \le i, j \le m}, \quad \mathbf{V} = \left[ \frac{\partial \mathcal{V}_i(\mathbf{x}_0)}{\partial x_j} \right]_{1 \le i, j \le m}$$

The matrices admit transparent biological interpretations:
- Element $F_{ij}$ represents the rate at which an infected individual in compartment $j$ generates new infections entering compartment $i$.
- Element $(V^{-1})_{jk}$ represents the average expected duration of time that an individual who initially enters infected compartment $k$ will spend residing in infected compartment $j$ throughout their entire infective lifespan.

The product matrix is the **Next Generation Matrix**:

$$\mathbf{K} = \mathbf{F} \mathbf{V}^{-1}$$

Element $K_{ik} = (\mathbf{F} \mathbf{V}^{-1})_{ik}$ represents the expected total number of secondary infections in compartment $i$ generated throughout the entire infectious lifetime of a single primary infected individual originally introduced into compartment $k$.

### 3. Theorem on $\mathcal{R}_0$ and Epidemic Stability
Diekmann and Heesterbeek proved the foundational stability theorem:
*Theorem*: The Basic Reproduction Number $\mathcal{R}_0$ is exactly the **Spectral Radius** (dominant eigenvalue in absolute value) of the Next Generation Matrix:

$$\mathcal{R}_0 = \rho(\mathbf{K}) = \rho(\mathbf{F} \mathbf{V}^{-1})$$

Furthermore:
- If $\mathcal{R}_0 < 1$, the disease-free equilibrium $\mathbf{x}_0$ is locally asymptotically stable: any small viral introduction decays exponentially to extinction.
- If $\mathcal{R}_0 > 1$, the disease-free equilibrium is unstable, guaranteeing that a pathogen introduction triggers an exponential epidemic wave.

By converting complex multi-stage differential systems into eigenvalue problems, the Next Generation Matrix provides mathematical epidemiologists with an analytical tool for evaluating vaccine coverage thresholds, quarantine protocols, and vector control programs.

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
