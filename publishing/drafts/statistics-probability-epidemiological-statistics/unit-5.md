# Unit 5: Multivariable Regression in Epidemiology: Logistic, Conditional Logistic, Log-Binomial & Poisson Models

While tabular stratification and Cochran-Mantel-Haenszel methods provide an intuitive and non-parametric foundation for confounding control, their practical utility breaks down rapidly when an observational study must adjust simultaneously for multiple continuous, categorical, and time-varying confounders. Stratifying by age in 5-year intervals, sex, smoking status in four categories, body mass index, systolic blood pressure, and socioeconomic status quickly partitions the cohort into thousands of sparse, empty cells (the curse of dimensionality). To overcome these limitations, modern analytical epidemiology relies on multivariable regression models. In this unit, we formalize the mathematical architecture of binary logistic regression, explore parameter interpretations as adjusted odds ratios, derive maximum likelihood estimation via Fisher scoring, establish conditional logistic regression for matched case-control designs to eliminate infinite nuisance parameters, contrast log-binomial regression against modified Poisson models with robust sandwich variance for estimating relative risks directly, examine Poisson and negative binomial models for incidence rates with person-time offsets, and formulate DAG-guided model-building strategies that avoid overadjustment and collider bias.

## 5.1 The Transition from Stratification to Multivariable Regression Modeling

In tabular stratification, controlling for $p$ discrete confounding variables requires partitioning the sample into $K = \prod_{j=1}^p k_j$ distinct strata, where $k_j$ represents the number of levels for covariate $j$. If an investigator wishes to adjust simultaneously for age (10 strata), smoking (3 strata), alcohol intake (3 strata), diabetes (2 strata), hypertension (2 strata), and geographic district (5 strata), the data are divided into $10 \times 3 \times 3 \times 2 \times 2 \times 5 = 1,800$ separate $2 \times 2$ tables. In a sample of $2,000$ individuals, the vast majority of these tables will contain zero cases or zero exposed participants. This **sparse-data problem** leads to catastrophic finite-sample bias, non-convergence of estimators, and severe loss of statistical power.

Multivariable regression models resolve this dimensionality catastrophe by imposing smooth mathematical structure across the covariate space. Rather than evaluating each subpopulation independently, parametric regression models assume that the log-odds, log-risk, or log-rate is a continuous, additive (or multiplicative) function of the covariates:

$$g(\mathbb{E}[Y \mid \mathbf{X}]) = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p$$

where $g(\cdot)$ is a monotonic **link function** that maps the bounded biological expectation into the real line $\mathbb{R}$.

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Epidemiological Model</th><th>Link Function $g(\mu)$</th><th>Underlying Distribution</th><th>Exponentiated Parameter $\exp(\beta_1)$</th><th>Primary Methodological Application</th></tr>
</thead>
<tbody>
<tr><td><strong>Binary Logistic Regression</strong></td><td>Logit: $\ln\left(\frac{\mu}{1 - \mu}\right)$</td><td>Bernoulli / Binomial</td><td>Adjusted Odds Ratio ($OR$)</td><td>Unmatched case-control studies, cross-sectional surveys.</td></tr>
<tr><td><strong>Conditional Logistic Regression</strong></td><td>Stratified Logit</td><td>Conditional Permutation</td><td>Matched Odds Ratio ($OR$)</td><td>Individually matched case-control studies (1:1, 1:M).</td></tr>
<tr><td><strong>Log-Binomial Regression</strong></td><td>Log: $\ln(\mu)$</td><td>Binomial</td><td>Adjusted Risk Ratio ($RR$)</td><td>Prospective cohort studies with common binary outcomes.</td></tr>
<tr><td><strong>Modified Poisson Regression</strong></td><td>Log: $\ln(\mu)$</td><td>Quasi-Poisson with Huber-White SE</td><td>Adjusted Risk Ratio ($RR$)</td><td>Robust alternative when log-binomial fails to converge.</td></tr>
<tr><td><strong>Poisson Rate Regression</strong></td><td>Log: $\ln(\mu / PT)$</td><td>Poisson with offset $\ln(PT)$</td><td>Adjusted Incidence Rate Ratio ($IRR$)</td><td>Open cohort tracking, incidence density analysis.</td></tr>
<tr><td><strong>Negative Binomial Regression</strong></td><td>Log: $\ln(\mu / PT)$</td><td>Negative Binomial</td><td>Adjusted Rate Ratio ($IRR$)</td><td>Overdispersed disease event count monitoring.</td></tr>
</tbody>
</table></div>

## 5.2 Binary Logistic Regression: Odds Ratios, Maximum Likelihood & Newton-Raphson

In binary logistic regression, the outcome variable $Y_i \in \{0, 1\}$ represents the presence ($1$) or absence ($0$) of disease for individual $i$. Let $\mathbf{x}_i = (1, x_{i1}, x_{i2}, \dots, x_{ip})^T$ denote the vector of explanatory covariates, where $x_{i1}$ represents the primary exposure of interest and $x_{i2}, \dots, x_{ip}$ are potential confounders. The conditional probability of disease is modeled through the logistic (sigmoid) cumulative distribution function:

$$\pi(\mathbf{x}_i) = P(Y_i = 1 \mid \mathbf{x}_i) = \frac{\exp(\mathbf{x}_i^T \boldsymbol{\beta})}{1 + \exp(\mathbf{x}_i^T \boldsymbol{\beta})} = \frac{1}{1 + \exp(-\mathbf{x}_i^T \boldsymbol{\beta})}$$

Applying the **logit link function** yields the linear predictor:

$$\text{logit}(\pi(\mathbf{x}_i)) = \ln\left( \frac{\pi(\mathbf{x}_i)}{1 - \pi(\mathbf{x}_i)} \right) = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \dots + \beta_p x_{ip}$$

### Interpretation of Regression Coefficients as Adjusted Odds Ratios
Consider the primary exposure variable $x_1$, evaluated for a dichotomous exposure ($x_1 = 1$ vs $x_1 = 0$) while holding all other adjustment covariates $\mathbf{x}_{-1} = (x_2, \dots, x_p)$ strictly constant:
- Log-odds among exposed: $\ln(\text{Odds}_1) = \beta_0 + \beta_1(1) + \sum_{j=2}^p \beta_j x_j$
- Log-odds among unexposed: $\ln(\text{Odds}_0) = \beta_0 + \beta_1(0) + \sum_{j=2}^p \beta_j x_j$

Subtracting the two equations:

$$\ln(\text{Odds}_1) - \ln(\text{Odds}_0) = \ln\left( \frac{\text{Odds}_1}{\text{Odds}_0} \right) = \beta_1$$

Exponentiating both sides:

$$OR_{\text{adjusted}} = \exp(\beta_1)$$

Thus, the exponentiated coefficient $\exp(\beta_1)$ represents the **adjusted odds ratio** for disease associated with exposure, holding all other covariates in the model mathematically constant. For a continuous covariate (such as age in years), $\exp(\beta_j)$ represents the multiplicative change in the odds of disease per 1-unit increase in that covariate. For a $c$-unit increase, the adjusted odds ratio is $\exp(c \cdot \beta_j)$.

### Maximum Likelihood Estimation via the Newton-Raphson Algorithm
Because $Y_i$ takes values in $\{0, 1\}$, its probability mass function under the Bernoulli distribution is $P(Y_i = y_i) = \pi(\mathbf{x}_i)^{y_i} [1 - \pi(\mathbf{x}_i)]^{1 - y_i}$. Assuming independent observations across $n$ individuals, the likelihood function is:

$$L(\boldsymbol{\beta}) = \prod_{i=1}^n \pi(\mathbf{x}_i)^{y_i} [1 - \pi(\mathbf{x}_i)]^{1 - y_i}$$

Taking the natural logarithm yields the log-likelihood function:

$$\ell(\boldsymbol{\beta}) = \sum_{i=1}^n \left[ y_i \ln \pi(\mathbf{x}_i) + (1 - y_i) \ln(1 - \pi(\mathbf{x}_i)) \right]$$

Substituting $\ln(1 - \pi(\mathbf{x}_i)) = -\ln(1 + e^{\mathbf{x}_i^T \boldsymbol{\beta}})$ and $\ln \pi(\mathbf{x}_i) = \mathbf{x}_i^T \boldsymbol{\beta} - \ln(1 + e^{\mathbf{x}_i^T \boldsymbol{\beta}})$:

$$\ell(\boldsymbol{\beta}) = \sum_{i=1}^n \left[ y_i \mathbf{x}_i^T \boldsymbol{\beta} - \ln(1 + \exp(\mathbf{x}_i^T \boldsymbol{\beta})) \right]$$

To maximize $\ell(\boldsymbol{\beta})$, we evaluate the first-order partial derivatives with respect to $\boldsymbol{\beta}$ (the **Score Vector** $\mathbf{U}(\boldsymbol{\beta})$):

$$\mathbf{U}(\boldsymbol{\beta}) = \frac{\partial \ell(\boldsymbol{\beta})}{\partial \boldsymbol{\beta}} = \sum_{i=1}^n \left[ y_i - \frac{\exp(\mathbf{x}_i^T \boldsymbol{\beta})}{1 + \exp(\mathbf{x}_i^T \boldsymbol{\beta})} \right] \mathbf{x}_i = \sum_{i=1}^n (y_i - \pi(\mathbf{x}_i)) \mathbf{x}_i = \mathbf{X}^T (\mathbf{y} - \boldsymbol{\pi})$$

Setting $\mathbf{U}(\boldsymbol{\beta}) = \mathbf{0}$ yields a system of non-linear equations with no closed-form algebraic solution. We compute the Maximum Likelihood Estimate $\widehat{\boldsymbol{\beta}}$ iteratively using the **Newton-Raphson algorithm** (Iteratively Reweighted Least Squares). The second partial derivative matrix is the negative **Hessian Matrix** (observed Fisher Information $\mathbf{I}(\boldsymbol{\beta})$):

$$\mathbf{I}(\boldsymbol{\beta}) = -\frac{\partial^2 \ell(\boldsymbol{\beta})}{\partial \boldsymbol{\beta} \partial \boldsymbol{\beta}^T} = \sum_{i=1}^n \pi(\mathbf{x}_i)(1 - \pi(\mathbf{x}_i)) \mathbf{x}_i \mathbf{x}_i^T = \mathbf{X}^T \mathbf{W} \mathbf{X}$$

where $\mathbf{W} = \text{diag}(\pi(\mathbf{x}_i)(1 - \pi(\mathbf{x}_i)))$ is an $n \times n$ diagonal weight matrix. The parameter vector is updated at iteration $(t + 1)$ via:

$$\boldsymbol{\beta}^{(t+1)} = \boldsymbol{\beta}^{(t)} + \left[ \mathbf{I}(\boldsymbol{\beta}^{(t)}) \right]^{-1} \mathbf{U}(\boldsymbol{\beta}^{(t)}) = \left( \mathbf{X}^T \mathbf{W}^{(t)} \mathbf{X} \right)^{-1} \mathbf{X}^T \mathbf{W}^{(t)} \mathbf{z}^{(t)}$$

where $\mathbf{z}^{(t)} = \mathbf{X} \boldsymbol{\beta}^{(t)} + [\mathbf{W}^{(t)}]^{-1} (\mathbf{y} - \boldsymbol{\pi}^{(t)})$ is the adjusted working response vector. Upon convergence, the asymptotic covariance matrix of $\widehat{\boldsymbol{\beta}}$ is obtained directly as the inverse Fisher information:

$$\widehat{\text{Cov}}(\widehat{\boldsymbol{\beta}}) = \left( \mathbf{X}^T \widehat{\mathbf{W}} \mathbf{X} \right)^{-1}$$

## 5.3 Conditional Logistic Regression for Matched Studies & Elimination of Nuisance Parameters

In individually matched case-control studies (e.g., each case matched to $M$ controls on age, sex, and clinic), standard unconditional logistic regression encounters a fatal theoretical obstacle known as the **Neyman-Scott Problem**.

### The Neyman-Scott Paradox
Suppose a study enrolls $K$ individually matched 1:1 pairs ($N = 2K$ total participants). To control for the matching strata in an unconditional logistic regression model, the investigator must include a separate indicator variable (intercept $\alpha_k$) for each matched pair:

$$\text{logit}(P(Y_{ki} = 1)) = \alpha_k + \beta_1 X_{ki}, \quad k = 1, \dots, K; \quad i \in \{1, 2\}$$

As sample size grows by enrolling more pairs ($K \to \infty$), the number of incidental nuisance parameters $\alpha_1, \dots, \alpha_K$ increases at the exact same rate as the sample size! In 1948, Jerzy Neyman and Elizabeth Scott proved that when the number of nuisance parameters grows proportionally with $n$, the unconditional Maximum Likelihood Estimator of $\beta_1$ is **asymptotically inconsistent**. For 1:1 matched pairs, the unconditional estimator converges to exactly twice the true parameter value:

$$\widehat{\beta}_{1, \text{unconditional}} \xrightarrow{p} 2 \beta_1 \implies \widehat{OR}_{\text{unconditional}} \xrightarrow{p} (OR_{\text{true}})^2$$

### The Conditional Likelihood Formulation
To eliminate the infinite nuisance intercepts $\alpha_k$, David Cox (1958) formulated **Conditional Logistic Regression**. Rather than maximizing the unconditional likelihood, we condition on the sufficient statistic for $\alpha_k$: the total number of cases observed in stratum $k$ (which is fixed at 1 for 1:$M$ matched designs).

Consider matched stratum $k$ containing 1 case ($i = 0$) and $M$ controls ($i = 1, \dots, M$). The conditional probability that individual 0 is the case, given that exactly one person in the set developed the disease, is:

$$P(Y_{k0} = 1 \mid \sum_{i=0}^M Y_{ki} = 1) = \frac{\pi(\mathbf{x}_{k0}) \prod_{i=1}^M [1 - \pi(\mathbf{x}_{ki})]}{\sum_{j=0}^M \pi(\mathbf{x}_{kj}) \prod_{i \neq j} [1 - \pi(\mathbf{x}_{ki})]}$$

Dividing numerator and denominator by $\prod_{i=0}^M [1 - \pi(\mathbf{x}_{ki})]$:

$$P(Y_{k0} = 1 \mid \sum_{i=0}^M Y_{ki} = 1) = \frac{\frac{\pi(\mathbf{x}_{k0})}{1 - \pi(\mathbf{x}_{k0})}}{\sum_{j=0}^M \frac{\pi(\mathbf{x}_{kj})}{1 - \pi(\mathbf{x}_{kj})}} = \frac{\exp(\alpha_k + \mathbf{x}_{k0}^T \boldsymbol{\beta})}{\sum_{j=0}^M \exp(\alpha_k + \mathbf{x}_{kj}^T \boldsymbol{\beta})}$$

Notice that the stratum intercept $\exp(\alpha_k)$ factors out identically from both the numerator and every term in the denominator:

$$P(Y_{k0} = 1 \mid \sum_{i=0}^M Y_{ki} = 1) = \frac{\exp(\mathbf{x}_{k0}^T \boldsymbol{\beta})}{\sum_{j=0}^M \exp(\mathbf{x}_{kj}^T \boldsymbol{\beta})}$$

The nuisance parameters $\alpha_k$ vanish completely! The **conditional log-likelihood** across all $K$ matched strata is:

$$\ell_{\text{cond}}(\boldsymbol{\beta}) = \sum_{k=1}^K \left[ \mathbf{x}_{k0}^T \boldsymbol{\beta} - \ln\left( \sum_{j=0}^M \exp(\mathbf{x}_{kj}^T \boldsymbol{\beta}) \right) \right]$$

Maximizing $\ell_{\text{cond}}(\boldsymbol{\beta})$ yields estimators that are fully consistent, asymptotically normal, and semiparametrically efficient. For 1:1 matched pairs with a single binary exposure, conditional logistic regression reduces exactly to **McNemar’s Test** and the paired ratio $b / c$.

## 5.4 Estimating Relative Risks Directly: Log-Binomial vs Modified Poisson Regression

In prospective cohort studies, randomized clinical trials, and cross-sectional studies where the outcome is common ($P > 10\%$), the odds ratio severely exaggerates the relative risk. Clinicians and policymakers naturally interpret adjusted effect estimates as relative risks. When analysts mistakenly interpret an adjusted odds ratio of $3.5$ from a logistic model as a "3.5-fold increase in risk," they mislead clinical audiences if the true risk ratio is only $1.8$.

### The Log-Binomial Regression Model
To estimate the adjusted Relative Risk directly, we specify a Generalized Linear Model with a **log link function** applied to the binomial probability $\pi(\mathbf{x}_i) = P(Y_i = 1 \mid \mathbf{x}_i)$:

$$\ln(\pi(\mathbf{x}_i)) = \mathbf{x}_i^T \boldsymbol{\beta} \implies \pi(\mathbf{x}_i) = \exp(\mathbf{x}_i^T \boldsymbol{\beta})$$

In this model, the parameter for a binary exposure $x_1$ has a direct relative risk interpretation:

$$\frac{\pi(x_1 = 1, \mathbf{x}_{-1})}{\pi(x_1 = 0, \mathbf{x}_{-1})} = \frac{\exp(\beta_0 + \beta_1(1) + \mathbf{x}_{-1}^T \boldsymbol{\beta}_{-1})}{\exp(\beta_0 + \beta_1(0) + \mathbf{x}_{-1}^T \boldsymbol{\beta}_{-1})} = \exp(\beta_1) \equiv RR_{\text{adjusted}}$$

However, the log-binomial model suffers from a severe numerical limitation: **convergence failure**. Because probabilities must satisfy $\pi(\mathbf{x}_i) \le 1.0$, the parameter space is constrained by the boundary condition $\mathbf{x}_i^T \boldsymbol{\beta} \le 0$ for all observed covariate vectors $\mathbf{x}_i$. In multivariable settings with continuous covariates, standard Newton-Raphson optimization algorithms frequently step outside this bounded parameter space, causing standard statistical software to crash with convergence errors.

### Modified Poisson Regression with Robust Sandwich Variance
To circumvent log-binomial non-convergence, George Zou (2004) proved that an investigator can fit a **Poisson regression model** to binary data while applying a **Huber-White robust sandwich covariance estimator**.

In a Poisson model, the log link is standard: $\ln(\mu_i) = \mathbf{x}_i^T \boldsymbol{\beta}$. When applied to binary $Y_i \in \{0, 1\}$, the expectation is mathematically identical to the probability: $\mu_i = \mathbb{E}[Y_i \mid \mathbf{x}_i] = P(Y_i = 1 \mid \mathbf{x}_i) = \pi(\mathbf{x}_i)$. Thus, the exponentiated coefficients $\exp(\beta_j)$ yield consistent, unbiased estimates of the true adjusted Relative Risks!

However, fitting a Poisson model to binary data violates the mean-variance equality assumption ($\text{Var}(Y) = \mu$), because binary data have variance $\text{Var}(Y) = \pi(1 - \pi) < \pi$. The naive Poisson variance severely overestimates the true sampling variability. Zou demonstrated that applying the **Huber-White Sandwich Estimator** corrects this variance distortion:

$$\widehat{\text{Cov}}_{\text{robust}}(\widehat{\boldsymbol{\beta}}) = (\mathbf{X}^T \widehat{\mathbf{W}} \mathbf{X})^{-1} \left( \sum_{i=1}^n \mathbf{x}_i \mathbf{x}_i^T (y_i - \hat{\mu}_i)^2 \right) (\mathbf{X}^T \widehat{\mathbf{W}} \mathbf{X})^{-1}$$

Modified Poisson regression with robust standard errors is guaranteed to converge, handles continuous covariates effortlessly, and provides mathematically sound, asymptotically valid confidence intervals for adjusted Relative Risks.

## 5.5 Poisson and Negative Binomial Regression for Incidence Rates with Offsets

When the epidemiological study tracks an open dynamic population or cohort where participants accumulate varying person-time at risk ($PT_i$), the outcome of interest is the count of incident events $Y_i \in \{0, 1, 2, \dots\}$.

### Poisson Regression with Person-Time Offset
The Poisson probability mass function for event count $Y_i$ is:

$$P(Y_i = y_i) = \frac{\mu_i^{y_i} \exp(-\mu_i)}{y_i!}$$

The expected count $\mu_i$ is the product of the underlying incidence rate $\lambda(\mathbf{x}_i)$ and the accumulated person-time $PT_i$:

$$\mu_i = \lambda(\mathbf{x}_i) \times PT_i$$

Taking the natural logarithm:

$$\ln(\mu_i) = \ln(\lambda(\mathbf{x}_i)) + \ln(PT_i) = \mathbf{x}_i^T \boldsymbol{\beta} + \ln(PT_i)$$

The term $\ln(PT_i)$ is included as a regression covariate whose coefficient is pre-fixed to exactly $1.0$. In generalized linear modeling, this fixed predictor is termed an **offset**.

The exponentiated regression coefficient $\exp(\beta_1)$ for a binary exposure represents the adjusted **Incidence Rate Ratio** ($IRR$):

$$\frac{\lambda(x_1 = 1)}{\lambda(x_1 = 0)} = \frac{\exp(\beta_0 + \beta_1 + \dots)}{\exp(\beta_0 + \dots)} = \exp(\beta_1) \equiv IRR_{\text{adjusted}}$$

### Overdispersion and Negative Binomial Regression
A strict property of the Poisson distribution is **equidispersion**: the conditional variance must equal the conditional mean ($\text{Var}(Y_i \mid \mathbf{x}_i) = \mathbb{E}[Y_i \mid \mathbf{x}_i] = \mu_i$). In real-world disease surveillance, biological clustering, unobserved heterogeneity, and contagion frequently cause **overdispersion**, where the observed variance substantially exceeds the mean ($\text{Var}(Y_i) > \mu_i$).

To diagnose overdispersion, we evaluate the Pearson dispersion statistic:

$$\phi = \frac{1}{n - p} \sum_{i=1}^n \frac{(y_i - \hat{\mu}_i)^2}{\hat{\mu}_i}$$

If $\phi \gg 1.0$, standard Poisson standard errors are falsely deflated, leading to inflated Type I error rates. In such settings, epidemiologists employ the **Negative Binomial Regression Model**, which models unobserved subject heterogeneity through a gamma-distributed latent disturbance $\nu_i \sim \text{Gamma}(1/\alpha, \alpha)$. The resulting negative binomial variance is quadratic:

$$\text{Var}(Y_i \mid \mathbf{x}_i) = \mu_i + \alpha \mu_i^2$$

where $\alpha \ge 0$ is the dispersion parameter. As $\alpha \to 0$, the negative binomial model converges back to the standard Poisson model.

## 5.6 Model Building Strategies: DAGs, Change-in-Estimate, and Overadjustment Bias

A central danger in multivariable epidemiological modeling is the uncritical use of automated algorithmic variable selection (such as forward stepwise selection or backward elimination based on $p$-values). Stepwise algorithms select variables based entirely on statistical significance in the sample, completely blind to the underlying biological causal structure.

### Directed Acyclic Graph (DAG) Guided Covariate Selection
Modern epidemiologic practice mandates that covariate selection be guided by an explicit **causal DAG** formulated *a priori* from biological and clinical domain knowledge:
1. Identify all variables that satisfy Pearl's Backdoor Criterion (common causes of exposure and outcome). Include these confounders in the adjustment set.
2. **Never adjust for an intermediate variable** on the causal pathway between exposure and disease ($E \to M \to D$), unless the explicit scientific goal is to estimate the direct effect via formal mediation analysis. Adjusting for an intermediate blocks the indirect causal mechanism, biasing total effect estimates toward the null (**overadjustment bias**).
3. **Never adjust for a collider** ($E \to C \leftarrow D$), as conditioning on a collider opens a non-causal path, inducing artificial selection bias.

### The Change-in-Estimate Criterion
In empirical data modeling, an informal criterion for assessing whether a candidate covariate $Z$ acts as an active confounder is the **Change-in-Estimate Criterion**:

$$\Delta \beta = \left| \frac{\widehat{\beta}_{\text{adjusted for } Z} - \widehat{\beta}_{\text{unadjusted for } Z}}{\widehat{\beta}_{\text{adjusted for } Z}} \right|$$

If removing $Z$ alters the primary exposure effect estimate by more than $10\%$ (i.e., $\Delta \beta > 0.10$), $Z$ is retained as an essential empirical confounder regardless of its individual $p$-value.

## 5.7 Zero-Inflated and Two-Part Hurdle Models for Excess Zero Counts

In healthcare utilization studies and environmental exposure monitoring, count data often exhibit a massive excess of zero observations far beyond what even a negative binomial distribution can accommodate. For example, in an annual survey of emergency department visits or days absent from work due to acute occupational asthma, $85\%$ of healthy workers may report exactly zero events.

Epidemiologists model this phenomenon through two distinct statistical paradigms:
1. **Zero-Inflated Poisson (ZIP) and Zero-Inflated Negative Binomial (ZINB) Models**:
   Postulate that the population is a mixture of two distinct latent subpopulations: an "always-zero" immune group who cannot experience the event (with probability $p_i$), and a susceptible count group whose event frequencies follow a Poisson or negative binomial distribution:
   $$P(Y_i = 0 \mid \mathbf{x}_i) = p_i + (1 - p_i) \exp(-\mu_i)$$
   $$P(Y_i = y_i \mid \mathbf{x}_i) = (1 - p_i) \frac{\mu_i^{y_i} \exp(-\mu_i)}{y_i!}, \quad y_i \ge 1$$
   The zero probability $p_i$ is modeled via a logistic link ($\text{logit}(p_i) = \mathbf{z}_i^T \boldsymbol{\gamma}$), while the count process $\mu_i$ is modeled via a log link ($\ln(\mu_i) = \mathbf{x}_i^T \boldsymbol{\beta}$).
2. **Two-Part Hurdle Models**:
   Formulate a sequential hurdle process: first, a binary logistic model determines whether an individual crosses the hurdle from zero to at least one event ($P(Y_i > 0)$); second, conditional on crossing the hurdle ($Y_i \ge 1$), a truncated-at-zero count distribution governs event frequency. Unlike zero-inflated models, hurdle models cleanly separate the initial propensity to use healthcare from subsequent frequency of use.

## Fully worked question 1: Multivariable Binary Logistic Regression: Adjusted Odds Ratios and Likelihood Ratio Testing

### Question
A hospital-based case-control study at Dhaka Medical College Hospital investigates whether heavy tobacco smoking ($X_1 = 1$ for $\ge 20$ pack-years, $0$ otherwise) increases the risk of esophageal squamous cell carcinoma ($Y = 1$), while adjusting for chronic betel quid chewing ($X_2 = 1$ for daily use, $0$ otherwise) and age in decades above 40 ($X_3 = (\text{Age} - 40) / 10$). A multivariable binary logistic regression model fitted to data from $N = 500$ participants ($200$ cases, $300$ controls) yields the following Maximum Likelihood parameter estimates:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Parameter</th><th>Covariate Name</th><th>Estimated $\widehat{\beta}_j$</th><th>Standard Error $\text{SE}(\widehat{\beta}_j)$</th></tr>
</thead>
<tbody>
<tr><td>$\beta_0$</td><td>Intercept</td><td>$-1.850$</td><td>$0.210$</td></tr>
<tr><td>$\beta_1$</td><td>Heavy Smoking ($X_1$)</td><td>$+1.0986$</td><td>$0.2450$</td></tr>
<tr><td>$\beta_2$</td><td>Betel Quid ($X_2$)</td><td>$+0.8473$</td><td>$0.2215$</td></tr>
<tr><td>$\beta_3$</td><td>Age per Decade ($X_3$)</td><td>$+0.4055$</td><td>$0.0980$</td></tr>
</tbody>
</table></div>

The maximized log-likelihood of this full 3-covariate model is $\ell_{\text{full}} = -282.40$. When a reduced model omitting the primary exposure $X_1$ is fitted to the identical data, the maximized log-likelihood is $\ell_{\text{reduced}} = -293.15$.

1. Compute the adjusted Odds Ratios and 95% Wald confidence intervals for heavy smoking ($X_1$), betel quid chewing ($X_2$), and a 20-year increase in age ($2$ decades, $X_3$).
2. Test the null hypothesis that heavy smoking is not associated with esophageal cancer ($H_0: \beta_1 = 0$) using both the **Wald Test** and the **Likelihood Ratio Test (LRT)**.
3. For a 60-year-old individual who both smokes heavily ($X_1 = 1$) and chews betel quid ($X_2 = 1$), calculate the model-predicted probability of esophageal carcinoma, and compare it to the predicted probability for an unexposed 40-year-old individual ($X_1 = 0, X_2 = 0, X_3 = 0$).

### Solution, step 1: Adjusted odds ratios and 95% Wald confidence intervals
1. **Heavy Smoking ($X_1$)**:
   $$\widehat{OR}_1 = \exp(\widehat{\beta}_1) = \exp(1.0986) \approx 3.000$$
   $$\text{95\% CI} = \exp(1.0986 \pm 1.96 \times 0.2450) = \exp(1.0986 \pm 0.4802) = [\exp(0.6184), \, \exp(1.5788)] = [1.856, \, 4.849]$$
   After controlling for betel quid chewing and age, heavy smokers have $3.00$ times the odds of esophageal carcinoma compared to non-smokers ($95\%\text{ CI}: [1.86, \, 4.85]$).

2. **Betel Quid Chewing ($X_2$)**:
   $$\widehat{OR}_2 = \exp(\widehat{\beta}_2) = \exp(0.8473) \approx 2.333$$
   $$\text{95\% CI} = \exp(0.8473 \pm 1.96 \times 0.2215) = \exp(0.8473 \pm 0.4341) = [\exp(0.4132), \, \exp(1.2814)] = [1.512, \, 3.602]$$
   Daily betel quid chewing increases the odds of esophageal carcinoma by $2.33$ times ($95\%\text{ CI}: [1.51, \, 3.60]$).

3. **Age per 2 Decades ($20\text{ years}$, $\Delta X_3 = 2$)**:
   $$\widehat{OR}_{3, \, 20\text{ yr}} = \exp(2 \times \widehat{\beta}_3) = \exp(2 \times 0.4055) = \exp(0.8110) \approx 2.250$$
   $$\text{SE}(2 \widehat{\beta}_3) = 2 \times 0.0980 = 0.1960$$
   $$\text{95\% CI} = \exp(0.8110 \pm 1.96 \times 0.1960) = \exp(0.8110 \pm 0.3842) = [\exp(0.4268), \, \exp(1.1952)] = [1.532, \, 3.304]$$
   Each 20-year increase in age increases the odds of esophageal cancer by $2.25$ times.

### Solution, step 2: Hypothesis testing: Wald test vs Likelihood Ratio Test
1. **Wald Test**:
   The Wald test statistic for $H_0: \beta_1 = 0$ is:
   $$z_{\text{Wald}} = \frac{\widehat{\beta}_1 - 0}{\text{SE}(\widehat{\beta}_1)} = \frac{1.0986}{0.2450} \approx 4.484$$
   $$\chi^2_{\text{Wald}} = z_{\text{Wald}}^2 = (4.484)^2 \approx 20.11$$
   With 1 degree of freedom, $p = P(\chi^2_1 \ge 20.11) \approx 7.3 \times 10^{-6}$.

2. **Likelihood Ratio Test (LRT)**:
   The deviance test statistic compares maximized log-likelihoods:
   $$G^2 = 2 (\ell_{\text{full}} - \ell_{\text{reduced}}) = 2 (-282.40 - (-293.15)) = 2 (10.75) = 21.50$$
   With $df = 4 - 3 = 1$, the critical value at $\alpha = 0.001$ is $\chi^2_{0.001, 1} = 10.83$. Since $G^2 = 21.50 \gg 10.83$ ($p = 3.5 \times 10^{-6}$), the likelihood ratio test decisively confirms that heavy smoking is an independent risk factor for esophageal carcinoma.

### Solution, step 3: Model-predicted probabilities
1. **For a 60-year-old exposed individual**:
   Here, $X_1 = 1, X_2 = 1$, and $X_3 = (60 - 40) / 10 = 2.0$.
   The linear predictor is:
   $$\eta = -1.850 + 1.0986(1) + 0.8473(1) + 0.4055(2.0) = -1.850 + 1.0986 + 0.8473 + 0.8110 = +0.9069$$
   The predicted probability of disease is:
   $$\pi(60, \text{exp}) = \frac{\exp(0.9069)}{1 + \exp(0.9069)} = \frac{2.4766}{3.4766} \approx 0.7124 \quad (71.24\%)$$

2. **For an unexposed 40-year-old individual**:
   Here, $X_1 = 0, X_2 = 0$, and $X_3 = (40 - 40) / 10 = 0.0$.
   $$\eta = -1.850 + 0 + 0 + 0 = -1.850$$
   $$\pi(40, \text{unexp}) = \frac{\exp(-1.850)}{1 + \exp(-1.850)} = \frac{0.1572}{1.1572} \approx 0.1359 \quad (13.59\%)$$

The model predicts that a 60-year-old heavy smoker who chews betel quid faces a $71.24\%$ disease probability, compared to $13.59\%$ for a baseline unexposed 40-year-old individual.

## Fully worked question 2: Modified Poisson Regression with Robust Error Variance for Common Binary Outcomes

### Question
An institutional obstetrics cohort study investigates whether severe gestational maternal anemia ($X_1 = 1$, hemoglobin $< 8.0 \text{ g/dL}$) increases the risk of preterm delivery ($Y = 1$, birth before 37 completed weeks) among $N = 2,500$ pregnant women. Preterm delivery is common in this tertiary hospital population, occurring in $450$ births ($18.0\%$). An investigator initially attempts to fit a log-binomial regression model adjusting for maternal age ($X_2$), pre-pregnancy hypertension ($X_3$), and parity ($X_4$), but the software terminates with the error: `"Log-binomial model failed to converge: linear predictor out of bounds"`.

The investigator switches to **Modified Poisson Regression with Huber-White Robust Error Variance**:
- Model specification: $\ln(P(Y_i = 1 \mid \mathbf{X}_i)) = \beta_0 + \beta_1 X_{i1} + \beta_2 X_{i2} + \beta_3 X_{i3} + \beta_4 X_{i4}$.
- The estimated coefficient for severe anemia is $\widehat{\beta}_1 = +0.5596$.
- The naive model-based standard error from standard Poisson software is $\text{SE}_{\text{naive}}(\widehat{\beta}_1) = 0.0820$.
- The Huber-White robust sandwich standard error is $\text{SE}_{\text{robust}}(\widehat{\beta}_1) = 0.1150$.
- For comparison, a standard multivariable binary logistic regression model fitted to the exact same dataset yields $\widehat{\beta}_{1, \text{logistic}} = +0.7885$ with $\text{SE}(\widehat{\beta}_{1, \text{logistic}}) = 0.1280$.

1. Explain the mathematical cause of the convergence failure in the log-binomial model, and demonstrate why Modified Poisson regression provides valid point estimates of the Relative Risk.
2. Calculate the adjusted Risk Ratio ($RR_{\text{adjusted}}$) and its 95% confidence interval using the robust sandwich standard error. Compare this against the naive Poisson confidence interval and explain why the robust adjustment is mathematically mandatory.
3. Calculate the adjusted Odds Ratio ($OR_{\text{adjusted}}$) from the logistic regression model. Demonstrate how the Odds Ratio substantially overstates the true Relative Risk due to the high baseline prevalence ($18\%$) of preterm birth.

### Solution, step 1: Mechanics of log-binomial convergence failure and Poisson equivalence
In log-binomial regression, the model enforces $\pi(\mathbf{x}_i) = \exp(\mathbf{x}_i^T \boldsymbol{\beta})$. Because probabilities cannot exceed $1.0$, the parameter space is strictly constrained by the linear inequality:

$$\mathbf{x}_i^T \boldsymbol{\beta} \le 0 \quad \forall i = 1, \dots, n$$

When covariates include continuous variables or multiple severe binary risk factors, the unconstrained Newton-Raphson update step attempts to evaluate likelihood gradients where $\mathbf{x}_i^T \boldsymbol{\beta} > 0 \implies \pi(\mathbf{x}_i) > 1.0$. Because $\ln(1 - \pi)$ is undefined for $\pi > 1$, the optimization algorithm immediately crashes.

By contrast, the Poisson likelihood does not contain a $1 - \pi$ term; its log-likelihood is:
$$\ell_{\text{Poisson}}(\boldsymbol{\beta}) = \sum_{i=1}^n [y_i \mathbf{x}_i^T \boldsymbol{\beta} - \exp(\mathbf{x}_i^T \boldsymbol{\beta}) - \ln(y_i!)]$$
Because $\exp(\mathbf{x}_i^T \boldsymbol{\beta})$ is infinitely differentiable and real-valued for all $\mathbf{x}_i^T \boldsymbol{\beta} \in (-\infty, \infty)$, the Poisson log-likelihood surface is strictly concave everywhere, guaranteeing rapid, unconditional convergence. Furthermore, the first-order score equation is:
$$\frac{\partial \ell}{\partial \boldsymbol{\beta}} = \sum_{i=1}^n (y_i - \exp(\mathbf{x}_i^T \boldsymbol{\beta})) \mathbf{x}_i = \mathbf{0}$$
Since $\mathbb{E}[Y_i \mid \mathbf{x}_i] = \pi(\mathbf{x}_i)$, the score equations are unbiased estimating equations. By the theory of Quasi-Maximum Likelihood, $\widehat{\boldsymbol{\beta}}$ is a consistent and asymptotically normal estimator of the true log-relative risk parameters.

### Solution, step 2: Adjusted Risk Ratio and robust vs naive confidence intervals
The adjusted Relative Risk is:
$$\widehat{RR}_{\text{adjusted}} = \exp(\widehat{\beta}_1) = \exp(0.5596) \approx 1.7500 \approx 1.75$$
Severe gestational anemia increases the adjusted risk of preterm delivery by $75.0\%$.

1. **Using the Robust Sandwich Standard Error ($\text{SE}_{\text{robust}} = 0.1150$)**:
   $$\text{95\% CI}_{\text{robust}} = \exp(0.5596 \pm 1.96 \times 0.1150) = \exp(0.5596 \pm 0.2254) = [\exp(0.3342), \, \exp(0.7850)] = [1.397, \, 2.192]$$
   $$\text{95\% CI}_{\text{robust}} = [1.40, \, 2.19]$$

2. **Using the Naive Poisson Standard Error ($\text{SE}_{\text{naive}} = 0.0820$)**:
   $$\text{95\% CI}_{\text{naive}} = \exp(0.5596 \pm 1.96 \times 0.0820) = \exp(0.5596 \pm 0.1607) = [\exp(0.3989), \, \exp(0.7203)] = [1.490, \, 2.055]$$

**Why Robust Adjustment is Mandatory**:
Under the Poisson model, the variance is assumed to equal the mean ($\mu_i$). However, binary data have variance $\pi_i(1 - \pi_i)$. The ratio of true variance to Poisson assumed variance is:
$$\frac{\text{Var}(Y_i)}{\text{Assumed Var}} = \frac{\pi_i(1 - \pi_i)}{\pi_i} = 1 - \pi_i < 1.0$$
Because the Poisson model mis-specifies the variance structure, the naive model-based standard error is incorrect. The Huber-White sandwich estimator uses the empirical squared residuals $(y_i - \hat{\mu}_i)^2$ to evaluate true sampling variability, producing asymptotically exact coverage.

### Solution, step 3: Comparison with logistic regression odds ratio
From the logistic model:
$$\widehat{OR}_{\text{adjusted}} = \exp(\widehat{\beta}_{1, \text{logistic}}) = \exp(0.7885) \approx 2.200$$
$$\text{95\% CI}_{\text{logistic}} = \exp(0.7885 \pm 1.96 \times 0.1280) = \exp(0.7885 \pm 0.2509) = [\exp(0.5376), \, \exp(1.0394)] = [1.712, \, 2.828]$$

**Clinical Comparison**:
The multivariable logistic regression model reports an adjusted Odds Ratio of $2.20$ ($120\%$ increase in odds). However, the true adjusted Relative Risk from the modified Poisson model is only $1.75$ ($75\%$ increase in risk).
Because preterm delivery is a common outcome ($18.0\%$), the Odds Ratio dramatically overstates the true risk ratio by $25.7\%$ ($2.20 / 1.75 = 1.257$). If an investigator reported the $OR = 2.20$ as a "risk ratio" to clinical obstetricians, it would seriously distort clinical perception of drug or exposure effect magnitude.

## Fully worked question 3: Poisson Regression with Person-Time Offsets and Overdispersion Testing

### Question
An open occupational cohort study at an industrial chemical processing facility in Chittagong tracks $N = 4,000$ chemical workers over a 10-year observation period to evaluate whether chronic inhalation of sulfur dioxide ($\text{SO}_2$) gas increases the incidence of severe acute bronchitis episodes. Workers accumulate varying person-years ($PT_i$) of observation due to staggered hiring dates and job transitions. The workers are grouped into $k = 4$ occupational exposure categories. The recorded person-time, total bronchitis events, and covariate summary are:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Exposure Group ($j$)</th><th>$\text{SO}_2$ Level</th><th>Person-Years ($PT_j$)</th><th>Bronchitis Events ($Y_j$)</th><th>Crude Rate per 1,000 PY</th></tr>
</thead>
<tbody>
<tr><td>Group 0 (Reference)</td><td>Unexposed (Office)</td><td>12,000</td><td>120</td><td>10.00</td></tr>
<tr><td>Group 1</td><td>Low ($\le 2.0\text{ ppm}$)</td><td>10,000</td><td>150</td><td>15.00</td></tr>
<tr><td>Group 2</td><td>Moderate ($2.1–5.0\text{ ppm}$)</td><td>8,000</td><td>192</td><td>24.00</td></tr>
<tr><td>Group 3</td><td>High ($> 5.0\text{ ppm}$)</td><td>5,000</td><td>200</td><td>40.00</td></tr>
</tbody>
</table></div>

A multivariable Poisson rate regression model with an offset $\ln(PT_j)$ and adjustment for smoking status ($X_{\text{smoke}} = 1$ for smoker, $0$ for non-smoker) is fitted:
$$\ln(\mathbb{E}[Y_j]) = \ln(PT_j) + \beta_0 + \beta_1 X_{j1} + \beta_2 X_{j2} + \beta_3 X_{j3} + \beta_{\text{smoke}} X_{\text{smoke}}$$
where $X_{j1}, X_{j2}, X_{j3}$ are indicator variables for Low, Moderate, and High $\text{SO}_2$ exposure. The estimated coefficients are:
- Intercept: $\widehat{\beta}_0 = -4.6052$
- Low $\text{SO}_2$ ($X_1$): $\widehat{\beta}_1 = +0.3365, \quad \text{SE}(\widehat{\beta}_1) = 0.1150$
- Moderate $\text{SO}_2$ ($X_2$): $\widehat{\beta}_2 = +0.7885, \quad \text{SE}(\widehat{\beta}_2) = 0.1080$
- High $\text{SO}_2$ ($X_3$): $\widehat{\beta}_3 = +1.2528, \quad \text{SE}(\widehat{\beta}_3) = 0.1120$
- Smoking ($X_{\text{smoke}}$): $\widehat{\beta}_{\text{smoke}} = +0.4055, \quad \text{SE} = 0.0850$

1. Explain the role of the offset term $\ln(PT_j)$ in Poisson regression.
2. Compute the adjusted Incidence Rate Ratios ($IRR$) and 95% confidence intervals for Low, Moderate, and High $\text{SO}_2$ exposure relative to unexposed workers, adjusting for smoking.
3. Across the entire cohort of individual records ($n = 4,000$), the residual deviance of the fitted Poisson model is $D = 4,785.0$ on $3,995$ degrees of freedom. Calculate the Pearson dispersion parameter $\hat{\phi}$, test for the presence of overdispersion, and describe how overdispersion affects statistical inferences if not corrected.

### Solution, step 1: Role of the offset term in Poisson rate regression
The Poisson distribution models non-negative integer event counts $Y_j \sim \text{Poisson}(\mu_j)$. In longitudinal epidemiology, the expected count $\mu_j$ is proportional to the person-time at risk:
$$\mu_j = \lambda_j \times PT_j$$
Taking logarithms:
$$\ln(\mu_j) = \ln(\lambda_j) + \ln(PT_j) = \mathbf{x}_j^T \boldsymbol{\beta} + \ln(PT_j)$$
The term $\ln(PT_j)$ enters the linear predictor with a regression coefficient strictly constrained to $+1.0$. This allows the model to estimate the **rate** $\lambda_j = \mu_j / PT_j$ rather than the absolute count $\mu_j$, directly accommodating unequal follow-up durations across participants without converting rates into crude proportions.

### Solution, step 2: Adjusted Incidence Rate Ratios and 95% confidence intervals
The adjusted Incidence Rate Ratio for exposure level $k$ is $IRR_k = \exp(\widehat{\beta}_k)$:

1. **Low $\text{SO}_2$ Exposure ($X_1$)**:
   $$\widehat{IRR}_1 = \exp(0.3365) \approx 1.400$$
   $$\text{95\% CI} = \exp(0.3365 \pm 1.96 \times 0.1150) = \exp(0.3365 \pm 0.2254) = [\exp(0.1111), \, \exp(0.5619)] = [1.117, \, 1.754]$$
   Low $\text{SO}_2$ exposure increases the rate of acute bronchitis by $40.0\%$ ($95\%\text{ CI}: [1.12, \, 1.75]$).

2. **Moderate $\text{SO}_2$ Exposure ($X_2$)**:
   $$\widehat{IRR}_2 = \exp(0.7885) \approx 2.200$$
   $$\text{95\% CI} = \exp(0.7885 \pm 1.96 \times 0.1080) = \exp(0.7885 \pm 0.2117) = [\exp(0.5768), \, \exp(1.0002)] = [1.780, \, 2.719]$$
   Moderate $\text{SO}_2$ exposure increases bronchitis incidence by $2.20$ times ($95\%\text{ CI}: [1.78, \, 2.72]$).

3. **High $\text{SO}_2$ Exposure ($X_3$)**:
   $$\widehat{IRR}_3 = \exp(1.2528) \approx 3.500$$
   $$\text{95\% CI} = \exp(1.2528 \pm 1.96 \times 0.1120) = \exp(1.2528 \pm 0.2195) = [\exp(1.0333), \, \exp(1.4723)] = [2.810, \, 4.359]$$
   High $\text{SO}_2$ exposure increases the incidence rate of bronchitis by $3.50$ times ($95\%\text{ CI}: [2.81, \, 4.36]$).

Notice the striking monotonic biological dose-response gradient: $IRR$ rises from $1.40 \to 2.20 \to 3.50$ as $\text{SO}_2$ concentrations escalate.

### Solution, step 3: Overdispersion evaluation and methodological implications
The dispersion parameter $\hat{\phi}$ is estimated from the residual deviance $D$ and residual degrees of freedom:

$$\hat{\phi} = \frac{D}{df} = \frac{4,785.0}{3,995} \approx 1.1977 \approx 1.20$$

Under the null hypothesis of pure Poisson equidispersion ($\phi = 1.0$), the deviance asymptotically follows a chi-square distribution with $df = 3,995$. We evaluate the standard normal test statistic:

$$z = \frac{D - df}{\sqrt{2 \cdot df}} = \frac{4,785.0 - 3,995}{\sqrt{2 \times 3,995}} = \frac{790.0}{\sqrt{7,990}} = \frac{790.0}{89.387} \approx 8.838$$

Because $z = 8.84 \gg 3.29$ ($p < 10^{-18}$), the null hypothesis of equidispersion is decisively rejected: statistically significant **overdispersion** is present ($\phi = 1.20$).

**Implications of Uncorrected Overdispersion**:
In standard Poisson regression, the covariance matrix of $\widehat{\boldsymbol{\beta}}$ assumes $\phi = 1.0$. When overdispersion is ignored:
1. True standard errors are understated by a factor of $\sqrt{\hat{\phi}} = \sqrt{1.1977} \approx 1.0944$ (nearly $10\%$ too narrow).
2. Test statistics (such as Wald $z$-scores) are artificially inflated by $9.4\%$.
3. $p$-values are falsely small, inflating the nominal Type I error rate above $\alpha = 0.05$.

To correct for this overdispersion, the analyst must either multiply all standard errors by $\sqrt{\hat{\phi}} = 1.0944$ (quasi-Poisson model) or refit the data using a **Negative Binomial Regression Model**, ensuring rigorous, conservative public health conclusions.
