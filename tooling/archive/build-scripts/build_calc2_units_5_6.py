import json

print("Building Calculus II: Units 5 & 6...")

# ==========================================
# UNIT 5: IMPROPER INTEGRALS & CONVERGENCE TESTS
# ==========================================
u5_sections = [
    {
        "id": "u5-sec1",
        "title": "Type I Improper Integrals: Infinite Intervals of Integration & The $p$-Test",
        "content": r"""<h4>1. Rigorous Definition of Type I Improper Integrals</h4>
<p>An integral is called a <strong>Type I improper integral</strong> if the interval of integration is unbounded. It is defined as the analytical limit of proper Riemann integrals over truncated compact intervals:</p>
<ul>
  <li><strong>Upper Infinite Limit:</strong> For $f$ continuous on $[a, \infty)$:
    $$\int_a^\infty f(x) \, dx = \lim_{M \to \infty} \int_a^M f(x) \, dx$$
  </li>
  <li><strong>Lower Infinite Limit:</strong> For $f$ continuous on $(-\infty, b]$:
    $$\int_{-\infty}^b f(x) \, dx = \lim_{N \to -\infty} \int_N^b f(x) \, dx$$
  </li>
  <li><strong>Doubly Infinite Domain:</strong> For $f$ continuous on $(-\infty, \infty)$ and any partitioning point $c \in \mathbb{R}$:
    $$\int_{-\infty}^\infty f(x) \, dx = \int_{-\infty}^c f(x) \, dx + \int_c^\infty f(x) \, dx = \lim_{N \to -\infty} \int_N^c f(x) \, dx + \lim_{M \to \infty} \int_c^M f(x) \, dx$$
    The doubly infinite integral <em>converges</em> if and only if <strong>both</strong> one-sided limits converge independently.
  </li>
</ul>

<h4>2. The Foundational $p$-Integral Convergence Test</h4>
<div class="math-display">
$$\mathbf{\int_1^\infty \frac{1}{x^p} \, dx \text{ converges if and only if } p > 1}$$
</div>
<p><strong>Proof:</strong> For $p \ne 1$:</p>
<div class="math-display">
$$\int_1^M x^{-p} \, dx = \left[ \frac{x^{1-p}}{1-p} \right]_1^M = \frac{M^{1-p} - 1}{1-p}$$
</div>
<p>As $M \to \infty$:</p>
<ul>
  <li>If $p > 1$, then $1 - p < 0 \implies \lim_{M \to \infty} M^{1-p} = 0$, so $\int_1^\infty x^{-p} \, dx = \frac{1}{p - 1}$ (Convergent).</li>
  <li>If $p < 1$, then $1 - p > 0 \implies \lim_{M \to \infty} M^{1-p} = \infty$ (Divergent).</li>
  <li>If $p = 1$, $\int_1^M \frac{1}{x} \, dx = \ln(M) \to \infty$ as $M \to \infty$ (Divergent). $\blacksquare$</li>
</ul>"""
    },
    {
        "id": "u5-sec2",
        "title": "Type II Improper Integrals: Discontinuous Integrands & Singularities",
        "content": r"""<h4>1. Unbounded Integrands on Bounded Intervals</h4>
<p>An integral $\int_a^b f(x) \, dx$ is called a <strong>Type II improper integral</strong> if the integrand $f(x)$ has an infinite singularity ($\lim |f(x)| = \infty$) at one or more points in $[a, b]$:</p>
<ul>
  <li><strong>Singularity at Upper Endpoint $b$:</strong>
    $$\int_a^b f(x) \, dx = \lim_{\varepsilon \to 0^+} \int_a^{b - \varepsilon} f(x) \, dx$$
  </li>
  <li><strong>Singularity at Lower Endpoint $a$:</strong>
    $$\int_a^b f(x) \, dx = \lim_{\varepsilon \to 0^+} \int_{a + \varepsilon}^b f(x) \, dx$$
  </li>
  <li><strong>Interior Singularity at $c \in (a, b)$:</strong>
    $$\int_a^b f(x) \, dx = \lim_{\varepsilon_1 \to 0^+} \int_a^{c - \varepsilon_1} f(x) \, dx + \lim_{\varepsilon_2 \to 0^+} \int_{c + \varepsilon_2}^b f(x) \, dx$$
    The integral converges if and only if both limits exist independently.
  </li>
</ul>

<h4>2. The Bounded Interval $p$-Singularity Test</h4>
<div class="math-display">
$$\mathbf{\int_0^1 \frac{1}{x^p} \, dx \text{ converges if and only if } p < 1}$$
</div>
<p>Notice the critical duality: for unbounded domains $[1, \infty)$, convergence requires $p > 1$; for singular origins $[0, 1]$, convergence requires $p < 1$. The reciprocal function $\int_0^\infty \frac{1}{x^p} dx$ diverges for <em>all</em> $p \in \mathbb{R}$.</p>"""
    },
    {
        "id": "u5-sec3",
        "title": "The Cauchy Principal Value (PV) & Symmetrical Cancellations",
        "content": r"""<h4>1. Definition of the Cauchy Principal Value</h4>
<p>When an improper integral diverges in the standard independent-limit sense, symmetric cancellation can produce a finite <strong>Cauchy Principal Value (P.V.)</strong>:</p>
<ul>
  <li><strong>For Type I Integrals:</strong>
    $$\operatorname{P.V.} \int_{-\infty}^\infty f(x) \, dx = \lim_{R \to \infty} \int_{-R}^R f(x) \, dx$$
  </li>
  <li><strong>For Type II Integrals with Interior Singularity at $c$:</strong>
    $$\operatorname{P.V.} \int_a^b f(x) \, dx = \lim_{\varepsilon \to 0^+} \left( \int_a^{c - \varepsilon} f(x) \, dx + \int_{c + \varepsilon}^b f(x) \, dx \right)$$
  </li>
</ul>

<h4>2. Strict Distinction from Standard Convergence</h4>
<p>Consider $f(x) = x$ over $(-\infty, \infty)$:</p>
<div class="math-display">
$$\operatorname{P.V.} \int_{-\infty}^\infty x \, dx = \lim_{R \to \infty} \int_{-R}^R x \, dx = \lim_{R \to \infty} \left[ \frac{x^2}{2} \right]_{-R}^R = \lim_{R \to \infty} 0 = 0$$
</div>
<p>However, the integral $\int_{-\infty}^\infty x \, dx$ <strong>diverges</strong> under standard definition because $\lim_{M \to \infty} \int_0^M x dx = \infty$. If an integral converges normally, its Cauchy Principal Value exists and is identical; the converse is strictly false.</p>"""
    },
    {
        "id": "u5-sec4",
        "title": "Comparison Tests: Direct Comparison & Limit Comparison for Integrals",
        "content": r"""<h4>1. The Direct Comparison Test</h4>
<p>Let $f, g$ be continuous functions on $[a, \infty)$ satisfying $0 \le f(x) \le g(x)$ for all $x \ge a$:</p>
<ol>
  <li><strong>Convergence Inheritance:</strong> If $\int_a^\infty g(x) \, dx$ converges, then $\int_a^\infty f(x) \, dx$ converges, and $\int_a^\infty f(x)dx \le \int_a^\infty g(x)dx$.</li>
  <li><strong>Divergence Inheritance:</strong> If $\int_a^\infty f(x) \, dx$ diverges to $\infty$, then $\int_a^\infty g(x) \, dx$ diverges to $\infty$.</li>
</ol>

<h4>2. The Limit Comparison Test</h4>
<p>Let $f(x) \ge 0$ and $g(x) > 0$ for all $x \ge a$. Suppose the asymptotic limit exists:</p>
<div class="math-display">
$$L = \lim_{x \to \infty} \frac{f(x)}{g(x)}$$
</div>
<ul>
  <li>If $0 < L < \infty$, then $\int_a^\infty f(x) \, dx$ and $\int_a^\infty g(x) \, dx$ <strong>either both converge or both diverge</strong>.</li>
  <li>If $L = 0$ and $\int_a^\infty g(x) \, dx$ converges, then $\int_a^\infty f(x) \, dx$ converges.</li>
  <li>If $L = \infty$ and $\int_a^\infty g(x) \, dx$ diverges, then $\int_a^\infty f(x) \, dx$ diverges.</li>
</ul>

<h4>3. Absolute vs Conditional Convergence</h4>
<div class="math-display">
$$\mathbf{\text{Absolute Convergence: } \int_a^\infty |f(x)| \, dx < \infty \implies \int_a^\infty f(x) \, dx \text{ converges}}$$
</div>
<p>If $\int_a^\infty f(x) \, dx$ converges but $\int_a^\infty |f(x)| \, dx = \infty$, the integral is <strong>conditionally convergent</strong>.</p>"""
    },
    {
        "id": "u5-sec5",
        "title": "Dirichlet's & Abel's Tests: Oscillating Integrals & The Dirichlet Sinc Integral",
        "content": r"""<h4>1. Dirichlet's Test for Improper Integrals</h4>
<div class="math-display">
$$\mathbf{\text{Theorem (Dirichlet's Test): Let } f, g: [a, \infty) \to \mathbb{R} \text{ satisfy:}}$$
</div>
<ol>
  <li>The antiderivative of $f$ is uniformly bounded: $\exists M > 0$ such that $\left| \int_a^x f(t) \, dt \right| \le M$ for all $x \ge a$.</li>
  <li>$g(x)$ is monotonic and decays to zero: $g'(x) \le 0$ (or $\ge 0$) and $\lim_{x \to \infty} g(x) = 0$.</li>
</ol>
<div class="math-display">
$$\mathbf{\text{Then the improper integral } \int_a^\infty f(x) g(x) \, dx \text{ converges.}}$$
</div>
<p><strong>Proof:</strong> Integrating by parts over $[a, B]$: $\int_a^B f(x)g(x) dx = F(B)g(B) - F(a)g(a) - \int_a^B F(x)g'(x)dx$. Since $|F(B)g(B)| \le M|g(B)| \to 0$ and $\int_a^\infty |F(x)g'(x)| dx \le M \int_a^\infty |g'(x)|dx = M g(a) < \infty$, the limit exists. $\blacksquare$</p>

<h4>2. The Dirichlet Sinc Integral: $\int_0^\infty \frac{\sin x}{x} \, dx = \frac{\pi}{2}$</h4>
<p>By Dirichlet's test with $f(x) = \sin(x)$ (bounded antiderivative $-\cos x \in [-1, 1]$) and $g(x) = \frac{1}{x} \to 0$ monotonically, $\int_1^\infty \frac{\sin x}{x} dx$ converges. Near $x = 0$, $\lim_{x \to 0} \frac{\sin x}{x} = 1$, so the integral is finite on $[0, 1]$. Hence $\int_0^\infty \frac{\sin x}{x} dx$ converges (conditionally, as $\int_0^\infty \frac{|\sin x|}{x} dx = \infty$).</p>"""
    }
]

u5_problems = [
    {
        "id": "calc2-p5-1",
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Logarithmic $p$-Integral Classification",
        "statement": r"""Determine the values of real parameter $p$ for which the improper integral converges, and evaluate it:
$$I = \int_2^\infty \frac{dx}{x (\ln x)^p}$$""",
        "solution": r"""<h4>Step 1: Substitute $u = \ln(x)$</h4>
<p>Let $u = \ln(x) \implies du = \frac{1}{x} dx$.</p>
<p>When $x = 2$, $u = \ln(2)$; as $x \to \infty$, $u \to \infty$.</p>
<div class="math-display">
$$I = \int_{\ln(2)}^\infty \frac{du}{u^p}$$
</div>

<h4>Step 2: Apply the $p$-Integral Convergence Criterion</h4>
<p>This is a standard Type I power integral:</p>
<ul>
  <li>If $p > 1$:
    $$I = \lim_{M \to \infty} \left[ \frac{u^{1-p}}{1-p} \right]_{\ln(2)}^M = \lim_{M \to \infty} \left( \frac{M^{1-p}}{1-p} - \frac{(\ln 2)^{1-p}}{1-p} \right) = \frac{(\ln 2)^{1-p}}{p - 1} = \frac{1}{(p-1)(\ln 2)^{p-1}}$$
  </li>
  <li>If $p \le 1$: The integral diverges to $\infty$.</li>
</ul>""",
        "answer": r"""Converges $\iff p > 1$, with value $I = \frac{1}{(p-1)(\ln 2)^{p-1}}$."""
    },
    {
        "id": "calc2-p5-2",
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Cauchy Principal Value of a Rational Integrand",
        "statement": r"""Evaluate both the standard improper integral and the Cauchy Principal Value of:
$$I = \int_{-\infty}^\infty \frac{x}{x^2 + 2x + 2} \, dx$$""",
        "solution": r"""<h4>Step 1: Test for Standard Convergence</h4>
<p>Complete the square in the denominator: $x^2 + 2x + 2 = (x + 1)^2 + 1$.</p>
<p>As $x \to \pm\infty$, $\frac{x}{x^2 + 2x + 2} \sim \frac{1}{x}$. Since $\int_1^\infty \frac{1}{x} dx$ diverges logarithmically, the independent limits $\int_0^\infty f(x)dx$ and $\int_{-\infty}^0 f(x)dx$ diverge. Therefore, the integral <strong>diverges in the standard sense</strong>.</p>

<h4>Step 2: Evaluate the Cauchy Principal Value</h4>
<div class="math-display">
$$\operatorname{P.V.} I = \lim_{R \to \infty} \int_{-R}^R \frac{x}{(x+1)^2 + 1} \, dx$$
</div>
<p>Substitute $u = x + 1 \implies x = u - 1$, $dx = du$. When $x = -R$, $u = 1 - R$; when $x = R$, $u = 1 + R$:</p>
<div class="math-display">
$$\int_{1-R}^{1+R} \frac{u - 1}{u^2 + 1} \, du = \int_{1-R}^{1+R} \frac{u}{u^2 + 1} \, du - \int_{1-R}^{1+R} \frac{1}{u^2 + 1} \, du$$
</div>
<p>Evaluate the logarithmic term:</p>
<div class="math-display">
$$\int_{1-R}^{1+R} \frac{u}{u^2 + 1} \, du = \left[ \frac{1}{2} \ln(u^2 + 1) \right]_{1-R}^{1+R} = \frac{1}{2} \ln\left( \frac{(1+R)^2 + 1}{(1-R)^2 + 1} \right) = \frac{1}{2} \ln\left( \frac{R^2 + 2R + 2}{R^2 - 2R + 2} \right)$$
</div>
<p>As $R \to \infty$, the argument of the logarithm tends to $1$, so $\lim_{R \to \infty} \frac{1}{2}\ln(1) = 0$.</p>
<p>Evaluate the arctangent term:</p>
<div class="math-display">
$$\int_{1-R}^{1+R} \frac{1}{u^2 + 1} \, du = \Big[ \arctan(u) \Big]_{1-R}^{1+R} = \arctan(1 + R) - \arctan(1 - R)$$
</div>
<p>As $R \to \infty$:</p>
<div class="math-display">
$$\lim_{R \to \infty} \Big( \arctan(1+R) - \arctan(1-R) \Big) = \frac{\pi}{2} - \left(-\frac{\pi}{2}\right) = \pi$$
</div>
<div class="math-display">
$$\operatorname{P.V.} I = 0 - \pi = -\mathbf{\pi}$$
</div>""",
        "answer": r"""Standard integral diverges; $\operatorname{P.V.} \int_{-\infty}^\infty \frac{x}{x^2+2x+2} dx = -\pi$."""
    },
    {
        "id": "calc2-p5-3",
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Evaluation of the Dirichlet Sinc Integral via Feynman's Trick",
        "statement": r"""Prove that the Dirichlet improper integral converges to:
$$I = \int_0^\infty \frac{\sin(x)}{x} \, dx = \frac{\pi}{2}$$
using Feynman's parameter differentiation method on $I(\alpha) = \int_0^\infty e^{-\alpha x} \frac{\sin x}{x} \, dx$ for $\alpha > 0$.""",
        "solution": r"""<h4>Step 1: Introduce the Damping Parameter $\alpha > 0$</h4>
<p>Define the parametric integral for $\alpha > 0$:</p>
<div class="math-display">
$$I(\alpha) = \int_0^\infty e^{-\alpha x} \frac{\sin(x)}{x} \, dx$$
</div>
<p>Note that $\lim_{\alpha \to 0^+} I(\alpha) = I(0) = \int_0^\infty \frac{\sin x}{x} dx$, and as $\alpha \to \infty$, the exponential damping drives $I(\alpha) \to 0$.</p>

<h4>Step 2: Differentiate Under the Integral Sign</h4>
<p>Applying the Leibniz rule with respect to parameter $\alpha$:</p>
<div class="math-display">
$$I'(\alpha) = \frac{d}{d\alpha} \int_0^\infty e^{-\alpha x} \frac{\sin(x)}{x} \, dx = \int_0^\infty \frac{\partial}{\partial \alpha} \left( e^{-\alpha x} \frac{\sin(x)}{x} \right) dx = \int_0^\infty -x e^{-\alpha x} \frac{\sin(x)}{x} \, dx$$
</div>
<div class="math-display">
$$I'(\alpha) = -\int_0^\infty e^{-\alpha x} \sin(x) \, dx$$
</div>

<h4>Step 3: Evaluate the Auxiliary Exponential-Sine Integral</h4>
<p>Using the cyclic integration formula derived in Unit 1 (§1.1):</p>
<div class="math-display">
$$\int_0^\infty e^{-\alpha x} \sin(x) \, dx = \left[ \frac{e^{-\alpha x}}{\alpha^2 + 1} \Big( -\alpha \sin(x) - \cos(x) \Big) \right]_0^\infty = 0 - \left( \frac{1}{\alpha^2 + 1} (0 - 1) \right) = \frac{1}{\alpha^2 + 1}$$
</div>
<p>Thus, we have the first-order differential equation:</p>
<div class="math-display">
$$I'(\alpha) = -\frac{1}{\alpha^2 + 1}$$
</div>

<h4>Step 4: Integrate with Respect to $\alpha$ and Apply Boundary Conditions</h4>
<div class="math-display">
$$I(\alpha) = -\int \frac{1}{\alpha^2 + 1} \, d\alpha = -\arctan(\alpha) + C$$
</div>
<p>Taking the limit as $\alpha \to \infty$:</p>
<div class="math-display">
$$\lim_{\alpha \to \infty} I(\alpha) = 0 \implies -\frac{\pi}{2} + C = 0 \implies C = \frac{\pi}{2}$$
</div>
<div class="math-display">
$$I(\alpha) = \frac{\pi}{2} - \arctan(\alpha)$$
</div>
<p>Taking the limit as $\alpha \to 0^+$:</p>
<div class="math-display">
$$\mathbf{I = \lim_{\alpha \to 0^+} I(\alpha) = \frac{\pi}{2} - \arctan(0) = \frac{\pi}{2}} \quad \blacksquare$$
</div>""",
        "answer": r"""$\int_0^\infty \frac{\sin(x)}{x} \, dx = \frac{\pi}{2}$"""
    }
]

u5_data = {
    "id": "unit5",
    "unit_number": 5,
    "title": "Improper Integrals & Rigorous Convergence Tests",
    "subtitle": "Type I & II Integrals, Cauchy Principal Value, Comparison Tests & The Dirichlet Sinc Integral",
    "sections": u5_sections,
    "simulations": ["sim_calc2_improper"],
    "problems": u5_problems
}


# ==========================================
# UNIT 6: SPECIAL FUNCTIONS: EULER'S GAMMA & BETA FUNCTIONS
# ==========================================
u6_sections = [
    {
        "id": "u6-sec1",
        "title": "Euler's Gamma Function: Axiomatic Integral, Recurrence & Factorial Interpolation",
        "content": r"""<h4>1. Definition of the Gamma Function</h4>
<p>The <strong>Euler Gamma Function</strong> $\Gamma(z)$ is defined for all complex numbers with positive real part $\operatorname{Re}(z) > 0$ (and for all real $x > 0$) by the improper integral:</p>
<div class="math-display">
$$\mathbf{\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \, dt}$$
</div>

<h4>2. The Fundamental Recurrence Relation: $\Gamma(z+1) = z\Gamma(z)$</h4>
<p>Applying integration by parts with $u = t^z \implies du = z t^{z-1} dt$ and $dv = e^{-t} dt \implies v = -e^{-t}$:</p>
<div class="math-display">
$$\Gamma(z+1) = \int_0^\infty t^z e^{-t} \, dt = \Big[ -t^z e^{-t} \Big]_0^\infty + z \int_0^\infty t^{z-1} e^{-t} \, dt$$
</div>
<p>For $\operatorname{Re}(z) > 0$, $\lim_{t \to \infty} t^z e^{-t} = 0$ and $\lim_{t \to 0^+} t^z e^{-t} = 0$. Thus:</p>
<div class="math-display">
$$\mathbf{\Gamma(z+1) = z \Gamma(z)}$$
</div>

<h4>3. Factorial Interpolation for Non-Negative Integers</h4>
<p>Evaluating the base case at $z = 1$:</p>
<div class="math-display">
$$\Gamma(1) = \int_0^\infty e^{-t} \, dt = \Big[ -e^{-t} \Big]_0^\infty = 0 - (-1) = 1$$
</div>
<p>By mathematical induction, for any positive integer $n \in \mathbb{N}$:</p>
<div class="math-display">
$$\mathbf{\Gamma(n+1) = n \cdot \Gamma(n) = n(n-1)\cdots 1 \cdot \Gamma(1) = n!}$$
</div>
<p>Thus, $\Gamma(z)$ extends the discrete factorial function continuously across the real continuum: $\Gamma(n) = (n - 1)!$.</p>"""
    },
    {
        "id": "u6-sec2",
        "title": "Half-Integer Values, The Reflection Formula & Legendre Duplication",
        "content": r"""<h4>1. The Fundamental Half-Integer Value: $\Gamma(1/2) = \sqrt{\pi}$</h4>
<p>Setting $z = 1/2$ in the definition:</p>
<div class="math-display">
$$\Gamma(1/2) = \int_0^\infty t^{-1/2} e^{-t} \, dt$$
</div>
<p>Substitute $t = u^2 \implies dt = 2u \, du$:</p>
<div class="math-display">
$$\Gamma(1/2) = \int_0^\infty \frac{1}{u} e^{-u^2} (2u \, du) = 2 \int_0^\infty e^{-u^2} \, du = \int_{-\infty}^\infty e^{-u^2} \, du = \mathbf{\sqrt{\pi}}$$
</div>
<p>Using the recurrence $\Gamma(x+1) = x\Gamma(x)$, higher half-integers are directly calculated:</p>
<div class="math-display">
$$\Gamma(3/2) = \frac{1}{2}\sqrt{\pi}, \quad \Gamma(5/2) = \frac{3}{4}\sqrt{\pi}, \quad \Gamma(7/2) = \frac{15}{8}\sqrt{\pi} = \frac{(2n-1)!!}{2^n}\sqrt{\pi}$$
</div>

<h4>2. Euler's Reflection Formula</h4>
<p>For any non-integer $z \in \mathbb{C} \setminus \mathbb{Z}$:</p>
<div class="math-display">
$$\mathbf{\Gamma(z) \Gamma(1 - z) = \frac{\pi}{\sin(\pi z)}}$$
</div>
<p>This remarkable identity links Gamma functions to circular trigonometry. Notice that for $z = 1/2$, $\Gamma(1/2)^2 = \frac{\pi}{\sin(\pi/2)} = \pi \implies \Gamma(1/2) = \sqrt{\pi}$.</p>

<h4>3. Legendre's Duplication Formula</h4>
<div class="math-display">
$$\mathbf{\Gamma(z) \Gamma\left(z + \frac{1}{2}\right) = 2^{1 - 2z} \sqrt{\pi} \, \Gamma(2z)}$$
</div>"""
    },
    {
        "id": "u6-sec3",
        "title": "Euler's Beta Function: Standard, Trigonometric & Infinite Representations",
        "content": r"""<h4>1. Definition of the Beta Function</h4>
<p>The <strong>Euler Beta Function</strong> $B(p, q)$ is defined for $p, q > 0$ by the compact interval integral:</p>
<div class="math-display">
$$\mathbf{B(p, q) = \int_0^1 t^{p-1} (1 - t)^{q-1} \, dt}$$
</div>

<h4>2. Fundamental Symmetry: $B(p, q) = B(q, p)$</h4>
<p>Substituting $u = 1 - t \implies dt = -du$ swaps the endpoints $t = 0 \to u = 1$ and $t = 1 \to u = 0$:</p>
<div class="math-display">
$$B(p, q) = \int_1^0 (1 - u)^{p-1} u^{q-1} (-du) = \int_0^1 u^{q-1} (1 - u)^{p-1} \, du = \mathbf{B(q, p)}$$
</div>

<h4>3. Alternative Representations</h4>
<ul>
  <li><strong>Trigonometric Form:</strong> Substitute $t = \sin^2\theta \implies dt = 2\sin\theta\cos\theta \, d\theta$:
    $$\mathbf{B(p, q) = 2 \int_0^{\pi/2} \sin^{2p-1}(\theta) \cos^{2q-1}(\theta) \, d\theta}$$
  </li>
  <li><strong>Infinite Domain Form:</strong> Substitute $t = \frac{u}{1 + u} \implies 1 - t = \frac{1}{1 + u}, dt = \frac{du}{(1+u)^2}$:
    $$\mathbf{B(p, q) = \int_0^\infty \frac{u^{p-1}}{(1 + u)^{p + q}} \, du}$$
  </li>
</ul>"""
    },
    {
        "id": "u6-sec4",
        "title": "The Fundamental Bridge: Line-by-Line Proof of $B(p, q) = \\frac{\\Gamma(p)\\Gamma(q)}{\\Gamma(p+q)}$",
        "content": r"""<h4>1. The Bridge Theorem</h4>
<div class="math-display">
$$\mathbf{B(p, q) = \frac{\Gamma(p) \Gamma(q)}{\Gamma(p + q)}}$$
</div>

<h4>2. Rigorous Multi-Dimensional Transformation Proof</h4>
<p>Consider the product of two Gamma functions expressed under substitutions $t = x^2$ and $s = y^2$:</p>
<div class="math-display">
$$\Gamma(p) = \int_0^\infty t^{p-1} e^{-t} \, dt = 2 \int_0^\infty x^{2p-1} e^{-x^2} \, dx$$
</div>
<div class="math-display">
$$\Gamma(q) = \int_0^\infty s^{q-1} e^{-s} \, ds = 2 \int_0^\infty y^{2q-1} e^{-y^2} \, dy$$
</div>
<p>Multiplying these two independent single integrals produces a double integral over the first quadrant $Q_1 = \{ (x, y) : x \ge 0, y \ge 0 \}$ of $\mathbb{R}^2$:</p>
<div class="math-display">
$$\Gamma(p) \Gamma(q) = 4 \int_0^\infty \int_0^\infty x^{2p-1} y^{2q-1} e^{-(x^2 + y^2)} \, dx \, dy$$
</div>
<p>Transform into 2D polar coordinates: $x = r\cos\theta, y = r\sin\theta, dx\,dy = r\,dr\,d\theta$ with $r \in [0, \infty)$ and $\theta \in [0, \pi/2]$:</p>
<div class="math-display">
$$\begin{aligned}
\Gamma(p) \Gamma(q) &= 4 \int_0^{\pi/2} \int_0^\infty (r\cos\theta)^{2p-1} (r\sin\theta)^{2q-1} e^{-r^2} r \, dr \, d\theta \\
&= 4 \left( \int_0^\infty r^{2(p+q) - 1} e^{-r^2} \, dr \right) \left( \int_0^{\pi/2} \cos^{2p-1}(\theta) \sin^{2q-1}(\theta) \, d\theta \right)
\end{aligned}$$
</div>
<p>Recognize both parenthetical factors:</p>
<ol>
  <li>The radial factor: substituting $u = r^2 \implies du = 2r\,dr$ gives $2 \int_0^\infty r^{2(p+q)-1} e^{-r^2} dr = \int_0^\infty u^{(p+q)-1} e^{-u} du = \mathbf{\Gamma(p + q)}$.</li>
  <li>The angular factor: by the trigonometric form of the Beta function from Section 6.3:
    $$2 \int_0^{\pi/2} \sin^{2q-1}(\theta) \cos^{2p-1}(\theta) \, d\theta = \mathbf{B(p, q)}$$
  </li>
</ol>
<p>Therefore:</p>
<div class="math-display">
$$\Gamma(p) \Gamma(q) = \Gamma(p + q) \cdot B(p, q) \implies \mathbf{B(p, q) = \frac{\Gamma(p) \Gamma(q)}{\Gamma(p + q)}} \quad \blacksquare$$
</div>"""
    },
    {
        "id": "u6-sec5",
        "title": "Applications of Gamma & Beta Functions: Hypersphere Volumes & Asymptotics",
        "content": r"""<h4>1. Volume of the $n$-Dimensional Euclidean Ball $V_n(R)$</h4>
<p>Let $B_n(R) = \{ x \in \mathbb{R}^n : \sum_{i=1}^n x_i^2 \le R^2 \}$ be the $n$-dimensional Euclidean ball of radius $R$. Its volume scales as $V_n(R) = C_n R^n$.</p>
<p>Integrating the multi-variable Gaussian over $\mathbb{R}^n$:</p>
<div class="math-display">
$$\int_{\mathbb{R}^n} e^{-\|x\|^2} \, d^n x = \left( \int_{-\infty}^\infty e^{-x^2} dx \right)^n = (\sqrt{\pi})^n = \pi^{n/2}$$
</div>
<p>Converting to spherical shell integration $d^n x = S_{n-1}(r) dr = n C_n r^{n-1} dr$:</p>
<div class="math-display">
$$\int_{\mathbb{R}^n} e^{-\|x\|^2} \, d^n x = n C_n \int_0^\infty r^{n-1} e^{-r^2} \, dr$$
</div>
<p>With substitution $u = r^2$, the integral evaluates to $\frac{1}{2}\Gamma(n/2)$. Thus:</p>
<div class="math-display">
$$\pi^{n/2} = n C_n \cdot \frac{1}{2}\Gamma(n/2) = C_n \cdot \frac{n}{2}\Gamma(n/2) = C_n \Gamma\left(\frac{n}{2} + 1\right)$$
</div>
<div class="math-display">
$$\mathbf{V_n(R) = \frac{\pi^{n/2}}{\Gamma\left(\frac{n}{2} + 1\right)} R^n}$$
</div>

<h4>2. Verification in Low Dimensions</h4>
<ul>
  <li>$n = 1$: $V_1(R) = \frac{\pi^{1/2}}{\Gamma(3/2)} R = \frac{\sqrt{\pi}}{\frac{1}{2}\sqrt{\pi}} R = 2R$ (Line segment length)</li>
  <li>$n = 2$: $V_2(R) = \frac{\pi^1}{\Gamma(2)} R^2 = \pi R^2$ (Circular disk area)</li>
  <li>$n = 3$: $V_3(R) = \frac{\pi^{3/2}}{\Gamma(5/2)} R^3 = \frac{\pi^{3/2}}{\frac{3}{4}\sqrt{\pi}} R^3 = \frac{4}{3}\pi R^3$ (3D sphere volume)</li>
  <li>$n = 4$: $V_4(R) = \frac{\pi^2}{\Gamma(3)} R^4 = \frac{\pi^2}{2} R^4$ (4D hypersphere volume)</li>
</ul>"""
    }
]

u6_problems = [
    {
        "id": "calc2-p6-1",
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Trigonometric Definite Integral via Beta Functions",
        "statement": r"""Evaluate the definite integral using the Beta and Gamma functions:
$$I = \int_0^{\pi/2} \sin^6(\theta) \cos^4(\theta) \, d\theta$$""",
        "solution": r"""<h4>Step 1: Match with the Trigonometric Beta Representation</h4>
<p>Recall the identity:</p>
<div class="math-display">
$$2 \int_0^{\pi/2} \sin^{2p-1}(\theta) \cos^{2q-1}(\theta) \, d\theta = B(p, q)$$
</div>
<p>Equating exponents:</p>
<div class="math-display">
$$2p - 1 = 6 \implies 2p = 7 \implies p = \frac{7}{2}$$
</div>
<div class="math-display">
$$2q - 1 = 4 \implies 2q = 5 \implies q = \frac{5}{2}$$
</div>
<div class="math-display">
$$I = \frac{1}{2} B\left(\frac{7}{2}, \frac{5}{2}\right) = \frac{1}{2} \frac{\Gamma(7/2) \Gamma(5/2)}{\Gamma(7/2 + 5/2)} = \frac{1}{2} \frac{\Gamma(7/2) \Gamma(5/2)}{\Gamma(6)}$$
</div>

<h4>Step 2: Evaluate the Gamma Values</h4>
<div class="math-display">
$$\Gamma(7/2) = \frac{5}{2} \cdot \frac{3}{2} \cdot \frac{1}{2} \sqrt{\pi} = \frac{15}{8} \sqrt{\pi}$$
</div>
<div class="math-display">
$$\Gamma(5/2) = \frac{3}{2} \cdot \frac{1}{2} \sqrt{\pi} = \frac{3}{4} \sqrt{\pi}$$
</div>
<div class="math-display">
$$\Gamma(6) = 5! = 120$$
</div>

<h4>Step 3: Combine and Simplify</h4>
<div class="math-display">
$$I = \frac{1}{2} \frac{\left( \frac{15}{8}\sqrt{\pi} \right) \left( \frac{3}{4}\sqrt{\pi} \right)}{120} = \frac{1}{2} \frac{\frac{45}{32} \pi}{120} = \frac{45\pi}{64 \times 120} = \frac{3\pi}{64 \times 8} = \frac{3\pi}{512}$$
</div>""",
        "answer": r"""$I = \frac{3\pi}{512}$"""
    },
    {
        "id": "calc2-p6-2",
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Improper Integral via Algebraic Beta Transformation",
        "statement": r"""Evaluate the improper integral:
$$I = \int_0^\infty \frac{x^2}{(1 + x^4)^2} \, dx$$
by mapping to the Beta function.""",
        "solution": r"""<h4>Step 1: Perform the Variable Transformation</h4>
<p>Substitute $u = x^4 \implies x = u^{1/4}$, with differential $dx = \frac{1}{4} u^{-3/4} du$.</p>
<p>When $x = 0 \implies u = 0$, and when $x \to \infty \implies u \to \infty$.</p>
<div class="math-display">
$$x^2 = (u^{1/4})^2 = u^{1/2}$$
</div>
<div class="math-display">
$$I = \int_0^\infty \frac{u^{1/2}}{(1 + u)^2} \left( \frac{1}{4} u^{-3/4} \, du \right) = \frac{1}{4} \int_0^\infty \frac{u^{1/2 - 3/4}}{(1 + u)^2} \, du = \frac{1}{4} \int_0^\infty \frac{u^{-1/4}}{(1 + u)^2} \, du$$
</div>

<h4>Step 2: Match with the Infinite Beta Representation</h4>
<p>Recall the identity:</p>
<div class="math-display">
$$B(p, q) = \int_0^\infty \frac{u^{p-1}}{(1 + u)^{p+q}} \, du$$
</div>
<p>Equating exponents:</p>
<div class="math-display">
$$p - 1 = -\frac{1}{4} \implies p = \frac{3}{4}$$
</div>
<div class="math-display">
$$p + q = 2 \implies \frac{3}{4} + q = 2 \implies q = \frac{5}{4}$$
</div>
<div class="math-display">
$$I = \frac{1}{4} B\left(\frac{3}{4}, \frac{5}{4}\right) = \frac{1}{4} \frac{\Gamma(3/4) \Gamma(5/4)}{\Gamma(3/4 + 5/4)} = \frac{1}{4} \frac{\Gamma(3/4) \Gamma(5/4)}{\Gamma(2)}$$
</div>

<h4>Step 3: Apply the Reflection Formula</h4>
<p>Since $\Gamma(2) = 1! = 1$ and $\Gamma(5/4) = \frac{1}{4}\Gamma(1/4)$:</p>
<div class="math-display">
$$I = \frac{1}{4} \cdot \Gamma\left(\frac{3}{4}\right) \left( \frac{1}{4}\Gamma\left(\frac{1}{4}\right) \right) = \frac{1}{16} \Gamma\left(\frac{1}{4}\right) \Gamma\left(1 - \frac{1}{4}\right)$$
</div>
<p>By Euler's Reflection Formula $\Gamma(z)\Gamma(1-z) = \frac{\pi}{\sin(\pi z)}$ with $z = 1/4$:</p>
<div class="math-display">
$$\Gamma\left(\frac{1}{4}\right) \Gamma\left(\frac{3}{4}\right) = \frac{\pi}{\sin(\pi/4)} = \frac{\pi}{1/\sqrt{2}} = \pi \sqrt{2}$$
</div>
<div class="math-display">
$$I = \frac{1}{16} \Big( \pi \sqrt{2} \Big) = \mathbf{\frac{\pi \sqrt{2}}{16}}$$
</div>""",
        "answer": r"""$I = \frac{\pi\sqrt{2}}{16}$"""
    },
    {
        "id": "calc2-p6-3",
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Derivation of the Fractional Dimension Gamma Peak",
        "statement": r"""Consider the volume $V_n$ of an $n$-dimensional unit ball ($R = 1$) as a continuous function of real dimension $n \in [0, \infty)$:
$$V(n) = \frac{\pi^{n/2}}{\Gamma(n/2 + 1)}$$
(a) Evaluate $V(n)$ for $n = 0, 1, 2, 3, 4, 5, 6$.
(b) Prove that as $n \to \infty$, $V(n) \to 0$ (the volume of a unit hypersphere vanishes in infinite dimensions).
(c) Determine the exact dimension $n^*$ at which the unit ball volume reaches its global maximum.""",
        "solution": r"""<h4>Part (a): Values in Dimensions $n = 0$ to $6$</h4>
<ul>
  <li>$n = 0$: $V(0) = \frac{1}{\Gamma(1)} = 1$</li>
  <li>$n = 1$: $V(1) = \frac{\sqrt{\pi}}{\Gamma(3/2)} = 2$</li>
  <li>$n = 2$: $V(2) = \frac{\pi}{\Gamma(2)} = \pi \approx 3.1416$</li>
  <li>$n = 3$: $V(3) = \frac{\pi^{3/2}}{\Gamma(5/2)} = \frac{4}{3}\pi \approx 4.1888$</li>
  <li>$n = 4$: $V(4) = \frac{\pi^2}{\Gamma(3)} = \frac{\pi^2}{2} \approx 4.9348$</li>
  <li>$n = 5$: $V(5) = \frac{\pi^{5/2}}{\Gamma(7/2)} = \frac{8\pi^2}{15} \approx 5.2638$</li>
  <li>$n = 6$: $V(6) = \frac{\pi^3}{\Gamma(4)} = \frac{\pi^3}{6} \approx 5.1677$</li>
</ul>
<p>Notice that the volume increases up to $n = 5$ ($V(5) \approx 5.2638$) and then drops at $n = 6$ ($V(6) \approx 5.1677$)!</p>

<h4>Part (b): Asymptotic Limit as $n \to \infty$</h4>
<p>By Stirling's approximation, $\Gamma(x+1) \sim \sqrt{2\pi x}\left(\frac{x}{e}\right)^x$. With $x = n/2$:</p>
<div class="math-display">
$$V(n) \sim \frac{\pi^{n/2}}{\sqrt{\pi n} \left( \frac{n}{2e} \right)^{n/2}} = \frac{1}{\sqrt{\pi n}} \left( \frac{2\pi e}{n} \right)^{n/2}$$
</div>
<p>For $n > 2\pi e \approx 17.079$, the base $\frac{2\pi e}{n} < 1$, driving the power to zero at a super-exponential rate:</p>
<div class="math-display">
$$\mathbf{\lim_{n \to \infty} V(n) = 0} \quad \blacksquare$$
</div>

<h4>Part (c): Global Maximum Dimension $n^*$</h4>
<p>Taking the natural logarithm of $V(n)$:</p>
<div class="math-display">
$$\ln V(n) = \frac{n}{2}\ln(\pi) - \ln\Gamma\left(\frac{n}{2} + 1\right)$$
</div>
<p>Differentiating with respect to $n$ and setting to zero:</p>
<div class="math-display">
$$\frac{d}{dn} \ln V(n) = \frac{1}{2}\ln(\pi) - \frac{1}{2} \psi\left(\frac{n}{2} + 1\right) = 0 \implies \psi\left(\frac{n}{2} + 1\right) = \ln(\pi)$$
</div>
<p>where $\psi(z) = \frac{\Gamma'(z)}{\Gamma(z)}$ is the Digamma function. Solving $\psi(z) = \ln(\pi) \approx 1.14473$ numerically yields $z \approx 3.627$, which corresponds to:</p>
<div class="math-display">
$$\frac{n^*}{2} + 1 \approx 3.627 \implies \frac{n^*}{2} \approx 2.627 \implies \mathbf{n^* \approx 5.2569}$$
</div>
<p>Thus, the unit hypersphere volume peaks at dimension $n^* \approx 5.26$, explaining why among integers, the maximum occurs at dimension $n = 5$.</p>""",
        "answer": r"""$V(n) \to 0$ as $n \to \infty$; global maximum occurs at $n^* \approx 5.26$ with integer maximum at $n = 5$ ($V(5) \approx 5.2638$)."""
    }
]

u6_data = {
    "id": "unit6",
    "unit_number": 6,
    "title": "Special Functions: Euler's Gamma & Beta Functions",
    "subtitle": "Factorial Interpolation, The Beta-Gamma Bridge, Reflection Identities & Hypersphere Volumes",
    "sections": u6_sections,
    "simulations": ["sim_calc2_gamma_beta"],
    "problems": u6_problems
}

# Write files
with open("calc2_u5.json", "w", encoding="utf-8") as f:
    json.dump(u5_data, f, indent=2, ensure_ascii=False)
print("Saved calc2_u5.json successfully.")

with open("calc2_u6.json", "w", encoding="utf-8") as f:
    json.dump(u6_data, f, indent=2, ensure_ascii=False)
print("Saved calc2_u6.json successfully.")
