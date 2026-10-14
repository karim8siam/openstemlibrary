# Unit 4: Cluster Sampling and Multistage Sampling

## Rationale, Operational Architecture and Hierarchical Populations

In the theoretical formulation of simple random sampling and stratified random sampling, the statistical inquiry presumes the immediate availability of an exhaustive, pristine sampling frame listing every individual observation unit (such as a person, patient, or household). In large-scale national, regional, and industrial surveys, this ideal assumption fails completely. Constructing and continuously updating a comprehensive register of tens of millions of dispersed elements across an entire subcontinent is often financially impossible, logistically prohibitive, and outdated before field enumeration can even commence. Moreover, even if such an element-level frame were theoretically obtainable, a pure simple random sample of individual households scattered across a massive geographical territory would require interviewers to travel exorbitant distances to conduct single, isolated interviews, inflating per-unit data collection costs to unsustainable levels.

To overcome these structural limitations, survey sampling theory introduces **cluster sampling**. Instead of selecting individual observation units directly from an exhaustive master list, the population is partitioned into identifiable, mutually exclusive, and collectively exhaustive groups termed **clusters** or **Primary Sampling Units (PSUs)**. A sampling frame of these clusters is constructed—an operational task that is vastly simpler and less expensive than listing all elements, because clusters correspond to existing administrative or physical entities such as census enumeration areas, municipalities, villages, school districts, or industrial plants. A probability sample of clusters is then selected. 

In **single-stage cluster sampling**, every observation unit within each selected cluster is completely enumerated. In **multistage sampling** (or sub-sampling), the selection process proceeds hierarchically through successive tiers: first, a sample of primary sampling units is drawn; subsequently, within each selected primary unit, a probability sample of **Secondary Sampling Units (SSUs)** (such as dwellings or classrooms) is selected; in three-stage designs, ultimate **Tertiary Sampling Units (TSUs)** (such as individuals or students) are sampled within the secondary units.

Cluster sampling therefore resolves two paramount operational bottlenecks:
1. **Frame Construction Efficiency**: A complete list of all ultimate elements in the population is never required. The statistician requires only a listing of primary units at the initial stage. Detailed listings of secondary units are compiled exclusively within the small subset of primary units that are actually selected into the sample.
2. **Fieldwork and Logistical Economy**: By concentrating interviews within geographically compact clusters, travel time, fuel expenditures, lodging overhead, and field supervision logistics are reduced by orders of magnitude compared to unclustered, dispersed sampling designs.

However, this substantial operational efficiency comes at an inevitable statistical price. In human, ecological, and economic populations, elements residing within the same cluster tend to resemble one another more closely than elements chosen at random from different clusters. Households in the same village share the same agro-climatic conditions, local markets, public infrastructure, and socioeconomic status. Students in the same classroom share the same teacher, curriculum, and physical learning environment. Consequently, observing multiple elements from the same cluster provides partially redundant information. This internal homogeneity induces a positive correlation among units within clusters, leading to an inflation of sampling variance relative to simple random sampling of the same total number of elements. The central mathematical challenge of cluster sampling is to formalize, quantify, and minimize this variance inflation through rigorous design choices.

---

## Single-Stage Cluster Sampling: Equal Cluster Sizes

We begin by establishing the formal notation and mathematical framework for single-stage cluster sampling where all clusters contain an identical number of observation units. While equal cluster sizes represent an idealized scenario, this classical formulation provides the clearest mathematical foundation for understanding variance decomposition and intracluster correlation.

### Population Structure and Notation

Consider a finite population $U$ partitioned into $N$ distinct clusters, with each cluster containing exactly $M$ observation units. The total number of elements in the entire finite population is therefore:
$$M_0 = N M$$

Let $y_{ij}$ denote the value of the survey characteristic for the $j$-th observation unit ($j = 1, 2, \dots, M$) within the $i$-th cluster ($i = 1, 2, \dots, N$).

We define the primary population parameters:
1. **Cluster Total for Cluster $i$**:
   $$Y_i = \sum_{j=1}^M y_{ij}$$
2. **Cluster Mean for Cluster $i$**:
   $$\bar{Y}_i = \frac{Y_i}{M} = \frac{1}{M} \sum_{j=1}^M y_{ij}$$
3. **Overall Population Total**:
   $$Y = \sum_{i=1}^N Y_i = \sum_{i=1}^N \sum_{j=1}^M y_{ij}$$
4. **Overall Population Mean per Observation Unit**:
   $$\bar{\bar{Y}} = \frac{Y}{N M} = \frac{1}{N} \sum_{i=1}^N \bar{Y}_i$$
   Notice that because all clusters have identical size $M$, the overall population mean per element $\bar{\bar{Y}}$ is exactly equal to the simple unweighted average of the $N$ cluster means $\bar{Y}_i$.

### Population Variance Decomposition

The total variability of the characteristic $y$ across all $NM$ elements in the finite population is quantified by the overall population variance:
$$S^2 = \frac{1}{NM - 1} \sum_{i=1}^N \sum_{j=1}^M (y_{ij} - \bar{\bar{Y}})^2$$

In cluster sampling, this total variation is decomposed into two orthogonal components: variation between cluster means (**between-cluster variance**) and variation among elements within the same cluster (**within-cluster variance**).

To formalize this decomposition, we express the total sum of squares ($\text{SST}$) as:
$$\text{SST} = \sum_{i=1}^N \sum_{j=1}^M (y_{ij} - \bar{\bar{Y}})^2 = \sum_{i=1}^N \sum_{j=1}^M \left[ (\bar{Y}_i - \bar{\bar{Y}}) + (y_{ij} - \bar{Y}_i) \right]^2$$

Expanding the squared bracket:
$$\text{SST} = \sum_{i=1}^N \sum_{j=1}^M (\bar{Y}_i - \bar{\bar{Y}})^2 + \sum_{i=1}^N \sum_{j=1}^M (y_{ij} - \bar{Y}_i)^2 + 2 \sum_{i=1}^N \sum_{j=1}^M (\bar{Y}_i - \bar{\bar{Y}})(y_{ij} - \bar{Y}_i)$$

The cross-product term evaluates to zero identically because $\sum_{j=1}^M (y_{ij} - \bar{Y}_i) = 0$ for every cluster $i$:
$$\sum_{i=1}^N (\bar{Y}_i - \bar{\bar{Y}}) \left[ \sum_{j=1}^M (y_{ij} - \bar{Y}_i) \right] = \sum_{i=1}^N (\bar{Y}_i - \bar{\bar{Y}}) \cdot 0 = 0$$

Therefore, we have the exact algebraic identity:
$$\sum_{i=1}^N \sum_{j=1}^M (y_{ij} - \bar{\bar{Y}})^2 = M \sum_{i=1}^N (\bar{Y}_i - \bar{\bar{Y}})^2 + \sum_{i=1}^N \sum_{j=1}^M (y_{ij} - \bar{Y}_i)^2$$
which is symbolically expressed as:
$$\text{SST} = \text{SSB} + \text{SSW}$$
where $\text{SSB}$ is the between-cluster sum of squares and $\text{SSW}$ is the within-cluster sum of squares.

We define the corresponding mean squares:
1. **Between-Cluster Mean Square (per element)**:
   $$S_b^2 = \frac{1}{N - 1} \sum_{i=1}^N (\bar{Y}_i - \bar{\bar{Y}})^2$$
   Note that the variance of the cluster totals $Y_i = M \bar{Y}_i$ is $S_t^2 = M^2 S_b^2$.
2. **Within-Cluster Mean Square**:
   $$S_w^2 = \frac{1}{N(M - 1)} \sum_{i=1}^N \sum_{j=1}^M (y_{ij} - \bar{Y}_i)^2 = \frac{1}{N} \sum_{i=1}^N S_i^2$$
   where $S_i^2 = \frac{1}{M - 1} \sum_{j=1}^M (y_{ij} - \bar{Y}_i)^2$ is the variance among elements within cluster $i$.

The relation between the overall variance $S^2$, between-cluster mean square $S_b^2$, and within-cluster mean square $S_w^2$ is obtained by dividing the sum of squares identity by $NM - 1$:
$$(NM - 1) S^2 = M(N - 1) S_b^2 + N(M - 1) S_w^2$$

For large populations where $N$ and $NM$ are sufficiently large so that $N-1 \approx N$ and $NM-1 \approx NM$, dividing through by $NM$ yields the familiar asymptotic relationship:
$$S^2 \approx S_b^2 + \frac{M - 1}{M} S_w^2$$

---

## The Intracluster (Intraclass) Correlation Coefficient

The degree of internal similarity among units belonging to the same cluster is mathematically captured by the **intracluster correlation coefficient** (also known as the intraclass correlation coefficient), denoted by $\rho$. Understanding $\rho$ is essential to mastering cluster sampling, as it dictates the entire magnitude of design efficiency and variance inflation.

### Formal Definition of $\rho$

In finite population sampling, the intracluster correlation coefficient $\rho$ is defined as the Pearson product-moment correlation coefficient between pairs of distinct elements belonging to the same cluster, evaluated across all possible distinct pairs in the entire population.

In cluster $i$, there are $M$ elements, yielding $M(M - 1)$ ordered pairs of distinct elements $(y_{ij}, y_{ik})$ with $j \ne k$. Summing across all $N$ clusters, there are exactly $N M (M - 1)$ such ordered pairs. The intracluster correlation coefficient is defined as:
$$\rho = \frac{\sum_{i=1}^N \sum_{j=1}^M \sum_{k \ne j}^M (y_{ij} - \bar{\bar{Y}})(y_{ik} - \bar{\bar{Y}})}{(M - 1) \sum_{i=1}^N \sum_{j=1}^M (y_{ij} - \bar{\bar{Y}})^2}$$

To express $\rho$ in terms of the between-cluster and within-cluster mean squares, we manipulate the numerator. For any cluster $i$:
$$\left[ \sum_{j=1}^M (y_{ij} - \bar{\bar{Y}}) \right]^2 = \sum_{j=1}^M (y_{ij} - \bar{\bar{Y}})^2 + \sum_{j=1}^M \sum_{k \ne j}^M (y_{ij} - \bar{\bar{Y}})(y_{ik} - \bar{\bar{Y}})$$

Recognizing that $\sum_{j=1}^M (y_{ij} - \bar{\bar{Y}}) = M (\bar{Y}_i - \bar{\bar{Y}})$, we have:
$$M^2 (\bar{Y}_i - \bar{\bar{Y}})^2 = \sum_{j=1}^M (y_{ij} - \bar{\bar{Y}})^2 + \sum_{j=1}^M \sum_{k \ne j}^M (y_{ij} - \bar{\bar{Y}})(y_{ik} - \bar{\bar{Y}})$$

Summing both sides across all $N$ clusters:
$$M^2 \sum_{i=1}^N (\bar{Y}_i - \bar{\bar{Y}})^2 = \sum_{i=1}^N \sum_{j=1}^M (y_{ij} - \bar{\bar{Y}})^2 + \sum_{i=1}^N \sum_{j=1}^M \sum_{k \ne j}^M (y_{ij} - \bar{\bar{Y}})(y_{ik} - \bar{\bar{Y}})$$

Substituting our sum of squares definitions:
$$M^2 (N - 1) S_b^2 = (NM - 1) S^2 + \sum_{i=1}^N \sum_{j=1}^M \sum_{k \ne j}^M (y_{ij} - \bar{\bar{Y}})(y_{ik} - \bar{\bar{Y}})$$

Thus, the numerator of $\rho$ is precisely:
$$\sum_{i=1}^N \sum_{j=1}^M \sum_{k \ne j}^M (y_{ij} - \bar{\bar{Y}})(y_{ik} - \bar{\bar{Y}}) = M^2 (N - 1) S_b^2 - (NM - 1) S^2$$

Dividing this by the denominator $(M - 1)(NM - 1) S^2$, we obtain the exact algebraic formulation for $\rho$:
$$\rho = \frac{M^2 (N - 1) S_b^2 - (NM - 1) S^2}{(M - 1)(NM - 1) S^2}$$

Rearranging this formula gives an exact expression for the between-cluster variance $S_b^2$ in terms of the total variance $S^2$ and the intracluster correlation $\rho$:
$$M(N - 1) S_b^2 = \frac{NM - 1}{M} S^2 \left[ 1 + (M - 1) \rho \right]$$

When $N$ is reasonably large such that $\frac{NM - 1}{M(N - 1)} \approx 1$, this simplifies to the fundamental relationship:
$$S_b^2 \approx \frac{S^2}{M} \left[ 1 + (M - 1) \rho \right]$$

### Mathematical Bounds of $\rho$

Unlike a standard bivariate correlation coefficient, which ranges over the symmetric interval $[-1, 1]$, the intracluster correlation coefficient $\rho$ is asymmetric:
$$-\frac{1}{M - 1} \le \rho \le 1$$

To prove this fundamental result:
1. **Upper Bound ($\rho \le 1$)**: 
   The between-cluster mean square $S_b^2$ is bounded above by the total variance scaled by $M$. If all units within every cluster are identical (complete internal homogeneity), then for every cluster $i$, $y_{ij} = \bar{Y}_i$ for all $j$. In this extreme scenario, $S_w^2 = 0$, so $\text{SSW} = 0$, which implies $\text{SST} = \text{SSB}$. Then:
   $$(NM - 1) S^2 = M(N - 1) S_b^2$$
   Substituting this into the definition of $\rho$:
   $$\rho = \frac{M(NM - 1) S^2 - (NM - 1) S^2}{(M - 1)(NM - 1) S^2} = \frac{(M - 1)(NM - 1) S^2}{(M - 1)(NM - 1) S^2} = 1$$
   Hence, the maximum value of $\rho$ is $+1$, achieved when clusters are completely internally homogeneous.

2. **Lower Bound ($\rho \ge -\frac{1}{M - 1}$)**:
   The between-cluster mean square $S_b^2$ is a sum of squared deviations and must satisfy $S_b^2 \ge 0$. Setting $S_b^2 = 0$ corresponds to the case where all cluster means are identical: $\bar{Y}_1 = \bar{Y}_2 = \dots = \bar{Y}_N = \bar{\bar{Y}}$. Under this condition:
   $$\rho = \frac{0 - (NM - 1) S^2}{(M - 1)(NM - 1) S^2} = -\frac{1}{M - 1}$$
   Therefore, the minimum possible value of $\rho$ is $-\frac{1}{M - 1}$.

### Substantive Interpretation in Empirical Practice

In practical survey work, what values does $\rho$ assume?
- When $M$ is large (for example, census enumeration areas containing $M = 100$ or $200$ households), the lower bound $-\frac{1}{M - 1}$ is practically zero (e.g., $-0.01$ or $-0.005$). Thus, negative values of $\rho$ are virtually impossible in large clusters.
- Because human settlements, natural environments, and socioeconomic characteristics naturally cluster in space, elements within the same geographic cluster are systematically more similar to one another than to elements from distant clusters. Therefore, in empirical surveys, $\rho$ is almost universally **positive**.
- Even seemingly small values of $\rho$ (e.g., $\rho = 0.05$ or $0.10$) have devastating effects on precision when cluster size $M$ is substantial. For instance, if $M = 101$ and $\rho = 0.05$, the multiplier $1 + (M - 1)\rho = 1 + 100(0.05) = 6.0$. This means the sampling variance is inflated by a factor of 6 compared to simple random sampling.

---

## Estimation and Variance in Single-Stage Cluster Sampling

Suppose a simple random sample without replacement (SRSWOR) of $n$ clusters is selected from the $N$ clusters in the population. Every unit within each selected cluster is enumerated, yielding a total observed sample of $n M$ elements.

### The Sample Mean Estimator

Let $s \subset \{1, 2, \dots, N\}$ denote the set of $n$ sampled cluster indices. The sample mean per observation unit is:
$$\bar{y}_{cl} = \frac{1}{n M} \sum_{i \in s} \sum_{j=1}^M y_{ij} = \frac{1}{n} \sum_{i \in s} \bar{y}_i$$
where $\bar{y}_i = \frac{1}{M} \sum_{j=1}^M y_{ij} = \bar{Y}_i$ is the exact mean of the $i$-th cluster, since all units in the selected cluster are observed without error.

Because the clusters are selected via SRSWOR from $N$ clusters, $\bar{y}_{cl}$ is formally equivalent to the sample mean of $n$ observations drawn from a finite population of $N$ cluster means $\{\bar{Y}_1, \dots, \bar{Y}_N\}$.

### Expectation and Design Unbiasedness

Taking the design expectation under the randomization distribution:
$$E(\bar{y}_{cl}) = E\left[ \frac{1}{n} \sum_{i \in s} \bar{Y}_i \right] = \frac{1}{N} \sum_{i=1}^N \bar{Y}_i = \bar{\bar{Y}}$$
Thus, the cluster sample mean $\bar{y}_{cl}$ is an strictly design-unbiased estimator of the overall population mean per element $\bar{\bar{Y}}$.

Similarly, the estimator for the population total $Y$ is:
$$\hat{Y}_{cl} = N M \bar{y}_{cl} = \frac{N}{n} \sum_{i \in s} Y_i$$
which is strictly design-unbiased: $E(\hat{Y}_{cl}) = Y$.

### Sampling Variance Derivation

Applying the classical finite-population variance formula for SRSWOR of $n$ units from $N$ units:
$$V(\bar{y}_{cl}) = \frac{1 - f}{n} S_b^2$$
where $f = \frac{n}{N}$ is the primary sampling fraction, and $S_b^2 = \frac{1}{N - 1} \sum_{i=1}^N (\bar{Y}_i - \bar{\bar{Y}})^2$ is the between-cluster mean square.

Substituting our relation between $S_b^2$, $S^2$, and $\rho$:
$$V(\bar{y}_{cl}) = \frac{1 - f}{n} \cdot \frac{NM - 1}{M(N - 1)} \frac{S^2}{M} \left[ 1 + (M - 1)\rho \right]$$

For large $N$, this expression simplifies to the fundamental equation:
$$V(\bar{y}_{cl}) \approx \frac{1 - f}{n M} S^2 \left[ 1 + (M - 1)\rho \right]$$

Now compare this with the variance of a simple random sample without replacement of the same total number of elements, $m_{tot} = n M$:
$$V_{srs}(\bar{y}) = \frac{1 - f_{elem}}{n M} S^2$$
where $f_{elem} = \frac{n M}{N M} = \frac{n}{N} = f$.

The ratio of the two variances is the **Design Effect ($\text{Deff}$)**:
$$\text{Deff} = \frac{V(\bar{y}_{cl})}{V_{srs}(\bar{y})} \approx 1 + (M - 1)\rho$$

This celebrated formula, popularized by Leslie Kish (1965), proves that:
1. If $\rho = 0$ (elements within clusters are as heterogeneous as the general population), $\text{Deff} = 1$, and cluster sampling is just as efficient as simple random sampling.
2. If $\rho > 0$, $\text{Deff} > 1$, indicating variance inflation. The inflation grows linearly with the cluster size $M$.
3. If $\rho < 0$ (elements within clusters are more heterogeneous than the population at large—an artificial condition rarely found in geography), $\text{Deff} < 1$, and cluster sampling is actually more precise than simple random sampling.

### Effective Sample Size

Because the design effect quantifies variance inflation, it reveals how many independent, uncorrelated observations the cluster sample is actually worth. The **effective sample size** ($n_{eff}$) is defined as:
$$n_{eff} = \frac{n M}{\text{Deff}} = \frac{n M}{1 + (M - 1)\rho}$$

For example, if a survey samples $n = 50$ clusters of size $M = 20$ (total elements $n M = 1,000$) and the intracluster correlation is $\rho = 0.10$:
$$\text{Deff} = 1 + (20 - 1)(0.10) = 1 + 1.9 = 2.9$$
$$n_{eff} = \frac{1000}{2.9} \approx 345$$
Although the survey interviewers enumerate $1,000$ individuals, the statistical information gathered is equivalent to only $345$ individuals selected through pure simple random sampling. The remaining $655$ interviews represent informational redundancy caused by within-cluster correlation.

### Unbiased Estimation of Variance from Sample Data

In practice, the true between-cluster mean square $S_b^2$ is unknown. We estimate it from the sample using the sample between-cluster mean square:
$$s_b^2 = \frac{1}{n - 1} \sum_{i \in s} (\bar{y}_i - \bar{y}_{cl})^2$$

Since the $n$ cluster means are selected by SRSWOR from the $N$ cluster means, $s_b^2$ is an strictly unbiased estimator of $S_b^2$:
$$E(s_b^2) = S_b^2$$

Consequently, the unbiased estimator of the variance of the cluster sample mean is:
$$\hat{V}(\bar{y}_{cl}) = \frac{1 - f}{n} s_b^2 = \frac{1 - f}{n(n - 1)} \sum_{i \in s} (\bar{y}_i - \bar{y}_{cl})^2$$

Notice the remarkable simplicity of this estimator: to compute the standard error of a single-stage cluster sample, one does **not** need to compute within-cluster variances. One treats the observed cluster totals or cluster means as the fundamental data points and applies the standard SRS variance formula directly at the cluster level.

---

## Single-Stage Cluster Sampling with Unequal Cluster Sizes

In real-world surveys, natural clusters (such as villages, city blocks, hospital wards, or schools) rarely contain equal numbers of observation units. Let $M_i$ denote the number of observation units in cluster $i$ ($i = 1, 2, \dots, N$). The total population size is:
$$M_0 = \sum_{i=1}^N M_i$$
and the average cluster size is $\bar{M} = \frac{M_0}{N}$.

When cluster sizes $M_i$ vary, several competing estimators of the population mean per element $\bar{\bar{Y}} = \frac{Y}{M_0}$ can be constructed, each with distinct statistical properties.

### 1. The Simple Mean of Cluster Means (Unweighted Estimator)

A naive estimator is the simple average of the sample cluster means:
$$\bar{y}_u = \frac{1}{n} \sum_{i \in s} \bar{y}_i$$
where $\bar{y}_i = \frac{1}{M_i} \sum_{j=1}^{M_i} y_{ij} = \bar{Y}_i$.

The expectation of this estimator is:
$$E(\bar{y}_u) = \frac{1}{N} \sum_{i=1}^N \bar{Y}_i$$
Notice that $E(\bar{y}_u)$ is equal to $\bar{\bar{Y}} = \frac{\sum_{i=1}^N M_i \bar{Y}_i}{\sum_{i=1}^N M_i}$ **if and only if** the cluster size $M_i$ is completely uncorrelated with the cluster mean $\bar{Y}_i$. In economic and social applications, cluster size is frequently correlated with the attribute of interest (e.g., larger cities have higher average household incomes or higher crime rates). Therefore, $\bar{y}_u$ is generally **biased** for $\bar{\bar{Y}}$:
$$\text{Bias}(\bar{y}_u) = \frac{1}{N} \sum_{i=1}^N \bar{Y}_i - \bar{\bar{Y}} = -\frac{1}{\bar{M}} \frac{1}{N} \sum_{i=1}^N (M_i - \bar{M})(\bar{Y}_i - \bar{\bar{Y}})$$
Unless the covariance between cluster size and cluster mean is known to be zero, this unweighted estimator should be avoided.

### 2. The Design-Unbiased Horvitz–Thompson Estimator

To obtain a strictly design-unbiased estimator when clusters are selected with equal probability (SRSWOR), we first estimate the population total $Y$ by scaling the sample cluster totals:
$$\hat{Y}_{unb} = \frac{N}{n} \sum_{i \in s} Y_i$$
where $Y_i = \sum_{j=1}^{M_i} y_{ij}$ is the total for cluster $i$.

Dividing by the known total population size $M_0$:
$$\hat{\bar{Y}}_{unb} = \frac{\hat{Y}_{unb}}{M_0} = \frac{N}{n M_0} \sum_{i \in s} Y_i = \frac{1}{n \bar{M}} \sum_{i \in s} Y_i$$

Because $E\left[ \frac{N}{n} \sum_{i \in s} Y_i \right] = \sum_{i=1}^N Y_i = Y$, this estimator is strictly unbiased:
$$E(\hat{\bar{Y}}_{unb}) = \bar{\bar{Y}}$$

The exact variance of $\hat{\bar{Y}}_{unb}$ under SRSWOR of clusters is:
$$V(\hat{\bar{Y}}_{unb}) = \frac{1 - f}{n \bar{M}^2} S_u^2$$
where $S_u^2 = \frac{1}{N - 1} \sum_{i=1}^N (Y_i - \bar{M} \bar{\bar{Y}})^2 = \frac{1}{N - 1} \sum_{i=1}^N (Y_i - \bar{Y}_t)^2$, and $\bar{Y}_t = \frac{Y}{N}$ is the average cluster total.

While strictly unbiased, $\hat{\bar{Y}}_{unb}$ suffers from a severe practical drawback: its variance depends on the variability of the cluster totals $Y_i$. Since $Y_i = M_i \bar{Y}_i$, wide variation in cluster sizes $M_i$ induces massive variation in $Y_i$, resulting in an unacceptably large sampling variance. Furthermore, calculating this estimator requires knowing the exact population total size $M_0$, which is frequently unknown when conducting surveys in developing or dynamic settings.

### 3. The Ratio-to-Size Estimator (The Combined Cluster Mean)

The standard, most widely adopted estimator in survey practice is the ratio estimator:
$$\hat{\bar{Y}}_R = \frac{\sum_{i \in s} Y_i}{\sum_{i \in s} M_i} = \frac{\sum_{i \in s} M_i \bar{y}_i}{\sum_{i \in s} M_i}$$

This estimator divides the total sample aggregate of the characteristic $y$ by the total number of elements actually observed in the sample clusters. It is a ratio of two random variables: the estimated total of $y$ and the estimated total number of elements.

#### Key Advantages of $\hat{\bar{Y}}_R$:
1. **Self-Weighting and Operational Feasibility**: It does not require knowledge of the total population size $M_0$.
2. **Substantial Variance Reduction**: The cluster total $Y_i$ is typically strongly correlated with cluster size $M_i$. By dividing by $\sum_{i \in s} M_i$, the ratio estimator absorbs the fluctuations in cluster sizes, dramatically dampening sampling variability.

#### Statistical Properties:
Like all ratio estimators, $\hat{\bar{Y}}_R$ is technically biased in finite samples, but its bias is of order $O(1/n)$ and becomes negligible when the number of sampled clusters $n$ exceeds 30.

Using a first-order Taylor series approximation, the mean squared error (approximate variance) is:
$$V(\hat{\bar{Y}}_R) \approx \frac{1 - f}{n \bar{M}^2} \frac{1}{N - 1} \sum_{i=1}^N M_i^2 (\bar{Y}_i - \bar{\bar{Y}})^2$$

An approximately unbiased sample estimator of this variance is:
$$\hat{V}(\hat{\bar{Y}}_R) = \frac{1 - f}{n \bar{m}^2} \frac{1}{n - 1} \sum_{i \in s} M_i^2 (\bar{y}_i - \hat{\bar{Y}}_R)^2$$
where $\bar{m} = \frac{1}{n} \sum_{i \in s} M_i$ is the average cluster size observed in the sample.

When cluster sizes $M_i$ vary drastically, simple random sampling of clusters followed by ratio estimation is still sub-optimal. The modern standard methodology is to select clusters with **Probability Proportional to Size (PPS)**, which we investigate thoroughly in Unit 5.

---

## Two-Stage Cluster Sampling: Hierarchy, Variance Decomposition and Estimation

When primary sampling units are large (such as entire districts, cities, or large health facility catchment areas), surveying every single element within selected PSUs is neither affordable nor necessary. Instead, the statistician implements **two-stage cluster sampling**:
- **Stage 1**: Select a probability sample of $n$ primary sampling units (PSUs) out of $N$.
- **Stage 2**: Within each selected PSU $i \in s$, select a probability sample of $m_i$ secondary sampling units (SSUs) out of the $M_i$ available elements.

### Conditional Expectation and the Law of Total Variance

The mathematical analysis of multistage sampling relies on the fundamental laws of iterated conditional expectation and conditional variance. Let $\hat{\theta}$ be an estimator of a population parameter $\theta$, and let $s_1$ denote the specific sample of PSUs chosen at the first stage.

1. **Law of Iterated Expectation**:
   $$E(\hat{\theta}) = E_1\left[ E_2(\hat{\theta} \mid s_1) \right]$$
   where $E_2(\cdot \mid s_1)$ denotes expectation over all possible second-stage samples conditional on the fixed first-stage sample $s_1$, and $E_1(\cdot)$ denotes expectation over all possible first-stage samples.

2. **Law of Total Variance (Variance Decomposition Theorem)**:
   $$V(\hat{\theta}) = V_1\left( E_2(\hat{\theta} \mid s_1) \right) + E_1\left( V_2(\hat{\theta} \mid s_1) \right)$$
   This decomposition partitions the total variance into two distinct structural mechanisms:
   - **First-Stage Variance Component ($V_1$)**: The variability arising because different sets of PSUs could have been chosen at the first stage.
   - **Second-Stage Variance Component ($E_1 V_2$)**: The average variability introduced by sampling a subset of SSUs within the selected PSUs, rather than enumerating them completely.

### Two-Stage Sampling with Equal Cluster and Sub-Sample Sizes

Consider a population of $N$ clusters, each containing $M$ elements. At the first stage, $n$ clusters are selected using SRSWOR ($f_1 = n/N$). At the second stage, $m$ elements are selected from each chosen cluster using SRSWOR ($f_2 = m/M$). The overall sampling fraction is $f = f_1 f_2 = \frac{n m}{N M}$.

The overall sample mean is:
$$\bar{\bar{y}} = \frac{1}{n m} \sum_{i=1}^n \sum_{j=1}^m y_{ij} = \frac{1}{n} \sum_{i=1}^n \bar{y}_i$$
where $\bar{y}_i = \frac{1}{m} \sum_{j=1}^m y_{ij}$ is the sample mean of the $m$ elements drawn from cluster $i$.

#### Unbiasedness:
First, condition on the selected primary units $s_1$:
$$E_2(\bar{y}_i \mid s_1) = \bar{Y}_i \implies E_2(\bar{\bar{y}} \mid s_1) = \frac{1}{n} \sum_{i=1}^n \bar{Y}_i$$
Taking the first-stage expectation over all possible selections of $s_1$:
$$E_1\left[ E_2(\bar{\bar{y}} \mid s_1) \right] = E_1\left[ \frac{1}{n} \sum_{i=1}^n \bar{Y}_i \right] = \frac{1}{N} \sum_{i=1}^N \bar{Y}_i = \bar{\bar{Y}}$$
Thus, $\bar{\bar{y}}$ is strictly design-unbiased.

#### Derivation of the Exact Sampling Variance:
Using the Law of Total Variance:
$$V(\bar{\bar{y}}) = V_1\left( E_2(\bar{\bar{y}} \mid s_1) \right) + E_1\left( V_2(\bar{\bar{y}} \mid s_1) \right)$$

1. **First-Stage Component**:
   Since $E_2(\bar{\bar{y}} \mid s_1) = \frac{1}{n} \sum_{i=1}^n \bar{Y}_i$, this is the sample mean of $n$ units drawn by SRSWOR from the population of $N$ cluster means. Therefore:
   $$V_1\left( E_2(\bar{\bar{y}} \mid s_1) \right) = \frac{1 - f_1}{n} S_b^2$$
   where $S_b^2 = \frac{1}{N - 1} \sum_{i=1}^N (\bar{Y}_i - \bar{\bar{Y}})^2$.

2. **Second-Stage Component**:
   Conditional on $s_1$, the sub-samples drawn within different PSUs are completely independent. Therefore, the variance of the sum is the sum of the variances:
   $$V_2(\bar{\bar{y}} \mid s_1) = V_2\left( \frac{1}{n} \sum_{i=1}^n \bar{y}_i \;\middle|\; s_1 \right) = \frac{1}{n^2} \sum_{i=1}^n V_2(\bar{y}_i \mid s_1)$$
   Within cluster $i$, an SRSWOR of $m$ elements is drawn from $M$ elements. Hence:
   $$V_2(\bar{y}_i \mid s_1) = \frac{1 - f_2}{m} S_i^2$$
   where $S_i^2 = \frac{1}{M - 1} \sum_{j=1}^M (y_{ij} - \bar{Y}_i)^2$.
   Substituting this into the sum:
   $$V_2(\bar{\bar{y}} \mid s_1) = \frac{1 - f_2}{n^2 m} \sum_{i=1}^n S_i^2$$
   Now, take the expectation $E_1$ over all first-stage samples. Since the $n$ clusters are chosen by SRSWOR from $N$:
   $$E_1\left[ \frac{1}{n} \sum_{i=1}^n S_i^2 \right] = \frac{1}{N} \sum_{i=1}^N S_i^2 = S_w^2$$
   Therefore:
   $$E_1\left( V_2(\bar{\bar{y}} \mid s_1) \right) = \frac{1 - f_2}{n m} S_w^2$$

Combining both components yields the celebrated **Two-Stage Variance Formula**:
$$V(\bar{\bar{y}}) = \frac{1 - f_1}{n} S_b^2 + \frac{1 - f_2}{n m} S_w^2$$

#### Structural Analysis of the Variance Formula:
Notice how the formula behaves under limiting design choices:
- If $m = M$, then $f_2 = 1$, and the second term vanishes completely:
  $$V(\bar{\bar{y}}) = \frac{1 - f_1}{n} S_b^2$$
  This matches our earlier single-stage cluster sampling variance exactly.
- If $n = N$, then $f_1 = 1$, and the first term vanishes:
  $$V(\bar{\bar{y}}) = \frac{1 - f_2}{N m} S_w^2 = \frac{1 - f_2}{n_{tot}} S_w^2$$
  This matches stratified random sampling with proportional allocation, where every cluster serves as a stratum.
- In two-stage cluster sampling, both terms are present. The first term represents the penalty for not sampling all clusters; the second term represents the penalty for not enumerating all elements within the sampled clusters.

### Sample Variance Estimation in Two-Stage Sampling

To estimate $V(\bar{\bar{y}})$ from empirical sample data, we define two sample mean squares:
1. **Sample Between-Cluster Mean Square**:
   $$s_1^2 = \frac{1}{n - 1} \sum_{i=1}^n (\bar{y}_i - \bar{\bar{y}})^2$$
2. **Sample Within-Cluster Mean Square**:
   $$s_2^2 = \frac{1}{n(m - 1)} \sum_{i=1}^n \sum_{j=1}^m (y_{ij} - \bar{y}_i)^2 = \frac{1}{n} \sum_{i=1}^n s_i^2$$
   where $s_i^2 = \frac{1}{m - 1} \sum_{j=1}^m (y_{ij} - \bar{y}_i)^2$.

It is straightforward to show that $s_2^2$ is an unbiased estimator of the population within-cluster variance:
$$E(s_2^2) = S_w^2$$

However, $s_1^2$ is **not** an unbiased estimator of $S_b^2$. Because $\bar{y}_i$ contains second-stage sampling error as an estimate of $\bar{Y}_i$, $s_1^2$ is inflated:
$$E(s_1^2) = S_b^2 + \frac{1 - f_2}{m} S_w^2$$

Solving for an unbiased estimator of $V(\bar{\bar{y}})$:
$$\hat{V}(\bar{\bar{y}}) = \frac{1 - f_1}{n} s_1^2 + \frac{f_1(1 - f_2)}{n m} s_2^2$$

#### The Ultimate Cluster Principle
Notice what happens when the first-stage sampling fraction $f_1 = \frac{n}{N}$ is small (for example, $f_1 < 0.05$, which is typical in large-scale national surveys where 300 enumeration areas are selected out of 50,000 national enumeration areas):
The term $\frac{f_1(1 - f_2)}{nm} s_2^2$ becomes negligibly small, and $1 - f_1 \approx 1$. 
The variance estimator simplifies to:
$$\hat{V}(\bar{\bar{y}}) \approx \frac{s_1^2}{n} = \frac{1}{n(n - 1)} \sum_{i=1}^n (\bar{y}_i - \bar{\bar{y}})^2$$

This foundational result is known as the **Ultimate Cluster Principle** (Hansen, Hurwitz, and Madow, 1953). When the first-stage sampling fraction is small, the complex internal multistage sampling structure within PSUs can be completely ignored when estimating total variance! The variation among the PSU totals or PSU means automatically captures both the first-stage and second-stage variance components.

---

## Cost Optimization in Two-Stage Sampling

A central operational question in designing a two-stage survey is: Given a fixed total budget, what combination of primary sampling units $n$ and secondary units per PSU $m$ will minimize the sampling variance? Or conversely, to achieve a pre-specified target variance, what allocation minimizes total financial cost?

### Linear Cost Model

In field operations, survey costs are accurately characterized by a linear cost function:
$$C = c_0 + n c_1 + n m c_2$$
where:
- $c_0$ is the fixed overhead cost (planning, frame development, software, administrative management).
- $c_1$ is the cost per Primary Sampling Unit (traveling to the cluster, locating boundaries, listing households, setting up field accommodation).
- $c_2$ is the marginal cost per Secondary Sampling Unit (conducting the interview with a household, administering questionnaires, biometric measurement).
- $C - c_0 = C_{field} = n(c_1 + m c_2)$ is the net operational field budget.

### Optimal Allocation Formula

Ignoring finite population corrections ($f_1 \approx 0, f_2 \approx 0$), the variance of the two-stage mean is:
$$V \approx \frac{S_b^2}{n} + \frac{S_w^2}{n m} = \frac{1}{n} \left( S_b^2 + \frac{S_w^2}{m} \right)$$
and the net field cost is:
$$C_{field} = n (c_1 + m c_2)$$

We seek to minimize $V$ subject to fixed $C_{field}$, or minimize $C_{field}$ subject to fixed $V$. By the Cauchy–Schwarz inequality, the product of variance and cost is minimized when:
$$V \cdot C_{field} = \left( S_b^2 + \frac{S_w^2}{m} \right) (c_1 + m c_2) = c_1 S_b^2 + m c_2 S_b^2 + \frac{c_1 S_w^2}{m} + c_2 S_w^2$$

Differentiating with respect to $m$ and setting to zero:
$$\frac{d(V \cdot C_{field})}{dm} = c_2 S_b^2 - \frac{c_1 S_w^2}{m^2} = 0 \implies m^2 = \frac{c_1}{c_2} \frac{S_w^2}{S_b^2}$$

Taking the positive square root yields the **Optimal Sub-Sample Size**:
$$m_{opt} = \sqrt{\frac{c_1}{c_2} \cdot \frac{S_w^2}{S_b^2}}$$

Using our relationship with the intracluster correlation $\rho$, where $\frac{S_w^2}{S_b^2} \approx \frac{1 - \rho}{\rho}$:
$$m_{opt} \approx \sqrt{\frac{c_1}{c_2} \cdot \frac{1 - \rho}{\rho}}$$

Once $m_{opt}$ is determined, the optimal number of clusters $n_{opt}$ is determined by the budget constraint:
$$n_{opt} = \frac{C - c_0}{c_1 + m_{opt} c_2}$$

### Practical Interpretation of $m_{opt}$
The mathematical structure of $m_{opt}$ reveals two fundamental design rules:
1. **Cost Ratio Effect ($\sqrt{c_1 / c_2}$)**: If visiting a cluster is very expensive relative to conducting an individual interview ($c_1 \gg c_2$), $m_{opt}$ increases. It pays to take more interviews per cluster to amortize the steep initial travel cost.
2. **Correlation Effect ($\sqrt{(1 - \rho) / \rho}$)**: If the intracluster correlation $\rho$ is high, $m_{opt}$ decreases. Because units within the cluster are highly redundant, sampling many units within the same cluster wastes resources; the budget is better spent visiting more clusters ($n \uparrow$) and taking few interviews per cluster ($m \downarrow$).

---

## Systematic Sampling as a Cluster Sampling Variant

Systematic sampling is one of the most widely applied sampling techniques in survey practice. In systematic sampling, elements are selected at equal numeric intervals from an ordered list.

### Selection Protocol and Notation

Suppose a population of $N$ units is indexed from $1$ to $N$. We wish to draw a sample of $n$ units. Let $k$ be an integer such that:
$$N = n k \implies k = \frac{N}{n}$$
The integer $k$ is called the **sampling interval**. 

The selection protocol proceeds as follows:
1. Draw a single random integer $r$ uniformly from the set $\{1, 2, \dots, k\}$. The value $r$ is the **random start**.
2. The sample consists of the units with indices:
   $$s = \{r, r + k, r + 2k, \dots, r + (n - 1)k\}$$

### Equivalence to Single-Stage Cluster Sampling

Statistically, systematic sampling is mathematically identical to selecting **exactly one cluster** out of $k$ available clusters with equal probability $1/k$.

To see this correspondence, consider arranging the $N$ units of the population in a rectangular matrix of $k$ rows and $n$ columns:

$$\begin{array}{c|ccccc|c}
\text{Cluster (Start)} & \text{Element 1} & \text{Element 2} & \dots & \text{Element } n & \text{Mean} \\
\hline
1 & y_1 & y_{1+k} & \dots & y_{1+(n-1)k} & \bar{y}_{1\cdot} \\
2 & y_2 & y_{2+k} & \dots & y_{2+(n-1)k} & \bar{y}_{2\cdot} \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
r & y_r & y_{r+k} & \dots & y_{r+(n-1)k} & \bar{y}_{r\cdot} \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
k & y_k & y_{2k} & \dots & y_{nk} & \bar{y}_{k\cdot} \\
\hline
\text{Total} & & & & & \bar{\bar{Y}}
\end{array}$$

Each row in this matrix represents a potential systematic sample. There are exactly $k$ possible samples, each containing $n$ elements. Selecting a random start $r \in \{1, \dots, k\}$ is exactly equivalent to selecting one row (one cluster) at random from a population of $k$ clusters, where each cluster contains $n$ elements!

### Variance of the Systematic Sample Mean

Let $\bar{y}_{sys} = \bar{y}_{r\cdot} = \frac{1}{n} \sum_{j=0}^{n-1} y_{r + jk}$ denote the sample mean of the systematic sample.

Because each of the $k$ rows is selected with equal probability $1/k$:
$$E(\bar{y}_{sys}) = \frac{1}{k} \sum_{r=1}^k \bar{y}_{r\cdot} = \bar{\bar{Y}}$$
Thus, the systematic sample mean is strictly design-unbiased.

The variance of $\bar{y}_{sys}$ over all $k$ possible samples is:
$$V(\bar{y}_{sys}) = \frac{1}{k} \sum_{r=1}^k (\bar{y}_{r\cdot} - \bar{\bar{Y}})^2$$

Using our earlier intracluster correlation identity for clusters of size $n$, we can express the variance of $\bar{y}_{sys}$ in terms of the population variance $S^2$ and the intracluster correlation among elements within the same systematic sample, denoted by $\rho_{sys}$:
$$V(\bar{y}_{sys}) = \frac{N - 1}{N} \frac{S^2}{n} \left[ 1 + (n - 1) \rho_{sys} \right]$$
where $\rho_{sys}$ is the correlation between pairs of elements in the same systematic sample:
$$\rho_{sys} = \frac{\sum_{r=1}^k \sum_{j=0}^{n-1} \sum_{l \ne j}^{n-1} (y_{r+jk} - \bar{\bar{Y}})(y_{r+lk} - \bar{\bar{Y}})}{(n - 1)(N - 1) S^2}$$

### Comparison of Systematic Sampling with SRS and Stratified Sampling

The performance of systematic sampling depends critically on how the population list is ordered:
1. **Randomly Ordered Population**: If the frame elements are ordered randomly (e.g., alphabetically by an unrelated name), $\rho_{sys} \approx -\frac{1}{N - 1} \approx 0$. Then $V(\bar{y}_{sys}) \approx V_{srs}(\bar{y})$. Systematic sampling performs identically to SRSWOR, but is operationally simpler to execute.
2. **Monotonic Trend (Linear Trend)**: If the list is ordered monotonically with respect to the survey variable (e.g., sorting farms by acreage or employees by salary), each systematic sample contains elements from the bottom, middle, and top of the distribution. In this case, within-sample heterogeneity is maximized, forcing $\rho_{sys} < 0$. Consequently:
   $$V(\bar{y}_{strat}) \le V(\bar{y}_{sys}) \ll V_{srs}(\bar{y})$$
   Systematic sampling behaves like an implicitly stratified sample with one unit per stratum of size $k$, achieving outstanding precision.
3. **Periodic Variation (The Fatal Trap)**: If the population exhibits cyclical or periodic patterns with a period $P$ that coincides with the sampling interval $k$ (or a multiple thereof), every selected element lands on the exact same phase of the cycle (e.g., always sampling retail sales on Mondays, or selecting corner lots in a grid city). In this catastrophic scenario, elements within the systematic sample are nearly identical, driving $\rho_{sys} \to 1$. The variance explodes, and $\bar{y}_{sys}$ becomes severely inefficient.

---

## Fully worked question 1: Analytical Derivation of Cluster Sampling Variance in Terms of Intraclass Correlation

**Question.** Consider a finite population of $N$ clusters, each containing exactly $M$ observation units, giving a total population size of $M_0 = NM$. A single-stage cluster sample of $n$ clusters is selected using simple random sampling without replacement (SRSWOR), and all $M$ elements within each selected cluster are observed. 

1. Derive from first principles the exact algebraic relationship expressing the between-cluster mean square $S_b^2 = \frac{1}{N - 1} \sum_{i=1}^N (\bar{Y}_i - \bar{\bar{Y}})^2$ in terms of the total finite-population variance $S^2 = \frac{1}{NM - 1} \sum_{i=1}^N \sum_{j=1}^M (y_{ij} - \bar{\bar{Y}})^2$ and the intracluster correlation coefficient $\rho$.
2. Prove that the variance of the cluster sample mean $\bar{y}_{cl} = \frac{1}{nM} \sum_{i \in s} \sum_{j=1}^M y_{ij}$ satisfies:
   $$V(\bar{y}_{cl}) = \frac{1 - f}{n M} S^2 \left( \frac{NM - 1}{M(N - 1)} \right) \left[ 1 + (M - 1)\rho \right]$$
   where $f = n / N$.
3. Given a population with $N = 500$ villages, each containing $M = 40$ households ($NM = 20,000$ households), total population variance $S^2 = 1,600$, and intracluster correlation $\rho = 0.08$. Compute the exact sampling variance $V(\bar{y}_{cl})$ for a sample of $n = 25$ villages, and evaluate the exact Design Effect relative to an SRSWOR of $1,000$ individual households.

**Solution, step 1: Deriving the relation between $S_b^2$, $S^2$, and $\rho$.**
We begin with the formal definition of the intracluster correlation coefficient $\rho$:
$$\rho = \frac{\sum_{i=1}^N \sum_{j=1}^M \sum_{k \ne j}^M (y_{ij} - \bar{\bar{Y}})(y_{ik} - \bar{\bar{Y}})}{(M - 1) \sum_{i=1}^N \sum_{j=1}^M (y_{ij} - \bar{\bar{Y}})^2}$$

Recall that the denominator contains the total sum of squares:
$$\sum_{i=1}^N \sum_{j=1}^M (y_{ij} - \bar{\bar{Y}})^2 = (NM - 1) S^2$$

Now expand the squared cluster deviation for cluster $i$:
$$\left[ \sum_{j=1}^M (y_{ij} - \bar{\bar{Y}}) \right]^2 = \sum_{j=1}^M (y_{ij} - \bar{\bar{Y}})^2 + \sum_{j=1}^M \sum_{k \ne j}^M (y_{ij} - \bar{\bar{Y}})(y_{ik} - \bar{\bar{Y}})$$

Since $\sum_{j=1}^M (y_{ij} - \bar{\bar{Y}}) = M (\bar{Y}_i - \bar{\bar{Y}})$, the left-hand side is $M^2 (\bar{Y}_i - \bar{\bar{Y}})^2$. Summing across all $N$ clusters:
$$\sum_{i=1}^N M^2 (\bar{Y}_i - \bar{\bar{Y}})^2 = \sum_{i=1}^N \sum_{j=1}^M (y_{ij} - \bar{\bar{Y}})^2 + \sum_{i=1}^N \sum_{j=1}^M \sum_{k \ne j}^M (y_{ij} - \bar{\bar{Y}})(y_{ik} - \bar{\bar{Y}})$$

Recognizing the between-cluster sum of squares $\sum_{i=1}^N (\bar{Y}_i - \bar{\bar{Y}})^2 = (N - 1) S_b^2$:
$$M^2 (N - 1) S_b^2 = (NM - 1) S^2 + \sum_{i=1}^N \sum_{j=1}^M \sum_{k \ne j}^M (y_{ij} - \bar{\bar{Y}})(y_{ik} - \bar{\bar{Y}})$$

From the definition of $\rho$, the double cross-product sum is:
$$\sum_{i=1}^N \sum_{j=1}^M \sum_{k \ne j}^M (y_{ij} - \bar{\bar{Y}})(y_{ik} - \bar{\bar{Y}}) = \rho (M - 1) (NM - 1) S^2$$

Substitute this back into the equation:
$$M^2 (N - 1) S_b^2 = (NM - 1) S^2 + \rho (M - 1) (NM - 1) S^2$$
$$M^2 (N - 1) S_b^2 = (NM - 1) S^2 \left[ 1 + (M - 1)\rho \right]$$

Dividing both sides by $M^2 (N - 1)$:
$$S_b^2 = \frac{NM - 1}{M^2 (N - 1)} S^2 \left[ 1 + (M - 1)\rho \right] = \frac{1}{M} \left( \frac{NM - 1}{M(N - 1)} \right) S^2 \left[ 1 + (M - 1)\rho \right]$$
This establishes the exact algebraic relationship without any asymptotic approximations.

**Solution, step 2: Deriving the variance of the cluster sample mean.**
The cluster sample mean is $\bar{y}_{cl} = \frac{1}{n} \sum_{i \in s} \bar{Y}_i$. Because $n$ clusters are chosen by SRSWOR from $N$ clusters, the sampling variance is:
$$V(\bar{y}_{cl}) = \frac{1 - f}{n} S_b^2$$
where $f = n / N$.

Substituting our exact expression for $S_b^2$ from Step 1:
$$V(\bar{y}_{cl}) = \frac{1 - f}{n} \cdot \frac{NM - 1}{M^2 (N - 1)} S^2 \left[ 1 + (M - 1)\rho \right]$$
$$V(\bar{y}_{cl}) = \frac{1 - f}{n M} S^2 \left( \frac{NM - 1}{M(N - 1)} \right) \left[ 1 + (M - 1)\rho \right]$$
This completes the analytical proof.

**Solution, step 3: Numerical calculation and Design Effect evaluation.**
We are given:
- $N = 500$, $M = 40$, $NM = 20,000$
- $n = 25$ villages, so total elements observed $m_{tot} = n M = 25 \times 40 = 1,000$
- First-stage sampling fraction: $f = \frac{n}{N} = \frac{25}{500} = 0.05$
- Population variance: $S^2 = 1,600$
- Intraclass correlation: $\rho = 0.08$

First, compute the finite-population correction adjustment factor:
$$\frac{NM - 1}{M(N - 1)} = \frac{20,000 - 1}{40(500 - 1)} = \frac{19,999}{40 \times 499} = \frac{19,999}{19,960} \approx 1.0019539$$

Next, evaluate the intracluster inflation term:
$$1 + (M - 1)\rho = 1 + (40 - 1)(0.08) = 1 + 39 \times 0.08 = 1 + 3.12 = 4.12$$

Now calculate the between-cluster mean square $S_b^2$:
$$S_b^2 = \frac{19,999}{40 \times 19,960} \times \frac{1,600}{40} \times 4.12 = 1.0019539 \times 40 \times 4.12 = 165.12199$$

Now compute the exact sampling variance of the cluster sample mean:
$$V(\bar{y}_{cl}) = \frac{1 - f}{n} S_b^2 = \frac{1 - 0.05}{25} \times 165.12199 = \frac{0.95}{25} \times 165.12199 = 0.038 \times 165.12199 = 6.274636$$
The standard error is:
$$\text{SE}(\bar{y}_{cl}) = \sqrt{6.274636} \approx 2.5049$$

Next, compute the variance under simple random sampling without replacement of $m_{tot} = 1,000$ elements:
The overall sampling fraction for elements is $f_{elem} = \frac{1,000}{20,000} = 0.05$.
$$V_{srs}(\bar{y}) = \frac{1 - f_{elem}}{m_{tot}} S^2 = \frac{1 - 0.05}{1,000} \times 1,600 = \frac{0.95}{1,000} \times 1,600 = 0.00095 \times 1,600 = 1.5200$$
The standard error under SRS is:
$$\text{SE}_{srs}(\bar{y}) = \sqrt{1.5200} \approx 1.2329$$

Finally, evaluate the exact Design Effect ($\text{Deff}$):
$$\text{Deff} = \frac{V(\bar{y}_{cl})}{V_{srs}(\bar{y})} = \frac{6.274636}{1.5200} \approx 4.12805$$
Notice that:
$$\text{Deff} = \left( \frac{NM - 1}{M(N - 1)} \right) \left[ 1 + (M - 1)\rho \right] = 1.0019539 \times 4.12 = 4.12805$$
This confirms that the design effect is almost perfectly captured by $1 + (M - 1)\rho = 4.12$. 

The effective sample size is:
$$n_{eff} = \frac{1,000}{\text{Deff}} = \frac{1,000}{4.12805} \approx 242.2$$
Even though $1,000$ households were surveyed across the 25 villages, the cluster design delivers the precision of only 242 independently sampled households.

---

## Fully worked question 2: Computing Design Effect, Variance Inflation and Effective Sample Size Under Severe Within-Cluster Homogeneity

**Question.** A nationwide public health assessment is designed to estimate the prevalence of iron-deficiency anemia among primary school children. The target population consists of $N = 1,200$ primary schools in a geographic division, with each school enrolling an average of $M = 50$ children in the target age bracket ($NM = 60,000$ children). 

An epidemiological pilot study reveals that anemia prevalence is heavily driven by localized environmental factors (soil quality, community water source, and school lunch menus), yielding an intracluster correlation of $\rho = 0.15$. The true population prevalence is hypothesized to be $P = 0.20$ (so the unit variance is $S^2 \approx P(1-P) = 0.16$).

1. If the agency conducts a single-stage cluster sample selecting $n = 30$ schools (total sample size $n M = 1,500$ students), compute:
   - The design effect ($\text{Deff}$).
   - The effective sample size ($n_{eff}$).
   - The exact standard error of the estimated proportion $\hat{p}_{cl}$.
   - The 95% confidence interval half-width (margin of error).
2. If the health authority demands that the margin of error must not exceed $\pm 0.025$ at the 95% confidence level ($z_{0.025} = 1.96$), determine the minimum number of schools $n$ that must be sampled under this single-stage design.
3. Compare the required sample size in schools and total students if the agency redesigns the survey as a two-stage cluster design selecting $m = 10$ students per school instead of enumerating all $M = 50$ students.

**Solution, step 1: Evaluating the single-stage design with $n = 30$ schools.**
Given:
- $N = 1,200$, $M = 50$, total population $NM = 60,000$
- $n = 30$ schools, so $m_{tot} = 30 \times 50 = 1,500$ students
- $\rho = 0.15$, $P = 0.20$, $S^2 \approx 0.20 \times 0.80 = 0.16$

1. **Design Effect ($\text{Deff}$)**:
   $$\text{Deff} = 1 + (M - 1)\rho = 1 + (50 - 1)(0.15) = 1 + 49 \times 0.15 = 1 + 7.35 = 8.35$$
   The sampling variance is inflated by a massive factor of 8.35 due to the high intracluster correlation ($\rho = 0.15$) and moderate cluster size ($M = 50$).

2. **Effective Sample Size ($n_{eff}$)**:
   $$n_{eff} = \frac{n M}{\text{Deff}} = \frac{1,500}{8.35} \approx 179.64 \approx 180 \text{ students}$$
   Enumerating 1,500 students in 30 schools provides the statistical precision of only 180 independent, unclustered student observations.

3. **Standard Error ($\text{SE}(\hat{p}_{cl})$)**:
   First, evaluate the first-stage sampling fraction:
   $$f = \frac{n}{N} = \frac{30}{1,200} = 0.025$$
   The variance under SRS of $1,500$ students is:
   $$V_{srs} = \frac{1 - f}{1,500} S^2 = \frac{1 - 0.025}{1,500} \times 0.16 = \frac{0.975}{1,500} \times 0.16 = 0.00065 \times 0.16 = 0.000104$$
   The variance under cluster sampling is:
   $$V(\hat{p}_{cl}) = \text{Deff} \times V_{srs} = 8.35 \times 0.000104 = 0.0008684$$
   The standard error is:
   $$\text{SE}(\hat{p}_{cl}) = \sqrt{0.0008684} \approx 0.029469 \approx 0.0295$$

4. **Margin of Error ($E$)**:
   At the 95% confidence level ($z = 1.96$):
   $$E = 1.96 \times \text{SE}(\hat{p}_{cl}) = 1.96 \times 0.029469 \approx 0.05776 \approx \pm 5.78\%$$
   The single-stage cluster sample of 30 schools yields a margin of error of $\pm 5.78\%$, which fails the health authority's precision requirement of $\pm 2.5\%$.

**Solution, step 2: Determining the required number of schools for $E \le 0.025$.**
We require:
$$E = z \cdot \text{SE}(\hat{p}_{cl}) \le 0.025 \implies \text{SE}(\hat{p}_{cl}) \le \frac{0.025}{1.96} \approx 0.012755$$
Squaring both sides gives the target variance:
$$V_{target} = (0.012755)^2 \approx 0.00016269$$

Recall the variance formula for single-stage cluster sampling:
$$V(\hat{p}_{cl}) = \frac{1 - n/N}{n M} S^2 \left[ 1 + (M - 1)\rho \right]$$
Let $A = \frac{S^2 [1 + (M - 1)\rho]}{M} = \frac{0.16 \times 8.35}{50} = \frac{1.336}{50} = 0.02672$.
Then:
$$V = \left( \frac{1}{n} - \frac{1}{N} \right) A \le V_{target}$$
$$\frac{1}{n} - \frac{1}{1,200} \le \frac{0.00016269}{0.02672} = 0.0060887$$
$$\frac{1}{n} \le 0.0060887 + \frac{1}{1,200} = 0.0060887 + 0.0008333 = 0.0069220$$
$$n \ge \frac{1}{0.0069220} \approx 144.47$$

Rounding up to the next integer:
$$n_{req} = 145 \text{ schools}$$
Under single-stage cluster sampling, the authority must sample $145$ schools and test all $M = 50$ students in each, requiring a total of:
$$m_{tot} = 145 \times 50 = 7,250 \text{ students}$$

**Solution, step 3: Redesigning as a two-stage cluster design with $m = 10$.**
Now suppose the agency adopts a two-stage design, sampling $n$ schools at Stage 1, but sampling only $m = 10$ students per school at Stage 2.

1. **New Design Effect for $m = 10$**:
   $$\text{Deff}_2 = 1 + (m - 1)\rho = 1 + (10 - 1)(0.15) = 1 + 9 \times 0.15 = 1 + 1.35 = 2.35$$
   Notice that reducing the sub-sample size from 50 to 10 slashes the design effect from $8.35$ down to $2.35$!

2. **Determining required $n$ under Two-Stage Sampling**:
   In two-stage sampling, ignoring the negligible second-stage finite population correction ($1 - m/M = 1 - 10/50 = 0.80$):
   $$V(\hat{p}_{2stage}) \approx \frac{1 - n/N}{n m} S^2 \left[ 1 + (m - 1)\rho \right]$$
   Let $B = \frac{S^2 [1 + (m - 1)\rho]}{m} = \frac{0.16 \times 2.35}{10} = \frac{0.376}{10} = 0.0376$.
   We require:
   $$\left( \frac{1}{n} - \frac{1}{N} \right) B \le V_{target} = 0.00016269$$
   $$\frac{1}{n} - \frac{1}{1,200} \le \frac{0.00016269}{0.0376} = 0.0043269$$
   $$\frac{1}{n} \le 0.0043269 + 0.0008333 = 0.0051602$$
   $$n \ge \frac{1}{0.0051602} \approx 193.79 \implies n = 194 \text{ schools}$$

3. **Comparison of Total Sample Burden**:
   - **Single-Stage ($M = 50$)**: $n = 145$ schools, $m_{tot} = 145 \times 50 = 7,250$ students.
   - **Two-Stage ($m = 10$)**: $n = 194$ schools, $m_{tot} = 194 \times 10 = 1,940$ students.

While the two-stage design requires visiting 49 more schools ($194$ vs $145$), it reduces the number of blood tests and laboratory assays from $7,250$ to $1,940$—a massive $73.2\%$ reduction in biological sample processing costs, while achieving the exact same margin of error ($\pm 2.5\%$).

---

## Fully worked question 3: Two-Stage Cluster Sampling Variance Estimation and Optimal Allocation Under a Linear Cost Model

**Question.** An agricultural research institute is designing an objective crop yield estimation survey across an agricultural province. The province contains $N = 800$ agricultural wards (PSUs), with each ward containing an average of $M = 120$ wheat farms (SSUs), giving a population of $NM = 96,000$ farms.

A comprehensive pilot survey of wheat yields (measured in metric tons per hectare) provides the following variance components:
- Between-ward variance: $S_b^2 = 0.450 \text{ (ton/ha)}^2$
- Within-ward variance: $S_w^2 = 1.350 \text{ (ton/ha)}^2$

The logistical cost model for field operations is estimated as:
- Fixed overhead: $c_0 = 15,000$ dollars
- Cost per sampled ward: $c_1 = 480$ dollars (field team travel, GPS perimeter boundary verification, farmer roster verification)
- Cost per sampled farm: $c_2 = 30$ dollars (crop-cutting quadrant measurement, grain threshing, moisture meter assay)
- Total operational budget available: $C = 75,000$ dollars (so net field budget is $C_{field} = 75,000 - 15,000 = 60,000$ dollars)

1. Determine the optimal number of farms to sample per ward ($m_{opt}$) and the optimal number of wards to sample ($n_{opt}$) to minimize the variance of the estimated mean yield $\bar{\bar{y}}$.
2. Calculate the resulting sampling variance $V(\bar{\bar{y}})$, standard error $\text{SE}(\bar{\bar{y}})$, and the 95% confidence interval half-width.
3. In the actual execution of the survey using the optimal allocation, sample data collected from the $n_{opt}$ wards yield sample mean squares $s_1^2 = 0.585$ and $s_2^2 = 1.320$. Compute the strictly unbiased estimate of the sampling variance $\hat{V}(\bar{\bar{y}})$ and verify the validity of the Ultimate Cluster approximation.

**Solution, step 1: Determining optimal allocation $(m_{opt}, n_{opt})$.**
We are given:
- $N = 800$, $M = 120$
- $S_b^2 = 0.450$, $S_w^2 = 1.350$
- $c_1 = 480$, $c_2 = 30$, $C_{field} = 60,000$

Using the optimal sub-sample size formula derived from the Cauchy–Schwarz inequality:
$$m_{opt} = \sqrt{\frac{c_1}{c_2} \cdot \frac{S_w^2}{S_b^2}}$$

Substitute the known parameters:
$$\frac{c_1}{c_2} = \frac{480}{30} = 16$$
$$\frac{S_w^2}{S_b^2} = \frac{1.350}{0.450} = 3.0$$

Therefore:
$$m_{opt} = \sqrt{16 \times 3.0} = \sqrt{48} \approx 6.9282$$

Rounding to the nearest integer:
$$m_{opt} = 7 \text{ farms per ward}$$

Now determine the number of wards $n_{opt}$ that can be sampled within the net field budget $C_{field} = 60,000$ dollars:
The cost per sampled ward including its 7 farm interviews is:
$$c_{ward} = c_1 + m_{opt} c_2 = 480 + 7 \times 30 = 480 + 210 = 690 \text{ dollars}$$

The maximum number of wards is:
$$n_{opt} = \left\lfloor \frac{C_{field}}{c_{ward}} \right\rfloor = \left\lfloor \frac{60,000}{690} \right\rfloor = \lfloor 86.9565 \rfloor = 86 \text{ wards}$$

Let us verify the budget expenditure with $n = 86$ and $m = 7$:
$$C_{exp} = 86 \times 690 = 59,340 \le 60,000 \text{ dollars}$$
The remaining unspent $660$ dollars can be held as operational contingency. Total farms sampled across the province:
$$m_{tot} = n \times m = 86 \times 7 = 602 \text{ farms}$$

**Solution, step 2: Calculating theoretical sampling variance and standard error.**
The exact two-stage sampling variance formula is:
$$V(\bar{\bar{y}}) = \frac{1 - f_1}{n} S_b^2 + \frac{1 - f_2}{n m} S_w^2$$
where:
- $f_1 = \frac{n}{N} = \frac{86}{800} = 0.1075$
- $f_2 = \frac{m}{M} = \frac{7}{120} \approx 0.058333$

Compute the two components:
1. **First-Stage Component**:
   $$V_1 = \frac{1 - f_1}{n} S_b^2 = \frac{1 - 0.1075}{86} \times 0.450 = \frac{0.8925}{86} \times 0.450 = 0.0103779 \times 0.450 \approx 0.0046701$$

2. **Second-Stage Component**:
   $$V_2 = \frac{1 - f_2}{n m} S_w^2 = \frac{1 - 0.058333}{602} \times 1.350 = \frac{0.941667}{602} \times 1.350 = 0.0015642 \times 1.350 \approx 0.0021117$$

3. **Total Variance**:
   $$V(\bar{\bar{y}}) = V_1 + V_2 = 0.0046701 + 0.0021117 = 0.0067818 \text{ (ton/ha)}^2$$

The standard error is:
$$\text{SE}(\bar{\bar{y}}) = \sqrt{0.0067818} \approx 0.08235 \text{ ton/ha}$$

At the 95% confidence level ($z = 1.96$):
$$E = 1.96 \times 0.08235 \approx \pm 0.1614 \text{ ton/ha}$$
The survey design guarantees that the provincial average wheat yield will be estimated within $\pm 0.161$ tons per hectare of the true population value.

**Solution, step 3: Sample variance estimation and Ultimate Cluster verification.**
In the empirical execution, we observe:
- $n = 86$, $m = 7$
- $f_1 = 0.1075$, $f_2 = 0.058333$
- $s_1^2 = 0.585$
- $s_2^2 = 1.320$

1. **Strictly Unbiased Sample Variance Estimator**:
   The exact unbiased estimator is:
   $$\hat{V}(\bar{\bar{y}}) = \frac{1 - f_1}{n} s_1^2 + \frac{f_1(1 - f_2)}{n m} s_2^2$$

   Compute each term:
   - Term 1: $\frac{1 - 0.1075}{86} \times 0.585 = \frac{0.8925}{86} \times 0.585 = 0.0103779 \times 0.585 \approx 0.0060711$
   - Term 2: $\frac{0.1075 \times (1 - 0.058333)}{86 \times 7} \times 1.320 = \frac{0.1075 \times 0.941667}{602} \times 1.320 = \frac{0.101229}{602} \times 1.320 = 0.00016815 \times 1.320 \approx 0.0002220$

   Summing both terms:
   $$\hat{V}(\bar{\bar{y}}) = 0.0060711 + 0.0002220 = 0.0062931 \text{ (ton/ha)}^2$$
   The estimated standard error is:
   $$\hat{\text{SE}}(\bar{\bar{y}}) = \sqrt{0.0062931} \approx 0.07933 \text{ ton/ha}$$

2. **Ultimate Cluster Approximation**:
   Under the Ultimate Cluster principle, we approximate the variance simply by treating the sample as an unistage sample of clusters:
   $$\hat{V}_{ult}(\bar{\bar{y}}) = \frac{1 - f_1}{n} s_1^2 = \frac{1 - 0.1075}{86} \times 0.585 \approx 0.0060711$$
   Comparing with the exact estimator:
   $$\frac{\hat{V}_{ult}}{\hat{V}_{exact}} = \frac{0.0060711}{0.0062931} \approx 0.9647$$
   The Ultimate Cluster estimator accounts for $96.5\%$ of the total variance, confirming its outstanding utility even with a moderate first-stage sampling fraction of $f_1 = 10.75\%$. If $f_1$ were below $5\%$, the agreement would exceed $99\%$.

---

---

## Multistage Sampling with Unequal Cluster Sizes: Foundations and Variance Decomposition

In Section 4.4, we derived the two-stage cluster sampling variance under the assumption that all $N$ primary clusters contained an identical number of observation units $M$, and that an equal number of elements $m$ was sampled from each selected cluster. In real-world demographic, agricultural, and socioeconomic surveys, clusters are natural administrative or geographical entities—villages, urban wards, schools, census enumeration areas—whose population sizes $M_i$ vary by orders of magnitude. 

When cluster sizes $M_i$ vary, the statistical design must formalize both the first-stage selection of primary sampling units (PSUs) and the second-stage selection of secondary sampling units (SSUs) to maintain strict design consistency and avoid uncontrolled variance inflation.

### The General Two-Stage Horvitz–Thompson Estimator

Consider a finite population $U$ partitioned into $N$ primary sampling units $U_1, U_2, \dots, U_N$. PSU $i$ contains $M_i$ elements. The total number of elements in the entire finite population is:
$$M_0 = \sum_{i=1}^N M_i$$
Let $y_{ij}$ denote the survey measurement for element $j \in U_i$ ($j = 1, 2, \dots, M_i$).
The total for PSU $i$ is $Y_i = \sum_{j=1}^{M_i} y_{ij}$, and the overall population total is $Y = \sum_{i=1}^N Y_i$.

The two-stage sampling protocol executes as follows:
- **Stage 1**: Select a sample $s_1$ of $n$ PSUs from $\{1, 2, \dots, N\}$ according to a probability design without replacement characterized by first-order inclusion probabilities $\pi_i$ and second-order joint inclusion probabilities $\pi_{ik}$ ($i, k = 1, \dots, N$).
- **Stage 2**: Within each selected PSU $i \in s_1$, select an SRSWOR sample $s_{2i}$ of $m_i$ elements from the $M_i$ available units, with conditional inclusion probabilities $\pi_{j|i} = m_i / M_i$.

For each selected PSU $i \in s_1$, the design-unbiased estimator of the PSU total $Y_i$ is:
$$\hat{Y}_i = \frac{M_i}{m_i} \sum_{j \in s_{2i}} y_{ij} = M_i \bar{y}_i$$
where $\bar{y}_i = \frac{1}{m_i} \sum_{j \in s_{2i}} y_{ij}$ is the sample mean of the elements observed in PSU $i$.

The **Two-Stage Horvitz–Thompson Estimator** of the overall population total $Y$ is:
$$\hat{Y}_{2HT} = \sum_{i \in s_1} \frac{\hat{Y}_i}{\pi_i} = \sum_{i \in s_1} \frac{M_i \bar{y}_i}{\pi_i}$$

To estimate the overall population mean per element $\bar{\bar{Y}} = Y / M_0$:
$$\hat{\bar{Y}}_{2HT} = \frac{\hat{Y}_{2HT}}{M_0} = \frac{1}{M_0} \sum_{i \in s_1} \frac{M_i \bar{y}_i}{\pi_i}$$

### Proof of Strict Design Unbiasedness

Using the Law of Iterated Expectation:
$$E(\hat{Y}_{2HT}) = E_1\left[ E_2(\hat{Y}_{2HT} \mid s_1) \right]$$

Conditioning on the selected primary units $s_1$:
$$E_2(\hat{Y}_{2HT} \mid s_1) = \sum_{i \in s_1} \frac{1}{\pi_i} E_2(\hat{Y}_i \mid s_1) = \sum_{i \in s_1} \frac{1}{\pi_i} Y_i$$
Taking the first-stage expectation over all possible selections of $s_1$:
$$E_1\left[ \sum_{i \in s_1} \frac{Y_i}{\pi_i} \right] = \sum_{i=1}^N \pi_i \frac{Y_i}{\pi_i} = \sum_{i=1}^N Y_i = Y$$
This proves that the two-stage Horvitz–Thompson estimator is strictly design-unbiased for any cluster sizes $M_i$ and any sub-sample sizes $m_i$.

### Exact Variance Decomposition for Unequal Cluster Sizes

Applying the Law of Total Variance:
$$V(\hat{Y}_{2HT}) = V_1\left( E_2(\hat{Y}_{2HT} \mid s_1) \right) + E_1\left( V_2(\hat{Y}_{2HT} \mid s_1) \right)$$

1. **First-Stage Variance Component ($V_1$)**:
   Since $E_2(\hat{Y}_{2HT} \mid s_1) = \sum_{i \in s_1} \frac{Y_i}{\pi_i}$, this is simply the Horvitz–Thompson estimator of the total of the population of cluster totals $\{Y_1, \dots, Y_N\}$.
   Under the Sen–Yates–Grundy formulation (for fixed $n$):
   $$V_1 = \sum_{i=1}^N \sum_{k > i}^N (\pi_i \pi_k - \pi_{ik}) \left( \frac{Y_i}{\pi_i} - \frac{Y_k}{\pi_k} \right)^2$$

2. **Second-Stage Variance Component ($E_1 V_2$)**:
   Conditional on $s_1$, sub-sampling across different PSUs is completely independent:
   $$V_2(\hat{Y}_{2HT} \mid s_1) = \sum_{i \in s_1} \frac{1}{\pi_i^2} V_2(\hat{Y}_i \mid s_1)$$
   Within PSU $i$, an SRSWOR of $m_i$ elements is drawn from $M_i$ elements. The variance of the estimated total $\hat{Y}_i = M_i \bar{y}_i$ is:
   $$V_2(\hat{Y}_i \mid s_1) = M_i^2 \left( \frac{1 - f_{2i}}{m_i} \right) S_i^2$$
   where $f_{2i} = m_i / M_i$ and $S_i^2 = \frac{1}{M_i - 1} \sum_{j=1}^{M_i} (y_{ij} - \bar{Y}_i)^2$.
   Substituting this into the sum:
   $$V_2(\hat{Y}_{2HT} \mid s_1) = \sum_{i \in s_1} \frac{M_i^2}{\pi_i^2} \left( \frac{1 - f_{2i}}{m_i} \right) S_i^2$$

   Taking the first-stage expectation $E_1$:
   $$E_1\left( V_2 \right) = \sum_{i=1}^N \pi_i \left[ \frac{M_i^2}{\pi_i^2} \left( \frac{1 - f_{2i}}{m_i} \right) S_i^2 \right] = \sum_{i=1}^N \frac{M_i^2}{\pi_i} \left( \frac{1 - f_{2i}}{m_i} \right) S_i^2$$

Combining both components yields the general **Two-Stage Variance Formula for Unequal Clusters**:
$$V(\hat{Y}_{2HT}) = \sum_{i=1}^N \sum_{k > i}^N (\pi_i \pi_k - \pi_{ik}) \left( \frac{Y_i}{\pi_i} - \frac{Y_k}{\pi_k} \right)^2 + \sum_{i=1}^N \frac{M_i^2}{\pi_i} \left( \frac{1 - f_{2i}}{m_i} \right) S_i^2$$

### Unbiased Sample Variance Estimation

To estimate $V(\hat{Y}_{2HT})$ from empirical sample data, we apply the Sen–Yates–Grundy estimator to the first stage, substituting the estimated cluster totals $\hat{Y}_i$ for the true totals $Y_i$, and subtracting the second-stage noise that inflates the between-cluster mean square.

The strictly unbiased sample variance estimator is:
$$\hat{V}(\hat{Y}_{2HT}) = \sum_{i \in s_1} \sum_{k \in s_1, k > i} \left( \frac{\pi_i \pi_k - \pi_{ik}}{\pi_{ik}} \right) \left( \frac{\hat{Y}_i}{\pi_i} - \frac{\hat{Y}_k}{\pi_k} \right)^2 + \sum_{i \in s_1} \frac{M_i^2}{\pi_i} \left( \frac{1 - f_{2i}}{m_i} \right) s_i^2$$
where $s_i^2 = \frac{1}{m_i - 1} \sum_{j \in s_{2i}} (y_{ij} - \bar{y}_i)^2$ is the sample variance of the elements observed in PSU $i$.

When the first-stage sampling fraction is small ($\pi_i \ll 1$), the first term dominates, and the Ultimate Cluster estimator provides an extraordinarily accurate, simple approximation.

---

## Non-Linear Field Cost Functions and Spatial Travel Optimization

In our initial investigation of optimal sample allocation (Section 4.5), survey operational costs were characterized by a linear model: $C = c_0 + n c_1 + n m c_2$. Under this simple model, the marginal cost of visiting a PSU ($c_1$) was assumed to be independent of the number of PSUs selected ($n$).

In actual field operations across large geographic expanses (such as provinces, agricultural river basins, or forestry tracts), the linear travel cost assumption fails. When field interview teams travel between sampled PSUs, the distance traveled between clusters depends directly on how densely or sparsely the $n$ clusters are scattered across the geographic territory.

### The Beardwood–Halton–Hammersley Spatial Travel Law

In mathematical spatial optimization, the Traveling Salesman Problem (TSP) addresses the shortest closed tour connecting $n$ points distributed across a two-dimensional geographic region of surface area $A$.

A landmark theorem in stochastic geometry proved by J. Beardwood, J. H. Halton, and J. M. Hammersley (1959) establishes that if $n$ points are distributed uniformly at random across a bounded region of area $A$, the minimum travel distance $D_n$ required to visit all $n$ locations satisfies:
$$\lim_{n \to \infty} \frac{D_n}{\sqrt{n A}} = \beta_{TSP} \approx 0.712 \quad \text{almost surely}$$
where $\beta_{TSP}$ is the universal Traveling Salesman constant for Euclidean two-dimensional space.

Consequently, the total mileage or travel distance between clusters does **not** grow linearly with $n$, but scales proportionally to the square root of the number of clusters:
$$D_{travel} \propto \sqrt{n A}$$

### The Non-Linear Spatial Survey Cost Model

Incorporating the Beardwood–Halton–Hammersley spatial law into survey operations yields the **Non-Linear Spatial Cost Function** (Hansen, Hurwitz, and Madow, 1953; Groves, 1989):
$$C = c_0 + c_t \sqrt{n A} + n c_1 + n m c_2$$
where:
- $c_0$ is fixed administrative overhead.
- $c_t$ is the travel cost per unit distance (fuel expenditures, vehicle maintenance, travel time wages).
- $A$ is the total geographical area of the survey universe (in square kilometers).
- $c_1$ is the local fixed cost per PSU (locating boundary monuments, meeting local community leaders, establishing field headquarters).
- $c_2$ is the marginal interview cost per secondary unit (household interview time, respondent incentives).

The term $c_t \sqrt{n A}$ represents the **inter-cluster travel cost**, while $n c_1 + n m c_2$ represents the **intra-cluster operational cost**.

### Optimal Allocation under Spatial Travel Constraints

To minimize the two-stage sampling variance $V \approx \frac{S_b^2}{n} + \frac{S_w^2}{n m}$ subject to the non-linear spatial budget constraint:
$$C_{field} = c_t \sqrt{n A} + n (c_1 + m c_2)$$

We set up the Lagrangian:
$$\mathcal{L}(n, m, \lambda) = \left( \frac{S_b^2}{n} + \frac{S_w^2}{n m} \right) + \lambda \left[ c_t \sqrt{n A} + n (c_1 + m c_2) - C_{field} \right]$$

Differentiating with respect to $m$ and $n$:
1. With respect to $m$:
   $$\frac{\partial \mathcal{L}}{\partial m} = -\frac{S_w^2}{n m^2} + \lambda n c_2 = 0 \implies \lambda = \frac{S_w^2}{n^2 m^2 c_2}$$

2. With respect to $n$:
   $$\frac{\partial \mathcal{L}}{\partial n} = -\frac{1}{n^2} \left( S_b^2 + \frac{S_w^2}{m} \right) + \lambda \left[ \frac{c_t \sqrt{A}}{2 \sqrt{n}} + (c_1 + m c_2) \right] = 0$$

Equating the expressions for $\lambda$ and solving for $m$:
$$m^2 = \frac{S_w^2}{S_b^2} \left[ \frac{c_1 + \frac{c_t \sqrt{A}}{2 \sqrt{n}}}{c_2} \right]$$

Taking the positive square root yields the **Spatially Adjusted Optimal Sub-Sample Size**:
$$m_{opt}(n) = \sqrt{\frac{S_w^2}{S_b^2} \left[ \frac{c_1 + \frac{c_t \sqrt{A}}{2 \sqrt{n}}}{c_2} \right]}$$

#### Methodological Insights from the Spatial Formulation:
1. **Density Dampening**: The effective cost per PSU is inflated by the spatial travel term $\frac{c_t \sqrt{A}}{2 \sqrt{n}}$. In vast, sparsely populated geographic regions (large area $A$), traveling between clusters is the dominant operational hurdle. This inflates the effective cost per PSU, forcing $m_{opt}$ upward: interview teams must conduct more interviews per cluster ($m \uparrow$) to amortize the grueling travel required to reach each isolated site.
2. **Urban Compactness**: In compact urban environments (small area $A$), inter-cluster travel is rapid and inexpensive ($c_t \sqrt{A} \to 0$). The optimal design shifts toward sampling many compact clusters with very few interviews per cluster ($n \uparrow, m \downarrow$), which minimizes variance inflation by suppressing the intracluster correlation penalty $1 + (m - 1)\rho$.

---

## Variance Estimation under Systematic Cluster Sampling: Wolter's Formulations

In Section 4.6, we proved that systematic sampling is formally identical to selecting a single cluster of size $n$ from $k$ systematic clusters. Because only one systematic cluster is observed, the classical textbook states that an unbiased estimator of variance does not exist without making strong modeling assumptions.

In modern survey practice, however, national statistical agencies frequently deploy **Systematic Selection of Clusters** (e.g., selecting census enumeration areas systematically along a geographical serpentining path). To provide rigorous, robust standard errors for systematic designs, Kirk Wolter (2007) formalized two primary replication frameworks:

### 1. The Successive Difference Replication Estimator

When clusters are ordered geographically or monotonically prior to systematic selection, adjacent clusters in the sample list are physically proximate and share similar environmental and demographic characteristics. 

Let $\bar{y}_1, \bar{y}_2, \dots, \bar{y}_n$ denote the sequence of sample cluster means arranged in the exact order of their systematic selection.
The **Successive Difference Variance Estimator** is defined as:
$$\hat{V}_{diff}(\bar{y}_{cl}) = \frac{1 - f}{2 n (n - 1)} \sum_{k=1}^{n-1} (\bar{y}_{k+1} - \bar{y}_k)^2$$

#### Proof of Trend Elimination:
Suppose the population values contain a deterministic linear trend across the ordered frame: $\bar{Y}_k = \alpha + \beta k$.
The standard sample variance $s_b^2 = \frac{1}{n - 1} \sum (\bar{y}_k - \bar{y})^2$ is heavily inflated by the trend, since $\sum (\bar{Y}_k - \bar{Y})^2 \approx \frac{\beta^2 n^3}{12}$.
Now evaluate the first differences:
$$\bar{y}_{k+1} - \bar{y}_k = [\alpha + \beta(k + 1) + \varepsilon_{k+1}] - [\alpha + \beta k + \varepsilon_k] = \beta + (\varepsilon_{k+1} - \varepsilon_k)$$
The linear trend is completely transformed into a constant intercept $\beta$, which is subtracted out in higher-order differences!
The **Second-Order Successive Difference Estimator** removes quadratic curvature:
$$\hat{V}_{diff2}(\bar{y}_{cl}) = \frac{1 - f}{6 n (n - 2)} \sum_{k=1}^{n-2} (\bar{y}_{k+2} - 2 \bar{y}_{k+1} + \bar{y}_k)^2$$
Successive difference estimators protect survey standard errors against false inflation caused by spatial trends and geographic sorting.

### 2. Random Group Systematic Sampling

To achieve strictly unbiased variance estimation without sacrificing the operational simplicity of systematic sampling, Wolter recommended **Random Group Systematic Selection**:
1. Instead of selecting a single systematic sample with interval $k = N / n$, the desired total sample size $n$ is divided into $R$ independent sub-samples ($R \ge 5$ or $10$), each of size $m = n / R$.
2. The sampling interval is expanded to:
   $$k' = \frac{N}{m} = R \frac{N}{n}$$
3. The statistician draws $R$ independent random starts $r_1, r_2, \dots, r_R$ from $\{1, 2, \dots, k'\}$ without replacement.
4. Each random start generates an independent systematic sample $s_r$ of size $m$, yielding $R$ independent systematic sample means $\bar{y}_1^*, \bar{y}_2^*, \dots, \bar{y}_R^*$.

The overall sample mean is the simple average:
$$\bar{\bar{y}} = \frac{1}{R} \sum_{r=1}^R \bar{y}_r^*$$

The **Random Group Variance Estimator** is:
$$\hat{V}_{RG}(\bar{\bar{y}}) = \frac{1 - f}{R(R - 1)} \sum_{r=1}^R (\bar{y}_r^* - \bar{\bar{y}})^2$$

Because the $R$ random starts are drawn independently, $\hat{V}_{RG}$ is a **strictly design-unbiased estimator** of the true sampling variance! Random group systematic sampling completely resolves the non-estimability of systematic variance while preserving all the fieldwork efficiencies of systematic selection.

---

## Practical Synthesis, Complex Geographies and Field Diagnostics

The practical execution of cluster and multistage surveys in developing and transitional statistical systems requires rigorous field management protocols to prevent non-sampling errors from overwhelming the theoretical gains of probability sampling.

### Household Listing Protocols and Segmentation

When Primary Sampling Units are selected, field teams must enumerate the secondary sampling units. In rapidly growing urban centers or informal settlements, census cartography rapidly becomes obsolete. Survey agencies implement standardized listing protocols:
1. **Canvassing and Boundary Verification**: Field supervisors locate the physical boundaries of the selected PSU using GPS coordinates and satellite basemaps.
2. **Segmentation**: If the PSU contains more than 300 households, it is partitioned into 2 to 4 compact segments with well-defined physical boundaries, and one segment is selected with probability proportional to estimated size.
3. **Numbering and Listing**: Enumerators walk sequentially through the segment, assigning a unique identification number to every structure and dwelling unit, recording the name of the household head and physical address.
4. **Equal Probability Systematic Selection**: Once the complete listing of $M_i$ households is compiled, field teams apply a systematic sampling interval $k_i = M_i / m_i$ with a random start provided by the central office. Interviewers are strictly prohibited from selecting households on the spot, as informal substitution introduces severe selection bias.

### Design Effect Monitoring and Weight Trimming

During survey analysis, survey statisticians calculate the empirical design effect for all primary survey indicators:
$$\text{Deff}_{emp} = \frac{\hat{V}_{complex}(\hat{\theta})}{\hat{V}_{srs}(\hat{\theta})}$$

Key empirical guidelines include:
- Demographic indicators (e.g., age, sex ratio) typically exhibit low clustering: $\text{Deff} \approx 1.2 - 1.8$ ($\rho \approx 0.01 - 0.03$).
- Health and immunization indicators (e.g., clinic access, measles vaccination) exhibit moderate clustering: $\text{Deff} \approx 2.0 - 3.5$ ($\rho \approx 0.05 - 0.10$).
- Poverty, agricultural practices, and environmental conditions exhibit severe clustering: $\text{Deff} \approx 4.0 - 8.0+$ ($\rho \approx 0.15 - 0.30$).

When cluster sizes $M_i$ vary widely, sampling weights $w_{ij} = \frac{1}{\pi_{ij}}$ fluctuate substantially. Extreme weights inflate variance according to Kish's weight design effect formula:
$$\text{Deff}_w = 1 + L = 1 + \frac{\sum (w_k - \bar{w})^2}{n \bar{w}^2} = \frac{n \sum w_k^2}{(\sum w_k)^2}$$
Total design effect is approximately the product of clustering and weighting effects:
$$\text{Deff}_{total} \approx \text{Deff}_c \times \text{Deff}_w$$

To protect survey precision against explosive variances caused by outlier weights, statistical agencies apply **weight trimming**, capping weights at the 95th or 99th percentile and recalibrating totals to preserve design consistency. In the next unit, we explore how unequal probability selection mechanisms—most notably Probability Proportional to Size (PPS)—eliminate this weight variance altogether.
