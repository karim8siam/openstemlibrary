import json

# Unit 3: Theory of Equations: Roots, Coefficients & Symmetric Functions
u3 = {
  "unit_id": "unit_3",
  "unit_title": "Theory of Equations: Roots, Coefficients & Symmetric Functions",
  "unit_subtitle": "Fundamental Theorem of Algebra, Viète's Formulas, Symmetric Reductions & Newton-Girard Identities",
  "sections": [
    {
      "id": "sec_3_1",
      "title": "Fundamental Theorem of Algebra & Factorization",
      "content": r"""
<h3>1. The Fundamental Theorem of Algebra</h3>
<p>
<strong>Theorem (d'Alembert–Gauss):</strong> Every non-constant single-variable polynomial with complex coefficients has at least one complex root.<br>
As an immediate corollary, any polynomial of degree $n \ge 1$:
$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0, \quad a_n \ne 0, \; a_i \in \mathbb{C}$$
can be completely factored into linear factors over $\mathbb{C}$:
$$\mathbf{P(x) = a_n (x - \alpha_1)(x - \alpha_2)\cdots(x - \alpha_n) = a_n \prod_{i=1}^n (x - \alpha_i)}$$
where $\alpha_1, \alpha_2, \dots, \alpha_n \in \mathbb{C}$ are the $n$ roots (counted with multiplicity).
</p>

<h3>2. The Conjugate Pairs Theorem for Real Polynomials</h3>
<p>
<strong>Theorem:</strong> If $P(x)$ is a polynomial with real coefficients ($a_i \in \mathbb{R}$) and $\alpha = u + iv$ is a complex root ($v \ne 0$), then its complex conjugate $\bar{\alpha} = u - iv$ is also a root of $P(x)$ of identical multiplicity.<br>
<em>Proof:</em> Since $P(\alpha) = \sum_{k=0}^n a_k \alpha^k = 0$, taking complex conjugates yields:
$$\overline{P(\alpha)} = \overline{\sum_{k=0}^n a_k \alpha^k} = \sum_{k=0}^n \bar{a}_k (\bar{\alpha})^k = \sum_{k=0}^n a_k (\bar{\alpha})^k = P(\bar{\alpha}) = \bar{0} = 0$$
Thus $P(\bar{\alpha}) = 0$. $\blacksquare$
</p>
<p>
Consequently, every complex root pair yields an irreducible real quadratic factor:
$$(x - \alpha)(x - \bar{\alpha}) = x^2 - 2u x + (u^2 + v^2) \in \mathbb{R}[x]$$
This guarantees that any real polynomial can be factored over $\mathbb{R}$ into linear and irreducible quadratic factors. In particular, every real polynomial of odd degree has at least one real root.
</p>
"""
    },
    {
      "id": "sec_3_2",
      "title": "Viète's Formulas Relating Roots and Coefficients",
      "content": r"""
<h3>1. General Formulation for Degree $n$</h3>
<p>
François Viète discovered the universal algebraic relations connecting the roots $\alpha_1, \dots, \alpha_n$ of a monic polynomial $x^n + p_1 x^{n-1} + p_2 x^{n-2} + \dots + p_n = 0$ to its coefficients:
$$\prod_{i=1}^n (x - \alpha_i) = x^n - \left(\sum \alpha_i\right)x^{n-1} + \left(\sum_{i < j} \alpha_i \alpha_j\right)x^{n-2} - \dots + (-1)^n (\alpha_1 \cdots \alpha_n)$$
Equating coefficients of identical powers of $x$:
$$\mathbf{p_k = (-1)^k e_k(\alpha_1, \dots, \alpha_n), \quad k = 1, 2, \dots, n}$$
where $e_k$ is the $k$-th elementary symmetric polynomial.
</p>

<h3>2. Explicit Relations for the Cubic Equation</h3>
<p>
For the cubic polynomial $x^3 + p x^2 + q x + r = 0$ with roots $\alpha, \beta, \gamma$:
<div class="math-display">
$$\mathbf{\sum \alpha = \alpha + \beta + \gamma = -p}$$
$$\mathbf{\sum \alpha\beta = \alpha\beta + \beta\gamma + \gamma\alpha = q}$$
$$\mathbf{\alpha\beta\gamma = -r}$$
</div>
</p>

<h3>3. Explicit Relations for the Quartic Equation</h3>
<p>
For the quartic polynomial $x^4 + p x^3 + q x^2 + r x + s = 0$ with roots $\alpha, \beta, \gamma, \delta$:
<div class="math-display">
$$\mathbf{\sum \alpha = -p}$$
$$\mathbf{\sum \alpha\beta = q}$$
$$\mathbf{\sum \alpha\beta\gamma = -r}$$
$$\mathbf{\alpha\beta\gamma\delta = s}$$
</div>
These relations permit setting up auxiliary algebraic equations when roots satisfy known constraints (e.g., arithmetic, geometric, or harmonic progressions).
</p>
"""
    },
    {
      "id": "sec_3_3",
      "title": "Elementary Symmetric Polynomials & Invariance",
      "content": r"""
<h3>1. Definition of Symmetric Polynomials</h3>
<p>
A polynomial $f(x_1, x_2, \dots, x_n)$ is called <strong>symmetric</strong> if it remains strictly invariant under every permutation $\sigma \in S_n$ of its variables:
$$f(x_{\sigma(1)}, x_{\sigma(2)}, \dots, x_{\sigma(n)}) = f(x_1, x_2, \dots, x_n)$$
</p>

<h3>2. The Elementary Symmetric Polynomials</h3>
<p>
The elementary symmetric polynomials $e_1, e_2, \dots, e_n$ in $n$ variables are defined as:
$$e_1 = \sum_{1 \le i \le n} x_i, \quad e_2 = \sum_{1 \le i < j \le n} x_i x_j, \quad \dots, \quad e_n = x_1 x_2 \cdots x_n$$
with generating function:
$$\prod_{i=1}^n (1 + t x_i) = 1 + e_1 t + e_2 t^2 + \dots + e_n t^n = \sum_{k=0}^n e_k t^k$$
</p>

<h3>3. The Fundamental Theorem of Symmetric Polynomials</h3>
<p>
<strong>Theorem:</strong> Every symmetric polynomial $f(x_1, \dots, x_n)$ with coefficients in a ring $R$ can be written uniquely as a polynomial in the elementary symmetric polynomials $e_1, \dots, e_n$ with coefficients in $R$:
$$\mathbf{f(x_1, \dots, x_n) = P(e_1, e_2, \dots, e_n)}$$
<em>Significance:</em> Any symmetric combination of the roots of a polynomial equation can be evaluated purely in terms of the polynomial's given coefficients without ever explicitly solving for the roots!
</p>
"""
    },
    {
      "id": "sec_3_4",
      "title": "Symmetric Functions of the Roots & Classical Reductions",
      "content": r"""
<h3>1. Classical Symmetric Sums for Cubic Roots</h3>
<p>
Let $\alpha, \beta, \gamma$ be the roots of $x^3 + p x^2 + q x + r = 0$, so $e_1 = -p$, $e_2 = q$, $e_3 = -r$.
We express classical symmetric combinations in terms of $p, q, r$:
<ul>
  <li><strong>Sum of Squares:</strong>
  $$\mathbf{\sum \alpha^2 \equiv \alpha^2 + \beta^2 + \gamma^2 = e_1^2 - 2e_2 = p^2 - 2q}$$</li>
  <li><strong>Product-Cross Sum:</strong>
  $$\mathbf{\sum \alpha^2 \beta = e_1 e_2 - 3e_3 = -pq + 3r}$$</li>
  <li><strong>Sum of Cubes:</strong>
  $$\mathbf{\sum \alpha^3 = e_1^3 - 3e_1 e_2 + 3e_3 = -p^3 + 3pq - 3r}$$</li>
  <li><strong>Sum of Squares of Differences:</strong>
  $$(\alpha - \beta)^2 + (\beta - \gamma)^2 + (\gamma - \alpha)^2 = 2\sum \alpha^2 - 2\sum \alpha\beta = 2(p^2 - 2q) - 2q = \mathbf{2p^2 - 6q}$$</li>
</ul>
</p>

<h3>2. The Polynomial Discriminant</h3>
<p>
The <strong>discriminant</strong> of a polynomial $P(x)$ of degree $n$ with roots $\alpha_1, \dots, \alpha_n$ is defined by:
$$\mathbf{\Delta \equiv a_n^{2n-2} \prod_{1 \le i < j \le n} (\alpha_i - \alpha_j)^2}$$
Since $\Delta$ is symmetric in the roots, it is a polynomial in the coefficients. For the depressed cubic $x^3 + px + q = 0$, its roots satisfy:
$$\mathbf{\Delta = -4p^3 - 27q^2}$$
If $\Delta > 0$, the cubic has 3 distinct real roots; if $\Delta = 0$, it has repeated roots; if $\Delta < 0$, it has 1 real root and 2 non-real conjugate roots.
</p>
"""
    },
    {
      "id": "sec_3_5",
      "title": "Sums of Powers of Roots & Newton-Girard Identities",
      "content": r"""
<h3>1. Definition of Power Sums</h3>
<p>
For a monic polynomial $P(x) = x^n + p_1 x^{n-1} + \dots + p_n = 0$ with roots $\alpha_1, \dots, \alpha_n$, we define the $k$-th <strong>power sum</strong> as:
$$\mathbf{s_k \equiv \sum_{i=1}^n \alpha_i^k = \alpha_1^k + \alpha_2^k + \dots + \alpha_n^k}$$
For $k = 0$, $s_0 = n$.
</p>

<h3>2. The Newton-Girard Recurrence Relations</h3>
<p>
Isaac Newton and Albert Girard derived the recursive relations connecting power sums $s_k$ directly to the polynomial coefficients $p_1, \dots, p_n$:
<div class="math-display">
$$\mathbf{s_k + p_1 s_{k-1} + p_2 s_{k-2} + \dots + p_{k-1} s_1 + k p_k = 0, \quad \text{for } 1 \le k \le n}$$
$$\mathbf{s_k + p_1 s_{k-1} + p_2 s_{k-2} + \dots + p_n s_{k-n} = 0, \quad \text{for } k > n}$$
</div>
</p>

<h3>3. Derivation via Logarithmic Differentiation</h3>
<p>
Writing $P(x) = \prod_{i=1}^n (x - \alpha_i)$, taking the formal logarithmic derivative:
$$\frac{P'(x)}{P(x)} = \sum_{i=1}^n \frac{1}{x - \alpha_i} = \frac{1}{x} \sum_{i=1}^n \frac{1}{1 - \alpha_i/x} = \sum_{i=1}^n \sum_{k=0}^\infty \frac{\alpha_i^k}{x^{k+1}} = \sum_{k=0}^\infty \frac{s_k}{x^{k+1}}$$
Multiplying both sides by $P(x) = x^n + p_1 x^{n-1} + \dots + p_n$ and equating coefficients of corresponding powers of $x$ establishes the Newton-Girard identities for all $k \ge 1$. $\blacksquare$
</p>
"""
    }
  ],
  "simulation": {
    "sim_id": "algebra-viete-symmetric-sim",
    "title": "Interactive Polynomial Roots & Viète Symmetric Invariant Explorer",
    "description": "Drag the real roots α, β, γ along the horizontal axis to dynamically reconstruct the cubic polynomial curve P(x). Live computes Viète coefficients, symmetric sums, and verifies Newton-Girard power sums s₁ through s₄."
  },
  "problems": [
    {
      "difficulty": "Tier 1: Foundational",
      "difficultyLabel": "Foundational Mechanics",
      "title": "Example 3.1: Cubic Roots in Arithmetic Progression",
      "statement": r"Solve the cubic equation $x^3 - 12x^2 + 39x - 28 = 0$, given that its roots are in Arithmetic Progression (A.P.).",
      "steps": [
        {
          "step": "Step 1: Parametrize Roots in A.P.",
          "math": r"\text{Let the roots be } \alpha = a - d, \quad \beta = a, \quad \gamma = a + d",
          "explanation": "Using symmetric parameterization simplifies the sum of roots."
        },
        {
          "step": "Step 2: Apply Viète's Formula for Sum of Roots",
          "math": r"\sum \text{roots} = (a - d) + a + (a + d) = 3a = -(-12) = 12 \implies a = 4",
          "explanation": "The sum eliminates the common difference $d$, directly giving middle root $a = 4$."
        },
        {
          "step": "Step 3: Apply Viète's Product Formula to Find d",
          "math": r"\text{Product of roots: } (a - d)a(a + d) = a(a^2 - d^2) = -(-28) = 28 \\ 4(16 - d^2) = 28 \implies 16 - d^2 = 7 \implies d^2 = 9 \implies d = \pm 3",
          "explanation": "Substitute $a = 4$ into the product relation and solve for $d$."
        },
        {
          "step": "Step 4: Compute All Roots",
          "math": r"\text{For } d = 3: \quad \alpha = 4 - 3 = 1, \quad \beta = 4, \quad \gamma = 4 + 3 = 7 \\ \text{Check } \sum \alpha\beta: 1\cdot 4 + 4\cdot 7 + 7\cdot 1 = 4 + 28 + 7 = 39 \quad \checkmark",
          "explanation": "The roots are 1, 4, and 7, matching all coefficients."
        }
      ],
      "answer": r"\text{The roots of the equation are } x \in \{1, 4, 7\}."
    },
    {
      "difficulty": "Tier 2: Intermediate Exam",
      "difficultyLabel": "Intermediate University Exam",
      "title": "Example 3.2: Symmetric Function Evaluation and Transformed Cubic",
      "statement": r"If $\alpha, \beta, \gamma$ are the roots of the cubic equation $x^3 + px + q = 0$, find: (a) The value of $\sum \frac{1}{\alpha^2 + \beta\gamma}$. (b) The cubic equation whose roots are $y_1 = \beta + \gamma - \alpha$, $y_2 = \gamma + \alpha - \beta$, and $y_3 = \alpha + \beta - \gamma$.",
      "steps": [
        {
          "step": "Step 1: Simplify Denominator via Viète Product",
          "math": r"\text{Since } \sum \alpha = 0, \quad \sum \alpha\beta = p, \quad \alpha\beta\gamma = -q \\ \beta\gamma = -\frac{q}{\alpha} \implies \alpha^2 + \beta\gamma = \alpha^2 - \frac{q}{\alpha} = \frac{\alpha^3 - q}{\alpha} \\ \text{Since } \alpha \text{ satisfies } \alpha^3 + p\alpha + q = 0: \quad \alpha^3 - q = -p\alpha - 2q \\ \frac{1}{\alpha^2 + \beta\gamma} = \frac{\alpha}{-p\alpha - 2q}",
          "explanation": "Rewrite $\\beta\\gamma$ using the root equation $\\alpha^3 = -p\\alpha - q$."
        },
        {
          "step": "Step 2: Construct the Transformed Equation for y",
          "math": r"\text{Since } \alpha + \beta + \gamma = 0: \quad \beta + \gamma = -\alpha \\ y_1 = -\alpha - \alpha = -2\alpha, \quad y_2 = -2\beta, \quad y_3 = -2\gamma",
          "explanation": "Substitute $\\beta + \\gamma = -\\alpha$ to obtain the direct root transformation $y = -2x$."
        },
        {
          "step": "Step 3: Transform the Polynomial Equation",
          "math": r"x = -\frac{y}{2} \implies \left(-\frac{y}{2}\right)^3 + p\left(-\frac{y}{2}\right) + q = 0 \\ -\frac{y^3}{8} - \frac{py}{2} + q = 0 \iff y^3 + 4py - 8q = 0",
          "explanation": "Substitute $x = -y/2$ into the original cubic and multiply by $-8$."
        }
      ],
      "answer": r"\text{Transformed Cubic: } \mathbf{y^3 + 4py - 8q = 0}; \quad \text{Roots are } -2\alpha, -2\beta, -2\gamma."
    },
    {
      "difficulty": "Tier 3: Honors / Proof Challenge",
      "difficultyLabel": "Honors / Proof Challenge",
      "title": "Example 3.3: Recursive Newton-Girard Power Sums for a Quartic",
      "statement": r"For the monic quartic equation $x^4 + p x^3 + q x^2 + r x + s = 0$ with roots $\alpha_1, \alpha_2, \alpha_3, \alpha_4$, use the Newton-Girard identities to derive explicit expressions for $s_1, s_2, s_3, s_4$, and prove that $s_4 = p^4 - 4p^2 q + 4pr + 2q^2 - 4s$.",
      "steps": [
        {
          "step": "Step 1: Compute s₁ and s₂ via Newton-Girard",
          "math": r"k = 1: \quad s_1 + p = 0 \implies s_1 = -p \\ k = 2: \quad s_2 + p s_1 + 2q = 0 \implies s_2 = -p(-p) - 2q = p^2 - 2q",
          "explanation": "Apply $s_k + p_1 s_{k-1} + \dots + k p_k = 0$ for $k = 1$ and $k = 2$."
        },
        {
          "step": "Step 2: Compute s₃",
          "math": r"k = 3: \quad s_3 + p s_2 + q s_1 + 3r = 0 \\ s_3 = -p(p^2 - 2q) - q(-p) - 3r = -p^3 + 2pq + pq - 3r = -p^3 + 3pq - 3r",
          "explanation": "Apply the recurrence for $k = 3$."
        },
        {
          "step": "Step 3: Compute s₄ and Conclude Proof",
          "math": r"k = 4: \quad s_4 + p s_3 + q s_2 + r s_1 + 4s = 0 \\ s_4 = -p s_3 - q s_2 - r s_1 - 4s \\ s_4 = -p(-p^3 + 3pq - 3r) - q(p^2 - 2q) - r(-p) - 4s \\ = (p^4 - 3p^2 q + 3pr) - (p^2 q - 2q^2) + pr - 4s \\ = p^4 - 4p^2 q + 4pr + 2q^2 - 4s \quad \blacksquare",
          "explanation": "Substitute $s_1, s_2, s_3$ into the order-4 recurrence relation and expand algebraically."
        }
      ],
      "answer": r"\mathbf{s_1 = -p}, \quad \mathbf{s_2 = p^2 - 2q}, \quad \mathbf{s_3 = -p^3 + 3pq - 3r}, \quad \mathbf{s_4 = p^4 - 4p^2 q + 4pr + 2q^2 - 4s}."
    }
  ]
}

# Unit 4: Polynomial Division, Descartes' Rule of Signs, Multiplicity & Transformations
u4 = {
  "unit_id": "unit_4",
  "unit_title": "Polynomial Division, Descartes' Rule of Signs & Transformations",
  "unit_subtitle": "Horner's Synthetic Division, Descartes' Sign Criteria, Multiple Root GCD Analysis & Reciprocal Solvers",
  "sections": [
    {
      "id": "sec_4_1",
      "title": "Euclidean Division Algorithm & Horner’s Synthetic Scheme",
      "content": r"""
<h3>1. The Division Algorithm for Polynomials</h3>
<p>
For any polynomial dividend $P(x)$ and non-zero divisor $D(x)$, there exist unique quotient $Q(x)$ and remainder $R(x)$ such that:
$$\mathbf{P(x) = D(x) Q(x) + R(x), \quad \text{where } \deg(R) < \deg(D) \text{ or } R(x) = 0}$$
<strong>Remainder Theorem:</strong> When divided by a linear factor $(x - c)$, the remainder is the constant $R = P(c)$.<br>
<strong>Factor Theorem:</strong> A linear binomial $(x - c)$ is a factor of $P(x)$ if and only if $P(c) = 0$.
</p>

<h3>2. Horner’s Synthetic Division Algorithm</h3>
<p>
William George Horner formalized a streamlined algorithm for dividing a polynomial $P(x) = a_n x^n + \dots + a_0$ by $(x - c)$ using only $n$ multiplications and $n$ additions:
$$\begin{array}{c|cccccc}
c & a_n & a_{n-1} & a_{n-2} & \dots & a_1 & a_0 \\
  &     & c b_{n-1} & c b_{n-2} & \dots & c b_1 & c b_0 \\
\hline
  & b_{n-1} & b_{n-2} & b_{n-3} & \dots & b_0 & R
\end{array}$$
where the recurrence is initialized by $b_{n-1} = a_n$ and generated by:
$$\mathbf{b_{k-1} = a_k + c \, b_k, \quad \text{with remainder } R = P(c) = a_0 + c \, b_0}$$
The quotient polynomial is $Q(x) = b_{n-1} x^{n-1} + b_{n-2} x^{n-2} + \dots + b_0$.
</p>
"""
    },
    {
      "id": "sec_4_2",
      "title": "Descartes’ Rule of Signs",
      "content": r"""
<h3>1. Statement of Descartes’ Theorem</h3>
<p>
René Descartes established an analytical bound on the real roots of a real polynomial $P(x) = a_n x^n + \dots + a_0$:
<ul>
  <li>Let $V$ denote the number of <strong>sign variations</strong> between consecutive non-zero coefficients of $P(x)$.</li>
  <li>The number of positive real roots $N_+$ of $P(x)$ is either equal to $V$ or less than $V$ by an even non-negative integer:
  $$\mathbf{N_+ = V - 2k, \quad k \in \{0, 1, 2, \dots\}, \quad N_+ \le V}$$</li>
  <li>The number of negative real roots $N_-$ of $P(x)$ is bounded similarly by the sign variations $V_-$ in the polynomial $P(-x)$:
  $$\mathbf{N_- = V_- - 2m, \quad m \in \{0, 1, 2, \dots\}, \quad N_- \le V_-}$$</li>
</ul>
</p>

<h3>2. Proof Outline & Bounding Imaginary Roots</h3>
<p>
Multiplying a polynomial by $(x - r)$ where $r > 0$ increases the number of sign variations by at least 1 and always by an odd number. Since non-real complex roots of real polynomials occur strictly in conjugate pairs (contributing in multiples of 2), the discrepancy between $V$ and $N_+$ must be an even integer.
<strong>Lower Bound on Non-Real Complex Roots:</strong>
Since the total number of complex roots is $n$, the number of non-real roots $N_c$ satisfies:
$$\mathbf{N_c = n - (N_+ + N_-) \ge n - (V + V_-)}$$
</p>
"""
    },
    {
      "id": "sec_4_3",
      "title": "Multiplicity of Roots & Polynomial Derivative GCD",
      "content": r"""
<h3>1. Definition and Derivative Criteria</h3>
<p>
A root $c$ of $P(x)$ has <strong>multiplicity $m \ge 1$</strong> if $(x - c)^m$ divides $P(x)$ but $(x - c)^{m+1}$ does not, so $P(x) = (x - c)^m g(x)$ with $g(c) \ne 0$.<br>
<strong>Theorem:</strong> A number $c$ is a root of $P(x)$ of multiplicity $m$ if and only if:
$$\mathbf{P(c) = P'(c) = P''(c) = \dots = P^{(m-1)}(c) = 0 \quad \text{and} \quad P^{(m)}(c) \ne 0}$$
<em>Proof:</em> Differentiating $P(x) = (x - c)^m g(x)$ by the Product Rule:
$$P'(x) = m(x - c)^{m-1} g(x) + (x - c)^m g'(x) = (x - c)^{m-1} [m g(x) + (x - c) g'(x)]$$
At $x = c$, $(x - c)^{m-1}$ is a factor, so $P'(c) = 0$ for $m \ge 2$. Repeated differentiation continues until order $m-1$. $\blacksquare$
</p>

<h3>2. Square-Free Factorization via Greatest Common Divisor</h3>
<p>
The greatest common divisor of $P(x)$ and its derivative $P'(x)$ isolates all repeated roots:
$$\mathbf{\gcd(P(x), P'(x)) = \prod_{i=1}^k (x - c_i)^{m_i - 1}}$$
The <strong>square-free part</strong> $P_{\text{red}}(x) = \frac{P(x)}{\gcd(P(x), P'(x))}$ has identical roots to $P(x)$ but with all multiplicities reduced to 1, allowing Euclidean algorithm polynomial GCD routines to isolate repeated roots without numerical root-finding!
</p>
"""
    },
    {
      "id": "sec_4_4",
      "title": "Systematic Transformation of Polynomial Equations",
      "content": r"""
<h3>1. Shifting Roots by a Constant $h$</h3>
<p>
To transform an equation $P(x) = 0$ into an equation whose roots are diminished by $h$ (i.e., $y = x - h \implies x = y + h$):
$$P(y + h) = A_n y^n + A_{n-1} y^{n-1} + \dots + A_1 y + A_0 = 0$$
The transformed coefficients $A_k$ are determined efficiently by performing $n$ successive synthetic divisions by $h$:
$$A_k = \frac{P^{(k)}(h)}{k!}$$
</p>

<h3>2. Scaling and Reciprocal Transformations</h3>
<p>
<ul>
  <li><strong>Multiplying Roots by $m$ ($y = mx \implies x = y/m$):</strong>
  $$a_n \left(\frac{y}{m}\right)^n + a_{n-1}\left(\frac{y}{m}\right)^{n-1} + \dots + a_0 = 0 \iff a_n y^n + m a_{n-1} y^{n-1} + m^2 a_{n-2} y^{n-2} + \dots + m^n a_0 = 0$$</li>
  <li><strong>Reciprocal Roots ($y = 1/x \implies x = 1/y$):</strong>
  $$a_n \left(\frac{1}{y}\right)^n + \dots + a_0 = 0 \iff a_0 y^n + a_1 y^{n-1} + \dots + a_{n-1} y + a_n = 0$$
  This simply reverses the order of the original coefficients!</li>
</ul>
</p>
"""
    },
    {
      "id": "sec_4_5",
      "title": "Removal of Terms & Reciprocal Equations",
      "content": r"""
<h3>1. Eliminating the Second Term (Tschirnhaus Shift)</h3>
<p>
Given $a_0 x^n + a_1 x^{n-1} + \dots + a_n = 0$, shifting roots by $x = y + h$:
$$a_0 (y + h)^n + a_1 (y + h)^{n-1} + \dots = a_0 [y^n + n h y^{n-1} + \dots] + a_1 [y^{n-1} + \dots] = 0$$
The coefficient of $y^{n-1}$ is $n a_0 h + a_1$. Setting this to zero yields:
$$\mathbf{h = -\frac{a_1}{n a_0}}$$
This canonical shift removes the degree $n-1$ term, reducing any general cubic $a x^3 + b x^2 + c x + d = 0$ to the depressed cubic $y^3 + p y + q = 0$!
</p>

<h3>2. Reciprocal Equations of First and Second Class</h3>
<p>
An equation is <strong>reciprocal</strong> if substituting $x \to 1/x$ leaves the equation unchanged:
$$a_k = a_{n-k} \quad (\text{Standard Class}) \qquad \text{or} \qquad a_k = -a_{n-k} \quad (\text{Second Class})$$
<strong>Solution Strategy:</strong>
<ul>
  <li>If degree $n$ is odd, $x = -1$ (Class 1) or $x = 1$ (Class 2) is always a root. Factoring out $(x \pm 1)$ reduces the equation to an even-degree reciprocal equation.</li>
  <li>For an even degree reciprocal equation $a x^4 + b x^3 + c x^2 + b x + a = 0$, divide by $x^2$:
  $$a\left(x^2 + \frac{1}{x^2}\right) + b\left(x + \frac{1}{x}\right) + c = 0$$
  Substituting $z = x + \frac{1}{x} \implies x^2 + \frac{1}{x^2} = z^2 - 2$ reduces the quartic to a quadratic in $z$:
  $$\mathbf{a(z^2 - 2) + bz + c = 0}$$
  Solving for $z$ and then solving $x^2 - zx + 1 = 0$ yields all roots!</li>
</ul>
</p>
"""
    }
  ],
  "simulation": {
    "sim_id": "algebra-descartes-multiplicity-sim",
    "title": "Interactive Descartes Sign Variations & Root Multiplicity Inspector",
    "description": "Examine polynomial sign changes, live Descartes upper bounds on positive/negative real roots, and inspect root multiplicity by visualizing simultaneous tangent touching points where P(x) = 0 and P'(x) = 0."
  },
  "problems": [
    {
      "difficulty": "Tier 1: Foundational",
      "difficultyLabel": "Foundational Mechanics",
      "title": "Example 4.1: Horner's Synthetic Division & Remainder Evaluation",
      "statement": r"Use Horner's synthetic division algorithm to divide $P(x) = 2x^4 - 5x^3 + 3x^2 - 7x + 12$ by $x - 3$. State the quotient polynomial $Q(x)$ and the exact remainder $R = P(3)$.",
      "steps": [
        {
          "step": "Step 1: Set Up the Synthetic Division Table",
          "math": r"\begin{array}{c|rrrrr} 3 & 2 & -5 & 3 & -7 & 12 \\ & & 6 & 3 & 18 & 33 \\ \hline & 2 & 1 & 6 & 11 & 45 \end{array}",
          "explanation": "Multiply each accumulated entry by $c = 3$ and add to the column above."
        },
        {
          "step": "Step 2: Read Off the Coefficients",
          "math": r"b_3 = 2, \quad b_2 = 1, \quad b_1 = 6, \quad b_0 = 11, \quad R = 45",
          "explanation": "The bottom row supplies quotient polynomial coefficients and the terminal remainder."
        },
        {
          "step": "Step 3: Construct the Factorization",
          "math": r"Q(x) = 2x^3 + x^2 + 6x + 11 \\ P(x) = (x - 3)(2x^3 + x^2 + 6x + 11) + 45",
          "explanation": "Verify by checking $P(3) = 2(81) - 5(27) + 3(9) - 7(3) + 12 = 162 - 135 + 27 - 21 + 12 = 45$."
        }
      ],
      "answer": r"Q(x) = 2x^3 + x^2 + 6x + 11; \quad R = P(3) = 45."
    },
    {
      "difficulty": "Tier 2: Intermediate Exam",
      "difficultyLabel": "Intermediate University Exam",
      "title": "Example 4.2: Descartes' Sign Analysis of Higher-Degree Polynomial",
      "statement": r"Apply Descartes' Rule of Signs to $P(x) = x^7 - 3x^4 + 2x^3 - x + 5 = 0$. Determine: (a) Maximum number of positive real roots. (b) Maximum number of negative real roots. (c) Minimum number of non-real complex roots.",
      "steps": [
        {
          "step": "Step 1: Count Sign Variations in P(x)",
          "math": r"\text{Coefficients of } P(x): \quad +1, \; -3, \; +2, \; -1, \; +5 \\ \text{Signs: } (+, -, +, -, +) \implies V = 4 \text{ sign changes}",
          "explanation": "There are 4 transitions between consecutive non-zero coefficients."
        },
        {
          "step": "Step 2: Determine Possible Positive Real Roots N₊",
          "math": r"N_+ \in \{4, 2, 0\}",
          "explanation": "By Descartes' rule, $N_+$ is 4 or less by an even integer."
        },
        {
          "step": "Step 3: Count Sign Variations in P(-x)",
          "math": r"P(-x) = (-x)^7 - 3(-x)^4 + 2(-x)^3 - (-x) + 5 = -x^7 - 3x^4 - 2x^3 + x + 5 \\ \text{Signs: } (-, -, -, +, +) \implies V_- = 1 \text{ sign change} \\ N_- = 1",
          "explanation": "Because $V_- = 1$, there is exactly 1 negative real root."
        },
        {
          "step": "Step 4: Bound Non-Real Complex Roots",
          "math": r"\text{Total degree } n = 7. \\ \text{If } N_+ = 4: \quad N_c = 7 - (4 + 1) = 2 \\ \text{If } N_+ = 2: \quad N_c = 7 - (2 + 1) = 4 \\ \text{If } N_+ = 0: \quad N_c = 7 - (0 + 1) = 6 \\ \min(N_c) = 2 \text{ complex roots}",
          "explanation": "Since $N_+ \le 4$ and $N_- = 1$, the polynomial must have at least 2 non-real complex roots (and may have up to 6)."
        }
      ],
      "answer": r"\text{Positive roots: } N_+ \in \{0, 2, 4\}; \quad \text{Negative roots: } N_- = 1; \quad \text{Complex roots: } N_c \in \{2, 4, 6\} \implies \text{At least 2 complex conjugate roots}."
    },
    {
      "difficulty": "Tier 3: Honors / Proof Challenge",
      "difficultyLabel": "Honors / Proof Challenge",
      "title": "Example 4.3: Complete Analytical Solution of a Reciprocal Sextic Equation",
      "statement": r"Solve the reciprocal equation $2x^6 - 9x^5 + 14x^4 - 14x^3 + 14x^2 - 9x + 2 = 0$ by reducing it to a cubic equation in $z = x + \frac{1}{x}$.",
      "steps": [
        {
          "step": "Step 1: Divide by x³ and Group Symmetric Terms",
          "math": r"\text{Divide by } x^3 \ne 0: \\ 2\left(x^3 + \frac{1}{x^3}\right) - 9\left(x^2 + \frac{1}{x^2}\right) + 14\left(x + \frac{1}{x}\right) - 14 = 0",
          "explanation": "Pair equidistant symmetric powers from both ends."
        },
        {
          "step": "Step 2: Express Powers in Terms of z = x + 1/x",
          "math": r"x + \frac{1}{x} = z \\ x^2 + \frac{1}{x^2} = z^2 - 2 \\ x^3 + \frac{1}{x^3} = z^3 - 3z \\ 2(z^3 - 3z) - 9(z^2 - 2) + 14z - 14 = 0 \\ 2z^3 - 6z - 9z^2 + 18 + 14z - 14 = 0 \\ 2z^3 - 9z^2 + 8z + 4 = 0",
          "explanation": "Substitute power reductions to yield a reduced cubic polynomial in $z$."
        },
        {
          "step": "Step 3: Factor the Cubic in z",
          "math": r"\text{Testing integer roots: at } z = 2: \quad 2(8) - 9(4) + 8(2) + 4 = 16 - 36 + 16 + 4 = 0 \quad \checkmark \\ \text{Synthetic division gives: } (z - 2)(2z^2 - 5z - 2) = 0 \\ z_1 = 2, \quad z_{2,3} = \frac{5 \pm \sqrt{25 - 4(2)(-2)}}{4} = \frac{5 \pm \sqrt{41}}{4}",
          "explanation": "Factor $(z - 2)$ out and apply the quadratic formula."
        },
        {
          "step": "Step 4: Solve for x from Each z",
          "math": r"\text{For } z = 2: \quad x + \frac{1}{x} = 2 \iff x^2 - 2x + 1 = 0 \implies (x - 1)^2 = 0 \implies x = 1 \text{ (double root)} \\ \text{For } z = \frac{5 \pm \sqrt{41}}{4}: \quad x^2 - z x + 1 = 0 \implies x = \frac{z \pm \sqrt{z^2 - 4}}{2}",
          "explanation": "Each value of $z$ yields two reciprocal roots for $x$."
        }
      ],
      "answer": r"x = 1 \text{ (multiplicity 2)}, \quad \text{and } x = \frac{z \pm \sqrt{z^2 - 4}}{2} \text{ where } z = \frac{5 \pm \sqrt{41}}{4}."
    }
  ]
}

with open("algebra_u3.json", "w", encoding="utf-8") as f:
    json.dump(u3, f, indent=2, ensure_ascii=False)
print("algebra_u3.json written successfully!")

with open("algebra_u4.json", "w", encoding="utf-8") as f:
    json.dump(u4, f, indent=2, ensure_ascii=False)
print("algebra_u4.json written successfully!")
