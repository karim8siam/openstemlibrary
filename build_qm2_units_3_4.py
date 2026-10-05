import json

# ==============================================================================
# CHAPTER 3: STATIONARY & TIME-DEPENDENT PERTURBATION THEORY
# ==============================================================================
u3 = {
    "id": "unit3",
    "number": 3,
    "title": "Stationary & Time-Dependent Perturbation Theory",
    "subtitle": "Non-Degenerate & Degenerate Expansions, Hydrogen Fine Structure, Stark/Zeeman Splittings, Fermi's Golden Rule & Radiative Transitions",
    "description": "Comprehensive mathematical development of quantum perturbation theory: non-degenerate first- and second-order corrections, degenerate secular determinants, the relativistic fine structure of hydrogen (relativistic kinetic mass shift, spin-orbit Thomas precession, and the Darwin contact term), electric and magnetic field splittings (linear/quadratic Stark and Zeeman/Paschen-Back regimes), time-dependent perturbation expansion, constant and harmonic couplings, Fermi's Golden Rule, and the semiclassical Einstein dipole transition theory.",
    "sections": [
        {
            "id": "sec3-1",
            "title": "Non-Degenerate Time-Independent Perturbation Theory: Systematic Energy & State Expansions",
            "content": r"""
<h3>1. The Rayleigh-Schrödinger Perturbation Series</h3>
<p>
Consider a quantum system described by a Hamiltonian $\hat{H}$ partitioned into an unperturbed Hermitian part $\hat{H}_0$ with known complete orthonormal eigenstates $\{|n^{(0)}\rangle\}$ and energies $\{E_n^{(0)}\}$, and a perturbing potential $\hat{V}$ modulated by a continuous bookkeeping parameter $\lambda \in [0, 1]$:
</p>
$$\hat{H} = \hat{H}_0 + \lambda \hat{V}$$
$$\hat{H}_0 |n^{(0)}\rangle = E_n^{(0)} |n^{(0)}\rangle, \quad \langle m^{(0)} | n^{(0)} \rangle = \delta_{mn}$$
<p>
For a non-degenerate unperturbed energy level ($E_m^{(0)} \ne E_n^{(0)}$ for all $m \ne n$), the exact energy eigenvalues $E_n$ and state kets $|n\rangle$ can be expanded as power series in $\lambda$:
</p>
$$E_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \lambda^3 E_n^{(3)} + \dots$$
$$|n\rangle = |n^{(0)}\rangle + \lambda |n^{(1)}\rangle + \lambda^2 |n^{(2)}\rangle + \dots$$
<p>
Imposing intermediate normalization $\langle n^{(0)} | n \rangle = 1$, all higher-order corrections are strictly orthogonal to the unperturbed state:
</p>
$$\langle n^{(0)} | n^{(k)}\rangle = 0 \quad \forall k \ge 1$$

<h3>2. First- and Second-Order Perturbation Equations</h3>
<p>
Substituting the expansions into the time-independent Schrödinger equation $(\hat{H}_0 + \lambda \hat{V})|n\rangle = E_n |n\rangle$ and collecting like powers of $\lambda$:
</p>
$$\mathcal{O}(\lambda^0): \quad (\hat{H}_0 - E_n^{(0)})|n^{(0)}\rangle = 0$$
$$\mathcal{O}(\lambda^1): \quad (\hat{H}_0 - E_n^{(0)})|n^{(1)}\rangle = (E_n^{(1)} - \hat{V})|n^{(0)}\rangle$$
$$\mathcal{O}(\lambda^2): \quad (\hat{H}_0 - E_n^{(0)})|n^{(2)}\rangle = E_n^{(2)}|n^{(0)}\rangle + (E_n^{(1)} - \hat{V})|n^{(1)}\rangle$$
<p>
Projecting the first-order equation onto $\langle n^{(0)}|$:
</p>
$$\langle n^{(0)} | (\hat{H}_0 - E_n^{(0)}) | n^{(1)}\rangle = 0 = \langle n^{(0)} | (E_n^{(1)} - \hat{V}) | n^{(0)}\rangle \implies E_n^{(1)} = \langle n^{(0)} | \hat{V} | n^{(0)}\rangle$$
<p>
The first-order energy shift is the expectation value of the perturbing potential in the unperturbed state.
</p>
<p>
To determine $|n^{(1)}\rangle$, we project onto an orthogonal unperturbed state $\langle m^{(0)}|$ ($m \ne n$):
</p>
$$\langle m^{(0)} | (\hat{H}_0 - E_n^{(0)}) | n^{(1)}\rangle = (E_m^{(0)} - E_n^{(0)})\langle m^{(0)} | n^{(1)}\rangle = -\langle m^{(0)} | \hat{V} | n^{(0)}\rangle$$
$$\langle m^{(0)} | n^{(1)}\rangle = \frac{\langle m^{(0)} | \hat{V} | n^{(0)}\rangle}{E_n^{(0)} - E_m^{(0)}} \implies |n^{(1)}\rangle = \sum_{m \ne n} \frac{\langle m^{(0)} | \hat{V} | n^{(0)}\rangle}{E_n^{(0)} - E_m^{(0)}} |m^{(0)}\rangle$$
<p>
Projecting the second-order equation onto $\langle n^{(0)}|$:
</p>
$$E_n^{(2)} = \langle n^{(0)} | \hat{V} | n^{(1)}\rangle = \sum_{m \ne n} \frac{|\langle m^{(0)} | \hat{V} | n^{(0)}\rangle|^2}{E_n^{(0)} - E_m^{(0)}}$$
<p>
<strong>Key Physical Insight:</strong> For the ground state ($n = 0$), the denominator $E_0^{(0)} - E_m^{(0)} < 0$ is strictly negative for all $m > 0$. Hence, the second-order energy shift of the ground state is <em>always non-positive</em> ($E_0^{(2)} \le 0$). The ground state energy is depressed by any perturbation that couples it to excited states.
</p>
"""
        },
        {
            "id": "sec3-2",
            "title": "Degenerate Perturbation Theory: Secular Determinant & Lifting of Degeneracy",
            "content": r"""
<h3>1. Breakdown of the Non-Degenerate Formula</h3>
<p>
When the unperturbed eigenvalue $E_n^{(0)}$ is $g$-fold degenerate, there exist $g$ orthonormal eigenstates $\{|n_1^{(0)}\rangle, |n_2^{(0)}\rangle, \dots, |n_g^{(0)}\rangle\}$ possessing the identical energy:
</p>
$$\hat{H}_0 |n_i^{(0)}\rangle = E_n^{(0)} |n_i^{(0)}\rangle \quad (i = 1, \dots, g)$$
<p>
In the non-degenerate formula for $|n^{(1)}\rangle$, energy denominators of the form $E_n^{(0)} - E_m^{(0)}$ vanish for states within the degenerate subspace, causing formal divergences.
</p>

<h3>2. The Secular Equation in the Degenerate Subspace</h3>
<p>
To lift the ambiguity, we must construct the correct zero-order linear combinations $|\psi_\alpha^{(0)}\rangle$ within the $g$-dimensional degenerate eigenspace:
</p>
$$|\psi_\alpha^{(0)}\rangle = \sum_{j=1}^g c_{\alpha j} |n_j^{(0)}\rangle$$
<p>
Writing the first-order Schrödinger equation for $|\psi_\alpha\rangle$:
</p>
$$(\hat{H}_0 - E_n^{(0)})|\psi_\alpha^{(1)}\rangle = (E_\alpha^{(1)} - \hat{V})|\psi_\alpha^{(0)}\rangle$$
<p>
Projecting onto any basis bra $\langle n_i^{(0)}|$ belonging to the degenerate subspace:
</p>
$$\langle n_i^{(0)} | (\hat{H}_0 - E_n^{(0)}) | \psi_\alpha^{(1)}\rangle = 0 = \langle n_i^{(0)} | (E_\alpha^{(1)} - \hat{V}) \sum_{j=1}^g c_{\alpha j} |n_j^{(0)}\rangle$$
$$\sum_{j=1}^g \left( \langle n_i^{(0)} | \hat{V} | n_j^{(0)}\rangle - E_\alpha^{(1)} \delta_{ij} \right) c_{\alpha j} = 0$$
<p>
Defining matrix elements $V_{ij} \equiv \langle n_i^{(0)} | \hat{V} | n_j^{(0)}\rangle$, non-trivial coefficients $c_{\alpha j}$ exist if and only if the <strong>secular determinant</strong> vanishes:
</p>
$$\det\left( V_{ij} - E^{(1)} \delta_{ij} \right) = 0$$
$$\begin{vmatrix} V_{11} - E^{(1)} & V_{12} & \cdots & V_{1g} \\ V_{21} & V_{22} - E^{(1)} & \cdots & V_{2g} \\ \vdots & \vdots & \ddots & \vdots \\ V_{g1} & V_{g2} & \cdots & V_{gg} - E^{(1)} \end{vmatrix} = 0$$
<p>
The roots $E_\alpha^{(1)}$ ($\alpha = 1, \dots, g$) yield the first-order energy splittings. If all $g$ roots are distinct, the perturbation completely lifts the degeneracy. If a symmetry operator $\hat{A}$ commutes with both $\hat{H}_0$ and $\hat{V}$, choosing the unperturbed basis to be simultaneous eigenstates of $\hat{A}$ automatically diagonalizes the matrix $V_{ij}$ ($V_{ij} \propto \delta_{ij}$), avoiding the need to solve the full determinant.
</p>
"""
        },
        {
            "id": "sec3-3",
            "title": "The Fine Structure of the Hydrogen Atom: Relativistic, Spin-Orbit & Darwin Corrections",
            "content": r"""
<h3>1. Physical Origin of Fine Structure</h3>
<p>
The non-relativistic Bohr/Schrödinger theory of hydrogen yields energy levels $E_n = -\frac{13.6\text{ eV}}{n^2}$ that depend solely on the principal quantum number $n$, exhibiting an $n^2$-fold degeneracy. High-resolution spectroscopy reveals that these spectral lines are split by fine structure, originating from three distinct relativistic corrections of order $\alpha^4 m c^2 \approx 10^{-4} E_n$:
</p>
$$\hat{H}_{\text{FS}} = \hat{H}_{\text{rel}} + \hat{H}_{\text{SO}} + \hat{H}_{\text{Darwin}}$$

<h3>2. The Relativistic Mass-Kinetic Correction</h3>
<p>
Expanding the relativistic energy-momentum relation $E = \sqrt{p^2 c^2 + m^2 c^4} = mc^2 + \frac{p^2}{2m} - \frac{p^4}{8m^3 c^2} + \dots$:
</p>
$$\hat{H}_{\text{rel}} = -\frac{\hat{p}^4}{8m^3 c^2} = -\frac{1}{2mc^2}\left(\frac{\hat{p}^2}{2m}\right)^2 = -\frac{1}{2mc^2}\left(\hat{H}_0 - V(r)\right)^2$$
<p>
Evaluating the expectation value in hydrogenic state $|n, l, m_l\rangle$:
</p>
$$\Delta E_{\text{rel}} = \langle \hat{H}_{\text{rel}} \rangle = -\frac{E_n^2}{2mc^2}\left( \frac{4n}{l + 1/2} - 3 \right)$$

<h3>3. Spin-Orbit Coupling and Thomas Precession</h3>
<p>
An electron moving with velocity $\vec{v}$ through the central Coulomb field $\vec{E} = -\frac{1}{e}\frac{dV}{dr}\frac{\vec{r}}{r}$ experiences in its rest frame an effective magnetic field:
</p>
$$\vec{B}' \approx -\frac{\vec{v} \times \vec{E}}{c} = \frac{1}{m e c r}\frac{dV}{dr}(\vec{r} \times \vec{p}) = \frac{1}{m e c r}\frac{dV}{dr}\vec{L}$$
<p>
Coupling to the electron's intrinsic magnetic dipole moment $\vec{\mu}_s = -g_s \frac{e}{2m}\vec{S}$ (with $g_s = 2$), and including the kinematic relativistic <strong>Thomas precession factor</strong> of $1/2$ arising from the rotating non-inertial reference frame:
</p>
$$\hat{H}_{\text{SO}} = \frac{1}{2m^2 c^2}\frac{1}{r}\frac{dV}{dr}(\vec{L}\cdot\vec{S}) = \frac{e^2}{8\pi\varepsilon_0 m^2 c^2 r^3}(\vec{L}\cdot\vec{S})$$
<p>
In the coupled angular momentum basis $|j, m_j, l, s=1/2\rangle$ where $\vec{J} = \vec{L} + \vec{S}$:
</p>
$$\vec{J}^2 = \vec{L}^2 + \vec{S}^2 + 2\vec{L}\cdot\vec{S} \implies \vec{L}\cdot\vec{S} = \frac{\hbar^2}{2}\left(j(j+1) - l(l+1) - 3/4\right)$$
<p>
For $l > 0$, using $\langle r^{-3} \rangle = \frac{1}{a_0^3 n^3 l(l+1/2)(l+1)}$:
</p>
$$\Delta E_{\text{SO}} = \frac{E_n^2}{mc^2}\frac{j(j+1) - l(l+1) - 3/4}{l(l+1/2)(l+1)}$$

<h3>4. The Darwin Term and Total Fine Structure Formula</h3>
<p>
The <strong>Darwin term</strong> arises from relativistic quantum <em>Zitterbewegung</em> (rapid trembling motion of the electron over the Compton wavelength $\lambda_c \sim \hbar/mc$), smearing out the Coulomb potential at the origin:
</p>
$$\hat{H}_{\text{Darwin}} = \frac{\pi\hbar^2}{2m^2 c^2}\left(\frac{e^2}{4\pi\varepsilon_0}\right)\delta^3(\vec{r})$$
<p>
Since only $s$-orbitals ($l=0$) have non-vanishing probability density at the nucleus ($|\psi(0)|^2 = \frac{1}{\pi a_0^3 n^3}$):
</p>
$$\Delta E_{\text{Darwin}} = \frac{E_n^2}{mc^2} n \quad (\text{for } l = 0)$$
<p>
Remarkably, when all three corrections are summed, the $l$-dependent terms algebraically collapse into a single unified formula depending exclusively on $n$ and $j$:
</p>
$$\Delta E_{\text{FS}} = \Delta E_{\text{rel}} + \Delta E_{\text{SO}} + \Delta E_{\text{Darwin}} = \frac{E_n \alpha^2}{n}\left( \frac{1}{j + 1/2} - \frac{3}{4n} \right)$$
<p>
Energy levels with identical total angular momentum $j$ remain degenerate (e.g., $2s_{1/2}$ and $2p_{1/2}$), a degeneracy lifted only by quantum electrodynamic vacuum fluctuations (the <strong>Lamb shift</strong> $\approx 1057\text{ MHz}$).
</p>
"""
        },
        {
            "id": "sec3-4",
            "title": "External Field Effects: Stark Effect (Linear & Quadratic) & Zeeman Splittings",
            "content": r"""
<h3>1. The Stark Effect: Atoms in an Electric Field</h3>
<p>
When an atom is placed in a uniform external electric field $\vec{\mathcal{E}} = \mathcal{E}\hat{z}$, the electrostatic perturbation is:
</p>
$$\hat{V}_{\text{Stark}} = -q\vec{\mathcal{E}}\cdot\vec{r} = e\mathcal{E}\hat{z} = e\mathcal{E}r\cos\theta$$
<p>
Since $\hat{z}$ is odd under spatial parity ($\hat{\Pi}^\dagger \hat{z} \hat{\Pi} = -\hat{z}$), the diagonal expectation value vanishes for any state of definite parity:
</p>
$$E_n^{(1)} = e\mathcal{E}\langle n^{(0)} | \hat{z} | n^{(0)} \rangle = 0$$
<p>
Consequently, non-degenerate atomic states (such as the Hydrogen $1s$ ground state) exhibit only a <strong>quadratic Stark effect</strong>:
</p>
$$\Delta E_{1s} = \sum_{n \ne 1} \frac{|\langle n | e\mathcal{E}z | 1s \rangle|^2}{E_{1s}^{(0)} - E_n^{(0)}} = -\frac{1}{2}\alpha_{\text{pol}}\mathcal{E}^2 = -\frac{9}{4}(4\pi\varepsilon_0)a_0^3 \mathcal{E}^2$$
<p>
where $\alpha_{\text{pol}} = \frac{9}{2}(4\pi\varepsilon_0)a_0^3$ is the atomic polarizability of ground state hydrogen.
</p>
<p>
In the degenerate excited states of hydrogen (such as $n=2$, with states $|2s\rangle, |2p_0\rangle, |2p_1\rangle, |2p_{-1}\rangle$), parity-opposite states $|2s\rangle$ and $|2p_0\rangle$ have non-vanishing dipole coupling:
</p>
$$\langle 2s | e\mathcal{E}z | 2p_0 \rangle = -3 e a_0 \mathcal{E}$$
<p>
Diagonalizing the $2\times 2$ submatrix yields the <strong>linear Stark effect</strong>:
</p>
$$\Delta E = \pm 3 e a_0 \mathcal{E}$$
<p>
The energy shifts linearly with the applied electric field, forming permanent electric dipole moments.
</p>

<h3>2. The Zeeman Effect: Atoms in a Magnetic Field</h3>
<p>
For an atom placed in a uniform magnetic field $\vec{B} = B\hat{z}$, the magnetic dipole interaction Hamiltonian is:
</p>
$$\hat{H}_B = -\vec{\mu}\cdot\vec{B} = \frac{\mu_B}{\hbar}(\hat{L}_z + g_s \hat{S}_z)B = \frac{\mu_B B}{\hbar}(\hat{J}_z + \hat{S}_z)$$
<p>
where $\mu_B = \frac{e\hbar}{2m_e} \approx 9.274 \times 10^{-24}\text{ J/T}$ is the Bohr magneton and $g_s \approx 2$.
</p>
<p>
Two distinct physical regimes arise depending on the ratio of magnetic energy to the fine-structure splitting:
</p>
<ol>
  <li><strong>Weak Field Regime (Zeeman Effect, $\mu_B B \ll \Delta E_{\text{FS}}$):</strong>
    Fine structure dominates; $\vec{J}$ is a good quantum number. In the coupled basis $|j, m_j, l, s\rangle$, using the projection theorem:
    $$\Delta E_Z = \langle j, m_j | \hat{H}_B | j, m_j \rangle = g_J \mu_B B m_j$$
    where $g_J$ is the <strong>Landé $g$-factor</strong>:
    $$g_J = 1 + \frac{j(j+1) + s(s+1) - l(l+1)}{2j(j+1)}$$
  </li>
  <li><strong>Strong Field Regime (Paschen-Back Effect, $\mu_B B \gg \Delta E_{\text{FS}}$):</strong>
    The magnetic field uncouples $\vec{L}$ and $\vec{S}$. States are described by the uncoupled basis $|l, m_l, s, m_s\rangle$:
    $$\Delta E_{PB} = \mu_B B(m_l + 2m_s)$$
  </li>
</ol>
"""
        },
        {
            "id": "sec3-5",
            "title": "Time-Dependent Perturbation Theory: Transition Amplitudes & Harmonic Perturbations",
            "content": r"""
<h3>1. Transition Amplitudes in the Interaction Picture</h3>
<p>
Consider a system with unperturbed Hamiltonian $\hat{H}_0$ subject to a time-dependent perturbation $\hat{V}(t)$ turned on at $t = 0$. In the Schrödinger picture:
</p>
$$|\psi(t)\rangle = \sum_n c_n(t) e^{-i E_n^{(0)} t/\hbar} |n^{(0)}\rangle$$
<p>
Substituting into $i\hbar \frac{\partial}{\partial t}|\psi(t)\rangle = (\hat{H}_0 + \hat{V}(t))|\psi(t)\rangle$ yields the exact set of coupled differential equations for the transition amplitudes:
</p>
$$i\hbar \frac{dc_f(t)}{dt} = \sum_k \langle f^{(0)} | \hat{V}(t) | k^{(0)} \rangle e^{i\omega_{fk}t} c_k(t)$$
<p>
where $\omega_{fk} \equiv \frac{E_f^{(0)} - E_k^{(0)}}{\hbar}$ is the Bohr angular frequency of the transition.
</p>

<h3>2. First-Order Transition Amplitude</h3>
<p>
Assuming the system is initially prepared in state $|i^{(0)}\rangle$ at $t = 0$, so $c_k(0) = \delta_{ki}$:
</p>
$$c_f^{(1)}(t) = -\frac{i}{\hbar}\int_0^t \langle f^{(0)} | \hat{V}(t') | i^{(0)} \rangle e^{i\omega_{fi}t'}\,dt'$$
<p>
The transition probability from state $|i\rangle$ to state $|f\rangle$ is:
</p>
$$\mathcal{P}_{i\to f}(t) = |c_f^{(1)}(t)|^2 = \frac{1}{\hbar^2}\left|\int_0^t V_{fi}(t')e^{i\omega_{fi}t'}\,dt'\right|^2$$

<h3>3. Constant Perturbation Switched on at $t=0$</h3>
<p>
For a constant potential $\hat{V}(t) = \hat{V}$ for $t \ge 0$:
</p>
$$c_f^{(1)}(t) = -\frac{i}{\hbar}V_{fi}\int_0^t e^{i\omega_{fi}t'}\,dt' = -\frac{i}{\hbar}V_{fi} \frac{e^{i\omega_{fi}t} - 1}{i\omega_{fi}} = -\frac{V_{fi}}{\hbar\omega_{fi}} e^{i\omega_{fi}t/2} 2i\sin\left(\frac{\omega_{fi}t}{2}\right)$$
$$\mathcal{P}_{i\to f}(t) = \frac{4|V_{fi}|^2}{\hbar^2\omega_{fi}^2}\sin^2\left(\frac{\omega_{fi}t}{2}\right) = \frac{|V_{fi}|^2}{\hbar^2} t^2 \left[\frac{\sin(\omega_{fi}t/2)}{\omega_{fi}t/2}\right]^2$$
<p>
The function exhibits a sharp central diffraction peak with height proportional to $t^2$ and width $\Delta\omega \sim 2\pi/t$, establishing the time-energy uncertainty relation $\Delta E \Delta t \sim 2\pi\hbar$.
</p>
"""
        },
        {
            "id": "sec3-6",
            "title": "Fermi's Golden Rule, Continuum Density of States & Transition Rates",
            "content": r"""
<h3>1. Transition into a Continuum of Final States</h3>
<p>
When the final state $|f\rangle$ belongs to a dense or continuous spectrum of states with density of states $\rho(E_f)$ (the number of states per unit energy interval $dE$), the total transition probability is the integral over all continuum final states:
</p>
$$\mathcal{P}_{\text{total}}(t) = \int \mathcal{P}_{i\to f}(t) \rho(E_f)\,dE_f = \int \frac{4|V_{fi}|^2}{\hbar^2}\frac{\sin^2[(\omega_{fi}t)/2]}{\omega_{fi}^2} \rho(E_f)\,dE_f$$
<p>
Using the representation of the Dirac delta distribution:
</p>
$$\lim_{t\to\infty} \frac{\sin^2(\alpha t)}{\pi t \alpha^2} = \delta(\alpha) \implies \lim_{t\to\infty} \frac{4\sin^2\left(\frac{(E_f - E_i)t}{2\hbar}\right)}{\frac{(E_f - E_i)^2}{\hbar^2} t} = 2\pi\hbar \delta(E_f - E_i)$$

<h3>2. Fermi's Golden Rule for Constant and Harmonic Perturbations</h3>
<p>
Differentiating with respect to time yields the constant steady-state transition rate $W_{i\to f} \equiv \frac{d\mathcal{P}}{dt}$:
</p>
$$W_{i\to f} = \frac{2\pi}{\hbar}|\langle f | \hat{V} | i \rangle|^2 \rho(E_f) \delta(E_f - E_i)$$
<p>
For a periodic harmonic perturbation $\hat{V}(t) = \hat{F} e^{-i\omega t} + \hat{F}^\dagger e^{i\omega t}$:
</p>
$$W_{i\to f} = \frac{2\pi}{\hbar}|\langle f | \hat{F} | i \rangle|^2 \rho(E_f) \delta(E_f - E_i - \hbar\omega) + \frac{2\pi}{\hbar}|\langle f | \hat{F}^\dagger | i \rangle|^2 \rho(E_f) \delta(E_f - E_i + \hbar\omega)$$
<p>
The first term describes <strong>stimulated absorption</strong> (absorbing a photon of energy $\hbar\omega = E_f - E_i$), while the second describes <strong>stimulated emission</strong> (emitting a photon of energy $\hbar\omega = E_i - E_f$).
</p>
"""
        },
        {
            "id": "sec3-7",
            "title": "Semiclassical Theory of Radiation: Dipole Selection Rules & Einstein Coefficients",
            "content": r"""
<h3>1. The Electric Dipole Approximation</h3>
<p>
In the semiclassical theory of radiation, an atom interacts with an electromagnetic plane wave vector potential $\vec{A}(\vec{r}, t) = A_0 \hat{\epsilon} \cos(\vec{k}\cdot\vec{r} - \omega t)$. Because the optical wavelength $\lambda \approx 500\text{ nm}$ is vastly larger than the atomic radius $a_0 \approx 0.05\text{ nm}$, the spatial phase factor across the atom is nearly constant:
</p>
$$e^{i\vec{k}\cdot\vec{r}} = 1 + i\vec{k}\cdot\vec{r} - \frac{1}{2}(\vec{k}\cdot\vec{r})^2 + \dots \approx 1$$
<p>
This is the <strong>electric dipole (E1) approximation</strong>. The interaction Hamiltonian reduces to the electric dipole interaction:
</p>
$$\hat{H}_{\text{int}} = -\hat{\vec{d}}\cdot\vec{\mathcal{E}}(t) = e\hat{\vec{r}}\cdot\vec{\mathcal{E}}(t)$$

<h3>2. Einstein A and B Coefficients and Spontaneous Emission</h3>
<p>
The rate of stimulated absorption is $W_{\text{abs}} = B_{12} u(\omega)$, where $u(\omega)$ is the spectral radiation energy density. The spontaneous emission rate $A_{21}$ (occurring in the absence of external radiation) is related to the stimulated coefficient by Planck's blackbody law:
</p>
$$A_{21} = \frac{\hbar\omega^3}{\pi^2 c^3} B_{21} = \frac{\omega^3 |\vec{d}_{fi}|^2}{3\pi\varepsilon_0 \hbar c^3}$$
<p>
The radiative lifetime of the excited state is $\tau = 1 / A_{21}$.
</p>

<h3>3. Electric Dipole Selection Rules</h3>
<p>
The transition dipole matrix element $\langle n', l', m' | \hat{\vec{r}} | n, l, m \rangle$ evaluates to zero unless the initial and final quantum numbers satisfy specific selection rules:
</p>
<ol>
  <li><strong>Parity Selection Rule:</strong> States must have opposite parity $\pi_i \pi_f = -1$.</li>
  <li><strong>Orbital Angular Momentum:</strong> $\Delta l = l' - l = \pm 1$. Direct transitions $l \to l$ (such as $2s \to 1s$) are strictly forbidden in E1 radiation.</li>
  <li><strong>Magnetic Quantum Number:</strong> $\Delta m = m' - m = 0$ (for $\pi$-polarized light parallel to $z$), and $\Delta m = \pm 1$ (for $\sigma^\pm$-circularly polarized light in the $xy$-plane).</li>
</ol>
"""
        }
    ],
    "simulations": [
        {
            "id": "qm2-stark-zeeman-levels-sim",
            "title": "Interactive Stark & Zeeman Hydrogen Level Splitting",
            "description": "Visualizer for Hydrogen n=2 energy level splitting under continuous variation of electric field E (linear Stark) and magnetic field B (weak Zeeman to strong Paschen-Back regimes)."
        },
        {
            "id": "qm2-fermi-golden-rule-sim",
            "title": "Fermi's Golden Rule Sinc-Squared Transition Dynamics",
            "description": "Interactive time-dependent transition probability visualizer demonstrating how the sinc²(Δω t / 2) curve narrows into a Dirac delta distribution as interaction time t increases."
        }
    ],
    "solvedProblems": [
        {
            "number": 1,
            "title": "Second-Order Perturbation of a Quartic Anharmonic Oscillator",
            "statement": r"A 1D quantum harmonic oscillator of mass $m$ and frequency $\omega$ is perturbed by a quartic potential $\hat{V} = \lambda \hat{x}^4$, where $\lambda$ is a small parameter.\n(a) Compute the first-order energy correction $E_n^{(1)}$ for any Fock state $|n\rangle$.\n(b) Compute the second-order ground-state energy correction $E_0^{(2)}$.",
            "solution": r"**(a) First-Order Correction:**\nExpressing $\hat{x}$ in terms of ladder operators:\n$$\hat{x} = \sqrt{\frac{\hbar}{2m\omega}}(\hat{a} + \hat{a}^\dagger)$$\n$$\hat{x}^4 = \left(\frac{\hbar}{2m\omega}\right)^2 (\hat{a} + \hat{a}^\dagger)^4$$\nUsing our result from Chapter 1, Section 7:\n$$\langle n | (\hat{a} + \hat{a}^\dagger)^4 | n \rangle = 3(2n^2 + 2n + 1)$$\nTherefore, the first-order energy shift is:\n$$E_n^{(1)} = \langle n | \lambda \hat{x}^4 | n \rangle = \lambda \frac{3\hbar^2}{4m^2\omega^2}(2n^2 + 2n + 1)$$\nFor the ground state ($n=0$):\n$$E_0^{(1)} = \frac{3\lambda\hbar^2}{4m^2\omega^2}$$\n\n**(b) Second-Order Correction for Ground State:**\nThe second-order energy formula is:\n$$E_0^{(2)} = \sum_{k \ne 0} \frac{|\langle k | \lambda \hat{x}^4 | 0 \rangle|^2}{E_0^{(0)} - E_k^{(0)}}$$\nWe evaluate the action of $(\hat{a} + \hat{a}^\dagger)^4$ on the vacuum state $|0\rangle$:\nSince $\hat{a}|0\rangle = 0$:\n$$(\hat{a} + \hat{a}^\dagger)|0\rangle = |1\rangle$$\n$$(\hat{a} + \hat{a}^\dagger)^2|0\rangle = (\hat{a} + \hat{a}^\dagger)|1\rangle = |0\rangle + \sqrt{2}|2\rangle$$\n$$(\hat{a} + \hat{a}^\dagger)^3|0\rangle = |1\rangle + \sqrt{2}(\sqrt{2}|1\rangle + \sqrt{3}|3\rangle) = 3|1\rangle + \sqrt{6}|3\rangle$$\n$$(\hat{a} + \hat{a}^\dagger)^4|0\rangle = 3|0\rangle + 3\sqrt{2}|2\rangle + \sqrt{6}(\sqrt{3}|2\rangle + 2|4\rangle) = 3|0\rangle + 6\sqrt{2}|2\rangle + 2\sqrt{6}|4\rangle$$\nTherefore, non-vanishing matrix elements exist only for intermediate states $k = 2$ and $k = 4$:\n$$\langle 2 | (\hat{a} + \hat{a}^\dagger)^4 | 0 \rangle = 6\sqrt{2}$$\n$$\langle 4 | (\hat{a} + \hat{a}^\dagger)^4 | 0 \rangle = 2\sqrt{6}$$\nThe unperturbed energy differences are:\n$$E_0^{(0)} - E_2^{(0)} = -2\hbar\omega, \quad E_0^{(0)} - E_4^{(0)} = -4\hbar\omega$$\nSubstituting into the sum:\n$$E_0^{(2)} = \lambda^2 \left(\frac{\hbar}{2m\omega}\right)^4 \left[ \frac{(6\sqrt{2})^2}{-2\hbar\omega} + \frac{(2\sqrt{6})^2}{-4\hbar\omega} \right] = \lambda^2 \frac{\hbar^4}{16m^4\omega^4} \left[ \frac{72}{-2\hbar\omega} + \frac{24}{-4\hbar\omega} \right]$$\n$$= \lambda^2 \frac{\hbar^4}{16m^4\omega^4} \left[ -\frac{36}{\hbar\omega} - \frac{6}{\hbar\omega} \right] = -\frac{42}{16}\frac{\lambda^2 \hbar^3}{m^4\omega^5} = -\frac{21}{8}\frac{\lambda^2 \hbar^3}{m^4\omega^5}$$\nNotice $E_0^{(2)} < 0$, verifying the universal depression of the ground state energy."
        },
        {
            "number": 2,
            "title": "Degenerate Perturbation Analysis of the Linear Stark Effect in Hydrogen n=2",
            "statement": r"The $n=2$ energy level of hydrogen is 4-fold degenerate (neglecting spin), spanned by basis states $\{|2s\rangle, |2p_0\rangle, |2p_1\rangle, |2p_{-1}\rangle\}$ with unperturbed energy $E_2^{(0)} = -3.4\text{ eV}$.\n(a) Write down the $4\times 4$ perturbation matrix for the electric dipole interaction $\hat{V} = e\mathcal{E}\hat{z}$.\n(b) Calculate the dipole matrix element $\langle 2s | e\mathcal{E}\hat{z} | 2p_0 \rangle$ using hydrogenic wavefunctions.\n(c) Diagonalize the secular matrix, find the first-order energy shifts, and identify the corresponding eigenstates.",
            "solution": r"**(a) Constructing the Perturbation Matrix:**\nThe perturbation operator is $\hat{V} = e\mathcal{E}r\cos\theta$.\n1. Parity: $\hat{z}$ has odd parity, so diagonal elements vanish: $\langle 2s | \hat{z} | 2s \rangle = \langle 2p_m | \hat{z} | 2p_{m'} \rangle = 0$.\n2. Magnetic quantum number: $\hat{z}$ commutes with $\hat{L}_z$, so $\langle n, l, m | \hat{z} | n', l', m' \rangle \propto \delta_{m, m'}$. Thus, matrix elements between $|2s\rangle$ ($m=0$) and $|2p_{\pm 1}\rangle$ ($m=\pm 1$) vanish identically.\nLet $\Delta \equiv \langle 2s | e\mathcal{E}\hat{z} | 2p_0 \rangle$. The secular matrix in the ordered basis $\{|2s\rangle, |2p_0\rangle, |2p_1\rangle, |2p_{-1}\rangle\}$ is:\n$$\mathbf{V} = \begin{pmatrix} 0 & \Delta & 0 & 0 \\ \Delta^* & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$\n\n**(b) Evaluating the Matrix Element $\Delta$:**\nThe hydrogen radial wavefunctions are:\n$$R_{20}(r) = \frac{1}{(2a_0)^{3/2}} 2\left(1 - \frac{r}{2a_0}\right)e^{-r/2a_0}$$\n$$R_{21}(r) = \frac{1}{(2a_0)^{3/2}} \frac{r}{\sqrt{3}a_0}e^{-r/2a_0}$$\nThe angular functions are $Y_{00} = \frac{1}{\sqrt{4\pi}}$ and $Y_{10} = \sqrt{\frac{3}{4\pi}}\cos\theta$.\n$$\Delta = e\mathcal{E}\int_0^\infty r^3 R_{20}(r) R_{21}(r)\,dr \int_0^{2\pi} d\phi \int_0^\pi \sin\theta \cos\theta Y_{00} Y_{10}\,d\theta$$\nThe angular integral is:\n$$\int_0^\pi \cos^2\theta \sin\theta\,d\theta \sqrt{\frac{3}{4\pi}}\frac{1}{\sqrt{4\pi}}(2\pi) = \frac{\sqrt{3}}{2}\left[-\frac{\cos^3\theta}{3}\right]_0^\pi = \frac{1}{\sqrt{3}}$$\nThe radial integral is:\n$$\int_0^\infty r^3 \frac{2}{\sqrt{3}(2a_0)^3}\left(1 - \frac{r}{2a_0}\right)\frac{r}{a_0}e^{-r/a_0}\,dr = -3\sqrt{3}a_0$$\nMultiplying radial and angular terms:\n$$\Delta = e\mathcal{E}(-3\sqrt{3}a_0)\left(\frac{1}{\sqrt{3}}\right) = -3ea_0\mathcal{E}$$\n\n**(c) Diagonalization and Eigenstates:**\nThe eigenvalues of the non-trivial $2\times 2$ block $\begin{pmatrix} 0 & -3ea_0\mathcal{E} \\ -3ea_0\mathcal{E} & 0 \end{pmatrix}$ are:\n$$E^{(1)} = \pm 3 e a_0 \mathcal{E}$$\nThe 4 split energy levels are:\n1. $E_+^{(1)} = +3 e a_0 \mathcal{E}$, with eigenstate $|\psi_+\rangle = \frac{1}{\sqrt{2}}(|2s\rangle - |2p_0\rangle)$\n2. $E_-^{(1)} = -3 e a_0 \mathcal{E}$, with eigenstate $|\psi_-\rangle = \frac{1}{\sqrt{2}}(|2s\rangle + |2p_0\rangle)$\n3. $E_0^{(1)} = 0$ (2-fold degenerate), with eigenstates $|2p_1\rangle$ and $|2p_{-1}\rangle$."
        },
        {
            "number": 3,
            "title": "Spontaneous Emission Rate and Radiative Lifetime of the Hydrogen 2p to 1s Transition",
            "statement": r"The Lyman-$\alpha$ line corresponds to the spontaneous transition from the $2p$ excited state to the $1s$ ground state in atomic hydrogen.\n(a) Compute the dipole transition matrix element $|\langle 1s | \hat{\vec{r}} | 2p_0 \rangle|$.\n(b) Determine the transition frequency $\omega_0$ and the numerical value of the Einstein spontaneous emission coefficient $A_{2p\to 1s}$.\n(c) Calculate the radiative lifetime $\tau$ of the $2p$ level.",
            "solution": r"**(a) Transition Dipole Matrix Element:**\nTaking the $z$-component $\langle 1s | z | 2p_0 \rangle = \langle 100 | r\cos\theta | 210 \rangle$:\n$$R_{10}(r) = 2a_0^{-3/2}e^{-r/a_0}, \quad R_{21}(r) = \frac{1}{2\sqrt{6}}a_0^{-3/2}\frac{r}{a_0}e^{-r/2a_0}$$\n$$\langle 1s | z | 2p_0 \rangle = \int_0^\infty r^3 R_{10}(r) R_{21}(r)\,dr \int Y_{00}^* \cos\theta Y_{10}\,d\Omega$$\nThe angular integral is $\frac{1}{\sqrt{3}}$. The radial integral is:\n$$\int_0^\infty r^4 \frac{1}{\sqrt{6}a_0^4}e^{-3r/2a_0}\,dr = \frac{1}{\sqrt{6}a_0^4}\frac{4!}{(3/2a_0)^5} = \frac{24}{\sqrt{6}}\left(\frac{2}{3}\right)^5 a_0 = \frac{2^7 \sqrt{6}}{3^5} a_0$$\nMultiplying by the angular factor $\frac{1}{\sqrt{3}}$:\n$$\langle 1s | z | 2p_0 \rangle = \frac{2^7 \sqrt{2}}{3^5} a_0 = \frac{128\sqrt{2}}{243}a_0 \approx 0.745\,a_0$$\nDue to spherical symmetry, $|\vec{d}_{fi}|^2 = e^2 |\langle 1s | z | 2p_0 \rangle|^2 = \frac{2^{15}}{3^9} e^2 a_0^2$.\n\n**(b) Transition Frequency and Einstein A Coefficient:**\n$$\hbar\omega_0 = E_2 - E_1 = -3.4\text{ eV} - (-13.6\text{ eV}) = 10.2\text{ eV} = 1.634 \times 10^{-18}\text{ J}$$\n$$\omega_0 = \frac{1.634 \times 10^{-18}\text{ J}}{1.055 \times 10^{-34}\text{ J}\cdot\text{s}} \approx 1.55 \times 10^{16}\text{ rad/s}$$\nThe Einstein coefficient is:\n$$A_{2p\to 1s} = \frac{\omega_0^3 e^2 |\langle 1s | z | 2p_0 \rangle|^2}{3\pi\varepsilon_0 \hbar c^3} = \frac{4\alpha\omega_0^3}{3c^2}|\langle 1s | z | 2p_0 \rangle|^2$$\nSubstituting numerical constants ($\alpha = 1/137.036$, $c = 3\times 10^8\text{ m/s}$, $a_0 = 5.292 \times 10^{-11}\text{ m}$):\n$$A_{2p\to 1s} \approx 6.27 \times 10^8 \text{ s}^{-1}$$\n\n**(c) Radiative Lifetime:**\n$$\tau = \frac{1}{A_{2p\to 1s}} = \frac{1}{6.27 \times 10^8 \text{ s}^{-1}} \approx 1.60 \times 10^{-9}\text{ s} = 1.60\text{ ns}$$"
        }
    ]
}

# ==============================================================================
# CHAPTER 4: VARIATIONAL METHODS, WKB SEMICLASSICAL APPROXIMATION & APPROXIMATIONS
# ==============================================================================
u4 = {
    "id": "unit4",
    "number": 4,
    "title": "Variational Methods, WKB Semiclassical Approximation & Dynamical Approximations",
    "subtitle": "Rayleigh-Ritz Variational Theorem, Helium Screening, WKB Asymptotics, Airy Connection Formulae, Tunneling & Berry Phase",
    "description": "Exhaustive treatment of non-perturbative approximation techniques: the Rayleigh-Ritz variational theorem, trial wavefunctions, electron shielding in the Helium atom ground state, the linear variational method, the WKB semiclassical expansion, connection formulae via Airy functions at turning points, Bohr-Sommerfeld quantization, quantum tunneling through arbitrary barriers with alpha decay kinetics, and dynamical approximations including the quantum adiabatic theorem, Berry's geometric phase, and sudden transitions.",
    "sections": [
        {
            "id": "sec4-1",
            "title": "The Variational Principle: Rayleigh-Ritz Quotient & Choice of Trial Wavefunctions",
            "content": r"""
<h3>1. The Rayleigh-Ritz Variational Theorem</h3>
<p>
The variational method provides a rigorous technique to establish an upper bound on the ground state energy $E_0$ of any quantum system described by a Hamiltonian $\hat{H}$. Let $\{|n\rangle\}$ be the complete unknown set of exact orthonormal energy eigenstates with true eigenvalues $E_0 \le E_1 \le E_2 \le \dots$.
</p>
<p>
Consider an arbitrary normalized trial state ket $|\psi_{\text{trial}}\rangle \in \mathcal{H}$. Expanding in the exact basis:
</p>
$$|\psi_{\text{trial}}\rangle = \sum_n c_n |n\rangle, \quad \sum_n |c_n|^2 = 1$$
<p>
The energy expectation value (the Rayleigh quotient) evaluates to:
</p>
$$\langle \hat{H} \rangle_{\text{trial}} = \langle \psi_{\text{trial}} | \hat{H} | \psi_{\text{trial}} \rangle = \sum_n |c_n|^2 E_n$$
<p>
Subtracting the true ground-state energy $E_0$:
</p>
$$\langle \hat{H} \rangle_{\text{trial}} - E_0 = \sum_n |c_n|^2 (E_n - E_0) \ge 0$$
<p>
Since $E_n \ge E_0$ and $|c_n|^2 \ge 0$ for all $n$, we obtain the fundamental <strong>Variational Inequality</strong>:
</p>
$$\langle \hat{H} \rangle_{\text{trial}} = \frac{\langle \psi_{\text{trial}} | \hat{H} | \psi_{\text{trial}} \rangle}{\langle \psi_{\text{trial}} | \psi_{\text{trial}} \rangle} \ge E_0$$
<p>
Equality holds if and only if $|\psi_{\text{trial}}\rangle = |0\rangle$.
</p>

<h3>2. Optimization with Variational Parameters</h3>
<p>
In practice, one selects an educated ansatz $\psi(x; \alpha_1, \alpha_2, \dots, \alpha_k)$ containing adjustable variational parameters $\{\alpha_i\}$. The best approximation to the ground state is found by minimizing the Rayleigh quotient:
</p>
$$\frac{\partial \langle \hat{H} \rangle}{\partial \alpha_i} = 0 \quad (i = 1, \dots, k)$$
<p>
The minimum value $\langle \hat{H} \rangle_{\min}$ serves as an upper bound to the true ground state energy $E_0$.
</p>
"""
        },
        {
            "id": "sec4-2",
            "title": "Application to Ground and Excited States: Helium Atom Screening & Linear Potentials",
            "content": r"""
<h3>1. The Ground State of the Helium Atom</h3>
<p>
The Helium atom ($Z=2$) consists of two electrons orbiting a nucleus of charge $+2e$. Neglecting nuclear recoil:
</p>
$$\hat{H} = -\frac{\hbar^2}{2m}\nabla_1^2 - \frac{Ze^2}{4\pi\varepsilon_0 r_1} - \frac{\hbar^2}{2m}\nabla_2^2 - \frac{Ze^2}{4\pi\varepsilon_0 r_2} + \frac{e^2}{4\pi\varepsilon_0 |\vec{r}_1 - \vec{r}_2|}$$
<p>
Without the electron-electron repulsion, the ground state would be two independent $1s$ electrons with energy $2 \times (-Z^2 \times 13.6\text{ eV}) = -108.8\text{ eV}$. However, the experimental ground state energy is $-79.0\text{ eV}$.
</p>

<h3>2. Variational Screening Parameter $Z_{\text{eff}}$</h3>
<p>
Because each electron partially screens the nuclear charge felt by the other, we choose a hydrogenic trial wavefunction with an effective nuclear charge $Z^*$ as the variational parameter:
</p>
$$\psi(\vec{r}_1, \vec{r}_2; Z^*) = \frac{Z^{*3}}{\pi a_0^3} \exp\left(-\frac{Z^*(r_1 + r_2)}{a_0}\right)$$
<p>
Rewriting the Hamiltonian in terms of the effective Hamiltonian:
</p>
$$\hat{H} = \hat{H}_0(Z^*) + (Z^* - Z)\frac{e^2}{4\pi\varepsilon_0}\left(\frac{1}{r_1} + \frac{1}{r_2}\right) + \frac{e^2}{4\pi\varepsilon_0 r_{12}}$$
<p>
Evaluating the expectation values:
</p>
$$\langle \hat{H}_0(Z^*) \rangle = 2 \left(-Z^{*2} E_R\right) = -2 Z^{*2} E_R \quad (E_R = 13.6\text{ eV})$$
$$\left\langle \frac{1}{r_1} + \frac{1}{r_2} \right\rangle = 2\frac{Z^*}{a_0} \implies \langle V_{\text{screen}} \rangle = 4(Z^* - Z)Z^* E_R$$
$$\left\langle \frac{e^2}{4\pi\varepsilon_0 r_{12}} \right\rangle = \frac{5}{8}Z^* \left(\frac{e^2}{4\pi\varepsilon_0 a_0}\right) = \frac{5}{4}Z^* E_R$$
<p>
Summing all terms yields the energy expectation value as a function of $Z^*$:
</p>
$$E(Z^*) = \left[ -2Z^{*2} + 4(Z^* - Z)Z^* + \frac{5}{4}Z^* \right] E_R = \left[ 2Z^{*2} - 4ZZ^* + \frac{5}{4}Z^* \right] E_R$$
<p>
Minimizing with respect to $Z^*$:
</p>
$$\frac{dE}{dZ^*} = \left( 4Z^* - 4Z + \frac{5}{4} \right) E_R = 0 \implies Z^* = Z - \frac{5}{16}$$
<p>
For Helium ($Z = 2$):
</p>
$$Z^* = 2 - \frac{5}{16} = \frac{27}{16} = 1.6875$$
<p>
Each electron screens the nucleus by approximately $0.3125$ electronic charges. The variational ground state energy is:
</p>
$$E(Z^*) = -2 \left(Z - \frac{5}{16}\right)^2 E_R = -2 \left(\frac{27}{16}\right)^2 (13.6\text{ eV}) = -\frac{729}{128}(13.6\text{ eV}) \approx -77.46\text{ eV}$$
<p>
This is within $1.9\%$ of the true experimental value ($-79.0\text{ eV}$).
</p>
"""
        },
        {
            "id": "sec4-3",
            "title": "Linear Variational Method: Secular Determinants & Configuration Interaction",
            "content": r"""
<h3>1. The Ritz Linear Combination of Basis Functions</h3>
<p>
When a system cannot be easily modeled by a simple parameterized function, one expands the trial wavefunction as a linear combination of $N$ known linearly independent basis functions $\{\phi_j\}$:
</p>
$$\psi_{\text{trial}} = \sum_{j=1}^N c_j \phi_j$$
<p>
The energy expectation value is:
</p>
$$E = \frac{\sum_{i=1}^N \sum_{j=1}^N c_i^* c_j H_{ij}}{\sum_{i=1}^N \sum_{j=1}^N c_i^* c_j S_{ij}}$$
<p>
where $H_{ij} = \langle \phi_i | \hat{H} | \phi_j \rangle$ is the Hamiltonian matrix element and $S_{ij} = \langle \phi_i | \phi_j \rangle$ is the overlap matrix element.
</p>

<h3>2. The Generalized Secular Equation</h3>
<p>
Multiplying by the denominator $\sum_{i,j} c_i^* c_j S_{ij}$ and differentiating with respect to $c_k^*$:
</p>
$$\frac{\partial}{\partial c_k^*} \left[ \sum_{i,j} c_i^* c_j (H_{ij} - E S_{ij}) \right] = 0 \implies \sum_{j=1}^N (H_{kj} - E S_{kj}) c_j = 0$$
<p>
This yields a system of linear homogeneous equations, with non-trivial solutions given by the generalized secular determinant:
</p>
$$\det(\mathbf{H} - E \mathbf{S}) = 0$$
<p>
The $N$ real roots $E_1 \le E_2 \le \dots \le E_N$ provide rigorous upper bounds not only for the ground state ($E_1 \ge E_0$), but also for the first $N-1$ excited states (the <strong>Hylleraas-Undheim-MacDonald Theorem</strong>):
</p>
$$E_k \ge E_k^{\text{true}} \quad (k = 1, \dots, N)$$
"""
        },
        {
            "id": "sec4-4",
            "title": "Semiclassical Approximation (W.K.B. Method): Asymptotics & Validity Criterion",
            "content": r"""
<h3>1. The Wentzel-Kramers-Brillouin (WKB) Semiclassical Expansion</h3>
<p>
The WKB method applies to systems where the potential energy $V(x)$ varies slowly compared to the local de Broglie wavelength of the particle. Starting from the 1D time-independent Schrödinger equation:
</p>
$$\frac{d^2\psi}{dx^2} + \frac{2m}{\hbar^2}(E - V(x))\psi(x) = 0 \implies \frac{d^2\psi}{dx^2} + \frac{p^2(x)}{\hbar^2}\psi(x) = 0$$
<p>
where $p(x) = \sqrt{2m(E - V(x))}$ is the classical local momentum. Writing the wave function in terms of an action phase $S(x)$:
</p>
$$\psi(x) = \exp\left(\frac{i}{\hbar}S(x)\right)$$
<p>
Substituting into the Schrödinger equation:
</p>
$$\frac{d\psi}{dx} = \frac{i}{\hbar}S'\psi, \quad \frac{d^2\psi}{dx^2} = \left(\frac{i}{\hbar}S'' - \frac{1}{\hbar^2}(S')^2\right)\psi$$
$$\implies -(S')^2 + i\hbar S'' + p^2(x) = 0$$
<p>
Expanding $S(x)$ as a power series in Planck's constant $\hbar$:
</p>
$$S(x) = S_0(x) + \hbar S_1(x) + \hbar^2 S_2(x) + \dots$$
<p>
Collecting orders of $\hbar$:
</p>
$$\mathcal{O}(\hbar^0): \quad -(S_0')^2 + p^2(x) = 0 \implies S_0'(x) = \pm p(x) \implies S_0(x) = \pm \int p(x)\,dx$$
$$\mathcal{O}(\hbar^1): \quad -2 S_0' S_1' + i S_0'' = 0 \implies S_1'(x) = \frac{i S_0''}{2 S_0'} = \frac{i p'(x)}{2 p(x)}$$
$$S_1(x) = \frac{i}{2}\ln p(x) \implies \exp(i S_1(x)) = \exp\left(-\frac{1}{2}\ln p(x)\right) = \frac{1}{\sqrt{p(x)}}$$

<h3>2. The Semiclassical Wavefunctions and Validity Criterion</h3>
<p>
To first order in $\hbar$, the WKB wavefunction is:
</p>
<ol>
  <li><strong>Classically Allowed Region ($E > V(x)$, $p(x) \in \mathbb{R}$):</strong>
    $$\psi(x) \approx \frac{A}{\sqrt{p(x)}}\exp\left(\frac{i}{\hbar}\int p(x)\,dx\right) + \frac{B}{\sqrt{p(x)}}\exp\left(-\frac{i}{\hbar}\int p(x)\,dx\right)$$
    The probability density $|\psi(x)|^2 \propto \frac{1}{p(x)} \propto \frac{1}{v(x)}$ correctly mirrors the classical dwell time: a particle spends the most time where it travels slowest.
  </li>
  <li><strong>Classically Forbidden Region ($E < V(x)$, $p(x) = i|p(x)|$):</strong>
    $$\psi(x) \approx \frac{C}{\sqrt{|p(x)|}}\exp\left(-\frac{1}{\hbar}\int |p(x)|\,dx\right) + \frac{D}{\sqrt{|p(x)|}}\exp\left(+\frac{1}{\hbar}\int |p(x)|\,dx\right)$$
  </li>
</ol>
<p>
<strong>WKB Validity Criterion:</strong> The condition $|\hbar S_1'| \ll |S_0'|$ requires:
</p>
$$\left| \frac{\hbar p'(x)}{2 p^2(x)} \right| \ll 1 \iff \left| \frac{d}{dx}\left(\frac{\hbar}{p(x)}\right) \right| = \left| \frac{d\bar{\lambda}(x)}{dx} \right| \ll 1$$
<p>
The reduced de Broglie wavelength must vary slowly over a distance of one wavelength. This condition fails catastrophically at classical turning points ($E = V(x)$), where $p(x) \to 0$ and $\lambda(x) \to \infty$.
</p>
"""
        },
        {
            "id": "sec4-5",
            "title": "Solutions Near Turning Points: Airy Functions & WKB Connection Formulae",
            "content": r"""
<h3>1. Linearization Around Classical Turning Points</h3>
<p>
Near a turning point $x = x_0$ where $V(x_0) = E$, the potential can be linearized via a Taylor series:
</p>
$$V(x) \approx E + V'(x_0)(x - x_0)$$
<p>
The Schrödinger equation becomes:
</p>
$$\frac{d^2\psi}{dx^2} - \frac{2m V'(x_0)}{\hbar^2}(x - x_0)\psi = 0$$
<p>
Defining the dimensionless coordinate $z = \left(\frac{2m V'(x_0)}{\hbar^2}\right)^{1/3}(x - x_0)$, this reduces to the canonical <strong>Airy Differential Equation</strong>:
</p>
$$\frac{d^2\psi}{dz^2} - z\psi = 0$$
<p>
Its general solution is a linear combination of the Airy functions $\text{Ai}(z)$ and $\text{Bi}(z)$. For a bound state that decays into the forbidden region $z > 0$, the physically admissible solution is $\text{Ai}(z)$.
</p>

<h3>2. Asymptotic Matching and Connection Formulae</h3>
<p>
Using the known asymptotic expansions of the Airy function $\text{Ai}(z)$:
</p>
$$\text{Ai}(z) \sim \begin{cases} \frac{1}{2\sqrt{\pi} z^{1/4}}\exp\left(-\frac{2}{3}z^{3/2}\right) & \text{for } z \gg 0 \text{ (forbidden)} \\ \frac{1}{\sqrt{\pi}(-z)^{1/4}}\cos\left(\frac{2}{3}(-z)^{3/2} - \frac{\pi}{4}\right) & \text{for } z \ll 0 \text{ (allowed)} \end{cases}$$
<p>
Matching the asymptotic forms of the Airy solution with the WKB expressions on either side of the turning point yields the <strong>WKB Connection Formulae</strong>:
</p>
$$\frac{1}{2\sqrt{|p(x)|}}\exp\left(-\frac{1}{\hbar}\int_{x_0}^x |p(x')|\,dx'\right) \longleftrightarrow \frac{1}{\sqrt{p(x)}}\cos\left(\frac{1}{\hbar}\int_x^{x_0} p(x')\,dx' - \frac{\pi}{4}\right)$$
<p>
The phase shift of $-\pi/4$ at a smooth turning point arises directly from tunneling into the linear turning potential.
</p>
"""
        },
        {
            "id": "sec4-6",
            "title": "WKB Bound State Quantization & Quantum Tunneling: Alpha Decay Barrier Penetration",
            "content": r"""
<h3>1. The Bohr-Sommerfeld-Wilson Quantization Condition</h3>
<p>
Consider a particle bound in a potential well between two classical turning points $x_1$ and $x_2$ ($x_1 < x_2$). Connecting the WKB solution from the left turning point $x_1$ and the right turning point $x_2$:
</p>
$$\psi(x) \propto \frac{1}{\sqrt{p(x)}}\cos\left(\frac{1}{\hbar}\int_{x_1}^x p(x')\,dx' - \frac{\pi}{4}\right)$$
$$\psi(x) \propto \frac{1}{\sqrt{p(x)}}\cos\left(\frac{1}{\hbar}\int_x^{x_2} p(x')\,dx' - \frac{\pi}{4}\right)$$
<p>
For these two expressions to represent the same single-valued physical wavefunction throughout the allowed region $x_1 < x < x_2$, the sum of their arguments must be an integral multiple of $\pi$:
</p>
$$\left(\frac{1}{\hbar}\int_{x_1}^{x_2} p(x')\,dx' - \frac{\pi}{4}\right) + \frac{\pi}{4} = \left(n + \frac{1}{2}\right)\pi$$
$$\int_{x_1}^{x_2} p(x)\,dx = \left(n + \frac{1}{2}\right)\pi\hbar \quad (n = 0, 1, 2, \dots)$$
<p>
This is the <strong>Bohr-Sommerfeld quantization rule</strong> with the Maslov index correction $1/2$ originating from the two smooth $-\pi/4$ turning-point phase losses.
</p>
<p>
If one boundary is an infinitely rigid wall (e.g. $V(x) = \infty$ for $x \le 0$), the wavefunction vanishes strictly at the boundary ($\psi(0) = 0$), yielding a phase shift of $\pi$ rather than $\pi/4$. The quantization rule becomes $\int p\,dx = (n + 3/4)\pi\hbar$.
</p>

<h3>2. Quantum Tunneling and Gamow's Theory of Alpha Decay</h3>
<p>
For a potential barrier extending from $x_1$ to $x_2$ where $V(x) > E$, the WKB transmission probability (tunneling coefficient) through the barrier is:
</p>
$$T \approx \exp\left(-\frac{2}{\hbar}\int_{x_1}^{x_2} |p(x)|\,dx\right) = \exp\left(-\frac{2}{\hbar}\int_{x_1}^{x_2} \sqrt{2m(V(x) - E)}\,dx\right)$$
<p>
Applying this to an alpha particle trapped inside a nucleus of radius $R$ attempting to penetrate the Coulomb barrier $V(r) = \frac{2Ze^2}{4\pi\varepsilon_0 r}$ at energy $E$:
</p>
$$\gamma = \frac{2}{\hbar}\int_R^{r_c} \sqrt{2m\left(\frac{2Ze^2}{4\pi\varepsilon_0 r} - E\right)}\,dr$$
<p>
Carrying out the integration yields the <strong>Geiger-Nuttall law</strong>:
</p>
$$\ln T = -C_1 \frac{Z}{\sqrt{E}} + C_2 \sqrt{ZR} \implies \ln \lambda_{\text{decay}} = A - B \frac{Z}{\sqrt{E}}$$
<p>
This explains why a small variation in alpha decay energy produces variations in nuclear half-lives spanning over 20 orders of magnitude.
</p>
"""
        },
        {
            "id": "sec4-7",
            "title": "Dynamical Approximations: The Adiabatic Theorem, Berry's Phase & Sudden Transitions",
            "content": r"""
<h3>1. The Quantum Adiabatic Theorem</h3>
<p>
Consider a Hamiltonian $\hat{H}(t)$ whose parameters vary smoothly and continuously over time $T$. At each instant $t$, there exists an instantaneous orthonormal basis of eigenstates:
</p>
$$\hat{H}(t)|\psi_n(t)\rangle = E_n(t)|\psi_n(t)\rangle$$
<p>
The <strong>Adiabatic Theorem</strong> (Born and Fock) states: If a system is initially prepared in the $n$-th discrete, non-degenerate eigenstate $|\psi_n(0)\rangle$ and the Hamiltonian changes sufficiently slowly:
</p>
$$\left| \frac{\langle \psi_m(t) | \frac{\partial \hat{H}}{\partial t} | \psi_n(t) \rangle}{E_m(t) - E_n(t)} \right| \ll \frac{|E_m(t) - E_n(t)|}{\hbar} \quad \forall m \ne n$$
<p>
then the system will remain in the instantaneous eigenstate $|\psi_n(t)\rangle$ for all $t$, acquiring only phase factors.
</p>

<h3>2. Berry's Geometric Phase</h3>
<p>
The evolved state under adiabatic evolution is:
</p>
$$|\Psi(t)\rangle = \exp\left(-\frac{i}{\hbar}\int_0^t E_n(t')\,dt'\right) \exp(i\gamma_n(t)) |\psi_n(t)\rangle$$
<p>
The first factor is the familiar dynamical phase. Substituting into the time-dependent Schrödinger equation reveals the equation for $\gamma_n(t)$:
</p>
$$\dot{\gamma}_n(t) = i \langle \psi_n(t) | \dot{\psi}_n(t) \rangle \implies \gamma_n(C) = i \oint_C \langle \psi_n(\vec{R}) | \nabla_{\vec{R}} \psi_n(\vec{R}) \rangle \cdot d\vec{R}$$
<p>
When the parameters trace out a closed circuit $C$ in parameter space, $\gamma_n(C)$ is a non-integrable holonomy depending solely on the geometry and topology of the path—<strong>Berry's Phase</strong>. Using Stokes' theorem:
</p>
$$\gamma_n(C) = \iint_{\Sigma} \vec{\Omega}_n(\vec{R}) \cdot d\vec{\Sigma}$$
<p>
where $\vec{\Omega}_n(\vec{R}) = \nabla \times \vec{\mathcal{A}}_n(\vec{R})$ is the <strong>Berry curvature</strong>.
</p>

<h3>3. The Sudden Approximation</h3>
<p>
In the opposite physical extreme, if the Hamiltonian changes abruptly on a time scale $\Delta t \to 0$ much shorter than the characteristic quantum oscillation period $\tau \sim \hbar / \Delta E$:
</p>
$$|\psi(t_0 + \Delta t)\rangle \approx |\psi(t_0)\rangle$$
<p>
The wavefunction does not have time to respond and remains instantaneously unchanged. The transition probability to find the system in a new energy eigenstate $|m_{\text{new}}\rangle$ is simply the projection:
</p>
$$\mathcal{P}_{n \to m} = |\langle m_{\text{new}} | n_{\text{old}} \rangle|^2$$
"""
        }
    ],
    "simulations": [
        {
            "id": "qm2-variational-helium-sim",
            "title": "Helium Atom Ground State Variational Energy Minimizer",
            "description": "Interactive variational minimization tool plotting ⟨H⟩ as a function of effective nuclear charge Z*, displaying the minimum at Z* = 1.6875 (-77.46 eV) alongside experimental benchmarks."
        },
        {
            "id": "qm2-wkb-tunneling-sim",
            "title": "WKB Semiclassical Barrier Penetration & Alpha Decay Simulator",
            "description": "Simulation of WKB wavefunctions across classical turning points with continuous connection matching, Airy function turning profiles, and exponential tunneling decay."
        }
    ],
    "solvedProblems": [
        {
            "number": 1,
            "title": "Variational Ground-State Energy of the Helium Atom with Screening",
            "statement": r"Using the two-electron trial wavefunction $\psi(\vec{r}_1, \vec{r}_2) = \frac{Z^{*3}}{\pi a_0^3}\exp\left(-\frac{Z^*(r_1 + r_2)}{a_0}\right)$ for the Helium atom ($Z = 2$):\n(a) Detail the calculation of the electron-electron Coulomb repulsion expectation value $\langle V_{ee} \rangle = \left\langle \frac{e^2}{4\pi\varepsilon_0 |\vec{r}_1 - \vec{r}_2|} \right\rangle$.\n(b) Minimize the total energy expectation value $\langle \hat{H} \rangle$ with respect to $Z^*$ and derive the optimal effective nuclear charge $Z^* = 27/16$.\n(c) Calculate the ground state energy and compare it with the first ionization energy of Helium.",
            "solution": r"**(a) Electron-Electron Repulsion Integral:**\nWe expand the Coulomb potential in spherical harmonics using Laplace's expansion:\n$$\frac{1}{|\vec{r}_1 - \vec{r}_2|} = \sum_{l=0}^\infty \frac{r_<^{\,l}}{r_>^{\,l+1}} \frac{4\pi}{2l+1} \sum_{m=-l}^l Y_{lm}^*(\Omega_1) Y_{lm}(\Omega_2)$$\nSince the trial wavefunction is spherically symmetric ($l_1 = l_2 = 0$), only the monopole term $l = 0$ contributes upon angular integration:\n$$\int Y_{00}^*(\Omega_1) Y_{00}(\Omega_1)\,d\Omega_1 \int Y_{00}^*(\Omega_2) Y_{00}(\Omega_2)\,d\Omega_2 = 1$$\nTherefore, the angular integral collapses to unity, leaving the double radial integral:\n$$\langle V_{ee} \rangle = \frac{e^2}{4\pi\varepsilon_0}\left(\frac{Z^{*3}}{\pi a_0^3}\right)^2 (4\pi)^2 \int_0^\infty r_1^2 dr_1 e^{-2Z^* r_1/a_0} \int_0^\infty r_2^2 dr_2 e^{-2Z^* r_2/a_0} \frac{1}{\max(r_1, r_2)}$$\nSplitting into two regions $r_2 < r_1$ and $r_2 > r_1$ and using symmetry:\n$$\int_0^\infty r_2^2 e^{-2Z^* r_2/a_0} \frac{1}{\max(r_1, r_2)}\,dr_2 = \frac{1}{r_1}\int_0^{r_1} r_2^2 e^{-2Z^* r_2/a_0}\,dr_2 + \int_{r_1}^\infty r_2 e^{-2Z^* r_2/a_0}\,dr_2$$\nEvaluating the integrals by parts and integrating over $r_1$ yields the famous result:\n$$\langle V_{ee} \rangle = \frac{5}{8}\frac{Z^* e^2}{4\pi\varepsilon_0 a_0} = \frac{5}{4}Z^* E_R \quad (E_R = 13.6\text{ eV})$$\n\n**(b) Energy Minimization:**\nThe total energy is:\n$$\langle \hat{H} \rangle = \langle T_1 + T_2 \rangle + \langle V_{1} + V_{2} \rangle + \langle V_{ee} \rangle$$\nUsing the virial theorem for hydrogenic states with parameter $Z^*$:\n$$\langle T \rangle = 2 \left(Z^{*2} E_R\right) = 2Z^{*2}E_R$$\n$$\langle V_{\text{nuc}} \rangle = 2\left\langle -\frac{Ze^2}{4\pi\varepsilon_0 r} \right\rangle = -4 Z Z^* E_R$$\n$$\langle \hat{H} \rangle(Z^*) = \left[ 2Z^{*2} - 4ZZ^* + \frac{5}{4}Z^* \right] E_R$$\nSetting $\frac{d\langle \hat{H} \rangle}{dZ^*} = 0$:\n$$4Z^* - 4Z + \frac{5}{4} = 0 \implies Z^* = Z - \frac{5}{16}$$\nFor Helium ($Z = 2$):\n$$Z^* = 2 - \frac{5}{16} = \frac{27}{16} = 1.6875$$\n\n**(c) Ground State Energy & Ionization Potential:**\n$$E_{\text{var}} = \left[ 2\left(\frac{27}{16}\right)^2 - 4(2)\left(\frac{27}{16}\right) + \frac{5}{4}\left(\frac{27}{16}\right) \right] (13.6\text{ eV}) = -2\left(\frac{27}{16}\right)^2 (13.6\text{ eV}) = -\frac{729}{128}(13.6\text{ eV}) \approx -77.46\text{ eV}$$\nComparing to the exact experimental value $-79.00\text{ eV}$, the error is only $1.95\\%$.\nThe energy of a single-ionized Helium ion $\text{He}^+$ is $-Z^2 E_R = -4(13.6\text{ eV}) = -54.4\text{ eV}$.\nThe first ionization energy is:\n$$I_1 = E(\text{He}^+) - E(\text{He}) = -54.4\text{ eV} - (-77.46\text{ eV}) = 23.06\text{ eV}$$\n(Experiment: $24.59\text{ eV}$)."
        },
        {
            "number": 2,
            "title": "Semiclassical WKB Bound State Spectrum of a Linear Potential",
            "statement": r"A particle of mass $m$ moves in a one-dimensional linear potential with an infinitely rigid boundary:\n$$V(x) = \begin{cases} \infty & \text{for } x \le 0 \\ Fx & \text{for } x > 0 \end{cases}$$\nwhere $F > 0$ is a constant force (e.g., a bouncing quantum ball under gravity with $F = mg$).\n(a) Determine the classical turning points for energy $E$.\n(b) Applying the appropriate WKB quantization condition accounting for the rigid wall at $x = 0$ and the smooth turning point at $x = x_0$, find the semiclassical energy eigenvalues $E_n$.\n(c) Compare the WKB energy of the ground state with the exact result obtained from the first zero of the Airy function ($a_1 \approx -2.338$).",
            "solution": r"**(a) Classical Turning Points:**\nFor $x \le 0$, the potential is infinite, so the particle is reflected strictly at $x = 0$.\nFor $x > 0$, the classical turning point $x_0$ satisfies $V(x_0) = E$:\n$$F x_0 = E \implies x_0 = \frac{E}{F}$$\n\n**(b) WKB Quantization Condition:**\nAt $x = 0$, the infinite barrier imposes the Dirichlet boundary condition $\psi(0) = 0$, producing a phase shift of $\pi$ (reflection without penetration).\nAt $x = x_0$, the turning point is smooth and linear, producing a phase shift of $\pi/4$.\nThe WKB quantization condition is:\n$$\int_0^{x_0} p(x)\,dx = \left(n - \frac{1}{4}\right)\pi\hbar = \left(n - \frac{1}{4}\right)\pi\hbar \quad (n = 1, 2, 3, \dots)$$\nThe classical momentum is $p(x) = \sqrt{2m(E - Fx)} = \sqrt{2mF}\sqrt{x_0 - x}$.\nEvaluating the integral:\n$$\int_0^{x_0} \sqrt{2mF}(x_0 - x)^{1/2}\,dx = \sqrt{2mF} \left[ -\frac{2}{3}(x_0 - x)^{3/2} \right]_0^{x_0} = \frac{2}{3}\sqrt{2mF} x_0^{3/2}$$\nSubstituting $x_0 = E/F$:\n$$\frac{2}{3}\frac{\sqrt{2m}}{F} E^{3/2} = \left(n - \frac{1}{4}\right)\pi\hbar$$\nSolving for the energy spectrum $E_n$:\n$$E_n^{3/2} = \frac{3\pi\hbar F}{2\sqrt{2m}}\left(n - \frac{1}{4}\right)$$\n$$E_n = \left(\frac{9\pi^2 \hbar^2 F^2}{8m}\right)^{1/3} \left(n - \frac{1}{4}\right)^{2/3} = \left(\frac{\hbar^2 F^2}{2m}\right)^{1/3} \left[\frac{3\pi}{2}\left(n - \frac{1}{4}\right)\right]^{2/3}$$\n\n**(c) Comparison with the Exact Ground State:**\nThe exact Schrödinger equation $\frac{d^2\psi}{dx^2} + \frac{2m}{\hbar^2}(E - Fx)\psi = 0$ is solved by the Airy function:\n$$\psi(x) \propto \text{Ai}\left(\left(\frac{2mF}{\hbar^2}\right)^{1/3}\left(x - \frac{E}{F}\right)\right)$$\nThe boundary condition $\psi(0) = 0$ requires that $-\left(\frac{2mF}{\hbar^2}\right)^{1/3}\frac{E}{F} = a_n$, where $a_n$ are the zeros of $\text{Ai}(z)$:\n$$E_n^{\text{exact}} = \left(\frac{\hbar^2 F^2}{2m}\right)^{1/3} (-a_n)$$\nFor the ground state ($n = 1$):\n- Exact: $-a_1 \approx 2.3381$\n- WKB: $\left[\frac{3\pi}{2}\left(1 - \frac{1}{4}\right)\right]^{2/3} = \left[\frac{9\pi}{8}\right]^{2/3} = (3.5343)^{2/3} \approx 2.3202$\nPercentage error:\n$$\text{Error} = \frac{2.3381 - 2.3202}{2.3381} \times 100\\% \approx 0.76\\%$$\nThe WKB approximation is remarkably accurate even for the lowest quantum state ($n=1$)!"
        },
        {
            "number": 3,
            "title": "Sudden Expansion of a 1D Infinite Potential Well",
            "statement": r"A particle of mass $m$ is initially in the ground state of an infinite square well of width $L$ ($0 \le x \le L$). At $t = 0$, the right wall is instantaneously moved from $x = L$ to $x = 2L$ (sudden expansion).\n(a) Using the sudden approximation, write down the state of the system immediately after the expansion.\n(b) Calculate the probability that the particle is found in the ground state of the new expanded well.\n(c) Calculate the probability that the particle is found in the first excited state of the new well.",
            "solution": r"**(a) State Immediately After Expansion:**\nBecause the expansion occurs instantaneously ($\Delta t \to 0$), the wavefunction does not change during the transition:\n$$\Psi(x, 0^+) = \psi_1^{\text{old}}(x) = \begin{cases} \sqrt{\frac{2}{L}}\sin\left(\frac{\pi x}{L}\right) & \text{for } 0 \le x \le L \\ 0 & \text{for } L < x \le 2L \end{cases}$$\nThe new stationary eigenstates in the expanded well of width $2L$ are:\n$$\phi_n^{\text{new}}(x) = \sqrt{\frac{2}{2L}}\sin\left(\frac{n\pi x}{2L}\right) = \frac{1}{\sqrt{L}}\sin\left(\frac{n\pi x}{2L}\right) \quad (0 \le x \le 2L)$$\n\n**(b) Probability of Ground State ($n = 1$):**\nThe transition amplitude is the projection overlap $c_1 = \langle \phi_1^{\text{new}} | \Psi(0^+) \rangle$:\n$$c_1 = \int_0^L \frac{1}{\sqrt{L}}\sin\left(\frac{\pi x}{2L}\right) \sqrt{\frac{2}{L}}\sin\left(\frac{\pi x}{L}\right)\,dx = \frac{\sqrt{2}}{L}\int_0^L \sin\left(\frac{\pi x}{2L}\right)\sin\left(\frac{\pi x}{L}\right)\,dx$$\nUsing the product-to-sum identity $\sin A \sin B = \frac{1}{2}[\cos(A - B) - \cos(A + B)]$:\n$$\sin\left(\frac{\pi x}{2L}\right)\sin\left(\frac{\pi x}{L}\right) = \frac{1}{2}\left[\cos\left(\frac{\pi x}{2L}\right) - \cos\left(\frac{3\pi x}{2L}\right)\right]$$\nIntegrating from $0$ to $L$:\n$$\int_0^L \cos\left(\frac{\pi x}{2L}\right)\,dx = \left[\frac{2L}{\pi}\sin\left(\frac{\pi x}{2L}\right)\right]_0^L = \frac{2L}{\pi}\sin\left(\frac{\pi}{2}\right) = \frac{2L}{\pi}$$\n$$\int_0^L \cos\left(\frac{3\pi x}{2L}\right)\,dx = \left[\frac{2L}{3\pi}\sin\left(\frac{3\pi x}{2L}\right)\right]_0^L = \frac{2L}{3\pi}\sin\left(\frac{3\pi}{2}\right) = -\frac{2L}{3\pi}$$\nCombining both integrals:\n$$c_1 = \frac{\sqrt{2}}{L} \frac{1}{2} \left[ \frac{2L}{\pi} - \left(-\frac{2L}{3\pi}\right) \right] = \frac{\sqrt{2}}{2L} \left(\frac{8L}{3\pi}\right) = \frac{4\sqrt{2}}{3\pi}$$\nThe probability of remaining in the ground state of the new well is:\n$$\mathcal{P}_1 = |c_1|^2 = \left(\frac{4\sqrt{2}}{3\pi}\right)^2 = \frac{32}{9\pi^2} \approx \frac{32}{88.826} \approx 0.3603 = 36.03\\%$$\n\n**(c) Probability of First Excited State ($n = 2$):**\nFor $n = 2$, $\phi_2^{\text{new}}(x) = \frac{1}{\sqrt{L}}\sin\left(\frac{\pi x}{L}\right)$:\n$$c_2 = \int_0^L \frac{1}{\sqrt{L}}\sin\left(\frac{\pi x}{L}\right) \sqrt{\frac{2}{L}}\sin\left(\frac{\pi x}{L}\right)\,dx = \frac{\sqrt{2}}{L} \int_0^L \sin^2\left(\frac{\pi x}{L}\right)\,dx = \frac{\sqrt{2}}{L}\left(\frac{L}{2}\right) = \frac{1}{\sqrt{2}}$$\nThe probability of finding the particle in the first excited state is:\n$$\mathcal{P}_2 = |c_2|^2 = \left(\frac{1}{\sqrt{2}}\right)^2 = \frac{1}{2} = 50.00\\%$$\nNotice that $\mathcal{P}_1 + \mathcal{P}_2 = 36.03\\% + 50.00\\% = 86.03\\%$, with the remaining $13.97\\%$ distributed among higher odd states ($c_n = 0$ for all other even $n \ge 4$)."
        }
    ]
}

with open("qm2_u3.json", "w", encoding="utf-8") as f:
    json.dump(u3, f, indent=2)
print("Saved qm2_u3.json")

with open("qm2_u4.json", "w", encoding="utf-8") as f:
    json.dump(u4, f, indent=2)
print("Saved qm2_u4.json")
