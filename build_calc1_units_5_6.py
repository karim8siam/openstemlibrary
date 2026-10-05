import json

print("Building Calculus I: Units 5 & 6...")

# ==============================================================================
# UNIT 5: THE DERIVATIVE: FOUNDATIONS, DIFFERENCE QUOTIENTS & DIFFERENTIATION RULES
# ==============================================================================
u5_sections = [
    {
        "id": "u5-sec1",
        "title": "The Tangent Line Problem, Instantaneous Rates & Difference Quotients",
        "content": r"""<h4>1. The Tangent Line as a Limiting Secant Line</h4>
<p>Let $P(x_0, f(x_0))$ be a fixed point on the curve $y = f(x)$. Let $Q(x_0 + h, f(x_0 + h))$ be a neighboring point with $h \ne 0$. The slope of the secant line passing through $P$ and $Q$ is given by the <strong>Newton-Leibniz difference quotient</strong>:</p>
<div class="math-display">
$$m_{\text{sec}} = \frac{\Delta y}{\Delta x} = \frac{f(x_0 + h) - f(x_0)}{h}$$
</div>
<p>As $h \to 0$, point $Q$ slides along the curve toward $P$. If the secant slopes approach a unique finite limiting value, that limit is defined as the <strong>slope of the tangent line</strong> to the curve at $P$:</p>
<div class="math-display">
$$m_{\text{tan}} = f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$$
</div>

<h4>2. Equations of Tangent and Normal Lines</h4>
<ul>
  <li><strong>Tangent Line:</strong> Passing through $(x_0, y_0)$ with slope $m = f'(x_0)$:
    <div class="math-display">
    $$y - f(x_0) = f'(x_0)(x - x_0)$$
    </div>
  </li>
  <li><strong>Normal Line:</strong> The line perpendicular to the tangent line at $(x_0, y_0)$ (provided $f'(x_0) \ne 0$, having slope $m_{\perp} = -1/f'(x_0)$):
    <div class="math-display">
    $$y - f(x_0) = -\frac{1}{f'(x_0)}(x - x_0)$$
    </div>
  </li>
</ul>"""
    },
    {
        "id": "u5-sec2",
        "title": "One-Sided Derivatives & Differentiability Implying Continuity",
        "content": r"""<h4>1. One-Sided Derivatives</h4>
<div class="math-display">
$$\begin{aligned}
\mathbf{\text{Right-Hand Derivative: }} & f'_+(x_0) = \lim_{h \to 0^+} \frac{f(x_0 + h) - f(x_0)}{h} \\
\mathbf{\text{Left-Hand Derivative: }} & f'_-(x_0) = \lim_{h \to 0^-} \frac{f(x_0 + h) - f(x_0)}{h}
\end{aligned}$$
</div>
<p>A function is differentiable at $x_0$ if and only if both one-sided derivatives exist as finite numbers and are equal: $f'(x_0) = f'_+(x_0) = f'_-(x_0)$.</p>

<h4>2. Theorem: Differentiability Implies Continuity</h4>
<div class="math-display">
$$\mathbf{\text{Theorem: If } f \text{ is differentiable at } x_0, \text{ then } f \text{ is continuous at } x_0.}$$
</div>
<p><em>Proof:</em> To prove continuity, we must show that $\lim_{x \to x_0} [f(x) - f(x_0)] = 0$. For $x \ne x_0$, write:</p>
<div class="math-display">
$$f(x) - f(x_0) = \frac{f(x) - f(x_0)}{x - x_0} \cdot (x - x_0)$$
</div>
<p>Taking the limit as $x \to x_0$ using the product limit law:</p>
<div class="math-display">
$$\lim_{x \to x_0} [f(x) - f(x_0)] = \left( \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} \right) \cdot \left( \lim_{x \to x_0} (x - x_0) \right) = f'(x_0) \cdot 0 = 0$$
</div>
<p>Thus $\lim_{x \to x_0} f(x) = f(x_0)$, proving that $f$ is continuous at $x_0 \quad \blacksquare$</p>

<h4>3. The Converse is False: Geometric Non-Differentiability Modes</h4>
<p>Continuity is a strictly weaker condition than differentiability. Functions may fail to be differentiable at points where they are continuous due to:</p>
<ol>
  <li><strong>Corner Point (Cusp):</strong> Left and right derivatives differ ($f(x) = |x|$ at $x = 0$, where $f'_-(0) = -1 \ne f'_+(0) = +1$).</li>
  <li><strong>Vertical Tangent:</strong> The difference quotient diverges to $\pm\infty$ ($f(x) = x^{1/3}$ at $x = 0$, where $f'(0) = \lim_{h \to 0} h^{1/3}/h = \lim_{h \to 0} 1/h^{2/3} = \infty$).</li>
  <li><strong>Wild Oscillation:</strong> $f(x) = x \sin(1/x)$ for $x \ne 0$ and $f(0) = 0$ is continuous at $x = 0$, but its difference quotient $\sin(1/h)$ oscillates indefinitely between $-1$ and $+1$ as $h \to 0$.</li>
</ol>"""
    },
    {
        "id": "u5-sec3",
        "title": "Fundamental Algebraic Differentiation Rules & Rigorous Proofs",
        "content": r"""<h4>1. The Power Rule</h4>
<div class="math-display">
$$\mathbf{\frac{d}{dx}[x^n] = n x^{n-1} \quad \forall n \in \mathbb{R}}$$
</div>
<p><em>Proof for $n \in \mathbb{N}$ via Binomial Theorem:</em></p>
<div class="math-display">
$$\begin{aligned}
\frac{d}{dx}[x^n] &= \lim_{h \to 0} \frac{(x + h)^n - x^n}{h} = \lim_{h \to 0} \frac{\left( x^n + n x^{n-1} h + \binom{n}{2} x^{n-2} h^2 + \dots + h^n \right) - x^n}{h} \\
&= \lim_{h \to 0} \left( n x^{n-1} + \binom{n}{2} x^{n-2} h + \dots + h^{n-1} \right) = n x^{n-1} \quad \blacksquare
\end{aligned}$$
</div>

<h4>2. Linearity of the Derivative Operator</h4>
<div class="math-display">
$$\frac{d}{dx}[c f(x)] = c f'(x), \qquad \frac{d}{dx}[f(x) \pm g(x)] = f'(x) \pm g'(x)$$
</div>

<h4>3. The Product Rule & Line-by-Line Deductive Proof</h4>
<div class="math-display">
$$\mathbf{\frac{d}{dx}[f(x) g(x)] = f'(x) g(x) + f(x) g'(x)}$$
</div>
<p><em>Proof:</em> Form the difference quotient for the product $P(x) = f(x) g(x)$:</p>
<div class="math-display">
$$\frac{P(x + h) - P(x)}{h} = \frac{f(x + h) g(x + h) - f(x) g(x)}{h}$$
</div>
<p>Add and subtract the strategic intermediate term $f(x) g(x + h)$ in the numerator:</p>
<div class="math-display">
$$\begin{aligned}
&= \frac{f(x + h) g(x + h) - f(x) g(x + h) + f(x) g(x + h) - f(x) g(x)}{h} \\
&= \left( \frac{f(x + h) - f(x)}{h} \right) g(x + h) + f(x) \left( \frac{g(x + h) - g(x)}{h} \right)
\end{aligned}$$
</div>
<p>Taking the limit as $h \to 0$: since $g$ is differentiable at $x$, it is continuous at $x$, so $\lim_{h \to 0} g(x + h) = g(x)$. Therefore:</p>
<div class="math-display">
$$\lim_{h \to 0} \frac{P(x + h) - P(x)}{h} = f'(x) g(x) + f(x) g'(x) \quad \blacksquare$$
</div>

<h4>4. The Quotient Rule</h4>
<div class="math-display">
$$\mathbf{\frac{d}{dx}\left[ \frac{f(x)}{g(x)} \right] = \frac{f'(x) g(x) - f(x) g'(x)}{[g(x)]^2} \quad (g(x) \ne 0)}$$
</div>"""
    },
    {
        "id": "u5-sec4",
        "title": "Derivatives of Trigonometric, Exponential & Hyperbolic Functions",
        "content": r"""<h4>1. Derivatives of Trigonometric Functions</h4>
<p>Using the angle addition identity $\sin(x + h) = \sin x \cos h + \cos x \sin h$:</p>
<div class="math-display">
$$\begin{aligned}
\frac{d}{dx}[\sin x] &= \lim_{h \to 0} \frac{\sin(x + h) - \sin x}{h} = \lim_{h \to 0} \frac{\sin x(\cos h - 1) + \cos x\sin h}{h} \\
&= \sin x \left( \lim_{h \to 0} \frac{\cos h - 1}{h} \right) + \cos x \left( \lim_{h \to 0} \frac{\sin h}{h} \right) = \sin x(0) + \cos x(1) = \cos x
\end{aligned}$$
</div>
<p>Similarly, using the Quotient Rule:</p>
<div class="math-display">
$$\frac{d}{dx}[\cos x] = -\sin x, \quad \frac{d}{dx}[\tan x] = \sec^2 x, \quad \frac{d}{dx}[\sec x] = \sec x \tan x, \quad \frac{d}{dx}[\cot x] = -\csc^2 x, \quad \frac{d}{dx}[\csc x] = -\csc x \cot x$$
</div>

<h4>2. Derivatives of Exponential & Logarithmic Functions</h4>
<div class="math-display">
$$\frac{d}{dx}[e^x] = \lim_{h \to 0} \frac{e^{x+h} - e^x}{h} = e^x \lim_{h \to 0} \frac{e^h - 1}{h} = e^x (1) = e^x$$
$$\frac{d}{dx}[a^x] = a^x \ln a, \qquad \frac{d}{dx}[\ln x] = \frac{1}{x} \quad (x > 0), \qquad \frac{d}{dx}[\log_a x] = \frac{1}{x \ln a}$$
</div>

<h4>3. Derivatives of Hyperbolic Functions</h4>
<div class="math-display">
$$\frac{d}{dx}[\sinh x] = \frac{d}{dx}\left[\frac{e^x - e^{-x}}{2}\right] = \frac{e^x + e^{-x}}{2} = \cosh x$$
$$\frac{d}{dx}[\cosh x] = \sinh x, \qquad \frac{d}{dx}[\tanh x] = \operatorname{sech}^2 x, \qquad \frac{d}{dx}[\operatorname{sech} x] = -\operatorname{sech} x \tanh x$$
</div>"""
    }
]

u5_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Derivatives via Product and Quotient Rules",
        "statement": r"Compute the exact derivative $f'(x)$ for: (a) $f(x) = (3x^2 - 5x + 2) e^x$, and (b) $g(x) = \frac{x^2 \sin x}{x + \cos x}$.",
        "steps": [
            {
                "step": "Step 1: Apply Product Rule to (a)",
                "math": r"f'(x) = \frac{d}{dx}[3x^2 - 5x + 2] e^x + (3x^2 - 5x + 2) \frac{d}{dx}[e^x] = (6x - 5) e^x + (3x^2 - 5x + 2) e^x",
                "explanation": "Differentiating term by term and factoring out $e^x$."
            },
            {
                "step": "Step 2: Simplify (a)",
                "math": r"f'(x) = (3x^2 + x - 3) e^x",
                "explanation": "Combining like algebraic polynomial coefficients."
            },
            {
                "step": "Step 3: Apply Quotient Rule to (b)",
                "math": r"g'(x) = \frac{\frac{d}{dx}[x^2 \sin x] (x + \cos x) - (x^2 \sin x) \frac{d}{dx}[x + \cos x]}{(x + \cos x)^2}",
                "explanation": "Compute numerator derivative: $\frac{d}{dx}[x^2 \sin x] = 2x \sin x + x^2 \cos x$. Compute denominator derivative: $\frac{d}{dx}[x + \cos x] = 1 - \sin x$."
            },
            {
                "step": "Step 4: Expand and Assemble (b)",
                "math": r"g'(x) = \frac{(2x \sin x + x^2 \cos x)(x + \cos x) - x^2 \sin x (1 - \sin x)}{(x + \cos x)^2}",
                "explanation": "This gives the exact derivative."
            }
        ],
        "answer": r"f'(x) = (3x^2 + x - 3) e^x, \qquad g'(x) = \frac{(2x \sin x + x^2 \cos x)(x + \cos x) - x^2 \sin x (1 - \sin x)}{(x + \cos x)^2}"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Tangent and Normal Line Equations to a Transcendental Curve",
        "statement": r"Find the exact Cartesian equations of the tangent line and the normal line to the curve $y = f(x) = x^2 \ln(x) - 3x$ at the point where $x = 1$.",
        "steps": [
            {
                "step": "Step 1: Compute Point Coordinates $(x_0, y_0)$",
                "math": r"y_0 = f(1) = 1^2 \ln(1) - 3(1) = 0 - 3 = -3",
                "explanation": "The point of tangency on the curve is $(1, -3)$."
            },
            {
                "step": "Step 2: Compute Derivative $f'(x)$",
                "math": r"f'(x) = \frac{d}{dx}[x^2 \ln x] - \frac{d}{dx}[3x] = \left( 2x \ln x + x^2 \cdot \frac{1}{x} \right) - 3 = 2x \ln x + x - 3",
                "explanation": "Applying the Product Rule to $x^2 \ln x$."
            },
            {
                "step": "Step 3: Evaluate Tangent Slope at $x = 1$",
                "math": r"m_{\text{tan}} = f'(1) = 2(1) \ln(1) + 1 - 3 = 0 + 1 - 3 = -2",
                "explanation": "The tangent slope is $m = -2$. The normal slope is $m_{\perp} = -1/(-2) = 1/2$."
            },
            {
                "step": "Step 4: Formulate Line Equations",
                "math": r"\text{Tangent: } y - (-3) = -2(x - 1) \implies y = -2x - 1 \\ \text{Normal: } y - (-3) = \frac{1}{2}(x - 1) \implies y = \frac{1}{2}x - \frac{7}{2}",
                "explanation": "Writing in slope-intercept form."
            }
        ],
        "answer": r"\text{Tangent Line: } y = -2x - 1, \qquad \text{Normal Line: } y = \frac{1}{2}x - \frac{7}{2}"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Differentiability vs Continuity Analysis of an Oscillatory Piecewise Function",
        "statement": r"Consider the function $f(x) = \begin{cases} x^2 \sin\left(\frac{1}{x}\right), & x \ne 0 \\ 0, & x = 0 \end{cases}$. (a) Prove using the limit definition that $f'(0)$ exists and find its value. (b) For $x \ne 0$, compute $f'(x)$. (c) Prove that $\lim_{x \to 0} f'(x)$ does NOT exist, and explain why this demonstrates that a derivative function need not be continuous.",
        "steps": [
            {
                "step": "Step 1: Evaluate $f'(0)$ from the Definition of Derivative",
                "math": r"f'(0) = \lim_{h \to 0} \frac{f(0 + h) - f(0)}{h} = \lim_{h \to 0} \frac{h^2 \sin(1/h) - 0}{h} = \lim_{h \to 0} h \sin\left(\frac{1}{h}\right)",
                "explanation": "We must evaluate this limit as $h \to 0$."
            },
            {
                "step": "Step 2: Apply the Squeeze Theorem to $f'(0)$",
                "math": r"-1 \le \sin(1/h) \le 1 \implies -|h| \le h \sin(1/h) \le |h| \implies \lim_{h \to 0} h \sin(1/h) = 0",
                "explanation": "Because $\lim_{h \to 0} (\pm|h|) = 0$, the Squeeze Theorem guarantees that $f'(0) = 0$ exists."
            },
            {
                "step": "Step 3: Compute $f'(x)$ for $x \ne 0$",
                "math": r"f'(x) = \frac{d}{dx}[x^2] \sin(1/x) + x^2 \frac{d}{dx}[\sin(1/x)] = 2x \sin\left(\frac{1}{x}\right) + x^2 \cos\left(\frac{1}{x}\right)\left(-\frac{1}{x^2}\right) = 2x \sin\left(\frac{1}{x}\right) - \cos\left(\frac{1}{x}\right)",
                "explanation": "Applying product and chain rules for $x \ne 0$."
            },
            {
                "step": "Step 4: Prove Non-Existence of $\lim_{x \to 0} f'(x)$",
                "math": r"\lim_{x \to 0} f'(x) = \lim_{x \to 0} \left[ 2x \sin\left(\frac{1}{x}\right) - \cos\left(\frac{1}{x}\right) \right] = 0 - \lim_{x \to 0} \cos\left(\frac{1}{x}\right) \quad (\text{DNE})",
                "explanation": "As $x \to 0$, $2x \sin(1/x) \to 0$ by squeezing, but $\cos(1/x)$ oscillates between $-1$ and $+1$ infinitely often. Thus $\lim_{x \to 0} f'(x)$ does not exist. Since $\lim_{x \to 0} f'(x) \ne f'(0) = 0$, the derivative $f'(x)$ is discontinuous at $x = 0$, providing a classic counterexample."
            }
        ],
        "answer": r"f'(0) = 0 \text{ exists}; \quad f'(x) = 2x\sin(1/x) - \cos(1/x) \text{ for } x \ne 0; \quad \lim_{x \to 0} f'(x) \text{ DNE (discontinuous derivative)}"
    }
]

u5_data = {
    "unitNumber": 5,
    "number": 5,
    "title": "The Derivative: Foundations, Difference Quotients & Differentiation Rules",
    "description": "Rigorous theory of differentiation: secant-to-tangent limiting process, Newton difference quotient, one-sided derivatives, proof that differentiability implies continuity, failure modes (cusps, vertical tangents, wild oscillations), power rule, product rule proof, quotient rule, and derivatives of trigonometric, exponential, and hyperbolic functions.",
    "sections": u5_sections,
    "problems": u5_problems
}

with open("calc1_u5.json", "w", encoding="utf-8") as f:
    json.dump(u5_data, f, indent=2)
print("calc1_u5.json created successfully!")

# ==============================================================================
# UNIT 6: THE CHAIN RULE, INVERSE FUNCTIONS, HIGHER DERIVATIVES & LEIBNIZ RULE
# ==============================================================================
u6_sections = [
    {
        "id": "u6-sec1",
        "title": "The Chain Rule Theorem & Rigorous Carathéodory Formulation",
        "content": r"""<h4>1. Statement of the Chain Rule Theorem</h4>
<div class="math-display">
$$\mathbf{\text{Theorem: If } g \text{ is differentiable at } x_0 \text{ and } f \text{ is differentiable at } g(x_0), \text{ then the composite function } (f \circ g) \text{ is differentiable at } x_0 \text{ with:}}$$
$$\mathbf{(f \circ g)'(x_0) = f'(g(x_0)) \cdot g'(x_0) \quad \text{or in Leibniz notation: } \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}}$$
</div>

<h4>2. The Classic Proof Pitfall & Carathéodory's Resolution</h4>
<p>The naive attempt writes $\frac{\Delta y}{\Delta x} = \frac{\Delta y}{\Delta u} \cdot \frac{\Delta u}{\Delta x}$. This fails whenever $\Delta u = g(x_0 + h) - g(x_0) = 0$ for values of $h \ne 0$ (division by zero).</p>
<p><strong>Carathéodory's Theorem:</strong> A function $f$ is differentiable at $u_0$ if and only if there exists a function $\Phi(u)$ that is continuous at $u_0$ such that for all $u$:</p>
<div class="math-display">
$$f(u) - f(u_0) = \Phi(u)(u - u_0), \quad \text{with } \Phi(u_0) = f'(u_0)$$
</div>
<p><em>Rigorous Proof of Chain Rule:</em> Let $u = g(x)$ and $u_0 = g(x_0)$. By Carathéodory's characterization for $f$ at $u_0$:</p>
<div class="math-display">
$$f(g(x)) - f(g(x_0)) = \Phi(g(x)) [g(x) - g(x_0)]$$
</div>
<p>Dividing by $x - x_0$ for $x \ne x_0$:</p>
<div class="math-display">
$$\frac{f(g(x)) - f(g(x_0))}{x - x_0} = \Phi(g(x)) \cdot \frac{g(x) - g(x_0)}{x - x_0}$$
</div>
<p>As $x \to x_0$: because $g$ is differentiable at $x_0$, it is continuous at $x_0$, so $\lim_{x \to x_0} g(x) = g(x_0) = u_0$. Since $\Phi$ is continuous at $u_0$, $\lim_{x \to x_0} \Phi(g(x)) = \Phi(u_0) = f'(g(x_0))$. Thus:</p>
<div class="math-display">
$$(f \circ g)'(x_0) = f'(g(x_0)) \cdot g'(x_0) \quad \blacksquare$$
</div>"""
    },
    {
        "id": "u6-sec2",
        "title": "Implicit Differentiation & Geometry of Algebraic Plane Curves",
        "content": r"""<h4>1. Implicit Functions & The Method of Implicit Differentiation</h4>
<p>An equation of the form $F(x, y) = 0$ defines $y$ as an <strong>implicit function</strong> of $x$. Instead of solving explicitly for $y = f(x)$, we differentiate both sides of $F(x, y) = 0$ with respect to $x$, treating $y$ as an unknown differentiable function of $x$ and applying the Chain Rule $\frac{d}{dx}[g(y)] = g'(y) \frac{dy}{dx}$:</p>
<div class="math-display">
$$\frac{d}{dx}[F(x, y)] = 0 \implies \text{Solve algebraically for } \frac{dy}{dx}$$
</div>

<h4>2. Higher-Order Implicit Derivatives</h4>
<p>To find the second derivative $\frac{d^2y}{dx^2}$, differentiate the expression for $\frac{dy}{dx}$ with respect to $x$, applying the Quotient Rule, Product Rule, and Chain Rule, and then substitute the expression for $\frac{dy}{dx}$ to express $\frac{d^2y}{dx^2}$ purely in terms of $x$ and $y$.</p>"""
    },
    {
        "id": "u6-sec3",
        "title": "Derivatives of Inverse Functions & Inverse Transcendental Relations",
        "content": r"""<h4>1. Derivative of the Inverse Function Theorem</h4>
<div class="math-display">
$$\mathbf{\text{Theorem: If } f \text{ is strictly monotonic and differentiable at } x_0 \text{ with } f'(x_0) \ne 0, \text{ then } f^{-1} \text{ is differentiable at } y_0 = f(x_0) \text{ with:}}$$
$$(f^{-1})'(y_0) = \frac{1}{f'(x_0)} = \frac{1}{f'(f^{-1}(y_0))} \quad \text{or } \frac{dx}{dy} = \frac{1}{\frac{dy}{dx}}$$
</div>

<h4>2. Derivatives of Inverse Trigonometric Functions</h4>
<p>Let $y = \arcsin x$ for $x \in (-1, 1)$. Then $x = \sin y$ with $y \in (-\pi/2, \pi/2)$:</p>
<div class="math-display">
$$\frac{d}{dx}[x] = \frac{d}{dx}[\sin y] \implies 1 = \cos y \frac{dy}{dx} \implies \frac{dy}{dx} = \frac{1}{\cos y} = \frac{1}{\sqrt{1 - \sin^2 y}} = \frac{1}{\sqrt{1 - x^2}}$$
</div>
<p>Similarly:</p>
<div class="math-display">
$$\frac{d}{dx}[\arccos x] = -\frac{1}{\sqrt{1 - x^2}}, \qquad \frac{d}{dx}[\arctan x] = \frac{1}{1 + x^2}, \qquad \frac{d}{dx}[\operatorname{arcsec} x] = \frac{1}{|x|\sqrt{x^2 - 1}}$$
</div>

<h4>3. Derivatives of Inverse Hyperbolic Functions</h4>
<div class="math-display">
$$\frac{d}{dx}[\operatorname{arsinh} x] = \frac{1}{\sqrt{x^2 + 1}}, \qquad \frac{d}{dx}[\operatorname{arcosh} x] = \frac{1}{\sqrt{x^2 - 1}} \quad (x > 1), \qquad \frac{d}{dx}[\operatorname{artanh} x] = \frac{1}{1 - x^2} \quad (|x| < 1)$$
</div>"""
    },
    {
        "id": "u6-sec4",
        "title": "Logarithmic Differentiation & Successive Higher-Order Derivatives",
        "content": r"""<h4>1. Logarithmic Differentiation</h4>
<p>For functions involving complicated products, quotients, or variable powers $y = [u(x)]^{v(x)}$:</p>
<ol>
  <li>Take the natural logarithm of both sides: $\ln y = v(x) \ln u(x)$.</li>
  <li>Differentiate implicitly with respect to $x$: $\frac{1}{y} \frac{dy}{dx} = v'(x) \ln u(x) + v(x) \frac{u'(x)}{u(x)}$.</li>
  <li>Multiply through by $y$: $\frac{dy}{dx} = [u(x)]^{v(x)} \left[ v'(x) \ln u(x) + \frac{v(x) u'(x)}{u(x)} \right]$.</li>
</ol>

<h4>2. Successive Derivatives & Notations</h4>
<p>The $n$-th derivative $f^{(n)}(x) = \frac{d^n y}{dx^n}$ is obtained by iteratively differentiating $n$ times.</p>

<h4>3. The General Leibniz Rule for the $n$-th Derivative of a Product</h4>
<div class="math-display">
$$\mathbf{(f \cdot g)^{(n)}(x) = \sum_{k=0}^n \binom{n}{k} f^{(n-k)}(x) g^{(k)}(x)}$$
</div>
<p>where $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ are binomial coefficients. This theorem is proven rigorously by mathematical induction using Pascal's identity $\binom{n}{k-1} + \binom{n}{k} = \binom{n+1}{k}$.</p>"""
    }
]

u6_problems = [
    {
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Logarithmic Differentiation of Variable Exponent Towers",
        "statement": r"Find the exact derivative $\frac{dy}{dx}$ for: (a) $y = x^{\sin x}$ for $x > 0$, and (b) $y = \frac{(x^2 + 1)^3 \sqrt{2x + 5}}{(3x - 1)^4}$ at $x = 2$.",
        "steps": [
            {
                "step": "Step 1: Take Logarithm of (a)",
                "math": r"\ln y = \ln(x^{\sin x}) = \sin x \ln x",
                "explanation": "Convert exponent into product."
            },
            {
                "step": "Step 2: Differentiate Implicitly for (a)",
                "math": r"\frac{1}{y}\frac{dy}{dx} = \cos x \ln x + \sin x \left(\frac{1}{x}\right) \implies \frac{dy}{dx} = x^{\sin x} \left[ \cos x \ln x + \frac{\sin x}{x} \right]",
                "explanation": "Multiplying through by $y = x^{\sin x}$."
            },
            {
                "step": "Step 3: Logarithmic Differentiation for (b)",
                "math": r"\ln y = 3\ln(x^2 + 1) + \frac{1}{2}\ln(2x + 5) - 4\ln(3x - 1)",
                "explanation": "Expand product and quotient using log laws."
            },
            {
                "step": "Step 4: Differentiate and Evaluate at $x = 2$",
                "math": r"\frac{1}{y}\frac{dy}{dx} = 3\left(\frac{2x}{x^2+1}\right) + \frac{1}{2}\left(\frac{2}{2x+5}\right) - 4\left(\frac{3}{3x-1}\right) = 3\left(\frac{4}{5}\right) + \frac{1}{9} - 4\left(\frac{3}{5}\right) = \frac{12}{5} + \frac{1}{9} - \frac{12}{5} = \frac{1}{9}",
                "explanation": "At $x = 2$, $y = \frac{(5)^3 \sqrt{9}}{(5)^4} = \frac{125 \times 3}{625} = \frac{3}{5}$. Thus $\frac{dy}{dx} = \left(\frac{3}{5}\right)\left(\frac{1}{9}\right) = \frac{1}{15}$."
            }
        ],
        "answer": r"\text{(a) } \frac{dy}{dx} = x^{\sin x}\left[\cos x \ln x + \frac{\sin x}{x}\right], \qquad \text{(b) } \left.\frac{dy}{dx}\right|_{x=2} = \frac{1}{15}"
    },
    {
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Implicit Differentiation and Second Derivative of the Folium of Descartes",
        "statement": r"Consider the Folium of Descartes $x^3 + y^3 = 6xy$. (a) Find the derivative $\frac{dy}{dx}$ in terms of $x$ and $y$. (b) Find the equation of the tangent line at the symmetric point $(3, 3)$. (c) Compute the second derivative $\frac{d^2y}{dx^2}$ at $(3, 3)$.",
        "steps": [
            {
                "step": "Step 1: Differentiate Implicitly with Respect to $x$",
                "math": r"3x^2 + 3y^2 \frac{dy}{dx} = 6\left(y + x \frac{dy}{dx}\right) \implies x^2 + y^2 \frac{dy}{dx} = 2y + 2x \frac{dy}{dx}",
                "explanation": "Dividing by 3 and applying the product rule to $6xy$."
            },
            {
                "step": "Step 2: Solve for $\frac{dy}{dx}$",
                "math": r"\frac{dy}{dx}(y^2 - 2x) = 2y - x^2 \implies \frac{dy}{dx} = \frac{2y - x^2}{y^2 - 2x}",
                "explanation": "Isolating $\frac{dy}{dx}$."
            },
            {
                "step": "Step 3: Evaluate Tangent Line at $(3, 3)$",
                "math": r"\left.\frac{dy}{dx}\right|_{(3,3)} = \frac{2(3) - 3^2}{3^2 - 2(3)} = \frac{6 - 9}{9 - 6} = \frac{-3}{3} = -1 \implies y - 3 = -1(x - 3) \implies y = -x + 6",
                "explanation": "The tangent line at $(3, 3)$ has slope $m = -1$."
            },
            {
                "step": "Step 4: Compute Second Derivative $\frac{d^2y}{dx^2}$ at $(3,3)$",
                "math": r"\frac{d^2y}{dx^2} = \frac{(2y' - 2x)(y^2 - 2x) - (2y - x^2)(2yy' - 2)}{(y^2 - 2x)^2}",
                "explanation": "Substituting $x = 3, y = 3, y' = -1$: numerator is $[2(-1) - 6](9 - 6) - (6 - 9)[2(3)(-1) - 2] = [-8](3) - (-3)[-8] = -24 - 24 = -48$. Denominator is $(9 - 6)^2 = 9$. Thus $\frac{d^2y}{dx^2} = -\frac{48}{9} = -\frac{16}{3}$."
            }
        ],
        "answer": r"\frac{dy}{dx} = \frac{2y - x^2}{y^2 - 2x}, \quad \text{Tangent: } y = -x + 6, \quad \left.\frac{d^2y}{dx^2}\right|_{(3,3)} = -\frac{16}{3}"
    },
    {
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "General Leibniz Rule for Higher Derivatives & Mathematical Induction",
        "statement": r"(a) Prove the General Leibniz Rule $(fg)^{(n)} = \sum_{k=0}^n \binom{n}{k} f^{(n-k)} g^{(k)}$ by mathematical induction for all $n \in \mathbb{N}$. (b) Apply the Leibniz rule to compute the exact 10th derivative $y^{(10)}$ of $y = x^3 e^{2x}$.",
        "steps": [
            {
                "step": "Step 1: Base Case $n = 1$",
                "math": r"(fg)' = \binom{1}{0} f' g + \binom{1}{1} f g' = f' g + f g'",
                "explanation": "This matches the standard Product Rule, establishing the base case."
            },
            {
                "step": "Step 2: Inductive Step using Pascal's Identity",
                "math": r"(fg)^{(n+1)} = \frac{d}{dx}\left[ \sum_{k=0}^n \binom{n}{k} f^{(n-k)} g^{(k)} \right] = \sum_{k=0}^n \binom{n}{k} f^{(n+1-k)} g^{(k)} + \sum_{k=0}^n \binom{n}{k} f^{(n-k)} g^{(k+1)}",
                "explanation": "Re-indexing the second sum and combining via Pascal's identity $\binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k}$ yields $\sum_{k=0}^{n+1} \binom{n+1}{k} f^{(n+1-k)} g^{(k)} \quad \blacksquare$."
            },
            {
                "step": "Step 3: Apply to $y = x^3 e^{2x}$ with $n = 10$",
                "math": r"f(x) = e^{2x} \implies f^{(m)}(x) = 2^m e^{2x}; \qquad g(x) = x^3",
                "explanation": "Notice $g'(x) = 3x^2, g''(x) = 6x, g'''(x) = 6$, and $g^{(k)}(x) = 0$ for all $k \ge 4$. Thus only terms $k = 0, 1, 2, 3$ survive!"
            },
            {
                "step": "Step 4: Compute the Surviving 4 Terms",
                "math": r"""\begin{aligned}
y^{(10)} &= \binom{10}{0} 2^{10} e^{2x} (x^3) + \binom{10}{1} 2^9 e^{2x} (3x^2) + \binom{10}{2} 2^8 e^{2x} (6x) + \binom{10}{3} 2^7 e^{2x} (6) \\
&= e^{2x} 2^7 \left[ 2^3 x^3 + 10(2^2)(3x^2) + 45(2)(6x) + 120(6) \right] \\
&= 128 e^{2x} \left[ 8x^3 + 120x^2 + 540x + 720 \right] = 1024 e^{2x} \left[ x^3 + 15x^2 + \frac{135}{2}x + 90 \right]
\end{aligned}""",
                "explanation": "Factor out common powers of 2."
            }
        ],
        "answer": r"y^{(10)} = 1024 e^{2x} \left( x^3 + 15x^2 + \frac{135}{2}x + 90 \right) = 128 e^{2x} (8x^3 + 120x^2 + 540x + 720)"
    }
]

u5_data = {
    "unitNumber": 5,
    "number": 5,
    "title": "The Derivative: Foundations, Difference Quotients & Differentiation Rules",
    "description": "Rigorous theory of differentiation: secant-to-tangent limiting process, Newton difference quotient, one-sided derivatives, proof that differentiability implies continuity, failure modes (cusps, vertical tangents, wild oscillations), power rule, product rule proof, quotient rule, and derivatives of trigonometric, exponential, and hyperbolic functions.",
    "sections": u5_sections,
    "problems": u5_problems
}

u6_data = {
    "unitNumber": 6,
    "number": 6,
    "title": "The Chain Rule, Inverse Functions, Higher Derivatives & The Leibniz Rule",
    "description": "Advanced differential mechanics: Caratheodory formulation and proof of the Chain Rule, implicit differentiation of algebraic curves, derivatives of inverse functions, inverse trigonometric and inverse hyperbolic derivatives, logarithmic differentiation, and the General Leibniz Rule for the n-th derivative of a product with mathematical induction proof.",
    "sections": u6_sections,
    "problems": u6_problems
}

with open("calc1_u5.json", "w", encoding="utf-8") as f:
    json.dump(u5_data, f, indent=2)
print("calc1_u5.json created successfully!")

with open("calc1_u6.json", "w", encoding="utf-8") as f:
    json.dump(u6_data, f, indent=2)
print("calc1_u6.json created successfully!")

