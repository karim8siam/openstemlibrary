# Unit 5 & Unit 6 Builder for Classical Mechanics & Special Relativity
import json

u5 = {
    "unitNumber": 5,
    "number": 5,
    "title": "Hamilton's Equations of Motion & Least Action",
    "subtitle": "Phase Space, Legendre Transformation, Canonical Equations, Energy Conservation & Maupertuis' Principle",
    "description": "Rigorous transition from configuration space to 2n-dimensional phase space, Legendre transformation from Lagrangian to Hamiltonian, derivation of Hamilton's 2n first-order canonical equations, physical meaning of H as total energy, modified Hamilton's principle, Maupertuis' principle of least action, and Hamiltonian dynamics of electromagnetic charged particles.",
    "topics": [
        "Configuration Space vs Phase Space",
        "Legendre Transformation L(q, q̇) to H(q, p)",
        "Derivation of Hamilton's Canonical Equations",
        "Physical Significance of H & Energy Conservation",
        "Modified Hamilton's Variational Principle",
        "Maupertuis' Principle of Least Action",
        "Canonical Phase Portraits & Charged Particle in EM Field"
    ],
    "sections": [
        {
            "id": "u5-sec1",
            "title": "Transition from Configuration Space to Phase Space",
            "content": """
<h4>1. Limitations of the Lagrangian Framework</h4>
In the Lagrangian formulation, a dynamical system of $n$ degrees of freedom is described in an $n$-dimensional <strong>configuration space</strong> spanned by generalized coordinates $(q_1, \\dots, q_n)$. The equations of motion:
<div class="math-display">$$\\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial L}{\\partial q_j} = 0, \\quad j = 1, \\dots, n$$</div>
constitute a set of $n$ coupled <strong>second-order differential equations</strong>. Specifying a unique dynamical trajectory requires $2n$ initial boundary conditions: initial positions $q_j(0)$ and initial velocities $\\dot{q}_j(0)$. However, generalized velocities $\\dot{q}_j$ are not independent state variables—they are geometric tangents to the trajectory.

<h4>2. The 2n-Dimensional Phase Space</h4>
In 1835, Sir William Rowan Hamilton developed a symmetric reformulation by replacing the $n$ generalized velocities $\\dot{q}_j$ with $n$ <strong>canonical conjugate momenta</strong> $p_j$:
<div class="math-display">$$p_j = \\frac{\\partial L}{\\partial \\dot{q}_j}(q, \\dot{q}, t)$$</div>
The state of the system is now mapped as a single point in a <strong>$2n$-dimensional phase space</strong> spanned by $2n$ independent coordinates:
<div class="math-display">$$(q_1, \\dots, q_n; p_1, \\dots, p_n) \\in \\mathbb{R}^{2n}$$</div>
Instead of $n$ second-order differential equations, Hamiltonian dynamics governs motion through a system of <strong>$2n$ first-order differential equations</strong>, displaying complete mathematical symmetry between positions and momenta.
"""
        },
        {
            "id": "u5-sec2",
            "title": "The Legendre Transformation & Derivation of Hamilton's Equations",
            "content": """
<h4>1. The Mathematical Legendre Transformation</h4>
Consider the total differential of the Lagrangian $L(q, \\dot{q}, t)$:
<div class="math-display">$$dL = \\sum_{j=1}^n \\frac{\\partial L}{\\partial q_j} dq_j + \\sum_{j=1}^n \\frac{\\partial L}{\\partial \\dot{q}_j} d\\dot{q}_j + \\frac{\\partial L}{\\partial t} dt = \\sum_{j=1}^n \\dot{p}_j dq_j + \\sum_{j=1}^n p_j d\\dot{q}_j + \\frac{\\partial L}{\\partial t} dt$$</div>
where we used $p_j = \\frac{\\partial L}{\\partial \\dot{q}_j}$ and Lagrange's equations $\\dot{p}_j = \\frac{\\partial L}{\\partial q_j}$.
To transform the active variable from $\\dot{q}_j$ to $p_j$, we perform a <strong>Legendre transformation</strong> by subtracting the differential $d\\left( \\sum_{j=1}^n p_j \\dot{q}_j \\right)$:
<div class="math-display">$$d\\left( \\sum_{j=1}^n p_j \\dot{q}_j - L \\right) = \\sum_{j=1}^n \\dot{q}_j dp_j + \\sum_{j=1}^n p_j d\\dot{q}_j - dL = \\sum_{j=1}^n \\dot{q}_j dp_j - \\sum_{j=1}^n \\dot{p}_j dq_j - \\frac{\\partial L}{\\partial t} dt$$</div>

<h4>2. Definition of the Hamiltonian Function $H$</h4>
We define the <strong>Hamiltonian function</strong> $H(q, p, t)$ by the Legendre transform:
<div class="math-display">$$H(q, p, t) = \\sum_{j=1}^n p_j \\dot{q}_j - L(q, \\dot{q}, t)$$</div>
where all occurrences of $\\dot{q}_j$ must be inverted algebraically in terms of $q, p, t$. The exact total differential of $H(q, p, t)$ as a function of its natural canonical variables is:
<div class="math-display">$$dH = \\sum_{j=1}^n \\frac{\\partial H}{\\partial q_j} dq_j + \\sum_{j=1}^n \\frac{\\partial H}{\\partial p_j} dp_j + \\frac{\\partial H}{\\partial t} dt$$</div>

<h4>3. Hamilton's Canonical Equations of Motion</h4>
Equating coefficients of the independent differentials $dq_j, dp_j, dt$:
<div class="math-display">$$\\dot{q}_j = \\frac{\\partial H}{\\partial p_j}, \\quad \\dot{p}_j = -\\frac{\\partial H}{\\partial q_j}, \\quad j = 1, 2, \\dots, n$$</div>
together with the partial time derivative identity:
<div class="math-display">$$\\frac{\\partial H}{\\partial t} = -\\frac{\\partial L}{\\partial t}$$</div>
<p>These $2n$ coupled equations are known as <strong>Hamilton's Canonical Equations of Motion</strong>.</p>
"""
        },
        {
            "id": "u5-sec3",
            "title": "Physical Meaning of the Hamiltonian & Energy Conservation",
            "content": """
<h4>1. Total Time Derivative of the Hamiltonian</h4>
Differentiating $H(q(t), p(t), t)$ along a physical dynamical trajectory:
<div class="math-display">$$\\frac{dH}{dt} = \\sum_{j=1}^n \\left( \\frac{\\partial H}{\\partial q_j} \\dot{q}_j + \\frac{\\partial H}{\\partial p_j} \\dot{p}_j \\right) + \\frac{\\partial H}{\\partial t}$$</div>
Substituting Hamilton's canonical equations:
<div class="math-display">$$\\frac{dH}{dt} = \\sum_{j=1}^n \\left( -\\dot{p}_j \\dot{q}_j + \\dot{q}_j \\dot{p}_j \\right) + \\frac{\\partial H}{\\partial t} = \\frac{\\partial H}{\\partial t} = -\\frac{\\partial L}{\\partial t}$$</div>
<p><strong>Conservation Theorem:</strong> If the Hamiltonian does not depend explicitly on time ($\\frac{\\partial H}{\\partial t} = 0$), then the Hamiltonian is a strict <strong>constant of motion</strong>: $H(q, p) = E = \\text{constant}$.</p>

<h4>2. Condition Under Which $H$ Equals Total Mechanical Energy ($H = T + V$)</h4>
Recall Euler's theorem for homogeneous functions. The kinetic energy $T$ is generally expressed as:
<div class="math-display">$$T = T_2 + T_1 + T_0$$</div>
where $T_2 = \\frac{1}{2} \\sum_{j,k} m_{jk}(q) \\dot{q}_j \\dot{q}_k$ (quadratic in velocities), $T_1 = \\sum_j a_j(q) \\dot{q}_j$ (linear), and $T_0$ is independent of $\\dot{q}$.
The canonical momenta are $p_j = \\frac{\\partial T_2}{\\partial \\dot{q}_j} + a_j$. Then:
<div class="math-display">$$\\sum_{j=1}^n p_j \\dot{q}_j = 2 T_2 + T_1$$</div>
The Hamiltonian is:
<div class="math-display">$$H = \\sum_{j=1}^n p_j \\dot{q}_j - (T - V) = (2T_2 + T_1) - (T_2 + T_1 + T_0 - V) = T_2 - T_0 + V$$</div>
Therefore, $H = T + V = E$ if and only if two conditions are met simultaneously:
<ol>
  <li>The transformation equations $\\vec{r}_i = \\vec{r}_i(q)$ are <strong>scleronomic</strong> (no explicit time dependence $\\frac{\\partial \\vec{r}_i}{\\partial t} = 0$), which makes $T_1 = 0$ and $T_0 = 0$.</li>
  <li>The potential energy $V = V(q)$ is independent of velocities $\\dot{q}$.</li>
</ol>
"""
        },
        {
            "id": "u5-sec4",
            "title": "Variational Principles: Modified Hamilton's Principle & Least Action",
            "content": """
<h4>1. Modified Hamilton's Principle in Phase Space</h4>
In configuration space, Hamilton's principle varies coordinates $q_j(t)$ with $\\delta q_j(t_1) = \\delta q_j(t_2) = 0$. In phase space, both $q_j(t)$ and $p_j(t)$ are treated as $2n$ independent path variables. Substituting $L = \\sum p_j \\dot{q}_j - H(q, p, t)$:
<div class="math-display">$$\\delta \\int_{t_1}^{t_2} \\left( \\sum_{j=1}^n p_j \\dot{q}_j - H(q, p, t) \\right) dt = 0$$</div>
Carrying out independent variations $\\delta q_j$ and $\\delta p_j$:
<div class="math-display">$$\\int_{t_1}^{t_2} \\sum_{j=1}^n \\left[ \\delta p_j \\dot{q}_j + p_j \\frac{d}{dt}(\\delta q_j) - \\frac{\\partial H}{\\partial q_j} \\delta q_j - \\frac{\\partial H}{\\partial p_j} \\delta p_j \\right] dt = 0$$</div>
Integrating $p_j \\frac{d}{dt}(\\delta q_j)$ by parts with fixed coordinate endpoints $\\delta q_j(t_1) = \\delta q_j(t_2) = 0$ (note that endpoint variations $\\delta p_j$ are unconstrained):
<div class="math-display">$$\\int_{t_1}^{t_2} \\sum_{j=1}^n \\left[ \\left( \\dot{q}_j - \\frac{\\partial H}{\\partial p_j} \\right) \\delta p_j - \\left( \\dot{p}_j + \\frac{\\partial H}{\\partial q_j} \\right) \\delta q_j \\right] dt = 0$$</div>
Because $\\delta q_j$ and $\\delta p_j$ are completely independent, their coefficients must vanish individually, reproducing Hamilton's equations.

<h4>2. Maupertuis' Principle of Least Action</h4>
For conservative systems ($H = E = \\text{const}$), Pierre Louis Maupertuis (1744) formulated an abbreviated variational principle where time is not held fixed at endpoints ($\\Delta t \\neq 0$). The <strong>abbreviated action</strong> $S_0$ is defined as:
<div class="math-display">$$S_0 = \\int_{q^{(1)}}^{q^{(2)}} \\sum_{j=1}^n p_j dq_j = \\int_{t_1}^{t_2} 2 T dt$$</div>
<p><strong>Maupertuis' Principle:</strong> For physical paths with constant total energy $E$, the varied path renders the abbreviated action stationary:</p>
<div class="math-display">$$\\Delta S_0 = \\Delta \\int \\sum_{j=1}^n p_j dq_j = 0$$</div>
For a single particle in a potential $V(\\vec{r})$ with mass $m$, $p = \\sqrt{2m(E - V)}$. The principle becomes:
<div class="math-display">$$\\delta \\int \\sqrt{2m(E - V(\\vec{r}))} ds = 0$$</div>
This is Jacobi's geometric form of the Principle of Least Action, showing that dynamical trajectories in potential fields are <strong>geodesics</strong> in a curved Riemannian space with metric $g_{ij} = 2m(E - V)\\delta_{ij}$, providing the classical mechanical analogue to Fermat's principle of least time in optics.
"""
        },
        {
            "id": "u5-sec5",
            "title": "Hamiltonian of a Charged Particle in an Electromagnetic Field",
            "content": """
<h4>1. Construction of the Electromagnetic Hamiltonian</h4>
Recall the velocity-dependent Lagrangian of a particle with charge $q$ and mass $m$ in potentials $(\\Phi, \\vec{A})$:
<div class="math-display">$$L = \\frac{1}{2}m \\vec{v}^2 - q\\Phi + q \\vec{v} \\cdot \\vec{A}$$</div>
The canonical momentum $\\vec{p}$ conjugate to position $\\vec{r}$ is:
<div class="math-display">$$\\vec{p} = \\frac{\\partial L}{\\partial \\vec{v}} = m \\vec{v} + q \\vec{A}$$</div>
Notice that canonical momentum $\\vec{p}$ differs fundamentally from kinematic mechanical momentum $m \\vec{v}$:
<div class="math-display">$$m \\vec{v} = \\vec{p} - q \\vec{A}$$</div>
Inverting for velocity: $\\vec{v} = \\frac{1}{m}(\\vec{p} - q\\vec{A})$.
Applying the Legendre transformation:
<div class="math-display">$$H = \\vec{p} \\cdot \\vec{v} - L = \\vec{p} \\cdot \\vec{v} - \\left( \\frac{1}{2}m v^2 - q\\Phi + q \\vec{v} \\cdot \\vec{A} \\right) = \\vec{v} \\cdot (\\vec{p} - q\\vec{A}) - \\frac{1}{2}m v^2 + q\\Phi$$</div>
Substituting $\\vec{v} = \\frac{1}{m}(\\vec{p} - q\\vec{A})$:
<div class="math-display">$$H(\\vec{r}, \\vec{p}, t) = \\frac{1}{2m} (\\vec{p} - q\\vec{A}(\\vec{r}, t))^2 + q\\Phi(\\vec{r}, t)$$</div>

<h4>2. Hamilton's Equations for the Charged Particle</h4>
<div class="math-display">$$\\dot{\\vec{r}} = \\nabla_p H = \\frac{1}{m}(\\vec{p} - q\\vec{A})$$</div>
<div class="math-display">$$\\dot{\\vec{p}} = -\\nabla_r H = -q \\nabla \\Phi + \\frac{q}{m} \\sum_{j=1}^3 (p_j - q A_j) \\nabla A_j$$</div>
Substituting $\\vec{p} = m \\dot{\\vec{r}} + q \\vec{A}$ recovers the complete Lorentz force law $m \\ddot{\\vec{r}} = q(\\vec{E} + \\dot{\\vec{r}} \\times \\vec{B})$, proving exact equivalence.
"""
        }
    ],
    "problems": [
        {
            "id": "cm-prob-5-1",
            "title": "Phase Space Trajectory of a Relativistic 1D Harmonic Oscillator",
            "statement": "A particle of rest mass $m$ and potential energy $V(x) = \\frac{1}{2}k x^2$ moves relativistically in one dimension where relativistic Hamiltonian is $H(x, p) = \\sqrt{p^2 c^2 + m^2 c^4} - m c^2 + \\frac{1}{2}k x^2$. Derive Hamilton's canonical equations and find the shape of the phase space orbit for total energy $E$.",
            "steps": [
                {
                    "step": "Step 1: Compute Hamilton's Canonical Equations of Motion",
                    "math": "$$\\dot{x} = \\frac{\\partial H}{\\partial p} = \\frac{p c^2}{\\sqrt{p^2 c^2 + m^2 c^4}}, \\quad \\dot{p} = -\\frac{\\partial H}{\\partial x} = -k x$$",
                    "explanation": "Differentiating $H$ with respect to $p$ gives the relativistic velocity $v = \\frac{p c^2}{E_{\\text{kin}} + mc^2} = \\frac{p}{\\gamma m}$. The rate of change of momentum is the linear restoring force $-kx$."
                },
                {
                    "step": "Step 2: Derive the Phase Space Boundary Equation",
                    "math": "$$\\sqrt{p^2 c^2 + m^2 c^4} + \\frac{1}{2}k x^2 = E + m c^2 = E_{\\text{total}}$$",
                    "explanation": "Since $\\frac{\\partial H}{\\partial t} = 0$, $H(x, p) = E = \\text{constant}$. Rearranging isolates the momentum $p(x)$."
                },
                {
                    "step": "Step 3: Solve for Phase Space Momentum p as a Function of x",
                    "math": "$$p(x) = \\pm \\frac{1}{c} \\sqrt{\\left(E + m c^2 - \\frac{1}{2}k x^2\\right)^2 - m^2 c^4}$$",
                    "explanation": "In the non-relativistic limit ($E \\ll mc^2$), this reduces to the familiar ellipse $p^2/(2m) + kx^2/2 = E$. In the ultra-relativistic limit ($p c \\gg mc^2$), the phase portrait deforms from an ellipse into diamond-like rounded contours."
                }
            ],
            "answer": "Equations of motion: ẋ = p c² / √(p² c² + m² c⁴), ṗ = -k x. Phase orbit: p(x) = ± (1/c) √[(E + mc² - kx²/2)² - m²c⁴]."
        },
        {
            "id": "cm-prob-5-2",
            "title": "Hamiltonian & Cyclic Coordinates of a Spherical Pendulum",
            "statement": "A spherical pendulum consists of a mass $m$ suspended by a rigid rod of length $l$ free to swing in any direction under gravity. Formulate the Hamiltonian $H(\\theta, \\phi, p_\\theta, p_\\phi)$ and determine the constants of motion.",
            "steps": [
                {
                    "step": "Step 1: Write Lagrangian in Spherical Coordinates (θ, φ)",
                    "math": "$$L = \\frac{1}{2}m l^2 (\\dot{\\theta}^2 + \\sin^2 \\theta \\dot{\\phi}^2) + m g l \\cos \\theta$$",
                    "explanation": "Here $\\theta$ is the polar angle from the downward vertical and $\\phi$ is the azimuthal angle. Potential energy is $V = -mgl\\cos\\theta$."
                },
                {
                    "step": "Step 2: Calculate Canonical Momenta and Invert for Velocities",
                    "math": "$$p_\\theta = m l^2 \\dot{\\theta} \\implies \\dot{\\theta} = \\frac{p_\\theta}{m l^2}, \\quad p_\\phi = m l^2 \\sin^2 \\theta \\dot{\\phi} \\implies \\dot{\\phi} = \\frac{p_\\phi}{m l^2 \\sin^2 \\theta}$$",
                    "explanation": "Notice that $\\phi$ does not appear in $L$; hence $p_\\phi$ is a strict constant of motion (conserved vertical angular momentum $L_z$)."
                },
                {
                    "step": "Step 3: Construct the Hamiltonian via Legendre Transform",
                    "math": "$$H = p_\\theta \\dot{\\theta} + p_\\phi \\dot{\\phi} - L = \\frac{p_\\theta^2}{2 m l^2} + \\frac{p_\\phi^2}{2 m l^2 \\sin^2 \\theta} - m g l \\cos \\theta$$",
                    "explanation": "Since the coordinates are scleronomic, $H = T + V = E = \\text{constant}$. The effective potential for $\\theta$-motion is $V_{\\text{eff}}(\\theta) = \\frac{p_\\phi^2}{2 m l^2 \\sin^2 \\theta} - m g l \\cos \\theta$."
                }
            ],
            "answer": "Hamiltonian: H = p_θ²/(2ml²) + p_φ²/(2ml² sin²θ) - mgl cos θ. Conserved quantities: H = E (total energy) and p_φ = L_z (azimuthal momentum)."
        },
        {
            "id": "cm-prob-5-3",
            "title": "Area of Phase Space Orbit for a 1D Harmonic Oscillator (Action Variable)",
            "statement": "For a 1D simple harmonic oscillator with mass $m$, spring constant $k = m\\omega^2$, and energy $E$, calculate the enclosed phase space area $J = \\oint p dq$ and show that it equals $2\\pi E / \\omega$.",
            "steps": [
                {
                    "step": "Step 1: Write the Equation of the Phase Space Trajectory",
                    "math": "$$H(q, p) = \\frac{p^2}{2m} + \\frac{1}{2}m \\omega^2 q^2 = E \\implies \\frac{q^2}{2E / (m\\omega^2)} + \\frac{p^2}{2m E} = 1$$",
                    "explanation": "The trajectory in $(q, p)$ phase space is an ellipse with semi-axes $q_0 = \\sqrt{\\frac{2E}{m\\omega^2}}$ and $p_0 = \\sqrt{2m E}$."
                },
                {
                    "step": "Step 2: Calculate the Enclosed Phase Area",
                    "math": "$$J = \\oint p dq = \\text{Area of Ellipse} = \\pi q_0 p_0 = \\pi \\sqrt{\\frac{2E}{m\\omega^2}} \\sqrt{2m E} = \\frac{2\\pi E}{\\omega}$$",
                    "explanation": "Evaluating the line integral $\\oint p dq$ around the closed periodic orbit yields the action variable $J = 2\\pi E / \\omega$."
                },
                {
                    "step": "Step 3: Relate to Period and Frequency",
                    "math": "$$\\frac{\\partial H}{\\partial J} = \\frac{\\partial E}{\\partial J} = \\frac{\\omega}{2\\pi} = \\nu = \\frac{1}{T_{\\text{period}}}$$",
                    "explanation": "The derivative of energy with respect to the action variable gives the orbital oscillation frequency $\\nu$, laying the foundation for action-angle variables and Bohr-Sommerfeld quantization $J = n h$."
                }
            ],
            "answer": "Phase space area: J = ∮ p dq = 2π E / ω. The quantity J is an adiabatic invariant under slow parameter variations."
        }
    ]
}

# Unit 6: Canonical Transformations & Poisson Brackets
u6 = {
    "unitNumber": 6,
    "number": 6,
    "title": "Canonical Transformations & Poisson Brackets",
    "subtitle": "Generating Functions, Symplectic Geometry, Poisson Bracket Lie Algebra & Liouville's Theorem",
    "description": "Exhaustive treatment of canonical transformations from (q, p) to (Q, P), four fundamental generating functions, symplectic matrix condition, Poisson brackets, fundamental canonical brackets, equation of motion in bracket notation, Poisson's theorem for constants of motion, Poincaré integral invariants, and Liouville's phase volume conservation theorem.",
    "topics": [
        "Concept of Canonical Transformations",
        "The Four Generating Functions (F1, F2, F3, F4)",
        "Symplectic Condition & Matrix Formulation",
        "Poisson Brackets & Fundamental Canonical Invariants",
        "Equations of Motion in Poisson Notation",
        "Constants of Motion & Poisson's Theorem",
        "Poincaré Invariants & Liouville's Phase Theorem"
    ],
    "sections": [
        {
            "id": "u6-sec1",
            "title": "Concept of Canonical Transformations & The Symplectic Condition",
            "content": """
<h4>1. Motivation for Coordinate Transformations in Phase Space</h4>
In Lagrangian mechanics, coordinate transformations are restricted to point transformations $Q_i = Q_i(q, t)$. In Hamiltonian mechanics, coordinates and conjugate momenta $(q, p)$ are treated on an equal footing. We consider broader transformations:
<div class="math-display">$$Q_i = Q_i(q, p, t), \\quad P_i = P_i(q, p, t), \\quad i = 1, 2, \\dots, n$$</div>
A transformation is defined as <strong>canonical</strong> (or contact) if there exists a new Hamiltonian $K(Q, P, t)$ such that the new variables satisfy Hamilton's canonical equations:
<div class="math-display">$$\\dot{Q}_i = \\frac{\\partial K}{\\partial P_i}, \\quad \\dot{P}_i = -\\frac{\\partial K}{\\partial Q_i}$$</div>

<h4>2. Variational Condition & Generating Function</h4>
Both original and transformed trajectories must satisfy the modified Hamilton's principle:
<div class="math-display">$$\\delta \\int_{t_1}^{t_2} \\left( \\sum_{i=1}^n p_i \\dot{q}_i - H(q, p, t) \\right) dt = 0, \\quad \\delta \\int_{t_1}^{t_2} \\left( \\sum_{i=1}^n P_i \\dot{Q}_i - K(Q, P, t) \\right) dt = 0$$</div>
The two integrands can differ at most by the exact total time derivative of an arbitrary function $F$, called the <strong>generating function</strong>:
<div class="math-display">$$\\sum_{i=1}^n p_i \\dot{q}_i - H = \\sum_{i=1}^n P_i \\dot{Q}_i - K + \\frac{dF}{dt}$$</div>
Multiplying by $dt$:
<div class="math-display">$$\\sum_{i=1}^n p_i dq_i - H dt = \\sum_{i=1}^n P_i dQ_i - K dt + dF$$</div>

<h4>3. The Symplectic Condition</h4>
Defining the $2n$-dimensional phase vector $\\mathbf{\\eta} = (q_1, \\dots, q_n, p_1, \\dots, p_n)^T$ and the fundamental symplectic matrix $\\mathbf{J}$:
<div class="math-display">$$\\mathbf{J} = \\begin{pmatrix} \\mathbf{0} & \\mathbf{I}_n \\\\ -\\mathbf{I}_n & \\mathbf{0} \\end{pmatrix}, \\quad \\mathbf{J}^T = -\\mathbf{J}, \\quad \\mathbf{J}^2 = -\\mathbf{I}_{2n}$$</div>
Let $\\mathbf{M}$ be the Jacobian matrix of the transformation $M_{ij} = \\frac{\\partial \\zeta_i}{\\partial \\eta_j}$ where $\\mathbf{\\zeta} = (Q, P)^T$. The transformation is canonical if and only if $\\mathbf{M}$ satisfies the <strong>symplectic condition</strong>:
<div class="math-display">$$\\mathbf{M}^T \\mathbf{J} \\mathbf{M} = \\mathbf{J}$$</div>
Taking the determinant yields $(\\det \\mathbf{M})^2 = 1 \\implies \\det \\mathbf{M} = 1$, proving that phase space volume is strictly preserved.
"""
        },
        {
            "id": "u6-sec2",
            "title": "The Four Fundamental Classes of Generating Functions",
            "content": """
<h4>1. Classification by Active Canonical Variables</h4>
Depending on which pair of old and new variables are chosen as independent variables, Legendre transformations yield four primary classes of generating functions:
<ol>
  <li><strong>Type 1: $F_1(q, Q, t)$</strong>
  <div class="math-display">$$dF_1 = \\sum_i p_i dq_i - \\sum_i P_i dQ_i + (K - H) dt$$</div>
  Equating partial differentials:
  <div class="math-display">$$p_i = \\frac{\\partial F_1}{\\partial q_i}, \\quad P_i = -\\frac{\\partial F_1}{\\partial Q_i}, \\quad K = H + \\frac{\\partial F_1}{\\partial t}$$</div></li>

  <li><strong>Type 2: $F_2(q, P, t) = F_1 + \\sum_i P_i Q_i$</strong>
  <div class="math-display">$$dF_2 = \\sum_i p_i dq_i + \\sum_i Q_i dP_i + (K - H) dt$$</div>
  Transformation relations:
  <div class="math-display">$$p_i = \\frac{\\partial F_2}{\\partial q_i}, \\quad Q_i = \\frac{\\partial F_2}{\\partial P_i}, \\quad K = H + \\frac{\\partial F_2}{\\partial t}$$</div>
  <p><em>Example:</em> The identity transformation is generated by $F_2 = \\sum_i q_i P_i$, giving $p_i = P_i$ and $Q_i = q_i$.</p></li>

  <li><strong>Type 3: $F_3(p, Q, t) = F_1 - \\sum_i p_i q_i$</strong>
  <div class="math-display">$$dF_3 = -\\sum_i q_i dp_i - \\sum_i P_i dQ_i + (K - H) dt$$</div>
  Transformation relations:
  <div class="math-display">$$q_i = -\\frac{\\partial F_3}{\\partial p_i}, \\quad P_i = -\\frac{\\partial F_3}{\\partial Q_i}, \\quad K = H + \\frac{\\partial F_3}{\\partial t}$$</div></li>

  <li><strong>Type 4: $F_4(p, P, t) = F_1 - \\sum_i p_i q_i + \\sum_i P_i Q_i$</strong>
  <div class="math-display">$$dF_4 = -\\sum_i q_i dp_i + \\sum_i Q_i dP_i + (K - H) dt$$</div>
  Transformation relations:
  <div class="math-display">$$q_i = -\\frac{\\partial F_4}{\\partial p_i}, \\quad Q_i = \\frac{\\partial F_4}{\\partial P_i}, \\quad K = H + \\frac{\\partial F_4}{\\partial t}$$</div></li>
</ol>
"""
        },
        {
            "id": "u6-sec3",
            "title": "Poisson Brackets: Definition, Properties & Lie Algebra",
            "content": """
<h4>1. Definition of the Poisson Bracket</h4>
Let $u(q, p, t)$ and $v(q, p, t)$ be two continuously differentiable functions defined on phase space. The <strong>Poisson bracket</strong> $[u, v]_{q,p}$ with respect to canonical variables $(q, p)$ is:
<div class="math-display">$$\\{u, v\\}_{q,p} = \\sum_{j=1}^n \\left( \\frac{\\partial u}{\\partial q_j} \\frac{\\partial v}{\\partial p_j} - \\frac{\\partial u}{\\partial p_j} \\frac{\\partial v}{\\partial q_j} \\right)$$</div>

<h4>2. Fundamental Algebraic Identities</h4>
Poisson brackets satisfy the defining axioms of a <strong>Lie algebra</strong>:
<ol>
  <li><strong>Anti-Symmetry:</strong> $\{u, v\} = -\{v, u\} \\implies \\{u, u\\} = 0$.</li>
  <li><strong>Bilinearity:</strong> $\{a u + b v, w\} = a\\{u, w\\} + b\\{v, w\\}$ for scalars $a, b$.</li>
  <li><strong>Leibniz Product Rule:</strong> $\{u v, w\} = u\\{v, w\\} + \\{u, w\\}v$.</li>
  <li><strong>The Jacobi Identity:</strong>
  <div class="math-display">$$\\{u, \\{v, w\\}\\} + \\{v, \\{w, u\\}\\} + \\{w, \\{u, v\\}\\} = 0$$</div></li>
</ol>

<h4>3. Fundamental Canonical Poisson Brackets</h4>
Evaluating the brackets for the fundamental coordinates and conjugate momenta yields:
<div class="math-display">$$\\{q_j, q_k\\} = 0, \\quad \\{p_j, p_k\\} = 0, \\quad \\{q_j, p_k\\} = \\delta_{jk}$$</div>
<p><strong>Canonical Invariance:</strong> A transformation $(q, p) \\to (Q, P)$ is canonical if and only if it preserves the fundamental Poisson brackets: $\{Q_j, Q_k\}_{q,p} = 0$, $\{P_j, P_k\}_{q,p} = 0$, and $\{Q_j, P_k\}_{q,p} = \\delta_{jk}$.</p>
<p><em>Quantum Correspondence:</em> Paul Dirac recognized that the quantum commutator $[\\hat{u}, \\hat{v}]$ directly maps to the classical Poisson bracket: $[\\hat{u}, \\hat{v}] = i \\hbar \\{u, v\\}$.</p>
"""
        },
        {
            "id": "u6-sec4",
            "title": "Equations of Motion in Poisson Bracket Notation & Poisson's Theorem",
            "content": """
<h4>1. Time Evolution of an Arbitrary Phase Space Observable</h4>
Let $f(q, p, t)$ be any dynamical variable. Its total time derivative along a trajectory is:
<div class="math-display">$$\\frac{df}{dt} = \\sum_{j=1}^n \\left( \\frac{\\partial f}{\\partial q_j} \\dot{q}_j + \\frac{\\partial f}{\\partial p_j} \\dot{p}_j \\right) + \\frac{\\partial f}{\\partial t}$$</div>
Substituting Hamilton's equations $\\dot{q}_j = \\frac{\\partial H}{\\partial p_j}$ and $\\dot{p}_j = -\\frac{\\partial H}{\\partial q_j}$:
<div class="math-display">$$\\frac{df}{dt} = \\sum_{j=1}^n \\left( \\frac{\\partial f}{\\partial q_j} \\frac{\\partial H}{\\partial p_j} - \\frac{\\partial f}{\\partial p_j} \\frac{\\partial H}{\\partial q_j} \\right) + \\frac{\\partial f}{\\partial t}$$</div>
Recognizing the Poisson bracket with the Hamiltonian:
<div class="math-display">$$\\frac{df}{dt} = \\{f, H\\} + \\frac{\\partial f}{\\partial t}$$</div>
<p>This is the master equation of classical Hamiltonian dynamics. Setting $f = q_j$ and $f = p_j$ automatically reproduces Hamilton's equations $\\dot{q}_j = \\{q_j, H\\}$ and $\\dot{p}_j = \\{p_j, H\\}$.</p>

<h4>2. First Integrals & Constants of Motion</h4>
If an observable $f(q, p)$ has no explicit time dependence ($\\frac{\\partial f}{\\partial t} = 0$), then $f$ is a <strong>constant of motion</strong> if and only if its Poisson bracket with the Hamiltonian vanishes:
<div class="math-display">$$\\frac{df}{dt} = 0 \\iff \\{f, H\\} = 0$$</div>

<h4>3. Poisson's Theorem for Generating New Conserved Quantities</h4>
<p><strong>Poisson's Theorem:</strong> If $f(q, p)$ and $g(q, p)$ are two independent constants of motion (so that $\{f, H\} = 0$ and $\{g, H\} = 0$), then their Poisson bracket $\{f, g\}$ is also a constant of motion.</p>
Proof via the Jacobi identity:
<div class="math-display">$$\\{\\{f, g\\}, H\\} = -\\{\\{g, H\\}, f\\} - \\{\\{H, f\\}, g\\} = -\\{0, f\\} - \\{0, g\\} = 0$$</div>
Hence $\\frac{d}{dt}\\{f, g\\} = 0$. Poisson's theorem enables systematically discovering new symmetries and conservation laws.
"""
        },
        {
            "id": "u6-sec5",
            "title": "Poincaré's Invariants & Liouville's Phase Volume Theorem",
            "content": """
<h4>1. Poincaré's Integral Invariants</h4>
Henri Poincaré proved that certain differential forms integrated over closed submanifolds in phase space remain invariant under canonical transformations and Hamiltonian time evolution.
The <strong>first Poincaré integral invariant</strong> of order 1 is:
<div class="math-display">$$J_1 = \\oint_C \\sum_{i=1}^n p_i dq_i = \\text{constant in time}$$</div>
where $C$ is any closed circuit in phase space carried along by the Hamiltonian flow.
Higher-order invariants $J_2, \\dots, J_n$ correspond to integrals over $2k$-dimensional manifolds. The invariant of maximum order $2n$ represents the total volume of phase space.

<h4>2. Liouville's Phase Volume Conservation Theorem</h4>
Consider an ensemble of non-interacting identical systems represented by a cloud of phase points with density distribution $\\rho(q, p, t)$ in $2n$-dimensional phase space.
By the continuity equation for probability conservation:
<div class="math-display">$$\\frac{\\partial \\rho}{\\partial t} + \\sum_{j=1}^n \\left( \\frac{\\partial (\\rho \\dot{q}_j)}{\\partial q_j} + \\frac{\\partial (\\rho \\dot{p}_j)}{\\partial p_j} \\right) = 0$$</div>
Expanding the derivatives:
<div class="math-display">$$\\frac{\\partial \\rho}{\\partial t} + \\sum_{j=1}^n \\left( \\frac{\\partial \\rho}{\\partial q_j} \\dot{q}_j + \\frac{\\partial \\rho}{\\partial p_j} \\dot{p}_j \\right) + \\rho \\sum_{j=1}^n \\left( \\frac{\\partial \\dot{q}_j}{\\partial q_j} + \\frac{\\partial \\dot{p}_j}{\\partial p_j} \\right) = 0$$</div>
Using Hamilton's canonical equations:
<div class="math-display">$$\\frac{\\partial \\dot{q}_j}{\\partial q_j} + \\frac{\\partial \\dot{p}_j}{\\partial p_j} = \\frac{\\partial}{\\partial q_j}\\left( \\frac{\\partial H}{\\partial p_j} \\right) + \\frac{\\partial}{\\partial p_j}\\left( -\\frac{\\partial H}{\\partial q_j} \\right) = \\frac{\\partial^2 H}{\\partial q_j \\partial p_j} - \\frac{\\partial^2 H}{\\partial p_j \\partial q_j} = 0$$</div>
The divergence of phase velocity vanishes identically: $\\nabla \\cdot \\vec{v}_{\\text{phase}} = 0$ (the phase flow is strictly incompressible).
Consequently, the convective total time derivative vanishes:
<div class="math-display">$$\\frac{d\\rho}{dt} = \\frac{\\partial \\rho}{\\partial t} + \\{\\rho, H\\} = 0$$</div>
<p><strong>Liouville's Theorem:</strong> The phase space volume $\\Gamma = \\int dq dp$ and the local phase space density $\\rho$ surrounding any moving system point remain strictly constant over time. Phase fluid flows like an incompressible liquid, preventing trajectories from ever crossing.</p>
"""
        }
    ],
    "problems": [
        {
            "id": "cm-prob-6-1",
            "title": "Verifying a Canonical Transformation via Type-1 Generating Function",
            "statement": "Given the generating function $F_1(q, Q) = \\frac{1}{2} m \\omega q^2 \\cot Q$, find the transformation equations relating $(q, p)$ to $(Q, P)$, show that the transformation is canonical, and apply it to solve the simple harmonic oscillator $H = \\frac{p^2}{2m} + \\frac{1}{2}m \\omega^2 q^2$.",
            "steps": [
                {
                    "step": "Step 1: Compute Canonical Momenta from Generating Relations",
                    "math": "$$p = \\frac{\\partial F_1}{\\partial q} = m \\omega q \\cot Q, \\quad P = -\\frac{\\partial F_1}{\\partial Q} = \\frac{1}{2} m \\omega q^2 \\csc^2 Q$$",
                    "explanation": "Solving for $q$ from the second equation: $q = \\sqrt{\\frac{2P}{m\\omega}} \\sin Q$. Substituting into the first equation: $p = m\\omega \\sqrt{\\frac{2P}{m\\omega}} \\sin Q \\frac{\\cos Q}{\\sin Q} = \\sqrt{2m \\omega P} \\cos Q$."
                },
                {
                    "step": "Step 2: Verify Fundamental Poisson Bracket {Q, P}",
                    "math": "$$\\{Q, P\\}_{q,p} = \\frac{\\partial Q}{\\partial q} \\frac{\\partial P}{\\partial p} - \\frac{\\partial Q}{\\partial p} \\frac{\\partial P}{\\partial q} = 1$$",
                    "explanation": "Evaluating the Poisson bracket confirms that the transformation preserves canonical invariants."
                },
                {
                    "step": "Step 3: Transform the Harmonic Oscillator Hamiltonian",
                    "math": "$$K(Q, P) = H(q(Q,P), p(Q,P)) = \\frac{2m \\omega P \\cos^2 Q}{2m} + \\frac{1}{2} m \\omega^2 \\left(\\frac{2P}{m\\omega} \\sin^2 Q\\right) = \\omega P$$",
                    "explanation": "Remarkably, $Q$ is completely cyclic in $K = \\omega P$. Hamilton's equations in the new variables become trivial: $\\dot{P} = -\\frac{\\partial K}{\\partial Q} = 0 \\implies P = \\text{const}$, and $\\dot{Q} = \\frac{\\partial K}{\\partial P} = \\omega \\implies Q(t) = \\omega t + \\beta$."
                }
            ],
            "answer": "Transformation: q = √(2P/(mω)) sin Q, p = √(2mωP) cos Q. Transformed Hamiltonian: K = ω P, yielding immediate linear solution Q(t) = ω t + β, P = E/ω."
        },
        {
            "id": "cm-prob-6-2",
            "title": "Poisson Bracket Lie Algebra of Angular Momentum Components",
            "statement": "Using the Cartesian definitions of orbital angular momentum components $L_x = y p_z - z p_y$, $L_y = z p_x - x p_z$, and $L_z = x p_y - y p_x$, compute the Poisson bracket $\{L_x, L_y\}$ and show that $\{L^2, L_z\} = 0$.",
            "steps": [
                {
                    "step": "Step 1: Compute {Lx, Ly} Using Fundamental Poisson Brackets",
                    "math": "$$\\{L_x, L_y\\} = \\{y p_z - z p_y, z p_x - x p_z\\} = \\{y p_z, z p_x\\} + \\{z p_y, x p_z\\}$$",
                    "explanation": "Cross terms with no shared coordinates vanish identically. Expanding using the Leibniz product rule: $\{y p_z, z p_x\} = y p_x \\{p_z, z\\} = -y p_x$."
                },
                {
                    "step": "Step 2: Evaluate the Second Term and Combine",
                    "math": "$$\\{z p_y, x p_z\\} = x p_y \\{z, p_z\\} = +x p_y \\implies \\{L_x, L_y\\} = x p_y - y p_x = L_z$$",
                    "explanation": "Cyclic permutations yield the complete angular momentum Lie algebra: $\{L_i, L_j\} = \\epsilon_{ijk} L_k$."
                },
                {
                    "step": "Step 3: Evaluate Poisson Bracket of L² with Lz",
                    "math": "$$\\{L^2, L_z\\} = \\{L_x^2 + L_y^2 + L_z^2, L_z\\} = 2 L_x \\{L_x, L_z\\} + 2 L_y \\{L_y, L_z\\} + 0 = 2 L_x (-L_y) + 2 L_y (L_x) = 0$$",
                    "explanation": "Because $\{L^2, L_z\} = 0$, total angular momentum magnitude squared $L^2$ and any one of its Cartesian components $L_z$ can be simultaneously conserved in spherically symmetric central force fields."
                }
            ],
            "answer": "Lie algebra: {Li, Lj} = ε_ijk L_k. Consequently, {L², L_z} = 0, proving simultaneous conservation."
        },
        {
            "id": "cm-prob-6-3",
            "title": "Symplectic Test on a Linear Phase Transformation",
            "statement": "Determine the conditions on constants $a, b, c, d$ such that the linear transformation $Q = a q + b p$, $P = c q + d p$ is strictly canonical, and verify Liouville's phase area preservation.",
            "steps": [
                {
                    "step": "Step 1: Compute the Fundamental Poisson Bracket {Q, P}",
                    "math": "$$\\{Q, P\\}_{q,p} = \\frac{\\partial Q}{\\partial q} \\frac{\\partial P}{\\partial p} - \\frac{\\partial Q}{\\partial p} \\frac{\\partial P}{\\partial q} = (a)(d) - (b)(c) = a d - b c$$",
                    "explanation": "For the transformation to be canonical, the fundamental Poisson bracket must satisfy $\{Q, P\} = 1$. This requires $a d - b c = 1$."
                },
                {
                    "step": "Step 2: Construct the Jacobian Transformation Matrix M",
                    "math": "$$\\mathbf{M} = \\begin{pmatrix} \\partial Q/\\partial q & \\partial Q/\\partial p \\\\ \\partial P/\\partial q & \\partial P/\\partial p \\end{pmatrix} = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$$",
                    "explanation": "The condition $a d - b c = 1$ is precisely the requirement that $\\det \\mathbf{M} = 1$, which belongs to the special linear group $SL(2, \\mathbb{R}) \\cong Sp(2, \\mathbb{R})$."
                },
                {
                    "step": "Step 3: Verify the Symplectic Condition M^T J M = J",
                    "math": "$$\\mathbf{M}^T \\mathbf{J} \\mathbf{M} = \\begin{pmatrix} a & c \\\\ b & d \\end{pmatrix} \\begin{pmatrix} 0 & 1 \\\\ -1 & 0 \\end{pmatrix} \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix} = \\begin{pmatrix} 0 & a d - b c \\\\ -(a d - b c) & 0 \\end{pmatrix} = \\mathbf{J}$$",
                    "explanation": "Since $\\det \\mathbf{M} = 1$, the transformation matrix preserves the symplectic 2-form $dq \\wedge dp = dQ \\wedge dP$, confirming Liouville's area conservation $dQ dP = dq dp$."
                }
            ],
            "answer": "The transformation is canonical if and only if ad - bc = 1 (unit Jacobian determinant), ensuring symplectic invariance and phase volume preservation."
        }
    ]
}

with open("cm_u5.json", "w", encoding="utf-8") as f:
    json.dump(u5, f, indent=2)

with open("cm_u6.json", "w", encoding="utf-8") as f:
    json.dump(u6, f, indent=2)

print("cm_u5.json and cm_u6.json generated successfully!")
