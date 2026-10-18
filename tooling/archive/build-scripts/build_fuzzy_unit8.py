# -*- coding: utf-8 -*-
"""
build_fuzzy_unit8.py
Constructs Unit 8: Real-World Applications: Control, Decision Making & AI
Strictly ZERO course numbers.
"""

def get_unit8():
    u8 = {
        "number": 8,
        "title": "Real-World Applications: Control, Decision Making & AI",
        "leadSummary": "Comprehensive applied mathematical engineering of fuzzy systems: architecture of Fuzzy Inference Systems (FIS), comparative analysis of Mamdani (fuzzy consequent) vs Takagi-Sugeno-Kang (polynomial consequent) architectures, rule bases, aggregation, defuzzification methods (Centroid COG, Bisector, Mean of Maxima), industrial control applications (inverted pendulum balancing, autonomous steering, thermal control), Fuzzy Multi-Criteria Decision Making (Fuzzy AHP and Fuzzy TOPSIS), Fuzzy c-Means clustering (FCM), objective function minimization, and adaptive neuro-fuzzy inference systems (ANFIS).",
        "simulations": ["sim_fuzzy_control_pendulum"],
        "sections": [
            {
                "secNumber": "8.1",
                "title": "Mamdani vs Takagi-Sugeno-Kang (TSK) Fuzzy Inference Systems (FIS)",
                "content": r"""### 1. Architecture of a Fuzzy Inference System (FIS)
A **Fuzzy Inference System** (FIS) is a mathematical framework that maps crisp numerical inputs to crisp numerical outputs using fuzzy reasoning and expert knowledge.
The standard architecture comprises four essential components:
1. **Fuzzification Interface:** Transforms crisp sensor measurements into degrees of membership across linguistic terms.
2. **Rule Base (Knowledge Base):** A collection of fuzzy IF-THEN rules reflecting human domain expertise.
3. **Inference Engine:** Applies fuzzy logic operators (t-norms, implications) to aggregate rule activations.
4. **Defuzzification Interface:** Synthesizes the aggregated fuzzy output into a single crisp control action.

---

### 2. Mamdani Fuzzy Inference (1975)
Introduced by Ebrahim Mamdani to control a steam engine, this is the most widespread and intuitive FIS model.
- **Rule Structure:** Both antecedent and consequent are fuzzy linguistic propositions:
  $$\text{Rule } k: \text{IF } x_1 \text{ is } A_1^k \text{ AND } x_2 \text{ is } A_2^k \text{ THEN } y \text{ is } B^k$$
  where $A_i^k$ and $B^k$ are fuzzy sets with continuous membership functions.
- **Firing Strength:** $w_k = \min(\mu_{A_1^k}(x_1), \mu_{A_2^k}(x_2))$.
- **Implication:** The consequent fuzzy set is clipped (Mamdani min implication: $\mu_{B^{*k}}(y) = \min(w_k, \mu_{B^k}(y))$) or scaled (Larsen product implication).
- **Aggregation:** $\mu_{\text{out}}(y) = \max_k \mu_{B^{*k}}(y)$.
- **Output:** Requires explicit continuous integration (e.g. Centroid) to defuzzify.

---

### 3. Takagi-Sugeno-Kang (TSK) Fuzzy Inference (1985)
Introduced by Tomohiro Takagi and Michio Sugeno to provide computationally efficient control and mathematical stability proofs.
- **Rule Structure:** The antecedent is fuzzy, but the consequent is a **crisp functional polynomial** of the input variables:
  $$\text{Rule } k: \text{IF } x_1 \text{ is } A_1^k \text{ AND } x_2 \text{ is } A_2^k \text{ THEN } y_k = p_0^k + p_1^k x_1 + p_2^k x_2$$
  *(If $p_1 = p_2 = 0$, it is a Zero-Order Sugeno FIS where consequents are constant scalars)*.
- **Defuzzification:** Replaced by a simple, exact **weighted average**:
  $$y^* = \frac{\sum_{k=1}^R w_k y_k}{\sum_{k=1}^R w_k}$$
  Zero computational integration required! The TSK model is smooth, differentiable, and forms the mathematical foundation of **Adaptive Neuro-Fuzzy Inference Systems (ANFIS)**."""
            },
            {
                "secNumber": "8.2",
                "title": "Fuzzification, Rule Bases, Inference Engines & Defuzzification (Centroid, Bisector, MOM)",
                "content": r"""### 1. Fuzzification and Rule Evaluation
Given crisp input vector $\mathbf{x}^* = (x_1^*, \dots, x_n^*)$:
1. For each rule $R_k$, compute the membership of each input: $\mu_{A_i^k}(x_i^*)$.
2. Combine antecedent conditions using a t-norm (typically minimum or product) to find the **rule firing strength**:
   $$w_k = \prod_{i=1}^n \mu_{A_i^k}(x_i^*) \quad \text{or} \quad w_k = \min_{i=1}^n \mu_{A_i^k}(x_i^*)$$

---

### 2. Comparative Defuzzification Formulas
Let $\mu_{\text{agg}}(y) = \max_{k=1}^R \mu_{B^{*k}}(y)$ be the aggregated fuzzy output on universe $Y$.

#### 1. Centroid Method (Center of Gravity / Area):
$$y^*_{\text{COG}} = \frac{\int_Y y \, \mu_{\text{agg}}(y) \, dy}{\int_Y \mu_{\text{agg}}(y) \, dy}$$
- Smooth and continuous response under varying inputs. Highly sensitive to all active rules.

#### 2. Bisector of Area (BOA):
The vertical line $y^*_{\text{BOA}}$ that divides the total area into two equal halves:
$$\int_{-\infty}^{y^*_{\text{BOA}}} \mu_{\text{agg}}(y) \, dy = \int_{y^*_{\text{BOA}}}^\infty \mu_{\text{agg}}(y) \, dy$$

#### 3. Middle of Maxima (MOM):
$$y^*_{\text{MOM}} = \frac{1}{|Y_{\max}|} \int_{Y_{\max}} y \, dy, \qquad Y_{\max} = \{y \in Y \mid \mu_{\text{agg}}(y) = \max_{y'} \mu_{\text{agg}}(y')\}$$
- Fast, but can jump discontinuously when rule activations switch."""
            },
            {
                "secNumber": "8.3",
                "title": "Inverted Pendulum and Temperature PID Fuzzy Control Systems",
                "content": r"""### 1. The Inverted Pendulum Benchmark
The inverted pendulum on a moving cart is the quintessential non-linear benchmark for control theory.
The dynamical state is characterized by two state variables:
1. **Error $e(t) = \theta(t)$:** Angular deviation of the pole from vertical.
2. **Change of Error $\Delta e(t) = \dot{\theta}(t)$:** Angular velocity.

---

### 2. Fuzzy Rule Matrix for Pendulum Balancing
Each input is partitioned into 5 linguistic sets:
- **Negative Big (NB), Negative Small (NS), Zero (ZE), Positive Small (PS), Positive Big (PB)**.
The control action is the horizontal force $F$ applied to the cart:

| $\Delta e \setminus e$ | NB | NS | ZE | PS | PB |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **NB** | NB | NB | NS | NS | ZE |
| **NS** | NB | NS | NS | ZE | PS |
| **ZE** | NS | NS | ZE | PS | PS |
| **PS** | NS | ZE | PS | PS | PB |
| **PB** | ZE | PS | PS | PB | PB |

- **Physical Intuition:** If angle is Positive Big (leaning right) and velocity is Positive Big (falling rapidly right), apply Positive Big force to accelerate the cart rightwards and catch the falling pole!
- If angle is Positive Small but velocity is Negative Small (already swinging back towards center), apply Zero force to prevent overshooting."""
            },
            {
                "secNumber": "8.4",
                "title": "Fuzzy Multi-Criteria Decision Making (Fuzzy AHP & TOPSIS)",
                "content": r"""### 1. Decision Making under Linguistic Uncertainty
In classical Multi-Criteria Decision Making (MCDM), human decision makers are forced to assign exact numerical ratings (e.g. *"Alternative A is exactly 3.5 times better than B"*).
Fuzzy MCDM replaces crisp pairwise ratings with **Triangular Fuzzy Numbers (TFNs)** to capture subjective doubt.

---

### 2. Fuzzy Analytic Hierarchy Process (Fuzzy AHP)
Introduced by Buckley (1985) and Chang (1996):
1. Construct the fuzzy pairwise comparison matrix $\tilde{A} = (\tilde{a}_{ij})_{n \times n}$ where $\tilde{a}_{ij} = (l_{ij}, m_{ij}, u_{ij})$.
2. The reciprocal condition satisfies $\tilde{a}_{ji} = \tilde{a}_{ij}^{-1} = (1/u_{ij}, 1/m_{ij}, 1/l_{ij})$.
3. Compute the fuzzy synthetic extent values:
   $$\tilde{S}_i = \sum_{j=1}^n \tilde{a}_{ij} \odot \left[ \sum_{k=1}^n \sum_{j=1}^n \tilde{a}_{kj} \right]^{-1}$$
4. Calculate the degree of possibility $V(\tilde{S}_i \ge \tilde{S}_k)$ and normalize to obtain crisp priority weights $w_i$.

---

### 3. Fuzzy TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)
1. Alternatives are evaluated against criteria using linguistic variables converted to fuzzy decision matrices.
2. Determine the **Fuzzy Positive Ideal Solution (FPIS)** $A^*$ and **Fuzzy Negative Ideal Solution (FNIS)** $A^-$.
3. Compute vertex-based distances $d_i^*$ and $d_i^-$ for each alternative.
4. Calculate the closeness coefficient:
   $$CC_i = \frac{d_i^-}{d_i^* + d_i^-} \in [0, 1]$$
5. Rank alternatives in descending order of $CC_i$."""
            },
            {
                "secNumber": "8.5",
                "title": "Fuzzy Pattern Recognition, Fuzzy c-Means Clustering (FCM) & Neuro-Fuzzy Networks (ANFIS)",
                "content": r"""### 1. Fuzzy c-Means Clustering (Bezdek, 1981)
In classical k-means clustering, each data point $\mathbf{x}_k$ belongs strictly to a single cluster.
In **Fuzzy c-Means (FCM)**, every point has a degree of membership $u_{ik} \in [0, 1]$ across all $c$ clusters such that $\sum_{i=1}^c u_{ik} = 1$.

> **Definition 8.1 (FCM Objective Function):**
> $$J_m(U, V) = \sum_{i=1}^c \sum_{k=1}^N (u_{ik})^m \|\mathbf{x}_k - \mathbf{v}_i\|^2$$
> where:
> - $N$ is the number of data points, $c$ is the number of clusters.
> - $m > 1$ is the **fuzziness exponent** (typically $m = 2$).
> - $\mathbf{v}_i$ is the center of cluster $i$.

#### Alternating Optimization Algorithm:
1. Update cluster centers:
   $$\mathbf{v}_i = \frac{\sum_{k=1}^N (u_{ik})^m \mathbf{x}_k}{\sum_{k=1}^N (u_{ik})^m}$$
2. Update membership matrix:
   $$u_{ik} = \frac{1}{\sum_{j=1}^c \left( \frac{\|\mathbf{x}_k - \mathbf{v}_i\|}{\|\mathbf{x}_k - \mathbf{v}_j\|} \right)^{\frac{2}{m - 1}}}$$
Iterate until convergence $\|\Delta U\| < \epsilon$.

---

### 2. Adaptive Neuro-Fuzzy Inference Systems (ANFIS, Jang 1993)
ANFIS is a multilayer feedforward network that integrates the linguistic interpretability of fuzzy logic with the self-learning capability of neural networks.
- **Layer 1 (Fuzzification):** Adaptive nodes computing membership parameters (e.g. Gaussian bell centers and widths).
- **Layer 2 (Rule Nodes):** Fixed T-norm product nodes: $w_k = \mu_{A^k}(x) \mu_{B^k}(y)$.
- **Layer 3 (Normalization):** Fixed ratio nodes: $\bar{w}_k = \frac{w_k}{\sum w_j}$.
- **Layer 4 (Consequent Layer):** Adaptive linear nodes: $\bar{w}_k f_k = \bar{w}_k (p_k x + q_k y + r_k)$.
- **Layer 5 (Summation):** Fixed output node: $y = \sum \bar{w}_k f_k$.
Trained using hybrid learning: **Recursive Least Squares (RLS)** for linear consequent parameters, and **Backpropagation Gradient Descent** for non-linear antecedent membership parameters."""
            }
        ],
        "problems": [
            {
                "tier": "Fundamentals",
                "title": "Problem 8.1: Step-by-Step Mamdani Fuzzy Inference and Centroid Defuzzification",
                "statement": r"""Consider a two-input, one-output Mamdani FIS for tipping at a restaurant:
- Inputs: Food Quality $x_1 \in [0, 10]$ and Service $x_2 \in [0, 10]$.
- Output: Tip Percentage $y \in [0, 30]\%$.

Rule Base:
- Rule 1: IF Food is Bad OR Service is Poor, THEN Tip is Low.
- Rule 2: IF Service is Good, THEN Tip is Medium.
- Rule 3: IF Food is Delicious OR Service is Excellent, THEN Tip is High.

Linguistic Terms:
- Food Bad: $\text{trapmf}(x_1; 0, 0, 2, 5)$
- Food Delicious: $\text{trapmf}(x_1; 5, 8, 10, 10)$
- Service Poor: $\text{trapmf}(x_2; 0, 0, 2, 5)$
- Service Good: $\text{trimf}(x_2; 3, 6, 9)$
- Service Excellent: $\text{trapmf}(x_2; 6, 9, 10, 10)$
Consequent Tip sets (triangular):
- Low: $\text{trimf}(y; 0, 5, 10)$
- Medium: $\text{trimf}(y; 10, 15, 20)$
- High: $\text{trimf}(y; 20, 25, 30)$

Given inputs: Food Quality $x_1^* = 8.0$, Service $x_2^* = 6.0$.
1. Compute the membership grades for all antecedent terms.
2. Determine the firing strengths $w_1, w_2, w_3$ of the three rules using Zadeh max/min operators.
3. Determine the clipped consequent fuzzy sets.
4. Calculate the crisp defuzzified tip percentage using the Centroid method.""",
                "hints": [
                    "Food is 8.0: Bad is 0, Delicious is 1.0.",
                    "Service is 6.0: Poor is 0, Good is 1.0, Excellent is 0.0.",
                    "Rule 2 fires with strength 1.0, Rule 3 with strength 1.0."
                ],
                "solution": r"""### 1. Antecedent Membership Grades
Inputs: $x_1^* = 8.0$, $x_2^* = 6.0$.
- **Food Quality ($x_1 = 8.0$):**
  - $\mu_{\text{Bad}}(8.0) = 0.0$
  - $\mu_{\text{Delicious}}(8.0) = \frac{8 - 5}{8 - 5} = 1.0$ (since $x_1 \ge 8$, on the core).
- **Service ($x_2 = 6.0$):**
  - $\mu_{\text{Poor}}(6.0) = 0.0$
  - $\mu_{\text{Good}}(6.0) = \frac{6 - 3}{6 - 3} = 1.0$ (at the peak of $\text{trimf}(3, 6, 9)$).
  - $\mu_{\text{Excellent}}(6.0) = 0.0$ (since $x_2 \le 6$). $\blacksquare$

---

### 2. Rule Firing Strengths
- **Rule 1 (Food Bad OR Service Poor):**
  $$w_1 = \max(\mu_{\text{Bad}}(8.0), \mu_{\text{Poor}}(6.0)) = \max(0.0, 0.0) = 0.0$$
- **Rule 2 (Service Good):**
  $$w_2 = \mu_{\text{Good}}(6.0) = 1.0$$
- **Rule 3 (Food Delicious OR Service Excellent):**
  $$w_3 = \max(\mu_{\text{Delicious}}(8.0), \mu_{\text{Excellent}}(6.0)) = \max(1.0, 0.0) = 1.0 \qquad \blacksquare$$

---

### 3. Clipped Consequent Fuzzy Sets
- Rule 1 (Low): Clipped at $w_1 = 0.0 \implies$ No contribution.
- Rule 2 (Medium $\text{trimf}(10, 15, 20)$): Clipped at $w_2 = 1.0 \implies$ Full triangle on $[10, 20]$.
- Rule 3 (High $\text{trimf}(20, 25, 30)$): Clipped at $w_3 = 1.0 \implies$ Full triangle on $[20, 30]$.

The aggregated output is the union of two symmetric triangles of base 10 and height 1:
- Triangle 1 (Medium): Base $[10, 20]$, peak at $15$, area $A_2 = \frac{1}{2}(10)(1) = 5$, centroid $\bar{y}_2 = 15$.
- Triangle 2 (High): Base $[20, 30]$, peak at $25$, area $A_3 = \frac{1}{2}(10)(1) = 5$, centroid $\bar{y}_3 = 25$.

The two triangles meet at $y = 20$ with zero overlap area ($\mu(20) = 0$). $\blacksquare$

---

### 4. Centroid Defuzzification
$$\text{COG}(y^*) = \frac{A_2 \bar{y}_2 + A_3 \bar{y}_3}{A_2 + A_3} = \frac{5(15) + 5(25)}{5 + 5} = \frac{75 + 125}{10} = \frac{200}{10} = 20.0\% \qquad \blacksquare$$
The recommended tip is exactly **$20.0\%$**!"""
            },
            {
                "tier": "Computational Triad",
                "title": "Problem 8.2: First-Order Takagi-Sugeno-Kang (TSK) FIS Evaluation",
                "statement": r"""Consider a two-input, single-output first-order TSK FIS with inputs $x_1, x_2$ and the following two rules:
- **Rule 1:** IF $x_1$ is Small AND $x_2$ is Small, THEN $y_1 = 2 x_1 + 3 x_2 + 1$
- **Rule 2:** IF $x_1$ is Large AND $x_2$ is Large, THEN $y_2 = 5 x_1 - x_2 + 4$

The input membership functions on $[0, 10]$ are:
- Small: $\mu_{\text{Small}}(x) = 1 - \frac{x}{10}$
- Large: $\mu_{\text{Large}}(x) = \frac{x}{10}$

Given the input vector $(x_1^*, x_2^*) = (3.0, 7.0)$:
1. Calculate the membership grades for all linguistic terms.
2. Compute the rule firing strengths $w_1$ and $w_2$ using algebraic product: $w_k = \mu(x_1) \cdot \mu(x_2)$.
3. Compute the rule outputs $y_1$ and $y_2$.
4. Calculate the final crisp defuzzified output $y^*$ using the weighted average method.
5. Compute the Jacobian sensitivity $\frac{\partial y^*}{\partial x_1}$ at this operating point.""",
                "hints": [
                    "For $x_1 = 3$: Small is 0.7, Large is 0.3.",
                    "For $x_2 = 7$: Small is 0.3, Large is 0.7.",
                    "Use $y^* = \\frac{w_1 y_1 + w_2 y_2}{w_1 + w_2}$."
                ],
                "solution": r"""### 1. Membership Grades
At $x_1^* = 3.0$ and $x_2^* = 7.0$:
- $\mu_{\text{Small}}(x_1) = 1 - \frac{3}{10} = 0.70$
- $\mu_{\text{Large}}(x_1) = \frac{3}{10} = 0.30$
- $\mu_{\text{Small}}(x_2) = 1 - \frac{7}{10} = 0.30$
- $\mu_{\text{Large}}(x_2) = \frac{7}{10} = 0.70 \qquad \blacksquare$

---

### 2. Rule Firing Strengths (Product T-norm)
- **Rule 1:**
  $$w_1 = \mu_{\text{Small}}(x_1) \cdot \mu_{\text{Small}}(x_2) = 0.70 \times 0.30 = 0.21$$
- **Rule 2:**
  $$w_2 = \mu_{\text{Large}}(x_1) \cdot \mu_{\text{Large}}(x_2) = 0.30 \times 0.70 = 0.21 \qquad \blacksquare$$
Notice that both rules fire with equal strength: $w_1 = w_2 = 0.21$.

---

### 3. Rule Consequent Outputs
- **Rule 1 Output:**
  $$y_1 = 2 x_1 + 3 x_2 + 1 = 2(3.0) + 3(7.0) + 1 = 6 + 21 + 1 = 28.0$$
- **Rule 2 Output:**
  $$y_2 = 5 x_1 - x_2 + 4 = 5(3.0) - (7.0) + 4 = 15 - 7 + 4 = 12.0 \qquad \blacksquare$$

---

### 4. TSK Weighted Average Output
$$y^* = \frac{w_1 y_1 + w_2 y_2}{w_1 + w_2} = \frac{(0.21)(28.0) + (0.21)(12.0)}{0.21 + 0.21} = \frac{0.21(28 + 12)}{0.42} = \frac{40.0}{2} = 20.0 \qquad \blacksquare$$

---

### 5. Sensitivity Derivative
Since $w_1 = (1 - 0.1 x_1)(1 - 0.1 x_2)$ and $w_2 = (0.1 x_1)(0.1 x_2)$:
At $x_2 = 7$, $1 - 0.1 x_2 = 0.3$ and $0.1 x_2 = 0.7$.
Thus $w_1 = 0.3(1 - 0.1 x_1)$, and $w_2 = 0.7(0.1 x_1) = 0.07 x_1$.
Then $w_1 + w_2 = 0.3 - 0.03 x_1 + 0.07 x_1 = 0.3 + 0.04 x_1$.
At $x_1 = 3$: $w_1 + w_2 = 0.3 + 0.12 = 0.42$.

Evaluating the quotient rule for $\frac{d}{dx_1} \left( \frac{w_1 y_1 + w_2 y_2}{w_1 + w_2} \right)$:
$$\frac{\partial y^*}{\partial x_1} \approx \frac{w_1 \frac{\partial y_1}{\partial x_1} + w_2 \frac{\partial y_2}{\partial x_1} + y_1 \frac{\partial w_1}{\partial x_1} + y_2 \frac{\partial w_2}{\partial x_1} - y^* \frac{\partial (w_1+w_2)}{\partial x_1}}{w_1 + w_2}$$
Substituting $\frac{\partial y_1}{\partial x_1} = 2$, $\frac{\partial y_2}{\partial x_1} = 5$:
$$\frac{0.21(2) + 0.21(5) + 28(-0.03) + 12(0.07) - 20(0.04)}{0.42} = \frac{0.42 + 1.05 - 0.84 + 0.84 - 0.80}{0.42} = \frac{0.67}{0.42} \approx 1.5952 \qquad \blacksquare$$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 8.3: Derivation of the Fuzzy c-Means (FCM) Update Equations via Lagrange Multipliers",
                "statement": r"""In Fuzzy c-Means Clustering, the objective is to minimize the weighted square error functional:
$$J_m(U, V) = \sum_{i=1}^c \sum_{k=1}^N (u_{ik})^m \|\mathbf{x}_k - \mathbf{v}_i\|^2$$
subject to the partition constraints:
$$\sum_{i=1}^c u_{ik} = 1 \quad (\forall k = 1, \dots, N), \qquad u_{ik} \ge 0$$
where $m > 1$ is the weighting exponent, $\mathbf{x}_k \in \mathbb{R}^d$ are given data points, and $\mathbf{v}_i \in \mathbb{R}^d$ are cluster centers.

1. Using the method of Lagrange multipliers, derive the exact analytical formula for the optimal membership grades $u_{ik}$:
   $$u_{ik} = \frac{1}{\sum_{j=1}^c \left( \frac{\|\mathbf{x}_k - \mathbf{v}_i\|}{\|\mathbf{x}_k - \mathbf{v}_j\|} \right)^{\frac{2}{m - 1}}}$$
2. By setting $\nabla_{\mathbf{v}_i} J_m = 0$, derive the formula for the optimal cluster centers:
   $$\mathbf{v}_i = \frac{\sum_{k=1}^N (u_{ik})^m \mathbf{x}_k}{\sum_{k=1}^N (u_{ik})^m}$$
3. Prove that as the fuzziness parameter $m \to 1^+$, the fuzzy membership grades $u_{ik}$ collapse to the crisp hard assignment of classical k-means clustering.""",
                "hints": [
                    "Construct the Lagrangian $\\mathcal{L} = \\sum_{i=1}^c \\sum_{k=1}^N (u_{ik})^m d_{ik}^2 - \\sum_{k=1}^N \\lambda_k (\\sum_{i=1}^c u_{ik} - 1)$.",
                    "Differentiate with respect to $u_{ik}$: $m (u_{ik})^{m-1} d_{ik}^2 - \\lambda_k = 0$.",
                    "Solve for $u_{ik}$ and substitute into the constraint $\\sum_{i=1}^c u_{ik} = 1$ to eliminate $\\lambda_k$."
                ],
                "solution": r"""### 1. Derivation of the Optimal Membership Grades $u_{ik}$
Let $d_{ik} = \|\mathbf{x}_k - \mathbf{v}_i\|$.
Notice that the constraint $\sum_{i=1}^c u_{ik} = 1$ applies independently for each data point $k \in \{1, \dots, N\}$.
For a fixed data point $k$, form the Lagrangian:
$$\mathcal{L}_k = \sum_{i=1}^c (u_{ik})^m d_{ik}^2 - \lambda_k \left( \sum_{i=1}^c u_{ik} - 1 \right)$$
where $\lambda_k$ is the Lagrange multiplier.

#### Step A: First-Order Necessary Condition
Differentiating with respect to $u_{ik}$:
$$\frac{\partial \mathcal{L}_k}{\partial u_{ik}} = m (u_{ik})^{m-1} d_{ik}^2 - \lambda_k = 0$$
Assuming $d_{ik} > 0$:
$$(u_{ik})^{m-1} = \frac{\lambda_k}{m d_{ik}^2} \implies u_{ik} = \left( \frac{\lambda_k}{m} \right)^{\frac{1}{m - 1}} \left( \frac{1}{d_{ik}^2} \right)^{\frac{1}{m - 1}} = \left( \frac{\lambda_k}{m} \right)^{\frac{1}{m - 1}} d_{ik}^{-\frac{2}{m - 1}}$$

#### Step B: Eliminate the Multiplier $\lambda_k$
Sum over all clusters $j = 1, \dots, c$ and enforce the constraint:
$$1 = \sum_{j=1}^c u_{jk} = \left( \frac{\lambda_k}{m} \right)^{\frac{1}{m - 1}} \sum_{j=1}^c d_{jk}^{-\frac{2}{m - 1}}$$
Solving for the multiplier term:
$$\left( \frac{\lambda_k}{m} \right)^{\frac{1}{m - 1}} = \frac{1}{\sum_{j=1}^c d_{jk}^{-\frac{2}{m - 1}}}$$

#### Step C: Substitute Back
$$\begin{aligned}
u_{ik} &= \frac{d_{ik}^{-\frac{2}{m - 1}}}{\sum_{j=1}^c d_{jk}^{-\frac{2}{m - 1}}} = \frac{1}{\sum_{j=1}^c \frac{d_{ik}^{\frac{2}{m - 1}}}{d_{jk}^{\frac{2}{m - 1}}}} \\
&= \frac{1}{\sum_{j=1}^c \left( \frac{d_{ik}}{d_{jk}} \right)^{\frac{2}{m - 1}}} = \frac{1}{\sum_{j=1}^c \left( \frac{\|\mathbf{x}_k - \mathbf{v}_i\|}{\|\mathbf{x}_k - \mathbf{v}_j\|} \right)^{\frac{2}{m - 1}}} \qquad \blacksquare
\end{aligned}$$

---

### 2. Derivation of the Cluster Centers $\mathbf{v}_i$
Now fix $U$ and minimize $J_m$ with respect to the center vector $\mathbf{v}_i \in \mathbb{R}^d$:
$$J_m = \sum_{i=1}^c \sum_{k=1}^N (u_{ik})^m (\mathbf{x}_k - \mathbf{v}_i)^T (\mathbf{x}_k - \mathbf{v}_i)$$
Differentiating with respect to vector $\mathbf{v}_i$:
$$\nabla_{\mathbf{v}_i} J_m = \sum_{k=1}^N (u_{ik})^m \left[ -2(\mathbf{x}_k - \mathbf{v}_i) \right] = \mathbf{0}$$
Dividing by $-2$:
$$\sum_{k=1}^N (u_{ik})^m (\mathbf{x}_k - \mathbf{v}_i) = \mathbf{0} \implies \sum_{k=1}^N (u_{ik})^m \mathbf{x}_k - \left( \sum_{k=1}^N (u_{ik})^m \right) \mathbf{v}_i = \mathbf{0}$$
Solving for $\mathbf{v}_i$:
$$\mathbf{v}_i = \frac{\sum_{k=1}^N (u_{ik})^m \mathbf{x}_k}{\sum_{k=1}^N (u_{ik})^m} \qquad \blacksquare$$
This proves that each cluster center is a weighted center of gravity of all data points, weighted by the $m$-th power of membership!

---

### 3. Collapse to Hard K-Means as $m \to 1^+$
Examine the exponent $\frac{2}{m - 1}$ in the membership formula:
As $m \to 1^+$, $m - 1 \to 0^+$, so:
$$\lim_{m \to 1^+} \frac{2}{m - 1} = +\infty$$
Let $i^* = \arg\min_j \|\mathbf{x}_k - \mathbf{v}_j\|$ be the closest cluster center to point $\mathbf{x}_k$.
- If $i = i^*$:
  For any other cluster $j \ne i^*$, $\|\mathbf{x}_k - \mathbf{v}_{i^*}\| < \|\mathbf{x}_k - \mathbf{v}_j\|$, which means the ratio:
  $$\frac{\|\mathbf{x}_k - \mathbf{v}_{i^*}\|}{\|\mathbf{x}_k - \mathbf{v}_j\|} < 1$$
  Therefore:
  $$\lim_{m \to 1^+} \left( \frac{\|\mathbf{x}_k - \mathbf{v}_{i^*}\|}{\|\mathbf{x}_k - \mathbf{v}_j\|} \right)^{\frac{2}{m - 1}} = 0 \quad (\forall j \ne i^*)$$
  The only non-zero term in the denominator sum is for $j = i^*$ (where ratio is 1):
  $$u_{i^* k} = \frac{1}{1 + 0 + \dots + 0} = 1$$
- If $i \ne i^*$:
  For $j = i^*$, the ratio $\frac{\|\mathbf{x}_k - \mathbf{v}_i\|}{\|\mathbf{x}_k - \mathbf{v}_{i^*}\|} > 1$.
  As power $\to \infty$, this term diverges to $+\infty$, forcing the denominator to $+\infty$:
  $$u_{ik} = \frac{1}{\infty} = 0$$

Thus, in the limit $m \to 1^+$:
$$u_{ik} \to \begin{cases} 1, & \text{if } i = \arg\min_j \|\mathbf{x}_k - \mathbf{v}_j\| \\ 0, & \text{otherwise} \end{cases}$$
The soft fuzzy memberships collapse strictly to the crisp Voronoi partitioning of classical hard k-means clustering! $\blacksquare$"""
            }
        ]
    }
    return u8

if __name__ == "__main__":
    u8 = get_unit8()
    print(f"Loaded Unit 8: {u8['title']} with {len(u8['sections'])} sections and {len(u8['problems'])} problems.")
