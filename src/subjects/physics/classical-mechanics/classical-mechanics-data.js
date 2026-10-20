// Classical Mechanics & Special Relativity Academic Data
// Comprehensive university-standard curriculum with complete derivations & solved exam problems

window.COURSE_DATA = {
  "courseId": "classical-mechanics",
  "courseTitle": "Classical Mechanics & Relativistic Dynamics",
  "courseSubtitle": "Lagrangian & Hamiltonian Formulations, Rigid Bodies, Poisson Brackets & Special Relativity",
  "units": [
    {
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
          "content": "\n<h4>1. Center of Mass & Total Linear Momentum</h4>\nConsider an assembly of $N$ discrete particles with masses $m_i$ ($i = 1, 2, \\dots, N$) and position vectors $\\vec{r}_i$ measured relative to an inertial reference frame. The <strong>center of mass</strong> position vector $\\vec{R}$ is defined by:\n<div class=\"math-display\">$$\\vec{R} = \\frac{1}{M} \\sum_{i=1}^N m_i \\vec{r}_i, \\quad M = \\sum_{i=1}^N m_i$$</div>\nDifferentiating with respect to time yields the center of mass velocity $\\vec{V} = \\dot{\\vec{R}}$ and the total linear momentum $\\vec{P}$:\n<div class=\"math-display\">$$\\vec{P} = \\sum_{i=1}^N m_i \\dot{\\vec{r}}_i = M \\dot{\\vec{R}} = M \\vec{V}$$</div>\n\n<h4>2. Newton's Second Law for Particle Systems</h4>\nThe net force acting on the $i$-th particle decomposes into an external force $\\vec{F}_i^{\\text{ext}}$ applied from outside the system and internal pairwise interaction forces $\\vec{F}_{ij}$ exerted on particle $i$ by particle $j$:\n<div class=\"math-display\">$$\\dot{\\vec{p}}_i = m_i \\ddot{\\vec{r}}_i = \\vec{F}_i^{\\text{ext}} + \\sum_{j \\neq i} \\vec{F}_{ij}$$</div>\nSumming over all $N$ particles gives:\n<div class=\"math-display\">$$\\frac{d\\vec{P}}{dt} = \\sum_{i=1}^N \\dot{\\vec{p}}_i = \\sum_{i=1}^N \\vec{F}_i^{\\text{ext}} + \\sum_{i=1}^N \\sum_{j \\neq i} \\vec{F}_{ij}$$</div>\nBy Newton's Third Law (weak form), pairwise internal forces are equal and opposite: $\\vec{F}_{ij} = -\\vec{F}_{ji}$. Therefore, the double summation vanishes identically:\n<div class=\"math-display\">$$\\sum_{i=1}^N \\sum_{j \\neq i} \\vec{F}_{ij} = \\sum_{i < j} (\\vec{F}_{ij} + \\vec{F}_{ji}) = 0$$</div>\nHence, the rate of change of total linear momentum equals the net external force:\n<div class=\"math-display\">$$\\frac{d\\vec{P}}{dt} = M \\ddot{\\vec{R}} = \\vec{F}^{\\text{ext}}$$</div>\n<p><strong>Conservation Theorem of Linear Momentum:</strong> If the total external force vanishes ($\\vec{F}^{\\text{ext}} = 0$), the total linear momentum is conserved ($\\vec{P} = \\text{constant}$), and the center of mass moves with constant rectilinear velocity.</p>\n\n<h4>3. Angular Momentum & Internal Torques</h4>\nThe total angular momentum about the origin is $\\vec{L} = \\sum_{i=1}^N \\vec{r}_i \\times \\vec{p}_i$. Its time derivative is:\n<div class=\"math-display\">$$\\frac{d\\vec{L}}{dt} = \\sum_{i=1}^N (\\dot{\\vec{r}}_i \\times \\vec{p}_i) + \\sum_{i=1}^N (\\vec{r}_i \\times \\dot{\\vec{p}}_i) = \\sum_{i=1}^N \\vec{r}_i \\times \\vec{F}_i^{\\text{ext}} + \\sum_{i=1}^N \\sum_{j \\neq i} \\vec{r}_i \\times \\vec{F}_{ij}$$</div>\nSince $\\dot{\\vec{r}}_i \\times m_i \\dot{\\vec{r}}_i = 0$. Grouping the internal cross products in pairs:\n<div class=\"math-display\">$$\\sum_{i < j} (\\vec{r}_i \\times \\vec{F}_{ij} + \\vec{r}_j \\times \\vec{F}_{ji}) = \\sum_{i < j} (\\vec{r}_i - \\vec{r}_j) \\times \\vec{F}_{ij}$$</div>\nBy the <strong>strong form of Newton's Third Law</strong>, internal forces are central—they act along the line connecting the particles, so $\\vec{F}_{ij} \\parallel (\\vec{r}_i - \\vec{r}_j)$. Consequently, $(\\vec{r}_i - \\vec{r}_j) \\times \\vec{F}_{ij} = 0$, yielding:\n<div class=\"math-display\">$$\\frac{d\\vec{L}}{dt} = \\sum_{i=1}^N \\vec{r}_i \\times \\vec{F}_i^{\\text{ext}} = \\vec{N}^{\\text{ext}}$$</div>\n<p><strong>Conservation Theorem of Angular Momentum:</strong> If the net external torque about a chosen point vanishes ($\\vec{N}^{\\text{ext}} = 0$), total angular momentum $\\vec{L}$ about that point is conserved.</p>\n",
          "simulation": "particle-system-momentum-sim"
        },
        {
          "id": "u1-sec2",
          "title": "Constraints, Degrees of Freedom & Generalized Coordinates",
          "content": "\n<h4>1. Classification of Mechanical Constraints</h4>\nIn any realistic dynamical setup, particle motions are restricted by geometric or kinematic limitations called <strong>constraints</strong>. Constraints are rigorously categorized into two primary divisions:\n<ul>\n  <li><strong>Holonomic Constraints:</strong> Expressible as algebraic equations involving only coordinates and time:\n  <div class=\"math-display\">$$f_k(\\vec{r}_1, \\vec{r}_2, \\dots, \\vec{r}_N, t) = 0, \\quad k = 1, 2, \\dots, m$$</div>\n  Examples include a rigid rod connecting two masses ($|\\vec{r}_1 - \\vec{r}_2|^2 - L^2 = 0$) or a particle sliding on a spherical surface ($x^2 + y^2 + z^2 - R^2 = 0$).</li>\n  <li><strong>Non-Holonomic Constraints:</strong> Cannot be integrated into coordinate-only relations. They occur as non-integrable differentials of velocities:\n  <div class=\"math-display\">$$\\sum_{i=1}^{3N} a_{ki} dq_i + a_{kt} dt = 0$$</div>\n  or inequalities ($r^2 - R^2 \\ge 0$, e.g., a gas in a container or a bead rolling off a sphere). A classic non-holonomic example is a rolling disc without slipping.</li>\n</ul>\n\n<h4>2. Temporal Dependence: Scleronomic vs. Rheonomic</h4>\n<ul>\n  <li><strong>Scleronomic:</strong> Constraint equations do not depend explicitly on time $t$: $f_k(\\vec{r}_i) = 0$ (e.g., rigid pendulum with fixed pivot).</li>\n  <li><strong>Rheonomic:</strong> Constraint equations depend explicitly on time $t$: $f_k(\\vec{r}_i, t) = 0$ (e.g., pendulum whose support oscillates vertically $z_0 = A \\cos \\omega t$).</li>\n</ul>\n\n<h4>3. Degrees of Freedom & Generalized Coordinates</h4>\nFor a system of $N$ particles subjected to $m$ independent holonomic constraints, the number of independent <strong>degrees of freedom</strong> $n$ is:\n<div class=\"math-display\">$$n = 3N - m$$</div>\nInstead of managing $3N$ constrained Cartesian coordinates and calculating unknown constraint forces, we introduce a set of $n$ independent variables called <strong>generalized coordinates</strong>:\n<div class=\"math-display\">$$q_1, q_2, \\dots, q_n$$</div>\nThe Cartesian position of every particle is a function of the generalized coordinates and possibly time:\n<div class=\"math-display\">$$\\vec{r}_i = \\vec{r}_i(q_1, q_2, \\dots, q_n, t), \\quad i = 1, 2, \\dots, N$$</div>\nThe velocities are obtained via the multivariate chain rule:\n<div class=\"math-display\">$$\\vec{v}_i = \\dot{\\vec{r}}_i = \\sum_{j=1}^n \\frac{\\partial \\vec{r}_i}{\\partial q_j} \\dot{q}_j + \\frac{\\partial \\vec{r}_i}{\\partial t}$$</div>\n",
          "simulation": "rotating-wire-hoop-sim"
        },
        {
          "id": "u1-sec3",
          "title": "Principle of Virtual Work & Virtual Displacements",
          "content": "\n<h4>1. Definition of Virtual Displacements</h4>\nA <strong>virtual displacement</strong> $\\delta \\vec{r}_i$ is defined as an infinitesimal, arbitrary change in the coordinates of the system that is:\n<ul>\n  <li><strong>Purely geometric and instantaneous:</strong> It takes place at a fixed instant of time ($\\delta t = 0$).</li>\n  <li><strong>Consistent with all instantaneous kinematic constraints:</strong> For holonomic constraints $f_k(\\vec{r}_i, t) = 0$, the virtual variations satisfy:\n  <div class=\"math-display\">$$\\sum_{i=1}^N \\nabla_i f_k \\cdot \\delta \\vec{r}_i = 0$$</div></li>\n</ul>\n<p>In contrast, a <em>real displacement</em> $d\\vec{r}_i = \\vec{v}_i dt$ occurs over a time interval $dt$ during which constraints may change explicitly with time.</p>\n\n<h4>2. Virtual Work & Ideal Constraints</h4>\nLet the total force on particle $i$ be decomposed into applied external force $\\vec{F}_i$ and constraint force $\\vec{f}_i$:\n<div class=\"math-display\">$$\\vec{F}_i^{\\text{total}} = \\vec{F}_i + \\vec{f}_i$$</div>\nThe virtual work $\\delta W$ done by all forces in an arbitrary virtual displacement is:\n<div class=\"math-display\">$$\\delta W = \\sum_{i=1}^N \\vec{F}_i^{\\text{total}} \\cdot \\delta \\vec{r}_i = \\sum_{i=1}^N \\vec{F}_i \\cdot \\delta \\vec{r}_i + \\sum_{i=1}^N \\vec{f}_i \\cdot \\delta \\vec{r}_i$$</div>\n<p><strong>Postulate of Ideal Constraints:</strong> In standard classical mechanics, the net virtual work done by constraint forces vanishes identically for any virtual displacement consistent with constraints:</p>\n<div class=\"math-display\">$$\\sum_{i=1}^N \\vec{f}_i \\cdot \\delta \\vec{r}_i = 0$$</div>\n<p>Examples of ideal constraints include rigid interatomic bonds, frictionless surfaces (where normal force $\\vec{N} \\perp \\delta \\vec{r}$), and rolling without slipping (where instantaneous point of contact has zero velocity).</p>\n\n<h4>3. The Principle of Virtual Work for Static Equilibrium</h4>\nFor a system in static equilibrium, $\\vec{F}_i^{\\text{total}} = 0$. Incorporating the ideal constraint postulate, the condition for equilibrium reduces purely to the applied forces:\n<div class=\"math-display\">$$\\delta W = \\sum_{i=1}^N \\vec{F}_i \\cdot \\delta \\vec{r}_i = 0$$</div>\n<p>This principle enables solving equilibrium problems without determining internal constraint forces.</p>\n"
        },
        {
          "id": "u1-sec4",
          "title": "D'Alembert's Principle & Dynamic Generalization",
          "content": "\n<h4>1. Dynamic Inertial Forces</h4>\nJean le Rond d'Alembert (1743) converted dynamical problems into equivalent static problems by rewriting Newton's equation $\\vec{F}_i^{\\text{total}} = \\dot{\\vec{p}}_i$ as:\n<div class=\"math-display\">$$\\vec{F}_i + \\vec{f}_i - \\dot{\\vec{p}}_i = 0$$</div>\nwhere $-\\dot{\\vec{p}}_i = -m_i \\ddot{\\vec{r}}_i$ is the reversed effective force (inertial force).\n\n<h4>2. Statement of D'Alembert's Principle</h4>\nTaking the dot product with an arbitrary virtual displacement $\\delta \\vec{r}_i$ and summing over all $N$ particles:\n<div class=\"math-display\">$$\\sum_{i=1}^N (\\vec{F}_i - \\dot{\\vec{p}}_i) \\cdot \\delta \\vec{r}_i + \\sum_{i=1}^N \\vec{f}_i \\cdot \\delta \\vec{r}_i = 0$$</div>\nInvoking the postulate of ideal constraints ($\\sum \\vec{f}_i \\cdot \\delta \\vec{r}_i = 0$), we obtain <strong>D'Alembert's Principle</strong>:\n<div class=\"math-display\">$$\\sum_{i=1}^N (\\vec{F}_i - \\dot{\\vec{p}}_i) \\cdot \\delta \\vec{r}_i = 0$$</div>\n<p>This principle is the cornerstone of analytical mechanics: it governs dynamics without requiring explicit knowledge of constraint forces.</p>\n"
        },
        {
          "id": "u1-sec5",
          "title": "Derivation of Lagrange's Equations from D'Alembert's Principle",
          "content": "\n<h4>1. Transformation to Generalized Coordinates</h4>\nSince $\\vec{r}_i = \\vec{r}_i(q_1, \\dots, q_n, t)$, the virtual displacement at fixed $t$ is:\n<div class=\"math-display\">$$\\delta \\vec{r}_i = \\sum_{j=1}^n \\frac{\\partial \\vec{r}_i}{\\partial q_j} \\delta q_j$$</div>\nSubstituting into D'Alembert's principle:\n<div class=\"math-display\">$$\\sum_{j=1}^n \\left[ \\sum_{i=1}^N \\vec{F}_i \\cdot \\frac{\\partial \\vec{r}_i}{\\partial q_j} - \\sum_{i=1}^N m_i \\ddot{\\vec{r}}_i \\cdot \\frac{\\partial \\vec{r}_i}{\\partial q_j} \\right] \\delta q_j = 0$$</div>\n\n<h4>2. Generalized Force Definition</h4>\nWe define the <strong>generalized force</strong> $Q_j$ associated with coordinate $q_j$ as:\n<div class=\"math-display\">$$Q_j = \\sum_{i=1}^N \\vec{F}_i \\cdot \\frac{\\partial \\vec{r}_i}{\\partial q_j}$$</div>\n\n<h4>3. Mathematical Identities for the Inertial Term</h4>\nConsider the term $\\sum_i m_i \\ddot{\\vec{r}}_i \\cdot \\frac{\\partial \\vec{r}_i}{\\partial q_j}$:\n<div class=\"math-display\">$$\\ddot{\\vec{r}}_i \\cdot \\frac{\\partial \\vec{r}_i}{\\partial q_j} = \\frac{d}{dt}\\left( \\dot{\\vec{r}}_i \\cdot \\frac{\\partial \\vec{r}_i}{\\partial q_j} \\right) - \\dot{\\vec{r}}_i \\cdot \\frac{d}{dt}\\left(\\frac{\\partial \\vec{r}_i}{\\partial q_j}\\right)$$</div>\nWe apply two fundamental kinematic lemmas:\n<ol>\n  <li><strong>Cancellation of Dots:</strong> Since $\\vec{v}_i = \\sum_k \\frac{\\partial \\vec{r}_i}{\\partial q_k}\\dot{q}_k + \\frac{\\partial \\vec{r}_i}{\\partial t}$, differentiating with respect to $\\dot{q}_j$ gives:\n  <div class=\"math-display\">$$\\frac{\\partial \\vec{v}_i}{\\partial \\dot{q}_j} = \\frac{\\partial \\vec{r}_i}{\\partial q_j}$$</div></li>\n  <li><strong>Interchange of Time and Partial Derivatives:</strong>\n  <div class=\"math-display\">$$\\frac{d}{dt}\\left(\\frac{\\partial \\vec{r}_i}{\\partial q_j}\\right) = \\sum_k \\frac{\\partial^2 \\vec{r}_i}{\\partial q_k \\partial q_j} \\dot{q}_k + \\frac{\\partial^2 \\vec{r}_i}{\\partial t \\partial q_j} = \\frac{\\partial}{\\partial q_j}\\left( \\sum_k \\frac{\\partial \\vec{r}_i}{\\partial q_k} \\dot{q}_k + \\frac{\\partial \\vec{r}_i}{\\partial t} \\right) = \\frac{\\partial \\vec{v}_i}{\\partial q_j}$$</div></li>\n</ol>\nSubstituting both lemmas:\n<div class=\"math-display\">$$\\sum_{i=1}^N m_i \\ddot{\\vec{r}}_i \\cdot \\frac{\\partial \\vec{r}_i}{\\partial q_j} = \\sum_{i=1}^N m_i \\left[ \\frac{d}{dt}\\left(\\vec{v}_i \\cdot \\frac{\\partial \\vec{v}_i}{\\partial \\dot{q}_j}\\right) - \\vec{v}_i \\cdot \\frac{\\partial \\vec{v}_i}{\\partial q_j} \\right] = \\frac{d}{dt}\\left( \\frac{\\partial T}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial T}{\\partial q_j}$$</div>\nwhere $T = \\frac{1}{2} \\sum_{i=1}^N m_i v_i^2$ is the total kinetic energy.\n\n<h4>4. Final Form of Lagrange's Equations</h4>\nD'Alembert's equation becomes:\n<div class=\"math-display\">$$\\sum_{j=1}^n \\left[ \\frac{d}{dt}\\left( \\frac{\\partial T}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial T}{\\partial q_j} - Q_j \\right] \\delta q_j = 0$$</div>\nSince the generalized coordinates $q_j$ are completely independent, each coefficient must vanish identically:\n<div class=\"math-display\">$$\\frac{d}{dt}\\left( \\frac{\\partial T}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial T}{\\partial q_j} = Q_j, \\quad j = 1, 2, \\dots, n$$</div>\nIf forces are conservative, $\\vec{F}_i = -\\nabla_i V(\\vec{r})$, then $Q_j = -\\frac{\\partial V}{\\partial q_j}$. Since $V$ is independent of generalized velocities $\\dot{q}_j$, defining the <strong>Lagrangian</strong> $L = T - V$ yields:\n<div class=\"math-display\">$$\\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial L}{\\partial q_j} = 0, \\quad j = 1, 2, \\dots, n$$</div>\n"
        },
        {
          "id": "u1-sec6",
          "title": "Velocity-Dependent Potentials & Dissipation Functions",
          "content": "\n<h4>1. Generalized Potentials for Velocity-Dependent Forces</h4>\nIf generalized forces can be expressed as:\n<div class=\"math-display\">$$Q_j = -\\frac{\\partial U}{\\partial q_j} + \\frac{d}{dt}\\left( \\frac{\\partial U}{\\partial \\dot{q}_j} \\right)$$</div>\nthen the Euler-Lagrange equations retain their standard canonical form $\\frac{d}{dt}\\frac{\\partial L}{\\partial \\dot{q}_j} - \\frac{\\partial L}{\\partial q_j} = 0$ with $L = T - U$.\n\n<h4>2. The Electromagnetic Lorentz Force as a Generalized Potential</h4>\nFor a charged particle of charge $q$ moving with velocity $\\vec{v}$ in an electromagnetic field described by scalar potential $\\Phi(\\vec{r}, t)$ and vector potential $\\vec{A}(\\vec{r}, t)$, the Lorentz force is:\n<div class=\"math-display\">$$\\vec{F} = q \\left( \\vec{E} + \\vec{v} \\times \\vec{B} \\right) = q \\left( -\\nabla \\Phi - \\frac{\\partial \\vec{A}}{\\partial t} + \\vec{v} \\times (\\nabla \\times \\vec{A}) \\right)$$</div>\nUsing the vector identity $\\vec{v} \\times (\\nabla \\times \\vec{A}) = \\nabla(\\vec{v} \\cdot \\vec{A}) - (\\vec{v} \\cdot \\nabla)\\vec{A}$:\n<div class=\"math-display\">$$\\vec{F} = -\\nabla \\left( q \\Phi - q \\vec{v} \\cdot \\vec{A} \\right) - q \\left[ \\frac{\\partial \\vec{A}}{\\partial t} + (\\vec{v} \\cdot \\nabla)\\vec{A} \\right] = -\\nabla U - q \\frac{d\\vec{A}}{dt}$$</div>\nNotice that $\\frac{\\partial U}{\\partial \\vec{v}} = -q \\vec{A}$. Hence:\n<div class=\"math-display\">$$\\frac{d}{dt}\\left( \\frac{\\partial U}{\\partial \\vec{v}} \\right) = -q \\frac{d\\vec{A}}{dt}$$</div>\nTherefore, the electromagnetic force is derived from the generalized velocity-dependent potential:\n<div class=\"math-display\">$$U(\\vec{r}, \\vec{v}, t) = q \\Phi(\\vec{r}, t) - q \\vec{v} \\cdot \\vec{A}(\\vec{r}, t)$$</div>\nThe corresponding Lagrangian for a non-relativistic charged particle is:\n<div class=\"math-display\">$$L = \\frac{1}{2} m v^2 - q \\Phi + q \\vec{v} \\cdot \\vec{A}$$</div>\nThe canonical momentum $\\vec{p}$ conjugate to $\\vec{r}$ is:\n<div class=\"math-display\">$$\\vec{p} = \\frac{\\partial L}{\\partial \\vec{v}} = m \\vec{v} + q \\vec{A}$$</div>\n\n<h4>3. Rayleigh's Dissipation Function</h4>\nWhen frictional or viscous forces are proportional to velocity, $\\vec{F}_{f, i} = -k_i \\vec{v}_i$, Lord Rayleigh introduced the dissipation function $\\mathcal{F}$:\n<div class=\"math-display\">$$\\mathcal{F} = \\frac{1}{2} \\sum_{i=1}^N (k_{ix} v_{ix}^2 + k_{iy} v_{iy}^2 + k_{iz} v_{iz}^2)$$</div>\nIn generalized coordinates, the non-conservative generalized dissipative force is $Q_{j}^{\\text{diss}} = -\\frac{\\partial \\mathcal{F}}{\\partial \\dot{q}_j}$. The extended Lagrange equations become:\n<div class=\"math-display\">$$\\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial L}{\\partial q_j} + \\frac{\\partial \\mathcal{F}}{\\partial \\dot{q}_j} = 0$$</div>\nThe rate of energy dissipation from the system satisfies $\\frac{dE}{dt} = -2 \\mathcal{F} \\le 0$.\n"
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
      ],
      "id": "unit-1"
    },
    {
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
          "content": "\n<h4>1. Functionals & Extremal Path Problems</h4>\nIn ordinary calculus, we find points $x^*$ that extremize a function $f(x)$. In the <strong>calculus of variations</strong>, we seek an entire function or path $y(x)$ that extremizes a <strong>functional</strong>—an integral of the form:\n<div class=\"math-display\">$$J[y] = \\int_{x_1}^{x_2} f(y(x), y'(x), x) dx$$</div>\nwhere $y'(x) = dy/dx$, and the endpoints are fixed: $y(x_1) = y_1$ and $y(x_2) = y_2$.\n\n<h4>2. Variational Derivation of the Euler-Lagrange Equation</h4>\nLet $y(x)$ be the true path that renders $J$ stationary. Consider a family of varied paths:\n<div class=\"math-display\">$$Y(x, \\alpha) = y(x) + \\alpha \\eta(x)$$</div>\nwhere $\\alpha$ is a continuous parameter, and $\\eta(x)$ is an arbitrary differentiable function vanishing at the boundaries: $\\eta(x_1) = \\eta(x_2) = 0$. The functional becomes a function of $\\alpha$:\n<div class=\"math-display\">$$J(\\alpha) = \\int_{x_1}^{x_2} f(Y(x, \\alpha), Y'(x, \\alpha), x) dx$$</div>\nStationarity requires $\\left.\\frac{dJ}{d\\alpha}\\right|_{\\alpha=0} = 0$:\n<div class=\"math-display\">$$\\frac{dJ}{d\\alpha} = \\int_{x_1}^{x_2} \\left( \\frac{\\partial f}{\\partial Y} \\frac{\\partial Y}{\\partial \\alpha} + \\frac{\\partial f}{\\partial Y'} \\frac{\\partial Y'}{\\partial \\alpha} \\right) dx = \\int_{x_1}^{x_2} \\left( \\frac{\\partial f}{\\partial Y} \\eta(x) + \\frac{\\partial f}{\\partial Y'} \\eta'(x) \\right) dx$$</div>\nIntegrating the second term by parts:\n<div class=\"math-display\">$$\\int_{x_1}^{x_2} \\frac{\\partial f}{\\partial Y'} \\eta'(x) dx = \\left[ \\frac{\\partial f}{\\partial Y'} \\eta(x) \\right]_{x_1}^{x_2} - \\int_{x_1}^{x_2} \\frac{d}{dx}\\left( \\frac{\\partial f}{\\partial Y'} \\right) \\eta(x) dx$$</div>\nSince $\\eta(x_1) = \\eta(x_2) = 0$, the boundary term vanishes. Setting $\\alpha = 0$:\n<div class=\"math-display\">$$\\int_{x_1}^{x_2} \\left[ \\frac{\\partial f}{\\partial y} - \\frac{d}{dx}\\left( \\frac{\\partial f}{\\partial y'} \\right) \\right] \\eta(x) dx = 0$$</div>\nBy the <strong>Fundamental Lemma of the Calculus of Variations</strong>, because $\\eta(x)$ is arbitrary, the integrand bracket must vanish everywhere:\n<div class=\"math-display\">$$\\frac{\\partial f}{\\partial y} - \\frac{d}{dx}\\left( \\frac{\\partial f}{\\partial y'} \\right) = 0$$</div>\n",
          "simulation": "brachistochrone-sim"
        },
        {
          "id": "u2-sec2",
          "title": "Hamilton's Principle of Stationary Action",
          "content": "\n<h4>1. Definition of the Action Integral</h4>\nIn 1834, Sir William Rowan Hamilton generalized variational mechanics to dynamics. For a conservative dynamical system with configuration described by coordinates $q(t) = (q_1(t), \\dots, q_n(t))$, the <strong>action integral</strong> $S$ is defined as:\n<div class=\"math-display\">$$S[q] = \\int_{t_1}^{t_2} L(q, \\dot{q}, t) dt$$</div>\nwhere $L = T - V$ is the Lagrangian.\n\n<h4>2. Statement of Hamilton's Principle</h4>\n<p><strong>Hamilton's Principle:</strong> The actual motion of a holonomic dynamical system from time $t_1$ to $t_2$ follows a trajectory $q(t)$ for which the action integral $S$ is stationary (an extremum, usually a minimum) with respect to arbitrary virtual variations $\\delta q_j(t)$ that vanish at the temporal endpoints:</p>\n<div class=\"math-display\">$$\\delta S = \\delta \\int_{t_1}^{t_2} L(q_j, \\dot{q}_j, t) dt = 0, \\quad \\delta q_j(t_1) = \\delta q_j(t_2) = 0$$</div>\n\n<h4>3. Derivation of Lagrange's Equations</h4>\nCommuting the variation $\\delta$ with the time integral:\n<div class=\"math-display\">$$\\delta S = \\int_{t_1}^{t_2} \\sum_{j=1}^n \\left( \\frac{\\partial L}{\\partial q_j} \\delta q_j + \\frac{\\partial L}{\\partial \\dot{q}_j} \\delta \\dot{q}_j \\right) dt$$</div>\nNoting that $\\delta \\dot{q}_j = \\delta \\left(\\frac{dq_j}{dt}\\right) = \\frac{d}{dt}(\\delta q_j)$ and integrating the second term by parts:\n<div class=\"math-display\">$$\\int_{t_1}^{t_2} \\frac{\\partial L}{\\partial \\dot{q}_j} \\frac{d}{dt}(\\delta q_j) dt = \\left[ \\frac{\\partial L}{\\partial \\dot{q}_j} \\delta q_j \\right]_{t_1}^{t_2} - \\int_{t_1}^{t_2} \\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) \\delta q_j dt$$</div>\nThe boundary term vanishes identically because $\\delta q_j(t_1) = \\delta q_j(t_2) = 0$. Therefore:\n<div class=\"math-display\">$$\\delta S = \\int_{t_1}^{t_2} \\sum_{j=1}^n \\left[ \\frac{\\partial L}{\\partial q_j} - \\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) \\right] \\delta q_j dt = 0$$</div>\nSince the variations $\\delta q_j$ are mutually independent, each coefficient must be zero, delivering the Euler-Lagrange equations of motion:\n<div class=\"math-display\">$$\\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial L}{\\partial q_j} = 0, \\quad j = 1, 2, \\dots, n$$</div>\n"
        },
        {
          "id": "u2-sec3",
          "title": "Extension to Non-Holonomic Systems & Lagrange Multipliers",
          "content": "\n<h4>1. Constrained Variations with Undetermined Multipliers</h4>\nWhen a system is subjected to $m$ non-holonomic constraints in differential form:\n<div class=\"math-display\">$$\\sum_{j=1}^n a_{kj} dq_j + a_{kt} dt = 0, \\quad k = 1, 2, \\dots, m$$</div>\nvirtual displacements (for which $\\delta t = 0$) are constrained by:\n<div class=\"math-display\">$$\\sum_{j=1}^n a_{kj} \\delta q_j = 0, \\quad k = 1, \\dots, m$$</div>\nBecause the variations $\\delta q_j$ are no longer independent, we cannot equate each coefficient in $\\delta S = 0$ to zero directly.\n\n<h4>2. The Method of Lagrange Multipliers</h4>\nWe introduce $m$ time-dependent undetermined multipliers $\\lambda_k(t)$. Multiplying each constraint variation by $\\lambda_k(t)$, integrating from $t_1$ to $t_2$, and summing yields:\n<div class=\"math-display\">$$\\int_{t_1}^{t_2} \\sum_{k=1}^m \\lambda_k(t) \\left( \\sum_{j=1}^n a_{kj} \\delta q_j \\right) dt = 0$$</div>\nAdding this zero sum to Hamilton's action variation $\\delta S = 0$:\n<div class=\"math-display\">$$\\int_{t_1}^{t_2} \\sum_{j=1}^n \\left[ \\frac{\\partial L}{\\partial q_j} - \\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) + \\sum_{k=1}^m \\lambda_k a_{kj} \\right] \\delta q_j dt = 0$$</div>\nBy appropriately choosing the $m$ multipliers $\\lambda_k(t)$, the brackets for $m$ of the coordinates vanish; the remaining $n - m$ variations are independent, requiring their brackets to vanish as well. Thus, for all $j = 1, 2, \\dots, n$:\n<div class=\"math-display\">$$\\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial L}{\\partial q_j} = \\sum_{k=1}^m \\lambda_k a_{kj} = Q_j^{\\text{constraint}}$$</div>\nThe terms $Q_j^{\\text{constraint}} = \\sum_{k=1}^m \\lambda_k a_{kj}$ represent the generalized forces of constraint. Together with the $m$ constraint equations, this provides $n + m$ equations for $n$ coordinates $q_j(t)$ and $m$ multipliers $\\lambda_k(t)$.\n"
        },
        {
          "id": "u2-sec4",
          "title": "Symmetries, Cyclic Coordinates & Noether's Theorem",
          "content": "\n<h4>1. Cyclic Coordinates</h4>\nIf the Lagrangian $L(q, \\dot{q}, t)$ does not explicitly depend on a specific coordinate $q_k$, so that:\n<div class=\"math-display\">$$\\frac{\\partial L}{\\partial q_k} = 0$$</div>\nthen $q_k$ is termed an <strong>ignorable or cyclic coordinate</strong>.\n\n<h4>2. Immediate Conservation of Conjugate Momentum</h4>\nSubstituting $\\frac{\\partial L}{\\partial q_k} = 0$ into Lagrange's equation:\n<div class=\"math-display\">$$\\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_k} \\right) = 0 \\implies p_k = \\frac{\\partial L}{\\partial \\dot{q}_k} = \\text{constant of motion}$$</div>\n<p><strong>First Integral of Motion:</strong> The generalized momentum conjugate to any cyclic coordinate is strictly conserved throughout the motion.</p>\n\n<h4>3. Spatial & Temporal Symmetries</h4>\n<ul>\n  <li><strong>Spatial Translation Invariance:</strong> If the Lagrangian is invariant under spatial translation along direction $\\hat{n}$, $\\sum_i \\vec{F}_i \\cdot \\hat{n} = 0$, the total linear momentum along $\\hat{n}$ is conserved.</li>\n  <li><strong>Rotational Invariance:</strong> If the Lagrangian is invariant under rotation about axis $\\hat{u}$, $\\frac{\\partial L}{\\partial \\phi} = 0$, the total angular momentum along $\\hat{u}$ is conserved.</li>\n  <li><strong>Time Translation Invariance & The Jacobi Integral:</strong> If the Lagrangian does not depend explicitly on time ($\\frac{\\partial L}{\\partial t} = 0$), the Jacobi energy integral $h$:\n  <div class=\"math-display\">$$h(q, \\dot{q}) = \\sum_{j=1}^n \\dot{q}_j \\frac{\\partial L}{\\partial \\dot{q}_j} - L = \\text{constant}$$</div>\n  is conserved. When transformations to Cartesian coordinates are scleronomic (time-independent), $h = T + V = E$ (total mechanical energy).</li>\n</ul>\n"
        },
        {
          "id": "u2-sec5",
          "title": "The Double Pendulum: Nonlinear Dynamics & Chaos",
          "content": "\n<h4>1. Coordinate Parameterization</h4>\nA planar double pendulum consists of mass $m_1$ connected by a rigid massless rod of length $l_1$ to a fixed pivot, and mass $m_2$ suspended from $m_1$ by a rod of length $l_2$. The generalized coordinates are the deflection angles $\\theta_1$ and $\\theta_2$ relative to the downward vertical:\n<div class=\"math-display\">$$x_1 = l_1 \\sin \\theta_1, \\quad y_1 = -l_1 \\cos \\theta_1$$</div>\n<div class=\"math-display\">$$x_2 = l_1 \\sin \\theta_1 + l_2 \\sin \\theta_2, \\quad y_2 = -l_1 \\cos \\theta_1 - l_2 \\cos \\theta_2$$</div>\n\n<h4>2. Kinetic and Potential Energy Formulations</h4>\nDifferentiating positions:\n<div class=\"math-display\">$$v_1^2 = l_1^2 \\dot{\\theta}_1^2$$</div>\n<div class=\"math-display\">$$v_2^2 = l_1^2 \\dot{\\theta}_1^2 + l_2^2 \\dot{\\theta}_2^2 + 2 l_1 l_2 \\dot{\\theta}_1 \\dot{\\theta}_2 \\cos(\\theta_1 - \\theta_2)$$</div>\nThe total kinetic energy is:\n<div class=\"math-display\">$$T = \\frac{1}{2}(m_1 + m_2)l_1^2 \\dot{\\theta}_1^2 + \\frac{1}{2}m_2 l_2^2 \\dot{\\theta}_2^2 + m_2 l_1 l_2 \\dot{\\theta}_1 \\dot{\\theta}_2 \\cos(\\theta_1 - \\theta_2)$$</div>\nThe gravitational potential energy is:\n<div class=\"math-display\">$$V = -(m_1 + m_2)g l_1 \\cos \\theta_1 - m_2 g l_2 \\cos \\theta_2$$</div>\n\n<h4>3. Coupled Nonlinear Equations of Motion</h4>\nApplying the Euler-Lagrange equations yields:\n<div class=\"math-display\">$$(m_1 + m_2)l_1 \\ddot{\\theta}_1 + m_2 l_2 \\ddot{\\theta}_2 \\cos(\\theta_1 - \\theta_2) + m_2 l_2 \\dot{\\theta}_2^2 \\sin(\\theta_1 - \\theta_2) + (m_1 + m_2)g \\sin \\theta_1 = 0$$</div>\n<div class=\"math-display\">$$m_2 l_2 \\ddot{\\theta}_2 + m_2 l_1 \\ddot{\\theta}_1 \\cos(\\theta_1 - \\theta_2) - m_2 l_1 \\dot{\\theta}_1^2 \\sin(\\theta_1 - \\theta_2) + m_2 g \\sin \\theta_2 = 0$$</div>\n\n<h4>4. Transition to Deterministic Chaos</h4>\nFor small amplitudes ($\\theta_1, \\theta_2 \\ll 1$), these equations linearize into coupled harmonic oscillators yielding two distinct <strong>normal modes</strong> with real frequencies $\\omega_1, \\omega_2$. However, at higher energies, the strong nonlinear coupling $\\cos(\\theta_1 - \\theta_2)$ and centrifugal terms induce <strong>deterministic chaos</strong>:\n<ul>\n  <li>Extreme sensitivity to initial conditions (positive Lyapunov exponent $\\lambda > 0$).</li>\n  <li>Two trajectories separated initially by $|\\Delta \\vec{x}(0)| \\sim 10^{-10}$ diverge exponentially: $|\\Delta \\vec{x}(t)| \\sim |\\Delta \\vec{x}(0)| e^{\\lambda t}$.</li>\n  <li>Non-repeating, ergodic phase space orbits while conserving total energy $E = T + V$.</li>\n</ul>\n",
          "simulation": "double-pendulum-sim"
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
      ],
      "id": "unit-2"
    },
    {
      "unitNumber": 3,
      "number": 3,
      "title": "Central Force: Two-Body Problem, Kepler's Laws & Scattering",
      "subtitle": "Equivalent One-Body Reduction, Effective Potential, Binet's Orbit Equation, Runge-Lenz Vector, Virial Theorem & Rutherford Scattering",
      "description": "Comprehensive analysis of central force motion: reduction to equivalent one-body problem via reduced mass, conservation of angular momentum and areal velocity, effective potential and centrifugal barrier, Binet's differential orbit equation, conic section classification, Kepler's three laws, Laplace-Runge-Lenz invariant vector, the Virial theorem, classical scattering differential cross-sections, and CM-to-Lab coordinate transformations.",
      "topics": [
        "Two-Body Reduction & Reduced Mass",
        "Effective Potential & Centrifugal Barrier",
        "Binet's Differential Orbit Equation",
        "Kepler's Laws & Conic Section Orbits",
        "Laplace-Runge-Lenz Invariant Vector",
        "The Virial Theorem for Power Potentials",
        "Rutherford Classical Scattering & CM-Lab Transformation"
      ],
      "sections": [
        {
          "id": "u3-sec1",
          "title": "Two-Body Central Force Problem & One-Body Reduction",
          "content": "\n<h4>1. Decoupling Center-of-Mass and Relative Coordinates</h4>\nConsider two isolated particles of masses $m_1$ and $m_2$ interacting solely via an internal central force directed along the line joining them:\n<div class=\"math-display\">$$\\vec{F}_{12} = -\\vec{F}_{21} = f(r) \\hat{r}, \\quad \\vec{r} = \\vec{r}_1 - \\vec{r}_2, \\quad r = |\\vec{r}|$$</div>\nThe equations of motion are $m_1 \\ddot{\\vec{r}}_1 = f(r) \\hat{r}$ and $m_2 \\ddot{\\vec{r}}_2 = -f(r) \\hat{r}$. We introduce the center of mass coordinate $\\vec{R}$ and relative separation vector $\\vec{r}$:\n<div class=\"math-display\">$$\\vec{R} = \\frac{m_1 \\vec{r}_1 + m_2 \\vec{r}_2}{m_1 + m_2}, \\quad \\vec{r} = \\vec{r}_1 - \\vec{r}_2$$</div>\nThe individual position vectors in terms of $\\vec{R}$ and $\\vec{r}$ are:\n<div class=\"math-display\">$$\\vec{r}_1 = \\vec{R} + \\frac{m_2}{M}\\vec{r}, \\quad \\vec{r}_2 = \\vec{R} - \\frac{m_1}{M}\\vec{r}, \\quad M = m_1 + m_2$$</div>\n\n<h4>2. Separation of the Lagrangian & The Reduced Mass</h4>\nThe total kinetic energy decomposes cleanly:\n<div class=\"math-display\">$$T = \\frac{1}{2}m_1 \\dot{\\vec{r}}_1^2 + \\frac{1}{2}m_2 \\dot{\\vec{r}}_2^2 = \\frac{1}{2}M \\dot{\\vec{R}}^2 + \\frac{1}{2}\\mu \\dot{\\vec{r}}^2$$</div>\nwhere $\\mu$ is the <strong>reduced mass</strong> of the system:\n<div class=\"math-display\">$$\\mu = \\frac{m_1 m_2}{m_1 + m_2} = \\frac{m_1 m_2}{M}$$</div>\nSince the interaction potential $V(r)$ depends only on relative distance $r$, the Lagrangian separates:\n<div class=\"math-display\">$$L = L_{\\text{CM}} + L_{\\text{rel}} = \\left( \\frac{1}{2}M \\dot{\\vec{R}}^2 \\right) + \\left( \\frac{1}{2}\\mu \\dot{\\vec{r}}^2 - V(r) \\right)$$</div>\nBecause $\\vec{R}$ is completely cyclic, the center of mass moves with constant linear momentum $\\vec{P} = M \\dot{\\vec{R}} = \\text{const}$. In the center-of-mass frame ($\\vec{R} = 0$), the problem reduces strictly to a single particle of mass $\\mu$ moving in a static central potential $V(r)$.\n"
        },
        {
          "id": "u3-sec2",
          "title": "Conservation Laws: Planar Motion, Angular Momentum & Areal Velocity",
          "content": "\n<h4>1. Confinement to a Fixed Plane of Motion</h4>\nThe torque exerted by any central force $\\vec{F} = f(r)\\hat{r}$ relative to the force center vanishes identically:\n<div class=\"math-display\">$$\\vec{\\tau} = \\vec{r} \\times \\vec{F} = f(r) (\\vec{r} \\times \\hat{r}) = 0$$</div>\nConsequently, the orbital angular momentum $\\vec{L}$ is a strict constant of motion:\n<div class=\"math-display\">$$\\vec{L} = \\vec{r} \\times \\vec{p} = \\mu (\\vec{r} \\times \\dot{\\vec{r}}) = \\text{constant vector}$$</div>\nSince $\\vec{r} \\cdot \\vec{L} = \\vec{r} \\cdot (\\vec{r} \\times \\vec{p}) = 0$, the position vector $\\vec{r}$ remains perpendicular to the fixed direction of $\\vec{L}$ for all time. Thus, <strong>all central force motion is strictly confined to a two-dimensional plane</strong>.\n\n<h4>2. Polar Coordinate Representation & Kepler's Second Law</h4>\nChoosing plane polar coordinates $(r, \\theta)$ in the orbital plane:\n<div class=\"math-display\">$$\\vec{r} = r \\hat{r}, \\quad \\dot{\\vec{r}} = \\dot{r} \\hat{r} + r \\dot{\\theta} \\hat{\\theta}$$</div>\nThe magnitude of the angular momentum is:\n<div class=\"math-display\">$$l = |\\vec{L}| = \\mu r^2 \\dot{\\theta} = \\text{constant}$$</div>\nThe area swept out by the radius vector in time $dt$ is $dA = \\frac{1}{2} r (r d\\theta) = \\frac{1}{2} r^2 \\dot{\\theta} dt$. The <strong>areal velocity</strong> is therefore:\n<div class=\"math-display\">$$\\frac{dA}{dt} = \\frac{1}{2} r^2 \\dot{\\theta} = \\frac{l}{2\\mu} = \\text{constant}$$</div>\n<p><strong>Kepler's Second Law:</strong> The radius vector from the force center to the body sweeps out equal areas in equal intervals of time. This law holds universally for <em>any</em> central force, regardless of whether it follows an inverse-square law.</p>\n"
        },
        {
          "id": "u3-sec3",
          "title": "The Effective Potential Energy & Classification of Orbits",
          "content": "\n<h4>1. Total Energy in Radial Coordinates</h4>\nThe total mechanical energy in polar coordinates is:\n<div class=\"math-display\">$$E = T + V = \\frac{1}{2}\\mu (\\dot{r}^2 + r^2 \\dot{\\theta}^2) + V(r)$$</div>\nEliminating $\\dot{\\theta}$ using the conserved angular momentum $\\dot{\\theta} = \\frac{l}{\\mu r^2}$:\n<div class=\"math-display\">$$E = \\frac{1}{2}\\mu \\dot{r}^2 + \\frac{l^2}{2\\mu r^2} + V(r) = \\frac{1}{2}\\mu \\dot{r}^2 + V_{\\text{eff}}(r)$$</div>\n\n<h4>2. The Effective Potential $V_{\\text{eff}}(r)$</h4>\nThe dynamics of the radial coordinate $r(t)$ behaves identically to a 1D particle of mass $\\mu$ in an <strong>effective potential</strong>:\n<div class=\"math-display\">$$V_{\\text{eff}}(r) = V(r) + \\frac{l^2}{2\\mu r^2}$$</div>\nThe term $\\frac{l^2}{2\\mu r^2}$ is the <strong>centrifugal potential barrier</strong>, representing the kinetic energy associated with angular rotation. As $r \\to 0$, this barrier diverges as $+1/r^2$, preventing particles with non-zero angular momentum ($l \\neq 0$) from falling into the center.\n\n<h4>3. Classification of Orbits for Inverse-Square Gravity ($V(r) = -k/r$)</h4>\n<div class=\"math-display\">$$V_{\\text{eff}}(r) = -\\frac{k}{r} + \\frac{l^2}{2\\mu r^2}$$</div>\nSetting $\\frac{dV_{\\text{eff}}}{dr} = 0$:\n<div class=\"math-display\">$$\\frac{k}{r_0^2} - \\frac{l^2}{\\mu r_0^3} = 0 \\implies r_0 = \\frac{l^2}{\\mu k}$$</div>\nThe minimum value of the effective potential is:\n<div class=\"math-display\">$$V_{\\text{min}} = -\\frac{\\mu k^2}{2 l^2}$$</div>\nOrbit classification based on total energy $E$:\n<ul>\n  <li><strong>$E = V_{\\text{min}} = -\\frac{\\mu k^2}{2 l^2}$ (Circular Orbit):</strong> $\\dot{r} = 0$ constantly; orbit is a circle of radius $r = r_0$ ($e = 0$).</li>\n  <li><strong>$V_{\\text{min}} < E < 0$ (Elliptical Orbit):</strong> Bound orbit oscillating between periapsis $r_{\\text{min}}$ and apoapsis $r_{\\text{max}}$ ($0 < e < 1$).</li>\n  <li><strong>$E = 0$ (Parabolic Orbit):</strong> Unbound orbit with escape velocity; particle reaches infinity with zero residual kinetic energy ($e = 1$).</li>\n  <li><strong>$E > 0$ (Hyperbolic Orbit):</strong> Unbound scattering orbit; particle approaches from infinity and deflects off with non-zero residual velocity ($e > 1$).</li>\n</ul>\n",
          "simulation": "effective-potential-sim"
        },
        {
          "id": "u3-sec4",
          "title": "Binet's Equation & Kepler's Inverse-Square Orbits",
          "content": "\n<h4>1. Derivation of Binet's Differential Orbit Equation</h4>\nTo determine the geometric trajectory $r(\\theta)$ directly without solving for time $t$, we substitute $u = 1/r$. The radial velocity is:\n<div class=\"math-display\">$$\\dot{r} = \\frac{d}{dt}\\left(\\frac{1}{u}\\right) = -\\frac{1}{u^2}\\frac{du}{d\\theta}\\dot{\\theta} = -\\frac{1}{u^2}\\frac{du}{d\\theta}\\left(\\frac{l u^2}{\\mu}\\right) = -\\frac{l}{\\mu}\\frac{du}{d\\theta}$$</div>\nDifferentiating once more with respect to $t$:\n<div class=\"math-display\">$$\\ddot{r} = -\\frac{l}{\\mu}\\frac{d^2u}{d\\theta^2}\\dot{\\theta} = -\\frac{l^2 u^2}{\\mu^2}\\frac{d^2u}{d\\theta^2}$$</div>\nSubstituting $\\ddot{r}$ into the radial equation of motion $\\mu(\\ddot{r} - r\\dot{\\theta}^2) = f(r)$:\n<div class=\"math-display\">$$-\\frac{l^2 u^2}{\\mu}\\frac{d^2u}{d\\theta^2} - \\frac{l^2 u^3}{\\mu} = f(1/u)$$</div>\nMultiplying by $-\\frac{\\mu}{l^2 u^2}$ yields <strong>Binet's Formula</strong>:\n<div class=\"math-display\">$$\\frac{d^2u}{d\\theta^2} + u = -\\frac{\\mu}{l^2 u^2} f(1/u)$$</div>\n\n<h4>2. Exact Solution for the Gravitational Force ($f(r) = -k/r^2 = -k u^2$)</h4>\nSubstituting $f(1/u) = -k u^2$:\n<div class=\"math-display\">$$\\frac{d^2u}{d\\theta^2} + u = \\frac{\\mu k}{l^2}$$</div>\nThis is an inhomogeneous linear second-order differential equation with constant coefficients. Its general solution is:\n<div class=\"math-display\">$$u(\\theta) = \\frac{\\mu k}{l^2} + A \\cos(\\theta - \\theta_0)$$</div>\nSetting $\\theta_0 = 0$ along the periapsis direction and defining the semi-latus rectum $p$ and eccentricity $e$:\n<div class=\"math-display\">$$p = \\frac{l^2}{\\mu k}, \\quad e = \\frac{A l^2}{\\mu k}$$</div>\nInverting $u = 1/r$ delivers the universal polar equation of conic sections:\n<div class=\"math-display\">$$r(\\theta) = \\frac{p}{1 + e \\cos \\theta}$$</div>\nThe orbital eccentricity is related to total energy $E$ by:\n<div class=\"math-display\">$$e = \\sqrt{1 + \\frac{2 E l^2}{\\mu k^2}}$$</div>\n\n<h4>3. Kepler's Three Laws Derived</h4>\n<ol>\n  <li><strong>First Law (Law of Ellipses):</strong> For bound states ($E < 0$), $0 \\le e < 1$; the trajectory $r(\\theta)$ is an ellipse with the gravitational center at one focus.</li>\n  <li><strong>Second Law (Law of Equal Areas):</strong> Areal velocity $dA/dt = l/(2\\mu)$ is constant.</li>\n  <li><strong>Third Law (Harmonic Law):</strong> The area of an ellipse is $A = \\pi a b$, where $a = p/(1-e^2)$ is the semi-major axis and $b = a\\sqrt{1-e^2} = \\sqrt{a p} = l\\sqrt{a}/\\sqrt{\\mu k}$ is the semi-minor axis. The orbital period $\\tau$ is:\n  <div class=\"math-display\">$$\\tau = \\frac{\\text{Area}}{dA/dt} = \\frac{\\pi a b}{l / (2\\mu)} = \\frac{2\\pi \\mu a b}{l} = 2\\pi a^{3/2} \\sqrt{\\frac{\\mu}{k}}$$</div>\n  Squaring both sides and setting $k = G m_1 m_2$ and $\\mu = m_1 m_2 / (m_1 + m_2)$:\n  <div class=\"math-display\">$$\\tau^2 = \\frac{4\\pi^2 a^3}{G(m_1 + m_2)}$$</div></li>\n</ol>\n",
          "simulation": "kepler-orbit-sim"
        },
        {
          "id": "u3-sec5",
          "title": "The Laplace-Runge-Lenz Vector & The Virial Theorem",
          "content": "\n<h4>1. The Laplace-Runge-Lenz (LRL) Conserved Vector</h4>\nIn addition to energy $E$ and angular momentum $\\vec{L}$, the $1/r$ Kepler potential possesses an additional conserved vector quantity, the <strong>Laplace-Runge-Lenz vector</strong> $\\vec{A}$:\n<div class=\"math-display\">$$\\vec{A} = \\vec{p} \\times \\vec{L} - \\mu k \\hat{r}$$</div>\nProof of conservation:\n<div class=\"math-display\">$$\\frac{d\\vec{A}}{dt} = \\dot{\\vec{p}} \\times \\vec{L} - \\mu k \\dot{\\hat{r}}$$</div>\nSince $\\dot{\\vec{p}} = -\\frac{k}{r^2}\\hat{r}$ and $\\vec{L} = \\mu \\vec{r} \\times \\dot{\\vec{r}}$:\n<div class=\"math-display\">$$\\dot{\\vec{p}} \\times \\vec{L} = -\\frac{\\mu k}{r^2} [\\hat{r} \\times (\\vec{r} \\times \\dot{\\vec{r}})] = -\\frac{\\mu k}{r^2} [r \\dot{\\vec{r}} - (\\hat{r} \\cdot \\dot{\\vec{r}})\\vec{r}] = -\\mu k \\left( \\frac{\\dot{\\vec{r}}}{r} - \\frac{\\dot{r}\\vec{r}}{r^2} \\right) = -\\mu k \\dot{\\hat{r}}$$</div>\nThus $\\frac{d\\vec{A}}{dt} = -\\mu k \\dot{\\hat{r}} - (-\\mu k \\dot{\\hat{r}}) = 0$.\n<p><strong>Physical Significance:</strong> The vector $\\vec{A}$ lies permanently in the orbital plane, pointing directly from the focus toward the periapsis with magnitude $|\\vec{A}| = \\mu k e$. Its constancy prevents orbital precession, ensuring that Keplerian orbits are strictly closed. In modern physics, this reflects an underlying dynamic $SO(4)$ symmetry.</p>\n\n<h4>2. The Virial Theorem for Central Potentials</h4>\nConsider the quantity $G = \\sum_{i=1}^N \\vec{p}_i \\cdot \\vec{r}_i$. Its time derivative is:\n<div class=\"math-display\">$$\\frac{dG}{dt} = \\sum_{i=1}^N \\dot{\\vec{p}}_i \\cdot \\vec{r}_i + \\sum_{i=1}^N \\vec{p}_i \\cdot \\dot{\\vec{r}}_i = \\sum_{i=1}^N \\vec{F}_i \\cdot \\vec{r}_i + 2 T$$</div>\nTaking the long-term time average $\\langle X \\rangle = \\lim_{\\tau \\to \\infty} \\frac{1}{\\tau} \\int_0^\\tau X dt$:\n<div class=\"math-display\">$$\\left\\langle \\frac{dG}{dt} \\right\\rangle = \\lim_{\\tau \\to \\infty} \\frac{G(\\tau) - G(0)}{\\tau} = 0$$</div>\nsince for bound systems $G(t)$ remains bounded. Hence:\n<div class=\"math-display\">$$2\\langle T \\rangle = -\\left\\langle \\sum_{i=1}^N \\vec{F}_i \\cdot \\vec{r}_i \\right\\rangle$$</div>\nFor power-law potentials $V(r) = a r^n$, $\\vec{F} = -\\nabla V = -n a r^{n-2} \\vec{r}$, so $\\vec{F} \\cdot \\vec{r} = -n V(r)$. This yields the <strong>Virial Theorem</strong>:\n<div class=\"math-display\">$$2\\langle T \\rangle = n \\langle V \\rangle$$</div>\n<ul>\n  <li><strong>Gravitational / Coulomb Potential ($n = -1$):</strong> $2\\langle T \\rangle = -\\langle V \\rangle \\implies E = \\langle T \\rangle + \\langle V \\rangle = -\\langle T \\rangle = \\frac{1}{2}\\langle V \\rangle$.</li>\n  <li><strong>Harmonic Oscillator ($n = 2$):</strong> $2\\langle T \\rangle = 2\\langle V \\rangle \\implies \\langle T \\rangle = \\langle V \\rangle = \\frac{1}{2} E$.</li>\n</ul>\n"
        },
        {
          "id": "u3-sec6",
          "title": "Classical Scattering in a Central Field & Rutherford Formula",
          "content": "\n<h4>1. Kinematics of Elastic Scattering</h4>\nConsider a projectile of mass $m$ and initial speed $v_0$ incident from infinity with <strong>impact parameter</strong> $b$ (the perpendicular distance from the scattering center to the incident velocity line). The total angular momentum and energy are:\n<div class=\"math-display\">$$l = m v_0 b = b \\sqrt{2m E}, \\quad E = \\frac{1}{2}m v_0^2$$</div>\n\n<h4>2. The Scattering Angle $\\Theta$</h4>\nFrom the orbital equation in polar coordinates:\n<div class=\"math-display\">$$\\Theta = \\pi - 2 \\int_{r_{\\text{min}}}^\\infty \\frac{\\frac{l}{r^2} dr}{\\sqrt{2m [E - V(r)] - \\frac{l^2}{r^2}}}$$</div>\nFor a repulsive Coulomb potential $V(r) = \\frac{k}{r} = \\frac{q_1 q_2}{4\\pi \\varepsilon_0 r}$, evaluating the integral delivers the relation between impact parameter $b$ and scattering angle $\\theta$:\n<div class=\"math-display\">$$b = \\frac{k}{2E} \\cot\\left(\\frac{\\theta}{2}\\right)$$</div>\n\n<h4>3. The Differential Scattering Cross-Section</h4>\nParticles incident within an annular area $d\\sigma = 2\\pi b db$ scatter into a solid angle $d\\Omega = 2\\pi \\sin\\theta d\\theta$. The <strong>differential cross-section</strong> $\\frac{d\\sigma}{d\\Omega}$ is:\n<div class=\"math-display\">$$\\frac{d\\sigma}{d\\Omega} = \\frac{b}{\\sin\\theta} \\left| \\frac{db}{d\\theta} \\right|$$</div>\nDifferentiating $b(\\theta)$:\n<div class=\"math-display\">$$\\left| \\frac{db}{d\\theta} \\right| = \\frac{k}{4E} \\csc^2\\left(\\frac{\\theta}{2}\\right)$$</div>\nUsing $\\sin\\theta = 2 \\sin(\\theta/2) \\cos(\\theta/2)$:\n<div class=\"math-display\">$$\\frac{d\\sigma}{d\\Omega} = \\frac{\\frac{k}{2E}\\cot(\\theta/2)}{2\\sin(\\theta/2)\\cos(\\theta/2)} \\frac{k}{4E}\\csc^2(\\theta/2) = \\left( \\frac{k}{4E} \\right)^2 \\frac{1}{\\sin^4(\\theta/2)}$$</div>\nSubstituting $k = \\frac{q_1 q_2}{4\\pi \\varepsilon_0}$ yields the celebrated <strong>Rutherford Scattering Formula</strong>:\n<div class=\"math-display\">$$\\frac{d\\sigma}{d\\Omega} = \\left( \\frac{q_1 q_2}{16\\pi \\varepsilon_0 E} \\right)^2 \\frac{1}{\\sin^4(\\theta/2)}$$</div>\n",
          "simulation": "rutherford-scattering-sim"
        }
      ],
      "problems": [
        {
          "id": "cm-prob-3-1",
          "title": "Hohmann Orbital Transfer Maneuver Between Planetary Orbits",
          "statement": "A satellite in a circular low-Earth orbit of radius $r_1$ is to be transferred to a higher circular orbit of radius $r_2$ using an elliptical Hohmann transfer orbit with periapsis at $r_1$ and apoapsis at $r_2$. Calculate the required velocity increments $\\Delta v_1$ and $\\Delta v_2$ at both engine burns in terms of $v_1 = \\sqrt{GM/r_1}$ and ratio $R = r_2/r_1$.",
          "steps": [
            {
              "step": "Step 1: Determine the Semi-Major Axis of the Transfer Orbit",
              "math": "$$2a_t = r_1 + r_2 \\implies a_t = \\frac{r_1 + r_2}{2} = \\frac{r_1(1 + R)}{2}$$",
              "explanation": "The transfer ellipse is tangent to circular orbit 1 at periapsis ($r_p = r_1$) and to orbit 2 at apoapsis ($r_a = r_2$)."
            },
            {
              "step": "Step 2: Calculate Velocity on Transfer Ellipse at Periapsis and First Burn",
              "math": "$$v_{t,1} = \\sqrt{GM\\left(\\frac{2}{r_1} - \\frac{1}{a_t}\\right)} = v_1 \\sqrt{\\frac{2R}{1+R}}$$",
              "explanation": "By the Vis-Viva equation $v^2 = GM(2/r - 1/a)$. The impulse required to enter the transfer orbit is $\\Delta v_1 = v_{t,1} - v_1 = v_1 \\left( \\sqrt{\\frac{2R}{1+R}} - 1 \\right)$."
            },
            {
              "step": "Step 3: Calculate Velocity at Apoapsis and Second Burn",
              "math": "$$v_{t,2} = \\sqrt{GM\\left(\\frac{2}{r_2} - \\frac{1}{a_t}\\right)} = v_1 \\sqrt{\\frac{2}{R(1+R)}}, \\quad v_2 = \\sqrt{\\frac{GM}{r_2}} = \\frac{v_1}{\\sqrt{R}}$$",
              "explanation": "The second burn circularizes the orbit at $r_2$: $\\Delta v_2 = v_2 - v_{t,2} = \\frac{v_1}{\\sqrt{R}}\\left(1 - \\sqrt{\\frac{2}{1+R}}\\right)$."
            }
          ],
          "answer": "First burn: Δv1 = v1 (√(2R/(1+R)) - 1); Second burn: Δv2 = (v1/√R) (1 - √(2/(1+R))); Total Δv = Δv1 + Δv2."
        },
        {
          "id": "cm-prob-3-2",
          "title": "Orbital Precession Under an Inverse-Cube Perturbation via Binet's Equation",
          "statement": "A central force has the perturbed potential $V(r) = -\\frac{k}{r} - \\frac{\\epsilon}{r^2}$ where $\\epsilon$ is small. Use Binet's equation to find the modified orbit equation and calculate the rate of periapsis precession $\\Delta \\theta$ per revolution.",
          "steps": [
            {
              "step": "Step 1: Formulate Force Law and Apply Binet's Equation",
              "math": "$$f(r) = -\\frac{dV}{dr} = -\\frac{k}{r^2} - \\frac{2\\epsilon}{r^3} \\implies f(1/u) = -k u^2 - 2\\epsilon u^3$$",
              "explanation": "Substituting $f(1/u)$ into Binet's equation $\\frac{d^2u}{d\\theta^2} + u = -\\frac{\\mu}{l^2 u^2} f(1/u)$ gives $\\frac{d^2u}{d\\theta^2} + u = \\frac{\\mu k}{l^2} + \\frac{2\\mu \\epsilon}{l^2} u$."
            },
            {
              "step": "Step 2: Collect Terms in u and Define Effective Angular Frequency",
              "math": "$$\\frac{d^2u}{d\\theta^2} + \\gamma^2 u = \\frac{\\mu k}{l^2}, \\quad \\gamma^2 = 1 - \\frac{2\\mu \\epsilon}{l^2}$$",
              "explanation": "Rearranging gives $\\frac{d^2u}{d\\theta^2} + \\left(1 - \\frac{2\\mu \\epsilon}{l^2}\\right) u = \\frac{\\mu k}{l^2}$. The solution is $u(\\theta) = \\frac{\\mu k}{\\gamma^2 l^2} [1 + e \\cos(\\gamma \\theta)]$."
            },
            {
              "step": "Step 3: Determine Periapsis Precession per Orbit",
              "math": "$$\\gamma \\Delta \\theta_{\\text{period}} = 2\\pi \\implies \\Delta \\theta_{\\text{period}} = \\frac{2\\pi}{\\gamma} \\approx 2\\pi \\left(1 + \\frac{\\mu \\epsilon}{l^2}\\right)$$",
              "explanation": "The periapsis shifts by $\\delta \\theta = \\Delta \\theta_{\\text{period}} - 2\\pi \\approx \\frac{2\\pi \\mu \\epsilon}{l^2}$ radians per complete orbital revolution."
            }
          ],
          "answer": "Periapsis advances by Δθ = 2π μ ε / l² radians per revolution, demonstrating the classical analogue of general relativistic perihelion advance."
        },
        {
          "id": "cm-prob-3-3",
          "title": "Hard Sphere Scattering Differential and Total Cross-Section",
          "statement": "Calculate the differential scattering cross-section $\\frac{d\\sigma}{d\\Omega}$ and the total cross-section $\\sigma_{\\text{total}}$ for the elastic scattering of point particles from a rigid, impenetrable sphere of radius $R$.",
          "steps": [
            {
              "step": "Step 1: Relate Impact Parameter b to Scattering Angle θ by Law of Reflection",
              "math": "$$b = R \\sin \\alpha, \\quad \\theta = \\pi - 2\\alpha \\implies \\alpha = \\frac{\\pi - \\theta}{2}$$",
              "explanation": "For specular reflection from a hard sphere, the angle of incidence equals angle of reflection $\\alpha$. Hence $b = R \\sin\\left(\\frac{\\pi - \\theta}{2}\\right) = R \\cos\\left(\\frac{\\theta}{2}\\right)$."
            },
            {
              "step": "Step 2: Differentiate to Obtain Differential Cross-Section",
              "math": "$$\\left| \\frac{db}{d\\theta} \\right| = \\frac{R}{2} \\sin\\left(\\frac{\\theta}{2}\\right), \\quad \\frac{d\\sigma}{d\\Omega} = \\frac{b}{\\sin\\theta} \\left| \\frac{db}{d\\theta} \\right| = \\frac{R \\cos(\\theta/2)}{2\\sin(\\theta/2)\\cos(\\theta/2)} \\frac{R}{2}\\sin(\\theta/2) = \\frac{R^2}{4}$$",
              "explanation": "Remarkably, $\\frac{d\\sigma}{d\\Omega} = \\frac{R^2}{4}$ is completely independent of the scattering angle $\\theta$ and incident particle energy; scattering from a hard sphere is completely isotropic."
            },
            {
              "step": "Step 3: Integrate over Full Solid Angle to Find Total Cross-Section",
              "math": "$$\\sigma_{\\text{total}} = \\int \\frac{d\\sigma}{d\\Omega} d\\Omega = \\int_0^{2\\pi} d\\phi \\int_0^\\pi \\frac{R^2}{4} \\sin\\theta d\\theta = 4\\pi \\left(\\frac{R^2}{4}\\right) = \\pi R^2$$",
              "explanation": "The total classical scattering cross-section equals the geometric cross-sectional area of the sphere $\\pi R^2$."
            }
          ],
          "answer": "Differential cross-section: dσ/dΩ = R²/4 (isotropic scattering); Total cross-section: σ_total = π R²."
        }
      ],
      "id": "unit-3"
    },
    {
      "unitNumber": 4,
      "number": 4,
      "title": "The Rigid Body Motion & Euler's Equations",
      "subtitle": "Orthogonal Transformations, Eulerian Angles, Inertia Tensors, Euler's Dynamical Equations & Heavy Symmetrical Top",
      "description": "Exhaustive treatment of rigid body kinematics and dynamics: degrees of freedom, orthogonal rotation matrices and SO(3) group properties, Eulerian angles (precession, nutation, spin), Euler's rotation theorem, inertia tensor and dyadics, principal axes of inertia, Euler's dynamical equations with fixed points, Poinsot construction for torque-free motion, and the heavy symmetrical top with sleeping top stability.",
      "topics": [
        "Rigid Body Coordinates & Orthogonal Transformations",
        "Eulerian Angles (Precession, Nutation, Spin)",
        "Inertia Tensor & Ellipsoid of Inertia",
        "Principal Axes & Diagonalization of Inertia",
        "Euler's Dynamical Equations of Motion",
        "Torque-Free Motion & Poinsot Construction",
        "Heavy Symmetrical Top & Sleeping Top Stability"
      ],
      "sections": [
        {
          "id": "u4-sec1",
          "title": "Degrees of Freedom & Orthogonal Transformation Matrices",
          "content": "\n<h4>1. Degrees of Freedom of an Ideal Rigid Body</h4>\nA <strong>rigid body</strong> is an idealized assembly of $N$ particles where the inter-particle distances remain invariant under all forces:\n<div class=\"math-display\">$$|\\vec{r}_i - \\vec{r}_j| = c_{ij} = \\text{constant}, \\quad \\forall i, j$$</div>\nSpecifying the position of 3 non-collinear particles requires 9 coordinates subject to 3 internal distance constraints, yielding <strong>6 independent degrees of freedom</strong>:\n<ul>\n  <li><strong>3 Translational Degrees of Freedom:</strong> Specifying the position vector $\\vec{R}$ of the center of mass in the space-fixed inertial frame.</li>\n  <li><strong>3 Rotational Degrees of Freedom:</strong> Specifying the orientation of a body-fixed coordinate frame relative to the space-fixed frame.</li>\n</ul>\n\n<h4>2. Orthogonal Transformations</h4>\nLet $\\vec{r} = (x, y, z)^T$ be the coordinates of a vector in the space-fixed frame and $\\vec{r}' = (x', y', z')^T$ in the rotated frame. The linear transformation is:\n<div class=\"math-display\">$$\\vec{r}' = \\mathbf{A} \\vec{r}, \\quad x_i' = \\sum_{j=1}^3 A_{ij} x_j$$</div>\nInvariance of vector length requires $\\vec{r}' \\cdot \\vec{r}' = \\vec{r} \\cdot \\vec{r}$:\n<div class=\"math-display\">$$(\\mathbf{A}\\vec{r})^T (\\mathbf{A}\\vec{r}) = \\vec{r}^T (\\mathbf{A}^T \\mathbf{A}) \\vec{r} = \\vec{r}^T \\mathbf{I} \\vec{r}$$</div>\nThis necessitates the <strong>orthogonality condition</strong>:\n<div class=\"math-display\">$$\\mathbf{A}^T \\mathbf{A} = \\mathbf{A} \\mathbf{A}^T = \\mathbf{I} \\implies \\sum_{k=1}^3 A_{ki} A_{kj} = \\delta_{ij}$$</div>\nTaking the determinant: $\\det(\\mathbf{A}^T \\mathbf{A}) = (\\det \\mathbf{A})^2 = 1 \\implies \\det \\mathbf{A} = \\pm 1$.\nFor proper physical rotations (preserving coordinate handedness), $\\det \\mathbf{A} = +1$. The set of all such transformation matrices forms the special orthogonal Lie group $\\mathbf{SO(3)}$.\n"
        },
        {
          "id": "u4-sec2",
          "title": "The Eulerian Angles & Euler's Rotation Theorem",
          "content": "\n<h4>1. Standard Eulerian Angle Parameterization</h4>\nTo transform an initial space-fixed coordinate system $(x, y, z)$ into an arbitrary body-fixed system $(x', y', z')$, Leonhard Euler defined three successive rotations parameterized by the <strong>Eulerian angles</strong> $(\\phi, \\theta, \\psi)$:\n<ol>\n  <li><strong>Precession (Angle $\\phi$):</strong> Rotation counter-clockwise by angle $\\phi$ about the initial $z$-axis ($0 \\le \\phi < 2\\pi$). The resulting line of nodes $\\xi$ lies along the intersection of the $(x, y)$ and $(x', y')$ planes:\n  <div class=\"math-display\">$$\\mathbf{D}(\\phi) = \\begin{pmatrix} \\cos \\phi & \\sin \\phi & 0 \\\\ -\\sin \\phi & \\cos \\phi & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$$</div></li>\n  <li><strong>Nutation (Angle $\\theta$):</strong> Rotation by angle $\\theta$ about the intermediate line of nodes $\\xi$ ($0 \\le \\theta \\le \\pi$):\n  <div class=\"math-display\">$$\\mathbf{C}(\\theta) = \\begin{pmatrix} 1 & 0 & 0 \\\\ 0 & \\cos \\theta & \\sin \\theta \\\\ 0 & -\\sin \\theta & \\cos \\theta \\end{pmatrix}$$</div></li>\n  <li><strong>Intrinsic Body Spin (Angle $\\psi$):</strong> Rotation by angle $\\psi$ about the final body-fixed $z'$-axis ($0 \\le \\psi < 2\\pi$):\n  <div class=\"math-display\">$$\\mathbf{B}(\\psi) = \\begin{pmatrix} \\cos \\psi & \\sin \\psi & 0 \\\\ -\\sin \\psi & \\cos \\psi & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$$</div></li>\n</ol>\nThe composite rotation matrix $\\mathbf{A} = \\mathbf{B}(\\psi) \\mathbf{C}(\\theta) \\mathbf{D}(\\phi)$ transforms space coordinates into body coordinates.\n\n<h4>2. Angular Velocity Vector in Terms of Euler Angles</h4>\nProjecting the rates of change $(\\dot{\\phi}, \\dot{\\theta}, \\dot{\\psi})$ onto the body-fixed axes $(x', y', z')$ yields the instantaneous angular velocity $\\vec{\\omega}$:\n<div class=\"math-display\">$$\\omega_{x'} = \\dot{\\phi} \\sin \\theta \\sin \\psi + \\dot{\\theta} \\cos \\psi$$</div>\n<div class=\"math-display\">$$\\omega_{y'} = \\dot{\\phi} \\sin \\theta \\cos \\psi - \\dot{\\theta} \\sin \\psi$$</div>\n<div class=\"math-display\">$$\\omega_{z'} = \\dot{\\phi} \\cos \\theta + \\dot{\\psi}$$</div>\n"
        },
        {
          "id": "u4-sec3",
          "title": "The Inertia Tensor, Dyadics & Principal Axes of Inertia",
          "content": "\n<h4>1. Angular Momentum and the Inertia Tensor</h4>\nFor a rigid body rotating with instantaneous angular velocity $\\vec{\\omega}$ about a fixed point (or about its center of mass), the velocity of each point mass is $\\vec{v}_i = \\vec{\\omega} \\times \\vec{r}_i$. The total angular momentum is:\n<div class=\"math-display\">$$\\vec{L} = \\sum_{i=1}^N m_i \\vec{r}_i \\times (\\vec{\\omega} \\times \\vec{r}_i) = \\sum_{i=1}^N m_i [r_i^2 \\vec{\\omega} - (\\vec{r}_i \\cdot \\vec{\\omega})\\vec{r}_i]$$</div>\nIn component notation, this linear relationship is written as $\\vec{L} = \\mathbf{I} \\vec{\\omega}$:\n<div class=\"math-display\">$$L_j = \\sum_{k=1}^3 I_{jk} \\omega_k$$</div>\nwhere $\\mathbf{I}$ is the rank-2 symmetric <strong>inertia tensor</strong>:\n<div class=\"math-display\">$$I_{jk} = \\int \\rho(\\vec{r}) (r^2 \\delta_{jk} - x_j x_k) dV$$</div>\nThe diagonal components are the <strong>moments of inertia</strong>:\n<div class=\"math-display\">$$I_{xx} = \\int (y^2 + z^2) dm, \\quad I_{yy} = \\int (x^2 + z^2) dm, \\quad I_{zz} = \\int (x^2 + y^2) dm$$</div>\nThe off-diagonal components are the <strong>products of inertia</strong>:\n<div class=\"math-display\">$$I_{xy} = I_{yx} = -\\int x y dm, \\quad I_{yz} = I_{zy} = -\\int y z dm, \\quad I_{xz} = I_{zx} = -\\int x z dm$$</div>\n\n<h4>2. Rotational Kinetic Energy</h4>\nThe rotational kinetic energy is a quadratic form in angular velocities:\n<div class=\"math-display\">$$T_{\\text{rot}} = \\frac{1}{2} \\sum_{i=1}^N m_i v_i^2 = \\frac{1}{2} \\vec{\\omega} \\cdot \\vec{L} = \\frac{1}{2} \\sum_{j=1}^3 \\sum_{k=1}^3 I_{jk} \\omega_j \\omega_k = \\frac{1}{2} \\vec{\\omega}^T \\mathbf{I} \\vec{\\omega}$$</div>\n\n<h4>3. Principal Axes of Inertia & Diagonalization</h4>\nBecause the inertia matrix $\\mathbf{I}$ is real and symmetric, the spectral theorem guarantees the existence of an orthogonal basis of eigenvectors called the <strong>principal axes of inertia</strong>. In this frame, all products of inertia vanish, and $\\mathbf{I}$ becomes purely diagonal:\n<div class=\"math-display\">$$\\mathbf{I} = \\begin{pmatrix} I_1 & 0 & 0 \\\\ 0 & I_2 & 0 \\\\ 0 & 0 & I_3 \\end{pmatrix}$$</div>\nwhere $I_1, I_2, I_3$ are the <strong>principal moments of inertia</strong>. The rotational kinetic energy and angular momentum simplify to:\n<div class=\"math-display\">$$T_{\\text{rot}} = \\frac{1}{2} I_1 \\omega_1^2 + \\frac{1}{2} I_2 \\omega_2^2 + \\frac{1}{2} I_3 \\omega_3^2$$</div>\n<div class=\"math-display\">$$\\vec{L} = I_1 \\omega_1 \\hat{e}_1 + I_2 \\omega_2 \\hat{e}_2 + I_3 \\omega_3 \\hat{e}_3$$</div>\n"
        },
        {
          "id": "u4-sec4",
          "title": "Euler's Equations of Motion for Rigid Bodies",
          "content": "\n<h4>1. Time Derivatives in Rotating Reference Frames</h4>\nLet an arbitrary vector $\\vec{G}$ be observed in both an inertial space-fixed frame and a body-fixed frame rotating with angular velocity $\\vec{\\omega}$. The operator relation between time rates of change is:\n<div class=\"math-display\">$$\\left(\\frac{d\\vec{G}}{dt}\\right)_{\\text{space}} = \\left(\\frac{d\\vec{G}}{dt}\\right)_{\\text{body}} + \\vec{\\omega} \\times \\vec{G}$$</div>\n\n<h4>2. Derivation of Euler's Dynamical Equations</h4>\nNewtonian mechanics requires that the rate of change of total angular momentum in the space frame equals the net external torque: $\\left(\\frac{d\\vec{L}}{dt}\\right)_{\\text{space}} = \\vec{N}^{\\text{ext}}$.\nApplying the rotating frame relation:\n<div class=\"math-display\">$$\\left(\\frac{d\\vec{L}}{dt}\\right)_{\\text{body}} + \\vec{\\omega} \\times \\vec{L} = \\vec{N}$$</div>\nExpressing this vector equation along the body's <strong>principal axes of inertia</strong> where $L_1 = I_1 \\omega_1$, $L_2 = I_2 \\omega_2$, $L_3 = I_3 \\omega_3$:\n<div class=\"math-display\">$$(\\vec{\\omega} \\times \\vec{L})_1 = \\omega_2 L_3 - \\omega_3 L_2 = (I_3 - I_2) \\omega_2 \\omega_3$$</div>\nThis yields <strong>Euler's Equations of Motion</strong>:\n<div class=\"math-display\">$$I_1 \\dot{\\omega}_1 - (I_2 - I_3) \\omega_2 \\omega_3 = N_1$$</div>\n<div class=\"math-display\">$$I_2 \\dot{\\omega}_2 - (I_3 - I_1) \\omega_3 \\omega_1 = N_2$$</div>\n<div class=\"math-display\">$$I_3 \\dot{\\omega}_3 - (I_1 - I_2) \\omega_1 \\omega_2 = N_3$$</div>\n<p>These coupled nonlinear first-order differential equations govern the time evolution of the body-fixed angular velocity components under external torques $N_i$.</p>\n",
          "simulation": "tennis-racket-sim"
        },
        {
          "id": "u4-sec5",
          "title": "Torque-Free Motion & The Heavy Symmetrical Top",
          "content": "\n<h4>1. Torque-Free Motion of a Symmetrical Top ($N_i = 0$, $I_1 = I_2 \\neq I_3$)</h4>\nSetting torques to zero and $I_1 = I_2$, Euler's equations become:\n<div class=\"math-display\">$$I_1 \\dot{\\omega}_1 = (I_1 - I_3) \\omega_2 \\omega_3$$</div>\n<div class=\"math-display\">$$I_1 \\dot{\\omega}_2 = -(I_1 - I_3) \\omega_1 \\omega_3$$</div>\n<div class=\"math-display\">$$I_3 \\dot{\\omega}_3 = 0 \\implies \\omega_3 = \\text{constant}$$</div>\nDefining the constant precession frequency $\\Omega_{\\text{prec}} = \\frac{I_1 - I_3}{I_1} \\omega_3$:\n<div class=\"math-display\">$$\\dot{\\omega}_1 = \\Omega_{\\text{prec}} \\omega_2, \\quad \\dot{\\omega}_2 = -\\Omega_{\\text{prec}} \\omega_1$$</div>\nDifferentiating again yields $\\ddot{\\omega}_1 + \\Omega_{\\text{prec}}^2 \\omega_1 = 0$. The angular velocity vector $\\vec{\\omega}$ precesses uniformly around the body symmetry axis ($z'$) with frequency $\\Omega_{\\text{prec}}$.\n\n<h4>2. The Heavy Symmetrical Top with Fixed Pivot</h4>\nConsider a symmetric top ($I_1 = I_2$) spinning under gravity with its apex supported at a fixed pivot. The Lagrangian in Eulerian angles $(\\phi, \\theta, \\psi)$ is:\n<div class=\"math-display\">$$L = \\frac{1}{2}I_1 (\\dot{\\theta}^2 + \\dot{\\phi}^2 \\sin^2 \\theta) + \\frac{1}{2}I_3 (\\dot{\\phi} \\cos \\theta + \\dot{\\psi})^2 - M g l \\cos \\theta$$</div>\nCoordinates $\\phi$ (precession) and $\\psi$ (spin) are cyclic:\n<div class=\"math-display\">$$p_\\phi = I_1 \\dot{\\phi} \\sin^2 \\theta + I_3 (\\dot{\\phi} \\cos \\theta + \\dot{\\psi}) \\cos \\theta = \\text{const}$$</div>\n<div class=\"math-display\">$$p_\\psi = I_3 (\\dot{\\phi} \\cos \\theta + \\dot{\\psi}) = I_3 \\omega_3 = \\text{const}$$</div>\nThe nutation angle $\\theta(t)$ oscillates between two turning points $\\theta_1$ and $\\theta_2$ governed by an effective potential.\n\n<h4>3. The Sleeping Top Stability Condition</h4>\nWhen a top spins vertically upright ($\\theta = 0$, the \"sleeping top\"), small perturbations are stable if and only if the spin angular velocity exceeds the critical threshold:\n<div class=\"math-display\">$$\\omega_3^2 \\ge \\frac{4 M g l I_1}{I_3^2}$$</div>\nIf friction slows $\\omega_3$ below this limit, the vertical state undergoes a bifurcation and the top begins to wobble (nutate) wildly.\n",
          "simulation": "euler-top-sim"
        }
      ],
      "problems": [
        {
          "id": "cm-prob-4-1",
          "title": "Principal Moments of Inertia of a Uniform Solid Cube",
          "statement": "Find the inertia tensor of a uniform solid cube of mass $M$ and edge length $a$ about one of its corners as origin, and determine the principal moments of inertia and the orientation of the principal axes.",
          "steps": [
            {
              "step": "Step 1: Calculate Moments and Products of Inertia About Corner Origin",
              "math": "$$I_{xx} = \\int_0^a dx \\int_0^a dy \\int_0^a dz \\rho (y^2 + z^2) = \\frac{M}{a^3} \\left( \\frac{a^5}{3} + \\frac{a^5}{3} \\right) = \\frac{2}{3} M a^2$$",
              "explanation": "By symmetry, $I_{xx} = I_{yy} = I_{zz} = \\frac{2}{3} M a^2$. The product of inertia is $I_{xy} = -\\int_0^a dx \\int_0^a dy \\int_0^a dz \\rho x y = -\\frac{M}{a^3} \\left(\\frac{a^2}{2}\\right)\\left(\\frac{a^2}{2}\\right) a = -\\frac{1}{4} M a^2$."
            },
            {
              "step": "Step 2: Construct the Full Inertia Matrix",
              "math": "$$\\mathbf{I} = M a^2 \\begin{pmatrix} 2/3 & -1/4 & -1/4 \\\\ -1/4 & 2/3 & -1/4 \\\\ -1/4 & -1/4 & 2/3 \\end{pmatrix}$$",
              "explanation": "All diagonal elements are $2/3 M a^2$ and all off-diagonal products of inertia are $-1/4 M a^2$."
            },
            {
              "step": "Step 3: Diagonalize the Matrix to Extract Principal Moments",
              "math": "$$\\det(\\mathbf{I} - \\lambda \\mathbf{I}_3) = 0 \\implies \\lambda_1 = \\frac{1}{6} M a^2, \\quad \\lambda_2 = \\lambda_3 = \\frac{11}{12} M a^2$$",
              "explanation": "The eigenvector for $\\lambda_1 = \\frac{1}{6} M a^2$ points along the main space diagonal $(1, 1, 1)^T$. The other two degenerate eigenvalues $\\frac{11}{12} M a^2$ correspond to any orthogonal vectors in the plane perpendicular to the main diagonal."
            }
          ],
          "answer": "Principal moments: I1 = (1/6) M a² (along space diagonal), I2 = I3 = (11/12) M a² (degenerate perpendicular plane)."
        },
        {
          "id": "cm-prob-4-2",
          "title": "Euler's Equations: Intermediate Axis Instability (Tennis Racket Theorem)",
          "statement": "An asymmetric rigid body with principal moments of inertia $I_1 < I_2 < I_3$ undergoes torque-free rotation. Use Euler's equations and linear stability analysis to prove that steady rotation about the intermediate axis $I_2$ is dynamically unstable, while rotation about $I_1$ and $I_3$ is stable.",
          "steps": [
            {
              "step": "Step 1: Perturb Motion Around the Intermediate Axis 2",
              "math": "$$\\vec{\\omega} = (\\eta_1, \\omega_0 + \\eta_2, \\eta_3), \\quad |\\eta_i| \\ll \\omega_0$$",
              "explanation": "Let the body rotate steadily around principal axis 2 with nominal velocity $\\omega_0$, with small perturbations $\\eta_1, \\eta_2, \\eta_3$."
            },
            {
              "step": "Step 2: Linearize Euler's Equations to First Order in Perturbations",
              "math": "$$I_1 \\dot{\\eta}_1 = (I_2 - I_3) \\omega_0 \\eta_3, \\quad I_3 \\dot{\\eta}_3 = (I_1 - I_2) \\omega_0 \\eta_1$$",
              "explanation": "To first order, $\\dot{\\eta}_2 = 0$. Differentiating the first equation: $I_1 \\ddot{\\eta}_1 = (I_2 - I_3) \\omega_0 \\dot{\\eta}_3 = \\frac{(I_2 - I_3)(I_1 - I_2)}{I_3} \\omega_0^2 \\eta_1$."
            },
            {
              "step": "Step 3: Evaluate Sign of the Coefficient",
              "math": "$$\\ddot{\\eta}_1 = \\frac{(I_2 - I_3)(I_1 - I_2)}{I_1 I_3} \\omega_0^2 \\eta_1 = +\\Omega^2 \\eta_1$$",
              "explanation": "Since $I_1 < I_2 < I_3$, $(I_2 - I_3) < 0$ and $(I_1 - I_2) < 0$, making their product strictly POSITIVE. The perturbation grows exponentially as $\\eta_1(t) \\propto e^{+\\Omega t}$, proving instability. (For axes 1 or 3, the product is negative, giving stable harmonic oscillation $\\ddot{\\eta} = -\\Omega^2 \\eta$)."
            }
          ],
          "answer": "Exponential growth rate Ω = ω0 √[(I3 - I2)(I2 - I1) / (I1 I3)] proves the intermediate axis is violently unstable (Dzhanibekov effect)."
        },
        {
          "id": "cm-prob-4-3",
          "title": "Steady Precession Rate of a Fast Heavy Symmetrical Top",
          "statement": "A heavy symmetrical top ($I_1 = I_2$, $I_3$) spins with large angular velocity $\\omega_3$ about its symmetry axis inclined at angle $\\theta$ to the vertical. Derive the slow and fast steady precession rates $\\dot{\\phi}$ from the torque-free balance equation.",
          "steps": [
            {
              "step": "Step 1: Set Up the Nutational Force Balance Equation",
              "math": "$$I_1 \\ddot{\\theta} = I_1 \\dot{\\phi}^2 \\sin \\theta \\cos \\theta - I_3 \\omega_3 \\dot{\\phi} \\sin \\theta + M g l \\sin \\theta = 0$$",
              "explanation": "For steady precession, nutation is fixed ($\\dot{\\theta} = 0, \\ddot{\\theta} = 0$). Dividing by $\\sin \\theta$ (assuming $\\sin \\theta \\neq 0$) yields a quadratic equation for precession speed $\\dot{\\phi}$."
            },
            {
              "step": "Step 2: Solve Quadratic Equation for Precession Speed φ̇",
              "math": "$$I_1 \\cos \\theta \\dot{\\phi}^2 - I_3 \\omega_3 \\dot{\\phi} + M g l = 0$$",
              "explanation": "The roots are $\\dot{\\phi} = \\frac{I_3 \\omega_3 \\pm \\sqrt{I_3^2 \\omega_3^2 - 4 I_1 M g l \\cos \\theta}}{2 I_1 \\cos \\theta}$."
            },
            {
              "step": "Step 3: Extract the Fast and Slow Precession Limits for Large Spin ω3",
              "math": "$$\\dot{\\phi}_{\\text{slow}} \\approx \\frac{M g l}{I_3 \\omega_3}, \\quad \\dot{\\phi}_{\\text{fast}} \\approx \\frac{I_3 \\omega_3}{I_1 \\cos \\theta}$$",
              "explanation": "Expanding the square root for $I_3^2 \\omega_3^2 \\gg 4 I_1 M g l \\cos \\theta$: the minus sign gives the ordinary slow gyroscopic precession $\\dot{\\phi} = \\tau / L$, and the plus sign gives the fast inertial precession."
            }
          ],
          "answer": "Slow steady precession: φ̇_slow = M g l / (I3 ω3); Fast precession: φ̇_fast = I3 ω3 / (I1 cos θ)."
        }
      ],
      "id": "unit-4"
    },
    {
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
          "content": "\n<h4>1. Limitations of the Lagrangian Framework</h4>\nIn the Lagrangian formulation, a dynamical system of $n$ degrees of freedom is described in an $n$-dimensional <strong>configuration space</strong> spanned by generalized coordinates $(q_1, \\dots, q_n)$. The equations of motion:\n<div class=\"math-display\">$$\\frac{d}{dt}\\left( \\frac{\\partial L}{\\partial \\dot{q}_j} \\right) - \\frac{\\partial L}{\\partial q_j} = 0, \\quad j = 1, \\dots, n$$</div>\nconstitute a set of $n$ coupled <strong>second-order differential equations</strong>. Specifying a unique dynamical trajectory requires $2n$ initial boundary conditions: initial positions $q_j(0)$ and initial velocities $\\dot{q}_j(0)$. However, generalized velocities $\\dot{q}_j$ are not independent state variables—they are geometric tangents to the trajectory.\n\n<h4>2. The 2n-Dimensional Phase Space</h4>\nIn 1835, Sir William Rowan Hamilton developed a symmetric reformulation by replacing the $n$ generalized velocities $\\dot{q}_j$ with $n$ <strong>canonical conjugate momenta</strong> $p_j$:\n<div class=\"math-display\">$$p_j = \\frac{\\partial L}{\\partial \\dot{q}_j}(q, \\dot{q}, t)$$</div>\nThe state of the system is now mapped as a single point in a <strong>$2n$-dimensional phase space</strong> spanned by $2n$ independent coordinates:\n<div class=\"math-display\">$$(q_1, \\dots, q_n; p_1, \\dots, p_n) \\in \\mathbb{R}^{2n}$$</div>\nInstead of $n$ second-order differential equations, Hamiltonian dynamics governs motion through a system of <strong>$2n$ first-order differential equations</strong>, displaying complete mathematical symmetry between positions and momenta.\n",
          "simulation": "phase-space-oscillator-sim"
        },
        {
          "id": "u5-sec2",
          "title": "The Legendre Transformation & Derivation of Hamilton's Equations",
          "content": "\n<h4>1. The Mathematical Legendre Transformation</h4>\nConsider the total differential of the Lagrangian $L(q, \\dot{q}, t)$:\n<div class=\"math-display\">$$dL = \\sum_{j=1}^n \\frac{\\partial L}{\\partial q_j} dq_j + \\sum_{j=1}^n \\frac{\\partial L}{\\partial \\dot{q}_j} d\\dot{q}_j + \\frac{\\partial L}{\\partial t} dt = \\sum_{j=1}^n \\dot{p}_j dq_j + \\sum_{j=1}^n p_j d\\dot{q}_j + \\frac{\\partial L}{\\partial t} dt$$</div>\nwhere we used $p_j = \\frac{\\partial L}{\\partial \\dot{q}_j}$ and Lagrange's equations $\\dot{p}_j = \\frac{\\partial L}{\\partial q_j}$.\nTo transform the active variable from $\\dot{q}_j$ to $p_j$, we perform a <strong>Legendre transformation</strong> by subtracting the differential $d\\left( \\sum_{j=1}^n p_j \\dot{q}_j \\right)$:\n<div class=\"math-display\">$$d\\left( \\sum_{j=1}^n p_j \\dot{q}_j - L \\right) = \\sum_{j=1}^n \\dot{q}_j dp_j + \\sum_{j=1}^n p_j d\\dot{q}_j - dL = \\sum_{j=1}^n \\dot{q}_j dp_j - \\sum_{j=1}^n \\dot{p}_j dq_j - \\frac{\\partial L}{\\partial t} dt$$</div>\n\n<h4>2. Definition of the Hamiltonian Function $H$</h4>\nWe define the <strong>Hamiltonian function</strong> $H(q, p, t)$ by the Legendre transform:\n<div class=\"math-display\">$$H(q, p, t) = \\sum_{j=1}^n p_j \\dot{q}_j - L(q, \\dot{q}, t)$$</div>\nwhere all occurrences of $\\dot{q}_j$ must be inverted algebraically in terms of $q, p, t$. The exact total differential of $H(q, p, t)$ as a function of its natural canonical variables is:\n<div class=\"math-display\">$$dH = \\sum_{j=1}^n \\frac{\\partial H}{\\partial q_j} dq_j + \\sum_{j=1}^n \\frac{\\partial H}{\\partial p_j} dp_j + \\frac{\\partial H}{\\partial t} dt$$</div>\n\n<h4>3. Hamilton's Canonical Equations of Motion</h4>\nEquating coefficients of the independent differentials $dq_j, dp_j, dt$:\n<div class=\"math-display\">$$\\dot{q}_j = \\frac{\\partial H}{\\partial p_j}, \\quad \\dot{p}_j = -\\frac{\\partial H}{\\partial q_j}, \\quad j = 1, 2, \\dots, n$$</div>\ntogether with the partial time derivative identity:\n<div class=\"math-display\">$$\\frac{\\partial H}{\\partial t} = -\\frac{\\partial L}{\\partial t}$$</div>\n<p>These $2n$ coupled equations are known as <strong>Hamilton's Canonical Equations of Motion</strong>.</p>\n"
        },
        {
          "id": "u5-sec3",
          "title": "Physical Meaning of the Hamiltonian & Energy Conservation",
          "content": "\n<h4>1. Total Time Derivative of the Hamiltonian</h4>\nDifferentiating $H(q(t), p(t), t)$ along a physical dynamical trajectory:\n<div class=\"math-display\">$$\\frac{dH}{dt} = \\sum_{j=1}^n \\left( \\frac{\\partial H}{\\partial q_j} \\dot{q}_j + \\frac{\\partial H}{\\partial p_j} \\dot{p}_j \\right) + \\frac{\\partial H}{\\partial t}$$</div>\nSubstituting Hamilton's canonical equations:\n<div class=\"math-display\">$$\\frac{dH}{dt} = \\sum_{j=1}^n \\left( -\\dot{p}_j \\dot{q}_j + \\dot{q}_j \\dot{p}_j \\right) + \\frac{\\partial H}{\\partial t} = \\frac{\\partial H}{\\partial t} = -\\frac{\\partial L}{\\partial t}$$</div>\n<p><strong>Conservation Theorem:</strong> If the Hamiltonian does not depend explicitly on time ($\\frac{\\partial H}{\\partial t} = 0$), then the Hamiltonian is a strict <strong>constant of motion</strong>: $H(q, p) = E = \\text{constant}$.</p>\n\n<h4>2. Condition Under Which $H$ Equals Total Mechanical Energy ($H = T + V$)</h4>\nRecall Euler's theorem for homogeneous functions. The kinetic energy $T$ is generally expressed as:\n<div class=\"math-display\">$$T = T_2 + T_1 + T_0$$</div>\nwhere $T_2 = \\frac{1}{2} \\sum_{j,k} m_{jk}(q) \\dot{q}_j \\dot{q}_k$ (quadratic in velocities), $T_1 = \\sum_j a_j(q) \\dot{q}_j$ (linear), and $T_0$ is independent of $\\dot{q}$.\nThe canonical momenta are $p_j = \\frac{\\partial T_2}{\\partial \\dot{q}_j} + a_j$. Then:\n<div class=\"math-display\">$$\\sum_{j=1}^n p_j \\dot{q}_j = 2 T_2 + T_1$$</div>\nThe Hamiltonian is:\n<div class=\"math-display\">$$H = \\sum_{j=1}^n p_j \\dot{q}_j - (T - V) = (2T_2 + T_1) - (T_2 + T_1 + T_0 - V) = T_2 - T_0 + V$$</div>\nTherefore, $H = T + V = E$ if and only if two conditions are met simultaneously:\n<ol>\n  <li>The transformation equations $\\vec{r}_i = \\vec{r}_i(q)$ are <strong>scleronomic</strong> (no explicit time dependence $\\frac{\\partial \\vec{r}_i}{\\partial t} = 0$), which makes $T_1 = 0$ and $T_0 = 0$.</li>\n  <li>The potential energy $V = V(q)$ is independent of velocities $\\dot{q}$.</li>\n</ol>\n"
        },
        {
          "id": "u5-sec4",
          "title": "Variational Principles: Modified Hamilton's Principle & Least Action",
          "content": "\n<h4>1. Modified Hamilton's Principle in Phase Space</h4>\nIn configuration space, Hamilton's principle varies coordinates $q_j(t)$ with $\\delta q_j(t_1) = \\delta q_j(t_2) = 0$. In phase space, both $q_j(t)$ and $p_j(t)$ are treated as $2n$ independent path variables. Substituting $L = \\sum p_j \\dot{q}_j - H(q, p, t)$:\n<div class=\"math-display\">$$\\delta \\int_{t_1}^{t_2} \\left( \\sum_{j=1}^n p_j \\dot{q}_j - H(q, p, t) \\right) dt = 0$$</div>\nCarrying out independent variations $\\delta q_j$ and $\\delta p_j$:\n<div class=\"math-display\">$$\\int_{t_1}^{t_2} \\sum_{j=1}^n \\left[ \\delta p_j \\dot{q}_j + p_j \\frac{d}{dt}(\\delta q_j) - \\frac{\\partial H}{\\partial q_j} \\delta q_j - \\frac{\\partial H}{\\partial p_j} \\delta p_j \\right] dt = 0$$</div>\nIntegrating $p_j \\frac{d}{dt}(\\delta q_j)$ by parts with fixed coordinate endpoints $\\delta q_j(t_1) = \\delta q_j(t_2) = 0$ (note that endpoint variations $\\delta p_j$ are unconstrained):\n<div class=\"math-display\">$$\\int_{t_1}^{t_2} \\sum_{j=1}^n \\left[ \\left( \\dot{q}_j - \\frac{\\partial H}{\\partial p_j} \\right) \\delta p_j - \\left( \\dot{p}_j + \\frac{\\partial H}{\\partial q_j} \\right) \\delta q_j \\right] dt = 0$$</div>\nBecause $\\delta q_j$ and $\\delta p_j$ are completely independent, their coefficients must vanish individually, reproducing Hamilton's equations.\n\n<h4>2. Maupertuis' Principle of Least Action</h4>\nFor conservative systems ($H = E = \\text{const}$), Pierre Louis Maupertuis (1744) formulated an abbreviated variational principle where time is not held fixed at endpoints ($\\Delta t \\neq 0$). The <strong>abbreviated action</strong> $S_0$ is defined as:\n<div class=\"math-display\">$$S_0 = \\int_{q^{(1)}}^{q^{(2)}} \\sum_{j=1}^n p_j dq_j = \\int_{t_1}^{t_2} 2 T dt$$</div>\n<p><strong>Maupertuis' Principle:</strong> For physical paths with constant total energy $E$, the varied path renders the abbreviated action stationary:</p>\n<div class=\"math-display\">$$\\Delta S_0 = \\Delta \\int \\sum_{j=1}^n p_j dq_j = 0$$</div>\nFor a single particle in a potential $V(\\vec{r})$ with mass $m$, $p = \\sqrt{2m(E - V)}$. The principle becomes:\n<div class=\"math-display\">$$\\delta \\int \\sqrt{2m(E - V(\\vec{r}))} ds = 0$$</div>\nThis is Jacobi's geometric form of the Principle of Least Action, showing that dynamical trajectories in potential fields are <strong>geodesics</strong> in a curved Riemannian space with metric $g_{ij} = 2m(E - V)\\delta_{ij}$, providing the classical mechanical analogue to Fermat's principle of least time in optics.\n"
        },
        {
          "id": "u5-sec5",
          "title": "Hamiltonian of a Charged Particle in an Electromagnetic Field",
          "content": "\n<h4>1. Construction of the Electromagnetic Hamiltonian</h4>\nRecall the velocity-dependent Lagrangian of a particle with charge $q$ and mass $m$ in potentials $(\\Phi, \\vec{A})$:\n<div class=\"math-display\">$$L = \\frac{1}{2}m \\vec{v}^2 - q\\Phi + q \\vec{v} \\cdot \\vec{A}$$</div>\nThe canonical momentum $\\vec{p}$ conjugate to position $\\vec{r}$ is:\n<div class=\"math-display\">$$\\vec{p} = \\frac{\\partial L}{\\partial \\vec{v}} = m \\vec{v} + q \\vec{A}$$</div>\nNotice that canonical momentum $\\vec{p}$ differs fundamentally from kinematic mechanical momentum $m \\vec{v}$:\n<div class=\"math-display\">$$m \\vec{v} = \\vec{p} - q \\vec{A}$$</div>\nInverting for velocity: $\\vec{v} = \\frac{1}{m}(\\vec{p} - q\\vec{A})$.\nApplying the Legendre transformation:\n<div class=\"math-display\">$$H = \\vec{p} \\cdot \\vec{v} - L = \\vec{p} \\cdot \\vec{v} - \\left( \\frac{1}{2}m v^2 - q\\Phi + q \\vec{v} \\cdot \\vec{A} \\right) = \\vec{v} \\cdot (\\vec{p} - q\\vec{A}) - \\frac{1}{2}m v^2 + q\\Phi$$</div>\nSubstituting $\\vec{v} = \\frac{1}{m}(\\vec{p} - q\\vec{A})$:\n<div class=\"math-display\">$$H(\\vec{r}, \\vec{p}, t) = \\frac{1}{2m} (\\vec{p} - q\\vec{A}(\\vec{r}, t))^2 + q\\Phi(\\vec{r}, t)$$</div>\n\n<h4>2. Hamilton's Equations for the Charged Particle</h4>\n<div class=\"math-display\">$$\\dot{\\vec{r}} = \\nabla_p H = \\frac{1}{m}(\\vec{p} - q\\vec{A})$$</div>\n<div class=\"math-display\">$$\\dot{\\vec{p}} = -\\nabla_r H = -q \\nabla \\Phi + \\frac{q}{m} \\sum_{j=1}^3 (p_j - q A_j) \\nabla A_j$$</div>\nSubstituting $\\vec{p} = m \\dot{\\vec{r}} + q \\vec{A}$ recovers the complete Lorentz force law $m \\ddot{\\vec{r}} = q(\\vec{E} + \\dot{\\vec{r}} \\times \\vec{B})$, proving exact equivalence.\n"
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
      ],
      "id": "unit-5"
    },
    {
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
          "content": "\n<h4>1. Motivation for Coordinate Transformations in Phase Space</h4>\nIn Lagrangian mechanics, coordinate transformations are restricted to point transformations $Q_i = Q_i(q, t)$. In Hamiltonian mechanics, coordinates and conjugate momenta $(q, p)$ are treated on an equal footing. We consider broader transformations:\n<div class=\"math-display\">$$Q_i = Q_i(q, p, t), \\quad P_i = P_i(q, p, t), \\quad i = 1, 2, \\dots, n$$</div>\nA transformation is defined as <strong>canonical</strong> (or contact) if there exists a new Hamiltonian $K(Q, P, t)$ such that the new variables satisfy Hamilton's canonical equations:\n<div class=\"math-display\">$$\\dot{Q}_i = \\frac{\\partial K}{\\partial P_i}, \\quad \\dot{P}_i = -\\frac{\\partial K}{\\partial Q_i}$$</div>\n\n<h4>2. Variational Condition & Generating Function</h4>\nBoth original and transformed trajectories must satisfy the modified Hamilton's principle:\n<div class=\"math-display\">$$\\delta \\int_{t_1}^{t_2} \\left( \\sum_{i=1}^n p_i \\dot{q}_i - H(q, p, t) \\right) dt = 0, \\quad \\delta \\int_{t_1}^{t_2} \\left( \\sum_{i=1}^n P_i \\dot{Q}_i - K(Q, P, t) \\right) dt = 0$$</div>\nThe two integrands can differ at most by the exact total time derivative of an arbitrary function $F$, called the <strong>generating function</strong>:\n<div class=\"math-display\">$$\\sum_{i=1}^n p_i \\dot{q}_i - H = \\sum_{i=1}^n P_i \\dot{Q}_i - K + \\frac{dF}{dt}$$</div>\nMultiplying by $dt$:\n<div class=\"math-display\">$$\\sum_{i=1}^n p_i dq_i - H dt = \\sum_{i=1}^n P_i dQ_i - K dt + dF$$</div>\n\n<h4>3. The Symplectic Condition</h4>\nDefining the $2n$-dimensional phase vector $\\mathbf{\\eta} = (q_1, \\dots, q_n, p_1, \\dots, p_n)^T$ and the fundamental symplectic matrix $\\mathbf{J}$:\n<div class=\"math-display\">$$\\mathbf{J} = \\begin{pmatrix} \\mathbf{0} & \\mathbf{I}_n \\\\ -\\mathbf{I}_n & \\mathbf{0} \\end{pmatrix}, \\quad \\mathbf{J}^T = -\\mathbf{J}, \\quad \\mathbf{J}^2 = -\\mathbf{I}_{2n}$$</div>\nLet $\\mathbf{M}$ be the Jacobian matrix of the transformation $M_{ij} = \\frac{\\partial \\zeta_i}{\\partial \\eta_j}$ where $\\mathbf{\\zeta} = (Q, P)^T$. The transformation is canonical if and only if $\\mathbf{M}$ satisfies the <strong>symplectic condition</strong>:\n<div class=\"math-display\">$$\\mathbf{M}^T \\mathbf{J} \\mathbf{M} = \\mathbf{J}$$</div>\nTaking the determinant yields $(\\det \\mathbf{M})^2 = 1 \\implies \\det \\mathbf{M} = 1$, proving that phase space volume is strictly preserved.\n"
        },
        {
          "id": "u6-sec2",
          "title": "The Four Fundamental Classes of Generating Functions",
          "content": "\n<h4>1. Classification by Active Canonical Variables</h4>\nDepending on which pair of old and new variables are chosen as independent variables, Legendre transformations yield four primary classes of generating functions:\n<ol>\n  <li><strong>Type 1: $F_1(q, Q, t)$</strong>\n  <div class=\"math-display\">$$dF_1 = \\sum_i p_i dq_i - \\sum_i P_i dQ_i + (K - H) dt$$</div>\n  Equating partial differentials:\n  <div class=\"math-display\">$$p_i = \\frac{\\partial F_1}{\\partial q_i}, \\quad P_i = -\\frac{\\partial F_1}{\\partial Q_i}, \\quad K = H + \\frac{\\partial F_1}{\\partial t}$$</div></li>\n\n  <li><strong>Type 2: $F_2(q, P, t) = F_1 + \\sum_i P_i Q_i$</strong>\n  <div class=\"math-display\">$$dF_2 = \\sum_i p_i dq_i + \\sum_i Q_i dP_i + (K - H) dt$$</div>\n  Transformation relations:\n  <div class=\"math-display\">$$p_i = \\frac{\\partial F_2}{\\partial q_i}, \\quad Q_i = \\frac{\\partial F_2}{\\partial P_i}, \\quad K = H + \\frac{\\partial F_2}{\\partial t}$$</div>\n  <p><em>Example:</em> The identity transformation is generated by $F_2 = \\sum_i q_i P_i$, giving $p_i = P_i$ and $Q_i = q_i$.</p></li>\n\n  <li><strong>Type 3: $F_3(p, Q, t) = F_1 - \\sum_i p_i q_i$</strong>\n  <div class=\"math-display\">$$dF_3 = -\\sum_i q_i dp_i - \\sum_i P_i dQ_i + (K - H) dt$$</div>\n  Transformation relations:\n  <div class=\"math-display\">$$q_i = -\\frac{\\partial F_3}{\\partial p_i}, \\quad P_i = -\\frac{\\partial F_3}{\\partial Q_i}, \\quad K = H + \\frac{\\partial F_3}{\\partial t}$$</div></li>\n\n  <li><strong>Type 4: $F_4(p, P, t) = F_1 - \\sum_i p_i q_i + \\sum_i P_i Q_i$</strong>\n  <div class=\"math-display\">$$dF_4 = -\\sum_i q_i dp_i + \\sum_i Q_i dP_i + (K - H) dt$$</div>\n  Transformation relations:\n  <div class=\"math-display\">$$q_i = -\\frac{\\partial F_4}{\\partial p_i}, \\quad Q_i = \\frac{\\partial F_4}{\\partial P_i}, \\quad K = H + \\frac{\\partial F_4}{\\partial t}$$</div></li>\n</ol>\n"
        },
        {
          "id": "u6-sec3",
          "title": "Poisson Brackets: Definition, Properties & Lie Algebra",
          "content": "\n<h4>1. Definition of the Poisson Bracket</h4>\nLet $u(q, p, t)$ and $v(q, p, t)$ be two continuously differentiable functions defined on phase space. The <strong>Poisson bracket</strong> $[u, v]_{q,p}$ with respect to canonical variables $(q, p)$ is:\n<div class=\"math-display\">$$\\{u, v\\}_{q,p} = \\sum_{j=1}^n \\left( \\frac{\\partial u}{\\partial q_j} \\frac{\\partial v}{\\partial p_j} - \\frac{\\partial u}{\\partial p_j} \\frac{\\partial v}{\\partial q_j} \\right)$$</div>\n\n<h4>2. Fundamental Algebraic Identities</h4>\nPoisson brackets satisfy the defining axioms of a <strong>Lie algebra</strong>:\n<ol>\n  <li><strong>Anti-Symmetry:</strong> $\\{u, v\\} = -\\{v, u\\} \\implies \\{u, u\\} = 0$.</li>\n  <li><strong>Bilinearity:</strong> $\\{a u + b v, w\\} = a\\{u, w\\} + b\\{v, w\\}$ for scalars $a, b$.</li>\n  <li><strong>Leibniz Product Rule:</strong> $\\{u v, w\\} = u\\{v, w\\} + \\{u, w\\}v$.</li>\n  <li><strong>The Jacobi Identity:</strong>\n  <div class=\"math-display\">$$\\{u, \\{v, w\\}\\} + \\{v, \\{w, u\\}\\} + \\{w, \\{u, v\\}\\} = 0$$</div></li>\n</ol>\n\n<h4>3. Fundamental Canonical Poisson Brackets</h4>\nEvaluating the brackets for the fundamental coordinates and conjugate momenta yields:\n<div class=\"math-display\">$$\\{q_j, q_k\\} = 0, \\quad \\{p_j, p_k\\} = 0, \\quad \\{q_j, p_k\\} = \\delta_{jk}$$</div>\n<p><strong>Canonical Invariance:</strong> A transformation $(q, p) \\to (Q, P)$ is canonical if and only if it preserves the fundamental Poisson brackets: $\\{Q_j, Q_k\\}_{q,p} = 0$, $\\{P_j, P_k\\}_{q,p} = 0$, and $\\{Q_j, P_k\\}_{q,p} = \\delta_{jk}$.</p>\n<p><em>Quantum Correspondence:</em> Paul Dirac recognized that the quantum commutator $[\\hat{u}, \\hat{v}]$ directly maps to the classical Poisson bracket: $[\\hat{u}, \\hat{v}] = i \\hbar \\{u, v\\}$.</p>\n"
        },
        {
          "id": "u6-sec4",
          "title": "Equations of Motion in Poisson Bracket Notation & Poisson's Theorem",
          "content": "\n<h4>1. Time Evolution of an Arbitrary Phase Space Observable</h4>\nLet $f(q, p, t)$ be any dynamical variable. Its total time derivative along a trajectory is:\n<div class=\"math-display\">$$\\frac{df}{dt} = \\sum_{j=1}^n \\left( \\frac{\\partial f}{\\partial q_j} \\dot{q}_j + \\frac{\\partial f}{\\partial p_j} \\dot{p}_j \\right) + \\frac{\\partial f}{\\partial t}$$</div>\nSubstituting Hamilton's equations $\\dot{q}_j = \\frac{\\partial H}{\\partial p_j}$ and $\\dot{p}_j = -\\frac{\\partial H}{\\partial q_j}$:\n<div class=\"math-display\">$$\\frac{df}{dt} = \\sum_{j=1}^n \\left( \\frac{\\partial f}{\\partial q_j} \\frac{\\partial H}{\\partial p_j} - \\frac{\\partial f}{\\partial p_j} \\frac{\\partial H}{\\partial q_j} \\right) + \\frac{\\partial f}{\\partial t}$$</div>\nRecognizing the Poisson bracket with the Hamiltonian:\n<div class=\"math-display\">$$\\frac{df}{dt} = \\{f, H\\} + \\frac{\\partial f}{\\partial t}$$</div>\n<p>This is the master equation of classical Hamiltonian dynamics. Setting $f = q_j$ and $f = p_j$ automatically reproduces Hamilton's equations $\\dot{q}_j = \\{q_j, H\\}$ and $\\dot{p}_j = \\{p_j, H\\}$.</p>\n\n<h4>2. First Integrals & Constants of Motion</h4>\nIf an observable $f(q, p)$ has no explicit time dependence ($\\frac{\\partial f}{\\partial t} = 0$), then $f$ is a <strong>constant of motion</strong> if and only if its Poisson bracket with the Hamiltonian vanishes:\n<div class=\"math-display\">$$\\frac{df}{dt} = 0 \\iff \\{f, H\\} = 0$$</div>\n\n<h4>3. Poisson's Theorem for Generating New Conserved Quantities</h4>\n<p><strong>Poisson's Theorem:</strong> If $f(q, p)$ and $g(q, p)$ are two independent constants of motion (so that $\\{f, H\\} = 0$ and $\\{g, H\\} = 0$), then their Poisson bracket $\\{f, g\\}$ is also a constant of motion.</p>\nProof via the Jacobi identity:\n<div class=\"math-display\">$$\\{\\{f, g\\}, H\\} = -\\{\\{g, H\\}, f\\} - \\{\\{H, f\\}, g\\} = -\\{0, f\\} - \\{0, g\\} = 0$$</div>\nHence $\\frac{d}{dt}\\{f, g\\} = 0$. Poisson's theorem enables systematically discovering new symmetries and conservation laws.\n"
        },
        {
          "id": "u6-sec5",
          "title": "Poincaré's Invariants & Liouville's Phase Volume Theorem",
          "content": "\n<h4>1. Poincaré's Integral Invariants</h4>\nHenri Poincaré proved that certain differential forms integrated over closed submanifolds in phase space remain invariant under canonical transformations and Hamiltonian time evolution.\nThe <strong>first Poincaré integral invariant</strong> of order 1 is:\n<div class=\"math-display\">$$J_1 = \\oint_C \\sum_{i=1}^n p_i dq_i = \\text{constant in time}$$</div>\nwhere $C$ is any closed circuit in phase space carried along by the Hamiltonian flow.\nHigher-order invariants $J_2, \\dots, J_n$ correspond to integrals over $2k$-dimensional manifolds. The invariant of maximum order $2n$ represents the total volume of phase space.\n\n<h4>2. Liouville's Phase Volume Conservation Theorem</h4>\nConsider an ensemble of non-interacting identical systems represented by a cloud of phase points with density distribution $\\rho(q, p, t)$ in $2n$-dimensional phase space.\nBy the continuity equation for probability conservation:\n<div class=\"math-display\">$$\\frac{\\partial \\rho}{\\partial t} + \\sum_{j=1}^n \\left( \\frac{\\partial (\\rho \\dot{q}_j)}{\\partial q_j} + \\frac{\\partial (\\rho \\dot{p}_j)}{\\partial p_j} \\right) = 0$$</div>\nExpanding the derivatives:\n<div class=\"math-display\">$$\\frac{\\partial \\rho}{\\partial t} + \\sum_{j=1}^n \\left( \\frac{\\partial \\rho}{\\partial q_j} \\dot{q}_j + \\frac{\\partial \\rho}{\\partial p_j} \\dot{p}_j \\right) + \\rho \\sum_{j=1}^n \\left( \\frac{\\partial \\dot{q}_j}{\\partial q_j} + \\frac{\\partial \\dot{p}_j}{\\partial p_j} \\right) = 0$$</div>\nUsing Hamilton's canonical equations:\n<div class=\"math-display\">$$\\frac{\\partial \\dot{q}_j}{\\partial q_j} + \\frac{\\partial \\dot{p}_j}{\\partial p_j} = \\frac{\\partial}{\\partial q_j}\\left( \\frac{\\partial H}{\\partial p_j} \\right) + \\frac{\\partial}{\\partial p_j}\\left( -\\frac{\\partial H}{\\partial q_j} \\right) = \\frac{\\partial^2 H}{\\partial q_j \\partial p_j} - \\frac{\\partial^2 H}{\\partial p_j \\partial q_j} = 0$$</div>\nThe divergence of phase velocity vanishes identically: $\\nabla \\cdot \\vec{v}_{\\text{phase}} = 0$ (the phase flow is strictly incompressible).\nConsequently, the convective total time derivative vanishes:\n<div class=\"math-display\">$$\\frac{d\\rho}{dt} = \\frac{\\partial \\rho}{\\partial t} + \\{\\rho, H\\} = 0$$</div>\n<p><strong>Liouville's Theorem:</strong> The phase space volume $\\Gamma = \\int dq dp$ and the local phase space density $\\rho$ surrounding any moving system point remain strictly constant over time. Phase fluid flows like an incompressible liquid, preventing trajectories from ever crossing.</p>\n",
          "simulation": "poincare-section-sim"
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
          "statement": "Using the Cartesian definitions of orbital angular momentum components $L_x = y p_z - z p_y$, $L_y = z p_x - x p_z$, and $L_z = x p_y - y p_x$, compute the Poisson bracket $\\{L_x, L_y\\}$ and show that $\\{L^2, L_z\\} = 0$.",
          "steps": [
            {
              "step": "Step 1: Compute {Lx, Ly} Using Fundamental Poisson Brackets",
              "math": "$$\\{L_x, L_y\\} = \\{y p_z - z p_y, z p_x - x p_z\\} = \\{y p_z, z p_x\\} + \\{z p_y, x p_z\\}$$",
              "explanation": "Cross terms with no shared coordinates vanish identically. Expanding using the Leibniz product rule: $\\{y p_z, z p_x\\} = y p_x \\{p_z, z\\} = -y p_x$."
            },
            {
              "step": "Step 2: Evaluate the Second Term and Combine",
              "math": "$$\\{z p_y, x p_z\\} = x p_y \\{z, p_z\\} = +x p_y \\implies \\{L_x, L_y\\} = x p_y - y p_x = L_z$$",
              "explanation": "Cyclic permutations yield the complete angular momentum Lie algebra: $\\{L_i, L_j\\} = \\epsilon_{ijk} L_k$."
            },
            {
              "step": "Step 3: Evaluate Poisson Bracket of L² with Lz",
              "math": "$$\\{L^2, L_z\\} = \\{L_x^2 + L_y^2 + L_z^2, L_z\\} = 2 L_x \\{L_x, L_z\\} + 2 L_y \\{L_y, L_z\\} + 0 = 2 L_x (-L_y) + 2 L_y (L_x) = 0$$",
              "explanation": "Because $\\{L^2, L_z\\} = 0$, total angular momentum magnitude squared $L^2$ and any one of its Cartesian components $L_z$ can be simultaneously conserved in spherically symmetric central force fields."
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
              "explanation": "For the transformation to be canonical, the fundamental Poisson bracket must satisfy $\\{Q, P\\} = 1$. This requires $a d - b c = 1$."
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
      ],
      "id": "unit-6"
    },
    {
      "unitNumber": 7,
      "number": 7,
      "title": "Special Theory of Relativity: Kinematics & Transformations",
      "subtitle": "Michelson-Morley Experiment, Postulates, Lorentz Transformations, Simultaneity, Dilation & Relativistic Addition",
      "description": "Historical failure of Galilean relativity, the Michelson-Morley null experiment, Einstein's two postulates of Special Relativity, rigorous derivation of the Lorentz transformation equations, relativity of simultaneity, kinematic time dilation, Lorentz-Fitzgerald length contraction, relativistic velocity addition theorem, and relativistic longitudinal & transverse Doppler shifts.",
      "topics": [
        "Failure of Galilean Relativity & Ether Drift",
        "Michelson-Morley Interferometer Experiment",
        "Einstein's Two Postulates of Special Relativity",
        "Derivation of the Lorentz Transformation Equations",
        "Relativity of Simultaneity & Causality",
        "Time Dilation & Muon Decay Verification",
        "Length Contraction & Relativistic Velocity Addition"
      ],
      "sections": [
        {
          "id": "u7-sec1",
          "title": "Breakdown of Galilean Relativity & The Michelson-Morley Experiment",
          "content": "\n<h4>1. The Galilean Transformation & The Classical Velocity Addition</h4>\nIn Newtonian mechanics, space and time are absolute entities independent of the observer. For two inertial reference frames $S$ and $S'$ with parallel axes where $S'$ moves along the positive $x$-axis with constant speed $v$ relative to $S$, the <strong>Galilean transformation</strong> is:\n<div class=\"math-display\">$$x' = x - v t, \\quad y' = y, \\quad z' = z, \\quad t' = t$$</div>\nDifferentiating with respect to the absolute time $t = t'$ yields the Galilean velocity addition law:\n<div class=\"math-display\">$$\\vec{u}' = \\vec{u} - \\vec{v}$$</div>\nWhile Newton's laws of mechanics are invariant under Galilean transformations, <strong>Maxwell's equations of electrodynamics are not</strong>. Maxwell's equations predict that electromagnetic waves propagate in vacuum at a universal constant speed:\n<div class=\"math-display\">$$c = \\frac{1}{\\sqrt{\\mu_0 \\varepsilon_0}} \\approx 2.9979 \\times 10^8 \\text{ m/s}$$</div>\nUnder Galilean transformations, an observer moving through the putative luminiferous ether at speed $v$ should measure a variable light speed $c' = c \\pm v$.\n\n<h4>2. The Michelson-Morley Interferometer Experiment (1887)</h4>\nAlbert A. Michelson and Edward W. Morley devised a high-precision optical interferometer floating on a pool of mercury to detect the Earth's orbital velocity through the ether ($v_{\\text{Earth}} \\approx 30 \\text{ km/s}$, $v/c \\approx 10^{-4}$).\nA monochromatic beam of light from source $S$ is split by a half-silvered mirror into two mutually perpendicular paths of length $L_1$ and $L_2$:\n<ul>\n  <li><strong>Longitudinal Arm (Parallel to Ether Wind):</strong> The light travels downstream at speed $c - v$ and upstream at $c + v$. The round-trip transit time is:\n  <div class=\"math-display\">$$t_\\parallel = \\frac{L_1}{c - v} + \\frac{L_1}{c + v} = \\frac{2 L_1 c}{c^2 - v^2} = \\frac{2 L_1}{c} \\left( 1 - \\frac{v^2}{c^2} \\right)^{-1} \\approx \\frac{2 L_1}{c} \\left( 1 + \\frac{v^2}{c^2} \\right)$$</div></li>\n  <li><strong>Transverse Arm (Perpendicular to Ether Wind):</strong> By the Pythagorean theorem, the effective light speed is $\\sqrt{c^2 - v^2}$. The round-trip time is:\n  <div class=\"math-display\">$$t_\\perp = \\frac{2 L_2}{\\sqrt{c^2 - v^2}} = \\frac{2 L_2}{c} \\left( 1 - \\frac{v^2}{c^2} \\right)^{-1/2} \\approx \\frac{2 L_2}{c} \\left( 1 + \\frac{1}{2}\\frac{v^2}{c^2} \\right)$$</div></li>\n</ul>\nSetting $L_1 = L_2 = L$, the round-trip time difference is:\n<div class=\"math-display\">$$\\Delta t = t_\\parallel - t_\\perp \\approx \\frac{L}{c} \\frac{v^2}{c^2}$$</div>\nRotating the apparatus by $90^\\circ$ exchanges the roles of the arms, doubling the time difference to $2\\Delta t$. The expected fringe shift on the detector was:\n<div class=\"math-display\">$$\\Delta N = \\frac{c (2\\Delta t)}{\\lambda} = \\frac{2 L v^2}{\\lambda c^2} \\approx 0.4 \\text{ fringes}$$</div>\nThe experiment was sensitive to $0.01$ fringes, yet <strong>no fringe shift was observed</strong>. The ether drift was conclusively zero.\n",
          "simulation": "michelson-morley-sim"
        },
        {
          "id": "u7-sec2",
          "title": "Einstein's Postulates & Derivation of Lorentz Transformations",
          "content": "\n<h4>1. Einstein's Two Postulates of Special Relativity (1905)</h4>\nAlbert Einstein resolved the conflict between Newtonian mechanics and Maxwellian electrodynamics by abandoning absolute Newtonian space and time, founding the Special Theory of Relativity on two postulates:\n<ol>\n  <li><strong>The Principle of Relativity:</strong> The laws of physics take identical mathematical forms in all inertial reference frames. No physical experiment can distinguish between absolute rest and uniform rectilinear motion.</li>\n  <li><strong>The Constancy of the Speed of Light:</strong> The speed of light in vacuum is an absolute universal constant $c$ in all inertial frames, independent of the motion of the emitting source or the observer.</li>\n</ol>\n\n<h4>2. Mathematical Derivation of the Lorentz Transformations</h4>\nLet frame $S'$ move at speed $v$ along the $x$-axis of frame $S$. Due to homogeneity of space and time, the transformation must be linear:\n<div class=\"math-display\">$$x' = \\gamma(x - v t), \\quad y' = y, \\quad z' = z$$</div>\nBy the relativity postulate, the inverse transformation must be identical with $v \\to -v$:\n<div class=\"math-display\">$$x = \\gamma(x' + v t')$$</div>\nConsider a spherical light wave emitted from the coincident origins at $t = t' = 0$. The wavefront is described in both frames by:\n<div class=\"math-display\">$$x^2 + y^2 + z^2 - c^2 t^2 = 0, \\quad x'^2 + y'^2 + z'^2 - c^2 t'^2 = 0$$</div>\nSince $y' = y$ and $z' = z$, along the $x$-axis $x = c t$ and $x' = c t'$. Substituting into the transformation equations:\n<div class=\"math-display\">$$c t' = \\gamma(c - v) t, \\quad c t = \\gamma(c + v) t'$$</div>\nMultiplying the two equations:\n<div class=\"math-display\">$$c^2 t t' = \\gamma^2 (c^2 - v^2) t t' \\implies \\gamma^2 = \\frac{c^2}{c^2 - v^2} = \\frac{1}{1 - v^2/c^2}$$</div>\nTaking the positive root (preserving direction of time):\n<div class=\"math-display\">$$\\gamma = \\frac{1}{\\sqrt{1 - \\beta^2}}, \\quad \\beta = \\frac{v}{c}$$</div>\nSubstituting $x' = \\gamma(x - vt)$ into $x = \\gamma(x' + vt')$ to solve for $t'$:\n<div class=\"math-display\">$$x = \\gamma[\\gamma(x - vt) + vt'] \\implies \\frac{x}{\\gamma} - \\gamma(x - vt) = \\gamma vt'$$</div>\n<div class=\"math-display\">$$t' = \\gamma \\left( t - \\frac{v x}{c^2} \\right)$$</div>\nCollecting the <strong>Lorentz Transformation Equations</strong>:\n<div class=\"math-display\">$$x' = \\gamma (x - v t), \\quad y' = y, \\quad z' = z, \\quad t' = \\gamma \\left( t - \\frac{v x}{c^2} \\right)$$</div>\n"
        },
        {
          "id": "u7-sec3",
          "title": "Relativity of Simultaneity, Time Dilation & Length Contraction",
          "content": "\n<h4>1. The Relativity of Simultaneity</h4>\nConsider two spatial events $A$ and $B$ that occur simultaneously at different spatial locations in frame $S$: $\\Delta t = t_B - t_A = 0$ with $\\Delta x = x_B - x_A \\neq 0$.\nIn the moving frame $S'$, the time difference is:\n<div class=\"math-display\">$$\\Delta t' = \\gamma \\left( \\Delta t - \\frac{v \\Delta x}{c^2} \\right) = -\\gamma \\frac{v \\Delta x}{c^2} \\neq 0$$</div>\n<p><strong>Crucial Consequence:</strong> Two spatially separated events that are simultaneous in one inertial frame are <em>never</em> simultaneous in any other inertial frame moving relative to it. Absolute simultaneity is physically meaningless.</p>\n\n<h4>2. Kinematic Time Dilation</h4>\nLet a clock be located at a fixed position in frame $S'$ ($x_1' = x_2'$, so $\\Delta x' = 0$). The time interval between two ticks measured by this clock is the <strong>proper time</strong> $\\Delta t_0 = \\Delta t' = \\tau$.\nIn frame $S$, using the inverse Lorentz transformation $t = \\gamma(t' + v x'/c^2)$:\n<div class=\"math-display\">$$\\Delta t = \\gamma \\Delta t' = \\gamma \\Delta t_0 = \\frac{\\Delta t_0}{\\sqrt{1 - v^2/c^2}} > \\Delta t_0$$</div>\n<p><strong>Moving Clocks Run Slow:</strong> A clock moving relative to an observer ticks slower by a factor of $\\gamma$.</p>\n<p><em>Experimental Proof:</em> High-energy cosmic-ray muons created in the upper atmosphere ($\\sim 15\\text{ km}$) travel at $v \\approx 0.999c$ ($\\gamma \\approx 22.4$). Their laboratory lifetime expands from $\\tau_0 = 2.2 \\;\\mu\\text{s}$ to $\\Delta t = 49.3 \\;\\mu\\text{s}$, allowing them to survive and reach ground-level detectors.</p>\n\n<h4>3. Lorentz-Fitzgerald Length Contraction</h4>\nLet a rod lie at rest along the $x'$-axis in frame $S'$. Its <strong>proper length</strong> is $L_0 = x_2' - x_1'$.\nTo measure the length $L = x_2 - x_1$ in frame $S$, the coordinates of both ends must be measured <em>simultaneously</em> at $t_1 = t_2$ ($\\Delta t = 0$).\nApplying the Lorentz transformation $x' = \\gamma(x - vt)$:\n<div class=\"math-display\">$$L_0 = x_2' - x_1' = \\gamma(x_2 - x_1) - \\gamma v(t_2 - t_1) = \\gamma L$$</div>\n<div class=\"math-display\">$$L = \\frac{L_0}{\\gamma} = L_0 \\sqrt{1 - \\frac{v^2}{c^2}} < L_0$$</div>\n<p><strong>Moving Objects Contract:</strong> The physical length of an object is contracted along its direction of motion by factor $1/\\gamma$. Dimensions perpendicular to the velocity ($y, z$) remain completely unaffected.</p>\n",
          "simulation": "lorentz-contraction-sim"
        },
        {
          "id": "u7-sec4",
          "title": "Relativistic Velocity Addition & The Relativistic Doppler Effect",
          "content": "\n<h4>1. Relativistic Velocity Transformation Formula</h4>\nLet a particle move with velocity $\\vec{u} = (u_x, u_y, u_z) = (dx/dt, dy/dt, dz/dt)$ in frame $S$. In frame $S'$:\n<div class=\"math-display\">$$dx' = \\gamma(dx - v dt), \\quad dy' = dy, \\quad dz' = dz, \\quad dt' = \\gamma\\left(dt - \\frac{v dx}{c^2}\\right)$$</div>\nDividing $dx'$ by $dt'$:\n<div class=\"math-display\">$$u_x' = \\frac{dx'}{dt'} = \\frac{\\gamma(dx - v dt)}{\\gamma\\left(dt - \\frac{v dx}{c^2}\\right)} = \\frac{\\frac{dx}{dt} - v}{1 - \\frac{v}{c^2}\\frac{dx}{dt}} = \\frac{u_x - v}{1 - \\frac{u_x v}{c^2}}$$</div>\nFor transverse components:\n<div class=\"math-display\">$$u_y' = \\frac{dy'}{dt'} = \\frac{u_y}{\\gamma \\left(1 - \\frac{u_x v}{c^2}\\right)}, \\quad u_z' = \\frac{dz'}{dt'} = \\frac{u_z}{\\gamma \\left(1 - \\frac{u_x v}{c^2}\\right)}$$</div>\n<p><strong>Universal Speed Limit:</strong> If a photon travels at $u_x = c$, then in any frame moving at speed $v$:\n<div class=\"math-display\">$$u_x' = \\frac{c - v}{1 - \\frac{c v}{c^2}} = \\frac{c - v}{1 - v/c} = c$$</div>\nThe speed of light $c$ is invariant under velocity addition. No compounding of sub-luminal velocities can ever exceed $c$.</p>\n\n<h4>2. Relativistic Doppler Effect</h4>\nFor an electromagnetic source emitting frequency $\\nu_0$ moving at speed $v$ relative to an observer:\n<ul>\n  <li><strong>Longitudinal Doppler Effect (Source Moving Away):</strong>\n  <div class=\"math-display\">$$\\nu = \\nu_0 \\sqrt{\\frac{1 - v/c}{1 + v/c}} = \\nu_0 \\frac{\\sqrt{1 - \\beta^2}}{1 + \\beta}$$</div>\n  The observed wavelength is redshifted: $\\lambda = \\lambda_0 \\sqrt{\\frac{1 + \\beta}{1 - \\beta}}$.</li>\n  <li><strong>Transverse Doppler Effect ($\\theta = 90^\\circ$):</strong>\n  When the source moves perpendicular to the line of sight:\n  <div class=\"math-display\">$$\\nu_{\\perp} = \\frac{\\nu_0}{\\gamma} = \\nu_0 \\sqrt{1 - \\frac{v^2}{c^2}}$$</div>\n  A purely relativistic phenomenon resulting directly from time dilation (predicted to be exactly zero in classical physics).</li>\n</ul>\n"
        }
      ],
      "problems": [
        {
          "id": "cm-prob-7-1",
          "title": "Muon Atmospheric Decay: Time Dilation vs. Length Contraction",
          "statement": "Muons are created at an altitude of $h = 10.0\\text{ km}$ above sea level and travel vertically downward toward Earth at $v = 0.998 c$. The proper rest lifetime of a muon is $\\tau_0 = 2.20 \\;\\mu\\text{s}$. (a) Calculate the fraction of muons that survive to reach sea level in the Earth observer frame. (b) Re-evaluate the problem in the muon's rest frame using length contraction.",
          "steps": [
            {
              "step": "Step 1: Compute the Lorentz Factor γ",
              "math": "$$\\beta = 0.998 \\implies \\gamma = \\frac{1}{\\sqrt{1 - (0.998)^2}} = \\frac{1}{\\sqrt{0.003996}} \\approx 15.82$$",
              "explanation": "The relativistic time dilation and length contraction factor is $\\gamma \\approx 15.82$."
            },
            {
              "step": "Step 2: Earth Frame Calculation (Time Dilation)",
              "math": "$$\\Delta t_{\\text{lab}} = \\frac{h}{v} = \\frac{10^4 \\text{ m}}{0.998 \\times 3 \\times 10^8 \\text{ m/s}} = 33.40 \\;\\mu\\text{s}, \\quad \\tau_{\\text{lab}} = \\gamma \\tau_0 = 15.82 \\times 2.20 = 34.80 \\;\\mu\\text{s}$$",
              "explanation": "The survival fraction according to radioactive exponential decay $N/N_0 = e^{-\\Delta t / \\tau}$ is $e^{-33.40 / 34.80} = e^{-0.9598} \\approx 0.383$ (38.3% survive). Without relativity, $N/N_0 = e^{-33.40/2.20} = e^{-15.18} \\approx 2.5 \\times 10^{-7}$."
            },
            {
              "step": "Step 3: Muon Frame Calculation (Length Contraction)",
              "math": "$$h' = \\frac{h}{\\gamma} = \\frac{10.0 \\text{ km}}{15.82} = 632.1 \\text{ m}, \\quad \\Delta t' = \\frac{h'}{v} = \\frac{632.1}{0.998 c} = 2.112 \\;\\mu\\text{s}$$",
              "explanation": "In the muon's frame, the clock ticks at normal proper rate $\\tau_0 = 2.20 \\;\\mu\\text{s}$, but the atmosphere is contracted to $632.1\\text{ m}$. Survival fraction: $N/N_0 = e^{-\\Delta t' / \\tau_0} = e^{-2.112 / 2.20} = e^{-0.960} \\approx 0.383$, yielding identical physical predictions."
            }
          ],
          "answer": "Survival fraction is 38.3% in both frames, demonstrating the physical equivalence of time dilation (Earth frame) and length contraction (muon frame)."
        },
        {
          "id": "cm-prob-7-2",
          "title": "Relativistic Head-On Spacecraft Velocity Composition",
          "statement": "Two starships $A$ and $B$ approach each other head-on as observed from a space station. Starship $A$ travels at $u_A = 0.80 c$ to the right, and starship $B$ travels at $u_B = 0.90 c$ to the left. (a) Calculate the speed of starship $B$ relative to starship $A$. (b) If starship $A$ fires a laser pulse toward $B$, calculate the speed of the laser pulse as measured by $B$.",
          "steps": [
            {
              "step": "Step 1: Set Up the Relativistic Velocity Transformation",
              "math": "$$u_x' = \\frac{u_x - v}{1 - \\frac{u_x v}{c^2}}$$",
              "explanation": "Let frame $S$ be the space station. Frame $S'$ is attached to starship $A$, so $v = +0.80 c$. The velocity of starship $B$ in $S$ is $u_x = -0.90 c$."
            },
            {
              "step": "Step 2: Calculate Relative Velocity of Starship B",
              "math": "$$u_B' = \\frac{-0.90 c - 0.80 c}{1 - \\frac{(-0.90 c)(0.80 c)}{c^2}} = \\frac{-1.70 c}{1 - (-0.72)} = \\frac{-1.70 c}{1.72} \\approx -0.9884 c$$",
              "explanation": "The relative approach speed is $0.9884 c$, strictly less than $c$. Classical Galilean addition would have given an unphysical $1.70 c$."
            },
            {
              "step": "Step 3: Laser Pulse Speed Measured by B",
              "math": "$$u_{\\text{laser}}' = \\frac{c - (-0.9884 c)}{1 - \\frac{c(-0.9884 c)}{c^2}} = \\frac{c(1 + 0.9884)}{1 + 0.9884} = c$$",
              "explanation": "By Einstein's second postulate, light travels at speed $c$ in all inertial reference frames regardless of relative velocities."
            }
          ],
          "answer": "(a) Relative speed of B as seen by A is 0.9884 c. (b) Laser pulse speed measured by B is exactly c."
        },
        {
          "id": "cm-prob-7-3",
          "title": "Cosmological Redshift & Relativistic Doppler Shift of a Quasar",
          "statement": "A distant quasar emits the Lyman-alpha spectral line of atomic hydrogen at rest wavelength $\\lambda_0 = 121.6\\text{ nm}$. The spectral line is observed on Earth at a redshifted wavelength $\\lambda_{\\text{obs}} = 486.4\\text{ nm}$. Determine the recession velocity $v/c$ of the quasar.",
          "steps": [
            {
              "step": "Step 1: Relate Observed and Rest Wavelengths to Relativistic Doppler Formula",
              "math": "$$\\frac{\\lambda_{\\text{obs}}}{\\lambda_0} = \\sqrt{\\frac{1 + \\beta}{1 - \\beta}} = 1 + z$$",
              "explanation": "The measured redshift parameter is $z = \\frac{\\lambda_{\\text{obs}} - \\lambda_0}{\\lambda_0} = \\frac{486.4 - 121.6}{121.6} = \\frac{364.8}{121.6} = 3.0$."
            },
            {
              "step": "Step 2: Square Both Sides and Solve for β = v/c",
              "math": "$$\\frac{1 + \\beta}{1 - \\beta} = (1 + z)^2 = (1 + 3.0)^2 = 4^2 = 16$$",
              "explanation": "Cross-multiplying: $1 + \\beta = 16(1 - \\beta) = 16 - 16\\beta$."
            },
            {
              "step": "Step 3: Solve for Dimensionless Velocity β",
              "math": "$$17 \\beta = 15 \\implies \\beta = \\frac{v}{c} = \\frac{15}{17} \\approx 0.8824$$",
              "explanation": "The quasar is receding away from Earth at $88.24\\%$ of the speed of light ($v \\approx 2.65 \\times 10^8\\text{ m/s}$)."
            }
          ],
          "answer": "Recession velocity: v/c = 15/17 ≈ 0.8824 (88.24% of light speed)."
        }
      ],
      "id": "unit-7"
    },
    {
      "unitNumber": 8,
      "number": 8,
      "title": "Relativistic Mechanics & Four-Vectors",
      "subtitle": "Minkowski Spacetime, Invariant Intervals, 4-Momentum, Mass-Energy Equivalence & Compton Scattering",
      "description": "Foundations of four-dimensional Minkowski spacetime, metric tensor η_μν, invariant spacetime intervals (timelike, spacelike, null), light cones, proper time, four-velocity, relativistic momentum, relativistic kinetic energy, universal mass-energy equivalence E=mc², four-momentum invariant E² = p²c² + m²c⁴, Minkowski four-force, and particle collision dynamics with Compton scattering.",
      "topics": [
        "Four-Dimensional Minkowski Spacetime & Metric Tensor",
        "Invariant Spacetime Intervals & Light Cone Geometry",
        "Proper Time & Four-Velocity Vector",
        "Relativistic Momentum & Relativistic Mass",
        "Relativistic Work-Energy Theorem & Kinetic Energy",
        "Mass-Energy Equivalence (E = mc²) & Four-Momentum",
        "Minkowski Four-Force & Compton Scattering"
      ],
      "sections": [
        {
          "id": "u8-sec1",
          "title": "Minkowski Four-Dimensional Spacetime & Invariant Intervals",
          "content": "\n<h4>1. The Four-Vector Formalism</h4>\nIn 1908, Hermann Minkowski recognized that Special Relativity unifies three-dimensional space and one-dimensional time into a single four-dimensional continuum: <strong>spacetime</strong>.\nAn event is specified by a contravariant position four-vector $x^\\mu$ ($\\mu = 0, 1, 2, 3$):\n<div class=\"math-display\">$$x^\\mu = (x^0, x^1, x^2, x^3) = (c t, x, y, z)$$</div>\nThe Minkowski spacetime metric tensor $\\eta_{\\mu\\nu}$ in the mostly-minus convention is:\n<div class=\"math-display\">$$\\eta_{\\mu\\nu} = \\begin{pmatrix} 1 & 0 & 0 & 0 \\\\ 0 & -1 & 0 & 0 \\\\ 0 & 0 & -1 & 0 \\\\ 0 & 0 & 0 & -1 \\end{pmatrix}$$</div>\nLowering indices via the metric defines the covariant four-vector $x_\\mu = \\eta_{\\mu\\nu} x^\\nu = (c t, -x, -y, -z)$.\n\n<h4>2. The Invariant Spacetime Interval</h4>\nThe scalar product of the infinitesimal displacement four-vector $dx^\\mu$ with itself defines the <strong>invariant spacetime interval</strong> $ds^2$:\n<div class=\"math-display\">$$ds^2 = dx_\\mu dx^\\mu = \\eta_{\\mu\\nu} dx^\\mu dx^\\nu = c^2 dt^2 - dx^2 - dy^2 - dz^2$$</div>\n<p><strong>Lorentz Invariance:</strong> $ds^2$ is an absolute scalar: its numerical value is identical for all inertial observers: $ds^2 = ds'^2$.</p>\n\n<h4>3. Causal Structure & Light Cones</h4>\nThe sign of $ds^2$ categorizes the causal connection between two spacetime events:\n<ul>\n  <li><strong>Timelike Interval ($ds^2 > 0$):</strong> $c^2 \\Delta t^2 > \\Delta \\vec{r}^2$. A physical signal traveling at speed $v < c$ can connect the two events. A reference frame exists where the events occur at the exact same spatial location. Events lie within the future or past <strong>light cone</strong>.</li>\n  <li><strong>Spacelike Interval ($ds^2 < 0$):</strong> $c^2 \\Delta t^2 < \\Delta \\vec{r}^2$. No physical signal can travel between the events without exceeding $c$. A reference frame exists where the events occur simultaneously ($\\Delta t' = 0$). Events lie outside the light cone.</li>\n  <li><strong>Lightlike / Null Interval ($ds^2 = 0$):</strong> $c^2 \\Delta t^2 = \\Delta \\vec{r}^2$. Events can be connected only by photons traveling at speed $c$. Events lie on the boundary surface of the light cone.</li>\n</ul>\n",
          "simulation": "minkowski-spacetime-sim"
        },
        {
          "id": "u8-sec2",
          "title": "Proper Time, Four-Velocity & Relativistic Momentum",
          "content": "\n<h4>1. Proper Time $\\tau$</h4>\nThe <strong>proper time</strong> $d\\tau$ is the time interval measured by a clock carried along with the moving particle ($d\\vec{r}' = 0$ in the instantaneous rest frame):\n<div class=\"math-display\">$$ds^2 = c^2 d\\tau^2 \\implies d\\tau = \\frac{ds}{c} = \\sqrt{dt^2 - \\frac{d\\vec{r}^2}{c^2}} = dt \\sqrt{1 - \\frac{u^2}{c^2}} = \\frac{dt}{\\gamma}$$</div>\nSince $ds$ and $c$ are Lorentz invariants, <strong>proper time $\\tau$ is a Lorentz scalar</strong>.\n\n<h4>2. Four-Velocity Vector $U^\\mu$</h4>\nDifferentiating the position four-vector $x^\\mu$ with respect to the invariant proper time $\\tau$:\n<div class=\"math-display\">$$U^\\mu = \\frac{dx^\\mu}{d\\tau} = \\gamma \\frac{dx^\\mu}{dt} = \\gamma (c, \\vec{u}) = (\\gamma c, \\gamma u_x, \\gamma u_y, \\gamma u_z)$$</div>\nThe invariant magnitude of the four-velocity is universally constant:\n<div class=\"math-display\">$$U^\\mu U_\\mu = \\gamma^2 (c^2 - u^2) = \\frac{c^2 - u^2}{1 - u^2/c^2} = c^2 = \\text{constant for all particles}$$</div>\n\n<h4>3. Relativistic Momentum & Four-Momentum $P^\\mu$</h4>\nMultiplying the four-velocity by the invariant rest mass $m$:\n<div class=\"math-display\">$$P^\\mu = m U^\\mu = (\\gamma m c, \\gamma m \\vec{u})$$</div>\nThe spatial part gives the <strong>relativistic three-momentum</strong>:\n<div class=\"math-display\">$$\\vec{p} = \\gamma m \\vec{u} = \\frac{m \\vec{u}}{\\sqrt{1 - u^2/c^2}}$$</div>\nNotice that as particle speed approaches light speed ($u \\to c$), $\\gamma \\to \\infty$, so $\\vec{p} \\to \\infty$. An infinite amount of momentum (and energy) is required to accelerate any massive body to $c$.\n"
        },
        {
          "id": "u8-sec3",
          "title": "Relativistic Work-Energy Theorem & Mass-Energy Equivalence",
          "content": "\n<h4>1. Derivation of Relativistic Kinetic Energy</h4>\nNewton's Second Law in relativistic mechanics defines force as the time rate of change of relativistic momentum: $\\vec{F} = \\frac{d\\vec{p}}{dt} = \\frac{d}{dt}(\\gamma m \\vec{u})$.\nThe work done by the force in moving a particle from rest to velocity $\\vec{u}$ is:\n<div class=\"math-display\">$$W = \\int_0^{\\vec{r}} \\vec{F} \\cdot d\\vec{r} = \\int_0^t \\frac{d\\vec{p}}{dt} \\cdot \\vec{u} dt = \\int_0^{\\vec{p}} \\vec{u} \\cdot d\\vec{p}$$</div>\nIntegrating by parts:\n<div class=\"math-display\">$$W = \\vec{u} \\cdot \\vec{p} - \\int_0^{\\vec{u}} \\vec{p} \\cdot d\\vec{u} = \\gamma m u^2 - \\int_0^u \\frac{m u du}{\\sqrt{1 - u^2/c^2}}$$</div>\nEvaluating the integral:\n<div class=\"math-display\">$$\\int_0^u \\frac{m u du}{\\sqrt{1 - u^2/c^2}} = \\left[ -m c^2 \\sqrt{1 - u^2/c^2} \\right]_0^u = m c^2 - \\frac{m c^2}{\\gamma}$$</div>\nSubstituting back:\n<div class=\"math-display\">$$W = \\gamma m u^2 + \\frac{m c^2}{\\gamma} - m c^2 = m c^2 \\left( \\frac{\\gamma^2 u^2/c^2 + 1}{\\gamma} \\right) - m c^2 = \\gamma m c^2 - m c^2$$</div>\nSince initial kinetic energy at rest was zero, the <strong>relativistic kinetic energy</strong> $K$ is:\n<div class=\"math-display\">$$K = (\\gamma - 1) m c^2$$</div>\n<p><strong>Non-Relativistic Limit ($u \\ll c$):</strong> Expanding $\\gamma = (1 - u^2/c^2)^{-1/2} \\approx 1 + \\frac{1}{2}\\frac{u^2}{c^2} + \\frac{3}{8}\\frac{u^4}{c^4} + \\dots$:\n<div class=\"math-display\">$$K = \\left( 1 + \\frac{1}{2}\\frac{u^2}{c^2} - 1 \\right) m c^2 = \\frac{1}{2}m u^2$$</div>\nreproducing classical Newtonian kinetic energy.</p>\n\n<h4>2. Mass-Energy Equivalence ($E = mc^2$)</h4>\nEinstein defined the <strong>total relativistic energy</strong> $E$ as the sum of kinetic energy and rest-mass energy $E_0$:\n<div class=\"math-display\">$$E = K + m c^2 = (\\gamma - 1)m c^2 + m c^2 = \\gamma m c^2$$</div>\nWhen the particle is at rest ($u = 0, \\gamma = 1$), it retains an intrinsic <strong>rest mass energy</strong>:\n<div class=\"math-display\">$$E_0 = m c^2$$</div>\n<p>Mass and energy are fundamentally equivalent: mass is concentrated, latent energy ($1\\text{ kg} \\approx 9 \\times 10^{16}\\text{ J}$).</p>\n\n<h4>3. The Four-Momentum Vector & The Energy-Momentum Invariant</h4>\nThe temporal component of four-momentum is $P^0 = \\gamma m c = E/c$. Thus:\n<div class=\"math-display\">$$P^\\mu = \\left( \\frac{E}{c}, \\vec{p} \\right)$$</div>\nEvaluating the Lorentz-invariant norm $P^\\mu P_\\mu$:\n<div class=\"math-display\">$$P^\\mu P_\\mu = \\left( \\frac{E}{c} \\right)^2 - \\vec{p}^2 = m^2 U^\\mu U_\\mu = m^2 c^2$$</div>\nMultiplying by $c^2$ yields the fundamental <strong>Energy-Momentum Relation</strong>:\n<div class=\"math-display\">$$E^2 = p^2 c^2 + m^2 c^4$$</div>\nFor massless particles ($m = 0$, such as photons):\n<div class=\"math-display\">$$E = p c \\implies p = \\frac{E}{c} = \\frac{h \\nu}{c} = \\frac{h}{\\lambda}$$</div>\n"
        },
        {
          "id": "u8-sec4",
          "title": "Minkowski Four-Force & Relativistic Collisions",
          "content": "\n<h4>1. The Minkowski Four-Force $K^\\mu$</h4>\nThe relativistic generalization of Newton's Second Law in four-vector form is:\n<div class=\"math-display\">$$K^\\mu = \\frac{dP^\\mu}{d\\tau} = \\gamma \\frac{dP^\\mu}{dt} = \\gamma \\left( \\frac{1}{c} \\frac{dE}{dt}, \\frac{d\\vec{p}}{dt} \\right)$$</div>\nSince $\\vec{F} = \\frac{d\\vec{p}}{dt}$ and power delivered is $\\frac{dE}{dt} = \\vec{F} \\cdot \\vec{u}$:\n<div class=\"math-display\">$$K^\\mu = \\gamma \\left( \\frac{\\vec{F} \\cdot \\vec{u}}{c}, \\vec{F} \\right)$$</div>\n\n<h4>2. Conservation of Four-Momentum in Particle Collisions</h4>\nIn any closed system of colliding particles, the total four-momentum is strictly conserved:\n<div class=\"math-display\">$$\\sum_{i=1}^{N_{\\text{in}}} P_i^\\mu = \\sum_{f=1}^{N_{\\text{out}}} P_f^\\mu$$</div>\nThis single four-vector relation encapsulates both <strong>conservation of total relativistic energy</strong> ($\\mu = 0$) and <strong>conservation of total three-momentum</strong> ($\\mu = 1, 2, 3$).\n\n<h4>3. Derivation of Compton Scattering</h4>\nConsider a photon of initial wavelength $\\lambda$ and four-momentum $P_\\gamma = (E/c, \\vec{p}_\\gamma)$ colliding with an electron of rest mass $m_e$ initially at rest: $P_e = (m_e c, \\vec{0})$.\nAfter scattering at angle $\\theta$, the photon has four-momentum $P_\\gamma' = (E'/c, \\vec{p}_\\gamma')$ and the electron has $P_e'$.\nConservation of four-momentum: $P_\\gamma + P_e = P_\\gamma' + P_e' \\implies P_e' = P_\\gamma - P_\\gamma' + P_e$.\nSquaring both sides using $P^\\mu P_\\mu$:\n<div class=\"math-display\">$$P_e'^2 = (P_\\gamma - P_\\gamma' + P_e)^2$$</div>\nSince $P_e^2 = P_e'^2 = m_e^2 c^2$ and $P_\\gamma^2 = P_\\gamma'^2 = 0$:\n<div class=\"math-display\">$$m_e^2 c^2 = -2 P_\\gamma \\cdot P_\\gamma' + 2 P_\\gamma \\cdot P_e - 2 P_\\gamma' \\cdot P_e + m_e^2 c^2$$</div>\n<div class=\"math-display\">$$P_\\gamma \\cdot P_\\gamma' = (P_\\gamma - P_\\gamma') \\cdot P_e$$</div>\nEvaluating scalar products:\n<div class=\"math-display\">$$P_\\gamma \\cdot P_\\gamma' = \\frac{E E'}{c^2} - \\vec{p}_\\gamma \\cdot \\vec{p}_\\gamma' = \\frac{E E'}{c^2}(1 - \\cos \\theta)$$</div>\n<div class=\"math-display$$(P_\\gamma - P_\\gamma') \\cdot P_e = \\left( \\frac{E - E'}{c} \\right)(m_e c) - 0 = m_e (E - E')$$</div>\nEquating expressions:\n<div class=\"math-display\">$$\\frac{E E'}{c^2}(1 - \\cos \\theta) = m_e (E - E')$$</div>\nDividing by $E E' m_e c$:\n<div class=\"math-display\">$$\\frac{1}{E'} - \\frac{1}{E} = \\frac{1}{m_e c^2}(1 - \\cos \\theta)$$</div>\nUsing $E = hc/\\lambda$ and $E' = hc/\\lambda'$ yields the <strong>Compton Scattering Formula</strong>:\n<div class=\"math-display\">$$\\lambda' - \\lambda = \\frac{h}{m_e c}(1 - \\cos \\theta) = \\lambda_C (1 - \\cos \\theta)$$</div>\nwhere $\\lambda_C = \\frac{h}{m_e c} \\approx 2.426 \\times 10^{-12}\\text{ m} = 0.002426\\text{ nm}$ is the Compton wavelength of the electron.\n",
          "simulation": "relativistic-collision-sim"
        }
      ],
      "problems": [
        {
          "id": "cm-prob-8-1",
          "title": "Threshold Kinetic Energy for Antiproton Creation via p + p Collision",
          "statement": "Calculate the minimum threshold kinetic energy $K_{\\text{th}}$ in the laboratory frame required for an incident proton of rest mass $m_p$ colliding with a target proton at rest to produce a proton-antiproton pair: $p + p \\to p + p + p + \\bar{p}$.",
          "steps": [
            {
              "step": "Step 1: Set Up Initial Four-Momentum in Laboratory Frame",
              "math": "$$P_{\\text{tot}}^{\\text{lab}} = P_1 + P_2 = \\left( \\frac{E_1 + m_p c^2}{c}, \\vec{p}_1 \\right)$$",
              "explanation": "Target proton 2 is at rest, so $P_2 = (m_p c, \\vec{0})$. The incident proton 1 has total energy $E_1 = K_{\\text{th}} + m_p c^2$."
            },
            {
              "step": "Step 2: Evaluate Invariant Mass Squared s = P_tot^μ P_tot,μ",
              "math": "$$s = (P_1 + P_2)^2 = P_1^2 + P_2^2 + 2 P_1 \\cdot P_2 = m_p^2 c^2 + m_p^2 c^2 + 2 \\left( \\frac{E_1}{c}(m_p c) - 0 \\right) = 2 m_p^2 c^2 + 2 m_p E_1$$",
              "explanation": "Because $s$ is a Lorentz scalar, its value in the laboratory frame must equal its value in the center-of-mass (CM) frame."
            },
            {
              "step": "Step 3: Evaluate s at Threshold in Center-of-Mass Frame",
              "math": "$$s = \\left(\\sum_{i=1}^4 m_i c\\right)^2 = (4 m_p c)^2 = 16 m_p^2 c^2$$",
              "explanation": "At threshold, all four final particles ($3p + 1\\bar{p}$) are produced at rest in the CM frame with zero residual kinetic energy."
            },
            {
              "step": "Step 4: Equate Invariant Masses and Solve for Threshold Energy",
              "math": "$$2 m_p^2 c^2 + 2 m_p E_1 = 16 m_p^2 c^2 \\implies 2 m_p E_1 = 14 m_p^2 c^2 \\implies E_1 = 7 m_p c^2$$",
              "explanation": "The threshold kinetic energy is $K_{\\text{th}} = E_1 - m_p c^2 = 7 m_p c^2 - m_p c^2 = 6 m_p c^2$. Since $m_p c^2 \\approx 938.3\\text{ MeV}$, $K_{\\text{th}} = 6 \\times 938.3 = 5.63\\text{ GeV}$."
            }
          ],
          "answer": "Threshold incident kinetic energy: K_th = 6 m_p c² ≈ 5.63 GeV (6 times the rest mass energy of a proton)."
        },
        {
          "id": "cm-prob-8-2",
          "title": "Invariant Mass and Velocity of a Decaying Neutral Pion",
          "statement": "A neutral pion $\\pi^0$ of rest mass $m_\\pi = 135.0\\text{ MeV}/c^2$ decays in flight into two high-energy photons: $\\pi^0 \\to \\gamma_1 + \\gamma_2$. In the laboratory frame, the two photons have energies $E_1 = 100.0\\text{ MeV}$ and $E_2 = 60.0\\text{ MeV}$. (a) Find the opening angle $\\theta$ between the two photons. (b) Find the velocity $v/c$ of the parent pion.",
          "steps": [
            {
              "step": "Step 1: Apply Four-Momentum Conservation P_π = P_γ1 + P_γ2",
              "math": "$$P_\\pi^2 = (P_{\\gamma 1} + P_{\\gamma 2})^2 = P_{\\gamma 1}^2 + P_{\\gamma 2}^2 + 2 P_{\\gamma 1} \\cdot P_{\\gamma 2}$$",
              "explanation": "Since $P_\\pi^2 = m_\\pi^2 c^2$ and photons are massless ($P_\\gamma^2 = 0$), $m_\\pi^2 c^2 = 2 P_{\\gamma 1} \\cdot P_{\\gamma 2}$."
            },
            {
              "step": "Step 2: Expand Photon Four-Vector Dot Product",
              "math": "$$2 P_{\\gamma 1} \\cdot P_{\\gamma 2} = 2 \\left( \\frac{E_1 E_2}{c^2} - \\vec{p}_1 \\cdot \\vec{p}_2 \\right) = \\frac{2 E_1 E_2}{c^2}(1 - \\cos \\theta) = m_\\pi^2 c^2$$",
              "explanation": "Solving for $\\cos \\theta$: $1 - \\cos \\theta = \\frac{m_\\pi^2 c^4}{2 E_1 E_2} = \\frac{(135.0)^2}{2(100.0)(60.0)} = \\frac{18225}{12000} = 1.51875$. Notice that for physical decay, $\\cos\\theta = 1 - 1.51875 = -0.51875$, so $\\theta = \\arccos(-0.51875) \\approx 121.25^\\circ$."
            },
            {
              "step": "Step 3: Determine Pion Total Energy and Velocity",
              "math": "$$E_\\pi = E_1 + E_2 = 160.0\\text{ MeV}, \\quad \\gamma = \\frac{E_\\pi}{m_\\pi c^2} = \\frac{160.0}{135.0} \\approx 1.1852$$",
              "explanation": "The velocity is $\\beta = \\frac{v}{c} = \\sqrt{1 - 1/\\gamma^2} = \\sqrt{1 - (135/160)^2} = \\sqrt{1 - 0.7119} = \\sqrt{0.2881} \\approx 0.5367$."
            }
          ],
          "answer": "(a) Opening angle between photons: θ ≈ 121.3°; (b) Parent pion velocity: v/c ≈ 0.537 (53.7% light speed)."
        },
        {
          "id": "cm-prob-8-3",
          "title": "Relativistic Rocket Motion: The Relativistic Tsiolkovsky Equation",
          "statement": "A relativistic rocket accelerates from rest in interstellar space by expelling propellant exhaust gas at constant speed $u_{\\text{ex}}$ relative to the rocket nozzle. Derive the relativistic generalization of Tsiolkovsky's rocket equation relating final velocity $v$ to the mass ratio $M_0 / M_f$.",
          "steps": [
            {
              "step": "Step 1: Balance Momentum in the Instantaneous Rest Frame of the Rocket",
              "math": "$$M dv' + u_{\\text{ex}} dM = 0 \\implies dv' = -u_{\\text{ex}} \\frac{dM}{M}$$",
              "explanation": "In the rocket's instantaneous comoving frame, the change in rocket velocity is $dv'$ and exhaust mass expelled is $-dM$."
            },
            {
              "step": "Step 2: Relate Comoving dv' to Lab Frame dv via Velocity Addition",
              "math": "$$v + dv = \\frac{v + dv'}{1 + v dv'/c^2} \\approx (v + dv')(1 - v dv'/c^2) \\implies dv = dv' (1 - v^2/c^2) = \\frac{dv'}{\\gamma^2}$$",
              "explanation": "Inverting gives $dv' = \\frac{dv}{1 - v^2/c^2}$."
            },
            {
              "step": "Step 3: Integrate Differential Equation",
              "math": "$$\\int_0^v \\frac{dv}{1 - v^2/c^2} = -u_{\\text{ex}} \\int_{M_0}^{M_f} \\frac{dM}{M} \\implies \\frac{c}{2} \\ln\\left( \\frac{1 + v/c}{1 - v/c} \\right) = u_{\\text{ex}} \\ln\\left( \\frac{M_0}{M_f} \\right)$$",
              "explanation": "Exponentiating: $\\frac{1 + v/c}{1 - v/c} = \\left( \\frac{M_0}{M_f} \\right)^{2 u_{\\text{ex}} / c}$. Solving for $v/c$ delivers the relativistic rocket velocity."
            }
          ],
          "answer": "Relativistic rocket velocity: v/c = [(M0/Mf)^(2 u_ex/c) - 1] / [(M0/Mf)^(2 u_ex/c) + 1]. In the photon rocket limit (u_ex = c), v/c = [(M0/Mf)² - 1] / [(M0/Mf)² + 1]."
        }
      ],
      "id": "unit-8"
    }
  ]
};
