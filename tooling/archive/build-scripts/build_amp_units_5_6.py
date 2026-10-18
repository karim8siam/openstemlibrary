import json

unit5 = {
    "id": "unit-5",
    "number": 5,
    "title": "Quantum Concepts & Detailed Atomic Structure",
    "description": "Rigorous quantum mechanics of the atom: 3D Schrödinger equation in spherical coordinates and hydrogen radial/angular solutions; spatial quantization and the Stern-Gerlach experiment; electron spin and spin-orbit fine structure; Normal and Anomalous Zeeman effects with Landé g-factors; Pauli exclusion principle, Hund's rules, and many-electron term symbols under L-S and j-j coupling.",
    "sections": [
        {
            "id": "u5-sec1",
            "title": "3D Schrödinger Equation for Hydrogenic Atoms: Radial & Angular Solutions",
            "content": """<h4>1. Three-Dimensional Schrödinger Equation in Spherical Coordinates</h4>
<p>For an electron of mass $m_e$ moving in the spherically symmetric Coulomb potential $V(r) = - \\frac{Z e^2}{4\\pi\\varepsilon_0 r}$ of a nucleus with charge $+Ze$, the time-independent Schrödinger equation is:</p>
<div class="math-display">
$$-\\frac{\\hbar^2}{2 m_e} \\nabla^2 \\psi(\\vec{r}) + V(r) \\psi(\\vec{r}) = E \\psi(\\vec{r})$$
</div>
<p>In spherical polar coordinates $(r, \\theta, \\phi)$, the Laplacian operator $\\nabla^2$ decomposes into radial and angular parts:</p>
<div class="math-display">
$$\\nabla^2 = \\frac{1}{r^2} \\frac{\\partial}{\\partial r}\\left( r^2 \\frac{\\partial}{\\partial r} \\right) + \\frac{1}{r^2 \\sin\\theta} \\frac{\\partial}{\\partial \\theta}\\left( \\sin\\theta \\frac{\\partial}{\\partial \\theta} \\right) + \\frac{1}{r^2 \\sin^2\\theta} \\frac{\\partial^2}{\\partial \\phi^2} = \\frac{1}{r^2} \\frac{\\partial}{\\partial r}\\left( r^2 \\frac{\\partial}{\\partial r} \\right) - \\frac{\\hat{L}^2}{\\hbar^2 r^2}$$
</div>
<p>where $\\hat{L}^2$ is the orbital angular momentum operator.</p>

<h4>2. Separation of Variables</h4>
<p>We seek separable solutions of the form $\\psi(r, \\theta, \\phi) = R(r) Y(\\theta, \\phi) = R(r) \\Theta(\\theta) \\Phi(\\phi)$. Substituting into the Schrödinger equation yields two uncoupled differential equations:
<ol>
<li><strong>Angular Equation (Spherical Harmonics):</strong>
<div class="math-display">
$$\\hat{L}^2 Y_{lm}(\\theta, \\phi) = l(l+1) \\hbar^2 Y_{lm}(\\theta, \\phi), \\quad \\hat{L}_z Y_{lm}(\\theta, \\phi) = m_l \\hbar Y_{lm}(\\theta, \\phi)$$
</div>
The solutions are the <strong>Spherical Harmonics $Y_{lm}(\\theta, \\phi) = \\Theta_{lm}(\\theta) \\Phi_m(\\phi)$</strong>, where $\\Phi_m(\\phi) = \\frac{1}{\\sqrt{2\\pi}} e^{i m_l \\phi}$ and $\\Theta_{lm}(\\theta)$ are the normalized Associated Legendre polynomials $P_l^{|m_l|}(\\cos\\theta)$.</li>
<li><strong>Radial Wave Equation:</strong>
<div class="math-display">
$$\\frac{1}{r^2} \\frac{d}{dr}\\left( r^2 \\frac{dR}{dr} \\right) + \\left[ \\frac{2 m_e}{\\hbar^2} \\left( E + \\frac{Z e^2}{4\\pi\\varepsilon_0 r} \\right) - \\frac{l(l+1)}{r^2} \\right] R(r) = 0$$
</div>
The term $\\frac{l(l+1)\\hbar^2}{2 m_e r^2}$ acts as an effective repulsive <strong>centrifugal potential barrier</strong> preventing electrons with non-zero orbital angular momentum from collapsing into $r = 0$.</li>
</ol>
</p>

<h4>3. Bound State Eigenvalues & Associated Laguerre Polynomials</h4>
<p>Requiring the radial wavefunction $R(r)$ to remain finite at $r = 0$ and decay exponentially as $r \\to \\infty$ constrains the energy to discrete quantized values governed by the <strong>Principal Quantum Number $n$</strong>:</p>
<div class="math-display">
$$E_n = - \\frac{m_e Z^2 e^4}{32 \\pi^2 \\varepsilon_0^2 \\hbar^2} \\frac{1}{n^2} = - \\frac{13.606\\,\\text{eV} \\times Z^2}{n^2} \\quad (n = 1, 2, 3, \\dots)$$
</div>
<p>The normalized radial wavefunctions are expressed in terms of the Associated Laguerre polynomials $L_{n-l-1}^{2l+1}(\\rho)$:</p>
<div class="math-display">
$$R_{nl}(r) = - \\left( \\frac{2 Z}{n a_0} \\right)^{3/2} \\sqrt{\\frac{(n-l-1)!}{2n [(n+l)!]^3}} e^{-\\rho/2} \\rho^l L_{n+l}^{2l+1}(\\rho), \\quad \\rho = \\frac{2 Z r}{n a_0}$$
</div>
<p>For the ground state ($n=1, l=0, m_l=0$): $\\psi_{100}(r) = \\frac{1}{\\sqrt{\\pi a_0^3}} e^{-r/a_0}$.</p>"""
        },
        {
            "id": "u5-sec2",
            "title": "The Four Quantum Numbers & Spatial Orbital Probability Densities",
            "content": """<h4>1. Hierarchy of the Four Quantum Numbers</h4>
<p>Every quantum electronic state in an atom is uniquely specified by a set of four quantum numbers:
<ol>
<li><strong>Principal Quantum Number ($n = 1, 2, 3, \\dots$):</strong> Dictates the primary energy shell and the mean distance of the electron from the nucleus ($\langle r \rangle \approx n^2 a_0 / Z$).</li>
<li><strong>Orbital Angular Momentum Quantum Number ($l = 0, 1, 2, \\dots, n-1$):</strong> Determines the subshell ($s, p, d, f, g$) and the magnitude of the orbital angular momentum:
<div class="math-display">
$$|\\vec{L}| = \\sqrt{l(l+1)} \\hbar$$
</div>
Notice that for the ground state ($n=1$), $l=0$, so orbital angular momentum is strictly zero ($L = 0$). This directly overturned Bohr's ad-hoc assumption that $L = 1\\hbar$ in the ground state!</li>
<li><strong>Magnetic Quantum Number ($m_l = -l, -l+1, \\dots, 0, \\dots, +l$):</strong> Defines the spatial orientation of the angular momentum vector relative to a chosen quantization axis ($z$-axis):
<div class="math-display">
$$L_z = m_l \\hbar \\quad (2l + 1 \\text{ degenerate orientations})$$
</div></li>
<li><strong>Spin Magnetic Quantum Number ($m_s = \\pm 1/2$):</strong> Specifies the orientation of the intrinsic electron spin angular momentum along the $z$-axis:
<div class="math-display">
$$S_z = m_s \\hbar = \\pm \\frac{1}{2} \\hbar$$
</div></li>
</ol>
</p>

<h4>2. Radial Probability Density Distribution</h4>
<p>The probability of finding the electron in a spherical shell of radius $r$ and thickness $dr$ (integrated over all angles) is given by the <strong>Radial Probability Density $P(r)$</strong>:</p>
<div class="math-display">
$$P(r) dr = \\int_0^{2\\pi} d\\phi \\int_0^\\pi \\sin\\theta d\\theta \\, |\\psi(r, \\theta, \\phi)|^2 r^2 dr = r^2 |R_{nl}(r)|^2 dr$$
</div>
<p>For the ground state of hydrogen ($n=1, l=0$):</p>
<div class="math-display">
$$P(r) = r^2 \\left( \\frac{4}{a_0^3} e^{-2r/a_0} \\right) = \\frac{4 r^2}{a_0^3} e^{-2r/a_0}$$
</div>
<p>To find the most probable radius, differentiate $P(r)$ with respect to $r$ and set to zero:</p>
<div class="math-display">
$$\\frac{dP}{dr} = \\frac{4}{a_0^3} \\left( 2r e^{-2r/a_0} - \\frac{2r^2}{a_0} e^{-2r/a_0} \\right) = \\frac{8 r}{a_0^3} \\left( 1 - \\frac{r}{a_0} \\right) e^{-2r/a_0} = 0 \\implies r_{mp} = a_0$$
</div>
<p>The maximum of the radial probability density curve occurs at exactly $r = a_0 = 0.529\,\text{\AA}$—recovering Bohr's first orbit radius as the peak of a 3D probability cloud.</p>"""
        },
        {
            "id": "u5-sec3",
            "title": "Space Quantization & The Stern-Gerlach Experiment",
            "simulation": "stern-gerlach-spin-sim",
            "content": """<h4>1. Concept of Spatial Quantization</h4>
<p>In classical physics, a magnetic dipole moment $\\vec{\\mu}$ can orient itself in any arbitrary continuous direction in space relative to an applied magnetic field $\\vec{B}$. Quantum mechanics predicts <strong>Spatial Quantization</strong>: the magnetic dipole can only orient at discrete quantized angles $\\theta$ such that its projection along the field axis is quantized:</p>
<div class="math-display">
$$\\cos\\theta = \\frac{L_z}{|\\vec{L}|} = \\frac{m_l \\hbar}{\\sqrt{l(l+1)}\\hbar} = \\frac{m_l}{\\sqrt{l(l+1)}}$$
</div>

<h4>2. The Stern-Gerlach Apparatus & Force Derivation (1922)</h4>
<p>Otto Stern and Walther Gerlach tested space quantization by directing a collimated beam of neutral silver atoms ($Z = 47$) through an inhomogeneous magnetic field.</p>
<p>In a uniform magnetic field, a magnetic dipole experiences only a torque ($\vec{\tau} = \vec{\mu} \times \vec{B}$) aligning it, but zero net translatory force ($\vec{F} = \vec{0}$). However, in an <strong>inhomogeneous field</strong> with gradient $\\frac{\\partial B_z}{\\partial z} \\neq 0$, the potential energy is $U = - \\vec{\\mu} \\cdot \\vec{B} = - \\mu_z B_z$. A net deflecting force acts on the atoms:</p>
<div class="math-display">
$$F_z = - \\frac{\\partial U}{\\partial z} = \\mu_z \\frac{\\partial B_z}{\\partial z}$$
</div>
<p>Classically, because atomic magnetic moments would be randomly distributed over all directions ($-1 \\le \\cos\\theta \\le +1$), the atomic beam should broaden continuously into a single uniform smeared patch on the detector plate.</p>

<h4>3. The Experimental Result & Discovery of Electron Spin</h4>
<p>Stern and Gerlach observed that the beam did <strong>NOT</strong> smear continuously. Instead, it split cleanly into <strong>two distinct, symmetric, separated traces</strong>!</p>
<p><strong>The Theoretical Puzzle & Resolution:</strong>
Silver has a single valence electron outside closed shells: $[\text{Kr}] 4d^{10} 5s^1$. For an $s$-electron, orbital angular momentum is $l = 0$. If the magnetic moment were purely orbital ($\mu_L$), then $m_l = 0$, so $\mu_z = 0$, predicting zero deflection (a single undeflected spot)!
Furthermore, if orbital angular momentum $l$ were responsible, the number of split beams would be $2l + 1$, which is always an <strong>odd integer</strong> ($1, 3, 5, \dots$). The observed splitting into an <strong>even number (2)</strong> was impossible under orbital quantization alone!</p>
<p>In 1925, Samuel Goudsmit and George Uhlenbeck solved the enigma by proposing that the electron possesses an intrinsic angular momentum termed <strong>Electron Spin $\\vec{S}$</strong> with spin quantum number $s = 1/2$. The spin angular momentum magnitude and $z$-component are:</p>
<div class="math-display">
$$|\\vec{S}| = \\sqrt{s(s+1)}\\hbar = \\frac{\\sqrt{3}}{2} \\hbar, \\quad S_z = m_s \\hbar = \\pm \\frac{1}{2} \\hbar \\quad (m_s = +1/2, -1/2)$$
</div>
<p>The associated spin magnetic dipole moment is:</p>
<div class="math-display">
$$\\vec{\\mu}_s = - g_s \\left( \\frac{e}{2 m_e} \\right) \\vec{S} = - \\frac{g_s \\mu_B}{\\hbar} \\vec{S}$$
</div>
<p>where $g_s \\approx 2.00232$ is the electron spin $g$-factor, and $\\mu_B$ is the <strong>Bohr Magneton</strong>:</p>
<div class="math-display">
$$\\mu_B = \\frac{e \\hbar}{2 m_e} = \\frac{(1.602 \\times 10^{-19})(1.0546 \\times 10^{-34})}{2(9.109 \\times 10^{-31})} \\approx 9.274 \\times 10^{-24}\\,\\text{J/T} = 5.788 \\times 10^{-5}\\,\\text{eV/T}$$
</div>
<p>The two split beams corresponded to the two discrete spin orientations: "spin-up" ($m_s = +1/2$) and "spin-down" ($m_s = -1/2$).</p>"""
        },
        {
            "id": "u5-sec4",
            "title": "Spin-Orbit Interaction, Thomas Precession & Fine Structure of Alkali Doublets",
            "content": """<h4>1. Physical Origin of Spin-Orbit Coupling</h4>
<p>In the rest frame of the nucleus, an electron orbits with velocity $\vec{v}$ in an electrostatic field $\vec{E} = - \nabla V(r)$. Transforming to the instantaneous rest frame of the orbiting electron, the moving nuclear charge creates an effective magnetic field:</p>
<div class="math-display">
$$\\vec{B}_{int} = - \\frac{\\vec{v} \\times \\vec{E}}{c^2} = \\frac{1}{m_e c^2 r} \\frac{dV}{dr} (\\vec{r} \\times m_e \\vec{v}) = \\frac{1}{m_e c^2 r} \\frac{dV}{dr} \\vec{L}$$
</div>
<p>The intrinsic spin magnetic dipole $\\vec{\\mu}_s = - \\frac{g_s e}{2m_e} \\vec{S} \\approx - \\frac{e}{m_e} \\vec{S}$ interacts with this internal magnetic field with energy $U' = - \\vec{\\mu}_s \\cdot \\vec{B}_{int}$.</p>
<p>Accounting for relativistic <strong>Thomas Precession</strong> (a factor of $1/2$ arising from the non-inertial accelerating frame of the rotating electron), the exact <strong>Spin-Orbit Hamiltonian $H_{so}$</strong> is:</p>
<div class="math-display">
$$H_{so} = \\frac{1}{2 m_e^2 c^2} \\left( \\frac{1}{r} \\frac{dV}{dr} \\right) \\vec{L} \\cdot \\vec{S} = \\xi(r) \\vec{L} \\cdot \\vec{S}$$
</div>

<h4>2. Evaluation of the $\\vec{L} \\cdot \\vec{S}$ Scalar Product</h4>
<p>The total angular momentum is the vector sum $\\vec{J} = \\vec{L} + \\vec{S}$. Squaring both sides:</p>
<div class="math-display">
$$\\vec{J}^2 = (\\vec{L} + \\vec{S})^2 = \\vec{L}^2 + \\vec{S}^2 + 2 \\vec{L} \\cdot \\vec{S} \\implies \\vec{L} \\cdot \\vec{S} = \\frac{1}{2} (\\vec{J}^2 - \\vec{L}^2 - \\vec{S}^2)$$
</div>
<p>Evaluating in an eigenstate of total angular momentum $|j, l, s\\rangle$:</p>
<div class="math-display">
$$\\langle \\vec{L} \\cdot \\vec{S} \\rangle = \\frac{\\hbar^2}{2} [ j(j+1) - l(l+1) - s(s+1) ]$$
</div>
<p>For a single electron ($s = 1/2$), the allowed total angular momentum quantum numbers are $j = l + 1/2$ and $j = l - 1/2$ (for $l > 0$).
<ul>
<li>For $j = l + 1/2$: $\langle \\vec{L}\\cdot\\vec{S} \\rangle = +\\frac{1}{2} l \\hbar^2$ (Energy shifted upward)</li>
<li>For $j = l - 1/2$: $\langle \\vec{L}\\cdot\\vec{S} \\rangle = -\\frac{1}{2} (l + 1) \\hbar^2$ (Energy shifted downward)</li>
</ul>
</p>
<p>The spin-orbit interaction splits every state with $l > 0$ into a fine-structure doublet separated by energy:</p>
<div class="math-display">
$$\\Delta E_{so} = \\frac{2l + 1}{2} \\hbar^2 \\langle \\xi(r) \\rangle$$
</div>

<h4>3. Fine Structure of the Sodium D-Lines</h4>
<p>In sodium ($Z = 11$, single valence electron $[\text{Ne}]3s^1$), the first excited $3p$ state ($l = 1, s = 1/2$) splits into two states:
<ul>
<li>$^2P_{3/2}$ ($j = 3/2$, higher energy)</li>
<li>$^2P_{1/2}$ ($j = 1/2$, lower energy)</li>
</ul>
</p>
<p>When the electron decays to the ground state $3s_{1/2}$ ($l = 0, j = 1/2$), it emits two closely spaced yellow spectral lines—the famous <strong>Sodium D-Lines</strong>:
<ol>
<li><strong>$D_2$ Line ($3^2P_{3/2} \\to 3^2S_{1/2}$):</strong> Wavelength $\\lambda_2 = 589.0\\,\\text{nm}$ (higher frequency, larger energy transition)</li>
<li><strong>$D_1$ Line ($3^2P_{1/2} \\to 3^2S_{1/2}$):</strong> Wavelength $\\lambda_1 = 589.6\\,\\text{nm}$</li>
</ol>
</p>
<p>The splitting $\Delta \lambda = 0.6\,\text{nm}$ ($17.2\,\text{cm}^{-1} \approx 2.13\,\text{meV}$) provides direct macroscopic optical verification of relativistic spin-orbit coupling.</p>"""
        },
        {
            "id": "u5-sec5",
            "title": "Magnetic Field Effects: Normal & Anomalous Zeeman Effect & Paschen-Back Effect",
            "simulation": "zeeman-effect-splitting-sim",
            "content": """<h4>1. The Normal Zeeman Effect (Singlet States, $S = 0$)</h4>
<p>Pieter Zeeman (1896) discovered that when a light source is placed in an external magnetic field $\vec{B} = B \hat{z}$, its spectral lines split into closely spaced polarized components.</p>
<p>In atoms where total spin is zero ($S = 0$, such as singlet states in Cadmium, Zinc, or Helium), the interaction Hamiltonian is purely orbital:</p>
<div class="math-display">
$$H_B = - \\vec{\\mu}_L \\cdot \\vec{B} = \\frac{e}{2 m_e} L_z B = \\mu_B B m_l \\quad (m_l = -l, \\dots, +l)$$
</div>
<p>The energy of each level is shifted by:</p>
<div class="math-display">
$$\\Delta E = m_l \\mu_B B$$
</div>
<p>Under the electric dipole selection rule $\\Delta m_l = 0, \\pm 1$:</p>
<div class="math-display">
$$h\\nu = (E_i + m_{li} \\mu_B B) - (E_f + m_{lf} \\mu_B B) = h\\nu_0 + \\Delta m_l \\mu_B B$$
</div>
<p>A single spectral line splits into exactly three components (the <strong>Lorentz Triplet</strong>):
<ol>
<li><strong>$\\pi$-Component ($\\Delta m_l = 0$):</strong> Unshifted frequency $\\nu = \\nu_0$, linearly polarized parallel to $\\vec{B}$.</li>
<li><strong>$\\sigma$-Components ($\\Delta m_l = \\pm 1$):</strong> Shifted frequencies $\\nu = \\nu_0 \\pm \\frac{\\mu_B B}{h} = \\nu_0 \\pm \\frac{e B}{4\\pi m_e}$, circularly polarized perpendicular to $\\vec{B}$.</li>
</ol>
</p>

<h4>2. The Anomalous Zeeman Effect & The Landé g-Factor ($S \neq 0$)</h4>
<p>For states with non-zero spin ($S \neq 0$), because the spin $g$-factor ($g_s \approx 2$) is double the orbital $g$-factor ($g_l = 1$), the total magnetic moment $\vec{\mu} = - \frac{\mu_B}{\hbar}(\vec{L} + 2\vec{S})$ is <strong>not parallel</strong> to the total angular momentum $\vec{J} = \vec{L} + \vec{S}$.</p>
<p>By the Wigner-Eckart projection theorem, only the component of $\vec{\mu}$ parallel to $\vec{J}$ survives time-averaging:</p>
<div class="math-display">
$$\\vec{\\mu}_J = - g_J \\frac{\\mu_B}{\\hbar} \\vec{J}$$
</div>
<p>where $g_J$ is the <strong>Landé $g$-Factor</strong>:</p>
<div class="math-display">
$$g_J = 1 + \\frac{J(J+1) + S(S+1) - L(L+1)}{2 J(J+1)}$$
</div>
<p>In an external magnetic field $B$, each level splits into $2J + 1$ equidistant sublevels:</p>
<div class="math-display">
$$\\Delta E = g_J \\mu_B B m_j \\quad (m_j = -J, -J+1, \\dots, +J)$$
</div>
<p>Because the initial and final states have different Landé $g$-factors ($g_i \neq g_f$), the transition frequencies split into complex multiplets (e.g., 4 lines for the Sodium $D_1$ line, 6 lines for the $D_2$ line). This was termed "anomalous" until spin was discovered.</p>

<h4>3. The Paschen-Back Effect (Strong Magnetic Field Limit)</h4>
<p>When the external magnetic field $B$ is made so powerful that the magnetic interaction energy $\mu_B B$ overwhelms the internal spin-orbit coupling energy ($\Delta E_{so}$), the coupling between $\vec{L}$ and $\vec{S}$ is broken.
$\\vec{L}$ and $\vec{S}$ precess independently around $\vec{B}$, and the good quantum numbers revert to $(m_l, m_s)$. The energy shift becomes:</p>
<div class="math-display">
$$\\Delta E = \\mu_B B (m_l + 2 m_s)$$
</div>
<p>Applying selection rules $\Delta m_s = 0$ and $\Delta m_l = 0, \pm 1$, the complex anomalous multiplet collapses back into a simple three-line normal Lorentz triplet!</p>"""
        },
        {
            "id": "u5-sec6",
            "title": "Many-Electron Atoms: L-S vs j-j Coupling & Spectroscopic Term Symbols",
            "content": """<h4>1. Angular Momentum Coupling Schemes in Multi-Electron Atoms</h4>
<p>In an atom containing multiple valence electrons, the electrostatic Coulomb repulsions between electrons compete with internal spin-orbit interactions:</p>
<ul>
<li><strong>$L-S$ (Russell-Saunders) Coupling (Light to Medium Atoms, $Z < 30$):</strong> Residual Coulomb interactions dominate over spin-orbit interactions.
The individual orbital angular momenta couple strongly into a total orbital angular momentum:
<div class="math-display">
$$\\vec{L} = \\sum_i \\vec{l}_i$$
</div>
The individual spins couple strongly into a total spin angular momentum:
<div class="math-display">
$$\\vec{S} = \\sum_i \\vec{s}_i$$
</div>
Finally, $\\vec{L}$ and $\\vec{S}$ couple weakly via spin-orbit interaction into total angular momentum $\\vec{J} = \\vec{L} + \\vec{S}$, where:
<div class="math-display">
$$|L - S| \\le J \\le L + S$$
</div></li>
<li><strong>$j-j$ Coupling (Heavy Atoms, $Z > 70$):</strong> In heavy atoms with large nuclear charge, spin-orbit coupling is colossal ($\propto Z^4$). For each electron individually, its spin $\vec{s}_i$ couples strongly to its own orbital momentum $\vec{l}_i$ to form $\vec{j}_i = \vec{l}_i + \vec{s}_i$. The individual $\vec{j}_i$ vectors then couple weakly to form total $\vec{J} = \sum \vec{j}_i$.</li>
</ul>

<h4>2. Spectroscopic Term Symbols</h4>
<p>Under Russell-Saunders coupling, an atomic energy level is designated by the standard <strong>Term Symbol</strong>:</p>
<div class="math-display">
$$^{2S+1}L_J$$
</div>
<p>where:
<ul>
<li>$2S + 1$ is the <strong>Multiplicity</strong> (Singlet for $S=0$, Doublet for $S=1/2$, Triplet for $S=1$, Quartet for $S=3/2$).</li>
<li>$L$ is represented by spectroscopic capital letters: $S$ ($L=0$), $P$ ($L=1$), $D$ ($L=2$), $F$ ($L=3$), $G$ ($L=4$).</li>
<li>$J$ is the total angular momentum quantum number written as a subscript.</li>
</ul>
</p>

<h4>3. Hund's Rules for Ground-State Term Determination</h4>
<p>To determine the ground state term of an equivalent electron configuration:
<ol>
<li><strong>Rule 1:</strong> The term with the maximum multiplicity ($2S+1$) has the lowest energy (minimizes electron-electron Coulomb repulsion by keeping spins parallel).</li>
<li><strong>Rule 2:</strong> For a given spin multiplicity, the term with the largest total orbital angular momentum $L$ has the lowest energy.</li>
<li><strong>Rule 3:</strong> For a given $L$ and $S$:
  <ul>
  <li>If the subshell is <strong>less than half-full</strong>, the level with the lowest $J = |L - S|$ has the lowest energy (regular multiplet).</li>
  <li>If the subshell is <strong>more than half-full</strong>, the level with the highest $J = L + S$ has the lowest energy (inverted multiplet).</li>
  </ul>
</li>
</ol>
</p>

<h4>4. Electric Dipole Selection Rules</h4>
<p>Allowed radiative transitions are governed by the electric dipole operator selection rules:
<div class="math-display">
$$\\Delta S = 0 \\quad (\\text{Intercombination transitions between different multiplicities are forbidden})$$
</div>
<div class="math-display">
$$\\Delta L = 0, \\pm 1 \\quad (\\text{with } L = 0 \\to L = 0 \\text{ strictly forbidden})$$
</div>
<div class="math-display">
$$\\Delta J = 0, \\pm 1 \\quad (\\text{with } J = 0 \\to J = 0 \\text{ strictly forbidden})$$
</div>
<div class="math-display">
$$\\Delta M_J = 0, \\pm 1$$
</div>
</p>"""
        }
    ],
    "problems": [
        {
            "id": "u5-prob1",
            "title": "Spin-Orbit Internal Magnetic Field & Fine Structure Splitting",
            "statement": "The Sodium doublet lines have measured wavelengths \\lambda_1 = 589.6\\,\\text{nm} (3^2P_{1/2} \\to 3^2S_{1/2}) and \\lambda_2 = 589.0\\,\\text{nm} (3^2P_{3/2} \\to 3^2S_{1/2}). (a) Calculate the fine structure energy difference \\Delta E_{so} between the 3^2P_{3/2} and 3^2P_{1/2} levels in eV and in wavenumber units (cm^{-1}). (b) Using \\Delta E_{so} = \\mu_B B_{int} (g_1 - g_2) / \\dots, estimate the effective internal magnetic field B_{int} experienced by the 3p electron due to its orbital motion.",
            "solution": """<p><strong>Step 1: Calculate Energy Splitting $\\Delta E_{so}$</strong></p>
<div class="math-display">
$$\\Delta E_{so} = E_2 - E_1 = h c \\left( \\frac{1}{\\lambda_2} - \\frac{1}{\\lambda_1} \\right) = h c \\left( \\frac{\\lambda_1 - \\lambda_2}{\\lambda_1 \\lambda_2} \\right)$$
</div>
<div class="math-display">
$$\\Delta \\lambda = 589.6\\,\\text{nm} - 589.0\\,\\text{nm} = 0.60\\,\\text{nm} = 6.0 \\times 10^{-10}\\,\\text{m}$$
</div>
<div class="math-display">
$$\\lambda_1 \\lambda_2 \\approx (589.3 \\times 10^{-9}\\,\\text{m})^2 \\approx 3.473 \\times 10^{-13}\\,\\text{m}^2$$
</div>
<div class="math-display">
$$\\Delta E_{so} = \\frac{(6.626 \\times 10^{-34}\\,\\text{J}\\cdot\\text{s})(2.998 \\times 10^8\\,\\text{m/s})(6.0 \\times 10^{-10}\\,\\text{m})}{3.473 \\times 10^{-13}\\,\\text{m}^2} = \\frac{1.192 \\times 10^{-34}}{3.473 \\times 10^{-13}} \\approx 3.432 \\times 10^{-22}\\,\\text{J}$$
</div>
<p>Converting to electron-volts:</p>
<div class="math-display">
$$\\Delta E_{so} = \\frac{3.432 \\times 10^{-22}\\,\\text{J}}{1.6022 \\times 10^{-19}\\,\\text{J/eV}} \\approx 2.142 \\times 10^{-3}\\,\\text{eV} = 2.142\\,\\text{meV}$$
</div>
<p>In wavenumber units:</p>
<div class="math-display">
$$\\Delta \\bar{\\nu} = \\frac{\\Delta E_{so}}{h c} = \\frac{3.432 \\times 10^{-22}}{(6.626 \\times 10^{-34})(3.0 \\times 10^{10}\\,\\text{cm/s})} \\approx 17.27\\,\\text{cm}^{-1}$$
</div>

<p><strong>Step 2: Calculate Effective Internal Magnetic Field $B_{int}$</strong></p>
<p>The energy difference between spin parallel ($j = 3/2$) and spin antiparallel ($j = 1/2$) to the orbital field is:</p>
<div class="math-display">
$$\\Delta E_{so} = 2 \\mu_B B_{int}$$
</div>
<div class="math-display">
$$B_{int} = \\frac{\\Delta E_{so}}{2 \\mu_B} = \\frac{3.432 \\times 10^{-22}\\,\\text{J}}{2 \\times (9.274 \\times 10^{-24}\\,\\text{J/T})} = \\frac{3.432 \\times 10^{-22}}{1.8548 \\times 10^{-23}} \\approx 18.5\\,\\text{Tesla}$$
</div>
<p>The internal magnetic field generated by the electron's orbital motion is colossal—approximately $18.5\\,\\text{Tesla}$, exceeding typical laboratory benchtop electromagnets!</p>"""
        },
        {
            "id": "u5-prob2",
            "title": "Landé g-Factor & Anomalous Zeeman Spectral Splitting",
            "statement": "An atom in a weak external magnetic field of B = 1.50\\,\\text{Tesla} undergoes a transition between the ^2P_{3/2} state and the ^2S_{1/2} ground state. (a) Calculate the Landé g-factor for both the ^2P_{3/2} and ^2S_{1/2} states. (b) Determine the number of magnetic sublevels for each state and their energy shifts in eV. (c) Determine the number of allowed optical transitions using electric dipole selection rules \\Delta m_j = 0, \\pm 1.",
            "solution": """<p><strong>Step 1: Calculate Landé $g$-Factors</strong></p>
<p>Using $g_J = 1 + \\frac{J(J+1) + S(S+1) - L(L+1)}{2 J(J+1)}$:</p>
<p>For $^2S_{1/2}$ ($L = 0, S = 1/2, J = 1/2$):</p>
<div class="math-display">
$$g_1 = 1 + \\frac{\\frac{1}{2}(\\frac{3}{2}) + \\frac{1}{2}(\\frac{3}{2}) - 0}{2 \\times \\frac{1}{2}(\\frac{3}{2})} = 1 + \\frac{\\frac{3}{4} + \\frac{3}{4}}{\\frac{3}{2}} = 1 + 1 = 2.00$$
</div>
<p>For $^2P_{3/2}$ ($L = 1, S = 1/2, J = 3/2$):</p>
<div class="math-display">
$$g_2 = 1 + \\frac{\\frac{3}{2}(\\frac{5}{2}) + \\frac{1}{2}(\\frac{3}{2}) - 1(2)}{2 \\times \\frac{3}{2}(\\frac{5}{2})} = 1 + \\frac{\\frac{15}{4} + \\frac{3}{4} - 2}{\\frac{15}{2}} = 1 + \\frac{\\frac{18}{4} - 2}{\\frac{15}{2}} = 1 + \\frac{2.5}{7.5} = 1 + \\frac{1}{3} = \\frac{4}{3} \\approx 1.333$$
</div>

<p><strong>Step 2: Energy Splitting of Sublevels</strong></p>
<p>Bohr magneton energy in $B = 1.50\\,\\text{T}$:</p>
<div class="math-display">
$$\\mu_B B = (5.788 \\times 10^{-5}\\,\\text{eV/T}) \\times 1.50\\,\\text{T} \\approx 8.682 \\times 10^{-5}\\,\\text{eV} = 86.82\\,\\mu\\text{eV}$$
</div>
<ul>
<li><strong>Ground State $^2S_{1/2}$ ($g = 2$):</strong> 2 sublevels ($m_j = \\pm 1/2$):
<div class="math-display">
$$\\Delta E = g \\mu_B B m_j = 2 \\times (86.82\\,\\mu\\text{eV}) \\times (\\pm 1/2) = \\pm 86.82\\,\\mu\\text{eV}$$
</div></li>
<li><strong>Excited State $^2P_{3/2}$ ($g = 4/3$):</strong> 4 sublevels ($m_j = +3/2, +1/2, -1/2, -3/2$):
<div class="math-display">
$$\\Delta E = \\frac{4}{3} (86.82\\,\\mu\\text{eV}) m_j = (115.76\\,\\mu\\text{eV}) m_j = \\pm 173.64\\,\\mu\\text{eV}, \\, \\pm 57.88\\,\\mu\\text{eV}$$
</div></li>
</ul>

<p><strong>Step 3: Allowed Optical Transitions</strong></p>
<p>Applying the selection rule $\\Delta m_j = m_{j2} - m_{j1} = 0, \\pm 1$ yields exactly <strong>6 allowed spectral lines</strong>:
<ul>
<li>$\\Delta m_j = +1$ (2 lines: $+3/2 \\to +1/2$, $+1/2 \\to -1/2$) — $\\sigma$-polarized</li>
<li>$\\Delta m_j = 0$ (2 lines: $+1/2 \\to +1/2$, $-1/2 \\to -1/2$) — $\\pi$-polarized</li>
<li>$\\Delta m_j = -1$ (2 lines: $-1/2 \\to +1/2$, $-3/2 \\to -1/2$) — $\\sigma$-polarized</li>
</ul>
</p>
<p>The single original spectral line splits into a symmetric 6-line anomalous Zeeman sextet.</p>"""
        },
        {
            "id": "u5-prob3",
            "title": "Derivation of Allowed Term Symbols for Equivalent p^2 Configuration",
            "statement": "For an atom with two equivalent p-electrons (p^2 configuration, such as Carbon in its ground state): (a) Determine all possible combinations of quantum numbers (m_{l1}, m_{s1}, m_{l2}, m_{s2}) satisfying the Pauli exclusion principle. (b) Group the allowed microstates into spectroscopic terms ^{2S+1}L_J. (c) Use Hund's rules to identify the ground state term symbol.",
            "solution": """<p><strong>Step 1: Total Number of Microstates</strong></p>
<p>For a $p$-subshell ($l = 1$), there are $2(2l+1) = 6$ spin-orbital states. The number of ways to place 2 indistinguishable electrons into 6 states is:</p>
<div class="math-display">
$$N = \\binom{6}{2} = \\frac{6 \\times 5}{2} = 15\\,\\text{microstates}$$
</div>

<p><strong>Step 2: Table of Microstates Classified by $(M_L, M_S)$</strong></p>
<p>Each microstate is $(m_{l1}, m_{s1}; m_{l2}, m_{s2})$ with $M_L = m_{l1} + m_{l2}$ and $M_S = m_{s1} + m_{s2}$, subject to the Pauli exclusion principle: no two electrons can have identical $(m_l, m_s)$.</p>
<ul>
<li><strong>Maximum $M_L = 2$:</strong> Requires $m_{l1} = 1, m_{l2} = 1$. Since $m_l$ values are identical, spins must be opposite: $m_{s1} = +1/2, m_{s2} = -1/2 \implies M_S = 0$.
This represents 1 state with $(M_L = 2, M_S = 0)$. It must belong to a term with $L = 2, S = 0$, which is <strong>$^1D$</strong> ($^1D_2$, containing $2L+1 = 5$ states: $M_L = 2, 1, 0, -1, -2$ all with $M_S = 0$).</li>
<li><strong>Maximum $M_S = 1$:</strong> Spins must be parallel ($+1/2, +1/2$). The electrons must have different $m_l$.
Possible pairs: $(1, 0) \implies M_L = 1$; $(1, -1) \implies M_L = 0$; $(0, -1) \implies M_L = -1$.
This gives $M_L = 1, 0, -1$ with $M_S = 1$, which belongs to a term with $L = 1, S = 1$, which is <strong>$^3P$</strong> ($9$ states: $J = 2, 1, 0$).</li>
<li><strong>Remaining State at $(M_L = 0, M_S = 0)$:</strong> After subtracting $5$ states for $^1D$ and $9$ states for $^3P$ from the $15$ total states, exactly $1$ state remains at $(M_L = 0, M_S = 0)$. This belongs to <strong>$^1S$</strong> ($^1S_0$, $1$ state).</li>
</ul>
<p>The allowed terms for a $p^2$ configuration are: <strong>$^1D_2$</strong>, <strong>$^3P_0, ^3P_1, ^3P_2$</strong>, and <strong>$^1S_0$</strong> (Total states = $5 + 9 + 1 = 15$).</p>

<p><strong>Step 3: Determine Ground State using Hund's Rules</strong></p>
<ol>
<li><strong>Hund's Rule 1 (Maximum Spin Multiplicity):</strong> The triplet state $^3P$ ($S = 1$, multiplicity 3) has lower energy than the singlets $^1D$ and $^1S$ ($S = 0$, multiplicity 1).</li>
<li><strong>Hund's Rule 2:</strong> There is only one triplet term ($^3P$), so $L = 1$ is fixed.</li>
<li><strong>Hund's Rule 3 (Subshell Less than Half Full):</strong> A $p^2$ subshell has 2 electrons out of 6 possible, so it is less than half full. Therefore, the level with the <strong>minimum $J$ value</strong> has the lowest energy:
<div class="math-display">
$$J = |L - S| = |1 - 1| = 0$$
</div>
</li>
</ol>
<p>Thus, the ground state term symbol of Carbon is <strong>$^3P_0$</strong>.</p>"""
        }
    ]
}

unit6 = {
    "id": "unit-6",
    "number": 6,
    "title": "Molecular Physics, Chemical Bonding & Molecular Spectroscopy",
    "description": "Comprehensive theory of molecular structure and spectroscopy: nature of chemical bonds (ionic, covalent, van der Waals); quantum theory of H2+ and H2 via the LCAO molecular orbital method; Born-Oppenheimer separation of electronic, vibrational, and rotational motions; pure rotational spectroscopy of rigid rotors and bond length determinations; vibrational spectroscopy, Morse potential anharmonicity, and vibration-rotation P/R branches; electronic spectra, Franck-Condon principle, and classical/quantum Raman scattering.",
    "sections": [
        {
            "id": "u6-sec1",
            "title": "Molecular Chemical Bonds & The Molecular Orbital Concept",
            "content": """<h4>1. Classification of Molecular Chemical Bonds</h4>
<p>Molecules are stable aggregates of two or more atoms bound together by electromagnetic interactions. Chemical bonds are categorized by their physical bonding mechanisms:
<ul>
<li><strong>Ionic Bonds:</strong> Formed by complete electrostatic electron transfer between atoms of widely differing electronegativities (e.g., $\text{NaCl}, \text{KBr}$). The cohesive energy is governed by Coulomb attraction balanced by Pauli short-range electron core repulsion:
<div class="math-display">
$$U(R) = - \\frac{e^2}{4\\pi\\varepsilon_0 R} + \\frac{A}{R^n} \\quad (n \\approx 8\\text{ to }10)$$
</div></li>
<li><strong>Covalent Bonds:</strong> Formed between atoms of similar electronegativities by the quantum mechanical sharing of valence electrons (e.g., $\text{H}_2, \text{O}_2, \text{CH}_4$). The shared electron density accumulates in the internuclear region, electrostatically screening the positive nuclei from mutual repulsion and lowering total quantum energy.</li>
<li><strong>Van der Waals Bonds:</strong> Weak intermolecular bonds ($0.01\\text{ to }0.1\\,\\text{eV}$) arising from fluctuating dipole-induced dipole electrostatic attractions ($U(R) \\propto -1/R^6$).</li>
<li><strong>Hydrogen Bonds:</strong> Intermediate dipole-dipole attractions ($0.1\\text{ to }0.5\\,\\text{eV}$) formed between an electropositive hydrogen atom covalently bound to an electronegative atom (N, O, F) and an adjacent lone pair.</li>
</ul>
</p>

<h4>2. The Molecular Orbital Concept & LCAO Approximation</h4>
<p>In molecular orbital theory, electrons are not confined to individual atoms, but occupy delocalized <strong>Molecular Orbitals (MOs)</strong> extending across the entire molecule.</p>
<p>The simplest mathematical approximation is the <strong>Linear Combination of Atomic Orbitals (LCAO)</strong>. For a diatomic molecule with nuclei $A$ and $B$, a molecular orbital $\psi_{MO}$ is constructed from atomic orbitals $\phi_A$ and $\phi_B$:</p>
<div class="math-display">
$$\\psi_{MO} = c_A \\phi_A + c_B \\phi_B$$
</div>
<p>For homonuclear diatomics ($c_A = \\pm c_B$), this produces two distinct spatial distributions:
<ol>
<li><strong>Bonding Molecular Orbital ($\\sigma_g$):</strong> Symmetric linear combination $\\psi_+ = N_+ (\\phi_A + \\phi_B)$. Electron density builds up constructively between the nuclei, lowering the electrostatic potential energy and forming a stable chemical bond.</li>
<li><strong>Antibonding Molecular Orbital ($\\sigma_u^*$):</strong> Antisymmetric linear combination $\\psi_- = N_- (\\phi_A - \\phi_B)$. A nodal plane where $\\psi = 0$ exists midway between the nuclei. Electron density is pushed away from the internuclear region, producing net nuclear repulsion.</li>
</ol>
</p>"""
        },
        {
            "id": "u6-sec2",
            "title": "Quantum Mechanics of the H2+ Ion & The Hydrogen Molecule (H2)",
            "content": """<h4>1. The Hydrogen Molecular Ion ($H_2^+$)</h4>
<p>The simplest molecular system in nature is the hydrogen molecular ion $H_2^+$, consisting of two positive protons ($A$ and $B$) separated by internuclear distance $R$, and a single electron.</p>
<p>The electronic Hamiltonian in atomic units ($\hbar = m_e = e = 1$) is:</p>
<div class="math-display">
$$\\hat{H} = -\\frac{1}{2} \\nabla^2 - \\frac{1}{r_A} - \\frac{1}{r_B} + \\frac{1}{R}$$
</div>
<p>Using the LCAO trial functions formed from hydrogen $1s$ orbitals $\phi_A$ and $\phi_B$:</p>
<div class="math-display">
$$\\psi_{\\pm}(\\vec{r}) = \\frac{1}{\\sqrt{2(1 \\pm S)}} [ \\phi_A(\\vec{r}) \\pm \\phi_B(\\vec{r}) ]$$
</div>
<p>where the <strong>Overlap Integral $S$</strong> is:</p>
<div class="math-display">
$$S(R) = \\int \\phi_A^* \\phi_B\\, d^3r = e^{-R/a_0} \\left( 1 + \\frac{R}{a_0} + \\frac{R^2}{3 a_0^2} \\right)$$
</div>
<p>The electronic expectation energy $E_{\\pm}(R) = \\langle \\psi_{\\pm} | \\hat{H} | \\psi_{\\pm} \\rangle$ evaluates to:</p>
<div class="math-display">
$$E_{\\pm}(R) = E_{1s} + \\frac{1}{R} + \\frac{J \\pm K}{1 \\pm S}$$
</div>
<p>where $J$ is the <strong>Coulomb Integral</strong> (classical electrostatic interaction between the charge cloud around nucleus $A$ and nucleus $B$) and $K$ is the <strong>Exchange (Resonance) Integral</strong> (representing quantum electron tunneling between the two protons):</p>
<div class="math-display">
$$J = \\int |\\phi_A|^2 \\left(-\\frac{1}{r_B}\\right) d^3r, \\quad K = \\int \\phi_A^* \\phi_B \\left(-\\frac{1}{r_B}\\right) d^3r$$
</div>
<p>Because $K$ is negative, the symmetric state $E_+(R)$ develops a pronounced potential energy minimum at equilibrium bond length $R_e = 1.06\,\text{\AA}$ with a binding dissociation energy $D_e = 2.79\,\text{eV}$.</p>

<h4>2. The Neutral Hydrogen Molecule ($H_2$) & Heitler-London Theory</h4>
<p>In the neutral hydrogen molecule ($H_2$), there are two electrons. By the Pauli exclusion principle, the total two-electron wavefunction must be antisymmetric under exchange of electrons $1$ and $2$:</p>
<div class="math-display">
$$\\Psi_{total}(1, 2) = \\psi_{space}(\\vec{r}_1, \\vec{r}_2) \\chi_{spin}(1, 2)$$
</div>
<ul>
<li><strong>Singlet Ground State ($S = 0$, Antiparallel Spins):</strong> The spin state is antisymmetric $\\chi_{singlet} = \\frac{1}{\\sqrt{2}}(\\alpha_1 \\beta_2 - \\beta_1 \\alpha_2)$. Consequently, the spatial wavefunction must be symmetric:
<div class="math-display">
$$\\psi_S(\\vec{r}_1, \\vec{r}_2) = \\frac{1}{\\sqrt{2(1 + S^2)}} [ \\phi_A(1) \\phi_B(2) + \\phi_B(1) \\phi_A(2) ]$$
</div>
This generates a deep potential well with equilibrium bond length $R_e = 0.74\,\text{\AA}$ and strong covalent dissociation energy $D_e = 4.75\,\text{eV}$.</li>
<li><strong>Triplet Excited State ($S = 1$, Parallel Spins):</strong> The spin state is symmetric, requiring an antisymmetric spatial function $\\psi_T \\propto [\\phi_A(1)\\phi_B(2) - \\phi_B(1)\\phi_A(2)]$. Spatial electron density vanishes between the nuclei, producing purely repulsive forces for all $R$.</li>
</ul>"""
        },
        {
            "id": "u6-sec3",
            "title": "Born-Oppenheimer Approximation & Molecular Energy Hierarchy",
            "content": """<h4>1. The Born-Oppenheimer Approximation (1927)</h4>
<p>Max Born and J. Robert Oppenheimer recognized that atomic nuclei are vastly more massive than electrons ($M_{nucleus} / m_e \\sim 1836\\text{ to }10^5$). Consequently, electrons move at velocities hundreds of times faster than nuclei.</p>
<p>On the timescale of electronic orbital motion, the heavy nuclei can be treated as essentially stationary fixed points in space. The full molecular Hamiltonian separates into:
<ol>
<li>An <strong>Electronic Schrödinger Equation</strong> solved at fixed nuclear configurations $R$, generating potential energy curves $V_{el}(R)$.</li>
<li>A <strong>Nuclear Schrödinger Equation</strong> governing the vibrational and rotational motions of the nuclei moving on the effective potential energy surface $V_{el}(R)$.</li>
</ol>
</p>

<h4>2. Molecular Energy Hierarchy</h4>
<p>To excellent approximation, the total internal energy of a molecule is the sum of three independent contributions:</p>
<div class="math-display">
$$E_{total} = E_{electronic} + E_{vibrational} + E_{rotational}$$
</div>
<table class="data-table" style="width:100%; border-collapse:collapse; margin:16px 0;">
<thead>
<tr style="background:rgba(255,255,255,0.05); text-align:left;">
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Motion Type</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Energy Order of Magnitude</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Spectral Region</th>
<th style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Typical Wavelength $\lambda$</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Electronic Transitions</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$1\\text{ to }10\\,\\text{eV}$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Visible / Ultraviolet</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$100\\text{ to }700\\,\\text{nm}$</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Vibrational Transitions</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$0.05\\text{ to }0.5\\,\\text{eV}$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Infrared (IR)</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$2\\text{ to }20\\,\\mu\\text{m}$</td>
</tr>
<tr>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);"><strong>Rotational Transitions</strong></td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$10^{-4}\\text{ to }10^{-2}\\,\\text{eV}$</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">Microwave / Far-IR</td>
<td style="padding:8px; border:1px solid rgba(255,255,255,0.1);">$0.1\\text{ to }10\\,\\text{mm}$</td>
</tr>
</tbody>
</table>
<p>Because $\Delta E_{rot} \ll \Delta E_{vib} \ll \Delta E_{el}$, molecular spectra exhibit fine structure: electronic bands contain closely spaced vibrational progressions, which in turn contain ultra-dense rotational lines.</p>"""
        },
        {
            "id": "u6-sec4",
            "title": "Pure Rotational Spectroscopy: Rigid Rotor Model & Bond Length Determinations",
            "simulation": "molecular-rigid-rotor-sim",
            "content": """<h4>1. The Rigid Rotor Model of a Diatomic Molecule</h4>
<p>Consider a diatomic molecule consisting of two masses $m_1$ and $m_2$ separated by a fixed equilibrium bond length $r_0$. The classical moment of inertia about the center of mass axis is:</p>
<div class="math-display">
$$I = m_1 r_1^2 + m_2 r_2^2 = \\mu r_0^2, \\quad \\mu = \\frac{m_1 m_2}{m_1 + m_2}$$
</div>
<p>The classical kinetic energy of rotation is $E = \\frac{L^2}{2 I}$. In quantum mechanics, orbital angular momentum is quantized: $L^2 = J(J+1) \\hbar^2$, where $J = 0, 1, 2, 3, \\dots$ is the <strong>Rotational Quantum Number</strong>.</p>
<p>The quantized rotational energy levels are:</p>
<div class="math-display">
$$E_J = \\frac{\\hbar^2}{2 I} J(J+1) = B J(J+1) h c$$
</div>
<p>where the <strong>Rotational Constant $B$</strong> (expressed in wavenumber units $\text{cm}^{-1}$) is:</p>
<div class="math-display">
$$B = \\frac{\\hbar}{4\\pi I c} = \\frac{h}{8\\pi^2 I c}$$
</div>

<h4>2. Selection Rules & Rotational Spectra</h4>
<p>For an electric dipole transition to occur in pure rotational spectroscopy:
<ol>
<li><strong>Gross Selection Rule:</strong> The molecule must possess a <strong>permanent electric dipole moment</strong> ($\mu_{el} \neq 0$). Homonuclear molecules ($\text{H}_2, \text{N}_2, \text{O}_2$) have zero dipole moment and are completely <em>microwave inactive</em>. Heteronuclear molecules ($\text{CO}, \text{HCl}, \text{NO}$) have permanent dipoles and exhibit intense rotational absorption.</li>
<li><strong>Specific Selection Rule:</strong>
<div class="math-display">
$$\\Delta J = \\pm 1 \\quad (+1 \\text{ for absorption, } -1 \\text{ for emission})$$
</div></li>
</ol>
</p>
<p>The wavenumber of the transition from level $J$ to $J + 1$ is:</p>
<div class="math-display">
$$\\bar{\\nu}_{J \\to J+1} = \\frac{E_{J+1} - E_J}{h c} = B [ (J+1)(J+2) - J(J+1) ] = 2 B (J + 1)$$
</div>
<p>Evaluating for consecutive transitions:
<ul>
<li>$J = 0 \\to 1$: $\\bar{\\nu} = 2B$</li>
<li>$J = 1 \\to 2$: $\\bar{\\nu} = 4B$</li>
<li>$J = 2 \\to 3$: $\\bar{\\nu} = 6B$</li>
<li>$J = 3 \\to 4$: $\\bar{\\nu} = 8B$</li>
</ul>
</p>
<p><strong>Fundamental Experimental Signature:</strong> The pure rotational absorption spectrum consists of a series of <strong>equidistant spectral lines separated by constant spacing $2B$</strong>:</p>
<div class="math-display">
$$\\Delta \\bar{\\nu} = \\bar{\\nu}_{J+1} - \\bar{\\nu}_J = 2 B$$
</div>
<p>By measuring this line separation $\Delta \bar{\nu} = 2B$ in the microwave laboratory, one calculates the moment of inertia $I = \frac{h}{8\pi^2 c B}$ and determines the internuclear bond distance $r_0 = \\sqrt{I / \\mu}$ to four decimal places of precision!</p>"""
        },
        {
            "id": "u6-sec5",
            "title": "Vibrational & Vibration-Rotation Spectra: P-Branch & R-Branch Transitions",
            "content": """<h4>1. Harmonic vs. Anharmonic Morse Potential</h4>
<p>Near equilibrium separation $r_0$, the molecular potential energy can be approximated as a simple harmonic oscillator with bond force constant $k$:</p>
<div class="math-display">
$$V(r) \\approx \\frac{1}{2} k (r - r_0)^2$$
</div>
<p>The quantized vibrational energy levels are:</p>
<div class="math-display">
$$E_v = \\left( v + \\frac{1}{2} \\right) \\hbar \\omega_0 = \\left( v + \\frac{1}{2} \\right) h c \\bar{\\nu}_0 \\quad (v = 0, 1, 2, \\dots)$$
</div>
<p>where $\\bar{\\nu}_0 = \\frac{1}{2\\pi c} \\sqrt{\\frac{k}{\\mu}}$. Even in the ground state ($v = 0$), the molecule possesses irreducible <strong>zero-point vibrational energy</strong> $E_0 = \\frac{1}{2} \\hbar \\omega_0$.</p>
<p>Real chemical bonds dissociate at large separations. A far more realistic model is the <strong>Morse Potential</strong>:</p>
<div class="math-display">
$$V(r) = D_e \\left[ 1 - e^{-a(r - r_0)} \\right]^2$$
</div>
<p>where $D_e$ is the depth of the potential well. The energy levels of an anharmonic Morse oscillator are:</p>
<div class="math-display">
$$E_v = h c \\bar{\\nu}_0 \\left( v + \\frac{1}{2} \\right) - h c \\bar{\\nu}_0 x_e \\left( v + \\frac{1}{2} \\right)^2$$
</div>
<p>where $x_e$ is the <strong>anharmonicity constant</strong>. Anharmonicity relaxes the strict harmonic selection rule $\Delta v = \pm 1$, permitting weaker <strong>overtone transitions</strong> ($\Delta v = \pm 2, \pm 3$).</p>

<h4>2. Vibration-Rotation Spectra & P/R Branch Architecture</h4>
<p>Because rotational energy levels are densely packed within each vibrational state, a vibrational transition ($v = 0 \\to 1$) is always accompanied by simultaneous rotational transitions ($J \\to J'$). The combined energy of a vibration-rotation state is:</p>
<div class="math-display">
$$T(v, J) = \\bar{\\nu}_0 \\left( v + \\frac{1}{2} \\right) + B J(J+1)$$
</div>
<p>For heteronuclear diatomic molecules with zero electronic angular momentum ($\Sigma$ states), the selection rules are:
<div class="math-display">
$$\\Delta v = +1, \\quad \\Delta J = \\pm 1$$
</div>
Notice that <strong>$\Delta J = 0$ is strictly forbidden</strong> in diatomic $\Sigma$ molecules!</p>
<p>The resulting spectrum splits into two distinct symmetric branches flanking the missing fundamental vibrational frequency $\bar{\nu}_0$:
<ol>
<li><strong>The $R$-Branch ($\Delta J = +1$, $J' = J + 1$):</strong> Rotational energy increases during vibrational absorption:
<div class="math-display">
$$\\bar{\\nu}_R(J) = \\bar{\\nu}_0 + B(J+1)(J+2) - B J(J+1) = \\bar{\\nu}_0 + 2 B (J + 1) \\quad (J = 0, 1, 2, \\dots)$$
</div>
Lines appear at higher frequencies: $\\bar{\\nu}_0 + 2B, \\bar{\\nu}_0 + 4B, \\bar{\\nu}_0 + 6B, \\dots$</li>
<li><strong>The $P$-Branch ($\Delta J = -1$, $J' = J - 1$):</strong> Rotational energy decreases:
<div class="math-display">
$$\\bar{\\nu}_P(J) = \\bar{\\nu}_0 + B(J-1)J - B J(J+1) = \\bar{\\nu}_0 - 2 B J \\quad (J = 1, 2, 3, \\dots)$$
</div>
Lines appear at lower frequencies: $\\bar{\\nu}_0 - 2B, \\bar{\\nu}_0 - 4B, \\bar{\\nu}_0 - 6B, \\dots$</li>
<li><strong>The Missing $Q$-Branch ($\Delta J = 0$):</strong> A line at $\bar{\nu} = \bar{\nu}_0$ would correspond to $\Delta J = 0$. Because $\Delta J = 0$ is forbidden, there is a distinct <strong>central gap of width $4B$</strong> at the fundamental origin!</li>
</ol>
</p>"""
        },
        {
            "id": "u6-sec6",
            "title": "Electronic Spectra, The Franck-Condon Principle & The Raman Effect",
            "simulation": "raman-spectroscopy-sim",
            "content": """<h4>1. Electronic Transitions & The Franck-Condon Principle</h4>
<p>Electronic transitions involve major rearrangements of electron clouds, shifting the equilibrium internuclear distance from $r_0$ to $r_0'$.</p>
<p>The <strong>Franck-Condon Principle</strong> states: <em>Because atomic nuclei are vastly heavier than electrons, an electronic transition occurs so rapidly ($\sim 10^{-15}\text{ s}$) that the nuclei do not have time to change their positions or momenta during the transition.</em></p>
<p>On a potential energy diagram, electronic transitions are represented as strictly <strong>vertical lines</strong>. The transition probability (intensity) between vibrational state $v$ in the ground electronic state and $v'$ in the excited state is proportional to the <strong>Franck-Condon Factor</strong>—the square of the vibrational overlap integral:</p>
<div class="math-display">
$$I_{v \\to v'} \\propto |\\langle \\psi_{v'} | \\psi_v \\rangle|^2$$
</div>

<h4>2. The Raman Effect: Classical Polarizability Model (1928)</h4>
<p>Sir C.V. Raman discovered that when a transparent substance is irradiated with intense monochromatic light of frequency $\nu_0$, a small fraction ($\sim 10^{-6}$) of the scattered radiation emerges with altered frequencies ($\nu_0 \pm \nu_v$).</p>
<p>Classically, the incident electric field $\vec{E}(t) = \vec{E}_0 \cos(2\pi \nu_0 t)$ induces an electric dipole moment in the molecule:</p>
<div class="math-display">
$$\\vec{P}(t) = \\alpha \\vec{E}(t)$$
</div>
<p>where $\alpha$ is the molecular <strong>polarizability</strong>. As the molecule vibrates with natural frequency $\nu_v$, its polarizability fluctuates periodically:</p>
<div class="math-display">
$$\\alpha(t) = \\alpha_0 + \\left( \\frac{\\partial \\alpha}{\\partial q} \\right)_0 q_0 \\cos(2\\pi \\nu_v t)$$
</div>
<p>Substituting $\alpha(t)$ into the induced dipole equation:</p>
<div class="math-display">
$$\\vec{P}(t) = \\alpha_0 \\vec{E}_0 \\cos(2\\pi \\nu_0 t) + \\frac{1}{2} \\left( \\frac{\\partial \\alpha}{\\partial q} \\right)_0 q_0 \\vec{E}_0 [ \\cos(2\\pi(\\nu_0 - \\nu_v)t) + \\cos(2\\pi(\\nu_0 + \\nu_v)t) ]$$
</div>
<p>The oscillating dipole radiates electromagnetic waves at three distinct frequencies:
<ol>
<li><strong>Rayleigh Scattering ($\\nu_0$):</strong> Elastic scattering at the unshifted incident frequency.</li>
<li><strong>Stokes Lines ($\\nu_0 - \\nu_v$):</strong> Inelastic scattering red-shifted to lower frequency. The incident photon transfers energy to excite a molecular vibration.</li>
<li><strong>Anti-Stokes Lines ($\\nu_0 + \\nu_v$):</strong> Inelastic scattering blue-shifted to higher frequency. The incident photon absorbs energy from an already-vibrating molecule.</li>
</ol>
</p>

<h4>3. Quantum Interpretation & The Rule of Mutual Exclusion</h4>
<p>In quantum theory, an incident photon of energy $h\nu_0$ promotes the molecule to a transient <strong>virtual state</strong>:
<ul>
<li>If it de-excites to a higher vibrational level ($v = 0 \\to 1$), the scattered photon carries reduced energy $h(\\nu_0 - \\nu_v)$ (<strong>Stokes</strong>).</li>
<li>If it de-excites from an initial excited level to the ground level ($v = 1 \\to 0$), the scattered photon carries increased energy $h(\\nu_0 + \\nu_v)$ (<strong>Anti-Stokes</strong>).</li>
</ul>
</p>
<p>Because the thermal population of the excited state $v = 1$ is governed by the Boltzmann distribution $N_1 / N_0 = e^{-h\nu_v / k_B T} \ll 1$, <strong>Stokes lines are always vastly more intense than Anti-Stokes lines</strong>:</p>
<div class="math-display">
$$\\frac{I_{\\text{Anti-Stokes}}}{I_{\\text{Stokes}}} = \\left( \\frac{\\nu_0 + \\nu_v}{\\nu_0 - \\nu_v} \\right)^4 e^{-h\\nu_v / k_B T}$$
</div>
<p><strong>The Rule of Mutual Exclusion:</strong> For molecules with a center of inversion symmetry (such as $\text{CO}_2, \text{C}_2\text{H}_4, \text{N}_2$), vibrations that are Infrared active (change in dipole moment, $\partial\mu/\partial q \neq 0$) are <strong>Raman inactive</strong>, and vibrations that are Raman active (change in polarizability, $\partial\alpha/\partial q \neq 0$) are <strong>Infrared inactive</strong>.</p>"""
        }
    ],
    "problems": [
        {
            "id": "u6-prob1",
            "title": "Rotational Constant & Bond Length Determination of Carbon Monoxide",
            "statement": "The pure rotational absorption spectrum of ^{12}\\text{C}^{16}\\text{O} exhibits a series of equidistant absorption lines in the microwave region with an adjacent line separation of \\Delta \\bar{\\nu} = 3.84235\\,\\text{cm}^{-1}$. Given atomic masses m(^{12}\\text{C}) = 1.99265 \\times 10^{-26}\\,\\text{kg}$ and m(^{16}\\text{O}) = 2.65600 \\times 10^{-26}\\,\\text{kg}$: (a) Calculate the rotational constant B of ^{12}\\text{C}^{16}\\text{O} in cm^{-1} and in Joules. (b) Calculate the moment of inertia I of the molecule. (c) Determine the equilibrium internuclear bond length r_0 in angstroms. (d) What is the wavenumber and frequency of the J = 4 \\to J = 5 transition?",
            "solution": """<p><strong>Step 1: Calculate Rotational Constant $B$</strong></p>
<p>For a rigid rotor, adjacent spectral line separation is $\Delta \bar{\nu} = 2B$:</p>
<div class="math-display">
$$B = \\frac{\\Delta \\bar{\\nu}}{2} = \\frac{3.84235\\,\\text{cm}^{-1}}{2} = 1.921175\\,\\text{cm}^{-1} = 192.1175\\,\\text{m}^{-1}$$
</div>
<p>In energy units:</p>
<div class="math-display">
$$E_B = B h c = (192.1175\\,\\text{m}^{-1})(6.62607 \\times 10^{-34}\\,\\text{J}\\cdot\\text{s})(2.99792 \\times 10^8\\,\\text{m/s}) \\approx 3.8163 \\times 10^{-23}\\,\\text{J}$$
</div>

<p><strong>Step 2: Calculate Moment of Inertia $I$</strong></p>
<div class="math-display">
$$I = \\frac{\\hbar}{4\\pi c B} = \\frac{h}{8\\pi^2 c B} = \\frac{6.62607 \\times 10^{-34}}{8\\pi^2 (2.99792 \\times 10^8\\,\\text{m/s})(192.1175\\,\\text{m}^{-1})} \\approx 1.45695 \\times 10^{-46}\\,\\text{kg}\\cdot\\text{m}^2$$
</div>

<p><strong>Step 3: Calculate Reduced Mass $\\mu$ and Bond Length $r_0$</strong></p>
<div class="math-display">
$$\\mu = \\frac{m_C m_O}{m_C + m_O} = \\frac{(1.99265 \\times 10^{-26})(2.65600 \\times 10^{-26})}{1.99265 \\times 10^{-26} + 2.65600 \\times 10^{-26}} = \\frac{5.29248 \\times 10^{-52}}{4.64865 \\times 10^{-26}} \\approx 1.138499 \\times 10^{-26}\\,\\text{kg}$$
</div>
<p>Using $I = \mu r_0^2$:</p>
<div class="math-display">
$$r_0 = \\sqrt{\\frac{I}{\\mu}} = \\sqrt{\\frac{1.45695 \\times 10^{-46}\\,\\text{kg}\\cdot\\text{m}^2}{1.138499 \\times 10^{-26}\\,\\text{kg}}} = \\sqrt{1.27971 \\times 10^{-20}\\,\\text{m}^2} \\approx 1.13124 \\times 10^{-10}\\,\\text{m} = 1.1312\\,\\text{\\AA}$$
</div>
<p>The $\text{C-O}$ triple bond length is determined to five significant figures: $r_0 = 1.1312\,\text{\AA}$.</p>

<p><strong>Step 4: Transition $J = 4 \\to 5$</strong></p>
<div class="math-display">
$$\\bar{\\nu} = 2 B (J + 1) = 2 (1.921175\\,\\text{cm}^{-1})(5) = 10 \\times 1.921175 = 19.21175\\,\\text{cm}^{-1}$$
</div>
<div class="math-display">
$$\\nu = c \\bar{\\nu} = (2.99792 \\times 10^{10}\\,\\text{cm/s}) \\times 19.21175\\,\\text{cm}^{-1} \\approx 5.7595 \\times 10^{11}\\,\\text{Hz} = 575.95\\,\\text{GHz}$$
</div>"""
        },
        {
            "id": "u6-prob2",
            "title": "Vibration-Rotation Band Analysis & Force Constant of HCl",
            "statement": "The fundamental infrared absorption band of hydrogen chloride (\\text{H}^{35}\\text{Cl}) has its band origin (missing Q-branch center) at \\bar{\\nu}_0 = 2886.0\\,\\text{cm}^{-1}$. The rotational constant of \\text{H}^{35}\\text{Cl} is B = 10.59\\,\\text{cm}^{-1}$. Given atomic masses m(^{1}\\text{H}) = 1.67356 \\times 10^{-27}\\,\\text{kg}$ and m(^{35}\\text{Cl}) = 5.8068 \\times 10^{-26}\\,\\text{kg}$: (a) Calculate the reduced mass \\mu of the molecule. (b) Determine the chemical bond force constant k in N/m. (c) Calculate the wavenumbers of the first two lines of the P-branch (P(1), P(2)) and the first two lines of the R-branch (R(0), R(1)). (d) What is the wavenumber separation across the central gap?",
            "solution": """<p><strong>Step 1: Calculate Reduced Mass $\\mu$</strong></p>
<div class="math-display">
$$\\mu = \\frac{m_H m_{Cl}}{m_H + m_{Cl}} = \\frac{(1.67356 \\times 10^{-27})(5.8068 \\times 10^{-26})}{1.67356 \\times 10^{-27} + 5.8068 \\times 10^{-26}} = \\frac{9.71803 \\times 10^{-53}}{5.97416 \\times 10^{-26}} \\approx 1.62668 \\times 10^{-27}\\,\\text{kg}$$
</div>

<p><strong>Step 2: Calculate Bond Force Constant $k$</strong></p>
<p>From $\bar{\nu}_0 = \frac{1}{2\pi c} \sqrt{\frac{k}{\mu}} \implies \omega_0 = 2\pi c \bar{\nu}_0$:</p>
<div class="math-display">
$$\\omega_0 = 2\\pi (2.99792 \\times 10^{10}\\,\\text{cm/s}) \\times 2886.0\\,\\text{cm}^{-1} \\approx 5.4371 \\times 10^{14}\\,\\text{rad/s}$$
</div>
<div class="math-display">
$$k = \\mu \\omega_0^2 = (1.62668 \\times 10^{-27}\\,\\text{kg}) \\times (5.4371 \\times 10^{14}\\,\\text{s}^{-1})^2 = (1.62668 \\times 10^{-27})(2.9562 \\times 10^{29}) \\approx 480.9\\,\\text{N/m}$$
</div>
<p>The $\text{H-Cl}$ single bond has a force constant of $k \approx 481\,\text{N/m}$.</p>

<p><strong>Step 3: Calculate Wavenumbers of $P$ and $R$ Branches</strong></p>
<p>Formulas: $\bar{\nu}_R(J) = \bar{\nu}_0 + 2B(J+1)$ and $\bar{\nu}_P(J) = \bar{\nu}_0 - 2BJ$, with $2B = 2(10.59) = 21.18\,\text{cm}^{-1}$:</p>
<ul>
<li><strong>$R(0)$ ($J = 0 \to 1$):</strong> $\bar{\nu} = 2886.0 + 21.18 = 2907.18\,\text{cm}^{-1}$</li>
<li><strong>$R(1)$ ($J = 1 \to 2$):</strong> $\bar{\nu} = 2886.0 + 2(21.18) = 2928.36\,\text{cm}^{-1}$</li>
<li><strong>$P(1)$ ($J = 1 \to 0$):</strong> $\bar{\nu} = 2886.0 - 21.18 = 2864.82\,\text{cm}^{-1}$</li>
<li><strong>$P(2)$ ($J = 2 \to 1$):</strong> $\bar{\nu} = 2886.0 - 2(21.18) = 2843.64\,\text{cm}^{-1}$</li>
</ul>

<p><strong>Step 4: Central Gap Separation</strong></p>
<div class="math-display">
$$\\Delta \\bar{\\nu}_{gap} = R(0) - P(1) = 2907.18 - 2864.82 = 42.36\\,\\text{cm}^{-1} = 4 B$$
</div>
<p>The missing central $Q$-branch leaves a double-spacing gap of $4B = 42.36\,\text{cm}^{-1}$.</p>"""
        },
        {
            "id": "u6-prob3",
            "title": "Raman Scattering Stokes & Anti-Stokes Intensity Ratio of Nitrogen",
            "statement": "A gas of nitrogen molecules (\\text{N}_2) is irradiated with a green Nd:YAG laser beam of wavelength \\lambda_0 = 532.0\\,\\text{nm}. The fundamental vibrational Raman frequency of \\text{N}_2 is \\Delta \\bar{\\nu}_v = 2331.0\\,\\text{cm}^{-1}$. (a) Calculate the wavenumber of the incident laser light \\bar{\\nu}_0. (b) Calculate the wavenumbers and wavelengths of the Raman Stokes line and Anti-Stokes line. (c) Calculate the theoretical intensity ratio I_{Anti-Stokes} / I_{Stokes} at room temperature T = 300\\,\\text{K}. (d) To what temperature must the gas be heated for the intensity ratio to reach 10%?",
            "solution": """<p><strong>Step 1: Calculate Incident Laser Wavenumber $\\bar{\\nu}_0$</strong></p>
<div class="math-display">
$$\\bar{\\nu}_0 = \\frac{1}{\\lambda_0} = \\frac{1}{532.0 \\times 10^{-7}\\,\\text{cm}} \\approx 18,796.99\\,\\text{cm}^{-1}$$
</div>

<p><strong>Step 2: Calculate Stokes and Anti-Stokes Lines</strong></p>
<p>Stokes Line (Red-Shifted):</p>
<div class="math-display">
$$\\bar{\\nu}_S = \\bar{\\nu}_0 - \\Delta \\bar{\\nu}_v = 18,796.99 - 2331.00 = 16,465.99\\,\\text{cm}^{-1}$$
</div>
<div class="math-display">
$$\\lambda_S = \\frac{1}{\\bar{\\nu}_S} = \\frac{1}{16,465.99\\,\\text{cm}^{-1}} \\approx 6.073 \\times 10^{-5}\\,\\text{cm} = 607.3\\,\\text{nm} \\text{ (Orange)}$$
</div>
<p>Anti-Stokes Line (Blue-Shifted):</p>
<div class="math-display">
$$\\bar{\\nu}_{AS} = \\bar{\\nu}_0 + \\Delta \\bar{\\nu}_v = 18,796.99 + 2331.00 = 21,127.99\\,\\text{cm}^{-1}$$
</div>
<div class="math-display">
$$\\lambda_{AS} = \\frac{1}{\\bar{\\nu}_{AS}} = \\frac{1}{21,127.99\\,\\text{cm}^{-1}} \\approx 4.733 \\times 10^{-5}\\,\\text{cm} = 473.3\\,\\text{nm} \\text{ (Blue)}$$
</div>

<p><strong>Step 3: Intensity Ratio at $T = 300\\,\\text{K}$</strong></p>
<p>The intensity ratio is governed by dipole radiation $\nu^4$ law and the Boltzmann factor:</p>
<div class="math-display">
$$\\frac{I_{AS}}{I_S} = \\left( \\frac{\\bar{\\nu}_{AS}}{\\bar{\\nu}_S} \\right)^4 e^{-h c \\Delta \\bar{\\nu}_v / k_B T}$$
</div>
<div class="math-display">
$$\\frac{\\bar{\\nu}_{AS}}{\\bar{\\nu}_S} = \\frac{21,127.99}{16,465.99} \\approx 1.28312 \\implies (1.28312)^4 \\approx 2.7107$$
</div>
<div class="math-display">
$$\\frac{h c \\Delta \\bar{\\nu}_v}{k_B T} = \\frac{(6.626 \\times 10^{-34})(2.998 \\times 10^{10})(2331.0)}{(1.381 \\times 10^{-23})(300)} = \\frac{4.630 \\times 10^{-20}}{4.143 \\times 10^{-21}} \\approx 11.1755$$
</div>
<div class="math-display">
$$e^{-11.1755} \\approx 1.3978 \\times 10^{-5}$$
</div>
<div class="math-display">
$$\\frac{I_{AS}}{I_S} = 2.7107 \\times 1.3978 \\times 10^{-5} \\approx 3.79 \\times 10^{-5} = 0.00379\\%$$
</div>
<p>At room temperature, the Anti-Stokes line is more than 26,000 times weaker than the Stokes line because virtually all nitrogen molecules reside in the ground vibrational state ($v = 0$).</p>

<p><strong>Step 4: Temperature for 10% Intensity Ratio ($I_{AS}/I_S = 0.10$)</strong></p>
<div class="math-display">
$$0.10 = 2.7107 \\times e^{-h c \\Delta \\bar{\\nu}_v / k_B T} \\implies e^{-h c \\Delta \\bar{\\nu}_v / k_B T} = \\frac{0.10}{2.7107} \\approx 0.03689$$
</div>
<div class="math-display">
$$\\frac{h c \\Delta \\bar{\\nu}_v}{k_B T} = -\\ln(0.03689) \\approx 3.300$$
</div>
<div class="math-display">
$$T = \\frac{h c \\Delta \\bar{\\nu}_v}{3.300 \\, k_B} = \\frac{4.630 \\times 10^{-20}\\,\\text{J}}{3.300 \\times (1.381 \\times 10^{-23}\\,\\text{J/K})} = \\frac{4.630 \\times 10^{-20}}{4.5573 \\times 10^{-23}} \\approx 1016\\,\\text{K} \\approx 743^\\circ\\text{C}$$
</div>"""
        }
    ]
}

with open("amp_u5.json", "w") as f:
    json.dump(unit5, f, indent=2)

with open("amp_u6.json", "w") as f:
    json.dump(unit6, f, indent=2)

print("amp_u5.json and amp_u6.json generated successfully!")
