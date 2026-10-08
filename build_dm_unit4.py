# -*- coding: utf-8 -*-
"""
build_dm_unit4.py
Constructs Unit 4: Recurrence Relations, Generating Functions & Divide-and-Conquer
Strictly ZERO course numbers.
"""

def get_unit4():
    u4 = {
        "number": 4,
        "title": "Recurrence Relations, Generating Functions & Divide-and-Conquer",
        "leadSummary": "Comprehensive mathematical theory of discrete difference equations: linear homogeneous recurrences with constant coefficients, characteristic polynomials and multiplicity degeneracies, non-homogeneous equations via undetermined coefficients and annihilators, divide-and-conquer relations and the Master Theorem, ordinary generating functions (OGF) for Catalan sequences, exponential generating functions (EGF), and recursive tree complexity analysis.",
        "simulations": ["sim_dm_recurrence_tree"],
        "sections": [
            {
                "secNumber": "4.1",
                "title": "Linear Homogeneous Recurrences & Characteristic Root Theory",
                "content": r"""### 1. General Form of Linear Homogeneous Recurrences

A **linear homogeneous recurrence relation of degree $k$ with constant coefficients** has the canonical algebraic form:
$$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \dots + c_k a_{n-k}$$
where $c_1, c_2, \dots, c_k$ are real or complex constants with $c_k \ne 0$, accompanied by $k$ initial conditions $a_0, a_1, \dots, a_{k-1}$.

---

### 2. Characteristic Polynomial and Root Multiplicities

We seek non-trivial geometric sequence solutions of the form $a_n = r^n$ with $r \ne 0$.
Substituting $a_n = r^n$ into the recurrence relation:
$$r^n = c_1 r^{n-1} + c_2 r^{n-2} + \dots + c_k r^{n-k}$$
Dividing both sides by $r^{n-k}$ yields the fundamental **characteristic equation**:
$$r^k - c_1 r^{k-1} - c_2 r^{k-2} - \dots - c_k = 0$$

> **Theorem 4.1 (Distinct Roots Solution):**
> If the characteristic polynomial has $k$ distinct real or complex roots $r_1, r_2, \dots, r_k$, then the general solution is:
> $$a_n = \alpha_1 r_1^n + \alpha_2 r_2^n + \dots + \alpha_k r_k^n$$
> where constants $\alpha_1, \dots, \alpha_k$ are uniquely determined by the initial conditions via the non-singular Vandermonde matrix:
> $$\begin{pmatrix} 1 & 1 & \dots & 1 \\ r_1 & r_2 & \dots & r_k \\ \vdots & \vdots & \ddots & \vdots \\ r_1^{k-1} & r_2^{k-1} & \dots & r_k^{k-1} \end{pmatrix} \begin{pmatrix} \alpha_1 \\ \alpha_2 \\ \vdots \\ \alpha_k \end{pmatrix} = \begin{pmatrix} a_0 \\ a_1 \\ \vdots \\ a_{k-1} \end{pmatrix}$$

> **Theorem 4.2 (Multiple Roots / Degeneracy):**
> If a characteristic root $r_j$ occurs with multiplicity $m_j > 1$, then its contribution to the general solution is:
> $$(\alpha_{j, 0} + \alpha_{j, 1} n + \alpha_{j, 2} n^2 + \dots + \alpha_{j, m_j - 1} n^{m_j - 1}) r_j^n$$
> Summing across all distinct roots yields the full $k$-parameter vector space of solutions."""
            },
            {
                "secNumber": "4.2",
                "title": "Non-Homogeneous Recurrences: Undetermined Coefficients & Annihilators",
                "content": r"""### 1. Structure of Linear Non-Homogeneous Recurrences

A linear non-homogeneous recurrence relation has the form:
$$a_n = c_1 a_{n-1} + c_2 a_{n-2} + \dots + c_k a_{n-k} + F(n)$$
where $F(n)$ is a non-zero driving function.

> **Theorem 4.3 (Superposition Principle):**
> The general solution of the non-homogeneous recurrence is the sum:
> $$a_n = a_n^{(h)} + a_n^{(p)}$$
> where $a_n^{(h)}$ is the general solution of the associated homogeneous equation, and $a_n^{(p)}$ is any particular solution of the non-homogeneous equation.

---

### 2. Method of Undetermined Coefficients

For standard forcing functions, trial particular solutions $a_n^{(p)}$ are selected based on the form of $F(n)$:

| Forcing Term $F(n)$ | Root Condition | Form of Particular Solution $a_n^{(p)}$ |
| :--- | :--- | :--- |
| Polynomial $P_d(n)$ of degree $d$ | $r = 1$ is not a root of char. eq. | $Q_d(n) = A_0 + A_1 n + \dots + A_d n^d$ |
| Polynomial $P_d(n)$ of degree $d$ | $r = 1$ is a root of multiplicity $s$ | $n^s Q_d(n) = n^s (A_0 + A_1 n + \dots + A_d n^d)$ |
| Exponential $c \cdot \lambda^n$ | $\lambda$ is not a characteristic root | $A \cdot \lambda^n$ |
| Exponential $c \cdot \lambda^n$ | $\lambda$ is a root of multiplicity $s$ | $A \cdot n^s \lambda^n$ |
| Mixed $P_d(n) \cdot \lambda^n$ | $\lambda$ is a root of multiplicity $s$ | $n^s (A_0 + A_1 n + \dots + A_d n^d) \lambda^n$ |

The unknown coefficients $A_i$ are determined by substituting $a_n^{(p)}$ directly into the recurrence equation and equating corresponding powers of $n$ and $\lambda^n$."""
            },
            {
                "secNumber": "4.3",
                "title": "Divide-and-Conquer Recurrences & The Master Theorem",
                "content": r"""### 1. Divide-and-Conquer Algorithm Complexity

Many foundational computer science algorithms (such as MergeSort, Karatsuba Integer Multiplication, and Strassen's Matrix Multiplication) divide a problem of size $n$ into $a$ subproblems of size $n/b$, solve them recursively, and combine their results in $f(n)$ work:
$$T(n) = a T\left(\frac{n}{b}\right) + f(n)$$
where $a \ge 1$, $b > 1$, and $f(n) \ge 0$ asymptotically.

---

### 2. The Master Theorem

The critical threshold exponent is:
$$p = \log_b a$$
which represents the asymptotic growth rate of work done at the leaf level of the recursion tree.

> **Theorem 4.4 (Master Theorem for Divide-and-Conquer):**
> Let $T(n) = a T(n/b) + f(n)$.
>
> 1. **Case 1 (Leaf Dominant / Subproblems Dominate):**
>    If $f(n) = O(n^{\log_b a - \epsilon})$ for some constant $\epsilon > 0$, then:
>    $$T(n) = \Theta(n^{\log_b a})$$
>
> 2. **Case 2 (Balanced / Even Work Across Tree Levels):**
>    If $f(n) = \Theta(n^{\log_b a} \log^k n)$ for some integer $k \ge 0$, then:
>    $$T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$$
>    *(Standard case $k=0$ yields $T(n) = \Theta(n^{\log_b a} \log n)$).*
>
> 3. **Case 3 (Root Dominant / Division & Combine Work Dominates):**
>    If $f(n) = \Omega(n^{\log_b a + \epsilon})$ for some constant $\epsilon > 0$, and if $f(n)$ satisfies the **regularity condition**:
>    $$a f(n/b) \le c f(n) \quad \text{for some constant } c < 1 \text{ and sufficiently large } n$$
>    then:
>    $$T(n) = \Theta(f(n))$$"""
            },
            {
                "secNumber": "4.4",
                "title": "Ordinary Generating Functions (OGF) & Catalan Numbers",
                "content": r"""### 1. Formal Power Series and Ordinary Generating Functions

The **ordinary generating function (OGF)** of a sequence $(a_0, a_1, a_2, \dots)$ is the formal power series:
$$G(x) \equiv A(x) = \sum_{n=0}^\infty a_n x^n = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \dots$$
In formal algebraic power series, $x$ serves as a mathematical placeholder; questions of analytic radius of convergence are secondary to algebraic identities.

#### Fundamental Algebraic Operations:
- **Sum:** $\sum (a_n + b_n) x^n = A(x) + B(x)$.
- **Cauchy Convolution (Product):**
  $$A(x) B(x) = \sum_{n=0}^\infty \left( \sum_{k=0}^n a_k b_{n-k} \right) x^n$$
- **Shifting:**
  $$x A(x) = \sum_{n=1}^\infty a_{n-1} x^n, \qquad \frac{A(x) - a_0}{x} = \sum_{n=0}^\infty a_{n+1} x^n$$
- **Differentiation:**
  $$x A'(x) = \sum_{n=0}^\infty n a_n x^n$$

---

### 2. The Catalan Sequence via Generating Functions

The Catalan numbers count the number of valid Dyck paths, binary search trees with $n$ nodes, and ways to parenthesize a string of $n+1$ factors.
They satisfy Segner's non-linear convolution recurrence:
$$C_0 = 1, \qquad C_n = \sum_{k=0}^{n-1} C_k C_{n-1-k} \quad (n \ge 1)$$

Multiplying by $x^n$ and summing over $n \ge 1$:
$$C(x) - C_0 = \sum_{n=1}^\infty \left( \sum_{k=0}^{n-1} C_k C_{n-1-k} \right) x^n = x \sum_{m=0}^\infty \left( \sum_{k=0}^m C_k C_{m-k} \right) x^m = x C(x)^2$$
Thus, $C(x)$ satisfies the quadratic equation:
$$x C(x)^2 - C(x) + 1 = 0$$
Solving via the quadratic formula:
$$C(x) = \frac{1 - \sqrt{1 - 4x}}{2x}$$
(choosing the negative square root to satisfy $C(0) = \lim_{x \to 0} C(x) = 1$).
Expanding via the generalized binomial theorem yields the celebrated formula:
$$C_n = \frac{1}{n+1} \binom{2n}{n}$$"""
            },
            {
                "secNumber": "4.5",
                "title": "Exponential Generating Functions & Interactive Recurrence Tree Explorer",
                "content": r"""### 1. Exponential Generating Functions (EGF)

When counting ordered structures (such as labeled graphs, surjections, or permutations with restrictions), the **exponential generating function (EGF)** is standard:
$$\hat{G}(x) = \sum_{n=0}^\infty a_n \frac{x^n}{n!}$$

#### Product Rule for EGF:
$$\hat{A}(x) \hat{B}(x) = \sum_{n=0}^\infty \left( \sum_{k=0}^n \binom{n}{k} a_k b_{n-k} \right) \frac{x^n}{n!}$$
The binomial coefficient $\binom{n}{k}$ automatically counts the ways to partition $n$ labeled elements between the two substructures!

---

### 2. Interactive Recurrence Tree Explorer

The interactive simulation below renders the recursion tree for any divide-and-conquer parameters $a, b, f(n)$:
- **Visual Depth Progression:** Displays individual tree levels, node counts ($a^k$), subproblem dimensions ($n/b^k$), and local non-recursive overhead $a^k f(n/b^k)$.
- **Dynamic Regime Classifier:** Highlights whether the recurrence belongs to Case 1 (Leaf Dominant), Case 2 (Balanced), or Case 3 (Root Dominant), displaying the exact Master Theorem complexity bound."""
            }
        ],
        "problems": [
            {
                "tier": "Foundational Level",
                "title": "Problem 4.1: Homogeneous and Non-Homogeneous Difference Equations",
                "statement": r"""1. Solve the second-order linear homogeneous recurrence relation:
$$a_n = 5 a_{n-1} - 6 a_{n-2} \quad \text{for } n \ge 2$$
subject to the initial conditions $a_0 = 1, a_1 = 4$.

2. Find the complete solution to the non-homogeneous recurrence relation:
$$b_n = 2 b_{n-1} + 3^n \quad \text{for } n \ge 1$$
with initial condition $b_0 = 5$.""",
                "hints": [
                    "For part 1, write down the characteristic polynomial $r^2 - 5r + 6 = 0$.",
                    "For part 2, find the homogeneous solution $b_n^{(h)} = A \cdot 2^n$.",
                    "For the particular solution, try $b_n^{(p)} = B \cdot 3^n$."
                ],
                "solution": r"""### 1. Solving $a_n = 5 a_{n-1} - 6 a_{n-2}$

#### Step A: Characteristic Equation
Assume $a_n = r^n$:
$$r^2 - 5r + 6 = 0$$
Factoring:
$$(r - 2)(r - 3) = 0$$
The roots are distinct: $r_1 = 2$ and $r_2 = 3$.

#### Step B: General Homogeneous Solution
$$a_n = \alpha_1 2^n + \alpha_2 3^n$$

#### Step C: Apply Initial Conditions
- For $n = 0$:
  $$a_0 = \alpha_1 2^0 + \alpha_2 3^0 = \alpha_1 + \alpha_2 = 1$$
- For $n = 1$:
  $$a_1 = \alpha_1 2^1 + \alpha_2 3^1 = 2 \alpha_1 + 3 \alpha_2 = 4$$

From the first equation, $\alpha_1 = 1 - \alpha_2$.
Substitute into the second:
$$2(1 - \alpha_2) + 3 \alpha_2 = 4 \implies 2 + \alpha_2 = 4 \implies \alpha_2 = 2$$
Then $\alpha_1 = 1 - 2 = -1$.

Thus, the exact solution is:
$$a_n = -2^n + 2 \cdot 3^n = 2 \cdot 3^n - 2^n$$

---

### 2. Solving $b_n = 2 b_{n-1} + 3^n$

#### Step A: Homogeneous Solution
The homogeneous equation is $b_n - 2 b_{n-1} = 0$, giving characteristic equation $r - 2 = 0 \implies r = 2$.
$$b_n^{(h)} = A \cdot 2^n$$

#### Step B: Particular Solution
Since the driving term is $F(n) = 3^n$ and $\lambda = 3$ is **not** a root of the characteristic equation ($3 \ne 2$), we try:
$$b_n^{(p)} = B \cdot 3^n$$
Substitute into the recurrence:
$$B \cdot 3^n = 2(B \cdot 3^{n-1}) + 3^n$$
Divide through by $3^{n-1}$:
$$3 B = 2 B + 3 \implies B = 3$$
Thus:
$$b_n^{(p)} = 3 \cdot 3^n = 3^{n+1}$$

#### Step C: General Solution and Initial Condition
$$b_n = b_n^{(h)} + b_n^{(p)} = A \cdot 2^n + 3^{n+1}$$
Using $b_0 = 5$:
$$b_0 = A \cdot 2^0 + 3^{0+1} = A + 3 = 5 \implies A = 2$$
Therefore, the unique solution is:
$$b_n = 2 \cdot 2^n + 3^{n+1} = 2^{n+1} + 3^{n+1} \blacksquare$$"""
            },
            {
                "tier": "Advanced Level",
                "title": "Problem 4.2: Closed-Form Derivation of Catalan Numbers via Generating Functions",
                "statement": r"""The Catalan numbers satisfy the non-linear recurrence:
$$C_0 = 1, \qquad C_n = \sum_{k=0}^{n-1} C_k C_{n-1-k} \quad \text{for } n \ge 1$$
1. Define the ordinary generating function $C(x) = \sum_{n=0}^\infty C_n x^n$. Prove that $C(x)$ satisfies the algebraic equation $x C(x)^2 - C(x) + 1 = 0$.
2. Solve this quadratic equation and justify mathematically why the negative square root branch must be chosen.
3. Use the generalized binomial series expansion of $(1 - 4x)^{1/2}$ to extract the coefficient of $x^n$ and establish that:
$$C_n = \frac{1}{n+1} \binom{2n}{n}$$""",
                "hints": [
                    "Recall that $(C(x))^2 = \\sum_{m=0}^\\infty (\\sum_{k=0}^m C_k C_{m-k}) x^m$.",
                    "Check the limit as $x \\to 0$: since $C_0 = 1$, we must have $\\lim_{x \\to 0} C(x) = 1$.",
                    "Recall $\\binom{1/2}{k} = \\frac{(-1)^{k-1}}{k! 2^{2k-1}} \\frac{(2k-2)!}{(k-1)!}$."
                ],
                "solution": r"""### 1. Generating Function Equation
Let $C(x) = \sum_{n=0}^\infty C_n x^n$.
The Cauchy product of $C(x)$ with itself is:
$$[C(x)]^2 = \sum_{m=0}^\infty \left( \sum_{k=0}^m C_k C_{m-k} \right) x^m$$
Multiplying by $x$:
$$x [C(x)]^2 = \sum_{m=0}^\infty \left( \sum_{k=0}^m C_k C_{m-k} \right) x^{m+1}$$
Let $n = m + 1$. The sum runs from $n = 1$ to $\infty$:
$$x [C(x)]^2 = \sum_{n=1}^\infty \left( \sum_{k=0}^{n-1} C_k C_{n-1-k} \right) x^n$$
By the recurrence relation, the bracketed inner sum is precisely $C_n$:
$$x [C(x)]^2 = \sum_{n=1}^\infty C_n x^n = C(x) - C_0 = C(x) - 1$$
Rearranging terms yields the quadratic relation:
$$x C(x)^2 - C(x) + 1 = 0$$

---

### 2. Solving the Quadratic and Branch Selection
Using the quadratic formula:
$$C(x) = \frac{1 \pm \sqrt{1 - 4x}}{2x}$$
To select the correct branch, evaluate the limit as $x \to 0$:
Since $C(x) = C_0 + C_1 x + \dots$, we must have $\lim_{x \to 0} C(x) = C_0 = 1$.
- If we chose the positive sign:
  $$\lim_{x \to 0} \frac{1 + \sqrt{1 - 4x}}{2x} = \lim_{x \to 0} \frac{2}{2x} = \infty \quad (\text{Singular!})$$
- Choosing the negative sign:
  $$\lim_{x \to 0} \frac{1 - \sqrt{1 - 4x}}{2x} = \lim_{x \to 0} \frac{-(1/2)(1 - 4x)^{-1/2}(-4)}{2} = \lim_{x \to 0} (1 - 4x)^{-1/2} = 1$$
  which matches $C_0 = 1$ perfectly!

Therefore, the generating function is:
$$C(x) = \frac{1 - (1 - 4x)^{1/2}}{2x}$$

---

### 3. Generalized Binomial Expansion and Coefficient Extraction
By Newton's generalized binomial theorem:
$$(1 - 4x)^{1/2} = \sum_{k=0}^\infty \binom{1/2}{k} (-4x)^k = 1 + \sum_{k=1}^\infty \binom{1/2}{k} (-4)^k x^k$$
Let us compute $\binom{1/2}{k}$ for $k \ge 1$:
$$\begin{aligned}
\binom{1/2}{k} &= \frac{\frac{1}{2}\left(-\frac{1}{2}\right)\left(-\frac{3}{2}\right)\cdots\left(\frac{1}{2} - k + 1\right)}{k!} \\
&= \frac{(-1)^{k-1} \cdot 1 \cdot 3 \cdot 5 \cdots (2k - 3)}{2^k \cdot k!}
\end{aligned}$$
Expressing the double factorial in terms of standard factorials:
$$1 \cdot 3 \cdot 5 \cdots (2k - 3) = \frac{(2k - 2)!}{2^{k-1}(k - 1)!}$$
Thus:
$$\binom{1/2}{k} = \frac{(-1)^{k-1} (2k - 2)!}{2^{2k - 1} k! (k - 1)!} = \frac{(-1)^{k-1}}{2^{2k - 1} k} \binom{2k - 2}{k - 1}$$
Now multiply by $(-4)^k = (-1)^k 2^{2k}$:
$$\binom{1/2}{k} (-4)^k = \frac{(-1)^{k-1}(-1)^k 2^{2k}}{2^{2k - 1} k} \binom{2k - 2}{k - 1} = -\frac{2}{k} \binom{2k - 2}{k - 1}$$
Substitute back into the expression for $C(x)$:
$$\begin{aligned}
C(x) &= \frac{1 - \left( 1 - \sum_{k=1}^\infty \frac{2}{k} \binom{2k - 2}{k - 1} x^k \right)}{2x} \\
&= \frac{1}{2x} \sum_{k=1}^\infty \frac{2}{k} \binom{2k - 2}{k - 1} x^k \\
&= \sum_{k=1}^\infty \frac{1}{k} \binom{2k - 2}{k - 1} x^{k-1}
\end{aligned}$$
Let $n = k - 1 \implies k = n + 1$:
$$C(x) = \sum_{n=0}^\infty \frac{1}{n + 1} \binom{2n}{n} x^n$$
Extracting the coefficient of $x^n$:
$$C_n = \frac{1}{n + 1} \binom{2n}{n} \blacksquare$$"""
            },
            {
                "tier": "Honors / Proof Challenge",
                "title": "Problem 4.3: Analytical Tree Proof of the Master Theorem Across Three Regimes",
                "statement": r"""Consider the divide-and-conquer recurrence relation:
$$T(n) = a T\left(\frac{n}{b}\right) + f(n)$$
defined on powers of $b$ ($n = b^k$), with base case $T(1) = \Theta(1)$.

1. Expand the recurrence into an explicit geometric tree summation across depth levels $j = 0, 1, \dots, \log_b n$.
2. **Prove Case 1:** If $f(n) = O(n^{\log_b a - \epsilon})$ for $\epsilon > 0$, prove that $T(n) = \Theta(n^{\log_b a})$.
3. **Prove Case 2:** If $f(n) = \Theta(n^{\log_b a})$, prove that $T(n) = \Theta(n^{\log_b a} \log n)$.
4. **Prove Case 3:** If $f(n) = \Omega(n^{\log_b a + \epsilon})$ and $a f(n/b) \le c f(n)$ for $c < 1$, prove that $T(n) = \Theta(f(n))$.""",
                "hints": [
                    "The number of subproblems at level $j$ is $a^j$, each of size $n/b^j$.",
                    "The total work is $T(n) = a^k T(1) + \\sum_{j=0}^{k-1} a^j f(n/b^j)$, where $k = \\log_b n$.",
                    "Use the algebraic identity $a^{\\log_b n} = n^{\\log_b a}$."
                ],
                "solution": r"""### 1. Recursion Tree Summation
At level $j$ of the recursion tree:
- Number of subproblems $= a^j$.
- Size of each subproblem $= \frac{n}{b^j}$.
- Non-recursive combine work per subproblem $= f\left(\frac{n}{b^j}\right)$.
- Total work done at level $j$: $W_j = a^j f\left(\frac{n}{b^j}\right)$.

The tree reaches the leaves when $\frac{n}{b^k} = 1 \implies k = \log_b n$.
The number of leaves is $a^k = a^{\log_b n} = n^{\log_b a}$.
Summing across all levels:
$$T(n) = \Theta(n^{\log_b a}) + \sum_{j=0}^{\log_b n - 1} a^j f\left(\frac{n}{b^j}\right)$$

---

### 2. Proof of Case 1: $f(n) = O(n^{\log_b a - \epsilon})$
Let $p = \log_b a$. We are given $f(n) \le C n^{p - \epsilon}$.
Substitute this bound into the level sum:
$$W_j = a^j f\left(\frac{n}{b^j}\right) \le C a^j \left( \frac{n}{b^j} \right)^{p - \epsilon} = C n^{p - \epsilon} \left( \frac{a}{b^{p - \epsilon}} \right)^j$$
Recall that $b^p = b^{\log_b a} = a$. Thus:
$$\frac{a}{b^{p - \epsilon}} = \frac{a}{b^p \cdot b^{-\epsilon}} = \frac{a}{a \cdot b^{-\epsilon}} = b^\epsilon$$
Therefore:
$$\sum_{j=0}^{k - 1} W_j \le C n^{p - \epsilon} \sum_{j=0}^{k - 1} (b^\epsilon)^j$$
Since $b > 1$ and $\epsilon > 0$, the ratio $b^\epsilon > 1$. The sum is an increasing geometric series:
$$\sum_{j=0}^{k - 1} (b^\epsilon)^j = \frac{(b^\epsilon)^k - 1}{b^\epsilon - 1} = O\left( (b^k)^\epsilon \right) = O(n^\epsilon)$$
Multiplying by $C n^{p - \epsilon}$:
$$\sum_{j=0}^{k - 1} W_j = O\left( n^{p - \epsilon} \cdot n^\epsilon \right) = O(n^p) = O(n^{\log_b a})$$
The leaf work $\Theta(n^{\log_b a})$ dominates the sum.
Hence:
$$T(n) = \Theta(n^{\log_b a}) \blacksquare$$

---

### 3. Proof of Case 2: $f(n) = \Theta(n^{\log_b a})$
Here $f(n) = \Theta(n^p)$.
Then at each level $j$:
$$W_j = a^j f\left(\frac{n}{b^j}\right) = \Theta\left( a^j \left(\frac{n}{b^j}\right)^p \right) = \Theta\left( n^p \left(\frac{a}{b^p}\right)^j \right)$$
Since $b^p = a$, the ratio $\frac{a}{b^p} = 1$.
Thus, every single level does **identical work**:
$$W_j = \Theta(n^p)$$
There are $k = \log_b n$ levels:
$$\sum_{j=0}^{k - 1} W_j = \sum_{j=0}^{\log_b n - 1} \Theta(n^p) = \Theta(n^p \log_b n)$$
Adding the leaf work $\Theta(n^p)$, we obtain:
$$T(n) = \Theta(n^{\log_b a} \log n) \blacksquare$$

---

### 4. Proof of Case 3: Root Dominant with Regularity Condition
We are given $a f(n/b) \le c f(n)$ for some constant $c < 1$.
Applying this inequality inductively:
$$a^j f\left(\frac{n}{b^j}\right) \le c^j f(n)$$
Therefore, the sum over all levels is bounded by a convergent geometric series:
$$\sum_{j=0}^{k - 1} a^j f\left(\frac{n}{b^j}\right) \le f(n) \sum_{j=0}^{k - 1} c^j < f(n) \sum_{j=0}^\infty c^j = f(n) \left(\frac{1}{1 - c}\right) = O(f(n))$$
Since the $j=0$ term (the root) alone is $f(n)$, the sum is also $\Omega(f(n))$.
Furthermore, since $f(n) = \Omega(n^{p + \epsilon})$, the root work $f(n)$ asymptotically dwarfs the leaf work $n^p$:
$$\lim_{n \to \infty} \frac{n^p}{f(n)} \le \lim_{n \to \infty} \frac{n^p}{K n^{p + \epsilon}} = 0$$
Thus:
$$T(n) = \Theta(f(n)) \blacksquare$$"""
            }
        ]
    }
    return u4

if __name__ == "__main__":
    u4 = get_unit4()
    print(f"Loaded Unit 4: {u4['title']} with {len(u4['sections'])} sections and {len(u4['problems'])} problems.")
