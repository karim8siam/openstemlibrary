"""
expand_spectroscopy_problem9.py
Generates Problem 9 for all 10 units of Chemical Spectroscopy (Unit 1 to Unit 10).
Completes the required 9 problems per unit (total 90 solved problems).
Zero prohibited tokens (no course numbers, no marks, no grades, no exams).
"""

def get_unit_problems9():
    problems = {}

    # Unit 1: Problem 9
    problems[1] = {
        "id": "chem-spec-u1-p9",
        "title": "Problem 9: Fellgett and Jacquinot Advantage Quantification in FTIR vs Dispersive Spectrometry",
        "difficulty": "Advanced",
        "statement": r"""A physical chemist is comparing the performance of a modern Fourier Transform Infrared (FTIR) spectrometer equipped with a Michelson interferometer against a classic scanning dispersive grating monochromator for measuring a wide spectral band from \(\tilde{\nu}_1 = 400\text{ cm}^{-1}\) to \(\tilde{\nu}_2 = 4000\text{ cm}^{-1}\) at a resolution of \(\Delta\tilde{\nu} = 2.0\text{ cm}^{-1}\).

Both instruments observe the broad IR source using identical thermal detector elements whose noise is detector-limited (Johnson / thermal noise, independent of photon flux).

1. Calculate the number of spectral resolution elements \(M\) across the scanning window.
2. Formulate and calculate the theoretical Signal-to-Noise Ratio (SNR) enhancement factor afforded by the Fellgett (multiplex) advantage for FTIR over the sequential dispersive instrument assuming identical total observation time \(T = 180\text{ s}\).
3. The Michelson interferometer circular aperture has a solid angle of throughput \(\Omega_{\text{FTIR}} = 0.050\text{ sr}\) with mirror area \(A_{\text{FTIR}} = 20.0\text{ cm}^2\). The dispersive spectrometer entrance slit (to achieve \(2.0\text{ cm}^{-1}\) resolution) restricts throughput to \(\Omega_{\text{disp}} = 0.00125\text{ sr}\) over grating area \(A_{\text{disp}} = 15.0\text{ cm}^2\). Calculate the Jacquinot (throughput) optical advantage ratio \(E_{\text{Jacquinot}} = \frac{A_{\text{FTIR}} \Omega_{\text{FTIR}}}{A_{\text{disp}} \Omega_{\text{disp}}}\).
4. Combine both advantages to estimate the overall theoretical SNR gain factor and determine how much faster the FTIR spectrometer can collect a spectrum of equivalent SNR compared to the dispersive instrument.""",
        "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Calculate the Number of Spectral Resolution Elements \(M\)
The spectral bandwidth covered is:
\[
\Delta\tilde{\nu}_{\text{total}} = \tilde{\nu}_2 - \tilde{\nu}_1 = 4000\text{ cm}^{-1} - 400\text{ cm}^{-1} = 3600\text{ cm}^{-1}
\]
Given the resolution \(\Delta\tilde{\nu} = 2.0\text{ cm}^{-1}\), the total number of independently resolved spectral elements (channels) \(M\) is:
\[
M = \frac{\Delta\tilde{\nu}_{\text{total}}}{\Delta\tilde{\nu}} = \frac{3600\text{ cm}^{-1}}{2.0\text{ cm}^{-1}} = 1800\text{ resolution elements}
\]

---

#### Step 2: Fellgett (Multiplex) Advantage Derivation & Calculation
In a sequential scanning dispersive monochromator, each resolution element \(M\) is sampled for only a fraction of the total measurement duration \(T\):
\[
\tau_{\text{disp}} = \frac{T}{M} = \frac{180\text{ s}}{1800} = 0.10\text{ s per resolution element}
\]
Since the signal accumulates linearly with time (\(S \propto \tau\)) while uncorrelated detector thermal noise (white noise) accumulates with the square root of time (\(N \propto \sqrt{\tau}\)), the signal-to-noise ratio in each channel scales as:
\[
\text{SNR}_{\text{disp}} \propto \frac{\tau_{\text{disp}}}{\sqrt{\tau_{\text{disp}}}} = \sqrt{\tau_{\text{disp}}} = \sqrt{\frac{T}{M}}
\]
In a Fourier transform spectrometer, all \(M\) resolution elements are encoded simultaneously onto the detector during the entire observation time \(T\):
\[
\tau_{\text{FTIR}} = T = 180\text{ s} \implies \text{SNR}_{\text{FTIR}} \propto \sqrt{T}
\]
Taking the ratio of SNRs yields the classic Fellgett (multiplex) enhancement factor:
\[
\xi_{\text{Fellgett}} = \frac{\text{SNR}_{\text{FTIR}}}{\text{SNR}_{\text{disp}}} = \sqrt{\frac{T}{T/M}} = \sqrt{M}
\]
Substituting \(M = 1800\):
\[
\xi_{\text{Fellgett}} = \sqrt{1800} \approx 42.43
\]
Thus, multiplexing alone improves the signal-to-noise ratio by a factor of \(\sim 42.4\) under detector-noise-limited conditions.

---

#### Step 3: Jacquinot (Throughput / Étendue) Optical Advantage
The optical étendue (throughput) \(G = A \cdot \Omega\) dictates the total photon power reaching the detector from an extended incoherent thermal source.
For the Michelson interferometer:
\[
G_{\text{FTIR}} = A_{\text{FTIR}} \cdot \Omega_{\text{FTIR}} = (20.0\text{ cm}^2) \times (0.050\text{ sr}) = 1.00\text{ cm}^2\cdot\text{sr}
\]
For the dispersive monochromator with narrow slit:
\[
G_{\text{disp}} = A_{\text{disp}} \cdot \Omega_{\text{disp}} = (15.0\text{ cm}^2) \times (0.00125\text{ sr}) = 0.01875\text{ cm}^2\cdot\text{sr}
\]
The Jacquinot throughput advantage ratio is:
\[
E_{\text{Jacquinot}} = \frac{G_{\text{FTIR}}}{G_{\text{disp}}} = \frac{1.00}{0.01875} \approx 53.33
\]
Because optical throughput increases the incident photon radiant power by \(53.33\times\) on the detector, the electrical signal increases proportionally by \(53.33\times\) without increasing the detector-limited dark noise. Hence:
\[
\xi_{\text{Jacquinot}} = E_{\text{Jacquinot}} \approx 53.33
\]

---

#### Step 4: Combined Theoretical Advantage and Measurement Speed Gain
Combining the multiplex (Fellgett) and throughput (Jacquinot) advantages:
\[
\text{Total SNR Gain} = \xi_{\text{Fellgett}} \times \xi_{\text{Jacquinot}} = 42.43 \times 53.33 \approx 2263
\]
To achieve an equivalent SNR, measurement time scales inversely with the square of the SNR advantage:
\[
\frac{T_{\text{disp}}}{T_{\text{FTIR}}} = (\text{Total SNR Gain})^2 = (2263)^2 \approx 5.12 \times 10^6
\]
This quantitative result explains why modern FTIR completely displaced dispersive IR instruments in chemical laboratories: collecting an identical high-quality mid-IR spectrum that takes 1 second in FTIR would take months on an equivalent dispersive scanning spectrometer."""
    }

    # Unit 2: Problem 9
    problems[2] = {
        "id": "chem-spec-u2-p9",
        "title": "Problem 9: Pure Rotational Microwave Analysis of Chloromethane with Quadrupole Splitting",
        "difficulty": "Advanced",
        "statement": r"""Chloromethane (\(^{12}\text{CH}_3^{35}\text{Cl}\)) is a prolate symmetric top molecule (\(I_A < I_B = I_C\)) with a non-zero electric quadrupole moment on the \(^{35}\text{Cl}\) nucleus (\(I_{\text{Cl}} = 3/2\)).

1. Formulate the rotational energy levels \(F(J, K)\) in \(\text{cm}^{-1}\) for an unperturbed prolate rotor including rotational constants \(B\) and \(A\), and identify the pure rotational selection rules.
2. Given \(B = 0.44340\text{ cm}^{-1}\) and \(A = 5.205\text{ cm}^{-1}\), calculate the transition frequencies (in GHz) for the \(J = 0 \rightarrow 1\) and \(J = 1 \rightarrow 2\) transitions.
3. Because \(^{35}\text{Cl}\) possesses nuclear spin \(I = 3/2\), the rotational level \(J\) couples with \(I\) to form total angular momentum \(\mathbf{F} = \mathbf{J} + \mathbf{I}\). State the allowed values of \(F\) for the levels \(J = 1\) and \(J = 2\).
4. The first-order nuclear electric quadrupole interaction energy is:
\[
E_Q(J, K, F) = -eQq \left[\frac{3K^2}{J(J+1)} - 1\right] f(I, J, F)
\]
where \(f(I, J, F) = \frac{\frac{3}{4}C(C+1) - I(I+1)J(J+1)}{2I(2I-1)(2J-1)(2J+3)}\) and \(C = F(F+1) - I(I+1) - J(J+1)\). For \(K=0\) and \(eQq = -74.76\text{ MHz}\), calculate the quadrupole shift for the \(J=1, F=5/2\) hyperfine sublevel.""",
        "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Energy Level Expression and Selection Rules
For a prolate symmetric top molecule (\(I_A < I_B = I_C\)), the unperturbed rigid rotor term values are:
\[
F(J, K) = B J(J+1) + (A - B) K^2
\]
where \(J = 0, 1, 2, \dots\) and \(K = -J, -J+1, \dots, +J\).
Because the permanent electric dipole moment \(\boldsymbol{\mu}\) of \(CH_3Cl\) lies entirely along the molecular symmetry axis (the \(a\)-axis), pure rotational transitions obey the selection rules:
\[
\Delta J = +1, \quad \Delta K = 0
\]
The transition wavenumber for \((J, K) \rightarrow (J+1, K)\) is therefore independent of \(K\) and \(A\):
\[
\tilde{\nu} = F(J+1, K) - F(J, K) = 2B(J+1)
\]

---

#### Step 2: Unperturbed Transition Frequencies in GHz
Converting rotational constant \(B\) to frequency units:
\[
B(\text{MHz}) = B(\text{cm}^{-1}) \times c = 0.44340\text{ cm}^{-1} \times 2.99792458 \times 10^{10}\text{ cm/s} \times 10^{-6} = 13292.8\text{ MHz} = 13.2928\text{ GHz}
\]
1. For \(J = 0 \rightarrow 1\):
\[
\nu(0 \rightarrow 1) = 2B(0+1) = 2B = 2 \times 13.2928\text{ GHz} = 26.5856\text{ GHz}
\]
2. For \(J = 1 \rightarrow 2\):
\[
\nu(1 \rightarrow 2) = 2B(1+1) = 4B = 4 \times 13.2928\text{ GHz} = 53.1712\text{ GHz}
\]

---

#### Step 3: Hyperfine Quantum Number Coupling
The total angular momentum is \(\mathbf{F} = \mathbf{J} + \mathbf{I}\). The allowed quantum numbers satisfy:
\[
|J - I| \le F \le J + I
\]
With \(I = 3/2\):
- For \(J = 1\):
  \[
  F \in \{ |1 - 3/2|, \dots, 1 + 3/2 \} = \{ 1/2, 3/2, 5/2 \}
  \]
- For \(J = 2\):
  \[
  F \in \{ |2 - 3/2|, \dots, 2 + 3/2 \} = \{ 1/2, 3/2, 5/2, 7/2 \}
  \]

---

#### Step 4: Quadrupole Energy Shift for \(J=1, K=0, F=5/2\)
Let \(J = 1\), \(I = 3/2\), \(F = 5/2\), and \(K = 0\).
First, evaluate Casimir's parameter \(C\):
\[
C = F(F+1) - I(I+1) - J(J+1)
\]
\[
F(F+1) = \frac{5}{2} \times \frac{7}{2} = \frac{35}{4} = 8.75
\]
\[
I(I+1) = \frac{3}{2} \times \frac{5}{2} = \frac{15}{4} = 3.75
\]
\[
J(J+1) = 1 \times 2 = 2
\]
\[
C = 8.75 - 3.75 - 2 = 3.00
\]
Next, evaluate Casimir's polynomial in the numerator:
\[
\text{Num} = \frac{3}{4}C(C+1) - I(I+1)J(J+1) = \frac{3}{4}(3)(4) - (3.75)(2) = 9.0 - 7.5 = 1.5
\]
Now evaluate the denominator:
\[
\text{Denom} = 2 I (2I - 1)(2J - 1)(2J + 3)
\]
\[
2(3/2) = 3, \quad 2(3/2) - 1 = 2, \quad 2(1) - 1 = 1, \quad 2(1) + 3 = 5
\]
\[
\text{Denom} = 3 \times 2 \times 1 \times 5 = 30
\]
Thus, Casimir's function is:
\[
f(I, J, F) = \frac{1.5}{30} = 0.050
\]
The geometric orientation factor for \(K = 0\) is:
\[
\left[\frac{3K^2}{J(J+1)} - 1\right] = \left[0 - 1\right] = -1
\]
Therefore, the quadrupole shift is:
\[
E_Q(1, 0, 5/2) = -(-74.76\text{ MHz}) \times (-1) \times (0.050) = -3.738\text{ MHz}
\]
This precisely explains the observable high-resolution microwave triplet splitting for the \(J = 0 \rightarrow 1\) line of \(CH_3Cl\)."""
    }

    # Unit 3: Problem 9
    problems[3] = {
        "id": "chem-spec-u3-p9",
        "title": "Problem 9: Fermi Resonance Deconvolution and Coupling Matrix Element in Carbon Dioxide",
        "difficulty": "Advanced",
        "statement": r"""In the Raman spectrum of gaseous carbon dioxide (\(\text{CO}_2\)), instead of a single symmetric stretch fundamental \(\nu_1\), one observes a pronounced doublet at \(\tilde{\nu}_+ = 1388.2\text{ cm}^{-1}\) and \(\tilde{\nu}_- = 1285.4\text{ cm}^{-1}\) with an integrated intensity ratio of \(\frac{I_+}{I_-} = 1.15\).

This perturbation arises from an accidental Fermi resonance between the fundamental symmetric stretching state \(|10^00\rangle\) and the overtone of the bending mode \(|02^00\rangle\).

1. State the symmetry species of \(|10^00\rangle\) and \(|02^00\rangle\) in the \(D_{\infty h}\) point group and explain why cubic anharmonic coupling can mix them.
2. Formulate the two-state perturbation secular determinant in terms of unperturbed energies \(E_a^0, E_b^0\) and cubic anharmonic coupling matrix element \(W = \langle 10^00 | \hat{H}_{\text{anharm}} | 02^00 \rangle\).
3. Using the observed peak positions \(\tilde{\nu}_+\) and \(\tilde{\nu}_-\) and the intensity ratio \(\frac{I_+}{I_-} = 1.15\) (assuming intrinsic Raman activity arises solely from the fundamental \(|10^00\rangle\)), calculate:
   - The mixing coefficients \(c_a\) and \(c_b\) where \(|\psi_+\rangle = c_a |10^00\rangle + c_b |02^00\rangle\).
   - The unperturbed vibrational frequencies \(\nu_1^0\) and \(2\nu_2^0\).
   - The magnitude of the anharmonic coupling constant \(|W|\) in \(\text{cm}^{-1}\).""",
        "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Symmetry Analysis and Fermi Resonance Condition
In linear carbon dioxide (\(D_{\infty h}\)):
- The symmetric stretch \(Q_1\) transforms as \(\Sigma_g^+\). Thus state \(|10^00\rangle\) has symmetry \(\Sigma_g^+\).
- The degenerate bending mode \(Q_2\) transforms as \(\Pi_u\). The first overtone gives direct product states:
  \[
  \Pi_u \otimes \Pi_u = \Sigma_g^+ \oplus [\Sigma_u^-] \oplus \Delta_g
  \]
  The \(l=0\) component \(|02^00\rangle\) has exactly \(\Sigma_g^+\) symmetry.
Since both states belong to the identical irreducible representation \(\Sigma_g^+\), the cubic anharmonic potential term \(k_{122} Q_1 (Q_{2x}^2 + Q_{2y}^2)\) (which transforms as totally symmetric \(\Sigma_g^+\)) mediates a non-zero coupling:
\[
W = \langle 10^00 | k_{122} Q_1 Q_2^2 | 02^00 \rangle \neq 0
\]

---

#### Step 2: Two-State Secular Determinant
The Hamiltonian matrix in the unperturbed basis \(\{|a\rangle = |10^00\rangle, |b\rangle = |02^00\rangle\}\) is:
\[
\mathbf{H} = \begin{pmatrix} E_a^0 & W \\ W & E_b^0 \end{pmatrix}
\]
Diagonalizing gives eigenvalues:
\[
E_\pm = \frac{E_a^0 + E_b^0}{2} \pm \frac{1}{2} \sqrt{(E_a^0 - E_b^0)^2 + 4W^2}
\]
Let \(\delta_0 = E_a^0 - E_b^0\) be the unperturbed separation and \(\Delta = E_+ - E_-\) be the observed doublet separation:
\[
\Delta = \tilde{\nu}_+ - \tilde{\nu}_- = 1388.2 - 1285.4 = 102.8\text{ cm}^{-1}
\]
Notice also that:
\[
E_+ + E_- = E_a^0 + E_b^0 = 1388.2 + 1285.4 = 2673.6\text{ cm}^{-1}
\]

---

#### Step 3: Determining Mixing Coefficients and Unperturbed Parameters
The perturbed eigenfunctions are:
\[
|\psi_+\rangle = \cos\theta |a\rangle + \sin\theta |b\rangle
\]
\[
|\psi_-\rangle = -\sin\theta |a\rangle + \cos\theta |b\rangle
\]
Assuming the bending overtone \(|b\rangle = |02^00\rangle\) has negligible zero-order Raman polarizability derivative (\(\alpha_b \approx 0\)), all transition intensity originates from \(|a\rangle = |10^00\rangle\):
\[
I_+ \propto |\langle 0 | \hat{\alpha} | \psi_+ \rangle|^2 = \cos^2\theta |\langle 0 | \hat{\alpha} | a \rangle|^2
\]
\[
I_- \propto |\langle 0 | \hat{\alpha} | \psi_- \rangle|^2 = \sin^2\theta |\langle 0 | \hat{\alpha} | a \rangle|^2
\]
The intensity ratio is:
\[
\frac{I_+}{I_-} = \frac{\cos^2\theta}{\sin^2\theta} = \cot^2\theta = 1.15
\]
Solving for \(\tan\theta\):
\[
\tan\theta = \frac{1}{\sqrt{1.15}} = \frac{1}{1.0724} \approx 0.9325 \implies \theta \approx 43.0^\circ
\]
Evaluating the coefficients:
\[
c_a = \cos(43.0^\circ) \approx 0.7314, \quad c_b = \sin(43.0^\circ) \approx 0.6820
\]
(Check normalization: \(0.7314^2 + 0.6820^2 = 0.5349 + 0.4651 = 1.000\)).

From standard two-level mixing theory:
\[
\cos(2\theta) = \frac{\delta_0}{\Delta}
\]
Evaluating \(\cos(2\theta)\) where \(2\theta = 86.0^\circ\):
\[
\cos(86.0^\circ) \approx 0.06976
\]
Therefore, the unperturbed energy difference \(\delta_0\) is:
\[
\delta_0 = \Delta \cos(2\theta) = 102.8\text{ cm}^{-1} \times 0.06976 \approx 7.17\text{ cm}^{-1}
\]
Now solve for the individual unperturbed levels:
\[
E_a^0 + E_b^0 = 2673.6\text{ cm}^{-1}
\]
\[
E_a^0 - E_b^0 = 7.17\text{ cm}^{-1}
\]
Adding the two equations:
\[
2E_a^0 = 2680.77 \implies E_a^0 = \nu_1^0 = 1340.39\text{ cm}^{-1}
\]
Subtracting:
\[
E_b^0 = 2\nu_2^0 = 1333.21\text{ cm}^{-1}
\]
Finally, calculating the coupling matrix element \(|W|\):
\[
\sin(2\theta) = \frac{2|W|}{\Delta} \implies |W| = \frac{\Delta}{2} \sin(2\theta)
\]
\[
\sin(86.0^\circ) \approx 0.9976
\]
\[
|W| = \frac{102.8}{2} \times 0.9976 = 51.4 \times 0.9976 \approx 51.27\text{ cm}^{-1}
\]
The unperturbed states lie merely \(7.17\text{ cm}^{-1}\) apart, but their strong Fermi resonance coupling (\(|W| \approx 51.3\text{ cm}^{-1}\)) repels them into the well-known \(102.8\text{ cm}^{-1}\) doublet!"""
    }

    # Unit 4: Problem 9
    problems[4] = {
        "id": "chem-spec-u4-p9",
        "title": "Problem 9: Raman Depolarization Ratio and Polarizability Invariant Analysis of Carbon Tetrachloride",
        "difficulty": "Advanced",
        "statement": r"""A linearly polarized continuous-wave laser (\(\lambda_0 = 532\text{ nm}\)) propagating along the \(y\)-axis with its electric field polarized along the \(z\)-axis irradiates a liquid sample of carbon tetrachloride (\(\text{CCl}_4\)). Raman scattering is collected at a \(90^\circ\) angle along the \(x\)-axis through a linear polarization analyzer oriented parallel (\(I_\parallel\), along \(z\)) and perpendicular (\(I_\perp\), along \(y\)) to the incident polarization.

The four fundamental vibrational normal modes of tetrahedral \(\text{CCl}_4\) (\(T_d\) point group) have frequencies:
- \(\nu_1 = 459\text{ cm}^{-1}\) (\(A_1\), symmetric \(\text{C-Cl}\) breathing)
- \(\nu_2 = 218\text{ cm}^{-1}\) (\(E\), deformation)
- \(\nu_3 = 776\text{ cm}^{-1}\) (\(T_2\), asymmetric stretch)
- \(\nu_4 = 314\text{ cm}^{-1}\) (\(T_2\), asymmetric bend)

1. Formulate the depolarization ratio \(\rho_p\) in terms of the isotropic polarizability derivative invariant \(a^2\) and anisotropic invariant \(\gamma^2\).
2. State the theoretical selection rules for depolarization ratio \(\rho_p\) for totally symmetric vs non-totally symmetric vibrational modes.
3. For the \(\nu_1\) band (\(459\text{ cm}^{-1}\)), experiment measures \(I_\parallel = 24500\text{ counts}\) and \(I_\perp = 122\text{ counts}\). Calculate the experimental depolarization ratio \(\rho_p\) and determine the ratio of anisotropic to isotropic polarizability invariants \(\gamma^2 / a^2\).
4. Predict the theoretical value of \(\rho_p\) for \(\nu_2, \nu_3\), and \(\nu_4\) based on symmetry arguments.""" ,
        "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Definition of Depolarization Ratio and Polarizability Invariants
In a \(90^\circ\) scattering geometry with incident linearly polarized radiation along the \(z\)-axis:
\[
\rho_p = \frac{I_\perp}{I_\parallel} = \frac{I_y}{I_z}
\]
The orientational average of the Raman scattering tensor yields:
\[
I_\parallel \propto 45 a^2 + 4 \gamma^2
\]
\[
I_\perp \propto 3 \gamma^2
\]
where:
- \(a = \frac{1}{3} (\alpha_{xx}' + \alpha_{yy}' + \alpha_{zz}')\) is the mean (isotropic) polarizability derivative invariant.
- \(\gamma^2 = \frac{1}{2}[(\alpha_{xx}' - \alpha_{yy}')^2 + (\alpha_{yy}' - \alpha_{zz}')^2 + (\alpha_{zz}' - \alpha_{xx}')^2 + 6(\alpha_{xy}'^2 + \alpha_{yz}'^2 + \alpha_{zx}'^2)]\) is the anisotropic invariant.
Therefore:
\[
\rho_p = \frac{3\gamma^2}{45 a^2 + 4\gamma^2}
\]

---

#### Step 2: Symmetry Criteria for \(\rho_p\)
1. **Non-totally symmetric modes** (e.g., \(E, T_1, T_2\) in \(T_d\)):
   The trace of the polarizability tensor derivative must be identically zero by symmetry: \(a = 0\).
   Substituting \(a = 0\):
   \[
   \rho_p = \frac{3\gamma^2}{0 + 4\gamma^2} = \frac{3}{4} = 0.75
   \]
   Such bands are classified as **depolarized**.
2. **Totally symmetric modes** (e.g., \(A_1\) in \(T_d\)):
   The mean polarizability derivative is non-zero (\(a \neq 0\)). Since \(\gamma^2 \ge 0\):
   \[
   0 \le \rho_p < \frac{3}{4}
   \]
   Such bands are classified as **polarized**. For an ideal spherical isotropic vibrator (\(\gamma^2 = 0\)), \(\rho_p = 0\).

---

#### Step 3: Experimental Depolarization Calculation for \(\nu_1\) (\(459\text{ cm}^{-1}\))
Given:
\[
I_\parallel = 24500\text{ counts}, \quad I_\perp = 122\text{ counts}
\]
The experimental depolarization ratio is:
\[
\rho_p(\nu_1) = \frac{I_\perp}{I_\parallel} = \frac{122}{24500} \approx 0.00498 \approx 0.005
\]
Since \(\rho_p \ll 0.75\), the band is strongly polarized, confirming complete conservation of spherical symmetry during the symmetric breathing vibration.

To find the ratio \(\frac{\gamma^2}{a^2}\):
\[
\rho_p (45 a^2 + 4 \gamma^2) = 3 \gamma^2 \implies 45 \rho_p a^2 = (3 - 4\rho_p) \gamma^2
\]
\[
\frac{\gamma^2}{a^2} = \frac{45 \rho_p}{3 - 4\rho_p} = \frac{45 \times 0.00498}{3 - 4(0.00498)} = \frac{0.2241}{3 - 0.0199} = \frac{0.2241}{2.9801} \approx 0.0752
\]
The anisotropy invariant is less than \(8\%\) of the isotropic invariant, demonstrating that the polarizability ellipsoid expands and contracts isotropically with negligible distortion.

---

#### Step 4: Theoretical Predictions for \(\nu_2, \nu_3, \nu_4\)
- \(\nu_2 = 218\text{ cm}^{-1}\) belongs to the doubly degenerate \(E\) representation. Since \(E \neq A_1\), \(a = 0 \implies \rho_p = 0.75\) (**depolarized**).
- \(\nu_3 = 776\text{ cm}^{-1}\) belongs to the triply degenerate \(T_2\) representation. Since \(T_2 \neq A_1\), \(a = 0 \implies \rho_p = 0.75\) (**depolarized**).
- \(\nu_4 = 314\text{ cm}^{-1}\) belongs to the triply degenerate \(T_2\) representation. Since \(T_2 \neq A_1\), \(a = 0 \implies \rho_p = 0.75\) (**depolarized**)."""
    }

    # Unit 5: Problem 9
    problems[5] = {
        "id": "chem-spec-u5-p9",
        "title": "Problem 9: Anomalous Zeeman Splitting Pattern and Energy Shifts for the Sodium D Lines",
        "difficulty": "Advanced",
        "statement": r"""The prominent yellow emission of gas-phase atomic sodium consists of the doublet \(D_1\) and \(D_2\) lines originating from the electric dipole transitions:
- \(D_1\): \(^2P_{1/2} \rightarrow {}^2S_{1/2}\) at \(\lambda_1 = 589.6\text{ nm}\)
- \(D_2\): \(^2P_{3/2} \rightarrow {}^2S_{1/2}\) at \(\lambda_2 = 589.0\text{ nm}\)

When placed in a uniform external magnetic field \(B_0 = 1.20\text{ T}\) (weak field regime, \(\mu_B B_0 \ll \Delta E_{\text{spin-orbit}}\)):

1. Calculate the Landé \(g\)-factor \(g_J\) for the three states: \(^2S_{1/2}\), \(^2P_{1/2}\), and \(^2P_{3/2}\).
2. Determine the magnetic quantum numbers \(M_J\) and evaluate the Zeeman energy shifts \(\Delta E(J, M_J) = g_J \mu_B B_0 M_J\) in \(\mu\text{eV}\) and in \(\text{cm}^{-1}\) for all sub-levels (given Bohr magneton \(\mu_B = 5.78838 \times 10^{-5}\text{ eV/T} = 0.46686\text{ cm}^{-1}/\text{T}\)).
3. Apply the electric dipole selection rules \(\Delta M_J = 0\) (\(\pi\) transitions) and \(\Delta M_J = \pm 1\) (\(\sigma\) transitions) to find:
   - The total number of Zeeman spectral components for the \(D_1\) line and their shifts relative to the unperturbed line center.
   - The total number of Zeeman spectral components for the \(D_2\) line and their shifts relative to the unperturbed line center.""",
        "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Landé \(g\)-Factor Calculations
The Landé \(g\)-factor is given by:
\[
g_J = 1 + \frac{J(J+1) + S(S+1) - L(L+1)}{2J(J+1)}
\]
For all states of neutral sodium, \(S = 1/2 \implies S(S+1) = 3/4\).
1. **Ground state \(^2S_{1/2}\)**: \(L = 0, J = 1/2, J(J+1) = 3/4\):
   \[
   g(^2S_{1/2}) = 1 + \frac{3/4 + 3/4 - 0}{2(3/4)} = 1 + \frac{1.5}{1.5} = 2.000
   \]
2. **Excited state \(^2P_{1/2}\)**: \(L = 1, L(L+1) = 2, J = 1/2, J(J+1) = 3/4\):
   \[
   g(^2P_{1/2}) = 1 + \frac{3/4 + 3/4 - 2}{2(3/4)} = 1 + \frac{1.5 - 2}{1.5} = 1 - \frac{1}{3} = \frac{2}{3} \approx 0.667
   \]
3. **Excited state \(^2P_{3/2}\)**: \(L = 1, L(L+1) = 2, J = 3/2, J(J+1) = 15/4\):
   \[
   g(^2P_{3/2}) = 1 + \frac{15/4 + 3/4 - 2}{2(15/4)} = 1 + \frac{4.5 - 2}{7.5} = 1 + \frac{2.5}{7.5} = 1 + \frac{1}{3} = \frac{4}{3} \approx 1.333
   \]

---

#### Step 2: Energy Level Shifts for \(B_0 = 1.20\text{ T}\)
The unit Zeeman splitting unit is:
\[
\delta_{\text{mag}} = \mu_B B_0 = (0.46686\text{ cm}^{-1}/\text{T}) \times 1.20\text{ T} = 0.56023\text{ cm}^{-1}
\]
In energy units:
\[
\mu_B B_0 = (5.78838 \times 10^{-5}\text{ eV/T}) \times 1.20\text{ T} = 6.946 \times 10^{-5}\text{ eV} = 69.46\text{ }\mu\text{eV}
\]
Now evaluating \(\Delta E = g_J M_J \delta_{\text{mag}}\):
- **\(^2S_{1/2}\)** (\(g = 2\)):
  - \(M_J = +1/2\): \(\Delta E = 2(+1/2)\delta_{\text{mag}} = +1.00 \delta_{\text{mag}} = +0.5602\text{ cm}^{-1}\)
  - \(M_J = -1/2\): \(\Delta E = 2(-1/2)\delta_{\text{mag}} = -1.00 \delta_{\text{mag}} = -0.5602\text{ cm}^{-1}\)
- **\(^2P_{1/2}\)** (\(g = 2/3\)):
  - \(M_J = +1/2\): \(\Delta E = (2/3)(+1/2)\delta_{\text{mag}} = +1/3 \delta_{\text{mag}} = +0.1867\text{ cm}^{-1}\)
  - \(M_J = -1/2\): \(\Delta E = (2/3)(-1/2)\delta_{\text{mag}} = -1/3 \delta_{\text{mag}} = -0.1867\text{ cm}^{-1}\)
- **\(^2P_{3/2}\)** (\(g = 4/3\)):
  - \(M_J = +3/2\): \(\Delta E = (4/3)(+3/2)\delta_{\text{mag}} = +2.00 \delta_{\text{mag}} = +1.1205\text{ cm}^{-1}\)
  - \(M_J = +1/2\): \(\Delta E = (4/3)(+1/2)\delta_{\text{mag}} = +2/3 \delta_{\text{mag}} = +0.3735\text{ cm}^{-1}\)
  - \(M_J = -1/2\): \(\Delta E = (4/3)(-1/2)\delta_{\text{mag}} = -2/3 \delta_{\text{mag}} = -0.3735\text{ cm}^{-1}\)
  - \(M_J = -3/2\): \(\Delta E = (4/3)(-3/2)\delta_{\text{mag}} = -2.00 \delta_{\text{mag}} = -1.1205\text{ cm}^{-1}\)

---

#### Step 3: Transition Frequencies and Patterns
Transition frequency shift:
\[
\Delta\tilde{\nu}_{\text{trans}} = \Delta E_{\text{upper}} - \Delta E_{\text{lower}} = [g_{\text{upper}} M_J' - g_{\text{lower}} M_J''] \delta_{\text{mag}}
\]

**1. \(D_1\) Line (\(^2P_{1/2} \rightarrow {}^2S_{1/2}\)):**
Allowed transitions (\(\Delta M_J = 0, \pm 1\)):
- \(\pi\) transitions (\(\Delta M_J = 0\)):
  1. \(M_J': +1/2 \rightarrow M_J'': +1/2 \implies \Delta\tilde{\nu} = (1/3 - 1)\delta_{\text{mag}} = -2/3 \delta_{\text{mag}} = -0.3735\text{ cm}^{-1}\)
  2. \(M_J': -1/2 \rightarrow M_J'': -1/2 \implies \Delta\tilde{\nu} = (-1/3 - (-1))\delta_{\text{mag}} = +2/3 \delta_{\text{mag}} = +0.3735\text{ cm}^{-1}\)
- \(\sigma\) transitions (\(\Delta M_J = \pm 1\)):
  3. \(M_J': +1/2 \rightarrow M_J'': -1/2 \implies \Delta\tilde{\nu} = (1/3 - (-1))\delta_{\text{mag}} = +4/3 \delta_{\text{mag}} = +0.7470\text{ cm}^{-1}\)
  4. \(M_J': -1/2 \rightarrow M_J'': +1/2 \implies \Delta\tilde{\nu} = (-1/3 - 1)\delta_{\text{mag}} = -4/3 \delta_{\text{mag}} = -0.7470\text{ cm}^{-1}\)
Total components for \(D_1\): **4 lines** (quartet at \(\pm 2/3 \delta_{\text{mag}}, \pm 4/3 \delta_{\text{mag}}\)).

**2. \(D_2\) Line (\(^2P_{3/2} \rightarrow {}^2S_{1/2}\)):**
Allowed transitions:
- \(\pi\) transitions (\(\Delta M_J = 0\)):
  1. \(+1/2 \rightarrow +1/2 \implies \Delta\tilde{\nu} = (2/3 - 1)\delta_{\text{mag}} = -1/3 \delta_{\text{mag}} = -0.1867\text{ cm}^{-1}\)
  2. \(-1/2 \rightarrow -1/2 \implies \Delta\tilde{\nu} = (-2/3 - (-1))\delta_{\text{mag}} = +1/3 \delta_{\text{mag}} = +0.1867\text{ cm}^{-1}\)
- \(\sigma\) transitions (\(\Delta M_J = \pm 1\)):
  3. \(+3/2 \rightarrow +1/2 \implies \Delta\tilde{\nu} = (2 - 1)\delta_{\text{mag}} = +1 \delta_{\text{mag}} = +0.5602\text{ cm}^{-1}\)
  4. \(+1/2 \rightarrow -1/2 \implies \Delta\tilde{\nu} = (2/3 - (-1))\delta_{\text{mag}} = +5/3 \delta_{\text{mag}} = +0.9337\text{ cm}^{-1}\)
  5. \(-1/2 \rightarrow +1/2 \implies \Delta\tilde{\nu} = (-2/3 - 1)\delta_{\text{mag}} = -5/3 \delta_{\text{mag}} = -0.9337\text{ cm}^{-1}\)
  6. \(-3/2 \rightarrow -1/2 \implies \Delta\tilde{\nu} = (-2 - (-1))\delta_{\text{mag}} = -1 \delta_{\text{mag}} = -0.5602\text{ cm}^{-1}\)
Total components for \(D_2\): **6 lines** (sextet at \(\pm 1/3, \pm 1, \pm 5/3 \delta_{\text{mag}}\))."""
    }

    # Unit 6: Problem 9
    problems[6] = {
        "id": "chem-spec-u6-p9",
        "title": "Problem 9: Isosbestic Point Analysis and Spectrophotometric Acid Dissociation Constant Determination",
        "difficulty": "Advanced",
        "statement": r"""A biochemist investigates the protonation equilibrium of an indicator dye \(\text{HIn} \rightleftharpoons \text{H}^+ + \text{In}^-\) across a buffer series from \(\text{pH} = 5.00\) to \(\text{pH} = 9.00\) at a constant total analytical concentration \(C_T = 4.00 \times 10^{-5}\text{ M}\) and optical path length \(b = 1.00\text{ cm}\).

The series of UV-Vis spectra exhibits a sharp crossing point (isosbestic point) at \(\lambda_{\text{iso}} = 492\text{ nm}\) where the absorbance remains strictly constant at \(A_{\text{iso}} = 0.520\) across all pH values.
At an analytical monitoring wavelength \(\lambda_{\text{anal}} = 550\text{ nm}\):
- In strong acid (\(\text{pH} = 2.0\)), the indicator exists entirely as \(\text{HIn}\), yielding \(A_{\text{acid}} = 0.080\).
- In strong base (\(\text{pH} = 12.0\)), the indicator exists entirely as \(\text{In}^-\), yielding \(A_{\text{base}} = 0.840\).
- At \(\text{pH} = 7.20\), the measured absorbance is \(A = 0.612\).

1. Prove mathematically using the Beer-Lambert law why an isosbestic point occurs only when the molar absorption coefficients of the two equilibrating species are identical (\(\epsilon_{\text{HIn}} = \epsilon_{\text{In}^-}\)) and calculate \(\epsilon_{\text{iso}}\) at \(492\text{ nm}\).
2. Derive the linear expression relating measured absorbance \(A\) at \(550\text{ nm}\) to the solution pH and acid dissociation constant \(\text{p}K_a\).
3. Calculate the molar fraction \(\alpha_{\text{In}^-}\) of the deprotonated form at \(\text{pH} = 7.20\).
4. Calculate the thermodynamic \(\text{p}K_a\) and \(K_a\) of the indicator.""" ,
        "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Mathematical Proof and Significance of the Isosbestic Point
By mass balance, the total analytical concentration is:
\[
C_T = [\text{HIn}] + [\text{In}^-]
\]
At any wavelength \(\lambda\) with path length \(b = 1.00\text{ cm}\), the total absorbance is the linear sum of contributions:
\[
A(\lambda) = \epsilon_{\text{HIn}}(\lambda) b [\text{HIn}] + \epsilon_{\text{In}^-}(\lambda) b [\text{In}^-]
\]
Substitute \([\text{HIn}] = C_T - [\text{In}^-]\):
\[
A(\lambda) = \epsilon_{\text{HIn}}(\lambda) b C_T + [\epsilon_{\text{In}^-}(\lambda) - \epsilon_{\text{HIn}}(\lambda)] b [\text{In}^-]
\]
For the absorbance \(A(\lambda)\) to remain strictly invariant with solution pH (and hence invariant with changing \([\text{In}^-]\)):
\[
\frac{\partial A(\lambda)}{\partial [\text{In}^-]} = [\epsilon_{\text{In}^-}(\lambda) - \epsilon_{\text{HIn}}(\lambda)] b = 0 \iff \epsilon_{\text{HIn}}(\lambda) = \epsilon_{\text{In}^-}(\lambda)
\]
Thus, an isosbestic point conclusively proves that exactly two absorbing species interconvert stoichiometrically without intermediate aggregates or side reactions.

At \(\lambda_{\text{iso}} = 492\text{ nm}\):
\[
\epsilon_{\text{iso}} = \frac{A_{\text{iso}}}{b C_T} = \frac{0.520}{(1.00\text{ cm})(4.00 \times 10^{-5}\text{ M})} = 13000\text{ M}^{-1}\text{cm}^{-1}
\]

---

#### Step 2: Derivation of the Spectrophotometric Henderson-Hasselbalch Equation
At \(\lambda_{\text{anal}} = 550\text{ nm}\):
\[
A_{\text{acid}} = \epsilon_{\text{HIn}} b C_T \implies \epsilon_{\text{HIn}} = \frac{A_{\text{acid}}}{b C_T}
\]
\[
A_{\text{base}} = \epsilon_{\text{In}^-} b C_T \implies \epsilon_{\text{In}^-} = \frac{A_{\text{base}}}{b C_T}
\]
At intermediate pH:
\[
A = \epsilon_{\text{HIn}} b [\text{HIn}] + \epsilon_{\text{In}^-} b [\text{In}^-]
\]
Expressing concentrations in terms of deprotonated fraction \(\alpha = \frac{[\text{In}^-]}{C_T}\):
\[
[\text{In}^-] = \alpha C_T, \quad [\text{HIn}] = (1 - \alpha) C_T
\]
\[
A = (1 - \alpha) A_{\text{acid}} + \alpha A_{\text{base}} = A_{\text{acid}} + \alpha (A_{\text{base}} - A_{\text{acid}})
\]
Rearranging for the ionization fraction \(\alpha\):
\[
\alpha = \frac{[\text{In}^-]}{C_T} = \frac{A - A_{\text{acid}}}{A_{\text{base}} - A_{\text{acid}}}
\]
The ratio of deprotonated to protonated species is:
\[
\frac{[\text{In}^-]}{[\text{HIn}]} = \frac{\alpha}{1 - \alpha} = \frac{A - A_{\text{acid}}}{A_{\text{base}} - A}
\]
Taking the base-10 logarithm and substituting into the Henderson-Hasselbalch relation:
\[
\text{pH} = \text{p}K_a + \log\left(\frac{[\text{In}^-]}{[\text{HIn}]}\right) \implies \text{p}K_a = \text{pH} - \log\left(\frac{A - A_{\text{acid}}}{A_{\text{base}} - A}\right)
\]

---

#### Step 3: Calculation of Deprotonated Fraction \(\alpha\) at \(\text{pH} = 7.20\)
Given:
\[
A = 0.612, \quad A_{\text{acid}} = 0.080, \quad A_{\text{base}} = 0.840
\]
\[
A - A_{\text{acid}} = 0.612 - 0.080 = 0.532
\]
\[
A_{\text{base}} - A = 0.840 - 0.612 = 0.228
\]
\[
\alpha_{\text{In}^-} = \frac{0.532}{0.840 - 0.080} = \frac{0.532}{0.760} = 0.700\text{ (or } 70.0\%\text{)}
\]
The concentration of \(\text{In}^-\) is \(0.700 \times 4.00 \times 10^{-5}\text{ M} = 2.80 \times 10^{-5}\text{ M}\), and \([\text{HIn}] = 1.20 \times 10^{-5}\text{ M}\).

---

#### Step 4: Extraction of Thermodynamic \(\text{p}K_a\)
Evaluating the concentration ratio:
\[
\frac{[\text{In}^-]}{[\text{HIn}]} = \frac{0.532}{0.228} \approx 2.3333
\]
\[
\log_{10}(2.3333) \approx 0.368
\]
Applying the derived formula:
\[
\text{p}K_a = 7.20 - 0.368 = 6.832 \approx 6.83
\]
The dissociation constant \(K_a\) is:
\[
K_a = 10^{-6.832} = 1.47 \times 10^{-7}\text{ M}
\]
The presence of the sharp isosbestic point confirms that this spectrophotometric method accurately extracts the thermodynamic equilibrium constant without interference."""
    }

    # Unit 7: Problem 9
    problems[7] = {
        "id": "chem-spec-u7-p9",
        "title": "Problem 9: Quantitative FRET Efficiency and Inter-Chromophore Distance in a Peptidic Biosensor",
        "difficulty": "Advanced",
        "statement": r"""A structural biochemist engineers a biosensor peptide labeled with Cyan Fluorescent Protein (CFP, donor \(D\)) at the N-terminus and Yellow Fluorescent Protein (YFP, acceptor \(A\)) at the C-terminus to monitor conformational changes upon ligand binding.

The spectral parameters of the donor-acceptor pair are:
- Donor fluorescence quantum yield in absence of acceptor: \(\Phi_D = 0.40\).
- Refractive index of aqueous buffer: \(n = 1.333\).
- Orientation factor assuming isotropic rotational averaging: \(\kappa^2 = 2/3\).
- Spectral overlap integral between donor emission and acceptor absorption: \(J(\lambda) = 1.75 \times 10^{-13}\text{ cm}^3\cdot\text{M}^{-1}\).

1. Calculate the Förster critical distance \(R_0\) (in Angstroms, \(\text{Å}\)) using the formula:
\[
R_0^6 = 8.79 \times 10^{-25} \left[\kappa^2 n^{-4} \Phi_D J(\lambda)\right] \text{ cm}^6
\]
2. Steady-state fluorescence measurements excited at \(430\text{ nm}\) (which excites CFP exclusively) reveal that the donor fluorescence intensity drops from \(F_D = 1200\text{ a.u.}\) in the absence of acceptor (cleaved peptide) to \(F_{DA} = 288\text{ a.u.}\) in the intact biosensor. Calculate the experimental energy transfer efficiency \(E\).
3. Using the distance-dependent Förster relation \(E = \frac{R_0^6}{R_0^6 + r^6}\), calculate the physical inter-chromophore distance \(r\) in \(\text{Å}\).
4. Time-correlated single photon counting (TCSPC) shows that the donor excited-state lifetime without acceptor is \(\tau_D = 2.70\text{ ns}\). Calculate the donor lifetime in the intact biosensor \(\tau_{DA}\) and the rate constant of energy transfer \(k_T\) in \(\text{s}^{-1}\).""",
        "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Calculation of Förster Critical Distance \(R_0\)
Given:
- \(\kappa^2 = 2/3 \approx 0.6667\)
- \(n = 1.333 \implies n^4 = (1.333)^4 \approx 3.1595\)
- \(\Phi_D = 0.40\)
- \(J(\lambda) = 1.75 \times 10^{-13}\text{ cm}^3\cdot\text{M}^{-1}\)

Evaluate the bracketed term:
\[
\text{Term} = \frac{\kappa^2 \Phi_D J(\lambda)}{n^4} = \frac{(0.6667) \times (0.40) \times (1.75 \times 10^{-13})}{3.1595} = \frac{4.6667 \times 10^{-14}}{3.1595} \approx 1.4770 \times 10^{-14}
\]
Now calculate \(R_0^6\):
\[
R_0^6 = (8.79 \times 10^{-25}) \times (1.4770 \times 10^{-14}) = 1.2983 \times 10^{-38}\text{ cm}^6
\]
Convert to Angstroms (\(1\text{ cm} = 10^8\text{ Å} \implies 1\text{ cm}^6 = 10^{48}\text{ Å}^6\)):
\[
R_0^6 = 1.2983 \times 10^{-38} \times 10^{48}\text{ Å}^6 = 1.2983 \times 10^{10}\text{ Å}^6
\]
Taking the 6th root:
\[
R_0 = (1.2983 \times 10^{10})^{1/6} \approx 48.7\text{ Å} = 4.87\text{ nm}
\]

---

#### Step 2: Experimental FRET Efficiency \(E\)
From steady-state donor quenching:
\[
E = 1 - \frac{F_{DA}}{F_D} = 1 - \frac{288}{1200} = 1 - 0.240 = 0.760\text{ (or } 76.0\%\text{)}
\]

---

#### Step 3: Determination of Donor-Acceptor Distance \(r\)
The Förster equation relating efficiency to distance is:
\[
E = \frac{R_0^6}{R_0^6 + r^6} \implies E (R_0^6 + r^6) = R_0^6 \implies r^6 = R_0^6 \left(\frac{1 - E}{E}\right)
\]
Substitute \(E = 0.760\):
\[
\frac{1 - E}{E} = \frac{0.240}{0.760} \approx 0.31579
\]
\[
r^6 = (1.2983 \times 10^{10}\text{ Å}^6) \times 0.31579 = 4.100 \times 10^9\text{ Å}^6
\]
Taking the 6th root:
\[
r = (4.100 \times 10^9)^{1/6} \approx 40.2\text{ Å} = 4.02\text{ nm}
\]
Because \(r < R_0\) (\(40.2\text{ Å} < 48.7\text{ Å}\)), energy transfer is highly efficient (\(>50\%\)).

---

#### Step 4: Lifetime and Kinetic Rate Constant of Transfer
Energy transfer efficiency can also be expressed in terms of donor excited-state lifetimes:
\[
E = 1 - \frac{\tau_{DA}}{\tau_D} \implies \tau_{DA} = \tau_D (1 - E)
\]
With \(\tau_D = 2.70\text{ ns}\):
\[
\tau_{DA} = 2.70\text{ ns} \times (1 - 0.760) = 2.70\text{ ns} \times 0.240 = 0.648\text{ ns}
\]
The rate constant of dipole-dipole energy transfer \(k_T\) is:
\[
k_T = \frac{1}{\tau_D} \left(\frac{R_0}{r}\right)^6 = \frac{1}{\tau_D} \left(\frac{E}{1 - E}\right)
\]
Using \(\tau_D = 2.70 \times 10^{-9}\text{ s}\):
\[
k_T = \frac{1}{2.70 \times 10^{-9}\text{ s}} \times \left(\frac{0.760}{0.240}\right) = (3.704 \times 10^8\text{ s}^{-1}) \times 3.1667 \approx 1.173 \times 10^9\text{ s}^{-1}
\]
Alternatively, from kinetic competition:
\[
\frac{1}{\tau_{DA}} = \frac{1}{\tau_D} + k_T \implies k_T = \frac{1}{0.648 \times 10^{-9}} - \frac{1}{2.70 \times 10^{-9}} = 1.543 \times 10^9 - 0.370 \times 10^9 = 1.173 \times 10^9\text{ s}^{-1}
\]
This demonstrates the power of FRET as a "spectroscopic ruler" operating on the nanometer scale."""
    }

    # Unit 8: Problem 9
    problems[8] = {
        "id": "chem-spec-u8-p9",
        "title": "Problem 9: Dynamic NMR Coalescence and Activation Free Energy of Amide Bond Rotation",
        "difficulty": "Advanced",
        "statement": r"""In \(N,N\)-dimethylformamide (\(\text{DMF}\)), the partial double-bond character of the central \(\text{C-N}\) bond hinders rotation of the dimethylamino group. At low temperatures, the two methyl groups are diastereotopic (one *cis* to carbonyl oxygen, one *trans*), appearing in the \(^1\text{H}\) NMR spectrum as two sharp singlets.

On a \(500\text{ MHz}\) spectrometer (\(\nu_0 = 500.13\text{ MHz}\)):
- In the slow exchange regime at \(T = 280\text{ K}\), the two methyl singlets appear at chemical shifts \(\delta_A = 2.97\text{ ppm}\) and \(\delta_B = 2.79\text{ ppm}\).
- Upon heating, the two peaks broaden, merge, and reach the coalescence temperature at \(T_c = 385\text{ K}\) (\(112^\circ\text{C}\)).

1. Calculate the frequency separation \(\Delta\nu\) (in Hz) between the two methyl peaks in the slow-exchange limit.
2. Calculate the first-order unimolecular forward rate constant of exchange \(k_c\) at coalescence using the Gutowsky-Holm relation \(k_c = \frac{\pi \Delta\nu}{\sqrt{2}}\).
3. Using the Eyring equation, calculate the activation free energy \(\Delta G^\ddagger\) for rotation around the \(\text{C-N}\) bond at \(T_c = 385\text{ K}\) (given Planck's constant \(h = 6.62607 \times 10^{-34}\text{ J}\cdot\text{s}\), Boltzmann constant \(k_B = 1.38065 \times 10^{-23}\text{ J/K}\), gas constant \(R = 8.3145\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}\), transmission coefficient \(\kappa = 1\)).
4. Predict what the coalescence temperature \(T_c\) would have been if the spectrum had instead been acquired on a lower-field \(100\text{ MHz}\) spectrometer, and explain the physical origin of the field dependence of \(T_c\) in dynamic NMR.""" ,
        "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Chemical Shift Separation in Hz
The chemical shift separation in ppm is:
\[
\Delta\delta = \delta_A - \delta_B = 2.97\text{ ppm} - 2.79\text{ ppm} = 0.18\text{ ppm}
\]
At an operating frequency of \(500.13\text{ MHz}\):
\[
\Delta\nu = \Delta\delta \times \nu_0 = 0.18 \times 10^{-6} \times 500.13 \times 10^6\text{ Hz} = 90.02\text{ Hz}
\]

---

#### Step 2: Exchange Rate Constant \(k_c\) at Coalescence
For an uncoupled two-site mutual exchange system with equal populations (\(p_A = p_B = 0.5\)), the rate constant at coalescence is given by the Gutowsky-Holm formula:
\[
k_c = \frac{\pi \Delta\nu}{\sqrt{2}}
\]
Substituting \(\Delta\nu = 90.02\text{ Hz}\):
\[
k_c = \frac{\pi \times 90.02}{1.41421} = \frac{282.81}{1.41421} \approx 199.98\text{ s}^{-1} \approx 200.0\text{ s}^{-1}
\]
The lifetime of a methyl group in a specific rotamer site at coalescence is:
\[
\tau_c = \frac{1}{k_c} \approx 5.0 \times 10^{-3}\text{ s} = 5.0\text{ ms}
\]

---

#### Step 3: Calculation of Free Energy of Activation \(\Delta G^\ddagger\)
The Eyring transition state equation is:
\[
k = \kappa \frac{k_B T}{h} \exp\left(-\frac{\Delta G^\ddagger}{R T}\right)
\]
Setting \(\kappa = 1\) and solving for \(\Delta G^\ddagger\) at \(T = T_c\):
\[
\Delta G^\ddagger = R T_c \ln\left(\frac{k_B T_c}{h k_c}\right)
\]
Calculate the pre-exponential factor at \(T_c = 385\text{ K}\):
\[
\frac{k_B T_c}{h} = \frac{(1.38065 \times 10^{-23}\text{ J/K})(385\text{ K})}{6.62607 \times 10^{-34}\text{ J}\cdot\text{s}} = \frac{5.3155 \times 10^{-21}}{6.62607 \times 10^{-34}} \approx 8.022 \times 10^{12}\text{ s}^{-1}
\]
Now evaluate the ratio:
\[
\frac{k_B T_c}{h k_c} = \frac{8.022 \times 10^{12}\text{ s}^{-1}}{200.0\text{ s}^{-1}} = 4.011 \times 10^{10}
\]
Taking the natural logarithm:
\[
\ln(4.011 \times 10^{10}) \approx 24.415
\]
Now calculate \(\Delta G^\ddagger\):
\[
\Delta G^\ddagger = (8.3145\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}) \times (385\text{ K}) \times 24.415 = 3201.08 \times 24.415 \approx 78155\text{ J/mol} \approx 78.2\text{ kJ/mol}
\]
(or in kcal/mol: \(78.16 / 4.184 \approx 18.7\text{ kcal/mol}\)).
This \(\sim 78\text{ kJ/mol}\) barrier matches the canonical value for the partial \(\pi\)-bond resonance character of the peptide/amide linkage (\(\text{O=C}-\ddot{\text{N}} \leftrightarrow {}^-\text{O}-\text{C}=\text{N}^+\)).

---

#### Step 4: Frequency Field Dependence of Coalescence Temperature
On a \(100\text{ MHz}\) spectrometer, the frequency separation is:
\[
\Delta\nu_{100} = 0.18\text{ ppm} \times 100\text{ MHz} = 18.0\text{ Hz}
\]
The required rate constant at coalescence on the \(100\text{ MHz}\) spectrometer is:
\[
k_c(100) = \frac{\pi \times 18.0}{\sqrt{2}} \approx 40.0\text{ s}^{-1}
\]
Since the rate constant must only reach \(40\text{ s}^{-1}\) rather than \(200\text{ s}^{-1}\), coalescence occurs at a **lower temperature**.
Assuming \(\Delta S^\ddagger \approx 0 \implies \Delta H^\ddagger \approx \Delta G^\ddagger \approx 78.2\text{ kJ/mol}\):
Using the ratio of rates:
\[
\frac{k_c(385)}{k_c(T_{c, 100})} = \frac{200}{40} = 5.0 = \exp\left[\frac{\Delta H^\ddagger}{R}\left(\frac{1}{T_{c,100}} - \frac{1}{385}\right)\right]
\]
\[
\ln(5.0) = 1.6094 = \frac{78200}{8.3145} \left(\frac{1}{T_{c,100}} - \frac{1}{385}\right) = 9405 \left(\frac{1}{T_{c,100}} - 0.0025974\right)
\]
\[
\frac{1}{T_{c,100}} = 0.0025974 + \frac{1.6094}{9405} = 0.0025974 + 0.0001711 = 0.0027685\text{ K}^{-1}
\]
\[
T_{c, 100} = \frac{1}{0.0027685} \approx 361.2\text{ K} \approx 88.1^\circ\text{C}
\]
Hence, on a lower-field instrument, coalescence occurs at \(88^\circ\text{C}\) compared to \(112^\circ\text{C}\) at \(500\text{ MHz}\). Coalescence temperature is inherently instrument-dependent because the NMR timescale (\(\Delta\nu^{-1}\)) is inversely proportional to \(B_0\)."""
    }

    # Unit 9: Problem 9
    problems[9] = {
        "id": "chem-spec-u9-p9",
        "title": "Problem 9: Complete Natural Product Structural Assignment via HSQC and HMBC Correlations",
        "difficulty": "Advanced",
        "statement": r"""A marine bioactive metabolite of molecular formula \(\text{C}_9\text{H}_{10}\text{O}_3\) has been isolated and analyzed by 1D and 2D NMR spectroscopy:

**1D \(^1\text{H}\) NMR (\(500\text{ MHz}, \text{CDCl}_3\)):**
- \(\delta 9.85\) (1H, s, sharp)
- \(\delta 7.82\) (2H, d, \(J = 8.8\text{ Hz}\))
- \(\delta 6.98\) (2H, d, \(J = 8.8\text{ Hz}\))
- \(\delta 3.89\) (3H, s)
- \(\delta 2.61\) (2H, q, \(J = 7.5\text{ Hz}\)) - wait, check degrees of unsaturation: \(\text{C}_9\text{H}_{10}\text{O}_3 \implies \text{DBE} = 9 - 10/2 + 1 = 5\).
Let the observed resonances be:
- \(\delta 9.86\) (1H, s)
- \(\delta 7.81\) (2H, d, \(J = 8.7\text{ Hz}\))
- \(\delta 6.99\) (2H, d, \(J = 8.7\text{ Hz}\))
- \(\delta 4.14\) (2H, q, \(J = 7.0\text{ Hz}\))
- \(\delta 1.45\) (3H, t, \(J = 7.0\text{ Hz}\))

**1D \(^{13}\text{C}\) NMR / DEPT-135:**
- C1: \(\delta 190.8\) (CH)
- C2: \(\delta 164.2\) (C, quaternary)
- C3: \(\delta 132.0\) (2 \(\times\) CH)
- C4: \(\delta 129.8\) (C, quaternary)
- C5: \(\delta 114.8\) (2 \(\times\) CH)
- C6: \(\delta 63.9\) (\(\text{CH}_2\))
- C7: \(\delta 14.7\) (\(\text{CH}_3\))

1. Calculate the Double Bond Equivalents (Degrees of Unsaturation) and assign each carbon to its directly attached protons using HSQC.
2. The HMBC experiment shows key long-range \(^2J_{\text{CH}}\) and \(^3J_{\text{CH}}\) correlations:
   - Proton \(\delta 9.86\) correlates with C4 (\(\delta 129.8\)) and C3 (\(\delta 132.0\)).
   - Protons \(\delta 7.81\) correlate with C1 (\(\delta 190.8\)), C2 (\(\delta 164.2\)), and C5 (\(\delta 114.8\)).
   - Protons \(\delta 6.99\) correlate with C4 (\(\delta 129.8\)) and C2 (\(\delta 164.2\)).
   - Protons \(\delta 4.14\) correlate with C2 (\(\delta 164.2\)) and C7 (\(\delta 14.7\)).
   - Protons \(\delta 1.45\) correlate with C6 (\(\delta 63.9\)).
3. Reconstruct the complete constitutional connectivity of the molecule step-by-step and provide its IUPAC name.
4. Explain how HMBC distinguishes whether the ethoxy group (\(-\text{OCH}_2\text{CH}_3\)) is attached directly to the aromatic ring vs as an ethyl ester, noting the characteristic differences in chemical shift and correlation topology.""" ,
        "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Degrees of Unsaturation and Direct HSQC Assignments
For \(\text{C}_9\text{H}_{10}\text{O}_3\):
\[
\text{DBE} = C - \frac{H}{2} + \frac{N}{2} + 1 = 9 - \frac{10}{2} + 0 + 1 = 9 - 5 + 1 = 5
\]
Five degrees of unsaturation indicate a benzene ring (4 unsaturations: 3 \(\pi\)-bonds + 1 ring) plus one carbonyl group (1 \(\pi\)-bond).

**Direct One-Bond (\(^1J_{\text{CH}}\)) HSQC Assignments:**
- Formyl proton \(\delta 9.86\) (1H, s) \(\rightarrow\) C1 (\(\delta 190.8\), \(\text{CH}\))
- Aromatic protons \(\delta 7.81\) (2H, d) \(\rightarrow\) C3 (\(\delta 132.0\), \(2 \times \text{CH}\))
- Aromatic protons \(\delta 6.99\) (2H, d) \(\rightarrow\) C5 (\(\delta 114.8\), \(2 \times \text{CH}\))
- Oxymethylene protons \(\delta 4.14\) (2H, q) \(\rightarrow\) C6 (\(\delta 63.9\), \(\text{CH}_2\))
- Methyl protons \(\delta 1.45\) (3H, t) \(\rightarrow\) C7 (\(\delta 14.7\), \(\text{CH}_3\))
Quaternary carbons with no HSQC cross-peaks:
- C2 (\(\delta 164.2\))
- C4 (\(\delta 129.8\))

---

#### Step 2: HMBC Network Analysis
HMBC detects \(^2J_{\text{CH}}\) and \(^3J_{\text{CH}}\) (rarely \(^4J\) across aromatic rings) heteronuclear couplings:
1. **Formyl group (\(-\text{CHO}\)):**
   - The formyl proton at \(\delta 9.86\) shows \(^2J\) correlation to C4 (\(\delta 129.8\)) and \(^3J\) correlation to C3 (\(\delta 132.0\)).
   - This proves the \(\text{CHO}\) group is directly attached to the aromatic ring at quaternary carbon C4.
2. **Aromatic Spin System:**
   - The two symmetrical 2H doublets with \(J = 8.7\text{ Hz}\) (\(\delta 7.81\) and \(\delta 6.99\)) form a classic \(\text{AA}'\text{XX}'\) pattern characteristic of a 1,4-disubstituted (para-substituted) benzene ring.
   - Protons at \(\delta 7.81\) (ortho to the electron-withdrawing carbonyl group) correlate via \(^3J\) to the carbonyl carbon C1 (\(\delta 190.8\)), unambiguously placing them at positions 3 and 5 adjacent to C4.
   - Protons at \(\delta 6.99\) (ortho to the electron-donating oxygen) correlate via \(^2J\) to C2 (\(\delta 164.2\)) and \(^3J\) to C4 (\(\delta 129.8\)).
3. **Ethoxy Group (\(-\text{OCH}_2\text{CH}_3\)):**
   - Protons at \(\delta 1.45\) (\(\text{CH}_3\)) couple via \(^3J_{\text{HH}}\) to \(\delta 4.14\) (\(\text{CH}_2\)) and exhibit HMBC correlation to C6 (\(\delta 63.9\)).
   - Crucially, the oxymethylene protons at \(\delta 4.14\) show a strong \(^3J_{\text{CH}}\) HMBC correlation to aromatic carbon C2 at \(\delta 164.2\).

---

#### Step 3: Complete Connectivity Assembly and IUPAC Name
Assembling the fragments:
- Fragment A: Formyl group \(-\text{CHO}\) (C1)
- Fragment B: 1,4-phenylene core (\(-\text{C}_6\text{H}_4-\), C2, C3, C4, C5)
- Fragment C: Ethoxy group \(-\text{O}-\text{CH}_2\text{CH}_3\) (C6, C7)
Connecting them:
- C1 is attached to C4 of the benzene ring.
- Oxygen is attached to C2 of the benzene ring and to C6 of the ethyl group.
Thus, the compound is:
\[
\text{4-ethoxybenzaldehyde}\quad (\text{also known as } p\text{-ethoxybenzaldehyde})
\]

---

#### Step 4: Disambiguation from Isomeric Ethyl Esters
If the molecule were an ethyl ester (such as ethyl 4-hydroxybenzoate, which also has formula \(\text{C}_9\text{H}_{10}\text{O}_3\)):
1. In an ethyl ester, the ester carbonyl carbon appears at \(\delta 166 - 170\text{ ppm}\), rather than an aldehyde carbonyl at \(\delta 190.8\text{ ppm}\).
2. The ester carbonyl would show a strong \(^3J_{\text{CH}}\) HMBC correlation to the oxymethylene protons (\(-\text{COOCH}_2\text{CH}_3\)). In our experimental data, the oxymethylene protons (\(\delta 4.14\)) correlate to the aromatic carbon at \(\delta 164.2\), not to the carbonyl carbon at \(\delta 190.8\).
3. The aldehyde proton singlet at \(\delta 9.86\) is entirely absent in an ethyl ester (which would instead show a phenolic \(-\text{OH}\) singlet).
Hence, HMBC connectivity firmly rules out the isomeric ester and unequivocally establishes 4-ethoxybenzaldehyde."""
    }

    # Unit 10: Problem 9
    problems[10] = {
        "id": "chem-spec-u10-p9",
        "title": "Problem 9: Temperature-Dependent Mössbauer Spectroscopy of High-Spin vs Low-Spin Spin-Crossover (SCO)",
        "difficulty": "Advanced",
        "statement": r"""An iron(II) coordination complex \([\text{Fe}(\text{phen})_2(\text{NCS})_2]\) (where phen = 1,10-phenanthroline) exhibits a thermally induced spin-crossover (SCO) transition between a diamagnetic low-spin (\(\text{LS}, S = 0\)) state and a paramagnetic high-spin (\(\text{HS}, S = 2\)) state.

\(^{57}\text{Fe}\) Mössbauer spectra acquired using a \(^{57}\text{Co}(\text{Rh})\) source at two temperatures reveal:
- At \(T = 77\text{ K}\): A single quadrupole doublet with isomer shift \(\delta_{\text{LS}} = 0.38\text{ mm/s}\) and quadrupole splitting \(\Delta E_{Q,\text{LS}} = 0.35\text{ mm/s}\).
- At \(T = 298\text{ K}\): A distinct quadrupole doublet with isomer shift \(\delta_{\text{HS}} = 1.05\text{ mm/s}\) and quadrupole splitting \(\Delta E_{Q,\text{HS}} = 2.68\text{ mm/s}\).

1. Write the electronic configuration for the \(\text{Fe}^{2+}\) ion (\(3d^6\)) in an octahedral ligand field in both the low-spin (\(^1A_{1g}\)) and high-spin (\(^5T_{2g}\)) states.
2. Explain physically why the isomer shift \(\delta\) is significantly larger for the high-spin state (\(1.05\text{ mm/s}\)) than for the low-spin state (\(0.38\text{ mm/s}\)) in terms of \(s\)-electron density at the nucleus \(|\psi_s(0)|^2\) and \(d\)-electron shielding.
3. Explain why the quadrupole splitting \(\Delta E_Q\) is massive in the high-spin state (\(2.68\text{ mm/s}\)) while small in the low-spin state (\(0.35\text{ mm/s}\)) in terms of electric field gradient (EFG) contributions from the valence \(d\)-electrons (\(q_{\text{val}}\)) vs the ligand lattice (\(q_{\text{lat}}\)).
4. At an intermediate temperature \(T = 175\text{ K}\), both doublets are observed simultaneously with integrated peak area ratio \(\frac{A_{\text{HS}}}{A_{\text{LS}}} = 1.25\). Assuming identical recoil-free Lamb-Mössbauer factors (\(f_{\text{HS}} \approx f_{\text{LS}}\)), calculate the high-spin mole fraction \(\gamma_{\text{HS}}\) and evaluate the equilibrium constant \(K_{\text{eq}} = \frac{[\text{HS}]}{[\text{LS}]}\) and \(\Delta G^\circ\) of the spin crossover transition at \(175\text{ K}\).""",
        "solution": r"""### Comprehensive Multi-Step Solution:

#### Step 1: Electronic Configurations of \(\text{Fe}^{2+}\) (\(3d^6\))
In an octahedral ligand field:
- **Low-spin (LS) state (\(S = 0\), diamagnetic):**
  Strong ligand field (\(\Delta_o > P\), pairing energy):
  \[
  t_{2g}^6 e_g^0 \implies {}^1A_{1g}
  \]
  All six \(3d\) electrons pair in the lower-energy \(t_{2g}\) orbitals (\(d_{xy}^2 d_{yz}^2 d_{xz}^2\)).
- **High-spin (HS) state (\(S = 2\), paramagnetic):**
  Weaker ligand field (\(\Delta_o < P\)):
  \[
  t_{2g}^4 e_g^2 \implies {}^5T_{2g}
  \]
  Four unpaired electrons: \(t_{2g}\) has four electrons (one pair, two parallel), and \(e_g\) has two electrons (\(d_{z^2}^1 d_{x^2-y^2}^1\)).

---

#### Step 2: Physical Origin of the Isomer Shift Disparity
The Mössbauer isomer shift relative to the source is:
\[
\delta = \frac{2\pi}{3} Z e^2 [\langle r^2 \rangle_{\text{exc}} - \langle r^2 \rangle_{\text{gnd}}] \left(|\psi_s(0)|_{\text{absorber}}^2 - |\psi_s(0)|_{\text{source}}^2\right)
\]
For \(^{57}\text{Fe}\), the nuclear radius shrinks upon excitation:
\[
\Delta \langle r^2 \rangle = \langle r^2 \rangle_{\text{exc}} - \langle r^2 \rangle_{\text{gnd}} < 0
\]
Therefore, an **increase** in \(s\)-electron density at the iron nucleus \(|\psi_s(0)|^2\) causes a **decrease** in the isomer shift \(\delta\).

Comparing LS and HS:
- In \(\text{LS Fe}^{2+}\) (\(t_{2g}^6\)), the \(e_g^*\) antibonding orbitals are completely empty. Strong \(\sigma\)-donation from the phenanthroline and thiocyanate ligands into empty \(e_g\) metal orbitals, combined with strong \(\pi\)-backdonation from filled \(t_{2g}\) into vacant ligand \(\pi^*\) orbitals, significantly delocalizes \(d\)-electron density away from the iron center.
- In \(\text{HS Fe}^{2+}\) (\(t_{2g}^4 e_g^2\)), the antibonding \(e_g^*\) orbitals are populated, causing elongated \(\text{Fe-N}\) bonds (by \(\sim 0.2\text{ Å}\)), weaker ligand donation, and concentrated non-bonding \(d\)-electrons around the iron nucleus.
- These localized \(3d\) electrons exert strong shielding against the inner \(3s\) electrons, reducing \(|\psi_{3s}(0)|^2\) at the iron nucleus.
- Lower \(|\psi_s(0)|^2\) in the HS state directly produces a much higher isomer shift:
  \[
  \delta_{\text{HS}} = 1.05\text{ mm/s} \gg \delta_{\text{LS}} = 0.38\text{ mm/s}
  \]

---

#### Step 3: Origin of Quadrupole Splitting Disparity
The quadrupole splitting is:
\[
\Delta E_Q = \frac{1}{2} e Q V_{zz} \sqrt{1 + \frac{\eta^2}{3}}
\]
where the principal electric field gradient (EFG) tensor component is:
\[
V_{zz} = (1 - R) q_{\text{val}} + (1 - \gamma_\infty) q_{\text{lat}}
\]
- **Low-spin \(\text{Fe}^{2+}\) (\(t_{2g}^6\)):**
  The \(t_{2g}\) subshell is completely filled with six electrons. Its charge distribution is closed-shell cubic and spherically symmetric:
  \[
  q_{\text{val}} \propto \left(-n_{d_{xy}} - n_{d_{xz}} + 2n_{d_{yz}} \dots \right) = 0
  \]
  The only EFG arises from the small rhombic distortion of the ligand coordination sphere (\(q_{\text{lat}}\)). Consequently, \(\Delta E_{Q,\text{LS}} = 0.35\text{ mm/s}\) is very small.
- **High-spin \(\text{Fe}^{2+}\) (\(t_{2g}^4 e_g^2\)):**
  The \(t_{2g}\) subshell has an asymmetrical occupancy (\(d_{xy}^2 d_{yz}^1 d_{xz}^1\)). The single extra electron in one of the \(t_{2g}\) orbitals generates a massive non-zero valence electron field gradient:
  \[
  q_{\text{val}} = \frac{4}{7} \langle r^{-3} \rangle_{3d} \neq 0
  \]
  This produces a huge electric field gradient at the \(^{57}\text{Fe}\) nucleus, yielding the massive quadrupole splitting \(\Delta E_{Q,\text{HS}} = 2.68\text{ mm/s}\).

---

#### Step 4: Equilibrium Thermodynamics at \(T = 175\text{ K}\)
Assuming equal recoilless fractions (\(f_{\text{HS}} \approx f_{\text{LS}}\)), the spectral area ratio equals the concentration ratio:
\[
K_{\text{eq}} = \frac{[\text{HS}]}{[\text{LS}]} = \frac{A_{\text{HS}}}{A_{\text{LS}}} = 1.25
\]
The high-spin mole fraction \(\gamma_{\text{HS}}\) is:
\[
\gamma_{\text{HS}} = \frac{[\text{HS}]}{[\text{HS}] + [\text{LS}]} = \frac{K_{\text{eq}}}{1 + K_{\text{eq}}} = \frac{1.25}{1 + 1.25} = \frac{1.25}{2.25} \approx 0.5556\text{ (or } 55.6\%\text{)}
\]
The standard Gibbs free energy change of the spin-crossover transition at \(175\text{ K}\) is:
\[
\Delta G^\circ = -R T \ln K_{\text{eq}} = -(8.3145\text{ J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}) \times (175\text{ K}) \times \ln(1.25)
\]
\[
\ln(1.25) \approx 0.22314
\]
\[
\Delta G^\circ = -1455.04 \times 0.22314 \approx -324.7\text{ J/mol} = -0.325\text{ kJ/mol}
\]
Because \(\Delta G^\circ \approx 0\), \(175\text{ K}\) is extremely close to the critical spin-crossover transition temperature \(T_{1/2}\) (where \([\text{HS}] = [\text{LS}] \implies K_{\text{eq}} = 1\))."""
    }

    return problems

if __name__ == "__main__":
    problems = get_unit_problems9()
    print(f"Generated Problem 9 for {len(problems)} units.")
    for u, p in sorted(problems.items()):
        print(f"Unit {u}: {p['title']}")
