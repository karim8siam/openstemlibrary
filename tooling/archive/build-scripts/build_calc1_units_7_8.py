import json

print("Building Calculus I: Units 7 & 8...")

# ==============================================================================
# UNIT 7: MEAN VALUE THEOREMS, TAYLOR APPROXIMATIONS & L'HOPITAL'S RULE
# ==============================================================================
u7_sections = [
    {
        "id": "u7-sec1",
        "title": "Rolle's Theorem & Lagrange's Mean Value Theorem (MVT)",
        "content": r"""<h4>1. Rolle's Theorem</h4>
<div class="math-display">
$$\mathbf{\text{Theorem (Rolle): Let } f: [a, b] \to \mathbb{R} \text{ satisfy:}}$$
$$\mathbf{1. } f \text{ is continuous on the closed interval } [a, b],$$
$$\mathbf{2. } f \text{ is differentiable on the open interval } (a, b), \text{ and}$$
$$\mathbf{3. } f(a) = f(b).$$
$$\mathbf{\text{Then there exists at least one number } c \in (a, b) \text{ such that } f'(c) = 0.}$$
</div>
<p><em>Rigorous Proof:</em> By the Extreme Value Theorem, continuous $f$ on $[a, b]$ attains an absolute maximum $M$ and minimum $m$.</p>
<ul>
  <li><strong>Case 1 (Constant Function):</strong> If $M = m$, then $f(x)$ is constant on $[a, b]$. Thus $f'(x) = 0$ for every $x \in (a, b)$, and any $c \in (a, b)$ satisfies the theorem.</li>
  <li><strong>Case 2 (Non-Constant Function):</strong> Since $f(a) = f(b)$, at least one of the extrema (say the maximum $M$) must be attained at an interior point $c \in (a, b)$. Since $f$ is differentiable at $c$ and attains a local maximum, Fermat's Interior Extremum Theorem forces $f'(c) = 0 \quad \blacksquare$</li>
</ul>

<h4>2. Lagrange's Mean Value Theorem (MVT)</h4>
<div class="math-display">
$$\mathbf{\text{Theorem (MVT): If } f \in C[a, b] \text{ and } f \in D(a, b), \text{ then there exists at least one } c \in (a, b) \text{ such that:}}$$
$$\mathbf{f'(c) = \frac{f(b) - f(a)}{b - a} \quad \iff \quad f(b) - f(a) = f'(c)(b - a)}$$
</div>
<p><em>Geometric Meaning:</em> There exists an interior point $c$ where the instantaneous rate of change (tangent slope) is strictly parallel to the average rate of change (secant slope connecting endpoints $(a, f(a))$ and $(b, f(b))$).</p>
<p><em>Proof via Rolle's Theorem:</em> Construct the auxiliary function measuring the vertical distance between the curve and the secant line:</p>
<div class="math-display">
$$h(x) = f(x) - f(a) - \left[\frac{f(b) - f(a)}{b - a}\right](x - a)$$
</div>
<p>Notice $h(a) = 0$ and $h(b) = 0$. Since $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, $h(x)$ satisfies all hypotheses of Rolle's Theorem on $[a, b]$. Thus $\exists c \in (a, b)$ with $h'(c) = 0$:</p>
<div class="math-display">
$$h'(c) = f'(c) - \frac{f(b) - f(a)}{b - a} = 0 \implies f'(c) = \frac{f(b) - f(a)}{b - a} \quad \blacksquare$$
</div>"""
    },
    {
        "id": "u7-sec2",
        "title": "Fundamental Corollaries of the MVT & Monotonicity Criteria",
        "content": r"""<h4>1. The Zero-Derivative Constant Function Theorem</h4>
<div class="math-display">
$$\mathbf{\text{Corollary 1: If } f'(x) = 0 \text{ for all } x \in (a, b), \text{ then } f(x) \text{ is constant on } (a, b).}$$
</div>
<p><em>Proof:</em> Choose any two points $x_1 < x_2$ in $(a, b)$. By the MVT on $[x_1, x_2]$, $\exists c \in (x_1, x_2)$ such that $f(x_2) - f(x_1) = f'(c)(x_2 - x_1) = 0 \cdot (x_2 - x_1) = 0$. Thus $f(x_1) = f(x_2)$ for all pairs, proving $f(x) \equiv C \quad \blacksquare$</p>

<h4>2. Functions Differing by a Constant</h4>
<div class="math-display">
$$\mathbf{\text{Corollary 2: If } f'(x) = g'(x) \text{ for all } x \in (a, b), \text{ then } f(x) = g(x) + C \text{ for some constant } C \in \mathbb{R}.}$$
</div>
<p>This is the fundamental justification for the $+ C$ constant of integration in antiderivatives.</p>

<h4>3. Monotonicity Test Criteria</h4>
<div class="math-display">
$$\begin{aligned}
f'(x) > 0 \quad \forall x \in (a, b) &\implies f \text{ is strictly increasing on } [a, b] \\
f'(x) < 0 \quad \forall x \in (a, b) &\implies f \text{ is strictly decreasing on } [a, b]
\end{aligned}$$
</div>"""
    },
    {
        "id": "u7-sec3",
        "title": "Cauchy's Generalized Mean Value Theorem & Rigorous L'Hôpital's Rule",
        "content": r"""<h4>1. Cauchy's Generalized Mean Value Theorem</h4>
<div class="math-display">
$$\mathbf{\text{Theorem: If } f, g \in C[a, b] \text{ and } f, g \in D(a, b) \text{ with } g'(x) \ne 0 \text{ on } (a, b), \text{ then there exists } c \in (a, b) \text{ such that:}}$$
$$\mathbf{\frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}}$$
</div>
<p><em>Proof:</em> By Rolle's Theorem on $g(x)$, $g(b) \ne g(a)$ (otherwise $g'(c) = 0$). Construct $H(x) = [f(b) - f(a)]g(x) - [g(b) - g(a)]f(x)$. Since $H(a) = H(b) = f(b)g(a) - g(b)f(a)$, Rolle's theorem yields $H'(c) = 0 \implies [f(b)-f(a)]g'(c) = [g(b)-g(a)]f'(c) \quad \blacksquare$</p>

<h4>2. L'Hôpital's Rule for Indeterminate Forms 0/0 and $\infty/\infty$</h4>
<div class="math-display">
$$\mathbf{\text{Theorem: Suppose } \lim_{x \to c} f(x) = 0 \text{ and } \lim_{x \to c} g(x) = 0 \text{ (or both } \pm\infty\text{)}. \text{ If } \lim_{x \to c} \frac{f'(x)}{g'(x)} = L \text{ exists (or is } \pm\infty\text{)}, \text{ then:}}$$
$$\mathbf{\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x \to c} \frac{f'(x)}{g'(x)} = L}$$
</div>
<p><em>Proof for $0/0$:</em> Define $f(c) = g(c) = 0$ to make $f, g$ continuous at $c$. For any $x$ near $c$, by Cauchy's MVT on $[c, x]$ (or $[x, c]$), there exists $x_1$ strictly between $c$ and $x$ such that:</p>
<div class="math-display">
$$\frac{f(x)}{g(x)} = \frac{f(x) - f(c)}{g(x) - g(c)} = \frac{f'(x_1)}{g'(x_1)}$$
</div>
<p>As $x \to c$, $x_1 \to c$ by squeezing. Thus $\lim_{x \to c} \frac{f(x)}{g(x)} = \lim_{x_1 \to c} \frac{f'(x_1)}{g'(x_1)} = L \quad \blacksquare$</p>

<h4>3. Resolution of Other Indeterminate Forms</h4>
<ul>
  <li><strong>Product $0 \cdot \infty$:</strong> Rewrite $f \cdot g = \frac{f}{1/g}$ or $\frac{g}{1/f}$ to convert to $\frac{0}{0}$ or $\frac{\infty}{\infty}$.</li>
  <li><strong>Difference $\infty - \infty$:</strong> Find a common algebraic denominator or rationalize.</li>
  <li><strong>Exponential Forms $0^0, 1^\infty, \infty^0$:</strong> Let $y = [f(x)]^{g(x)}$, take logarithms $\ln y = g(x) \ln f(x)$ (which becomes $0 \cdot \infty$), evaluate limit $L$, and recover $\lim y = e^L$.</li>
</ul>"""
    },
    {
        "id": "u7-sec4",
        "title": "Linear Approximations, Differentials & Error Propagation",
        "content": r"""<h4>1. Linear (Tangent Line) Approximation</h4>
<p>The tangent line to $y = f(x)$ at $x = x_0$ provides the optimal first-order linear approximation $L(x) \approx f(x)$ for values of $x$ close to $x_0$:</p>
<div class="math-display">
$$L(x) = f(x_0) + f'(x_0)(x - x_0)$$
</div>

<h4>2. Differentials</h4>
<p>Let $y = f(x)$. If $dx = \Delta x$ represents an independent change in the input, the <strong>differential</strong> $dy$ represents the corresponding change along the tangent line:</p>
<div class="math-display">
$$dy = f'(x) dx$$
</div>
<p>While the actual change along the curve is $\Delta y = f(x + \Delta x) - f(x)$, for small $dx$ we have $\Delta y \approx dy$.</p>

<h4>3. Error Estimation Metrics</h4>
<ul>
  <li><strong>Absolute Error:</strong> $\Delta y \approx dy = f'(x_0) dx$</li>
  <li><strong>Relative Error:</strong> $\frac{\Delta y}{y} \approx \frac{dy}{y} = \frac{f'(x_0) dx}{f(x_0)}$</li>
  <li><strong>Percentage Error:</strong> $\left( \frac{dy}{y} \right) \times 100\%$</li>
</ul>"""
    }
]

u7_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "L'Hôpital Evaluation of Exponential Indeterminate Form 1^∞",
        "statement": r"Evaluate the exact limit using L'Hôpital's Rule: $\lim_{x \to 0} (1 + 3x)^{2/x}$.",
        "steps": [
            {
                "step": "Step 1: Identify Indeterminate Form and Take Logarithm",
                "math": r"\text{As } x \to 0, \quad (1 + 3(0))^{2/0} = [1^\infty]. \quad \text{Let } y = (1 + 3x)^{2/x}",
                "explanation": "Taking natural log of both sides converts power to product:"
            },
            {
                "step": "Step 2: Transform into Fraction for L'Hôpital",
                "math": r"\ln y = \frac{2}{x} \ln(1 + 3x) = \frac{2\ln(1 + 3x)}{x}",
                "explanation": "As $x \to 0$, numerator is $2\ln(1) = 0$ and denominator is $0$, which is the indeterminate form $0/0$."
            },
            {
                "step": "Step 3: Apply L'Hôpital's Rule",
                "math": r"\lim_{x \to 0} \ln y = \lim_{x \to 0} \frac{\frac{d}{dx}[2\ln(1 + 3x)]}{\frac{d}{dx}[x]} = \lim_{x \to 0} \frac{2 \left(\frac{3}{1 + 3x}\right)}{1} = \frac{6}{1 + 0} = 6",
                "explanation": "Differentiating numerator and denominator independently."
            },
            {
                "step": "Step 4: Exponentiate to Recover Limit of $y$",
                "math": r"\lim_{x \to 0} y = e^{\lim_{x \to 0} \ln y} = e^6",
                "explanation": "Since the natural exponential function is continuous, $\lim e^{\ln y} = e^{\lim \ln y}$."
            }
        ],
        "answer": r"\lim_{x \to 0} (1 + 3x)^{2/x} = e^6"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Application of Rolle's Theorem to Prove Uniqueness of Real Roots",
        "statement": r"Prove that the polynomial equation $f(x) = 2x^5 + 5x^3 + 10x - 4 = 0$ has exactly one real root in $\mathbb{R}$. (Use the IVT for existence, and Rolle's Theorem for uniqueness).",
        "steps": [
            {
                "step": "Step 1: Prove Existence via Intermediate Value Theorem",
                "math": r"f(0) = -4 < 0, \qquad f(1) = 2(1) + 5(1) + 10(1) - 4 = 13 > 0",
                "explanation": "Since $f$ is continuous on $[0, 1]$ and $f(0) f(1) < 0$, the IVT guarantees at least one root $c \in (0, 1)$."
            },
            {
                "step": "Step 2: Compute Derivative and Analyze Sign",
                "math": r"f'(x) = 10x^4 + 15x^2 + 10 = 5(2x^4 + 3x^2 + 2)",
                "explanation": "Notice that for all real $x \in \mathbb{R}$, $x^4 \ge 0$ and $x^2 \ge 0$. Thus $f'(x) \ge 10 > 0$ strictly for every $x \in \mathbb{R}$."
            },
            {
                "step": "Step 3: Uniqueness Proof by Contradiction via Rolle's Theorem",
                "math": r"\text{Suppose } \exists x_1 < x_2 \text{ such that } f(x_1) = f(x_2) = 0",
                "explanation": "Since $f$ is a polynomial, it is continuous on $[x_1, x_2]$ and differentiable on $(x_1, x_2)$. By Rolle's Theorem, there must exist $c \in (x_1, x_2)$ such that $f'(c) = 0$."
            },
            {
                "step": "Step 4: Conclude Contradiction",
                "math": r"f'(c) = 10c^4 + 15c^2 + 10 \ge 10 \ne 0 \implies \text{Contradiction!}",
                "explanation": "Since $f'(x)$ is never zero, it is impossible for two distinct roots to exist. Therefore, exactly one real root exists in $\mathbb{R}$."
            }
        ],
        "answer": r"f(x) = 0 \text{ has exactly one real root in } (0, 1) \subset \mathbb{R}"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Cauchy MVT Proof of Classical Strict Inequality Bounds on sin x",
        "statement": r"Use the Mean Value Theorem and Cauchy's MVT to prove rigorously that for all $x > 0$: $\cos x > 1 - \frac{x^2}{2}$ and $\sin x > x - \frac{x^3}{6}$.",
        "steps": [
            {
                "step": "Step 1: First MVT Application to $\sin t$ on $[0, x]$",
                "math": r"\frac{\sin x - \sin 0}{x - 0} = \cos(c_1) \implies \sin x = x \cos(c_1) < x \cdot 1 = x \quad (0 < c_1 < x)",
                "explanation": "Since $\cos(c_1) < 1$ for $c_1 \in (0, x)$, we establish $\sin x < x$ for all $x > 0$."
            },
            {
                "step": "Step 2: Second MVT Application to Auxiliary Function for Cosine",
                "math": r"g(t) = \cos t - \left(1 - \frac{t^2}{2}\right) \implies g'(t) = -\sin t + t = t - \sin t",
                "explanation": "From Step 1, $g'(t) = t - \sin t > 0$ for all $t > 0$."
            },
            {
                "step": "Step 3: Deduce Cosine Inequality by Monotonicity",
                "math": r"g(x) - g(0) = g'(c_2)(x - 0) > 0 \implies \cos x - \left(1 - \frac{x^2}{2}\right) > 0 \implies \cos x > 1 - \frac{x^2}{2}",
                "explanation": "Since $g(0) = 1 - 1 = 0$, $g(x) > 0$ strictly for all $x > 0$."
            },
            {
                "step": "Step 4: Third Application to Establish Sine Lower Bound",
                "math": r"h(t) = \sin t - \left(t - \frac{t^3}{6}\right) \implies h'(t) = \cos t - \left(1 - \frac{t^2}{2}\right) > 0",
                "explanation": "By Step 3, $h'(t) > 0$ for all $t > 0$. Since $h(0) = 0$, $h(x) > 0$ for all $x > 0$, proving $\sin x > x - \frac{x^3}{6} \quad \blacksquare$."
            }
        ],
        "answer": r"\cos x > 1 - \frac{x^2}{2} \quad \text{and} \quad \sin x > x - \frac{x^3}{6} \quad \forall x > 0 \quad (\text{Strict Taylor Bounds})"
    }
]

u7_data = {
    "unitNumber": 7,
    "number": 7,
    "title": "Mean Value Theorems, Taylor Approximations & L'Hôpital's Rule",
    "description": "The deep theoretical core of differential calculus: Rolle's theorem and proof via EVT and Fermat's theorem, Lagrange's Mean Value Theorem, zero-derivative constant function theorem, Cauchy generalized MVT, rigorous proof of L'Hopital's rule for 0/0 and infinity/infinity, resolution of exponential indeterminate forms, and linear differentials.",
    "sections": u7_sections,
    "problems": u7_problems
}

with open("calc1_u7.json", "w", encoding="utf-8") as f:
    json.dump(u7_data, f, indent=2)
print("calc1_u7.json created successfully!")

# ==============================================================================
# UNIT 8: DIFFERENTIAL CURVE SKETCHING, EXTREME VALUES & OPTIMIZATION
# ==============================================================================
u8_sections = [
    {
        "id": "u8-sec1",
        "title": "Critical Numbers, Fermat's Theorem on Stationary Points & Extrema",
        "content": r"""<h4>1. Local Extrema & Critical Numbers</h4>
<div class="math-display">
$$\mathbf{\text{Definition (Critical Number): A number } c \in \operatorname{Dom}(f) \text{ is a critical number of } f \text{ if either:}}$$
$$\mathbf{f'(c) = 0 \quad \text{(stationary point)} \quad \text{or} \quad f'(c) \text{ is undefined (sharp corner, cusp, vertical tangent).}}$$
</div>

<h4>2. Fermat's Interior Extremum Theorem</h4>
<div class="math-display">
$$\mathbf{\text{Theorem (Fermat): If } f \text{ has a local extremum (maximum or minimum) at an interior point } c, \text{ and } f'(c) \text{ exists, then } f'(c) = 0.}$$
</div>
<p><em>Proof for Local Maximum:</em> Suppose $f$ has a local maximum at $c$. Then there exists $\delta > 0$ such that $f(x) \le f(c)$ for all $x \in (c - \delta, c + \delta)$.</p>
<ul>
  <li>For $h \in (0, \delta)$ (approaching from right): $f(c + h) - f(c) \le 0 \implies \frac{f(c + h) - f(c)}{h} \le 0 \implies f'_+(c) \le 0$.</li>
  <li>For $h \in (-\delta, 0)$ (approaching from left): $f(c + h) - f(c) \le 0 \implies \frac{f(c + h) - f(c)}{h} \ge 0 \implies f'_-(c) \ge 0$.</li>
</ul>
<p>Since $f$ is differentiable at $c$, $f'(c) = f'_+(c) = f'_-(c)$. The only real number satisfying both $f'(c) \le 0$ and $f'(c) \ge 0$ is $f'(c) = 0 \quad \blacksquare$</p>

<h4>3. The Closed Interval Method for Absolute Extrema</h4>
<p>To find the absolute maximum and minimum of a continuous function $f$ on a closed bounded interval $[a, b]$:</p>
<ol>
  <li>Find all critical numbers $c_i \in (a, b)$.</li>
  <li>Evaluate $f(c_i)$ at every critical number.</li>
  <li>Evaluate $f(a)$ and $f(b)$ at the endpoints.</li>
  <li>The greatest evaluated value is the absolute maximum; the least is the absolute minimum.</li>
</ol>"""
    },
    {
        "id": "u8-sec2",
        "title": "First & Second Derivative Tests, Concavity & Inflection Points",
        "content": r"""<h4>1. The First Derivative Test for Local Extrema</h4>
<p>Let $c$ be a critical number of a continuous function $f$:</p>
<ul>
  <li>If $f'(x)$ changes from <strong>positive to negative</strong> as $x$ increases through $c$, then $f(c)$ is a <strong>local maximum</strong>.</li>
  <li>If $f'(x)$ changes from <strong>negative to positive</strong> as $x$ increases through $c$, then $f(c)$ is a <strong>local minimum</strong>.</li>
  <li>If $f'(x)$ does not change sign across $c$ (e.g. $+ \to +$ or $- \to -$), then $f(c)$ is neither a local maximum nor a local minimum (e.g. $f(x) = x^3$ at $c = 0$).</li>
</ul>

<h4>2. Concavity & Inflection Points</h4>
<div class="math-display">
$$\begin{aligned}
\mathbf{\text{Concave Upward: }} & f''(x) > 0 \quad \forall x \in I \iff \text{The tangent lines lie strictly below the curve} \\
\mathbf{\text{Concave Downward: }} & f''(x) < 0 \quad \forall x \in I \iff \text{The tangent lines lie strictly above the curve}
\end{aligned}$$
</div>
<p><strong>Point of Inflection:</strong> A point $(c, f(c))$ on the curve where the function is continuous and the concavity changes (from upward to downward, or vice versa). A necessary condition for an inflection point is $f''(c) = 0$ or $f''(c)$ undefined.</p>

<h4>3. The Second Derivative Test for Local Extrema</h4>
<p>Suppose $f''(x)$ is continuous near a stationary point $c$ with $f'(c) = 0$:</p>
<ul>
  <li>If $f''(c) > 0$, then the curve is concave upward at $c$, so $f(c)$ is a <strong>local minimum</strong>.</li>
  <li>If $f''(c) < 0$, then the curve is concave downward at $c$, so $f(c)$ is a <strong>local maximum</strong>.</li>
  <li>If $f''(c) = 0$, the test is <strong>inconclusive</strong> (e.g. $x^4$ has a minimum, $-x^4$ has a maximum, $x^3$ has an inflection point); one must revert to the First Derivative Test.</li>
</ul>"""
    },
    {
        "id": "u8-sec3",
        "title": "Systematic 7-Step Protocol for Mathematical Curve Sketching",
        "content": r"""<h4>The Universal 7-Step Curve Sketching Protocol</h4>
<p>To sketch the graph of an arbitrary function $y = f(x)$ with analytical precision without guesswork:</p>
<ol>
  <li><strong>Step 1: Domain & Symmetries</strong> — Identify $\operatorname{Dom}(f)$. Test for even symmetry $f(-x) = f(x)$, odd symmetry $f(-x) = -f(x)$, or periodicity $f(x+T) = f(x)$.</li>
  <li><strong>Step 2: Intercepts</strong> — $y$-intercept at $(0, f(0))$. $x$-intercepts by solving $f(x) = 0$.</li>
  <li><strong>Step 3: Asymptotes</strong> — Vertical asymptotes where $Q(x) = 0$ with $\lim |f(x)| = \infty$. Horizontal asymptotes $\lim_{x \to \pm\infty} f(x) = L$. Slant asymptotes $y = mx + b$ if $\lim [f(x) - (mx+b)] = 0$.</li>
  <li><strong>Step 4: First Derivative $f'(x)$</strong> — Critical numbers ($f'(x) = 0$ or undefined). Sign chart for $f'(x)$ to determine intervals of increase and decrease.</li>
  <li><strong>Step 5: Local Extrema</strong> — Apply First or Second Derivative Test to classify each critical point.</li>
  <li><strong>Step 6: Second Derivative $f''(x)$</strong> — Determine $f''(x) = 0$ or undefined. Sign chart for $f''(x)$ to determine intervals of concavity upward/downward and exact inflection points.</li>
  <li><strong>Step 7: Global Assembly & Plot</strong> — Plot intercepts, asymptotes, extrema, and inflection points; sketch the smooth curve following the concavity and monotonicity signatures.</li>
</ol>"""
    },
    {
        "id": "u8-sec4",
        "title": "Applied Real-World Optimization & Related Rates Framework",
        "content": r"""<h4>1. Applied Mathematical Optimization Protocol</h4>
<ol>
  <li><strong>Variable Identification & Sketch:</strong> Assign variables to all quantities. Draw a diagram.</li>
  <li><strong>Objective Function:</strong> Write an explicit formula for the quantity $Q$ to be maximized or minimized (e.g. volume, area, cost, material).</li>
  <li><strong>Constraint Equations:</strong> Relate secondary variables via geometric or physical constraints (e.g. surface area budget, perimeter, Pythagorean theorem) to express $Q = f(x)$ purely in terms of a single independent variable.</li>
  <li><strong>Domain Specification:</strong> Establish the feasible physical domain $x \in [a, b]$ or $(a, b)$.</li>
  <li><strong>Extremum Determination:</strong> Compute $f'(x) = 0$. Use the Closed Interval Method or Second Derivative Test to verify that the critical point is indeed the global optimum.</li>
</ol>

<h4>2. The Systematic Related Rates Protocol</h4>
<p>When physical variables are related by an equation $F(x, y, z) = 0$ and change over time $t$:</p>
<ol>
  <li>Identify the given rates (e.g. $\frac{dx}{dt}$) and the target rate (e.g. $\frac{dy}{dt}$) at a specific instant $t_0$.</li>
  <li>Formulate a geometric equation relating the static variables (never substitute numerical values that change with time before differentiating!).</li>
  <li>Differentiate implicitly with respect to time $t$ using the Chain Rule: $\frac{d}{dt}[y^2] = 2y \frac{dy}{dt}$.</li>
  <li>Substitute the instantaneous values and solve algebraically for the desired rate of change.</li>
</ol>"""
    }
]

u8_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Complete Critical Point and Inflection Point Determination",
        "statement": r"For the polynomial function $f(x) = x^4 - 4x^3 + 10$: (a) Find all critical numbers. (b) Determine the intervals of increase and decrease. (c) Classify all local extrema. (d) Find all points of inflection and intervals of concavity.",
        "steps": [
            {
                "step": "Step 1: Compute First Derivative and Critical Numbers",
                "math": r"f'(x) = 4x^3 - 12x^2 = 4x^2(x - 3) = 0 \implies x = 0, \quad x = 3",
                "explanation": "Critical numbers occur at $x = 0$ and $x = 3$."
            },
            {
                "step": "Step 2: Sign Analysis of $f'(x)$",
                "math": r"""\begin{array}{c|c|c|c}
\text{Interval} & (-\infty, 0) & (0, 3) & (3, \infty) \\
\hline
4x^2 & + & + & + \\
x - 3 & - & - & + \\
\hline
f'(x) & - & - & +
\end{array}""",
                "explanation": "$f$ is strictly decreasing on $(-\infty, 3)$ and strictly increasing on $(3, \infty)$. Notice $f'$ does NOT change sign across $x = 0$."
            },
            {
                "step": "Step 3: Classify Local Extrema",
                "math": r"\text{At } x = 3: \quad f(3) = 3^4 - 4(3^3) + 10 = 81 - 108 + 10 = -17 \quad (\text{Local \& Absolute Minimum})",
                "explanation": "At $x = 0$, $f'$ changes from negative to negative, so $(0, 10)$ is a stationary horizontal inflection point, NOT an extremum."
            },
            {
                "step": "Step 4: Second Derivative and Concavity",
                "math": r"f''(x) = 12x^2 - 24x = 12x(x - 2) = 0 \implies x = 0, \quad x = 2",
                "explanation": "$f''(x) > 0$ on $(-\infty, 0) \cup (2, \infty)$ (Concave Up). $f''(x) < 0$ on $(0, 2)$ (Concave Down). Inflection points at $(0, 10)$ and $(2, -6)$."
            }
        ],
        "answer": r"\text{Local/Abs Min at } (3, -17); \quad \text{Inflection Points at } (0, 10) \text{ and } (2, -6); \quad \text{Concave Up on } (-\infty, 0) \cup (2, \infty)"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Applied Geometric Optimization: Maximum Volume Cylindrical Can",
        "statement": r"A manufacturer wishes to design a closed cylindrical can of volume $V = 1000\pi\text{ cm}^3$ using the minimum possible surface area of metal. (a) Formulate the total surface area $A$ as a function of the radius $r$. (b) Determine the radius $r$ and height $h$ that minimize the surface area. (c) Prove that for any optimum cylinder, the height must equal the diameter ($h = 2r$).",
        "steps": [
            {
                "step": "Step 1: Constraint Equation and Objective Function",
                "math": r"V = \pi r^2 h = 1000\pi \implies h = \frac{1000}{r^2}",
                "explanation": "Total surface area is two circular ends plus the cylindrical lateral mantle: $A(r) = 2\pi r^2 + 2\pi r h$."
            },
            {
                "step": "Step 2: Express Area as a Function of $r$",
                "math": r"A(r) = 2\pi r^2 + 2\pi r \left(\frac{1000}{r^2}\right) = 2\pi r^2 + \frac{2000\pi}{r} \quad (r > 0)",
                "explanation": "This expresses the objective function purely in terms of radius $r$."
            },
            {
                "step": "Step 3: Differentiate and Find Critical Radius",
                "math": r"A'(r) = 4\pi r - \frac{2000\pi}{r^2} = 0 \implies 4\pi r^3 = 2000\pi \implies r^3 = 500 \implies r = \sqrt[3]{500} = 5\sqrt[3]{4}\text{ cm}",
                "explanation": "Setting $A'(r) = 0$ gives the unique positive critical radius."
            },
            {
                "step": "Step 4: Verify Minimum via Second Derivative Test & Height Ratio",
                "math": r"A''(r) = 4\pi + \frac{4000\pi}{r^3} \implies A''(\sqrt[3]{500}) = 4\pi + \frac{4000\pi}{500} = 4\pi + 8\pi = 12\pi > 0",
                "explanation": "Since $A''(r) > 0$, the critical radius guarantees a strict global minimum. Computing $h$: $h = \frac{V}{\pi r^2} = \frac{\pi r^2 h}{\pi r^2} \implies h = \frac{2000}{2r^2} = 2 \left(\frac{1000}{2r^2}\right) = 2r$. Thus $h = 2r = 10\sqrt[3]{4}\text{ cm}$."
            }
        ],
        "answer": r"r = 5\sqrt[3]{4} \approx 7.94\text{ cm}, \qquad h = 10\sqrt[3]{4} \approx 15.87\text{ cm}, \qquad h = 2r \text{ (Height equals Diameter)}"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Related Rates Analysis: Inverted Conical Tank Drainage & Surface Recession Speed",
        "statement": r"An inverted conical water tank has a height of $H = 6.0\text{ m}$ and a top radius of $R = 2.0\text{ m}$. Water leaks out of a hole in the bottom vertex at a constant rate of $k = 0.50\text{ m}^3/\text{min}$. (a) Find a formula relating the water volume $V$ directly to the instantaneous water depth $h$. (b) Derive the rate at which the water depth is falling $\frac{dh}{dt}$ as a function of depth $h$. (c) Compute $\frac{dh}{dt}$ when the water is $h = 3.0\text{ m}$ deep and when $h = 1.0\text{ m}$ deep, explaining why the water level drops with accelerating speed as it empties.",
        "steps": [
            {
                "step": "Step 1: Relate Radius and Height by Similar Triangles",
                "math": r"\frac{r}{h} = \frac{R}{H} = \frac{2.0}{6.0} = \frac{1}{3} \implies r = \frac{1}{3}h",
                "explanation": "Because the cone has straight cross-sectional walls, the water radius $r$ scales strictly proportionally with depth $h$."
            },
            {
                "step": "Step 2: Express Volume as a Function of Depth $h$",
                "math": r"V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi \left(\frac{1}{3}h\right)^2 h = \frac{\pi}{27} h^3",
                "explanation": "Substituting $r = h/3$ yields $V(h)$ purely in terms of depth."
            },
            {
                "step": "Step 3: Differentiate with Respect to Time $t$",
                "math": r"\frac{dV}{dt} = \frac{\pi}{27} \left(3 h^2 \frac{dh}{dt}\right) = \frac{\pi h^2}{9} \frac{dh}{dt} \implies \frac{dh}{dt} = \frac{9}{\pi h^2} \frac{dV}{dt}",
                "explanation": "Given that water is leaking out at $0.50\text{ m}^3/\text{min}$, we have $\frac{dV}{dt} = -0.50 = -1/2\text{ m}^3/\text{min}$."
            },
            {
                "step": "Step 4: Compute Rates at Specified Depths",
                "math": r"\frac{dh}{dt} = -\frac{9}{2\pi h^2} \\ \text{At } h = 3\text{ m}: \quad \frac{dh}{dt} = -\frac{9}{2\pi(9)} = -\frac{1}{2\pi} \approx -0.159\text{ m/min} \\ \text{At } h = 1\text{ m}: \quad \frac{dh}{dt} = -\frac{9}{2\pi(1)} = -\frac{9}{2\pi} \approx -1.432\text{ m/min}",
                "explanation": "As the tank empties, the cross-sectional surface area $\pi r^2 \propto h^2$ shrinks quadratically. To sustain the constant volumetric drain rate, the water depth recession rate $\left|\frac{dh}{dt}\right| \propto 1/h^2$ increases inversely with the square of depth, accelerating as $h \to 0$."
            }
        ],
        "answer": r"\frac{dh}{dt} = -\frac{9}{2\pi h^2}; \quad \text{At } h = 3\text{ m}: -\frac{1}{2\pi} \approx -0.16\text{ m/min}; \quad \text{At } h = 1\text{ m}: -\frac{9}{2\pi} \approx -1.43\text{ m/min}"
    }
]

u8_data = {
    "unitNumber": 8,
    "number": 8,
    "title": "Differential Curve Sketching, Extreme Values & Optimization",
    "description": "Comprehensive applications of derivatives: Fermat's interior extremum theorem, critical numbers, First and Second Derivative Tests, concavity and inflection points, universal 7-step analytical curve sketching algorithm, applied geometric and physical optimization problems, and the related rates framework.",
    "sections": u8_sections,
    "problems": u8_problems
}

with open("calc1_u7.json", "w", encoding="utf-8") as f:
    json.dump(u7_data, f, indent=2)
print("calc1_u7.json created successfully!")

with open("calc1_u8.json", "w", encoding="utf-8") as f:
    json.dump(u8_data, f, indent=2)
print("calc1_u8.json created successfully!")

