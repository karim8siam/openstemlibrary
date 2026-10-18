# -*- coding: utf-8 -*-
"""
build_fuzzy_unit4.py
Constructs Unit 4: Fuzzy Numbers, Intervals & Linguistic Variables
Strictly ZERO course numbers.
"""

def get_unit4():
    u4 = {
        "number": 4,
        "title": "Fuzzy Numbers, Intervals & Linguistic Variables",
        "leadSummary": "Rigorous theory of fuzzy numbers and intervals on the real line: axiomatic characterization of fuzzy numbers (normality, fuzzy convexity, upper semicontinuity, compact bounded support), interval analysis [a, b] as 0-level fuzzy arithmetic, parameterization of Triangular Fuzzy Numbers (TFN) and Trapezoidal Fuzzy Numbers (TrFN), linguistic variables (name, term set, universe, syntactic rules, semantic rules), linguistic hedges (concentrators, dilators, intensifiers), the lattice of fuzzy numbers, and fuzzy ranking / defuzzification methods (Centroid, First of Maxima, Middle of Maxima).",
        "simulations": ["sim_fuzzy_number_arithmetic"],
        "sections": [
            {
                "secNumber": "4.1",
                "title": "Axiomatic Definition of Fuzzy Numbers (Convexity, Normality, Compact Upper Semicontinuity)",
                "content": r"""### 1. What is a Fuzzy Number?
In real analysis and practical engineering, measurement uncertainty and tolerance intervals lead naturally to concepts like *"approximately 5 volts"* or *"around 20 degrees Celsius"*.
To formalize these concepts mathematically, a fuzzy subset of the real numbers $\mathbb{R}$ must satisfy specific topological and algebraic axioms:

> **Definition 4.1 (Fuzzy Number):**
> A fuzzy set $A$ on the real line $\mathbb{R}$ is called a **fuzzy number** (or fuzzy quantity) if its membership function $\mu_A: \mathbb{R} \to [0, 1]$ satisfies all four of the following axioms:
> 1. **Normality:** $A$ is normal, meaning there exists at least one $x_0 \in \mathbb{R}$ such that $\mu_A(x_0) = 1$. (The core is non-empty).
> 2. **Fuzzy Convexity:** $A$ is fuzzy convex, meaning for all $x_1, x_2 \in \mathbb{R}$ and $\lambda \in [0, 1]$:
>    $$\mu_A(\lambda x_1 + (1 - \lambda) x_2) \ge \min(\mu_A(x_1), \mu_A(x_2))$$
>    Equivalently, every $\alpha$-cut $A_\alpha$ is a closed convex interval of $\mathbb{R}$.
> 3. **Upper Semicontinuity:** The function $\mu_A$ is upper semicontinuous, meaning for any sequence $x_n \to x$:
>    $$\limsup_{n \to \infty} \mu_A(x_n) \le \mu_A(x)$$
>    (This guarantees that every $\alpha$-cut $A_\alpha$ is topologically closed).
> 4. **Compact (Bounded) Support:** The support closure $\text{cl}(\text{Supp}(A)) = A_0$ is a bounded subset of $\mathbb{R}$.

---

### 2. Fundamental Representation via Interval Level Sets
As an immediate consequence of Definition 4.1:

> **Theorem 4.1 (Interval Representation of Fuzzy Numbers):**
> A fuzzy set $A$ is a fuzzy number if and only if for every $\alpha \in (0, 1]$, the $\alpha$-cut $A_\alpha$ is a non-empty, compact (closed and bounded) real interval:
> $$A_\alpha = [a_1(\alpha), a_2(\alpha)] \subset \mathbb{R}$$
> where:
> - $a_1(\alpha)$ is a bounded, monotonically non-decreasing, left-continuous function of $\alpha \in (0, 1]$.
> - $a_2(\alpha)$ is a bounded, monotonically non-increasing, left-continuous function of $\alpha \in (0, 1]$.
> - $a_1(1) \le a_2(1)$.
> If $a_1(1) = a_2(1) = m$, the fuzzy number has a unique modal peak $m$."""
            },
            {
                "secNumber": "4.2",
                "title": "Interval Arithmetic: Addition, Subtraction, Multiplication & Inverses of Closed Intervals",
                "content": r"""### 1. Classical Interval Analysis (Moore, 1966)
Because every $\alpha$-cut of a fuzzy number is a compact real interval, all fuzzy number operations are fundamentally rooted in **interval arithmetic**.

Let $I = [a_1, a_2]$ and $J = [b_1, b_2]$ be two closed bounded intervals in $\mathbb{R}$.
For any binary operation $* \in \{+, -, \times, /\}$, the interval operation is defined set-theoretically by:
$$I * J = \{x * y \mid x \in I, \; y \in J\}$$

---

### 2. Analytical Formulae for Interval Operations

#### 1. Interval Addition ($+$):
$$[a_1, a_2] + [b_1, b_2] = [a_1 + b_1, \; a_2 + b_2]$$
- Associative and commutative. Neutral element: $[0, 0]$.

#### 2. Interval Subtraction ($-I$ and $I - J$):
The negation of an interval is: $-[b_1, b_2] = [-b_2, -b_1]$.
Thus:
$$[a_1, a_2] - [b_1, b_2] = [a_1, a_2] + (-[b_1, b_2]) = [a_1 - b_2, \; a_2 - b_1]$$

#### 3. Interval Multiplication ($\times$):
$$[a_1, a_2] \times [b_1, b_2] = [\min(a_1 b_1, a_1 b_2, a_2 b_1, a_2 b_2), \; \max(a_1 b_1, a_1 b_2, a_2 b_1, a_2 b_2)]$$
For strictly positive intervals ($a_1, b_1 \ge 0$):
$$[a_1, a_2] \times [b_1, b_2] = [a_1 b_1, \; a_2 b_2]$$

#### 4. Interval Reciprocal and Division ($/$):
For $0 \notin [b_1, b_2]$:
$$[b_1, b_2]^{-1} = \left[ \frac{1}{b_2}, \; \frac{1}{b_1} \right]$$
$$[a_1, a_2] / [b_1, b_2] = [a_1, a_2] \times [b_1, b_2]^{-1} = \left[ \min\left(\frac{a_1}{b_2}, \frac{a_1}{b_1}, \frac{a_2}{b_2}, \frac{a_2}{b_1}\right), \; \max\left(\frac{a_1}{b_2}, \frac{a_1}{b_1}, \frac{a_2}{b_2}, \frac{a_2}{b_1}\right) \right]$$

---

### 3. The Non-Invertibility Trap of Intervals
A crucial algebraic property that distinguishes interval arithmetic from field arithmetic is that **intervals do NOT possess additive or multiplicative inverses**:
$$[a_1, a_2] - [a_1, a_2] = [a_1 - a_2, \; a_2 - a_1] \ne [0, 0] \quad (\text{unless } a_1 = a_2)$$
For example: $[2, 5] - [2, 5] = [2 - 5, 5 - 2] = [-3, 3] \ne 0$!
Subtracting an interval from itself doubles the uncertainty rather than eliminating it!"""
            },
            {
                "secNumber": "4.3",
                "title": "Triangular Fuzzy Numbers (TFN) and Trapezoidal Fuzzy Numbers (TrFN)",
                "content": r"""### 1. Triangular Fuzzy Numbers (TFN)
A **Triangular Fuzzy Number** $A = (a_1, a_2, a_3)$ is parameterized by three real numbers $a_1 \le a_2 \le a_3$:
$$\mu_A(x) = \begin{cases} 
0, & x < a_1 \\ 
\frac{x - a_1}{a_2 - a_1}, & a_1 \le x \le a_2 \\ 
\frac{a_3 - x}{a_3 - a_2}, & a_2 \le x \le a_3 \\ 
0, & x > a_3 
\end{cases}$$
- $a_1$: lower boundary (left spread start).
- $a_2$: modal value (peak / core).
- $a_3$: upper boundary (right spread end).
- $\alpha$-cut representation:
  $$A_\alpha = [a_1 + \alpha(a_2 - a_1), \; a_3 - \alpha(a_3 - a_2)]$$

---

### 2. Trapezoidal Fuzzy Numbers (TrFN)
A **Trapezoidal Fuzzy Number** $A = (a_1, a_2, a_3, a_4)$ is parameterized by four real numbers $a_1 \le a_2 \le a_3 \le a_4$:
$$\mu_A(x) = \begin{cases} 
0, & x < a_1 \\ 
\frac{x - a_1}{a_2 - a_1}, & a_1 \le x \le a_2 \\ 
1, & a_2 \le x \le a_3 \\ 
\frac{a_4 - x}{a_4 - a_3}, & a_3 \le x \le a_4 \\ 
0, & x > a_4 
\end{cases}$$
- Core: $[a_2, a_3]$ (a flat plateau interval).
- $\alpha$-cut representation:
  $$A_\alpha = [a_1 + \alpha(a_2 - a_1), \; a_4 - \alpha(a_4 - a_3)]$$
If $a_2 = a_3$, the trapezoidal fuzzy number degenerates to a triangular fuzzy number."""
            },
            {
                "secNumber": "4.4",
                "title": "Linguistic Variables, Hedges (Very, Slightly, More or Less), and Modifiers",
                "content": r"""### 1. The Concept of Linguistic Variables
In 1975, Zadeh introduced the concept of a **linguistic variable** to bridge natural human language with mathematical algorithms:

> **Definition 4.2 (Linguistic Variable):**
> A linguistic variable is characterized by a quintuple $(X, T(X), U, G, M)$:
> 1. $X$: The name of the variable (e.g. *Temperature*, *Age*, *Speed*).
> 2. $T(X)$: The term set of $X$ (the set of linguistic values, e.g. $\{ \text{Freezing}, \text{Cold}, \text{Warm}, \text{Hot} \}$).
> 3. $U$: The universe of discourse (e.g. $U = [-20^\circ\text{C}, 100^\circ\text{C}]$).
> 4. $G$: A syntactic rule (grammar) for generating new terms using linguistic hedges.
> 5. $M$: A semantic rule mapping each linguistic term $t \in T(X)$ to a fuzzy subset $M(t)$ on $U$.

---

### 2. Linguistic Hedges (Fuzzy Modifiers)
Linguistic hedges are operators that modify the shape of primary membership functions:

#### 1. Concentration (Hedge *"Very"*):
Squaring the membership grades narrows the fuzzy set:
$$\mu_{\text{Very } A}(x) = [\mu_A(x)]^2$$
For example, if $\mu_{\text{Tall}}(180\text{ cm}) = 0.8$, then $\mu_{\text{Very Tall}}(180\text{ cm}) = (0.8)^2 = 0.64$.

#### 2. Dilation (Hedge *"More or Less"* / *"Somewhat"*):
Taking the square root broadens the fuzzy set:
$$\mu_{\text{More or Less } A}(x) = [\mu_A(x)]^{1/2} = \sqrt{\mu_A(x)}$$
$\mu_{\text{More or Less Tall}}(180\text{ cm}) = \sqrt{0.8} \approx 0.894$.

#### 3. Contrast Intensification:
Increases membership for values $> 0.5$ and decreases membership for values $< 0.5$:
$$\mu_{\text{Intensify } A}(x) = \begin{cases} 2[\mu_A(x)]^2, & 0 \le \mu_A(x) \le 0.5 \\ 1 - 2[1 - \mu_A(x)]^2, & 0.5 < \mu_A(x) \le 1 \end{cases}$$"""
            },
            {
                "secNumber": "4.5",
                "title": "The Lattice $(\\mathcal{F}_N(\\mathbb{R}), \\le, \\wedge, \\vee)$ of Fuzzy Numbers & Ranking Methods",
                "content": r"""### 1. Defuzzification and Ranking of Fuzzy Numbers
In practical optimization, economics, and decision-making, one frequently needs to **rank** or order two fuzzy numbers $A$ and $B$, or convert a fuzzy number into a single crisp scalar representative (**defuzzification**).

---

### 2. Major Defuzzification Techniques

#### 1. Center of Gravity / Centroid Method (Centroid Defuzzification):
The horizontal center of mass of the membership area:
$$x^* = \text{COG}(A) = \frac{\int_{-\infty}^\infty x \, \mu_A(x) \, dx}{\int_{-\infty}^\infty \mu_A(x) \, dx}$$
For a discrete fuzzy set: $x^* = \frac{\sum x_i \mu_A(x_i)}{\sum \mu_A(x_i)}$.
For a Triangular Fuzzy Number $A = (a_1, a_2, a_3)$:
$$\text{COG}(A) = \frac{a_1 + a_2 + a_3}{3}$$

#### 2. Mean of Maxima (MOM):
The average of the elements having maximum membership grade ($\mu = 1$):
$$\text{MOM}(A) = \frac{\int_{\text{Core}(A)} x \, dx}{\int_{\text{Core}(A)} dx}$$
For a Trapezoidal Fuzzy Number $A = (a_1, a_2, a_3, a_4)$:
$$\text{MOM}(A) = \frac{a_2 + a_3}{2}$$

#### 3. First of Maxima (FOM) and Last of Maxima (LOM):
$$\text{FOM}(A) = \inf\{x \in \text{Core}(A)\}, \qquad \text{LOM}(A) = \sup\{x \in \text{Core}(A)\}$$

---

### 3. Yager's Centroid Ranking Index
To rank two fuzzy numbers $A$ and $B$, Yager (1981) introduced the ranking integral:
$$R(A) = \int_0^1 \frac{a_1(\alpha) + a_2(\alpha)}{2} \, d\alpha$$
Then $A < B \iff R(A) < R(B)$, and $A \approx B \iff R(A) = R(B)$.
This index computes the mean centroid position of all $\alpha$-cut midpoints across the full spectrum $\alpha \in [0, 1]$."""
            }
        ],
        "problems": [
            {
                "tier": "Fundamentals",
                "title": "Problem 4.1: Interval Arithmetic Operations on Closed Intervals",
                "statement": r"""Let $I = [3, 7]$ and $J = [2, 5]$ be two closed bounded intervals in $\mathbb{R}$.
1. Compute the interval sum $I + J$.
2. Compute the interval difference $I - J$.
3. Compute the interval product $I \times J$.
4. Compute the interval quotient $I / J$.
5. Evaluate $I - I$ and explain why it is NOT equal to the zero interval $[0, 0]$.""",
                "hints": [
                    "Recall $[a_1, a_2] - [b_1, b_2] = [a_1 - b_2, a_2 - b_1]$.",
                    "For positive intervals, $[a_1, a_2] \\times [b_1, b_2] = [a_1 b_1, a_2 b_2]$.",
                    "For quotient: $[a_1, a_2] / [b_1, b_2] = [a_1 / b_2, a_2 / b_1]$."
                ],
                "solution": r"""### 1. Interval Sum $I + J$
$$I + J = [3, 7] + [2, 5] = [3 + 2, \; 7 + 5] = [5, 12] \qquad \blacksquare$$

---

### 2. Interval Difference $I - J$
$$I - J = [3, 7] - [2, 5] = [3 - 5, \; 7 - 2] = [-2, 5] \qquad \blacksquare$$

---

### 3. Interval Product $I \times J$
Since all endpoints are strictly positive:
$$I \times J = [3, 7] \times [2, 5] = [3 \times 2, \; 7 \times 5] = [6, 35] \qquad \blacksquare$$

---

### 4. Interval Quotient $I / J$
Since $0 \notin [2, 5]$:
$$J^{-1} = [2, 5]^{-1} = \left[ \frac{1}{5}, \; \frac{1}{2} \right]$$
$$I / J = [3, 7] \times \left[ \frac{1}{5}, \; \frac{1}{2} \right] = \left[ 3 \times \frac{1}{5}, \; 7 \times \frac{1}{2} \right] = \left[ \frac{3}{5}, \; \frac{7}{2} \right] = [0.6, 3.5] \qquad \blacksquare$$

---

### 5. Self-Difference $I - I$
$$I - I = [3, 7] - [3, 7] = [3 - 7, \; 7 - 3] = [-4, 4] \ne [0, 0]$$
#### Explanation:
In interval analysis, elements $x \in I$ and $y \in I$ are chosen **independently**.
The operation $I - I = \{x - y \mid x \in [3, 7], y \in [3, 7]\}$.
When $x = 3$ (minimum) and $y = 7$ (maximum), $x - y = -4$.
When $x = 7$ (maximum) and $y = 3$ (minimum), $x - y = +4$.
Because the two instances of $I$ are not bound to take identical values simultaneously, the uncertainty intervals accumulate rather than canceling. This proves intervals lack an additive inverse. $\blacksquare$"""
            },
            {
                "tier": "Computational Triad",
                "title": "Problem 4.2: Defuzzification Comparison for a Trapezoidal Fuzzy Number",
                "statement": r"""Consider a Trapezoidal Fuzzy Number $A = (2, 5, 8, 12)$ representing a linguistic variable.
1. Determine the exact $\alpha$-cut representation $A_\alpha = [a_1(\alpha), a_2(\alpha)]$.
2. Compute the defuzzified value using the **Centroid (Center of Gravity)** method:
   $$\text{COG}(A) = \frac{\int_2^{12} x \, \mu_A(x) \, dx}{\int_2^{12} \mu_A(x) \, dx}$$
3. Compute the **Mean of Maxima (MOM)** defuzzification.
4. Compute the **First of Maxima (FOM)** and **Last of Maxima (LOM)** values.
5. Compute Yager's ranking index $R(A) = \int_0^1 \frac{a_1(\alpha) + a_2(\alpha)}{2} \, d\alpha$ and compare with COG.""",
                "hints": [
                    "For trapezoid with parameters $(a, b, c, d)$, area is $\\frac{1}{2}( (c - b) + (d - a) )$.",
                    "For centroid of trapezoid: $x^* = \\frac{1}{3} \\frac{d^2 + c^2 + cd - a^2 - b^2 - ab}{(d + c - a - b)}$.",
                    "MOM is $(b + c)/2$."
                ],
                "solution": r"""### 1. $\alpha$-Cut Representation
- Left branch ($2 \le x \le 5$): $\frac{x - 2}{5 - 2} = \frac{x - 2}{3} = \alpha \implies a_1(\alpha) = 2 + 3\alpha$.
- Right branch ($8 \le x \le 12$): $\frac{12 - x}{12 - 8} = \frac{12 - x}{4} = \alpha \implies a_2(\alpha) = 12 - 4\alpha$.
Thus:
$$A_\alpha = [2 + 3\alpha, \; 12 - 4\alpha] \qquad \blacksquare$$

---

### 2. Centroid (COG) Method
Break the area and first moments into three geometric parts:
1. Left triangle: $x \in [2, 5]$, base $b_1 = 3$, height $h = 1$.
   Area $A_1 = \frac{1}{2}(3)(1) = 1.5$. Centroid $\bar{x}_1 = 2 + \frac{2}{3}(3) = 4.0$.
2. Center rectangle: $x \in [5, 8]$, base $b_2 = 3$, height $h = 1$.
   Area $A_2 = 3 \times 1 = 3.0$. Centroid $\bar{x}_2 = \frac{5 + 8}{2} = 6.5$.
3. Right triangle: $x \in [8, 12]$, base $b_3 = 4$, height $h = 1$.
   Area $A_3 = \frac{1}{2}(4)(1) = 2.0$. Centroid $\bar{x}_3 = 8 + \frac{1}{3}(4) = \frac{28}{3} \approx 9.3333$.

Total Area:
$$A_{\text{total}} = 1.5 + 3.0 + 2.0 = 6.5$$
Total First Moment:
$$M = A_1 \bar{x}_1 + A_2 \bar{x}_2 + A_3 \bar{x}_3 = (1.5)(4.0) + (3.0)(6.5) + (2.0)\left(\frac{28}{3}\right) = 6.0 + 19.5 + 18.6667 = 44.1667$$
Centroid:
$$\text{COG}(A) = \frac{M}{A_{\text{total}}} = \frac{44.1667}{6.5} \approx 6.7949 \qquad \blacksquare$$

---

### 3. Mean of Maxima (MOM)
The core of $A$ is the interval $[5, 8]$.
$$\text{MOM}(A) = \frac{5 + 8}{2} = 6.5 \qquad \blacksquare$$

---

### 4. FOM and LOM
- $\text{FOM}(A) = \inf[5, 8] = 5.0$
- $\text{LOM}(A) = \sup[5, 8] = 8.0 \qquad \blacksquare$

---

### 5. Yager's Ranking Index $R(A)$
Using the $\alpha$-cut endpoints $a_1(\alpha) = 2 + 3\alpha$ and $a_2(\alpha) = 12 - 4\alpha$:
$$\frac{a_1(\alpha) + a_2(\alpha)}{2} = \frac{(2 + 3\alpha) + (12 - 4\alpha)}{2} = \frac{14 - \alpha}{2} = 7 - 0.5\alpha$$
Integrating from $\alpha = 0$ to $1$:
$$R(A) = \int_0^1 (7 - 0.5\alpha) \, d\alpha = \left[ 7\alpha - 0.25\alpha^2 \right]_0^1 = 7 - 0.25 = 6.75 \qquad \blacksquare$$
Notice that $R(A) = 6.75$ is very close to $\text{COG}(A) \approx 6.7949$!"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 4.3: Proof that Centroid of Any Triangular Fuzzy Number is $(a_1 + a_2 + a_3)/3$",
                "statement": r"""Let $A = (a_1, a_2, a_3)$ be an arbitrary Triangular Fuzzy Number with $a_1 < a_2 < a_3$.
1. Using integration of the piecewise linear membership function:
   $$\text{COG}(A) = \frac{\int_{a_1}^{a_3} x \, \mu_A(x) \, dx}{\int_{a_1}^{a_3} \mu_A(x) \, dx}$$
   prove rigorously from first principles that:
   $$\text{COG}(A) = \frac{a_1 + a_2 + a_3}{3}$$
2. Prove that Yager's ranking index $R(A) = \int_0^1 \frac{a_1(\alpha) + a_2(\alpha)}{2} \, d\alpha$ yields:
   $$R(A) = \frac{a_1 + 2a_2 + a_3}{4}$$
3. Contrast the weights assigned to the mode $a_2$ by COG ($1/3 \approx 0.333$) versus Yager ($2/4 = 0.5$).""",
                "hints": [
                    "Total area of a triangle of base $(a_3 - a_1)$ and height 1 is $\\frac{1}{2}(a_3 - a_1)$.",
                    "Use integration by substitution $u = x - a_1$ and $v = a_3 - x$.",
                    "For Yager, integrate $a_1(\\alpha) = a_1 + \\alpha(a_2 - a_1)$ and $a_2(\\alpha) = a_3 - \\alpha(a_3 - a_2)$."
                ],
                "solution": r"""### 1. Proof of the Centroid Formula $\text{COG}(A) = \frac{a_1 + a_2 + a_3}{3}$

#### Step A: Denominator (Total Area)
The graph of $\mu_A(x)$ is a triangle with base $a_3 - a_1$ and height 1.
The area is:
$$A_{\text{total}} = \int_{a_1}^{a_3} \mu_A(x) \, dx = \frac{1}{2} (a_3 - a_1) \cdot 1 = \frac{a_3 - a_1}{2}$$

#### Step B: Numerator (First Moment of Area)
$$M = \int_{a_1}^{a_3} x \, \mu_A(x) \, dx = \int_{a_1}^{a_2} x \left( \frac{x - a_1}{a_2 - a_1} \right) dx + \int_{a_2}^{a_3} x \left( \frac{a_3 - x}{a_3 - a_2} \right) dx$$

##### Integral 1: Left Branch
Let $u = x - a_1 \implies x = u + a_1$, $dx = du$. As $x: a_1 \to a_2$, $u: 0 \to (a_2 - a_1) = L_1$:
$$\begin{aligned}
I_1 &= \frac{1}{L_1} \int_0^{L_1} (u + a_1) u \, du = \frac{1}{L_1} \int_0^{L_1} (u^2 + a_1 u) \, du \\
&= \frac{1}{L_1} \left[ \frac{L_1^3}{3} + a_1 \frac{L_1^2}{2} \right] = \frac{L_1^2}{3} + \frac{a_1 L_1}{2} = L_1 \left( \frac{a_2 - a_1}{3} + \frac{a_1}{2} \right) \\
&= (a_2 - a_1) \left( \frac{2a_2 + a_1}{6} \right) = \frac{(a_2 - a_1)(a_1 + 2a_2)}{6}
\end{aligned}$$

##### Integral 2: Right Branch
Let $v = a_3 - x \implies x = a_3 - v$, $dx = -dv$. As $x: a_2 \to a_3$, $v: (a_3 - a_2) = L_2 \to 0$:
$$\begin{aligned}
I_2 &= \frac{1}{L_2} \int_0^{L_2} (a_3 - v) v \, dv = \frac{1}{L_2} \int_0^{L_2} (a_3 v - v^2) \, dv \\
&= \frac{1}{L_2} \left[ a_3 \frac{L_2^2}{2} - \frac{L_2^3}{3} \right] = \frac{a_3 L_2}{2} - \frac{L_2^2}{3} = L_2 \left( \frac{a_3}{2} - \frac{a_3 - a_2}{3} \right) \\
&= (a_3 - a_2) \left( \frac{a_3 + 2a_2}{6} \right) = \frac{(a_3 - a_2)(2a_2 + a_3)}{6}
\end{aligned}$$

##### Sum of Moments:
$$\begin{aligned}
M = I_1 + I_2 &= \frac{1}{6} \left[ (a_2 - a_1)(a_1 + 2a_2) + (a_3 - a_2)(2a_2 + a_3) \right] \\
&= \frac{1}{6} \left[ a_1 a_2 + 2a_2^2 - a_1^2 - 2a_1 a_2 + 2a_2 a_3 + a_3^2 - 2a_2^2 - a_2 a_3 \right] \\
&= \frac{1}{6} \left[ a_3^2 - a_1^2 + a_2 a_3 - a_1 a_2 \right] \\
&= \frac{1}{6} \left[ (a_3 - a_1)(a_3 + a_1) + a_2(a_3 - a_1) \right] \\
&= \frac{a_3 - a_1}{6} \left( a_1 + a_2 + a_3 \right)
\end{aligned}$$

#### Step C: Ratio
$$\text{COG}(A) = \frac{M}{A_{\text{total}}} = \frac{\frac{a_3 - a_1}{6} (a_1 + a_2 + a_3)}{\frac{a_3 - a_1}{2}} = \frac{a_1 + a_2 + a_3}{3} \qquad \blacksquare$$

---

### 2. Derivation of Yager's Ranking Index $R(A)$
$\alpha$-cut endpoints are:
$$a_1(\alpha) = a_1 + \alpha(a_2 - a_1), \qquad a_2(\alpha) = a_3 - \alpha(a_3 - a_2)$$
Midpoint:
$$\frac{a_1(\alpha) + a_2(\alpha)}{2} = \frac{a_1 + a_3 + \alpha(2a_2 - a_1 - a_3)}{2}$$
Integrating with respect to $\alpha \in [0, 1]$:
$$\begin{aligned}
R(A) &= \int_0^1 \left[ \frac{a_1 + a_3}{2} + \alpha \frac{2a_2 - a_1 - a_3}{2} \right] d\alpha \\
&= \frac{a_1 + a_3}{2} + \left[ \frac{\alpha^2}{2} \right]_0^1 \frac{2a_2 - a_1 - a_3}{2} \\
&= \frac{a_1 + a_3}{2} + \frac{2a_2 - a_1 - a_3}{4} \\
&= \frac{2a_1 + 2a_3 + 2a_2 - a_1 - a_3}{4} \\
&= \frac{a_1 + 2a_2 + a_3}{4} \qquad \blacksquare
\end{aligned}$$

---

### 3. Comparison of Weightings
- In the geometric Centroid ($\text{COG}$), all three vertices contribute with equal weights: $(1/3, 1/3, 1/3)$.
- In Yager's level-cut ranking index ($R$), the weights are $(1/4, 2/4, 1/4) = (0.25, 0.50, 0.25)$.
Yager's index places twice as much weight on the modal core $a_2$ (the most certain value with $\mu = 1$) as on either endpoint, which aligns naturally with decision-maker confidence in the most possible value! $\blacksquare$"""
            }
        ]
    }
    return u4

if __name__ == "__main__":
    u4 = get_unit4()
    print(f"Loaded Unit 4: {u4['title']} with {len(u4['sections'])} sections and {len(u4['problems'])} problems.")
