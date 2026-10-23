#!/usr/bin/env python3
"""
Generate Units 5 and 6 of Epidemiological Statistics with high academic depth.
"""
from pathlib import Path

OUT_DIR = Path("publishing/drafts/statistics-probability-epidemiological-statistics")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# UNIT 5
# -------------------------------------------------------------
unit5 = r"""# Unit 5: Multivariable Regression in Epidemiology: Logistic, Conditional Logistic, Log-Binomial & Poisson Models

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
"""

# -------------------------------------------------------------
# UNIT 6
# -------------------------------------------------------------
unit6 = r"""# Unit 6: Screening, Diagnostic Testing & Receiver Operating Characteristic (ROC) Analysis

In public health and clinical medicine, the early detection of disease among asymptomatic individuals through population screening offers the promise of secondary prevention: halting pathologic progression before irreversible biological damage or metastatic dissemination occurs. However, no diagnostic or screening test is biologically infallible. Imperfect tests produce false positives that induce psychological distress and unnecessary invasive procedures, as well as false negatives that foster dangerous complacency. To establish the clinical validity of a diagnostic technology, epidemiologists employ formal quantitative criteria. In this unit, we formalize the natural history of disease and the Wilson-Jungner screening criteria, establish the fundamental $2 \times 2$ diagnostic matrix (sensitivity, specificity, false positive and false negative rates), demonstrate the mathematical dominance of disease prevalence over positive predictive values, formulate Bayesian clinical reasoning using diagnostic likelihood ratios and the Fagan nomogram, construct continuous Receiver Operating Characteristic (ROC) curves, prove the mathematical equivalence between the Area Under the Curve (AUC) and the Wilcoxon-Mann-Whitney statistic, evaluate Youden’s $J$ cutpoint optimization, and analyze the methodological biases that distort screening evaluations (lead-time bias, length-biased sampling, and overdiagnosis).

## 6.1 Principles of Secondary Prevention, Natural History & The Wilson-Jungner Criteria

Screening is defined as the presumptive identification of unrecognized disease or defect by the application of tests, examinations, or other procedures that can be applied rapidly to asymptomatic target populations. Screening sorts out apparently well persons who probably have a disease from those who probably do not.

### Natural History of Disease and the Critical Window
The biological trajectory of disease unfolds across distinct phases:
1. **Stage of Susceptibility**: Biological exposure has occurred, but pathologic alterations have not yet initiated.
2. **Pre-symptomatic (Subclinical) Phase**: Pathologic changes have initiated, but the disease remains entirely asymptomatic. Within this phase lies the **Detectably Pre-clinical Phase (DPCP)**: the window of time beginning when the disease first becomes detectable by an objective screening biomarker ($t_d$) and ending when clinical symptoms naturally emerge ($t_s$).
3. **Clinical Phase**: Symptoms manifest, prompting clinical diagnosis and therapy.

For a screening program to be medically effective, there must exist a **critical point** located within the DPCP: an inflection point before which therapeutic intervention confers substantially greater survival or functional recovery than treatment delayed until clinical symptom onset. If the critical point occurs before the screening test can detect the lesion (e.g., highly aggressive pancreatic adenocarcinoma), or if therapy is equally effective whenever applied, screening confers zero mortality benefit.

### The Wilson-Jungner Screening Criteria
In 1968, James Maxwell Glover Wilson and Gunnar Jungner established the foundational ten principles of screening for the World Health Organization:
1. The condition sought should be an important health problem for the individual and community.
2. There should be an accepted treatment for patients with recognized disease.
3. Facilities for diagnosis and treatment should be available.
4. There should be a recognizable latent or early symptomatic stage.
5. There should be a suitable test or examination.
6. The test should be acceptable to the general population.
7. The natural history of the condition, including development from latent to declared disease, should be adequately understood.
8. There should be an agreed policy on whom to treat as patients.
9. The cost of case-finding (including diagnosis and subsequent treatment) should be economically balanced in relation to possible total expenditure on medical care.
10. Case-finding should be a continuous process and not a "once and for all" project.

## 6.2 The Fundamental Diagnostic Matrix: Sensitivity, Specificity, and Error Rates

To evaluate the intrinsic diagnostic accuracy of a binary screening test, test results are cross-tabulated against an independent **Gold Standard** (the definitive diagnostic criterion, such as tissue biopsy, surgical histopathology, or necropsy):

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Screening Test Result</th><th>True Disease Present ($D^+$)</th><th>True Disease Absent ($D^-$)</th><th>Total Tested</th></tr>
</thead>
<tbody>
<tr><td><strong>Test Positive ($T^+$)</strong></td><td>$TP$ (True Positive)</td><td>$FP$ (False Positive)</td><td>$n_{\text{test}+} = TP + FP$</td></tr>
<tr><td><strong>Test Negative ($T^-$)</strong></td><td>$FN$ (False Negative)</td><td>$TN$ (True Negative)</td><td>$n_{\text{test}-} = FN + TN$</td></tr>
<tr><td><strong>Total Reference</strong></td><td>$N_D = TP + FN$</td><td>$N_H = FP + TN$</td><td>$N = TP + FP + FN + TN$</td></tr>
</tbody>
</table></div>

### Sensitivity (True Positive Rate)
**Sensitivity** ($Se$), or the **True Positive Rate** ($TPR$), is the conditional probability that a truly diseased individual tests positive:

$$Se = P(T^+ \mid D^+) = \frac{TP}{TP + FN} = \frac{TP}{N_D}$$

A test with $Se = 0.95$ correctly detects $95\%$ of diseased individuals, while missing $5\%$ ($FN = 5\%$). The complementary probability is the **False Negative Rate** ($FNR = 1 - Se$). High-sensitivity tests are prized for "ruling out" disease (the clinical mnemonic **SnNOut**: High **S**e**n**sitivity, **N**egative test rules **Out** disease).

### Specificity (True Negative Rate)
**Specificity** ($Sp$), or the **True Negative Rate** ($TNR$), is the conditional probability that a truly healthy individual tests negative:

$$Sp = P(T^- \mid D^-) = \frac{TN}{FP + TN} = \frac{TN}{N_H}$$

A test with $Sp = 0.98$ correctly clears $98\%$ of healthy individuals, while incorrectly flagging $2\%$ as false alarms. The complementary probability is the **False Positive Rate** ($FPR = 1 - Sp$). High-specificity tests are prized for "ruling in" disease (the clinical mnemonic **SpPIn**: High **Sp**ecificity, **P**ositive test rules **In** disease).

Crucially, **sensitivity and specificity are intrinsic properties of the diagnostic test technology**: within a defined patient population, they remain mathematically constant regardless of how common or rare the disease is in the community.

## 6.3 Positive and Negative Predictive Values: The Mathematical Dominance of Prevalence

While clinicians evaluate test technology using sensitivity and specificity, the patient who receives a positive test result asks a fundamentally different question: *"Given that my test is positive, what is the actual probability that I truly have the disease?"*

This clinical question is answered by the **predictive values**.

### Positive Predictive Value (PPV)
The **Positive Predictive Value** ($PPV$), or post-test probability of disease following a positive result, is the conditional probability that an individual who tests positive is truly diseased:

$$PPV = P(D^+ \mid T^+) = \frac{TP}{TP + FP}$$

Applying **Bayes' Theorem** decomposes the $PPV$ into the test's operating characteristics and the pre-test disease **prevalence** ($\pi = P(D^+)$):

$$PPV = \frac{P(T^+ \mid D^+) P(D^+)}{P(T^+ \mid D^+) P(D^+) + P(T^+ \mid D^-) P(D^-)} = \frac{Se \cdot \pi}{Se \cdot \pi + (1 - Sp) \cdot (1 - \pi)}$$

### Negative Predictive Value (NPV)
The **Negative Predictive Value** ($NPV$), or post-test probability of health following a negative result, is the conditional probability that an individual who tests negative is truly free of disease:

$$NPV = P(D^- \mid T^-) = \frac{TN}{FN + TN} = \frac{Sp \cdot (1 - \pi)}{(1 - Se) \cdot \pi + Sp \cdot (1 - \pi)}$$

### The Paradox of Rare Disease Screening
Notice the critical algebraic feature of Bayes' formula: **Predictive values are profoundly dependent upon disease prevalence ($\pi$)**.
Even for a test with extraordinary analytical accuracy (e.g., $Se = 99\%$ and $Sp = 99\%$), if the disease is rare in the general screening population ($\pi = 1 / 1,000 = 0.001$), the positive predictive value collapses:

$$PPV = \frac{(0.99)(0.001)}{(0.99)(0.001) + (1 - 0.99)(1 - 0.001)} = \frac{0.00099}{0.00099 + (0.01)(0.999)} = \frac{0.00099}{0.00099 + 0.00999} = \frac{0.00099}{0.01098} \approx 0.0902 \quad (9.02\%)$$

Out of every 100 positive test results, **more than 90 are false positives!** This mathematical reality explains why universal population screening for low-prevalence cancers or rare conditions is counter-productive: the massive flood of false-positive results causes severe patient trauma and overwhelms diagnostic healthcare resources with unnecessary invasive biopsies.

## 6.4 Likelihood Ratios, Diagnostic Odds Ratios & The Bayesian Fagan Nomogram

To overcome the prevalence-dependence of predictive values while maintaining clinically actionable intuition, modern evidence-based medicine utilizes **Likelihood Ratios** ($LR$).

### Positive Likelihood Ratio (LR+)
The **Positive Likelihood Ratio** is the ratio of the probability of a positive test in a diseased person to the probability of a positive test in a non-diseased person:

$$LR^+ = \frac{P(T^+ \mid D^+)}{P(T^+ \mid D^-)} = \frac{Se}{1 - Sp} = \frac{\text{True Positive Rate}}{\text{False Positive Rate}}$$

- $LR^+ = 1.0$: Diagnostic test provides zero information; post-test probability equals pre-test probability.
- $LR^+ > 10.0$: Strong diagnostic evidence; highly effective at ruling in disease.
- $LR^+ \in (5, 10)$: Moderate diagnostic evidence.

### Negative Likelihood Ratio (LR-)
The **Negative Likelihood Ratio** is the ratio of the probability of a negative test in a diseased person to the probability of a negative test in a non-diseased person:

$$LR^- = \frac{P(T^- \mid D^+)}{P(T^- \mid D^-)} = \frac{1 - Se}{Sp} = \frac{\text{False Negative Rate}}{\text{True Negative Rate}}$$

- $LR^- < 0.1$: Strong diagnostic evidence; highly effective at ruling out disease.
- $LR^- \in (0.1, 0.2)$: Moderate diagnostic evidence.

### The Odds Form of Bayes' Theorem and the Fagan Nomogram
Recall that odds is defined as $\text{Odds} = p / (1 - p)$. The **Pre-test Odds** of disease is:

$$\text{Pre-test Odds} = \frac{\pi}{1 - \pi}$$

By Bayes' theorem, multiplying the pre-test odds by the likelihood ratio directly yields the **Post-test Odds**:

$$\text{Post-test Odds}(D^+ \mid T^+) = \text{Pre-test Odds} \times LR^+$$

$$\text{Post-test Odds}(D^+ \mid T^-) = \text{Pre-test Odds} \times LR^-$$

Once the post-test odds are obtained, the post-test probability ($PPV$ or $1 - NPV$) is recovered via:

$$\text{Post-test Probability} = \frac{\text{Post-test Odds}}{1 + \text{Post-test Odds}}$$

In clinical practice, this Bayesian updating is executed instantly using the **Fagan Nomogram**: a graphical three-axis alignment chart linking pre-test probability on the left, likelihood ratio in the center, and post-test probability on the right with a straight line.

### Diagnostic Odds Ratio (DOR)
The overall diagnostic performance of a test is summarized by the **Diagnostic Odds Ratio** ($DOR$):

$$DOR = \frac{LR^+}{LR^-} = \frac{Se / (1 - Sp)}{(1 - Se) / Sp} = \frac{Se \cdot Sp}{(1 - Se)(1 - Sp)} = \frac{TP \cdot TN}{FP \cdot FN}$$

A diagnostic test with $DOR = 1.0$ has zero discriminatory capacity; values exceeding $100$ indicate excellent diagnostic separation.

## 6.5 Continuous Biomarkers and Receiver Operating Characteristic (ROC) Analysis

Many modern diagnostic tests do not generate binary positive/negative outcomes; instead, they output continuous quantitative biomarkers (e.g., serum Prostate-Specific Antigen in $\text{ng/mL}$, fasting blood glucose in $\text{mg/dL}$, or coronary artery calcium scores). To classify an individual as "diseased," the clinician must designate a **decision cutoff threshold** $c$.

Let $X$ denote the continuous test score. By convention, higher biomarker values indicate greater likelihood of disease:
$$\text{Classify } T^+ \text{ if } X \ge c, \qquad \text{Classify } T^- \text{ if } X < c$$

Let $f_D(x)$ and $f_H(x)$ denote the probability density functions of the biomarker in the diseased and healthy populations, respectively. For any designated cutoff $c$:

$$Se(c) = P(X \ge c \mid D^+) = \int_c^\infty f_D(x) \, dx$$

$$Sp(c) = P(X < c \mid D^-) = \int_{-\infty}^c f_H(x) \, dx \implies FPR(c) = 1 - Sp(c) = \int_c^\infty f_H(x) \, dx$$

As the cutoff $c$ shifts:
- If $c \to -\infty$: Every patient is classified positive $\implies Se \to 1.0$, but $Sp \to 0.0$ ($FPR \to 1.0$).
- If $c \to +\infty$: Every patient is classified negative $\implies Se \to 0.0$, but $Sp \to 1.0$ ($FPR \to 0.0$).

### Construction of the ROC Curve
Originated in electrical radar signal detection during World War II, the **Receiver Operating Characteristic (ROC) Curve** is a graphical plot of the **True Positive Rate** ($Se(c)$) on the vertical $y$-axis versus the **False Positive Rate** ($1 - Sp(c)$) on the horizontal $x$-axis, traced continuously as the decision cutoff $c$ varies from $+\infty$ to $-\infty$.

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>ROC Graphic Feature</th><th>Mathematical Meaning</th><th>Epidemiological Interpretation</th></tr>
</thead>
<tbody>
<tr><td><strong>Point $(0, 0)$</strong></td><td>$c = +\infty$: Classify all as negative.</td><td>Zero false alarms, but misses every true case ($Se = 0, Sp = 1$).</td></tr>
<tr><td><strong>Point $(1, 1)$</strong></td><td>$c = -\infty$: Classify all as positive.</td><td>Catches every case, but falsely flags every healthy person ($Se = 1, Sp = 0$).</td></tr>
<tr><td><strong>Point $(0, 1)$</strong></td><td>Ideal diagnostic perfection.</td><td>$100\%$ Sensitivity and $100\%$ Specificity (zero error).</td></tr>
<tr><td><strong>45-Degree Diagonal Line</strong></td><td>$Se(c) = FPR(c)$ for all $c$.</td><td>The test performs no better than random guessing (flipping an unweighted coin).</td></tr>
</tbody>
</table></div>

## 6.6 Area Under the Curve (AUC), Youden's J, and Screening Evaluation Biases

### The Area Under the Curve (AUC / c-statistic)
The global discriminatory accuracy of a continuous diagnostic test is quantified by the **Area Under the ROC Curve** ($AUC$), also known as the **concordance index** ($c$-statistic):

$$AUC = \int_0^1 Se(FPR) \, d(FPR) = \int_{-\infty}^\infty Se(c) \left| \frac{d(1 - Sp(c))}{dc} \right| dc$$

The $AUC$ spans the interval $[0.5, 1.0]$:
- $AUC = 0.50$: Pure chance; zero diagnostic discrimination.
- $AUC \in [0.70, 0.80)$: Acceptable discrimination.
- $AUC \in [0.80, 0.90)$: Excellent discrimination.
- $AUC \ge 0.90$: Outstanding diagnostic accuracy ($AUC = 1.0$ is perfect separation).

### Probabilistic Equivalence to the Wilcoxon-Mann-Whitney Statistic
A celebrated mathematical theorem established by David Green and John Swets (1966) and popularized by James Hanley and Barbara McNeil (1982) proves that the **AUC is mathematically identical to the Wilcoxon-Mann-Whitney U-statistic probability**:

$$AUC = P(X_D > X_H)$$

where $X_D$ is the biomarker score of a randomly chosen diseased individual and $X_H$ is the biomarker score of a randomly chosen healthy individual. Thus, an $AUC$ of $0.85$ means that if one diseased patient and one healthy patient are selected at random, there is an $85\%$ probability that the diseased patient will exhibit a higher biomarker concentration than the healthy patient!

For empirical sample data with $n_D$ cases and $n_H$ controls, the non-parametric trapezoidal $AUC$ is:

$$\widehat{AUC} = \frac{1}{n_D n_H} \sum_{i=1}^{n_D} \sum_{j=1}^{n_H} I(X_{Di} > X_{Hj}) + 0.5 \cdot I(X_{Di} = X_{Hj})$$

### Cutpoint Optimization: Youden's J Statistic
To choose the single "optimal" clinical cutoff threshold $c^*$ that maximizes diagnostic efficacy, William J. Youden (1950) introduced **Youden’s Index** ($J$):

$$J(c) = Se(c) + Sp(c) - 1 = Se(c) - FPR(c)$$

Geometrically, $J(c)$ represents the vertical distance between the ROC curve and the 45-degree chance diagonal at cutoff $c$. The optimal cutoff $c^*$ is the point that maximizes $J(c)$:

$$c^* = \arg\max_c [Se(c) + Sp(c) - 1]$$

### Methodological Biases in Screening Program Evaluation
Evaluating whether a screening program successfully reduces population mortality requires randomized clinical trials with mortality endpoints, because observational comparisons of screened vs unscreened patients are distorted by three insidious survival biases:

1. **Lead-Time Bias**:
   **Lead time** is the duration by which screening advances the date of diagnosis compared to standard clinical symptom presentation. Even if screening and early therapy have zero biological effect on the ultimate date of death, screened patients will survive longer *from the date of diagnosis* purely because their diagnosis was established earlier in time! Comparing 5-year survival rates between screened and unscreened cases creates an illusion of therapeutic benefit caused entirely by clock-resetting.
2. **Length-Biased Sampling (Prognostic Selection)**:
   Screening tests administered at periodic intervals preferentially detect slow-growing, indolent, biologically indolent tumors that spend years in the Detectably Pre-clinical Phase. Highly aggressive, fast-growing malignancies pass rapidly through the DPCP between screening rounds and emerge as symptomatic "interval cancers." Consequently, screened cases have inherently superior biological prognoses, creating false impressions of screening efficacy.
3. **Overdiagnosis Bias**:
   **Overdiagnosis** is the detection of subclinical pseudodisease: microscopic, histologically abnormal lesions that would never have progressed to cause clinical symptoms, impairment, or death during the patient’s natural lifetime (e.g., indolent thyroid papillary microcarcinomas, low-grade prostate cancer, ductal carcinoma in situ). Overdiagnosed patients undergo toxic surgeries and chemotherapy with zero possibility of clinical benefit, while artificially inflating survival statistics.

## Fully worked question 1: Bayesian Clinical Diagnosis: Sensitivity, Specificity, Predictive Values, and Fagan Nomogram

### Question
A specialized clinical serology laboratory evaluates a fourth-generation Chemiluminescent Immunoassay (CLIA) for detecting Hepatitis C Virus (HCV) antibodies. Validation against viral RNA PCR gold standard in an analytical laboratory study demonstrates:
- Sensitivity: $Se = 0.980$ ($98.0\%$).
- Specificity: $Sp = 0.995$ ($99.5\%$).

The immunoassay is deployed in two vastly different clinical settings:
- **Setting A (High-Risk Needle-Exchange Addiction Clinic)**: HCV infection prevalence is $\pi_A = 0.200$ ($20.0\%$).
- **Setting B (Low-Risk General Asymptomatic Blood Donor Screening)**: HCV infection prevalence is $\pi_B = 0.001$ ($0.1\%$, 1 per 1,000 donors).

1. For both Setting A and Setting B, calculate the Positive Predictive Value ($PPV$) and the Negative Predictive Value ($NPV$).
2. Compute the Positive Likelihood Ratio ($LR^+$) and Negative Likelihood Ratio ($LR^-$).
3. Using the odds formulation of Bayes' theorem, demonstrate how the pre-test odds in Setting B are updated by $LR^+$ to yield the post-test odds, and show that this matches the $PPV$ computed via Bayes' theorem. What are the clinical and ethical implications for blood donor notification?

### Solution, step 1: Calculate PPV and NPV for Setting A and Setting B
1. **Setting A (High-Risk Clinic, $\pi_A = 0.20$)**:
   Apply Bayes' Theorem:
   $$PPV_A = \frac{Se \cdot \pi_A}{Se \cdot \pi_A + (1 - Sp)(1 - \pi_A)} = \frac{(0.980)(0.200)}{(0.980)(0.200) + (1 - 0.995)(1 - 0.200)}$$
   $$= \frac{0.1960}{0.1960 + (0.005)(0.800)} = \frac{0.1960}{0.1960 + 0.0040} = \frac{0.1960}{0.2000} = 0.9800 \quad (98.00\%)$$

   $$NPV_A = \frac{Sp \cdot (1 - \pi_A)}{(1 - Se)\pi_A + Sp(1 - \pi_A)} = \frac{(0.995)(0.800)}{(1 - 0.980)(0.200) + (0.995)(0.800)}$$
   $$= \frac{0.7960}{(0.020)(0.200) + 0.7960} = \frac{0.7960}{0.0040 + 0.7960} = \frac{0.7960}{0.8000} = 0.9950 \quad (99.50\%)$$

   In Setting A, a positive test is overwhelmingly accurate ($PPV = 98.0\%$).

2. **Setting B (Low-Risk Blood Donors, $\pi_B = 0.001$)**:
   $$PPV_B = \frac{Se \cdot \pi_B}{Se \cdot \pi_B + (1 - Sp)(1 - \pi_B)} = \frac{(0.980)(0.001)}{(0.980)(0.001) + (0.005)(0.999)}$$
   $$= \frac{0.000980}{0.000980 + 0.004995} = \frac{0.000980}{0.005975} \approx 0.1640 \quad (16.40\%)$$

   $$NPV_B = \frac{(0.995)(0.999)}{(0.020)(0.001) + (0.995)(0.999)} = \frac{0.994005}{0.000020 + 0.994005} = \frac{0.994005}{0.994025} \approx 0.99998 \quad (99.998\%)$$

   In Setting B, despite a test specificity of $99.5\%$, **only $16.4\%$ of screen-positive blood donors actually have Hepatitis C!** Fully $83.6\%$ of all positive test results are false positives.

### Solution, step 2: Calculate Likelihood Ratios
$$LR^+ = \frac{Se}{1 - Sp} = \frac{0.980}{1 - 0.995} = \frac{0.980}{0.005} = 196.0$$

$$LR^- = \frac{1 - Se}{Sp} = \frac{1 - 0.980}{0.995} = \frac{0.020}{0.995} \approx 0.0201$$

The test has a massive $LR^+ = 196.0$ (ruling in disease strongly) and a very small $LR^- \approx 0.020$ (ruling out disease strongly).

### Solution, step 3: Bayesian odds formulation and ethical implications
In Setting B ($\pi_B = 0.001$):
$$\text{Pre-test Odds} = \frac{\pi_B}{1 - \pi_B} = \frac{0.001}{0.999} \approx 0.0010010$$

Multiplying by $LR^+ = 196.0$:
$$\text{Post-test Odds} = \text{Pre-test Odds} \times LR^+ = 0.0010010 \times 196.0 \approx 0.196196$$

Converting back to probability:
$$\text{Post-test Probability} = \frac{\text{Post-test Odds}}{1 + \text{Post-test Odds}} = \frac{0.196196}{1 + 0.196196} = \frac{0.196196}{1.196196} \approx 0.1640 \quad (16.40\%)$$
This matches the Bayesian $PPV_B$ precisely.

**Clinical and Ethical Implications**:
In blood banking, blood units testing positive are discarded to guarantee transfusion safety. However, notifying donors that they are "HCV positive" based on a single screening immunoassay is ethically reckless: more than 5 out of 6 positive donors are completely healthy. Standard blood bank protocols mandate that screen-positive samples undergo **confirmatory secondary testing** (such as nucleic acid RT-PCR) before communicating a diagnosis to the donor.

## Fully worked question 2: Empirical ROC Construction, Trapezoidal AUC Integration, and Youden’s J Cutpoint Optimization

### Question
An oncology research laboratory investigates a novel serum microRNA biomarker ($\text{miR-21}$, expressed in relative quantification units) for distinguishing patients with early-stage ovarian carcinoma from benign pelvic masses. The biomarker concentrations measured in $n_D = 6$ confirmed ovarian cancer patients and $n_H = 6$ healthy/benign control patients are:
- **Cancer Patients ($X_D$)**: $2.8, \, 3.4, \, 4.2, \, 5.1, \, 6.0, \, 7.5$
- **Control Patients ($X_H$)**: $1.2, \, 1.8, \, 2.2, \, 3.0, \, 3.8, \, 4.8$

1. For candidate diagnostic cutoff thresholds $c \in \{1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0\}$, determine the Sensitivity ($Se$), Specificity ($Sp$), and False Positive Rate ($FPR = 1 - Sp$). Tabulate the coordinates of the empirical ROC curve.
2. Calculate the non-parametric Area Under the Curve ($\widehat{AUC}$) using both trapezoidal integration and the Mann-Whitney $U$-statistic formulation.
3. Compute Youden’s Index $J(c) = Se(c) + Sp(c) - 1$ across all candidate cutoffs, determine the optimal decision threshold $c^*$, and report the diagnostic sensitivity and specificity achieved at that optimal cutoff.

### Solution, step 1: Tabulate empirical ROC coordinates across cutoffs
A patient tests positive if $X \ge c$.
- Cancer group ($n_D = 6$): $\{2.8, 3.4, 4.2, 5.1, 6.0, 7.5\}$
- Control group ($n_H = 6$): $\{1.2, 1.8, 2.2, 3.0, 3.8, 4.8\}$

Let us evaluate $TP(c)$ (cancer $\ge c$) and $FP(c)$ (control $\ge c$):
- **$c = 1.0$**: All 6 cancers $\ge 1.0 \implies Se = 6/6 = 1.000$. All 6 controls $\ge 1.0 \implies FP = 6 \implies FPR = 6/6 = 1.000, Sp = 0.000$. Point: $(1.0, 1.0)$.
- **$c = 2.0$**: Cancers $\ge 2.0$: all 6 $\implies Se = 6/6 = 1.000$. Controls $\ge 2.0$: $\{2.2, 3.0, 3.8, 4.8\}$ (4 controls) $\implies FPR = 4/6 \approx 0.667, Sp = 2/6 \approx 0.333$. Point: $(0.667, 1.000)$.
- **$c = 3.0$**: Cancers $\ge 3.0$: $\{3.4, 4.2, 5.1, 6.0, 7.5\}$ (5 cancers) $\implies Se = 5/6 \approx 0.833$. Controls $\ge 3.0$: $\{3.0, 3.8, 4.8\}$ (3 controls) $\implies FPR = 3/6 = 0.500, Sp = 0.500$. Point: $(0.500, 0.833)$.
- **$c = 4.0$**: Cancers $\ge 4.0$: $\{4.2, 5.1, 6.0, 7.5\}$ (4 cancers) $\implies Se = 4/6 \approx 0.667$. Controls $\ge 4.0$: $\{4.8\}$ (1 control) $\implies FPR = 1/6 \approx 0.167, Sp = 5/6 \approx 0.833$. Point: $(0.167, 0.667)$.
- **$c = 5.0$**: Cancers $\ge 5.0$: $\{5.1, 6.0, 7.5\}$ (3 cancers) $\implies Se = 3/6 = 0.500$. Controls $\ge 5.0$: 0 controls $\implies FPR = 0/6 = 0.000, Sp = 1.000$. Point: $(0.000, 0.500)$.
- **$c = 6.0$**: Cancers $\ge 6.0$: $\{6.0, 7.5\}$ (2 cancers) $\implies Se = 2/6 \approx 0.333$. Controls $\ge 6.0$: 0 controls $\implies FPR = 0.000, Sp = 1.000$. Point: $(0.000, 0.333)$.
- **$c = 8.0$**: Cancers $\ge 8.0$: 0 cancers $\implies Se = 0.000$. Controls $\ge 8.0$: 0 $\implies FPR = 0.000, Sp = 1.000$. Point: $(0.0, 0.0)$.

<div class="table-wrapper"><table class="data-table">
<thead>
<tr><th>Cutoff $c$</th><th>Sensitivity $Se(c)$</th><th>Specificity $Sp(c)$</th><th>False Positive Rate $FPR(c)$</th><th>ROC Coordinate $(x, y)$</th><th>Youden's Index $J(c)$</th></tr>
</thead>
<tbody>
<tr><td>$\infty$ ($8.0$)</td><td>$0.000$</td><td>$1.000$</td><td>$0.000$</td><td>$(0.000, 0.000)$</td><td>$0.000$</td></tr>
<tr><td>$5.0$</td><td>$0.500$</td><td>$1.000$</td><td>$0.000$</td><td>$(0.000, 0.500)$</td><td>$+0.500$</td></tr>
<tr><td>$4.0$</td><td>$0.667$</td><td>$0.833$</td><td>$0.167$</td><td>$(0.167, 0.667)$</td><td>$+0.500$</td></tr>
<tr><td>$3.0$</td><td>$0.833$</td><td>$0.500$</td><td>$0.500$</td><td>$(0.500, 0.833)$</td><td>$+0.333$</td></tr>
<tr><td>$2.0$</td><td>$1.000$</td><td>$0.333$</td><td>$0.667$</td><td>$(0.667, 1.000)$</td><td>$+0.333$</td></tr>
<tr><td>$-\infty$ ($1.0$)</td><td>$1.000$</td><td>$0.000$</td><td>$1.000$</td><td>$(1.000, 1.000)$</td><td>$0.000$</td></tr>
</tbody>
</table></div>

### Solution, step 2: Area Under the Curve via Mann-Whitney U-statistic and trapezoids
1. **Mann-Whitney U-Statistic Method**:
   We compare each of the 6 cancer values against all 6 control values ($6 \times 6 = 36$ pairwise comparisons). We count how many times $X_{Di} > X_{Hj}$:
   - $X_{D1} = 2.8 > \{1.2, 1.8, 2.2\}$ (3 controls) $\implies 3$
   - $X_{D2} = 3.4 > \{1.2, 1.8, 2.2, 3.0\}$ (4 controls) $\implies 4$
   - $X_{D3} = 4.2 > \{1.2, 1.8, 2.2, 3.0, 3.8\}$ (5 controls) $\implies 5$
   - $X_{D4} = 5.1 > \{1.2, 1.8, 2.2, 3.0, 3.8, 4.8\}$ (all 6 controls) $\implies 6$
   - $X_{D5} = 6.0 > \text{all 6 controls} \implies 6$
   - $X_{D6} = 7.5 > \text{all 6 controls} \implies 6$

   Total pairwise wins $U_D = 3 + 4 + 5 + 6 + 6 + 6 = 30$.
   $$\widehat{AUC} = \frac{U_D}{n_D \times n_H} = \frac{30}{6 \times 6} = \frac{30}{36} \approx 0.8333 \quad (83.33\%)$$

2. **Trapezoidal Rule Integration**:
   Integrating under the empirical ROC step segments from $(0, 0)$ to $(1, 1)$:
   - Segment from $x = 0$ to $x = 1/6$: width $= 1/6$, average height $= (0.500 + 0.667)/2 = 0.5833 \implies \text{Area} = (1/6)(0.5833) = 0.0972$.
   - Segment from $x = 1/6$ to $x = 3/6$: width $= 2/6$, average height $= (0.667 + 0.833)/2 = 0.7500 \implies \text{Area} = (2/6)(0.750) = 0.2500$.
   - Segment from $x = 3/6$ to $x = 4/6$: width $= 1/6$, average height $= (0.833 + 1.000)/2 = 0.9167 \implies \text{Area} = (1/6)(0.9167) = 0.1528$.
   - Segment from $x = 4/6$ to $x = 1$: width $= 2/6$, height $= 1.000 \implies \text{Area} = (2/6)(1.000) = 0.3333$.
   Sum of areas $= 0.0972 + 0.2500 + 0.1528 + 0.3333 = 0.8333$.
   Both methods identically confirm $\widehat{AUC} = 0.833$ (excellent diagnostic discrimination).

### Solution, step 3: Youden's Index optimization
From our table of $J(c) = Se(c) + Sp(c) - 1$:
- Cutoff $c = 5.0$: $J = 0.500 + 1.000 - 1 = +0.500$. (Provides $100\%$ Specificity, $50\%$ Sensitivity).
- Cutoff $c = 4.0$: $J = 0.667 + 0.833 - 1 = +0.500$. (Provides $83.3\%$ Specificity, $66.7\%$ Sensitivity).

**Clinical Decision Rationale**:
In ovarian cancer screening, where false-positive surgery carries high morbidity, the investigator selects **$c^* = 4.0\text{ units}$** (or $c^* = 5.0$ if zero false alarms are demanded). At $c^* = 4.0$, the test achieves $Se = 66.7\%$ and $Sp = 83.3\%$ with maximum Youden Index $J = 0.50$.

## Fully worked question 3: Diagnostic Screening in Populations: Lead-Time Bias, Length Bias, and Overdiagnosis

### Question
A health authority in Scandinavia evaluates a mobile mammography breast cancer screening trial conducted between 2010 and 2025. Two non-randomized cohorts of women aged 50–69 are compared:
- **Screened Cohort ($n_{\text{scr}} = 10,000$)**: Screened biennially. Exactly $300$ invasive breast cancers are diagnosed. Among these 300 women, 240 survive at least 5 years from their date of diagnosis ($5\text{-year survival} = 80.0\%$). Over the 15-year trial, 60 breast cancer deaths occur in the screened cohort ($15\text{-year mortality} = 6.0 \text{ per 1,000 women}$).
- **Unscreened Control Cohort ($n_{\text{unscr}} = 10,000$)**: Routine symptomatic care. Exactly $200$ invasive breast cancers are diagnosed upon clinical symptom presentation. Among these 200 women, 100 survive at least 5 years from diagnosis ($5\text{-year survival} = 50.0\%$). Over the 15-year trial, 60 breast cancer deaths occur in the unscreened cohort ($15\text{-year mortality} = 6.0 \text{ per 1,000 women}$).
- Extensive natural history modeling indicates that screening advances the diagnosis date by an average **lead time of $\bar{L} = 3.0\text{ years}$**.

1. Analyze the apparent 5-year survival statistics: compute the survival improvement ($80\%$ vs $50\%$). Explain why comparing 5-year survival from diagnosis creates a deceptive illusion of screening efficacy, and prove why **disease-specific population mortality** is the only valid primary endpoint.
2. Demonstrate how **lead-time bias** mathematically inflates 5-year survival without delaying death. If an unscreened patient is diagnosed symptomatically at age 55 and dies at age 59 (survival $= 4\text{ years}$, 5-year survivor $=$ No), show what happens if screening detects her cancer at age 52 with the exact same death age of 59.
3. Calculate the excess cancer detection count in the screened arm ($300$ vs $200$). Formally define **overdiagnosis**, estimate the overdiagnosis fraction, and describe the clinical and societal harms of overdiagnosing pseudodisease.

### Solution, step 1: Deceptive 5-year survival vs population mortality
1. **Apparent 5-Year Survival Comparison**:
   $$\text{Survival}_{\text{screened}} = \frac{240}{300} = 0.800 \quad (80.0\%)$$
   $$\text{Survival}_{\text{unscreened}} = \frac{100}{200} = 0.500 \quad (50.0\%)$$
   A naive observer would celebrate an apparent $30.0\%$ absolute increase in 5-year survival ($RRR = 60\%$).

2. **True Population Disease-Specific Mortality**:
   $$\text{Mortality Rate}_{\text{screened}} = \frac{60}{10,000} = 0.0060 = 6.0 \text{ per 1,000 women}$$
   $$\text{Mortality Rate}_{\text{unscreened}} = \frac{60}{10,000} = 0.0060 = 6.0 \text{ per 1,000 women}$$
   $$\text{Mortality Rate Ratio} = \frac{6.0}{6.0} = 1.000$$

**Methodological Conclusion**:
The screening program had **zero effect on saving human lives**: exactly 60 women died of breast cancer in both arms! The apparent leap in 5-year survival from $50\%$ to $80\%$ was entirely a mathematical artifact of **lead-time bias**, **length bias**, and **overdiagnosis**.
Survival calculated from the date of diagnosis is completely invalid because screening artificially changes the starting point of the survival clock. Only **cause-specific population mortality** (deaths divided by total randomized population) has a fixed, uncompromised denominator and serves as the gold standard endpoint.

### Solution, step 2: Mathematical mechanics of lead-time bias
Consider a patient whose tumor has a predetermined biological trajectory:
- Biological inception: Age 45.
- Symptomatic presentation: Age 55.
- Biological death: Age 59.

1. **Under Symptomatic Care (Unscreened)**:
   - Diagnosed at Age 55.
   - Dies at Age 59.
   - Observed Survival: $59 - 55 = 4\text{ years}$.
   - 5-Year Survival Status: **Fails** ($4 < 5\text{ years}$).

2. **Under Screening (with Lead Time $\bar{L} = 3\text{ years}$)**:
   - Diagnosed by mammography at Age 52 ($55 - 3 = 52$).
   - Dies at the exact same Age 59 (treatment had zero biological efficacy).
   - Observed Survival: $59 - 52 = 7\text{ years}$.
   - 5-Year Survival Status: **Succeeds** ($7 \ge 5\text{ years}$)!

Screening did not prolong this woman's life by even one single day. She lived for exactly 59 years. The only consequence of screening was that she lived with the anxiety, fear, and surgical side effects of knowing she had cancer for 7 years instead of 4 years. Yet in the hospital's statistical ledger, she was miraculously converted from a "5-year failure" into a "5-year survival triumph."

### Solution, step 3: Overdiagnosis evaluation and clinical harms
In this cohort:
- Diagnosed in screened arm: $300$ cancers.
- Diagnosed in unscreened arm: $200$ cancers.
- Excess cancers diagnosed: $300 - 200 = 100$ excess cases.

**Formal Definition of Overdiagnosis**:
Overdiagnosis is the detection through screening of indolent, non-progressive, or extremely slow-growing cancers that would never have produced clinical symptoms or threatened the patient's life before she died of unrelated natural causes (e.g., cardiovascular disease or old age).

**Estimated Overdiagnosis Fraction**:
Relative to all screen-detected cancers:
$$\text{Overdiagnosis Fraction} = \frac{\text{Excess Screen-Detected Cancers}}{\text{Total Screened Cancers}} = \frac{100}{300} = 0.3333 \quad (33.33\%)$$
One out of every three breast cancers detected in the screening program represents an overdiagnosed pseudodisease!

**Harms of Overdiagnosis**:
Because pathologists cannot reliably distinguish between lethal and indolent micro-cancers under a microscope, all 100 overdiagnosed women underwent unnecessary partial or total mastectomies, radiation therapy, and systemic endocrine chemotherapy. They suffered physical scarring, chronic lymphedema, sexual dysfunction, and intense psychological trauma—all to treat a disease that was never going to harm them. Balancing true mortality reduction against the grave harms of overdiagnosis is the central ethical dilemma of population cancer screening.
"""

(OUT_DIR / "unit-5.md").write_text(unit5.strip() + "\n", encoding="utf-8")
(OUT_DIR / "unit-6.md").write_text(unit6.strip() + "\n", encoding="utf-8")
print("Units 5 and 6 written.")
