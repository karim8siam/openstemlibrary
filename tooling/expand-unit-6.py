# tooling/expand-unit-6.py
import re

content = r"""

---

## Double Sampling for Nonresponse: The Hansen–Hurwitz Multi-Phase Architecture

In modern survey field operations, nonresponse is inevitable. When field operations encounter non-respondents, simply replacing non-respondents with adjacent households introduces fatal selection bias. In 1946, Morris Hansen and William Hurwitz formulated an ingenious application of **Two-Phase (Double) Sampling for Nonresponse**, which converts nonresponse from an uncontrolled bias hazard into a controlled probability design.

### The Two-Phase Nonresponse Protocol

Consider a target population of $N$ units. The population conceptually consists of two strata:
1. **Response Stratum ($U_1$)**: Units who would respond if contacted under the initial standard survey mode (e.g. mail questionnaire or online web survey). Size $N_1$, proportion $W_1 = N_1 / N$.
2. **Nonresponse Stratum ($U_2$)**: Units who do not respond to the initial survey mode. Size $N_2$, proportion $W_2 = N_2 / N$.

Neither $N_1$ nor $N_2$ is known prior to data collection. The survey protocol proceeds in two sequential phases:

1. **Phase 1**: An initial probability sample of $n$ units is selected from $N$ via SRSWOR. The questionnaire is administered via a low-cost survey mode (e.g., electronic mail or self-administered web portal at unit cost $c_1$).
   - $n_1$ units respond successfully, providing observations $y_{11}, \dots, y_{1n_1}$.
   - $n_2 = n - n_1$ units fail to respond.
2. **Phase 2 (Subsampling Nonrespondents)**: From the $n_2$ non-respondents, a subsample of size $m = n_2 / k$ ($k \ge 1$) is selected at random via SRSWOR.
   - Field interviewers deploy an intensive, high-cost tracking protocol (e.g., personal face-to-face visits with monetary incentives at unit cost $c_2 \gg c_1$) to achieve a **$100\%$ response rate** among the $m$ selected nonrespondents, obtaining measurements $y_{21}, \dots, y_{2m}$.

### Hansen–Hurwitz Unbiased Estimator

The **Hansen–Hurwitz Estimator** of the population mean $\bar{Y}$ is:
$$\hat{\bar{Y}}_{HH} = \frac{n_1}{n} \bar{y}_1 + \frac{n_2}{n} \bar{y}_{2m} = w_1 \bar{y}_1 + w_2 \bar{y}_{2m}$$
where:
- $\bar{y}_1 = \frac{1}{n_1} \sum_{i=1}^{n_1} y_{1i}$ is the sample mean of the initial respondents.
- $\bar{y}_{2m} = \frac{1}{m} \sum_{j=1}^m y_{2j}$ is the sample mean of the subsampled nonrespondents.
- $w_1 = n_1 / n$ and $w_2 = n_2 / n$ are the empirical sample response and nonresponse proportions.

#### Proof of Strict Unbiasedness:
Using the law of total expectation, condition on the realized Phase 1 sample $s$:
$$E(\hat{\bar{Y}}_{HH}) = E_1 \left[ E_2(\hat{\bar{Y}}_{HH} \mid s) \right]$$
In Phase 2, the $m$ units are drawn via SRSWOR from the $n_2$ nonrespondents. Therefore, $E_2(\bar{y}_{2m} \mid s) = \bar{y}_2$, where $\bar{y}_2 = \frac{1}{n_2} \sum_{i \in s_2} y_{2i}$ is the mean of all nonrespondents in the initial sample $s$:
$$E_2(\hat{\bar{Y}}_{HH} \mid s) = \frac{n_1}{n} \bar{y}_1 + \frac{n_2}{n} \bar{y}_2 = \frac{n_1 \bar{y}_1 + n_2 \bar{y}_2}{n} = \bar{y}$$
where $\bar{y}$ is the unobserved overall sample mean of the full sample of size $n$.
Now take expectation over Phase 1 SRSWOR selection from the population $U$:
$$E_1(\bar{y}) = \bar{Y}$$
Thus:
$$E(\hat{\bar{Y}}_{HH}) = \bar{Y}$$
The Hansen–Hurwitz estimator is **strictly design-unbiased for the true population mean**, completely eliminating nonresponse bias through probability subsampling.

### Exact Sampling Variance and Optimal Allocation

Using the conditional variance decomposition $V(\hat{\bar{Y}}_{HH}) = V_1(E_2(\hat{\bar{Y}}_{HH} \mid s)) + E_1(V_2(\hat{\bar{Y}}_{HH} \mid s))$:
1. $V_1(E_2(\hat{\bar{Y}}_{HH} \mid s)) = V_1(\bar{y}) = \left( \frac{1 - f}{n} \right) S^2$
2. $E_1(V_2(\hat{\bar{Y}}_{HH} \mid s)) = E_1 \left[ \left(\frac{n_2}{n}\right)^2 \left(\frac{1 - m/n_2}{m}\right) s_{2}^2 \right] = \left( \frac{k - 1}{n} \right) W_2 S_2^2$

Summing both components yields the exact variance:
$$V(\hat{\bar{Y}}_{HH}) = \left( \frac{N - n}{N n} \right) S^2 + \frac{W_2 (k - 1)}{n} S_2^2$$
where:
- $S^2$ is the overall population variance.
- $S_2^2$ is the variance among units in the nonresponse stratum $U_2$.
- $W_2$ is the population nonresponse rate.

#### Cost Optimization:
The total expected survey budget is:
$$C = c_0 + c_1 n + c_2 E(m) = c_0 + c_1 n + c_2 \frac{n W_2}{k} = c_0 + n \left( c_1 + \frac{c_2 W_2}{k} \right)$$
where $c_0$ is overhead fixed cost, $c_1$ is initial mail/web contact cost, and $c_2$ is intensive face-to-face field follow-up cost.

Minimizing the product of variable cost and variance via Cauchy–Schwarz inequality yields the **Optimal Subsampling Interval ($k^*$)** and **Optimal Initial Sample Size ($n^*$)**:
$$k^* = \sqrt{\frac{c_2 (S^2 - W_2 S_2^2)}{c_1 S_2^2}}$$
$$n^* = \frac{C - c_0}{c_1 + c_2 W_2 / k^*} \approx \frac{V_0}{S^2} \left[ S^2 - W_2 S_2^2 + W_2 S_2 \sqrt{\frac{c_2}{c_1}} \right]$$

When follow-up costs are high ($c_2 / c_1 \gg 1$), $k^*$ increases, directing field interviewers to intensively trace a smaller, highly targeted subsample of nonrespondents while preserving design unbiasedness and protecting survey budgets.
"""

filepath = 'publishing/drafts/statistics-probability-sample-surveys-and-sampling-theory/unit-6.md'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

split_phrase = '## Bias-Reduced and Exactly Unbiased Ratio Estimation'
if split_phrase in text:
    parts = text.split(split_phrase)
    new_text = parts[0] + content + '\n---\n\n## Bias-Reduced and Exactly Unbiased Ratio Estimation' + parts[1]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("SUCCESSFULLY EXPANDED UNIT 6!")
else:
    print("Split phrase not found!")
