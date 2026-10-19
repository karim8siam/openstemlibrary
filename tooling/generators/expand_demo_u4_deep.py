import re
from pathlib import Path

d = Path("publishing/drafts/statistics-probability-demography-and-population-statistics")

def prose_count(text):
    text = re.sub(r"\$\$[\s\S]*?\$\$", " ", text)
    text = re.sub(r"\$[^$\n]+\$", " ", text)
    text = re.sub(r"```[\s\S]*?```", " ", text)
    text = re.sub(r"`[^`\n]+`", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"^#+\s.*$", " ", text, flags=re.MULTILINE)
    text = re.sub(r"^[-*+]\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"^\d+\.\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    words = re.findall(r"\b[A-Za-z]+(?:['’\-][A-Za-z]+)*\b", text)
    return len(words)

u4 = (d / "unit-4.md").read_text(encoding="utf-8")
u4_add = """
### Variance of Life Table Functions and Chiang's Large-Sample Variance of Life Expectancy
In applied demographic and public health research, life table functions are estimated from empirical samples of deaths and living populations, making them subject to random stochastic fluctuations. In 1960 and 1984, C. L. Chiang developed the classical large-sample variance formulas that allow mathematical demographers to attach standard errors and confidence intervals to life expectancy at birth $e_0$ and remaining life expectancy $e_x$.

#### The Binomial Sampling Model for Cohort Deaths
Consider the cohort in age interval $[x, x+n)$. Conditional on $l_x$ survivors entering the interval, the number of deaths $_n d_x$ follows a binomial distribution with sample size $l_x$ and probability parameter $_n q_x$:

$$_n d_x \\sim \\text{Binomial}(l_x, {_n q_x})$$

The variance of the sample mortality probability $_n q_x$ is given by:

$$\\text{Var}(_n q_x) = \\frac{_n q_x (1 - {_n q_x})}{l_x}$$

When converting from empirical central death rates $_n m_x = {_n D_x} / {_n P_x}$, Chiang showed that using the Taylor series delta method, the variance of the life table mortality probability is:

$$\\text{Var}(_n q_x) = \\frac{n^2 \\cdot {_n m_x} (1 - {_n a_x} \\cdot {_n m_x})}{_n P_x \\cdot \\left[ 1 + (n - {_n a_x}) {_n m_x} \\right]^3}$$

#### Chiang's Variance Formula for Life Expectancy ($e_x$)
To derive the variance of the remaining life expectancy $e_x = T_x / l_x$, Chiang expressed $e_x$ as a linear combination of the conditional survival probabilities across all subsequent age intervals. By assuming that mortality probabilities in disjoint age intervals are stochastically independent, Chiang established that:

$$\\text{Var}(e_x) = \\sum_{y \\ge x} \\left( _n p_x \\right)^2 \\cdot \\left[ (1 - {_n a_y}) \\cdot n + e_{y+n} \\right]^2 \\cdot \\text{Var}(_n q_y)$$

For life expectancy at birth ($x = 0$), this simplifies to:

$$\\text{Var}(e_0) = \\sum_{y=0}^{\\omega} \\left( \\frac{l_y}{l_0} \\right)^2 \\cdot \\left[ (1 - {_n a_y}) \\cdot n + e_{y+n} \\right]^2 \\cdot \\text{Var}(_n q_y)$$

The standard error is $\\text{SE}(e_0) = \\sqrt{\\text{Var}(e_0)}$, allowing the construction of asymptotic ninety-five percent Wald confidence intervals:

$$\\text{CI}_{95\\%}(e_0) = \\left[ \\hat{e}_0 - 1.96 \\cdot \\text{SE}(\\hat{e}_0), \\; \\hat{e}_0 + 1.96 \\cdot \\text{SE}(\\hat{e}_0) \\right]$$

In municipal health departments and small island nations where population counts are modest (e.g., populations under 100,000), Chiang's variance formulas provide the indispensable statistical foundation for determining whether observed gains in life expectancy represent genuine epidemiological improvements or mere random sampling noise.

### Sullivan's Method for Health-Adjusted and Disability-Free Life Expectancy
In modern health economics, demographers go beyond measuring mere length of life to quantify the qualitative health status of person-years lived. In 1971, D. F. Sullivan formulated an elegant mathematical extension of the life table that integrates prevalence data on chronic disability with standard life table person-years.

#### Mathematical Formulation of Sullivan's Health Table
Let $_n L_x$ denote the standard life table person-years lived between ages $x$ and $x+n$.
Let $_n \\pi_x$ denote the age-specific prevalence of chronic illness, severe functional limitation, or cognitive disability in the living population, typically measured through representative national health interview surveys (such as the National Health and Nutrition Examination Survey or European Health Interview Survey):

$$_n \\pi_x = \\frac{\\text{Number of Persons with Disability in Age Interval } [x, x+n)}{_n P_x}$$

Sullivan partitions the total person-years $_n L_x$ into two mutually exclusive components:
1. **Person-Years Lived with Disability**:
   $$_n L_x^D = {_n \\pi_x} \\cdot {_n L_x}$$
2. **Person-Years Lived Free of Disability**:
   $$_n L_x^{DF} = (1 - {_n \\pi_x}) \\cdot {_n L_x}$$

The total cumulative disability-free person-years remaining above age $x$ is:

$$T_x^{DF} = \\sum_{y \\ge x} {_n L_y^{DF}} = \\sum_{y \\ge x} (1 - {_n \\pi_y}) \\cdot {_n L_y}$$

The **Disability-Free Life Expectancy ($DFLE_x$)** (also termed healthy life years) is:

$$DFLE_x = \\frac{T_x^{DF}}{l_x}$$

The **Proportion of Remaining Life Spent Free of Disability** is:

$$P_{DF}(x) = \\frac{DFLE_x}{e_x} \\times 100 = \\frac{T_x^{DF}}{T_x} \\times 100$$

Sullivan's method reveals striking public health realities: while biological life expectancy at birth $e_0$ in Western nations often reaches eighty-two years, disability-free life expectancy $DFLE_0$ is frequently between sixty-eight and seventy-two years, indicating that individuals spend an average of ten to fourteen years living with chronic functional impairments. Comparing $DFLE$ across cohorts over time provides the decisive empirical test of the Fries compression of morbidity hypothesis.
"""

u4 = u4.replace("## Fully worked question 3", u4_add + "\n## Fully worked question 3")
(d / "unit-4.md").write_text(u4, encoding="utf-8")
print(f"Deeply Expanded Unit 4: {prose_count((d / 'unit-4.md').read_text(encoding='utf-8'))} words")
