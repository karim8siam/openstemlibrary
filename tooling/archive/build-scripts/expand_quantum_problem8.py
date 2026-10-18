"""
expand_quantum_problem8.py
Provides Problem 8 for all 10 units of Quantum Chemistry and Statistical Thermodynamics.
Strictly zero prohibited tokens (no course numbers, no marks, no grades, no exams).
"""

def get_problem8_dict():
    return {
        "unit-1": {
            "id": "prob-1-8",
            "title": "Commutator Algebra, Ehrenfest Theorem & Heisenberg Uncertainty",
            "problem": r"""1. For the position operator \(\hat{x}\) and momentum operator \(\hat{p}_x = -i\hbar \frac{\partial}{\partial x}\), evaluate the fundamental commutator \([\hat{x}, \hat{p}_x]\) and the commutator \([\hat{x}^2, \hat{p}_x]\).
2. Using the generalized Robertson-Schrödinger uncertainty relation \(\sigma_A \sigma_B \ge \frac{1}{2} |\langle [\hat{A}, \hat{B}] \rangle|\), prove that \(\Delta x \Delta p_x \ge \frac{\hbar}{2}\).
3. State Ehrenfest's theorem for the expectation value of momentum \(\frac{d\langle p_x \rangle}{dt}\) and show how it recovers Newton's second law of motion in the classical limit.""",
            "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Commutator Evaluations
1. **Fundamental commutator \([\hat{x}, \hat{p}_x]\):**
   Apply the commutator to an arbitrary test function \(f(x)\):
   \[
   [\hat{x}, \hat{p}_x] f(x) = \hat{x} (\hat{p}_x f) - \hat{p}_x (\hat{x} f) = x \left( -i\hbar \frac{\partial f}{\partial x} \right) - \left( -i\hbar \frac{\partial}{\partial x}(x f) \right)
   \]
   Using the product rule \(\frac{\partial}{\partial x}(x f) = f + x \frac{\partial f}{\partial x}\):
   \[
   [\hat{x}, \hat{p}_x] f(x) = -i\hbar x \frac{\partial f}{\partial x} + i\hbar \left( f + x \frac{\partial f}{\partial x} \right) = i\hbar f(x)
   \]
   Since this holds for any well-behaved function \(f(x)\):
   \[
   [\hat{x}, \hat{p}_x] = i\hbar \hat{I}
   \]
2. **Commutator \([\hat{x}^2, \hat{p}_x]\):**
   Using the operator identity \([\hat{A}\hat{B}, \hat{C}] = \hat{A}[\hat{B}, \hat{C}] + [\hat{A}, \hat{C}]\hat{B}\) with \(\hat{A} = \hat{B} = \hat{x}\) and \(\hat{C} = \hat{p}_x\):
   \[
   [\hat{x}^2, \hat{p}_x] = \hat{x} [\hat{x}, \hat{p}_x] + [\hat{x}, \hat{p}_x] \hat{x} = \hat{x} (i\hbar) + (i\hbar) \hat{x} = 2i\hbar \hat{x}
   \]

---

#### Step 2: Proof of Heisenberg Uncertainty Relation
The Robertson-Schrödinger uncertainty theorem for any two Hermitian operators \(\hat{A}\) and \(\hat{B}\) states:
\[
\sigma_A^2 \sigma_B^2 \ge \left( \frac{1}{2i} \langle [\hat{A}, \hat{B}] \rangle \right)^2 + \left( \frac{1}{2} \langle \{ \Delta\hat{A}, \Delta\hat{B} \} \rangle \right)^2 \ge \frac{1}{4} |\langle [\hat{A}, \hat{B}] \rangle|^2
\]
Substituting \(\hat{A} = \hat{x}\) and \(\hat{B} = \hat{p}_x\):
\[
[\hat{x}, \hat{p}_x] = i\hbar \implies |\langle [\hat{x}, \hat{p}_x] \rangle| = |i\hbar| = \hbar
\]
Therefore:
\[
\sigma_x^2 \sigma_p^2 \ge \frac{1}{4} \hbar^2 \implies \sigma_x \sigma_p \ge \frac{\hbar}{2}
\]
Writing in standard notation \(\Delta x \equiv \sigma_x\) and \(\Delta p_x \equiv \sigma_p\):
\[
\Delta x \Delta p_x \ge \frac{\hbar}{2}
\]
The lower bound \(\hbar/2\) is attained strictly by minimum-uncertainty Gaussian wavepackets.

---

#### Step 3: Ehrenfest Theorem and Classical Limit
For any time-independent operator \(\hat{A}\), the Heisenberg equation of motion yields:
\[
\frac{d\langle A \rangle}{dt} = \frac{i}{\hbar} \langle [\hat{H}, \hat{A}] \rangle
\]
For the momentum operator \(\hat{p}_x\) with Hamiltonian \(\hat{H} = \frac{\hat{p}_x^2}{2m} + V(\hat{x})\):
\[
[\hat{H}, \hat{p}_x] = [V(\hat{x}), \hat{p}_x] = i\hbar \frac{\partial V}{\partial x}
\]
Therefore:
\[
\frac{d\langle p_x \rangle}{dt} = \frac{i}{\hbar} \langle i\hbar \frac{\partial V}{\partial x} \rangle = -\left\langle \frac{\partial V}{\partial x} \right\rangle = \langle F_x \rangle
\]
In the classical macroscopic limit, the wavepacket is tightly localized (\(\Delta x \rightarrow 0\)), so \(\langle \frac{\partial V}{\partial x} \rangle \approx \frac{\partial V}{\partial x}\Big|_{\langle x \rangle}\).
The equation reduces to:
\[
\frac{d\langle p_x \rangle}{dt} = -\frac{dV}{dx}\Big|_{\langle x \rangle} = F_x(\langle x \rangle)
\]
This precisely recovers Newton's second law \(\mathbf{F} = \frac{d\mathbf{p}}{dt}\), proving that classical mechanics emerges as the macroscopic expectation value of quantum mechanics."""
        },
        "unit-2": {
            "id": "prob-2-8",
            "title": "Inversion Tunneling Splitting and Inversion Time in Ammonia",
            "problem": r"""In the ammonia molecule (\(\text{NH}_3\)), the nitrogen atom tunnels through the plane of three hydrogen atoms between two equivalent pyramidal configurations.
The tunnel splitting between the symmetric ground state and antisymmetric first excited state is measured to be \(\Delta\tilde{\nu} = 0.7935\text{ cm}^{-1}\).
1. Calculate the energy splitting \(\Delta E\) in Joules and in electron volts.
2. Determine the microwave inversion tunneling frequency \(\nu_{\text{inv}}\) in GHz.
3. If the nitrogen atom is prepared initially localized in the left pyramidal configuration at \(t = 0\), calculate the time required for complete inversion to the right configuration.""",
            "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Energy Splitting \(\Delta E\)
Given \(\Delta\tilde{\nu} = 0.7935\text{ cm}^{-1}\):
\[
\Delta E = h c \Delta\tilde{\nu}
\]
Using \(h = 6.62607 \times 10^{-34}\text{ J}\cdot\text{s}\) and \(c = 2.99792 \times 10^{10}\text{ cm/s}\):
\[
h c = (6.62607 \times 10^{-34})(2.99792 \times 10^{10}) \approx 1.98645 \times 10^{-23}\text{ J}\cdot\text{cm}
\]
\[
\Delta E = (1.98645 \times 10^{-23}\text{ J}\cdot\text{cm}) \times 0.7935\text{ cm}^{-1} \approx 1.5762 \times 10^{-23}\text{ J}
\]
Converting to electron volts (\(1\text{ eV} = 1.60218 \times 10^{-19}\text{ J}\)):
\[
\Delta E = \frac{1.5762 \times 10^{-23}\text{ J}}{1.60218 \times 10^{-19}\text{ J/eV}} \approx 9.838 \times 10^{-5}\text{ eV} = 98.38\text{ \mu eV}
\]

---

#### Step 2: Inversion Frequency \(\nu_{\text{inv}}\)
\[
\nu_{\text{inv}} = c \Delta\tilde{\nu} = (2.99792 \times 10^{10}\text{ cm/s}) \times 0.7935\text{ cm}^{-1} \approx 2.3789 \times 10^{10}\text{ Hz} = 23.789\text{ GHz}
\]
The inversion transition occurs at \(23.79\text{ GHz}\) in the microwave K-band (\(\lambda \approx 1.26\text{ cm}\)).

---

#### Step 3: Complete Inversion Time \(\tau_{\text{inv}}\)
The wavefunction evolves as:
\[
P_R(t) = \sin^2\left( \frac{\Delta E \, t}{2\hbar} \right) = \sin^2(\pi \nu_{\text{inv}} t)
\]
Complete inversion (\(P_R = 1\)) occurs when the phase reaches \(\pi/2\):
\[
\pi \nu_{\text{inv}} \tau_{\text{inv}} = \frac{\pi}{2} \implies \tau_{\text{inv}} = \frac{1}{2 \nu_{\text{inv}}}
\]
Substitute \(\nu_{\text{inv}} = 2.3789 \times 10^{10}\text{ s}^{-1}\):
\[
\tau_{\text{inv}} = \frac{1}{2 \times 2.3789 \times 10^{10}\text{ s}^{-1}} \approx 2.102 \times 10^{-11}\text{ s} = 21.02\text{ picoseconds}
\]
The nitrogen atom tunnels back and forth through the barrier approximately 24 billion times every second, inverting every 21 picoseconds."""
            },
            "unit-3": {
                "id": "prob-3-8",
                "title": "Rovibrational P-Branch and R-Branch Transitions for HCl",
                "problem": r"""For the fundamental infrared band (\(v = 0 \rightarrow 1\)) of \(^1\text{H}^{35}\text{Cl}\):
The spectroscopic constants are:
- Band origin: \(\tilde{\nu}_0 = 2885.98\text{ cm}^{-1}\)
- Ground state rotational constant: \(B_0 = 10.440\text{ cm}^{-1}\)
- Excited state rotational constant: \(B_1 = 10.137\text{ cm}^{-1}\)
1. Write the explicit formulas for the transition wavenumbers of the R-branch \(\tilde{\nu}_R(J'')\) and P-branch \(\tilde{\nu}_P(J'')\) ignoring centrifugal distortion.
2. Calculate the wavenumbers for the first three lines of the R-branch (\(R(0), R(1), R(2)\)) and P-branch (\(P(1), P(2), P(3)\)).
3. Calculate the spacing between adjacent lines in the R and P branches and explain why lines converge in the R-branch while spreading in the P-branch.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Formulas for Rovibrational Transitions
The term values are \(T(v, J) = G(v) + B_v J(J + 1)\).
The transition wavenumbers from ground state \(J''\) are:
1. **R-branch (\(J' = J'' + 1\)):**
   \[
   \tilde{\nu}_R(J'') = \tilde{\nu}_0 + B_1(J'' + 1)(J'' + 2) - B_0 J''(J'' + 1)
   \]
   Expanding:
   \[
   \tilde{\nu}_R(J'') = \tilde{\nu}_0 + 2 B_1 + (3 B_1 - B_0) J'' + (B_1 - B_0) J''^2
   \]
2. **P-branch (\(J' = J'' - 1\)):**
   \[
   \tilde{\nu}_P(J'') = \tilde{\nu}_0 + B_1(J'' - 1) J'' - B_0 J''(J'' + 1)
   \]
   Expanding:
   \[
   \tilde{\nu}_P(J'') = \tilde{\nu}_0 - (B_1 + B_0) J'' + (B_1 - B_0) J''^2
   \]

---

#### Step 2: Numerical Calculation of Transition Wavenumbers
Given \(\tilde{\nu}_0 = 2885.98\text{ cm}^{-1}\), \(B_0 = 10.440\text{ cm}^{-1}\), \(B_1 = 10.137\text{ cm}^{-1}\):
- \(B_1 - B_0 = 10.137 - 10.440 = -0.303\text{ cm}^{-1}\)
- \(3 B_1 - B_0 = 3(10.137) - 10.440 = 30.411 - 10.440 = 19.971\text{ cm}^{-1}\)
- \(2 B_1 = 20.274\text{ cm}^{-1}\)
- \(B_1 + B_0 = 10.137 + 10.440 = 20.577\text{ cm}^{-1}\)

1. **R-Branch Lines:**
   - \(R(0)\) (\(J'' = 0\)):
     \[
     \tilde{\nu}_R(0) = 2885.98 + 20.274 = 2906.25\text{ cm}^{-1}
     \]
   - \(R(1)\) (\(J'' = 1\)):
     \[
     \tilde{\nu}_R(1) = 2885.98 + 20.274 + 19.971(1) - 0.303(1)^2 = 2906.254 + 19.668 = 2925.92\text{ cm}^{-1}
     \]
   - \(R(2)\) (\(J'' = 2\)):
     \[
     \tilde{\nu}_R(2) = 2885.98 + 20.274 + 19.971(2) - 0.303(4) = 2906.254 + 39.942 - 1.212 = 2944.98\text{ cm}^{-1}
     \]

2. **P-Branch Lines:**
   - \(P(1)\) (\(J'' = 1\)):
     \[
     \tilde{\nu}_P(1) = 2885.98 - 20.577(1) - 0.303(1)^2 = 2885.98 - 20.880 = 2865.10\text{ cm}^{-1}
     \]
   - \(P(2)\) (\(J'' = 2\)):
     \[
     \tilde{\nu}_P(2) = 2885.98 - 20.577(2) - 0.303(4) = 2885.98 - 41.154 - 1.212 = 2843.61\text{ cm}^{-1}
     \]
   - \(P(3)\) (\(J'' = 3\)):
     \[
     \tilde{\nu}_P(3) = 2885.98 - 20.577(3) - 0.303(9) = 2885.98 - 61.731 - 2.727 = 2821.52\text{ cm}^{-1}
     \]

---

#### Step 3: Spacing and Asymmetry Analysis
- Spacings in R-branch:
  - \(R(1) - R(0) = 2925.92 - 2906.25 = 19.67\text{ cm}^{-1}\)
  - \(R(2) - R(1) = 2944.98 - 2925.92 = 19.06\text{ cm}^{-1}\)
  The spacing **decreases** by \(\approx 0.61\text{ cm}^{-1} \approx 2(B_0 - B_1)\).
- Spacings in P-branch:
  - \(P(1) - P(2) = 2865.10 - 2843.61 = 21.49\text{ cm}^{-1}\)
  - \(P(2) - P(3) = 2843.61 - 2821.52 = 22.09\text{ cm}^{-1}\)
  The spacing **increases** by \(\approx 0.60\text{ cm}^{-1} \approx 2(B_0 - B_1)\).
**Physical Reason:**
In higher vibrational states (\(v = 1\)), anharmonic stretching increases the average bond length \(\langle R \rangle\), which increases the moment of inertia \(I\) and decreases the rotational constant (\(B_1 < B_0\)). Because \((B_1 - B_0) < 0\), the quadratic correction shifts all transitions toward lower wavenumbers, compressing lines in the R-branch while spreading them apart in the P-branch."""
            },
            "unit-4": {
                "id": "prob-4-8",
                "title": "Linear Stark Effect Splitting of the n=2 Level of Hydrogen",
                "problem": r"""Consider the \(n = 2\) excited state of atomic hydrogen in an external electric field \(\mathcal{E} = 1.00 \times 10^7\text{ V/m}\) along the \(z\)-axis.
1. The perturbation matrix element between \(2s\) and \(2p_z\) is \(H'_{12} = \langle 2s | e \mathcal{E} z | 2p_z \rangle = -3 e a_0 \mathcal{E}\). Evaluate \(H'_{12}\) in electron volts.
2. Calculate the energy splitting \(\Delta E_{\text{Stark}}\) between the upper and lower Stark levels.
3. Determine the electric dipole moment of the perturbed eigenstates in units of Debye.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Matrix Element Evaluation
Given \(a_0 = 5.29177 \times 10^{-11}\text{ m}\), \(e = 1.60218 \times 10^{-19}\text{ C}\), and \(\mathcal{E} = 1.00 \times 10^7\text{ V/m}\):
\[
|H'_{12}| = 3 e a_0 \mathcal{E}
\]
In Joules:
\[
|H'_{12}| = 3(1.60218 \times 10^{-19}\text{ C})(5.29177 \times 10^{-11}\text{ m})(1.00 \times 10^7\text{ V/m}) \approx 2.5435 \times 10^{-22}\text{ J}
\]
In electron volts:
\[
|H'_{12}| = 3 a_0 \mathcal{E} (\text{in V}) = 3(5.29177 \times 10^{-11}\text{ m})(1.00 \times 10^7\text{ V/m}) \approx 1.5875 \times 10^{-3}\text{ eV} = 1.588\text{ meV}
\]

---

#### Step 2: Energy Splitting \(\Delta E_{\text{Stark}}\)
The secular equation within the \(\{2s, 2p_z\}\) subspace yields eigenvalues:
\[
E^{(1)} = \pm 3 e a_0 \mathcal{E}
\]
The total splitting between the upper and lower levels is:
\[
\Delta E_{\text{Stark}} = E_+^{(1)} - E_-^{(1)} = 6 e a_0 \mathcal{E} = 2 \times (1.5875\text{ meV}) \approx 3.175\text{ meV}
\]
Converting to frequency:
\[
\Delta \nu = \frac{\Delta E}{h} = \frac{2.5435 \times 10^{-22} \times 2}{6.626 \times 10^{-34}} \approx 767.7\text{ GHz}
\]

---

#### Step 3: Induced Electric Dipole Moment
The normalized eigenstates are:
\[
|\psi_\pm\rangle = \frac{1}{\sqrt{2}} (|2s\rangle \mp |2p_z\rangle)
\]
The electric dipole moment operator is \(\hat{d}_z = -e \hat{z}\).
The permanent dipole moment of state \(|\psi_\pm\rangle\) is:
\[
\langle \psi_\pm | \hat{d}_z | \psi_\pm \rangle = \frac{1}{2} [\langle 2s | (-ez) | 2s \rangle + \langle 2p_z | (-ez) | 2p_z \rangle \mp 2 \langle 2s | (-ez) | 2p_z \rangle] = \pm 3 e a_0
\]
Evaluate numerically:
\[
d = 3 e a_0 = 3(1.60218 \times 10^{-19}\text{ C})(5.29177 \times 10^{-11}\text{ m}) \approx 2.5435 \times 10^{-29}\text{ C}\cdot\text{m}
\]
Using \(1\text{ Debye (D)} \approx 3.33564 \times 10^{-30}\text{ C}\cdot\text{m}\):
\[
d = \frac{2.5435 \times 10^{-29}\text{ C}\cdot\text{m}}{3.33564 \times 10^{-30}\text{ C}\cdot\text{m/D}} \approx 7.625\text{ Debye}
\]
Each mixed \(s-p\) hybrid state possesses a gigantic permanent electric dipole moment of \(\pm 7.63\text{ D}\) (larger than the dipole moment of water, which is \(1.85\text{ D}\)), aligning parallel or antiparallel to the field."""
            },
            "unit-5": {
                "id": "prob-5-8",
                "title": "WKB Tunneling Transmission Through a Parabolic Potential Barrier",
                "problem": r"""Consider a particle of mass \(m\) and energy \(E\) encountering an inverted parabolic potential barrier:
\[
V(x) = V_0 - \frac{1}{2} k x^2 \quad \text{for } |x| \le x_0
\]
with \(E < V_0\).
1. Determine the classical turning points \(x_1\) and \(x_2\).
2. Using the WKB approximation, evaluate the barrier penetration integral \(\gamma = \frac{1}{\hbar} \int_{x_1}^{x_2} \sqrt{2m(V(x) - E)} \, dx\).
3. Derive the transmission coefficient \(T(E)\) and show that \(\ln T \propto -(V_0 - E)\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Classical Turning Points
The turning points occur where \(V(x) = E\):
\[
V_0 - \frac{1}{2} k x^2 = E \implies \frac{1}{2} k x^2 = V_0 - E \implies x^2 = \frac{2(V_0 - E)}{k}
\]
Let \(a = \sqrt{\frac{2(V_0 - E)}{k}}\). The turning points are:
\[
x_1 = -a, \quad x_2 = +a
\]

---

#### Step 2: Evaluation of the WKB Barrier Integral
The WKB barrier exponent is:
\[
\gamma = \frac{1}{\hbar} \int_{-a}^a \sqrt{2m \left( V_0 - \frac{1}{2}kx^2 - E \right)} \, dx = \frac{\sqrt{2m}}{\hbar} \int_{-a}^a \sqrt{(V_0 - E) - \frac{1}{2}kx^2} \, dx
\]
Factor out \(\sqrt{V_0 - E}\):
\[
\gamma = \frac{\sqrt{2m(V_0 - E)}}{\hbar} \int_{-a}^a \sqrt{1 - \frac{k x^2}{2(V_0 - E)}} \, dx = \frac{\sqrt{2m(V_0 - E)}}{\hbar} \int_{-a}^a \sqrt{1 - \frac{x^2}{a^2}} \, dx
\]
Let \(x = a \sin\theta\):
\[
\int_{-a}^a \sqrt{1 - \frac{x^2}{a^2}} dx = a \int_{-\pi/2}^{\pi/2} \cos^2\theta \, d\theta = a \left( \frac{\pi}{2} \right) = \frac{\pi a}{2}
\]
Substitute \(a = \sqrt{\frac{2(V_0 - E)}{k}}\):
\[
\gamma = \frac{\sqrt{2m(V_0 - E)}}{\hbar} \frac{\pi}{2} \sqrt{\frac{2(V_0 - E)}{k}} = \frac{\pi}{2\hbar} \sqrt{\frac{4m}{k}} (V_0 - E) = \frac{\pi}{\hbar} \sqrt{\frac{m}{k}} (V_0 - E)
\]
Recognizing \(\omega = \sqrt{k/m}\):
\[
\gamma = \frac{\pi (V_0 - E)}{\hbar \omega}
\]

---

#### Step 3: Transmission Probability \(T(E)\)
In the WKB limit for \(\gamma \gg 1\):
\[
T(E) \approx e^{-2\gamma} = \exp\left[ -\frac{2\pi (V_0 - E)}{\hbar \omega} \right]
\]
Taking natural logarithms:
\[
\ln T(E) = -\frac{2\pi}{\hbar\omega} (V_0 - E)
\]
The tunneling transmission decreases exponentially with barrier height \(V_0 - E\). The exact Kemble barrier formula replaces \(e^{-2\gamma}\) with \(\frac{1}{1 + e^{2\gamma}}\), which correctly gives \(T = 1/2\) at the barrier apex (\(E = V_0\))."""
            },
            "unit-6": {
                "id": "prob-6-8",
                "title": "Hückel Calculation of Benzene vs Cyclobutadiene (Aromatic vs Antiaromatic)",
                "problem": r"""1. For cyclobutadiene (\(\text{C}_4\text{H}_4\), planar 4-membered cyclic ring):
   Solve the \(4 \times 4\) HMO secular determinant to find the orbital energies \(E_k\).
2. Determine the ground-state electron configuration, total \(\pi\)-energy \(E_\pi\), and resonance energy for cyclobutadiene.
3. Compare the delocalization energies of benzene (\(6\pi\)) and cyclobutadiene (\(4\pi\)) to demonstrate Hückel's \(4n + 2\) rule.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: HMO Orbital Energies of Cyclobutadiene
For a 4-membered cyclic ring, the secular determinant is:
\[
\begin{vmatrix} \alpha - E & \beta & 0 & \beta \\ \beta & \alpha - E & \beta & 0 \\ 0 & \beta & \alpha - E & \beta \\ \beta & 0 & \beta & \alpha - E \end{vmatrix} = 0
\]
Let \(x = \frac{\alpha - E}{\beta}\):
\[
\begin{vmatrix} x & 1 & 0 & 1 \\ 1 & x & 1 & 0 \\ 0 & 1 & x & 1 \\ 1 & 0 & 1 & x \end{vmatrix} = x^4 - 4x^2 = x^2(x^2 - 4) = 0
\]
The roots are \(x = 0, 0, \pm 2\).
The orbital energies are:
- \(E_1 = \alpha + 2\beta\) (lowest bonding orbital)
- \(E_2 = E_3 = \alpha\) (doubly degenerate non-bonding orbitals)
- \(E_4 = \alpha - 2\beta\) (highest antibonding orbital)

---

#### Step 2: Ground-State Electronic Structure of Cyclobutadiene
Cyclobutadiene has \(4\) \(\pi\)-electrons:
- 2 electrons pair in the bonding orbital \(E_1\): energy \(2(\alpha + 2\beta) = 2\alpha + 4\beta\).
- By Hund's rule, the remaining 2 electrons occupy the degenerate non-bonding orbitals \(E_2, E_3\) with parallel spins (triplet diradical state): energy \(2\alpha\).
Total \(\pi\)-electron energy:
\[
E_\pi(\text{cyclobutadiene}) = (2\alpha + 4\beta) + 2\alpha = 4\alpha + 4\beta
\]
For two isolated, localized ethylene double bonds:
\[
E_\pi(\text{localized}) = 2 \times [2(\alpha + \beta)] = 4\alpha + 4\beta
\]
The delocalization energy is:
\[
E_{\text{deloc}} = E_\pi(\text{cyclobutadiene}) - E_\pi(\text{localized}) = (4\alpha + 4\beta) - (4\alpha + 4\beta) = 0
\]
Cyclobutadiene gains **zero resonance energy** from cyclic delocalization. Furthermore, the open-shell triplet ground state in a square geometry undergoes a first-order Jahn-Teller distortion to a rectangular geometry with localized alternating double and single bonds.

---

#### Step 3: Comparison and Hückel's Rule Verification
1. **Benzene (\(4n + 2\) with \(n = 1\), \(6\pi\)-electrons):**
   - \(E_\pi = 6\alpha + 8\beta\)
   - Localized reference: \(6\alpha + 6\beta\)
   - Delocalization energy: \(E_{\text{deloc}} = 2\beta \approx -150\text{ kJ/mol}\) (**Aromatic stabilization**)
2. **Cyclobutadiene (\(4n\) with \(n = 1\), \(4\pi\)-electrons):**
   - \(E_\pi = 4\alpha + 4\beta\)
   - Delocalization energy: \(E_{\text{deloc}} = 0\) (**Antiaromatic destabilization**)
This confirms Hückel's \(4n + 2\) rule: rings with \(4n + 2\) electrons have closed bonding shells with large resonance stabilization, while \(4n\) rings have unfilled non-bonding shells, making them highly reactive and unstable."""
            },
            "unit-7": {
                "id": "prob-7-8",
                "title": "Einstein-Smoluchowski Diffusion Coefficient and Avogadro's Number",
                "problem": r"""In a Jean Perrin Brownian motion experiment at \(T = 293.15\text{ K}\) (\(20^\circ\text{C}\)):
Spherical gamboge colloidal particles of radius \(a = 2.12 \times 10^{-7}\text{ m}\) are suspended in water with dynamic viscosity \(\eta = 1.002 \times 10^{-3}\text{ Pa}\cdot\text{s}\).
1. Calculate the frictional drag coefficient \(\gamma = 6\pi \eta a\).
2. The experimentally observed mean square displacement along one axis after \(\tau = 60.0\text{ seconds}\) is \(\langle (\Delta x)^2 \rangle = 1.25 \times 10^{-11}\text{ m}^2\). Calculate the diffusion coefficient \(D\).
3. Using the Einstein-Smoluchowski relation \(D = \frac{k_B T}{\gamma}\), compute Boltzmann's constant \(k_B\) and Avogadro's number \(N_A = R / k_B\) (given \(R = 8.3145\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\)).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Frictional Drag Coefficient \(\gamma\)
Using Stokes' law:
\[
\gamma = 6\pi \eta a = 6 \pi (1.002 \times 10^{-3}\text{ Pa}\cdot\text{s})(2.12 \times 10^{-7}\text{ m})
\]
\[
\gamma = 6 \pi \times 2.1242 \times 10^{-10} \approx 4.004 \times 10^{-9}\text{ kg/s}
\]

---

#### Step 2: Experimental Diffusion Coefficient \(D\)
In 1D Brownian diffusion:
\[
\langle (\Delta x)^2 \rangle = 2 D \tau \implies D = \frac{\langle (\Delta x)^2 \rangle}{2 \tau}
\]
Substitute \(\langle (\Delta x)^2 \rangle = 1.25 \times 10^{-11}\text{ m}^2\) and \(\tau = 60.0\text{ s}\):
\[
D = \frac{1.25 \times 10^{-11}\text{ m}^2}{2 \times 60.0\text{ s}} = \frac{1.25 \times 10^{-11}}{120} \approx 1.0417 \times 10^{-13}\text{ m}^2/\text{s}
\]

---

#### Step 3: Calculation of \(k_B\) and \(N_A\)
From the Einstein relation \(D = \frac{k_B T}{\gamma}\):
\[
k_B = \frac{D \gamma}{T}
\]
Substitute numerical values:
\[
k_B = \frac{(1.0417 \times 10^{-13}\text{ m}^2/\text{s})(4.004 \times 10^{-9}\text{ kg/s})}{293.15\text{ K}} = \frac{4.171 \times 10^{-22}}{293.15} \approx 1.423 \times 10^{-23}\text{ J/K}
\]
Now calculate Avogadro's number \(N_A = \frac{R}{k_B}\):
\[
N_A = \frac{8.3145\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}}{1.423 \times 10^{-23}\text{ J/K}} \approx 5.84 \times 10^{23}\text{ mol}^{-1}
\]
Perrin's historic measurement (\(N_A \approx 6 \times 10^{23}\)) provided the decisive empirical proof that convinced skeptics like Wilhelm Ostwald that atoms and molecules are real physical entities."""
            },
            "unit-8": {
                "id": "prob-8-8",
                "title": "Torsional Partition Function and Hindered Internal Rotation in Ethane",
                "problem": r"""For ethane (\(\text{CH}_3-\text{CH}_3\)) at \(T = 300.0\text{ K}\):
The internal rotation barrier is \(V_3 = 12.0\text{ kJ/mol}\).
The reduced moment of inertia for methyl group rotation is \(I_{\text{red}} = 2.65 \times 10^{-47}\text{ kg}\cdot\text{m}^2\), and the symmetry number is \(\sigma_{\text{int}} = 3\).
1. Calculate the free-rotor partition function \(q_{\text{free}}\) at \(300\text{ K}\).
2. Calculate the torsional vibrational frequency \(\nu_{\text{tors}}\) and the characteristic vibrational temperature \(\theta_{\text{tors}}\) in the harmonic oscillator limit.
3. Compute the harmonic torsional partition function \(q_{\text{tors}}\) and compare it with \(q_{\text{free}}\).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Free-Rotor Partition Function
The 1D free-rotor formula is:
\[
q_{\text{free}} = \frac{1}{\sigma_{\text{int}}} \left( \frac{8\pi^2 I_{\text{red}} k_B T}{h^2} \right)^{1/2}
\]
Evaluate the argument:
\[
8\pi^2 I_{\text{red}} k_B T = 8\pi^2 (2.65 \times 10^{-47}\text{ kg}\cdot\text{m}^2)(1.38065 \times 10^{-23}\text{ J/K})(300\text{ K})
\]
\[
= 8\pi^2 \times 2.65 \times 1.38065 \times 300 \times 10^{-70} \approx 8.665 \times 10^{-67}\text{ J}^2\cdot\text{s}^2
\]
Divide by \(h^2 = (6.626 \times 10^{-34})^2 \approx 4.3905 \times 10^{-67}\):
\[
\frac{8\pi^2 I_{\text{red}} k_B T}{h^2} = \frac{8.665 \times 10^{-67}}{4.3905 \times 10^{-67}} \approx 1.9736
\]
Taking square root:
\[
\sqrt{1.9736} \approx 1.4048
\]
Dividing by \(\sigma_{\text{int}} = 3\):
\[
q_{\text{free}} = \frac{1.4048}{3} \approx 0.468
\]

---

#### Step 2: Torsional Vibrational Frequency in the Harmonic Limit
The barrier per molecule is:
\[
V_3 = \frac{12000\text{ J/mol}}{6.02214 \times 10^{23}\text{ mol}^{-1}} \approx 1.9926 \times 10^{-20}\text{ J}
\]
The effective torsional spring constant is \(k_\phi = \frac{9 V_3}{2}\):
\[
k_\phi = 4.5 \times (1.9926 \times 10^{-20}\text{ J}) \approx 8.967 \times 10^{-20}\text{ J/rad}^2
\]
The torsional frequency is:
\[
\nu_{\text{tors}} = \frac{1}{2\pi} \sqrt{\frac{k_\phi}{I_{\text{red}}}} = \frac{1}{2\pi} \sqrt{\frac{8.967 \times 10^{-20}\text{ J}}{2.65 \times 10^{-47}\text{ kg}\cdot\text{m}^2}} = \frac{1}{2\pi} \sqrt{3.3837 \times 10^{27}} \approx \frac{5.817 \times 10^{13}}{2\pi} \approx 9.258 \times 10^{12}\text{ Hz}
\]
In wavenumber:
\[
\tilde{\nu}_{\text{tors}} = \frac{\nu_{\text{tors}}}{c} = \frac{9.258 \times 10^{12}\text{ s}^{-1}}{2.9979 \times 10^{10}\text{ cm/s}} \approx 308.8\text{ cm}^{-1}
\]
Characteristic temperature:
\[
\theta_{\text{tors}} = \frac{h \nu_{\text{tors}}}{k_B} = 1.43878 \times 308.8 \approx 444.3\text{ K}
\]

---

#### Step 3: Harmonic Torsional Partition Function
At \(T = 300.0\text{ K}\):
\[
\frac{\theta_{\text{tors}}}{T} = \frac{444.3}{300.0} = 1.481
\]
\[
e^{-\theta_{\text{tors}} / T} = e^{-1.481} \approx 0.2274
\]
The harmonic oscillator partition function is:
\[
q_{\text{tors}} = \frac{1}{1 - e^{-\theta_{\text{tors}} / T}} = \frac{1}{1 - 0.2274} = \frac{1}{0.7726} \approx 1.294
\]
Because \(V_3 / k_B T = \frac{12000}{8.314 \times 300} \approx 4.81 > 1\), the potential barrier is substantial compared to thermal energy. Ethane at room temperature behaves predominantly as a torsional harmonic oscillator (\(q \approx 1.29\)) rather than a free internal rotor."""
            },
            "unit-9": {
                "id": "prob-9-8",
                "title": "Second Virial Coefficient and Boyle Temperature for a Model Gas",
                "problem": r"""Consider a model real gas described by the square-well potential:
\[
u(r) = \begin{cases} +\infty & (r < \sigma) \\ -\varepsilon & (\sigma \le r \le \lambda\sigma) \\ 0 & (r > \lambda\sigma) \end{cases}
\]
with hard-core diameter \(\sigma\), well depth \(\varepsilon > 0\), and well width parameter \(\lambda > 1\).
1. Using the statistical formula \(B_2(T) = -2\pi N_A \int_0^\infty (e^{-u(r)/k_B T} - 1) r^2 dr\), derive an analytical expression for \(B_2(T)\) in terms of \(\sigma, \lambda, \varepsilon\), and \(b = \frac{2\pi N_A \sigma^3}{3}\).
2. Determine the Boyle temperature \(T_B\) where \(B_2(T_B) = 0\).
3. For methane (\(\text{CH}_4\)) with \(\sigma = 0.380\text{ nm}\), \(\lambda = 1.60\), and \(\varepsilon / k_B = 150\text{ K}\), calculate \(T_B\) in Kelvin.""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Analytical Derivation of \(B_2(T)\)
Split the radial integral into three distinct piecewise regions:
1. **Region 1 (\(0 \le r < \sigma\), Hard Core):**
   \(u(r) = +\infty \implies e^{-u/k_B T} = 0 \implies e^{-u/k_B T} - 1 = -1\).
   \[
   I_1 = \int_0^\sigma (-1) r^2 dr = -\frac{\sigma^3}{3}
   \]
2. **Region 2 (\(\sigma \le r \le \lambda\sigma\), Attractive Well):**
   \(u(r) = -\varepsilon \implies e^{-u/k_B T} - 1 = e^{\varepsilon / k_B T} - 1\).
   \[
   I_2 = (e^{\varepsilon / k_B T} - 1) \int_\sigma^{\lambda\sigma} r^2 dr = (e^{\varepsilon / k_B T} - 1) \frac{(\lambda^3 - 1)\sigma^3}{3}
   \]
3. **Region 3 (\(r > \lambda\sigma\), Zero Potential):**
   \(u(r) = 0 \implies e^0 - 1 = 0 \implies I_3 = 0\).

Summing the integrals:
\[
\int_0^\infty (e^{-u(r)/k_B T} - 1) r^2 dr = -\frac{\sigma^3}{3} + (e^{\varepsilon / k_B T} - 1) \frac{(\lambda^3 - 1)\sigma^3}{3}
\]
Multiply by \(-2\pi N_A\):
\[
B_2(T) = -2\pi N_A \left[ -\frac{\sigma^3}{3} + (e^{\varepsilon / k_B T} - 1) \frac{(\lambda^3 - 1)\sigma^3}{3} \right] = \frac{2\pi N_A \sigma^3}{3} \left[ 1 - (\lambda^3 - 1)(e^{\varepsilon / k_B T} - 1) \right]
\]
Defining the van der Waals hard-sphere volume \(b = \frac{2\pi N_A \sigma^3}{3}\):
\[
B_2(T) = b \left[ 1 - (\lambda^3 - 1)(e^{\varepsilon / k_B T} - 1) \right]
\]

---

#### Step 2: Determination of the Boyle Temperature \(T_B\)
Setting \(B_2(T_B) = 0\):
\[
1 - (\lambda^3 - 1)(e^{\varepsilon / k_B T_B} - 1) = 0 \implies e^{\varepsilon / k_B T_B} - 1 = \frac{1}{\lambda^3 - 1}
\]
\[
e^{\varepsilon / k_B T_B} = 1 + \frac{1}{\lambda^3 - 1} = \frac{\lambda^3}{\lambda^3 - 1}
\]
Taking natural logarithms:
\[
\frac{\varepsilon}{k_B T_B} = \ln\left( \frac{\lambda^3}{\lambda^3 - 1} \right) \implies T_B = \frac{\varepsilon / k_B}{\ln\left( \frac{\lambda^3}{\lambda^3 - 1} \right)}
\]

---

#### Step 3: Numerical Value for Methane
Given \(\lambda = 1.60\) and \(\varepsilon / k_B = 150.0\text{ K}\):
\[
\lambda^3 = (1.60)^3 = 4.096
\]
\[
\lambda^3 - 1 = 4.096 - 1 = 3.096
\]
\[
\frac{\lambda^3}{\lambda^3 - 1} = \frac{4.096}{3.096} \approx 1.322997
\]
Taking the natural logarithm:
\[
\ln(1.322997) \approx 0.27993
\]
Calculating \(T_B\):
\[
T_B = \frac{150.0\text{ K}}{0.27993} \approx 535.8\text{ K}
\]
The predicted Boyle temperature for methane is approximately \(536\text{ K}\) (\(\approx 263^\circ\text{C}\)), which matches experimental gas compressibility measurements."""
            },
            "unit-10": {
                "id": "prob-10-8",
                "title": "BCS Energy Gap, Critical Temperature, and Critical Field of Lead",
                "problem": r"""For the elemental superconductor lead (\(\text{Pb}\)):
The critical temperature is \(T_c = 7.193\text{ K}\), and the critical magnetic field at absolute zero is \(\mu_0 H_c(0) = 0.0803\text{ Tesla}\) (\(803\text{ Gauss}\)).
1. Using the BCS universal weak-coupling relation \(2\Delta(0) = 3.528 k_B T_c\), calculate the superconducting energy gap \(\Delta(0)\) in Joules and in meV.
2. Calculate the threshold photon frequency \(\nu_{\text{gap}}\) and wavelength \(\lambda_{\text{gap}}\) required to break a Cooper pair at \(0\text{ K}\).
3. Calculate the critical magnetic field \(\mu_0 H_c(T)\) at \(T = 4.20\text{ K}\) (liquid helium boiling point).""",
                "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: BCS Energy Gap Calculation
Given \(T_c = 7.193\text{ K}\):
\[
2\Delta(0) = 3.528 k_B T_c
\]
\[
\Delta(0) = \frac{3.528}{2} k_B T_c = 1.764 (1.38065 \times 10^{-23}\text{ J/K})(7.193\text{ K}) \approx 1.7518 \times 10^{-22}\text{ J}
\]
Converting to millielectron volts (meV):
\[
\Delta(0) = \frac{1.7518 \times 10^{-22}\text{ J}}{1.60218 \times 10^{-19}\text{ J/eV}} \approx 1.0934 \times 10^{-3}\text{ eV} = 1.093\text{ meV}
\]
The total energy gap to create two quasiparticle excitations is:
\[
2\Delta(0) = 2 \times 1.0934\text{ meV} \approx 2.187\text{ meV}
\]
(Experimental measurements on lead yield \(2\Delta(0) \approx 2.7\text{ meV}\) due to strong electron-phonon coupling).

---

#### Step 2: Threshold Photon Frequency and Wavelength
To break a Cooper pair, an incoming photon must have energy \(h \nu \ge 2\Delta(0)\):
\[
\nu_{\text{gap}} = \frac{2\Delta(0)}{h} = \frac{2(1.7518 \times 10^{-22}\text{ J})}{6.62607 \times 10^{-34}\text{ J}\cdot\text{s}} = \frac{3.5036 \times 10^{-22}}{6.62607 \times 10^{-34}} \approx 5.287 \times 10^{11}\text{ Hz} \approx 529\text{ GHz}
\]
The corresponding threshold wavelength is:
\[
\lambda_{\text{gap}} = \frac{c}{\nu_{\text{gap}}} = \frac{2.9979 \times 10^8\text{ m/s}}{5.287 \times 10^{11}\text{ s}^{-1}} \approx 5.67 \times 10^{-4}\text{ m} = 0.567\text{ mm}
\]
Photons in the sub-millimeter far-infrared (terahertz) region are absorbed by breaking Cooper pairs, while microwave photons below \(529\text{ GHz}\) cannot be absorbed at \(0\text{ K}\).

---

#### Step 3: Critical Magnetic Field at \(4.20\text{ K}\)
Using the parabolic temperature dependence:
\[
H_c(T) = H_c(0) \left[ 1 - \left( \frac{T}{T_c} \right)^2 \right]
\]
At \(T = 4.20\text{ K}\) with \(T_c = 7.193\text{ K}\):
\[
\frac{T}{T_c} = \frac{4.20}{7.193} \approx 0.5839
\]
\[
\left( \frac{T}{T_c} \right)^2 \approx (0.5839)^2 \approx 0.3409
\]
\[
1 - \left( \frac{T}{T_c} \right)^2 = 1 - 0.3409 = 0.6591
\]
Therefore:
\[
\mu_0 H_c(4.2\text{ K}) = (0.0803\text{ T}) \times 0.6591 \approx 0.0529\text{ T} = 529\text{ Gauss}
\]
At liquid helium temperature, lead remains superconducting up to a magnetic field of \(0.053\text{ Tesla}\)."""
            }
    }
