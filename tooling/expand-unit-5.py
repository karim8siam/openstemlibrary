# tooling/expand-unit-5.py
import re

content = """

---

## Classical Unequal Probability Without Replacement Schemes: Brewer and Murthy

While the Horvitz–Thompson estimator provides a universal framework for any probability sampling design, implementing unequal probability sampling without replacement (WOR) presents a fundamental technical challenge: for an arbitrary selection protocol, calculating the second-order joint inclusion probabilities $\\pi_{ij}$ is often analytically intractable or yields probabilities where $\\pi_{ij} > \\pi_i \\pi_j$, which causes the Sen–Yates–Grundy variance estimator to produce negative variance estimates.

To overcome this, early pioneers formulated specialized without-replacement selection protocols that guarantee exact first-order probabilities $\\pi_i = n p_i$ while ensuring that joint probabilities $\\pi_{ij}$ satisfy the condition $\\pi_{ij} < \\pi_i \\pi_j$ everywhere, guaranteeing that the Sen–Yates–Grundy variance estimator is strictly non-negative. Two of the most celebrated methods in the literature are Brewer's scheme and Murthy's unordered estimator.

### 1. Brewer's Unequal Probability Selection Scheme

In 1963, K. R. W. Brewer introduced an elegant selection scheme for drawing a sample of $n = 2$ units without replacement such that the inclusion probability of unit $i$ is strictly proportional to its measure of size:
$$\\pi_i = 2 p_i \\quad \\text{for all } i = 1, \\dots, N$$
subject to the physical feasibility condition that $p_i < 1/2$ for all $i$.

#### Selection Algorithm for $n = 2$:
1. **First Draw**: Select the first unit $i$ from the population $U$ with revised selection probability:
   $$p_i^{(1)} = \\frac{p_i (1 - p_i)}{D (1 - 2 p_i)}$$
   where the normalizing denominator $D$ is the constant that ensures the probabilities sum to unity:
   $$D = \\sum_{k=1}^N \\frac{p_k (1 - p_k)}{1 - 2 p_k} = \\frac{1}{2} \\left( 1 + \\sum_{k=1}^N \\frac{p_k}{1 - 2 p_k} \\right)$$
2. **Second Draw**: Having selected unit $i$ on the first draw, select the second unit $j$ ($j \\ne i$) from the remaining $N - 1$ units with probability strictly proportional to its original size:
   $$p_{j|i}^{(2)} = \\frac{p_j}{1 - p_i}$$

#### Proof of Exact Inclusion Probabilities:
The probability that unit $i$ is selected on the first draw is $p_i^{(1)}$.
The probability that unit $i$ is selected on the second draw given that some other unit $j$ was selected first is:
$$P(\\text{Unit } i \\text{ on draw 2}) = \\sum_{j \\ne i}^N p_j^{(1)} p_{i|j}^{(2)} = \\sum_{j \\ne i}^N \\left[ \\frac{p_j (1 - p_j)}{D (1 - 2 p_j)} \\right] \\left[ \\frac{p_i}{1 - p_j} \\right] = \\frac{p_i}{D} \\sum_{j \\ne i}^N \\frac{p_j}{1 - 2 p_j}$$

The unconditional first-order inclusion probability of unit $i$ is the sum of its chances of being selected on either draw:
$$\\pi_i = P(\\text{Unit } i \\text{ on draw 1}) + P(\\text{Unit } i \\text{ on draw 2}) = \\frac{p_i (1 - p_i)}{D (1 - 2 p_i)} + \\frac{p_i}{D} \\sum_{j \\ne i}^N \\frac{p_j}{1 - 2 p_j}$$
$$= \\frac{p_i}{D} \\left[ \\frac{1 - p_i}{1 - 2 p_i} + \\sum_{j \\ne i}^N \\frac{p_j}{1 - 2 p_j} \\right] = \\frac{p_i}{D} \\left[ 1 + \\frac{p_i}{1 - 2 p_i} + \\sum_{j \\ne i}^N \\frac{p_j}{1 - 2 p_j} \\right]$$
$$= \\frac{p_i}{D} \\left[ 1 + \\sum_{k=1}^N \\frac{p_k}{1 - 2 p_k} \\right]$$

Now substitute the definition of $D = \\frac{1}{2} \\left( 1 + \\sum_{k=1}^N \\frac{p_k}{1 - 2 p_k} \\right)$:
$$\\pi_i = \\frac{p_i}{\\frac{1}{2} \\left( 1 + \\sum_{k=1}^N \\frac{p_k}{1 - 2 p_k} \\right)} \\left[ 1 + \\sum_{k=1}^N \\frac{p_k}{1 - 2 p_k} \\right] = 2 p_i$$
This proves that Brewer's method yields strictly exact first-order PPS inclusion probabilities $\\pi_i = 2 p_i$ without any approximation error.

#### Joint Inclusion Probabilities $\\pi_{ij}$:
The joint probability that both unit $i$ and unit $j$ are included in the sample is:
$$\\pi_{ij} = P(i \\text{ 1st}, j \\text{ 2nd}) + P(j \\text{ 1st}, i \\text{ 2nd}) = p_i^{(1)} p_{j|i}^{(2)} + p_j^{(1)} p_{i|j}^{(2)}$$
$$= \\left[ \\frac{p_i (1 - p_i)}{D (1 - 2 p_i)} \\right] \\left[ \\frac{p_j}{1 - p_i} \\right] + \\left[ \\frac{p_j (1 - p_j)}{D (1 - 2 p_j)} \\right] \\left[ \\frac{p_i}{1 - p_j} \\right]$$
$$= \\frac{p_i p_j}{D} \\left[ \\frac{1}{1 - 2 p_i} + \\frac{1}{1 - 2 p_j} \\right] = \\frac{2 p_i p_j}{D} \\left[ \\frac{1 - p_i - p_j}{(1 - 2 p_i)(1 - 2 p_j)} \\right]$$

Brewer proved that under this formulation, the inequality $\\pi_{ij} < \\pi_i \\pi_j = 4 p_i p_j$ holds universally for all distinct pairs $(i, j)$. Consequently, the Sen–Yates–Grundy variance estimator is guaranteed to be strictly positive for all realized samples.

---

### 2. Murthy's Unordered Estimator

In standard Horvitz–Thompson estimation, the order in which units are drawn is ignored, but the estimator relies heavily on knowing the joint inclusion probabilities $\\pi_{ij}$. In 1956, Des Raj proposed an ordered estimator where observations are weighted according to their sequential draw probabilities. While Des Raj's estimator is strictly unbiased, it is inefficient because it depends on the order of the sample draws.

Recognizing this deficiency, V. K. Murthy (1957) applied the **Rao–Blackwell theorem** to Des Raj's estimator: by conditioning on the unordered set of sampled units $s = \\{i_1, i_2, \\dots, i_n\\}$, Murthy eliminated the order dependence, producing a uniformly minimum variance unordered estimator that does not require calculating $\\pi_{ij}$.

#### Murthy's Estimator for $n = 2$:
Consider drawing $n = 2$ units without replacement.
- Draw 1: Unit $i$ is selected with probability $p_i$.
- Draw 2: Unit $j$ is selected from the remaining units with conditional probability $p_{j|i} = \\frac{p_j}{1 - p_i}$.

The joint probability of drawing unit $i$ first and unit $j$ second is:
$$P(i, j) = p_i \\times \\frac{p_j}{1 - p_i} = \\frac{p_i p_j}{1 - p_i}$$
The joint probability of drawing unit $j$ first and unit $i$ second is:
$$P(j, i) = p_j \\times \\frac{p_i}{1 - p_j} = \\frac{p_i p_j}{1 - p_j}$$

The unconditional probability of obtaining the unordered sample pair $s = \\{i, j\\}$ is:
$$P(s) = P(i, j) + P(j, i) = \\frac{p_i p_j}{1 - p_i} + \\frac{p_i p_j}{1 - p_j} = p_i p_j \\left[ \\frac{(1 - p_j) + (1 - p_i)}{(1 - p_i)(1 - p_j)} \\right] = \\frac{p_i p_j (2 - p_i - p_j)}{(1 - p_i)(1 - p_j)}$$

By Rao–Blackwellization, Murthy's unordered estimator for the population total $Y$ based on the realized pair $(y_1, y_2)$ with size measures $(p_1, p_2)$ is:
$$\\hat{Y}_M = \\frac{1}{2 - p_1 - p_2} \\left[ \\frac{(1 - p_2) y_1}{p_1} + \\frac{(1 - p_1) y_2}{p_2} \\right]$$

#### Proof of Unbiasedness:
To prove $E(\\hat{Y}_M) = Y$, evaluate the expectation over all possible unordered sample pairs $s = \\{i, j\\}$:
$$E(\\hat{Y}_M) = \\sum_{i=1}^N \\sum_{j > i}^N P(s) \\hat{Y}_M(s)$$
$$= \\sum_{i=1}^N \\sum_{j > i}^N \\left[ \\frac{p_i p_j (2 - p_i - p_j)}{(1 - p_i)(1 - p_j)} \\right] \\times \\frac{1}{2 - p_i - p_j} \\left[ \\frac{(1 - p_j) y_i}{p_i} + \\frac{(1 - p_i) y_j}{p_j} \\right]$$
$$= \\sum_{i=1}^N \\sum_{j > i}^N \\frac{p_i p_j}{(1 - p_i)(1 - p_j)} \\left[ \\frac{(1 - p_j) y_i}{p_i} + \\frac{(1 - p_i) y_j}{p_j} \\right]$$
$$= \\sum_{i=1}^N \\sum_{j > i}^N \\left[ \\frac{p_j y_i}{1 - p_i} + \\frac{p_i y_j}{1 - p_j} \\right]$$

Expanding the double sum:
$$E(\\hat{Y}_M) = \\sum_{i=1}^N \\frac{y_i}{1 - p_i} \\sum_{j \\ne i}^N p_j$$
Since $\\sum_{j \\ne i}^N p_j = 1 - p_i$:
$$E(\\hat{Y}_M) = \\sum_{i=1}^N \\frac{y_i}{1 - p_i} (1 - p_i) = \\sum_{i=1}^N y_i = Y$$
This rigorous proof demonstrates that Murthy's estimator is strictly design-unbiased.

#### The Exact Variance of Murthy's Estimator:
Murthy derived the closed-form population variance:
$$V(\\hat{Y}_M) = \\sum_{i=1}^N \\sum_{j > i}^N p_i p_j \\left( \\frac{1 - p_i - p_j}{2 - p_i - p_j} \\right) \\left( \\frac{y_i}{p_i} - \\frac{y_j}{p_j} \\right)^2$$

Notice the structure of this variance:
1. Like the Sen–Yates–Grundy variance, it depends on differences of ratios $(y_i / p_i - y_j / p_j)^2$. If $y_i$ is perfectly proportional to $p_i$, the variance vanishes identically!
2. The weight coefficient $p_i p_j \\left( \\frac{1 - p_i - p_j}{2 - p_i - p_j} \\right)$ is strictly positive for all $p_i + p_j < 1$.

#### Murthy's Strictly Non-Negative Sample Variance Estimator:
From a realized sample pair $(y_1, y_2)$ with size probabilities $(p_1, p_2)$, the unbiased sample estimator of variance is:
$$\\hat{V}(\\hat{Y}_M) = \\frac{(1 - p_1)(1 - p_2)(1 - p_1 - p_2)}{(2 - p_1 - p_2)^2} \\left( \\frac{y_1}{p_1} - \\frac{y_2}{p_2} \\right)^2$$

Because $(1 - p_1) > 0$, $(1 - p_2) > 0$, and $(1 - p_1 - p_2) > 0$ under any standard sampling frame, **Murthy's variance estimator is strictly non-negative for every single sample that can ever be drawn**. It requires no matrix inversion and no computation of second-order inclusion probabilities, making it an extraordinarily reliable tool in empirical survey research.
"""

filepath = 'publishing/drafts/statistics-probability-sample-surveys-and-sampling-theory/unit-5.md'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

split_phrase = '## Poisson Sampling and Pareto PPS'
if split_phrase in text:
    parts = text.split(split_phrase)
    new_text = parts[0] + content + '\n---\n\n## Poisson Sampling and Pareto PPS' + parts[1]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("SUCCESSFULLY EXPANDED UNIT 5!")
else:
    print("Split phrase not found!")
