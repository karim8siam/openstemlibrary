import json

print("Building Calculus I: Units 1 & 2...")

# ==========================================
# UNIT 1: FOUNDATIONS OF FUNCTIONS & GRAPHS
# ==========================================
u1_sections = [
    {
        "id": "u1-sec1",
        "title": "The Real Number System, Sets, Intervals & The Function Concept",
        "content": r"""<h4>1. The Real Number Continuum $\mathbb{R}$ & Set Notation</h4>
<p>The foundation of all single-variable real analysis and calculus is the set of real numbers $\mathbb{R}$, equipped with the standard algebraic operations of addition and multiplication, satisfying the field axioms, order axioms, and the <strong>Completeness Axiom</strong> (every non-empty subset of $\mathbb{R}$ bounded above has a least upper bound or supremum in $\mathbb{R}$).</p>
<p>Subsets of $\mathbb{R}$ are frequently represented using interval notation:</p>
<div class="math-display">
$$\begin{aligned}
\text{Open Interval: } & (a, b) = \{ x \in \mathbb{R} : a < x < b \} \\
\text{Closed Interval: } & [a, b] = \{ x \in \mathbb{R} : a \le x \le b \} \\
\text{Half-Open Intervals: } & [a, b) = \{ x \in \mathbb{R} : a \le x < b \}, \quad (a, b] = \{ x \in \mathbb{R} : a < x \le b \} \\
\text{Infinite Rays: } & [a, \infty) = \{ x \in \mathbb{R} : x \ge a \}, \quad (-\infty, b) = \{ x \in \mathbb{R} : x < b \}
\end{aligned}$$
</div>

<h4>2. Formal Definition of a Real Function</h4>
<div class="math-display">
$$\mathbf{\text{Definition (Function): A function } f: X \to Y \text{ from a set } X \subseteq \mathbb{R} \text{ (domain) to } Y \subseteq \mathbb{R} \text{ (codomain) is a rule that assigns to each } x \in X \text{ exactly one element } f(x) \in Y.}$$
</div>
<p>The <strong>Range</strong> (or image) of $f$ is the set of all attained values:</p>
<div class="math-display">
$$\operatorname{Range}(f) = \{ y \in Y : \exists x \in X \text{ such that } f(x) = y \} = f(X)$$
</div>

<h4>3. The Natural Domain & The Vertical Line Test</h4>
<p>Unless explicitly restricted, the <em>natural domain</em> of a function defined by an algebraic expression is the largest subset of $\mathbb{R}$ for which the expression produces a well-defined real number. In single-variable calculus, two foundational constraints govern natural domains:</p>
<ol>
  <li><strong>Division by Zero:</strong> Denominators cannot equal zero ($Q(x) \ne 0$).</li>
  <li><strong>Even Roots of Negative Numbers:</strong> For $\sqrt[2n]{g(x)}$, we require $g(x) \ge 0$.</li>
</ol>
<p><strong>The Vertical Line Test:</strong> A curve in the Cartesian plane $\mathbb{R}^2$ represents the graph of a function $y = f(x)$ if and only if no vertical line $x = c$ intersects the curve at more than one point. If a vertical line intersects at two or more points, a single input would map to multiple outputs, violating single-valued functionality.</p>"""
    },
    {
        "id": "u1-sec2",
        "title": "Polynomial & Rational Functions: Degrees, Roots & Asymptotic Behavior",
        "content": r"""<h4>1. Polynomial Functions</h4>
<p>A <strong>polynomial function</strong> of degree $n \in \mathbb{N}_0$ with real coefficients $a_n, a_{n-1}, \dots, a_0$ ($a_n \ne 0$) is defined for all $x \in \mathbb{R}$ by:</p>
<div class="math-display">
$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0 = \sum_{k=0}^n a_k x^k$$
</div>
<p>By the Fundamental Theorem of Algebra, a degree-$n$ polynomial has exactly $n$ complex roots (counting multiplicity), and at most $n$ distinct real roots. The end behavior of $P(x)$ as $x \to \pm\infty$ is strictly governed by its leading monomial term $a_n x^n$:</p>
<div class="math-display">
$$\lim_{x \to \pm\infty} P(x) = \lim_{x \to \pm\infty} a_n x^n \left( 1 + \frac{a_{n-1}}{a_n x} + \dots + \frac{a_0}{a_n x^n} \right) = \lim_{x \to \pm\infty} a_n x^n$$
</div>

<h4>2. Rational Functions & Asymptotes</h4>
<p>A <strong>rational function</strong> is a ratio of two polynomials $R(x) = \frac{P(x)}{Q(x)}$ where $Q(x) \not\equiv 0$. Its natural domain is $\operatorname{Dom}(R) = \{ x \in \mathbb{R} : Q(x) \ne 0 \}$.</p>
<p>Let $P(x) = a_n x^n + \dots$ and $Q(x) = b_m x^m + \dots$ with $a_n \ne 0, b_m \ne 0$:</p>
<ul>
  <li><strong>Vertical Asymptotes:</strong> If $x = c$ is a root of $Q(x)$ such that $(x - c)$ has higher multiplicity in $Q(x)$ than in $P(x)$, then $\lim_{x \to c} |R(x)| = \infty$, producing a vertical asymptote at $x = c$. If $(x - c)$ cancels completely, $x = c$ is a <em>removable discontinuity (hole)</em>.</li>
  <li><strong>Horizontal Asymptotes:</strong>
    <ul>
      <li>If $n < m$: The line $y = 0$ is a horizontal asymptote ($\lim_{x \to \pm\infty} R(x) = 0$).</li>
      <li>If $n = m$: The horizontal line $y = \frac{a_n}{b_m}$ is an asymptote ($\lim_{x \to \pm\infty} R(x) = a_n / b_m$).</li>
      <li>If $n > m$: No horizontal asymptote exists.</li>
    </ul>
  </li>
  <li><strong>Oblique (Slant) Asymptotes:</strong> If $n = m + 1$, polynomial long division yields $R(x) = (m_0 x + c_0) + \frac{r(x)}{Q(x)}$ with $\deg(r) < m$. The line $y = m_0 x + c_0$ is an oblique asymptote as $x \to \pm\infty$.</li>
</ul>"""
    },
    {
        "id": "u1-sec3",
        "title": "Piecewise Functions, Absolute Value Mechanics & Step Operators",
        "content": r"""<h4>1. Piecewise-Defined Functions</h4>
<p>A function defined by different analytical rules on disjoint sub-intervals of its domain is called a <strong>piecewise-defined function</strong>:</p>
<div class="math-display">
$$f(x) = \begin{cases}
g_1(x), & x \in I_1 \\
g_2(x), & x \in I_2 \\
\vdots & \vdots \\
g_k(x), & x \in I_k
\end{cases}$$
</div>

<h4>2. The Absolute Value (Modulus) Function</h4>
<p>The absolute value function $|x|: \mathbb{R} \to [0, \infty)$ is defined algebraically as:</p>
<div class="math-display">
$$|x| = \sqrt{x^2} = \begin{cases}
x, & x \ge 0 \\
-x, & x < 0
\end{cases}$$
</div>
<p><strong>Fundamental Properties of Absolute Value:</strong></p>
<ol>
  <li><strong>Non-negativity:</strong> $|x| \ge 0$, with $|x| = 0 \iff x = 0$.</li>
  <li><strong>Multiplicativity:</strong> $|x y| = |x| |y|$ and $\left|\frac{x}{y}\right| = \frac{|x|}{|y|}$ for $y \ne 0$.</li>
  <li><strong>The Triangle Inequality:</strong> For all $x, y \in \mathbb{R}$,
    <div class="math-display">
    $$|x + y| \le |x| + |y|$$
    </div>
  </li>
  <li><strong>The Reverse Triangle Inequality:</strong>
    <div class="math-display">
    $$||x| - |y|| \le |x - y|$$
    </div>
  </li>
  <li><strong>Interval Equivalence:</strong> For any $c > 0$, $|x - a| < c \iff a - c < x < a + c$.</li>
</ol>

<h4>3. Step, Signum & Floor Functions</h4>
<p>The <strong>signum function</strong> $\operatorname{sgn}(x)$ extracts the algebraic sign of $x$:</p>
<div class="math-display">
$$\operatorname{sgn}(x) = \begin{cases}
+1, & x > 0 \\
0, & x = 0 \\
-1, & x < 0
\end{cases} = \frac{x}{|x|} \quad (x \ne 0)$$
</div>
<p>The <strong>floor function</strong> (greatest integer function) $\lfloor x \rfloor$ maps $x$ to the unique integer $k \in \mathbb{Z}$ satisfying $k \le x < k + 1$. The ceiling function $\lceil x \rceil$ satisfies $k - 1 < x \le k$.</p>"""
    },
    {
        "id": "u1-sec4",
        "title": "Geometric Transformations, Symmetry Tests & Monotonicity",
        "content": r"""<h4>1. Rigid and Non-Rigid Transformations</h4>
<p>Given the base graph $y = f(x)$, algebraic modifications to the argument or output produce exact geometric transformations in $\mathbb{R}^2$ ($c > 0$):</p>
<ul>
  <li><strong>Vertical Shift:</strong> $y = f(x) + c$ shifts the graph upward by $c$ units; $y = f(x) - c$ shifts downward.</li>
  <li><strong>Horizontal Shift:</strong> $y = f(x - c)$ shifts the graph to the right by $c$ units; $y = f(x + c)$ shifts to the left.</li>
  <li><strong>Vertical Scaling & Reflection:</strong> $y = a f(x)$ stretches vertically by factor $|a|$ if $|a| > 1$, compresses if $0 < |a| < 1$, and reflects across the $x$-axis if $a < 0$.</li>
  <li><strong>Horizontal Scaling & Reflection:</strong> $y = f(b x)$ compresses horizontally by factor $1/|b|$ if $|b| > 1$, stretches if $0 < |b| < 1$, and reflects across the $y$-axis if $b < 0$.</li>
</ul>

<h4>2. Algebraic Symmetry Tests: Even and Odd Functions</h4>
<div class="math-display">
$$\begin{aligned}
\mathbf{\text{Even Function: }} & f(-x) = f(x) \quad \forall x \in \operatorname{Dom}(f) \iff \text{Symmetric with respect to the } y\text{-axis} \\
\mathbf{\text{Odd Function: }} & f(-x) = -f(x) \quad \forall x \in \operatorname{Dom}(f) \iff \text{Symmetric with respect to the origin } (0,0)
\end{aligned}$$
</div>
<p><strong>Decomposition Theorem:</strong> Every function $f: \mathbb{R} \to \mathbb{R}$ whose domain is symmetric about the origin can be uniquely decomposed into the sum of an even function $f_{\text{even}}$ and an odd function $f_{\text{odd}}$:</p>
<div class="math-display">
$$f(x) = f_{\text{even}}(x) + f_{\text{odd}}(x) = \frac{f(x) + f(-x)}{2} + \frac{f(x) - f(-x)}{2}$$
</div>

<h4>3. Monotonicity on Intervals</h4>
<p>Let $I \subseteq \operatorname{Dom}(f)$ be an interval. We define:</p>
<ul>
  <li><strong>Strictly Increasing:</strong> $\forall x_1, x_2 \in I$, $x_1 < x_2 \implies f(x_1) < f(x_2)$.</li>
  <li><strong>Strictly Decreasing:</strong> $\forall x_1, x_2 \in I$, $x_1 < x_2 \implies f(x_1) > f(x_2)$.</li>
  <li><strong>Strictly Monotonic:</strong> A function that is either strictly increasing on $I$ or strictly decreasing on $I$. Strictly monotonic functions are guaranteed to be one-to-one (injective) on $I$.</li>
</ul>"""
    },
    {
        "id": "u1-sec5",
        "title": "Algebra of Functions, Composition & Invertibility",
        "content": r"""<h4>1. Composition of Functions</h4>
<p>Given two functions $f: Y \to Z$ and $g: X \to Y$, the <strong>composite function</strong> $(f \circ g): X \to Z$ is defined by:</p>
<div class="math-display">
$$(f \circ g)(x) = f(g(x))$$
</div>
<p>The natural domain of $f \circ g$ consists of all $x$ in the domain of $g$ whose outputs $g(x)$ lie in the domain of $f$:</p>
<div class="math-display">
$$\operatorname{Dom}(f \circ g) = \{ x \in \operatorname{Dom}(g) : g(x) \in \operatorname{Dom}(f) \}$$
</div>
<p>Note that function composition is generally <strong>non-commutative</strong>: $f \circ g \ne g \circ f$ in general, though it is always associative: $f \circ (g \circ h) = (f \circ g) \circ h$.</p>

<h4>2. Invertibility: Injectivity, Surjectivity & Bijectivity</h4>
<div class="math-display">
$$\begin{aligned}
\mathbf{\text{Injective (One-to-One): }} & f(x_1) = f(x_2) \implies x_1 = x_2 \quad (\text{Horizontal Line Test}) \\
\mathbf{\text{Surjective (Onto): }} & \forall y \in Y, \, \exists x \in X \text{ such that } f(x) = y \quad (\operatorname{Range}(f) = Y) \\
\mathbf{\text{Bijective: }} & f \text{ is both injective and surjective}
\end{aligned}$$
</div>
<p><strong>Theorem (Existence of Inverse Function):</strong> A function $f: X \to Y$ possesses a two-sided inverse function $f^{-1}: Y \to X$ if and only if $f$ is a bijection. When $f^{-1}$ exists, it satisfies:</p>
<div class="math-display">
$$(f^{-1} \circ f)(x) = x \quad \forall x \in X, \qquad (f \circ f^{-1})(y) = y \quad \forall y \in Y$$
</div>
<p>Geometrically, the point $(a, b)$ lies on the graph of $y = f(x)$ if and only if $(b, a)$ lies on the graph of $y = f^{-1}(x)$. Thus, the graph of $f^{-1}$ is the exact reflection of the graph of $f$ across the principal diagonal line $y = x$.</p>"""
    }
]

u1_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Natural Domain & Range of Radical Rational Functions",
        "statement": r"Find the exact natural domain and range of the function $f(x) = \sqrt{\frac{4 - x^2}{x^2 - 1}}$. Express both sets in rigorous interval notation.",
        "steps": [
            {
                "step": "Step 1: Formulate Domain Inequality Constraints",
                "math": r"\frac{4 - x^2}{x^2 - 1} \ge 0 \quad \text{and} \quad x^2 - 1 \ne 0",
                "explanation": "Because the square root is defined only for non-negative radicands, the quotient must be $\ge 0$. Simultaneously, the denominator cannot vanish."
            },
            {
                "step": "Step 2: Factor Polynomials and Find Critical Zeros",
                "math": r"\frac{(2 - x)(2 + x)}{(x - 1)(x + 1)} \ge 0",
                "explanation": "The critical boundary points where the sign of the rational expression can change are $x = -2, -1, 1, 2$."
            },
            {
                "step": "Step 3: Sign Table Analysis across Sub-Intervals",
                "math": r"""\begin{array}{c|c|c|c|c|c}
\text{Interval} & (-\infty, -2) & (-2, -1) & (-1, 1) & (1, 2) & (2, \infty) \\
\hline
4 - x^2 & - & + & + & + & - \\
x^2 - 1 & + & + & - & + & + \\
\hline
\text{Quotient} & - & + & - & + & -
\end{array}""",
                "explanation": "The quotient is strictly non-negative on $[-2, -1)$ and $(1, 2]$. Notice that $x = \pm 1$ must be strictly excluded due to denominator zero."
            },
            {
                "step": "Step 4: Determine the Range",
                "math": r"u = \frac{4 - x^2}{x^2 - 1} \implies u \in [0, \infty) \implies \operatorname{Range}(f) = [0, \infty)",
                "explanation": "At $x = \pm 2$, the radicand is $0$, giving $f(\pm 2) = 0$. As $x \to 1^+$ or $x \to -1^-$, the denominator approaches $0^+$ while the numerator approaches $3$, driving $u \to \infty$. Hence, the range is all non-negative real numbers."
            }
        ],
        "answer": r"\operatorname{Dom}(f) = [-2, -1) \cup (1, 2], \qquad \operatorname{Range}(f) = [0, \infty)"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Constructing and Verifying the Algebraic Inverse of a Fractional Linear Function",
        "statement": r"Given the Möbius fractional linear transformation $f(x) = \frac{3x + 5}{2x - 7}$: (a) Determine the natural domain and range of $f$. (b) Prove that $f$ is strictly injective on its domain. (c) Derive an explicit formula for $f^{-1}(x)$. (d) Verify the cancellation identities $(f \circ f^{-1})(x) = x$ and $(f^{-1} \circ f)(x) = x$.",
        "steps": [
            {
                "step": "Step 1: Domain and Range Determination",
                "math": r"\operatorname{Dom}(f) = \mathbb{R} \setminus \{7/2\}, \qquad \lim_{x \to \pm\infty} f(x) = \frac{3}{2} \implies \operatorname{Range}(f) = \mathbb{R} \setminus \{3/2\}",
                "explanation": "The denominator $2x - 7 = 0 \implies x = 7/2$. The horizontal asymptote is $y = 3/2$, which is never attained for any finite real $x$."
            },
            {
                "step": "Step 2: Rigorous Proof of Injectivity",
                "math": r"\frac{3x_1 + 5}{2x_1 - 7} = \frac{3x_2 + 5}{2x_2 - 7} \implies (3x_1 + 5)(2x_2 - 7) = (3x_2 + 5)(2x_1 - 7)",
                "explanation": "Cross-multiplying: $6x_1 x_2 - 21 x_1 + 10 x_2 - 35 = 6x_1 x_2 - 21 x_2 + 10 x_1 - 35$. Canceling like terms yields $-31 x_1 = -31 x_2 \implies x_1 = x_2$. Thus $f$ is strictly injective."
            },
            {
                "step": "Step 3: Algebraic Inversion",
                "math": r"y = \frac{3x + 5}{2x - 7} \implies y(2x - 7) = 3x + 5 \implies x(2y - 3) = 7y + 5 \implies x = \frac{7y + 5}{2y - 3}",
                "explanation": "Interchanging variables yields the inverse function $f^{-1}(x) = \frac{7x + 5}{2x - 3}$ with domain $\mathbb{R} \setminus \{3/2\}$."
            },
            {
                "step": "Step 4: Direct Verification of Cancellation Identity",
                "math": r"f(f^{-1}(x)) = \frac{3\left(\frac{7x+5}{2x-3}\right) + 5}{2\left(\frac{7x+5}{2x-3}\right) - 7} = \frac{(21x + 15) + 5(2x - 3)}{(14x + 10) - 7(2x - 3)} = \frac{31x}{31} = x",
                "explanation": "Both numerator and denominator simplify identically, confirming that $f(f^{-1}(x)) = x$ identically."
            }
        ],
        "answer": r"f^{-1}(x) = \frac{7x + 5}{2x - 3}, \quad \operatorname{Dom}(f^{-1}) = \mathbb{R} \setminus \{3/2\}, \quad \operatorname{Range}(f^{-1}) = \mathbb{R} \setminus \{7/2\}"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Even-Odd Symmetry Decomposition & Functional Equation Analysis",
        "statement": r"Let $f: \mathbb{R} \to \mathbb{R}$ satisfy the functional relation $f(x + y) + f(x - y) = 2f(x)f(y)$ for all $x, y \in \mathbb{R}$ (d'Alembert's functional equation) with $f$ not identically zero. (a) Prove that $f(0) = 1$. (b) Prove that $f$ must be an even function: $f(-x) = f(x)$. (c) If in addition $f(x)$ is decomposed into $f(x) = f_e(x) + f_o(x)$, show that $f_o(x) \equiv 0$.",
        "steps": [
            {
                "step": "Step 1: Evaluate at $x = 0$ to Determine $f(0)$",
                "math": r"f(0 + y) + f(0 - y) = 2f(0)f(y) \implies f(y) + f(-y) = 2f(0)f(y)",
                "explanation": "Setting $y = 0$: $f(x) + f(x) = 2f(x)f(0) \implies 2f(x) = 2f(x)f(0) \implies 2f(x)[1 - f(0)] = 0$. Since $f$ is not identically zero, there exists $x_0$ with $f(x_0) \ne 0$, forcing $f(0) = 1$."
            },
            {
                "step": "Step 2: Prove $f$ is Even",
                "math": r"f(y) + f(-y) = 2(1)f(y) = 2f(y) \implies f(-y) = 2f(y) - f(y) = f(y)",
                "explanation": "Since $f(-y) = f(y)$ holds for every $y \in \mathbb{R}$, $f$ is an even function."
            },
            {
                "step": "Step 3: Verification of Odd Component Vanishing",
                "math": r"f_o(x) = \frac{f(x) - f(-x)}{2} = \frac{f(x) - f(x)}{2} = 0 \quad \forall x \in \mathbb{R}",
                "explanation": "Because $f(-x) = f(x)$ globally, the unique odd part in the canonical even-odd decomposition $f(x) = f_e(x) + f_o(x)$ vanishes identically, leaving $f(x) = f_e(x)$."
            }
        ],
        "answer": r"f(0) = 1, \quad f(-x) = f(x) \text{ (strictly even)}, \quad f_o(x) \equiv 0"
    }
]

u1_data = {
    "unitNumber": 1,
    "number": 1,
    "title": "Foundations of Functions, Graphs, Symmetries & Inverses",
    "description": "Comprehensive foundations of single-variable mathematics: real number continuum R, natural domains and ranges, polynomial degrees and asymptotes, absolute value mechanics, triangle inequalities, geometric graph transformations, even/odd symmetries, and bijective inverse functions.",
    "sections": u1_sections,
    "problems": u1_problems
}

with open("calc1_u1.json", "w", encoding="utf-8") as f:
    json.dump(u1_data, f, indent=2)
print("calc1_u1.json created successfully!")

# ==========================================================
# UNIT 2: TRANSCENDENTAL FUNCTIONS & HYPERBOLIC TRIGONOMETRY
# ==========================================================
u2_sections = [
    {
        "id": "u2-sec1",
        "title": "Exponential Functions, Euler's Number e & Logarithmic Foundations",
        "content": r"""<h4>1. Exponential Functions</h4>
<p>For a fixed positive base $a > 0$ with $a \ne 1$, the <strong>exponential function</strong> with base $a$ is defined for all $x \in \mathbb{R}$ by $f(x) = a^x$.</p>
<p><strong>Fundamental Exponential Laws:</strong> For all $x, y \in \mathbb{R}$ and $a, b > 0$:</p>
<div class="math-display">
$$a^{x+y} = a^x a^y, \qquad a^{x-y} = \frac{a^x}{a^y}, \qquad (a^x)^y = a^{x y}, \qquad (a b)^x = a^x b^x$$
</div>
<p>The function is strictly positive: $\operatorname{Range}(a^x) = (0, \infty)$. It is strictly increasing if $a > 1$, and strictly decreasing if $0 < a < 1$.</p>

<h4>2. Euler's Number $e$ & The Natural Exponential</h4>
<p>The base of the natural exponential function, Euler's number $e \approx 2.718281828459...$, is uniquely defined by the fundamental limit:</p>
<div class="math-display">
$$e = \lim_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n = \sum_{k=0}^\infty \frac{1}{k!} = 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \dots$$
</div>
<p>Geometrically, $y = e^x$ is the unique exponential curve whose tangent line at the $y$-intercept $(0, 1)$ has a slope of exactly $1$.</p>

<h4>3. Logarithmic Functions</h4>
<p>Because $f(x) = a^x$ is strictly monotonic on $\mathbb{R}$, it is a bijection from $\mathbb{R}$ to $(0, \infty)$. Its inverse function is the <strong>logarithm to base $a$</strong>:</p>
<div class="math-display">
$$y = \log_a(x) \iff a^y = x \quad (x > 0)$$
</div>
<p>The inverse of the natural exponential $e^x$ is the <strong>natural logarithm</strong> $\ln(x) = \log_e(x)$:</p>
<div class="math-display">
$$\ln(e^x) = x \quad \forall x \in \mathbb{R}, \qquad e^{\ln(x)} = x \quad \forall x > 0$$
</div>
<p><strong>Logarithmic Properties & Change of Base:</strong></p>
<div class="math-display">
$$\ln(x y) = \ln(x) + \ln(y), \quad \ln(x/y) = \ln(x) - \ln(y), \quad \ln(x^r) = r \ln(x), \quad \log_a(x) = \frac{\ln(x)}{\ln(a)}$$
</div>"""
    },
    {
        "id": "u2-sec2",
        "title": "Trigonometric Functions, Exact Identities & Unit Circle Geometry",
        "content": r"""<h4>1. The Unit Circle Definition of Trigonometric Functions</h4>
<p>In analytical calculus, angles are measured strictly in <strong>radians</strong>. Let $(x, y)$ be the terminal coordinates of an angle $\theta \in \mathbb{R}$ on the unit circle $x^2 + y^2 = 1$ measured counterclockwise from $(1, 0)$:</p>
<div class="math-display">
$$\cos\theta = x, \qquad \sin\theta = y, \qquad \tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{y}{x} \quad (x \ne 0)$$
</div>
<p>The reciprocal functions are $\sec\theta = 1/\cos\theta$, $\csc\theta = 1/\sin\theta$, and $\cot\theta = 1/\tan\theta = \cos\theta/\sin\theta$.</p>

<h4>2. Fundamental Trigonometric Identities</h4>
<p>From the Pythagorean theorem $x^2 + y^2 = 1$ on the unit circle:</p>
<div class="math-display">
$$\sin^2\theta + \cos^2\theta = 1, \qquad 1 + \tan^2\theta = \sec^2\theta, \qquad 1 + \cot^2\theta = \csc^2\theta$$
</div>
<p><strong>Angle Addition & Double-Angle Formulas:</strong></p>
<div class="math-display">
$$\begin{aligned}
\sin(\alpha \pm \beta) &= \sin\alpha \cos\beta \pm \cos\alpha \sin\beta \\
\cos(\alpha \pm \beta) &= \cos\alpha \cos\beta \mp \sin\alpha \sin\beta \\
\sin(2\theta) &= 2\sin\theta\cos\theta \\
\cos(2\theta) &= \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta \\
\tan(\alpha \pm \beta) &= \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}
\end{aligned}$$
</div>
<p><strong>Power-Reduction (Half-Angle) Formulas:</strong> Crucial for integration in calculus:</p>
<div class="math-display">
$$\sin^2\theta = \frac{1 - \cos(2\theta)}{2}, \qquad \cos^2\theta = \frac{1 + \cos(2\theta)}{2}$$
</div>"""
    },
    {
        "id": "u2-sec3",
        "title": "Inverse Trigonometric Functions & Principal Value Branches",
        "content": r"""<h4>1. Restriction of Domains & Principal Branches</h4>
<p>Because trigonometric functions are periodic, they fail the horizontal line test across $\mathbb{R}$. To construct inverses, we restrict each function to a standard <strong>principal interval</strong> on which it is strictly monotonic and surjective onto its range:</p>

<div class="math-display">
$$\begin{array}{l|c|c|l}
\text{Function} & \text{Restricted Domain} & \text{Range} & \text{Inverse Function } f^{-1} \\
\hline
\sin x & [-\pi/2, \pi/2] & [-1, 1] & y = \arcsin x \iff x = \sin y, \quad y \in [-\pi/2, \pi/2] \\
\cos x & [0, \pi] & [-1, 1] & y = \arccos x \iff x = \cos y, \quad y \in [0, \pi] \\
\tan x & (-\pi/2, \pi/2) & (-\infty, \infty) & y = \arctan x \iff x = \tan y, \quad y \in (-\pi/2, \pi/2) \\
\sec x & [0, \pi/2) \cup (\pi/2, \pi] & (-\infty, -1] \cup [1, \infty) & y = \operatorname{arcsec} x \iff x = \sec y
\end{array}$$
</div>

<h4>2. Fundamental Identities of Inverse Trigonometric Functions</h4>
<div class="math-display">
$$\arcsin(x) + \arccos(x) = \frac{\pi}{2} \quad \forall x \in [-1, 1], \qquad \arctan(x) + \operatorname{arccot}(x) = \frac{\pi}{2} \quad \forall x \in \mathbb{R}$$
</div>
<p><strong>Cancellation Cautions:</strong></p>
<div class="math-display">
$$\sin(\arcsin x) = x \quad \forall x \in [-1, 1], \quad \text{but} \quad \arcsin(\sin x) = x \iff x \in [-\pi/2, \pi/2]$$
</div>
<p>For arguments outside the principal range, symmetry must be utilized: e.g., $\arcsin(\sin(5\pi/6)) = \arcsin(1/2) = \pi/6 \ne 5\pi/6$.</p>"""
    },
    {
        "id": "u2-sec4",
        "title": "Hyperbolic Functions: Symmetries, Identities & The Unit Hyperbola",
        "content": r"""<h4>1. Formal Definitions of Hyperbolic Functions</h4>
<p>The <strong>hyperbolic functions</strong> are defined as the symmetric and antisymmetric linear combinations of the exponential functions $e^x$ and $e^{-x}$:</p>
<div class="math-display">
$$\begin{aligned}
\text{Hyperbolic Sine: } & \sinh x = \frac{e^x - e^{-x}}{2} \quad (\text{Strictly Odd: } \sinh(-x) = -\sinh x) \\
\text{Hyperbolic Cosine: } & \cosh x = \frac{e^x + e^{-x}}{2} \quad (\text{Strictly Even: } \cosh(-x) = \cosh x) \\
\text{Hyperbolic Tangent: } & \tanh x = \frac{\sinh x}{\cosh x} = \frac{e^x - e^{-x}}{e^x + e^{-x}} = \frac{e^{2x} - 1}{e^{2x} + 1}
\end{aligned}$$
</div>
<p>Reciprocals: $\operatorname{sech} x = \frac{1}{\cosh x}$, $\operatorname{csch} x = \frac{1}{\sinh x}$, $\operatorname{coth} x = \frac{\cosh x}{\sinh x}$.</p>

<h4>2. The Fundamental Hyperbolic Identity & The Unit Hyperbola</h4>
<div class="math-display">
$$\cosh^2 x - \sinh^2 x = \left(\frac{e^x + e^{-x}}{2}\right)^2 - \left(\frac{e^x - e^{-x}}{2}\right)^2 = \frac{(e^{2x} + 2 + e^{-2x}) - (e^{2x} - 2 + e^{-2x})}{4} = \frac{4}{4} = 1$$
</div>
<p><strong>Geometric Analogy:</strong> Just as $(\cos t, \sin t)$ parametrizes the unit circle $x^2 + y^2 = 1$, the parametric coordinates $(x, y) = (\cosh t, \sinh t)$ trace the right branch of the unit equilateral hyperbola:</p>
<div class="math-display">
$$x^2 - y^2 = 1 \quad (x \ge 1)$$
</div>
<p><strong>Derived Identities:</strong></p>
<div class="math-display">
$$1 - \tanh^2 x = \operatorname{sech}^2 x, \qquad \coth^2 x - 1 = \operatorname{csch}^2 x$$
$$\sinh(2x) = 2\sinh x\cosh x, \qquad \cosh(2x) = \cosh^2 x + \sinh^2 x = 2\cosh^2 x - 1 = 1 + 2\sinh^2 x$$
</div>"""
    },
    {
        "id": "u2-sec5",
        "title": "Inverse Hyperbolic Functions & Derivation of Explicit Logarithmic Forms",
        "content": r"""<h4>1. Invertibility of Hyperbolic Functions</h4>
<ul>
  <li>$\sinh x$ is strictly increasing on $\mathbb{R}$ with range $\mathbb{R}$. Its inverse $\operatorname{arsinh} x$ is defined for all $x \in \mathbb{R}$.</li>
  <li>$\cosh x$ is even on $\mathbb{R}$ with range $[1, \infty)$. Restricting to $x \ge 0$ yields the principal branch of $\operatorname{arcosh} x$ for $x \ge 1$, with range $[0, \infty)$.</li>
  <li>$\tanh x$ is strictly increasing with range $(-1, 1)$. Its inverse $\operatorname{artanh} x$ is defined on $(-1, 1)$.</li>
</ul>

<h4>2. Rigorous Derivation of Logarithmic Closed Forms</h4>
<p><strong>Theorem:</strong> For all $x \in \mathbb{R}$, $\operatorname{arsinh} x = \ln(x + \sqrt{x^2 + 1})$.</p>
<p><em>Proof:</em> Let $y = \operatorname{arsinh} x$. Then $x = \sinh y = \frac{e^y - e^{-y}}{2}$. Multiplying by $2e^y$ yields:</p>
<div class="math-display">
$$2x e^y = e^{2y} - 1 \implies (e^y)^2 - 2x(e^y) - 1 = 0$$
</div>
<p>This is a quadratic equation in $u = e^y$. By the quadratic formula:</p>
<div class="math-display">
$$e^y = \frac{2x \pm \sqrt{4x^2 - 4(1)(-1)}}{2} = x \pm \sqrt{x^2 + 1}$$
</div>
<p>Since $e^y > 0$ for all real $y$, and $\sqrt{x^2+1} > \sqrt{x^2} = |x| \ge x$, the minus sign yields a strictly negative value $x - \sqrt{x^2+1} < 0$, which is inadmissible. Thus:</p>
<div class="math-display">
$$e^y = x + \sqrt{x^2 + 1} \implies y = \operatorname{arsinh} x = \ln(x + \sqrt{x^2 + 1}) \quad \blacksquare$$
</div>

<p><strong>Complete Logarithmic Catalog:</strong></p>
<div class="math-display">
$$\begin{aligned}
\operatorname{arcosh} x &= \ln\left(x + \sqrt{x^2 - 1}\right), \quad x \ge 1 \\
\operatorname{artanh} x &= \frac{1}{2}\ln\left(\frac{1 + x}{1 - x}\right), \quad -1 < x < 1 \\
\operatorname{arcoth} x &= \frac{1}{2}\ln\left(\frac{x + 1}{x - 1}\right), \quad |x| > 1
\end{aligned}$$
</div>"""
    }
]

u2_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Exact Evaluation of Inverse Trigonometric Expressions",
        "statement": r"Find the exact real values of: (a) $\arcsin\left(\sin\left(\frac{7\pi}{6}\right)\right)$, (b) $\cos\left(2\arcsin\left(-\frac{3}{5}\right)\right)$, and (c) $\tan\left(\arccos\left(\frac{5}{13}\right)\right)$.",
        "steps": [
            {
                "step": "Step 1: Evaluate (a) via Principal Branch Interval",
                "math": r"\sin\left(\frac{7\pi}{6}\right) = -\frac{1}{2} \implies \arcsin\left(-\frac{1}{2}\right) = -\frac{\pi}{6}",
                "explanation": "Because $7\pi/6 \notin [-\pi/2, \pi/2]$, we cannot simply cancel. We evaluate the inner sine first to get $-1/2$, whose principal arcsine value is $-\pi/6$."
            },
            {
                "step": "Step 2: Evaluate (b) via Double-Angle Formula",
                "math": r"\cos(2\theta) = 1 - 2\sin^2\theta \quad \text{where } \theta = \arcsin(-3/5) \implies \sin\theta = -\frac{3}{5}",
                "explanation": "Substitute $\sin\theta$: $\cos(2\theta) = 1 - 2\left(-\frac{3}{5}\right)^2 = 1 - 2\left(\frac{9}{25}\right) = 1 - \frac{18}{25} = \frac{7}{25}$."
            },
            {
                "step": "Step 3: Evaluate (c) via Right Triangle Geometry",
                "math": r"\alpha = \arccos\left(\frac{5}{13}\right) \implies \cos\alpha = \frac{5}{13}, \quad \sin\alpha = \sqrt{1 - (5/13)^2} = \frac{12}{13}",
                "explanation": "Then $\tan\alpha = \frac{\sin\alpha}{\cos\alpha} = \frac{12/13}{5/13} = \frac{12}{5}$."
            }
        ],
        "answer": r"\text{(a) } -\frac{\pi}{6}, \qquad \text{(b) } \frac{7}{25}, \qquad \text{(c) } \frac{12}{5}"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Derivation of the Explicit Logarithmic Formula for Inverse Hyperbolic Tangent",
        "statement": r"Let $y = \operatorname{artanh}(x)$ for $x \in (-1, 1)$. (a) Starting from the definition $\tanh(y) = \frac{e^{2y} - 1}{e^{2y} + 1} = x$, derive the closed logarithmic formula $\operatorname{artanh}(x) = \frac{1}{2}\ln\left(\frac{1 + x}{1 - x}\right)$. (b) Use this formula to compute the exact value of $\operatorname{artanh}(3/5)$ and $\operatorname{artanh}(0)$.",
        "steps": [
            {
                "step": "Step 1: Set up the Inversion Equation",
                "math": r"x = \frac{e^{2y} - 1}{e^{2y} + 1} \implies x(e^{2y} + 1) = e^{2y} - 1",
                "explanation": "Expand and isolate the exponential term $e^{2y}$."
            },
            {
                "step": "Step 2: Solve for $e^{2y}$",
                "math": r"x e^{2y} + x = e^{2y} - 1 \implies 1 + x = e^{2y}(1 - x) \implies e^{2y} = \frac{1 + x}{1 - x}",
                "explanation": "Since $-1 < x < 1$, both $1+x > 0$ and $1-x > 0$, so the ratio is strictly positive."
            },
            {
                "step": "Step 3: Take Natural Logarithms",
                "math": r"2y = \ln\left(\frac{1 + x}{1 - x}\right) \implies y = \operatorname{artanh}(x) = \frac{1}{2}\ln\left(\frac{1 + x}{1 - x}\right)",
                "explanation": "Dividing by 2 yields the exact logarithmic formula."
            },
            {
                "step": "Step 4: Compute Values",
                "math": r"\operatorname{artanh}(3/5) = \frac{1}{2}\ln\left(\frac{1 + 3/5}{1 - 3/5}\right) = \frac{1}{2}\ln\left(\frac{8/5}{2/5}\right) = \frac{1}{2}\ln(4) = \ln(2)",
                "explanation": "For $x = 0$: $\operatorname{artanh}(0) = \frac{1}{2}\ln(1/1) = 0$."
            }
        ],
        "answer": r"\operatorname{artanh}(x) = \frac{1}{2}\ln\left(\frac{1 + x}{1 - x}\right), \qquad \operatorname{artanh}(3/5) = \ln(2), \qquad \operatorname{artanh}(0) = 0"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Hyperbolic Addition Theorem & Ultra-Relativistic Rapidity Invariance",
        "statement": r"In special relativity, the velocity $v$ of a particle is related to its rapidity $\theta \in \mathbb{R}$ by $v/c = \tanh\theta$. (a) Using the definitions of $\sinh$ and $\cosh$, prove the general hyperbolic addition formula: $\tanh(\theta_1 + \theta_2) = \frac{\tanh\theta_1 + \tanh\theta_2}{1 + \tanh\theta_1 \tanh\theta_2}$. (b) Deduce that the relativistic velocity addition law $v_{12} = \frac{v_1 + v_2}{1 + v_1 v_2 / c^2}$ corresponds to the simple linear addition of rapidities: $\theta_{12} = \theta_1 + \theta_2$. (c) Prove that if $v_1 < c$ and $v_2 < c$, then $v_{12} < c$ strictly.",
        "steps": [
            {
                "step": "Step 1: Expand $\sinh(\theta_1 + \theta_2)$ and $\cosh(\theta_1 + \theta_2)$",
                "math": r"""\begin{aligned}
\sinh(\theta_1 + \theta_2) &= \sinh\theta_1 \cosh\theta_2 + \cosh\theta_1 \sinh\theta_2 \\
\cosh(\theta_1 + \theta_2) &= \cosh\theta_1 \cosh\theta_2 + \sinh\theta_1 \sinh\theta_2
\end{aligned}""",
                "explanation": "Expanding $e^{(\theta_1+\theta_2)} \pm e^{-(\theta_1+\theta_2)}$ directly from definition proves these two addition identities."
            },
            {
                "step": "Step 2: Form the Ratio $\tanh(\theta_1 + \theta_2)$",
                "math": r"\tanh(\theta_1 + \theta_2) = \frac{\sinh\theta_1 \cosh\theta_2 + \cosh\theta_1 \sinh\theta_2}{\cosh\theta_1 \cosh\theta_2 + \sinh\theta_1 \sinh\theta_2} = \frac{\frac{\sinh\theta_1}{\cosh\theta_1} + \frac{\sinh\theta_2}{\cosh\theta_2}}{1 + \frac{\sinh\theta_1\sinh\theta_2}{\cosh\theta_1\cosh\theta_2}} = \frac{\tanh\theta_1 + \tanh\theta_2}{1 + \tanh\theta_1 \tanh\theta_2}",
                "explanation": "Dividing numerator and denominator by $\cosh\theta_1 \cosh\theta_2$ establishes the identity."
            },
            {
                "step": "Step 3: Relate to Velocity Addition and Strict Subluminal Bound",
                "math": r"\frac{v_{12}}{c} = \tanh(\theta_1 + \theta_2) = \frac{v_1/c + v_2/c}{1 + (v_1/c)(v_2/c)} \implies v_{12} = \frac{v_1 + v_2}{1 + v_1 v_2 / c^2}",
                "explanation": "Because $\operatorname{Range}(\tanh\theta) = (-1, 1)$ for all finite real rapidities $\theta \in (-\infty, \infty)$, the combined velocity $v_{12}/c = \tanh(\theta_1 + \theta_2)$ lies strictly in $(-1, 1)$, proving $v_{12} < c$ for all subluminal speeds."
            }
        ],
        "answer": r"\tanh(\theta_1 + \theta_2) = \frac{\tanh\theta_1 + \tanh\theta_2}{1 + \tanh\theta_1 \tanh\theta_2}, \quad \theta_{12} = \theta_1 + \theta_2, \quad |v_{12}| < c \text{ strictly}"
    }
]

u2_data = {
    "unitNumber": 2,
    "number": 2,
    "title": "Transcendental Functions & Hyperbolic Trigonometry",
    "description": "Comprehensive theory of transcendental mathematics: exponential functions, Euler's number e, natural logarithms, unit circle trigonometry, principal branch inverse trigonometric functions, hyperbolic geometry on x^2 - y^2 = 1, and rigorous logarithmic derivations of inverse hyperbolic functions.",
    "sections": u2_sections,
    "problems": u2_problems
}

with open("calc1_u2.json", "w", encoding="utf-8") as f:
    json.dump(u2_data, f, indent=2)
print("calc1_u2.json created successfully!")
