# tooling/add-unit4-depth.py
content = r"""

---

## Sudman's Optimal Cluster Take Rule and Hansen–Hurwitz Field Cost Models

In designing multistage cluster surveys, one of the most critical decisions confronting the survey methodologist is determining the **optimal cluster take** (the number of households or individuals $m$ to interview within each sampled primary sampling unit). If $m$ is chosen too small (e.g. $m = 2$ or $3$), field travel costs explode because enumerator teams must journey across hundreds of geographically separated villages. Conversely, if $m$ is chosen too large (e.g. $m = 80$ or $100$), the survey suffers from severe variance inflation due to intracluster correlation, causing the design effect $\text{Deff} = 1 + (m - 1)\rho$ to skyrocket and wasting survey budget on redundant interviews.

To formalize this fundamental trade-off, Seymour Sudman (1976) and Hansen, Hurwitz, and Madow (1953) formulated mathematical models for the optimal cluster take $m^*$.

### Mathematical Derivation of Sudman's Formula
Consider a two-stage cluster survey with equal cluster sizes $M$. The statistician wishes to estimate a population mean $\bar{Y}$.
The total sampling variance under two-stage sampling is:
$$V(\bar{y}) \approx \frac{S^2}{n m} \left[ 1 + (m - 1)\rho \right] = \frac{S^2}{n m} \left[ (1 - \rho) + m \rho \right] = S^2 \left[ \frac{1 - \rho}{n m} + \frac{\rho}{n} \right]$$

Now consider the classical field budget cost model:
$$C = c_0 + c_1 n + c_2 n m$$
where:
- $c_0$ is overhead administrative cost.
- $c_1$ is the cost of adding an additional primary sampling unit (cluster listing, community entry, supervisor travel, and lodging).
- $c_2$ is the marginal cost of interviewing an additional household within an already visited cluster.
- The total variable budget available for field operations is $C_{var} = C - c_0 = n (c_1 + c_2 m)$.

Solving the budget constraint for the number of clusters $n$:
$$n = \frac{C_{var}}{c_1 + c_2 m}$$

Substitute this expression for $n$ into the variance formula:
$$V(\bar{y}) \approx \frac{S^2}{C_{var}} (c_1 + c_2 m) \left[ \frac{1 - \rho}{m} + \rho \right] = \frac{S^2}{C_{var}} \left[ \frac{c_1(1 - \rho)}{m} + c_1 \rho + c_2(1 - \rho) + c_2 m \rho \right]$$

Notice that $c_1 \rho$ and $c_2(1 - \rho)$ are constants independent of $m$.
To find the value of $m$ that minimizes the variance $V(\bar{y})$ for a fixed budget $C_{var}$, differentiate with respect to $m$ and set to zero:
$$\frac{\partial V(\bar{y})}{\partial m} = \frac{S^2}{C_{var}} \left[ -\frac{c_1(1 - \rho)}{m^2} + c_2 \rho \right] = 0$$

Equating the two terms:
$$\frac{c_1(1 - \rho)}{m^2} = c_2 \rho \implies m^2 = \frac{c_1}{c_2} \left( \frac{1 - \rho}{\rho} \right)$$

Taking the positive square root yields **Sudman's Optimal Cluster Take Formula**:
$$m^* = \sqrt{\frac{c_1}{c_2} \left( \frac{1 - \rho}{\rho} \right)}$$

### Methodological Interpretation of Sudman's Rule
Sudman's formula reveals the exact mathematical interplay between cost structure and demographic clustering:
1. **Ratio of Unit Costs ($c_1 / c_2$)**: The term $c_1 / c_2$ represents the relative cost of accessing a cluster compared to interviewing an individual within that cluster.
   - If travel is cheap ($c_1 \approx c_2$), $m^*$ is small: the survey should visit many clusters and conduct very few interviews per cluster.
   - If travel is extremely expensive (e.g., remote rural provinces where reaching a cluster requires four-wheel drive vehicles or boats, such that $c_1 / c_2 = 50$ or $100$), $m^*$ expands substantially, justifying larger cluster takes to amortize heavy travel costs.
2. **Intraclass Correlation ($\rho$)**: The term $(1 - \rho)/\rho$ represents the demographic diversity of the cluster.
   - When $\rho$ is small ($\rho \approx 0.01$), units within a cluster are nearly independent: $(1 - \rho)/\rho \approx 99$, driving $m^*$ upward.
   - When $\rho$ is large ($\rho \approx 0.20$), units within a cluster are nearly identical copies of one another: $(1 - \rho)/\rho \approx 4$, forcing $m^*$ down to avoid collecting redundant data.

### Numerical Walkthrough: Sudman's Rule in Field Practice
Suppose a national statistical agency is designing a household expenditure survey across rural districts:
- Cost to establish a cluster (cartography, listing, community leader consent, travel): $c_1 = 450 \text{ dollars}$.
- Cost per household interview: $c_2 = 18 \text{ dollars}$.
- Cost ratio: $c_1 / c_2 = 450 / 18 = 25.0$.
- Pilot survey estimate of intracluster correlation for household consumption expenditure: $\rho = 0.06$.

Evaluate Sudman's formula:
$$m^* = \sqrt{25.0 \times \left( \frac{1 - 0.06}{0.06} \right)} = \sqrt{25.0 \times \left( \frac{0.94}{0.06} \right)} = \sqrt{25.0 \times 15.6667} = \sqrt{391.667} \approx 19.79 \approx 20 \text{ households}$$

The optimal cluster take is exactly **$20$ households per primary sampling unit**.
If the total available variable field budget is $C_{var} = 72,000 \text{ dollars}$, the optimal number of clusters to sample is:
$$n^* = \frac{C_{var}}{c_1 + c_2 m^*} = \frac{72,000}{450 + 18(20)} = \frac{72,000}{450 + 360} = \frac{72,000}{810} \approx 88.88 \approx 89 \text{ clusters}$$

The survey will visit $n = 89$ clusters, sampling $m = 20$ households per cluster, yielding a total sample size of $89 \times 20 = 1,780$ households. This allocation mathematically guarantees the lowest possible sampling variance for the fixed 72,000-dollar budget.
"""

filepath4 = 'publishing/drafts/statistics-probability-sample-surveys-and-sampling-theory/unit-4.md'
with open(filepath4, 'r', encoding='utf-8') as f:
    text4 = f.read()

split4 = '## Practical Synthesis, Complex Geographies and Field Diagnostics'
if split4 in text4:
    parts = text4.split(split4)
    new4 = parts[0] + content + '\n---\n\n## Practical Synthesis, Complex Geographies and Field Diagnostics' + parts[1]
    with open(filepath4, 'w', encoding='utf-8') as f:
        f.write(new4)
    print("SUCCESSFULLY EXPANDED UNIT 4!")
else:
    print("Unit 4 split phrase not found!")
