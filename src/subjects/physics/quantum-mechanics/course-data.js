// Quantum Mechanics — University Standard Textbook Edition
// Complete chapters with inline topic simulations.

window.COURSE_DATA = {
  "courseCode": "PHYSICS",
  "courseTitle": "Quantum Mechanics",
  "edition": "Interactive Digital Textbook Edition",
  "textbookTitle": "Principles of Quantum Mechanics: Theory, Mathematical Formulation, and Interactive Simulations",
  "author": "OpenSTEM Academic Press",
  "units": [
    {
      "id": "unit-1",
      "number": 1,
      "title": "Physical Basis & Heisenberg Uncertainty Principle",
      "leadSummary": "An exhaustive exposition of the historical breakdown of classical physics at the end of the 19th century, Planck's radiation law, the Einstein photoelectric effect, Compton scattering, the Bohr-Sommerfeld old quantum theory, de Broglie matter waves, and the foundational Heisenberg uncertainty relations.",
      "simulations": [
        "double-slit",
        "uncertainty-principle"
      ],
      "sections": [
        {
          "secNumber": "1.1",
          "heading": "The Crisis of Classical Physics and Empirical Anomalies",
          "content": "\nAt the close of the nineteenth century, Newtonian classical mechanics, combined with Maxwell's unified electrodynamics and Boltzmann-Gibbs statistical thermodynamics, was widely considered the complete and final foundation of the physical sciences. However, when applied to microscopic phenomena on atomic and subatomic scales, the classical framework yielded catastrophic contradictions with experimental reality.\n\n#### 1. Blackbody Radiation and the Ultraviolet Catastrophe\nA blackbody is an idealized physical body that absorbs all incident electromagnetic radiation, regardless of frequency or angle of incidence. In thermodynamic equilibrium at absolute temperature $T$, it emits electromagnetic cavity radiation whose spectral energy density is denoted by $u(\\nu, T) d\\nu$.\n\nUsing classical statistical mechanics, the equipartition theorem assigns an average thermal energy of $\\langle E \\rangle = k_B T$ to each electromagnetic standing wave mode within the cavity. Calculating the number of spatial cavity modes per unit volume in the frequency interval $[\\nu, \\nu + d\\nu]$:\n\n$$g(\\nu) d\\nu = \\frac{8\\pi \\nu^2}{c^3} d\\nu$$\n\nMultiplying $g(\\nu)$ by the classical average energy $\\langle E \\rangle = k_B T$ yields the classical **Rayleigh-Jeans Radiation Formula**:\n\n$$u_{\\text{RJ}}(\\nu, T) d\\nu = \\frac{8\\pi \\nu^2}{c^3} k_B T d\\nu$$\n\nAs the frequency approaches the ultraviolet and beyond ($\\nu \\to \\infty$), $u_{\\text{RJ}}(\\nu, T) \\to \\infty$. Consequently, the integrated total energy density radiated by a cavity at any non-zero temperature diverges:\n\n$$U = \\int_0^\\infty u_{\\text{RJ}}(\\nu, T) d\\nu = \\frac{8\\pi k_B T}{c^3} \\int_0^\\infty \\nu^2 d\\nu = \\infty$$\n\nThis absurd prediction—that an oven or glowing iron bar would radiate infinite energy at high frequencies—is known as the **Ultraviolet Catastrophe**.\n\nIn December 1900, Max Planck resolved this crisis by introducing a revolutionary quantum postulate: the atomic oscillators in the cavity walls cannot absorb or emit energy continuously; rather, energy exchange occurs exclusively in discrete packets, or *quanta*, proportional to the oscillation frequency:\n\n$$E_n = n h \\nu, \\quad n \\in \\{0, 1, 2, 3, \\dots\\}$$\n\nwhere $h = 6.62607015 \\times 10^{-34} \\text{ J}\\cdot\\text{s}$ is Planck's constant.\n\nApplying Maxwell-Boltzmann statistics, the thermal average energy of a quantum oscillator is given by:\n\n$$\\langle E \\rangle = \\frac{\\sum_{n=0}^\\infty n h \\nu e^{-n h \\nu / k_B T}}{\\sum_{n=0}^\\infty e^{-n h \\nu / k_B T}} = \\frac{h\\nu}{e^{h\\nu / k_B T} - 1}$$\n\nSubstituting this quantum average into the density of modes yields **Planck's Radiation Law**:\n\n$$u(\\nu, T) d\\nu = \\frac{8\\pi h \\nu^3}{c^3} \\frac{1}{e^{h\\nu / k_B T} - 1} d\\nu$$\n\nIn the low-frequency limit ($h\\nu \\ll k_B T$), expanding the exponential $e^{h\\nu / k_B T} \\approx 1 + \\frac{h\\nu}{k_B T}$ recovers the Rayleigh-Jeans formula. In the high-frequency limit ($h\\nu \\gg k_B T$), the exponential denominator dominates, cutting off emission and preventing any ultraviolet divergence.\n\n#### 2. The Photoelectric Effect\nIn 1887, Heinrich Hertz discovered that ultraviolet light incident on metallic surfaces ejects electrons. Classical wave theory predicted that:\n1. The kinetic energy of ejected electrons should increase with light *intensity* (the electric field amplitude).\n2. For very low light intensities, there should be a measurable time delay while electrons accumulate sufficient energy to escape the metallic surface.\n\nExperiments conducted by Philipp Lenard (1902) directly refuted both classical predictions:\n1. The maximum kinetic energy $K_{\\text{max}}$ of ejected photoelectrons is strictly independent of light intensity and depends linearly solely on the *frequency* $\\nu$.\n2. Emission occurs quasi-instantaneously (within $10^{-9}$ seconds), even at exceptionally low light intensities.\n3. Below a characteristic threshold frequency $\\nu_0$ (dependent on the specific metal), no electrons are emitted regardless of light intensity.\n\nIn 1905, Albert Einstein extended Planck's concept, proposing that electromagnetic radiation is not merely emitted in quanta, but propagates and interacts as localized particle-like energy packets called **photons**, each with energy:\n\n$$E = h\\nu = \\hbar\\omega$$\n\nwhere $\\hbar = \\frac{h}{2\\pi} = 1.0545718 \\times 10^{-34} \\text{ J}\\cdot\\text{s}$. An incoming photon transfers its entire energy to a single conduction electron. If this energy exceeds the binding work function $\\Phi$ of the metal, the electron escapes with kinetic energy governed by **Einstein's Photoelectric Equation**:\n\n$$K_{\\text{max}} = h\\nu - \\Phi = h(\\nu - \\nu_0)$$\n\n#### 3. Compton Scattering\nIn 1923, Arthur Compton directed monochromatic X-rays of wavelength $\\lambda$ at a graphite target and observed that the scattered radiation contained a shifted wavelength component $\\lambda' > \\lambda$.\n\nTreating the collision between an incident photon (energy $E=h\\nu$, relativistic momentum $p=h/\\lambda$) and a stationary target electron ($m_e$) as an elastic relativistic two-body collision:\n* Conservation of relativistic energy: $h\\nu + m_e c^2 = h\\nu' + \\sqrt{p_e^2 c^2 + m_e^2 c^4}$\n* Conservation of momentum: $\\mathbf{p}_\\gamma = \\mathbf{p}'_\\gamma + \\mathbf{p}_e$\n\nSolving the relativistic conservation laws yields the **Compton Scattering Formula**:\n\n$$\\Delta \\lambda = \\lambda' - \\lambda = \\frac{h}{m_e c} (1 - \\cos\\theta) = \\lambda_C (1 - \\cos\\theta)$$\n\nwhere $\\lambda_C = \\frac{h}{m_e c} \\approx 0.02426 \\text{ Å} = 2.426 \\times 10^{-12} \\text{ m}$ is the Compton wavelength of the electron, and $\\theta$ is the scattering angle. This demonstrated that photons carry localized momentum $\\mathbf{p} = \\hbar \\mathbf{k}$.\n          ",
          "simulation": "blackbody-spectrum-sim"
        },
        {
          "secNumber": "1.2",
          "heading": "The Bohr Atom and the Old Quantum Theory",
          "content": "\n#### Rutherford Nuclear Model Instability\nErnest Rutherford's 1911 alpha-scattering experiments proved that an atom consists of a tiny, massive, positively charged nucleus surrounded by electrons. However, classical electrodynamics states that an orbiting electron experiences continuous centripetal acceleration $a = v^2/r$. According to Larmor's radiation formula, an accelerated charge radiates electromagnetic power:\n\n$$P = \\frac{e^2 a^2}{6\\pi \\epsilon_0 c^3}$$\n\nAs the electron loses mechanical orbital energy, its orbital radius must shrink continuously, causing the electron to spiral into the nucleus within an estimated lifetime of $\\tau \\approx 10^{-11} \\text{ seconds}$. Classical mechanics could not explain why atoms exist as stable structures.\n\n#### Bohr Postulates (1913)\nNiels Bohr resolved atomic instability for the hydrogen atom ($Z=1$) by introducing three non-classical postulates:\n1. **Stationary States:** The electron moves in discrete circular orbits without radiating electromagnetic energy.\n2. **Quantization of Orbital Angular Momentum:** The electron's orbital angular momentum $L = m_e v r$ is restricted to integral multiples of $\\hbar$:\n$$L = m_e v_n r_n = n\\hbar, \\quad n \\in \\{1, 2, 3, \\dots\\}$$\n3. **Bohr Frequency Condition:** Radiation is emitted or absorbed only when an electron undergoes a discrete transition between stationary orbits $E_i$ and $E_f$:\n$$\\Delta E = E_i - E_f = h\\nu = \\hbar\\omega$$\n\n#### Derivation of Quantized Radii and Energy Levels\nBalancing Coulomb attraction with centripetal force:\n\n$$\\frac{m_e v_n^2}{r_n} = \\frac{e^2}{4\\pi \\epsilon_0 r_n^2} \\implies m_e v_n^2 r_n = \\frac{e^2}{4\\pi \\epsilon_0}$$\n\nCombining this with the quantization condition $v_n = \\frac{n\\hbar}{m_e r_n}$:\n\n$$r_n = \\frac{4\\pi \\epsilon_0 \\hbar^2}{m_e e^2} n^2 = n^2 a_0$$\n\nwhere $a_0 = \\frac{4\\pi\\epsilon_0\\hbar^2}{m_e e^2} \\approx 0.529177 \\times 10^{-10} \\text{ m} = 0.529 \\text{ Å}$ is the **Bohr radius**.\n\nThe total mechanical energy $E_n = K_n + U_n = \\frac{1}{2}m_e v_n^2 - \\frac{e^2}{4\\pi\\epsilon_0 r_n} = -\\frac{e^2}{8\\pi\\epsilon_0 r_n}$:\n\n$$E_n = -\\frac{m_e e^4}{32 \\pi^2 \\epsilon_0^2 \\hbar^2} \\frac{1}{n^2} = -\\frac{13.6 \\text{ eV}}{n^2}$$\n\nTransitioning between states $n_2 \\to n_1$ yields the Rydberg formula:\n\n$$\\frac{1}{\\lambda} = R_H \\left( \\frac{1}{n_1^2} - \\frac{1}{n_2^2} \\right), \\quad R_H = \\frac{m_e e^4}{8 \\epsilon_0^2 h^3 c} \\approx 1.09737 \\times 10^7 \\text{ m}^{-1}$$\n\nWhile the Bohr-Sommerfeld model successfully explained the Balmer and Lyman spectral series of hydrogen, it was fundamentally limited: it could not explain the spectra of multi-electron atoms (even Helium), chemical bonding, transition rates, or the Zeeman effect without ad-hoc rules.\n          ",
          "simulations": [
            "photoelectric-effect-sim",
            "bohr-orbit-sim"
          ]
        },
        {
          "secNumber": "1.3",
          "heading": "de Broglie Hypothesis and Matter Waves",
          "content": "\nIn 1924, Louis de Broglie hypothesized that nature possesses deep physical symmetry: if electromagnetic waves exhibit particle properties (photons with momentum $p = h/\\lambda$), then material particles with mass $m$ and momentum $p$ must simultaneously exhibit wave properties.\n\n#### The de Broglie Relations\nFor any physical entity with energy $E$ and momentum $\\mathbf{p}$:\n\n$$\\lambda = \\frac{h}{p} = \\frac{h}{mv}, \\qquad \\mathbf{p} = \\hbar \\mathbf{k}, \\qquad E = \\hbar \\omega$$\n\nwhere $\\mathbf{k}$ is the wave vector ($|\\mathbf{k}| = 2\\pi/\\lambda$) and $\\omega$ is the angular frequency.\n\n#### Bohr's Orbit as a Standing Wave\nde Broglie provided an intuitive physical basis for Bohr's angular momentum quantization: an electron orbit is stable because it forms a **standing de Broglie wave** around the nucleus. Constructive interference requires an integral number of wavelengths around the circular circumference:\n\n$$2\\pi r_n = n \\lambda = n \\left( \\frac{h}{m_e v_n} \\right) \\implies m_e v_n r_n = n\\hbar$$\n\n#### Experimental Confirmation: The Davisson-Germer Experiment (1927)\nClinton Davisson and Lester Germer fired low-energy electrons ($54 \\text{ eV}$) at a crystalline nickel target and recorded an intense diffraction peak at a scattering angle of $\\theta = 50^\\circ$.\n\nUsing Bragg's law for crystal diffraction ($n\\lambda = 2d \\sin\\phi$):\n* Crystal plane spacing $d = 0.091 \\text{ nm}$, glancing angle $\\phi = 65^\\circ$\n* Measured Bragg wavelength: $\\lambda_{\\text{exp}} = 2(0.091 \\text{ nm})\\sin(65^\\circ) = 0.165 \\text{ nm}$.\n* Theoretical de Broglie calculation for a $54\\text{ eV}$ electron:\n$$\\lambda_{\\text{theory}} = \\frac{h}{\\sqrt{2 m_e E}} = \\frac{6.626 \\times 10^{-34}}{\\sqrt{2 (9.109 \\times 10^{-31}) (54 \\times 1.602 \\times 10^{-19})}} = 0.167 \\text{ nm}$$\n\nThe theoretical and experimental values matched within experimental error, providing definitive proof of matter waves.\n\nExplore this directly in **Simulation 1.1** below, where individual electron hits build an interference pattern on a phosphor screen, demonstrating wave-particle duality.\n          ",
          "simulation": "double-slit"
        },
        {
          "secNumber": "1.4",
          "heading": "The Heisenberg Uncertainty Principle",
          "content": "\n#### Mathematical Origin: Fourier Conjugacy\nIn classical mechanics, a particle has simultaneously well-defined position $x(t)$ and momentum $p(t)$. In quantum mechanics, a localized spatial entity is described by a wave packet formed by superposing monochromatic plane waves:\n\n$$\\psi(x) = \\frac{1}{\\sqrt{2\\pi}} \\int_{-\\infty}^{+\\infty} \\phi(k) e^{i k x} dk$$\n\nThe spatial wavefunction $\\psi(x)$ and the wave-number distribution $\\phi(k)$ form a **Fourier transform pair**. From the fundamental bandwidth theorem of harmonic analysis, any wave packet has a spatial spread $\\Delta x$ and a wavenumber spread $\\Delta k$ bounded by:\n\n$$\\Delta x \\cdot \\Delta k \\ge \\frac{1}{2}$$\n\nSubstituting the de Broglie relation $p = \\hbar k \\implies \\Delta p = \\hbar \\Delta k$ yields the **Heisenberg Uncertainty Principle**:\n\n$$\\Delta x \\cdot \\Delta p_x \\ge \\frac{\\hbar}{2}$$\n\n#### Physical Meaning and Gaussian Minimum Uncertainty\nHere, the uncertainties are formally defined as the statistical standard deviations (root-mean-square variances) of the observables:\n\n$$\\Delta x = \\sqrt{\\langle x^2 \\rangle - \\langle x \\rangle^2}, \\qquad \\Delta p = \\sqrt{\\langle p^2 \\rangle - \\langle p \\rangle^2}$$\n\nThe lower bound $\\frac{\\hbar}{2}$ is saturated exclusively by a **Gaussian wave packet**:\n\n$$\\psi_G(x) = \\left( \\frac{1}{2\\pi \\sigma^2} \\right)^{1/4} e^{-\\frac{x^2}{4\\sigma^2}} e^{i k_0 x} \\implies \\Delta x = \\sigma, \\quad \\Delta p = \\frac{\\hbar}{2\\sigma} \\implies \\Delta x \\cdot \\Delta p = \\frac{\\hbar}{2}$$\n\nAny other wave packet shape has an uncertainty product strictly greater than $\\hbar/2$.\n\n#### Energy-Time Uncertainty Relation\nA complementary uncertainty relation connects energy and time:\n\n$$\\Delta E \\cdot \\Delta t \\ge \\frac{\\hbar}{2}$$\n\nWhere $\\Delta t$ represents the characteristic time interval over which an expectation value changes appreciably: $\\Delta t = \\frac{\\Delta A}{|d\\langle A \\rangle / dt|}$. This explains why unstable excited states with short lifetimes $\\tau$ display an intrinsic spectral energy line width:\n\n$$\\Gamma \\approx \\frac{\\hbar}{\\tau}$$\n\nTest this principle in **Simulation 1.2** below: adjust the spatial width $\\Delta x$ and observe the conjugate momentum distribution $\\Delta p$ widen in response.\n          ",
          "simulation": "uncertainty-principle"
        }
      ],
      "problems": [
        {
          "id": "p1-1",
          "difficulty": "Easy",
          "title": "de Broglie Wavelength of Relativistic vs Non-Relativistic Electrons",
          "question": "An electron is accelerated from rest through an electrostatic potential difference of $V = 150 \\text{ V}$.\\n(a) Determine its de Broglie wavelength using non-relativistic mechanics.\\n(b) At what accelerating potential does the relativistic correction to the de Broglie wavelength exceed $1\\%$?",
          "steps": [
            {
              "stepName": "Step 1: Non-relativistic Calculation",
              "math": "K = e V = 150 \\text{ eV} = 150 \\times 1.602 \\times 10^{-19} \\text{ J} = 2.403 \\times 10^{-17} \\text{ J}\n$$\n$$p = \\sqrt{2 m_e K} = \\sqrt{2(9.109 \\times 10^{-31} \\text{ kg})(2.403 \\times 10^{-17} \\text{ J})} = 6.617 \\times 10^{-24} \\text{ kg}\\cdot\\text{m/s}\n$$\n$$\\lambda = \\frac{h}{p} = \\frac{6.626 \\times 10^{-34} \\text{ J}\\cdot\\text{s}}{6.617 \\times 10^{-24} \\text{ kg}\\cdot\\text{m/s}} = 1.001 \\times 10^{-10} \\text{ m} = 1.001 \\text{ Å}",
              "explanation": "For quick calculations, note that $\\lambda = \\sqrt{\\frac{150}{V}} \\text{ Å}$. For $V = 150 \\text{ V}$, $\\lambda = 1.00 \\text{ Å}$, which corresponds to typical atomic crystal lattice spacings."
            },
            {
              "stepName": "Step 2: Relativistic Condition",
              "math": "E^2 = p^2 c^2 + m_0^2 c^4 \\implies p = \\frac{1}{c}\\sqrt{K(K + 2m_0 c^2)}\n$$\n$$\\lambda_{\\text{rel}} = \\frac{h c}{\\sqrt{K(K + 2m_0 c^2)}} = \\frac{\\lambda_{\\text{class}}}{\\sqrt{1 + \\frac{K}{2m_0 c^2}}} \\approx \\lambda_{\\text{class}}\\left(1 - \\frac{K}{4 m_0 c^2}\\right)\n$$\n$$\\frac{\\Delta \\lambda}{\\lambda} \\approx \\frac{K}{4 m_0 c^2} \\ge 0.01 \\implies K \\ge 0.04 m_0 c^2 = 0.04 (511 \\text{ keV}) \\approx 20.44 \\text{ keV}",
              "explanation": "When accelerating potentials exceed roughly $20 \\text{ kV}$ (typical in transmission electron microscopes), relativistic momentum corrections become necessary."
            }
          ]
        },
        {
          "id": "p1-2",
          "difficulty": "Medium",
          "title": "Rigorous Proof of Ground-State Energy of Hydrogen via Uncertainty Principle",
          "question": "Using the Heisenberg uncertainty relation $\\Delta x \\cdot \\Delta p \\ge \\hbar/2$, derive an order-of-magnitude estimate for the ground-state radius (Bohr radius) and binding energy of the hydrogen atom without solving the Schrödinger equation.",
          "steps": [
            {
              "stepName": "Step 1: Express total energy in terms of uncertainty",
              "math": "E = K + U = \\frac{p^2}{2m_e} - \\frac{e^2}{4\\pi \\epsilon_0 r}\n$$\n$$\\text{Setting } r \\approx \\Delta x \\text{ and } p \\approx \\Delta p \\ge \\frac{\\hbar}{2r} \\implies p \\approx \\frac{\\hbar}{r}\n$$\n$$E(r) = \\frac{\\hbar^2}{2 m_e r^2} - \\frac{e^2}{4\\pi \\epsilon_0 r}",
              "explanation": "The kinetic energy term scales as $1/r^2$ due to quantum confinement (confinement increases momentum spread), while the attractive Coulomb potential scales as $-1/r$. The competition between these two terms creates a stable ground state."
            },
            {
              "stepName": "Step 2: Minimize E(r) with respect to r",
              "math": "\\frac{dE}{dr} = -\\frac{\\hbar^2}{m_e r^3} + \\frac{e^2}{4\\pi \\epsilon_0 r^2} = 0\n$$\n$$\\frac{\\hbar^2}{m_e r^3} = \\frac{e^2}{4\\pi \\epsilon_0 r^2} \\implies r_0 = \\frac{4\\pi \\epsilon_0 \\hbar^2}{m_e e^2} = a_0 \\approx 0.529 \\text{ Å}\n$$\n$$E(r_0) = \\frac{\\hbar^2}{2 m_e a_0^2} - \\frac{e^2}{4\\pi \\epsilon_0 a_0} = -\\frac{m_e e^4}{32 \\pi^2 \\epsilon_0^2 \\hbar^2} = -13.6 \\text{ eV}",
              "explanation": "This shows that atomic stability is a direct consequence of the Heisenberg uncertainty principle: if the electron collapsed into the nucleus ($r \\to 0$), its kinetic energy would diverge as $+1/r^2$, overwhelming the Coulomb attraction."
            }
          ]
        }
      ]
    },
    {
      "id": "unit-2",
      "number": 2,
      "title": "Mathematical Formulation & Postulates of Quantum Mechanics",
      "lectures": 10,
      "leadSummary": "The axiomatic mathematical structure of quantum theory: abstract Hilbert space, Dirac bra-ket notation, linear Hermitian operators, eigenvalue equations, spectral decomposition, commutation algebra, generalized uncertainty relations, and measurement postulates.",
      "simulations": [
        "quantum-measurement"
      ],
      "sections": [
        {
          "secNumber": "2.1",
          "heading": "Hilbert Space and Dirac Bra-Ket Notation",
          "content": "\n#### Mathematical Foundation: Hilbert Space $\\mathcal{H}$\nIn quantum mechanics, the state of a physical system is represented by a state vector $|\\psi\\rangle$ living in a complex linear vector space endowed with an inner product: a **Hilbert Space** $\\mathcal{H}$.\n\nA Hilbert space satisfies four core mathematical criteria:\n1. **Linearity:** If $|\\psi_1\\rangle, |\\psi_2\\rangle \\in \\mathcal{H}$, then for any complex scalars $c_1, c_2 \\in \\mathbb{C}$, the linear superposition $c_1|\\psi_1\\rangle + c_2|\\psi_2\\rangle \\in \\mathcal{H}$.\n2. **Inner Product:** For any two vectors $|\\phi\\rangle, |\\psi\\rangle \\in \\mathcal{H}$, there exists a complex scalar $\\langle \\phi | \\psi \\rangle$ satisfying:\n   - Conjugate symmetry: $\\langle \\phi | \\psi \\rangle = \\langle \\psi | \\phi \\rangle^*$\n   - Linearity in the second argument: $\\langle \\phi | c_1 \\psi_1 + c_2 \\psi_2 \\rangle = c_1 \\langle \\phi | \\psi_1 \\rangle + c_2 \\langle \\phi | \\psi_2 \\rangle$\n   - Positive-definiteness: $\\langle \\psi | \\psi \\rangle \\ge 0$, and $\\langle \\psi | \\psi \\rangle = 0 \\iff |\\psi\\rangle = 0$.\n3. **Cauchy Completeness:** Every Cauchy sequence of vectors in $\\mathcal{H}$ converges to an element within $\\mathcal{H}$ under the norm $||\\psi|| = \\sqrt{\\langle \\psi | \\psi \\rangle}$.\n4. **Separability:** The space possesses a countable dense subset, ensuring the existence of an orthonormal basis.\n\n#### Dirac Notation: Kets, Bras, and Dual Space\n* **Ket Vector $|\\psi\\rangle$:** Represents a state vector in $\\mathcal{H}$.\n* **Bra Vector $\\langle \\phi |$:** Represents a continuous linear functional in the dual space $\\mathcal{H}^*$. By the Riesz Representation Theorem, every bra $\\langle \\phi |$ corresponds uniquely to a ket $|\\phi\\rangle$.\n* **Wavefunction in Position Representation:** The continuous spatial wavefunction $\\psi(x)$ is simply the inner product projection of the abstract state vector $|\\psi\\rangle$ onto the continuous coordinate basis kets $|x\\rangle$:\n$$\\psi(x) = \\langle x | \\psi \\rangle, \\qquad \\psi^*(x) = \\langle \\psi | x \\rangle$$\nThe inner product of two wavefunctions is given by:\n$$\\langle \\phi | \\psi \\rangle = \\int_{-\\infty}^{+\\infty} \\langle \\phi | x \\rangle \\langle x | \\psi \\rangle dx = \\int_{-\\infty}^{+\\infty} \\phi^*(x) \\psi(x) dx$$\n          "
        },
        {
          "secNumber": "2.2",
          "heading": "Linear and Hermitian Operators",
          "content": "\n#### Linear Operators\nAn operator $\\hat{A}$ maps kets to kets: $\\hat{A}|\\psi\\rangle = |\\psi'\\rangle$. An operator is **linear** if:\n\n$$\\hat{A}(c_1 |\\psi_1\\rangle + c_2 |\\psi_2\\rangle) = c_1 \\hat{A}|\\psi_1\\rangle + c_2 \\hat{A}|\\psi_2\\rangle$$\n\n#### Adjoint (Hermitian Conjugate) Operator $\\hat{A}^\\dagger$\nThe adjoint of an operator $\\hat{A}$, denoted $\\hat{A}^\\dagger$, is defined through the inner product relation:\n\n$$\\langle \\phi | \\hat{A} | \\psi \\rangle = \\langle \\hat{A}^\\dagger \\phi | \\psi \\rangle = \\left( \\langle \\psi | \\hat{A}^\\dagger | \\phi \\rangle \\right)^*$$\n\nProperties of the adjoint:\n* $(\\hat{A}^\\dagger)^\\dagger = \\hat{A}$\n* $(c \\hat{A})^\\dagger = c^* \\hat{A}^\\dagger$\n* $(\\hat{A} + \\hat{B})^\\dagger = \\hat{A}^\\dagger + \\hat{B}^\\dagger$\n* $(\\hat{A}\\hat{B})^\\dagger = \\hat{B}^\\dagger \\hat{A}^\\dagger$\n\n#### Hermitian (Self-Adjoint) Operators\nAn operator is **Hermitian** if it equals its own adjoint:\n\n$$\\hat{A}^\\dagger = \\hat{A} \\iff \\langle \\phi | \\hat{A} | \\psi \\rangle = \\langle \\hat{A} \\phi | \\psi \\rangle$$\n\n#### Fundamental Theorems of Hermitian Operators\n1. **Theorem 1: The eigenvalues of a Hermitian operator are strictly real.**\n   * *Proof:* Let $\\hat{A}|\\psi\\rangle = a|\\psi\\rangle$ with $\\langle \\psi | \\psi \\rangle \\ne 0$.\n   $$\\langle \\psi | \\hat{A} | \\psi \\rangle = a \\langle \\psi | \\psi \\rangle$$\n   Taking the complex conjugate and using $\\hat{A} = \\hat{A}^\\dagger$:\n   $$\\langle \\psi | \\hat{A} | \\psi \\rangle^* = \\langle \\psi | \\hat{A}^\\dagger | \\psi \\rangle = \\langle \\psi | \\hat{A} | \\psi \\rangle = a^* \\langle \\psi | \\psi \\rangle$$\n   Therefore, $(a - a^*)\\langle \\psi | \\psi \\rangle = 0$. Since $\\langle \\psi | \\psi \\rangle > 0$, we have $a = a^* \\implies a \\in \\mathbb{R}$.\n\n2. **Theorem 2: Eigenvectors corresponding to distinct eigenvalues are orthogonal.**\n   * *Proof:* Let $\\hat{A}|\\phi_1\\rangle = a_1|\\phi_1\\rangle$ and $\\hat{A}|\\phi_2\\rangle = a_2|\\phi_2\\rangle$ with $a_1 \\ne a_2$.\n   $$\\langle \\phi_2 | \\hat{A} | \\phi_1 \\rangle = a_1 \\langle \\phi_2 | \\phi_1 \\rangle$$\n   $$\\langle \\phi_2 | \\hat{A} | \\phi_1 \\rangle = \\langle \\hat{A} \\phi_2 | \\phi_1 \\rangle = a_2^* \\langle \\phi_2 | \\phi_1 \\rangle = a_2 \\langle \\phi_2 | \\phi_1 \\rangle$$\n   Subtracting gives: $(a_1 - a_2) \\langle \\phi_2 | \\phi_1 \\rangle = 0$. Since $a_1 \\ne a_2$, it follows that $\\langle \\phi_2 | \\phi_1 \\rangle = 0$.\n          "
        },
        {
          "secNumber": "2.3",
          "heading": "Commutator Algebra and Compatible Observables",
          "content": "\n#### Commutator Definition and Properties\nThe commutator of two operators $\\hat{A}$ and $\\hat{B}$ is defined as:\n\n$$[\\hat{A}, \\hat{B}] = \\hat{A}\\hat{B} - \\hat{B}\\hat{A}$$\n\nFundamental identities:\n* Anti-symmetry: $[\\hat{A}, \\hat{B}] = -[\\hat{B}, \\hat{A}]$\n* Linearity: $[\\hat{A}, \\hat{B} + \\hat{C}] = [\\hat{A}, \\hat{B}] + [\\hat{A}, \\hat{C}]$\n* Product rule: $[\\hat{A}, \\hat{B}\\hat{C}] = [\\hat{A}, \\hat{B}]\\hat{C} + \\hat{B}[\\hat{A}, \\hat{C}]$\n* Product rule: $[\\hat{A}\\hat{B}, \\hat{C}] = \\hat{A}[\\hat{B}, \\hat{C}] + [\\hat{A}, \\hat{C}]\\hat{B}$\n* Jacobi Identity: $[\\hat{A}, [\\hat{B}, \\hat{C}]] + [\\hat{B}, [\\hat{C}, \\hat{A}]] + [\\hat{C}, [\\hat{A}, \\hat{B}]] = 0$\n\n#### The Fundamental Position-Momentum Commutator\nApplying $[\\hat{x}, \\hat{p}]$ to an arbitrary differentiable test function $f(x)$:\n\n$$[\\hat{x}, \\hat{p}]f(x) = x\\left(-i\\hbar \\frac{df}{dx}\\right) - \\left(-i\\hbar \\frac{d}{dx}(x f(x))\\right) = -i\\hbar x \\frac{df}{dx} + i\\hbar\\left(f + x\\frac{df}{dx}\\right) = i\\hbar f(x)$$\n\n$$\\implies [\\hat{x}, \\hat{p}] = i\\hbar \\hat{I}$$\n\n#### Generalized Robertson-Schrödinger Uncertainty Relation\nFor any two Hermitian observables $\\hat{A}$ and $\\hat{B}$:\n\n$$\\Delta A \\cdot \\Delta B \\ge \\frac{1}{2} |\\langle [\\hat{A}, \\hat{B}] \\rangle|$$\n\nIf $[\\hat{A}, \\hat{B}] = 0$, the observables are **compatible**: they share a common complete set of simultaneous eigenstates and can be measured simultaneously to arbitrary precision. If $[\\hat{A}, \\hat{B}] \\ne 0$, they are **incompatible**, giving rise to an uncertainty relation.\n          "
        },
        {
          "secNumber": "2.4",
          "heading": "The Postulates of Quantum Mechanics",
          "content": "\nThe complete theoretical structure of nonrelativistic quantum mechanics is founded upon five core postulates:\n\n1. **Postulate 1 (State of the System):** At any given time $t$, the state of a physical system is completely specified by a normalized state vector $|\\psi(t)\\rangle$ residing in a complex Hilbert space $\\mathcal{H}$.\n2. **Postulate 2 (Observables):** Every physically measurable dynamical variable $\\mathcal{A}$ is represented by a linear Hermitian operator $\\hat{A}$ acting in $\\mathcal{H}$.\n3. **Postulate 3 (Possible Measurement Outcomes):** The measurement of an observable $\\mathcal{A}$ can yield only one of the eigenvalues $a_n$ of the corresponding Hermitian operator equation:\n$$\\hat{A}|\\phi_n\\rangle = a_n |\\phi_n\\rangle$$\n4. **Postulate 4 (Born's Probabilistic Interpretation & State Reduction):** If a system is in state $|\\psi\\rangle$, the probability of obtaining non-degenerate eigenvalue $a_n$ upon measurement of $\\hat{A}$ is given by:\n$$P(a_n) = \\frac{|\\langle \\phi_n | \\psi \\rangle|^2}{\\langle \\psi | \\psi \\rangle}$$\nImmediately following the measurement, if eigenvalue $a_n$ is obtained, the state vector collapses into the corresponding eigenstate:\n$$|\\psi\\rangle \\xrightarrow{\\text{measurement}} |\\phi_n\\rangle$$\nThe expectation value of $\\hat{A}$ across an ensemble of identically prepared systems is:\n$$\\langle \\hat{A} \\rangle = \\frac{\\langle \\psi | \\hat{A} | \\psi \\rangle}{\\langle \\psi | \\psi \\rangle}$$\n5. **Postulate 5 (Time Evolution):** Between measurements, the time evolution of the state vector $|\\psi(t)\\rangle$ is governed by the deterministic **Time-Dependent Schrödinger Equation**:\n$$i\\hbar \\frac{\\partial}{\\partial t}|\\psi(t)\\rangle = \\hat{H}(t)|\\psi(t)\\rangle$$\nwhere $\\hat{H}$ is the Hamiltonian operator of the system.\n\nExamine state reduction in **Simulation 2.1** below, which lets you prepare a two-level superposition state and trigger wavefunction collapse into individual eigenstates.\n          ",
          "simulation": "quantum-measurement"
        }
      ],
      "problems": [
        {
          "id": "p2-1",
          "difficulty": "Hard",
          "title": "Commutator Algebra: [x^n, p] and Generalized Ehrenfest Relation",
          "question": "Prove by induction that $[\\hat{x}^n, \\hat{p}] = i\\hbar n \\hat{x}^{n-1}$ for any integer $n \\ge 1$. Hence, evaluate $[f(\\hat{x}), \\hat{p}]$ for any analytic function $f(x)$.",
          "steps": [
            {
              "stepName": "Step 1: Base Case and Product Rule Induction",
              "math": "\\text{For } n = 1: [\\hat{x}, \\hat{p}] = i\\hbar \\hat{I} \\quad (\\text{Holds})\n$$\n$$\\text{Assume true for } n = k: [\\hat{x}^k, \\hat{p}] = i\\hbar k \\hat{x}^{k-1}\n$$\n$$\\text{For } n = k+1: [\\hat{x}^{k+1}, \\hat{p}] = [\\hat{x}^k \\hat{x}, \\hat{p}] = \\hat{x}^k [\\hat{x}, \\hat{p}] + [\\hat{x}^k, \\hat{p}]\\hat{x}\n$$\n$$= \\hat{x}^k (i\\hbar) + (i\\hbar k \\hat{x}^{k-1})\\hat{x} = i\\hbar \\hat{x}^k + i\\hbar k \\hat{x}^k = i\\hbar (k+1) \\hat{x}^k",
              "explanation": "The relation holds for $n=1$, and if it holds for $n=k$, it holds for $n=k+1$. By mathematical induction, it holds for all positive integers $n$."
            },
            {
              "stepName": "Step 2: Extension to Analytic Functions",
              "math": "f(\\hat{x}) = \\sum_{n=0}^\\infty c_n \\hat{x}^n\n$$\n$$[f(\\hat{x}), \\hat{p}] = \\sum_{n=0}^\\infty c_n [\\hat{x}^n, \\hat{p}] = \\sum_{n=1}^\\infty c_n (i\\hbar n \\hat{x}^{n-1}) = i\\hbar \\frac{df(\\hat{x})}{d\\hat{x}}",
              "explanation": "This commutator identity is widely used in quantum mechanics to derive the equations of motion for expectation values."
            }
          ]
        }
      ]
    },
    {
      "id": "unit-3",
      "number": 3,
      "title": "Schrödinger’s Equation, Probability Current & Ehrenfest Theorems",
      "lectures": 12,
      "leadSummary": "The dynamics of wave mechanics: derivation of the Time-Dependent and Time-Independent Schrödinger equations, stationary states, the conservation of probability, continuity equation, probability current density, time variation of observables, and Ehrenfest's theorem connecting quantum and classical trajectories.",
      "simulations": [
        "wavepacket-dispersion"
      ],
      "sections": [
        {
          "secNumber": "3.1",
          "heading": "The Schrödinger Wave Equations",
          "content": "\n#### The Time-Dependent Schrödinger Equation (TDSE)\nIn 1926, Erwin Schrödinger formulated the fundamental wave equation for a non-relativistic particle of mass $m$ subjected to a potential energy $V(\\mathbf{r}, t)$:\n\n$$i\\hbar \\frac{\\partial \\Psi(\\mathbf{r}, t)}{\\partial t} = \\hat{H}\\Psi(\\mathbf{r}, t) = \\left( -\\frac{\\hbar^2}{2m}\\nabla^2 + V(\\mathbf{r}, t) \\right) \\Psi(\\mathbf{r}, t)$$\n\nWhere:\n* $i = \\sqrt{-1}$ is the imaginary unit.\n* $\\nabla^2 = \\frac{\\partial^2}{\\partial x^2} + \\frac{\\partial^2}{\\partial y^2} + \\frac{\\partial^2}{\\partial z^2}$ is the spatial Laplacian operator.\n* $\\hat{H} = \\frac{\\hat{p}^2}{2m} + V(\\mathbf{r})$ is the Hamiltonian operator.\n\nBecause the TDSE is first-order in time $t$, specifying the initial wavefunction $\\Psi(\\mathbf{r}, 0)$ uniquely determines $\\Psi(\\mathbf{r}, t)$ for all future times. Because it is linear in $\\Psi$, it satisfies the superposition principle.\n\n#### Separation of Variables: The Time-Independent Schrödinger Equation (TISE)\nWhen the potential energy is independent of time ($V(\\mathbf{r}, t) = V(\\mathbf{r})$), we seek product solutions:\n\n$$\\Psi(\\mathbf{r}, t) = \\psi(\\mathbf{r}) \\phi(t)$$\n\nSubstituting into the TDSE and dividing both sides by $\\psi(\\mathbf{r}) \\phi(t)$:\n\n$$i\\hbar \\frac{1}{\\phi(t)} \\frac{d\\phi(t)}{dt} = \\frac{1}{\\psi(\\mathbf{r})} \\left( -\\frac{\\hbar^2}{2m}\\nabla^2 + V(\\mathbf{r}) \\right) \\psi(\\mathbf{r})$$\n\nThe left side depends solely on $t$, while the right side depends solely on $\\mathbf{r}$. Both sides must therefore equal a separation constant $E$ with dimensions of energy:\n\n1. **Temporal Differential Equation:**\n$$i\\hbar \\frac{d\\phi(t)}{dt} = E \\phi(t) \\implies \\phi(t) = e^{-i E t / \\hbar}$$\n2. **Spatial Differential Equation (TISE):**\n$$\\hat{H}\\psi(\\mathbf{r}) = E\\psi(\\mathbf{r}) \\implies -\\frac{\\hbar^2}{2m}\\nabla^2\\psi(\\mathbf{r}) + V(\\mathbf{r})\\psi(\\mathbf{r}) = E\\psi(\\mathbf{r})$$\n\n#### Stationary States and Their Properties\nSolutions of the form $\\Psi_n(\\mathbf{r}, t) = \\psi_n(\\mathbf{r}) e^{-i E_n t / \\hbar}$ are called **stationary states** because their physical properties are time-independent:\n1. **Probability Density:**\n$$\\rho(\\mathbf{r}, t) = |\\Psi_n(\\mathbf{r}, t)|^2 = \\left| \\psi_n(\\mathbf{r}) e^{-i E_n t / \\hbar} \\right|^2 = |\\psi_n(\\mathbf{r})|^2$$\n2. **Expectation Values:** For any time-independent observable $\\hat{A}$:\n$$\\langle \\hat{A} \\rangle_t = \\int \\Psi_n^* \\hat{A} \\Psi_n d^3\\mathbf{r} = \\int \\psi_n^* e^{i E_n t/\\hbar} \\hat{A} \\psi_n e^{-i E_n t/\\hbar} d^3\\mathbf{r} = \\langle \\hat{A} \\rangle_0 = \\text{constant}$$\n          "
        },
        {
          "secNumber": "3.2",
          "heading": "Conservation of Probability and the Continuity Equation",
          "content": "\n#### Mathematical Derivation of the Continuity Equation\nThe total probability of finding a particle in all of space is:\n\n$$P(t) = \\int_{-\\infty}^{+\\infty} |\\Psi(x,t)|^2 dx = \\int_{-\\infty}^{+\\infty} \\Psi^*(x,t) \\Psi(x,t) dx$$\n\nTaking the time derivative:\n\n$$\\frac{dP}{dt} = \\int_{-\\infty}^{+\\infty} \\frac{\\partial}{\\partial t}(\\Psi^* \\Psi) dx = \\int_{-\\infty}^{+\\infty} \\left( \\frac{\\partial \\Psi^*}{\\partial t} \\Psi + \\Psi^* \\frac{\\partial \\Psi}{\\partial t} \\right) dx$$\n\nFrom the TDSE:\n\n$$\\frac{\\partial \\Psi}{\\partial t} = \\frac{1}{i\\hbar} \\left( -\\frac{\\hbar^2}{2m} \\frac{\\partial^2 \\Psi}{\\partial x^2} + V \\Psi \\right) = \\frac{i\\hbar}{2m} \\frac{\\partial^2 \\Psi}{\\partial x^2} - \\frac{i}{\\hbar} V \\Psi$$\n\nTaking the complex conjugate:\n\n$$\\frac{\\partial \\Psi^*}{\\partial t} = -\\frac{i\\hbar}{2m} \\frac{\\partial^2 \\Psi^*}{\\partial x^2} + \\frac{i}{\\hbar} V \\Psi^*$$\n\nSubstituting these into the time derivative of the probability density $\\rho = \\Psi^* \\Psi$:\n\n$$\\frac{\\partial \\rho}{\\partial t} = \\left( -\\frac{i\\hbar}{2m} \\frac{\\partial^2 \\Psi^*}{\\partial x^2} + \\frac{i}{\\hbar} V \\Psi^* \\right) \\Psi + \\Psi^* \\left( \\frac{i\\hbar}{2m} \\frac{\\partial^2 \\Psi}{\\partial x^2} - \\frac{i}{\\hbar} V \\Psi \\right)$$\n\nThe potential terms cancel:\n\n$$\\frac{\\partial \\rho}{\\partial t} = \\frac{i\\hbar}{2m} \\left( \\Psi^* \\frac{\\partial^2 \\Psi}{\\partial x^2} - \\Psi \\frac{\\partial^2 \\Psi^*}{\\partial x^2} \\right) = -\\frac{\\partial}{\\partial x} \\left[ \\frac{\\hbar}{2mi} \\left( \\Psi^* \\frac{\\partial \\Psi}{\\partial x} - \\Psi \\frac{\\partial \\Psi^*}{\\partial x} \\right) \\right]$$\n\nDefining the **Probability Current Density** $J(x,t)$:\n\n$$J(x,t) = \\frac{\\hbar}{2mi} \\left( \\Psi^* \\frac{\\partial \\Psi}{\\partial x} - \\Psi \\frac{\\partial \\Psi^*}{\\partial x} \\right) = \\frac{\\hbar}{m} \\text{Im}\\left( \\Psi^* \\frac{\\partial \\Psi}{\\partial x} \\right)$$\n\nThis yields the **Quantum Continuity Equation**:\n\n$$\\frac{\\partial \\rho(x,t)}{\\partial t} + \\frac{\\partial J(x,t)}{\\partial x} = 0 \\qquad \\left( \\text{or in 3D: } \\frac{\\partial \\rho}{\\partial t} + \\nabla \\cdot \\mathbf{J} = 0 \\right)$$\n\nIntegrating over all space:\n\n$$\\frac{dP}{dt} = -\\int_{-\\infty}^{+\\infty} \\frac{\\partial J}{\\partial x} dx = -[J(\\infty, t) - J(-\\infty, t)] = 0$$\n\nSince physical wavefunctions must vanish at infinity for square-integrability, $J(\\pm \\infty, t) = 0$. Consequently, total probability is conserved for all time: $\\int_{-\\infty}^{+\\infty} |\\Psi(x,t)|^2 dx = 1$.\n          "
        },
        {
          "secNumber": "3.3",
          "heading": "Time Evolution of Observables and Ehrenfest's Theorem",
          "content": "\n#### General Equation of Motion for Expectation Values\nLet $\\hat{A}$ be an arbitrary quantum observable. Its expectation value is $\\langle A \\rangle = \\langle \\Psi | \\hat{A} | \\Psi \\rangle$. Taking the total time derivative:\n\n$$\\frac{d\\langle A \\rangle}{dt} = \\frac{d}{dt} \\langle \\Psi | \\hat{A} | \\Psi \\rangle = \\left( \\frac{d}{dt}\\langle \\Psi | \\right) \\hat{A} |\\psi\\rangle + \\langle \\Psi | \\frac{\\partial \\hat{A}}{\\partial t} | \\Psi \\rangle + \\langle \\Psi | \\hat{A} \\left( \\frac{d}{dt}|\\psi\\rangle \\right)$$\n\nUsing the TDSE $|\\dot{\\Psi}\\rangle = \\frac{1}{i\\hbar}\\hat{H}|\\Psi\\rangle$ and $\\langle \\dot{\\Psi}| = -\\frac{1}{i\\hbar}\\langle \\Psi|\\hat{H}$:\n\n$$\\frac{d\\langle A \\rangle}{dt} = -\\frac{1}{i\\hbar}\\langle \\Psi | \\hat{H}\\hat{A} | \\Psi \\rangle + \\frac{1}{i\\hbar}\\langle \\Psi | \\hat{A}\\hat{H} | \\Psi \\rangle + \\left\\langle \\frac{\\partial \\hat{A}}{\\partial t} \\right\\rangle$$\n\n$$\\frac{d\\langle A \\rangle}{dt} = \\frac{1}{i\\hbar} \\langle [\\hat{A}, \\hat{H}] \\rangle + \\left\\langle \\frac{\\partial \\hat{A}}{\\partial t} \\right\\rangle$$\n\n#### Constants of Motion\nIf an observable $\\hat{A}$ has no explicit time dependence ($\\frac{\\partial \\hat{A}}{\\partial t} = 0$) and commutes with the Hamiltonian ($[\\hat{A}, \\hat{H}] = 0$), then:\n\n$$\\frac{d\\langle A \\rangle}{dt} = 0$$\n\nSuch an observable is a **constant of motion**. Its expectation value is time-independent in any state.\n\n#### Ehrenfest's Theorems (The Classical Limit)\nPaul Ehrenfest (1927) showed that quantum expectation values obey classical equations of motion:\n\n1. **First Ehrenfest Theorem (Position):**\nLet $\\hat{A} = \\hat{x}$. Commuting with $\\hat{H} = \\frac{\\hat{p}^2}{2m} + V(\\hat{x})$:\n$$[\\hat{x}, \\hat{H}] = \\left[ \\hat{x}, \\frac{\\hat{p}^2}{2m} \\right] = \\frac{1}{2m} (\\hat{p}[\\hat{x}, \\hat{p}] + [\\hat{x}, \\hat{p}]\\hat{p}) = \\frac{i\\hbar}{m}\\hat{p}$$\n$$\\frac{d\\langle x \\rangle}{dt} = \\frac{1}{i\\hbar}\\left( \\frac{i\\hbar}{m}\\langle p \\rangle \\right) \\implies \\frac{d\\langle x \\rangle}{dt} = \\frac{\\langle p \\rangle}{m}$$\n\n2. **Second Ehrenfest Theorem (Momentum):**\nLet $\\hat{A} = \\hat{p}$. Commuting with $\\hat{H}$:\n$$[\\hat{p}, \\hat{H}] = [\\hat{p}, V(\\hat{x})] = -i\\hbar \\frac{\\partial V}{\\partial x}$$\n$$\\frac{d\\langle p \\rangle}{dt} = \\frac{1}{i\\hbar}\\left( -i\\hbar \\left\\langle \\frac{\\partial V}{\\partial x} \\right\\rangle \\right) \\implies \\frac{d\\langle p \\rangle}{dt} = -\\left\\langle \\frac{\\partial V(\\hat{x})}{\\partial x} \\right\\rangle = \\langle F(\\hat{x}) \\rangle$$\n\nThis reproduces Newton's Second Law ($mathbf{F} = mmathbf{a}$) for expectation values, showing how classical physics emerges from quantum mechanics in macroscopic systems.\n\nSee **Simulation 3.1** below for a real-time visualization of a free Gaussian wavepacket spreading and dispersing over time.\n          ",
          "simulation": "wavepacket-dispersion"
        }
      ],
      "problems": [
        {
          "id": "p3-1",
          "difficulty": "Hard",
          "title": "Rigorous Calculation of Gaussian Wave Packet Dispersion Rate",
          "question": "A free particle ($V(x)=0$) is initialized at $t=0$ as a Gaussian wave packet $\\psi(x,0) = (2\\pi\\sigma_0^2)^{-1/4} e^{-x^2 / 4\\sigma_0^2}$. Solve the time-dependent Schrödinger equation to find $\\psi(x,t)$, and prove that the packet width broadens according to $\\sigma(t) = \\sigma_0 \\sqrt{1 + \\left( \\frac{\\hbar t}{2m\\sigma_0^2} \\right)^2}$.",
          "steps": [
            {
              "stepName": "Step 1: Fourier Transform to Momentum Space",
              "math": "\\phi(k) = \\frac{1}{\\sqrt{2\\pi}} \\int_{-\\infty}^{+\\infty} \\psi(x,0) e^{-i k x} dx = \\left( \\frac{2\\sigma_0^2}{\\pi} \\right)^{1/4} e^{-\\sigma_0^2 k^2}",
              "explanation": "In momentum space, each plane wave component evolves with a simple phase factor: $e^{-i E_k t / \\hbar} = e^{-i \\frac{\\hbar k^2}{2m} t}$."
            },
            {
              "stepName": "Step 2: Inverse Fourier Transform at time t",
              "math": "\\psi(x,t) = \\frac{1}{\\sqrt{2\\pi}} \\int_{-\\infty}^{+\\infty} \\phi(k) e^{i(kx - \\omega_k t)} dk = \\frac{(2\\sigma_0^2 / \\pi)^{1/4}}{\\sqrt{2\\sigma_0^2 + i \\frac{\\hbar t}{m}}} \\exp\\left( -\\frac{x^2}{4\\sigma_0^2 + 2i \\frac{\\hbar t}{m}} \\right)\n$$\n$$|\\psi(x,t)|^2 = \\frac{1}{\\sqrt{2\\pi} \\sigma(t)} \\exp\\left( -\\frac{x^2}{2\\sigma(t)^2} \\right), \\quad \\text{where } \\sigma(t) = \\sigma_0 \\sqrt{1 + \\left(\\frac{\\hbar t}{2m\\sigma_0^2}\\right)^2}",
              "explanation": "Because different momentum components travel at different group velocities ($v_g = \\hbar k / m$), the wave packet broadens over time. This dispersion is purely quantum mechanical."
            }
          ]
        }
      ]
    },
    {
      "id": "unit-4",
      "number": 4,
      "title": "One-Dimensional Potentials & Quantum Mechanical Tunneling",
      "lectures": 8,
      "leadSummary": "Analytical solutions of piecewise constant potentials: boundary conditions, potential steps (reflection and transmission), the rectangular potential barrier, quantum tunneling ($E < V_0$), the infinite square well (particle in a box), and the finite square well.",
      "simulations": [
        "quantum-tunneling",
        "particle-in-a-box"
      ],
      "sections": [
        {
          "secNumber": "4.1",
          "heading": "Boundary Conditions and Piecewise Constant Potentials",
          "content": "\n#### Standard Boundary Conditions\nFor a one-dimensional Time-Independent Schrödinger Equation:\n\n$$-\\frac{\\hbar^2}{2m} \\frac{d^2\\psi(x)}{dx^2} + V(x)\\psi(x) = E\\psi(x)$$\n\nIntegrating across an infinitesimal interval $[x_0 - \\epsilon, x_0 + \\epsilon]$ centered at a potential boundary $x_0$:\n\n$$-\\frac{\\hbar^2}{2m} \\left[ \\left.\\frac{d\\psi}{dx}\\right|_{x_0+\\epsilon} - \\left.\\frac{d\\psi}{dx}\\right|_{x_0-\\epsilon} \\right] + \\lim_{\\epsilon \\to 0} \\int_{x_0-\\epsilon}^{x_0+\\epsilon} V(x)\\psi(x) dx = E \\lim_{\\epsilon \\to 0} \\int_{x_0-\\epsilon}^{x_0+\\epsilon} \\psi(x) dx$$\n\nFrom this integration, two general boundary conditions emerge:\n1. **Continuity of the Wavefunction:** $\\psi(x)$ must be continuous everywhere:\n$$\\psi(x_0^-) = \\psi(x_0^+)$$\n2. **Continuity of the Derivative:** Provided $V(x)$ does not contain infinite Dirac delta spikes, $\\frac{d\\psi}{dx}$ must be continuous:\n$$\\left.\\frac{d\\psi}{dx}\\right|_{x_0^-} = \\left.\\frac{d\\psi}{dx}\\right|_{x_0^+}$$\n          ",
          "simulation": "finite-square-well-sim"
        },
        {
          "secNumber": "4.2",
          "heading": "The Potential Step",
          "content": "\nConsider a potential step defined by:\n\n$$V(x) = \\begin{cases} 0 & \\text{for } x < 0 \\quad (\\text{Region I}) \\\\ V_0 & \\text{for } x \\ge 0 \\quad (\\text{Region II}) \\end{cases}$$\n\nA stream of particles of mass $m$ and energy $E$ is incident from the left ($x \\to -\\infty$).\n\n#### Case 1: $E > V_0$\nIn Region I ($x < 0$): $\\psi_I(x) = A e^{i k_1 x} + B e^{-i k_1 x}$, where $k_1 = \\frac{\\sqrt{2mE}}{\\hbar}$.\nIn Region II ($x > 0$): $\\psi_{II}(x) = C e^{i k_2 x}$, where $k_2 = \\frac{\\sqrt{2m(E - V_0)}}{\\hbar}$.\n\nApplying boundary conditions at $x = 0$:\n1. $\\psi_I(0) = \\psi_{II}(0) \\implies A + B = C$\n2. $\\psi'_I(0) = \\psi'_{II}(0) \\implies i k_1 (A - B) = i k_2 C \\implies A - B = \\frac{k_2}{k_1} C$\n\nSolving for reflection amplitude $B/A$ and transmission amplitude $C/A$:\n\n$$\\frac{B}{A} = \\frac{k_1 - k_2}{k_1 + k_2}, \\qquad \\frac{C}{A} = \\frac{2 k_1}{k_1 + k_2}$$\n\nThe **Reflection Coefficient** $R$ and **Transmission Coefficient** $T$ are ratios of probability currents:\n\n$$R = \\frac{|J_{\\text{refl}}|}{|J_{\\text{inc}}|} = \\left| \\frac{B}{A} \\right|^2 = \\left( \\frac{k_1 - k_2}{k_1 + k_2} \\right)^2$$\n\n$$T = \\frac{|J_{\\text{trans}}|}{|J_{\\text{inc}}|} = \\frac{k_2}{k_1} \\left| \\frac{C}{A} \\right|^2 = \\frac{4 k_1 k_2}{(k_1 + k_2)^2}$$\n\nSumming these yields probability conservation: $R + T = 1$. Even when $E > V_0$, quantum mechanics predicts non-zero reflection ($R > 0$), a purely wave phenomenon with no classical counterpart.\n\n#### Case 2: $E < V_0$\nIn Region II, the wave vector becomes imaginary: $k_2 = i \\kappa$, where $\\kappa = \\frac{\\sqrt{2m(V_0 - E)}}{\\hbar}$.\nThe physically acceptable solution in Region II is an exponentially decaying wave:\n\n$$\\psi_{II}(x) = C e^{-\\kappa x}$$\n\nApplying boundary conditions yields $R = |\\frac{k_1 - i\\kappa}{k_1 + i\\kappa}|^2 = 1$ and $T = 0$.\nAll particles are eventually reflected ($R = 1$), but the wavefunction penetrates a finite distance $\\delta = 1/\\kappa$ into the classically forbidden region. This penetration leads directly to quantum tunneling in finite barriers.\n          ",
          "simulation": "quantum-tunneling"
        },
        {
          "secNumber": "4.3",
          "heading": "The Rectangular Potential Barrier and Quantum Tunneling",
          "content": "\nConsider a barrier of height $V_0$ and width $a$:\n\n$$V(x) = \\begin{cases} 0 & x < 0 \\quad (\\text{Region I}) \\\\ V_0 & 0 \\le x \\le a \\quad (\\text{Region II}) \\\\ 0 & x > a \\quad (\\text{Region III}) \\end{cases}$$\n\nFor $E < V_0$:\n* Region I ($x < 0$): $\\psi_I(x) = A e^{i k x} + B e^{-i k x}$, with $k = \\frac{\\sqrt{2mE}}{\\hbar}$\n* Region II ($0 \\le x \\le a$): $\\psi_{II}(x) = F e^{\\kappa x} + G e^{-\\kappa x}$, with $\\kappa = \\frac{\\sqrt{2m(V_0 - E)}}{\\hbar}$\n* Region III ($x > a$): $\\psi_{III}(x) = C e^{i k x}$\n\nMatching $\\psi$ and $\\frac{d\\psi}{dx}$ at $x = 0$ and $x = a$ yields the exact **Transmission Coefficient Formula**:\n\n$$T = \\left[ 1 + \\frac{V_0^2}{4E(V_0 - E)} \\sinh^2(\\kappa a) \\right]^{-1}$$\n\nWhen the barrier is wide and high ($\\kappa a \\gg 1$), $\\sinh(\\kappa a) \\approx \\frac{1}{2} e^{\\kappa a}$, simplifying $T$ to:\n\n$$T \\approx 16 \\frac{E}{V_0} \\left( 1 - \\frac{E}{V_0} \\right) e^{-2\\kappa a}$$\n\n#### Physical Applications of Quantum Tunneling\n1. **Alpha Decay in Nuclear Physics:** Gamow (1928) explained the Geiger-Nuttall law by modeling the alpha particle as tunneling through the nuclear Coulomb barrier.\n2. **Scanning Tunneling Microscopy (STM):** Binnig and Rohrer (Nobel Prize 1986) developed the STM, which relies on tunneling current between an atomic tip and sample surface: $I \\propto e^{-2\\kappa d}$, yielding sub-angstrom spatial resolution.\n\nExperiment with barrier height and width in **Simulation 4.1** below to observe real-time evanescent decay and transmission.\n          ",
          "simulation": "particle-in-a-box"
        },
        {
          "secNumber": "4.4",
          "heading": "The Infinite Square Well (Particle in a Box)",
          "content": "\nConsider a particle trapped in an infinite potential well:\n\n$$V(x) = \\begin{cases} 0 & 0 \\le x \\le L \\\\ \\infty & \\text{otherwise} \\end{cases}$$\n\nBecause $V = \\infty$ outside the well, $\\psi(x) = 0$ for $x \\le 0$ and $x \\ge L$. Inside the well ($0 < x < L$):\n\n$$\\frac{d^2\\psi}{dx^2} + k^2\\psi = 0, \\quad k = \\frac{\\sqrt{2mE}}{\\hbar} \\implies \\psi(x) = A \\sin(kx) + B \\cos(kx)$$\n\nApplying boundary conditions:\n1. $\\psi(0) = 0 \\implies B = 0$\n2. $\\psi(L) = 0 \\implies A \\sin(kL) = 0 \\implies kL = n\\pi, \\quad n \\in \\{1, 2, 3, \\dots\\}$\n\nThis gives the quantized wave numbers $k_n$ and **Quantized Energy Levels**:\n\n$$E_n = \\frac{\\hbar^2 k_n^2}{2m} = \\frac{n^2 \\pi^2 \\hbar^2}{2mL^2} = \\frac{n^2 h^2}{8mL^2}$$\n\nNormalizing $\\int_0^L |\\psi_n(x)|^2 dx = 1$ yields:\n\n$$\\psi_n(x) = \\sqrt{\\frac{2}{L}} \\sin\\left( \\frac{n\\pi x}{L} \\right)$$\n\nKey properties:\n* **Zero-Point Energy:** The ground state ($n=1$) energy $E_1 = \\frac{\\pi^2 \\hbar^2}{2mL^2} > 0$ is strictly positive, satisfying the uncertainty principle $\\Delta p \\approx \\hbar / L$.\n* **Nodes:** The state $\\psi_n(x)$ has $n-1$ interior nodes where the probability density vanishes identically.\n\nSee **Simulation 4.2** below to interact with quantum numbers $n=1$ to $5$ and view standing wavefunctions alongside their energy ladder.\n          "
        }
      ],
      "problems": [
        {
          "id": "p4-1",
          "difficulty": "Medium",
          "title": "Symmetric Finite Square Well: Bound State Transcendental Equations",
          "question": "For a symmetric finite potential well $V(x) = -V_0$ for $|x| \\le a$ and $V(x) = 0$ for $|x| > a$, derive the transcendental equations for the bound-state energy eigenvalues for even-parity states. Prove that at least one even bound state exists regardless of how shallow the well is.",
          "steps": [
            {
              "stepName": "Step 1: Set up wavefunctions by parity",
              "math": "\\text{For } |x| \\le a: \\psi(x) = A \\cos(l x), \\quad l = \\frac{\\sqrt{2m(E + V_0)}}{\\hbar}\n$$\n$$\\text{For } x > a: \\psi(x) = C e^{-\\kappa x}, \\quad \\kappa = \\frac{\\sqrt{-2mE}}{\\hbar}",
              "explanation": "For an even parity potential $V(-x) = V(x)$, the eigenstates can be categorized into even and odd functions. Even bound states use cosine inside the well."
            },
            {
              "stepName": "Step 2: Match boundary conditions at x = a",
              "math": "\\psi(a^-) = \\psi(a^+) \\implies A \\cos(l a) = C e^{-\\kappa a}\n$$\n$$\\psi'(a^-) = \\psi'(a^+) \\implies -l A \\sin(l a) = -\\kappa C e^{-\\kappa a}\n$$\n$$\\frac{\\psi'(a)}{\\psi(a)} \\implies l \\tan(l a) = \\kappa",
              "explanation": "Defining dimensionless variables $\\xi = l a$ and $\\eta = \\kappa a$, this becomes $\\xi \\tan\\xi = \\eta$ subject to the circle constraint $\\xi^2 + \\eta^2 = \\frac{2m V_0 a^2}{\\hbar^2} = R^2$. Because $\\tan\\xi \\to 0$ as $\\xi \\to 0$, the curve $\\eta = \\xi \\tan\\xi$ always intersects the circle in the first quadrant for any $R > 0$, guaranteeing at least one even bound state."
            }
          ]
        }
      ]
    },
    {
      "id": "unit-5",
      "number": 5,
      "title": "The One-Dimensional Quantum Harmonic Oscillator",
      "lectures": 11,
      "leadSummary": "The quintessential quantum model: the harmonic oscillator potential, analytic series solution using Hermite polynomials, algebraic Dirac ladder operator formalism, zero-point energy, expectation values, and comparison with classical turning points.",
      "simulations": [
        "harmonic-oscillator"
      ],
      "sections": [
        {
          "secNumber": "5.1",
          "heading": "Physical Importance and Analytic Solution",
          "content": "\n#### Universal Significance of the Harmonic Oscillator\nThe harmonic oscillator is a cornerstone of theoretical physics. Any arbitrary potential $V(x)$ with a local stable minimum at $x_0$ can be Taylor-expanded about that minimum:\n\n$$V(x) = V(x_0) + V'(x_0)(x - x_0) + \\frac{1}{2}V''(x_0)(x - x_0)^2 + \\dots$$\n\nSetting $V(x_0) = 0$ as reference, and noting $V'(x_0) = 0$ at equilibrium:\n\n$$V(x) \\approx \\frac{1}{2} k (x - x_0)^2 = \\frac{1}{2} m \\omega^2 x^2$$\n\nwhere $\\omega = \\sqrt{k/m} = \\sqrt{V''(x_0)/m}$. Consequently, any system undergoing small oscillations about stable equilibrium—such as molecular vibrations, phonons in crystal lattices, and electromagnetic field modes—behaves as a harmonic oscillator.\n\n#### Analytic Solution of the Schrödinger Equation\nThe Time-Independent Schrödinger Equation is:\n\n$$-\\frac{\\hbar^2}{2m}\\frac{d^2\\psi}{dx^2} + \\frac{1}{2}m\\omega^2 x^2 \\psi = E\\psi$$\n\nIntroducing the dimensionless coordinate $\\xi$ and energy parameter $\\epsilon$:\n\n$$\\xi = \\alpha x = \\sqrt{\\frac{m\\omega}{\\hbar}} x, \\qquad \\epsilon = \\frac{2E}{\\hbar\\omega}$$\n\nThe equation simplifies to:\n\n$$\\frac{d^2\\psi}{d\\xi^2} + (\\epsilon - \\xi^2)\\psi = 0$$\n\n#### Asymptotic Behavior and Hermite Polynomials\nAs $\\xi \\to \\pm \\infty$, $\\frac{d^2\\psi}{d\\xi^2} \\approx \\xi^2\\psi$, which has normalizable asymptotic solutions $\\psi(\\xi) \\propto e^{-\\xi^2/2}$. We therefore factor out the Gaussian:\n\n$$\\psi(\\xi) = H(\\xi) e^{-\\xi^2/2}$$\n\nSubstituting this into the differential equation yields the **Hermite Differential Equation**:\n\n$$\\frac{d^2 H}{d\\xi^2} - 2\\xi \\frac{dH}{d\\xi} + (\\epsilon - 1)H = 0$$\n\nExpressing $H(\\xi)$ as a power series $H(\\xi) = \\sum_{j=0}^\\infty a_j \\xi^j$, the recurrence relation is:\n\n$$a_{j+2} = \\frac{2j + 1 - \\epsilon}{(j+1)(j+2)} a_j$$\n\nFor the wavefunction to remain normalizable as $\\xi \\to \\infty$, the series must terminate at some finite index $j = n$. Setting the numerator to zero:\n\n$$2n + 1 - \\epsilon = 0 \\implies \\epsilon = 2n + 1$$\n\nSince $\\epsilon = \\frac{2E}{\\hbar\\omega}$, we obtain the **Quantized Energy Eigenvalues**:\n\n$$E_n = \\left( n + \\frac{1}{2} \\right) \\hbar \\omega, \\quad n \\in \\{0, 1, 2, 3, \\dots\\}$$\n\nThe corresponding polynomial solutions $H_n(\\xi)$ are the **Hermite Polynomials**:\n* $H_0(\\xi) = 1$\n* $H_1(\\xi) = 2\\xi$\n* $H_2(\\xi) = 4\\xi^2 - 2$\n* $H_3(\\xi) = 8\\xi^3 - 12\\xi$\n\nThe normalized stationary state wavefunctions are:\n\n$$\\psi_n(x) = \\left( \\frac{m\\omega}{\\pi \\hbar} \\right)^{1/4} \\frac{1}{\\sqrt{2^n n!}} H_n\\left( \\sqrt{\\frac{m\\omega}{\\hbar}} x \\right) e^{-\\frac{m\\omega x^2}{2\\hbar}}$$\n          ",
          "simulation": "harmonic-oscillator"
        },
        {
          "secNumber": "5.2",
          "heading": "The Algebraic Operator Method: Dirac Ladder Operators",
          "content": "\nPaul Dirac introduced a powerful algebraic method using non-Hermitian ladder operators:\n\n$$\\hat{a} = \\sqrt{\\frac{m\\omega}{2\\hbar}} \\left( \\hat{x} + \\frac{i}{m\\omega}\\hat{p} \\right) \\quad (\\text{Annihilation / Lowering Operator})$$\n\n$$\\hat{a}^\\dagger = \\sqrt{\\frac{m\\omega}{2\\hbar}} \\left( \\hat{x} - \\frac{i}{m\\omega}\\hat{p} \\right) \\quad (\\text{Creation / Raising Operator})$$\n\n#### Fundamental Commutation Relations\nUsing $[\\hat{x}, \\hat{p}] = i\\hbar$:\n\n$$[\\hat{a}, \\hat{a}^\\dagger] = \\frac{1}{2\\hbar m\\omega} [m\\omega\\hat{x} + i\\hat{p}, m\\omega\\hat{x} - i\\hat{p}] = \\frac{1}{2\\hbar m\\omega} (-2i m\\omega [\\hat{x}, \\hat{p}]) = 1$$\n\nRewriting the Hamiltonian in terms of ladder operators:\n\n$$\\hat{H} = \\hbar \\omega \\left( \\hat{a}^\\dagger \\hat{a} + \\frac{1}{2} \\right) = \\hbar \\omega \\left( \\hat{N} + \\frac{1}{2} \\right)$$\n\nwhere $\\hat{N} = \\hat{a}^\\dagger \\hat{a}$ is the Hermitian **Number Operator**, with eigenvalues $n \\ge 0$: $\\hat{N}|n\\rangle = n|n\\rangle$.\n\n#### Action on Eigenstates\n$$\\hat{a}|n\\rangle = \\sqrt{n} |n-1\\rangle$$\n$$\\hat{a}^\\dagger|n\\rangle = \\sqrt{n+1} |n+1\\rangle$$\n\nSince lowering the ground state must terminate the ladder: $\\hat{a}|0\\rangle = 0$. In position space:\n\n$$\\sqrt{\\frac{m\\omega}{2\\hbar}} \\left( x + \\frac{\\hbar}{m\\omega}\\frac{d}{dx} \\right)\\psi_0(x) = 0 \\implies \\frac{d\\psi_0}{dx} = -\\frac{m\\omega}{\\hbar} x \\psi_0$$\n\nIntegrating yields the Gaussian ground state: $\\psi_0(x) = (\\frac{m\\omega}{\\pi\\hbar})^{1/4} e^{-\\frac{m\\omega x^2}{2\\hbar}}$.\n\nAny excited state $|n\\rangle$ can then be generated algebraically:\n\n$$|n\\rangle = \\frac{(\\hat{a}^\\dagger)^n}{\\sqrt{n!}} |0\\rangle$$\n\nExplore the energy ladder, Hermite wavefunctions, and classical turning points in **Simulation 5.1** below.\n          "
        }
      ],
      "problems": [
        {
          "id": "p5-1",
          "difficulty": "Hard",
          "title": "Expectation Values <x^2>, <p^2> and the Virial Theorem via Ladder Operators",
          "question": "Using Dirac ladder operators $\\hat{a}$ and $\\hat{a}^\\dagger$, evaluate $\\langle n | \\hat{x}^2 | n \\rangle$ and $\\langle n | \\hat{p}^2 | n \\rangle$ for the $n$-th excited state of a quantum harmonic oscillator. Verify the Virial Theorem: $\\langle T \\rangle = \\langle V \\rangle = \\frac{1}{2} E_n$.",
          "steps": [
            {
              "stepName": "Step 1: Express x and p in terms of ladder operators",
              "math": "\\hat{x} = \\sqrt{\\frac{\\hbar}{2m\\omega}} (\\hat{a} + \\hat{a}^\\dagger), \\qquad \\hat{p} = -i\\sqrt{\\frac{m\\omega\\hbar}{2}} (\\hat{a} - \\hat{a}^\\dagger)\n$$\n$$\\hat{x}^2 = \\frac{\\hbar}{2m\\omega} (\\hat{a}^2 + \\hat{a}\\hat{a}^\\dagger + \\hat{a}^\\dagger\\hat{a} + (\\hat{a}^\\dagger)^2)\n$$\n$$\\hat{p}^2 = -\\frac{m\\omega\\hbar}{2} (\\hat{a}^2 - \\hat{a}\\hat{a}^\\dagger - \\hat{a}^\\dagger\\hat{a} + (\\hat{a}^\\dagger)^2)",
              "explanation": "Terms with $\\hat{a}^2$ and $(\\hat{a}^\\dagger)^2$ change the state by $\\pm 2$, so their diagonal matrix elements vanish: $\\langle n | \\hat{a}^2 | n \\rangle = 0$."
            },
            {
              "stepName": "Step 2: Evaluate expectation values",
              "math": "\\langle n | \\hat{a}\\hat{a}^\\dagger + \\hat{a}^\\dagger\\hat{a} | n \\rangle = (n+1) + n = 2n + 1\n$$\n$$\\langle x^2 \\rangle_n = \\frac{\\hbar}{2m\\omega} (2n + 1) = \\left( n + \\frac{1}{2} \\right) \\frac{\\hbar}{m\\omega}\n$$\n$$\\langle p^2 \\rangle_n = \\frac{m\\omega\\hbar}{2} (2n + 1) = \\left( n + \\frac{1}{2} \\right) m\\omega\\hbar\n$$\n$$\\langle V \\rangle = \\frac{1}{2}m\\omega^2 \\langle x^2 \\rangle = \\frac{1}{2}\\left(n + \\frac{1}{2}\\right)\\hbar\\omega = \\frac{1}{2}E_n\n$$\n$$\\langle T \\rangle = \\frac{\\langle p^2 \\rangle}{2m} = \\frac{1}{2}\\left(n + \\frac{1}{2}\\right)\\hbar\\omega = \\frac{1}{2}E_n",
              "explanation": "This verifies the quantum Virial Theorem: the average kinetic energy equals the average potential energy, each contributing half of the total energy $E_n$."
            }
          ]
        }
      ]
    },
    {
      "id": "unit-6",
      "number": 6,
      "title": "The Hydrogen Atom & Central Force Potentials",
      "lectures": 11,
      "leadSummary": "Three-dimensional quantum mechanics in spherical coordinates: central force reduction, orbital angular momentum algebra and spherical harmonics $Y_l^m(\\theta,\\phi)$, the radial Schrödinger equation, associated Laguerre polynomials, quantum numbers $(n, l, m)$, energy degeneracies, and radial probability distributions.",
      "simulations": [
        "hydrogen-orbitals"
      ],
      "sections": [
        {
          "secNumber": "6.1",
          "heading": "Schrödinger Equation in Spherical Coordinates",
          "content": "\n#### Central Potential and Reduced Mass Reduction\nThe hydrogen atom consists of two interacting particles: a proton ($m_p$, position $\\mathbf{r}_p$) and an electron ($m_e$, position $\\mathbf{r}_e$) interacting via the central Coulomb potential:\n\n$$V(r) = -\\frac{e^2}{4\\pi \\epsilon_0 r}, \\quad r = |\\mathbf{r}_e - \\mathbf{r}_p|$$\n\nTransforming to center-of-mass coordinates $\\mathbf{R}$ and relative coordinates $\\mathbf{r}$, the center-of-mass motion separates into a free particle equation, while the relative motion is described by an effective single-particle equation with **reduced mass** $\\mu$:\n\n$$\\mu = \\frac{m_e m_p}{m_e + m_p} \\approx m_e \\left( 1 - \\frac{m_e}{m_p} \\right) \\approx 0.99945 m_e$$\n\nIn spherical coordinates $(r, \\theta, \\phi)$, where $x = r\\sin\\theta\\cos\\phi$, $y = r\\sin\\theta\\sin\\phi$, $z = r\\cos\\theta$, the Laplacian $\\nabla^2$ is:\n\n$$\\nabla^2 = \\frac{1}{r^2}\\frac{\\partial}{\\partial r}\\left( r^2 \\frac{\\partial}{\\partial r} \\right) + \\frac{1}{r^2 \\sin\\theta}\\frac{\\partial}{\\partial \\theta}\\left( \\sin\\theta \\frac{\\partial}{\\partial \\theta} \\right) + \\frac{1}{r^2 \\sin^2\\theta}\\frac{\\partial^2}{\\partial \\phi^2}$$\n\nThe Time-Independent Schrödinger Equation becomes:\n\n$$-\\frac{\\hbar^2}{2\\mu}\\nabla^2 \\psi(r,\\theta,\\phi) + V(r)\\psi(r,\\theta,\\phi) = E\\psi(r,\\theta,\\phi)$$\n          ",
          "simulation": "hydrogen-orbitals"
        },
        {
          "secNumber": "6.2",
          "heading": "Orbital Angular Momentum and Spherical Harmonics",
          "content": "\n#### Angular Momentum Operators\nClassical angular momentum $\\mathbf{L} = \\mathbf{r} \\times \\mathbf{p}$ translates into quantum mechanical differential operators:\n\n$$\\hat{L}_x = -i\\hbar \\left( y\\frac{\\partial}{\\partial z} - z\\frac{\\partial}{\\partial y} \\right), \\quad \\hat{L}_y = -i\\hbar \\left( z\\frac{\\partial}{\\partial x} - x\\frac{\\partial}{\\partial z} \\right), \\quad \\hat{L}_z = -i\\hbar \\left( x\\frac{\\partial}{\\partial y} - y\\frac{\\partial}{\\partial x} \\right)$$\n\nFundamental commutation relations:\n\n$$[\\hat{L}_x, \\hat{L}_y] = i\\hbar \\hat{L}_z, \\quad [\\hat{L}_y, \\hat{L}_z] = i\\hbar \\hat{L}_x, \\quad [\\hat{L}_z, \\hat{L}_x] = i\\hbar \\hat{L}_y$$\n\nThe total angular momentum operator $\\hat{L}^2 = \\hat{L}_x^2 + \\hat{L}_y^2 + \\hat{L}_z^2$ commutes with each individual component:\n\n$$[\\hat{L}^2, \\hat{L}_z] = 0$$\n\nIn spherical coordinates:\n\n$$\\hat{L}_z = -i\\hbar \\frac{\\partial}{\\partial \\phi}$$\n\n$$\\hat{L}^2 = -\\hbar^2 \\left[ \\frac{1}{\\sin\\theta}\\frac{\\partial}{\\partial \\theta}\\left( \\sin\\theta \\frac{\\partial}{\\partial \\theta} \\right) + \\frac{1}{\\sin^2\\theta}\\frac{\\partial^2}{\\partial \\phi^2} \\right]$$\n\n#### Separation of Variables\nFactoring the wavefunction into radial and angular components:\n\n$$\\psi(r,\\theta,\\phi) = R(r) Y(\\theta,\\phi)$$\n\nThe angular functions $Y_l^m(\\theta,\\phi)$ are the **Spherical Harmonics**, simultaneous eigenfunctions of $\\hat{L}^2$ and $\\hat{L}_z$:\n\n$$\\hat{L}^2 Y_l^m(\\theta,\\phi) = l(l+1)\\hbar^2 Y_l^m(\\theta,\\phi), \\quad l \\in \\{0, 1, 2, \\dots\\}$$\n\n$$\\hat{L}_z Y_l^m(\\theta,\\phi) = m_l \\hbar Y_l^m(\\theta,\\phi), \\quad m_l \\in \\{-l, -l+1, \\dots, +l\\}$$\n\nExplicitly, $Y_l^m(\\theta,\\phi) = \\sqrt{\\frac{(2l+1)}{4\\pi}\\frac{(l-m)!}{(l+m)!}} P_l^m(\\cos\\theta) e^{i m \\phi}$, where $P_l^m$ are Associated Legendre polynomials.\n          ",
          "simulation": "angular-momentum-sim"
        },
        {
          "secNumber": "6.3",
          "heading": "The Radial Equation and Energy Eigenvalues",
          "content": "\nSubstituting the angular eigenvalue $l(l+1)\\hbar^2$ into the full Schrödinger equation leaves the **Radial Differential Equation**:\n\n$$\\frac{1}{r^2}\\frac{d}{dr}\\left( r^2 \\frac{dR}{dr} \\right) + \\frac{2\\mu}{\\hbar^2}\\left[ E - V(r) - \\frac{l(l+1)\\hbar^2}{2\\mu r^2} \\right]R = 0$$\n\nThe effective potential includes an outward **centrifugal barrier**:\n\n$$V_{\\text{eff}}(r) = -\\frac{e^2}{4\\pi \\epsilon_0 r} + \\frac{l(l+1)\\hbar^2}{2\\mu r^2}$$\n\n#### Bound State Solutions ($E < 0$) and Quantized Energies\nSolving the radial equation via power series around $r=0$ and extracting the asymptotic behavior at $r \\to \\infty$ yields solutions in terms of **Associated Laguerre Polynomials** $L_{n-l-1}^{2l+1}$:\n\n$$R_{nl}(r) = -\\sqrt{\\left(\\frac{2}{n a_0}\\right)^3 \\frac{(n-l-1)!}{2n[(n+l)!]^3}} e^{-r/n a_0} \\left( \\frac{2r}{n a_0} \\right)^l L_{n-l-1}^{2l+1}\\left( \\frac{2r}{n a_0} \\right)$$\n\nThe solutions are normalizable if and only if the principal quantum number $n$ satisfies:\n\n$$n = 1, 2, 3, \\dots \\qquad \\text{with } l \\in \\{0, 1, 2, \\dots, n-1\\}$$\n\nThis gives the **Bohr Energy Levels**:\n\n$$E_n = -\\frac{\\mu e^4}{32 \\pi^2 \\epsilon_0^2 \\hbar^2} \\frac{1}{n^2} = -\\frac{13.6 \\text{ eV}}{n^2}$$\n\n#### Degeneracy\nThe energy depends exclusively on $n$. For a given $n$:\n* $l$ ranges from $0$ to $n-1$ ($n$ distinct orbital angular momenta).\n* For each $l$, $m_l$ ranges from $-l$ to $+l$ ($2l+1$ values).\n\nTotal orbital degeneracy:\n\n$$g_n = \\sum_{l=0}^{n-1} (2l+1) = n^2$$\n\nIncluding the two electron spin states ($m_s = \\pm 1/2$), the total degeneracy is $2n^2$.\n\n#### Radial Probability Density $P(r)$\nThe probability of finding the electron between radius $r$ and $r+dr$ integrated over all angles is:\n\n$$P(r) dr = r^2 |R_{nl}(r)|^2 dr$$\n\nFor the ground state ($1s$: $n=1, l=0$):\n\n$$R_{10}(r) = \\frac{2}{a_0^{3/2}} e^{-r/a_0} \\implies P(r) = \\frac{4}{a_0^3} r^2 e^{-2r/a_0}$$\n\nThe maximum of $P(r)$ occurs at $\\frac{dP}{dr} = 0 \\implies r_{\\text{max}} = a_0 = 0.529 \\text{ Å}$, matching the Bohr radius.\n\nSee **Simulation 6.1** below to visualize radial distribution curves $P(r)$ and 2D quantum electron cloud slices for $1s, 2s, 2p,$ and $3d$ orbitals.\n          ",
          "simulation": "zeeman-effect-sim"
        }
      ],
      "problems": [
        {
          "id": "p6-1",
          "difficulty": "Hard",
          "title": "Expectation Values <r> and <1/r> for Hydrogen Ground State",
          "question": "Using the normalized hydrogen ground-state wavefunction $\\psi_{100}(r) = \\frac{1}{\\sqrt{\\pi a_0^3}} e^{-r/a_0}$, calculate:\\n(a) The expectation value of the electron-nuclear distance $\\langle r \\rangle$.\\n(b) The expectation value $\\langle 1/r \\rangle$.\\n(c) The average potential energy $\\langle V \\rangle$ and kinetic energy $\\langle T \\rangle$, verifying the quantum Virial theorem for Coulomb potentials ($2\\langle T \\rangle + \\langle V \\rangle = 0$).",
          "steps": [
            {
              "stepName": "Step 1: Calculate <r> and <1/r>",
              "math": "\\langle r \\rangle = \\int_0^\\infty r P(r) dr = \\frac{4}{a_0^3} \\int_0^\\infty r^3 e^{-2r/a_0} dr\n$$\n$$\\text{Using } \\int_0^\\infty x^n e^{-a x} dx = \\frac{n!}{a^{n+1}} \\implies \\langle r \\rangle = \\frac{4}{a_0^3} \\frac{3!}{(2/a_0)^4} = \\frac{4 \\times 6}{16} a_0 = \\frac{3}{2} a_0\n$$\n$$\\langle 1/r \\rangle = \\frac{4}{a_0^3} \\int_0^\\infty r e^{-2r/a_0} dr = \\frac{4}{a_0^3} \\frac{1!}{(2/a_0)^2} = \\frac{1}{a_0}",
              "explanation": "Notice that $\\langle r \\rangle = 1.5 a_0$, whereas the most probable distance is $r_{\\text{mp}} = a_0$. The radial probability distribution has a long exponential tail extending outward."
            },
            {
              "stepName": "Step 2: Verify the Coulomb Virial Theorem",
              "math": "\\langle V \\rangle = -\\frac{e^2}{4\\pi \\epsilon_0} \\left\\langle \\frac{1}{r} \\right\\rangle = -\\frac{e^2}{4\\pi \\epsilon_0 a_0} = 2 E_1 = -27.2 \\text{ eV}\n$$\n$$\\langle T \\rangle = E_1 - \\langle V \\rangle = -13.6 \\text{ eV} - (-27.2 \\text{ eV}) = +13.6 \\text{ eV} = -E_1\n$$\n$$2\\langle T \\rangle + \\langle V \\rangle = 2(+13.6) + (-27.2) = 0",
              "explanation": "For any homogeneous potential of degree $k$ ($V \\propto r^k$), the Virial theorem states $2\\langle T \\rangle = k\\langle V \\rangle$. For the Coulomb potential, $k = -1$, yielding $2\\langle T \\rangle = -\\langle V \\rangle$, exactly confirmed."
            }
          ]
        }
      ]
    }
  ]
};

