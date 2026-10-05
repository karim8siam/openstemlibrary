# Unit 3 & Unit 4 Builder for Classical Mechanics & Special Relativity
import json

u3 = {
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
            "content": """
<h4>1. Decoupling Center-of-Mass and Relative Coordinates</h4>
Consider two isolated particles of masses $m_1$ and $m_2$ interacting solely via an internal central force directed along the line joining them:
<div class="math-display">$$\\vec{F}_{12} = -\\vec{F}_{21} = f(r) \\hat{r}, \\quad \\vec{r} = \\vec{r}_1 - \\vec{r}_2, \\quad r = |\\vec{r}|$$</div>
The equations of motion are $m_1 \\ddot{\\vec{r}}_1 = f(r) \\hat{r}$ and $m_2 \\ddot{\\vec{r}}_2 = -f(r) \\hat{r}$. We introduce the center of mass coordinate $\\vec{R}$ and relative separation vector $\\vec{r}$:
<div class="math-display">$$\\vec{R} = \\frac{m_1 \\vec{r}_1 + m_2 \\vec{r}_2}{m_1 + m_2}, \\quad \\vec{r} = \\vec{r}_1 - \\vec{r}_2$$</div>
The individual position vectors in terms of $\\vec{R}$ and $\\vec{r}$ are:
<div class="math-display">$$\\vec{r}_1 = \\vec{R} + \\frac{m_2}{M}\\vec{r}, \\quad \\vec{r}_2 = \\vec{R} - \\frac{m_1}{M}\\vec{r}, \\quad M = m_1 + m_2$$</div>

<h4>2. Separation of the Lagrangian & The Reduced Mass</h4>
The total kinetic energy decomposes cleanly:
<div class="math-display">$$T = \\frac{1}{2}m_1 \\dot{\\vec{r}}_1^2 + \\frac{1}{2}m_2 \\dot{\\vec{r}}_2^2 = \\frac{1}{2}M \\dot{\\vec{R}}^2 + \\frac{1}{2}\\mu \\dot{\\vec{r}}^2$$</div>
where $\\mu$ is the <strong>reduced mass</strong> of the system:
<div class="math-display">$$\\mu = \\frac{m_1 m_2}{m_1 + m_2} = \\frac{m_1 m_2}{M}$$</div>
Since the interaction potential $V(r)$ depends only on relative distance $r$, the Lagrangian separates:
<div class="math-display">$$L = L_{\\text{CM}} + L_{\\text{rel}} = \\left( \\frac{1}{2}M \\dot{\\vec{R}}^2 \\right) + \\left( \\frac{1}{2}\\mu \\dot{\\vec{r}}^2 - V(r) \\right)$$</div>
Because $\\vec{R}$ is completely cyclic, the center of mass moves with constant linear momentum $\\vec{P} = M \\dot{\\vec{R}} = \\text{const}$. In the center-of-mass frame ($\\vec{R} = 0$), the problem reduces strictly to a single particle of mass $\\mu$ moving in a static central potential $V(r)$.
"""
        },
        {
            "id": "u3-sec2",
            "title": "Conservation Laws: Planar Motion, Angular Momentum & Areal Velocity",
            "content": """
<h4>1. Confinement to a Fixed Plane of Motion</h4>
The torque exerted by any central force $\\vec{F} = f(r)\\hat{r}$ relative to the force center vanishes identically:
<div class="math-display">$$\\vec{\\tau} = \\vec{r} \\times \\vec{F} = f(r) (\\vec{r} \\times \\hat{r}) = 0$$</div>
Consequently, the orbital angular momentum $\\vec{L}$ is a strict constant of motion:
<div class="math-display">$$\\vec{L} = \\vec{r} \\times \\vec{p} = \\mu (\\vec{r} \\times \\dot{\\vec{r}}) = \\text{constant vector}$$</div>
Since $\\vec{r} \\cdot \\vec{L} = \\vec{r} \\cdot (\\vec{r} \\times \\vec{p}) = 0$, the position vector $\\vec{r}$ remains perpendicular to the fixed direction of $\\vec{L}$ for all time. Thus, <strong>all central force motion is strictly confined to a two-dimensional plane</strong>.

<h4>2. Polar Coordinate Representation & Kepler's Second Law</h4>
Choosing plane polar coordinates $(r, \\theta)$ in the orbital plane:
<div class="math-display">$$\\vec{r} = r \\hat{r}, \\quad \\dot{\\vec{r}} = \\dot{r} \\hat{r} + r \\dot{\\theta} \\hat{\\theta}$$</div>
The magnitude of the angular momentum is:
<div class="math-display">$$l = |\\vec{L}| = \\mu r^2 \\dot{\\theta} = \\text{constant}$$</div>
The area swept out by the radius vector in time $dt$ is $dA = \\frac{1}{2} r (r d\\theta) = \\frac{1}{2} r^2 \\dot{\\theta} dt$. The <strong>areal velocity</strong> is therefore:
<div class="math-display">$$\\frac{dA}{dt} = \\frac{1}{2} r^2 \\dot{\\theta} = \\frac{l}{2\\mu} = \\text{constant}$$</div>
<p><strong>Kepler's Second Law:</strong> The radius vector from the force center to the body sweeps out equal areas in equal intervals of time. This law holds universally for <em>any</em> central force, regardless of whether it follows an inverse-square law.</p>
"""
        },
        {
            "id": "u3-sec3",
            "title": "The Effective Potential Energy & Classification of Orbits",
            "content": """
<h4>1. Total Energy in Radial Coordinates</h4>
The total mechanical energy in polar coordinates is:
<div class="math-display">$$E = T + V = \\frac{1}{2}\\mu (\\dot{r}^2 + r^2 \\dot{\\theta}^2) + V(r)$$</div>
Eliminating $\\dot{\\theta}$ using the conserved angular momentum $\\dot{\\theta} = \\frac{l}{\\mu r^2}$:
<div class="math-display">$$E = \\frac{1}{2}\\mu \\dot{r}^2 + \\frac{l^2}{2\\mu r^2} + V(r) = \\frac{1}{2}\\mu \\dot{r}^2 + V_{\\text{eff}}(r)$$</div>

<h4>2. The Effective Potential $V_{\\text{eff}}(r)$</h4>
The dynamics of the radial coordinate $r(t)$ behaves identically to a 1D particle of mass $\\mu$ in an <strong>effective potential</strong>:
<div class="math-display">$$V_{\\text{eff}}(r) = V(r) + \\frac{l^2}{2\\mu r^2}$$</div>
The term $\\frac{l^2}{2\\mu r^2}$ is the <strong>centrifugal potential barrier</strong>, representing the kinetic energy associated with angular rotation. As $r \\to 0$, this barrier diverges as $+1/r^2$, preventing particles with non-zero angular momentum ($l \\neq 0$) from falling into the center.

<h4>3. Classification of Orbits for Inverse-Square Gravity ($V(r) = -k/r$)</h4>
<div class="math-display">$$V_{\\text{eff}}(r) = -\\frac{k}{r} + \\frac{l^2}{2\\mu r^2}$$</div>
Setting $\\frac{dV_{\\text{eff}}}{dr} = 0$:
<div class="math-display">$$\\frac{k}{r_0^2} - \\frac{l^2}{\\mu r_0^3} = 0 \\implies r_0 = \\frac{l^2}{\\mu k}$$</div>
The minimum value of the effective potential is:
<div class="math-display">$$V_{\\text{min}} = -\\frac{\\mu k^2}{2 l^2}$$</div>
Orbit classification based on total energy $E$:
<ul>
  <li><strong>$E = V_{\\text{min}} = -\\frac{\\mu k^2}{2 l^2}$ (Circular Orbit):</strong> $\\dot{r} = 0$ constantly; orbit is a circle of radius $r = r_0$ ($e = 0$).</li>
  <li><strong>$V_{\\text{min}} < E < 0$ (Elliptical Orbit):</strong> Bound orbit oscillating between periapsis $r_{\\text{min}}$ and apoapsis $r_{\\text{max}}$ ($0 < e < 1$).</li>
  <li><strong>$E = 0$ (Parabolic Orbit):</strong> Unbound orbit with escape velocity; particle reaches infinity with zero residual kinetic energy ($e = 1$).</li>
  <li><strong>$E > 0$ (Hyperbolic Orbit):</strong> Unbound scattering orbit; particle approaches from infinity and deflects off with non-zero residual velocity ($e > 1$).</li>
</ul>
"""
        },
        {
            "id": "u3-sec4",
            "title": "Binet's Equation & Kepler's Inverse-Square Orbits",
            "content": """
<h4>1. Derivation of Binet's Differential Orbit Equation</h4>
To determine the geometric trajectory $r(\\theta)$ directly without solving for time $t$, we substitute $u = 1/r$. The radial velocity is:
<div class="math-display">$$\\dot{r} = \\frac{d}{dt}\\left(\\frac{1}{u}\\right) = -\\frac{1}{u^2}\\frac{du}{d\\theta}\\dot{\\theta} = -\\frac{1}{u^2}\\frac{du}{d\\theta}\\left(\\frac{l u^2}{\\mu}\\right) = -\\frac{l}{\\mu}\\frac{du}{d\\theta}$$</div>
Differentiating once more with respect to $t$:
<div class="math-display">$$\\ddot{r} = -\\frac{l}{\\mu}\\frac{d^2u}{d\\theta^2}\\dot{\\theta} = -\\frac{l^2 u^2}{\\mu^2}\\frac{d^2u}{d\\theta^2}$$</div>
Substituting $\\ddot{r}$ into the radial equation of motion $\\mu(\\ddot{r} - r\\dot{\\theta}^2) = f(r)$:
<div class="math-display">$$-\\frac{l^2 u^2}{\\mu}\\frac{d^2u}{d\\theta^2} - \\frac{l^2 u^3}{\\mu} = f(1/u)$$</div>
Multiplying by $-\\frac{\\mu}{l^2 u^2}$ yields <strong>Binet's Formula</strong>:
<div class="math-display">$$\\frac{d^2u}{d\\theta^2} + u = -\\frac{\\mu}{l^2 u^2} f(1/u)$$</div>

<h4>2. Exact Solution for the Gravitational Force ($f(r) = -k/r^2 = -k u^2$)</h4>
Substituting $f(1/u) = -k u^2$:
<div class="math-display">$$\\frac{d^2u}{d\\theta^2} + u = \\frac{\\mu k}{l^2}$$</div>
This is an inhomogeneous linear second-order differential equation with constant coefficients. Its general solution is:
<div class="math-display">$$u(\\theta) = \\frac{\\mu k}{l^2} + A \\cos(\\theta - \\theta_0)$$</div>
Setting $\\theta_0 = 0$ along the periapsis direction and defining the semi-latus rectum $p$ and eccentricity $e$:
<div class="math-display">$$p = \\frac{l^2}{\\mu k}, \\quad e = \\frac{A l^2}{\\mu k}$$</div>
Inverting $u = 1/r$ delivers the universal polar equation of conic sections:
<div class="math-display">$$r(\\theta) = \\frac{p}{1 + e \\cos \\theta}$$</div>
The orbital eccentricity is related to total energy $E$ by:
<div class="math-display">$$e = \\sqrt{1 + \\frac{2 E l^2}{\\mu k^2}}$$</div>

<h4>3. Kepler's Three Laws Derived</h4>
<ol>
  <li><strong>First Law (Law of Ellipses):</strong> For bound states ($E < 0$), $0 \\le e < 1$; the trajectory $r(\\theta)$ is an ellipse with the gravitational center at one focus.</li>
  <li><strong>Second Law (Law of Equal Areas):</strong> Areal velocity $dA/dt = l/(2\\mu)$ is constant.</li>
  <li><strong>Third Law (Harmonic Law):</strong> The area of an ellipse is $A = \\pi a b$, where $a = p/(1-e^2)$ is the semi-major axis and $b = a\\sqrt{1-e^2} = \\sqrt{a p} = l\\sqrt{a}/\\sqrt{\\mu k}$ is the semi-minor axis. The orbital period $\\tau$ is:
  <div class="math-display">$$\\tau = \\frac{\\text{Area}}{dA/dt} = \\frac{\\pi a b}{l / (2\\mu)} = \\frac{2\\pi \\mu a b}{l} = 2\\pi a^{3/2} \\sqrt{\\frac{\\mu}{k}}$$</div>
  Squaring both sides and setting $k = G m_1 m_2$ and $\\mu = m_1 m_2 / (m_1 + m_2)$:
  <div class="math-display">$$\\tau^2 = \\frac{4\\pi^2 a^3}{G(m_1 + m_2)}$$</div></li>
</ol>
"""
        },
        {
            "id": "u3-sec5",
            "title": "The Laplace-Runge-Lenz Vector & The Virial Theorem",
            "content": """
<h4>1. The Laplace-Runge-Lenz (LRL) Conserved Vector</h4>
In addition to energy $E$ and angular momentum $\\vec{L}$, the $1/r$ Kepler potential possesses an additional conserved vector quantity, the <strong>Laplace-Runge-Lenz vector</strong> $\\vec{A}$:
<div class="math-display">$$\\vec{A} = \\vec{p} \\times \\vec{L} - \\mu k \\hat{r}$$</div>
Proof of conservation:
<div class="math-display">$$\\frac{d\\vec{A}}{dt} = \\dot{\\vec{p}} \\times \\vec{L} - \\mu k \\dot{\\hat{r}}$$</div>
Since $\\dot{\\vec{p}} = -\\frac{k}{r^2}\\hat{r}$ and $\\vec{L} = \\mu \\vec{r} \\times \\dot{\\vec{r}}$:
<div class="math-display">$$\\dot{\\vec{p}} \\times \\vec{L} = -\\frac{\\mu k}{r^2} [\\hat{r} \\times (\\vec{r} \\times \\dot{\\vec{r}})] = -\\frac{\\mu k}{r^2} [r \\dot{\\vec{r}} - (\\hat{r} \\cdot \\dot{\\vec{r}})\\vec{r}] = -\\mu k \\left( \\frac{\\dot{\\vec{r}}}{r} - \\frac{\\dot{r}\\vec{r}}{r^2} \\right) = -\\mu k \\dot{\\hat{r}}$$</div>
Thus $\\frac{d\\vec{A}}{dt} = -\\mu k \\dot{\\hat{r}} - (-\\mu k \\dot{\\hat{r}}) = 0$.
<p><strong>Physical Significance:</strong> The vector $\\vec{A}$ lies permanently in the orbital plane, pointing directly from the focus toward the periapsis with magnitude $|\\vec{A}| = \\mu k e$. Its constancy prevents orbital precession, ensuring that Keplerian orbits are strictly closed. In modern physics, this reflects an underlying dynamic $SO(4)$ symmetry.</p>

<h4>2. The Virial Theorem for Central Potentials</h4>
Consider the quantity $G = \\sum_{i=1}^N \\vec{p}_i \\cdot \\vec{r}_i$. Its time derivative is:
<div class="math-display">$$\\frac{dG}{dt} = \\sum_{i=1}^N \\dot{\\vec{p}}_i \\cdot \\vec{r}_i + \\sum_{i=1}^N \\vec{p}_i \\cdot \\dot{\\vec{r}}_i = \\sum_{i=1}^N \\vec{F}_i \\cdot \\vec{r}_i + 2 T$$</div>
Taking the long-term time average $\\langle X \\rangle = \\lim_{\\tau \\to \\infty} \\frac{1}{\\tau} \\int_0^\\tau X dt$:
<div class="math-display">$$\\left\\langle \\frac{dG}{dt} \\right\\rangle = \\lim_{\\tau \\to \\infty} \\frac{G(\\tau) - G(0)}{\\tau} = 0$$</div>
since for bound systems $G(t)$ remains bounded. Hence:
<div class="math-display">$$2\\langle T \\rangle = -\\left\\langle \\sum_{i=1}^N \\vec{F}_i \\cdot \\vec{r}_i \\right\\rangle$$</div>
For power-law potentials $V(r) = a r^n$, $\\vec{F} = -\\nabla V = -n a r^{n-2} \\vec{r}$, so $\\vec{F} \\cdot \\vec{r} = -n V(r)$. This yields the <strong>Virial Theorem</strong>:
<div class="math-display">$$2\\langle T \\rangle = n \\langle V \\rangle$$</div>
<ul>
  <li><strong>Gravitational / Coulomb Potential ($n = -1$):</strong> $2\\langle T \\rangle = -\\langle V \\rangle \\implies E = \\langle T \\rangle + \\langle V \\rangle = -\\langle T \\rangle = \\frac{1}{2}\\langle V \\rangle$.</li>
  <li><strong>Harmonic Oscillator ($n = 2$):</strong> $2\\langle T \\rangle = 2\\langle V \\rangle \\implies \\langle T \\rangle = \\langle V \\rangle = \\frac{1}{2} E$.</li>
</ul>
"""
        },
        {
            "id": "u3-sec6",
            "title": "Classical Scattering in a Central Field & Rutherford Formula",
            "content": """
<h4>1. Kinematics of Elastic Scattering</h4>
Consider a projectile of mass $m$ and initial speed $v_0$ incident from infinity with <strong>impact parameter</strong> $b$ (the perpendicular distance from the scattering center to the incident velocity line). The total angular momentum and energy are:
<div class="math-display">$$l = m v_0 b = b \\sqrt{2m E}, \\quad E = \\frac{1}{2}m v_0^2$$</div>

<h4>2. The Scattering Angle $\\Theta$</h4>
From the orbital equation in polar coordinates:
<div class="math-display">$$\\Theta = \\pi - 2 \\int_{r_{\\text{min}}}^\\infty \\frac{\\frac{l}{r^2} dr}{\\sqrt{2m [E - V(r)] - \\frac{l^2}{r^2}}}$$</div>
For a repulsive Coulomb potential $V(r) = \\frac{k}{r} = \\frac{q_1 q_2}{4\\pi \\varepsilon_0 r}$, evaluating the integral delivers the relation between impact parameter $b$ and scattering angle $\\theta$:
<div class="math-display">$$b = \\frac{k}{2E} \\cot\\left(\\frac{\\theta}{2}\\right)$$</div>

<h4>3. The Differential Scattering Cross-Section</h4>
Particles incident within an annular area $d\\sigma = 2\\pi b db$ scatter into a solid angle $d\\Omega = 2\\pi \\sin\\theta d\\theta$. The <strong>differential cross-section</strong> $\\frac{d\\sigma}{d\\Omega}$ is:
<div class="math-display">$$\\frac{d\\sigma}{d\\Omega} = \\frac{b}{\\sin\\theta} \\left| \\frac{db}{d\\theta} \\right|$$</div>
Differentiating $b(\\theta)$:
<div class="math-display">$$\\left| \\frac{db}{d\\theta} \\right| = \\frac{k}{4E} \\csc^2\\left(\\frac{\\theta}{2}\\right)$$</div>
Using $\\sin\\theta = 2 \\sin(\\theta/2) \\cos(\\theta/2)$:
<div class="math-display">$$\\frac{d\\sigma}{d\\Omega} = \\frac{\\frac{k}{2E}\\cot(\\theta/2)}{2\\sin(\\theta/2)\\cos(\\theta/2)} \\frac{k}{4E}\\csc^2(\\theta/2) = \\left( \\frac{k}{4E} \\right)^2 \\frac{1}{\\sin^4(\\theta/2)}$$</div>
Substituting $k = \\frac{q_1 q_2}{4\\pi \\varepsilon_0}$ yields the celebrated <strong>Rutherford Scattering Formula</strong>:
<div class="math-display">$$\\frac{d\\sigma}{d\\Omega} = \\left( \\frac{q_1 q_2}{16\\pi \\varepsilon_0 E} \\right)^2 \\frac{1}{\\sin^4(\\theta/2)}$$</div>
"""
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
    ]
}

# Unit 4: The Rigid Body Motion
u4 = {
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
            "content": """
<h4>1. Degrees of Freedom of an Ideal Rigid Body</h4>
A <strong>rigid body</strong> is an idealized assembly of $N$ particles where the inter-particle distances remain invariant under all forces:
<div class="math-display">$$|\\vec{r}_i - \\vec{r}_j| = c_{ij} = \\text{constant}, \\quad \\forall i, j$$</div>
Specifying the position of 3 non-collinear particles requires 9 coordinates subject to 3 internal distance constraints, yielding <strong>6 independent degrees of freedom</strong>:
<ul>
  <li><strong>3 Translational Degrees of Freedom:</strong> Specifying the position vector $\\vec{R}$ of the center of mass in the space-fixed inertial frame.</li>
  <li><strong>3 Rotational Degrees of Freedom:</strong> Specifying the orientation of a body-fixed coordinate frame relative to the space-fixed frame.</li>
</ul>

<h4>2. Orthogonal Transformations</h4>
Let $\\vec{r} = (x, y, z)^T$ be the coordinates of a vector in the space-fixed frame and $\\vec{r}' = (x', y', z')^T$ in the rotated frame. The linear transformation is:
<div class="math-display">$$\\vec{r}' = \\mathbf{A} \\vec{r}, \\quad x_i' = \\sum_{j=1}^3 A_{ij} x_j$$</div>
Invariance of vector length requires $\\vec{r}' \\cdot \\vec{r}' = \\vec{r} \\cdot \\vec{r}$:
<div class="math-display">$$(\\mathbf{A}\\vec{r})^T (\\mathbf{A}\\vec{r}) = \\vec{r}^T (\\mathbf{A}^T \\mathbf{A}) \\vec{r} = \\vec{r}^T \\mathbf{I} \\vec{r}$$</div>
This necessitates the <strong>orthogonality condition</strong>:
<div class="math-display">$$\\mathbf{A}^T \\mathbf{A} = \\mathbf{A} \\mathbf{A}^T = \\mathbf{I} \\implies \\sum_{k=1}^3 A_{ki} A_{kj} = \\delta_{ij}$$</div>
Taking the determinant: $\\det(\\mathbf{A}^T \\mathbf{A}) = (\\det \\mathbf{A})^2 = 1 \\implies \\det \\mathbf{A} = \\pm 1$.
For proper physical rotations (preserving coordinate handedness), $\\det \\mathbf{A} = +1$. The set of all such transformation matrices forms the special orthogonal Lie group $\\mathbf{SO(3)}$.
"""
        },
        {
            "id": "u4-sec2",
            "title": "The Eulerian Angles & Euler's Rotation Theorem",
            "content": """
<h4>1. Standard Eulerian Angle Parameterization</h4>
To transform an initial space-fixed coordinate system $(x, y, z)$ into an arbitrary body-fixed system $(x', y', z')$, Leonhard Euler defined three successive rotations parameterized by the <strong>Eulerian angles</strong> $(\\phi, \\theta, \\psi)$:
<ol>
  <li><strong>Precession (Angle $\\phi$):</strong> Rotation counter-clockwise by angle $\\phi$ about the initial $z$-axis ($0 \\le \\phi < 2\\pi$). The resulting line of nodes $\\xi$ lies along the intersection of the $(x, y)$ and $(x', y')$ planes:
  <div class="math-display">$$\\mathbf{D}(\\phi) = \\begin{pmatrix} \\cos \\phi & \\sin \\phi & 0 \\\\ -\\sin \\phi & \\cos \\phi & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$$</div></li>
  <li><strong>Nutation (Angle $\\theta$):</strong> Rotation by angle $\\theta$ about the intermediate line of nodes $\\xi$ ($0 \\le \\theta \\le \\pi$):
  <div class="math-display">$$\\mathbf{C}(\\theta) = \\begin{pmatrix} 1 & 0 & 0 \\\\ 0 & \\cos \\theta & \\sin \\theta \\\\ 0 & -\\sin \\theta & \\cos \\theta \\end{pmatrix}$$</div></li>
  <li><strong>Intrinsic Body Spin (Angle $\\psi$):</strong> Rotation by angle $\\psi$ about the final body-fixed $z'$-axis ($0 \\le \\psi < 2\\pi$):
  <div class="math-display">$$\\mathbf{B}(\\psi) = \\begin{pmatrix} \\cos \\psi & \\sin \\psi & 0 \\\\ -\\sin \\psi & \\cos \\psi & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$$</div></li>
</ol>
The composite rotation matrix $\\mathbf{A} = \\mathbf{B}(\\psi) \\mathbf{C}(\\theta) \\mathbf{D}(\\phi)$ transforms space coordinates into body coordinates.

<h4>2. Angular Velocity Vector in Terms of Euler Angles</h4>
Projecting the rates of change $(\\dot{\\phi}, \\dot{\\theta}, \\dot{\\psi})$ onto the body-fixed axes $(x', y', z')$ yields the instantaneous angular velocity $\\vec{\\omega}$:
<div class="math-display">$$\\omega_{x'} = \\dot{\\phi} \\sin \\theta \\sin \\psi + \\dot{\\theta} \\cos \\psi$$</div>
<div class="math-display">$$\\omega_{y'} = \\dot{\\phi} \\sin \\theta \\cos \\psi - \\dot{\\theta} \\sin \\psi$$</div>
<div class="math-display">$$\\omega_{z'} = \\dot{\\phi} \\cos \\theta + \\dot{\\psi}$$</div>
"""
        },
        {
            "id": "u4-sec3",
            "title": "The Inertia Tensor, Dyadics & Principal Axes of Inertia",
            "content": """
<h4>1. Angular Momentum and the Inertia Tensor</h4>
For a rigid body rotating with instantaneous angular velocity $\\vec{\\omega}$ about a fixed point (or about its center of mass), the velocity of each point mass is $\\vec{v}_i = \\vec{\\omega} \\times \\vec{r}_i$. The total angular momentum is:
<div class="math-display">$$\\vec{L} = \\sum_{i=1}^N m_i \\vec{r}_i \\times (\\vec{\\omega} \\times \\vec{r}_i) = \\sum_{i=1}^N m_i [r_i^2 \\vec{\\omega} - (\\vec{r}_i \\cdot \\vec{\\omega})\\vec{r}_i]$$</div>
In component notation, this linear relationship is written as $\\vec{L} = \\mathbf{I} \\vec{\\omega}$:
<div class="math-display">$$L_j = \\sum_{k=1}^3 I_{jk} \\omega_k$$</div>
where $\\mathbf{I}$ is the rank-2 symmetric <strong>inertia tensor</strong>:
<div class="math-display">$$I_{jk} = \\int \\rho(\\vec{r}) (r^2 \\delta_{jk} - x_j x_k) dV$$</div>
The diagonal components are the <strong>moments of inertia</strong>:
<div class="math-display">$$I_{xx} = \\int (y^2 + z^2) dm, \\quad I_{yy} = \\int (x^2 + z^2) dm, \\quad I_{zz} = \\int (x^2 + y^2) dm$$</div>
The off-diagonal components are the <strong>products of inertia</strong>:
<div class="math-display">$$I_{xy} = I_{yx} = -\\int x y dm, \\quad I_{yz} = I_{zy} = -\\int y z dm, \\quad I_{xz} = I_{zx} = -\\int x z dm$$</div>

<h4>2. Rotational Kinetic Energy</h4>
The rotational kinetic energy is a quadratic form in angular velocities:
<div class="math-display">$$T_{\\text{rot}} = \\frac{1}{2} \\sum_{i=1}^N m_i v_i^2 = \\frac{1}{2} \\vec{\\omega} \\cdot \\vec{L} = \\frac{1}{2} \\sum_{j=1}^3 \\sum_{k=1}^3 I_{jk} \\omega_j \\omega_k = \\frac{1}{2} \\vec{\\omega}^T \\mathbf{I} \\vec{\\omega}$$</div>

<h4>3. Principal Axes of Inertia & Diagonalization</h4>
Because the inertia matrix $\\mathbf{I}$ is real and symmetric, the spectral theorem guarantees the existence of an orthogonal basis of eigenvectors called the <strong>principal axes of inertia</strong>. In this frame, all products of inertia vanish, and $\\mathbf{I}$ becomes purely diagonal:
<div class="math-display">$$\\mathbf{I} = \\begin{pmatrix} I_1 & 0 & 0 \\\\ 0 & I_2 & 0 \\\\ 0 & 0 & I_3 \\end{pmatrix}$$</div>
where $I_1, I_2, I_3$ are the <strong>principal moments of inertia</strong>. The rotational kinetic energy and angular momentum simplify to:
<div class="math-display">$$T_{\\text{rot}} = \\frac{1}{2} I_1 \\omega_1^2 + \\frac{1}{2} I_2 \\omega_2^2 + \\frac{1}{2} I_3 \\omega_3^2$$</div>
<div class="math-display">$$\\vec{L} = I_1 \\omega_1 \\hat{e}_1 + I_2 \\omega_2 \\hat{e}_2 + I_3 \\omega_3 \\hat{e}_3$$</div>
"""
        },
        {
            "id": "u4-sec4",
            "title": "Euler's Equations of Motion for Rigid Bodies",
            "content": """
<h4>1. Time Derivatives in Rotating Reference Frames</h4>
Let an arbitrary vector $\\vec{G}$ be observed in both an inertial space-fixed frame and a body-fixed frame rotating with angular velocity $\\vec{\\omega}$. The operator relation between time rates of change is:
<div class="math-display">$$\\left(\\frac{d\\vec{G}}{dt}\\right)_{\\text{space}} = \\left(\\frac{d\\vec{G}}{dt}\\right)_{\\text{body}} + \\vec{\\omega} \\times \\vec{G}$$</div>

<h4>2. Derivation of Euler's Dynamical Equations</h4>
Newtonian mechanics requires that the rate of change of total angular momentum in the space frame equals the net external torque: $\\left(\\frac{d\\vec{L}}{dt}\\right)_{\\text{space}} = \\vec{N}^{\\text{ext}}$.
Applying the rotating frame relation:
<div class="math-display">$$\\left(\\frac{d\\vec{L}}{dt}\\right)_{\\text{body}} + \\vec{\\omega} \\times \\vec{L} = \\vec{N}$$</div>
Expressing this vector equation along the body's <strong>principal axes of inertia</strong> where $L_1 = I_1 \\omega_1$, $L_2 = I_2 \\omega_2$, $L_3 = I_3 \\omega_3$:
<div class="math-display">$$(\\vec{\\omega} \\times \\vec{L})_1 = \\omega_2 L_3 - \\omega_3 L_2 = (I_3 - I_2) \\omega_2 \\omega_3$$</div>
This yields <strong>Euler's Equations of Motion</strong>:
<div class="math-display">$$I_1 \\dot{\\omega}_1 - (I_2 - I_3) \\omega_2 \\omega_3 = N_1$$</div>
<div class="math-display">$$I_2 \\dot{\\omega}_2 - (I_3 - I_1) \\omega_3 \\omega_1 = N_2$$</div>
<div class="math-display">$$I_3 \\dot{\\omega}_3 - (I_1 - I_2) \\omega_1 \\omega_2 = N_3$$</div>
<p>These coupled nonlinear first-order differential equations govern the time evolution of the body-fixed angular velocity components under external torques $N_i$.</p>
"""
        },
        {
            "id": "u4-sec5",
            "title": "Torque-Free Motion & The Heavy Symmetrical Top",
            "content": """
<h4>1. Torque-Free Motion of a Symmetrical Top ($N_i = 0$, $I_1 = I_2 \\neq I_3$)</h4>
Setting torques to zero and $I_1 = I_2$, Euler's equations become:
<div class="math-display">$$I_1 \\dot{\\omega}_1 = (I_1 - I_3) \\omega_2 \\omega_3$$</div>
<div class="math-display">$$I_1 \\dot{\\omega}_2 = -(I_1 - I_3) \\omega_1 \\omega_3$$</div>
<div class="math-display">$$I_3 \\dot{\\omega}_3 = 0 \\implies \\omega_3 = \\text{constant}$$</div>
Defining the constant precession frequency $\\Omega_{\\text{prec}} = \\frac{I_1 - I_3}{I_1} \\omega_3$:
<div class="math-display">$$\\dot{\\omega}_1 = \\Omega_{\\text{prec}} \\omega_2, \\quad \\dot{\\omega}_2 = -\\Omega_{\\text{prec}} \\omega_1$$</div>
Differentiating again yields $\\ddot{\\omega}_1 + \\Omega_{\\text{prec}}^2 \\omega_1 = 0$. The angular velocity vector $\\vec{\\omega}$ precesses uniformly around the body symmetry axis ($z'$) with frequency $\\Omega_{\\text{prec}}$.

<h4>2. The Heavy Symmetrical Top with Fixed Pivot</h4>
Consider a symmetric top ($I_1 = I_2$) spinning under gravity with its apex supported at a fixed pivot. The Lagrangian in Eulerian angles $(\\phi, \\theta, \\psi)$ is:
<div class="math-display">$$L = \\frac{1}{2}I_1 (\\dot{\\theta}^2 + \\dot{\\phi}^2 \\sin^2 \\theta) + \\frac{1}{2}I_3 (\\dot{\\phi} \\cos \\theta + \\dot{\\psi})^2 - M g l \\cos \\theta$$</div>
Coordinates $\\phi$ (precession) and $\\psi$ (spin) are cyclic:
<div class="math-display">$$p_\\phi = I_1 \\dot{\\phi} \\sin^2 \\theta + I_3 (\\dot{\\phi} \\cos \\theta + \\dot{\\psi}) \\cos \\theta = \\text{const}$$</div>
<div class="math-display">$$p_\\psi = I_3 (\\dot{\\phi} \\cos \\theta + \\dot{\\psi}) = I_3 \\omega_3 = \\text{const}$$</div>
The nutation angle $\\theta(t)$ oscillates between two turning points $\\theta_1$ and $\\theta_2$ governed by an effective potential.

<h4>3. The Sleeping Top Stability Condition</h4>
When a top spins vertically upright ($\\theta = 0$, the "sleeping top"), small perturbations are stable if and only if the spin angular velocity exceeds the critical threshold:
<div class="math-display">$$\\omega_3^2 \\ge \\frac{4 M g l I_1}{I_3^2}$$</div>
If friction slows $\\omega_3$ below this limit, the vertical state undergoes a bifurcation and the top begins to wobble (nutate) wildly.
"""
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
    ]
}

with open("cm_u3.json", "w", encoding="utf-8") as f:
    json.dump(u3, f, indent=2)

with open("cm_u4.json", "w", encoding="utf-8") as f:
    json.dump(u4, f, indent=2)

print("cm_u3.json and cm_u4.json generated successfully!")
