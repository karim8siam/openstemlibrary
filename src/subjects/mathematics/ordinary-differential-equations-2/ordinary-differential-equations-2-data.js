window.COURSE_DATA = {
  "courseCode": "",
  "courseTitle": "Ordinary Differential Equations II",
  "courseSubtitle": "First-Order Systems, Series Solutions, Classical Orthogonal Functions & Sturm-Liouville Theory",
  "credits": 3,
  "lectureHours": 45,
  "prerequisites": "Calculus I, Calculus II & Ordinary Differential Equations I",
  "description": "Exhaustive honors-level university digital textbook covering advanced linear differential systems, series solutions near ordinary and regular singular points, classical orthogonal functions (Legendre, Bessel, Laguerre, Hermite), Sturm-Liouville eigenvalue boundary value theory, the Fredholm Alternative, and Green's functions with 8 interactive 60 FPS simulations and 24 tiered solved university examination problems.",
  "units": [
    {
      "number": 1,
      "title": "Systems of Linear First-Order ODEs: Foundations, Operator Elimination & Phase Plane Topology",
      "leadSummary": "Transformation of higher-order differential equations into first-order dynamical systems, algebraic operator elimination, autonomous phase plane topology, and complete classification of equilibrium points.",
      "simulations": [
        "ode2-phase-portrait-sim"
      ],
      "sections": [
        {
          "secNumber": "1.1",
          "title": "Conversion of n-th Order Linear ODEs into First-Order Vector Systems & Fundamental Existence-Uniqueness Theorem",
          "content": "<h3>1. The Canonical Vector Formulation</h3>\n<p>In analytical dynamics, control theory, and multivariable physics, physical systems rarely present themselves as single isolated scalar equations. Instead, systems of interconnected components are modeled by coupled differential equations. Consider the general $n$-th order linear ordinary differential equation:</p>\n$$y^{(n)}(t) + p_{n-1}(t) y^{(n-1)}(t) + \\dots + p_1(t) y'(t) + p_0(t) y(t) = g(t)$$\n<p>We convert this single $n$-th order equation into an equivalent system of $n$ first-order differential equations by introducing state variables:</p>\n$$\\begin{aligned}\nx_1(t) &= y(t) \\\\\nx_2(t) &= y'(t) = x_1'(t) \\\\\nx_3(t) &= y''(t) = x_2'(t) \\\\\n&\\;\\;\\vdots \\\\\nx_n(t) &= y^{(n-1)}(t) = x_{n-1}'(t)\n\\end{aligned}$$\n<p>Differentiating the state vector $\\vec{x}(t) = \\begin{pmatrix} x_1(t) & x_2(t) & \\dots & x_n(t) \\end{pmatrix}^T$, the final derivative is:</p>\n$$x_n'(t) = y^{(n)}(t) = -p_0(t) x_1(t) - p_1(t) x_2(t) - \\dots - p_{n-1}(t) x_n(t) + g(t)$$\n<p>In compact matrix-vector notation, this yields the standard linear dynamical system:</p>\n$$\\frac{d\\vec{x}}{dt} = \\mathbf{A}(t) \\vec{x}(t) + \\vec{g}(t)$$\n<p>where the system companion matrix $\\mathbf{A}(t) \\in \\mathbb{R}^{n \\times n}$ and nonhomogeneous source vector $\\vec{g}(t)$ are:</p>\n$$\\mathbf{A}(t) = \\begin{pmatrix}\n0 & 1 & 0 & \\dots & 0 \\\\\n0 & 0 & 1 & \\dots & 0 \\\\\n\\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\\n0 & 0 & 0 & \\dots & 1 \\\\\n-p_0(t) & -p_1(t) & -p_2(t) & \\dots & -p_{n-1}(t)\n\\end{pmatrix}, \\quad \\vec{g}(t) = \\begin{pmatrix} 0 \\\\ 0 \\\\ \\vdots \\\\ 0 \\\\ g(t) \\end{pmatrix}$$\n\n<h3>2. The Picard-Lindelöf Theorem for Vector Systems</h3>\n<div class=\"math-theorem\">\n<b>Theorem 1.1 (Existence and Uniqueness for Linear Systems):</b> Let the matrix function $\\mathbf{A}(t)$ and the vector function $\\vec{g}(t)$ be continuous on an open interval $I = (\\alpha, \\beta) \\subseteq \\mathbb{R}$. Let $t_0 \\in I$, and let $\\vec{x}_0 \\in \\mathbb{R}^n$ be an arbitrary prescribed initial vector. Then the initial value problem (IVP):\n$$\\frac{d\\vec{x}}{dt} = \\mathbf{A}(t) \\vec{x}(t) + \\vec{g}(t), \\quad \\vec{x}(t_0) = \\vec{x}_0$$\npossesses a <b>unique</b> continuously differentiable solution $\\vec{x}(t)$ defined across the entire interval $I$.\n</div>\n<p>The proof relies on constructing the vector Picard iteration operator $\\mathcal{T}[\\vec{x}](t) = \\vec{x}_0 + \\int_{t_0}^t [\\mathbf{A}(s)\\vec{x}(s) + \\vec{g}(s)]\\,ds$ and proving it is a contraction mapping on the Banach space $C(J, \\mathbb{R}^n)$ under the supremum norm $\\|\\vec{x}\\|_\\infty = \\sup_{t \\in J} \\|\\vec{x}(t)\\|$.</p>"
        },
        {
          "secNumber": "1.2",
          "title": "The Method of Elimination & Differential Polynomial Determinants",
          "content": "<h3>1. Differential Operator Notation</h3>\n<p>Let $D = \\frac{d}{dt}$ denote the differential operator. A linear coupled system of two differential equations in dependent variables $x(t)$ and $y(t)$ can be expressed algebraically as:</p>\n$$\\begin{aligned}\nL_1[x] + L_2[y] &= f_1(t) \\\\\nL_3[x] + L_4[y] &= f_2(t)\n\\end{aligned}$$\n<p>where $L_1, L_2, L_3, L_4 \\in \\mathbb{R}[D]$ are polynomial differential operators with constant coefficients. Written in operator matrix form:</p>\n$$\\begin{pmatrix} L_1(D) & L_2(D) \\\\ L_3(D) & L_4(D) \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\end{pmatrix} = \\begin{pmatrix} f_1(t) \\\\ f_2(t) \\end{pmatrix}$$\n\n<h3>2. Elimination via Cramer's Operator Rule</h3>\n<p>Applying the operator determinant $\\Delta(D) = L_1(D) L_4(D) - L_2(D) L_3(D)$ eliminates variables systematically:</p>\n$$\\begin{aligned}\n\\Delta(D) x(t) &= L_4(D) f_1(t) - L_2(D) f_2(t) \\\\\n\\Delta(D) y(t) &= L_1(D) f_2(t) - L_3(D) f_1(t)\n\\end{aligned}$$\n<p><b>Caution on Arbitrary Constants:</b> If $\\Delta(D)$ has degree $m$, each scalar equation produces $m$ arbitrary constants. However, the original system requires only $m$ independent constants in total! Substituting the solutions back into the original coupled equations establishes the algebraic constraints connecting the constant pairs $(c_1, \\dots, c_m)$ and $(k_1, \\dots, k_m)$.</p>"
        },
        {
          "secNumber": "1.3",
          "title": "Autonomous 2D Linear Systems, Phase Portraits & Classification of Critical Equilibrium Points",
          "simulation": "ode2-phase-portrait-sim",
          "content": "<h3>1. Autonomous 2D Linear Systems</h3>\n<p>Consider the planar autonomous linear system:</p>\n$$\\frac{d\\vec{x}}{dt} = \\mathbf{A} \\vec{x}, \\quad \\mathbf{A} = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix} \\in \\mathbb{R}^{2 \\times 2}$$\n<p>The origin $\\vec{x}^* = \\begin{pmatrix} 0 & 0 \\end{pmatrix}^T$ is the unique equilibrium point whenever $\\det(\\mathbf{A}) \\ne 0$. The characteristic equation governing the eigenvalues $\\lambda$ is:</p>\n$$\\det(\\mathbf{A} - \\lambda \\mathbf{I}) = \\lambda^2 - \\tau \\lambda + \\Delta = 0$$\n<p>where $\\tau = \\text{Tr}(\\mathbf{A}) = a + d$ is the matrix trace, and $\\Delta = \\det(\\mathbf{A}) = ad - bc$ is the determinant. The discriminant is:</p>\n$$\\mathcal{D} = \\tau^2 - 4\\Delta$$\n\n<h3>2. The Poincaré Trace-Determinant Classification</h3>\n<div class=\"math-theorem\">\n<b>Classification of Critical Points:</b>\n<ul>\n<li><b>$\\Delta < 0$:</b> Eigenvalues $\\lambda_1 < 0 < \\lambda_2$ are real with opposite signs. The origin is a <b>Saddle Point</b> (always asymptotically unstable). Orbits approach along the stable eigenvector and depart along the unstable eigenvector.</li>\n<li><b>$\\Delta > 0$ and $\\mathcal{D} > 0$:</b> Real distinct eigenvalues of the same sign.\n  <ul>\n    <li>$\\tau < 0 \\implies \\lambda_1, \\lambda_2 < 0$: <b>Stable Node</b> (asymptotically stable attractor).</li>\n    <li>$\\tau > 0 \\implies \\lambda_1, \\lambda_2 > 0$: <b>Unstable Node</b> (repeller).</li>\n  </ul>\n</li>\n<li><b>$\\Delta > 0$ and $\\mathcal{D} < 0$:</b> Complex conjugate eigenvalues $\\lambda = \\alpha \\pm i\\beta$ where $\\alpha = \\frac{\\tau}{2}$ and $\\beta = \\frac{\\sqrt{4\\Delta - \\tau^2}}{2}$.\n  <ul>\n    <li>$\\tau < 0 \\implies \\alpha < 0$: <b>Stable Spiral (Focus)</b>. Orbits spiral inward toward the origin.</li>\n    <li>$\\tau > 0 \\implies \\alpha > 0$: <b>Unstable Spiral (Focus)</b>. Orbits spiral outward to infinity.</li>\n    <li>$\\tau = 0 \\implies \\alpha = 0$: <b>Center (Vortex)</b>. Eigenvalues are purely imaginary $\\lambda = \\pm i\\beta$. Orbits form closed concentric ellipses (neutrally stable, non-isolated periodic orbits).</li>\n  </ul>\n</li>\n<li><b>$\\mathcal{D} = 0$:</b> Repeated eigenvalue $\\lambda_1 = \\lambda_2 = \\frac{\\tau}{2}$.\n  <ul>\n    <li>If $\\mathbf{A} = \\lambda \\mathbf{I}$: <b>Proper Star Node</b> (every radial direction is an eigenvector trajectory).</li>\n    <li>If $\\mathbf{A} \\ne \\lambda \\mathbf{I}$ (defective matrix): <b>Degenerate / Improper Node</b> (trajectories tangent to the single eigenvector span).</li>\n  </ul>\n</li>\n</ul>\n</div>"
        }
      ],
      "problems": [
        {
          "id": "prob-01",
          "tier": 1,
          "difficultyLabel": "Tier 1 • Foundational",
          "title": "Homogeneous 2x2 System with Real Distinct Eigenvalues",
          "statement": "Solve the initial value problem for the linear system:<br>$$\\frac{d\\vec{x}}{dt} = \\begin{pmatrix} 1 & 2 \\\\ 2 & 1 \\end{pmatrix} \\vec{x}, \\quad \\vec{x}(0) = \\begin{pmatrix} 3 \\\\ 1 \\end{pmatrix}$$",
          "solution": "<b>Step 1: Eigenvalues of the system matrix</b><br>\n$$\\det(\\mathbf{A} - \\lambda \\mathbf{I}) = \\begin{vmatrix} 1 - \\lambda & 2 \\\\ 2 & 1 - \\lambda \\end{vmatrix} = (1 - \\lambda)^2 - 4 = \\lambda^2 - 2\\lambda - 3 = 0$$\nFactorizing yields $(\\lambda - 3)(\\lambda + 1) = 0 \\implies \\lambda_1 = 3, \\lambda_2 = -1$.<br><br>\n<b>Step 2: Eigenvector for $\\lambda_1 = 3$</b><br>\n$$(\\mathbf{A} - 3\\mathbf{I})\\vec{v}_1 = \\begin{pmatrix} -2 & 2 \\\\ 2 & -2 \\end{pmatrix} \\begin{pmatrix} v_{11} \\\\ v_{12} \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 0 \\end{pmatrix} \\implies v_{11} = v_{12} \\implies \\vec{v}_1 = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}$$\n<br><b>Step 3: Eigenvector for $\\lambda_2 = -1$</b><br>\n$$(\\mathbf{A} + \\mathbf{I})\\vec{v}_2 = \\begin{pmatrix} 2 & 2 \\\\ 2 & 2 \\end{pmatrix} \\begin{pmatrix} v_{21} \\\\ v_{22} \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 0 \\end{pmatrix} \\implies v_{21} = -v_{22} \\implies \\vec{v}_2 = \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix}$$\n<br><b>Step 4: General Solution & Initial Condition</b><br>\n$$\\vec{x}(t) = c_1 e^{3t} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} + c_2 e^{-t} \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix}$$\nAt $t = 0$:\n$$\\vec{x}(0) = \\begin{pmatrix} c_1 + c_2 \\\\ c_1 - c_2 \\end{pmatrix} = \\begin{pmatrix} 3 \\\\ 1 \\end{pmatrix}$$\nAdding both equations: $2c_1 = 4 \\implies c_1 = 2$. Subtracting: $2c_2 = 2 \\implies c_2 = 1$.<br><br>\n$$\\vec{x}(t) = 2e^{3t} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} + e^{-t} \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix} = \\begin{pmatrix} 2e^{3t} + e^{-t} \\\\ 2e^{3t} - e^{-t} \\end{pmatrix}$$",
          "answer": "$\\vec{x}(t) = \\begin{pmatrix} 2e^{3t} + e^{-t} \\\\ 2e^{3t} - e^{-t} \\end{pmatrix}$",
          "difficulty": "Easy"
        },
        {
          "id": "prob-09",
          "tier": 2,
          "difficultyLabel": "Tier 2 • Intermediate Exam",
          "title": "3x3 System with Complex Eigenvalues & Invariant Orbital Manifold",
          "statement": "Solve the $3 \\times 3$ linear differential system:<br>$$\\vec{x}' = \\begin{pmatrix} 0 & 1 & 0 \\\\ -4 & 0 & 0 \\\\ 0 & 0 & -2 \\end{pmatrix} \\vec{x}, \\quad \\vec{x}(0) = \\begin{pmatrix} 1 \\\\ 0 \\\\ 2 \\end{pmatrix}$$",
          "solution": "<b>Step 1: Block structure and eigenvalues</b><br>\nThe matrix is block diagonal: $\\mathbf{A} = \\begin{pmatrix} \\mathbf{B} & \\vec{0} \\\\ \\vec{0}^T & -2 \\end{pmatrix}$ where $\\mathbf{B} = \\begin{pmatrix} 0 & 1 \\\\ -4 & 0 \\end{pmatrix}$.\n$\\det(\\mathbf{B} - \\lambda \\mathbf{I}) = \\lambda^2 + 4 = 0 \\implies \\lambda_{1, 2} = \\pm 2i$.\nThe third eigenvalue is $\\lambda_3 = -2$.<br><br>\n<b>Step 2: Eigenvectors</b><br>\nFor $\\lambda_1 = 2i$:\n$$\\begin{pmatrix} -2i & 1 & 0 \\\\ -4 & -2i & 0 \\\\ 0 & 0 & -2 - 2i \\end{pmatrix} \\begin{pmatrix} v_1 \\\\ v_2 \\\\ v_3 \\end{pmatrix} = \\vec{0} \\implies v_3 = 0, \\quad v_2 = 2i v_1 \\implies \\vec{v} = \\begin{pmatrix} 1 \\\\ 2i \\\\ 0 \\end{pmatrix} = \\begin{pmatrix} 1 \\\\ 0 \\\\ 0 \\end{pmatrix} + i \\begin{pmatrix} 0 \\\\ 2 \\\\ 0 \\end{pmatrix}$$\nReal independent solutions:\n$$\\vec{x}_1(t) = \\begin{pmatrix} \\cos 2t \\\\ -2\\sin 2t \\\\ 0 \\end{pmatrix}, \\quad \\vec{x}_2(t) = \\begin{pmatrix} \\sin 2t \\\\ 2\\cos 2t \\\\ 0 \\end{pmatrix}$$\nFor $\\lambda_3 = -2$:\n$$\\vec{v}_3 = \\begin{pmatrix} 0 \\\\ 0 \\\\ 1 \\end{pmatrix} \\implies \\vec{x}_3(t) = e^{-2t} \\begin{pmatrix} 0 \\\\ 0 \\\\ 1 \\end{pmatrix}$$\n<br><b>Step 3: Initial conditions</b><br>\n$$\\vec{x}(t) = c_1 \\begin{pmatrix} \\cos 2t \\\\ -2\\sin 2t \\\\ 0 \\end{pmatrix} + c_2 \\begin{pmatrix} \\sin 2t \\\\ 2\\cos 2t \\\\ 0 \\end{pmatrix} + c_3 \\begin{pmatrix} 0 \\\\ 0 \\\\ e^{-2t} \\end{pmatrix}$$\nAt $t = 0$: $c_1 = 1, 2c_2 = 0 \\implies c_2 = 0$, and $c_3 = 2$.<br><br>\n$$\\vec{x}(t) = \\begin{pmatrix} \\cos 2t \\\\ -2\\sin 2t \\\\ 2e^{-2t} \\end{pmatrix}$$",
          "answer": "$\\vec{x}(t) = \\begin{pmatrix} \\cos 2t \\\\ -2\\sin 2t \\\\ 2e^{-2t} \\end{pmatrix}$",
          "difficulty": "Medium"
        },
        {
          "id": "prob-17",
          "tier": 3,
          "difficultyLabel": "Tier 3 • Honors Challenge",
          "title": "Matrix Riccati Transformation & Hamiltonian Linear System",
          "statement": "Convert the nonlinear matrix Riccati differential equation $\\mathbf{R}' = \\mathbf{B} - \\mathbf{R} \\mathbf{D} \\mathbf{R}$ into an equivalent $2n \\times 2n$ linear Hamiltonian dynamical system $\\vec{z}' = \\mathbf{H}\\vec{z}$.",
          "solution": "<b>Step 1: Fractional Linear Transformation</b><br>\nLet $\\mathbf{R}(t) = \\mathbf{X}(t) \\mathbf{Y}^{-1}(t)$ where $\\mathbf{X}(t), \\mathbf{Y}(t) \\in \\mathbb{R}^{n \\times n}$ and $\\det \\mathbf{Y}(t) \\ne 0$.<br><br>\n<b>Step 2: Differentiate the quotient</b><br>\nUsing the matrix product rule and derivative of inverse $\\frac{d}{dt}[\\mathbf{Y}^{-1}] = -\\mathbf{Y}^{-1} \\mathbf{Y}' \\mathbf{Y}^{-1}$:\n$$\\mathbf{R}' = \\mathbf{X}' \\mathbf{Y}^{-1} + \\mathbf{X} (\\mathbf{Y}^{-1})' = \\mathbf{X}' \\mathbf{Y}^{-1} - \\mathbf{X} \\mathbf{Y}^{-1} \\mathbf{Y}' \\mathbf{Y}^{-1} = (\\mathbf{X}' - \\mathbf{R} \\mathbf{Y}') \\mathbf{Y}^{-1}$$\n<br><b>Step 3: Equate to Riccati expression</b><br>\n$$\\mathbf{R}' = \\mathbf{B} - \\mathbf{R} \\mathbf{D} \\mathbf{R} = \\mathbf{B} - \\mathbf{R} \\mathbf{D} \\mathbf{X} \\mathbf{Y}^{-1}$$\nEquating both expressions and post-multiplying by $\\mathbf{Y}$:\n$$\\mathbf{X}' - \\mathbf{R} \\mathbf{Y}' = \\mathbf{B} \\mathbf{Y} - \\mathbf{R} \\mathbf{D} \\mathbf{X}$$\nRearranging terms by isolating $\\mathbf{R}$:\n$$\\mathbf{X}' - \\mathbf{B} \\mathbf{Y} = \\mathbf{R} (\\mathbf{Y}' - \\mathbf{D} \\mathbf{X})$$\n<br><b>Step 4: Decouple into Linear System</b><br>\nThis identity holds identically if both parenthetical sides vanish:\n$$\\mathbf{X}' = \\mathbf{B} \\mathbf{Y}, \\quad \\mathbf{Y}' = \\mathbf{D} \\mathbf{X}$$\nStacking state vectors $\\vec{z} = \\begin{pmatrix} \\mathbf{X} \\\\ \\mathbf{Y} \\end{pmatrix}$:\n$$\\frac{d}{dt} \\begin{pmatrix} \\mathbf{X} \\\\ \\mathbf{Y} \\end{pmatrix} = \\begin{pmatrix} \\mathbf{0} & \\mathbf{B} \\\\ \\mathbf{D} & \\mathbf{0} \\end{pmatrix} \\begin{pmatrix} \\mathbf{X} \\\\ \\mathbf{Y} \\end{pmatrix}$$\nThis establishes that the solution of the nonlinear Riccati equation is $\\mathbf{R}(t) = \\mathbf{X}(t)\\mathbf{Y}^{-1}(t)$ generated by the linear flow map $e^{\\mathbf{H}t}$.",
          "answer": "$\\mathbf{R}(t) = \\mathbf{X}(t)\\mathbf{Y}(t)^{-1}$ where $\\frac{d}{dt}\\begin{pmatrix} \\mathbf{X} \\\\ \\mathbf{Y} \\end{pmatrix} = \\begin{pmatrix} \\mathbf{0} & \\mathbf{B} \\\\ \\mathbf{D} & \\mathbf{0} \\end{pmatrix} \\begin{pmatrix} \\mathbf{X} \\\\ \\mathbf{Y} \\end{pmatrix}$.",
          "difficulty": "Hard"
        }
      ]
    },
    {
      "number": 2,
      "title": "Homogeneous Matrix Systems with Constant Coefficients & Generalized Eigenvectors",
      "leadSummary": "Algebraic spectral theory of first-order vector equations: real distinct eigenvalues, complex conjugate modes and rotation matrices, defective matrices, and chains of generalized eigenvectors.",
      "simulations": [
        "ode2-eigen-decomp-sim"
      ],
      "sections": [
        {
          "secNumber": "2.1",
          "title": "The Matrix System x' = Ax with Real Distinct Eigenvalues",
          "content": "<h3>1. Eigenpair Formulation</h3>\n<p>To solve the homogeneous system $\\vec{x}' = \\mathbf{A}\\vec{x}$ where $\\mathbf{A} \\in \\mathbb{R}^{n \\times n}$ is a constant matrix, we seek exponential vector solutions of the form $\\vec{x}(t) = e^{\\lambda t} \\vec{v}$. Substituting into the system:</p>\n$$\\lambda e^{\\lambda t} \\vec{v} = \\mathbf{A} e^{\\lambda t} \\vec{v} \\implies (\\mathbf{A} - \\lambda \\mathbf{I}) \\vec{v} = \\vec{0}$$\n<p>Non-trivial solutions $\\vec{v} \\ne \\vec{0}$ exist if and only if $\\lambda$ satisfies the characteristic equation $\\det(\\mathbf{A} - \\lambda \\mathbf{I}) = 0$.</p>\n<p>If $\\mathbf{A}$ possesses $n$ real distinct eigenvalues $\\lambda_1, \\lambda_2, \\dots, \\lambda_n$, the corresponding eigenvectors $\\vec{v}_1, \\vec{v}_2, \\dots, \\vec{v}_n$ are linearly independent in $\\mathbb{R}^n$. The general solution is a linear superposition of the fundamental modes:</p>\n$$\\vec{x}(t) = \\sum_{k=1}^n c_k e^{\\lambda_k t} \\vec{v}_k = c_1 e^{\\lambda_1 t} \\vec{v}_1 + c_2 e^{\\lambda_2 t} \\vec{v}_2 + \\dots + c_n e^{\\lambda_n t} \\vec{v}_n$$"
        },
        {
          "secNumber": "2.2",
          "title": "Complex Conjugate Eigenvalues, Elliptic Orbits & Spiral Stability",
          "content": "<h3>1. Real Solutions from Complex Eigenpairs</h3>\n<p>When the real matrix $\\mathbf{A}$ possesses a complex conjugate pair of eigenvalues $\\lambda = \\alpha \\pm i\\beta$ ($\\beta \\ne 0$), the corresponding eigenvector is also complex: $\\vec{v} = \\vec{u} + i\\vec{w}$ where $\\vec{u}, \\vec{w} \\in \\mathbb{R}^n$. The complex solution is:</p>\n$$\\vec{z}(t) = e^{(\\alpha + i\\beta)t} (\\vec{u} + i\\vec{w}) = e^{\\alpha t} (\\cos\\beta t + i\\sin\\beta t)(\\vec{u} + i\\vec{w})$$\n<p>Splitting $\\vec{z}(t)$ into its real and imaginary parts $\\vec{z}(t) = \\vec{x}_1(t) + i\\vec{x}_2(t)$:</p>\n$$\\begin{aligned}\n\\vec{x}_1(t) &= \\text{Re}[\\vec{z}(t)] = e^{\\alpha t} (\\vec{u} \\cos\\beta t - \\vec{w} \\sin\\beta t) \\\\\n\\vec{x}_2(t) &= \\text{Im}[\\vec{z}(t)] = e^{\\alpha t} (\\vec{u} \\sin\\beta t + \\vec{w} \\cos\\beta t)\n\\end{aligned}$$\n<div class=\"math-theorem\">\n<b>Theorem 2.1:</b> The vector functions $\\vec{x}_1(t)$ and $\\vec{x}_2(t)$ are linearly independent real solutions of $\\vec{x}' = \\mathbf{A}\\vec{x}$ on $\\mathbb{R}$. Their span describes a 2D plane in which orbits rotate with angular frequency $\\beta$ while expanding ($\\alpha > 0$) or decaying ($\\alpha < 0$) exponentially.\n</div>"
        },
        {
          "secNumber": "2.3",
          "title": "Repeated Eigenvalues, Defective Matrices & Chains of Generalized Eigenvectors",
          "simulation": "ode2-eigen-decomp-sim",
          "content": "<h3>1. Algebraic vs Geometric Multiplicity</h3>\n<p>Let $\\lambda$ be an eigenvalue of $\\mathbf{A}$ with algebraic multiplicity $m_a = k$ (meaning $(\\lambda - \\lambda_0)^k$ divides the characteristic polynomial). The geometric multiplicity $m_g = \\dim \\ker(\\mathbf{A} - \\lambda \\mathbf{I})$ is the number of linearly independent eigenvectors associated with $\\lambda$.</p>\n<p>If $m_g < m_a$, the matrix $\\mathbf{A}$ is called <b>defective</b>. In this case, ordinary eigenvectors cannot span the full solution subspace, requiring <b>generalized eigenvectors</b>.</p>\n\n<h3>2. Chains of Generalized Eigenvectors</h3>\n<p>A chain of generalized eigenvectors $\\{\\vec{v}_1, \\vec{v}_2, \\dots, \\vec{v}_k\\}$ associated with eigenvalue $\\lambda$ satisfies:</p>\n$$\\begin{aligned}\n(\\mathbf{A} - \\lambda \\mathbf{I}) \\vec{v}_1 &= \\vec{0} \\quad (\\text{genuine eigenvector}) \\\\\n(\\mathbf{A} - \\lambda \\mathbf{I}) \\vec{v}_2 &= \\vec{v}_1 \\implies (\\mathbf{A} - \\lambda \\mathbf{I})^2 \\vec{v}_2 = \\vec{0} \\\\\n(\\mathbf{A} - \\lambda \\mathbf{I}) \\vec{v}_3 &= \\vec{v}_2 \\implies (\\mathbf{A} - \\lambda \\mathbf{I})^3 \\vec{v}_3 = \\vec{0} \\\\\n&\\;\\;\\vdots \\\\\n(\\mathbf{A} - \\lambda \\mathbf{I}) \\vec{v}_k &= \\vec{v}_{k-1} \\implies (\\mathbf{A} - \\lambda \\mathbf{I})^k \\vec{v}_k = \\vec{0}\n\\end{aligned}$$\n\n<h3>3. Form of Independent Solutions</h3>\n<p>For a chain of length 2 ($\\vec{v}_1, \\vec{v}_2$), the two linearly independent solutions are:</p>\n$$\\begin{aligned}\n\\vec{x}_1(t) &= e^{\\lambda t} \\vec{v}_1 \\\\\n\\vec{x}_2(t) &= e^{\\lambda t} (t \\vec{v}_1 + \\vec{v}_2)\n\\end{aligned}$$\n<p>For a chain of length 3 ($\\vec{v}_1, \\vec{v}_2, \\vec{v}_3$):</p>\n$$\\vec{x}_3(t) = e^{\\lambda t} \\left( \\frac{t^2}{2} \\vec{v}_1 + t \\vec{v}_2 + \\vec{v}_3 \\right)$$\n<p>This matches the Taylor expansion of $e^{\\mathbf{A}t} \\vec{v}_k = e^{\\lambda t} e^{(\\mathbf{A} - \\lambda \\mathbf{I})t} \\vec{v}_k$.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-02",
          "tier": 1,
          "difficultyLabel": "Tier 1 • Foundational",
          "title": "Matrix Exponential for Defective Repeated Eigenvalue Matrix",
          "statement": "Compute the matrix exponential $e^{\\mathbf{A}t}$ for the defective matrix:<br>$$\\mathbf{A} = \\begin{pmatrix} 2 & 1 \\\\ 0 & 2 \\end{pmatrix}$$",
          "solution": "<b>Step 1: Nilpotent Decomposition</b><br>\nNotice that $\\mathbf{A}$ can be split into a scalar multiple of identity and a nilpotent upper-triangular matrix:\n$$\\mathbf{A} = 2\\mathbf{I} + \\mathbf{N}, \\quad \\text{where } \\mathbf{N} = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix}$$\nObserve that $\\mathbf{N}^2 = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} = \\begin{pmatrix} 0 & 0 \\\\ 0 & 0 \\end{pmatrix}$. Thus $\\mathbf{N}$ is nilpotent of degree 2.<br><br>\n<b>Step 2: Commuting Matrices Property</b><br>\nSince $(2\\mathbf{I}t)(\\mathbf{N}t) = (\\mathbf{N}t)(2\\mathbf{I}t)$, we can multiply their exponentials:\n$$e^{\\mathbf{A}t} = e^{2\\mathbf{I}t + \\mathbf{N}t} = e^{2\\mathbf{I}t} e^{\\mathbf{N}t}$$\n<br><b>Step 3: Exponentiation of Terms</b><br>\n$$e^{2\\mathbf{I}t} = e^{2t} \\mathbf{I} = \\begin{pmatrix} e^{2t} & 0 \\\\ 0 & e^{2t} \\end{pmatrix}$$\n$$e^{\\mathbf{N}t} = \\mathbf{I} + t\\mathbf{N} + \\frac{t^2}{2!} \\mathbf{N}^2 + \\dots = \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix} + t \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} = \\begin{pmatrix} 1 & t \\\\ 0 & 1 \\end{pmatrix}$$\n<br><b>Step 4: Matrix Multiplication</b><br>\n$$e^{\\mathbf{A}t} = e^{2t} \\begin{pmatrix} 1 & t \\\\ 0 & 1 \\end{pmatrix} = \\begin{pmatrix} e^{2t} & t e^{2t} \\\\ 0 & e^{2t} \\end{pmatrix}$$",
          "answer": "$e^{\\mathbf{A}t} = \\begin{pmatrix} e^{2t} & t e^{2t} \\\\ 0 & e^{2t} \\end{pmatrix}$",
          "difficulty": "Easy"
        },
        {
          "id": "prob-10",
          "tier": 2,
          "difficultyLabel": "Tier 2 • Intermediate Exam",
          "title": "Putzer's Algorithm for 3x3 Nilpotent Jordan Block",
          "statement": "Use Putzer's algorithm to compute the matrix exponential $e^{\\mathbf{A}t}$ for the $3 \\times 3$ matrix:<br>$$\\mathbf{A} = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 1 \\\\ 0 & 0 & 0 \\end{pmatrix}$$",
          "solution": "<b>Step 1: Eigenvalues</b><br>\nThe characteristic polynomial is $\\det(\\mathbf{A} - \\lambda \\mathbf{I}) = -\\lambda^3 = 0 \\implies \\lambda_1 = \\lambda_2 = \\lambda_3 = 0$.<br><br>\n<b>Step 2: Putzer's polynomial matrices $\\mathbf{P}_k$</b><br>\n$$\\mathbf{P}_0 = \\mathbf{I} = \\begin{pmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$$\n$$\\mathbf{P}_1 = \\mathbf{A} - \\lambda_1 \\mathbf{I} = \\mathbf{A} = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 1 \\\\ 0 & 0 & 0 \\end{pmatrix}$$\n$$\\mathbf{P}_2 = (\\mathbf{A} - \\lambda_2 \\mathbf{I})\\mathbf{P}_1 = \\mathbf{A}^2 = \\begin{pmatrix} 0 & 0 & 1 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix}$$\n<br><b>Step 3: Scalar differential equations for $r_k(t)$</b><br>\n$r_1'(t) = 0, r_1(0) = 1 \\implies r_1(t) = 1$.<br>\n$r_2'(t) = r_1(t) = 1, r_2(0) = 0 \\implies r_2(t) = t$.<br>\n$r_3'(t) = r_2(t) = t, r_3(0) = 0 \\implies r_3(t) = \\frac{t^2}{2}$.<br><br>\n<b>Step 4: Matrix exponential assembly</b><br>\n$$e^{\\mathbf{A}t} = r_1(t)\\mathbf{P}_0 + r_2(t)\\mathbf{P}_1 + r_3(t)\\mathbf{P}_2 = \\mathbf{I} + t\\mathbf{A} + \\frac{t^2}{2}\\mathbf{A}^2 = \\begin{pmatrix} 1 & t & t^2/2 \\\\ 0 & 1 & t \\\\ 0 & 0 & 1 \\end{pmatrix}$$",
          "answer": "$e^{\\mathbf{A}t} = \\begin{pmatrix} 1 & t & t^2/2 \\\\ 0 & 1 & t \\\\ 0 & 0 & 1 \\end{pmatrix}$",
          "difficulty": "Medium"
        },
        {
          "id": "prob-18",
          "tier": 3,
          "difficultyLabel": "Tier 3 • Honors Challenge",
          "title": "Jordan Canonical Form Derivation for Highly Defective 3x3 System",
          "statement": "Solve the defective system $\\vec{x}' = \\mathbf{A}\\vec{x}$ where $\\mathbf{A} = \\begin{pmatrix} 3 & 1 & 0 \\\\ 0 & 3 & 1 \\\\ 0 & 0 & 3 \\end{pmatrix}$ using generalized eigenvector chains.",
          "solution": "<b>Step 1: Spectral Analysis</b><br>\nThe characteristic polynomial is $(\\lambda - 3)^3 = 0 \\implies \\lambda = 3$ with algebraic multiplicity $m_a = 3$.\nThe null space $(\\mathbf{A} - 3\\mathbf{I})\\vec{v} = \\vec{0}$ has rank 2, so the geometric multiplicity is $m_g = 3 - 2 = 1$. The matrix is defective with a single Jordan block of size 3.<br><br>\n<b>Step 2: Construct the Jordan Chain</b><br>\nWe seek a generalized eigenvector $\\vec{v}_3$ of rank 3:\n$$(\\mathbf{A} - 3\\mathbf{I})^3 = \\mathbf{0}, \\quad (\\mathbf{A} - 3\\mathbf{I})^2 \\vec{v}_3 \\ne \\vec{0}$$\n$$\\mathbf{A} - 3\\mathbf{I} = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 1 \\\\ 0 & 0 & 0 \\end{pmatrix}, \\quad (\\mathbf{A} - 3\\mathbf{I})^2 = \\begin{pmatrix} 0 & 0 & 1 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix}$$\nChoose $\\vec{v}_3 = \\begin{pmatrix} 0 \\\\ 0 \\\\ 1 \\end{pmatrix}$.\nThen:\n$$\\vec{v}_2 = (\\mathbf{A} - 3\\mathbf{I}) \\vec{v}_3 = \\begin{pmatrix} 0 \\\\ 1 \\\\ 0 \\end{pmatrix}$$\n$$\\vec{v}_1 = (\\mathbf{A} - 3\\mathbf{I}) \\vec{v}_2 = \\begin{pmatrix} 1 \\\\ 0 \\\\ 0 \\end{pmatrix} \\quad (\\text{genuine eigenvector})$$\n<br><b>Step 3: Construct Three Linearly Independent Solutions</b><br>\n$$\\begin{aligned}\n\\vec{x}_1(t) &= e^{3t} \\vec{v}_1 = e^{3t} \\begin{pmatrix} 1 \\\\ 0 \\\\ 0 \\end{pmatrix} \\\\\n\\vec{x}_2(t) &= e^{3t} (t \\vec{v}_1 + \\vec{v}_2) = e^{3t} \\begin{pmatrix} t \\\\ 1 \\\\ 0 \\end{pmatrix} \\\\\n\\vec{x}_3(t) &= e^{3t} \\left( \\frac{t^2}{2} \\vec{v}_1 + t \\vec{v}_2 + \\vec{v}_3 \\right) = e^{3t} \\begin{pmatrix} t^2/2 \\\\ t \\\\ 1 \\end{pmatrix}\n\\end{aligned}$$\n<br><b>Step 4: General Solution</b><br>\n$$\\vec{x}(t) = e^{3t} \\begin{pmatrix} c_1 + c_2 t + c_3 \\frac{t^2}{2} \\\\ c_2 + c_3 t \\\\ c_3 \\end{pmatrix}$$",
          "answer": "$\\vec{x}(t) = e^{3t} \\begin{pmatrix} c_1 + c_2 t + c_3 \\frac{t^2}{2} \\\\ c_2 + c_3 t \\\\ c_3 \\end{pmatrix}$",
          "difficulty": "Hard"
        }
      ]
    },
    {
      "number": 3,
      "title": "The Fundamental Matrix, Matrix Exponential & Nonhomogeneous Systems",
      "leadSummary": "Fundamental matrix manifolds, the matrix exponential operator e^(At) via Putzer's algorithm, and nonhomogeneous systems via matrix variation of parameters.",
      "simulations": [
        "ode2-matrix-exp-sim"
      ],
      "sections": [
        {
          "secNumber": "3.1",
          "title": "The Fundamental Matrix Φ(t), System Wronskian & Abel-Liouville Identity",
          "content": "<h3>1. The Fundamental Matrix</h3>\n<p>Let $\\vec{x}_1(t), \\vec{x}_2(t), \\dots, \\vec{x}_n(t)$ be $n$ linearly independent solutions of $\\vec{x}' = \\mathbf{A}(t)\\vec{x}$ on an interval $I$. The $n \\times n$ matrix whose columns are these solution vectors:</p>\n$$\\mathbf{\\Phi}(t) = \\begin{pmatrix} \\vec{x}_1(t) & \\vec{x}_2(t) & \\dots & \\vec{x}_n(t) \\end{pmatrix}$$\n<p>is called a <b>fundamental matrix</b> of the system. By construction, it satisfies the matrix differential equation:</p>\n$$\\frac{d\\mathbf{\\Phi}}{dt} = \\mathbf{A}(t) \\mathbf{\\Phi}(t)$$\n<p>The general homogeneous solution is simply $\\vec{x}(t) = \\mathbf{\\Phi}(t)\\vec{c}$ where $\\vec{c} \\in \\mathbb{R}^n$ is a constant vector.</p>\n\n<h3>2. The System Wronskian & Abel-Liouville Formula</h3>\n<p>The Wronskian determinant of the system is $W(t) = \\det \\mathbf{\\Phi}(t)$. Differentiating the determinant:</p>\n$$\\frac{dW}{dt} = \\text{Tr}(\\mathbf{A}(t)) W(t)$$\n<div class=\"math-theorem\">\n<b>Theorem 3.1 (Abel-Liouville Identity for Systems):</b> For any fundamental matrix $\\mathbf{\\Phi}(t)$ on $I$, and any $t_0 \\in I$:\n$$W(t) = W(t_0) \\exp\\left( \\int_{t_0}^t \\text{Tr}(\\mathbf{A}(s))\\,ds \\right)$$\nConsequently, $W(t) \\ne 0$ for all $t \\in I$ if and only if $W(t_0) \\ne 0$.\n</div>"
        },
        {
          "secNumber": "3.2",
          "title": "The Matrix Exponential e^(At): Putzer's Algorithm, Cayley-Hamilton & Series",
          "simulation": "ode2-matrix-exp-sim",
          "content": "<h3>1. The Matrix Exponential Operator</h3>\n<p>For any constant square matrix $\\mathbf{A} \\in \\mathbb{C}^{n \\times n}$, the matrix exponential is defined by the absolutely convergent power series:</p>\n$$e^{\\mathbf{A}t} = \\sum_{k=0}^\\infty \\frac{t^k}{k!} \\mathbf{A}^k = \\mathbf{I} + t\\mathbf{A} + \\frac{t^2}{2!} \\mathbf{A}^2 + \\frac{t^3}{3!} \\mathbf{A}^3 + \\dots$$\n<p>The matrix exponential $e^{\\mathbf{A}t}$ is the unique fundamental matrix that equals the identity at $t = 0$: $\\mathbf{\\Phi}(0) = \\mathbf{I}$. The unique solution to the IVP $\\vec{x}' = \\mathbf{A}\\vec{x}, \\vec{x}(0) = \\vec{x}_0$ is:</p>\n$$\\vec{x}(t) = e^{\\mathbf{A}t} \\vec{x}_0$$\n\n<h3>2. Putzer's Algorithm</h3>\n<p>Putzer's algorithm computes $e^{\\mathbf{A}t}$ without matrix inversions or Jordan canonical forms. Let $\\lambda_1, \\lambda_2, \\dots, \\lambda_n$ be the eigenvalues of $\\mathbf{A}$ in any order. Define the polynomial sequence of matrices:</p>\n$$\\mathbf{P}_0 = \\mathbf{I}, \\quad \\mathbf{P}_k = \\prod_{j=1}^k (\\mathbf{A} - \\lambda_j \\mathbf{I}) = (\\mathbf{A} - \\lambda_k \\mathbf{I}) \\mathbf{P}_{k-1}, \\quad k = 1, \\dots, n-1$$\n<p>Then the matrix exponential is expressed as:</p>\n$$e^{\\mathbf{A}t} = \\sum_{k=0}^{n-1} r_{k+1}(t) \\mathbf{P}_k$$\n<p>where the scalar functions $r_1(t), \\dots, r_n(t)$ satisfy the triangular scalar differential system:</p>\n$$\\begin{aligned}\nr_1'(t) &= \\lambda_1 r_1(t), \\quad r_1(0) = 1 \\\\\nr_k'(t) &= \\lambda_k r_k(t) + r_{k-1}(t), \\quad r_k(0) = 0 \\quad (k = 2, \\dots, n)\n\\end{aligned}$$"
        },
        {
          "secNumber": "3.3",
          "title": "Nonhomogeneous Systems: Undetermined Coefficients & Variation of Parameters",
          "content": "<h3>1. Matrix Variation of Parameters</h3>\n<p>Consider the nonhomogeneous linear system $\\vec{x}'(t) = \\mathbf{A}(t)\\vec{x}(t) + \\vec{g}(t)$. Let $\\mathbf{\\Phi}(t)$ be a fundamental matrix for the associated homogeneous system $\\vec{x}' = \\mathbf{A}(t)\\vec{x}$. We seek a particular solution of the form:</p>\n$$\\vec{x}_p(t) = \\mathbf{\\Phi}(t) \\vec{u}(t)$$\n<p>Differentiating using the product rule:</p>\n$$\\vec{x}_p'(t) = \\mathbf{\\Phi}'(t) \\vec{u}(t) + \\mathbf{\\Phi}(t) \\vec{u}'(t) = \\mathbf{A}(t) \\mathbf{\\Phi}(t) \\vec{u}(t) + \\mathbf{\\Phi}(t) \\vec{u}'(t)$$\n<p>Substituting into the nonhomogeneous equation:</p>\n$$\\mathbf{A}(t) \\mathbf{\\Phi}(t) \\vec{u}(t) + \\mathbf{\\Phi}(t) \\vec{u}'(t) = \\mathbf{A}(t) \\mathbf{\\Phi}(t) \\vec{u}(t) + \\vec{g}(t)$$\n$$\\mathbf{\\Phi}(t) \\vec{u}'(t) = \\vec{g}(t) \\implies \\vec{u}'(t) = \\mathbf{\\Phi}^{-1}(t) \\vec{g}(t)$$\n<div class=\"math-theorem\">\n<b>Theorem 3.2 (Variation of Parameters Formula for Systems):</b> Integrating $\\vec{u}'(t)$ from $t_0$ to $t$ yields the complete general solution:\n$$\\vec{x}(t) = \\mathbf{\\Phi}(t)\\mathbf{\\Phi}^{-1}(t_0) \\vec{x}_0 + \\mathbf{\\Phi}(t) \\int_{t_0}^t \\mathbf{\\Phi}^{-1}(s) \\vec{g}(s)\\,ds$$\nFor constant matrix $\\mathbf{A}$, where $\\mathbf{\\Phi}(t) = e^{\\mathbf{A}t}$, this simplifies to Duhamel's convolution integral:\n$$\\vec{x}(t) = e^{\\mathbf{A}(t - t_0)} \\vec{x}_0 + \\int_{t_0}^t e^{\\mathbf{A}(t - s)} \\vec{g}(s)\\,ds$$\n</div>"
        }
      ],
      "problems": [
        {
          "id": "prob-03",
          "tier": 1,
          "difficultyLabel": "Tier 1 • Foundational",
          "title": "Variation of Parameters for Nonhomogeneous 2x2 System",
          "statement": "Find a particular solution using Variation of Parameters for the system:<br>$$\\vec{x}' = \\begin{pmatrix} 0 & 1 \\\\ -2 & 3 \\end{pmatrix} \\vec{x} + \\begin{pmatrix} 0 \\\\ e^t \\end{pmatrix}$$",
          "solution": "<b>Step 1: Homogeneous eigenvalues and eigenvectors</b><br>\n$\\det(\\mathbf{A} - \\lambda \\mathbf{I}) = \\lambda^2 - 3\\lambda + 2 = (\\lambda - 1)(\\lambda - 2) = 0 \\implies \\lambda_1 = 1, \\lambda_2 = 2$.<br>\nFor $\\lambda_1 = 1$: $(\\mathbf{A} - \\mathbf{I})\\vec{v}_1 = \\begin{pmatrix} -1 & 1 \\\\ -2 & 2 \\end{pmatrix} \\begin{pmatrix} v_1 \\\\ v_2 \\end{pmatrix} = \\vec{0} \\implies \\vec{v}_1 = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}$.<br>\nFor $\\lambda_2 = 2$: $(\\mathbf{A} - 2\\mathbf{I})\\vec{v}_2 = \\begin{pmatrix} -2 & 1 \\\\ -2 & 1 \\end{pmatrix} \\begin{pmatrix} v_1 \\\\ v_2 \\end{pmatrix} = \\vec{0} \\implies \\vec{v}_2 = \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix}$.<br><br>\n<b>Step 2: Fundamental Matrix $\\mathbf{\\Phi}(t)$</b><br>\n$$\\mathbf{\\Phi}(t) = \\begin{pmatrix} e^t & e^{2t} \\\\ e^t & 2e^{2t} \\end{pmatrix}, \\quad \\det \\mathbf{\\Phi}(t) = 2e^{3t} - e^{3t} = e^{3t}$$\n$$\\mathbf{\\Phi}^{-1}(t) = \\frac{1}{e^{3t}} \\begin{pmatrix} 2e^{2t} & -e^{2t} \\\\ -e^t & e^t \\end{pmatrix} = \\begin{pmatrix} 2e^{-t} & -e^{-t} \\\\ -e^{-2t} & e^{-2t} \\end{pmatrix}$$\n<br><b>Step 3: Integrate $\\vec{u}'(t) = \\mathbf{\\Phi}^{-1}(t) \\vec{g}(t)$</b><br>\n$$\\vec{u}'(t) = \\begin{pmatrix} 2e^{-t} & -e^{-t} \\\\ -e^{-2t} & e^{-2t} \\end{pmatrix} \\begin{pmatrix} 0 \\\\ e^t \\end{pmatrix} = \\begin{pmatrix} -1 \\\\ e^{-t} \\end{pmatrix}$$\nIntegrating with respect to $t$:\n$$\\vec{u}(t) = \\begin{pmatrix} -t \\\\ -e^{-t} \\end{pmatrix}$$\n<br><b>Step 4: Form Particular Solution $\\vec{x}_p(t) = \\mathbf{\\Phi}(t) \\vec{u}(t)$</b><br>\n$$\\vec{x}_p(t) = \\begin{pmatrix} e^t & e^{2t} \\\\ e^t & 2e^{2t} \\end{pmatrix} \\begin{pmatrix} -t \\\\ -e^{-t} \\end{pmatrix} = \\begin{pmatrix} -t e^t - e^t \\\\ -t e^t - 2e^t \\end{pmatrix}$$",
          "answer": "$\\vec{x}_p(t) = \\begin{pmatrix} -(t + 1)e^t \\\\ -(t + 2)e^t \\end{pmatrix}$",
          "difficulty": "Easy"
        },
        {
          "id": "prob-13",
          "tier": 2,
          "difficultyLabel": "Tier 2 • Intermediate Exam",
          "title": "Bessel Differential Recurrence & Integral Evaluation",
          "statement": "Prove the recurrence identity $\\frac{d}{dx}[x^\\nu J_\\nu(x)] = x^\\nu J_{\\nu-1}(x)$ and use it to evaluate $\\int x^3 J_0(x)\\,dx$.",
          "solution": "<b>Step 1: Proof of identity</b><br>\nFrom the series definition:\n$$x^\\nu J_\\nu(x) = \\sum_{m=0}^\\infty \\frac{(-1)^m}{m!\\, \\Gamma(m + \\nu + 1)} \\frac{x^{2m + 2\\nu}}{2^{2m + \\nu}}$$\nDifferentiating with respect to $x$:\n$$\\frac{d}{dx}[x^\\nu J_\\nu(x)] = \\sum_{m=0}^\\infty \\frac{(-1)^m (2m + 2\\nu)}{m!\\, \\Gamma(m + \\nu + 1)} \\frac{x^{2m + 2\\nu - 1}}{2^{2m + \\nu}}$$\nSince $2m + 2\\nu = 2(m + \\nu)$ and $\\Gamma(m + \\nu + 1) = (m + \\nu)\\Gamma(m + \\nu)$:\n$$= x^\\nu \\sum_{m=0}^\\infty \\frac{(-1)^m}{m!\\, \\Gamma(m + \\nu)} \\left(\\frac{x}{2}\\right)^{2m + \\nu - 1} = x^\\nu J_{\\nu-1}(x)$$\n<br><b>Step 2: Integration of $\\int x^3 J_0(x)\\,dx$</b><br>\nRewrite integrand as $x^2 \\cdot [x J_0(x)]$.\nFrom identity with $\\nu = 1$: $\\frac{d}{dx}[x J_1(x)] = x J_0(x) \\implies \\int x J_0(x)\\,dx = x J_1(x)$.<br>\nIntegrate by parts:\n$$u = x^2 \\implies du = 2x\\,dx, \\quad dv = x J_0(x)\\,dx \\implies v = x J_1(x)$$\n$$\\int x^3 J_0(x)\\,dx = x^2 [x J_1(x)] - \\int [x J_1(x)](2x)\\,dx = x^3 J_1(x) - 2 \\int x^2 J_1(x)\\,dx$$\nNow apply identity with $\\nu = 2$: $\\frac{d}{dx}[x^2 J_2(x)] = x^2 J_1(x) \\implies \\int x^2 J_1(x)\\,dx = x^2 J_2(x)$.<br>\n$$= x^3 J_1(x) - 2 x^2 J_2(x) + C$$\nUsing recurrence $J_2(x) = \\frac{2}{x} J_1(x) - J_0(x)$:\n$$x^3 J_1(x) - 2x^2 \\left( \\frac{2}{x} J_1(x) - J_0(x) \\right) = (x^3 - 4x) J_1(x) + 2x^2 J_0(x) + C$$",
          "answer": "$\\int x^3 J_0(x)\\,dx = x^3 J_1(x) - 2x^2 J_2(x) + C = (x^3 - 4x)J_1(x) + 2x^2 J_0(x) + C$",
          "difficulty": "Medium"
        },
        {
          "id": "prob-21",
          "tier": 3,
          "difficultyLabel": "Tier 3 • Honors Challenge",
          "title": "Associated Laguerre Transformation of Hydrogen Radial Schrödinger Equation",
          "statement": "Transform the radial hydrogenic Schrödinger equation $\\frac{d^2 R}{dr^2} + \\frac{2}{r} \\frac{dR}{dr} + \\left[ \\frac{2Z}{r} - \\frac{l(l+1)}{r^2} - \\kappa^2 \\right] R = 0$ into the confluent hypergeometric Associated Laguerre equation.",
          "solution": "<b>Step 1: Asymptotic Behavior</b><br>\nAs $r \\to \\infty$: $R'' - \\kappa^2 R \\approx 0 \\implies R(r) \\sim e^{-\\kappa r}$.<br>\nAs $r \\to 0$: $R'' + \\frac{2}{r} R' - \\frac{l(l+1)}{r^2} R \\approx 0 \\implies R(r) \\sim r^l$.<br><br>\n<b>Step 2: Dimensionless variable and ansatz</b><br>\nDefine dimensionless coordinate $\\rho = 2\\kappa r$.<br>\nLet $R(\\rho) = \\rho^l e^{-\\rho/2} v(\\rho)$.<br><br>\n<b>Step 3: Derivatives of the ansatz</b><br>\nCompute $R'$ and $R''$ in terms of $\\rho$ and substitute into the radial equation. After factorizing $\\rho^l e^{-\\rho/2}$, the equation reduces to:\n$$\\rho \\frac{d^2 v}{d\\rho^2} + [2(l + 1) - \\rho] \\frac{dv}{d\\rho} + (n - l - 1) v = 0$$\nwhere $n = \\frac{Z}{\\kappa}$ is the principal quantum number.<br><br>\n<b>Step 4: Associated Laguerre Polynomials</b><br>\nLet $k = 2l + 1$ and $p = n - l - 1 \\ge 0$. The equation becomes:\n$$\\rho v'' + (k + 1 - \\rho) v' + p v = 0$$\nwhich is precisely the <b>Associated Laguerre differential equation</b>!\nThe solutions are $v(\\rho) = L_{n - l - 1}^{2l + 1}(\\rho)$, proving that the bound state energy levels are quantized:\n$$E_n = -\\frac{\\hbar^2 \\kappa^2}{2\\mu} = -\\frac{\\mu Z^2 e^4}{2\\hbar^2 n^2}, \\quad n = l + 1, l + 2, \\dots$$",
          "answer": "$\\rho v'' + (2l + 2 - \\rho)v' + (n - l - 1)v = 0$ with solution $v(\\rho) = L_{n-l-1}^{2l+1}(2\\kappa r)$.",
          "difficulty": "Hard"
        }
      ]
    },
    {
      "number": 4,
      "title": "Series Solutions Near Ordinary Points & Legendre Differential Equation",
      "leadSummary": "Analytic function theory, power series expansions near ordinary points, recurrence relations, Legendre polynomials P_n(x), Rodrigues' formula, and complete orthogonality.",
      "simulations": [
        "ode2-legendre-series-sim"
      ],
      "sections": [
        {
          "secNumber": "4.1",
          "title": "Real Analytic Functions, Ordinary vs Singular Points & Complex Radius of Convergence",
          "content": "<h3>1. Classification of Points for Linear ODEs</h3>\n<p>Consider the second-order homogeneous linear differential equation written in standard normalized form:</p>\n$$y'' + P(x) y' + Q(x) y = 0$$\n<div class=\"math-theorem\">\n<b>Definition 4.1:</b> A point $x_0 \\in \\mathbb{R}$ is called an <b>ordinary point</b> of the ODE if both coefficient functions $P(x)$ and $Q(x)$ are real analytic at $x_0$; that is, both possess Taylor series expansions with non-zero radius of convergence:\n$$P(x) = \\sum_{n=0}^\\infty p_n (x - x_0)^n, \\quad Q(x) = \\sum_{n=0}^\\infty q_n (x - x_0)^n$$\nIf either $P(x)$ or $Q(x)$ fails to be analytic at $x_0$, then $x_0$ is called a <b>singular point</b>.\n</div>\n\n<h3>2. The Fuchs-Frobenius Radius of Convergence Theorem</h3>\n<div class=\"math-theorem\">\n<b>Theorem 4.1:</b> If $x_0$ is an ordinary point of $y'' + P(x)y' + Q(x)y = 0$, then every solution $y(x)$ is analytic at $x_0$ and can be expanded as a power series:\n$$y(x) = \\sum_{n=0}^\\infty a_n (x - x_0)^n = a_0 y_1(x) + a_1 y_2(x)$$\nwhere $y_1(x)$ and $y_2(x)$ are linearly independent analytic solutions. The radius of convergence $R$ of these series is at least equal to the distance from $x_0$ to the nearest singularity of $P(z)$ or $Q(z)$ in the <i>complex plane</i> $\\mathbb{C}$.\n</div>"
        },
        {
          "secNumber": "4.2",
          "title": "The Power Series Method Near an Ordinary Point & Recurrence Relations",
          "content": "<h3>1. The Systematic Power Series Algorithm</h3>\n<p>To solve $y'' + P(x)y' + Q(x)y = 0$ about $x_0 = 0$, we substitute:</p>\n$$y(x) = \\sum_{n=0}^\\infty a_n x^n, \\quad y'(x) = \\sum_{n=1}^\\infty n a_n x^{n-1}, \\quad y''(x) = \\sum_{n=2}^\\infty n(n - 1) a_n x^{n-2}$$\n<p>Shift summation indices so that every term involves $x^k$. Factoring $x^k$, linear independence of powers $\\{1, x, x^2, \\dots\\}$ requires that each coefficient bracket vanishes independently, yielding the <b>recurrence relation</b> for $a_{k+2}$ in terms of preceding coefficients.</p>\n<p>The constants $a_0 = y(0)$ and $a_1 = y'(0)$ remain completely arbitrary, parametrizing the fundamental solution pair:</p>\n$$y_1(x) = 1 + \\sum_{n=2}^\\infty c_n^{(1)} x^n \\quad (a_0 = 1, a_1 = 0), \\qquad y_2(x) = x + \\sum_{n=2}^\\infty c_n^{(2)} x^n \\quad (a_0 = 0, a_1 = 1)$$"
        },
        {
          "secNumber": "4.3",
          "title": "Legendre's Differential Equation, Legendre Polynomials P_n(x), Rodrigues' Formula & Orthogonality",
          "simulation": "ode2-legendre-series-sim",
          "content": "<h3>1. Legendre's Differential Equation</h3>\n<p>Legendre's differential equation arises ubiquitously in electrostatics, quantum mechanics, and gravitational potential theory when solving Laplace's equation in spherical coordinates:</p>\n$$(1 - x^2) y'' - 2x y' + \\alpha(\\alpha + 1) y = 0$$\n<p>Dividing by $1 - x^2$, the singular points are $x = \\pm 1$. The origin $x_0 = 0$ is an ordinary point. Substituting $y = \\sum a_n x^n$ yields the two-step recurrence relation:</p>\n$$a_{n+2} = -\\frac{(\\alpha - n)(\\alpha + n + 1)}{(n + 1)(n + 2)} a_n$$\n<p>When $\\alpha = n$ is a non-negative integer, the series terminates after the term $x^n$, producing a polynomial of degree $n$. Normalized such that $P_n(1) = 1$, these are the <b>Legendre Polynomials</b> $P_n(x)$:</p>\n$$P_0(x) = 1, \\quad P_1(x) = x, \\quad P_2(x) = \\frac{1}{2}(3x^2 - 1), \\quad P_3(x) = \\frac{1}{2}(5x^3 - 3x), \\quad P_4(x) = \\frac{1}{8}(35x^4 - 30x^2 + 3)$$\n\n<h3>2. Rodrigues' Formula & Orthogonality</h3>\n<div class=\"math-theorem\">\n<b>Rodrigues' Formula:</b>\n$$P_n(x) = \\frac{1}{2^n n!} \\frac{d^n}{dx^n} (x^2 - 1)^n$$\n<b>Orthogonality Relation:</b> The Legendre polynomials form a complete orthogonal set in $L^2[-1, 1]$:\n$$\\int_{-1}^1 P_n(x) P_m(x)\\,dx = \\frac{2}{2n + 1} \\delta_{nm}$$\n</div>"
        }
      ],
      "problems": [
        {
          "id": "prob-04",
          "tier": 1,
          "difficultyLabel": "Tier 1 • Foundational",
          "title": "Power Series Solution of Airy-Type Equation about x = 0",
          "statement": "Find the general power series solution about the ordinary point $x_0 = 0$ for:<br>$$y'' - x y = 0$$",
          "solution": "<b>Step 1: Series Substitution</b><br>\nLet $y = \\sum_{n=0}^\\infty a_n x^n$. Then:\n$$y'' = \\sum_{n=2}^\\infty n(n - 1) a_n x^{n-2}, \\quad x y = \\sum_{n=0}^\\infty a_n x^{n+1}$$\n<br><b>Step 2: Align Indices</b><br>\nLet $k$ be the power of $x$:\nIn $y''$: $k = n - 2 \\implies n = k + 2 \\implies \\sum_{k=0}^\\infty (k + 2)(k + 1) a_{k+2} x^k$.\nFor $k = 0$: $2(1) a_2 = 0 \\implies a_2 = 0$.\nFor $k \\ge 1$: let $j = k - 1 \\ge 0$, equating coefficients gives:\n$$(k + 2)(k + 1) a_{k+2} = a_{k-1} \\implies a_{k+2} = \\frac{a_{k-1}}{(k + 2)(k + 1)}$$\nSetting $k + 2 = n$:\n$$a_n = \\frac{a_{n-3}}{n(n - 1)} \\quad \\text{for } n \\ge 3$$\n<br><b>Step 3: Compute Coefficients</b><br>\nSince $a_2 = 0$, all terms $a_{3m+2} = 0$.<br>\nMultiples of 3 (governed by $a_0$):\n$$a_3 = \\frac{a_0}{3 \\cdot 2}, \\quad a_6 = \\frac{a_3}{6 \\cdot 5} = \\frac{a_0}{6 \\cdot 5 \\cdot 3 \\cdot 2}$$\nTerms of form $3m+1$ (governed by $a_1$):\n$$a_4 = \\frac{a_1}{4 \\cdot 3}, \\quad a_7 = \\frac{a_4}{7 \\cdot 6} = \\frac{a_1}{7 \\cdot 6 \\cdot 4 \\cdot 3}$$\n<br><b>Step 4: Solution</b><br>\n$$y(x) = a_0 \\left( 1 + \\frac{x^3}{6} + \\frac{x^6}{180} + \\dots \\right) + a_1 \\left( x + \\frac{x^4}{12} + \\frac{x^7}{504} + \\dots \\right)$$",
          "answer": "$y(x) = a_0 \\left(1 + \\frac{x^3}{6} + \\frac{x^6}{180} + \\dots\\right) + a_1 \\left(x + \\frac{x^4}{12} + \\frac{x^7}{504} + \\dots\\right)$",
          "difficulty": "Easy"
        },
        {
          "id": "prob-06",
          "tier": 1,
          "difficultyLabel": "Tier 1 • Foundational",
          "title": "Legendre Polynomial P_3(x) and Orthogonality Verification",
          "statement": "Derive $P_3(x)$ via Rodrigues' formula and verify the orthogonality $\\int_{-1}^1 P_1(x) P_3(x)\\,dx = 0$.",
          "solution": "<b>Step 1: Rodrigues' Formula for $n = 3$</b><br>\n$$P_3(x) = \\frac{1}{2^3 \\cdot 3!} \\frac{d^3}{dx^3} (x^2 - 1)^3 = \\frac{1}{48} \\frac{d^3}{dx^3} (x^6 - 3x^4 + 3x^2 - 1)$$\nFirst derivative:\n$$\\frac{d}{dx}(x^6 - 3x^4 + 3x^2 - 1) = 6x^5 - 12x^3 + 6x$$\nSecond derivative:\n$$\\frac{d^2}{dx^2} = 30x^4 - 36x^2 + 6$$\nThird derivative:\n$$\\frac{d^3}{dx^3} = 120x^3 - 72x$$\nDividing by 48:\n$$P_3(x) = \\frac{120x^3 - 72x}{48} = \\frac{5}{2}x^3 - \\frac{3}{2}x = \\frac{1}{2}(5x^3 - 3x)$$\n<br><b>Step 2: Orthogonality integral with $P_1(x) = x$</b><br>\n$$\\int_{-1}^1 P_1(x) P_3(x)\\,dx = \\int_{-1}^1 x \\cdot \\frac{1}{2}(5x^3 - 3x)\\,dx = \\frac{1}{2} \\int_{-1}^1 (5x^4 - 3x^2)\\,dx$$\nBecause the integrand is even:\n$$= \\int_0^1 (5x^4 - 3x^2)\\,dx = \\left[ x^5 - x^3 \\right]_0^1 = (1 - 1) - 0 = 0$$\nOrthogonality is verified identically!",
          "answer": "$P_3(x) = \\frac{1}{2}(5x^3 - 3x)$ and $\\int_{-1}^1 P_1(x)P_3(x)\\,dx = 0$.",
          "difficulty": "Easy"
        },
        {
          "id": "prob-19",
          "tier": 3,
          "difficultyLabel": "Tier 3 • Honors Challenge",
          "title": "Complete Legendre Series Expansion & Parseval's Identity",
          "statement": "Expand $f(x) = x(1 - x^2)$ in terms of Legendre polynomials on $[-1, 1]$ and verify Parseval's identity.",
          "solution": "<b>Step 1: Algebraic decomposition</b><br>\n$f(x) = x - x^3$. We express $f(x)$ as a linear combination of Legendre polynomials:\n$$P_1(x) = x \\implies x = P_1(x)$$\n$$P_3(x) = \\frac{1}{2}(5x^3 - 3x) \\implies 5x^3 = 2P_3(x) + 3x = 2P_3(x) + 3P_1(x) \\implies x^3 = \\frac{2}{5}P_3(x) + \\frac{3}{5}P_1(x)$$\nSubstituting $x^3$:\n$$f(x) = P_1(x) - \\left( \\frac{2}{5}P_3(x) + \\frac{3}{5}P_1(x) \\right) = \\frac{2}{5}P_1(x) - \\frac{2}{5}P_3(x)$$\nAll other coefficients $c_n = 0$.<br><br>\n<b>Step 2: Parseval's Identity Verification</b><br>\nLHS: Directly compute $\\int_{-1}^1 [f(x)]^2\\,dx$:\n$$[f(x)]^2 = x^2(1 - x^2)^2 = x^2(1 - 2x^2 + x^4) = x^2 - 2x^4 + x^6$$\n$$\\int_{-1}^1 (x^2 - 2x^4 + x^6)\\,dx = 2 \\left[ \\frac{1}{3} - \\frac{2}{5} + \\frac{1}{7} \\right] = 2 \\left( \\frac{35 - 42 + 15}{105} \\right) = 2 \\left(\\frac{8}{105}\\right) = \\frac{16}{105}$$\nRHS: Compute $\\sum c_n^2 \\|P_n\\|^2$ where $\\|P_n\\|^2 = \\frac{2}{2n + 1}$:\n$$c_1^2 \\|P_1\\|^2 + c_3^2 \\|P_3\\|^2 = \\left(\\frac{2}{5}\\right)^2 \\left(\\frac{2}{3}\\right) + \\left(-\\frac{2}{5}\\right)^2 \\left(\\frac{2}{7}\\right)$$\n$$= \\frac{4}{25} \\left( \\frac{2}{3} + \\frac{2}{7} \\right) = \\frac{4}{25} \\left( \\frac{20}{21} \\right) = \\frac{80}{525} = \\frac{16}{105}$$\nLHS = RHS = $\\frac{16}{105}$. Parseval's identity holds with 100% precision!",
          "answer": "$f(x) = \\frac{2}{5}P_1(x) - \\frac{2}{5}P_3(x)$ and $\\|f\\|^2 = \\sum c_n^2 \\|P_n\\|^2 = \\frac{16}{105}$.",
          "difficulty": "Hard"
        }
      ]
    },
    {
      "number": 5,
      "title": "Regular Singular Points & The Method of Frobenius",
      "leadSummary": "Singularity classifications, the indicial polynomial F(r), and the three classical cases of the Frobenius method for regular singular points.",
      "simulations": [
        "ode2-frobenius-sim"
      ],
      "sections": [
        {
          "secNumber": "5.1",
          "title": "Classification of Singular Points (Ordinary, Regular Singular, Irregular Singular)",
          "content": "<h3>1. Rigorous Classification of Singular Points</h3>\n<p>Let $y'' + P(x) y' + Q(x) y = 0$. Suppose $x_0$ is a singular point (either $P(x)$ or $Q(x)$ blows up at $x_0$).</p>\n<div class=\"math-theorem\">\n<b>Definition 5.1:</b> The singular point $x_0$ is called a <b>regular singular point</b> if the singularities are at most a simple pole for $P(x)$ and a double pole for $Q(x)$; that is, both functions:\n$$p(x) = (x - x_0) P(x) \\quad \\text{and} \\quad q(x) = (x - x_0)^2 Q(x)$$\nare analytic at $x_0$. If either $p(x)$ or $q(x)$ is not analytic at $x_0$, the point is an <b>irregular singular point</b> (essential singularity).\n</div>"
        },
        {
          "secNumber": "5.2",
          "title": "The Method of Frobenius & The Indicial Equation",
          "content": "<h3>1. The Frobenius Series Ansatz</h3>\n<p>About a regular singular point (taken at $x_0 = 0$ without loss of generality), we seek solutions of the generalized power series form:</p>\n$$y(x) = x^r \\sum_{n=0}^\\infty a_n x^n = \\sum_{n=0}^\\infty a_n x^{n+r}, \\quad a_0 \\ne 0$$\n<p>where the index $r \\in \\mathbb{C}$ is a parameter to be determined. Expanding $p(x) = \\sum p_n x^n$ and $q(x) = \\sum q_n x^n$, the lowest-order term in $x$ is $x^r$, whose coefficient gives the <b>indicial equation</b>:</p>\n$$F(r) = r(r - 1) + p_0 r + q_0 = 0$$\n<p>The two roots $r_1, r_2$ (with $\\text{Re}(r_1) \\ge \\text{Re}(r_2)$) govern the algebraic nature of the solutions near $x = 0$.</p>"
        },
        {
          "secNumber": "5.3",
          "title": "Case 1: Roots Differing by Non-Integer; Case 2: Equal Roots & Logarithmic Solutions",
          "simulation": "ode2-frobenius-sim",
          "content": "<h3>Case 1: $r_1 - r_2 \\notin \\mathbb{Z}$ (Roots Not Differing by an Integer)</h3>\n<p>When the roots do not differ by an integer, two linearly independent Frobenius series solutions exist directly:</p>\n$$y_1(x) = x^{r_1} \\sum_{n=0}^\\infty a_n x^n, \\quad y_2(x) = x^{r_2} \\sum_{n=0}^\\infty b_n x^n \\quad (x > 0)$$\n\n<h3>Case 2: $r_1 = r_2 = r$ (Equal Indicial Roots)</h3>\n<p>When the indicial roots coincide, the first solution is $y_1(x) = x^r \\sum a_n x^n$. The second linearly independent solution strictly contains a logarithmic branch singularity:</p>\n$$y_2(x) = y_1(x) \\ln x + x^r \\sum_{n=1}^\\infty b_n x^n \\quad (x > 0)$$\n<p>This is derived rigorously by differentiating the parameterized series $y(x, r)$ with respect to the indicial parameter $r$:</p>\n$$y_2(x) = \\left. \\frac{\\partial y(x, r)}{\\partial r} \\right|_{r = r_1}$$"
        },
        {
          "secNumber": "5.4",
          "title": "Case 3: Roots Differing by a Positive Integer & The Logarithmic Factor Criterion",
          "content": "<h3>1. Case 3: $r_1 - r_2 = N \\in \\mathbb{Z}^+$</h3>\n<p>When the roots differ by a positive integer $N$, the recurrence relation for the smaller root $r_2$ encounters $F(r_2 + N) = F(r_1) = 0$ in the denominator of $a_N$, which may lead to division by zero.</p>\n<div class=\"math-theorem\">\n<b>Theorem 5.1 (Frobenius Case 3 Structure):</b> The second solution takes the general form:\n$$y_2(x) = C y_1(x) \\ln x + x^{r_2} \\sum_{n=0}^\\infty c_n x^n \\quad (c_0 \\ne 0)$$\nwhere the constant $C$ is given by:\n$$C = \\lim_{r \\to r_2} (r - r_2) a_N(r)$$\n<ul>\n<li>If $C = 0$, the logarithmic term vanishes, and $y_2(x)$ is a pure Frobenius series without logarithms.</li>\n<li>If $C \\ne 0$, the logarithmic term is mandatory.</li>\n</ul>\n</div>"
        }
      ],
      "problems": [
        {
          "id": "prob-05",
          "tier": 1,
          "difficultyLabel": "Tier 1 • Foundational",
          "title": "Frobenius Series Case 1: Roots Differing by Non-Integer",
          "statement": "Find the Frobenius series solutions about $x = 0$ for:<br>$$2x y'' + y' + y = 0$$",
          "solution": "<b>Step 1: Identify singularity and indicial equation</b><br>\nNormalized form: $y'' + \\frac{1}{2x} y' + \\frac{1}{2x} y = 0$.\n$p(x) = x P(x) = \\frac{1}{2} \\implies p_0 = \\frac{1}{2}$, and $q(x) = x^2 Q(x) = \\frac{x}{2} \\implies q_0 = 0$.\nThe point $x = 0$ is a regular singular point.\nIndicial equation:\n$$r(r - 1) + \\frac{1}{2} r + 0 = r\\left(r - \\frac{1}{2}\\right) = 0 \\implies r_1 = \\frac{1}{2}, \\quad r_2 = 0$$\nSince $r_1 - r_2 = \\frac{1}{2} \\notin \\mathbb{Z}$, this is <b>Case 1</b> (two distinct Frobenius series).<br><br>\n<b>Step 2: Recurrence relation for general $r$</b><br>\nSubstitute $y = \\sum_{n=0}^\\infty a_n x^{n+r}$:\n$$2 \\sum (n+r)(n+r-1) a_n x^{n+r-1} + \\sum (n+r) a_n x^{n+r-1} + \\sum a_n x^{n+r} = 0$$\nFor $n \\ge 1$:\n$$[(n+r)(2n + 2r - 1)] a_n = -a_{n-1} \\implies a_n = -\\frac{a_{n-1}}{(n+r)(2n + 2r - 1)}$$\n<br><b>Step 3: Solution for $r_1 = 1/2$</b><br>\nDenominator factor: $(n + 1/2)(2n) = n(2n + 1)$.\n$$a_n = -\\frac{a_{n-1}}{n(2n + 1)} \\implies y_1(x) = x^{1/2} \\left( 1 - \\frac{x}{3} + \\frac{x^2}{30} - \\frac{x^3}{630} + \\dots \\right)$$\n<br><b>Step 4: Solution for $r_2 = 0$</b><br>\nDenominator factor: $n(2n - 1)$.\n$$a_n = -\\frac{a_{n-1}}{n(2n - 1)} \\implies y_2(x) = 1 - x + \\frac{x^2}{6} - \\frac{x^3}{90} + \\dots$$",
          "answer": "$y(x) = c_1 x^{1/2}\\left(1 - \\frac{x}{3} + \\frac{x^2}{30} - \\dots\\right) + c_2 \\left(1 - x + \\frac{x^2}{6} - \\dots\\right)$",
          "difficulty": "Easy"
        },
        {
          "id": "prob-11",
          "tier": 2,
          "difficultyLabel": "Tier 2 • Intermediate Exam",
          "title": "Frobenius Method Case 2: Equal Indicial Roots & Logarithmic Branch",
          "statement": "Find two linearly independent solutions about $x = 0$ for:<br>$$x y'' + y' - y = 0$$",
          "solution": "<b>Step 1: Indicial equation</b><br>\nMultiply by $x$: $x^2 y'' + x y' - x y = 0$.\n$p(x) = 1 \\implies p_0 = 1$, $q(x) = -x \\implies q_0 = 0$.\nIndicial equation: $F(r) = r(r - 1) + r = r^2 = 0 \\implies r_1 = r_2 = 0$.\nEqual roots $\\implies$ <b>Case 2</b> (logarithmic second solution).<br><br>\n<b>Step 2: Recurrence relation for $y(x, r)$</b><br>\nSubstitute $y(x, r) = \\sum_{n=0}^\\infty a_n(r) x^{n+r}$:\n$$F(n + r) a_n = a_{n-1} \\implies (n + r)^2 a_n(r) = a_{n-1}(r) \\implies a_n(r) = \\frac{a_0}{[(1+r)(2+r)\\dots(n+r)]^2}$$\nFor $r = 0$ and $a_0 = 1$:\n$$a_n(0) = \\frac{1}{(n!)^2} \\implies y_1(x) = \\sum_{n=0}^\\infty \\frac{x^n}{(n!)^2} = 1 + x + \\frac{x^2}{4} + \\frac{x^3}{36} + \\dots$$\n<br><b>Step 3: Differentiate with respect to $r$ to obtain $y_2(x)$</b><br>\n$$y_2(x) = \\left. \\frac{\\partial y(x, r)}{\\partial r} \\right|_{r=0} = y_1(x) \\ln x + \\sum_{n=1}^\\infty a_n'(0) x^n$$\nUsing logarithmic differentiation on $a_n(r)$:\n$$\\ln a_n(r) = -2 \\sum_{k=1}^n \\ln(k + r) \\implies \\frac{a_n'(r)}{a_n(r)} = -2 \\sum_{k=1}^n \\frac{1}{k + r}$$\nAt $r = 0$: $a_n'(0) = -2 H_n a_n(0) = -2 \\frac{H_n}{(n!)^2}$, where $H_n = \\sum_{k=1}^n \\frac{1}{k}$ is the $n$-th harmonic number.<br><br>\n$$y_2(x) = y_1(x) \\ln x - 2 \\sum_{n=1}^\\infty \\frac{H_n}{(n!)^2} x^n = y_1(x) \\ln x - 2\\left( x + \\frac{3}{8}x^2 + \\frac{11}{216}x^3 + \\dots \\right)$$",
          "answer": "$y_1(x) = \\sum_{n=0}^\\infty \\frac{x^n}{(n!)^2}, \\quad y_2(x) = y_1(x)\\ln x - 2\\sum_{n=1}^\\infty \\frac{H_n}{(n!)^2} x^n$",
          "difficulty": "Medium"
        },
        {
          "id": "prob-14",
          "tier": 2,
          "difficultyLabel": "Tier 2 • Intermediate Exam",
          "title": "Hermite Polynomials Generating Function & Orthogonality",
          "statement": "Using the generating function $\\Phi(x, t) = e^{2xt - t^2} = \\sum_{n=0}^\\infty \\frac{H_n(x)}{n!} t^n$, prove the orthogonality relation:<br>$$\\int_{-\\infty}^\\infty e^{-x^2} H_n(x) H_m(x)\\,dx = 2^n n! \\sqrt{\\pi}\\, \\delta_{nm}$$",
          "solution": "<b>Step 1: Product of generating functions</b><br>\nConsider two generating functions with parameters $t$ and $s$:\n$$\\sum_{n=0}^\\infty \\sum_{m=0}^\\infty \\frac{t^n s^m}{n!\\, m!} \\int_{-\\infty}^\\infty e^{-x^2} H_n(x) H_m(x)\\,dx = \\int_{-\\infty}^\\infty e^{-x^2} \\Phi(x, t) \\Phi(x, s)\\,dx$$\n<br><b>Step 2: Combine exponents</b><br>\n$$\\Phi(x, t) \\Phi(x, s) = e^{2xt - t^2} e^{2xs - s^2} = e^{2x(t + s) - (t^2 + s^2)}$$\nThe integrand exponent is:\n$$-x^2 + 2x(t + s) - (t^2 + s^2) = -[x - (t + s)]^2 + (t + s)^2 - (t^2 + s^2) = -[x - (t + s)]^2 + 2ts$$\n<br><b>Step 3: Evaluate Gaussian integral</b><br>\n$$\\int_{-\\infty}^\\infty e^{-[x - (t + s)]^2 + 2ts}\\,dx = e^{2ts} \\int_{-\\infty}^\\infty e^{-u^2}\\,du = \\sqrt{\\pi} e^{2ts}$$\n<br><b>Step 4: Taylor series expansion of $e^{2ts}$</b><br>\n$$\\sqrt{\\pi} e^{2ts} = \\sqrt{\\pi} \\sum_{n=0}^\\infty \\frac{(2ts)^n}{n!} = \\sqrt{\\pi} \\sum_{n=0}^\\infty \\frac{2^n}{n!} t^n s^n$$\nNotice that there are NO terms with unequal powers $t^n s^m$ ($n \\ne m$). Hence:\n$$\\int_{-\\infty}^\\infty e^{-x^2} H_n(x) H_m(x)\\,dx = 0 \\quad \\text{for } n \\ne m$$\nFor $n = m$, equating coefficients of $\\frac{t^n s^n}{(n!)^2}$:\n$$\\frac{1}{(n!)^2} \\int_{-\\infty}^\\infty e^{-x^2} [H_n(x)]^2\\,dx = \\sqrt{\\pi} \\frac{2^n}{n!} \\implies \\int_{-\\infty}^\\infty e^{-x^2} [H_n(x)]^2\\,dx = 2^n n! \\sqrt{\\pi}$$",
          "answer": "$\\int_{-\\infty}^\\infty e^{-x^2} H_n(x) H_m(x)\\,dx = 2^n n! \\sqrt{\\pi}\\, \\delta_{nm}$",
          "difficulty": "Medium"
        }
      ]
    },
    {
      "number": 6,
      "title": "Bessel Functions & Classical Orthogonal Systems (Laguerre & Hermite)",
      "leadSummary": "Cylindrical Bessel functions of the first and second kinds, circular drum vibrations, Laguerre polynomials in quantum mechanics, and Hermite polynomials of the quantum oscillator.",
      "simulations": [
        "ode2-bessel-harmonics-sim"
      ],
      "sections": [
        {
          "secNumber": "6.1",
          "title": "Bessel's Differential Equation & Cylindrical Functions of the First Kind J_ν(x)",
          "content": "<h3>1. Bessel's Differential Equation</h3>\n<p>Bessel's equation of order $\\nu \\ge 0$ appears in physical problems possessing cylindrical symmetry (wave propagation in waveguides, heat conduction in cylinders, vibrations of circular membranes):</p>\n$$x^2 y'' + x y' + (x^2 - \\nu^2) y = 0$$\n<p>Here $x = 0$ is a regular singular point with indicial equation $r^2 - \\nu^2 = 0 \\implies r = \\pm \\nu$. Applying the method of Frobenius yields the <b>Bessel functions of the first kind</b> $J_\\nu(x)$:</p>\n$$J_\\nu(x) = \\sum_{m=0}^\\infty \\frac{(-1)^m}{m!\\, \\Gamma(m + \\nu + 1)} \\left( \\frac{x}{2} \\right)^{2m + \\nu}$$\n<p>For non-integer $\\nu$, $J_\\nu(x)$ and $J_{-\\nu}(x)$ are linearly independent.</p>"
        },
        {
          "secNumber": "6.2",
          "title": "Bessel Functions of the Second Kind Y_ν(x), Generating Function & Recurrence Formulas",
          "simulation": "ode2-bessel-harmonics-sim",
          "content": "<h3>1. Bessel Functions of the Second Kind (Neumann Functions)</h3>\n<p>When $\\nu = n$ is an integer, $J_{-n}(x) = (-1)^n J_n(x)$, so they are linearly dependent! The second independent solution is the <b>Weber-Neumann function</b> $Y_\\nu(x)$:</p>\n$$Y_\\nu(x) = \\frac{J_\\nu(x) \\cos(\\nu\\pi) - J_{-\\nu}(x)}{\\sin(\\nu\\pi)}, \\quad Y_n(x) = \\lim_{\\nu \\to n} Y_\\nu(x)$$\n<p>$Y_n(x)$ diverges logarithmically as $x \\to 0^+$. The general solution for any order $\\nu$ is $y(x) = c_1 J_\\nu(x) + c_2 Y_\\nu(x)$.</p>\n\n<h3>2. Master Differential Recurrence Relations</h3>\n<div class=\"math-theorem\">\n<b>Bessel Recurrence Identities:</b>\n$$\\begin{aligned}\n\\frac{d}{dx} \\left[ x^\\nu J_\\nu(x) \\right] &= x^\\nu J_{\\nu-1}(x) \\\\\n\\frac{d}{dx} \\left[ x^{-\\nu} J_\\nu(x) \\right] &= -x^{-\\nu} J_{\\nu+1}(x) \\\\\nJ_{\\nu-1}(x) + J_{\\nu+1}(x) &= \\frac{2\\nu}{x} J_\\nu(x) \\\\\nJ_{\\nu-1}(x) - J_{\\nu+1}(x) &= 2 J_\\nu'(x)\n\\end{aligned}$$\n</div>"
        },
        {
          "secNumber": "6.3",
          "title": "Laguerre's Differential Equation, Associated Laguerre Polynomials & Quantum Radial Eigenstates",
          "content": "<h3>1. Laguerre's Differential Equation</h3>\n<p>Laguerre's equation arises in the quantum mechanical description of the hydrogen atom:</p>\n$$x y'' + (1 - x) y' + n y = 0$$\n<p>For non-negative integers $n$, polynomial solutions are the <b>Laguerre Polynomials</b> $L_n(x)$:</p>\n$$L_n(x) = \\frac{e^x}{n!} \\frac{d^n}{dx^n} (x^n e^{-x}) = \\sum_{k=0}^n \\frac{(-1)^k}{k!} \\binom{n}{k} x^k$$\n<p>They satisfy the orthogonality relation with weight $e^{-x}$ on $[0, \\infty)$:</p>\n$$\\int_0^\\infty e^{-x} L_n(x) L_m(x)\\,dx = \\delta_{nm}$$"
        },
        {
          "secNumber": "6.4",
          "title": "Hermite's Differential Equation, Hermite Polynomials H_n(x) & Harmonic Oscillator Orthogonality",
          "content": "<h3>1. Hermite's Differential Equation</h3>\n<p>Hermite's equation governs the stationary wavefunctions of the quantum harmonic oscillator:</p>\n$$y'' - 2x y' + 2n y = 0$$\n<p>For integer $n \\ge 0$, the solutions are the <b>Hermite Polynomials</b> $H_n(x)$:</p>\n$$H_n(x) = (-1)^n e^{x^2} \\frac{d^n}{dx^n} (e^{-x^2})$$\n<p>First few polynomials: $H_0(x) = 1$, $H_1(x) = 2x$, $H_2(x) = 4x^2 - 2$, $H_3(x) = 8x^3 - 12x$.</p>\n<div class=\"math-theorem\">\n<b>Orthogonality of Hermite Polynomials:</b>\n$$\\int_{-\\infty}^\\infty e^{-x^2} H_n(x) H_m(x)\\,dx = 2^n n! \\sqrt{\\pi}\\, \\delta_{nm}$$\n</div>"
        }
      ],
      "problems": [
        {
          "id": "prob-12",
          "tier": 2,
          "difficultyLabel": "Tier 2 • Intermediate Exam",
          "title": "Bessel Differential Equation of Order Zero: J_0(x) and Y_0(x)",
          "statement": "Obtain the series solution for Bessel's equation of order zero:<br>$$x y'' + y' + x y = 0$$",
          "solution": "<b>Step 1: Indicial equation</b><br>\nMultiply by $x$: $x^2 y'' + x y' + x^2 y = 0$.\n$p_0 = 1, q_0 = 0 \\implies r^2 = 0 \\implies r_1 = r_2 = 0$.<br><br>\n<b>Step 2: Recurrence relation</b><br>\nSubstitute $y = \\sum a_n x^{n+r}$:\n$$(n + r)^2 a_n = -a_{n-2} \\quad (a_1 = 0)$$\nOdd coefficients vanish: $a_{2m+1} = 0$.\nFor even coefficients $n = 2m$:\n$$a_{2m}(r) = \\frac{(-1)^m a_0}{2^{2m} [(1 + r/2)(2 + r/2)\\dots(m + r/2)]^2}$$\nFor $r = 0, a_0 = 1$:\n$$a_{2m}(0) = \\frac{(-1)^m}{2^{2m} (m!)^2} \\implies J_0(x) = \\sum_{m=0}^\\infty \\frac{(-1)^m}{(m!)^2} \\left(\\frac{x}{2}\\right)^{2m}$$\n<br><b>Step 3: Second solution $Y_0(x)$</b><br>\nDifferentiating with respect to $r$:\n$$\\left. \\frac{\\partial a_{2m}}{\\partial r} \\right|_{r=0} = -H_m a_{2m}(0)$$\n$$y_2(x) = J_0(x) \\ln x - \\sum_{m=1}^\\infty \\frac{(-1)^m H_m}{(m!)^2} \\left(\\frac{x}{2}\\right)^{2m}$$\nThe standard Neumann function is normalized as $Y_0(x) = \\frac{2}{\\pi}\\left[ y_2(x) + (\\gamma - \\ln 2) J_0(x) \\right]$.",
          "answer": "$J_0(x) = \\sum_{m=0}^\\infty \\frac{(-1)^m}{(m!)^2} \\left(\\frac{x}{2}\\right)^{2m}$ and $Y_0(x)$ contains logarithmic singularity $\\frac{2}{\\pi} J_0(x)\\ln x$.",
          "difficulty": "Medium"
        },
        {
          "id": "prob-20",
          "tier": 3,
          "difficultyLabel": "Tier 3 • Honors Challenge",
          "title": "Inhomogeneous Bessel Equation via Lommel's Integrals",
          "statement": "Solve the inhomogeneous Bessel equation of order zero:<br>$$x^2 y'' + x y' + x^2 y = x$$<br>using Variation of Parameters.",
          "solution": "<b>Step 1: Normalized standard form</b><br>\nDivide by $x^2$:\n$$y'' + \\frac{1}{x} y' + y = \\frac{1}{x}$$\nThe homogeneous solutions are $y_1(x) = J_0(x)$ and $y_2(x) = Y_0(x)$.<br><br>\n<b>Step 2: Wronskian of Bessel functions</b><br>\nAbel's identity gives:\n$$W(J_0, Y_0)(x) = \\frac{2}{\\pi x}$$\n<br><b>Step 3: Variation of Parameters formulas</b><br>\n$$u_1'(x) = -\\frac{y_2(x) g(x)}{W(x)} = -\\frac{Y_0(x) (1/x)}{2/(\\pi x)} = -\\frac{\\pi}{2} Y_0(x)$$\n$$u_2'(x) = \\frac{y_1(x) g(x)}{W(x)} = \\frac{J_0(x) (1/x)}{2/(\\pi x)} = \\frac{\\pi}{2} J_0(x)$$\n<br><b>Step 4: Particular solution</b><br>\n$$y_p(x) = -\\frac{\\pi}{2} J_0(x) \\int_0^x Y_0(s)\\,ds + \\frac{\\pi}{2} Y_0(x) \\int_0^x J_0(s)\\,ds$$\nThis is the celebrated Struve function relation: $y_p(x) = \\frac{\\pi}{2} \\mathbf{H}_0(x)$.",
          "answer": "$y(x) = c_1 J_0(x) + c_2 Y_0(x) + \\frac{\\pi}{2}\\left[ Y_0(x)\\int_0^x J_0(s)ds - J_0(x)\\int_0^x Y_0(s)ds \\right]$",
          "difficulty": "Hard"
        },
        {
          "id": "prob-15",
          "tier": 2,
          "difficultyLabel": "Tier 2 • Intermediate Exam",
          "title": "Sturm Comparison Theorem & Interlacing Zeros of Bessel Functions",
          "statement": "Prove using Sturm's Separation/Comparison Theorem that between any two consecutive positive zeros of $J_0(x)$, there is exactly one zero of $J_1(x)$.",
          "solution": "<b>Step 1: Recurrence relation between $J_0$ and $J_1$</b><br>\nRecall from Bessel recurrence relations:\n$$\\frac{d}{dx} J_0(x) = -J_1(x)$$\n<br><b>Step 2: Apply Rolle's Theorem</b><br>\nLet $0 < x_1 < x_2$ be two consecutive positive zeros of $J_0(x)$, so $J_0(x_1) = 0$ and $J_0(x_2) = 0$, and $J_0(x) \\ne 0$ for all $x \\in (x_1, x_2)$.<br>\nSince $J_0(x)$ is continuously differentiable on $[x_1, x_2]$, Rolle's theorem guarantees that there exists at least one point $\\xi \\in (x_1, x_2)$ such that $J_0'(\\xi) = 0$.<br>\nSince $J_0'(x) = -J_1(x)$, this means $J_1(\\xi) = 0$. Thus $J_1$ has <i>at least one</i> zero in $(x_1, x_2)$.<br><br>\n<b>Step 3: Uniqueness via Sturm Separation</b><br>\nNow consider the identity:\n$$\\frac{d}{dx}[x J_1(x)] = x J_0(x)$$\nSuppose $J_1(x)$ had two zeros $\\xi_1 < \\xi_2$ in $(x_1, x_2)$. Then applying Rolle's theorem to $g(x) = x J_1(x)$ on $[\\xi_1, \\xi_2]$ would imply $g'(\\eta) = \\eta J_0(\\eta) = 0$ for some $\\eta \\in (\\xi_1, \\xi_2) \\subset (x_1, x_2)$.<br>\nSince $\\eta > 0$, this would force $J_0(\\eta) = 0$, directly contradicting that $x_1$ and $x_2$ are <i>consecutive</i> zeros of $J_0(x)$!<br><br>\n<b>Conclusion:</b> There is <b>strictly one</b> zero of $J_1(x)$ between any two consecutive zeros of $J_0(x)$. The zeros strictly interlace: $0 < j_{0, 1} < j_{1, 1} < j_{0, 2} < j_{1, 2} < \\dots$.",
          "answer": "Proved: zeros of $J_0(x)$ and $J_1(x)$ strictly interlace.",
          "difficulty": "Medium"
        }
      ]
    },
    {
      "number": 7,
      "title": "Sturm-Liouville Theory, Self-Adjoint Operators & Oscillation Theorems",
      "leadSummary": "Formal self-adjoint differential operators, Lagrange's identity, regular Sturm-Liouville boundary value problems, reality of eigenvalues, eigenfunction orthogonality, and Sturm oscillation theorems.",
      "simulations": [
        "ode2-sturm-liouville-sim"
      ],
      "sections": [
        {
          "secNumber": "7.1",
          "title": "Formal Self-Adjoint Differential Operators & Lagrange's Identity",
          "content": "<h3>1. The Sturm-Liouville Differential Operator</h3>\n<p>Consider the second-order linear differential operator acting on $C^2[a, b]$:</p>\n$$L[y] = -\\frac{d}{dx}\\left[ p(x) \\frac{dy}{dx} \\right] + q(x) y$$\n<p>where $p(x) > 0$, $p'(x)$, $q(x)$, and weight $w(x) > 0$ are continuous on $[a, b]$. Any linear equation $a_2(x)y'' + a_1(x)y' + a_0(x)y = 0$ with $a_2(x) > 0$ can be transformed into Sturm-Liouville form by multiplying by the integrating factor:</p>\n$$\\mu(x) = \\frac{1}{a_2(x)} \\exp\\left( \\int \\frac{a_1(x)}{a_2(x)}\\,dx \\right)$$\n\n<h3>2. Lagrange's Identity & Green's Formula</h3>\n<div class=\"math-theorem\">\n<b>Theorem 7.1 (Lagrange's Identity):</b> For any twice-differentiable functions $u, v$:\n$$u L[v] - v L[u] = -\\frac{d}{dx} \\left[ p(x) (u v' - v u') \\right] = -\\frac{d}{dx} [p(x) W(u, v)]$$\nIntegrating over $[a, b]$ yields <b>Green's Formula</b>:\n$$\\int_a^b (u L[v] - v L[u])\\,dx = \\left[ -p(x)(u v' - v u') \\right]_a^b$$\n</div>"
        },
        {
          "secNumber": "7.2",
          "title": "Regular Sturm-Liouville Problems: Reality of Eigenvalues & Orthogonality",
          "content": "<h3>1. The Regular Sturm-Liouville Problem</h3>\n<p>The eigenvalue problem consists of $L[y] = \\lambda w(x) y$ subject to separated boundary conditions:</p>\n$$\\begin{aligned}\n\\alpha_1 y(a) + \\alpha_2 y'(a) &= 0 \\quad (|\\alpha_1| + |\\alpha_2| > 0) \\\\\n\\beta_1 y(b) + \\beta_2 y'(b) &= 0 \\quad (|\\beta_1| + |\\beta_2| > 0)\n\\end{aligned}$$\n<p>Under these boundary conditions, the boundary term in Green's formula vanishes: $[-p(x)(u v' - v u')]_a^b = 0$. Hence $L$ is <b>self-adjoint</b> (Hermitian) on the domain of admissible boundary functions.</p>\n\n<div class=\"math-theorem\">\n<b>Theorem 7.2 (Fundamental Sturm-Liouville Theorem):</b>\n<ol>\n<li>All eigenvalues $\\lambda_n$ are strictly <b>real</b>.</li>\n<li>The eigenvalues are countably infinite, discrete, bounded below, and can be ordered:\n$$\\lambda_1 < \\lambda_2 < \\lambda_3 < \\dots < \\lambda_n \\to \\infty$$</li>\n<li>To each eigenvalue $\\lambda_n$, there corresponds a unique eigenfunction $y_n(x)$ (up to a scalar multiple). There is no degeneracy: all eigenspaces are one-dimensional.</li>\n<li>Eigenfunctions corresponding to distinct eigenvalues are <b>orthogonal</b> with respect to $w(x)$:\n$$\\int_a^b y_n(x) y_m(x) w(x)\\,dx = 0 \\quad (n \\ne m)$$</li>\n</ol>\n</div>"
        },
        {
          "secNumber": "7.3",
          "title": "Sturm Oscillation Theorem & Sturm Comparison/Separation Theorems",
          "simulation": "ode2-sturm-liouville-sim",
          "content": "<h3>1. The Sturm Oscillation Theorem</h3>\n<div class=\"math-theorem\">\n<b>Theorem 7.3 (Sturm Oscillation Theorem):</b> The eigenfunction $y_n(x)$ corresponding to the $n$-th eigenvalue $\\lambda_n$ has exactly $n - 1$ simple zeros in the open interval $(a, b)$.\n</div>\n<p>For example, the fundamental mode $y_1(x)$ has 0 interior zeros (does not change sign), $y_2(x)$ has 1 zero, $y_3(x)$ has 2 zeros, etc.</p>\n\n<h3>2. Sturm Separation and Comparison Theorems</h3>\n<div class=\"math-theorem\">\n<b>Sturm's Separation Theorem:</b> Let $y_1(x)$ and $y_2(x)$ be two linearly independent solutions of $y'' + q(x)y = 0$ on $(a, b)$. Then between any two consecutive zeros of $y_1(x)$, there is exactly one zero of $y_2(x)$ (their zeros strictly interlace).<br><br>\n<b>Sturm's Comparison Theorem:</b> Let $u'' + q_1(x)u = 0$ and $v'' + q_2(x)v = 0$ where $q_2(x) \\ge q_1(x)$. If $x_1, x_2$ are consecutive zeros of $u(x)$, then $v(x)$ must have at least one zero in $[x_1, x_2]$.\n</div>"
        },
        {
          "secNumber": "7.4",
          "title": "Generalized Fourier Series & Eigenfunction Completeness in L^2_w[a, b]",
          "content": "<h3>1. Generalized Fourier Series Expansions</h3>\n<p>The normalized eigenfunctions $\\phi_n(x) = \\frac{y_n(x)}{\\sqrt{\\int_a^b y_n^2 w\\,dx}}$ form an orthonormal basis for the Hilbert space $L^2_w[a, b]$. Any piecewise smooth function $f(x)$ on $[a, b]$ can be expanded in a generalized Fourier series:</p>\n$$f(x) \\sim \\sum_{n=1}^\\infty c_n \\phi_n(x), \\quad c_n = \\langle f, \\phi_n \\rangle_w = \\int_a^b f(x) \\phi_n(x) w(x)\\,dx$$\n<p>The series converges pointwise to $\\frac{f(x^+) + f(x^-)}{2}$ at all interior points $x \\in (a, b)$, and satisfies Parseval's identity:</p>\n$$\\|f\\|_w^2 = \\int_a^b [f(x)]^2 w(x)\\,dx = \\sum_{n=1}^\\infty c_n^2$$"
        }
      ],
      "problems": [
        {
          "id": "prob-07",
          "tier": 1,
          "difficultyLabel": "Tier 1 • Foundational",
          "title": "Regular Sturm-Liouville Eigenvalues & Mixed Boundary Conditions",
          "statement": "Find all eigenvalues and eigenfunctions of the regular Sturm-Liouville problem:<br>$$y'' + \\lambda y = 0, \\quad y(0) = 0, \\quad y'(\\pi) = 0$$",
          "solution": "<b>Case 1: $\\lambda < 0$ ($\\lambda = -\\mu^2, \\mu > 0$)</b><br>\n$y(x) = c_1 \\cosh(\\mu x) + c_2 \\sinh(\\mu x)$.<br>\n$y(0) = c_1 = 0 \\implies y(x) = c_2 \\sinh(\\mu x)$.<br>\n$y'(\\pi) = c_2 \\mu \\cosh(\\mu \\pi) = 0$. Since $\\mu \\ne 0$ and $\\cosh(\\mu \\pi) \\ge 1$, $c_2 = 0$. No non-trivial solutions.<br><br>\n<b>Case 2: $\\lambda = 0$</b><br>\n$y(x) = c_1 x + c_2$. $y(0) = c_2 = 0$. $y'(x) = c_1 \\implies y'(\\pi) = c_1 = 0$. Only trivial solution.<br><br>\n<b>Case 3: $\\lambda > 0$ ($\\lambda = k^2, k > 0$)</b><br>\n$y(x) = c_1 \\cos(kx) + c_2 \\sin(kx)$.<br>\n$y(0) = c_1 = 0 \\implies y(x) = c_2 \\sin(kx)$.<br>\n$y'(x) = c_2 k \\cos(kx) \\implies y'(\\pi) = c_2 k \\cos(k\\pi) = 0$.<br>\nFor non-trivial solutions ($c_2 \\ne 0$), we require:\n$$\\cos(k\\pi) = 0 \\implies k\\pi = \\left(n - \\frac{1}{2}\\right)\\pi \\implies k_n = n - \\frac{1}{2} = \\frac{2n - 1}{2}, \\quad n = 1, 2, 3, \\dots$$\n<br><b>Step 4: Eigenvalues & Orthonormal Eigenfunctions</b><br>\n$$\\lambda_n = k_n^2 = \\frac{(2n - 1)^2}{4}, \\quad y_n(x) = \\sin\\left(\\frac{2n - 1}{2} x\\right)$$\nNorm: $\\int_0^\\pi \\sin^2\\left(\\frac{2n - 1}{2} x\\right) dx = \\frac{\\pi}{2}$.\nOrthonormal set: $\\phi_n(x) = \\sqrt{\\frac{2}{\\pi}} \\sin\\left(\\frac{2n - 1}{2} x\\right)$.",
          "answer": "$\\lambda_n = \\frac{(2n - 1)^2}{4}, \\quad y_n(x) = \\sin\\left(\\frac{2n - 1}{2} x\\right), \\quad n = 1, 2, 3, \\dots$",
          "difficulty": "Easy"
        },
        {
          "id": "prob-15",
          "tier": 2,
          "difficultyLabel": "Tier 2 • Intermediate Exam",
          "title": "Sturm Comparison Theorem & Interlacing Zeros of Bessel Functions",
          "statement": "Prove using Sturm's Separation/Comparison Theorem that between any two consecutive positive zeros of $J_0(x)$, there is exactly one zero of $J_1(x)$.",
          "solution": "<b>Step 1: Recurrence relation between $J_0$ and $J_1$</b><br>\nRecall from Bessel recurrence relations:\n$$\\frac{d}{dx} J_0(x) = -J_1(x)$$\n<br><b>Step 2: Apply Rolle's Theorem</b><br>\nLet $0 < x_1 < x_2$ be two consecutive positive zeros of $J_0(x)$, so $J_0(x_1) = 0$ and $J_0(x_2) = 0$, and $J_0(x) \\ne 0$ for all $x \\in (x_1, x_2)$.<br>\nSince $J_0(x)$ is continuously differentiable on $[x_1, x_2]$, Rolle's theorem guarantees that there exists at least one point $\\xi \\in (x_1, x_2)$ such that $J_0'(\\xi) = 0$.<br>\nSince $J_0'(x) = -J_1(x)$, this means $J_1(\\xi) = 0$. Thus $J_1$ has <i>at least one</i> zero in $(x_1, x_2)$.<br><br>\n<b>Step 3: Uniqueness via Sturm Separation</b><br>\nNow consider the identity:\n$$\\frac{d}{dx}[x J_1(x)] = x J_0(x)$$\nSuppose $J_1(x)$ had two zeros $\\xi_1 < \\xi_2$ in $(x_1, x_2)$. Then applying Rolle's theorem to $g(x) = x J_1(x)$ on $[\\xi_1, \\xi_2]$ would imply $g'(\\eta) = \\eta J_0(\\eta) = 0$ for some $\\eta \\in (\\xi_1, \\xi_2) \\subset (x_1, x_2)$.<br>\nSince $\\eta > 0$, this would force $J_0(\\eta) = 0$, directly contradicting that $x_1$ and $x_2$ are <i>consecutive</i> zeros of $J_0(x)$!<br><br>\n<b>Conclusion:</b> There is <b>strictly one</b> zero of $J_1(x)$ between any two consecutive zeros of $J_0(x)$. The zeros strictly interlace: $0 < j_{0, 1} < j_{1, 1} < j_{0, 2} < j_{1, 2} < \\dots$.",
          "answer": "Proved: zeros of $J_0(x)$ and $J_1(x)$ strictly interlace.",
          "difficulty": "Medium"
        },
        {
          "id": "prob-22",
          "tier": 3,
          "difficultyLabel": "Tier 3 • Honors Challenge",
          "title": "Periodic Sturm-Liouville Problem & Double Spectral Degeneracy",
          "statement": "Establish the self-adjointness, non-negative spectrum, and double degeneracy for the periodic Sturm-Liouville problem:<br>$$y'' + \\lambda y = 0, \\quad y(-\\pi) = y(\\pi), \\quad y'(-\\pi) = y'(\\pi)$$",
          "solution": "<b>Step 1: Self-Adjointness via Green's Formula</b><br>\nFor $L[y] = -y''$:\n$$\\int_{-\\pi}^\\pi (u L[v] - v L[u])\\,dx = \\left[ -u v' + v u' \\right]_{-\\pi}^\\pi = [-u(\\pi)v'(\\pi) + v(\\pi)u'(\\pi)] - [-u(-\\pi)v'(-\\pi) + v(-\\pi)u'(-\\pi)]$$\nUsing periodic conditions $u(-\\pi) = u(\\pi)$ and $u'(-\\pi) = u'(\\pi)$:\n$$= [-u(\\pi)v'(\\pi) + v(\\pi)u'(\\pi)] - [-u(\\pi)v'(\\pi) + v(\\pi)u'(\\pi)] = 0$$\nThe periodic boundary conditions make the boundary term vanish. Hence $L$ is <b>self-adjoint</b>.<br><br>\n<b>Step 2: Non-negative eigenvalues ($\\lambda \\ge 0$)</b><br>\nMultiply by $y$ and integrate by parts:\n$$\\lambda \\int_{-\\pi}^\\pi y^2\\,dx = \\int_{-\\pi}^\\pi (y')^2\\,dx - [y y']_{-\\pi}^\\pi = \\int_{-\\pi}^\\pi (y')^2\\,dx \\ge 0$$\nHence $\\lambda \\ge 0$.<br><br>\n<b>Step 3: Eigenvalues & Degeneracy</b><br>\nFor $\\lambda_0 = 0$: $y_0(x) = 1$ (non-degenerate, dimension 1).<br>\nFor $\\lambda_n = n^2 > 0$ ($n = 1, 2, 3, \\dots$):\nBoth $y_{n, 1}(x) = \\cos(nx)$ and $y_{n, 2}(x) = \\sin(nx)$ satisfy the periodic boundary conditions!\nThus every eigenvalue $\\lambda_n = n^2$ has <b>multiplicity 2</b> (doubly degenerate eigenspace spanned by $\\{\\cos nx, \\sin nx\\}$), generating the classical full Fourier series!",
          "answer": "$\\lambda_0 = 0$ (simple), $\\lambda_n = n^2$ ($n \\ge 1$, doubly degenerate with basis $\\{\\cos nx, \\sin nx\\}$).",
          "difficulty": "Hard"
        }
      ]
    },
    {
      "number": 8,
      "title": "Nonhomogeneous Boundary Value Problems, The Fredholm Alternative & Green's Functions",
      "leadSummary": "Solvability criteria via the Fredholm Alternative, the Dirac delta distribution, jump conditions, and explicit closed-form construction of Green's functions.",
      "simulations": [
        "ode2-greens-function-sim"
      ],
      "sections": [
        {
          "secNumber": "8.1",
          "title": "Nonhomogeneous Boundary Value Problems & Solvability via The Fredholm Alternative",
          "content": "<h3>1. Inhomogeneous Boundary Value Problems</h3>\n<p>Consider the nonhomogeneous boundary value problem:</p>\n$$L[y] = f(x), \\quad x \\in [a, b], \\quad B_1[y] = 0, \\quad B_2[y] = 0$$\n<p>where $L$ is a self-adjoint differential operator with homogeneous boundary operators $B_1, B_2$.</p>\n<div class=\"math-theorem\">\n<b>Theorem 8.1 (The Fredholm Alternative for Differential Operators):</b>\n<ol>\n<li><b>Case I:</b> If the homogeneous problem $L[y] = 0, B_1[y] = 0, B_2[y] = 0$ has only the trivial solution $y \\equiv 0$, then for <i>any</i> continuous function $f(x)$, the nonhomogeneous problem has a <b>unique</b> solution $y(x)$.</li>\n<li><b>Case II:</b> If the homogeneous problem has non-trivial solutions $\\phi_1(x), \\dots, \\phi_k(x)$, then the nonhomogeneous problem has solutions if and only if $f(x)$ is orthogonal to every homogeneous solution:\n$$\\int_a^b f(x) \\phi_j(x)\\,dx = 0 \\quad \\text{for all } j = 1, \\dots, k$$\nIf this orthogonality condition holds, there exists an infinite family of solutions.\n</li>\n</ol>\n</div>"
        },
        {
          "secNumber": "8.2",
          "title": "Green's Functions: Definition, Dirac Delta Distribution & Jump Discontinuity Conditions",
          "simulation": "ode2-greens-function-sim",
          "content": "<h3>1. The Green's Function as Impulse Response</h3>\n<p>The Green's function $G(x, \\xi)$ is the kernel representing the physical response at point $x$ produced by an idealized unit point-source impulse $\\delta(x - \\xi)$ applied at $\\xi \\in (a, b)$:</p>\n$$L[G(x, \\xi)] = \\delta(x - \\xi), \\quad B_1[G] = 0, \\quad B_2[G] = 0$$\n<p>By linearity and superposition, once $G(x, \\xi)$ is known, the solution for <i>any</i> distributed source $f(x)$ is given by the integral convolution:</p>\n$$y(x) = \\int_a^b G(x, \\xi) f(\\xi)\\,d\\xi$$\n\n<h3>2. The Four Defining Properties of G(x, ξ)</h3>\n<div class=\"math-theorem\">\n<b>Axiomatic Properties of Green's Function:</b>\n<ol>\n<li><b>Differential Equation:</b> For $x \\ne \\xi$, $L[G(x, \\xi)] = 0$.</li>\n<li><b>Boundary Conditions:</b> $G(x, \\xi)$ satisfies the homogeneous boundary conditions $B_1[G] = 0$ at $x = a$ and $B_2[G] = 0$ at $x = b$.</li>\n<li><b>Continuity at $x = \\xi$:</b> $G(x, \\xi)$ is continuous across the point source:\n$$\\lim_{x \\to \\xi^+} G(x, \\xi) = \\lim_{x \\to \\xi^-} G(x, \\xi)$$</li>\n<li><b>Jump Discontinuity in Derivative:</b> Integrating $L[G] = -\\frac{d}{dx}[p(x) G'] + q(x)G = \\delta(x - \\xi)$ over $[\\xi - \\epsilon, \\xi + \\epsilon]$ as $\\epsilon \\to 0$ yields the jump condition:\n$$\\left. \\frac{\\partial G}{\\partial x} \\right|_{x = \\xi^+} - \\left. \\frac{\\partial G}{\\partial x} \\right|_{x = \\xi^-} = -\\frac{1}{p(\\xi)}$$</li>\n</ol>\n</div>"
        },
        {
          "secNumber": "8.3",
          "title": "Explicit Closed-Form Construction of Green's Functions for Second-Order Operators",
          "content": "<h3>1. Closed-Form Construction Recipe</h3>\n<p>Let $y_1(x)$ be a non-trivial solution of $L[y] = 0$ satisfying the boundary condition at $x = a$, and let $y_2(x)$ be a non-trivial solution satisfying the boundary condition at $x = b$.</p>\n<p>Since $G(x, \\xi)$ must satisfy $B_1[G] = 0$ for $x < \\xi$ and $B_2[G] = 0$ for $x > \\xi$:</p>\n$$G(x, \\xi) = \\begin{cases}\nc_1(\\xi) y_1(x), & a \\le x \\le \\xi \\\\\nc_2(\\xi) y_2(x), & \\xi \\le x \\le b\n\\end{cases}$$\n<p>Applying the continuity condition $c_2(\\xi) y_2(\\xi) - c_1(\\xi) y_1(\\xi) = 0$ and the jump condition $c_2(\\xi) y_2'(\\xi) - c_1(\\xi) y_1'(\\xi) = -\\frac{1}{p(\\xi)}$ gives a $2 \\times 2$ linear system for $c_1, c_2$ with determinant $W(y_1, y_2)(\\xi)$:</p>\n$$c_1(\\xi) = -\\frac{y_2(\\xi)}{p(\\xi) W(\\xi)}, \\quad c_2(\\xi) = -\\frac{y_1(\\xi)}{p(\\xi) W(\\xi)}$$\n<div class=\"math-theorem\">\n<b>Theorem 8.2 (Universal Green's Function Formula):</b>\n$$G(x, \\xi) = \\begin{cases}\n-\\frac{y_1(x) y_2(\\xi)}{p(\\xi) W(\\xi)}, & a \\le x \\le \\xi \\\\\n-\\frac{y_1(\\xi) y_2(x)}{p(\\xi) W(\\xi)}, & \\xi \\le x \\le b\n\\end{cases}$$\nBecause $p(\\xi) W(\\xi) = \\text{const}$ by Abel's identity, $G(x, \\xi)$ is perfectly <b>symmetric</b>: $G(x, \\xi) = G(\\xi, x)$.\n</div>"
        },
        {
          "secNumber": "8.4",
          "title": "Green's Function Representation of Inhomogeneous Solutions & Physical Applications",
          "content": "<h3>1. Physical Example: Deflection of a Taut Elastic String</h3>\n<p>A taut string of length $L$ under uniform tension $T$ clamped at both ends ($y(0) = 0, y(L) = 0$) subject to transverse load density $f(x)$ satisfies:</p>\n$$-T y''(x) = f(x), \\quad y(0) = 0, \\quad y(L) = 0$$\n<p>Here $p(x) = T$. The solutions satisfying the boundary conditions are $y_1(x) = x$ and $y_2(x) = L - x$. The Wronskian is $W(y_1, y_2) = x(-1) - (L - x)(1) = -L$. Hence $p W = -TL$. The Green's function is:</p>\n$$G(x, \\xi) = \\begin{cases}\n\\frac{x(L - \\xi)}{TL}, & 0 \\le x \\le \\xi \\\\\n\\frac{\\xi(L - x)}{TL}, & \\xi \\le x \\le L\n\\end{cases}$$\n<p>The deflection caused by a uniform distributed gravitational load $f(x) = \\rho g$ is:</p>\n$$y(x) = \\int_0^L G(x, \\xi) \\rho g\\,d\\xi = \\frac{\\rho g}{2T} x(L - x)$$\n<p>which matches the classical parabolic profile of hanging cables and beam theory.</p>"
        }
      ],
      "problems": [
        {
          "id": "prob-08",
          "tier": 1,
          "difficultyLabel": "Tier 1 • Foundational",
          "title": "Explicit Construction of Green's Function for y'' = f(x)",
          "statement": "Construct the Green's function for the Dirichlet boundary value problem:<br>$$y'' = f(x), \\quad y(0) = 0, \\quad y(1) = 0$$<br>and find the solution for $f(x) = x$.",
          "solution": "<b>Step 1: Linearly independent solutions satisfying boundary conditions</b><br>\nHomogeneous ODE: $y'' = 0 \\implies y(x) = c_1 x + c_2$.<br>\nLeft solution satisfying $y_1(0) = 0$: $y_1(x) = x$.<br>\nRight solution satisfying $y_2(1) = 0$: $y_2(x) = 1 - x$.<br><br>\n<b>Step 2: Wronskian computation</b><br>\n$$W(y_1, y_2) = y_1 y_2' - y_2 y_1' = x(-1) - (1 - x)(1) = -x - 1 + x = -1$$\nIn $L[y] = -y''$, $p(x) = 1$. So $-p W = -1(-1) = 1$.<br><br>\n<b>Step 3: Green's Function Formulation</b><br>\nFor $-y'' = -f(x)$, or directly:\n$$G(x, \\xi) = \\begin{cases}\nx(1 - \\xi), & 0 \\le x \\le \\xi \\\\\n\\xi(1 - x), & \\xi \\le x \\le 1\n\\end{cases}$$\n<br><b>Step 4: Solution for $f(x) = x$ (where $-y'' = -x \\implies y'' = x$)</b><br>\n$$y(x) = \\int_0^1 G(x, \\xi) (-\\xi)\\,d\\xi = -\\int_0^x \\xi(1 - x) \\xi\\,d\\xi - \\int_x^1 x(1 - \\xi) \\xi\\,d\\xi$$\nFirst integral:\n$$-(1 - x) \\int_0^x \\xi^2 d\\xi = -(1 - x) \\frac{x^3}{3} = -\\frac{x^3}{3} + \\frac{x^4}{3}$$\nSecond integral:\n$$-x \\int_x^1 (\\xi - \\xi^2) d\\xi = -x \\left[ \\frac{\\xi^2}{2} - \\frac{\\xi^3}{3} \\right]_x^1 = -x \\left( \\frac{1}{6} - \\frac{x^2}{2} + \\frac{x^3}{3} \\right) = -\\frac{x}{6} + \\frac{x^3}{2} - \\frac{x^4}{3}$$\nSumming both:\n$$y(x) = -\\frac{x^3}{3} + \\frac{x^4}{3} - \\frac{x}{6} + \\frac{x^3}{2} - \\frac{x^4}{3} = \\frac{x^3}{6} - \\frac{x}{6} = \\frac{x(x^2 - 1)}{6}$$\nVerify: $y'' = x, y(0) = 0, y(1) = 0$. Matches!",
          "answer": "$G(x, \\xi) = \\begin{cases} x(1-\\xi), & x \\le \\xi \\\\ \\xi(1-x), & x > \\xi \\end{cases}$ and $y(x) = \\frac{x(x^2 - 1)}{6}$",
          "difficulty": "Easy"
        },
        {
          "id": "prob-16",
          "tier": 2,
          "difficultyLabel": "Tier 2 • Intermediate Exam",
          "title": "Solvability Condition via the Fredholm Alternative",
          "statement": "Determine the exact condition on the function $h(x)$ for the boundary value problem to possess a solution:<br>$$y'' + \\pi^2 y = h(x), \\quad y(0) = 0, \\quad y(1) = 0$$",
          "solution": "<b>Step 1: Check homogeneous boundary value problem</b><br>\n$$y_h'' + \\pi^2 y_h = 0 \\implies y_h(x) = c_1 \\cos(\\pi x) + c_2 \\sin(\\pi x)$$\nBoundary conditions:\n$$y_h(0) = c_1 = 0 \\implies y_h(x) = c_2 \\sin(\\pi x)$$\n$$y_h(1) = c_2 \\sin(\\pi) = 0 \\quad (\\text{satisfied for any } c_2)$$\nThe homogeneous problem has non-trivial solution $\\phi(x) = \\sin(\\pi x)$.<br><br>\n<b>Step 2: Self-adjointness of operator</b><br>\nThe operator $L[y] = y'' + \\pi^2 y$ with Dirichlet conditions $y(0) = y(1) = 0$ is formally self-adjoint:\n$$\\int_0^1 (u L[v] - v L[u])\\,dx = [u v' - v u']_0^1 = 0$$\n<br><b>Step 3: Apply the Fredholm Alternative (Case II)</b><br>\nBy Theorem 8.1, the nonhomogeneous problem has a solution if and only if $h(x)$ is orthogonal to the null space of the adjoint operator:\n$$\\int_0^1 h(x) \\phi(x)\\,dx = 0 \\implies \\int_0^1 h(x) \\sin(\\pi x)\\,dx = 0$$\nIf this integral is zero, an infinite family of solutions exists ($y(x) = y_p(x) + c \\sin(\\pi x)$). If non-zero, NO solution exists.",
          "answer": "Solvability condition: $\\int_0^1 h(x) \\sin(\\pi x)\\,dx = 0$.",
          "difficulty": "Medium"
        },
        {
          "id": "prob-23",
          "tier": 3,
          "difficultyLabel": "Tier 3 • Honors Challenge",
          "title": "Bilinear Mercer Eigenfunction Expansion of Green's Function",
          "statement": "Prove the bilinear eigenfunction expansion for the Green's function of a regular Sturm-Liouville problem:<br>$$G(x, \\xi) = \\sum_{n=1}^\\infty \\frac{\\phi_n(x) \\phi_n(\\xi)}{\\lambda_n}$$",
          "solution": "<b>Step 1: Expand Green's function in orthonormal eigenfunctions</b><br>\nLet $\\{\\phi_n(x)\\}$ be the complete orthonormal eigenfunctions of $L[\\phi_n] = \\lambda_n w(x) \\phi_n$ with separated boundary conditions. For any fixed $\\xi \\in (a, b)$, $G(x, \\xi)$ satisfies the boundary conditions in $x$. Expand $G(x, \\xi)$ in terms of $\\phi_n(x)$:\n$$G(x, \\xi) = \\sum_{n=1}^\\infty c_n(\\xi) \\phi_n(x)$$\n<br><b>Step 2: Determine expansion coefficients $c_n(\\xi)$</b><br>\nBy orthonormality $\\int_a^b \\phi_n(x) \\phi_m(x) w(x)\\,dx = \\delta_{nm}$:\n$$c_n(\\xi) = \\int_a^b G(x, \\xi) \\phi_n(x) w(x)\\,dx$$\n<br><b>Step 3: Exploit self-adjointness and eigenvalue equation</b><br>\nSince $\\phi_n(x) = \\frac{1}{\\lambda_n w(x)} L[\\phi_n](x)$:\n$$c_n(\\xi) = \\frac{1}{\\lambda_n} \\int_a^b G(x, \\xi) L[\\phi_n](x)\\,dx$$\nUsing Green's formula $\\int_a^b (u L[v] - v L[u])\\,dx = 0$:\n$$c_n(\\xi) = \\frac{1}{\\lambda_n} \\int_a^b \\phi_n(x) L_x[G(x, \\xi)]\\,dx$$\nSince $L_x[G(x, \\xi)] = \\delta(x - \\xi)$:\n$$c_n(\\xi) = \\frac{1}{\\lambda_n} \\int_a^b \\phi_n(x) \\delta(x - \\xi)\\,dx = \\frac{\\phi_n(\\xi)}{\\lambda_n}$$\n<br><b>Step 4: Substitute $c_n(\\xi)$ back</b><br>\n$$G(x, \\xi) = \\sum_{n=1}^\\infty \\frac{\\phi_n(x) \\phi_n(\\xi)}{\\lambda_n}$$\nThis Mercer series proves the exact symmetry $G(x, \\xi) = G(\\xi, x)$ and convergence in $L^2$.",
          "answer": "$G(x, \\xi) = \\sum_{n=1}^\\infty \\frac{\\phi_n(x) \\phi_n(\\xi)}{\\lambda_n}$ (Mercer's Bilinear Expansion).",
          "difficulty": "Hard"
        }
      ]
    }
  ],
  "problems": [
    {
      "id": "prob-01",
      "tier": 1,
      "difficultyLabel": "Tier 1 • Foundational",
      "title": "Homogeneous 2x2 System with Real Distinct Eigenvalues",
      "statement": "Solve the initial value problem for the linear system:<br>$$\\frac{d\\vec{x}}{dt} = \\begin{pmatrix} 1 & 2 \\\\ 2 & 1 \\end{pmatrix} \\vec{x}, \\quad \\vec{x}(0) = \\begin{pmatrix} 3 \\\\ 1 \\end{pmatrix}$$",
      "solution": "<b>Step 1: Eigenvalues of the system matrix</b><br>\n$$\\det(\\mathbf{A} - \\lambda \\mathbf{I}) = \\begin{vmatrix} 1 - \\lambda & 2 \\\\ 2 & 1 - \\lambda \\end{vmatrix} = (1 - \\lambda)^2 - 4 = \\lambda^2 - 2\\lambda - 3 = 0$$\nFactorizing yields $(\\lambda - 3)(\\lambda + 1) = 0 \\implies \\lambda_1 = 3, \\lambda_2 = -1$.<br><br>\n<b>Step 2: Eigenvector for $\\lambda_1 = 3$</b><br>\n$$(\\mathbf{A} - 3\\mathbf{I})\\vec{v}_1 = \\begin{pmatrix} -2 & 2 \\\\ 2 & -2 \\end{pmatrix} \\begin{pmatrix} v_{11} \\\\ v_{12} \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 0 \\end{pmatrix} \\implies v_{11} = v_{12} \\implies \\vec{v}_1 = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}$$\n<br><b>Step 3: Eigenvector for $\\lambda_2 = -1$</b><br>\n$$(\\mathbf{A} + \\mathbf{I})\\vec{v}_2 = \\begin{pmatrix} 2 & 2 \\\\ 2 & 2 \\end{pmatrix} \\begin{pmatrix} v_{21} \\\\ v_{22} \\end{pmatrix} = \\begin{pmatrix} 0 \\\\ 0 \\end{pmatrix} \\implies v_{21} = -v_{22} \\implies \\vec{v}_2 = \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix}$$\n<br><b>Step 4: General Solution & Initial Condition</b><br>\n$$\\vec{x}(t) = c_1 e^{3t} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} + c_2 e^{-t} \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix}$$\nAt $t = 0$:\n$$\\vec{x}(0) = \\begin{pmatrix} c_1 + c_2 \\\\ c_1 - c_2 \\end{pmatrix} = \\begin{pmatrix} 3 \\\\ 1 \\end{pmatrix}$$\nAdding both equations: $2c_1 = 4 \\implies c_1 = 2$. Subtracting: $2c_2 = 2 \\implies c_2 = 1$.<br><br>\n$$\\vec{x}(t) = 2e^{3t} \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix} + e^{-t} \\begin{pmatrix} 1 \\\\ -1 \\end{pmatrix} = \\begin{pmatrix} 2e^{3t} + e^{-t} \\\\ 2e^{3t} - e^{-t} \\end{pmatrix}$$",
      "answer": "$\\vec{x}(t) = \\begin{pmatrix} 2e^{3t} + e^{-t} \\\\ 2e^{3t} - e^{-t} \\end{pmatrix}$",
      "difficulty": "Easy"
    },
    {
      "id": "prob-02",
      "tier": 1,
      "difficultyLabel": "Tier 1 • Foundational",
      "title": "Matrix Exponential for Defective Repeated Eigenvalue Matrix",
      "statement": "Compute the matrix exponential $e^{\\mathbf{A}t}$ for the defective matrix:<br>$$\\mathbf{A} = \\begin{pmatrix} 2 & 1 \\\\ 0 & 2 \\end{pmatrix}$$",
      "solution": "<b>Step 1: Nilpotent Decomposition</b><br>\nNotice that $\\mathbf{A}$ can be split into a scalar multiple of identity and a nilpotent upper-triangular matrix:\n$$\\mathbf{A} = 2\\mathbf{I} + \\mathbf{N}, \\quad \\text{where } \\mathbf{N} = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix}$$\nObserve that $\\mathbf{N}^2 = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} = \\begin{pmatrix} 0 & 0 \\\\ 0 & 0 \\end{pmatrix}$. Thus $\\mathbf{N}$ is nilpotent of degree 2.<br><br>\n<b>Step 2: Commuting Matrices Property</b><br>\nSince $(2\\mathbf{I}t)(\\mathbf{N}t) = (\\mathbf{N}t)(2\\mathbf{I}t)$, we can multiply their exponentials:\n$$e^{\\mathbf{A}t} = e^{2\\mathbf{I}t + \\mathbf{N}t} = e^{2\\mathbf{I}t} e^{\\mathbf{N}t}$$\n<br><b>Step 3: Exponentiation of Terms</b><br>\n$$e^{2\\mathbf{I}t} = e^{2t} \\mathbf{I} = \\begin{pmatrix} e^{2t} & 0 \\\\ 0 & e^{2t} \\end{pmatrix}$$\n$$e^{\\mathbf{N}t} = \\mathbf{I} + t\\mathbf{N} + \\frac{t^2}{2!} \\mathbf{N}^2 + \\dots = \\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix} + t \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix} = \\begin{pmatrix} 1 & t \\\\ 0 & 1 \\end{pmatrix}$$\n<br><b>Step 4: Matrix Multiplication</b><br>\n$$e^{\\mathbf{A}t} = e^{2t} \\begin{pmatrix} 1 & t \\\\ 0 & 1 \\end{pmatrix} = \\begin{pmatrix} e^{2t} & t e^{2t} \\\\ 0 & e^{2t} \\end{pmatrix}$$",
      "answer": "$e^{\\mathbf{A}t} = \\begin{pmatrix} e^{2t} & t e^{2t} \\\\ 0 & e^{2t} \\end{pmatrix}$",
      "difficulty": "Easy"
    },
    {
      "id": "prob-03",
      "tier": 1,
      "difficultyLabel": "Tier 1 • Foundational",
      "title": "Variation of Parameters for Nonhomogeneous 2x2 System",
      "statement": "Find a particular solution using Variation of Parameters for the system:<br>$$\\vec{x}' = \\begin{pmatrix} 0 & 1 \\\\ -2 & 3 \\end{pmatrix} \\vec{x} + \\begin{pmatrix} 0 \\\\ e^t \\end{pmatrix}$$",
      "solution": "<b>Step 1: Homogeneous eigenvalues and eigenvectors</b><br>\n$\\det(\\mathbf{A} - \\lambda \\mathbf{I}) = \\lambda^2 - 3\\lambda + 2 = (\\lambda - 1)(\\lambda - 2) = 0 \\implies \\lambda_1 = 1, \\lambda_2 = 2$.<br>\nFor $\\lambda_1 = 1$: $(\\mathbf{A} - \\mathbf{I})\\vec{v}_1 = \\begin{pmatrix} -1 & 1 \\\\ -2 & 2 \\end{pmatrix} \\begin{pmatrix} v_1 \\\\ v_2 \\end{pmatrix} = \\vec{0} \\implies \\vec{v}_1 = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}$.<br>\nFor $\\lambda_2 = 2$: $(\\mathbf{A} - 2\\mathbf{I})\\vec{v}_2 = \\begin{pmatrix} -2 & 1 \\\\ -2 & 1 \\end{pmatrix} \\begin{pmatrix} v_1 \\\\ v_2 \\end{pmatrix} = \\vec{0} \\implies \\vec{v}_2 = \\begin{pmatrix} 1 \\\\ 2 \\end{pmatrix}$.<br><br>\n<b>Step 2: Fundamental Matrix $\\mathbf{\\Phi}(t)$</b><br>\n$$\\mathbf{\\Phi}(t) = \\begin{pmatrix} e^t & e^{2t} \\\\ e^t & 2e^{2t} \\end{pmatrix}, \\quad \\det \\mathbf{\\Phi}(t) = 2e^{3t} - e^{3t} = e^{3t}$$\n$$\\mathbf{\\Phi}^{-1}(t) = \\frac{1}{e^{3t}} \\begin{pmatrix} 2e^{2t} & -e^{2t} \\\\ -e^t & e^t \\end{pmatrix} = \\begin{pmatrix} 2e^{-t} & -e^{-t} \\\\ -e^{-2t} & e^{-2t} \\end{pmatrix}$$\n<br><b>Step 3: Integrate $\\vec{u}'(t) = \\mathbf{\\Phi}^{-1}(t) \\vec{g}(t)$</b><br>\n$$\\vec{u}'(t) = \\begin{pmatrix} 2e^{-t} & -e^{-t} \\\\ -e^{-2t} & e^{-2t} \\end{pmatrix} \\begin{pmatrix} 0 \\\\ e^t \\end{pmatrix} = \\begin{pmatrix} -1 \\\\ e^{-t} \\end{pmatrix}$$\nIntegrating with respect to $t$:\n$$\\vec{u}(t) = \\begin{pmatrix} -t \\\\ -e^{-t} \\end{pmatrix}$$\n<br><b>Step 4: Form Particular Solution $\\vec{x}_p(t) = \\mathbf{\\Phi}(t) \\vec{u}(t)$</b><br>\n$$\\vec{x}_p(t) = \\begin{pmatrix} e^t & e^{2t} \\\\ e^t & 2e^{2t} \\end{pmatrix} \\begin{pmatrix} -t \\\\ -e^{-t} \\end{pmatrix} = \\begin{pmatrix} -t e^t - e^t \\\\ -t e^t - 2e^t \\end{pmatrix}$$",
      "answer": "$\\vec{x}_p(t) = \\begin{pmatrix} -(t + 1)e^t \\\\ -(t + 2)e^t \\end{pmatrix}$",
      "difficulty": "Easy"
    },
    {
      "id": "prob-04",
      "tier": 1,
      "difficultyLabel": "Tier 1 • Foundational",
      "title": "Power Series Solution of Airy-Type Equation about x = 0",
      "statement": "Find the general power series solution about the ordinary point $x_0 = 0$ for:<br>$$y'' - x y = 0$$",
      "solution": "<b>Step 1: Series Substitution</b><br>\nLet $y = \\sum_{n=0}^\\infty a_n x^n$. Then:\n$$y'' = \\sum_{n=2}^\\infty n(n - 1) a_n x^{n-2}, \\quad x y = \\sum_{n=0}^\\infty a_n x^{n+1}$$\n<br><b>Step 2: Align Indices</b><br>\nLet $k$ be the power of $x$:\nIn $y''$: $k = n - 2 \\implies n = k + 2 \\implies \\sum_{k=0}^\\infty (k + 2)(k + 1) a_{k+2} x^k$.\nFor $k = 0$: $2(1) a_2 = 0 \\implies a_2 = 0$.\nFor $k \\ge 1$: let $j = k - 1 \\ge 0$, equating coefficients gives:\n$$(k + 2)(k + 1) a_{k+2} = a_{k-1} \\implies a_{k+2} = \\frac{a_{k-1}}{(k + 2)(k + 1)}$$\nSetting $k + 2 = n$:\n$$a_n = \\frac{a_{n-3}}{n(n - 1)} \\quad \\text{for } n \\ge 3$$\n<br><b>Step 3: Compute Coefficients</b><br>\nSince $a_2 = 0$, all terms $a_{3m+2} = 0$.<br>\nMultiples of 3 (governed by $a_0$):\n$$a_3 = \\frac{a_0}{3 \\cdot 2}, \\quad a_6 = \\frac{a_3}{6 \\cdot 5} = \\frac{a_0}{6 \\cdot 5 \\cdot 3 \\cdot 2}$$\nTerms of form $3m+1$ (governed by $a_1$):\n$$a_4 = \\frac{a_1}{4 \\cdot 3}, \\quad a_7 = \\frac{a_4}{7 \\cdot 6} = \\frac{a_1}{7 \\cdot 6 \\cdot 4 \\cdot 3}$$\n<br><b>Step 4: Solution</b><br>\n$$y(x) = a_0 \\left( 1 + \\frac{x^3}{6} + \\frac{x^6}{180} + \\dots \\right) + a_1 \\left( x + \\frac{x^4}{12} + \\frac{x^7}{504} + \\dots \\right)$$",
      "answer": "$y(x) = a_0 \\left(1 + \\frac{x^3}{6} + \\frac{x^6}{180} + \\dots\\right) + a_1 \\left(x + \\frac{x^4}{12} + \\frac{x^7}{504} + \\dots\\right)$",
      "difficulty": "Easy"
    },
    {
      "id": "prob-05",
      "tier": 1,
      "difficultyLabel": "Tier 1 • Foundational",
      "title": "Frobenius Series Case 1: Roots Differing by Non-Integer",
      "statement": "Find the Frobenius series solutions about $x = 0$ for:<br>$$2x y'' + y' + y = 0$$",
      "solution": "<b>Step 1: Identify singularity and indicial equation</b><br>\nNormalized form: $y'' + \\frac{1}{2x} y' + \\frac{1}{2x} y = 0$.\n$p(x) = x P(x) = \\frac{1}{2} \\implies p_0 = \\frac{1}{2}$, and $q(x) = x^2 Q(x) = \\frac{x}{2} \\implies q_0 = 0$.\nThe point $x = 0$ is a regular singular point.\nIndicial equation:\n$$r(r - 1) + \\frac{1}{2} r + 0 = r\\left(r - \\frac{1}{2}\\right) = 0 \\implies r_1 = \\frac{1}{2}, \\quad r_2 = 0$$\nSince $r_1 - r_2 = \\frac{1}{2} \\notin \\mathbb{Z}$, this is <b>Case 1</b> (two distinct Frobenius series).<br><br>\n<b>Step 2: Recurrence relation for general $r$</b><br>\nSubstitute $y = \\sum_{n=0}^\\infty a_n x^{n+r}$:\n$$2 \\sum (n+r)(n+r-1) a_n x^{n+r-1} + \\sum (n+r) a_n x^{n+r-1} + \\sum a_n x^{n+r} = 0$$\nFor $n \\ge 1$:\n$$[(n+r)(2n + 2r - 1)] a_n = -a_{n-1} \\implies a_n = -\\frac{a_{n-1}}{(n+r)(2n + 2r - 1)}$$\n<br><b>Step 3: Solution for $r_1 = 1/2$</b><br>\nDenominator factor: $(n + 1/2)(2n) = n(2n + 1)$.\n$$a_n = -\\frac{a_{n-1}}{n(2n + 1)} \\implies y_1(x) = x^{1/2} \\left( 1 - \\frac{x}{3} + \\frac{x^2}{30} - \\frac{x^3}{630} + \\dots \\right)$$\n<br><b>Step 4: Solution for $r_2 = 0$</b><br>\nDenominator factor: $n(2n - 1)$.\n$$a_n = -\\frac{a_{n-1}}{n(2n - 1)} \\implies y_2(x) = 1 - x + \\frac{x^2}{6} - \\frac{x^3}{90} + \\dots$$",
      "answer": "$y(x) = c_1 x^{1/2}\\left(1 - \\frac{x}{3} + \\frac{x^2}{30} - \\dots\\right) + c_2 \\left(1 - x + \\frac{x^2}{6} - \\dots\\right)$",
      "difficulty": "Easy"
    },
    {
      "id": "prob-06",
      "tier": 1,
      "difficultyLabel": "Tier 1 • Foundational",
      "title": "Legendre Polynomial P_3(x) and Orthogonality Verification",
      "statement": "Derive $P_3(x)$ via Rodrigues' formula and verify the orthogonality $\\int_{-1}^1 P_1(x) P_3(x)\\,dx = 0$.",
      "solution": "<b>Step 1: Rodrigues' Formula for $n = 3$</b><br>\n$$P_3(x) = \\frac{1}{2^3 \\cdot 3!} \\frac{d^3}{dx^3} (x^2 - 1)^3 = \\frac{1}{48} \\frac{d^3}{dx^3} (x^6 - 3x^4 + 3x^2 - 1)$$\nFirst derivative:\n$$\\frac{d}{dx}(x^6 - 3x^4 + 3x^2 - 1) = 6x^5 - 12x^3 + 6x$$\nSecond derivative:\n$$\\frac{d^2}{dx^2} = 30x^4 - 36x^2 + 6$$\nThird derivative:\n$$\\frac{d^3}{dx^3} = 120x^3 - 72x$$\nDividing by 48:\n$$P_3(x) = \\frac{120x^3 - 72x}{48} = \\frac{5}{2}x^3 - \\frac{3}{2}x = \\frac{1}{2}(5x^3 - 3x)$$\n<br><b>Step 2: Orthogonality integral with $P_1(x) = x$</b><br>\n$$\\int_{-1}^1 P_1(x) P_3(x)\\,dx = \\int_{-1}^1 x \\cdot \\frac{1}{2}(5x^3 - 3x)\\,dx = \\frac{1}{2} \\int_{-1}^1 (5x^4 - 3x^2)\\,dx$$\nBecause the integrand is even:\n$$= \\int_0^1 (5x^4 - 3x^2)\\,dx = \\left[ x^5 - x^3 \\right]_0^1 = (1 - 1) - 0 = 0$$\nOrthogonality is verified identically!",
      "answer": "$P_3(x) = \\frac{1}{2}(5x^3 - 3x)$ and $\\int_{-1}^1 P_1(x)P_3(x)\\,dx = 0$.",
      "difficulty": "Easy"
    },
    {
      "id": "prob-07",
      "tier": 1,
      "difficultyLabel": "Tier 1 • Foundational",
      "title": "Regular Sturm-Liouville Eigenvalues & Mixed Boundary Conditions",
      "statement": "Find all eigenvalues and eigenfunctions of the regular Sturm-Liouville problem:<br>$$y'' + \\lambda y = 0, \\quad y(0) = 0, \\quad y'(\\pi) = 0$$",
      "solution": "<b>Case 1: $\\lambda < 0$ ($\\lambda = -\\mu^2, \\mu > 0$)</b><br>\n$y(x) = c_1 \\cosh(\\mu x) + c_2 \\sinh(\\mu x)$.<br>\n$y(0) = c_1 = 0 \\implies y(x) = c_2 \\sinh(\\mu x)$.<br>\n$y'(\\pi) = c_2 \\mu \\cosh(\\mu \\pi) = 0$. Since $\\mu \\ne 0$ and $\\cosh(\\mu \\pi) \\ge 1$, $c_2 = 0$. No non-trivial solutions.<br><br>\n<b>Case 2: $\\lambda = 0$</b><br>\n$y(x) = c_1 x + c_2$. $y(0) = c_2 = 0$. $y'(x) = c_1 \\implies y'(\\pi) = c_1 = 0$. Only trivial solution.<br><br>\n<b>Case 3: $\\lambda > 0$ ($\\lambda = k^2, k > 0$)</b><br>\n$y(x) = c_1 \\cos(kx) + c_2 \\sin(kx)$.<br>\n$y(0) = c_1 = 0 \\implies y(x) = c_2 \\sin(kx)$.<br>\n$y'(x) = c_2 k \\cos(kx) \\implies y'(\\pi) = c_2 k \\cos(k\\pi) = 0$.<br>\nFor non-trivial solutions ($c_2 \\ne 0$), we require:\n$$\\cos(k\\pi) = 0 \\implies k\\pi = \\left(n - \\frac{1}{2}\\right)\\pi \\implies k_n = n - \\frac{1}{2} = \\frac{2n - 1}{2}, \\quad n = 1, 2, 3, \\dots$$\n<br><b>Step 4: Eigenvalues & Orthonormal Eigenfunctions</b><br>\n$$\\lambda_n = k_n^2 = \\frac{(2n - 1)^2}{4}, \\quad y_n(x) = \\sin\\left(\\frac{2n - 1}{2} x\\right)$$\nNorm: $\\int_0^\\pi \\sin^2\\left(\\frac{2n - 1}{2} x\\right) dx = \\frac{\\pi}{2}$.\nOrthonormal set: $\\phi_n(x) = \\sqrt{\\frac{2}{\\pi}} \\sin\\left(\\frac{2n - 1}{2} x\\right)$.",
      "answer": "$\\lambda_n = \\frac{(2n - 1)^2}{4}, \\quad y_n(x) = \\sin\\left(\\frac{2n - 1}{2} x\\right), \\quad n = 1, 2, 3, \\dots$",
      "difficulty": "Easy"
    },
    {
      "id": "prob-08",
      "tier": 1,
      "difficultyLabel": "Tier 1 • Foundational",
      "title": "Explicit Construction of Green's Function for y'' = f(x)",
      "statement": "Construct the Green's function for the Dirichlet boundary value problem:<br>$$y'' = f(x), \\quad y(0) = 0, \\quad y(1) = 0$$<br>and find the solution for $f(x) = x$.",
      "solution": "<b>Step 1: Linearly independent solutions satisfying boundary conditions</b><br>\nHomogeneous ODE: $y'' = 0 \\implies y(x) = c_1 x + c_2$.<br>\nLeft solution satisfying $y_1(0) = 0$: $y_1(x) = x$.<br>\nRight solution satisfying $y_2(1) = 0$: $y_2(x) = 1 - x$.<br><br>\n<b>Step 2: Wronskian computation</b><br>\n$$W(y_1, y_2) = y_1 y_2' - y_2 y_1' = x(-1) - (1 - x)(1) = -x - 1 + x = -1$$\nIn $L[y] = -y''$, $p(x) = 1$. So $-p W = -1(-1) = 1$.<br><br>\n<b>Step 3: Green's Function Formulation</b><br>\nFor $-y'' = -f(x)$, or directly:\n$$G(x, \\xi) = \\begin{cases}\nx(1 - \\xi), & 0 \\le x \\le \\xi \\\\\n\\xi(1 - x), & \\xi \\le x \\le 1\n\\end{cases}$$\n<br><b>Step 4: Solution for $f(x) = x$ (where $-y'' = -x \\implies y'' = x$)</b><br>\n$$y(x) = \\int_0^1 G(x, \\xi) (-\\xi)\\,d\\xi = -\\int_0^x \\xi(1 - x) \\xi\\,d\\xi - \\int_x^1 x(1 - \\xi) \\xi\\,d\\xi$$\nFirst integral:\n$$-(1 - x) \\int_0^x \\xi^2 d\\xi = -(1 - x) \\frac{x^3}{3} = -\\frac{x^3}{3} + \\frac{x^4}{3}$$\nSecond integral:\n$$-x \\int_x^1 (\\xi - \\xi^2) d\\xi = -x \\left[ \\frac{\\xi^2}{2} - \\frac{\\xi^3}{3} \\right]_x^1 = -x \\left( \\frac{1}{6} - \\frac{x^2}{2} + \\frac{x^3}{3} \\right) = -\\frac{x}{6} + \\frac{x^3}{2} - \\frac{x^4}{3}$$\nSumming both:\n$$y(x) = -\\frac{x^3}{3} + \\frac{x^4}{3} - \\frac{x}{6} + \\frac{x^3}{2} - \\frac{x^4}{3} = \\frac{x^3}{6} - \\frac{x}{6} = \\frac{x(x^2 - 1)}{6}$$\nVerify: $y'' = x, y(0) = 0, y(1) = 0$. Matches!",
      "answer": "$G(x, \\xi) = \\begin{cases} x(1-\\xi), & x \\le \\xi \\\\ \\xi(1-x), & x > \\xi \\end{cases}$ and $y(x) = \\frac{x(x^2 - 1)}{6}$",
      "difficulty": "Easy"
    },
    {
      "id": "prob-09",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Intermediate Exam",
      "title": "3x3 System with Complex Eigenvalues & Invariant Orbital Manifold",
      "statement": "Solve the $3 \\times 3$ linear differential system:<br>$$\\vec{x}' = \\begin{pmatrix} 0 & 1 & 0 \\\\ -4 & 0 & 0 \\\\ 0 & 0 & -2 \\end{pmatrix} \\vec{x}, \\quad \\vec{x}(0) = \\begin{pmatrix} 1 \\\\ 0 \\\\ 2 \\end{pmatrix}$$",
      "solution": "<b>Step 1: Block structure and eigenvalues</b><br>\nThe matrix is block diagonal: $\\mathbf{A} = \\begin{pmatrix} \\mathbf{B} & \\vec{0} \\\\ \\vec{0}^T & -2 \\end{pmatrix}$ where $\\mathbf{B} = \\begin{pmatrix} 0 & 1 \\\\ -4 & 0 \\end{pmatrix}$.\n$\\det(\\mathbf{B} - \\lambda \\mathbf{I}) = \\lambda^2 + 4 = 0 \\implies \\lambda_{1, 2} = \\pm 2i$.\nThe third eigenvalue is $\\lambda_3 = -2$.<br><br>\n<b>Step 2: Eigenvectors</b><br>\nFor $\\lambda_1 = 2i$:\n$$\\begin{pmatrix} -2i & 1 & 0 \\\\ -4 & -2i & 0 \\\\ 0 & 0 & -2 - 2i \\end{pmatrix} \\begin{pmatrix} v_1 \\\\ v_2 \\\\ v_3 \\end{pmatrix} = \\vec{0} \\implies v_3 = 0, \\quad v_2 = 2i v_1 \\implies \\vec{v} = \\begin{pmatrix} 1 \\\\ 2i \\\\ 0 \\end{pmatrix} = \\begin{pmatrix} 1 \\\\ 0 \\\\ 0 \\end{pmatrix} + i \\begin{pmatrix} 0 \\\\ 2 \\\\ 0 \\end{pmatrix}$$\nReal independent solutions:\n$$\\vec{x}_1(t) = \\begin{pmatrix} \\cos 2t \\\\ -2\\sin 2t \\\\ 0 \\end{pmatrix}, \\quad \\vec{x}_2(t) = \\begin{pmatrix} \\sin 2t \\\\ 2\\cos 2t \\\\ 0 \\end{pmatrix}$$\nFor $\\lambda_3 = -2$:\n$$\\vec{v}_3 = \\begin{pmatrix} 0 \\\\ 0 \\\\ 1 \\end{pmatrix} \\implies \\vec{x}_3(t) = e^{-2t} \\begin{pmatrix} 0 \\\\ 0 \\\\ 1 \\end{pmatrix}$$\n<br><b>Step 3: Initial conditions</b><br>\n$$\\vec{x}(t) = c_1 \\begin{pmatrix} \\cos 2t \\\\ -2\\sin 2t \\\\ 0 \\end{pmatrix} + c_2 \\begin{pmatrix} \\sin 2t \\\\ 2\\cos 2t \\\\ 0 \\end{pmatrix} + c_3 \\begin{pmatrix} 0 \\\\ 0 \\\\ e^{-2t} \\end{pmatrix}$$\nAt $t = 0$: $c_1 = 1, 2c_2 = 0 \\implies c_2 = 0$, and $c_3 = 2$.<br><br>\n$$\\vec{x}(t) = \\begin{pmatrix} \\cos 2t \\\\ -2\\sin 2t \\\\ 2e^{-2t} \\end{pmatrix}$$",
      "answer": "$\\vec{x}(t) = \\begin{pmatrix} \\cos 2t \\\\ -2\\sin 2t \\\\ 2e^{-2t} \\end{pmatrix}$",
      "difficulty": "Medium"
    },
    {
      "id": "prob-10",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Intermediate Exam",
      "title": "Putzer's Algorithm for 3x3 Nilpotent Jordan Block",
      "statement": "Use Putzer's algorithm to compute the matrix exponential $e^{\\mathbf{A}t}$ for the $3 \\times 3$ matrix:<br>$$\\mathbf{A} = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 1 \\\\ 0 & 0 & 0 \\end{pmatrix}$$",
      "solution": "<b>Step 1: Eigenvalues</b><br>\nThe characteristic polynomial is $\\det(\\mathbf{A} - \\lambda \\mathbf{I}) = -\\lambda^3 = 0 \\implies \\lambda_1 = \\lambda_2 = \\lambda_3 = 0$.<br><br>\n<b>Step 2: Putzer's polynomial matrices $\\mathbf{P}_k$</b><br>\n$$\\mathbf{P}_0 = \\mathbf{I} = \\begin{pmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$$\n$$\\mathbf{P}_1 = \\mathbf{A} - \\lambda_1 \\mathbf{I} = \\mathbf{A} = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 1 \\\\ 0 & 0 & 0 \\end{pmatrix}$$\n$$\\mathbf{P}_2 = (\\mathbf{A} - \\lambda_2 \\mathbf{I})\\mathbf{P}_1 = \\mathbf{A}^2 = \\begin{pmatrix} 0 & 0 & 1 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix}$$\n<br><b>Step 3: Scalar differential equations for $r_k(t)$</b><br>\n$r_1'(t) = 0, r_1(0) = 1 \\implies r_1(t) = 1$.<br>\n$r_2'(t) = r_1(t) = 1, r_2(0) = 0 \\implies r_2(t) = t$.<br>\n$r_3'(t) = r_2(t) = t, r_3(0) = 0 \\implies r_3(t) = \\frac{t^2}{2}$.<br><br>\n<b>Step 4: Matrix exponential assembly</b><br>\n$$e^{\\mathbf{A}t} = r_1(t)\\mathbf{P}_0 + r_2(t)\\mathbf{P}_1 + r_3(t)\\mathbf{P}_2 = \\mathbf{I} + t\\mathbf{A} + \\frac{t^2}{2}\\mathbf{A}^2 = \\begin{pmatrix} 1 & t & t^2/2 \\\\ 0 & 1 & t \\\\ 0 & 0 & 1 \\end{pmatrix}$$",
      "answer": "$e^{\\mathbf{A}t} = \\begin{pmatrix} 1 & t & t^2/2 \\\\ 0 & 1 & t \\\\ 0 & 0 & 1 \\end{pmatrix}$",
      "difficulty": "Medium"
    },
    {
      "id": "prob-11",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Intermediate Exam",
      "title": "Frobenius Method Case 2: Equal Indicial Roots & Logarithmic Branch",
      "statement": "Find two linearly independent solutions about $x = 0$ for:<br>$$x y'' + y' - y = 0$$",
      "solution": "<b>Step 1: Indicial equation</b><br>\nMultiply by $x$: $x^2 y'' + x y' - x y = 0$.\n$p(x) = 1 \\implies p_0 = 1$, $q(x) = -x \\implies q_0 = 0$.\nIndicial equation: $F(r) = r(r - 1) + r = r^2 = 0 \\implies r_1 = r_2 = 0$.\nEqual roots $\\implies$ <b>Case 2</b> (logarithmic second solution).<br><br>\n<b>Step 2: Recurrence relation for $y(x, r)$</b><br>\nSubstitute $y(x, r) = \\sum_{n=0}^\\infty a_n(r) x^{n+r}$:\n$$F(n + r) a_n = a_{n-1} \\implies (n + r)^2 a_n(r) = a_{n-1}(r) \\implies a_n(r) = \\frac{a_0}{[(1+r)(2+r)\\dots(n+r)]^2}$$\nFor $r = 0$ and $a_0 = 1$:\n$$a_n(0) = \\frac{1}{(n!)^2} \\implies y_1(x) = \\sum_{n=0}^\\infty \\frac{x^n}{(n!)^2} = 1 + x + \\frac{x^2}{4} + \\frac{x^3}{36} + \\dots$$\n<br><b>Step 3: Differentiate with respect to $r$ to obtain $y_2(x)$</b><br>\n$$y_2(x) = \\left. \\frac{\\partial y(x, r)}{\\partial r} \\right|_{r=0} = y_1(x) \\ln x + \\sum_{n=1}^\\infty a_n'(0) x^n$$\nUsing logarithmic differentiation on $a_n(r)$:\n$$\\ln a_n(r) = -2 \\sum_{k=1}^n \\ln(k + r) \\implies \\frac{a_n'(r)}{a_n(r)} = -2 \\sum_{k=1}^n \\frac{1}{k + r}$$\nAt $r = 0$: $a_n'(0) = -2 H_n a_n(0) = -2 \\frac{H_n}{(n!)^2}$, where $H_n = \\sum_{k=1}^n \\frac{1}{k}$ is the $n$-th harmonic number.<br><br>\n$$y_2(x) = y_1(x) \\ln x - 2 \\sum_{n=1}^\\infty \\frac{H_n}{(n!)^2} x^n = y_1(x) \\ln x - 2\\left( x + \\frac{3}{8}x^2 + \\frac{11}{216}x^3 + \\dots \\right)$$",
      "answer": "$y_1(x) = \\sum_{n=0}^\\infty \\frac{x^n}{(n!)^2}, \\quad y_2(x) = y_1(x)\\ln x - 2\\sum_{n=1}^\\infty \\frac{H_n}{(n!)^2} x^n$",
      "difficulty": "Medium"
    },
    {
      "id": "prob-12",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Intermediate Exam",
      "title": "Bessel Differential Equation of Order Zero: J_0(x) and Y_0(x)",
      "statement": "Obtain the series solution for Bessel's equation of order zero:<br>$$x y'' + y' + x y = 0$$",
      "solution": "<b>Step 1: Indicial equation</b><br>\nMultiply by $x$: $x^2 y'' + x y' + x^2 y = 0$.\n$p_0 = 1, q_0 = 0 \\implies r^2 = 0 \\implies r_1 = r_2 = 0$.<br><br>\n<b>Step 2: Recurrence relation</b><br>\nSubstitute $y = \\sum a_n x^{n+r}$:\n$$(n + r)^2 a_n = -a_{n-2} \\quad (a_1 = 0)$$\nOdd coefficients vanish: $a_{2m+1} = 0$.\nFor even coefficients $n = 2m$:\n$$a_{2m}(r) = \\frac{(-1)^m a_0}{2^{2m} [(1 + r/2)(2 + r/2)\\dots(m + r/2)]^2}$$\nFor $r = 0, a_0 = 1$:\n$$a_{2m}(0) = \\frac{(-1)^m}{2^{2m} (m!)^2} \\implies J_0(x) = \\sum_{m=0}^\\infty \\frac{(-1)^m}{(m!)^2} \\left(\\frac{x}{2}\\right)^{2m}$$\n<br><b>Step 3: Second solution $Y_0(x)$</b><br>\nDifferentiating with respect to $r$:\n$$\\left. \\frac{\\partial a_{2m}}{\\partial r} \\right|_{r=0} = -H_m a_{2m}(0)$$\n$$y_2(x) = J_0(x) \\ln x - \\sum_{m=1}^\\infty \\frac{(-1)^m H_m}{(m!)^2} \\left(\\frac{x}{2}\\right)^{2m}$$\nThe standard Neumann function is normalized as $Y_0(x) = \\frac{2}{\\pi}\\left[ y_2(x) + (\\gamma - \\ln 2) J_0(x) \\right]$.",
      "answer": "$J_0(x) = \\sum_{m=0}^\\infty \\frac{(-1)^m}{(m!)^2} \\left(\\frac{x}{2}\\right)^{2m}$ and $Y_0(x)$ contains logarithmic singularity $\\frac{2}{\\pi} J_0(x)\\ln x$.",
      "difficulty": "Medium"
    },
    {
      "id": "prob-13",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Intermediate Exam",
      "title": "Bessel Differential Recurrence & Integral Evaluation",
      "statement": "Prove the recurrence identity $\\frac{d}{dx}[x^\\nu J_\\nu(x)] = x^\\nu J_{\\nu-1}(x)$ and use it to evaluate $\\int x^3 J_0(x)\\,dx$.",
      "solution": "<b>Step 1: Proof of identity</b><br>\nFrom the series definition:\n$$x^\\nu J_\\nu(x) = \\sum_{m=0}^\\infty \\frac{(-1)^m}{m!\\, \\Gamma(m + \\nu + 1)} \\frac{x^{2m + 2\\nu}}{2^{2m + \\nu}}$$\nDifferentiating with respect to $x$:\n$$\\frac{d}{dx}[x^\\nu J_\\nu(x)] = \\sum_{m=0}^\\infty \\frac{(-1)^m (2m + 2\\nu)}{m!\\, \\Gamma(m + \\nu + 1)} \\frac{x^{2m + 2\\nu - 1}}{2^{2m + \\nu}}$$\nSince $2m + 2\\nu = 2(m + \\nu)$ and $\\Gamma(m + \\nu + 1) = (m + \\nu)\\Gamma(m + \\nu)$:\n$$= x^\\nu \\sum_{m=0}^\\infty \\frac{(-1)^m}{m!\\, \\Gamma(m + \\nu)} \\left(\\frac{x}{2}\\right)^{2m + \\nu - 1} = x^\\nu J_{\\nu-1}(x)$$\n<br><b>Step 2: Integration of $\\int x^3 J_0(x)\\,dx$</b><br>\nRewrite integrand as $x^2 \\cdot [x J_0(x)]$.\nFrom identity with $\\nu = 1$: $\\frac{d}{dx}[x J_1(x)] = x J_0(x) \\implies \\int x J_0(x)\\,dx = x J_1(x)$.<br>\nIntegrate by parts:\n$$u = x^2 \\implies du = 2x\\,dx, \\quad dv = x J_0(x)\\,dx \\implies v = x J_1(x)$$\n$$\\int x^3 J_0(x)\\,dx = x^2 [x J_1(x)] - \\int [x J_1(x)](2x)\\,dx = x^3 J_1(x) - 2 \\int x^2 J_1(x)\\,dx$$\nNow apply identity with $\\nu = 2$: $\\frac{d}{dx}[x^2 J_2(x)] = x^2 J_1(x) \\implies \\int x^2 J_1(x)\\,dx = x^2 J_2(x)$.<br>\n$$= x^3 J_1(x) - 2 x^2 J_2(x) + C$$\nUsing recurrence $J_2(x) = \\frac{2}{x} J_1(x) - J_0(x)$:\n$$x^3 J_1(x) - 2x^2 \\left( \\frac{2}{x} J_1(x) - J_0(x) \\right) = (x^3 - 4x) J_1(x) + 2x^2 J_0(x) + C$$",
      "answer": "$\\int x^3 J_0(x)\\,dx = x^3 J_1(x) - 2x^2 J_2(x) + C = (x^3 - 4x)J_1(x) + 2x^2 J_0(x) + C$",
      "difficulty": "Medium"
    },
    {
      "id": "prob-14",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Intermediate Exam",
      "title": "Hermite Polynomials Generating Function & Orthogonality",
      "statement": "Using the generating function $\\Phi(x, t) = e^{2xt - t^2} = \\sum_{n=0}^\\infty \\frac{H_n(x)}{n!} t^n$, prove the orthogonality relation:<br>$$\\int_{-\\infty}^\\infty e^{-x^2} H_n(x) H_m(x)\\,dx = 2^n n! \\sqrt{\\pi}\\, \\delta_{nm}$$",
      "solution": "<b>Step 1: Product of generating functions</b><br>\nConsider two generating functions with parameters $t$ and $s$:\n$$\\sum_{n=0}^\\infty \\sum_{m=0}^\\infty \\frac{t^n s^m}{n!\\, m!} \\int_{-\\infty}^\\infty e^{-x^2} H_n(x) H_m(x)\\,dx = \\int_{-\\infty}^\\infty e^{-x^2} \\Phi(x, t) \\Phi(x, s)\\,dx$$\n<br><b>Step 2: Combine exponents</b><br>\n$$\\Phi(x, t) \\Phi(x, s) = e^{2xt - t^2} e^{2xs - s^2} = e^{2x(t + s) - (t^2 + s^2)}$$\nThe integrand exponent is:\n$$-x^2 + 2x(t + s) - (t^2 + s^2) = -[x - (t + s)]^2 + (t + s)^2 - (t^2 + s^2) = -[x - (t + s)]^2 + 2ts$$\n<br><b>Step 3: Evaluate Gaussian integral</b><br>\n$$\\int_{-\\infty}^\\infty e^{-[x - (t + s)]^2 + 2ts}\\,dx = e^{2ts} \\int_{-\\infty}^\\infty e^{-u^2}\\,du = \\sqrt{\\pi} e^{2ts}$$\n<br><b>Step 4: Taylor series expansion of $e^{2ts}$</b><br>\n$$\\sqrt{\\pi} e^{2ts} = \\sqrt{\\pi} \\sum_{n=0}^\\infty \\frac{(2ts)^n}{n!} = \\sqrt{\\pi} \\sum_{n=0}^\\infty \\frac{2^n}{n!} t^n s^n$$\nNotice that there are NO terms with unequal powers $t^n s^m$ ($n \\ne m$). Hence:\n$$\\int_{-\\infty}^\\infty e^{-x^2} H_n(x) H_m(x)\\,dx = 0 \\quad \\text{for } n \\ne m$$\nFor $n = m$, equating coefficients of $\\frac{t^n s^n}{(n!)^2}$:\n$$\\frac{1}{(n!)^2} \\int_{-\\infty}^\\infty e^{-x^2} [H_n(x)]^2\\,dx = \\sqrt{\\pi} \\frac{2^n}{n!} \\implies \\int_{-\\infty}^\\infty e^{-x^2} [H_n(x)]^2\\,dx = 2^n n! \\sqrt{\\pi}$$",
      "answer": "$\\int_{-\\infty}^\\infty e^{-x^2} H_n(x) H_m(x)\\,dx = 2^n n! \\sqrt{\\pi}\\, \\delta_{nm}$",
      "difficulty": "Medium"
    },
    {
      "id": "prob-15",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Intermediate Exam",
      "title": "Sturm Comparison Theorem & Interlacing Zeros of Bessel Functions",
      "statement": "Prove using Sturm's Separation/Comparison Theorem that between any two consecutive positive zeros of $J_0(x)$, there is exactly one zero of $J_1(x)$.",
      "solution": "<b>Step 1: Recurrence relation between $J_0$ and $J_1$</b><br>\nRecall from Bessel recurrence relations:\n$$\\frac{d}{dx} J_0(x) = -J_1(x)$$\n<br><b>Step 2: Apply Rolle's Theorem</b><br>\nLet $0 < x_1 < x_2$ be two consecutive positive zeros of $J_0(x)$, so $J_0(x_1) = 0$ and $J_0(x_2) = 0$, and $J_0(x) \\ne 0$ for all $x \\in (x_1, x_2)$.<br>\nSince $J_0(x)$ is continuously differentiable on $[x_1, x_2]$, Rolle's theorem guarantees that there exists at least one point $\\xi \\in (x_1, x_2)$ such that $J_0'(\\xi) = 0$.<br>\nSince $J_0'(x) = -J_1(x)$, this means $J_1(\\xi) = 0$. Thus $J_1$ has <i>at least one</i> zero in $(x_1, x_2)$.<br><br>\n<b>Step 3: Uniqueness via Sturm Separation</b><br>\nNow consider the identity:\n$$\\frac{d}{dx}[x J_1(x)] = x J_0(x)$$\nSuppose $J_1(x)$ had two zeros $\\xi_1 < \\xi_2$ in $(x_1, x_2)$. Then applying Rolle's theorem to $g(x) = x J_1(x)$ on $[\\xi_1, \\xi_2]$ would imply $g'(\\eta) = \\eta J_0(\\eta) = 0$ for some $\\eta \\in (\\xi_1, \\xi_2) \\subset (x_1, x_2)$.<br>\nSince $\\eta > 0$, this would force $J_0(\\eta) = 0$, directly contradicting that $x_1$ and $x_2$ are <i>consecutive</i> zeros of $J_0(x)$!<br><br>\n<b>Conclusion:</b> There is <b>strictly one</b> zero of $J_1(x)$ between any two consecutive zeros of $J_0(x)$. The zeros strictly interlace: $0 < j_{0, 1} < j_{1, 1} < j_{0, 2} < j_{1, 2} < \\dots$.",
      "answer": "Proved: zeros of $J_0(x)$ and $J_1(x)$ strictly interlace.",
      "difficulty": "Medium"
    },
    {
      "id": "prob-16",
      "tier": 2,
      "difficultyLabel": "Tier 2 • Intermediate Exam",
      "title": "Solvability Condition via the Fredholm Alternative",
      "statement": "Determine the exact condition on the function $h(x)$ for the boundary value problem to possess a solution:<br>$$y'' + \\pi^2 y = h(x), \\quad y(0) = 0, \\quad y(1) = 0$$",
      "solution": "<b>Step 1: Check homogeneous boundary value problem</b><br>\n$$y_h'' + \\pi^2 y_h = 0 \\implies y_h(x) = c_1 \\cos(\\pi x) + c_2 \\sin(\\pi x)$$\nBoundary conditions:\n$$y_h(0) = c_1 = 0 \\implies y_h(x) = c_2 \\sin(\\pi x)$$\n$$y_h(1) = c_2 \\sin(\\pi) = 0 \\quad (\\text{satisfied for any } c_2)$$\nThe homogeneous problem has non-trivial solution $\\phi(x) = \\sin(\\pi x)$.<br><br>\n<b>Step 2: Self-adjointness of operator</b><br>\nThe operator $L[y] = y'' + \\pi^2 y$ with Dirichlet conditions $y(0) = y(1) = 0$ is formally self-adjoint:\n$$\\int_0^1 (u L[v] - v L[u])\\,dx = [u v' - v u']_0^1 = 0$$\n<br><b>Step 3: Apply the Fredholm Alternative (Case II)</b><br>\nBy Theorem 8.1, the nonhomogeneous problem has a solution if and only if $h(x)$ is orthogonal to the null space of the adjoint operator:\n$$\\int_0^1 h(x) \\phi(x)\\,dx = 0 \\implies \\int_0^1 h(x) \\sin(\\pi x)\\,dx = 0$$\nIf this integral is zero, an infinite family of solutions exists ($y(x) = y_p(x) + c \\sin(\\pi x)$). If non-zero, NO solution exists.",
      "answer": "Solvability condition: $\\int_0^1 h(x) \\sin(\\pi x)\\,dx = 0$.",
      "difficulty": "Medium"
    },
    {
      "id": "prob-17",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Matrix Riccati Transformation & Hamiltonian Linear System",
      "statement": "Convert the nonlinear matrix Riccati differential equation $\\mathbf{R}' = \\mathbf{B} - \\mathbf{R} \\mathbf{D} \\mathbf{R}$ into an equivalent $2n \\times 2n$ linear Hamiltonian dynamical system $\\vec{z}' = \\mathbf{H}\\vec{z}$.",
      "solution": "<b>Step 1: Fractional Linear Transformation</b><br>\nLet $\\mathbf{R}(t) = \\mathbf{X}(t) \\mathbf{Y}^{-1}(t)$ where $\\mathbf{X}(t), \\mathbf{Y}(t) \\in \\mathbb{R}^{n \\times n}$ and $\\det \\mathbf{Y}(t) \\ne 0$.<br><br>\n<b>Step 2: Differentiate the quotient</b><br>\nUsing the matrix product rule and derivative of inverse $\\frac{d}{dt}[\\mathbf{Y}^{-1}] = -\\mathbf{Y}^{-1} \\mathbf{Y}' \\mathbf{Y}^{-1}$:\n$$\\mathbf{R}' = \\mathbf{X}' \\mathbf{Y}^{-1} + \\mathbf{X} (\\mathbf{Y}^{-1})' = \\mathbf{X}' \\mathbf{Y}^{-1} - \\mathbf{X} \\mathbf{Y}^{-1} \\mathbf{Y}' \\mathbf{Y}^{-1} = (\\mathbf{X}' - \\mathbf{R} \\mathbf{Y}') \\mathbf{Y}^{-1}$$\n<br><b>Step 3: Equate to Riccati expression</b><br>\n$$\\mathbf{R}' = \\mathbf{B} - \\mathbf{R} \\mathbf{D} \\mathbf{R} = \\mathbf{B} - \\mathbf{R} \\mathbf{D} \\mathbf{X} \\mathbf{Y}^{-1}$$\nEquating both expressions and post-multiplying by $\\mathbf{Y}$:\n$$\\mathbf{X}' - \\mathbf{R} \\mathbf{Y}' = \\mathbf{B} \\mathbf{Y} - \\mathbf{R} \\mathbf{D} \\mathbf{X}$$\nRearranging terms by isolating $\\mathbf{R}$:\n$$\\mathbf{X}' - \\mathbf{B} \\mathbf{Y} = \\mathbf{R} (\\mathbf{Y}' - \\mathbf{D} \\mathbf{X})$$\n<br><b>Step 4: Decouple into Linear System</b><br>\nThis identity holds identically if both parenthetical sides vanish:\n$$\\mathbf{X}' = \\mathbf{B} \\mathbf{Y}, \\quad \\mathbf{Y}' = \\mathbf{D} \\mathbf{X}$$\nStacking state vectors $\\vec{z} = \\begin{pmatrix} \\mathbf{X} \\\\ \\mathbf{Y} \\end{pmatrix}$:\n$$\\frac{d}{dt} \\begin{pmatrix} \\mathbf{X} \\\\ \\mathbf{Y} \\end{pmatrix} = \\begin{pmatrix} \\mathbf{0} & \\mathbf{B} \\\\ \\mathbf{D} & \\mathbf{0} \\end{pmatrix} \\begin{pmatrix} \\mathbf{X} \\\\ \\mathbf{Y} \\end{pmatrix}$$\nThis establishes that the solution of the nonlinear Riccati equation is $\\mathbf{R}(t) = \\mathbf{X}(t)\\mathbf{Y}^{-1}(t)$ generated by the linear flow map $e^{\\mathbf{H}t}$.",
      "answer": "$\\mathbf{R}(t) = \\mathbf{X}(t)\\mathbf{Y}(t)^{-1}$ where $\\frac{d}{dt}\\begin{pmatrix} \\mathbf{X} \\\\ \\mathbf{Y} \\end{pmatrix} = \\begin{pmatrix} \\mathbf{0} & \\mathbf{B} \\\\ \\mathbf{D} & \\mathbf{0} \\end{pmatrix} \\begin{pmatrix} \\mathbf{X} \\\\ \\mathbf{Y} \\end{pmatrix}$.",
      "difficulty": "Hard"
    },
    {
      "id": "prob-18",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Jordan Canonical Form Derivation for Highly Defective 3x3 System",
      "statement": "Solve the defective system $\\vec{x}' = \\mathbf{A}\\vec{x}$ where $\\mathbf{A} = \\begin{pmatrix} 3 & 1 & 0 \\\\ 0 & 3 & 1 \\\\ 0 & 0 & 3 \\end{pmatrix}$ using generalized eigenvector chains.",
      "solution": "<b>Step 1: Spectral Analysis</b><br>\nThe characteristic polynomial is $(\\lambda - 3)^3 = 0 \\implies \\lambda = 3$ with algebraic multiplicity $m_a = 3$.\nThe null space $(\\mathbf{A} - 3\\mathbf{I})\\vec{v} = \\vec{0}$ has rank 2, so the geometric multiplicity is $m_g = 3 - 2 = 1$. The matrix is defective with a single Jordan block of size 3.<br><br>\n<b>Step 2: Construct the Jordan Chain</b><br>\nWe seek a generalized eigenvector $\\vec{v}_3$ of rank 3:\n$$(\\mathbf{A} - 3\\mathbf{I})^3 = \\mathbf{0}, \\quad (\\mathbf{A} - 3\\mathbf{I})^2 \\vec{v}_3 \\ne \\vec{0}$$\n$$\\mathbf{A} - 3\\mathbf{I} = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 1 \\\\ 0 & 0 & 0 \\end{pmatrix}, \\quad (\\mathbf{A} - 3\\mathbf{I})^2 = \\begin{pmatrix} 0 & 0 & 1 \\\\ 0 & 0 & 0 \\\\ 0 & 0 & 0 \\end{pmatrix}$$\nChoose $\\vec{v}_3 = \\begin{pmatrix} 0 \\\\ 0 \\\\ 1 \\end{pmatrix}$.\nThen:\n$$\\vec{v}_2 = (\\mathbf{A} - 3\\mathbf{I}) \\vec{v}_3 = \\begin{pmatrix} 0 \\\\ 1 \\\\ 0 \\end{pmatrix}$$\n$$\\vec{v}_1 = (\\mathbf{A} - 3\\mathbf{I}) \\vec{v}_2 = \\begin{pmatrix} 1 \\\\ 0 \\\\ 0 \\end{pmatrix} \\quad (\\text{genuine eigenvector})$$\n<br><b>Step 3: Construct Three Linearly Independent Solutions</b><br>\n$$\\begin{aligned}\n\\vec{x}_1(t) &= e^{3t} \\vec{v}_1 = e^{3t} \\begin{pmatrix} 1 \\\\ 0 \\\\ 0 \\end{pmatrix} \\\\\n\\vec{x}_2(t) &= e^{3t} (t \\vec{v}_1 + \\vec{v}_2) = e^{3t} \\begin{pmatrix} t \\\\ 1 \\\\ 0 \\end{pmatrix} \\\\\n\\vec{x}_3(t) &= e^{3t} \\left( \\frac{t^2}{2} \\vec{v}_1 + t \\vec{v}_2 + \\vec{v}_3 \\right) = e^{3t} \\begin{pmatrix} t^2/2 \\\\ t \\\\ 1 \\end{pmatrix}\n\\end{aligned}$$\n<br><b>Step 4: General Solution</b><br>\n$$\\vec{x}(t) = e^{3t} \\begin{pmatrix} c_1 + c_2 t + c_3 \\frac{t^2}{2} \\\\ c_2 + c_3 t \\\\ c_3 \\end{pmatrix}$$",
      "answer": "$\\vec{x}(t) = e^{3t} \\begin{pmatrix} c_1 + c_2 t + c_3 \\frac{t^2}{2} \\\\ c_2 + c_3 t \\\\ c_3 \\end{pmatrix}$",
      "difficulty": "Hard"
    },
    {
      "id": "prob-19",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Complete Legendre Series Expansion & Parseval's Identity",
      "statement": "Expand $f(x) = x(1 - x^2)$ in terms of Legendre polynomials on $[-1, 1]$ and verify Parseval's identity.",
      "solution": "<b>Step 1: Algebraic decomposition</b><br>\n$f(x) = x - x^3$. We express $f(x)$ as a linear combination of Legendre polynomials:\n$$P_1(x) = x \\implies x = P_1(x)$$\n$$P_3(x) = \\frac{1}{2}(5x^3 - 3x) \\implies 5x^3 = 2P_3(x) + 3x = 2P_3(x) + 3P_1(x) \\implies x^3 = \\frac{2}{5}P_3(x) + \\frac{3}{5}P_1(x)$$\nSubstituting $x^3$:\n$$f(x) = P_1(x) - \\left( \\frac{2}{5}P_3(x) + \\frac{3}{5}P_1(x) \\right) = \\frac{2}{5}P_1(x) - \\frac{2}{5}P_3(x)$$\nAll other coefficients $c_n = 0$.<br><br>\n<b>Step 2: Parseval's Identity Verification</b><br>\nLHS: Directly compute $\\int_{-1}^1 [f(x)]^2\\,dx$:\n$$[f(x)]^2 = x^2(1 - x^2)^2 = x^2(1 - 2x^2 + x^4) = x^2 - 2x^4 + x^6$$\n$$\\int_{-1}^1 (x^2 - 2x^4 + x^6)\\,dx = 2 \\left[ \\frac{1}{3} - \\frac{2}{5} + \\frac{1}{7} \\right] = 2 \\left( \\frac{35 - 42 + 15}{105} \\right) = 2 \\left(\\frac{8}{105}\\right) = \\frac{16}{105}$$\nRHS: Compute $\\sum c_n^2 \\|P_n\\|^2$ where $\\|P_n\\|^2 = \\frac{2}{2n + 1}$:\n$$c_1^2 \\|P_1\\|^2 + c_3^2 \\|P_3\\|^2 = \\left(\\frac{2}{5}\\right)^2 \\left(\\frac{2}{3}\\right) + \\left(-\\frac{2}{5}\\right)^2 \\left(\\frac{2}{7}\\right)$$\n$$= \\frac{4}{25} \\left( \\frac{2}{3} + \\frac{2}{7} \\right) = \\frac{4}{25} \\left( \\frac{20}{21} \\right) = \\frac{80}{525} = \\frac{16}{105}$$\nLHS = RHS = $\\frac{16}{105}$. Parseval's identity holds with 100% precision!",
      "answer": "$f(x) = \\frac{2}{5}P_1(x) - \\frac{2}{5}P_3(x)$ and $\\|f\\|^2 = \\sum c_n^2 \\|P_n\\|^2 = \\frac{16}{105}$.",
      "difficulty": "Hard"
    },
    {
      "id": "prob-20",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Inhomogeneous Bessel Equation via Lommel's Integrals",
      "statement": "Solve the inhomogeneous Bessel equation of order zero:<br>$$x^2 y'' + x y' + x^2 y = x$$<br>using Variation of Parameters.",
      "solution": "<b>Step 1: Normalized standard form</b><br>\nDivide by $x^2$:\n$$y'' + \\frac{1}{x} y' + y = \\frac{1}{x}$$\nThe homogeneous solutions are $y_1(x) = J_0(x)$ and $y_2(x) = Y_0(x)$.<br><br>\n<b>Step 2: Wronskian of Bessel functions</b><br>\nAbel's identity gives:\n$$W(J_0, Y_0)(x) = \\frac{2}{\\pi x}$$\n<br><b>Step 3: Variation of Parameters formulas</b><br>\n$$u_1'(x) = -\\frac{y_2(x) g(x)}{W(x)} = -\\frac{Y_0(x) (1/x)}{2/(\\pi x)} = -\\frac{\\pi}{2} Y_0(x)$$\n$$u_2'(x) = \\frac{y_1(x) g(x)}{W(x)} = \\frac{J_0(x) (1/x)}{2/(\\pi x)} = \\frac{\\pi}{2} J_0(x)$$\n<br><b>Step 4: Particular solution</b><br>\n$$y_p(x) = -\\frac{\\pi}{2} J_0(x) \\int_0^x Y_0(s)\\,ds + \\frac{\\pi}{2} Y_0(x) \\int_0^x J_0(s)\\,ds$$\nThis is the celebrated Struve function relation: $y_p(x) = \\frac{\\pi}{2} \\mathbf{H}_0(x)$.",
      "answer": "$y(x) = c_1 J_0(x) + c_2 Y_0(x) + \\frac{\\pi}{2}\\left[ Y_0(x)\\int_0^x J_0(s)ds - J_0(x)\\int_0^x Y_0(s)ds \\right]$",
      "difficulty": "Hard"
    },
    {
      "id": "prob-21",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Associated Laguerre Transformation of Hydrogen Radial Schrödinger Equation",
      "statement": "Transform the radial hydrogenic Schrödinger equation $\\frac{d^2 R}{dr^2} + \\frac{2}{r} \\frac{dR}{dr} + \\left[ \\frac{2Z}{r} - \\frac{l(l+1)}{r^2} - \\kappa^2 \\right] R = 0$ into the confluent hypergeometric Associated Laguerre equation.",
      "solution": "<b>Step 1: Asymptotic Behavior</b><br>\nAs $r \\to \\infty$: $R'' - \\kappa^2 R \\approx 0 \\implies R(r) \\sim e^{-\\kappa r}$.<br>\nAs $r \\to 0$: $R'' + \\frac{2}{r} R' - \\frac{l(l+1)}{r^2} R \\approx 0 \\implies R(r) \\sim r^l$.<br><br>\n<b>Step 2: Dimensionless variable and ansatz</b><br>\nDefine dimensionless coordinate $\\rho = 2\\kappa r$.<br>\nLet $R(\\rho) = \\rho^l e^{-\\rho/2} v(\\rho)$.<br><br>\n<b>Step 3: Derivatives of the ansatz</b><br>\nCompute $R'$ and $R''$ in terms of $\\rho$ and substitute into the radial equation. After factorizing $\\rho^l e^{-\\rho/2}$, the equation reduces to:\n$$\\rho \\frac{d^2 v}{d\\rho^2} + [2(l + 1) - \\rho] \\frac{dv}{d\\rho} + (n - l - 1) v = 0$$\nwhere $n = \\frac{Z}{\\kappa}$ is the principal quantum number.<br><br>\n<b>Step 4: Associated Laguerre Polynomials</b><br>\nLet $k = 2l + 1$ and $p = n - l - 1 \\ge 0$. The equation becomes:\n$$\\rho v'' + (k + 1 - \\rho) v' + p v = 0$$\nwhich is precisely the <b>Associated Laguerre differential equation</b>!\nThe solutions are $v(\\rho) = L_{n - l - 1}^{2l + 1}(\\rho)$, proving that the bound state energy levels are quantized:\n$$E_n = -\\frac{\\hbar^2 \\kappa^2}{2\\mu} = -\\frac{\\mu Z^2 e^4}{2\\hbar^2 n^2}, \\quad n = l + 1, l + 2, \\dots$$",
      "answer": "$\\rho v'' + (2l + 2 - \\rho)v' + (n - l - 1)v = 0$ with solution $v(\\rho) = L_{n-l-1}^{2l+1}(2\\kappa r)$.",
      "difficulty": "Hard"
    },
    {
      "id": "prob-22",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Periodic Sturm-Liouville Problem & Double Spectral Degeneracy",
      "statement": "Establish the self-adjointness, non-negative spectrum, and double degeneracy for the periodic Sturm-Liouville problem:<br>$$y'' + \\lambda y = 0, \\quad y(-\\pi) = y(\\pi), \\quad y'(-\\pi) = y'(\\pi)$$",
      "solution": "<b>Step 1: Self-Adjointness via Green's Formula</b><br>\nFor $L[y] = -y''$:\n$$\\int_{-\\pi}^\\pi (u L[v] - v L[u])\\,dx = \\left[ -u v' + v u' \\right]_{-\\pi}^\\pi = [-u(\\pi)v'(\\pi) + v(\\pi)u'(\\pi)] - [-u(-\\pi)v'(-\\pi) + v(-\\pi)u'(-\\pi)]$$\nUsing periodic conditions $u(-\\pi) = u(\\pi)$ and $u'(-\\pi) = u'(\\pi)$:\n$$= [-u(\\pi)v'(\\pi) + v(\\pi)u'(\\pi)] - [-u(\\pi)v'(\\pi) + v(\\pi)u'(\\pi)] = 0$$\nThe periodic boundary conditions make the boundary term vanish. Hence $L$ is <b>self-adjoint</b>.<br><br>\n<b>Step 2: Non-negative eigenvalues ($\\lambda \\ge 0$)</b><br>\nMultiply by $y$ and integrate by parts:\n$$\\lambda \\int_{-\\pi}^\\pi y^2\\,dx = \\int_{-\\pi}^\\pi (y')^2\\,dx - [y y']_{-\\pi}^\\pi = \\int_{-\\pi}^\\pi (y')^2\\,dx \\ge 0$$\nHence $\\lambda \\ge 0$.<br><br>\n<b>Step 3: Eigenvalues & Degeneracy</b><br>\nFor $\\lambda_0 = 0$: $y_0(x) = 1$ (non-degenerate, dimension 1).<br>\nFor $\\lambda_n = n^2 > 0$ ($n = 1, 2, 3, \\dots$):\nBoth $y_{n, 1}(x) = \\cos(nx)$ and $y_{n, 2}(x) = \\sin(nx)$ satisfy the periodic boundary conditions!\nThus every eigenvalue $\\lambda_n = n^2$ has <b>multiplicity 2</b> (doubly degenerate eigenspace spanned by $\\{\\cos nx, \\sin nx\\}$), generating the classical full Fourier series!",
      "answer": "$\\lambda_0 = 0$ (simple), $\\lambda_n = n^2$ ($n \\ge 1$, doubly degenerate with basis $\\{\\cos nx, \\sin nx\\}$).",
      "difficulty": "Hard"
    },
    {
      "id": "prob-23",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Bilinear Mercer Eigenfunction Expansion of Green's Function",
      "statement": "Prove the bilinear eigenfunction expansion for the Green's function of a regular Sturm-Liouville problem:<br>$$G(x, \\xi) = \\sum_{n=1}^\\infty \\frac{\\phi_n(x) \\phi_n(\\xi)}{\\lambda_n}$$",
      "solution": "<b>Step 1: Expand Green's function in orthonormal eigenfunctions</b><br>\nLet $\\{\\phi_n(x)\\}$ be the complete orthonormal eigenfunctions of $L[\\phi_n] = \\lambda_n w(x) \\phi_n$ with separated boundary conditions. For any fixed $\\xi \\in (a, b)$, $G(x, \\xi)$ satisfies the boundary conditions in $x$. Expand $G(x, \\xi)$ in terms of $\\phi_n(x)$:\n$$G(x, \\xi) = \\sum_{n=1}^\\infty c_n(\\xi) \\phi_n(x)$$\n<br><b>Step 2: Determine expansion coefficients $c_n(\\xi)$</b><br>\nBy orthonormality $\\int_a^b \\phi_n(x) \\phi_m(x) w(x)\\,dx = \\delta_{nm}$:\n$$c_n(\\xi) = \\int_a^b G(x, \\xi) \\phi_n(x) w(x)\\,dx$$\n<br><b>Step 3: Exploit self-adjointness and eigenvalue equation</b><br>\nSince $\\phi_n(x) = \\frac{1}{\\lambda_n w(x)} L[\\phi_n](x)$:\n$$c_n(\\xi) = \\frac{1}{\\lambda_n} \\int_a^b G(x, \\xi) L[\\phi_n](x)\\,dx$$\nUsing Green's formula $\\int_a^b (u L[v] - v L[u])\\,dx = 0$:\n$$c_n(\\xi) = \\frac{1}{\\lambda_n} \\int_a^b \\phi_n(x) L_x[G(x, \\xi)]\\,dx$$\nSince $L_x[G(x, \\xi)] = \\delta(x - \\xi)$:\n$$c_n(\\xi) = \\frac{1}{\\lambda_n} \\int_a^b \\phi_n(x) \\delta(x - \\xi)\\,dx = \\frac{\\phi_n(\\xi)}{\\lambda_n}$$\n<br><b>Step 4: Substitute $c_n(\\xi)$ back</b><br>\n$$G(x, \\xi) = \\sum_{n=1}^\\infty \\frac{\\phi_n(x) \\phi_n(\\xi)}{\\lambda_n}$$\nThis Mercer series proves the exact symmetry $G(x, \\xi) = G(\\xi, x)$ and convergence in $L^2$.",
      "answer": "$G(x, \\xi) = \\sum_{n=1}^\\infty \\frac{\\phi_n(x) \\phi_n(\\xi)}{\\lambda_n}$ (Mercer's Bilinear Expansion).",
      "difficulty": "Hard"
    },
    {
      "id": "prob-24",
      "tier": 3,
      "difficultyLabel": "Tier 3 • Honors Challenge",
      "title": "Modified Generalized Green's Function for Semi-Definite Neumann Problems",
      "statement": "Construct the modified (generalized) Green's function for the pure Neumann boundary value problem:<br>$$-y'' = f(x), \\quad y'(0) = 0, \\quad y'(1) = 0$$<br>subject to the Fredholm solvability condition $\\int_0^1 f(x)\\,dx = 0$.",
      "solution": "<b>Step 1: Check Homogeneous Neumann Problem</b><br>\n$-y_h'' = 0 \\implies y_h(x) = c_1 x + c_2$.\n$y_h'(0) = c_1 = 0 \\implies y_h(x) = c_2$. $y_h'(1) = 0$ holds identically.\nThus $\\phi(x) = 1$ is a non-trivial homogeneous solution (normalized: $\\phi_0(x) = 1$).\nThe standard Green's function does NOT exist because $\\lambda = 0$ is an eigenvalue!<br><br>\n<b>Step 2: Modified Green's Function Definition</b><br>\nThe modified Green's function $G_m(x, \\xi)$ satisfies:\n$$-G_m''(x, \\xi) = \\delta(x - \\xi) - 1, \\quad G_m'(0, \\xi) = 0, \\quad G_m'(1, \\xi) = 0, \\quad \\int_0^1 G_m(x, \\xi)\\,dx = 0$$\nNotice that integrating both sides over $[0, 1]$ gives $-(G_m'(1) - G_m'(0)) = 1 - 1 = 0$, guaranteeing consistency!<br><br>\n<b>Step 3: Integrate piecewise</b><br>\nFor $x < \\xi$: $-G_m'' = -1 \\implies G_m'' = 1 \\implies G_m'(x) = x + A$.\nSince $G_m'(0) = 0 \\implies A = 0 \\implies G_m'(x) = x$.\nIntegrating: $G_m(x) = \\frac{x^2}{2} + C_1$.<br>\nFor $x > \\xi$: $G_m'(x) = x - 1$ to satisfy $G_m'(1) = 0$.\nIntegrating: $G_m(x) = \\frac{x^2}{2} - x + C_2$.<br><br>\n<b>Step 4: Jump and Continuity Conditions</b><br>\nDerivative jump: $\\left. G_m' \\right|_{\\xi^+} - \\left. G_m' \\right|_{\\xi^-} = (\\xi - 1) - \\xi = -1$. (Satisfied identically!)<br>\nContinuity at $x = \\xi$: $\\frac{\\xi^2}{2} + C_1 = \\frac{\\xi^2}{2} - \\xi + C_2 \\implies C_1 = C_2 - \\xi$.<br>\nSymmetric form:\n$$G_m(x, \\xi) = \\frac{x^2 + \\xi^2}{2} - \\max(x, \\xi) + C$$\nApplying normalization $\\int_0^1 G_m(x, \\xi)\\,dx = 0$ fixes $C = \\frac{1}{3}$:\n$$G_m(x, \\xi) = \\frac{x^2 + \\xi^2}{2} - \\max(x, \\xi) + \\frac{1}{3}$$\nFor any load with $\\int_0^1 f(x)\\,dx = 0$, the unique zero-mean solution is $y(x) = \\int_0^1 G_m(x, \\xi) f(\\xi)\\,d\\xi$.",
      "answer": "$G_m(x, \\xi) = \\frac{x^2 + \\xi^2}{2} - \\max(x, \\xi) + \\frac{1}{3}$.",
      "difficulty": "Hard"
    }
  ]
};
window.BOOK_DATA = window.COURSE_DATA;
