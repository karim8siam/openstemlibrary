import json

unit3 = {
    "id": "unit-3",
    "number": 3,
    "title": "Wave Properties of Particles & Quantum Foundations",
    "description": "Foundational quantum physics: Louis de Broglie's matter wave hypothesis, phase velocity vs group velocity, and relativistic wave packets; Davisson-Germer electron diffraction and Thomson crystal transmission; Heisenberg uncertainty principle, Fourier analysis, and experimental thought experiments; fundamental physical applications of uncertainty; Born statistical interpretation, wave function normalization, and probability currents.",
    "sections": [
        {
            "id": "u3-sec1",
            "title": "de Broglie Matter Wave Hypothesis & Wave-Packet Velocity Dynamics",
            "simulation": "de-broglie-matter-waves-sim",
            "content": """<h4>1. Louis de Broglie's Hypothesis of Matter Waves (1924)</h4>
<p>Inspired by the dual wave-particle nature of light (Einstein's photons), Prince Louis de Broglie proposed that nature possesses fundamental symmetry: if radiation exhibits particle properties, then material particles (electrons, protons, atoms) must also possess wave-like properties.</p>
<p>For any particle of relativistic energy $E$ and momentum $p$, its associated <strong>matter wave (de Broglie wave)</strong> has frequency $\nu$ and wavelength $\lambda$ given by:</p>
<div class="math-display">
$$\\nu = \\frac{E}{h} = \\frac{\\gamma m_0 c^2}{h}, \\quad \\lambda = \\frac{h}{p} = \\frac{h}{\\gamma m_0 v} = \\frac{h}{m v} \\quad (\\text{for } v \\ll c)$$
</div>
<p>Using the reduced Planck constant $\\hbar = h / (2\\pi)$ and wave vector $k = 2\\pi / \\lambda$, the momentum relation becomes:</p>
<div class="math-display">
$$\\vec{p} = \\hbar \\vec{k}, \\quad E = \\hbar \\omega$$
</div>
<p>For an electron accelerated from rest through an electrostatic potential difference $V$:</p>
<div class="math-display">
$$K = \\frac{p^2}{2 m_e} = e V \\implies p = \\sqrt{2 m_e e V}$$
</div>
<div class="math-display">
$$\\lambda = \\frac{h}{\\sqrt{2 m_e e V}} = \\frac{1.226}{\\sqrt{V\\,(\\text{in Volts})}}\\,\\text{nm} = \\frac{12.26}{\\sqrt{V\\,(\\text{in Volts})}}\\,\\text{\\AA}$$
</div>
<p>For $V = 100\\,\\text{V}$, $\\lambda = 0.123\\,\\text{nm} = 1.23\\,\\text{\\AA}$, which is identical to the interatomic spacings in crystalline lattices.</p>

<h4>2. Phase Velocity vs. Group Velocity of Matter Waves</h4>
<p>A pure monochromatic harmonic plane wave $\\psi(x, t) = A e^{i(kx - \\omega t)}$ propagates with <strong>Phase Velocity $v_p$</strong>:</p>
<div class="math-display">
$$v_p = \\frac{\\omega}{k} = \\frac{E / \\hbar}{p / \\hbar} = \\frac{E}{p} = \\frac{\\gamma m_0 c^2}{\\gamma m_0 v} = \\frac{c^2}{v}$$
</div>
<p>Because every material particle travels at speed $v < c$, the phase velocity $v_p = c^2 / v > c$. The phase of an individual wave crest travels faster than light! This does not violate relativity because a single infinite monochromatic sine wave carries zero information.</p>
<p>To represent a localized physical particle, multiple waves with slightly different frequencies and wavelengths interfere to form a localized <strong>wave packet</strong>:</p>
<div class="math-display">
$$\\Psi(x, t) = \\int A(k) e^{i(k x - \\omega(k) t)}\\, dk$$
</div>
<p>The envelope of the wave packet, which carries the physical energy, mass, and information, propagates at the <strong>Group Velocity $v_g$</strong>:</p>
<div class="math-display">
$$v_g = \\frac{d\\omega}{dk} = \\frac{d(\\hbar\\omega)}{d(\\hbar k)} = \\frac{dE}{dp}$$
</div>
<p>Using the relativistic energy-momentum invariant $E^2 = p^2 c^2 + m_0^2 c^4$, differentiate both sides with respect to $p$:</p>
<div class="math-display">
$$2 E \\frac{dE}{dp} = 2 p c^2 \\implies \\frac{dE}{dp} = \\frac{p c^2}{E} = \\frac{(\\gamma m_0 v) c^2}{\\gamma m_0 c^2} = v$$
</div>
<p><strong>Crucial Theorem:</strong> The group velocity of the de Broglie matter wave packet equals precisely the physical velocity of the particle:</p>
<div class="math-display">
$$v_g = v_{\\text{particle}}$$
</div>
<p>Furthermore, multiplying phase and group velocities reveals the relativistic relationship:</p>
<div class="math-display">
$$v_p \\cdot v_g = \\left( \\frac{c^2}{v} \\right) \\cdot v = c^2$$
</div>"""
        },
        {
            "id": "u3-sec2",
            "title": "Experimental Confirmation of Matter Waves: Davisson-Germer & Thomson Experiments",
            "simulation": "davisson-germer-diffraction-sim",
            "content": """<h4>1. The Davisson-Germer Experiment (1927)</h4>
<p>Clinton Davisson and Lester Germer at Bell Telephone Laboratories provided direct, incontrovertible experimental proof of de Broglie matter waves by demonstrating the diffraction of electrons from a single-crystal nickel target.</p>
<p>Electrons emitted from a hot tungsten filament were accelerated through variable potential $V$ ($40\\text{ to }68\\,\\text{V}$) and directed normally onto a cleaved surface of a single nickel crystal. The scattered electrons were collected at varying scattering angles $\\theta$ using a movable Faraday ionization chamber.</p>
<p><strong>Key Observation:</strong> At an accelerating potential of exactly $V = 54\\,\\text{V}$, a pronounced, sharp intensity peak emerged at scattering angle $\\theta = 50^\\circ$.</p>

<h4>2. Quantitative Mathematical Agreement</h4>
<p>The interatomic lattice plane spacing of nickel along the crystal surface is known from X-ray diffraction to be $D = 0.215\\,\\text{nm}$.</p>
<p>The glancing angle $\\phi$ relative to the Bragg planes is related to the scattering angle $\\theta$ by:</p>
<div class="math-display">
$$\\phi = \\frac{180^\\circ - \\theta}{2} = \\frac{180^\\circ - 50^\\circ}{2} = 65^\\circ$$
</div>
<p>The interplanar spacing $d$ perpendicular to these planes is:</p>
<div class="math-display">
$$d = D \\sin\\left( \\frac{\\theta}{2} \\right) = (0.215\\,\\text{nm}) \\sin(25^\\circ) = 0.0909\\,\\text{nm}$$
</div>
<p>Applying Bragg's law for first-order ($n = 1$) constructive interference:</p>
<div class="math-display">
$$\\lambda_{\\text{Bragg}} = 2 d \\sin\\phi = 2 (0.0909\\,\\text{nm}) \\sin(65^\\circ) = 0.1648\\,\\text{nm} \\approx 1.65\\,\\text{\\AA}$$
</div>
<p>Now evaluate de Broglie's theoretical matter wavelength for an electron accelerated through $54\\,\\text{V}$:</p>
<div class="math-display">
$$\\lambda_{\\text{de Broglie}} = \\frac{h}{\\sqrt{2 m_e e V}} = \\frac{1.226}{\\sqrt{54}}\\,\\text{nm} = \\frac{1.226}{7.348}\\,\\text{nm} = 0.1668\\,\\text{nm} \\approx 1.67\\,\\text{\\AA}$$
</div>
<p>The Bragg diffraction wavelength and de Broglie's theoretical matter wavelength agree within $1.2\\%$, proving beyond all doubt that electrons propagate as physical waves.</p>

<h4>3. The G.P. Thomson Transmission Diffraction Experiment</h4>
<p>Simultaneously in 1927, George Paget Thomson in Scotland demonstrated transmission diffraction of high-energy electrons ($10\\text{ to }60\\,\\text{keV}$) passed through ultra-thin polycrystalline gold and platinum foils ($d \\sim 10\\,\\text{nm}$).</p>
<p>Because the foil contained millions of randomly oriented micro-crystallites, the diffracted electrons formed sharp concentric circular rings on a photographic film behind the foil—identical to the Debye-Scherrer X-ray powder diffraction rings!</p>
<p><strong>Historic Irony:</strong> J.J. Thomson received the 1906 Nobel Prize for proving the electron is a <em>particle</em>; his son G.P. Thomson received the 1937 Nobel Prize for proving the electron is a <em>wave</em>.</p>"""
        },
        {
            "id": "u3-sec3",
            "title": "Heisenberg Uncertainty Principle: Mathematical Statement & Thought Experiments",
            "simulation": "heisenberg-microscope-sim",
            "content": """<h4>1. Werner Heisenberg's Formal Uncertainty Principle (1927)</h4>
<p>In classical Newtonian mechanics, the position $\\vec{r}(t)$ and momentum $\\vec{p}(t)$ of a particle can simultaneously be measured with infinite precision. In quantum mechanics, because particles are described by wave packets, it is physically impossible to simultaneously measure non-commuting conjugate physical observables with unlimited accuracy.</p>
<p>For position and momentum along the same spatial coordinate axis:</p>
<div class="math-display">
$$\\Delta x \\cdot \\Delta p_x \\ge \\frac{\\hbar}{2}$$
</div>
<div class="math-display">
$$\\Delta y \\cdot \\Delta p_y \\ge \\frac{\\hbar}{2}, \\quad \\Delta z \\cdot \\Delta p_z \\ge \\frac{\\hbar}{2}$$
</div>
<p>where $\\Delta x$ and $\\Delta p_x$ are the root-mean-square standard deviations: $\\Delta x = \\sqrt{\\langle x^2 \\rangle - \\langle x \\rangle^2}$.</p>
<p>For energy and time, an analogous uncertainty relation holds:</p>
<div class="math-display">
$$\\Delta E \\cdot \\Delta t \\ge \\frac{\\hbar}{2}$$
</div>
<p>where $\\Delta t$ represents the time duration during which the state evolves significantly or the lifetime of an excited quantum state.</p>

<h4>2. Fourier Wave-Packet Derivation</h4>
<p>Mathematically, a localized spatial wave packet $\\psi(x)$ and its momentum-space distribution $\\phi(p)$ are related by a spatial Fourier transform:</p>
<div class="math-display">
$$\\phi(p) = \\frac{1}{\\sqrt{2\\pi\\hbar}} \\int_{-\\infty}^\\infty \\psi(x) e^{-i p x / \\hbar}\\, dx$$
</div>
<p>By the fundamental properties of Fourier analysis, the spatial spread $\\Delta x$ of a wave packet and its spatial frequency spread $\\Delta k = \\Delta p / \\hbar$ satisfy the bandwidth theorem: $\\Delta x \\cdot \\Delta k \\ge \\frac{1}{2}$, which directly yields $\\Delta x \\cdot \\Delta p \\ge \\frac{\\hbar}{2}$. The lower bound is achieved only by a Gaussian wave packet.</p>

<h4>3. The Heisenberg Gamma-Ray Microscope Thought Experiment</h4>
<p>To determine the position of an electron with high precision $\Delta x$, one must illuminate it with light of very short wavelength $\lambda$ and observe it through a microscope objective of subtended angular aperture $2\theta$.</p>
<p>By Abbe's optical diffraction resolution criterion, the spatial resolution is:</p>
<div class="math-display">
$$\\Delta x \\approx \\frac{\\lambda}{2 \\sin\\theta}$$
</div>
<p>To see the electron, at least one photon must scatter off it and enter the microscope lens anywhere within the cone of half-angle $\theta$. In doing so, the photon transfers an unknown recoil momentum to the electron. The horizontal component of the scattered photon momentum can range from $- (h/\lambda) \sin\theta$ to $+ (h/\lambda) \sin\theta$, imparting an unavoidable momentum uncertainty to the electron:</p>
<div class="math-display">
$$\\Delta p_x \\approx 2 \\left( \\frac{h}{\\lambda} \\right) \\sin\\theta$$
</div>
<p>Multiplying the two uncertainties:</p>
<div class="math-display">
$$\\Delta x \\cdot \\Delta p_x \\approx \\left( \\frac{\\lambda}{2 \\sin\\theta} \\right) \\left( \\frac{2 h \\sin\\theta}{\\lambda} \\right) \\approx h > \\frac{\\hbar}{2}$$
</div>
<p>Attempting to measure position more accurately by using shorter wavelengths ($\lambda \to 0$) inevitably imparts colossal uncontrollable momentum kicks ($\Delta p_x \to \infty$).</p>"""
        },
        {
            "id": "u3-sec4",
            "title": "Applications of the Uncertainty Principle: Bound States & Zero-Point Energy",
            "content": """<h4>1. Non-Existence of Electrons Inside the Atomic Nucleus</h4>
<p>Before the discovery of the neutron by Chadwick (1932), it was hypothesized that the atomic nucleus consisted of protons and electrons. We can test this hypothesis using the Uncertainty Principle.</p>
<p>A typical nucleus has a radius $R \\sim 5\\,\\text{fm} = 5 \\times 10^{-15}\\,\\text{m}$. If an electron were confined inside the nucleus, its maximum spatial uncertainty would be $\\Delta x \\approx 2 R \\approx 10^{-14}\\,\\text{m}$.</p>
<p>The minimum momentum uncertainty of the confined electron is:</p>
<div class="math-display">
$$\\Delta p \\ge \\frac{\\hbar}{2 \\Delta x} = \\frac{1.054 \\times 10^{-34}\\,\\text{J}\\cdot\\text{s}}{2 \\times 10^{-14}\\,\\text{m}} \\approx 5.27 \\times 10^{-21}\\,\\text{kg}\\cdot\\text{m/s}$$
</div>
<p>Since $\Delta p \sim p$, the electron must be relativistic. Its total energy is:</p>
<div class="math-display">
$$E \\approx p c = (5.27 \\times 10^{-21}\\,\\text{kg}\\cdot\\text{m/s}) \\times (3.0 \\times 10^8\\,\\text{m/s}) \\approx 1.58 \\times 10^{-12}\\,\\text{J} \\approx 9.9\\,\\text{MeV}$$
</div>
<p>The kinetic energy of the electron would be $K = E - m_e c^2 \\approx 9.4\\,\\text{MeV}$. However, experimental beta decay measurements show that electrons emitted from nuclei have kinetic energies of only $1\\text{ to }3\\,\\text{MeV}$, and the nuclear Coulomb potential well (depth $\sim 2-3\\,\\text{MeV}$) is vastly too shallow to trap a $10\\,\\text{MeV}$ electron.</p>
<p><strong>Conclusion:</strong> Electrons cannot exist as permanent constituent particles inside the atomic nucleus. Beta-decay electrons must be created instantaneously at the moment of nuclear decay.</p>

<h4>2. Zero-Point Energy of a Quantum Harmonic Oscillator</h4>
<p>In classical mechanics, a harmonic oscillator at $T = 0\\text{ K}$ can sit motionless at the bottom of its potential well with zero position and zero momentum ($x = 0, p = 0$), yielding zero energy ($E = 0$).</p>
<p>In quantum mechanics, if $x = 0$ exactly ($\Delta x = 0$), then $\Delta p \to \infty$, making kinetic energy infinite! The total energy of an oscillator of mass $m$ and natural frequency $\omega$ is:</p>
<div class="math-display">
$$E = \\frac{p^2}{2m} + \\frac{1}{2} m \\omega^2 x^2 \\approx \\frac{(\\Delta p)^2}{2m} + \\frac{1}{2} m \\omega^2 (\\Delta x)^2$$
</div>
<p>Using the minimum uncertainty relation $\\Delta p = \\frac{\\hbar}{2 \\Delta x}$:</p>
<div class="math-display">
$$E(\\Delta x) = \\frac{\\hbar^2}{8 m (\\Delta x)^2} + \\frac{1}{2} m \\omega^2 (\\Delta x)^2$$
</div>
<p>To find the minimum ground-state energy, differentiate with respect to $\Delta x$ and set to zero:</p>
<div class="math-display">
$$\\frac{dE}{d(\\Delta x)} = - \\frac{\\hbar^2}{4 m (\\Delta x)^3} + m \\omega^2 (\\Delta x) = 0 \\implies (\\Delta x)^2 = \\frac{\\hbar}{2 m \\omega}$$
</div>
<p>Substituting back into the energy equation:</p>
<div class="math-display">
$$E_{min} = \\frac{\\hbar^2}{8 m \\left(\\frac{\\hbar}{2 m \\omega}\\right)} + \\frac{1}{2} m \\omega^2 \\left(\\frac{\\hbar}{2 m \\omega}\\right) = \\frac{1}{4} \\hbar \\omega + \\frac{1}{4} \\hbar \\omega = \\frac{1}{2} \\hbar \\omega$$
</div>
<p>This yields the exact <strong>zero-point energy $E_0 = \\frac{1}{2} \\hbar\\omega$</strong> of quantum mechanics! A quantum oscillator can never be brought to complete rest, even at absolute zero.</p>"""
        },
        {
            "id": "u3-sec5",
            "title": "Born Statistical Interpretation, Wave Function Normalization & Probability Currents",
            "content": """<h4>1. Max Born's Probability Interpretation of the Wave Function (1926)</h4>
<p>A quantum particle is fully characterized by its complex-valued wave function $\\Psi(\\vec{r}, t)$. While $\\Psi$ itself is not directly measurable, Max Born recognized that its modulus squared represents the <strong>probability density</strong> of finding the particle at position $\\vec{r}$ at time $t$:</p>
<div class="math-display">
$$P(\\vec{r}, t) = |\\Psi(\\vec{r}, t)|^2 = \\Psi^*(\vec{r}, t) \\Psi(\\vec{r}, t)$$
</div>
<p>The probability of finding the particle in an infinitesimal spatial volume element $d^3r = dx dy dz$ is $dP = |\\Psi|^2 d^3r$.</p>

<h4>2. Normalization Condition & Physical Requirements</h4>
<p>Because the particle must exist somewhere in the universe with $100\\%$ certainty, the total integrated probability over all space must equal unity:</p>
<div class="math-display">
$$\\int_{-\\infty}^\\infty \\int_{-\\infty}^\\infty \\int_{-\\infty}^\\infty |\\Psi(\\vec{r}, t)|^2\\, d^3r = 1$$
</div>
<p>To be physically admissible, a wave function must be <strong>square-integrable</strong> ($L^2$ space), single-valued everywhere, continuous, and possess continuous first spatial derivatives.</p>

<h4>3. Probability Current Density & The Continuity Equation</h4>
<p>To demonstrate that total probability is conserved over time, differentiate the probability density with respect to $t$ using the time-dependent Schrödinger equation $i\\hbar \\frac{\\partial \\Psi}{\\partial t} = -\\frac{\\hbar^2}{2m} \\nabla^2 \\Psi + V \\Psi$:</p>
<div class="math-display">
$$\\frac{\\partial |\\Psi|^2}{\\partial t} = \\frac{\\partial (\\Psi^* \\Psi)}{\\partial t} = \\Psi^* \\frac{\\partial \\Psi}{\\partial t} + \\Psi \\frac{\\partial \\Psi^*}{\\partial t}$$
</div>
<div class="math-display">
$$\\frac{\\partial |\\Psi|^2}{\\partial t} = \\Psi^* \\left( \\frac{i\\hbar}{2m} \\nabla^2 \\Psi - \\frac{i}{\\hbar} V \\Psi \\right) + \\Psi \\left( -\\frac{i\\hbar}{2m} \\nabla^2 \\Psi^* + \\frac{i}{\\hbar} V \\Psi^* \\right)$$
</div>
<div class="math-display">
$$\\frac{\\partial |\\Psi|^2}{\\partial t} = \\frac{i\\hbar}{2m} (\\Psi^* \\nabla^2 \\Psi - \\Psi \\nabla^2 \\Psi^*) = \\nabla \\cdot \\left[ \\frac{i\\hbar}{2m} (\\Psi^* \\nabla \\Psi - \\Psi \\nabla \\Psi^*) \\right]$$
</div>
<p>Defining the <strong>Probability Current Density $\\vec{j}(\\vec{r}, t)$</strong>:</p>
<div class="math-display">
$$\\vec{j}(\\vec{r}, t) = \\frac{\\hbar}{2 m i} \\left( \\Psi^* \\nabla \\Psi - \\Psi \\nabla \\Psi^* \\right) = \\frac{\\hbar}{m} \\text{Im}(\\Psi^* \\nabla \\Psi)$$
</div>
<p>The relation assumes the canonical form of the <strong>Continuity Equation</strong>:</p>
<div class="math-display">
$$\\frac{\\partial \\rho}{\\partial t} + \\nabla \\cdot \\vec{j} = 0 \\quad (\\text{where } \\rho = |\\Psi|^2)$$
</div>
<p>Applying the divergence theorem confirms that the total integrated probability $\int |\\Psi|^2 d^3r$ is strictly conserved for all time.</p>"""
        }
    ],
    "problems": [
        {
            "id": "u3-prob1",
            "title": "de Broglie Wavelength of Non-Relativistic, Relativistic & Thermal Particles",
            "statement": "Calculate the de Broglie wavelength for three different physical systems: (a) An electron accelerated from rest across a potential difference of V = 150\\,\\text{V}$. (b) A relativistic proton with kinetic energy K = 2.0\\,\\text{GeV}$ (rest energy m_p c^2 = 938.3\\,\\text{MeV}$). (c) A thermal neutron at room temperature T = 300\\,\\text{K}$ with average kinetic energy K = \\frac{3}{2} k_B T (m_n = 1.675 \\times 10^{-27}\\,\\text{kg}$).",
            "solution": """<p><strong>Step 1: Electron Accelerated Through 150 V (Non-Relativistic)</strong></p>
<p>Since $K = 150\\,\\text{eV} \\ll m_e c^2 = 511\\,\\text{keV}$, non-relativistic mechanics applies:</p>
<div class="math-display">
$$\\lambda_e = \\frac{h}{\\sqrt{2 m_e e V}} = \\frac{1.226}{\\sqrt{150}}\\,\\text{nm} = \\frac{1.226}{12.247}\\,\\text{nm} \\approx 0.1001\\,\\text{nm} = 1.001\\,\\text{\\AA}$$
</div>

<p><strong>Step 2: Relativistic Proton at K = 2.0 GeV</strong></p>
<p>Total energy of the proton is $E = K + m_p c^2 = 2000\\,\\text{MeV} + 938.3\\,\\text{MeV} = 2938.3\\,\\text{MeV}$.</p>
<p>Using the relativistic momentum-energy relation $p c = \\sqrt{E^2 - (m_p c^2)^2}$:</p>
<div class="math-display">
$$p c = \\sqrt{(2938.3)^2 - (938.3)^2} = \\sqrt{8.6336 \\times 10^6 - 0.8804 \\times 10^6} = \\sqrt{7.7532 \\times 10^6} \\approx 2784.5\\,\\text{MeV}$$
</div>
<div class="math-display">
$$p = \\frac{2784.5 \\times 10^6 \\times 1.602 \\times 10^{-19}\\,\\text{J}}{3.0 \\times 10^8\\,\\text{m/s}} \\approx 1.487 \\times 10^{-18}\\,\\text{kg}\\cdot\\text{m/s}$$
</div>
<div class="math-display">
$$\\lambda_p = \\frac{h}{p} = \\frac{6.626 \\times 10^{-34}\\,\\text{J}\\cdot\\text{s}}{1.487 \\times 10^{-18}\\,\\text{kg}\\cdot\\text{m/s}} \\approx 4.456 \\times 10^{-16}\\,\\text{m} = 0.446\\,\\text{fm}$$
</div>
<p>This wavelength ($0.45\\,\\text{fm}$) is smaller than the size of a proton ($0.84\\,\\text{fm}$), making it ideal for probing deep quark structures inside hadrons.</p>

<p><strong>Step 3: Thermal Neutron at 300 K</strong></p>
<div class="math-display">
$$K = \\frac{3}{2} k_B T = 1.5 \\times (1.381 \\times 10^{-23}\\,\\text{J/K}) \\times 300\\,\\text{K} = 6.2145 \\times 10^{-21}\\,\\text{J}$$
</div>
<div class="math-display">
$$p = \\sqrt{2 m_n K} = \\sqrt{2(1.675 \\times 10^{-27}\\,\\text{kg})(6.2145 \\times 10^{-21}\\,\\text{J})} = \\sqrt{2.082 \\times 10^{-47}} \\approx 4.563 \\times 10^{-24}\\,\\text{kg}\\cdot\\text{m/s}$$
</div>
<div class="math-display">
$$\\lambda_n = \\frac{h}{p} = \\frac{6.626 \\times 10^{-34}}{4.563 \\times 10^{-24}} \\approx 1.452 \\times 10^{-10}\\,\\text{m} = 0.145\\,\\text{nm} = 1.45\\,\\text{\\AA}$$
</div>
<p>Thermal neutrons have wavelengths perfectly matched to interatomic crystalline planes, which is why thermal neutron scattering is a primary tool for mapping magnetic and atomic structures.</p>"""
        },
        {
            "id": "u3-prob2",
            "title": "Uncertainty Principle Proof of Nuclear Electron Confinement Impossibility",
            "statement": "An atomic nucleus has a characteristic diameter of d = 8.0\\,\\text{fm} (8.0 \\times 10^{-15}\\,\\text{m}). Assuming an electron were trapped inside this nuclear volume: (a) Calculate the minimum uncertainty in its momentum \\Delta p. (b) Calculate the minimum relativistic total energy E and kinetic energy K that the electron must possess. (c) Compare this kinetic energy with the depth of typical nuclear electrostatic potential wells (approximately 2.5 to 3.0 MeV) and explain why the electron must escape.",
            "solution": """<p><strong>Step 1: Calculate Minimum Momentum Uncertainty $\\Delta p$</strong></p>
<p>The maximum spatial uncertainty for confinement within the nucleus is $\\Delta x = d = 8.0 \\times 10^{-15}\\,\\text{m}$:</p>
<div class="math-display">
$$\\Delta p \\ge \\frac{\\hbar}{2 \\Delta x} = \\frac{1.05457 \\times 10^{-34}\\,\\text{J}\\cdot\\text{s}}{2 \\times 8.0 \\times 10^{-15}\\,\\text{m}} = \\frac{1.05457 \\times 10^{-34}}{1.60 \\times 10^{-14}} \\approx 6.591 \\times 10^{-21}\\,\\text{kg}\\cdot\\text{m/s}$$
</div>

<p><strong>Step 2: Calculate Relativistic Energy</strong></p>
<p>Since $\Delta p \sim p$, the momentum is $p \\approx 6.591 \\times 10^{-21}\\,\\text{kg}\\cdot\\text{m/s}$:</p>
<div class="math-display">
$$p c = (6.591 \\times 10^{-21}\\,\\text{kg}\\cdot\\text{m/s}) \\times (2.9979 \\times 10^8\\,\\text{m/s}) = 1.976 \\times 10^{-12}\\,\\text{J}$$
</div>
<p>In electron-volts:</p>
<div class="math-display">
$$p c = \\frac{1.976 \\times 10^{-12}\\,\\text{J}}{1.6022 \\times 10^{-19}\\,\\text{J/eV}} \\approx 1.233 \\times 10^7\\,\\text{eV} = 12.33\\,\\text{MeV}$$
</div>
<p>The total relativistic energy is:</p>
<div class="math-display">
$$E = \\sqrt{(p c)^2 + (m_e c^2)^2} = \\sqrt{(12.33)^2 + (0.511)^2} \\approx 12.34\\,\\text{MeV}$$
</div>
<p>The kinetic energy is:</p>
<div class="math-display">
$$K = E - m_e c^2 = 12.34\\,\\text{MeV} - 0.51\\,\\text{MeV} = 11.83\\,\\text{MeV}$$
</div>

<p><strong>Step 3: Physical Assessment</strong></p>
<p>The electrostatic attractive potential well experienced by an electron near the edge of a nucleus ($Z \\sim 20$) is at most:</p>
<div class="math-display">
$$V \\approx \\frac{Z e^2}{4\\pi\\varepsilon_0 R} \\approx 3\\text{ to }4\\,\\text{MeV}$$
</div>
<p>Because the kinetic energy ($11.8\\,\\text{MeV}$) overwhelmingly exceeds the potential well binding depth ($3.5\\,\\text{MeV}$), no bound quantum state can exist. The electron would immediately tunnel out and escape into the continuum, proving that electrons cannot be nuclear building blocks.</p>"""
        },
        {
            "id": "u3-prob3",
            "title": "Natural Spectral Linewidth & Excited State Lifetime via Energy-Time Uncertainty",
            "statement": "An excited atomic state of an atom has a mean lifetime of \\tau = 1.20 \\times 10^{-8}\\,\\text{s} (12.0 ns) before de-exciting to the ground state via spontaneous emission of a photon of wavelength \\lambda = 589.0\\,\\text{nm} (sodium D-line). Calculate: (a) The minimum uncertainty in the energy of the excited state \\Delta E in eV. (b) The fractional energy uncertainty \\Delta E / E. (c) The natural frequency linewidth \\Delta \\nu of the emitted radiation. (d) The natural wavelength linewidth \\Delta \\lambda in angstroms.",
            "solution": """<p><strong>Step 1: Calculate Energy Uncertainty $\\Delta E$</strong></p>
<p>Using the energy-time uncertainty principle $\\Delta E \\cdot \\Delta t \\ge \\frac{\\hbar}{2}$ with $\\Delta t = \\tau = 1.20 \\times 10^{-8}\\,\\text{s}$:</p>
<div class="math-display">
$$\\Delta E = \\frac{\\hbar}{2 \\tau} = \\frac{1.05457 \\times 10^{-34}\\,\\text{J}\\cdot\\text{s}}{2 \\times (1.20 \\times 10^{-8}\\,\\text{s})} \\approx 4.394 \\times 10^{-27}\\,\\text{J}$$
</div>
<p>Converting to electron-volts:</p>
<div class="math-display">
$$\\Delta E = \\frac{4.394 \\times 10^{-27}\\,\\text{J}}{1.6022 \\times 10^{-19}\\,\\text{J/eV}} \\approx 2.742 \\times 10^{-8}\\,\\text{eV} = 27.42\\,\\text{neV}$$
</div>

<p><strong>Step 2: Calculate Transition Energy & Fractional Uncertainty</strong></p>
<div class="math-display">
$$E = \\frac{h c}{\\lambda} = \\frac{1239.84\\,\\text{eV}\\cdot\\text{nm}}{589.0\\,\\text{nm}} \\approx 2.105\\,\\text{eV}$$
</div>
<div class="math-display">
$$\\frac{\\Delta E}{E} = \\frac{2.742 \\times 10^{-8}\\,\\text{eV}}{2.105\\,\\text{eV}} \\approx 1.30 \\times 10^{-8}$$
</div>

<p><strong>Step 3: Natural Frequency Linewidth $\\Delta \\nu$</strong></p>
<div class="math-display">
$$\\Delta \\nu = \\frac{\\Delta E}{h} = \\frac{\\hbar / (2\\tau)}{2\\pi \\hbar} = \\frac{1}{4\\pi \\tau} = \\frac{1}{4\\pi \\times (1.20 \\times 10^{-8}\\,\\text{s})} \\approx 6.63 \\times 10^6\\,\\text{Hz} = 6.63\\,\\text{MHz}$$
</div>

<p><strong>Step 4: Natural Wavelength Linewidth $\\Delta \\lambda$</strong></p>
<p>Differentiating $\lambda = c/\nu \implies |d\lambda| = \frac{c}{\nu^2} d\nu = \frac{\lambda^2}{c} \Delta\nu$:</p>
<div class="math-display">
$$\\Delta \\lambda = \\frac{\\lambda^2}{c} \\Delta \\nu = \\frac{(589.0 \\times 10^{-9}\\,\\text{m})^2}{3.0 \\times 10^8\\,\\text{m/s}} \\times (6.63 \\times 10^6\\,\\text{s}^{-1}) = \\frac{3.469 \\times 10^{-13}}{3.0 \\times 10^8} \\times 6.63 \\times 10^6 \\approx 7.67 \\times 10^{-15}\\,\\text{m} = 0.0000767\\,\\text{\\AA}$$
</div>
<p>The natural spectral line is exceedingly narrow ($\sim 10^{-4}\,\text{\AA}$); in practical laboratory gases, Doppler broadening and collision pressure broadening swamped this natural width by factors of thousands until Doppler-free saturated laser spectroscopy was developed.</p>"""
        }
    ]
}

unit4 = {
    "id": "unit-4",
    "number": 4,
    "title": "Rutherford-Bohr Atomic Model & Old Quantum Theory",
    "description": "Exhaustive treatment of atomic architecture: Thomson's plum-pudding model limitations; Rutherford alpha-particle scattering experiment, hyperbolic Coulomb orbit derivations, and nuclear dimension formulas; classical radiative collapse and the Larmor formula; Bohr's quantum model of hydrogenic atoms and spectral series; finite nuclear mass reduced mass corrections and the discovery of deuterium; Franck-Hertz inelastic electron impact excitation.",
    "sections": [
        {
            "id": "u4-sec1",
            "title": "Classical Atomic Models & The Rutherford Alpha-Scattering Experiment",
            "content": """<h4>1. J.J. Thomson's Plum-Pudding Model (1904)</h4>
<p>Following his discovery of the electron (1897), J.J. Thomson proposed that an atom consists of a uniform sphere of positive electrostatic charge of atomic radius $R \\sim 10^{-10}\\,\\text{m}$ (1 \u00c5), within which tiny negative electrons are embedded like plums in a pudding.</p>
<p><strong>Classical Predictions:</strong> Because positive charge is diffuse across the entire atomic volume, the maximum electric field inside the atom is weak ($E_{max} = \\frac{Q}{4\pi\varepsilon_0 R^2} \\sim 10^{11}\\,\\text{V/m}$). An energetic $\\alpha$-particle ($q = +2e$, mass $m_\\alpha \\approx 7300 m_e$, $E_k \\sim 5\\text{ to }8\\,\\text{MeV}$) passing through a thin gold foil would experience only tiny deflections ($\theta < 1^\circ$). Multiple scattering could produce at most average deflections of a few degrees ($< 3^\circ$).</p>

<h4>2. The Geiger-Marsden Experiments (1909–1911)</h4>
<p>Under Ernest Rutherford's direction, Hans Geiger and Ernest Marsden directed a collimated beam of $5.5\\,\\text{MeV}$ $\\alpha$-particles from a bismuth-214 radioactive source through an ultra-thin gold foil (thickness $\\sim 400\\,\\text{nm}$, roughly $1000$ atoms thick) and recorded scintillations on a zinc sulfide ($\text{ZnS}$) phosphorescent screen.</p>
<p><strong>The Shocking Discovery:</strong> While the vast majority of $\\alpha$-particles passed straight through undeflected, roughly <strong>1 in 8,000 $\alpha$-particles was deflected by angles greater than $90^\circ$</strong>, and some bounced directly backward ($\theta \\approx 180^\circ$)! Rutherford famously recounted: <em>"It was quite the most incredible event that has ever happened to me in my life. It was almost as incredible as if you fired a 15-inch shell at a piece of tissue paper and it came back and hit you."</em></p>
<p>Thomson's diffuse atom could never produce the colossal electrostatic field required to reverse a massive energetic $\alpha$-particle.</p>"""
        },
        {
            "id": "u4-sec2",
            "title": "Mathematical Derivation of Rutherford Scattering Cross-Section & Nuclear Dimensions",
            "simulation": "rutherford-alpha-scattering-sim",
            "content": """<h4>1. Coulomb Hyperbolic Trajectory Kinematics</h4>
<p>Rutherford (1911) proposed that all the positive charge $+Z e$ and virtually all the mass of the atom are concentrated in a tiny central core termed the <strong>nucleus</strong>, surrounded by a cloud of orbiting electrons.</p>
<p>Consider an $\\alpha$-particle (charge $q_1 = +2e$, mass $m_\\alpha$) fired with initial speed $v_0$ and <strong>impact parameter $b$</strong> (the perpendicular distance from the nucleus to the initial asymptotic velocity line) toward a stationary gold nucleus of charge $q_2 = +Z e$. The repulsive Coulomb force is:</p>
<div class="math-display">
$$F = \\frac{1}{4\\pi\\varepsilon_0} \\frac{(2e)(Ze)}{r^2} = \\frac{2 Z e^2}{4\\pi\\varepsilon_0 r^2}$$
</div>
<p>Because the force is central, angular momentum $L = m_\\alpha v_0 b = m_\\alpha r^2 \\dot{\\phi}$ is strictly conserved. Integrating Newton's Second Law along the axis of symmetry yields the fundamental relation between impact parameter $b$ and scattering deflection angle $\\theta$:</p>
<div class="math-display">
$$b = \\frac{2 Z e^2}{4\\pi\\varepsilon_0 (m_\\alpha v_0^2)} \\cot\\left( \\frac{\\theta}{2} \\right) = \\frac{z Z e^2}{4\\pi\\varepsilon_0 (2 K)} \\cot\\left( \\frac{\\theta}{2} \\right)$$
</div>
<p>where $K = \\frac{1}{2} m_\\alpha v_0^2$ is the kinetic energy of the incoming particle.</p>

<h4>2. Derivation of the Rutherford Differential Cross-Section</h4>
<p>Particles incident with impact parameters between $b$ and $b + db$ through an annular ring of area $d\\sigma = 2\\pi b |db|$ are scattered into solid angle $d\\Omega = 2\\pi \\sin\\theta d\\theta$:</p>
<div class="math-display">
$$\\frac{d\\sigma}{d\\Omega} = \\frac{2\\pi b |db|}{2\\pi \\sin\\theta d\\theta} = \\frac{b}{\\sin\\theta} \\left| \\frac{db}{d\\theta} \\right|$$
</div>
<p>Differentiating $b(\\theta)$:</p>
<div class="math-display">
$$\\frac{db}{d\\theta} = - \\frac{z Z e^2}{8\\pi\\varepsilon_0 K} \\csc^2\\left( \\frac{\\theta}{2} \\right) \\frac{1}{2}$$
</div>
<p>Substituting into the cross-section and using $\\sin\\theta = 2 \\sin(\\theta/2) \\cos(\\theta/2)$:</p>
<div class="math-display">
$$\\frac{d\\sigma}{d\\Omega} = \\left( \\frac{z Z e^2}{4\\pi\\varepsilon_0 \\cdot 4 K} \\right)^2 \\frac{1}{\\sin^4\\left( \\frac{\\theta}{2} \\right)}$$
</div>
<p>This is the celebrated <strong>Rutherford Scattering Formula</strong>. Key testable predictions verified experimentally by Geiger and Marsden:
<ol>
<li>Scattering intensity scales inversely as the fourth power of the sine of half the angle: $N(\\theta) \\propto \\csc^4(\\theta/2)$.</li>
<li>Scattering scales inversely with the square of incident kinetic energy: $N \\propto K^{-2}$.</li>
<li>Scattering scales with the square of target nuclear charge: $N \\propto Z^2$.</li>
<li>Scattering scales linearly with foil thickness $t$.</li>
</ol>
</p>

<h4>3. Nuclear Dimension: Distance of Closest Approach ($d_{min}$)</h4>
<p>In a head-on collision ($b = 0, \\theta = 180^\\circ$), the $\\alpha$-particle decelerates until its entire initial kinetic energy is converted into electrostatic potential energy at the turning point $d_{min}$:</p>
<div class="math-display">
$$K = \\frac{1}{4\\pi\\varepsilon_0} \\frac{(2e)(Ze)}{d_{min}} \\implies d_{min} = \\frac{2 Z e^2}{4\\pi\\varepsilon_0 K}$$
</div>
<p>For a $7.7\\,\\text{MeV}$ $\\alpha$-particle fired at Gold ($Z = 79$):</p>
<div class="math-display">
$$d_{min} = \\frac{2 \\times 79 \\times (1.602 \\times 10^{-19})^2}{4\\pi (8.854 \\times 10^{-12}) \\times (7.7 \\times 1.602 \\times 10^{-13}\\,\\text{J})} \\approx 2.95 \\times 10^{-14}\\,\\text{m} = 29.5\\,\\text{fm}$$
</div>
<p>Since Coulomb's law held precisely down to $d_{min}$, the atomic nucleus must have radius $R_{nuc} < 30\\,\\text{fm} = 3 \\times 10^{-14}\\,\\text{m}$—more than <strong>10,000 times smaller</strong> than the overall atomic radius ($10^{-10}\\,\\text{m}$)! The atom is almost entirely empty space.</p>"""
        },
        {
            "id": "u4-sec3",
            "title": "Classical Radiative Collapse & The Need for Quantum Atomic Postulates",
            "content": """<h4>1. The Classical Instability of Rutherford's Planetary Atom</h4>
<p>Although Rutherford's nuclear model triumphed in explaining scattering, it suffered from a fatal theoretical catastrophe under classical electrodynamics.</p>
<p>In Rutherford's model, electrons orbit the central nucleus like planets around the Sun, held by Coulomb attraction:</p>
<div class="math-display">
$$\\frac{m_e v^2}{r} = \\frac{e^2}{4\\pi\\varepsilon_0 r^2} \\implies a = \\frac{v^2}{r} = \\frac{e^2}{4\\pi\\varepsilon_0 m_e r^2}$$
</div>
<p>An orbiting electron undergoing centripetal acceleration is an accelerated electric charge. According to classical electrodynamics, any accelerated charge radiates electromagnetic power governed by the <strong>Larmor Radiation Formula</strong>:</p>
<div class="math-display">
$$P = \\frac{e^2 a^2}{6\\pi\\varepsilon_0 c^3} = \\frac{e^2}{6\\pi\\varepsilon_0 c^3} \\left( \\frac{e^2}{4\\pi\\varepsilon_0 m_e r^2} \\right)^2 = \\frac{e^6}{96 \\pi^3 \\varepsilon_0^3 m_e^2 c^3 r^4}$$
</div>

<h4>2. Derivation of the Collapse Time ($\tau$)</h4>
<p>The total mechanical energy of an electron in a circular orbit of radius $r$ is:</p>
<div class="math-display">
$$E = K + U = \\frac{1}{2} m_e v^2 - \\frac{e^2}{4\\pi\\varepsilon_0 r} = \\frac{e^2}{8\\pi\\varepsilon_0 r} - \\frac{e^2}{4\\pi\\varepsilon_0 r} = - \\frac{e^2}{8\\pi\\varepsilon_0 r}$$
</div>
<p>Differentiating with respect to time:</p>
<div class="math-display">
$$\\frac{dE}{dt} = \\frac{e^2}{8\\pi\\varepsilon_0 r^2} \\frac{dr}{dt} = - P = - \\frac{e^6}{96 \\pi^3 \\varepsilon_0^3 m_e^2 c^3 r^4}$$
</div>
<p>Solving for the orbital decay rate $dr/dt$:</p>
<div class="math-display">
$$\\frac{dr}{dt} = - \\frac{e^4}{12 \\pi^2 \\varepsilon_0^2 m_e^2 c^3} \\frac{1}{r^2}$$
</div>
<p>Integrating from initial radius $r_0 \\approx 0.53 \\times 10^{-10}\\,\\text{m}$ down to $r = 0$:</p>
<div class="math-display">
$$\\int_{r_0}^0 r^2\\, dr = - \\frac{e^4}{12 \\pi^2 \\varepsilon_0^2 m_e^2 c^3} \\int_0^\\tau dt \\implies \\frac{r_0^3}{3} = \\frac{e^4 \\tau}{12 \\pi^2 \\varepsilon_0^2 m_e^2 c^3}$$
</div>
<div class="math-display">
$$\\tau = \\frac{4 \\pi^2 \\varepsilon_0^2 m_e^2 c^3 r_0^3}{e^4} \\approx 1.56 \\times 10^{-11}\\,\\text{s}$$
</div>
<p><strong>The Classical Paradox:</strong> Classical electrodynamics predicts that every atom in the universe must collapse into its nucleus within a hundredth of a nanosecond, emitting a continuous burst of radiation! In reality, atoms are stable for billions of years and emit sharp, discrete line spectra.</p>"""
        },
        {
            "id": "u4-sec4",
            "title": "Bohr Theory of Hydrogenic Atoms: Radii, Energy Levels & Spectral Series",
            "simulation": "bohr-atom-spectral-series-sim",
            "content": """<h4>1. Niels Bohr's Quantum Postulates (1913)</h4>
<p>To overcome classical collapse, Niels Bohr introduced three bold quantum postulates for hydrogenic atoms (one electron orbiting a nucleus of charge $+Ze$):
<ol>
<li><strong>Stationary States Postulate:</strong> Electrons move in discrete, non-radiating circular orbits called stationary states. While in these orbits, the electron accelerates but does NOT radiate electromagnetic energy.</li>
<li><strong>Angular Momentum Quantization:</strong> The orbital angular momentum $L$ of the electron is quantized in integer multiples of $\\hbar = h / (2\\pi)$:
<div class="math-display">
$$L = m_e v r = n \\hbar = n \\frac{h}{2\\pi} \\quad (n = 1, 2, 3, \\dots)$$
</div></li>
<li><strong>Frequency Postulate (Bohr Transition Rule):</strong> Radiation is emitted or absorbed only when an electron transitions discontinuously between two stationary states ($n_i \\to n_f$). The photon frequency is:
<div class="math-display">
$$h\\nu = E_i - E_f$$
</div></li>
</ol>
</p>

<h4>2. Derivation of Orbit Radii and Speeds</h4>
<p>Equating the Coulomb electrostatic force to the centripetal force:</p>
<div class="math-display">
$$\\frac{m_e v^2}{r} = \\frac{Z e^2}{4\\pi\\varepsilon_0 r^2} \\implies v = \\frac{Z e^2}{4\\pi\\varepsilon_0 m_e v r} = \\frac{Z e^2}{4\\pi\\varepsilon_0 n \\hbar}$$
</div>
<p>Substituting $v$ into the quantization condition $m_e v r = n\\hbar$ yields the <strong>quantized radius $r_n$</strong>:</p>
<div class="math-display">
$$r_n = \\frac{4\\pi\\varepsilon_0 \\hbar^2}{m_e e^2} \\frac{n^2}{Z} = n^2 \\frac{a_0}{Z}$$
</div>
<p>where the <strong>Bohr radius of hydrogen</strong> ($Z = 1, n = 1$) is:</p>
<div class="math-display">
$$a_0 = \\frac{4\\pi\\varepsilon_0 \\hbar^2}{m_e e^2} = \\frac{4\\pi (8.854 \\times 10^{-12})(1.0546 \\times 10^{-34})^2}{(9.109 \\times 10^{-31})(1.602 \\times 10^{-19})^2} \\approx 0.529177\\,\\text{\\AA} = 0.05292\\,\\text{nm}$$
</div>

<h4>3. Quantized Energy Levels & Rydberg Formula</h4>
<p>The total energy $E_n = K + U = \\frac{1}{2} m_e v^2 - \\frac{Z e^2}{4\\pi\\varepsilon_0 r_n} = - \\frac{Z e^2}{8\\pi\\varepsilon_0 r_n}$:</p>
<div class="math-display">
$$E_n = - \\frac{m_e Z^2 e^4}{32 \\pi^2 \\varepsilon_0^2 \\hbar^2} \\frac{1}{n^2} = - \\frac{13.606\\,\\text{eV} \\times Z^2}{n^2}$$
</div>
<p>For a transition from initial level $n_i$ to final level $n_f$ ($n_i > n_f$), the wavenumber $\\bar{\\nu} = 1/\\lambda$ of the emitted photon is:</p>
<div class="math-display">
$$\\frac{1}{\\lambda} = \\frac{E_i - E_f}{h c} = R_\\infty Z^2 \\left( \\frac{1}{n_f^2} - \\frac{1}{n_i^2} \\right)$$
</div>
<p>where the <strong>Rydberg constant for infinite mass</strong> is:</p>
<div class="math-display">
$$R_\\infty = \\frac{m_e e^4}{8 \\varepsilon_0^2 h^3 c} \\approx 1.097373 \\times 10^7\\,\\text{m}^{-1} = 109,737.3\\,\\text{cm}^{-1}$$
</div>

<h4>4. The Hydrogen Spectral Series</h4>
<table class="data-table" style="width:100%; border-collapse:collapse; margin:16px 0;">
<thead>
<tr style="background:rgba(255,255,255,0.05); text-align:left;">
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Series Name</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Lower State $n_f$</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Upper State $n_i$</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Spectral Region</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">First Line $\lambda$</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Lyman Series</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$n_f = 1$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$2, 3, 4, \\dots$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Ultraviolet</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$121.6\\,\\text{nm}$ ($L_\\alpha$)</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Balmer Series</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$n_f = 2$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$3, 4, 5, \\dots$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Visible / Near-UV</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$656.3\\,\\text{nm}$ ($H_\\alpha$, Red)</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Paschen Series</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$n_f = 3$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$4, 5, 6, \\dots$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Infrared</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$1875.1\\,\\text{nm}$</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Brackett Series</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$n_f = 4$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$5, 6, 7, \\dots$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Infrared</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$4051.2\\,\\text{nm}$</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Pfund Series</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$n_f = 5$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$6, 7, 8, \\dots$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Far Infrared</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$7457.8\\,\\text{nm}$</td>
</tr>
</tbody>
</table>"""
        },
        {
            "id": "u4-sec5",
            "title": "Finite Nuclear Mass, Reduced Mass & The Discovery of Deuterium",
            "content": """<h4>1. Finite Nuclear Mass & Reduced Mass Formulation</h4>
<p>In Bohr's elementary derivation, the nucleus was assumed to have infinite mass ($M = \infty$) and remain strictly fixed at the center of the orbit. In reality, both the electron (mass $m_e$) and nucleus (mass $M$) orbit around their common center of mass.</p>
<p>To account for finite nuclear motion, the electron mass $m_e$ in all dynamical formulas is replaced by the two-body <strong>Reduced Mass $\\mu$</strong>:</p>
<div class="math-display">
$$\\mu = \\frac{m_e M}{m_e + M} = \\frac{m_e}{1 + \\frac{m_e}{M}}$$
</div>
<p>Because $\mu < m_e$, the actual Rydberg constant $R_M$ for an atom with nuclear mass $M$ is slightly smaller than the theoretical infinite-mass constant $R_\infty$:</p>
<div class="math-display">
$$R_M = R_\\infty \\left( \\frac{\\mu}{m_e} \\right) = \\frac{R_\\infty}{1 + \\frac{m_e}{M}}$$
</div>
<p>For ordinary Hydrogen ($^1\text{H}$, $M = m_p \approx 1836.15 m_e$):</p>
<div class="math-display">
$$R_H = \\frac{R_\\infty}{1 + \\frac{1}{1836.15}} = \\frac{R_\\infty}{1.0005446} \\approx 1.096776 \\times 10^7\\,\\text{m}^{-1}$$
</div>

<h4>2. Harold Urey's Discovery of Deuterium (1932)</h4>
<p>Heavy hydrogen, or <strong>Deuterium ($^2\text{H}$ or $\text{D}$)</strong>, possesses a nucleus (deuteron) containing one proton and one neutron, giving it a nuclear mass approximately double that of protium: $M_D \approx 2 m_p \approx 3670.48 m_e$.</p>
<p>The Rydberg constant for deuterium is:</p>
<div class="math-display">
$$R_D = \\frac{R_\\infty}{1 + \\frac{1}{3670.48}} = \\frac{R_\\infty}{1.0002724} \\approx 1.097074 \\times 10^7\\,\\text{m}^{-1}$$
</div>
<p>Because $R_D > R_H$, every spectral line of deuterium is shifted slightly toward shorter wavelengths (higher frequencies) relative to hydrogen. For the red $H_\\alpha$ Balmer line ($n = 3 \\to n = 2$):</p>
<div class="math-display">
$$\\Delta \\lambda = \\lambda_H - \\lambda_D = \\lambda_H \\left( 1 - \\frac{R_H}{R_D} \\right) \\approx (656.3\\,\\text{nm}) \\times (2.72 \\times 10^{-4}) \\approx 0.179\\,\\text{nm} = 1.79\\,\\text{\\AA}$$
</div>
<p>By evaporating liquid hydrogen down to its triple point to concentrate heavy isotopes, Harold Urey and collaborators photographed a faint satellite line shifted by precisely $1.79\,\text{\AA}$ from the $H_\alpha$ line, confirming the existence of deuterium and earning Urey the 1934 Nobel Prize in Chemistry.</p>"""
        },
        {
            "id": "u4-sec6",
            "title": "The Franck-Hertz Experiment: Direct Proof of Quantized Energy Levels",
            "content": """<h4>1. Objective of the Franck-Hertz Experiment (1914)</h4>
<p>While atomic emission spectroscopy revealed discrete light wavelengths, James Franck and Gustav Hertz provided the first <strong>direct non-optical proof</strong> that internal atomic energy states are quantized, demonstrating discrete energy absorption through inelastic electron collisions with mercury vapor atoms.</p>

<h4>2. Experimental Apparatus & Operational Mechanics</h4>
<p>The apparatus consists of a heated glass tube filled with mercury ($\text{Hg}$) vapor at low pressure ($P \\approx 1\\text{ to }10\\,\\text{Torr}$):
<ul>
<li><strong>Cathode (K):</strong> Heated filament emitting electrons with negligible initial thermal energy.</li>
<li><strong>Grid Anode (G):</strong> Fine mesh accelerated by variable forward voltage $V_a$ ($0\\text{ to }30\\,\\text{V}$).</li>
<li><strong>Collector Plate (P):</strong> Positioned beyond the grid, biased with a small retarding reverse voltage $V_r \\approx 1.0\\text{ to }1.5\\,\\text{V}$ relative to the grid.</li>
</ul>
</p>
<p>Electrons reaching the grid must possess kinetic energy $K > e V_r$ to overcome the retarding barrier and register as collector current $I_c$.</p>

<h4>3. Elastic vs. Inelastic Collisions & Current Drops</h4>
<ul>
<li><strong>Low Accelerating Voltages ($V_a < 4.9\\,\\text{V}$):</strong> The kinetic energy of the electrons is insufficient to excite a mercury atom from its ground state ($6^1S_0$) to its first excited state ($6^3P_1$, which lies $4.9\\,\\text{eV}$ higher). The electrons undergo purely <strong>elastic collisions</strong>. Because a mercury atom is $\sim 360,000$ times heavier than an electron, the electron bounces off with essentially zero kinetic energy loss. As $V_a$ increases, collector current $I_c$ rises steadily.</li>
<li><strong>First Inelastic Threshold ($V_a = 4.9\\,\\text{V}$):</strong> As soon as $V_a$ reaches $4.9\\,\\text{V}$, electrons near the grid attain exactly $4.9\\,\\text{eV}$ of kinetic energy. They undergo <strong>inelastic collisions</strong> with mercury atoms, transferring their entire $4.9\\,\\text{eV}$ to excite mercury electrons. Left with near-zero kinetic energy ($K \\approx 0$), these electrons cannot overcome the $1.5\\,\\text{V}$ retarding potential. Collector current $I_c$ plunges sharply!</li>
<li><strong>Periodic Successive Inelastic Drops ($V_a = 9.8\\,\\text{V}, 14.7\\,\\text{V}, 19.6\\,\\text{V}$):</strong> As $V_a$ increases further, electrons gain enough energy to undergo a second inelastic collision at $9.8\\,\\text{V}$ ($2 \\times 4.9\\,\\text{V}$), a third at $14.7\\,\\text{V}$ ($3 \\times 4.9\\,\\text{V}$), and so on.</li>
</ul>
<p>The resulting $I_c$ versus $V_a$ curve exhibits a striking series of periodic peaks and valleys separated by exactly $\Delta V = 4.9\,\text{V}$.</p>
<p><strong>Optical Confirmation:</strong> When mercury atoms de-excite back to the ground state, they emit ultraviolet photons of wavelength:</p>
<div class="math-display">
$$\\lambda = \\frac{h c}{\\Delta E} = \\frac{1240\\,\\text{eV}\\cdot\\text{nm}}{4.9\\,\\text{eV}} \\approx 253\\,\\text{nm}$$
</div>
<p>Franck and Hertz observed the simultaneous appearance of $253.7\,\text{nm}$ UV luminescence as soon as $V_a$ exceeded $4.9\,\text{V}$, clinching the 1925 Nobel Prize in Physics.</p>"""
        }
    ],
    "problems": [
        {
            "id": "u4-prob1",
            "title": "Rutherford Scattering Closest Approach & Cross-Section Calculation",
            "statement": "An alpha particle beam with kinetic energy K = 7.7\\,\\text{MeV} is directed at a thin gold foil (Z = 79, density \\rho = 19.3\\,\\text{g/cm}^3, atomic weight A = 197\\,\\text{g/mol}) of thickness t = 1.0\\,\\mu\\text{m}. (a) Calculate the distance of closest approach d_{min} in a head-on collision (\\theta = 180^\\circ). (b) Calculate the impact parameter b corresponding to a scattering angle of \\theta = 60^\\circ. (c) What fraction f of the incident alpha particles are scattered through angles greater than 90^\\circ?",
            "solution": """<p><strong>Step 1: Calculate Distance of Closest Approach $d_{min}$</strong></p>
<div class="math-display">
$$K = 7.7\\,\\text{MeV} = 7.7 \\times 10^6 \\times 1.6022 \\times 10^{-19}\\,\\text{J} = 1.2337 \\times 10^{-12}\\,\\text{J}$$
</div>
<div class="math-display">
$$d_{min} = \\frac{2 Z e^2}{4\\pi\\varepsilon_0 K} = \\frac{2 \\times 79 \\times (1.6022 \\times 10^{-19})^2}{4\\pi (8.854 \\times 10^{-12}) \\times (1.2337 \\times 10^{-12}\\,\\text{J})} = \\frac{4.056 \\times 10^{-36}}{1.373 \\times 10^{-22}} \\approx 2.954 \\times 10^{-14}\\,\\text{m} = 29.54\\,\\text{fm}$$
</div>

<p><strong>Step 2: Calculate Impact Parameter $b$ for $\\theta = 60^\\circ$</strong></p>
<p>Using the impact parameter relation $b = \\frac{d_{min}}{2} \\cot(\\theta/2)$:</p>
<div class="math-display">
$$b = \\frac{29.54\\,\\text{fm}}{2} \\cot(30^\\circ) = (14.77\\,\\text{fm}) \\times \\sqrt{3} = 14.77 \\times 1.732 \\approx 25.58\\,\\text{fm}$$
</div>

<p><strong>Step 3: Calculate Fraction Scattered Beyond $90^\\circ$</strong></p>
<p>Scattering at angles $\\theta > 90^\\circ$ corresponds to impact parameters $b < b_{90}$:</p>
<div class="math-display">
$$b_{90} = \\frac{d_{min}}{2} \\cot(45^\\circ) = \\frac{29.54\\,\\text{fm}}{2} \\times 1.0 = 14.77\\,\\text{fm} = 1.477 \\times 10^{-14}\\,\\text{m}$$
</div>
<p>The cross-section for scattering beyond $90^\circ$ is $\sigma(> 90^\circ) = \pi b_{90}^2$:</p>
<div class="math-display">
$$\\sigma(> 90^\\circ) = \\pi (1.477 \\times 10^{-14}\\,\\text{m})^2 \\approx 6.853 \\times 10^{-28}\\,\\text{m}^2 = 0.6853\\,\\text{barns}$$
</div>
<p>Number density of target gold atoms $n$:</p>
<div class="math-display">
$$n = \\frac{\\rho N_A}{A} = \\frac{(19.3 \\times 10^3\\,\\text{kg/m}^3)(6.022 \\times 10^{23}\\,\\text{mol}^{-1})}{0.197\\,\\text{kg/mol}} \\approx 5.90 \\times 10^{28}\\,\\text{atoms/m}^3$$
</div>
<p>The fraction $f$ scattered by foil thickness $t = 1.0\\,\\mu\\text{m} = 1.0 \\times 10^{-6}\\,\\text{m}$ is:</p>
<div class="math-display">
$$f = n t \\sigma(> 90^\\circ) = (5.90 \\times 10^{28}\\,\\text{m}^{-3})(1.0 \\times 10^{-6}\\,\\text{m})(6.853 \\times 10^{-28}\\,\\text{m}^2) \\approx 4.04 \\times 10^{-5}$$
</div>
<p>Approximately 1 in every 24,700 incident alpha particles is scattered by more than $90^\circ$.</p>"""
        },
        {
            "id": "u4-prob2",
            "title": "Bohr Model Hydrogenic Transitions & Ionized Helium Spectra",
            "statement": "For singly-ionized helium (He^+, Z = 2): (a) Calculate the radius of the ground state orbit r_1 and the ground state energy E_1 in eV. (b) Find the wavelength of the photon emitted in the transition from n = 4 to n = 2. (c) Compare this wavelength to the corresponding Balmer transition (n = 4 to n = 2) in hydrogen (Z = 1). (d) Find the series limit wavelength for the He^+ Lyman series (n_f = 1).",
            "solution": """<p><strong>Step 1: Ground State Radius and Energy of $\\text{He}^+$</strong></p>
<div class="math-display">
$$r_1(\\text{He}^+) = \\frac{a_0}{Z} = \\frac{0.5292\\,\\text{\\AA}}{2} = 0.2646\\,\\text{\\AA} = 0.02646\\,\\text{nm}$$
</div>
<div class="math-display">
$$E_1(\\text{He}^+) = - (13.606\\,\\text{eV}) \\frac{Z^2}{1^2} = - 13.606 \\times 4 = - 54.424\\,\\text{eV}$$
</div>

<p><strong>Step 2: Transition from $n = 4$ to $n = 2$ in $\\text{He}^+$</strong></p>
<div class="math-display">
$$\\frac{1}{\\lambda} = R_\\infty Z^2 \\left( \\frac{1}{2^2} - \\frac{1}{4^2} \\right) = R_\\infty (4) \\left( \\frac{1}{4} - \\frac{1}{16} \\right) = R_\\infty (4) \\left( \\frac{3}{16} \\right) = \\frac{3}{4} R_\\infty$$
</div>
<div class="math-display">
$$\\lambda = \\frac{4}{3 R_\\infty} = \\frac{4}{3 \\times 1.09737 \\times 10^7\\,\\text{m}^{-1}} \\approx 1.215 \\times 10^{-7}\\,\\text{m} = 121.5\\,\\text{nm}$$
</div>
<p>This emission lies in the ultraviolet spectrum.</p>

<p><strong>Step 3: Comparison with Hydrogen ($Z = 1$)</strong></p>
<p>For Hydrogen ($n = 4 \\to n = 2$, the $H_\\beta$ Balmer line):</p>
<div class="math-display">
$$\\frac{1}{\\lambda_H} = R_\\infty (1)^2 \\left( \\frac{3}{16} \\right) = \\frac{3}{16} R_\\infty \\implies \\lambda_H = \\frac{16}{3 R_\\infty} = 4 \\times \\lambda(\\text{He}^+) = 4 \\times 121.5\\,\\text{nm} = 486.1\\,\\text{nm} \\text{ (Cyan Visible)}$$
</div>
<p>Because wavelengths scale as $1/Z^2$, $\\text{He}^+$ lines are shifted by a factor of 4 toward shorter wavelengths relative to corresponding hydrogen lines.</p>

<p><strong>Step 4: Lyman Series Limit for $\\text{He}^+$ ($n_i = \\infty, n_f = 1$)</strong></p>
<div class="math-display">
$$\\frac{1}{\\lambda_{limit}} = R_\\infty (2^2) \\left( \\frac{1}{1^2} - \\frac{1}{\\infty} \\right) = 4 R_\\infty$$
</div>
<div class="math-display">
$$\\lambda_{limit} = \\frac{1}{4 R_\\infty} = \\frac{1}{4 \\times 1.09737 \\times 10^7\\,\\text{m}^{-1}} \\approx 2.278 \\times 10^{-8}\\,\\text{m} = 22.78\\,\\text{nm}$$
</div>"""
        },
        {
            "id": "u4-prob3",
            "title": "Hydrogen-Deuterium Isotope Shift in the Balmer Alpha Line",
            "statement": "Given the proton mass m_p = 1.67262 \\times 10^{-27}\\,\\text{kg}$, deuteron mass m_d = 3.34358 \\times 10^{-27}\\,\\text{kg}$, electron mass m_e = 9.10938 \\times 10^{-31}\\,\\text{kg}$, and the infinite-mass Rydberg constant R_\\infty = 1.097373 \\times 10^7\\,\\text{m}^{-1}$: (a) Calculate the reduced mass of hydrogen \\mu_H and deuterium \\mu_D. (b) Compute the exact Rydberg constants R_H and R_D. (c) Determine the exact wavelength of the red H_\\alpha line (n = 3 \\to n = 2) for both hydrogen and deuterium. (d) Calculate the isotope shift \\Delta \\lambda = \\lambda_H - \\lambda_D in angstroms.",
            "solution": """<p><strong>Step 1: Calculate Reduced Masses $\\mu_H$ and $\\mu_D$</strong></p>
<div class="math-display">
$$\\frac{m_e}{m_p} = \\frac{9.10938 \\times 10^{-31}}{1.67262 \\times 10^{-27}} \\approx 5.44617 \\times 10^{-4}$$
</div>
<div class="math-display">
$$\\mu_H = \\frac{m_e}{1 + \\frac{m_e}{m_p}} = \\frac{m_e}{1 + 0.000544617} = \\frac{m_e}{1.000544617} \\approx 0.9994557 m_e$$
</div>
<div class="math-display">
$$\\frac{m_e}{m_d} = \\frac{9.10938 \\times 10^{-31}}{3.34358 \\times 10^{-27}} \\approx 2.72444 \\times 10^{-4}$$
</div>
<div class="math-display">
$$\\mu_D = \\frac{m_e}{1 + \\frac{m_e}{m_d}} = \\frac{m_e}{1.000272444} \\approx 0.9997276 m_e$$
</div>

<p><strong>Step 2: Calculate Rydberg Constants $R_H$ and $R_D$</strong></p>
<div class="math-display">
$$R_H = R_\\infty \\left( \\frac{\\mu_H}{m_e} \\right) = (1.097373 \\times 10^7\\,\\text{m}^{-1}) \\times 0.9994557 \\approx 1.096776 \\times 10^7\\,\\text{m}^{-1}$$
</div>
<div class="math-display">
$$R_D = R_\\infty \\left( \\frac{\\mu_D}{m_e} \\right) = (1.097373 \\times 10^7\\,\\text{m}^{-1}) \\times 0.9997276 \\approx 1.097074 \\times 10^7\\,\\text{m}^{-1}$$
</div>

<p><strong>Step 3: Calculate $H_\\alpha$ Wavelengths ($n = 3 \\to n = 2$)</strong></p>
<p>For $n = 3 \\to n = 2$: $\\frac{1}{\\lambda} = R \\left(\\frac{1}{4} - \\frac{1}{9}\\right) = \\frac{5}{36} R \\implies \\lambda = \\frac{36}{5 R}$:</p>
<div class="math-display">
$$\\lambda_H = \\frac{36}{5 \\times 1.096776 \\times 10^7\\,\\text{m}^{-1}} = \\frac{7.2}{1.096776 \\times 10^7} \\approx 6.56469 \\times 10^{-7}\\,\\text{m} = 6564.69\\,\\text{\\AA}$$
</div>
<div class="math-display">
$$\\lambda_D = \\frac{36}{5 \\times 1.097074 \\times 10^7\\,\\text{m}^{-1}} = \\frac{7.2}{1.097074 \\times 10^7} \\approx 6.56291 \\times 10^{-7}\\,\\text{m} = 6562.91\\,\\text{\\AA}$$
</div>

<p><strong>Step 4: Calculate Isotope Shift $\\Delta \\lambda$</strong></p>
<div class="math-display">
$$\\Delta \\lambda = \\lambda_H - \\lambda_D = 6564.69\\,\\text{\\AA} - 6562.91\\,\\text{\\AA} = 1.78\\,\\text{\\AA} = 0.178\\,\\text{nm}$$
</div>
<p>This $1.78\,\text{\AA}$ spectral separation is easily resolved with standard diffraction grating spectrometers, confirming Urey's discovery of deuterium.</p>"""
        }
    ]
}

with open("amp_u3.json", "w") as f:
    json.dump(unit3, f, indent=2)

with open("amp_u4.json", "w") as f:
    json.dump(unit4, f, indent=2)

print("amp_u3.json and amp_u4.json generated successfully!")
