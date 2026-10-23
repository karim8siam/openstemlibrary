# Unit 8: Multi-Sample Nonparametrics, Rank Correlation & Resampling: Kruskal-Wallis, Friedman, Kendall & Permutation

In classical parametric analysis of variance (ANOVA) and Pearson correlation analysis, exact finite-sample distributional results rely heavily on the assumption that experimental observations are drawn from Gaussian populations with homogeneous variances. When multi-group experimental data arise from heavy-tailed distributions, skewed survival or income processes, ordinal rating scales, or small samples contaminated by gross outliers, parametric $F$-tests and product-moment correlation tests suffer severe losses in Pitman asymptotic relative efficiency and exhibit distorted Type I error rates. In this concluding unit, we extend distribution-free rank-based methodology and modern computational resampling from two-sample comparisons to general $k$-sample experimental designs ($k \ge 3$), multivariate rank association, and permutation-based randomization inference.

We begin by developing William Kruskal and W. Allen Wallis's (1952) one-way analysis of variance by ranks ($H$-test) as the multi-sample generalization of the Wilcoxon–Mann–Whitney test, establishing its exact permutation moments, midrank tie correction, asymptotic $\chi^2_{k-1}$ distribution via multivariate central limit theory for rank sums, and olive-Jean Dunn's (1964) multiple comparison procedure. Next, we analyze two-way randomized complete block designs via Milton Friedman's (1937) intra-block rank test, Ronald Iman and James Davenport's (1980) $F$-approximation, and William Cochran's (1950) $Q$-test for matched dichotomous responses, linking blocked rank sums directly to Maurice Kendall and Bernard Babington Smith's (1939) Coefficient of Concordance $W$. We then construct high-power tests tailored specifically to **ordered monotonic alternatives** ($\theta_1 \le \theta_2 \le \dots \le \theta_k$)—namely, the Jonckheere–Terpstra test for independent samples and Ellis Page's (1963) $L$-test for blocked designs. Following a rigorous treatment of Spearman's rank correlation $\rho_s$, Kendall's $\tau$ as a Hoeffding $U$-statistic of degree two, and Leo Goodman and William Kruskal's (1954) $\gamma$ for tied contingency tables, we conclude with the mathematical foundations of Ronald Fisher and Edwin Pitman's exact permutation tests under the exchangeability hypothesis, Phipson–Smyth unbiased Monte Carlo randomization $p$-values, and Bradley Efron's bootstrap hypothesis testing framework.

---

## 8.1 One-Way Nonparametric ANOVA: The Kruskal–Wallis $H$-Test, Asymptotic $\chi^2_{k-1}$ Theory, Tie Corrections, and Dunn's Post-Hoc Comparisons

Consider a completely randomized one-way experimental design comparing $k \ge 3$ mutually independent treatment groups or populations. For each group $i \in \{1, 2, \dots, k\}$, we observe an independent random sample $X_{i1}, X_{i2}, \dots, X_{in_i}$ of size $n_i$ drawn from a continuous cumulative distribution function $F_i(x)$, with total combined sample size $N = \sum_{i=1}^k n_i$. Under the location-shift parameterization $F_i(x) = F(x - \theta_i)$, where $F(\cdot)$ is an arbitrary unspecified continuous distribution with median zero, we wish to test the omnibus null hypothesis of identical population distributions against the general shift alternative:

$$H_0: \theta_1 = \theta_2 = \dots = \theta_k \quad (\text{i.e., } F_1(x) = F_2(x) = \dots = F_k(x) \text{ for all } x \in \mathbb{R})$$

$$H_1: \theta_i \neq \theta_\ell \quad \text{for at least one pair } (i, \ell) \in \{1, \dots, k\}^2$$

### Pooling, Ranking, and Exact Moments of Group Rank Sums Under $H_0$

To construct a distribution-free test statistic that is invariant under any strictly increasing monotonic transformation of the measurement scale, William Kruskal and W. Allen Wallis (1952) pooled all $N = \sum_{i=1}^k n_i$ observations into a single combined sample and ordered them from smallest to largest, assigning ranks $1, 2, \dots, N$. Let $R_{ij} = \operatorname{rank}(X_{ij})$ denote the joint rank of the $j$-th observation in the $i$-th group within the combined sample of size $N$. Define the **$i$-th Group Rank Sum** $R_{i\cdot}$ and the **$i$-th Group Mean Rank** $\bar{R}_{i\cdot}$:

$$R_{i\cdot} = \sum_{j=1}^{n_i} R_{ij}, \qquad \bar{R}_{i\cdot} = \frac{R_{i\cdot}}{n_i}, \qquad \text{with grand mean rank } \bar{R}_{\cdot\cdot} = \frac{1}{N}\sum_{i=1}^k R_{i\cdot} = \frac{1}{N}\sum_{r=1}^N r = \frac{N + 1}{2}$$

Under the null hypothesis $H_0$ and continuity of $F$, all $N!$ rank permutations of $\{1, 2, \dots, N\}$ are equally likely, and the $\frac{N!}{n_1! n_2! \cdots n_k!}$ partitions of the integer set $\{1, 2, \dots, N\}$ into $k$ subsets of sizes $n_1, \dots, n_k$ occur with uniform probability $\frac{n_1! n_2! \cdots n_k!}{N!}$. Thus, for each group $i$, the set of ranks $\{R_{i1}, \dots, R_{in_i}\}$ constitutes a **Simple Random Sample Without Replacement (SRSWOR)** of size $n_i$ drawn from the finite population $\{1, 2, \dots, N\}$. Using the exact first and second moments of a finite population with mean $\mu_R = \frac{N+1}{2}$ and finite-population variance $\sigma_R^2 = \frac{1}{N}\sum_{r=1}^N \left(r - \frac{N+1}{2}\right)^2 = \frac{N^2 - 1}{12}$, we obtain the exact finite-sample expectation, variance, and covariance of the group mean ranks $\bar{R}_{i\cdot}$ under $H_0$:

$$\mathbb{E}_{H_0}\left[\bar{R}_{i\cdot}\right] = \frac{N + 1}{2}, \qquad \mathbb{E}_{H_0}\left[R_{i\cdot}\right] = \frac{n_i(N + 1)}{2}$$

$$\operatorname{Var}_{H_0}\left(\bar{R}_{i\cdot}\right) = \frac{\sigma_R^2}{n_i} \left(\frac{N - n_i}{N - 1}\right) = \frac{N^2 - 1}{12 n_i}\left(\frac{N - n_i}{N - 1}\right) = \frac{(N + 1)(N - n_i)}{12 n_i}$$

$$\operatorname{Cov}_{H_0}\left(\bar{R}_{i\cdot}, \, \bar{R}_{\ell\cdot}\right) = -\frac{\sigma_R^2}{N - 1} = -\frac{N + 1}{12} \qquad (i \neq \ell)$$

### Derivation of the Kruskal–Wallis $H$-Statistic and Its Computational Shortcut

If the classical one-way ANOVA between-group sum of squares $\text{SSB}_R = \sum_{i=1}^k n_i \left(\bar{R}_{i\cdot} - \bar{R}_{\cdot\cdot}\right)^2 = \sum_{i=1}^k n_i \left(\bar{R}_{i\cdot} - \frac{N+1}{2}\right)^2$ is scaled by the total rank variance divisor $\frac{N(N+1)}{12}$ (noting that $\operatorname{Var}_{H_0}\left(\sqrt{n_i}(\bar{R}_{i\cdot} - \frac{N+1}{2})\right) = \frac{N(N+1)}{12}\left(1 - \frac{n_i}{N}\right)$), we obtain the **Kruskal–Wallis $H$-Statistic**:

$$H = \frac{12}{N(N + 1)} \sum_{i=1}^k n_i \left( \bar{R}_{i\cdot} - \frac{N + 1}{2} \right)^2$$

Wait: Why does the coefficient $\frac{12}{N(N+1)}$ appear rather than the naive standardized sum $\sum_{i=1}^k \frac{(\bar{R}_{i\cdot} - \mathbb{E}[\bar{R}_{i\cdot}])^2}{\operatorname{Var}(\bar{R}_{i\cdot})}$? Because the vector of centered rank averages $\mathbf{Z} = \left(\bar{R}_{1\cdot} - \frac{N+1}{2}, \dots, \bar{R}_{k\cdot} - \frac{N+1}{2}\right)^\top$ satisfies the linear dependency $\sum_{i=1}^k n_i Z_i = 0$, its $k \times k$ covariance matrix $\boldsymbol{\Sigma}_Z$ has rank $k - 1$ with generalized inverse $\boldsymbol{\Sigma}_Z^- = \frac{12}{N(N+1)}\operatorname{diag}(n_1, n_2, \dots, n_k)$! Thus, $H = \mathbf{Z}^\top \boldsymbol{\Sigma}_Z^- \mathbf{Z}$ is the exact Mahalanobis quadratic form of the rank means. Expanding the square inside $H$ yields the computationally convenient **hand-calculation shortcut formula**:

$$\sum_{i=1}^k n_i \left(\bar{R}_{i\cdot} - \frac{N+1}{2}\right)^2 = \sum_{i=1}^k n_i \bar{R}_{i\cdot}^2 - (N+1)\sum_{i=1}^k n_i \bar{R}_{i\cdot} + \frac{(N+1)^2}{4}\sum_{i=1}^k n_i = \sum_{i=1}^k \frac{R_{i\cdot}^2}{n_i} - \frac{N(N+1)^2}{4}$$

Multiplying through by $\frac{12}{N(N+1)}$ gives:

$$H = \left[ \frac{12}{N(N + 1)} \sum_{i=1}^k \frac{R_{i\cdot}^2}{n_i} \right] - 3(N + 1)$$

By the multivariate Hájek–Wald–Wolfowitz Central Limit Theorem for linear rank statistics, as $\min_{1 \le i \le k} n_i \to \infty$ with $\frac{n_i}{N} \to \lambda_i \in (0, 1)$, the quadratic form $H$ converges in distribution under $H_0$ to a central Chi-square distribution with $k - 1$ degrees of freedom:

$$H \;\underset{H_0}{\xrightarrow{d}}\; \chi^2_{k - 1}$$

We reject $H_0$ at significance level $\alpha$ if $H \ge \chi^2_{\alpha, \, k - 1}$ (or if $H$ exceeds the exact permutation critical value for small $n_i \le 5$). Under Gaussian distributions, the Pitman Asymptotic Relative Efficiency (ARE) of the Kruskal–Wallis test relative to the parametric one-way ANOVA $F$-test is $\frac{3}{\pi} \approx 0.9549$ ($95.5\%$), while for Laplace (double exponential) errors its ARE is $1.50$ ($150\%$) and for heavy-tailed distributions it never falls below $0.864$!

### Exact Variance Adjustment for Tied Observations ($H_{\text{adj}}$)

When ties occur among the $N$ observations and each tied group of size $t_g$ ($g = 1, \dots, G$, where $t_g$ is the number of observations tied at the $g$-th distinct value) is assigned the average midrank, the mean of the ranks remains $\frac{N+1}{2}$, but the finite-population variance of the $N$ midranks is strictly reduced from $\frac{N^2 - 1}{12}$ by $\frac{\sum_{g=1}^G (t_g^3 - t_g)}{12 N}$:

$$\sigma_{R,\text{tied}}^2 = \frac{N^2 - 1}{12} - \frac{\sum_{g=1}^G \left(t_g^3 - t_g\right)}{12 N} = \frac{N^2 - 1}{12}\left[ 1 - \frac{\sum_{g=1}^G \left(t_g^3 - t_g\right)}{N^3 - N} \right]$$

Dividing the unadjusted $H$ statistic by the **tie-correction factor** $C_{\text{ties}} = 1 - \frac{\sum_{g=1}^G (t_g^3 - t_g)}{N^3 - N} \in (0, 1]$ yields the **Tie-Adjusted Kruskal–Wallis Statistic**:

$$H_{\text{adj}} = \frac{H}{1 - \frac{\sum_{g=1}^G \left(t_g^3 - t_g\right)}{N^3 - N}}$$

Because $C_{\text{ties}} < 1$ whenever at least one tie is present ($t_g \ge 2 \implies t_g^3 - t_g \ge 6$), $H_{\text{adj}} > H$, so failing to correct for ties makes the unadjusted $H$ test slightly conservative.

### Dunn's (1964) Post-Hoc Multiple Comparisons Procedure

When the omnibus Kruskal–Wallis test rejects $H_0$, we identify which specific pairs of groups $(i, \ell)$ differ significantly using Olive Jean Dunn's (1964) joint-rank multiple comparison test. Under $H_0$, the difference between the $i$-th and $\ell$-th group mean ranks $\bar{R}_{i\cdot} - \bar{R}_{\ell\cdot}$ has exact variance:

$$\operatorname{Var}_{H_0}\left(\bar{R}_{i\cdot} - \bar{R}_{\ell\cdot}\right) = \operatorname{Var}_{H_0}(\bar{R}_{i\cdot}) + \operatorname{Var}_{H_0}(\bar{R}_{\ell\cdot}) - 2\operatorname{Cov}_{H_0}(\bar{R}_{i\cdot}, \bar{R}_{\ell\cdot}) = \left[ \frac{N(N + 1)}{12} - \frac{\sum_{g=1}^G (t_g^3 - t_g)}{12(N - 1)} \right] \left( \frac{1}{n_i} + \frac{1}{n_\ell} \right)$$

Thus, **Dunn's Standardized $Z$-Statistic** for comparing Group $i$ and Group $\ell$ is:

$$Z_{i\ell} = \frac{\left|\bar{R}_{i\cdot} - \bar{R}_{\ell\cdot}\right|}{\sqrt{\left[ \frac{N(N + 1)}{12} - \frac{\sum_{g=1}^G (t_g^3 - t_g)}{12(N - 1)} \right] \left( \frac{1}{n_i} + \frac{1}{n_\ell} \right)}} \;\underset{H_0}{\xrightarrow{d}}\; |\mathcal{N}(0, 1)|$$

To control the Family-Wise Error Rate (FWER) at level $\alpha$ across all $M = \binom{k}{2} = \frac{k(k-1)}{2}$ pairwise comparisons, Dunn applied the Bonferroni inequality (or Holm's step-down procedure), declaring Group $i$ and Group $\ell$ significantly different if $Z_{i\ell} \ge z_{\alpha / (2M)} = z_{\alpha / [k(k-1)]}$.

---

## 8.2 Nonparametric Randomized Complete Block Designs: Friedman's Two-Way Rank Test, Iman–Davenport $F$-Approximation, and Cochran's $Q$-Test

In many agricultural, industrial, clinical, and psychological experiments, observations are arranged in a **Randomized Complete Block Design (RCBD)** (or a repeated-measures design) in which $b$ homogeneous blocks (or subjects) are each evaluated across all $k$ treatments. Let $X_{ij}$ denote the response of block $i \in \{1, \dots, b\}$ under treatment $j \in \{1, \dots, k\}$:

$$X_{ij} = \mu + \beta_i + \tau_j + \varepsilon_{ij}, \qquad i = 1, \dots, b; \quad j = 1, \dots, k$$

where $\beta_i$ is the nuisance block effect and $\tau_j$ is the treatment effect of interest. We wish to test $H_0: \tau_1 = \tau_2 = \dots = \tau_k = 0$ against $H_1: \text{not all } \tau_j \text{ are equal}$, without assuming normality of the errors $\varepsilon_{ij}$.

### Intra-Block Ranking and Derivation of Friedman's $Q_F$ Statistic (1937)

Because block effects $\beta_i$ vary arbitrarily across blocks, pooling all $b k$ observations together (as in Kruskal–Wallis) would confound treatment differences with inter-block heterogeneity. Instead, Milton Friedman (1937) eliminated the additive block effect $\beta_i$ completely by **ranking observations separately within each block**:
- Within block $i$, order $X_{i1}, X_{i2}, \dots, X_{ik}$ from smallest to largest and assign **intra-block ranks** $r_{i1}, r_{i2}, \dots, r_{ik} \in \{1, 2, \dots, k\}$ (assigning midranks if ties occur within block $i$).
- Compute the **$j$-th Treatment Rank Sum** $R_{\cdot j}$ and **Treatment Mean Rank** $\bar{R}_{\cdot j}$ across the $b$ blocks:

$$R_{\cdot j} = \sum_{i=1}^b r_{ij}, \qquad \bar{R}_{\cdot j} = \frac{R_{\cdot j}}{b}, \qquad \text{with grand mean } \bar{r}_{\cdot\cdot} = \frac{k + 1}{2} \quad \text{and} \quad \sum_{j=1}^k R_{\cdot j} = \frac{b k(k + 1)}{2}$$

Under $H_0$, within each independent block $i$, the rank vector $(r_{i1}, \dots, r_{ik})$ is uniformly distributed over all $k!$ permutations of $\{1, \dots, k\}$, with $\mathbb{E}[r_{ij}] = \frac{k+1}{2}$, $\operatorname{Var}(r_{ij}) = \frac{k^2 - 1}{12}$, and $\operatorname{Cov}(r_{ij}, r_{i\ell}) = -\frac{k+1}{12}$ ($j \neq \ell$). Summing across the $b$ mutually independent blocks yields:

$$\mathbb{E}_{H_0}\left[R_{\cdot j}\right] = \frac{b(k + 1)}{2}, \qquad \operatorname{Var}_{H_0}\left(R_{\cdot j}\right) = \frac{b(k^2 - 1)}{12}, \qquad \operatorname{Cov}_{H_0}\left(R_{\cdot j}, R_{\cdot\ell}\right) = -\frac{b(k + 1)}{12}$$

Scaling the between-treatment sum of squares $\sum_{j=1}^k b\left(\bar{R}_{\cdot j} - \frac{k+1}{2}\right)^2 = \frac{1}{b}\sum_{j=1}^k \left(R_{\cdot j} - \frac{b(k+1)}{2}\right)^2$ by $\frac{12}{k(k+1)}$ yields **Friedman's Two-Way Analysis of Variance by Ranks Statistic ($Q_F$ or $\chi^2_r$)**:

$$Q_F = \frac{12 b}{k(k + 1)} \sum_{j=1}^k \left( \bar{R}_{\cdot j} - \frac{k + 1}{2} \right)^2 = \left[ \frac{12}{b k(k + 1)} \sum_{j=1}^k R_{\cdot j}^2 \right] - 3b(k + 1) \;\underset{H_0}{\xrightarrow{d}}\; \chi^2_{k - 1} \quad \text{as } b \to \infty$$

If intra-block ties occur in block $i$ with tie group sizes $t_{ig}$ ($g = 1, \dots, G_i$), the tie-adjusted Friedman statistic is:

$$Q_{F,\text{adj}} = \frac{12 \sum_{j=1}^k \left( R_{\cdot j} - \frac{b(k+1)}{2} \right)^2}{b k(k + 1) - \frac{1}{k - 1}\sum_{i=1}^b \sum_{g=1}^{G_i} \left(t_{ig}^3 - t_{ig}\right)}$$

### The Iman–Davenport (1980) $F$-Distribution Improvement

Because the $\chi^2_{k-1}$ approximation to $Q_F$ is noticeably conservative in small-to-moderate block sizes $b$ (since $Q_F$ is bounded above by $b(k - 1)$), Ronald Iman and James Davenport (1980) demonstrated that transforming $Q_F$ into the classical two-way ANOVA $F$-statistic computed directly on the intra-block ranks produces a dramatically more accurate finite-sample approximation:

$$F_{\text{ID}} = \frac{(b - 1) Q_F}{b(k - 1) - Q_F} \;\underset{H_0}{\sim}\; F_{k - 1, \, (b - 1)(k - 1)}$$

Notice that as $Q_F \to b(k - 1)$ (complete agreement of rankings across all $b$ blocks), $F_{\text{ID}} \to \infty$, faithfully reflecting zero residual error variance!

### Cochran's $Q$-Test for Binary ($0/1$) Matched Responses across $k \ge 3$ Treatments (1950)

When the response $X_{ij} \in \{0, 1\}$ is dichotomous ($1 = \text{Success}$, $0 = \text{Failure}$) across $b$ matched subjects or blocks and $k \ge 3$ treatments (extending McNemar's $k = 2$ paired test to $k \ge 3$ treatments), William Cochran (1950) derived the exact conditional randomization test statistic. Let $C_j = \sum_{i=1}^b X_{ij}$ denote the total number of successes under treatment $j$ (column total), and let $L_i = \sum_{j=1}^k X_{ij}$ denote the total number of successes for block $i$ (row total). **Cochran's $Q$-Statistic** is identical to the tie-adjusted Friedman statistic $Q_{F,\text{adj}}$ applied to binary $0/1$ scores:

$$Q_{\text{Cochran}} = \frac{k(k - 1) \sum_{j=1}^k \left(C_j - \bar{C}\right)^2}{k \sum_{i=1}^b L_i - \sum_{i=1}^b L_i^2} = \frac{(k - 1)\left[ k \sum_{j=1}^k C_j^2 - \left(\sum_{j=1}^k C_j\right)^2 \right]}{k \sum_{i=1}^b L_i - \sum_{i=1}^b L_i^2} \;\underset{H_0}{\xrightarrow{d}}\; \chi^2_{k - 1}$$

Notice that blocks with $L_i = 0$ (all $0$s) or $L_i = k$ (all $1$s) contribute $k L_i - L_i^2 = 0$ to the denominator and equal increments to all $C_j$, so concordant rows automatically drop out of Cochran's $Q$, exactly generalizing McNemar's test!

When Friedman's omnibus test (or Cochran's $Q$-test) rejects the null hypothesis $H_0: \tau_1 = \dots = \tau_k$, post-hoc pairwise comparisons between Treatment $j$ and Treatment $\ell$ are conducted using the **Nemenyi–Wilcoxon–Wilcox Multiple Comparison Procedure** or **Conover's (1999) $t$-Test on Intra-Block Ranks**. Under $H_0$, the difference between two treatment rank sums $R_{\cdot j} - R_{\cdot \ell}$ has exact variance $\operatorname{Var}_{H_0}(R_{\cdot j} - R_{\cdot \ell}) = 2\operatorname{Var}_{H_0}(R_{\cdot j}) - 2\operatorname{Cov}_{H_0}(R_{\cdot j}, R_{\cdot \ell}) = \frac{2b(k^2 - 1)}{12} + \frac{2b(k + 1)}{12} = \frac{b k(k + 1)}{6}$, so the standard error of the mean-rank difference $\bar{R}_{\cdot j} - \bar{R}_{\cdot \ell}$ is $\sqrt{\frac{k(k + 1)}{6b}}$. Applying a Bonferroni correction across all $M = \binom{k}{2}$ pairs declares Treatments $j$ and $\ell$ significantly different at family-wise error rate $\alpha$ whenever:

$$\left|R_{\cdot j} - R_{\cdot \ell}\right| \ge z_{\alpha / [k(k-1)]} \sqrt{\frac{b k(k + 1)}{6}} \quad \Longleftrightarrow \quad \left|\bar{R}_{\cdot j} - \bar{R}_{\cdot \ell}\right| \ge \frac{q_{\alpha, \, k, \, \infty}}{\sqrt{2}} \sqrt{\frac{k(k + 1)}{6b}}$$

where $q_{\alpha, k, \infty}$ is the upper-$\alpha$ critical value of the Studentized Range distribution for $k$ groups.

---

## 8.3 Judge Agreement and Inter-Rater Reliability: Kendall's Coefficient of Concordance $W$ and Its Exact Algebra With Friedman's Statistic

Suppose $b$ independent judges (or clinical raters, consumer panels, or machine learning ranking algorithms) each rank $k$ candidate objects (e.g., job applicants, medical images, or competing products) from $1$ to $k$. Rather than testing whether treatments differ as an experimental intervention, our goal is to measure the **degree of inter-rater agreement (concordance)** among the $b$ judges.

Let $R_{\cdot j} = \sum_{i=1}^b r_{ij}$ denote the sum of ranks assigned to object $j$ by the $b$ judges, with mean $\bar{R}_{\cdot} = \frac{b(k+1)}{2}$. Define the **Sum of Squared Deviations of Object Rank Sums ($S$)**:

$$S = \sum_{j=1}^k \left( R_{\cdot j} - \frac{b(k + 1)}{2} \right)^2$$

Let us evaluate the two extreme boundary regimes for $S$:
1. **Complete Disagreement / Maximum Discordance ($S_{\min} = 0$)**: If the $b$ judges disagree in such a completely balanced fashion that every object $j = 1, \dots, k$ receives the exact same total rank sum $R_{\cdot j} = \frac{b(k+1)}{2}$, then $S = 0$.
2. **Perfect Agreement / Complete Concordance ($S = S_{\max}$)**: If all $b$ judges assign identical rankings to the $k$ objects, then after relabeling the objects in increasing order of preference, object $1$ receives rank $1$ from every judge ($R_{\cdot 1} = b$), object $2$ receives rank $2$ from every judge ($R_{\cdot 2} = 2b$), $\dots$, and object $k$ receives rank $k$ from every judge ($R_{\cdot k} = b k$). Therefore, the maximum possible sum of squared deviations is:

$$S_{\max} = \sum_{j=1}^k \left( b j - \frac{b(k + 1)}{2} \right)^2 = b^2 \sum_{j=1}^k \left( j - \frac{k + 1}{2} \right)^2 = b^2 \left[ \frac{k\left(k^2 - 1\right)}{12} \right] = \frac{b^2 k\left(k^2 - 1\right)}{12}$$

### Definition of Kendall's Coefficient of Concordance $W$ (1939)

Maurice Kendall and Bernard Babington Smith (1939) defined **Kendall's Coefficient of Concordance ($W$)** as the ratio of the observed sum of squares $S$ to its theoretical maximum $S_{\max}$:

$$W = \frac{S}{S_{\max}} = \frac{12 \sum_{j=1}^k \left( R_{\cdot j} - \frac{b(k + 1)}{2} \right)^2}{b^2 k\left(k^2 - 1\right)} = \frac{12 \sum_{j=1}^k R_{\cdot j}^2 - 3 b^2 k(k + 1)^2}{b^2 k\left(k^2 - 1\right)} \in [0, 1]$$

When intra-judge ties occur, $S_{\max}$ is reduced by $\frac{b}{12}\sum_{i=1}^b \sum_{g=1}^{G_i}(t_{ig}^3 - t_{ig})$, yielding the tie-corrected coefficient $W_{\text{adj}} = \frac{12 S}{b^2 k(k^2 - 1) - b \sum_{i=1}^b \sum_{g=1}^{G_i}(t_{ig}^3 - t_{ig})}$.

### Exact Algebraic Identities Linking $W$, Friedman's $Q_F$, and Average Pairwise Spearman Correlation $\bar{\rho}_s$

Comparing the numerator and denominator of $W = \frac{12 S}{b^2 k(k^2 - 1)}$ with Friedman's statistic $Q_F = \frac{12 S}{b k(k + 1)}$ reveals a remarkably clean **exact algebraic identity**:

$$Q_F = b(k - 1) W \quad \Longleftrightarrow \quad W = \frac{Q_F}{b(k - 1)}$$

Consequently, testing the null hypothesis of random, independent judge rankings $H_0: W = 0$ is **mathematically identical** to executing Friedman's $\chi^2_{k-1}$ test via $Q_F = b(k - 1)W \sim \chi^2_{k-1}$ (or the Iman–Davenport test $F_{\text{ID}} = \frac{(b - 1)W}{1 - W} \sim F_{k-1, (b-1)(k-1)}$)!

Furthermore, let $\rho_{s}^{(i, m)} = 1 - \frac{6\sum_{j=1}^k (r_{ij} - r_{mj})^2}{k(k^2 - 1)}$ denote Spearman's rank correlation coefficient between judge $i$ and judge $m$, and let $\bar{\rho}_s = \frac{2}{b(b - 1)}\sum_{1 \le i < m \le b} \rho_s^{(i, m)}$ denote the **average of all $\binom{b}{2}$ pairwise Spearman rank correlations** among the $b$ judges. Expanding $\sum_{j=1}^k \left(\sum_{i=1}^b (r_{ij} - \frac{k+1}{2})\right)^2$ into diagonal and off-diagonal terms establishes the exact relationship:

$$W = \frac{(b - 1)\bar{\rho}_s + 1}{b} \quad \Longleftrightarrow \quad \bar{\rho}_s = \frac{b W - 1}{b - 1}$$

Notice why $W \in [0, 1]$ cannot be negative even when judges negatively correlate: because $W \ge 0$, the average correlation among $b$ rankings is bounded below by $\bar{\rho}_s \ge -\frac{1}{b - 1}$! Moreover, when $H_0: W = 0$ is rejected and the judges exhibit statistically significant concordance, Kendall proved that the **optimal consensus ranking**—defined as the permutation $\hat{\boldsymbol{\pi}} \in \mathcal{S}_k$ that minimizes the total sum of squared Spearman rank distances $\sum_{i=1}^b \sum_{j=1}^k (r_{ij} - \pi_j)^2$ across all $b$ judges—is achieved by ordering the $k$ objects in ascending order of their aggregate rank sums $R_{\cdot 1}, R_{\cdot 2}, \dots, R_{\cdot k}$.

---

## 8.4 Testing Against Ordered Alternatives: The Jonckheere–Terpstra Test for Independent Samples and Page's $L$-Test for Blocked Designs

Both the Kruskal–Wallis $H$-test and Friedman's $Q_F$-test are **omnibus tests** whose test statistics are symmetric functions of the group rank sums $(R_{1\cdot}, \dots, R_{k\cdot})$. If we permute the labels of the $k$ treatment groups arbitrarily, $H$ and $Q_F$ remain completely unchanged! However, in dose-response toxicology, educational intervention trials, and economic development studies, the $k$ treatments often correspond to increasing dosage levels $d_1 < d_2 < \dots < d_k$, and the investigator specifically hypothesizes a **monotonic ordered trend**:

$$H_0: \theta_1 = \theta_2 = \dots = \theta_k \quad \text{versus} \quad H_1: \theta_1 \le \theta_2 \le \dots \le \theta_k \quad (\text{with at least one strict inequality } \theta_i < \theta_\ell)$$

Spreading omnibus test power across all $k!$ possible orderings wastes substantial statistical sensitivity when the alternative is restricted to the single monotonic cone $\theta_1 \le \dots \le \theta_k$.

### 1. The Jonckheere–Terpstra ($JT$) Test for Independent Samples (1952, 1954)

Independently proposed by T. J. Terpstra (1952) and A. R. Jonckheere (1954), the **Jonckheere–Terpstra Test** aggregates all $\binom{k}{2} = \frac{k(k-1)}{2}$ pairwise Mann–Whitney count statistics $U_{i\ell}$ comparing each lower-indexed group $i$ against each higher-indexed group $\ell$ ($1 \le i < \ell \le k$):

$$J = \sum_{i=1}^{k-1} \sum_{\ell=i+1}^k U_{i\ell}, \qquad \text{where } U_{i\ell} = \sum_{a=1}^{n_i} \sum_{b=1}^{n_\ell} \left( \mathbf{1}_{\{X_{ia} < X_{\ell b}\}} + \frac{1}{2}\mathbf{1}_{\{X_{ia} = X_{\ell b}\}} \right)$$

Here $U_{i\ell}$ counts the number of pairs $(X_{ia}, X_{\ell b})$ with $i < \ell$ for which the observation in the higher-indexed group $\ell$ exceeds the observation in the lower-indexed group $i$. Under the strictly increasing trend $\theta_1 < \theta_2 < \dots < \theta_k$, each $U_{i\ell}$ exceeds its null expectation $\frac{n_i n_\ell}{2}$, reinforcing constructively across all $\binom{k}{2}$ pairs! Under $H_0$ (with no ties and total sample size $N = \sum_{i=1}^k n_i$), the exact mean and variance of $J$ are:

$$\mathbb{E}_{H_0}[J] = \frac{1}{2}\sum_{1 \le i < \ell \le k} n_i n_\ell = \frac{N^2 - \sum_{i=1}^k n_i^2}{4}$$

$$\operatorname{Var}_{H_0}(J) = \frac{N^2(2N + 3) - \sum_{i=1}^k n_i^2(2n_i + 3)}{72}$$

As $N \to \infty$, the standardized statistic $Z_{\text{JT}} = \frac{J - \mathbb{E}_{H_0}[J]}{\sqrt{\operatorname{Var}_{H_0}(J)}} \xrightarrow{d} \mathcal{N}(0, 1)$, and we reject $H_0$ in favor of an increasing trend if $Z_{\text{JT}} \ge z_\alpha$. Notice that whereas the omnibus Kruskal–Wallis test converts deviations into a $k-1$ degree-of-freedom quadratic form whose non-centrality parameter is diluted by $k - 1$, the Jonckheere–Terpstra statistic concentrates all monotonic trend signal into a **single $1$-degree-of-freedom directional normal score** $Z_{\text{JT}}$ (or equivalently $Z_{\text{JT}}^2 \sim \chi^2_1$). Under linear shift alternatives $\theta_i = i \cdot \Delta / \sqrt{N}$ with Gaussian disturbances, the Pitman Asymptotic Relative Efficiency of the Jonckheere–Terpstra test relative to parametric linear regression on group indices is $\frac{3}{\pi} \approx 0.955$, and its power advantage over Kruskal–Wallis increases monotonically with the number of groups $k$.

### 2. Page's $L$-Test for Ordered Alternatives in Randomized Block Designs (1963)

In a randomized complete block design with $b$ blocks and $k$ treatments ordered *a priori* as $1, 2, \dots, k$ under the monotonic alternative $H_1: \tau_1 \le \tau_2 \le \dots \le \tau_k$, Ellis Batten Page (1963) defined the linear rank contrast statistic **$L$** as the weighted sum of the treatment rank sums $R_{\cdot j} = \sum_{i=1}^b r_{ij}$ weighted by their hypothesized integer order $j \in \{1, 2, \dots, k\}$:

$$L = \sum_{j=1}^k j R_{\cdot j} = 1 R_{\cdot 1} + 2 R_{\cdot 2} + 3 R_{\cdot 3} + \dots + k R_{\cdot k}$$

Why does $L$ focus power on the ordered alternative? Notice that within each block $i$, the linear combination $\sum_{j=1}^k j r_{ij}$ is linearly equivalent to Spearman's rank correlation between the observed intra-block ranks $(r_{i1}, \dots, r_{ik})$ and the hypothesized order $(1, 2, \dots, k)$! Using $\mathbb{E}_{H_0}[R_{\cdot j}] = \frac{b(k+1)}{2}$ and the covariance matrix of $(R_{\cdot 1}, \dots, R_{\cdot k})$, the exact null expectation and variance of $L$ under $H_0$ are:

$$\mathbb{E}_{H_0}[L] = \frac{b(k + 1)}{2}\sum_{j=1}^k j = \frac{b k(k + 1)^2}{4}$$

$$\operatorname{Var}_{H_0}(L) = b \operatorname{Var}_{H_0}\left(\sum_{j=1}^k j r_{1j}\right) = \frac{b k^2(k + 1)\left(k^2 - 1\right)}{144} = \frac{b\left(k^3 - k\right)^2}{144(k - 1)}$$

For moderate or large $b$, the standardized statistic (with continuity correction $-0.5$) is asymptotically standard normal:

$$Z_L = \frac{L - \frac{b k(k + 1)^2}{4}}{\sqrt{\frac{b k^2(k + 1)(k^2 - 1)}{144}}} = \frac{12 L - 3 b k(k + 1)^2}{k(k + 1)\sqrt{b(k - 1)}} \;\underset{H_0}{\xrightarrow{d}}\; \mathcal{N}(0, 1)$$

We reject $H_0$ in favor of the increasing monotonic trend $H_1: \tau_1 \le \dots \le \tau_k$ at level $\alpha$ if $Z_L \ge z_\alpha$. Notice that $Z_L^2 = \frac{[12 L - 3 b k(k+1)^2]^2}{b k^2(k+1)^2(k-1)} \le Q_F$ represents the exact single-degree-of-freedom **linear trend component** extracted from Friedman's $(k-1)$-degree-of-freedom statistic $Q_F$, while the remaining difference $Q_{\text{rem}} = Q_F - Z_L^2 \sim \chi^2_{k-2}$ tests for higher-order non-linear departures from monotonicity!

---

## 8.5 Rank Correlation and Nonparametric Measures of Association: Spearman's $\rho_s$, Kendall's $\tau$ via U-Statistics, and Goodman–Kruskal $\gamma$

Let $(X_1, Y_1), (X_2, Y_2), \dots, (X_n, Y_n)$ be an independent random sample of size $n$ from a bivariate population with joint cumulative distribution function $F_{X,Y}(x, y)$ and marginal distributions $F_X(x)$ and $F_Y(y)$. While Pearson's product-moment correlation $r = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum (X_i - \bar{X})^2 \sum (Y_i - \bar{Y})^2}}$ measures strictly **linear** dependence and is non-robust to outliers or non-linear monotonic transformations (e.g., $Y = e^X$), nonparametric correlation coefficients measure **monotonic association** and are strictly invariant under any order-preserving transformations $X \mapsto g_1(X), Y \mapsto g_2(Y)$.

### 1. Spearman's Rank Correlation Coefficient $\rho_s$ (1904)

Let $R_i = \operatorname{rank}(X_i) \in \{1, \dots, n\}$ and $S_i = \operatorname{rank}(Y_i) \in \{1, \dots, n\}$ denote the marginal ranks of $X_i$ and $Y_i$ within their respective samples. Charles Spearman (1904) defined $\rho_s$ (or $r_s$) as Pearson's product-moment correlation evaluated directly on the rank pairs $(R_i, S_i)$:

$$\rho_s = \frac{\sum_{i=1}^n \left(R_i - \bar{R}\right)\left(S_i - \bar{S}\right)}{\sqrt{\sum_{i=1}^n \left(R_i - \bar{R}\right)^2 \sum_{i=1}^n \left(S_i - \bar{S}\right)^2}}$$

When there are **no ties** in either $X$ or $Y$, both $\{R_1, \dots, R_n\}$ and $\{S_1, \dots, S_n\}$ are permutations of $\{1, 2, \dots, n\}$ with $\bar{R} = \bar{S} = \frac{n+1}{2}$ and $\sum_{i=1}^n (R_i - \bar{R})^2 = \sum_{i=1}^n (S_i - \bar{S})^2 = \frac{n(n^2 - 1)}{12}$. Using the algebraic identity for the squared rank differences $d_i = R_i - S_i$:

$$\sum_{i=1}^n d_i^2 = \sum_{i=1}^n \left[ (R_i - \bar{R}) - (S_i - \bar{S}) \right]^2 = \sum_{i=1}^n (R_i - \bar{R})^2 + \sum_{i=1}^n (S_i - \bar{S})^2 - 2\sum_{i=1}^n (R_i - \bar{R})(S_i - \bar{S})$$

we solve for $\sum_{i=1}^n (R_i - \bar{R})(S_i - \bar{S}) = \frac{n(n^2 - 1)}{12} - \frac{1}{2}\sum_{i=1}^n d_i^2$ and divide by $\frac{n(n^2 - 1)}{12}$ to obtain **Spearman's Shortcut Formula**:

$$\rho_s = 1 - \frac{6 \sum_{i=1}^n d_i^2}{n\left(n^2 - 1\right)}, \qquad \text{where } d_i = R_i - S_i \quad (\text{valid when no ties exist})$$

Under the null hypothesis of bivariate independence $H_0: F_{X,Y}(x, y) = F_X(x)F_Y(y)$, all $n!$ pairings of $\mathbf{S}$ with $\mathbf{R}$ are equally likely, yielding exact moments:

$$\mathbb{E}_{H_0}[\rho_s] = 0, \qquad \operatorname{Var}_{H_0}(\rho_s) = \frac{1}{n - 1}$$

Thus, for large $n$, $Z_s = \rho_s \sqrt{n - 1} \xrightarrow{d} \mathcal{N}(0, 1)$, or even more accurately in finite samples ($n \ge 10$), Student's $t$-approximation $t_s = \rho_s \sqrt{\frac{n - 2}{1 - \rho_s^2}} \sim t_{n - 2}$. Under bivariate normality, the Pitman ARE of Spearman's test relative to Pearson's $r$ test is $\left(\frac{3}{\pi}\right)^2 = \frac{9}{\pi^2} \approx 0.9119$ ($91.2\%$).

### 2. Kendall's Rank Correlation $\tau$ (1938): Concordant/Discordant Pairs and U-Statistic Variance

Maurice Kendall (1938) formulated a direct probabilistic measure of ordinal concordance based on all $\binom{n}{2} = \frac{n(n-1)}{2}$ distinct pairs of observations $\{(X_i, Y_i), (X_j, Y_j)\}$ ($1 \le i < j \le n$):
- A pair $(i, j)$ is **Concordant ($C$)** if $(X_i - X_j)(Y_i - Y_j) > 0$ (both $X_i > X_j, Y_i > Y_j$ or both $X_i < X_j, Y_i < Y_j$; the two variables move in the same direction).
- A pair $(i, j)$ is **Discordant ($D$)** if $(X_i - X_j)(Y_i - Y_j) < 0$ ($X_i$ and $Y_j$ move in opposite directions).
- A pair $(i, j)$ is **Tied** if $X_i = X_j$ or $Y_i = Y_j$.

In the population, let $\pi_c = \mathbb{P}\left((X_1 - X_2)(Y_1 - Y_2) > 0\right)$ and $\pi_d = \mathbb{P}\left((X_1 - X_2)(Y_1 - Y_2) < 0\right)$. **Kendall's Population Parameter $\tau = \pi_c - \pi_d \in [-1, +1]$** is the difference between the probability of concordance and the probability of discordance for two randomly drawn bivariate observations! Its sample estimator (**Kendall's $\tau_a$** when no ties exist) is a symmetric **Hoeffding $U$-Statistic of degree $m = 2$** with bounded kernel $h\left((X_i, Y_i), (X_j, Y_j)\right) = \operatorname{sgn}(X_i - X_j)\operatorname{sgn}(Y_i - Y_j) \in \{-1, 0, +1\}$:

$$\hat{\tau}_a = \frac{1}{\binom{n}{2}} \sum_{1 \le i < j \le n} \operatorname{sgn}(X_i - X_j)\operatorname{sgn}(Y_i - Y_j) = \frac{N_c - N_d}{n(n - 1) / 2}$$

where $N_c$ is the total number of concordant pairs and $N_d$ is the total number of discordant pairs ($N_c + N_d = \binom{n}{2}$ when no ties exist). Under $H_0$ (independence), by Hoeffding's $U$-statistic projection theorem, the exact finite-sample expectation and variance of $\hat{\tau}_a$ and of $S_K = N_c - N_d$ are:

$$\mathbb{E}_{H_0}[\hat{\tau}_a] = 0, \qquad \operatorname{Var}_{H_0}(S_K) = \frac{n(n - 1)(2n + 5)}{18}, \qquad \operatorname{Var}_{H_0}(\hat{\tau}_a) = \frac{2(2n + 5)}{9n(n - 1)}$$

Thus, the standardized asymptotic normal test statistic under $H_0$ is:

$$Z_\tau = \frac{S_K}{\sqrt{\frac{n(n - 1)(2n + 5)}{18}}} = \frac{3\hat{\tau}_a \sqrt{n(n - 1)}}{\sqrt{2(2n + 5)}} \;\underset{H_0}{\xrightarrow{d}}\; \mathcal{N}(0, 1)$$

Under bivariate normality with correlation $\rho$, Greiner's relation states $\tau = \frac{2}{\pi}\arcsin(\rho)$, and the Pitman ARE of Kendall's $\tau$ test relative to Pearson's $r$ is identical to Spearman's test: $\frac{9}{\pi^2} \approx 0.9119$.

### 3. Adjusting for Ties: Kendall's $\tau_b$ vs. Goodman–Kruskal $\gamma$ (1954)

When ties occur ($T_X = \frac{1}{2}\sum_g t_{X,g}(t_{X,g} - 1)$ pairs tied on $X$, and $T_Y = \frac{1}{2}\sum_h t_{Y,h}(t_{Y,h} - 1)$ pairs tied on $Y$), two primary adjustments exist:
1. **Kendall's $\tau_b$**: Normalizes $N_c - N_d$ by the geometric mean of the number of untied $X$-pairs and untied $Y$-pairs:

$$\hat{\tau}_b = \frac{N_c - N_d}{\sqrt{\left[\binom{n}{2} - T_X\right]\left[\binom{n}{2} - T_Y\right]}}$$

2. **Goodman and Kruskal's Gamma ($\gamma$, 1954)**: Completely conditions on the event that a pair is untied on both variables, measuring the conditional excess of concordant over discordant pairs among all strictly untied pairs:

$$\hat{\gamma} = \frac{N_c - N_d}{N_c + N_d} \in [-1, +1]$$

In ordinal contingency tables with many ties, $|\hat{\gamma}| \ge |\hat{\tau}_b| \ge |\hat{\tau}_a|$, and $\hat{\gamma} = \pm 1$ under weak monotonicity (e.g., upper-triangular or staircase tables) even when $\hat{\tau}_b < 1$.

---

## 8.6 Resampling and Exact Randomization Inference: Fisher–Pitman Permutation Tests, Exchangeability, Monte Carlo P-Values, and Bootstrap Hypothesis Testing

Whereas rank tests achieve distribution-free exactness by replacing raw observations $X_i$ with their integer ranks $R_i$ (thereby discarding exact metric distances between observations), Ronald Fisher (1935) and Edwin Pitman (1937) demonstrated that **exact distribution-free tests can be constructed directly from the original metric data** by conditioning on the observed order statistics!

### Exchangeability Under $H_0$ and Exact Two-Sample Fisher–Pitman Permutation Tests

Let $\mathbf{Z} = (Z_1, Z_2, \dots, Z_N) = (X_1, \dots, X_m, Y_1, \dots, Y_n)$ denote the combined vector of $N = m + n$ observations from two independent samples $X_1, \dots, X_m \sim F_X$ and $Y_1, \dots, Y_n \sim F_Y$. Under the null hypothesis of identical distributions $H_0: F_X = F_Y = F$, the joint distribution of $(Z_1, \dots, Z_N)$ is **exchangeable**: for every permutation $\pi \in \mathcal{S}_N$ of $\{1, 2, \dots, N\}$, the permuted vector $(Z_{\pi(1)}, \dots, Z_{\pi(N)})$ has the exact same joint probability distribution as $(Z_1, \dots, Z_N)$.

Let $\mathbf{Z}_{(\cdot)} = (Z_{(1)} \le Z_{(2)} \le \dots \le Z_{(N)})$ denote the vector of pooled order statistics. Under $H_0$, $\mathbf{Z}_{(\cdot)}$ is a **complete sufficient statistic** for the unknown common distribution $F$. Conditioning on the observed order statistics $\mathbf{Z}_{(\cdot)} = \mathbf{z}_{(\cdot)}$, all $\binom{N}{m} = \frac{N!}{m! n!}$ distinct assignments of $m$ values to the treatment group $\mathcal{X}^*$ and $n$ values to the control group $\mathcal{Y}^*$ have **exact conditional probability $1 / \binom{N}{m}$**, regardless of what the true underlying distribution $F$ is!

Let $T(\mathbf{Z}) = \bar{X} - \bar{Y}$ (or any test statistic, such as the Studentized $t$-statistic or trimmed mean difference) be evaluated on the observed sample, yielding $t_{\text{obs}} = T(\mathbf{z})$. Note that because the grand sum $S_{\text{total}} = \sum_{i=1}^m X_i + \sum_{j=1}^n Y_j$ is strictly constant across all $\binom{N}{m}$ partitions, $\bar{X} - \bar{Y} = \frac{1}{m}\sum_{i=1}^m X_i - \frac{1}{n}\left(S_{\text{total}} - \sum_{i=1}^m X_i\right) = \frac{N}{m n}\sum_{i=1}^m X_i - \frac{S_{\text{total}}}{n}$ is a strictly increasing linear function of the first-sample sum $S_X = \sum_{i=1}^m X_i$! Thus, the **Exact One-Sided Fisher–Pitman Permutation $p$-Value** is simply the fraction of all $M = \binom{N}{m}$ partitions $\mathcal{P}_r$ ($r = 1, \dots, M$) whose test statistic $T(\mathbf{z}_r^*)$ is at least as extreme as $t_{\text{obs}}$:

$$p_{\text{exact}} = \mathbb{P}_{H_0}\left( T(\mathbf{Z}^*) \ge t_{\text{obs}} \;\middle|\; \mathbf{Z}_{(\cdot)} = \mathbf{z}_{(\cdot)} \right) = \frac{1}{\binom{N}{m}} \sum_{r=1}^{\binom{N}{m}} \mathbf{1}_{\left\{ T(\mathbf{z}_r^*) \ge t_{\text{obs}} \right\}}$$

By Lehmann and Stein's (1949) theorem, any test that maintains an exact Type I error rate $\alpha$ across all continuous distributions $F$ **must** be a conditional permutation test given $\mathbf{Z}_{(\cdot)}$, and the Fisher–Pitman permutation test has a Pitman ARE of **$1.000$ ($100\%$)** relative to Student's $t$-test under Gaussian populations!

In matched-pairs designs where $n$ paired differences $D_i = X_i - Y_i$ ($i = 1, \dots, n$) are observed under the null hypothesis that each $D_i$ is symmetrically distributed around zero ($f_D(d) = f_D(-d)$), the conditional randomization group consists of all $2^n$ **sign-flippings** $\mathbf{D}^*(\mathbf{s}) = (s_1 |D_1|, s_2 |D_2|, \dots, s_n |D_n|)$ with independent signs $s_i \in \{-1, +1\}$. Conditioning on the observed absolute differences $(|D_1|, \dots, |D_n|)$, each of the $2^n$ sign assignments occurs with exact probability $2^{-n}$, and the Fisher–Pitman paired randomization test computes the fraction of the $2^n$ signed sums $\sum_{i=1}^n s_i |D_i|$ that equal or exceed the observed sum $\sum_{i=1}^n D_i$. Moreover, by exploiting the **Neyman–Pearson Duality Between Hypothesis Tests and Confidence Regions**, we can invert the two-sample Fisher–Pitman permutation test of $H_0(\Delta_0): F_X(x - \Delta_0) = F_Y(x)$ by subtracting the hypothesized shift $\Delta_0$ from every treatment observation ($X_i(\Delta_0) = X_i - \Delta_0$) and collecting all values of $\Delta_0 \in \mathbb{R}$ that are not rejected at level $\alpha$. This test inversion produces an exact $100(1 - \alpha)\%$ distribution-free confidence interval $[\hat{\Delta}_L, \hat{\Delta}_U]$ for the location shift $\Delta$ whose endpoints coincide with ordered pairwise differences $X_i - Y_j$ when applied to Wilcoxon rank sums (the **Hodges–Lehmann estimator** and Moses confidence interval).

### Unbiased Monte Carlo Randomization $P$-Values (Phipson and Smyth, 2010)

When $m$ and $n$ are moderate (e.g., $m = n = 20 \implies \binom{40}{20} \approx 1.378 \times 10^{11}$), enumerating all $\binom{N}{m}$ partitions is computationally intractable. Instead, we draw $B$ independent uniform random permutations $\mathbf{z}_1^*, \dots, \mathbf{z}_B^*$ (typically $B = 9{,}999$ or $99{,}999$) and count how many simulated values satisfy $T(\mathbf{z}_b^*) \ge t_{\text{obs}}$.

> [!IMPORTANT]
> **Why the $+1$ Pseudocount Is Mandatory**: If $K = \sum_{b=1}^B \mathbf{1}_{\{T(\mathbf{z}_b^*) \ge t_{\text{obs}}\}}$, the naive Monte Carlo estimator $\hat{p}_{\text{naive}} = K / B$ can equal $0$ with positive probability, violating the exact validity requirement $\mathbb{P}_{H_0}(\hat{p} \le \alpha) \le \alpha$. Including the observed data configuration itself as one of the $B + 1$ exchangeable realizations under $H_0$ yields the **exact valid Monte Carlo $p$-value** (Barnard, 1963; Phipson and Smyth, 2010):
> $$\hat{p}_{\text{MC}} = \frac{1 + \sum_{b=1}^B \mathbf{1}_{\left\{ T(\mathbf{z}_b^*) \ge t_{\text{obs}} \right\}}}{B + 1}$$
> Under $H_0$, the rank of $t_{\text{obs}}$ among $\{t_{\text{obs}}, T(\mathbf{z}_1^*), \dots, T(\mathbf{z}_B^*)\}$ is discrete uniform on $\{1, 2, \dots, B + 1\}$, guaranteeing $\mathbb{P}_{H_0}\left(\hat{p}_{\text{MC}} \le \frac{j}{B+1}\right) = \frac{j}{B+1}$ exactly!

### Bootstrap Hypothesis Testing vs. Permutation Testing: Shifting to Impose $H_0$ and Pivotal Studentization

Unlike permutation testing—which samples **without replacement** from the pooled data and strictly requires total exchangeability of the distributions ($F_X = F_Y$) under $H_0$—**Bootstrap Hypothesis Testing** (Efron and Tibshirani, 1993; Hall and Wilson, 1991) can test equality of a specific parameter such as means $H_0: \mu_X = \mu_Y$ even when the population variances or shapes differ ($\sigma_X^2 \neq \sigma_Y^2$, known as the nonparametric Behrens–Fisher problem)!

However, executing a valid bootstrap hypothesis test requires obeying **Hall and Wilson's Two Golden Rules of Bootstrap Testing**:
1. **Resample From an Empirical Distribution That Explicitly Satisfies $H_0$**: If we naively resampled $X_1^*, \dots, X_m^*$ from $\{X_1, \dots, X_m\}$ (which has sample mean $\bar{X}$) and $Y_1^*, \dots, Y_n^*$ from $\{Y_1, \dots, Y_n\}$ (which has sample mean $\bar{Y} \neq \bar{X}$), the bootstrap world would have true mean difference $\bar{X} - \bar{Y} \neq 0$, mimicking $H_1$ rather than $H_0$! Instead, we must recenter each sample to share the common pooled mean $\bar{Z} = \frac{m\bar{X} + n\bar{Y}}{m+n}$ (or recenter both to $0$):

$$\tilde{X}_i = X_i - \bar{X} + \bar{Z} \quad (i = 1, \dots, m), \qquad \tilde{Y}_j = Y_j - \bar{Y} + \bar{Z} \quad (j = 1, \dots, n)$$

   and draw $X_1^*, \dots, X_m^*$ with replacement from $\{\tilde{X}_1, \dots, \tilde{X}_m\}$ and $Y_1^*, \dots, Y_n^*$ with replacement from $\{\tilde{Y}_1, \dots, \tilde{Y}_n\}$.
2. **Pivot / Studentize the Bootstrap Test Statistic**: Compute the Welch-studentized statistic on the observed sample and on each bootstrap resample $b = 1, \dots, B$:

$$t_{\text{obs}} = \frac{\bar{X} - \bar{Y}}{\sqrt{\frac{s_X^2}{m} + \frac{s_Y^2}{n}}}, \qquad t_b^* = \frac{\bar{X}_b^* - \bar{Y}_b^*}{\sqrt{\frac{(s_{X,b}^*)^2}{m} + \frac{(s_{Y,b}^*)^2}{n}}}$$

   Because $t_b^*$ is an **asymptotically pivotal quantity** (its limiting $\mathcal{N}(0, 1)$ distribution is free of unknown nuisance variances $\sigma_X^2, \sigma_Y^2$), Edgeworth expansion theory proves that the studentized bootstrap achieves **second-order asymptotic accuracy** (Type I error discrepancy $O(n^{-1})$ instead of $O(n^{-1/2})$).

<div class="table-wrapper"><table class="data-table">
<thead>
<tr>
<th>Nonparametric / Resampling Test</th>
<th>Experimental Design &amp; Hypotheses</th>
<th>Test Statistic Formula</th>
<th>Null Reference Distribution</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Kruskal–Wallis $H$-Test</strong></td>
<td>$k$ independent samples ($N = \sum n_i$); omnibus $H_0: \theta_1 = \dots = \theta_k$</td>
<td>$H = \frac{12}{N(N+1)}\sum_{i=1}^k \frac{R_{i\cdot}^2}{n_i} - 3(N+1)$</td>
<td>Asymptotic $\chi^2_{k-1}$; exact permutation table for small $n_i$</td>
</tr>
<tr>
<td><strong>Friedman's Rank Test ($Q_F$)</strong></td>
<td>Randomized Complete Block Design ($b$ blocks, $k$ treatments); omnibus $H_0: \tau_1 = \dots = \tau_k$</td>
<td>$Q_F = \frac{12}{b k(k+1)}\sum_{j=1}^k R_{\cdot j}^2 - 3b(k+1)$</td>
<td>Asymptotic $\chi^2_{k-1}$; Iman–Davenport $F_{k-1, (b-1)(k-1)}$</td>
</tr>
<tr>
<td><strong>Kendall's Concordance $W$</strong></td>
<td>$b$ judges ranking $k$ items; inter-rater agreement $H_0: W = 0$</td>
<td>$W = \frac{12 S}{b^2 k(k^2 - 1)} = \frac{Q_F}{b(k-1)}$</td>
<td>Tested via $Q_F = b(k-1)W \sim \chi^2_{k-1}$</td>
</tr>
<tr>
<td><strong>Jonckheere–Terpstra ($JT$)</strong></td>
<td>$k$ independent samples; ordered trend $H_1: \theta_1 \le \dots \le \theta_k$</td>
<td>$J = \sum_{1 \le i < \ell \le k} U_{i\ell}$</td>
<td>Asymptotic $Z_{\text{JT}} = \frac{J - \mathbb{E}[J]}{\sqrt{\operatorname{Var}(J)}} \sim \mathcal{N}(0, 1)$</td>
</tr>
<tr>
<td><strong>Page's $L$-Test</strong></td>
<td>RCBD ($b$ blocks, $k$ treatments); ordered trend $H_1: \tau_1 \le \dots \le \tau_k$</td>
<td>$L = \sum_{j=1}^k j R_{\cdot j}$</td>
<td>Asymptotic $Z_L = \frac{12 L - 3 b k(k+1)^2}{k(k+1)\sqrt{b(k-1)}} \sim \mathcal{N}(0, 1)$</td>
</tr>
<tr>
<td><strong>Fisher–Pitman Permutation</strong></td>
<td>Two or $k$ samples under exchangeability $H_0: F_1 = \dots = F_k$</td>
<td>$T(\mathbf{Z}) = \bar{X} - \bar{Y}$ or $\sum n_i \bar{X}_i^2$</td>
<td>Exact uniform over all $\binom{N}{m}$ or $\frac{N!}{n_1!\cdots n_k!}$ partitions</td>
</tr>
</tbody>
</table></div>

---

## Worked Questions and Solutions

### Question 1: Kruskal–Wallis $H$-Test With Ties, Exact Tie-Correction Factor, and Dunn–Bonferroni Pairwise Post-Hoc Comparisons

An environmental toxicologist measures heavy-metal bioaccumulation (in $\mu\text{g/g}$) in fish specimens sampled from $k = 3$ river estuaries with $n_1 = 4$, $n_2 = 4$, and $n_3 = 4$ observations ($N = 12$):
- **Estuary 1 (Upstream Reference)**: $12, \; 15, \; 15, \; 18$
- **Estuary 2 (Agricultural Runoff)**: $20, \; 24, \; 24, \; 24$
- **Estuary 3 (Industrial Discharge)**: $28, \; 32, \; 35, \; 40$

1. Pool all $N = 12$ observations, assign midranks to tied values, and compute the group rank sums $R_{1\cdot}, R_{2\cdot}, R_{3\cdot}$, the group mean ranks $\bar{R}_{1\cdot}, \bar{R}_{2\cdot}, \bar{R}_{3\cdot}$, and the unadjusted Kruskal–Wallis statistic $H$.
2. Identify all tied groups, calculate the exact tie-correction factor $C_{\text{ties}} = 1 - \frac{\sum (t_g^3 - t_g)}{N^3 - N}$, compute the tie-adjusted statistic $H_{\text{adj}}$, and test $H_0: \theta_1 = \theta_2 = \theta_3$ at $\alpha = 0.05$ ($\chi^2_{0.05, 2} = 5.991$, $\chi^2_{0.01, 2} = 9.210$).
3. Execute Dunn's pairwise post-hoc multiple comparison procedure with tie-adjusted standard error and Bonferroni family-wise error control at $\alpha = 0.05$ across all $M = \binom{3}{2} = 3$ pairs ($z_{0.05 / 6} = z_{0.00833} = 2.394$).

### Solution, step 1: Pooled Midranks, Group Rank Sums, and Unadjusted $H$

Sorting all $N = 12$ observations in ascending order gives:

$$12, \; \underbrace{15, \; 15}_{\text{positions } 2, 3}, \; 18, \; 20, \; \underbrace{24, \; 24, \; 24}_{\text{positions } 6, 7, 8}, \; 28, \; 32, \; 35, \; 40$$

Assigning midranks to the two tied clusters:
- Value $12$ (pos $1$): rank $1.0$
- Value $15$ (pos $2, 3$, $t_1 = 2$): midrank $\frac{2 + 3}{2} = 2.5$
- Value $18$ (pos $4$): rank $4.0$
- Value $20$ (pos $5$): rank $5.0$
- Value $24$ (pos $6, 7, 8$, $t_2 = 3$): midrank $\frac{6 + 7 + 8}{3} = 7.0$
- Value $28$ (pos $9$): rank $9.0$
- Value $32$ (pos $10$): rank $10.0$
- Value $35$ (pos $11$): rank $11.0$
- Value $40$ (pos $12$): rank $12.0$

Summing the midranks within each of the $k = 3$ groups ($n_1 = n_2 = n_3 = 4$):
- **Estuary 1**: $R_{1\cdot} = 1.0 + 2.5 + 2.5 + 4.0 = 10.0 \implies \bar{R}_{1\cdot} = \frac{10.0}{4} = 2.50$
- **Estuary 2**: $R_{2\cdot} = 5.0 + 7.0 + 7.0 + 7.0 = 26.0 \implies \bar{R}_{2\cdot} = \frac{26.0}{4} = 6.50$
- **Estuary 3**: $R_{3\cdot} = 9.0 + 10.0 + 11.0 + 12.0 = 42.0 \implies \bar{R}_{3\cdot} = \frac{42.0}{4} = 10.50$

(Check: $R_{1\cdot} + R_{2\cdot} + R_{3\cdot} = 10.0 + 26.0 + 42.0 = 78.0 = \frac{12(13)}{2}$). Now compute the unadjusted Kruskal–Wallis $H$ statistic:

$$H = \frac{12}{N(N + 1)}\sum_{i=1}^3 \frac{R_{i\cdot}^2}{n_i} - 3(N + 1) = \frac{12}{12(13)} \left( \frac{10.0^2}{4} + \frac{26.0^2}{4} + \frac{42.0^2}{4} \right) - 3(13)$$

$$H = \frac{1}{13} \left( \frac{100 + 676 + 1{,}764}{4} \right) - 39 = \frac{1}{13} \left( \frac{2{,}540}{4} \right) - 39 = \frac{635}{13} - 39 = 48.8462 - 39.0000 = 9.8462$$

### Solution, step 2: Tie-Correction Factor $C_{\text{ties}}$ and Tie-Adjusted $H_{\text{adj}}$

We have two tied sets:
- $g = 1$ (at value $15$): $t_1 = 2 \implies t_1^3 - t_1 = 8 - 2 = 6$
- $g = 2$ (at value $24$): $t_2 = 3 \implies t_2^3 - t_2 = 27 - 3 = 24$

Summing $\sum_{g=1}^2 (t_g^3 - t_g) = 6 + 24 = 30$, with $N^3 - N = 12^3 - 12 = 1{,}728 - 12 = 1{,}716$:

$$C_{\text{ties}} = 1 - \frac{30}{1{,}716} = 1 - \frac{5}{286} = \frac{281}{286} \approx 0.9825$$

Dividing $H$ by $C_{\text{ties}}$ gives the tie-adjusted Kruskal–Wallis statistic:

$$H_{\text{adj}} = \frac{9.8462}{281 / 286} = \frac{128 / 13}{281 / 286} = \frac{128 \times 22}{281} = \frac{2{,}816}{281} \approx 10.0214$$

Because $H_{\text{adj}} = 10.0214 > \chi^2_{0.01, 2} = 9.210$ ($p\text{-value} \approx 0.00667$), we reject $H_0$ at both the $5\%$ and $1\%$ significance levels.

### Solution, step 3: Dunn's Post-Hoc Pairwise Comparisons With Bonferroni Adjustment

For equal sample sizes $n_i = n_\ell = 4$ and $N = 12$, the tie-adjusted standard error of any pairwise mean-rank difference $\bar{R}_{i\cdot} - \bar{R}_{\ell\cdot}$ is:

$$\operatorname{SE}_{\text{Dunn}} = \sqrt{\left[ \frac{N(N + 1)}{12} - \frac{\sum (t_g^3 - t_g)}{12(N - 1)} \right] \left(\frac{1}{4} + \frac{1}{4}\right)} = \sqrt{\left[ \frac{12(13)}{12} - \frac{30}{12(11)} \right] (0.50)} = \sqrt{(13 - 0.2273)(0.50)} = \sqrt{6.3864} \approx 2.5271$$

Evaluating Dunn's $Z_{i\ell} = \frac{|\bar{R}_{i\cdot} - \bar{R}_{\ell\cdot}|}{2.5271}$ against the Bonferroni critical value $z_{0.05/6} = 2.394$:
- **Estuary 1 vs. Estuary 2**: $Z_{12} = \frac{|2.50 - 6.50|}{2.5271} = \frac{4.00}{2.5271} = 1.5828 < 2.394$ (not significant after Bonferroni correction).
- **Estuary 2 vs. Estuary 3**: $Z_{23} = \frac{|6.50 - 10.50|}{2.5271} = \frac{4.00}{2.5271} = 1.5828 < 2.394$ (not significant after Bonferroni correction).
- **Estuary 1 vs. Estuary 3**: $Z_{13} = \frac{|2.50 - 10.50|}{2.5271} = \frac{8.00}{2.5271} = 3.1657 > 2.394$ (**statistically significant**, adjusted $p\text{-value} = 3 \times 2\Phi(-3.1657) = 6 \times 0.00077 = 0.0046 < 0.05$).

---

### Question 2: Friedman's Randomized Block Test, Kendall's Coefficient of Concordance $W$, and Page's $L$-Test for Ordered Monotonic Trend

A clinical pharmacology study evaluates pain-relief latency scores across $b = 6$ subjects (blocks) under $k = 4$ increasing dosage regimens of an analgesic ($D_1 = 5\text{ mg} < D_2 = 10\text{ mg} < D_3 = 20\text{ mg} < D_4 = 40\text{ mg}$). Within each subject $i \in \{1, \dots, 6\}$, the $k = 4$ regimens are ranked from $1$ (lowest efficacy) to $4$ (highest efficacy) with no ties, yielding the intra-block rank matrix $(r_{ij})$:

<div class="table-wrapper"><table class="data-table">
<thead>
<tr>
<th>Subject (Block $i$)</th>
<th>Regimen $D_1$ ($j=1$)</th>
<th>Regimen $D_2$ ($j=2$)</th>
<th>Regimen $D_3$ ($j=3$)</th>
<th>Regimen $D_4$ ($j=4$)</th>
</tr>
</thead>
<tbody>
<tr><td>Subject 1</td><td>$1$</td><td>$2$</td><td>$3$</td><td>$4$</td></tr>
<tr><td>Subject 2</td><td>$1$</td><td>$3$</td><td>$2$</td><td>$4$</td></tr>
<tr><td>Subject 3</td><td>$2$</td><td>$1$</td><td>$3$</td><td>$4$</td></tr>
<tr><td>Subject 4</td><td>$1$</td><td>$2$</td><td>$4$</td><td>$3$</td></tr>
<tr><td>Subject 5</td><td>$1$</td><td>$2$</td><td>$3$</td><td>$4$</td></tr>
<tr><td>Subject 6</td><td>$1$</td><td>$2$</td><td>$3$</td><td>$4$</td></tr>
</tbody>
</table></div>

1. Compute the treatment rank sums $R_{\cdot 1}, R_{\cdot 2}, R_{\cdot 3}, R_{\cdot 4}$, Friedman's statistic $Q_F$, and the Iman–Davenport $F_{\text{ID}}$ statistic, and test the omnibus null hypothesis $H_0: \tau_1 = \tau_2 = \tau_3 = \tau_4$ at $\alpha = 0.05$ ($\chi^2_{0.05, 3} = 7.815$, $F_{0.05, 3, 15} = 3.287$).
2. Compute Kendall's Coefficient of Concordance $W$, verify $Q_F = b(k - 1)W$, and find the exact average pairwise Spearman rank correlation $\bar{\rho}_s$ across the $\binom{6}{2} = 15$ pairs of subjects.
3. Compute Page's ordered trend statistic $L = \sum_{j=1}^4 j R_{\cdot j}$ and its standardized score $Z_L$ to test $H_0$ against the ordered dose-response alternative $H_1: \tau_1 \le \tau_2 \le \tau_3 \le \tau_4$.

### Solution, step 1: Treatment Rank Sums, Friedman's $Q_F$, and Iman–Davenport $F_{\text{ID}}$

Summing the intra-block ranks down each column across the $b = 6$ subjects:
- $R_{\cdot 1} = 1 + 1 + 2 + 1 + 1 + 1 = 7$ ($\bar{R}_{\cdot 1} = 7/6 = 1.1667$)
- $R_{\cdot 2} = 2 + 3 + 1 + 2 + 2 + 2 = 12$ ($\bar{R}_{\cdot 2} = 12/6 = 2.0000$)
- $R_{\cdot 3} = 3 + 2 + 3 + 4 + 3 + 3 = 18$ ($\bar{R}_{\cdot 3} = 18/6 = 3.0000$)
- $R_{\cdot 4} = 4 + 4 + 4 + 3 + 4 + 4 = 23$ ($\bar{R}_{\cdot 4} = 23/6 = 3.8333$)

(Check: $\sum_{j=1}^4 R_{\cdot j} = 7 + 12 + 18 + 23 = 60 = \frac{b k(k+1)}{2} = \frac{6(4)(5)}{2}$, with null expected column sum $\frac{b(k+1)}{2} = 15.0$). Now evaluate the sum of squared deviations $S = \sum_{j=1}^4 (R_{\cdot j} - 15)^2$:

$$S = (7 - 15)^2 + (12 - 15)^2 + (18 - 15)^2 + (23 - 15)^2 = (-8)^2 + (-3)^2 + 3^2 + 8^2 = 64 + 9 + 9 + 64 = 146$$

Substituting $S = 146$ (or $\sum R_{\cdot j}^2 = 49 + 144 + 324 + 529 = 1{,}046$) into Friedman's formula:

$$Q_F = \frac{12 S}{b k(k + 1)} = \frac{12(146)}{6(4)(5)} = \frac{1{,}752}{120} = 14.6000$$

Since $Q_F = 14.6000 > \chi^2_{0.05, 3} = 7.815$ ($p\text{-value} = 0.00219$), we reject $H_0$. Furthermore, the Iman–Davenport $F$-statistic with $(k - 1, (b - 1)(k - 1)) = (3, 15)$ degrees of freedom is:

$$F_{\text{ID}} = \frac{(b - 1) Q_F}{b(k - 1) - Q_F} = \frac{5(14.60)}{6(3) - 14.60} = \frac{73.00}{3.40} \approx 21.4706 > F_{0.05, 3, 15} = 3.287$$

### Solution, step 2: Kendall's Coefficient of Concordance $W$ and Average Spearman Correlation $\bar{\rho}_s$

For $b = 6$ and $k = 4$, the maximum possible sum of squared deviations is:

$$S_{\max} = \frac{b^2 k\left(k^2 - 1\right)}{12} = \frac{36(4)(15)}{12} = 180$$

Thus, Kendall's Coefficient of Concordance is:

$$W = \frac{S}{S_{\max}} = \frac{146}{180} = \frac{73}{90} \approx 0.8111$$

Verifying the exact identity with Friedman's statistic: $b(k - 1)W = 6(3)\left(\frac{73}{90}\right) = 18\left(\frac{73}{90}\right) = \frac{73}{5} = 14.6000 = Q_F$. Finally, the average pairwise Spearman rank correlation across all $\binom{6}{2} = 15$ pairs of subjects is:

$$\bar{\rho}_s = \frac{b W - 1}{b - 1} = \frac{6(73 / 90) - 1}{6 - 1} = \frac{4.8667 - 1}{5} = \frac{3.8667}{5} = \frac{58}{75} \approx 0.7733$$

### Solution, step 3: Page's $L$-Test for Monotonic Dose-Response Trend

Evaluating Page's linear rank statistic $L = \sum_{j=1}^4 j R_{\cdot j}$:

$$L = 1(7) + 2(12) + 3(18) + 4(23) = 7 + 24 + 54 + 92 = 177$$

Under $H_0$, the exact mean and variance of $L$ for $b = 6, k = 4$ are:

$$\mathbb{E}_{H_0}[L] = \frac{b k(k + 1)^2}{4} = \frac{6(4)(25)}{4} = 150.0$$

$$\operatorname{Var}_{H_0}(L) = \frac{b k^2(k + 1)\left(k^2 - 1\right)}{144} = \frac{6(16)(5)(15)}{144} = \frac{7{,}200}{144} = 50.0 \quad \Longrightarrow \quad \operatorname{SD}_{H_0}(L) = \sqrt{50.0} \approx 7.0711$$

Computing the standardized normal score $Z_L$:

$$Z_L = \frac{177 - 150.0}{\sqrt{50.0}} = \frac{27.0}{7.0711} \approx 3.8184$$

The one-sided $p$-value is $1 - \Phi(3.8184) \approx 0.000067$ ($6.7 \times 10^{-5}$), which is more than $30$ times smaller than the omnibus Friedman $p$-value ($0.00219$), illustrating the dramatic power gain of Page's $L$-test when the true response follows a monotonic trend!

---

### Question 3: Spearman's Rank Correlation $\rho_s$, Kendall's $\tau$ via Concordant and Discordant Pairs, and Exact Two-Sample Fisher–Pitman Permutation Test

1. **Part A (Rank Correlation)**: A biostatistician records paired measurements $(X_i, Y_i)$ for $n = 6$ patients: $(10, 14)$, $(15, 11)$, $(20, 22)$, $(25, 19)$, $(30, 28)$, and $(35, 34)$. Compute both Spearman's rank correlation $\rho_s$ and Kendall's $\tau_a$ (explicitly enumerating the number of concordant pairs $N_c$ and discordant pairs $N_d$ for each observation), and find the exact two-sided $Z_\tau$ score.
2. **Part B (Exact Fisher–Pitman Permutation Test)**: In a pilot clinical trial, $m = 3$ treatment patients yield recovery scores $\mathcal{X} = \{19, 22, 25\}$ and $n = 3$ control patients yield scores $\mathcal{Y} = \{10, 13, 20\}$. Enumerate the total number of partitions $\binom{6}{3}$, identify every partition whose treatment sum $\sum_{i=1}^3 X_i^*$ is greater than or equal to the observed treatment sum $S_{X,\text{obs}}$, and compute the **exact one-sided and two-sided Fisher–Pitman permutation $p$-values**.

### Solution, step 1: Marginal Ranks and Spearman's Rank Correlation $\rho_s$ (Part A)

Because the $X_i$ values $(10, 15, 20, 25, 30, 35)$ are already sorted in strictly ascending order, their ranks are $R_i = (1, 2, 3, 4, 5, 6)$. Ranking the corresponding $Y_i$ values $(14, 11, 22, 19, 28, 34)$ from smallest to largest ($11 < 14 < 19 < 22 < 28 < 34$) yields $S_i = (2, 1, 4, 3, 5, 6)$:
- $i = 1$: $(R_1, S_1) = (1, 2) \implies d_1 = 1 - 2 = -1 \implies d_1^2 = 1$
- $i = 2$: $(R_2, S_2) = (2, 1) \implies d_2 = 2 - 1 = +1 \implies d_2^2 = 1$
- $i = 3$: $(R_3, S_3) = (3, 4) \implies d_3 = 3 - 4 = -1 \implies d_3^2 = 1$
- $i = 4$: $(R_4, S_4) = (4, 3) \implies d_4 = 4 - 3 = +1 \implies d_4^2 = 1$
- $i = 5$: $(R_5, S_5) = (5, 5) \implies d_5 = 5 - 5 = 0 \implies d_5^2 = 0$
- $i = 6$: $(R_6, S_6) = (6, 6) \implies d_6 = 6 - 6 = 0 \implies d_6^2 = 0$

Summing the squared rank differences gives $\sum_{i=1}^6 d_i^2 = 1 + 1 + 1 + 1 + 0 + 0 = 4$. Applying Spearman's formula for $n = 6$:

$$\rho_s = 1 - \frac{6 \sum_{i=1}^6 d_i^2}{6\left(6^2 - 1\right)} = 1 - \frac{6(4)}{6(35)} = 1 - \frac{4}{35} = \frac{31}{35} \approx 0.8857$$

### Solution, step 2: Concordant/Discordant Pair Enumeration and Kendall's $\tau_a$ (Part A)

Since $X_1 < X_2 < \dots < X_6$ are ordered by $R_i = i$, for each $i \in \{1, \dots, 5\}$ and $j > i$, a pair $(i, j)$ is **concordant** if $S_j > S_i$ and **discordant** if $S_j < S_i$. Inspecting $S = (2, 1, 4, 3, 5, 6)$ from left to right across all $\binom{6}{2} = 15$ pairs:
- From $i = 1$ ($S_1 = 2$ vs. $\{1, 4, 3, 5, 6\}$): $4$ larger ($\{4, 3, 5, 6\}$), $1$ smaller ($\{1\}$) $\implies c_1 = 4, d_1 = 1$.
- From $i = 2$ ($S_2 = 1$ vs. $\{4, 3, 5, 6\}$): $4$ larger ($\{4, 3, 5, 6\}$), $0$ smaller $\implies c_2 = 4, d_2 = 0$.
- From $i = 3$ ($S_3 = 4$ vs. $\{3, 5, 6\}$): $2$ larger ($\{5, 6\}$), $1$ smaller ($\{3\}$) $\implies c_3 = 2, d_3 = 1$.
- From $i = 4$ ($S_4 = 3$ vs. $\{5, 6\}$): $2$ larger ($\{5, 6\}$), $0$ smaller $\implies c_4 = 2, d_4 = 0$.
- From $i = 5$ ($S_5 = 5$ vs. $\{6\}$): $1$ larger ($\{6\}$), $0$ smaller $\implies c_5 = 1, d_5 = 0$.

Summing across all $15$ pairs gives $N_c = 4 + 4 + 2 + 2 + 1 = 13$ concordant pairs and $N_d = 1 + 0 + 1 + 0 + 0 = 2$ discordant pairs ($S_K = N_c - N_d = 13 - 2 = 11$). Therefore, Kendall's rank correlation is:

$$\hat{\tau}_a = \frac{N_c - N_d}{\binom{6}{2}} = \frac{13 - 2}{15} = \frac{11}{15} \approx 0.7333$$

with standardized normal score $Z_\tau = \frac{11}{\sqrt{6(5)(17)/18}} = \frac{11}{\sqrt{28.3333}} = \frac{11}{5.3229} \approx 2.0665$.

### Solution, step 3: Exact Enumeration of the Fisher–Pitman Permutation Test (Part B)

The pooled order statistics across the $N = 3 + 3 = 6$ patients are $\mathbf{z}_{(\cdot)} = \{10, 13, 19, 20, 22, 25\}$, with grand sum $S_{\text{total}} = 10 + 13 + 19 + 20 + 22 + 25 = 109$. There are exactly:

$$M = \binom{6}{3} = \frac{6!}{3! 3!} = 20 \text{ equally likely partitions}$$

In the observed sample, the treatment group $\mathcal{X}_{\text{obs}} = \{19, 22, 25\}$ has sum $S_{X,\text{obs}} = 19 + 22 + 25 = 66$ and observed mean difference $\bar{X}_{\text{obs}} - \bar{Y}_{\text{obs}} = \frac{66}{3} - \frac{43}{3} = 22.00 - 14.33 = +7.67$. Let us check which of the $20$ subsets of size $3$ drawn from $\{10, 13, 19, 20, 22, 25\}$ achieve a sum $S_X^* \ge 66$:
- Maximum possible sum: $\{20, 22, 25\} \implies S_X^* = 67$ ($\bar{X}^* - \bar{Y}^* = \frac{67 - 42}{3} = +8.33$)
- Second largest sum: $\{19, 22, 25\} \implies S_X^* = 66$ ($\bar{X}^* - \bar{Y}^* = \frac{66 - 43}{3} = +7.67$, the observed sample!)
- Third largest sum: $\{19, 20, 25\} \implies S_X^* = 64 < 66$.

Only **2 out of the 20 partitions** ($\{20, 22, 25\}$ and $\{19, 22, 25\}$) satisfy $S_X^* \ge 66$ (and symmetrically, only $2$ partitions—$\{10, 13, 19\}$ with $S_X^* = 42$ and $\{10, 13, 20\}$ with $S_X^* = 43$—satisfy $|\bar{X}^* - \bar{Y}^*| \ge 7.67$ in the opposite tail). Therefore:

$$p_{\text{one-sided}} = \frac{2}{20} = 0.1000, \qquad p_{\text{two-sided}} = \frac{2 + 2}{20} = \frac{4}{20} = 0.2000$$
