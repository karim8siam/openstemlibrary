window.COURSE_DATA = {
  "courseId": "calculus-1",
  "courseTitle": "Calculus I: Single-Variable Differential Calculus, Real Analysis Foundations & Optimization",
  "courseDescription": "A rigorous, university honors-level digital textbook and computational laboratory covering single-variable differential calculus and elementary real analysis: Part A establishes analytical foundations across four units (real numbers, completeness, functions, algebraic transformations, piecewise operators, and bijectivity; transcendental functions, exponential and logarithmic bases, trigonometric unit circle geometry, and hyperbolic catenary mechanics; intuitive limits, one-sided limits, the Cauchy-Weierstrass \u03b5-\u03b4 definition, squeeze theorem, and asymptotic infinities; three-part continuity criteria, topological classifications of discontinuities, the Intermediate Value Theorem IVT, root bisection algorithms, and the Extreme Value Theorem EVT). Part B explores differential mechanics, theorems, and optimization across four units (difference quotients, geometric secant-to-tangent limits, differentiability implying continuity, power rule proofs via binomial expansion, product, quotient, and chain rules via Carath\u00e9odory formulation; implicit differentiation, orthogonal trajectories, inverse function derivatives, and higher-order derivatives with Leibniz's product formula; Rolle's theorem, Lagrange Mean Value Theorem MVT, Cauchy generalized MVT, rigorous L'H\u00f4pital's rule derivations across all indeterminate forms 0/0, \u221e/\u221e, 0\u00b7\u221e, 1^\u221e, 0^0, and Taylor linear approximations; Fermat's stationary point theorem, First and Second Derivative Tests, concavity, points of inflection, the universal 7-step analytical curve sketching algorithm, applied geometric/physical optimization, and the related rates framework). Accompanied by 8 interactive 60 FPS geometric calculators and 24 tiered solved university examination problems (Foundational, Intermediate Exam, and Honors/Proof Challenge).",
  "units": [
    {
      "unitNumber": 1,
      "number": 1,
      "title": "Foundations of Functions, Graphs, Symmetries & Inverses",
      "description": "Comprehensive foundations of single-variable mathematics: real number continuum R, natural domains and ranges, polynomial degrees and asymptotes, absolute value mechanics, triangle inequalities, geometric graph transformations, even/odd symmetries, and bijective inverse functions.",
      "sections": [
        {
          "id": "u1-sec1",
          "title": "The Real Number System, Sets, Intervals & The Function Concept",
          "content": "<h4>1. The Real Number Continuum $\\mathbb{R}$ & Set Notation</h4>\n<p>The foundation of all single-variable real analysis and calculus is the set of real numbers $\\mathbb{R}$, equipped with the standard algebraic operations of addition and multiplication, satisfying the field axioms, order axioms, and the <strong>Completeness Axiom</strong> (every non-empty subset of $\\mathbb{R}$ bounded above has a least upper bound or supremum in $\\mathbb{R}$).</p>\n<p>Subsets of $\\mathbb{R}$ are frequently represented using interval notation:</p>\n<div class=\"math-display\">\n$$\\begin{aligned}\n\\text{Open Interval: } & (a, b) = \\{ x \\in \\mathbb{R} : a < x < b \\} \\\n\\text{Closed Interval: } & [a, b] = \\{ x \\in \\mathbb{R} : a \\le x \\le b \\} \\\n\\text{Half-Open Intervals: } & [a, b) = \\{ x \\in \\mathbb{R} : a \\le x < b \\}, \\quad (a, b] = \\{ x \\in \\mathbb{R} : a < x \\le b \\} \\\n\\text{Infinite Rays: } & [a, \\infty) = \\{ x \\in \\mathbb{R} : x \\ge a \\}, \\quad (-\\infty, b) = \\{ x \\in \\mathbb{R} : x < b \\}\n\\end{aligned}$$\n</div>\n\n<h4>2. Formal Definition of a Real Function</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Definition (Function): A function } f: X \\to Y \\text{ from a set } X \\subseteq \\mathbb{R} \\text{ (domain) to } Y \\subseteq \\mathbb{R} \\text{ (codomain) is a rule that assigns to each } x \\in X \\text{ exactly one element } f(x) \\in Y.}$$\n</div>\n<p>The <strong>Range</strong> (or image) of $f$ is the set of all attained values:</p>\n<div class=\"math-display\">\n$$\\operatorname{Range}(f) = \\{ y \\in Y : \\exists x \\in X \\text{ such that } f(x) = y \\} = f(X)$$\n</div>\n\n<h4>3. The Natural Domain & The Vertical Line Test</h4>\n<p>Unless explicitly restricted, the <em>natural domain</em> of a function defined by an algebraic expression is the largest subset of $\\mathbb{R}$ for which the expression produces a well-defined real number. In single-variable calculus, two foundational constraints govern natural domains:</p>\n<ol>\n  <li><strong>Division by Zero:</strong> Denominators cannot equal zero ($Q(x) \\ne 0$).</li>\n  <li><strong>Even Roots of Negative Numbers:</strong> For $\\sqrt[2n]{g(x)}$, we require $g(x) \\ge 0$.</li>\n</ol>\n<p><strong>The Vertical Line Test:</strong> A curve in the Cartesian plane $\\mathbb{R}^2$ represents the graph of a function $y = f(x)$ if and only if no vertical line $x = c$ intersects the curve at more than one point. If a vertical line intersects at two or more points, a single input would map to multiple outputs, violating single-valued functionality.</p>"
        },
        {
          "id": "u1-sec2",
          "title": "Polynomial & Rational Functions: Degrees, Roots & Asymptotic Behavior",
          "content": "<h4>1. Polynomial Functions</h4>\n<p>A <strong>polynomial function</strong> of degree $n \\in \\mathbb{N}_0$ with real coefficients $a_n, a_{n-1}, \\dots, a_0$ ($a_n \\ne 0$) is defined for all $x \\in \\mathbb{R}$ by:</p>\n<div class=\"math-display\">\n$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \\dots + a_1 x + a_0 = \\sum_{k=0}^n a_k x^k$$\n</div>\n<p>By the Fundamental Theorem of Algebra, a degree-$n$ polynomial has exactly $n$ complex roots (counting multiplicity), and at most $n$ distinct real roots. The end behavior of $P(x)$ as $x \\to \\pm\\infty$ is strictly governed by its leading monomial term $a_n x^n$:</p>\n<div class=\"math-display\">\n$$\\lim_{x \\to \\pm\\infty} P(x) = \\lim_{x \\to \\pm\\infty} a_n x^n \\left( 1 + \\frac{a_{n-1}}{a_n x} + \\dots + \\frac{a_0}{a_n x^n} \\right) = \\lim_{x \\to \\pm\\infty} a_n x^n$$\n</div>\n\n<h4>2. Rational Functions & Asymptotes</h4>\n<p>A <strong>rational function</strong> is a ratio of two polynomials $R(x) = \\frac{P(x)}{Q(x)}$ where $Q(x) \\not\\equiv 0$. Its natural domain is $\\operatorname{Dom}(R) = \\{ x \\in \\mathbb{R} : Q(x) \\ne 0 \\}$.</p>\n<p>Let $P(x) = a_n x^n + \\dots$ and $Q(x) = b_m x^m + \\dots$ with $a_n \\ne 0, b_m \\ne 0$:</p>\n<ul>\n  <li><strong>Vertical Asymptotes:</strong> If $x = c$ is a root of $Q(x)$ such that $(x - c)$ has higher multiplicity in $Q(x)$ than in $P(x)$, then $\\lim_{x \\to c} |R(x)| = \\infty$, producing a vertical asymptote at $x = c$. If $(x - c)$ cancels completely, $x = c$ is a <em>removable discontinuity (hole)</em>.</li>\n  <li><strong>Horizontal Asymptotes:</strong>\n    <ul>\n      <li>If $n < m$: The line $y = 0$ is a horizontal asymptote ($\\lim_{x \\to \\pm\\infty} R(x) = 0$).</li>\n      <li>If $n = m$: The horizontal line $y = \\frac{a_n}{b_m}$ is an asymptote ($\\lim_{x \\to \\pm\\infty} R(x) = a_n / b_m$).</li>\n      <li>If $n > m$: No horizontal asymptote exists.</li>\n    </ul>\n  </li>\n  <li><strong>Oblique (Slant) Asymptotes:</strong> If $n = m + 1$, polynomial long division yields $R(x) = (m_0 x + c_0) + \\frac{r(x)}{Q(x)}$ with $\\deg(r) < m$. The line $y = m_0 x + c_0$ is an oblique asymptote as $x \\to \\pm\\infty$.</li>\n</ul>"
        },
        {
          "id": "u1-sec3",
          "title": "Piecewise Functions, Absolute Value Mechanics & Step Operators",
          "content": "<h4>1. Piecewise-Defined Functions</h4>\n<p>A function defined by different analytical rules on disjoint sub-intervals of its domain is called a <strong>piecewise-defined function</strong>:</p>\n<div class=\"math-display\">\n$$f(x) = \\begin{cases}\ng_1(x), & x \\in I_1 \\\ng_2(x), & x \\in I_2 \\\n\\vdots & \\vdots \\\ng_k(x), & x \\in I_k\n\\end{cases}$$\n</div>\n\n<h4>2. The Absolute Value (Modulus) Function</h4>\n<p>The absolute value function $|x|: \\mathbb{R} \\to [0, \\infty)$ is defined algebraically as:</p>\n<div class=\"math-display\">\n$$|x| = \\sqrt{x^2} = \\begin{cases}\nx, & x \\ge 0 \\\n-x, & x < 0\n\\end{cases}$$\n</div>\n<p><strong>Fundamental Properties of Absolute Value:</strong></p>\n<ol>\n  <li><strong>Non-negativity:</strong> $|x| \\ge 0$, with $|x| = 0 \\iff x = 0$.</li>\n  <li><strong>Multiplicativity:</strong> $|x y| = |x| |y|$ and $\\left|\\frac{x}{y}\\right| = \\frac{|x|}{|y|}$ for $y \\ne 0$.</li>\n  <li><strong>The Triangle Inequality:</strong> For all $x, y \\in \\mathbb{R}$,\n    <div class=\"math-display\">\n    $$|x + y| \\le |x| + |y|$$\n    </div>\n  </li>\n  <li><strong>The Reverse Triangle Inequality:</strong>\n    <div class=\"math-display\">\n    $$||x| - |y|| \\le |x - y|$$\n    </div>\n  </li>\n  <li><strong>Interval Equivalence:</strong> For any $c > 0$, $|x - a| < c \\iff a - c < x < a + c$.</li>\n</ol>\n\n<h4>3. Step, Signum & Floor Functions</h4>\n<p>The <strong>signum function</strong> $\\operatorname{sgn}(x)$ extracts the algebraic sign of $x$:</p>\n<div class=\"math-display\">\n$$\\operatorname{sgn}(x) = \\begin{cases}\n+1, & x > 0 \\\n0, & x = 0 \\\n-1, & x < 0\n\\end{cases} = \\frac{x}{|x|} \\quad (x \\ne 0)$$\n</div>\n<p>The <strong>floor function</strong> (greatest integer function) $\\lfloor x \\rfloor$ maps $x$ to the unique integer $k \\in \\mathbb{Z}$ satisfying $k \\le x < k + 1$. The ceiling function $\\lceil x \\rceil$ satisfies $k - 1 < x \\le k$.</p>"
        },
        {
          "id": "u1-sec4",
          "title": "Geometric Transformations, Symmetry Tests & Monotonicity",
          "content": "<h4>1. Rigid and Non-Rigid Transformations</h4>\n<p>Given the base graph $y = f(x)$, algebraic modifications to the argument or output produce exact geometric transformations in $\\mathbb{R}^2$ ($c > 0$):</p>\n<ul>\n  <li><strong>Vertical Shift:</strong> $y = f(x) + c$ shifts the graph upward by $c$ units; $y = f(x) - c$ shifts downward.</li>\n  <li><strong>Horizontal Shift:</strong> $y = f(x - c)$ shifts the graph to the right by $c$ units; $y = f(x + c)$ shifts to the left.</li>\n  <li><strong>Vertical Scaling & Reflection:</strong> $y = a f(x)$ stretches vertically by factor $|a|$ if $|a| > 1$, compresses if $0 < |a| < 1$, and reflects across the $x$-axis if $a < 0$.</li>\n  <li><strong>Horizontal Scaling & Reflection:</strong> $y = f(b x)$ compresses horizontally by factor $1/|b|$ if $|b| > 1$, stretches if $0 < |b| < 1$, and reflects across the $y$-axis if $b < 0$.</li>\n</ul>\n\n<h4>2. Algebraic Symmetry Tests: Even and Odd Functions</h4>\n<div class=\"math-display\">\n$$\\begin{aligned}\n\\mathbf{\\text{Even Function: }} & f(-x) = f(x) \\quad \\forall x \\in \\operatorname{Dom}(f) \\iff \\text{Symmetric with respect to the } y\\text{-axis} \\\n\\mathbf{\\text{Odd Function: }} & f(-x) = -f(x) \\quad \\forall x \\in \\operatorname{Dom}(f) \\iff \\text{Symmetric with respect to the origin } (0,0)\n\\end{aligned}$$\n</div>\n<p><strong>Decomposition Theorem:</strong> Every function $f: \\mathbb{R} \\to \\mathbb{R}$ whose domain is symmetric about the origin can be uniquely decomposed into the sum of an even function $f_{\\text{even}}$ and an odd function $f_{\\text{odd}}$:</p>\n<div class=\"math-display\">\n$$f(x) = f_{\\text{even}}(x) + f_{\\text{odd}}(x) = \\frac{f(x) + f(-x)}{2} + \\frac{f(x) - f(-x)}{2}$$\n</div>\n\n<h4>3. Monotonicity on Intervals</h4>\n<p>Let $I \\subseteq \\operatorname{Dom}(f)$ be an interval. We define:</p>\n<ul>\n  <li><strong>Strictly Increasing:</strong> $\\forall x_1, x_2 \\in I$, $x_1 < x_2 \\implies f(x_1) < f(x_2)$.</li>\n  <li><strong>Strictly Decreasing:</strong> $\\forall x_1, x_2 \\in I$, $x_1 < x_2 \\implies f(x_1) > f(x_2)$.</li>\n  <li><strong>Strictly Monotonic:</strong> A function that is either strictly increasing on $I$ or strictly decreasing on $I$. Strictly monotonic functions are guaranteed to be one-to-one (injective) on $I$.</li>\n</ul>"
        },
        {
          "id": "u1-sec5",
          "title": "Algebra of Functions, Composition & Invertibility",
          "content": "<h4>1. Composition of Functions</h4>\n<p>Given two functions $f: Y \\to Z$ and $g: X \\to Y$, the <strong>composite function</strong> $(f \\circ g): X \\to Z$ is defined by:</p>\n<div class=\"math-display\">\n$$(f \\circ g)(x) = f(g(x))$$\n</div>\n<p>The natural domain of $f \\circ g$ consists of all $x$ in the domain of $g$ whose outputs $g(x)$ lie in the domain of $f$:</p>\n<div class=\"math-display\">\n$$\\operatorname{Dom}(f \\circ g) = \\{ x \\in \\operatorname{Dom}(g) : g(x) \\in \\operatorname{Dom}(f) \\}$$\n</div>\n<p>Note that function composition is generally <strong>non-commutative</strong>: $f \\circ g \\ne g \\circ f$ in general, though it is always associative: $f \\circ (g \\circ h) = (f \\circ g) \\circ h$.</p>\n\n<h4>2. Invertibility: Injectivity, Surjectivity & Bijectivity</h4>\n<div class=\"math-display\">\n$$\\begin{aligned}\n\\mathbf{\\text{Injective (One-to-One): }} & f(x_1) = f(x_2) \\implies x_1 = x_2 \\quad (\\text{Horizontal Line Test}) \\\n\\mathbf{\\text{Surjective (Onto): }} & \\forall y \\in Y, \\, \\exists x \\in X \\text{ such that } f(x) = y \\quad (\\operatorname{Range}(f) = Y) \\\n\\mathbf{\\text{Bijective: }} & f \\text{ is both injective and surjective}\n\\end{aligned}$$\n</div>\n<p><strong>Theorem (Existence of Inverse Function):</strong> A function $f: X \\to Y$ possesses a two-sided inverse function $f^{-1}: Y \\to X$ if and only if $f$ is a bijection. When $f^{-1}$ exists, it satisfies:</p>\n<div class=\"math-display\">\n$$(f^{-1} \\circ f)(x) = x \\quad \\forall x \\in X, \\qquad (f \\circ f^{-1})(y) = y \\quad \\forall y \\in Y$$\n</div>\n<p>Geometrically, the point $(a, b)$ lies on the graph of $y = f(x)$ if and only if $(b, a)$ lies on the graph of $y = f^{-1}(x)$. Thus, the graph of $f^{-1}$ is the exact reflection of the graph of $f$ across the principal diagonal line $y = x$.</p>",
          "simulation": "calc1-trans-inverse-sim",
          "simulations": [
            "calc1-trans-inverse-sim"
          ]
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "Natural Domain & Range of Radical Rational Functions",
          "statement": "Find the exact natural domain and range of the function $f(x) = \\sqrt{\\frac{4 - x^2}{x^2 - 1}}$. Express both sets in rigorous interval notation.",
          "steps": [
            {
              "step": "Step 1: Formulate Domain Inequality Constraints",
              "math": "\\frac{4 - x^2}{x^2 - 1} \\ge 0 \\quad \\text{and} \\quad x^2 - 1 \\ne 0",
              "explanation": "Because the square root is defined only for non-negative radicands, the quotient must be $\\ge 0$. Simultaneously, the denominator cannot vanish."
            },
            {
              "step": "Step 2: Factor Polynomials and Find Critical Zeros",
              "math": "\\frac{(2 - x)(2 + x)}{(x - 1)(x + 1)} \\ge 0",
              "explanation": "The critical boundary points where the sign of the rational expression can change are $x = -2, -1, 1, 2$."
            },
            {
              "step": "Step 3: Sign Table Analysis across Sub-Intervals",
              "math": "\\begin{array}{c|c|c|c|c|c}\n\\text{Interval} & (-\\infty, -2) & (-2, -1) & (-1, 1) & (1, 2) & (2, \\infty) \\\\\\\n\\hline\n4 - x^2 & - & + & + & + & - \\\nx^2 - 1 & + & + & - & + & + \\\\\\\n\\hline\n\\text{Quotient} & - & + & - & + & -\n\\end{array}",
              "explanation": "The quotient is strictly non-negative on $[-2, -1)$ and $(1, 2]$. Notice that $x = \\pm 1$ must be strictly excluded due to denominator zero."
            },
            {
              "step": "Step 4: Determine the Range",
              "math": "u = \\frac{4 - x^2}{x^2 - 1} \\implies u \\in [0, \\infty) \\implies \\operatorname{Range}(f) = [0, \\infty)",
              "explanation": "At $x = \\pm 2$, the radicand is $0$, giving $f(\\pm 2) = 0$. As $x \to 1^+$ or $x \to -1^-$, the denominator approaches $0^+$ while the numerator approaches $3$, driving $u \to \\infty$. Hence, the range is all non-negative real numbers."
            }
          ],
          "answer": "\\operatorname{Dom}(f) = [-2, -1) \\cup (1, 2], \\qquad \\operatorname{Range}(f) = [0, \\infty)"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "Constructing and Verifying the Algebraic Inverse of a Fractional Linear Function",
          "statement": "Given the M\u00f6bius fractional linear transformation $f(x) = \\frac{3x + 5}{2x - 7}$: (a) Determine the natural domain and range of $f$. (b) Prove that $f$ is strictly injective on its domain. (c) Derive an explicit formula for $f^{-1}(x)$. (d) Verify the cancellation identities $(f \\circ f^{-1})(x) = x$ and $(f^{-1} \\circ f)(x) = x$.",
          "steps": [
            {
              "step": "Step 1: Domain and Range Determination",
              "math": "\\operatorname{Dom}(f) = \\mathbb{R} \\setminus \\{7/2\\}, \\qquad \\lim_{x \\to \\pm\\infty} f(x) = \\frac{3}{2} \\implies \\operatorname{Range}(f) = \\mathbb{R} \\setminus \\{3/2\\}",
              "explanation": "The denominator $2x - 7 = 0 \\implies x = 7/2$. The horizontal asymptote is $y = 3/2$, which is never attained for any finite real $x$."
            },
            {
              "step": "Step 2: Rigorous Proof of Injectivity",
              "math": "\\frac{3x_1 + 5}{2x_1 - 7} = \\frac{3x_2 + 5}{2x_2 - 7} \\implies (3x_1 + 5)(2x_2 - 7) = (3x_2 + 5)(2x_1 - 7)",
              "explanation": "Cross-multiplying: $6x_1 x_2 - 21 x_1 + 10 x_2 - 35 = 6x_1 x_2 - 21 x_2 + 10 x_1 - 35$. Canceling like terms yields $-31 x_1 = -31 x_2 \\implies x_1 = x_2$. Thus $f$ is strictly injective."
            },
            {
              "step": "Step 3: Algebraic Inversion",
              "math": "y = \\frac{3x + 5}{2x - 7} \\implies y(2x - 7) = 3x + 5 \\implies x(2y - 3) = 7y + 5 \\implies x = \\frac{7y + 5}{2y - 3}",
              "explanation": "Interchanging variables yields the inverse function $f^{-1}(x) = \\frac{7x + 5}{2x - 3}$ with domain $\\mathbb{R} \\setminus \\{3/2\\}$."
            },
            {
              "step": "Step 4: Direct Verification of Cancellation Identity",
              "math": "f(f^{-1}(x)) = \\frac{3\\left(\\frac{7x+5}{2x-3}\\right) + 5}{2\\left(\\frac{7x+5}{2x-3}\\right) - 7} = \\frac{(21x + 15) + 5(2x - 3)}{(14x + 10) - 7(2x - 3)} = \\frac{31x}{31} = x",
              "explanation": "Both numerator and denominator simplify identically, confirming that $f(f^{-1}(x)) = x$ identically."
            }
          ],
          "answer": "f^{-1}(x) = \\frac{7x + 5}{2x - 3}, \\quad \\operatorname{Dom}(f^{-1}) = \\mathbb{R} \\setminus \\{3/2\\}, \\quad \\operatorname{Range}(f^{-1}) = \\mathbb{R} \\setminus \\{7/2\\}"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "Even-Odd Symmetry Decomposition & Functional Equation Analysis",
          "statement": "Let $f: \\mathbb{R} \\to \\mathbb{R}$ satisfy the functional relation $f(x + y) + f(x - y) = 2f(x)f(y)$ for all $x, y \\in \\mathbb{R}$ (d'Alembert's functional equation) with $f$ not identically zero. (a) Prove that $f(0) = 1$. (b) Prove that $f$ must be an even function: $f(-x) = f(x)$. (c) If in addition $f(x)$ is decomposed into $f(x) = f_e(x) + f_o(x)$, show that $f_o(x) \\equiv 0$.",
          "steps": [
            {
              "step": "Step 1: Evaluate at $x = 0$ to Determine $f(0)$",
              "math": "f(0 + y) + f(0 - y) = 2f(0)f(y) \\implies f(y) + f(-y) = 2f(0)f(y)",
              "explanation": "Setting $y = 0$: $f(x) + f(x) = 2f(x)f(0) \\implies 2f(x) = 2f(x)f(0) \\implies 2f(x)[1 - f(0)] = 0$. Since $f$ is not identically zero, there exists $x_0$ with $f(x_0) \ne 0$, forcing $f(0) = 1$."
            },
            {
              "step": "Step 2: Prove $f$ is Even",
              "math": "f(y) + f(-y) = 2(1)f(y) = 2f(y) \\implies f(-y) = 2f(y) - f(y) = f(y)",
              "explanation": "Since $f(-y) = f(y)$ holds for every $y \\in \\mathbb{R}$, $f$ is an even function."
            },
            {
              "step": "Step 3: Verification of Odd Component Vanishing",
              "math": "f_o(x) = \\frac{f(x) - f(-x)}{2} = \\frac{f(x) - f(x)}{2} = 0 \\quad \\forall x \\in \\mathbb{R}",
              "explanation": "Because $f(-x) = f(x)$ globally, the unique odd part in the canonical even-odd decomposition $f(x) = f_e(x) + f_o(x)$ vanishes identically, leaving $f(x) = f_e(x)$."
            }
          ],
          "answer": "f(0) = 1, \\quad f(-x) = f(x) \\text{ (strictly even)}, \\quad f_o(x) \\equiv 0"
        }
      ],
      "simulations": [
        "calc1-trans-inverse-sim"
      ],
      "id": "unit1",
      "unitId": "unit1-calc1",
      "leadSummary": "Comprehensive foundations of single-variable mathematics: real number continuum R, natural domains and ranges, polynomial degrees and asymptotes, absolute value mechanics, triangle inequalities, geometric graph transformations, even/odd symmetries, and bijective inverse functions."
    },
    {
      "unitNumber": 2,
      "number": 2,
      "title": "Transcendental Functions & Hyperbolic Trigonometry",
      "description": "Comprehensive theory of transcendental mathematics: exponential functions, Euler's number e, natural logarithms, unit circle trigonometry, principal branch inverse trigonometric functions, hyperbolic geometry on x^2 - y^2 = 1, and rigorous logarithmic derivations of inverse hyperbolic functions.",
      "sections": [
        {
          "id": "u2-sec1",
          "title": "Exponential Functions, Euler's Number e & Logarithmic Foundations",
          "content": "<h4>1. Exponential Functions</h4>\n<p>For a fixed positive base $a > 0$ with $a \\ne 1$, the <strong>exponential function</strong> with base $a$ is defined for all $x \\in \\mathbb{R}$ by $f(x) = a^x$.</p>\n<p><strong>Fundamental Exponential Laws:</strong> For all $x, y \\in \\mathbb{R}$ and $a, b > 0$:</p>\n<div class=\"math-display\">\n$$a^{x+y} = a^x a^y, \\qquad a^{x-y} = \\frac{a^x}{a^y}, \\qquad (a^x)^y = a^{x y}, \\qquad (a b)^x = a^x b^x$$\n</div>\n<p>The function is strictly positive: $\\operatorname{Range}(a^x) = (0, \\infty)$. It is strictly increasing if $a > 1$, and strictly decreasing if $0 < a < 1$.</p>\n\n<h4>2. Euler's Number $e$ & The Natural Exponential</h4>\n<p>The base of the natural exponential function, Euler's number $e \\approx 2.718281828459...$, is uniquely defined by the fundamental limit:</p>\n<div class=\"math-display\">\n$$e = \\lim_{n \\to \\infty} \\left( 1 + \\frac{1}{n} \\right)^n = \\sum_{k=0}^\\infty \\frac{1}{k!} = 1 + 1 + \\frac{1}{2!} + \\frac{1}{3!} + \\dots$$\n</div>\n<p>Geometrically, $y = e^x$ is the unique exponential curve whose tangent line at the $y$-intercept $(0, 1)$ has a slope of exactly $1$.</p>\n\n<h4>3. Logarithmic Functions</h4>\n<p>Because $f(x) = a^x$ is strictly monotonic on $\\mathbb{R}$, it is a bijection from $\\mathbb{R}$ to $(0, \\infty)$. Its inverse function is the <strong>logarithm to base $a$</strong>:</p>\n<div class=\"math-display\">\n$$y = \\log_a(x) \\iff a^y = x \\quad (x > 0)$$\n</div>\n<p>The inverse of the natural exponential $e^x$ is the <strong>natural logarithm</strong> $\\ln(x) = \\log_e(x)$:</p>\n<div class=\"math-display\">\n$$\\ln(e^x) = x \\quad \\forall x \\in \\mathbb{R}, \\qquad e^{\\ln(x)} = x \\quad \\forall x > 0$$\n</div>\n<p><strong>Logarithmic Properties & Change of Base:</strong></p>\n<div class=\"math-display\">\n$$\\ln(x y) = \\ln(x) + \\ln(y), \\quad \\ln(x/y) = \\ln(x) - \\ln(y), \\quad \\ln(x^r) = r \\ln(x), \\quad \\log_a(x) = \\frac{\\ln(x)}{\\ln(a)}$$\n</div>"
        },
        {
          "id": "u2-sec2",
          "title": "Trigonometric Functions, Exact Identities & Unit Circle Geometry",
          "content": "<h4>1. The Unit Circle Definition of Trigonometric Functions</h4>\n<p>In analytical calculus, angles are measured strictly in <strong>radians</strong>. Let $(x, y)$ be the terminal coordinates of an angle $\\theta \\in \\mathbb{R}$ on the unit circle $x^2 + y^2 = 1$ measured counterclockwise from $(1, 0)$:</p>\n<div class=\"math-display\">\n$$\\cos\\theta = x, \\qquad \\sin\\theta = y, \\qquad \\tan\\theta = \\frac{\\sin\\theta}{\\cos\\theta} = \\frac{y}{x} \\quad (x \\ne 0)$$\n</div>\n<p>The reciprocal functions are $\\sec\\theta = 1/\\cos\\theta$, $\\csc\\theta = 1/\\sin\\theta$, and $\\cot\\theta = 1/\\tan\\theta = \\cos\\theta/\\sin\\theta$.</p>\n\n<h4>2. Fundamental Trigonometric Identities</h4>\n<p>From the Pythagorean theorem $x^2 + y^2 = 1$ on the unit circle:</p>\n<div class=\"math-display\">\n$$\\sin^2\\theta + \\cos^2\\theta = 1, \\qquad 1 + \\tan^2\\theta = \\sec^2\\theta, \\qquad 1 + \\cot^2\\theta = \\csc^2\\theta$$\n</div>\n<p><strong>Angle Addition & Double-Angle Formulas:</strong></p>\n<div class=\"math-display\">\n$$\\begin{aligned}\n\\sin(\\alpha \\pm \\beta) &= \\sin\\alpha \\cos\\beta \\pm \\cos\\alpha \\sin\\beta \\\n\\cos(\\alpha \\pm \\beta) &= \\cos\\alpha \\cos\\beta \\mp \\sin\\alpha \\sin\\beta \\\n\\sin(2\\theta) &= 2\\sin\\theta\\cos\\theta \\\n\\cos(2\\theta) &= \\cos^2\\theta - \\sin^2\\theta = 2\\cos^2\\theta - 1 = 1 - 2\\sin^2\\theta \\\n\\tan(\\alpha \\pm \\beta) &= \\frac{\\tan\\alpha \\pm \\tan\\beta}{1 \\mp \\tan\\alpha\\tan\\beta}\n\\end{aligned}$$\n</div>\n<p><strong>Power-Reduction (Half-Angle) Formulas:</strong> Crucial for integration in calculus:</p>\n<div class=\"math-display\">\n$$\\sin^2\\theta = \\frac{1 - \\cos(2\\theta)}{2}, \\qquad \\cos^2\\theta = \\frac{1 + \\cos(2\\theta)}{2}$$\n</div>"
        },
        {
          "id": "u2-sec3",
          "title": "Inverse Trigonometric Functions & Principal Value Branches",
          "content": "<h4>1. Restriction of Domains & Principal Branches</h4>\n<p>Because trigonometric functions are periodic, they fail the horizontal line test across $\\mathbb{R}$. To construct inverses, we restrict each function to a standard <strong>principal interval</strong> on which it is strictly monotonic and surjective onto its range:</p>\n\n<div class=\"math-display\">\n$$\\begin{array}{l|c|c|l}\n\\text{Function} & \\text{Restricted Domain} & \\text{Range} & \\text{Inverse Function } f^{-1} \\\\\\\n\\hline\n\\sin x & [-\\pi/2, \\pi/2] & [-1, 1] & y = \\arcsin x \\iff x = \\sin y, \\quad y \\in [-\\pi/2, \\pi/2] \\\n\\cos x & [0, \\pi] & [-1, 1] & y = \\arccos x \\iff x = \\cos y, \\quad y \\in [0, \\pi] \\\n\\tan x & (-\\pi/2, \\pi/2) & (-\\infty, \\infty) & y = \\arctan x \\iff x = \\tan y, \\quad y \\in (-\\pi/2, \\pi/2) \\\n\\sec x & [0, \\pi/2) \\cup (\\pi/2, \\pi] & (-\\infty, -1] \\cup [1, \\infty) & y = \\operatorname{arcsec} x \\iff x = \\sec y\n\\end{array}$$\n</div>\n\n<h4>2. Fundamental Identities of Inverse Trigonometric Functions</h4>\n<div class=\"math-display\">\n$$\\arcsin(x) + \\arccos(x) = \\frac{\\pi}{2} \\quad \\forall x \\in [-1, 1], \\qquad \\arctan(x) + \\operatorname{arccot}(x) = \\frac{\\pi}{2} \\quad \\forall x \\in \\mathbb{R}$$\n</div>\n<p><strong>Cancellation Cautions:</strong></p>\n<div class=\"math-display\">\n$$\\sin(\\arcsin x) = x \\quad \\forall x \\in [-1, 1], \\quad \\text{but} \\quad \\arcsin(\\sin x) = x \\iff x \\in [-\\pi/2, \\pi/2]$$\n</div>\n<p>For arguments outside the principal range, symmetry must be utilized: e.g., $\\arcsin(\\sin(5\\pi/6)) = \\arcsin(1/2) = \\pi/6 \\ne 5\\pi/6$.</p>"
        },
        {
          "id": "u2-sec4",
          "title": "Hyperbolic Functions: Symmetries, Identities & The Unit Hyperbola",
          "content": "<h4>1. Formal Definitions of Hyperbolic Functions</h4>\n<p>The <strong>hyperbolic functions</strong> are defined as the symmetric and antisymmetric linear combinations of the exponential functions $e^x$ and $e^{-x}$:</p>\n<div class=\"math-display\">\n$$\\begin{aligned}\n\\text{Hyperbolic Sine: } & \\sinh x = \\frac{e^x - e^{-x}}{2} \\quad (\\text{Strictly Odd: } \\sinh(-x) = -\\sinh x) \\\n\\text{Hyperbolic Cosine: } & \\cosh x = \\frac{e^x + e^{-x}}{2} \\quad (\\text{Strictly Even: } \\cosh(-x) = \\cosh x) \\\n\\text{Hyperbolic Tangent: } & \\tanh x = \\frac{\\sinh x}{\\cosh x} = \\frac{e^x - e^{-x}}{e^x + e^{-x}} = \\frac{e^{2x} - 1}{e^{2x} + 1}\n\\end{aligned}$$\n</div>\n<p>Reciprocals: $\\operatorname{sech} x = \\frac{1}{\\cosh x}$, $\\operatorname{csch} x = \\frac{1}{\\sinh x}$, $\\operatorname{coth} x = \\frac{\\cosh x}{\\sinh x}$.</p>\n\n<h4>2. The Fundamental Hyperbolic Identity & The Unit Hyperbola</h4>\n<div class=\"math-display\">\n$$\\cosh^2 x - \\sinh^2 x = \\left(\\frac{e^x + e^{-x}}{2}\\right)^2 - \\left(\\frac{e^x - e^{-x}}{2}\\right)^2 = \\frac{(e^{2x} + 2 + e^{-2x}) - (e^{2x} - 2 + e^{-2x})}{4} = \\frac{4}{4} = 1$$\n</div>\n<p><strong>Geometric Analogy:</strong> Just as $(\\cos t, \\sin t)$ parametrizes the unit circle $x^2 + y^2 = 1$, the parametric coordinates $(x, y) = (\\cosh t, \\sinh t)$ trace the right branch of the unit equilateral hyperbola:</p>\n<div class=\"math-display\">\n$$x^2 - y^2 = 1 \\quad (x \\ge 1)$$\n</div>\n<p><strong>Derived Identities:</strong></p>\n<div class=\"math-display\">\n$$1 - \\tanh^2 x = \\operatorname{sech}^2 x, \\qquad \\coth^2 x - 1 = \\operatorname{csch}^2 x$$\n$$\\sinh(2x) = 2\\sinh x\\cosh x, \\qquad \\cosh(2x) = \\cosh^2 x + \\sinh^2 x = 2\\cosh^2 x - 1 = 1 + 2\\sinh^2 x$$\n</div>",
          "simulation": "calc1-exp-log-hyperbolic-sim",
          "simulations": [
            "calc1-exp-log-hyperbolic-sim"
          ]
        },
        {
          "id": "u2-sec5",
          "title": "Inverse Hyperbolic Functions & Derivation of Explicit Logarithmic Forms",
          "content": "<h4>1. Invertibility of Hyperbolic Functions</h4>\n<ul>\n  <li>$\\sinh x$ is strictly increasing on $\\mathbb{R}$ with range $\\mathbb{R}$. Its inverse $\\operatorname{arsinh} x$ is defined for all $x \\in \\mathbb{R}$.</li>\n  <li>$\\cosh x$ is even on $\\mathbb{R}$ with range $[1, \\infty)$. Restricting to $x \\ge 0$ yields the principal branch of $\\operatorname{arcosh} x$ for $x \\ge 1$, with range $[0, \\infty)$.</li>\n  <li>$\\tanh x$ is strictly increasing with range $(-1, 1)$. Its inverse $\\operatorname{artanh} x$ is defined on $(-1, 1)$.</li>\n</ul>\n\n<h4>2. Rigorous Derivation of Logarithmic Closed Forms</h4>\n<p><strong>Theorem:</strong> For all $x \\in \\mathbb{R}$, $\\operatorname{arsinh} x = \\ln(x + \\sqrt{x^2 + 1})$.</p>\n<p><em>Proof:</em> Let $y = \\operatorname{arsinh} x$. Then $x = \\sinh y = \\frac{e^y - e^{-y}}{2}$. Multiplying by $2e^y$ yields:</p>\n<div class=\"math-display\">\n$$2x e^y = e^{2y} - 1 \\implies (e^y)^2 - 2x(e^y) - 1 = 0$$\n</div>\n<p>This is a quadratic equation in $u = e^y$. By the quadratic formula:</p>\n<div class=\"math-display\">\n$$e^y = \\frac{2x \\pm \\sqrt{4x^2 - 4(1)(-1)}}{2} = x \\pm \\sqrt{x^2 + 1}$$\n</div>\n<p>Since $e^y > 0$ for all real $y$, and $\\sqrt{x^2+1} > \\sqrt{x^2} = |x| \\ge x$, the minus sign yields a strictly negative value $x - \\sqrt{x^2+1} < 0$, which is inadmissible. Thus:</p>\n<div class=\"math-display\">\n$$e^y = x + \\sqrt{x^2 + 1} \\implies y = \\operatorname{arsinh} x = \\ln(x + \\sqrt{x^2 + 1}) \\quad \\blacksquare$$\n</div>\n\n<p><strong>Complete Logarithmic Catalog:</strong></p>\n<div class=\"math-display\">\n$$\\begin{aligned}\n\\operatorname{arcosh} x &= \\ln\\left(x + \\sqrt{x^2 - 1}\\right), \\quad x \\ge 1 \\\n\\operatorname{artanh} x &= \\frac{1}{2}\\ln\\left(\\frac{1 + x}{1 - x}\\right), \\quad -1 < x < 1 \\\n\\operatorname{arcoth} x &= \\frac{1}{2}\\ln\\left(\\frac{x + 1}{x - 1}\\right), \\quad |x| > 1\n\\end{aligned}$$\n</div>"
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "Exact Evaluation of Inverse Trigonometric Expressions",
          "statement": "Find the exact real values of: (a) $\\arcsin\\left(\\sin\\left(\\frac{7\\pi}{6}\\right)\\right)$, (b) $\\cos\\left(2\\arcsin\\left(-\\frac{3}{5}\\right)\\right)$, and (c) $\\tan\\left(\\arccos\\left(\\frac{5}{13}\\right)\\right)$.",
          "steps": [
            {
              "step": "Step 1: Evaluate (a) via Principal Branch Interval",
              "math": "\\sin\\left(\\frac{7\\pi}{6}\\right) = -\\frac{1}{2} \\implies \\arcsin\\left(-\\frac{1}{2}\\right) = -\\frac{\\pi}{6}",
              "explanation": "Because $7\\pi/6 \notin [-\\pi/2, \\pi/2]$, we cannot simply cancel. We evaluate the inner sine first to get $-1/2$, whose principal arcsine value is $-\\pi/6$."
            },
            {
              "step": "Step 2: Evaluate (b) via Double-Angle Formula",
              "math": "\\cos(2\\theta) = 1 - 2\\sin^2\\theta \\quad \\text{where } \\theta = \\arcsin(-3/5) \\implies \\sin\\theta = -\\frac{3}{5}",
              "explanation": "Substitute $\\sin\theta$: $\\cos(2\theta) = 1 - 2\\left(-\\frac{3}{5}\\right)^2 = 1 - 2\\left(\\frac{9}{25}\\right) = 1 - \\frac{18}{25} = \\frac{7}{25}$."
            },
            {
              "step": "Step 3: Evaluate (c) via Right Triangle Geometry",
              "math": "\\alpha = \\arccos\\left(\\frac{5}{13}\\right) \\implies \\cos\\alpha = \\frac{5}{13}, \\quad \\sin\\alpha = \\sqrt{1 - (5/13)^2} = \\frac{12}{13}",
              "explanation": "Then $\tan\\alpha = \\frac{\\sin\\alpha}{\\cos\\alpha} = \\frac{12/13}{5/13} = \\frac{12}{5}$."
            }
          ],
          "answer": "\\text{(a) } -\\frac{\\pi}{6}, \\qquad \\text{(b) } \\frac{7}{25}, \\qquad \\text{(c) } \\frac{12}{5}"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "Derivation of the Explicit Logarithmic Formula for Inverse Hyperbolic Tangent",
          "statement": "Let $y = \\operatorname{artanh}(x)$ for $x \\in (-1, 1)$. (a) Starting from the definition $\\tanh(y) = \\frac{e^{2y} - 1}{e^{2y} + 1} = x$, derive the closed logarithmic formula $\\operatorname{artanh}(x) = \\frac{1}{2}\\ln\\left(\\frac{1 + x}{1 - x}\\right)$. (b) Use this formula to compute the exact value of $\\operatorname{artanh}(3/5)$ and $\\operatorname{artanh}(0)$.",
          "steps": [
            {
              "step": "Step 1: Set up the Inversion Equation",
              "math": "x = \\frac{e^{2y} - 1}{e^{2y} + 1} \\implies x(e^{2y} + 1) = e^{2y} - 1",
              "explanation": "Expand and isolate the exponential term $e^{2y}$."
            },
            {
              "step": "Step 2: Solve for $e^{2y}$",
              "math": "x e^{2y} + x = e^{2y} - 1 \\implies 1 + x = e^{2y}(1 - x) \\implies e^{2y} = \\frac{1 + x}{1 - x}",
              "explanation": "Since $-1 < x < 1$, both $1+x > 0$ and $1-x > 0$, so the ratio is strictly positive."
            },
            {
              "step": "Step 3: Take Natural Logarithms",
              "math": "2y = \\ln\\left(\\frac{1 + x}{1 - x}\\right) \\implies y = \\operatorname{artanh}(x) = \\frac{1}{2}\\ln\\left(\\frac{1 + x}{1 - x}\\right)",
              "explanation": "Dividing by 2 yields the exact logarithmic formula."
            },
            {
              "step": "Step 4: Compute Values",
              "math": "\\operatorname{artanh}(3/5) = \\frac{1}{2}\\ln\\left(\\frac{1 + 3/5}{1 - 3/5}\\right) = \\frac{1}{2}\\ln\\left(\\frac{8/5}{2/5}\\right) = \\frac{1}{2}\\ln(4) = \\ln(2)",
              "explanation": "For $x = 0$: $\\operatorname{artanh}(0) = \\frac{1}{2}\\ln(1/1) = 0$."
            }
          ],
          "answer": "\\operatorname{artanh}(x) = \\frac{1}{2}\\ln\\left(\\frac{1 + x}{1 - x}\\right), \\qquad \\operatorname{artanh}(3/5) = \\ln(2), \\qquad \\operatorname{artanh}(0) = 0"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "Hyperbolic Addition Theorem & Ultra-Relativistic Rapidity Invariance",
          "statement": "In special relativity, the velocity $v$ of a particle is related to its rapidity $\\theta \\in \\mathbb{R}$ by $v/c = \\tanh\\theta$. (a) Using the definitions of $\\sinh$ and $\\cosh$, prove the general hyperbolic addition formula: $\\tanh(\\theta_1 + \\theta_2) = \\frac{\\tanh\\theta_1 + \\tanh\\theta_2}{1 + \\tanh\\theta_1 \\tanh\\theta_2}$. (b) Deduce that the relativistic velocity addition law $v_{12} = \\frac{v_1 + v_2}{1 + v_1 v_2 / c^2}$ corresponds to the simple linear addition of rapidities: $\\theta_{12} = \\theta_1 + \\theta_2$. (c) Prove that if $v_1 < c$ and $v_2 < c$, then $v_{12} < c$ strictly.",
          "steps": [
            {
              "step": "Step 1: Expand $\\sinh(\theta_1 + \theta_2)$ and $\\cosh(\theta_1 + \theta_2)$",
              "math": "\\begin{aligned}\n\\sinh(\\theta_1 + \\theta_2) &= \\sinh\\theta_1 \\cosh\\theta_2 + \\cosh\\theta_1 \\sinh\\theta_2 \\\n\\cosh(\\theta_1 + \\theta_2) &= \\cosh\\theta_1 \\cosh\\theta_2 + \\sinh\\theta_1 \\sinh\\theta_2\n\\end{aligned}",
              "explanation": "Expanding $e^{(\theta_1+\theta_2)} \\pm e^{-(\theta_1+\theta_2)}$ directly from definition proves these two addition identities."
            },
            {
              "step": "Step 2: Form the Ratio $\tanh(\theta_1 + \theta_2)$",
              "math": "\\tanh(\\theta_1 + \\theta_2) = \\frac{\\sinh\\theta_1 \\cosh\\theta_2 + \\cosh\\theta_1 \\sinh\\theta_2}{\\cosh\\theta_1 \\cosh\\theta_2 + \\sinh\\theta_1 \\sinh\\theta_2} = \\frac{\\frac{\\sinh\\theta_1}{\\cosh\\theta_1} + \\frac{\\sinh\\theta_2}{\\cosh\\theta_2}}{1 + \\frac{\\sinh\\theta_1\\sinh\\theta_2}{\\cosh\\theta_1\\cosh\\theta_2}} = \\frac{\\tanh\\theta_1 + \\tanh\\theta_2}{1 + \\tanh\\theta_1 \\tanh\\theta_2}",
              "explanation": "Dividing numerator and denominator by $\\cosh\theta_1 \\cosh\theta_2$ establishes the identity."
            },
            {
              "step": "Step 3: Relate to Velocity Addition and Strict Subluminal Bound",
              "math": "\\frac{v_{12}}{c} = \\tanh(\\theta_1 + \\theta_2) = \\frac{v_1/c + v_2/c}{1 + (v_1/c)(v_2/c)} \\implies v_{12} = \\frac{v_1 + v_2}{1 + v_1 v_2 / c^2}",
              "explanation": "Because $\\operatorname{Range}(\tanh\theta) = (-1, 1)$ for all finite real rapidities $\theta \\in (-\\infty, \\infty)$, the combined velocity $v_{12}/c = \tanh(\theta_1 + \theta_2)$ lies strictly in $(-1, 1)$, proving $v_{12} < c$ for all subluminal speeds."
            }
          ],
          "answer": "\\tanh(\\theta_1 + \\theta_2) = \\frac{\\tanh\\theta_1 + \\tanh\\theta_2}{1 + \\tanh\\theta_1 \\tanh\\theta_2}, \\quad \\theta_{12} = \\theta_1 + \\theta_2, \\quad |v_{12}| < c \\text{ strictly}"
        }
      ],
      "simulations": [
        "calc1-exp-log-hyperbolic-sim"
      ],
      "id": "unit2",
      "unitId": "unit2-calc1",
      "leadSummary": "Comprehensive theory of transcendental mathematics: exponential functions, Euler's number e, natural logarithms, unit circle trigonometry, principal branch inverse trigonometric functions, hyperbolic geometry on x^2 - y^2 = 1, and rigorous logarithmic derivations of inverse hyperbolic functions."
    },
    {
      "unitNumber": 3,
      "number": 3,
      "title": "The Theory of Limits & Rigorous \u03b5-\u03b4 Analysis",
      "description": "The mathematical foundation of single-variable analysis: intuitive limit mechanics, left and right one-sided limits, Cauchy-Weierstrass epsilon-delta definition and scratchwork methodology, limit arithmetic laws, Squeeze theorem, geometric proof of lim (sin theta)/theta = 1, limits at infinity, and infinite limits with asymptotes.",
      "sections": [
        {
          "id": "u3-sec1",
          "title": "The Intuitive Limit Concept, Numerical Behavior & One-Sided Limits",
          "content": "<h4>1. Intuitive Limit Concept</h4>\n<p>In calculus, the limit is the foundational concept that enables the transition from static algebra to dynamical rates of change. Intuitively, we say that the limit of $f(x)$ as $x$ approaches $c$ is $L$:</p>\n<div class=\"math-display\">\n$$\\lim_{x \\to c} f(x) = L$$\n</div>\n<p>if the values of $f(x)$ can be made arbitrarily close to $L$ by taking $x$ sufficiently close to $c$ (with $x \\ne c$). Crucially, <strong>the value of $f(c)$ itself is completely irrelevant</strong> to the limit; $f(c)$ may equal $L$, may equal some other value, or may be completely undefined.</p>\n\n<h4>2. One-Sided Limits</h4>\n<p>Often, a function behaves differently depending on whether $x$ approaches $c$ from numbers strictly less than $c$ (from the left) or strictly greater than $c$ (from the right):</p>\n<div class=\"math-display\">\n$$\\begin{aligned}\n\\mathbf{\\text{Left-Hand Limit: }} & \\lim_{x \\to c^-} f(x) = L_1 \\quad (\\text{as } x \\to c \\text{ with } x < c) \\\n\\mathbf{\\text{Right-Hand Limit: }} & \\lim_{x \\to c^+} f(x) = L_2 \\quad (\\text{as } x \\to c \\text{ with } x > c)\n\\end{aligned}$$\n</div>\n<p><strong>Theorem (Two-Sided Limit Existence Criterion):</strong> The two-sided limit $\\lim_{x \\to c} f(x)$ exists and equals $L$ if and only if both one-sided limits exist and are strictly equal:</p>\n<div class=\"math-display\">\n$$\\lim_{x \\to c} f(x) = L \\iff \\lim_{x \\to c^-} f(x) = \\lim_{x \\to c^+} f(x) = L$$\n</div>\n<p>If $\\lim_{x \\to c^-} f(x) \\ne \\lim_{x \\to c^+} f(x)$, the two-sided limit <em>does not exist (DNE)</em>.</p>"
        },
        {
          "id": "u3-sec2",
          "title": "The Formal Cauchy-Weierstrass Epsilon-Delta Definition of Limit",
          "content": "<h4>1. The Formal Cauchy-Weierstrass Definition</h4>\n<p>To eliminate ambiguity in phrases like \"arbitrarily close\" and \"sufficiently close\", Augustin-Louis Cauchy and Karl Weierstrass formulated the rigorous $\\varepsilon$-$\\delta$ definition:</p>\n<div class=\"math-display\">\n$$\\mathbf{\\lim_{x \\to c} f(x) = L \\iff \\forall \\varepsilon > 0, \\, \\exists \\delta > 0 \\text{ such that } 0 < |x - c| < \\delta \\implies |f(x) - L| < \\varepsilon}$$\n</div>\n\n<h4>2. Geometric Interpretation of the $\\varepsilon$-$\\delta$ Challenge</h4>\n<p>The definition is a mathematical game between two players:</p>\n<ol>\n  <li>A challenger proposes a tolerance $\\varepsilon > 0$, demanding that $f(x)$ lie in the horizontal target band $(L - \\varepsilon, L + \\varepsilon)$.</li>\n  <li>You must respond by finding a neighborhood radius $\\delta > 0$ such that for every $x$ within the punctured vertical interval $(c - \\delta, c + \\delta) \\setminus \\{c\\}$, the graph $y = f(x)$ stays strictly inside the horizontal $\\varepsilon$-tube.</li>\n</ol>\n<p>Notice that $\\delta$ depends on both $\\varepsilon$ and $c$: $\\delta = \\delta(\\varepsilon, c)$.</p>\n\n<h4>3. The Canonical $\\varepsilon$-$\\delta$ Proof Template</h4>\n<p>A rigorous $\\varepsilon$-$\\delta$ proof always proceeds in two distinct phases:</p>\n<ul>\n  <li><strong>Scratchwork Analysis:</strong> Start with the target inequality $|f(x) - L| < \\varepsilon$. Factor out $|x - c|$ to obtain $|x - c| \\cdot |g(x)| < \\varepsilon$. Choose a preliminary bound on $|x - c|$ (typically $\\delta_1 \\le 1$) to bound the auxiliary factor $|g(x)| \\le M$. Then deduce $\\delta = \\min\\{1, \\varepsilon / M\\}$.</li>\n  <li><strong>Formal Deductive Proof:</strong> State \"Let $\\varepsilon > 0$ be given. Choose $\\delta = \\min\\{1, \\varepsilon / M\\}$.\" Then, assuming $0 < |x - c| < \\delta$, deduce sequentially that $|f(x) - L| < \\varepsilon$ by direct algebraic inequalities.</li>\n</ul>",
          "simulation": "calc1-epsilon-delta-sim",
          "simulations": [
            "calc1-epsilon-delta-sim"
          ]
        },
        {
          "id": "u3-sec3",
          "title": "Limit Arithmetic Laws & The Squeeze (Sandwich) Theorem",
          "content": "<h4>1. Limit Arithmetic Theorems</h4>\n<p>Let $\\lim_{x \\to c} f(x) = L$ and $\\lim_{x \\to c} g(x) = M$. Then:</p>\n<div class=\"math-display\">\n$$\\begin{aligned}\n\\text{Sum / Difference: } & \\lim_{x \\to c} [f(x) \\pm g(x)] = L \\pm M \\\n\\text{Scalar Multiple: } & \\lim_{x \\to c} [k f(x)] = k L \\quad (k \\in \\mathbb{R}) \\\n\\text{Product Law: } & \\lim_{x \\to c} [f(x) g(x)] = L \\cdot M \\\n\\text{Quotient Law: } & \\lim_{x \\to c} \\left[\\frac{f(x)}{g(x)}\\right] = \\frac{L}{M} \\quad (\\text{provided } M \\ne 0) \\\n\\text{Power / Root Law: } & \\lim_{x \\to c} [f(x)]^n = L^n, \\quad \\lim_{x \\to c} \\sqrt[n]{f(x)} = \\sqrt[n]{L} \\quad (L > 0 \\text{ if } n \\text{ is even})\n\\end{aligned}$$\n</div>\n\n<h4>2. The Squeeze (Sandwich) Theorem</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Theorem: If } g(x) \\le f(x) \\le h(x) \\text{ for all } x \\text{ in an open interval containing } c \\text{ (except possibly at } c\\text{)}, \\text{ and } \\lim_{x \\to c} g(x) = \\lim_{x \\to c} h(x) = L, \\text{ then } \\lim_{x \\to c} f(x) = L.}$$\n</div>\n\n<h4>3. Rigorous Geometric Proof of the Fundamental Limit $\\lim_{\\theta \\to 0} \\frac{\\sin\\theta}{\\theta} = 1$</h4>\n<p>Consider a unit circle of radius $r = 1$. For an acute central angle $\\theta \\in (0, \\pi/2)$ measured in radians:</p>\n<ol>\n  <li>Area of inner triangle with vertices $(0,0), (1,0), (\\cos\\theta, \\sin\\theta)$:\n    <div class=\"math-display\">\n    $$A_{\\text{inner}} = \\frac{1}{2} (1) (\\sin\\theta) = \\frac{1}{2} \\sin\\theta$$\n    </div>\n  </li>\n  <li>Area of circular sector of angle $\\theta$:\n    <div class=\"math-display\">\n    $$A_{\\text{sector}} = \\frac{1}{2} r^2 \\theta = \\frac{1}{2} \\theta$$\n    </div>\n  </li>\n  <li>Area of outer tangent triangle with vertices $(0,0), (1,0), (1, \\tan\\theta)$:\n    <div class=\"math-display\">\n    $$A_{\\text{outer}} = \\frac{1}{2} (1) (\\tan\\theta) = \\frac{1}{2} \\frac{\\sin\\theta}{\\cos\\theta}$$\n    </div>\n  </li>\n</ol>\n<p>By geometric containment, $A_{\\text{inner}} < A_{\\text{sector}} < A_{\\text{outer}}$:</p>\n<div class=\"math-display\">\n$$\\frac{1}{2} \\sin\\theta < \\frac{1}{2} \\theta < \\frac{1}{2} \\frac{\\sin\\theta}{\\cos\\theta}$$\n</div>\n<p>Multiplying by $2 / \\sin\\theta$ (since $\\sin\\theta > 0$ on $(0, \\pi/2)$):</p>\n<div class=\"math-display\">\n$$1 < \\frac{\\theta}{\\sin\\theta} < \\frac{1}{\\cos\\theta} \\implies \\cos\\theta < \\frac{\\sin\\theta}{\\theta} < 1$$\n</div>\n<p>Taking the limit as $\\theta \\to 0^+$: since $\\lim_{\\theta \\to 0^+} \\cos\\theta = 1$, the Squeeze Theorem forces $\\lim_{\\theta \\to 0^+} \\frac{\\sin\\theta}{\\theta} = 1$. By even symmetry $\\frac{\\sin(-\\theta)}{-\\theta} = \\frac{\\sin\\theta}{\\theta}$, the two-sided limit is established: $\\lim_{\\theta \\to 0} \\frac{\\sin\\theta}{\\theta} = 1 \\quad \\blacksquare$</p>"
        },
        {
          "id": "u3-sec4",
          "title": "Limits at Infinity, Infinite Limits & Asymptotic Analysis",
          "content": "<h4>1. Limits at Infinity & Horizontal Asymptotes</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\lim_{x \\to \\infty} f(x) = L \\iff \\forall \\varepsilon > 0, \\, \\exists N > 0 \\text{ such that } x > N \\implies |f(x) - L| < \\varepsilon}$$\n</div>\n<p>If $\\lim_{x \\to \\infty} f(x) = L$ or $\\lim_{x \\to -\\infty} f(x) = L$, the horizontal line $y = L$ is a <strong>horizontal asymptote</strong> of the graph $y = f(x)$.</p>\n\n<h4>2. Fundamental Rational Limit Theorem</h4>\n<p>For any rational power $r > 0$:</p>\n<div class=\"math-display\">\n$$\\lim_{x \\to \\infty} \\frac{1}{x^r} = 0, \\qquad \\lim_{x \\to -\\infty} \\frac{1}{x^r} = 0 \\quad (\\text{for } x^r \\text{ defined for negative } x)$$\n</div>\n\n<h4>3. Infinite Limits & Vertical Asymptotes</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\lim_{x \\to c} f(x) = \\infty \\iff \\forall M > 0, \\, \\exists \\delta > 0 \\text{ such that } 0 < |x - c| < \\delta \\implies f(x) > M}$$\n</div>\n<p>If $f(x) \\to \\pm\\infty$ as $x \\to c^+$ or $x \\to c^-$, the line $x = c$ is a <strong>vertical asymptote</strong>.</p>"
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "Direct Algebraic Limit Evaluation with Indeterminate 0/0 Conjugation",
          "statement": "Evaluate the exact analytical limit: $\\lim_{x \\to 0} \\frac{\\sqrt{x^2 + 9} - 3}{x^2}$. Show all factorization and rationalization steps.",
          "steps": [
            {
              "step": "Step 1: Check Direct Substitution",
              "math": "\\frac{\\sqrt{0^2 + 9} - 3}{0^2} = \\frac{3 - 3}{0} = \\left[\\frac{0}{0}\\right]",
              "explanation": "Direct substitution yields the indeterminate form $0/0$, necessitating algebraic transformation."
            },
            {
              "step": "Step 2: Multiply by Radical Conjugate",
              "math": "\\frac{\\sqrt{x^2 + 9} - 3}{x^2} \\cdot \\frac{\\sqrt{x^2 + 9} + 3}{\\sqrt{x^2 + 9} + 3} = \\frac{(x^2 + 9) - 9}{x^2 (\\sqrt{x^2 + 9} + 3)} = \\frac{x^2}{x^2 (\\sqrt{x^2 + 9} + 3)}",
              "explanation": "Expanding the difference of squares in the numerator eliminates the radical."
            },
            {
              "step": "Step 3: Cancel Common Zero Factor and Evaluate",
              "math": "\\lim_{x \\to 0} \\frac{1}{\\sqrt{x^2 + 9} + 3} = \\frac{1}{\\sqrt{0 + 9} + 3} = \\frac{1}{3 + 3} = \\frac{1}{6}",
              "explanation": "Since $x \ne 0$ in the punctured limit neighborhood, we cancel $x^2$ and evaluate by direct substitution."
            }
          ],
          "answer": "\\lim_{x \\to 0} \\frac{\\sqrt{x^2 + 9} - 3}{x^2} = \\frac{1}{6}"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "Rigorous Cauchy Epsilon-Delta Proof for a Quadratic Function",
          "statement": "Use the formal $\\varepsilon$-$\\delta$ definition of a limit to prove rigorously that $\\lim_{x \\to 3} (2x^2 - 5x + 1) = 4$.",
          "steps": [
            {
              "step": "Step 1: Scratchwork Analysis",
              "math": "|(2x^2 - 5x + 1) - 4| = |2x^2 - 5x - 3| = |(2x + 1)(x - 3)| = |2x + 1| \\cdot |x - 3| < \\varepsilon",
              "explanation": "We factored out the critical deviation factor $|x - 3|$. We must now bound the auxiliary factor $|2x + 1|$."
            },
            {
              "step": "Step 2: Establish a Preliminary Bound on |x - 3|",
              "math": "\\text{Assume } |x - 3| < 1 \\implies -1 < x - 3 < 1 \\implies 2 < x < 4",
              "explanation": "Bounding $x$ on $(2, 4)$ allows us to bound $2x + 1$:"
            },
            {
              "step": "Step 3: Bound the Auxiliary Term",
              "math": "2 < x < 4 \\implies 4 < 2x < 8 \\implies 5 < 2x + 1 < 9 \\implies |2x + 1| < 9",
              "explanation": "Thus, whenever $|x - 3| < 1$, we have $|2x + 1| \\cdot |x - 3| < 9 |x - 3|$. To ensure this is $< \\varepsilon$, we require $|x - 3| < \\varepsilon / 9$."
            },
            {
              "step": "Step 4: Formal Proof",
              "math": "\\text{Let } \\varepsilon > 0. \\text{ Choose } \\delta = \\min\\left(1, \\frac{\\varepsilon}{9}\\right). \\text{ If } 0 < |x - 3| < \\delta, \\text{ then } |(2x^2 - 5x + 1) - 4| < 9|x - 3| < 9\\left(\\frac{\\varepsilon}{9}\\right) = \\varepsilon. \\quad \\blacksquare",
              "explanation": "This completes the formal deductive proof according to Cauchy's criterion."
            }
          ],
          "answer": "\\delta = \\min\\left(1, \\frac{\\varepsilon}{9}\\right) \\implies |(2x^2 - 5x + 1) - 4| < \\varepsilon"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "Trigonometric Squeeze Theorem Proof for an Oscillatory Radical Limit",
          "statement": "Evaluate the limit $\\lim_{x \\to 0} \\frac{x^3 \\sin\\left(\\frac{1}{x}\\right) + \\tan(4x)}{\\sin(2x) + x^2 \\cos\\left(\\frac{1}{x^2}\\right)}$ using rigorous limit theorems and the Squeeze Theorem. Prove every step without L'H\u00f4pital's Rule.",
          "steps": [
            {
              "step": "Step 1: Divide Numerator and Denominator by $x$",
              "math": "\\frac{x^3 \\sin(1/x) + \\tan(4x)}{\\sin(2x) + x^2 \\cos(1/x^2)} = \\frac{x^2 \\sin(1/x) + \\frac{\\tan(4x)}{x}}{\\frac{\\sin(2x)}{x} + x \\cos(1/x^2)}",
              "explanation": "Dividing by $x \ne 0$ isolates the fundamental trigonometric limits and small oscillatory terms."
            },
            {
              "step": "Step 2: Evaluate the Squeezed Oscillatory Limits",
              "math": "-1 \\le \\sin(1/x) \\le 1 \\implies -x^2 \\le x^2 \\sin(1/x) \\le x^2 \\implies \\lim_{x \\to 0} x^2 \\sin(1/x) = 0",
              "explanation": "Similarly, $-|x| \\le x \\cos(1/x^2) \\le |x| \\implies \\lim_{x \to 0} x \\cos(1/x^2) = 0$ by the Squeeze Theorem."
            },
            {
              "step": "Step 3: Evaluate the Trigonometric Limits",
              "math": "\\lim_{x \\to 0} \\frac{\\tan(4x)}{x} = \\lim_{x \\to 0} 4 \\left(\\frac{\\sin(4x)}{4x}\\right) \\frac{1}{\\cos(4x)} = 4(1)(1) = 4, \\qquad \\lim_{x \\to 0} \\frac{\\sin(2x)}{x} = 2(1) = 2",
              "explanation": "Using the fundamental theorem $\\lim_{u \to 0} \\frac{\\sin u}{u} = 1$."
            },
            {
              "step": "Step 4: Combine via Quotient and Sum Limit Laws",
              "math": "\\lim_{x \\to 0} \\frac{x^2 \\sin(1/x) + \\frac{\\tan(4x)}{x}}{\\frac{\\sin(2x)}{x} + x \\cos(1/x^2)} = \\frac{0 + 4}{2 + 0} = \\frac{4}{2} = 2",
              "explanation": "Since the denominator limit $2 \ne 0$, the quotient limit law holds rigorously."
            }
          ],
          "answer": "\\lim_{x \\to 0} \\frac{x^3 \\sin(1/x) + \\tan(4x)}{\\sin(2x) + x^2 \\cos(1/x^2)} = 2"
        }
      ],
      "simulations": [
        "calc1-epsilon-delta-sim"
      ],
      "id": "unit3",
      "unitId": "unit3-calc1",
      "leadSummary": "The mathematical foundation of single-variable analysis: intuitive limit mechanics, left and right one-sided limits, Cauchy-Weierstrass epsilon-delta definition and scratchwork methodology, limit arithmetic laws, Squeeze theorem, geometric proof of lim (sin theta)/theta = 1, limits at infinity, and infinite limits with asymptotes."
    },
    {
      "unitNumber": 4,
      "number": 4,
      "title": "Continuity & Global Theorems on Intervals",
      "description": "Rigorous continuity theory in real analysis: three-part definition of continuity at a point, epsilon-delta formulation, classification of removable, jump, and essential discontinuities, algebra of continuous functions, Intermediate Value Theorem (IVT) with bisection root-finding, Extreme Value Theorem (EVT), and topological antipodal proofs.",
      "sections": [
        {
          "id": "u4-sec1",
          "title": "Continuity at a Point: The Three-Part Criterion & Epsilon-Delta Formulation",
          "content": "<h4>1. The Three-Part Definition of Continuity at a Point</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Definition: A function } f \\text{ is continuous at a point } c \\in \\operatorname{Dom}(f) \\text{ if and only if:}}$$\n$$\\mathbf{1. } f(c) \\text{ is defined } (c \\in \\operatorname{Dom}(f)), \\quad \\mathbf{2. } \\lim_{x \\to c} f(x) \\text{ exists, and} \\quad \\mathbf{3. } \\lim_{x \\to c} f(x) = f(c)$$\n</div>\n<p>If any of these three conditions fails, $f$ is said to be <strong>discontinuous</strong> at $c$.</p>\n\n<h4>2. The $\\varepsilon$-$\\delta$ Characterization of Continuity</h4>\n<div class=\"math-display\">\n$$f \\text{ is continuous at } c \\iff \\forall \\varepsilon > 0, \\, \\exists \\delta > 0 \\text{ such that } |x - c| < \\delta \\implies |f(x) - f(c)| < \\varepsilon$$\n</div>\n<p>Notice that unlike the limit definition where $x \\ne c$ was required ($0 < |x - c|$), here if $x = c$, $|f(c) - f(c)| = 0 < \\varepsilon$ holds trivially.</p>\n\n<h4>3. Continuity on an Interval</h4>\n<p>A function $f$ is continuous on an open interval $(a, b)$ if it is continuous at every $c \\in (a, b)$. It is continuous on a closed interval $[a, b]$ if it is continuous on $(a, b)$, right-continuous at $a$ ($\\lim_{x \\to a^+} f(x) = f(a)$), and left-continuous at $b$ ($\\lim_{x \\to b^-} f(x) = f(b)$).</p>"
        },
        {
          "id": "u4-sec2",
          "title": "Classification of Discontinuities: Removable, Jump & Essential",
          "content": "<h4>1. Removable Discontinuities (Holes)</h4>\n<p>A point $c$ is a <strong>removable discontinuity</strong> of $f$ if $\\lim_{x \\to c} f(x) = L$ exists as a finite real number, but either $f(c)$ is undefined or $f(c) \\ne L$.</p>\n<p>The discontinuity can be \"removed\" by redefining $f(c) = L$. Typical example: $f(x) = \\frac{x^2 - 1}{x - 1}$ at $c = 1$.</p>\n\n<h4>2. Jump (First Kind) Discontinuities</h4>\n<p>A point $c$ is a <strong>jump discontinuity</strong> if both one-sided limits exist as finite real numbers, but they are unequal:</p>\n<div class=\"math-display\">\n$$\\lim_{x \\to c^-} f(x) = L_1 \\ne \\lim_{x \\to c^+} f(x) = L_2$$\n</div>\n<p>The quantity $J = L_2 - L_1$ is called the <strong>jump</strong> of $f$ at $c$. Classic example: the signum function $\\operatorname{sgn}(x)$ at $c = 0$, where $L_1 = -1, L_2 = +1, J = 2$.</p>\n\n<h4>3. Essential (Second Kind) Discontinuities</h4>\n<p>A discontinuity at $c$ is <strong>essential</strong> if at least one of the one-sided limits fails to exist (either diverging to $\\pm\\infty$ or oscillating indefinitely):</p>\n<ul>\n  <li><strong>Infinite Discontinuity:</strong> $f(x) = 1/(x - 2)$ at $c = 2$.</li>\n  <li><strong>Oscillatory Discontinuity:</strong> $f(x) = \\sin(1/x)$ at $c = 0$. As $x \\to 0$, $1/x \\to \\infty$, and the sine function oscillates between $-1$ and $+1$ infinitely often, so neither one-sided limit exists.</li>\n</ul>"
        },
        {
          "id": "u4-sec3",
          "title": "Algebra of Continuous Functions & Continuity of Compositions",
          "content": "<h4>1. Algebraic Combinations</h4>\n<p><strong>Theorem:</strong> If $f$ and $g$ are continuous at $c$, then for any scalar $k \\in \\mathbb{R}$:</p>\n<div class=\"math-display\">\n$$f + g, \\quad f - g, \\quad k f, \\quad f \\cdot g \\quad \\text{are continuous at } c$$\n$$\\text{and } \\frac{f}{g} \\text{ is continuous at } c \\text{ provided } g(c) \\ne 0$$\n</div>\n\n<h4>2. Continuity of Composite Functions</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Theorem: If } g \\text{ is continuous at } c \\text{ and } f \\text{ is continuous at } g(c), \\text{ then the composite function } (f \\circ g) \\text{ is continuous at } c.}$$\n</div>\n<p><em>Proof:</em> Let $\\varepsilon > 0$. Since $f$ is continuous at $u_0 = g(c)$, $\\exists \\eta > 0$ such that $|u - u_0| < \\eta \\implies |f(u) - f(u_0)| < \\varepsilon$. Since $g$ is continuous at $c$, for this $\\eta > 0$, $\\exists \\delta > 0$ such that $|x - c| < \\delta \\implies |g(x) - g(c)| < \\eta$. Substituting $u = g(x)$ establishes $|f(g(x)) - f(g(c))| < \\varepsilon \\quad \\blacksquare$</p>\n\n<h4>3. Continuity of Elementary Functions</h4>\n<p>All polynomials, rational functions, power functions, trigonometric functions, inverse trigonometric functions, exponential functions, logarithmic functions, and hyperbolic functions are continuous on their entire natural domains.</p>"
        },
        {
          "id": "u4-sec4",
          "title": "The Intermediate Value Theorem (IVT) & Root-Finding Algorithms",
          "content": "<h4>1. The Intermediate Value Theorem (Bolzano-Cauchy)</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Theorem (IVT): Let } f: [a, b] \\to \\mathbb{R} \\text{ be continuous on the closed bounded interval } [a, b]. \\text{ If } u \\text{ is any real number strictly between } f(a) \\text{ and } f(b), \\text{ then there exists at least one } c \\in (a, b) \\text{ such that } f(c) = u.}$$\n</div>\n<p>Geometrically, the graph of a continuous function on $[a, b]$ has no breaks or jumps, so it must cross any horizontal line $y = u$ lying between the endpoint values $y = f(a)$ and $y = f(b)$.</p>\n\n<h4>2. Bolzano's Theorem (Existence of Roots)</h4>\n<p><strong>Corollary:</strong> If $f \\in C[a, b]$ and $f(a) \\cdot f(b) < 0$ (opposite signs at endpoints), then there exists at least one root $c \\in (a, b)$ such that $f(c) = 0$.</p>\n\n<h4>3. The Bisection Algorithm</h4>\n<p>Bolzano's theorem provides a constructive numerical method to compute roots to arbitrary precision:</p>\n<ol>\n  <li>Set interval $[a_0, b_0]$ with $f(a_0) f(b_0) < 0$.</li>\n  <li>Evaluate midpoint $m_k = \\frac{a_k + b_k}{2}$. If $f(m_k) = 0$, $m_k$ is the exact root.</li>\n  <li>If $f(a_k) f(m_k) < 0$, set $[a_{k+1}, b_{k+1}] = [a_k, m_k]$; otherwise set $[a_{k+1}, b_{k+1}] = [m_k, b_k]$.</li>\n  <li>After $n$ iterations, the error is bounded by $|c - m_n| \\le \\frac{b_0 - a_0}{2^{n+1}}$.</li>\n</ol>",
          "simulation": "calc1-ivt-bisection-sim",
          "simulations": [
            "calc1-ivt-bisection-sim"
          ]
        },
        {
          "id": "u4-sec5",
          "title": "The Extreme Value Theorem (EVT) & Compactness on Closed Intervals",
          "content": "<h4>1. The Extreme Value Theorem (Weierstrass)</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Theorem (EVT): If a function } f: [a, b] \\to \\mathbb{R} \\text{ is continuous on a closed, bounded interval } [a, b], \\text{ then } f \\text{ attains both an absolute maximum and an absolute minimum on } [a, b].}$$\n$$\\exists x_{\\min}, x_{\\max} \\in [a, b] \\quad \\text{such that} \\quad f(x_{\\min}) \\le f(x) \\le f(x_{\\max}) \\quad \\forall x \\in [a, b]$$\n</div>\n\n<h4>2. Necessity of the Hypotheses</h4>\n<p>Both hypotheses\u2014<strong>continuity</strong> and a <strong>closed bounded interval</strong>\u2014are strictly necessary:</p>\n<ul>\n  <li><strong>Failure on Open Interval:</strong> $f(x) = x$ on $(0, 1)$ is continuous, but attains neither a minimum (infimum is $0 \\notin (0, 1)$) nor a maximum (supremum is $1 \\notin (0, 1)$).</li>\n  <li><strong>Failure on Unbounded Domain:</strong> $f(x) = x^2$ on $[0, \\infty)$ is continuous, but attains no maximum as $x \\to \\infty$.</li>\n  <li><strong>Failure if Discontinuous:</strong> $f(x) = \\begin{cases} 1/x, & x \\in (0, 1] \\\\ 0, & x = 0 \\end{cases}$ on $[0, 1]$ is defined on a closed bounded interval, but discontinuous at $x = 0$, having no maximum.</li>\n</ul>"
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "Piecewise Function Parameter Determination for Global Continuity",
          "statement": "Find the unique values of constants $a, b \\in \\mathbb{R}$ that make the piecewise function $f(x)$ continuous everywhere on $\\mathbb{R}$:\n$$f(x) = \\begin{cases} \\frac{x^2 - 4}{x - 2}, & x < 2 \\\\ a x^2 - b x + 3, & 2 \\le x < 3 \\\\ 2x - a + b, & x \\ge 3 \\end{cases}$$",
          "steps": [
            {
              "step": "Step 1: Enforce Continuity at the Boundary $x = 2$",
              "math": "\\lim_{x \\to 2^-} f(x) = \\lim_{x \\to 2^-} \\frac{(x-2)(x+2)}{x-2} = 2 + 2 = 4, \\qquad f(2) = a(2^2) - b(2) + 3 = 4a - 2b + 3",
              "explanation": "For continuity at $x = 2$, the left limit must equal the value at $x = 2$: $4a - 2b + 3 = 4 \\implies 4a - 2b = 1$ (Equation 1)."
            },
            {
              "step": "Step 2: Enforce Continuity at the Boundary $x = 3$",
              "math": "\\lim_{x \\to 3^-} f(x) = 9a - 3b + 3, \\qquad \\lim_{x \\to 3^+} f(x) = 2(3) - a + b = 6 - a + b",
              "explanation": "Equating the two limits at $x = 3$: $9a - 3b + 3 = 6 - a + b \\implies 10a - 4b = 3$ (Equation 2)."
            },
            {
              "step": "Step 3: Solve the Linear System",
              "math": "\\begin{cases} 4a - 2b = 1 \\\\ 10a - 4b = 3 \\end{cases} \\implies 2(4a - 2b) = 8a - 4b = 2",
              "explanation": "Subtracting this from Equation 2: $(10a - 4b) - (8a - 4b) = 3 - 2 \\implies 2a = 1 \\implies a = 1/2$. Substituting into Equation 1: $4(1/2) - 2b = 1 \\implies 2 - 2b = 1 \\implies 2b = 1 \\implies b = 1/2$."
            }
          ],
          "answer": "a = \\frac{1}{2}, \\qquad b = \\frac{1}{2}"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "Rigorous Proof of Root Existence via the Intermediate Value Theorem",
          "statement": "Prove that the transcendental equation $e^x = 3 - 2x$ has at least one real root in the interval $(0, 1)$. Furthermore, explain how 4 iterations of the Bisection Method locate this root to an error of at most $1/32$.",
          "steps": [
            {
              "step": "Step 1: Construct Auxiliary Function and Verify Continuity",
              "math": "g(x) = e^x + 2x - 3",
              "explanation": "The function $g(x)$ is continuous on $[0, 1]$ as the sum of the natural exponential $e^x$ and a linear polynomial $2x - 3$."
            },
            {
              "step": "Step 2: Evaluate Endpoints and Verify Sign Change",
              "math": "g(0) = e^0 + 2(0) - 3 = 1 - 3 = -2 < 0, \\qquad g(1) = e^1 + 2(1) - 3 = e - 1 \\approx 2.718 - 1 = 1.718 > 0",
              "explanation": "Since $g(0) < 0$ and $g(1) > 0$, $0$ lies strictly between $g(0)$ and $g(1)$."
            },
            {
              "step": "Step 3: Apply the Intermediate Value Theorem",
              "math": "\\exists c \\in (0, 1) \\quad \\text{such that} \\quad g(c) = 0 \\implies e^c + 2c - 3 = 0 \\implies e^c = 3 - 2c \\quad \\blacksquare",
              "explanation": "By the IVT (Bolzano's theorem), there exists at least one solution $c \\in (0, 1)$."
            },
            {
              "step": "Step 4: Error Bound of Bisection Method",
              "math": "\\text{Error}_n \\le \\frac{b_0 - a_0}{2^{n+1}} = \\frac{1 - 0}{2^5} = \\frac{1}{32} \\approx 0.03125",
              "explanation": "After $n = 4$ bisections, the half-width of the enclosing sub-interval is $(1 - 0)/2^5 = 1/32$."
            }
          ],
          "answer": "\\exists c \\in (0, 1) \\text{ with } e^c = 3 - 2c; \\quad \\text{Bisection Error after 4 steps } \\le \\frac{1}{32}"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "Topological Proof of Antipodal Temperature Equivalence (Borsuk-Ulam 1D)",
          "statement": "Suppose the temperature $T(\\theta)$ along the Earth's equator is a continuous function of the longitude angle $\\theta \\in [0, 2\\pi]$ where $\\theta = 0$ and $\\theta = 2\\pi$ represent the same point ($T(0) = T(2\\pi)$). Prove rigorously using the Intermediate Value Theorem that there exists at least one pair of diametrically opposite (antipodal) points on the equator with exactly the same temperature: $T(c) = T(c + \\pi)$ for some $c \\in [0, \\pi]$.",
          "steps": [
            {
              "step": "Step 1: Construct the Antipodal Difference Function",
              "math": "f(\\theta) = T(\\theta) - T(\\theta + \\pi) \\quad \\text{for } \\theta \\in [0, \\pi]",
              "explanation": "Since $T$ is continuous, $f(\theta)$ is continuous on the closed interval $[0, \\pi]$."
            },
            {
              "step": "Step 2: Evaluate $f(\theta)$ at the Endpoints $\theta = 0$ and $\theta = \\pi$",
              "math": "f(0) = T(0) - T(\\pi), \\qquad f(\\pi) = T(\\pi) - T(2\\pi) = T(\\pi) - T(0)",
              "explanation": "Since $T(2\\pi) = T(0)$, we have $f(\\pi) = -(T(0) - T(\\pi)) = -f(0)$."
            },
            {
              "step": "Step 3: Analyze Signs and Apply IVT",
              "math": "\\text{Case 1: If } f(0) = 0 \\implies T(0) = T(\\pi), \\text{ then } c = 0 \\text{ is the desired point.}",
              "explanation": "Case 2: If $f(0) \ne 0$, then $f(0)$ and $f(\\pi) = -f(0)$ have strictly opposite signs ($f(0) f(\\pi) < 0$)."
            },
            {
              "step": "Step 4: Conclude via Bolzano's Theorem",
              "math": "\\exists c \\in (0, \\pi) \\quad \\text{such that} \\quad f(c) = 0 \\implies T(c) - T(c + \\pi) = 0 \\implies T(c) = T(c + \\pi) \\quad \\blacksquare",
              "explanation": "The Intermediate Value Theorem guarantees the existence of a point $c$ with zero difference, completing the proof of the 1D Borsuk-Ulam theorem."
            }
          ],
          "answer": "\\exists c \\in [0, \\pi] \\text{ such that } T(c) = T(c + \\pi) \\quad (\\text{Antipodal Temperature Equivalence})"
        }
      ],
      "simulations": [
        "calc1-ivt-bisection-sim"
      ],
      "id": "unit4",
      "unitId": "unit4-calc1",
      "leadSummary": "Rigorous continuity theory in real analysis: three-part definition of continuity at a point, epsilon-delta formulation, classification of removable, jump, and essential discontinuities, algebra of continuous functions, Intermediate Value Theorem (IVT) with bisection root-finding, Extreme Value Theorem (EVT), and topological antipodal proofs."
    },
    {
      "unitNumber": 5,
      "number": 5,
      "title": "The Derivative: Foundations, Difference Quotients & Differentiation Rules",
      "description": "Rigorous theory of differentiation: secant-to-tangent limiting process, Newton difference quotient, one-sided derivatives, proof that differentiability implies continuity, failure modes (cusps, vertical tangents, wild oscillations), power rule, product rule proof, quotient rule, and derivatives of trigonometric, exponential, and hyperbolic functions.",
      "sections": [
        {
          "id": "u5-sec1",
          "title": "The Tangent Line Problem, Instantaneous Rates & Difference Quotients",
          "content": "<h4>1. The Tangent Line as a Limiting Secant Line</h4>\n<p>Let $P(x_0, f(x_0))$ be a fixed point on the curve $y = f(x)$. Let $Q(x_0 + h, f(x_0 + h))$ be a neighboring point with $h \\ne 0$. The slope of the secant line passing through $P$ and $Q$ is given by the <strong>Newton-Leibniz difference quotient</strong>:</p>\n<div class=\"math-display\">\n$$m_{\\text{sec}} = \\frac{\\Delta y}{\\Delta x} = \\frac{f(x_0 + h) - f(x_0)}{h}$$\n</div>\n<p>As $h \\to 0$, point $Q$ slides along the curve toward $P$. If the secant slopes approach a unique finite limiting value, that limit is defined as the <strong>slope of the tangent line</strong> to the curve at $P$:</p>\n<div class=\"math-display\">\n$$m_{\\text{tan}} = f'(x_0) = \\lim_{h \\to 0} \\frac{f(x_0 + h) - f(x_0)}{h}$$\n</div>\n\n<h4>2. Equations of Tangent and Normal Lines</h4>\n<ul>\n  <li><strong>Tangent Line:</strong> Passing through $(x_0, y_0)$ with slope $m = f'(x_0)$:\n    <div class=\"math-display\">\n    $$y - f(x_0) = f'(x_0)(x - x_0)$$\n    </div>\n  </li>\n  <li><strong>Normal Line:</strong> The line perpendicular to the tangent line at $(x_0, y_0)$ (provided $f'(x_0) \\ne 0$, having slope $m_{\\perp} = -1/f'(x_0)$):\n    <div class=\"math-display\">\n    $$y - f(x_0) = -\\frac{1}{f'(x_0)}(x - x_0)$$\n    </div>\n  </li>\n</ul>",
          "simulation": "calc1-secant-tangent-sim",
          "simulations": [
            "calc1-secant-tangent-sim"
          ]
        },
        {
          "id": "u5-sec2",
          "title": "One-Sided Derivatives & Differentiability Implying Continuity",
          "content": "<h4>1. One-Sided Derivatives</h4>\n<div class=\"math-display\">\n$$\\begin{aligned}\n\\mathbf{\\text{Right-Hand Derivative: }} & f'_+(x_0) = \\lim_{h \\to 0^+} \\frac{f(x_0 + h) - f(x_0)}{h} \\\n\\mathbf{\\text{Left-Hand Derivative: }} & f'_-(x_0) = \\lim_{h \\to 0^-} \\frac{f(x_0 + h) - f(x_0)}{h}\n\\end{aligned}$$\n</div>\n<p>A function is differentiable at $x_0$ if and only if both one-sided derivatives exist as finite numbers and are equal: $f'(x_0) = f'_+(x_0) = f'_-(x_0)$.</p>\n\n<h4>2. Theorem: Differentiability Implies Continuity</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Theorem: If } f \\text{ is differentiable at } x_0, \\text{ then } f \\text{ is continuous at } x_0.}$$\n</div>\n<p><em>Proof:</em> To prove continuity, we must show that $\\lim_{x \\to x_0} [f(x) - f(x_0)] = 0$. For $x \\ne x_0$, write:</p>\n<div class=\"math-display\">\n$$f(x) - f(x_0) = \\frac{f(x) - f(x_0)}{x - x_0} \\cdot (x - x_0)$$\n</div>\n<p>Taking the limit as $x \\to x_0$ using the product limit law:</p>\n<div class=\"math-display\">\n$$\\lim_{x \\to x_0} [f(x) - f(x_0)] = \\left( \\lim_{x \\to x_0} \\frac{f(x) - f(x_0)}{x - x_0} \\right) \\cdot \\left( \\lim_{x \\to x_0} (x - x_0) \\right) = f'(x_0) \\cdot 0 = 0$$\n</div>\n<p>Thus $\\lim_{x \\to x_0} f(x) = f(x_0)$, proving that $f$ is continuous at $x_0 \\quad \\blacksquare$</p>\n\n<h4>3. The Converse is False: Geometric Non-Differentiability Modes</h4>\n<p>Continuity is a strictly weaker condition than differentiability. Functions may fail to be differentiable at points where they are continuous due to:</p>\n<ol>\n  <li><strong>Corner Point (Cusp):</strong> Left and right derivatives differ ($f(x) = |x|$ at $x = 0$, where $f'_-(0) = -1 \\ne f'_+(0) = +1$).</li>\n  <li><strong>Vertical Tangent:</strong> The difference quotient diverges to $\\pm\\infty$ ($f(x) = x^{1/3}$ at $x = 0$, where $f'(0) = \\lim_{h \\to 0} h^{1/3}/h = \\lim_{h \\to 0} 1/h^{2/3} = \\infty$).</li>\n  <li><strong>Wild Oscillation:</strong> $f(x) = x \\sin(1/x)$ for $x \\ne 0$ and $f(0) = 0$ is continuous at $x = 0$, but its difference quotient $\\sin(1/h)$ oscillates indefinitely between $-1$ and $+1$ as $h \\to 0$.</li>\n</ol>"
        },
        {
          "id": "u5-sec3",
          "title": "Fundamental Algebraic Differentiation Rules & Rigorous Proofs",
          "content": "<h4>1. The Power Rule</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\frac{d}{dx}[x^n] = n x^{n-1} \\quad \\forall n \\in \\mathbb{R}}$$\n</div>\n<p><em>Proof for $n \\in \\mathbb{N}$ via Binomial Theorem:</em></p>\n<div class=\"math-display\">\n$$\\begin{aligned}\n\\frac{d}{dx}[x^n] &= \\lim_{h \\to 0} \\frac{(x + h)^n - x^n}{h} = \\lim_{h \\to 0} \\frac{\\left( x^n + n x^{n-1} h + \\binom{n}{2} x^{n-2} h^2 + \\dots + h^n \\right) - x^n}{h} \\\n&= \\lim_{h \\to 0} \\left( n x^{n-1} + \\binom{n}{2} x^{n-2} h + \\dots + h^{n-1} \\right) = n x^{n-1} \\quad \\blacksquare\n\\end{aligned}$$\n</div>\n\n<h4>2. Linearity of the Derivative Operator</h4>\n<div class=\"math-display\">\n$$\\frac{d}{dx}[c f(x)] = c f'(x), \\qquad \\frac{d}{dx}[f(x) \\pm g(x)] = f'(x) \\pm g'(x)$$\n</div>\n\n<h4>3. The Product Rule & Line-by-Line Deductive Proof</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\frac{d}{dx}[f(x) g(x)] = f'(x) g(x) + f(x) g'(x)}$$\n</div>\n<p><em>Proof:</em> Form the difference quotient for the product $P(x) = f(x) g(x)$:</p>\n<div class=\"math-display\">\n$$\\frac{P(x + h) - P(x)}{h} = \\frac{f(x + h) g(x + h) - f(x) g(x)}{h}$$\n</div>\n<p>Add and subtract the strategic intermediate term $f(x) g(x + h)$ in the numerator:</p>\n<div class=\"math-display\">\n$$\\begin{aligned}\n&= \\frac{f(x + h) g(x + h) - f(x) g(x + h) + f(x) g(x + h) - f(x) g(x)}{h} \\\n&= \\left( \\frac{f(x + h) - f(x)}{h} \\right) g(x + h) + f(x) \\left( \\frac{g(x + h) - g(x)}{h} \\right)\n\\end{aligned}$$\n</div>\n<p>Taking the limit as $h \\to 0$: since $g$ is differentiable at $x$, it is continuous at $x$, so $\\lim_{h \\to 0} g(x + h) = g(x)$. Therefore:</p>\n<div class=\"math-display\">\n$$\\lim_{h \\to 0} \\frac{P(x + h) - P(x)}{h} = f'(x) g(x) + f(x) g'(x) \\quad \\blacksquare$$\n</div>\n\n<h4>4. The Quotient Rule</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\frac{d}{dx}\\left[ \\frac{f(x)}{g(x)} \\right] = \\frac{f'(x) g(x) - f(x) g'(x)}{[g(x)]^2} \\quad (g(x) \\ne 0)}$$\n</div>"
        },
        {
          "id": "u5-sec4",
          "title": "Derivatives of Trigonometric, Exponential & Hyperbolic Functions",
          "content": "<h4>1. Derivatives of Trigonometric Functions</h4>\n<p>Using the angle addition identity $\\sin(x + h) = \\sin x \\cos h + \\cos x \\sin h$:</p>\n<div class=\"math-display\">\n$$\\begin{aligned}\n\\frac{d}{dx}[\\sin x] &= \\lim_{h \\to 0} \\frac{\\sin(x + h) - \\sin x}{h} = \\lim_{h \\to 0} \\frac{\\sin x(\\cos h - 1) + \\cos x\\sin h}{h} \\\n&= \\sin x \\left( \\lim_{h \\to 0} \\frac{\\cos h - 1}{h} \\right) + \\cos x \\left( \\lim_{h \\to 0} \\frac{\\sin h}{h} \\right) = \\sin x(0) + \\cos x(1) = \\cos x\n\\end{aligned}$$\n</div>\n<p>Similarly, using the Quotient Rule:</p>\n<div class=\"math-display\">\n$$\\frac{d}{dx}[\\cos x] = -\\sin x, \\quad \\frac{d}{dx}[\\tan x] = \\sec^2 x, \\quad \\frac{d}{dx}[\\sec x] = \\sec x \\tan x, \\quad \\frac{d}{dx}[\\cot x] = -\\csc^2 x, \\quad \\frac{d}{dx}[\\csc x] = -\\csc x \\cot x$$\n</div>\n\n<h4>2. Derivatives of Exponential & Logarithmic Functions</h4>\n<div class=\"math-display\">\n$$\\frac{d}{dx}[e^x] = \\lim_{h \\to 0} \\frac{e^{x+h} - e^x}{h} = e^x \\lim_{h \\to 0} \\frac{e^h - 1}{h} = e^x (1) = e^x$$\n$$\\frac{d}{dx}[a^x] = a^x \\ln a, \\qquad \\frac{d}{dx}[\\ln x] = \\frac{1}{x} \\quad (x > 0), \\qquad \\frac{d}{dx}[\\log_a x] = \\frac{1}{x \\ln a}$$\n</div>\n\n<h4>3. Derivatives of Hyperbolic Functions</h4>\n<div class=\"math-display\">\n$$\\frac{d}{dx}[\\sinh x] = \\frac{d}{dx}\\left[\\frac{e^x - e^{-x}}{2}\\right] = \\frac{e^x + e^{-x}}{2} = \\cosh x$$\n$$\\frac{d}{dx}[\\cosh x] = \\sinh x, \\qquad \\frac{d}{dx}[\\tanh x] = \\operatorname{sech}^2 x, \\qquad \\frac{d}{dx}[\\operatorname{sech} x] = -\\operatorname{sech} x \\tanh x$$\n</div>"
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "Derivatives via Product and Quotient Rules",
          "statement": "Compute the exact derivative $f'(x)$ for: (a) $f(x) = (3x^2 - 5x + 2) e^x$, and (b) $g(x) = \\frac{x^2 \\sin x}{x + \\cos x}$.",
          "steps": [
            {
              "step": "Step 1: Apply Product Rule to (a)",
              "math": "f'(x) = \\frac{d}{dx}[3x^2 - 5x + 2] e^x + (3x^2 - 5x + 2) \\frac{d}{dx}[e^x] = (6x - 5) e^x + (3x^2 - 5x + 2) e^x",
              "explanation": "Differentiating term by term and factoring out $e^x$."
            },
            {
              "step": "Step 2: Simplify (a)",
              "math": "f'(x) = (3x^2 + x - 3) e^x",
              "explanation": "Combining like algebraic polynomial coefficients."
            },
            {
              "step": "Step 3: Apply Quotient Rule to (b)",
              "math": "g'(x) = \\frac{\\frac{d}{dx}[x^2 \\sin x] (x + \\cos x) - (x^2 \\sin x) \\frac{d}{dx}[x + \\cos x]}{(x + \\cos x)^2}",
              "explanation": "Compute numerator derivative: $\\frac{d}{dx}[x^2 \\sin x] = 2x \\sin x + x^2 \\cos x$. Compute denominator derivative: $\\frac{d}{dx}[x + \\cos x] = 1 - \\sin x$."
            },
            {
              "step": "Step 4: Expand and Assemble (b)",
              "math": "g'(x) = \\frac{(2x \\sin x + x^2 \\cos x)(x + \\cos x) - x^2 \\sin x (1 - \\sin x)}{(x + \\cos x)^2}",
              "explanation": "This gives the exact derivative."
            }
          ],
          "answer": "f'(x) = (3x^2 + x - 3) e^x, \\qquad g'(x) = \\frac{(2x \\sin x + x^2 \\cos x)(x + \\cos x) - x^2 \\sin x (1 - \\sin x)}{(x + \\cos x)^2}"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "Tangent and Normal Line Equations to a Transcendental Curve",
          "statement": "Find the exact Cartesian equations of the tangent line and the normal line to the curve $y = f(x) = x^2 \\ln(x) - 3x$ at the point where $x = 1$.",
          "steps": [
            {
              "step": "Step 1: Compute Point Coordinates $(x_0, y_0)$",
              "math": "y_0 = f(1) = 1^2 \\ln(1) - 3(1) = 0 - 3 = -3",
              "explanation": "The point of tangency on the curve is $(1, -3)$."
            },
            {
              "step": "Step 2: Compute Derivative $f'(x)$",
              "math": "f'(x) = \\frac{d}{dx}[x^2 \\ln x] - \\frac{d}{dx}[3x] = \\left( 2x \\ln x + x^2 \\cdot \\frac{1}{x} \\right) - 3 = 2x \\ln x + x - 3",
              "explanation": "Applying the Product Rule to $x^2 \\ln x$."
            },
            {
              "step": "Step 3: Evaluate Tangent Slope at $x = 1$",
              "math": "m_{\\text{tan}} = f'(1) = 2(1) \\ln(1) + 1 - 3 = 0 + 1 - 3 = -2",
              "explanation": "The tangent slope is $m = -2$. The normal slope is $m_{\\perp} = -1/(-2) = 1/2$."
            },
            {
              "step": "Step 4: Formulate Line Equations",
              "math": "\\text{Tangent: } y - (-3) = -2(x - 1) \\implies y = -2x - 1 \\\\ \\text{Normal: } y - (-3) = \\frac{1}{2}(x - 1) \\implies y = \\frac{1}{2}x - \\frac{7}{2}",
              "explanation": "Writing in slope-intercept form."
            }
          ],
          "answer": "\\text{Tangent Line: } y = -2x - 1, \\qquad \\text{Normal Line: } y = \\frac{1}{2}x - \\frac{7}{2}"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "Differentiability vs Continuity Analysis of an Oscillatory Piecewise Function",
          "statement": "Consider the function $f(x) = \\begin{cases} x^2 \\sin\\left(\\frac{1}{x}\\right), & x \\ne 0 \\\\ 0, & x = 0 \\end{cases}$. (a) Prove using the limit definition that $f'(0)$ exists and find its value. (b) For $x \\ne 0$, compute $f'(x)$. (c) Prove that $\\lim_{x \\to 0} f'(x)$ does NOT exist, and explain why this demonstrates that a derivative function need not be continuous.",
          "steps": [
            {
              "step": "Step 1: Evaluate $f'(0)$ from the Definition of Derivative",
              "math": "f'(0) = \\lim_{h \\to 0} \\frac{f(0 + h) - f(0)}{h} = \\lim_{h \\to 0} \\frac{h^2 \\sin(1/h) - 0}{h} = \\lim_{h \\to 0} h \\sin\\left(\\frac{1}{h}\\right)",
              "explanation": "We must evaluate this limit as $h \to 0$."
            },
            {
              "step": "Step 2: Apply the Squeeze Theorem to $f'(0)$",
              "math": "-1 \\le \\sin(1/h) \\le 1 \\implies -|h| \\le h \\sin(1/h) \\le |h| \\implies \\lim_{h \\to 0} h \\sin(1/h) = 0",
              "explanation": "Because $\\lim_{h \to 0} (\\pm|h|) = 0$, the Squeeze Theorem guarantees that $f'(0) = 0$ exists."
            },
            {
              "step": "Step 3: Compute $f'(x)$ for $x \ne 0$",
              "math": "f'(x) = \\frac{d}{dx}[x^2] \\sin(1/x) + x^2 \\frac{d}{dx}[\\sin(1/x)] = 2x \\sin\\left(\\frac{1}{x}\\right) + x^2 \\cos\\left(\\frac{1}{x}\\right)\\left(-\\frac{1}{x^2}\\right) = 2x \\sin\\left(\\frac{1}{x}\\right) - \\cos\\left(\\frac{1}{x}\\right)",
              "explanation": "Applying product and chain rules for $x \ne 0$."
            },
            {
              "step": "Step 4: Prove Non-Existence of $\\lim_{x \to 0} f'(x)$",
              "math": "\\lim_{x \\to 0} f'(x) = \\lim_{x \\to 0} \\left[ 2x \\sin\\left(\\frac{1}{x}\\right) - \\cos\\left(\\frac{1}{x}\\right) \\right] = 0 - \\lim_{x \\to 0} \\cos\\left(\\frac{1}{x}\\right) \\quad (\\text{DNE})",
              "explanation": "As $x \to 0$, $2x \\sin(1/x) \to 0$ by squeezing, but $\\cos(1/x)$ oscillates between $-1$ and $+1$ infinitely often. Thus $\\lim_{x \to 0} f'(x)$ does not exist. Since $\\lim_{x \to 0} f'(x) \ne f'(0) = 0$, the derivative $f'(x)$ is discontinuous at $x = 0$, providing a classic counterexample."
            }
          ],
          "answer": "f'(0) = 0 \\text{ exists}; \\quad f'(x) = 2x\\sin(1/x) - \\cos(1/x) \\text{ for } x \\ne 0; \\quad \\lim_{x \\to 0} f'(x) \\text{ DNE (discontinuous derivative)}"
        }
      ],
      "simulations": [
        "calc1-secant-tangent-sim"
      ],
      "id": "unit5",
      "unitId": "unit5-calc1",
      "leadSummary": "Rigorous theory of differentiation: secant-to-tangent limiting process, Newton difference quotient, one-sided derivatives, proof that differentiability implies continuity, failure modes (cusps, vertical tangents, wild oscillations), power rule, product rule proof, quotient rule, and derivatives of trigonometric, exponential, and hyperbolic functions."
    },
    {
      "unitNumber": 6,
      "number": 6,
      "title": "The Chain Rule, Inverse Functions, Higher Derivatives & The Leibniz Rule",
      "description": "Advanced differential mechanics: Caratheodory formulation and proof of the Chain Rule, implicit differentiation of algebraic curves, derivatives of inverse functions, inverse trigonometric and inverse hyperbolic derivatives, logarithmic differentiation, and the General Leibniz Rule for the n-th derivative of a product with mathematical induction proof.",
      "sections": [
        {
          "id": "u6-sec1",
          "title": "The Chain Rule Theorem & Rigorous Carath\u00e9odory Formulation",
          "content": "<h4>1. Statement of the Chain Rule Theorem</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Theorem: If } g \\text{ is differentiable at } x_0 \\text{ and } f \\text{ is differentiable at } g(x_0), \\text{ then the composite function } (f \\circ g) \\text{ is differentiable at } x_0 \\text{ with:}}$$\n$$\\mathbf{(f \\circ g)'(x_0) = f'(g(x_0)) \\cdot g'(x_0) \\quad \\text{or in Leibniz notation: } \\frac{dy}{dx} = \\frac{dy}{du} \\cdot \\frac{du}{dx}}$$\n</div>\n\n<h4>2. The Classic Proof Pitfall & Carath\u00e9odory's Resolution</h4>\n<p>The naive attempt writes $\\frac{\\Delta y}{\\Delta x} = \\frac{\\Delta y}{\\Delta u} \\cdot \\frac{\\Delta u}{\\Delta x}$. This fails whenever $\\Delta u = g(x_0 + h) - g(x_0) = 0$ for values of $h \\ne 0$ (division by zero).</p>\n<p><strong>Carath\u00e9odory's Theorem:</strong> A function $f$ is differentiable at $u_0$ if and only if there exists a function $\\Phi(u)$ that is continuous at $u_0$ such that for all $u$:</p>\n<div class=\"math-display\">\n$$f(u) - f(u_0) = \\Phi(u)(u - u_0), \\quad \\text{with } \\Phi(u_0) = f'(u_0)$$\n</div>\n<p><em>Rigorous Proof of Chain Rule:</em> Let $u = g(x)$ and $u_0 = g(x_0)$. By Carath\u00e9odory's characterization for $f$ at $u_0$:</p>\n<div class=\"math-display\">\n$$f(g(x)) - f(g(x_0)) = \\Phi(g(x)) [g(x) - g(x_0)]$$\n</div>\n<p>Dividing by $x - x_0$ for $x \\ne x_0$:</p>\n<div class=\"math-display\">\n$$\\frac{f(g(x)) - f(g(x_0))}{x - x_0} = \\Phi(g(x)) \\cdot \\frac{g(x) - g(x_0)}{x - x_0}$$\n</div>\n<p>As $x \\to x_0$: because $g$ is differentiable at $x_0$, it is continuous at $x_0$, so $\\lim_{x \\to x_0} g(x) = g(x_0) = u_0$. Since $\\Phi$ is continuous at $u_0$, $\\lim_{x \\to x_0} \\Phi(g(x)) = \\Phi(u_0) = f'(g(x_0))$. Thus:</p>\n<div class=\"math-display\">\n$$(f \\circ g)'(x_0) = f'(g(x_0)) \\cdot g'(x_0) \\quad \\blacksquare$$\n</div>"
        },
        {
          "id": "u6-sec2",
          "title": "Implicit Differentiation & Geometry of Algebraic Plane Curves",
          "content": "<h4>1. Implicit Functions & The Method of Implicit Differentiation</h4>\n<p>An equation of the form $F(x, y) = 0$ defines $y$ as an <strong>implicit function</strong> of $x$. Instead of solving explicitly for $y = f(x)$, we differentiate both sides of $F(x, y) = 0$ with respect to $x$, treating $y$ as an unknown differentiable function of $x$ and applying the Chain Rule $\\frac{d}{dx}[g(y)] = g'(y) \\frac{dy}{dx}$:</p>\n<div class=\"math-display\">\n$$\\frac{d}{dx}[F(x, y)] = 0 \\implies \\text{Solve algebraically for } \\frac{dy}{dx}$$\n</div>\n\n<h4>2. Higher-Order Implicit Derivatives</h4>\n<p>To find the second derivative $\\frac{d^2y}{dx^2}$, differentiate the expression for $\\frac{dy}{dx}$ with respect to $x$, applying the Quotient Rule, Product Rule, and Chain Rule, and then substitute the expression for $\\frac{dy}{dx}$ to express $\\frac{d^2y}{dx^2}$ purely in terms of $x$ and $y$.</p>",
          "simulation": "calc1-implicit-slope-sim",
          "simulations": [
            "calc1-implicit-slope-sim"
          ]
        },
        {
          "id": "u6-sec3",
          "title": "Derivatives of Inverse Functions & Inverse Transcendental Relations",
          "content": "<h4>1. Derivative of the Inverse Function Theorem</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Theorem: If } f \\text{ is strictly monotonic and differentiable at } x_0 \\text{ with } f'(x_0) \\ne 0, \\text{ then } f^{-1} \\text{ is differentiable at } y_0 = f(x_0) \\text{ with:}}$$\n$$(f^{-1})'(y_0) = \\frac{1}{f'(x_0)} = \\frac{1}{f'(f^{-1}(y_0))} \\quad \\text{or } \\frac{dx}{dy} = \\frac{1}{\\frac{dy}{dx}}$$\n</div>\n\n<h4>2. Derivatives of Inverse Trigonometric Functions</h4>\n<p>Let $y = \\arcsin x$ for $x \\in (-1, 1)$. Then $x = \\sin y$ with $y \\in (-\\pi/2, \\pi/2)$:</p>\n<div class=\"math-display\">\n$$\\frac{d}{dx}[x] = \\frac{d}{dx}[\\sin y] \\implies 1 = \\cos y \\frac{dy}{dx} \\implies \\frac{dy}{dx} = \\frac{1}{\\cos y} = \\frac{1}{\\sqrt{1 - \\sin^2 y}} = \\frac{1}{\\sqrt{1 - x^2}}$$\n</div>\n<p>Similarly:</p>\n<div class=\"math-display\">\n$$\\frac{d}{dx}[\\arccos x] = -\\frac{1}{\\sqrt{1 - x^2}}, \\qquad \\frac{d}{dx}[\\arctan x] = \\frac{1}{1 + x^2}, \\qquad \\frac{d}{dx}[\\operatorname{arcsec} x] = \\frac{1}{|x|\\sqrt{x^2 - 1}}$$\n</div>\n\n<h4>3. Derivatives of Inverse Hyperbolic Functions</h4>\n<div class=\"math-display\">\n$$\\frac{d}{dx}[\\operatorname{arsinh} x] = \\frac{1}{\\sqrt{x^2 + 1}}, \\qquad \\frac{d}{dx}[\\operatorname{arcosh} x] = \\frac{1}{\\sqrt{x^2 - 1}} \\quad (x > 1), \\qquad \\frac{d}{dx}[\\operatorname{artanh} x] = \\frac{1}{1 - x^2} \\quad (|x| < 1)$$\n</div>"
        },
        {
          "id": "u6-sec4",
          "title": "Logarithmic Differentiation & Successive Higher-Order Derivatives",
          "content": "<h4>1. Logarithmic Differentiation</h4>\n<p>For functions involving complicated products, quotients, or variable powers $y = [u(x)]^{v(x)}$:</p>\n<ol>\n  <li>Take the natural logarithm of both sides: $\\ln y = v(x) \\ln u(x)$.</li>\n  <li>Differentiate implicitly with respect to $x$: $\\frac{1}{y} \\frac{dy}{dx} = v'(x) \\ln u(x) + v(x) \\frac{u'(x)}{u(x)}$.</li>\n  <li>Multiply through by $y$: $\\frac{dy}{dx} = [u(x)]^{v(x)} \\left[ v'(x) \\ln u(x) + \\frac{v(x) u'(x)}{u(x)} \\right]$.</li>\n</ol>\n\n<h4>2. Successive Derivatives & Notations</h4>\n<p>The $n$-th derivative $f^{(n)}(x) = \\frac{d^n y}{dx^n}$ is obtained by iteratively differentiating $n$ times.</p>\n\n<h4>3. The General Leibniz Rule for the $n$-th Derivative of a Product</h4>\n<div class=\"math-display\">\n$$\\mathbf{(f \\cdot g)^{(n)}(x) = \\sum_{k=0}^n \\binom{n}{k} f^{(n-k)}(x) g^{(k)}(x)}$$\n</div>\n<p>where $\\binom{n}{k} = \\frac{n!}{k!(n-k)!}$ are binomial coefficients. This theorem is proven rigorously by mathematical induction using Pascal's identity $\\binom{n}{k-1} + \\binom{n}{k} = \\binom{n+1}{k}$.</p>"
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "Logarithmic Differentiation of Variable Exponent Towers",
          "statement": "Find the exact derivative $\\frac{dy}{dx}$ for: (a) $y = x^{\\sin x}$ for $x > 0$, and (b) $y = \\frac{(x^2 + 1)^3 \\sqrt{2x + 5}}{(3x - 1)^4}$ at $x = 2$.",
          "steps": [
            {
              "step": "Step 1: Take Logarithm of (a)",
              "math": "\\ln y = \\ln(x^{\\sin x}) = \\sin x \\ln x",
              "explanation": "Convert exponent into product."
            },
            {
              "step": "Step 2: Differentiate Implicitly for (a)",
              "math": "\\frac{1}{y}\\frac{dy}{dx} = \\cos x \\ln x + \\sin x \\left(\\frac{1}{x}\\right) \\implies \\frac{dy}{dx} = x^{\\sin x} \\left[ \\cos x \\ln x + \\frac{\\sin x}{x} \\right]",
              "explanation": "Multiplying through by $y = x^{\\sin x}$."
            },
            {
              "step": "Step 3: Logarithmic Differentiation for (b)",
              "math": "\\ln y = 3\\ln(x^2 + 1) + \\frac{1}{2}\\ln(2x + 5) - 4\\ln(3x - 1)",
              "explanation": "Expand product and quotient using log laws."
            },
            {
              "step": "Step 4: Differentiate and Evaluate at $x = 2$",
              "math": "\\frac{1}{y}\\frac{dy}{dx} = 3\\left(\\frac{2x}{x^2+1}\\right) + \\frac{1}{2}\\left(\\frac{2}{2x+5}\\right) - 4\\left(\\frac{3}{3x-1}\\right) = 3\\left(\\frac{4}{5}\\right) + \\frac{1}{9} - 4\\left(\\frac{3}{5}\\right) = \\frac{12}{5} + \\frac{1}{9} - \\frac{12}{5} = \\frac{1}{9}",
              "explanation": "At $x = 2$, $y = \\frac{(5)^3 \\sqrt{9}}{(5)^4} = \\frac{125 \times 3}{625} = \\frac{3}{5}$. Thus $\\frac{dy}{dx} = \\left(\\frac{3}{5}\\right)\\left(\\frac{1}{9}\\right) = \\frac{1}{15}$."
            }
          ],
          "answer": "\\text{(a) } \\frac{dy}{dx} = x^{\\sin x}\\left[\\cos x \\ln x + \\frac{\\sin x}{x}\\right], \\qquad \\text{(b) } \\left.\\frac{dy}{dx}\\right|_{x=2} = \\frac{1}{15}"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "Implicit Differentiation and Second Derivative of the Folium of Descartes",
          "statement": "Consider the Folium of Descartes $x^3 + y^3 = 6xy$. (a) Find the derivative $\\frac{dy}{dx}$ in terms of $x$ and $y$. (b) Find the equation of the tangent line at the symmetric point $(3, 3)$. (c) Compute the second derivative $\\frac{d^2y}{dx^2}$ at $(3, 3)$.",
          "steps": [
            {
              "step": "Step 1: Differentiate Implicitly with Respect to $x$",
              "math": "3x^2 + 3y^2 \\frac{dy}{dx} = 6\\left(y + x \\frac{dy}{dx}\\right) \\implies x^2 + y^2 \\frac{dy}{dx} = 2y + 2x \\frac{dy}{dx}",
              "explanation": "Dividing by 3 and applying the product rule to $6xy$."
            },
            {
              "step": "Step 2: Solve for $\\frac{dy}{dx}$",
              "math": "\\frac{dy}{dx}(y^2 - 2x) = 2y - x^2 \\implies \\frac{dy}{dx} = \\frac{2y - x^2}{y^2 - 2x}",
              "explanation": "Isolating $\\frac{dy}{dx}$."
            },
            {
              "step": "Step 3: Evaluate Tangent Line at $(3, 3)$",
              "math": "\\left.\\frac{dy}{dx}\\right|_{(3,3)} = \\frac{2(3) - 3^2}{3^2 - 2(3)} = \\frac{6 - 9}{9 - 6} = \\frac{-3}{3} = -1 \\implies y - 3 = -1(x - 3) \\implies y = -x + 6",
              "explanation": "The tangent line at $(3, 3)$ has slope $m = -1$."
            },
            {
              "step": "Step 4: Compute Second Derivative $\\frac{d^2y}{dx^2}$ at $(3,3)$",
              "math": "\\frac{d^2y}{dx^2} = \\frac{(2y' - 2x)(y^2 - 2x) - (2y - x^2)(2yy' - 2)}{(y^2 - 2x)^2}",
              "explanation": "Substituting $x = 3, y = 3, y' = -1$: numerator is $[2(-1) - 6](9 - 6) - (6 - 9)[2(3)(-1) - 2] = [-8](3) - (-3)[-8] = -24 - 24 = -48$. Denominator is $(9 - 6)^2 = 9$. Thus $\\frac{d^2y}{dx^2} = -\\frac{48}{9} = -\\frac{16}{3}$."
            }
          ],
          "answer": "\\frac{dy}{dx} = \\frac{2y - x^2}{y^2 - 2x}, \\quad \\text{Tangent: } y = -x + 6, \\quad \\left.\\frac{d^2y}{dx^2}\\right|_{(3,3)} = -\\frac{16}{3}"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "General Leibniz Rule for Higher Derivatives & Mathematical Induction",
          "statement": "(a) Prove the General Leibniz Rule $(fg)^{(n)} = \\sum_{k=0}^n \\binom{n}{k} f^{(n-k)} g^{(k)}$ by mathematical induction for all $n \\in \\mathbb{N}$. (b) Apply the Leibniz rule to compute the exact 10th derivative $y^{(10)}$ of $y = x^3 e^{2x}$.",
          "steps": [
            {
              "step": "Step 1: Base Case $n = 1$",
              "math": "(fg)' = \\binom{1}{0} f' g + \\binom{1}{1} f g' = f' g + f g'",
              "explanation": "This matches the standard Product Rule, establishing the base case."
            },
            {
              "step": "Step 2: Inductive Step using Pascal's Identity",
              "math": "(fg)^{(n+1)} = \\frac{d}{dx}\\left[ \\sum_{k=0}^n \\binom{n}{k} f^{(n-k)} g^{(k)} \\right] = \\sum_{k=0}^n \\binom{n}{k} f^{(n+1-k)} g^{(k)} + \\sum_{k=0}^n \\binom{n}{k} f^{(n-k)} g^{(k+1)}",
              "explanation": "Re-indexing the second sum and combining via Pascal's identity $\\binom{n}{k} + \\binom{n}{k-1} = \\binom{n+1}{k}$ yields $\\sum_{k=0}^{n+1} \\binom{n+1}{k} f^{(n+1-k)} g^{(k)} \\quad \\blacksquare$."
            },
            {
              "step": "Step 3: Apply to $y = x^3 e^{2x}$ with $n = 10$",
              "math": "f(x) = e^{2x} \\implies f^{(m)}(x) = 2^m e^{2x}; \\qquad g(x) = x^3",
              "explanation": "Notice $g'(x) = 3x^2, g''(x) = 6x, g'''(x) = 6$, and $g^{(k)}(x) = 0$ for all $k \\ge 4$. Thus only terms $k = 0, 1, 2, 3$ survive!"
            },
            {
              "step": "Step 4: Compute the Surviving 4 Terms",
              "math": "\\begin{aligned}\ny^{(10)} &= \\binom{10}{0} 2^{10} e^{2x} (x^3) + \\binom{10}{1} 2^9 e^{2x} (3x^2) + \\binom{10}{2} 2^8 e^{2x} (6x) + \\binom{10}{3} 2^7 e^{2x} (6) \\\n&= e^{2x} 2^7 \\left[ 2^3 x^3 + 10(2^2)(3x^2) + 45(2)(6x) + 120(6) \\right] \\\n&= 128 e^{2x} \\left[ 8x^3 + 120x^2 + 540x + 720 \\right] = 1024 e^{2x} \\left[ x^3 + 15x^2 + \\frac{135}{2}x + 90 \\right]\n\\end{aligned}",
              "explanation": "Factor out common powers of 2."
            }
          ],
          "answer": "y^{(10)} = 1024 e^{2x} \\left( x^3 + 15x^2 + \\frac{135}{2}x + 90 \\right) = 128 e^{2x} (8x^3 + 120x^2 + 540x + 720)"
        }
      ],
      "simulations": [
        "calc1-implicit-slope-sim"
      ],
      "id": "unit6",
      "unitId": "unit6-calc1",
      "leadSummary": "Advanced differential mechanics: Caratheodory formulation and proof of the Chain Rule, implicit differentiation of algebraic curves, derivatives of inverse functions, inverse trigonometric and inverse hyperbolic derivatives, logarithmic differentiation, and the General Leibniz Rule for the n-th derivative of a product with mathematical induction proof."
    },
    {
      "unitNumber": 7,
      "number": 7,
      "title": "Mean Value Theorems, Taylor Approximations & L'H\u00f4pital's Rule",
      "description": "The deep theoretical core of differential calculus: Rolle's theorem and proof via EVT and Fermat's theorem, Lagrange's Mean Value Theorem, zero-derivative constant function theorem, Cauchy generalized MVT, rigorous proof of L'Hopital's rule for 0/0 and infinity/infinity, resolution of exponential indeterminate forms, and linear differentials.",
      "sections": [
        {
          "id": "u7-sec1",
          "title": "Rolle's Theorem & Lagrange's Mean Value Theorem (MVT)",
          "content": "<h4>1. Rolle's Theorem</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Theorem (Rolle): Let } f: [a, b] \\to \\mathbb{R} \\text{ satisfy:}}$$\n$$\\mathbf{1. } f \\text{ is continuous on the closed interval } [a, b],$$\n$$\\mathbf{2. } f \\text{ is differentiable on the open interval } (a, b), \\text{ and}$$\n$$\\mathbf{3. } f(a) = f(b).$$\n$$\\mathbf{\\text{Then there exists at least one number } c \\in (a, b) \\text{ such that } f'(c) = 0.}$$\n</div>\n<p><em>Rigorous Proof:</em> By the Extreme Value Theorem, continuous $f$ on $[a, b]$ attains an absolute maximum $M$ and minimum $m$.</p>\n<ul>\n  <li><strong>Case 1 (Constant Function):</strong> If $M = m$, then $f(x)$ is constant on $[a, b]$. Thus $f'(x) = 0$ for every $x \\in (a, b)$, and any $c \\in (a, b)$ satisfies the theorem.</li>\n  <li><strong>Case 2 (Non-Constant Function):</strong> Since $f(a) = f(b)$, at least one of the extrema (say the maximum $M$) must be attained at an interior point $c \\in (a, b)$. Since $f$ is differentiable at $c$ and attains a local maximum, Fermat's Interior Extremum Theorem forces $f'(c) = 0 \\quad \\blacksquare$</li>\n</ul>\n\n<h4>2. Lagrange's Mean Value Theorem (MVT)</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Theorem (MVT): If } f \\in C[a, b] \\text{ and } f \\in D(a, b), \\text{ then there exists at least one } c \\in (a, b) \\text{ such that:}}$$\n$$\\mathbf{f'(c) = \\frac{f(b) - f(a)}{b - a} \\quad \\iff \\quad f(b) - f(a) = f'(c)(b - a)}$$\n</div>\n<p><em>Geometric Meaning:</em> There exists an interior point $c$ where the instantaneous rate of change (tangent slope) is strictly parallel to the average rate of change (secant slope connecting endpoints $(a, f(a))$ and $(b, f(b))$).</p>\n<p><em>Proof via Rolle's Theorem:</em> Construct the auxiliary function measuring the vertical distance between the curve and the secant line:</p>\n<div class=\"math-display\">\n$$h(x) = f(x) - f(a) - \\left[\\frac{f(b) - f(a)}{b - a}\\right](x - a)$$\n</div>\n<p>Notice $h(a) = 0$ and $h(b) = 0$. Since $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, $h(x)$ satisfies all hypotheses of Rolle's Theorem on $[a, b]$. Thus $\\exists c \\in (a, b)$ with $h'(c) = 0$:</p>\n<div class=\"math-display\">\n$$h'(c) = f'(c) - \\frac{f(b) - f(a)}{b - a} = 0 \\implies f'(c) = \\frac{f(b) - f(a)}{b - a} \\quad \\blacksquare$$\n</div>",
          "simulation": "calc1-mvt-rolle-sim",
          "simulations": [
            "calc1-mvt-rolle-sim"
          ]
        },
        {
          "id": "u7-sec2",
          "title": "Fundamental Corollaries of the MVT & Monotonicity Criteria",
          "content": "<h4>1. The Zero-Derivative Constant Function Theorem</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Corollary 1: If } f'(x) = 0 \\text{ for all } x \\in (a, b), \\text{ then } f(x) \\text{ is constant on } (a, b).}$$\n</div>\n<p><em>Proof:</em> Choose any two points $x_1 < x_2$ in $(a, b)$. By the MVT on $[x_1, x_2]$, $\\exists c \\in (x_1, x_2)$ such that $f(x_2) - f(x_1) = f'(c)(x_2 - x_1) = 0 \\cdot (x_2 - x_1) = 0$. Thus $f(x_1) = f(x_2)$ for all pairs, proving $f(x) \\equiv C \\quad \\blacksquare$</p>\n\n<h4>2. Functions Differing by a Constant</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Corollary 2: If } f'(x) = g'(x) \\text{ for all } x \\in (a, b), \\text{ then } f(x) = g(x) + C \\text{ for some constant } C \\in \\mathbb{R}.}$$\n</div>\n<p>This is the fundamental justification for the $+ C$ constant of integration in antiderivatives.</p>\n\n<h4>3. Monotonicity Test Criteria</h4>\n<div class=\"math-display\">\n$$\\begin{aligned}\nf'(x) > 0 \\quad \\forall x \\in (a, b) &\\implies f \\text{ is strictly increasing on } [a, b] \\\nf'(x) < 0 \\quad \\forall x \\in (a, b) &\\implies f \\text{ is strictly decreasing on } [a, b]\n\\end{aligned}$$\n</div>"
        },
        {
          "id": "u7-sec3",
          "title": "Cauchy's Generalized Mean Value Theorem & Rigorous L'H\u00f4pital's Rule",
          "content": "<h4>1. Cauchy's Generalized Mean Value Theorem</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Theorem: If } f, g \\in C[a, b] \\text{ and } f, g \\in D(a, b) \\text{ with } g'(x) \\ne 0 \\text{ on } (a, b), \\text{ then there exists } c \\in (a, b) \\text{ such that:}}$$\n$$\\mathbf{\\frac{f'(c)}{g'(c)} = \\frac{f(b) - f(a)}{g(b) - g(a)}}$$\n</div>\n<p><em>Proof:</em> By Rolle's Theorem on $g(x)$, $g(b) \\ne g(a)$ (otherwise $g'(c) = 0$). Construct $H(x) = [f(b) - f(a)]g(x) - [g(b) - g(a)]f(x)$. Since $H(a) = H(b) = f(b)g(a) - g(b)f(a)$, Rolle's theorem yields $H'(c) = 0 \\implies [f(b)-f(a)]g'(c) = [g(b)-g(a)]f'(c) \\quad \\blacksquare$</p>\n\n<h4>2. L'H\u00f4pital's Rule for Indeterminate Forms 0/0 and $\\infty/\\infty$</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Theorem: Suppose } \\lim_{x \\to c} f(x) = 0 \\text{ and } \\lim_{x \\to c} g(x) = 0 \\text{ (or both } \\pm\\infty\\text{)}. \\text{ If } \\lim_{x \\to c} \\frac{f'(x)}{g'(x)} = L \\text{ exists (or is } \\pm\\infty\\text{)}, \\text{ then:}}$$\n$$\\mathbf{\\lim_{x \\to c} \\frac{f(x)}{g(x)} = \\lim_{x \\to c} \\frac{f'(x)}{g'(x)} = L}$$\n</div>\n<p><em>Proof for $0/0$:</em> Define $f(c) = g(c) = 0$ to make $f, g$ continuous at $c$. For any $x$ near $c$, by Cauchy's MVT on $[c, x]$ (or $[x, c]$), there exists $x_1$ strictly between $c$ and $x$ such that:</p>\n<div class=\"math-display\">\n$$\\frac{f(x)}{g(x)} = \\frac{f(x) - f(c)}{g(x) - g(c)} = \\frac{f'(x_1)}{g'(x_1)}$$\n</div>\n<p>As $x \\to c$, $x_1 \\to c$ by squeezing. Thus $\\lim_{x \\to c} \\frac{f(x)}{g(x)} = \\lim_{x_1 \\to c} \\frac{f'(x_1)}{g'(x_1)} = L \\quad \\blacksquare$</p>\n\n<h4>3. Resolution of Other Indeterminate Forms</h4>\n<ul>\n  <li><strong>Product $0 \\cdot \\infty$:</strong> Rewrite $f \\cdot g = \\frac{f}{1/g}$ or $\\frac{g}{1/f}$ to convert to $\\frac{0}{0}$ or $\\frac{\\infty}{\\infty}$.</li>\n  <li><strong>Difference $\\infty - \\infty$:</strong> Find a common algebraic denominator or rationalize.</li>\n  <li><strong>Exponential Forms $0^0, 1^\\infty, \\infty^0$:</strong> Let $y = [f(x)]^{g(x)}$, take logarithms $\\ln y = g(x) \\ln f(x)$ (which becomes $0 \\cdot \\infty$), evaluate limit $L$, and recover $\\lim y = e^L$.</li>\n</ul>"
        },
        {
          "id": "u7-sec4",
          "title": "Linear Approximations, Differentials & Error Propagation",
          "content": "<h4>1. Linear (Tangent Line) Approximation</h4>\n<p>The tangent line to $y = f(x)$ at $x = x_0$ provides the optimal first-order linear approximation $L(x) \\approx f(x)$ for values of $x$ close to $x_0$:</p>\n<div class=\"math-display\">\n$$L(x) = f(x_0) + f'(x_0)(x - x_0)$$\n</div>\n\n<h4>2. Differentials</h4>\n<p>Let $y = f(x)$. If $dx = \\Delta x$ represents an independent change in the input, the <strong>differential</strong> $dy$ represents the corresponding change along the tangent line:</p>\n<div class=\"math-display\">\n$$dy = f'(x) dx$$\n</div>\n<p>While the actual change along the curve is $\\Delta y = f(x + \\Delta x) - f(x)$, for small $dx$ we have $\\Delta y \\approx dy$.</p>\n\n<h4>3. Error Estimation Metrics</h4>\n<ul>\n  <li><strong>Absolute Error:</strong> $\\Delta y \\approx dy = f'(x_0) dx$</li>\n  <li><strong>Relative Error:</strong> $\\frac{\\Delta y}{y} \\approx \\frac{dy}{y} = \\frac{f'(x_0) dx}{f(x_0)}$</li>\n  <li><strong>Percentage Error:</strong> $\\left( \\frac{dy}{y} \\right) \\times 100\\%$</li>\n</ul>"
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "L'H\u00f4pital Evaluation of Exponential Indeterminate Form 1^\u221e",
          "statement": "Evaluate the exact limit using L'H\u00f4pital's Rule: $\\lim_{x \\to 0} (1 + 3x)^{2/x}$.",
          "steps": [
            {
              "step": "Step 1: Identify Indeterminate Form and Take Logarithm",
              "math": "\\text{As } x \\to 0, \\quad (1 + 3(0))^{2/0} = [1^\\infty]. \\quad \\text{Let } y = (1 + 3x)^{2/x}",
              "explanation": "Taking natural log of both sides converts power to product:"
            },
            {
              "step": "Step 2: Transform into Fraction for L'H\u00f4pital",
              "math": "\\ln y = \\frac{2}{x} \\ln(1 + 3x) = \\frac{2\\ln(1 + 3x)}{x}",
              "explanation": "As $x \to 0$, numerator is $2\\ln(1) = 0$ and denominator is $0$, which is the indeterminate form $0/0$."
            },
            {
              "step": "Step 3: Apply L'H\u00f4pital's Rule",
              "math": "\\lim_{x \\to 0} \\ln y = \\lim_{x \\to 0} \\frac{\\frac{d}{dx}[2\\ln(1 + 3x)]}{\\frac{d}{dx}[x]} = \\lim_{x \\to 0} \\frac{2 \\left(\\frac{3}{1 + 3x}\\right)}{1} = \\frac{6}{1 + 0} = 6",
              "explanation": "Differentiating numerator and denominator independently."
            },
            {
              "step": "Step 4: Exponentiate to Recover Limit of $y$",
              "math": "\\lim_{x \\to 0} y = e^{\\lim_{x \\to 0} \\ln y} = e^6",
              "explanation": "Since the natural exponential function is continuous, $\\lim e^{\\ln y} = e^{\\lim \\ln y}$."
            }
          ],
          "answer": "\\lim_{x \\to 0} (1 + 3x)^{2/x} = e^6"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "Application of Rolle's Theorem to Prove Uniqueness of Real Roots",
          "statement": "Prove that the polynomial equation $f(x) = 2x^5 + 5x^3 + 10x - 4 = 0$ has exactly one real root in $\\mathbb{R}$. (Use the IVT for existence, and Rolle's Theorem for uniqueness).",
          "steps": [
            {
              "step": "Step 1: Prove Existence via Intermediate Value Theorem",
              "math": "f(0) = -4 < 0, \\qquad f(1) = 2(1) + 5(1) + 10(1) - 4 = 13 > 0",
              "explanation": "Since $f$ is continuous on $[0, 1]$ and $f(0) f(1) < 0$, the IVT guarantees at least one root $c \\in (0, 1)$."
            },
            {
              "step": "Step 2: Compute Derivative and Analyze Sign",
              "math": "f'(x) = 10x^4 + 15x^2 + 10 = 5(2x^4 + 3x^2 + 2)",
              "explanation": "Notice that for all real $x \\in \\mathbb{R}$, $x^4 \\ge 0$ and $x^2 \\ge 0$. Thus $f'(x) \\ge 10 > 0$ strictly for every $x \\in \\mathbb{R}$."
            },
            {
              "step": "Step 3: Uniqueness Proof by Contradiction via Rolle's Theorem",
              "math": "\\text{Suppose } \\exists x_1 < x_2 \\text{ such that } f(x_1) = f(x_2) = 0",
              "explanation": "Since $f$ is a polynomial, it is continuous on $[x_1, x_2]$ and differentiable on $(x_1, x_2)$. By Rolle's Theorem, there must exist $c \\in (x_1, x_2)$ such that $f'(c) = 0$."
            },
            {
              "step": "Step 4: Conclude Contradiction",
              "math": "f'(c) = 10c^4 + 15c^2 + 10 \\ge 10 \\ne 0 \\implies \\text{Contradiction!}",
              "explanation": "Since $f'(x)$ is never zero, it is impossible for two distinct roots to exist. Therefore, exactly one real root exists in $\\mathbb{R}$."
            }
          ],
          "answer": "f(x) = 0 \\text{ has exactly one real root in } (0, 1) \\subset \\mathbb{R}"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "Cauchy MVT Proof of Classical Strict Inequality Bounds on sin x",
          "statement": "Use the Mean Value Theorem and Cauchy's MVT to prove rigorously that for all $x > 0$: $\\cos x > 1 - \\frac{x^2}{2}$ and $\\sin x > x - \\frac{x^3}{6}$.",
          "steps": [
            {
              "step": "Step 1: First MVT Application to $\\sin t$ on $[0, x]$",
              "math": "\\frac{\\sin x - \\sin 0}{x - 0} = \\cos(c_1) \\implies \\sin x = x \\cos(c_1) < x \\cdot 1 = x \\quad (0 < c_1 < x)",
              "explanation": "Since $\\cos(c_1) < 1$ for $c_1 \\in (0, x)$, we establish $\\sin x < x$ for all $x > 0$."
            },
            {
              "step": "Step 2: Second MVT Application to Auxiliary Function for Cosine",
              "math": "g(t) = \\cos t - \\left(1 - \\frac{t^2}{2}\\right) \\implies g'(t) = -\\sin t + t = t - \\sin t",
              "explanation": "From Step 1, $g'(t) = t - \\sin t > 0$ for all $t > 0$."
            },
            {
              "step": "Step 3: Deduce Cosine Inequality by Monotonicity",
              "math": "g(x) - g(0) = g'(c_2)(x - 0) > 0 \\implies \\cos x - \\left(1 - \\frac{x^2}{2}\\right) > 0 \\implies \\cos x > 1 - \\frac{x^2}{2}",
              "explanation": "Since $g(0) = 1 - 1 = 0$, $g(x) > 0$ strictly for all $x > 0$."
            },
            {
              "step": "Step 4: Third Application to Establish Sine Lower Bound",
              "math": "h(t) = \\sin t - \\left(t - \\frac{t^3}{6}\\right) \\implies h'(t) = \\cos t - \\left(1 - \\frac{t^2}{2}\\right) > 0",
              "explanation": "By Step 3, $h'(t) > 0$ for all $t > 0$. Since $h(0) = 0$, $h(x) > 0$ for all $x > 0$, proving $\\sin x > x - \\frac{x^3}{6} \\quad \\blacksquare$."
            }
          ],
          "answer": "\\cos x > 1 - \\frac{x^2}{2} \\quad \\text{and} \\quad \\sin x > x - \\frac{x^3}{6} \\quad \\forall x > 0 \\quad (\\text{Strict Taylor Bounds})"
        }
      ],
      "simulations": [
        "calc1-mvt-rolle-sim"
      ],
      "id": "unit7",
      "unitId": "unit7-calc1",
      "leadSummary": "The deep theoretical core of differential calculus: Rolle's theorem and proof via EVT and Fermat's theorem, Lagrange's Mean Value Theorem, zero-derivative constant function theorem, Cauchy generalized MVT, rigorous proof of L'Hopital's rule for 0/0 and infinity/infinity, resolution of exponential indeterminate forms, and linear differentials."
    },
    {
      "unitNumber": 8,
      "number": 8,
      "title": "Differential Curve Sketching, Extreme Values & Optimization",
      "description": "Comprehensive applications of derivatives: Fermat's interior extremum theorem, critical numbers, First and Second Derivative Tests, concavity and inflection points, universal 7-step analytical curve sketching algorithm, applied geometric and physical optimization problems, and the related rates framework.",
      "sections": [
        {
          "id": "u8-sec1",
          "title": "Critical Numbers, Fermat's Theorem on Stationary Points & Extrema",
          "content": "<h4>1. Local Extrema & Critical Numbers</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Definition (Critical Number): A number } c \\in \\operatorname{Dom}(f) \\text{ is a critical number of } f \\text{ if either:}}$$\n$$\\mathbf{f'(c) = 0 \\quad \\text{(stationary point)} \\quad \\text{or} \\quad f'(c) \\text{ is undefined (sharp corner, cusp, vertical tangent).}}$$\n</div>\n\n<h4>2. Fermat's Interior Extremum Theorem</h4>\n<div class=\"math-display\">\n$$\\mathbf{\\text{Theorem (Fermat): If } f \\text{ has a local extremum (maximum or minimum) at an interior point } c, \\text{ and } f'(c) \\text{ exists, then } f'(c) = 0.}$$\n</div>\n<p><em>Proof for Local Maximum:</em> Suppose $f$ has a local maximum at $c$. Then there exists $\\delta > 0$ such that $f(x) \\le f(c)$ for all $x \\in (c - \\delta, c + \\delta)$.</p>\n<ul>\n  <li>For $h \\in (0, \\delta)$ (approaching from right): $f(c + h) - f(c) \\le 0 \\implies \\frac{f(c + h) - f(c)}{h} \\le 0 \\implies f'_+(c) \\le 0$.</li>\n  <li>For $h \\in (-\\delta, 0)$ (approaching from left): $f(c + h) - f(c) \\le 0 \\implies \\frac{f(c + h) - f(c)}{h} \\ge 0 \\implies f'_-(c) \\ge 0$.</li>\n</ul>\n<p>Since $f$ is differentiable at $c$, $f'(c) = f'_+(c) = f'_-(c)$. The only real number satisfying both $f'(c) \\le 0$ and $f'(c) \\ge 0$ is $f'(c) = 0 \\quad \\blacksquare$</p>\n\n<h4>3. The Closed Interval Method for Absolute Extrema</h4>\n<p>To find the absolute maximum and minimum of a continuous function $f$ on a closed bounded interval $[a, b]$:</p>\n<ol>\n  <li>Find all critical numbers $c_i \\in (a, b)$.</li>\n  <li>Evaluate $f(c_i)$ at every critical number.</li>\n  <li>Evaluate $f(a)$ and $f(b)$ at the endpoints.</li>\n  <li>The greatest evaluated value is the absolute maximum; the least is the absolute minimum.</li>\n</ol>"
        },
        {
          "id": "u8-sec2",
          "title": "First & Second Derivative Tests, Concavity & Inflection Points",
          "content": "<h4>1. The First Derivative Test for Local Extrema</h4>\n<p>Let $c$ be a critical number of a continuous function $f$:</p>\n<ul>\n  <li>If $f'(x)$ changes from <strong>positive to negative</strong> as $x$ increases through $c$, then $f(c)$ is a <strong>local maximum</strong>.</li>\n  <li>If $f'(x)$ changes from <strong>negative to positive</strong> as $x$ increases through $c$, then $f(c)$ is a <strong>local minimum</strong>.</li>\n  <li>If $f'(x)$ does not change sign across $c$ (e.g. $+ \\to +$ or $- \\to -$), then $f(c)$ is neither a local maximum nor a local minimum (e.g. $f(x) = x^3$ at $c = 0$).</li>\n</ul>\n\n<h4>2. Concavity & Inflection Points</h4>\n<div class=\"math-display\">\n$$\\begin{aligned}\n\\mathbf{\\text{Concave Upward: }} & f''(x) > 0 \\quad \\forall x \\in I \\iff \\text{The tangent lines lie strictly below the curve} \\\n\\mathbf{\\text{Concave Downward: }} & f''(x) < 0 \\quad \\forall x \\in I \\iff \\text{The tangent lines lie strictly above the curve}\n\\end{aligned}$$\n</div>\n<p><strong>Point of Inflection:</strong> A point $(c, f(c))$ on the curve where the function is continuous and the concavity changes (from upward to downward, or vice versa). A necessary condition for an inflection point is $f''(c) = 0$ or $f''(c)$ undefined.</p>\n\n<h4>3. The Second Derivative Test for Local Extrema</h4>\n<p>Suppose $f''(x)$ is continuous near a stationary point $c$ with $f'(c) = 0$:</p>\n<ul>\n  <li>If $f''(c) > 0$, then the curve is concave upward at $c$, so $f(c)$ is a <strong>local minimum</strong>.</li>\n  <li>If $f''(c) < 0$, then the curve is concave downward at $c$, so $f(c)$ is a <strong>local maximum</strong>.</li>\n  <li>If $f''(c) = 0$, the test is <strong>inconclusive</strong> (e.g. $x^4$ has a minimum, $-x^4$ has a maximum, $x^3$ has an inflection point); one must revert to the First Derivative Test.</li>\n</ul>"
        },
        {
          "id": "u8-sec3",
          "title": "Systematic 7-Step Protocol for Mathematical Curve Sketching",
          "content": "<h4>The Universal 7-Step Curve Sketching Protocol</h4>\n<p>To sketch the graph of an arbitrary function $y = f(x)$ with analytical precision without guesswork:</p>\n<ol>\n  <li><strong>Step 1: Domain & Symmetries</strong> \u2014 Identify $\\operatorname{Dom}(f)$. Test for even symmetry $f(-x) = f(x)$, odd symmetry $f(-x) = -f(x)$, or periodicity $f(x+T) = f(x)$.</li>\n  <li><strong>Step 2: Intercepts</strong> \u2014 $y$-intercept at $(0, f(0))$. $x$-intercepts by solving $f(x) = 0$.</li>\n  <li><strong>Step 3: Asymptotes</strong> \u2014 Vertical asymptotes where $Q(x) = 0$ with $\\lim |f(x)| = \\infty$. Horizontal asymptotes $\\lim_{x \\to \\pm\\infty} f(x) = L$. Slant asymptotes $y = mx + b$ if $\\lim [f(x) - (mx+b)] = 0$.</li>\n  <li><strong>Step 4: First Derivative $f'(x)$</strong> \u2014 Critical numbers ($f'(x) = 0$ or undefined). Sign chart for $f'(x)$ to determine intervals of increase and decrease.</li>\n  <li><strong>Step 5: Local Extrema</strong> \u2014 Apply First or Second Derivative Test to classify each critical point.</li>\n  <li><strong>Step 6: Second Derivative $f''(x)$</strong> \u2014 Determine $f''(x) = 0$ or undefined. Sign chart for $f''(x)$ to determine intervals of concavity upward/downward and exact inflection points.</li>\n  <li><strong>Step 7: Global Assembly & Plot</strong> \u2014 Plot intercepts, asymptotes, extrema, and inflection points; sketch the smooth curve following the concavity and monotonicity signatures.</li>\n</ol>"
        },
        {
          "id": "u8-sec4",
          "title": "Applied Real-World Optimization & Related Rates Framework",
          "content": "<h4>1. Applied Mathematical Optimization Protocol</h4>\n<ol>\n  <li><strong>Variable Identification & Sketch:</strong> Assign variables to all quantities. Draw a diagram.</li>\n  <li><strong>Objective Function:</strong> Write an explicit formula for the quantity $Q$ to be maximized or minimized (e.g. volume, area, cost, material).</li>\n  <li><strong>Constraint Equations:</strong> Relate secondary variables via geometric or physical constraints (e.g. surface area budget, perimeter, Pythagorean theorem) to express $Q = f(x)$ purely in terms of a single independent variable.</li>\n  <li><strong>Domain Specification:</strong> Establish the feasible physical domain $x \\in [a, b]$ or $(a, b)$.</li>\n  <li><strong>Extremum Determination:</strong> Compute $f'(x) = 0$. Use the Closed Interval Method or Second Derivative Test to verify that the critical point is indeed the global optimum.</li>\n</ol>\n\n<h4>2. The Systematic Related Rates Protocol</h4>\n<p>When physical variables are related by an equation $F(x, y, z) = 0$ and change over time $t$:</p>\n<ol>\n  <li>Identify the given rates (e.g. $\\frac{dx}{dt}$) and the target rate (e.g. $\\frac{dy}{dt}$) at a specific instant $t_0$.</li>\n  <li>Formulate a geometric equation relating the static variables (never substitute numerical values that change with time before differentiating!).</li>\n  <li>Differentiate implicitly with respect to time $t$ using the Chain Rule: $\\frac{d}{dt}[y^2] = 2y \\frac{dy}{dt}$.</li>\n  <li>Substitute the instantaneous values and solve algebraically for the desired rate of change.</li>\n</ol>",
          "simulation": "calc1-curve-optimization-sim",
          "simulations": [
            "calc1-curve-optimization-sim"
          ]
        }
      ],
      "problems": [
        {
          "difficulty": "Easy",
          "difficultyLabel": "Tier 1: Foundational",
          "title": "Complete Critical Point and Inflection Point Determination",
          "statement": "For the polynomial function $f(x) = x^4 - 4x^3 + 10$: (a) Find all critical numbers. (b) Determine the intervals of increase and decrease. (c) Classify all local extrema. (d) Find all points of inflection and intervals of concavity.",
          "steps": [
            {
              "step": "Step 1: Compute First Derivative and Critical Numbers",
              "math": "f'(x) = 4x^3 - 12x^2 = 4x^2(x - 3) = 0 \\implies x = 0, \\quad x = 3",
              "explanation": "Critical numbers occur at $x = 0$ and $x = 3$."
            },
            {
              "step": "Step 2: Sign Analysis of $f'(x)$",
              "math": "\\begin{array}{c|c|c|c}
\\text{Interval} & (-\\infty, 0) & (0, 3) & (3, \\infty) \\\\ \\hline
4x^2 & + & + & + \\\\
x - 3 & - & - & + \\\\ \\hline
f'(x) & - & - & +
\\end{array}",
              "explanation": "$f$ is strictly decreasing on $(-\\infty, 3)$ and strictly increasing on $(3, \\infty)$. Notice $f'$ does NOT change sign across $x = 0$."
            },
            {
              "step": "Step 3: Classify Local Extrema",
              "math": "\\text{At } x = 3: \\quad f(3) = 3^4 - 4(3^3) + 10 = 81 - 108 + 10 = -17 \\quad (\\text{Local \\& Absolute Minimum})",
              "explanation": "At $x = 0$, $f'$ changes from negative to negative, so $(0, 10)$ is a stationary horizontal inflection point, NOT an extremum."
            },
            {
              "step": "Step 4: Second Derivative and Concavity",
              "math": "f''(x) = 12x^2 - 24x = 12x(x - 2) = 0 \\implies x = 0, \\quad x = 2",
              "explanation": "$f''(x) > 0$ on $(-\\infty, 0) \\cup (2, \\infty)$ (Concave Up). $f''(x) < 0$ on $(0, 2)$ (Concave Down). Inflection points at $(0, 10)$ and $(2, -6)$."
            }
          ],
          "answer": "\\text{Local/Abs Min at } (3, -17); \\quad \\text{Inflection Points at } (0, 10) \\text{ and } (2, -6); \\quad \\text{Concave Up on } (-\\infty, 0) \\cup (2, \\infty)"
        },
        {
          "difficulty": "Medium",
          "difficultyLabel": "Tier 2: Intermediate Exam",
          "title": "Applied Geometric Optimization: Maximum Volume Cylindrical Can",
          "statement": "A manufacturer wishes to design a closed cylindrical can of volume $V = 1000\\pi\\text{ cm}^3$ using the minimum possible surface area of metal. (a) Formulate the total surface area $A$ as a function of the radius $r$. (b) Determine the radius $r$ and height $h$ that minimize the surface area. (c) Prove that for any optimum cylinder, the height must equal the diameter ($h = 2r$).",
          "steps": [
            {
              "step": "Step 1: Constraint Equation and Objective Function",
              "math": "V = \\pi r^2 h = 1000\\pi \\implies h = \\frac{1000}{r^2}",
              "explanation": "Total surface area is two circular ends plus the cylindrical lateral mantle: $A(r) = 2\\pi r^2 + 2\\pi r h$."
            },
            {
              "step": "Step 2: Express Area as a Function of $r$",
              "math": "A(r) = 2\\pi r^2 + 2\\pi r \\left(\\frac{1000}{r^2}\\right) = 2\\pi r^2 + \\frac{2000\\pi}{r} \\quad (r > 0)",
              "explanation": "This expresses the objective function purely in terms of radius $r$."
            },
            {
              "step": "Step 3: Differentiate and Find Critical Radius",
              "math": "A'(r) = 4\\pi r - \\frac{2000\\pi}{r^2} = 0 \\implies 4\\pi r^3 = 2000\\pi \\implies r^3 = 500 \\implies r = \\sqrt[3]{500} = 5\\sqrt[3]{4}\\text{ cm}",
              "explanation": "Setting $A'(r) = 0$ gives the unique positive critical radius."
            },
            {
              "step": "Step 4: Verify Minimum via Second Derivative Test & Height Ratio",
              "math": "A''(r) = 4\\pi + \\frac{4000\\pi}{r^3} \\implies A''(\\sqrt[3]{500}) = 4\\pi + \\frac{4000\\pi}{500} = 4\\pi + 8\\pi = 12\\pi > 0",
              "explanation": "Since $A''(r) > 0$, the critical radius guarantees a strict global minimum. Computing $h$: $h = \\frac{V}{\\pi r^2} = \\frac{\\pi r^2 h}{\\pi r^2} \\implies h = \\frac{2000}{2r^2} = 2 \\left(\\frac{1000}{2r^2}\\right) = 2r$. Thus $h = 2r = 10\\sqrt[3]{4}\text{ cm}$."
            }
          ],
          "answer": "r = 5\\sqrt[3]{4} \\approx 7.94\\text{ cm}, \\qquad h = 10\\sqrt[3]{4} \\approx 15.87\\text{ cm}, \\qquad h = 2r \\text{ (Height equals Diameter)}"
        },
        {
          "difficulty": "Hard",
          "difficultyLabel": "Tier 3: Honors / Proof Challenge",
          "title": "Related Rates Analysis: Inverted Conical Tank Drainage & Surface Recession Speed",
          "statement": "An inverted conical water tank has a height of $H = 6.0\\text{ m}$ and a top radius of $R = 2.0\\text{ m}$. Water leaks out of a hole in the bottom vertex at a constant rate of $k = 0.50\\text{ m}^3/\\text{min}$. (a) Find a formula relating the water volume $V$ directly to the instantaneous water depth $h$. (b) Derive the rate at which the water depth is falling $\\frac{dh}{dt}$ as a function of depth $h$. (c) Compute $\\frac{dh}{dt}$ when the water is $h = 3.0\\text{ m}$ deep and when $h = 1.0\\text{ m}$ deep, explaining why the water level drops with accelerating speed as it empties.",
          "steps": [
            {
              "step": "Step 1: Relate Radius and Height by Similar Triangles",
              "math": "\\frac{r}{h} = \\frac{R}{H} = \\frac{2.0}{6.0} = \\frac{1}{3} \\implies r = \\frac{1}{3}h",
              "explanation": "Because the cone has straight cross-sectional walls, the water radius $r$ scales strictly proportionally with depth $h$."
            },
            {
              "step": "Step 2: Express Volume as a Function of Depth $h$",
              "math": "V = \\frac{1}{3}\\pi r^2 h = \\frac{1}{3}\\pi \\left(\\frac{1}{3}h\\right)^2 h = \\frac{\\pi}{27} h^3",
              "explanation": "Substituting $r = h/3$ yields $V(h)$ purely in terms of depth."
            },
            {
              "step": "Step 3: Differentiate with Respect to Time $t$",
              "math": "\\frac{dV}{dt} = \\frac{\\pi}{27} \\left(3 h^2 \\frac{dh}{dt}\\right) = \\frac{\\pi h^2}{9} \\frac{dh}{dt} \\implies \\frac{dh}{dt} = \\frac{9}{\\pi h^2} \\frac{dV}{dt}",
              "explanation": "Given that water is leaking out at $0.50\text{ m}^3/\text{min}$, we have $\\frac{dV}{dt} = -0.50 = -1/2\text{ m}^3/\text{min}$."
            },
            {
              "step": "Step 4: Compute Rates at Specified Depths",
              "math": "\\frac{dh}{dt} = -\\frac{9}{2\\pi h^2} \\\\ \\text{At } h = 3\\text{ m}: \\quad \\frac{dh}{dt} = -\\frac{9}{2\\pi(9)} = -\\frac{1}{2\\pi} \\approx -0.159\\text{ m/min} \\\\ \\text{At } h = 1\\text{ m}: \\quad \\frac{dh}{dt} = -\\frac{9}{2\\pi(1)} = -\\frac{9}{2\\pi} \\approx -1.432\\text{ m/min}",
              "explanation": "As the tank empties, the cross-sectional surface area $\\pi r^2 \\propto h^2$ shrinks quadratically. To sustain the constant volumetric drain rate, the water depth recession rate $\\left|\\frac{dh}{dt}\\right| \\propto 1/h^2$ increases inversely with the square of depth, accelerating as $h \to 0$."
            }
          ],
          "answer": "\\frac{dh}{dt} = -\\frac{9}{2\\pi h^2}; \\quad \\text{At } h = 3\\text{ m}: -\\frac{1}{2\\pi} \\approx -0.16\\text{ m/min}; \\quad \\text{At } h = 1\\text{ m}: -\\frac{9}{2\\pi} \\approx -1.43\\text{ m/min}"
        }
      ],
      "simulations": [
        "calc1-curve-optimization-sim"
      ],
      "id": "unit8",
      "unitId": "unit8-calc1",
      "leadSummary": "Comprehensive applications of derivatives: Fermat's interior extremum theorem, critical numbers, First and Second Derivative Tests, concavity and inflection points, universal 7-step analytical curve sketching algorithm, applied geometric and physical optimization problems, and the related rates framework."
    }
  ]
};
