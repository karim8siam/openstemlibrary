import json

print("Building Calculus II: Units 7 & 8...")

# ==========================================
# UNIT 7: INFINITE SERIES & POWER SERIES
# ==========================================
u7_sections = [
    {
        "id": "u7-sec1",
        "title": "Infinite Sequences, Series & The Cauchy Convergence Criterion",
        "content": r"""<h4>1. Sequences and the Sequence of Partial Sums</h4>
<p>An infinite sequence is an ordered map $a: \mathbb{N} \to \mathbb{R}$, denoted $(a_n)_{n=1}^\infty$. An <strong>infinite series</strong> is the formal sum $\sum_{n=1}^\infty a_n$.</p>
<p>Its convergence is defined strictly as the limit of its sequence of <strong>partial sums</strong> $s_N = \sum_{n=1}^N a_n$:</p>
<div class="math-display">
$$\sum_{n=1}^\infty a_n = \lim_{N \to \infty} s_N = S \in \mathbb{R}$$
</div>
<p>If $\lim_{N \to \infty} s_N$ does not exist as a finite real number, the series <strong>diverges</strong>.</p>

<h4>2. The Necessary Divergence Test ($n$-th Term Test)</h4>
<div class="math-display">
$$\mathbf{\sum_{n=1}^\infty a_n \text{ converges} \implies \lim_{n \to \infty} a_n = 0}$$
</div>
<p><strong>Contrapositive:</strong> If $\lim_{n \to \infty} a_n \ne 0$ (or does not exist), the series $\sum a_n$ diverges. <em>Warning:</em> The converse is false; the Harmonic series $\sum_{n=1}^\infty \frac{1}{n}$ satisfies $\lim \frac{1}{n} = 0$ but diverges logarithmically.</p>

<h4>3. The Cauchy Criterion for Series</h4>
<div class="math-display">
$$\mathbf{\sum_{n=1}^\infty a_n \text{ converges} \iff \forall \varepsilon > 0, \exists N \in \mathbb{N} \text{ such that } \forall m > n \ge N: \left| \sum_{k=n+1}^m a_k \right| < \varepsilon}$$
</div>
<p>This characterization relies solely on the completeness of $\mathbb{R}$, eliminating the need to know the sum $S$ a priori.</p>"""
    },
    {
        "id": "u7-sec2",
        "title": "Convergence Tests for Non-Negative Series: Integral, Comparison, Ratio & Root",
        "content": r"""<h4>1. The Integral Test (Maclaurin-Cauchy)</h4>
<p>Let $f: [1, \infty) \to \mathbb{R}$ be continuous, positive, and monotonically decreasing such that $f(n) = a_n$. Then:</p>
<div class="math-display">
$$\sum_{n=1}^\infty a_n \text{ converges} \iff \int_1^\infty f(x) \, dx < \infty$$
</div>
<p><strong>Application to $p$-Series:</strong> $\sum_{n=1}^\infty \frac{1}{n^p}$ converges if and only if $p > 1$.</p>

<h4>2. Direct Comparison & Limit Comparison Tests</h4>
<ul>
  <li><strong>Direct:</strong> If $0 \le a_n \le b_n$, then $\sum b_n < \infty \implies \sum a_n < \infty$; and $\sum a_n = \infty \implies \sum b_n = \infty$.</li>
  <li><strong>Limit:</strong> If $a_n > 0, b_n > 0$ and $L = \lim_{n \to \infty} \frac{a_n}{b_n} \in (0, \infty)$, then $\sum a_n$ and $\sum b_n$ share the exact same convergence status.</li>
</ul>

<h4>3. d'Alembert's Ratio Test</h4>
<p>Let $L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|$:</p>
<ul>
  <li>If $L < 1$: The series converges absolutely.</li>
  <li>If $L > 1$: The series diverges.</li>
  <li>If $L = 1$: The test is inconclusive (requires Raabe's test or Integral test).</li>
</ul>

<h4>4. Cauchy's Root Test</h4>
<p>Let $L = \limsup_{n \to \infty} \sqrt[n]{|a_n|}$:</p>
<ul>
  <li>If $L < 1$: Converges absolutely.</li>
  <li>If $L > 1$: Diverges.</li>
  <li>If $L = 1$: Inconclusive.</li>
</ul>"""
    },
    {
        "id": "u7-sec3",
        "title": "Alternating Series, Absolute vs Conditional Convergence & Riemann Rearrangement",
        "content": r"""<h4>1. The Leibniz Alternating Series Test</h4>
<p>An alternating series $\sum_{n=1}^\infty (-1)^{n-1} b_n$ with $b_n > 0$ converges if:</p>
<ol>
  <li>$b_{n+1} \le b_n$ for all $n \ge N$ (monotonic decrease).</li>
  <li>$\lim_{n \to \infty} b_n = 0$.</li>
</ol>
<p><strong>Alternating Series Estimation Theorem:</strong> If $S$ is the sum, the truncation error $|R_N| = |S - s_N|$ satisfies:</p>
<div class="math-display">
$$|S - s_N| \le b_{N+1}$$
</div>
<p>The error is strictly bounded by the magnitude of the first neglected term.</p>

<h4>2. Absolute vs Conditional Convergence</h4>
<ul>
  <li><strong>Absolute Convergence:</strong> $\sum |a_n|$ converges. Every absolutely convergent series converges.</li>
  <li><strong>Conditional Convergence:</strong> $\sum a_n$ converges, but $\sum |a_n| = \infty$ (e.g. the alternating harmonic series $\sum \frac{(-1)^{n-1}}{n} = \ln 2$).</li>
</ul>

<h4>3. Riemann's Rearrangement Theorem</h4>
<p>If a series $\sum a_n$ is <em>conditionally convergent</em>, then for <strong>any</strong> real number $M \in \mathbb{R}$ (or $\pm\infty$), there exists a permutation $\sigma: \mathbb{N} \to \mathbb{N}$ of the series indices such that the rearranged series sums exactly to $M$:</p>
<div class="math-display">
$$\sum_{n=1}^\infty a_{\sigma(n)} = M$$
</div>
<p>In contrast, absolutely convergent series can be rearranged arbitrarily without altering their sum (Dirichlet's theorem).</p>"""
    },
    {
        "id": "u7-sec4",
        "title": "Power Series & The Cauchy-Hadamard Radius of Convergence",
        "content": r"""<h4>1. Definition of a Power Series</h4>
<p>A power series centered at $x_0 \in \mathbb{R}$ with real coefficients $(c_n)$ is:</p>
<div class="math-display">
$$f(x) = \sum_{n=0}^\infty c_n (x - x_0)^n = c_0 + c_1(x - x_0) + c_2(x - x_0)^2 + \dots$$
</div>

<h4>2. The Cauchy-Hadamard Theorem</h4>
<div class="math-display">
$$\mathbf{\text{Theorem: For any power series } \sum c_n (x - x_0)^n, \text{ there exists a unique } R \in [0, \infty] \text{ such that:}}$$
</div>
<ul>
  <li>The series converges absolutely for all $|x - x_0| < R$.</li>
  <li>The series diverges for all $|x - x_0| > R$.</li>
  <li>At the boundary points $x = x_0 \pm R$, the series may converge absolutely, converge conditionally, or diverge.</li>
</ul>
<p>The <strong>Radius of Convergence</strong> $R$ is determined by the Cauchy-Hadamard formula:</p>
<div class="math-display">
$$\mathbf{\frac{1}{R} = \limsup_{n \to \infty} \sqrt[n]{|c_n|} \quad \text{or} \quad R = \lim_{n \to \infty} \left| \frac{c_n}{c_{n+1}} \right|}$$
</div>
<p>The <strong>Interval of Convergence</strong> is one of $(x_0 - R, x_0 + R)$, $[x_0 - R, x_0 + R)$, $(x_0 - R, x_0 + R]$, or $[x_0 - R, x_0 + R]$.</p>"""
    },
    {
        "id": "u7-sec5",
        "title": "Term-by-Term Differentiation & Integration of Power Series",
        "content": r"""<h4>1. Uniform Convergence on Compact Subsets</h4>
<p>Within its open disk of convergence $|x - x_0| < R$, a power series converges uniformly on every compact subinterval $[x_0 - r, x_0 + r]$ ($r < R$). Consequently, $f(x)$ is infinitely differentiable ($C^\infty$) on $(x_0 - R, x_0 + R)$.</p>

<h4>2. Term-by-Term Differentiation Theorem</h4>
<p>The derivative of $f(x) = \sum_{n=0}^\infty c_n (x - x_0)^n$ is obtained by differentiating term by term:</p>
<div class="math-display">
$$\mathbf{f'(x) = \sum_{n=1}^\infty n c_n (x - x_0)^{n-1} = \sum_{k=0}^\infty (k+1) c_{k+1} (x - x_0)^k}$$
</div>
<p>The derivative series has the <strong>exact same radius of convergence $R$</strong>.</p>

<h4>3. Term-by-Term Integration Theorem</h4>
<p>The indefinite integral of $f(x)$ is obtained by integrating term by term:</p>
<div class="math-display">
$$\mathbf{\int f(x) \, dx = C + \sum_{n=0}^\infty \frac{c_n}{n+1} (x - x_0)^{n+1}}$$
</div>
<p>The integrated series also preserves the exact same radius of convergence $R$.</p>"""
    }
]

u7_problems = [
    {
        "id": "calc2-p7-1",
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Interval of Convergence with Boundary Endpoint Testing",
        "statement": r"""Find the radius and exact interval of convergence of the power series, testing both boundary endpoints:
$$\sum_{n=1}^\infty \frac{(-1)^n (x - 3)^n}{n \cdot 5^n}$$""",
        "solution": r"""<h4>Step 1: Compute the Radius of Convergence $R$ via the Ratio Test</h4>
<p>Let $u_n(x) = \frac{(-1)^n (x - 3)^n}{n \cdot 5^n}$. Compute the consecutive ratio:</p>
<div class="math-display">
$$\left| \frac{u_{n+1}(x)}{u_n(x)} \right| = \left| \frac{(x-3)^{n+1}}{(n+1) 5^{n+1}} \cdot \frac{n \cdot 5^n}{(x-3)^n} \right| = \frac{|x - 3|}{5} \cdot \frac{n}{n+1}$$
</div>
<p>Taking the limit as $n \to \infty$:</p>
<div class="math-display">
$$L = \lim_{n \to \infty} \left| \frac{u_{n+1}}{u_n} \right| = \frac{|x - 3|}{5} \lim_{n \to \infty} \frac{n}{n+1} = \frac{|x - 3|}{5}$$
</div>
<p>For absolute convergence, $L < 1 \implies \frac{|x - 3|}{5} < 1 \implies |x - 3| < 5$.</p>
<p>Thus, the <strong>Radius of Convergence is $R = 5$</strong>, and the open interval is $(-2, 8)$.</p>

<h4>Step 2: Test the Left Endpoint $x = -2$</h4>
<p>Substitute $x = -2 \implies x - 3 = -5$:</p>
<div class="math-display">
$$\sum_{n=1}^\infty \frac{(-1)^n (-5)^n}{n \cdot 5^n} = \sum_{n=1}^\infty \frac{(-1)^n (-1)^n 5^n}{n \cdot 5^n} = \sum_{n=1}^\infty \frac{1}{n}$$
</div>
<p>This is the standard Harmonic Series, which <strong>diverges</strong> ($p = 1$). Hence $x = -2$ is excluded.</p>

<h4>Step 3: Test the Right Endpoint $x = 8$</h4>
<p>Substitute $x = 8 \implies x - 3 = 5$:</p>
<div class="math-display">
$$\sum_{n=1}^\infty \frac{(-1)^n 5^n}{n \cdot 5^n} = \sum_{n=1}^\infty \frac{(-1)^n}{n}$$
</div>
<p>This is the Alternating Harmonic Series, which <strong>converges</strong> by the Leibniz test. Hence $x = 8$ is included.</p>

<h4>Conclusion</h4>
<div class="math-display">
$$\mathbf{R = 5, \qquad \text{Interval of Convergence: } (-2, 8]}$$
</div>""",
        "answer": r"""$R = 5$; Interval of Convergence is $(-2, 8]$."""
    },
    {
        "id": "calc2-p7-2",
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Summation of Series via Term-by-Term Differentiation",
        "statement": r"""Evaluate the exact sum of the series using term-by-term differentiation of the geometric series:
$$S = \sum_{n=1}^\infty \frac{n}{2^n}$$""",
        "solution": r"""<h4>Step 1: Start with the Geometric Series</h4>
<p>For $|x| < 1$, the geometric series evaluates to:</p>
<div class="math-display">
$$\sum_{n=0}^\infty x^n = \frac{1}{1 - x}$$
</div>

<h4>Step 2: Differentiate Term-by-Term</h4>
<p>Differentiating both sides with respect to $x$:</p>
<div class="math-display">
$$\frac{d}{dx} \left( \sum_{n=0}^\infty x^n \right) = \sum_{n=1}^\infty n x^{n-1} = \frac{d}{dx} (1 - x)^{-1} = \frac{1}{(1 - x)^2}$$
</div>

<h4>Step 3: Multiply by $x$</h4>
<div class="math-display">
$$\sum_{n=1}^\infty n x^n = x \sum_{n=1}^\infty n x^{n-1} = \frac{x}{(1 - x)^2}$$
</div>

<h4>Step 4: Substitute $x = 1/2$</h4>
<p>Since $|1/2| < 1$, the substitution is valid:</p>
<div class="math-display">
$$S = \sum_{n=1}^\infty \frac{n}{2^n} = \sum_{n=1}^\infty n \left(\frac{1}{2}\right)^n = \frac{1/2}{\left(1 - \frac{1}{2}\right)^2} = \frac{1/2}{(1/2)^2} = \frac{1/2}{1/4} = \mathbf{2}$$
</div>""",
        "answer": r"""$S = 2$"""
    },
    {
        "id": "calc2-p7-3",
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Rigorous Proof of the Cauchy-Hadamard Theorem",
        "statement": r"""Let $\sum_{n=0}^\infty c_n x^n$ be a power series. Define $\rho = \limsup_{n \to \infty} \sqrt[n]{|c_n|}$ and $R = 1/\rho$ (with $R = \infty$ if $\rho = 0$, and $R = 0$ if $\rho = \infty$).
Prove that:
(a) The series converges absolutely for all $|x| < R$.
(b) The series diverges for all $|x| > R$.""",
        "solution": r"""<h4>Part (a): Proof of Absolute Convergence for $|x| < R$</h4>
<p>Assume $0 < \rho < \infty$ and let $|x| < R = 1/\rho$, so $|x|\rho < 1$. Choose $\varepsilon > 0$ small enough such that:</p>
<div class="math-display">
$$q = |x|(\rho + \varepsilon) < 1$$
</div>
<p>By the definition of the limit superior $\limsup \sqrt[n]{|c_n|} = \rho$, there exists an integer $N \in \mathbb{N}$ such that for all $n \ge N$:</p>
<div class="math-display">
$$\sqrt[n]{|c_n|} < \rho + \varepsilon \implies |c_n| < (\rho + \varepsilon)^n$$
</div>
<p>Multiplying by $|x|^n$:</p>
<div class="math-display">
$$|c_n x^n| = |c_n| |x|^n < \Big( |x|(\rho + \varepsilon) \Big)^n = q^n$$
</div>
<p>Since $q < 1$, the geometric series $\sum_{n=N}^\infty q^n$ converges. By the Direct Comparison Test, $\sum_{n=0}^\infty |c_n x^n|$ converges, establishing that $\sum c_n x^n$ converges absolutely for all $|x| < R$. $\blacksquare$</p>

<h4>Part (b): Proof of Divergence for $|x| > R$</h4>
<p>Assume $|x| > R = 1/\rho$, so $|x|\rho > 1$. Then $\rho > 1/|x|$.</p>
<p>By the definition of the limit superior, there exist infinitely many indices $n_k \in \mathbb{N}$ such that:</p>
<div class="math-display">
$$\sqrt[n_k]{|c_{n_k}|} > \frac{1}{|x|} \implies |c_{n_k}| > \left(\frac{1}{|x|}\right)^{n_k} \implies |c_{n_k} x^{n_k}| = |c_{n_k}| |x|^{n_k} > 1$$
</div>
<p>Thus, the sequence of terms $a_n = c_n x^n$ does NOT converge to zero as $n \to \infty$ ($\lim_{n \to \infty} c_n x^n \ne 0$).</p>
<p>By the $n$-th term divergence test, the series $\sum c_n x^n$ must diverge. $\blacksquare$</p>""",
        "answer": r"""Proved: $\sum c_n x^n$ converges absolutely for $|x| < R$ and diverges for $|x| > R$ where $1/R = \limsup \sqrt[n]{|c_n|}$."""
    }
]

u7_data = {
    "id": "unit7",
    "unit_number": 7,
    "title": "Infinite Series Convergence & Power Series",
    "subtitle": "D'Alembert Ratio Test, Cauchy Root Test, Cauchy-Hadamard Radius & Term-by-Term Calculus",
    "sections": u7_sections,
    "simulations": ["sim_calc2_power_series"],
    "problems": u7_problems
}


# ==========================================
# UNIT 8: TAYLOR POLYNOMIALS & APPLICATIONS
# ==========================================
u8_sections = [
    {
        "id": "u8-sec1",
        "title": "Taylor & Maclaurin Polynomials: Local Matching of Higher Derivatives",
        "content": r"""<h4>1. Motivation: Polynomial Interpolation of Differential Jets</h4>
<p>Let $f: I \to \mathbb{R}$ be $n$ times continuously differentiable on an open interval $I$ containing $x_0$. The <strong>$n$-th degree Taylor polynomial</strong> $P_n(x)$ centered at $x_0$ is the unique polynomial of degree at most $n$ whose derivatives at $x_0$ match those of $f$ up to order $n$:</p>
<div class="math-display">
$$P_n^{(k)}(x_0) = f^{(k)}(x_0) \quad \text{for all } k = 0, 1, 2, \dots, n$$
</div>
<div class="math-display">
$$\mathbf{P_n(x) = \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!} (x - x_0)^k = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2!}(x - x_0)^2 + \dots + \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n}$$
</div>
<p>When centered at $x_0 = 0$, $P_n(x)$ is specifically called the <strong>Maclaurin polynomial</strong>.</p>

<h4>2. Standard Maclaurin Expansions</h4>
<ul>
  <li>$e^x = \sum_{k=0}^\infty \frac{x^k}{k!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots \quad (R = \infty)$</li>
  <li>$\sin(x) = \sum_{k=0}^\infty \frac{(-1)^k x^{2k+1}}{(2k+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots \quad (R = \infty)$</li>
  <li>$\cos(x) = \sum_{k=0}^\infty \frac{(-1)^k x^{2k}}{(2k)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots \quad (R = \infty)$</li>
  <li>$\frac{1}{1 - x} = \sum_{k=0}^\infty x^k = 1 + x + x^2 + x^3 + \dots \quad (R = 1)$</li>
  <li>$\ln(1 + x) = \sum_{k=1}^\infty \frac{(-1)^{k-1} x^k}{k} = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots \quad (R = 1)$</li>
  <li>$(1 + x)^\alpha = \sum_{k=0}^\infty \binom{\alpha}{k} x^k = 1 + \alpha x + \frac{\alpha(\alpha-1)}{2!} x^2 + \dots \quad (R = 1)$</li>
</ul>"""
    },
    {
        "id": "u8-sec2",
        "title": "Taylor's Theorem with Remainder: Lagrange, Cauchy & Integral Forms",
        "content": r"""<h4>1. Statement of Taylor's Theorem</h4>
<p>Let $f \in C^{n+1}([a, b])$ with $x_0, x \in [a, b]$. Then $f(x) = P_n(x) + R_n(x)$, where $R_n(x)$ is the <strong>remainder</strong> (truncation error).</p>

<h4>2. Lagrange Form of the Remainder</h4>
<div class="math-display">
$$\mathbf{R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!} (x - x_0)^{n+1}}$$
</div>
<p>for some intermediate point $c$ strictly between $x_0$ and $x$. Notice that for $n = 0$, this is identically the Lagrange Mean Value Theorem $f(x) - f(x_0) = f'(c)(x - x_0)$.</p>

<h4>3. Integral Form of the Remainder</h4>
<p>Repeated integration by parts establishes:</p>
<div class="math-display">
$$\mathbf{R_n(x) = \frac{1}{n!} \int_{x_0}^x (x - t)^n f^{(n+1)}(t) \, dt}$$
</div>

<h4>4. The Lagrange Truncation Error Bound</h4>
<p>If $|f^{(n+1)}(t)| \le M$ for all $t$ between $x_0$ and $x$:</p>
<div class="math-display">
$$\mathbf{|R_n(x)| \le \frac{M}{(n+1)!} |x - x_0|^{n+1}}$$
</div>"""
    },
    {
        "id": "u8-sec3",
        "title": "High-Precision Numerical Computations & Error Estimation",
        "content": r"""<h4>1. Error Budgeting Principle</h4>
<p>To approximate $f(x)$ with error strictly less than a specified tolerance $\varepsilon > 0$, we find the smallest integer $n$ such that:</p>
<div class="math-display">
$$\frac{M}{(n+1)!} |x - x_0|^{n+1} < \varepsilon$$
</div>

<h4>2. High-Precision Approximation of $e$</h4>
<p>Expanding $e^x$ at $x_0 = 0$ for $x = 1$ with $M = \max_{c \in [0, 1]} e^c = e < 3$:</p>
<div class="math-display">
$$|R_n(1)| \le \frac{3}{(n+1)!}$$
</div>
<p>For $\varepsilon = 10^{-6}$, setting $\frac{3}{(n+1)!} < 10^{-6} \implies (n+1)! > 3 \times 10^6 \implies n = 9$ (since $10! = 3,628,800$). Thus, adding just 10 terms of $P_9(1)$ guarantees 6 decimal places of accuracy!</p>"""
    },
    {
        "id": "u8-sec4",
        "title": "Differentiation & Integration of Non-Elementary Series Functions",
        "content": r"""<h4>1. Integrating Non-Elementary Integrands</h4>
<p>Many foundational integrals in physics and probability (such as the error function $\operatorname{erf}(x) = \frac{2}{\sqrt{\pi}}\int_0^x e^{-t^2} dt$ and the sine integral $\operatorname{Si}(x) = \int_0^x \frac{\sin t}{t} dt$) have no closed-form elementary antiderivative. Taylor series integration resolves them completely.</p>
<p>Expanding $e^{-t^2} = \sum_{k=0}^\infty \frac{(-1)^k t^{2k}}{k!}$:</p>
<div class="math-display">
$$\int_0^x e^{-t^2} \, dt = \sum_{k=0}^\infty \frac{(-1)^k}{k!} \int_0^x t^{2k} \, dt = \sum_{k=0}^\infty \frac{(-1)^k x^{2k+1}}{k! (2k+1)} = x - \frac{x^3}{3} + \frac{x^5}{10} - \frac{x^7}{42} + \dots$$
</div>
<p>Because this is an alternating series, the truncation error after $N$ terms is bounded by the magnitude of the $(N+1)$-th term.</p>"""
    },
    {
        "id": "u8-sec5",
        "title": "Applied Taylor Models: Physics, Economics & Biological Systems",
        "content": r"""<h4>1. Physics: Relativistic Kinetic Energy Correction</h4>
<p>Einstein's relativistic total energy is $E = \gamma m c^2$ with $\gamma = (1 - v^2/c^2)^{-1/2}$. Expanding via the binomial Taylor series for $x = v^2/c^2 \ll 1$:</p>
<div class="math-display">
$$\gamma = 1 + \frac{1}{2}\left(\frac{v^2}{c^2}\right) + \frac{3}{8}\left(\frac{v^2}{c^2}\right)^2 + \mathcal{O}\left(\frac{v^6}{c^6}\right)$$
</div>
<p>The kinetic energy $K = E - mc^2 = (\gamma - 1)mc^2$ becomes:</p>
<div class="math-display">
$$\mathbf{K = \frac{1}{2} m v^2 + \frac{3}{8} \frac{m v^4}{c^2} + \mathcal{O}(v^6)}$$
</div>
<p>The leading Taylor term recovers Newtonian kinetic energy $\frac{1}{2}mv^2$, while the second term provides the leading relativistic correction!</p>

<h4>2. Economics: Arrow-Pratt Risk Aversion Measure</h4>
<p>Expanding an agent's expected utility $U(w + \tilde{z})$ around wealth $w$ reveals that risk premium is proportional to $-\frac{U''(w)}{U'(w)}$.</p>

<h4>3. Biology: Population Linearization</h4>
<p>Expanding the non-linear logistic growth equation $\frac{dN}{dt} = r N (1 - N/K)$ around the carrying capacity $K$ yields stable exponential decay of perturbations.</p>"""
    }
]

u8_problems = [
    {
        "id": "calc2-p8-1",
        "difficulty": "Easy",
        "difficultyLabel": "Tier 1: Foundational",
        "title": "Maclaurin Polynomial and Error Bound for $\\ln(1 + 2x)$",
        "statement": r"""(a) Find the 3rd-degree Maclaurin polynomial $P_3(x)$ for $f(x) = \ln(1 + 2x)$.
(b) Use the Lagrange remainder to bound the error $|f(x) - P_3(x)|$ on the interval $[0, 0.1]$.""",
        "solution": r"""<h4>Part (a): Compute Derivatives and Maclaurin Polynomial</h4>
<p>Evaluating derivatives at $x = 0$:</p>
<div class="math-display">
$$\begin{aligned}
f(x) &= \ln(1 + 2x) \implies f(0) = 0 \\
f'(x) &= 2(1 + 2x)^{-1} \implies f'(0) = 2 \\
f''(x) &= -4(1 + 2x)^{-2} \implies f''(0) = -4 \\
f'''(x) &= 16(1 + 2x)^{-3} \implies f'''(0) = 16
\end{aligned}$$
</div>
<p>The 3rd-degree Maclaurin polynomial is:</p>
<div class="math-display">
$$P_3(x) = 0 + 2x + \frac{-4}{2!} x^2 + \frac{16}{3!} x^3 = \mathbf{2x - 2x^2 + \frac{8}{3}x^3}$$
</div>

<h4>Part (b): Error Bound on $[0, 0.1]$</h4>
<p>The 4th derivative is $f^{(4)}(x) = -96(1 + 2x)^{-4}$.</p>
<p>On $[0, 0.1]$, $|f^{(4)}(x)|$ is maximized at $x = 0$ because the denominator is monotonically increasing:</p>
<div class="math-display">
$$M = \max_{c \in [0, 0.1]} |f^{(4)}(c)| = |f^{(4)}(0)| = 96$$
</div>
<p>By the Lagrange Remainder Bound:</p>
<div class="math-display">
$$|R_3(x)| \le \frac{M}{4!} |x|^4 \le \frac{96}{24} (0.1)^4 = 4 \times 10^{-4} = \mathbf{0.0004}$$
</div>""",
        "answer": r"""$P_3(x) = 2x - 2x^2 + \frac{8}{3}x^3$; error bound $|R_3(x)| \le 0.0004$ on $[0, 0.1]$."""
    },
    {
        "id": "calc2-p8-2",
        "difficulty": "Medium",
        "difficultyLabel": "Tier 2: Intermediate Exam",
        "title": "Numerical Integration of a Non-Elementary Integral",
        "statement": r"""Approximate the definite integral to within $10^{-5}$ accuracy using Maclaurin series expansion:
$$I = \int_0^{0.5} \frac{1 - \cos(x)}{x^2} \, dx$$""",
        "solution": r"""<h4>Step 1: Series Expansion of the Integrand</h4>
<p>Recall the Maclaurin expansion for $\cos(x)$:</p>
<div class="math-display">
$$\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots$$
</div>
<p>Therefore:</p>
<div class="math-display">
$$\frac{1 - \cos(x)}{x^2} = \frac{\frac{x^2}{2} - \frac{x^4}{24} + \frac{x^6}{720} - \dots}{x^2} = \frac{1}{2} - \frac{x^2}{24} + \frac{x^4}{720} - \frac{x^6}{40320} + \dots$$
</div>

<h4>Step 2: Term-by-Term Integration</h4>
<div class="math-display">
$$\begin{aligned}
I &= \int_0^{0.5} \left( \frac{1}{2} - \frac{x^2}{24} + \frac{x^4}{720} - \frac{x^6}{40320} + \dots \right) dx \\
&= \left[ \frac{x}{2} - \frac{x^3}{72} + \frac{x^5}{3600} - \frac{x^7}{282240} + \dots \right]_0^{0.5}
\end{aligned}$$
</div>

<h4>Step 3: Evaluate Terms at $x = 0.5$</h4>
<div class="math-display">
$$\text{Term 1: } \frac{0.5}{2} = 0.25$$
</div>
<div class="math-display">
$$\text{Term 2: } -\frac{(0.5)^3}{72} = -\frac{0.125}{72} \approx -0.00173611$$
</div>
<div class="math-display">
$$\text{Term 3: } \frac{(0.5)^5}{3600} = \frac{0.03125}{3600} \approx 0.00000868$$
</div>
<p>Since this is an alternating series whose terms decrease monotonically, the truncation error after Term 2 is bounded by Term 3:</p>
<div class="math-display">
$$|R_2| \le \text{Term 3} \approx 8.68 \times 10^{-6} < 10^{-5}$$
</div>
<p>Summing the first two terms:</p>
<div class="math-display">
$$I \approx 0.25 - 0.00173611 = \mathbf{0.248264}$$
</div>""",
        "answer": r"""$I \approx 0.24826$ (accurate to within $10^{-5}$)."""
    },
    {
        "id": "calc2-p8-3",
        "difficulty": "Hard",
        "difficultyLabel": "Tier 3: Honors / Proof Challenge",
        "title": "Relativistic Kinetic Energy and Quantum Perturbations",
        "statement": r"""Consider the relativistic energy-momentum dispersion relation for a particle of rest mass $m$:
$$E(p) = \sqrt{p^2 c^2 + m^2 c^4}$$
(a) Using the binomial Taylor series for $\sqrt{1 + u}$, expand $E(p)$ in powers of $p/(mc)$ for non-relativistic momenta $p \ll mc$.
(b) Identify the rest energy, Newtonian kinetic energy, and first relativistic correction.
(c) In relativistic quantum mechanics, this expansion generates the Dirac Hamiltonian fine structure Hamiltonian. Write down the perturbed Hamiltonian operator $H = H_0 + H_1$ in position representation with momentum operator $\hat{p} = -i\hbar\nabla$.""",
        "solution": r"""<h4>Part (a): Binomial Taylor Series Expansion</h4>
<p>Factor out the rest mass energy $m c^2$:</p>
<div class="math-display">
$$E(p) = mc^2 \sqrt{1 + \frac{p^2}{m^2 c^2}} = mc^2 \left( 1 + \frac{p^2}{m^2 c^2} \right)^{1/2}$$
</div>
<p>Let $u = \frac{p^2}{m^2 c^2} \ll 1$. Recall the binomial series for $(1 + u)^{1/2}$:</p>
<div class="math-display">
$$(1 + u)^{1/2} = 1 + \frac{1}{2}u - \frac{1}{8}u^2 + \frac{1}{16}u^3 - \dots$$
</div>
<p>Substituting $u = \frac{p^2}{m^2 c^2}$:</p>
<div class="math-display">
$$E(p) = mc^2 \left( 1 + \frac{1}{2}\frac{p^2}{m^2 c^2} - \frac{1}{8}\frac{p^4}{m^4 c^4} + \mathcal{O}(p^6) \right)$$
</div>
<div class="math-display">
$$\mathbf{E(p) = mc^2 + \frac{p^2}{2m} - \frac{p^4}{8m^3 c^2} + \mathcal{O}(p^6)}$$
</div>

<h4>Part (b): Identification of Energy Terms</h4>
<ol>
  <li><strong>Rest Energy:</strong> $E_0 = mc^2$</li>
  <li><strong>Classical Newtonian Kinetic Energy:</strong> $K_{\text{Newton}} = \frac{p^2}{2m} = \frac{1}{2}mv^2$</li>
  <li><strong>First Relativistic Correction:</strong> $\Delta E_{\text{rel}} = -\frac{p^4}{8m^3 c^2}$ (strictly negative, lowering the energy levels of high-velocity states).</li>
</ol>

<h4>Part (c): Quantum Mechanical Operator Representation</h4>
<p>Promoting momentum to the quantum operator $\hat{p} = -i\hbar\nabla$, the Laplacian gives $\hat{p}^2 = -\hbar^2 \nabla^2$ and $\hat{p}^4 = \hbar^4 \nabla^4$. Subtracting the constant rest energy $mc^2$:</p>
<div class="math-display">
$$\hat{H}_0 = -\frac{\hbar^2}{2m} \nabla^2 + V(r) \quad \text{(Standard Schrödinger Hamiltonian)}$$
</div>
<div class="math-display">
$$\mathbf{\hat{H}_1 = -\frac{\hat{p}^4}{8m^3 c^2} = -\frac{\hbar^4}{8m^3 c^2} \nabla^4} \quad \blacksquare$$
</div>
<p>This is precisely the relativistic mass-velocity fine-structure correction Hamiltonian in atomic spectroscopy.</p>""",
        "answer": r"""$E(p) = mc^2 + \frac{p^2}{2m} - \frac{p^4}{8m^3 c^2} + \dots$; in quantum mechanics, $\hat{H}_1 = -\frac{\hat{p}^4}{8m^3 c^2} = -\frac{\hbar^4}{8m^3 c^2}\nabla^4$."""
    }
]

u8_data = {
    "id": "unit8",
    "unit_number": 8,
    "title": "Taylor Polynomials, Remainder Theorems & Applied Expansions",
    "subtitle": "Maclaurin Series, Lagrange & Integral Remainder Bounds, and Relativistic Quantum Corrections",
    "sections": u8_sections,
    "simulations": ["sim_calc2_taylor"],
    "problems": u8_problems
}

# Write files
with open("calc2_u7.json", "w", encoding="utf-8") as f:
    json.dump(u7_data, f, indent=2, ensure_ascii=False)
print("Saved calc2_u7.json successfully.")

with open("calc2_u8.json", "w", encoding="utf-8") as f:
    json.dump(u8_data, f, indent=2, ensure_ascii=False)
print("Saved calc2_u8.json successfully.")
