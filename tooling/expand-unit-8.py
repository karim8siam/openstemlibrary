# tooling/expand-unit-8.py
import re

content = """

### Unit-Level Small Area Estimation: The Battese–Harter–Fuller Nested Error Model

While the Fay–Herriot model operates on aggregated area-level summary statistics $\\hat{\\theta}_d$, statistical agencies frequently possess survey microdata recorded at the individual sampling unit level alongside complete administrative registers or census data. In their seminal contribution, Battese, Harter, and Fuller (1988) formulated the **Nested Error Regression Model** for unit-level small area estimation, originally applied to predict county-level crop acreage using Landsat satellite spectral readings.

#### Model Formulation
Let $y_{dj}$ denote the response variable of interest for individual unit $j$ ($j = 1, \\dots, n_d$) in small area $d$ ($d = 1, \\dots, D$). Let $\\mathbf{x}_{dj} = (x_{dj1}, \\dots, x_{djp})^\\top$ denote a $p$-dimensional vector of unit-level auxiliary covariates whose values are known for all sampled units as well as for all non-sampled units in the target population (or at minimum, the area-level population mean vector $\\bar{\\mathbf{X}}_d = \\frac{1}{N_d} \\sum_{j=1}^{N_d} \\mathbf{x}_{dj}$ is known from census records).

The classical Battese–Harter–Fuller model postulates:
$$y_{dj} = \\mathbf{x}_{dj}^\\top \\boldsymbol{\\beta} + v_d + e_{dj}, \\quad d = 1, \\dots, D; \\quad j = 1, \\dots, n_d$$

where:
1. $\\boldsymbol{\\beta}$ is a $p \\times 1$ vector of fixed regression coefficients shared across all areas.
2. $v_d \\stackrel{iid}{\\sim} \\mathcal{N}(0, \\sigma_v^2)$ are unobserved area-specific random effects capturing common unmeasured geographical or institutional factors characterizing area $d$.
3. $e_{dj} \\stackrel{iid}{\\sim} \\mathcal{N}(0, \\sigma_e^2)$ are individual-level idiosyncratic disturbances.
4. The random effects $v_d$ and unit errors $e_{dj}$ are mutually independent for all $d$ and $j$.

The parameter of interest is the true small area finite population mean:
$$\\bar{Y}_d = \\frac{1}{N_d} \\sum_{j=1}^{N_d} y_{dj} = \\frac{1}{N_d} \\left[ \\sum_{j \\in s_d} y_{dj} + \\sum_{j \\notin s_d} y_{dj} \\right]$$

For populations where the sampling fraction $f_d = n_d / N_d$ is negligible ($f_d \\approx 0$), predicting the finite population mean $\\bar{Y}_d$ is equivalent to predicting the conditional superpopulation mean:
$$\\mu_d = E(y_{dj} \\mid v_d) = \\bar{\\mathbf{X}}_d^\\top \\boldsymbol{\\beta} + v_d$$

#### Derivation of the Best Linear Unbiased Predictor (BLUP)
Under the nested error structure, the covariance matrix of the observations $\\mathbf{y}_d = (y_{d1}, \\dots, y_{dn_d})^\\top$ in area $d$ takes the compound symmetric form:
$$\\mathbf{V}_d = \\text{Var}(\\mathbf{y}_d) = \\sigma_v^2 \\mathbf{1}_{n_d} \\mathbf{1}_{n_d}^\\top + \\sigma_e^2 \\mathbf{I}_{n_d}$$
where $\\mathbf{1}_{n_d}$ is an $n_d \\times 1$ vector of ones, and $\\mathbf{I}_{n_d}$ is the identity matrix of order $n_d$.

Applying the Sherman–Morrison matrix inversion formula, the inverse covariance matrix is:
$$\\mathbf{V}_d^{-1} = \\frac{1}{\\sigma_e^2} \\left[ \\mathbf{I}_{n_d} - \\frac{\\gamma_d}{n_d} \\mathbf{1}_{n_d} \\mathbf{1}_{n_d}^\\top \\right]$$
where the shrinkage factor $\\gamma_d \\in [0, 1]$ is explicitly defined as:
$$\\gamma_d = \\frac{n_d \\sigma_v^2}{\\sigma_e^2 + n_d \\sigma_v^2} = \\frac{\\sigma_v^2}{\\sigma_v^2 + \\sigma_e^2 / n_d}$$

Notice the mathematical structure of this expression: $\\sigma_e^2 / n_d$ is simply the variance of the sample mean of the individual error terms $\\bar{e}_d = \\frac{1}{n_d} \\sum_{j=1}^{n_d} e_{dj}$.

Using Henderson's mixed model equations, the Best Linear Unbiased Predictor (BLUP) of the random effect $v_d$ is:
$$\\tilde{v}_d = E(v_d \\mid \\mathbf{y}_d) = \\gamma_d (\\bar{y}_d - \\bar{\\mathbf{x}}_d^\\top \\tilde{\\boldsymbol{\\beta}})$$
where $\\bar{y}_d = \\frac{1}{n_d} \\sum_{j=1}^{n_d} y_{dj}$ is the sample mean in area $d$, $\\bar{\\mathbf{x}}_d = \\frac{1}{n_d} \\sum_{j=1}^{n_d} \\mathbf{x}_{dj}$ is the sample covariate mean vector in area $d$, and $\\tilde{\\boldsymbol{\\beta}}$ is the generalized least squares (GLS) estimator:
$$\\tilde{\\boldsymbol{\\beta}} = \\left( \\sum_{d=1}^D \\mathbf{X}_d^\\top \\mathbf{V}_d^{-1} \\mathbf{X}_d \\right)^{-1} \\sum_{d=1}^D \\mathbf{X}_d^\\top \\mathbf{V}_d^{-1} \\mathbf{y}_d$$

Consequently, the BLUP of the small area mean $\\mu_d$ is:
$$\\tilde{\\mu}_d = \\bar{\\mathbf{X}}_d^\\top \\tilde{\\boldsymbol{\\beta}} + \\tilde{v}_d = \\bar{\\mathbf{X}}_d^\\top \\tilde{\\boldsymbol{\\beta}} + \\gamma_d (\\bar{y}_d - \\bar{\\mathbf{x}}_d^\\top \\tilde{\\boldsymbol{\\beta}})$$

Rearranging terms into an intuitive convex combination reveals the shrinkage mechanism:
$$\\tilde{\\mu}_d = \\gamma_d \\left[ \\bar{y}_d + (\\bar{\\mathbf{X}}_d - \\bar{\\mathbf{x}}_d)^\\top \\tilde{\\boldsymbol{\\beta}} \\right] + (1 - \\gamma_d) \\bar{\\mathbf{X}}_d^\\top \\tilde{\\boldsymbol{\\beta}}$$

The first bracketed term is the survey regression-adjusted estimate for area $d$, which corrects for any imbalance between the sample covariates $\\bar{\\mathbf{x}}_d$ and the true population covariates $\\bar{\\mathbf{X}}_d$. The second term is the synthetic prediction derived entirely from the national regression model.
- When the area sample size $n_d$ is large, $\\gamma_d \\to 1$, giving almost exclusive weight to the area-specific sample data.
- When $n_d = 0$, $\\gamma_d = 0$, collapsing smoothly to the synthetic regression estimate $\\bar{\\mathbf{X}}_d^\\top \\tilde{\\boldsymbol{\\beta}}$.

#### Pseudo-EBLUP under Complex Sampling Designs
A critical limitation of the classical BHF BLUP is that it assumes equal probability sampling within each small area. If the survey deployed unequal probability sampling (such that units have differing sampling weights $w_{dj}$), the standard sample mean $\\bar{y}_d$ is biased for the population mean whenever sampling is informative.

To resolve this challenge, You and Rao (2002) formulated the **Pseudo-EBLUP**. Let $\\tilde{w}_{dj} = w_{dj} / \\sum_{k=1}^{n_d} w_{dk}$ be the normalized survey weight within area $d$. The weighted sample means are:
$$\\bar{y}_{d,w} = \\sum_{j=1}^{n_d} \\tilde{w}_{dj} y_{dj}, \\quad \\bar{\\mathbf{x}}_{d,w} = \\sum_{j=1}^{n_d} \\tilde{w}_{dj} \\mathbf{x}_{dj}$$

The pseudo-BLUP of $v_d$ replaces unweighted sample averages with survey-weighted averages:
$$\\tilde{v}_d^{(w)} = \\gamma_{d,w} (\\bar{y}_{d,w} - \\bar{\\mathbf{x}}_{d,w}^\\top \\tilde{\\boldsymbol{\\beta}}_w)$$
where the design-consistent shrinkage factor is:
$$\\gamma_{d,w} = \\frac{\\sigma_v^2}{\\sigma_v^2 + \\sigma_e^2 \\sum_{j=1}^{n_d} \\tilde{w}_{dj}^2}$$

Notice that if weights are equal ($w_{dj} = c$), then $\\sum \\tilde{w}_{dj}^2 = n_d (1/n_d)^2 = 1/n_d$, exactly recovering the classical BHF shrinkage factor. The pseudo-EBLUP satisfies design consistency: as $n_d \\to \\infty$, the estimator converges in design probability to the true population domain mean, guarding against model misspecification.

---

### Survival Analysis and Event-History Modeling under Complex Survey Sampling

In longitudinal epidemiological and demographic studies—such as the National Health and Nutrition Examination Survey (NHANES) linked to the National Death Index (NDI), or the Health and Retirement Study (HRS)—analysts study time-to-event outcomes (e.g. time to cardiovascular mortality, duration of unemployment, or time to household bankruptcy). Standard survival analysis software packages assume independent and identically distributed observations. Applying unweighted Kaplan–Meier estimators or standard Cox proportional hazards models to complex survey data generates biased hazard ratios and severely deflated standard errors.

#### The Counting Process Formulation
Let $T_i^*$ denote the true event time for individual $i$, and $C_i$ denote the right-censoring time. We observe the bivariate pair:
$$T_i = \\min(T_i^*, C_i), \\quad \\delta_i = I(T_i^* \\le C_i)$$
where $\\delta_i = 1$ if the event was observed and $\\delta_i = 0$ if the observation was right-censored. Let $\\mathbf{z}_i(t)$ denote a $p$-dimensional vector of possibly time-varying covariates.

Following the counting process formulation of Aalen and Gill, define:
$$N_i(t) = I(T_i \\le t, \\delta_i = 1)$$
as the counting process that records whether individual $i$ has experienced the failure event by time $t$, and:
$$Y_i(t) = I(T_i \\ge t)$$
as the at-risk indicator, indicating whether individual $i$ remains under observation and at risk of failing immediately prior to time $t$.

#### The Survey-Weighted Cox Proportional Hazards Model
The Cox model postulates that the hazard function for unit $i$ is:
$$\\lambda_i(t \\mid \\mathbf{z}_i(t)) = \\lambda_0(t) \\exp(\\mathbf{z}_i(t)^\\top \\boldsymbol{\\beta})$$
where $\\lambda_0(t)$ is an unspecified, non-parametric baseline hazard function, and $\\boldsymbol{\\beta}$ is the vector of log-hazard ratios.

In a finite population of $N$ units, the census log-partial likelihood formulated by David Cox is:
$$\\ell_{census}(\\boldsymbol{\\beta}) = \\sum_{i=1}^N \\int_0^\\infty \\left[ \\mathbf{z}_i(t)^\\top \\boldsymbol{\\beta} - \\log S^{(0)}_{census}(\\boldsymbol{\\beta}, t) \\right] dN_i(t)$$
where the census at-risk process aggregates are:
$$S^{(0)}_{census}(\\boldsymbol{\\beta}, t) = \\sum_{j=1}^N Y_j(t) \\exp(\\mathbf{z}_j(t)^\\top \\boldsymbol{\\beta})$$
$$S^{(1)}_{census}(\\boldsymbol{\\beta}, t) = \\sum_{j=1}^N Y_j(t) \\mathbf{z}_j(t) \\exp(\\mathbf{z}_j(t)^\\top \\boldsymbol{\\beta})$$

In a sample survey with complex design weights $w_i$, we cannot observe the census quantities. Binder (1992) and Lin (2000) demonstrated that design-consistent estimators of the census score functions are obtained by introducing analytic survey weights:
$$\\hat{S}^{(0)}_w(\\boldsymbol{\\beta}, t) = \\sum_{j \\in s} w_j Y_j(t) \\exp(\\mathbf{z}_j(t)^\\top \\boldsymbol{\\beta})$$
$$\\hat{S}^{(1)}_w(\\boldsymbol{\\beta}, t) = \\sum_{j \\in s} w_j Y_j(t) \\mathbf{z}_j(t) \\exp(\\mathbf{z}_j(t)^\\top \\boldsymbol{\\beta})$$

The **Survey-Weighted Pseudo-Log-Partial Likelihood** is:
$$\\ell_w(\\boldsymbol{\\beta}) = \\sum_{i \\in s} w_i \\delta_i \\left[ \\mathbf{z}_i(T_i)^\\top \\boldsymbol{\\beta} - \\log \\hat{S}^{(0)}_w(\\boldsymbol{\\beta}, T_i) \\right]$$

Differentiating $\\ell_w(\\boldsymbol{\\beta})$ with respect to $\\boldsymbol{\\beta}$ yields the survey-weighted score vector:
$$\\mathbf{U}_w(\\boldsymbol{\\beta}) = \\sum_{i \\in s} w_i \\delta_i \\left[ \\mathbf{z}_i(T_i) - \\bar{\\mathbf{Z}}_w(\\boldsymbol{\\beta}, T_i) \\right]$$
where $\\bar{\\mathbf{Z}}_w(\\boldsymbol{\\beta}, t) = \\hat{S}^{(1)}_w(\\boldsymbol{\\beta}, t) / \\hat{S}^{(0)}_w(\\boldsymbol{\\beta}, t)$ is the weighted mean covariate vector of individuals at risk at time $t$. The pseudo-maximum partial likelihood estimate $\\hat{\\boldsymbol{\\beta}}_w$ is the unique root solving $\\mathbf{U}_w(\\hat{\\boldsymbol{\\beta}}_w) = \\mathbf{0}$.

#### Robust Sandwich Covariance Estimation for Survey Cox Models
Standard survival routines compute standard errors by inverting the observed information matrix:
$$\\hat{\\mathbf{I}}_w(\\hat{\\boldsymbol{\\beta}}_w) = -\\frac{\\partial \\mathbf{U}_w}{\\partial \\boldsymbol{\\beta}^\\top} = \\sum_{i \\in s} w_i \\delta_i \\left[ \\frac{\\hat{S}^{(2)}_w(\\hat{\\boldsymbol{\\beta}}_w, T_i)}{\\hat{S}^{(0)}_w(\\hat{\\boldsymbol{\\beta}}_w, T_i)} - \\bar{\\mathbf{Z}}_w(\\hat{\\boldsymbol{\\beta}}_w, T_i) \\bar{\\mathbf{Z}}_w(\\hat{\\boldsymbol{\\beta}}_w, T_i)^\\top \\right]$$
where $\\hat{S}^{(2)}_w(\\boldsymbol{\\beta}, t) = \\sum_{j \\in s} w_j Y_j(t) \\mathbf{z}_j(t) \\mathbf{z}_j(t)^\\top \\exp(\\mathbf{z}_j(t)^\\top \\boldsymbol{\\beta})$.

However, $\\hat{\\mathbf{I}}_w^{-1}$ completely ignores the spatial clustering and stratification of the sampling design.
To compute design-defensible standard errors, Lin (2000) derived the **survey score residual** (or martingale-based influence function) for unit $i$:
$$\\mathbf{w}_{score, i} = w_i \\left\\{ \\delta_i \\left[ \\mathbf{z}_i(T_i) - \\bar{\\mathbf{Z}}_w(\\hat{\\boldsymbol{\\beta}}_w, T_i) \\right] - \\sum_{k \\in s} \\frac{w_k \\delta_k Y_i(T_k) \\exp(\\mathbf{z}_i(T_k)^\\top \\hat{\\boldsymbol{\\beta}}_w)}{\\hat{S}^{(0)}_w(\\hat{\\boldsymbol{\\beta}}_w, T_k)} \\left[ \\mathbf{z}_i(T_k) - \\bar{\\mathbf{Z}}_w(\\hat{\\boldsymbol{\\beta}}_w, T_k) \\right] \\right\\}$$

Aggregating these score residuals to the primary sampling unit (cluster) level:
$$\\mathbf{u}_{hi} = \\sum_{j \\in \\text{PSU}_{hi}} \\mathbf{w}_{score, hij}$$
the empirical between-PSU covariance matrix is:
$$\\hat{\\boldsymbol{\\Sigma}}_U = \\sum_{h=1}^H \\frac{n_h}{n_h - 1} \\sum_{i=1}^{n_h} (\\mathbf{u}_{hi} - \\bar{\\mathbf{u}}_h)(\\mathbf{u}_{hi} - \\bar{\\mathbf{u}}_h)^\\top$$

The cluster-robust sandwich variance-covariance matrix of the survey hazard ratio log-coefficients is:
$$\\hat{\\mathbf{V}}(\\hat{\\boldsymbol{\\beta}}_w) = \\hat{\\mathbf{I}}_w^{-1} \\hat{\\boldsymbol{\\Sigma}}_U \\hat{\\mathbf{I}}_w^{-1}$$

This sandwich covariance matrix guarantees asymptotically valid statistical inference and nominal coverage for 95% confidence intervals under complex multistage probability designs.

#### The Weighted Breslow Estimator for the Baseline Cumulative Hazard
To estimate absolute survival probabilities $S(t \\mid \\mathbf{z}) = \\exp(-\\Lambda_0(t) \\exp(\\mathbf{z}^\\top \\boldsymbol{\\beta}))$, the non-parametric baseline cumulative hazard $\\Lambda_0(t) = \\int_0^t \\lambda_0(u) du$ is estimated via the **Survey-Weighted Breslow Estimator**:
$$\\hat{\\Lambda}_{0,w}(t) = \\sum_{i \\in s : T_i \\le t} \\frac{w_i \\delta_i}{\\hat{S}^{(0)}_w(\\hat{\\boldsymbol{\\beta}}_w, T_i)}$$

The corresponding weighted survival function at baseline covariate values $\\mathbf{z} = \\mathbf{0}$ is $\\hat{S}_{0,w}(t) = \\exp(-\\hat{\\Lambda}_{0,w}(t))$.

---

### Longitudinal and Rotating Panel Surveys: Composite Estimation

Many of the world's most critical macroeconomic and social indicators—such as the monthly national unemployment rate, quarterly gross domestic product estimates, and monthly consumer expenditure—are produced by national statistical agencies using **rotating panel surveys**. Examples include the U.S. Current Population Survey (CPS), the Canadian Labour Force Survey (LFS), and the Eurostat Labour Force Survey (EU-LFS).

#### The Architecture of Rotating Panel Designs
In a pure cross-sectional survey, a completely fresh sample is drawn at every survey wave. While this eliminates respondent fatigue, it suffers from two major deficiencies:
1. High sampling variance when estimating month-to-month changes ($\\Delta Y = Y_t - Y_{t-1}$).
2. Substantial operational costs associated with recruiting and establishing contact with completely new households each month.

Conversely, in a pure fixed longitudinal cohort panel, the same sample of individuals is interviewed repeatedly across all waves. While this minimizes the variance of change estimates, it suffers from severe attrition, progressive nonresponse bias, and cumulative respondent conditioning.

A **Rotating Panel Survey** achieves the optimal balance. A sample is partitioned into distinct rotation groups (panels). Each rotation group enters the survey according to a prescribed schedule, remains in the sample for a designated number of months, temporarily or permanently departs, and is replaced by a newly introduced rotation group.

#### The 4-8-4 Rotation Scheme of the Current Population Survey
The U.S. Current Population Survey deploys a classic **4-8-4 rotation scheme**:
- A selected household is interviewed for **4 consecutive months** (Month in Sample MIS 1 through MIS 4).
- The household is rotated out of the sample for the next **8 consecutive months**.
- The household is returned to the sample for another **4 consecutive months** (MIS 5 through MIS 8).
- The household is then permanently retired from the survey.

At any given month $t$, the CPS sample consists of exactly 8 rotation groups:
- One group is in its 1st month in sample (new entrants).
- One group is in its 2nd month.
- One group is in its 3rd month.
- One group is in its 4th month (departing for an 8-month rest).
- One group is in its 5th month (returning after an 8-month rest).
- One group is in its 6th month.
- One group is in its 7th month.
- One group is in its 8th month (permanently departing).

This design guarantees exceptional analytical overlaps:
- **Month-to-Month Overlap**: Between month $t$ and month $t-1$, exactly 6 of the 8 rotation groups ($75\\%$) are identical (groups in MIS 2, 3, 4 and 6, 7, 8 at time $t$ were in MIS 1, 2, 3 and 5, 6, 7 at time $t-1$).
- **Year-to-Year Overlap**: Between month $t$ and month $t-12$, exactly 4 of the 8 rotation groups ($50\\%$) are identical (groups in MIS 5, 6, 7, 8 at time $t$ were in MIS 1, 2, 3, 4 at time $t-12$).

#### Theory of Composite Estimation
Let $y_{t,g}$ denote the survey estimator of the population total $Y_t$ at time $t$ based exclusively on rotation group $g$ ($g = 1, \\dots, G$, where $G = 8$ in CPS).
The standard cross-sectional estimator at time $t$ is the simple unweighted average across all $G$ rotation groups:
$$\\bar{y}_t = \\frac{1}{G} \\sum_{g=1}^G y_{t,g}$$

Although $\\bar{y}_t$ is design-unbiased, it fails to exploit the strong positive correlation $\\rho$ between the measurements of identical individuals across consecutive months. Because individuals tend to maintain their employment status from one month to the next, $\\rho = \\text{Corr}(y_{t,g}, y_{t-1,g})$ typically ranges between $0.70$ and $0.85$.

To harvest this temporal autocorrelation, Hansen, Hurwitz, and Madow (1953) developed the **K-Composite Estimator**:
$$\\hat{Y}_t^{(K)} = (1 - K) \\bar{y}_t + K \\left[ \\hat{Y}_{t-1}^{(K)} + (\\bar{y}_{t, match} - \\bar{y}_{t-1, match}) \\right]$$
where:
- $\\bar{y}_{t, match}$ is the average of the rotation groups observed at time $t$ that were also observed at time $t-1$ (the matching subsample).
- $\\bar{y}_{t-1, match}$ is the average of these same matching rotation groups evaluated at time $t-1$.
- $K \\in [0, 1)$ is a smoothing weight parameter chosen to minimize the variance of $\\hat{Y}_t^{(K)}$.

The second term inside the bracket represents an update to yesterday's composite estimate $\\hat{Y}_{t-1}^{(K)}$ using the sample difference observed among the matched panel units.

#### The AK-Composite Estimator and Rotation Group Bias
Empirical survey practitioners noticed that respondents report systematically different responses depending on how long they have been in the survey—a phenomenon known as **Rotation Group Bias** or **Time-in-Sample Bias**. For example, in labor surveys, reported unemployment rates are consistently highest in Month in Sample 1 (MIS 1) and lowest in MIS 4 and MIS 8. This is driven by differential respondent fatigue, telephonic versus in-person interview modes, and learning effects.

To simultaneously exploit autocorrelation and correct for rotation group bias, Gurney and Daly (1965) formulated the **AK-Composite Estimator**:
$$\\hat{Y}_t^{(AK)} = (1 - K) \\bar{y}_t + K \\left[ \\hat{Y}_{t-1}^{(AK)} + (\\bar{y}_{t, match} - \\bar{y}_{t-1, match}) \\right] + A \\left[ \\bar{y}_{t, unmatch} - \\frac{1}{G - m} \\sum_{g \\notin match} y_{t,g} \\right]$$
In standard CPS operations for level estimation, the Bureau of Labor Statistics optimizes the parameters at $K = 0.40$ and $A = 0.20$.
This composite estimator reduces the sampling variance of monthly unemployment levels by approximately **$15\\%$ to $20\\%$**, equivalent to interviewing thousands of additional households for free!

---

### Modern Big Data and Non-Probability Sample Integration

In the contemporary data ecosystem, survey statisticians face a dual revolution: on one side, traditional probability survey response rates have declined dramatically over the past two decades (often below $10\\%$ to $20\\%$), driving data collection costs to historic highs. On the other side, an explosion of non-probability "Big Data" sources has emerged—including opt-in online web panels, electronic health record (EHR) databases, smartphone mobility traces, and administrative transaction registries.

While non-probability datasets offer massive sample sizes ($n$ reaching hundreds of thousands or millions), they are fundamentally plagued by **selection bias**. A large sample size does not rescue an unrepresentative sample.

#### The Law of Large Populations and the Meng Paradox
To understand the danger of unweighted non-probability datasets, Xiao-Li Meng (2018) established a foundational identity relating the sample size $n$, the population size $N$, and the correlation between the survey measurement $Y$ and the sampling inclusion indicator $R$.

Let $R_i = 1$ if unit $i$ is included in the non-probability sample, and $R_i = 0$ otherwise.
The sample mean of the non-probability sample is $\\bar{y}_A = \\frac{1}{n_A} \\sum_{i=1}^N R_i y_i$.
Meng proved that the estimation error of the unweighted sample mean is:
$$\\bar{y}_A - \\bar{Y} = \\rho_{R, Y} \\times \\sigma_Y \\times \\sqrt{\\frac{N - n_A}{n_A}}$$
where:
- $\\rho_{R, Y} = \\text{Corr}(R, Y)$ is the **Data Defect Correlation (DDC)**, measuring the degree of informative selection bias.
- $\\sigma_Y$ is the standard deviation of $Y$ in the target population.
- $\\sqrt{\\frac{N - n_A}{n_A}}$ is the population scale factor.

Under simple random sampling, $\\rho_{R, Y} = O_p(1/\\sqrt{N})$, so the error shrinks at the standard $1/\\sqrt{n_A}$ rate.
However, in a non-probability sample where selection is informative (for example, healthier individuals being more likely to sign up for a digital health app, or politically engaged citizens volunteering for an online poll), $\\rho_{R, Y}$ is a non-zero constant independent of $N$.

Consequently, as population size $N$ grows, the mean squared error is dominated by the bias squared:
$$\\text{MSE}(\\bar{y}_A) \\approx \\rho_{R, Y}^2 \\sigma_Y^2 \\left( \\frac{N - n_A}{n_A} \\right)$$
Meng deduced the **Effective Sample Size ($n_{eff}$)** of a non-probability sample compared to a simple random sample:
$$n_{eff} \\approx \\frac{n_A}{1 + (N - 1) \\rho_{R, Y}^2}$$

If the target population is $N = 300,000,000$ (e.g. the United States) and the data defect correlation is merely $\rho_{R, Y} = 0.005$ (a minuscule $0.5\\%$ correlation), then:
$$n_{eff} \\approx \\frac{n_A}{1 + 300,000,000 \\times (0.005)^2} = \\frac{n_A}{1 + 300,000,000 \\times 0.000025} = \\frac{n_A}{1 + 7,500} \\approx \\frac{n_A}{7,501}$$
If the non-probability dataset has $n_A = 2,300,000$ respondents (as observed in COVID-19 vaccine uptake web surveys), its statistical accuracy is mathematically equivalent to an SRS of merely:
$$n_{eff} = \\frac{2,300,000}{7,501} \\approx 306 \\text{ individuals}$$
A rigorous probability survey of 1,000 respondents will crush a biased big dataset of 2.3 million observations in mean squared error!

#### Data Integration Architecture: Combining $S_A$ and $S_B$
To harness the rich granular size of a non-probability sample $S_A$ while preserving the design-unbiased integrity of a probability survey $S_B$, modern survey statistics deploys **Data Integration Methodology** (Rivers 2007, Yang and Kim 2020).

We assume the following data structure:
1. **Sample $S_A$ (Non-Probability)**: Contains $n_A$ units with measurements on the study variable $y_i$ and auxiliary covariates $\\mathbf{x}_i$. Sampling inclusion probabilities $\\pi_{Ai} = P(R_i = 1 \\mid \\mathbf{x}_i, y_i)$ are completely unknown.
2. **Sample $S_B$ (Probability Benchmark Survey)**: Contains $n_B$ units drawn under a known probability design with design weights $d_{Bi} = 1/\\pi_{Bi}$. $S_B$ measures covariates $\\mathbf{x}_i$, but does NOT measure the target study variable $y_i$ (or measures it only on a tiny subset).
3. **Common Covariates**: The vector of auxiliary variables $\\mathbf{x}_i$ is measured harmoniously across both datasets.

We invoke the **Ignorability Assumption** (Conditional Independence):
$$P(R_i = 1 \\mid \\mathbf{x}_i, y_i) = P(R_i = 1 \\mid \\mathbf{x}_i) = \\pi_A(\\mathbf{x}_i)$$
stating that conditional on the auxiliary vector $\\mathbf{x}_i$, inclusion into the non-probability sample $S_A$ is independent of the target outcome $y_i$. Furthermore, we require the **Positivity Assumption**: $\\pi_A(\\mathbf{x}) > 0$ for all $\\mathbf{x}$ in the support of the target population.

#### Approach 1: Mass Imputation
Under Mass Imputation (Kim, Park, Chen, and Choi 2021), we train an outcome regression model $m(\\mathbf{x}) = E(Y \\mid \\mathbf{X} = \\mathbf{x})$ using the non-probability sample $S_A$, which contains observed values of $y_i$.
Let $\\hat{m}(\\mathbf{x})$ denote the fitted regression surface (such as generalized linear models, regression trees, or deep neural networks).

We then impute the missing values of $y_i$ for every single unit in the probability benchmark sample $S_B$:
$$\\hat{y}_i = \\hat{m}(\\mathbf{x}_i), \\quad \\forall i \\in S_B$$

The **Mass Imputation Estimator** of the population mean $\\bar{Y}$ is the design-weighted average across the probability sample:
$$\\hat{\\bar{Y}}_{MI} = \\frac{\\sum_{i \\in S_B} d_{Bi} \\hat{m}(\\mathbf{x}_i)}{\\sum_{i \\in S_B} d_{Bi}}$$
Because $S_B$ is a representative probability sample, $\\hat{\\bar{Y}}_{MI}$ is design-consistent for the population mean as long as the outcome model $m(\\mathbf{x})$ is correctly specified.

#### Approach 2: Pseudo-Propensity Score Weighting
Alternatively, we can estimate the unknown propensity of entering the non-probability sample, $\\pi_A(\\mathbf{x}) = P(R_i = 1 \\mid \\mathbf{X}_i = \\mathbf{x})$.
Pool the two samples $S_A$ and $S_B$ into a combined dataset. Define a binary indicator:
$$Z_i = \\begin{cases} 1 & \\text{if } i \\in S_A \\\\ 0 & \\text{if } i \\in S_B \\end{cases}$$

Chen, Li, and Wu (2020) demonstrated that the pseudo-propensity score model $\\pi_A(\\mathbf{x}; \\boldsymbol{\\alpha}) = \\frac{\\exp(\\mathbf{x}^\\top \\boldsymbol{\\alpha})}{1 + \\exp(\\mathbf{x}^\\top \\boldsymbol{\\alpha})}$ can be estimated by solving the survey-weighted score equations:
$$\\sum_{i \\in S_A} \\mathbf{x}_i - \\sum_{i \\in S_B} d_{Bi} \\frac{\\pi_A(\\mathbf{x}_i; \\boldsymbol{\\alpha})}{1 - \\pi_A(\\mathbf{x}_i; \\boldsymbol{\\alpha})} \\mathbf{x}_i = \\mathbf{0}$$

Once the propensity parameters $\\hat{\\boldsymbol{\\alpha}}$ are estimated, the non-probability sample units receive inverse probability weights:
$$w_i^A = \\frac{1}{\\hat{\\pi}_A(\\mathbf{x}_i; \\hat{\\boldsymbol{\\alpha}})} - 1$$
The **Inverse Propensity Weighting (IPW)** estimator is:
$$\\hat{\\bar{Y}}_{IPW} = \\frac{\\sum_{i \\in S_A} w_i^A y_i}{\\sum_{i \\in S_A} w_i^A}$$

#### Approach 3: Doubly Robust Estimation
To protect against model misspecification, we combine Mass Imputation and Pseudo-Propensity Weighting into a **Doubly Robust (DR) Estimator**:
$$\\hat{\\bar{Y}}_{DR} = \\frac{1}{\\hat{N}_B} \\sum_{i \\in S_B} d_{Bi} \\hat{m}(\\mathbf{x}_i) + \\frac{1}{\\hat{N}_B} \\sum_{i \\in S_A} w_i^A \\left[ y_i - \\hat{m}(\\mathbf{x}_i) \\right]$$
where $\\hat{N}_B = \\sum_{i \\in S_B} d_{Bi}$.

#### Mathematical Proof of Double Robustness:
1. **Case 1 (Outcome Model $m(\\mathbf{x})$ is Correct, Propensity Model $\\pi_A(\\mathbf{x})$ is Misspecified)**:
   Under conditional expectation given $\\mathbf{x}$, $E(y_i \\mid \\mathbf{x}_i) = m(\\mathbf{x}_i)$.
   The second term has expectation:
   $$E\\left[ \\sum_{i \\in S_A} w_i^A (y_i - \\hat{m}(\\mathbf{x}_i)) \\right] = \\sum_{i \\in S_A} w_i^A \\left[ E(y_i \\mid \\mathbf{x}_i) - \\hat{m}(\\mathbf{x}_i) \\right] = \\sum_{i \\in S_A} w_i^A [0] = 0$$
   Therefore, the second term vanishes in expectation, and the estimator collapses to $\\frac{1}{\\hat{N}_B} \\sum_{i \\in S_B} d_{Bi} \\hat{m}(\\mathbf{x}_i)$, which is design-unbiased for $\\bar{Y}$ because $S_B$ is a probability sample.

2. **Case 2 (Propensity Model $\\pi_A(\\mathbf{x})$ is Correct, Outcome Model $m(\\mathbf{x})$ is Misspecified)**:
   If $\\pi_A(\\mathbf{x})$ is correctly specified, then by the properties of inverse propensity weighting:
   $$E\\left[ \\frac{1}{\\hat{N}_B} \\sum_{i \\in S_A} w_i^A \\hat{m}(\\mathbf{x}_i) \\right] = \\frac{1}{N} \\sum_{i=1}^N \\hat{m}(\\mathbf{x}_i) \\approx E\\left[ \\frac{1}{\\hat{N}_B} \\sum_{i \\in S_B} d_{Bi} \\hat{m}(\\mathbf{x}_i) \\right]$$
   The misspecified model terms $\\hat{m}(\\mathbf{x}_i)$ cancel each other out identically. What remains is:
   $$\\frac{1}{\\hat{N}_B} \\sum_{i \\in S_A} w_i^A y_i \\to \\bar{Y}$$
   which converges to the true population mean.

The Doubly Robust estimator $\\hat{\\bar{Y}}_{DR}$ is asymptotically unbiased if **either** the outcome regression model $m(\\mathbf{x})$ **or** the propensity score model $\\pi_A(\\mathbf{x})$ is correctly specified. This double insurance makes doubly robust estimation the gold standard for integrating non-probability big data into national statistical architectures.
"""

filepath = 'publishing/drafts/statistics-probability-sample-surveys-and-sampling-theory/unit-8.md'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

split_phrase = '## Practical Synthesis: Survey Quality Reporting Standards'
if split_phrase in text:
    parts = text.split(split_phrase)
    new_text = parts[0] + content + '\n---\n\n## Practical Synthesis: Survey Quality Reporting Standards' + parts[1]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("SUCCESSFULLY EXPANDED UNIT 8!")
else:
    print("Split phrase not found!")
