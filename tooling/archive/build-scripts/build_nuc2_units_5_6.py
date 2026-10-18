import json

u5_data = {
    "title": "Nuclear Structure Models: Advanced Shell Model & Collective Dynamics",
    "subtitle": "Spin-Orbit Splitting, Magic Numbers, Schmidt Limits, Nilsson Model & Rotational Bands",
    "summary": "Microscopic and collective nuclear structure: degenerate Fermi gas model, 3D isotropic harmonic oscillator and Woods-Saxon central potentials, Maria Goeppert Mayer and J. Hans D. Jensen strong inverted spin-orbit coupling V_{so}(r) L·S, complete derivation of the nuclear magic numbers (2, 8, 20, 28, 50, 82, 126), single-particle state predictions for odd-A and odd-odd nuclei (Nordheim rules), nuclear magnetic moments and Schmidt limits, collective Bohr-Mottelson quadrupole/octupole vibrations, deformed Nilsson mean field [N n_z Λ]Ω^π, rotational bands with characteristic E(4⁺)/E(2⁺) ≈ 3.33 energy ratios, and high-spin Coriolis backbending.",
    "sections": [
        {
            "id": "sec-5-1",
            "title": "Nuclear Mean Field & The Degenerate Fermi Gas Model",
            "content": r"""
<h3>1. The Independent Particle Mean Field Approximation</h3>
<p>
Although the bare nucleon-nucleon interaction contains strong repulsive cores and tensor components, inside a many-nucleon nucleus each nucleon moves predominantly in an average, smooth, spherically symmetric <strong>mean-field potential</strong> $V_{\text{MF}}(\vec{r})$ created by the collective action of all other $A-1$ nucleons:
</p>
$$\hat{H} = \sum_{i=1}^A \left[ -\frac{\hbar^2}{2M}\nabla_i^2 + V_{\text{MF}}(\vec{r}_i) \right] + \hat{V}_{\text{residual}}$$
<p>
This independent-particle motion is made possible by the <strong>Pauli exclusion principle</strong>: when two nucleons collide inside a nucleus, the states into which they could scatter are already occupied by other nucleons, suppressing short-range collisions and imparting nucleons with long mean free paths ($\lambda_{\text{mfp}} \gg R$).
</p>

<h3>2. The Degenerate Nuclear Fermi Gas Model</h3>
<p>
As the simplest microscopic mean-field model, consider protons and neutrons as two independent, non-interacting ideal Fermi gases confined within a spherical nuclear volume $V = \frac{4}{3}\pi R^3 = \frac{4}{3}\pi R_0^3 A$ of constant density $\rho_0 \approx 0.16\text{ fm}^{-3}$.
</p>
<p>
Each nucleon state occupies a phase space volume of $h^3 = (2\pi\hbar)^3$. For $Z$ protons and $N$ neutrons with spin degeneracy $g = 2$:
</p>
$$N = 2 \frac{V}{(2\pi)^3} \int_0^{k_{F,n}} 4\pi k^2 dk = \frac{V}{\pi^2} \frac{k_{F,n}^3}{3} \implies k_{F,n} = \left( 3\pi^2 \rho_n \right)^{1/3}$$
$$Z = 2 \frac{V}{(2\pi)^3} \int_0^{k_{F,p}} 4\pi k^2 dk = \frac{V}{\pi^2} \frac{k_{F,p}^3}{3} \implies k_{F,p} = \left( 3\pi^2 \rho_p \right)^{1/3}$$
<p>
For a symmetric nucleus with $N = Z = A/2$ and $\rho_n = \rho_p = \rho_0 / 2 \approx 0.08\text{ fm}^{-3}$:
</p>
$$k_F = \left( 3\pi^2 \frac{\rho_0}{2} \right)^{1/3} = \left( \frac{3\pi^2}{2} \times 0.16 \right)^{1/3} = (2.3687)^{1/3} \approx 1.33\text{ to }1.36\text{ fm}^{-1}$$
<p>
The maximum kinetic energy at absolute zero is the <strong>Fermi Energy</strong> $E_F$:
</p>
$$E_F = \frac{\hbar^2 k_F^2}{2 M} = \frac{(197.3\text{ MeV}\cdot\text{fm})^2 (1.36\text{ fm}^{-1})^2}{2(938.9\text{ MeV})} = \frac{38938 \times 1.8496}{1877.8} \approx 38.35\text{ MeV}$$
<p>
Because nucleons are bound by an average separation energy $B/A \approx 8\text{ MeV}$, the total potential well depth $V_0$ must be:
</p>
$$V_0 = E_F + B \approx 38\text{ MeV} + 8\text{ MeV} \approx 46\text{ MeV}$$
<p>
The average kinetic energy per nucleon is $\langle E_k \rangle = \frac{3}{5} E_F \approx 23\text{ MeV}$.
</p>
"""
        },
        {
            "id": "sec-5-2",
            "title": "Central Potentials: 3D Harmonic Oscillator vs Woods-Saxon Diffuse Well",
            "content": r"""
<h3>1. The 3D Isotropic Harmonic Oscillator Potential</h3>
<p>
An analytically solvable model for the nuclear mean field is the 3D harmonic oscillator:
</p>
$$V_{\text{HO}}(r) = -V_0 + \frac{1}{2} M \omega^2 r^2$$
<p>
The energy eigenvalues are governed by the principal oscillator quantum number $N_{\text{osc}} = 2(n - 1) + l = 0, 1, 2, 3, \dots$:
</p>
$$E_N = \left( N_{\text{osc}} + \frac{3}{2} \right) \hbar\omega$$
<p>
where the standard empirical oscillator frequency scales with mass number as $\hbar\omega \approx 41 A^{-1/3}\text{ MeV}$.
</p>
<p>
The degeneracies of the harmonic oscillator shells are:
</p>
<ul>
  <li>$N_{\text{osc}} = 0$: $1s$ (Degeneracy $2$) $\implies$ Cumulative: **2**</li>
  <li>$N_{\text{osc}} = 1$: $1p$ (Degeneracy $6$) $\implies$ Cumulative: **8**</li>
  <li>$N_{\text{osc}} = 2$: $1d, 2s$ (Degeneracy $10 + 2 = 12$) $\implies$ Cumulative: **20**</li>
  <li>$N_{\text{osc}} = 3$: $1f, 2p$ (Degeneracy $14 + 6 = 20$) $\implies$ Cumulative: **40** (Not 28!)</li>
  <li>$N_{\text{osc}} = 4$: $1g, 2d, 3s$ (Degeneracy $18 + 10 + 2 = 30$) $\implies$ Cumulative: **70** (Not 50!)</li>
</ul>
<p>
The harmonic oscillator correctly predicts the first three magic numbers ($2, 8, 20$), but completely fails to explain the higher magic numbers ($28, 50, 82, 126$).
</p>

<h3>2. The Realistic Woods-Saxon Potential</h3>
<p>
In real nuclei, the nuclear density is constant in the interior and drops smoothly to zero at the surface over a skin thickness $t \approx 2.4\text{ fm}$. This is modeled by the <strong>Woods-Saxon potential</strong>:
</p>
$$V_{\text{WS}}(r) = -\frac{V_0}{1 + \exp\left( \frac{r - R}{a} \right)}$$
<p>
where $V_0 \approx 50\text{ MeV}$, $R = R_0 A^{1/3} \approx 1.25 A^{1/3}\text{ fm}$, and diffuseness $a \approx 0.65\text{ fm}$.
</p>
<p>
Because the Woods-Saxon potential is flatter at the center and steeper at the surface than a parabola, it lifts the $l$-degeneracy: states with higher orbital angular momentum $l$ have wavefunctions concentrated closer to the surface and are pulled downward in energy relative to lower-$l$ states. However, even with this flattening, the magic numbers beyond 20 cannot be explained without spin-orbit coupling.
</p>
"""
        },
        {
            "id": "sec-5-3",
            "title": "Mayer-Jensen Strong Spin-Orbit Coupling & Nuclear Magic Numbers",
            "content": r"""
<h3>1. The Inverted Nuclear Spin-Orbit Interaction</h3>
<p>
In 1949, Maria Goeppert Mayer and independently J. Hans D. Jensen (Nobel Prize 1963) solved the mystery of the magic numbers by introducing a powerful, relativistic <strong>spin-orbit potential</strong> into the nuclear mean field:
</p>
$$V(r) = V_{\text{WS}}(r) + V_{so}(r) \vec{l}\cdot\vec{s}$$
<p>
where $V_{so}(r) = -V_{so}^{(0)} \frac{1}{r}\frac{dV_{\text{WS}}}{dr}$ is concentrated entirely at the nuclear surface.
</p>
<p>
Evaluating the operator $\vec{l}\cdot\vec{s}$ from total single-particle angular momentum $\vec{j} = \vec{l} + \vec{s}$:
</p>
$$\vec{j}^2 = \vec{l}^2 + \vec{s}^2 + 2\vec{l}\cdot\vec{s} \implies \vec{l}\cdot\vec{s} = \frac{1}{2}\left[ j(j+1) - l(l+1) - s(s+1) \right]$$
<p>
For nucleon spin $s = 1/2$, the allowed total angular momenta are $j = l + 1/2$ and $j = l - 1/2$:
</p>
$$\langle \vec{l}\cdot\vec{s} \rangle = \begin{cases} +\frac{1}{2} l, & j = l + 1/2 \text{ (spin parallel to orbit)} \\ -\frac{1}{2}(l + 1), & j = l - 1/2 \text{ (spin antiparallel to orbit)} \end{cases}$$
<p>
The energy splitting between the two members of the spin-orbit doublet is:
</p>
$$\Delta E_{so} = E(j = l - 1/2) - E(j = l + 1/2) = \frac{2l + 1}{2} \langle V_{so} \rangle$$
<p>
<strong>CRITICAL PHYSICAL DISTINCTION FROM ATOMIC PHYSICS:</strong>
In atomic physics, spin-orbit coupling is positive ($+\vec{L}\cdot\vec{S}$), placing $j = l - 1/2$ lower in energy. In nuclear physics, the spin-orbit interaction is <strong>strongly attractive and negative</strong>: the state with <strong>$j = l + 1/2$ is pushed dramatically DOWNWARD in energy</strong>.
</p>

<h3>2. The Exact Generation of the Magic Numbers</h3>
<p>
Because $\Delta E_{so} \propto (2l + 1)$, the splitting grows enormously with orbital angular momentum $l$:
</p>
<ul>
  <li>In the $N_{\text{osc}} = 3$ shell ($1f, 2p$), the $1f_{7/2}$ state ($j = 3 + 1/2$) is pushed downward so strongly that it detaches from the shell and joins the lower shell. With its capacity of $2j + 1 = 8$ nucleons, adding it to $20$ produces the magic number:
  $$\mathbf{20 + 8 = 28}$$</li>
  <li>In the $N_{\text{osc}} = 4$ shell, the intruder state $1g_{9/2}$ ($2j + 1 = 10$) plunges downward across the major shell gap. Adding it to $40$ yields:
  $$\mathbf{40 + 10 = 50}$$</li>
  <li>In the $N_{\text{osc}} = 5$ shell, the intruder state $1h_{11/2}$ ($2j + 1 = 12$) plunges downward. Adding it to $70$ yields:
  $$\mathbf{70 + 12 = 82}$$</li>
  <li>In the $N_{\text{osc}} = 6$ shell, the intruder state $1i_{13/2}$ ($2j + 1 = 14$) plunges downward. Adding it to $112$ yields:
  $$\mathbf{112 + 14 = 126}$$</li>
</ul>
<p>
The complete sequence of nuclear magic numbers is rigorously explained:
</p>
$$\mathbf{2, \quad 8, \quad 20, \quad 28, \quad 50, \quad 82, \quad 126}$$
<p>
Nuclei with both $Z$ and $N$ equal to magic numbers (${}^4_2\text{He}_2$, ${}^{16}_8\text{O}_8$, ${}^{40}_{20}\text{Ca}_{20}$, ${}^{48}_{20}\text{Ca}_{28}$, ${}^{208}_{82}\text{Pb}_{126}$) are <strong>doubly magic</strong>, exhibiting exceptional stability, spherical symmetry, high excitation thresholds, and tiny neutron capture cross sections.
</p>
""",
            "simulation": "nuc2-shell-model-spin-orbit-sim"
        },
        {
            "id": "sec-5-4",
            "title": "Single-Particle Shell Predictions: Spins, Parities & Nordheim's Rules",
            "content": r"""
<h3>1. Ground-State Spin and Parity for Even-Even and Odd-A Nuclei</h3>
<p>
The Extreme Single-Particle Shell Model (ESPM) provides robust rules for determining ground-state spins and parities $J^\pi$:
</p>
<ol>
  <li><strong>Even-Even Nuclei ($Z$ even, $N$ even):</strong> All protons pair up in time-reversed orbits with opposite magnetic quantum numbers ($|j, m\rangle$ and $|j, -m\rangle$), and all neutrons pair up identically. The net spin and parity for all even-even ground states without exception is:
  $$J^\pi = 0^+$$</li>
  <li><strong>Odd-$A$ Nuclei ($Z$ odd, $N$ even or $Z$ even, $N$ odd):</strong> All even nucleons pair off to $J = 0^+$. The total spin and parity of the nucleus are determined entirely by the <strong>single unpaired valence nucleon</strong> occupying the state $n l_j$:
  $$J = j_{\text{val}}, \qquad \pi = (-1)^{l_{\text{val}}}$$
  <em>Examples:</em>
  <ul>
    <li>${}^{17}_8\text{O}_9$: $Z=8$ is magic; $N=9$ has one valence neutron in $1d_{5/2}$ ($l=2$). Predicts $J^\pi = 5/2^+$. (Experiment: $5/2^+$).</li>
    <li>${}^{41}_{20}\text{Ca}_{21}$: $Z=20$ is magic; $N=21$ has one valence neutron in $1f_{7/2}$ ($l=3$). Predicts $J^\pi = 7/2^-$. (Experiment: $7/2^-$).</li>
    <li>${}^{207}_{82}\text{Pb}_{125}$: $Z=82$ is magic; $N=125$ has a single neutron hole in $3p_{1/2}$ ($l=1$). Predicts $J^\pi = 1/2^-$. (Experiment: $1/2^-$).</li>
  </ul>
  </li>
</ol>

<h3>2. Odd-Odd Nuclei & Nordheim's Coupling Rules</h3>
<p>
For nuclei with both $Z$ odd and $N$ odd, the spin arises from the vector coupling of the unpaired proton $(j_p, l_p)$ and unpaired neutron $(j_n, l_n)$:
</p>
$$|j_p - j_n| \le J \le j_p + j_n, \qquad \pi = (-1)^{l_p + l_n}$$
<p>
The precise value of $J$ is predicted by <strong>Nordheim's empirical coupling rules</strong>, governed by the Nordheim number $\mathcal{N} \equiv (j_p - l_p) + (j_n - l_n)$:
</p>
<ul>
  <li><strong>Strong Rule ($\mathcal{N} = 0$, intrinsic spins parallel):</strong>
  $$J = |j_p - j_n|$$
  <em>Example:</em> ${}^{38}_{17}\text{Cl}_{21}$: Proton hole in $1d_{3/2}$ ($j_p = 3/2, l_p = 2 \implies j_p - l_p = -1/2$). Valence neutron in $1f_{7/2}$ ($j_n = 7/2, l_n = 3 \implies j_n - l_n = +1/2$). Here $\mathcal{N} = -1/2 + 1/2 = 0$. Predicts $J = |3/2 - 7/2| = 2$. Parity $\pi = (-1)^{2+3} = -1$. Predicts $J^\pi = 2^-$. (Experiment: $2^-$).</li>
  <li><strong>Weak Rule ($\mathcal{N} = \pm 1$, intrinsic spins antiparallel):</strong>
  $$J \text{ is intermediate: tends toward } |j_p + j_n| \text{ or } |j_p - j_n|$$</li>
</ul>
"""
        },
        {
            "id": "sec-5-5",
            "title": "Nuclear Magnetic Moments, Schmidt Limits & Core Polarization",
            "content": r"""
<h3>1. Derivation of the Schmidt Single-Particle Magnetic Moments</h3>
<p>
In the extreme single-particle model of an odd-$A$ nucleus, the total magnetic dipole moment is generated entirely by the single valence nucleon with orbital angular momentum $\vec{l}$ and spin $\vec{s}$:
</p>
$$\vec{\mu} = \left( g_l \vec{l} + g_s \vec{s} \right) \mu_N$$
<p>
Projecting along the total angular momentum $\vec{j} = \vec{l} + \vec{s}$ in the state $m_j = j$:
</p>
$$\mu = \langle j, m_j=j | \mu_z | j, m_j=j \rangle = \frac{\langle \vec{\mu}\cdot\vec{j} \rangle}{j+1}$$
<p>
Evaluating $\vec{l}\cdot\vec{j} = \frac{j(j+1) + l(l+1) - 3/4}{2}$ and $\vec{s}\cdot\vec{j} = \frac{j(j+1) - l(l+1) + 3/4}{2}$:
</p>
<ul>
  <li><strong>Case I: $j = l + 1/2$ (Spin Parallel to Orbit):</strong>
  $$\mu = \left[ (j - 1/2) g_l + \frac{1}{2} g_s \right] \mu_N$$</li>
  <li><strong>Case II: $j = l - 1/2$ (Spin Antiparallel to Orbit):</strong>
  $$\mu = \frac{j}{j+1} \left[ (j + 3/2) g_l - \frac{1}{2} g_s \right] \mu_N$$</li>
</ul>
<p>
Substituting bare nucleon $g$-factors ($g_l = 1, g_s = +5.586$ for proton; $g_l = 0, g_s = -3.826$ for neutron) yields the four classic <strong>Schmidt lines</strong>:
</p>
$$\text{Odd Proton: } \mu = \begin{cases} j + 2.293\text{ }\mu_N, & j = l + 1/2 \\ j - 2.293\frac{j}{j+1}\text{ }\mu_N, & j = l - 1/2 \end{cases}$$
$$\text{Odd Neutron: } \mu = \begin{cases} -1.913\text{ }\mu_N, & j = l + 1/2 \\ +1.913\frac{j}{j+1}\text{ }\mu_N, & j = l - 1/2 \end{cases}$$

<h3>2. The Schmidt Plots & Core Polarization Quenching</h3>
<p>
When experimental magnetic moments are plotted as a function of nuclear spin $j$ (the <strong>Schmidt plots</strong>), almost all experimental points lie <em>between</em> the two Schmidt lines, but rarely right on them.
</p>
<p>
This quenching of empirical magnetic moments is caused by:
</p>
<ol>
  <li><strong>Core Polarization:</strong> The magnetic moment of the valence nucleon polarizes the time-reversed nucleon pairs in the closed core via the residual spin-spin and tensor interactions, inducing an opposing core magnetic moment.</li>
  <li><strong>Meson Exchange Currents:</strong> Virtual charged pions in flight between nucleons alter the effective $g$-factors inside the nuclear medium ($g_s^{\text{eff}} \approx 0.7\text{ to }0.8\text{ }g_s^{\text{bare}}$).</li>
</ol>
"""
        },
        {
            "id": "sec-5-6",
            "title": "Collective Liquid Drop Vibrations & The Phonon Spectrum",
            "content": r"""
<h3>1. Multipole Expansion of the Nuclear Surface</h3>
<p>
Near closed shells, nuclei are spherical in their ground states, but can undergo collective surface vibrations described by the Bohr-Mottelson collective model. The instantaneous nuclear radius in direction $(\theta, \phi)$ is expanded in spherical harmonics:
</p>
$$R(\theta, \phi, t) = R_0 \left[ 1 + \sum_{\lambda=0}^\infty \sum_{\mu=-\lambda}^\lambda \alpha_{\lambda\mu}(t) Y_{\lambda\mu}^*(\theta, \phi) \right]$$
<p>
Physical modes of oscillation:
</p>
<ul>
  <li>$\lambda = 0$ (Monopole / Breathing Mode): Compresses the nuclear fluid, requiring immense symmetry energy ($\hbar\omega \approx 80 A^{-1/3}\text{ MeV}$).</li>
  <li>$\lambda = 1$ (Dipole Mode): Pure center-of-mass translation (no internal excitation for isoscalar motion; for isovector motion, it is the Giant Dipole Resonance).</li>
  <li>$\lambda = 2$ (Quadrupole Mode): Lowest true shape vibration. Deforms sphere into prolate and oblate spheroids with five collective degrees of freedom $\alpha_{2\mu}$.</li>
  <li>$\lambda = 3$ (Octupole Mode): Pear-shaped deformation with negative parity ($J^\pi = 3^-$).</li>
</ul>

<h3>2. The Quadrupole Harmonic Vibrator Spectrum</h3>
<p>
Quantizing the collective Hamiltonian $\hat{H} = \frac{1}{2} B_2 \sum |\dot{\alpha}_{2\mu}|^2 + \frac{1}{2} C_2 \sum |\alpha_{2\mu}|^2$ yields harmonic quadrupole <strong>phonons</strong> carrying angular momentum $\lambda = 2$ and positive parity $\pi = +1$:
</p>
<ol>
  <li><strong>Ground State (Zero Phonons):</strong> $J^\pi = 0^+$.</li>
  <li><strong>One-Phonon State:</strong> A single $2^+$ phonon excitation with energy $\hbar\omega_2 = \hbar\sqrt{C_2/B_2}$:
  $$E(1\text{ phonon}) = \hbar\omega_2, \quad J^\pi = 2^+$$</li>
  <li><strong>Two-Phonon State:</strong> Coupling two identical quadrupole bosons ($l_1 = 2, l_2 = 2$). By Bose-Einstein symmetry for identical phonons, only even total angular momenta are allowed:
  $$J^\pi = 0^+, \quad 2^+, \quad 4^+$$
  In a pure harmonic vibrator, this forms a <strong>degenerate triplet</strong> at exactly twice the single-phonon energy:
  $$E(2\text{ phonons}) = 2\hbar\omega_2, \qquad \frac{E(4^+)}{E(2^+)} = \frac{E(0^+_2)}{E(2^+)} = \mathbf{2.00}$$</li>
</ol>
<p>
In real vibrational nuclei (such as ${}^{106}\text{Pd}$ or ${}^{114}\text{Cd}$), anharmonic terms split the triplet, but the ratio remains very close to $E(4^+)/E(2^+) \approx 2.0\text{ to }2.2$.
</p>
"""
        },
        {
            "id": "sec-5-7",
            "title": "Deformed Nuclei, Nilsson Model, Rotational Bands & Backbending",
            "content": r"""
<h3>1. Permanent Deformation and the Nilsson Model</h3>
<p>
In nuclei with many valence nucleons far from closed shells (rare-earth region $150 < A < 190$ and actinide region $A > 220$), the residual nucleon-nucleon quadrupole interaction overcomes the spherical pairing force, locking the nuclear core into a permanently deformed shape (typically an axially symmetric prolate ellipsoid).
</p>
<p>
Sven Gösta Nilsson (1955) extended the shell model to an axially deformed harmonic oscillator potential parameterized by the quadrupole deformation parameter $\delta$ (or $\beta_2$):
</p>
$$V_{\text{Nilsson}} = \frac{1}{2} M \left[ \omega_\perp^2 (x^2 + y^2) + \omega_z^2 z^2 \right] - C \vec{l}\cdot\vec{s} - D \vec{l}^2$$
<p>
Because spherical symmetry is broken, total angular momentum $j$ is no longer a good quantum number. Only the projection of angular momentum along the nuclear symmetry axis ($\Omega = j_z$) and parity $\pi$ are conserved. Single-particle states are classified by the <strong>asymptotic Nilsson quantum numbers</strong>:
</p>
$$\Omega^\pi [N, n_z, \Lambda]$$
<p>
where $N$ is total oscillator quantum number, $n_z$ is quanta along symmetry axis, and $\Lambda$ is orbital projection ($j_z = \Lambda \pm 1/2$).
</p>

<h3>2. Nuclear Rotational Bands</h3>
<p>
A permanently deformed, axially symmetric even-even nucleus rotates collectively perpendicular to its symmetry axis. The quantum rotational energy spectrum is governed by the rotational Hamiltonian:
</p>
$$E(I) = \frac{\hbar^2}{2\mathcal{I}} I(I+1)$$
<p>
Because the prolate ellipsoid is symmetric under $180^\circ$ rotation about any perpendicular axis ($\mathcal{R}$-parity), only <strong>even spin states</strong> are allowed in the ground-state band ($K = 0$):
</p>
$$I^\pi = 0^+, \quad 2^+, \quad 4^+, \quad 6^+, \quad 8^+, \quad 10^+, \dots$$
<p>
The energy ratio between the first two excited states is universal:
</p>
$$\frac{E(4^+)}{E(2^+)} = \frac{4(5)}{2(3)} = \frac{20}{6} = \mathbf{3.333}$$
<p>
Observation of $E(4^+)/E(2^+) \approx 3.33$ is the definitive experimental hallmark of a rigid nuclear rotor.
</p>

<h3>3. The Backbending Phenomenon at High Angular Momentum</h3>
<p>
The empirical moment of inertia $\mathcal{I}$ of deformed nuclei is approximately $40\text{ to }50\%$ of the rigid-body value $\mathcal{I}_{\text{rigid}}$, due to pairing correlations that produce nuclear superfluidity.
</p>
<p>
As the nucleus is spun up to high angular momentum ($I \sim 14\text{ to }16\hbar$), the colossal <strong>Coriolis force</strong> $\vec{F}_C = -2 M (\vec{\omega}\times\vec{v})$ acts with opposite sign on time-reversed paired nucleons in high-$j$ intruder orbitals ($1i_{13/2}$ neutrons). At a critical rotational frequency $\omega_c$, the Coriolis force breaks the pair (Coriolis Anti-Pairing effect) and aligns their spins along the rotation axis.
</p>
<p>
This abrupt alignment increases the nuclear moment of inertia toward the rigid-body value, producing a dramatic S-shaped curve when $\mathcal{I}$ is plotted against $\omega^2$—a phenomenon known as <strong>backbending</strong>.
</p>
""",
            "simulation": "nuc2-collective-rotational-vibrational-sim"
        }
    ],
    "problems": [
        {
            "id": "nuc2-prob-5-1",
            "title": "Shell Model Predictions for Ground State Spins and Magnetic Moments",
            "statement": r"""Using the Extreme Single-Particle Shell Model with spin-orbit coupling:
(a) Determine the ground-state spin and parity $J^\pi$ for the three odd-$A$ nuclei:
1. Nitrogen-15 (${}^{15}_7\text{N}_8$)
2. Potassium-39 (${}^{39}_{19}\text{K}_{20}$)
3. Bismuth-209 (${}^{209}_{83}\text{Bi}_{126}$)
(b) Calculate the theoretical single-particle Schmidt magnetic dipole moment $\mu_{\text{Schmidt}}$ in units of $\mu_N$ for each of these three nuclei.
(c) Compare each calculated Schmidt value with the experimental measurement:
$\mu_{\text{exp}}({}^{15}\text{N}) = -0.283\text{ }\mu_N$, $\mu_{\text{exp}}({}^{39}\text{K}) = +0.391\text{ }\mu_N$, $\mu_{\text{exp}}({}^{209}\text{Bi}) = +4.111\text{ }\mu_N$, and comment on the sign and agreement.""",
            "solution": r"""**(a) Shell Filling and $J^\pi$ Predictions:**
1. **${}^{15}_7\text{N}_8$:**
   Neutrons: $N = 8$ is a magic closed shell ($1s_{1/2}^2 1p_{3/2}^4 1p_{1/2}^2$).
   Protons: $Z = 7$ has a hole in the $1p_{1/2}$ shell (capacity 2, contains 1 proton).
   Valence proton is in $1p_{1/2}$ ($l = 1, j = 1/2$).
   Parity $\pi = (-1)^l = (-1)^1 = -1$.
   Predicts: **$J^\pi = 1/2^-$**. (Experiment: $1/2^-$).
2. **${}^{39}_{19}\text{K}_{20}$:**
   Neutrons: $N = 20$ is a magic closed shell.
   Protons: $Z = 19$ has a single proton hole in $1d_{3/2}$ ($l = 2, j = 3/2$).
   Parity $\pi = (-1)^2 = +1$.
   Predicts: **$J^\pi = 3/2^+$**. (Experiment: $3/2^+$).
3. **${}^{209}_{83}\text{Bi}_{126}$:**
   Neutrons: $N = 126$ is a magic closed shell.
   Protons: $Z = 83$ has one valence proton outside magic $Z = 82$ in $1h_{9/2}$ ($l = 5, j = 9/2$).
   Parity $\pi = (-1)^5 = -1$.
   Predicts: **$J^\pi = 9/2^-$**. (Experiment: $9/2^-$).

**(b) Schmidt Magnetic Moment Calculations:**
Using proton $g$-factors $g_l = 1, g_s = +5.5857$:
1. **${}^{15}\text{N}$ (Proton in $p_{1/2}$, $j = l - 1/2$ with $l=1, j=1/2$):**
   $$\mu = \frac{j}{j+1}\left[ (j + 3/2)g_l - \frac{1}{2}g_s \right]\mu_N = \frac{1/2}{3/2}\left[ 2(1) - \frac{1}{2}(5.5857) \right]\mu_N$$
   $$\mu = \frac{1}{3}\left[ 2 - 2.7928 \right]\mu_N = \frac{-0.7928}{3}\mu_N \approx \mathbf{-0.2643\text{ }\mu_N}$$
2. **${}^{39}\text{K}$ (Proton hole in $d_{3/2}$, $j = l - 1/2$ with $l=2, j=3/2$):**
   $$\mu = \frac{j}{j+1}\left[ (j + 3/2)g_l - \frac{1}{2}g_s \right]\mu_N = \frac{3/2}{5/2}\left[ 3(1) - 2.7928 \right]\mu_N$$
   $$\mu = \frac{3}{5}\left[ 0.2072 \right]\mu_N \approx \mathbf{+0.1243\text{ }\mu_N}$$
3. **${}^{209}\text{Bi}$ (Proton in $h_{9/2}$, $j = l - 1/2$ with $l=5, j=9/2$):**
   $$\mu = \frac{j}{j+1}\left[ (j + 3/2)g_l - \frac{1}{2}g_s \right]\mu_N = \frac{9/2}{11/2}\left[ 6(1) - 2.7928 \right]\mu_N$$
   $$\mu = \frac{9}{11}\left[ 3.2072 \right]\mu_N \approx \mathbf{+2.624\text{ }\mu_N}$$

**(c) Comparison with Experiment:**
- ${}^{15}\text{N}$: $\mu_{\text{Schmidt}} = -0.264\text{ }\mu_N$ vs $\mu_{\text{exp}} = -0.283\text{ }\mu_N$. The sign is correctly negative and the numerical agreement is outstanding ($< 7\%$ error), characteristic of light, tightly bound closed-shell nuclei.
- ${}^{39}\text{K}$: $\mu_{\text{Schmidt}} = +0.124\text{ }\mu_N$ vs $\mu_{\text{exp}} = +0.391\text{ }\mu_N$. Both are positive.
- ${}^{209}\text{Bi}$: $\mu_{\text{Schmidt}} = +2.624\text{ }\mu_N$ vs $\mu_{\text{exp}} = +4.111\text{ }\mu_N$. The discrepancy is due to core polarization of the large 82-proton/126-neutron core."""
        },
        {
            "id": "nuc2-prob-5-2",
            "title": "Rotational Band Energy Levels and Moment of Inertia of Erbium-164",
            "statement": r"""The experimental excitation energies of the lowest ground-state band levels of the deformed even-even nucleus $^{164}\text{Er}$ are:
$$E(2^+) = 91.4\text{ keV}, \quad E(4^+) = 299.4\text{ keV}, \quad E(6^+) = 614.4\text{ keV}, \quad E(8^+) = 1024.7\text{ keV}$$
(a) Evaluate the experimental energy ratios $E(4^+)/E(2^+)$ and $E(6^+)/E(2^+)$ and compare them with the predictions of an ideal quantum rotor.
(b) From the $2^+$ excitation energy, compute the effective nuclear moment of inertia parameter $A_{\text{rot}} \equiv \frac{\hbar^2}{2\mathcal{I}}$ in $\text{keV}$.
(c) Assuming a rigid prolate ellipsoid of mass $M = A M_N$ and radius $R_0 = 1.2 A^{1/3}\text{ fm}$ with $\beta_2 = 0.30$, the rigid-body moment of inertia is $\mathcal{I}_{\text{rigid}} \approx \frac{2}{5} M R_0^2 (1 + 0.31\beta_2)$. Compute $\frac{\hbar^2}{2\mathcal{I}_{\text{rigid}}}$ and determine the ratio $\mathcal{I}_{\text{eff}} / \mathcal{I}_{\text{rigid}}$. Explain why $\mathcal{I}_{\text{eff}} < \mathcal{I}_{\text{rigid}}$.""",
            "solution": r"""**(a) Experimental Energy Ratios:**
$$R_{4/2} = \frac{E(4^+)}{E(2^+)} = \frac{299.4\text{ keV}}{91.4\text{ keV}} \approx \mathbf{3.276}$$
$$R_{6/2} = \frac{E(6^+)}{E(2^+)} = \frac{614.4\text{ keV}}{91.4\text{ keV}} \approx \mathbf{6.722}$$
For an ideal rotor with $E(I) = A_{\text{rot}} I(I+1)$:
$$R_{4/2}^{\text{ideal}} = \frac{4(5)}{2(3)} = \frac{20}{6} \approx \mathbf{3.333}, \qquad R_{6/2}^{\text{ideal}} = \frac{6(7)}{2(3)} = \frac{42}{6} = \mathbf{7.000}$$
The empirical ratio $R_{4/2} = 3.28$ is within $1.7\%$ of the ideal rigid rotor value $3.33$, definitively confirming that $^{164}\text{Er}$ is a well-deformed collective rotor.

**(b) Effective Rotational Parameter $A_{\text{rot}}$:**
$$E(2^+) = A_{\text{rot}} [2(3)] = 6 A_{\text{rot}} \implies A_{\text{rot}} = \frac{91.4\text{ keV}}{6} \approx \mathbf{15.23\text{ keV}}$$
$$\frac{\hbar^2}{2\mathcal{I}_{\text{eff}}} = 15.23\text{ keV}$$

**(c) Rigid-Body Moment of Inertia and Comparison:**
For $^{164}\text{Er}$ ($A = 164$):
$$R_0 = 1.2 (164)^{1/3} = 1.2 \times 5.474 \approx 6.568\text{ fm}$$
$$M R_0^2 = (164 \times 938.92\text{ MeV}/c^2) (6.568\text{ fm})^2 = 153983 \times 43.14 / c^2 \approx 6.643 \times 10^6\text{ MeV}\cdot\text{fm}^2/c^2$$
Rigid moment of inertia:
$$\mathcal{I}_{\text{rigid}} \approx \frac{2}{5}(6.643 \times 10^6)(1 + 0.31 \times 0.30) = 2.657 \times 10^6 \times 1.093 \approx 2.904 \times 10^6\text{ MeV}\cdot\text{fm}^2/c^2$$
In energy units:
$$\frac{\hbar^2}{2\mathcal{I}_{\text{rigid}}} = \frac{(\hbar c)^2}{2 c^2 \mathcal{I}_{\text{rigid}}} = \frac{38938\text{ MeV}^2\cdot\text{fm}^2}{2 \times 2.904 \times 10^6\text{ MeV}\cdot\text{fm}^2} = \frac{38938}{5.808 \times 10^6}\text{ MeV} \approx 6.704 \times 10^{-3}\text{ MeV} = \mathbf{6.70\text{ keV}}$$
Comparing effective and rigid moments:
$$\frac{\mathcal{I}_{\text{eff}}}{\mathcal{I}_{\text{rigid}}} = \frac{\hbar^2 / 2\mathcal{I}_{\text{rigid}}}{\hbar^2 / 2\mathcal{I}_{\text{eff}}} = \frac{6.70\text{ keV}}{15.23\text{ keV}} \approx \mathbf{0.44} = \mathbf{44\%}$$
**Physical Explanation:**
The effective moment of inertia is only **$44\%$ of the rigid-body value**. This dramatic reduction occurs because atomic nuclei are **BCS-type superfluids**. The pairing force between identical nucleons in time-reversed orbits creates a paired superconducting-like condensate: when the nucleus rotates, only the unpaired particles outside the condensate drag with the rotation, while the paired core flows irrotationally, sharply reducing the effective moment of inertia."""
        },
        {
            "id": "nuc2-prob-5-3",
            "title": "Quadrupole Phonon Spectrum and Anharmonic Splitting in Cadmium-112",
            "statement": r"""In the even-even nucleus $^{112}\text{Cd}$, the ground state has $J^\pi = 0^+$.
The first excited state is at $E(2_1^+) = 617.5\text{ keV}$.
Around $1.3\text{ to }1.4\text{ MeV}$, a nearly degenerate triplet of states is observed:
$$E(0_2^+) = 1224.4\text{ keV}, \quad E(2_2^+) = 1312.4\text{ keV}, \quad E(4_1^+) = 1415.6\text{ keV}$$
(a) Identify the phonon nature of these states in the Bohr-Mottelson collective vibrational model.
(b) Calculate the ideal harmonic vibrator predictions for the energies of the two-phonon states based on $E(2_1^+)$.
(c) Calculate the energy ratios $E(0_2^+)/E(2_1^+)$, $E(2_2^+)/E(2_1^+)$, and $E(4_1^+)/E(2_1^+)$ and analyze the anharmonic energy shifts.""",
            "solution": r"""**(a) Phonon Classification:**
- The ground state ($0^+$) is the **zero-phonon vacuum state** $|0\rangle$.
- The first excited state $2_1^+$ at $617.5\text{ keV}$ is the **one-phonon state** carrying $\lambda^\pi = 2^+$ and energy $\hbar\omega_2 = 617.5\text{ keV}$.
- The triplet $0_2^+, 2_2^+, 4_1^+$ corresponds to the coupling of **two identical quadrupole phonons** ($|2^+ \otimes 2^+\rangle$). Bose-Einstein symmetry restricts total angular momentum to even values: $J^\pi = 0^+, 2^+, 4^+$.

**(b) Ideal Harmonic Predictions:**
In an ideal harmonic quadrupole vibrator:
$$E(2\text{ phonons}) = 2 \hbar\omega_2 = 2 \times 617.5\text{ keV} = \mathbf{1235.0\text{ keV}}$$
All three members of the two-phonon multiplet are predicted to be degenerate at $1235.0\text{ keV}$.

**(c) Experimental Ratios and Anharmonic Analysis:**
$$R(0_2^+) = \frac{1224.4\text{ keV}}{617.5\text{ keV}} \approx \mathbf{1.983}$$
$$R(2_2^+) = \frac{1312.4\text{ keV}}{617.5\text{ keV}} \approx \mathbf{2.125}$$
$$R(4_1^+) = \frac{1415.6\text{ keV}}{617.5\text{ keV}} \approx \mathbf{2.292}$$
**Anharmonic Shift Analysis:**
1. The average energy of the two-phonon triplet is $\langle E_2 \rangle = \frac{1224.4 + 1312.4 + 1415.6}{3} = \frac{3952.4}{3} \approx 1317.5\text{ keV}$, giving an average ratio $\langle R \rangle \approx 2.13$, remarkably close to the harmonic expectation of $2.00$.
2. The splitting of the triplet ($\Delta E = 1415.6 - 1224.4 = 191.2\text{ keV}$) is caused by **cubic and quartic anharmonic terms** in the collective potential energy surface (such as $V_{\text{anh}} \propto (\alpha_2 \otimes \alpha_2 \otimes \alpha_2)_0$), which partially couple vibrational phonons to underlying quasiparticle degrees of freedom."""
        }
    ]
}

u6_data = {
    "title": "Nuclear Reactions & Scattering: Optical Model, Direct/Compound Processes & Resonances",
    "subtitle": "Complex Potentials, Partial Waves, S-Matrix, Stripping/Pickup & Breit-Wigner",
    "summary": "Mathematical framework of nuclear collisions: reaction kinematics, Q-values and laboratory threshold energies, phenomenological Optical Model using complex potentials U(r) = -V f(r) - i W g(r) representing non-elastic channel absorption (cloudy crystal ball), partial-wave decomposition with scattering matrix S_l = η_l e^{2iδ_l}, transmission coefficients T_l, direct reaction mechanisms (deuteron stripping and pickup) with Butler forward angular distributions, Niels Bohr compound nucleus hypothesis with independent statistical decay, continuum level densities, and Breit-Wigner single-level resonance dispersion formula with resonant-potential scattering interference.",
    "sections": [
        {
            "id": "sec-6-1",
            "title": "Nuclear Reaction Kinematics, Q-Values & Threshold Energies",
            "content": r"""
<h3>1. Energetics and the Reaction Q-Value</h3>
<p>
Consider a generic two-body nuclear reaction in which projectile $a$ collides with stationary target $X$, producing ejectile $b$ and residual nucleus $Y$:
</p>
$$a + X \to Y + b \quad \text{or} \quad X(a, b)Y$$
<p>
The <strong>reaction $Q$-value</strong> is defined as the difference between initial and final nuclear rest masses:
</p>
$$Q \equiv \left[ (m_a + M_X) - (m_b + M_Y) \right] c^2 = T_b + T_Y - T_a$$
<p>
where $T_i$ denotes kinetic energy.
</p>
<ul>
  <li><strong>Exoergic (Exothermic) Reaction ($Q > 0$):</strong> Nuclear mass is converted into kinetic energy. The reaction can proceed even at zero incident projectile energy ($T_a \to 0$).</li>
  <li><strong>Endoergic (Endothermic) Reaction ($Q < 0$):</strong> Incident kinetic energy is converted into mass. The reaction cannot occur unless the projectile energy exceeds a minimum <strong>threshold energy</strong> $E_{\text{th}}$.</li>
</ul>

<h3>2. Derivation of the Laboratory Threshold Energy</h3>
<p>
In the center-of-mass (CM) frame, total linear momentum is zero. To create the final rest masses at threshold, the center-of-mass kinetic energy $E_{\text{cm}}$ must at least equal the mass deficit $|Q|$:
</p>
$$E_{\text{cm}} = \frac{M_X}{m_a + M_X} T_{\text{lab}} \ge |Q| = -Q$$
<p>
Solving for the minimum laboratory kinetic energy of projectile $a$:
</p>
$$E_{\text{th}} = |Q| \left( \frac{m_a + M_X}{M_X} \right) = -Q \left( 1 + \frac{m_a}{M_X} \right)$$
<p>
The additional energy fraction $\frac{m_a}{M_X}|Q|$ is unavoidable: it represents the center-of-mass kinetic energy that must be conserved to maintain total linear momentum.
</p>
"""
        },
        {
            "id": "sec-6-2",
            "title": "Phenomenological Optical Model: Complex Potential U(r) = -V - iW",
            "content": r"""
<h3>1. The Cloudy Crystal Ball Model</h3>
<p>
When nucleons or composite projectiles collide with nuclei, two competing processes occur:
</p>
<ol>
  <li><strong>Elastic Scattering:</strong> Projectile and target remain in their ground states ($a + X \to a + X$).</li>
  <li><strong>Absorption / Inelastic Reactions:</strong> The projectile is removed from the elastic channel via inelastic scattering, nucleon transfer, or compound nucleus formation.</li>
</ol>
<p>
In 1954, Herman Feshbach, Charles Porter, and Victor Weisskopf introduced the <strong>Optical Model</strong>, drawing an analogy to a light wave propagating through a semi-transparent, absorbing sphere of glass (a "cloudy crystal ball").
</p>
<p>
In optics, an absorbing medium is described by a complex index of refraction:
</p>
$$\tilde{n} = n + i \kappa$$
<p>
The optical wavevector becomes $k = \tilde{n} k_0 = n k_0 + i \kappa k_0$, causing the electromagnetic wave intensity to attenuate exponentially:
</p>
$$I(z) \propto e^{-2 \kappa k_0 z}$$
<p>
In quantum mechanics, this spatial attenuation is produced by adding a negative <strong>imaginary potential</strong> to the Schrödinger equation:
</p>
$$U(r) = -V(r) - i W(r)$$

<h3>2. The Complex Optical Potential Parameterization</h3>
<p>
Standard phenomenological optical potentials (such as the Becchetti-Greenlees and Koning-Delaroche global parameterizations) take the form:
</p>
$$U(r) = -V_R f_{\text{WS}}(r, R_R, a_R) - i W_V f_{\text{WS}}(r, R_V, a_V) + 4 i a_S W_S \frac{d}{dr}f_{\text{WS}}(r, R_S, a_S) + V_{so} \vec{l}\cdot\vec{s} \left(\frac{\hbar}{m_\pi c}\right)^2 \frac{1}{r}\frac{df_{\text{WS}}}{dr}$$
<p>
where $f_{\text{WS}}(r, R, a) = [1 + \exp((r-R)/a)]^{-1}$ is the Woods-Saxon function.
</p>
<ul>
  <li><strong>Real Depth ($V_R \approx 45\text{ to }55\text{ MeV}$):</strong> Refracts the incoming wave, determining the average phase shift and shape of diffraction oscillations.</li>
  <li><strong>Volume Imaginary Depth ($W_V \approx 5\text{ to }12\text{ MeV}$):</strong> Represents absorption throughout the nuclear volume (dominant at high energies $E > 50\text{ MeV}$).</li>
  <li><strong>Surface Imaginary Depth ($W_S \approx 8\text{ to }14\text{ MeV}$):</strong> Peaked strictly at the nuclear surface via $\frac{df}{dr}$. At low energies ($E < 20\text{ MeV}$), the Pauli principle prevents collisions in the nuclear interior, restricting reactions to the surface.</li>
</ul>
"""
        },
        {
            "id": "sec-6-3",
            "title": "Partial-Wave Analysis of the Optical Model: S-Matrix & Reaction Cross Sections",
            "content": r"""
<h3>1. The Scattering Matrix (S-Matrix) with Absorption</h3>
<p>
In partial-wave scattering from a complex potential, probability is not conserved within the elastic channel alone. The asymptotic radial wavefunction for partial wave $l$ is:
</p>
$$u_l(r) \xrightarrow{r\to\infty} \frac{i}{2} \left[ e^{-i(kr - l\pi/2)} - S_l e^{i(kr - l\pi/2)} \right]$$
<p>
where $S_l$ is the complex <strong>scattering matrix element</strong> ($S$-matrix). Writing $S_l$ in terms of a real phase shift $\delta_l$ and inelastic absorption parameter $\eta_l$:
</p>
$$S_l \equiv \eta_l e^{2i\delta_l}, \qquad 0 \le \eta_l \le 1$$
<ul>
  <li>If there is no absorption ($W = 0$), the flux in the outgoing wave equals the incoming flux: $\eta_l = 1 \implies |S_l| = 1$ (unitary $S$-matrix).</li>
  <li>If absorption occurs ($W > 0$), flux is lost to other channels: $\eta_l < 1 \implies |S_l| < 1$.</li>
  <li>If complete absorption occurs for partial wave $l$ (black disk limit): $\eta_l = 0 \implies S_l = 0$.</li>
</ul>

<h3>2. Elastic, Reaction, and Total Cross Sections</h3>
<p>
Integrating the probability flux gives the exact partial-wave cross sections:
</p>
<ol>
  <li><strong>Elastic Scattering Cross Section:</strong>
  $$\sigma_{\text{el}} = \frac{\pi}{k^2} \sum_{l=0}^\infty (2l+1) |1 - S_l|^2 = \frac{\pi}{k^2} \sum_{l=0}^\infty (2l+1) \left[ 1 + \eta_l^2 - 2\eta_l \cos(2\delta_l) \right]$$</li>
  <li><strong>Reaction (Absorption) Cross Section:</strong>
  $$\sigma_{\text{reac}} = \frac{\pi}{k^2} \sum_{l=0}^\infty (2l+1) \left( 1 - |S_l|^2 \right) = \frac{\pi}{k^2} \sum_{l=0}^\infty (2l+1) (1 - \eta_l^2)$$
  The factor $T_l \equiv 1 - |S_l|^2 = 1 - \eta_l^2$ is the <strong>transmission coefficient</strong>.</li>
  <li><strong>Total Cross Section:</strong>
  $$\sigma_{\text{tot}} = \sigma_{\text{el}} + \sigma_{\text{reac}} = \frac{2\pi}{k^2} \sum_{l=0}^\infty (2l+1) \left[ 1 - \text{Re}(S_l) \right] = \frac{4\pi}{k}\text{Im}[f(0)]$$
  (The Optical Theorem!).</li>
</ol>
<p>
<strong>Important Physical Theorem:</strong>
If $\sigma_{\text{reac}} > 0$ (absorption occurs, $\eta_l < 1$), then $|1 - S_l|^2 > 0$ is unavoidable. Therefore, <strong>absorption is always accompanied by elastic scattering</strong> (shadow/diffraction scattering). You cannot have absorption without elastic scattering!
</p>
""",
            "simulation": "nuc2-optical-model-scattering-sim"
        },
        {
            "id": "sec-6-4",
            "title": "Direct Reactions: Stripping (d, p), Pickup (p, d) & Angular Distributions",
            "content": r"""
<h3>1. Characteristics of Direct Nuclear Reactions</h3>
<p>
When the incident projectile has moderate to high energy ($E \ge 10\text{ MeV/nucleon}$), a collision can proceed via a <strong>direct reaction</strong>:
</p>
<ul>
  <li><strong>Interaction Time:</strong> Extremely brief, equal to the transit time across the nucleus:
  $$\tau_{\text{direct}} \sim \frac{2 R}{v} \approx \frac{10\text{ fm}}{0.2 c} \approx 1.5 \times 10^{-22}\text{ s}$$</li>
  <li><strong>Peripheral Nature:</strong> Direct reactions involve only one or two valence nucleons at the surface of the nucleus; the core nucleons remain undisturbed "spectators".</li>
  <li><strong>Forward-Peaked Angular Distribution:</strong> The differential cross section $\frac{d\sigma}{d\Omega}(\theta)$ is strongly peaked at forward laboratory angles ($\theta \approx 0^\circ \text{ to } 30^\circ$).</li>
</ul>

<h3>2. Stripping and Pickup Reactions</h3>
<ol>
  <li><strong>Deuteron Stripping $(d, p)$ or $(d, n)$:</strong> The loosely bound deuteron ($B = 2.22\text{ MeV}$) grazes the target nucleus. The nuclear force captures the neutron into an empty single-particle shell model orbital $(n, l, j)$, while the proton escapes without entering the nucleus.</li>
  <li><strong>Pickup Reactions $(p, d)$ or $(d, t)$:</strong> The incoming proton snatches a valence neutron from an occupied shell model orbital of the target, emerging as a deuteron.</li>
</ol>

<h3>3. Butler Theory and Spectroscopic Factors</h3>
<p>
In the semi-classical Butler theory, the transferred nucleon carries orbital angular momentum $l$ into the nucleus at impact parameter $R$:
</p>
$$\hbar l \approx p_{\text{trans}} R = q R$$
<p>
where $\vec{q} = \vec{k}_i - \vec{k}_f$ is the momentum transfer vector:
</p>
$$q = \sqrt{k_i^2 + k_f^2 - 2 k_i k_f \cos\theta}$$
<p>
The differential cross section is proportional to the square of the spherical Bessel function $j_l(q R)$:
</p>
$$\frac{d\sigma}{d\Omega}(\theta) \propto |j_l(q R)|^2$$
<p>
Because $j_l(x)$ has its first maximum at a characteristic value $x_{\max} \approx l$:
</p>
<ul>
  <li>$l = 0$: Peak is at $\theta = 0^\circ$ ($q = 0$).</li>
  <li>$l = 1$: Peak is at a small finite angle $\theta_1 > 0^\circ$.</li>
  <li>$l = 2$: Peak is at a larger angle $\theta_2 > \theta_1$.</li>
</ul>
<p>
By simply measuring the angular position of the first maximum in $\frac{d\sigma}{d\Omega}$, experimentalists uniquely determine the <strong>orbital angular momentum $l$</strong> of the single-particle state! The absolute cross-section magnitude yields the <strong>spectroscopic factor $S$</strong>, measuring the degree to which the state matches an unperturbed single-particle shell model state.
</p>
"""
        },
        {
            "id": "sec-6-5",
            "title": "Compound Nucleus Mechanism (Bohr Hypothesis) & Statistical Decay",
            "content": r"""
<h3>1. The Niels Bohr Compound Nucleus Hypothesis</h3>
<p>
In 1936, Niels Bohr proposed that low-energy nuclear reactions (such as thermal or slow neutron capture) proceed through a two-stage mechanism:
</p>
$$a + X \xrightarrow{\text{Stage 1: Formation}} C^* \xrightarrow{\text{Stage 2: Decay}} Y + b$$
<ol>
  <li><strong>Stage 1 (Formation):</strong> The projectile $a$ enters the target nucleus $X$ and undergoes multiple collisions with nucleons, rapidly sharing its kinetic energy and binding energy among all $A$ nucleons. The system forms a highly excited quasi-equilibrium state called the <strong>compound nucleus</strong> $C^*$.</li>
  <li><strong>Stage 2 (Statistical Decay):</strong> The compound nucleus has a long lifetime compared to direct transit times:
  $$\tau_{\text{compound}} \sim 10^{-18} \text{ to } 10^{-15}\text{ s} \quad \left( 10^4 \text{ to } 10^7 \times \tau_{\text{direct}} \right)$$
  During this long lifetime, the energy fluctuations statistically concentrate sufficient energy on a single nucleon (or cluster) to allow it to evaporate from the nucleus.</li>
</ol>

<h3>2. Bohr's Independence Hypothesis</h3>
<p>
Because the lifetime is so long, the compound nucleus loses all memory of its mode of formation, retaining only conserved macroscopic constants of motion: total energy $E^*$, total angular momentum $J$, and parity $\pi$.
</p>
<p>
Therefore, the cross section factorizes into the formation cross section $\sigma_{\text{form}}(a+X \to C^*)$ multiplied by the decay branching ratio $P_{\text{decay}}(C^* \to Y+b) = \frac{\Gamma_b}{\Gamma_{\text{total}}}$:
</p>
$$\sigma(a, b) = \sigma_{\text{form}}(a+X \to C^*) \times \frac{\Gamma_b}{\sum_c \Gamma_c}$$

<h3>3. Classic Experimental Test: Ghoshal's Experiment (1950)</h3>
<p>
S. N. Ghoshal brilliantly tested Bohr's independence hypothesis by forming the same compound nucleus ${}^{64}_{30}\text{Zn}^*$ via two completely different entrance channels at the same excitation energy ($E^* \approx 30\text{ MeV}$):
</p>
$$\text{Channel A: } p + {}^{63}_{29}\text{Cu} \to {}^{64}_{30}\text{Zn}^*$$
$$\text{Channel B: } \alpha + {}^{60}_{28}\text{Ni} \to {}^{64}_{30}\text{Zn}^*$$
<p>
He measured the cross sections for three different exit channels:
</p>
$${}^{64}\text{Zn}^* \to \begin{cases} {}^{63}\text{Zn} + n \\ {}^{62}\text{Cu} + p + n \\ {}^{62}\text{Zn} + 2n \end{cases}$$
<p>
Ghoshal found that the ratios of cross sections for the three exit channels were <strong>identical for both entrance reactions</strong>:
</p>
$$\sigma(p, n) : \sigma(p, pn) : \sigma(p, 2n) = \sigma(\alpha, n) : \sigma(\alpha, pn) : \sigma(\alpha, 2n)$$
<p>
This landmark result provided irrefutable confirmation of the compound nucleus independence hypothesis.
</p>
"""
        },
        {
            "id": "sec-6-6",
            "title": "Continuum Theory & Nuclear Level Density ρ(E)",
            "content": r"""
<h3>1. The Statistical Evaporation Model</h3>
<p>
At high excitation energies ($E^* > 10\text{ MeV}$), individual compound nucleus resonances overlap so densely that discrete quantum states blend into a continuum.
</p>
<p>
In the continuum regime, particle emission is modeled as statistical evaporation from a boiling droplet at nuclear temperature $T$. The kinetic energy spectrum of evaporated neutrons follows a Maxwellian-type distribution:
</p>
$$\frac{d N(E)}{d E} \propto E \exp\left( -\frac{E}{T} \right)$$
<p>
where the nuclear temperature $T$ (in MeV) is related to excitation energy $E^*$ by $E^* = a T^2$.
</p>

<h3>2. Bethe's Nuclear Level Density Formula</h3>
<p>
Hans Bethe (1936) treated the nucleus as an ensemble of non-interacting Fermi gas quasiparticles. Applying the grand canonical partition function:
</p>
$$\rho(E^*) = \frac{1}{\sqrt{48} E^*} \exp\left( 2\sqrt{a E^*} \right)$$
<p>
where the <strong>level density parameter</strong> $a$ is proportional to the single-particle density of states $g(\epsilon_F)$ at the Fermi surface:
</p>
$$a = \frac{\pi^2}{6} g(\epsilon_F) \approx \frac{A}{8} \text{ to } \frac{A}{10}\text{ MeV}^{-1}$$
<p>
Key physical properties:
</p>
<ul>
  <li><strong>Exponential Explosion:</strong> The level density grows exponentially with $\sqrt{E^*}$. In heavy nuclei such as $^{238}\text{U}$ at neutron separation energy ($E^* \approx 6.5\text{ MeV}$), $a \approx 25\text{ MeV}^{-1}$, yielding $\rho \sim 10^6\text{ levels/MeV}$ (average level spacing $D = 1/\rho \sim 1\text{ eV}$).</li>
  <li><strong>Shell Effects:</strong> Near magic numbers ($Z, N = 20, 28, 50, 82, 126$), the single-particle density $g(\epsilon_F)$ drops sharply, reducing $a$ and causing level densities to be orders of magnitude lower than in mid-shell deformed nuclei.</li>
</ul>
"""
        },
        {
            "id": "sec-6-7",
            "title": "Single-Level Breit-Wigner Dispersion Formula & Potential Interference",
            "content": r"""
<h3>1. The Single-Level Breit-Wigner Formula</h3>
<p>
Gregory Breit and Eugene Wigner (1936) derived the dispersion formula for a nuclear reaction proceeding through an isolated compound nucleus resonance state of energy $E_0$, total spin $J$, and total width $\Gamma$:
</p>
$$\sigma(a, b) = \frac{\pi}{k^2} g_J \frac{\Gamma_a \Gamma_b}{(E - E_0)^2 + (\Gamma/2)^2}$$
<p>
where:
</p>
<ul>
  <li>$k = \frac{\sqrt{2\mu E}}{\hbar}$ is the incident relative wavevector.</li>
  <li>$g_J$ is the statistical spin factor:
  $$g_J = \frac{2J + 1}{(2s_a + 1)(2I_X + 1)}$$</li>
  <li>$\Gamma_a$ is the partial width for the entrance channel ($a + X$).</li>
  <li>$\Gamma_b$ is the partial width for the exit channel ($Y + b$).</li>
  <li>$\Gamma$ is the total resonance width: $\Gamma = \sum_c \Gamma_c = \Gamma_a + \Gamma_b + \Gamma_\gamma + \dots$</li>
  <li>By the Heisenberg uncertainty relation, the mean lifetime of the compound resonance is:
  $$\tau = \frac{\hbar}{\Gamma}$$</li>
</ul>

<h3>2. Resonant and Potential Scattering Interference</h3>
<p>
In the elastic channel ($b = a$), the total scattering amplitude is the coherent quantum sum of the hard-sphere potential scattering amplitude $A_{\text{pot}} = \frac{i}{2k}(1 - e^{2i\delta_{\text{pot}}})$ and the resonant Breit-Wigner amplitude $A_{\text{res}}$:
</p>
$$f(\theta) = f_{\text{pot}}(\theta) + f_{\text{res}}(\theta)$$
<p>
For an $s$-wave resonance with potential phase shift $\delta_{\text{pot}} = -k R$:
</p>
$$\sigma_{\text{el}}(E) = \frac{\pi}{k^2} g_J \left| e^{2i\delta_{\text{pot}}} - 1 + \frac{i\Gamma_n}{(E - E_0) + i\Gamma/2} \right|^2$$
$$\sigma_{\text{el}}(E) = \frac{4\pi}{k^2}\sin^2(k R) + \frac{\pi}{k^2} g_J \frac{\Gamma_n^2 + 2\Gamma_n\Gamma\sin^2(kR) - 4\Gamma_n(E - E_0)\sin(kR)\cos(kR)}{(E - E_0)^2 + (\Gamma/2)^2}$$
<p>
The cross-term produces asymmetric <strong>Fano-type interference</strong>:
</p>
<ul>
  <li>Just below the resonance energy ($E < E_0$), the resonant and potential amplitudes interfere destructively, causing the cross section to dip sharply below the potential baseline.</li>
  <li>Just above the resonance energy ($E > E_0$), the amplitudes interfere constructively, generating a steep peak.</li>
</ul>
""",
            "simulation": "nuc2-breit-wigner-resonance-sim"
        }
    ],
    "problems": [
        {
            "id": "nuc2-prob-6-1",
            "title": "Threshold Kinetic Energy and Center-of-Mass Kinematics",
            "statement": r"""Consider the endoergic reaction $^{14}\text{N}(\alpha, p)^{17}\text{O}$, the historical reaction used by Ernest Rutherford in 1919 to achieve the first artificial nuclear transmutation:
Atomic masses:
$M(^{14}\text{N}) = 14.003074\text{ u}$, $M(\alpha) = 4.002603\text{ u}$, $M(p) = 1.007825\text{ u}$, $M(^{17}\text{O}) = 16.999132\text{ u}$
($1\text{ u} = 931.494\text{ MeV}/c^2$).
(a) Calculate the reaction $Q$-value in MeV.
(b) Calculate the minimum kinetic energy $E_{\text{th}}$ the incident alpha particle must possess in the laboratory frame to initiate this reaction on stationary nitrogen.
(c) If an alpha particle of $E_\alpha = 7.68\text{ MeV}$ from $^{214}\text{Po}$ is used, what is the total kinetic energy shared by the proton and $^{17}\text{O}$ in the center-of-mass frame?""",
            "solution": r"""**(a) Reaction $Q$-Value:**
$$\Delta M = [M(^{14}\text{N}) + M(\alpha)] - [M(^{17}\text{O}) + M(p)]$$
$$M_i = 14.003074 + 4.002603 = 18.005677\text{ u}$$
$$M_f = 16.999132 + 1.007825 = 18.006957\text{ u}$$
$$\Delta M = 18.005677 - 18.006957 = -0.001280\text{ u}$$
$$Q = (-0.001280\text{ u}) \times 931.494\text{ MeV/u} \approx \mathbf{-1.1923\text{ MeV}}$$
Because $Q < 0$, the reaction is endoergic.

**(b) Laboratory Threshold Energy $E_{\text{th}}$:**
$$E_{\text{th}} = |Q| \left( 1 + \frac{m_\alpha}{M_N} \right) = 1.1923\text{ MeV} \times \left( 1 + \frac{4.0026}{14.0031} \right)$$
$$1 + \frac{4.0026}{14.0031} = 1 + 0.285837 = 1.285837$$
$$E_{\text{th}} = 1.1923 \times 1.285837 \approx \mathbf{1.533\text{ MeV}}$$
The alpha particle must have at least **$1.533\text{ MeV}$** of kinetic energy in the laboratory frame to initiate the reaction.

**(c) Center-of-Mass Kinetic Energy for $E_\alpha = 7.68\text{ MeV}$:**
The center-of-mass kinetic energy of the entrance channel is:
$$E_{\text{cm, initial}} = E_\alpha \left( \frac{M_N}{m_\alpha + M_N} \right) = 7.68\text{ MeV} \times \frac{14.0031}{18.0057} = 7.68 \times 0.7777 \approx 5.973\text{ MeV}$$
In the exit channel:
$$E_{\text{cm, final}} = E_{\text{cm, initial}} + Q = 5.973\text{ MeV} - 1.192\text{ MeV} \approx \mathbf{4.781\text{ MeV}}$$
The proton and $^{17}\text{O}$ share **$4.78\text{ MeV}$** of kinetic energy in the center-of-mass frame."""
        },
        {
            "id": "nuc2-prob-6-2",
            "title": "Breit-Wigner Analysis of Slow Neutron Resonance in Cadmium-113",
            "statement": r"""Cadmium-113 ($^{113}_{48}\text{Cd}$) has an enormous capture cross section for thermal neutrons due to an isolated $s$-wave ($l = 0$) compound resonance at $E_0 = 0.178\text{ eV}$ in $^{114}\text{Cd}^*$.
The target spin is $I_X = 1/2^+$, the compound state has $J^\pi = 1^+$, the neutron partial width is $\Gamma_n = 0.65\text{ meV}$, and the radiative capture width is $\Gamma_\gamma = 113\text{ meV}$. (Scattering and fission widths are negligible, so $\Gamma \approx \Gamma_n + \Gamma_\gamma$).
(a) Calculate the statistical spin factor $g_J$.
(b) Determine the relative de Broglie wavelength $\lambdabar$ of the neutron at resonance energy $E_0$.
(c) Calculate the peak radiative capture cross section $\sigma_\gamma(E_0)$ in barns ($1\text{ b} = 10^{-24}\text{ cm}^2$).""",
            "solution": r"""**(a) Statistical Spin Factor $g_J$:**
Neutron spin $s_n = 1/2$, target nucleus spin $I_X = 1/2$, resonance spin $J = 1$:
$$g_J = \frac{2J + 1}{(2s_n + 1)(2I_X + 1)} = \frac{2(1) + 1}{(2(1/2) + 1)(2(1/2) + 1)} = \frac{3}{(2)(2)} = \frac{3}{4} = \mathbf{0.75}$$

**(b) Reduced Wavelength $\lambdabar$ at Resonance:**
Neutron mass $m_n c^2 \approx 939.57\text{ MeV}$. At $E_0 = 0.178\text{ eV} = 0.178 \times 10^{-6}\text{ MeV}$:
$$k = \frac{\sqrt{2 m_n E_0}}{\hbar} = \frac{\sqrt{2(939.57)(0.178 \times 10^{-6})}}{197.327\text{ MeV}\cdot\text{fm}} = \frac{\sqrt{3.3449 \times 10^{-4}}}{197.327} = \frac{0.018289}{197.327} \approx 9.2684 \times 10^{-5}\text{ fm}^{-1}$$
$$\lambdabar = \frac{1}{k} = \frac{1}{9.2684 \times 10^{-5}\text{ fm}^{-1}} \approx 10789\text{ fm} = \mathbf{1.079 \times 10^{-10}\text{ cm}}$$
$$\frac{\pi}{k^2} = \pi \lambdabar^2 = \pi (10789\text{ fm})^2 = \pi (1.164 \times 10^8\text{ fm}^2) \approx 3.657 \times 10^8\text{ fm}^2 = 3.657 \times 10^6\text{ b}$$

**(c) Peak Radiative Capture Cross Section $\sigma_\gamma(E_0)$:**
Total width:
$$\Gamma = \Gamma_n + \Gamma_\gamma = 0.65\text{ meV} + 113\text{ meV} = 113.65\text{ meV} = 0.11365\text{ eV}$$
At exact resonance ($E = E_0$), $(E - E_0)^2 = 0$:
$$\sigma_\gamma(E_0) = \frac{\pi}{k^2} g_J \frac{\Gamma_n \Gamma_\gamma}{(\Gamma/2)^2} = \frac{4\pi}{k^2} g_J \frac{\Gamma_n \Gamma_\gamma}{\Gamma^2}$$
$$\frac{\Gamma_n \Gamma_\gamma}{\Gamma^2} = \frac{(0.65\text{ meV})(113\text{ meV})}{(113.65\text{ meV})^2} = \frac{73.45}{12916.3} \approx 0.0056866$$
Multiplying factors:
$$\sigma_\gamma(E_0) = 4(3.657 \times 10^6\text{ b}) \times (0.75) \times (0.0056866) = 1.0971 \times 10^7\text{ b} \times 0.0056866 \approx \mathbf{62386\text{ b}} \approx \mathbf{6.24 \times 10^4\text{ b}}$$
The peak capture cross section is colossal: **$\approx 62{,}400\text{ barns}$**! This immense cross section is why cadmium metal is widely used as a thermal neutron control rod in nuclear reactors."""
        },
        {
            "id": "nuc2-prob-6-3",
            "title": "Nuclear Level Density Calculation via Bethe's Formula",
            "statement": r"""Consider the compound nucleus $^{236}_{92}\text{U}^*$ formed by the capture of a thermal neutron on $^{235}\text{U}$.
The excitation energy is equal to the neutron separation energy: $E^* = S_n = 6.55\text{ MeV}$.
The experimental level density parameter for actinides is $a \approx 25.0\text{ MeV}^{-1}$.
(a) Using Hans Bethe's Fermi gas level density formula:
$$\rho(E^*) = \frac{1}{\sqrt{48} E^*} \exp\left( 2\sqrt{a E^*} \right)$$
calculate the total level density $\rho(E^*)$ in $\text{levels/MeV}$.
(b) Compute the average energy spacing between adjacent compound resonance levels $D = 1/\rho(E^*)$ in electron-volts ($\text{eV}$).
(c) Contrast this average spacing with the typical spacing of low-lying discrete single-particle shell model levels ($\sim 1\text{ MeV}$) and explain the physical origin of the colossal difference.""",
            "solution": r"""**(a) Nuclear Level Density $\rho(E^*)$:**
For $E^* = 6.55\text{ MeV}$ and $a = 25.0\text{ MeV}^{-1}$:
$$2\sqrt{a E^*} = 2\sqrt{25.0 \times 6.55} = 2\sqrt{163.75} = 2 \times 12.7965 = 25.593$$
Evaluating the exponential:
$$\exp(25.593) \approx 1.3027 \times 10^{11}$$
Prefactor:
$$\frac{1}{\sqrt{48} E^*} = \frac{1}{\sqrt{48} \times 6.55} = \frac{1}{6.9282 \times 6.55} = \frac{1}{45.38} \approx 0.022036\text{ MeV}^{-1}$$
Multiplying:
$$\rho(E^*) = 0.022036 \times 1.3027 \times 10^{11} \approx \mathbf{2.87 \times 10^9\text{ levels/MeV}}$$

**(b) Average Level Spacing $D$:**
$$D = \frac{1}{\rho(E^*)} = \frac{1}{2.87 \times 10^9\text{ MeV}^{-1}} \approx 3.48 \times 10^{-10}\text{ MeV} = \mathbf{0.348\text{ eV}}$$
The average spacing between adjacent levels is only **$\approx 0.35\text{ eV}$** (about one-third of an electron-volt!).

**(c) Contrast and Physical Origin:**
- Near the ground state ($E^* \sim 0$), nucleons occupy the lowest single-particle orbitals. Creating an excitation requires lifting a single valence nucleon across the shell gap, which costs $\Delta E \sim \hbar\omega \approx 1\text{ MeV}$. Hence $D_{\text{g.s.}} \sim 1\text{ MeV}$.
- At $E^* = 6.55\text{ MeV}$, the excitation energy can be partitioned among dozens of nucleons in an astronomical number of possible combinatorial permutations (microstates): breaking nucleon pairs, scattering across multiple sub-shells, and coupling various angular momentum components.
- By Boltzmann's statistical entropy relation $S = k_B \ln \Omega(E) = 2\sqrt{a E^*}$, the number of accessible many-particle configurations explodes exponentially ($e^{25.6} \sim 10^{11}$), cramming billions of compound states into each MeV and reducing level spacing by a factor of **several million**."""
        }
    ]
}

with open("nuc2_u5.json", "w", encoding="utf-8") as f:
    json.dump(u5_data, f, indent=2, ensure_ascii=False)

with open("nuc2_u6.json", "w", encoding="utf-8") as f:
    json.dump(u6_data, f, indent=2, ensure_ascii=False)

print("nuc2_u5.json and nuc2_u6.json successfully written!")
