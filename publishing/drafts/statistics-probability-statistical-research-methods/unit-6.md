# Unit 6: Modern Causal Inference in Statistical Research

For nearly a century following Karl Pearson's rejection of causation as "unscientific metaphysics," statistical orthodoxy insisted that statistics could speak only of association, correlation, and joint probability distributions. The dogma "correlation does not imply causation" was treated as an impenetrable barrier, leaving researchers without a formal mathematical language to express causal questions. Yet in every empirical discipline—medicine, epidemiology, economics, public policy, and social science—the core scientific questions are inherently causal: *"Does this therapeutic compound cure the disease?" "Does increasing the minimum wage elevate youth unemployment?" "Did the emissions regulation decrease respiratory hospitalizations?"*

In the late twentieth and early twenty-first centuries, a profound methodological revolution swept statistical science: the emergence of modern formal causal inference. Synthesizing Donald Rubin's Potential Outcomes Framework with Judea Pearl's Structural Causal Models and Directed Acyclic Graphs (DAGs), statistics acquired the mathematical machinery to formalize, identify, and estimate causal effects from observational and quasi-experimental data. This unit examines the foundational theorems of modern causal inference, graphical d-separation, the Backdoor and Frontdoor criteria, Instrumental Variables (IV), Regression Discontinuity Designs (RDD), and Difference-in-Differences (DiD) architectures.

## 6.1 Correlation versus Causation: The Potential Outcomes Framework
The modern mathematical formalization of causation originated in Jerzy Neyman's 1923 agricultural experiments and was generalized to observational studies by Donald Rubin in 1974 (the Neyman-Rubin Causal Model).

Consider a binary treatment indicator $D_i \in \{0, 1\}$, where $D_i = 1$ denotes exposure to the experimental treatment and $D_i = 0$ denotes exposure to the control condition.
For each individual unit $i$ in a population, we define two Potential Outcomes:
- $Y_i(1)$: The outcome value that unit $i$ would realize if exposed to treatment ($D_i = 1$).
- $Y_i(0)$: The outcome value that unit $i$ would realize if exposed to control ($D_i = 0$).

The individual causal effect for unit $i$ is defined as the contrast:
$$\tau_i \equiv Y_i(1) - Y_i(0)$$
This definition reveals the Fundamental Problem of Causal Inference:
For any individual unit $i$, we observe only the outcome corresponding to the treatment actually received:
$$Y_i = D_i Y_i(1) + (1 - D_i) Y_i(0)$$
If unit $i$ receives treatment ($D_i = 1$), we observe $Y_i(1)$, while the counterfactual potential outcome $Y_i(0)$ remains unobservable. If unit $i$ receives control ($D_i = 0$), we observe $Y_i(0)$, while $Y_i(1)$ is counterfactual. Causal inference is fundamentally a missing data problem: for every individual, exactly one potential outcome is missing.

To identify causal effects, researchers shift from individual effects $\tau_i$ to population average effects:
- Average Treatment Effect (ATE):
$$\tau_{\text{ATE}} \equiv \mathbb{E}[Y(1) - Y(0)] = \mathbb{E}[Y(1)] - \mathbb{E}[Y(0)]$$
- Average Treatment Effect on the Treated (ATT):
$$\tau_{\text{ATT}} \equiv \mathbb{E}[Y(1) - Y(0) \mid D = 1] = \mathbb{E}[Y(1) \mid D = 1] - \mathbb{E}[Y(0) \mid D = 1]$$

### The Stable Unit Treatment Value Assumption (SUTVA)
The mathematical validity of the potential outcomes framework requires SUTVA:
1. No Interference (Spillover): The potential outcomes of unit $i$ are unaffected by the treatment status of any other unit $j \ne i$:
$$Y_i(d_1, d_2, \dots, d_n) = Y_i(d_i)$$
(Violated in vaccination programs with herd immunity, or social network interventions).
2. No Hidden Variations of Treatment: The treatment administered to unit $i$ is identical in dosage and delivery mechanism to the treatment received by any other treated unit (consistency: if $D_i = d$, then $Y_i = Y_i(d)$).

### Decomposing Naive Observational Association
Consider the naive observational difference between the sample means of treated and untreated cohorts:
$$\Delta_{\text{naive}} = \mathbb{E}[Y \mid D = 1] - \mathbb{E}[Y \mid D = 0]$$
Using the potential outcomes identity, expand $\Delta_{\text{naive}}$:
$$\Delta_{\text{naive}} = \mathbb{E}[Y(1) \mid D = 1] - \mathbb{E}[Y(0) \mid D = 0]$$
Add and subtract the counterfactual quantity $\mathbb{E}[Y(0) \mid D = 1]$:
$$\Delta_{\text{naive}} = \underbrace{\mathbb{E}[Y(1) \mid D = 1] - \mathbb{E}[Y(0) \mid D = 1]}_{\tau_{\text{ATT}}} + \underbrace{\left( \mathbb{E}[Y(0) \mid D = 1] - \mathbb{E}[Y(0) \mid D = 0] \right)}_{\text{Selection Bias}}$$
Naive observational comparisons confound the true causal treatment effect on the treated ($\tau_{\text{ATT}}$) with Selection Bias: the baseline disparity in potential control outcomes between individuals who choose treatment versus those who do not. In a completely randomized trial, $D \perp\!\!\perp (Y(1), Y(0))$, so baseline selection bias vanishes ($\mathbb{E}[Y(0) \mid D = 1] = \mathbb{E}[Y(0) \mid D = 0]$), guaranteeing $\Delta_{\text{naive}} = \tau_{\text{ATE}}$. In observational studies, selection bias must be neutralized through structural causal modeling.

## 6.2 Causal Directed Acyclic Graphs (DAGs) and the $d$-Separation Criterion
Judea Pearl formalized causal relationships using non-parametric Directed Acyclic Graphs (DAGs). A causal DAG $\mathcal{G} = (\mathcal{V}, \mathcal{E})$ consists of a set of vertices $\mathcal{V}$ representing random variables and a set of directed arrows $\mathcal{E}$ representing direct causal influences. The graph is acyclic: no directed path can loop back to its starting node.

A causal DAG encodes the complete qualitative causal structure of a data-generating system. All statistical associations between two variables $X$ and $Y$ flow along paths connecting them. Paths consist of combinations of three fundamental junction typologies:

1. The Chain (Mediation):
$$X \longrightarrow M \longrightarrow Y$$
Variable $X$ causally influences mediator $M$, which causally influences $Y$.
- Unconditioned: The path is open; $X$ and $Y$ are statistically dependent ($X \not\perp\!\!\perp Y$).
- Conditioned on $M$: Conditioning on the intermediate mediator blocks the path; $X$ and $Y$ become conditionally independent ($X \perp\!\!\perp Y \mid M$).
2. The Fork (Common Cause / Confounder):
$$X \longleftarrow Z \longrightarrow Y$$
Variable $Z$ is a mutual common cause of both $X$ and $Y$.
- Unconditioned: The path is open; $Z$ transmits a spurious non-causal association between $X$ and $Y$ ($X \not\perp\!\!\perp Y$).
- Conditioned on $Z$: Conditioning on the common cause blocks the spurious path; $X$ and $Y$ become conditionally independent ($X \perp\!\!\perp Y \mid Z$).
3. The Inverted Fork / Collider (Mutual Effect):
$$X \longrightarrow C \longleftarrow Y$$
Two independent causes $X$ and $Y$ both influence a mutual outcome (collider) $C$.
- Unconditioned: The collider naturally blocks the path! Without conditioning, no association flows between $X$ and $Y$; they are completely independent ($X \perp\!\!\perp Y$).
- Conditioned on $C$ (or any descendant of $C$): Conditioning on a collider *opens* the path! Conditioning induces a spurious, non-causal statistical correlation between previously independent causes ($X \not\perp\!\!\perp Y \mid C$). This phenomenon is known as Berkson's Paradox or Collider Stratification Bias (M-bias).

### The $d$-Separation Criterion
Judea Pearl established the $d$-separation (directional separation) theorem, providing a purely algorithmic graphical rule for determining whether two variables $X$ and $Y$ are conditionally independent given an conditioning set $\mathbf{Z}$:

Definition: A path $p$ between $X$ and $Y$ is blocked (d-separated) by a set of conditioning nodes $\mathbf{Z}$ if and only if:
1. Path $p$ contains a chain ($A \to B \to C$) or a fork ($A \leftarrow B \to C$) such that the middle node $B$ is in $\mathbf{Z}$; OR
2. Path $p$ contains a collider ($A \to C \leftarrow B$) such that neither the collider $C$ nor any descendant of $C$ is in $\mathbf{Z}$.

If all paths connecting $X$ and $Y$ are blocked by $\mathbf{Z}$, then $X$ and $Y$ are $d$-separated by $\mathbf{Z}$, which implies that $X$ and $Y$ are conditionally independent given $\mathbf{Z}$ across all probability distributions compatible with the graph:
$$X \perp\!\!\perp_{\mathcal{G}} Y \mid \mathbf{Z} \implies X \perp\!\!\perp Y \mid \mathbf{Z}$$

## 6.3 The Backdoor Criterion and Frontdoor Adjustment
Pearl derived non-parametric identification theorems that dictate exactly which variables must be adjusted for—and which variables must *never* be adjusted for—to estimate the true causal effect of an intervention $\mathrm{do}(X = x)$ on outcome $Y$:

### The Backdoor Criterion
A set of variables $\mathbf{Z}$ satisfies the Backdoor Criterion relative to an ordered pair of variables $(X, Y)$ in a DAG $\mathcal{G}$ if:
1. No node in $\mathbf{Z}$ is a causal descendant of $X$; AND
2. The set $\mathbf{Z}$ blocks (d-separates) every backdoor path from $X$ to $Y$ (where a backdoor path is any path connecting $X$ and $Y$ that begins with an arrow pointing *into* $X$: $X \leftarrow \cdots Y$).

Theorem (Backdoor Adjustment Formula):
If a set of covariates $\mathbf{Z}$ satisfies the Backdoor Criterion, the causal effect of $X$ on $Y$ is non-parametrically identified by the adjustment formula:
$$P(Y = y \mid \mathrm{do}(X = x)) = \sum_{\mathbf{z}} P(Y = y \mid X = x, \mathbf{Z} = \mathbf{z}) P(\mathbf{Z} = \mathbf{z})$$
The corresponding average causal effect is estimated by adjusting for $\mathbf{Z}$ via multivariable regression, propensity score matching, or inverse probability weighting.

### The Frontdoor Criterion
When confounders $U$ between $X$ and $Y$ are completely unobserved (making backdoor adjustment impossible), Pearl discovered that causal effects can still be identified if an observed intermediate mechanism $M$ satisfies the Frontdoor Criterion:
1. $M$ intercepts all directed causal paths from $X$ to $Y$ ($X \to M \to Y$).
2. There are no unblocked backdoor paths from $X$ to $M$.
3. All backdoor paths from $M$ to $Y$ are blocked by $X$.

Under the Frontdoor Criterion, the causal effect is identified without measuring $U$:
$$P(Y = y \mid \mathrm{do}(X = x)) = \sum_m P(M = m \mid X = x) \sum_{x'} P(Y = y \mid X = x', M = m) P(X = x')$$

## 6.4 Instrumental Variables (IV) and Two-Stage Least Squares (2SLS)
When unmeasured confounding between treatment $X$ and outcome $Y$ exists and cannot be blocked, the Instrumental Variables (IV) approach achieves causal identification by exploiting an exogenous source of variation $Z$.

A valid instrumental variable $Z$ must satisfy three structural core conditions:
1. Relevance Condition (Instrument Strength): $Z$ has a non-zero causal effect on treatment $X$:
$$\mathrm{Cov}(Z, X) \ne 0$$
2. Exogeneity / Independence Condition: $Z$ is as good as randomly assigned; it is statistically independent of all unobserved confounders $U$:
$$Z \perp\!\!\perp U$$
3. Exclusion Restriction: $Z$ affects the outcome $Y$ *only* through its effect on treatment $X$. There is no direct causal arrow from $Z$ to $Y$, and no unblocked backdoor path connecting $Z$ and $Y$:
$$Y(x, z) = Y(x)$$

Under linear homogeneous models:
$$Y = \beta_0 + \beta_1 X + \epsilon, \quad \mathrm{Cov}(X, \epsilon) \ne 0$$
The Instrumental Variable estimator (Wald Estimator for binary $Z$) is:
$$\beta_{\text{IV}} = \frac{\mathrm{Cov}(Y, Z)}{\mathrm{Cov}(X, Z)} = \frac{\mathbb{E}[Y \mid Z = 1] - \mathbb{E}[Y \mid Z = 0]}{\mathbb{E}[X \mid Z = 1] - \mathbb{E}[X \mid Z = 0]} = \frac{\text{Reduced-Form Intention-to-Treat Effect}}{\text{First-Stage Compliance Rate}}$$

### Local Average Treatment Effects (LATE)
In their seminal 1994 paper, Joshua Angrist and Guido Imbens (2021 Nobel Prize in Economic Sciences) analyzed IV under heterogeneous treatment effects and non-compliance.
They partitioned the population into four latent compliance strata:
1. Compliers: Units who take treatment if assigned, and do not if not assigned ($X(1) = 1, X(0) = 0$).
2. Always-Takers: Units who always take treatment regardless of instrument status ($X(1) = 1, X(0) = 1$).
3. Never-Takers: Units who never take treatment regardless of instrument status ($X(1) = 0, X(0) = 0$).
4. Defiers: Units who do the exact opposite of their assignment ($X(1) = 0, X(0) = 1$).

Under the Monotonicity Assumption (no defiers: $X_i(1) \ge X_i(0)$ for all $i$), Angrist and Imbens proved that the IV estimator identifies the Local Average Treatment Effect (LATE):
$$\beta_{\text{IV}} = \mathbb{E}[Y(1) - Y(0) \mid X(1) - X(0) = 1] = \tau_{\text{LATE}}$$
The causal effect is identified specifically for the subpopulation of Compliers—individuals whose treatment uptake was actively induced by the instrument.

### Weak Instrument Problem and Stock-Yogo Diagnostic
If the instrument is weakly correlated with treatment ($\mathrm{Cov}(Z, X) \approx 0$), the denominator of $\beta_{\text{IV}}$ approaches zero. James Stock and Motohiro Yogo established that weak instruments cause severe finite-sample bias toward the confounded OLS estimate and produce invalid standard errors. Researchers must report the First-Stage $F$-statistic testing $H_0: \gamma = 0$ in $X = \pi_0 + \gamma Z + \nu$. As a rule of thumb, $F > 10$ (or Stock-Yogo critical values $F > 16.38$) is required to rule out weak instrument bias.

## 6.5 Regression Discontinuity Design (RDD)
The Regression Discontinuity Design (RDD), introduced by Donald Thistlethwaite and Donald Campbell (1960), is widely considered the most credible quasi-experimental architecture because it exploits local administrative rules to mimic randomized trials.

In RDD, treatment assignment $D_i$ is determined strictly by whether an observed continuous running variable (forcing variable) $X_i$ crosses an exogenous cutoff threshold $c$:
- Sharp RDD: Treatment is deterministic:
$$D_i = \mathbb{I}(X_i \ge c)$$
(e.g., students scoring $\ge 80.0$ receive a merit scholarship; students scoring $< 80.0$ do not).
- Fuzzy RDD: The probability of treatment jumps discontinuously at the cutoff:
$$\lim_{x \downarrow c} P(D = 1 \mid X = x) \ne \lim_{x \uparrow c} P(D = 1 \mid X = x)$$

### Identification Assumption: Continuity of Potential Outcomes
The foundational identification assumption of RDD is that in the absence of treatment, the conditional expectations of potential outcomes $\mathbb{E}[Y(0) \mid X = x]$ and $\mathbb{E}[Y(1) \mid X = x]$ are smooth, continuous functions of the running variable $X$ across the threshold $c$.
Units scoring just above the threshold ($c + \epsilon$) are virtually identical in all baseline traits, unobserved ability, and potential outcomes to units scoring just below ($c - \epsilon$).
Under continuity, the causal treatment effect at the cutoff is non-parametrically identified:
$$\tau_{\text{SRDD}} = \lim_{x \downarrow c} \mathbb{E}[Y \mid X = x] - \lim_{x \uparrow c} \mathbb{E}[Y \mid X = x]$$
Estimation is executed using Local Polynomial Regression within an optimal bandwidth $h$ around $c$ (using Imbens-Kalyanaraman or Calonico-Cattaneo-Titiunik optimal bandwidth selectors).
The McCrary Density Test verifies that individuals cannot precisely manipulate or sort themselves across the cutoff: a discontinuity in the marginal density of $X$ at $c$ indicates strategic gaming, invalidating RDD.

## 6.6 Difference-in-Differences (DiD) and Event Studies
Difference-in-Differences identifies causal effects in longitudinal or panel settings where a treatment group is exposed to an intervention at a specific time point, while a comparison group remains unexposed.

Let $D_i \in \{0, 1\}$ indicate treatment group membership, and let $T_t \in \{0, 1\}$ indicate post-intervention time periods.
The canonical Two-Way Fixed Effects (TWFE) regression model is:
$$Y_{it} = \alpha + \gamma D_i + \lambda T_t + \tau (D_i \times T_t) + \epsilon_{it}$$
The Difference-in-Differences estimator computes the double difference across groups and time:
$$\hat{\tau}_{\text{DiD}} = \left( \bar{Y}_{\text{treat, post}} - \bar{Y}_{\text{treat, pre}} \right) - \left( \bar{Y}_{\text{ctrl, post}} - \bar{Y}_{\text{ctrl, pre}} \right)$$

### The Parallel Trends Assumption
The fundamental identification assumption of DiD is Parallel Trends: in the counterfactual absence of treatment, the average outcome of the treatment group would have followed the identical temporal trajectory as the control group:
$$\mathbb{E}[Y_1(0) - Y_0(0) \mid D = 1] = \mathbb{E}[Y_1(0) - Y_0(0) \mid D = 0]$$
Parallel trends cannot be verified directly in the post-treatment era because counterfactual $Y_1(0) \mid D = 1$ is unobserved. Researchers assess plausibility using Event-Study Specifications across multiple pre-treatment periods:
$$Y_{it} = \alpha_i + \lambda_t + \sum_{k = -K, k \ne -1}^M \beta_k (D_i \times \mathbb{I}(t = k)) + \epsilon_{it}$$
Estimating $\beta_k \approx 0$ for all pre-treatment periods $k < -1$ provides empirical support for parallel trends.

## 6.7 Worked Problem Examples

### Fully worked question 1: Backdoor Path Identification and Sufficient Adjustment Set
An epidemiological research group investigates the causal effect of physical exercise ($X$) on cardiovascular events ($Y$).
The scientific domain knowledge is codified in a causal DAG containing five variables:
- $X$: Physical Exercise (Treatment)
- $Y$: Cardiovascular Event (Outcome)
- $A$: Age (Exogenous Demographic Variable)
- $B$: Body Mass Index (BMI)
- $S$: Genetic Cardiovascular Susceptibility (Unobserved Latent Genetic Factor)

The directed edges in the causal DAG are:
1. $A \longrightarrow X$ (Age influences exercise habits)
2. $A \longrightarrow Y$ (Age directly influences cardiovascular disease)
3. $A \longrightarrow B$ (Age influences BMI)
4. $X \longrightarrow B$ (Exercise reduces BMI)
5. $B \longrightarrow Y$ (BMI increases cardiovascular risk)
6. $S \longrightarrow B$ (Genetics influences BMI)
7. $S \longrightarrow Y$ (Genetics directly influences cardiovascular disease)

1. Enumerate all paths connecting treatment $X$ and outcome $Y$. Classify each as a causal (directed) path or a backdoor path.
2. For each backdoor path, determine whether it is naturally open or blocked, and identify any colliders.
3. Determine the minimal sufficient adjustment set of covariates $\mathbf{Z}$ that identifies the total causal effect of $X$ on $Y$ via the Backdoor Criterion. Specifically evaluate why conditioning on BMI ($B$) produces collider stratification bias (M-bias).

### Solution, step 1: Enumerate All Paths Between $X$ and $Y$
Examine all sequences of adjacent nodes connecting $X$ and $Y$:
- Path 1: $X \longrightarrow B \longrightarrow Y$
  - Classification: Directed causal path ($X$ affects $B$, which affects $Y$; $B$ is a mediator).
- Path 2: $X \longleftarrow A \longrightarrow Y$
  - Classification: Backdoor path (starts with arrow pointing into $X$: $X \leftarrow A$).
- Path 3: $X \longleftarrow A \longrightarrow B \longrightarrow Y$
  - Classification: Backdoor path ($X \leftarrow A$).
- Path 4: $X \longleftarrow A \longrightarrow B \longleftarrow S \longrightarrow Y$
  - Classification: Backdoor path ($X \leftarrow A$).
- Path 5: $X \longrightarrow B \longleftarrow S \longrightarrow Y$
  - Notice that Path 5 starts with $X \to B$. This is not a backdoor path for $X$; however, it contains node $B$ which is a collider.

### Solution, step 2: Analyze Backdoor Paths and Colliders
Evaluate the open/blocked status of each backdoor path without conditioning on any variables ($\mathbf{Z} = \emptyset$):
- Path 2 ($X \longleftarrow A \longrightarrow Y$):
  - Node $A$ is a fork (common cause). Path 2 is OPEN. It transmits confounding bias from age.
- Path 3 ($X \longleftarrow A \longrightarrow B \longrightarrow Y$):
  - Contains fork at $A$ and chain at $B$. Path 3 is OPEN. Transmits confounding bias.
- Path 4 ($X \longleftarrow A \longrightarrow B \longleftarrow S \longrightarrow Y$):
  - Notice the junction at $B$: $A \longrightarrow B \longleftarrow S$.
  - In this path, node $B$ is a COLLIDER!
  - By the rules of $d$-separation, an unconditioned collider naturally blocks the path! Therefore, Path 4 is naturally BLOCKED by collider $B$ when $\mathbf{Z} = \emptyset$.

### Solution, step 3: Determine the Minimal Sufficient Adjustment Set
We seek a conditioning set $\mathbf{Z}$ that blocks all backdoor paths without blocking causal paths or opening colliders:
1. Backdoor Path 2 ($X \leftarrow A \to Y$) is open. To block it, we MUST condition on $A$.
2. Backdoor Path 3 ($X \leftarrow A \to B \to Y$) contains $A$. Conditioning on $A$ also blocks Path 3!
3. Backdoor Path 4 ($X \leftarrow A \to B \leftarrow S \to Y$) is naturally blocked by collider $B$.
Conditioning on $\mathbf{Z} = \{A\}$ blocks both Path 2 and Path 3, while leaving Path 4 blocked.
Furthermore, $A$ is not a descendant of $X$.
Therefore, the minimal sufficient adjustment set is:
$$\mathbf{Z} = \{A\} \quad (\text{Age only})$$

### The Peril of Conditioning on BMI ($B$):
Suppose an epidemiologist includes BMI ($B$) in their regression model.
1. Over-controlling (Mediator Blocking): $B$ is on the causal path $X \to B \to Y$. Conditioning on $B$ blocks the indirect causal effect of exercise mediated through weight loss!
2. Collider Stratification Bias (M-Bias): In Path 4, $B$ is a collider between Age $A$ and unobserved genetics $S$ ($A \to B \leftarrow S$). Conditioning on $B$ *opens* Path 4:
$$X \longleftarrow A \longrightarrow [B] \longleftarrow S \longrightarrow Y$$
This creates a spurious non-causal association between $X$ and $Y$ through unobserved genetics $S$!
Controlling for BMI is a severe methodological blunder. The total causal effect is uniquely identified by adjusting strictly for Age: $\mathbf{Z} = \{A\}$.

---

### Fully worked question 2: Instrumental Variables Wald Estimator and Weak Instrument Test
An educational economist investigates the causal effect of completing an elite coding bootcamp ($X \in \{0, 1\}$) on annual software engineering salary ($Y$, in thousands of dollars).
Because motivated, high-ability students are more likely to enroll in the bootcamp, OLS regression of $Y$ on $X$ is confounded by unobserved innate ability $U$.
The admissions lottery randomly awards tuition vouchers ($Z \in \{0, 1\}$) to applicants:
- $Z = 1$: Applicant randomly awarded voucher.
- $Z = 0$: Applicant not awarded voucher.

Across a sample of $N = 2,000$ applicants:
- Reduced-form salary outcomes:
  - Mean salary for voucher winners: $\mathbb{E}[Y \mid Z = 1] = \$92.4\text{k}$.
  - Mean salary for non-winners: $\mathbb{E}[Y \mid Z = 0] = \$84.0\text{k}$.
- First-stage bootcamp completion rates:
  - Bootcamp completion rate for voucher winners: $\mathbb{E}[X \mid Z = 1] = 0.70$ ($70\%$).
  - Bootcamp completion rate for non-winners: $\mathbb{E}[X \mid Z = 0] = 0.22$ ($22\%$).
- First-stage regression coefficient standard error: $\mathrm{SE}(\hat{\gamma}_1) = 0.040$.

1. Compute the First-Stage Compliance Contrast and the Intention-to-Treat (ITT) effect.
2. Compute the Instrumental Variables Wald Estimator $\hat{\beta}_{\text{IV}}$ (Local Average Treatment Effect of bootcamp completion).
3. Compute the First-Stage $F$-statistic and evaluate whether the lottery voucher is a weak instrument under the Stock-Yogo criterion.

### Solution, step 1: Compute First-Stage Compliance and ITT Effect
The First-Stage compliance contrast is the change in the probability of bootcamp completion induced by winning the voucher:
$$\Delta X = \mathbb{E}[X \mid Z = 1] - \mathbb{E}[X \mid Z = 0] = 0.70 - 0.22 = \mathbf{0.48} \quad (48.0\%)$$
Winning the voucher increases the probability of completing the bootcamp by $48$ percentage points.
The Reduced-Form Intention-to-Treat (ITT) effect is the average difference in salary between voucher winners and non-winners:
$$\mathrm{ITT}_Y = \mathbb{E}[Y \mid Z = 1] - \mathbb{E}[Y \mid Z = 0] = 92.4 - 84.0 = \mathbf{+\$8.4\text{k}} \quad (\$8,400)$$

### Solution, step 2: Compute the Wald Estimator ($\tau_{\text{LATE}}$)
The Wald IV estimator is the ratio of the reduced-form ITT effect to the first-stage compliance contrast:
$$\hat{\beta}_{\text{IV}} = \frac{\mathbb{E}[Y \mid Z = 1] - \mathbb{E}[Y \mid Z = 0]}{\mathbb{E}[X \mid Z = 1] - \mathbb{E}[X \mid Z = 0]} = \frac{\mathrm{ITT}_Y}{\Delta X}$$
Substitute the numerical values:
$$\hat{\beta}_{\text{IV}} = \frac{8.4}{0.48} = \mathbf{+\$17.5\text{k}} \quad (\$17,500)$$
The Local Average Treatment Effect (LATE) of completing the coding bootcamp is an increase in annual salary of $\$17,500$ for the Compliers—students whose decision to complete the bootcamp was actively triggered by winning the tuition voucher.

### Solution, step 3: Calculate First-Stage $F$-Statistic and Test for Weak Instrument
In the first-stage linear regression $X_i = \gamma_0 + \gamma_1 Z_i + \nu_i$:
The estimated coefficient is $\hat{\gamma}_1 = \Delta X = 0.48$.
The standard error is $\mathrm{SE}(\hat{\gamma}_1) = 0.040$.
The $t$-statistic for the instrument is:
$$t = \frac{\hat{\gamma}_1}{\mathrm{SE}(\hat{\gamma}_1)} = \frac{0.48}{0.040} = 12.0$$
For a single instrumental variable, the first-stage $F$-statistic is simply the square of the $t$-statistic:
$$F = t^2 = (12.0)^2 = \mathbf{144.0}$$
Evaluate against the Stock-Yogo weak instrument benchmarks:
- Traditional rule of thumb: $F > 10$.
- Stock-Yogo critical value for $10\%$ maximal IV relative bias: $F = 16.38$.
Because $F = 144.0 \gg 16.38$, the voucher lottery is an extraordinarily strong instrument. Weak instrument bias is completely ruled out, and finite-sample inference is reliable.

---

### Fully worked question 3: Difference-in-Differences with Parallel Trends Verification
A municipal health department evaluates the impact of an urban sugar-sweetened beverage excise tax introduced on January 1, 2024, in City A ($D = 1$). Neighboring City B did not enact a beverage tax ($D = 0$).
An observational panel tracks average monthly consumption of sugary beverages (liters per capita):
- 2022 (Pre-tax Baseline 1): City A = $14.2$, City B = $12.1$
- 2023 (Pre-tax Baseline 2): City A = $14.0$, City B = $11.9$
- 2024 (Post-tax Year 1): City A = $11.2$, City B = $11.8$

1. Test the Parallel Trends Assumption during the pre-tax period (2022 to 2023).
2. Calculate the Difference-in-Differences estimator $\hat{\tau}_{\text{DiD}}$ of the causal effect of the beverage tax.
3. Formulate the standard Two-Way Fixed Effects regression equation and interpret the interaction parameter.

### Solution, step 1: Verify the Parallel Trends Assumption Pre-Intervention
The parallel trends assumption demands that prior to the intervention, both cities followed identical trajectories:
Compute change from 2022 to 2023 in City A (Treatment):
$$\Delta_{\text{City A, pre}} = Y_{\text{A}, 2023} - Y_{\text{A}, 2022} = 14.0 - 14.2 = \mathbf{-0.2 \text{ liters}}$$
Compute change from 2022 to 2023 in City B (Control):
$$\Delta_{\text{City B, pre}} = Y_{\text{B}, 2023} - Y_{\text{B}, 2022} = 11.9 - 12.1 = \mathbf{-0.2 \text{ liters}}$$
Compute the pre-treatment differential trend:
$$\Delta_{\text{pre-trend}} = \Delta_{\text{City A, pre}} - \Delta_{\text{City B, pre}} = -0.2 - (-0.2) = \mathbf{0.0 \text{ liters}}$$
Both cities experienced the identical $0.2\text{ liter}$ decline prior to the policy. The parallel trends assumption is verified during the pre-treatment window.

### Solution, step 2: Calculate the Difference-in-Differences Estimator
Using 2023 as the baseline pre-period and 2024 as the post-period:
- Observed change in Treatment City A:
$$\Delta_{\text{Treat}} = Y_{\text{A}, 2024} - Y_{\text{A}, 2023} = 11.2 - 14.0 = \mathbf{-2.8 \text{ liters}}$$
- Observed change in Control City B:
$$\Delta_{\text{Control}} = Y_{\text{B}, 2024} - Y_{\text{B}, 2023} = 11.8 - 11.9 = \mathbf{-0.1 \text{ liters}}$$
Compute the Difference-in-Differences:
$$\hat{\tau}_{\text{DiD}} = \Delta_{\text{Treat}} - \Delta_{\text{Control}} = (-2.8) - (-0.1) = \mathbf{-2.7 \text{ liters per capita}}$$
The beverage excise tax caused a causal reduction of $2.7$ liters of sugary beverage consumption per capita per month.

### Solution, step 3: State the Two-Way Fixed Effects Specification
The regression model estimated on monthly panel data is:
$$Y_{it} = \beta_0 + \beta_1 \mathrm{Treat}_i + \beta_2 \mathrm{Post}_t + \tau (\mathrm{Treat}_i \times \mathrm{Post}_t) + \epsilon_{it}$$
where:
- $\mathrm{Treat}_i = 1$ for City A, $0$ for City B.
- $\mathrm{Post}_t = 1$ for Year 2024, $0$ for Year 2023.
- $\beta_1 = 14.0 - 11.9 = +2.1$ captures the permanent baseline difference between City A and City B.
- $\beta_2 = -0.1$ captures the secular macroeconomic time trend common to both cities.
- The interaction coefficient $\tau = \mathbf{-2.7}$ is the true causal DiD effect of the excise tax.

## 6.9 Sensitivity Analysis for Unmeasured Confounding: Rosenbaum's $\Gamma$ and the E-Value
Because observational causal inference relies on the untestable assumption of no unmeasured confounding (unconfoundedness), rigorous research methodology requires quantitative Sensitivity Analysis: assessing how strong an unmeasured confounder would need to be to overturn the study's conclusions.

1. Rosenbaum's Bounding Method ($\Gamma$):
   Paul Rosenbaum (2002) formulated sensitivity bounds for matched observational studies. Let $\Gamma \ge 1$ denote the odds ratio of receiving treatment between two individuals matched on all observed covariates $\mathbf{X}$, caused by an unobserved confounder $U$:
   $$\frac{1}{\Gamma} \le \frac{P(D_i = 1 \mid \mathbf{X}, U_i) / [1 - P(D_i = 1 \mid \mathbf{X}, U_i)]}{P(D_j = 1 \mid \mathbf{X}, U_j) / [1 - P(D_j = 1 \mid \mathbf{X}, U_j)]} \le \Gamma$$
   When $\Gamma = 1.0$, there is zero unmeasured confounding. Rosenbaum bounds compute the threshold $\Gamma^*$ at which the $p$-value for the treatment effect crosses the non-significance boundary $\alpha = 0.05$. If a study achieves $\Gamma^* = 3.5$, an unobserved confounder would need to multiply the odds of treatment by $350\%$ to explain away the observed effect, demonstrating exceptional robustness.
2. The E-Value Metric (Ding & VanderWeele, 2016):
   Tyler VanderWeele and Peng Ding introduced the E-value, defining the minimum strength of association that an unmeasured confounder $U$ must have with *both* the treatment $D$ and the outcome $Y$, conditional on observed covariates, to fully explain away the observed treatment-outcome risk ratio $\mathrm{RR}$:
   $$\mathrm{E\text{-}value} = \mathrm{RR} + \sqrt{\mathrm{RR}(\mathrm{RR} - 1)}$$
   For an observed risk ratio of $\mathrm{RR} = 3.0$:
   $$\mathrm{E\text{-}value} = 3.0 + \sqrt{3.0(2.0)} = 3.0 + \sqrt{6.0} \approx 3.0 + 2.45 = \mathbf{5.45}$$
   To nullify the finding, an unmeasured confounder would have to be associated with both the treatment and the outcome by a risk ratio of at least $5.45$-fold each, beyond all measured controls.

## 6.10 Staggered Difference-in-Differences and the Goodman-Bacon Decomposition
In classical Difference-in-Differences, all treated units receive intervention at the identical calendar time. In real-world policy research, however, interventions adopt a Staggered Rollout architecture: different states, municipalities, or hospitals enact policies at different times.

Historically, researchers estimated staggered DiD using Two-Way Fixed Effects (TWFE) regression:
$$Y_{it} = \alpha_i + \lambda_t + \beta_{\text{TWFE}} D_{it} + \epsilon_{it}$$
In a groundbreaking 2021 econometrics paper, Andrew Goodman-Bacon proved the Goodman-Bacon Decomposition Theorem:
Under staggered timing, the TWFE coefficient $\hat{\beta}_{\text{TWFE}}$ is a weighted average of all possible $2 \times 2$ DiD comparisons across timing cohorts:
$$\hat{\beta}_{\text{TWFE}} = \sum_{k \ne l} w_{k, l} \hat{\beta}_{k, l}^{2 \times 2}$$
Critically, Goodman-Bacon proved that the comparison pairs include:
1. Early-treated units versus never-treated controls (Clean comparison).
2. Late-treated units versus never-treated controls (Clean comparison).
3. Late-treated units versus *already-treated* early units, where the early-treated units serve as the control group ("Forbidden Comparison")!

If the causal treatment effect evolves, grows, or decays over time (dynamic treatment heterogeneity), using already-treated units as controls subtracts the ongoing treatment trajectory of the early cohort, producing negative weights! In fact, $\hat{\beta}_{\text{TWFE}}$ can be negative even when every individual unit experiences a positive causal effect!
Modern causal econometrics resolves this bias using robust staggered estimators: Callaway and Sant'Anna (2021) and Sun and Abraham (2021), which estimate group-time Average Treatment Effects $\mathrm{ATT}(g, t)$ using strictly clean, untreated comparison cohorts.

## 6.8 Unit 6 Methodological Synthesis and Review
Modern causal inference provides the mathematical language to answer foundational scientific inquiries:
- Formalize causal questions using Potential Outcomes ($Y(1), Y(0)$), recognizing that individual causal effects are missing data problems.
- Construct causal Directed Acyclic Graphs (DAGs) and apply $d$-separation to differentiate mediators, confounders, and colliders.
- Apply the Backdoor Criterion to identify minimal sufficient adjustment sets, strictly avoiding collider stratification bias (M-bias).
- In the presence of unobserved confounding, deploy quasi-experimental identification strategies: Instrumental Variables (2SLS/LATE), Regression Discontinuity Designs (RDD), and Difference-in-Differences (DiD).
