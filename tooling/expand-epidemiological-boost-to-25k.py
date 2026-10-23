#!/usr/bin/env python3
"""
Booster script for Epidemiological Statistics to ensure substantive prose
in data.js comfortably exceeds 25,000 words.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "publishing/drafts/statistics-probability-epidemiological-statistics"

# Unit 1
u1_path = DRAFT_DIR / "unit-1.md"
u1_text = u1_path.read_text(encoding="utf-8")
u1_add = r"""
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
"""

# Unit 2
u2_path = DRAFT_DIR / "unit-2.md"
u2_text = u2_path.read_text(encoding="utf-8")
u2_add = r"""
## 2.8 The Counterfactual Framework and Potential Outcomes in Causal Inference

A central objective of modern epidemiological research is determining whether an observed statistical association between an exposure $A$ and a health outcome $Y$ represents a true causal relationship. Classical observational epidemiology relied on associative risk ratios and odds ratios, which are vulnerable to confounding and selection biases. Contemporary causal inference formalizes causality using the **Counterfactual (Potential Outcomes) Framework**, formulated by Donald Rubin and extended to epidemiology by James Robins and Miguel Hernán.

### 1. Potential Outcomes Definition
Let $A \in \{0, 1\}$ denote a binary exposure (e.g., $A = 1$ if treated with an antihypertensive medication, $A = 0$ if untreated).
For each individual $i$ in the study population, we define two **Potential Outcomes**:
- $Y_i(1)$: The health outcome that would be observed if individual $i$ were exposed to $A = 1$.
- $Y_i(0)$: The health outcome that would be observed if individual $i$ were exposed to $A = 0$.

The **Individual Causal Effect** of exposure $A$ for person $i$ is defined as the difference between their potential outcomes:
$$\Delta_i = Y_i(1) - Y_i(0)$$

**The Fundamental Problem of Causal Inference**: For any given individual, we can observe $Y_i(1)$ (if they received exposure) or $Y_i(0)$ (if they remained unexposed), but *never both simultaneously*. The unobserved potential outcome is the **counterfactual**.

### 2. Population Causal Contrasts
Because individual causal effects are unobservable, epidemiology focuses on **Average Causal Effects** across populations:
1. **Average Treatment Effect (ATE)**: The expected difference in potential outcomes across the entire target population:
   $$ATE = \mathbb{E}[Y(1) - Y(0)] = \mathbb{E}[Y(1)] - \mathbb{E}[Y(0)]$$
2. **Average Treatment Effect on the Treated (ATT)**: The causal effect among those who actually received the exposure:
   $$ATT = \mathbb{E}[Y(1) - Y(0) \mid A = 1] = \mathbb{E}[Y(1) \mid A = 1] - \mathbb{E}[Y(0) \mid A = 1]$$
3. **Causal Risk Ratio ($RR_{\text{causal}}$)**:
   $$RR_{\text{causal}} = \frac{\mathbb{E}[Y(1)]}{\mathbb{E}[Y(0)]}$$

### 3. The Three Core Identifiability Conditions
To estimate causal effects from observational data (where treatment assignment is non-random), three rigorous mathematical identifiability conditions must hold:
1. **Exchangeability (Conditional Unconfoundedness)**: Conditional on a vector of measured pre-exposure baseline confounders $L$, the potential outcomes are conditionally independent of actual exposure assignment:
   $$(Y(1), Y(0)) \perp A \mid L$$
   Under exchangeability, the counterfactual outcome among the exposed had they been unexposed equals the observed outcome among the unexposed within strata of $L$: $\mathbb{E}[Y(0) \mid A = 1, L] = \mathbb{E}[Y \mid A = 0, L]$.
2. **Positivity**: Every individual in the population within covariate strata $L$ must have a non-zero probability of receiving either exposure level:
   $$0 < P(A = 1 \mid L = l) < 1 \quad \text{for all } l \text{ such that } P(L = l) > 0$$
   If positivity is violated (structural or random zeros), causal contrast is mathematically undefined because counterfactual trajectories cannot be observed.
3. **Consistency**: The observed outcome $Y$ for an individual receiving treatment $A = a$ equals their potential outcome under that specific treatment:
   $$Y = A \cdot Y(1) + (1 - A) \cdot Y(0)$$
   Consistency requires well-defined interventions with no hidden versions of treatment and no interference between individuals (Stable Unit Treatment Value Assumption - SUTVA).

When these three conditions are satisfied, the causal effect is non-parametrically identifiable from observational data via G-computation or propensity score weighting:
$$\mathbb{E}[Y(a)] = \sum_l \mathbb{E}[Y \mid A = a, L = l] \cdot P(L = l)$$
"""

# Unit 8
u8_path = DRAFT_DIR / "unit-8.md"
u8_text = u8_path.read_text(encoding="utf-8")
u8_add = r"""
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
"""

targets = [
    (1, u1_path, u1_text, u1_add),
    (2, u2_path, u2_text, u2_add),
    (8, u8_path, u8_text, u8_add),
]

for unit_num, path, text, add in targets:
    marker = "## Fully worked question 1:"
    idx = text.find(marker)
    if idx == -1:
        print(f"Warning: Marker not found in unit {unit_num}!")
        continue
    new_text = text[:idx] + add.strip() + "\n\n" + text[idx:]
    path.write_text(new_text, encoding="utf-8")
    print(f"Unit {unit_num} boosted successfully.")

print("Epidemiological units boosted.")
