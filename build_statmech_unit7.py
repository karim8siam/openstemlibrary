# Build Script for Unit 7: Transport Phenomena and Phase Transition
import json

u7_sections = [
    {
        "id": "sec-7-1",
        "number": "§7.1",
        "heading": "The Boltzmann Transport Equation",
        "simulation": "mean-free-path-transport-sim",
        "content": """When a system is driven out of thermodynamic equilibrium by temperature gradients, concentration gradients, or external electromagnetic fields, transport phenomena occur. The fundamental microscopic equation governing non-equilibrium statistical mechanics is the **Boltzmann Transport Equation** (Ludwig Boltzmann, 1872).

<h4>1. Phase-Space Distribution Function ($f(\\mathbf{r}, \\mathbf{p}, t)$)</h4>
Let $f(\\mathbf{r}, \\mathbf{p}, t) \\, d^3\\mathbf{r} \\, d^3\\mathbf{p}$ be the number of particles in physical volume element $d^3\\mathbf{r}$ with momenta in $d^3\\mathbf{p}$ at time $t$.
In the absence of interparticle collisions, particles flow smoothly through phase space according to Hamilton's equations $\\mathbf{v} = \\mathbf{p}/m$ and $\\dot{\\mathbf{p}} = \\mathbf{F}$:
$$f(\\mathbf{r} + \\mathbf{v}\\delta t, \\, \\mathbf{p} + \\mathbf{F}\\delta t, \\, t + \\delta t) = f(\\mathbf{r}, \\mathbf{p}, t)$$

<h4>2. The Collision Term</h4>
Interparticle collisions abruptly scatter particles into and out of the phase-space volume element:
$$f(\\mathbf{r} + \\mathbf{v}\\delta t, \\, \\mathbf{p} + \\mathbf{F}\\delta t, \\, t + \\delta t) - f(\\mathbf{r}, \\mathbf{p}, t) = \\left( \\frac{\\partial f}{\\partial t} \\right)_{\\text{coll}} \\delta t$$
Expanding the left side in a first-order Taylor series yields the **Boltzmann Transport Equation**:
$$\\frac{\\partial f}{\\partial t} + \\mathbf{v} \\cdot \\boldsymbol{\\nabla}_{\\mathbf{r}} f + \\frac{\\mathbf{F}}{m} \\cdot \\boldsymbol{\\nabla}_{\\mathbf{v}} f = \\left( \\frac{\\partial f}{\\partial t} \\right)_{\\text{coll}}$$

<h4>3. The Relaxation-Time (BGK) Approximation</h4>
Because the exact non-linear collision integral involves 5-dimensional integration over collision cross sections, Bhatnagar, Gross, and Krook (1954) introduced the widely used **Relaxation-Time Approximation**:
$$\\left( \\frac{\\partial f}{\\partial t} \\right)_{\\text{coll}} \\approx -\\frac{f(\\mathbf{r}, \\mathbf{v}, t) - f_0(\\mathbf{v})}{\\tau}$$
where $f_0(\\mathbf{v})$ is the local equilibrium Maxwell-Boltzmann distribution, and $\\tau$ is the characteristic collision relaxation time. Any local perturbation decays exponentially back to equilibrium as $e^{-t/\\tau}$."""
    },
    {
        "id": "sec-7-2",
        "number": "§7.2",
        "heading": "The Boltzmann H-Theorem and the Arrow of Time",
        "simulation": "mean-free-path-transport-sim",
        "content": """How can time-reversible microscopic Newtonian mechanics give rise to irreversible macroscopic thermodynamics (Second Law)? Ludwig Boltzmann solved this with his famous **H-Theorem** (1872).

<h4>1. Definition of the $H$-Function</h4>
Boltzmann defined the functional $H(t)$ for a gas with velocity distribution $f(\\mathbf{v}, t)$:
$$H(t) \\equiv \\int f(\\mathbf{v}, t) \\ln f(\\mathbf{v}, t) \\, d^3\\mathbf{v}$$
Because statistical entropy is $S = -k_B \\int f \\ln f \\, d^3\\mathbf{v}$, Boltzmann's $H$-function is directly proportional to negative entropy:
$$S(t) = -k_B H(t) + \\text{constant}$$

<h4>2. Derivation of $dH/dt \\le 0$</h4>
Using the exact binary collision integral and the principle of detailed balance (microscopic time-reversibility of collisions $\\mathbf{v}_1, \\mathbf{v}_2 \\leftrightarrow \\mathbf{v}_1', \\mathbf{v}_2'$):
$$\\frac{dH}{dt} = -\\frac{1}{4} \\int \\dots \\int (f_1' f_2' - f_1 f_2) \\ln\\left( \\frac{f_1' f_2'}{f_1 f_2} \\right) \\sigma \\, |\\mathbf{v}_1 - \\mathbf{v}_2| \\, d\\Omega \\, d^3\\mathbf{v}_1 \\, d^3\\mathbf{v}_2$$
Because for any positive numbers $x, y$, the inequality $(x - y)\\ln(x/y) \\ge 0$ holds strictly (being zero if and only if $x = y$):
$$\\frac{dH}{dt} \\le 0 \\iff \\frac{dS}{dt} \\ge 0$$
<blockquote>
<strong>Boltzmann's H-Theorem:</strong> The functional $H(t)$ decreases monotonically over time until the gas attains the Maxwell-Boltzmann distribution, where $dH/dt = 0$. Consequently, macroscopic entropy can never decrease!
</blockquote>

<h4>3. Resolution of Historical Paradoxes</h4>
<ul>
  <li><strong>Loschmidt's Time-Reversal Paradox (Umkehreinwand):</strong> If Newton's laws are time-reversible, reversing all velocities should make entropy decrease. Resolution: The H-theorem assumes the <em>Molecular Chaos Hypothesis</em> (Stoßzahlansatz)—that velocities of colliding particles are uncorrelated <em>before</em> collision. Reversing velocities introduces exquisite fine-tuned microscopic correlations that violate this hypothesis.</li>
  <li><strong>Zermelo's Recurrence Paradox (Wiederkehreinwand):</strong> Poincaré's theorem states any bounded mechanical system must return arbitrarily close to its initial microstate. Resolution: For $10^{23}$ particles, the Poincaré recurrence time is $\\sim 10^{10^{23}}$ years—vastly longer than the age of the universe!</li>
</ul>"""
    },
    {
        "id": "sec-7-3",
        "number": "§7.3",
        "heading": "Mean Free Path and Kinetic Collision Theory",
        "simulation": "mean-free-path-transport-sim",
        "content": """The **mean free path** $\\lambda$ is the average distance traversed by a molecule between successive collisions.

<h4>1. Collision Cross Section</h4>
Model gas molecules as hard spheres of diameter $d$. A collision occurs whenever the centers of two molecules approach within distance $d$.
The collision cross section is the area of a disk of radius $d$:
$$\\sigma = \\pi d^2$$

<h4>2. Derivation of the Mean Free Path</h4>
If a molecule moves with relative speed $\\bar{v}_{\\text{rel}}$, in time $\\Delta t$ its collision cross section sweeps out a cylinder of volume $\\Delta V = \\sigma \\bar{v}_{\\text{rel}} \\Delta t$.
If the number density of scatterers is $n = N/V$, the number of collisions is:
$$\\Delta N_{\\text{coll}} = n \\Delta V = n \\pi d^2 \\bar{v}_{\\text{rel}} \\Delta t$$
For a thermal gas, the average relative speed between two randomly oriented molecules is $\\bar{v}_{\\text{rel}} = \\sqrt{2} \\bar{v}$.
The collision frequency is:
$$\\nu_{\\text{coll}} = \\frac{\\Delta N_{\\text{coll}}}{\\Delta t} = \\sqrt{2} \\pi n d^2 \\bar{v}$$
The mean free path is the average speed divided by collision frequency:
$$\\lambda = \\frac{\\bar{v}}{\\nu_{\\text{coll}}} = \\frac{1}{\\sqrt{2} \\pi n d^2}$$
Using the ideal gas law $P = n k_B T$:
$$\\lambda = \\frac{k_B T}{\\sqrt{2} \\pi d^2 P}$$
At room temperature and atmospheric pressure for air ($d \\approx 3.7\\text{ Å}$):
$$\\lambda \\approx 68\\text{ nm}$$
Molecules travel hundreds of times their own diameter between collisions!"""
    },
    {
        "id": "sec-7-4",
        "number": "§7.4",
        "heading": "Viscosity, Thermal Conductivity, and Diffusion in Gases",
        "simulation": "transport-coefficients-sim",
        "content": """The kinetic theory of transport explains how molecules transport momentum (viscosity), energy (thermal conductivity), and mass (diffusion).

<h4>1. Dynamic Viscosity ($\\eta$): Momentum Transport</h4>
Consider a gas with a shear flow velocity gradient $\\frac{du_x}{dy}$. Molecules crossing plane $y$ from a mean free path distance $\\pm \\lambda$ carry momentum $m u_x(y \\pm \\lambda)$.
The shear stress is:
$$\\tau_{xy} = -\\frac{1}{3} n m \\bar{v} \\lambda \\frac{du_x}{dy} = -\\eta \\frac{du_x}{dy}$$
$$\\eta = \\frac{1}{3} \\rho \\bar{v} \\lambda = \\frac{1}{3} (n m) \\bar{v} \\left( \\frac{1}{\\sqrt{2} \\pi n d^2} \\right) = \\frac{m \\bar{v}}{3 \\sqrt{2} \\pi d^2} = \\frac{\\sqrt{m k_B T}}{3 \\pi^{3/2} d^2}$$
<blockquote>
<strong>Maxwell's Paradox:</strong> Notice that density $n$ cancels out completely!
The viscosity of a dilute gas is <strong>completely independent of pressure and density</strong>!
$$\\left(\\frac{\\partial \\eta}{\\partial P}\\right)_T = 0$$
Furthermore, gas viscosity increases with temperature ($\\eta \\propto \\sqrt{T}$), unlike liquids whose viscosity drops with temperature.
</blockquote>

<h4>2. Thermal Conductivity ($\\kappa$): Heat Energy Transport</h4>
For a temperature gradient $\\frac{dT}{dz}$, molecules transport thermal energy $c_v m T$:
$$J_q = -\\kappa \\frac{dT}{dz}, \\quad \\kappa = \\frac{1}{3} n c_v m \\bar{v} \\lambda = \\frac{1}{3} C_V \\rho \\bar{v} \\lambda = \\frac{c_v \\sqrt{m k_B T}}{3 \\pi^{3/2} d^2}$$
Thermal conductivity is also independent of gas pressure.

<h4>3. Self-Diffusion Coefficient ($D$): Mass Transport</h4>
For a concentration gradient $\\frac{dn}{dz}$, the particle flux is given by Fick's Law:
$$J_N = -D \\frac{dn}{dz}, \\quad D = \\frac{1}{3} \\bar{v} \\lambda = \\frac{2}{3 \\pi^{3/2} d^2} \\frac{\\sqrt{k_B T / m}}{n} \\propto \\frac{T^{3/2}}{P}$$
Unlike viscosity, diffusion is inversely proportional to pressure."""
    },
    {
        "id": "sec-7-5",
        "number": "§7.5",
        "heading": "Electrical Conductivity and the Drude-Sommerfeld Model",
        "simulation": "transport-coefficients-sim",
        "content": """Electrical conduction in metals is the transport of electric charge under an applied electric field $\\mathbf{E}$.

<h4>1. The Drude-Sommerfeld Conductivity Formula</h4>
In an electric field $\\mathbf{E}$, conduction electrons experience acceleration $\\mathbf{a} = -e\\mathbf{E}/m^*$.
Collisions with lattice phonons and impurities randomize momentum with relaxation time $\\tau$.
The steady-state drift velocity is:
$$\\mathbf{v}_d = -\\frac{e \\tau}{m^*} \\mathbf{E}$$
The electric current density is given by Ohm's Law $\\mathbf{J} = -n e \\mathbf{v}_d = \\sigma \\mathbf{E}$, yielding:
$$\\sigma = \\frac{n e^2 \\tau}{m^*}$$

<h4>2. The Wiedemann-Franz Law and Lorenz Number</h4>
In metals, conduction electrons transport both electric charge and thermal heat.
The electronic thermal conductivity is $\\kappa_{\\text{el}} = \\frac{1}{3} C_V^{\\text{el}} v_F^2 \\tau$.
Using the Sommerfeld linear electronic heat capacity $C_V^{\\text{el}} = \\frac{\\pi^2}{2} n k_B (T / T_F)$:
$$\\kappa_{\\text{el}} = \\frac{1}{3} \\left( \\frac{\\pi^2}{2} \\frac{n k_B^2 T}{\\epsilon_F} \\right) \\left( \\frac{2\\epsilon_F}{m^*} \\right) \\tau = \\frac{\\pi^2 n k_B^2 T \\tau}{3 m^*}$$
Dividing thermal conductivity $\\kappa$ by electrical conductivity $\\sigma$:
$$\\frac{\\kappa}{\\sigma T} = \\frac{\\pi^2}{3} \\left( \\frac{k_B}{e} \\right)^2 \\equiv L$$
This is the celebrated **Wiedemann-Franz Law** (1853).
The ratio is a universal physical constant known as the **Lorenz Number**:
$$L = \\frac{\\pi^2}{3} \\left( \\frac{k_B}{e} \\right)^2 = 2.443 \\times 10^{-8}\\text{ W}\\cdot\\Omega\\text{/K}^2$$
This universal constant holds remarkably across copper, silver, gold, and aluminum at room temperature!"""
    },
    {
        "id": "sec-7-6",
        "number": "§7.6",
        "heading": "Brownian Motion and the Langevin Stochastic Equation",
        "simulation": "mean-free-path-transport-sim",
        "content": """Brownian motion—the irregular, ceaseless jigging of microscopic particles suspended in a fluid—provided the definitive experimental proof of the physical reality of atoms.

<h4>1. The Langevin Equation (Paul Langevin, 1908)</h4>
A microscopic particle of mass $m$ and radius $a$ suspended in a fluid experiences two forces:
<ol>
  <li>A macroscopic viscous drag force: $-\\gamma v = -6\\pi \\eta a v$ (Stokes' Law).</li>
  <li>A fluctuating, stochastic force $\\xi(t)$ due to billions of thermal molecular collisions.</li>
</ol>
The stochastic equation of motion is:
$$m \\frac{dv}{dt} = -\\gamma v + \\xi(t)$$
The random force has zero mean $\\langle \\xi(t) \\rangle = 0$ and is $\\delta$-correlated in time (white noise):
$$\\langle \\xi(t) \\xi(t') \\rangle = 2 \\gamma k_B T \\, \\delta(t - t')$$
This is the **Fluctuation-Dissipation Theorem**: the microscopic random kicks $\\xi(t)$ and the macroscopic viscous drag $\\gamma$ have the exact same physical origin (collisions with fluid molecules).

<h4>2. Derivation of Mean Squared Displacement (Einstein, 1905)</h4>
Multiplying the Langevin equation by $x$ and taking ensemble averages:
$$m \\left\\langle x \\frac{dv}{dt} \\right\\rangle = -\\gamma \\langle x v \\rangle + \\langle x \\xi \\rangle$$
Using $\\frac{d}{dt}(x^2) = 2xv$ and $\\frac{d}{dt}(xv) = v^2 + x\\frac{dv}{dt}$:
$$\\frac{m}{2} \\frac{d^2}{dt^2} \\langle x^2 \\rangle - m \\langle v^2 \\rangle = -\\frac{\\gamma}{2} \\frac{d}{dt} \\langle x^2 \\rangle$$
By the equipartition theorem, $m \\langle v^2 \\rangle = k_B T$. In the overdamped regime ($t \\gg m/\\gamma$):
$$\\frac{\\gamma}{2} \\frac{d}{dt} \\langle x^2 \\rangle = k_B T \\implies \\frac{d}{dt} \\langle x^2 \\rangle = \\frac{2 k_B T}{\\gamma}$$
Integrating over time:
$$\\langle x^2(t) \\rangle = 2 D t$$
where $D$ is the **Einstein Diffusion Coefficient**:
$$D = \\frac{k_B T}{\\gamma} = \\frac{k_B T}{6\\pi \\eta a}$$
By tracking the displacement $\\langle x^2 \\rangle$ of gamboge particles under a microscope, Jean Perrin measured Boltzmann's constant $k_B$ and calculated Avogadro's number $N_A$, winning the 1926 Nobel Prize for proving the reality of atoms!"""
    },
    {
        "id": "sec-7-7",
        "number": "§7.7",
        "heading": "Thermodynamic Classification of Phase Transitions and Clausius-Clapeyron",
        "simulation": "phase-diagram-clapeyron-sim",
        "content": """Phase transitions are transformations between distinct macroscopic states of matter (phases) as external thermodynamic parameters ($T, P, B$) vary.

<h4>1. The Ehrenfest Classification of Phase Transitions</h4>
Paul Ehrenfest (1933) classified phase transitions by the lowest order derivative of Gibbs free energy $G(T, P)$ that exhibits a mathematical discontinuity:
<ul>
  <li><strong>First-Order Phase Transitions:</strong> Discontinuity in the <em>first derivatives</em> of $G$:
  $$\\Delta S = -\\Delta \\left(\\frac{\\partial G}{\\partial T}\\right)_P \\ne 0, \\quad \\Delta V = \\Delta \\left(\\frac{\\partial G}{\\partial P}\\right)_T \\ne 0$$
  Characterized by a non-zero **Latent Heat** $L = T \\Delta S$ and a discontinuous change in volume/density $\\Delta V$. Examples: Ice melting, water boiling, sublimation.</li>
  <li><strong>Second-Order (Continuous) Phase Transitions:</strong> First derivatives are continuous (no latent heat: $\\Delta S = 0, \\Delta V = 0$), but <em>second derivatives</em> diverge or jump discontinuously:
  $$C_P = -T \\left(\\frac{\\partial^2 G}{\\partial T^2}\\right)_P, \\quad \\kappa_T = -\\frac{1}{V} \\left(\\frac{\\partial^2 G}{\\partial P^2}\\right)_T, \\quad \\alpha = \\frac{1}{V} \\frac{\\partial^2 G}{\\partial T \\partial P}$$
  Examples: Ferromagnetic Curie transition, superconductor-normal transition in zero field, superfluid He-II $\\lambda$-transition.</li>
</ul>

<h4>2. The Clausius-Clapeyron Equation</h4>
Along a first-order phase coexistence boundary curve $P(T)$, the two phases ($1$ and $2$) have identical chemical potential:
$$dG_1 = dG_2 \\implies -S_1 dT + V_1 dP = -S_2 dT + V_2 dP$$
Rearranging gives the **Clausius-Clapeyron Equation**:
$$\\frac{dP}{dT} = \\frac{S_2 - S_1}{V_2 - V_1} = \\frac{\\Delta S}{\\Delta V} = \\frac{L}{T \\Delta V}$$
Because ice expands when freezing ($V_{\\text{ice}} > V_{\\text{water}} \\implies \\Delta V < 0$), the melting curve of ice has a negative slope ($dP/dT < 0$), allowing ice skates to glide on a thin liquid layer!"""
    },
    {
        "id": "sec-7-8",
        "number": "§7.8",
        "heading": "Mean-Field Theory of the Ising Model",
        "simulation": "ising-model-monte-carlo-sim",
        "content": """The **Ising Model** (Ernst Ising and Wilhelm Lenz, 1925) is the preeminent model for studying collective phenomena, ferromagnetism, and continuous phase transitions.

<h4>1. The Microscopic Ising Hamiltonian</h4>
Consider a crystal lattice where each site $i$ has an Ising spin $s_i = \\pm 1$ (spin up or spin down):
$$H = -J \\sum_{\\langle i, j \\rangle} s_i s_j - h \\sum_i s_i$$
where $J > 0$ is the ferromagnetic exchange coupling between nearest neighbors $\\langle i, j \\rangle$, and $h = g \\mu_B B$ is an external magnetic field.

<h4>2. Weiss Molecular Mean-Field Approximation</h4>
In Mean-Field Theory (MFT), we approximate the fluctuating neighbor spins $s_j$ by their average expectation value $\\langle s \\rangle = m$ (the **order parameter**):
$$s_i s_j = (s_i - m + m)(s_j - m + m) \\approx m s_i + m s_j - m^2$$
For a lattice with coordination number $z$ (number of nearest neighbors per site):
$$H_{\\text{MF}} = -\\sum_i s_i (h + z J m) + \\frac{1}{2} N z J m^2 = -\\sum_i s_i h_{\\text{eff}} + \\frac{1}{2} N z J m^2$$
where $h_{\\text{eff}} = h + z J m$ is the effective **Weiss molecular field**.

<h4>3. The Self-Consistency Equation</h4>
The single-spin partition function is:
$$z_1 = e^{\\beta h_{\\text{eff}}} + e^{-\\beta h_{\\text{eff}}} = 2 \\cosh(\\beta h_{\\text{eff}})$$
The average magnetization per site is:
$$m = \\langle s_i \\rangle = \\frac{e^{\\beta h_{\\text{eff}}} - e^{-\\beta h_{\\text{eff}}}}{z_1} = \\tanh(\\beta h_{\\text{eff}})$$
Substituting $h_{\\text{eff}} = h + z J m$:
$$m = \\tanh\\left( \\frac{z J m + h}{k_B T} \\right)$$

<h4>4. Spontaneous Magnetization and Critical Curie Temperature</h4>
In zero external field ($h = 0$):
$$m = \\tanh\\left( \\frac{z J}{k_B T} m \\right)$$
For high temperatures, the slope of $\\tanh(x)$ at $x = 0$ is less than $1$: the only solution is $m = 0$ (paramagnetic phase).
A non-trivial solution ($m \\ne 0$) emerges when the slope at the origin exceeds $1$:
$$\\left.\\frac{d}{dm}\\tanh\\left(\\frac{z J m}{k_B T}\\right)\\right|_{m=0} = \\frac{z J}{k_B T} > 1$$
This defines the **Curie Transition Temperature**:
$$T_c = \\frac{z J}{k_B}$$
For $T < T_c$, spontaneous symmetry breaking occurs: the spins spontaneously align into a macroscopic ferromagnet with $m \\propto (T_c - T)^{1/2}$ near $T_c$ (mean-field critical exponent $\\beta = 1/2$)."""
    }
]

u7_problems = [
    {
        "id": "prob-7-1",
        "difficulty": "Medium",
        "title": "Mean Free Path and Collision Rate in the Upper Atmosphere",
        "question": "At an altitude of $100\\text{ km}$ in the thermosphere (the Kármán line), the atmospheric pressure is $P = 0.032\\text{ Pa}$ and the temperature is $T = 200\\text{ K}$. Assuming an effective molecular diameter $d = 3.7 \\times 10^{-10}\\text{ m}$ and average molecular mass $m = 4.8 \\times 10^{-26}\\text{ kg}$ (diatomic nitrogen). (a) Calculate the number density $n$ and the mean free path $\\lambda$. (b) Determine the average collision frequency $\\nu_{\\text{coll}}$.",
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

with open('/Users/karimsiam/.gemini/antigravity/scratch/quantum-mechanics-library/unit7_data.json', 'w') as f:
    json.dump({"number": 7, "title": "Transport Phenomena and Phase Transition", "leadSummary": "Boltzmann transport equation, H-theorem and arrow of time, mean free path, viscosity, thermal conductivity, diffusion, Brownian motion, Ehrenfest phase transition classification, Clausius-Clapeyron, and mean-field Ising model.", "sections": u7_sections, "problems": u7_problems}, f, indent=2)

print("Unit 7 built successfully with 8 topics and 3 solved problems!")
