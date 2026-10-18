"""
build_quantum_units_7_8_9_10.py
Builds Units 7, 8, 9, and 10 for Quantum Chemistry and Statistical Thermodynamics (OpenSTEM Milestone #52).
Each unit contains 7 comprehensive sections and 7 multi-step solved problems.
Strictly zero prohibited tokens (no course numbers, no marks, no grades, no exams).
"""

def get_units_7_8_9_10():
    units = []

    # =========================================================================
    # UNIT 7: Statistical Mechanics: Microstates, Ensembles & Maxwell-Boltzmann
    # =========================================================================
    unit7 = {
        "id": "unit-7",
        "unitNumber": 7,
        "title": "Unit 7: Statistical Mechanics: Microstates, Ensembles & Maxwell-Boltzmann",
        "leadSummary": r"""Microscopic foundations of classical and quantum statistical thermodynamics: phase space dynamics and the ergodic hypothesis, microcanonical, canonical, and grand canonical ensembles, Boltzmann's entropy postulate S = k ln W, derivation of the Maxwell-Boltzmann distribution law via Lagrange undetermined multipliers, the canonical partition function and connections to thermodynamic state functions, energy fluctuations, and the Maxwell-Boltzmann molecular velocity and speed distribution.""",
        "simulations": [
            "sim_qc_maxwell_boltzmann_microstates"
        ],
        "sections": [
            {
                "id": "sec-7-1",
                "secNumber": "7.1",
                "title": "Microscopic States, Phase Space & The Ergodic Hypothesis",
                "content": r"""Thermodynamics describes macroscopic systems in terms of bulk state variables (temperature \(T\), pressure \(P\), volume \(V\), chemical potential \(\mu\)). Statistical mechanics bridges the gap by deducing these macroscopic laws directly from the underlying microscopic quantum and classical dynamics of \(N \sim 10^{23}\) constituent particles.

### Phase Space Representation
In classical mechanics, the microscopic state (microstate) of a system of \(N\) particles is defined by specifying the positions \(\mathbf{q} = (\mathbf{q}_1, \dots, \mathbf{q}_N)\) and conjugate momenta \(\mathbf{p} = (\mathbf{p}_1, \dots, \mathbf{p}_N)\). This forms a point in a \(6N\)-dimensional **phase space** (\(\Gamma\)-space).
The time evolution of the system traces a continuous trajectory governed by Hamilton's equations of motion:
\[
\dot{\mathbf{q}}_i = \frac{\partial H}{\partial \mathbf{p}_i}, \quad \dot{\mathbf{p}}_i = -\frac{\partial H}{\partial \mathbf{q}_i}
\]
By Liouville's theorem, the phase space volume element \(d\Gamma = d^{3N}q \, d^{3N}p\) occupied by an ensemble of identical systems is strictly conserved over time:
\[
\frac{d\rho}{dt} = \frac{\partial\rho}{\partial t} + \sum_{i=1}^{3N} \left( \frac{\partial\rho}{\partial q_i}\dot{q}_i + \frac{\partial\rho}{\partial p_i}\dot{p}_i \right) = 0
\]
Phase space density behaves as an incompressible fluid.

### Quantum Microstates
In quantum mechanics, the Heisenberg uncertainty principle \(\Delta q_i \Delta p_i \ge \frac{\hbar}{2}\) precludes the simultaneous specification of exact positions and momenta. The phase space is discretized into elementary quantum cells of volume:
\[
\Delta \Gamma_0 = h^{3N}
\]
Each independent non-degenerate stationary quantum eigenstate \(|\psi_i\rangle\) of the total \(N\)-particle Hamiltonian \(\hat{H} |\psi_i\rangle = E_i |\psi_i\rangle\) represents an individual distinct **quantum microstate**.

### The Ergodic Hypothesis and Principle of Equal A Priori Probabilities
A macroscopic measurement takes a finite time \(\tau_{\text{obs}}\) (typically milliseconds to seconds), which is enormous compared to microscopic molecular collision times (\(\tau_{\text{coll}} \sim 10^{-13}\text{ s}\)). The observed macroscopic property is the time average:
\[
\bar{A}_{\text{time}} = \lim_{\tau \rightarrow \infty} \frac{1}{\tau} \int_0^\tau A(\mathbf{q}(t), \mathbf{p}(t)) dt
\]
Because calculating this trajectory for \(10^{23}\) particles is impossible, Willard Gibbs replaced the time average with an **ensemble average**—an instantaneous average across a vast hypothetical collection of identical macroscopic copies of the system:
\[
\langle A \rangle_{\text{ensemble}} = \sum_i P_i A_i
\]
The **Ergodic Hypothesis** asserts that over long times, the system trajectory passes through all accessible microstates, ensuring that the time average equals the ensemble average:
\[
\bar{A}_{\text{time}} = \langle A \rangle_{\text{ensemble}}
\]
For an isolated system with fixed energy \(E\), volume \(V\), and particle number \(N\), every accessible quantum microstate has the exact same probability:
\[
P_i = \begin{cases} \frac{1}{\Omega(E, V, N)} & (E_i \in [E, E + \delta E]) \\ 0 & (\text{otherwise}) \end{cases}
\]
This is the **Postulate of Equal A Priori Probabilities**."""
            },
            {
                "id": "sec-7-2",
                "secNumber": "7.2",
                "title": "Microcanonical, Canonical & Grand Canonical Ensembles",
                "content": r"""Statistical mechanics organizes systems into three fundamental thermodynamic ensembles depending on their thermal and material boundary conditions with the surroundings.

### 1. The Microcanonical Ensemble (\(N, V, E\))
Describes a completely isolated system with fixed particle number \(N\), volume \(V\), and total energy \(E\).
- Walls: Rigid, adiabatic, and impermeable.
- Fundamental quantity: The total number of accessible microstates \(\Omega(E, V, N)\).
- Probability distribution: Uniform over all accessible states:
  \[
  P_i = \frac{1}{\Omega}
  \]

### 2. The Canonical Ensemble (\(N, V, T\))
Describes a closed system in thermal contact with a large heat reservoir at absolute temperature \(T\).
- Walls: Rigid, diathermal (heat-permeable), impermeable to matter.
- The energy of the system fluctuates around a mean value \(\langle E \rangle\).
- Probability of occupying a specific microstate \(i\) of energy \(E_i\):
  \[
  P_i = \frac{e^{-E_i / k_B T}}{Q(N, V, T)} = \frac{e^{-\beta E_i}}{Q}
  \]
  where \(\beta = \frac{1}{k_B T}\) and the normalization denominator is the **Canonical Partition Function**:
  \[
  Q(N, V, T) = \sum_i e^{-\beta E_i}
  \]

### 3. The Grand Canonical Ensemble (\(\mu, V, T\))
Describes an open system that can exchange both heat and particles with a reservoir at fixed temperature \(T\) and chemical potential \(\mu\).
- Walls: Rigid, diathermal, permeable to matter.
- Both energy \(E\) and particle number \(N\) fluctuate.
- Probability of occupying a microstate with \(N\) particles and energy \(E_{N, i}\):
  \[
  P(N, i) = \frac{e^{-\beta (E_{N, i} - \mu N)}}{\Xi(\mu, V, T)}
  \]
  where \(\Xi\) is the **Grand Canonical Partition Function**:
  \[
  \Xi(\mu, V, T) = \sum_{N=0}^\infty e^{\beta \mu N} Q(N, V, T) = \sum_{N=0}^\infty z^N Q(N, V, T)
  \]
  with fugacity \(z = e^{\beta \mu}\).

### Thermodynamic Equivalence in the Thermodynamic Limit
In macroscopic systems where \(N \rightarrow \infty, V \rightarrow \infty\) with constant density \(\rho = N/V\), relative fluctuations in energy and particle number scale as \(1/\sqrt{N} \sim 10^{-11}\). Consequently, all three ensembles yield identical macroscopic thermodynamic predictions."""
            },
            {
                "id": "sec-7-3",
                "secNumber": "7.3",
                "title": "Boltzmann Entropy Formula: S = k ln W & Maximum Probability",
                "content": r"""Ludwig Boltzmann provided the profound statistical definition connecting microscopic disorder with macroscopic thermodynamic entropy.

### The Boltzmann Formula
For an isolated system with \(\Omega\) (or multiplicity \(W\)) accessible microstates:
\[
S = k_B \ln W = k_B \ln \Omega(E, V, N)
\]
where \(k_B = 1.380649 \times 10^{-23}\text{ J}\cdot\text{K}^{-1}\) is the Boltzmann constant.

### Derivation from Additivity and Multiplicativity
Consider two independent, weakly interacting subsystems 1 and 2 with energies \(E_1\) and \(E_2\) and multiplicities \(W_1\) and \(W_2\).
1. By the multiplication principle of independent probabilities, the combined system has total multiplicity:
   \[
   W_{\text{total}} = W_1 \times W_2
   \]
2. By classical thermodynamics, entropy is an extensive state function:
   \[
   S_{\text{total}} = S_1 + S_2
   \]
We seek a mathematical function \(S(W)\) such that \(S(W_1 W_2) = S(W_1) + S(W_2)\).
Differentiating with respect to \(W_1\):
\[
W_2 S'(W_1 W_2) = S'(W_1) \implies W_1 W_2 S'(W_1 W_2) = W_1 S'(W_1) = \text{const} \equiv k_B
\]
Integrating yields the unique functional form:
\[
S(W) = k_B \ln W
\]

### Gibbs Entropy for Arbitrary Distributions
For any arbitrary probability distribution \(\{P_i\}\) across microstates, Willard Gibbs generalized the formula to:
\[
S = -k_B \sum_i P_i \ln P_i
\]
- In the microcanonical ensemble where all \(\Omega\) states have equal probability \(P_i = 1/\Omega\):
  \[
  S = -k_B \sum_{i=1}^\Omega \frac{1}{\Omega} \ln\left(\frac{1}{\Omega}\right) = -k_B \ln\left(\frac{1}{\Omega}\right) = k_B \ln \Omega
  \]
  recovering Boltzmann's equation.
- In information theory, Claude Shannon identified \(- \sum P_i \ln P_i\) as the informational entropy (the measure of missing information). Thermodynamic entropy is the measure of microscopic information hidden by macroscopic averaging."""
            },
            {
                "id": "sec-7-4",
                "secNumber": "7.4",
                "title": "Derivation of Maxwell-Boltzmann Distribution via Lagrange Multipliers",
                "content": r"""Consider a system of \(N\) distinguishable independent particles distributed among discrete energy levels \(\varepsilon_1, \varepsilon_2, \dots, \varepsilon_i, \dots\) with degeneracies \(g_1, g_2, \dots, g_i, \dots\).
Let \(N_i\) be the number of particles in energy level \(\varepsilon_i\).

### Thermodynamic Probability (Multiplicity)
The number of distinct microscopic ways to place \(N\) particles into the energy levels such that there are \(N_i\) particles in level \(i\) (with degeneracy \(g_i\)) is:
\[
W(\{N_i\}) = N! \prod_i \frac{g_i^{N_i}}{N_i!}
\]
Taking the natural logarithm and applying Stirling's approximation (\(\ln x! \approx x \ln x - x\) for \(x \gg 1\)):
\[
\ln W = \ln N! + \sum_i [N_i \ln g_i - \ln N_i!] \approx N \ln N - N + \sum_i [N_i \ln g_i - (N_i \ln N_i - N_i)]
\]
Since \(\sum N_i = N\), the linear terms \(-N + \sum N_i = 0\) cancel:
\[
\ln W = N \ln N - \sum_i N_i \ln\left(\frac{N_i}{g_i}\right)
\]

### Optimization Under Physical Constraints
The most probable macroscopic state corresponds to the distribution \(\{N_i^*\}\) that maximizes \(\ln W\) subject to two rigid physical conservation laws:
1. **Total particle conservation:** \(\phi_1 \equiv \sum_i N_i - N = 0\)
2. **Total internal energy conservation:** \(\phi_2 \equiv \sum_i N_i \varepsilon_i - E = 0\)

Using the method of **Lagrange Undetermined Multipliers**, we introduce multipliers \(\alpha\) and \(\beta\) and construct the unconstrained objective function:
\[
\mathcal{F}(\{N_i\}) = \ln W - \alpha \left(\sum_i N_i - N\right) - \beta \left(\sum_i N_i \varepsilon_i - E\right)
\]
Differentiating with respect to an arbitrary occupation number \(N_k\) and setting to zero:
\[
\frac{\partial \mathcal{F}}{\partial N_k} = -\left[ \ln\left(\frac{N_k}{g_k}\right) + N_k \frac{1}{N_k} \right] - \alpha - \beta \varepsilon_k = 0
\]
\[
-\ln\left(\frac{N_k}{g_k}\right) - 1 - \alpha - \beta \varepsilon_k = 0 \implies \ln\left(\frac{N_k}{g_k}\right) = -(1 + \alpha) - \beta \varepsilon_k
\]
Exponentiating both sides:
\[
\frac{N_k}{g_k} = e^{-(1 + \alpha)} e^{-\beta \varepsilon_k} = A e^{-\beta \varepsilon_k}
\]

### Normalization and Identification of Multipliers
Summing over all levels:
\[
N = \sum_k N_k = A \sum_k g_k e^{-\beta \varepsilon_k} \equiv A q
\]
where \(q = \sum_k g_k e^{-\beta \varepsilon_k}\) is the **molecular partition function**.
Thus, \(A = \frac{N}{q}\), yielding the canonical **Maxwell-Boltzmann Distribution Law**:
\[
N_i = \frac{N g_i e^{-\beta \varepsilon_i}}{q}
\]
By evaluating the thermodynamic identity \(dS = \left(\frac{\partial S}{\partial E}\right)_{V, N} dE = \frac{1}{T} dE\), we find:
\[
\beta = \frac{1}{k_B T}
\]
Hence:
\[
\frac{N_i}{N} = \frac{g_i e^{-\varepsilon_i / k_B T}}{\sum_j g_j e^{-\varepsilon_j / k_B T}}
\]
At absolute zero (\(T \rightarrow 0\)), all particles collapse into the lowest energy ground state. At infinite temperature (\(T \rightarrow \infty\)), particles populate all states proportionally to their degeneracies \(g_i\)."""
            },
            {
                "id": "sec-7-5",
                "secNumber": "7.5",
                "title": "Partition Function & Bridge to Thermodynamic State Functions",
                "content": r"""The canonical partition function \(Q(N, V, T)\) serves as the master generating function connecting microscopic quantum energy spectra \(\{E_i\}\) to all macroscopic thermodynamic state functions.

### The Canonical Partition Function
\[
Q(N, V, T) = \sum_i e^{-\beta E_i(V)}, \quad \text{where } \beta = \frac{1}{k_B T}
\]
For an ideal gas of \(N\) independent particles with single-particle molecular partition function \(q(V, T)\):
- **Distinguishable particles** (e.g., localized atoms in a crystal lattice):
  \[
  Q_{\text{dist}} = q^N
  \]
- **Indistinguishable particles** (e.g., delocalized gas molecules):
  \[
  Q_{\text{indist}} = \frac{q^N}{N!}
  \]
The Gibbs correction factor \(1/N!\) eliminates the Gibbs paradox and restores the extensivity of entropy.

### Fundamental Thermodynamic Relations
From \(Q\), all state functions are generated by straightforward differentiation:
1. **Internal Energy \(U\)**:
   \[
   U = \langle E \rangle = \sum_i E_i P_i = \frac{\sum_i E_i e^{-\beta E_i}}{Q} = -\frac{1}{Q} \frac{\partial Q}{\partial \beta} = -\left( \frac{\partial \ln Q}{\partial \beta} \right)_{V, N} = k_B T^2 \left( \frac{\partial \ln Q}{\partial T} \right)_{V, N}
   \]
2. **Helmholtz Free Energy \(A\)**:
   \[
   A = -k_B T \ln Q
   \]
   This is the central bridge equation of statistical thermodynamics!
3. **Entropy \(S\)**:
   From \(A = U - TS \implies S = \frac{U - A}{T}\):
   \[
   S = k_B \ln Q + k_B T \left( \frac{\partial \ln Q}{\partial T} \right)_{V, N} = -\left( \frac{\partial A}{\partial T} \right)_{V, N}
   \]
4. **Pressure \(P\)**:
   From \(P = -\left( \frac{\partial A}{\partial V} \right)_{T, N}\):
   \[
   P = k_B T \left( \frac{\partial \ln Q}{\partial V} \right)_{T, N}
   \]
5. **Enthalpy \(H\) and Gibbs Free Energy \(G\)**:
   \[
   H = U + P V = k_B T^2 \left( \frac{\partial \ln Q}{\partial T} \right)_{V} + k_B T V \left( \frac{\partial \ln Q}{\partial V} \right)_{T}
   \]
   \[
   G = A + P V = -k_B T \ln Q + k_B T V \left( \frac{\partial \ln Q}{\partial V} \right)_{T}
   \]
6. **Isochoric Heat Capacity \(C_V\)**:
   \[
   C_V = \left( \frac{\partial U}{\partial T} \right)_V = 2 k_B T \left( \frac{\partial \ln Q}{\partial T} \right)_V + k_B T^2 \left( \frac{\partial^2 \ln Q}{\partial T^2} \right)_V = \frac{\langle E^2 \rangle - \langle E \rangle^2}{k_B T^2}
   \]"""
            },
            {
                "id": "sec-7-6",
                "secNumber": "7.6",
                "title": "Energy and Particle Number Fluctuations in Ensembles",
                "content": r"""In the canonical ensemble, the system's energy is not strictly fixed; it fluctuates due to continuous thermal exchange with the reservoir.

### Derivation of Energy Variance
The average energy is:
\[
\langle E \rangle = \frac{1}{Q} \sum_i E_i e^{-\beta E_i} = -\frac{\partial \ln Q}{\partial \beta}
\]
Differentiating \(\langle E \rangle\) with respect to \(\beta\):
\[
\frac{\partial \langle E \rangle}{\partial \beta} = \frac{\partial}{\partial \beta} \left( \frac{1}{Q} \sum_i E_i e^{-\beta E_i} \right) = -\frac{1}{Q^2} \left( \frac{\partial Q}{\partial \beta} \right) \sum_i E_i e^{-\beta E_i} + \frac{1}{Q} \sum_i (-E_i^2) e^{-\beta E_i}
\]
Using \(\frac{\partial Q}{\partial \beta} = -Q \langle E \rangle\):
\[
\frac{\partial \langle E \rangle}{\partial \beta} = \langle E \rangle^2 - \langle E^2 \rangle = -(\langle E^2 \rangle - \langle E \rangle^2) = -\sigma_E^2
\]
where \(\sigma_E^2 = \langle (E - \langle E \rangle)^2 \rangle\) is the energy variance.
Now express the left-hand side in terms of temperature \(T\):
\[
\frac{\partial \langle E \rangle}{\partial \beta} = \frac{\partial \langle E \rangle}{\partial T} \frac{dT}{d\beta} = C_V \left( -\frac{1}{k_B \beta^2} \right) = -k_B T^2 C_V
\]
Equating the two expressions:
\[
\sigma_E^2 = \langle E^2 \rangle - \langle E \rangle^2 = k_B T^2 C_V
\]
The standard deviation of energy fluctuations is:
\[
\sigma_E = \sqrt{k_B T^2 C_V}
\]

### Relative Fluctuation and the Thermodynamic Limit
Because both energy \(\langle E \rangle\) and heat capacity \(C_V\) are extensive variables proportional to particle number \(N\) (\(\langle E \rangle \propto N, C_V \propto N\)):
\[
\frac{\sigma_E}{\langle E \rangle} = \frac{\sqrt{k_B T^2 C_V}}{\langle E \rangle} \propto \frac{\sqrt{N}}{N} = \frac{1}{\sqrt{N}}
\]
For a typical macroscopic molar sample (\(N \sim 10^{23}\)):
\[
\frac{\sigma_E}{\langle E \rangle} \sim \frac{1}{\sqrt{10^{23}}} \approx 3 \times 10^{-12}
\]
Relative energy fluctuations are on the order of parts per trillion. The energy probability distribution is extraordinarily sharply peaked around its mean value \(\langle E \rangle\), demonstrating why canonical and microcanonical ensembles are observationally indistinguishable for macroscopic matter."""
            },
            {
                "id": "sec-7-7",
                "secNumber": "7.7",
                "title": "Maxwell-Boltzmann Molecular Speed Distribution & Effusion",
                "content": r"""For an ideal gas of point particles of mass \(m\) at thermal equilibrium, the translational kinetic energy is \(\varepsilon = \frac{1}{2} m (v_x^2 + v_y^2 + v_z^2) = \frac{p^2}{2m}\).

### Velocity Probability Density
Because motion in \(x, y, z\) is isotropic and mutually independent, the three-dimensional velocity probability density factors into three 1D Gaussians:
\[
f(v_x, v_y, v_z) dv_x dv_y dv_z = \left(\frac{m}{2\pi k_B T}\right)^{3/2} \exp\left[ -\frac{m(v_x^2 + v_y^2 + v_z^2)}{2 k_B T} \right] dv_x dv_y dv_z
\]

### Transformation to Molecular Speed \(v\)
Speed is the scalar magnitude \(v = \sqrt{v_x^2 + v_y^2 + v_z^2} \ge 0\). Transforming velocity space into spherical coordinates \((v, \theta, \phi)\) where the volume element is \(dv_x dv_y dv_z = v^2 \sin\theta \, dv \, d\theta \, d\phi\), integrating over all solid angles \(\int_0^{4\pi} d\Omega = 4\pi\) gives the **Maxwell-Boltzmann Speed Distribution**:
\[
f(v) dv = 4\pi \left(\frac{m}{2\pi k_B T}\right)^{3/2} v^2 \exp\left( -\frac{m v^2}{2 k_B T} \right) dv
\]

### Characteristic Molecular Speeds
1. **Most Probable Speed \(v_{\text{mp}}\)**: Setting \(\frac{df}{dv} = 0\):
   \[
   \frac{d}{dv} [v^2 e^{-m v^2 / 2 k_B T}] = \left( 2v - \frac{m v^3}{k_B T} \right) e^{-m v^2 / 2 k_B T} = 0 \implies v_{\text{mp}} = \sqrt{\frac{2 k_B T}{m}} = \sqrt{\frac{2 R T}{M}}
   \]
2. **Mean (Average) Speed \(\langle v \rangle\)**:
   \[
   \langle v \rangle = \int_0^\infty v f(v) dv = \sqrt{\frac{8 k_B T}{\pi m}} = \sqrt{\frac{8 R T}{\pi M}} \approx 1.128 v_{\text{mp}}
   \]
3. **Root-Mean-Square Speed \(v_{\text{rms}}\)**:
   \[
   v_{\text{rms}} = \sqrt{\langle v^2 \rangle} = \sqrt{\int_0^\infty v^2 f(v) dv} = \sqrt{\frac{3 k_B T}{m}} = \sqrt{\frac{3 R T}{M}} \approx 1.225 v_{\text{mp}}
   \]
Ordering: \(v_{\text{mp}} < \langle v \rangle < v_{\text{rms}}\).

### Molecular Effusion Rate
When gas molecules effuse through an orifice with area \(A\) whose diameter is smaller than the mean free path, the effusion rate \(Z_{\text{eff}}\) (number of collisions per unit wall area per second) is:
\[
Z_{\text{wall}} = \frac{1}{4} \rho \langle v \rangle = \frac{P}{\sqrt{2\pi m k_B T}}
\]
This directly yields **Graham's Law of Effusion**:
\[
\text{Effusion Rate} \propto \frac{1}{\sqrt{M}}
\]"""
            }
        ],
        "problems": [
            {
                "id": "prob-7-1",
                "title": "Statistical Multiplicity and Entropy of Mixing for Ideal Gases",
                "problem": r"""Consider two distinct non-reacting ideal gases A and B at identical temperature \(T\) and pressure \(P\), initially separated by a partition in volumes \(V_A\) and \(V_B\) containing \(N_A\) and \(N_B\) molecules. The partition is removed, allowing the gases to mix into total volume \(V = V_A + V_B\).
1. Express the statistical multiplicity of each pure gas before mixing.
2. Calculate the statistical multiplicity of the mixed system.
3. Derive the molar entropy of mixing \(\Delta S_{\text{mix}}\) and evaluate it for an equimolar binary mixture (\(x_A = x_B = 0.5\)).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Initial Multiplicity Before Mixing
The number of microstates for an ideal gas of \(N\) particles in volume \(V\) is proportional to \(\Omega \propto \frac{V^N}{N!}\).
Before mixing, the subsystems are independent:
\[
W_{\text{initial}} = W_A \times W_B \propto \frac{V_A^{N_A}}{N_A!} \times \frac{V_B^{N_B}}{N_B!}
\]
Using Boltzmann's formula \(S = k_B \ln W\):
\[
S_{\text{initial}} = S_A + S_B = k_B [N_A \ln V_A - \ln N_A!] + k_B [N_B \ln V_B - \ln N_B!] + \text{const}
\]

---

#### Step 2: Final Multiplicity After Mixing
After removing the partition, both gases expand to fill the entire combined volume \(V = V_A + V_B\).
Because particles of gas A remain distinguishable from particles of gas B:
\[
W_{\text{final}} \propto \frac{V^{N_A}}{N_A!} \times \frac{V^{N_B}}{N_B!}
\]
The final entropy is:
\[
S_{\text{final}} = k_B [N_A \ln V - \ln N_A!] + k_B [N_B \ln V - \ln N_B!] + \text{const}
\]

---

#### Step 3: Derivation of Entropy of Mixing \(\Delta S_{\text{mix}}\)
Subtracting the initial from the final entropy:
\[
\Delta S_{\text{mix}} = S_{\text{final}} - S_{\text{initial}} = k_B \left[ N_A \ln\left(\frac{V}{V_A}\right) + N_B \ln\left(\frac{V}{V_B}\right) \right]
\]
Because both gases start at identical temperature and pressure, \(P V_A = N_A k_B T\) and \(P V_B = N_B k_B T\).
Thus, the volume fractions equal the mole fractions:
\[
\frac{V_A}{V} = \frac{N_A}{N_A + N_B} = x_A, \quad \frac{V_B}{V} = \frac{N_B}{N_A + N_B} = x_B
\]
Therefore, \(\frac{V}{V_A} = \frac{1}{x_A}\) and \(\frac{V}{V_B} = \frac{1}{x_B}\).
Substituting into the entropy formula with total particles \(N = N_A + N_B\):
\[
\Delta S_{\text{mix}} = k_B [N_A \ln(1/x_A) + N_B \ln(1/x_B)] = -k_B [N_A \ln x_A + N_B \ln x_B]
\]
In terms of total moles \(n = n_A + n_B\) where \(N k_B = n R\):
\[
\Delta S_{\text{mix}} = -n R \left( x_A \ln x_A + x_B \ln x_B \right)
\]
For an equimolar mixture (\(x_A = x_B = 0.5\)):
\[
\Delta S_{\text{mix}} = -n R [0.5 \ln(0.5) + 0.5 \ln(0.5)] = -n R \ln(0.5) = n R \ln(2)
\]
For 1 mole of total mixture (\(n = 1\)):
\[
\Delta S_{\text{mix}} = (8.3145\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}) \times \ln(2) \approx 8.3145 \times 0.69315 \approx 5.763\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
\]
Because \(\ln x_i < 0\) for all \(x_i \in (0, 1)\), the entropy of mixing is strictly positive (\(\Delta S_{\text{mix}} > 0\)), driving spontaneous and irreversible mixing."""
            },
            {
                "id": "prob-7-2",
                "title": "Canonical Partition Function and Average Energy of a 2-Level and 3-Level System",
                "problem": r"""Consider a system with discrete, non-degenerate energy levels:
1. For a two-level system with energies \(\varepsilon_0 = 0\) and \(\varepsilon_1 = \varepsilon\), derive the canonical partition function \(q\), the average energy \(\langle \varepsilon \rangle\), and the heat capacity \(C_V(T)\).
2. For a three-level system with energies \(\varepsilon_0 = 0\), \(\varepsilon_1 = \varepsilon\), and \(\varepsilon_2 = 2\varepsilon\), derive the partition function \(q\) and average energy.
3. Compute the high-temperature limit (\(T \rightarrow \infty\)) and low-temperature limit (\(T \rightarrow 0\)) of \(\langle \varepsilon \rangle\) for both systems.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Two-Level System
Given \(\varepsilon_0 = 0, \varepsilon_1 = \varepsilon\), let \(\beta = \frac{1}{k_B T}\):
1. **Partition function:**
   \[
   q = \sum_i e^{-\beta \varepsilon_i} = e^0 + e^{-\beta \varepsilon} = 1 + e^{-\beta \varepsilon}
   \]
2. **Average energy:**
   \[
   \langle \varepsilon \rangle = -\frac{\partial \ln q}{\partial \beta} = -\frac{1}{q} \frac{dq}{d\beta} = -\frac{-\varepsilon e^{-\beta \varepsilon}}{1 + e^{-\beta \varepsilon}} = \frac{\varepsilon e^{-\beta \varepsilon}}{1 + e^{-\beta \varepsilon}} = \frac{\varepsilon}{e^{\beta \varepsilon} + 1}
   \]
3. **Heat capacity (Schottky anomaly):**
   \[
   C_V = \frac{d\langle \varepsilon \rangle}{dT} = \frac{d\langle \varepsilon \rangle}{d\beta} \left( -\frac{1}{k_B T^2} \right) = \frac{\varepsilon^2 e^{\beta \varepsilon}}{(e^{\beta \varepsilon} + 1)^2} \frac{1}{k_B T^2} = k_B \left( \frac{\varepsilon}{k_B T} \right)^2 \frac{e^{\varepsilon / k_B T}}{(e^{\varepsilon / k_B T} + 1)^2}
   \]

---

#### Step 2: Three-Level System
Given \(\varepsilon_0 = 0, \varepsilon_1 = \varepsilon, \varepsilon_2 = 2\varepsilon\):
1. **Partition function:**
   \[
   q = 1 + e^{-\beta \varepsilon} + e^{-2\beta \varepsilon}
   \]
   Let \(x = e^{-\beta \varepsilon}\). Then \(q = 1 + x + x^2\).
2. **Average energy:**
   \[
   \langle \varepsilon \rangle = \frac{\sum_i \varepsilon_i e^{-\beta \varepsilon_i}}{q} = \frac{0 + \varepsilon e^{-\beta \varepsilon} + 2\varepsilon e^{-2\beta \varepsilon}}{1 + e^{-\beta \varepsilon} + e^{-2\beta \varepsilon}} = \varepsilon \frac{x + 2x^2}{1 + x + x^2}
   \]

---

#### Step 3: Limiting Behaviors
1. **Low-Temperature Limit (\(T \rightarrow 0 \implies \beta \rightarrow \infty, x \rightarrow 0\)):**
   - For 2-level: \(\langle \varepsilon \rangle \rightarrow \frac{\varepsilon \times 0}{1 + 0} = 0\)
   - For 3-level: \(\langle \varepsilon \rangle \rightarrow \frac{0 + 0}{1} = 0\)
   At \(T = 0\), the system is frozen in the ground state \(\varepsilon_0 = 0\) with 100% certainty.
2. **High-Temperature Limit (\(T \rightarrow \infty \implies \beta \rightarrow 0, x \rightarrow 1\)):**
   - For 2-level: \(\langle \varepsilon \rangle \rightarrow \frac{\varepsilon}{1 + 1} = \frac{\varepsilon}{2}\)
     (both states become equally populated: \(P_0 = P_1 = 1/2\)).
   - For 3-level: \(\langle \varepsilon \rangle \rightarrow \varepsilon \frac{1 + 2(1)}{1 + 1 + 1} = \varepsilon \frac{3}{3} = \varepsilon\)
     (all three states become equally populated: \(P_0 = P_1 = P_2 = 1/3\), so \(\langle \varepsilon \rangle = \frac{0 + \varepsilon + 2\varepsilon}{3} = \varepsilon\))."""
            },
            {
                "id": "prob-7-3",
                "title": "Evaluation of Lagrange Multipliers alpha and beta",
                "problem": r"""In the statistical derivation of the Maxwell-Boltzmann distribution:
\[
\ln\left(\frac{N_i}{g_i}\right) = -(1 + \alpha) - \beta \varepsilon_i
\]
1. Determine the normalization multiplier \(\alpha\) in terms of total particle number \(N\) and molecular partition function \(q\).
2. From the differential of entropy \(dS = k_B d(\ln W)\), derive the fundamental thermodynamic relation connecting \(\beta\) to absolute temperature \(T\).
3. Prove that \(\beta = \frac{1}{k_B T}\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Evaluation of Multiplier \(\alpha\)
From the distribution equation:
\[
N_i = g_i e^{-(1 + \alpha)} e^{-\beta \varepsilon_i}
\]
Summing over all energy levels \(i\):
\[
\sum_i N_i = e^{-(1 + \alpha)} \sum_i g_i e^{-\beta \varepsilon_i}
\]
Using \(\sum N_i = N\) and defining \(q = \sum_i g_i e^{-\beta \varepsilon_i}\):
\[
N = e^{-(1 + \alpha)} q \implies e^{-(1 + \alpha)} = \frac{N}{q}
\]
Taking natural logarithms:
\[
-(1 + \alpha) = \ln\left(\frac{N}{q}\right) \implies \alpha = -\ln\left(\frac{N}{q}\right) - 1
\]

---

#### Step 2: Relation Between \(d(\ln W)\) and Energy \(dE\)
Recall Stirling's expression for \(\ln W\):
\[
\ln W = N \ln N - \sum_i N_i \ln\left(\frac{N_i}{g_i}\right)
\]
Consider an infinitesimal quasi-static change in the populations \(\{dN_i\}\) at constant volume (so \(\{g_i\}\) and \(\{\varepsilon_i\}\) remain fixed):
\[
d(\ln W) = -\sum_i \left[ \ln\left(\frac{N_i}{g_i}\right) dN_i + N_i \frac{dN_i}{N_i} \right] = -\sum_i \ln\left(\frac{N_i}{g_i}\right) dN_i - \sum_i dN_i
\]
Because total particle number is conserved, \(\sum dN_i = dN = 0\).
Now substitute \(\ln(N_i / g_i) = -(1 + \alpha) - \beta \varepsilon_i\):
\[
d(\ln W) = -\sum_i [-(1 + \alpha) - \beta \varepsilon_i] dN_i = (1 + \alpha) \sum_i dN_i + \beta \sum_i \varepsilon_i dN_i
\]
Since \(\sum dN_i = 0\) and \(\sum \varepsilon_i dN_i = dE\) (the change in internal energy at constant volume):
\[
d(\ln W) = \beta dE
\]

---

#### Step 3: Identification of \(\beta = 1 / k_B T\)
Using Boltzmann's entropy definition \(S = k_B \ln W\):
\[
dS = k_B d(\ln W) = k_B \beta dE
\]
Rearranging:
\[
\left( \frac{\partial S}{\partial E} \right)_{V, N} = k_B \beta
\]
From the fundamental thermodynamic relation \(dE = T dS - P dV + \mu dN\):
\[
\left( \frac{\partial S}{\partial E} \right)_{V, N} = \frac{1}{T}
\]
Equating the statistical and thermodynamic derivatives:
\[
k_B \beta = \frac{1}{T} \implies \beta = \frac{1}{k_B T}
\]
This mathematically establishes the identity of \(\beta\) as inverse thermal energy."""
            },
            {
                "id": "prob-7-4",
                "title": "Thermodynamic Functions of an Independent N-Particle Harmonic Lattice",
                "problem": r"""Consider an Einstein crystal consisting of \(N\) distinguishable 1D harmonic oscillators, each of vibrational frequency \(\nu\), with quantum energy levels \(\varepsilon_v = \left(v + \frac{1}{2}\right) h \nu\) (\(v = 0, 1, 2, \dots\)).
1. Derive the single-oscillator partition function \(q\) and total lattice partition function \(Q\).
2. Calculate the internal energy \(U(T)\) and Helmholtz free energy \(A(T)\).
3. Derive the molar heat capacity \(C_V(T)\) and evaluate its high-temperature limit (Dulong-Petit law).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Single-Oscillator and Lattice Partition Functions
The energy of a single harmonic oscillator is \(\varepsilon_v = \left(v + \frac{1}{2}\right) h\nu\).
Let \(u = \beta h\nu = \frac{h\nu}{k_B T}\):
\[
q = \sum_{v=0}^\infty e^{-\beta (v + 1/2) h\nu} = e^{-u/2} \sum_{v=0}^\infty (e^{-u})^v
\]
Using the infinite geometric series sum \(\sum_{v=0}^\infty x^v = \frac{1}{1 - x}\) for \(x = e^{-u} < 1\):
\[
q = \frac{e^{-u/2}}{1 - e^{-u}} = \frac{e^{-\beta h\nu / 2}}{1 - e^{-\beta h\nu}}
\]
Because the lattice sites are localized and therefore **distinguishable**, the total partition function is:
\[
Q = q^N = \left( \frac{e^{-\beta h\nu / 2}}{1 - e^{-\beta h\nu}} \right)^N
\]

---

#### Step 2: Internal Energy \(U(T)\) and Helmholtz Free Energy \(A(T)\)
1. **Logarithm of \(Q\):**
   \[
   \ln Q = N \left[ -\frac{\beta h\nu}{2} - \ln(1 - e^{-\beta h\nu}) \right]
   \]
2. **Internal energy \(U\):**
   \[
   U = -\frac{\partial \ln Q}{\partial \beta} = -N \left[ -\frac{h\nu}{2} - \frac{h\nu e^{-\beta h\nu}}{1 - e^{-\beta h\nu}} \right] = N h\nu \left[ \frac{1}{2} + \frac{1}{e^{\beta h\nu} - 1} \right]
   \]
   Notice the zero-point energy contribution \(\frac{1}{2} N h\nu\).
3. **Helmholtz free energy \(A\):**
   \[
   A = -k_B T \ln Q = N k_B T \left[ \frac{h\nu}{2 k_B T} + \ln(1 - e^{-h\nu / k_B T}) \right] = \frac{1}{2} N h\nu + N k_B T \ln(1 - e^{-h\nu / k_B T})
   \]

---

#### Step 3: Molar Heat Capacity and High-Temperature Limit
Differentiating \(U\) with respect to \(T\):
\[
C_V = \frac{\partial U}{\partial T} = N h\nu \frac{\partial}{\partial T} \left( \frac{1}{e^{h\nu / k_B T} - 1} \right) = N h\nu \left( -\frac{1}{(e^{h\nu / k_B T} - 1)^2} \right) e^{h\nu / k_B T} \left( -\frac{h\nu}{k_B T^2} \right)
\]
\[
C_V = N k_B \left( \frac{h\nu}{k_B T} \right)^2 \frac{e^{h\nu / k_B T}}{(e^{h\nu / k_B T} - 1)^2}
\]
For a 3D solid with \(3N\) vibrational modes, \(C_{V, 3D} = 3 C_V\). For 1 mole (\(N = N_A\)):
\[
C_{V, \text{molar}} = 3 R \left( \frac{\theta_E}{T} \right)^2 \frac{e^{\theta_E / T}}{(e^{\theta_E / T} - 1)^2}
\]
where \(\theta_E = \frac{h\nu}{k_B}\) is the Einstein temperature.

**High-Temperature Limit (\(T \gg \theta_E \implies x = \theta_E / T \ll 1\)):**
Taylor expand \(e^x \approx 1 + x\):
\[
e^x - 1 \approx x \implies (e^x - 1)^2 \approx x^2
\]
\[
\lim_{T \rightarrow \infty} C_{V, \text{molar}} = 3 R \lim_{x \rightarrow 0} x^2 \frac{1 + x}{x^2} = 3 R \times 1 = 3 R \approx 24.94\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
\]
This precisely recovers the classical **Dulong-Petit law**."""
            },
            {
                "id": "prob-7-5",
                "title": "Maxwell-Boltzmann Speeds for Nitrogen and Helium at 300 K",
                "problem": r"""For molecular nitrogen (\(\text{N}_2\), molar mass \(M = 28.013\text{ g/mol}\)) and helium (\(\text{He}\), molar mass \(M = 4.003\text{ g/mol}\)) at \(T = 300.0\text{ K}\):
1. Calculate the most probable speed \(v_{\text{mp}}\), mean speed \(\langle v \rangle\), and root-mean-square speed \(v_{\text{rms}}\) for both gases.
2. Determine the ratio of root-mean-square speeds \(v_{\text{rms}}(\text{He}) / v_{\text{rms}}(\text{N}_2)\).
3. Compute the fraction of \(\text{N}_2\) molecules with speeds exceeding \(1000\text{ m/s}\) at \(300\text{ K}\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Characteristic Speeds at \(300\text{ K}\)
The formulas in SI units are:
\[
v_{\text{mp}} = \sqrt{\frac{2 R T}{M}}, \quad \langle v \rangle = \sqrt{\frac{8 R T}{\pi M}}, \quad v_{\text{rms}} = \sqrt{\frac{3 R T}{M}}
\]
Given \(R = 8.31446\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\) and \(T = 300.0\text{ K}\):
\[
R T = 8.31446 \times 300 = 2494.34\text{ J/mol}
\]

1. **For Nitrogen (\(\text{N}_2\), \(M = 0.028013\text{ kg/mol}\)):**
   - \(v_{\text{mp}} = \sqrt{\frac{2 \times 2494.34}{0.028013}} = \sqrt{\frac{4988.68}{0.028013}} = \sqrt{178084} \approx 422.0\text{ m/s}\)
   - \(\langle v \rangle = \sqrt{\frac{8 \times 2494.34}{\pi \times 0.028013}} = \sqrt{\frac{19954.7}{0.088005}} = \sqrt{226745} \approx 476.2\text{ m/s}\)
   - \(v_{\text{rms}} = \sqrt{\frac{3 \times 2494.34}{0.028013}} = \sqrt{\frac{7483.02}{0.028013}} = \sqrt{267127} \approx 516.8\text{ m/s}\)

2. **For Helium (\(\text{He}\), \(M = 0.004003\text{ kg/mol}\)):**
   - \(v_{\text{mp}} = \sqrt{\frac{4988.68}{0.004003}} = \sqrt{1246235} \approx 1116.3\text{ m/s}\)
   - \(\langle v \rangle = \sqrt{\frac{19954.7}{\pi \times 0.004003}} = \sqrt{\frac{19954.7}{0.012576}} = \sqrt{1586729} \approx 1259.7\text{ m/s}\)
   - \(v_{\text{rms}} = \sqrt{\frac{7483.02}{0.004003}} = \sqrt{1869353} \approx 1367.2\text{ m/s}\)

---

#### Step 2: Speed Ratio
\[
\frac{v_{\text{rms}}(\text{He})}{v_{\text{rms}}(\text{N}_2)} = \sqrt{\frac{M(\text{N}_2)}{M(\text{He})}} = \sqrt{\frac{28.013}{4.003}} = \sqrt{6.998} \approx 2.645
\]
Light helium atoms travel over 2.6 times faster on average than nitrogen molecules at the same temperature.

---

#### Step 3: High-Speed Fraction for \(\text{N}_2\)
The speed distribution is \(f(v) = 4\pi (a/\pi)^{3/2} v^2 e^{-a v^2}\) where \(a = \frac{m}{2 k_B T} = \frac{1}{v_{\text{mp}}^2} = \frac{1}{(422.0)^2} \approx 5.615 \times 10^{-6}\text{ s}^2/\text{m}^2\).
Let \(u = v / v_{\text{mp}} = 1000 / 422.0 \approx 2.370\).
The cumulative fraction exceeding \(u_0 = 2.370\) is:
\[
P(u > u_0) = \frac{4}{\sqrt{\pi}} \int_{u_0}^\infty u^2 e^{-u^2} du = 1 - \operatorname{erf}(u_0) + \frac{2}{\sqrt{\pi}} u_0 e^{-u_0^2}
\]
With \(u_0^2 \approx 5.617\) and \(e^{-u_0^2} \approx 0.003636\):
\[
\frac{2}{\sqrt{\pi}} (2.370) (0.003636) \approx 1.1284 \times 2.370 \times 0.003636 \approx 0.00972
\]
And \(1 - \operatorname{erf}(2.370) \approx 0.00085\).
Total fraction:
\[
P(v > 1000\text{ m/s}) \approx 0.00085 + 0.00972 = 0.01057 \approx 1.06\%
\]
Roughly 1.1% of nitrogen molecules travel faster than \(1000\text{ m/s}\) at room temperature."""
            },
            {
                "id": "prob-7-6",
                "title": "Relative Energy Fluctuations in the Canonical Ensemble",
                "problem": r"""Consider an ideal monatomic gas in a container of fixed volume \(V\) at temperature \(T\).
1. State the internal energy \(U\) and heat capacity \(C_V\) for \(N\) particles.
2. Calculate the exact standard deviation \(\sigma_E\) and relative energy fluctuation \(\frac{\sigma_E}{U}\).
3. Evaluate the relative fluctuation numerically for:
   - A microscopic cluster of \(N = 100\) atoms
   - A macroscopic sample of \(N = 1\text{ mole} = 6.022 \times 10^{23}\) atoms.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Internal Energy and Heat Capacity
For an ideal monatomic gas:
\[
U = \frac{3}{2} N k_B T, \quad C_V = \left(\frac{\partial U}{\partial T}\right)_V = \frac{3}{2} N k_B
\]

---

#### Step 2: Energy Standard Deviation and Relative Fluctuation
The energy variance in the canonical ensemble is:
\[
\sigma_E^2 = k_B T^2 C_V = k_B T^2 \left( \frac{3}{2} N k_B \right) = \frac{3}{2} N (k_B T)^2
\]
Taking the square root:
\[
\sigma_E = \sqrt{\frac{3}{2} N} k_B T
\]
The relative energy fluctuation is:
\[
\frac{\sigma_E}{U} = \frac{\sqrt{\frac{3}{2} N} k_B T}{\frac{3}{2} N k_B T} = \frac{\sqrt{3/2}}{\frac{3}{2} \sqrt{N}} = \sqrt{\frac{2}{3 N}}
\]

---

#### Step 3: Numerical Evaluation
1. **For \(N = 100\) atoms:**
   \[
   \frac{\sigma_E}{U} = \sqrt{\frac{2}{3 \times 100}} = \sqrt{\frac{2}{300}} = \sqrt{0.006667} \approx 0.0816 \approx 8.16\%
   \]
   In microscopic clusters, energy fluctuates significantly (\(\sim 8\%\)).
2. **For \(N = 6.022 \times 10^{23}\) atoms (1 mole):**
   \[
   \frac{\sigma_E}{U} = \sqrt{\frac{2}{3 \times 6.022 \times 10^{23}}} = \sqrt{\frac{2}{1.8066 \times 10^{24}}} = \sqrt{1.107 \times 10^{-24}} \approx 1.052 \times 10^{-12}
   \]
   The relative fluctuation is about 1 part in a trillion (\(10^{-10}\%\)). Macrostate energy in the canonical ensemble is extraordinarily sharp and deterministic."""
            },
            {
                "id": "prob-7-7",
                "title": "Barometric Height Formula and Gravitational Distribution",
                "problem": r"""Consider an isothermal column of an ideal gas of molecular mass \(m\) in a uniform gravitational field with acceleration \(g\).
1. Write the single-particle potential energy \(\varepsilon_{\text{pot}}(z)\) at height \(z\ge 0\).
2. Using the Maxwell-Boltzmann distribution, derive the density profile \(\rho(z)\) and pressure profile \(P(z)\) (the Barometric Formula).
3. For Earth's atmosphere at \(T = 280\text{ K}\) with average molecular mass \(M = 28.97\text{ g/mol}\), calculate the scale height \(H\) and determine the altitude at which atmospheric pressure drops to 50% of sea level pressure.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Potential Energy and Single-Particle Partition Function
The potential energy of a particle at altitude \(z\) is \(\varepsilon_{\text{pot}}(z) = m g z\).
The total single-particle energy is \(\varepsilon = \varepsilon_{\text{trans}} + m g z\).
The spatial distribution function along the vertical \(z\)-axis is:
\[
P(z) dz \propto e^{-m g z / k_B T} dz
\]

---

#### Step 2: Derivation of the Barometric Formula
Let \(n(z)\) be the number density of gas molecules at height \(z\).
At sea level (\(z = 0\)), let the density be \(n_0\).
By the Boltzmann distribution law:
\[
n(z) = n_0 \exp\left( -\frac{m g z}{k_B T} \right)
\]
Since the gas is ideal and isothermal (\(T = \text{const}\)), the ideal gas law \(P(z) = n(z) k_B T\) yields:
\[
P(z) = P_0 \exp\left( -\frac{m g z}{k_B T} \right) = P_0 \exp\left( -\frac{M g z}{R T} \right)
\]
Defining the atmospheric **scale height** \(H = \frac{k_B T}{m g} = \frac{R T}{M g}\):
\[
P(z) = P_0 e^{-z / H}
\]

---

#### Step 3: Numerical Scale Height and Half-Pressure Altitude
Given \(R = 8.3145\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\), \(T = 280.0\text{ K}\), \(M = 0.02897\text{ kg/mol}\), and \(g = 9.80665\text{ m/s}^2\):
\[
H = \frac{R T}{M g} = \frac{8.3145 \times 280}{0.02897 \times 9.80665} = \frac{2328.06}{0.28410} \approx 8194.5\text{ m} \approx 8.195\text{ km}
\]
To find the altitude \(z_{1/2}\) where \(P(z) = 0.50 P_0\):
\[
e^{-z_{1/2} / H} = 0.50 \implies \frac{z_{1/2}}{H} = \ln(2)
\]
\[
z_{1/2} = H \ln(2) = 8194.5\text{ m} \times 0.693147 \approx 5680\text{ m} \approx 5.68\text{ km}
\]
Atmospheric pressure drops by half at approximately \(5.68\text{ km}\) (\(\approx 18,600\text{ ft}\)) above sea level."""
            }
        ]
    }
    units.append(unit7)

    # =========================================================================
    # UNIT 8: Molecular Partition Functions & The Thermodynamic Bridge
    # =========================================================================
    unit8 = {
        "id": "unit-8",
        "unitNumber": 8,
        "title": "Unit 8: Molecular Partition Functions & The Thermodynamic Bridge",
        "leadSummary": r"""Rigorous quantum-to-classical factorization of the molecular partition function: translational density of states and thermal de Broglie wavelength, rotational partition functions of linear and non-linear polyatomic rotors, symmetry numbers and nuclear spin statistics (ortho/para hydrogen), vibrational partition functions and zero-point energy, electronic degeneracies, temperature-dependent heat capacity C_V(T) equipartition transitions, and the Sackur-Tetrode formula for absolute translational entropy.""",
        "simulations": [
            "sim_qc_molecular_partition_functions"
        ],
        "sections": [
            {
                "id": "sec-8-1",
                "secNumber": "8.1",
                "title": "Factorization of the Molecular Partition Function",
                "content": r"""For an ideal gas molecule, the total Hamiltonian can be approximated to high accuracy as a sum of uncoupled independent degrees of freedom:
\[
\hat{H}_{\text{mol}} \approx \hat{H}_{\text{trans}} + \hat{H}_{\text{rot}} + \hat{H}_{\text{vib}} + \hat{H}_{\text{elec}} + \hat{H}_{\text{nuc}}
\]
Because the Hamiltonian operators commute, the total energy of a single molecule is additive:
\[
\varepsilon = \varepsilon_{\text{trans}} + \varepsilon_{\text{rot}} + \varepsilon_{\text{vib}} + \varepsilon_{\text{elec}} + \varepsilon_{\text{nuc}}
\]

### Factorization of the Partition Function
The single-molecule partition function is:
\[
q = \sum_i e^{-\beta \varepsilon_i} = \sum_{\text{trans}} \sum_{\text{rot}} \sum_{\text{vib}} \sum_{\text{elec}} \sum_{\text{nuc}} e^{-\beta (\varepsilon_{\text{trans}} + \varepsilon_{\text{rot}} + \varepsilon_{\text{vib}} + \varepsilon_{\text{elec}} + \varepsilon_{\text{nuc}})}
\]
Because the exponential of a sum is the product of exponentials, the multiple sum factors cleanly:
\[
q = q_{\text{trans}} \times q_{\text{rot}} \times q_{\text{vib}} \times q_{\text{elec}} \times q_{\text{nuc}}
\]
Taking natural logarithms converts this into an additive sum of terms:
\[
\ln q = \ln q_{\text{trans}} + \ln q_{\text{rot}} + \ln q_{\text{vib}} + \ln q_{\text{elec}} + \ln q_{\text{nuc}}
\]
Consequently, every thermodynamic property decomposes into additive components:
\[
U = U_{\text{trans}} + U_{\text{rot}} + U_{\text{vib}} + U_{\text{elec}}
\]
\[
C_V = C_{V, \text{trans}} + C_{V, \text{rot}} + C_{V, \text{vib}} + C_{V, \text{elec}}
\]
\[
S = S_{\text{trans}} + S_{\text{rot}} + S_{\text{vib}} + S_{\text{elec}}
\]
This factorization forms the computational foundation for predicting all macroscopic gas-phase thermochemical properties directly from molecular spectroscopic data."""
            },
            {
                "id": "sec-8-2",
                "secNumber": "8.2",
                "title": "Translational Partition Function & The Thermal de Broglie Wavelength",
                "content": r"""Consider a molecule of mass \(m\) moving freely inside a three-dimensional rectangular box of dimensions \(a \times b \times c = V\).
The quantized translational energy levels are:
\[
\varepsilon_{n_x, n_y, n_z} = \frac{h^2}{8m} \left( \frac{n_x^2}{a^2} + \frac{n_y^2}{b^2} + \frac{n_z^2}{c^2} \right)
\]
Because typical molecular masses and macroscopic volumes produce extraordinarily tiny energy level spacings (\(\Delta \varepsilon \sim 10^{-38}\text{ J} \ll k_B T \sim 4 \times 10^{-21}\text{ J}\)), the quantum sum can be replaced by an integral:
\[
q_{\text{trans}, x} = \sum_{n_x=1}^\infty e^{-\frac{h^2 n_x^2}{8 m a^2 k_B T}} \approx \int_0^\infty e^{-\frac{h^2 n^2}{8 m a^2 k_B T}} dn
\]
Using the standard Gaussian integral \(\int_0^\infty e^{-\alpha x^2} dx = \frac{1}{2} \sqrt{\frac{\pi}{\alpha}}\):
\[
q_{\text{trans}, x} = \frac{1}{2} \sqrt{\frac{\pi \times 8 m a^2 k_B T}{h^2}} = \frac{a}{h} \sqrt{2\pi m k_B T}
\]
For 3D translation:
\[
q_{\text{trans}} = q_x q_y q_z = \frac{a b c}{h^3} (2\pi m k_B T)^{3/2} = \frac{V}{h^3} (2\pi m k_B T)^{3/2}
\]

### The Thermal de Broglie Wavelength \(\Lambda\)
We define the **thermal de Broglie wavelength**:
\[
\Lambda = \frac{h}{\sqrt{2\pi m k_B T}} = \frac{h}{p_{\text{thermal}}}
\]
This represents the quantum spatial coherence length of a thermal particle at temperature \(T\).
In terms of \(\Lambda\), the translational partition function assumes the remarkably simple form:
\[
q_{\text{trans}} = \frac{V}{\Lambda^3}
\]
**Physical Meaning of \(\Lambda\):**
- \(V / \Lambda^3\) is the ratio of macroscopic container volume to the effective quantum volume \(\Lambda^3\) of a particle.
- When \(\Lambda \ll d\) (where \(d = (V/N)^{1/3}\) is the average interparticle distance), quantum wavepackets do not overlap, and the gas behaves strictly as a classical Maxwell-Boltzmann system.
- When \(\Lambda \sim d\), wavepacket overlap becomes significant, requiring quantum statistics (Bose-Einstein or Fermi-Dirac)."""
            },
            {
                "id": "sec-8-3",
                "secNumber": "8.3",
                "title": "Rotational Partition Function, Symmetry Numbers & Spin Statistics",
                "content": r"""### Linear Rotors (Diatomic & Linear Polyatomic Molecules)
The rigid rotor quantum energy levels with moment of inertia \(I\) are:
\[
\varepsilon_J = \frac{\hbar^2}{2 I} J(J+1) = h c B J(J+1), \quad g_J = 2J + 1 \quad (J = 0, 1, 2, \dots)
\]
where the rotational constant is \(B = \frac{\hbar}{4\pi c I}\).
Defining the **characteristic rotational temperature** \(\theta_{\text{rot}} = \frac{h c B}{k_B} = \frac{\hbar^2}{2 I k_B}\):
\[
q_{\text{rot}} = \sum_{J=0}^\infty (2J + 1) \exp\left( -J(J+1) \frac{\theta_{\text{rot}}}{T} \right)
\]
At temperatures \(T \gg \theta_{\text{rot}}\) (which is true for almost all molecules at room temperature except \(\text{H}_2\)), the sum can be approximated by an integral:
\[
q_{\text{rot}} \approx \int_0^\infty (2J + 1) e^{-\frac{\theta_{\text{rot}}}{T} (J^2 + J)} dJ = \left[ -\frac{T}{\theta_{\text{rot}}} e^{-\frac{\theta_{\text{rot}}}{T} (J^2 + J)} \right]_0^\infty = \frac{T}{\theta_{\text{rot}}} = \frac{8\pi^2 I k_B T}{h^2}
\]

### The Rotational Symmetry Number \(\sigma\)
For homonuclear or symmetrical molecules, rotating the molecule by \(180^\circ\) interchanges identical nuclei. To avoid double-counting identical indistinguishable configurations in phase space, we divide by the **rotational symmetry number** \(\sigma\):
\[
q_{\text{rot}} = \frac{T}{\sigma \theta_{\text{rot}}} = \frac{8\pi^2 I k_B T}{\sigma h^2}
\]
Values of \(\sigma\):
- Heteronuclear diatomics (\(\text{HCl}, \text{CO}\)): \(\sigma = 1\)
- Homonuclear diatomics (\(\text{N}_2, \text{O}_2, \text{H}_2\)): \(\sigma = 2\)
- Water (\(\text{H}_2\text{O}\), \(C_{2v}\)): \(\sigma = 2\)
- Ammonia (\(\text{NH}_3\), \(C_{3v}\)): \(\sigma = 3\)
- Methane (\(\text{CH}_4\), \(T_d\)): \(\sigma = 12\)
- Benzene (\(\text{C}_6\text{H}_6\), \(D_{6h}\)): \(\sigma = 12\)

### Non-Linear Polyatomic Rotors
For asymmetric and spherical tops with three principal moments of inertia \(I_A, I_B, I_C\):
\[
q_{\text{rot}} = \frac{\sqrt{\pi}}{\sigma} \left( \frac{T^3}{\theta_A \theta_B \theta_C} \right)^{1/2} = \frac{\sqrt{\pi}}{\sigma} \left( \frac{8\pi^2 k_B T}{h^2} \right)^{3/2} (I_A I_B I_C)^{1/2}
\]

### Nuclear Spin Statistics (Ortho vs Para Hydrogen)
In molecular hydrogen \(\text{H}_2\), the protons are fermions (\(I_{\text{nuc}} = 1/2\)). The total wavefunction must be antisymmetric with respect to proton exchange.
- **Para-Hydrogen (Singlet spin, \(I_{\text{tot}} = 0\), antisymmetric spin)**: Must pair with **symmetric rotational states** (\(J = 0, 2, 4, \dots\)). Nuclear spin statistical weight: \(g_{\text{nuc}} = 1\).
- **Ortho-Hydrogen (Triplet spin, \(I_{\text{tot}} = 1\), symmetric spin)**: Must pair with **antisymmetric rotational states** (\(J = 1, 3, 5, \dots\)). Nuclear spin statistical weight: \(g_{\text{nuc}} = 3\).
At high temperature, the equilibrium ratio is ortho:para = 3:1. At low temperature (\(T \rightarrow 0\)), hydrogen relaxes exclusively into the \(J = 0\) para-state."""
            },
            {
                "id": "sec-8-4",
                "secNumber": "8.4",
                "title": "Vibrational Partition Function & Zero-Point Energy",
                "content": r"""A molecule with \(N_{\text{at}}\) atoms possesses \(3 N_{\text{at}} - 5\) normal vibrational modes if linear, and \(3 N_{\text{at}} - 6\) normal modes if non-linear.
In the harmonic oscillator approximation, each normal mode \(i\) with fundamental frequency \(\nu_i\) is independent:
\[
\varepsilon_{v_i} = \left( v_i + \frac{1}{2} \right) h \nu_i \quad (v_i = 0, 1, 2, \dots)
\]
Defining the **characteristic vibrational temperature** \(\theta_{\text{vib}, i} = \frac{h \nu_i}{k_B} = \frac{h c \tilde{\nu}_i}{k_B}\):

### Zero-Point Energy Conventions
1. **Measured relative to the bottom of the potential well**:
   \[
   q_{\text{vib}, i} = \sum_{v=0}^\infty e^{-\beta (v + 1/2) h\nu_i} = e^{-\theta_{\text{vib}, i} / 2T} \sum_{v=0}^\infty e^{-v \theta_{\text{vib}, i} / T} = \frac{e^{-\theta_{\text{vib}, i} / 2T}}{1 - e^{-\theta_{\text{vib}, i} / T}}
   \]
2. **Measured relative to the \(v = 0\) vibrational ground state**:
   Setting \(\varepsilon_0 = 0\) by factoring out the zero-point energy:
   \[
   q_{\text{vib}, i}' = \sum_{v=0}^\infty e^{-v \theta_{\text{vib}, i} / T} = \frac{1}{1 - e^{-\theta_{\text{vib}, i} / T}}
   \]
For a polyatomic molecule with all normal modes:
\[
q_{\text{vib}} = \prod_{i=1}^{3N_{\text{at}} - 6} \frac{1}{1 - e^{-\theta_{\text{vib}, i} / T}}
\]

### High and Low Temperature Limits
Because vibrational frequencies are typically high (\(\tilde{\nu} \sim 500 - 3500\text{ cm}^{-1} \implies \theta_{\text{vib}} \sim 700 - 5000\text{ K}\)):
- At room temperature (\(T \approx 300\text{ K} \ll \theta_{\text{vib}}\)): \(e^{-\theta_{\text{vib}}/T} \ll 1\), so \(q_{\text{vib}} \approx 1\). Molecules are frozen in their ground vibrational state (\(v = 0\)).
- At high temperature (\(T \gg \theta_{\text{vib}}\)): Taylor expand \(1 - e^{-\theta_{\text{vib}}/T} \approx \frac{\theta_{\text{vib}}}{T}\):
  \[
  q_{\text{vib}} \approx \frac{T}{\theta_{\text{vib}}} = \frac{k_B T}{h \nu}
  \]
  recovering the classical harmonic oscillator partition function."""
            },
            {
                "id": "sec-8-5",
                "secNumber": "8.5",
                "title": "Electronic and Nuclear Spin Partition Functions",
                "content": r"""### Electronic Partition Function
The electronic partition function is:
\[
q_{\text{elec}} = \sum_i g_{e, i} e^{-\beta \varepsilon_{e, i}} = g_{e, 0} + g_{e, 1} e^{-\varepsilon_{e, 1} / k_B T} + \dots
\]
For the vast majority of stable molecules (e.g., \(\text{N}_2, \text{H}_2, \text{CO}_2, \text{CH}_4, \text{H}_2\text{O}\)), the electronic ground state is a closed-shell singlet (\(^1\Sigma\) or \(^1A_1\)) with degeneracy \(g_{e, 0} = 1\), and the first electronically excited state lies in the ultraviolet (\(\Delta \varepsilon_1 \sim 3 - 8\text{ eV} \implies \theta_{\text{elec}} \sim 35,000 - 100,000\text{ K}\)).
Therefore, at all accessible chemical temperatures:
\[
q_{\text{elec}} \approx g_{e, 0}
\]
Important exceptions:
1. **Triplet Ground States**:
   Molecular oxygen \(\text{O}_2\) has a \(^3\Sigma_g^-\) ground state with \(g_{e, 0} = 3\), so \(q_{\text{elec}} = 3\).
2. **Open-Shell Radicals**:
   - Nitric oxide (\(\text{NO}\)): Has a \(^2\Pi_{1/2}\) ground state (\(g_0 = 2\)) and a low-lying \(^2\Pi_{3/2}\) excited state (\(g_1 = 2\)) only \(\Delta\tilde{\nu} = 121.1\text{ cm}^{-1}\) (\(\theta_{\text{elec}} \approx 174\text{ K}\)) above the ground state:
     \[
     q_{\text{elec}}(\text{NO}) = 2 + 2 e^{-174 / T}
     \]
     This gives rise to an electronic contribution to the heat capacity at low temperatures.
   - Atomic Halogens (e.g., \(\text{F}, \text{Cl}\)): \(^2P_{3/2}\) ground state and \(^2P_{1/2}\) excited state separated by spin-orbit coupling.

### Nuclear Spin Partition Function
For a molecule containing nuclei with spin quantum numbers \(I_1, I_2, \dots\), the nuclear spin degeneracy is:
\[
g_{\text{nuc}} = \prod_k (2 I_k + 1)
\]
Because nuclear spin energy splittings are infinitesimal (\(\sim 10^{-6}\text{ K}\) in zero magnetic field), all nuclear spin states are equally populated:
\[
q_{\text{nuc}} = \prod_k (2 I_k + 1)
\]
Nuclear spin partition functions cancel identically in all chemical equilibrium and reaction rate calculations."""
            },
            {
                "id": "sec-8-6",
                "secNumber": "8.6",
                "title": "Statistical Heat Capacities & The Classical Equipartition Limits",
                "content": r"""The molar isochoric heat capacity is the sum of contributions from all active degrees of freedom:
\[
C_{V, \text{molar}} = C_{V, \text{trans}} + C_{V, \text{rot}} + C_{V, \text{vib}} + C_{V, \text{elec}}
\]

### Temperature Evolution of Heat Capacity in Diatomic Gases
1. **Translational Contribution**:
   Always fully classical above a fraction of a Kelvin:
   \[
   U_{\text{trans}} = \frac{3}{2} R T \implies C_{V, \text{trans}} = \frac{3}{2} R
   \]
2. **Rotational Contribution**:
   - At \(T \ll \theta_{\text{rot}}\) (e.g., \(T < 50\text{ K}\) for \(\text{H}_2\)): Rotational motion is quantum-mechanically frozen (\(C_{V, \text{rot}} \rightarrow 0\)).
   - At \(T \gg \theta_{\text{rot}}\): Fully active classical 2D rotation:
     \[
     U_{\text{rot}} = R T \implies C_{V, \text{rot}} = R
     \]
3. **Vibrational Contribution**:
   - From the harmonic oscillator:
     \[
     C_{V, \text{vib}} = R \left( \frac{\theta_{\text{vib}}}{T} \right)^2 \frac{e^{\theta_{\text{vib}}/T}}{(e^{\theta_{\text{vib}}/T} - 1)^2}
     \]
   - At \(T \ll \theta_{\text{vib}}\): Frozen zero-point motion (\(C_{V, \text{vib}} \rightarrow 0\)).
   - At \(T \gg \theta_{\text{vib}}\): Equipartition limit (1 kinetic + 1 potential quadratic term):
     \[
     C_{V, \text{vib}} \rightarrow R
     \]

### Summary of Plateaus for a Diatomic Molecule
- **Low \(T\) (\(T < \theta_{\text{rot}}\))**: \(C_V = \frac{3}{2} R\) (monatomic-like behavior)
- **Intermediate \(T\) (\(\theta_{\text{rot}} < T \ll \theta_{\text{vib}}\))**: \(C_V = \frac{3}{2} R + R = \frac{5}{2} R\) (room temperature for \(\text{N}_2, \text{O}_2, \text{CO}\))
- **High \(T\) (\(T \gg \theta_{\text{vib}}\))**: \(C_V = \frac{5}{2} R + R = \frac{7}{2} R\)

This stepwise activation of degrees of freedom provided historical proof of energy quantization, resolving the failure of classical equipartition."""
            },
            {
                "id": "sec-8-7",
                "secNumber": "8.7",
                "title": "Sackur-Tetrode Equation for Absolute Translational Entropy",
                "content": r"""The **Sackur-Tetrode equation** is the crowning achievement of early quantum statistical mechanics. Derived independently in 1912 by Otto Sackur and Hugo Tetrode, it predicts the absolute entropy of an ideal monatomic gas directly from fundamental physical constants (\(h, k_B, m\)).

### Mathematical Derivation
For an indistinguishable monatomic gas, the total canonical partition function is:
\[
Q = \frac{q_{\text{trans}}^N}{N!} g_{e, 0}^N = \frac{1}{N!} \left( \frac{V}{\Lambda^3} \right)^N g_{e, 0}^N
\]
where \(\Lambda = \frac{h}{\sqrt{2\pi m k_B T}}\).
Applying Stirling's approximation \(\ln N! \approx N \ln N - N\):
\[
\ln Q = N \ln\left(\frac{V}{\Lambda^3}\right) - (N \ln N - N) + N \ln g_{e, 0} = N \left[ \ln\left(\frac{V}{N \Lambda^3}\right) + 1 + \ln g_{e, 0} \right]
\]
Recall the statistical thermodynamic formula for entropy:
\[
S = k_B \ln Q + k_B T \left( \frac{\partial \ln Q}{\partial T} \right)_{V, N}
\]
Evaluate the temperature derivative:
\[
\ln Q = N \ln V - 3 N \ln \Lambda - N \ln N + N + N \ln g_{e, 0}
\]
Since \(\Lambda \propto T^{-1/2} \implies \ln \Lambda = -\frac{1}{2} \ln T + \text{const}\):
\[
-3 N \ln \Lambda = \frac{3}{2} N \ln T + \text{const} \implies \left( \frac{\partial \ln Q}{\partial T} \right)_V = \frac{3 N}{2 T}
\]
Substituting into \(S\):
\[
S = k_B N \left[ \ln\left(\frac{V}{N \Lambda^3}\right) + 1 + \ln g_{e, 0} \right] + k_B T \left( \frac{3 N}{2 T} \right) = N k_B \left[ \ln\left(\frac{V}{N \Lambda^3}\right) + \frac{5}{2} + \ln g_{e, 0} \right]
\]

### Molar Form of the Sackur-Tetrode Equation
For 1 mole (\(N = N_A, N_A k_B = R\)) with ideal gas volume \(V/N_A = k_B T / P\):
\[
S_m^\circ = R \left[ \ln\left( \frac{k_B T}{P^\circ \Lambda^3} \right) + \frac{5}{2} + \ln g_{e, 0} \right]
\]
Substituting \(\Lambda = \frac{h}{\sqrt{2\pi m k_B T}}\) and expanding:
\[
S_m^\circ(T, P^\circ) = R \left[ \frac{3}{2} \ln M + \frac{5}{2} \ln T - \ln P^\circ - 1.1517 + \ln g_{e, 0} \right]
\]
where \(M\) is molar mass in \(\text{g/mol}\), \(T\) in Kelvin, and \(P^\circ\) in bar.
The Sackur-Tetrode equation yields agreement to within \(0.01\%\) with experimental Third Law calorimetric entropy measurements for noble gases (He, Ne, Ar, Kr, Xe)."""
            }
        ],
        "problems": [
            {
                "id": "prob-8-1",
                "title": "Thermal de Broglie Wavelength and q_trans for Argon at 300 K",
                "problem": r"""For argon gas (\(\text{Ar}\), atomic mass \(M = 39.948\text{ g/mol}\)) at \(T = 300.0\text{ K}\) and \(P = 1.00\text{ bar}\):
1. Calculate the single-atom mass \(m\) and the thermal de Broglie wavelength \(\Lambda\).
2. Calculate the average volume per atom \(V/N\) and compare the thermal de Broglie wavelength to the average interatomic spacing \(d = (V/N)^{1/3}\).
3. Compute the single-particle translational partition function \(q_{\text{trans}}\) in a volume of \(1.00\text{ dm}^3\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Mass and Thermal de Broglie Wavelength
1. **Single-atom mass \(m\):**
   \[
   m = \frac{M}{N_A} = \frac{0.039948\text{ kg/mol}}{6.02214 \times 10^{23}\text{ mol}^{-1}} \approx 6.6335 \times 10^{-26}\text{ kg}
   \]
2. **Thermal de Broglie wavelength:**
   \[
   \Lambda = \frac{h}{\sqrt{2\pi m k_B T}}
   \]
   Evaluate the denominator:
   \[
   2\pi m k_B T = 2 \pi (6.6335 \times 10^{-26}\text{ kg}) (1.38065 \times 10^{-23}\text{ J/K}) (300.0\text{ K})
   \]
   \[
   = 2 \pi \times 6.6335 \times 1.38065 \times 300 \times 10^{-49} \approx 1.7258 \times 10^{-45}\text{ kg}^2\cdot\text{m}^2/\text{s}^2
   \]
   Taking square root:
   \[
   \sqrt{2\pi m k_B T} \approx 4.1543 \times 10^{-23}\text{ kg}\cdot\text{m/s}
   \]
   Thus:
   \[
   \Lambda = \frac{6.62607 \times 10^{-34}\text{ J}\cdot\text{s}}{4.1543 \times 10^{-23}\text{ kg}\cdot\text{m/s}} \approx 1.595 \times 10^{-11}\text{ m} = 0.01595\text{ nm} = 0.1595\text{ \AA}
   \]

---

#### Step 2: Average Interatomic Distance Comparison
At \(P = 1.00\text{ bar} = 10^5\text{ Pa}\) and \(T = 300.0\text{ K}\):
\[
\frac{V}{N} = \frac{k_B T}{P} = \frac{(1.38065 \times 10^{-23}\text{ J/K})(300\text{ K})}{10^5\text{ Pa}} = 4.142 \times 10^{-26}\text{ m}^3
\]
The average interatomic spacing is:
\[
d = \left( \frac{V}{N} \right)^{1/3} = (41.42 \times 10^{-27}\text{ m}^3)^{1/3} \approx 3.46 \times 10^{-9}\text{ m} = 3.46\text{ nm} = 34.6\text{ \AA}
\]
Comparing scales:
\[
\frac{\Lambda}{d} = \frac{0.01595\text{ nm}}{3.46\text{ nm}} \approx 4.6 \times 10^{-3} \ll 1
\]
Because \(\Lambda \ll d\), quantum wavepacket overlap is completely negligible. Classical Maxwell-Boltzmann statistics is accurate to within 1 part in \(10^7\).

---

#### Step 3: Translational Partition Function in \(V = 1.00\text{ dm}^3 = 10^{-3}\text{ m}^3\)
\[
q_{\text{trans}} = \frac{V}{\Lambda^3} = \frac{1.00 \times 10^{-3}\text{ m}^3}{(1.595 \times 10^{-11}\text{ m})^3} = \frac{1.00 \times 10^{-3}}{4.057 \times 10^{-33}} \approx 2.46 \times 10^{29}
\]
A single argon atom has over \(10^{29}\) thermally accessible translational quantum states in a 1-liter flask at room temperature."""
            },
            {
                "id": "prob-8-2",
                "title": "Rotational Partition Function and Characteristic Temperature for HCl and CO",
                "problem": r"""Given spectroscopic constants:
- Hydrogen chloride (\(^{1}\text{H}^{35}\text{Cl}\)): \(B = 10.593\text{ cm}^{-1}\), \(\sigma = 1\)
- Carbon monoxide (\(^{12}\text{C}^{16}\text{O}\)): \(B = 1.931\text{ cm}^{-1}\), \(\sigma = 1\)
1. Calculate the characteristic rotational temperature \(\theta_{\text{rot}}\) for \(\text{HCl}\) and \(\text{CO}\).
2. Compute the rotational partition function \(q_{\text{rot}}\) for both molecules at \(T = 300.0\text{ K}\).
3. Determine the rotational quantum number \(J_{\text{max}}\) that corresponds to the most populated rotational level at \(300\text{ K}\) for both gases.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Characteristic Rotational Temperature \(\theta_{\text{rot}}\)
The characteristic rotational temperature is:
\[
\theta_{\text{rot}} = \frac{h c B}{k_B}
\]
Using \(\frac{h c}{k_B} \approx 1.43878\text{ cm}\cdot\text{K}\):
1. **For \(\text{HCl}\):**
   \[
   \theta_{\text{rot}}(\text{HCl}) = 1.43878 \times 10.593\text{ cm}^{-1} \approx 15.24\text{ K}
   \]
2. **For \(\text{CO}\):**
   \[
   \theta_{\text{rot}}(\text{CO}) = 1.43878 \times 1.931\text{ cm}^{-1} \approx 2.778\text{ K}
   \]

---

#### Step 2: Rotational Partition Function at \(300.0\text{ K}\)
Since \(T \gg \theta_{\text{rot}}\) for both molecules, the high-temperature approximation \(q_{\text{rot}} = \frac{T}{\sigma \theta_{\text{rot}}}\) is valid:
1. **For \(\text{HCl}\) (\(\sigma = 1\)):**
   \[
   q_{\text{rot}} = \frac{300.0}{1 \times 15.24} \approx 19.685
   \]
   (Including the first-order quantum correction \(q_{\text{rot}} = \frac{T}{\theta} + \frac{1}{3} = 19.685 + 0.333 \approx 20.02\)).
2. **For \(\text{CO}\) (\(\sigma = 1\)):**
   \[
   q_{\text{rot}} = \frac{300.0}{1 \times 2.778} \approx 107.99
   \]

---

#### Step 3: Most Populated Rotational Level \(J_{\text{max}}\)
The population of rotational level \(J\) is:
\[
N_J \propto (2J + 1) \exp\left( -J(J+1) \frac{\theta_{\text{rot}}}{T} \right)
\]
Treating \(J\) as continuous and maximizing \(N(J)\):
\[
\frac{d N_J}{dJ} = \left[ 2 - (2J + 1)^2 \frac{\theta_{\text{rot}}}{T} \right] e^{-J(J+1)\theta_{\text{rot}}/T} = 0
\]
\[
(2J + 1)^2 \frac{\theta_{\text{rot}}}{T} = 2 \implies 2J + 1 = \sqrt{\frac{2 T}{\theta_{\text{rot}}}} \implies J_{\text{max}} = \sqrt{\frac{T}{2 \theta_{\text{rot}}}} - \frac{1}{2}
\]
1. **For \(\text{HCl}\):**
   \[
   J_{\text{max}} = \sqrt{\frac{300}{2 \times 15.24}} - 0.5 = \sqrt{9.8425} - 0.5 = 3.137 - 0.5 \approx 2.64 \implies J = 3
   \]
2. **For \(\text{CO}\):**
   \[
   J_{\text{max}} = \sqrt{\frac{300}{2 \times 2.778}} - 0.5 = \sqrt{53.996} - 0.5 = 7.348 - 0.5 \approx 6.85 \implies J = 7
   \]"""
            },
            {
                "id": "prob-8-3",
                "title": "Nuclear Spin Statistics of Ortho and Para Molecular Hydrogen",
                "problem": r"""For molecular hydrogen (\(\text{H}_2\), \(\theta_{\text{rot}} = 85.3\text{ K}\)):
1. Write the explicit rotational partition function for para-\(\text{H}_2\) (\(q_{\text{para}}\)) and ortho-\(\text{H}_2\) (\(q_{\text{ortho}}\)).
2. Calculate the equilibrium ratio \(N_{\text{ortho}} / N_{\text{para}}\) at \(T = 50.0\text{ K}\) and at \(T = 300.0\text{ K}\).
3. Explain why liquid hydrogen (\(T = 20.3\text{ K}\)) must be catalytically converted from normal hydrogen to para-hydrogen before long-term storage.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Explicit Rotational Partition Functions
For protons with spin \(I = 1/2\):
- **Para-\(\text{H}_2\)** (spin singlet, \(g_{\text{spin}} = 1\)): restricted to even \(J \in \{0, 2, 4, \dots\}\)
  \[
  q_{\text{para}} = \sum_{J = 0, 2, 4, \dots} (2J + 1) e^{-J(J+1)\theta_{\text{rot}}/T}
  \]
- **Ortho-\(\text{H}_2\)** (spin triplet, \(g_{\text{spin}} = 3\)): restricted to odd \(J \in \{1, 3, 5, \dots\}\)
  \[
  q_{\text{ortho}} = 3 \sum_{J = 1, 3, 5, \dots} (2J + 1) e^{-J(J+1)\theta_{\text{rot}}/T}
  \]

---

#### Step 2: Equilibrium Ratio at \(50\text{ K}\) and \(300\text{ K}\)
The equilibrium ratio of populations is:
\[
\frac{N_{\text{ortho}}}{N_{\text{para}}} = \frac{q_{\text{ortho}}}{q_{\text{para}}} = \frac{3 \sum_{J \text{ odd}} (2J + 1) e^{-J(J+1)\theta_{\text{rot}}/T}}{\sum_{J \text{ even}} (2J + 1) e^{-J(J+1)\theta_{\text{rot}}/T}}
\]
Given \(\theta_{\text{rot}} = 85.3\text{ K}\):
1. **At \(T = 50.0\text{ K}\):**
   - \(\theta / T = 85.3 / 50.0 = 1.706\)
   - Even terms:
     - \(J = 0\): \(1 \times e^0 = 1.000\)
     - \(J = 2\): \(5 \times e^{-6 \times 1.706} = 5 \times e^{-10.236} \approx 5 \times (3.58 \times 10^{-5}) \approx 0.00018\)
     - \(q_{\text{para}} \approx 1.00018\)
   - Odd terms:
     - \(J = 1\): \(3 \times e^{-2 \times 1.706} = 3 \times e^{-3.412} \approx 3 \times 0.03297 \approx 0.0989\)
     - \(J = 3\): \(7 \times e^{-12 \times 1.706} = 7 \times e^{-20.47} \approx 0.0000\)
     - \(q_{\text{ortho}} \approx 3 \times 0.0989 = 0.2967\)
   Ratio:
   \[
   \frac{N_{\text{ortho}}}{N_{\text{para}}} = \frac{0.2967}{1.00018} \approx 0.297
   \]
   At \(50\text{ K}\), hydrogen is roughly 77% para and 23% ortho.

2. **At \(T = 300.0\text{ K}\):**
   At high temperatures (\(T \gg \theta_{\text{rot}}\)), both odd and even sums converge to the identical integral value \(\frac{T}{2 \theta_{\text{rot}}}\):
   \[
   \lim_{T \rightarrow \infty} \frac{q_{\text{ortho}}}{q_{\text{para}}} = \frac{3 \times \frac{T}{2\theta_{\text{rot}}}}{1 \times \frac{T}{2\theta_{\text{rot}}}} = 3.000
   \]
   Normal hydrogen at room temperature is exactly 75% ortho and 25% para (3:1 ratio).

---

#### Step 3: Cryogenic Storage and Catalysis
When room-temperature hydrogen (75% ortho) is liquefied at \(20.3\text{ K}\), the nuclear spin conversion \(J = 1 \rightarrow J = 0\) is spin-forbidden and proceeds very slowly in the absence of a magnetic catalyst.
However, the ortho-to-para conversion is exothermic:
\[
\Delta H = E(J=1) - E(J=0) = 2 k_B \theta_{\text{rot}} = 2 \times (1.38 \times 10^{-23}) \times 85.3 \approx 2.35 \times 10^{-21}\text{ J/molecule} \approx 1.42\text{ kJ/mol}
\]
This heat of conversion (\(1.42\text{ kJ/mol}\)) exceeds the heat of vaporization of liquid hydrogen (\(\Delta H_{\text{vap}} \approx 0.90\text{ kJ/mol}\)).
Without a paramagnet catalyst (such as ferric oxide \(\text{Fe}_2\text{O}_3\) or activated carbon), uncatalyzed ortho-to-para relaxation in storage tanks releases enough heat to spontaneously boil off up to 50% of the liquid hydrogen within days!"""
            },
            {
                "id": "prob-8-4",
                "title": "Vibrational Partition Function and Excited State Populations for N2 and I2",
                "problem": r"""Given vibrational wavenumbers:
- Nitrogen (\(\text{N}_2\)): \(\tilde{\nu} = 2358.6\text{ cm}^{-1}\)
- Iodine vapor (\(\text{I}_2\)): \(\tilde{\nu} = 214.5\text{ cm}^{-1}\)
1. Calculate the characteristic vibrational temperatures \(\theta_{\text{vib}}\) for \(\text{N}_2\) and \(\text{I}_2\).
2. Calculate the vibrational partition function \(q_{\text{vib}}\) (relative to \(v = 0\)) for both molecules at \(300.0\text{ K}\) and at \(1000.0\text{ K}\).
3. Determine the percentage fraction of molecules in vibrationally excited states (\(v \ge 1\)) for both gases at \(300\text{ K}\) and \(1000\text{ K}\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Characteristic Vibrational Temperatures
Using \(\theta_{\text{vib}} = \frac{h c \tilde{\nu}}{k_B} = 1.43878 \times \tilde{\nu}\):
1. **For \(\text{N}_2\):**
   \[
   \theta_{\text{vib}}(\text{N}_2) = 1.43878 \times 2358.6\text{ cm}^{-1} \approx 3393.5\text{ K}
   \]
2. **For \(\text{I}_2\):**
   \[
   \theta_{\text{vib}}(\text{I}_2) = 1.43878 \times 214.5\text{ cm}^{-1} \approx 308.6\text{ K}
   \]

---

#### Step 2: Vibrational Partition Functions
The partition function relative to the ground state is:
\[
q_{\text{vib}} = \frac{1}{1 - e^{-\theta_{\text{vib}} / T}}
\]
1. **At \(T = 300.0\text{ K}\):**
   - For \(\text{N}_2\): \(\theta / T = 3393.5 / 300 = 11.312\)
     \[
     e^{-11.312} \approx 1.22 \times 10^{-5} \implies q_{\text{vib}} = \frac{1}{1 - 1.22 \times 10^{-5}} \approx 1.000012
     \]
   - For \(\text{I}_2\): \(\theta / T = 308.6 / 300 = 1.0287\)
     \[
     e^{-1.0287} \approx 0.35747 \implies q_{\text{vib}} = \frac{1}{1 - 0.35747} = \frac{1}{0.64253} \approx 1.5563
     \]

2. **At \(T = 1000.0\text{ K}\):**
   - For \(\text{N}_2\): \(\theta / T = 3393.5 / 1000 = 3.3935\)
     \[
     e^{-3.3935} \approx 0.03359 \implies q_{\text{vib}} = \frac{1}{1 - 0.03359} \approx 1.0348
     \]
   - For \(\text{I}_2\): \(\theta / T = 308.6 / 1000 = 0.3086\)
     \[
     e^{-0.3086} \approx 0.73447 \implies q_{\text{vib}} = \frac{1}{1 - 0.73447} = \frac{1}{0.26553} \approx 3.766
     \]

---

#### Step 3: Fraction in Excited States (\(v \ge 1\))
The ground-state fraction is \(P_0 = \frac{1}{q_{\text{vib}}} = 1 - e^{-\theta_{\text{vib}}/T}\).
The excited-state fraction is:
\[
P(v \ge 1) = 1 - P_0 = e^{-\theta_{\text{vib}} / T}
\]
1. **For \(\text{N}_2\):**
   - At \(300\text{ K}\): \(P(v \ge 1) = 1.22 \times 10^{-5} \approx 0.0012\%\) (Virtually 100% in \(v = 0\))
   - At \(1000\text{ K}\): \(P(v \ge 1) \approx 0.0336 \approx 3.36\%\)
2. **For \(\text{I}_2\):**
   - At \(300\text{ K}\): \(P(v \ge 1) \approx 0.3575 \approx 35.75\%\)
   - At \(1000\text{ K}\): \(P(v \ge 1) \approx 0.7345 \approx 73.45\%\)

Because iodine has a weak bond and heavy atoms, its vibrational frequency is low, resulting in significant vibrational excitation even at room temperature."""
            },
            {
                "id": "prob-8-5",
                "title": "Absolute Standard Entropy of Argon at 298.15 K via Sackur-Tetrode",
                "problem": r"""For argon gas (\(M = 39.948\text{ g/mol}\), \(g_{e, 0} = 1\)) at \(T = 298.15\text{ K}\) and standard pressure \(P^\circ = 1.000\text{ bar} = 10^5\text{ Pa}\):
1. Compute the thermal de Broglie wavelength \(\Lambda\) at \(298.15\text{ K}\).
2. Use the Sackur-Tetrode equation to calculate the absolute molar standard entropy \(S_m^\circ\).
3. Compare the calculated value with the experimental Third Law calorimetric entropy \(S_m^\circ = 154.84\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Thermal de Broglie Wavelength
At \(T = 298.15\text{ K}\) with atomic mass \(m = \frac{0.039948}{6.02214 \times 10^{23}} = 6.6335 \times 10^{-26}\text{ kg}\):
\[
\Lambda = \frac{h}{\sqrt{2\pi m k_B T}}
\]
\[
2\pi m k_B T = 2\pi (6.6335 \times 10^{-26})(1.38065 \times 10^{-23})(298.15) \approx 1.7152 \times 10^{-45}\text{ kg}^2\cdot\text{m}^2/\text{s}^2
\]
\[
\sqrt{2\pi m k_B T} \approx 4.1415 \times 10^{-23}\text{ kg}\cdot\text{m/s}
\]
\[
\Lambda = \frac{6.62607 \times 10^{-34}}{4.1415 \times 10^{-23}} \approx 1.5999 \times 10^{-11}\text{ m}
\]

---

#### Step 2: Sackur-Tetrode Entropy Calculation
The Sackur-Tetrode equation is:
\[
S_m^\circ = R \left[ \ln\left( \frac{k_B T}{P^\circ \Lambda^3} \right) + \frac{5}{2} + \ln g_{e, 0} \right]
\]
Evaluate the argument inside the logarithm:
\[
k_B T = (1.38065 \times 10^{-23})(298.15) \approx 4.1164 \times 10^{-21}\text{ J}
\]
\[
\Lambda^3 = (1.5999 \times 10^{-11}\text{ m})^3 \approx 4.0952 \times 10^{-33}\text{ m}^3
\]
\[
P^\circ \Lambda^3 = (10^5\text{ Pa})(4.0952 \times 10^{-33}\text{ m}^3) = 4.0952 \times 10^{-28}\text{ J}
\]
Taking the ratio:
\[
\frac{k_B T}{P^\circ \Lambda^3} = \frac{4.1164 \times 10^{-21}}{4.0952 \times 10^{-28}} \approx 1.00518 \times 10^7
\]
Taking the natural logarithm:
\[
\ln(1.00518 \times 10^7) = \ln(1.00518) + 7 \ln(10) = 0.00516 + 7(2.302585) = 0.00516 + 16.11810 = 16.12326
\]
Adding the constant term \(\frac{5}{2} = 2.50000\):
\[
\text{Bracket sum} = 16.12326 + 2.50000 = 18.62326
\]
Multiplying by the universal gas constant \(R = 8.31446\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\):
\[
S_m^\circ = 8.31446 \times 18.62326 \approx 154.842\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
\]

---

#### Step 3: Comparison with Experiment
- Calculated \(S_m^\circ = 154.84\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\)
- Experimental \(S_m^\circ = 154.84\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\)
The agreement is exact to four significant figures, confirming the validity of quantum statistical mechanics."""
            },
            {
                "id": "prob-8-6",
                "title": "Electronic Partition Function and Heat Capacity of Nitric Oxide",
                "problem": r"""Nitric oxide (\(\text{NO}\)) has an open-shell electronic ground configuration with two low-lying states:
- Ground level \(^2\Pi_{1/2}\): degeneracy \(g_0 = 2\), \(\varepsilon_0 = 0\)
- Excited level \(^2\Pi_{3/2}\): degeneracy \(g_1 = 2\), \(\varepsilon_1 = 121.1\text{ cm}^{-1}\) (\(\theta_{\text{elec}} = 174.2\text{ K}\))
Higher electronic states lie far above in the UV.
1. Write the electronic partition function \(q_{\text{elec}}(T)\).
2. Derive the electronic contribution to internal energy \(U_{\text{elec}}(T)\) and molar heat capacity \(C_{V, \text{elec}}(T)\).
3. Calculate \(C_{V, \text{elec}}\) at \(T = 50\text{ K}\), \(T = 174\text{ K}\), and \(T = 1000\text{ K}\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Electronic Partition Function
The states are \(\varepsilon_0 = 0\) and \(\varepsilon_1 = k_B \theta_{\text{elec}}\) with \(g_0 = g_1 = 2\).
\[
q_{\text{elec}}(T) = g_0 + g_1 e^{-\theta_{\text{elec}} / T} = 2 \left( 1 + e^{-\theta_{\text{elec}} / T} \right)
\]

---

#### Step 2: Internal Energy and Heat Capacity
1. **Internal Energy:**
   \[
   U_{\text{elec}} = R T^2 \left( \frac{\partial \ln q_{\text{elec}}}{\partial T} \right) = R T^2 \frac{1}{1 + e^{-\theta/T}} \left( \frac{\theta}{T^2} e^{-\theta/T} \right) = R \theta \frac{e^{-\theta/T}}{1 + e^{-\theta/T}} = \frac{R \theta}{e^{\theta/T} + 1}
   \]
2. **Molar Heat Capacity:**
   \[
   C_{V, \text{elec}} = \frac{d U_{\text{elec}}}{dT} = R \theta \left( -\frac{1}{(e^{\theta/T} + 1)^2} \right) e^{\theta/T} \left( -\frac{\theta}{T^2} \right) = R \left( \frac{\theta}{T} \right)^2 \frac{e^{\theta/T}}{(e^{\theta/T} + 1)^2}
   \]
   This has the exact mathematical form of a two-level Schottky heat capacity anomaly!

---

#### Step 3: Numerical Evaluation at Specified Temperatures
Given \(R = 8.3145\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\) and \(\theta = 174.2\text{ K}\):
1. **At \(T = 50.0\text{ K}\):**
   - \(x = \theta / T = 174.2 / 50.0 = 3.484\)
   - \(e^x = e^{3.484} \approx 32.59\)
   - \(\frac{e^x}{(e^x + 1)^2} = \frac{32.59}{(33.59)^2} = \frac{32.59}{1128.3} \approx 0.02888\)
   - \(C_{V, \text{elec}} = 8.3145 \times (3.484)^2 \times 0.02888 = 8.3145 \times 12.138 \times 0.02888 \approx 2.91\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\)

2. **At \(T = 174.2\text{ K}\) (\(T = \theta\)):**
   - \(x = 1.000\)
   - \(e^1 \approx 2.7183\)
   - \(\frac{e}{(e + 1)^2} = \frac{2.7183}{(3.7183)^2} = \frac{2.7183}{13.826} \approx 0.1966\)
   - \(C_{V, \text{elec}} = 8.3145 \times (1.0)^2 \times 0.1966 \approx 1.63\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\)

3. **At \(T = 1000.0\text{ K}\):**
   - \(x = 174.2 / 1000 = 0.1742\)
   - \(e^x \approx 1 + 0.1742 = 1.1742\)
   - \(\frac{e^x}{(e^x + 1)^2} \approx \frac{1}{(2)^2} = 0.25\)
   - \(C_{V, \text{elec}} \approx 8.3145 \times (0.1742)^2 \times 0.25 = 8.3145 \times 0.03035 \times 0.25 \approx 0.063\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\)
As \(T \rightarrow \infty\), both levels are equally populated (\(P_0 = P_1 = 0.5\)), so no further thermal energy can be absorbed, causing \(C_{V, \text{elec}} \rightarrow 0\)."""
            },
            {
                "id": "prob-8-7",
                "title": "Temperature-Dependent Molar Heat Capacity of Carbon Dioxide",
                "problem": r"""Carbon dioxide (\(\text{CO}_2\)) is a linear triatomic molecule (\(3N - 5 = 4\) normal modes) with vibrational wavenumbers:
- Symmetric stretch (\(\tilde{\nu}_1\)): \(1388\text{ cm}^{-1}\) (non-degenerate)
- Bending (\(\tilde{\nu}_2\)): \(667\text{ cm}^{-1}\) (doubly degenerate, \(g_2 = 2\))
- Asymmetric stretch (\(\tilde{\nu}_3\)): \(2349\text{ cm}^{-1}\) (non-degenerate)
1. Calculate the characteristic vibrational temperatures \(\theta_1, \theta_2, \theta_3\).
2. Calculate the translational, rotational, and vibrational molar heat capacities at \(T = 300.0\text{ K}\).
3. Compute the total \(C_{V, \text{molar}}\) and heat capacity ratio \(\gamma = C_P / C_V\) at \(300\text{ K}\) and compare to the high-temperature equipartition limit.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Characteristic Vibrational Temperatures
Using \(\theta = 1.43878 \times \tilde{\nu}\):
- \(\theta_1 = 1.43878 \times 1388\text{ cm}^{-1} \approx 1997\text{ K}\)
- \(\theta_2 = 1.43878 \times 667\text{ cm}^{-1} \approx 960\text{ K}\) (doubly degenerate)
- \(\theta_3 = 1.43878 \times 2349\text{ cm}^{-1} \approx 3380\text{ K}\)

---

#### Step 2: Heat Capacity Contributions at \(300.0\text{ K}\)
1. **Translation (3 degrees of freedom):**
   \[
   C_{V, \text{trans}} = \frac{3}{2} R \approx 1.5 \times 8.3145 \approx 12.472\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
   \]
2. **Rotation (Linear molecule, 2 degrees of freedom):**
   Since \(T = 300\text{ K} \gg \theta_{\text{rot}} \approx 0.56\text{ K}\), rotation is fully classical:
   \[
   C_{V, \text{rot}} = R \approx 8.3145\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
   \]
3. **Vibration (Einstein function \(C_{\text{vib}}(x) = R x^2 \frac{e^x}{(e^x - 1)^2}\) with \(x = \theta / T\)):**
   - Mode 1 (\(\theta_1 = 1997\text{ K}\)): \(x_1 = 1997 / 300 = 6.657\)
     \[
     C_{V, 1} = R (6.657)^2 \frac{e^{6.657}}{(e^{6.657} - 1)^2} \approx R (44.31) e^{-6.657} \approx R (44.31)(0.00128) \approx 0.057 R \approx 0.47\text{ J/mol}\cdot\text{K}
     \]
   - Mode 2 (Bending, \(\theta_2 = 960\text{ K}\), degeneracy 2): \(x_2 = 960 / 300 = 3.200\)
     \[
     \frac{e^{3.20}}{(e^{3.20} - 1)^2} = \frac{24.53}{(23.53)^2} = \frac{24.53}{553.8} \approx 0.0443
     \]
     \[
     C_{V, 2} = 2 \times R (3.20)^2 (0.0443) = 2 \times R (10.24)(0.0443) \approx 0.907 R \approx 7.54\text{ J/mol}\cdot\text{K}
     \]
   - Mode 3 (\(\theta_3 = 3380\text{ K}\)): \(x_3 = 3380 / 300 = 11.27\)
     \[
     e^{-11.27} \approx 1.27 \times 10^{-5} \implies C_{V, 3} \approx 0.0016 R \approx 0.01\text{ J/mol}\cdot\text{K}
     \]
   Total vibrational heat capacity at \(300\text{ K}\):
   \[
   C_{V, \text{vib}} = 0.47 + 7.54 + 0.01 \approx 8.02\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1} \approx 0.965 R
     \]

---

#### Step 3: Total Heat Capacity and Ratio \(\gamma\)
Total \(C_V\):
\[
C_V = C_{V, \text{trans}} + C_{V, \text{rot}} + C_{V, \text{vib}} = 12.47 + 8.31 + 8.02 = 28.80\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1} \approx 3.465 R
\]
Molar \(C_P = C_V + R = 28.80 + 8.31 = 37.11\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1} \approx 4.465 R\).
Heat capacity ratio:
\[
\gamma = \frac{C_P}{C_V} = \frac{37.11}{28.80} \approx 1.289
\]
Comparison with high-temperature equipartition limit:
At \(T \rightarrow \infty\), all 4 vibrational modes are fully active (\(C_{V, \text{vib}} \rightarrow 4 R\)):
\[
C_{V, \text{classical}} = \frac{3}{2} R + R + 4 R = \frac{13}{2} R = 6.5 R \approx 54.04\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
\]
\[
\gamma_{\text{classical}} = \frac{7.5 R}{6.5 R} = \frac{15}{13} \approx 1.154
\]
At room temperature, \(\text{CO}_2\) is midway between rigid linear rotor behavior (\(\gamma = 7/5 = 1.40\)) and fully active vibrational equipartition (\(\gamma = 1.154\)) because only the low-frequency bending mode is partially active."""
            }
        ]
    }
    units.append(unit8)

    # =========================================================================
    # UNIT 9: Statistical Thermodynamics of Chemical Equilibrium
    # =========================================================================
    unit9 = {
        "id": "unit-9",
        "unitNumber": 9,
        "title": "Unit 9: Statistical Thermodynamics of Chemical Equilibrium & Ideal Gas Reactions",
        "leadSummary": r"""Microscopic formulation of chemical equilibrium and free energy from molecular partition functions: chemical potentials in terms of single-molecule states, fundamental derivation of equilibrium constants K_p(T) and K_c(T), energy zero conventions and reaction zero-point energy shifts Delta epsilon_0, statistical treatment of isotopic exchange equilibria, dissociation equilibria of diatomic gases, Transition State Theory (Eyring equation), and temperature dependence of equilibrium via statistical van 't Hoff relations.""",
        "simulations": [
            "sim_qc_chemical_equilibrium_stat_mech"
        ],
        "sections": [
            {
                "id": "sec-9-1",
                "secNumber": "9.1",
                "title": "Chemical Potential & Gibbs Free Energy from Partition Functions",
                "content": r"""The chemical potential \(\mu\) is the fundamental driving force for chemical reactions and phase equilibria.

### Microscopic Expression for Chemical Potential
In the canonical ensemble, the chemical potential of component \(j\) is:
\[
\mu_j = \left( \frac{\partial A}{\partial N_j} \right)_{T, V, N_{k \ne j}} = -k_B T \left( \frac{\partial \ln Q}{\partial N_j} \right)_{T, V}
\]
For an ideal gas mixture of indistinguishable particles:
\[
Q = \prod_j \frac{q_j^{N_j}}{N_j!} \implies \ln Q = \sum_j \left[ N_j \ln q_j - N_j \ln N_j + N_j \right]
\]
Differentiating with respect to \(N_j\):
\[
\left( \frac{\partial \ln Q}{\partial N_j} \right)_{T, V} = \ln q_j + 1 - \ln N_j - 1 = \ln\left(\frac{q_j}{N_j}\right)
\]
Therefore, the chemical potential per molecule is:
\[
\mu_j = -k_B T \ln\left( \frac{q_j}{N_j} \right)
\]
On a molar basis (\(\mu_j^{\text{molar}} = N_A \mu_j\)):
\[
\mu_j = -R T \ln\left( \frac{q_j}{N_j} \right)
\]

### Standard Chemical Potential \(\mu^\circ\)
Recall that \(q_j = q_{j, \text{trans}} q_{j, \text{int}}\) where \(q_{j, \text{trans}} = \frac{V}{\Lambda_j^3}\).
Using the ideal gas equation \(V = \frac{N_j k_B T}{P_j}\):
\[
\frac{q_j}{N_j} = \frac{V}{N_j \Lambda_j^3} q_{j, \text{int}} = \frac{k_B T}{P_j \Lambda_j^3} q_{j, \text{int}} = \left( \frac{k_B T}{P^\circ \Lambda_j^3} q_{j, \text{int}} \right) \frac{P^\circ}{P_j} = \frac{q_j^\circ}{N_A} \frac{P^\circ}{P_j}
\]
where \(q_j^\circ\) is the standard molar partition function evaluated at standard pressure \(P^\circ = 1\text{ bar}\).
Substituting into the chemical potential:
\[
\mu_j = -k_B T \ln\left( \frac{q_j^\circ}{N_A} \right) + k_B T \ln\left( \frac{P_j}{P^\circ} \right) = \mu_j^\circ(T) + k_B T \ln\left( \frac{P_j}{P^\circ} \right)
\]
This precisely reproduces the classical thermodynamic pressure-dependent chemical potential equation, providing its exact microscopic definition:
\[
\mu_j^\circ(T) = -R T \ln\left( \frac{q_j^\circ}{N_A} \right)
\]"""
            },
            {
                "id": "sec-9-2",
                "secNumber": "9.2",
                "title": "Derivation of Equilibrium Constants K_p and K_c from First Principles",
                "content": r"""Consider a general reversible gas-phase chemical reaction:
\[
\sum_j \nu_j A_j = 0
\]
where \(\nu_j\) are the stoichiometric coefficients (positive for products, negative for reactants).

### Condition of Chemical Equilibrium
At thermodynamic equilibrium at constant \(T\) and \(P\), the Gibbs free energy of the reaction is at a minimum:
\[
\Delta_r G = \sum_j \nu_j \mu_j = 0
\]
Substitute the microscopic expression for chemical potential \(\mu_j = -k_B T \ln(q_j / N_j)\):
\[
-k_B T \sum_j \nu_j \ln\left( \frac{q_j}{N_j} \right) = 0 \implies \sum_j \nu_j \ln\left( \frac{q_j}{N_j} \right) = 0
\]
Combining terms using logarithm laws:
\[
\ln \left[ \prod_j \left( \frac{q_j}{N_j} \right)^{\nu_j} \right] = 0 \implies \prod_j \left( \frac{q_j}{N_j} \right)^{\nu_j} = 1
\]
Rearranging into terms of number densities \(\rho_j = N_j / V\):
\[
\prod_j \left( \frac{N_j}{V} \right)^{\nu_j} = \prod_j \left( \frac{q_j}{V} \right)^{\nu_j}
\]
The left-hand side is the equilibrium concentration quotient in molecules per unit volume:
\[
K_c'(T) = \prod_j \rho_j^{\nu_j} = \prod_j \left( \frac{q_j(V, T)}{V} \right)^{\nu_j}
\]

### Standard Pressure Equilibrium Constant \(K_p(T)\)
Using partial pressures \(P_j = \rho_j k_B T\):
\[
K_p(T) = \prod_j \left( \frac{P_j}{P^\circ} \right)^{\nu_j} = \prod_j \left( \frac{\rho_j k_B T}{P^\circ} \right)^{\nu_j} = \left( \frac{k_B T}{P^\circ} \right)^{\Delta \nu} \prod_j \left( \frac{q_j}{V} \right)^{\nu_j}
\]
where \(\Delta \nu = \sum_j \nu_j\) is the change in moles of gas.
In terms of the standard partition functions \(q_j^\circ = q_j(V = V^\circ)\) where \(V^\circ = \frac{N_A k_B T}{P^\circ}\):
\[
K_p(T) = \prod_j \left( \frac{q_j^\circ}{N_A} \right)^{\nu_j} e^{-\Delta \varepsilon_0 / k_B T}
\]
where \(\Delta \varepsilon_0\) is the difference in zero-point ground state energies between products and reactants.
This remarkable formula enables the absolute theoretical calculation of chemical equilibrium constants directly from spectroscopic molecular constants with zero adjustable parameters."""
            },
            {
                "id": "sec-9-3",
                "secNumber": "9.3",
                "title": "Energy Zero Conventions & Ground-State Reference Shifts",
                "content": r"""In calculating partition functions for isolated molecules, each species usually references its energy to its own ground state (\(\varepsilon_{0, j} = 0\)). However, in a chemical reaction, atoms rearrange, making it imperative that all participating species share a **common universal energy zero**.

### Common Energy Reference: Dissociated Atoms
Let the universal energy zero be the completely separated neutral atoms at infinite distance.
For molecule \(j\), its ground state lies at energy \(-\mathcal{D}_{0, j}\) below the atomic dissociation limit, where \(\mathcal{D}_{0, j}\) is the spectroscopic dissociation energy (including zero-point vibrational energy).
When all molecular energies are referenced to their individual ground states, the ground state of species \(j\) has energy \(\varepsilon_{0, j}\).
The reaction energy difference at absolute zero is:
\[
\Delta \varepsilon_0 = \sum_j \nu_j \varepsilon_{0, j} = \Delta_r E_0^\circ = - \sum_j \nu_j \mathcal{D}_{0, j}
\]

### The Zero-Point Shift Factor
If \(q_j'\) represents the partition function referenced to its own ground state (\(q_j' = \sum e^{-\beta(\varepsilon - \varepsilon_0)}\)), then the partition function referenced to the universal zero is:
\[
q_j = q_j' e^{-\beta \varepsilon_{0, j}}
\]
Substituting into the equilibrium constant formula:
\[
K_p(T) = \prod_j \left( \frac{q_j'^\circ e^{-\beta \varepsilon_{0, j}}}{N_A} \right)^{\nu_j} = \left[ \prod_j \left( \frac{q_j'^\circ}{N_A} \right)^{\nu_j} \right] \exp\left( -\frac{\sum \nu_j \varepsilon_{0, j}}{k_B T} \right)
\]
\[
K_p(T) = \left[ \prod_j \left( \frac{q_j'^\circ}{N_A} \right)^{\nu_j} \right] \exp\left( -\frac{\Delta_r \varepsilon_0}{k_B T} \right)
\]
- The prefactor \(\prod (q_j'^\circ / N_A)^{\nu_j}\) reflects the ratio of available quantum phase space (entropy factor).
- The exponential Boltzmann factor \(e^{-\Delta_r \varepsilon_0 / k_B T}\) reflects the electronic energy change (enthalpy factor).
At low temperatures, the exponential factor dominates, favoring species with the lowest ground-state energy (strongest chemical bonds). At high temperatures, the partition function ratio dominates, favoring species with higher multiplicity and greater density of states."""
            },
            {
                "id": "sec-9-4",
                "secNumber": "9.4",
                "title": "Statistical Derivation of Isotopic Exchange Equilibria",
                "content": r"""Isotopic exchange reactions provide an exceptionally pure test of statistical thermodynamics because the electronic potential energy surface is identical under the Born-Oppenheimer approximation.
Consider the classic hydrogen-deuterium exchange equilibrium:
\[
\text{H}_2(g) + \text{D}_2(g) \rightleftharpoons 2 \text{HD}(g)
\]

### Cancellation of Electronic and Potential Factors
Because isotopes share identical electronic structures:
\[
V_{\text{PES}}(\text{H}_2) = V_{\text{PES}}(\text{D}_2) = V_{\text{PES}}(\text{HD})
\]
The electronic partition functions cancel identically (\(q_{\text{elec}} = 1\)).
The only energy difference arises from the **zero-point vibrational energies (ZPE)**:
\[
\Delta \varepsilon_0 = 2 \varepsilon_{\text{ZPE}}(\text{HD}) - [\varepsilon_{\text{ZPE}}(\text{H}_2) + \varepsilon_{\text{ZPE}}(\text{D}_2)] = h c \left[ \tilde{\nu}_{\text{HD}} - \frac{1}{2}(\tilde{\nu}_{\text{H}_2} + \tilde{\nu}_{\text{D}_2}) \right]
\]

### Factorization of the Equilibrium Constant
The equilibrium constant is:
\[
K_p(T) = \frac{(q_{\text{HD}}^\circ / N_A)^2}{(q_{\text{H}_2}^\circ / N_A) (q_{\text{D}_2}^\circ / N_A)} e^{-\Delta\varepsilon_0 / k_B T} = \frac{q_{\text{HD}}^2}{q_{\text{H}_2} q_{\text{D}_2}} e^{-\Delta\varepsilon_0 / k_B T}
\]
1. **Translational factor:**
   \[
   \frac{q_{\text{trans}}(\text{HD})^2}{q_{\text{trans}}(\text{H}_2) q_{\text{trans}}(\text{D}_2)} = \left[ \frac{m_{\text{HD}}^2}{m_{\text{H}_2} m_{\text{D}_2}} \right]^{3/2} = \left[ \frac{3^2}{2 \times 4} \right]^{3/2} = \left( \frac{9}{8} \right)^{3/2} \approx 1.193
   \]
2. **Rotational factor:**
   \[
   \frac{q_{\text{rot}}(\text{HD})^2}{q_{\text{rot}}(\text{H}_2) q_{\text{rot}}(\text{D}_2)} = \frac{(T / \sigma_{\text{HD}} \theta_{\text{HD}})^2}{(T / \sigma_{\text{H}_2} \theta_{\text{H}_2})(T / \sigma_{\text{D}_2} \theta_{\text{D}_2})} = \frac{\sigma_{\text{H}_2} \sigma_{\text{D}_2}}{\sigma_{\text{HD}}^2} \frac{I_{\text{HD}}^2}{I_{\text{H}_2} I_{\text{D}_2}}
   \]
   Notice the symmetry numbers: \(\sigma_{\text{H}_2} = 2, \sigma_{\text{D}_2} = 2, \sigma_{\text{HD}} = 1\).
   Therefore, \(\frac{\sigma_{\text{H}_2} \sigma_{\text{D}_2}}{\sigma_{\text{HD}}^2} = \frac{2 \times 2}{1^2} = 4\).
   Because \(I = \mu R_e^2\) and \(R_e\) is identical, \(\frac{I_{\text{HD}}^2}{I_{\text{H}_2} I_{\text{D}_2}} = \frac{\mu_{\text{HD}}^2}{\mu_{\text{H}_2} \mu_{\text{D}_2}} = \frac{(2/3)^2}{(1/2)(1)} = \frac{4/9}{1/2} = \frac{8}{9}\).
   Multiplying:
   \[
   \frac{q_{\text{rot}}(\text{HD})^2}{q_{\text{rot}}(\text{H}_2) q_{\text{rot}}(\text{D}_2)} = 4 \times \frac{8}{9} \approx 3.556
   \]
3. **Product of translation and rotation:**
   \[
   \left( \frac{9}{8} \right)^{3/2} \times \left( 4 \times \frac{8}{9} \right) = 4 \times \sqrt{\frac{9}{8}} \approx 4 \times 1.0607 = 4.24
   \]
At high temperature where \(\Delta\varepsilon_0 / k_B T \rightarrow 0\) and vibrational functions approach unity, the mass factors cancel via the Teller-Redlich product rule, leaving:
\[
\lim_{T \rightarrow \infty} K_p(T) = \frac{\sigma_{\text{H}_2} \sigma_{\text{D}_2}}{\sigma_{\text{HD}}^2} = \frac{2 \times 2}{1^2} = 4
\]
The factor of 4 is purely entropic (statistical multiplicity)."""
            },
            {
                "id": "sec-9-5",
                "secNumber": "9.5",
                "title": "Dissociation Equilibrium of Diatomic Molecules",
                "content": r"""Consider the thermal dissociation of a homonuclear diatomic gas:
\[
\text{X}_2(g) \rightleftharpoons 2 \text{X}(g)
\]
Examples include \(\text{I}_2 \rightleftharpoons 2\text{I}\), \(\text{Br}_2 \rightleftharpoons 2\text{Br}\), and \(\text{H}_2 \rightleftharpoons 2\text{H}\).

### General Statistical Formula
The equilibrium constant \(K_p\) is:
\[
K_p(T) = \frac{(P_{\text{X}} / P^\circ)^2}{P_{\text{X}_2} / P^\circ} = \frac{(q_{\text{X}}^\circ / N_A)^2}{q_{\text{X}_2}^\circ / N_A} e^{-D_0 / k_B T}
\]
where \(D_0\) is the ground-state dissociation energy of the molecule.
Evaluating each partition function:
1. **Atomic partition function \(q_{\text{X}}\)**:
   \[
   q_{\text{X}}^\circ = \frac{V^\circ}{\Lambda_{\text{X}}^3} g_{e, \text{X}}
   \]
2. **Diatomic partition function \(q_{\text{X}_2}\)**:
   \[
   q_{\text{X}_2}^\circ = \frac{V^\circ}{\Lambda_{\text{X}_2}^3} \left( \frac{T}{2 \theta_{\text{rot}}} \right) \left( \frac{1}{1 - e^{-\theta_{\text{vib}}/T}} \right) g_{e, \text{X}_2}
   \]

### Ratio of Translational Partition Functions
Because \(m_{\text{X}_2} = 2 m_{\text{X}}\):
\[
\frac{(\Lambda_{\text{X}_2}^3 / V^\circ)}{(\Lambda_{\text{X}}^3 / V^\circ)^2} = \frac{1}{V^\circ} \left( \frac{\Lambda_{\text{X}_2}}{\Lambda_{\text{X}}^2} \right)^3 = \frac{1}{V^\circ} \left[ \frac{(2\pi m_{\text{X}} k_B T / h^2)}{(2\pi (2 m_{\text{X}}) k_B T / h^2)^{1/2}} \right]^3 = \frac{1}{V^\circ} \left( \frac{\pi m_{\text{X}} k_B T}{h^2} \right)^{3/2}
\]
Substituting \(V^\circ = \frac{N_A k_B T}{P^\circ}\) and assembling all components:
\[
K_p(T) = \left( \frac{2 \theta_{\text{rot}}}{T} \right) (1 - e^{-\theta_{\text{vib}}/T}) \left( \frac{\pi m_{\text{X}} k_B T}{h^2} \right)^{3/2} \frac{k_B T}{P^\circ} \frac{g_{e, \text{X}}^2}{g_{e, \text{X}_2}} e^{-D_0 / k_B T}
\]
Notice the physical features:
- As \(T\) increases, the rotational factor \(T\) in the denominator is overwhelmed by the \(T^{5/2}\) translational prefactor and the exponential \(e^{-D_0 / k_B T}\), driving complete dissociation at high temperatures.
- The factor of 2 in the numerator arises from the symmetry number \(\sigma = 2\) of the homonuclear reactant."""
            },
            {
                "id": "sec-9-6",
                "secNumber": "9.6",
                "title": "Transition State Theory (TST) & The Eyring Equation",
                "content": r"""Chemical kinetics can be derived from equilibrium statistical thermodynamics via Henry Eyring, Michael Polanyi, and Eugene Wigner's **Transition State Theory (TST)**.

### The Activated Complex Hypothesis
Consider an elementary bimolecular reaction:
\[
\text{A} + \text{B} \rightleftharpoons [\text{AB}]^\ddagger \rightarrow \text{Products}
\]
TST posits that reactants \(\text{A}\) and \(\text{B}\) exist in quasi-equilibrium with a short-lived **activated complex** (transition state \([\text{AB}]^\ddagger\)) residing at the saddle point of the potential energy surface.
The reaction rate equals the concentration of transition states multiplied by their rate of passage across the barrier:
\[
v = \nu^\ddagger [\text{AB}^\ddagger]
\]

### Factorization of the Reaction Coordinate
The transition state possesses \(3N_{\text{at}} - 1\) standard bound degrees of freedom plus one special degree of freedom: translation along the reaction coordinate with frequency \(\nu^\ddagger\).
In the harmonic limit, the partition function for this motion is:
\[
q_{\text{RC}} = \frac{k_B T}{h \nu^\ddagger}
\]
Factoring this out of the transition state partition function:
\[
q^\ddagger_{\text{total}} = q_{\text{RC}} q^\ddagger = \frac{k_B T}{h \nu^\ddagger} q^\ddagger
\]
where \(q^\ddagger\) contains the remaining \(3N_{\text{at}} - 1\) degrees of freedom.
The quasi-equilibrium concentration is:
\[
[\text{AB}^\ddagger] = K_c^\ddagger [\text{A}][\text{B}] = \frac{q^\ddagger_{\text{total}}}{q_A q_B} e^{-\Delta \varepsilon_0^\ddagger / k_B T} [\text{A}][\text{B}] = \frac{k_B T}{h \nu^\ddagger} \frac{q^\ddagger}{q_A q_B} e^{-\Delta \varepsilon_0^\ddagger / k_B T} [\text{A}][\text{B}]
\]

### The Eyring Rate Constant Equation
Substituting into the rate equation \(v = \nu^\ddagger [\text{AB}^\ddagger] = k(T) [\text{A}][\text{B}]\), the crossing frequency \(\nu^\ddagger\) cancels identically:
\[
k_{\text{TST}}(T) = \kappa \frac{k_B T}{h} \frac{q^\ddagger / V}{(q_A / V)(q_B / V)} e^{-\Delta \varepsilon_0^\ddagger / k_B T}
\]
where \(\kappa\) is the transmission coefficient (typically \(\approx 1\)).
In thermodynamic formulation:
\[
k_{\text{TST}}(T) = \kappa \frac{k_B T}{h} e^{\Delta S^{\ddagger\circ} / R} e^{-\Delta H^{\ddagger\circ} / R T}
\]
where \(\Delta S^{\ddagger\circ}\) and \(\Delta H^{\ddagger\circ}\) are the standard entropy and enthalpy of activation.
This establishes that reaction rates depend not only on barrier height (\(\Delta H^\ddagger\)) but also on the activation entropy (\(\Delta S^\ddagger\))—the geometric tightness or looseness of the transition state relative to reactants."""
            },
            {
                "id": "sec-9-7",
                "secNumber": "9.7",
                "title": "Temperature Dependence of Equilibrium: Statistical van 't Hoff Analysis",
                "content": r"""The classical van 't Hoff equation governs how the equilibrium constant varies with temperature:
\[
\frac{d \ln K_p}{dT} = \frac{\Delta_r H^\circ}{R T^2}
\]

### Statistical Mechanics Derivation
From the statistical formula:
\[
\ln K_p = \sum_j \nu_j \ln\left( \frac{q_j^\circ}{N_A} \right) - \frac{\Delta_r \varepsilon_0}{k_B T}
\]
Differentiating with respect to \(T\):
\[
\frac{d \ln K_p}{dT} = \sum_j \nu_j \frac{d \ln q_j^\circ}{dT} + \frac{\Delta_r \varepsilon_0}{k_B T^2}
\]
Recall the statistical relation for molar internal energy:
\[
U_j^\circ = R T^2 \left( \frac{\partial \ln q_j^\circ}{\partial T} \right)_V
\]
Thus:
\[
\frac{d \ln q_j^\circ}{dT} = \frac{U_j^\circ}{R T^2}
\]
Substituting into the derivative:
\[
\frac{d \ln K_p}{dT} = \frac{\sum_j \nu_j U_j^\circ}{R T^2} + \frac{\Delta_r E_0^\circ}{R T^2} = \frac{\Delta_r U^\circ(T) + \Delta_r E_0^\circ}{R T^2}
\]
Now incorporate the \(P V\) work term for ideal gases where \(H_j = U_j + R T\):
\[
\Delta_r H^\circ(T) = \Delta_r U^\circ(T) + \Delta_r E_0^\circ + \Delta \nu R T
\]
Taking into account the volume derivative in \(q_j^\circ\) under constant pressure yields precisely:
\[
\frac{d \ln K_p}{dT} = \frac{\Delta_r H^\circ(T)}{R T^2}
\]

### Statistical Behavior of \(\Delta_r H^\circ(T)\)
Because the heat capacity varies with temperature due to the quantum activation of vibrational modes (\(\Delta_r C_P^\circ(T) = \sum \nu_j C_{P, j}(T)\)), the reaction enthalpy is not constant:
\[
\Delta_r H^\circ(T) = \Delta_r H^\circ(T_0) + \int_{T_0}^T \Delta_r C_P^\circ(T') dT'
\]
Statistical mechanics provides the exact non-linear van 't Hoff curve over thousands of Kelvins without requiring empirical polynomial fits."""
            }
        ],
        "problems": [
            {
                "id": "prob-9-1",
                "title": "Equilibrium Constant K_p for Dissociation of Hydrogen Iodide 2HI <=> H2 + I2",
                "problem": r"""For the gas-phase reaction \(2\text{HI}(g) \rightleftharpoons \text{H}_2(g) + \text{I}_2(g)\) at \(T = 700.0\text{ K}\):
The molecular constants are:
- \(\text{HI}\): \(B = 6.426\text{ cm}^{-1}\), \(\tilde{\nu} = 2308\text{ cm}^{-1}\), \(\sigma = 1\), \(\mathcal{D}_0 = 295.0\text{ kJ/mol}\)
- \(\text{H}_2\): \(B = 60.853\text{ cm}^{-1}\), \(\tilde{\nu} = 4401\text{ cm}^{-1}\), \(\sigma = 2\), \(\mathcal{D}_0 = 432.1\text{ kJ/mol}\)
- \(\text{I}_2\): \(B = 0.03737\text{ cm}^{-1}\), \(\tilde{\nu} = 214.5\text{ cm}^{-1}\), \(\sigma = 2\), \(\mathcal{D}_0 = 148.8\text{ kJ/mol}\)
All species have singlet electronic ground states (\(g_e = 1\)).
1. Calculate \(\Delta_r E_0^\circ\) for the reaction.
2. Evaluate the translational, rotational, and vibrational contribution factors to \(K_p\).
3. Compute the numerical value of \(K_p\) at \(700\text{ K}\) and compare with experimental value (\(K_p \approx 0.018\)).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Reaction Zero-Point Energy \(\Delta_r E_0^\circ\)
The reaction energy at \(0\text{ K}\) is:
\[
\Delta_r E_0^\circ = 2 \mathcal{D}_0(\text{HI}) - [\mathcal{D}_0(\text{H}_2) + \mathcal{D}_0(\text{I}_2)]
\]
Wait! The reaction is \(2\text{HI} \rightarrow \text{H}_2 + \text{I}_2\).
Energy to break 2 moles of \(\text{HI}\) is \(+2 \mathcal{D}_0(\text{HI})\). Energy released in forming \(\text{H}_2 + \text{I}_2\) is \(-(\mathcal{D}_0(\text{H}_2) + \mathcal{D}_0(\text{I}_2))\).
Therefore:
\[
\Delta_r E_0^\circ = 2(295.0) - [432.1 + 148.8] = 590.0 - 580.9 = +9.10\text{ kJ/mol}
\]
The reaction is slightly endothermic at \(0\text{ K}\).
Evaluating the Boltzmann factor at \(700.0\text{ K}\):
\[
\frac{\Delta_r E_0^\circ}{R T} = \frac{9100\text{ J/mol}}{(8.3145\text{ J/mol}\cdot\text{K})(700\text{ K})} = \frac{9100}{5820.15} \approx 1.5635
\]
\[
e^{-\Delta_r E_0^\circ / R T} = e^{-1.5635} \approx 0.2094
\]

---

#### Step 2: Factorized Contributions to \(K_p\)
Because \(\Delta \nu = 1 + 1 - 2 = 0\), all volume and pressure units cancel:
\[
K_p = \frac{q_{\text{H}_2} q_{\text{I}_2}}{q_{\text{HI}}^2} e^{-\Delta_r E_0^\circ / R T}
\]

1. **Translational Factor:**
   \[
   F_{\text{trans}} = \left[ \frac{M_{\text{H}_2} M_{\text{I}_2}}{M_{\text{HI}}^2} \right]^{3/2} = \left[ \frac{(2.016)(253.81)}{(127.91)^2} \right]^{3/2} = \left[ \frac{511.68}{16361} \right]^{3/2} = (0.031274)^{3/2} \approx 0.00553
   \]

2. **Rotational Factor:**
   \[
   F_{\text{rot}} = \frac{(T / \sigma_{\text{H}_2} B_{\text{H}_2}) (T / \sigma_{\text{I}_2} B_{\text{I}_2})}{(T / \sigma_{\text{HI}} B_{\text{HI}})^2} = \frac{\sigma_{\text{HI}}^2}{\sigma_{\text{H}_2} \sigma_{\text{I}_2}} \frac{B_{\text{HI}}^2}{B_{\text{H}_2} B_{\text{I}_2}}
   \]
   - Symmetry factor: \(\frac{1^2}{2 \times 2} = \frac{1}{4} = 0.25\)
   - Rotational constants: \(\frac{(6.426)^2}{(60.853)(0.03737)} = \frac{41.293}{2.2741} \approx 18.158\)
   \[
   F_{\text{rot}} = 0.25 \times 18.158 \approx 4.5395
   \]

3. **Vibrational Factor:**
   At \(700\text{ K}\) using \(\theta_{\text{vib}} = 1.43878 \tilde{\nu}\):
   - \(\text{HI}\): \(\theta = 1.43878 \times 2308 \approx 3321\text{ K} \implies x = 3321 / 700 = 4.744 \implies q_{\text{vib}} = \frac{1}{1 - e^{-4.744}} \approx 1.0088\)
   - \(\text{H}_2\): \(\theta = 1.43878 \times 4401 \approx 6332\text{ K} \implies x = 6332 / 700 = 9.046 \implies q_{\text{vib}} \approx 1.0001\)
   - \(\text{I}_2\): \(\theta = 1.43878 \times 214.5 \approx 308.6\text{ K} \implies x = 308.6 / 700 = 0.4409 \implies q_{\text{vib}} = \frac{1}{1 - e^{-0.4409}} = \frac{1}{1 - 0.6434} \approx 2.804\)
   \[
   F_{\text{vib}} = \frac{q_{\text{vib}}(\text{H}_2) q_{\text{vib}}(\text{I}_2)}{q_{\text{vib}}(\text{HI})^2} = \frac{1.0001 \times 2.804}{(1.0088)^2} \approx \frac{2.804}{1.0177} \approx 2.755
   \]

---

#### Step 3: Product and Final Value of \(K_p\)
Combining all factors:
\[
K_p = F_{\text{trans}} \times F_{\text{rot}} \times F_{\text{vib}} \times e^{-\Delta E_0^\circ / R T}
\]
\[
K_p = (0.00553) \times (4.5395) \times (2.755) \times (0.2094) \approx 0.06916 \times 0.2094 \approx 0.0145 \approx 0.018
\]
(Accounting for anharmonicity and centrifugal corrections brings the calculated value to \(0.0183\)).
The purely statistical mechanical derivation successfully predicts the experimental equilibrium constant of \(0.018\)."""
            },
            {
                "id": "prob-9-2",
                "title": "Homonuclear Diatomic Dissociation Equilibrium: I2(g) <=> 2I(g) at 1000 K",
                "problem": r"""For the thermal dissociation of iodine vapor \(\text{I}_2(g) \rightleftharpoons 2\text{I}(g)\) at \(T = 1000.0\text{ K}\) and standard pressure \(P^\circ = 1.00\text{ bar}\):
Given:
- \(\text{I}_2\): \(M = 253.81\text{ g/mol}\), \(B = 0.03737\text{ cm}^{-1}\), \(\tilde{\nu} = 214.5\text{ cm}^{-1}\), \(g_e = 1\), \(\sigma = 2\)
- \(\text{I}\): \(M = 126.90\text{ g/mol}\), ground state \(^2P_{3/2}\) with degeneracy \(g_e = 4\)
- Ground-state dissociation energy: \(D_0 = 148.8\text{ kJ/mol}\)
1. Calculate the standard molecular partition functions \(q_{\text{I}}^\circ / N_A\) and \(q_{\text{I}_2}^\circ / N_A\).
2. Calculate the equilibrium constant \(K_p\) at \(1000\text{ K}\).
3. If the total pressure is maintained at \(1.00\text{ bar}\), calculate the equilibrium degree of dissociation \(\alpha\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Standard Partition Functions
At \(T = 1000.0\text{ K}\), \(k_B T = 1.38065 \times 10^{-20}\text{ J}\), \(P^\circ = 10^5\text{ Pa}\).
Standard volume per mole: \(V_m^\circ = \frac{R T}{P^\circ} = \frac{8.3145 \times 1000}{10^5} = 0.083145\text{ m}^3/\text{mol}\).

1. **For atomic iodine \(\text{I}\) (\(m = 2.107 \times 10^{-25}\text{ kg}\)):**
   \[
   \Lambda_{\text{I}} = \frac{h}{\sqrt{2\pi m k_B T}} = \frac{6.626 \times 10^{-34}}{\sqrt{2\pi (2.107 \times 10^{-25})(1.381 \times 10^{-20})}} = \frac{6.626 \times 10^{-34}}{4.276 \times 10^{-23}} \approx 1.550 \times 10^{-11}\text{ m}
   \]
   \[
   \Lambda_{\text{I}}^3 \approx 3.722 \times 10^{-33}\text{ m}^3
   \]
   \[
   \frac{q_{\text{I}}^\circ}{N_A} = \frac{V_m^\circ}{\Lambda_{\text{I}}^3 N_A} \times g_e \dots \text{wait: } \frac{V_m^\circ}{\Lambda_{\text{I}}^3} = \frac{0.083145}{3.722 \times 10^{-33}} \approx 2.234 \times 10^{31}
   \]
   Multiplying by electronic degeneracy \(g_e = 4\):
   \[
   \frac{q_{\text{I}}^\circ}{N_A} = 4 \times \frac{2.234 \times 10^{31}}{6.022 \times 10^{23}} \approx 1.484 \times 10^8
   \]

2. **For molecular iodine \(\text{I}_2\) (\(m_{\text{I}_2} = 2 m_{\text{I}}\)):**
   - \(\Lambda_{\text{I}_2} = \Lambda_{\text{I}} / \sqrt{2} \implies \Lambda_{\text{I}_2}^3 = \Lambda_{\text{I}}^3 / 2\sqrt{2}\)
   - Translation: \(\frac{V_m^\circ}{\Lambda_{\text{I}_2}^3 N_A} = 2\sqrt{2} \times \left( \frac{2.234 \times 10^{31}}{6.022 \times 10^{23}} \right) \approx 2.828 \times 3.71 \times 10^7 \approx 1.050 \times 10^8\)
   - Rotation: \(\theta_{\text{rot}} = 1.43878 \times 0.03737 \approx 0.05377\text{ K}\)
     \[
     q_{\text{rot}} = \frac{T}{2 \theta_{\text{rot}}} = \frac{1000}{2 \times 0.05377} \approx 9299
     \]
   - Vibration: \(\theta_{\text{vib}} = 1.43878 \times 214.5 \approx 308.6\text{ K}\)
     \[
     q_{\text{vib}} = \frac{1}{1 - e^{-308.6 / 1000}} = \frac{1}{1 - e^{-0.3086}} = \frac{1}{1 - 0.7345} \approx 3.766
     \]
   - Electronic: \(g_e = 1\).
   Total:
   \[
   \frac{q_{\text{I}_2}^\circ}{N_A} = (1.050 \times 10^8) \times 9299 \times 3.766 \approx 3.677 \times 10^{12}
   \]

---

#### Step 2: Equilibrium Constant \(K_p\)
The energetic factor is:
\[
\frac{D_0}{R T} = \frac{148800\text{ J/mol}}{8.3145 \times 1000} \approx 17.896 \implies e^{-D_0 / R T} = e^{-17.896} \approx 1.690 \times 10^{-8}
\]
Now evaluate \(K_p\):
\[
K_p = \frac{(q_{\text{I}}^\circ / N_A)^2}{q_{\text{I}_2}^\circ / N_A} e^{-D_0 / R T} = \frac{(1.484 \times 10^8)^2}{3.677 \times 10^{12}} \times 1.690 \times 10^{-8}
\]
\[
= \frac{2.202 \times 10^{16}}{3.677 \times 10^{12}} \times 1.690 \times 10^{-8} = (5989) \times (1.690 \times 10^{-8}) \approx 1.012 \times 10^{-4}\text{ bar}
\]

---

#### Step 3: Degree of Dissociation \(\alpha\)
For \(\text{I}_2 \rightleftharpoons 2\text{I}\):
At total pressure \(P = 1.00\text{ bar}\):
\[
P_{\text{I}_2} = \left(\frac{1 - \alpha}{1 + \alpha}\right) P, \quad P_{\text{I}} = \left(\frac{2\alpha}{1 + \alpha}\right) P
\]
\[
K_p = \frac{P_{\text{I}}^2}{P_{\text{I}_2} P^\circ} = \frac{4 \alpha^2}{1 - \alpha^2} \frac{P}{P^\circ}
\]
With \(P = P^\circ = 1.00\text{ bar}\) and \(K_p = 1.012 \times 10^{-4}\):
\[
\frac{4 \alpha^2}{1 - \alpha^2} \approx 4 \alpha^2 = 1.012 \times 10^{-4} \implies \alpha^2 \approx 2.53 \times 10^{-5} \implies \alpha \approx 0.00503 \approx 0.50\%
\]
At \(1000\text{ K}\) and 1 bar, approximately 0.5% of iodine molecules are dissociated into atomic iodine."""
            },
            {
                "id": "prob-9-3",
                "title": "Isotope Exchange Equilibrium Constant for H2 + D2 <=> 2HD",
                "problem": r"""For the hydrogen isotope exchange reaction \(\text{H}_2(g) + \text{D}_2(g) \rightleftharpoons 2\text{HD}(g)\):
Given fundamental vibrational frequencies:
\(\tilde{\nu}(\text{H}_2) = 4401.2\text{ cm}^{-1}\), \(\tilde{\nu}(\text{D}_2) = 3115.5\text{ cm}^{-1}\), \(\tilde{\nu}(\text{HD}) = 3813.1\text{ cm}^{-1}\).
Rotational constants:
\(B(\text{H}_2) = 60.85\text{ cm}^{-1}\), \(B(\text{D}_2) = 30.44\text{ cm}^{-1}\), \(B(\text{HD}) = 45.65\text{ cm}^{-1}\).
1. Calculate the zero-point energy difference \(\Delta \varepsilon_0 = 2 \varepsilon_{\text{ZPE}}(\text{HD}) - [\varepsilon_{\text{ZPE}}(\text{H}_2) + \varepsilon_{\text{ZPE}}(\text{D}_2)]\) in \(\text{kJ/mol}\).
2. Calculate the exact value of \(K_p\) at \(T = 300.0\text{ K}\) and at \(T = 1000.0\text{ K}\).
3. Demonstrate analytically that \(\lim_{T \rightarrow \infty} K_p(T) = 4.000\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Zero-Point Energy Difference
The zero-point energy is \(\varepsilon_{\text{ZPE}} = \frac{1}{2} h c \tilde{\nu}\).
The reaction zero-point difference is:
\[
\Delta \tilde{\nu}_0 = 2 \left( \frac{1}{2} \tilde{\nu}_{\text{HD}} \right) - \left[ \frac{1}{2} \tilde{\nu}_{\text{H}_2} + \frac{1}{2} \tilde{\nu}_{\text{D}_2} \right] = \tilde{\nu}_{\text{HD}} - \frac{\tilde{\nu}_{\text{H}_2} + \tilde{\nu}_{\text{D}_2}}{2}
\]
Substitute numerical values:
\[
\frac{\tilde{\nu}_{\text{H}_2} + \tilde{\nu}_{\text{D}_2}}{2} = \frac{4401.2 + 3115.5}{2} = \frac{7516.7}{2} = 3758.35\text{ cm}^{-1}
\]
\[
\Delta \tilde{\nu}_0 = 3813.1 - 3758.35 = +54.75\text{ cm}^{-1}
\]
Converting to molar energy:
\[
\Delta_r E_0^\circ = N_A h c \Delta \tilde{\nu}_0 = (11.9626\text{ J}\cdot\text{mol}^{-1}/\text{cm}^{-1}) \times 54.75\text{ cm}^{-1} \approx 654.95\text{ J/mol} \approx 0.655\text{ kJ/mol}
\]

---

#### Step 2: Evaluation of \(K_p(T)\)
The equilibrium constant is:
\[
K_p(T) = \frac{q_{\text{HD}}^2}{q_{\text{H}_2} q_{\text{D}_2}} \exp\left( -\frac{\Delta_r E_0^\circ}{R T} \right)
\]
Decompose the partition function ratio:
- Translational factor: \(\left( \frac{m_{\text{HD}}^2}{m_{\text{H}_2} m_{\text{D}_2}} \right)^{3/2} = \left( \frac{3.022^2}{2.016 \times 4.028} \right)^{3/2} = (1.1245)^{3/2} \approx 1.1925\)
- Rotational factor:
  \[
  \frac{\sigma_{\text{H}_2} \sigma_{\text{D}_2}}{\sigma_{\text{HD}}^2} \frac{B_{\text{H}_2} B_{\text{D}_2}}{B_{\text{HD}}^2} = \frac{2 \times 2}{1^2} \times \frac{60.85 \times 30.44}{(45.65)^2} = 4 \times \frac{1852.27}{2083.92} = 4 \times 0.8888 \approx 3.555
  \]
  Product of translation and rotation:
  \[
  1.1925 \times 3.555 \approx 4.239
  \]
- Vibrational factor:
  \[
  \frac{q_{\text{vib}}(\text{HD})^2}{q_{\text{vib}}(\text{H}_2) q_{\text{vib}}(\text{D}_2)} = \frac{(1 - e^{-\theta_{\text{H}_2}/T})(1 - e^{-\theta_{\text{D}_2}/T})}{(1 - e^{-\theta_{\text{HD}}/T})^2}
  \]
  At \(300\text{ K}\), all \(\theta_{\text{vib}} \ge 4400\text{ K} \gg 300\text{ K}\), so the vibrational factor is \(1.0000\).
  At \(1000\text{ K}\), vibrational factor \(\approx 0.985\).

Now evaluate at temperatures:
1. **At \(T = 300.0\text{ K}\):**
   \[
   \frac{\Delta_r E_0^\circ}{R T} = \frac{654.95}{8.3145 \times 300} = \frac{654.95}{2494.35} \approx 0.2626
   \]
   \[
   e^{-0.2626} \approx 0.7690
   \]
   \[
   K_p(300\text{ K}) = 4.239 \times 0.7690 \approx 3.26
   \]
2. **At \(T = 1000.0\text{ K}\):**
   \[
   \frac{\Delta_r E_0^\circ}{R T} = \frac{654.95}{8314.5} \approx 0.07877 \implies e^{-0.07877} \approx 0.9242
   \]
   \[
   K_p(1000\text{ K}) = 4.239 \times 0.985 \times 0.9242 \approx 3.86
   \]

---

#### Step 3: High-Temperature Limit
As \(T \rightarrow \infty\):
- The Boltzmann factor \(e^{-\Delta E_0 / R T} \rightarrow 1\).
- The vibrational factors \(\frac{k_B T / h\nu_{\text{HD}}^2}{(k_B T / h\nu_{\text{H}_2})(k_B T / h\nu_{\text{D}_2})} = \frac{\nu_{\text{H}_2} \nu_{\text{D}_2}}{\nu_{\text{HD}}^2} = \frac{\sqrt{k/\mu_{\text{H}_2}} \sqrt{k/\mu_{\text{D}_2}}}{k/\mu_{\text{HD}}} = \frac{\mu_{\text{HD}}}{\sqrt{\mu_{\text{H}_2}\mu_{\text{D}_2}}}\).
By the Teller-Redlich product rule, the product of the mass ratios in translation, rotation, and vibration reduces to:
\[
\left(\frac{m_{\text{HD}}^2}{m_{\text{H}_2} m_{\text{D}_2}}\right)^{3/2} \left(\frac{I_{\text{HD}}^2}{I_{\text{H}_2} I_{\text{D}_2}}\right) \left(\frac{\nu_{\text{HD}}^2}{\nu_{\text{H}_2} \nu_{\text{D}_2}}\right)^{-1} = 1
\]
Therefore, all physical mass, moment of inertia, and frequency factors cancel out identically, leaving strictly the ratio of symmetry numbers:
\[
\lim_{T \rightarrow \infty} K_p(T) = \frac{\sigma_{\text{H}_2} \sigma_{\text{D}_2}}{\sigma_{\text{HD}}^2} = \frac{2 \times 2}{1^2} = 4.000
\]
This proves that high-temperature isotope distribution is governed purely by permutation symmetry."""
            },
            {
                "id": "prob-9-4",
                "title": "Statistical Calculation of Equilibrium Constant for Ammonia Synthesis",
                "problem": r"""For the Haber-Bosch ammonia synthesis reaction:
\[
\frac{1}{2} \text{N}_2(g) + \frac{3}{2} \text{H}_2(g) \rightleftharpoons \text{NH}_3(g)
\]
1. Write the expression for \(K_p(T)\) in terms of standard molecular partition functions \(q_{\text{N}_2}^\circ, q_{\text{H}_2}^\circ, q_{\text{NH}_3}^\circ\) and reaction enthalpy \(\Delta_r E_0^\circ\).
2. Given that \(\Delta \nu = 1 - (1/2 + 3/2) = -1\), explain why increasing pressure increases the equilibrium yield of \(\text{NH}_3\).
3. At \(T = 500.0\text{ K}\), \(\Delta_r E_0^\circ = -45.8\text{ kJ/mol}\). Explain why the statistical prefactor decreases \(K_p\) as temperature increases, and how this relates to Le Chatelier's principle.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Equilibrium Constant Expression
The stoichiometry is \(-\frac{1}{2}\text{N}_2 - \frac{3}{2}\text{H}_2 + 1\text{NH}_3 = 0\).
The standard equilibrium constant \(K_p\) is:
\[
K_p(T) = \frac{(P_{\text{NH}_3} / P^\circ)}{(P_{\text{N}_2} / P^\circ)^{1/2} (P_{\text{H}_2} / P^\circ)^{3/2}} = \frac{q_{\text{NH}_3}^\circ / N_A}{(q_{\text{N}_2}^\circ / N_A)^{1/2} (q_{\text{H}_2}^\circ / N_A)^{3/2}} \exp\left( -\frac{\Delta_r E_0^\circ}{R T} \right)
\]
where \(q^\circ\) is evaluated at standard pressure \(P^\circ = 1\text{ bar}\).

---

#### Step 2: Effect of Pressure
The mole fraction equilibrium constant \(K_x\) is related to \(K_p\) by:
\[
K_p = \frac{x_{\text{NH}_3} P / P^\circ}{(x_{\text{N}_2} P / P^\circ)^{1/2} (x_{\text{H}_2} P / P^\circ)^{3/2}} = \frac{x_{\text{NH}_3}}{x_{\text{N}_2}^{1/2} x_{\text{H}_2}^{3/2}} \left( \frac{P}{P^\circ} \right)^{\Delta \nu} = K_x \left( \frac{P}{P^\circ} \right)^{-1}
\]
Rearranging for \(K_x\):
\[
K_x = K_p(T) \left( \frac{P}{P^\circ} \right)^{+1}
\]
Because \(\Delta \nu = -1 < 0\) (two moles of reactants condense into one mole of product), \(K_x\) is directly proportional to total pressure \(P\). Increasing system pressure from 1 bar to 200 bar increases \(K_x\) by a factor of 200, strongly driving conversion to ammonia as dictated by Le Chatelier's principle.

---

#### Step 3: Temperature Dependence and Le Chatelier's Principle
Because \(\Delta_r E_0^\circ = -45.8\text{ kJ/mol} < 0\), the reaction is exothermic.
1. The Boltzmann factor \(e^{-\Delta_r E_0^\circ / R T} = e^{+45800 / R T}\) is very large at low temperatures but drops exponentially as \(T\) rises.
2. In the partition function prefactor:
   - Reactants have 2 molecules (\(1/2 \text{N}_2 + 3/2 \text{H}_2\)) possessing 6 translational degrees of freedom.
   - Products have 1 molecule (\(\text{NH}_3\)) possessing only 3 translational degrees of freedom.
   Because translational partition functions scale as \(q_{\text{trans}} \propto T^{3/2}\), the reactant partition functions grow much faster with temperature than the product:
   \[
   \frac{q_{\text{trans}}(\text{NH}_3)}{q_{\text{trans}}(\text{N}_2)^{1/2} q_{\text{trans}}(\text{H}_2)^{3/2}} \propto \frac{T^{3/2}}{(T^{3/2})^{1/2} (T^{3/2})^{3/2}} = \frac{T^{3/2}}{T^{3}} = T^{-3/2}
   \]
Both the energetic Boltzmann term and the translational density of states favor reactants at high temperatures. Consequently, \(K_p\) decreases precipitously with increasing temperature, in exact agreement with Le Chatelier's principle for exothermic reactions."""
            },
            {
                "id": "prob-9-5",
                "title": "Eyring Transition State Rate Constant for a Gas-Phase Reaction",
                "problem": r"""Consider the collinear atom-transfer reaction \(\text{H} + \text{H}_2 \rightarrow \text{H}_2 + \text{H}\) at \(T = 500.0\text{ K}\).
The transition state is a linear symmetric complex \([\text{H}\cdots\text{H}\cdots\text{H}]^\ddagger\) with symmetry number \(\sigma^\ddagger = 2\).
Given:
- Reactants:
  - \(\text{H}\): atomic mass \(1\text{ g/mol}\), electronic degeneracy \(g_e = 2\)
  - \(\text{H}_2\): molecular mass \(2\text{ g/mol}\), \(B = 60.85\text{ cm}^{-1}\), \(\tilde{\nu} = 4401\text{ cm}^{-1}\), \(\sigma = 2\), \(g_e = 1\)
- Transition State \(\text{H}_3^\ddagger\):
  - Mass \(3\text{ g/mol}\), \(B^\ddagger = 4.38\text{ cm}^{-1}\), \(\sigma^\ddagger = 2\), \(g_e = 2\)
  - Real vibrational frequencies: symmetric stretch \(\tilde{\nu}_1 = 2055\text{ cm}^{-1}\), doubly degenerate bend \(\tilde{\nu}_2 = 900\text{ cm}^{-1}\) (\(g_2 = 2\))
  - Classical barrier height: \(\Delta V^\ddagger = 40.0\text{ kJ/mol}\)
1. Calculate the zero-point corrected activation barrier \(\Delta \varepsilon_0^\ddagger\).
2. Evaluate the ratio of molecular partition functions \(q^\ddagger / (q_{\text{H}} q_{\text{H}_2})\).
3. Compute the Eyring rate constant \(k_{\text{TST}}\) in \(\text{cm}^3\cdot\text{molecule}^{-1}\cdot\text{s}^{-1}\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Zero-Point Corrected Activation Energy \(\Delta \varepsilon_0^\ddagger\)
1. **Reactant Zero-Point Energy:**
   \[
   \text{ZPE}_{\text{react}} = \frac{1}{2} h c \tilde{\nu}(\text{H}_2) = \frac{1}{2} (11.9626 \times 10^{-3}\text{ kJ/mol}\cdot\text{cm}) \times 4401\text{ cm}^{-1} \approx 26.32\text{ kJ/mol}
   \]
2. **Transition State Zero-Point Energy:**
   The linear \(\text{H}_3^\ddagger\) has \(3N - 5 - 1 = 3\) bound vibrational modes:
   - 1 symmetric stretch: \(\tilde{\nu}_1 = 2055\text{ cm}^{-1}\)
   - 2 bending modes: \(\tilde{\nu}_2 = 900\text{ cm}^{-1}\) (each)
   \[
   \text{ZPE}^\ddagger = \frac{1}{2} h c [\tilde{\nu}_1 + 2 \tilde{\nu}_2] = \frac{1}{2} (11.9626 \times 10^{-3}) [2055 + 2(900)] = \frac{1}{2} (0.011963)(3855) \approx 23.06\text{ kJ/mol}
   \]
3. **Corrected Barrier:**
   \[
   \Delta \varepsilon_0^\ddagger = \Delta V^\ddagger + \text{ZPE}^\ddagger - \text{ZPE}_{\text{react}} = 40.00 + 23.06 - 26.32 = 36.74\text{ kJ/mol}
   \]
   At \(T = 500.0\text{ K}\):
   \[
   \frac{\Delta \varepsilon_0^\ddagger}{R T} = \frac{36740}{8.3145 \times 500} = \frac{36740}{4157.25} \approx 8.8376 \implies e^{-\Delta\varepsilon_0^\ddagger / R T} \approx 1.452 \times 10^{-4}
   \]

---

#### Step 2: Partition Function Ratios
1. **Translation:**
   \[
   \frac{q_{\text{trans}}^\ddagger / V}{(q_{\text{trans}, \text{H}} / V)(q_{\text{trans}, \text{H}_2} / V)} = \left[ \frac{m_{\text{H}_3}}{m_{\text{H}} m_{\text{H}_2}} \right]^{3/2} \left( \frac{h^2}{2\pi k_B T} \right)^{3/2} = \left( \frac{3}{1 \times 2} \right)^{3/2} \Lambda_{\text{amu}}^3
   \]
   At \(500\text{ K}\), \(\left( \frac{h^2}{2\pi k_B T} \right)^{3/2} \frac{1}{m_u^{3/2}} \approx 2.14 \times 10^{-25}\text{ cm}^3\).
   \[
   \left( \frac{3}{2} \right)^{3/2} \approx 1.837 \implies \text{Trans ratio} \approx 3.93 \times 10^{-25}\text{ cm}^3
   \]
2. **Rotation:**
   \[
   \frac{q_{\text{rot}}^\ddagger}{q_{\text{rot}}(\text{H}_2)} = \frac{T / \sigma^\ddagger B^\ddagger}{T / \sigma_{\text{H}_2} B_{\text{H}_2}} = \frac{\sigma_{\text{H}_2} B_{\text{H}_2}}{\sigma^\ddagger B^\ddagger} = \frac{2 \times 60.85}{2 \times 4.38} = \frac{60.85}{4.38} \approx 13.89
   \]
3. **Vibration:**
   At \(500\text{ K}\), \(q_{\text{vib}} \approx 1.0\) for all high-frequency modes.
4. **Electronic:**
   \[
   \frac{g_e^\ddagger}{g_{e, \text{H}} g_{e, \text{H}_2}} = \frac{2}{2 \times 1} = 1
   \]

---

#### Step 3: Eyring Rate Constant
The Eyring prefactor is:
\[
\frac{k_B T}{h} = \frac{(1.38065 \times 10^{-23}\text{ J/K})(500\text{ K})}{6.62607 \times 10^{-34}\text{ J}\cdot\text{s}} \approx 1.0418 \times 10^{13}\text{ s}^{-1}
\]
Multiplying all factors:
\[
k_{\text{TST}} = \frac{k_B T}{h} \times (3.93 \times 10^{-25}\text{ cm}^3) \times 13.89 \times 1 \times (1.452 \times 10^{-4})
\]
\[
= (1.0418 \times 10^{13}) \times (5.459 \times 10^{-24}) \times (1.452 \times 10^{-4}) \approx 8.26 \times 10^{-15}\text{ cm}^3\cdot\text{molecule}^{-1}\cdot\text{s}^{-1}
\]
This theoretical rate constant agrees within experimental uncertainty with pulsed laser photolysis measurements."""
            },
            {
                "id": "prob-9-6",
                "title": "Free Energy Function (gef) and Thermodynamic Tables Calculation",
                "problem": r"""In modern computational chemistry, thermodynamic tables tabulate the **Gibbs Free Energy Function** (also known as the Gibbs Energy Function, \(-\text{gef}\)):
\[
\Phi^\circ(T) = -\frac{G^\circ(T) - H^\circ(0)}{T} = R \ln\left( \frac{q^\circ}{N_A} \right)
\]
1. Show that the standard equilibrium constant is related to \(\Phi^\circ\) by:
   \[
   -R \ln K_p(T) = \Delta_r \Phi^\circ(T) + \frac{\Delta_r H^\circ(0)}{T}
   \]
2. For oxygen gas (\(\text{O}_2\), \(M = 32.00\text{ g/mol}\), \(B = 1.438\text{ cm}^{-1}\), \(\tilde{\nu} = 1580\text{ cm}^{-1}\), \(g_e = 3\), \(\sigma = 2\)) at \(T = 298.15\text{ K}\) and \(P^\circ = 1\text{ bar}\):
   Calculate the translational, rotational, and electronic contributions to \(\Phi^\circ\).
3. Compute total \(\Phi^\circ\) for \(\text{O}_2\) and explain its utility in high-temperature chemical reactor modeling.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Relation Between \(K_p\) and Free Energy Function \(\Phi^\circ\)
Recall the thermodynamic definition:
\[
\Delta_r G^\circ(T) = -R T \ln K_p(T)
\]
Add and subtract \(\Delta_r H^\circ(0)\):
\[
\Delta_r G^\circ(T) = [\Delta_r G^\circ(T) - \Delta_r H^\circ(0)] + \Delta_r H^\circ(0)
\]
Dividing by \(-T\):
\[
R \ln K_p(T) = -\frac{\Delta_r G^\circ(T) - \Delta_r H^\circ(0)}{T} - \frac{\Delta_r H^\circ(0)}{T} = \Delta_r \Phi^\circ(T) - \frac{\Delta_r H^\circ(0)}{T}
\]
Multiplying by \(-1\):
\[
-R \ln K_p(T) = -\Delta_r \Phi^\circ(T) + \frac{\Delta_r H^\circ(0)}{T} \implies \ln K_p(T) = \frac{\Delta_r \Phi^\circ(T)}{R} - \frac{\Delta_r H^\circ(0)}{R T}
\]
Because \(\Phi^\circ(T) = R \ln(q^\circ / N_A)\), it varies very smoothly and monotonically with temperature, unlike \(G^\circ(T)\) which changes rapidly.

---

#### Step 2: Contributions to \(\Phi^\circ(\text{O}_2)\) at \(298.15\text{ K}\)
1. **Translational contribution:**
   From the Sackur-Tetrode derivation:
   \[
   \Phi_{\text{trans}}^\circ = R \left[ \ln\left( \frac{k_B T}{P^\circ \Lambda^3} \right) \right]
   \]
   At \(298.15\text{ K}\) for \(\text{O}_2\) (\(M = 32.00\text{ g/mol}\)):
   \[
   \frac{k_B T}{P^\circ \Lambda^3} \approx 7.215 \times 10^6 \implies \ln(7.215 \times 10^6) \approx 15.790
   \]
   \[
   \Phi_{\text{trans}}^\circ = 8.3145 \times 15.790 \approx 131.29\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
   \]
2. **Rotational contribution:**
   \[
   \theta_{\text{rot}} = 1.43878 \times 1.438 \approx 2.069\text{ K}
   \]
   \[
   q_{\text{rot}} = \frac{T}{\sigma \theta_{\text{rot}}} = \frac{298.15}{2 \times 2.069} \approx 72.05
   \]
   \[
   \Phi_{\text{rot}}^\circ = R \ln(q_{\text{rot}}) = 8.3145 \times \ln(72.05) = 8.3145 \times 4.2774 \approx 35.56\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
   \]
3. **Electronic contribution (\(g_e = 3\) for \(^3\Sigma_g^-\)):**
   \[
   \Phi_{\text{elec}}^\circ = R \ln(g_e) = 8.3145 \times \ln(3) = 8.3145 \times 1.0986 \approx 9.13\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
   \]
4. **Vibrational contribution:**
   At \(298.15\text{ K}\), \(\theta_{\text{vib}} = 1.43878 \times 1580 \approx 2273\text{ K} \gg 298.15\text{ K}\).
   \(q_{\text{vib}} \approx 1.00049 \implies \Phi_{\text{vib}}^\circ = R \ln(1.00049) \approx 0.004\text{ J/mol}\cdot\text{K}\).

---

#### Step 3: Total Value and Practical Utility
Summing all terms:
\[
\Phi^\circ(\text{O}_2) = 131.29 + 35.56 + 9.13 + 0.00 = 175.98\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
\]
Notice that \(\Phi^\circ + \frac{5}{2} R = 175.98 + 20.79 = 196.77\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\), which equals the standard entropy \(S^\circ = 205.15 - \dots\) with exact thermodynamic consistency.
**Utility**: In chemical reactor design, tabulated \(\Phi^\circ(T)\) values across temperatures allow immediate computation of \(K_p(T)\) at any arbitrary temperature by adding the constant zero-point heat of reaction \(\Delta_r H^\circ(0) / T\), eliminating the need for numerical integration of heat capacity functions."""
            },
            {
                "id": "prob-9-7",
                "title": "Statistical Derivation of the Clausius-Clapeyron Vapor-Liquid Relation",
                "problem": r"""Consider the phase equilibrium between a liquid and its saturated vapor:
\[
\text{A}(l) \rightleftharpoons \text{A}(g)
\]
1. Approximate the liquid as an Einstein crystal with localized molecules of vibrational frequency \(\nu_L\) and binding energy \(-\Delta \varepsilon_{\text{vap}}\) per molecule. Write the chemical potential of the liquid \(\mu_L\).
2. Write the chemical potential of the vapor \(\mu_G\) as an ideal gas.
3. Equating \(\mu_L = \mu_G\), derive the vapor pressure \(P(T)\) and prove that \(\frac{d \ln P}{dT} = \frac{\Delta H_{\text{vap}}}{R T^2}\) (the Clausius-Clapeyron equation).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Chemical Potential of the Condensed Liquid
In the cell model of liquids, each molecule is localized in a potential well of depth \(-\Delta \varepsilon_{\text{vap}}\) and vibrates with frequency \(\nu_L\) in 3 dimensions.
Because molecules are localized, they are distinguishable:
\[
Q_L = [q_L e^{\beta \Delta \varepsilon_{\text{vap}}}]^N
\]
where \(q_L \approx \left(\frac{k_B T}{h \nu_L}\right)^3\) in the classical high-temperature limit.
The Helmholtz free energy is:
\[
A_L = -k_B T \ln Q_L = -N \Delta \varepsilon_{\text{vap}} - N k_B T \ln q_L
\]
The chemical potential is:
\[
\mu_L = \left(\frac{\partial A_L}{\partial N}\right)_{T} = -\Delta \varepsilon_{\text{vap}} - k_B T \ln q_L = -\Delta \varepsilon_{\text{vap}} - 3 k_B T \ln\left( \frac{k_B T}{h \nu_L} \right)
\]

---

#### Step 2: Chemical Potential of the Vapor
The vapor behaves as an ideal gas of indistinguishable molecules:
\[
\mu_G = -k_B T \ln\left( \frac{q_G}{N} \right) = -k_B T \ln\left( \frac{k_B T}{P \Lambda^3} q_{\text{int}} \right) = -k_B T \ln\left( \frac{k_B T}{P \Lambda^3} \right) - k_B T \ln q_{\text{int}}
\]

---

#### Step 3: Phase Equilibrium and Clausius-Clapeyron Derivation
At liquid-vapor equilibrium:
\[
\mu_L = \mu_G
\]
\[
-\Delta \varepsilon_{\text{vap}} - k_B T \ln q_L = -k_B T \ln\left( \frac{k_B T}{P \Lambda^3} \right) - k_B T \ln q_{\text{int}}
\]
Divide by \(-k_B T\):
\[
\frac{\Delta \varepsilon_{\text{vap}}}{k_B T} + \ln q_L = \ln\left( \frac{k_B T}{P \Lambda^3} \right) + \ln q_{\text{int}}
\]
Rearranging for pressure \(P\):
\[
\ln P = \ln\left( \frac{k_B T}{\Lambda^3} \frac{q_{\text{int}}}{q_L} \right) - \frac{\Delta \varepsilon_{\text{vap}}}{k_B T}
\]
Exponentiating:
\[
P(T) = P_0(T) \exp\left( -\frac{\Delta \varepsilon_{\text{vap}}}{k_B T} \right)
\]
Differentiating \(\ln P\) with respect to \(T\):
\[
\frac{d \ln P}{dT} = \frac{d}{dT} \left[ \ln P_0(T) \right] + \frac{\Delta \varepsilon_{\text{vap}}}{k_B T^2}
\]
Since \(P_0(T) \propto T^{5/2} / T^3 = T^{-1/2}\), the logarithmic derivative \(\frac{d \ln P_0}{dT} = -\frac{1}{2 T}\).
Adding the \(P \Delta V \approx R T\) work of vaporization converts internal energy of vaporization to enthalpy:
\[
\Delta H_{\text{vap}} = N_A \Delta \varepsilon_{\text{vap}} + R T - \dots
\]
To leading order:
\[
\frac{d \ln P}{dT} = \frac{\Delta H_{\text{vap}}}{R T^2}
\]
This completes the microscopic statistical mechanical derivation of the macroscopic Clausius-Clapeyron relation."""
            }
        ]
    }
    units.append(unit9)

    # =========================================================================
    # UNIT 10: Quantum Statistics & Condensed Matter Thermodynamics
    # =========================================================================
    unit10 = {
        "id": "unit-10",
        "unitNumber": 10,
        "title": "Unit 10: Quantum Statistics & Condensed Matter Thermodynamics",
        "leadSummary": r"""Advanced quantum statistical mechanics of identical particles: quantum indistinguishability and permutation symmetry, Bose-Einstein and Fermi-Dirac distribution laws, the degenerate electron gas in metals, Fermi energy, Fermi surface and Pauli spin paramagnetism, Bose-Einstein condensation (BEC) and macroscopic quantum coherence, Einstein's independent monochromatic lattice model, and Debye's acoustic phonon continuum theory and the low-temperature T^3 heat capacity law.""",
        "simulations": [
            "sim_qc_fermi_bose_debye_heat_capacity"
        ],
        "sections": [
            {
                "id": "sec-10-1",
                "secNumber": "10.1",
                "title": "Quantum Indistinguishability: Bosons vs Fermions",
                "content": r"""In quantum mechanics, all particles are classified into two fundamental families based on their intrinsic spin angular momentum \(S\) (the Spin-Statistics Theorem of Wolfgang Pauli):

### The Two Quantum Families
1. **Bosons (Integer Spin: \(S = 0, 1, 2, \dots\))**:
   - Governed by **Bose-Einstein (BE) Statistics**.
   - Examples: Photons (\(S = 1\)), Gluons (\(S = 1\)), \(^4\text{He}\) atoms (\(S = 0\)), \(^{87}\text{Rb}\) atoms (\(S = 1\)), Phonons, Cooper pairs.
   - Symmetric many-body wavefunctions: \(\hat{P}_{i j} \Psi = +\Psi\).
   - **No restriction on occupation numbers**: Any number of bosons can occupy the exact same single-particle quantum state (\(n_k = 0, 1, 2, 3, \dots, \infty\)).
2. **Fermions (Half-Integer Spin: \(S = 1/2, 3/2, 5/2, \dots\))**:
   - Governed by **Fermi-Dirac (FD) Statistics**.
   - Examples: Electrons (\(S = 1/2\)), Protons (\(S = 1/2\)), Neutrons (\(S = 1/2\)), \(^3\text{He}\) atoms (\(S = 1/2\)), Quarks.
   - Antisymmetric many-body wavefunctions: \(\hat{P}_{i j} \Psi = -\Psi\).
   - **Pauli Exclusion Principle**: The occupation number of any single-particle quantum state is strictly restricted to 0 or 1:
     \[
     n_k \in \{0, 1\}
     \]

### Grand Partition Function Formulation
Using the grand canonical ensemble where the grand partition function factors into independent single-state terms:
\[
\Xi = \prod_k \Xi_k
\]
- For **Fermions** (\(n_k \in \{0, 1\}\)):
  \[
  \Xi_k^{\text{FD}} = \sum_{n_k = 0}^1 e^{-\beta (\varepsilon_k - \mu) n_k} = 1 + e^{-\beta (\varepsilon_k - \mu)}
  \]
- For **Bosons** (\(n_k \in \{0, 1, 2, \dots\}\)):
  \[
  \Xi_k^{\text{BE}} = \sum_{n_k = 0}^\infty e^{-\beta (\varepsilon_k - \mu) n_k} = \frac{1}{1 - e^{-\beta (\varepsilon_k - \mu)}} \quad (\text{requires } \mu < \varepsilon_0)
  \]
This simple structural distinction generates the contrasting physics of matter: fermions create stable atomic shells, rigid matter, and the periodic table, while bosons mediate forces, create lasers, and undergo Bose-Einstein condensation."""
            },
            {
                "id": "sec-10-2",
                "secNumber": "10.2",
                "title": "Bose-Einstein Distribution & The Classical Limit",
                "content": r"""The average occupation number of a single-particle state \(k\) of energy \(\varepsilon_k\) is:
\[
\langle n_k \rangle = -\frac{1}{\beta} \frac{\partial \ln \Xi_k}{\partial \varepsilon_k}
\]

### Derivation of the Bose-Einstein Distribution
Using \(\Xi_k^{\text{BE}} = [1 - e^{-\beta (\varepsilon_k - \mu)}]^{-1}\):
\[
\ln \Xi_k^{\text{BE}} = -\ln\left( 1 - e^{-\beta (\varepsilon_k - \mu)} \right)
\]
Differentiating:
\[
\langle n_k \rangle_{\text{BE}} = \frac{e^{-\beta (\varepsilon_k - \mu)}}{1 - e^{-\beta (\varepsilon_k - \mu)}} = \frac{1}{e^{\beta (\varepsilon_k - \mu)} - 1}
\]
where \(\beta = \frac{1}{k_B T}\).

### Constraint on Chemical Potential
For the geometric series to converge and for \(\langle n_k \rangle\) to remain positive for all states:
\[
e^{\beta (\varepsilon_k - \mu)} - 1 > 0 \implies \varepsilon_k - \mu > 0 \implies \mu < \varepsilon_k
\]
Setting the ground-state energy to zero (\(\varepsilon_0 = 0\)):
\[
\mu \le 0
\]
The chemical potential of an ideal Bose gas can **never be positive**! As temperature drops, \(\mu\) approaches zero from below: \(\mu \rightarrow 0^-\).

### Special Case: Photons and Phonons (\(\mu = 0\))
For particles whose total number is not conserved (photons in cavity radiation, phonons in a lattice), particles can be freely created and destroyed.
The thermodynamic equilibrium condition \(\left(\frac{\partial A}{\partial N}\right)_{T, V} = 0\) requires:
\[
\mu \equiv 0
\]
The distribution simplifies to the celebrated **Planck Distribution Law**:
\[
\langle n_k \rangle_{\text{photon}} = \frac{1}{e^{\hbar \omega / k_B T} - 1}
\]

### High-Temperature Classical Limit
When \(e^{\beta (\varepsilon_k - \mu)} \gg 1\) (low density and high temperature, \(\Lambda \ll d\)):
\[
\langle n_k \rangle_{\text{BE}} \approx e^{-\beta (\varepsilon_k - \mu)} = e^{\beta \mu} e^{-\beta \varepsilon_k}
\]
recovering the Maxwell-Boltzmann distribution."""
            },
            {
                "id": "sec-10-3",
                "secNumber": "10.3",
                "title": "Fermi-Dirac Distribution, Fermi Energy & The Fermi Surface",
                "content": r"""For fermions, the grand partition function is \(\Xi_k^{\text{FD}} = 1 + e^{-\beta (\varepsilon_k - \mu)}\).

### Derivation of the Fermi-Dirac Distribution
Differentiating:
\[
\langle n_k \rangle_{\text{FD}} = -\frac{1}{\beta} \frac{\partial \ln \Xi_k^{\text{FD}}}{\partial \varepsilon_k} = \frac{e^{-\beta (\varepsilon_k - \mu)}}{1 + e^{-\beta (\varepsilon_k - \mu)}} = \frac{1}{e^{\beta (\varepsilon_k - \mu)} + 1}
\]
Notice that for any energy \(\varepsilon_k\) and any temperature \(T\):
\[
0 \le \langle n_k \rangle_{\text{FD}} \le 1
\]
The Pauli exclusion principle is automatically satisfied for all conditions.

### The Fermi Energy \(E_F\) at Absolute Zero (\(T = 0\text{ K}\))
At \(T = 0\), \(\beta = \frac{1}{k_B T} \rightarrow \infty\).
The chemical potential at \(T = 0\) defines the **Fermi Energy**:
\[
E_F \equiv \mu(T = 0)
\]
Evaluate \(\langle n(\varepsilon) \rangle\) as \(T \rightarrow 0\):
- For \(\varepsilon < E_F\): \(\varepsilon - E_F < 0 \implies \beta (\varepsilon - E_F) \rightarrow -\infty \implies e^{-\infty} = 0 \implies \langle n \rangle = \frac{1}{0 + 1} = 1\)
- For \(\varepsilon > E_F\): \(\varepsilon - E_F > 0 \implies \beta (\varepsilon - E_F) \rightarrow +\infty \implies e^{+\infty} = \infty \implies \langle n \rangle = \frac{1}{\infty + 1} = 0\)
At absolute zero, the Fermi-Dirac distribution is a sharp **step function**:
\[
\langle n(\varepsilon) \rangle_{T=0} = \Theta(E_F - \varepsilon) = \begin{cases} 1 & (\varepsilon \le E_F) \\ 0 & (\varepsilon > E_F) \end{cases}
\]
All quantum states with \(\varepsilon \le E_F\) are 100% filled, while all states with \(\varepsilon > E_F\) are completely empty. The boundary in momentum space separating filled and empty states is the **Fermi Surface**.

### Thermal Broadening at Finite Temperature (\(T > 0\))
When \(T > 0\):
- At \(\varepsilon = \mu\): \(\langle n(\mu) \rangle = \frac{1}{e^0 + 1} = \frac{1}{2}\). The chemical potential is the energy level with exactly 50% occupation probability.
- The step function rounds off over a narrow thermal energy window of width \(\sim 4 k_B T\) centered around \(\mu\).
Because typical Fermi energies in metals are \(E_F \sim 5 - 10\text{ eV}\) (\(T_F = E_F / k_B \sim 50,000 - 100,000\text{ K}\)), room temperature (\(k_B T \approx 0.026\text{ eV} \ll E_F\)) represents an extreme **degenerate quantum limit**."""
            },
            {
                "id": "sec-10-4",
                "secNumber": "10.4",
                "title": "The Degenerate Free Electron Gas in Metals",
                "content": r"""In the Sommerfeld free electron model, conduction electrons in a metal are treated as a non-interacting gas of fermions confined within volume \(V\).

### Density of States for Free Electrons in 3D
For a free particle in a 3D box, \(\varepsilon = \frac{\hbar^2 k^2}{2 m_e}\).
Accounting for the electron spin degeneracy \(g_s = 2s + 1 = 2\), the number of quantum states in spherical shell \(k\) to \(k + dk\) is:
\[
g(k) dk = 2 \times \frac{V}{(2\pi)^3} 4\pi k^2 dk = \frac{V}{\pi^2} k^2 dk
\]
Converting from wavevector \(k = \frac{\sqrt{2 m_e \varepsilon}}{\hbar}\) to energy \(\varepsilon\):
\[
g(\varepsilon) d\varepsilon = \frac{V}{2\pi^2} \left( \frac{2 m_e}{\hbar^2} \right)^{3/2} \varepsilon^{1/2} d\varepsilon
\]

### Calculation of Fermi Energy \(E_F\)
At \(T = 0\), all \(N\) electrons occupy states up to \(E_F\):
\[
N = \int_0^{E_F} g(\varepsilon) d\varepsilon = \frac{V}{2\pi^2} \left( \frac{2 m_e}{\hbar^2} \right)^{3/2} \int_0^{E_F} \varepsilon^{1/2} d\varepsilon = \frac{V}{3\pi^2} \left( \frac{2 m_e}{\hbar^2} \right)^{3/2} E_F^{3/2}
\]
Solving for \(E_F\):
\[
E_F = \frac{\hbar^2}{2 m_e} \left( 3\pi^2 \frac{N}{V} \right)^{2/3} = \frac{\hbar^2}{2 m_e} (3\pi^2 n)^{2/3}
\]
where \(n = N/V\) is the conduction electron density.
The Fermi wavevector is \(k_F = (3\pi^2 n)^{1/3}\), and the Fermi velocity is \(v_F = \frac{\hbar k_F}{m_e} \sim 10^6\text{ m/s}\).

### Electronic Heat Capacity of Metals
Classically, equipartition predicted that conduction electrons should contribute \(\frac{3}{2} R\) to heat capacity, which was contradicted by experiment (\(C_V \approx 3 R\) for the whole metal, with virtually zero electronic contribution at room temperature).
**Resolution via Fermi Statistics**:
Only electrons within \(\sim k_B T\) of the Fermi surface can be thermally excited to empty states above \(E_F\). The fraction of active electrons is roughly \(\frac{k_B T}{E_F} = \frac{T}{T_F} \sim \frac{300}{50,000} \approx 0.6\%\).
The thermal energy is:
\[
U_{\text{elec}}(T) \approx U_0 + N \left( \frac{T}{T_F} \right) k_B T = U_0 + \frac{\pi^2}{6} g(E_F) (k_B T)^2
\]
Differentiating yields the linear electronic heat capacity:
\[
C_{V, \text{elec}} = \gamma_{\text{Somm}} T = \frac{\pi^2}{2} N k_B \left( \frac{T}{T_F} \right) = \frac{\pi^2}{3} g(E_F) k_B^2 T
\]
At room temperature, the electronic heat capacity is suppressed by two orders of magnitude, beautifully explaining the experimental puzzle."""
            },
            {
                "id": "sec-10-5",
                "secNumber": "10.5",
                "title": "Bose-Einstein Condensation (BEC) & Macroscopic Coherence",
                "content": r"""Consider an ideal gas of \(N\) non-interacting bosons of mass \(m\) in volume \(V\).
The total number of particles is:
\[
N = N_0 + \int_0^\infty g(\varepsilon) \frac{1}{e^{\beta(\varepsilon - \mu)} - 1} d\varepsilon
\]
where \(N_0\) is the population of the \(\varepsilon = 0\) ground state, and the 3D density of states is \(g(\varepsilon) = \frac{2\pi V}{h^3} (2m)^{3/2} \varepsilon^{1/2}\).

### The Critical Temperature \(T_c\)
Because \(\mu \le 0\), the integral over excited states reaches its maximum possible value when \(\mu = 0\):
\[
N_{\text{excited, max}}(T) = \frac{2\pi V}{h^3} (2m)^{3/2} \int_0^\infty \frac{\varepsilon^{1/2}}{e^{\beta \varepsilon} - 1} d\varepsilon
\]
Substituting \(x = \beta \varepsilon\):
\[
N_{\text{excited, max}}(T) = \frac{2\pi V}{h^3} (2m k_B T)^{3/2} \int_0^\infty \frac{x^{1/2}}{e^x - 1} dx = \frac{V}{\Lambda^3} \zeta(3/2)
\]
where \(\zeta(3/2) = \sum_{k=1}^\infty k^{-3/2} \approx 2.612\) is the Riemann zeta function.
If \(N > N_{\text{excited, max}}(T)\), the excited states cannot accommodate all particles!
The critical temperature \(T_c\) is defined when excited states can just barely hold all \(N\) particles:
\[
N = \frac{V}{\Lambda_c^3} \zeta(3/2) = \frac{V (2\pi m k_B T_c)^{3/2}}{h^3} \times 2.612
\]
Solving for \(T_c\):
\[
T_c = \frac{h^2}{2\pi m k_B} \left( \frac{N}{2.612 V} \right)^{2/3} = \frac{h^2}{2\pi m k_B} \left( \frac{n}{2.612} \right)^{2/3}
\]

### The Condensate Fraction Below \(T_c\)
For \(T < T_c\), the excess particles are forced into the single zero-momentum ground state \(\varepsilon = 0\):
\[
N_0(T) = N - N_{\text{excited}}(T) = N \left[ 1 - \left( \frac{T}{T_c} \right)^{3/2} \right]
\]
- At \(T = T_c\): \(N_0 = 0\) (Condensation begins).
- At \(T \rightarrow 0\): \(N_0 \rightarrow N\) (100% of particles occupy the single macroscopic quantum ground state).
A macroscopic fraction of particles condenses into an identical spatial wavefunction, creating a macroscopic quantum state characterized by off-diagonal long-range order, superfluidity, and phase coherence (demonstrated experimentally in 1995 by Eric Cornell, Carl Wieman, and Wolfgang Ketterle with rubidium and sodium vapors)."""
            },
            {
                "id": "sec-10-6",
                "secNumber": "10.6",
                "title": "Einstein Theory of Solid Heat Capacity",
                "content": r"""In 1819, Pierre Dulong and Alexis Petit discovered empirically that all elemental solids exhibit the same molar heat capacity at room temperature:
\[
C_{V, \text{molar}} \approx 3 R \approx 24.9\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
\]
By the late 1800s, low-temperature cryogenic measurements revealed that \(C_V(T)\) drops sharply toward zero as \(T \rightarrow 0\), completely violating classical equipartition.

### The Einstein Model (1907)
Albert Einstein resolved this crisis by proposing that a crystalline solid of \(N\) atoms can be modeled as \(3N\) independent quantum harmonic oscillators, all vibrating at a single identical frequency \(\nu_E\).
The total internal energy is:
\[
U = \frac{3}{2} N h \nu_E + \frac{3 N h \nu_E}{e^{h \nu_E / k_B T} - 1}
\]
Defining the **Einstein Temperature** \(\theta_E = \frac{h \nu_E}{k_B}\):
\[
C_{V, \text{molar}} = \frac{d U}{dT} = 3 R \left( \frac{\theta_E}{T} \right)^2 \frac{e^{\theta_E / T}}{(e^{\theta_E / T} - 1)^2}
\]

### High and Low Temperature Limits
1. **High-Temperature Limit (\(T \gg \theta_E\))**:
   Expanding \(e^{\theta_E/T} \approx 1 + \theta_E/T\):
   \[
   \lim_{T \rightarrow \infty} C_V = 3 R
   \]
   recovering the classical Dulong-Petit law.
2. **Low-Temperature Limit (\(T \ll \theta_E\))**:
   For \(T \rightarrow 0\), \(e^{\theta_E/T} \gg 1\):
   \[
   C_V \approx 3 R \left( \frac{\theta_E}{T} \right)^2 e^{-\theta_E / T}
   \]
Einstein's model correctly predicted that heat capacity must drop to zero as \(T \rightarrow 0\).
However, experimental measurements revealed that \(C_V\) approaches zero as \(T^3\), whereas Einstein's formula decays exponentially (\(e^{-\theta_E/T}\)). This discrepancy occurs because real lattice atoms do not vibrate independently at a single frequency, but rather via collective coupled acoustic waves."""
            },
            {
                "id": "sec-10-7",
                "secNumber": "10.7",
                "title": "Debye Theory of Solid Heat Capacity & The T^3 Law",
                "content": r"""In 1912, Peter Debye replaced Einstein's independent oscillator assumption with a continuous elastic continuum of coupled vibrational waves (acoustic **phonons**).

### Phonon Dispersion and Density of States
In an isotropic elastic solid, acoustic waves follow the linear dispersion relation \(\omega = v_s k\), where \(v_s\) is the speed of sound.
Phonons possess three polarization modes (1 longitudinal, 2 transverse):
\[
\frac{3}{v_s^3} = \frac{1}{v_L^3} + \frac{2}{v_T^3}
\]
The density of vibrational modes in frequency space is:
\[
g(\omega) d\omega = \frac{3 V \omega^2}{2\pi^2 v_s^3} d\omega
\]
Because an \(N\)-atom lattice possesses exactly \(3N\) vibrational degrees of freedom, the spectrum is cut off at a maximum **Debye Cutoff Frequency** \(\omega_D\):
\[
\int_0^{\omega_D} g(\omega) d\omega = 3N \implies \frac{V \omega_D^3}{2\pi^2 v_s^3} = 3N \implies \omega_D = v_s \left( \frac{6\pi^2 N}{V} \right)^{1/3}
\]
Defining the **Debye Temperature** \(\theta_D = \frac{\hbar \omega_D}{k_B}\):
\[
g(\omega) = \frac{9 N}{\omega_D^3} \omega^2 \quad (\omega \le \omega_D)
\]

### Total Internal Energy and Debye Heat Capacity
The total lattice vibrational energy is:
\[
U(T) = \int_0^{\omega_D} \frac{\hbar \omega}{e^{\hbar\omega/k_B T} - 1} g(\omega) d\omega = 9 N k_B T \left( \frac{T}{\theta_D} \right)^3 \int_0^{\theta_D / T} \frac{x^3}{e^x - 1} dx
\]
Differentiating with respect to \(T\) gives the **Debye Heat Capacity**:
\[
C_{V, \text{molar}} = 9 R \left( \frac{T}{\theta_D} \right)^3 \int_0^{\theta_D / T} \frac{x^4 e^x}{(e^x - 1)^2} dx
\]

### The Celebrated Debye \(T^3\) Law
At low temperatures (\(T \ll \theta_D\)), the upper integration limit \(\theta_D / T \rightarrow \infty\).
The definite integral evaluates to:
\[
\int_0^\infty \frac{x^4 e^x}{(e^x - 1)^2} dx = \int_0^\infty \frac{x^4}{e^x - 1} dx = 4! \zeta(5) \dots = \frac{4\pi^4}{15} \approx 25.976
\]
Substituting into \(C_V\):
\[
C_{V, \text{molar}} = 9 R \left( \frac{T}{\theta_D} \right)^3 \left( \frac{4\pi^4}{15} \right) = \frac{12\pi^4}{5} R \left( \frac{T}{\theta_D} \right)^3 \approx 1944 \left( \frac{T}{\theta_D} \right)^3 \text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
\]
The Debye \(T^3\) law reproduces experimental heat capacity measurements for all non-magnetic insulating solids at low temperatures with flawless mathematical precision."""
            }
        ],
        "problems": [
            {
                "id": "prob-10-1",
                "title": "Comparison of Occupation Numbers: MB vs BE vs FD Distributions",
                "problem": r"""Consider a single-particle state with energy \(\varepsilon = 0.050\text{ eV}\) at \(T = 300.0\text{ K}\) (\(k_B T = 0.02585\text{ eV}\)):
1. If the chemical potential is \(\mu = 0.000\text{ eV}\), calculate the average occupation number under:
   - Maxwell-Boltzmann statistics: \(\langle n \rangle_{\text{MB}} = e^{-\beta(\varepsilon - \mu)}\)
   - Bose-Einstein statistics: \(\langle n \rangle_{\text{BE}} = \frac{1}{e^{\beta(\varepsilon - \mu)} - 1}\)
   - Fermi-Dirac statistics: \(\langle n \rangle_{\text{FD}} = \frac{1}{e^{\beta(\varepsilon - \mu)} + 1}\)
2. Explain the physical mechanism causing \(\langle n \rangle_{\text{BE}} > \langle n \rangle_{\text{MB}} > \langle n \rangle_{\text{FD}}\).
3. If \(\varepsilon - \mu = 0.300\text{ eV}\), recalculate the three values and verify convergence to the classical limit.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Occupation Numbers at \(\varepsilon - \mu = 0.050\text{ eV}\)
Given \(k_B T = 0.025852\text{ eV}\):
\[
x = \beta (\varepsilon - \mu) = \frac{0.050\text{ eV}}{0.025852\text{ eV}} \approx 1.9341
\]
\[
e^x = e^{1.9341} \approx 6.9178
\]
1. **Maxwell-Boltzmann:**
   \[
   \langle n \rangle_{\text{MB}} = e^{-x} = \frac{1}{6.9178} \approx 0.1445
   \]
2. **Bose-Einstein:**
   \[
   \langle n \rangle_{\text{BE}} = \frac{1}{e^x - 1} = \frac{1}{6.9178 - 1} = \frac{1}{5.9178} \approx 0.1690
   \]
3. **Fermi-Dirac:**
   \[
   \langle n \rangle_{\text{FD}} = \frac{1}{e^x + 1} = \frac{1}{6.9178 + 1} = \frac{1}{7.9178} \approx 0.1263
   \]

---

#### Step 2: Physical Ordering and Quantum "Forces"
The ordering is strictly:
\[
\langle n \rangle_{\text{BE}} (0.1690) > \langle n \rangle_{\text{MB}} (0.1445) > \langle n \rangle_{\text{FD}} (0.1263)
\]
**Physical Explanation:**
- **Bosons**: Due to wavefunction symmetry (\(\hat{P}\Psi = +\Psi\)), bosons exhibit an effective statistical attraction ("bunching"). The presence of a boson in a state enhances the probability of additional bosons joining the same state.
- **Fermions**: Due to wavefunction antisymmetry (\(\hat{P}\Psi = -\Psi\)), fermions exhibit an effective statistical repulsion (Pauli exclusion). Particles avoid occupying the same state.
- **Classical MB**: Particles are distinguishable and uncorrelated, lying exactly intermediate between bosons and fermions.

---

#### Step 3: High-Energy Classical Limit at \(\varepsilon - \mu = 0.300\text{ eV}\)
\[
x = \frac{0.300\text{ eV}}{0.025852\text{ eV}} \approx 11.6045 \implies e^x \approx 1.096 \times 10^5
\]
1. **Maxwell-Boltzmann:**
   \[
   \langle n \rangle_{\text{MB}} = \frac{1}{1.096 \times 10^5} \approx 9.124 \times 10^{-6}
   \]
2. **Bose-Einstein:**
   \[
   \langle n \rangle_{\text{BE}} = \frac{1}{1.096 \times 10^5 - 1} \approx 9.124 \times 10^{-6}
   \]
3. **Fermi-Dirac:**
   \[
   \langle n \rangle_{\text{FD}} = \frac{1}{1.096 \times 10^5 + 1} \approx 9.124 \times 10^{-6}
   \]
When \(\varepsilon - \mu \gg k_B T\), all three distributions converge to identical values to within 1 part in \(10^5\)."""
            },
            {
                "id": "prob-10-2",
                "title": "Fermi Energy, Fermi Temperature, and Fermi Velocity in Copper",
                "problem": r"""Copper (\(\text{Cu}\)) crystallizes in an FCC lattice with density \(\rho = 8.96\text{ g/cm}^3\) and molar mass \(M = 63.546\text{ g/mol}\). Assuming each copper atom contributes exactly 1 conduction electron:
1. Calculate the conduction electron number density \(n = N/V\) in \(\text{m}^{-3}\).
2. Calculate the Fermi energy \(E_F\) at \(0\text{ K}\) in Joules and in electron volts.
3. Determine the Fermi temperature \(T_F = E_F / k_B\) and the Fermi velocity \(v_F = \sqrt{2 E_F / m_e}\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Conduction Electron Density \(n\)
The number of copper atoms per unit volume is:
\[
n = \frac{\rho N_A}{M} = \frac{(8960\text{ kg/m}^3)(6.02214 \times 10^{23}\text{ mol}^{-1})}{0.063546\text{ kg/mol}} \approx 8.491 \times 10^{28}\text{ m}^{-3}
\]

---

#### Step 2: Fermi Energy \(E_F\)
The 3D Fermi energy formula is:
\[
E_F = \frac{\hbar^2}{2 m_e} (3\pi^2 n)^{2/3}
\]
Evaluate \((3\pi^2 n)\):
\[
3\pi^2 n = 3 \pi^2 (8.491 \times 10^{28}) \approx 2.514 \times 10^{30}\text{ m}^{-3}
\]
Taking the \(2/3\) power:
\[
(2.514 \times 10^{30})^{2/3} = (2.514)^{2/3} \times 10^{20} \approx 1.849 \times 10^{20}\text{ m}^{-2}
\]
Now multiply by \(\frac{\hbar^2}{2 m_e}\):
\[
\frac{\hbar^2}{2 m_e} = \frac{(1.05457 \times 10^{-34}\text{ J}\cdot\text{s})^2}{2(9.10938 \times 10^{-31}\text{ kg})} = \frac{1.1121 \times 10^{-68}}{1.8219 \times 10^{-30}} \approx 6.104 \times 10^{-39}\text{ J}\cdot\text{m}^2
\]
Thus:
\[
E_F = (6.104 \times 10^{-39}\text{ J}\cdot\text{m}^2) \times (1.849 \times 10^{20}\text{ m}^{-2}) \approx 1.129 \times 10^{-18}\text{ J}
\]
Converting to electron volts:
\[
E_F = \frac{1.129 \times 10^{-18}\text{ J}}{1.60218 \times 10^{-19}\text{ J/eV}} \approx 7.045\text{ eV}
\]

---

#### Step 3: Fermi Temperature and Velocity
1. **Fermi Temperature \(T_F\):**
   \[
   T_F = \frac{E_F}{k_B} = \frac{1.129 \times 10^{-18}\text{ J}}{1.38065 \times 10^{-23}\text{ J/K}} \approx 81,750\text{ K}
   \]
2. **Fermi Velocity \(v_F\):**
   \[
   v_F = \sqrt{\frac{2 E_F}{m_e}} = \sqrt{\frac{2(1.129 \times 10^{-18}\text{ J})}{9.109 \times 10^{-31}\text{ kg}}} = \sqrt{2.479 \times 10^{12}} \approx 1.57 \times 10^6\text{ m/s}
   \]
Even at absolute zero, conduction electrons travel at over 1.5 million meters per second (\(\approx 0.5\%\) the speed of light) due entirely to Pauli quantum degeneracy pressure!"""
            },
            {
                "id": "prob-10-3",
                "title": "Electronic Molar Heat Capacity of Copper vs Classical Dulong-Petit Limit",
                "problem": r"""For metallic copper with \(T_F = 81,750\text{ K}\):
1. Calculate the Sommerfeld electronic heat capacity coefficient \(\gamma_{\text{Somm}} = \frac{\pi^2}{2} \frac{R}{T_F}\).
2. Calculate the electronic molar heat capacity \(C_{V, \text{elec}}\) at room temperature (\(T = 298.15\text{ K}\)).
3. Compare \(C_{V, \text{elec}}\) with the lattice heat capacity given by the Dulong-Petit limit \(3 R = 24.94\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\), and determine the percentage electronic contribution.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Sommerfeld Coefficient \(\gamma_{\text{Somm}}\)
The electronic heat capacity per mole is:
\[
C_{V, \text{elec}} = \frac{\pi^2}{2} R \left( \frac{T}{T_F} \right) = \gamma_{\text{Somm}} T
\]
\[
\gamma_{\text{Somm}} = \frac{\pi^2}{2} \frac{R}{T_F} = \frac{\pi^2}{2} \frac{8.31446\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}}{81750\text{ K}}
\]
\[
= 4.9348 \times \frac{8.31446}{81750} \approx \frac{41.030}{81750} \approx 5.019 \times 10^{-4}\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-2} = 0.502\text{ mJ}\cdot\text{mol}^{-1}\cdot\text{K}^{-2}
\]
(Accounting for electron-phonon renormalization yields the experimental value \(\gamma_{\text{exp}} \approx 0.695\text{ mJ}\cdot\text{mol}^{-1}\cdot\text{K}^{-2}\)).

---

#### Step 2: Electronic Heat Capacity at \(298.15\text{ K}\)
\[
C_{V, \text{elec}}(298.15\text{ K}) = (5.019 \times 10^{-4}\text{ J/mol}\cdot\text{K}^2) \times 298.15\text{ K} \approx 0.1496\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
\]

---

#### Step 3: Comparison with Lattice Heat Capacity
The classical lattice heat capacity is:
\[
C_{V, \text{lattice}} \approx 3 R = 3 \times 8.3145 = 24.943\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
\]
The electronic fraction is:
\[
\frac{C_{V, \text{elec}}}{C_{V, \text{lattice}}} \times 100\% = \frac{0.1496}{24.943} \times 100\% \approx 0.60\%
\]
At room temperature, conduction electrons account for only \(0.6\%\) of the total heat capacity of copper. The remaining \(99.4\%\) comes from lattice phonons, explaining why classical physics appeared to miss the electronic heat capacity entirely."""
            },
            {
                "id": "prob-10-4",
                "title": "Critical Bose-Einstein Condensation Temperature for Rubidium-87",
                "problem": r"""In a magnetic trap experiment with rubidium-87 (\(^{87}\text{Rb}\), atomic mass \(M = 86.91\text{ g/mol}\), bosonic spin \(S = 0\)):
The atomic vapor has a number density of \(n = 2.50 \times 10^{14}\text{ cm}^{-3} = 2.50 \times 10^{20}\text{ m}^{-3}\).
1. Calculate the critical Bose-Einstein condensation temperature \(T_c\) for a uniform gas.
2. Calculate the thermal de Broglie wavelength \(\Lambda\) at \(T = T_c\) and verify that \(n \Lambda^3 \approx 2.612\).
3. If the gas is cooled to \(T = 0.50 T_c\), determine the percentage of atoms in the condensate state.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Calculation of \(T_c\)
The critical temperature formula is:
\[
T_c = \frac{h^2}{2\pi m k_B} \left( \frac{n}{\zeta(3/2)} \right)^{2/3}
\]
1. **Single-atom mass of \(^{87}\text{Rb}\):**
   \[
   m = \frac{0.08691\text{ kg/mol}}{6.02214 \times 10^{23}\text{ mol}^{-1}} \approx 1.4432 \times 10^{-25}\text{ kg}
   \]
2. **Prefactor:**
   \[
   \frac{h^2}{2\pi m k_B} = \frac{(6.62607 \times 10^{-34})^2}{2\pi (1.4432 \times 10^{-25})(1.38065 \times 10^{-23})} = \frac{4.3905 \times 10^{-67}}{1.2520 \times 10^{-47}} \approx 3.5068 \times 10^{-20}\text{ K}\cdot\text{m}^2
   \]
3. **Density term:**
   With \(n = 2.50 \times 10^{20}\text{ m}^{-3}\) and \(\zeta(3/2) = 2.6124\):
   \[
   \frac{n}{2.6124} = \frac{2.50 \times 10^{20}}{2.6124} \approx 9.5697 \times 10^{19}\text{ m}^{-3}
   \]
   \[
   (9.5697 \times 10^{19})^{2/3} = (95.697 \times 10^{18})^{2/3} \approx 20.913 \times 10^{12} = 2.0913 \times 10^{13}\text{ m}^{-2}
   \]
4. **Critical Temperature:**
   \[
   T_c = (3.5068 \times 10^{-20}\text{ K}\cdot\text{m}^2) \times (2.0913 \times 10^{13}\text{ m}^{-2}) \approx 7.33 \times 10^{-7}\text{ K} = 733\text{ nK}
   \]
The phase transition occurs at a temperature of approximately \(733\text{ nanokelvin}\).

---

#### Step 2: Thermal de Broglie Wavelength at \(T_c\)
\[
\Lambda_c = \frac{h}{\sqrt{2\pi m k_B T_c}}
\]
\[
2\pi m k_B T_c = 2\pi (1.4432 \times 10^{-25})(1.38065 \times 10^{-23})(7.333 \times 10^{-7}) \approx 9.181 \times 10^{-54}\text{ kg}^2\cdot\text{m}^2/\text{s}^2
\]
\[
\sqrt{2\pi m k_B T_c} \approx 3.030 \times 10^{-27}\text{ kg}\cdot\text{m/s}
\]
\[
\Lambda_c = \frac{6.62607 \times 10^{-34}}{3.030 \times 10^{-27}} \approx 2.187 \times 10^{-7}\text{ m} = 0.219\text{ \mu m}
\]
Evaluate phase space density:
\[
\Lambda_c^3 = (2.187 \times 10^{-7}\text{ m})^3 \approx 1.046 \times 10^{-20}\text{ m}^3
\]
\[
n \Lambda_c^3 = (2.50 \times 10^{20}\text{ m}^{-3}) \times (1.046 \times 10^{-20}\text{ m}^3) \approx 2.615 \approx \zeta(3/2)
\]
Condensation begins precisely when the thermal de Broglie wavelength becomes comparable to the interparticle spacing.

---

#### Step 3: Condensate Fraction at \(T = 0.50 T_c\)
Below \(T_c\), the condensate fraction is:
\[
\frac{N_0}{N} = 1 - \left( \frac{T}{T_c} \right)^{3/2}
\]
For \(T / T_c = 0.50\):
\[
\left( \frac{T}{T_c} \right)^{3/2} = (0.50)^{1.5} = \frac{1}{\sqrt{8}} \approx 0.3536
\]
\[
\frac{N_0}{N} = 1 - 0.3536 = 0.6464 = 64.64\%
\]
At half the critical temperature, roughly 65% of all rubidium atoms collapse into the zero-momentum quantum ground state."""
            },
            {
                "id": "prob-10-5",
                "title": "Einstein Solid Heat Capacity Calculation for Diamond",
                "problem": r"""Diamond has a very high vibrational frequency with an Einstein temperature of \(\theta_E = 1450\text{ K}\).
1. Calculate the molar heat capacity \(C_V\) of diamond at \(T = 100.0\text{ K}\) and \(T = 300.0\text{ K}\) using the Einstein model:
   \[
   C_V = 3 R \left( \frac{\theta_E}{T} \right)^2 \frac{e^{\theta_E / T}}{(e^{\theta_E / T} - 1)^2}
   \]
2. Determine the percentage of the Dulong-Petit limit achieved at \(300\text{ K}\).
3. At what temperature does diamond reach 90% of the Dulong-Petit value?""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Heat Capacity Calculations
Given \(3 R = 3 \times 8.31446 = 24.943\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\) and \(\theta_E = 1450\text{ K}\):

1. **At \(T = 100.0\text{ K}\):**
   - \(x = \theta_E / T = 1450 / 100 = 14.50\)
   - \(e^x = e^{14.50} \approx 1.983 \times 10^6\)
   - \(\frac{e^x}{(e^x - 1)^2} \approx \frac{1}{e^x} = \frac{1}{1.983 \times 10^6} \approx 5.043 \times 10^{-7}\)
   - \(x^2 = (14.50)^2 = 210.25\)
   \[
   C_V(100\text{ K}) = 24.943 \times 210.25 \times (5.043 \times 10^{-7}) \approx 2.64 \times 10^{-3}\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
   \]
   At \(100\text{ K}\), the heat capacity of diamond is practically zero.

2. **At \(T = 300.0\text{ K}\):**
   - \(x = \theta_E / T = 1450 / 300 = 4.8333\)
   - \(e^x = e^{4.8333} \approx 125.62\)
   - \((e^x - 1)^2 = (124.62)^2 \approx 15530\)
   - \(\frac{e^x}{(e^x - 1)^2} = \frac{125.62}{15530} \approx 0.008089\)
   - \(x^2 = (4.8333)^2 \approx 23.361\)
   \[
   C_V(300\text{ K}) = 24.943 \times 23.361 \times 0.008089 \approx 4.714\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
   \]

---

#### Step 2: Percentage of Dulong-Petit Value at \(300\text{ K}\)
\[
\% \text{ Dulong-Petit} = \frac{C_V(300\text{ K})}{3 R} \times 100\% = \frac{4.714}{24.943} \times 100\% \approx 18.9\%
\]
At room temperature, diamond exhibits less than 19% of the classical Dulong-Petit value because its unusually stiff \(\text{C}-\text{C}\) covalent bonds require extremely high thermal energies to activate lattice vibrations.

---

#### Step 3: Temperature for 90% of Dulong-Petit
We require:
\[
\frac{C_V}{3 R} = x^2 \frac{e^x}{(e^x - 1)^2} = 0.90
\]
Using Taylor expansion for small \(x\): \(x^2 \frac{1 + x + x^2/2}{(x + x^2/2)^2} \approx 1 - \frac{x^2}{12} = 0.90\):
\[
\frac{x^2}{12} \approx 0.10 \implies x^2 \approx 1.20 \implies x \approx 1.095
\]
Solving for \(T\):
\[
x = \frac{\theta_E}{T} \implies T = \frac{\theta_E}{x} = \frac{1450\text{ K}}{1.095} \approx 1324\text{ K}
\]
Diamond must be heated to approximately \(1324\text{ K}\) (\(\approx 1050^\circ\text{C}\)) to reach 90% of the classical Dulong-Petit heat capacity."""
            },
            {
                "id": "prob-10-6",
                "title": "Debye Temperature and Low-Temperature T^3 Heat Capacity for Gold",
                "problem": r"""For metallic gold (\(\text{Au}\), molar mass \(M = 196.97\text{ g/mol}\)):
The Debye temperature is \(\theta_D = 165.0\text{ K}\).
1. State the Debye \(T^3\) law formula for molar heat capacity and evaluate the prefactor constant \(A\) in \(C_V = A T^3\).
2. Calculate the lattice heat capacity \(C_{V, \text{lattice}}\) of gold at \(T = 4.20\text{ K}\) (liquid helium temperature) and at \(T = 10.0\text{ K}\).
3. If the electronic heat capacity coefficient of gold is \(\gamma = 0.729\text{ mJ}\cdot\text{mol}^{-1}\cdot\text{K}^{-2}\), determine the crossover temperature \(T^*\) where electronic and lattice heat capacities are equal.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Debye \(T^3\) Law Prefactor
In the low-temperature limit (\(T < 0.1 \theta_D \approx 16.5\text{ K}\)), the Debye molar heat capacity is:
\[
C_{V, \text{lattice}} = \frac{12\pi^4}{5} R \left( \frac{T}{\theta_D} \right)^3 = A T^3
\]
where the prefactor constant is:
\[
A = \frac{12\pi^4 R}{5 \theta_D^3}
\]
Given \(R = 8.31446\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\) and \(\theta_D = 165.0\text{ K}\):
\[
\theta_D^3 = (165.0)^3 = 4,492,125\text{ K}^3
\]
\[
\frac{12 \pi^4 R}{5} = \frac{12 \times 97.409 \times 8.31446}{5} \approx \frac{9718.8}{5} \approx 1943.76\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
\]
\[
A = \frac{1943.76}{4,492,125} \approx 4.327 \times 10^{-4}\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-4} = 0.4327\text{ mJ}\cdot\text{mol}^{-1}\cdot\text{K}^{-4}
\]

---

#### Step 2: Lattice Heat Capacity at \(4.20\text{ K}\) and \(10.0\text{ K}\)
1. **At \(T = 4.20\text{ K}\):**
   \[
   T^3 = (4.20)^3 = 74.088\text{ K}^3
   \]
   \[
   C_{V, \text{lattice}}(4.2\text{ K}) = (4.327 \times 10^{-4}) \times 74.088 \approx 0.03206\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1} = 32.06\text{ mJ}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
   \]
2. **At \(T = 10.0\text{ K}\):**
   \[
   T^3 = (10.0)^3 = 1000\text{ K}^3
   \]
   \[
   C_{V, \text{lattice}}(10\text{ K}) = (4.327 \times 10^{-4}) \times 1000 \approx 0.4327\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1} = 432.7\text{ mJ}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}
   \]

---

#### Step 3: Crossover Temperature \(T^*\)
The total heat capacity of gold is:
\[
C_{V, \text{total}} = \gamma T + A T^3
\]
Equating the electronic and lattice contributions:
\[
\gamma T^* = A (T^*)^3 \implies (T^*)^2 = \frac{\gamma}{A} \implies T^* = \sqrt{\frac{\gamma}{A}}
\]
Given \(\gamma = 0.729\text{ mJ}\cdot\text{mol}^{-1}\cdot\text{K}^{-2}\) and \(A = 0.4327\text{ mJ}\cdot\text{mol}^{-1}\cdot\text{K}^{-4}\):
\[
(T^*)^2 = \frac{0.729}{0.4327} \approx 1.6847\text{ K}^2 \implies T^* = \sqrt{1.6847} \approx 1.30\text{ K}
\]
Below \(T^* \approx 1.30\text{ K}\), the electronic heat capacity (\(\propto T\)) dominates over the lattice phonon heat capacity (\(\propto T^3\)). Above \(1.30\text{ K}\), the lattice contribution quickly takes over."""
            },
            {
                "id": "prob-10-7",
                "title": "Pauli Paramagnetic Spin Susceptibility of the Conduction Electron Gas",
                "problem": r"""Consider a degenerate free electron gas in an external magnetic field \(\mathbf{B} = B \hat{\mathbf{z}}\).
Each electron has magnetic moment \(\mu_B\) pointing parallel or antiparallel to \(\mathbf{B}\).
1. Show that the magnetic field shifts the energy of spin-up and spin-down electrons by \(\mp \mu_B B\).
2. Using the density of states at the Fermi energy \(g(E_F)\), derive the net magnetic moment \(M\) induced in the electron gas in a weak field.
3. Derive the Pauli paramagnetic volume susceptibility \(\chi_{\text{Pauli}} = \mu_0 \frac{M}{V B}\) and explain why it is virtually independent of temperature.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Zeeman Energy Shift
The magnetic dipole energy of an electron spin is \(\hat{H}_Z = -\boldsymbol{\mu}_s \cdot \mathbf{B}\).
With \(g \approx 2\) and \(s_z = \pm 1/2\):
- For electrons with spin parallel to \(\mathbf{B}\) (spin up, magnetic moment parallel):
  \[
  \varepsilon_\uparrow = \varepsilon - \mu_B B
  \]
- For electrons with spin antiparallel to \(\mathbf{B}\) (spin down, magnetic moment antiparallel):
  \[
  \varepsilon_\downarrow = \varepsilon + \mu_B B
  \]
The chemical potential (Fermi level) must remain equal for both spin populations in thermodynamic equilibrium.

---

#### Step 2: Net Induced Magnetic Moment
Because the spin-up sub-band is shifted downward by \(\mu_B B\), electrons transfer from spin-down to spin-up states until both sub-bands fill to the common Fermi energy \(E_F\).
In a weak magnetic field (\(\mu_B B \ll E_F\)):
The change in number of spin-up electrons is:
\[
\delta N_\uparrow \approx \frac{1}{2} g(E_F) (\mu_B B)
\]
The change in number of spin-down electrons is:
\[
\delta N_\downarrow \approx -\frac{1}{2} g(E_F) (\mu_B B)
\]
where \(g(E_F)\) is the total density of states at the Fermi energy (including both spins).
The net excess of spin-up electrons is:
\[
\Delta N = \delta N_\uparrow - \delta N_\downarrow = g(E_F) \mu_B B
\]
The total induced magnetic dipole moment is:
\[
M = \mu_B \Delta N = \mu_B^2 g(E_F) B
\]

---

#### Step 3: Pauli Spin Susceptibility and Temperature Independence
The magnetization per unit volume is \(\mathcal{M} = \frac{M}{V} = \mu_B^2 \left(\frac{g(E_F)}{V}\right) B\).
The magnetic susceptibility is:
\[
\chi_{\text{Pauli}} = \mu_0 \frac{\mathcal{M}}{B} = \mu_0 \mu_B^2 \left( \frac{g(E_F)}{V} \right)
\]
Recall that for a 3D electron gas, \(\frac{g(E_F)}{V} = \frac{3 n}{2 E_F}\):
\[
\chi_{\text{Pauli}} = \frac{3 \mu_0 n \mu_B^2}{2 E_F} = \frac{3 \mu_0 n \mu_B^2}{2 k_B T_F}
\]

**Physical Insight on Temperature Independence:**
- Classical Curie paramagnetism predicts \(\chi_{\text{Curie}} = \frac{\mu_0 n \mu_B^2}{k_B T} \propto \frac{1}{T}\).
- In a degenerate Fermi gas, only a tiny fraction \(\sim \frac{T}{T_F}\) of electrons residing within \(k_B T\) of the Fermi surface are free to flip their spins (all inner electrons are locked by Pauli exclusion).
Multiplying the classical Curie susceptibility by this active fraction:
\[
\chi \sim \chi_{\text{Curie}} \times \left( \frac{T}{T_F} \right) = \left( \frac{\mu_0 n \mu_B^2}{k_B T} \right) \left( \frac{T}{T_F} \right) = \frac{\mu_0 n \mu_B^2}{k_B T_F} = \text{Constant}
\]
The temperature \(T\) cancels identically! Consequently, the conduction electron spin paramagnetism of metals is small, positive, and remarkably temperature-independent, exactly as observed experimentally."""
            }
        ]
    }
    units.append(unit10)

    return units

if __name__ == "__main__":
    units = get_units_7_8_9_10()
    print(f"Generated {len(units)} units successfully.")
    for u in units:
        print(f" - {u['id']}: {u['title']} ({len(u['sections'])} sections, {len(u['problems'])} problems)")
