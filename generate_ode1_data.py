# -*- coding: utf-8 -*-
"""
Generator for ordinary-differential-equations-1-data.js
Full 8-chapter university honors textbook with 3x content depth, complete KaTeX proofs,
24 tiered solved university examination problems, and 8 inline simulations.
"""
import json

course_data = {
    "courseCode": "MTH 2103",
    "courseTitle": "Ordinary Differential Equations I",
    "courseSubtitle": "Analytical Methods, Existence Theory, Higher-Order Linear Systems & Dynamic Modeling",
    "credits": 3,
    "lectureHours": 45,
    "prerequisites": "Calculus I (MTH 1101) & Calculus II (MTH 1202)",
    "description": "Comprehensive university honors digital textbook covering ordinary differential equations and their applications in physical, biological, and engineering sciences: classifications, Picard-Lindelöf existence and uniqueness theory, direction fields, exact differential forms, integrating factors, Bernoulli, Riccati, and Clairaut equations, orthogonal trajectories, linear differential operators, Wronskian algebra, Abel's identity, reduction of order, constant coefficient and Cauchy-Euler equations, undetermined coefficients, variation of parameters, mechanical vibrations, resonance, RLC circuits, and rocket motion.",
    "units": [
        # UNIT 1
        {
            "unitNumber": 1,
            "title": "Foundations, Classifications & Geometric Theory of Differential Equations",
            "leadSummary": "Comprehensive mathematical foundations of ordinary differential equations: classification criteria (order, degree, linearity), elimination of arbitrary constants, general versus singular solutions, initial and boundary value formulations, Picard-Lindelöf existence and uniqueness theorem, Picard iteration convergence, direction fields, isoclines, and autonomous phase line stability.",
            "sections": [
                {
                    "id": "u1-sec1",
                    "secNumber": "1.1",
                    "title": "Classification of Differential Equations: Order, Degree & Linearity",
                    "content": r"""
<h4>1. Fundamental Definitions & Terminology</h4>
<p>A <strong>differential equation (DE)</strong> is any mathematical equation involving an unknown function $y = \phi(x)$ and one or more of its derivatives with respect to one or more independent variables. If the unknown function depends on only <em>one</em> independent variable, the equation is called an <strong>Ordinary Differential Equation (ODE)</strong>. If the unknown function depends on two or more independent variables, the equation involves partial derivatives and is designated a <strong>Partial Differential Equation (PDE)</strong>.</p>

<p>The general implicit representation of an $n$-th order ODE in a single dependent variable $y$ and independent variable $x$ is expressed as:</p>
<div class="math-display">
$$F\left(x, y, \frac{dy}{dx}, \frac{d^2y}{dx^2}, \dots, \frac{d^ny}{dx^n}\right) = 0, \quad \text{or explicitly as } \frac{d^ny}{dx^n} = f\left(x, y, y', \dots, y^{(n-1)}\right)$$
</div>

<h4>2. Order and Degree of an Ordinary Differential Equation</h4>
<p>Two foundational topological and algebraic integers characterize any ODE:</p>
<ul>
  <li><strong>Order</strong>: The order of a differential equation is the order of the <em>highest derivative</em> appearing in the equation. For instance, $\frac{d^2y}{dx^2} + 5\left(\frac{dy}{dx}\right)^3 + y = 0$ is of <strong>order 2</strong>.</li>
  <li><strong>Degree</strong>: The degree of a differential equation is the power (algebraic exponent) to which the highest derivative is raised, after the equation has been rationalized and cleared of all fractional powers and radicals with respect to the derivatives. For example, in $\left[1 + \left(\frac{dy}{dx}\right)^2\right]^{3/2} = k \frac{d^2y}{dx^2}$, squaring both sides yields $\left[1 + (y')^2\right]^3 = k^2 (y'')^2$, confirming that the equation has <strong>order 2 and degree 2</strong>.</li>
</ul>

<h4>3. The Criterion of Linearity</h4>
<p>An $n$-th order ordinary differential equation is classified as <strong>linear</strong> if it can be written in the form:</p>
<div class="math-display">
$$a_n(x) \frac{d^ny}{dx^n} + a_{n-1}(x) \frac{d^{n-1}y}{dx^{n-1}} + \dots + a_1(x) \frac{dy}{dx} + a_0(x) y = g(x)$$
</div>
<p>Linearly characterized equations must strictly satisfy two defining properties:</p>
<ol>
  <li>The dependent variable $y$ and all its derivatives $y', y'', \dots, y^{(n)}$ appear strictly to the <strong>first power</strong> (no terms like $y^2, (y')^3, \sqrt{y'}$).</li>
  <li>No products of the dependent variable and its derivatives appear (no terms like $y \cdot y'$ or $y' \cdot y''$).</li>
  <li>Coefficients $a_k(x)$ and the forcing term $g(x)$ depend solely on the independent variable $x$.</li>
</ol>
<p>If any of these conditions are violated, the equation is non-linear (e.g., $y'' + \sin(y) = 0$ is non-linear due to the transcendental term in $y$; $y y' + x = 0$ is non-linear due to the product $y y'$).</p>
"""
                },
                {
                    "id": "u1-sec2",
                    "secNumber": "1.2",
                    "title": "Formation of ODEs, Solution Concepts & Initial vs Boundary Value Problems",
                    "content": r"""
<h4>1. Formation of Differential Equations by Eliminating Arbitrary Constants</h4>
<p>In physical modeling and analytical geometry, a family of curves is defined by an algebraic equation containing $n$ arbitrary parameters (constants) $C_1, C_2, \dots, C_n$:</p>
<div class="math-display">
$$\Phi(x, y, C_1, C_2, \dots, C_n) = 0$$
</div>
<p>To eliminate these $n$ arbitrary constants, we differentiate the relation successively $n$ times with respect to $x$, yielding a system of $n + 1$ equations involving $x, y, y', y'', \dots, y^{(n)}$ and $C_1, \dots, C_n$. Eliminating the $n$ constants among these $n+1$ relations produces an ODE of order $n$.</p>
<p><strong>Fundamental Theorem</strong>: The elimination of $n$ independent arbitrary constants from a relation yields a differential equation of order exactly $n$.</p>

<h4>2. Taxonomies of Solutions: General, Particular & Singular</h4>
<ul>
  <li><strong>General Solution</strong>: An explicit or implicit relation $\phi(x, y, C_1, \dots, C_n) = 0$ that satisfies the $n$-th order ODE and contains exactly $n$ essential arbitrary constants.</li>
  <li><strong>Particular Solution</strong>: Any solution obtained directly from the general solution by assigning specific numerical values to one or more of the arbitrary constants $C_k$, typically dictated by initial or boundary constraints.</li>
  <li><strong>Singular Solution</strong>: A solution that cannot be obtained from the general solution by any choice of the arbitrary constants. Geometrically, singular solutions represent envelopes of the family of curves represented by the general solution.</li>
</ul>

<h4>3. Initial Value Problems (IVPs) versus Boundary Value Problems (BVPs)</h4>
<p>An <strong>Initial Value Problem (IVP)</strong> prescribes conditions on the unknown function and its derivatives at a <em>single value</em> of the independent variable $x_0$:</p>
<div class="math-display">
$$y^{(n)} = f(x, y, y', \dots, y^{(n-1)}), \quad y(x_0) = y_0, \quad y'(x_0) = y_1, \quad \dots, \quad y^{(n-1)}(x_0) = y_{n-1}$$
</div>
<p>A <strong>Boundary Value Problem (BVP)</strong>, by contrast, prescribes conditions at two or more distinct points (e.g., $y(a) = \alpha$, $y(b) = \beta$). While IVPs generally possess unique solutions under Lipschitz conditions, BVPs can have a unique solution, infinitely many solutions, or no solution at all.</p>
"""
                },
                {
                    "id": "u1-sec3",
                    "secNumber": "1.3",
                    "title": "The Picard-Lindelöf Existence & Uniqueness Theorem and Picard Iterations",
                    "content": r"""
<h4>1. Statement of the Picard-Lindelöf Theorem</h4>
<div class="math-display">
$$\mathbf{\text{Theorem (Picard-Lindelöf): Let } R = \{(x, y) \in \mathbb{R}^2 : |x - x_0| \le a, |y - y_0| \le b\} \text{ be a closed rectangle.}}$$
</div>
<p>If $f(x, y)$ is continuous on $R$ and satisfies a <strong>Lipschitz condition</strong> with respect to $y$ in $R$, that is, there exists a constant $L > 0$ such that:</p>
<div class="math-display">
$$|f(x, y_1) - f(x, y_2)| \le L |y_1 - y_2| \quad \forall (x, y_1), (x, y_2) \in R$$
</div>
<p>then there exists a unique solution $y = \phi(x)$ to the initial value problem $y' = f(x, y), y(x_0) = y_0$, defined on an interval $|x - x_0| \le h$, where $h = \min\left(a, \frac{b}{M}\right)$ and $M = \max_{(x,y) \in R} |f(x, y)|$.</p>

<h4>2. Picard's Method of Successive Approximations</h4>
<p>Integrating $y' = f(t, y(t))$ from $x_0$ to $x$ converts the differential initial value problem into an equivalent <em>Volterra integral equation</em>:</p>
<div class="math-display">
$$y(x) = y_0 + \int_{x_0}^x f(t, y(t)) dt$$
</div>
<p>Picard's iterative algorithm constructs a sequence of continuous approximations $\{\phi_k(x)\}_{k=0}^\infty$ defined recursively by:</p>
<div class="math-display">
$$\phi_0(x) = y_0, \qquad \phi_{k+1}(x) = y_0 + \int_{x_0}^x f(t, \phi_k(t)) dt \quad (k = 0, 1, 2, \dots)$$
</div>
<p>By Banach's fixed-point theorem on the complete metric space $C([x_0-h, x_0+h])$, this sequence converges uniformly to the unique continuous solution $\phi(x) = \lim_{k\to\infty} \phi_k(x)$.</p>

<h4>3. Step-by-Step Analytical Example</h4>
<p>Consider the IVP: $y' = 2x(1 + y)$ with $y(0) = 0$. Here $x_0 = 0, y_0 = 0$, and $f(x, y) = 2x(1 + y)$:</p>
<div class="math-display">
$$\begin{aligned}
\phi_0(x) &= 0 \\
\phi_1(x) &= 0 + \int_0^x 2t(1 + \phi_0(t)) dt = \int_0^x 2t dt = x^2 \\
\phi_2(x) &= \int_0^x 2t(1 + t^2) dt = \left[ t^2 + \frac{t^4}{2} \right]_0^x = x^2 + \frac{x^4}{2!} \\
\phi_3(x) &= \int_0^x 2t\left(1 + t^2 + \frac{t^4}{2}\right) dt = x^2 + \frac{x^4}{2!} + \frac{x^6}{3!} \\
\dots \\
\phi_n(x) &= \sum_{k=1}^n \frac{(x^2)^k}{k!} \implies \lim_{n\to\infty} \phi_n(x) = \sum_{k=1}^\infty \frac{(x^2)^k}{k!} = e^{x^2} - 1
\end{aligned}$$
</div>
<p>Direct differentiation confirms: $\phi'(x) = 2x e^{x^2} = 2x(1 + (e^{x^2}-1)) = 2x(1 + y)$ with $\phi(0) = e^0 - 1 = 0$, yielding the exact closed-form solution!</p>
"""
                },
                {
                    "id": "u1-sec4",
                    "secNumber": "1.4",
                    "title": "Direction Fields, Isoclines & Autonomous Phase Line Dynamics",
                    "content": r"""
<h4>1. Direction Fields (Slope Fields) & Geometric Interpretation</h4>
<p>Even when a first-order ODE $y' = f(x, y)$ cannot be solved by elementary analytical integration, the equation provides immediate geometric insight: at every point $(x, y)$ in the plane where $f(x, y)$ is defined, the derivative $y'$ represents the <strong>slope of the tangent line</strong> to the integral curve passing through that point. A <em>direction field</em> is a graphical grid of small line segments possessing slope $f(x, y)$.</p>

<h4>2. The Method of Isoclines</h4>
<p>An <strong>isocline</strong> is a curve along which the slopes of the integral curves are constant. Setting $f(x, y) = c$, where $c$ is a constant parameter, yields the family of isoclines. Integral curves cross each isocline $f(x, y) = c$ with precisely the slope $c$. Sketching several isoclines provides an exact scaffolding for tracing solution trajectories.</p>

<h4>3. Autonomous Equations & Phase Line Stability</h4>
<p>An ODE is called <strong>autonomous</strong> if the independent variable $x$ (often time $t$) does not appear explicitly:</p>
<div class="math-display">
$$\frac{dy}{dt} = f(y)$$
</div>
<p>The zeros of $f(y)$, where $f(c) = 0$, are called <strong>equilibrium points</strong> (or critical points). The constant functions $y(t) \equiv c$ are equilibrium solutions. The qualitative behavior of all non-equilibrium solutions is classified on the one-dimensional <strong>phase line</strong>:</p>
<ul>
  <li><strong>Asymptotically Stable (Attractor / Sink)</strong>: If $f'(c) < 0$, trajectories on both sides move toward $c$ as $t \to \infty$.</li>
  <li><strong>Unstable (Repeller / Source)</strong>: If $f'(c) > 0$, trajectories on both sides move away from $c$ as $t \to \infty$.</li>
  <li><strong>Semi-stable (Shunt)</strong>: Trajectories approach $c$ from one side and diverge on the other (occurs when $f(y)$ does not change sign across $c$, such as when $f(y)$ has a double root).</li>
</ul>
""",
                    "simulation": "ode1-dirfield-sim"
                }
            ],
            "problems": [
                {
                    "id": "ode1-prob-1",
                    "difficulty": "Easy",
                    "difficultyLabel": "Tier 1 • Foundational",
                    "title": "Picard Successive Iteration for a Linear IVP",
                    "statement": "Apply Picard's method of successive approximations to compute the first three iterative approximations $\\phi_1(x), \\phi_2(x), \\phi_3(x)$ for the initial value problem:<br>$$\\frac{dy}{dx} = x + y, \\quad y(0) = 1$$<br>Verify the induction pattern and compare with the exact solution.",
                    "solution": r"The initial value problem is $y' = x + y$ with initial condition $x_0 = 0, y_0 = 1$. The integral formulation is $\phi_{k+1}(x) = 1 + \int_0^x (t + \phi_k(t)) dt$.<br><br><b>Step 1: Zeroth approximation</b><br>$\phi_0(x) = y_0 = 1$.<br><br><b>Step 2: First approximation</b><br>$$\phi_1(x) = 1 + \int_0^x (t + 1) dt = 1 + \left[\frac{t^2}{2} + t\right]_0^x = 1 + x + \frac{x^2}{2}$$<br><br><b>Step 3: Second approximation</b><br>$$\phi_2(x) = 1 + \int_0^x \left(t + 1 + t + \frac{t^2}{2}\right) dt = 1 + \int_0^x \left(1 + 2t + \frac{t^2}{2}\right) dt = 1 + x + x^2 + \frac{x^3}{6}$$<br><br><b>Step 4: Third approximation</b><br>$$\phi_3(x) = 1 + \int_0^x \left(t + 1 + t + t^2 + \frac{t^3}{6}\right) dt = 1 + x + x^2 + \frac{x^3}{3} + \frac{x^4}{24}$$<br><br><b>Analytical Comparison:</b><br>The exact linear solution via integrating factor $\mu(x) = e^{-x}$ gives $y(x) = 2e^x - x - 1$. Expanding $2e^x - x - 1 = 2(1 + x + x^2/2! + x^3/3! + x^4/4! + \dots) - x - 1 = 1 + x + x^2 + x^3/3 + x^4/12 + \dots$, matching the Picard polynomial expansion order by order.",
                    "answer": r"$\phi_1(x) = 1 + x + \frac{x^2}{2}$, $\phi_2(x) = 1 + x + x^2 + \frac{x^3}{6}$, $\phi_3(x) = 1 + x + x^2 + \frac{x^3}{3} + \frac{x^4}{24}$. The iterations converge to $y(x) = 2e^x - x - 1$."
                },
                {
                    "id": "ode1-prob-2",
                    "difficulty": "Medium",
                    "difficultyLabel": "Tier 2 • Analytical University Exam",
                    "title": "Elimination of Arbitrary Constants & Differential Family of Circles",
                    "statement": "Find the differential equation of the family of all circles in the $xy$-plane having their centers on the $x$-axis. Determine its order, degree, and linearity.",
                    "solution": r"<b>Step 1: General equation of the family</b><br>A circle with center on the $x$-axis has coordinates $(h, 0)$ and arbitrary radius $r$. The family depends on two arbitrary parameters $h$ and $r$:<br>$$(x - h)^2 + y^2 = r^2$$<br><br><b>Step 2: First differentiation with respect to $x$</b><br>$$2(x - h) + 2y \frac{dy}{dx} = 0 \implies x - h = -y y' \implies h = x + y y'$$<br><br><b>Step 3: Second differentiation to eliminate $h$ and $r$</b><br>Differentiating $x - h = -y y'$ with respect to $x$:<br>$$\frac{d}{dx}(x - h) = \frac{d}{dx}(-y y') \implies 1 = -\left[ (y')^2 + y y'' \right]$$Rearranging into standard form:<br>$$y \frac{d^2y}{dx^2} + \left(\frac{dy}{dx}\right)^2 + 1 = 0$$<br><br><b>Step 4: Classification</b><br>The highest derivative is $y''$, so the <b>order is 2</b>. The power of $y''$ is 1, so the <b>degree is 1</b>. However, the presence of the product $y y''$ and the squared term $(y')^2$ proves the equation is <b>non-linear</b>.",
                    "answer": r"Differential equation: $y y'' + (y')^2 + 1 = 0$. Order: 2, Degree: 1, Linearity: Non-linear."
                },
                {
                    "id": "ode1-prob-3",
                    "difficulty": "Hard",
                    "difficultyLabel": "Tier 3 • Honors Challenge",
                    "title": "Lipschitz Domain & Local Uniqueness Breakdown Analysis",
                    "statement": "Investigate the existence and uniqueness of solutions for the initial value problem:<br>$$\\frac{dy}{dx} = 3 y^{2/3}, \\quad y(0) = 0$$<br>Prove that the Lipschitz condition is violated on any interval containing $y = 0$, construct infinitely many distinct solutions, and interpret geometrically.",
                    "solution": r"<b>Step 1: Lipschitz continuity examination</b><br>Here $f(x, y) = 3 y^{2/3}$. Consider the partial derivative with respect to $y$:<br>$$\frac{\partial f}{\partial y} = \frac{d}{dy}\left(3 y^{2/3}\right) = 2 y^{-1/3} = \frac{2}{\sqrt[3]{y}}$$As $y \to 0$, $\left|\frac{\partial f}{\partial y}\right| \to \infty$. By the Mean Value Theorem, $|f(x, y_1) - f(x, y_2)| / |y_1 - y_2| = |f_y(x, \xi)| = 2 / |\xi|^{1/3}$. As $\xi \to 0$, no finite Lipschitz constant $L$ exists on any rectangle containing $y = 0$.<br><br><b>Step 2: Analytical separation of variables</b><br>For $y \neq 0$:<br>$$\frac{dy}{y^{2/3}} = 3 dx \implies \int y^{-2/3} dy = \int 3 dx \implies 3 y^{1/3} = 3x + C \implies y(x) = (x + c)^3$$Applying $y(0) = 0$ gives $c = 0$, yielding the solution $y_1(x) = x^3$.<br><br><b>Step 3: Trivial solution & infinite family of branch solutions</b><br>By inspection, the constant function $y_0(x) \equiv 0$ is also a solution since $y_0'(x) = 0 = 3(0)^{2/3}$ and $y_0(0) = 0$.<br>Moreover, for any parameter $c > 0$, we can construct the $C^1$ spliced solution:<br>$$y_c(x) = \begin{cases} 0, & x \le c \\ (x - c)^3, & x > c \end{cases}$$Direct differentiation verifies that $y_c'(x) = 3(y_c(x))^{2/3}$ everywhere and $y_c(0) = 0$. Thus, there are infinitely many distinct solutions passing through $(0, 0)$!",
                    "answer": r"The Lipschitz condition fails at $y=0$ because $\lim_{y\to 0} |f_y| = \infty$. Consequently, uniqueness fails: both $y(x) \equiv 0$ and $y(x) = x^3$ (as well as piecewise families spliced at any $c \ge 0$) satisfy the IVP."
                }
            ]
        },

        # UNIT 2
        {
            "unitNumber": 2,
            "title": "Solution of First-Order Equations: Separable, Exact & Special Integrating Factors",
            "leadSummary": "Exhaustive treatment of first-order analytical integration: variables separable equations, substitutions reducing to separable forms, homogeneous equations and the Euler substitution v = y/x, exact differential forms, potential function construction, special single-variable and multi-variable integrating factors, and Leibniz first-order linear equations.",
            "sections": [
                {
                    "id": "u2-sec1",
                    "secNumber": "2.1",
                    "title": "Separable Differential Equations & Transformations of Dependent Variables",
                    "content": r"""
<h4>1. Variables Separable Equations</h4>
<p>A first-order differential equation is <strong>separable</strong> if the derivative factorizes into a product of a function of $x$ alone and a function of $y$ alone:</p>
<div class="math-display">
$$\frac{dy}{dx} = g(x) h(y) \implies \frac{1}{h(y)} dy = g(x) dx \quad (h(y) \neq 0)$$
</div>
<p>Integrating both sides directly yields the one-parameter implicit general solution:</p>
<div class="math-display">
$$\int \frac{dy}{h(y)} = \int g(x) dx + C$$
</div>
<p><em>Caution</em>: Any constant $y = c$ where $h(c) = 0$ is a potential singular or equilibrium solution that must be checked separately, as division by $h(y)$ assumes $h(y) \neq 0$.</p>

<h4>2. Equations Reducible to Separable Form via Substitution $v = ax + by + c$</h4>
<p>Equations of the form $\frac{dy}{dx} = f(ax + by + c)$, where $b \neq 0$, are rendered separable by defining the substitution $v = ax + by + c$. Differentiating with respect to $x$:</p>
<div class="math-display">
$$\frac{dv}{dx} = a + b \frac{dy}{dx} = a + b f(v) \implies \frac{dv}{a + b f(v)} = dx$$
</div>
<p>Integrating both sides yields the solution in terms of $v$, and back-substituting $v = ax + by + c$ gives the final answer.</p>

<h4>3. Homogeneous Equations of Degree Zero</h4>
<p>A function $f(x, y)$ is <strong>homogeneous of degree $n$</strong> if $f(tx, ty) = t^n f(x, y)$ for all $t > 0$. An ODE $M(x, y)dx + N(x, y)dy = 0$ is homogeneous if $M$ and $N$ are homogeneous functions of the same degree $n$. In that case, $\frac{dy}{dx} = F\left(\frac{y}{x}\right)$.</p>
<p>The standard transformation is the <strong>Euler substitution</strong>: $y = v x$, whence $\frac{dy}{dx} = v + x \frac{dv}{dx}$. Substituting into the ODE:</p>
<div class="math-display">
$$v + x \frac{dv}{dx} = F(v) \implies x \frac{dv}{dx} = F(v) - v \implies \frac{dv}{F(v) - v} = \frac{dx}{x}$$
</div>
<p>which is completely separated in the variables $v$ and $x$.</p>
"""
                },
                {
                    "id": "u2-sec2",
                    "secNumber": "2.2",
                    "title": "Exact Differential Equations & Potential Function Construction",
                    "content": r"""
<h4>1. The Total Differential & The Exactness Criterion</h4>
<p>A first-order differential expression $M(x, y)dx + N(x, y)dy$ is an <strong>exact differential</strong> in an open simply connected domain $D \subset \mathbb{R}^2$ if there exists a continuously differentiable potential function $\Phi(x, y)$ such that:</p>
<div class="math-display">
$$d\Phi = \frac{\partial \Phi}{\partial x} dx + \frac{\partial \Phi}{\partial y} dy = M(x, y)dx + N(x, y)dy$$
</div>
<p>If $M(x, y)dx + N(x, y)dy = 0$ is exact, its general solution is immediately given by the level curves:</p>
<div class="math-display">
$$\Phi(x, y) = C$$
</div>

<div class="math-display">
$$\mathbf{\text{Theorem (Criterion for Exactness): Let } M(x, y) \text{ and } N(x, y) \text{ be continuous with continuous first partial derivatives on } D.}}$$
</div>
<p>The differential equation $M(x, y)dx + N(x, y)dy = 0$ is exact if and only if:</p>
<div class="math-display">
$$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x} \quad \forall (x, y) \in D$$
</div>

<h4>2. Construction of the Potential Function $\Phi(x, y)$</h4>
<p>To find $\Phi(x, y)$, we integrate $\frac{\partial \Phi}{\partial x} = M(x, y)$ with respect to $x$, treating $y$ as a constant:</p>
<div class="math-display">
$$\Phi(x, y) = \int M(x, y) dx + g(y)$$
</div>
<p>where $g(y)$ is an arbitrary function of $y$ acting as the integration constant. Differentiating this expression with respect to $y$ and equating to $N(x, y)$:</p>
<div class="math-display">
$$\frac{\partial \Phi}{\partial y} = \frac{\partial}{\partial y}\left(\int M(x, y) dx\right) + g'(y) = N(x, y) \implies g'(y) = N(x, y) - \frac{\partial}{\partial y}\left(\int M(x, y) dx\right)$$
</div>
<p>By the exactness condition $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$, the right-hand side is strictly independent of $x$. Integrating $g'(y)$ with respect to $y$ yields $g(y)$ and completes the potential function $\Phi(x, y) = C$.</p>
""",
                    "simulation": "ode1-exact-contour-sim"
                },
                {
                    "id": "u2-sec3",
                    "secNumber": "2.3",
                    "title": "Special Integrating Factors: Single & Multi-Variable Formulas",
                    "content": r"""
<h4>1. Concept of the Integrating Factor</h4>
<p>If the equation $M(x, y)dx + N(x, y)dy = 0$ is not exact ($\frac{\partial M}{\partial y} \neq \frac{\partial N}{\partial x}$), it can often be made exact by multiplying by an <strong>integrating factor</strong> $\mu(x, y) \neq 0$ such that:</p>
<div class="math-display">
$$\frac{\partial}{\partial y}(\mu M) = \frac{\partial}{\partial x}(\mu N) \implies \mu \frac{\partial M}{\partial y} + M \frac{\partial \mu}{\partial y} = \mu \frac{\partial N}{\partial x} + N \frac{\partial \mu}{\partial x}$$
</div>

<h4>2. Standard Single-Variable Integrating Factors</h4>
<ul>
  <li><strong>Integrating factor depending only on $x$ ($\mu = \mu(x)$)</strong>:<br>
    Here $\frac{\partial \mu}{\partial y} = 0$ and $\frac{\partial \mu}{\partial x} = \frac{d\mu}{dx}$. The condition reduces to:
    $$\frac{1}{\mu} \frac{d\mu}{dx} = \frac{M_y - N_x}{N}$$
    If $\frac{M_y - N_x}{N} = f(x)$ is a function of $x$ alone, then:
    $$\mu(x) = \exp\left(\int \frac{M_y - N_x}{N} dx\right)$$
  </li>
  <li><strong>Integrating factor depending only on $y$ ($\mu = \mu(y)$)</strong>:<br>
    Here $\frac{\partial \mu}{\partial x} = 0$ and $\frac{\partial \mu}{\partial y} = \frac{d\mu}{dy}$. The condition reduces to:
    $$\frac{1}{\mu} \frac{d\mu}{dy} = \frac{N_x - M_y}{M}$$
    If $\frac{N_x - M_y}{M} = g(y)$ is a function of $y$ alone, then:
    $$\mu(y) = \exp\left(\int \frac{N_x - M_y}{M} dy\right)$$
  </li>
</ul>

<h4>3. Multi-Variable Integrating Factors & Homogeneous Theorem</h4>
<ul>
  <li>If $\frac{M_y - N_x}{y N - x M} = h(xy)$, then $\mu = \exp\left(\int h(u) du\right)$ where $u = xy$.</li>
  <li><strong>Homogeneous Equation Theorem</strong>: If $M dx + N dy = 0$ is a homogeneous equation of degree $n$ and $Mx + Ny \neq 0$, then:
    $$\mu(x, y) = \frac{1}{Mx + Ny}$$
    is always an integrating factor.
  </li>
</ul>
"""
                },
                {
                    "id": "u2-sec4",
                    "secNumber": "2.4",
                    "title": "First-Order Linear Differential Equations (Leibniz Formula)",
                    "content": r"""
<h4>1. Standard Linear Form</h4>
<p>The general first-order linear differential equation is written in canonical form as:</p>
<div class="math-display">
$$\frac{dy}{dx} + P(x) y = Q(x)$$
</div>
<p>where $P(x)$ and $Q(x)$ are continuous functions on an interval $I$. Rewriting in differential form: $(P(x)y - Q(x))dx + dy = 0$, where $M = P(x)y - Q(x)$ and $N = 1$.</p>
<p>Testing for exactness: $M_y = P(x)$ and $N_x = 0$. Since $M_y \neq N_x$, the equation is not exact, but:</p>
<div class="math-display">
$$\frac{M_y - N_x}{N} = \frac{P(x) - 0}{1} = P(x)$$
</div>
<p>which depends strictly on $x$ alone!</p>

<h4>2. Derivation of the Closed-Form General Solution</h4>
<p>The integrating factor is $\mu(x) = \exp\left(\int P(x) dx\right)$. Multiplying the standard form by $\mu(x)$:</p>
<div class="math-display">
$$e^{\int P(x)dx} \frac{dy}{dx} + P(x) e^{\int P(x)dx} y = Q(x) e^{\int P(x)dx}$$
</div>
<p>By the product rule of differentiation, the left side is the exact derivative of the product $\mu(x) y$:</p>
<div class="math-display">
$$\frac{d}{dx}\left[ y \cdot e^{\int P(x)dx} \right] = Q(x) e^{\int P(x)dx}$$
</div>
<p>Integrating both sides directly with respect to $x$:</p>
<div class="math-display">
$$y \cdot e^{\int P(x)dx} = \int Q(x) e^{\int P(x)dx} dx + C \implies y(x) = e^{-\int P(x)dx} \left[ \int Q(x) e^{\int P(x)dx} dx + C \right]$$
</div>
<p>This closed-form formula provides the complete general solution to any first-order linear ODE.</p>
"""
                }
            ],
            "problems": [
                {
                    "id": "ode1-prob-4",
                    "difficulty": "Easy",
                    "difficultyLabel": "Tier 1 • Foundational",
                    "title": "Exact Differential Equation with Trigonometric Potential",
                    "statement": "Test for exactness and find the general solution of the differential equation:<br>$$(2x \cos y + 3x^2 y) dx + (x^3 - x^2 \sin y - y) dy = 0$$",
                    "solution": r"<b>Step 1: Test exactness</b><br>Here $M(x, y) = 2x \cos y + 3x^2 y$ and $N(x, y) = x^3 - x^2 \sin y - y$.<br>Compute the partial derivatives:<br>$$\frac{\partial M}{\partial y} = -2x \sin y + 3x^2$$<br>$$\frac{\partial N}{\partial x} = 3x^2 - 2x \sin y$$<br>Since $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$, the equation is exact in all of $\mathbb{R}^2$.<br><br><b>Step 2: Integrate $M$ with respect to $x$</b><br>$$\Phi(x, y) = \int (2x \cos y + 3x^2 y) dx + g(y) = x^2 \cos y + x^3 y + g(y)$$<br><br><b>Step 3: Differentiate with respect to $y$ and match $N$</b><br>$$\frac{\partial \Phi}{\partial y} = -x^2 \sin y + x^3 + g'(y) = N(x, y) = x^3 - x^2 \sin y - y$$Equating gives $g'(y) = -y \implies g(y) = -\frac{1}{2}y^2$.<br><br><b>Step 4: Formulate the general solution</b><br>The potential function is $\Phi(x, y) = x^2 \cos y + x^3 y - \frac{1}{2}y^2 = C$.",
                    "answer": r"$\Phi(x, y) = x^2 \cos y + x^3 y - \frac{1}{2}y^2 = C$ (or $2x^2 \cos y + 2x^3 y - y^2 = C'$)."
                },
                {
                    "id": "ode1-prob-5",
                    "difficulty": "Medium",
                    "difficultyLabel": "Tier 2 • Analytical University Exam",
                    "title": "Special Integrating Factor $\mu(y)$ for a Non-Exact Equation",
                    "statement": "Solve the non-exact differential equation:<br>$$(y + x y^2) dx - x dy = 0$$<br>by deriving an appropriate integrating factor.",
                    "solution": r"<b>Step 1: Test exactness</b><br>$M = y + x y^2$ and $N = -x$.<br>$$\frac{\partial M}{\partial y} = 1 + 2xy, \quad \frac{\partial N}{\partial x} = -1 \implies M_y - N_x = 2 + 2xy = 2(1 + xy)$$Since $M_y \neq N_x$, the equation is not exact.<br><br><b>Step 2: Determine integrating factor</b><br>Check $\frac{N_x - M_y}{M}$:<br>$$\frac{N_x - M_y}{M} = \frac{-1 - (1 + 2xy)}{y(1 + xy)} = \frac{-2(1 + xy)}{y(1 + xy)} = -\frac{2}{y}$$This depends purely on $y$! The integrating factor is:<br>$$\mu(y) = \exp\left(\int -\frac{2}{y} dy\right) = e^{-2 \ln |y|} = \frac{1}{y^2}$$<br><br><b>Step 3: Multiply ODE by $\mu(y)$</b><br>$$\frac{y + x y^2}{y^2} dx - \frac{x}{y^2} dy = 0 \implies \left(\frac{1}{y} + x\right) dx - \frac{x}{y^2} dy = 0$$Now $M^* = \frac{1}{y} + x$ and $N^* = -\frac{x}{y^2}$. Note $M^*_y = -1/y^2 = N^*_x$ (exact!).<br><br><b>Step 4: Integrate</b><br>$$\Phi = \int \left(\frac{1}{y} + x\right) dx + g(y) = \frac{x}{y} + \frac{x^2}{2} + g(y)$$$$\frac{\partial \Phi}{\partial y} = -\frac{x}{y^2} + g'(y) = -\frac{x}{y^2} \implies g'(y) = 0 \implies g(y) = C_0$$Thus $\frac{x}{y} + \frac{x^2}{2} = C$.",
                    "answer": r"$\mu(y) = \frac{1}{y^2}$, yielding the general solution $\frac{x}{y} + \frac{x^2}{2} = C$ (or $2x + x^2 y = 2Cy$)."
                },
                {
                    "id": "ode1-prob-6",
                    "difficulty": "Hard",
                    "difficultyLabel": "Tier 3 • Honors Challenge",
                    "title": "Homogeneous Differential Form & Polar Integrating Factor",
                    "statement": "Solve the homogeneous initial value problem:<br>$$(x^2 + 3xy + y^2) dx - x^2 dy = 0, \\quad y(1) = 0$$<br>using both the substitution $y = vx$ and the homogeneous integrating factor theorem $\\mu = 1/(Mx + Ny)$.",
                    "solution": r"<b>Method 1: Euler Substitution $y = vx$</b><br>With $y = vx \implies dy = v dx + x dv$:<br>$$(x^2 + 3x(vx) + v^2 x^2) dx - x^2 (v dx + x dv) = 0$$Dividing by $x^2 \neq 0$:<br>$$(1 + 3v + v^2) dx - v dx - x dv = 0 \implies (1 + 2v + v^2) dx - x dv = 0 \implies (v + 1)^2 dx = x dv$$Separating variables:<br>$$\frac{dx}{x} = \frac{dv}{(v + 1)^2} \implies \ln |x| = -\frac{1}{v + 1} + C$$Back-substituting $v = y/x$:<br>$$\ln |x| = -\frac{1}{\frac{y}{x} + 1} + C = -\frac{x}{x + y} + C \implies \frac{x}{x + y} + \ln |x| = C$$<br><b>Method 2: Homogeneous Integrating Factor</b><br>$M = x^2 + 3xy + y^2$, $N = -x^2$.<br>$$Mx + Ny = x(x^2 + 3xy + y^2) - x^2 y = x^3 + 2x^2 y + x y^2 = x(x + y)^2$$Therefore, $\mu = \frac{1}{x(x + y)^2}$. Multiplying the ODE by $\mu$ yields the identical potential function differential $d\left[\ln |x| + \frac{x}{x + y}\right] = 0$.<br><br><b>Initial Condition:</b><br>At $x = 1, y = 0$: $\frac{1}{1 + 0} + \ln(1) = 1 + 0 = C \implies C = 1$.<br>Thus $\frac{x}{x + y} + \ln |x| = 1 \implies x + y = \frac{x}{1 - \ln |x|}$.",
                    "answer": r"General solution: $\frac{x}{x + y} + \ln |x| = C$. With $y(1) = 0$, $C = 1$, yielding explicit solution $y(x) = \frac{x \ln |x|}{1 - \ln |x|}$."
                }
            ]
        },

        # UNIT 3
        {
            "unitNumber": 3,
            "title": "Advanced Non-Linear First-Order Equations & Singular Solutions",
            "leadSummary": "Comprehensive study of non-linear first-order equations: Bernoulli's equation and transformation to linear form, Riccati's equation and relation to second-order linear ODEs, first-order equations of higher degree solvable for p, y, and x, Clairaut's equation, singular solutions, and the p-discriminant envelope geometry.",
            "sections": [
                {
                    "id": "u3-sec1",
                    "secNumber": "3.1",
                    "title": "Bernoulli's Differential Equation & Transformation to Linear Form",
                    "content": r"""
<h4>1. Standard Form of Bernoulli's Equation</h4>
<p>An equation of the form:</p>
<div class="math-display">
$$\frac{dy}{dx} + P(x) y = Q(x) y^n$$
</div>
<p>where $P(x)$ and $Q(x)$ are continuous functions and $n \in \mathbb{R}$ is any real constant, is called <strong>Bernoulli's equation</strong>. If $n = 0$, it is linear non-homogeneous. If $n = 1$, it is linear homogeneous and separable. For any $n \neq 0, 1$, it is strictly non-linear.</p>

<h4>2. The Power Transformation Method</h4>
<p>Dividing the equation by $y^n$:</p>
<div class="math-display">
$$y^{-n} \frac{dy}{dx} + P(x) y^{1-n} = Q(x)$$
</div>
<p>Introduce the change of variable $v = y^{1-n}$. Differentiating with respect to $x$ using the chain rule:</p>
<div class="math-display">
$$\frac{dv}{dx} = (1 - n) y^{-n} \frac{dy}{dx} \implies y^{-n} \frac{dy}{dx} = \frac{1}{1 - n} \frac{dv}{dx}$$
</div>
<p>Substituting into the equation transforms it into an exact first-order <strong>linear</strong> ODE in $v$:</p>
<div class="math-display">
$$\frac{1}{1 - n} \frac{dv}{dx} + P(x) v = Q(x) \implies \frac{dv}{dx} + (1 - n) P(x) v = (1 - n) Q(x)$$
</div>
<p>This linear equation is solved using integrating factor $\mu(x) = \exp\left((1 - n) \int P(x) dx\right)$, followed by back-substitution $v = y^{1-n}$.</p>
"""
                },
                {
                    "id": "u3-sec2",
                    "secNumber": "3.2",
                    "title": "Riccati's Equation: Reduction Theorems & Second-Order Connection",
                    "content": r"""
<h4>1. The General Riccati Equation</h4>
<p>A non-linear differential equation of the quadratic form:</p>
<div class="math-display">
$$\frac{dy}{dx} = P(x) y^2 + Q(x) y + R(x)$$
</div>
<p>is called a <strong>Riccati equation</strong>. In general, Riccati equations cannot be solved by elementary quadratures unless at least one particular solution is already known.</p>

<h4>2. Reduction Given One Known Particular Solution $y_1(x)$</h4>
<p>If a particular solution $y_1(x)$ is known (so that $y_1' = P y_1^2 + Q y_1 + R$), the general solution is obtained by the substitution:</p>
<div class="math-display">
$$y(x) = y_1(x) + \frac{1}{v(x)}$$
</div>
<p>Differentiating and substituting into Riccati's equation:</p>
<div class="math-display">
$$y_1' - \frac{1}{v^2} v' = P\left(y_1 + \frac{1}{v}\right)^2 + Q\left(y_1 + \frac{1}{v}\right) + R = \left(P y_1^2 + Q y_1 + R\right) + \frac{2 P y_1 + Q}{v} + \frac{P}{v^2}$$
</div>
<p>Subtracting $y_1'$ and multiplying by $-v^2$ reduces the equation to a standard <strong>linear first-order ODE</strong> in $v$:</p>
<div class="math-display">
$$\frac{dv}{dx} + (2 P(x) y_1(x) + Q(x)) v = -P(x)$$
</div>

<h4>3. Transformation to a Second-Order Linear Equation</h4>
<p>Making the substitution $y = -\frac{1}{P(x) u} \frac{du}{dx}$ transforms the non-linear first-order Riccati equation into a homogeneous <strong>second-order linear ODE</strong> in $u(x)$:</p>
<div class="math-display">
$$u'' - \left(Q(x) + \frac{P'(x)}{P(x)}\right) u' + P(x) R(x) u = 0$$
</div>
"""
                },
                {
                    "id": "u3-sec3",
                    "secNumber": "3.3",
                    "title": "First-Order Higher-Degree Equations & Clairaut's Equation",
                    "content": r"""
<h4>1. First-Order Equations of Higher Degree ($F(x, y, p) = 0$, $p = dy/dx$)</h4>
<p>When the first derivative appears to powers greater than 1, we write $p = \frac{dy}{dx}$. Three primary classical methods solve such equations:</p>
<ol>
  <li><strong>Equations Solvable for $p$</strong>: If $F(x, y, p) = 0$ can be factored as $[p - f_1(x, y)][p - f_2(x, y)] \dots [p - f_k(x, y)] = 0$, then each factor $p = f_i(x, y)$ is solved independently to yield solutions $\phi_i(x, y, C) = 0$. The composite general solution is $\prod_{i=1}^k \phi_i(x, y, C) = 0$.</li>
  <li><strong>Equations Solvable for $y$</strong>: Written as $y = f(x, p)$. Differentiating both sides with respect to $x$ yields $p = \frac{\partial f}{\partial x} + \frac{\partial f}{\partial p} \frac{dp}{dx}$, which is a first-order differential equation in $p$ and $x$.</li>
  <li><strong>Equations Solvable for $x$</strong>: Written as $x = g(y, p)$. Differentiating both sides with respect to $y$ using $\frac{dx}{dy} = \frac{1}{p}$ gives a first-order ODE in $p$ and $y$.</li>
</ol>

<h4>2. Clairaut's Equation</h4>
<p>A classic and prominent equation solvable for $y$ is <strong>Clairaut's equation</strong>:</p>
<div class="math-display">
$$y = x p + f(p), \quad \text{where } p = \frac{dy}{dx}$$
</div>
<p>Differentiating both sides with respect to $x$:</p>
<div class="math-display">
$$p = p + x \frac{dp}{dx} + f'(p) \frac{dp}{dx} \implies \left[ x + f'(p) \right] \frac{dp}{dx} = 0$$
</div>
<p>This product produces two distinct solution branches:</p>
<ul>
  <li><strong>Branch 1 (General Solution)</strong>: $\frac{dp}{dx} = 0 \implies p = C$ (constant). Substituting $p = C$ into the original equation yields the general solution:
    $$y = C x + f(C)$$
    which represents a one-parameter family of straight lines!
  </li>
  <li><strong>Branch 2 (Singular Solution / Envelope)</strong>: $x + f'(p) = 0 \implies x = -f'(p)$. Substituting this into $y = xp + f(p)$ gives the parametric equations of the <strong>singular solution</strong>:
    $$x = -f'(p), \quad y = -p f'(p) + f(p)$$
    Eliminating $p$ between these relations yields an envelope curve that is tangent to every member of the general solution family of straight lines, yet cannot be obtained from $y = Cx + f(C)$ for any constant $C$.
  </li>
</ul>
""",
                    "simulation": "ode1-clairaut-envelope-sim"
                }
            ],
            "problems": [
                {
                    "id": "ode1-prob-7",
                    "difficulty": "Easy",
                    "difficultyLabel": "Tier 1 • Foundational",
                    "title": "Bernoulli Equation with Cubic Non-Linearity",
                    "statement": "Solve the non-linear initial value problem:<br>$$\\frac{dy}{dx} - y = x y^3, \\quad y(0) = 1$$",
                    "solution": r"<b>Step 1: Identify Bernoulli form</b><br>$y' - y = x y^3$ is a Bernoulli equation with $P(x) = -1, Q(x) = x, n = 3$.<br><br><b>Step 2: Apply power substitution</b><br>Divide by $y^3$:<br>$$y^{-3} y' - y^{-2} = x$$Let $v = y^{1-n} = y^{-2}$. Then $v' = -2 y^{-3} y' \implies y^{-3} y' = -\frac{1}{2} v'$.<br>Substitute into the equation:<br>$$-\frac{1}{2} v' - v = x \implies v' + 2v = -2x$$<br><br><b>Step 3: Solve the linear equation for $v$</b><br>Integrating factor $\mu(x) = e^{\int 2 dx} = e^{2x}$.<br>$$\frac{d}{dx}[v e^{2x}] = -2x e^{2x} \implies v e^{2x} = \int -2x e^{2x} dx + C$$Using integration by parts: $\int -2x e^{2x} dx = -x e^{2x} + \frac{1}{2} e^{2x}$.<br>$$v(x) = -x + \frac{1}{2} + C e^{-2x}$$<br><br><b>Step 4: Back-substitute and apply initial condition</b><br>$$y^{-2} = \frac{1}{y^2} = -x + \frac{1}{2} + C e^{-2x}$$At $x = 0, y = 1$: $\frac{1}{1^2} = 0 + \frac{1}{2} + C \implies C = \frac{1}{2}$.<br>Thus $\frac{1}{y^2} = -x + \frac{1}{2} + \frac{1}{2} e^{-2x} = \frac{1 - 2x + e^{-2x}}{2}$.",
                    "answer": r"$y(x) = \sqrt{\frac{2}{1 - 2x + e^{-2x}}}$."
                },
                {
                    "id": "ode1-prob-8",
                    "difficulty": "Medium",
                    "difficultyLabel": "Tier 2 • Analytical University Exam",
                    "title": "Riccati Equation with Known Polynomial Solution",
                    "statement": "Solve the Riccati equation:<br>$$\\frac{dy}{dx} = y^2 - 2xy + x^2 + 1$$<br>given that $y_1(x) = x$ is a particular solution.",
                    "solution": r"<b>Step 1: Verify particular solution</b><br>With $y_1(x) = x$: $y_1' = 1$. The RHS is $x^2 - 2x(x) + x^2 + 1 = 1$. Since $1 = 1$, $y_1 = x$ is indeed a particular solution.<br><br><b>Step 2: Apply Riccati reduction substitution</b><br>Let $y(x) = y_1(x) + \frac{1}{v} = x + \frac{1}{v}$.<br>$$y' = 1 - \frac{v'}{v^2}$$Substitute into the ODE:<br>$$1 - \frac{v'}{v^2} = \left(x + \frac{1}{v}\right)^2 - 2x\left(x + \frac{1}{v}\right) + x^2 + 1 = x^2 + \frac{2x}{v} + \frac{1}{v^2} - 2x^2 - \frac{2x}{v} + x^2 + 1 = 1 + \frac{1}{v^2}$$<br><br><b>Step 3: Simplify and integrate</b><br>Subtracting 1 from both sides:<br>$$-\frac{v'}{v^2} = \frac{1}{v^2} \implies -v' = 1 \implies \frac{dv}{dx} = -1 \implies v(x) = -x + C$$<br><br><b>Step 4: Back-substitute to find $y$</b><br>$$y(x) = x + \frac{1}{C - x} = \frac{x(C - x) + 1}{C - x} = \frac{Cx - x^2 + 1}{C - x}$$",
                    "answer": r"$y(x) = x + \frac{1}{C - x}$."
                },
                {
                    "id": "ode1-prob-9",
                    "difficulty": "Hard",
                    "difficultyLabel": "Tier 3 • Honors Challenge",
                    "title": "Clairaut's Equation & Singular Parabolic Envelope",
                    "statement": "Find both the general solution and the singular solution of Clairaut's equation:<br>$$y = x \\frac{dy}{dx} - \\frac{1}{4}\\left(\\frac{dy}{dx}\\right)^2$$<br>Show that the singular solution is a parabola and verify that it is tangent to every member of the general solution.",
                    "solution": r"<b>Step 1: Identify Clairaut form</b><br>With $p = y'$, the equation is $y = xp - \frac{1}{4}p^2$, where $f(p) = -\frac{1}{4}p^2$.<br><br><b>Step 2: Differentiate with respect to $x$</b><br>$$p = p + x p' - \frac{1}{2}p p' \implies \left(x - \frac{1}{2}p\right) \frac{dp}{dx} = 0$$<br><br><b>Step 3: General solution branch</b><br>$\frac{dp}{dx} = 0 \implies p = C$. Substituting into the original equation yields the general family of straight lines:<br>$$y = C x - \frac{1}{4} C^2$$<br><br><b>Step 4: Singular solution branch (envelope)</b><br>Setting $x - \frac{1}{2}p = 0 \implies p = 2x$.<br>Substitute $p = 2x$ into the ODE:<br>$$y = x(2x) - \frac{1}{4}(2x)^2 = 2x^2 - x^2 = x^2$$Thus the singular solution is the parabola $y = x^2$.<br><br><b>Step 5: Tangency verification</b><br>Find the intersection of the line $y = Cx - C^2/4$ and the parabola $y = x^2$:<br>$$x^2 = Cx - \frac{1}{4}C^2 \implies x^2 - Cx + \frac{1}{4}C^2 = 0 \implies \left(x - \frac{C}{2}\right)^2 = 0$$The discriminant is zero, confirming that every line in the family intersects the parabola at exactly one point $x = C/2$ with identical slope $y' = 2(C/2) = C$, proving tangency everywhere!",
                    "answer": r"General solution: $y = Cx - \frac{1}{4}C^2$ (family of tangent lines). Singular solution: $y = x^2$ (parabolic envelope)."
                }
            ]
        },

        # UNIT 4
        {
            "unitNumber": 4,
            "title": "Modeling with First-Order Differential Equations",
            "leadSummary": "Physical and biological formulation of first-order differential equations: radioactive decay, Newton's law of cooling with time-dependent ambient variations, cascading mixing tank balances, logistic population growth with harvesting bifurcation, falling bodies under linear and quadratic aerodynamic drag, and Cartesian and polar orthogonal trajectories.",
            "sections": [
                {
                    "id": "u4-sec1",
                    "secNumber": "4.1",
                    "title": "Exponential Growth, Decay & Newton's Law of Cooling",
                    "content": r"""
<h4>1. Law of Exponential Growth and Decay</h4>
<p>When the rate of change of a physical quantity $N(t)$ is directly proportional to the amount currently present, it obeys the foundational differential equation:</p>
<div class="math-display">
$$\frac{dN}{dt} = k N, \quad N(0) = N_0 \implies N(t) = N_0 e^{kt}$$
</div>
<p>If $k > 0$, the process represents exponential growth (e.g., unconstrained bacterial colonies, continuous compound interest). If $k < 0$, writing $k = -\lambda$ ($\lambda > 0$) models exponential decay (e.g., radioactive isotopes). The <strong>half-life</strong> $t_{1/2}$ is the time required for half the original atoms to decay:</p>
<div class="math-display">
$$N(t_{1/2}) = \frac{N_0}{2} = N_0 e^{-\lambda t_{1/2}} \implies t_{1/2} = \frac{\ln 2}{\lambda}$$
</div>

<h4>2. Newton's Law of Cooling/Warming</h4>
<p>Newton's empirical law states that the time rate of heat loss of a body is proportional to the difference in temperatures between the body and its surroundings:</p>
<div class="math-display">
$$\frac{dT}{dt} = -k (T - T_m(t)), \quad k > 0$$
</div>
<p>where $T(t)$ is the temperature of the object and $T_m(t)$ is the ambient surrounding temperature. If $T_m$ is constant, this is a separable equation yielding:</p>
<div class="math-display">
$$T(t) = T_m + (T_0 - T_m) e^{-kt}$$
</div>
<p>If $T_m(t)$ varies dynamically with time (e.g., daily solar oscillations $T_m(t) = T_0 + A \sin(\omega t)$), the equation is solved as a first-order linear ODE via integrating factor $\mu(t) = e^{kt}$.</p>
"""
                },
                {
                    "id": "u4-sec2",
                    "secNumber": "4.2",
                    "title": "Mixing Tank Balances & Logistic Harvesting Bifurcation",
                    "content": r"""
<h4>1. Principle of Mass Balance in Well-Stirred Mixing Tanks</h4>
<p>Consider a tank containing volume $V(t)$ of liquid into which a solute (e.g., salt) is pumped. Let $Q(t)$ denote the mass of solute in the tank at time $t$. The conservation of mass requires:</p>
<div class="math-display">
$$\frac{dQ}{dt} = \text{Rate of Input } (R_{\text{in}}) - \text{Rate of Output } (R_{\text{out}})$$
</div>
<p>Let fluid enter at volumetric rate $r_{\text{in}}$ with concentration $c_{\text{in}}$, and leave at volumetric rate $r_{\text{out}}$ with uniform concentration $c_{\text{out}}(t) = \frac{Q(t)}{V(t)}$. Then:</p>
<div class="math-display">
$$R_{\text{in}} = r_{\text{in}} c_{\text{in}}, \qquad R_{\text{out}} = r_{\text{out}} \frac{Q(t)}{V(t)}, \qquad V(t) = V_0 + (r_{\text{in}} - r_{\text{out}}) t$$
</div>
<p>This yields the first-order linear differential equation:</p>
<div class="math-display">
$$\frac{dQ}{dt} + \frac{r_{\text{out}}}{V_0 + (r_{\text{in}} - r_{\text{out}}) t} Q = r_{\text{in}} c_{\text{in}}$$
</div>

<h4>2. Logistic Population Dynamics Under Harvesting</h4>
<p>The Verhulst logistic growth model accounts for resource limitation with carrying capacity $K$ and intrinsic reproductive rate $r$. When subject to a constant harvesting rate $H$ (e.g., commercial fishing), the governing equation is:</p>
<div class="math-display">
$$\frac{dP}{dt} = r P \left(1 - \frac{P}{K}\right) - H = -\frac{r}{K} P^2 + r P - H$$
</div>
<p>The equilibrium populations are given by the roots of the quadratic RHS:</p>
<div class="math-display">
$$P^* = \frac{r \pm \sqrt{r^2 - 4(r/K)H}}{2r/K} = \frac{K}{2} \left[ 1 \pm \sqrt{1 - \frac{4H}{rK}} \right]$$
</div>
<p><strong>Bifurcation Analysis</strong>:</p>
<ul>
  <li>If $H < \frac{rK}{4}$: There are two distinct equilibria $P_1^* < P_2^*$. $P_2^*$ is stable (carrying state) while $P_1^*$ is unstable (threshold extinction boundary).</li>
  <li>If $H = \frac{rK}{4}$: A saddle-node bifurcation occurs at the critical harvesting limit $P^* = K/2$.</li>
  <li>If $H > \frac{rK}{4}$: $\frac{dP}{dt} < 0$ for all $P$, causing catastrophic population collapse to zero in finite time.</li>
</ul>
""",
                    "simulation": "ode1-firstorder-models-sim"
                },
                {
                    "id": "u4-sec3",
                    "secNumber": "4.3",
                    "title": "Falling Bodies Under Air Drag & Orthogonal Trajectories",
                    "content": r"""
<h4>1. Motion of a Falling Body Under Drag</h4>
<p>By Newton's second law, $m \frac{dv}{dt} = \sum F = m g - F_{\text{drag}}$.</p>
<ul>
  <li><strong>Linear Drag (Stokes Regime, Low Reynolds Number)</strong>: $F_{\text{drag}} = k v$.
    $$\frac{dv}{dt} = g - \frac{k}{m} v \implies v(t) = \frac{m g}{k}\left(1 - e^{-(k/m)t}\right) + v_0 e^{-(k/m)t}$$
    The terminal velocity is $v_T = \lim_{t\to\infty} v(t) = \frac{mg}{k}$.
  </li>
  <li><strong>Quadratic Drag (Newtonian Regime, High Reynolds Number)</strong>: $F_{\text{drag}} = k v^2$.
    $$\frac{dv}{dt} = g - \frac{k}{m} v^2 = g\left(1 - \frac{v^2}{v_T^2}\right), \quad \text{where } v_T = \sqrt{\frac{mg}{k}}$$
    Separating variables: $\int \frac{dv}{v_T^2 - v^2} = \frac{g}{v_T^2} dt \implies v(t) = v_T \tanh\left(\frac{g t}{v_T}\right)$ (for $v(0) = 0$).
  </li>
</ul>

<h4>2. Theory of Orthogonal Trajectories</h4>
<p>An <strong>orthogonal trajectory</strong> is a curve that intersects every member of a given family of curves at right angles ($90^\circ$).</p>
<ul>
  <li><strong>Cartesian Coordinates</strong>: Given a family $F(x, y, C) = 0$, differentiate to find the differential equation $\frac{dy}{dx} = f(x, y)$. Since the product of perpendicular slopes is $-1$, the differential equation of the orthogonal family is:
    $$\left(\frac{dy}{dx}\right)_{\text{orth}} = -\frac{1}{f(x, y)}$$
  </li>
  <li><strong>Polar Coordinates</strong>: Given a family $F(r, \theta, C) = 0$, differentiate to find $r \frac{d\theta}{dr} = f(r, \theta)$. The orthogonal family satisfies:
    $$\left(r \frac{d\theta}{dr}\right)_{\text{orth}} = -\frac{1}{f(r, \theta)} \implies \left(\frac{dr}{d\theta}\right)_{\text{orth}} = -r^2 \left(\frac{d\theta}{dr}\right)_{\text{orig}}$$
  </li>
</ul>
"""
                }
            ],
            "problems": [
                {
                    "id": "ode1-prob-10",
                    "difficulty": "Easy",
                    "difficultyLabel": "Tier 1 • Foundational",
                    "title": "Newton's Cooling Law for Forensic Time of Death",
                    "statement": "A coroner arrives at a crime scene at 10:00 AM and measures a body's temperature to be $30^\circ\\text{C}$. At 11:00 AM, the temperature has dropped to $28^\circ\\text{C}$. The ambient room temperature is held strictly constant at $20^\circ\\text{C}$. Assuming normal body temperature at death is $37^\circ\\text{C}$, determine the exact time of death.",
                    "solution": r"<b>Step 1: Formulate the cooling model</b><br>$\frac{dT}{dt} = -k(T - T_m)$ with $T_m = 20^\circ\text{C}$.<br>The general solution is $T(t) = 20 + (T(0) - 20) e^{-kt}$.<br>Let $t = 0$ correspond to 10:00 AM, so $T(0) = 30^\circ\text{C}$.<br>$$T(t) = 20 + 10 e^{-kt}$$<br><br><b>Step 2: Determine cooling constant $k$</b><br>At 11:00 AM ($t = 1\text{ hr}$), $T(1) = 28^\circ\text{C}$:<br>$$28 = 20 + 10 e^{-k} \implies 8 = 10 e^{-k} \implies e^{-k} = 0.8 \implies k = -\ln(0.8) \approx 0.22314 \text{ hr}^{-1}$$<br><br><b>Step 3: Solve for time of death $t_d < 0$</b><br>At time of death $t_d$, $T(t_d) = 37^\circ\text{C}$:<br>$$37 = 20 + 10 e^{-k t_d} \implies 17 = 10 e^{-k t_d} \implies e^{-k t_d} = 1.7$$$$-k t_d = \ln(1.7) \implies t_d = -\frac{\ln(1.7)}{k} = -\frac{\ln(1.7)}{-\ln(0.8)} = -\frac{0.53063}{0.22314} \approx -2.378 \text{ hours}$$<br><br><b>Step 4: Convert to clock time</b><br>$2.378\text{ hours} \approx 2\text{ hours and } 23\text{ minutes}$ prior to 10:00 AM.<br>Subtracting from 10:00 AM yields approximately 7:37 AM.",
                    "answer": r"Estimated time of death: approximately 7:37 AM ($t_d \approx -2.38\text{ hr}$)."
                },
                {
                    "id": "ode1-prob-11",
                    "difficulty": "Medium",
                    "difficultyLabel": "Tier 2 • Analytical University Exam",
                    "title": "Cascading Variable Volume Mixing Tank Problem",
                    "statement": "A tank initially holds $100\\text{ gallons}$ of pure water. Brine containing $2\\text{ lb/gal}$ of salt flows into the tank at $5\\text{ gal/min}$, and the well-stirred mixture flows out at $3\\text{ gal/min}$. Find the amount of salt in the tank at any time $t$, and calculate the exact salt concentration when the tank reaches $200\\text{ gallons}$.",
                    "solution": r"<b>Step 1: Formulate the balance equation</b><br>Initial conditions: $V_0 = 100\text{ gal}$, $Q(0) = 0\text{ lb}$.<br>Flow rates: $r_{\text{in}} = 5\text{ gal/min}$, $c_{\text{in}} = 2\text{ lb/gal}$, $r_{\text{out}} = 3\text{ gal/min}$.<br>Volume at time $t$: $V(t) = 100 + (5 - 3)t = 100 + 2t\text{ gallons}$.<br>The differential equation for salt mass $Q(t)$ is:<br>$$\frac{dQ}{dt} = R_{\text{in}} - R_{\text{out}} = (5)(2) - 3 \frac{Q}{100 + 2t} \implies \frac{dQ}{dt} + \frac{3}{100 + 2t} Q = 10$$<br><br><b>Step 2: Integrating factor</b><br>$$\mu(t) = \exp\left(\int \frac{3}{100 + 2t} dt\right) = \exp\left(\frac{3}{2} \ln(100 + 2t)\right) = (100 + 2t)^{3/2}$$<br><br><b>Step 3: Solve for $Q(t)$</b><br>$$\frac{d}{dt}\left[ Q(t) (100 + 2t)^{3/2} \right] = 10 (100 + 2t)^{3/2}$$Integrating both sides:<br>$$Q(t) (100 + 2t)^{3/2} = 10 \frac{(100 + 2t)^{5/2}}{\frac{5}{2} \cdot 2} + C = 2(100 + 2t)^{5/2} + C$$Dividing by $(100 + 2t)^{3/2}$:<br>$$Q(t) = 2(100 + 2t) + C(100 + 2t)^{-3/2}$$<br><br><b>Step 4: Initial condition & concentration calculation</b><br>At $t = 0, Q(0) = 0$: $0 = 2(100) + C(100)^{-3/2} \implies C = -200 \times 1000 = -200000$.<br>The tank reaches $200\text{ gallons}$ when $100 + 2t = 200 \implies t = 50\text{ min}$.<br>$$Q(50) = 2(200) - 200000(200)^{-3/2} = 400 - \frac{200000}{2828.43} = 400 - 70.71 = 329.29\text{ lbs}$$The concentration is $c(50) = \frac{329.29\text{ lb}}{200\text{ gal}} \approx 1.646\text{ lb/gal}$.",
                    "answer": r"$Q(t) = 2(100 + 2t) - 200000(100 + 2t)^{-3/2}\text{ lbs}$. Concentration at $V = 200\text{ gal}$: $\approx 1.65\text{ lb/gal}$."
                },
                {
                    "id": "ode1-prob-12",
                    "difficulty": "Hard",
                    "difficultyLabel": "Tier 3 • Honors Challenge",
                    "title": "Self-Orthogonal Family of Confocal Parabolas",
                    "statement": "Prove that the family of confocal parabolas having focus at the origin and axis along the $x$-axis:<br>$$y^2 = 4a(x + a)$$<br>is <b>self-orthogonal</b> (that is, its orthogonal trajectories are identical to the original family with an altered parameter).",
                    "solution": r"<b>Step 1: Obtain the differential equation of the given family</b><br>Given $y^2 = 4ax + 4a^2$. Differentiate with respect to $x$:<br>$$2y \frac{dy}{dx} = 4a \implies a = \frac{1}{2} y y' = \frac{1}{2} y p \quad \left(p = \frac{dy}{dx}\right)$$<br><br><b>Step 2: Eliminate the parameter $a$</b><br>Substitute $a = \frac{1}{2}yp$ into $y^2 = 4ax + 4a^2$:<br>$$y^2 = 4\left(\frac{1}{2}yp\right)x + 4\left(\frac{1}{2}yp\right)^2 = 2xyp + y^2 p^2$$Divide by $y \neq 0$:<br>$$y = 2xp + yp^2 \implies y(1 - p^2) - 2xp = 0 \implies \frac{dy}{dx} \text{ satisfies } y\left[1 - \left(\frac{dy}{dx}\right)^2\right] = 2x \frac{dy}{dx}$$<br><br><b>Step 3: Replace $\frac{dy}{dx}$ with $-\frac{dx}{dy}$ for the orthogonal family</b><br>For the orthogonal trajectories, replace $p = \frac{dy}{dx}$ with $-\frac{1}{p} = -\frac{dx}{dy}$:<br>$$y\left[ 1 - \left(-\frac{1}{p}\right)^2 \right] = 2x \left(-\frac{1}{p}\right) \implies y\left(1 - \frac{1}{p^2}\right) = -\frac{2x}{p}$$Multiply the entire equation by $-p^2$:<br>$$-y(p^2 - 1) = 2xp \implies y(1 - p^2) - 2xp = 0$$<br><br><b>Conclusion:</b><br>The differential equation for the orthogonal trajectories is algebraically <i>identical</i> to the original differential equation! Therefore, the family is self-orthogonal.",
                    "answer": r"Proven. The differential equation $y(p^2 - 1) + 2xp = 0$ is invariant under the transformation $p \mapsto -1/p$, proving self-orthogonality."
                }
            ]
        },

        # UNIT 5
        {
            "unitNumber": 5,
            "title": "Solution of Higher-Order Linear Equations: Wronskian, Solution Space & Reduction of Order",
            "leadSummary": "Rigorous algebraic and analytic theory of n-th order linear differential equations: linear differential operators, the principle of superposition, linear independence, the Wronskian determinant, Abel's identity for the Wronskian, fundamental solution sets, and d'Alembert's reduction of order formula.",
            "sections": [
                {
                    "id": "u5-sec1",
                    "secNumber": "5.1",
                    "title": "The Linear Differential Operator & Superposition Principle",
                    "content": r"""
<h4>1. The General Linear $n$-th Order Differential Equation</h4>
<p>The standard normalized $n$-th order linear differential equation is expressed as:</p>
<div class="math-display">
$$L[y] \equiv \frac{d^ny}{dx^n} + P_{n-1}(x) \frac{d^{n-1}y}{dx^{n-1}} + \dots + P_1(x) \frac{dy}{dx} + P_0(x) y = g(x)$$
</div>
<p>where $P_0, \dots, P_{n-1}$ and $g$ are continuous on an interval $I \subseteq \mathbb{R}$. The operator $L: C^n(I) \to C(I)$ is a <strong>linear operator</strong>, satisfying:</p>
<div class="math-display">
$$L[c_1 y_1 + c_2 y_2] = c_1 L[y_1] + c_2 L[y_2] \quad \forall c_1, c_2 \in \mathbb{R}, \, y_1, y_2 \in C^n(I)$$
</div>

<h4>2. The Principle of Superposition</h4>
<div class="math-display">
$$\mathbf{\text{Theorem (Superposition): If } y_1(x), y_2(x), \dots, y_k(x) \text{ are solutions to the homogeneous equation } L[y] = 0,}}$$
</div>
<p>then any linear combination $y(x) = c_1 y_1(x) + c_2 y_2(x) + \dots + c_k y_k(x)$ is also a solution to $L[y] = 0$. Consequently, the solution space of the homogeneous equation is a vector subspace of $C^n(I)$, denoted by $\ker(L)$.</p>

<h4>3. Dimension of the Homogeneous Solution Space</h4>
<p>By the fundamental existence and uniqueness theorem for linear IVPs, for any fixed $x_0 \in I$, the mapping that associates each solution $y \in \ker(L)$ with its initial vector $(y(x_0), y'(x_0), \dots, y^{(n-1)}(x_0)) \in \mathbb{R}^n$ is a linear isomorphism. Thus, the solution space $\ker(L)$ has <strong>dimension exactly $n$</strong>.</p>
"""
                },
                {
                    "id": "u5-sec2",
                    "secNumber": "5.2",
                    "title": "The Wronskian Determinant & Abel's Formula",
                    "content": r"""
<h4>1. Definition of the Wronskian Determinant</h4>
<p>Let $y_1, y_2, \dots, y_n$ be $n$ functions that are $(n-1)$-times differentiable on an interval $I$. The <strong>Wronskian</strong> of these functions is the determinant:</p>
<div class="math-display">
$$W(y_1, y_2, \dots, y_n)(x) = \begin{vmatrix}
y_1(x) & y_2(x) & \dots & y_n(x) \\
y_1'(x) & y_2'(x) & \dots & y_n'(x) \\
\vdots & \vdots & \ddots & \vdots \\
y_1^{(n-1)}(x) & y_2^{(n-1)}(x) & \dots & y_n^{(n-1)}(x)
\end{vmatrix}$$
</div>

<h4>2. The Wronskian Test for Linear Independence</h4>
<div class="math-display">
$$\mathbf{\text{Theorem: Let } y_1, \dots, y_n \text{ be } n \text{ solutions to } L[y] = 0 \text{ on } I. \text{ Then they are linearly independent on } I}$$
</div>
<p>if and only if $W(y_1, \dots, y_n)(x) \neq 0$ for all $x \in I$. Furthermore, the Wronskian is either identically zero everywhere on $I$ or never zero anywhere on $I$.</p>

<h4>3. Proof of Abel's Identity (Abel's Formula)</h4>
<p>Consider the second-order homogeneous equation $y'' + P(x)y' + Q(x)y = 0$, with solutions $y_1, y_2$. The Wronskian is $W(x) = y_1 y_2' - y_1' y_2$. Differentiating with respect to $x$:</p>
<div class="math-display">
$$W'(x) = (y_1' y_2' + y_1 y_2'') - (y_1'' y_2 + y_1' y_2') = y_1 y_2'' - y_1'' y_2$$
</div>
<p>Since $y_1$ and $y_2$ satisfy the ODE, $y_i'' = -P(x)y_i' - Q(x)y_i$. Substituting:</p>
<div class="math-display">
$$W'(x) = y_1(-P y_2' - Q y_2) - (-P y_1' - Q y_1) y_2 = -P(x)(y_1 y_2' - y_1' y_2) = -P(x) W(x)$$
</div>
<p>This is a first-order separable differential equation in $W(x)$: $\frac{dW}{W} = -P(x)dx$. Integrating from $x_0$ to $x$ yields <strong>Abel's formula</strong>:</p>
<div class="math-display">
$$W(x) = W(x_0) \exp\left(-\int_{x_0}^x P(t) dt\right)$$
</div>
<p>Since the exponential function never vanishes, $W(x)$ is zero everywhere if $W(x_0) = 0$, and non-zero everywhere if $W(x_0) \neq 0$.</p>
""",
                    "simulation": "ode1-wronskian-sim"
                },
                {
                    "id": "u5-sec3",
                    "secNumber": "5.3",
                    "title": "Reduction of Order (d'Alembert's Method)",
                    "content": r"""
<h4>1. Theoretical Basis for Reduction of Order</h4>
<p>If one non-trivial solution $y_1(x) \neq 0$ of the homogeneous second-order linear ODE:</p>
<div class="math-display">
$$y'' + P(x) y' + Q(x) y = 0$$
</div>
<p>is already known, a second linearly independent solution $y_2(x)$ can always be found by setting $y_2(x) = v(x) y_1(x)$, where $v(x)$ is a non-constant function to be determined.</p>

<h4>2. Derivation of the Reduction Formula</h4>
<p>Differentiating $y_2(x) = v y_1$:</p>
<div class="math-display">
$$y_2' = v' y_1 + v y_1', \qquad y_2'' = v'' y_1 + 2 v' y_1' + v y_1''$$
</div>
<p>Substituting into the ODE:</p>
<div class="math-display">
$$(v'' y_1 + 2 v' y_1' + v y_1'') + P(x)(v' y_1 + v y_1') + Q(x)(v y_1) = 0$$
</div>
<p>Regrouping by derivatives of $v$:</p>
<div class="math-display">
$$y_1 v'' + (2 y_1' + P y_1) v' + [y_1'' + P y_1' + Q y_1] v = 0$$
</div>
<p>Since $y_1$ is a solution, the bracketed coefficient of $v$ vanishes identically! Setting $w = v'$ (whence $w' = v''$) reduces the equation to a <strong>first-order separable ODE</strong> for $w$:</p>
<div class="math-display">
$$y_1 w' + (2 y_1' + P y_1) w = 0 \implies \frac{w'}{w} = -2 \frac{y_1'}{y_1} - P(x)$$
</div>
<p>Integrating with respect to $x$:</p>
<div class="math-display">
$$\ln |w| = -2 \ln |y_1| - \int P(x) dx \implies w(x) = v'(x) = \frac{e^{-\int P(x) dx}}{y_1(x)^2}$$
</div>
<p>Integrating once more gives $v(x) = \int \frac{e^{-\int P(x) dx}}{y_1(x)^2} dx$, yielding the universal <strong>reduction of order formula</strong>:</p>
<div class="math-display">
$$y_2(x) = y_1(x) \int \frac{\exp\left(-\int P(x) dx\right)}{[y_1(x)]^2} dx$$
</div>
"""
                }
            ],
            "problems": [
                {
                    "id": "ode1-prob-13",
                    "difficulty": "Easy",
                    "difficultyLabel": "Tier 1 • Foundational",
                    "title": "Wronskian & Linear Independence of Polynomial Functions",
                    "statement": "Compute the Wronskian of the three functions $y_1(x) = 1, y_2(x) = x, y_3(x) = x^2$. Deduce whether they form a fundamental set of solutions for a third-order linear ODE on $(-\\infty, \\infty)$, and construct the ODE they satisfy.",
                    "solution": r"<b>Step 1: Construct the Wronskian determinant</b><br>$$W(1, x, x^2) = \begin{vmatrix} 1 & x & x^2 \\ 0 & 1 & 2x \\ 0 & 0 & 2 \end{vmatrix}$$<br><br><b>Step 2: Evaluate the determinant</b><br>Since the matrix is upper triangular, its determinant is simply the product of its diagonal entries:<br>$$W(x) = 1 \cdot 1 \cdot 2 = 2$$<br><br><b>Step 3: Linear independence and ODE construction</b><br>Since $W(x) = 2 \neq 0$ for all $x \in \mathbb{R}$, the functions are linearly independent on $(-\infty, \infty)$ and form a fundamental solution set.<br>Differentiating $y_3(x) = x^2$ three times gives $\frac{d^3(x^2)}{dx^3} = 0$. Likewise for $1$ and $x$. Thus, the third-order ODE is:<br>$$y''' = 0$$",
                    "answer": r"$W(x) = 2 \neq 0$ everywhere, confirming linear independence. The governing ODE is $y''' = 0$."
                },
                {
                    "id": "ode1-prob-14",
                    "difficulty": "Medium",
                    "difficultyLabel": "Tier 2 • Analytical University Exam",
                    "title": "Reduction of Order for Variable-Coefficient Equation",
                    "statement": "Given that $y_1(x) = x$ is a solution to the differential equation:<br>$$x^2 y'' + 2x y' - 2y = 0, \\quad x > 0$$<br>use the reduction of order method to find a second linearly independent solution $y_2(x)$ and write the general solution.",
                    "solution": r"<b>Step 1: Put the ODE into standard normalized form</b><br>Divide by $x^2$:<br>$$y'' + \frac{2}{x} y' - \frac{2}{x^2} y = 0 \implies P(x) = \frac{2}{x}$$<br><br><b>Step 2: Apply the reduction of order formula</b><br>Here $y_1(x) = x$ and $e^{-\int P(x)dx} = e^{-\int (2/x) dx} = e^{-2 \ln x} = \frac{1}{x^2}$.<br>$$y_2(x) = y_1(x) \int \frac{e^{-\int P(x)dx}}{[y_1(x)]^2} dx = x \int \frac{1/x^2}{x^2} dx = x \int x^{-4} dx$$<br><br><b>Step 3: Evaluate the integral</b><br>$$\int x^{-4} dx = -\frac{1}{3} x^{-3}$$Dropping the multiplicative constant $-1/3$ (since any non-zero multiple is linearly independent):<br>$$y_2(x) = x \cdot x^{-3} = x^{-2} = \frac{1}{x^2}$$<br><br><b>Step 4: Verify linear independence</b><br>$$W(y_1, y_2) = \begin{vmatrix} x & x^{-2} \\ 1 & -2x^{-3} \end{vmatrix} = x(-2x^{-3}) - (x^{-2})(1) = -2x^{-2} - x^{-2} = -3x^{-2} \neq 0 \quad (x > 0)$$<br><br><b>Step 5: General solution</b><br>$$y(x) = c_1 x + c_2 x^{-2}$$",
                    "answer": r"$y_2(x) = x^{-2}$. General solution: $y(x) = c_1 x + \frac{c_2}{x^2}$."
                },
                {
                    "id": "ode1-prob-15",
                    "difficulty": "Hard",
                    "difficultyLabel": "Tier 3 • Honors Challenge",
                    "title": "Abel's Formula Applied to Legendre's Equation",
                    "statement": "Legendre's differential equation of order $n$ is given by:<br>$$(1 - x^2) y'' - 2x y' + n(n + 1) y = 0, \\quad -1 < x < 1$$<br>Use Abel's identity to prove that the Wronskian of any two linearly independent solutions satisfies $W(x) = \\frac{C}{1 - x^2}$, and explain why $x = \\pm 1$ represent singular points.",
                    "solution": r"<b>Step 1: Normalize Legendre's equation</b><br>Divide by $(1 - x^2)$:<br>$$y'' - \frac{2x}{1 - x^2} y' + \frac{n(n + 1)}{1 - x^2} y = 0$$Here $P(x) = -\frac{2x}{1 - x^2}$.<br><br><b>Step 2: Apply Abel's formula</b><br>$$\int P(x) dx = \int -\frac{2x}{1 - x^2} dx = \int \frac{d(1 - x^2)}{1 - x^2} = \ln|1 - x^2| = \ln(1 - x^2) \quad (|x| < 1)$$$$-\int P(x) dx = -\ln(1 - x^2) = \ln\left(\frac{1}{1 - x^2}\right)$$By Abel's formula:<br>$$W(x) = C \exp\left(-\int P(x) dx\right) = C \exp\left(\ln\left(\frac{1}{1 - x^2}\right)\right) = \frac{C}{1 - x^2}$$<br><br><b>Step 3: Singular point interpretation</b><br>As $x \to \pm 1$, the denominator $1 - x^2 \to 0$, causing $W(x) \to \infty$ (unless $C = 0$). This divergence reflects the fact that $x = \pm 1$ are regular singular points of Legendre's equation, where the coefficient of $y''$ vanishes and solutions exhibit logarithmic or branch-cut singularities unless $n$ is an integer (yielding the polynomial solutions $P_n(x)$).",
                    "answer": r"Proven: $W(x) = \frac{C}{1 - x^2}$. As $x \to \pm 1$, $W(x)$ diverges, identifying $x = \pm 1$ as singular points of the differential operator."
                }
            ]
        },

        # UNIT 6
        {
            "unitNumber": 6,
            "title": "Homogeneous Linear Equations with Constant Coefficients & Cauchy-Euler Equations",
            "leadSummary": "Complete algebraic theory of homogeneous equations with constant coefficients: characteristic polynomials, distinct real roots, repeated root multipliers, complex conjugate roots and Euler's harmonic representation, and Cauchy-Euler (equidimensional) equations via the logarithmic transformation x = e^t.",
            "sections": [
                {
                    "id": "u6-sec1",
                    "secNumber": "6.1",
                    "title": "Characteristic Polynomials & Roots Classification",
                    "content": r"""
<h4>1. The Second-Order Constant Coefficient Equation</h4>
<p>Consider the homogeneous linear ODE with constant real coefficients:</p>
<div class="math-display">
$$a y'' + b y' + c y = 0, \quad a \neq 0$$
</div>
<p>Assuming a trial solution of exponential form $y(x) = e^{rx}$, we compute $y' = r e^{rx}$ and $y'' = r^2 e^{rx}$. Substituting into the ODE:</p>
<div class="math-display">
$$(a r^2 + b r + c) e^{rx} = 0$$
</div>
<p>Since $e^{rx} \neq 0$ for all real $x$, $r$ must satisfy the <strong>characteristic (auxiliary) equation</strong>:</p>
<div class="math-display">
$$a r^2 + b r + c = 0 \implies r = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
</div>

<h4>2. The Three Root Regimes</h4>
<ul>
  <li><strong>Case 1: Real and Distinct Roots ($\Delta = b^2 - 4ac > 0$)</strong><br>
    The roots $r_1 \neq r_2$ are real numbers. Two linearly independent solutions are $y_1 = e^{r_1 x}$ and $y_2 = e^{r_2 x}$. The general solution is:
    $$y(x) = c_1 e^{r_1 x} + c_2 e^{r_2 x}$$
  </li>
  <li><strong>Case 2: Real and Repeated Roots ($\Delta = b^2 - 4ac = 0$)</strong><br>
    There is a single root of multiplicity two: $r = -b / (2a)$. One solution is $y_1 = e^{rx}$. Using reduction of order, the second independent solution is $y_2 = x e^{rx}$. The general solution is:
    $$y(x) = (c_1 + c_2 x) e^{rx}$$
  </li>
  <li><strong>Case 3: Complex Conjugate Roots ($\Delta = b^2 - 4ac < 0$)</strong><br>
    The roots are $r = \alpha \pm i \beta$, where $\alpha = -b/(2a)$ and $\beta = \frac{\sqrt{4ac - b^2}}{2a} > 0$. Using Euler's formula $e^{(\alpha \pm i\beta)x} = e^{\alpha x}(\cos\beta x \pm i \sin\beta x)$, the real linearly independent fundamental solutions are $y_1 = e^{\alpha x} \cos(\beta x)$ and $y_2 = e^{\alpha x} \sin(\beta x)$. The general solution is:
    $$y(x) = e^{\alpha x} \left[ c_1 \cos(\beta x) + c_2 \sin(\beta x) \right] = R e^{\alpha x} \cos(\beta x - \delta)$$
  </li>
</ul>
""",
                    "simulation": "ode1-aux-roots-sim"
                },
                {
                    "id": "u6-sec2",
                    "secNumber": "6.2",
                    "title": "Higher-Order Constant Coefficient Equations ($n$-th Order)",
                    "content": r"""
<h4>1. Generalization to $n$-th Order Equations</h4>
<p>For an $n$-th order linear ODE $a_n y^{(n)} + a_{n-1} y^{(n-1)} + \dots + a_1 y' + a_0 y = 0$, the characteristic polynomial is:</p>
<div class="math-display">
$$P(r) = a_n r^n + a_{n-1} r^{n-1} + \dots + a_1 r + a_0 = 0$$
</div>
<p>By the Fundamental Theorem of Algebra, $P(r)$ has exactly $n$ complex roots (counting multiplicities):</p>
<ul>
  <li>Each real root $r$ of multiplicity $k$ contributes $k$ linearly independent solutions:
    $$e^{rx}, \quad x e^{rx}, \quad x^2 e^{rx}, \quad \dots, \quad x^{k-1} e^{rx}$$
  </li>
  <li>Each complex conjugate pair $\alpha \pm i\beta$ of multiplicity $k$ contributes $2k$ linearly independent solutions:
    $$\begin{aligned}
    e^{\alpha x} \cos\beta x, \quad x e^{\alpha x} \cos\beta x, \quad \dots, \quad x^{k-1} e^{\alpha x} \cos\beta x \\
    e^{\alpha x} \sin\beta x, \quad x e^{\alpha x} \sin\beta x, \quad \dots, \quad x^{k-1} e^{\alpha x} \sin\beta x
    \end{aligned}$$
  </li>
</ul>
<p>The sum of all these solutions multiplied by arbitrary constants $c_1, \dots, c_n$ forms the complete general solution.</p>
"""
                },
                {
                    "id": "u6-sec3",
                    "secNumber": "6.3",
                    "title": "Cauchy-Euler (Equidimensional) Differential Equations",
                    "content": r"""
<h4>1. Standard Form of Cauchy-Euler Equations</h4>
<p>A linear differential equation of the form:</p>
<div class="math-display">
$$a_n x^n \frac{d^ny}{dx^n} + a_{n-1} x^{n-1} \frac{d^{n-1}y}{dx^{n-1}} + \dots + a_1 x \frac{dy}{dx} + a_0 y = g(x)$$
</div>
<p>where the power of $x$ matches the order of the derivative in each term, is called a <strong>Cauchy-Euler (or equidimensional) equation</strong>.</p>

<h4>2. Second-Order Homogeneous Cauchy-Euler Equation</h4>
<p>Consider $a x^2 y'' + b x y' + c y = 0$ for $x > 0$. We seek solutions of the form $y = x^m$. Differentiating:</p>
<div class="math-display">
$$y' = m x^{m-1}, \qquad y'' = m(m-1) x^{m-2}$$
</div>
<p>Substituting into the ODE:</p>
<div class="math-display">
$$a x^2 [m(m-1) x^{m-2}] + b x [m x^{m-1}] + c x^m = 0 \implies [a m(m - 1) + b m + c] x^m = 0$$
</div>
<p>This yields the <strong>indicial (auxiliary) equation</strong>:</p>
<div class="math-display">
$$a m^2 + (b - a) m + c = 0$$
</div>

<h4>3. Three Cases of Solutions for Cauchy-Euler Equations</h4>
<ul>
  <li><strong>Distinct Real Roots ($m_1 \neq m_2$)</strong>: $y(x) = c_1 x^{m_1} + c_2 x^{m_2}$.</li>
  <li><strong>Repeated Real Root ($m_1 = m_2 = m$)</strong>: The second solution is obtained by logarithmic scaling:
    $$y(x) = x^m (c_1 + c_2 \ln x)$$
  </li>
  <li><strong>Complex Conjugate Roots ($m = \alpha \pm i \beta$)</strong>: Using $x^{\alpha \pm i\beta} = x^\alpha e^{\pm i \beta \ln x} = x^\alpha [\cos(\beta \ln x) \pm i \sin(\beta \ln x)]$:
    $$y(x) = x^\alpha \left[ c_1 \cos(\beta \ln x) + c_2 \sin(\beta \ln x) \right]$$
  </li>
</ul>
"""
                }
            ],
            "problems": [
                {
                    "id": "ode1-prob-16",
                    "difficulty": "Easy",
                    "difficultyLabel": "Tier 1 • Foundational",
                    "title": "Fourth-Order Constant Coefficient Initial Value Problem",
                    "statement": "Find the general solution of the fourth-order differential equation:<br>$$\\frac{d^4y}{dx^4} - 16y = 0$$",
                    "solution": r"<b>Step 1: Write the characteristic equation</b><br>$$r^4 - 16 = 0$$<br><br><b>Step 2: Factor the polynomial</b><br>$$(r^2 - 4)(r^2 + 4) = 0 \implies (r - 2)(r + 2)(r^2 + 4) = 0$$<br><br><b>Step 3: Identify the roots</b><br>The four roots are:<br>$$r_1 = 2, \quad r_2 = -2, \quad r_{3,4} = \pm 2i$$<br><br><b>Step 4: Formulate the fundamental solutions</b><br>For real roots: $y_1 = e^{2x}, y_2 = e^{-2x}$.<br>For imaginary roots $\alpha = 0, \beta = 2$: $y_3 = \cos(2x), y_4 = \sin(2x)$.<br><br><b>Step 5: Write the general solution</b><br>$$y(x) = c_1 e^{2x} + c_2 e^{-2x} + c_3 \cos(2x) + c_4 \sin(2x)$$",
                    "answer": r"$y(x) = c_1 e^{2x} + c_2 e^{-2x} + c_3 \cos(2x) + c_4 \sin(2x)$ (or $A \cosh(2x) + B \sinh(2x) + c_3 \cos(2x) + c_4 \sin(2x)$)."
                },
                {
                    "id": "ode1-prob-17",
                    "difficulty": "Medium",
                    "difficultyLabel": "Tier 2 • Analytical University Exam",
                    "title": "Cauchy-Euler Equation with Complex Conjugate Roots",
                    "statement": "Solve the Cauchy-Euler boundary value problem:<br>$$x^2 y'' - 3x y' + 13 y = 0, \\quad y(1) = 2, \\quad y(e^{\\pi/6}) = 0, \\quad x > 0$$",
                    "solution": r"<b>Step 1: Set up the indicial equation</b><br>With $y = x^m$, the equation becomes:<br>$$m(m - 1) - 3m + 13 = 0 \implies m^2 - 4m + 13 = 0$$<br><br><b>Step 2: Solve for $m$</b><br>$$m = \frac{4 \pm \sqrt{16 - 52}}{2} = \frac{4 \pm \sqrt{-36}}{2} = 2 \pm 3i$$Here $\alpha = 2, \beta = 3$.<br><br><b>Step 3: General solution</b><br>$$y(x) = x^2 \left[ c_1 \cos(3 \ln x) + c_2 \sin(3 \ln x) \right]$$<br><br><b>Step 4: Apply boundary conditions</b><br>At $x = 1$ ($\ln 1 = 0$):<br>$$y(1) = 1^2 [c_1 \cos(0) + c_2 \sin(0)] = c_1 = 2$$At $x = e^{\pi/6}$ ($\ln(e^{\pi/6}) = \pi/6$):<br>$$y(e^{\pi/6}) = (e^{\pi/6})^2 \left[ 2 \cos\left(3 \cdot \frac{\pi}{6}\right) + c_2 \sin\left(3 \cdot \frac{\pi}{6}\right) \right] = 0$$$$e^{\pi/3} \left[ 2 \cos\left(\frac{\pi}{2}\right) + c_2 \sin\left(\frac{\pi}{2}\right) \right] = 0 \implies e^{\pi/3} [2(0) + c_2(1)] = 0 \implies c_2 = 0$$<br><br><b>Step 5: Final solution</b><br>$$y(x) = 2x^2 \cos(3 \ln x)$$",
                    "answer": r"$y(x) = 2x^2 \cos(3 \ln x)$."
                },
                {
                    "id": "ode1-prob-18",
                    "difficulty": "Hard",
                    "difficultyLabel": "Tier 3 • Honors Challenge",
                    "title": "Critical Damping & Energy Minimization in a RLC Oscillator",
                    "statement": "An unforced RLC circuit is described by $L q'' + R q' + \\frac{1}{C} q = 0$. For fixed $L = 1\\text{ H}$ and $C = 0.25\\text{ F}$, determine the critical damping resistance $R_{\\text{crit}}$. If the circuit starts with initial charge $q(0) = Q_0$ and zero current $q'(0) = 0$, solve the critical IVP and prove that the charge never crosses zero for $t > 0$.",
                    "solution": r"<b>Step 1: Indicial equation and critical damping</b><br>Characteristic equation: $L r^2 + R r + \frac{1}{C} = 0 \implies r^2 + R r + 4 = 0$.<br>The discriminant is $\Delta = R^2 - 4(1)(4) = R^2 - 16$.<br>Critical damping occurs when $\Delta = 0 \implies R_{\\text{crit}} = \sqrt{16} = 4\\,\\Omega$.<br><br><b>Step 2: Repeated root solution</b><br>With $R = 4\\,\\Omega$, the repeated root is $r = -R/(2L) = -4/2 = -2$.<br>The general solution for the charge is:<br>$$q(t) = (c_1 + c_2 t) e^{-2t}$$<br><br><b>Step 3: Apply initial conditions</b><br>$q(0) = Q_0 \implies c_1 = Q_0$.<br>Compute the current (derivative):<br>$$q'(t) = c_2 e^{-2t} - 2(c_1 + c_2 t)e^{-2t} = (c_2 - 2c_1 - 2c_2 t)e^{-2t}$$At $t = 0$: $q'(0) = c_2 - 2c_1 = 0 \implies c_2 = 2c_1 = 2Q_0$.<br>Thus:<br>$$q(t) = Q_0 (1 + 2t) e^{-2t}$$<br><br><b>Step 4: Zero-crossing proof</b><br>For $t > 0$, since $Q_0 > 0$, $1 + 2t > 1 > 0$ and $e^{-2t} > 0$. Thus $q(t) > 0$ for all $t \ge 0$. The charge monotonically decays toward zero as $t \to \infty$ without ever oscillating or crossing zero, proving the defining property of critical damping.",
                    "answer": r"$R_{\text{crit}} = 4\,\Omega$. Solution: $q(t) = Q_0 (1 + 2t) e^{-2t}$. Since $1 + 2t > 0$ for all $t > 0$, $q(t) > 0$ strictly, verifying that the charge never crosses zero."
                }
            ]
        },

        # UNIT 7
        {
            "unitNumber": 7,
            "title": "Non-Homogeneous Linear Equations: Undetermined Coefficients & Variation of Parameters",
            "leadSummary": "Complete theory of non-homogeneous linear differential equations: complementary and particular integrals, the method of undetermined coefficients, the modification rule, differential annihilator operators, and Lagrange's method of variation of parameters for arbitrary continuous forcing.",
            "sections": [
                {
                    "id": "u7-sec1",
                    "secNumber": "7.1",
                    "title": "Structure of the General Solution & Principle of Superposition",
                    "content": r"""
<h4>1. Theorem on the Non-Homogeneous Solution Structure</h4>
<p>Let $L[y] = g(x)$ be an $n$-th order linear differential equation, and let $L[y] = 0$ be its associated homogeneous equation. If $y_p(x)$ is any particular solution of $L[y] = g(x)$, and $\{y_1, y_2, \dots, y_n\}$ is a fundamental solution set of $L[y] = 0$, then the <strong>complete general solution</strong> is:</p>
<div class="math-display">
$$y(x) = y_c(x) + y_p(x) = \sum_{k=1}^n c_k y_k(x) + y_p(x)$$
</div>
<p>where $y_c(x)$ is the <strong>complementary function</strong> and $y_p(x)$ is the <strong>particular integral</strong>.</p>

<h4>2. Extended Superposition for Multiple Forcing Functions</h4>
<p>If $g(x) = g_1(x) + g_2(x) + \dots + g_m(x)$, and $y_{p,i}(x)$ is a particular solution to $L[y] = g_i(x)$ for each $i = 1, \dots, m$, then by linearity of $L$:</p>
<div class="math-display">
$$L[y_{p,1} + \dots + y_{p,m}] = L[y_{p,1}] + \dots + L[y_{p,m}] = g_1(x) + \dots + g_m(x) = g(x)$$
</div>
<p>Hence, the total particular solution is the sum $y_p(x) = \sum_{i=1}^m y_{p,i}(x)$.</p>
"""
                },
                {
                    "id": "u7-sec2",
                    "secNumber": "7.2",
                    "title": "The Method of Undetermined Coefficients & The Annihilator Operator",
                    "content": r"""
<h4>1. Scope and Trial Forms for Undetermined Coefficients</h4>
<p>The method of undetermined coefficients applies to constant-coefficient linear ODEs where the forcing function $g(x)$ is a linear combination of polynomials, exponentials, sines, and cosines:</p>
<table style="width:100%; border-collapse:collapse; margin:1rem 0; font-size:0.9rem;">
  <thead>
    <tr style="border-bottom:1px solid #334155; text-align:left;">
      <th style="padding:0.5rem; color:#38bdf8;">Forcing Term $g(x)$</th>
      <th style="padding:0.5rem; color:#38bdf8;">Trial Form for $y_p(x)$ (Basic)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="border-bottom:1px solid #1e293b;">
      <td style="padding:0.5rem;">Polynomial: $a_m x^m + \dots + a_0$</td>
      <td style="padding:0.5rem;">$A_m x^m + A_{m-1} x^{m-1} + \dots + A_0$</td>
    </tr>
    <tr style="border-bottom:1px solid #1e293b;">
      <td style="padding:0.5rem;">Exponential: $e^{\alpha x}$</td>
      <td style="padding:0.5rem;">$A e^{\alpha x}$</td>
    </tr>
    <tr style="border-bottom:1px solid #1e293b;">
      <td style="padding:0.5rem;">Harmonic: $\sin(\beta x)$ or $\cos(\beta x)$</td>
      <td style="padding:0.5rem;">$A \cos(\beta x) + B \sin(\beta x)$</td>
    </tr>
    <tr style="border-bottom:1px solid #1e293b;">
      <td style="padding:0.5rem;">Product: $x^m e^{\alpha x} \cos(\beta x)$</td>
      <td style="padding:0.5rem;">$x^s e^{\alpha x} [(A_m x^m + \dots + A_0)\cos\beta x + (B_m x^m + \dots + B_0)\sin\beta x]$</td>
    </tr>
  </tbody>
</table>

<h4>2. The Modification Rule</h4>
<p><strong>The Modification Rule</strong>: If any term in the trial form of $y_p(x)$ is a solution of the associated homogeneous equation (i.e., appears in $y_c(x)$), that trial form must be multiplied by $x^s$, where $s$ is the smallest positive integer such that no term in $x^s y_p(x)$ belongs to $y_c(x)$. In other words, $s$ is the multiplicity of the root in the characteristic equation.</p>

<h4>3. The Annihilator Operator Method</h4>
<p>Let $D = \frac{d}{dx}$ denote the differential operator. An operator $A(D)$ is an <strong>annihilator</strong> for $g(x)$ if $A(D)[g(x)] \equiv 0$.</p>
<ul>
  <li>$D^n$ annihilates $1, x, x^2, \dots, x^{n-1}$.</li>
  <li>$(D - \alpha)^n$ annihilates $e^{\alpha x}, x e^{\alpha x}, \dots, x^{n-1} e^{\alpha x}$.</li>
  <li>$[(D - \alpha)^2 + \beta^2]^n$ annihilates $x^k e^{\alpha x}\cos\beta x$ and $x^k e^{\alpha x}\sin\beta x$ for $k = 0, 1, \dots, n-1$.</li>
</ul>
<p>If $L(D)[y] = g(x)$ and $A(D)[g] = 0$, applying $A(D)$ to both sides gives the higher-order homogeneous equation $A(D)L(D)[y] = 0$. Solving this homogeneous equation immediately reveals both $y_c(x)$ and the exact required trial form for $y_p(x)$.</p>
""",
                    "simulation": "ode1-resonance-beats-sim"
                },
                {
                    "id": "u7-sec3",
                    "secNumber": "7.3",
                    "title": "Lagrange's Method of Variation of Parameters",
                    "content": r"""
<h4>1. Motivation and Scope</h4>
<p>The method of undetermined coefficients is restricted to polynomials, exponentials, and sinusoidal forcing. When $g(x)$ is any general continuous function (e.g., $\tan x, \sec x, \frac{1}{x}, \ln x$), <strong>Lagrange's Method of Variation of Parameters</strong> provides a universal, exact integral formula.</p>

<h4>2. Rigorous Derivation for Second-Order Equations</h4>
<p>Consider $y'' + P(x) y' + Q(x) y = g(x)$, with known complementary solution $y_c(x) = c_1 y_1(x) + c_2 y_2(x)$. We replace the constants $c_1, c_2$ with functions $u_1(x), u_2(x)$:</p>
<div class="math-display">
$$y_p(x) = u_1(x) y_1(x) + u_2(x) y_2(x)$$
</div>
<p>Differentiating with respect to $x$:</p>
<div class="math-display">
$$y_p' = (u_1 y_1' + u_2 y_2') + (u_1' y_1 + u_2' y_2)$$
</div>
<p>To avoid second derivatives of $u_1, u_2$, we impose Lagrange's first constraint:</p>
<div class="math-display">
$$u_1'(x) y_1(x) + u_2'(x) y_2(x) = 0 \quad \text{(Constraint 1)}$$
</div>
<p>Then $y_p' = u_1 y_1' + u_2 y_2'$, and differentiating again:</p>
<div class="math-display">
$$y_p'' = u_1' y_1' + u_2' y_2' + u_1 y_1'' + u_2 y_2''$$
</div>
<p>Substituting $y_p, y_p', y_p''$ into $y'' + P y' + Q y = g(x)$:</p>
<div class="math-display">
$$u_1[y_1'' + P y_1' + Q y_1] + u_2[y_2'' + P y_2' + Q y_2] + (u_1' y_1' + u_2' y_2') = g(x)$$
</div>
<p>Since $y_1$ and $y_2$ satisfy the homogeneous equation, the bracketed terms vanish, leaving:</p>
<div class="math-display">
$$u_1'(x) y_1'(x) + u_2'(x) y_2'(x) = g(x) \quad \text{(Constraint 2)}$$
</div>

<h4>3. Solution via Cramer's Rule</h4>
<p>Constraints 1 and 2 form a linear algebraic system for the derivatives $u_1'$ and $u_2'$:</p>
<div class="math-display">
$$\begin{pmatrix} y_1 & y_2 \\ y_1' & y_2' \end{pmatrix} \begin{pmatrix} u_1' \\ u_2' \end{pmatrix} = \begin{pmatrix} 0 \\ g(x) \end{pmatrix}$$
</div>
<p>The coefficient matrix determinant is precisely the Wronskian $W(y_1, y_2)(x)$. By Cramer's Rule:</p>
<div class="math-display">
$$u_1'(x) = -\frac{y_2(x) g(x)}{W(y_1, y_2)(x)}, \qquad u_2'(x) = \frac{y_1(x) g(x)}{W(y_1, y_2)(x)}$$
</div>
<p>Integrating $u_1'$ and $u_2'$ yields the universal particular integral:</p>
<div class="math-display">
$$y_p(x) = -y_1(x) \int \frac{y_2(x) g(x)}{W(y_1, y_2)(x)} dx + y_2(x) \int \frac{y_1(x) g(x)}{W(y_1, y_2)(x)} dx$$
</div>
"""
                }
            ],
            "problems": [
                {
                    "id": "ode1-prob-19",
                    "difficulty": "Easy",
                    "difficultyLabel": "Tier 1 • Foundational",
                    "title": "Undetermined Coefficients with Resonance Multiplication",
                    "statement": "Find the general solution of the differential equation:<br>$$y'' - 4y' + 4y = (x + 1) e^{2x}$$",
                    "solution": r"<b>Step 1: Solve the homogeneous equation</b><br>Characteristic equation: $r^2 - 4r + 4 = 0 \implies (r - 2)^2 = 0 \implies r = 2$ (double root).<br>$$y_c(x) = (c_1 + c_2 x) e^{2x}$$<br><br><b>Step 2: Determine trial form for $y_p(x)$</b><br>The basic trial form for $(x + 1)e^{2x}$ is $(A x + B) e^{2x}$.<br>However, both $e^{2x}$ and $x e^{2x}$ appear in $y_c(x)$ (multiplicity $s = 2$).<br>By the modification rule, we multiply by $x^2$:<br>$$y_p(x) = x^2 (A x + B) e^{2x} = (A x^3 + B x^2) e^{2x}$$<br><br><b>Step 3: Differentiate and substitute</b><br>Let $u(x) = A x^3 + B x^2$, so $y_p = u e^{2x}$.<br>By Leibniz formula for $(D - 2)^2[u e^{2x}] = e^{2x} D^2[u] = e^{2x} u''$.<br>$$u''(x) = \frac{d^2}{dx^2}(A x^3 + B x^2) = 6A x + 2B$$Thus $(D - 2)^2[y_p] = (6A x + 2B) e^{2x}$.<br>Equating to the RHS $(x + 1) e^{2x}$:<br>$$6A x + 2B = x + 1 \implies 6A = 1 \implies A = \frac{1}{6}, \quad 2B = 1 \implies B = \frac{1}{2}$$<br><br><b>Step 4: Form the general solution</b><br>$$y_p(x) = \left(\frac{1}{6} x^3 + \frac{1}{2} x^2\right) e^{2x}$$<br>$$y(x) = (c_1 + c_2 x) e^{2x} + \left(\frac{1}{6} x^3 + \frac{1}{2} x^2\right) e^{2x}$$",
                    "answer": r"$y(x) = \left(c_1 + c_2 x + \frac{1}{2} x^2 + \frac{1}{6} x^3\right) e^{2x}$."
                },
                {
                    "id": "ode1-prob-20",
                    "difficulty": "Medium",
                    "difficultyLabel": "Tier 2 • Analytical University Exam",
                    "title": "Variation of Parameters for Secant Forcing Function",
                    "statement": "Solve the non-homogeneous differential equation:<br>$$y'' + y = \\sec x, \\quad -\frac{\\pi}{2} < x < \\frac{\\pi}{2}$$<br>using Lagrange's method of variation of parameters.",
                    "solution": r"<b>Step 1: Homogeneous complementary solution</b><br>$r^2 + 1 = 0 \implies r = \pm i$.<br>$$y_1(x) = \cos x, \quad y_2(x) = \sin x \implies y_c(x) = c_1 \cos x + c_2 \sin x$$<br><br><b>Step 2: Wronskian computation</b><br>$$W(y_1, y_2)(x) = \begin{vmatrix} \cos x & \sin x \\ -\sin x & \cos x \end{vmatrix} = \cos^2 x + \sin^2 x = 1$$<br><br><b>Step 3: Compute $u_1(x)$ and $u_2(x)$</b><br>Here $g(x) = \sec x$.<br>$$u_1'(x) = -\frac{y_2 g(x)}{W} = -\frac{\sin x \sec x}{1} = -\tan x \implies u_1(x) = -\int \tan x dx = \ln|\cos x|$$<br>$$u_2'(x) = \frac{y_1 g(x)}{W} = \frac{\cos x \sec x}{1} = 1 \implies u_2(x) = \int 1 dx = x$$<br><br><b>Step 4: Formulate particular and general solution</b><br>$$y_p(x) = u_1 y_1 + u_2 y_2 = (\ln|\cos x|) \cos x + x \sin x$$<br>$$y(x) = c_1 \cos x + c_2 \sin x + \cos x \ln(\cos x) + x \sin x$$",
                    "answer": r"$y(x) = c_1 \cos x + c_2 \sin x + \cos x \ln(\cos x) + x \sin x$ (for $|x| < \pi/2$)."
                },
                {
                    "id": "ode1-prob-21",
                    "difficulty": "Hard",
                    "difficultyLabel": "Tier 3 • Honors Challenge",
                    "title": "Non-Homogeneous Cauchy-Euler Equation via Variation of Parameters",
                    "statement": "Solve the non-homogeneous Cauchy-Euler differential equation:<br>$$x^2 y'' - 2x y' + 2y = x^3 \\ln x, \\quad x > 0$$",
                    "solution": r"""<b>Step 1: Homogeneous solution</b><br>Indicial equation: $m(m - 1) - 2m + 2 = 0 \implies m^2 - 3m + 2 = 0 \implies (m - 1)(m - 2) = 0$.<br>$$y_1(x) = x, \quad y_2(x) = x^2 \implies y_c(x) = c_1 x + c_2 x^2$$<br><br><b>Step 2: Normalize the ODE to standard form</b><br>Divide by $x^2$:<br>$$y'' - \frac{2}{x} y' + \frac{2}{x^2} y = x \ln x \implies g(x) = x \ln x$$<br><br><b>Step 3: Wronskian computation</b><br>$$W(y_1, y_2) = \begin{vmatrix} x & x^2 \\ 1 & 2x \end{vmatrix} = 2x^2 - x^2 = x^2$$<br><br><b>Step 4: Integrate parameter derivatives</b><br>$$u_1'(x) = -\frac{y_2 g(x)}{W} = -\frac{x^2 (x \ln x)}{x^2} = -x \ln x$$$$\int -x \ln x dx = -\left[\frac{x^2}{2} \ln x - \int \frac{x^2}{2} \cdot \frac{1}{x} dx\right] = -\frac{x^2}{2} \ln x + \frac{x^2}{4}$$<br>$$u_2'(x) = \frac{y_1 g(x)}{W} = \frac{x (x \ln x)}{x^2} = \ln x$$$$\int \ln x dx = x \ln x - x$$<br><br><b>Step 5: Formulate $y_p(x)$</b><br>$$\begin{aligned}
y_p(x) &= u_1 y_1 + u_2 y_2 = x\left(-\frac{x^2}{2}\ln x + \frac{x^2}{4}\right) + x^2(x \ln x - x) \\
&= -\frac{x^3}{2}\ln x + \frac{x^3}{4} + x^3 \ln x - x^3 = \frac{x^3}{2}\ln x - \frac{3}{4}x^3
\end{aligned}$$<br><br><b>Step 6: General solution</b><br>$$y(x) = c_1 x + c_2 x^2 + \frac{1}{2}x^3 \ln x - \frac{3}{4}x^3$$""",
                    "answer": r"$y(x) = c_1 x + c_2 x^2 + \frac{1}{2} x^3 \ln x - \frac{3}{4} x^3$ (or absorb $-3x^3/4$ into $y_p$)."
                }
            ]
        },

        # UNIT 8
        {
            "unitNumber": 8,
            "title": "Dynamical Modeling with Second-Order Systems: Oscillations, Resonance & Rocket Dynamics",
            "leadSummary": "Comprehensive modeling of second-order mechanical, electrical, and aerospace systems: free undamped and damped vibrations, logarithmic decrement, forced oscillations, the phenomenon of beats, resonance and Q-factors, series RLC electrical networks, and variable-mass Tsiolkovsky rocket dynamics under gravity and drag.",
            "sections": [
                {
                    "id": "u8-sec1",
                    "secNumber": "8.1",
                    "title": "Mechanical Vibrations: Free Undamped & Damped Oscillators",
                    "content": r"""
<h4>1. Newton's Second Law for the Spring-Mass-Damper System</h4>
<p>Consider a mass $m$ attached to a linear spring of stiffness constant $k$ and a viscous damper with damping coefficient $c$. By Newton's second law, $m x'' = F_{\text{spring}} + F_{\text{damping}} + F_{\text{ext}}(t) = -kx - cx' + F(t)$:</p>
<div class="math-display">
$$m \frac{d^2x}{dt^2} + c \frac{dx}{dt} + k x = F(t)$$
</div>
<p>Dividing by $m$, we write the canonical form: $x'' + 2\zeta \omega_0 x' + \omega_0^2 x = \frac{F(t)}{m}$, where $\omega_0 = \sqrt{\frac{k}{m}}$ is the <strong>undamped natural angular frequency</strong> and $\zeta = \frac{c}{2\sqrt{km}}$ is the dimensionless <strong>damping ratio</strong>.</p>

<h4>2. Free Motion Classification ($F(t) \equiv 0$)</h4>
<ul>
  <li><strong>Undamped Motion ($\zeta = 0, c = 0$)</strong>: Simple Harmonic Motion (SHM):
    $$x(t) = c_1 \cos(\omega_0 t) + c_2 \sin(\omega_0 t) = A \cos(\omega_0 t - \phi)$$
    where amplitude $A = \sqrt{c_1^2 + c_2^2}$ and period $T = \frac{2\pi}{\omega_0}$.
  </li>
  <li><strong>Overdamped Motion ($\zeta > 1, c^2 > 4km$)</strong>: Characteristic roots are real, negative, and distinct: $r_{1,2} = -\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2 - 1}$. The system returns to equilibrium non-oscillatingly.</li>
  <li><strong>Critically Damped Motion ($\zeta = 1, c = 2\sqrt{km}$)</strong>: Repeated real root $r = -\omega_0$. Solution:
    $$x(t) = (c_1 + c_2 t) e^{-\omega_0 t}$$
    This provides the <em>fastest possible return to equilibrium without oscillation</em> (crucial in automobile shock absorbers and gun recoil mechanisms).
  </li>
  <li><strong>Underdamped Motion ($\zeta < 1, c^2 < 4km$)</strong>: Complex roots $r = -\alpha \pm i \omega_d$, where $\alpha = \zeta \omega_0 = \frac{c}{2m}$ and $\omega_d = \omega_0 \sqrt{1 - \zeta^2}$ is the <strong>quasi-frequency</strong>.
    $$x(t) = A e^{-\alpha t} \cos(\omega_d t - \phi)$$
    The amplitude decays exponentially. The rate of decay is quantified by the <strong>logarithmic decrement</strong> $\delta$:
    $$\delta = \ln\left(\frac{x(t)}{x(t + T_d)}\right) = \alpha T_d = \frac{2\pi \zeta}{\sqrt{1 - \zeta^2}}$$
  </li>
</ul>
"""
                },
                {
                    "id": "u8-sec2",
                    "secNumber": "8.2",
                    "title": "Forced Vibrations, Secular Resonance & The Quality Factor",
                    "content": r"""
<h4>1. Forced Oscillations with Harmonic Excitation</h4>
<p>When subjected to a periodic external force $F(t) = F_0 \cos(\omega t)$:</p>
<div class="math-display">
$$m x'' + c x' + k x = F_0 \cos(\omega t)$$
</div>
<p>The general solution consists of a transient complementary solution $x_c(t)$ (which dies out exponentially as $t \to \infty$) and a persistent steady-state particular solution $x_p(t) = x_{ss}(t)$:</p>
<div class="math-display">
$$x_{ss}(t) = X(\omega) \cos(\omega t - \phi)$$
</div>
<p>Using the method of undetermined coefficients, the steady-state amplitude is derived exactly as:</p>
<div class="math-display">
$$X(\omega) = \frac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + \left(\frac{c\omega}{m}\right)^2}} = \frac{F_0/k}{\sqrt{\left(1 - \frac{\omega^2}{\omega_0^2}\right)^2 + \left(2\zeta \frac{\omega}{\omega_0}\right)^2}}$$
</div>
<p>and the phase lag is $\phi = \arctan\left(\frac{c\omega/m}{\omega_0^2 - \omega^2}\right) = \arctan\left(\frac{2\zeta (\omega/\omega_0)}{1 - (\omega/\omega_0)^2}\right)$.</p>

<h4>2. Resonance Phenomena</h4>
<ul>
  <li><strong>Pure Secular Resonance (No Damping, $\zeta = 0$)</strong>: When $\omega = \omega_0$, the denominator vanishes. The particular solution undergoes linear secular growth:
    $$x_p(t) = \frac{F_0}{2 m \omega_0} t \sin(\omega_0 t)$$
    The amplitude grows without bound as $t \to \infty$, leading to structural destruction.
  </li>
  <li><strong>Resonance with Damping ($\zeta < 1/\sqrt{2}$)</strong>: Maximizing $X(\omega)$ by minimizing the radicand yields the <strong>resonant frequency</strong> $\omega_r$:
    $$\omega_r = \omega_0 \sqrt{1 - 2\zeta^2}$$
    At resonance, the peak amplitude is $X_{\text{max}} = \frac{F_0/k}{2\zeta\sqrt{1 - \zeta^2}}$. The sharpness of the resonance peak is measured by the <strong>Quality Factor $Q$</strong>:
    $$Q = \frac{1}{2\zeta} = \frac{\sqrt{km}}{c}$$
  </li>
</ul>
""",
                    "simulation": "ode1-damped-resonance-sim"
                },
                {
                    "id": "u8-sec3",
                    "secNumber": "8.3",
                    "title": "Series RLC Electrical Networks & Variable-Mass Rocket Dynamics",
                    "content": r"""
<h4>1. Series RLC Electrical Network Modeling</h4>
<p>By Kirchhoff's voltage law, the sum of voltage drops across an inductor $L$, resistor $R$, and capacitor $C$ in a closed loop equals the applied electromotive force $E(t)$:</p>
<div class="math-display">
$$V_L + V_R + V_C = L \frac{dI}{dt} + R I + \frac{1}{C} q = E(t)$$
</div>
<p>Since electric current is the time derivative of charge, $I(t) = \frac{dq}{dt}$, substituting yields the second-order linear ODE for charge $q(t)$:</p>
<div class="math-display">
$$L \frac{d^2q}{dt^2} + R \frac{dq}{dt} + \frac{1}{C} q = E(t)$$
</div>
<p>Differentiating with respect to $t$ yields the dual equation for the electric current $I(t)$:</p>
<div class="math-display">
$$L \frac{d^2I}{dt^2} + R \frac{dI}{dt} + \frac{1}{C} I = \frac{dE}{dt}$$
</div>
<p><strong>Mechanical-Electrical Analogy</strong>: Inductance $L \leftrightarrow$ Mass $m$; Resistance $R \leftrightarrow$ Damping $c$; Inverse capacitance $1/C \leftrightarrow$ Spring stiffness $k$; Charge $q \leftrightarrow$ Position $x$; Current $I \leftrightarrow$ Velocity $v$.</p>

<h4>2. Rocket Motion Dynamics (Variable Mass Systems)</h4>
<p>A rocket burning propellant is an open variable-mass mechanical system. Let $M(t) = M_0 - \alpha t$ denote the total mass of the rocket at time $t$, where $\alpha = -\frac{dM}{dt}$ is the constant mass burn rate, and let $u$ denote the exhaust velocity of gases relative to the rocket.</p>
<p>By conservation of momentum in a vertical gravitational field $g$ with linear atmospheric drag $-k v$:</p>
<div class="math-display">
$$M(t) \frac{dv}{dt} = -u \frac{dM}{dt} - M(t) g - k v = \alpha u - (M_0 - \alpha t) g - k v$$
</div>
<p>Dividing by $M(t)$ yields the first-order linear differential equation for velocity $v(t)$:</p>
<div class="math-display">
$$\frac{dv}{dt} + \frac{k}{M_0 - \alpha t} v = \frac{\alpha u}{M_0 - \alpha t} - g$$
</div>
<p>In the vacuum limit ($k = 0$), integrating directly yields the famous <strong>Tsiolkovsky rocket equation</strong>:</p>
<div class="math-display">
$$v(t) = v_0 - g t + u \ln\left(\frac{M_0}{M(t)}\right)$$
</div>
"""
                }
            ],
            "problems": [
                {
                    "id": "ode1-prob-22",
                    "difficulty": "Easy",
                    "difficultyLabel": "Tier 1 • Foundational",
                    "title": "Logarithmic Decrement & Damping Extraction in a Mechanical Oscillator",
                    "statement": "An underdamped spring-mass system with mass $m = 2\\text{ kg}$ and spring constant $k = 50\\text{ N/m}$ undergoes free oscillations. Successive peak amplitudes on the same side are measured to be $x_1 = 8.0\\text{ cm}$ and $x_2 = 5.0\\text{ cm}$. Calculate the logarithmic decrement $\\delta$, the damping ratio $\\zeta$, the damping coefficient $c$, and the quasi-period $T_d$.",
                    "solution": r"<b>Step 1: Compute logarithmic decrement</b><br>$$\delta = \ln\left(\frac{x_1}{x_2}\right) = \ln\left(\frac{8.0}{5.0}\right) = \ln(1.6) \approx 0.4700$$<br><br><b>Step 2: Calculate damping ratio $\zeta$</b><br>$$\delta = \frac{2\pi \zeta}{\sqrt{1 - \zeta^2}} \implies \zeta = \frac{\delta}{\sqrt{4\pi^2 + \delta^2}} = \frac{0.4700}{\sqrt{4\pi^2 + (0.4700)^2}} = \frac{0.4700}{\sqrt{39.478 + 0.2209}} = \frac{0.4700}{6.3007} \approx 0.0746$$<br><br><b>Step 3: Calculate undamped natural frequency and damping coefficient $c$</b><br>$$\omega_0 = \sqrt{\frac{k}{m}} = \sqrt{\frac{50}{2}} = \sqrt{25} = 5.0\text{ rad/s}$$Critical damping $c_c = 2\sqrt{km} = 2\sqrt{50 \cdot 2} = 2\sqrt{100} = 20\text{ N}\cdot\text{s/m}$.<br>$$c = \zeta c_c = (0.0746)(20) \approx 1.492\text{ N}\cdot\text{s/m}$$<br><br><b>Step 4: Quasi-frequency and quasi-period</b><br>$$\omega_d = \omega_0 \sqrt{1 - \zeta^2} = 5.0 \sqrt{1 - (0.0746)^2} = 5.0(0.9972) \approx 4.986\text{ rad/s}$$<br>$$T_d = \frac{2\pi}{\omega_d} = \frac{2\pi}{4.986} \approx 1.260\text{ seconds}$$",
                    "answer": r"$\delta = 0.470$, $\zeta = 0.0746$, $c = 1.49\text{ N}\cdot\text{s/m}$, and $T_d = 1.26\text{ s}$."
                },
                {
                    "id": "ode1-prob-23",
                    "difficulty": "Medium",
                    "difficultyLabel": "Tier 2 • Analytical University Exam",
                    "title": "Steady-State Resonance Amplification & Peak Analysis",
                    "statement": "A $10\\text{ kg}$ machine is supported on isolators with total stiffness $k = 4000\\text{ N/m}$ and damping $c = 40\\text{ N}\\cdot\\text{s/m}$. A harmonic force $F(t) = 100 \\cos(\\omega t)\\text{ N}$ acts on the machine. Find the resonant frequency $\\omega_r$, the maximum steady-state displacement amplitude $X_{\\text{max}}$, and compare with the static deflection.",
                    "solution": r"<b>Step 1: Compute system baseline parameters</b><br>$$\omega_0 = \sqrt{\frac{k}{m}} = \sqrt{\frac{4000}{10}} = \sqrt{400} = 20\text{ rad/s}$$Static deflection under force $F_0 = 100\text{ N}$:<br>$$\delta_{st} = \frac{F_0}{k} = \frac{100}{4000} = 0.025\text{ m} = 2.5\text{ cm}$$Damping ratio $\zeta$:<br>$$\zeta = \frac{c}{2\sqrt{km}} = \frac{40}{2\sqrt{4000 \cdot 10}} = \frac{40}{2(200)} = \frac{40}{400} = 0.10$$<br><br><b>Step 2: Resonant frequency $\omega_r$</b><br>$$\omega_r = \omega_0 \sqrt{1 - 2\zeta^2} = 20 \sqrt{1 - 2(0.10)^2} = 20 \sqrt{1 - 0.02} = 20 \sqrt{0.98} \approx 19.80\text{ rad/s}$$<br><br><b>Step 3: Maximum amplitude $X_{\text{max}}$</b><br>$$X_{\text{max}} = \frac{\delta_{st}}{2\zeta\sqrt{1 - \zeta^2}} = \frac{0.025}{2(0.10)\sqrt{1 - 0.01}} = \frac{0.025}{0.20 \cdot 0.99498} = \frac{0.025}{0.1990} \approx 0.1256\text{ m} = 12.56\text{ cm}$$<br><br><b>Step 4: Dynamic amplification factor</b><br>$$Q \approx \frac{X_{\text{max}}}{\delta_{st}} = \frac{12.56\text{ cm}}{2.5\text{ cm}} \approx 5.025$$",
                    "answer": r"$\omega_r \approx 19.80\text{ rad/s}$, $X_{\text{max}} \approx 12.56\text{ cm}$, with dynamic amplification factor $M \approx 5.03$ times static deflection."
                },
                {
                    "id": "ode1-prob-24",
                    "difficulty": "Hard",
                    "difficultyLabel": "Tier 3 • Honors Challenge",
                    "title": "Variable-Mass Rocket Ascent Under Gravity & Burnout Velocity",
                    "statement": "A sounding rocket of initial mass $M_0 = 1000\\text{ kg}$ burns propellant at a constant rate $\\alpha = 20\\text{ kg/s}$ with constant exhaust velocity $u = 2400\\text{ m/s}$. The propellant accounts for $800\\text{ kg}$ of total initial mass. Assuming vertical ascent from rest ($v(0) = 0$) under uniform gravity $g = 9.81\\text{ m/s}^2$ and negligible atmospheric resistance, calculate the burnout time $t_b$, burnout altitude $y(t_b)$, and maximum velocity attained.",
                    "solution": r"<b>Step 1: Determine burnout time and mass ratio</b><br>Fuel mass is $M_f = 800\text{ kg}$, dry mass is $M_b = 200\text{ kg}$.<br>$$t_b = \frac{M_f}{\alpha} = \frac{800}{20} = 40\text{ seconds}$$At burnout, $M(t_b) = 1000 - 20(40) = 200\text{ kg}$.<br>Mass ratio $\frac{M_0}{M_b} = \frac{1000}{200} = 5$.<br><br><b>Step 2: Compute burnout velocity via Tsiolkovsky equation</b><br>$$v(t) = -gt + u \ln\left(\frac{M_0}{M_0 - \alpha t}\right)$$At burnout $t = 40\text{ s}$:<br>$$v(t_b) = -9.81(40) + 2400 \ln(5) = -392.4 + 2400(1.60944) = -392.4 + 3862.65 = 3470.25\text{ m/s}$$<br><br><b>Step 3: Integrate for burnout altitude $y(t_b)$</b><br>$$y(t_b) = \int_0^{t_b} v(t) dt = \int_0^{t_b} \left[ -gt + u \ln M_0 - u \ln(M_0 - \alpha t) \right] dt$$Evaluating the integral:<br>$$\int_0^{t_b} -gt dt = -\frac{1}{2} g t_b^2 = -\frac{1}{2}(9.81)(1600) = -7848\text{ m}$$Using $\int \ln(A - \alpha t) dt = -\frac{1}{\alpha}[(A - \alpha t)\ln(A - \alpha t) - (A - \alpha t)]$:<br>$$\int_0^{t_b} u \ln\left(\frac{M_0}{M_0 - \alpha t}\right) dt = u t_b - \frac{u M_b}{\alpha} \ln\left(\frac{M_0}{M_b}\right) = (2400)(40) - \frac{(2400)(200)}{20} \ln(5) = 96000 - 24000(1.60944) = 96000 - 38626.5 = 57373.5\text{ m}$$Thus total altitude at burnout is:<br>$$y(t_b) = 57373.5 - 7848 = 49525.5\text{ meters} \approx 49.53\text{ km}$$",
                    "answer": r"Burnout time: $t_b = 40\text{ s}$. Maximum burnout velocity: $v(t_b) \approx 3470\text{ m/s}$ ($3.47\text{ km/s}$). Burnout altitude: $y(t_b) \approx 49.53\text{ km}$."
                }
            ]
        }
    ]
}

# Write out ordinary-differential-equations-1-data.js
js_code = "window.COURSE_DATA = " + json.dumps(course_data, indent=2, ensure_ascii=False) + ";\n"

with open("ordinary-differential-equations-1-data.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Generated ordinary-differential-equations-1-data.js successfully with 8 units and 24 solved problems!")
