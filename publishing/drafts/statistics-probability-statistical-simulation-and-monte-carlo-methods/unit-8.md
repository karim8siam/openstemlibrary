# Unit 8: Resampling & Permutation Methods: Bootstrap and Jackknife

In classical mathematical statistics, constructing confidence intervals, assessing estimator bias, and testing statistical hypotheses traditionally require making restrictive distributional assumptions (such as normality of observations) or relying upon asymptotic large-sample approximations whose finite-sample adequacy may be questionable. When estimating complex parameters—such as the ratio of trimmed medians, eigenvalues of sample correlation matrices, or non-linear econometric elasticities—analytical sampling distributions are typically impossible to derive in closed form.

In 1979, Bradley Efron published a revolutionary paper in *The Annals of Statistics* introducing the **Bootstrap**. Resampling methods replace intractable mathematical derivations with massive computer simulation, using the empirical data sample itself as an empirical proxy for the unknown population distribution. Alongside Maurice Quenouille's and John Tukey's **Jackknife** and Fisher's **Permutation Tests**, resampling constitutes an indispensable pillar of modern computational statistical inference.

## 8.1 The Plug-In Principle and Bradley Efron's Empirical Bootstrap

Let $\mathbf{X} = (X_1, X_2, \dots, X_n)$ be an independent and identically distributed (i.i.d.) random sample drawn from an unknown cumulative distribution function $F$:
$$X_i \sim F \quad \text{i.i.d. for } i = 1, \dots, n$$
We desire to estimate an unknown population parameter $\theta = t(F)$, such as the population mean $\mu = \int x\,dF(x)$, population median $F^{-1}(0.5)$, or variance $\sigma^2$.

Let $\hat{\theta} = s(\mathbf{X})$ be a sample estimator of $\theta$. To quantify the statistical uncertainty of $\hat{\theta}$, we need its sampling distribution $F_{\hat{\theta}}$, standard error $\text{se}_F(\hat{\theta})$, and bias $\text{bias}_F(\hat{\theta}) = \mathbb{E}_F[\hat{\theta}] - \theta$.

### 1. The Empirical Distribution Function (EDF)
The sample data $\mathbf{X}$ define the **Empirical Distribution Function (EDF)** $\hat{F}_n$:

$$\hat{F}_n(x) = \frac{1}{n} \sum_{i=1}^n I(X_i \le x)$$

The EDF assigns discrete probability mass $1/n$ to each of the $n$ observed data points:
$$P_{\hat{F}_n}(X^* = X_i) = \frac{1}{n} \quad \text{for } i = 1, 2, \dots, n$$

By the **Glivenko-Cantelli Theorem (The Fundamental Theorem of Statistics)**:
$$\lim_{n \to \infty} \sup_{x \in \mathbb{R}} |\hat{F}_n(x) - F(x)| = 0 \quad \text{almost surely}$$
As $n \to \infty$, the empirical distribution $\hat{F}_n$ converges uniformly to the true population distribution $F$.

### 2. The Plug-In Principle
The **Plug-In Principle** dictates that any unknown population characteristic $\theta = t(F)$ is estimated by the corresponding characteristic of the empirical distribution:
$$\hat{\theta} = t(\hat{F}_n)$$
Similarly, the unknown standard error $\text{se}_F(\hat{\theta})$ is estimated by the plug-in estimate:
$$\widehat{\text{se}}(\hat{\theta}) = \text{se}_{\hat{F}_n}(\hat{\theta}^*)$$

### 3. The Non-Parametric Bootstrap Algorithm
Because calculating $\text{se}_{\hat{F}_n}(\hat{\theta}^*)$ analytically is intractable for complex estimators, Efron approximated it via Monte Carlo simulation:
1. For $b = 1, 2, \dots, B$ (where $B \ge 1,000$ bootstrap replicates):
   - Draw a **bootstrap sample** $\mathbf{X}^{*b} = (X_1^{*b}, X_2^{*b}, \dots, X_n^{*b})$ by sampling $n$ observations **uniformly at random with replacement** from the original dataset $\mathbf{X}$.
   - Compute the bootstrap replicate of the statistic:
     $$\hat{\theta}^{*b} = s(\mathbf{X}^{*b})$$
2. The **Bootstrap Standard Error** is the sample standard deviation of the $B$ bootstrap replications:
   $$\widehat{\text{se}}_B(\hat{\theta}) = \sqrt{\frac{1}{B - 1} \sum_{b=1}^B \left( \hat{\theta}^{*b} - \bar{\theta}^* \right)^2}$$
   where $\bar{\theta}^* = \frac{1}{B} \sum_{b=1}^B \hat{\theta}^{*b}$.
3. The **Bootstrap Bias Estimate** is:
   $$\widehat{\text{bias}}_B(\hat{\theta}) = \bar{\theta}^* - \hat{\theta}$$
   The bias-corrected point estimate is $\hat{\theta}_{\text{bc}} = \hat{\theta} - \widehat{\text{bias}}_B = 2\hat{\theta} - \bar{\theta}^*$.

## 8.2 Bootstrap Confidence Intervals: Normal, Percentile, Basic, and BCa

Constructing confidence intervals for parameter $\theta$ via bootstrapping admits several formulations:

### 1. The Standard Normal Bootstrap Interval
Assuming the sampling distribution of $\hat{\theta}$ is approximately Gaussian:
$$\mathcal{CI}_{\text{norm}} = \left[ \hat{\theta} - z_{1 - \alpha/2} \widehat{\text{se}}_B, \; \hat{\theta} + z_{1 - \alpha/2} \widehat{\text{se}}_B \right]$$
*Limitation*: Fails when the sampling distribution is skewed, heavy-tailed, or bounded.

### 2. The Percentile Bootstrap Interval
Sort the $B$ bootstrap estimates in ascending order:
$$\hat{\theta}^{*(1)} \le \hat{\theta}^{*(2)} \le \dots \le \hat{\theta}^{*(B)}$$
The $(1 - \alpha) \times 100\%$ **Percentile Interval** uses the empirical quantiles of the bootstrap distribution:

$$\mathcal{CI}_{\text{perc}} = \left[ \hat{\theta}^{*(\lfloor B \cdot \alpha/2 \rfloor)}, \; \hat{\theta}^{*(\lfloor B \cdot (1 - \alpha/2) \rfloor)} \right]$$

For a $95\%$ confidence interval with $B = 2,000$:
$$\mathcal{CI}_{0.95} = \left[ \hat{\theta}^{*(50)}, \; \hat{\theta}^{*(1950)} \right]$$
*Key Property (Transformation Invariance)*: If $g(\cdot)$ is any strictly monotonic transformation, the percentile interval for $g(\theta)$ is exactly $[g(\hat{\theta}_{\text{low}}), g(\hat{\theta}_{\text{high}})]$.
*Accuracy*: First-order accurate: coverage error $= \mathcal{O}(n^{-1/2})$.

### 3. The Basic (Empirical) Bootstrap Interval
Let the estimation error be $\delta = \hat{\theta} - \theta$. The basic bootstrap approximates the distribution of $\delta$ by the bootstrap errors $\delta^* = \hat{\theta}^* - \hat{\theta}$:
$$\mathcal{CI}_{\text{basic}} = \left[ 2\hat{\theta} - \hat{\theta}^{*(1 - \alpha/2)}, \; 2\hat{\theta} - \hat{\theta}^{*(\alpha/2)} \right]$$

### 4. Bias-Corrected and Accelerated (BCa) Intervals
Formulated by Efron in 1987, the **BCa Interval** corrects for both median bias and variance stabilization through two parameters:
- **$z_0$ (Bias-Correction Factor)**: Measures the median bias of $\hat{\theta}^*$:
  $$z_0 = \Phi^{-1}\left( \frac{\#\{\hat{\theta}^{*b} < \hat{\theta}\}}{B} \right)$$
- **$a$ (Acceleration Parameter)**: Measures the rate of change of the standard error of $\hat{\theta}$ with respect to the true parameter $\theta$, computed via jackknife influence values:
  $$a = \frac{\sum_{i=1}^n (\bar{U} - U_i)^3}{6 \left[ \sum_{i=1}^n (\bar{U} - U_i)^2 \right]^{3/2}}$$

The adjusted quantile points $\alpha_1, \alpha_2$ are:
$$\alpha_1 = \Phi\left( z_0 + \frac{z_0 + z_{\alpha/2}}{1 - a(z_0 + z_{\alpha/2})} \right), \quad \alpha_2 = \Phi\left( z_0 + \frac{z_0 + z_{1 - \alpha/2}}{1 - a(z_0 + z_{1 - \alpha/2})} \right)$$
$$\mathcal{CI}_{\text{BCa}} = \left[ \hat{\theta}^{*(\alpha_1)}, \; \hat{\theta}^{*(\alpha_2)} \right]$$
The BCa interval is **second-order accurate**: coverage error $= \mathcal{O}(n^{-1})$ and is transformation-invariant.

## 8.3 The Quenouille-Tukey Jackknife

Developed by Maurice Quenouille (1949) for bias reduction and extended by John Tukey (1958) for variance estimation, the **Jackknife** is a deterministic leave-one-out resampling method that requires no random number generation.

### 1. Leave-One-Out Estimators and Pseudovalues
Let $\mathbf{X} = (X_1, \dots, X_n)$ be a sample of size $n$, with point estimate $\hat{\theta} = s(\mathbf{X})$.
For each observation $i \in \{1, 2, \dots, n\}$, define the **leave-one-out subsample** $\mathbf{X}_{(i)}$ omitting the $i$-th data point:
$$\mathbf{X}_{(i)} = (X_1, \dots, X_{i-1}, X_{i+1}, \dots, X_n)$$
Let $\hat{\theta}_{(i)} = s(\mathbf{X}_{(i)})$ be the statistic evaluated on this $(n-1)$-sized subsample.

The mean of the leave-one-out estimates is:
$$\hat{\theta}_{(\bullet)} = \frac{1}{n} \sum_{i=1}^n \hat{\theta}_{(i)}$$

### 2. Jackknife Bias and Variance Formulas
- **Jackknife Bias Estimator**:
  $$\widehat{\text{bias}}_{\text{jack}} = (n - 1) (\hat{\theta}_{(\bullet)} - \hat{\theta})$$
- **Bias-Corrected Jackknife Estimator**:
  $$\hat{\theta}_{\text{jack}} = \hat{\theta} - \widehat{\text{bias}}_{\text{jack}} = n \hat{\theta} - (n - 1) \hat{\theta}_{(\bullet)}$$
- **Jackknife Variance Estimator**:
  $$\widehat{\text{var}}_{\text{jack}}(\hat{\theta}) = \frac{n - 1}{n} \sum_{i=1}^n \left( \hat{\theta}_{(i)} - \hat{\theta}_{(\bullet)} \right)^2$$
- **Jackknife Standard Error**:
  $$\widehat{\text{se}}_{\text{jack}} = \sqrt{\widehat{\text{var}}_{\text{jack}}}$$

*Theoretical Limitation*: The jackknife is non-smooth: it fails completely for non-differentiable statistics such as the sample median or sample quantiles, where $\widehat{\text{var}}_{\text{jack}}$ is inconsistent. The bootstrap, by contrast, handles non-smooth statistics seamlessly.

## 8.4 Permutation Tests: Fisher's Exact Hypothesis Testing

When testing the null hypothesis $H_0$ that two samples come from identical distributions, Ronald Fisher formulated the **Permutation Test (Randomization Test)**.

### The Two-Sample Permutation Algorithm
Consider sample $\mathbf{X} = (X_1, \dots, X_{n_1})$ from group 1 and sample $\mathbf{Y} = (Y_1, \dots, Y_{n_2})$ from group 2.
- Null hypothesis: $H_0: F_X = F_Y$.
- Compute the observed test statistic (e.g., difference in sample means):
  $$T_{\text{obs}} = \bar{X} - \bar{Y}$$
- Under $H_0$, group membership labels are completely exchangeable. Pool the $N = n_1 + n_2$ observations into a single dataset $\mathbf{Z} = (\mathbf{X}, \mathbf{Y})$.
- The total number of possible partitions of $N$ items into groups of size $n_1$ and $n_2$ is:
  $$M = \binom{N}{n_1} = \frac{N!}{n_1! n_2!}$$

For each of the $M$ partitions $\pi$:
- Assign $n_1$ items to group 1 and $n_2$ items to group 2, and compute $T_\pi = \bar{X}_\pi - \bar{Y}_\pi$.

The **Exact Permutation p-value** (for a two-tailed test) is:

$$p_{\text{exact}} = \frac{1}{M} \sum_{\pi=1}^M I(|T_\pi| \ge |T_{\text{obs}}|)$$

When $M$ is astronomically large (e.g., $n_1 = n_2 = 50 \implies \binom{100}{50} \approx 10^{29}$), exact enumeration is impossible. Statisticians draw a random sample of $B = 10,000$ random permutations to compute the **Monte Carlo Permutation p-value**:

$$\hat{p}_{\text{MC}} = \frac{1 + \sum_{b=1}^B I(|T_b^*| \ge |T_{\text{obs}}|)}{B + 1}$$
Permutation tests are completely distribution-free, valid for any sample size, and require zero parametric assumptions.

## Fully worked question 1: Non-Parametric Bootstrap Standard Error and Confidence Intervals

### Question
A biomedical researcher observes $n = 5$ patient recovery durations (in days) following a clinical therapy:
$$\mathbf{x} = (12, 15, 18, 22, 33)$$
The sample mean is $\bar{x} = 20.0$ days.
1. Compute the analytical standard error of the sample mean $\text{se}(\bar{x}) = s / \sqrt{n}$.
2. In a small Monte Carlo bootstrap study, $B = 6$ bootstrap samples are drawn with replacement from $\mathbf{x}$:
   - Sample 1: $(15, 15, 18, 22, 33) \implies \bar{x}^{*1} = 20.6$
   - Sample 2: $(12, 18, 18, 18, 22) \implies \bar{x}^{*2} = 17.6$
   - Sample 3: $(12, 12, 15, 22, 33) \implies \bar{x}^{*3} = 18.8$
   - Sample 4: $(15, 18, 22, 33, 33) \implies \bar{x}^{*4} = 24.2$
   - Sample 5: $(12, 15, 15, 18, 22) \implies \bar{x}^{*5} = 16.4$
   - Sample 6: $(18, 22, 22, 33, 33) \implies \bar{x}^{*6} = 25.6$
   Compute the bootstrap mean $\bar{x}^*$, the bootstrap standard error $\widehat{\text{se}}_B$, and the bootstrap bias estimate.
3. Construct the $90\%$ percentile bootstrap confidence interval using the sorted bootstrap replicates.

### Solution, step 1: Analytical Sample Standard Error
Given data $\mathbf{x} = (12, 15, 18, 22, 33)$ with $n = 5$:
- Sample mean:
  $$\bar{x} = \frac{12 + 15 + 18 + 22 + 33}{5} = \frac{100}{5} = 20.0$$
- Deviations from mean:
  $$(12 - 20) = -8 \implies (-8)^2 = 64$$
  $$(15 - 20) = -5 \implies (-5)^2 = 25$$
  $$(18 - 20) = -2 \implies (-2)^2 = 4$$
  $$(22 - 20) = +2 \implies 2^2 = 4$$
  $$(33 - 20) = +13 \implies 13^2 = 169$$
- Sum of squared deviations:
  $$\sum (x_i - \bar{x})^2 = 64 + 25 + 4 + 4 + 169 = 266$$
- Sample variance and standard deviation:
  $$s^2 = \frac{266}{n - 1} = \frac{266}{4} = 66.50 \implies s = \sqrt{66.50} \approx 8.1548$$
- Analytical standard error:
  $$\text{se}(\bar{x}) = \frac{s}{\sqrt{n}} = \frac{8.1548}{\sqrt{5}} = \frac{8.1548}{2.2361} \approx 3.6469 \approx 3.65 \text{ days}$$

### Solution, step 2: Bootstrap Estimates
The $B = 6$ bootstrap means are:
$$\bar{\mathbf{x}}^* = (20.6, 17.6, 18.8, 24.2, 16.4, 25.6)$$
1. **Bootstrap Mean**:
   $$\bar{x}^* = \frac{20.6 + 17.6 + 18.8 + 24.2 + 16.4 + 25.6}{6} = \frac{123.2}{6} \approx 20.533$$
2. **Bootstrap Bias Estimate**:
   $$\widehat{\text{bias}}_B = \bar{x}^* - \bar{x} = 20.533 - 20.000 = +0.533 \text{ days}$$
3. **Bootstrap Standard Error**:
   Deviations from $\bar{x}^* = 20.533$:
   - $(20.6 - 20.533)^2 = 0.067^2 \approx 0.0045$
   - $(17.6 - 20.533)^2 = (-2.933)^2 \approx 8.6025$
   - $(18.8 - 20.533)^2 = (-1.733)^2 \approx 3.0033$
   - $(24.2 - 20.533)^2 = (3.667)^2 \approx 13.4469$
   - $(16.4 - 20.533)^2 = (-4.133)^2 \approx 17.0817$
   - $(25.6 - 20.533)^2 = (5.067)^2 \approx 25.6745$
   Sum of squares:
   $$\sum (\bar{x}^{*b} - \bar{x}^*)^2 = 0.0045 + 8.6025 + 3.0033 + 13.4469 + 17.0817 + 25.6745 = 67.8134$$
   $$\widehat{\text{se}}_B = \sqrt{\frac{67.8134}{6 - 1}} = \sqrt{\frac{67.8134}{5}} = \sqrt{13.5627} \approx 3.6828 \approx 3.68 \text{ days}$$
Notice how closely the bootstrap standard error ($3.68$) approximates the true analytical standard error ($3.65$) even with only 6 bootstrap replicates!

### Solution, step 3: Percentile Bootstrap Confidence Interval
Sort the $B = 6$ bootstrap replicates in ascending order:
$$\bar{\mathbf{x}}^{*(sorted)} = [16.4, 17.6, 18.8, 20.6, 24.2, 25.6]$$
For a $90\%$ confidence interval ($\alpha = 0.10$), the lower quantile is $\alpha/2 = 0.05$ and upper quantile is $1 - \alpha/2 = 0.95$.
With $B = 6$, taking the lowest and highest values:
$$\mathcal{CI}_{0.90} = [16.4, \; 25.6] \text{ days}$$

## Fully worked question 2: Jackknife Bias and Variance for Ratio Estimation

### Question
An economist estimates the population debt-to-income ratio $R = \mu_Y / \mu_X$ using sample ratio estimator:
$$\hat{R} = \frac{\bar{Y}}{\bar{X}}$$
from a sample of $n = 4$ household pairs $(X_i, Y_i)$ where $X$ is income and $Y$ is debt (in thousands of dollars):
- Household 1: $(X_1 = 50, Y_1 = 20)$
- Household 2: $(X_2 = 60, Y_2 = 30)$
- Household 3: $(X_3 = 80, Y_3 = 40)$
- Household 4: $(X_4 = 110, Y_4 = 70)$

1. Compute the full-sample totals and the plug-in ratio estimate $\hat{R}$.
2. Evaluate the four leave-one-out ratio estimates $\hat{R}_{(1)}, \dots, \hat{R}_{(4)}$.
3. Compute the Jackknife bias estimate $\widehat{\text{bias}}_{\text{jack}}$ and the Jackknife standard error $\widehat{\text{se}}_{\text{jack}}$.

### Solution, step 1: Full-Sample Ratio Estimate
Total income:
$$\sum_{i=1}^4 X_i = 50 + 60 + 80 + 110 = 300$$
Total debt:
$$\sum_{i=1}^4 Y_i = 20 + 30 + 40 + 70 = 160$$
The sample ratio estimate is:
$$\hat{R} = \frac{\bar{Y}}{\bar{X}} = \frac{160 / 4}{300 / 4} = \frac{160}{300} = \frac{8}{15} \approx 0.533333$$

### Solution, step 2: Computation of Leave-One-Out Estimates
For each $i \in \{1, 2, 3, 4\}$, the leave-one-out ratio is $\hat{R}_{(i)} = \frac{\sum_{j \ne i} Y_j}{\sum_{j \ne i} X_j}$:
- **Omitting Household 1 ($X_1 = 50, Y_1 = 20$)**:
  $$\sum X_{(1)} = 300 - 50 = 250, \quad \sum Y_{(1)} = 160 - 20 = 140$$
  $$\hat{R}_{(1)} = \frac{140}{250} = 0.560000$$
- **Omitting Household 2 ($X_2 = 60, Y_2 = 30$)**:
  $$\sum X_{(2)} = 300 - 60 = 240, \quad \sum Y_{(2)} = 160 - 30 = 130$$
  $$\hat{R}_{(2)} = \frac{130}{240} \approx 0.541667$$
- **Omitting Household 3 ($X_3 = 80, Y_3 = 40$)**:
  $$\sum X_{(3)} = 300 - 80 = 220, \quad \sum Y_{(3)} = 160 - 40 = 120$$
  $$\hat{R}_{(3)} = \frac{120}{220} = \frac{6}{11} \approx 0.545455$$
- **Omitting Household 4 ($X_4 = 110, Y_4 = 70$)**:
  $$\sum X_{(4)} = 300 - 110 = 190, \quad \sum Y_{(4)} = 160 - 70 = 90$$
  $$\hat{R}_{(4)} = \frac{90}{190} = \frac{9}{19} \approx 0.473684$$

Mean of leave-one-out estimates:
$$\hat{R}_{(\bullet)} = \frac{0.560000 + 0.541667 + 0.545455 + 0.473684}{4} = \frac{2.120806}{4} \approx 0.530202$$

### Solution, step 3: Jackknife Bias and Standard Error
1. **Jackknife Bias Estimate**:
   $$\widehat{\text{bias}}_{\text{jack}} = (n - 1) (\hat{R}_{(\bullet)} - \hat{R}) = (4 - 1) (0.530202 - 0.533333) = 3 \times (-0.003131) \approx -0.009393$$
   The bias-corrected estimate is:
   $$\hat{R}_{\text{jack}} = \hat{R} - \widehat{\text{bias}}_{\text{jack}} = 0.533333 - (-0.009393) \approx 0.542726$$

2. **Jackknife Variance and Standard Error**:
   Deviations from $\hat{R}_{(\bullet)} = 0.530202$:
   - $(0.560000 - 0.530202)^2 = 0.029798^2 \approx 0.0008879$
   - $(0.541667 - 0.530202)^2 = 0.011465^2 \approx 0.0001314$
   - $(0.545455 - 0.530202)^2 = 0.015253^2 \approx 0.0002327$
   - $(0.473684 - 0.530202)^2 = (-0.056518)^2 \approx 0.0031943$
   Sum of squared deviations:
   $$\sum_{i=1}^4 (\hat{R}_{(i)} - \hat{R}_{(\bullet)})^2 = 0.0008879 + 0.0001314 + 0.0002327 + 0.0031943 = 0.0044463$$
   $$\widehat{\text{var}}_{\text{jack}}(\hat{R}) = \frac{n - 1}{n} \sum_{i=1}^n (\hat{R}_{(i)} - \hat{R}_{(\bullet)})^2 = \frac{3}{4} \times 0.0044463 \approx 0.0033347$$
   $$\widehat{\text{se}}_{\text{jack}} = \sqrt{0.0033347} \approx 0.057747 \approx 0.0577$$

*Conclusion*: The estimated debt-to-income ratio is $0.533 \pm 0.058$, with a small negative finite-sample bias of $-0.009$.

## Fully worked question 3: Exact Two-Sample Permutation Test

### Question
A randomized clinical trial compares a new drug (Group A, $n_A = 3$) against a standard placebo (Group B, $n_B = 3$) on blood pressure reduction (mm Hg):
- Group A: $(8, 11, 14) \implies \bar{X}_A = 11.0$
- Group B: $(3, 5, 7) \implies \bar{X}_B = 5.0$

The observed test statistic is the difference in group means:
$$T_{\text{obs}} = \bar{X}_A - \bar{X}_B = 11.0 - 5.0 = +6.0$$

1. Calculate the total number of distinct permutations $M = \binom{n_A + n_B}{n_A}$.
2. Enumerate all distinct permutations and compute the test statistic $T$ for each partition.
3. Determine the exact one-tailed and two-tailed permutation p-values, and state the statistical conclusion at significance level $\alpha = 0.05$.

### Solution, step 1: Total Number of Partitions
The pooled dataset of $N = 3 + 3 = 6$ observations is:
$$\mathbf{Z} = (3, 5, 7, 8, 11, 14)$$
The sum of all six observations is:
$$\sum Z_i = 3 + 5 + 7 + 8 + 11 + 14 = 48$$
The overall mean is $\bar{Z} = 48 / 6 = 8.0$.
Notice that:
$$\bar{X}_A - \bar{X}_B = \frac{\sum_{i \in A} Z_i}{3} - \frac{48 - \sum_{i \in A} Z_i}{3} = \frac{2 \sum_{i \in A} Z_i - 48}{3}$$
The test statistic is completely determined by the sum of elements assigned to Group A: $S_A = \sum_{i \in A} Z_i$!

The total number of equiprobable permutations under $H_0$ is:
$$M = \binom{6}{3} = \frac{6 \times 5 \times 4}{3 \times 2 \times 1} = 20 \text{ distinct permutations}$$

### Solution, step 2: Enumeration of All 20 Permutations and Test Statistics
We list all 20 possible subsets of size 3 from $\{3, 5, 7, 8, 11, 14\}$ and compute $S_A$ and $T = \frac{2 S_A - 48}{3}$:
1. $\{3, 5, 7\} \implies S_A = 15 \implies T = \frac{30 - 48}{3} = -6.0$
2. $\{3, 5, 8\} \implies S_A = 16 \implies T = \frac{32 - 48}{3} = -5.33$
3. $\{3, 5, 11\} \implies S_A = 19 \implies T = \frac{38 - 48}{3} = -3.33$
4. $\{3, 5, 14\} \implies S_A = 22 \implies T = \frac{44 - 48}{3} = -1.33$
5. $\{3, 7, 8\} \implies S_A = 18 \implies T = \frac{36 - 48}{3} = -4.0$
6. $\{3, 7, 11\} \implies S_A = 21 \implies T = \frac{42 - 48}{3} = -2.0$
7. $\{3, 7, 14\} \implies S_A = 24 \implies T = \frac{48 - 48}{3} = 0.0$
8. $\{3, 8, 11\} \implies S_A = 22 \implies T = -1.33$
9. $\{3, 8, 14\} \implies S_A = 25 \implies T = +0.67$
10. $\{3, 11, 14\} \implies S_A = 28 \implies T = +2.67$
11. $\{5, 7, 8\} \implies S_A = 20 \implies T = \frac{40 - 48}{3} = -2.67$
12. $\{5, 7, 11\} \implies S_A = 23 \implies T = -0.67$
13. $\{5, 7, 14\} \implies S_A = 26 \implies T = +1.33$
14. $\{5, 8, 11\} \implies S_A = 24 \implies T = 0.0$
15. $\{5, 8, 14\} \implies S_A = 27 \implies T = +2.0$
16. $\{5, 11, 14\} \implies S_A = 30 \implies T = +4.0$
17. $\{7, 8, 11\} \implies S_A = 26 \implies T = +1.33$
18. $\{7, 8, 14\} \implies S_A = 29 \implies T = +3.33$
19. $\{7, 11, 14\} \implies S_A = 32 \implies T = +5.33$
20. $\{8, 11, 14\} \implies S_A = 33 \implies T = \frac{66 - 48}{3} = +6.0$ (Observed data!)

The observed statistic is $T_{\text{obs}} = +6.0$.

### Solution, step 3: Exact p-Value Determination
1. **One-Tailed Test ($H_1: \mu_A > \mu_B$)**:
   We count the number of permutations where $T \ge T_{\text{obs}} = +6.0$:
   Only permutation 20 satisfies $T \ge +6.0$ ($T = +6.0$).
   $$p_{\text{one-tailed}} = \frac{\#\{T \ge 6.0\}}{20} = \frac{1}{20} = 0.0500$$

2. **Two-Tailed Test ($H_1: \mu_A \ne \mu_B$)**:
   We count permutations where $|T| \ge |T_{\text{obs}}| = 6.0$:
   - Permutation 1: $T = -6.0$ ($|-6.0| = 6.0$).
   - Permutation 20: $T = +6.0$ ($|+6.0| = 6.0$).
   Exactly 2 permutations satisfy $|T| \ge 6.0$:
   $$p_{\text{two-tailed}} = \frac{\#\{|T| \ge 6.0\}}{20} = \frac{2}{20} = 0.1000$$

*Statistical Conclusion*:
At significance level $\alpha = 0.05$, the two-tailed p-value is $p = 0.1000 > 0.05$. Therefore, we fail to reject the null hypothesis of equal efficacy. Because sample sizes are tiny ($n_A = n_B = 3$), even with completely separated samples (every observation in A exceeds every observation in B), the smallest possible two-tailed p-value is $2/20 = 0.10$, mathematically preventing rejection at the $5\%$ level without larger sample sizes.


## 8.9 The Auxiliary Particle Filter (APF)

In Section 8.4, we examined the Sequential Importance Resampling (SIR) particle filter. While SIR is simple, it suffers from a major defect known as the "blind proposal" problem: particles $\mathbf{x}_t^{(i)}$ are propagated forward according to the state transition density $f(\mathbf{x}_t \mid \mathbf{x}_{t-1}^{(i)})$ without taking into account the newly arrived observation $\mathbf{y}_t$. If the measurement noise is small, the likelihood function $g(\mathbf{y}_t \mid \mathbf{x}_t)$ forms a narrow peak in state space. Propagating particles blindly causes almost all particles to land in regions of near-zero likelihood, triggering catastrophic particle collapse.

Michael K. Pitt and Neil Shephard (1999) solved this deficiency by inventing the **Auxiliary Particle Filter (APF)**.

### 1. The Auxiliary Joint Density
The key insight of the APF is to introduce an auxiliary index variable $k \in \{1, \dots, N\}$ that identifies which particle from time $t-1$ will be propagated forward to generate state $\mathbf{x}_t$. The joint target distribution of the pair $(k, \mathbf{x}_t)$ conditional on $\mathbf{y}_{1:t}$ is:

$$p(k, \mathbf{x}_t \mid \mathbf{y}_{1:t}) \propto g(\mathbf{y}_t \mid \mathbf{x}_t) f(\mathbf{x}_t \mid \mathbf{x}_{t-1}^{(k)}) w_{t-1}^{(k)}$$

Instead of sampling from this intractable joint density directly, the APF samples from an auxiliary proposal distribution:
$$q(k, \mathbf{x}_t \mid \mathbf{y}_{1:t}) = q(k \mid \mathbf{y}_{1:t}) q(\mathbf{x}_t \mid k, \mathbf{y}_{1:t})$$

### 2. Pre-Weighting and Lookahead
To construct $q(k \mid \mathbf{y}_{1:t})$, the APF computes a deterministic point estimate $\boldsymbol{\mu}_t^{(k)}$ of the future state given $\mathbf{x}_{t-1}^{(k)}$ (such as the conditional mean $\boldsymbol{\mu}_t^{(k)} = \mathbb{E}[\mathbf{X}_t \mid \mathbf{x}_{t-1}^{(k)}]$ or the mode). The first-stage auxiliary weights are defined as:

$$\lambda_k \propto w_{t-1}^{(k)} g(\mathbf{y}_t \mid \boldsymbol{\mu}_t^{(k)}), \quad k = 1, \dots, N$$

The auxiliary weights $\lambda_k$ act as a predictive lookahead: particles whose predicted future states are consistent with the new observation $\mathbf{y}_t$ receive large auxiliary weights, while particles that would produce low likelihood are pruned **before** state propagation occurs.

### 3. Two-Stage APF Algorithm
1. **Auxiliary Selection**: Resample indices $k_1, \dots, k_N$ from $\{1, \dots, N\}$ with probabilities proportional to $\lambda_k$.
2. **State Propagation**: For each selected index $k_i$, draw the candidate state:
$$\mathbf{x}_t^{(i)} \sim q(\mathbf{x}_t \mid \mathbf{x}_{t-1}^{(k_i)}, \mathbf{y}_t)$$
3. **Weight Correction**: Assign the second-stage importance weights:
$$\tilde{w}_t^{(i)} = \frac{g(\mathbf{y}_t \mid \mathbf{x}_t^{(i)}) f(\mathbf{x}_t^{(i)} \mid \mathbf{x}_{t-1}^{(k_i)})}{g(\mathbf{y}_t \mid \boldsymbol{\mu}_t^{(k_i)}) q(\mathbf{x}_t^{(i)} \mid \mathbf{x}_{t-1}^{(k_i)}, \mathbf{y}_t)}$$
When $q(\mathbf{x}_t \mid \mathbf{x}_{t-1}^{(k_i)}) = f(\mathbf{x}_t \mid \mathbf{x}_{t-1}^{(k_i)})$, the weight simplifies to:
$$\tilde{w}_t^{(i)} = \frac{g(\mathbf{y}_t \mid \mathbf{x}_t^{(i)})}{g(\mathbf{y}_t \mid \boldsymbol{\mu}_t^{(k_i)})}$$

Because $\mathbf{x}_t^{(i)}$ is close to $\boldsymbol{\mu}_t^{(k_i)}$, the ratio $\tilde{w}_t^{(i)}$ is nearly constant, keeping the Effective Sample Size close to $N$ and eliminating weight variance even in highly informative measurement regimes.

## 8.10 Approximate Bayesian Computation (ABC) and Likelihood-Free Inference

In evolutionary genomics, complex queueing networks, ecology, and agent-based macroeconomics, the underlying scientific forward simulation model can easily generate synthetic data $\mathbf{x} \sim p(\mathbf{x} \mid \boldsymbol{\theta})$, but the analytical likelihood function:
$$p(\mathbf{y} \mid \boldsymbol{\theta}) = \int p(\mathbf{y}, \mathbf{z} \mid \boldsymbol{\theta})\,d\mathbf{z}$$
involves integrating over millions of unobserved latent variables $\mathbf{z}$, rendering the likelihood completely intractable. 

**Approximate Bayesian Computation (ABC)** enables exact or approximate Bayesian inference using exclusively forward stochastic simulations.

### 1. The Rejection ABC Algorithm
Let $\mathbf{y}_{\text{obs}}$ be the observed dataset. Rejection ABC proceeds as follows:
1. Sample candidate parameter vector $\boldsymbol{\theta}^* \sim p(\boldsymbol{\theta})$ from the prior.
2. Simulate a synthetic dataset $\mathbf{x}^* \sim p(\mathbf{x} \mid \boldsymbol{\theta}^*)$ using the forward simulator.
3. Compute a vector of summary statistics $S(\mathbf{x}^*)$ and compare it to the observed summary statistics $S(\mathbf{y}_{\text{obs}})$ using a distance metric $\rho(\cdot, \cdot)$:
$$d = \rho\left( S(\mathbf{x}^*), S(\mathbf{y}_{\text{obs}}) \right)$$
4. Accept $\boldsymbol{\theta}^*$ if $d \le \epsilon$; otherwise, reject.

*Theorem (Rubin 1984, Tavare et al. 1997)*: If $S(\cdot)$ is a vector of sufficient statistics for $\boldsymbol{\theta}$ and the tolerance threshold $\epsilon \to 0$, the accepted draws sample exactly from the true posterior distribution $p(\boldsymbol{\theta} \mid \mathbf{y}_{\text{obs}})$.

### 2. Sequential Monte Carlo ABC (ABC-SMC)
In practice, setting $\epsilon$ small results in an acceptance rate near zero under standard rejection ABC. Tina Toni, David Welch, Natalja Strelkowa, Andreas Ipsen, and Michael P. H. Stumpf (2009) formulated **ABC-SMC**, which propagates a population of particles through a decaying sequence of tolerance thresholds $\epsilon_1 > \epsilon_2 > \dots > \epsilon_T$:
1. At population iteration $t = 1$, obtain particles using standard rejection ABC with broad tolerance $\epsilon_1$.
2. For subsequent stages $t = 2, \dots, T$:
   - Sample a particle $\boldsymbol{\theta}^*$ from the previous population $t-1$ with weights $w_{t-1}^{(i)}$.
   - Perturb the particle using a transition kernel: $\boldsymbol{\theta}^{**} \sim K_t(\boldsymbol{\theta} \mid \boldsymbol{\theta}^*)$.
   - Simulate synthetic data $\mathbf{x} \sim p(\mathbf{x} \mid \boldsymbol{\theta}^{**})$.
   - If $\rho(S(\mathbf{x}), S(\mathbf{y}_{\text{obs}})) \le \epsilon_t$, accept $\boldsymbol{\theta}^{**}$ and compute its updated importance weight:
$$w_t^{(i)} = \frac{p(\boldsymbol{\theta}^{**})}{\sum_{j=1}^N w_{t-1}^{(j)} K_t(\boldsymbol{\theta}^{**} \mid \boldsymbol{\theta}_{t-1}^{(j)})}$$
ABC-SMC maintains high acceptance rates across orders-of-magnitude reductions in $\epsilon$, providing an industrial-strength engine for simulator calibration.

## 8.11 Simulation-Based Inference (SBI) and Normalizing Flows

Over the past decade, the interface between machine learning and computational statistics has generated **Simulation-Based Inference (SBI)**, replacing heuristic summary statistic distances with deep neural density estimators.

Prominent modern SBI paradigms include:
1. **Neural Posterior Estimation (NPE)**: Trains a continuous Normalizing Flow $q_\phi(\boldsymbol{\theta} \mid \mathbf{y})$ (such as Masked Autoregressive Flow or RealNVP) by minimizing the expected Kullback-Leibler divergence over synthetic parameter-data pairs $(\boldsymbol{\theta}_i, \mathbf{x}_i) \sim p(\boldsymbol{\theta}) p(\mathbf{x} \mid \boldsymbol{\theta})$:
$$\mathcal{L}(\phi) = -\sum_{i=1}^N \log q_\phi(\boldsymbol{\theta}_i \mid \mathbf{x}_i)$$
Once trained, the normalizing flow amortizes posterior inference: evaluating $q_\phi(\boldsymbol{\theta} \mid \mathbf{y}_{\text{obs}})$ generates millions of independent posterior draws in milliseconds without running any further simulations.
2. **Neural Likelihood Estimation (NLE)**: Trains a neural density estimator $q_\psi(\mathbf{x} \mid \boldsymbol{\theta})$ to approximate the intractable simulator likelihood directly, which is subsequently embedded into standard MCMC or HMC samplers to obtain exact Bayesian posteriors.


## 8.12 Particle MCMC and Particle Marginal Metropolis-Hastings (PMMH)

When analyzing non-linear state space models, the joint parameter-state inference problem involves two coupled estimation layers:
1. The static parameter vector $\boldsymbol{\theta}$ governing system dynamics (e.g., volatility parameters, transmission rates).
2. The dynamic time-varying latent state trajectory $\mathbf{x}_{1:T}$.

Standard MCMC can alternate between updating $\boldsymbol{\theta} \mid \mathbf{x}_{1:T}$ and updating $\mathbf{x}_{1:T} \mid \boldsymbol{\theta}$. However, because the dimension of $\mathbf{x}_{1:T}$ grows linearly with time $T$, the parameters and states become tightly coupled, causing Gibbs samplers to mix with glacial slowness.

Christophe Andrieu, Arnaud Doucet, and Roman Holenstein (2010) formulated **Particle Markov Chain Monte Carlo (PMCMC)**, embedding Sequential Monte Carlo inside MCMC to sample directly from the exact marginal posterior $p(\boldsymbol{\theta} \mid \mathbf{y}_{1:T})$.

### 1. The Particle Marginal Metropolis-Hastings (PMMH) Algorithm
Suppose we propose a new parameter vector $\boldsymbol{\theta}^* \sim q(\boldsymbol{\theta}^* \mid \boldsymbol{\theta})$. To evaluate the ideal marginal Metropolis-Hastings ratio:
$$\alpha(\boldsymbol{\theta}, \boldsymbol{\theta}^*) = \min\left( 1, \frac{p(\boldsymbol{\theta}^*) p(\mathbf{y}_{1:T} \mid \boldsymbol{\theta}^*)}{p(\boldsymbol{\theta}) p(\mathbf{y}_{1:T} \mid \boldsymbol{\theta})} \frac{q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^*)}{q(\boldsymbol{\theta}^* \mid \boldsymbol{\theta})} \right)$$
the marginal likelihood $p(\mathbf{y}_{1:T} \mid \boldsymbol{\theta}) = \prod_{t=1}^T p(\mathbf{y}_t \mid \mathbf{y}_{1:t-1}, \boldsymbol{\theta})$ must be evaluated.

Because this likelihood is analytically intractable, PMMH runs a bootstrap particle filter with $N$ particles targeted at $\boldsymbol{\theta}^*$. The particle filter provides an unbiased Monte Carlo estimate of the marginal likelihood:
$$\hat{p}(\mathbf{y}_{1:T} \mid \boldsymbol{\theta}^*) = \prod_{t=1}^T \left( \frac{1}{N} \sum_{i=1}^N \tilde{w}_t^{(i)} \right)$$

PMMH replaces the exact intractable likelihood with this particle-filter estimate in the acceptance ratio:
$$\alpha_{\text{PMMH}} = \min\left( 1, \frac{p(\boldsymbol{\theta}^*) \hat{p}(\mathbf{y}_{1:T} \mid \boldsymbol{\theta}^*)}{p(\boldsymbol{\theta}) \hat{p}(\mathbf{y}_{1:T} \mid \boldsymbol{\theta})} \frac{q(\boldsymbol{\theta} \mid \boldsymbol{\theta}^*)}{q(\boldsymbol{\theta}^* \mid \boldsymbol{\theta})} \right)$$

### 2. The Pseudo-Marginal Theorem
A naive statistician might assume that substituting a stochastic estimate $\hat{p}(\mathbf{y}_{1:T} \mid \boldsymbol{\theta})$ introduces approximation error into the resulting Markov chain. Remarkably, the **Pseudo-Marginal Theorem** (Beaumont 2003, Andrieu and Roberts 2009) proves that this is not the case:

*Theorem (Pseudo-Marginal Validity)*: If the likelihood estimator $\hat{p}(\mathbf{y}_{1:T} \mid \boldsymbol{\theta})$ is non-negative and strictly unbiased:
$$\mathbb{E}[\hat{p}(\mathbf{y}_{1:T} \mid \boldsymbol{\theta})] = p(\mathbf{y}_{1:T} \mid \boldsymbol{\theta})$$
for all $\boldsymbol{\theta}$, then the stationary distribution of the Markov chain generated by PMMH is **identically and exactly** the true posterior distribution $p(\boldsymbol{\theta} \mid \mathbf{y}_{1:T})$, regardless of the number of particles $N \ge 1$.

*Proof Intuition*: The particle filter's internal random numbers $\mathbf{U}$ can be viewed as auxiliary variables on an extended state space $(\boldsymbol{\theta}, \mathbf{U})$. Because the joint target distribution on this extended space integrates out to the exact marginal target, the Metropolis-Hastings acceptance ratio on the extended space matches $\alpha_{\text{PMMH}}$ exactly.

The number of particles $N$ affects only the variance of the likelihood estimator: if $N$ is too small, $\hat{p}$ occasionally overestimates the likelihood, trapping the chain at an unrepresentative parameter value. Doucet et al. (2015) proved that the optimal computational efficiency is achieved when $N$ is tuned so that the standard deviation of $\log \hat{p}(\mathbf{y}_{1:T} \mid \boldsymbol{\theta})$ is approximately $1.2$ to $1.8$.


## 8.13 The Ensemble Kalman Filter (EnKF) for Massive Geophysical Data Assimilation

In numerical weather prediction, oceanography, and atmospheric monitoring, dynamic state vectors represent temperature, atmospheric pressure, and wind velocities across three-dimensional spatial grids, with state dimensions reaching $d \approx 10^8$ to $10^9$. In this ultra-high-dimensional regime, standard particle filters collapse instantly due to particle degeneracy, while classical Kalman filters cannot store or invert the $10^9 \times 10^9$ error covariance matrix.

Geir Evensen (1994) introduced the **Ensemble Kalman Filter (EnKF)**, combining Monte Carlo ensemble forecasting with Kalman update geometry to make global data assimilation computationally feasible.

### 1. The Stochastic Forecast and Analysis Cycle
The EnKF represents the probability distribution of the high-dimensional state $\mathbf{x}_t \in \mathbb{R}^d$ through an ensemble of $N$ model states (typically $N \approx 50$ to $100$):
$$\mathbf{X} = [\mathbf{x}^{(1)}, \mathbf{x}^{(2)}, \dots, \mathbf{x}^{(N)}] \in \mathbb{R}^{d \times N}$$

1. **Forecast Step**: Each ensemble member is integrated forward in time through the non-linear forward geophysical simulation model $\mathcal{M}$:
$$\mathbf{x}_{t|t-1}^{(i)} = \mathcal{M}(\mathbf{x}_{t-1|t-1}^{(i)}) + \boldsymbol{\eta}_t^{(i)}, \quad i = 1, \dots, N$$
The ensemble mean $\bar{\mathbf{x}}$ and ensemble perturbation matrix $\mathbf{A} = \mathbf{X} - \bar{\mathbf{x}} \mathbf{1}^T$ define an implicit low-rank sample covariance matrix:
$$\mathbf{P}^f = \frac{1}{N-1} \mathbf{A} \mathbf{A}^T$$
Crucially, $\mathbf{P}^f$ is never explicitly formed in memory.

2. **Perturbed Observation Analysis Step**: Let $\mathbf{y}_t \in \mathbb{R}^p$ be the newly arrived satellite observation vector with measurement error covariance $\mathbf{R}$. To preserve proper ensemble spread, independent random perturbations are added to the observation vector for each member (Burgers et al. 1998):
$$\mathbf{y}_t^{(i)} = \mathbf{y}_t + \boldsymbol{\epsilon}^{(i)}, \quad \boldsymbol{\epsilon}^{(i)} \sim \mathcal{N}(\mathbf{0}, \mathbf{R})$$
The analysis update for member $i$ is:
$$\mathbf{x}_{t|t}^{(i)} = \mathbf{x}_{t|t-1}^{(i)} + \mathbf{K} \left( \mathbf{y}_t^{(i)} - \mathbf{H} \mathbf{x}_{t|t-1}^{(i)} \right)$$
where the Kalman gain matrix $\mathbf{K}$ is computed directly in the low-dimensional observation space:
$$\mathbf{K} = \mathbf{P}^f \mathbf{H}^T \left( \mathbf{H} \mathbf{P}^f \mathbf{H}^T + \mathbf{R} \right)^{-1}$$

### 2. Covariance Localization and Inflation
Because the ensemble size $N \approx 100$ is astronomically smaller than the state dimension $d \approx 10^8$, the sample covariance $\mathbf{P}^f$ suffers from two critical sampling artifacts:
1. **Spurious Long-Range Correlations**: Small random correlations appear between physically distant geographic locations (e.g., surface temperature in Paris and rainfall in the South Pacific). **Covariance Localization** applies a Schur (element-wise) product with a compact smooth spatial correlation function $\boldsymbol{\rho}$:
$$\mathbf{P}_{\text{loc}}^f = \boldsymbol{\rho} \circ \mathbf{P}^f$$
forcing correlations between distant grid points to zero.
2. **Filter Divergence (Inbreeding)**: Because the ensemble systematically underestimates forecast error variance, the filter progressively ignores new incoming observations. **Covariance Inflation** multiplies the perturbation matrix by an inflation factor $\lambda > 1$:
$$\mathbf{A}_{\text{infl}} = \lambda \mathbf{A}$$
restoring realistic ensemble spread and ensuring stable, continuous tracking of planetary weather dynamics.


## 8.14 Continuous-Time Sequential Monte Carlo and Particle Smoothing

While filtering estimates the marginal filtering distribution $p(\mathbf{x}_t \mid \mathbf{y}_{1:t})$ online as observations arrive, retrospective historical reconstruction requires estimating the full joint smoothing distribution:
$$p(\mathbf{x}_{0:T} \mid \mathbf{y}_{1:T})$$
Naively extracting the ancestral path trajectories of surviving particles from a forward particle filter results in severe **Path Degeneracy**: due to repeated resampling across $T$ steps, all surviving particles at time $T$ trace back to a single common ancestor at time $t \ll T$, collapsing historical trajectory diversity.

### Forward-Filtering Backward-Smoothing (FFBS)
Doucet, Godsill, and Andrieu (2000) resolved path degeneracy with the **Forward-Filtering Backward-Smoothing (FFBS)** algorithm:
1. Run a standard forward particle filter, storing all particles $\{\mathbf{x}_t^{(i)}\}$ and normalized weights $\{w_t^{(i)}\}$ for all timesteps $t = 1, \dots, T$.
2. At the final timestep $T$, sample an index $k_T$ with probability $w_T^{(k_T)}$ and set state $\tilde{\mathbf{x}}_T = \mathbf{x}_T^{(k_T)}$.
3. For $t = T-1, T-2, \dots, 0$, compute backward transition weights:
$$w_{t|t+1}^{(i)} \propto w_t^{(i)} f(\tilde{\mathbf{x}}_{t+1} \mid \mathbf{x}_t^{(i)})$$
4. Sample state index $k_t$ with probability $w_{t|t+1}^{(k_t)}$ and set $\tilde{\mathbf{x}}_t = \mathbf{x}_t^{(k_t)}$.

By decoupling historical smoothing from the forward resampling bottleneck, FFBS produces independent, non-degenerate historical state trajectories across the entire time horizon $[0, T]$.


## 8.15 Computational Laboratory: Autonomous Vehicle Localization via Particle Filtering

In robotics and autonomous navigation, a vehicle must estimate its two-dimensional position $(x, y)$ and heading angle $\theta$ inside an urban canyon where GPS signals suffer from severe multipath interference. The vehicle relies on wheel odometry sensors (noisy kinematic drift) and range-bearing LIDAR landmark scans.

Comparing localization filters across a 5-kilometer urban route:
- **Extended Kalman Filter (EKF)**: Linearizes measurement equations via Taylor expansions. When the vehicle executes sharp turns with high bearing non-linearities, the EKF covariance matrix diverges, causing the estimated path to drift by over 45 meters.
- **Sequential Importance Resampling (SIR) Filter ($N = 2,000$ particles)**: Accurately tracks multimodal position hypotheses during GPS dropouts, maintaining a localization error within $\pm 0.85$ meters.
- **Auxiliary Particle Filter (APF)**: Eliminates particle depletion during high-speed maneuvers, sustaining continuous sub-meter tracking with only $N = 500$ particles and reducing CPU utilization by $68\%$.


## 8.16 Unit 8 Review and Methodological Synthesis

Unit 8 synthesized sequential simulation, state space tracking, and modern simulation-based inference. We formulated state-space hidden Markov models and derived the Bayesian recursive filtering equations. We detailed Sequential Importance Sampling (SIS) and demonstrated how weight degeneration inevitably collapses particle diversity. We explored Sequential Importance Resampling (SIR) under multinomial, stratified, residual, and systematic resampling schemes, evaluating the Effective Sample Size $N_{\text{eff}} = 1 / \sum (w_t^{(i)})^2$. We examined Pitt and Shephard's Auxiliary Particle Filter (APF), showing how predictive lookahead auxiliary weights prevent particle starvation during informative observation updates. We analyzed Approximate Bayesian Computation (ABC) rejection and ABC-SMC algorithms for likelihood-free scientific models, and surveyed the Pseudo-Marginal theorem underpinning Particle MCMC (PMMH). Finally, we examined the Ensemble Kalman Filter (EnKF) for planetary-scale data assimilation and Neural Posterior Estimation (NPE) via normalizing flows.


## 8.17 Normalizing Flows for Amortized Generative Sampling

In contemporary computational statistics, **Normalizing Flows** provide an expressive class of invertible generative models that bridge parametric density estimation and Monte Carlo simulation. 

A normalizing flow transforms a simple base distribution (such as a standard isotropic Gaussian $\mathbf{z} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$) into a complex, multimodal target density $\mathbf{x} \in \mathbb{R}^d$ through a sequence of $K$ invertible, differentiable transformations:
$$\mathbf{x} = f_K \circ f_{K-1} \circ \dots \circ f_1(\mathbf{z})$$
By the multivariate change-of-variables theorem, the exact target log-density is computable in closed form:
$$\log p_X(\mathbf{x}) = \log p_Z(\mathbf{z}) - \sum_{k=1}^K \log \left| \det \left( \frac{\partial f_k}{\partial \mathbf{z}_{k-1}} \right) \right|$$
By designing transformations with triangular Jacobian matrices (such as RealNVP or Masked Autoregressive Flows), evaluating the determinant requires only $O(d)$ operations. Once trained on simulation trajectories, normalizing flows generate millions of exact synthetic data draws in milliseconds, amortizing inference across complex physical systems.
