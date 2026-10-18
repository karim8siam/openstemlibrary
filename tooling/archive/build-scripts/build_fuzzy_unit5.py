# -*- coding: utf-8 -*-
"""
build_fuzzy_unit5.py
Constructs Unit 5: Fuzzy Arithmetic & Solution of Fuzzy Equations
Strictly ZERO course numbers.
"""

def get_unit5():
    u5 = {
        "number": 5,
        "title": "Fuzzy Arithmetic & Solution of Fuzzy Equations",
        "leadSummary": "Comprehensive theory of arithmetic on fuzzy numbers and the solution of fuzzy algebraic equations: addition, subtraction, multiplication, and division defined through Zadeh's Extension Principle and verified through interval α-cuts, shape alterations (e.g. non-triangular product of two TFNs), MIN and MAX operations on fuzzy numbers, the fundamental non-invertibility problem (why B - A does NOT solve A + X = B), solvability criteria and closed-form solutions for linear fuzzy equations A + X = B and multiplicative equations A · X = B.",
        "simulations": ["sim_fuzzy_equations_solver"],
        "sections": [
            {
                "secNumber": "5.1",
                "title": "Addition and Subtraction of Fuzzy Numbers via the Extension Principle & $\\alpha$-Cuts",
                "content": r"""### 1. Addition of Fuzzy Numbers ($A + B$)
Let $A$ and $B$ be two fuzzy numbers on $\mathbb{R}$.
By Zadeh's Extension Principle, their sum $C = A + B$ has membership function:
$$\mu_{A + B}(z) = \sup_{z = x + y} \min(\mu_A(x), \mu_B(y))$$

#### Verification via $\alpha$-Cuts:
For every $\alpha \in (0, 1]$, let $A_\alpha = [a_1(\alpha), a_2(\alpha)]$ and $B_\alpha = [b_1(\alpha), b_2(\alpha)]$.
By Nguyen's theorem:
$$[A + B]_\alpha = A_\alpha + B_\alpha = [a_1(\alpha) + b_1(\alpha), \; a_2(\alpha) + b_2(\alpha)]$$

#### Addition of Triangular Fuzzy Numbers (TFNs):
If $A = (a_1, a_2, a_3)$ and $B = (b_1, b_2, b_3)$ are TFNs:
$$a_1(\alpha) + b_1(\alpha) = (a_1 + b_1) + \alpha[(a_2 + b_2) - (a_1 + b_1)]$$
$$a_2(\alpha) + b_2(\alpha) = (a_3 + b_3) - \alpha[(a_3 + b_3) - (a_2 + b_2)]$$
Both endpoints remain linear in $\alpha$. Therefore:
> **Theorem 5.1 (TFN Addition):**
> The sum of two Triangular Fuzzy Numbers is **strictly a Triangular Fuzzy Number**:
> $$(a_1, a_2, a_3) + (b_1, b_2, b_3) = (a_1 + b_1, \; a_2 + b_2, \; a_3 + b_3)$$

---

### 2. Subtraction of Fuzzy Numbers ($A - B$)
By the Extension Principle, $C = A - B$ has membership function:
$$\mu_{A - B}(z) = \sup_{z = x - y} \min(\mu_A(x), \mu_B(y))$$
In terms of $\alpha$-cuts:
$$[A - B]_\alpha = A_\alpha - B_\alpha = [a_1(\alpha) - b_2(\alpha), \; a_2(\alpha) - b_1(\alpha)]$$

#### Subtraction of TFNs:
For $A = (a_1, a_2, a_3)$ and $B = (b_1, b_2, b_3)$:
$$[A - B]_\alpha = [(a_1 + \alpha(a_2 - a_1)) - (b_3 - \alpha(b_3 - b_2)), \; (a_3 - \alpha(a_3 - a_2)) - (b_1 + \alpha(b_2 - b_1))]$$
$$= [(a_1 - b_3) + \alpha((a_2 - b_2) - (a_1 - b_3)), \; (a_3 - b_1) - \alpha((a_3 - b_1) - (a_2 - b_2))]$$
Therefore:
> **Theorem 5.2 (TFN Subtraction):**
> $$(a_1, a_2, a_3) - (b_1, b_2, b_3) = (a_1 - b_3, \; a_2 - b_2, \; a_3 - b_1)$$
> Notice that the left bound is $a_1 - b_3$ and the right bound is $a_3 - b_1$!"""
            },
            {
                "secNumber": "5.2",
                "title": "Multiplication, Division, Reciprocals and Extreme Bounds",
                "content": r"""### 1. Multiplication of Fuzzy Numbers ($A \cdot B$)
By the Extension Principle:
$$\mu_{A \cdot B}(z) = \sup_{z = x \cdot y} \min(\mu_A(x), \mu_B(y))$$
In terms of $\alpha$-cuts, for positive fuzzy numbers ($A_\alpha, B_\alpha > 0$):
$$[A \cdot B]_\alpha = [a_1(\alpha) \cdot b_1(\alpha), \; a_2(\alpha) \cdot b_2(\alpha)]$$

#### The Quadratic Shape Distortion:
For two TFNs $A = (a_1, a_2, a_3)$ and $B = (b_1, b_2, b_3)$ with positive vertices:
$$a_1(\alpha) \cdot b_1(\alpha) = (a_1 + \alpha(a_2 - a_1))(b_1 + \alpha(b_2 - b_1))$$
This expression contains a **quadratic term in $\alpha$** ($\alpha^2$)!
Consequently:
> **Crucial Observation:**
> The product of two Triangular Fuzzy Numbers is **NOT a Triangular Fuzzy Number**! Its left and right membership branches become non-linear (parabolic curves).
> However, for practical approximations, engineers often approximate the product as a TFN: $(a_1 b_1, a_2 b_2, a_3 b_3)$.

---

### 2. Reciprocal and Division ($A / B$)
For a strictly positive fuzzy number $B$ ($b_1 > 0$):
$$[B^{-1}]_\alpha = \left[ \frac{1}{b_2(\alpha)}, \; \frac{1}{b_1(\alpha)} \right] = \left[ \frac{1}{b_3 - \alpha(b_3 - b_2)}, \; \frac{1}{b_1 + \alpha(b_2 - b_1)} \right]$$
Then the division $A / B = A \cdot B^{-1}$ on $\alpha$-cuts is:
$$[A / B]_\alpha = \left[ \frac{a_1(\alpha)}{b_2(\alpha)}, \; \frac{a_2(\alpha)}{b_1(\alpha)} \right] = \left[ \frac{a_1 + \alpha(a_2 - a_1)}{b_3 - \alpha(b_3 - b_2)}, \; \frac{a_3 - \alpha(a_3 - a_2)}{b_1 + \alpha(b_2 - b_1)} \right]$$
The branches of $A / B$ are rational functions of $\alpha$, exhibiting hyperbolic curvature."""
            },
            {
                "secNumber": "5.3",
                "title": "Min and Max Operations on Fuzzy Numbers",
                "content": r"""### 1. Extended Min and Max
Beyond standard arithmetic, one can apply the Extension Principle to the crisp binary functions $\min(x, y)$ and $\max(x, y)$.

Let $A$ and $B$ be fuzzy numbers. We define:
$$\text{MIN}(A, B)(z) = \sup_{z = \min(x, y)} \min(\mu_A(x), \mu_B(y))$$
$$\text{MAX}(A, B)(z) = \sup_{z = \max(x, y)} \min(\mu_A(x), \mu_B(y))$$

---

### 2. $\alpha$-Cut Characterization
For any intervals $I = [a_1, a_2]$ and $J = [b_1, b_2]$:
$$\min([a_1, a_2], [b_1, b_2]) = [\min(a_1, b_1), \; \min(a_2, b_2)]$$
$$\max([a_1, a_2], [b_1, b_2]) = [\max(a_1, b_1), \; \max(a_2, b_2)]$$
Therefore:
$$[\text{MIN}(A, B)]_\alpha = [\min(a_1(\alpha), b_1(\alpha)), \; \min(a_2(\alpha), b_2(\alpha))]$$
$$[\text{MAX}(A, B)]_\alpha = [\max(a_1(\alpha), b_1(\alpha)), \; \max(a_2(\alpha), b_2(\alpha))]$$

Both $\text{MIN}(A, B)$ and $\text{MAX}(A, B)$ are valid fuzzy numbers.
Together with the fuzzy number ordering $A \le B \iff a_1(\alpha) \le b_1(\alpha) \text{ and } a_2(\alpha) \le b_2(\alpha)$, the set of fuzzy numbers forms a **distributive lattice**."""
            },
            {
                "secNumber": "5.4",
                "title": "Linear Fuzzy Equations: Solving $A + X = B$ and Non-Invertibility of Fuzzy Subtraction",
                "content": r"""### 1. The Fundamental Problem of Fuzzy Equations
Consider the simple linear algebraic equation where $A$ and $B$ are known fuzzy numbers, and $X$ is an unknown fuzzy number to be determined:
$$A + X = B$$
In classical algebra, one simply subtracts $A$ from both sides: $X = B - A$.
**In fuzzy mathematics, setting $X = B - A$ generally FAILS to solve $A + X = B$!**

#### Why $B - A$ Fails:
Compute $A + (B - A)$:
$$[A + (B - A)]_\alpha = A_\alpha + (B_\alpha - A_\alpha) = [a_1, a_2] + [b_1 - a_2, b_2 - a_1] = [b_1 - (a_2 - a_1), \; b_2 + (a_2 - a_1)]$$
The width of $A + (B - A)$ is $(b_2 - b_1) + 2(a_2 - a_1)$, which is strictly wider than $B_\alpha$!
Thus $A + (B - A) \ne B$ whenever $A$ is non-crisp.

---

### 2. Exact Solvability Criterion for $A + X = B$

> **Theorem 5.3 (Solvability of Linear Fuzzy Equation $A + X = B$):**
> Let $A$ and $B$ be fuzzy numbers with $\alpha$-cuts $A_\alpha = [a_1(\alpha), a_2(\alpha)]$ and $B_\alpha = [b_1(\alpha), b_2(\alpha)]$.
> The equation $A + X = B$ has an exact fuzzy number solution $X$ if and only if:
> 1. For all $\alpha \in (0, 1]$, $x_1(\alpha) \equiv b_1(\alpha) - a_1(\alpha)$ is non-decreasing in $\alpha$.
> 2. For all $\alpha \in (0, 1]$, $x_2(\alpha) \equiv b_2(\alpha) - a_2(\alpha)$ is non-increasing in $\alpha$.
> 3. $x_1(1) \le x_2(1)$.
>
> In terms of spreads (uncertainty widths $\Delta A_\alpha = a_2(\alpha) - a_1(\alpha)$ and $\Delta B_\alpha = b_2(\alpha) - b_1(\alpha)$):
> An exact solution exists if and only if **the uncertainty of $B$ is greater than or equal to the uncertainty of $A$ at every level**:
> $$\Delta B_\alpha \ge \Delta A_\alpha \quad (\forall \alpha \in [0, 1])$$
> When this condition holds, the unique solution $X$ has $\alpha$-cuts:
> $$X_\alpha = [b_1(\alpha) - a_1(\alpha), \; b_2(\alpha) - a_2(\alpha)]$$

For Triangular Fuzzy Numbers $A = (a_1, a_2, a_3)$ and $B = (b_1, b_2, b_3)$:
The candidate solution is $X = (b_1 - a_1, \; b_2 - a_2, \; b_3 - a_3)$.
It is a valid TFN if and only if:
$$b_1 - a_1 \le b_2 - a_2 \le b_3 - a_3 \iff b_2 - b_1 \ge a_2 - a_1 \text{ and } b_3 - b_2 \ge a_3 - a_2$$"""
            },
            {
                "secNumber": "5.5",
                "title": "Solving $A \\cdot X = B$ and Non-Linear Fuzzy Algebraic Systems",
                "content": r"""### 1. Multiplicative Fuzzy Equations ($A \cdot X = B$)
Consider the multiplicative equation for strictly positive fuzzy numbers $A, B > 0$:
$$A \cdot X = B$$
In terms of $\alpha$-cuts:
$[A \cdot X]_\alpha = [a_1(\alpha) x_1(\alpha), \; a_2(\alpha) x_2(\alpha)] = [b_1(\alpha), \; b_2(\alpha)]$

> **Theorem 5.4 (Solvability of Multiplicative Equation $A \cdot X = B$):**
> For strictly positive fuzzy numbers $A, B$, the equation $A \cdot X = B$ possesses an exact fuzzy number solution $X$ if and only if:
> 1. $x_1(\alpha) = \frac{b_1(\alpha)}{a_1(\alpha)}$ is non-decreasing with $\alpha \in (0, 1]$.
> 2. $x_2(\alpha) = \frac{b_2(\alpha)}{a_2(\alpha)}$ is non-increasing with $\alpha \in (0, 1]$.
> 3. $x_1(1) \le x_2(1)$.
> When these conditions hold, the unique solution is given by:
> $$X_\alpha = \left[ \frac{b_1(\alpha)}{a_1(\alpha)}, \; \frac{b_2(\alpha)}{a_2(\alpha)} \right]$$

---

### 2. Fuzzy Polynomial Equations
For general equations such as $A X^2 + B X = C$, solutions are obtained by solving the coupled non-linear interval equations at each $\alpha$-cut level:
$$a_1(\alpha) [x_1(\alpha)]^2 + b_1(\alpha) x_1(\alpha) = c_1(\alpha)$$
$$a_2(\alpha) [x_2(\alpha)]^2 + b_2(\alpha) x_2(\alpha) = c_2(\alpha)$$
and verifying monotonicity to ensure the resulting family of intervals $[x_1(\alpha), x_2(\alpha)]$ defines a legitimate fuzzy number."""
            }
        ],
        "problems": [
            {
                "tier": "Fundamentals",
                "title": "Problem 5.1: Addition and Subtraction of Triangular Fuzzy Numbers",
                "statement": r"""Let $A = (2, 5, 8)$ and $B = (3, 6, 10)$ be two Triangular Fuzzy Numbers.
1. Compute the sum $C = A + B$. Determine its parameters and verify its modal core and support.
2. Compute the difference $D = A - B$. Determine its parameters, modal core, and support.
3. Compute $E = A - A$. Explain why $E \ne 0$ and state its modal value and support.""",
                "hints": [
                    "$(a_1, a_2, a_3) + (b_1, b_2, b_3) = (a_1 + b_1, a_2 + b_2, a_3 + b_3)$.",
                    "$(a_1, a_2, a_3) - (b_1, b_2, b_3) = (a_1 - b_3, a_2 - b_2, a_3 - b_1)$.",
                    "For $A - A$, evaluate $(a_1 - a_3, a_2 - a_2, a_3 - a_1)$."
                ],
                "solution": r"""### 1. Fuzzy Addition $C = A + B$
$$A = (2, 5, 8), \qquad B = (3, 6, 10)$$
Using Theorem 5.1:
$$C = (2 + 3, \; 5 + 6, \; 8 + 10) = (5, 11, 18) \qquad \blacksquare$$
- **Core:** $\{11\}$
- **Support:** $(5, 18)$
- **Spread:** $18 - 5 = 13$ (which equals $(8 - 2) + (10 - 3) = 6 + 7 = 13$).

---

### 2. Fuzzy Subtraction $D = A - B$
Using Theorem 5.2:
$$D = (a_1 - b_3, \; a_2 - b_2, \; a_3 - b_1) = (2 - 10, \; 5 - 6, \; 8 - 3) = (-8, -1, 5) \qquad \blacksquare$$
- **Core:** $\{-1\}$
- **Support:** $(-8, 5)$
- **Spread:** $5 - (-8) = 13$.

---

### 3. Self-Difference $E = A - A$
$$E = (a_1 - a_3, \; a_2 - a_2, \; a_3 - a_1) = (2 - 8, \; 5 - 5, \; 8 - 2) = (-6, 0, 6) \qquad \blacksquare$$
- **Modal value (Core):** $\{0\}$.
- **Support:** $(-6, 6)$.
- **Explanation:** Although the peak is centered at 0, the support $(-6, 6)$ has non-zero width because subtracting independent uncertainties doubles the span. This proves $A - A \ne 0$. $\blacksquare$"""
            },
            {
                "tier": "Computational Triad",
                "title": "Problem 5.2: Solvability of Linear Fuzzy Equations $A + X = B$",
                "statement": r"""Consider the linear fuzzy equation $A + X = B$.
Let $A = (1, 3, 5)$ be a Triangular Fuzzy Number.
1. Suppose $B_1 = (4, 8, 14)$.
   - Check the solvability criteria for $A + X = B_1$.
   - If solvable, find the exact solution $X$.
   - Verify that $A + X = B_1$.
2. Suppose $B_2 = (4, 8, 9)$.
   - Check the solvability criteria for $A + X = B_2$.
   - What happens to the candidate vertices of $X$? Explain why no exact solution exists in $\mathcal{F}_N(\mathbb{R})$.
3. For $B_2$, evaluate the naive subtraction candidate $\tilde{X} = B_2 - A$ and compute $A + \tilde{X}$ to show explicitly that it fails to solve the equation.""",
                "hints": [
                    "Candidate vertices: $x_1 = b_1 - a_1, x_2 = b_2 - a_2, x_3 = b_3 - a_3$.",
                    "Requires $x_1 \\le x_2 \\le x_3$.",
                    "Evaluate $A + (B_2 - A)$."
                ],
                "solution": r"""### 1. Case 1: $B_1 = (4, 8, 14)$
$A = (1, 3, 5) \implies a_1 = 1, a_2 = 3, a_3 = 5$.
$B_1 = (4, 8, 14) \implies b_1 = 4, b_2 = 8, b_3 = 14$.

#### Solvability Check:
- Left spread of $A$: $a_2 - a_1 = 3 - 1 = 2$.
  Left spread of $B_1$: $b_2 - b_1 = 8 - 4 = 4 \ge 2$. (Satisfied).
- Right spread of $A$: $a_3 - a_2 = 5 - 3 = 2$.
  Right spread of $B_1$: $b_3 - b_2 = 14 - 8 = 6 \ge 2$. (Satisfied).

Candidate solution:
$$X = (b_1 - a_1, \; b_2 - a_2, \; b_3 - a_3) = (4 - 1, \; 8 - 3, \; 14 - 5) = (3, 5, 9)$$
Since $3 \le 5 \le 9$, $X = (3, 5, 9)$ is a valid TFN.

#### Verification:
$$A + X = (1, 3, 5) + (3, 5, 9) = (1 + 3, \; 3 + 5, \; 5 + 9) = (4, 8, 14) = B_1 \qquad \blacksquare$$

---

### 2. Case 2: $B_2 = (4, 8, 9)$
Here $b_3 - b_2 = 9 - 8 = 1$, whereas $a_3 - a_2 = 5 - 3 = 2$.
Since $1 < 2$, the right spread condition FAILS!
Candidate vertices:
$$x_1 = 4 - 1 = 3, \quad x_2 = 8 - 3 = 5, \quad x_3 = 9 - 5 = 4$$
Notice that $x_2 = 5 > x_3 = 4$.
The tuple $(3, 5, 4)$ is NOT an ordered sequence of real numbers; its membership function would fold backwards, which violates fuzzy convexity!
Therefore, **NO exact solution exists** in the space of fuzzy numbers. $\blacksquare$

---

### 3. Failure of Naive Subtraction $\tilde{X} = B_2 - A$
$$\tilde{X} = B_2 - A = (4, 8, 9) - (1, 3, 5) = (4 - 5, \; 8 - 3, \; 9 - 1) = (-1, 5, 8)$$
Now substitute $\tilde{X}$ back into the left-hand side:
$$A + \tilde{X} = (1, 3, 5) + (-1, 5, 8) = (1 + (-1), \; 3 + 5, \; 5 + 8) = (0, 8, 13)$$
Comparing:
$$A + \tilde{X} = (0, 8, 13) \ne (4, 8, 9) = B_2$$
The resulting fuzzy number is far wider and has a completely different support $[0, 13]$ instead of $[4, 9]$!
This demonstrates conclusively that $B - A$ does NOT solve $A + X = B$. $\blacksquare$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 5.3: Exact Non-Linear Membership Function of Product of Two TFNs",
                "statement": r"""Consider two symmetric Triangular Fuzzy Numbers:
$$A = (1, 2, 3), \qquad B = (1, 2, 3)$$
1. Using interval arithmetic on $\alpha$-cuts, determine the exact $\alpha$-cut representation $[A \cdot B]_\alpha$ of their product.
2. Invert the $\alpha$-cut boundaries to derive the exact analytical membership function $\mu_{A \cdot B}(z)$ for all $z \in [1, 9]$.
3. Prove that the graph of $\mu_{A \cdot B}(z)$ consists of two parabolic arcs and calculate the curvature at the peak $z = 4$.
4. Compare the exact product with the standard linear heuristic approximation $C_{\text{approx}} = (1, 4, 9)$ at $z = 2.25$.""",
                "hints": [
                    "For $A$, $A_\\alpha = [1 + \\alpha, 3 - \\alpha]$.",
                    "For $A \\cdot B$, $[A \\cdot B]_\\alpha = [(1 + \\alpha)^2, (3 - \\alpha)^2]$.",
                    "Set $z = (1 + \\alpha)^2$ to solve for $\\alpha(z) = \\sqrt{z} - 1$ on the left branch."
                ],
                "solution": r"""### 1. $\alpha$-Cut Representation of $A \cdot B$
Since $A = B = (1, 2, 3)$:
$$A_\alpha = B_\alpha = [1 + \alpha, \; 3 - \alpha], \quad \alpha \in [0, 1]$$
Since all values are positive, the product of the intervals is:
$$[A \cdot B]_\alpha = [ (1 + \alpha)^2, \; (3 - \alpha)^2 ] \qquad \blacksquare$$
- For $\alpha = 0$: $[A \cdot B]_0 = [1^2, 3^2] = [1, 9]$.
- For $\alpha = 1$: $[A \cdot B]_1 = [2^2, 2^2] = [4, 4] = \{4\}$.

---

### 2. Inversion to Membership Function $\mu_{A \cdot B}(z)$

#### Left Branch ($1 \le z \le 4$):
On the left boundary:
$$z = (1 + \alpha)^2 \implies \sqrt{z} = 1 + \alpha \implies \alpha = \sqrt{z} - 1$$

#### Right Branch ($4 \le z \le 9$):
On the right boundary:
$$z = (3 - \alpha)^2 \implies \sqrt{z} = 3 - \alpha \implies \alpha = 3 - \sqrt{z}$$

#### Exact Piecewise Membership Function:
$$\mu_{A \cdot B}(z) = \begin{cases} 
0, & z < 1 \\ 
\sqrt{z} - 1, & 1 \le z \le 4 \\ 
3 - \sqrt{z}, & 4 \le z \le 9 \\ 
0, & z > 9 
\end{cases} \qquad \blacksquare$$

---

### 3. Curvature Analysis
- On $[1, 4]$: $\frac{d\mu}{dz} = \frac{1}{2\sqrt{z}}$, and $\frac{d^2\mu}{dz^2} = -\frac{1}{4 z^{3/2}} < 0$.
  The curve is strictly concave (parabolic arc), NOT linear!
- On $[4, 9]$: $\frac{d\mu}{dz} = -\frac{1}{2\sqrt{z}}$, and $\frac{d^2\mu}{dz^2} = \frac{1}{4 z^{3/2}} > 0$.
  The curve is strictly convex.

At the peak $z = 4$:
- Left derivative: $\left.\frac{d\mu}{dz}\right|_{4^-} = \frac{1}{2\sqrt{4}} = \frac{1}{4} = 0.25$.
- Right derivative: $\left.\frac{d\mu}{dz}\right|_{4^+} = -\frac{1}{2\sqrt{4}} = -\frac{1}{4} = -0.25$.
The peak is a sharp corner with derivative jump $\Delta = -0.5$. $\blacksquare$

---

### 4. Comparison with Heuristic Approximation
The heuristic linear approximation is $C_{\text{approx}} = (1, 4, 9)$:
$$\mu_{\text{approx}}(z) = \frac{z - 1}{4 - 1} = \frac{z - 1}{3}, \quad z \in [1, 4]$$
Evaluate at $z = 2.25$:
- **Exact membership:**
  $$\mu_{\text{exact}}(2.25) = \sqrt{2.25} - 1 = 1.5 - 1 = 0.5000$$
- **Linear approximation:**
  $$\mu_{\text{approx}}(2.25) = \frac{2.25 - 1}{3} = \frac{1.25}{3} \approx 0.4167$$
The linear approximation underestimates the true membership grade by over 16.7%!
This highlights the importance of using exact $\alpha$-cuts in critical engineering applications. $\blacksquare$"""
            }
        ]
    }
    return u5

if __name__ == "__main__":
    u5 = get_unit5()
    print(f"Loaded Unit 5: {u5['title']} with {len(u5['sections'])} sections and {len(u5['problems'])} problems.")
