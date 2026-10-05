import json

print("Building Calculus II: Units 1 & 2...")

# ==========================================
# UNIT 1: ADVANCED TECHNIQUES OF INTEGRATION & REDUCTION
# ==========================================
u1_sections = [
    {
        "id": "u1-sec1",
        "title": "Integration by Parts: Differential Foundations, Cyclic Reductions & Tabular Integration",
        "content": r"""<h4>1. Product Rule & Differential Derivation</h4>
<p>Integration by parts is the integral calculus analog of the differential product rule. For two continuously differentiable functions $u, v \in C^1([a, b])$, the differential of their product is given by:</p>
<div class="math-display">
$$d(uv) = u \, dv + v \, du$$
</div>
<p>Integrating both sides over the real interval $[a, b]$ yields the fundamental integration by parts identity:</p>
<div class="math-display">
$$\int u \, dv = uv - \int v \, du \quad \Longleftrightarrow \quad \int_a^b u(x) v'(x) \, dx = \Big[ u(x)v(x) \Big]_a^b - \int_a^b v(x) u'(x) \, dx$$
</div>

<h4>2. Optimal Choice of Partitions: The LIATE Heuristic</h4>
<p>To ensure that the residual integral $\int v \, du$ is strictly simpler than the original integral $\int u \, dv$, the choice of $u(x)$ typically follows the <strong>LIATE priority hierarchy</strong>:</p>
<ol>
  <li><strong>L</strong>ogarithmic functions: $\ln(x), \log_b(x)$ (differentiate to simple rational functions)</li>
  <li><strong>I</strong>nverse trigonometric functions: $\arcsin(x), \arctan(x), \operatorname{arcsec}(x)$</li>
  <li><strong>A</strong>lgebraic polynomials: $x^n, ax + b$ (differentiate to lower degrees)</li>
  <li><strong>T</strong>rigonometric functions: $\sin(x), \cos(x), \sec(x)$ (stable under differentiation)</li>
  <li><strong>E</strong>xponential functions: $e^{ax}, b^x$ (trivially integrable as $dv$)</li>
</ol>

<h4>3. Cyclic (Self-Referential) Integrals</h4>
<p>When integrating products of exponential and trigonometric functions, integration by parts reproduces the original integrand after two successive applications. Consider the archetypal cyclic integral:</p>
<div class="math-display">
$$I = \int e^{ax} \cos(bx) \, dx$$
</div>
<p><strong>Step 1:</strong> Let $u = e^{ax}$ and $dv = \cos(bx) \, dx$. Then $du = a e^{ax} \, dx$ and $v = \frac{1}{b}\sin(bx)$:</p>
<div class="math-display">
$$I = \frac{1}{b} e^{ax}\sin(bx) - \frac{a}{b} \int e^{ax} \sin(bx) \, dx$$
</div>
<p><strong>Step 2:</strong> Apply integration by parts to the new integral with $u_1 = e^{ax}$ and $dv_1 = \sin(bx) \, dx$, giving $du_1 = a e^{ax} \, dx$ and $v_1 = -\frac{1}{b}\cos(bx)$:</p>
<div class="math-display">
$$\int e^{ax} \sin(bx) \, dx = -\frac{1}{b} e^{ax}\cos(bx) + \frac{a}{b} \int e^{ax}\cos(bx) \, dx = -\frac{1}{b} e^{ax}\cos(bx) + \frac{a}{b} I$$
</div>
<p><strong>Step 3:</strong> Substituting back into the primary equation:</p>
<div class="math-display">
$$I = \frac{1}{b} e^{ax}\sin(bx) - \frac{a}{b} \left( -\frac{1}{b} e^{ax}\cos(bx) + \frac{a}{b} I \right) = \frac{e^{ax}}{b}\sin(bx) + \frac{a e^{ax}}{b^2}\cos(bx) - \frac{a^2}{b^2} I$$
</div>
<p>Collecting like terms in $I$:</p>
<div class="math-display">
$$\left( 1 + \frac{a^2}{b^2} \right) I = \frac{a^2 + b^2}{b^2} I = \frac{e^{ax}}{b^2} \Big( b \sin(bx) + a \cos(bx) \Big)$$
</div>
<div class="math-display">
$$I = \int e^{ax}\cos(bx) \, dx = \frac{e^{ax}}{a^2 + b^2} \Big( a \cos(bx) + b \sin(bx) \Big) + C$$
</div>

<h4>4. The Stand-Alone Logarithmic & Inverse Trigonometric Technique</h4>
<p>Integrals of single functions such as $\int \ln(x) \, dx$ or $\int \arctan(x) \, dx$ are evaluated by setting the algebraic factor $dv = dx \implies v = x$:</p>
<div class="math-display">
$$\int \ln(x) \, dx = x \ln(x) - \int x \cdot \frac{1}{x} \, dx = x \ln(x) - \int 1 \, dx = x \ln(x) - x + C = x(\ln x - 1) + C$$
</div>
<div class="math-display">
$$\int \arctan(x) \, dx = x \arctan(x) - \int x \cdot \frac{1}{1 + x^2} \, dx = x \arctan(x) - \frac{1}{2} \ln(1 + x^2) + C$$
</div>"""
    },
    {
        "id": "u1-sec2",
        "title": "Rational Fractions: Heaviside Cover-Up, Repeated Factors & Irreducible Quadratics",
        "content": r"""<h4>1. Algebraic Theory of Partial Fraction Decomposition</h4>
<p>Let $R(x) = \frac{P(x)}{Q(x)}$ be a rational function where $P(x), Q(x) \in \mathbb{R}[x]$ are polynomials with real coefficients and $\gcd(P, Q) = 1$.</p>
<ul>
  <li><strong>Proper Rational Fractions:</strong> If $\deg(P) < \deg(Q)$, the fraction is proper. If $\deg(P) \ge \deg(Q)$, polynomial long division must first be executed: $R(x) = S(x) + \frac{P_1(x)}{Q(x)}$ where $\deg(P_1) < \deg(Q)$.</li>
  <li>By the Fundamental Theorem of Algebra, any monic polynomial $Q(x) \in \mathbb{R}[x]$ factors uniquely over $\mathbb{R}$ into products of distinct and repeated linear factors $(x - r)^m$ and irreducible quadratic factors $(x^2 + px + q)^k$ with negative discriminant $p^2 - 4q < 0$.</li>
</ul>

<h4>2. Distinct Linear Factors & Heaviside's Cover-Up Method</h4>
<p>When $Q(x) = (x - r_1)(x - r_2)\cdots(x - r_n)$ has distinct real roots $r_k$:</p>
<div class="math-display">
$$\frac{P(x)}{Q(x)} = \frac{A_1}{x - r_1} + \frac{A_2}{x - r_2} + \dots + \frac{A_n}{x - r_n}$$
</div>
<p>Multiplying both sides by $(x - r_k)$ and evaluating the limit as $x \to r_k$ eliminates all terms except $A_k$, establishing <strong>Heaviside's Cover-Up Formula</strong>:</p>
<div class="math-display">
$$A_k = \lim_{x \to r_k} (x - r_k) \frac{P(x)}{Q(x)} = \frac{P(r_k)}{Q'(r_k)}$$
</div>

<h4>3. Repeated Linear Factors & Irreducible Quadratics</h4>
<p>For higher multiplicities and quadratic factors:</p>
<ol>
  <li><strong>Repeated Linear:</strong> A factor $(x - r)^m$ contributes $m$ partial fractions:
    $$\frac{A_1}{x - r} + \frac{A_2}{(x - r)^2} + \dots + \frac{A_m}{(x - r)^m}$$
  </li>
  <li><strong>Irreducible Quadratic:</strong> A factor $(x^2 + px + q)$ ($p^2 - 4q < 0$) requires a linear numerator:
    $$\frac{Bx + C}{x^2 + px + q}$$
    Completing the square $x^2 + px + q = \left(x + \frac{p}{2}\right)^2 + \left(q - \frac{p^2}{4}\right) = u^2 + a^2$ decomposes the integral into a logarithmic part and an arctangent part:
    $$\int \frac{Bx + C}{x^2 + px + q} \, dx = \frac{B}{2}\ln(x^2 + px + q) + \frac{C - \frac{Bp}{2}}{\sqrt{q - p^2/4}} \arctan\left(\frac{x + p/2}{\sqrt{q - p^2/4}}\right) + C_0$$
  </li>
</ol>"""
    },
    {
        "id": "u1-sec3",
        "title": "Trigonometric Integrals & The Universal Weierstrass Substitution",
        "content": r"""<h4>1. Powers and Products of Trigonometric Functions</h4>
<p>Integrals of the form $\int \sin^m(x) \cos^n(x) \, dx$ are categorized by parity of the exponents:</p>
<ul>
  <li><strong>Case 1 ($m$ or $n$ is Odd):</strong> If $n = 2k + 1$ is odd, isolate $\cos(x)\,dx = d(\sin x)$ and convert remaining cosines using $\cos^{2k}(x) = (1 - \sin^2 x)^k$. The substitution $u = \sin(x)$ yields a purely polynomial integral:
    $$\int \sin^m(x) \cos^{2k+1}(x) \, dx = \int u^m (1 - u^2)^k \, du$$
  </li>
  <li><strong>Case 2 (Both $m$ and $n$ are Even):</strong> Apply the half-angle power reduction identities:
    $$\sin^2(x) = \frac{1 - \cos(2x)}{2}, \quad \cos^2(x) = \frac{1 + \cos(2x)}{2}, \quad \sin(x)\cos(x) = \frac{\sin(2x)}{2}$$
  </li>
</ul>

<h4>2. The Universal Weierstrass Half-Angle Substitution</h4>
<p>For any rational function of trigonometric terms $R(\sin x, \cos x)$, the transformation $t = \tan\left(\frac{x}{2}\right)$ maps the trigonometric integral onto a purely rational algebraic integral over $t \in \mathbb{R}$.</p>
<p><strong>Geometric Derivation:</strong> From the double-angle identities:</p>
<div class="math-display">
$$\cos(x) = \cos^2(x/2) - \sin^2(x/2) = \frac{\cos^2(x/2) - \sin^2(x/2)}{\cos^2(x/2) + \sin^2(x/2)} = \frac{1 - \tan^2(x/2)}{1 + \tan^2(x/2)} = \frac{1 - t^2}{1 + t^2}$$
</div>
<div class="math-display">
$$\sin(x) = 2\sin(x/2)\cos(x/2) = \frac{2\tan(x/2)}{1 + \tan^2(x/2)} = \frac{2t}{1 + t^2}$$
</div>
<p>Differentiating $x = 2\arctan(t)$ yields the differential element:</p>
<div class="math-display">
$$dx = \frac{2}{1 + t^2} \, dt$$
</div>
<div class="math-display">
$$\mathbf{\int R(\sin x, \cos x) \, dx = \int R\left( \frac{2t}{1 + t^2}, \, \frac{1 - t^2}{1 + t^2} \right) \frac{2}{1 + t^2} \, dt}$$
</div>
<p>This universal substitution transforms every rational trigonometric expression into a standard partial fraction problem.</p>"""
    },
    {
        "id": "u1-sec4",
        "title": "Successive Reduction Formulas: Recurrence Relations for Higher Powers",
        "content": r"""<h4>1. General Philosophy of Reduction Formulas</h4>
<p>When an integral depends on an integer parameter $n \in \mathbb{N}$, a <strong>reduction formula</strong> expresses the integral $I_n$ in terms of $I_{n-1}$ or $I_{n-2}$, allowing recursive reduction to elementary base cases ($I_0$ or $I_1$).</p>

<h4>2. Reduction Formula for $I_n = \int \sin^n(x) \, dx$</h4>
<p>Split the integrand as $\sin^n(x) = \sin^{n-1}(x) \cdot \sin(x)$ and set up integration by parts:</p>
<div class="math-display">
$$u = \sin^{n-1}(x) \implies du = (n-1)\sin^{n-2}(x)\cos(x) \, dx$$
</div>
<div class="math-display">
$$dv = \sin(x) \, dx \implies v = -\cos(x)$$
</div>
<p>Applying the formula $\int u \, dv = uv - \int v \, du$:</p>
<div class="math-display">
$$I_n = -\sin^{n-1}(x)\cos(x) + (n-1) \int \sin^{n-2}(x)\cos^2(x) \, dx$$
</div>
<p>Using the Pythagorean identity $\cos^2(x) = 1 - \sin^2(x)$:</p>
<div class="math-display">
$$\begin{aligned}
I_n &= -\sin^{n-1}(x)\cos(x) + (n-1) \int \sin^{n-2}(x)(1 - \sin^2 x) \, dx \\
&= -\sin^{n-1}(x)\cos(x) + (n-1) \int \sin^{n-2}(x) \, dx - (n-1) \int \sin^n(x) \, dx \\
&= -\sin^{n-1}(x)\cos(x) + (n-1) I_{n-2} - (n-1) I_n
\end{aligned}$$
</div>
<p>Collecting terms in $I_n$ on the left-hand side:</p>
<div class="math-display">
$$I_n + (n-1)I_n = n I_n = -\sin^{n-1}(x)\cos(x) + (n-1)I_{n-2}$$
</div>
<div class="math-display">
$$\mathbf{I_n = \int \sin^n(x) \, dx = -\frac{\sin^{n-1}(x)\cos(x)}{n} + \frac{n-1}{n} I_{n-2}}$$
</div>

<h4>3. Reduction Formula for $K_n = \int \sec^n(x) \, dx$</h4>
<p>Decomposing $\sec^n(x) = \sec^{n-2}(x) \cdot \sec^2(x)$ with $u = \sec^{n-2}(x)$ and $dv = \sec^2(x) \, dx$ gives $v = \tan(x)$ and $du = (n-2)\sec^{n-2}(x)\tan(x) \, dx$:</p>
<div class="math-display">
$$K_n = \sec^{n-2}(x)\tan(x) - (n-2) \int \sec^{n-2}(x)\tan^2(x) \, dx$$
</div>
<p>Since $\tan^2(x) = \sec^2(x) - 1$:</p>
<div class="math-display">
$$K_n = \sec^{n-2}(x)\tan(x) - (n-2) \left[ K_n - K_{n-2} \right]$$
</div>
<div class="math-display">
$$\mathbf{K_n = \int \sec^n(x) \, dx = \frac{\sec^{n-2}(x)\tan(x)}{n-1} + \frac{n-2}{n-1} K_{n-2}}$$
</div>"""
    },
    {
        "id": "u1-sec5",
        "title": "Wallis Formulas & The Infinite Product for $\\pi/2$",
        "content": r"""<h4>1. Definite Integrals on $[0, \pi/2]$</h4>
<p>Applying the reduction formula for $\sin^n(x)$ to the definite integral $W_n = \int_0^{\pi/2} \sin^n(x) \, dx$:</p>
<div class="math-display">
$$W_n = \left[ -\frac{\sin^{n-1}(x)\cos(x)}{n} \right]_0^{\pi/2} + \frac{n-1}{n} W_{n-2} = 0 + \frac{n-1}{n} W_{n-2}$$
</div>
<p>Base cases:</p>
<div class="math-display">
$$W_0 = \int_0^{\pi/2} 1 \, dx = \frac{\pi}{2}, \qquad W_1 = \int_0^{\pi/2} \sin(x) \, dx = \Big[ -\cos(x) \Big]_0^{\pi/2} = 1$$
</div>

<h4>2. Closed-Form Wallis Formulas</h4>
<p>Unwinding the recurrence relation $W_n = \frac{n-1}{n} W_{n-2}$ yields distinct expressions based on parity:</p>
<ul>
  <li><strong>Even Index ($n = 2m$):</strong>
    $$W_{2m} = \frac{2m-1}{2m} \cdot \frac{2m-3}{2m-2} \cdots \frac{1}{2} \cdot W_0 = \frac{(2m-1)!!}{(2m)!!} \cdot \frac{\pi}{2}$$
  </li>
  <li><strong>Odd Index ($n = 2m + 1$):</strong>
    $$W_{2m+1} = \frac{2m}{2m+1} \cdot \frac{2m-2}{2m-1} \cdots \frac{2}{3} \cdot W_1 = \frac{(2m)!!}{(2m+1)!!}$$
  </li>
</ul>

<h4>3. The Wallis Ratio & Infinite Product for $\pi/2$</h4>
<p>Since $0 \le \sin(x) \le 1$ for all $x \in [0, \pi/2]$, powers are monotonically decreasing:</p>
<div class="math-display">
$$\sin^{2m+1}(x) \le \sin^{2m}(x) \le \sin^{2m-1}(x) \implies W_{2m+1} \le W_{2m} \le W_{2m-1}$$
</div>
<p>Dividing by $W_{2m+1}$:</p>
<div class="math-display">
$$1 \le \frac{W_{2m}}{W_{2m+1}} \le \frac{W_{2m-1}}{W_{2m+1}} = \frac{2m+1}{2m} = 1 + \frac{1}{2m}$$
</div>
<p>By the Squeeze Theorem, as $m \to \infty$:</p>
<div class="math-display">
$$\lim_{m \to \infty} \frac{W_{2m}}{W_{2m+1}} = 1 \implies \lim_{m \to \infty} \left( \frac{(2m-1)!! (2m+1)!!}{[(2m)!!]^2} \cdot \frac{\pi}{2} \right) = 1$$
</div>
<p>Inverting the ratio establishes <strong>Wallis' Celebrated Infinite Product</strong> (1655):</p>
<div class="math-display">
$$\mathbf{\frac{\pi}{2} = \lim_{m \to \infty} \prod_{k=1}^m \frac{(2k)(2k)}{(2k-1)(2k+1)} = \frac{2}{1} \cdot \frac{2}{3} \cdot \frac{4}{3} \cdot \frac{4}{5} \cdot \frac{6}{5} \cdot \frac{6}{7} \cdots}$$
</div>"""
    }
]

u1_problems = [
    {
        "id": "calc2-p1-1",
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Repeated Integration by Parts for $x^3 e^{2x}$",
        "statement": r"""Evaluate the indefinite integral using repeated integration by parts and verify via the tabular method:
$$I = \int x^3 e^{2x} \, dx$$""",
        "solution": r"""<h4>Step 1: Setting up Tabular Differentiation and Integration</h4>
<p>Let $u(x) = x^3$ be the polynomial factor to be differentiated repeatedly until zero, and $dv = e^{2x}\,dx$ be the repeatedly integrated exponential factor:</p>
<table style="width:100%; border-collapse: collapse; margin: 1rem 0; text-align: center;">
  <thead>
    <tr style="border-bottom: 2px solid #334155;">
      <th style="padding: 6px;">Sign</th>
      <th style="padding: 6px;">Differentiate $D[u]$</th>
      <th style="padding: 6px;">Integrate $I[v]$</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="color:#10b981;">$+$</td><td>$x^3$</td><td>$\frac{1}{2} e^{2x}$</td></tr>
    <tr><td style="color:#ef4444;">$-$</td><td>$3x^2$</td><td>$\frac{1}{4} e^{2x}$</td></tr>
    <tr><td style="color:#10b981;">$+$</td><td>$6x$</td><td>$\frac{1}{8} e^{2x}$</td></tr>
    <tr><td style="color:#ef4444;">$-$</td><td>$6$</td><td>$\frac{1}{16} e^{2x}$</td></tr>
    <tr><td></td><td>$0$</td><td>$\frac{1}{32} e^{2x}$</td></tr>
  </tbody>
</table>

<h4>Step 2: Summing the Cross-Products</h4>
<p>Multiplying each derivative row by the succeeding integral row with the alternating signs:</p>
<div class="math-display">
$$I = (+1)(x^3)\left(\frac{1}{2}e^{2x}\right) + (-1)(3x^2)\left(\frac{1}{4}e^{2x}\right) + (+1)(6x)\left(\frac{1}{8}e^{2x}\right) + (-1)(6)\left(\frac{1}{16}e^{2x}\right) + C$$
</div>

<h4>Step 3: Factoring the Common Exponential</h4>
<div class="math-display">
$$I = e^{2x} \left( \frac{x^3}{2} - \frac{3x^2}{4} + \frac{3x}{4} - \frac{3}{8} \right) + C = \frac{e^{2x}}{8} \Big( 4x^3 - 6x^2 + 6x - 3 \Big) + C$$
</div>""",
        "answer": r"""$\int x^3 e^{2x} \, dx = \frac{e^{2x}}{8} \left( 4x^3 - 6x^2 + 6x - 3 \right) + C$"""
    },
    {
        "id": "calc2-p1-2",
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Partial Fractions with Irreducible Quadratics",
        "statement": r"""Evaluate the definite integral using partial fraction decomposition:
$$I = \int_0^1 \frac{2x^2 + 3}{(x+1)(x^2 + 1)} \, dx$$""",
        "solution": r"""<h4>Step 1: Partial Fraction Decomposition Template</h4>
<p>Decompose the proper rational integrand into linear and quadratic denominators:</p>
<div class="math-display">
$$\frac{2x^2 + 3}{(x+1)(x^2 + 1)} = \frac{A}{x+1} + \frac{Bx + C}{x^2 + 1}$$
</div>

<h4>Step 2: Determine Coefficients</h4>
<p>Multiply through by the common denominator $(x+1)(x^2 + 1)$:</p>
<div class="math-display">
$$2x^2 + 3 = A(x^2 + 1) + (Bx + C)(x + 1) = (A + B)x^2 + (B + C)x + (A + C)$$
</div>
<p>Using Heaviside's method at $x = -1$:</p>
<div class="math-display">
$$2(-1)^2 + 3 = A((-1)^2 + 1) + 0 \implies 5 = 2A \implies A = \frac{5}{2}$$
</div>
<p>Equating coefficients of $x^2$ and the constant term:</p>
<div class="math-display">
$$A + B = 2 \implies B = 2 - \frac{5}{2} = -\frac{1}{2}$$
</div>
<div class="math-display">
$$A + C = 3 \implies C = 3 - \frac{5}{2} = \frac{1}{2}$$
</div>

<h4>Step 3: Integrate Term by Term</h4>
<div class="math-display">
$$\int_0^1 \left( \frac{5/2}{x+1} - \frac{1}{2}\frac{x}{x^2+1} + \frac{1}{2}\frac{1}{x^2+1} \right) dx$$
</div>
<div class="math-display">
$$\begin{aligned}
I &= \left[ \frac{5}{2}\ln|x+1| - \frac{1}{4}\ln(x^2+1) + \frac{1}{2}\arctan(x) \right]_0^1 \\
&= \left( \frac{5}{2}\ln(2) - \frac{1}{4}\ln(2) + \frac{1}{2}\arctan(1) \right) - \left( 0 - 0 + 0 \right) \\
&= \frac{9}{4}\ln(2) + \frac{1}{2}\left(\frac{\pi}{4}\right) = \frac{9}{4}\ln(2) + \frac{\pi}{8}
\end{aligned}$$
</div>""",
        "answer": r"""$I = \frac{9}{4}\ln(2) + \frac{\pi}{8}$"""
    },
    {
        "id": "calc2-p1-3",
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Wallis Asymptotics & Gaussian Integral Connection",
        "statement": r"""Consider the integral $I_n = \int_0^1 (1 - x^2)^n \, dx$ for $n \in \mathbb{N}$.
(a) Establish a reduction formula connecting $I_n$ to $I_{n-1}$.
(b) Evaluate $I_n$ in terms of the double factorial.
(c) Prove that $\lim_{n \to \infty} \sqrt{n} \, I_n = \frac{\sqrt{\pi}}{2}$, establishing the link to the Gaussian integral $\int_{-\infty}^\infty e^{-t^2} dt = \sqrt{\pi}$.""",
        "solution": r"""<h4>Part (a): Reduction via Integration by Parts</h4>
<p>Set $u = (1 - x^2)^n$ and $dv = dx \implies v = x$. Then $du = -2nx(1-x^2)^{n-1}\,dx$:</p>
<div class="math-display">
$$I_n = \Big[ x(1 - x^2)^n \Big]_0^1 - \int_0^1 x \Big( -2nx(1 - x^2)^{n-1} \Big) dx = 0 + 2n \int_0^1 x^2 (1 - x^2)^{n-1} \, dx$$
</div>
<p>Rewrite $x^2 = 1 - (1 - x^2)$:</p>
<div class="math-display">
$$I_n = 2n \int_0^1 (1 - x^2)^{n-1} \, dx - 2n \int_0^1 (1 - x^2)^n \, dx = 2n I_{n-1} - 2n I_n$$
</div>
<div class="math-display">
$$(2n + 1) I_n = 2n I_{n-1} \implies \mathbf{I_n = \frac{2n}{2n + 1} I_{n-1}}$$
</div>

<h4>Part (b): Closed-Form Evaluation</h4>
<p>Since $I_0 = \int_0^1 1 \, dx = 1$, unwinding the recurrence gives:</p>
<div class="math-display">
$$I_n = \frac{2n}{2n+1} \cdot \frac{2n-2}{2n-1} \cdots \frac{2}{3} \cdot 1 = \frac{(2n)!!}{(2n+1)!!}$$
</div>
<p>Notice that this is identically equal to the odd Wallis integral $W_{2n+1} = \int_0^{\pi/2} \sin^{2n+1}(\theta) \, d\theta$ under the substitution $x = \cos(\theta)$.</p>

<h4>Part (c): Asymptotic Limit and Gaussian Connection</h4>
<p>By the Wallis ratio theorem derived in Section 1.5, $\lim_{n \to \infty} \frac{W_{2n}}{W_{2n+1}} = 1$. Furthermore, the product identity implies:</p>
<div class="math-display">
$$W_{2n} \cdot W_{2n+1} = \frac{(2n-1)!!}{(2n)!!}\frac{\pi}{2} \cdot \frac{(2n)!!}{(2n+1)!!} = \frac{\pi}{2(2n+1)}$$
</div>
<p>Since $W_{2n} \sim W_{2n+1} = I_n$ as $n \to \infty$:</p>
<div class="math-display">
$$I_n^2 \sim \frac{\pi}{2(2n+1)} \sim \frac{\pi}{4n} \implies I_n \sim \frac{\sqrt{\pi}}{2\sqrt{n}}$$
</div>
<div class="math-display">
$$\mathbf{\lim_{n \to \infty} \sqrt{n} \, I_n = \frac{\sqrt{\pi}}{2}}$$
</div>
<p>Under the substitution $x = \frac{t}{\sqrt{n}}$, $(1 - x^2)^n = \left(1 - \frac{t^2}{n}\right)^n \to e^{-t^2}$, recovering the Gaussian integral $\int_0^\infty e^{-t^2} dt = \frac{\sqrt{\pi}}{2}$.</p>""",
        "answer": r"""$\lim_{n \to \infty} \sqrt{n} I_n = \frac{\sqrt{\pi}}{2}$"""
    }
]

u1_data = {
    "id": "unit1",
    "unit_number": 1,
    "title": "Advanced Techniques of Integration & Reduction Formulas",
    "subtitle": "Integration by Parts, Partial Fractions, Weierstrass Substitution & Wallis Products",
    "sections": u1_sections,
    "simulations": ["sim_calc2_reduction"],
    "problems": u1_problems
}


# ==========================================
# UNIT 2: RIEMANN SUMS & FUNDAMENTAL THEOREMS
# ==========================================
u2_sections = [
    {
        "id": "u2-sec1",
        "title": "Partitions, Darboux Sums & The Rigorous Riemann Integral",
        "content": r"""<h4>1. Partitions and Mesh Size</h4>
<p>Let $[a, b] \subset \mathbb{R}$ be a compact interval. A <strong>partition</strong> $\mathcal{P}$ of $[a, b]$ is a finite ordered sequence of points:</p>
<div class="math-display">
$$\mathcal{P} = \{ a = x_0 < x_1 < x_2 < \dots < x_{n-1} < x_n = b \}$$
</div>
<p>The $k$-th subinterval is $\Delta x_k = x_k - x_{k-1}$. The <strong>mesh</strong> (or norm) of $\mathcal{P}$ is the maximal subinterval width:</p>
<div class="math-display">
$$\|\mathcal{P}\| = \max_{1 \le k \le n} \Delta x_k$$
</div>

<h4>2. Darboux Upper and Lower Sums</h4>
<p>For a bounded function $f: [a, b] \to \mathbb{R}$, define the infimum and supremum on each subinterval $[x_{k-1}, x_k]$:</p>
<div class="math-display">
$$m_k = \inf_{x \in [x_{k-1}, x_k]} f(x), \qquad M_k = \sup_{x \in [x_{k-1}, x_k]} f(x)$$
</div>
<p>The <strong>Lower Darboux Sum</strong> $L(f, \mathcal{P})$ and <strong>Upper Darboux Sum</strong> $U(f, \mathcal{P})$ are:</p>
<div class="math-display">
$$L(f, \mathcal{P}) = \sum_{k=1}^n m_k \Delta x_k, \qquad U(f, \mathcal{P}) = \sum_{k=1}^n M_k \Delta x_k$$
</div>
<p>For any partition $\mathcal{P}$, $L(f, \mathcal{P}) \le U(f, \mathcal{P})$. Furthermore, if $\mathcal{P}^*$ is a <em>refinement</em> of $\mathcal{P}$ ($\mathcal{P} \subseteq \mathcal{P}^*$), adding partition points only increases lower sums and decreases upper sums:</p>
<div class="math-display">
$$L(f, \mathcal{P}) \le L(f, \mathcal{P}^*) \le U(f, \mathcal{P}^*) \le U(f, \mathcal{P})$$
</div>

<h4>3. The Riemann Integrability Criterion</h4>
<p>Define the Lower and Upper Darboux Integrals over all possible partitions $\mathscr{P}$ of $[a, b]$:</p>
<div class="math-display">
$$\underline{\int_a^b} f(x) \, dx = \sup_{\mathcal{P} \in \mathscr{P}} L(f, \mathcal{P}), \qquad \overline{\int_a^b} f(x) \, dx = \inf_{\mathcal{P} \in \mathscr{P}} U(f, \mathcal{P})$$
</div>
<div class="math-display">
$$\mathbf{\text{Riemann Integrability: } f \text{ is Riemann integrable on } [a, b] \iff \underline{\int_a^b} f(x) \, dx = \overline{\int_a^b} f(x) \, dx = \int_a^b f(x) \, dx}$$
</div>
<p><strong>Cauchy-Riemann $\varepsilon$-Criterion:</strong> A bounded function $f$ is Riemann integrable on $[a, b]$ if and only if for every $\varepsilon > 0$, there exists a partition $\mathcal{P}_\varepsilon$ such that:</p>
<div class="math-display">
$$U(f, \mathcal{P}_\varepsilon) - L(f, \mathcal{P}_\varepsilon) = \sum_{k=1}^n (M_k - m_k) \Delta x_k < \varepsilon$$
</div>
<p><strong>Theorem:</strong> Every continuous function $f \in C([a, b])$ is Riemann integrable (by Heine-Cantor Uniform Continuity on compact intervals).</p>"""
    },
    {
        "id": "u2-sec2",
        "title": "Riemann Sum Approximations: Left, Right, Midpoint & Trapezoidal Rules",
        "content": r"""<h4>1. Tagged Partitions and General Riemann Sums</h4>
<p>Choosing an arbitrary evaluation tag $c_k \in [x_{k-1}, x_k]$ inside each subinterval yields the general Riemann sum:</p>
<div class="math-display">
$$S(f, \mathcal{P}, \{c_k\}) = \sum_{k=1}^n f(c_k) \Delta x_k$$
</div>
<p>The definite integral is the strict analytical limit as mesh size vanishes:</p>
<div class="math-display">
$$\int_a^b f(x) \, dx = \lim_{\|\mathcal{P}\| \to 0} \sum_{k=1}^n f(c_k) \Delta x_k$$
</div>

<h4>2. Standard Uniform Partitions ($\Delta x = \frac{b - a}{n}$)</h4>
<p>Dividing $[a, b]$ into $n$ equal subintervals with $x_k = a + k \Delta x$ generates classical numerical rules:</p>
<ul>
  <li><strong>Left Riemann Sum:</strong> $c_k = x_{k-1} \implies L_n = \sum_{k=1}^n f(x_{k-1}) \Delta x$</li>
  <li><strong>Right Riemann Sum:</strong> $c_k = x_k \implies R_n = \sum_{k=1}^n f(x_k) \Delta x$</li>
  <li><strong>Midpoint Rule:</strong> $c_k = \frac{x_{k-1} + x_k}{2} \implies M_n = \sum_{k=1}^n f\left(x_{k-1/2}\right) \Delta x$</li>
  <li><strong>Trapezoidal Rule:</strong> The average of Left and Right sums:
    $$T_n = \frac{L_n + R_n}{2} = \frac{\Delta x}{2} \left[ f(x_0) + 2f(x_1) + 2f(x_2) + \dots + 2f(x_{n-1}) + f(x_n) \right]$$
  </li>
</ul>

<h4>3. Asymptotic Error Order</h4>
<p>Using Taylor expansions, the truncation error $E(f) = \int_a^b f(x)dx - \text{Approximation}$ scales as:</p>
<div class="math-display">
$$|E_{\text{Left}}| \le \frac{(b-a)^2}{2n} M_1, \qquad |E_{\text{Midpoint}}| \le \frac{(b-a)^3}{24n^2} M_2, \qquad |E_{\text{Trap}}| \le \frac{(b-a)^3}{12n^2} M_2$$
</div>
<p>where $M_1 = \max |f'(x)|$ and $M_2 = \max |f''(x)|$. The Midpoint and Trapezoidal rules achieve second-order convergence $\mathcal{O}(1/n^2)$.</p>"""
    },
    {
        "id": "u2-sec3",
        "title": "Fundamental Properties of Definite Integrals & The Integral Mean Value Theorem",
        "content": r"""<h4>1. Algebraic and Order Properties</h4>
<p>For Riemann integrable functions $f, g$ and scalars $\alpha, \beta \in \mathbb{R}$:</p>
<ol>
  <li><strong>Linearity:</strong> $\int_a^b (\alpha f(x) + \beta g(x)) \, dx = \alpha \int_a^b f(x) \, dx + \beta \int_a^b g(x) \, dx$</li>
  <li><strong>Subinterval Additivity:</strong> For any $c \in (a, b)$, $\int_a^b f(x) \, dx = \int_a^c f(x) \, dx + \int_c^b f(x) \, dx$</li>
  <li><strong>Monotonicity:</strong> If $f(x) \le g(x)$ for all $x \in [a, b]$, then $\int_a^b f(x) \, dx \le \int_a^b g(x) \, dx$</li>
  <li><strong>Integral Triangle Inequality:</strong>
    $$\left| \int_a^b f(x) \, dx \right| \le \int_a^b |f(x)| \, dx$$
  </li>
</ol>

<h4>2. The Cauchy-Schwarz Inequality for Integrals</h4>
<p>For any two real square-integrable functions $f, g \in L^2([a, b])$:</p>
<div class="math-display">
$$\left( \int_a^b f(x) g(x) \, dx \right)^2 \le \left( \int_a^b f(x)^2 \, dx \right) \left( \int_a^b g(x)^2 \, dx \right)$$
</div>
<p><strong>Proof:</strong> Consider the quadratic polynomial in $\lambda \in \mathbb{R}$: $P(\lambda) = \int_a^b (\lambda f(x) + g(x))^2 \, dx \ge 0$. Expanding $P(\lambda) = A \lambda^2 + 2B \lambda + C \ge 0$, the discriminant $\Delta = 4(B^2 - AC) \le 0 \implies B^2 \le AC$.</p>

<h4>3. The Mean Value Theorem for Definite Integrals</h4>
<div class="math-display">
$$\mathbf{\text{Theorem: If } f: [a, b] \to \mathbb{R} \text{ is continuous, there exists at least one } c \in (a, b) \text{ such that:}}$$
</div>
<div class="math-display">
$$f(c) = \frac{1}{b - a} \int_a^b f(x) \, dx$$
</div>
<p><strong>Proof:</strong> By the Extreme Value Theorem, $f$ attains minimum $m$ and maximum $M$ on $[a, b]$. Integrating $m \le f(x) \le M$ gives $m(b - a) \le \int_a^b f(x) \, dx \le M(b - a) \implies m \le \frac{1}{b-a}\int_a^b f(x)\,dx \le M$. By Bolzano's Intermediate Value Theorem, $f$ must attain this average value at some point $c \in (a, b)$.</p>"""
    },
    {
        "id": "u2-sec4",
        "title": "The Fundamental Theorems of Calculus (FTC 1 & 2): Line-by-Line Proofs",
        "content": r"""<h4>1. The First Fundamental Theorem of Calculus (FTC-1: Differentiation of Accumulation)</h4>
<div class="math-display">
$$\mathbf{\text{Theorem (FTC-1): Let } f: [a, b] \to \mathbb{R} \text{ be continuous. Define the accumulation function } F(x) = \int_a^x f(t) \, dt. \text{ Then } F \text{ is differentiable on } (a, b) \text{ and } F'(x) = f(x).}$$
</div>
<p><strong>Rigorous Proof:</strong> Form the Newton difference quotient for $h \ne 0$:</p>
<div class="math-display">
$$\frac{F(x + h) - F(x)}{h} = \frac{1}{h} \left( \int_a^{x+h} f(t) \, dt - \int_a^x f(t) \, dt \right) = \frac{1}{h} \int_x^{x+h} f(t) \, dt$$
</div>
<p>Subtract $f(x) = \frac{1}{h} \int_x^{x+h} f(x) \, dt$ from both sides:</p>
<div class="math-display">
$$\left| \frac{F(x + h) - F(x)}{h} - f(x) \right| = \left| \frac{1}{h} \int_x^{x+h} \Big( f(t) - f(x) \Big) dt \right| \le \frac{1}{|h|} \left| \int_x^{x+h} |f(t) - f(x)| dt \right|$$
</div>
<p>Since $f$ is continuous at $x$, for any $\varepsilon > 0$ there exists $\delta > 0$ such that $|t - x| < \delta \implies |f(t) - f(x)| < \varepsilon$. When $0 < |h| < \delta$, every $t$ in the integration interval satisfies $|t - x| \le |h| < \delta$. Therefore:</p>
<div class="math-display">
$$\left| \frac{F(x + h) - F(x)}{h} - f(x) \right| < \frac{1}{|h|} \int_{\min(x, x+h)}^{\max(x, x+h)} \varepsilon \, dt = \frac{1}{|h|} \cdot \varepsilon |h| = \varepsilon$$
</div>
<p>Taking the limit as $h \to 0$ proves that $F'(x) = \lim_{h \to 0} \frac{F(x+h) - F(x)}{h} = f(x)$. $\blacksquare$</p>

<h4>2. The Second Fundamental Theorem of Calculus (FTC-2: Evaluation Theorem)</h4>
<div class="math-display">
$$\mathbf{\text{Theorem (FTC-2): If } f \in C([a, b]) \text{ and } G \text{ is ANY antiderivative of } f \text{ (i.e. } G'(x) = f(x)\text{), then:}}$$
</div>
<div class="math-display">
$$\int_a^b f(x) \, dx = G(b) - G(a)$$
</div>
<p><strong>Proof:</strong> From FTC-1, $F(x) = \int_a^x f(t)\,dt$ is an antiderivative of $f$. Since any two antiderivatives differ by a constant on a connected interval, $G(x) = F(x) + C$ for some $C \in \mathbb{R}$.</p>
<p>Evaluating at $x = a$: $G(a) = F(a) + C = \int_a^a f(t)\,dt + C = 0 + C = C$.</p>
<p>Evaluating at $x = b$: $G(b) = F(b) + C = \int_a^b f(t)\,dt + G(a)$.</p>
<p>Subtracting $G(a)$ from both sides establishes: $\int_a^b f(t)\,dt = G(b) - G(a)$. $\blacksquare$</p>"""
    },
    {
        "id": "u2-sec5",
        "title": "The Leibniz Integral Rule: Differentiation Under the Integral Sign",
        "content": r"""<h4>1. Variable Limits and Parameter-Dependent Integrals</h4>
<p>Let $f(x, t)$ and its partial derivative $\frac{\partial f}{\partial x}$ be continuous in both variables, and let $u(x), v(x)$ be continuously differentiable functions. Consider the accumulation integral:</p>
<div class="math-display">
$$I(x) = \int_{u(x)}^{v(x)} f(x, t) \, dt$$
</div>

<h4>2. The Full Leibniz Integral Formula</h4>
<div class="math-display">
$$\mathbf{\frac{d}{dx} \left[ \int_{u(x)}^{v(x)} f(x, t) \, dt \right] = f(x, v(x)) \cdot v'(x) - f(x, u(x)) \cdot u'(x) + \int_{u(x)}^{v(x)} \frac{\partial f}{\partial x}(x, t) \, dt}$$
</div>

<h4>3. Analytical Derivation via Multi-Variable Chain Rule</h4>
<p>Define $H(x, u, v) = \int_u^v f(x, t) \, dt$. The total derivative of $I(x) = H(x, u(x), v(x))$ with respect to $x$ is:</p>
<div class="math-display">
$$\frac{dI}{dx} = \frac{\partial H}{\partial x} + \frac{\partial H}{\partial u} \frac{du}{dx} + \frac{\partial H}{\partial v} \frac{dv}{dx}$$
</div>
<p>By FTC-1:</p>
<div class="math-display">
$$\frac{\partial H}{\partial v} = \frac{\partial}{\partial v}\int_u^v f(x, t) dt = f(x, v)$$
</div>
<div class="math-display">
$$\frac{\partial H}{\partial u} = \frac{\partial}{\partial u}\left( -\int_v^u f(x, t) dt \right) = -f(x, u)$$
</div>
<p>Differentiating the integral with respect to parameter $x$ inside the constant limits $[u, v]$ allows passing the derivative under the integral sign: $\frac{\partial H}{\partial x} = \int_u^v \frac{\partial f}{\partial x}(x, t) dt$. Summing these three terms recovers the Leibniz rule.</p>"""
    }
]

u2_problems = [
    {
        "id": "calc2-p2-1",
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Limit of a Riemann Sum via Definite Integration",
        "statement": r"""Evaluate the limit of the sequence by expressing it as a definite Riemann integral:
$$L = \lim_{n \to \infty} \sum_{k=1}^n \frac{k^3}{n^4 + k^4}$$""",
        "solution": r"""<h4>Step 1: Normalize into a Standard Riemann Sum Form</h4>
<p>To convert $\lim_{n \to \infty} \sum_{k=1}^n f(k/n) \frac{1}{n}$ into $\int_0^1 f(x) \, dx$, factor $n^4$ from the denominator:</p>
<div class="math-display">
$$\frac{k^3}{n^4 + k^4} = \frac{k^3}{n^4 \left( 1 + \frac{k^4}{n^4} \right)} = \frac{1}{n} \cdot \frac{(k/n)^3}{1 + (k/n)^4}$$
</div>

<h4>Step 2: Recognize the Riemann Sum Components</h4>
<p>With $\Delta x = \frac{1}{n}$ and evaluation points $x_k = \frac{k}{n} \in [0, 1]$:</p>
<div class="math-display">
$$L = \lim_{n \to \infty} \sum_{k=1}^n \frac{(x_k)^3}{1 + (x_k)^4} \Delta x = \int_0^1 \frac{x^3}{1 + x^4} \, dx$$
</div>

<h4>Step 3: Evaluate the Definite Integral</h4>
<p>Substitute $u = 1 + x^4 \implies du = 4x^3 \, dx \implies x^3 \, dx = \frac{1}{4} du$.</p>
<p>Limits: when $x = 0$, $u = 1$; when $x = 1$, $u = 2$.</p>
<div class="math-display">
$$L = \int_1^2 \frac{1/4}{u} \, du = \frac{1}{4} \Big[ \ln|u| \Big]_1^2 = \frac{1}{4} \Big( \ln(2) - \ln(1) \Big) = \frac{\ln(2)}{4}$$
</div>""",
        "answer": r"""$L = \frac{\ln(2)}{4}$"""
    },
    {
        "id": "calc2-p2-2",
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Leibniz Integral Rule with Variable Limits",
        "statement": r"""Compute the derivative $F'(x)$ for $x > 0$ where:
$$F(x) = \int_{x}^{x^2} \frac{\cos(xt)}{t} \, dt$$""",
        "solution": r"""<h4>Step 1: Identify Leibniz Rule Components</h4>
<p>For $F(x) = \int_{u(x)}^{v(x)} f(x, t) \, dt$ with $u(x) = x$, $v(x) = x^2$, and $f(x, t) = \frac{\cos(xt)}{t}$:</p>
<div class="math-display">
$$u'(x) = 1, \qquad v'(x) = 2x$$
</div>
<p>The partial derivative with respect to parameter $x$ is:</p>
<div class="math-display">
$$\frac{\partial f}{\partial x} = \frac{\partial}{\partial x} \left( \frac{\cos(xt)}{t} \right) = \frac{-t \sin(xt)}{t} = -\sin(xt)$$
</div>

<h4>Step 2: Apply the Leibniz Formula</h4>
<div class="math-display">
$$F'(x) = f(x, v(x)) \cdot v'(x) - f(x, u(x)) \cdot u'(x) + \int_{u(x)}^{v(x)} \frac{\partial f}{\partial x} \, dt$$
</div>
<div class="math-display">
$$F'(x) = \left( \frac{\cos(x \cdot x^2)}{x^2} \right) (2x) - \left( \frac{\cos(x \cdot x)}{x} \right) (1) + \int_x^{x^2} (-\sin(xt)) \, dt$$
</div>

<h4>Step 3: Evaluate the Boundary Terms and the Residual Integral</h4>
<p>Boundary terms:</p>
<div class="math-display">
$$\frac{2x \cos(x^3)}{x^2} - \frac{\cos(x^2)}{x} = \frac{2\cos(x^3) - \cos(x^2)}{x}$$
</div>
<p>Residual integral with respect to $t$:</p>
<div class="math-display">
$$\int_x^{x^2} (-\sin(xt)) \, dt = \left[ \frac{\cos(xt)}{x} \right]_x^{x^2} = \frac{\cos(x^3) - \cos(x^2)}{x}$$
</div>

<h4>Step 4: Combine All Terms</h4>
<div class="math-display">
$$F'(x) = \frac{2\cos(x^3) - \cos(x^2)}{x} + \frac{\cos(x^3) - \cos(x^2)}{x} = \frac{3\cos(x^3) - 2\cos(x^2)}{x}$$
</div>""",
        "answer": r"""$F'(x) = \frac{3\cos(x^3) - 2\cos(x^2)}{x}$"""
    },
    {
        "id": "calc2-p2-3",
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Strict Integrability of Composition & Triangle Inequality",
        "statement": r"""Let $f: [a, b] \to \mathbb{R}$ be bounded and Riemann integrable.
(a) Prove that the absolute value function $|f|: [a, b] \to \mathbb{R}$ is also Riemann integrable.
(b) Prove the integral triangle inequality:
$$\left| \int_a^b f(x) \, dx \right| \le \int_a^b |f(x)| \, dx$$
(c) Provide a counterexample showing that the converse of (a) is generally false.""",
        "solution": r"""<h4>Part (a): Proof of Integrability of $|f|$</h4>
<p>Let $\mathcal{P} = \{x_0, x_1, \dots, x_n\}$ be any partition of $[a, b]$. For any subinterval $[x_{k-1}, x_k]$, define:</p>
<div class="math-display">
$$M_k = \sup_{x \in I_k} f(x), \quad m_k = \inf_{x \in I_k} f(x), \quad M_k^* = \sup_{x \in I_k} |f(x)|, \quad m_k^* = \inf_{x \in I_k} |f(x)|$$
</div>
<p>For any two points $x, y \in I_k$, the reverse triangle inequality states:</p>
<div class="math-display">
$$||f(x)| - |f(y)|| \le |f(x) - f(y)| \le M_k - m_k$$
</div>
<p>Taking the supremum over all $x, y \in I_k$ yields the key oscillation inequality:</p>
<div class="math-display">
$$M_k^* - m_k^* \le M_k - m_k$$
</div>
<p>Multiplying by $\Delta x_k$ and summing over $k = 1, \dots, n$:</p>
<div class="math-display">
$$U(|f|, \mathcal{P}) - L(|f|, \mathcal{P}) = \sum_{k=1}^n (M_k^* - m_k^*) \Delta x_k \le \sum_{k=1}^n (M_k - m_k) \Delta x_k = U(f, \mathcal{P}) - L(f, \mathcal{P})$$
</div>
<p>Since $f$ is Riemann integrable, for any $\varepsilon > 0$ there exists a partition $\mathcal{P}_\varepsilon$ such that $U(f, \mathcal{P}_\varepsilon) - L(f, \mathcal{P}_\varepsilon) < \varepsilon$. Thus $U(|f|, \mathcal{P}_\varepsilon) - L(|f|, \mathcal{P}_\varepsilon) < \varepsilon$, establishing that $|f|$ is Riemann integrable by the Cauchy criterion. $\blacksquare$</p>

<h4>Part (b): Proof of the Integral Triangle Inequality</h4>
<p>For all $x \in [a, b]$, the definitions of absolute value imply:</p>
<div class="math-display">
$$-|f(x)| \le f(x) \le |f(x)|$$
</div>
<p>By the monotonicity property of the Riemann integral:</p>
<div class="math-display">
$$-\int_a^b |f(x)| \, dx \le \int_a^b f(x) \, dx \le \int_a^b |f(x)| \, dx$$
</div>
<p>This is equivalent to the statement:</p>
<div class="math-display">
$$\mathbf{\left| \int_a^b f(x) \, dx \right| \le \int_a^b |f(x)| \, dx} \quad \blacksquare$$
</div>

<h4>Part (c): Counterexample to the Converse</h4>
<p>Consider Dirichlet's Modified Function on $[0, 1]$:</p>
<div class="math-display">
$$f(x) = \begin{cases} 1 & \text{if } x \in \mathbb{Q} \cap [0, 1] \\ -1 & \text{if } x \in (\mathbb{R} \setminus \mathbb{Q}) \cap [0, 1] \end{cases}$$
</div>
<p>Then $|f(x)| = 1$ for all $x \in [0, 1]$, which is a constant function and trivially Riemann integrable with $\int_0^1 |f(x)|dx = 1$.</p>
<p>However, for any partition $\mathcal{P}$ of $[0, 1]$, every subinterval contains both rationals and irrationals, so $M_k = 1$ and $m_k = -1$. Hence $U(f, \mathcal{P}) = 1$ and $L(f, \mathcal{P}) = -1$. Since $U \ne L$, $f(x)$ is NOT Riemann integrable. This proves the converse does not hold.</p>""",
        "answer": r"""$|f|$ is Riemann integrable and satisfies $|\int f| \le \int |f|$; converse is refuted by the modified Dirichlet function."""
    }
]

u2_data = {
    "id": "unit2",
    "unit_number": 2,
    "title": "Riemann Sums, Definite Integrals & Fundamental Theorems",
    "subtitle": "Darboux Partitions, Integrability Criteria, FTC 1 & 2 Proofs, and Leibniz Rule",
    "sections": u2_sections,
    "simulations": ["sim_calc2_riemann"],
    "problems": u2_problems
}

# Write files
with open("calc2_u1.json", "w", encoding="utf-8") as f:
    json.dump(u1_data, f, indent=2, ensure_ascii=False)
print("Saved calc2_u1.json successfully.")

with open("calc2_u2.json", "w", encoding="utf-8") as f:
    json.dump(u2_data, f, indent=2, ensure_ascii=False)
print("Saved calc2_u2.json successfully.")
