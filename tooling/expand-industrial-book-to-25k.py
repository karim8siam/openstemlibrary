#!/usr/bin/env python3
"""
Expand Industrial and Official Statistics units to comfortably exceed 25,000 substantive prose words.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-industrial-and-official-statistics"

# Unit 2 expansion: Johnson translation system for non-normal capability
u2_path = DRAFT_DIR / "unit-2.md"
u2_text = u2_path.read_text(encoding="utf-8")
u2_add = r"""
## 2.11 The Johnson Translation System for Non-Normal Capability Estimation

When manufacturing data exhibit severe departures from Gaussian symmetry (such as non-negative dimensions with physical zero boundaries, surface roughness, or cycle times), transforming data via Norman L. Johnson's (1949) translation system provides a mathematically rigorous alternative to empirical percentiles.

The Johnson system maps an arbitrary continuous random variable $X$ to a standard normal variate $Z \sim \mathcal{N}(0, 1)$ through a monotonic transformation:

$$Z = \gamma + \eta \cdot g\left(\frac{X - \xi}{\lambda}\right)$$

where $\gamma$ and $\eta > 0$ are shape parameters, $\xi$ is a location parameter, $\lambda > 0$ is a scale parameter, and $g(\cdot)$ is one of three functional forms:
1. **Unbounded System ($S_U$)**: For distributions with infinite support in both directions:
   $$g(u) = \sinh^{-1}(u) = \ln\left(u + \sqrt{u^2 + 1}\right)$$
2. **Bounded System ($S_B$)**: For distributions with physical upper and lower boundaries (e.g., percentage measurements or dimensions bounded by tooling clearances $[\xi, \xi + \lambda]$):
   $$g(u) = \ln\left(\frac{u}{1 - u}\right), \qquad 0 < u < 1$$
3. **Lognormal System ($S_L$)**: For strictly positive distributions bounded below by $\xi$:
   $$g(u) = \ln(u), \qquad u > 0$$

### Fitting and Capability Evaluation
Parameters are estimated by matching the first four empirical sample moments (mean $\bar{X}$, variance $S^2$, skewness $\sqrt{b_1}$, and kurtosis $b_2$) or using quantile matching across four selected percentiles ($z = \pm 0.5, \pm 1.5$). Once the optimal transformation function $f_J(X)$ is established, the engineering specification limits are mapped into the standard Gaussian space:

$$Z_{USL} = f_J(USL), \qquad Z_{LSL} = f_J(LSL)$$

The non-normal process capability indices are evaluated directly in Gaussian units:

$$C_{pu}^* = \frac{Z_{USL}}{3}, \qquad C_{pl}^* = \frac{-Z_{LSL}}{3}, \qquad C_{pk}^* = \min(C_{pu}^*, C_{pl}^*)$$

The nonconforming fraction is then computed with high numerical accuracy:
$$p = \Phi(-Z_{USL}) + \Phi(Z_{LSL})$$
This methodology avoids the large sample variance inherent in nonparametric empirical percentile estimation, providing a robust industry benchmark for non-normal capability certification.
"""
idx2 = u2_text.find("## Fully worked question 1:")
u2_text = u2_text[:idx2] + u2_add.strip() + "\n\n" + u2_text[idx2:]
u2_path.write_text(u2_text, encoding="utf-8")
print("Unit 2 expanded.")

# Unit 4 expansion: Profile Monitoring and Calibration SPC
u4_path = DRAFT_DIR / "unit-4.md"
u4_text = u4_path.read_text(encoding="utf-8")
u4_add = r"""
## 4.11 Statistical Profile Monitoring and Calibration Curve Surveillance

In modern automated manufacturing and smart machining systems, the quality of a process is increasingly characterized not by a scalar measurement or a fixed vector, but by a functional relationship—a **profile**—relating a dependent response variable $Y$ to one or more independent explanatory variables $X$:

$$Y_{ij} = f(X_{ij}; \boldsymbol{\beta}_i) + \varepsilon_{ij}, \qquad i = 1, 2, \dots, m; \quad j = 1, 2, \dots, n$$

Examples of industrial profiles include:
- The force-displacement signature curve of an automated metal stamping press.
- The torque-angle rotation profile of a robotic nut-runner tightening automotive cylinder head bolts.
- The spectrophotometric absorbance calibration curve of an in-line optical sensor.

### Linear Profile Monitoring
In the baseline Phase I formulation, suppose the profile can be modeled as a simple linear function:

$$Y_{ij} = A_{0i} + A_{1i} X_j + \varepsilon_{ij}, \qquad \varepsilon_{ij} \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)$$

where the explanatory design points $X_1, X_2, \dots, X_n$ remain fixed across all inspection cycles. For each sample $i$, ordinary least squares (OLS) regression yields sample estimates of the intercept $\widehat{a}_{0i}$, slope $\widehat{a}_{1i}$, and residual mean square error $MSE_i$.

Let $\mathbf{B}_i = (\widehat{a}_{0i}, \widehat{a}_{1i})^T$. Because the intercept and slope estimators are correlated ($\text{Cov}(\widehat{a}_0, \widehat{a}_1) = -\bar{X} \sigma^2 / S_{xx}$), univariate monitoring of slope or intercept independently causes severe blind spots.

J. D. Kang and M. B. Albin (2000) formulated the bivariate $T^2$ profile control chart:

$$T_i^2 = (\mathbf{B}_i - \boldsymbol{\beta}_0)^T \boldsymbol{\Sigma}_{\mathbf{B}}^{-1} (\mathbf{B}_i - \boldsymbol{\beta}_0)$$

where $\boldsymbol{\beta}_0 = (A_0, A_1)^T$ is the in-control parameter vector, and:

$$\boldsymbol{\Sigma}_{\mathbf{B}} = \sigma^2 \begin{pmatrix} \frac{1}{n} + \frac{\bar{X}^2}{S_{xx}} & -\frac{\bar{X}}{S_{xx}} \\ -\frac{\bar{X}}{S_{xx}} & \frac{1}{S_{xx}} \end{pmatrix}$$

Simultaneously, the residual variance $\sigma^2$ is monitored using a sample variance chart based on $MSE_i / \sigma^2 \sim \chi^2_{n-2} / (n - 2)$. If the stamping die wears out or cracking occurs, the torque-angle slope shifts or residual curvature develops, triggering an immediate profile anomaly alarm.
"""
idx4 = u4_text.find("## Fully worked question 1:")
u4_text = u4_text[:idx4] + u4_add.strip() + "\n\n" + u4_text[idx4:]
u4_path.write_text(u4_text, encoding="utf-8")
print("Unit 4 expanded.")

# Unit 5 expansion: MIL-STD-105E Switching Rules Markov Chain Analysis
u5_path = DRAFT_DIR / "unit-5.md"
u5_text = u5_path.read_text(encoding="utf-8")
u5_add = r"""
## 5.10 Mathematical Analysis of MIL-STD-105E Switching Rules via Markov Chains

The military sampling standard MIL-STD-105E (and its civilian equivalent ANSI/ASQ Z1.4) does not operate as an isolated sampling plan, but as an adaptive dynamic inspection system with three operational states: **Normal Inspection (State N)**, **Tightened Inspection (State T)**, and **Reduced Inspection (State R)**, plus an absorbing state of **Discontinued Inspection (State D)**.

The operational switching rules are defined as follows:
1. **Normal to Tightened**: When 2 out of 5 (or fewer) consecutive lots are rejected on original normal inspection.
2. **Tightened to Normal**: When 5 consecutive lots are accepted on original tightened inspection.
3. **Tightened to Discontinue**: When 5 lots remain on tightened inspection without reverting to normal inspection; contractual procurement is formally halted.
4. **Normal to Reduced**: When 10 consecutive lots are accepted under normal inspection, the total number of nonconforming units is below a specified limit number, production is steady, and reduced inspection is approved by the responsible authority.
5. **Reduced to Normal**: If a single lot is rejected, or if lot production becomes irregular.

### Markov Chain Formulation
Let $P_N(p)$, $P_T(p)$, and $P_R(p)$ denote the probability of lot acceptance under normal, tightened, and reduced inspection plans at incoming defect rate $p$. The entire system can be modeled as a discrete-time Markov chain with transition matrix $\mathbf{P}$.

W. R. Pabst and H. F. Dodge derived the stationary equilibrium probabilities $(\pi_N, \pi_T, \pi_R)$ of the operating system:

$$\boldsymbol{\pi} = \boldsymbol{\pi} \mathbf{P}, \qquad \pi_N + \pi_T + \pi_R = 1.0$$

The **Composite Operating Characteristic Curve ($P_{a, \text{system}}$)** of the complete MIL-STD-105E system is:

$$P_{a, \text{system}}(p) = \pi_N(p) P_N(p) + \pi_T(p) P_T(p) + \pi_R(p) P_R(p)$$

The switching mechanism dramatically steepens the overall OC curve:
- When incoming supplier quality is high ($p \le AQL$), $\pi_N + \pi_R \approx 1.0$, allowing the supplier to enjoy low inspection costs and near $100\%$ acceptance.
- As soon as incoming quality degrades beyond AQL ($p > AQL$), the system transitions with high probability into Tightened Inspection ($\pi_T \to 1.0$). If quality does not improve immediately, the probability of reaching Discontinuation approaches $1.0$, creating massive economic pressure on the vendor to maintain manufacturing discipline.
"""
idx5 = u5_text.find("## Fully worked question 1:")
u5_text = u5_text[:idx5] + u5_add.strip() + "\n\n" + u5_text[idx5:]
u5_path.write_text(u5_text, encoding="utf-8")
print("Unit 5 expanded.")

# Unit 6 expansion: Proportional Hazards and Competing Risks in Reliability
u6_path = DRAFT_DIR / "unit-6.md"
u6_text = u6_path.read_text(encoding="utf-8")
u6_add = r"""
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
"""
idx6 = u6_text.find("## Fully worked question 1:")
u6_text = u6_text[:idx6] + u6_add.strip() + "\n\n" + u6_text[idx6:]
u6_path.write_text(u6_text, encoding="utf-8")
print("Unit 6 expanded.")

# Unit 7 expansion: Input-Output Analysis & Leontief Multipliers
u7_path = DRAFT_DIR / "unit-7.md"
u7_text = u7_path.read_text(encoding="utf-8")
u7_add = r"""
## 7.7 Input-Output Economics: The Leontief Multiplier Matrix and Inter-Industry Linkages

A crowning analytical achievement of the System of National Accounts is the derivation of symmetric **Input-Output (I-O) Tables**, pioneered by Nobel laureate Wassily Leontief (1941). While GDP summarizes aggregate macroeconomic volume, Input-Output analysis models the intricate technological interdependencies connecting every productive sector of the industrial economy.

### The Mathematical Input-Output Architecture
Consider an economy partitioned into $n$ distinct industrial sectors. Let:
- $X_i$: Total gross output of sector $i$.
- $z_{ij}$: The monetary value of output produced by sector $i$ that is consumed as intermediate input by sector $j$ in its production process.
- $Y_i$: Final demand for the output of sector $i$ (household consumption, government spending, capital investment, and exports).

The fundamental material balance equation for sector $i$ states that total output equals intermediate demand plus final demand:

$$X_i = \sum_{j=1}^n z_{ij} + Y_i, \qquad i = 1, 2, \dots, n$$

### Technical Coefficients Matrix ($\mathbf{A}$)
Leontief introduced the assumption of fixed-proportion production technologies (constant returns to scale with zero input substitution). The **technical coefficient** $a_{ij}$ represents the value of input from sector $i$ required to produce one monetary unit of output in sector $j$:

$$a_{ij} = \frac{z_{ij}}{X_j}$$

Substituting $z_{ij} = a_{ij} X_j$ into the balance equation yields:

$$X_i = \sum_{j=1}^n a_{ij} X_j + Y_i$$

In matrix notation:

$$\mathbf{X} = \mathbf{A} \mathbf{X} + \mathbf{Y}$$

where $\mathbf{X} = (X_1, \dots, X_n)^T$ is the gross output vector, $\mathbf{Y} = (Y_1, \dots, Y_n)^T$ is the final demand vector, and $\mathbf{A} = [a_{ij}]$ is the $n \times n$ matrix of technical coefficients.

### The Leontief Inverse Matrix
Rearranging the matrix balance equation:

$$(\mathbf{I} - \mathbf{A}) \mathbf{X} = \mathbf{Y}$$

Assuming the matrix $(\mathbf{I} - \mathbf{A})$ is non-singular (which is guaranteed if the economy is productive under the Hawkins-Simon conditions):

$$\mathbf{X} = (\mathbf{I} - \mathbf{A})^{-1} \mathbf{Y} = \mathbf{L} \mathbf{Y}$$

where $\mathbf{L} = (\mathbf{I} - \mathbf{A})^{-1} = [l_{ij}]$ is the celebrated **Leontief Inverse Matrix** (or Total Requirements Matrix).

Expanding $\mathbf{L}$ as a geometric matrix power series reveals its economic meaning:

$$(\mathbf{I} - \mathbf{A})^{-1} = \mathbf{I} + \mathbf{A} + \mathbf{A}^2 + \mathbf{A}^3 + \dots$$
- $\mathbf{I}$: The direct initial impact of satisfying final demand $\mathbf{Y}$.
- $\mathbf{A}$: The first-round direct intermediate inputs required from suppliers.
- $\mathbf{A}^2$: The second-round indirect intermediate inputs required by those suppliers to produce their inputs.
- $\mathbf{A}^k$: The infinite cascade of higher-order indirect ripple effects propagating across the supply chain!

Each element $l_{ij}$ measures the total dollar increase in gross output required from sector $i$ to satisfy a one-dollar increase in final demand for the products of sector $j$.

### Forward and Backward Industrial Linkages
Albert O. Hirschman (1958) utilized the Leontief inverse to identify key industrial growth sectors:
1. **Backward Linkage Multiplier ($BL_j$)**: The column sum of the Leontief inverse:
   $$BL_j = \sum_{i=1}^n l_{ij}$$
   $BL_j$ measures the total economic stimulus transmitted backward into the upstream supply chain when demand for sector $j$ expands. Sectors with $BL_j > 1$ (e.g., automotive manufacturing, basic steel) act as powerful economic locomotives.
2. **Forward Linkage Multiplier ($FL_i$)**: The row sum of the Leontief inverse:
   $$FL_i = \sum_{j=1}^n l_{ij}$$
   $FL_i$ measures the sensitivity of sector $i$ to expansions across all downstream customer industries (e.g., electric power utilities, petroleum refining).
"""
idx7 = u7_text.find("## Fully worked question 1:")
u7_text = u7_text[:idx7] + u7_add.strip() + "\n\n" + u7_text[idx7:]
u7_path.write_text(u7_text, encoding="utf-8")
print("Unit 7 expanded.")

# Unit 8 expansion: Advanced Poverty and Inequality Metrics (SST, S-Gini)
u8_path = DRAFT_DIR / "unit-8.md"
u8_text = u8_path.read_text(encoding="utf-8")
u8_add = r"""
## 8.7 Advanced Welfare Economics: The Sen-Shorrocks-Thon Index and S-Gini

While the standard FGT family provides a foundational benchmark, modern welfare economists deploy sophisticated synthetic metrics that unify poverty incidence, poverty depth, and income inequality among the poor into a single axiomatic framework.

### The Sen-Shorrocks-Thon (SST) Index of Poverty
In 1976, Amartya Sen formulated his groundbreaking axiomatic critique of standard poverty measures, demonstrating that neither the headcount ratio ($H$) nor the poverty gap ($PG$) accounts for inequality among the poor themselves. Anthony Shorrocks (1995) and Dominique Thon (1979) refined Sen’s original metric into the **Sen-Shorrocks-Thon ($P_{\text{SST}}$) Index**:

$$P_{\text{SST}} = H \cdot I \cdot (1 + G_p)$$

where:
- $H$: The poverty headcount ratio ($q / N$).
- $I$: The income gap ratio ($\frac{1}{q} \sum_{i=1}^q \frac{z - y_i}{z}$).
- $G_p$: The Gini coefficient of the normalized poverty gaps among the poor population.

Taking logarithms decomposes changes in poverty over time into three distinct policy mechanisms:

$$\Delta \ln P_{\text{SST}} \approx \Delta \ln H + \Delta \ln I + \Delta \ln(1 + G_p)$$

This decomposition allows finance ministries to determine whether poverty reductions are being achieved by lifting marginal individuals just below the poverty line out of poverty (lowering $H$), by improving average transfers to the poor (lowering $I$), or by reducing inequality among the destitute (lowering $G_p$).

### The Generalized Extended Gini Family ($S\text{-Gini}$)
The standard Gini coefficient assigns linear rank weights $w(p) = 2(1 - p)$ across the population, which implies a fixed, moderate social preference for equality. 

S. Yitzhaki (1983) generalized the Gini coefficient into the **Single-Parameter Extended Gini ($S\text{-Gini}$)**:

$$G(\nu) = 1 - \nu (\nu - 1) \int_0^1 (1 - p)^{\nu - 2} L(p)\,dp, \qquad \nu > 1$$

where $\nu$ is an ethical inequality aversion parameter:
- When $\nu = 2$, $G(2)$ collapses exactly to the standard Corrado Gini coefficient.
- As $\nu \to \infty$, the social welfare weighting shifts entirely to the poorest individual in society, converging to the **Rawlsian Maximin criterion** ($G(\infty) = 1 - y_{\text{min}}/\mu$).
- When $\nu \to 1$, $G(1) = 0$, reflecting complete social indifference to inequality.

By calculating $G(\nu)$ across multiple values of $\nu \in [1.5, 4.0]$, national statistical agencies provide policymakers with sensitivity bounds that prevent ideological bias in national welfare reporting.
"""
idx8 = u8_text.find("## Fully worked question 1:")
u8_text = u8_text[:idx8] + u8_add.strip() + "\n\n" + u8_text[idx8:]
u8_path.write_text(u8_text, encoding="utf-8")
print("Unit 8 expanded.")
