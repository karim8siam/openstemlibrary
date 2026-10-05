// Statistical Mechanics (Physics Core Courseware)
// Comprehensive university-standard textbook dataset covering all 7 Units with 64 topics, KaTeX derivations, and 21 solved exam problems.

window.COURSE_DATA = {
  "courseTitle": "Statistical Mechanics",
  "courseCode": "PHYSICS",
  "department": "Department of Physics",
  "institution": "OpenSTEM Global Academic Press",
  "authorContact": "shahriyarkarimsiam@gmail.com",
  "units": [
    {
      "number": 1,
      "title": "Classical Statistical Mechanics",
      "leadSummary": "Phase space, Liouville's theorem, microstates and macrostates, statistical equilibrium, thermodynamic probability, density of states, and Stirling's approximation.",
      "sections": [
        {
          "id": "sec-1-1",
          "number": "\u00a71.1",
          "heading": "The Scope of Statistical Physics and Assemblies",
          "simulation": "microstates-macrostates-sim",
          "content": "Statistical mechanics bridges the microscopic dynamics of individual atoms and molecules with the macroscopic laws of classical thermodynamics. A macroscopic system typically contains on the order of Avogadro's number $N \\sim 10^{23}$ particles. Directly solving $10^{23}$ coupled classical equations of motion or solving the Schr\u00f6dinger equation in a $10^{23}$-dimensional Hilbert space is computationally and analytically impossible.\n\n<h4>1. Microscopic vs. Macroscopic Descriptions</h4>\nIn classical mechanics, the exact state of a system of $N$ particles is determined by specifying all generalized coordinates $q_i$ and conjugate momenta $p_i$ ($i = 1, 2, \\dots, 3N$). In quantum mechanics, it is specified by an exact many-body state vector $|\\Psi(t)\\rangle$. This microscopic specification contains vastly more information than can ever be observed experimentally.\n\nConversely, a **macroscopic description** characterizes the system using a few gross thermodynamic parameters: total internal energy $E$, volume $V$, pressure $P$, temperature $T$, and chemical potential $\\mu$. Statistical mechanics demonstrates that macroscopic observables are exact statistical averages over accessible microscopic states:\n$$\\langle A \\rangle = \\sum_{i} P_i A_i$$\n\n<h4>2. Definition of an Assembly and System Classifications</h4>\nAn **assembly** is a collection of a very large number $N$ of particles (atoms, molecules, ions, photons) confined within a macroscopic volume $V$. Assemblies are classified according to their boundary interactions with their surroundings:\n<ul>\n  <li><strong>Isolated Assembly:</strong> Exchanges neither energy nor matter with its surroundings. Constant internal energy $E$, volume $V$, and particle number $N$ ($dE = 0, dV = 0, dN = 0$).</li>\n  <li><strong>Closed Assembly:</strong> Exchanges energy (heat and mechanical work) with a surrounding thermal reservoir, but cannot exchange matter ($T, V, N$ fixed; $dN = 0$).</li>\n  <li><strong>Open Assembly:</strong> Exchanges both energy and matter with its surroundings ($T, V, \\mu$ fixed).</li>\n</ul>\n\n<h4>3. The Role of Probability in Thermal Physics</h4>\nBecause macroscopic systems are in ceaseless microscopic motion, any macroscopic observable $M$ exhibits microscopic fluctuations $\\Delta M$. For an assembly of $N$ particles, the central limit theorem dictates that relative fluctuations vanish as:\n$$\\frac{\\Delta M}{\\langle M \\rangle} \\sim \\frac{1}{\\sqrt{N}} \\sim \\frac{1}{\\sqrt{10^{23}}} = 10^{-11.5}$$\nThus, statistical averages predict macroscopic phenomena with virtually deterministic experimental precision."
        },
        {
          "id": "sec-1-2",
          "number": "\u00a71.2",
          "heading": "Phase Space and Phase Trajectories",
          "simulation": "liouville-phase-space-sim",
          "content": "To describe the instantaneous mechanical state and dynamical evolution of a classical system, statistical mechanics employs the geometrical concept of **Phase Space**.\n\n<h4>1. Definition of Phase Space</h4>\nFor a system possessing $f$ degrees of freedom, its configuration is specified by $f$ generalized coordinates $q_1, q_2, \\dots, q_f$, and its dynamical state requires $f$ generalized conjugate momenta $p_1, p_2, \\dots, p_f$, where:\n$$p_i = \\frac{\\partial L}{\\partial \\dot{q}_i}$$\nPhase space is an orthogonal, $2f$-dimensional Euclidean space whose Cartesian coordinate axes are $(q_1, \\dots, q_f, p_1, \\dots, p_f)$.\n\n<h4>2. $\\mu$-Space versus $\\Gamma$-Space</h4>\nFollowing Paul and Tatyana Ehrenfest, we distinguish two fundamental phase space formalisms:\n<ul>\n  <li><strong>$\\mu$-Space (Molecule Space):</strong> A 6-dimensional phase space $(x, y, z, p_x, p_y, p_z)$ for a single particle. An assembly of $N$ non-interacting particles is represented by a swarm of $N$ distinct points moving simultaneously in this 6D space.</li>\n  <li><strong>$\\Gamma$-Space (Gas Phase Space):</strong> A $6N$-dimensional phase space for the entire assembly of $N$ particles. The instantaneous microstate of the entire macroscopic assembly corresponds to a <em>single representative point</em>:\n  $$\\mathbf{X} = (q_1, q_2, \\dots, q_{3N}, p_1, p_2, \\dots, p_{3N}) \\in \\mathbb{R}^{6N}$$\n  As time progresses, this single point traces out a continuous curve termed the <strong>phase trajectory</strong>.</li>\n</ul>\n\n<h4>3. Phase Trajectory of a 1D Harmonic Oscillator</h4>\nConsider a 1D harmonic oscillator with mass $m$ and spring constant $k = m\\omega^2$. The Hamiltonian is:\n$$H(q, p) = \\frac{p^2}{2m} + \\frac{1}{2}m\\omega^2 q^2 = E$$\nRearranging in canonical ellipse form:\n$$\\frac{q^2}{\\left(\\sqrt{\\frac{2E}{m\\omega^2}}\\right)^2} + \\frac{p^2}{\\left(\\sqrt{2mE}\\right)^2} = 1$$\nThe phase trajectory is an ellipse centered at the origin with semi-axes:\n$$a = \\sqrt{\\frac{2E}{m\\omega^2}}, \\quad b = \\sqrt{2mE}$$\nThe total area enclosed by this orbit in 2D phase space is:\n$$\\oint p \\, dq = \\pi a b = \\pi \\sqrt{\\frac{2E}{m\\omega^2}} \\sqrt{2mE} = \\frac{2\\pi E}{\\omega} = \\frac{E}{\\nu}$$\nThis demonstrates that the phase trajectory for a conservative periodic system forms a closed loop whose enclosed phase volume is an adiabatic invariant."
        },
        {
          "id": "sec-1-3",
          "number": "\u00a71.3",
          "heading": "Volume in Phase Space and Specification of States",
          "simulation": "liouville-phase-space-sim",
          "content": "In classical continuum mechanics, phase space is infinite and continuous. However, to count discrete microstates and transition to quantum mechanics, phase space must be partitioned into elementary phase cells.\n\n<h4>1. Differential Volume Element in Phase Space</h4>\nThe infinitesimal volume element $d\\Gamma$ of $6N$-dimensional phase space is defined by:\n$$d\\Gamma = dq_1 \\, dq_2 \\dots dq_{3N} \\, dp_1 \\, dp_2 \\dots dp_{3N} = \\prod_{i=1}^{3N} dq_i \\, dp_i = d^{3N}q \\, d^{3N}p$$\nThe dimensions of a coordinate times its conjugate momentum $[q_i p_i]$ are:\n$$[\\text{length}] \\times [\\text{mass} \\cdot \\text{velocity}] = [\\text{energy} \\times \\text{time}] = [\\text{Action}] = \\text{Joule} \\cdot \\text{second}$$\nTherefore, each product $dq_i dp_i$ has physical dimensions of action ($\\,\\text{J}\\cdot\\text{s}$).\n\n<h4>2. Elementary Quantum Phase Cell Volume ($h_0$)</h4>\nAccording to the Heisenberg uncertainty principle:\n$$\\Delta q_i \\Delta p_i \\ge \\frac{\\hbar}{2} \\sim h$$\nTwo physical microstates cannot be distinguished if they lie within a volume less than Planck's constant $h$. Thus, classical phase space is divided into discrete cells of volume:\n$$h_0 = h^{3N}$$\nwhere $h = 6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s}$.\n\n<h4>3. Discrete Microstate Number</h4>\nIf an assembly occupies a finite accessible phase volume $\\Delta \\Gamma$, the number of quantum microstates $\\Omega$ contained within this volume is:\n$$\\Omega = \\frac{\\Delta \\Gamma}{N! \\, h^{3N}} = \\frac{1}{N! \\, h^{3N}} \\int_{\\Delta \\Gamma} d^{3N}q \\, d^{3N}p$$\nThe factor $N!$ accounts for Gibbs' correction for the fundamental indistinguishability of identical particles, preventing Gibbs' paradox in entropy calculations."
        },
        {
          "id": "sec-1-4",
          "number": "\u00a71.4",
          "heading": "Density of States and its General Behavior",
          "simulation": "liouville-phase-space-sim",
          "content": "The **density of states** $g(E)$ or $\\Omega(E)$ is the number of accessible microscopic quantum states per unit energy interval in the vicinity of energy $E$.\n\n<h4>1. Phase Volume Below Energy $E$</h4>\nLet $\\Phi(E)$ represent the total volume of phase space accessible to the system with total energy less than or equal to $E$:\n$$\\Phi(E) = \\int_{H(q, p) \\le E} d^{3N}q \\, d^{3N}p$$\nThe density of states $g(E)$ is the derivative of $\\Phi(E)$ with respect to energy:\n$$g(E) = \\frac{d\\Phi(E)}{dE}$$\nThe number of microstates in a small energy shell $[E, E + \\delta E]$ is:\n$$\\Omega(E) = \\frac{g(E) \\, \\delta E}{N! \\, h^{3N}}$$\n\n<h4>2. Derivation for an Ideal Classical Gas of $N$ Particles</h4>\nFor an ideal gas of $N$ non-interacting particles of mass $m$ confined in a container of volume $V$, the Hamiltonian depends only on momenta:\n$$H = \\sum_{i=1}^{3N} \\frac{p_i^2}{2m} \\le E$$\nIntegrating over all spatial coordinates yields:\n$$\\int_V d^{3N}q = V^N$$\nThe momentum integral represents the volume of a $3N$-dimensional hypersphere of radius $R = \\sqrt{2mE}$:\n$$\\sum_{i=1}^{3N} p_i^2 \\le 2mE$$\nThe volume of a $D$-dimensional hypersphere of radius $R$ is:\n$$V_D(R) = \\frac{\\pi^{D/2}}{\\Gamma\\left(\\frac{D}{2} + 1\\right)} R^D$$\nSubstituting $D = 3N$ and $R = (2mE)^{1/2}$:\n$$\\Phi(E) = V^N \\frac{\\pi^{3N/2}}{\\Gamma\\left(\\frac{3N}{2} + 1\\right)} (2mE)^{3N/2}$$\n\n<h4>3. Exponential Growth with Particle Number</h4>\nDifferentiating with respect to $E$:\n$$g(E) = \\frac{d\\Phi}{dE} = V^N \\frac{\\pi^{3N/2}}{\\Gamma\\left(\\frac{3N}{2}\\right)} (2m)^{3N/2} E^{3N/2 - 1}$$\nBecause $N \\sim 10^{23}$, the exponent $3N/2 - 1 \\approx 10^{23}$. This shows that:\n$$g(E) \\propto E^{10^{23}}$$\nThe density of states is an overwhelmingly, astronomically steep function of energy. Almost all states below energy $E$ are concentrated in an infinitesimally thin skin directly beneath $E$!"
        },
        {
          "id": "sec-1-5",
          "number": "\u00a71.5",
          "heading": "Liouville's Theorem and its Dynamical Consequences",
          "simulation": "liouville-phase-space-sim",
          "content": "Liouville's theorem is the foundational theorem of classical statistical mechanics. It governs the time evolution of an ensemble of systems in phase space.\n\n<h4>1. Ensemble Density in Phase Space</h4>\nConsider an ensemble of $\\mathcal{N}$ identical systems. Let $d\\mathcal{N}$ be the number of representative points in phase volume $d\\Gamma$ around point $(q, p)$ at time $t$. The phase-space probability density $\\rho(q, p, t)$ is:\n$$\\rho(q, p, t) = \\lim_{\\mathcal{N}\\to\\infty} \\frac{d\\mathcal{N}}{\\mathcal{N} \\, d\\Gamma}$$\nThe total probability is normalized:\n$$\\int \\rho(q, p, t) \\, d\\Gamma = 1$$\n\n<h4>2. Continuity Equation in Phase Space</h4>\nBecause representative points cannot be created or destroyed (conservation of probability), $\\rho$ satisfies the continuity equation in $2f$-dimensional phase space:\n$$\\frac{\\partial \\rho}{\\partial t} + \\sum_{i=1}^{3N} \\left[ \\frac{\\partial(\\rho \\dot{q}_i)}{\\partial q_i} + \\frac{\\partial(\\rho \\dot{p}_i)}{\\partial p_i} \\right] = 0$$\nExpanding the spatial derivatives:\n$$\\frac{\\partial \\rho}{\\partial t} + \\sum_{i=1}^{3N} \\left( \\dot{q}_i \\frac{\\partial \\rho}{\\partial q_i} + \\dot{p}_i \\frac{\\partial \\rho}{\\partial p_i} \\right) + \\rho \\sum_{i=1}^{3N} \\left( \\frac{\\partial \\dot{q}_i}{\\partial q_i} + \\frac{\\partial \\dot{p}_i}{\\partial p_i} \\right) = 0$$\n\n<h4>3. Application of Hamilton's Canonical Equations</h4>\nHamilton's equations of motion state:\n$$\\dot{q}_i = \\frac{\\partial H}{\\partial p_i}, \\quad \\dot{p}_i = -\\frac{\\partial H}{\\partial q_i}$$\nTaking partial derivatives:\n$$\\frac{\\partial \\dot{q}_i}{\\partial q_i} = \\frac{\\partial^2 H}{\\partial q_i \\partial p_i}, \\quad \\frac{\\partial \\dot{p}_i}{\\partial p_i} = -\\frac{\\partial^2 H}{\\partial p_i \\partial q_i}$$\nAssuming $H$ is twice continuously differentiable, mixed partial derivatives commute:\n$$\\frac{\\partial \\dot{q}_i}{\\partial q_i} + \\frac{\\partial \\dot{p}_i}{\\partial p_i} = \\frac{\\partial^2 H}{\\partial q_i \\partial p_i} - \\frac{\\partial^2 H}{\\partial p_i \\partial q_i} = 0$$\nThe velocity field in phase space is strictly divergence-free: $\\boldsymbol{\\nabla}_{2f} \\cdot \\mathbf{v}_{\\text{phase}} = 0$.\n\n<h4>4. The Liouville Equation and Incompressibility</h4>\nThe continuity equation reduces directly to:\n$$\\frac{d\\rho}{dt} = \\frac{\\partial \\rho}{\\partial t} + \\sum_{i=1}^{3N} \\left( \\frac{\\partial \\rho}{\\partial q_i} \\dot{q}_i + \\frac{\\partial \\rho}{\\partial p_i} \\dot{p}_i \\right) = 0$$\n<blockquote>\n<strong>Liouville's Theorem:</strong> The convective (substantial) derivative of the phase space density following the motion of representative points is zero:\n$$\\frac{d\\rho}{dt} = 0$$\nAn ensemble of systems flows through phase space like an <strong>ideal, incompressible fluid</strong>.\n</blockquote>\n\nIn terms of Poisson brackets, where $\\{A, B\\} = \\sum_i \\left( \\frac{\\partial A}{\\partial q_i}\\frac{\\partial B}{\\partial p_i} - \\frac{\\partial A}{\\partial p_i}\\frac{\\partial B}{\\partial q_i} \\right)$:\n$$\\frac{\\partial \\rho}{\\partial t} = -\\{\\rho, H\\}$$\nFor statistical equilibrium, $\\frac{\\partial \\rho}{\\partial t} = 0 \\implies \\{\\rho, H\\} = 0$. Hence, $\\rho$ can only be a function of invariants of the motion (such as energy $H(q, p)$)."
        },
        {
          "id": "sec-1-6",
          "number": "\u00a71.6",
          "heading": "The Postulates of Classical Statistical Mechanics",
          "simulation": "microstates-macrostates-sim",
          "content": "Because we cannot track $10^{23}$ coordinates, classical statistical mechanics establishes foundational postulates to compute statistical averages.\n\n<h4>1. The Postulate of Equal A Priori Probabilities</h4>\n<blockquote>\n<strong>Fundamental Postulate:</strong> For an isolated system in thermodynamic equilibrium with energy $E$ in range $[E, E + \\delta E]$, all accessible microscopic states within that energy shell are equally probable:\n$$P_i = \\begin{cases} \\frac{1}{\\Omega(E)} & \\text{if } E \\le E_i \\le E + \\delta E \\\\ 0 & \\text{otherwise} \\end{cases}$$\n</blockquote>\nIn phase space, this implies that the equilibrium density $\\rho(q, p)$ is strictly uniform across the accessible energy hypersurface:\n$$\\rho(q, p) = \\begin{cases} C & \\text{for } E \\le H(q, p) \\le E + \\delta E \\\\ 0 & \\text{elsewhere} \\end{cases}$$\n\n<h4>2. The Ergodic Hypothesis</h4>\nHow can an ensemble average (an imaginary average across $10^9$ parallel virtual universes) equal the time average observed by an experimenter measuring a single physical system over time?\nThe **Ergodic Hypothesis** (Boltzmann, 1871) asserts:\n<blockquote>\nThe phase trajectory of an isolated system passes through <em>every single accessible point</em> on the constant energy surface $H(q, p) = E$ before returning to its starting state.\n</blockquote>\nBecause mathematical trajectories cannot intersect without self-repeating, modern physics relies on the **Quasi-Ergodic Theorem** (Birkhoff and von Neumann):\nThe phase trajectory comes arbitrarily close to every accessible point on the energy surface and spends an amount of time in any phase region proportional to its phase volume:\n$$\\langle A \\rangle_{\\text{time}} = \\lim_{T\\to\\infty} \\frac{1}{T} \\int_0^T A(q(t), p(t)) \\, dt = \\int A(q, p) \\rho(q, p) \\, d\\Gamma = \\langle A \\rangle_{\\text{ensemble}}$$"
        },
        {
          "id": "sec-1-7",
          "number": "\u00a71.7",
          "heading": "Stirling's Approximation and Asymptotic Series",
          "simulation": "entropy-stirling-sim",
          "content": "Statistical mechanics continually requires evaluating factorials of astronomical numbers: $N!$, where $N \\sim 10^{23}$. Stirling's approximation provides the indispensable asymptotic mathematical tool.\n\n<h4>1. Integral Representation of $N!$</h4>\nUsing Euler's Gamma function:\n$$N! = \\Gamma(N + 1) = \\int_0^\\infty x^N e^{-x} \\, dx = \\int_0^\\infty e^{N \\ln x - x} \\, dx$$\nLet $f(x) = N \\ln x - x$. To evaluate this integral by the saddle-point (Laplace's) method, find the extremum of $f(x)$:\n$$f'(x) = \\frac{N}{x} - 1 = 0 \\implies x_0 = N$$\nThe second derivative at the peak is:\n$$f''(x_0) = -\\frac{N}{x_0^2} = -\\frac{1}{N} < 0$$\nExpanding $f(x)$ in a Taylor series about $x_0 = N$:\n$$f(x) \\approx f(N) + \\frac{1}{2}f''(N)(x - N)^2 = N \\ln N - N - \\frac{(x - N)^2}{2N}$$\n\n<h4>2. Saddle-Point Gaussian Integration</h4>\nSubstitute this Taylor expansion into the integral:\n$$N! \\approx e^{N \\ln N - N} \\int_{-\\infty}^\\infty e^{-\\frac{(x - N)^2}{2N}} \\, dx$$\nUsing the standard Gaussian integral $\\int_{-\\infty}^\\infty e^{-u^2/(2N)} du = \\sqrt{2\\pi N}$:\n$$N! \\approx \\sqrt{2\\pi N} \\left(\\frac{N}{e}\\right)^N$$\n\n<h4>3. Logarithmic Form of Stirling's Approximation</h4>\nTaking the natural logarithm of both sides:\n$$\\ln(N!) = N \\ln N - N + \\frac{1}{2}\\ln(2\\pi N) + \\mathcal{O}\\left(\\frac{1}{N}\\right)$$\nFor macroscopic physics where $N \\sim 10^{23}$:\n$$\\frac{1}{2}\\ln(2\\pi N) \\approx \\frac{1}{2}\\ln(10^{24}) \\approx 27.6$$\nWhile $N \\ln N \\sim 10^{23} \\times 53 \\sim 5.3 \\times 10^{24}$. The logarithmic term $\\frac{1}{2}\\ln(2\\pi N)$ is completely negligible compared to $N$:\n$$\\ln(N!) \\approx N \\ln N - N$$\nDifferentiating with respect to $N$ yields the ubiquitous relation:\n$$\\frac{d}{dN} \\ln(N!) \\approx \\ln N$$"
        },
        {
          "id": "sec-1-8",
          "number": "\u00a71.8",
          "heading": "Thermodynamic Probability and Statistical Weight",
          "simulation": "microstates-macrostates-sim",
          "content": "The **thermodynamic probability** $W$, also called the **statistical weight** or **multiplicity**, is the total number of microstates that realize a given macrostate.\n\n<h4>1. Mathematical Distinction: Mathematical Probability vs $W$</h4>\nIn ordinary mathematics, probability $P$ is a fraction between $0$ and $1$: $0 \\le P \\le 1$.\nIn statistical physics, **thermodynamic probability** $W$ is an enormous integer ($W \\ge 1$):\n$$W \\in \\{1, 2, 3, \\dots, 10^{10^{23}}\\}$$\nThe normalized mathematical probability of a macrostate is $P = W / \\sum W$.\n\n<h4>2. Combinatorial Derivation for Two-Level Systems</h4>\nConsider an assembly of $N$ localized, independent particles (such as magnetic spin-1/2 dipoles in an external magnetic field). Each particle can point UP ($+1$) or DOWN ($-1$).\nA macrostate is defined by the number of UP spins $n$ (leaving $N - n$ DOWN spins). The number of microscopic arrangements realizing this macrostate is given by the binomial coefficient:\n$$W(N, n) = \\binom{N}{n} = \\frac{N!}{n! \\, (N - n)!}$$\n\n<h4>3. Determination of the Most Probable Macrostate</h4>\nTo find the macrostate that maximizes $W$, maximize $\\ln W$ with respect to $n$:\n$$\\ln W = \\ln(N!) - \\ln(n!) - \\ln((N - n)!)$$\nApplying Stirling's approximation $\\ln(x!) \\approx x \\ln x - x$:\n$$\\ln W \\approx N\\ln N - n\\ln n - (N - n)\\ln(N - n)$$\nSetting the derivative to zero:\n$$\\frac{\\partial \\ln W}{\\partial n} = -\\ln n - 1 + \\ln(N - n) + 1 = \\ln\\left(\\frac{N - n}{n}\\right) = 0$$\n$$\\frac{N - n}{n} = 1 \\implies n^* = \\frac{N}{2}$$\nThe most probable macrostate occurs at exact symmetry: half the spins UP, half DOWN.\n\n<h4>4. Sharpness of the Multiplicity Peak</h4>\nExpanding $\\ln W(n)$ around $n^* = N/2 + \\delta$:\n$$W(\\delta) \\approx W_{\\max} \\exp\\left( -\\frac{2\\delta^2}{N} \\right)$$\nFor $N = 10^{20}$, if the system deviates by just $\\delta / N = 10^{-6}$ (one part in a million), the probability drops by:\n$$\\exp\\left( -2 \\frac{(10^{14})^2}{10^{20}} \\right) = \\exp(-2 \\times 10^8) \\approx 10^{-86,858,896} \\approx 0$$\nThe maximum macrostate is so overwhelmingly dominant that the system spends essentially $100\\%$ of its time in this state."
        },
        {
          "id": "sec-1-9",
          "number": "\u00a71.9",
          "heading": "Statistical Equilibrium and the Boltzmann Entropy Relation",
          "simulation": "entropy-stirling-sim",
          "content": "Statistical equilibrium is the macroscopic state corresponding to maximum thermodynamic probability. We now derive the statistical origin of Temperature and Entropy.\n\n<h4>1. Thermal Contact Between Isolated Subsystems</h4>\nConsider two isolated assemblies $A_1$ and $A_2$ with fixed volumes $V_1, V_2$ and particle numbers $N_1, N_2$. Let their energies be $E_1$ and $E_2$.\nBring them into thermal contact through a rigid, impermeable, diathermal wall. The combined system $A = A_1 + A_2$ is isolated:\n$$E = E_1 + E_2 = \\text{constant} \\implies dE_1 = -dE_2$$\nThe total multiplicity of the composite system is the product of individual multiplicities:\n$$W(E, E_1) = W_1(E_1) \\times W_2(E_2) = W_1(E_1) \\times W_2(E - E_1)$$\nTaking logarithms:\n$$\\ln W(E, E_1) = \\ln W_1(E_1) + \\ln W_2(E_2)$$\n\n<h4>2. Condition for Statistical Equilibrium</h4>\nIn equilibrium, the combined system settles into the most probable energy configuration:\n$$\\frac{\\partial \\ln W}{\\partial E_1} = 0 \\implies \\frac{\\partial \\ln W_1}{\\partial E_1} + \\frac{\\partial \\ln W_2}{\\partial E_2} \\frac{\\partial E_2}{\\partial E_1} = 0$$\nSince $\\frac{\\partial E_2}{\\partial E_1} = -1$:\n$$\\left(\\frac{\\partial \\ln W_1}{\\partial E_1}\\right)_{V_1, N_1} = \\left(\\frac{\\partial \\ln W_2}{\\partial E_2}\\right)_{V_2, N_2}$$\nWe define the thermodynamic parameter $\\beta$:\n$$\\beta \\equiv \\left(\\frac{\\partial \\ln W}{\\partial E}\\right)_{V, N}$$\nThermal equilibrium requires: $\\beta_1 = \\beta_2$.\n\n<h4>3. Derivation of the Boltzmann Entropy Relation ($S = k_B \\ln W$)</h4>\nIn classical thermodynamics, thermal equilibrium between two bodies requires equality of temperature: $T_1 = T_2$.\nFurthermore, the thermodynamic definition of temperature is:\n$$\\frac{1}{T} = \\left(\\frac{\\partial S}{\\partial E}\\right)_{V, N}$$\nComparing this with $\\beta = \\frac{\\partial \\ln W}{\\partial E}$, there must be a universal constant $k_B$ such that:\n$$\\beta = \\frac{1}{k_B T}$$\n$$\\frac{\\partial S}{\\partial E} = k_B \\frac{\\partial \\ln W}{\\partial E}$$\nIntegrating gives the celebrated **Boltzmann Entropy Formula**:\n$$S = k_B \\ln W$$\nwhere $k_B = 1.380649 \\times 10^{-23}\\text{ J/K}$ is Boltzmann's constant.\nBecause $W_{12} = W_1 W_2$, the logarithm ensures that entropy is strictly additive:\n$$S_{12} = k_B \\ln(W_1 W_2) = k_B \\ln W_1 + k_B \\ln W_2 = S_1 + S_2$$"
        },
        {
          "id": "sec-1-10",
          "number": "\u00a71.10",
          "heading": "Macrostates and Microstates in Equilibrium Systems",
          "simulation": "microstates-macrostates-sim",
          "content": "The distinction between macrostates and microstates explains the arrow of time and the Second Law of Thermodynamics.\n\n<h4>1. Microscopic Chaos vs. Macroscopic Determinism</h4>\nA **microstate** is a detailed microscopic snapshot:\n$$\\mathbf{X}(t) = (q_1(t), \\dots, q_{3N}(t), p_1(t), \\dots, p_{3N}(t))$$\nAccording to classical mechanics, microstates follow time-reversible Hamiltonian dynamics: if every particle velocity were reversed, the system would trace its path backward.\nYet a **macrostate** is defined by thermodynamic variables $(E, V, N)$ and thermodynamic probability $W$. The Second Law of Thermodynamics states:\n$$dS \\ge 0 \\iff d\\ln W \\ge 0$$\nSystems evolve spontaneously from macrostates of low multiplicity to macrostates of overwhelmingly high multiplicity.\n\n<h4>2. Why Systems Never Spontaneously De-mix</h4>\nConsider $N = 10^{22}$ gas molecules initially confined to the left half of a container of volume $V$. The partition is removed.\nThe probability that at any future time, all $N$ molecules will spontaneously be found simultaneously in the left half is:\n$$P = \\left(\\frac{1}{2}\\right)^N = 2^{-10^{22}} = 10^{-3 \\times 10^{21}}$$\nEven if the universe existed for $10^{100}$ years, the probability of observing this fluctuation is effectively zero.\nThermodynamic irreversibility is not a breakdown of microscopic mechanics; it is the statistical certainty of vast numbers!"
        }
      ],
      "problems": [
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
    },
    {
      "number": 2,
      "title": "Statistics and Thermodynamics",
      "leadSummary": "Statistical temperature, microcanonical, canonical, and grand canonical ensembles, free energy, Maxwell velocity distribution, ideal gas Sackur-Tetrode equation, harmonic oscillators, and specific heat.",
      "sections": [
        {
          "id": "sec-2-1",
          "number": "\u00a72.1",
          "heading": "The Statistical Concept of Temperature and the Zeroth Law",
          "simulation": "canonical-boltzmann-sim",
          "content": "In classical thermodynamics, temperature is introduced empirically through the Zeroth Law via thermal equilibrium. Statistical mechanics provides the microscopic explanation of temperature.\n\n<h4>1. Microscopic Definition of Temperature</h4>\nWhen two systems $A_1$ and $A_2$ are in thermal contact with fixed volumes and particle numbers, their total energy $E = E_1 + E_2$ is conserved. As proven in Chapter 1, the condition for the combined multiplicity $W(E_1, E_2) = W_1(E_1)W_2(E_2)$ to attain its maximum is:\n$$\\left(\\frac{\\partial \\ln W_1}{\\partial E_1}\\right)_{V_1, N_1} = \\left(\\frac{\\partial \\ln W_2}{\\partial E_2}\\right)_{V_2, N_2}$$\nWe define the thermodynamic parameter $\\beta$:\n$$\\beta \\equiv \\left(\\frac{\\partial \\ln W}{\\partial E}\\right)_{V, N}$$\nThe statistical absolute temperature $T$ is defined fundamentally as:\n$$\\frac{1}{T} \\equiv k_B \\beta = k_B \\left(\\frac{\\partial \\ln W}{\\partial E}\\right)_{V, N} = \\left(\\frac{\\partial S}{\\partial E}\\right)_{V, N}$$\n\n<h4>2. Statistical Derivation of the Zeroth Law</h4>\nThe Zeroth Law states: *If body A is in thermal equilibrium with body C, and body B is in thermal equilibrium with body C, then body A is in thermal equilibrium with body B.*\nMicroscopically, thermal equilibrium between A and C implies $\\beta_A = \\beta_C$. Equilibrium between B and C implies $\\beta_B = \\beta_C$.\nBy the transitivity of real numbers:\n$$\\beta_A = \\beta_B \\iff T_A = T_B$$\nThe Zeroth Law is thus a mathematical consequence of the transitivity of equality for the statistical parameter $\\beta$.\n\n<h4>3. Physical Direction of Heat Flow</h4>\nIf two systems with $\\beta_1 \\ne \\beta_2$ are placed in thermal contact, spontaneous heat exchange $dE_1 = -dE_2$ changes the total entropy by:\n$$dS = dS_1 + dS_2 = \\left(\\frac{\\partial S_1}{\\partial E_1} - \\frac{\\partial S_2}{\\partial E_2}\\right) dE_1 = k_B (\\beta_1 - \\beta_2) dE_1 = \\left(\\frac{1}{T_1} - \\frac{1}{T_2}\\right) dE_1$$\nAccording to the Second Law, $dS > 0$. If $T_1 > T_2$, then $\\frac{1}{T_1} - \\frac{1}{T_2} < 0$, which requires $dE_1 < 0$.\nHeat must flow spontaneously from the body with higher temperature to the body with lower temperature."
        },
        {
          "id": "sec-2-2",
          "number": "\u00a72.2",
          "heading": "Ensembles: The Microcanonical Ensemble",
          "simulation": "microstates-macrostates-sim",
          "content": "An **ensemble** is an idealized mental collection of a very large number $\\mathcal{N}$ of independent, macroscopic replicas of a system, all satisfying identical thermodynamic constraints.\n\n<h4>1. Specification of the Microcanonical Ensemble</h4>\nThe **Microcanonical Ensemble** represents an **isolated system** with strictly fixed:\n<ul>\n  <li>Total internal energy $E$ within an infinitesimal range $[E, E + \\delta E]$</li>\n  <li>Volume $V$</li>\n  <li>Total number of particles $N$</li>\n</ul>\nNo energy or particle exchange occurs with the exterior environment.\n\n<h4>2. Microcanonical Probability Distribution</h4>\nAccording to the Postulate of Equal A Priori Probabilities, every accessible microstate $r$ within the energy shell is equally likely:\n$$P_r = \\begin{cases} \\frac{1}{\\Omega(E, V, N)} & \\text{if } E \\le E_r \\le E + \\delta E \\\\ 0 & \\text{otherwise} \\end{cases}$$\nThe microcanonical partition function $\\Omega(E, V, N)$ is the total number of quantum microstates accessible to the system:\n$$\\Omega(E, V, N) = \\sum_{E \\le E_r \\le E + \\delta E} 1 = \\frac{1}{N! \\, h^{3N}} \\int_{E \\le H(q, p) \\le E + \\delta E} d^{3N}q \\, d^{3N}p$$\n\n<h4>3. Thermodynamics from the Microcanonical Ensemble</h4>\nThe bridge to thermodynamics is Boltzmann's relation:\n$$S(E, V, N) = k_B \\ln \\Omega(E, V, N)$$\nFrom the fundamental thermodynamic relation $dE = T dS - P dV + \\mu dN$, or rearranged:\n$$dS = \\frac{1}{T} dE + \\frac{P}{T} dV - \\frac{\\mu}{T} dN$$\nWe determine all thermodynamic quantities directly:\n$$\\frac{1}{T} = \\left(\\frac{\\partial S}{\\partial E}\\right)_{V, N}, \\quad \\frac{P}{T} = \\left(\\frac{\\partial S}{\\partial V}\\right)_{E, N}, \\quad \\frac{\\mu}{T} = -\\left(\\frac{\\partial S}{\\partial N}\\right)_{E, V}$$"
        },
        {
          "id": "sec-2-3",
          "number": "\u00a72.3",
          "heading": "The Canonical Ensemble and Connection with Thermodynamics",
          "simulation": "canonical-boltzmann-sim",
          "content": "Most physical systems in laboratory experiments are not isolated; they are maintained at a constant temperature by thermal contact with a large heat bath. This situation is described by the **Canonical Ensemble**.\n\n<h4>1. Derivation of the Boltzmann Canonical Distribution</h4>\nConsider a small system $A$ with microstates $r$ of energy $E_r$, in thermal contact with a huge heat reservoir $R$ at temperature $T$. The combined system $A_0 = A + R$ is isolated with total energy $E_0 = E_r + E_R = \\text{constant}$.\nThe probability $P_r$ of finding system $A$ in a specific microstate $r$ is proportional to the number of accessible states of the reservoir $\\Omega_R(E_0 - E_r)$:\n$$P_r \\propto \\Omega_R(E_0 - E_r) = \\exp\\left( \\frac{S_R(E_0 - E_r)}{k_B} \\right)$$\nBecause the reservoir is much larger than the system ($E_r \\ll E_0$), we expand $S_R$ in a Taylor series about $E_0$:\n$$S_R(E_0 - E_r) \\approx S_R(E_0) - E_r \\left(\\frac{\\partial S_R}{\\partial E_R}\\right)_{E_R=E_0} = S_R(E_0) - \\frac{E_r}{T}$$\nTherefore:\n$$P_r \\propto e^{S_R(E_0)/k_B} \\, e^{-E_r / (k_B T)} = \\text{const} \\times e^{-\\beta E_r}$$\nNormalizing $\\sum_r P_r = 1$, we obtain the **Boltzmann Canonical Distribution**:\n$$P_r = \\frac{e^{-\\beta E_r}}{Z}$$\nwhere $\\beta = \\frac{1}{k_B T}$, and $Z$ is the **Canonical Partition Function** (German: *Zustandssumme* - sum over states):\n$$Z(T, V, N) = \\sum_r e^{-\\beta E_r}$$\n\n<h4>2. Connection with Helmholtz Free Energy ($F$)</h4>\nThe ensemble average energy is:\n$$\\langle E \\rangle = U = \\sum_r P_r E_r = \\frac{1}{Z} \\sum_r E_r e^{-\\beta E_r} = -\\frac{\\partial \\ln Z}{\\partial \\beta}$$\nGibbs defined the statistical entropy as:\n$$S = -k_B \\sum_r P_r \\ln P_r = -k_B \\sum_r P_r (-\\beta E_r - \\ln Z) = k_B \\beta \\langle E \\rangle + k_B \\ln Z = \\frac{U}{T} + k_B \\ln Z$$\nRearranging gives $U - TS = -k_B T \\ln Z$.\nRecalling the definition of Helmholtz Free Energy $F = U - TS$, we obtain the fundamental bridge:\n$$F(T, V, N) = -k_B T \\ln Z(T, V, N)$$\n\n<h4>3. Complete Thermodynamic Equations of State</h4>\nFrom the differential $dF = -S dT - P dV + \\mu dN$, all thermodynamic variables are computed by simple differentiation of $\\ln Z$:\n$$S = -\\left(\\frac{\\partial F}{\\partial T}\\right)_{V, N} = k_B \\ln Z + k_B T \\left(\\frac{\\partial \\ln Z}{\\partial T}\\right)_{V, N}$$\n$$P = -\\left(\\frac{\\partial F}{\\partial V}\\right)_{T, N} = k_B T \\left(\\frac{\\partial \\ln Z}{\\partial V}\\right)_{T, N}$$\n$$\\mu = \\left(\\frac{\\partial F}{\\partial N}\\right)_{T, V} = -k_B T \\left(\\frac{\\partial \\ln Z}{\\partial N}\\right)_{T, V}$$\n$$C_V = \\left(\\frac{\\partial U}{\\partial T}\\right)_V = k_B \\beta^2 \\frac{\\partial^2 \\ln Z}{\\partial \\beta^2}$$"
        },
        {
          "id": "sec-2-4",
          "number": "\u00a72.4",
          "heading": "The Grand Canonical Ensemble",
          "simulation": "canonical-boltzmann-sim",
          "content": "The **Grand Canonical Ensemble** describes an open system that can exchange both thermal energy and particles with a large reservoir at fixed temperature $T$ and chemical potential $\\mu$.\n\n<h4>1. Grand Canonical Probability Distribution</h4>\nLet the system $A$ have state $r$ with energy $E_r$ and particle number $N$. The combined system $A_0 = A + R$ is isolated with total energy $E_0 = E_r + E_R$ and total particles $N_0 = N + N_R$.\nExpanding the reservoir entropy $S_R(E_0 - E_r, N_0 - N)$:\n$$S_R \\approx S_R(E_0, N_0) - E_r \\left(\\frac{\\partial S_R}{\\partial E_R}\\right) - N \\left(\\frac{\\partial S_R}{\\partial N_R}\\right) = S_R(E_0, N_0) - \\frac{E_r}{T} + \\frac{\\mu N}{T}$$\nThe grand canonical probability distribution is:\n$$P_{r, N} = \\frac{e^{-\\beta (E_r - \\mu N)}}{\\Xi}$$\nwhere $\\Xi(T, V, \\mu)$ is the **Grand Canonical Partition Function**:\n$$\\Xi(T, V, \\mu) = \\sum_{N=0}^\\infty \\sum_r e^{-\\beta (E_r - \\mu N)} = \\sum_{N=0}^\\infty z^N Z_N(T, V)$$\nHere, $z \\equiv e^{\\beta \\mu} = e^{\\mu / k_B T}$ is called the **fugacity** (absolute activity).\n\n<h4>2. Connection with the Grand Potential ($\\Phi_G$)</h4>\nThe thermodynamic characteristic potential for open systems is the **Grand Potential** $\\Phi_G$ (also denoted $\\Omega$):\n$$\\Phi_G = F - \\mu N = U - TS - \\mu N = -P V$$\nIts statistical connection is:\n$$\\Phi_G(T, V, \\mu) = -k_B T \\ln \\Xi(T, V, \\mu) = -P V$$\nThis remarkable relation directly gives the equation of state:\n$$P(T, \\mu) = \\frac{k_B T}{V} \\ln \\Xi$$\nThe mean particle number and its fluctuations are:\n$$\\langle N \\rangle = k_B T \\left(\\frac{\\partial \\ln \\Xi}{\\partial \\mu}\\right)_{T, V}$$\n$$\\sigma_N^2 = \\langle N^2 \\rangle - \\langle N \\rangle^2 = (k_B T)^2 \\frac{\\partial^2 \\ln \\Xi}{\\partial \\mu^2} = k_B T \\left(\\frac{\\partial \\langle N \\rangle}{\\partial \\mu}\\right)_{T, V}$$"
        },
        {
          "id": "sec-2-5",
          "number": "\u00a72.5",
          "heading": "Thermodynamic Functions, Potentials, and Equilibrium Conditions",
          "simulation": "canonical-boltzmann-sim",
          "content": "Thermodynamics uses Legendre transformations to define four fundamental thermodynamic potentials, each corresponding to different experimental constraints.\n\n<h4>1. The Four Fundamental Thermodynamic Potentials</h4>\n<table style=\"width:100%; border-collapse:collapse; margin:1rem 0;\">\n  <tr style=\"border-bottom:1px solid #334155;\">\n    <th style=\"text-align:left; padding:6px;\">Potential</th>\n    <th style=\"text-align:left; padding:6px;\">Definition</th>\n    <th style=\"text-align:left; padding:6px;\">Differential Form</th>\n    <th style=\"text-align:left; padding:6px;\">Natural Variables</th>\n  </tr>\n  <tr>\n    <td style=\"padding:6px;\"><strong>Internal Energy $U$</strong></td>\n    <td style=\"padding:6px;\">$U$</td>\n    <td style=\"padding:6px;\">$dU = T dS - P dV + \\mu dN$</td>\n    <td style=\"padding:6px;\">$(S, V, N)$</td>\n  </tr>\n  <tr>\n    <td style=\"padding:6px;\"><strong>Helmholtz Free Energy $F$</strong></td>\n    <td style=\"padding:6px;\">$F = U - TS$</td>\n    <td style=\"padding:6px;\">$dF = -S dT - P dV + \\mu dN$</td>\n    <td style=\"padding:6px;\">$(T, V, N)$</td>\n  </tr>\n  <tr>\n    <td style=\"padding:6px;\"><strong>Enthalpy $H$</strong></td>\n    <td style=\"padding:6px;\">$H = U + PV$</td>\n    <td style=\"padding:6px;\">$dH = T dS + V dP + \\mu dN$</td>\n    <td style=\"padding:6px;\">$(S, P, N)$</td>\n  </tr>\n  <tr>\n    <td style=\"padding:6px;\"><strong>Gibbs Free Energy $G$</strong></td>\n    <td style=\"padding:6px;\">$G = U - TS + PV$</td>\n    <td style=\"padding:6px;\">$dG = -S dT + V dP + \\mu dN$</td>\n    <td style=\"padding:6px;\">$(T, P, N)$</td>\n  </tr>\n</table>\n\n<h4>2. Maxwell Relations</h4>\nBecause mixed second partial derivatives of state functions are invariant under order of differentiation, we derive the four fundamental **Maxwell Relations**:\n$$\\left(\\frac{\\partial T}{\\partial V}\\right)_S = -\\left(\\frac{\\partial P}{\\partial S}\\right)_V, \\quad \\left(\\frac{\\partial S}{\\partial V}\\right)_T = \\left(\\frac{\\partial P}{\\partial T}\\right)_V$$\n$$\\left(\\frac{\\partial T}{\\partial P}\\right)_S = \\left(\\frac{\\partial V}{\\partial S}\\right)_P, \\quad \\left(\\frac{\\partial S}{\\partial P}\\right)_T = -\\left(\\frac{\\partial V}{\\partial T}\\right)_P$$\n\n<h4>3. Equilibrium Conditions</h4>\nA system undergoing spontaneous evolution at constant:\n<ul>\n  <li>$(E, V)$: Maximizes entropy $S$ ($dS \\ge 0$, maximum at equilibrium).</li>\n  <li>$(T, V)$: Minimizes Helmholtz free energy $F$ ($dF \\le 0$, minimum at equilibrium).</li>\n  <li>$(T, P)$: Minimizes Gibbs free energy $G$ ($dG \\le 0$, minimum at equilibrium).</li>\n</ul>"
        },
        {
          "id": "sec-2-6",
          "number": "\u00a72.6",
          "heading": "Statistical Distribution Functions and Energy Fluctuations",
          "simulation": "canonical-boltzmann-sim",
          "content": "Why does the canonical ensemble (where energy fluctuates) yield identical thermodynamic results to the microcanonical ensemble (where energy is strictly fixed)?\n\n<h4>1. Energy Fluctuations in the Canonical Ensemble</h4>\nIn the canonical ensemble, the average energy is:\n$$\\langle E \\rangle = -\\frac{\\partial \\ln Z}{\\partial \\beta} = \\frac{1}{Z} \\sum_r E_r e^{-\\beta E_r}$$\nDifferentiating $\\langle E \\rangle$ with respect to $\\beta$:\n$$\\frac{\\partial \\langle E \\rangle}{\\partial \\beta} = \\frac{\\partial}{\\partial \\beta} \\left( \\frac{1}{Z} \\sum_r E_r e^{-\\beta E_r} \\right) = -\\frac{1}{Z^2} \\left(\\frac{\\partial Z}{\\partial \\beta}\\right) \\sum_r E_r e^{-\\beta E_r} - \\frac{1}{Z} \\sum_r E_r^2 e^{-\\beta E_r}$$\n$$\\frac{\\partial \\langle E \\rangle}{\\partial \\beta} = \\langle E \\rangle^2 - \\langle E^2 \\rangle = -(\\langle E^2 \\rangle - \\langle E \\rangle^2) = -\\sigma_E^2$$\nTherefore, the variance of energy is:\n$$\\sigma_E^2 = -\\frac{\\partial U}{\\partial \\beta} = -\\frac{\\partial U}{\\partial T} \\frac{\\partial T}{\\partial \\beta} = C_V k_B T^2$$\n\n<h4>2. Relative Energy Fluctuations in the Thermodynamic Limit</h4>\nFor a macroscopic system of $N$ particles:\n$$U \\propto N, \\quad C_V = \\left(\\frac{\\partial U}{\\partial T}\\right)_V \\propto N$$\nTherefore, the root-mean-square energy fluctuation is:\n$$\\sigma_E = \\sqrt{k_B T^2 C_V} \\propto \\sqrt{N}$$\nThe relative energy fluctuation is:\n$$\\frac{\\sigma_E}{\\langle E \\rangle} = \\frac{\\sqrt{k_B T^2 C_V}}{U} \\propto \\frac{\\sqrt{N}}{N} = \\frac{1}{\\sqrt{N}}$$\nFor $N = 10^{24}$:\n$$\\frac{\\sigma_E}{\\langle E \\rangle} \\approx \\frac{1}{\\sqrt{10^{24}}} = 10^{-12}$$\nEnergy fluctuations in the canonical ensemble are so vanishingly tiny that canonical and microcanonical ensembles are strictly mathematically equivalent in the thermodynamic limit ($N \\to \\infty$)."
        },
        {
          "id": "sec-2-7",
          "number": "\u00a72.7",
          "heading": "The Boltzmann Partition Function for Independent Particles",
          "simulation": "canonical-boltzmann-sim",
          "content": "For systems composed of non-interacting, independent particles, the total Hamiltonian is the sum of single-particle Hamiltonians:\n$$H(\\mathbf{X}) = \\sum_{i=1}^N h_i(\\mathbf{x}_i)$$\n\n<h4>1. Distinguishable Particles (Localized Lattice Sites)</h4>\nIf particles are distinguishable (such as atoms fixed at crystal lattice sites), each particle microstate is independent:\n$$Z_N = \\sum_{r_1, r_2, \\dots, r_N} e^{-\\beta (\\epsilon_{r_1} + \\epsilon_{r_2} + \\dots + \\epsilon_{r_N})} = \\left( \\sum_{r_1} e^{-\\beta \\epsilon_{r_1}} \\right) \\left( \\sum_{r_2} e^{-\\beta \\epsilon_{r_2}} \\right) \\dots \\left( \\sum_{r_N} e^{-\\beta \\epsilon_{r_N}} \\right)$$\n$$Z_N = [z_1(T, V)]^N$$\nwhere $z_1 = \\sum_j e^{-\\beta \\epsilon_j}$ is the **single-particle partition function**.\n\n<h4>2. Indistinguishable Particles and Gibbs' Correction Factor ($1/N!$)</h4>\nIn a gas of identical atoms, particles are fundamentally indistinguishable. Permuting any two particles does not create a new physical state.\nIf we used $Z_N = z_1^N$, we would overcount states by $N!$, leading to **Gibbs' Paradox** (entropy not being extensive: mixing two samples of the same gas would erroneously yield an entropy increase).\nGibbs introduced the correct quantum statistical count:\n$$Z_N = \\frac{[z_1(T, V)]^N}{N!}$$\nUsing Stirling's approximation $\\ln(N!) \\approx N \\ln N - N$:\n$$\\ln Z_N = N \\ln z_1 - N \\ln N + N = N \\ln\\left(\\frac{z_1}{N}\\right) + N$$\n\n<h4>3. Factorization of Molecular Degrees of Freedom</h4>\nFor a gas of independent polyatomic molecules, the single-particle Hamiltonian decouples:\n$$h_i = h_{\\text{trans}} + h_{\\text{rot}} + h_{\\text{vib}} + h_{\\text{elec}} + h_{\\text{nucl}}$$\nThe single-particle partition function factorizes into a product:\n$$z_1 = z_{\\text{trans}} \\times z_{\\text{rot}} \\times z_{\\text{vib}} \\times z_{\\text{elec}} \\times z_{\\text{nucl}}$$\nEach degree of freedom contributes additively to free energy and heat capacity."
        },
        {
          "id": "sec-2-8",
          "number": "\u00a72.8",
          "heading": "Maxwell-Boltzmann Velocity Distribution and Mean Values",
          "simulation": "canonical-boltzmann-sim",
          "content": "Maxwell (1859) and Boltzmann (1871) derived the fundamental distribution of molecular speeds in an ideal thermal gas.\n\n<h4>1. 3D Velocity Distribution</h4>\nFor a classical particle of mass $m$, the kinetic energy is $\\epsilon = \\frac{1}{2}m(v_x^2 + v_y^2 + v_z^2)$. The probability of finding a molecule with velocity in range $[\\mathbf{v}, \\mathbf{v} + d^3\\mathbf{v}]$ is:\n$$f(v_x, v_y, v_z) \\, dv_x dv_y dv_z = C \\exp\\left( -\\frac{m(v_x^2 + v_y^2 + v_z^2)}{2 k_B T} \\right) dv_x dv_y dv_z$$\nNormalizing via standard Gaussian integrals $\\int_{-\\infty}^\\infty e^{-\\alpha v_x^2} dv_x = \\sqrt{\\frac{\\pi}{\\alpha}}$ with $\\alpha = \\frac{m}{2 k_B T}$:\n$$f(\\mathbf{v}) = \\left(\\frac{m}{2\\pi k_B T}\\right)^{3/2} \\exp\\left( -\\frac{m v^2}{2 k_B T} \\right)$$\n\n<h4>2. Maxwell Speed Distribution</h4>\nTransforming to spherical velocity coordinates $(v, \\theta, \\phi)$ where $d^3\\mathbf{v} = v^2 \\sin\\theta \\, dv \\, d\\theta \\, d\\phi$, and integrating over angles $\\int_0^{2\\pi} d\\phi \\int_0^\\pi \\sin\\theta d\\theta = 4\\pi$:\n$$F(v) \\, dv = 4\\pi \\left(\\frac{m}{2\\pi k_B T}\\right)^{3/2} v^2 \\exp\\left( -\\frac{m v^2}{2 k_B T} \\right) dv$$\n\n<h4>3. Analytical Derivation of Characteristic Molecular Speeds</h4>\n<ul>\n  <li><strong>Most Probable Speed ($v_p$):</strong> Found by maximizing $F(v)$:\n  $$\\frac{dF(v)}{dv} = 0 \\implies \\frac{d}{dv}\\left( v^2 e^{-\\alpha v^2} \\right) = (2v - 2\\alpha v^3)e^{-\\alpha v^2} = 0 \\implies v_p = \\frac{1}{\\sqrt{\\alpha}} = \\sqrt{\\frac{2 k_B T}{m}}$$\n  </li>\n  <li><strong>Average (Mean) Speed ($\\langle v \\rangle$):</strong>\n  $$\\langle v \\rangle = \\int_0^\\infty v F(v) \\, dv = 4\\pi \\left(\\frac{m}{2\\pi k_B T}\\right)^{3/2} \\int_0^\\infty v^3 e^{-\\frac{m v^2}{2 k_B T}} \\, dv = \\sqrt{\\frac{8 k_B T}{\\pi m}}$$\n  </li>\n  <li><strong>Root-Mean-Square (RMS) Speed ($v_{\\text{rms}}$):</strong>\n  $$\\langle v^2 \\rangle = \\int_0^\\infty v^2 F(v) \\, dv = \\frac{3 k_B T}{m} \\implies v_{\\text{rms}} = \\sqrt{\\langle v^2 \\rangle} = \\sqrt{\\frac{3 k_B T}{m}}$$\n  </li>\n</ul>\nNotice the invariant universal ratio:\n$$v_p : \\langle v \\rangle : v_{\\text{rms}} = \\sqrt{2} : \\sqrt{\\frac{8}{\\pi}} : \\sqrt{3} \\approx 1.414 : 1.596 : 1.732$$\nThe most probable speed is always less than the average, which is always less than the RMS speed."
        },
        {
          "id": "sec-2-9",
          "number": "\u00a72.9",
          "heading": "The Ideal Monatomic Gas and the Sackur-Tetrode Equation",
          "simulation": "canonical-boltzmann-sim",
          "content": "We now derive the complete thermodynamic properties of an ideal monatomic gas from microscopic first principles.\n\n<h4>1. Translational Partition Function ($z_{\\text{trans}}$)</h4>\nFor a single particle confined in volume $V$:\n$$z_{\\text{trans}} = \\frac{1}{h^3} \\int_V d^3\\mathbf{r} \\int_{-\\infty}^\\infty d^3\\mathbf{p} \\, e^{-\\beta p^2 / (2m)} = \\frac{V}{h^3} \\left( \\int_{-\\infty}^\\infty e^{-\\beta p_x^2 / 2m} dp_x \\right)^3 = \\frac{V}{h^3} (2\\pi m k_B T)^{3/2}$$\nWe define the **thermal de Broglie wavelength** $\\lambda_{\\text{th}}$:\n$$\\lambda_{\\text{th}} \\equiv \\frac{h}{\\sqrt{2\\pi m k_B T}}$$\nThus:\n$$z_{\\text{trans}} = \\frac{V}{\\lambda_{\\text{th}}^3}$$\n\n<h4>2. $N$-Particle Partition Function and Helmholtz Free Energy</h4>\nApplying Gibbs' indistinguishability factor $1/N!$:\n$$Z_N = \\frac{z_{\\text{trans}}^N}{N!} = \\frac{1}{N!} \\left( \\frac{V}{\\lambda_{\\text{th}}^3} \\right)^N$$\n$$F = -k_B T \\ln Z_N = -N k_B T \\left[ \\ln\\left( \\frac{V}{N \\lambda_{\\text{th}}^3} \\right) + 1 \\right]$$\n\n<h4>3. Derivation of the Ideal Gas Law and Internal Energy</h4>\nPressure is obtained by volume differentiation:\n$$P = -\\left(\\frac{\\partial F}{\\partial V}\\right)_{T, N} = N k_B T \\frac{\\partial}{\\partial V}\\ln V = \\frac{N k_B T}{V} \\implies P V = N k_B T$$\nThe Ideal Gas Equation of State is derived microscopically!\nThe internal energy is:\n$$U = -\\frac{\\partial \\ln Z_N}{\\partial \\beta} = N \\left( -\\frac{\\partial}{\\partial \\beta}\\ln\\beta^{-3/2} \\right) = \\frac{3}{2} N k_B T$$\nThe heat capacity at constant volume is:\n$$C_V = \\left(\\frac{\\partial U}{\\partial T}\\right)_V = \\frac{3}{2} N k_B = \\frac{3}{2} n R$$\n\n<h4>4. The Sackur-Tetrode Equation for Entropy</h4>\nUsing $S = -\\left(\\frac{\\partial F}{\\partial T}\\right)_{V, N}$:\n$$S = N k_B \\left[ \\ln\\left( \\frac{V}{N \\lambda_{\\text{th}}^3} \\right) + \\frac{5}{2} \\right] = N k_B \\left[ \\ln\\left( \\frac{V}{N} \\left(\\frac{2\\pi m k_B T}{h^2}\\right)^{3/2} \\right) + \\frac{5}{2} \\right]$$\nThis is the renowned **Sackur-Tetrode Equation** (1912). It provides the absolute entropy of an ideal gas and explicitly contains Planck's constant $h$, proving that classical thermodynamics requires quantum mechanics for complete consistency!"
        },
        {
          "id": "sec-2-10",
          "number": "\u00a72.10",
          "heading": "The Classical and Quantum Harmonic Oscillator",
          "simulation": "equipartition-dof-sim",
          "content": "The harmonic oscillator is the foundation for modeling vibrational states of molecules and lattice vibrations in solids.\n\n<h4>1. The Classical Harmonic Oscillator</h4>\nFor a 1D classical oscillator with Hamiltonian $H = \\frac{p^2}{2m} + \\frac{1}{2}m\\omega^2 q^2$:\n$$z_{\\text{class}} = \\frac{1}{h} \\int_{-\\infty}^\\infty dq \\int_{-\\infty}^\\infty dp \\, e^{-\\beta \\left(\\frac{p^2}{2m} + \\frac{1}{2}m\\omega^2 q^2\\right)}$$\nUsing Gaussian integrals $\\int e^{-\\alpha u^2} du = \\sqrt{\\pi / \\alpha}$:\n$$z_{\\text{class}} = \\frac{1}{h} \\sqrt{\\frac{2\\pi m}{\\beta}} \\sqrt{\\frac{2\\pi}{m\\omega^2 \\beta}} = \\frac{2\\pi}{\\beta \\omega h} = \\frac{k_B T}{\\hbar \\omega}$$\nThe average energy is:\n$$\\langle E \\rangle_{\\text{class}} = -\\frac{\\partial \\ln z_{\\text{class}}}{\\partial \\beta} = \\frac{1}{\\beta} = k_B T$$\nEach degree of freedom (kinetic and potential) contributes $\\frac{1}{2}k_B T$, giving $k_B T$ total.\n\n<h4>2. The Quantum Harmonic Oscillator</h4>\nIn quantum mechanics, energy levels are quantized:\n$$E_n = \\left(n + \\frac{1}{2}\\right)\\hbar \\omega, \\quad n = 0, 1, 2, \\dots$$\nThe quantum partition function is a geometric series:\n$$z_{\\text{quant}} = \\sum_{n=0}^\\infty e^{-\\beta \\hbar \\omega (n + 1/2)} = e^{-\\beta \\hbar \\omega / 2} \\sum_{n=0}^\\infty \\left(e^{-\\beta \\hbar \\omega}\\right)^n = \\frac{e^{-\\beta \\hbar \\omega / 2}}{1 - e^{-\\beta \\hbar \\omega}} = \\frac{1}{2 \\sinh(\\beta \\hbar \\omega / 2)}$$\nThe average energy is:\n$$\\langle E \\rangle_{\\text{quant}} = -\\frac{\\partial \\ln z_{\\text{quant}}}{\\partial \\beta} = \\frac{1}{2}\\hbar \\omega + \\frac{\\hbar \\omega}{e^{\\beta \\hbar \\omega} - 1}$$\nHere $\\frac{1}{2}\\hbar \\omega$ is the **Zero-Point Energy**, and $\\frac{1}{e^{\\beta \\hbar \\omega} - 1}$ is the Planck-Bose distribution of thermal oscillator quanta (phonons).\n\n<h4>3. High- and Low-Temperature Limits</h4>\n<ul>\n  <li><strong>High Temperature ($k_B T \\gg \\hbar \\omega$):</strong> Expanding $e^{\\beta \\hbar \\omega} - 1 \\approx \\beta \\hbar \\omega$:\n  $$\\langle E \\rangle \\approx \\frac{1}{2}\\hbar \\omega + \\frac{\\hbar \\omega}{\\beta \\hbar \\omega} = k_B T + \\frac{1}{2}\\hbar \\omega \\to k_B T$$\n  The quantum result recovers the classical equipartition theorem!</li>\n  <li><strong>Low Temperature ($k_B T \\ll \\hbar \\omega$):</strong> As $T \\to 0$, $e^{\\beta \\hbar \\omega} \\to \\infty$:\n  $$\\langle E \\rangle \\to \\frac{1}{2}\\hbar \\omega$$\n  Thermal excitations vanish; the oscillator is frozen into its quantum ground state.</li>\n</ul>"
        },
        {
          "id": "sec-2-11",
          "number": "\u00a72.11",
          "heading": "Specific Heat of Solids and the Classical Limit",
          "simulation": "equipartition-dof-sim",
          "content": "The specific heat of crystalline solids provided the first historical proof of the breakdown of classical statistical mechanics and the necessity of quantum physics.\n\n<h4>1. The Classical Dulong-Petit Law (1819)</h4>\nIn a 3D crystalline solid containing $N$ atoms, each atom oscillates around its equilibrium lattice site in three dimensions.\nThe system can be modeled as $3N$ independent 1D harmonic oscillators.\nAccording to the classical equipartition theorem, each harmonic oscillator has two quadratic energy terms (kinetic $\\frac{p^2}{2m}$ and potential $\\frac{1}{2}m\\omega^2 q^2$), each contributing $\\frac{1}{2}k_B T$:\n$$U = 3N \\times k_B T = 3 N k_B T$$\nThe heat capacity at constant volume is:\n$$C_V = \\left(\\frac{\\partial U}{\\partial T}\\right)_V = 3 N k_B$$\nFor one mole of atoms ($N = N_A$):\n$$C_V = 3 N_A k_B = 3 R \\approx 3 \\times 8.314\\text{ J/(mol}\\cdot\\text{K)} = 24.94\\text{ J/(mol}\\cdot\\text{K)}$$\nThis is the empirical **Dulong-Petit Law**.\n\n<h4>2. The Classical Breakdown at Low Temperatures</h4>\nExperimentally, while the Dulong-Petit law holds well at room temperature for heavy metals (lead, copper), it fails completely for light, stiff solids like diamond at room temperature, and **fails for all solids as $T \\to 0$**.\nExperimentally:\n$$\\lim_{T \\to 0} C_V(T) = 0$$\nClassical mechanics predicts a strictly constant $C_V = 3R$ down to absolute zero, in direct violation of the Third Law of Thermodynamics (Nernst Heat Theorem).\nThe resolution of this crisis was achieved by Albert Einstein (1907) and Peter Debye (1912) by applying quantum quantization to lattice vibrations."
        }
      ],
      "problems": [
        {
          "id": "prob-2-1",
          "difficulty": "Medium",
          "title": "Equipartition Theorem and Heat Capacity of a Diatomic Gas",
          "question": "A container contains $N$ molecules of a rigid diatomic gas (e.g., $N_2$ at room temperature). Each molecule has 3 translational degrees of freedom and 2 rotational degrees of freedom, while vibrational modes are frozen ($k_B T \\ll \\hbar \\omega_{\\text{vib}}$). (a) Use the classical equipartition theorem to calculate the total internal energy $U$ and molar heat capacities $C_V$ and $C_P$. (b) Determine the adiabatic index $\\gamma = C_P / C_V$.",
          "steps": [
            {
              "title": "Step 1: Count quadratic degrees of freedom",
              "math": "$$f = f_{\\text{trans}} + f_{\\text{rot}} = 3 + 2 = 5$$",
              "explanation": "Because the molecule is linear, rotation about the internuclear axis has negligible moment of inertia, leaving exactly 2 active rotational degrees of freedom."
            },
            {
              "title": "Step 2: Apply the equipartition theorem for internal energy",
              "math": "$$U = N \\times \\frac{f}{2} k_B T = \\frac{5}{2} N k_B T = \\frac{5}{2} n R T$$",
              "explanation": "Each quadratic degree of freedom contributes $\\frac{1}{2}k_B T$ to the internal energy."
            },
            {
              "title": "Step 3: Calculate heat capacities and adiabatic index",
              "math": "$$C_V = \\left(\\frac{\\partial U}{\\partial T}\\right)_V = \\frac{5}{2} n R \\implies c_V = \\frac{5}{2} R \\approx 20.79\\text{ J/(mol}\\cdot\\text{K)}$$\n$$C_P = C_V + n R = \\frac{7}{2} n R \\implies c_P = \\frac{7}{2} R \\approx 29.10\\text{ J/(mol}\\cdot\\text{K)}$$\n$$\\gamma = \\frac{C_P}{C_V} = \\frac{7/2 R}{5/2 R} = \\frac{7}{5} = 1.40$$",
              "explanation": "This precisely matches the experimental adiabatic index of air and diatomic nitrogen ($\\gamma = 1.40$)."
            }
          ]
        },
        {
          "id": "prob-2-2",
          "difficulty": "Hard",
          "title": "Sackur-Tetrode Entropy Calculation for Argon Gas",
          "question": "One mole ($N_A = 6.022 \\times 10^{23}$) of argon gas (atomic mass $M = 39.95\\text{ g/mol}$) is at standard temperature and pressure ($T = 298.15\\text{ K}, P = 1.013 \\times 10^5\\text{ Pa}$). Using the Sackur-Tetrode equation, calculate the absolute molar entropy $S$ from fundamental quantum constants and compare with the experimental value ($154.8\\text{ J/(mol}\\cdot\\text{K)}$).",
          "steps": [
            {
              "title": "Step 1: Compute particle mass and volume per particle",
              "math": "$$m = \\frac{M}{N_A} = \\frac{0.03995\\text{ kg/mol}}{6.022 \\times 10^{23}\\text{ mol}^{-1}} = 6.634 \\times 10^{-26}\\text{ kg}$$\n$$V = \\frac{n R T}{P} = \\frac{(1)(8.314)(298.15)}{1.013 \\times 10^5} = 0.02447\\text{ m}^3$$\n$$\\frac{V}{N} = \\frac{0.02447}{6.022 \\times 10^{23}} = 4.063 \\times 10^{-26}\\text{ m}^3$$",
              "explanation": "This establishes the average volume available to a single argon atom in the gas phase."
            },
            {
              "title": "Step 2: Calculate the thermal de Broglie wavelength",
              "math": "$$\\lambda_{\\text{th}} = \\frac{h}{\\sqrt{2\\pi m k_B T}} = \\frac{6.626 \\times 10^{-34}}{\\sqrt{2\\pi (6.634 \\times 10^{-26})(1.381 \\times 10^{-23})(298.15)}} = 1.601 \\times 10^{-11}\\text{ m} = 0.1601\\text{ \u00c5}$$\n$$\\lambda_{\\text{th}}^3 = (1.601 \\times 10^{-11})^3 = 4.103 \\times 10^{-33}\\text{ m}^3$$",
              "explanation": "Because $\\lambda_{\\text{th}} \\ll (V/N)^{1/3} \\approx 34\\text{ \u00c5}$, quantum wavepackets do not overlap, confirming the validity of classical Maxwell-Boltzmann statistics."
            },
            {
              "title": "Step 3: Evaluate the Sackur-Tetrode formula",
              "math": "$$\\frac{V}{N \\lambda_{\\text{th}}^3} = \\frac{4.063 \\times 10^{-26}}{4.103 \\times 10^{-33}} = 9.902 \\times 10^6$$\n$$\\ln\\left(\\frac{V}{N \\lambda_{\\text{th}}^3}\\right) = \\ln(9.902 \\times 10^6) = 16.108$$\n$$S = N_A k_B \\left[ 16.108 + 2.5 \\right] = R [18.608] = 8.314 \\times 18.608 = 154.71\\text{ J/(mol}\\cdot\\text{K)}$$",
              "explanation": "The derived theoretical entropy ($154.71\\text{ J/(mol}\\cdot\\text{K)}$) matches the experimental calorimeter measurement ($154.8\\text{ J/(mol}\\cdot\\text{K)}$) to within $0.06\\%$, demonstrating the predictive power of statistical thermodynamics."
            }
          ]
        },
        {
          "id": "prob-2-3",
          "difficulty": "Hard",
          "title": "Einstein Model of Heat Capacity of a Solid",
          "question": "In the Einstein model of a solid, $N$ atoms are treated as $3N$ independent quantum harmonic oscillators with identical frequency $\\omega_E$. (a) Derive the Einstein expression for heat capacity $C_V(T)$. (b) Define the Einstein temperature $\\Theta_E = \\hbar \\omega_E / k_B$ and show that $C_V$ vanishes exponentially as $T \\to 0$.",
          "steps": [
            {
              "title": "Step 1: Write down total energy for 3N quantum oscillators",
              "math": "$$U = 3N \\langle \\epsilon \\rangle = 3N \\left( \\frac{1}{2}\\hbar \\omega_E + \\frac{\\hbar \\omega_E}{e^{\\hbar \\omega_E / k_B T} - 1} \\right) = \\frac{3}{2}N \\hbar \\omega_E + \\frac{3N k_B \\Theta_E}{e^{\\Theta_E / T} - 1}$$",
              "explanation": "Here $\\Theta_E \\equiv \\frac{\\hbar \\omega_E}{k_B}$ is the characteristic Einstein temperature of the solid."
            },
            {
              "title": "Step 2: Differentiate with respect to temperature to find C_V",
              "math": "$$C_V = \\frac{\\partial U}{\\partial T} = 3N k_B \\Theta_E \\left( -\\frac{1}{(e^{\\Theta_E / T} - 1)^2} \\right) e^{\\Theta_E / T} \\left( -\\frac{\\Theta_E}{T^2} \\right)$$\n$$C_V(T) = 3 N k_B \\left(\\frac{\\Theta_E}{T}\\right)^2 \\frac{e^{\\Theta_E / T}}{(e^{\\Theta_E / T} - 1)^2}$$",
              "explanation": "This is the famous Einstein Heat Capacity formula."
            },
            {
              "title": "Step 3: Analyze the low-temperature limit (T << \\Theta_E)",
              "math": "$$\\text{As } T \\to 0, \\quad e^{\\Theta_E / T} \\gg 1 \\implies e^{\\Theta_E / T} - 1 \\approx e^{\\Theta_E / T}$$\n$$C_V(T) \\approx 3 N k_B \\left(\\frac{\\Theta_E}{T}\\right)^2 \\frac{e^{\\Theta_E / T}}{e^{2\\Theta_E / T}} = 3 N k_B \\left(\\frac{\\Theta_E}{T}\\right)^2 e^{-\\Theta_E / T} \\xrightarrow{T \\to 0} 0$$",
              "explanation": "Because $e^{-\\Theta_E/T}$ drops to zero faster than any power of $T$, the specific heat freezes to zero, explaining the observed failure of the classical Dulong-Petit law."
            }
          ]
        }
      ]
    },
    {
      "number": 3,
      "title": "Quantum Statistical Mechanics",
      "leadSummary": "Postulates of quantum statistics, indistinguishability, spin-statistics connection, exchange degeneracy, the density matrix operator, von Neumann equation, and unified quantum ensembles.",
      "sections": [
        {
          "id": "sec-3-1",
          "number": "\u00a73.1",
          "heading": "Postulates of Quantum Statistical Mechanics",
          "simulation": "quantum-wavefunction-symmetry-sim",
          "content": "Classical statistical mechanics deals with phase-space points $(q_i, p_i)$. In the quantum realm, physical states are vectors in a complex Hilbert space, and physical observables are Hermitian operators.\n\n<h4>1. Pure States versus Mixed States</h4>\nA **pure state** is a system described by a single state vector $|\\Psi\\rangle$ with complete quantum coherence. The expectation value of an observable $\\hat{A}$ is $\\langle \\hat{A} \\rangle = \\langle \\Psi | \\hat{A} | \\Psi \\rangle$.\nA **mixed state** represents a statistical ensemble where the system has probability $p_n$ of being in state $|\\psi_n\\rangle$. There is two-fold uncertainty:\n<ol>\n  <li>Fundamental quantum indeterminacy (wavefunction collapse).</li>\n  <li>Classical statistical ignorance of which state the system occupies.</li>\n</ol>\n\n<h4>2. The Postulate of Equal A Priori Probabilities (Quantum Formulation)</h4>\nFor an isolated quantum system in thermodynamic equilibrium with energy in shell $[E, E + \\delta E]$, all accessible orthonormal eigenstates $|n\\rangle$ of the Hamiltonian $\\hat{H}$ are equally likely:\n$$p_n = \\begin{cases} \\frac{1}{\\Omega(E)} & \\text{if } E \\le E_n \\le E + \\delta E \\\\ 0 & \\text{otherwise} \\end{cases}$$\n\n<h4>3. The Postulate of Random Phases</h4>\nWhen expanding a general state in energy eigenstates $|\\Psi\\rangle = \\sum_n c_n e^{i\\theta_n} |n\\rangle$, the quantum phases $\\theta_n$ are completely uncorrelated and uniformly distributed over $[0, 2\\pi]$:\n$$\\overline{c_n^* c_m} = |c_n|^2 \\delta_{nm}$$\nAll off-diagonal interference terms vanish on statistical average. The density matrix is diagonal in the energy representation for any equilibrium system."
        },
        {
          "id": "sec-3-2",
          "number": "\u00a73.2",
          "heading": "Transition from Classical to Quantum Statistical Mechanics",
          "simulation": "three-statistics-comparison-sim",
          "content": "How does quantum statistical mechanics reproduce classical physics in the macroscopic limit?\n\n<h4>1. The Phase Cell Volume and Planck's Constant</h4>\nIn classical mechanics, the number of microstates in phase volume $\\Delta \\Gamma$ was computed with an arbitrary volume constant $h_0$: $\\Omega = \\Delta \\Gamma / h_0$.\nQuantum mechanics reveals that the elementary volume of a single quantum state in 6-dimensional single-particle phase space is precisely Planck's constant cubed:\n$$h_0 = h^3 = (6.626 \\times 10^{-34}\\text{ J}\\cdot\\text{s})^3$$\nFor an $N$-particle system:\n$$h_0^{(N)} = N! \\, h^{3N}$$\nwhere $N!$ accounts for quantum indistinguishability.\n\n<h4>2. The Quantum Degeneracy Criterion</h4>\nThe transition between classical and quantum regimes is governed by the ratio of the thermal de Broglie wavelength $\\lambda_{\\text{th}}$ to the average interparticle spacing $\\bar{r} = (V/N)^{1/3}$:\n$$\\lambda_{\\text{th}} = \\frac{h}{\\sqrt{2\\pi m k_B T}}$$\nWe define the dimensionless **quantum degeneracy parameter** $\\xi$:\n$$\\xi \\equiv n \\lambda_{\\text{th}}^3 = \\frac{N}{V} \\left( \\frac{h}{\\sqrt{2\\pi m k_B T}} \\right)^3$$\n<ul>\n  <li><strong>Classical Regime ($\\xi \\ll 1$):</strong> When $n \\lambda_{\\text{th}}^3 \\ll 1$ (high temperature, low density, large particle mass), individual particle wavepackets do not overlap. Quantum exchange effects vanish, and the system obeys classical Maxwell-Boltzmann statistics.</li>\n  <li><strong>Quantum Degenerate Regime ($\\xi \\gtrsim 1$):</strong> When $n \\lambda_{\\text{th}}^3 \\ge 1$ (low temperature, high density, light particles such as electrons in metals or helium at $2\\text{ K}$), wavepackets overlap substantially. Quantum symmetry dominates, requiring Fermi-Dirac or Bose-Einstein statistics.</li>\n</ul>"
        },
        {
          "id": "sec-3-3",
          "number": "\u00a73.3",
          "heading": "Particle Statistics: Principle of Indistinguishability",
          "simulation": "quantum-wavefunction-symmetry-sim",
          "content": "In classical physics, identical particles can always be distinguished by tracking their continuous trajectories. In quantum mechanics, the uncertainty principle makes tracing continuous trajectories impossible: identical particles are **fundamentally indistinguishable**.\n\n<h4>1. The Permutation Operator ($\\hat{P}_{12}$)</h4>\nConsider a system of two identical particles. Let $|\\Psi(1, 2)\\rangle = |\\Psi(\\mathbf{r}_1, \\sigma_1; \\mathbf{r}_2, \\sigma_2)\\rangle$ be the state vector, where $\\mathbf{r}_i$ is position and $\\sigma_i$ is spin.\nDefine the particle exchange (permutation) operator $\\hat{P}_{12}$:\n$$\\hat{P}_{12} |\\Psi(1, 2)\\rangle = |\\Psi(2, 1)\\rangle$$\nBecause the particles are identical, exchanging them cannot alter any physical observable. Thus, the Hamiltonian commutes with the permutation operator:\n$$[\\hat{H}, \\hat{P}_{12}] = 0$$\nFurthermore, applying $\\hat{P}_{12}$ twice returns the original state:\n$$\\hat{P}_{12}^2 = \\hat{I} \\implies \\text{eigenvalues of } \\hat{P}_{12} \\text{ are } \\lambda = \\pm 1$$\n\n<h4>2. Symmetric and Antisymmetric States</h4>\nEvery physical state of identical particles in nature belongs strictly to one of two one-dimensional representations:\n<ul>\n  <li><strong>Symmetric States ($\\lambda = +1$):</strong>\n  $$\\Psi(2, 1) = +\\Psi(1, 2)$$\n  </li>\n  <li><strong>Antisymmetric States ($\\lambda = -1$):</strong>\n  $$\\Psi(2, 1) = -\\Psi(1, 2)$$\n  </li>\n</ul>\nStates of mixed symmetry are never observed in the physical universe."
        },
        {
          "id": "sec-3-4",
          "number": "\u00a73.4",
          "heading": "The Spin-Statistics Connection and Pauli Exclusion Principle",
          "simulation": "quantum-wavefunction-symmetry-sim",
          "content": "The relationship between particle intrinsic spin and wavefunction symmetry is one of the deepest theorems in theoretical physics.\n\n<h4>1. The Spin-Statistics Theorem</h4>\nProved by Wolfgang Pauli (1940) within relativistic quantum field theory under the axioms of Lorentz invariance, microcausality, and positive-definite energy:\n<blockquote>\n<strong>Spin-Statistics Theorem:</strong>\n<ol>\n  <li>Particles possessing <strong>integer intrinsic spin</strong> ($s = 0, 1, 2, \\dots$) are <strong>BOSONS</strong>. Their many-body state vectors are strictly <em>symmetric</em> under particle exchange.</li>\n  <li>Particles possessing <strong>half-odd-integer intrinsic spin</strong> ($s = 1/2, 3/2, 5/2, \\dots$) are <strong>FERMIONS</strong>. Their many-body state vectors are strictly <em>antisymmetric</em> under particle exchange.</li>\n</ol>\n</blockquote>\n\nExamples:\n<ul>\n  <li><strong>Fermions:</strong> Electrons ($s=1/2$), protons ($s=1/2$), neutrons ($s=1/2$), quarks ($s=1/2$), $^3\\text{He}$ atoms.</li>\n  <li><strong>Bosons:</strong> Photons ($s=1$), gluons ($s=1$), $W^\\pm, Z^0$ bosons ($s=1$), Higgs boson ($s=0$), $^4\\text{He}$ atoms ($s=0$).</li>\n</ul>\n\n<h4>2. The Pauli Exclusion Principle</h4>\nFor a system of $N$ non-interacting identical fermions, the total antisymmetric wavefunction is given by the **Slater Determinant**:\n$$\\Psi(\\mathbf{x}_1, \\dots, \\mathbf{x}_N) = \\frac{1}{\\sqrt{N!}} \\begin{vmatrix} \\phi_1(\\mathbf{x}_1) & \\phi_1(\\mathbf{x}_2) & \\dots & \\phi_1(\\mathbf{x}_N) \\\\ \\phi_2(\\mathbf{x}_1) & \\phi_2(\\mathbf{x}_2) & \\dots & \\phi_2(\\mathbf{x}_N) \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ \\phi_N(\\mathbf{x}_1) & \\phi_N(\\mathbf{x}_2) & \\dots & \\phi_N(\\mathbf{x}_N) \\end{vmatrix}$$\nIf two fermions attempt to occupy the <em>identical single-particle quantum state</em> ($\\phi_i = \\phi_j$), two rows of the determinant become identical, so $\\Psi \\equiv 0$.\n<blockquote>\n<strong>Pauli Exclusion Principle:</strong> No two identical fermions can simultaneously occupy the same quantum state. The occupation number of any single-particle quantum state $i$ is strictly restricted to:\n$$n_i \\in \\{0, 1\\}$$\n</blockquote>\nFor bosons, no such restriction exists: $n_i \\in \\{0, 1, 2, 3, \\dots\\}$."
        },
        {
          "id": "sec-3-5",
          "number": "\u00a73.5",
          "heading": "Exchange Degeneracy and Spatial Correlations",
          "simulation": "quantum-wavefunction-symmetry-sim",
          "content": "Wavefunction symmetry introduces a purely quantum mechanical effective force between particles known as the **Exchange Interaction**.\n\n<h4>1. Two-Particle Spatial Wavefunction</h4>\nConsider two non-interacting identical particles in spatial states $\\phi_a(\\mathbf{r})$ and $\\phi_b(\\mathbf{r})$.\nThe properly symmetrized / antisymmetrized spatial wavefunctions are:\n$$\\psi_S(\\mathbf{r}_1, \\mathbf{r}_2) = \\frac{1}{\\sqrt{2}}\\left[ \\phi_a(\\mathbf{r}_1)\\phi_b(\\mathbf{r}_2) + \\phi_b(\\mathbf{r}_1)\\phi_a(\\mathbf{r}_2) \\right] \\quad (\\text{Bosons})$$\n$$\\psi_A(\\mathbf{r}_1, \\mathbf{r}_2) = \\frac{1}{\\sqrt{2}}\\left[ \\phi_a(\\mathbf{r}_1)\\phi_b(\\mathbf{r}_2) - \\phi_b(\\mathbf{r}_1)\\phi_a(\\mathbf{r}_2) \\right] \\quad (\\text{Fermions})$$\n\n<h4>2. Probability Density and Quantum Statistical Force</h4>\nThe probability density of finding particle 1 at $\\mathbf{r}_1$ and particle 2 at $\\mathbf{r}_2$ is:\n$$P_{\\pm}(\\mathbf{r}_1, \\mathbf{r}_2) = |\\psi_{\\pm}(\\mathbf{r}_1, \\mathbf{r}_2)|^2 = \\frac{1}{2}|\\phi_a(\\mathbf{r}_1)|^2 |\\phi_b(\\mathbf{r}_2)|^2 + \\frac{1}{2}|\\phi_b(\\mathbf{r}_1)|^2 |\\phi_a(\\mathbf{r}_2)|^2 \\pm \\operatorname{Re}[\\phi_a(\\mathbf{r}_1)\\phi_b^*(\\mathbf{r}_1) \\phi_b(\\mathbf{r}_2)\\phi_a^*(\\mathbf{r}_2)]$$\nNotice what happens as the two particles approach the same point in space ($\\mathbf{r}_1 \\to \\mathbf{r}_2 = \\mathbf{r}$):\n<ul>\n  <li><strong>For Fermions ($-$) with parallel spins:</strong>\n  $$P_A(\\mathbf{r}, \\mathbf{r}) = 0$$\n  Identical fermions avoid each other in space, creating an effective **Pauli Exclusion Hole**. This statistical repulsion stabilizes atoms, prevents white dwarf collapse, and explains the periodic table.</li>\n  <li><strong>For Bosons ($+$):</strong>\n  $$P_S(\\mathbf{r}, \\mathbf{r}) = 2 |\\phi_a(\\mathbf{r})|^2 |\\phi_b(\\mathbf{r})|^2 > P_{\\text{classical}}$$\n  Identical bosons tend to clump or bunch together in the same spatial quantum state. This statistical attraction drives **Bose-Einstein Condensation** and laser coherence!</li>\n</ul>"
        },
        {
          "id": "sec-3-6",
          "number": "\u00a73.6",
          "heading": "Average Values and the Density Matrix Formulation",
          "simulation": "density-matrix-pure-mixed-sim",
          "content": "The **density matrix** $\\hat{\\rho}$, introduced independently by John von Neumann and Lev Landau in 1927, is the central mathematical object of quantum statistical mechanics.\n\n<h4>1. Definition of the Density Operator</h4>\nFor a mixed state ensemble consisting of states $|\\psi_n\\rangle$ with statistical probabilities $p_n$ ($p_n \\ge 0, \\sum_n p_n = 1$), the density operator $\\hat{\\rho}$ is defined as:\n$$\\hat{\\rho} \\equiv \\sum_n p_n |\\psi_n\\rangle \\langle \\psi_n|$$\n\n<h4>2. Fundamental Properties of $\\hat{\\rho}$</h4>\n<ol>\n  <li><strong>Hermiticity:</strong> $\\hat{\\rho}^\\dagger = \\hat{\\rho}$.</li>\n  <li><strong>Unit Trace (Normalization):</strong> $\\operatorname{Tr}(\\hat{\\rho}) = \\sum_k \\langle k | \\hat{\\rho} | k \\rangle = \\sum_n p_n \\sum_k |\\langle k | \\psi_n \\rangle|^2 = \\sum_n p_n = 1$.</li>\n  <li><strong>Positive Semi-Definite:</strong> For any state $|\\phi\\rangle$, $\\langle \\phi | \\hat{\\rho} | \\phi \\rangle = \\sum_n p_n |\\langle \\phi | \\psi_n \\rangle|^2 \\ge 0$.</li>\n  <li><strong>Purity Criterion:</strong>\n  $$\\operatorname{Tr}(\\hat{\\rho}^2) \\le 1$$\n  $$\\operatorname{Tr}(\\hat{\\rho}^2) = 1 \\iff \\text{Pure State}, \\quad \\operatorname{Tr}(\\hat{\\rho}^2) < 1 \\iff \\text{Mixed State}$$\n  </li>\n</ol>\n\n<h4>3. Expectation Value of an Observable $\\hat{A}$</h4>\nThe ensemble average of any quantum observable $\\hat{A}$ is given cleanly by the trace:\n$$\\langle \\hat{A} \\rangle = \\sum_n p_n \\langle \\psi_n | \\hat{A} | \\psi_n \\rangle = \\sum_n p_n \\sum_k \\langle \\psi_n | k \\rangle \\langle k | \\hat{A} | \\psi_n \\rangle = \\sum_k \\langle k | \\hat{A} \\left( \\sum_n p_n |\\psi_n\\rangle \\langle \\psi_n| \\right) | k \\rangle$$\n$$\\langle \\hat{A} \\rangle = \\operatorname{Tr}(\\hat{\\rho} \\hat{A})$$"
        },
        {
          "id": "sec-3-7",
          "number": "\u00a73.7",
          "heading": "The von Neumann Equation of Motion",
          "simulation": "density-matrix-pure-mixed-sim",
          "content": "The time evolution of the density operator represents the quantum analog of classical Liouville dynamics.\n\n<h4>1. Derivation of the von Neumann Equation</h4>\nDifferentiating $\\hat{\\rho}(t) = \\sum_n p_n |\\psi_n(t)\\rangle \\langle \\psi_n(t)|$ with respect to time:\n$$i\\hbar \\frac{\\partial \\hat{\\rho}}{\\partial t} = i\\hbar \\sum_n p_n \\left( \\frac{\\partial |\\psi_n\\rangle}{\\partial t} \\langle \\psi_n| + |\\psi_n\\rangle \\frac{\\partial \\langle \\psi_n|}{\\partial t} \\right)$$\nUsing the time-dependent Schr\u00f6dinger equation $i\\hbar \\frac{\\partial |\\psi_n\\rangle}{\\partial t} = \\hat{H} |\\psi_n\\rangle$ and its adjoint $-i\\hbar \\frac{\\partial \\langle \\psi_n|}{\\partial t} = \\langle \\psi_n| \\hat{H}$:\n$$i\\hbar \\frac{\\partial \\hat{\\rho}}{\\partial t} = \\sum_n p_n \\left( \\hat{H} |\\psi_n\\rangle \\langle \\psi_n| - |\\psi_n\\rangle \\langle \\psi_n| \\hat{H} \\right) = \\hat{H} \\hat{\\rho} - \\hat{\\rho} \\hat{H}$$\n$$i\\hbar \\frac{\\partial \\hat{\\rho}}{\\partial t} = [\\hat{H}, \\hat{\\rho}]$$\nThis is the **von Neumann Equation** (or quantum Liouville equation).\n\n<h4>2. Classical Correspondence</h4>\nUnder Dirac's correspondence rule $[\\hat{A}, \\hat{B}] \\longleftrightarrow i\\hbar \\{A, B\\}_{\\text{PB}}$:\n$$\\frac{\\partial \\hat{\\rho}}{\\partial t} = \\frac{1}{i\\hbar} [\\hat{H}, \\hat{\\rho}] \\longleftrightarrow -\\{\\rho, H\\}_{\\text{PB}}$$\nThe von Neumann equation matches Liouville's theorem $\\frac{\\partial \\rho}{\\partial t} = -\\{\\rho, H\\}$.\n\n<h4>3. Stationary Equilibrium State</h4>\nFor a quantum system in statistical equilibrium, $\\frac{\\partial \\hat{\\rho}}{\\partial t} = 0$, requiring:\n$$[\\hat{H}, \\hat{\\rho}] = 0$$\nThe equilibrium density operator must commute with the Hamiltonian. Consequently, $\\hat{\\rho}$ must be diagonal in the basis of energy eigenstates."
        },
        {
          "id": "sec-3-8",
          "number": "\u00a73.8",
          "heading": "Quantum Ensembles and Unified Quantum Statistics",
          "simulation": "three-statistics-comparison-sim",
          "content": "We now express the fundamental thermodynamic ensembles in terms of the quantum density operator and derive the three quantum distribution functions.\n\n<h4>1. Quantum Density Operators for the Three Ensembles</h4>\n<ul>\n  <li><strong>Quantum Microcanonical Ensemble:</strong>\n  $$\\hat{\\rho} = \\frac{1}{\\Omega} \\sum_{E \\le E_n \\le E + \\delta E} |n\\rangle \\langle n|, \\quad S = -k_B \\operatorname{Tr}(\\hat{\\rho} \\ln \\hat{\\rho}) = k_B \\ln \\Omega$$\n  </li>\n  <li><strong>Quantum Canonical Ensemble:</strong>\n  $$\\hat{\\rho} = \\frac{e^{-\\beta \\hat{H}}}{Z}, \\quad Z = \\operatorname{Tr}(e^{-\\beta \\hat{H}}) = \\sum_n e^{-\\beta E_n}$$\n  $$F = -k_B T \\ln Z$$\n  </li>\n  <li><strong>Quantum Grand Canonical Ensemble:</strong>\n  $$\\hat{\\rho} = \\frac{e^{-\\beta (\\hat{H} - \\mu \\hat{N})}}{\\Xi}, \\quad \\Xi = \\operatorname{Tr}(e^{-\\beta (\\hat{H} - \\mu \\hat{N})})$$\n  $$\\Phi_G = -k_B T \\ln \\Xi = -PV$$\n  </li>\n</ul>\n\n<h4>2. Derivation of Unified Mean Occupation Numbers</h4>\nFor non-interacting quantum particles with single-particle energy levels $\\epsilon_i$, the grand partition function factorizes over independent single-particle states:\n$$\\Xi = \\prod_i \\Xi_i, \\quad \\Xi_i = \\sum_{n_i} e^{-\\beta (\\epsilon_i - \\mu) n_i}$$\n<ul>\n  <li><strong>For Fermions (Fermi-Dirac):</strong> $n_i \\in \\{0, 1\\}$ due to Pauli exclusion:\n  $$\\Xi_i^{\\text{FD}} = 1 + e^{-\\beta(\\epsilon_i - \\mu)}$$\n  $$\\bar{n}_i^{\\text{FD}} = -\\frac{1}{\\beta}\\frac{\\partial \\ln \\Xi_i}{\\partial \\epsilon_i} = \\frac{e^{-\\beta(\\epsilon_i - \\mu)}}{1 + e^{-\\beta(\\epsilon_i - \\mu)}} = \\frac{1}{e^{\\beta(\\epsilon_i - \\mu)} + 1}$$\n  </li>\n  <li><strong>For Bosons (Bose-Einstein):</strong> $n_i \\in \\{0, 1, 2, \\dots\\}$ (requires $\\mu < \\epsilon_0$ for convergence):\n  $$\\Xi_i^{\\text{BE}} = \\sum_{n=0}^\\infty \\left(e^{-\\beta(\\epsilon_i - \\mu)}\\right)^n = \\frac{1}{1 - e^{-\\beta(\\epsilon_i - \\mu)}}$$\n  $$\\bar{n}_i^{\\text{BE}} = -\\frac{1}{\\beta}\\frac{\\partial \\ln \\Xi_i}{\\partial \\epsilon_i} = \\frac{1}{e^{\\beta(\\epsilon_i - \\mu)} - 1}$$\n  </li>\n  <li><strong>Classical Maxwell-Boltzmann Limit:</strong> When $e^{\\beta(\\epsilon_i - \\mu)} \\gg 1$:\n  $$\\bar{n}_i^{\\text{MB}} = \\frac{1}{e^{\\beta(\\epsilon_i - \\mu)}}$$\n  </li>\n</ul>\n\n<h4>3. The Master Master Distribution Formula</h4>\nAll three statistics are captured by a single unified equation:\n$$\\bar{n}_i = \\frac{1}{e^{\\beta(\\epsilon_i - \\mu)} + a}, \\quad a = \\begin{cases} +1 & \\text{Fermi-Dirac (Fermions)} \\\\ -1 & \\text{Bose-Einstein (Bosons)} \\\\ 0 & \\text{Maxwell-Boltzmann (Classical)} \\end{cases}$$"
        }
      ],
      "problems": [
        {
          "id": "prob-3-1",
          "difficulty": "Medium",
          "title": "Density Matrix and Purity of a Spin-1/2 Ensemble",
          "question": "A beam of silver atoms with spin-1/2 is prepared in an ensemble where $75\\%$ of the atoms are in state $|\\uparrow\\rangle$ and $25\\%$ are in state $|\\downarrow\\rangle$. (a) Write down the density matrix $\\hat{\\rho}$ in the $\\{|\\uparrow\\rangle, |\\downarrow\\rangle\\}$ basis. (b) Compute $\\operatorname{Tr}(\\hat{\\rho}^2)$ to verify that this is a mixed state. (c) Calculate the expectation value $\\langle S_z \\rangle$ and $\\langle S_x \\rangle$.",
          "steps": [
            {
              "title": "Step 1: Construct the density matrix",
              "math": "$$\\hat{\\rho} = p_1 |\\uparrow\\rangle\\langle\\uparrow| + p_2 |\\downarrow\\rangle\\langle\\downarrow| = \\frac{3}{4} \\begin{pmatrix} 1 & 0 \\\\ 0 & 0 \\end{pmatrix} + \\frac{1}{4} \\begin{pmatrix} 0 & 0 \\\\ 0 & 1 \\end{pmatrix} = \\begin{pmatrix} 3/4 & 0 \\\\ 0 & 1/4 \\end{pmatrix}$$",
              "explanation": "Because the states are an incoherent statistical mixture along the z-axis, all off-diagonal coherence terms are zero."
            },
            {
              "title": "Step 2: Test purity via trace of rho squared",
              "math": "$$\\hat{\\rho}^2 = \\begin{pmatrix} 9/16 & 0 \\\\ 0 & 1/16 \\end{pmatrix}$$\n$$\\operatorname{Tr}(\\hat{\\rho}^2) = \\frac{9}{16} + \\frac{1}{16} = \\frac{10}{16} = \\frac{5}{8} = 0.625 < 1$$",
              "explanation": "Since $\\operatorname{Tr}(\\hat{\\rho}^2) < 1$, the state is strictly a mixed state with von Neumann entropy $S = -k_B \\operatorname{Tr}(\\hat{\\rho}\\ln\\hat{\\rho}) > 0$."
            },
            {
              "title": "Step 3: Compute spin expectation values",
              "math": "$$\\langle S_z \\rangle = \\operatorname{Tr}(\\hat{\\rho} S_z) = \\operatorname{Tr}\\left( \\begin{pmatrix} 3/4 & 0 \\\\ 0 & 1/4 \\end{pmatrix} \\frac{\\hbar}{2}\\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix} \\right) = \\frac{\\hbar}{2}\\left(\\frac{3}{4} - \\frac{1}{4}\\right) = \\frac{\\hbar}{4}$$\n$$\\langle S_x \\rangle = \\operatorname{Tr}(\\hat{\\rho} S_x) = \\operatorname{Tr}\\left( \\begin{pmatrix} 3/4 & 0 \\\\ 0 & 1/4 \\end{pmatrix} \\frac{\\hbar}{2}\\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix} \\right) = \\operatorname{Tr}\\left( \\frac{\\hbar}{2}\\begin{pmatrix} 0 & 3/4 \\\\ 1/4 & 0 \\end{pmatrix} \\right) = 0$$",
              "explanation": "There is a net macroscopic magnetization along $z$, but zero magnetization along $x$ due to the absence of quantum phase coherence."
            }
          ]
        },
        {
          "id": "prob-3-2",
          "difficulty": "Hard",
          "title": "Exchange Degeneracy Energy Correction for Two Interacting Particles",
          "question": "Two identical particles move in a 1D harmonic oscillator potential $V(x) = \\frac{1}{2}m\\omega^2 x^2$ and interact via a short-range contact potential $V_{\\text{int}}(x_1, x_2) = g\\,\\delta(x_1 - x_2)$. One particle is in the ground state $\\phi_0(x)$ and the other is in the first excited state $\\phi_1(x)$. (a) Write the properly symmetrized wavefunctions for Bosons and Fermions (spin-triplet). (b) Calculate the first-order perturbation energy shift $\\Delta E = \\langle V_{\\text{int}} \\rangle$ for both Bosons and Fermions.",
          "steps": [
            {
              "title": "Step 1: Write symmetrized wavefunctions",
              "math": "$$\\Psi_S(x_1, x_2) = \\frac{1}{\\sqrt{2}}[\\phi_0(x_1)\\phi_1(x_2) + \\phi_1(x_1)\\phi_0(x_2)] \\quad (\\text{Bosons})$$\n$$\\Psi_A(x_1, x_2) = \\frac{1}{\\sqrt{2}}[\\phi_0(x_1)\\phi_1(x_2) - \\phi_1(x_1)\\phi_0(x_2)] \\quad (\\text{Fermions})$$",
              "explanation": "For Fermions with parallel spins (triplet state), the spatial wavefunction must be strictly antisymmetric."
            },
            {
              "title": "Step 2: Evaluate perturbation integral for Fermions",
              "math": "$$\\Delta E_F = \\int_{-\\infty}^\\infty dx_1 \\int_{-\\infty}^\\infty dx_2 \\, |\\Psi_A(x_1, x_2)|^2 g \\,\\delta(x_1 - x_2) = g \\int_{-\\infty}^\\infty |\\Psi_A(x_1, x_1)|^2 dx_1$$\n$$\\text{Since } \\Psi_A(x_1, x_1) = \\frac{1}{\\sqrt{2}}[\\phi_0(x_1)\\phi_1(x_1) - \\phi_1(x_1)\\phi_0(x_1)] \\equiv 0 \\implies \\Delta E_F = 0$$",
              "explanation": "Because identical fermions never occupy the same spatial coordinate, they never feel the contact delta-function interaction! The Pauli exclusion principle provides complete shielding."
            },
            {
              "title": "Step 3: Evaluate perturbation integral for Bosons",
              "math": "$$\\Delta E_B = g \\int_{-\\infty}^\\infty |\\Psi_S(x_1, x_1)|^2 dx_1 = 2g \\int_{-\\infty}^\\infty |\\phi_0(x_1)|^2 |\\phi_1(x_1)|^2 dx_1 > 0$$",
              "explanation": "For bosons, the spatial bunching doubles the interaction probability, resulting in a positive repulsive energy shift of $2g I_{01}$."
            }
          ]
        },
        {
          "id": "prob-3-3",
          "difficulty": "Hard",
          "title": "Classical Limit and Quantum Virial Coefficient",
          "question": "Show that the first quantum correction to the ideal gas equation of state yields $P V = N k_B T (1 \\pm \\frac{B_2(T) N}{V})$, where the plus sign applies to Fermions and the minus sign to Bosons. Express the second virial coefficient $B_2(T)$ in terms of the thermal de Broglie wavelength $\\lambda_{\\text{th}}$.",
          "steps": [
            {
              "title": "Step 1: Expand grand potential in powers of fugacity",
              "math": "$$\\frac{P V}{k_B T} = \\ln \\Xi = \\mp \\sum_i \\ln(1 \\mp z e^{-\\beta \\epsilon_i}) \\approx z \\sum_i e^{-\\beta \\epsilon_i} \\pm \\frac{z^2}{2} \\sum_i e^{-2\\beta \\epsilon_i} + \\dots$$\n$$N = z \\frac{\\partial \\ln \\Xi}{\\partial z} \\approx z \\sum_i e^{-\\beta \\epsilon_i} \\pm z^2 \\sum_i e^{-2\\beta \\epsilon_i} + \\dots$$",
              "explanation": "Here upper signs correspond to Fermions ($+$) and lower signs to Bosons ($-$). Converting sums to integrals over momentum space."
            },
            {
              "title": "Step 2: Evaluate integrals using density of states",
              "math": "$$\\sum_i e^{-\\beta \\epsilon_i} = \\frac{V}{\\lambda_{\\text{th}}^3}, \\quad \\sum_i e^{-2\\beta \\epsilon_i} = \\frac{V}{(2\\pi m / 2\\beta)^{3/2} h^3 / (2\\pi)^{3/2}} = \\frac{V}{2^{3/2} \\lambda_{\\text{th}}^3}$$",
              "explanation": "This gives the high-temperature quantum expansion of particle number and pressure."
            },
            {
              "title": "Step 3: Invert for fugacity and obtain the equation of state",
              "math": "$$n = \\frac{N}{V} = \\frac{z}{\\lambda_{\\text{th}}^3} \\left( 1 \\pm \\frac{z}{2^{3/2}} \\right) \\implies z \\approx n \\lambda_{\\text{th}}^3 \\left( 1 \\mp \\frac{n \\lambda_{\\text{th}}^3}{2^{3/2}} \\right)$$\n$$\\frac{P}{k_B T} = n \\left( 1 \\pm \\frac{1}{2^{5/2}} n \\lambda_{\\text{th}}^3 \\right) \\implies P V = N k_B T \\left( 1 \\pm \\frac{1}{4\\sqrt{2}} \\frac{N \\lambda_{\\text{th}}^3}{V} \\right)$$\n$$B_2(T) = \\pm \\frac{\\lambda_{\\text{th}}^3}{4\\sqrt{2}}$$",
              "explanation": "Fermions exert a positive quantum effective pressure ($P > P_{\\text{ideal}}$) due to Pauli repulsion, whereas Bosons exert a negative quantum effective pressure ($P < P_{\\text{ideal}}$) due to bosonic attraction."
            }
          ]
        }
      ]
    },
    {
      "number": 4,
      "title": "Fermi Systems",
      "leadSummary": "Fermi-Dirac distribution, Fermi energy, Fermi surface, Sommerfeld expansion, Landau diamagnetism, Pauli paramagnetism, thermionic emission, and white dwarf degeneracy.",
      "sections": [
        {
          "id": "sec-4-1",
          "number": "\u00a74.1",
          "heading": "The Fermi-Dirac Distribution Function",
          "simulation": "fermi-dirac-step-sim",
          "content": "The **Fermi-Dirac distribution function** governs the statistical occupation of single-particle quantum states for any system of identical fermions (particles with half-integer spin, obeying the Pauli exclusion principle).\n\n<h4>1. Derivation via the Grand Canonical Ensemble</h4>\nConsider a single-particle state $i$ with energy $\\epsilon_i$. Due to the Pauli exclusion principle, the state can be occupied by either $n_i = 0$ or $n_i = 1$ fermion.\nThe grand canonical partition function for this single state is:\n$$\\Xi_i = \\sum_{n_i \\in \\{0, 1\\}} e^{-\\beta(\\epsilon_i - \\mu)n_i} = 1 + e^{-\\beta(\\epsilon_i - \\mu)}$$\nThe mean occupation number (probability of the state being occupied) is:\n$$f(\\epsilon_i) = \\langle n_i \\rangle = -\\frac{1}{\\beta}\\frac{\\partial \\ln \\Xi_i}{\\partial \\epsilon_i} = \\frac{e^{-\\beta(\\epsilon_i - \\mu)}}{1 + e^{-\\beta(\\epsilon_i - \\mu)}} = \\frac{1}{e^{(\\epsilon_i - \\mu)/(k_B T)} + 1}$$\nThis is the celebrated **Fermi-Dirac Distribution Function**.\n\n<h4>2. Behavior at Absolute Zero ($T = 0\\text{ K}$)</h4>\nAt $T = 0\\text{ K}$, the chemical potential defines the **Fermi Energy**: $\\mu(0) \\equiv \\epsilon_F$.\n$$\\lim_{T \\to 0} \\frac{\\epsilon - \\epsilon_F}{k_B T} = \\begin{cases} -\\infty & \\text{if } \\epsilon < \\epsilon_F \\\\ +\\infty & \\text{if } \\epsilon > \\epsilon_F \\end{cases}$$\nTherefore:\n$$f(\\epsilon) = \\begin{cases} 1 & \\text{if } \\epsilon < \\epsilon_F \\\\ 0 & \\text{if } \\epsilon > \\epsilon_F \\end{cases}$$\nAt absolute zero, the distribution is an exact Heaviside step function: all quantum states below $\\epsilon_F$ are $100\\%$ completely occupied, while all states above $\\epsilon_F$ are strictly empty.\n\n<h4>3. Thermal Broadening at Finite Temperature ($T > 0$)</h4>\nAt any finite temperature $T > 0$:\n<ul>\n  <li>At $\\epsilon = \\mu$, $f(\\mu) = \\frac{1}{e^0 + 1} = \\frac{1}{2}$ regardless of temperature! The chemical potential is always the exact energy level where the occupation probability is $50\\%$.</li>\n  <li>Thermal excitation only affects states within a narrow energy window of width $\\sim 2 k_B T$ to $4 k_B T$ around $\\mu$.</li>\n  <li>For $\\epsilon - \\mu \\gg k_B T$, $f(\\epsilon) \\approx e^{-(\\epsilon - \\mu)/k_B T}$, decaying into the classical Maxwell-Boltzmann tail.</li>\n</ul>"
        },
        {
          "id": "sec-4-2",
          "number": "\u00a74.2",
          "heading": "The Ideal Fermi-Dirac Gas and Density of States",
          "simulation": "fermi-dirac-step-sim",
          "content": "We now consider an ideal gas of $N$ non-interacting spin-1/2 fermions (electrons, neutrons) confined in a container of volume $V$.\n\n<h4>1. Quantum Density of States for Spin-1/2 Particles</h4>\nIn 3D reciprocal wavevector space ($k$-space), the volume occupied by one spatial orbital with periodic boundary conditions is $(2\\pi/L)^3 = 8\\pi^3 / V$.\nTaking into account electron spin degeneracy $g_s = 2s + 1 = 2$ (spin-up and spin-down):\n$$g(k) \\, dk = 2 \\times \\frac{V}{(2\\pi)^3} \\, 4\\pi k^2 dk = \\frac{V}{\\pi^2} k^2 dk$$\nFor non-relativistic fermions, energy is $\\epsilon = \\frac{\\hbar^2 k^2}{2m} \\implies k = \\frac{\\sqrt{2m\\epsilon}}{\\hbar}$, and $dk = \\frac{1}{2\\hbar}\\sqrt{\\frac{2m}{\\epsilon}} d\\epsilon$:\n$$g(\\epsilon) \\, d\\epsilon = \\frac{V}{\\pi^2} \\left(\\frac{2m\\epsilon}{\\hbar^2}\\right) \\frac{1}{2\\hbar}\\sqrt{\\frac{2m}{\\epsilon}} d\\epsilon = \\frac{V}{2\\pi^2} \\left( \\frac{2m}{\\hbar^2} \\right)^{3/2} \\epsilon^{1/2} d\\epsilon$$\nThe density of states grows as the square root of energy: $g(\\epsilon) \\propto \\epsilon^{1/2}$.\n\n<h4>2. Normalization Conditions</h4>\nThe total number of particles $N$ and total internal energy $U$ are given by:\n$$N = \\int_0^\\infty g(\\epsilon) f(\\epsilon) \\, d\\epsilon = \\frac{V}{2\\pi^2} \\left( \\frac{2m}{\\hbar^2} \\right)^{3/2} \\int_0^\\infty \\frac{\\epsilon^{1/2} d\\epsilon}{e^{(\\epsilon - \\mu)/k_B T} + 1}$$\n$$U = \\int_0^\\infty \\epsilon \\, g(\\epsilon) f(\\epsilon) \\, d\\epsilon = \\frac{V}{2\\pi^2} \\left( \\frac{2m}{\\hbar^2} \\right)^{3/2} \\int_0^\\infty \\frac{\\epsilon^{3/2} d\\epsilon}{e^{(\\epsilon - \\mu)/k_B T} + 1}$$"
        },
        {
          "id": "sec-4-3",
          "number": "\u00a74.3",
          "heading": "Fermi Energy, Fermi Momentum, and the Fermi Surface",
          "simulation": "fermi-surface-sphere-sim",
          "content": "At absolute zero, fermions pack into the lowest available quantum states up to a sharp energy cutoff termed the **Fermi Energy** $\\epsilon_F$.\n\n<h4>1. Derivation of the Fermi Energy</h4>\nSetting $T = 0\\text{ K}$, where $f(\\epsilon) = 1$ for $\\epsilon \\le \\epsilon_F$ and $0$ for $\\epsilon > \\epsilon_F$:\n$$N = \\int_0^{\\epsilon_F} g(\\epsilon) \\, d\\epsilon = \\frac{V}{2\\pi^2} \\left( \\frac{2m}{\\hbar^2} \\right)^{3/2} \\int_0^{\\epsilon_F} \\epsilon^{1/2} d\\epsilon = \\frac{V}{2\\pi^2} \\left( \\frac{2m}{\\hbar^2} \\right)^{3/2} \\frac{2}{3} \\epsilon_F^{3/2}$$\n$$N = \\frac{V}{3\\pi^2} \\left( \\frac{2m \\epsilon_F}{\\hbar^2} \\right)^{3/2}$$\nSolving explicitly for $\\epsilon_F$ in terms of particle number density $n = N/V$:\n$$\\epsilon_F = \\frac{\\hbar^2}{2m} (3\\pi^2 n)^{2/3}$$\n\n<h4>2. Fermi Wavevector and Fermi Momentum</h4>\nIn $k$-space, occupied states fill a sphere of radius $k_F$ called the **Fermi Sphere**:\n$$k_F = (3\\pi^2 n)^{1/3}$$\nThe corresponding **Fermi Momentum** is:\n$$p_F = \\hbar k_F = \\hbar (3\\pi^2 n)^{1/3}$$\nThe boundary in momentum space separating occupied from unoccupied states at $T = 0\\text{ K}$ is the **Fermi Surface**.\n\n<h4>3. Ground-State Total Energy and Zero-Point Pressure</h4>\nThe total kinetic energy of the Fermi gas at $T = 0\\text{ K}$ is:\n$$U_0 = \\int_0^{\\epsilon_F} \\epsilon \\, g(\\epsilon) \\, d\\epsilon = \\frac{V}{2\\pi^2} \\left( \\frac{2m}{\\hbar^2} \\right)^{3/2} \\frac{2}{5} \\epsilon_F^{5/2} = \\frac{3}{5} N \\epsilon_F$$\nThe average energy per particle at absolute zero is $\\langle \\epsilon \\rangle = \\frac{3}{5}\\epsilon_F > 0$.\nEven at absolute zero, fermions possess substantial kinetic energy due to quantum confinement and Pauli exclusion, exerting an enormous **Zero-Point Degeneracy Pressure**:\n$$P_0 = -\\frac{\\partial U_0}{\\partial V} = -\\frac{3}{5} N \\frac{\\partial \\epsilon_F}{\\partial V} = \\frac{2}{5} \\frac{N}{V} \\epsilon_F = \\frac{2}{3} \\frac{U_0}{V} = \\frac{2}{5} n \\epsilon_F$$"
        },
        {
          "id": "sec-4-4",
          "number": "\u00a74.4",
          "heading": "The Fermi Temperature and Characteristic Scales",
          "simulation": "fermi-surface-sphere-sim",
          "content": "To understand why quantum effects dominate electron behavior at room temperature, we introduce the **Fermi Temperature**.\n\n<h4>1. Definition of Fermi Temperature ($T_F$)</h4>\nThe Fermi temperature is defined as:\n$$T_F \\equiv \\frac{\\epsilon_F}{k_B} = \\frac{\\hbar^2}{2m k_B} (3\\pi^2 n)^{2/3}$$\n\n<h4>2. Characteristic Numerical Values for Real Metals</h4>\nConsider metallic Copper (Cu):\n<ul>\n  <li>Electron density: $n \\approx 8.49 \\times 10^{28}\\text{ electrons/m}^3$</li>\n  <li>Fermi energy: $\\epsilon_F = \\frac{(1.055 \\times 10^{-34})^2}{2(9.109 \\times 10^{-31})} [3\\pi^2 (8.49 \\times 10^{28})]^{2/3} = 1.125 \\times 10^{-18}\\text{ J} \\approx 7.03\\text{ eV}$</li>\n  <li>Fermi temperature: $T_F = \\frac{1.125 \\times 10^{-18}\\text{ J}}{1.381 \\times 10^{-23}\\text{ J/K}} \\approx 81,600\\text{ K}$</li>\n</ul>\n\n<h4>3. The Extreme Quantum Degeneracy of Metals</h4>\nBecause $T_F \\approx 80,000\\text{ K}$ is vastly higher than room temperature ($T = 300\\text{ K}$), the ratio is:\n$$\\frac{T}{T_F} \\approx \\frac{300}{80,000} \\approx 0.0037 \\ll 1$$\nEven glowing white-hot molten steel ($T \\sim 1800\\text{ K}$) has $T/T_F \\sim 0.02 \\ll 1$.\nConduction electrons in metals are **permanently and deeply in their quantum degenerate ground state** under all terrestrial conditions!"
        },
        {
          "id": "sec-4-5",
          "number": "\u00a74.5",
          "heading": "Fermi Velocity and Mean Velocity of Free Electrons",
          "simulation": "fermi-dirac-step-sim",
          "content": "Because electrons are packed into states up to $\\epsilon_F$, electrons at the Fermi surface move with tremendous speeds.\n\n<h4>1. The Fermi Velocity ($v_F$)</h4>\nThe speed of an electron residing on the Fermi surface is:\n$$v_F = \\frac{p_F}{m} = \\frac{\\hbar k_F}{m} = \\sqrt{\\frac{2\\epsilon_F}{m}}$$\nFor Copper ($\\epsilon_F = 7.03\\text{ eV}$):\n$$v_F = \\sqrt{\\frac{2 \\times (7.03 \\times 1.602 \\times 10^{-19}\\text{ J})}{9.109 \\times 10^{-31}\\text{ kg}}} = 1.57 \\times 10^6\\text{ m/s}$$\nThis is approximately $0.5\\%$ of the speed of light ($c$)!\nEven at absolute zero, electrons zip through the atomic crystal lattice at over $1,500\\text{ km/second}$.\n\n<h4>2. Mean Velocity of Free Electrons</h4>\nThe mean speed $\\langle v \\rangle$ of electrons throughout the Fermi sphere at $T = 0\\text{ K}$ is:\n$$\\langle v \\rangle = \\frac{1}{N} \\int_0^{\\epsilon_F} \\sqrt{\\frac{2\\epsilon}{m}} \\, g(\\epsilon) \\, d\\epsilon = \\frac{1}{N} \\frac{V}{2\\pi^2} \\left( \\frac{2m}{\\hbar^2} \\right)^{3/2} \\sqrt{\\frac{2}{m}} \\int_0^{\\epsilon_F} \\epsilon \\, d\\epsilon = \\frac{3}{4} v_F$$\nFor Copper, $\\langle v \\rangle = 0.75 \\times 1.57 \\times 10^6\\text{ m/s} = 1.18 \\times 10^6\\text{ m/s}$."
        },
        {
          "id": "sec-4-6",
          "number": "\u00a74.6",
          "heading": "Degenerate Fermi Systems and the Sommerfeld Expansion",
          "simulation": "fermi-dirac-step-sim",
          "content": "To evaluate thermodynamic quantities at temperatures $T \\ll T_F$, we use the **Sommerfeld Expansion**.\n\n<h4>1. The Sommerfeld Lemma</h4>\nFor any smooth function $H(\\epsilon)$ that vanishes at $\\epsilon = 0$:\n$$\\int_0^\\infty H(\\epsilon) f(\\epsilon) \\, d\\epsilon = \\int_0^\\mu H(\\epsilon) \\, d\\epsilon + \\frac{\\pi^2}{6}(k_B T)^2 H'(\\mu) + \\frac{7\\pi^4}{360}(k_B T)^4 H'''(\\mu) + \\dots$$\n\n<h4>2. Temperature Dependence of Chemical Potential $\\mu(T)$</h4>\nApplying the Sommerfeld expansion to the particle number $N = \\int_0^\\infty g(\\epsilon) f(\\epsilon) d\\epsilon$:\n$$N = \\int_0^\\mu g(\\epsilon) d\\epsilon + \\frac{\\pi^2}{6}(k_B T)^2 g'(\\mu)$$\nSince $N = \\int_0^{\\epsilon_F} g(\\epsilon) d\\epsilon$, and $g(\\epsilon) \\propto \\epsilon^{1/2} \\implies g'(\\mu) = \\frac{1}{2\\mu} g(\\mu)$:\n$$\\mu(T) \\approx \\epsilon_F \\left[ 1 - \\frac{\\pi^2}{12} \\left( \\frac{T}{T_F} \\right)^2 \\right]$$\nThe chemical potential shifts downward slightly with increasing temperature.\n\n<h4>3. Electronic Heat Capacity of Metals ($C_V^{\\text{el}}$)</h4>\nExpanding total energy $U(T)$:\n$$U(T) \\approx U_0 + \\frac{\\pi^2}{6} g(\\epsilon_F) (k_B T)^2 = \\frac{3}{5}N\\epsilon_F + \\frac{\\pi^2}{4} N k_B \\frac{T^2}{T_F}$$\nDifferentiating with respect to temperature gives the celebrated **Sommerfeld Linear Heat Capacity**:\n$$C_V^{\\text{el}} = \\frac{\\partial U}{\\partial T} = \\frac{\\pi^2}{2} N k_B \\left( \\frac{T}{T_F} \\right) = \\gamma T$$\nwhere $\\gamma = \\frac{\\pi^2}{2} \\frac{N k_B}{T_F}$ is the **Sommerfeld constant**.\n\n<h4>4. Resolution of the Classical Heat Capacity Catastrophe</h4>\nClassical physics predicted that conduction electrons should contribute $C_V = \\frac{3}{2} N k_B$, which was contradicted by experiments showing total heat capacity in metals at room temperature was dominated by phonons ($3R$).\nQuantum statistics explains this: only a tiny fraction of electrons\u2014those within $k_B T$ of the Fermi surface (a fraction $\\sim T / T_F \\approx 0.004$)\u2014can be thermally excited. The remaining $99.6\\%$ of electrons are locked in lower states by the Pauli exclusion principle and cannot absorb thermal energy!"
        },
        {
          "id": "sec-4-7",
          "number": "\u00a74.7",
          "heading": "Landau Diamagnetism",
          "simulation": "fermi-surface-sphere-sim",
          "content": "When an external magnetic field $\\mathbf{B} = B\\hat{\\mathbf{z}}$ is applied to a free electron gas, classical mechanics (the Bohr-van Leeuwen theorem) asserts that thermal equilibrium orbital magnetism is identically zero. Lev Landau (1930) showed that quantum mechanics produces a purely orbital diamagnetic response.\n\n<h4>1. Quantized Landau Energy Levels</h4>\nIn a uniform magnetic field $B$, classical cyclotron orbits are quantized into discrete **Landau levels**:\n$$\\epsilon(n, p_z) = \\left( n + \\frac{1}{2} \\right) \\hbar \\omega_c + \\frac{p_z^2}{2m}$$\nwhere $\\omega_c = \\frac{e B}{m}$ is the **cyclotron frequency**, and $n = 0, 1, 2, \\dots$.\nEach Landau level has an enormous macroscopic degeneracy per unit area:\n$$g_L = \\frac{e B}{h} = \\frac{1}{2\\pi \\ell_B^2}$$\nwhere $\\ell_B = \\sqrt{\\hbar / eB}$ is the magnetic length.\n\n<h4>2. Landau Diamagnetic Susceptibility</h4>\nSumming over the discrete Landau levels in the grand potential and expanding for weak fields ($k_B T \\gg \\hbar \\omega_c$ or $\\epsilon_F \\gg \\hbar \\omega_c$):\n$$\\Phi_G(B) \\approx \\Phi_G(0) + \\frac{V}{6} \\mu_B^2 \\left( \\frac{\\partial n}{\\partial \\mu} \\right) B^2$$\nThe resulting magnetization $M = -\\frac{1}{V}\\frac{\\partial \\Phi_G}{\\partial B}$ yields the **Landau Diamagnetic Susceptibility**:\n$$\\chi_{\\text{Landau}} = -\\frac{1}{3} \\mu_B^2 g(\\epsilon_F) = -\\frac{1}{3} \\chi_{\\text{Pauli}}$$\nQuantized orbital motion creates an opposing diamagnetic moment exactly one-third the magnitude of spin paramagnetism."
        },
        {
          "id": "sec-4-8",
          "number": "\u00a74.8",
          "heading": "Pauli Paramagnetism",
          "simulation": "fermi-surface-sphere-sim",
          "content": "Wolfgang Pauli (1927) explained why the conduction electrons in metals exhibit a small, temperature-independent paramagnetic susceptibility.\n\n<h4>1. Zeeman Splitting in the Conduction Band</h4>\nEach electron possesses an intrinsic magnetic dipole moment $\\boldsymbol{\\mu} = -g \\mu_B \\mathbf{s} \\approx -2 \\mu_B \\mathbf{s}$, where $\\mu_B = \\frac{e\\hbar}{2m} = 9.274 \\times 10^{-24}\\text{ J/T}$ is the Bohr magneton.\nIn an external field $B$, Zeeman interaction splits the energy levels:\n$$\\epsilon_\\uparrow = \\epsilon - \\mu_B B \\quad (\\text{spin parallel to } B), \\quad \\epsilon_\\downarrow = \\epsilon + \\mu_B B \\quad (\\text{spin antiparallel})$$\n\n<h4>2. Fermi Surface Asymmetry</h4>\nIn equilibrium, both spin sub-bands must fill to the identical chemical potential $\\epsilon_F$. Consequently, spin-up states expand while spin-down states contract:\n$$N_\\uparrow = \\frac{1}{2} \\int_0^{\\epsilon_F + \\mu_B B} g(\\epsilon) d\\epsilon \\approx \\frac{N}{2} + \\frac{1}{2} g(\\epsilon_F) \\mu_B B$$\n$$N_\\downarrow = \\frac{1}{2} \\int_0^{\\epsilon_F - \\mu_B B} g(\\epsilon) d\\epsilon \\approx \\frac{N}{2} - \\frac{1}{2} g(\\epsilon_F) \\mu_B B$$\nThe net excess of parallel spins is:\n$$\\Delta N = N_\\uparrow - N_\\downarrow = g(\\epsilon_F) \\mu_B B$$\n\n<h4>3. The Pauli Susceptibility Formula</h4>\nThe macroscopic magnetic moment is $M = \\mu_B \\Delta N = \\mu_B^2 g(\\epsilon_F) B$.\nThe magnetic susceptibility per unit volume is:\n$$\\chi_{\\text{Pauli}} = \\frac{\\mu_0 M}{B} = \\mu_0 \\mu_B^2 g(\\epsilon_F) = \\frac{3 n \\mu_0 \\mu_B^2}{2 \\epsilon_F}$$\nNotice that:\n<ol>\n  <li>$\\chi_{\\text{Pauli}}$ is **strictly independent of temperature** to leading order (unlike classical Curie paramagnetism $\\chi \\propto 1/T$).</li>\n  <li>Combining Pauli paramagnetism with Landau diamagnetism gives the net response:\n  $$\\chi_{\\text{total}} = \\chi_{\\text{Pauli}} + \\chi_{\\text{Landau}} = \\left(1 - \\frac{1}{3}\\right) \\chi_{\\text{Pauli}} = \\frac{2}{3} \\chi_{\\text{Pauli}} > 0$$\n  The electron gas in normal metals remains weakly paramagnetic overall.</li>\n</ol>"
        },
        {
          "id": "sec-4-9",
          "number": "\u00a74.9",
          "heading": "Thermionic Emission and the Richardson-Dushman Law",
          "simulation": "fermi-dirac-step-sim",
          "content": "Thermionic emission is the thermally induced flow of charge carriers over a surface potential barrier (used in vacuum tubes, electron microscopes, and cathode ray tubes).\n\n<h4>1. The Escape Condition and Work Function</h4>\nInside a metal, electrons occupy states up to the Fermi energy $\\epsilon_F$. The minimum energy required to liberate an electron from the Fermi level into vacuum at rest is the **Work Function** $\\Phi$ (typically $4.5\\text{ eV}$ for tungsten).\nAn electron at surface $z = 0$ can escape into vacuum only if its kinetic energy perpendicular to the surface exceeds the barrier:\n$$\\frac{p_z^2}{2m} \\ge \\epsilon_F + \\Phi$$\n\n<h4>2. Derivation of the Emission Current Density</h4>\nThe emission current density $J$ is obtained by integrating the flux $v_z = p_z / m$ over all escape states:\n$$J = 2 e \\left(\\frac{1}{h^3}\\right) \\int_{-\\infty}^\\infty dp_x \\int_{-\\infty}^\\infty dp_y \\int_{p_{z,\\min}}^\\infty dp_z \\, \\frac{p_z}{m} \\frac{1}{e^{(\\epsilon - \\mu)/k_B T} + 1}$$\nBecause $\\epsilon - \\mu \\ge \\Phi \\gg k_B T$, the Fermi-Dirac distribution reduces to the Maxwell-Boltzmann approximation $e^{-(\\epsilon - \\epsilon_F)/k_B T}$:\n$$J = \\frac{2 e}{m h^3} e^{\\epsilon_F / k_B T} \\left( \\int_{-\\infty}^\\infty e^{-p_x^2 / 2m k_B T} dp_x \\right)^2 \\int_{p_{z,\\min}}^\\infty p_z e^{-p_z^2 / 2m k_B T} dp_z$$\nThe transverse integrals yield $(2\\pi m k_B T)$. Evaluating the $p_z$ integral:\n$$\\int_{p_{z,\\min}}^\\infty p_z e^{-p_z^2 / 2m k_B T} dp_z = m k_B T \\exp\\left( -\\frac{\\epsilon_F + \\Phi}{k_B T} \\right)$$\n\n<h4>3. The Richardson-Dushman Equation</h4>\nCombining terms gives the famous **Richardson-Dushman Law**:\n$$J = A T^2 \\exp\\left( -\\frac{\\Phi}{k_B T} \\right)$$\nwhere $A$ is the universal **Richardson constant**:\n$$A = \\frac{4\\pi m e k_B^2}{h^3} = 1.20173 \\times 10^6\\text{ A/(m}^2\\cdot\\text{K}^2)$$"
        },
        {
          "id": "sec-4-10",
          "number": "\u00a74.10",
          "heading": "Statistical Equilibrium in White Dwarf Stars and Chandrasekhar Limit",
          "simulation": "white-dwarf-chandrasekhar-sim",
          "content": "When an intermediate-mass star (such as the Sun) exhausts its nuclear fuel, it collapses under self-gravity until halted by the **electron degeneracy pressure** of its completely degenerate electron gas, forming a **White Dwarf star**.\n\n<h4>1. Non-Relativistic Equilibrium</h4>\nIn a star of mass $M$ and radius $R$, the gravitational potential energy is:\n$$U_{\\text{grav}} = -\\frac{3}{5} \\frac{G M^2}{R}$$\nFor non-relativistic degenerate electrons ($p_F \\ll m_e c$), the kinetic energy scales as:\n$$U_{\\text{kin}} = \\frac{3}{5} N \\epsilon_F \\propto N \\frac{\\hbar^2}{m_e} \\left(\\frac{N}{R^3}\\right)^{2/3} \\propto \\frac{\\hbar^2 N^{5/3}}{m_e R^2}$$\nMinimizing total energy $E = U_{\\text{kin}} + U_{\\text{grav}}$ with respect to $R$:\n$$\\frac{dE}{dR} = -\\frac{2 C_1}{R^3} + \\frac{C_2 G M^2}{R^2} = 0 \\implies R \\propto M^{-1/3}$$\nRemarkably, a heavier white dwarf is physically smaller!\n\n<h4>2. Relativistic Core Collapse and the Chandrasekhar Limit</h4>\nAs stellar mass increases, the star contracts and core density soars, driving the Fermi momentum into the ultra-relativistic regime:\n$$p_F = \\hbar (3\\pi^2 n)^{1/3} \\gg m_e c$$\nFor ultra-relativistic electrons, energy is linear in momentum: $\\epsilon = p c$. The kinetic degeneracy energy becomes:\n$$U_{\\text{kin}}^{\\text{rel}} \\propto N p_F c \\propto \\hbar c \\frac{N^{4/3}}{R}$$\nNotice that both gravitational and relativistic kinetic energy scale as $1/R$:\n$$E_{\\text{total}} = \\left( A \\hbar c N^{4/3} - B G M^2 \\right) \\frac{1}{R}$$\nIf gravity exceeds degeneracy pressure ($B G M^2 > A \\hbar c N^{4/3}$), no stable equilibrium radius exists: the star collapses indefinitely!\nEquating the two terms yields the **Chandrasekhar Mass Limit** (Subrahmanyan Chandrasekhar, 1930):\n$$M_{\\text{Ch}} = \\frac{\\omega_3^0}{4\\pi} \\left( \\frac{h c}{G} \\right)^{3/2} \\left( \\frac{1}{\\mu_e m_p} \\right)^2 \\approx 1.44 M_\\odot$$\nAny stellar core exceeding $1.44$ solar masses cannot be supported by electron degeneracy and must collapse into a neutron star or black hole."
        }
      ],
      "problems": [
        {
          "id": "prob-4-1",
          "difficulty": "Medium",
          "title": "Fermi Energy and Degeneracy Pressure in Liquid 3He",
          "question": "Liquid helium-3 ($^3\\text{He}$) is a fermion liquid with spin-1/2 and atomic mass $m = 5.01 \\times 10^{-27}\\text{ kg}$. At low temperatures, its mass density is $\\rho = 81\\text{ kg/m}^3$. (a) Calculate the number density $n$, Fermi wavevector $k_F$, and Fermi energy $\\epsilon_F$ in Kelvin. (b) Calculate the zero-point degeneracy pressure $P_0$ exerted by the liquid at $T = 0\\text{ K}$.",
          "steps": [
            {
              "title": "Step 1: Compute particle number density",
              "math": "$$n = \\frac{\\rho}{m} = \\frac{81\\text{ kg/m}^3}{5.01 \\times 10^{-27}\\text{ kg}} = 1.617 \\times 10^{28}\\text{ atoms/m}^3$$",
              "explanation": "This establishes the atomic number density of the liquid."
            },
            {
              "title": "Step 2: Determine Fermi wavevector and Fermi energy",
              "math": "$$k_F = (3\\pi^2 n)^{1/3} = [3\\pi^2 (1.617 \\times 10^{28})]^{1/3} = 7.823 \\times 10^9\\text{ m}^{-1}$$\n$$\\epsilon_F = \\frac{\\hbar^2 k_F^2}{2m} = \\frac{(1.055 \\times 10^{-34})^2 (7.823 \\times 10^9)^2}{2 (5.01 \\times 10^{-27})} = 6.792 \\times 10^{-23}\\text{ J}$$\n$$T_F = \\frac{\\epsilon_F}{k_B} = \\frac{6.792 \\times 10^{-23}\\text{ J}}{1.381 \\times 10^{-23}\\text{ J/K}} = 4.92\\text{ K}$$",
              "explanation": "Because $T_F \\approx 4.9\\text{ K}$, liquid $^3\\text{He}$ below $1\\text{ K}$ is a degenerate quantum Fermi liquid."
            },
            {
              "title": "Step 3: Calculate the zero-point degeneracy pressure",
              "math": "$$P_0 = \\frac{2}{5} n \\epsilon_F = 0.4 \\times (1.617 \\times 10^{28}\\text{ m}^{-3}) \\times (6.792 \\times 10^{-23}\\text{ J}) = 4.393 \\times 10^5\\text{ Pa} \\approx 4.34\\text{ atm}$$",
              "explanation": "The quantum zero-point degeneracy pressure exceeds 4 atmospheres, preventing liquid $^3\\text{He}$ from freezing into a solid under ambient pressure down to absolute zero."
            }
          ]
        },
        {
          "id": "prob-4-2",
          "difficulty": "Hard",
          "title": "Electronic vs Lattice Heat Capacity in Copper",
          "question": "For Copper, the Fermi temperature is $T_F = 81,600\\text{ K}$ and the Debye temperature is $\\Theta_D = 343\\text{ K}$. (a) Express the electronic heat capacity $C_V^{\\text{el}} = \\gamma T$ and lattice heat capacity $C_V^{\\text{ph}} = A T^3$. (b) Find the crossover temperature $T^*$ below which the electronic contribution exceeds the phonon contribution.",
          "steps": [
            {
              "title": "Step 1: Write down electronic and lattice heat capacities",
              "math": "$$C_V^{\\text{el}} = \\frac{\\pi^2}{2} R \\left(\\frac{T}{T_F}\\right) = \\gamma T, \\quad \\gamma = \\frac{\\pi^2 (8.314)}{2 (81,600)} = 5.03 \\times 10^{-4}\\text{ J/(mol}\\cdot\\text{K}^2)$$\n$$C_V^{\\text{ph}} = \\frac{12\\pi^4}{5} R \\left(\\frac{T}{\\Theta_D}\\right)^3 = A T^3, \\quad A = \\frac{12\\pi^4 (8.314)}{5 (343)^3} = 4.80 \\times 10^{-5}\\text{ J/(mol}\\cdot\\text{K}^4)$$",
              "explanation": "At low temperatures, total heat capacity is $C_V = \\gamma T + A T^3$."
            },
            {
              "title": "Step 2: Equate contributions to find crossover temperature T*",
              "math": "$$\\gamma T^* = A (T^*)^3 \\implies (T^*)^2 = \\frac{\\gamma}{A} = \\frac{5.03 \\times 10^{-4}}{4.80 \\times 10^{-5}} = 10.48\\text{ K}^2$$\n$$T^* = \\sqrt{10.48} \\approx 3.24\\text{ K}$$",
              "explanation": "Below $3.24\\text{ K}$, the linear electronic term dominates over the cubic lattice term, while at room temperature ($300\\text{ K}$) phonons dominate overwhelmingly."
            }
          ]
        },
        {
          "id": "prob-4-3",
          "difficulty": "Hard",
          "title": "Ultra-Relativistic Electron Degeneracy in a Massive White Dwarf",
          "question": "In a dense white dwarf, electrons are ultra-relativistic with $\\epsilon \\approx p c$. (a) Derive the density of states $g(\\epsilon)$ and Fermi energy $\\epsilon_F$. (b) Derive the relativistic degeneracy equation of state $P \\propto \\rho^{4/3}$.",
          "steps": [
            {
              "title": "Step 1: Compute relativistic density of states",
              "math": "$$\\epsilon = p c = \\hbar k c \\implies k = \\frac{\\epsilon}{\\hbar c}, \\quad dk = \\frac{d\\epsilon}{\\hbar c}$$\n$$g(\\epsilon) d\\epsilon = 2 \\times \\frac{V}{2\\pi^2} k^2 dk = \\frac{V}{\\pi^2 (\\hbar c)^3} \\epsilon^2 d\\epsilon$$",
              "explanation": "For ultra-relativistic particles, the density of states grows quadratically with energy."
            },
            {
              "title": "Step 2: Integrate to obtain Fermi energy",
              "math": "$$N = \\int_0^{\\epsilon_F} g(\\epsilon) d\\epsilon = \\frac{V}{3\\pi^2 (\\hbar c)^3} \\epsilon_F^3 \\implies \\epsilon_F = \\hbar c (3\\pi^2 n)^{1/3}$$",
              "explanation": "The ultra-relativistic Fermi energy scales with density as $n^{1/3}$ rather than $n^{2/3}$."
            },
            {
              "title": "Step 3: Calculate energy and pressure",
              "math": "$$U_0 = \\int_0^{\\epsilon_F} \\epsilon g(\\epsilon) d\\epsilon = \\frac{V}{4\\pi^2 (\\hbar c)^3} \\epsilon_F^4 = \\frac{3}{4} N \\epsilon_F = \\frac{3}{4} \\hbar c (3\\pi^2)^{1/3} V \\left(\\frac{N}{V}\\right)^{4/3}$$\n$$P_0 = -\\frac{\\partial U_0}{\\partial V} = \\frac{1}{3}\\frac{U_0}{V} = \\frac{1}{4} \\hbar c (3\\pi^2)^{1/3} n^{4/3} \\propto \\rho^{4/3}$$",
              "explanation": "The adiabatic index softens from $\\gamma = 5/3$ down to $\\gamma = 4/3$, leading directly to the gravitational instability discovered by Chandrasekhar."
            }
          ]
        }
      ]
    },
    {
      "number": 5,
      "title": "Bose Systems",
      "leadSummary": "Bose-Einstein distribution, Planck radiation law, photon gas thermodynamics, phonon specific heat, Debye model, Bose-Einstein condensation, superfluidity, and ortho/para hydrogen.",
      "sections": [
        {
          "id": "sec-5-1",
          "number": "\u00a75.1",
          "heading": "The Bose-Einstein Distribution Function and Applications",
          "simulation": "three-statistics-comparison-sim",
          "content": "The **Bose-Einstein distribution function** governs the statistical occupancy of single-particle quantum states for any system of identical bosons (particles with integer intrinsic spin $s = 0, 1, 2, \\dots$, possessing symmetric many-body wavefunctions).\n\n<h4>1. Derivation via the Grand Canonical Ensemble</h4>\nFor bosons, any single-particle quantum state $i$ can be occupied by any number of particles $n_i \\in \\{0, 1, 2, 3, \\dots\\}$.\nThe grand partition function for a single state $i$ is a geometric series:\n$$\\Xi_i = \\sum_{n_i=0}^\\infty e^{-\\beta(\\epsilon_i - \\mu)n_i} = \\frac{1}{1 - e^{-\\beta(\\epsilon_i - \\mu)}}$$\nFor this geometric series to converge, the ratio $e^{-\\beta(\\epsilon_i - \\mu)}$ must be strictly less than $1$, requiring:\n$$\\epsilon_i - \\mu > 0 \\implies \\mu < \\epsilon_0$$\nThe chemical potential of an ideal Bose gas must always be strictly less than the ground-state energy.\nThe mean occupation number is:\n$$n(\\epsilon_i) = \\langle n_i \\rangle = -\\frac{1}{\\beta}\\frac{\\partial \\ln \\Xi_i}{\\partial \\epsilon_i} = \\frac{e^{-\\beta(\\epsilon_i - \\mu)}}{1 - e^{-\\beta(\\epsilon_i - \\mu)}} = \\frac{1}{e^{(\\epsilon_i - \\mu)/(k_B T)} - 1}$$\nThis is the **Bose-Einstein Distribution Function**.\n\n<h4>2. Fundamental Differences Between Quantum Statistics</h4>\n<ul>\n  <li>As $\\epsilon \\to \\mu$, the Bose occupation number diverges: $n(\\epsilon) \\to +\\infty$. Bosons enjoy occupying the same quantum state, leading to macroscopic condensation.</li>\n  <li>In contrast, the Fermi-Dirac occupation can never exceed $1$: $f(\\epsilon) \\le 1$.</li>\n  <li>In the classical dilute limit where $e^{(\\epsilon - \\mu)/k_B T} \\gg 1$, both distributions converge to the classical Maxwell-Boltzmann exponential $e^{-(\\epsilon - \\mu)/k_B T}$.</li>\n</ul>"
        },
        {
          "id": "sec-5-2",
          "number": "\u00a75.2",
          "heading": "Planck's Radiation Law and Cavity Modes",
          "simulation": "planck-blackbody-spectrum-sim",
          "content": "Blackbody radiation is the thermal electromagnetic radiation within an enclosed cavity in thermodynamic equilibrium with its cavity walls.\n\n<h4>1. Photons as a Bose Gas with Zero Chemical Potential</h4>\nPhotons are spin-1 massless bosons. In a cavity, photons are continuously absorbed and emitted by the cavity walls; their total number $N$ is not conserved.\nIn thermal equilibrium, Helmholtz free energy $F$ is minimized with respect to photon number:\n$$\\left(\\frac{\\partial F}{\\partial N}\\right)_{T, V} = \\mu = 0$$\nThe chemical potential of a photon gas is **identically zero**: $\\mu = 0$.\nThe mean number of photons in a cavity mode of frequency $\\nu$ is:\n$$\\langle n_\\nu \\rangle = \\frac{1}{e^{h\\nu / k_B T} - 1}$$\n\n<h4>2. Density of Electromagnetic Modes</h4>\nElectromagnetic waves in a cavity of volume $V$ have wavevector $k = 2\\pi \\nu / c$.\nBecause electromagnetic waves are transverse, there are $g = 2$ independent orthogonal polarization states for every wavevector:\n$$g(\\nu) \\, d\\nu = 2 \\times \\frac{V}{(2\\pi)^3} 4\\pi k^2 dk = 2 \\times \\frac{4\\pi V}{(2\\pi)^3} \\left(\\frac{2\\pi \\nu}{c}\\right)^2 \\frac{2\\pi}{c} d\\nu = \\frac{8\\pi V}{c^3} \\nu^2 d\\nu$$\n\n<h4>3. Planck's Spectral Radiation Formula</h4>\nMultiplying mode density by average mode energy $\\langle E_\\nu \\rangle = h\\nu \\langle n_\\nu \\rangle$:\n$$u(\\nu) \\, d\\nu = \\frac{1}{V} g(\\nu) h\\nu \\langle n_\\nu \\rangle d\\nu = \\frac{8\\pi h \\nu^3}{c^3} \\frac{d\\nu}{e^{h\\nu / k_B T} - 1}$$\nExpressed in terms of wavelength $\\lambda = c / \\nu$ ($|d\\nu| = \\frac{c}{\\lambda^2} d\\lambda$):\n$$u(\\lambda) \\, d\\lambda = \\frac{8\\pi h c}{\\lambda^5} \\frac{d\\lambda}{e^{h c / (\\lambda k_B T)} - 1}$$\nThis is **Planck's Law of Blackbody Radiation** (1900), which birthed quantum physics."
        },
        {
          "id": "sec-5-3",
          "number": "\u00a75.3",
          "heading": "The Photon Gas and Thermodynamics of Radiation",
          "simulation": "planck-blackbody-spectrum-sim",
          "content": "We now integrate Planck's law to derive the macroscopic thermodynamic properties of blackbody radiation.\n\n<h4>1. Total Energy Density and the Stefan-Boltzmann Law</h4>\nThe total electromagnetic energy density in the cavity is:\n$$u(T) = \\int_0^\\infty u(\\nu) \\, d\\nu = \\frac{8\\pi h}{c^3} \\int_0^\\infty \\frac{\\nu^3 d\\nu}{e^{h\\nu / k_B T} - 1}$$\nSubstituting $x = \\frac{h\\nu}{k_B T}$:\n$$u(T) = \\frac{8\\pi h}{c^3} \\left(\\frac{k_B T}{h}\\right)^4 \\int_0^\\infty \\frac{x^3 dx}{e^x - 1}$$\nThe standard Bose-Einstein definite integral is $\\int_0^\\infty \\frac{x^3 dx}{e^x - 1} = \\frac{\\pi^4}{15}$. Therefore:\n$$u(T) = \\left( \\frac{8\\pi^5 k_B^4}{15 c^3 h^3} \\right) T^4 = a T^4$$\nwhere $a = 7.5657 \\times 10^{-16}\\text{ J/(m}^3\\cdot\\text{K}^4)$ is the radiation constant.\nThe radiant emissive power (flux density) from an ideal blackbody surface is:\n$$J = \\frac{c}{4} u(T) = \\sigma T^4$$\nwhere $\\sigma = \\frac{a c}{4} = 5.6704 \\times 10^{-8}\\text{ W/(m}^2\\cdot\\text{K}^4)$ is the **Stefan-Boltzmann constant**.\n\n<h4>2. Wien's Displacement Law</h4>\nMaximizing $u(\\lambda)$ with respect to $\\lambda$ yields $\\frac{d}{d\\lambda} u(\\lambda) = 0$, leading to:\n$$\\frac{hc}{\\lambda_{\\max} k_B T} \\left( 1 - e^{-hc/(\\lambda_{\\max} k_B T)} \\right) = 5$$\nSolving numerically gives $x = \\frac{hc}{\\lambda_{\\max} k_B T} \\approx 4.9651$, establishing **Wien's Displacement Law**:\n$$\\lambda_{\\max} T = \\frac{h c}{4.9651 k_B} = 2.8978 \\times 10^{-3}\\text{ m}\\cdot\\text{K}$$\n\n<h4>3. Radiation Pressure and Entropy of the Photon Gas</h4>\nBecause photons are relativistic ($E = p c$), the radiation pressure is:\n$$P = \\frac{1}{3} u(T) = \\frac{1}{3} a T^4$$\nThe total Helmholtz free energy is:\n$$F = U - TS = -PV = -\\frac{1}{3} a V T^4$$\nThe entropy of the photon gas is:\n$$S = -\\left(\\frac{\\partial F}{\\partial T}\\right)_V = \\frac{4}{3} a V T^3$$"
        },
        {
          "id": "sec-5-4",
          "number": "\u00a75.4",
          "heading": "The Specific Heat of Solids and the Phonon Gas",
          "simulation": "debye-vs-einstein-cv-sim",
          "content": "In a crystalline solid, atomic nuclei do not vibrate independently; their motion is coupled by interatomic electrostatic forces, forming collective vibrational wave modes called **phonons**.\n\n<h4>1. Phonons as Quasiparticles</h4>\nA phonon is a quantum of crystal lattice vibration possessing energy $E = \\hbar \\omega$ and crystal momentum $\\mathbf{p} = \\hbar \\mathbf{k}$.\nLike photons:\n<ul>\n  <li>Phonons are bosons with spin 0.</li>\n  <li>Phonons are created and destroyed thermally without number conservation; their chemical potential is zero: $\\mu = 0$.</li>\n  <li>Mean phonon occupancy is given by Planck's distribution:\n  $$\\langle n_\\omega \\rangle = \\frac{1}{e^{\\hbar \\omega / k_B T} - 1}$$\n  </li>\n</ul>\n\n<h4>2. Acoustic and Optical Phonon Branches</h4>\nFor a 3D crystal lattice with $N$ unit cells and $p$ atoms per basis:\n<ul>\n  <li>Total degrees of freedom: $3pN$.</li>\n  <li>$3$ **Acoustic Branches:** At long wavelengths ($k \\to 0$), atoms in a cell move in phase; frequency is linear: $\\omega = v_s k$ (sound waves).</li>\n  <li>$3(p - 1)$ **Optical Branches:** Adjacent basis atoms vibrate out of phase, creating oscillating electric dipoles that couple to light.</li>\n</ul>"
        },
        {
          "id": "sec-5-5",
          "number": "\u00a75.5",
          "heading": "The Debye Model of Lattice Specific Heat",
          "simulation": "debye-vs-einstein-cv-sim",
          "content": "Peter Debye (1912) recognized that low-temperature heat capacity is dominated by long-wavelength acoustic phonons, which can be treated as an elastic continuous medium.\n\n<h4>1. The Debye Density of States and Debye Cutoff Frequency</h4>\nIn an isotropic elastic solid with 1 longitudinal and 2 transverse sound speeds:\n$$g(\\omega) = \\frac{V}{2\\pi^2} \\left( \\frac{1}{v_L^3} + \\frac{2}{v_T^3} \\right) \\omega^2 = \\frac{3V}{2\\pi^2 v_s^3} \\omega^2$$\nBecause a crystal of $N$ atoms has exactly $3N$ vibrational modes, the spectrum must terminate at a maximum **Debye Cutoff Frequency** $\\omega_D$:\n$$\\int_0^{\\omega_D} g(\\omega) \\, d\\omega = 3N \\implies \\frac{V}{2\\pi^2 v_s^3} \\omega_D^3 = 3N \\implies \\omega_D = v_s \\left( \\frac{6\\pi^2 N}{V} \\right)^{1/3}$$\nWe define the **Debye Temperature** $\\Theta_D$:\n$$\\Theta_D \\equiv \\frac{\\hbar \\omega_D}{k_B}$$\n\n<h4>2. Total Lattice Energy and Debye Specific Heat</h4>\nThe total vibrational internal energy is:\n$$U(T) = \\int_0^{\\omega_D} \\hbar \\omega \\langle n_\\omega \\rangle g(\\omega) d\\omega = 9 N k_B T \\left( \\frac{T}{\\Theta_D} \\right)^3 \\int_0^{\\Theta_D/T} \\frac{x^3 dx}{e^x - 1}$$\nDifferentiating with respect to $T$ yields the **Debye Heat Capacity**:\n$$C_V(T) = 9 N k_B \\left( \\frac{T}{\\Theta_D} \\right)^3 \\int_0^{\\Theta_D/T} \\frac{x^4 e^x}{(e^x - 1)^2} dx$$\n\n<h4>3. The Low-Temperature Debye $T^3$ Law</h4>\nAt low temperatures ($T \\ll \\Theta_D$), the upper integration limit extends to infinity: $\\int_0^\\infty \\frac{x^4 e^x dx}{(e^x - 1)^2} = \\frac{4\\pi^4}{15}$.\n$$C_V(T) = 9 N k_B \\left( \\frac{T}{\\Theta_D} \\right)^3 \\frac{4\\pi^4}{15} = \\frac{12\\pi^4}{5} N k_B \\left( \\frac{T}{\\Theta_D} \\right)^3$$\nThis is the famous **Debye $T^3$ Law**. It perfectly matches experimental calorimeter data for all non-magnetic insulating solids at low temperatures."
        },
        {
          "id": "sec-5-6",
          "number": "\u00a75.6",
          "heading": "Bose-Einstein Condensation (BEC)",
          "simulation": "bose-einstein-condensation-sim",
          "content": "Satyendra Nath Bose (1924) and Albert Einstein (1925) predicted that an ideal gas of massive bosons undergoes a spectacular phase transition at low temperatures, with a macroscopic fraction of particles collapsing into the identical zero-momentum ground state.\n\n<h4>1. Maximum Capacity of Excited States</h4>\nFor a 3D gas of $N$ non-relativistic bosons of mass $m$ in volume $V$, the density of states is $g(\\epsilon) = \\frac{2\\pi V}{h^3} (2m)^{3/2} \\epsilon^{1/2}$.\nThe total number of particles in excited states ($\\epsilon > 0$) is:\n$$N_{\\text{exc}} = \\int_0^\\infty \\frac{g(\\epsilon) d\\epsilon}{e^{(\\epsilon - \\mu)/k_B T} - 1}$$\nBecause $\\mu \\le 0$, the maximum number of bosons that excited states can hold occurs when $\\mu \\to 0^-$:\n$$N_{\\text{exc}}^{\\max}(T) = \\frac{2\\pi V (2m)^{3/2}}{h^3} (k_B T)^{3/2} \\int_0^\\infty \\frac{x^{1/2} dx}{e^x - 1} = V \\left( \\frac{m k_B T}{2\\pi \\hbar^2} \\right)^{3/2} \\zeta(3/2)$$\nwhere $\\zeta(3/2) \\approx 2.6124$ is the Riemann zeta function.\n\n<h4>2. The Critical Condensation Temperature ($T_c$)</h4>\nWhen the temperature falls below a critical value $T_c$, the maximum capacity of excited states becomes strictly less than the total number of particles: $N_{\\text{exc}}^{\\max}(T) < N$.\nSetting $N_{\\text{exc}}^{\\max}(T_c) = N$ defines the **Bose-Einstein Transition Temperature**:\n$$T_c = \\frac{2\\pi \\hbar^2}{m k_B} \\left( \\frac{N/V}{\\zeta(3/2)} \\right)^{2/3} = \\frac{2\\pi \\hbar^2}{m k_B} \\left( \\frac{n}{2.6124} \\right)^{2/3}$$\n\n<h4>3. Macroscopic Ground-State Condensation Fraction</h4>\nFor $T < T_c$, all surplus particles must condense into the single ground state $\\epsilon_0 = 0$:\n$$N_0(T) = N - N_{\\text{exc}}(T) = N \\left[ 1 - \\left( \\frac{T}{T_c} \\right)^{3/2} \\right]$$\nBelow $T_c$, a macroscopic fraction of the gas forms a single giant macroscopic quantum wavepacket, experimentally observed in 1995 in trapped Rubidium-87 atoms by Cornell, Wieman, and Ketterle (Nobel Prize 2001)."
        },
        {
          "id": "sec-5-7",
          "number": "\u00a75.7",
          "heading": "Superfluidity in Liquid Helium-4",
          "simulation": "superfluid-two-fluid-sim",
          "content": "When Helium-4 ($^4\\text{He}$, a spin-0 boson) is cooled below $T_\\lambda = 2.17\\text{ K}$ at saturated vapor pressure, it undergoes the **Lambda Transition** from normal Liquid He-I to superfluid **Liquid He-II**.\n\n<h4>1. The Two-Fluid Model (Tisza and Landau)</h4>\nLiquid He-II behaves hydrodynamically as an interpenetrating mixture of two components:\n$$\\rho = \\rho_n + \\rho_s$$\n<ul>\n  <li><strong>Superfluid Component ($\\rho_s$):</strong> Fraction of atoms in the macroscopic quantum condensate. It possesses **strictly zero viscosity** ($\\eta_s = 0$) and **zero entropy** ($s_s = 0$). It can flow with zero friction through sub-micron capillaries!</li>\n  <li><strong>Normal Fluid Component ($\\rho_n$):</strong> Thermal gas of elementary quasiparticle excitations (phonons and rotons). It has normal viscosity and carries all the entropy of the liquid.</li>\n</ul>\nAs $T \\to 0\\text{ K}$, $\\rho_n / \\rho \\to 0$ and $\\rho_s / \\rho \\to 1$.\n\n<h4>2. Landau's Criterion for Superfluidity and the Roton Spectrum</h4>\nLev Landau (1941) asked: *At what speed will an object moving through He-II experience frictional drag by creating elementary excitations?*\nBy energy and momentum conservation, creation of an excitation with energy $\\epsilon(p)$ and momentum $p$ requires:\n$$v > v_c = \\min_p \\left( \\frac{\\epsilon(p)}{p} \\right)$$\nFor He-II, the excitation spectrum exhibits a local minimum at $p_0 / \\hbar \\approx 1.92\\text{ \u00c5}^{-1}$ with energy gap $\\Delta / k_B \\approx 8.6\\text{ K}$ called the **Roton minimum**:\n$$\\epsilon(p) \\approx \\Delta + \\frac{(p - p_0)^2}{2\\mu}$$\nThe minimum ratio $\\epsilon(p)/p$ is:\n$$v_c = \\frac{\\Delta}{p_0} \\approx 58\\text{ m/s}$$\nFor any flow velocity $v < v_c$, creating excitations is kinematically forbidden by quantum mechanics: the liquid flows with **strictly zero dissipation**!"
        },
        {
          "id": "sec-5-8",
          "number": "\u00a75.8",
          "heading": "Thermodynamics of Bose Systems",
          "simulation": "bose-gas-momentum-distribution-sim",
          "content": "We now explore the thermodynamic behavior of the degenerate Bose gas across the BEC transition.\n\n<h4>1. Pressure Below $T_c$</h4>\nIn the condensed phase ($T < T_c$), the chemical potential is locked at zero: $\\mu = 0$.\nThe grand potential $\\Phi_G = -PV$ is given solely by excited states:\n$$P(T) = k_B T \\left( \\frac{m k_B T}{2\\pi \\hbar^2} \\right)^{3/2} \\zeta(5/2) \\propto T^{5/2}$$\nwhere $\\zeta(5/2) \\approx 1.3415$.\nNotice that:\n<blockquote>\nBelow $T_c$, the pressure depends strictly on temperature $T$ and is <strong>completely independent of volume $V$</strong>!\n$$\\left(\\frac{\\partial P}{\\partial V}\\right)_T = 0$$\n</blockquote>\nThe isothermal compressibility $\\kappa_T = -\\frac{1}{V}\\left(\\frac{\\partial V}{\\partial P}\\right)_T \\to \\infty$ diverges. Compressing the gas simply transfers particles from excited states into the zero-volume condensate without changing pressure.\n\n<h4>2. Heat Capacity Across the Transition</h4>\nThe heat capacity is:\n$$C_V(T) = \\begin{cases} \\frac{15}{4} k_B \\zeta(5/2) \\left( \\frac{m k_B T}{2\\pi \\hbar^2} \\right)^{3/2} V \\propto T^{3/2} & \\text{for } T < T_c \\\\ \\frac{3}{2} N k_B \\left[ 1 + 0.231 \\left( \\frac{T_c}{T} \\right)^{3/2} + \\dots \\right] & \\text{for } T > T_c \\end{cases}$$\nAt $T = T_c$, $C_V$ reaches a sharp peak with value $C_V(T_c) \\approx 1.925 N k_B$, exhibiting a cusp that marks a continuous third-order thermodynamic transition in the ideal gas (and a famous logarithmic $\\lambda$-peak in interacting Liquid Helium)."
        },
        {
          "id": "sec-5-9",
          "number": "\u00a75.9",
          "heading": "Thermodynamic Properties of Diatomic Molecules",
          "simulation": "equipartition-dof-sim",
          "content": "The thermal properties of a diatomic gas (such as $N_2, O_2, CO$) depend on the quantum excitation of rotational and vibrational molecular levels.\n\n<h4>1. Molecular Rotational Partition Function</h4>\nTreating the diatomic molecule as a rigid rotor with moment of inertia $I = \\mu_m r_0^2$:\n$$E_J = \\frac{\\hbar^2}{2I} J(J + 1) = k_B \\Theta_{\\text{rot}} J(J + 1), \\quad J = 0, 1, 2, \\dots$$\nwhere $\\Theta_{\\text{rot}} \\equiv \\frac{\\hbar^2}{2 I k_B}$ is the **characteristic rotational temperature** (typically $2\\text{ K}$ to $85\\text{ K}$).\nThe degeneracy of each rotational level is $g_J = 2J + 1$:\n$$z_{\\text{rot}} = \\sum_{J=0}^\\infty (2J + 1) e^{-J(J+1) \\Theta_{\\text{rot}} / T}$$\nFor $T \\gg \\Theta_{\\text{rot}}$ (room temperature for most gases), the sum can be approximated by an integral:\n$$z_{\\text{rot}} \\approx \\int_0^\\infty (2J + 1) e^{-J(J+1) \\Theta_{\\text{rot}} / T} dJ = \\frac{T}{\\sigma \\Theta_{\\text{rot}}}$$\nwhere $\\sigma$ is the symmetry number ($\\sigma = 2$ for homonuclear $N_2$, $\\sigma = 1$ for heteronuclear $CO$).\nThe rotational heat capacity in this high-temperature limit is $C_V^{\\text{rot}} = R$.\n\n<h4>2. Molecular Vibrational Partition Function</h4>\nTreated as a 1D harmonic oscillator with vibrational frequency $\\omega$:\n$$\\Theta_{\\text{vib}} \\equiv \\frac{\\hbar \\omega}{k_B}$$\nFor typical molecules, $\\Theta_{\\text{vib}} \\sim 1,000\\text{ K}$ to $3,000\\text{ K}$ (e.g., $N_2$: $\\Theta_{\\text{vib}} = 3,374\\text{ K}$).\n$$z_{\\text{vib}} = \\frac{e^{-\\Theta_{\\text{vib}} / 2T}}{1 - e^{-\\Theta_{\\text{vib}} / T}}$$\n$$C_V^{\\text{vib}} = R \\left( \\frac{\\Theta_{\\text{vib}}}{T} \\right)^2 \\frac{e^{\\Theta_{\\text{vib}}/T}}{(e^{\\Theta_{\\text{vib}}/T} - 1)^2}$$\nAt room temperature ($300\\text{ K} \\ll \\Theta_{\\text{vib}}$), vibrational modes are frozen into their quantum ground state."
        },
        {
          "id": "sec-5-10",
          "number": "\u00a75.10",
          "heading": "Nuclear Spin Effects in Diatomic Molecules: Ortho- and Para-Hydrogen",
          "simulation": "equipartition-dof-sim",
          "content": "In a homonuclear diatomic molecule like Hydrogen ($H_2$), quantum statistics of the two identical atomic nuclei imposes strict selection rules on molecular rotation!\n\n<h4>1. Nuclear Spin States of Hydrogen ($H_2$)</h4>\nEach proton has nuclear spin $I = 1/2$ (fermion). The two proton spins couple to give total nuclear spin $I_{\\text{tot}} \\in \\{0, 1\\}$:\n<ul>\n  <li><strong>Para-Hydrogen ($I_{\\text{tot}} = 0$, Nuclear Singlet):</strong>\n  $$\\chi_{\\text{para}} = \\frac{1}{\\sqrt{2}}(|\\uparrow\\downarrow\\rangle - |\\downarrow\\uparrow\\rangle) \\quad (1\\text{ antisymmetric nuclear spin state})$$\n  </li>\n  <li><strong>Ortho-Hydrogen ($I_{\\text{tot}} = 1$, Nuclear Triplet):</strong>\n  $$\\chi_{\\text{ortho}} \\in \\left\\{ |\\uparrow\\uparrow\\rangle, \\, \\frac{|\\uparrow\\downarrow\\rangle + |\\downarrow\\uparrow\\rangle}{\\sqrt{2}}, \\, |\\downarrow\\downarrow\\rangle \\right\\} \\quad (3\\text{ symmetric nuclear spin states})$$\n  </li>\n</ul>\n\n<h4>2. Total Wavefunction Symmetry Requirement</h4>\nBecause protons are fermions, the total molecular wavefunction must be **antisymmetric** under the exchange of the two protons:\n$$\\Psi_{\\text{total}} = \\psi_{\\text{trans}} \\times \\psi_{\\text{vib}} \\times \\psi_{\\text{rot}} \\times \\chi_{\\text{spin}}$$\nThe spatial exchange of the two nuclei is equivalent to an inversion: $\\mathbf{r} \\to -\\mathbf{r}$, which multiplies the rotational spherical harmonic $Y_{JM}(\\theta, \\phi)$ by $(-1)^J$:\n<ul>\n  <li>Even $J$ ($J = 0, 2, 4, \\dots$): Symmetric rotational state ($(-1)^J = +1$).</li>\n  <li>Odd $J$ ($J = 1, 3, 5, \\dots$): Antisymmetric rotational state ($(-1)^J = -1$).</li>\n</ul>\nTo make $\\Psi_{\\text{total}}$ antisymmetric:\n<ol>\n  <li><strong>Para-Hydrogen:</strong> Antisymmetric spin state $\\implies$ Must have **EVEN rotational levels only** ($J = 0, 2, 4, \\dots$). Ground state energy $E_0 = 0$ ($J=0$).</li>\n  <li><strong>Ortho-Hydrogen:</strong> Symmetric spin state $\\implies$ Must have **ODD rotational levels only** ($J = 1, 3, 5, \\dots$). Lowest state is $J=1$ with energy $E_1 = 2 k_B \\Theta_{\\text{rot}}$.</li>\n</ol>\n\n<h4>3. The High-Temperature 3:1 Equilibrium Ratio</h4>\nAt room temperature ($T \\gg \\Theta_{\\text{rot}} \\approx 85\\text{ K}$), all nuclear spin states are equally populated. The equilibrium ratio is given by their nuclear spin statistical weights:\n$$\\frac{\\text{Ortho}}{\\text{Para}} = \\frac{g_{\\text{ortho}}}{g_{\\text{para}}} = \\frac{3}{1} = 75\\% \\text{ Ortho}, \\quad 25\\% \\text{ Para}$$\nWhen hydrogen is cooled to liquid temperature ($20\\text{ K}$) without a catalyst, conversion from ortho ($J=1$) to para ($J=0$) is extraordinarily slow (taking weeks) because it requires an electron-nuclear spin-flip. Catalysts (activated carbon, ferric oxide) are added to speed conversion and prevent boil-off in liquid hydrogen rocket propellant storage!"
        }
      ],
      "problems": [
        {
          "id": "prob-5-1",
          "difficulty": "Medium",
          "title": "Bose-Einstein Critical Condensation Temperature in Rubidium-87",
          "question": "In a magneto-optical trap, $N = 2.0 \\times 10^5$ atoms of Rubidium-87 ($^{87}\\text{Rb}$, atomic mass $m = 1.443 \\times 10^{-25}\\text{ kg}$, boson with integer nuclear spin) are confined to an effective volume $V = 1.0 \\times 10^{-15}\\text{ m}^3$. (a) Calculate the critical temperature $T_c$ for Bose-Einstein condensation. (b) If the gas is cooled to $T = 0.5 T_c$, determine the number of atoms $N_0$ condensed into the zero-momentum ground state.",
          "steps": [
            {
              "title": "Step 1: Compute particle number density",
              "math": "$$n = \\frac{N}{V} = \\frac{2.0 \\times 10^5}{1.0 \\times 10^{-15}\\text{ m}^3} = 2.0 \\times 10^{20}\\text{ atoms/m}^3$$",
              "explanation": "This gives the atomic number density in the ultra-cold optical trap."
            },
            {
              "title": "Step 2: Calculate the critical condensation temperature T_c",
              "math": "$$T_c = \\frac{2\\pi \\hbar^2}{m k_B} \\left(\\frac{n}{\\zeta(3/2)}\\right)^{2/3}$$\n$$\\frac{2\\pi \\hbar^2}{m k_B} = \\frac{2\\pi (1.055 \\times 10^{-34})^2}{(1.443 \\times 10^{-25})(1.381 \\times 10^{-23})} = 3.511 \\times 10^{-20}\\text{ K}\\cdot\\text{m}^2$$\n$$\\left(\\frac{2.0 \\times 10^{20}}{2.6124}\\right)^{2/3} = (7.656 \\times 10^{19})^{2/3} = 1.803 \\times 10^{13}\\text{ m}^{-2}$$\n$$T_c = (3.511 \\times 10^{-20}) \\times (1.803 \\times 10^{13}) = 6.33 \\times 10^{-7}\\text{ K} = 633\\text{ nK}$$",
              "explanation": "The critical temperature is approximately $633$ nanokelvin, matching typical laboratory laser-cooling experiments."
            },
            {
              "title": "Step 3: Calculate the condensate fraction at T = 0.5 T_c",
              "math": "$$\\frac{N_0}{N} = 1 - \\left(\\frac{T}{T_c}\\right)^{3/2} = 1 - (0.5)^{3/2} = 1 - 0.3536 = 0.6464$$\n$$N_0 = 0.6464 \\times (2.0 \\times 10^5) \\approx 129,280\\text{ atoms}$$",
              "explanation": "At half the transition temperature, nearly $65\\%$ of all atoms occupy the single zero-momentum ground state, forming a macroscopic quantum matter wave."
            }
          ]
        },
        {
          "id": "prob-5-2",
          "difficulty": "Hard",
          "title": "Solar Surface Temperature from Planck Radiation Law",
          "question": "The total solar irradiance (solar constant) measured at Earth's distance ($R = 1.496 \\times 10^{11}\\text{ m}$) outside the atmosphere is $S_0 = 1361\\text{ W/m}^2$. The Sun's radius is $R_\\odot = 6.963 \\times 10^8\\text{ m}$. (a) Using the Stefan-Boltzmann law, calculate the effective surface temperature $T_{\\text{eff}}$ of the Sun. (b) Using Wien's displacement law, calculate the peak wavelength $\\lambda_{\\max}$ of solar radiation and determine what color of the spectrum it corresponds to.",
          "steps": [
            {
              "title": "Step 1: Relate solar constant to surface emissive power",
              "math": "$$L_\\odot = 4\\pi R^2 S_0 = 4\\pi (1.496 \\times 10^{11}\\text{ m})^2 (1361\\text{ W/m}^2) = 3.828 \\times 10^{26}\\text{ W}$$\n$$J_{\\text{surf}} = \\frac{L_\\odot}{4\\pi R_\\odot^2} = \\frac{3.828 \\times 10^{26}}{4\\pi (6.963 \\times 10^8)^2} = 6.284 \\times 10^7\\text{ W/m}^2$$",
              "explanation": "This gives the total radiant flux emitted per square meter of the solar photosphere."
            },
            {
              "title": "Step 2: Compute effective surface temperature via Stefan-Boltzmann law",
              "math": "$$J_{\\text{surf}} = \\sigma T_{\\text{eff}}^4 \\implies T_{\\text{eff}} = \\left( \\frac{6.284 \\times 10^7\\text{ W/m}^2}{5.6704 \\times 10^{-8}\\text{ W/(m}^2\\cdot\\text{K}^4)} \\right)^{1/4}$$\n$$T_{\\text{eff}} = (1.1082 \\times 10^{15})^{1/4} \\approx 5,772\\text{ K}$$",
              "explanation": "The derived effective blackbody temperature of the Sun is $5,772\\text{ K}$."
            },
            {
              "title": "Step 3: Determine peak wavelength via Wien's law",
              "math": "$$\\lambda_{\\max} = \\frac{2.8978 \\times 10^{-3}\\text{ m}\\cdot\\text{K}}{5,772\\text{ K}} = 5.020 \\times 10^{-7}\\text{ m} = 502\\text{ nm}$$",
              "explanation": "The peak wavelength is $502\\text{ nm}$, which lies directly in the green portion of the visible spectrum, where human vision has maximum optical sensitivity."
            }
          ]
        },
        {
          "id": "prob-5-3",
          "difficulty": "Hard",
          "title": "Landau Critical Velocity in Liquid Helium-4",
          "question": "In liquid $^4\\text{He}$ at $T = 1.0\\text{ K}$, the roton excitation parameters are $\\Delta / k_B = 8.65\\text{ K}$, $p_0 / \\hbar = 1.92 \\times 10^{10}\\text{ m}^{-1}$, and effective mass $\\mu = 0.16 m_4$, where $m_4 = 6.646 \\times 10^{-27}\\text{ kg}$. (a) Calculate the Landau critical velocity $v_c = \\Delta / p_0$. (b) Explain why macroscopic superfluid flow in wide pipes breaks down at much lower velocities ($v \\sim 1\\text{ cm/s}$) than $v_c$.",
          "steps": [
            {
              "title": "Step 1: Compute roton gap energy and momentum",
              "math": "$$\\Delta = (8.65\\text{ K}) \\times (1.381 \\times 10^{-23}\\text{ J/K}) = 1.195 \\times 10^{-22}\\text{ J}$$\n$$p_0 = \\hbar (1.92 \\times 10^{10}\\text{ m}^{-1}) = (1.055 \\times 10^{-34}) \\times (1.92 \\times 10^{10}) = 2.026 \\times 10^{-24}\\text{ kg}\\cdot\\text{m/s}$$",
              "explanation": "These are the energy gap and characteristic momentum of the roton minimum."
            },
            {
              "title": "Step 2: Calculate Landau critical velocity",
              "math": "$$v_c = \\frac{\\Delta}{p_0} = \\frac{1.195 \\times 10^{-22}\\text{ J}}{2.026 \\times 10^{-24}\\text{ kg}\\cdot\\text{m/s}} = 58.98\\text{ m/s} \\approx 59\\text{ m/s}$$",
              "explanation": "This is the microscopic Landau critical velocity required to create single roton excitations."
            },
            {
              "title": "Step 3: Explain the discrepancy in wide channels",
              "math": "$$\\text{In macroscopic channels: } v_{\\text{crit}}^{\\text{vortex}} = \\frac{\\hbar}{m_4 R} \\ln\\left(\\frac{R}{a_0}\\right) \\ll v_c$$",
              "explanation": "In pipes wider than a few nanometers, dissipation is initiated not by creating individual rotons, but by nucleating quantized vortex lines and vortex rings (Feynman-Onsager vortex creation), which have a much lower energy per unit momentum, reducing the practical critical velocity to millimeters per second."
            }
          ]
        }
      ]
    },
    {
      "number": 6,
      "title": "The Condensed State",
      "leadSummary": "Solids at low and high temperatures, Debye interpolation, thermal expansion and Gr\u00fcneisen parameter, quantum Bose and Fermi liquids, and electronic band spectra of metals and dielectrics.",
      "sections": [
        {
          "id": "sec-6-1",
          "number": "\u00a76.1",
          "heading": "Solids at Low and High Temperature",
          "simulation": "debye-vs-einstein-cv-sim",
          "content": "The thermal properties of solids reflect the quantum mechanical excitation of their crystal lattice vibrations and conduction electrons.\n\n<h4>1. The High-Temperature Classical Limit</h4>\nAt high temperatures ($T \\gg \\Theta_D$), the thermal energy $k_B T$ is far larger than the quantum energy of any lattice vibration ($\\hbar \\omega_D$).\nAll $3N$ normal modes of vibration are fully excited. According to the classical equipartition theorem, each harmonic mode contributes $k_B T$ of internal energy:\n$$U \\to 3 N k_B T \\implies C_V \\to 3 N k_B = 3 R \\approx 24.94\\text{ J/(mol}\\cdot\\text{K)}$$\nThis is the classical Dulong-Petit value, which is identical for all non-magnetic monoatomic solids regardless of chemical identity.\n\n<h4>2. The Low-Temperature Quantum Freezing</h4>\nAs temperature drops below the Debye temperature ($T \\ll \\Theta_D$), thermal energy becomes insufficient to excite high-frequency vibrational modes:\n<ul>\n  <li>In **Insulators:** Lattice acoustic phonons dominate completely, yielding the universal cubic temperature dependence:\n  $$C_V^{\\text{insulator}}(T) = A T^3 = \\frac{12\\pi^4}{5} N k_B \\left( \\frac{T}{\\Theta_D} \\right)^3$$\n  </li>\n  <li>In **Metals:** Both conduction electrons and acoustic phonons contribute:\n  $$C_V^{\\text{metal}}(T) = \\gamma T + A T^3$$\n  Plotting $C_V / T$ versus $T^2$ yields a straight line whose $y$-intercept gives the electronic Sommerfeld constant $\\gamma$ and whose slope gives the lattice coefficient $A$!</li>\n</ul>"
        },
        {
          "id": "sec-6-2",
          "number": "\u00a76.2",
          "heading": "Debye's Interpolation Formula and Universal Heat Capacity Scaling",
          "simulation": "debye-vs-einstein-cv-sim",
          "content": "Peter Debye synthesized the low- and high-temperature regimes into a single, universal dimensionless function that describes virtually all insulating crystals.\n\n<h4>1. The Debye Function ($D(y)$)</h4>\nThe internal energy of a crystal is expressed in terms of the **Debye Function**:\n$$U(T) = 3 N k_B T \\, D\\left( \\frac{\\Theta_D}{T} \\right)$$\nwhere $y = \\Theta_D / T$, and $D(y)$ is defined as:\n$$D(y) \\equiv \\frac{3}{y^3} \\int_0^y \\frac{x^3 dx}{e^x - 1}$$\n\n<h4>2. The Universal Specific Heat Expression</h4>\nDifferentiating $U(T)$ gives the molar heat capacity:\n$$C_V(T) = 3 R \\left[ 4 D(y) - \\frac{3 y}{e^y - 1} \\right] = 9 R \\left( \\frac{T}{\\Theta_D} \\right)^3 \\int_0^{\\Theta_D / T} \\frac{x^4 e^x dx}{(e^x - 1)^2}$$\nNotice that:\n<blockquote>\nThe reduced heat capacity $\\frac{C_V}{3R}$ is a <strong>universal function</strong> of the single dimensionless ratio $\\frac{T}{\\Theta_D}$.\n</blockquote>\nWhen experimental specific heat data for diverse solids (lead with $\\Theta_D = 105\\text{ K}$, copper with $\\Theta_D = 343\\text{ K}$, and diamond with $\\Theta_D = 2230\\text{ K}$) are plotted against $T / \\Theta_D$, all data points collapse onto the exact same theoretical Debye master curve!"
        },
        {
          "id": "sec-6-3",
          "number": "\u00a76.3",
          "heading": "Thermal Expansion of Solids and the Gr\u00fcneisen Parameter",
          "simulation": "transport-coefficients-sim",
          "content": "Why does a solid expand when heated? A perfectly harmonic crystal lattice ($V(x) = \\frac{1}{2}c x^2$) **does not expand at all**! Thermal expansion is a direct consequence of **anharmonicity** in the interatomic potential.\n\n<h4>1. Proof that Harmonic Oscillators Have Zero Thermal Expansion</h4>\nConsider an atom displaced by $x$ from its equilibrium position. In a symmetric parabolic potential $V(x) = c x^2$:\n$$\\langle x \\rangle = \\frac{\\int_{-\\infty}^\\infty x e^{-\\beta c x^2} dx}{\\int_{-\\infty}^\\infty e^{-\\beta c x^2} dx} = 0$$\nBecause the potential is strictly symmetric, the thermal average displacement $\\langle x \\rangle$ vanishes identically at all temperatures. A purely harmonic crystal never expands!\n\n<h4>2. Anharmonicity and Thermal Expansion</h4>\nThe real interatomic potential (such as the Lennard-Jones potential) is asymmetric, resisting compression more strongly than expansion.\nExpanding about the minimum:\n$$V(x) = c x^2 - g x^3 - f x^4, \\quad (g, f > 0)$$\nTreating the cubic anharmonic term $-g x^3$ as a perturbation:\n$$e^{-\\beta V(x)} \\approx e^{-\\beta c x^2} (1 + \\beta g x^3)$$\n$$\\langle x \\rangle = \\frac{\\int_{-\\infty}^\\infty x e^{-\\beta c x^2} (1 + \\beta g x^3) dx}{\\int_{-\\infty}^\\infty e^{-\\beta c x^2} dx} = \\frac{\\beta g \\int_{-\\infty}^\\infty x^4 e^{-\\beta c x^2} dx}{\\int_{-\\infty}^\\infty e^{-\\beta c x^2} dx} = \\frac{3 g}{4 c^2} k_B T$$\nThe average interatomic spacing increases linearly with temperature: $\\langle x \\rangle \\propto T$.\n\n<h4>3. The Gr\u00fcneisen Parameter and Equation of State</h4>\nAs a solid expands ($V$ increases), phonon vibrational frequencies shift downward:\n$$\\gamma_G \\equiv -\\frac{d\\ln \\omega_D}{d\\ln V} = -\\frac{V}{\\omega_D}\\frac{d\\omega_D}{dV}$$\nwhere $\\gamma_G$ is the dimensionless **Gr\u00fcneisen Parameter** (typically $\\sim 1$ to $2$).\nThe volumetric thermal expansion coefficient $\\beta_V = \\frac{1}{V}\\left(\\frac{\\partial V}{\\partial T}\\right)_P$ satisfies the **Mie-Gr\u00fcneisen Equation**:\n$$\\beta_V = \\frac{\\gamma_G C_V}{V K_T}$$\nwhere $K_T$ is the isothermal bulk modulus.\nThermal expansion is directly proportional to lattice heat capacity: as $T \\to 0$, $\\beta_V \\propto T^3$, vanishing at absolute zero in agreement with the Third Law of Thermodynamics."
        },
        {
          "id": "sec-6-4",
          "number": "\u00a76.4",
          "heading": "Quantum Liquids with Bose-Type Spectrum",
          "simulation": "liquid-helium-lambda-sim",
          "content": "Liquid Helium-4 ($^4\\text{He}$) is the prototypical strongly interacting **quantum Bose liquid**.\n\n<h4>1. The Elementary Excitation Spectrum</h4>\nLev Landau (1941) proposed that elementary excitations in Liquid $^4\\text{He}$ are single quasiparticles whose energy $\\epsilon(p)$ depends continuously on momentum $p$:\n<ol>\n  <li><strong>Phonon Branch ($p/\\hbar < 0.6\\text{ \u00c5}^{-1}$):</strong> Longitudinal sound waves with linear dispersion:\n  $$\\epsilon(p) = c_s p$$\n  where $c_s \\approx 238\\text{ m/s}$ is the speed of first sound.</li>\n  <li><strong>Maxon Peak ($p/\\hbar \\approx 1.1\\text{ \u00c5}^{-1}$):</strong> A local maximum around $\\epsilon / k_B \\approx 14\\text{ K}$.</li>\n  <li><strong>Roton Minimum ($p/\\hbar \\approx 1.92\\text{ \u00c5}^{-1}$):</strong> A parabolic dip around characteristic momentum $p_0$:\n  $$\\epsilon(p) \\approx \\Delta + \\frac{(p - p_0)^2}{2\\mu}$$\n  with energy gap $\\Delta / k_B \\approx 8.65\\text{ K}$, $p_0 / \\hbar \\approx 1.92\\text{ \u00c5}^{-1}$, and effective mass $\\mu \\approx 0.16 m_4$.</li>\n</ol>\n\n<h4>2. Bogoliubov's Microscopic Theory</h4>\nNikolay Bogoliubov (1947) derived this excitation spectrum microscopically for a weakly interacting Bose gas using canonical transformation:\n$$E(k) = \\sqrt{\\epsilon_k^2 + 2 n U_0 \\epsilon_k}$$\nwhere $\\epsilon_k = \\frac{\\hbar^2 k^2}{2m}$ is the free-particle kinetic energy, and $U_0 = \\frac{4\\pi \\hbar^2 a}{m}$ is the repulsive contact interaction.\n<ul>\n  <li>At low wavevector ($k \\to 0$): $E(k) \\approx \\sqrt{2 n U_0 \\frac{\\hbar^2 k^2}{2m}} = \\hbar c_s k$, reproducing linear sound waves with sound speed $c_s = \\sqrt{n U_0 / m}$.</li>\n  <li>At high wavevector ($k \\to \\infty$): $E(k) \\to \\epsilon_k + n U_0$, recovering quadratic single-particle behavior.</li>\n</ul>"
        },
        {
          "id": "sec-6-5",
          "number": "\u00a76.5",
          "heading": "Quantum Liquids with Fermi-Type Spectrum (Landau Fermi Liquid Theory)",
          "simulation": "fermi-surface-sphere-sim",
          "content": "Liquid Helium-3 ($^3\\text{He}$, a spin-1/2 fermion) and conduction electrons in heavy fermion metals represent strongly interacting **quantum Fermi liquids**.\n\n<h4>1. Landau Fermi Liquid Theory</h4>\nLev Landau (1956) recognized that strong repulsive interactions do not destroy the sharpness of the Fermi surface.\nInstead, there is a continuous one-to-one correspondence between the eigenstates of a non-interacting Fermi gas and the low-energy excitations of the interacting system, called **quasiparticles**.\n\n<h4>2. Quasiparticles and Effective Mass ($m^*$)</h4>\nA quasiparticle is an individual fermion dressed by a surrounding cloud of interactions with other particles.\nNear the Fermi surface, the quasiparticle energy is:\n$$\\epsilon(p) \\approx \\epsilon_F + v_F^* (p - p_F) = \\epsilon_F + \\frac{p_F}{m^*} (p - p_F)$$\nwhere $m^*$ is the **quasiparticle effective mass**:\n$$\\frac{m^*}{m} = 1 + \\frac{1}{3} F_1^s$$\nIn Liquid $^3\\text{He}$ at ambient pressure, $m^* \\approx 3.0 m_3$; under high pressure ($30\\text{ bar}$), $m^* \\approx 6.0 m_3$.\n\n<h4>3. Quasiparticle Lifetime Divergence</h4>\nBy Pauli exclusion, scattering between quasiparticles near the Fermi surface requires both initial and final states to lie within energy $k_B T$ of $\\epsilon_F$.\nThe scattering rate scales as $\\Gamma \\propto (k_B T)^2 + (\\epsilon - \\epsilon_F)^2$.\nTherefore, the quasiparticle lifetime diverges at low temperatures:\n$$\\tau \\propto \\frac{1}{T^2} \\to \\infty$$\nAs $T \\to 0$, quasiparticles become infinitely well-defined quantum excitations, explaining why free-electron models work remarkably well in metals!"
        },
        {
          "id": "sec-6-6",
          "number": "\u00a76.6",
          "heading": "The Electronic Spectra of Metals",
          "simulation": "fermi-surface-sphere-sim",
          "content": "In a crystalline metal, conduction electrons move in the periodic electrostatic potential created by the ionic lattice: $V(\\mathbf{r} + \\mathbf{R}) = V(\\mathbf{r})$.\n\n<h4>1. Bloch's Theorem and Energy Bands</h4>\nAccording to Bloch's Theorem, single-electron wavefunctions are plane waves modulated by the lattice periodicity:\n$$\\psi_{n\\mathbf{k}}(\\mathbf{r}) = e^{i\\mathbf{k}\\cdot\\mathbf{r}} u_{n\\mathbf{k}}(\\mathbf{r}), \\quad u_{n\\mathbf{k}}(\\mathbf{r} + \\mathbf{R}) = u_{n\\mathbf{k}}(\\mathbf{r})$$\nThe energy spectrum separates into continuous **energy bands** $\\epsilon_n(\\mathbf{k})$ separated by **bandgaps**.\n\n<h4>2. The Electronic Hallmark of a Metal</h4>\nA material is an electrical conductor (metal) if and only if:\n<blockquote>\nThe highest occupied energy level\u2014the <strong>Fermi Energy $\\epsilon_F$</strong>\u2014lies inside a partially filled electronic energy band.\n</blockquote>\nBecause empty quantum states are available immediately above $\\epsilon_F$ with infinitesimal energy spacing $d\\epsilon \\to 0$:\n<ul>\n  <li>An applied electric field $\\mathbf{E}$ accelerates electrons into adjacent unoccupied states, producing a net electrical current (Drude-Sommerfeld conductivity $\\sigma = \\frac{n e^2 \\tau}{m^*}$).</li>\n  <li>The density of states at the Fermi level $g(\\epsilon_F) > 0$ is finite, yielding linear electronic heat capacity $C_V = \\gamma T$ and Pauli paramagnetism $\\chi = \\mu_B^2 g(\\epsilon_F)$.</li>\n</ul>"
        },
        {
          "id": "sec-6-7",
          "number": "\u00a76.7",
          "heading": "The Electronic Spectra of Solid Dielectrics",
          "simulation": "transport-coefficients-sim",
          "content": "In solid dielectrics (insulators and semiconductors), the Fermi level lies within a forbidden energy gap separating filled and empty electronic bands.\n\n<h4>1. Band Structure of Insulators and Semiconductors</h4>\nIn an intrinsic dielectric at $T = 0\\text{ K}$:\n<ul>\n  <li>The **Valence Band** is $100\\%$ completely filled with electrons.</li>\n  <li>The **Conduction Band** is completely empty.</li>\n  <li>They are separated by a finite **Bandgap** $E_g$:\n  $$E_g = \\epsilon_c - \\epsilon_v$$\n  For semiconductors, $E_g \\lesssim 3\\text{ eV}$ (Silicon: $1.12\\text{ eV}$, Gallium Arsenide: $1.42\\text{ eV}$). For insulators, $E_g \\gtrsim 4\\text{ eV}$ (Diamond: $5.47\\text{ eV}$, Silicon Dioxide: $9.0\\text{ eV}$).</li>\n</ul>\n\n<h4>2. Thermal Carrier Generation and Chemical Potential</h4>\nAt finite temperature $T > 0$, thermal fluctuations promote electrons across the bandgap into the conduction band, leaving empty states (**holes**) in the valence band.\nThe electron density $n$ and hole density $p$ are:\n$$n = N_c e^{-(\\epsilon_c - \\mu)/k_B T}, \\quad p = N_v e^{-(\\mu - \\epsilon_v)/k_B T}$$\nwhere $N_c = 2\\left(\\frac{m_e^* k_B T}{2\\pi \\hbar^2}\\right)^{3/2}$ and $N_v = 2\\left(\\frac{m_h^* k_B T}{2\\pi \\hbar^2}\\right)^{3/2}$ are the effective densities of states.\nEquating $n = p = n_i$ (intrinsic semiconductor):\n$$n_i = \\sqrt{N_c N_v} \\exp\\left( -\\frac{E_g}{2 k_B T} \\right)$$\n$$\\mu = \\frac{\\epsilon_c + \\epsilon_v}{2} + \\frac{3}{4} k_B T \\ln\\left( \\frac{m_h^*}{m_e^*} \\right)$$\nThe Fermi level in an intrinsic dielectric sits essentially at the mid-gap!\nElectrical conductivity grows exponentially with temperature: $\\sigma(T) \\propto e^{-E_g / (2 k_B T)}$, in stark contrast to metals where resistance increases with temperature due to phonon scattering."
        }
      ],
      "problems": [
        {
          "id": "prob-6-1",
          "difficulty": "Medium",
          "title": "Debye Temperature and Maximum Lattice Frequency in Diamond",
          "question": "For diamond, the atomic number density is $n = 1.76 \\times 10^{29}\\text{ atoms/m}^3$ and the average sound speed is $v_s = 1.20 \\times 10^4\\text{ m/s}$. (a) Calculate the Debye cutoff frequency $\\omega_D$ and Debye temperature $\\Theta_D$. (b) Explain why diamond feels remarkably cold to the touch and has a high thermal conductivity at room temperature ($300\\text{ K}$).",
          "steps": [
            {
              "title": "Step 1: Calculate the Debye cutoff frequency",
              "math": "$$\\omega_D = v_s (6\\pi^2 n)^{1/3} = (1.20 \\times 10^4\\text{ m/s}) [6\\pi^2 (1.76 \\times 10^{29}\\text{ m}^{-3})]^{1/3}$$\n$$6\\pi^2 (1.76 \\times 10^{29}) = 1.042 \\times 10^{31} \\implies (1.042 \\times 10^{31})^{1/3} = 2.184 \\times 10^{10}\\text{ m}^{-1}$$\n$$\\omega_D = (1.20 \\times 10^4) \\times (2.184 \\times 10^{10}) = 2.621 \\times 10^{14}\\text{ rad/s}$$",
              "explanation": "This is the maximum lattice vibrational frequency in diamond."
            },
            {
              "title": "Step 2: Determine the Debye temperature",
              "math": "$$\\Theta_D = \\frac{\\hbar \\omega_D}{k_B} = \\frac{(1.055 \\times 10^{-34}\\text{ J}\\cdot\\text{s})(2.621 \\times 10^{14}\\text{ s}^{-1})}{1.381 \\times 10^{-23}\\text{ J/K}} = 2,002\\text{ K}$$",
              "explanation": "Because $\\Theta_D \\approx 2,000\\text{ K}$ is far above room temperature ($300\\text{ K}$), diamond is deeply in the quantum regime at room temperature."
            },
            {
              "title": "Step 3: Analyze thermal properties at 300 K",
              "math": "$$\\frac{T}{\\Theta_D} = \\frac{300}{2002} \\approx 0.15 \\ll 1$$\n$$C_V \\approx \\frac{12\\pi^4}{5} R \\left(\\frac{300}{2002}\\right)^3 \\approx 6.1\\text{ J/(mol}\\cdot\\text{K)} \\ll 3R (24.9\\text{ J/(mol}\\cdot\\text{K)})$$",
              "explanation": "Because phonon modes are largely frozen, phonon-phonon Umklapp scattering is exceptionally rare, giving diamond an extraordinarily large phonon mean free path and the highest room-temperature thermal conductivity of any bulk solid ($k \\approx 2200\\text{ W/(m}\\cdot\\text{K)}$)."
            }
          ]
        },
        {
          "id": "prob-6-2",
          "difficulty": "Hard",
          "title": "Intrinsic Carrier Concentration and Fermi Level in Silicon",
          "question": "Silicon has an indirect bandgap $E_g = 1.12\\text{ eV}$ at $T = 300\\text{ K}$. The effective masses of electrons and holes are $m_e^* = 1.08 m_0$ and $m_h^* = 0.56 m_0$. (a) Calculate the intrinsic carrier density $n_i$ at $300\\text{ K}$. (b) Determine the offset of the Fermi level from the mid-gap position.",
          "steps": [
            {
              "title": "Step 1: Compute effective densities of states N_c and N_v",
              "math": "$$N_c = 2\\left(\\frac{2\\pi m_e^* k_B T}{h^2}\\right)^{3/2} = 2.81 \\times 10^{25}\\text{ m}^{-3}$$\n$$N_v = 2\\left(\\frac{2\\pi m_h^* k_B T}{h^2}\\right)^{3/2} = 1.04 \\times 10^{25}\\text{ m}^{-3}$$",
              "explanation": "These are the effective quantum densities of states of the conduction and valence bands."
            },
            {
              "title": "Step 2: Calculate intrinsic carrier concentration n_i",
              "math": "$$n_i = \\sqrt{N_c N_v} e^{-E_g / (2 k_B T)}$$\n$$\\sqrt{N_c N_v} = \\sqrt{(2.81 \\times 10^{25})(1.04 \\times 10^{25})} = 1.71 \\times 10^{25}\\text{ m}^{-3}$$\n$$\\frac{E_g}{2 k_B T} = \\frac{1.12\\text{ eV}}{2 (0.02585\\text{ eV})} = 21.663$$\n$$n_i = (1.71 \\times 10^{25}) \\times e^{-21.663} = (1.71 \\times 10^{25})(3.91 \\times 10^{-10}) = 6.69 \\times 10^{15}\\text{ m}^{-3} = 6.69 \\times 10^9\\text{ cm}^{-3}$$",
              "explanation": "At room temperature, only roughly one atom in ten trillion is thermally ionized."
            },
            {
              "title": "Step 3: Calculate Fermi level offset from mid-gap",
              "math": "$$\\Delta \\mu = \\mu - \\frac{\\epsilon_c + \\epsilon_v}{2} = \\frac{3}{4} k_B T \\ln\\left(\\frac{m_h^*}{m_e^*}\\right) = \\frac{3}{4} (0.02585\\text{ eV}) \\ln\\left(\\frac{0.56}{1.08}\\right) = -0.0127\\text{ eV} = -12.7\\text{ meV}$$",
              "explanation": "Because holes are lighter than electrons ($m_h^* < m_e^*$), the Fermi level is shifted downward by $12.7\\text{ meV}$ below the exact center of the bandgap."
            }
          ]
        },
        {
          "id": "prob-6-3",
          "difficulty": "Hard",
          "title": "Gr\u00fcneisen Parameter and Thermal Expansion of Aluminum",
          "question": "For Aluminum, the molar heat capacity at $T = 300\\text{ K}$ is $C_V = 24.2\\text{ J/(mol}\\cdot\\text{K)}$, molar volume is $V_m = 1.00 \\times 10^{-5}\\text{ m}^3\\text{/mol}$, isothermal bulk modulus is $K_T = 76\\text{ GPa}$, and the linear thermal expansion coefficient is $\\alpha_L = 23.1 \\times 10^{-6}\\text{ K}^{-1}$. (a) Calculate the volumetric thermal expansion coefficient $\\beta_V = 3\\alpha_L$. (b) Use the Mie-Gr\u00fcneisen relation to calculate the Gr\u00fcneisen parameter $\\gamma_G$.",
          "steps": [
            {
              "title": "Step 1: Compute volumetric thermal expansion coefficient",
              "math": "$$\\beta_V = 3 \\alpha_L = 3 \\times (23.1 \\times 10^{-6}\\text{ K}^{-1}) = 6.93 \\times 10^{-5}\\text{ K}^{-1}$$",
              "explanation": "For an isotropic cubic crystal, volumetric expansion is three times linear expansion."
            },
            {
              "title": "Step 2: Solve Mie-Gr\u00fcneisen equation for gamma_G",
              "math": "$$\\beta_V = \\frac{\\gamma_G C_V}{V_m K_T} \\implies \\gamma_G = \\frac{\\beta_V V_m K_T}{C_V}$$\n$$\\gamma_G = \\frac{(6.93 \\times 10^{-5}\\text{ K}^{-1}) \\times (1.00 \\times 10^{-5}\\text{ m}^3\\text{/mol}) \\times (76 \\times 10^9\\text{ Pa})}{24.2\\text{ J/(mol}\\cdot\\text{K)}}$$\n$$\\gamma_G = \\frac{52.668}{24.2} \\approx 2.18$$",
              "explanation": "The Gr\u00fcneisen parameter of Aluminum is $2.18$, which is characteristic of anharmonic acoustic phonon shifts in fcc metals."
            }
          ]
        }
      ]
    },
    {
      "number": 7,
      "title": "Transport Phenomena and Phase Transition",
      "leadSummary": "Boltzmann transport equation, H-theorem and arrow of time, mean free path, viscosity, thermal conductivity, diffusion, Brownian motion, Ehrenfest phase transition classification, Clausius-Clapeyron, and mean-field Ising model.",
      "sections": [
        {
          "id": "sec-7-1",
          "number": "\u00a77.1",
          "heading": "The Boltzmann Transport Equation",
          "simulation": "mean-free-path-transport-sim",
          "content": "When a system is driven out of thermodynamic equilibrium by temperature gradients, concentration gradients, or external electromagnetic fields, transport phenomena occur. The fundamental microscopic equation governing non-equilibrium statistical mechanics is the **Boltzmann Transport Equation** (Ludwig Boltzmann, 1872).\n\n<h4>1. Phase-Space Distribution Function ($f(\\mathbf{r}, \\mathbf{p}, t)$)</h4>\nLet $f(\\mathbf{r}, \\mathbf{p}, t) \\, d^3\\mathbf{r} \\, d^3\\mathbf{p}$ be the number of particles in physical volume element $d^3\\mathbf{r}$ with momenta in $d^3\\mathbf{p}$ at time $t$.\nIn the absence of interparticle collisions, particles flow smoothly through phase space according to Hamilton's equations $\\mathbf{v} = \\mathbf{p}/m$ and $\\dot{\\mathbf{p}} = \\mathbf{F}$:\n$$f(\\mathbf{r} + \\mathbf{v}\\delta t, \\, \\mathbf{p} + \\mathbf{F}\\delta t, \\, t + \\delta t) = f(\\mathbf{r}, \\mathbf{p}, t)$$\n\n<h4>2. The Collision Term</h4>\nInterparticle collisions abruptly scatter particles into and out of the phase-space volume element:\n$$f(\\mathbf{r} + \\mathbf{v}\\delta t, \\, \\mathbf{p} + \\mathbf{F}\\delta t, \\, t + \\delta t) - f(\\mathbf{r}, \\mathbf{p}, t) = \\left( \\frac{\\partial f}{\\partial t} \\right)_{\\text{coll}} \\delta t$$\nExpanding the left side in a first-order Taylor series yields the **Boltzmann Transport Equation**:\n$$\\frac{\\partial f}{\\partial t} + \\mathbf{v} \\cdot \\boldsymbol{\\nabla}_{\\mathbf{r}} f + \\frac{\\mathbf{F}}{m} \\cdot \\boldsymbol{\\nabla}_{\\mathbf{v}} f = \\left( \\frac{\\partial f}{\\partial t} \\right)_{\\text{coll}}$$\n\n<h4>3. The Relaxation-Time (BGK) Approximation</h4>\nBecause the exact non-linear collision integral involves 5-dimensional integration over collision cross sections, Bhatnagar, Gross, and Krook (1954) introduced the widely used **Relaxation-Time Approximation**:\n$$\\left( \\frac{\\partial f}{\\partial t} \\right)_{\\text{coll}} \\approx -\\frac{f(\\mathbf{r}, \\mathbf{v}, t) - f_0(\\mathbf{v})}{\\tau}$$\nwhere $f_0(\\mathbf{v})$ is the local equilibrium Maxwell-Boltzmann distribution, and $\\tau$ is the characteristic collision relaxation time. Any local perturbation decays exponentially back to equilibrium as $e^{-t/\\tau}$."
        },
        {
          "id": "sec-7-2",
          "number": "\u00a77.2",
          "heading": "The Boltzmann H-Theorem and the Arrow of Time",
          "simulation": "mean-free-path-transport-sim",
          "content": "How can time-reversible microscopic Newtonian mechanics give rise to irreversible macroscopic thermodynamics (Second Law)? Ludwig Boltzmann solved this with his famous **H-Theorem** (1872).\n\n<h4>1. Definition of the $H$-Function</h4>\nBoltzmann defined the functional $H(t)$ for a gas with velocity distribution $f(\\mathbf{v}, t)$:\n$$H(t) \\equiv \\int f(\\mathbf{v}, t) \\ln f(\\mathbf{v}, t) \\, d^3\\mathbf{v}$$\nBecause statistical entropy is $S = -k_B \\int f \\ln f \\, d^3\\mathbf{v}$, Boltzmann's $H$-function is directly proportional to negative entropy:\n$$S(t) = -k_B H(t) + \\text{constant}$$\n\n<h4>2. Derivation of $dH/dt \\le 0$</h4>\nUsing the exact binary collision integral and the principle of detailed balance (microscopic time-reversibility of collisions $\\mathbf{v}_1, \\mathbf{v}_2 \\leftrightarrow \\mathbf{v}_1', \\mathbf{v}_2'$):\n$$\\frac{dH}{dt} = -\\frac{1}{4} \\int \\dots \\int (f_1' f_2' - f_1 f_2) \\ln\\left( \\frac{f_1' f_2'}{f_1 f_2} \\right) \\sigma \\, |\\mathbf{v}_1 - \\mathbf{v}_2| \\, d\\Omega \\, d^3\\mathbf{v}_1 \\, d^3\\mathbf{v}_2$$\nBecause for any positive numbers $x, y$, the inequality $(x - y)\\ln(x/y) \\ge 0$ holds strictly (being zero if and only if $x = y$):\n$$\\frac{dH}{dt} \\le 0 \\iff \\frac{dS}{dt} \\ge 0$$\n<blockquote>\n<strong>Boltzmann's H-Theorem:</strong> The functional $H(t)$ decreases monotonically over time until the gas attains the Maxwell-Boltzmann distribution, where $dH/dt = 0$. Consequently, macroscopic entropy can never decrease!\n</blockquote>\n\n<h4>3. Resolution of Historical Paradoxes</h4>\n<ul>\n  <li><strong>Loschmidt's Time-Reversal Paradox (Umkehreinwand):</strong> If Newton's laws are time-reversible, reversing all velocities should make entropy decrease. Resolution: The H-theorem assumes the <em>Molecular Chaos Hypothesis</em> (Sto\u00dfzahlansatz)\u2014that velocities of colliding particles are uncorrelated <em>before</em> collision. Reversing velocities introduces exquisite fine-tuned microscopic correlations that violate this hypothesis.</li>\n  <li><strong>Zermelo's Recurrence Paradox (Wiederkehreinwand):</strong> Poincar\u00e9's theorem states any bounded mechanical system must return arbitrarily close to its initial microstate. Resolution: For $10^{23}$ particles, the Poincar\u00e9 recurrence time is $\\sim 10^{10^{23}}$ years\u2014vastly longer than the age of the universe!</li>\n</ul>"
        },
        {
          "id": "sec-7-3",
          "number": "\u00a77.3",
          "heading": "Mean Free Path and Kinetic Collision Theory",
          "simulation": "mean-free-path-transport-sim",
          "content": "The **mean free path** $\\lambda$ is the average distance traversed by a molecule between successive collisions.\n\n<h4>1. Collision Cross Section</h4>\nModel gas molecules as hard spheres of diameter $d$. A collision occurs whenever the centers of two molecules approach within distance $d$.\nThe collision cross section is the area of a disk of radius $d$:\n$$\\sigma = \\pi d^2$$\n\n<h4>2. Derivation of the Mean Free Path</h4>\nIf a molecule moves with relative speed $\\bar{v}_{\\text{rel}}$, in time $\\Delta t$ its collision cross section sweeps out a cylinder of volume $\\Delta V = \\sigma \\bar{v}_{\\text{rel}} \\Delta t$.\nIf the number density of scatterers is $n = N/V$, the number of collisions is:\n$$\\Delta N_{\\text{coll}} = n \\Delta V = n \\pi d^2 \\bar{v}_{\\text{rel}} \\Delta t$$\nFor a thermal gas, the average relative speed between two randomly oriented molecules is $\\bar{v}_{\\text{rel}} = \\sqrt{2} \\bar{v}$.\nThe collision frequency is:\n$$\\nu_{\\text{coll}} = \\frac{\\Delta N_{\\text{coll}}}{\\Delta t} = \\sqrt{2} \\pi n d^2 \\bar{v}$$\nThe mean free path is the average speed divided by collision frequency:\n$$\\lambda = \\frac{\\bar{v}}{\\nu_{\\text{coll}}} = \\frac{1}{\\sqrt{2} \\pi n d^2}$$\nUsing the ideal gas law $P = n k_B T$:\n$$\\lambda = \\frac{k_B T}{\\sqrt{2} \\pi d^2 P}$$\nAt room temperature and atmospheric pressure for air ($d \\approx 3.7\\text{ \u00c5}$):\n$$\\lambda \\approx 68\\text{ nm}$$\nMolecules travel hundreds of times their own diameter between collisions!"
        },
        {
          "id": "sec-7-4",
          "number": "\u00a77.4",
          "heading": "Viscosity, Thermal Conductivity, and Diffusion in Gases",
          "simulation": "transport-coefficients-sim",
          "content": "The kinetic theory of transport explains how molecules transport momentum (viscosity), energy (thermal conductivity), and mass (diffusion).\n\n<h4>1. Dynamic Viscosity ($\\eta$): Momentum Transport</h4>\nConsider a gas with a shear flow velocity gradient $\\frac{du_x}{dy}$. Molecules crossing plane $y$ from a mean free path distance $\\pm \\lambda$ carry momentum $m u_x(y \\pm \\lambda)$.\nThe shear stress is:\n$$\\tau_{xy} = -\\frac{1}{3} n m \\bar{v} \\lambda \\frac{du_x}{dy} = -\\eta \\frac{du_x}{dy}$$\n$$\\eta = \\frac{1}{3} \\rho \\bar{v} \\lambda = \\frac{1}{3} (n m) \\bar{v} \\left( \\frac{1}{\\sqrt{2} \\pi n d^2} \\right) = \\frac{m \\bar{v}}{3 \\sqrt{2} \\pi d^2} = \\frac{\\sqrt{m k_B T}}{3 \\pi^{3/2} d^2}$$\n<blockquote>\n<strong>Maxwell's Paradox:</strong> Notice that density $n$ cancels out completely!\nThe viscosity of a dilute gas is <strong>completely independent of pressure and density</strong>!\n$$\\left(\\frac{\\partial \\eta}{\\partial P}\\right)_T = 0$$\nFurthermore, gas viscosity increases with temperature ($\\eta \\propto \\sqrt{T}$), unlike liquids whose viscosity drops with temperature.\n</blockquote>\n\n<h4>2. Thermal Conductivity ($\\kappa$): Heat Energy Transport</h4>\nFor a temperature gradient $\\frac{dT}{dz}$, molecules transport thermal energy $c_v m T$:\n$$J_q = -\\kappa \\frac{dT}{dz}, \\quad \\kappa = \\frac{1}{3} n c_v m \\bar{v} \\lambda = \\frac{1}{3} C_V \\rho \\bar{v} \\lambda = \\frac{c_v \\sqrt{m k_B T}}{3 \\pi^{3/2} d^2}$$\nThermal conductivity is also independent of gas pressure.\n\n<h4>3. Self-Diffusion Coefficient ($D$): Mass Transport</h4>\nFor a concentration gradient $\\frac{dn}{dz}$, the particle flux is given by Fick's Law:\n$$J_N = -D \\frac{dn}{dz}, \\quad D = \\frac{1}{3} \\bar{v} \\lambda = \\frac{2}{3 \\pi^{3/2} d^2} \\frac{\\sqrt{k_B T / m}}{n} \\propto \\frac{T^{3/2}}{P}$$\nUnlike viscosity, diffusion is inversely proportional to pressure."
        },
        {
          "id": "sec-7-5",
          "number": "\u00a77.5",
          "heading": "Electrical Conductivity and the Drude-Sommerfeld Model",
          "simulation": "transport-coefficients-sim",
          "content": "Electrical conduction in metals is the transport of electric charge under an applied electric field $\\mathbf{E}$.\n\n<h4>1. The Drude-Sommerfeld Conductivity Formula</h4>\nIn an electric field $\\mathbf{E}$, conduction electrons experience acceleration $\\mathbf{a} = -e\\mathbf{E}/m^*$.\nCollisions with lattice phonons and impurities randomize momentum with relaxation time $\\tau$.\nThe steady-state drift velocity is:\n$$\\mathbf{v}_d = -\\frac{e \\tau}{m^*} \\mathbf{E}$$\nThe electric current density is given by Ohm's Law $\\mathbf{J} = -n e \\mathbf{v}_d = \\sigma \\mathbf{E}$, yielding:\n$$\\sigma = \\frac{n e^2 \\tau}{m^*}$$\n\n<h4>2. The Wiedemann-Franz Law and Lorenz Number</h4>\nIn metals, conduction electrons transport both electric charge and thermal heat.\nThe electronic thermal conductivity is $\\kappa_{\\text{el}} = \\frac{1}{3} C_V^{\\text{el}} v_F^2 \\tau$.\nUsing the Sommerfeld linear electronic heat capacity $C_V^{\\text{el}} = \\frac{\\pi^2}{2} n k_B (T / T_F)$:\n$$\\kappa_{\\text{el}} = \\frac{1}{3} \\left( \\frac{\\pi^2}{2} \\frac{n k_B^2 T}{\\epsilon_F} \\right) \\left( \\frac{2\\epsilon_F}{m^*} \\right) \\tau = \\frac{\\pi^2 n k_B^2 T \\tau}{3 m^*}$$\nDividing thermal conductivity $\\kappa$ by electrical conductivity $\\sigma$:\n$$\\frac{\\kappa}{\\sigma T} = \\frac{\\pi^2}{3} \\left( \\frac{k_B}{e} \\right)^2 \\equiv L$$\nThis is the celebrated **Wiedemann-Franz Law** (1853).\nThe ratio is a universal physical constant known as the **Lorenz Number**:\n$$L = \\frac{\\pi^2}{3} \\left( \\frac{k_B}{e} \\right)^2 = 2.443 \\times 10^{-8}\\text{ W}\\cdot\\Omega\\text{/K}^2$$\nThis universal constant holds remarkably across copper, silver, gold, and aluminum at room temperature!"
        },
        {
          "id": "sec-7-6",
          "number": "\u00a77.6",
          "heading": "Brownian Motion and the Langevin Stochastic Equation",
          "simulation": "mean-free-path-transport-sim",
          "content": "Brownian motion\u2014the irregular, ceaseless jigging of microscopic particles suspended in a fluid\u2014provided the definitive experimental proof of the physical reality of atoms.\n\n<h4>1. The Langevin Equation (Paul Langevin, 1908)</h4>\nA microscopic particle of mass $m$ and radius $a$ suspended in a fluid experiences two forces:\n<ol>\n  <li>A macroscopic viscous drag force: $-\\gamma v = -6\\pi \\eta a v$ (Stokes' Law).</li>\n  <li>A fluctuating, stochastic force $\\xi(t)$ due to billions of thermal molecular collisions.</li>\n</ol>\nThe stochastic equation of motion is:\n$$m \\frac{dv}{dt} = -\\gamma v + \\xi(t)$$\nThe random force has zero mean $\\langle \\xi(t) \\rangle = 0$ and is $\\delta$-correlated in time (white noise):\n$$\\langle \\xi(t) \\xi(t') \\rangle = 2 \\gamma k_B T \\, \\delta(t - t')$$\nThis is the **Fluctuation-Dissipation Theorem**: the microscopic random kicks $\\xi(t)$ and the macroscopic viscous drag $\\gamma$ have the exact same physical origin (collisions with fluid molecules).\n\n<h4>2. Derivation of Mean Squared Displacement (Einstein, 1905)</h4>\nMultiplying the Langevin equation by $x$ and taking ensemble averages:\n$$m \\left\\langle x \\frac{dv}{dt} \\right\\rangle = -\\gamma \\langle x v \\rangle + \\langle x \\xi \\rangle$$\nUsing $\\frac{d}{dt}(x^2) = 2xv$ and $\\frac{d}{dt}(xv) = v^2 + x\\frac{dv}{dt}$:\n$$\\frac{m}{2} \\frac{d^2}{dt^2} \\langle x^2 \\rangle - m \\langle v^2 \\rangle = -\\frac{\\gamma}{2} \\frac{d}{dt} \\langle x^2 \\rangle$$\nBy the equipartition theorem, $m \\langle v^2 \\rangle = k_B T$. In the overdamped regime ($t \\gg m/\\gamma$):\n$$\\frac{\\gamma}{2} \\frac{d}{dt} \\langle x^2 \\rangle = k_B T \\implies \\frac{d}{dt} \\langle x^2 \\rangle = \\frac{2 k_B T}{\\gamma}$$\nIntegrating over time:\n$$\\langle x^2(t) \\rangle = 2 D t$$\nwhere $D$ is the **Einstein Diffusion Coefficient**:\n$$D = \\frac{k_B T}{\\gamma} = \\frac{k_B T}{6\\pi \\eta a}$$\nBy tracking the displacement $\\langle x^2 \\rangle$ of gamboge particles under a microscope, Jean Perrin measured Boltzmann's constant $k_B$ and calculated Avogadro's number $N_A$, winning the 1926 Nobel Prize for proving the reality of atoms!"
        },
        {
          "id": "sec-7-7",
          "number": "\u00a77.7",
          "heading": "Thermodynamic Classification of Phase Transitions and Clausius-Clapeyron",
          "simulation": "phase-diagram-clapeyron-sim",
          "content": "Phase transitions are transformations between distinct macroscopic states of matter (phases) as external thermodynamic parameters ($T, P, B$) vary.\n\n<h4>1. The Ehrenfest Classification of Phase Transitions</h4>\nPaul Ehrenfest (1933) classified phase transitions by the lowest order derivative of Gibbs free energy $G(T, P)$ that exhibits a mathematical discontinuity:\n<ul>\n  <li><strong>First-Order Phase Transitions:</strong> Discontinuity in the <em>first derivatives</em> of $G$:\n  $$\\Delta S = -\\Delta \\left(\\frac{\\partial G}{\\partial T}\\right)_P \\ne 0, \\quad \\Delta V = \\Delta \\left(\\frac{\\partial G}{\\partial P}\\right)_T \\ne 0$$\n  Characterized by a non-zero **Latent Heat** $L = T \\Delta S$ and a discontinuous change in volume/density $\\Delta V$. Examples: Ice melting, water boiling, sublimation.</li>\n  <li><strong>Second-Order (Continuous) Phase Transitions:</strong> First derivatives are continuous (no latent heat: $\\Delta S = 0, \\Delta V = 0$), but <em>second derivatives</em> diverge or jump discontinuously:\n  $$C_P = -T \\left(\\frac{\\partial^2 G}{\\partial T^2}\\right)_P, \\quad \\kappa_T = -\\frac{1}{V} \\left(\\frac{\\partial^2 G}{\\partial P^2}\\right)_T, \\quad \\alpha = \\frac{1}{V} \\frac{\\partial^2 G}{\\partial T \\partial P}$$\n  Examples: Ferromagnetic Curie transition, superconductor-normal transition in zero field, superfluid He-II $\\lambda$-transition.</li>\n</ul>\n\n<h4>2. The Clausius-Clapeyron Equation</h4>\nAlong a first-order phase coexistence boundary curve $P(T)$, the two phases ($1$ and $2$) have identical chemical potential:\n$$dG_1 = dG_2 \\implies -S_1 dT + V_1 dP = -S_2 dT + V_2 dP$$\nRearranging gives the **Clausius-Clapeyron Equation**:\n$$\\frac{dP}{dT} = \\frac{S_2 - S_1}{V_2 - V_1} = \\frac{\\Delta S}{\\Delta V} = \\frac{L}{T \\Delta V}$$\nBecause ice expands when freezing ($V_{\\text{ice}} > V_{\\text{water}} \\implies \\Delta V < 0$), the melting curve of ice has a negative slope ($dP/dT < 0$), allowing ice skates to glide on a thin liquid layer!"
        },
        {
          "id": "sec-7-8",
          "number": "\u00a77.8",
          "heading": "Mean-Field Theory of the Ising Model",
          "simulation": "ising-model-monte-carlo-sim",
          "content": "The **Ising Model** (Ernst Ising and Wilhelm Lenz, 1925) is the preeminent model for studying collective phenomena, ferromagnetism, and continuous phase transitions.\n\n<h4>1. The Microscopic Ising Hamiltonian</h4>\nConsider a crystal lattice where each site $i$ has an Ising spin $s_i = \\pm 1$ (spin up or spin down):\n$$H = -J \\sum_{\\langle i, j \\rangle} s_i s_j - h \\sum_i s_i$$\nwhere $J > 0$ is the ferromagnetic exchange coupling between nearest neighbors $\\langle i, j \\rangle$, and $h = g \\mu_B B$ is an external magnetic field.\n\n<h4>2. Weiss Molecular Mean-Field Approximation</h4>\nIn Mean-Field Theory (MFT), we approximate the fluctuating neighbor spins $s_j$ by their average expectation value $\\langle s \\rangle = m$ (the **order parameter**):\n$$s_i s_j = (s_i - m + m)(s_j - m + m) \\approx m s_i + m s_j - m^2$$\nFor a lattice with coordination number $z$ (number of nearest neighbors per site):\n$$H_{\\text{MF}} = -\\sum_i s_i (h + z J m) + \\frac{1}{2} N z J m^2 = -\\sum_i s_i h_{\\text{eff}} + \\frac{1}{2} N z J m^2$$\nwhere $h_{\\text{eff}} = h + z J m$ is the effective **Weiss molecular field**.\n\n<h4>3. The Self-Consistency Equation</h4>\nThe single-spin partition function is:\n$$z_1 = e^{\\beta h_{\\text{eff}}} + e^{-\\beta h_{\\text{eff}}} = 2 \\cosh(\\beta h_{\\text{eff}})$$\nThe average magnetization per site is:\n$$m = \\langle s_i \\rangle = \\frac{e^{\\beta h_{\\text{eff}}} - e^{-\\beta h_{\\text{eff}}}}{z_1} = \\tanh(\\beta h_{\\text{eff}})$$\nSubstituting $h_{\\text{eff}} = h + z J m$:\n$$m = \\tanh\\left( \\frac{z J m + h}{k_B T} \\right)$$\n\n<h4>4. Spontaneous Magnetization and Critical Curie Temperature</h4>\nIn zero external field ($h = 0$):\n$$m = \\tanh\\left( \\frac{z J}{k_B T} m \\right)$$\nFor high temperatures, the slope of $\\tanh(x)$ at $x = 0$ is less than $1$: the only solution is $m = 0$ (paramagnetic phase).\nA non-trivial solution ($m \\ne 0$) emerges when the slope at the origin exceeds $1$:\n$$\\left.\\frac{d}{dm}\\tanh\\left(\\frac{z J m}{k_B T}\\right)\\right|_{m=0} = \\frac{z J}{k_B T} > 1$$\nThis defines the **Curie Transition Temperature**:\n$$T_c = \\frac{z J}{k_B}$$\nFor $T < T_c$, spontaneous symmetry breaking occurs: the spins spontaneously align into a macroscopic ferromagnet with $m \\propto (T_c - T)^{1/2}$ near $T_c$ (mean-field critical exponent $\\beta = 1/2$)."
        }
      ],
      "problems": [
        {
          "id": "prob-7-1",
          "difficulty": "Medium",
          "title": "Mean Free Path and Collision Rate in the Upper Atmosphere",
          "question": "At an altitude of $100\\text{ km}$ in the thermosphere (the K\u00e1rm\u00e1n line), the atmospheric pressure is $P = 0.032\\text{ Pa}$ and the temperature is $T = 200\\text{ K}$. Assuming an effective molecular diameter $d = 3.7 \\times 10^{-10}\\text{ m}$ and average molecular mass $m = 4.8 \\times 10^{-26}\\text{ kg}$ (diatomic nitrogen). (a) Calculate the number density $n$ and the mean free path $\\lambda$. (b) Determine the average collision frequency $\\nu_{\\text{coll}}$.",
          "steps": [
            {
              "title": "Step 1: Compute molecular number density",
              "math": "$$n = \\frac{P}{k_B T} = \\frac{0.032\\text{ Pa}}{(1.381 \\times 10^{-23}\\text{ J/K})(200\\text{ K})} = 1.159 \\times 10^{19}\\text{ molecules/m}^3$$",
              "explanation": "This establishes the molecular density at the edge of outer space."
            },
            {
              "title": "Step 2: Calculate mean free path",
              "math": "$$\\lambda = \\frac{1}{\\sqrt{2} \\pi n d^2} = \\frac{1}{\\sqrt{2}\\pi (1.159 \\times 10^{19}\\text{ m}^{-3})(3.7 \\times 10^{-10}\\text{ m})^2}$$\n$$\\lambda = \\frac{1}{1.414 \\times 3.1416 \\times 1.159 \\times 10^{19} \\times 1.369 \\times 10^{-19}} = \\frac{1}{7.050} = 0.1418\\text{ m} \\approx 14.2\\text{ cm}$$",
              "explanation": "At $100\\text{ km}$ altitude, the mean free path is over $14\\text{ centimeters}$, compared to $68\\text{ nanometers}$ at sea level. Aerodynamic continuum fluid mechanics breaks down, requiring Knudsen rarefied gas dynamics."
            },
            {
              "title": "Step 3: Determine mean speed and collision frequency",
              "math": "$$\\bar{v} = \\sqrt{\\frac{8 k_B T}{\\pi m}} = \\sqrt{\\frac{8 (1.381 \\times 10^{-23})(200)}{\\pi (4.8 \\times 10^{-26})}} = \\sqrt{\\frac{2.210 \\times 10^{-20}}{1.508 \\times 10^{-25}}} = \\sqrt{1.465 \\times 10^5} = 382.8\\text{ m/s}$$\n$$\\nu_{\\text{coll}} = \\frac{\\bar{v}}{\\lambda} = \\frac{382.8\\text{ m/s}}{0.1418\\text{ m}} \\approx 2,700\\text{ collisions/second}$$",
              "explanation": "Molecules collide only a few thousand times per second, compared to billions of collisions per second at sea level."
            }
          ]
        },
        {
          "id": "prob-7-2",
          "difficulty": "Hard",
          "title": "Perrin's Determination of Avogadro's Number via Brownian Motion",
          "question": "In a Brownian motion experiment, spherical colloidal particles of radius $a = 0.50\\,\\mu\\text{m}$ are suspended in water at $T = 293\\text{ K}$ (viscosity $\\eta = 1.00 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s}$). (a) Calculate the diffusion coefficient $D$. (b) If the observed root-mean-square displacement in the $x$-direction over time $t = 60\\text{ s}$ is $\\sqrt{\\langle x^2 \\rangle} = 7.18\\,\\mu\\text{m}$, calculate Boltzmann's constant $k_B$ and Avogadro's number $N_A = R / k_B$ (taking $R = 8.314\\text{ J/(mol}\\cdot\\text{K)}$).",
          "steps": [
            {
              "title": "Step 1: Express diffusion coefficient from experimental displacement",
              "math": "$$\\langle x^2 \\rangle = 2 D t \\implies D = \\frac{\\langle x^2 \\rangle}{2t} = \\frac{(7.18 \\times 10^{-6}\\text{ m})^2}{2 \\times (60\\text{ s})} = \\frac{5.155 \\times 10^{-11}\\text{ m}^2}{120\\text{ s}} = 4.296 \\times 10^{-13}\\text{ m}^2\\text{/s}$$",
              "explanation": "This gives the experimental diffusion coefficient of the microscopic colloidal particles."
            },
            {
              "title": "Step 2: Solve Einstein's relation for Boltzmann's constant",
              "math": "$$D = \\frac{k_B T}{6\\pi \\eta a} \\implies k_B = \\frac{6\\pi \\eta a D}{T}$$\n$$k_B = \\frac{6\\pi (1.00 \\times 10^{-3}\\text{ Pa}\\cdot\\text{s})(0.50 \\times 10^{-6}\\text{ m})(4.296 \\times 10^{-13}\\text{ m}^2\\text{/s})}{293\\text{ K}}$$\n$$k_B = \\frac{4.049 \\times 10^{-21}}{293} = 1.382 \\times 10^{-23}\\text{ J/K}$$",
              "explanation": "This directly yields Boltzmann's constant."
            },
            {
              "title": "Step 3: Calculate Avogadro's number",
              "math": "$$N_A = \\frac{R}{k_B} = \\frac{8.314\\text{ J/(mol}\\cdot\\text{K)}}{1.382 \\times 10^{-23}\\text{ J/K}} = 6.016 \\times 10^{23}\\text{ mol}^{-1}$$",
              "explanation": "The experimental measurement yields $N_A \\approx 6.02 \\times 10^{23}\\text{ mol}^{-1}$, proving that thermal fluctuations are caused by discrete microscopic atoms."
            }
          ]
        },
        {
          "id": "prob-7-3",
          "difficulty": "Hard",
          "title": "Clausius-Clapeyron Vapor Pressure and Boiling Point at Altitude",
          "question": "At atmospheric pressure ($P_0 = 1.013 \\times 10^5\\text{ Pa}$), water boils at $T_0 = 373.15\\text{ K}$ with latent heat of vaporization $L = 2.260 \\times 10^6\\text{ J/kg}$ (molar latent heat $L_m = 40.68\\text{ kJ/mol}$). At the summit of Mount Everest ($8,848\\text{ m}$), atmospheric pressure drops to $P = 3.37 \\times 10^4\\text{ Pa}$. (a) Assuming the vapor behaves as an ideal gas and $V_{\\text{vapor}} \\gg V_{\\text{liquid}}$, derive the integrated Clausius-Clapeyron equation. (b) Calculate the boiling point of water on Mount Everest.",
          "steps": [
            {
              "title": "Step 1: Approximate Clausius-Clapeyron equation for vapor",
              "math": "$$\\Delta V = V_{\\text{vapor}} - V_{\\text{liquid}} \\approx V_{\\text{vapor}} = \\frac{R T}{P}$$\n$$\\frac{dP}{dT} = \\frac{L_m}{T \\Delta V} = \\frac{L_m P}{R T^2} \\implies \\frac{dP}{P} = \\frac{L_m}{R} \\frac{dT}{T^2}$$",
              "explanation": "Because the volume of steam is over 1600 times greater than liquid water, liquid volume can be neglected."
            },
            {
              "title": "Step 2: Integrate between sea level and Mount Everest",
              "math": "$$\\int_{P_0}^P \\frac{dP'}{P'} = \\frac{L_m}{R} \\int_{T_0}^T \\frac{dT'}{T'^2} \\implies \\ln\\left(\\frac{P}{P_0}\\right) = -\\frac{L_m}{R} \\left( \\frac{1}{T} - \\frac{1}{T_0} \\right)$$\n$$\\frac{1}{T} = \\frac{1}{T_0} - \\frac{R}{L_m} \\ln\\left(\\frac{P}{P_0}\\right)$$",
              "explanation": "This gives the vapor pressure curve as a function of temperature."
            },
            {
              "title": "Step 3: Evaluate numerical boiling temperature",
              "math": "$$\\ln\\left(\\frac{P}{P_0}\\right) = \\ln\\left(\\frac{3.37 \\times 10^4}{1.013 \\times 10^5}\\right) = \\ln(0.3327) = -1.1006$$\n$$\\frac{R}{L_m} = \\frac{8.314\\text{ J/(mol}\\cdot\\text{K)}}{40,680\\text{ J/mol}} = 2.0438 \\times 10^{-4}\\text{ K}^{-1}$$\n$$\\frac{1}{T} = \\frac{1}{373.15} - (2.0438 \\times 10^{-4})(-1.1006) = 2.6799 \\times 10^{-3} + 2.2494 \\times 10^{-4} = 2.9048 \\times 10^{-3}\\text{ K}^{-1}$$\n$$T = \\frac{1}{2.9048 \\times 10^{-3}} = 344.25\\text{ K} \\approx 71.1^\\circ\\text{C}$$",
              "explanation": "On Mount Everest, water boils at only $71.1^\\circ\\text{C}$ ($160^\\circ\\text{F}$), illustrating the dramatic pressure dependence predicted by the Clausius-Clapeyron equation."
            }
          ]
        }
      ]
    }
  ]
};
