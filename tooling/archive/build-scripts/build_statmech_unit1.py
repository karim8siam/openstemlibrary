# Build Script for Unit 1 and Unit 2: Statistical Mechanics
import json

u1_sections = [
    {
        "id": "sec-1-1",
        "number": "§1.1",
        "heading": "The Scope of Statistical Physics and Assemblies",
        "simulation": "microstates-macrostates-sim",
        "content": """Statistical mechanics bridges the microscopic dynamics of individual atoms and molecules with the macroscopic laws of classical thermodynamics. A macroscopic system typically contains on the order of Avogadro's number $N \\sim 10^{23}$ particles. Directly solving $10^{23}$ coupled classical equations of motion or solving the Schrödinger equation in a $10^{23}$-dimensional Hilbert space is computationally and analytically impossible.

<h4>1. Microscopic vs. Macroscopic Descriptions</h4>
In classical mechanics, the exact state of a system of $N$ particles is determined by specifying all generalized coordinates $q_i$ and conjugate momenta $p_i$ ($i = 1, 2, \\dots, 3N$). In quantum mechanics, it is specified by an exact many-body state vector $|\\Psi(t)\\rangle$. This microscopic specification contains vastly more information than can ever be observed experimentally.

Conversely, a **macroscopic description** characterizes the system using a few gross thermodynamic parameters: total internal energy $E$, volume $V$, pressure $P$, temperature $T$, and chemical potential $\\mu$. Statistical mechanics demonstrates that macroscopic observables are exact statistical averages over accessible microscopic states:
$$\\langle A \\rangle = \\sum_{i} P_i A_i$$

<h4>2. Definition of an Assembly and System Classifications</h4>
An **assembly** is a collection of a very large number $N$ of particles (atoms, molecules, ions, photons) confined within a macroscopic volume $V$. Assemblies are classified according to their boundary interactions with their surroundings:
<ul>
  <li><strong>Isolated Assembly:</strong> Exchanges neither energy nor matter with its surroundings. Constant internal energy $E$, volume $V$, and particle number $N$ ($dE = 0, dV = 0, dN = 0$).</li>
  <li><strong>Closed Assembly:</strong> Exchanges energy (heat and mechanical work) with a surrounding thermal reservoir, but cannot exchange matter ($T, V, N$ fixed; $dN = 0$).</li>
  <li><strong>Open Assembly:</strong> Exchanges both energy and matter with its surroundings ($T, V, \\mu$ fixed).</li>
</ul>

<h4>3. The Role of Probability in Thermal Physics</h4>
Because macroscopic systems are in ceaseless microscopic motion, any macroscopic observable $M$ exhibits microscopic fluctuations $\\Delta M$. For an assembly of $N$ particles, the central limit theorem dictates that relative fluctuations vanish as:
$$\\frac{\\Delta M}{\\langle M \\rangle} \\sim \\frac{1}{\\sqrt{N}} \\sim \\frac{1}{\\sqrt{10^{23}}} = 10^{-11.5}$$
Thus, statistical averages predict macroscopic phenomena with virtually deterministic experimental precision."""
    },
    {
        "id": "sec-1-2",
        "number": "§1.2",
        "heading": "Phase Space and Phase Trajectories",
        "simulation": "liouville-phase-space-sim",
        "content": """To describe the instantaneous mechanical state and dynamical evolution of a classical system, statistical mechanics employs the geometrical concept of **Phase Space**.

<h4>1. Definition of Phase Space</h4>
For a system possessing $f$ degrees of freedom, its configuration is specified by $f$ generalized coordinates $q_1, q_2, \\dots, q_f$, and its dynamical state requires $f$ generalized conjugate momenta $p_1, p_2, \\dots, p_f$, where:
$$p_i = \\frac{\\partial L}{\\partial \\dot{q}_i}$$
Phase space is an orthogonal, $2f$-dimensional Euclidean space whose Cartesian coordinate axes are $(q_1, \\dots, q_f, p_1, \\dots, p_f)$.

<h4>2. $\\mu$-Space versus $\\Gamma$-Space</h4>
Following Paul and Tatyana Ehrenfest, we distinguish two fundamental phase space formalisms:
<ul>
  <li><strong>$\\mu$-Space (Molecule Space):</strong> A 6-dimensional phase space $(x, y, z, p_x, p_y, p_z)$ for a single particle. An assembly of $N$ non-interacting particles is represented by a swarm of $N$ distinct points moving simultaneously in this 6D space.</li>
  <li><strong>$\\Gamma$-Space (Gas Phase Space):</strong> A $6N$-dimensional phase space for the entire assembly of $N$ particles. The instantaneous microstate of the entire macroscopic assembly corresponds to a <em>single representative point</em>:
  $$\\mathbf{X} = (q_1, q_2, \\dots, q_{3N}, p_1, p_2, \\dots, p_{3N}) \\in \\mathbb{R}^{6N}$$
  As time progresses, this single point traces out a continuous curve termed the <strong>phase trajectory</strong>.</li>
</ul>

<h4>3. Phase Trajectory of a 1D Harmonic Oscillator</h4>
Consider a 1D harmonic oscillator with mass $m$ and spring constant $k = m\\omega^2$. The Hamiltonian is:
$$H(q, p) = \\frac{p^2}{2m} + \\frac{1}{2}m\\omega^2 q^2 = E$$
Rearranging in canonical ellipse form:
$$\\frac{q^2}{\\left(\\sqrt{\\frac{2E}{m\\omega^2}}\\right)^2} + \\frac{p^2}{\\left(\\sqrt{2mE}\\right)^2} = 1$$
The phase trajectory is an ellipse centered at the origin with semi-axes:
$$a = \\sqrt{\\frac{2E}{m\\omega^2}}, \\quad b = \\sqrt{2mE}$$
The total area enclosed by this orbit in 2D phase space is:
$$\\oint p \\, dq = \\pi a b = \\pi \\sqrt{\\frac{2E}{m\\omega^2}} \\sqrt{2mE} = \\frac{2\\pi E}{\\omega} = \\frac{E}{\\nu}$$
This demonstrates that the phase trajectory for a conservative periodic system forms a closed loop whose enclosed phase volume is an adiabatic invariant."""
    },
    {
        "id": "sec-1-3",
        "number": "§1.3",
        "heading": "Volume in Phase Space and Specification of States",
        "simulation": "liouville-phase-space-sim",
        "content": """In classical continuum mechanics, phase space is infinite and continuous. However, to count discrete microstates and transition to quantum mechanics, phase space must be partitioned into elementary phase cells.

<h4>1. Differential Volume Element in Phase Space</h4>
The infinitesimal volume element $d\\Gamma$ of $6N$-dimensional phase space is defined by:
$$d\\Gamma = dq_1 \\, dq_2 \\dots dq_{3N} \\, dp_1 \\, dp_2 \\dots dp_{3N} = \\prod_{i=1}^{3N} dq_i \\, dp_i = d^{3N}q \\, d^{3N}p$$
The dimensions of a coordinate times its conjugate momentum $[q_i p_i]$ are:
$$[\\text{length}] \\times [\\text{mass} \\cdot \\text{velocity}] = [\\text{energy} \\times \\text{time}] = [\\text{Action}] = \\text{Joule} \\cdot \\text{second}$$
Therefore, each product $dq_i dp_i$ has physical dimensions of action ($\\,\\text{J}\\cdot\\text{s}$).

<h4>2. Elementary Quantum Phase Cell Volume ($h_0$)</h4>
According to the Heisenberg uncertainty principle:
$$\\Delta q_i \\Delta p_i \\ge \\frac{\\hbar}{2} \\sim h$$
Two physical microstates cannot be distinguished if they lie within a volume less than Planck's constant $h$. Thus, classical phase space is divided into discrete cells of volume:
$$h_0 = h^{3N}$$
where $h = 6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$.

<h4>3. Discrete Microstate Number</h4>
If an assembly occupies a finite accessible phase volume $\\Delta \\Gamma$, the number of quantum microstates $\\Omega$ contained within this volume is:
$$\\Omega = \\frac{\\Delta \\Gamma}{N! \\, h^{3N}} = \\frac{1}{N! \\, h^{3N}} \\int_{\\Delta \\Gamma} d^{3N}q \\, d^{3N}p$$
The factor $N!$ accounts for Gibbs' correction for the fundamental indistinguishability of identical particles, preventing Gibbs' paradox in entropy calculations."""
    },
    {
        "id": "sec-1-4",
        "number": "§1.4",
        "heading": "Density of States and its General Behavior",
        "simulation": "liouville-phase-space-sim",
        "content": """The **density of states** $g(E)$ or $\\Omega(E)$ is the number of accessible microscopic quantum states per unit energy interval in the vicinity of energy $E$.

<h4>1. Phase Volume Below Energy $E$</h4>
Let $\\Phi(E)$ represent the total volume of phase space accessible to the system with total energy less than or equal to $E$:
$$\\Phi(E) = \\int_{H(q, p) \\le E} d^{3N}q \\, d^{3N}p$$
The density of states $g(E)$ is the derivative of $\\Phi(E)$ with respect to energy:
$$g(E) = \\frac{d\\Phi(E)}{dE}$$
The number of microstates in a small energy shell $[E, E + \\delta E]$ is:
$$\\Omega(E) = \\frac{g(E) \\, \\delta E}{N! \\, h^{3N}}$$

<h4>2. Derivation for an Ideal Classical Gas of $N$ Particles</h4>
For an ideal gas of $N$ non-interacting particles of mass $m$ confined in a container of volume $V$, the Hamiltonian depends only on momenta:
$$H = \\sum_{i=1}^{3N} \\frac{p_i^2}{2m} \\le E$$
Integrating over all spatial coordinates yields:
$$\\int_V d^{3N}q = V^N$$
The momentum integral represents the volume of a $3N$-dimensional hypersphere of radius $R = \\sqrt{2mE}$:
$$\\sum_{i=1}^{3N} p_i^2 \\le 2mE$$
The volume of a $D$-dimensional hypersphere of radius $R$ is:
$$V_D(R) = \\frac{\\pi^{D/2}}{\\Gamma\\left(\\frac{D}{2} + 1\\right)} R^D$$
Substituting $D = 3N$ and $R = (2mE)^{1/2}$:
$$\\Phi(E) = V^N \\frac{\\pi^{3N/2}}{\\Gamma\\left(\\frac{3N}{2} + 1\\right)} (2mE)^{3N/2}$$

<h4>3. Exponential Growth with Particle Number</h4>
Differentiating with respect to $E$:
$$g(E) = \\frac{d\\Phi}{dE} = V^N \\frac{\\pi^{3N/2}}{\\Gamma\\left(\\frac{3N}{2}\\right)} (2m)^{3N/2} E^{3N/2 - 1}$$
Because $N \\sim 10^{23}$, the exponent $3N/2 - 1 \\approx 10^{23}$. This shows that:
$$g(E) \\propto E^{10^{23}}$$
The density of states is an overwhelmingly, astronomically steep function of energy. Almost all states below energy $E$ are concentrated in an infinitesimally thin skin directly beneath $E$!"""
    },
    {
        "id": "sec-1-5",
        "number": "§1.5",
        "heading": "Liouville's Theorem and its Dynamical Consequences",
        "simulation": "liouville-phase-space-sim",
        "content": """Liouville's theorem is the foundational theorem of classical statistical mechanics. It governs the time evolution of an ensemble of systems in phase space.

<h4>1. Ensemble Density in Phase Space</h4>
Consider an ensemble of $\\mathcal{N}$ identical systems. Let $d\\mathcal{N}$ be the number of representative points in phase volume $d\\Gamma$ around point $(q, p)$ at time $t$. The phase-space probability density $\\rho(q, p, t)$ is:
$$\\rho(q, p, t) = \\lim_{\\mathcal{N}\\to\\infty} \\frac{d\\mathcal{N}}{\\mathcal{N} \\, d\\Gamma}$$
The total probability is normalized:
$$\\int \\rho(q, p, t) \\, d\\Gamma = 1$$

<h4>2. Continuity Equation in Phase Space</h4>
Because representative points cannot be created or destroyed (conservation of probability), $\\rho$ satisfies the continuity equation in $2f$-dimensional phase space:
$$\\frac{\\partial \\rho}{\\partial t} + \\sum_{i=1}^{3N} \\left[ \\frac{\\partial(\\rho \\dot{q}_i)}{\\partial q_i} + \\frac{\\partial(\\rho \\dot{p}_i)}{\\partial p_i} \\right] = 0$$
Expanding the spatial derivatives:
$$\\frac{\\partial \\rho}{\\partial t} + \\sum_{i=1}^{3N} \\left( \\dot{q}_i \\frac{\\partial \\rho}{\\partial q_i} + \\dot{p}_i \\frac{\\partial \\rho}{\\partial p_i} \\right) + \\rho \\sum_{i=1}^{3N} \\left( \\frac{\\partial \\dot{q}_i}{\\partial q_i} + \\frac{\\partial \\dot{p}_i}{\\partial p_i} \\right) = 0$$

<h4>3. Application of Hamilton's Canonical Equations</h4>
Hamilton's equations of motion state:
$$\\dot{q}_i = \\frac{\\partial H}{\\partial p_i}, \\quad \\dot{p}_i = -\\frac{\\partial H}{\\partial q_i}$$
Taking partial derivatives:
$$\\frac{\\partial \\dot{q}_i}{\\partial q_i} = \\frac{\\partial^2 H}{\\partial q_i \\partial p_i}, \\quad \\frac{\\partial \\dot{p}_i}{\\partial p_i} = -\\frac{\\partial^2 H}{\\partial p_i \\partial q_i}$$
Assuming $H$ is twice continuously differentiable, mixed partial derivatives commute:
$$\\frac{\\partial \\dot{q}_i}{\\partial q_i} + \\frac{\\partial \\dot{p}_i}{\\partial p_i} = \\frac{\\partial^2 H}{\\partial q_i \\partial p_i} - \\frac{\\partial^2 H}{\\partial p_i \\partial q_i} = 0$$
The velocity field in phase space is strictly divergence-free: $\\boldsymbol{\\nabla}_{2f} \\cdot \\mathbf{v}_{\\text{phase}} = 0$.

<h4>4. The Liouville Equation and Incompressibility</h4>
The continuity equation reduces directly to:
$$\\frac{d\\rho}{dt} = \\frac{\\partial \\rho}{\\partial t} + \\sum_{i=1}^{3N} \\left( \\frac{\\partial \\rho}{\\partial q_i} \\dot{q}_i + \\frac{\\partial \\rho}{\\partial p_i} \\dot{p}_i \\right) = 0$$
<blockquote>
<strong>Liouville's Theorem:</strong> The convective (substantial) derivative of the phase space density following the motion of representative points is zero:
$$\\frac{d\\rho}{dt} = 0$$
An ensemble of systems flows through phase space like an <strong>ideal, incompressible fluid</strong>.
</blockquote>

In terms of Poisson brackets, where $\\{A, B\\} = \\sum_i \\left( \\frac{\\partial A}{\\partial q_i}\\frac{\\partial B}{\\partial p_i} - \\frac{\\partial A}{\\partial p_i}\\frac{\\partial B}{\\partial q_i} \\right)$:
$$\\frac{\\partial \\rho}{\\partial t} = -\\{\\rho, H\\}$$
For statistical equilibrium, $\\frac{\\partial \\rho}{\\partial t} = 0 \\implies \\{\\rho, H\\} = 0$. Hence, $\\rho$ can only be a function of invariants of the motion (such as energy $H(q, p)$)."""
    },
    {
        "id": "sec-1-6",
        "number": "§1.6",
        "heading": "The Postulates of Classical Statistical Mechanics",
        "simulation": "microstates-macrostates-sim",
        "content": """Because we cannot track $10^{23}$ coordinates, classical statistical mechanics establishes foundational postulates to compute statistical averages.

<h4>1. The Postulate of Equal A Priori Probabilities</h4>
<blockquote>
<strong>Fundamental Postulate:</strong> For an isolated system in thermodynamic equilibrium with energy $E$ in range $[E, E + \\delta E]$, all accessible microscopic states within that energy shell are equally probable:
$$P_i = \\begin{cases} \\frac{1}{\\Omega(E)} & \\text{if } E \\le E_i \\le E + \\delta E \\\\ 0 & \\text{otherwise} \\end{cases}$$
</blockquote>
In phase space, this implies that the equilibrium density $\\rho(q, p)$ is strictly uniform across the accessible energy hypersurface:
$$\\rho(q, p) = \\begin{cases} C & \\text{for } E \\le H(q, p) \\le E + \\delta E \\\\ 0 & \\text{elsewhere} \\end{cases}$$

<h4>2. The Ergodic Hypothesis</h4>
How can an ensemble average (an imaginary average across $10^9$ parallel virtual universes) equal the time average observed by an experimenter measuring a single physical system over time?
The **Ergodic Hypothesis** (Boltzmann, 1871) asserts:
<blockquote>
The phase trajectory of an isolated system passes through <em>every single accessible point</em> on the constant energy surface $H(q, p) = E$ before returning to its starting state.
</blockquote>
Because mathematical trajectories cannot intersect without self-repeating, modern physics relies on the **Quasi-Ergodic Theorem** (Birkhoff and von Neumann):
The phase trajectory comes arbitrarily close to every accessible point on the energy surface and spends an amount of time in any phase region proportional to its phase volume:
$$\\langle A \\rangle_{\\text{time}} = \\lim_{T\\to\\infty} \\frac{1}{T} \\int_0^T A(q(t), p(t)) \\, dt = \\int A(q, p) \\rho(q, p) \\, d\\Gamma = \\langle A \\rangle_{\\text{ensemble}}$$"""
    },
    {
        "id": "sec-1-7",
        "number": "§1.7",
        "heading": "Stirling's Approximation and Asymptotic Series",
        "simulation": "entropy-stirling-sim",
        "content": """Statistical mechanics continually requires evaluating factorials of astronomical numbers: $N!$, where $N \\sim 10^{23}$. Stirling's approximation provides the indispensable asymptotic mathematical tool.

<h4>1. Integral Representation of $N!$</h4>
Using Euler's Gamma function:
$$N! = \\Gamma(N + 1) = \\int_0^\\infty x^N e^{-x} \\, dx = \\int_0^\\infty e^{N \\ln x - x} \\, dx$$
Let $f(x) = N \\ln x - x$. To evaluate this integral by the saddle-point (Laplace's) method, find the extremum of $f(x)$:
$$f'(x) = \\frac{N}{x} - 1 = 0 \\implies x_0 = N$$
The second derivative at the peak is:
$$f''(x_0) = -\\frac{N}{x_0^2} = -\\frac{1}{N} < 0$$
Expanding $f(x)$ in a Taylor series about $x_0 = N$:
$$f(x) \\approx f(N) + \\frac{1}{2}f''(N)(x - N)^2 = N \\ln N - N - \\frac{(x - N)^2}{2N}$$

<h4>2. Saddle-Point Gaussian Integration</h4>
Substitute this Taylor expansion into the integral:
$$N! \\approx e^{N \\ln N - N} \\int_{-\\infty}^\\infty e^{-\\frac{(x - N)^2}{2N}} \\, dx$$
Using the standard Gaussian integral $\\int_{-\\infty}^\\infty e^{-u^2/(2N)} du = \\sqrt{2\\pi N}$:
$$N! \\approx \\sqrt{2\\pi N} \\left(\\frac{N}{e}\\right)^N$$

<h4>3. Logarithmic Form of Stirling's Approximation</h4>
Taking the natural logarithm of both sides:
$$\\ln(N!) = N \\ln N - N + \\frac{1}{2}\\ln(2\\pi N) + \\mathcal{O}\\left(\\frac{1}{N}\\right)$$
For macroscopic physics where $N \\sim 10^{23}$:
$$\\frac{1}{2}\\ln(2\\pi N) \\approx \\frac{1}{2}\\ln(10^{24}) \\approx 27.6$$
While $N \\ln N \\sim 10^{23} \\times 53 \\sim 5.3 \\times 10^{24}$. The logarithmic term $\\frac{1}{2}\\ln(2\\pi N)$ is completely negligible compared to $N$:
$$\\ln(N!) \\approx N \\ln N - N$$
Differentiating with respect to $N$ yields the ubiquitous relation:
$$\\frac{d}{dN} \\ln(N!) \\approx \\ln N$$"""
    },
    {
        "id": "sec-1-8",
        "number": "§1.8",
        "heading": "Thermodynamic Probability and Statistical Weight",
        "simulation": "microstates-macrostates-sim",
        "content": """The **thermodynamic probability** $W$, also called the **statistical weight** or **multiplicity**, is the total number of microstates that realize a given macrostate.

<h4>1. Mathematical Distinction: Mathematical Probability vs $W$</h4>
In ordinary mathematics, probability $P$ is a fraction between $0$ and $1$: $0 \\le P \\le 1$.
In statistical physics, **thermodynamic probability** $W$ is an enormous integer ($W \\ge 1$):
$$W \\in \\{1, 2, 3, \\dots, 10^{10^{23}}\\}$$
The normalized mathematical probability of a macrostate is $P = W / \\sum W$.

<h4>2. Combinatorial Derivation for Two-Level Systems</h4>
Consider an assembly of $N$ localized, independent particles (such as magnetic spin-1/2 dipoles in an external magnetic field). Each particle can point UP ($+1$) or DOWN ($-1$).
A macrostate is defined by the number of UP spins $n$ (leaving $N - n$ DOWN spins). The number of microscopic arrangements realizing this macrostate is given by the binomial coefficient:
$$W(N, n) = \\binom{N}{n} = \\frac{N!}{n! \\, (N - n)!}$$

<h4>3. Determination of the Most Probable Macrostate</h4>
To find the macrostate that maximizes $W$, maximize $\\ln W$ with respect to $n$:
$$\\ln W = \\ln(N!) - \\ln(n!) - \\ln((N - n)!)$$
Applying Stirling's approximation $\\ln(x!) \\approx x \\ln x - x$:
$$\\ln W \\approx N\\ln N - n\\ln n - (N - n)\\ln(N - n)$$
Setting the derivative to zero:
$$\\frac{\\partial \\ln W}{\\partial n} = -\\ln n - 1 + \\ln(N - n) + 1 = \\ln\\left(\\frac{N - n}{n}\\right) = 0$$
$$\\frac{N - n}{n} = 1 \\implies n^* = \\frac{N}{2}$$
The most probable macrostate occurs at exact symmetry: half the spins UP, half DOWN.

<h4>4. Sharpness of the Multiplicity Peak</h4>
Expanding $\\ln W(n)$ around $n^* = N/2 + \\delta$:
$$W(\\delta) \\approx W_{\\max} \\exp\\left( -\\frac{2\\delta^2}{N} \\right)$$
For $N = 10^{20}$, if the system deviates by just $\\delta / N = 10^{-6}$ (one part in a million), the probability drops by:
$$\\exp\\left( -2 \\frac{(10^{14})^2}{10^{20}} \\right) = \\exp(-2 \\times 10^8) \\approx 10^{-86,858,896} \\approx 0$$
The maximum macrostate is so overwhelmingly dominant that the system spends essentially $100\\%$ of its time in this state."""
    },
    {
        "id": "sec-1-9",
        "number": "§1.9",
        "heading": "Statistical Equilibrium and the Boltzmann Entropy Relation",
        "simulation": "entropy-stirling-sim",
        "content": """Statistical equilibrium is the macroscopic state corresponding to maximum thermodynamic probability. We now derive the statistical origin of Temperature and Entropy.

<h4>1. Thermal Contact Between Isolated Subsystems</h4>
Consider two isolated assemblies $A_1$ and $A_2$ with fixed volumes $V_1, V_2$ and particle numbers $N_1, N_2$. Let their energies be $E_1$ and $E_2$.
Bring them into thermal contact through a rigid, impermeable, diathermal wall. The combined system $A = A_1 + A_2$ is isolated:
$$E = E_1 + E_2 = \\text{constant} \\implies dE_1 = -dE_2$$
The total multiplicity of the composite system is the product of individual multiplicities:
$$W(E, E_1) = W_1(E_1) \\times W_2(E_2) = W_1(E_1) \\times W_2(E - E_1)$$
Taking logarithms:
$$\\ln W(E, E_1) = \\ln W_1(E_1) + \\ln W_2(E_2)$$

<h4>2. Condition for Statistical Equilibrium</h4>
In equilibrium, the combined system settles into the most probable energy configuration:
$$\\frac{\\partial \\ln W}{\\partial E_1} = 0 \\implies \\frac{\\partial \\ln W_1}{\\partial E_1} + \\frac{\\partial \\ln W_2}{\\partial E_2} \\frac{\\partial E_2}{\\partial E_1} = 0$$
Since $\\frac{\\partial E_2}{\\partial E_1} = -1$:
$$\\left(\\frac{\\partial \\ln W_1}{\\partial E_1}\\right)_{V_1, N_1} = \\left(\\frac{\\partial \\ln W_2}{\\partial E_2}\\right)_{V_2, N_2}$$
We define the thermodynamic parameter $\\beta$:
$$\\beta \\equiv \\left(\\frac{\\partial \\ln W}{\\partial E}\\right)_{V, N}$$
Thermal equilibrium requires: $\\beta_1 = \\beta_2$.

<h4>3. Derivation of the Boltzmann Entropy Relation ($S = k_B \\ln W$)</h4>
In classical thermodynamics, thermal equilibrium between two bodies requires equality of temperature: $T_1 = T_2$.
Furthermore, the thermodynamic definition of temperature is:
$$\\frac{1}{T} = \\left(\\frac{\\partial S}{\\partial E}\\right)_{V, N}$$
Comparing this with $\\beta = \\frac{\\partial \\ln W}{\\partial E}$, there must be a universal constant $k_B$ such that:
$$\\beta = \\frac{1}{k_B T}$$
$$\\frac{\\partial S}{\\partial E} = k_B \\frac{\\partial \\ln W}{\\partial E}$$
Integrating gives the celebrated **Boltzmann Entropy Formula**:
$$S = k_B \\ln W$$
where $k_B = 1.380649 \\times 10^{-23}\\text{ J/K}$ is Boltzmann's constant.
Because $W_{12} = W_1 W_2$, the logarithm ensures that entropy is strictly additive:
$$S_{12} = k_B \\ln(W_1 W_2) = k_B \\ln W_1 + k_B \\ln W_2 = S_1 + S_2$$"""
    },
    {
        "id": "sec-1-10",
        "number": "§1.10",
        "heading": "Macrostates and Microstates in Equilibrium Systems",
        "simulation": "microstates-macrostates-sim",
        "content": """The distinction between macrostates and microstates explains the arrow of time and the Second Law of Thermodynamics.

<h4>1. Microscopic Chaos vs. Macroscopic Determinism</h4>
A **microstate** is a detailed microscopic snapshot:
$$\\mathbf{X}(t) = (q_1(t), \\dots, q_{3N}(t), p_1(t), \\dots, p_{3N}(t))$$
According to classical mechanics, microstates follow time-reversible Hamiltonian dynamics: if every particle velocity were reversed, the system would trace its path backward.
Yet a **macrostate** is defined by thermodynamic variables $(E, V, N)$ and thermodynamic probability $W$. The Second Law of Thermodynamics states:
$$dS \\ge 0 \\iff d\\ln W \\ge 0$$
Systems evolve spontaneously from macrostates of low multiplicity to macrostates of overwhelmingly high multiplicity.

<h4>2. Why Systems Never Spontaneously De-mix</h4>
Consider $N = 10^{22}$ gas molecules initially confined to the left half of a container of volume $V$. The partition is removed.
The probability that at any future time, all $N$ molecules will spontaneously be found simultaneously in the left half is:
$$P = \\left(\\frac{1}{2}\\right)^N = 2^{-10^{22}} = 10^{-3 \\times 10^{21}}$$
Even if the universe existed for $10^{100}$ years, the probability of observing this fluctuation is effectively zero.
Thermodynamic irreversibility is not a breakdown of microscopic mechanics; it is the statistical certainty of vast numbers!"""
    }
]

u1_problems = [
    {
        "id": "prob-1-1",
        "difficulty": "Medium",
        "title": "Phase Space Volume and Trajectory of a Free Relativistic Particle",
        "question": "A free ultra-relativistic particle of rest mass $m_0$ and energy $E = p c$ is confined within a 3D box of volume $V$. (a) Calculate the phase space volume $\\Phi(E)$ accessible to this particle with energy less than or equal to $E$. (b) Determine the density of states $g(E) = d\\Phi/dE$ and the number of quantum states available in the energy interval $[E, E + dE]$.",
        "steps": [
            {
                "title": "Step 1: Write down the phase volume integral",
                "math": "$$\\Phi(E) = \\int_{H \\le E} d^3q \\, d^3p = \\left( \\int_V d^3q \\right) \\left( \\int_{p \\le E/c} d^3p \\right)$$",
                "explanation": "Because the particle is free, the spatial integral is simply the container volume $V$, and the momentum integral is over a 3D sphere of radius $p_{\\max} = E/c$."
            },
            {
                "title": "Step 2: Compute the momentum sphere volume",
                "math": "$$\\int_{p \\le E/c} d^3p = \\frac{4}{3}\\pi p_{\\max}^3 = \\frac{4\\pi}{3}\\left(\\frac{E}{c}\\right)^3 = \\frac{4\\pi E^3}{3 c^3}$$\n$$\\Phi(E) = \\frac{4\\pi V E^3}{3 c^3}$$",
                "explanation": "This gives the total continuous volume of phase space occupied by states with energy up to $E$."
            },
            {
                "title": "Step 3: Differentiate to find density of states g(E)",
                "math": "$$g(E) = \\frac{d\\Phi(E)}{dE} = \\frac{4\\pi V E^2}{c^3}$$\n$$\\text{Number of quantum states } d\\Omega = \\frac{g(E)dE}{h^3} = \\frac{4\\pi V E^2}{c^3 h^3} dE$$",
                "explanation": "For an ultra-relativistic particle, the density of states scales quadratically with energy ($g(E) \\propto E^2$), in contrast to the non-relativistic square root dependence ($g(E) \\propto E^{1/2}$)."
            }
        ]
    },
    {
        "id": "prob-1-2",
        "difficulty": "Hard",
        "title": "Proof of Liouville's Incompressibility for a Charged Particle in a Magnetic Field",
        "question": "A particle of mass $m$ and charge $q$ moves in an arbitrary magnetic field $\\mathbf{B}(\\mathbf{r}) = \\boldsymbol{\\nabla} \\times \\mathbf{A}(\\mathbf{r})$. Prove that Liouville's theorem $\\frac{\\partial \\dot{q}_i}{\\partial q_i} + \\frac{\\partial \\dot{p}_i}{\\partial p_i} = 0$ holds identically in the presence of velocity-dependent magnetic vector potentials.",
        "steps": [
            {
                "title": "Step 1: Write the canonical Hamiltonian for a charged particle",
                "math": "$$H(\\mathbf{r}, \\mathbf{p}) = \\frac{1}{2m}(\\mathbf{p} - q\\mathbf{A}(\\mathbf{r}))^2 + q\\phi(\\mathbf{r})$$",
                "explanation": "Here $\\mathbf{p} = m\\mathbf{v} + q\\mathbf{A}$ is the canonical momentum, which differs from the mechanical momentum $m\\mathbf{v}$."
            },
            {
                "title": "Step 2: Apply Hamilton's canonical equations",
                "math": "$$\\dot{r}_i = \\frac{\\partial H}{\\partial p_i} = \\frac{p_i - q A_i(\\mathbf{r})}{m}$$\n$$\\dot{p}_i = -\\frac{\\partial H}{\\partial r_i} = \\frac{q}{m} \\sum_{j=1}^3 (p_j - q A_j) \\frac{\\partial A_j}{\\partial r_i} - q \\frac{\\partial \\phi}{\\partial r_i}$$",
                "explanation": "These are the exact canonical velocity and force equations."
            },
            {
                "title": "Step 3: Evaluate phase velocity divergence",
                "math": "$$\\frac{\\partial \\dot{r}_i}{\\partial r_i} = \\frac{\\partial}{\\partial r_i}\\left( \\frac{p_i - q A_i}{m} \\right) = -\\frac{q}{m}\\frac{\\partial A_i}{\\partial r_i}$$\n$$\\frac{\\partial \\dot{p}_i}{\\partial p_i} = \\frac{\\partial}{\\partial p_i}\\left( \\frac{q}{m} (p_i - q A_i)\\frac{\\partial A_i}{\\partial r_i} + \\dots \\right) = \\frac{q}{m}\\frac{\\partial A_i}{\\partial r_i}$$\n$$\\frac{\\partial \\dot{r}_i}{\\partial r_i} + \\frac{\\partial \\dot{p}_i}{\\partial p_i} = -\\frac{q}{m}\\frac{\\partial A_i}{\\partial r_i} + \\frac{q}{m}\\frac{\\partial A_i}{\\partial r_i} = 0$$",
                "explanation": "Summing over $i=1,2,3$ yields identically zero, proving that phase space volume is strictly conserved even in external electromagnetic fields."
            }
        ]
    },
    {
        "id": "prob-1-3",
        "difficulty": "Medium",
        "title": "Entropy and Multiplicity of a Paramagnetic Salt",
        "question": "A crystal contains $N$ independent atoms, each having magnetic moment $\\mu$ that can orient either parallel ($+1$) or antiparallel ($-1$) to an external magnetic field $B$. The total energy of the system is $E = -M B = -(2n - N)\\mu B$, where $n$ is the number of parallel dipoles. (a) Express the entropy $S$ as a function of total energy $E$. (b) Derive the temperature $T$ of the system and explain under what conditions negative absolute temperature occurs.",
        "steps": [
            {
                "title": "Step 1: Write multiplicity W(n) and apply Stirling approximation",
                "math": "$$W(n) = \\frac{N!}{n! (N-n)!}$$\n$$\\ln W \\approx N\\ln N - n\\ln n - (N-n)\\ln(N-n)$$",
                "explanation": "Relate $n$ to energy: $E = -(2n - N)\\mu B \\implies n = \\frac{N}{2} - \\frac{E}{2\\mu B}$, and $N - n = \\frac{N}{2} + \\frac{E}{2\\mu B}$."
            },
            {
                "title": "Step 2: Differentiate with respect to E to obtain temperature",
                "math": "$$\\frac{1}{T} = \\frac{\\partial S}{\\partial E} = k_B \\frac{\\partial \\ln W}{\\partial n} \\frac{\\partial n}{\\partial E}$$\n$$\\frac{\\partial \\ln W}{\\partial n} = \\ln\\left(\\frac{N - n}{n}\\right), \\quad \\frac{\\partial n}{\\partial E} = -\\frac{1}{2\\mu B}$$\n$$\\frac{1}{T} = -\\frac{k_B}{2\\mu B} \\ln\\left(\\frac{\\frac{N}{2} + \\frac{E}{2\\mu B}}{\\frac{N}{2} - \\frac{E}{2\\mu B}}\\right) = \\frac{k_B}{2\\mu B} \\ln\\left(\\frac{N\\mu B - E}{N\\mu B + E}\\right)$$",
                "explanation": "This gives the exact inverse temperature equation of state for the paramagnetic dipole system."
            },
            {
                "title": "Step 3: Analyze negative absolute temperature condition",
                "math": "$$\\text{If } E > 0 \\implies N\\mu B - E < N\\mu B + E \\implies \\ln\\left(\\frac{N\\mu B - E}{N\\mu B + E}\\right) < 0 \\implies T < 0$$",
                "explanation": "When energy $E > 0$, more than half the spins are inverted against the field ($n < N/2$). Adding energy inverts more spins toward the single state where all spins are antiparallel ($W=1$), so entropy decreases as energy increases ($dS/dE < 0$). This yields a physically genuine negative absolute temperature, hotter than $+\\infty\\text{ K}$."
            }
        ]
    }
]

with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/unit1_data.json', 'w') as f:
    json.dump({"number": 1, "title": "Classical Statistical Mechanics", "leadSummary": "Phase space, Liouville's theorem, microstates and macrostates, statistical equilibrium, thermodynamic probability, density of states, and Stirling's approximation.", "sections": u1_sections, "problems": u1_problems}, f, indent=2)

print("Unit 1 built successfully with 10 topics and 3 solved problems!")
