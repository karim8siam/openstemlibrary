# Unit 1 & Unit 2 Builder for Classical Mechanics & Special Relativity
import json

u1 = {
    "unitNumber": 1,
    "number": 1,
    "title": "Review of Elementary Principles & D'Alembert's Principle",
    "subtitle": "Constraints, Generalized Coordinates, Virtual Work, D'Alembert's Formulation & Velocity-Dependent Potentials",
    "description": "Exhaustive treatment of particle systems, classification of kinematic constraints, generalized coordinates, degrees of freedom, the principle of virtual work, D'Alembert's dynamic principle, derivation of Lagrange's equations, generalized velocity-dependent potentials (Lorentz force), and Rayleigh's dissipation function.",
    "topics": [
        "System of Particles & Conservation Laws",
        "Kinematic Constraints & Degrees of Freedom",
        "Principle of Virtual Work",
        "D'Alembert's Dynamic Formulation",
        "Derivation of Lagrange's Equations",
        "Velocity-Dependent Potentials (Lorentz Force)",
        "Rayleigh's Dissipation Function"
    ],
    "sections": [
        {
            "id": "u1-sec1",
            "title": "Mechanics of a System of Particles & Conservation Theorems",
            "content": """
<h4>1. Center of Mass & Total Linear Momentum</h4>
Consider an assembly of $N$ discrete particles with masses $m_i$ ($i = 1, 2, \\dots, N$) and position vectors $\\vec{r}_i$ measured relative to an inertial reference frame. The <strong>center of mass</strong> position vector $\\vec{R}$ is defined by:
<div class="math-display">$$\\vec{R} = \\frac{1}{M} \\sum_{i=1}^N m_i \\vec{r}_i, \\quad M = \\sum_{i=1}^N m_i$$</div>
Differentiating with respect to time yields the center of mass velocity $\\vec{V} = \\dot{\\vec{R}}$ and the total linear momentum $\\vec{P}$:
<div class="math-display">$$\\vec{P} = \\sum_{i=1}^N m_i \\dot{\\vec{r}}_i = M \\dot{\\vec{R}} = M \\vec{V}$$</div>

<h4>2. Newton's Second Law for Particle Systems</h4>
The net force acting on the $i$-th particle decomposes into an external force $\\vec{F}_i^{\\text{ext}}$ applied from outside the system and internal pairwise interaction forces $\\vec{F}_{ij}$ exerted on particle $i$ by particle $j$:
<div class="math-display">$$\\dot{\\vec{p}}_i = m_i \\ddot{\\vec{r}}_i = \\vec{F}_i^{\\text{ext}} + \\sum_{j \\neq i} \\vec{F}_{ij}$$</div>
Summing over all $N$ particles gives:
<div class="math-display">$$\\frac{d\\vec{P}}{dt} = \\sum_{i=1}^N \\dot{\\vec{p}}_i = \\sum_{i=1}^N \\vec{F}_i^{\\text{ext}} + \\sum_{i=1}^N \\sum_{j \\neq i} \\vec{F}_{ij}$$</div>
By Newton's Third Law (weak form), pairwise internal forces are equal and opposite: $\\vec{F}_{ij} = -\\vec{F}_{ji}$. Therefore, the double summation vanishes identically:
<div class="math-display">$$\\sum_{i=1}^N \\sum_{j \\neq i} \\vec{F}_{ij} = \\sum_{i < j} (\\vec{F}_{ij} + \\vec{F}_{ji}) = 0$$</div>
Hence, the rate of change of total linear momentum equals the net external force:
<div class="math-display">$$\\frac{d\\vec{P}}{dt} = M \\ddot{\\vec{R}} = \\vec{F}^{\\text{ext}}$$</div>
<p><strong>Conservation Theorem of Linear Momentum:</strong> If the total external force vanishes ($\\vec{F}^{\\text{ext}} = 0$), the total linear momentum is conserved ($\\vec{P} = \\text{constant}$), and the center of mass moves with constant rectilinear velocity.</p>

<h4>3. Angular Momentum & Internal Torques</h4>
The total angular momentum about the origin is $\\vec{L} = \\sum_{i=1}^N \\vec{r}_i \\times \\vec{p}_i$. Its time derivative is:
<div class="math-display">$$\\frac{d\\vec{L}}{dt} = \\sum_{i=1}^N (\\dot{\\vec{r}}_i \\times \\vec{p}_i) + \\sum_{i=1}^N (\\vec{r}_i \\times \\dot{\\vec{p}}_i) = \\sum_{i=1}^N \\vec{r}_i \\times \\vec{F}_i^{\\text{ext}} + \\sum_{i=1}^N \\sum_{j \\neq i} \\vec{r}_i \\times \\vec{F}_{ij}$$</div>
Since $\\dot{\\vec{r}}_i \\times m_i \\dot{\\vec{r}}_i = 0$. Grouping the internal cross products in pairs:
<div class="math-display">$$\\sum_{i < j} (\\vec{r}_i \\times \\vec{F}_{ij} + \\vec{r}_j \\times \\vec{F}_{ji}) = \\sum_{i < j} (\\vec{r}_i - \\vec{r}_j) \\times \\vec{F}_{ij}$$</div>
By the <strong>strong form of Newton's Third Law</strong>, internal forces are central—they act along the line connecting the particles, so $\\vec{F}_{ij} \\parallel (\\vec{r}_i - \\vec{r}_j)$. Consequently, $(\\vec{r}_i - \\vec{r}_j) \\times \\vec{F}_{ij} = 0$, yielding:
<div class="math-display">$$\\frac{d\\vec{L}}{dt} = \\sum_{i=1}^N \\vec{r}_i \\times \\vec{F}_i^{\\text{ext}} = \\vec{N}^{\\text{ext}}$$</div>
<p><strong>Conservation Theorem of Angular Momentum:</strong> If the net external torque about a chosen point vanishes ($\\vec{N}^{\\text{ext}} = 0$), total angular momentum $\\vec{L}$ about that point is conserved.</p>
"""
        },
        {
            "id": "u1-sec2",
            "title": "Constraints, Degrees of Freedom & Generalized Coordinates",
            "content": """
<h4>1. Classification of Mechanical Constraints</h4>
In any realistic dynamical setup, particle motions are restricted by geometric or kinematic limitations called <strong>constraints</strong>. Constraints are rigorously categorized into two primary divisions:
<ul>
  <li><strong>Holonomic Constraints:</strong> Expressible as algebraic equations involving only coordinates and time:
  <div class="math-display">$$f_k(\\vec{r}_1, \\vec{r}_2, \\dots, \\vec{r}_N, t) = 0, \\quad k = 1, 2, \\dots, m$$</div>
  Examples include a rigid rod connecting two masses ($|\\vec{r}_1 - \\vec{r}_2|^2 - L^2 = 0$) or a particle sliding on a spherical surface ($x^2 + y^2 + z^2 - R^2 = 0$).</li>
  <li><strong>Non-Holonomic Constraints:</strong> Cannot be integrated into coordinate-only relations. They occur as non-integrable differentials of velocities:
  <div class="math-display">$$\\sum_{i=1}^{3N} a_{ki} dq_i + a_{kt} dt = 0$$</div>
  or inequalities ($r^2 - R^2 \\ge 0$, e.g., a gas in a container or a bead rolling off a sphere). A classic non-holonomic example is a rolling disc without slipping.</li>
</ul>

<h4>2. Temporal Dependence: Scleronomic vs. Rheonomic</h4>
<ul>
  <li><strong>Scleronomic:</strong> Constraint equations do not depend explicitly on time $t$: $f_k(\\vec{r}_i) = 0$ (e.g., rigid pendulum with fixed pivot).</li>
  <li><strong>Rheonomic:</strong> Constraint equations depend explicitly on time $t$: $f_k(\\vec{r}_i, t) = 0$ (e.g., pendulum whose support oscillates vertically $z_0 = A \\cos \\omega t$).</li>
</ul>

<h4>3. Degrees of Freedom & Generalized Coordinates</h4>
For a system of $N$ particles subjected to $m$ independent holonomic constraints, the number of independent <strong>degrees of freedom</strong> $n$ is:
<div class="math-display">$$n = 3N - m$$</div>
Instead of managing $3N$ constrained Cartesian coordinates and calculating unknown constraint forces, we introduce a set of $n$ independent variables called <strong>generalized coordinates</strong>:
<div class="math-display">$$q_1, q_2, \\dots, q_n$$</div>
The Cartesian position of every particle is a function of the generalized coordinates and possibly time:
<div class="math-display">$$\\vec{r}_i = \\vec{r}_i(q_1, q_2, \\dots, q_n, t), \\quad i = 1, 2, \\dots, N$$</div>
The velocities are obtained via the multivariate chain rule:
<div class="math-display">$$\\vec{v}_i = \\dot{\\vec{r}}_i = \\sum_{j=1}^n \\frac{\\partial \\vec{r}_i}{\\partial q_j} \\dot{q}_j + \\frac{\\partial \\vec{r}_i}{\\partial t}$$</div>
"""
        },
        {
            "id": "u1-sec3",
            "title": "Principle of Virtual Work & Virtual Displacements",
            "content": """
<h4>1. Definition of Virtual Displacements</h4>
A <strong>virtual displacement</strong> $\\delta \\vec{r}_i$ is defined as an infinitesimal, arbitrary change in the coordinates of the system that is:
<ul>
  <li><strong>Purely geometric and instantaneous:</strong> It takes place at a fixed instant of time ($\\delta t = 0$).</li>
  <li><strong>Consistent with all instantaneous kinematic constraints:</strong> For holonomic constraints $f_k(\\vec{r}_i, t) = 0$, the virtual variations satisfy:
  <div class="math-display">$$\\sum_{i=1}^N \\nabla_i f_k \\cdot \\delta \\vec{r}_i = 0$$</div></li>
</ul>
<p>In contrast, a <em>real displacement</em> $d\\vec{r}_i = \\vec{v}_i dt$ occurs over a time interval $dt$ during which constraints may change explicitly with time.</p>

<h4>2. Virtual Work & Ideal Constraints</h4>
Let the total force on particle $i$ be decomposed into applied external force $\\vec{F}_i$ and constraint force $\\vec{f}_i$:
<div class="math-display">$$\\vec{F}_i^{\\text{total}} = \\vec{F}_i + \\vec{f}_i$$</div>
The virtual work $\\delta W$ done by all forces in an arbitrary virtual displacement is:
<div class="math-display">$$\\delta W = \\sum_{i=1}^N \\vec{F}_i^{\\text{total}} \\cdot \\delta \\vec{r}_i = \\sum_{i=1}^N \\vec{F}_i \\cdot \\delta \\vec{r}_i + \\sum_{i=1}^N \\vec{f}_i \\cdot \\delta \\vec{r}_i$$</div>
<p><strong>Postulate of Ideal Constraints:</strong> In standard classical mechanics, the net virtual work done by constraint forces vanishes identically for any virtual displacement consistent with constraints:</p>
<div class="math-display">$$\\sum_{i=1}^N \\vec{f}_i \\cdot \\delta \\vec{r}_i = 0$$</div>
<p>Examples of ideal constraints include rigid interatomic bonds, frictionless surfaces (where normal force $\\vec{N} \\perp \\delta \\vec{r}$), and rolling without slipping (where instantaneous point of contact has zero velocity).</p>

<h4>3. The Principle of Virtual Work for Static Equilibrium</h4>
For a system in static equilibrium, $\\vec{F}_i^{\\text{total}} = 0$. Incorporating the ideal constraint postulate, the condition for equilibrium reduces purely to the applied forces:
<div class="math-display">$$\\delta W = \\sum_{i=1}^N \\vec{F}_i \\cdot \\delta \\vec{r}_i = 0$$</div>
<p>This principle enables solving equilibrium problems without determining internal constraint forces.</p>
"""
        },
        {
            "id": "u1-sec4",
            "title": "D'Alembert's Principle & Dynamic Generalization",
            "content": """
<h4>1. Dynamic Inertial Forces</h4>
Jean le Rond d'Alembert (1743) converted dynamical problems into equivalent static problems by rewriting Newton's equation $\\vec{F}_i^{\\text{total}} = \\dot{\\vec{p}}_i$ as:
<div class="math-display">$$\\vec{F}_i + \\vec{f}_i - \\dot{\\vec{p}}_i = 0$$</div>
where $-\\dot{\\vec{p}}_i = -m_i \\ddot{\\vec{r}}_i$ is the reversed effective force (inertial force).

<h4>2. Statement of D'Alembert's Principle</h4>
Taking the dot product with an arbitrary virtual displacement $\\delta \\vec{r}_i$ and summing over all $N$ particles:
<div class="math-display">$$\\sum_{i=1}^N (\\vec{F}_i - \\dot{\\vec{p}}_i) \\cdot \\delta \\vec{r}_i + \\sum_{i=1}^N \\vec{f}_i \\cdot \\delta \\vec{r}_i = 0$$</div>
Invoking the postulate of ideal constraints ($\\sum \\vec{f}_i \\cdot \\delta \\vec{r}_i = 0$), we obtain <strong>D'Alembert's Principle</strong>:
<div class="math-display">$$\\sum_{i=1}^N (\\vec{F}_i - \\dot{\\vec{p}}_i) \\cdot \\delta \\vec{r}_i = 0$$</div>
<p>This principle is the cornerstone of analytical mechanics: it governs dynamics without requiring explicit knowledge of constraint forces.</p>
"""
        },
        {
            "id": "u1-sec5",
            "title": "Derivation of Lagrange's Equations from D'Alembert's Principle",
            "content": """
<h4>1. Transformation to Generalized Coordinates</h4>
Since $\\vec{r}_i = \\vec{r}_i(q_1, \\dots, q_n, t)$, the virtual displacement at fixed $t$ is:
<div class="math-display">$$\\delta \\vec{r}_i = \\sum_{j=1}^n \\frac{\\partial \\vec{r}_i}{\\partial q_j} \\delta q_j$$</div>
Substituting into D'Alembert's principle:
<div class="math-display">$$\\sum_{j=1}^n \\left[ \\sum_{i=1}^N \\vec{F}_i \\cdot \\frac{\\partial \\vec{r}_i}{\\partial q_j} - \\sum_{i=1}^N m_i \\ddot{\\vec{r}}_i \\cdot \\frac{\\partial \\vec{r}_i}{\\partial q_j} \\right] \\delta q_j = 0$$</div>

<h4>2. Generalized Force Definition</h4>
We define the <strong>generalized force</strong> $Q_j$ associated with coordinate $q_j$ as:
<div class="math-display">$$Q_j = \\sum_{i=1}^N \\vec{F}_i \\cdot \\frac{\\partial \\vec{r}_i}{\\partial q_j}$$</div>

<h4>3. Mathematical Identities for the Inertial Term</h4>
Consider the term $\\sum_i m_i \\ddot{\\vec{r}}_i \\cdot \\frac{\\partial \\vec{r}_i}{\\partial q_j}$:
<div class="math-display">$$\\ddot{\\vec{r}}_i \\cdot \\frac{\\partial \\vec{r}_i}{\\partial q_j} = \\frac{d}{dt}\\left( \\dot{\\vec{r}}_i \\cdot \\frac{\\partial \\vec{r}_i}{\\partial q_j} \\right) - \\dot{\\vec{r}}_i \\cdot \\frac{d}{dt}\\left(\\frac{\\partial \\vec{r}_i}{\\partial q_j}\\right)$$</div>
We apply two fundamental kinematic lemmas:
<ol>
  <li><strong>Cancellation of Dots:</strong> Since $\\vec{v}_i = \\sum_k \\frac{\\partial \\vec{r}_i}{\\partial q_k}\\dot{q}_k + \\frac{\\partial \\vec{r}_i}{\\partial t}$, differentiating with respect to $\\dot{q}_j$ gives:
  <div class="math-display">$$\\frac{\\partial \\vec{v}_i}{\\partial \\dot{q}_j} = \\frac{\\partial \\vec{r}_i}{\\partial q_j}$$</div></li>
  <li><strong>Interchange of Time and Partial Derivatives:</strong>
  <div class="math-display">$$\\frac{d}{dt}\\left(\\frac{\\partial \\vec{r}_i}{\\partial q_j}\\right) = \\sum_k \\frac{\\partial^2 \\vec{r}_i}{\\partial q_k \\partial q_j} \\dot{q}_k + \\frac{\\partial^2 \\vec{r}_i}{\\partial t \\partial q_j} = \\frac{\\partial}{\\partial q_j}\\left( \\sum_k \\frac{\\partial \\vec{r}_i}{\\partial q_k} \\dot{q}_k + \\frac{\\partial \\vec{r}_i}{\\partial t} \\right) = \\frac{\\partial \\vec{v}_i}{\\partial q_j}$$</div></li>
</ol>
Substituting both lemmas:
<div class="math-display">$$\\sum_{i=1}^N m_i \\ddot{\\vec{r}}_i \\cdot \\frac{\\partial \\vec{r}_i}{\\partial q_j} = \\sum_{i=1}^N m_i \\left[ \\frac{d}{dt}\\left(\\vec{v}_i \\cdot \\frac{\\partial \\vec{v}_i}{\\partial \\dot{q}_j}\\right) - \\vec{v}_i \\cdot \\frac{\\partial \\vec{v}_i}{\\partial q_j} \\right] = \\frac{d}{dt}\\left( \\frac{\\partial T}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial T}{\\partial q_j}$$</div>
where $T = \\frac{1}{2} \\sum_{i=1}^N m_i v_i^2$ is the total kinetic energy.

<h4>4. Final Form of Lagrange's Equations</h4>
D'Alembert's equation becomes:
<div class="math-display">$$\\sum_{j=1}^n \\left[ \\frac{d}{dt}\\left( \\frac{\\partial T}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial T}{\\partial q_j} - Q_j \\right] \\delta q_j = 0$$</div>
Since the generalized coordinates $q_j$ are completely independent, each coefficient must vanish identically:
<div class="math-display">$$\\frac{d}{dt}\\left( \\frac{\\partial T}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial T}{\\partial q_j} = Q_j, \\quad j = 1, 2, \\dots, n$$</div>
If forces are conservative, $\\vec{F}_i = -\\nabla_i V(\\vec{r})$, then $Q_j = -\\frac{\\partial V}{\\partial q_j}$. Since $V$ is independent of generalized velocities $\\dot{q}_j$, defining the <strong>Lagrangian</strong> $L = T - V$ yields:
<div class="math-display">$$\\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial L}{\\partial q_j} = 0, \\quad j = 1, 2, \\dots, n$$</div>
"""
        },
        {
            "id": "u1-sec6",
            "title": "Velocity-Dependent Potentials & Dissipation Functions",
            "content": """
<h4>1. Generalized Potentials for Velocity-Dependent Forces</h4>
If generalized forces can be expressed as:
<div class="math-display">$$Q_j = -\\frac{\\partial U}{\\partial q_j} + \\frac{d}{dt}\\left( \\frac{\\partial U}{\\partial \\dot{q}_j} \\right)$$</div>
then the Euler-Lagrange equations retain their standard canonical form $\\frac{d}{dt}\\frac{\\partial L}{\\partial \\dot{q}_j} - \\frac{\\partial L}{\\partial q_j} = 0$ with $L = T - U$.

<h4>2. The Electromagnetic Lorentz Force as a Generalized Potential</h4>
For a charged particle of charge $q$ moving with velocity $\\vec{v}$ in an electromagnetic field described by scalar potential $\\Phi(\\vec{r}, t)$ and vector potential $\\vec{A}(\\vec{r}, t)$, the Lorentz force is:
<div class="math-display">$$\\vec{F} = q \\left( \\vec{E} + \\vec{v} \\times \\vec{B} \\right) = q \\left( -\\nabla \\Phi - \\frac{\\partial \\vec{A}}{\\partial t} + \\vec{v} \\times (\\nabla \\times \\vec{A}) \\right)$$</div>
Using the vector identity $\\vec{v} \\times (\\nabla \\times \\vec{A}) = \\nabla(\\vec{v} \\cdot \\vec{A}) - (\\vec{v} \\cdot \\nabla)\\vec{A}$:
<div class="math-display">$$\\vec{F} = -\\nabla \\left( q \\Phi - q \\vec{v} \\cdot \\vec{A} \\right) - q \\left[ \\frac{\\partial \\vec{A}}{\\partial t} + (\\vec{v} \\cdot \\nabla)\\vec{A} \\right] = -\\nabla U - q \\frac{d\\vec{A}}{dt}$$</div>
Notice that $\\frac{\\partial U}{\\partial \\vec{v}} = -q \\vec{A}$. Hence:
<div class="math-display">$$\\frac{d}{dt}\\left( \\frac{\\partial U}{\\partial \\vec{v}} \\right) = -q \\frac{d\\vec{A}}{dt}$$</div>
Therefore, the electromagnetic force is derived from the generalized velocity-dependent potential:
<div class="math-display">$$U(\\vec{r}, \\vec{v}, t) = q \\Phi(\\vec{r}, t) - q \\vec{v} \\cdot \\vec{A}(\\vec{r}, t)$$</div>
The corresponding Lagrangian for a non-relativistic charged particle is:
<div class="math-display">$$L = \\frac{1}{2} m v^2 - q \\Phi + q \\vec{v} \\cdot \\vec{A}$$</div>
The canonical momentum $\\vec{p}$ conjugate to $\\vec{r}$ is:
<div class="math-display">$$\\vec{p} = \\frac{\\partial L}{\\partial \\vec{v}} = m \\vec{v} + q \\vec{A}$$</div>

<h4>3. Rayleigh's Dissipation Function</h4>
When frictional or viscous forces are proportional to velocity, $\\vec{F}_{f, i} = -k_i \\vec{v}_i$, Lord Rayleigh introduced the dissipation function $\\mathcal{F}$:
<div class="math-display">$$\\mathcal{F} = \\frac{1}{2} \\sum_{i=1}^N (k_{ix} v_{ix}^2 + k_{iy} v_{iy}^2 + k_{iz} v_{iz}^2)$$</div>
In generalized coordinates, the non-conservative generalized dissipative force is $Q_{j}^{\\text{diss}} = -\\frac{\\partial \\mathcal{F}}{\\partial \\dot{q}_j}$. The extended Lagrange equations become:
<div class="math-display">$$\\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial L}{\\partial q_j} + \\frac{\\partial \\mathcal{F}}{\\partial \\dot{q}_j} = 0$$</div>
The rate of energy dissipation from the system satisfies $\\frac{dE}{dt} = -2 \\mathcal{F} \\le 0$.
"""
        }
    ],
    "problems": [
        {
            "id": "cm-prob-1-1",
            "title": "Double Incline with Connected Masses via D'Alembert's Principle",
            "statement": "Two masses $m_1$ and $m_2$ rest on frictionless planes inclined at angles $\\alpha$ and $\\beta$ respectively. They are connected by an inextensible string passing over a frictionless massless pulley. Use D'Alembert's principle to determine the acceleration of the system and the tension in the string.",
            "steps": [
                {
                    "step": "Step 1: Formulate the Holonomic Constraint & Virtual Displacements",
                    "math": "$$s_1 + s_2 = L \\implies \\delta s_2 = -\\delta s_1$$",
                    "explanation": "Let $s_1$ be the displacement of mass $m_1$ down plane $\\alpha$, and $s_2$ the position of $m_2$ from the pulley along plane $\\beta$. Inextensibility requires $s_1 + s_2 = L$, so any virtual displacement satisfies $\\delta s_2 = -\\delta s_1$."
                },
                {
                    "step": "Step 2: Apply D'Alembert's Equation",
                    "math": "$$\\sum_{i=1}^2 (F_i - m_i a_i) \\delta s_i = (m_1 g \\sin \\alpha - m_1 a)\\delta s_1 + (m_2 g \\sin \\beta - m_2 (-a))(-\\delta s_1) = 0$$",
                    "explanation": "Since $a_1 = a$ and $a_2 = -a$, substituting applied forces along the planes and collecting terms in $\\delta s_1$ gives $(m_1 g \\sin \\alpha - m_2 g \\sin \\beta - (m_1 + m_2)a)\\delta s_1 = 0$."
                },
                {
                    "step": "Step 3: Solve for System Acceleration",
                    "math": "$$a = g \\frac{m_1 \\sin \\alpha - m_2 \\sin \\beta}{m_1 + m_2}$$",
                    "explanation": "Because $\\delta s_1$ is arbitrary, the coefficient must vanish. String tension is then found from single particle dynamics $T = m_1(g \\sin \\alpha - a) = \\frac{m_1 m_2 g(\\sin \\alpha + \\sin \\beta)}{m_1 + m_2}$."
                }
            ],
            "answer": "System acceleration: a = g (m1 sin α - m2 sin β)/(m1 + m2); Tension: T = m1 m2 g (sin α + sin β)/(m1 + m2)."
        },
        {
            "id": "cm-prob-1-2",
            "title": "Lagrangian of a Bead Sliding on a Uniformly Rotating Wire Hoop",
            "statement": "A bead of mass $m$ slides without friction on a circular wire hoop of radius $R$ in a vertical plane. The hoop rotates with constant angular velocity $\\omega$ about its vertical diameter. Set up the Lagrangian and derive the equation of motion for the angular position $\\theta$ of the bead.",
            "steps": [
                {
                    "step": "Step 1: Define Coordinates in Terms of Generalized Coordinate θ",
                    "math": "$$x = R \\sin \\theta \\cos(\\omega t), \\quad y = R \\sin \\theta \\sin(\\omega t), \\quad z = -R \\cos \\theta$$",
                    "explanation": "Here $\\theta$ is the angle of the bead measured from the lowest point of the hoop. The vertical axis is $z$, and the hoop rotates at azimuth $\\phi = \\omega t$."
                },
                {
                    "step": "Step 2: Calculate Velocities and Kinetic & Potential Energies",
                    "math": "$$v^2 = \\dot{x}^2 + \\dot{y}^2 + \\dot{z}^2 = R^2 \\dot{\\theta}^2 + R^2 \\omega^2 \\sin^2 \\theta$$",
                    "explanation": "The kinetic energy is $T = \\frac{1}{2}m R^2(\\dot{\\theta}^2 + \\omega^2 \\sin^2 \\theta)$. Taking $z=0$ at the center, potential energy is $V = -m g R \\cos \\theta$."
                },
                {
                    "step": "Step 3: Form the Lagrangian and Euler-Lagrange Equation",
                    "math": "$$L = \\frac{1}{2} m R^2 \\dot{\\theta}^2 + \\frac{1}{2} m R^2 \\omega^2 \\sin^2 \\theta + m g R \\cos \\theta$$",
                    "explanation": "Evaluating $\\frac{\\partial L}{\\partial \\dot{\\theta}} = m R^2 \\dot{\\theta}$ and $\\frac{\\partial L}{\\partial \\theta} = m R^2 \\omega^2 \\sin \\theta \\cos \\theta - m g R \\sin \\theta$, we obtain $\\ddot{\\theta} - \\left(\\omega^2 \\cos \\theta - \\frac{g}{R}\\right)\\sin \\theta = 0$."
                }
            ],
            "answer": "Equation of motion: θ̈ = (ω² cos θ - g/R) sin θ. A supercritical pitchfork bifurcation occurs at critical rotation speed ω_c = √(g/R)."
        },
        {
            "id": "cm-prob-1-3",
            "title": "Canonical Momentum & Lagrangian for a Charged Particle in Crossed E and B Fields",
            "statement": "Find the Lagrangian, generalized momentum, and equations of motion for a particle of charge $q$ and mass $m$ moving in a uniform magnetic field $\\vec{B} = B_0 \\hat{z}$ and uniform electric field $\\vec{E} = E_0 \\hat{y}$ using the Landau gauge $\\vec{A} = -B_0 y \\hat{x}$, $\\Phi = -E_0 y$.",
            "steps": [
                {
                    "step": "Step 1: Construct the Velocity-Dependent Lagrangian",
                    "math": "$$L = \\frac{1}{2}m (\\dot{x}^2 + \\dot{y}^2 + \\dot{z}^2) - q(-E_0 y) + q(-B_0 y \\dot{x})$$",
                    "explanation": "Substituting vector potential components $A_x = -B_0 y, A_y = A_z = 0$ and scalar potential $\\Phi = -E_0 y$ into $L = T - q\\Phi + q \\vec{v}\\cdot\\vec{A}$."
                },
                {
                    "step": "Step 2: Identify Cyclic Coordinates and Canonical Momenta",
                    "math": "$$p_x = \\frac{\\partial L}{\\partial \\dot{x}} = m \\dot{x} - q B_0 y = \\text{const}, \\quad p_z = m \\dot{z} = \\text{const}$$",
                    "explanation": "Coordinates $x$ and $z$ are cyclic since they do not appear explicitly in $L$. Their canonical momenta $p_x$ and $p_z$ are strict constants of motion."
                },
                {
                    "step": "Step 3: Derive Equation of Motion for the Non-Cyclic Coordinate y",
                    "math": "$$\\frac{d}{dt}(m \\dot{y}) - \\left( q E_0 - q B_0 \\dot{x} \\right) = 0 \\implies m \\ddot{y} = q E_0 - q B_0 \\dot{x}$$",
                    "explanation": "Substituting $\\dot{x} = \\frac{p_x + q B_0 y}{m}$ yields $m \\ddot{y} + \\omega_c^2 y = q E_0 - \\omega_c p_x$, showing harmonic cycloidal drift at cyclotron frequency $\\omega_c = q B_0 / m$."
                }
            ],
            "answer": "px = m ẋ - q B0 y = const; pz = m ż = const; y-motion undergoes cycloidal drift with drift velocity v_d = E0/B0."
        }
    ]
}

# Unit 2: Variational Principle & Advanced Lagrangian Dynamics
u2 = {
    "unitNumber": 2,
    "number": 2,
    "title": "Variational Principle and Lagrange's Equations",
    "subtitle": "Hamilton's Principle, Functional Calculus, Non-Holonomic Constraints & Chaotic Systems",
    "description": "Calculus of variations, Euler-Lagrange functional derivatives, Hamilton's principle of stationary action, derivation of equations of motion, undetermined Lagrange multipliers for non-holonomic systems, symmetries, cyclic coordinates, conservation laws, and the double pendulum chaotic dynamical system.",
    "topics": [
        "Calculus of Variations & Stationary Functionals",
        "Hamilton's Principle (Stationary Action)",
        "Equivalence to Newtonian Mechanics",
        "Lagrange Multipliers for Non-Holonomic Systems",
        "Symmetries & Noether's Conservation Theorems",
        "Coupled Oscillators & Normal Modes",
        "The Double Pendulum & Deterministic Chaos"
    ],
    "sections": [
        {
            "id": "u2-sec1",
            "title": "Calculus of Variations & The Fundamental Lemma",
            "content": """
<h4>1. Functionals & Extremal Path Problems</h4>
In ordinary calculus, we find points $x^*$ that extremize a function $f(x)$. In the <strong>calculus of variations</strong>, we seek an entire function or path $y(x)$ that extremizes a <strong>functional</strong>—an integral of the form:
<div class="math-display">$$J[y] = \\int_{x_1}^{x_2} f(y(x), y'(x), x) dx$$</div>
where $y'(x) = dy/dx$, and the endpoints are fixed: $y(x_1) = y_1$ and $y(x_2) = y_2$.

<h4>2. Variational Derivation of the Euler-Lagrange Equation</h4>
Let $y(x)$ be the true path that renders $J$ stationary. Consider a family of varied paths:
<div class="math-display">$$Y(x, \\alpha) = y(x) + \\alpha \\eta(x)$$</div>
where $\\alpha$ is a continuous parameter, and $\\eta(x)$ is an arbitrary differentiable function vanishing at the boundaries: $\\eta(x_1) = \\eta(x_2) = 0$. The functional becomes a function of $\\alpha$:
<div class="math-display">$$J(\\alpha) = \\int_{x_1}^{x_2} f(Y(x, \\alpha), Y'(x, \\alpha), x) dx$$</div>
Stationarity requires $\\left.\\frac{dJ}{d\\alpha}\\right|_{\\alpha=0} = 0$:
<div class="math-display">$$\\frac{dJ}{d\\alpha} = \\int_{x_1}^{x_2} \\left( \\frac{\\partial f}{\\partial Y} \\frac{\\partial Y}{\\partial \\alpha} + \\frac{\\partial f}{\\partial Y'} \\frac{\\partial Y'}{\\partial \\alpha} \\right) dx = \\int_{x_1}^{x_2} \\left( \\frac{\\partial f}{\\partial Y} \\eta(x) + \\frac{\\partial f}{\\partial Y'} \\eta'(x) \\right) dx$$</div>
Integrating the second term by parts:
<div class="math-display">$$\\int_{x_1}^{x_2} \\frac{\\partial f}{\\partial Y'} \\eta'(x) dx = \\left[ \\frac{\\partial f}{\\partial Y'} \\eta(x) \\right]_{x_1}^{x_2} - \\int_{x_1}^{x_2} \\frac{d}{dx}\\left( \\frac{\\partial f}{\\partial Y'} \\right) \\eta(x) dx$$</div>
Since $\\eta(x_1) = \\eta(x_2) = 0$, the boundary term vanishes. Setting $\\alpha = 0$:
<div class="math-display">$$\\int_{x_1}^{x_2} \\left[ \\frac{\\partial f}{\\partial y} - \\frac{d}{dx}\\left( \\frac{\\partial f}{\\partial y'} \\right) \\right] \\eta(x) dx = 0$$</div>
By the <strong>Fundamental Lemma of the Calculus of Variations</strong>, because $\\eta(x)$ is arbitrary, the integrand bracket must vanish everywhere:
<div class="math-display">$$\\frac{\\partial f}{\\partial y} - \\frac{d}{dx}\\left( \\frac{\\partial f}{\\partial y'} \\right) = 0$$</div>
"""
        },
        {
            "id": "u2-sec2",
            "title": "Hamilton's Principle of Stationary Action",
            "content": """
<h4>1. Definition of the Action Integral</h4>
In 1834, Sir William Rowan Hamilton generalized variational mechanics to dynamics. For a conservative dynamical system with configuration described by coordinates $q(t) = (q_1(t), \\dots, q_n(t))$, the <strong>action integral</strong> $S$ is defined as:
<div class="math-display">$$S[q] = \\int_{t_1}^{t_2} L(q, \\dot{q}, t) dt$$</div>
where $L = T - V$ is the Lagrangian.

<h4>2. Statement of Hamilton's Principle</h4>
<p><strong>Hamilton's Principle:</strong> The actual motion of a holonomic dynamical system from time $t_1$ to $t_2$ follows a trajectory $q(t)$ for which the action integral $S$ is stationary (an extremum, usually a minimum) with respect to arbitrary virtual variations $\\delta q_j(t)$ that vanish at the temporal endpoints:</p>
<div class="math-display">$$\\delta S = \\delta \\int_{t_1}^{t_2} L(q_j, \\dot{q}_j, t) dt = 0, \\quad \\delta q_j(t_1) = \\delta q_j(t_2) = 0$$</div>

<h4>3. Derivation of Lagrange's Equations</h4>
Commuting the variation $\\delta$ with the time integral:
<div class="math-display">$$\\delta S = \\int_{t_1}^{t_2} \\sum_{j=1}^n \\left( \\frac{\\partial L}{\\partial q_j} \\delta q_j + \\frac{\\partial L}{\\partial \\dot{q}_j} \\delta \\dot{q}_j \\right) dt$$</div>
Noting that $\\delta \\dot{q}_j = \\delta \\left(\\frac{dq_j}{dt}\\right) = \\frac{d}{dt}(\\delta q_j)$ and integrating the second term by parts:
<div class="math-display">$$\\int_{t_1}^{t_2} \\frac{\\partial L}{\\partial \\dot{q}_j} \\frac{d}{dt}(\\delta q_j) dt = \\left[ \\frac{\\partial L}{\\partial \\dot{q}_j} \\delta q_j \\right]_{t_1}^{t_2} - \\int_{t_1}^{t_2} \\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) \\delta q_j dt$$</div>
The boundary term vanishes identically because $\\delta q_j(t_1) = \\delta q_j(t_2) = 0$. Therefore:
<div class="math-display">$$\\delta S = \\int_{t_1}^{t_2} \\sum_{j=1}^n \\left[ \\frac{\\partial L}{\\partial q_j} - \\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) \\right] \\delta q_j dt = 0$$</div>
Since the variations $\\delta q_j$ are mutually independent, each coefficient must be zero, delivering the Euler-Lagrange equations of motion:
<div class="math-display">$$\\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial L}{\\partial q_j} = 0, \\quad j = 1, 2, \\dots, n$$</div>
"""
        },
        {
            "id": "u2-sec3",
            "title": "Extension to Non-Holonomic Systems & Lagrange Multipliers",
            "content": """
<h4>1. Constrained Variations with Undetermined Multipliers</h4>
When a system is subjected to $m$ non-holonomic constraints in differential form:
<div class="math-display">$$\\sum_{j=1}^n a_{kj} dq_j + a_{kt} dt = 0, \\quad k = 1, 2, \\dots, m$$</div>
virtual displacements (for which $\\delta t = 0$) are constrained by:
<div class="math-display">$$\\sum_{j=1}^n a_{kj} \\delta q_j = 0, \\quad k = 1, \\dots, m$$</div>
Because the variations $\\delta q_j$ are no longer independent, we cannot equate each coefficient in $\\delta S = 0$ to zero directly.

<h4>2. The Method of Lagrange Multipliers</h4>
We introduce $m$ time-dependent undetermined multipliers $\\lambda_k(t)$. Multiplying each constraint variation by $\\lambda_k(t)$, integrating from $t_1$ to $t_2$, and summing yields:
<div class="math-display">$$\\int_{t_1}^{t_2} \\sum_{k=1}^m \\lambda_k(t) \\left( \\sum_{j=1}^n a_{kj} \\delta q_j \\right) dt = 0$$</div>
Adding this zero sum to Hamilton's action variation $\\delta S = 0$:
<div class="math-display">$$\\int_{t_1}^{t_2} \\sum_{j=1}^n \\left[ \\frac{\\partial L}{\\partial q_j} - \\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) + \\sum_{k=1}^m \\lambda_k a_{kj} \\right] \\delta q_j dt = 0$$</div>
By appropriately choosing the $m$ multipliers $\\lambda_k(t)$, the brackets for $m$ of the coordinates vanish; the remaining $n - m$ variations are independent, requiring their brackets to vanish as well. Thus, for all $j = 1, 2, \\dots, n$:
<div class="math-display">$$\\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial L}{\\partial q_j} = \\sum_{k=1}^m \\lambda_k a_{kj} = Q_j^{\\text{constraint}}$$</div>
The terms $Q_j^{\\text{constraint}} = \\sum_{k=1}^m \\lambda_k a_{kj}$ represent the generalized forces of constraint. Together with the $m$ constraint equations, this provides $n + m$ equations for $n$ coordinates $q_j(t)$ and $m$ multipliers $\\lambda_k(t)$.
"""
        },
        {
            "id": "u2-sec4",
            "title": "Symmetries, Cyclic Coordinates & Noether's Theorem",
            "content": """
<h4>1. Cyclic Coordinates</h4>
If the Lagrangian $L(q, \\dot{q}, t)$ does not explicitly depend on a specific coordinate $q_k$, so that:
<div class="math-display">$$\\frac{\\partial L}{\\partial q_k} = 0$$</div>
then $q_k$ is termed an <strong>ignorable or cyclic coordinate</strong>.

<h4>2. Immediate Conservation of Conjugate Momentum</h4>
Substituting $\\frac{\\partial L}{\\partial q_k} = 0$ into Lagrange's equation:
<div class="math-display">$$\\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_k} \\right) = 0 \\implies p_k = \\frac{\\partial L}{\\partial \\dot{q}_k} = \\text{constant of motion}$$</div>
<p><strong>First Integral of Motion:</strong> The generalized momentum conjugate to any cyclic coordinate is strictly conserved throughout the motion.</p>

<h4>3. Spatial & Temporal Symmetries</h4>
<ul>
  <li><strong>Spatial Translation Invariance:</strong> If the Lagrangian is invariant under spatial translation along direction $\\hat{n}$, $\\sum_i \\vec{F}_i \\cdot \\hat{n} = 0$, the total linear momentum along $\\hat{n}$ is conserved.</li>
  <li><strong>Rotational Invariance:</strong> If the Lagrangian is invariant under rotation about axis $\\hat{u}$, $\\frac{\\partial L}{\\partial \\phi} = 0$, the total angular momentum along $\\hat{u}$ is conserved.</li>
  <li><strong>Time Translation Invariance & The Jacobi Integral:</strong> If the Lagrangian does not depend explicitly on time ($\\frac{\\partial L}{\\partial t} = 0$), the Jacobi energy integral $h$:
  <div class="math-display">$$h(q, \\dot{q}) = \\sum_{j=1}^n \\dot{q}_j \\frac{\\partial L}{\\partial \\dot{q}_j} - L = \\text{constant}$$</div>
  is conserved. When transformations to Cartesian coordinates are scleronomic (time-independent), $h = T + V = E$ (total mechanical energy).</li>
</ul>
"""
        },
        {
            "id": "u2-sec5",
            "title": "The Double Pendulum: Nonlinear Dynamics & Chaos",
            "content": """
<h4>1. Coordinate Parameterization</h4>
A planar double pendulum consists of mass $m_1$ connected by a rigid massless rod of length $l_1$ to a fixed pivot, and mass $m_2$ suspended from $m_1$ by a rod of length $l_2$. The generalized coordinates are the deflection angles $\\theta_1$ and $\\theta_2$ relative to the downward vertical:
<div class="math-display">$$x_1 = l_1 \\sin \\theta_1, \\quad y_1 = -l_1 \\cos \\theta_1$$</div>
<div class="math-display">$$x_2 = l_1 \\sin \\theta_1 + l_2 \\sin \\theta_2, \\quad y_2 = -l_1 \\cos \\theta_1 - l_2 \\cos \\theta_2$$</div>

<h4>2. Kinetic and Potential Energy Formulations</h4>
Differentiating positions:
<div class="math-display">$$v_1^2 = l_1^2 \\dot{\\theta}_1^2$$</div>
<div class="math-display">$$v_2^2 = l_1^2 \\dot{\\theta}_1^2 + l_2^2 \\dot{\\theta}_2^2 + 2 l_1 l_2 \\dot{\\theta}_1 \\dot{\\theta}_2 \\cos(\\theta_1 - \\theta_2)$$</div>
The total kinetic energy is:
<div class="math-display">$$T = \\frac{1}{2}(m_1 + m_2)l_1^2 \\dot{\\theta}_1^2 + \\frac{1}{2}m_2 l_2^2 \\dot{\\theta}_2^2 + m_2 l_1 l_2 \\dot{\\theta}_1 \\dot{\\theta}_2 \\cos(\\theta_1 - \\theta_2)$$</div>
The gravitational potential energy is:
<div class="math-display">$$V = -(m_1 + m_2)g l_1 \\cos \\theta_1 - m_2 g l_2 \\cos \\theta_2$$</div>

<h4>3. Coupled Nonlinear Equations of Motion</h4>
Applying the Euler-Lagrange equations yields:
<div class="math-display">$$(m_1 + m_2)l_1 \\ddot{\\theta}_1 + m_2 l_2 \\ddot{\\theta}_2 \\cos(\\theta_1 - \\theta_2) + m_2 l_2 \\dot{\\theta}_2^2 \\sin(\\theta_1 - \\theta_2) + (m_1 + m_2)g \\sin \\theta_1 = 0$$</div>
<div class="math-display">$$m_2 l_2 \\ddot{\\theta}_2 + m_2 l_1 \\ddot{\\theta}_1 \\cos(\\theta_1 - \\theta_2) - m_2 l_1 \\dot{\\theta}_1^2 \\sin(\\theta_1 - \\theta_2) + m_2 g \\sin \\theta_2 = 0$$</div>

<h4>4. Transition to Deterministic Chaos</h4>
For small amplitudes ($\\theta_1, \\theta_2 \\ll 1$), these equations linearize into coupled harmonic oscillators yielding two distinct <strong>normal modes</strong> with real frequencies $\\omega_1, \\omega_2$. However, at higher energies, the strong nonlinear coupling $\\cos(\\theta_1 - \\theta_2)$ and centrifugal terms induce <strong>deterministic chaos</strong>:
<ul>
  <li>Extreme sensitivity to initial conditions (positive Lyapunov exponent $\\lambda > 0$).</li>
  <li>Two trajectories separated initially by $|\Delta \\vec{x}(0)| \\sim 10^{-10}$ diverge exponentially: $|\\Delta \\vec{x}(t)| \\sim |\\Delta \\vec{x}(0)| e^{\\lambda t}$.</li>
  <li>Non-repeating, ergodic phase space orbits while conserving total energy $E = T + V$.</li>
</ul>
"""
        }
    ],
    "problems": [
        {
            "id": "cm-prob-2-1",
            "title": "The Brachistochrone Problem via Euler-Lagrange Variational Calculus",
            "statement": "Find the path connecting two points $A(0,0)$ and $B(x_2, y_2)$ in a uniform downward vertical gravitational field $g$ such that a bead sliding without friction takes the minimum possible transit time.",
            "steps": [
                {
                    "step": "Step 1: Set Up the Time Integral Functional",
                    "math": "$$v = \\sqrt{2gy} \\implies dt = \\frac{ds}{v} = \\frac{\\sqrt{1 + y'^2}}{\\sqrt{2gy}} dx$$",
                    "explanation": "Orienting the $y$-axis downwards from origin $(0,0)$, conservation of energy gives $v = \\sqrt{2gy}$. The transit time functional is $T[y] = \\frac{1}{\\sqrt{2g}} \\int_0^{x_2} \\frac{\\sqrt{1 + y'^2}}{\\sqrt{y}} dx$."
                },
                {
                    "step": "Step 2: Apply Beltrami Identity for Independent Variable x Missing",
                    "math": "$$f - y' \\frac{\\partial f}{\\partial y'} = C \\implies \\frac{\\sqrt{1 + y'^2}}{\\sqrt{y}} - y' \\frac{y'}{\\sqrt{y(1 + y'^2)}} = \\frac{1}{\\sqrt{y(1 + y'^2)}} = \\text{const}$$",
                    "explanation": "Since the integrand $f(y, y') = \\frac{\\sqrt{1+y'^2}}{\\sqrt{y}}$ does not explicitly depend on $x$, the first integral (Beltrami identity) applies: $y(1 + y'^2) = 2a$, where $a$ is a constant."
                },
                {
                    "step": "Step 3: Integrate Using Cycloid Parametrization",
                    "math": "$$y' = \\sqrt{\\frac{2a - y}{y}} \\implies x = \\int \\sqrt{\\frac{y}{2a - y}} dy$$",
                    "explanation": "Substituting $y = a(1 - \\cos \\theta)$ yields $dy = a \\sin \\theta d\\theta$, leading directly to $x = a(\\theta - \\sin \\theta)$. The optimal path is a cycloid."
                }
            ],
            "answer": "Parametric curve of fastest descent is a cycloid: x = a(θ - sin θ), y = a(1 - cos θ)."
        },
        {
            "id": "cm-prob-2-2",
            "title": "Lagrange Multipliers: Cylinder Rolling Down an Incline Without Slipping",
            "statement": "A uniform solid cylinder of mass $M$ and radius $R$ rolls down a rough incline of angle $\\alpha$ without slipping. Use Lagrange multipliers to simultaneously determine the linear acceleration and the force of static friction.",
            "steps": [
                {
                    "step": "Step 1: Formulate the Lagrangian with Coordinates x and θ",
                    "math": "$$L = T - V = \\left( \\frac{1}{2}M \\dot{x}^2 + \\frac{1}{2}I \\dot{\\theta}^2 \\right) - (-M g x \\sin \\alpha) = \\frac{1}{2}M \\dot{x}^2 + \\frac{1}{4}M R^2 \\dot{\\theta}^2 + M g x \\sin \\alpha$$",
                    "explanation": "Treat $x$ (displacement down the incline) and $\\theta$ (rotation angle) as initially independent coordinates. For a uniform solid cylinder, moment of inertia is $I = \\frac{1}{2}MR^2$."
                },
                {
                    "step": "Step 2: Express the Rolling Constraint in Differential Form",
                    "math": "$$dx - R d\\theta = 0 \\implies a_x = 1, \\quad a_\\theta = -R$$",
                    "explanation": "The rolling condition is $f(x, \\theta) = x - R\\theta = 0$. The generalized constraint forces are $Q_x = \\lambda(1) = \\lambda$ and $Q_\\theta = \\lambda(-R) = -\\lambda R$."
                },
                {
                    "step": "Step 3: Solve Lagrange's Equations with Multiplier λ",
                    "math": "$$M \\ddot{x} - M g \\sin \\alpha = \\lambda, \\quad \\frac{1}{2}M R^2 \\ddot{\\theta} = -\\lambda R$$",
                    "explanation": "Using $\\ddot{x} = R \\ddot{\\theta}$, the rotational equation becomes $\\frac{1}{2}M \\ddot{x} = -\\lambda$. Substituting $\\lambda = -\\frac{1}{2}M \\ddot{x}$ into the $x$-equation gives $M \\ddot{x} - M g \\sin \\alpha = -\\frac{1}{2}M \\ddot{x} \\implies \\ddot{x} = \\frac{2}{3}g \\sin \\alpha$."
                }
            ],
            "answer": "Acceleration: ẍ = (2/3) g sin α; Frictional constraint force: f_friction = |λ| = (1/3) M g sin α."
        },
        {
            "id": "cm-prob-2-3",
            "title": "Normal Modes of a Symmetric Linear Triatomic Molecule",
            "statement": "Model a linear triatomic molecule (such as CO₂) as three masses on a line connected by identical springs of constant $k$: a central atom of mass $M$ flanked by two equal masses $m$. Find the Lagrangian, normal mode frequencies, and normal coordinates.",
            "steps": [
                {
                    "step": "Step 1: Set Up Kinetic and Potential Energy Matrices",
                    "math": "$$T = \\frac{1}{2}m(\\dot{x}_1^2 + \\dot{x}_3^2) + \\frac{1}{2}M \\dot{x}_2^2, \\quad V = \\frac{1}{2}k(x_2 - x_1)^2 + \\frac{1}{2}k(x_3 - x_2)^2$$",
                    "explanation": "Coordinates $x_1, x_2, x_3$ represent linear displacements from equilibrium. Mass matrix is $T_{ij} = \\text{diag}(m, M, m)$ and potential matrix $V_{ij}$ has diagonal elements $(k, 2k, k)$ and off-diagonals $-k$."
                },
                {
                    "step": "Step 2: Solve the Characteristic Secular Determinant |V - ω² T| = 0",
                    "math": "$$\\det \\begin{pmatrix} k - m\\omega^2 & -k & 0 \\\\ -k & 2k - M\\omega^2 & -k \\\\ 0 & -k & k - m\\omega^2 \\end{pmatrix} = 0$$",
                    "explanation": "Expanding the determinant: $(k - m\\omega^2)[(k - m\\omega^2)(2k - M\\omega^2) - 2k^2] = 0$. Factoring yields $\\omega^2 [k - m\\omega^2][k(2m + M) - m M \\omega^2] = 0$."
                },
                {
                    "step": "Step 3: Extract the Three Normal Mode Frequencies",
                    "math": "$$\\omega_1 = 0, \\quad \\omega_2 = \\sqrt{\\frac{k}{m}}, \\quad \\omega_3 = \\sqrt{\\frac{k}{\\mu}}, \\quad \\mu = \\frac{m M}{2m + M}$$",
                    "explanation": "$\\omega_1 = 0$ corresponds to rigid translation of the entire molecule ($x_1 = x_2 = x_3$). $\\omega_2 = \\sqrt{k/m}$ is the symmetric stretch ($x_1 = -x_3, x_2 = 0$). $\\omega_3 = \\sqrt{k(2m+M)/(mM)}$ is the asymmetric stretch."
                }
            ],
            "answer": "Normal frequencies: ω1 = 0 (rigid translation), ω2 = √(k/m) (symmetric stretch), ω3 = √(k(1 + 2m/M)/m) (asymmetric stretch)."
        }
    ]
}

with open("cm_u1.json", "w", encoding="utf-8") as f:
    json.dump(u1, f, indent=2)

with open("cm_u2.json", "w", encoding="utf-8") as f:
    json.dump(u2, f, indent=2)

print("cm_u1.json and cm_u2.json generated successfully!")
