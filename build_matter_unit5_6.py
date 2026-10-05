# Build Script for Units 5 and 6: Oscillations and Traveling Waves
import json

# =========================================================================
# UNIT 5: Oscillations
# =========================================================================
u5_sections = [
    {
        "id": "sec-5-1",
        "number": "§5.1",
        "heading": "Harmonic Motion and Simple Harmonic Motion (SHM)",
        "simulation": "shm-resonance-sim",
        "content": """Periodic motion is any motion that repeats itself identically at regular intervals of time $T$. Harmonic motion is periodic motion where the restoring mechanism is directly proportional to displacement.

<h4>1. Definition and Kinematics of SHM</h4>
A particle executes <strong>Simple Harmonic Motion (SHM)</strong> when the restoring force acting on it is directly proportional to its displacement from equilibrium and directed toward that equilibrium position:
$$F = -k x$$
where $k$ is the force constant (stiffness) in N/m. By Newton's second law ($F = m \\ddot{x}$):
$$m \\frac{d^2 x}{dt^2} + k x = 0 \\implies \\frac{d^2 x}{dt^2} + \\omega_0^2 x = 0$$
where $\\omega_0 = \\sqrt{k/m}$ is the <strong>natural undamped angular frequency</strong> (rad/s).
The general harmonic solution is:
$$x(t) = A \\cos(\\omega_0 t + \\phi)$$
where:
<ul>
  <li>$A$: <strong>Amplitude</strong> (maximum displacement from equilibrium).</li>
  <li>$\\omega_0 = 2\\pi f = \\frac{2\\pi}{T}$: Angular frequency.</li>
  <li>$\\phi$: <strong>Initial phase constant</strong> (determined by initial conditions $x(0)$ and $v(0)$).</li>
  <li>$T = 2\\pi \\sqrt{\\frac{m}{k}}$: Period of oscillation (independent of amplitude — <em>isochronism</em>).</li>
</ul>

<h4>2. Velocity and Acceleration</h4>
Differentiating displacement with respect to time:
$$v(t) = \\dot{x}(t) = -\\omega_0 A \\sin(\\omega_0 t + \\phi) = \\omega_0 A \\cos\\left(\\omega_0 t + \\phi + \\frac{\\pi}{2}\\right)$$
$$a(t) = \\ddot{x}(t) = -\\omega_0^2 A \\cos(\\omega_0 t + \\phi) = -\\omega_0^2 x(t) = \\omega_0^2 A \\cos(\\omega_0 t + \\phi + \\pi)$$
Key phase relationships:
<ul>
  <li>Velocity leads displacement by $\\frac{\\pi}{2}$ radians (90°). Maximum speed $v_{max} = \\omega_0 A$ occurs at equilibrium ($x = 0$).</li>
  <li>Acceleration leads displacement by $\\pi$ radians (180°). Maximum acceleration $a_{max} = \\omega_0^2 A$ occurs at maximum displacement ($x = \\pm A$).</li>
</ul>
Eliminating time between $x$ and $v$ yields the elliptical phase space trajectory:
$$v(x) = \\pm \\omega_0 \\sqrt{A^2 - x^2} \\implies \\frac{x^2}{A^2} + \\frac{v^2}{\\omega_0^2 A^2} = 1$$"""
    },
    {
        "id": "sec-5-2",
        "number": "§5.2",
        "heading": "Energy Considerations in Simple Harmonic Motion",
        "simulation": "shm-resonance-sim",
        "content": """Simple harmonic motion is a conservative mechanical system where potential energy and kinetic energy continuously transform into one another while total mechanical energy remains invariant.

<h4>1. Kinetic and Potential Energy</h4>
<ul>
  <li><strong>Kinetic Energy ($T$):</strong>
  $$T(t) = \\frac{1}{2}m v^2 = \\frac{1}{2}m \\omega_0^2 A^2 \\sin^2(\\omega_0 t + \\phi) = \\frac{1}{2}k (A^2 - x^2)$$</li>
  <li><strong>Potential Energy ($V$):</strong> Work done against the restoring force $F = -kx$:
  $$V(x) = -\\int_0^x (-k x') dx' = \\frac{1}{2}k x^2 = \\frac{1}{2}k A^2 \\cos^2(\\omega_0 t + \\phi)$$</li>
</ul>

<h4>2. Conservation of Total Energy</h4>
Summing kinetic and potential energies:
$$E = T + V = \\frac{1}{2}k A^2 \\left[ \\sin^2(\\omega_0 t + \\phi) + \\cos^2(\\omega_0 t + \\phi) \\right] = \\frac{1}{2}k A^2 = \\frac{1}{2}m \\omega_0^2 A^2 = \\text{constant}$$
The total mechanical energy is proportional to the square of the amplitude and independent of time and position.
At the turning points ($x = \\pm A$), velocity vanishes, and energy is purely potential ($E = V_{max} = \\frac{1}{2}kA^2$).
At the equilibrium position ($x = 0$), potential energy vanishes, and energy is purely kinetic ($E = T_{max} = \\frac{1}{2}m v_{max}^2$).

<h4>3. Time-Averaged Energies and the Virial Theorem</h4>
Averaging over a complete oscillation period $T = 2\\pi / \\omega_0$:
$$\\langle \\sin^2(\\omega_0 t + \\phi) \\rangle = \\frac{1}{T}\\int_0^T \\sin^2(\\omega_0 t + \\phi) dt = \\frac{1}{2}$$
$$\\langle \\cos^2(\\omega_0 t + \\phi) \\rangle = \\frac{1}{2}$$
Therefore:
$$\\langle T \\rangle = \\frac{1}{4} k A^2 = \\frac{1}{2}E, \\quad \\langle V \\rangle = \\frac{1}{4} k A^2 = \\frac{1}{2}E$$
$$\\langle T \\rangle = \\langle V \\rangle = \\frac{1}{2}E$$
This exact equipartition of average kinetic and potential energy is a direct consequence of the <strong>Virial Theorem</strong> for harmonic potentials ($V \\propto x^2$)."""
    },
    {
        "id": "sec-5-3",
        "number": "§5.3",
        "heading": "Applications of SHM: Simple, Compound, and Torsion Pendulums",
        "simulation": "shm-resonance-sim",
        "content": """Simple harmonic motion governs a multitude of oscillating mechanical and structural devices.

<h4>1. Simple Pendulum</h4>
A point mass $m$ suspended by an inextensible massless string of length $L$.
Restoring torque about suspension point $O$:
$$\\tau = -m g L \\sin\\theta = I \\alpha = (m L^2) \\frac{d^2\\theta}{dt^2}$$
$$\\frac{d^2\\theta}{dt^2} + \\frac{g}{L}\\sin\\theta = 0$$
For small angular displacements ($\sin\\theta \\approx \\theta$ in radians):
$$\\frac{d^2\\theta}{dt^2} + \\omega_0^2 \\theta = 0 \\implies \\omega_0 = \\sqrt{\\frac{g}{L}}, \\quad T = 2\\pi \\sqrt{\\frac{L}{g}}$$

<h4>2. Compound (Physical) Pendulum</h4>
A rigid body of arbitrary shape and mass $M$ free to oscillate in a vertical plane about a horizontal knife-edge axis $O$.
Let $d$ be the distance from the pivot $O$ to the center of mass $G$, and $I$ the moment of inertia about $O$.
By the parallel axis theorem: $I = I_G + M d^2 = M (k_g^2 + d^2)$, where $k_g$ is the radius of gyration about $G$.
The restoring torque is:
$$\\tau = -M g d \\sin\\theta \\approx -M g d \\theta$$
$$I \\frac{d^2\\theta}{dt^2} + M g d \\theta = 0 \\implies \\frac{d^2\\theta}{dt^2} + \\left(\\frac{M g d}{I}\\right) \\theta = 0$$
The period of oscillation is:
$$T = 2\\pi \\sqrt{\\frac{I}{M g d}} = 2\\pi \\sqrt{\\frac{k_g^2 + d^2}{g d}} = 2\\pi \\sqrt{\\frac{L_{eq}}{g}}$$
where $L_{eq} = \\frac{k_g^2 + d^2}{d} = d + \\frac{k_g^2}{d}$ is the <strong>length of the equivalent simple pendulum</strong>.
<ul>
  <li><strong>Center of Oscillation ($O'$):</strong> A point lying along the line $OG$ at distance $L_{eq}$ from $O$.
  If the body is suspended from $O'$, its period of oscillation is identical to that about $O$ (<em>Theorem of Reversibility</em>, exploited in Kater's reversible pendulum to determine $g$ with parts-per-million accuracy).</li>
  <li><strong>Minimum Period:</strong> Minimizing $L_{eq}(d)$ with respect to $d$:
  $$\\frac{dL_{eq}}{dd} = 1 - \\frac{k_g^2}{d^2} = 0 \\implies d = k_g$$
  The minimum period occurs when the suspension point is at a distance equal to the radius of gyration: $T_{min} = 2\\pi \\sqrt{2 k_g / g}$.</li>
</ul>

<h4>3. Torsional Pendulum</h4>
A disk or cylinder suspended by a thin elastic wire. Twisting by angle $\\theta$ creates a restoring torque $\\tau = -C \\theta$, where $C = \\frac{\\pi \\eta r^4}{2 L}$ is the torsional rigidity of the wire.
$$I \\frac{d^2\\theta}{dt^2} + C \\theta = 0 \\implies T = 2\\pi \\sqrt{\\frac{I}{C}}$$"""
    },
    {
        "id": "sec-5-4",
        "number": "§5.4",
        "heading": "Relation between SHM and Uniform Circular Motion",
        "simulation": "shm-resonance-sim",
        "content": """Simple harmonic motion can be mathematically and visually understood as the one-dimensional orthogonal projection of uniform circular motion.

<h4>1. The Reference Circle and Phasor Representation</h4>
Consider a reference particle $P$ moving counterclockwise along a circle of radius $A$ (called the <strong>reference circle</strong>) with constant angular velocity $\\omega_0$.
At $t = 0$, the radius vector makes an angle $\\phi$ with the positive x-axis. At subsequent time $t$, the angle is $\\theta(t) = \\omega_0 t + \\phi$.
Projecting point $P$ onto the horizontal x-axis yields point $Q$:
$$x(t) = A \\cos(\\omega_0 t + \\phi)$$
Projecting point $P$ onto the vertical y-axis yields point $Q'$:
$$y(t) = A \\sin(\\omega_0 t + \\phi) = A \\cos\\left(\\omega_0 t + \\phi - \\frac{\\pi}{2}\\right)$$
Both projected points $Q$ and $Q'$ execute pure simple harmonic motion with amplitude $A$ and angular frequency $\\omega_0$, separated by a 90° phase difference.

<h4>2. Kinematic Projections</h4>
<ul>
  <li><strong>Velocity:</strong> The linear tangential speed of $P$ on the circle is $v_0 = \\omega_0 A$.
  Its projection on the x-axis gives the SHM velocity:
  $$v_x = -v_0 \\sin(\\omega_0 t + \\phi) = -\\omega_0 A \\sin(\\omega_0 t + \\phi)$$</li>
  <li><strong>Acceleration:</strong> The centripetal acceleration of $P$ directed toward the center is $a_c = \\omega_0^2 A$.
  Its projection on the x-axis gives the SHM acceleration:
  $$a_x = -a_c \\cos(\\omega_0 t + \\phi) = -\\omega_0^2 x(t)$$</li>
</ul>
This phasor technique enables geometric addition of multiple harmonic oscillations using planar vector addition."""
    },
    {
        "id": "sec-5-5",
        "number": "§5.5",
        "heading": "Superposition of Harmonic Motions and Lissajous Figures",
        "simulation": "shm-resonance-sim",
        "content": """When a particle is acted upon by two or more simultaneous harmonic restoring forces, its resultant trajectory is determined by the principle of superposition.

<h4>1. Superposition of Two Collinear SHMs of Identical Frequency</h4>
Let two collinear oscillations along the x-axis be:
$$x_1(t) = A_1 \\cos(\\omega t + \\phi_1), \\quad x_2(t) = A_2 \\cos(\\omega t + \\phi_2)$$
The resultant displacement is $x(t) = x_1(t) + x_2(t) = A \\cos(\\omega t + \\Phi)$, where:
$$A = \\sqrt{A_1^2 + A_2^2 + 2 A_1 A_2 \\cos(\\phi_2 - \\phi_1)}$$
$$\\tan\\Phi = \\frac{A_1 \\sin\\phi_1 + A_2 \\sin\\phi_2}{A_1 \\cos\\phi_1 + A_2 \\cos\\phi_2}$$
<ul>
  <li>If in phase ($\Delta\\phi = 2n\\pi$): $A = A_1 + A_2$ (Constructive).</li>
  <li>If in antiphase ($\Delta\\phi = (2n+1)\\pi$): $A = |A_1 - A_2|$ (Destructive).</li>
</ul>

<h4>2. Superposition of Two Mutually Perpendicular SHMs: Lissajous Figures</h4>
Consider a particle subjected to two orthogonal oscillations:
$$x(t) = A \\cos(\\omega_x t), \\quad y(t) = B \\cos(\\omega_y t + \\delta)$$
The resulting path $(x(t), y(t))$ in the 2D plane is called a <strong>Lissajous Figure</strong> (discovered by Jules Antoine Lissajous, 1857).

<h5>Case A: Equal Frequencies ($\omega_x = \omega_y = \omega$)</h5>
Expanding $y(t)$:
$$\\frac{y}{B} = \\cos(\\omega t)\\cos\\delta - \\sin(\\omega t)\\sin\\delta = \\frac{x}{A}\\cos\\delta - \\sqrt{1 - \\frac{x^2}{A^2}}\\sin\\delta$$
Rearranging and squaring:
$$\\left(\\frac{y}{B} - \\frac{x}{A}\\cos\\delta\\right)^2 = \\left(1 - \\frac{x^2}{A^2}\\right)\\sin^2\\delta$$
$$\\frac{x^2}{A^2} - \\frac{2 x y}{A B}\\cos\\delta + \\frac{y^2}{B^2} = \\sin^2\\delta$$
This is the general equation of an oblique ellipse bounded within the rectangle $[-A, A] \\times [-B, B]$:
<ul>
  <li>$\\delta = 0$: Straight line of positive slope $y = (B/A) x$.</li>
  <li>$\\delta = \\pi/2$: Symmetrical upright ellipse $\\frac{x^2}{A^2} + \\frac{y^2}{B^2} = 1$ (circle if $A = B$).</li>
  <li>$\\delta = \\pi$: Straight line of negative slope $y = -(B/A) x$.</li>
  <li>$\\delta = 3\\pi/2$: Upright ellipse traced clockwise.</li>
</ul>

<h5>Case B: Frequency Ratio 1:2 ($\omega_y = 2\\omega_x$)</h5>
$$x = A \\cos(\\omega t), \\quad y = B \\cos(2\\omega t + \\delta)$$
Using $\\cos(2\\theta) = 2\\cos^2\\theta - 1$, when $\\delta = 0$:
$$y = B [2(x/A)^2 - 1]$$
This forms a parabola! For arbitrary phase differences $\\delta$, the curve traces a figure-eight (lemniscate) or distorted loop.
The frequency ratio is determined experimentally by counting tangencies:
$$\\frac{\\omega_x}{\\omega_y} = \\frac{\\text{Number of intersections with vertical line}}{\\text{Number of intersections with horizontal line}}$$"""
    },
    {
        "id": "sec-5-6",
        "number": "§5.6",
        "heading": "Damped Harmonic Motion and the Quality Factor",
        "simulation": "shm-resonance-sim",
        "content": """Real physical oscillators experience dissipative resistive forces (viscous drag, friction) that continually remove mechanical energy.

<h4>1. The Damped Equation of Motion</h4>
Assuming viscous damping where the retarding force is proportional to velocity: $F_d = -b \\dot{x}$, where $b$ is the damping coefficient (N·s/m).
Newton's second law:
$$m \\ddot{x} = -k x - b \\dot{x} \\implies m \\ddot{x} + b \\dot{x} + k x = 0$$
$$\\ddot{x} + 2\\gamma \\dot{x} + \\omega_0^2 x = 0$$
where $\\gamma = \\frac{b}{2m}$ is the <strong>damping attenuation constant</strong> (s⁻¹) and $\\omega_0 = \\sqrt{k/m}$ is the natural frequency.
Seeking solutions of the form $x(t) = e^{\\lambda t}$ yields the auxiliary equation:
$$\\lambda^2 + 2\\gamma \\lambda + \\omega_0^2 = 0 \\implies \\lambda = -\\gamma \\pm \\sqrt{\\gamma^2 - \\omega_0^2}$$

<h4>2. The Three Damping Regimes</h4>
<ol>
  <li><strong>Underdamped Case ($\gamma < \omega_0$):</strong>
  The roots are complex conjugates $\\lambda = -\\gamma \\pm i \\omega_d$, where $\\omega_d = \\sqrt{\\omega_0^2 - \\gamma^2}$ is the damped angular frequency.
  $$x(t) = A_0 e^{-\\gamma t} \\cos(\\omega_d t + \\phi)$$
  The system oscillates with period $T_d = \\frac{2\\pi}{\\omega_d} > T_0$ while its amplitude decays exponentially: $A(t) = A_0 e^{-\\gamma t}$.
  <strong>Logarithmic Decrement ($\delta$):</strong> The natural logarithm of the ratio of two consecutive peak amplitudes separated by one period $T_d$:
  $$\\delta = \\ln\\left( \\frac{x(t)}{x(t + T_d)} \\right) = \\ln\\left( \\frac{A_0 e^{-\\gamma t}}{A_0 e^{-\\gamma (t + T_d)}} \\right) = \\gamma T_d = \\frac{2\\pi \\gamma}{\\omega_d}$$</li>
  <li><strong>Critically Damped Case ($\gamma = \omega_0$):</strong>
  Repeated real root $\\lambda = -\\gamma$. The general solution is:
  $$x(t) = (C_1 + C_2 t) e^{-\\gamma t}$$
  The system returns to equilibrium in the shortest possible time without oscillating (vital for car shock absorbers, galvonometers, and door closers).</li>
  <li><strong>Overdamped Case ($\gamma > \omega_0$):</strong>
  Two unequal negative real roots. The motion is non-oscillatory and dies out sluggishly:
  $$x(t) = C_1 e^{-(\\gamma - \\sqrt{\\gamma^2-\\omega_0^2}) t} + C_2 e^{-(\\gamma + \\sqrt{\\gamma^2-\\omega_0^2}) t}$$</li>
</ol>

<h4>3. The Quality Factor ($Q$)</h4>
The Quality Factor $Q$ quantifies the sharpness of an oscillator and its ability to store energy relative to rate of dissipation:
$$Q = 2\\pi \\left( \\frac{\\text{Energy Stored in System}}{\\text{Energy Dissipated per Cycle}} \\right) = \\frac{\\omega_0}{2\\gamma} = \\frac{\\omega_0 m}{b} = \\frac{\\pi}{\\delta}$$
High-Q oscillators (e.g., quartz crystals with $Q \\sim 10^5$, or optical cavities with $Q \\sim 10^9$) ring for many thousands of cycles before dying out."""
    },
    {
        "id": "sec-5-7",
        "number": "§5.7",
        "heading": "Forced Oscillations and Resonance",
        "simulation": "shm-resonance-sim",
        "content": """When a damped oscillator is driven by a periodic external force $F(t) = F_0 \\cos(\\omega t)$, it undergoes forced oscillations.

<h4>1. Differential Equation and Steady-State Solution</h4>
$$\\ddot{x} + 2\\gamma \\dot{x} + \\omega_0^2 x = \\frac{F_0}{m} \\cos(\\omega t)$$
The complete solution consists of a transient complementary function $x_h(t)$ (which decays as $e^{-\\gamma t}$) plus a steady-state particular solution $x_p(t)$ oscillating at the driving frequency $\\omega$:
$$x(t) = x_{\\text{transient}}(t) + x_{\\text{steady}}(t)$$
After transient decay, the steady-state response is:
$$x(t) = A(\\omega) \\cos(\\omega t - \\phi)$$
where amplitude $A(\\omega)$ and phase lag $\\phi(\\omega)$ are:
$$A(\\omega) = \\frac{F_0 / m}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4 \\gamma^2 \\omega^2}}$$
$$\\tan\\phi(\\omega) = \\frac{2\\gamma \\omega}{\\omega_0^2 - \\omega^2}, \\quad 0 \\le \\phi \\le \\pi$$

<h4>2. Amplitude and Velocity Resonance</h4>
<ul>
  <li><strong>Amplitude Resonance:</strong> Maximizing $A(\\omega)$ by minimizing the denominator:
  $$\\frac{d}{d\\omega}\\left[ (\\omega_0^2 - \\omega^2)^2 + 4\\gamma^2 \\omega^2 \\right] = 2(\\omega_0^2 - \\omega^2)(-2\\omega) + 8\\gamma^2 \\omega = 0$$
  $$\\omega_r = \\sqrt{\\omega_0^2 - 2\\gamma^2}$$
  Resonance occurs slightly below the natural frequency $\\omega_0$.
  The peak amplitude at $\\omega = \\omega_r$ is:
  $$A_{max} = \\frac{F_0 / m}{2\\gamma \\sqrt{\\omega_0^2 - \\gamma^2}} \\approx \\frac{F_0 / m}{2\\gamma \\omega_0} = \\frac{Q F_0}{m \\omega_0^2} = Q \\cdot x_{\\text{static}}$$
  At resonance, amplitude is magnified by exactly the Quality Factor $Q$!</li>
  <li><strong>Velocity (Power) Resonance:</strong> Differentiating $x(t)$ gives velocity amplitude:
  $$v_{max}(\\omega) = \\frac{\\omega F_0 / m}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + 4\\gamma^2 \\omega^2}} = \\frac{F_0 / m}{\\sqrt{(\\frac{\\omega_0^2 - \\omega^2}{\\omega})^2 + 4\\gamma^2}}$$
  The velocity resonance peak occurs exactly at $\\omega = \\omega_0$, where the velocity is in phase with the driving force ($\phi = \\pi/2$).</li>
</ul>

<h4>3. Sharpness of Resonance and Bandwidth (FWHM)</h4>
The average power absorbed by the oscillator is:
$$\\langle P(\\omega) \\rangle = \\frac{1}{2} b v_{max}^2(\\omega) = \\frac{F_0^2 \\gamma \\omega^2 / m}{(\\omega_0^2 - \\omega^2)^2 + 4\\gamma^2 \\omega^2}$$
The half-power frequencies $\\omega_1, \\omega_2$ occur when $\\langle P \\rangle = \\frac{1}{2} P_{max}$:
$$\\Delta \\omega = \\omega_2 - \\omega_1 = 2\\gamma = \\frac{\\omega_0}{Q}$$
The sharpness of resonance is inversely proportional to bandwidth: a high $Q$ produces an extremely narrow, sharp resonance peak."""
    }
]

u5_problems = [
    {
        "id": "prob-5-1",
        "difficulty": "Undergraduate Honors Classical Exam Standard",
        "title": "Compound Pendulum: Equivalent Simple Length and Minimum Period",
        "question": "A uniform slender metal rod of mass $M = 2.40\\text{ kg}$ and length $L = 1.20\\text{ m}$ is pivoted about a horizontal axis passing through a small hole drilled at distance $d$ from its center of mass.\\n(a) Derive the expression for the period of oscillation $T(d)$ in terms of $d$, $L$, and $g$,\\n(b) If the rod is pivoted at a distance $d = 0.300\\text{ m}$ from its center, find the time period $T$ and the length of the equivalent simple pendulum $L_{eq}$, and\\n(c) Determine the position of the pivot $d_{min}$ that minimizes the period of oscillation and calculate that minimum time period $T_{min}$. Take $g = 9.80\\text{ m/s}^2$.",
        "steps": [
            {
                "title": "Step 1: Moment of inertia and period derivation",
                "math": "$$I_G = \\frac{1}{12}M L^2 = M k_g^2 \\implies k_g^2 = \\frac{L^2}{12} = \\frac{(1.20)^2}{12} = 0.120 \\text{ m}^2$$\n$$I = I_G + M d^2 = M(k_g^2 + d^2)$$\n$$T = 2\\pi \\sqrt{\\frac{I}{M g d}} = 2\\pi \\sqrt{\\frac{k_g^2 + d^2}{g d}} = 2\\pi \\sqrt{\\frac{L_{eq}}{g}}$$\n$$L_{eq} = d + \\frac{k_g^2}{d} = d + \\frac{L^2}{12 d}$$",
                "explanation": "The radius of gyration of a uniform slender rod about its center of mass is $k_g = L / \\sqrt{12}$."
            },
            {
                "title": "Step 2: Numerical evaluation at d = 0.300 m",
                "math": "$$L_{eq} = 0.300 + \\frac{0.120}{0.300} = 0.300 + 0.400 = 0.700 \\text{ m}$$\n$$T = 2\\pi \\sqrt{\\frac{0.700}{9.80}} = 2\\pi \\sqrt{0.071428} = 2\\pi \\times 0.26726 = 1.679 \\text{ s}$$",
                "explanation": "The equivalent simple pendulum has length 0.700 m, yielding an oscillation period of 1.68 s."
            },
            {
                "title": "Step 3: Minimum period condition",
                "math": "$$\\frac{dL_{eq}}{dd} = 1 - \\frac{k_g^2}{d^2} = 0 \\implies d_{min} = k_g = \\sqrt{0.120} = 0.3464 \\text{ m} = 34.64 \\text{ cm}$$\n$$L_{eq,min} = 2 k_g = 2 \\times 0.3464 = 0.6928 \\text{ m}$$\n$$T_{min} = 2\\pi \\sqrt{\\frac{2 k_g}{g}} = 2\\pi \\sqrt{\\frac{0.6928}{9.80}} = 2\\pi \\sqrt{0.07069} = 1.671 \\text{ s}$$",
                "explanation": "The shortest possible period is 1.671 s, occurring when suspended at 34.6 cm from the center."
            }
        ]
    },
    {
        "id": "prob-5-2",
        "difficulty": "Intermediate Classical Exam",
        "title": "Damped Oscillator: Logarithmic Decrement and Quality Factor",
        "question": "A mechanical oscillator of mass $m = 250\\text{ g}$ is attached to a spring of force constant $k = 100\\text{ N/m}$. It moves in a viscous medium where the damping force is $-b v$. The amplitude of oscillation drops to $1/e$ of its initial value after 50 complete oscillations.\\n(a) Determine the logarithmic decrement $\\delta$,\\n(b) Calculate the damping attenuation constant $\\gamma$ and the damping coefficient $b$,\\n(c) Compute the Quality Factor $Q$ and the energy dissipated after 50 oscillations.",
        "steps": [
            {
                "title": "Step 1: Compute natural frequency and logarithmic decrement",
                "math": "$$\\omega_0 = \\sqrt{\\frac{k}{m}} = \\sqrt{\\frac{100}{0.250}} = \\sqrt{400} = 20.0 \\text{ rad/s}$$\n$$A(t) = A_0 e^{-\\gamma t} = A_0 e^{-\\gamma N T_d}$$\n$$\\text{Given } \\frac{A_{50}}{A_0} = \\frac{1}{e} \\implies e^{-\\gamma \\cdot 50 T_d} = e^{-1} \\implies 50 \\gamma T_d = 1$$\n$$\\delta = \\gamma T_d = \\frac{1}{50} = 0.0200$$",
                "explanation": "The logarithmic decrement is the fractional decay per cycle, here exactly 0.0200."
            },
            {
                "title": "Step 2: Damping constants gamma and b",
                "math": "$$\\omega_d = \\frac{2\\pi}{T_d} \\approx \\omega_0 = 20.0 \\text{ rad/s} \\implies T_d \\approx \\frac{2\\pi}{20.0} = 0.31416 \\text{ s}$$\n$$\\gamma = \\frac{\\delta}{T_d} = \\frac{0.0200}{0.31416} = 0.06366 \\text{ s}^{-1}$$\n$$b = 2 m \\gamma = 2 \\times 0.250 \\times 0.06366 = 0.03183 \\text{ N}\\cdot\\text{s/m}$$",
                "explanation": "Because damping is very weak ($\gamma \ll \omega_0$), $\omega_d \approx \omega_0$ to four significant digits."
            },
            {
                "title": "Step 3: Quality factor and energy dissipation",
                "math": "$$Q = \\frac{\\pi}{\\delta} = \\frac{\\pi}{0.0200} = 157.1$$\n$$E(t) \\propto A^2(t) \\implies \\frac{E_{50}}{E_0} = \\left( \\frac{A_{50}}{A_0} \\right)^2 = \\left(\\frac{1}{e}\\right)^2 = e^{-2} \\approx 0.1353$$\n$$\\Delta E_{\\text{loss}} = (1 - 0.1353) E_0 = 86.47\\% \\text{ of initial energy dissipated.}$$",
                "explanation": "A high Quality Factor of 157 corresponds to very light damping; 86.5% of total mechanical energy is lost over 50 cycles."
            }
        ]
    },
    {
        "id": "prob-5-3",
        "difficulty": "Rigorous Honors Resonance Problem",
        "title": "Forced Oscillation Resonance Amplitude and Half-Power Bandwidth",
        "question": "An oscillating system consists of mass $m = 0.500\\text{ kg}$, spring constant $k = 450\\text{ N/m}$, and damping constant $b = 1.50\\text{ N}\\cdot\\text{s/m}$. It is driven by a sinusoidal force $F(t) = F_0 \\cos(\\omega t)$ with force amplitude $F_0 = 6.00\\text{ N}$.\\n(a) Determine the natural angular frequency $\\omega_0$, damping factor $\\gamma$, and Quality Factor $Q$,\\n(b) Find the amplitude resonance frequency $\\omega_r$ and the maximum steady-state displacement amplitude $A_{max}$, and\\n(c) Calculate the half-power bandwidth $\\Delta \\omega$ and the average power absorbed at velocity resonance.",
        "steps": [
            {
                "title": "Step 1: Compute natural frequency, damping factor, and Q",
                "math": "$$\\omega_0 = \\sqrt{\\frac{k}{m}} = \\sqrt{\\frac{450}{0.500}} = \\sqrt{900} = 30.0 \\text{ rad/s}$$\n$$\\gamma = \\frac{b}{2m} = \\frac{1.50}{2 \\times 0.500} = 1.50 \\text{ s}^{-1}$$\n$$Q = \\frac{\\omega_0}{2\\gamma} = \\frac{30.0}{2 \\times 1.50} = 10.0$$",
                "explanation": "The oscillator has a natural frequency of 30.0 rad/s and a quality factor $Q = 10$."
            },
            {
                "title": "Step 2: Resonance frequency and peak amplitude",
                "math": "$$\\omega_r = \\sqrt{\\omega_0^2 - 2\\gamma^2} = \\sqrt{900 - 2(1.50)^2} = \\sqrt{900 - 4.50} = \\sqrt{895.5} = 29.925 \\text{ rad/s}$$\n$$A_{max} = \\frac{F_0 / m}{2\\gamma \\sqrt{\\omega_0^2 - \\gamma^2}} = \\frac{6.00 / 0.500}{2(1.50) \\sqrt{900 - 2.25}} = \\frac{12.0}{3.0 \\times \\sqrt{897.75}} = \\frac{4.0}{29.962} = 0.1335 \\text{ m} = 13.35 \\text{ cm}$$\n$$x_{\\text{static}} = \\frac{F_0}{k} = \\frac{6.00}{450} = 0.01333 \\text{ m} = 1.333 \\text{ cm} \\implies A_{max} \\approx Q \\cdot x_{\\text{static}} = 10 \\times 1.333 = 13.33 \\text{ cm}$$",
                "explanation": "The resonance amplitude is amplified by a factor of 10 relative to the static Hookean deflection."
            },
            {
                "title": "Step 3: Bandwidth and resonance power absorption",
                "math": "$$\\Delta \\omega = 2\\gamma = 2 \\times 1.50 = 3.00 \\text{ rad/s}$$\n$$\\text{At velocity resonance } (\\omega = \\omega_0 = 30.0 \\text{ rad/s}):$$\n$$v_{max} = \\frac{F_0}{b} = \\frac{6.00}{1.50} = 4.00 \\text{ m/s}$$\n$$\\langle P_{max} \\rangle = \\frac{1}{2} F_0 v_{max} = \\frac{1}{2} \\times 6.00 \\times 4.00 = 12.0 \\text{ W}$$",
                "explanation": "The half-power resonance bandwidth is 3.0 rad/s and the system absorbs an average power of 12.0 W from the driver at peak resonance."
            }
        ]
    }
]

unit5_data = {
    "number": 5,
    "title": "Oscillations",
    "leadSummary": "A comprehensive mathematical and physical treatment of harmonic motion, phase space representation, energy conservation, compound and torsion pendulums, orthogonal superposition and Lissajous figures, damped decay regimes, logarithmic decrement, Q-factor, and forced mechanical resonance.",
    "sections": u5_sections,
    "problems": u5_problems
}

with open("matter_u5.json", "w") as f:
    json.dump(unit5_data, f, indent=2)

print("Unit 5 built successfully with", len(u5_sections), "sections and", len(u5_problems), "solved problems!")

# =========================================================================
# UNIT 6: Traveling Waves
# =========================================================================
u6_sections = [
    {
        "id": "sec-6-1",
        "number": "§6.1",
        "heading": "The 1D Wave Equation and Traveling Wave Kinematics",
        "simulation": "traveling-wave-sim",
        "content": """A wave is an organized disturbance that propagates through space or a material medium, transporting energy and momentum without transporting macroscopic matter.

<h4>1. General Form of a 1D Traveling Wave</h4>
Consider a 1D disturbance $\\psi(x, t)$ maintaining its shape as it translates along the x-axis with speed $v$:
$$\\psi(x, t) = f(x \\mp vt)$$
where the minus sign denotes propagation in the $+x$ direction (forward wave) and the plus sign denotes propagation in the $-x$ direction (backward wave).

<h4>2. The Classical 1D Wave Equation</h4>
Using the chain rule with variables $\\xi = x - vt$ and $\\eta = x + vt$:
$$\\frac{\\partial \\psi}{\\partial x} = f'(\\xi), \\quad \\frac{\\partial^2 \\psi}{\\partial x^2} = f''(\\xi)$$
$$\\frac{\\partial \\psi}{\\partial t} = -v f'(\\xi), \\quad \\frac{\\partial^2 \\psi}{\\partial t^2} = v^2 f''(\\xi)$$
Equating second derivatives:
$$\\frac{\\partial^2 \\psi}{\\partial x^2} = \\frac{1}{v^2} \\frac{\\partial^2 \\psi}{\\partial t^2}$$
This is the celebrated linear, second-order hyperbolic <strong>Classical Wave Equation</strong>.
Its general solution, established by Jean le Rond d'Alembert (1747), is:
$$\\psi(x, t) = f(x - vt) + g(x + vt)$$
where $f$ and $g$ are arbitrary twice-differentiable functions determined by initial Cauchy boundary data $\\psi(x, 0)$ and $\\dot{\\psi}(x, 0)$.

<h4>3. Harmonic Plane Waves</h4>
For sinusoidal disturbances:
$$\\psi(x, t) = A \\cos(k x - \\omega t + \\phi) = A \\cos\\left[ \\frac{2\\pi}{\\lambda} (x - v t) + \\phi \\right]$$
where:
<ul>
  <li>$A$: Wave amplitude.</li>
  <li>$k = \\frac{2\\pi}{\\lambda}$: <strong>Wavenumber</strong> (spatial angular frequency in rad/m).</li>
  <li>$\\omega = 2\\pi f$: Temporal angular frequency in rad/s.</li>
  <li>$v = \\frac{\\omega}{k} = f \\lambda$: Phase speed.</li>
  <li>Complex notation: $\\psi(x, t) = \\text{Re}\\{ A e^{i(kx - \\omega t)} \\}$.</li>
</ul>"""
    },
    {
        "id": "sec-6-2",
        "number": "§6.2",
        "heading": "Speed of Transverse Waves in a Stretched String",
        "simulation": "traveling-wave-sim",
        "content": """Consider a flexible, perfectly elastic string of uniform linear mass density $\\mu$ (kg/m) stretched under constant equilibrium tension $T$ (N).

<h4>1. Derivation from Newton's Second Law</h4>
Let the string undergo small transverse vibrations in the xy-plane. Consider an infinitesimal segment located between $x$ and $x + dx$ with mass $dm = \\mu \\, dx$.
The slope of the string at $x$ is $\\frac{\\partial y}{\\partial x} = \\tan\\theta_1 \\approx \\sin\\theta_1$.
The net transverse force $dF_y$ acting on the segment is:
$$dF_y = T \\sin\\theta_2 - T \\sin\\theta_1 \\approx T \\left[ \\left( \\frac{\\partial y}{\\partial x} \\right)_{x+dx} - \\left( \\frac{\\partial y}{\\partial x} \\right)_x \\right] = T \\frac{\\partial^2 y}{\\partial x^2} dx$$
By Newton's second law ($dF_y = dm \\, a_y = \\mu \\, dx \\frac{\\partial^2 y}{\\partial t^2}$):
$$T \\frac{\\partial^2 y}{\\partial x^2} dx = \\mu \\, dx \\frac{\\partial^2 y}{\\partial t^2}$$
$$\\frac{\\partial^2 y}{\\partial x^2} = \\frac{\\mu}{T} \\frac{\\partial^2 y}{\\partial t^2}$$
Comparing with the general wave equation $\\frac{\\partial^2 y}{\\partial x^2} = \\frac{1}{v^2} \\frac{\\partial^2 y}{\\partial t^2}$ immediately yields:
$$v = \\sqrt{\\frac{T}{\\mu}}$$
<em>Physical Meaning:</em> Wave propagation speed is governed strictly by the ratio of the medium's elastic restoring property ($T$) to its inertial property ($\mu$). Amplitude and wavelength have zero effect in non-dispersive strings."""
    },
    {
        "id": "sec-6-3",
        "number": "§6.3",
        "heading": "Longitudinal Waves in a Solid Bar and Fluids",
        "simulation": "traveling-wave-sim",
        "content": """Longitudinal waves transmit disturbances via compressive and rarefactive displacements along the axis of propagation.

<h4>1. Longitudinal Waves in an Elastic Solid Bar</h4>
Consider a thin cylindrical solid rod of cross-sectional area $A$, material density $\\rho$, and Young's modulus $Y$.
Let $u(x, t)$ denote the longitudinal displacement of a cross-section originally at $x$.
An infinitesimal segment of initial length $dx$ experiences longitudinal strain:
$$\\epsilon = \\frac{\\partial u}{\\partial x}$$
The normal compressive/tensile stress is:
$$\\sigma = Y \\epsilon = Y \\frac{\\partial u}{\\partial x}$$
The net force acting on the element of mass $dm = \\rho A \\, dx$ is:
$$dF = [\\sigma(x+dx) - \\sigma(x)] A = A \\frac{\\partial \\sigma}{\\partial x} dx = A Y \\frac{\\partial^2 u}{\\partial x^2} dx$$
Applying Newton's second law ($dF = dm \\frac{\\partial^2 u}{\\partial t^2}$):
$$A Y \\frac{\\partial^2 u}{\\partial x^2} dx = \\rho A \\, dx \\frac{\\partial^2 u}{\\partial t^2} \\implies \\frac{\\partial^2 u}{\\partial x^2} = \\frac{\\rho}{Y} \\frac{\\partial^2 u}{\\partial t^2}$$
The speed of longitudinal acoustic waves in a thin solid bar is:
$$v = \\sqrt{\\frac{Y}{\\rho}}$$
(For steel: $Y \\approx 2 \\times 10^{11} \\text{ Pa}, \\rho \\approx 7850 \\text{ kg/m}^3 \\implies v \\approx 5050 \\text{ m/s}$).

<h4>2. Acoustic Plane Waves in Fluid Media</h4>
In fluids, shear modulus vanishes, so restoring forces are provided exclusively by the <strong>Bulk Modulus ($B$)</strong>:
$$B = -V \\frac{dP}{dV} = \\rho \\frac{dP}{d\\rho}$$
Following identical dynamic balance for an acoustic plane wave:
$$v = \\sqrt{\\frac{B}{\\rho}}$$
<ul>
  <li><strong>Newton's Isothermal Formula (1687):</strong> Newton assumed sound compressions occurred isothermally ($P V = \\text{const} \\implies B_{iso} = P$).
  $$v_{\\text{Newton}} = \\sqrt{\\frac{P}{\\rho}} \\approx 280 \\text{ m/s in air at STP (16% error!)}$$</li>
  <li><strong>Laplace's Adiabatic Correction (1816):</strong> Pierre-Simon Laplace recognized that acoustic compressions and rarefactions happen so rapidly that heat conduction between adjacent regions is negligible. Acoustic cycles are strictly <strong>adiabatic</strong> ($P V^\\gamma = \\text{const}$):
  $$B_{ad} = \\gamma P$$
  $$v = \\sqrt{\\frac{\\gamma P}{\\rho}} = \\sqrt{\\frac{\\gamma R T}{M}}$$
  where $\\gamma = C_p / C_v \\approx 1.40$ for diatomic air ($M = 0.02897 \\text{ kg/mol}$).
  At 20°C (293.15 K): $v = \\sqrt{1.40 \\times 8.314 \\times 293.15 / 0.02897} = 343.2 \\text{ m/s}$, matching experimental data perfectly!</li>
</ul>"""
    },
    {
        "id": "sec-6-4",
        "number": "§6.4",
        "heading": "Transmission of Energy and Power by Traveling Waves",
        "simulation": "traveling-wave-sim",
        "content": """Traveling waves transport mechanical energy down the medium as particles oscillate in succession.

<h4>1. Energy Density of a Harmonic Transverse Wave</h4>
Consider a harmonic wave on a string: $y(x, t) = A \\cos(kx - \\omega t)$.
For an element of mass $dm = \\mu \\, dx$:
<ul>
  <li><strong>Kinetic Energy ($dK$):</strong>
  $$dK = \\frac{1}{2} dm \\left( \\frac{\\partial y}{\\partial t} \\right)^2 = \\frac{1}{2} \\mu \\, dx \\left[ \\omega A \\sin(kx - \\omega t) \\right]^2 = \\frac{1}{2}\\mu \\omega^2 A^2 \\sin^2(kx - \\omega t) dx$$</li>
  <li><strong>Potential Energy ($dU$):</strong> Work done in stretching the string element from $dx$ to $ds = \\sqrt{dx^2 + dy^2} \\approx dx [1 + \\frac{1}{2}(\\frac{\\partial y}{\\partial x})^2]$:
  $$dU = T (ds - dx) = \\frac{1}{2} T \\left( \\frac{\\partial y}{\\partial x} \\right)^2 dx = \\frac{1}{2} T \\left[ -k A \\sin(kx - \\omega t) \\right]^2 dx = \\frac{1}{2} T k^2 A^2 \\sin^2(kx - \\omega t) dx$$
  Since $v = \\omega / k = \\sqrt{T / \\mu} \\implies T k^2 = \\mu \\omega^2$:
  $$dU = \\frac{1}{2} \\mu \\omega^2 A^2 \\sin^2(kx - \\omega t) dx = dK$$</li>
</ul>
<em>Fundamental Property:</em> In a pure traveling wave, kinetic energy and potential energy are in phase and locally identical at all points!
Total energy per unit length (linear energy density):
$$u_L = \\frac{dE}{dx} = \\mu \\omega^2 A^2 \\sin^2(kx - \\omega t)$$
Average energy density over one wavelength:
$$\\langle u_L \\rangle = \\frac{1}{2} \\mu \\omega^2 A^2 \\quad (\\text{J/m})$$

<h4>2. Wave Power and Intensity</h4>
The rate at which energy is transmitted through any cross-section is the instantaneous power:
$$P(t) = -T \\left( \\frac{\\partial y}{\\partial x} \\right) \\left( \\frac{\\partial y}{\\partial t} \\right) = T k \\omega A^2 \\sin^2(kx - \\omega t)$$
Since $T k = \\mu v^2 (\\omega / v) = \\mu v \\omega$:
$$P(t) = \\mu v \\omega^2 A^2 \\sin^2(kx - \\omega t)$$
The time-averaged transmitted power is:
$$\\langle P \\rangle = \\frac{1}{2} \\mu v \\omega^2 A^2 = \\langle u_L \\rangle v \\quad (\\text{Watts})$$
For a 3D medium with volume density $\\rho$, the wave <strong>intensity</strong> $I$ (power per unit area) is:
$$I = \\frac{\\langle P \\rangle}{\\text{Area}} = \\frac{1}{2} \\rho v \\omega^2 A^2 = 2 \\pi^2 \\rho v f^2 A^2 \\quad (\\text{W/m}^2)$$
Intensity is strictly proportional to the square of frequency and the square of amplitude ($I \\propto f^2 A^2$)."""
    },
    {
        "id": "sec-6-5",
        "number": "§6.5",
        "heading": "Superposition Principle, Canal Gravity Waves, and Ripples",
        "simulation": "traveling-wave-sim",
        "content": """The linear nature of the classical wave equation implies that multiple wave disturbances superpose linearly.

<h4>1. The Principle of Superposition</h4>
If $\\psi_1(x, t)$ and $\\psi_2(x, t)$ are individual solutions to the linear wave equation, any linear combination:
$$\\psi(x, t) = c_1 \\psi_1(x, t) + c_2 \\psi_2(x, t)$$
is also an exact solution. When two waves pass through the same region, the net displacement is simply the algebraic sum of their separate displacements.

<h4>2. Shallow Water Waves in an Open Canal</h4>
Consider surface waves propagating along a shallow canal of uniform depth $h$ where wavelength $\\lambda \\gg h$.
The horizontal velocity of water parcels is nearly uniform from bed to surface.
The wave speed is governed purely by gravitational restoring forces:
$$v = \\sqrt{g h}$$
Remarkably, this shallow water wave speed is completely non-dispersive (independent of wavelength $\\lambda$).
(This explains the immense speed of ocean tsunamis: across an ocean basin of depth $h = 4000 \\text{ m}$, speed reaches $v = \\sqrt{9.8 \\times 4000} \\approx 200 \\text{ m/s} \\approx 720 \\text{ km/h}$).

<h4>3. Capillary Waves and Ripples</h4>
On water surfaces, restoring forces are provided by both gravity ($g$) and surface tension ($\\gamma$).
Hydrodynamic analysis of Airy wave theory yields the general dispersion relation for surface waves on water of depth $h$:
$$\\omega^2 = \\left( g k + \\frac{\\gamma}{\\rho} k^3 \\right) \\tanh(k h)$$
For deep water ($k h \\gg 1 \\implies \\tanh(kh) \\to 1$):
$$v_p^2 = \\frac{\\omega^2}{k^2} = \\frac{g}{k} + \\frac{\\gamma}{\\rho} k = \\frac{g \\lambda}{2\\pi} + \\frac{2\\pi \\gamma}{\\rho \\lambda}$$
Two asymptotic regimes exist:
<ul>
  <li><strong>Gravity Waves ($\lambda \gg 1.7\text{ cm}$):</strong> Gravity dominates. Phase speed increases with wavelength:
  $$v_p \\approx \\sqrt{\\frac{g \\lambda}{2\\pi}}$$</li>
  <li><strong>Ripples / Capillary Waves ($\lambda \ll 1.7\text{ cm}$):</strong> Surface tension dominates. Phase speed increases as wavelength gets smaller:
  $$v_p \\approx \\sqrt{\\frac{2\\pi \\gamma}{\\rho \\lambda}}$$</li>
</ul>
<strong>Minimum Phase Speed:</strong> Minimizing $v_p(\\lambda)$:
$$\\frac{d(v_p^2)}{d\\lambda} = \\frac{g}{2\\pi} - \\frac{2\\pi \\gamma}{\\rho \\lambda^2} = 0 \\implies \\lambda_c = 2\\pi \\sqrt{\\frac{\\gamma}{\\rho g}}$$
For pure water at 20°C ($\\gamma = 0.0728 \\text{ N/m}, \\rho = 1000 \\text{ kg/m}^3$):
$$\\lambda_c = 2\\pi \\sqrt{\\frac{0.0728}{1000 \\times 9.80}} \\approx 1.71 \\text{ cm}$$
$$v_{p,min} = \\left( \\frac{4 g \\gamma}{\\rho} \\right)^{1/4} = \\left( \\frac{4 \\times 9.80 \\times 0.0728}{1000} \\right)^{1/4} \\approx 0.231 \\text{ m/s} = 23.1 \\text{ cm/s}$$
No surface disturbance can propagate across quiet water slower than 23.1 cm/s!"""
    },
    {
        "id": "sec-6-6",
        "number": "§6.6",
        "heading": "Phase Velocity, Group Velocity, and Fourier Decomposition",
        "simulation": "traveling-wave-sim",
        "content": """When the wave velocity depends on frequency or wavelength ($\frac{dv}{d\lambda} \ne 0$), the medium is said to be <strong>dispersive</strong>.

<h4>1. Phase Velocity ($v_p$) vs. Group Velocity ($v_g$)</h4>
Consider the superposition of two harmonic waves with slightly different frequencies and wavenumbers:
$$\\psi(x, t) = A \\cos(k_1 x - \\omega_1 t) + A \\cos(k_2 x - \\omega_2 t)$$
Let $k = \\frac{k_1 + k_2}{2}, \\Delta k = k_1 - k_2$ and $\\omega = \\frac{\\omega_1 + \\omega_2}{2}, \\Delta \\omega = \\omega_1 - \\omega_2$.
Using the trigonometric identity $\\cos\\alpha + \\cos\\beta = 2\\cos\\frac{\\alpha-\\beta}{2}\\cos\\frac{\\alpha+\\beta}{2}$:
$$\\psi(x, t) = 2 A \\cos\\left( \\frac{\\Delta k}{2} x - \\frac{\\Delta \\omega}{2} t \\right) \\cos(k x - \\omega t)$$
This represents a high-frequency carrier wave modulated by a slowly varying envelope:
<ul>
  <li><strong>Phase Velocity ($v_p$):</strong> The speed at which individual crests and troughs of the carrier advance:
  $$v_p = \\frac{\\omega}{k}$$</li>
  <li><strong>Group Velocity ($v_g$):</strong> The speed at which the modulation envelope (and physical wave energy/information) propagates:
  $$v_g = \\lim_{\\Delta k \\to 0} \\frac{\\Delta \\omega}{\\Delta k} = \\frac{d\\omega}{dk}$$</li>
</ul>

<h4>2. Rayleigh's Dispersion Relation</h4>
Since $\\omega = k v_p$:
$$v_g = \\frac{d(k v_p)}{dk} = v_p + k \\frac{dv_p}{dk}$$
Rewriting in terms of wavelength $\\lambda = 2\\pi / k$ (where $dk = -\\frac{2\\pi}{\\lambda^2} d\\lambda$):
$$v_g = v_p - \\lambda \\frac{dv_p}{d\\lambda}$$
<ul>
  <li><strong>Non-dispersive medium ($\frac{dv_p}{d\lambda} = 0$):</strong> $v_g = v_p$ (e.g., sound in air, light in vacuum).</li>
  <li><strong>Normal dispersion ($\frac{dv_p}{d\lambda} > 0$):</strong> $v_g < v_p$ (e.g., deep-water gravity waves where $v_g = \\frac{1}{2} v_p$).</li>
  <li><strong>Anomalous dispersion ($\frac{dv_p}{d\lambda} < 0$):</strong> $v_g > v_p$ (e.g., surface ripples where $v_g = \\frac{3}{2} v_p$).</li>
</ul>

<h4>3. Fourier Series and Harmonic Wave Packets</h4>
Joseph Fourier (1822) proved that any arbitrary periodic function $f(x)$ with period $\\lambda$ can be synthesized as an infinite sum of discrete sinusoidal harmonics:
$$f(x) = \\frac{a_0}{2} + \\sum_{n=1}^\\infty \\left[ a_n \\cos(n k x) + b_n \\sin(n k x) \\right]$$
where the Fourier coefficients are obtained via orthogonality integrals:
$$a_n = \\frac{2}{\\lambda} \\int_0^\\lambda f(x) \\cos(n k x) dx, \\quad b_n = \\frac{2}{\\lambda} \\int_0^\\lambda f(x) \\sin(n k x) dx$$
In a non-dispersive medium, all harmonics travel at the same speed $v$, maintaining the wave pulse shape.
In a dispersive medium, each harmonic travels at its own phase speed $v_p(\\omega_n)$, causing localized pulses to disperse and broaden over time."""
    }
]

u6_problems = [
    {
        "id": "prob-6-1",
        "difficulty": "Undergraduate Classical Exam Standard",
        "title": "Transverse Wave on a Stretched Wire: Speed, Tension, and Power",
        "question": "A steel piano wire of diameter $D = 1.20\\text{ mm}$ and material density $\\rho = 7800\\text{ kg/m}^3$ is stretched under tension $T = 600\\text{ N}$. A sinusoidal wave of frequency $f = 250\\text{ Hz}$ and peak-to-peak displacement $2A = 4.00\\text{ mm}$ propagates down the wire.\\n(a) Calculate the linear mass density $\\mu$ and the wave propagation speed $v$,\\n(b) Find the wavelength $\\lambda$ and angular wavenumber $k$, and\\n(c) Determine the linear energy density $\\langle u_L \\rangle$ and the average power $\\langle P \\rangle$ transmitted by the wave.",
        "steps": [
            {
                "title": "Step 1: Compute linear density and wave speed",
                "math": "$$A_{\\text{wire}} = \\frac{\\pi D^2}{4} = \\frac{\\pi (1.20 \\times 10^{-3})^2}{4} = 1.131 \\times 10^{-6} \\text{ m}^2$$\n$$\\mu = \\rho A_{\\text{wire}} = 7800 \\times 1.131 \\times 10^{-6} = 8.822 \\times 10^{-3} \\text{ kg/m}$$\n$$v = \\sqrt{\\frac{T}{\\mu}} = \\sqrt{\\frac{600}{8.822 \\times 10^{-3}}} = \\sqrt{68012} = 260.8 \\text{ m/s}$$",
                "explanation": "Wave speed is governed strictly by the square root of tension over linear mass density."
            },
            {
                "title": "Step 2: Calculate wavelength, angular frequency, and wavenumber",
                "math": "$$\\lambda = \\frac{v}{f} = \\frac{260.8}{250} = 1.043 \\text{ m}$$\n$$k = \\frac{2\\pi}{\\lambda} = \\frac{2\\pi}{1.043} = 6.024 \\text{ rad/m}$$\n$$\\omega = 2\\pi f = 2\\pi \\times 250 = 1570.8 \\text{ rad/s}$$\n$$\\text{Amplitude } A = \\frac{4.00 \\text{ mm}}{2} = 2.00 \\times 10^{-3} \\text{ m}$$",
                "explanation": "Peak displacement amplitude is half the peak-to-peak excursion."
            },
            {
                "title": "Step 3: Average energy density and transmitted power",
                "math": "$$\\langle u_L \\rangle = \\frac{1}{2} \\mu \\omega^2 A^2 = \\frac{1}{2} \\times (8.822 \\times 10^{-3}) \\times (1570.8)^2 \\times (2.00 \\times 10^{-3})^2$$\n$$\\langle u_L \\rangle = 0.5 \\times 0.008822 \\times 2.4674 \\times 10^6 \\times 4.00 \\times 10^{-6} = 4.353 \\times 10^{-2} \\text{ J/m}$$\n$$\\langle P \\rangle = \\langle u_L \\rangle v = (4.353 \\times 10^{-2}) \\times 260.8 = 11.35 \\text{ Watts}$$",
                "explanation": "The piano wire transports a continuous average mechanical power of 11.35 Watts along its length."
            }
        ]
    },
    {
        "id": "prob-6-2",
        "difficulty": "Honors Fluid Wave Mechanics",
        "title": "Capillary-Gravity Waves: Phase Speed and Transition Threshold",
        "question": "For deep-water surface waves, the dispersion relation is given by $v_p^2 = \\frac{g \\lambda}{2\\pi} + \\frac{2\\pi \\gamma}{\\rho \\lambda}$. For clean water at $20^\\circ\\text{C}$ with surface tension $\\gamma = 0.0730\\text{ N/m}$, density $\\rho = 1000\\text{ kg/m}^3$, and $g = 9.80\\text{ m/s}^2$:\\n(a) Derive the wavelength $\\lambda_c$ and frequency $f_c$ at which the phase speed is minimum,\\n(b) Compute the numerical value of minimum phase velocity $v_{p,min}$, and\\n(c) For a swell of wavelength $\\lambda = 20.0\\text{ m}$ and a ripple of wavelength $\\lambda = 5.0\\text{ mm}$, find whether each belongs to the gravity or capillary regime and compute their respective phase speeds.",
        "steps": [
            {
                "title": "Step 1: Determine critical threshold wavelength and minimum speed",
                "math": "$$\\frac{d(v_p^2)}{d\\lambda} = \\frac{g}{2\\pi} - \\frac{2\\pi \\gamma}{\\rho \\lambda^2} = 0 \\implies \\lambda_c = 2\\pi \\sqrt{\\frac{\\gamma}{\\rho g}}$$\n$$\\lambda_c = 2\\pi \\sqrt{\\frac{0.0730}{1000 \\times 9.80}} = 2\\pi \\sqrt{7.449 \\times 10^{-6}} = 2\\pi \\times 2.729 \\times 10^{-3} = 1.715 \\times 10^{-2} \\text{ m} = 1.715 \\text{ cm}$$\n$$v_{p,min} = \\left( \\frac{4 g \\gamma}{\\rho} \\right)^{1/4} = \\left( \\frac{4 \\times 9.80 \\times 0.0730}{1000} \\right)^{1/4} = (2.8616 \\times 10^{-3})^{0.25} = 0.2311 \\text{ m/s} = 23.11 \\text{ cm/s}$$",
                "explanation": "At $\lambda = 1.71$ cm, gravity and capillary forces contribute identically to the wave speed."
            },
            {
                "title": "Step 2: Minimum frequency",
                "math": "$$f_c = \\frac{v_{p,min}}{\\lambda_c} = \\frac{0.2311 \\text{ m/s}}{0.01715 \\text{ m}} = 13.48 \\text{ Hz}$$",
                "explanation": "Disturbances at 13.5 Hz propagate at the absolute lowest phase speed possible in water."
            },
            {
                "title": "Step 3: Regime identification and speeds",
                "math": "$$\\text{For } \\lambda = 20.0 \\text{ m} \\gg \\lambda_c \\implies \\text{Pure Gravity Swell:}$$\n$$v_p = \\sqrt{\\frac{g \\lambda}{2\\pi}} = \\sqrt{\\frac{9.80 \\times 20.0}{2\\pi}} = \\sqrt{31.19} = 5.58 \\text{ m/s}$$\n$$\\text{For } \\lambda = 5.00 \\text{ mm} = 0.0050 \\text{ m} \\ll \\lambda_c \\implies \\text{Pure Capillary Ripple:}$$\n$$v_p = \\sqrt{\\frac{2\\pi \\gamma}{\\rho \\lambda}} = \\sqrt{\\frac{2\\pi \\times 0.0730}{1000 \\times 0.0050}} = \\sqrt{\\frac{0.4587}{5.0}} = \\sqrt{0.09174} = 0.303 \\text{ m/s} = 30.3 \\text{ cm/s}$$",
                "explanation": "Ocean swells travel rapidly under gravity (5.58 m/s), whereas fine wind ripples travel under surface tension (30.3 cm/s)."
            }
        ]
    },
    {
        "id": "prob-6-3",
        "difficulty": "Advanced Honors Wave Mechanics",
        "title": "Group Velocity and Rayleigh Dispersion in a Waveguide",
        "question": "In an acoustic rectangular duct, the dispersion relation for higher-order acoustic modes is given by $\\omega(k) = \\sqrt{\\omega_{co}^2 + c^2 k^2}$, where $\\omega_{co} = 2\\pi \\times 1000\\text{ rad/s}$ is the duct cutoff frequency and $c = 340\\text{ m/s}$ is the free-space speed of sound.\\n(a) Derive analytical expressions for the phase velocity $v_p(k)$ and group velocity $v_g(k)$ as functions of frequency $\\omega$,\\n(b) Prove that $v_p \\cdot v_g = c^2$, and\\n(c) For a signal operating at $\\omega = 2\\pi \\times 1250\\text{ rad/s}$, calculate $v_p$, $v_g$, and the time required for a wave packet to travel a distance $L = 50.0\\text{ m}$ through the duct.",
        "steps": [
            {
                "title": "Step 1: Derive phase velocity and group velocity",
                "math": "$$v_p = \\frac{\\omega}{k} = \\frac{\\omega}{\\sqrt{\\frac{\\omega^2 - \\omega_{co}^2}{c^2}}} = \\frac{c}{\\sqrt{1 - (\\omega_{co} / \\omega)^2}}$$\n$$v_g = \\frac{d\\omega}{dk} = \\frac{d}{dk}\\left( \\sqrt{\\omega_{co}^2 + c^2 k^2} \\right) = \\frac{c^2 k}{\\sqrt{\\omega_{co}^2 + c^2 k^2}} = \\frac{c^2 (\\frac{\\omega}{v_p})}{\\omega} = \\frac{c^2}{v_p}$$\n$$v_g = c \\sqrt{1 - \\left(\\frac{\\omega_{co}}{\\omega}\\right)^2}$$",
                "explanation": "Group velocity represents envelope energy velocity and is always less than free-space sound speed $c$."
            },
            {
                "title": "Step 2: Prove the reciprocal velocity product",
                "math": "$$v_p \\cdot v_g = \\left[ \\frac{c}{\\sqrt{1 - (\\omega_{co}/\\omega)^2}} \\right] \\times \\left[ c \\sqrt{1 - (\\omega_{co}/\\omega)^2} \\right] = c^2$$\n$$\\text{Q.E.D.}$$",
                "explanation": "This identity mirrors the relativistic de Broglie relation for massive quantum particles and electromagnetic waveguides."
            },
            {
                "title": "Step 3: Numerical calculation at 1250 Hz",
                "math": "$$\\frac{\\omega_{co}}{\\omega} = \\frac{1000}{1250} = 0.800$$\n$$\\sqrt{1 - (0.800)^2} = \\sqrt{1 - 0.640} = \\sqrt{0.360} = 0.600$$\n$$v_p = \\frac{340}{0.600} = 566.7 \\text{ m/s}$$\n$$v_g = 340 \\times 0.600 = 204.0 \\text{ m/s}$$\n$$t_{\\text{packet}} = \\frac{L}{v_g} = \\frac{50.0 \\text{ m}}{204.0 \\text{ m/s}} = 0.2451 \\text{ s} = 245.1 \\text{ ms}$$",
                "explanation": "While phase crests advance superluminally/supersonically at 566.7 m/s, physical pulse energy propagates strictly at group speed 204.0 m/s, requiring 245 ms to traverse 50 m."
            }
        ]
    }
]

unit6_data = {
    "number": 6,
    "title": "Traveling Waves",
    "leadSummary": "A rigorous study of 1D wave dynamics, d'Alembert's general solution, transverse string waves, longitudinal waves in solids and fluids, Laplace's adiabatic correction, energy flux and intensity, canal gravity waves, capillary ripples, Fourier decomposition, and group versus phase velocity.",
    "sections": u6_sections,
    "problems": u6_problems
}

with open("matter_u6.json", "w") as f:
    json.dump(unit6_data, f, indent=2)

print("Unit 6 built successfully with", len(u6_sections), "sections and", len(u6_problems), "solved problems!")
