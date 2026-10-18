import json

print("Building Calculus I: Units 3 & 4...")

# ==============================================================
# UNIT 3: THE THEORY OF LIMITS & RIGOROUS EPSILON-DELTA ANALYSIS
# ==============================================================
u3_sections = [
    {
        "id": "u3-sec1",
        "title": "The Intuitive Limit Concept, Numerical Behavior & One-Sided Limits",
        "content": r"""<h4>1. Intuitive Limit Concept</h4>
<p>In calculus, the limit is the foundational concept that enables the transition from static algebra to dynamical rates of change. Intuitively, we say that the limit of $f(x)$ as $x$ approaches $c$ is $L$:</p>
<div class="math-display">
$$\lim_{x \to c} f(x) = L$$
</div>
<p>if the values of $f(x)$ can be made arbitrarily close to $L$ by taking $x$ sufficiently close to $c$ (with $x \ne c$). Crucially, <strong>the value of $f(c)$ itself is completely irrelevant</strong> to the limit; $f(c)$ may equal $L$, may equal some other value, or may be completely undefined.</p>

<h4>2. One-Sided Limits</h4>
<p>Often, a function behaves differently depending on whether $x$ approaches $c$ from numbers strictly less than $c$ (from the left) or strictly greater than $c$ (from the right):</p>
<div class="math-display">
$$\begin{aligned}
\mathbf{\text{Left-Hand Limit: }} & \lim_{x \to c^-} f(x) = L_1 \quad (\text{as } x \to c \text{ with } x < c) \\
\mathbf{\text{Right-Hand Limit: }} & \lim_{x \to c^+} f(x) = L_2 \quad (\text{as } x \to c \text{ with } x > c)
\end{aligned}$$
</div>
<p><strong>Theorem (Two-Sided Limit Existence Criterion):</strong> The two-sided limit $\lim_{x \to c} f(x)$ exists and equals $L$ if and only if both one-sided limits exist and are strictly equal:</p>
<div class="math-display">
$$\lim_{x \to c} f(x) = L \iff \lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = L$$
</div>
<p>If $\lim_{x \to c^-} f(x) \ne \lim_{x \to c^+} f(x)$, the two-sided limit <em>does not exist (DNE)</em>.</p>"""
    },
    {
        "id": "u3-sec2",
        "title": "The Formal Cauchy-Weierstrass Epsilon-Delta Definition of Limit",
        "content": r"""<h4>1. The Formal Cauchy-Weierstrass Definition</h4>
<p>To eliminate ambiguity in phrases like "arbitrarily close" and "sufficiently close", Augustin-Louis Cauchy and Karl Weierstrass formulated the rigorous $\varepsilon$-$\delta$ definition:</p>
<div class="math-display">
$$\mathbf{\lim_{x \to c} f(x) = L \iff \forall \varepsilon > 0, \, \exists \delta > 0 \text{ such that } 0 < |x - c| < \delta \implies |f(x) - L| < \varepsilon}$$
</div>

<h4>2. Geometric Interpretation of the $\varepsilon$-$\delta$ Challenge</h4>
<p>The definition is a mathematical game between two players:</p>
<ol>
  <li>A challenger proposes a tolerance $\varepsilon > 0$, demanding that $f(x)$ lie in the horizontal target band $(L - \varepsilon, L + \varepsilon)$.</li>
  <li>You must respond by finding a neighborhood radius $\delta > 0$ such that for every $x$ within the punctured vertical interval $(c - \delta, c + \delta) \setminus \{c\}$, the graph $y = f(x)$ stays strictly inside the horizontal $\varepsilon$-tube.</li>
</ol>
<p>Notice that $\delta$ depends on both $\varepsilon$ and $c$: $\delta = \delta(\varepsilon, c)$.</p>

<h4>3. The Canonical $\varepsilon$-$\delta$ Proof Template</h4>
<p>A rigorous $\varepsilon$-$\delta$ proof always proceeds in two distinct phases:</p>
<ul>
  <li><strong>Scratchwork Analysis:</strong> Start with the target inequality $|f(x) - L| < \varepsilon$. Factor out $|x - c|$ to obtain $|x - c| \cdot |g(x)| < \varepsilon$. Choose a preliminary bound on $|x - c|$ (typically $\delta_1 \le 1$) to bound the auxiliary factor $|g(x)| \le M$. Then deduce $\delta = \min\{1, \varepsilon / M\}$.</li>
  <li><strong>Formal Deductive Proof:</strong> State "Let $\varepsilon > 0$ be given. Choose $\delta = \min\{1, \varepsilon / M\}$." Then, assuming $0 < |x - c| < \delta$, deduce sequentially that $|f(x) - L| < \varepsilon$ by direct algebraic inequalities.</li>
</ul>"""
    },
    {
        "id": "u3-sec3",
        "title": "Limit Arithmetic Laws & The Squeeze (Sandwich) Theorem",
        "content": r"""<h4>1. Limit Arithmetic Theorems</h4>
<p>Let $\lim_{x \to c} f(x) = L$ and $\lim_{x \to c} g(x) = M$. Then:</p>
<div class="math-display">
$$\begin{aligned}
\text{Sum / Difference: } & \lim_{x \to c} [f(x) \pm g(x)] = L \pm M \\
\text{Scalar Multiple: } & \lim_{x \to c} [k f(x)] = k L \quad (k \in \mathbb{R}) \\
\text{Product Law: } & \lim_{x \to c} [f(x) g(x)] = L \cdot M \\
\text{Quotient Law: } & \lim_{x \to c} \left[\frac{f(x)}{g(x)}\right] = \frac{L}{M} \quad (\text{provided } M \ne 0) \\
\text{Power / Root Law: } & \lim_{x \to c} [f(x)]^n = L^n, \quad \lim_{x \to c} \sqrt[n]{f(x)} = \sqrt[n]{L} \quad (L > 0 \text{ if } n \text{ is even})
\end{aligned}$$
</div>

<h4>2. The Squeeze (Sandwich) Theorem</h4>
<div class="math-display">
$$\mathbf{\text{Theorem: If } g(x) \le f(x) \le h(x) \text{ for all } x \text{ in an open interval containing } c \text{ (except possibly at } c\text{)}, \text{ and } \lim_{x \to c} g(x) = \lim_{x \to c} h(x) = L, \text{ then } \lim_{x \to c} f(x) = L.}$$
</div>

<h4>3. Rigorous Geometric Proof of the Fundamental Limit $\lim_{\theta \to 0} \frac{\sin\theta}{\theta} = 1$</h4>
<p>Consider a unit circle of radius $r = 1$. For an acute central angle $\theta \in (0, \pi/2)$ measured in radians:</p>
<ol>
  <li>Area of inner triangle with vertices $(0,0), (1,0), (\cos\theta, \sin\theta)$:
    <div class="math-display">
    $$A_{\text{inner}} = \frac{1}{2} (1) (\sin\theta) = \frac{1}{2} \sin\theta$$
    </div>
  </li>
  <li>Area of circular sector of angle $\theta$:
    <div class="math-display">
    $$A_{\text{sector}} = \frac{1}{2} r^2 \theta = \frac{1}{2} \theta$$
    </div>
  </li>
  <li>Area of outer tangent triangle with vertices $(0,0), (1,0), (1, \tan\theta)$:
    <div class="math-display">
    $$A_{\text{outer}} = \frac{1}{2} (1) (\tan\theta) = \frac{1}{2} \frac{\sin\theta}{\cos\theta}$$
    </div>
  </li>
</ol>
<p>By geometric containment, $A_{\text{inner}} < A_{\text{sector}} < A_{\text{outer}}$:</p>
<div class="math-display">
$$\frac{1}{2} \sin\theta < \frac{1}{2} \theta < \frac{1}{2} \frac{\sin\theta}{\cos\theta}$$
</div>
<p>Multiplying by $2 / \sin\theta$ (since $\sin\theta > 0$ on $(0, \pi/2)$):</p>
<div class="math-display">
$$1 < \frac{\theta}{\sin\theta} < \frac{1}{\cos\theta} \implies \cos\theta < \frac{\sin\theta}{\theta} < 1$$
</div>
<p>Taking the limit as $\theta \to 0^+$: since $\lim_{\theta \to 0^+} \cos\theta = 1$, the Squeeze Theorem forces $\lim_{\theta \to 0^+} \frac{\sin\theta}{\theta} = 1$. By even symmetry $\frac{\sin(-\theta)}{-\theta} = \frac{\sin\theta}{\theta}$, the two-sided limit is established: $\lim_{\theta \to 0} \frac{\sin\theta}{\theta} = 1 \quad \blacksquare$</p>"""
    },
    {
        "id": "u3-sec4",
        "title": "Limits at Infinity, Infinite Limits & Asymptotic Analysis",
        "content": r"""<h4>1. Limits at Infinity & Horizontal Asymptotes</h4>
<div class="math-display">
$$\mathbf{\lim_{x \to \infty} f(x) = L \iff \forall \varepsilon > 0, \, \exists N > 0 \text{ such that } x > N \implies |f(x) - L| < \varepsilon}$$
</div>
<p>If $\lim_{x \to \infty} f(x) = L$ or $\lim_{x \to -\infty} f(x) = L$, the horizontal line $y = L$ is a <strong>horizontal asymptote</strong> of the graph $y = f(x)$.</p>

<h4>2. Fundamental Rational Limit Theorem</h4>
<p>For any rational power $r > 0$:</p>
<div class="math-display">
$$\lim_{x \to \infty} \frac{1}{x^r} = 0, \qquad \lim_{x \to -\infty} \frac{1}{x^r} = 0 \quad (\text{for } x^r \text{ defined for negative } x)$$
</div>

<h4>3. Infinite Limits & Vertical Asymptotes</h4>
<div class="math-display">
$$\mathbf{\lim_{x \to c} f(x) = \infty \iff \forall M > 0, \, \exists \delta > 0 \text{ such that } 0 < |x - c| < \delta \implies f(x) > M}$$
</div>
<p>If $f(x) \to \pm\infty$ as $x \to c^+$ or $x \to c^-$, the line $x = c$ is a <strong>vertical asymptote</strong>.</p>"""
    }
]

u3_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Direct Algebraic Limit Evaluation with Indeterminate 0/0 Conjugation",
        "statement": r"Evaluate the exact analytical limit: $\lim_{x \to 0} \frac{\sqrt{x^2 + 9} - 3}{x^2}$. Show all factorization and rationalization steps.",
        "steps": [
            {
                "step": "Step 1: Check Direct Substitution",
                "math": r"\frac{\sqrt{0^2 + 9} - 3}{0^2} = \frac{3 - 3}{0} = \left[\frac{0}{0}\right]",
                "explanation": "Direct substitution yields the indeterminate form $0/0$, necessitating algebraic transformation."
            },
            {
                "step": "Step 2: Multiply by Radical Conjugate",
                "math": r"\frac{\sqrt{x^2 + 9} - 3}{x^2} \cdot \frac{\sqrt{x^2 + 9} + 3}{\sqrt{x^2 + 9} + 3} = \frac{(x^2 + 9) - 9}{x^2 (\sqrt{x^2 + 9} + 3)} = \frac{x^2}{x^2 (\sqrt{x^2 + 9} + 3)}",
                "explanation": "Expanding the difference of squares in the numerator eliminates the radical."
            },
            {
                "step": "Step 3: Cancel Common Zero Factor and Evaluate",
                "math": r"\lim_{x \to 0} \frac{1}{\sqrt{x^2 + 9} + 3} = \frac{1}{\sqrt{0 + 9} + 3} = \frac{1}{3 + 3} = \frac{1}{6}",
                "explanation": "Since $x \ne 0$ in the punctured limit neighborhood, we cancel $x^2$ and evaluate by direct substitution."
            }
        ],
        "answer": r"\lim_{x \to 0} \frac{\sqrt{x^2 + 9} - 3}{x^2} = \frac{1}{6}"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Rigorous Cauchy Epsilon-Delta Proof for a Quadratic Function",
        "statement": r"Use the formal $\varepsilon$-$\delta$ definition of a limit to prove rigorously that $\lim_{x \to 3} (2x^2 - 5x + 1) = 4$.",
        "steps": [
            {
                "step": "Step 1: Scratchwork Analysis",
                "math": r"|(2x^2 - 5x + 1) - 4| = |2x^2 - 5x - 3| = |(2x + 1)(x - 3)| = |2x + 1| \cdot |x - 3| < \varepsilon",
                "explanation": "We factored out the critical deviation factor $|x - 3|$. We must now bound the auxiliary factor $|2x + 1|$."
            },
            {
                "step": "Step 2: Establish a Preliminary Bound on |x - 3|",
                "math": r"\text{Assume } |x - 3| < 1 \implies -1 < x - 3 < 1 \implies 2 < x < 4",
                "explanation": "Bounding $x$ on $(2, 4)$ allows us to bound $2x + 1$:"
            },
            {
                "step": "Step 3: Bound the Auxiliary Term",
                "math": r"2 < x < 4 \implies 4 < 2x < 8 \implies 5 < 2x + 1 < 9 \implies |2x + 1| < 9",
                "explanation": "Thus, whenever $|x - 3| < 1$, we have $|2x + 1| \cdot |x - 3| < 9 |x - 3|$. To ensure this is $< \varepsilon$, we require $|x - 3| < \varepsilon / 9$."
            },
            {
                "step": "Step 4: Formal Proof",
                "math": r"\text{Let } \varepsilon > 0. \text{ Choose } \delta = \min\left(1, \frac{\varepsilon}{9}\right). \text{ If } 0 < |x - 3| < \delta, \text{ then } |(2x^2 - 5x + 1) - 4| < 9|x - 3| < 9\left(\frac{\varepsilon}{9}\right) = \varepsilon. \quad \blacksquare",
                "explanation": "This completes the formal deductive proof according to Cauchy's criterion."
            }
        ],
        "answer": r"\delta = \min\left(1, \frac{\varepsilon}{9}\right) \implies |(2x^2 - 5x + 1) - 4| < \varepsilon"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Trigonometric Squeeze Theorem Proof for an Oscillatory Radical Limit",
        "statement": r"Evaluate the limit $\lim_{x \to 0} \frac{x^3 \sin\left(\frac{1}{x}\right) + \tan(4x)}{\sin(2x) + x^2 \cos\left(\frac{1}{x^2}\right)}$ using rigorous limit theorems and the Squeeze Theorem. Prove every step without L'Hôpital's Rule.",
        "steps": [
            {
                "step": "Step 1: Divide Numerator and Denominator by $x$",
                "math": r"\frac{x^3 \sin(1/x) + \tan(4x)}{\sin(2x) + x^2 \cos(1/x^2)} = \frac{x^2 \sin(1/x) + \frac{\tan(4x)}{x}}{\frac{\sin(2x)}{x} + x \cos(1/x^2)}",
                "explanation": "Dividing by $x \ne 0$ isolates the fundamental trigonometric limits and small oscillatory terms."
            },
            {
                "step": "Step 2: Evaluate the Squeezed Oscillatory Limits",
                "math": r"-1 \le \sin(1/x) \le 1 \implies -x^2 \le x^2 \sin(1/x) \le x^2 \implies \lim_{x \to 0} x^2 \sin(1/x) = 0",
                "explanation": "Similarly, $-|x| \le x \cos(1/x^2) \le |x| \implies \lim_{x \to 0} x \cos(1/x^2) = 0$ by the Squeeze Theorem."
            },
            {
                "step": "Step 3: Evaluate the Trigonometric Limits",
                "math": r"\lim_{x \to 0} \frac{\tan(4x)}{x} = \lim_{x \to 0} 4 \left(\frac{\sin(4x)}{4x}\right) \frac{1}{\cos(4x)} = 4(1)(1) = 4, \qquad \lim_{x \to 0} \frac{\sin(2x)}{x} = 2(1) = 2",
                "explanation": "Using the fundamental theorem $\lim_{u \to 0} \frac{\sin u}{u} = 1$."
            },
            {
                "step": "Step 4: Combine via Quotient and Sum Limit Laws",
                "math": r"\lim_{x \to 0} \frac{x^2 \sin(1/x) + \frac{\tan(4x)}{x}}{\frac{\sin(2x)}{x} + x \cos(1/x^2)} = \frac{0 + 4}{2 + 0} = \frac{4}{2} = 2",
                "explanation": "Since the denominator limit $2 \ne 0$, the quotient limit law holds rigorously."
            }
        ],
        "answer": r"\lim_{x \to 0} \frac{x^3 \sin(1/x) + \tan(4x)}{\sin(2x) + x^2 \cos(1/x^2)} = 2"
    }
]

u3_data = {
    "unitNumber": 3,
    "number": 3,
    "title": "The Theory of Limits & Rigorous ε-δ Analysis",
    "description": "The mathematical foundation of single-variable analysis: intuitive limit mechanics, left and right one-sided limits, Cauchy-Weierstrass epsilon-delta definition and scratchwork methodology, limit arithmetic laws, Squeeze theorem, geometric proof of lim (sin theta)/theta = 1, limits at infinity, and infinite limits with asymptotes.",
    "sections": u3_sections,
    "problems": u3_problems
}

with open("calc1_u3.json", "w", encoding="utf-8") as f:
    json.dump(u3_data, f, indent=2)
print("calc1_u3.json created successfully!")

# ==========================================================
# UNIT 4: CONTINUITY & GLOBAL THEOREMS ON INTERVALS
# ==========================================================
u4_sections = [
    {
        "id": "u4-sec1",
        "title": "Continuity at a Point: The Three-Part Criterion & Epsilon-Delta Formulation",
        "content": r"""<h4>1. The Three-Part Definition of Continuity at a Point</h4>
<div class="math-display">
$$\mathbf{\text{Definition: A function } f \text{ is continuous at a point } c \in \operatorname{Dom}(f) \text{ if and only if:}}$$
$$\mathbf{1. } f(c) \text{ is defined } (c \in \operatorname{Dom}(f)), \quad \mathbf{2. } \lim_{x \to c} f(x) \text{ exists, and} \quad \mathbf{3. } \lim_{x \to c} f(x) = f(c)$$
</div>
<p>If any of these three conditions fails, $f$ is said to be <strong>discontinuous</strong> at $c$.</p>

<h4>2. The $\varepsilon$-$\delta$ Characterization of Continuity</h4>
<div class="math-display">
$$f \text{ is continuous at } c \iff \forall \varepsilon > 0, \, \exists \delta > 0 \text{ such that } |x - c| < \delta \implies |f(x) - f(c)| < \varepsilon$$
</div>
<p>Notice that unlike the limit definition where $x \ne c$ was required ($0 < |x - c|$), here if $x = c$, $|f(c) - f(c)| = 0 < \varepsilon$ holds trivially.</p>

<h4>3. Continuity on an Interval</h4>
<p>A function $f$ is continuous on an open interval $(a, b)$ if it is continuous at every $c \in (a, b)$. It is continuous on a closed interval $[a, b]$ if it is continuous on $(a, b)$, right-continuous at $a$ ($\lim_{x \to a^+} f(x) = f(a)$), and left-continuous at $b$ ($\lim_{x \to b^-} f(x) = f(b)$).</p>"""
    },
    {
        "id": "u4-sec2",
        "title": "Classification of Discontinuities: Removable, Jump & Essential",
        "content": r"""<h4>1. Removable Discontinuities (Holes)</h4>
<p>A point $c$ is a <strong>removable discontinuity</strong> of $f$ if $\lim_{x \to c} f(x) = L$ exists as a finite real number, but either $f(c)$ is undefined or $f(c) \ne L$.</p>
<p>The discontinuity can be "removed" by redefining $f(c) = L$. Typical example: $f(x) = \frac{x^2 - 1}{x - 1}$ at $c = 1$.</p>

<h4>2. Jump (First Kind) Discontinuities</h4>
<p>A point $c$ is a <strong>jump discontinuity</strong> if both one-sided limits exist as finite real numbers, but they are unequal:</p>
<div class="math-display">
$$\lim_{x \to c^-} f(x) = L_1 \ne \lim_{x \to c^+} f(x) = L_2$$
</div>
<p>The quantity $J = L_2 - L_1$ is called the <strong>jump</strong> of $f$ at $c$. Classic example: the signum function $\operatorname{sgn}(x)$ at $c = 0$, where $L_1 = -1, L_2 = +1, J = 2$.</p>

<h4>3. Essential (Second Kind) Discontinuities</h4>
<p>A discontinuity at $c$ is <strong>essential</strong> if at least one of the one-sided limits fails to exist (either diverging to $\pm\infty$ or oscillating indefinitely):</p>
<ul>
  <li><strong>Infinite Discontinuity:</strong> $f(x) = 1/(x - 2)$ at $c = 2$.</li>
  <li><strong>Oscillatory Discontinuity:</strong> $f(x) = \sin(1/x)$ at $c = 0$. As $x \to 0$, $1/x \to \infty$, and the sine function oscillates between $-1$ and $+1$ infinitely often, so neither one-sided limit exists.</li>
</ul>"""
    },
    {
        "id": "u4-sec3",
        "title": "Algebra of Continuous Functions & Continuity of Compositions",
        "content": r"""<h4>1. Algebraic Combinations</h4>
<p><strong>Theorem:</strong> If $f$ and $g$ are continuous at $c$, then for any scalar $k \in \mathbb{R}$:</p>
<div class="math-display">
$$f + g, \quad f - g, \quad k f, \quad f \cdot g \quad \text{are continuous at } c$$
$$\text{and } \frac{f}{g} \text{ is continuous at } c \text{ provided } g(c) \ne 0$$
</div>

<h4>2. Continuity of Composite Functions</h4>
<div class="math-display">
$$\mathbf{\text{Theorem: If } g \text{ is continuous at } c \text{ and } f \text{ is continuous at } g(c), \text{ then the composite function } (f \circ g) \text{ is continuous at } c.}$$
</div>
<p><em>Proof:</em> Let $\varepsilon > 0$. Since $f$ is continuous at $u_0 = g(c)$, $\exists \eta > 0$ such that $|u - u_0| < \eta \implies |f(u) - f(u_0)| < \varepsilon$. Since $g$ is continuous at $c$, for this $\eta > 0$, $\exists \delta > 0$ such that $|x - c| < \delta \implies |g(x) - g(c)| < \eta$. Substituting $u = g(x)$ establishes $|f(g(x)) - f(g(c))| < \varepsilon \quad \blacksquare$</p>

<h4>3. Continuity of Elementary Functions</h4>
<p>All polynomials, rational functions, power functions, trigonometric functions, inverse trigonometric functions, exponential functions, logarithmic functions, and hyperbolic functions are continuous on their entire natural domains.</p>"""
    },
    {
        "id": "u4-sec4",
        "title": "The Intermediate Value Theorem (IVT) & Root-Finding Algorithms",
        "content": r"""<h4>1. The Intermediate Value Theorem (Bolzano-Cauchy)</h4>
<div class="math-display">
$$\mathbf{\text{Theorem (IVT): Let } f: [a, b] \to \mathbb{R} \text{ be continuous on the closed bounded interval } [a, b]. \text{ If } u \text{ is any real number strictly between } f(a) \text{ and } f(b), \text{ then there exists at least one } c \in (a, b) \text{ such that } f(c) = u.}$$
</div>
<p>Geometrically, the graph of a continuous function on $[a, b]$ has no breaks or jumps, so it must cross any horizontal line $y = u$ lying between the endpoint values $y = f(a)$ and $y = f(b)$.</p>

<h4>2. Bolzano's Theorem (Existence of Roots)</h4>
<p><strong>Corollary:</strong> If $f \in C[a, b]$ and $f(a) \cdot f(b) < 0$ (opposite signs at endpoints), then there exists at least one root $c \in (a, b)$ such that $f(c) = 0$.</p>

<h4>3. The Bisection Algorithm</h4>
<p>Bolzano's theorem provides a constructive numerical method to compute roots to arbitrary precision:</p>
<ol>
  <li>Set interval $[a_0, b_0]$ with $f(a_0) f(b_0) < 0$.</li>
  <li>Evaluate midpoint $m_k = \frac{a_k + b_k}{2}$. If $f(m_k) = 0$, $m_k$ is the exact root.</li>
  <li>If $f(a_k) f(m_k) < 0$, set $[a_{k+1}, b_{k+1}] = [a_k, m_k]$; otherwise set $[a_{k+1}, b_{k+1}] = [m_k, b_k]$.</li>
  <li>After $n$ iterations, the error is bounded by $|c - m_n| \le \frac{b_0 - a_0}{2^{n+1}}$.</li>
</ol>"""
    },
    {
        "id": "u4-sec5",
        "title": "The Extreme Value Theorem (EVT) & Compactness on Closed Intervals",
        "content": r"""<h4>1. The Extreme Value Theorem (Weierstrass)</h4>
<div class="math-display">
$$\mathbf{\text{Theorem (EVT): If a function } f: [a, b] \to \mathbb{R} \text{ is continuous on a closed, bounded interval } [a, b], \text{ then } f \text{ attains both an absolute maximum and an absolute minimum on } [a, b].}$$
$$\exists x_{\min}, x_{\max} \in [a, b] \quad \text{such that} \quad f(x_{\min}) \le f(x) \le f(x_{\max}) \quad \forall x \in [a, b]$$
</div>

<h4>2. Necessity of the Hypotheses</h4>
<p>Both hypotheses—<strong>continuity</strong> and a <strong>closed bounded interval</strong>—are strictly necessary:</p>
<ul>
  <li><strong>Failure on Open Interval:</strong> $f(x) = x$ on $(0, 1)$ is continuous, but attains neither a minimum (infimum is $0 \notin (0, 1)$) nor a maximum (supremum is $1 \notin (0, 1)$).</li>
  <li><strong>Failure on Unbounded Domain:</strong> $f(x) = x^2$ on $[0, \infty)$ is continuous, but attains no maximum as $x \to \infty$.</li>
  <li><strong>Failure if Discontinuous:</strong> $f(x) = \begin{cases} 1/x, & x \in (0, 1] \\ 0, & x = 0 \end{cases}$ on $[0, 1]$ is defined on a closed bounded interval, but discontinuous at $x = 0$, having no maximum.</li>
</ul>"""
    }
]

u4_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Piecewise Function Parameter Determination for Global Continuity",
        "statement": r"Find the unique values of constants $a, b \in \mathbb{R}$ that make the piecewise function $f(x)$ continuous everywhere on $\mathbb{R}$:" + "\n" + r"$$f(x) = \begin{cases} \frac{x^2 - 4}{x - 2}, & x < 2 \\ a x^2 - b x + 3, & 2 \le x < 3 \\ 2x - a + b, & x \ge 3 \end{cases}$$",
        "steps": [
            {
                "step": "Step 1: Enforce Continuity at the Boundary $x = 2$",
                "math": r"\lim_{x \to 2^-} f(x) = \lim_{x \to 2^-} \frac{(x-2)(x+2)}{x-2} = 2 + 2 = 4, \qquad f(2) = a(2^2) - b(2) + 3 = 4a - 2b + 3",
                "explanation": "For continuity at $x = 2$, the left limit must equal the value at $x = 2$: $4a - 2b + 3 = 4 \implies 4a - 2b = 1$ (Equation 1)."
            },
            {
                "step": "Step 2: Enforce Continuity at the Boundary $x = 3$",
                "math": r"\lim_{x \to 3^-} f(x) = 9a - 3b + 3, \qquad \lim_{x \to 3^+} f(x) = 2(3) - a + b = 6 - a + b",
                "explanation": "Equating the two limits at $x = 3$: $9a - 3b + 3 = 6 - a + b \implies 10a - 4b = 3$ (Equation 2)."
            },
            {
                "step": "Step 3: Solve the Linear System",
                "math": r"\begin{cases} 4a - 2b = 1 \\ 10a - 4b = 3 \end{cases} \implies 2(4a - 2b) = 8a - 4b = 2",
                "explanation": "Subtracting this from Equation 2: $(10a - 4b) - (8a - 4b) = 3 - 2 \implies 2a = 1 \implies a = 1/2$. Substituting into Equation 1: $4(1/2) - 2b = 1 \implies 2 - 2b = 1 \implies 2b = 1 \implies b = 1/2$."
            }
        ],
        "answer": r"a = \frac{1}{2}, \qquad b = \frac{1}{2}"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Rigorous Proof of Root Existence via the Intermediate Value Theorem",
        "statement": r"Prove that the transcendental equation $e^x = 3 - 2x$ has at least one real root in the interval $(0, 1)$. Furthermore, explain how 4 iterations of the Bisection Method locate this root to an error of at most $1/32$.",
        "steps": [
            {
                "step": "Step 1: Construct Auxiliary Function and Verify Continuity",
                "math": r"g(x) = e^x + 2x - 3",
                "explanation": "The function $g(x)$ is continuous on $[0, 1]$ as the sum of the natural exponential $e^x$ and a linear polynomial $2x - 3$."
            },
            {
                "step": "Step 2: Evaluate Endpoints and Verify Sign Change",
                "math": r"g(0) = e^0 + 2(0) - 3 = 1 - 3 = -2 < 0, \qquad g(1) = e^1 + 2(1) - 3 = e - 1 \approx 2.718 - 1 = 1.718 > 0",
                "explanation": "Since $g(0) < 0$ and $g(1) > 0$, $0$ lies strictly between $g(0)$ and $g(1)$."
            },
            {
                "step": "Step 3: Apply the Intermediate Value Theorem",
                "math": r"\exists c \in (0, 1) \quad \text{such that} \quad g(c) = 0 \implies e^c + 2c - 3 = 0 \implies e^c = 3 - 2c \quad \blacksquare",
                "explanation": "By the IVT (Bolzano's theorem), there exists at least one solution $c \in (0, 1)$."
            },
            {
                "step": "Step 4: Error Bound of Bisection Method",
                "math": r"\text{Error}_n \le \frac{b_0 - a_0}{2^{n+1}} = \frac{1 - 0}{2^5} = \frac{1}{32} \approx 0.03125",
                "explanation": "After $n = 4$ bisections, the half-width of the enclosing sub-interval is $(1 - 0)/2^5 = 1/32$."
            }
        ],
        "answer": r"\exists c \in (0, 1) \text{ with } e^c = 3 - 2c; \quad \text{Bisection Error after 4 steps } \le \frac{1}{32}"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Topological Proof of Antipodal Temperature Equivalence (Borsuk-Ulam 1D)",
        "statement": r"Suppose the temperature $T(\theta)$ along the Earth's equator is a continuous function of the longitude angle $\theta \in [0, 2\pi]$ where $\theta = 0$ and $\theta = 2\pi$ represent the same point ($T(0) = T(2\pi)$). Prove rigorously using the Intermediate Value Theorem that there exists at least one pair of diametrically opposite (antipodal) points on the equator with exactly the same temperature: $T(c) = T(c + \pi)$ for some $c \in [0, \pi]$.",
        "steps": [
            {
                "step": "Step 1: Construct the Antipodal Difference Function",
                "math": r"f(\theta) = T(\theta) - T(\theta + \pi) \quad \text{for } \theta \in [0, \pi]",
                "explanation": "Since $T$ is continuous, $f(\theta)$ is continuous on the closed interval $[0, \pi]$."
            },
            {
                "step": "Step 2: Evaluate $f(\theta)$ at the Endpoints $\theta = 0$ and $\theta = \pi$",
                "math": r"f(0) = T(0) - T(\pi), \qquad f(\pi) = T(\pi) - T(2\pi) = T(\pi) - T(0)",
                "explanation": "Since $T(2\pi) = T(0)$, we have $f(\pi) = -(T(0) - T(\pi)) = -f(0)$."
            },
            {
                "step": "Step 3: Analyze Signs and Apply IVT",
                "math": r"\text{Case 1: If } f(0) = 0 \implies T(0) = T(\pi), \text{ then } c = 0 \text{ is the desired point.}",
                "explanation": "Case 2: If $f(0) \ne 0$, then $f(0)$ and $f(\pi) = -f(0)$ have strictly opposite signs ($f(0) f(\pi) < 0$)."
            },
            {
                "step": "Step 4: Conclude via Bolzano's Theorem",
                "math": r"\exists c \in (0, \pi) \quad \text{such that} \quad f(c) = 0 \implies T(c) - T(c + \pi) = 0 \implies T(c) = T(c + \pi) \quad \blacksquare",
                "explanation": "The Intermediate Value Theorem guarantees the existence of a point $c$ with zero difference, completing the proof of the 1D Borsuk-Ulam theorem."
            }
        ],
        "answer": r"\exists c \in [0, \pi] \text{ such that } T(c) = T(c + \pi) \quad (\text{Antipodal Temperature Equivalence})"
    }
]

u4_data = {
    "unitNumber": 4,
    "number": 4,
    "title": "Continuity & Global Theorems on Intervals",
    "description": "Rigorous continuity theory in real analysis: three-part definition of continuity at a point, epsilon-delta formulation, classification of removable, jump, and essential discontinuities, algebra of continuous functions, Intermediate Value Theorem (IVT) with bisection root-finding, Extreme Value Theorem (EVT), and topological antipodal proofs.",
    "sections": u4_sections,
    "problems": u4_problems
}

with open("calc1_u4.json", "w", encoding="utf-8") as f:
    json.dump(u4_data, f, indent=2)
print("calc1_u4.json created successfully!")
